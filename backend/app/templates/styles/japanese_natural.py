"""Japanese Natural / Wabi-Sabi style definition.

Key visual traits:
- Warm earth tones with natural wood and linen textures
- Soft ambient window light, gentle golden warmth
- Asymmetric composition embracing gentle imperfection
- Muji / zakka-inspired minimalism with seasonal accents
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="japanese_natural",
    name="日系自然",
    name_en="Japanese Natural",
    description="溫潤木紋亞麻底，自然光窗邊感，侘寂美學，適合居家食品文具",
    icon="🍃",
    preview_color="#D4C5B2",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Japanese natural aesthetic product photography. "
                "Warm earth tones with soft ambient light. "
                "Natural wood grain and linen textures as base surfaces. "
            ),
            "suffix": (
                " Asymmetric, off-center composition embracing gentle imperfection. "
                "Tranquil, meditative atmosphere. "
                "Muted warm tones, understated elegance, clean simplicity."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Japanese zakka and Muji-inspired product photography. "
                "Set beside a window with soft, diffused natural light "
                "streaming in from the left. "
                "Raw light-oak wood table surface, "
                "natural linen or cotton cloth as backdrop accent. "
                "Warm, unhurried morning atmosphere. "
            ),
            "suffix": (
                " Styled following wabi-sabi principles: beauty in simplicity "
                "and gentle imperfection. "
                "A single seasonal accent prop: a small ceramic tea cup, "
                "a sprig of dried pampas grass, a linen napkin, "
                "or a handmade pottery plate. "
                "Warm golden light with soft shadows from window frame. "
                "Color grading: warm midtones, slightly desaturated, "
                "creamy highlights. "
                "Conveys handcrafted quality and mindful living. "
                "Calm, editorial, zakka-magazine composition."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
