"""
Projects router: CRUD for project management.

Projects allow users to group generation jobs, set default product types/styles,
and maintain brand consistency.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import func, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.database import get_db
from app.models.db_models import Project, User

router = APIRouter(prefix="/api/projects", tags=["projects"])


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------

class ProjectCreate(BaseModel):
    name: str
    description: str = ""
    brand_color: str | None = None
    default_product_type: str | None = None
    default_style: str | None = None


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    brand_color: str | None = None
    default_product_type: str | None = None
    default_style: str | None = None
    is_archived: bool | None = None


class ProjectResponse(BaseModel):
    id: str
    name: str
    description: str
    brand_color: str | None
    default_product_type: str | None
    default_style: str | None
    is_archived: bool
    created_at: str
    updated_at: str


class ProjectListResponse(BaseModel):
    projects: list[ProjectResponse]
    total: int


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("", response_model=ProjectListResponse)
async def list_projects(
    include_archived: bool = Query(False),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """List all projects for the current user."""
    query = select(Project).where(Project.user_id == user.id)
    if not include_archived:
        query = query.where(Project.is_archived == False)  # noqa: E712
    query = query.order_by(Project.updated_at.desc())

    result = await db.execute(query)
    projects = list(result.scalars().all())

    count_query = select(func.count(Project.id)).where(Project.user_id == user.id)
    if not include_archived:
        count_query = count_query.where(Project.is_archived == False)  # noqa: E712
    count_result = await db.execute(count_query)
    total = count_result.scalar_one()

    return ProjectListResponse(
        projects=[
            ProjectResponse(
                id=p.id,
                name=p.name,
                description=p.description,
                brand_color=p.brand_color,
                default_product_type=p.default_product_type,
                default_style=p.default_style,
                is_archived=p.is_archived,
                created_at=p.created_at.isoformat(),
                updated_at=p.updated_at.isoformat(),
            )
            for p in projects
        ],
        total=total,
    )


@router.post("", response_model=ProjectResponse, status_code=201)
async def create_project(
    request: ProjectCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Create a new project."""
    if not request.name.strip():
        raise HTTPException(status_code=400, detail="專案名稱不能為空")

    project = Project(
        user_id=user.id,
        name=request.name.strip(),
        description=request.description,
        brand_color=request.brand_color,
        default_product_type=request.default_product_type,
        default_style=request.default_style,
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)

    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        brand_color=project.brand_color,
        default_product_type=project.default_product_type,
        default_style=project.default_style,
        is_archived=project.is_archived,
        created_at=project.created_at.isoformat(),
        updated_at=project.updated_at.isoformat(),
    )


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Get a single project."""
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="專案未找到")

    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        brand_color=project.brand_color,
        default_product_type=project.default_product_type,
        default_style=project.default_style,
        is_archived=project.is_archived,
        created_at=project.created_at.isoformat(),
        updated_at=project.updated_at.isoformat(),
    )


@router.patch("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: str,
    request: ProjectUpdate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Update a project."""
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="專案未找到")

    # Only update fields that were provided
    update_data = request.model_dump(exclude_unset=True)
    if "name" in update_data and update_data["name"] is not None:
        update_data["name"] = update_data["name"].strip()
        if not update_data["name"]:
            raise HTTPException(status_code=400, detail="專案名稱不能為空")

    if update_data:
        await db.execute(
            update(Project)
            .where(Project.id == project_id)
            .values(**update_data)
        )
        await db.commit()
        await db.refresh(project)

    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        brand_color=project.brand_color,
        default_product_type=project.default_product_type,
        default_style=project.default_style,
        is_archived=project.is_archived,
        created_at=project.created_at.isoformat(),
        updated_at=project.updated_at.isoformat(),
    )


@router.delete("/{project_id}")
async def delete_project(
    project_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Delete a project (permanent)."""
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="專案未找到")

    await db.execute(delete(Project).where(Project.id == project_id))
    await db.commit()

    return {"message": "專案已刪除", "project_id": project_id}
