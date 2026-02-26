from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ProductType(str, Enum):
    BAGS = "bags"
    JEWELRY = "jewelry"
    CLOTHING = "clothing"
    SHOES = "shoes"
    ELECTRONICS = "electronics"
    BEAUTY = "beauty"
    HOME = "home"
    TOYS = "toys"
    SPORTS = "sports"
    FOOD = "food"
    STATIONERY = "stationery"
    PETS = "pets"
    AUTOMOTIVE = "automotive"
    PHONES = "phones"
    TRAVEL = "travel"
    FASHION_ACC = "fashion_acc"
    KITCHENWARE = "kitchenware"
    HEALTH = "health"
    HOBBIES = "hobbies"
    MOTORCYCLE = "motorcycle"


class UploadResponse(BaseModel):
    image_id: str
    filename: str
    url: str


class RemoveBgResponse(BaseModel):
    image_id: str
    original_url: str
    removed_bg_url: str


class SceneTemplateSchema(BaseModel):
    id: str
    name: str
    name_en: str
    product_type: str
    prompt: str
    description: str = ""
    aspect_ratio: str
    recommended_provider: str
    injection_level: str = "full"
    sub_category: str = "common"
    sub_category_name: str = "通用場景"


class StyleSchema(BaseModel):
    id: str
    name: str
    name_en: str
    description: str
    icon: str
    preview_color: str


class SubCategoryInfo(BaseModel):
    id: str
    name: str


class ProductTypeInfo(BaseModel):
    id: str
    name: str
    name_en: str
    icon: str
    template_count: int
    sub_categories: list[SubCategoryInfo] = []


class TemplateOverride(BaseModel):
    template_id: str
    custom_prompt: Optional[str] = None


class GenerateRequest(BaseModel):
    image_id: str
    product_type: ProductType
    remove_bg: bool = True
    style: Optional[str] = None  # Style ID (e.g., "western", "japanese", "korean", "chinese")
    templates: Optional[list[TemplateOverride]] = None
    selected_template_ids: Optional[list[str]] = None  # Only generate selected templates


class RegenerateRequest(BaseModel):
    template_id: str
    custom_prompt: Optional[str] = None


class CompositeRequest(BaseModel):
    layout: str = "grid3x3"  # "grid3x3", "detail_long", "hero_center"
    image_order: Optional[list[str]] = None  # template_id ordering
    cell_size: int = 800  # pixel size per cell
    gap: int = 8  # pixel gap between cells
    bg_color: str = "#ffffff"


class GenerateTaskResponse(BaseModel):
    task_id: str
    status: str
    total: int
    credits_charged: Optional[int] = None
    credits_remaining: Optional[int] = None


class ImageStatus(str, Enum):
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class GeneratedImage(BaseModel):
    template_id: str
    template_name: str
    status: ImageStatus
    url: Optional[str] = None
    error: Optional[str] = None


class GenerateResultResponse(BaseModel):
    task_id: str
    status: str
    progress: int
    total: int
    images: list[GeneratedImage]


class PlatformSpec(BaseModel):
    name: str
    width: int
    height: int


PLATFORM_SPECS = {
    "shopee": PlatformSpec(name="蝦皮 Shopee", width=800, height=800),
    "momo": PlatformSpec(name="MOMO", width=1000, height=1000),
    "instagram": PlatformSpec(name="IG 貼文", width=1080, height=1080),
    "ig_story": PlatformSpec(name="IG 限動", width=1080, height=1920),
    "facebook": PlatformSpec(name="FB 貼文", width=1200, height=630),
    "line": PlatformSpec(name="LINE 購物", width=800, height=800),
    "general": PlatformSpec(name="通用高畫質", width=1024, height=1024),
}


# --- Copywriting ---

class CopySceneInfo(BaseModel):
    name: str
    name_en: str
    description: str = ""


class CopywritingRequest(BaseModel):
    product_details: str
    product_type: str
    scenes: list[CopySceneInfo]


class CopyItem(BaseModel):
    scene_index: int
    title: str
    subtitle: str
    description: str
    hashtags: list[str] = []


class CopywritingResponse(BaseModel):
    copies: list[CopyItem]
    raw: Optional[str] = None  # Raw AI output for debugging


# ---------------------------------------------------------------------------
# V2: Product Analysis
# ---------------------------------------------------------------------------

class AnalyzeProductRequest(BaseModel):
    image_id: str


class AnalyzeProductResponse(BaseModel):
    product_name: str
    category: str
    audience: str
    primary_color: str
    secondary_color: str
    material: str
    material_confidence: float
    features: list[str]
    local_features: list[str]
    texture_feel: str
    contour_type: str


class MaterialSample(BaseModel):
    name: str
    thumbnail_url: str
    description: str


class MaterialListResponse(BaseModel):
    materials: list[MaterialSample]


class ModelPreset(BaseModel):
    ethnicity: str
    body_type: str
    style: str
    thumbnail_url: str


