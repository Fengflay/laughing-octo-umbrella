from __future__ import annotations

import asyncio
import functools
import io
import json
import zipfile
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
from sqlalchemy.ext.asyncio import AsyncSession

from app import config
from app.auth import get_optional_user
from app.config import CREDIT_PER_IMAGE, OUTPUT_DIR, UPLOAD_DIR
from app.database import get_db
from app.models.db_models import User
from app.models.schemas import (
    CompositeRequest,
    CopywritingRequest,
    CopywritingResponse,
    CopyItem,
    GenerateRequest,
    GenerateResultResponse,
    GenerateTaskResponse,
    GeneratedImage,
    ImageStatus,
    PlatformSpec,
    PLATFORM_SPECS,
    ProductTypeInfo,
    RegenerateRequest,
    SceneTemplateSchema,
    StyleSchema,
)
from app.services import credit_service, generation_service
from app.services import copywriting_service
from app.templates.registry import TemplateRegistry
from app.templates.styles.registry import StyleRegistry

router = APIRouter(prefix="/api", tags=["generate"])


@router.get("/styles", response_model=list[StyleSchema])
async def get_styles():
    """Get all available visual styles."""
    return [
        StyleSchema(
            id=s.id,
            name=s.name,
            name_en=s.name_en,
            description=s.description,
            icon=s.icon,
            preview_color=s.preview_color,
        )
        for s in StyleRegistry.get_all_styles()
    ]


@router.get("/styles/{product_type}", response_model=list[StyleSchema])
async def get_styles_for_category(product_type: str):
    """Get recommended visual styles for a specific product category."""
    styles = StyleRegistry.get_styles_for_category(product_type)
    return [
        StyleSchema(
            id=s.id,
            name=s.name,
            name_en=s.name_en,
            description=s.description,
            icon=s.icon,
            preview_color=s.preview_color,
        )
        for s in styles
    ]


@router.get("/product-types", response_model=list[ProductTypeInfo])
async def get_product_types():
    """Get all available product types."""
    return TemplateRegistry.get_product_types()


@router.get("/templates/{product_type}", response_model=list[SceneTemplateSchema])
async def get_templates(product_type: str):
    """Get templates for a product type."""
    templates = TemplateRegistry.get_templates(product_type)
    if not templates:
        raise HTTPException(status_code=404, detail=f"No templates for type: {product_type}")

    return [
        SceneTemplateSchema(
            id=t.id,
            name=t.name,
            name_en=t.name_en,
            product_type=t.product_type,
            prompt=t.prompt,
            description=t.description,
            aspect_ratio=t.aspect_ratio,
            recommended_provider=t.recommended_provider,
            injection_level=t.injection_level,
            sub_category=t.sub_category,
            sub_category_name=t.sub_category_name,
        )
        for t in templates
    ]


