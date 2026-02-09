from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

from app import config

router = APIRouter(prefix="/api", tags=["settings"])

ENV_FILE = config.BASE_DIR / ".env"


class ApiKeysRequest(BaseModel):
    gemini_api_key: str | None = None
    together_api_key: str | None = None


class ApiKeysStatus(BaseModel):
    gemini_configured: bool
    together_configured: bool
    gemini_key_preview: str
    together_key_preview: str


def _mask_key(key: str) -> str:
    """Show first 4 and last 4 chars, mask the rest."""
    if not key or len(key) < 10:
        return "未設定" if not key else "****"
    return f"{key[:4]}{'*' * (len(key) - 8)}{key[-4:]}"


def _read_env() -> dict[str, str]:
    """Read existing .env file into a dict."""
    env_vars: dict[str, str] = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env_vars[k.strip()] = v.strip()
    return env_vars


def _write_env(env_vars: dict[str, str]) -> None:
    """Write dict back to .env file."""
    lines = [f"{k}={v}" for k, v in env_vars.items()]
    ENV_FILE.write_text("\n".join(lines) + "\n")


@router.get("/settings/api-keys", response_model=ApiKeysStatus)
async def get_api_keys_status():
    """Get current API key configuration status."""
    return ApiKeysStatus(
        gemini_configured=bool(config.GEMINI_API_KEY),
        together_configured=bool(config.TOGETHER_API_KEY),
        gemini_key_preview=_mask_key(config.GEMINI_API_KEY),
        together_key_preview=_mask_key(config.TOGETHER_API_KEY),
    )


@router.post("/settings/api-keys", response_model=ApiKeysStatus)
async def save_api_keys(req: ApiKeysRequest):
    """Save API keys to .env and reload config."""
    env_vars = _read_env()

    if req.gemini_api_key is not None:
        env_vars["GEMINI_API_KEY"] = req.gemini_api_key
        config.GEMINI_API_KEY = req.gemini_api_key

    if req.together_api_key is not None:
        env_vars["TOGETHER_API_KEY"] = req.together_api_key
        config.TOGETHER_API_KEY = req.together_api_key

    _write_env(env_vars)

    # Reset cached API clients so they pick up new keys
    from app.services import gemini_service, kimi_service
    gemini_service._client = None
    kimi_service._client = None

    return ApiKeysStatus(
        gemini_configured=bool(config.GEMINI_API_KEY),
        together_configured=bool(config.TOGETHER_API_KEY),
        gemini_key_preview=_mask_key(config.GEMINI_API_KEY),
        together_key_preview=_mask_key(config.TOGETHER_API_KEY),
    )
