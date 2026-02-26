"""
優化後的包包類產品提示詞模板

改進重點：
1. 更精確的相機參數（焦距、光圈、ISO、快門）
2. 具體的光線描述（色溫、方向、強度、修飾器）
3. 明確的否定提示（Negative Prompts）
4. 產品特定細節（材質、紋理、五金）
5. 電商平台合規要素
"""

from app.templates.registry import SceneTemplate, TemplateRegistry

BAG_TEMPLATES_OPTIMIZED = [
    # ===== Common (通用場景) =====
    SceneTemplate(
        id="bag_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="bags",
        description="純白背景，產品居中，符合各平台主圖規範",
        prompt=(
            "Professional e-commerce product photography of a bag on pure white background (RGB 255,255,255). "
            "Camera: Sony A7R V with 90mm macro lens at f/8, ISO 100, 1/160s. "
            "Lighting: Large octagonal softbox overhead at 45° (main), two strip boxes on sides for fill (ratio 2:1), "
            "white bounce cards below for shadow fill. Color temperature 5500K ± 200K. "
            "Composition: Product centered, occupying 75-85% of frame. Slight 15° tilt to show depth. "
            "The bag shows natural soft shadow beneath (feathered, not harsh). "
            "Ultra-sharp focus on front surface, stitching details visible at 100% zoom. "
            "Material texture (leather grain, canvas weave, nylon sheen) clearly rendered. "
            "No color cast, accurate product colors. "
            "NEGATIVE: No props, no text, no watermark, no reflections on white surface, "
            "no harsh shadows, no color tint, no blur, no background gradient."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    
    SceneTemplate(
        id="bag_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="bags",
        description="2x2 拼圖佈局，多角度展示產品核心賣點",
        prompt=(
            "Four-panel product specification grid for a bag, clean 2x2 layout on pure white background. "
            "Panel 1 (Top-Left): Front view at 10° angle showing overall silhouette and brand logo. "
            "Panel 2 (Top-Right): Macro detail of material texture and stitching quality, 100mm macro at f/5.6. "
            "Panel 3 (Bottom-Left): Hardware detail - zipper pull, buckle, metal clasp with visible metallic reflections. "
            "Panel 4 (Bottom-Right): Interior view showing lining material and inner pockets. "
            "Consistent lighting across all panels: 5500K studio strobes, soft even illumination. "
            "Each panel has 15px white space border. Unified color temperature and exposure. "
            "Professional product catalog aesthetic, premium brand quality. "
            "NEGATIVE: No text overlays, no arrows, no inconsistent lighting between panels, "
            "no color variation, no busy backgrounds."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    
    SceneTemplate(
        id="bag_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="bags",
        description="微距特寫，展示材質紋理、車線、五金配件",
        prompt=(
            "Extreme macro detail photography of bag craftsmanship. "
            "Camera: Canon EOS R5 with RF 100mm f/2.8L Macro at f/4, ISO 200, 1/200s. "
            "Focus stacking technique for maximum depth of field across detail zones. "
            "Zone A: Material texture - leather grain, canvas weave pattern, or nylon ripstop texture at 1:1 magnification. "
            "Zone B: Precision stitching - even thread tension, consistent stitch length (8-10 stitches per inch visible). "
            "Zone C: Metal hardware - zipper teeth, pull tab, buckle mechanism with surface reflections. "
            "Lighting: Ring light (even illumination) + single directional side light at 45° to reveal texture via micro-shadows. "
            "Color temperature: 5000K neutral white. "
            "Background: Neutral gray 18% card for color reference. "
            "NEGATIVE: No dust particles, no fingerprints on hardware, no loose threads, "
            "no uneven lighting, no color cast, no out-of-focus areas on main subject."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    
    SceneTemplate(
        id="bag_05_daily_scene",
        name="日常場景",
        name_en="Daily Life Scene",
        product_type="bags",
        description="咖啡廳/辦公桌等日常使用情境",
        prompt=(
            "Lifestyle product photography of a bag in modern cafe setting. "
            "Scene: Light oak wooden table, laptop (MacBook Pro or similar) in background, "
            "ceramic coffee cup with latte art nearby, small succulent plant as accent. "
            "Camera: Sony A7 IV with 35mm f/1.4 at f/2.8, ISO 400, 1/125s. "
            "Natural window light from left side (soft diffused daylight, approximately 5600K), "
            "white sheer curtain as natural diffuser. Gentle shadows on right side. "
            "The bag placed naturally on table, slightly angled toward camera, as if just set down. "
            "Shallow depth of field: bag in sharp focus, background softly blurred (bokeh circles visible). "
            "Color palette: Warm neutrals, cream, light wood tones, green plant accent. "
            "Mood: Productive morning, aspirational yet relatable lifestyle. "
            "NEGATIVE: No harsh artificial lighting, no cluttered background, no competing colors, "
            "no plastic-looking props, no unrealistic shadows, no over-saturated colors."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    
    SceneTemplate(
        id="bag_07_model_carry",
        name="模特展示",
        name_en="Model Showcase",
        product_type="bags",
        description="模特背著/手提包包，展示實際使用效果",
        prompt=(
            "Fashion editorial photography: model wearing/carrying a bag as hero accessory. "
            "Camera: Hasselblad X2D with 80mm f/1.9 at f/4, ISO 100, 1/250s. "
            "Studio setup: Large octabox as key light (camera left, 45°), fill card opposite, "
            "hair light from behind for separation, gray seamless backdrop. "
            "Model styling: Simple solid-color clothing (black, white, or beige) that doesn't compete with bag. "
            "Pose: Natural confident stance, 3/4 view to camera, bag clearly visible at chest/hip level. "
            "Focus: Critical sharpness on bag surface and hardware, slight softness on model's face acceptable. "
            "Color grading: Neutral with slight warmth, maintaining bag's true colors. "
            "Composition following rule of thirds, bag at intersection point. "
            "NEGATIVE: No busy patterns on clothing, no distracting jewelry, no logos on clothing, "
            "no harsh shadows on bag, no washed-out colors, no awkward poses, no looking directly at camera."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
]

# 使用說明：
# 這些優化後的提示詞特點：
# 1. 具體相機參數讓 AI 生成更真實的景深和透視
# 2. 詳細光線設置確保一致的照明風格
# 3. 否定提示避免常見的 AI 生成問題
# 4. 產品特定細節提升專業感
# 5. 電商合規要素（白底、無水印、準確色彩）
