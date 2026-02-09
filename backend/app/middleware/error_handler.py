"""
Global error handler middleware.

Catches unhandled exceptions, logs them with the request ID,
and returns a standardized JSON error response.
"""

import logging
import traceback
import uuid

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse

logger = logging.getLogger("app.error_handler")


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """Catches all unhandled exceptions and returns structured JSON errors."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Generate a unique request ID for tracing
        request_id = uuid.uuid4().hex[:8]
        request.state.request_id = request_id

        try:
            response = await call_next(request)
            # Attach request ID to response header for debugging
            response.headers["X-Request-ID"] = request_id
            return response

        except Exception as exc:
            # Log the full traceback
            logger.error(
                f"[{request_id}] Unhandled exception on {request.method} {request.url.path}: "
                f"{type(exc).__name__}: {exc}\n{traceback.format_exc()}"
            )

            # Determine error code
            status_code = getattr(exc, "status_code", 500)
            detail = getattr(exc, "detail", None)

            if status_code == 500 or detail is None:
                detail = "伺服器內部錯誤，請稍後再試"

            return JSONResponse(
                status_code=status_code,
                content={
                    "detail": detail,
                    "request_id": request_id,
                },
                headers={"X-Request-ID": request_id},
            )
