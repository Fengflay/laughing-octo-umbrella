"""Luxury Editorial / Marble-and-metal premium style definition.

Key visual traits:
- Marble and metallic surfaces (gold, rose-gold accents)
- Diffused studio lighting with soft, even illumination
- Minimal, curated composition with intentional negative space
- Fashion-magazine quality, premium brand aesthetic
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="luxury_editorial",
    name="輕奢編輯",
    name_en="Luxury Editorial",
    description="大理石/金屬質感，編輯風格，極簡高端，適合包包飾品美妝",
    icon="✨",
    preview_color="#F5F0EB",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Luxury editorial product photography. "
                "Marble or metallic surface as base. "
                "Diffused, even studio lighting with a neutral luxury palette. "
            ),
            "suffix": (
                " Minimal props, refined matte and gloss textures. "
                "Shallow depth of field drawing focus to the product. "
                "Premium brand feel, clean and aspirational."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "High-end editorial product photography. "
                "White marble surface with subtle gold or rose-gold metallic accents. "
                "Scandinavian luxury interior setting, bright and airy. "
                "Soft, diffused studio lighting from a large overhead softbox "
                "creating gentle, wrapped illumination. "
            ),
            "suffix": (
                " Minimal, curated props: a single stem flower, "
                "a piece of draped silk fabric, or a slender gold tray. "
                "Clean composition with intentional negative space. "
                "Shallow depth of field with creamy bokeh on background elements. "
                "Color grading: neutral warm whites, soft ivory tones, "
                "delicate contrast preserving texture detail. "
                "Conveys premium quality and understated sophistication. "
                "Fashion magazine editorial composition."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
