"""
Credit service: check balance, charge, refund, and query transactions.

Credits are simple integers: 1 credit = 1 generated image.
All mutations are atomic (single DB transaction) with audit trail.
"""

import logging
from typing import Optional

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db_models import CreditTransaction, User

logger = logging.getLogger(__name__)


async def check_balance(db: AsyncSession, user_id: str, required: int) -> bool:
    """Check if user has enough credits. Does NOT lock or modify."""
    result = await db.execute(select(User.credits).where(User.id == user_id))
    balance = result.scalar_one_or_none()
    if balance is None:
        return False
    return balance >= required


async def charge_credits(
    db: AsyncSession,
    user_id: str,
    amount: int,
    description: str,
    job_id: Optional[str] = None,
) -> CreditTransaction:
    """Atomically deduct credits and create a transaction record.

    Uses a single UPDATE with a WHERE guard (credits >= amount) to prevent
    race conditions under concurrent requests — no separate SELECT needed.

    Args:
        amount: positive number of credits to deduct
    Returns:
        The CreditTransaction record
    Raises:
        RuntimeError if insufficient balance or user not found
    """
    if amount <= 0:
        raise ValueError("Charge amount must be positive")

    # Atomic update: deduct only if sufficient balance exists.
    # The WHERE clause ensures no negative balance can occur even under
    # concurrent requests — the DB engine serialises row-level writes.
    result = await db.execute(
        update(User)
        .where(User.id == user_id, User.credits >= amount)
        .values(credits=User.credits - amount)
    )

    if result.rowcount == 0:
        # Distinguish "user not found" from "insufficient balance"
        user_result = await db.execute(
            select(User.credits).where(User.id == user_id)
        )
        balance = user_result.scalar_one_or_none()
        if balance is None:
            raise RuntimeError("User not found")
        raise RuntimeError(f"點數不足：需要 {amount} 點，目前餘額 {balance} 點")

    # Read back the new balance for the audit log record
    bal_result = await db.execute(
        select(User.credits).where(User.id == user_id)
    )
    new_balance = bal_result.scalar_one()

    # Create transaction record
    tx = CreditTransaction(
        user_id=user_id,
        amount=-amount,
        balance_after=new_balance,
        description=description,
        job_id=job_id,
    )
    db.add(tx)

    await db.commit()

    logger.info(f"Charged {amount} credits from user {user_id} (balance: {new_balance})")
    return tx


async def refund_credits(
    db: AsyncSession,
    user_id: str,
    amount: int,
    description: str,
    job_id: Optional[str] = None,
) -> CreditTransaction:
    """Atomically refund credits to user (e.g., on total job failure).

    Args:
        amount: positive number of credits to refund
    """
    if amount <= 0:
        raise ValueError("Refund amount must be positive")

    # Atomic update: add credits back
    result = await db.execute(
        update(User)
        .where(User.id == user_id)
        .values(credits=User.credits + amount)
    )

    if result.rowcount == 0:
        raise RuntimeError("User not found")

    # Read back the new balance for the audit log record
    bal_result = await db.execute(
        select(User.credits).where(User.id == user_id)
    )
    new_balance = bal_result.scalar_one()

    tx = CreditTransaction(
        user_id=user_id,
        amount=amount,
        balance_after=new_balance,
        description=description,
        job_id=job_id,
    )
    db.add(tx)

    await db.commit()

    logger.info(f"Refunded {amount} credits to user {user_id} (balance: {new_balance})")
    return tx


async def get_balance(db: AsyncSession, user_id: str) -> int:
    """Get current credit balance."""
    result = await db.execute(select(User.credits).where(User.id == user_id))
    balance = result.scalar_one_or_none()
    return balance or 0


async def get_transactions(
    db: AsyncSession,
    user_id: str,
    limit: int = 50,
    offset: int = 0,
) -> list[CreditTransaction]:
    """Get transaction history for a user, newest first."""
    result = await db.execute(
        select(CreditTransaction)
        .where(CreditTransaction.user_id == user_id)
        .order_by(CreditTransaction.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(result.scalars().all())
