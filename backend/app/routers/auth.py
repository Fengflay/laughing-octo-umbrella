"""
Authentication router: register, login, get current user.
"""

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import create_access_token, get_current_user, hash_password, verify_password
from app.config import FREE_CREDITS
from app.database import get_db
from app.models.db_models import CreditTransaction, User

router = APIRouter(prefix="/api/auth", tags=["auth"])


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------

class RegisterRequest(BaseModel):
    email: str
    password: str
    display_name: str = ""


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    user_id: str
    email: str
    display_name: str
    token: str
    credits: int


class UserInfoResponse(BaseModel):
    user_id: str
    email: str
    display_name: str
    credits: int


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/register", response_model=AuthResponse)
async def register(req: RegisterRequest, db: AsyncSession = Depends(get_db)):
    """Register a new user account with free credits."""
    # Validate email format (basic)
    email = req.email.strip().lower()
    if not email or "@" not in email:
        raise HTTPException(status_code=400, detail="請輸入有效的電子郵件")

    # Validate password
    if len(req.password) < 6:
        raise HTTPException(status_code=400, detail="密碼至少需要 6 個字元")

    # Check if email already exists
    result = await db.execute(select(User).where(User.email == email))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=409, detail="此電子郵件已被註冊")

    # Create user
    user_id = uuid.uuid4().hex
    user = User(
        id=user_id,
        email=email,
        password_hash=hash_password(req.password),
        display_name=req.display_name.strip() or email.split("@")[0],
        credits=FREE_CREDITS,
    )
    db.add(user)

    # Record the initial credit grant
    tx = CreditTransaction(
        user_id=user_id,
        amount=FREE_CREDITS,
        balance_after=FREE_CREDITS,
        description=f"註冊贈送 {FREE_CREDITS} 點",
    )
    db.add(tx)

    await db.commit()
    await db.refresh(user)

    token = create_access_token(user.id, user.email)

    return AuthResponse(
        user_id=user.id,
        email=user.email,
        display_name=user.display_name,
        token=token,
        credits=user.credits,
    )


@router.post("/login", response_model=AuthResponse)
async def login(req: LoginRequest, db: AsyncSession = Depends(get_db)):
    """Login with email and password."""
    email = req.email.strip().lower()

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=401, detail="電子郵件或密碼錯誤")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="帳號已被停用")

    token = create_access_token(user.id, user.email)

    return AuthResponse(
        user_id=user.id,
        email=user.email,
        display_name=user.display_name,
        token=token,
        credits=user.credits,
    )


@router.get("/me", response_model=UserInfoResponse)
async def get_me(user: User = Depends(get_current_user)):
    """Get current authenticated user info."""
    return UserInfoResponse(
        user_id=user.id,
        email=user.email,
        display_name=user.display_name,
        credits=user.credits,
    )