@router.post("/generate", response_model=GenerateTaskResponse)
async def start_generation(
    request: GenerateRequest,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Start image generation task. Works with or without authentication."""
    if not config.GEMINI_API_KEY:
        raise HTTPException(
            status_code=400,
            detail="Gemini API Key 未設定，請先到 /settings 頁面填入 API Key",
        )

    # Find the image to use
    image_id = request.image_id
    if request.remove_bg:
        nobg_path = UPLOAD_DIR / f"{image_id}_nobg.png"
        if nobg_path.exists():
            image_path = nobg_path
        else:
            # Auto remove bg first (run in thread to avoid blocking event loop)
            matching = list(UPLOAD_DIR.glob(f"{image_id}.*"))
            matching = [p for p in matching if "_nobg" not in p.name]
            if not matching:
                raise HTTPException(status_code=404, detail="Image not found")
            import asyncio
            import functools
            from app.services.background_removal import remove_background
            loop = asyncio.get_running_loop()
            try:
                await loop.run_in_executor(
                    None,
                    functools.partial(remove_background, matching[0], nobg_path),
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"背景移除失敗: {e}")
            image_path = nobg_path
    else:
        matching = list(UPLOAD_DIR.glob(f"{image_id}.*"))
        matching = [p for p in matching if "_nobg" not in p.name]
        if not matching:
            raise HTTPException(status_code=404, detail="Image not found")
        image_path = matching[0]

    # Build template overrides
    template_overrides = None
    if request.templates:
        template_overrides = {
            t.template_id: t.custom_prompt
            for t in request.templates
            if t.custom_prompt
        }

    # Determine number of images to generate (for credit check)
    templates = TemplateRegistry.get_templates(request.product_type.value)
    if request.selected_template_ids:
        selected_set = set(request.selected_template_ids)
        templates = [t for t in templates if t.id in selected_set]
    image_count = len(templates)

    # Check & charge credits (only if user is logged in)
    credits_needed = image_count * CREDIT_PER_IMAGE
    credits_remaining = 0
    if user:
        has_balance = await credit_service.check_balance(db, user.id, credits_needed)
        if not has_balance:
            balance = await credit_service.get_balance(db, user.id)
            raise HTTPException(
                status_code=402,
                detail=f"點數不足：需要 {credits_needed} 點，目前餘額 {balance} 點",
            )
        # Charge credits
        await credit_service.charge_credits(
            db, user.id, credits_needed,
            description=f"生成 {image_count} 張圖片（{request.product_type.value}）",
        )
        credits_remaining = await credit_service.get_balance(db, user.id)

    task = generation_service.create_task(
        image_path=image_path,
        product_type=request.product_type.value,
        template_overrides=template_overrides,
        selected_template_ids=request.selected_template_ids,
        style=request.style,
        user_id=user.id if user else None,
        shopee_optimize=(request.platform == "shopee"),
    )

    # Persist to DB
    await generation_service.persist_task_to_db(task)

    return GenerateTaskResponse(
        task_id=task.task_id,
        status=task.status,
        total=task.total,
        credits_charged=credits_needed if user else 0,
        credits_remaining=credits_remaining,
    )


@router.get("/generate/{task_id}/status")
async def generation_status_sse(task_id: str):
    """SSE endpoint for real-time generation progress."""
    task = generation_service.get_task(task_id)

    # Fallback: try loading from DB if not in memory
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Guard against duplicate generation: only start if task is still pending
    if task.status == "pending":
        task.status = "starting"  # Mark immediately to prevent re-entry

        async def event_stream():
            async for event in generation_service.run_generation(task_id):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"

        return StreamingResponse(
            event_stream(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )
    elif task.status in ("starting", "running"):
        # Already generating — return 409 to prevent duplicate generation
        raise HTTPException(
            status_code=409,
            detail="Generation already in progress for this task",
        )
    else:
        # Task already completed/failed/partial — return final results directly
        results_payload = generation_service._build_results_payload(task_id, task.results)
        final_event = {
            "event": "completed",
            "task_id": task_id,
            "status": task.status,
            "progress": task.total,
            "total": task.total,
            "results": results_payload,
        }

        async def done_stream():
            yield f"data: {json.dumps(final_event, ensure_ascii=False)}\n\n"

        return StreamingResponse(
            done_stream(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )


@router.get("/generate/{task_id}/results", response_model=GenerateResultResponse)
async def get_results(task_id: str):
    """Get generation results."""
    task = generation_service.get_task(task_id)
    # Fallback: try loading from DB if not in memory
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    images = []
    for r in task.results:
        images.append(GeneratedImage(
            template_id=r.template_id,
            template_name=r.template_name,
            status=ImageStatus(r.status.value),
            url=f"/api/outputs/{task_id}/{r.template_id}.png" if r.output_path else None,
            error=r.error,
        ))

    return GenerateResultResponse(
        task_id=task_id,
        status=task.status,
        progress=task.progress,
        total=task.total,
        images=images,
    )


def _resize_image_for_platform(
    output_path: str,
    target_w: int,
    target_h: int,
) -> tuple[str, bytes]:
    """Resize a single image to fit the platform spec (CPU-bound, sync).

    Returns (filename, png_bytes).
    """
    img = Image.open(output_path)
    img.thumbnail((target_w, target_h), Image.LANCZOS)
    canvas = Image.new("RGB", (target_w, target_h), (255, 255, 255))
    paste_x = (target_w - img.width) // 2
    paste_y = (target_h - img.height) // 2
    if img.mode == "RGBA":
        canvas.paste(img, (paste_x, paste_y), img)
    else:
        canvas.paste(img, (paste_x, paste_y))
    buf = io.BytesIO()
    canvas.save(buf, format="PNG")
    return buf.getvalue()


def _build_zip_bytes(
    results: list,
    spec_width: int,
    spec_height: int,
    platform: str,
    optimize_shopee: bool = False,
) -> bytes:
    """Build a zip archive from results (CPU-bound, sync)."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for r in results:
            if r.output_path and Path(r.output_path).exists():
                png_bytes = _resize_image_for_platform(
                    r.output_path, spec_width, spec_height,
                )
                filename = f"{r.template_id}_{spec_width}x{spec_height}.png"

                if optimize_shopee:
                    from app.services.image_processing import optimize_bytes_for_shopee
                    png_bytes, ext = optimize_bytes_for_shopee(png_bytes)
                    filename = f"{r.template_id}_{spec_width}x{spec_height}.{ext}"

                zf.writestr(filename, png_bytes)
    return buf.getvalue()


@router.get("/download/{task_id}")
async def download_all(task_id: str, platform: str = "general"):
    """Download all generated images as a zip file, optionally resized for platform."""
    task = generation_service.get_task(task_id)
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    spec = PLATFORM_SPECS.get(platform, PLATFORM_SPECS["general"])

    # Run CPU-intensive image processing + zip creation off the event loop
    loop = asyncio.get_running_loop()
    zip_bytes = await loop.run_in_executor(
        None,
        functools.partial(
            _build_zip_bytes,
            results=task.results,
            spec_width=spec.width,
            spec_height=spec.height,
            platform=platform,
            optimize_shopee=(platform == "shopee"),
        ),
    )

    return StreamingResponse(
        io.BytesIO(zip_bytes),
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename=product_images_{task_id}_{platform}.zip",
        },
    )


