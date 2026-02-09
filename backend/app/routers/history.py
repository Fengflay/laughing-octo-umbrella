"""
History router: server-side generation history for authenticated users.

Replaces the frontend localStorage-based history with persistent,
cross-device accessible records.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.config import OUTPUT_DIR
from app.database import get_db
from app.models.db_models import GeneratedImage as GeneratedImageModel
from app.models.db_models import GenerationJob, User

router = APIRouter(prefix="/api", tags=["history"])


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------

class HistoryItemResponse(BaseModel):
    job_id: str
    product_type: str
    style: str | None
    status: str
    total_images: int
    completed_images: int
    credits_charged: int
    created_at: str
    first_image_url: str | None


class HistoryDetailResponse(BaseModel):
    job_id: str
    product_type: str
    style: str | None
    status: str
    total_images: int
    completed_images: int
    credits_charged: int
    error_message: str | None
    created_at: str
    updated_at: str
    images: list[HistoryImageResponse]


class HistoryImageResponse(BaseModel):
    template_id: str
    template_name: str
    status: str
    url: str | None
    error: str | None


class PaginatedHistoryResponse(BaseModel):
    items: list[HistoryItemResponse]
    total: int
    page: int
    page_size: int


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("/history", response_model=PaginatedHistoryResponse)
async def get_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Get generation history for the authenticated user (paginated)."""
    offset = (page - 1) * page_size

    # Count total
    count_result = await db.execute(
        select(func.count(GenerationJob.id)).where(GenerationJob.user_id == user.id)
    )
    total = count_result.scalar_one()

    # Fetch jobs with pagination
    result = await db.execute(
        select(GenerationJob)
        .where(GenerationJob.user_id == user.id)
        .order_by(GenerationJob.created_at.desc())
        .limit(page_size)
        .offset(offset)
    )
    jobs = list(result.scalars().all())

    items = []
    for job in jobs:
        # Find first completed image for thumbnail
        first_image_url = None
        if job.images:
            for img in job.images:
                if img.status == "completed" and img.output_path:
                    first_image_url = f"/api/outputs/{job.id}/{img.template_id}.png"
                    break

        items.append(HistoryItemResponse(
            job_id=job.id,
            product_type=job.product_type,
            style=job.style,
            status=job.status,
            total_images=job.total_images,
            completed_images=job.completed_images,
            credits_charged=job.credits_charged,
            created_at=job.created_at.isoformat(),
            first_image_url=first_image_url,
        ))

    return PaginatedHistoryResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/history/{job_id}", response_model=HistoryDetailResponse)
async def get_history_detail(
    job_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Get detailed history for a single generation job."""
    result = await db.execute(
        select(GenerationJob)
        .where(GenerationJob.id == job_id, GenerationJob.user_id == user.id)
    )
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=404, detail="生成記錄未找到")

    images = [
        HistoryImageResponse(
            template_id=img.template_id,
            template_name=img.template_name,
            status=img.status,
            url=f"/api/outputs/{job.id}/{img.template_id}.png" if img.status == "completed" and img.output_path else None,
            error=img.error,
        )
        for img in (job.images or [])
    ]

    return HistoryDetailResponse(
        job_id=job.id,
        product_type=job.product_type,
        style=job.style,
        status=job.status,
        total_images=job.total_images,
        completed_images=job.completed_images,
        credits_charged=job.credits_charged,
        error_message=job.error_message,
        created_at=job.created_at.isoformat(),
        updated_at=job.updated_at.isoformat(),
        images=images,
    )
