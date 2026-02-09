from __future__ import annotations

import asyncio
import base64
import functools
import logging
from pathlib import Path

from app import config

logger = logging.getLogger(__name__)

_client = None
_current_key = ""


def _get_client():
    global _client, _current_key
    key = config.TOGETHER_API_KEY
    if not key:
        raise RuntimeError("Together AI API Key 未設定，請先到設定頁面填入 API Key")
    if _client is None or key != _current_key:
        from together import Together
        _client = Together(api_key=key)
        _current_key = key
    return _client


def _sync_generate(
    product_image_path: Path,
    prompt: str,
    width: int,
    height: int,
    steps: int,
) -> bytes:
    """Synchronous image generation — runs in a thread pool."""
    client = _get_client()

    image_bytes = product_image_path.read_bytes()
    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    mime_type = "image/png" if product_image_path.suffix == ".png" else "image/jpeg"
    data_url = f"data:{mime_type};base64,{image_b64}"

    response = client.images.generate(
        model="moonshotai/Kimi-K2.5",
        prompt=prompt,
        image_url=data_url,
        width=width,
        height=height,
        steps=steps,
        response_format="b64_json",
    )

    if response.data and len(response.data) > 0:
        b64_data = response.data[0].b64_json
        return base64.standard_b64decode(b64_data)

    raise RuntimeError("No image returned from Kimi K2.5 API")


async def generate_scene_image(
    product_image_path: Path,
    prompt: str,
    width: int = 1024,
    height: int = 1024,
    steps: int = 28,
) -> bytes:
    """Generate a scene image using Kimi K2.5 via Together AI.

    Uses run_in_executor to avoid blocking the asyncio event loop.

    Args:
        product_image_path: Path to the product image.
        prompt: Scene description prompt.
        width: Output width.
        height: Output height.
        steps: Generation steps.

    Returns:
        Generated image as bytes (PNG).
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        None,
        functools.partial(
            _sync_generate,
            product_image_path=product_image_path,
            prompt=prompt,
            width=width,
            height=height,
            steps=steps,
        ),
    )


# ---------------------------------------------------------------------------
# Provider interface wrapper (for provider_registry)
# ---------------------------------------------------------------------------

from app.services.provider_base import ImageProvider  # noqa: E402


def _sync_generate_from_bytes(
    image_bytes: bytes,
    prompt: str,
    width: int = 1024,
    height: int = 1024,
    steps: int = 28,
) -> bytes:
    """Kimi generation from pre-loaded image bytes."""
    import io
    import tempfile

    client = _get_client()

    image_b64 = base64.standard_b64encode(image_bytes).decode("utf-8")
    data_url = f"data:image/png;base64,{image_b64}"

    response = client.images.generate(
        model="moonshotai/Kimi-K2.5",
        prompt=prompt,
        image_url=data_url,
        width=width,
        height=height,
        steps=steps,
        response_format="b64_json",
    )

    if response.data and len(response.data) > 0:
        b64_data = response.data[0].b64_json
        return base64.standard_b64decode(b64_data)

    raise RuntimeError("No image returned from Kimi K2.5 API")


class KimiProvider(ImageProvider):
    """Kimi K2.5 image generation provider via Together AI."""

    @property
    def name(self) -> str:
        return "kimi"

    async def generate(
        self,
        image_bytes: bytes,
        prompt: str,
        aspect_ratio: str = "1:1",
    ) -> bytes:
        # Map aspect_ratio to width/height for Kimi
        ar_map = {
            "1:1": (1024, 1024),
            "3:4": (768, 1024),
            "4:3": (1024, 768),
            "9:16": (576, 1024),
            "16:9": (1024, 576),
        }
        width, height = ar_map.get(aspect_ratio, (1024, 1024))

        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None,
            functools.partial(
                _sync_generate_from_bytes,
                image_bytes=image_bytes,
                prompt=prompt,
                width=width,
                height=height,
            ),
        )
