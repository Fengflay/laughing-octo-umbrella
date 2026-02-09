"""
Credits router: balance + transaction history for authenticated users.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.database import get_db
from app.models.db_models import User
from app.services import credit_service

router = APIRouter(prefix="/api/credits", tags=["credits"])


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------

class BalanceResponse(BaseModel):
    credits: int
    user_id: str


class TransactionResponse(BaseModel):
    id: int
    amount: int
    balance_after: int
    description: str
    job_id: str | None
    created_at: str


class TransactionListResponse(BaseModel):
    transactions: list[TransactionResponse]
    total: int
    page: int
    page_size: int


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("/balance", response_model=BalanceResponse)
async def get_balance(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Get current credit balance."""
    balance = await credit_service.get_balance(db, user.id)
    return BalanceResponse(credits=balance, user_id=user.id)


@router.get("/transactions", response_model=TransactionListResponse)
async def get_transactions(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Get credit transaction history (paginated, newest first)."""
    from sqlalchemy import func, select
    from app.models.db_models import CreditTransaction

    offset = (page - 1) * page_size

    # Count total
    count_result = await db.execute(
        select(func.count(CreditTransaction.id))
        .where(CreditTransaction.user_id == user.id)
    )
    total = count_result.scalar_one()

    # Fetch transactions
    txns = await credit_service.get_transactions(
        db, user.id, limit=page_size, offset=offset,
    )

    items = [
        TransactionResponse(
            id=tx.id,
            amount=tx.amount,
            balance_after=tx.balance_after,
            description=tx.description,
            job_id=tx.job_id,
            created_at=tx.created_at.isoformat(),
        )
        for tx in txns
    ]

    return TransactionListResponse(
        transactions=items,
        total=total,
        page=page,
        page_size=page_size,
    )
