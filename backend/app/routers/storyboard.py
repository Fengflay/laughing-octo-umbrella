"""
Storyboard router: 9-grid preview generation and management.

Endpoints:
- POST /api/storyboard/generate-preview — Generate 9 low-res previews
- POST /api/storyboard/confirm — Confirm and trigger high-res render
- PUT /api/storyboard/{task_id}/swap — Swap two grid positions
- PUT /api/storyboard/{task_id}/change-type — Change image type at position
"""

from __future__ import annotations

import json
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.database import get_db
from app.models.db_models import StoryboardConfig, User
from app.models.schemas import (
    ChangeTypeRequest,
    ChangeTypeResponse,
    ConfirmStoryboardRequest,
    ConfirmStoryboardResponse,
    GeneratePreviewRequest,
    GeneratePreviewResponse,
    GridCellConfig,
    PreviewImage,
    SwapPositionRequest,
    SwapPositionResponse,
)

router = APIRouter(prefix="/api/storyboard", tags=["storyboard"])


# ---------------------------------------------------------------------------
# Mock image types for 9-grid
# ---------------------------------------------------------------------------

MOCK_IMAGE_TYPES = [
    "主圖 - 白底正面（純白背景居中展示，雙側柔光箱 45° 均勻照明）",
    "主圖 - 白底 45°（白底 45 度側面展示，突出產品輪廓與立體感）",
    "情境圖 - 生活場景（日常使用情境，自然光環境，增強購買代入感）",
    "情境圖 - 使用場景（展示產品功能與使用方式，突出實際體驗效果）",
    "細節圖 - 材質特寫（100mm 微距鏡頭近攝，低角度側光突顯紋理與工藝品質）",
    "細節圖 - 功能展示（拉鍊、扣環、口袋等功能部件特寫，展示設計巧思）",
    "模特圖 - 正面穿搭（虛擬模特全身正面展示，自然站姿配合專業棚拍燈光）",
    "尺寸對比圖（產品搭配常見物品的尺寸參照，直觀展示實際大小）",
    "包裝展示圖（禮盒或包裝全景，展示開箱體驗與品牌質感）",
]


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/generate-preview", response_model=GeneratePreviewResponse)
async def generate_preview(
    request: GeneratePreviewRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Generate 9 low-res preview thumbnails for the storyboard.

    TODO: Replace with AI-powered preview generation.
    """
    from app.config import UPLOAD_DIR

    # Verify image exists
    matching = list(UPLOAD_DIR.glob(f"{request.image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="圖片未找到，請先上傳圖片")

    task_id = uuid.uuid4().hex[:12]

    # Mock 9 preview images
    previews = []
    grid_config = []
    for i in range(9):
        image_type = MOCK_IMAGE_TYPES[i]
        previews.append(PreviewImage(
            position=i,
            image_url=f"/api/uploads/placeholder_preview_{i}.png",
            image_type=image_type,
        ))
        grid_config.append(GridCellConfig(
            position=i,
            image_type=image_type,
            selected=True,
        ))

    # Persist storyboard config
    config = StoryboardConfig(
        id=uuid.uuid4().hex[:12],
        user_id=user.id,
        task_id=task_id,
        image_id=request.image_id,
        grid_config=json.dumps(
            [c.model_dump() for c in grid_config],
            ensure_ascii=False,
        ),
        atmosphere_lock=request.atmosphere_lock,
        status="preview",
    )
    db.add(config)
    await db.commit()

    return GeneratePreviewResponse(
        task_id=task_id,
        previews=previews,
    )


@router.post("/confirm", response_model=ConfirmStoryboardResponse)
async def confirm_storyboard(
    request: ConfirmStoryboardRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Confirm storyboard and trigger high-res rendering.

    TODO: Hook into existing generation pipeline for high-res output.
    """
    # Find storyboard config
    result = await db.execute(
        select(StoryboardConfig).where(
            StoryboardConfig.task_id == request.task_id,
            StoryboardConfig.user_id == user.id,
        )
    )
    config = result.scalar_one_or_none()
    if not config:
        raise HTTPException(status_code=404, detail="故事板配置未找到")

    if config.status not in ("preview", "draft"):
        raise HTTPException(status_code=400, detail=f"故事板狀態為 {config.status}，無法確認")

    # Update grid config with user adjustments
    await db.execute(
        update(StoryboardConfig)
        .where(StoryboardConfig.id == config.id)
        .values(
            grid_config=json.dumps(
                [c.model_dump() for c in request.grid_config],
                ensure_ascii=False,
            ),
            status="confirmed",
        )
    )
    await db.commit()

    return ConfirmStoryboardResponse(
        task_id=request.task_id,
        status="confirmed",
        message="已確認，高清圖片正在渲染中。請透過 SSE 追蹤進度。",
    )


@router.put("/{task_id}/swap", response_model=SwapPositionResponse)
async def swap_positions(
    task_id: str,
    request: SwapPositionRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Swap two grid cell positions."""
    result = await db.execute(
        select(StoryboardConfig).where(
            StoryboardConfig.task_id == task_id,
            StoryboardConfig.user_id == user.id,
        )
    )
    config = result.scalar_one_or_none()
    if not config:
        raise HTTPException(status_code=404, detail="故事板配置未找到")

    # Parse current grid config
    cells = json.loads(config.grid_config)

    # Validate positions
    if not (0 <= request.position_a < len(cells) and 0 <= request.position_b < len(cells)):
        raise HTTPException(status_code=400, detail="位置超出範圍")

    # Swap image_type between two positions
    cells[request.position_a]["image_type"], cells[request.position_b]["image_type"] = (
        cells[request.position_b]["image_type"],
        cells[request.position_a]["image_type"],
    )

    # Persist
    await db.execute(
        update(StoryboardConfig)
        .where(StoryboardConfig.id == config.id)
        .values(grid_config=json.dumps(cells, ensure_ascii=False))
    )
    await db.commit()

    updated_config = [GridCellConfig(**c) for c in cells]
    return SwapPositionResponse(grid_config=updated_config)


@router.put("/{task_id}/change-type", response_model=ChangeTypeResponse)
async def change_type(
    task_id: str,
    request: ChangeTypeRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Change the image type at a specific grid position.

    TODO: Replace with AI re-generation of the specific cell preview.
    """
    result = await db.execute(
        select(StoryboardConfig).where(
            StoryboardConfig.task_id == task_id,
            StoryboardConfig.user_id == user.id,
        )
    )
    config = result.scalar_one_or_none()
    if not config:
        raise HTTPException(status_code=404, detail="故事板配置未找到")

    cells = json.loads(config.grid_config)

    if not (0 <= request.position < len(cells)):
        raise HTTPException(status_code=400, detail="位置超出範圍")

    # Update the type
    cells[request.position]["image_type"] = request.new_type

    # Persist
    await db.execute(
        update(StoryboardConfig)
        .where(StoryboardConfig.id == config.id)
        .values(grid_config=json.dumps(cells, ensure_ascii=False))
    )
    await db.commit()

    return ChangeTypeResponse(
        position=request.position,
        new_type=request.new_type,
        preview_url=f"/api/uploads/placeholder_preview_{request.position}.png",
    )
