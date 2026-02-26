"""
Image optimization router: regenerate, inpaint, upscale, outpaint.

Endpoints:
- POST /api/optimize/regenerate — Regenerate with same/custom seed
- POST /api/optimize/inpaint — Inpaint with mask
- POST /api/optimize/generate-additional — Generate additional images
- POST /api/optimize/upscale — Upscale to 4K
- POST /api/optimize/outpaint — Outpaint to target ratio
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from app.auth import get_current_user
from app.models.db_models import User
from app.models.schemas import (
    GenerateAdditionalRequest,
    GenerateAdditionalResponse,
    InpaintRequest,
    InpaintResponse,
    OutpaintRequest,
    OutpaintResponse,
    RegenerateOptRequest,
    RegenerateOptResponse,
    UpscaleRequest,
    UpscaleResponse,
)

router = APIRouter(prefix="/api/optimize", tags=["optimization"])


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/regenerate", response_model=RegenerateOptResponse)
async def regenerate(
    request: RegenerateOptRequest,
    user: User = Depends(get_current_user),
):
    """Regenerate an image with original seed or custom parameters.

    TODO: Connect to AI generation service.
    """
    from app.config import UPLOAD_DIR

    # Verify the image exists (by image_id)
    matching = list(UPLOAD_DIR.glob(f"{request.image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="圖片未找到")

    # Mock: return the original image URL
    original_file = matching[0]
    return RegenerateOptResponse(
        new_image_url=f"/api/uploads/{original_file.name}",
    )


@router.post("/inpaint", response_model=InpaintResponse)
async def inpaint(
    request: InpaintRequest,
    user: User = Depends(get_current_user),
):
    """Inpaint a region of an image using a mask.

    TODO: Connect to AI inpainting service.
    """
    from app.config import UPLOAD_DIR

    if not request.mask_data:
        raise HTTPException(status_code=400, detail="遮罩資料不可為空")

    # Verify the image exists
    matching = list(UPLOAD_DIR.glob(f"{request.image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="圖片未找到")

    # Mock: return the original image
    original_file = matching[0]
    return InpaintResponse(
        repaired_image_url=f"/api/uploads/{original_file.name}",
    )


@router.post("/generate-additional", response_model=GenerateAdditionalResponse)
async def generate_additional(
    request: GenerateAdditionalRequest,
    user: User = Depends(get_current_user),
):
    """Generate additional images of a specific type.

    TODO: Connect to AI generation service.
    """
    if request.count < 1 or request.count > 10:
        raise HTTPException(status_code=400, detail="數量需在 1-10 之間")

    # Mock: return placeholder URLs
    images = [
        f"/api/uploads/placeholder_additional_{i}.png"
        for i in range(request.count)
    ]
    return GenerateAdditionalResponse(images=images)


@router.post("/upscale", response_model=UpscaleResponse)
async def upscale(
    request: UpscaleRequest,
    user: User = Depends(get_current_user),
):
    """Upscale an image to 4K resolution.

    TODO: Connect to AI upscaling service (Real-ESRGAN, etc.).
    """
    from app.config import UPLOAD_DIR

    matching = list(UPLOAD_DIR.glob(f"{request.image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="圖片未找到")

    # Mock: return the original image
    original_file = matching[0]
    return UpscaleResponse(
        upscaled_image_url=f"/api/uploads/{original_file.name}",
    )


@router.post("/outpaint", response_model=OutpaintResponse)
async def outpaint(
    request: OutpaintRequest,
    user: User = Depends(get_current_user),
):
    """Outpaint an image to a target aspect ratio.

    TODO: Connect to AI outpainting service.
    """
    from app.config import UPLOAD_DIR

    matching = list(UPLOAD_DIR.glob(f"{request.image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="圖片未找到")

    # Validate target ratio format
    if ":" not in request.target_ratio:
        raise HTTPException(status_code=400, detail="比例格式無效，請使用如 '9:16' 的格式")

    # Mock: return the original image
    original_file = matching[0]
    return OutpaintResponse(
        outpainted_image_url=f"/api/uploads/{original_file.name}",
    )
