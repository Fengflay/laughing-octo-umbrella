from __future__ import annotations

import io
from pathlib import Path

from PIL import Image
from rembg import remove


def remove_background(input_path: Path, output_path: Path) -> Path:
    """Remove background from product image using rembg."""
    input_image = Image.open(input_path)
    output_image = remove(input_image)

    # Ensure RGBA for transparency
    if output_image.mode != "RGBA":
        output_image = output_image.convert("RGBA")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_image.save(output_path, format="PNG")
    return output_path


def remove_background_bytes(image_bytes: bytes) -> bytes:
    """Remove background from image bytes, return PNG bytes."""
    input_image = Image.open(io.BytesIO(image_bytes))
    output_image = remove(input_image)

    if output_image.mode != "RGBA":
        output_image = output_image.convert("RGBA")

    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    return buf.getvalue()
