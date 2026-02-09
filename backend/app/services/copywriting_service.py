"""Product copywriting generation service using Gemini text API.

Generates Traditional Chinese (繁體中文) marketing copy for e-commerce product images
based on product details provided by the user.
"""
from __future__ import annotations

import asyncio
import functools
import logging
from typing import Optional

from app import config

logger = logging.getLogger(__name__)


SYSTEM_PROMPT = """\
你是一位專業的電商文案撰寫專家，專精繁體中文行銷文案。
你的任務是根據產品資訊和圖片場景，為每張電商產品圖生成吸引人的繁體中文行銷文案。

要求：
1. 所有文案必須使用繁體中文
2. 文案風格要專業、吸引人、有購買慾
3. 每個場景的文案要根據該場景的用途量身定制
4. 文案要簡潔有力，適合電商平台展示
5. 包含適當的 emoji 增加吸引力
6. 標題控制在 15 字以內，描述控制在 50 字以內
"""


def _sync_generate_copy(
    product_details: str,
    product_type: str,
    scene_names: list[dict[str, str]],
    model: str = "gemini-2.5-flash",
) -> str:
    """Synchronous copy generation — runs in a thread pool."""
    from google import genai
    from google.genai import types

    key = config.GEMINI_API_KEY
    if not key:
        raise RuntimeError("Gemini API Key 未設定")

    client = genai.Client(api_key=key)

    scenes_text = "\n".join(
        f"- 場景 {i+1}: {s['name']} ({s['name_en']}) — {s.get('description', '')}"
        for i, s in enumerate(scene_names)
    )

    # Handle empty/missing product details
    details_stripped = (product_details or "").strip()
    is_no_details = not details_stripped or details_stripped == "(未提供詳情)"

    if is_no_details:
        details_section = f"產品詳情：（用戶未提供具體詳情，請根據「{product_type}」這個產品類型以及下方各場景名稱，自行推斷合理的產品特點、材質、功能等來撰寫文案。文案應通用且專業。）"
    else:
        details_section = f"產品詳情：{details_stripped}"

    user_prompt = f"""\
請為以下產品的每張電商圖片生成繁體中文行銷文案。

【產品資訊】
產品類型：{product_type}
{details_section}

【需要文案的場景圖片】
{scenes_text}

請為每個場景生成文案，嚴格按以下 JSON 格式輸出（不要加 markdown 代碼塊標記）：
[
  {{
    "scene_index": 1,
    "title": "主標題（15字以內）",
    "subtitle": "副標題/賣點（20字以內）",
    "description": "詳細描述文案（50字以內）",
    "hashtags": ["標籤1", "標籤2", "標籤3"]
  }}
]

注意：
- scene_index 從 1 開始，對應上面的場景編號
- 每個場景的文案要針對該場景的特點和用途
- 白底圖的文案著重產品本身特點
- 場景圖的文案要融合場景氛圍
- 賣點圖要突出產品功能和優勢
- hashtags 用於社群媒體推廣
"""

    response = client.models.generate_content(
        model=model,
        contents=[user_prompt],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7,
        ),
    )

    return response.text


async def generate_copy(
    product_details: str,
    product_type: str,
    scene_names: list[dict[str, str]],
) -> str:
    """Generate marketing copy for product images.

    Args:
        product_details: User-provided product description/features.
        product_type: Product category (e.g., "bags", "jewelry").
        scene_names: List of dicts with 'name', 'name_en', 'description' for each scene.

    Returns:
        JSON string containing copy for each scene.
    """
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        None,
        functools.partial(
            _sync_generate_copy,
            product_details=product_details,
            product_type=product_type,
            scene_names=scene_names,
        ),
    )
