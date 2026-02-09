from app.templates.registry import SceneTemplate, TemplateRegistry

HEALTH_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="health_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="health",
        description="純白背景，保健護理產品居中展示",
        prompt=(
            "Place this health and personal care product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with a large softbox overhead at 45 degrees "
            "and two side fill lights for clean, shadowless illumination. "
            "The product should be centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding and depth. "
            "Front-facing angle tilted 10 degrees to show packaging design and form. "
            "Shot with a 70mm lens at f/9 for maximum depth of field across the entire product. "
            "Ultra-high resolution, crisp details on label text, packaging texture, and product surface. "
            "No other objects in frame. Color accuracy is critical for hygiene products."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="health",
        description="2x2 拼圖佈局，展示成分、功能、設計等賣點",
        prompt=(
            "Create a professional product photography collage for this health/personal care product. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front packaging view showing the brand, product name, and key claims. "
            "2) Close-up of the active ingredient or product texture/consistency. "
            "3) Ergonomic design detail: grip, bristle pattern, nozzle, or applicator. "
            "4) Back label or certification marks showing safety and quality standards. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all shots. "
            "Shot with a 60mm lens at f/8 for uniform sharpness. "
            "The layout conveys clinical cleanliness and trustworthy product quality."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="health",
        description="微距特寫，展示刷毛、材質、質地等細節",
        prompt=(
            "Extreme macro close-up photography of this health/personal care product showing quality details. "
            "Split into 2-3 detail zones: bristle tips or product texture at microscopic level, "
            "handle grip pattern and ergonomic contours, and material quality with surface finish. "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The detail level should convey clinical precision and hygiene-grade manufacturing. "
            "Focus stacking technique for maximum sharpness across detail zones. "
            "Clean, clinical lighting with cool white tone for a medical-grade aesthetic. "
            "Professional personal care product macro photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="health",
        description="與手掌、常見洗漱用品對比，直觀展示大小",
        prompt=(
            "This health/personal care product photographed next to common reference objects for size: "
            "a hand holding or gripping the product naturally, and a standard toothbrush or "
            "travel toiletry bag nearby for scale comparison. "
            "All items arranged on a clean white surface with a subtle grid pattern for measurement. "
            "The product is the hero element in the center. "
            "Clean white background, even studio lighting from an overhead softbox. "
            "Shot with a 50mm lens at f/11 to keep all objects tack-sharp. "
            "The items are proportionally realistic to each other. "
            "The composition clearly communicates the product's portable, practical size."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_05_bathroom_scene",
        name="浴室場景",
        name_en="Bathroom Scene",
        product_type="health",
        description="乾淨浴室環境中的產品展示",
        prompt=(
            "This health/personal care product placed naturally in a bright, clean modern bathroom setting. "
            "A pristine white marble or stone countertop next to a sink, with the product as the hero item. "
            "A small potted succulent and a folded white towel nearby for warmth. "
            "Soft natural light streaming through a frosted window from the left, "
            "mixed with clean overhead bathroom lighting. "
            "Shot with a 35mm lens at f/2.8, shallow depth of field keeping the product sharp "
            "while the bathroom provides a clean, spa-like context. "
            "Camera angle slightly above at 20 degrees. Cool-neutral color tones around 5800K. "
            "Fresh, hygienic lifestyle photography conveying daily wellness."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_06_usage_scene",
        name="使用場景",
        name_en="Usage Scene",
        product_type="health",
        description="展示產品實際使用中的自然場景",
        prompt=(
            "A person naturally using this health/personal care product in an authentic daily routine moment. "
            "The scene shows the product in active use: brushing teeth at a vanity mirror, "
            "using a massage tool while relaxing, or applying personal care product in a well-lit bathroom. "
            "Soft, flattering natural light from the side creating gentle shadows. "
            "The person appears relaxed, healthy, and content during their self-care routine. "
            "Shot with a 50mm lens at f/2.0 for cinematic bokeh, "
            "the product and hands in crisp focus against a soft background. "
            "Camera at eye level for an intimate, relatable perspective. "
            "Warm wellness lifestyle photography with authentic, unforced feel."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_07_effect_demo",
        name="效果展示",
        name_en="Effect Demo",
        product_type="health",
        description="展示產品使用效果或前後對比",
        prompt=(
            "A compelling demonstration of this health/personal care product's benefits and results. "
            "Show the product prominently in the foreground with visible evidence of its effectiveness: "
            "a bright confident smile for oral care, relaxed muscles for massage tools, "
            "or clean refreshed skin for personal care products. "
            "Clean, clinical yet warm studio setting with a soft gradient background. "
            "Shot with a 85mm lens at f/3.5, the product and result area in sharp focus "
            "with a professional portrait-style lighting setup: key light at 45 degrees, "
            "fill light opposite, and a subtle backlight for dimension. "
            "The image conveys tangible health benefits and product efficacy. "
            "Trustworthy, professional health product photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_08_care_bundle",
        name="護理組合",
        name_en="Care Bundle",
        product_type="health",
        description="個人護理套組平拍，展示日常護理搭配",
        prompt=(
            "This health/personal care product arranged in a clean flat lay with complementary care items: "
            "matching toothbrush and toothpaste, a face towel, cotton pads, and a small plant or flower. "
            "Top-down perspective on a clean white marble or light wood surface. "
            "Each item neatly spaced with intentional symmetrical arrangement. "
            "The hero product is centrally placed and visually prominent. "
            "Shot overhead with a 35mm lens at f/7.1, even diffused softbox lighting "
            "eliminating harsh shadows while preserving clean, crisp textures. "
            "Professional personal care flat lay photography showing a complete daily wellness routine. "
            "Fresh, clean aesthetic with spa-inspired minimalism."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="health_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="health",
        description="展示品牌調性的健康生活美學",
        prompt=(
            "This health/personal care product styled in a serene wellness lifestyle scene. "
            "A spa-inspired vignette: the product on a natural stone tray alongside "
            "eucalyptus sprigs, a beeswax candle, organic cotton towels, and a small ceramic dish. "
            "Soft morning light filtering through sheer curtains, creating ethereal glow and gentle shadows. "
            "Shot with a 40mm lens at f/4.5 from a slightly elevated angle. "
            "Calming, natural color palette with whites, greens, and soft earth tones. "
            "The composition conveys purity, self-care ritual, and mindful wellness. "
            "Premium health brand campaign aesthetic with a tranquil, editorial feel."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== oral_care (口腔護理) ====================
    SceneTemplate(
        id="health_oral_01_brush",
        name="刷牙場景",
        name_en="Brushing Scene",
        product_type="health",
        description="牙刷或口腔產品在浴室洗手台旁的場景",
        prompt=(
            "This oral care product positioned in a clean, bright bathroom sink area with the faucet and mirror visible. "
            "The toothbrush or oral care device stands upright in a minimalist holder on a white marble countertop, "
            "with a glass of water and a small potted plant nearby for freshness. "
            "Shot with a 50mm lens at f/3.2 from a three-quarter front angle at countertop height. "
            "Cool, clean bathroom lighting mixed with soft natural light from the side "
            "creates a fresh, hygienic atmosphere with gentle highlights on the chrome fixtures. "
            "The scene conveys a clean, modern morning routine and the importance of quality oral care tools."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="oral_care",
        sub_category_name="口腔護理",
    ),
    SceneTemplate(
        id="health_oral_02_set",
        name="套裝展示",
        name_en="Oral Care Set",
        product_type="health",
        description="口腔護理套裝（牙刷、牙膏、牙線）的組合展示",
        prompt=(
            "A complete oral care set neatly arranged: toothbrush, toothpaste, dental floss, "
            "and mouthwash from this product line, displayed together on a clean white surface. "
            "Each item is angled to show its label and design, spaced evenly in a slight arc formation "
            "with the hero product at the center. "
            "Shot from a 20-degree overhead angle with a 50mm lens at f/6.3, "
            "even diffused studio lighting at 5800K creating a clinical yet inviting brightness. "
            "The composition communicates a complete oral care routine, product line cohesion, "
            "and the convenience of a matching dental hygiene system."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="oral_care",
        sub_category_name="口腔護理",
    ),
    SceneTemplate(
        id="health_oral_03_travel",
        name="旅行攜帶",
        name_en="Travel Oral Care Kit",
        product_type="health",
        description="口腔護理旅行套裝的便攜展示",
        prompt=(
            "This oral care product packed in a compact travel toiletry case or pouch, partially unzipped "
            "to reveal the product alongside travel-sized toothpaste and a small mouthwash bottle. "
            "The travel case sits on a hotel bathroom countertop or beside a carry-on suitcase. "
            "Shot with a 45mm lens at f/4.0 from a slight overhead angle, "
            "the product clearly visible inside the open case in sharp focus. "
            "Bright, clean lighting simulating hotel bathroom or travel environment. "
            "The image conveys portability, travel convenience, and maintaining oral care routines on the go, "
            "perfect for travelers who prioritize hygiene."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="oral_care",
        sub_category_name="口腔護理",
    ),
    SceneTemplate(
        id="health_oral_04_close_up",
        name="刷頭特寫",
        name_en="Brush Head Close-up",
        product_type="health",
        description="牙刷刷頭或刷毛的微距特寫",
        prompt=(
            "Extreme macro close-up of the brush head or bristle tips of this oral care product, "
            "showing the bristle pattern, density, tip shape, and any special bristle technology. "
            "Shot with a 100mm macro lens at f/3.2, very shallow depth of field "
            "with the front bristle row in pin-sharp focus graduating into soft blur toward the back. "
            "Ring light illumination creates even, clinical lighting that reveals every bristle fiber. "
            "The background is a clean gradient from white to soft mint green, suggesting freshness. "
            "Professional dental product photography that communicates advanced bristle engineering "
            "and gentle yet effective cleaning technology."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="oral_care",
        sub_category_name="口腔護理",
    ),
    SceneTemplate(
        id="health_oral_05_family",
        name="家庭使用",
        name_en="Family Oral Care",
        product_type="health",
        description="全家人口腔護理產品的組合展示",
        prompt=(
            "A family oral care setup showing multiple sizes or variants of this product: "
            "adult and child versions of the toothbrush in different colors, family-size toothpaste, "
            "and individual holders, all arranged together in a bright bathroom setting. "
            "The products are lined up in a matching holder or displayed on a bathroom shelf. "
            "Shot with a 35mm lens at f/4.5 from a front angle at shelf height, "
            "bright overhead bathroom lighting providing clean, even illumination. "
            "The scene is colorful and cheerful, conveying that oral care is a family activity. "
            "The composition communicates product range variety and family-friendly design."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="oral_care",
        sub_category_name="口腔護理",
    ),
    # ==================== massage (按摩器具) ====================
    SceneTemplate(
        id="health_mass_01_using",
        name="使用場景",
        name_en="Massage Device in Use",
        product_type="health",
        description="模特使用按摩器具的展示",
        prompt=(
            "A model using this massage device on their neck, shoulders, or back in a relaxed seated position "
            "on a comfortable sofa or yoga mat in a serene home environment. "
            "The device is pressed against the target muscle area, clearly showing its ergonomic design in action. "
            "Shot with a 70mm lens at f/2.8 from a three-quarter angle, the device and contact area in sharp focus "
            "while the calm living room background softens into peaceful bokeh. "
            "Warm, ambient side lighting from a floor lamp creates a relaxing atmosphere with gentle skin highlights. "
            "The model's expression conveys relief and relaxation, demonstrating the product's therapeutic benefit."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="massage",
        sub_category_name="按摩器具",
    ),
    SceneTemplate(
        id="health_mass_02_body_parts",
        name="部位展示",
        name_en="Body Parts Application",
        product_type="health",
        description="展示按摩器具在不同身體部位的使用",
        prompt=(
            "A collage showing this massage device applied to three different body areas: "
            "neck and shoulders in the top panel, lower back in the middle, and legs or feet in the bottom panel. "
            "Each panel shows the device in contact with the specific body area from a clear, informative angle. "
            "Consistent warm lighting and a neutral background across all panels at 5500K. "
            "Shot with a 50mm lens at f/4.0, each application clearly visible with the device in sharp focus. "
            "Clean white dividers between panels for a professional product guide layout. "
            "The composition serves as a practical usage guide showing the device's versatility "
            "across multiple muscle groups and tension points."
        ),
        aspect_ratio="3:4",
        injection_level="light",
        sub_category="massage",
        sub_category_name="按摩器具",
    ),
    SceneTemplate(
        id="health_mass_03_relaxation",
        name="放鬆場景",
        name_en="Relaxation Scene",
        product_type="health",
        description="在放鬆的居家環境中使用按摩器的場景",
        prompt=(
            "This massage device being used in a tranquil home relaxation setting: "
            "a cozy reading nook with soft throw blankets, ambient candles, and warm fairy lights in the background. "
            "The user reclines comfortably while the massage device works on their shoulders or feet. "
            "Shot with a 35mm lens at f/2.4 from a slightly elevated angle, "
            "warm golden lamplight creating a serene, spa-like home atmosphere. "
            "The device is clearly visible and in sharp focus as the functional hero of the relaxation scene. "
            "Soft, diffused lighting with warm tones around 4500K. "
            "The image conveys deep relaxation, self-care, and the luxury of at-home therapeutic massage."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="massage",
        sub_category_name="按摩器具",
    ),
    SceneTemplate(
        id="health_mass_04_intensity",
        name="力度展示",
        name_en="Intensity Settings Display",
        product_type="health",
        description="展示按摩器具可調節的力度和模式",
        prompt=(
            "Close-up of this massage device's control panel or adjustment mechanism, "
            "showing the intensity levels, mode buttons, LED indicators, or speed settings. "
            "The device is held at an angle that clearly displays the interface with one button being pressed "
            "and the LED screen or indicator lights illuminated. "
            "Shot with a 60mm macro lens at f/4.5, the control area in razor-sharp focus "
            "with the rest of the device body in soft focus for depth. "
            "Clean studio lighting with a subtle blue accent light suggesting technology and precision. "
            "The image communicates ease of use, multiple customization options, "
            "and the sophisticated engineering behind adjustable therapeutic massage."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="massage",
        sub_category_name="按摩器具",
    ),
    SceneTemplate(
        id="health_mass_05_portable",
        name="便攜展示",
        name_en="Portable Massage Device",
        product_type="health",
        description="便攜式按摩器放入包中或隨身攜帶的展示",
        prompt=(
            "This compact massage device shown partially tucked into an open gym bag, backpack, or travel case, "
            "demonstrating its portable size and on-the-go convenience. "
            "The bag sits on a bench in a gym locker room or an airport lounge seating area. "
            "The device is clearly visible, standing out from other bag contents. "
            "Shot with a 45mm lens at f/3.5 from a slight overhead angle, "
            "the device in sharp focus while the travel context provides soft, lifestyle background. "
            "Bright, even lighting suggests an active, mobile lifestyle. "
            "The composition conveys that this massage device is compact enough to travel anywhere "
            "and fits seamlessly into an active person's daily routine."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="massage",
        sub_category_name="按摩器具",
    ),
    # ==================== personal_care (個人護理) ====================
    SceneTemplate(
        id="health_pc_01_routine",
        name="日常使用",
        name_en="Daily Care Routine",
        product_type="health",
        description="個人護理產品在日常使用中的場景",
        prompt=(
            "This personal care product being used as part of a daily routine: "
            "a person applying the product at a well-lit vanity mirror or bathroom countertop, "
            "with the packaging visible alongside their skincare and grooming essentials. "
            "Shot with a 50mm lens at f/2.8 from a three-quarter angle at counter height, "
            "the product and hands in sharp focus against a softly blurred mirror reflection and bathroom background. "
            "Soft, flattering natural side light creates gentle highlights on skin and product surfaces. "
            "The scene feels authentic and aspirational, showing the product as an essential step "
            "in a thoughtful, well-curated daily personal care routine."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="personal_care",
        sub_category_name="個人護理",
    ),
    SceneTemplate(
        id="health_pc_02_bathroom",
        name="浴室擺放",
        name_en="Bathroom Shelf Display",
        product_type="health",
        description="個人護理產品在浴室架子或檯面上的擺放",
        prompt=(
            "This personal care product displayed on a clean bathroom shelf or countertop alongside complementary items: "
            "a hand towel, a small succulent, a soap dispenser, and a decorative tray. "
            "The product is the hero item positioned at the front, label facing the camera. "
            "Shot with a 45mm lens at f/3.5 from a straight-on shelf-level angle, "
            "the product in crisp focus with the bathroom tiles and fixtures providing clean depth. "
            "Bright, cool-toned overhead lighting mixed with natural window light creates a fresh, hygienic atmosphere. "
            "The composition communicates organized bathroom aesthetics and shows how the product "
            "integrates beautifully into a modern, minimalist bathroom design."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="personal_care",
        sub_category_name="個人護理",
    ),
    SceneTemplate(
        id="health_pc_03_ingredients",
        name="成分展示",
        name_en="Natural Ingredients Display",
        product_type="health",
        description="個人護理產品與天然成分的展示",
        prompt=(
            "This personal care product styled with its key natural ingredients arranged around it: "
            "fresh aloe vera leaves, lavender sprigs, honey in a small dish, coconut halves, "
            "or citrus slices, depending on the product's formulation. "
            "Shot from a slight overhead angle with a 50mm lens at f/4.0 on a clean natural wood or stone surface. "
            "Soft, bright studio lighting at 5500K emphasizes the freshness of the ingredients "
            "and the clean packaging design of the product. "
            "The product is centrally placed with ingredients fanning out around it. "
            "The composition conveys natural, clean beauty and transparent ingredient sourcing."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="personal_care",
        sub_category_name="個人護理",
    ),
    SceneTemplate(
        id="health_pc_04_travel",
        name="旅行裝",
        name_en="Travel Size Products",
        product_type="health",
        description="旅行裝個人護理產品的便攜展示",
        prompt=(
            "Travel-sized versions of this personal care product neatly packed in a clear TSA-approved toiletry bag, "
            "partially unzipped to show the products inside alongside mini bottles and travel containers. "
            "The toiletry bag sits on a hotel bathroom counter or beside a packed suitcase. "
            "Shot with a 45mm lens at f/4.0 from a slight overhead angle, "
            "the products clearly visible through the transparent bag with sharp focus on the hero item. "
            "Clean, bright lighting simulating a travel environment. "
            "The image communicates travel readiness, compact convenience, and the ability to maintain "
            "a full personal care routine while on the go."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="personal_care",
        sub_category_name="個人護理",
    ),
    SceneTemplate(
        id="health_pc_05_comparison",
        name="前後對比",
        name_en="Before and After Comparison",
        product_type="health",
        description="個人護理產品使用前後效果對比",
        prompt=(
            "A split-composition image demonstrating this personal care product's effectiveness: "
            "the left side shows a before state with the product placed prominently at the dividing line, "
            "and the right side shows the improved after result. "
            "The product bottle or device is positioned centrally at the split point as the hero solution. "
            "Shot with an 85mm lens at f/4.0, the product in sharp focus with both sides clearly visible. "
            "Clean, even studio lighting at 5500K with a subtle warm tone on the after side "
            "and slightly cooler tone on the before side to visually reinforce the transformation. "
            "Professional health product efficacy photography that builds trust and demonstrates real results."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="personal_care",
        sub_category_name="個人護理",
    ),
]

TemplateRegistry.register("health", HEALTH_TEMPLATES)
