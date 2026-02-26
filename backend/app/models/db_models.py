"""
SQLAlchemy ORM models for all persistent data.

Tables:
- users: User accounts with credit balance
- generation_jobs: Image generation tasks (mirrors in-memory GenerationTask)
- generated_images: Individual generated images per job
- credit_transactions: Audit trail for all credit changes
- uploaded_images: Uploaded product images metadata
"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _new_uuid() -> str:
    return uuid.uuid4().hex[:12]


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: uuid.uuid4().hex)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    display_name: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    credits: Mapped[int] = mapped_column(Integer, nullable=False, default=50)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow, onupdate=_utcnow)

    # Relationships
    jobs: Mapped[list["GenerationJob"]] = relationship(back_populates="user", lazy="selectin")
    transactions: Mapped[list["CreditTransaction"]] = relationship(back_populates="user", lazy="selectin")


# ---------------------------------------------------------------------------
# Generation Jobs
# ---------------------------------------------------------------------------

class GenerationJob(Base):
    __tablename__ = "generation_jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)  # = task_id
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    product_type: Mapped[str] = mapped_column(String(50), nullable=False)
    style: Mapped[str | None] = mapped_column(String(50), nullable=True)
    image_path: Mapped[str] = mapped_column(Text, nullable=False)
    total_images: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    completed_images: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    credits_charged: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow, onupdate=_utcnow)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="jobs")
    images: Mapped[list["GeneratedImage"]] = relationship(back_populates="job", lazy="selectin")


# ---------------------------------------------------------------------------
# Generated Images (per-template results within a job)
# ---------------------------------------------------------------------------

class GeneratedImage(Base):
    __tablename__ = "generated_images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(String(36), ForeignKey("generation_jobs.id"), index=True, nullable=False)
    template_id: Mapped[str] = mapped_column(String(100), nullable=False)
    template_name: Mapped[str] = mapped_column(String(200), nullable=False, default="")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    output_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)

    # Relationships
    job: Mapped["GenerationJob"] = relationship(back_populates="images")


# ---------------------------------------------------------------------------
# Credit Transactions (audit trail)
# ---------------------------------------------------------------------------

class CreditTransaction(Base):
    __tablename__ = "credit_transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)  # positive = credit, negative = debit
    balance_after: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False, default="")
    job_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("generation_jobs.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="transactions")


# ---------------------------------------------------------------------------
# Uploaded Images (metadata tracking)
# ---------------------------------------------------------------------------

class UploadedImage(Base):
    __tablename__ = "uploaded_images"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)  # = image_id
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    nobg_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)


# ---------------------------------------------------------------------------
# Batch Jobs (Phase 3: multi-SKU batch processing)
# ---------------------------------------------------------------------------

class Batch(Base):
    __tablename__ = "batches"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: uuid.uuid4().hex[:12])
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    total_skus: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    completed_skus: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    total_credits: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    csv_data: Mapped[str] = mapped_column(Text, nullable=False, default="")
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow, onupdate=_utcnow)

    user: Mapped["User"] = relationship()
    items: Mapped[list["BatchItem"]] = relationship(back_populates="batch", lazy="selectin")


class BatchItem(Base):
    __tablename__ = "batch_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    batch_id: Mapped[str] = mapped_column(String(36), ForeignKey("batches.id"), index=True, nullable=False)
    sku_name: Mapped[str] = mapped_column(String(255), nullable=False)
    product_type: Mapped[str] = mapped_column(String(50), nullable=False)
    style: Mapped[str | None] = mapped_column(String(50), nullable=True)
    image_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    image_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    job_id: Mapped[str | None] = mapped_column(String(36), ForeignKey("generation_jobs.id"), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    error: Mapped[str | None] = mapped_column(Text, nullable=True)

    batch: Mapped["Batch"] = relationship(back_populates="items")


# ---------------------------------------------------------------------------
# Projects (Phase 3: project management)
# ---------------------------------------------------------------------------

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: uuid.uuid4().hex[:12])
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    brand_color: Mapped[str | None] = mapped_column(String(20), nullable=True)
    default_product_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    default_style: Mapped[str | None] = mapped_column(String(50), nullable=True)
    is_archived: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow, onupdate=_utcnow)

    user: Mapped["User"] = relationship()


# ---------------------------------------------------------------------------
# Audit Logs (Phase 3: production hardening)
# ---------------------------------------------------------------------------

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    request_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    user_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    method: Mapped[str] = mapped_column(String(10), nullable=False)
    path: Mapped[str] = mapped_column(String(500), nullable=False)
    status_code: Mapped[int] = mapped_column(Integer, nullable=False)
    duration_ms: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    client_ip: Mapped[str | None] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)


# ---------------------------------------------------------------------------
# V2: Product Analysis (AI 分析結果)
# ---------------------------------------------------------------------------

class ProductAnalysis(Base):
    __tablename__ = "product_analyses"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: uuid.uuid4().hex[:12])
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    image_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    product_name: Mapped[str] = mapped_column(String(200), nullable=False, default="")
    category: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    audience: Mapped[str] = mapped_column(String(20), nullable=False, default="通用")
    primary_color: Mapped[str] = mapped_column(String(10), nullable=False, default="#000000")
    secondary_color: Mapped[str] = mapped_column(String(10), nullable=False, default="#ffffff")
    material: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    material_confidence: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    features: Mapped[str] = mapped_column(Text, nullable=False, default="[]")  # JSON array
    local_features: Mapped[str] = mapped_column(Text, nullable=False, default="[]")  # JSON array
    texture_feel: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    contour_type: Mapped[str] = mapped_column(String(50), nullable=False, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)

    user: Mapped["User"] = relationship()


# ---------------------------------------------------------------------------
# V2: Storyboard Config (9 宮格配置)
# ---------------------------------------------------------------------------

class StoryboardConfig(Base):
    __tablename__ = "storyboard_configs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: uuid.uuid4().hex[:12])
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    task_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    image_id: Mapped[str] = mapped_column(String(36), nullable=False)
    grid_config: Mapped[str] = mapped_column(Text, nullable=False, default="[]")  # JSON array of cell configs
    atmosphere_lock: Mapped[str | None] = mapped_column(String(50), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="draft")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow, onupdate=_utcnow)

    user: Mapped["User"] = relationship()


# ---------------------------------------------------------------------------
# V2: Style Reference (風格參考圖)
# ---------------------------------------------------------------------------

class StyleReference(Base):
    __tablename__ = "style_references"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: uuid.uuid4().hex[:12])
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"), index=True, nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    extracted_style_info: Mapped[str] = mapped_column(Text, nullable=False, default="{}")  # JSON object
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=_utcnow)

    user: Mapped["User"] = relationship()
