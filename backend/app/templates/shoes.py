from app.templates.registry import SceneTemplate, TemplateRegistry

SHOES_TEMPLATES = [
    # ===== Common (通用場景) =====
    SceneTemplate(
        id="shoes_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="shoes",
        description="純白背景，鞋子 45 度角展示，標準主圖",
        prompt=(
            "This shoe product on a pure white background at a 3/4 angle (45 degrees). "
            "Professional footwear photography with soft box lighting. "
            "The shoe is centered, occupying about 80% of the frame. "
            "Slight shadow beneath for grounding. Shows the outer side profile clearly. "
            "Shot with a 90mm lens at f/11 for front-to-back sharpness across the entire shoe. "
            "Ultra-crisp focus on materials and design details. "
            "Commercial e-commerce quality."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="shoes",
        description="展示鞋底、鞋墊、材質等核心賣點",
        prompt=(
            "Create a professional footwear infographic for this shoe. "
            "Show the shoe at a dynamic angle on a clean white background. "
            "Add elegant callout lines pointing to 4 key features: "
            "the upper material, the sole technology/grip, the cushioning/insole, "
            "and any special design elements (breathable mesh, waterproof coating, etc). "
            "Clean modern typography with small icons. "
            "Lit with dual softboxes flanking the shoe at 45-degree angles for even, detail-revealing illumination. "
            "Nike/Adidas product page aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="shoes",
        description="材質紋理、鞋底花紋、車線工藝特寫",
        prompt=(
            "Extreme close-up of this shoe showing craftsmanship and material quality. "
            "Multiple detail shots: upper material texture, sole tread pattern, "
            "stitching quality, logo embossing, lace/buckle hardware. "
            "Macro photography with a dedicated macro lens at f/5.6 and ring light illumination for shadow-free detail capture. "
            "Add a focused side spot at a low 15-degree angle to reveal surface texture and depth in stitching. "
            "Professional product detail photography for premium footwear."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="shoes",
        description="穿在腳上展示，搭配褲腳效果",
        prompt=(
            "This shoe worn on a person's feet, photographed from a natural standing angle. "
            "Show both shoes on feet with the bottom of pants/jeans visible. "
            "Clean floor surface (light wood or white). "
            "The photo helps buyers see how the shoe looks when actually worn, "
            "including its proportion relative to the foot and ankle. "
            "Shot at f/4 with an 85mm lens at ankle height to show accurate on-foot proportions. "
            "Natural lighting, sharp focus on the shoes."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_05_daily_scene",
        name="日常場景",
        name_en="Daily Life Scene",
        product_type="shoes",
        description="日常穿著走路、通勤等場景",
        prompt=(
            "A person wearing this shoe walking on a clean city sidewalk or modern indoor space. "
            "Shot from knee-down angle focusing on the shoes in motion. "
            "Natural daylight photography with soft shadows. "
            "Camera positioned low at approximately 30 degrees from ground level, shot at f/2.8 with an 85mm lens. "
            "Urban lifestyle photography showing everyday use. "
            "The shoes are the clear hero with sharp focus, "
            "background has pleasant soft bokeh with gentle directional sunlight creating depth."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_06_outdoor_scene",
        name="戶外場景",
        name_en="Outdoor Scene",
        product_type="shoes",
        description="運動/戶外/旅行等穿著場景",
        prompt=(
            "This shoe in an active outdoor setting: on a hiking trail, at a park, "
            "on gym steps, or a running track depending on the shoe style. "
            "Dynamic angle showing the shoe in its intended environment. "
            "Golden hour or bright daylight with a reflector used to bounce warm fill light onto the shoe. "
            "Shot from a low angle at f/4 with a 70mm lens to make the shoe appear powerful and grounded. "
            "Energetic, aspirational lifestyle photography. "
            "The shoe is sharply focused against a natural outdoor background."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_07_multi_angle",
        name="多角度展示",
        name_en="Multi-Angle View",
        product_type="shoes",
        description="正面、側面、底部多角度展示",
        prompt=(
            "This shoe shown from multiple angles in a single composed image: "
            "side profile view, front view, and sole/bottom view. "
            "Clean white background for all angles. "
            "Neatly arranged in a grid or diagonal layout. "
            "Professional studio lighting consistent across all angles using a large overhead diffusion panel and side fill cards. "
            "Each angle shot at f/8 with a 90mm lens for uniform sharpness and perspective. "
            "Helps buyers see the complete shoe design from every perspective."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_08_pair_display",
        name="成雙展示",
        name_en="Pair Display",
        product_type="shoes",
        description="一雙鞋的完整展示，展示配對效果",
        prompt=(
            "Both shoes of this pair artfully arranged together. "
            "One shoe placed normally, the other at a slight angle leaning against it. "
            "Clean white or light gray background. "
            "Professional footwear photography with beautiful lighting using a key softbox overhead and a low-angle accent light to highlight material sheen. "
            "Shot at f/8 with a 85mm lens from a slightly elevated 30-degree angle for a balanced view of both shoes. "
            "The composition is dynamic yet balanced. Premium product photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="shoes_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="shoes",
        description="展示品牌調性的時尚穿搭照",
        prompt=(
            "A full outfit shot featuring this shoe as the key piece. "
            "Styled with a complete fashionable outfit. "
            "Shot in a visually interesting location: minimalist studio, urban loft, or outdoor. "
            "The camera angle emphasizes the shoes while showing the full look. "
            "Shot at f/2.8 with a 50mm prime lens from a low three-quarter angle to draw the eye toward the footwear. "
            "Fashion editorial quality with creative color grading and warm-toned rim lighting for atmosphere. "
            "Aspirational brand lifestyle photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ===== Sneakers (運動鞋) =====
    SceneTemplate(
        id="shoe_snkr_01_sole_detail",
        name="鞋底展示",
        name_en="Sole Detail",
        product_type="shoes",
        description="由下往上展示鞋底紋路與科技材質",
        prompt=(
            "This sneaker photographed from directly below, showing the full sole pattern and tread design. "
            "The shoe is held or suspended so the bottom faces the camera, filling about 85% of the frame. "
            "Every groove, grip pattern, and cushioning technology in the sole is clearly visible. "
            "Shot with a macro lens at f/8 for edge-to-edge sharpness across the entire sole. "
            "Bright, even lighting from two large softboxes flanking the shoe from above to illuminate every tread detail. "
            "Clean white background. "
            "The image communicates the sole's engineering, grip technology, and durability. "
            "Professional technical footwear photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="sneakers",
        sub_category_name="運動鞋",
    ),
    SceneTemplate(
        id="shoe_snkr_02_on_feet",
        name="上腳效果",
        name_en="On Feet",
        product_type="shoes",
        description="模特穿著運動鞋的腰部以下展示",
        prompt=(
            "A model wearing these sneakers, photographed from the waist down in a natural standing pose. "
            "The sneakers are paired with casual athletic or streetwear pants, showing the full on-foot look. "
            "Both feet are visible, one slightly forward for a dynamic stance. "
            "Clean concrete or light pavement floor surface. "
            "Natural daylight from the side creates gentle shadows that define the shoe's shape on foot. "
            "Shot at f/4 with a 50mm lens from a low angle, approximately 45 degrees from ground level. "
            "The sneakers are the sharpest elements with pleasant bokeh on the upper body. "
            "Street style sneaker photography showing authentic on-foot appearance."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="sneakers",
        sub_category_name="運動鞋",
    ),
    SceneTemplate(
        id="shoe_snkr_03_lacing",
        name="鞋帶細節",
        name_en="Lacing Detail",
        product_type="shoes",
        description="鞋帶系統與鞋舌設計的近距離特寫",
        prompt=(
            "Close-up shot of this sneaker's lacing system and tongue area. "
            "Show the lace threading through eyelets, the tongue padding and logo, "
            "and the collar cushioning around the ankle opening. "
            "The laces are neatly tied in a fresh, clean configuration. "
            "Shot with a 100mm macro lens at f/4 for beautiful shallow depth of field focused on the lacing zone. "
            "Directional side lighting from the left at a 30-degree angle to reveal eyelet depth and lace texture. "
            "Clean neutral background. "
            "The image highlights the quality of the lacing hardware and the tongue construction. "
            "Premium sneaker detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="sneakers",
        sub_category_name="運動鞋",
    ),
    SceneTemplate(
        id="shoe_snkr_04_running",
        name="運動場景",
        name_en="Action Running",
        product_type="shoes",
        description="運動鞋在跑步或運動中的動態場景",
        prompt=(
            "A runner in mid-stride wearing these sneakers on a clean running track or scenic park trail. "
            "Shot from a low ground-level angle, focusing on the feet and lower legs in dynamic motion. "
            "The front foot is mid-push-off, showing the sole flex and heel cushion compression. "
            "Frozen motion at 1/1000s shutter speed with sharp detail on the shoe despite movement. "
            "Natural bright daylight with a warm side light from golden hour sun. "
            "Shot at f/2.8 with a 70-200mm lens for dramatic compression. "
            "The background shows a blurred track or path with bokeh. "
            "Energetic, athletic lifestyle photography showcasing the sneaker's performance capabilities."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="sneakers",
        sub_category_name="運動鞋",
    ),
    SceneTemplate(
        id="shoe_snkr_05_collection",
        name="系列展示",
        name_en="Colorway Collection",
        product_type="shoes",
        description="多種配色的運動鞋一起展示的系列照",
        prompt=(
            "Three to five different colorways of this sneaker displayed together in a dynamic arrangement. "
            "The shoes are arranged in a staggered diagonal line or fan pattern on a clean white surface. "
            "Each shoe is at a slightly different angle to show the color variant clearly. "
            "The hero colorway is in the center or most prominent position. "
            "Consistent even studio lighting from a large overhead softbox at 5500K for accurate color rendering. "
            "Shot at f/8 with a 50mm lens from a 30-degree elevated angle. "
            "The composition showcases the full range of available colors and patterns. "
            "Professional sneaker collection photography for product line presentation."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="sneakers",
        sub_category_name="運動鞋",
    ),
    # ===== Sandals (涼拖鞋) =====
    SceneTemplate(
        id="shoe_sandal_01_beach",
        name="海灘場景",
        name_en="Beach Scene",
        product_type="shoes",
        description="涼鞋放在沙灘上的夏日度假場景",
        prompt=(
            "These sandals placed casually on a pristine sandy beach near the water's edge. "
            "Gentle waves visible in the soft-focus background, turquoise ocean meeting golden sand. "
            "The sandals are slightly askew in a natural, just-kicked-off placement. "
            "Warm, bright summer sunlight from above and slightly behind, creating a rim glow on the sandal edges. "
            "Shot at f/4 with a 50mm lens from a low 20-degree angle to make the sandals appear large against the ocean backdrop. "
            "Small seashells or smooth pebbles near the sandals for natural beach styling. "
            "Vacation lifestyle photography that evokes summer relaxation and beach getaways."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="sandals",
        sub_category_name="涼拖鞋",
    ),
    SceneTemplate(
        id="shoe_sandal_02_toe_detail",
        name="前端設計",
        name_en="Toe Strap Detail",
        product_type="shoes",
        description="涼鞋前端繫帶設計的近距離特寫",
        prompt=(
            "Close-up shot focusing on the toe area and front strap design of these sandals. "
            "Show the strap material, buckle or closure mechanism, and how the straps connect to the sole. "
            "The sandal is placed on a clean white or natural stone surface at a slight angle. "
            "Shot with a 100mm macro lens at f/4 for shallow depth of field isolating the front design. "
            "Soft directional lighting from the upper left at 45 degrees to reveal strap texture and hardware shine. "
            "A subtle fill from the right prevents harsh shadows. "
            "The image highlights the sandal's front design craftsmanship and comfortable toe fit. "
            "Professional footwear detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="sandals",
        sub_category_name="涼拖鞋",
    ),
    SceneTemplate(
        id="shoe_sandal_03_indoor",
        name="室內穿著",
        name_en="Indoor Wear",
        product_type="shoes",
        description="模特在室內穿著拖鞋的居家場景",
        prompt=(
            "A person wearing these slippers or indoor sandals in a cozy home environment. "
            "Shot from knee-down showing the feet on a warm wooden floor or soft carpet. "
            "The home setting includes subtle details: a sofa leg, a coffee table corner, natural light from a window. "
            "Relaxed, comfortable atmosphere with warm morning or afternoon light. "
            "Shot at f/3.5 with a 50mm lens from a low angle near floor level. "
            "The slippers are in sharp focus against a pleasantly blurred domestic background. "
            "The image conveys comfort, warmth, and everyday home relaxation. "
            "Cozy lifestyle footwear photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="sandals",
        sub_category_name="涼拖鞋",
    ),
    SceneTemplate(
        id="shoe_sandal_04_pool",
        name="泳池邊",
        name_en="Poolside",
        product_type="shoes",
        description="涼鞋放在泳池邊的清涼場景",
        prompt=(
            "These sandals placed at the edge of a sparkling swimming pool. "
            "The sandals sit on clean white or light stone pool deck tiles, with the clear blue pool water visible adjacent. "
            "Water reflections create dancing light patterns on the sandals. "
            "Bright, overhead summer sunlight with strong but not harsh highlights. "
            "A folded towel and sunglasses nearby for poolside lifestyle context. "
            "Shot at f/5.6 with a 35mm lens from a 40-degree angle to capture both the sandals and the pool water. "
            "Cool blue and warm white color palette. "
            "Resort lifestyle photography that conveys summer fun and water activities."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="sandals",
        sub_category_name="涼拖鞋",
    ),
    SceneTemplate(
        id="shoe_sandal_05_summer_outfit",
        name="夏日穿搭",
        name_en="Summer Outfit",
        product_type="shoes",
        description="涼鞋搭配夏日服裝的完整穿搭展示",
        prompt=(
            "A model wearing these sandals styled with a complete summer outfit: "
            "linen shorts or a flowing summer dress, paired with a straw tote bag. "
            "Full body shot from head to toe on a bright outdoor terrace or garden path. "
            "Warm, golden summer sunlight creating a cheerful, relaxed atmosphere. "
            "Shot at f/4 with a 50mm lens at waist height, with the sandals clearly visible and in focus. "
            "The camera captures the full outfit coordination from head to toe. "
            "Light, airy color tones with soft shadows. "
            "Summer lifestyle fashion photography showcasing the sandals as part of a complete warm-weather look."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="sandals",
        sub_category_name="涼拖鞋",
    ),
    # ===== Heels (高跟鞋) =====
    SceneTemplate(
        id="shoe_heel_01_profile",
        name="側面線條",
        name_en="Side Profile",
        product_type="shoes",
        description="高跟鞋優雅側面線條的展示",
        prompt=(
            "This high heel shoe photographed in pure side profile, showing the elegant arch from toe to heel. "
            "The heel curve, platform height, and toe shape are all clearly defined. "
            "Clean white or soft gradient background. "
            "Dramatic directional lighting from behind at a 30-degree angle creates a beautiful rim light along the shoe's silhouette. "
            "A soft front fill prevents the front from going too dark. "
            "Shot at f/8 with a 90mm lens at exact shoe height for a true side-on perspective. "
            "The image emphasizes the heel's sculptural design and elegant proportions. "
            "High-fashion footwear photography with an architectural quality."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="heels",
        sub_category_name="高跟鞋",
    ),
    SceneTemplate(
        id="shoe_heel_02_on_stairs",
        name="階梯展示",
        name_en="Staircase Display",
        product_type="shoes",
        description="高跟鞋放在大理石階梯上的優雅展示",
        prompt=(
            "These high heels placed elegantly on polished marble or stone staircase steps. "
            "One heel on a higher step, the other on the step below, creating visual depth and drama. "
            "The marble texture adds a luxurious backdrop with subtle veining patterns. "
            "Warm ambient lighting from a window to the side, supplemented by a soft directional accent light. "
            "Shot at f/4 with a 70mm lens from a low angle looking slightly upward at the shoes. "
            "The composition creates a sense of ascension and aspiration. "
            "Shallow depth of field with the front heel sharp and the rear heel slightly soft. "
            "Luxury fashion editorial photography for premium footwear."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="heels",
        sub_category_name="高跟鞋",
    ),
    SceneTemplate(
        id="shoe_heel_03_evening",
        name="晚宴穿搭",
        name_en="Evening Styling",
        product_type="shoes",
        description="高跟鞋搭配晚禮服的腳踝以下展示",
        prompt=(
            "A model wearing these high heels with an elegant evening dress, shot from ankle down. "
            "The dress hem is visible just above the ankle, showing the elegant transition from dress to heel. "
            "The model stands on a polished dark floor that reflects the heels subtly. "
            "Shot from a low ground-level angle at f/3.5 with an 85mm lens. "
            "Warm, low ambient lighting reminiscent of a formal event venue with soft overhead spotlights. "
            "The heels catch beautiful highlights on their patent or satin surface. "
            "The image conveys sophistication, glamour, and evening elegance. "
            "Formal event fashion photography focusing on the footwear."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="heels",
        sub_category_name="高跟鞋",
    ),
    SceneTemplate(
        id="shoe_heel_04_heel_detail",
        name="鞋跟特寫",
        name_en="Heel Detail",
        product_type="shoes",
        description="鞋跟設計與材質的微距特寫",
        prompt=(
            "Extreme macro close-up focused on the heel portion of this high heel shoe. "
            "Show the heel's shape, material finish (wrapped leather, lacquered wood, metal tip), "
            "and the precision of where the heel meets the sole. "
            "The heel fills about 80% of the frame at high magnification. "
            "Shot with a 100mm macro lens at f/4 with focus stacking for complete sharpness. "
            "Dramatic spot lighting from the side at a low 15-degree angle to reveal material texture and construction quality. "
            "Clean dark background to make the heel design pop. "
            "The image showcases the engineering and craftsmanship of the heel construction. "
            "Luxury footwear macro photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="heels",
        sub_category_name="高跟鞋",
    ),
    SceneTemplate(
        id="shoe_heel_05_red_carpet",
        name="紅毯風格",
        name_en="Red Carpet Style",
        product_type="shoes",
        description="高跟鞋在華麗紅毯風格場景中的展示",
        prompt=(
            "These high heels styled in a glamorous red carpet inspired setting. "
            "The shoes are placed on or beside a deep red velvet surface or actual red carpet runner. "
            "Dramatic lighting with warm spotlights creating golden highlights on the shoe's surface. "
            "A touch of sparkle from scattered crystal elements or a champagne glass nearby for luxury context. "
            "Shot at f/2.8 with a 85mm lens from a low 20-degree angle for a dramatic, aspirational perspective. "
            "Rich, warm color palette dominated by deep reds, golds, and the shoe's color. "
            "The shallow depth of field creates a dreamy background glow. "
            "Celebrity red carpet glamour photography for premium high heels."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="heels",
        sub_category_name="高跟鞋",
    ),
]

TemplateRegistry.register("shoes", SHOES_TEMPLATES)
