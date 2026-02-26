"""
Festival themes router: seasonal and holiday theme presets.

Endpoints:
- GET /api/themes/festivals — Festival theme list
"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import get_current_user
from app.models.db_models import User
from app.models.schemas import FestivalTheme, FestivalThemeListResponse

router = APIRouter(prefix="/api/themes", tags=["themes"])


# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

MOCK_FESTIVAL_THEMES: list[dict] = [
    {
        "id": "theme_double11",
        "name": "雙 11 購物節",
        "border_style": "solid 3px #FF2D55",
        "bg_color": "#FFF0F0",
        "accent_color": "#FF2D55",
        "preview_url": "/api/uploads/placeholder_theme_double11.png",
        "description": "淘寶天貓雙 11 風格，紅色主調搭配金色促銷標籤，限時搶購氛圍",
        "prompt_modifier": "festive shopping festival atmosphere with red and gold promotional elements, urgency and excitement, sale countdown energy",
    },
    {
        "id": "theme_mid_autumn",
        "name": "中秋節",
        "border_style": "solid 2px #D4A574",
        "bg_color": "#FFF8F0",
        "accent_color": "#D4A574",
        "preview_url": "/api/uploads/placeholder_theme_midautumn.png",
        "description": "中秋團圓意境，暖金色月光搭配桂花元素，溫暖典雅的傳統節日風格",
        "prompt_modifier": "Mid-Autumn Festival warm golden moonlight, osmanthus flowers and mooncake elements, traditional elegance with family warmth",
    },
    {
        "id": "theme_spring_new",
        "name": "春季新品",
        "border_style": "solid 2px #4CAF50",
        "bg_color": "#F0FFF0",
        "accent_color": "#4CAF50",
        "preview_url": "/api/uploads/placeholder_theme_spring.png",
        "description": "春日新品上市，清新嫩綠搭配櫻花粉，充滿生機與新鮮感",
        "prompt_modifier": "spring season fresh green with cherry blossom pink accents, new beginnings energy, bright and vibrant natural light",
    },
    {
        "id": "theme_christmas",
        "name": "聖誕節",
        "border_style": "solid 3px #C41E3A",
        "bg_color": "#FDF5F5",
        "accent_color": "#C41E3A",
        "preview_url": "/api/uploads/placeholder_theme_christmas.png",
        "description": "西方聖誕節慶，紅綠經典配色搭配金色裝飾，雪花與松枝元素",
        "prompt_modifier": "Christmas holiday atmosphere with red-green-gold color scheme, snowflakes and pine branches, warm fairy lights bokeh, festive and joyful",
    },
    {
        "id": "theme_lunar_new_year",
        "name": "農曆新年",
        "border_style": "solid 3px #E60000",
        "bg_color": "#FFF5F5",
        "accent_color": "#E60000",
        "preview_url": "/api/uploads/placeholder_theme_cny.png",
        "description": "農曆新年喜氣洋洋，中國紅搭配金色祥雲紋樣，春聯與燈籠元素",
        "prompt_modifier": "Chinese New Year festive red and gold, auspicious cloud patterns, spring couplets and red lanterns, prosperous and joyful celebration",
    },
    {
        "id": "theme_valentines",
        "name": "情人節",
        "border_style": "solid 2px #FF6B9D",
        "bg_color": "#FFF5F9",
        "accent_color": "#FF6B9D",
        "preview_url": "/api/uploads/placeholder_theme_valentines.png",
        "description": "浪漫情人節，粉紅玫瑰搭配心形元素，柔和夢幻的愛情氛圍",
        "prompt_modifier": "Valentine's Day romantic pink roses and heart elements, soft dreamy lighting, love and tenderness atmosphere with subtle glitter",
    },
    {
        "id": "theme_summer_sale",
        "name": "夏日特賣",
        "border_style": "solid 2px #00BCD4",
        "bg_color": "#F0FFFE",
        "accent_color": "#00BCD4",
        "preview_url": "/api/uploads/placeholder_theme_summer.png",
        "description": "盛夏清涼特賣，海洋藍搭配冰淇淋色調，清爽活力的夏日感",
        "prompt_modifier": "summer sale cool ocean blue and ice cream pastels, tropical beach vibes, refreshing and energetic with bright sunlight",
    },
]


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("/festivals", response_model=FestivalThemeListResponse)
async def get_festival_themes(
    user: User = Depends(get_current_user),
):
    """Get festival theme list."""
    themes = [FestivalTheme(**t) for t in MOCK_FESTIVAL_THEMES]
    return FestivalThemeListResponse(themes=themes)
