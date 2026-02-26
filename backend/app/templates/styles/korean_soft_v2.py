"""
優化後的風格定義 - 韓系柔光風格

改進重點：
1. 更具體的色彩數值（HEX 色碼）
2. 明確的道具清單和擺放位置
3. 具體的光線設置（燈具類型、距離、強度）
4. 後期處理參數（對比度、飽和度、曲線）
5. 否定提示避免常見問題
"""

from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style_optimized = StyleDefinition(
    id="korean_soft_v2",
    name="韓系柔光 V2",
    name_en="Korean Soft V2",
    description="柔和粉彩色調，明亮無陰影打光，精選道具配置，適合服飾美妝飾品",
    icon="🌸",
    preview_color="#F8E8F0",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": (
                "Korean beauty aesthetic product photography. "
                "Lighting: Large ring light (18-inch) directly in front of product at 1-meter distance, "
                "plus two small LED panels on sides at 30° for subtle fill. "
                "Result: Bright, even illumination with minimal shadows. "
                "Color palette: Soft pastels - baby pink (#FFD1DC), lavender (#E6E6FA), mint (#F5FFFA), cream (#FFFDD0). "
                "Camera: 85mm lens at f/2.8 for gentle background blur. "
            ),
            "suffix": (
                " Props (select 1-2): Dried baby's breath in small ceramic vase (white or blush pink), "
                "thin satin ribbon (2cm width, champagne color) loosely draped, "
                "small pearl dish (3-inch diameter) partially visible, clear glass with sparkling water. "
                "Post-processing: Lifted blacks (+20), reduced contrast (-15), "
                "subtle pink tint in highlights (+10 magenta), soft highlight roll-off. "
                "NEGATIVE: No harsh shadows, no dark backgrounds, no warm orange tones, "
                "no cluttered composition, no large props overshadowing product, no artificial color casts."
            ),
        },
        InjectionLevel.FULL: {
            "prefix": (
                "Korean K-beauty editorial lifestyle photography. "
                "Scene setup: Bright, airy pastel-toned space. "
                "Surface: Light marble (white with gray veining) or matte white tabletop. "
                "Background: Soft gradient from white to blush pink (#FFE4E1) or soft lavender (#E6E6FA). "
                "Lighting: 48-inch octagonal softbox directly overhead + two large diffused panels on sides. "
                "Ring light as fill to eliminate all shadows. Color temperature: 5500K pure white. "
                "Camera: Sony A7 IV with 50mm f/1.2 at f/2.0, ISO 100, 1/160s. "
                "Angle: 30° above horizontal, slight tilt for dynamic composition. "
            ),
            "suffix": (
                " Props arrangement (choose 2-3): "
                "- Dried flower arrangement: baby's breath, cotton stems, pampas grass in small ceramic vase (white, 4-inch height). "
                "- Satin ribbon: 2cm width, champagne or blush color, loosely draped in S-curve. "
                "- Pearl accents: small dish (3-inch) with 3-5 scattered pearls, or pearl hair clip nearby. "
                "- Pastel ceramic tray: hexagonal shape in mint or pink, partially visible. "
                "- Clear glass: sparkling water with lemon slice, catching light. "
                "- Macaron or small pastel dessert on ceramic plate (optional). "
                "Composition: Asymmetrical balance, product as hero at left-third intersection, "
                "props supporting but not competing. Rule of thirds applied. "
                "Background: Soft gaussian blur (bokeh circles visible), dreamy ethereal quality. "
                "Post-processing color grade: Lifted blacks (+25), reduced contrast (-20), "
                "highlights tinted pink (+15 magenta), shadows slightly blue/cyan tinted (+10), "
                "overall reduced saturation (-10 except skin tones), clarity reduced (-10) for soft glow. "
                "Mood: Youthful elegance, curated lifestyle, scroll-stopping Instagram aesthetic, "
                "innocent romance, aspirational femininity. "
                "NEGATIVE: No harsh directional lighting, no deep shadows, no dark wood, "
                "no metallic industrial props, no bold/contrasting colors, no text overlays, "
                "no messy clutter, no oversized props, no yellow/orange color cast, "
                "no realistic/aged textures, no dramatic lighting, no busy patterns."
            ),
        },
    },
)

# 韓系風格 V2 特點總結：
# 1. 具體色碼讓 AI 更準確生成指定色調
# 2. 道具尺寸和擺放位置明確
# 3. 專業燈光設置確保無陰影效果
# 4. 後期參數可指導 AI 生成特定調性
# 5. 否定提示避免常見 AI 錯誤（過深陰影、錯誤色溫等）

# 如果要註冊到系統，取消下面的註解：
# StyleRegistry.register_style(_style_optimized)
