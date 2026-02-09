"""
Abstract base class for image generation providers.

All providers (Gemini, Kimi, Banana Pro, etc.) must implement this interface.
This enables hot-swapping providers without changing the generation pipeline.
"""

from abc import ABC, abstractmethod


class ImageProvider(ABC):
    """Abstract image generation provider."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name (e.g., 'gemini', 'kimi', 'banana_pro')."""
        ...

    @abstractmethod
    async def generate(
        self,
        image_bytes: bytes,
        prompt: str,
        aspect_ratio: str = "1:1",
    ) -> bytes:
        """Generate a scene image from product image + prompt.

        Args:
            image_bytes: Product image as PNG/JPEG bytes
            prompt: Full assembled prompt (with style injection)
            aspect_ratio: Target aspect ratio (e.g., "1:1", "3:4")

        Returns:
            Generated image as PNG bytes

        Raises:
            Exception on generation failure
        """
        ...
