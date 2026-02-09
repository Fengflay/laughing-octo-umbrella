"""
Authentication utilities: JWT tokens + password hashing.

Provides FastAPI dependencies for protecting endpoints.
"""

from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
from fastapi import Depends, HTTPException, Query, Request, status
from jose import JWTError, jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import JWT_ALGORITHM, JWT_EXPIRY_HOURS, JWT_SECRET
from app.database import get_db
from app.models.db_models import User


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its bcrypt hash."""
    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
    except Exception:
        return False


def create_access_token(user_id: str, email: str) -> str:
    """Create a JWT token with user_id and email claims."""
    expire = datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRY_HOURS)
    payload = {
        "sub": user_id,
        "email": email,
        "exp": expire,
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    """Decode and validate a JWT token. Raises JWTError on failure."""
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])


def _extract_token(request: Request, token_query: Optional[str] = None) -> Optional[str]:
    """Extract Bearer token from Authorization header or query param.

    Query param fallback is needed for SSE (EventSource cannot set headers).
    """
    # Try Authorization header first
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        return auth_header[7:]

    # Fallback to query param (for SSE endpoints)
    if token_query:
        return token_query

    return None


async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
    token: Optional[str] = Query(None, alias="token"),
) -> User:
    """FastAPI dependency: requires authenticated user.

    Extracts JWT from Authorization header or ?token= query param.
    Returns the User ORM object.
    Raises 401 if not authenticated.
    """
    raw_token = _extract_token(request, token)
    if not raw_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="未登入，請先登入",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        payload = decode_token(raw_token)
        user_id: str = payload.get("sub", "")
        if not user_id:
            raise HTTPException(status_code=401, detail="無效的登入令牌")
    except JWTError:
        raise HTTPException(status_code=401, detail="登入令牌已過期或無效")

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="用戶不存在或已停用")

    return user


async def get_optional_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
    token: Optional[str] = Query(None, alias="token"),
) -> Optional[User]:
    """FastAPI dependency: optional authentication.

    Returns User if valid token is present, None otherwise.
    Used during Phase 1 transition (existing endpoints work without auth).
    """
    raw_token = _extract_token(request, token)
    if not raw_token:
        return None

    try:
        payload = decode_token(raw_token)
        user_id: str = payload.get("sub", "")
        if not user_id:
            return None
    except JWTError:
        return None

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        return None

    return user
