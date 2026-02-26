"""
Global atmosphere router: atmosphere presets for image generation.

Endpoints:
- GET /api/atmosphere/presets — Atmosphere preset list
"""

from __future__ import annotations

from fastapi import APIRouter, Depends

from app.auth import get_current_user
from app.models.db_models import User
from app.models.schemas import AtmosphereListResponse, AtmospherePreset

router = APIRouter(prefix="/api/atmosphere", tags=["atmosphere"])


# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

MOCK_ATMOSPHERE_PRESETS: list[dict] = [
    {
        "id": "atm_warm_afternoon",
        "name": "暖陽午後",
        "color_temperature": 4500,
        "brightness": 0.85,
        "thumbnail_url": "/api/uploads/placeholder_atm_warm.png",
        "description": "如同秋日午後三點的溫暖陽光，從側面灑入的金色光線帶來溫暖舒適的氛圍",
        "prompt_modifier": "warm afternoon sunlight at 4500K color temperature, soft golden side lighting, cozy and inviting atmosphere",
    },
    {
        "id": "atm_cold_industrial",
        "name": "清冷工業風",
        "color_temperature": 6500,
        "brightness": 0.70,
        "thumbnail_url": "/api/uploads/placeholder_atm_cold.png",
        "description": "冷色調工業風照明，高色溫帶來現代感與專業感，適合科技與金屬質感商品",
        "prompt_modifier": "cool industrial lighting at 6500K, slightly underexposed for moody depth, modern and professional atmosphere",
    },
    {
        "id": "atm_natural_soft",
        "name": "自然柔光",
        "color_temperature": 5000,
        "brightness": 0.80,
        "thumbnail_url": "/api/uploads/placeholder_atm_natural.png",
        "description": "模擬窗邊自然光的柔和照明，中性色溫還原真實色彩，百搭任何商品類型",
        "prompt_modifier": "natural window light at 5000K neutral white, soft diffused shadows, true-to-life color rendering",
    },
    {
        "id": "atm_golden_hour",
        "name": "黃金時刻",
        "color_temperature": 3500,
        "brightness": 0.75,
        "thumbnail_url": "/api/uploads/placeholder_atm_golden.png",
        "description": "日落前一小時的魔幻金色光線，低色溫暖光為畫面增添浪漫與戲劇性",
        "prompt_modifier": "golden hour magic light at 3500K, warm amber backlighting with lens flare, romantic and dramatic mood",
    },
    {
        "id": "atm_studio_bright",
        "name": "攝影棚亮光",
        "color_temperature": 5500,
        "brightness": 1.0,
        "thumbnail_url": "/api/uploads/placeholder_atm_studio.png",
        "description": "專業攝影棚的標準照明設定，雙柔光箱均勻打光，最適合產品主圖拍攝",
        "prompt_modifier": "professional studio lighting at 5500K daylight, dual softbox even illumination, no harsh shadows, commercial product photography",
    },
    {
        "id": "atm_moody_dark",
        "name": "暗調氛圍",
        "color_temperature": 4000,
        "brightness": 0.45,
        "thumbnail_url": "/api/uploads/placeholder_atm_moody.png",
        "description": "低調暗黑氛圍，大面積暗部搭配精準重點照明，神秘而高級的視覺效果",
        "prompt_modifier": "moody dark key lighting at 4000K, deep shadows with precise spotlight on product, mysterious and luxurious atmosphere",
    },
    {
        "id": "atm_pastel_dream",
        "name": "粉彩夢境",
        "color_temperature": 5200,
        "brightness": 0.90,
        "thumbnail_url": "/api/uploads/placeholder_atm_pastel.png",
        "description": "夢幻粉彩色調，高亮度低對比的棉花糖般視覺效果，適合少女系與美妝商品",
        "prompt_modifier": "dreamy pastel lighting at 5200K, high-key overexposed softness, cotton-candy pink and lavender tones, ethereal and feminine",
    },
    {
        "id": "atm_neon_night",
        "name": "霓虹夜景",
        "color_temperature": 7000,
        "brightness": 0.55,
        "thumbnail_url": "/api/uploads/placeholder_atm_neon.png",
        "description": "賽博朋克風格的混合色溫霓虹照明，粉紫與青色交織的未來感夜間氛圍",
        "prompt_modifier": "neon night lighting with mixed pink-purple and cyan tones, high contrast, wet reflective surfaces, cyberpunk futuristic atmosphere",
    },
    {
        "id": "atm_sunrise_fresh",
        "name": "清晨日出",
        "color_temperature": 5800,
        "brightness": 0.75,
        "thumbnail_url": "/api/uploads/placeholder_atm_sunrise.png",
        "description": "清晨第一道晨光，清新通透帶有微微粉色，充滿希望與活力的新一天",
        "prompt_modifier": "early morning sunrise light at 5800K, fresh and crisp with slight pink undertones, optimistic and energetic mood",
    },
    {
        "id": "atm_candlelight",
        "name": "燭光晚餐",
        "color_temperature": 2700,
        "brightness": 0.40,
        "thumbnail_url": "/api/uploads/placeholder_atm_candle.png",
        "description": "溫馨燭光照明，極低色溫帶來私密浪漫的用餐氛圍，適合餐具與食品類",
        "prompt_modifier": "intimate candlelight at 2700K, very warm amber glow, soft flickering light creating romantic intimacy",
    },
]


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("/presets", response_model=AtmosphereListResponse)
async def get_atmosphere_presets(
    user: User = Depends(get_current_user),
):
    """Get atmosphere preset list."""
    presets = [AtmospherePreset(**p) for p in MOCK_ATMOSPHERE_PRESETS]
    return AtmosphereListResponse(presets=presets)
