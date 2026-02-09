"""
Batch router: multi-SKU bulk image generation.

Flow:
1. POST /api/batch/upload — upload CSV + ZIP of images → preview
2. POST /api/batch/{id}/start — confirm → deduct credits → enqueue
3. GET /api/batch/{id}/status — check progress
4. GET /api/batch/{id}/download — download all results as ZIP
"""

from __future__ import annotations

import csv
import io
import uuid
import zipfile
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.config import CREDIT_PER_IMAGE, OUTPUT_DIR, UPLOAD_DIR
from app.database import get_db
from app.models.db_models import Batch, BatchItem, User
from app.services import credit_service

router = APIRouter(prefix="/api/batch", tags=["batch"])


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------

class BatchItemPreview(BaseModel):
    sku_name: str
    product_type: str
    style: str | None
    image_filename: str
    estimated_credits: int


class BatchPreviewResponse(BaseModel):
    batch_id: str
    total_skus: int
    total_credits: int
    items: list[BatchItemPreview]
    errors: list[str]


class BatchStatusResponse(BaseModel):
    batch_id: str
    status: str
    total_skus: int
    completed_skus: int
    total_credits: int
    error_message: str | None
    items: list[BatchItemStatus]


class BatchItemStatus(BaseModel):
    sku_name: str
    product_type: str
    status: str
    job_id: str | None
    error: str | None


# ---------------------------------------------------------------------------
# Valid product types for validation
# ---------------------------------------------------------------------------

VALID_PRODUCT_TYPES = {
    "bags", "jewelry", "clothing", "shoes", "electronics",
    "beauty", "home", "toys", "sports", "food",
    "stationery", "pets", "automotive", "phones", "travel",
    "fashion_acc", "kitchenware", "health", "hobbies", "motorcycle",
}