class ModelPresetListResponse(BaseModel):
    presets: list[ModelPreset]


# ---------------------------------------------------------------------------
# V2: Scenes & Style
# ---------------------------------------------------------------------------

class SceneItem(BaseModel):
    id: str
    name: str
    category: str  # "indoor" | "outdoor"
    thumbnail_url: str
    description: str


class SceneListResponse(BaseModel):
    scenes: list[SceneItem]


class PropItem(BaseModel):
    id: str
    name: str
    category: str
    thumbnail_url: str


class PropListResponse(BaseModel):
    props: list[PropItem]


class StyleReferenceResponse(BaseModel):
    reference_id: str
    extracted_style_info: dict


# ---------------------------------------------------------------------------
# V2: Storyboard
# ---------------------------------------------------------------------------

class StoryboardProductAttributes(BaseModel):
    product_name: Optional[str] = None
    category: Optional[str] = None
    audience: Optional[str] = None
    primary_color: Optional[str] = None
    material: Optional[str] = None
    features: Optional[list[str]] = None


class StoryboardSceneConfig(BaseModel):
    scene_id: Optional[str] = None
    props: Optional[list[str]] = None
    style_reference_id: Optional[str] = None


class GeneratePreviewRequest(BaseModel):
    image_id: str
    product_attributes: Optional[StoryboardProductAttributes] = None
    scene_config: Optional[StoryboardSceneConfig] = None
    atmosphere_lock: Optional[str] = None


class PreviewImage(BaseModel):
    position: int
    image_url: str
    image_type: str  # e.g., "主圖", "白底圖", "情境圖", "模特圖", etc.


class GeneratePreviewResponse(BaseModel):
    task_id: str
    previews: list[PreviewImage]


class GridCellConfig(BaseModel):
    position: int
    image_type: str
    selected: bool = True


class ConfirmStoryboardRequest(BaseModel):
    task_id: str
    grid_config: list[GridCellConfig]


class ConfirmStoryboardResponse(BaseModel):
    task_id: str
    status: str
    message: str


class SwapPositionRequest(BaseModel):
    position_a: int
    position_b: int


class SwapPositionResponse(BaseModel):
    grid_config: list[GridCellConfig]


class ChangeTypeRequest(BaseModel):
    position: int
    new_type: str


class ChangeTypeResponse(BaseModel):
    position: int
    new_type: str
    preview_url: str


# ---------------------------------------------------------------------------
# V2: Optimization
# ---------------------------------------------------------------------------

class RegenerateOptRequest(BaseModel):
    task_id: str
    image_id: str
    mode: str = "original_seed"  # "original_seed" | "custom"
    custom_params: Optional[dict] = None


class RegenerateOptResponse(BaseModel):
    new_image_url: str


class InpaintRequest(BaseModel):
    task_id: str
    image_id: str
    mask_data: str  # Base64 encoded mask


class InpaintResponse(BaseModel):
    repaired_image_url: str


class GenerateAdditionalRequest(BaseModel):
    task_id: str
    image_type: str
    count: int = 1
    options: Optional[dict] = None


class GenerateAdditionalResponse(BaseModel):
    images: list[str]


class UpscaleRequest(BaseModel):
    image_id: str


class UpscaleResponse(BaseModel):
    upscaled_image_url: str


class OutpaintRequest(BaseModel):
    image_id: str
    target_ratio: str = "9:16"


class OutpaintResponse(BaseModel):
    outpainted_image_url: str


# ---------------------------------------------------------------------------
# V2: Detail Layout
# ---------------------------------------------------------------------------

class GenerateCopyRequest(BaseModel):
    product_name: str
    features: list[str]
    target_market: str = "tw"


class MarketingCopy(BaseModel):
    headline: str
    subtitle: str
    selling_points: list[str]
    cta: str


class GenerateCopyResponse(BaseModel):
    marketing_copy: MarketingCopy


class PlatformExportConfig(BaseModel):
    platform: str
    width: int
    height: int


class ExportDetailRequest(BaseModel):
    task_id: str
    platforms: list[PlatformExportConfig]
    include_4k_upscale: bool = False


class ExportDetailResponse(BaseModel):
    download_url: str


# ---------------------------------------------------------------------------
# V2: Atmosphere
# ---------------------------------------------------------------------------

class AtmospherePreset(BaseModel):
    id: str
    name: str
    color_temperature: int
    brightness: float
    thumbnail_url: str


class AtmosphereListResponse(BaseModel):
    presets: list[AtmospherePreset]


# ---------------------------------------------------------------------------
# V2: Festival Themes
# ---------------------------------------------------------------------------

class FestivalTheme(BaseModel):
    id: str
    name: str
    border_style: str
    bg_color: str
    accent_color: str
    preview_url: str


class FestivalThemeListResponse(BaseModel):
    themes: list[FestivalTheme]
