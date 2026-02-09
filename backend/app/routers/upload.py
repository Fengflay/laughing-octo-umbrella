from __future__ import annotations

import asyncio
import functools
import io
import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from PIL import Image as PILImage
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_optional_user
from app.config import ALLOWED_EXTENSIONS, MAX_UPLOAD_SIZE, UPLOAD_DIR
from app.database import get_db
from app.models.db_models import UploadedImage, User
from app.models.schemas import RemoveBgResponse, UploadResponse
from app.services.background_removal import remove_background

router = APIRouter(prefix="/api", tags=["upload"])


@router.post("/upload", response_model=UploadResponse)
async def upload_image(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Upload a product image. Works with or without authentication."""
    # Validate file extension
    ext = Path(file.filename or "").suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type {ext} not allowed. Allowed: {ALLOWED_EXTENSIONS}",
        )

    # Read and validate size
    content = await file.read()
    if len(content) > MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max size: {MAX_UPLOAD_SIZE // (1024*1024)}MB",
        )

    # Validate file content is a real image (not just extension check)
    try:
        img = PILImage.open(io.BytesIO(content))
        img.verify()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid image file. The uploaded file is not a valid image.",
        )

    # Save file
    image_id = uuid.uuid4().hex[:12]
    filename = f"{image_id}{ext}"
    file_path = UPLOAD_DIR / filename
    file_path.write_bytes(content)

    # Persist upload record to DB (only if user is logged in)
    if user:
        try:
            upload_record = UploadedImage(
                id=image_id,
                user_id=user.id,
                filename=filename,
                file_path=str(file_path),
            )
            db.add(upload_record)
            await db.commit()
        except Exception:
            pass  # Non-critical: file is saved even if DB record fails

    return UploadResponse(
        image_id=image_id,
        filename=filename,
        url=f"/api/uploads/{filename}",
    )


@router.post("/remove-bg/{image_id}", response_model=RemoveBgResponse)
async def remove_bg(
    image_id: str,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Remove background from uploaded image. Works with or without authentication."""
    # Find the uploaded image
    matching = list(UPLOAD_DIR.glob(f"{image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="Image not found")

    input_path = matching[0]
    output_filename = f"{image_id}_nobg.png"
    output_path = UPLOAD_DIR / output_filename

    try:
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(
            None,
            functools.partial(remove_background, input_path, output_path),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Background removal failed: {e}")

    # Update DB record with nobg_path (only if user is logged in)
    if user:
        try:
            from sqlalchemy import update
            from app.models.db_models import UploadedImage as UploadedImageModel
            await db.execute(
                update(UploadedImageModel)
                .where(UploadedImageModel.id == image_id)
                .values(nobg_path=str(output_path))
            )
            await db.commit()
        except Exception:
            pass  # Non-critical

    return RemoveBgResponse(
        image_id=image_id,
        original_url=f"/api/uploads/{input_path.name}",
        removed_bg_url=f"/api/uploads/{output_filename}",
    )
