"""Studio Dramatic / Dark-background cinematic style definition.

Key visual traits:
- Dark or black studio backdrop with controlled dramatic lighting
- Strong rim / edge lighting to sculpt product contours
- High contrast with selective metallic and glossy highlights
- Cinematic, tech-premium atmosphere suited for 3C and sports gear
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="studio_dramatic",
    name="棚拍質感",
    name_en="Studio Dramatic",
    description="暗底棚拍風格，戲劇輪廓光，高對比質感，適合3C數碼運動用品",
    icon="🎬",
    preview_color="#1A1A2E",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Professional studio product photography with controlled dramatic lighting. "
                "Dark, neutral background. "
                "High contrast illumination emphasizing product form. "
            ),
            "suffix": (
                " Subtle rim lighting tracing the product contour. "
                "Sleek, premium feel with sharp, crisp details. "
                "Polished, high-end product presentation."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Dark-background studio product photography. "
                "Black or deep navy seamless backdrop with subtle gradient. "
                "Dramatic rim lighting and edge lighting sculpting the product silhouette. "
                "Carefully placed spot lights creating controlled specular highlights. "
            ),
            "suffix": (
                " High contrast ratio between product and background. "
                "Metallic and glossy surfaces catching precise highlight reflections. "
                "Product appears to float against the dark environment. "
                "Cinematic color grading: cool steel blues in shadows, "
                "warm highlights on key surfaces. "
                "Tech-premium atmosphere conveying power and precision. "
                "Magazine cover quality, razor-sharp focus on product details."
            ),
        },
    },
)

StyleRegistry.register_style(_style)
