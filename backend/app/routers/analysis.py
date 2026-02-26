"""
Product analysis router: AI-powered product attribute extraction.

Endpoints:
- POST /api/analysis/analyze-product — Analyze product image attributes
- GET /api/analysis/materials — Material sample library
- GET /api/analysis/model-presets — Virtual model presets
"""

from __future__ import annotations

import json
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import get_current_user
from app.database import get_db
from app.models.db_models import ProductAnalysis, User
from app.models.schemas import (
    AnalyzeProductRequest,
    AnalyzeProductResponse,
    MaterialListResponse,
    MaterialSample,
    ModelPreset,
    ModelPresetListResponse,
)

router = APIRouter(prefix="/api/analysis", tags=["analysis"])


# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

MOCK_MATERIALS: list[dict] = [
    {"name": "義大利植鞣牛皮", "thumbnail_url": "/api/uploads/placeholder_material_leather.png", "description": "經典托斯卡尼植物鞣製牛皮，觸感溫潤如奶油，隨時間使用產生獨特蜜色光澤與包漿"},
    {"name": "桑蠶真絲", "thumbnail_url": "/api/uploads/placeholder_material_silk.png", "description": "100% 桑蠶絲，輕若無物如水般垂墜，光線在表面形成流動的絲綢光澤"},
    {"name": "304 不鏽鋼", "thumbnail_url": "/api/uploads/placeholder_material_steel.png", "description": "食品級 304 不鏽鋼，鏡面拋光處理，耐腐蝕易清潔，完美金屬光澤"},
    {"name": "GOTS 有機棉", "thumbnail_url": "/api/uploads/placeholder_material_cotton.png", "description": "GOTS 認證有機棉，親膚透氣，柔軟蓬鬆的自然纖維質感"},
    {"name": "北美黑胡桃木", "thumbnail_url": "/api/uploads/placeholder_material_walnut.png", "description": "北美黑胡桃木，深巧克力色紋理如流水般蜿蜒，絲緞般的細膩觸感"},
    {"name": "高硼矽玻璃", "thumbnail_url": "/api/uploads/placeholder_material_glass.png", "description": "高硼矽耐熱玻璃，晶瑩剔透如水晶，光線透射產生細膩焦散光影"},
    {"name": "ECONYL 再生尼龍", "thumbnail_url": "/api/uploads/placeholder_material_nylon.png", "description": "ECONYL 再生尼龍，軍規強度防水耐磨，水珠在緊密格紋表面滾落"},
    {"name": "天然竹纖維", "thumbnail_url": "/api/uploads/placeholder_material_bamboo.png", "description": "天然竹纖維，抑菌透氣柔軟親膚，可見輕薄織紋結構"},
    {"name": "法國亞麻", "thumbnail_url": "/api/uploads/placeholder_material_linen.png", "description": "法國諾曼底亞麻，特有的粗紡節感紋理，自然褶皺增添有機質感"},
    {"name": "手工柴燒陶瓷", "thumbnail_url": "/api/uploads/placeholder_material_ceramic.png", "description": "高溫柴燒窯變釉面，每件色澤與開片紋路獨一無二，充滿手作溫度"},
    {"name": "環氧樹脂", "thumbnail_url": "/api/uploads/placeholder_material_resin.png", "description": "透明環氧樹脂，可封裝花朵與色料，如寶石般晶瑩的藝術效果"},
    {"name": "日本和紙", "thumbnail_url": "/api/uploads/placeholder_material_washi.png", "description": "傳統手抄和紙工藝，纖維細密可見透光性，觸感柔韌溫暖"},
]

