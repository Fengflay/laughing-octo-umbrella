from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SceneTemplate:
    id: str
    name: str
    name_en: str
    product_type: str
    prompt: str
    description: str = ""
    aspect_ratio: str = "1:1"
    negative_prompt: str = ""
    recommended_provider: str = "gemini"
    injection_level: str = "full"  # "none", "light", or "full"
    sub_category: str = "common"
    sub_category_name: str = "通用場景"


class TemplateRegistry:
    _templates: dict[str, list[SceneTemplate]] = {}

    @classmethod
    def register(cls, product_type: str, templates: list[SceneTemplate]) -> None:
        cls._templates[product_type] = templates

    @classmethod
    def get_templates(cls, product_type: str) -> list[SceneTemplate]:
        return cls._templates.get(product_type, [])

    @classmethod
    def get_template_by_id(cls, product_type: str, template_id: str) -> SceneTemplate | None:
        for t in cls._templates.get(product_type, []):
            if t.id == template_id:
                return t
        return None

    @classmethod
    def get_sub_categories(cls, product_type: str) -> list[dict]:
        """Get all sub-categories for a product type (deduplicated, insertion order)."""
        templates = cls._templates.get(product_type, [])
        seen: dict[str, str] = {}
        for t in templates:
            if t.sub_category not in seen:
                seen[t.sub_category] = t.sub_category_name
        return [{"id": k, "name": v} for k, v in seen.items()]

    @classmethod
    def get_product_types(cls) -> list[dict]:
        product_type_info = {
            "bags": {"name": "包包/背包", "name_en": "Bags & Backpacks", "icon": "👜"},
            "jewelry": {"name": "首飾/項鏈", "name_en": "Jewelry & Necklaces", "icon": "💎"},
            "clothing": {"name": "服裝", "name_en": "Clothing & Apparel", "icon": "👔"},
            "shoes": {"name": "鞋類", "name_en": "Shoes & Footwear", "icon": "👟"},
            "electronics": {"name": "3C數碼", "name_en": "Electronics & Gadgets", "icon": "📱"},
            "beauty": {"name": "美妝護膚", "name_en": "Beauty & Skincare", "icon": "💄"},
            "home": {"name": "家居用品", "name_en": "Home & Living", "icon": "🏠"},
            "toys": {"name": "母嬰玩具", "name_en": "Baby & Toys", "icon": "🧸"},
            "sports": {"name": "運動戶外", "name_en": "Sports & Outdoor", "icon": "⚽"},
            "food": {"name": "食品飲料", "name_en": "Food & Beverage", "icon": "🍵"},
            "stationery": {"name": "文具辦公", "name_en": "Stationery & Office", "icon": "✏️"},
            "pets": {"name": "寵物用品", "name_en": "Pet Supplies", "icon": "🐾"},
            "automotive": {"name": "汽車配件", "name_en": "Automotive Accessories", "icon": "🚗"},
            "phones": {"name": "手機配件", "name_en": "Phone & Tablet Accessories", "icon": "📲"},
            "travel": {"name": "旅行箱包", "name_en": "Travel & Luggage", "icon": "✈️"},
            "fashion_acc": {"name": "時尚配飾", "name_en": "Fashion Accessories", "icon": "🎩"},
            "kitchenware": {"name": "廚具餐飲", "name_en": "Kitchenware & Dining", "icon": "🍳"},
            "health": {"name": "保健護理", "name_en": "Health & Personal Care", "icon": "❤️"},
            "hobbies": {"name": "興趣文娛", "name_en": "Hobbies & Entertainment", "icon": "🎯"},
            "motorcycle": {"name": "摩托車配件", "name_en": "Motorcycle Accessories", "icon": "🏍️"},
        }
        result = []
        for pt, templates in cls._templates.items():
            info = product_type_info.get(pt, {"name": pt, "name_en": pt, "icon": "📦"})
            result.append({
                "id": pt,
                "name": info["name"],
                "name_en": info["name_en"],
                "icon": info["icon"],
                "template_count": len(templates),
                "sub_categories": cls.get_sub_categories(pt),
            })
        return result
