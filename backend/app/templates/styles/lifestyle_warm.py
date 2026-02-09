"""Warm lifestyle product photography style.

Key visual traits:
- Warm color temperature (5800K+), soft bounced lighting
- Cozy home/kitchen/living room settings
- Natural props: wooden surfaces, linen, green plants, coffee cups
- Orange-tinted color grading, gentle depth of field
- Conveys comfort, trust, and genuine daily-life atmosphere
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="lifestyle_warm",
    name="暖調情境",
    name_en="Warm Lifestyle",
    description="暖色溫場景照，生活化佈置，有人情味，適合食品母嬰居家用品",
    icon="🏡",
    preview_color="#F5E6D3",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Warm lifestyle product photography, warm color temperature (5800K+), "
                "soft bounced light, inviting homey feel. "
            ),
            "suffix": (
                " Natural props (wooden cutting board, linen napkin, green plant), "
                "warm shadows, genuine daily-life atmosphere."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Warm lifestyle scene photography, cozy home/kitchen/living room setting, "
                "afternoon golden light through window, warm wood table with fabric textures. "
            ),
            "suffix": (
                " Styled like real daily life (coffee cup, book, woven basket, fresh flowers), "
                "warm orange-tinted color grading, gentle depth of field, "
                "conveys comfort and trust, feels like a home not a studio."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
