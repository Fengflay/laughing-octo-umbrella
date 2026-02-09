"""
Provider registry: register and look up image generation providers.

Usage:
    from app.services.provider_registry import ProviderRegistry

    provider = ProviderRegistry.get("gemini")
    result = await provider.generate(image_bytes, prompt, aspect_ratio)
"""

import logging
from typing import Optional

from app.services.provider_base import ImageProvider

logger = logging.getLogger(__name__)


class ProviderRegistry:
    """Central registry for image generation providers."""

    _providers: dict[str, ImageProvider] = {}
    _default: Optional[str] = None

    @classmethod
    def register(cls, provider: ImageProvider, is_default: bool = False) -> None:
        """Register an image provider."""
        cls._providers[provider.name] = provider
        if is_default or cls._default is None:
            cls._default = provider.name
        logger.info(f"Registered provider: {provider.name} (default={is_default})")

    @classmethod
    def get(cls, name: str) -> ImageProvider:
        """Get a provider by name. Raises KeyError if not found."""
        if name not in cls._providers:
            raise KeyError(f"Provider '{name}' not registered. Available: {list(cls._providers.keys())}")
        return cls._providers[name]

    @classmethod
    def get_default(cls) -> ImageProvider:
        """Get the default provider."""
        if not cls._default or cls._default not in cls._providers:
            raise RuntimeError("No default provider registered")
        return cls._providers[cls._default]

    @classmethod
    def list_providers(cls) -> list[str]:
        """List all registered provider names."""
        return list(cls._providers.keys())
