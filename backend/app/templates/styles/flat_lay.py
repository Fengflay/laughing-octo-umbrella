"""Flat lay overhead product photography style.

Key visual traits:
- Perfect 90-degree top-down camera angle
- Organized symmetrical or grid-based arrangement
- Shadow-free even illumination from large overhead softbox
- Clean surface backgrounds (white, marble, pastel)
- Instagram-worthy bird's eye visual storytelling
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="flat_lay",
    name="平拍排列",
    name_en="Flat Lay",
    description="俯拍90度排列組合，適合展示套裝配件，適合飾品美妝文具",
    icon="📐",
    preview_color="#E8E4F0",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Flat lay overhead product photography, 90-degree top-down angle, "
                "organized symmetrical arrangement, clean background surface. "
            ),
            "suffix": (
                " Even shadow-free lighting from directly above, neat organized composition, "
                "each item clearly visible, satisfying visual order."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Professional flat lay product photography, perfect 90-degree overhead angle, "
                "products arranged on a clean surface (white/marble/pastel), "
                "with curated complementary props around the main product. "
            ),
            "suffix": (
                " Styled arrangement with complementary items "
                "(small plants, stationery, fabric swatches, decorative elements), "
                "perfect grid or radial layout, Instagram-worthy bird's eye composition, "
                "shadow-free even illumination from large overhead softbox, "
                "clean and organized visual storytelling."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
