"""
Audit log middleware.

Records significant user actions (mutations) to the database for
compliance and debugging purposes.

Only logs POST/PUT/PATCH/DELETE requests to /api/ endpoints.
"""

import logging
import time
from datetime import datetime, timezone

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.database import AsyncSessionLocal

logger = logging.getLogger("app.audit")

# Paths that should be audited (mutation endpoints)
AUDIT_METHODS = {"POST", "PUT", "PATCH", "DELETE"}

# Paths to skip (high-volume read-only, auth, or static)
SKIP_PATHS = {
    "/api/health",
    "/api/auth/me",
}


def _get_user_id_from_request(request: Request) -> str | None:
    """Try to extract user_id from JWT without full auth dependency."""
    auth_header = request.headers.get("Authorization", "")
    token = None
    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
    elif request.query_params.get("token"):
        token = request.query_params.get("token")

    if not token:
        return None

    try:
        from app.auth import decode_token
        payload = decode_token(token)
        return payload.get("sub")
    except Exception:
        return None


class AuditLogMiddleware(BaseHTTPMiddleware):
    """Logs mutation API requests to the database audit_logs table."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        path = request.url.path
        method = request.method

        # Only audit mutation methods on API paths
        if method not in AUDIT_METHODS or not path.startswith("/api/"):
            return await call_next(request)

        # Skip noisy paths
        if path in SKIP_PATHS:
            return await call_next(request)

        start_time = time.time()
        user_id = _get_user_id_from_request(request)
        request_id = getattr(request.state, "request_id", None)

        # Execute the request
        response = await call_next(request)

        duration_ms = int((time.time() - start_time) * 1000)
        status_code = response.status_code

        # Log to database asynchronously (non-blocking)
        try:
            await _write_audit_log(
                request_id=request_id,
                user_id=user_id,
                method=method,
                path=path,
                status_code=status_code,
                duration_ms=duration_ms,
                client_ip=request.client.host if request.client else None,
            )
        except Exception as e:
            logger.warning(f"Failed to write audit log: {e}")

        return response


async def _write_audit_log(
    request_id: str | None,
    user_id: str | None,
    method: str,
    path: str,
    status_code: int,
    duration_ms: int,
    client_ip: str | None,
) -> None:
    """Write a single audit log entry to the database."""
    try:
        from sqlalchemy import text
        async with AsyncSessionLocal() as db:
            await db.execute(
                text("""
                    INSERT INTO audit_logs
                    (request_id, user_id, method, path, status_code, duration_ms, client_ip, created_at)
                    VALUES (:request_id, :user_id, :method, :path, :status_code, :duration_ms, :client_ip, :created_at)
                """),
                {
                    "request_id": request_id,
                    "user_id": user_id,
                    "method": method,
                    "path": path,
                    "status_code": status_code,
                    "duration_ms": duration_ms,
                    "client_ip": client_ip,
                    "created_at": datetime.now(timezone.utc).isoformat(),
                },
            )
            await db.commit()
    except Exception as e:
        # If the table doesn't exist yet (first run), log and skip
        logger.debug(f"Audit log write skipped: {e}")