MOCK_MODEL_PRESETS: list[dict] = [
    {"ethnicity": "東亞", "body_type": "纖細", "style": "清新甜美", "thumbnail_url": "/api/uploads/placeholder_model_sweet.png", "description": "韓系清新甜美風格，鄰家女孩氣質，自然妝容微捲長髮，20-25 歲"},
    {"ethnicity": "東亞", "body_type": "標準", "style": "知性優雅", "thumbnail_url": "/api/uploads/placeholder_model_elegant.png", "description": "日系知性優雅風格，低馬尾或齊肩短髮，精緻淡妝成熟質感，28-35 歲"},
    {"ethnicity": "東亞", "body_type": "健美", "style": "陽光運動", "thumbnail_url": "/api/uploads/placeholder_model_athletic.png", "description": "陽光運動型男，短髮乾淨俐落，健康小麥膚色自信笑容，25-32 歲"},
    {"ethnicity": "東亞", "body_type": "纖細", "style": "文藝書生", "thumbnail_url": "/api/uploads/placeholder_model_literary.png", "description": "文藝書生氣質，中分微長髮白皙膚色金絲眼鏡，22-30 歲"},
    {"ethnicity": "歐美", "body_type": "高挑", "style": "時尚超模", "thumbnail_url": "/api/uploads/placeholder_model_highfashion.png", "description": "歐美高級時裝風格，高顴骨輪廓分明金棕長髮，高冷氣場，22-30 歲"},
    {"ethnicity": "歐美", "body_type": "標準", "style": "都市雅痞", "thumbnail_url": "/api/uploads/placeholder_model_urbanman.png", "description": "都市雅痞風格，輪廓清晰深色短髮整齊梳理，輕度鬍鬚魅力笑容，30-38 歲"},
    {"ethnicity": "南亞", "body_type": "標準", "style": "異域風情", "thumbnail_url": "/api/uploads/placeholder_model_exotic.png", "description": "異域風情美感，深色大波浪長髮蜜色皮膚明亮大眼，充滿活力，23-30 歲"},
    {"ethnicity": "東亞", "body_type": "標準", "style": "混血時尚", "thumbnail_url": "/api/uploads/placeholder_model_mixed.png", "description": "混血模特氣質，融合東西方特徵五官精緻立體短髮幹練，22-28 歲"},
]


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/analyze-product", response_model=AnalyzeProductResponse)
async def analyze_product(
    request: AnalyzeProductRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    """Analyze a product image to extract attributes.

    TODO: Replace mock with Gemini AI analysis.
    """
    from app.config import UPLOAD_DIR

    # Verify image exists
    matching = list(UPLOAD_DIR.glob(f"{request.image_id}.*"))
    if not matching:
        raise HTTPException(status_code=404, detail="圖片未找到，請先上傳圖片")

    # Mock analysis result
    mock_result = AnalyzeProductResponse(
        product_name="復古真皮手提包",
        category="女包 > 手提包 > 真皮手提包",
        audience="女性",
        primary_color="#8B4513",
        secondary_color="#D2B48C",
        material="頭層牛皮",
        material_confidence=0.92,
        features=["防潑水", "大容量", "可調節肩帶", "內置隔層"],
        local_features=["復古金屬扣", "車線裝飾", "品牌壓印 Logo"],
        texture_feel="溫潤皮革質感",
        contour_type="梯形結構",
    )

    # Persist to DB
    analysis = ProductAnalysis(
        id=uuid.uuid4().hex[:12],
        user_id=user.id,
        image_id=request.image_id,
        product_name=mock_result.product_name,
        category=mock_result.category,
        audience=mock_result.audience,
        primary_color=mock_result.primary_color,
        secondary_color=mock_result.secondary_color,
        material=mock_result.material,
        material_confidence=mock_result.material_confidence,
        features=json.dumps(mock_result.features, ensure_ascii=False),
        local_features=json.dumps(mock_result.local_features, ensure_ascii=False),
        texture_feel=mock_result.texture_feel,
        contour_type=mock_result.contour_type,
    )
    db.add(analysis)
    await db.commit()

    return mock_result


@router.get("/materials", response_model=MaterialListResponse)
async def get_materials(
    user: User = Depends(get_current_user),
):
    """Get material sample library."""
    materials = [MaterialSample(**m) for m in MOCK_MATERIALS]
    return MaterialListResponse(materials=materials)


@router.get("/model-presets", response_model=ModelPresetListResponse)
async def get_model_presets(
    user: User = Depends(get_current_user),
):
    """Get virtual model presets."""
    presets = [ModelPreset(**p) for p in MOCK_MODEL_PRESETS]
    return ModelPresetListResponse(presets=presets)
