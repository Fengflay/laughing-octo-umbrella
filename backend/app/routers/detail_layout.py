"""
Detail page layout router: marketing copy generation and multi-platform export.

Endpoints:
- POST /api/detail-layout/generate-copy — Generate marketing copy
- POST /api/detail-layout/export — Export for multiple platforms as ZIP
"""

from __future__ import annotations

import io
import zipfile

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.database import get_db
from app.models.db_models import User
from app.models.schemas import (
    ExportDetailRequest,
    ExportDetailResponse,
    GenerateCopyRequest,
    GenerateCopyResponse,
    MarketingCopy,
)

router = APIRouter(prefix="/api/detail-layout", tags=["detail-layout"])


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/generate-copy", response_model=GenerateCopyResponse)
async def generate_copy(
    request: GenerateCopyRequest,
    user: User = Depends(get_current_user),
):
    """Generate marketing copy for a product.

    TODO: Connect to Gemini AI for copy generation.
    """
    if not request.product_name.strip():
        raise HTTPException(status_code=400, detail="商品名稱不可為空")

    # Mock: return Traditional Chinese marketing copy (Taiwan style)
    features_text = "、".join(request.features[:3]) if request.features else "高品質設計"

    mock_copy = MarketingCopy(
        headline=f"【限時特惠】{request.product_name} — 質感生活新選擇",
        subtitle=f"嚴選 {features_text}，讓每一天都充滿品味",
        selling_points=[
            f"嚴選材質：採用頂級原料，{features_text}",
            "匠心工藝：細節決定品質，每一處都經得起檢視",
            "百搭實用：適合多種場合，輕鬆提升生活質感",
            "限量供應：錯過不再，立即擁有專屬品味",
        ],
        cta="立即購買，享受限時免運優惠！",
    )

    return GenerateCopyResponse(marketing_copy=mock_copy)


@router.post("/export")
async def export_detail(
    request: ExportDetailRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Export images for multiple platforms as a ZIP file.

    TODO: Implement full platform-specific resizing and 4K upscale.
    """
    from pathlib import Path
    from app.config import OUTPUT_DIR

    task_output_dir = OUTPUT_DIR / request.task_id
    if not task_output_dir.exists():
        raise HTTPException(status_code=404, detail="生成任務未找到，請先生成圖片")

    # Collect images
    images = list(task_output_dir.glob("*.png"))
    images = [img for img in images if "_v" not in img.name]  # Skip variants
    if not images:
        raise HTTPException(status_code=400, detail="沒有可匯出的圖片")

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for platform_config in request.platforms:
            platform_dir = platform_config.platform
            for img_file in images:
                # For now, just include original images organized by platform
                arcname = f"{platform_dir}/{img_file.name}"
                zf.write(img_file, arcname)

        # If 4K upscale requested, add a note file
        if request.include_4k_upscale:
            zf.writestr(
                "4K_UPSCALE_NOTE.txt",
                "4K 放大功能尚在開發中，目前匯出為原始解析度。\n"
                "4K upscaling is under development. Current export uses original resolution.\n",
            )

    buf.seek(0)
    filename = f"export_{request.task_id}.zip"
    return StreamingResponse(
        buf,
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename={filename}",
        },
    )
