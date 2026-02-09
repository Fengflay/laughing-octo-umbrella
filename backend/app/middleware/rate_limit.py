"""
Rate limiting middleware using in-memory sliding window counters.

Rules:
- Generation endpoints: 10 requests / hour / user
- General API: 100 requests / minute / user
- Anonymous (by IP): same limits but tracked by IP

Returns 429 Too Many Requests with Retry-After header when exceeded.
"""

import time
from collections import defaultdict
from typing import Optional

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse


class SlidingWindowCounter:
    """Simple in-memory sliding window rate limiter."""

    def __init__(self):
        # key -> list of timestamps
        self._windows: dict[str, list[float]] = defaultdict(list)

    def is_allowed(self, key: str, max_requests: int, window_seconds: int) -> tuple[bool, int]:
        """Check if request is allowed under the rate limit.

        Returns:
            (allowed, retry_after_seconds)
        """
        now = time.time()
        cutoff = now - window_seconds

        # Clean old entries
        timestamps = self._windows[key]
        self._windows[key] = [t for t in timestamps if t > cutoff]
        timestamps = self._windows[key]

        if len(timestamps) >= max_requests:
            # Calculate when the oldest entry will expire
            oldest = min(timestamps) if timestamps else now
            retry_after = int(oldest + window_seconds - now) + 1
            return False, max(retry_after, 1)

        # Record this request
        timestamps.append(now)
        return True, 0

    def cleanup(self):
        """Remove empty keys to prevent memory growth."""
        empty_keys = [k for k, v in self._windows.items() if not v]
        for k in empty_keys:
            del self._windows[k]


# Global counters
_generation_limiter = SlidingWindowCounter()
_general_limiter = SlidingWindowCounter()

# Rate limit config
GENERATION_LIMIT = 10  # per hour
GENERATION_WINDOW = 3600  # 1 hour in seconds
GENERAL_LIMIT = 100  # per minute
GENERAL_WINDOW = 60  # 1 minute in seconds

# Paths that count as "generation" (more expensive operations)
GENERATION_PATHS = {
    "/api/generate",
    "/api/generate-copy",
}

# Paths that should be excluded from rate limiting
EXCLUDED_PATHS = {
    "/api/health",
    "/api/auth/login",
    "/api/auth/register",
    "/api/uploads",
    "/api/outputs",
}


def _get_identifier(request: Request) -> str:
    """Get rate limit key: user_id from JWT if available, otherwise client IP."""
    # Try to get user from request state (set by auth dependency)
    # Since middleware runs before dependencies, we parse the token manually
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
        try:
            from app.auth import decode_token
            payload = decode_token(token)
            user_id = payload.get("sub", "")
            if user_id:
                return f"user:{user_id}"
        except Exception:
            pass

    # Fallback: query param token (SSE endpoints)
    token_param = request.query_params.get("token")
    if token_param:
        try:
            from app.auth import decode_token
            payload = decode_token(token_param)
            user_id = payload.get("sub", "")
            if user_id:
                return f"user:{user_id}"
        except Exception:
            pass

    # Fallback to IP
    client_ip = request.client.host if request.client else "unknown"
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        client_ip = forwarded.split(",")[0].strip()
    return f"ip:{client_ip}"


def _is_excluded(path: str) -> bool:
    """Check if path should be excluded from rate limiting."""
    for excluded in EXCLUDED_PATHS:
        if path.startswith(excluded):
            return True
    return False


def _is_generation(path: str, method: str) -> bool:
    """Check if this is a generation endpoint (stricter limit)."""
    if method != "POST":
        return False
    for gen_path in GENERATION_PATHS:
        if path.startswith(gen_path):
            return True
    # Also match regenerate / variants
    if "/regenerate" in path or "/variants/" in path:
        return True
    return False


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limiting middleware with per-user sliding window counters."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        path = request.url.path
        method = request.method

        # Skip excluded paths and non-API paths
        if not path.startswith("/api/") or _is_excluded(path):
            return await call_next(request)

        # Skip GET for static assets
        if method == "GET" and (path.startswith("/api/uploads/") or path.startswith("/api/outputs/")):
            return await call_next(request)

        identifier = _get_identifier(request)

        # Check generation-specific rate limit
        if _is_generation(path, method):
            allowed, retry_after = _generation_limiter.is_allowed(
                f"gen:{identifier}", GENERATION_LIMIT, GENERATION_WINDOW
            )
            if not allowed:
                return JSONResponse(
                    status_code=429,
                    content={
                        "detail": f"生成請求過於頻繁，請 {retry_after} 秒後再試",
                        "retry_after": retry_after,
                    },
                    headers={"Retry-After": str(retry_after)},
                )

        # Check general rate limit
        allowed, retry_after = _general_limiter.is_allowed(
            f"api:{identifier}", GENERAL_LIMIT, GENERAL_WINDOW
        )
        if not allowed:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": f"請求過於頻繁，請 {retry_after} 秒後再試",
                    "retry_after": retry_after,
                },
                headers={"Retry-After": str(retry_after)},
            )

        return await call_next(request)
