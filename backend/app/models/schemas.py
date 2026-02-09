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
