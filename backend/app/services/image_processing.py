"""Image processing helpers for platform-specific optimisation.

Currently supports Shopee (蝦皮) requirements:
  - Max file size: 2 MB
  - Max resolution: 1024×1024
  - Format: JPEG (RGB) or PNG; strips alpha channel unless the source is
    a background-removed image (detected by existing RGBA mode).
"""

from __future__ import annotations

import io
import logging
from pathlib import Path

from PIL import Image

logger = logging.getLogger(__name__)

# Shopee constraints
SHOPEE_MAX_BYTES = 2 * 1024 * 1024  # 2 MB
SHOPEE_MAX_DIMENSION = 1024
SHOPEE_QUALITY_STEPS = [95, 85, 75, 65]


def optimize_for_shopee(image_path: str) -> str:
    """Optimize an image file in-place for Shopee platform requirements.

    1. Downscale to fit within 1024×1024 (preserving aspect ratio).
    2. Convert to JPEG (RGB) unless the image has meaningful transparency.
    3. Progressively reduce JPEG quality until file size ≤ 2 MB.

    Returns the (possibly changed) output path — the extension may switch
    from .png to .jpg if the format changed.
    """
    img = Image.open(image_path)
    p = Path(image_path)

    # --- Resolution cap ---
    if img.width > SHOPEE_MAX_DIMENSION or img.height > SHOPEE_MAX_DIMENSION:
        img.thumbnail((SHOPEE_MAX_DIMENSION, SHOPEE_MAX_DIMENSION), Image.LANCZOS)
        logger.info(f"Shopee resize: {p.name} → {img.width}x{img.height}")

    # --- Format decision ---
    # Keep PNG only if the image has a meaningful alpha channel (bg-removed).
    has_alpha = img.mode == "RGBA" and img.getextrema()[3][0] < 255
    if has_alpha:
        fmt = "PNG"
        ext = "png"
    else:
        fmt = "JPEG"
        ext = "jpg"
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

    # --- Size cap (progressive quality reduction for JPEG) ---
    if fmt == "JPEG":
        for quality in SHOPEE_QUALITY_STEPS:
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=quality, optimize=True)
            if buf.tell() <= SHOPEE_MAX_BYTES:
                out_path = p.with_suffix(f".{ext}")
                out_path.write_bytes(buf.getvalue())
                logger.info(
                    f"Shopee optimize: {p.name} → {out_path.name} "
                    f"(quality={quality}, size={buf.tell()} bytes)"
                )
                return str(out_path)
        # Even at lowest quality it's too big — save anyway at lowest quality
        out_path = p.with_suffix(f".{ext}")
        buf.seek(0)
        out_path.write_bytes(buf.getvalue())
        logger.warning(f"Shopee optimize: {p.name} still exceeds 2 MB at quality={SHOPEE_QUALITY_STEPS[-1]}")
        return str(out_path)
    else:
        # PNG — just save the resized version
        buf = io.BytesIO()
        img.save(buf, format="PNG", optimize=True)
        if buf.tell() > SHOPEE_MAX_BYTES:
            # Fallback: convert to JPEG even if it has alpha
            img_rgb = img.convert("RGB")
            for quality in SHOPEE_QUALITY_STEPS:
                jbuf = io.BytesIO()
                img_rgb.save(jbuf, format="JPEG", quality=quality, optimize=True)
                if jbuf.tell() <= SHOPEE_MAX_BYTES:
                    out_path = p.with_suffix(".jpg")
                    out_path.write_bytes(jbuf.getvalue())
                    logger.info(
                        f"Shopee optimize (PNG→JPG fallback): {p.name} → {out_path.name} "
                        f"(quality={quality}, size={jbuf.tell()} bytes)"
                    )
                    return str(out_path)
            out_path = p.with_suffix(".jpg")
            jbuf.seek(0)
            out_path.write_bytes(jbuf.getvalue())
            return str(out_path)
        else:
            out_path = p.with_suffix(".png")
            out_path.write_bytes(buf.getvalue())
            return str(out_path)


def optimize_bytes_for_shopee(image_bytes: bytes) -> tuple[bytes, str]:
    """Optimize in-memory image bytes for Shopee. Returns (bytes, extension).

    Used by the download_all route to optimize images before zipping.
    """
    img = Image.open(io.BytesIO(image_bytes))

    # --- Resolution cap ---
    if img.width > SHOPEE_MAX_DIMENSION or img.height > SHOPEE_MAX_DIMENSION:
        img.thumbnail((SHOPEE_MAX_DIMENSION, SHOPEE_MAX_DIMENSION), Image.LANCZOS)

    # --- Format decision ---
    has_alpha = img.mode == "RGBA" and img.getextrema()[3][0] < 255
    if has_alpha:
        fmt = "PNG"
        ext = "png"
    else:
        fmt = "JPEG"
        ext = "jpg"
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

    # --- Size cap ---
    if fmt == "JPEG":
        for quality in SHOPEE_QUALITY_STEPS:
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=quality, optimize=True)
            if buf.tell() <= SHOPEE_MAX_BYTES:
                return buf.getvalue(), ext
        return buf.getvalue(), ext
    else:
        buf = io.BytesIO()
        img.save(buf, format="PNG", optimize=True)
        if buf.tell() <= SHOPEE_MAX_BYTES:
            return buf.getvalue(), ext
        # Fallback: convert to JPEG
        img_rgb = img.convert("RGB")
        for quality in SHOPEE_QUALITY_STEPS:
            jbuf = io.BytesIO()
            img_rgb.save(jbuf, format="JPEG", quality=quality, optimize=True)
            if jbuf.tell() <= SHOPEE_MAX_BYTES:
                return jbuf.getvalue(), "jpg"
        return jbuf.getvalue(), "jpg"
