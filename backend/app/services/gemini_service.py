from __future__ import annotations

import asyncio
import functools
import logging
from pathlib import Path

from PIL import Image

from app import config

logger = logging.getLogger(__name__)

_client = None
_current_key = ""


def _get_client():
    global _client, _current_key
    key = config.GEMINI_API_KEY
    if not key:
        raise RuntimeError("Gemini API Key 未設定，請先到設定頁面填入 API Key")
    if _client is None or key != _current_key:
        from google import genai
        _client = genai.Client(api_key=key)
        _current_key = key
    return _client


def _sync_generate(
    product_image_path: Path,
    prompt: str,
    aspect_ratio: str,
    model: str,
) -> bytes:
    """Synchronous image generation — runs in a thread pool to avoid blocking the event loop."""
    from google.genai import types

    client = _get_client()
    input_image = Image.open(product_image_path)

    response = client.models.generate_content(
        model=model,
        contents=[prompt, input_image],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
        ),
    )

    for part in response.parts:
        if part.inline_data is not None:
            result_image = part.as_image()
            return result_image.image_bytes

    raise RuntimeError("No image returned from Gemini API")


def _sync_generate_from_bytes(
    image_bytes: bytes,
    prompt: str,
    aspect_ratio: str,
    model: str,
) -> bytes:
    """Synchronous image generation from pre-loaded image bytes.

    Avoids re-reading the same product image from disk for every generation call
    within a batch, reducing I/O overhead significantly.
    """
    import io

    from google.genai import types

    client = _get_client()
    input_image = Image.open(io.BytesIO(image_bytes))

    response = client.models.generate_content(
        model=model,
        contents=[prompt, input_image],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
        ),
    )

    for part in response.parts:
        if part.inline_data is not None:
            result_image = part.as_image()
            return result_image.image_bytes

    raise RuntimeError("No image returned from Gemini API")


async def generate_scene_image(
    product_image_path: Path,
    prompt: str,
    aspect_ratio: str = "1:1",
    model: str = "gemini-2.5-flash-image",
) -> bytes:
    """Generate a scene image using Gemini Image API.

    Uses run_in_executor to avoid blocking the asyncio event loop,
    so SSE progress events can still be pushed while generating.

    Args:
        product_image_path: Path to the product image (preferably background-removed).
        prompt: Scene description prompt.
        aspect_ratio: Output aspect ratio.
        model: Gemini model to use.

    Returns:
        Generated image as PNG bytes.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        None,
        functools.partial(
            _sync_generate,
            product_image_path=product_image_path,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            model=model,
        ),
    )


async def generate_scene_image_from_bytes(
    image_bytes: bytes,
    prompt: str,
    aspect_ratio: str = "1:1",
    model: str = "gemini-2.5-flash-image",
) -> bytes:
    """Generate a scene image from pre-loaded image bytes.

    Optimized version that avoids repeated disk reads when generating
    multiple images from the same product photo in a batch.

    Args:
        image_bytes: Pre-loaded product image bytes.
        prompt: Scene description prompt.
        aspect_ratio: Output aspect ratio.
        model: Gemini model to use.

    Returns:
        Generated image as PNG bytes.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        None,
        functools.partial(
            _sync_generate_from_bytes,
            image_bytes=image_bytes,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
            model=model,
        ),
    )


# ---------------------------------------------------------------------------
# Provider interface wrapper (for provider_registry)
# ---------------------------------------------------------------------------

from app.services.provider_base import ImageProvider  # noqa: E402


class GeminiProvider(ImageProvider):
    """Gemini image generation provider."""

    @property
    def name(self) -> str:
        return "gemini"

    async def generate(
        self,
        image_bytes: bytes,
        prompt: str,
        aspect_ratio: str = "1:1",
    ) -> bytes:
        return await generate_scene_image_from_bytes(
            image_bytes=image_bytes,
            prompt=prompt,
            aspect_ratio=aspect_ratio,
        )
