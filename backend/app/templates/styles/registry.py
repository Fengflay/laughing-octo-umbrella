"""Style registry: manages visual style definitions and prompt injection logic.

The style system is an orthogonal modifier layer that wraps around existing
template prompts. Instead of creating N*M combinations (templates x styles),
each style defines prefix/suffix modifiers at different injection levels.

Injection levels:
- NONE: No style modification. Used for templates where style would hurt
  quality (white background, selling points, size reference).
- LIGHT: Gentle style hints added. Used for close-ups and detail shots
  where style should influence texture/lighting but not dominate.
- FULL: Complete style immersion. Used for lifestyle scenes, model shots,
  and brand atmosphere shots where the style defines the setting.

Each template has an injection_level field (defaulting to FULL) that
determines how much style influence it receives.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class InjectionLevel(str, Enum):
    """How much style should be injected into a template's prompt."""
    NONE = "none"
    LIGHT = "light"
    FULL = "full"


@dataclass
class StyleDefinition:
    """A visual style that can be applied to any product template."""
    id: str
    name: str
    name_en: str
    description: str
    icon: str
    preview_color: str  # Hex color for UI card background
    modifiers: dict[InjectionLevel, dict[str, str]] = field(default_factory=dict)
    # modifiers structure: { InjectionLevel.LIGHT: {"prefix": "...", "suffix": "..."}, ... }


class StyleRegistry:
    """Central registry for all visual styles."""
    _styles: dict[str, StyleDefinition] = {}

    # 品類 → 推薦風格列表（有序，第一個為推薦）
    CATEGORY_STYLES: dict[str, list[str]] = {
        "bags": ["korean_soft", "luxury_editorial", "lifestyle_warm"],
        "jewelry": ["korean_soft", "flat_lay", "luxury_editorial"],
        "clothing": ["korean_soft", "japanese_natural", "lifestyle_warm"],
        "shoes": ["korean_soft", "studio_dramatic", "outdoor_dynamic"],
        "electronics": ["studio_dramatic", "japanese_natural", "flat_lay"],
        "beauty": ["korean_soft", "flat_lay", "luxury_editorial"],
        "home": ["japanese_natural", "lifestyle_warm", "korean_soft"],
        "toys": ["lifestyle_warm", "flat_lay", "korean_soft"],
        "sports": ["studio_dramatic", "outdoor_dynamic", "lifestyle_warm"],
        "food": ["japanese_natural", "lifestyle_warm", "flat_lay"],
        "stationery": ["japanese_natural", "flat_lay", "korean_soft"],
        "pets": ["lifestyle_warm", "japanese_natural", "korean_soft"],
        "automotive": ["studio_dramatic", "outdoor_dynamic", "lifestyle_warm"],
        "phones": ["studio_dramatic", "flat_lay", "korean_soft"],
        "travel": ["luxury_editorial", "outdoor_dynamic", "lifestyle_warm"],
        "fashion_acc": ["korean_soft", "luxury_editorial", "flat_lay"],
        "kitchenware": ["japanese_natural", "flat_lay", "lifestyle_warm"],
        "health": ["japanese_natural", "lifestyle_warm", "korean_soft"],
        "hobbies": ["lifestyle_warm", "japanese_natural", "studio_dramatic"],
        "motorcycle": ["studio_dramatic", "outdoor_dynamic", "lifestyle_warm"],
    }

    @classmethod
    def register_style(cls, style: StyleDefinition) -> None:
        cls._styles[style.id] = style

    @classmethod
    def get_style(cls, style_id: str) -> StyleDefinition | None:
        return cls._styles.get(style_id)

    @classmethod
    def get_all_styles(cls) -> list[StyleDefinition]:
        return list(cls._styles.values())

    @classmethod
    def get_styles_for_category(cls, product_type: str) -> list[StyleDefinition]:
        """取得某品類的推薦風格列表（有序，第一個為推薦）"""
        style_ids = cls.CATEGORY_STYLES.get(product_type, [])
        return [cls._styles[sid] for sid in style_ids if sid in cls._styles]

    @classmethod
    def assemble_prompt(
        cls,
        base_prompt: str,
        style_id: str | None,
        injection_level: InjectionLevel,
    ) -> str:
        """Assemble final prompt by injecting style modifiers around base prompt.

        Args:
            base_prompt: The template's original prompt.
            style_id: The style to apply (None = no style).
            injection_level: How much style to inject (NONE/LIGHT/FULL).

        Returns:
            The assembled prompt with style modifiers.
        """
        if not style_id or injection_level == InjectionLevel.NONE:
            return base_prompt

        style = cls._styles.get(style_id)
        if not style:
            return base_prompt

        modifier = style.modifiers.get(injection_level)
        if not modifier:
            # If requested level doesn't exist, try falling back to LIGHT
            if injection_level == InjectionLevel.FULL:
                modifier = style.modifiers.get(InjectionLevel.LIGHT)
            if not modifier:
                return base_prompt

        prefix = modifier.get("prefix", "")
        suffix = modifier.get("suffix", "")

        return f"{prefix}{base_prompt}{suffix}"
