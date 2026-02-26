"""
Scenes & style router: scene library, props, and style reference uploads.

Endpoints:
- GET /api/scenes — Scene library (indoor/outdoor)
- GET /api/scenes/props — Prop list
- POST /api/scenes/style-reference — Upload style reference image
"""

from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.config import ALLOWED_EXTENSIONS, MAX_UPLOAD_SIZE, UPLOAD_DIR
from app.database import get_db
from app.models.db_models import StyleReference, User
from app.models.schemas import (
    PropItem,
    PropListResponse,
    SceneItem,
    SceneListResponse,
    StyleReferenceResponse,
)

router = APIRouter(prefix="/api/scenes", tags=["scenes"])


# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

MOCK_SCENES: list[dict] = [
    # ===== 室內場景 =====
    {"id": "scene_studio_white", "name": "純白攝影棚", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_studio.png", "description": "專業白底攝影棚，雙側 45° 條形柔光箱均勻照明，適合電商主圖標準拍攝"},
    {"id": "scene_jp_minimal", "name": "日系極簡", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_jp.png", "description": "清新日式簡約空間，檜木表面搭配留白美學，自然光透過障子紙柔和漫射"},
    {"id": "scene_living_room", "name": "北歐風客廳", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_living.png", "description": "明亮北歐客廳，白橡木傢俱搭配亞麻布藝，大面積北向窗戶提供均勻自然光"},
    {"id": "scene_kr_cream", "name": "韓系奶油風", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_kr.png", "description": "柔和奶油色調韓式空間，暖黃牆面搭配米白桌布，微過曝夢幻氛圍感"},
    {"id": "scene_kitchen_modern", "name": "現代廚房", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_kitchen.png", "description": "簡約現代廚房，卡拉卡塔大理石檯面搭配不鏽鋼器具，適合廚具與食品類"},
    {"id": "scene_bedroom_warm", "name": "溫馨臥室", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_bedroom.png", "description": "暖色調臥室，法國亞麻寢具搭配柔和床頭燈光，適合居家與織物類"},
    {"id": "scene_office_minimal", "name": "極簡辦公室", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_office.png", "description": "乾淨極簡辦公場景，白色桌面搭配綠色盆栽，適合 3C 數碼與文具類"},
    {"id": "scene_luxury_marble", "name": "奢華大理石", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_luxury.png", "description": "卡拉卡塔大理石台面搭配金色點綴，頂部柔光箱照明，適合珠寶與奢品"},
    {"id": "scene_loft", "name": "現代 LOFT", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_loft.png", "description": "工業風格閣樓空間，裸露紅磚牆與水泥地面，愛迪生燈泡暖光點綴"},
    {"id": "scene_cafe_indoor", "name": "文青咖啡廳", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_cafe.png", "description": "木質調咖啡廳，自然光灑落搭配暖色吊燈，拿鐵拉花作為生活道具"},
    {"id": "scene_detail_macro", "name": "細節微距", "category": "indoor", "thumbnail_url": "/api/uploads/placeholder_scene_macro.png", "description": "100mm 微距鏡頭近攝材質紋理與工藝細節，低角度側光突出表面肌理"},
    # ===== 室外場景 =====
    {"id": "scene_street", "name": "都市街拍", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_street.png", "description": "時尚都市街景，現代建築背景，清晨斜射光形成戲劇性明暗對比"},
    {"id": "scene_beach", "name": "海濱度假", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_beach.png", "description": "白沙灘與碧海，棕櫚樹斑駁陰影，適合泳裝、太陽鏡與夏季商品"},
    {"id": "scene_garden", "name": "花園庭院", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_garden.png", "description": "英式花園繡球花與藤蔓，柔和漫射光斑穿過樹冠，浪漫唯美的花園場景"},
    {"id": "scene_mountain", "name": "山野徒步", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_mountain.png", "description": "蒼翠山間步道，清晨薄霧與遼闊山谷，適合戶外裝備與運動服飾"},
    {"id": "scene_rooftop", "name": "天台夕陽", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_rooftop.png", "description": "高樓天台黃金時刻，城市天際線柔化背景，逆光暈染產生光環效果"},
    {"id": "scene_camping", "name": "露營野趣", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_camping.png", "description": "帆布鐘形帳篷與松林，營火暖光搭配琺瑯杯，戶外生活美學"},
    {"id": "scene_neon_night", "name": "霓虹夜景", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_neon.png", "description": "賽博朋克霓虹都市夜景，粉紫青光影映射在濕潤柏油路面上"},
    {"id": "scene_park", "name": "城市公園", "category": "outdoor", "thumbnail_url": "/api/uploads/placeholder_scene_park.png", "description": "綠意盎然城市公園步道，梧桐樹蔭下斑駁光影，適合運動休閒商品"},
]

MOCK_PROPS: list[dict] = [
    {"id": "prop_flower", "name": "鮮花束", "category": "裝飾", "thumbnail_url": "/api/uploads/placeholder_prop_flower.png", "description": "新鮮花束（玫瑰、芍藥或尤加利），增添浪漫與生活感"},
    {"id": "prop_book", "name": "精裝書籍", "category": "文創", "thumbnail_url": "/api/uploads/placeholder_prop_book.png", "description": "精裝封面書籍，增加知性文藝氛圍"},
    {"id": "prop_coffee", "name": "拿鐵咖啡", "category": "飲品", "thumbnail_url": "/api/uploads/placeholder_prop_coffee.png", "description": "陶瓷杯裝拿鐵拉花，增加咖啡廳生活感"},
    {"id": "prop_candle", "name": "香氛蠟燭", "category": "裝飾", "thumbnail_url": "/api/uploads/placeholder_prop_candle.png", "description": "琥珀色玻璃杯裝香氛蠟燭，增添溫馨氣氛"},
    {"id": "prop_plant", "name": "綠色盆栽", "category": "植物", "thumbnail_url": "/api/uploads/placeholder_prop_plant.png", "description": "小型多肉或尤加利盆栽，注入自然清新感"},
    {"id": "prop_fabric", "name": "亞麻布巾", "category": "布料", "thumbnail_url": "/api/uploads/placeholder_prop_fabric.png", "description": "法國亞麻布巾，自然褶皺紋理增添層次"},
    {"id": "prop_wood_tray", "name": "木質托盤", "category": "器皿", "thumbnail_url": "/api/uploads/placeholder_prop_tray.png", "description": "胡桃木圓形托盤，溫潤木紋搭配任何風格"},
    {"id": "prop_marble", "name": "大理石板", "category": "器皿", "thumbnail_url": "/api/uploads/placeholder_prop_marble.png", "description": "白色大理石切板，灰金紋理增添奢華感"},
    {"id": "prop_sunglasses", "name": "太陽眼鏡", "category": "配件", "thumbnail_url": "/api/uploads/placeholder_prop_sunglasses.png", "description": "復古飛行員太陽鏡，增添時尚生活感"},
    {"id": "prop_hat", "name": "草編帽", "category": "配件", "thumbnail_url": "/api/uploads/placeholder_prop_hat.png", "description": "天然草編寬沿帽，增添度假氛圍"},
    {"id": "prop_fruit", "name": "新鮮水果", "category": "食物", "thumbnail_url": "/api/uploads/placeholder_prop_fruit.png", "description": "新鮮柑橘或漿果，增添色彩與新鮮感"},
    {"id": "prop_magazine", "name": "時尚雜誌", "category": "文創", "thumbnail_url": "/api/uploads/placeholder_prop_magazine.png", "description": "時尚或設計雜誌，增加品味與格調"},
    {"id": "prop_jewelry_box", "name": "首飾盒", "category": "裝飾", "thumbnail_url": "/api/uploads/placeholder_prop_jewelry.png", "description": "天鵝絨首飾收納盒，增添精緻奢華感"},
    {"id": "prop_silk_scarf", "name": "絲綢圍巾", "category": "布料", "thumbnail_url": "/api/uploads/placeholder_prop_silk.png", "description": "印花真絲圍巾，柔和流動增添時尚層次"},
]


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("", response_model=SceneListResponse)
async def get_scenes(
    user: User = Depends(get_current_user),
):
    """Get scene library (indoor/outdoor)."""
    scenes = [SceneItem(**s) for s in MOCK_SCENES]
    return SceneListResponse(scenes=scenes)


@router.get("/props", response_model=PropListResponse)
async def get_props(
    user: User = Depends(get_current_user),
):
    """Get prop list."""
    props = [PropItem(**p) for p in MOCK_PROPS]
    return PropListResponse(props=props)


@router.post("/style-reference", response_model=StyleReferenceResponse)
async def upload_style_reference(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Upload a style reference image for IP-Adapter.

    TODO: Replace mock style extraction with AI analysis.
    """
    # Validate file extension
    ext = Path(file.filename or "").suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"不支援的檔案格式 {ext}，支援：{ALLOWED_EXTENSIONS}",
        )

    # Read and validate size
    content = await file.read()
    if len(content) > MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"檔案過大，上限 {MAX_UPLOAD_SIZE // (1024*1024)}MB",
        )

    # Save file
    reference_id = uuid.uuid4().hex[:12]
    filename = f"styleref_{reference_id}{ext}"
    file_path = UPLOAD_DIR / filename
    file_path.write_bytes(content)

    # Mock extracted style info
    mock_style_info = {
        "dominant_style": "日系清新",
        "color_palette": ["#F5F0EB", "#D4C5B2", "#8B7355"],
        "lighting": "自然側光",
        "mood": "溫暖舒適",
        "composition": "中心對稱",
    }

    # Persist to DB
    import json
    ref = StyleReference(
        id=reference_id,
        user_id=user.id,
        filename=filename,
        file_path=str(file_path),
        extracted_style_info=json.dumps(mock_style_info, ensure_ascii=False),
    )
    db.add(ref)
    await db.commit()

    return StyleReferenceResponse(
        reference_id=reference_id,
        extracted_style_info=mock_style_info,
    )
