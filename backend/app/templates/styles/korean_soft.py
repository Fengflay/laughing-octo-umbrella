"""Korean Soft / Dreamy Pastel style definition.

Key visual traits:
- Soft, dreamy pastel color palette (baby pink, lavender, mint, cream)
- Bright, even lighting with minimal shadows (flat light / ring light)
- Romantic, delicate props: dried flowers, satin ribbons, pearl accents
- Lifted shadows, gentle color grading for youthful, aspirational look
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="korean_soft",
    name="韓系柔光",
    name_en="Korean Soft",
    description="柔和粉彩色調，明亮無陰影打光，乾燥花/緞帶道具，適合服飾美妝飾品",
    icon="🌸",
    preview_color="#F8E8F0",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Soft dreamy Korean aesthetic product photography. "
                "Bright, even lighting with almost no shadows. "
                "Gentle pastel palette: blush pink, cream, lavender, and mint tones. "
            ),
            "suffix": (
                " Styled with delicate props: a sprig of dried baby's breath, "
                "thin satin ribbon, or small pearl accents. "
                "Lifted shadows, soft highlight roll-off. "
                "Clean, polished, e-commerce-ready composition."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Korean lifestyle editorial product photography (K-style soft light). "
                "Set in a bright, airy pastel-toned space: "
                "soft pink or cream background, light marble or matte tabletop, "
                "lavender and mint accent tones throughout the scene. "
                "Ring light or large diffused softbox creating perfectly even, "
                "shadow-free illumination on the product. "
            ),
            "suffix": (
                " Styled with dreamy K-beauty inspired props: "
                "dried flower arrangement (baby's breath, cotton stems), "
                "satin ribbon loosely draped, small pearl dish, "
                "pastel ceramic tray, or a clear glass with sparkling water. "
                "Soft gaussian background blur for gentle dreamy bokeh. "
                "Color grading: lifted blacks, reduced contrast, "
                "subtle pink and lavender tint in highlights. "
                "Conveys youthful elegance and curated lifestyle. "
                "Aspirational, scroll-stopping e-commerce aesthetic."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