@router.post("/generate/{task_id}/regenerate")
async def regenerate_image(
    task_id: str,
    request: RegenerateRequest,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Regenerate a single image within an existing task. Works with or without authentication."""
    task = generation_service.get_task(task_id)
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Charge 1 credit for regeneration (only if user is logged in)
    if user:
        has_balance = await credit_service.check_balance(db, user.id, CREDIT_PER_IMAGE)
        if not has_balance:
            raise HTTPException(status_code=402, detail="點數不足，無法重新生成")
        await credit_service.charge_credits(
            db, user.id, CREDIT_PER_IMAGE,
            description=f"重新生成圖片（{request.template_id}）",
            job_id=task_id,
        )

    try:
        result = await generation_service.regenerate_single(
            task_id=task_id,
            template_id=request.template_id,
            custom_prompt=request.custom_prompt,
        )
        return {
            "template_id": result.template_id,
            "template_name": result.template_name,
            "status": result.status.value,
            "url": f"/api/outputs/{task_id}/{result.template_id}.png" if result.output_path else None,
            "error": result.error,
        }
    except Exception as e:
        # Refund credit on failure (only if user is logged in)
        if user:
            try:
                await credit_service.refund_credits(
                    db, user.id, CREDIT_PER_IMAGE,
                    description=f"重新生成失敗退費（{request.template_id}）",
                    job_id=task_id,
                )
            except Exception:
                pass
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate/{task_id}/variants/{template_id}")
async def generate_variants(
    task_id: str,
    template_id: str,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Generate 4 variant images for a single template. Works with or without authentication."""
    task = generation_service.get_task(task_id)
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    variant_count = 4

    # Charge credits for variants (only if user is logged in)
    if user:
        credits_needed = variant_count * CREDIT_PER_IMAGE
        has_balance = await credit_service.check_balance(db, user.id, credits_needed)
        if not has_balance:
            raise HTTPException(status_code=402, detail=f"點數不足：需要 {credits_needed} 點")
        await credit_service.charge_credits(
            db, user.id, credits_needed,
            description=f"生成 {variant_count} 個變體（{template_id}）",
            job_id=task_id,
        )

    try:
        variants = await generation_service.generate_variants(
            task_id=task_id,
            template_id=template_id,
            count=variant_count,
        )
        return {"variants": variants}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate/{task_id}/select-variant")
async def select_variant(task_id: str, request: dict):
    """Select a variant to replace the main image."""
    task = generation_service.get_task(task_id)
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    template_id = request.get("template_id")
    variant_index = request.get("variant_index")
    if template_id is None or variant_index is None:
        raise HTTPException(status_code=400, detail="template_id and variant_index are required")

    try:
        result = await generation_service.select_variant(
            task_id=task_id,
            template_id=template_id,
            variant_index=variant_index,
        )
        return {
            "template_id": result.template_id,
            "template_name": result.template_name,
            "status": result.status.value,
            "url": f"/api/outputs/{task_id}/{result.template_id}.png" if result.output_path else None,
            "error": result.error,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def _process_composite_image(
    completed: dict,
    ordered_ids: list[str],
    count: int,
    cell: int,
    gap: int,
    layout: str,
    bg_r: int,
    bg_g: int,
    bg_b: int,
) -> bytes:
    """Build a composite image from completed results (CPU-bound, sync).

    Returns PNG bytes.
    """
    import math

    cols = 3

    if layout == "detail_long":
        target_w = cell
        resized_images: list[Image.Image] = []
        for i in range(count):
            tid = ordered_ids[i]
            r = completed[tid]
            try:
                img = Image.open(r.output_path)
                if img.mode == "RGBA":
                    bg_img = Image.new("RGB", img.size, (bg_r, bg_g, bg_b))
                    bg_img.paste(img, mask=img)
                    img = bg_img
                elif img.mode != "RGB":
                    img = img.convert("RGB")
                scale = target_w / img.width
                new_h = int(img.height * scale)
                img = img.resize((target_w, new_h), Image.LANCZOS)
                resized_images.append(img)
            except Exception:
                continue

        if not resized_images:
            return b""

        total_h = sum(im.height for im in resized_images) + gap * (len(resized_images) - 1)
        canvas = Image.new("RGB", (target_w, total_h), (bg_r, bg_g, bg_b))
        y_offset = 0
        for im in resized_images:
            canvas.paste(im, (0, y_offset))
            y_offset += im.height + gap
    else:
        if layout == "hero_center":
            rows = 3
        else:
            rows = math.ceil(count / cols)

        total_w = cols * cell + (cols - 1) * gap
        total_h = rows * cell + (rows - 1) * gap
        canvas = Image.new("RGB", (total_w, total_h), (bg_r, bg_g, bg_b))

        for i in range(count):
            tid = ordered_ids[i]
            r = completed[tid]

            try:
                img = Image.open(r.output_path)
                if img.mode == "RGBA":
                    bg_img = Image.new("RGB", img.size, (bg_r, bg_g, bg_b))
                    bg_img.paste(img, mask=img)
                    img = bg_img
                elif img.mode != "RGB":
                    img = img.convert("RGB")
            except Exception:
                continue

            if layout == "hero_center" and i == 0:
                w = cell * 2 + gap
                h = cell * 2 + gap
                col, row = 0, 0
            elif layout == "hero_center" and i > 0:
                positions = [
                    (2, 0), (2, 1), (2, 2),
                    (0, 2), (1, 2),
                ]
                pos_idx = (i - 1) % len(positions)
                col, row = positions[pos_idx]
                w, h = cell, cell
            else:
                col = i % cols
                row = i // cols
                w, h = cell, cell

            x = col * (cell + gap)
            y = row * (cell + gap)

            scale = max(w / img.width, h / img.height)
            new_w = int(img.width * scale)
            new_h = int(img.height * scale)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            left = (new_w - w) // 2
            top = (new_h - h) // 2
            img = img.crop((left, top, left + w, top + h))

            canvas.paste(img, (x, y))

    buf = io.BytesIO()
    canvas.save(buf, format="PNG", quality=95)
    return buf.getvalue()


@router.post("/composite/{task_id}")
async def composite_grid(task_id: str, request: CompositeRequest):
    """Composite all completed images into a single grid image (server-side)."""
    task = generation_service.get_task(task_id)
    if not task:
        task = await generation_service.get_task_from_db(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Collect completed images in the requested order
    completed = {
        r.template_id: r
        for r in task.results
        if r.status.value == "completed" and r.output_path and Path(r.output_path).exists()
    }
    if not completed:
        raise HTTPException(status_code=400, detail="No completed images to composite")

    if request.image_order:
        ordered_ids = [tid for tid in request.image_order if tid in completed]
    else:
        ordered_ids = list(completed.keys())

    count = min(len(ordered_ids), 9)
    if count == 0:
        raise HTTPException(status_code=400, detail="No valid images for composite")

    bg_hex = request.bg_color.lstrip("#")
    try:
        bg_r, bg_g, bg_b = int(bg_hex[0:2], 16), int(bg_hex[2:4], 16), int(bg_hex[4:6], 16)
    except (ValueError, IndexError):
        bg_r, bg_g, bg_b = 255, 255, 255

    # Run CPU-intensive PIL compositing off the event loop
    loop = asyncio.get_running_loop()
    png_bytes = await loop.run_in_executor(
        None,
        functools.partial(
            _process_composite_image,
            completed=completed,
            ordered_ids=ordered_ids,
            count=count,
            cell=request.cell_size,
            gap=request.gap,
            layout=request.layout,
            bg_r=bg_r,
            bg_g=bg_g,
            bg_b=bg_b,
        ),
    )

    if not png_bytes:
        raise HTTPException(status_code=400, detail="No valid images for composite")

    filename = f"composite_{task_id}_{request.layout}.png"
    return StreamingResponse(
        io.BytesIO(png_bytes),
        media_type="image/png",
        headers={
            "Content-Disposition": f"attachment; filename={filename}",
        },
    )


@router.get("/platforms")
async def get_platforms():
    """Get available platform specs."""
    return {k: {"name": v.name, "width": v.width, "height": v.height} for k, v in PLATFORM_SPECS.items()}


@router.post("/generate-copy", response_model=CopywritingResponse)
async def generate_copy(request: CopywritingRequest):
    """Generate Traditional Chinese marketing copy for product images."""
    if not config.GEMINI_API_KEY:
        raise HTTPException(
            status_code=400,
            detail="Gemini API Key 未設定，請先到 /settings 頁面填入 API Key",
        )

    if not request.product_details.strip():
        raise HTTPException(status_code=400, detail="請輸入產品詳情")

    if not request.scenes:
        raise HTTPException(status_code=400, detail="請選擇至少一個場景")

    try:
        raw_text = await copywriting_service.generate_copy(
            product_details=request.product_details,
            product_type=request.product_type,
            scene_names=[
                {"name": s.name, "name_en": s.name_en, "description": s.description}
                for s in request.scenes
            ],
        )

        # Parse the JSON response from AI
        import re
        # Strip markdown code block markers if present
        cleaned = raw_text.strip()
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)

        copies = []
        try:
            items = json.loads(cleaned)
            for item in items:
                # Strip leading # from hashtags if AI included them
                raw_tags = item.get("hashtags", [])
                clean_tags = [t.lstrip("#") for t in raw_tags]
                copies.append(CopyItem(
                    scene_index=item.get("scene_index", 0),
                    title=item.get("title", ""),
                    subtitle=item.get("subtitle", ""),
                    description=item.get("description", ""),
                    hashtags=clean_tags,
                ))
        except json.JSONDecodeError:
            # If JSON parsing fails, return raw text
            return CopywritingResponse(copies=[], raw=raw_text)

        return CopywritingResponse(copies=copies, raw=raw_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"文案生成失敗: {str(e)}")
