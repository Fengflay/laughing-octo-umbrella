"""Outdoor dynamic product photography style.

Key visual traits:
- Natural sunlight with dramatic skies
- Vibrant saturated colors, punchy color grading
- Active lifestyle environments (trails, beaches, parks, mountains)
- Motion-implied angles or slight motion blur
- GoPro/action camera aesthetic conveying adventure and energy
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="outdoor_dynamic",
    name="戶外動感",
    name_en="Outdoor Dynamic",
    description="戶外自然光，運動活力感，鮮明色彩，適合運動旅行戶外用品",
    icon="🌄",
    preview_color="#87CEEB",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Outdoor dynamic product photography, natural sunlight, "
                "vibrant saturated colors, energetic composition. "
            ),
            "suffix": (
                " Motion-implied angles, warm natural light, "
                "vivid color contrast, active lifestyle feel."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Dynamic outdoor product photography in a natural environment setting "
                "(trail, beach, park, mountain view), bright natural sunlight with dramatic sky, "
                "vibrant energetic atmosphere. "
            ),
            "suffix": (
                " Active lifestyle context (hiking trail, sports field, adventure setting), "
                "warm golden-hour or bright daylight, punchy saturated color grading, "
                "slight motion blur or dynamic angle suggesting movement, "
                "conveys adventure, freedom and athletic energy, "
                "GoPro/action camera aesthetic."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