# Default images per SKU (common templates count)
IMAGES_PER_SKU = 9


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/upload", response_model=BatchPreviewResponse)
async def batch_upload(
    csv_file: UploadFile = File(...),
    zip_file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Upload CSV + ZIP to create a batch preview.

    CSV format: sku_name,product_type,style (header row required)
    ZIP contains image files referenced in CSV's sku_name (e.g., sku1.jpg)
    """
    # Read CSV
    csv_content = (await csv_file.read()).decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(csv_content))

    errors: list[str] = []
    items_preview: list[BatchItemPreview] = []
    sku_rows: list[dict] = []

    # Read ZIP to get available filenames
    zip_content = await zip_file.read()
    try:
        with zipfile.ZipFile(io.BytesIO(zip_content)) as zf:
            zip_filenames = set(zf.namelist())
    except zipfile.BadZipFile:
        raise HTTPException(status_code=400, detail="無效的 ZIP 檔案")

    for i, row in enumerate(reader, start=2):  # start=2 because row 1 is header
        sku_name = (row.get("sku_name") or "").strip()
        product_type = (row.get("product_type") or "").strip()
        style = (row.get("style") or "").strip() or None

        if not sku_name:
            errors.append(f"第 {i} 行：缺少 sku_name")
            continue
        if not product_type:
            errors.append(f"第 {i} 行：缺少 product_type")
            continue
        if product_type not in VALID_PRODUCT_TYPES:
            errors.append(f"第 {i} 行：無效的 product_type '{product_type}'")
            continue

        # Look for image in ZIP (try common extensions)
        image_filename = None
        for ext in [".jpg", ".jpeg", ".png", ".webp"]:
            candidate = f"{sku_name}{ext}"
            if candidate in zip_filenames:
                image_filename = candidate
                break
            # Also try inside a subfolder
            for zname in zip_filenames:
                if zname.endswith(f"/{sku_name}{ext}") or zname == f"{sku_name}{ext}":
                    image_filename = zname
                    break
            if image_filename:
                break

        if not image_filename:
            errors.append(f"第 {i} 行：ZIP 中找不到 SKU '{sku_name}' 的圖片")
            continue

        sku_rows.append({
            "sku_name": sku_name,
            "product_type": product_type,
            "style": style,
            "image_filename": image_filename,
        })
        items_preview.append(BatchItemPreview(
            sku_name=sku_name,
            product_type=product_type,
            style=style,
            image_filename=image_filename,
            estimated_credits=IMAGES_PER_SKU,
        ))

    if not sku_rows:
        raise HTTPException(
            status_code=400,
            detail=f"CSV 中沒有有效的 SKU 資料。錯誤：{'; '.join(errors) if errors else '空白 CSV'}",
        )

    total_credits = len(sku_rows) * IMAGES_PER_SKU

    # Create batch record
    batch_id = uuid.uuid4().hex[:12]
    batch = Batch(
        id=batch_id,
        user_id=user.id,
        status="pending",
        total_skus=len(sku_rows),
        total_credits=total_credits,
        csv_data=csv_content,
    )
    db.add(batch)

    # Extract images from ZIP and save
    batch_upload_dir = UPLOAD_DIR / f"batch_{batch_id}"
    batch_upload_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(io.BytesIO(zip_content)) as zf:
        for row in sku_rows:
            image_data = zf.read(row["image_filename"])
            save_path = batch_upload_dir / Path(row["image_filename"]).name
            save_path.write_bytes(image_data)

            item = BatchItem(
                batch_id=batch_id,
                sku_name=row["sku_name"],
                product_type=row["product_type"],
                style=row["style"],
                image_filename=row["image_filename"],
                image_path=str(save_path),
                status="pending",
            )
            db.add(item)

    await db.commit()

    return BatchPreviewResponse(
        batch_id=batch_id,
        total_skus=len(sku_rows),
        total_credits=total_credits,
        items=items_preview,
        errors=errors,
    )


@router.post("/{batch_id}/start")
async def batch_start(
    batch_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Confirm and start batch generation. Deducts credits first."""
    result = await db.execute(
        select(Batch).where(Batch.id == batch_id, Batch.user_id == user.id)
    )
    batch = result.scalar_one_or_none()
    if not batch:
        raise HTTPException(status_code=404, detail="批量任務未找到")
    if batch.status != "pending":
        raise HTTPException(status_code=400, detail=f"批量任務狀態為 {batch.status}，無法啟動")

    # Check & charge credits
    has_balance = await credit_service.check_balance(db, user.id, batch.total_credits)
    if not has_balance:
        balance = await credit_service.get_balance(db, user.id)
        raise HTTPException(
            status_code=402,
            detail=f"點數不足：需要 {batch.total_credits} 點，目前餘額 {balance} 點",
        )

    await credit_service.charge_credits(
        db, user.id, batch.total_credits,
        description=f"批量生成 {batch.total_skus} 個 SKU（{batch.total_credits} 張圖片）",
    )

    # Update batch status
    await db.execute(
        update(Batch).where(Batch.id == batch_id).values(status="confirmed")
    )
    await db.commit()

    # Enqueue batch processing in background
    import asyncio
    asyncio.create_task(_process_batch(batch_id))

    return {
        "batch_id": batch_id,
        "status": "confirmed",
        "message": f"已確認，{batch.total_skus} 個 SKU 開始排隊生成",
    }


@router.get("/{batch_id}/status", response_model=BatchStatusResponse)
async def batch_status(
    batch_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Get batch processing status."""
    result = await db.execute(
        select(Batch).where(Batch.id == batch_id, Batch.user_id == user.id)
    )
    batch = result.scalar_one_or_none()
    if not batch:
        raise HTTPException(status_code=404, detail="批量任務未找到")

    items = [
        BatchItemStatus(
            sku_name=item.sku_name,
            product_type=item.product_type,
            status=item.status,
            job_id=item.job_id,
            error=item.error,
        )
        for item in (batch.items or [])
    ]

    return BatchStatusResponse(
        batch_id=batch.id,
        status=batch.status,
        total_skus=batch.total_skus,
        completed_skus=batch.completed_skus,
        total_credits=batch.total_credits,
        error_message=batch.error_message,
        items=items,
    )


@router.get("/{batch_id}/download")
async def batch_download(
    batch_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Download all batch results as a ZIP organized by SKU."""
    result = await db.execute(
        select(Batch).where(Batch.id == batch_id, Batch.user_id == user.id)
    )
    batch = result.scalar_one_or_none()
    if not batch:
        raise HTTPException(status_code=404, detail="批量任務未找到")

    if batch.status not in ("completed", "partial"):
        raise HTTPException(status_code=400, detail="批量任務尚未完成")

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in (batch.items or []):
            if item.job_id and item.status == "completed":
                # Find generated images for this job
                task_output_dir = OUTPUT_DIR / item.job_id
                if task_output_dir.exists():
                    for img_file in task_output_dir.glob("*.png"):
                        if "_v" not in img_file.name:  # Skip variants
                            arcname = f"{item.sku_name}/{img_file.name}"
                            zf.write(img_file, arcname)

    buf.seek(0)
    return StreamingResponse(
        buf,
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename=batch_{batch_id}.zip",
        },
    )


# ---------------------------------------------------------------------------
# Background batch processing
# ---------------------------------------------------------------------------

async def _process_batch(batch_id: str) -> None:
    """Process all SKUs in a batch sequentially."""
    import logging
    from app.database import AsyncSessionLocal
    from app.services import generation_service

    logger = logging.getLogger("app.batch")

    try:
        async with AsyncSessionLocal() as db:
            # Mark as running
            await db.execute(
                update(Batch).where(Batch.id == batch_id).values(status="running")
            )
            await db.commit()

            # Load batch and items
            result = await db.execute(select(Batch).where(Batch.id == batch_id))
            batch = result.scalar_one_or_none()
            if not batch:
                return

            completed = 0
            for item in (batch.items or []):
                try:
                    # Update item status
                    await db.execute(
                        update(BatchItem)
                        .where(BatchItem.id == item.id)
                        .values(status="running")
                    )
                    await db.commit()

                    # Create generation task for this SKU
                    image_path = Path(item.image_path) if item.image_path else None
                    if not image_path or not image_path.exists():
                        await db.execute(
                            update(BatchItem)
                            .where(BatchItem.id == item.id)
                            .values(status="failed", error="圖片檔案未找到")
                        )
                        await db.commit()
                        continue

                    task = generation_service.create_task(
                        image_path=image_path,
                        product_type=item.product_type,
                        style=item.style,
                        user_id=batch.user_id,
                    )
                    await generation_service.persist_task_to_db(task)

                    # Update batch item with job_id
                    await db.execute(
                        update(BatchItem)
                        .where(BatchItem.id == item.id)
                        .values(job_id=task.task_id)
                    )
                    await db.commit()

                    # Run generation (consume the async generator)
                    async for _event in generation_service.run_generation(task.task_id):
                        pass  # Just drive it to completion

                    # Check result
                    final_task = generation_service.get_task(task.task_id)
                    if final_task and final_task.status in ("completed", "partial"):
                        completed += 1
                        await db.execute(
                            update(BatchItem)
                            .where(BatchItem.id == item.id)
                            .values(status="completed")
                        )
                    else:
                        await db.execute(
                            update(BatchItem)
                            .where(BatchItem.id == item.id)
                            .values(status="failed", error="生成失敗")
                        )

                    # Update batch progress
                    await db.execute(
                        update(Batch)
                        .where(Batch.id == batch_id)
                        .values(completed_skus=completed)
                    )
                    await db.commit()

                except Exception as e:
                    logger.error(f"Batch item {item.sku_name} failed: {e}")
                    await db.execute(
                        update(BatchItem)
                        .where(BatchItem.id == item.id)
                        .values(status="failed", error=str(e))
                    )
                    await db.commit()

            # Final batch status
            final_status = "completed" if completed == batch.total_skus else (
                "partial" if completed > 0 else "failed"
            )
            await db.execute(
                update(Batch)
                .where(Batch.id == batch_id)
                .values(status=final_status, completed_skus=completed)
            )
            await db.commit()
            logger.info(f"Batch {batch_id} finished: {final_status} ({completed}/{batch.total_skus})")

    except Exception as e:
        logger.error(f"Batch {batch_id} processing error: {e}")
        try:
            async with AsyncSessionLocal() as db:
                await db.execute(
                    update(Batch)
                    .where(Batch.id == batch_id)
                    .values(status="failed", error_message=str(e))
                )
                await db.commit()
        except Exception:
            pass
