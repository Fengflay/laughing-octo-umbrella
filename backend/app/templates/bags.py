from app.templates.registry import SceneTemplate, TemplateRegistry

BAG_TEMPLATES = [
    # ===== Common (通用場景) =====
    SceneTemplate(
        id="bag_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="bags",
        description="純白背景，產品居中，符合各平台主圖規範",
        prompt=(
            "Place this bag product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with soft box lighting from above at 45 degrees and two side fill lights. "
            "The bag should be centered, occupying about 85% of the frame. "
            "Slight natural shadow beneath the bag for depth. "
            "Front-facing angle slightly tilted 15 degrees to show depth and dimension. "
            "Ultra-high resolution, crisp details on stitching, hardware and material texture. "
            "No other objects in frame. Color accuracy is critical."
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
            "Create a professional product photography collage for this bag. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the main design and brand details. "
            "2) Close-up of the premium material texture and stitching quality. "
            "3) Hardware and zipper detail shot with metallic shine visible. "
            "4) Strap and carrying mechanism from the side angle. "
            "Each view is clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "The overall layout is balanced and looks like a premium product specification page."
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
            "Extreme macro close-up photography of this bag showing fine craftsmanship details. "
            "Split into 2-3 detail zones: material texture and grain pattern, precise stitching lines, "
            "and metal hardware/zipper quality with reflections. "
            "Shot with 100mm macro lens at f/4, shallow depth of field, ring light illumination. "
            "The texture should be so detailed you can almost feel the material. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional product detail photography for luxury e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="bag_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="bags",
        description="與筆電、手機等常見物品對比，直觀展示大小",
        prompt=(
            "This bag photographed from a straight-on front angle next to a standard 15-inch laptop "
            "and a standard smartphone for size comparison. "
            "All items are standing upright on a clean white surface. "
            "The bag is in the center as the hero element. "
            "The laptop is leaning against the bag on one side, the smartphone placed on the other side. "
            "A subtle grid pattern on the surface beneath for scale reference. "
            "Clean white background, even studio lighting from above. "
            "The items are proportionally realistic to each other. "
            "The composition clearly communicates the bag's practical everyday size."
        ),
        aspect_ratio="1:1",
        injection_level="none",
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
            "This bag placed naturally on a wooden table in a bright, modern cafe or co-working space. "
            "A laptop and coffee cup visible nearby. Warm natural window light streaming in from the left. "
            "The scene conveys a productive, stylish daily routine. "
            "Lifestyle photography with soft bokeh background, shot at f/2.8. "
            "The bag should be the clear focal point, taking up about 40% of the frame. "
            "Warm color tones around 5800K, inviting atmosphere. "
            "Camera angle slightly above at 30 degrees."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="bag_06_outdoor_scene",
        name="戶外場景",
        name_en="Outdoor Scene",
        product_type="bags",
        description="街頭/公園/旅行等戶外使用場景",
        prompt=(
            "This bag in an outdoor urban setting: placed on a clean park bench or stone ledge "
            "with a beautiful city street or green park in the soft-focus background. "
            "Golden hour natural lighting creating warm tones and gentle shadows. "
            "Travel and adventure lifestyle mood. "
            "The bag is the hero subject, sharply focused against the dreamy bokeh background. "
            "Aspirational outdoor lifestyle photography. "
            "Shot at eye level, f/2.0 for beautiful background separation."
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
            "A stylish person carrying this bag in a natural, confident pose. "
            "Shot from waist up, the bag is clearly visible and is the focal point. "
            "Clean neutral background (light beige or soft gray studio backdrop). "
            "Fashion editorial lighting: key light at 45 degrees with soft fill and hair light. "
            "The model wears simple, solid-color clothing that doesn't compete with the bag. "
            "The image conveys style, quality, and everyday elegance. "
            "Sharp focus on the bag, slight softness on the model's face."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="bag_08_capacity_show",
        name="容量展示",
        name_en="Capacity Showcase",
        product_type="bags",
        description="打開包包，展示內部空間與可容納物品",
        prompt=(
            "This bag shown open from directly above with everyday essentials neatly organized inside: "
            "smartphone, wallet, keys, sunglasses, water bottle, notebook, earphones, cosmetic pouch. "
            "Top-down flat lay perspective on a clean white surface. "
            "The items should be colorful and clearly identifiable, arranged with intentional spacing. "
            "This demonstrates the bag's generous storage capacity and practical organization. "
            "Bright, even overhead lighting with no harsh shadows. "
            "Each item slightly overlapping the bag edges to show depth."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="bag_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="bags",
        description="展示品牌調性的精緻擺拍，提升品牌感",
        prompt=(
            "This bag styled in an elegant flat lay arrangement with premium lifestyle accessories: "
            "designer sunglasses, a luxury watch, a leather passport holder, and fresh flowers. "
            "Shot on a clean cream or marble surface from directly above. "
            "Cohesive warm color palette, editorial fashion mood board aesthetic. "
            "Soft directional lighting from upper left creating subtle shadows. "
            "The composition conveys premium quality and aspirational lifestyle. "
            "Each object placed with precise intentional spacing following rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ===== Crossbody (斜背包) =====
    SceneTemplate(
        id="bag_cross_01_street",
        name="街拍斜背",
        name_en="Street Crossbody",
        product_type="bags",
        description="模特在街頭斜背包包行走，展示日常穿搭的時尚感",
        prompt=(
            "A stylish model walking confidently down a modern city sidewalk wearing this crossbody bag. "
            "The bag strap goes diagonally across the chest, bag resting on the hip. "
            "Shot from a three-quarter front angle at waist level to showcase the crossbody silhouette. "
            "Urban street background with soft bokeh from storefronts and trees. "
            "Natural daylight with gentle side lighting from the left. "
            "The model wears a casual yet fashionable outfit in neutral tones. "
            "Shot at f/2.8 with a 70mm lens, the bag is the sharpest element in the frame. "
            "Dynamic street style photography with a candid editorial feel."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="crossbody",
        sub_category_name="斜背包",
    ),
    SceneTemplate(
        id="bag_cross_02_strap_detail",
        name="肩帶細節",
        name_en="Strap Detail",
        product_type="bags",
        description="特寫可調式肩帶與五金配件的精緻做工",
        prompt=(
            "Close-up macro photography of this crossbody bag's adjustable strap and hardware details. "
            "Focus on the metal buckle, adjustment slider, lobster clasp, and strap stitching. "
            "Show the strap material texture and the smoothness of the metal finishing. "
            "Shot with a 100mm macro lens at f/4 with shallow depth of field. "
            "Directional side lighting from the right at a low 20-degree angle to reveal surface textures and metallic reflections. "
            "Clean neutral gray background. "
            "The image communicates adjustability, durability, and premium hardware quality. "
            "Professional product detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="crossbody",
        sub_category_name="斜背包",
    ),
    SceneTemplate(
        id="bag_cross_03_phone_access",
        name="隨手取物",
        name_en="Quick Phone Access",
        product_type="bags",
        description="展示斜背包方便取用手機與錢包的實用性",
        prompt=(
            "A person wearing this crossbody bag across their body, one hand reaching into the open bag "
            "pulling out a smartphone, demonstrating easy and quick access while on the go. "
            "The bag flap or zipper is open showing the organized interior with wallet and keys visible inside. "
            "Shot at eye level from a slightly side angle, using a 50mm lens at f/3.5. "
            "Bright, airy indoor environment with soft natural window light. "
            "The person is standing in a casual pose, conveying convenience and practicality. "
            "Focus is sharp on the hand, phone, and bag opening. "
            "Lifestyle photography that communicates everyday functionality."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="crossbody",
        sub_category_name="斜背包",
    ),
    SceneTemplate(
        id="bag_cross_04_outfit_match",
        name="穿搭搭配",
        name_en="Outfit Matching",
        product_type="bags",
        description="展示斜背包搭配三種不同穿搭風格的效果",
        prompt=(
            "A triptych layout showing this crossbody bag styled with three distinct outfits: "
            "1) Casual look with jeans, white t-shirt, and sneakers. "
            "2) Smart casual look with tailored trousers, a button-down shirt, and loafers. "
            "3) Sporty athleisure look with joggers, hoodie, and running shoes. "
            "Each panel shows a model from waist to knees with the crossbody bag prominently displayed. "
            "Clean light gray studio backdrop, consistent soft box lighting at 5500K across all three panels. "
            "Shot at f/5.6 with an 85mm lens for consistent perspective. "
            "The layout demonstrates the bag's versatility across different personal styles."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="crossbody",
        sub_category_name="斜背包",
    ),
    SceneTemplate(
        id="bag_cross_05_travel_light",
        name="輕旅行",
        name_en="Travel Light",
        product_type="bags",
        description="斜背包在旅行或通勤場景中的輕便使用",
        prompt=(
            "A traveler wearing this crossbody bag in a transit setting: standing at a train station platform, "
            "boarding a bus, or walking through an airport terminal. "
            "The bag is worn across the body for hands-free convenience, with a carry-on suitcase nearby. "
            "Shot from a medium distance at a natural eye-level angle. "
            "Bright ambient overhead lighting mixed with natural daylight from large windows. "
            "The scene conveys mobility, lightness, and travel readiness. "
            "Shot at f/4 with a 35mm lens to capture the full scene with context. "
            "The crossbody bag stands out through sharp focus and color contrast against the background."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="crossbody",
        sub_category_name="斜背包",
    ),
    # ===== Backpack (後背包) =====
    SceneTemplate(
        id="bag_bp_01_back_view",
        name="背面展示",
        name_en="Back View",
        product_type="bags",
        description="模特背著後背包的背面照，展示整體背負效果",
        prompt=(
            "A model photographed from behind, wearing this backpack with both straps on. "
            "Full back view from head to mid-thigh showing how the backpack sits on the body. "
            "The straps are properly adjusted, and the backpack fits snugly against the back. "
            "Clean studio backdrop in light gray or beige. "
            "Fashion lighting with a large key softbox directly in front of the model, illuminating the backpack from behind via wraparound, "
            "plus two edge lights creating bright rim highlights on the bag's sides. "
            "Shot at f/5.6 with a 70mm lens at torso height. "
            "The model wears minimal dark clothing to keep focus on the backpack."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="backpack",
        sub_category_name="後背包",
    ),
    SceneTemplate(
        id="bag_bp_02_compartments",
        name="分層展示",
        name_en="Compartment Showcase",
        product_type="bags",
        description="打開後背包展示多層收納空間與隔層設計",
        prompt=(
            "This backpack shown fully opened with all compartments and pockets unzipped and spread out. "
            "The main compartment, front pocket, side pockets, and any hidden compartments are all visible. "
            "Each section contains representative items: laptop in the padded sleeve, books in the main area, "
            "pens and phone in the organizer pocket, water bottle in the side pocket. "
            "Shot from a 45-degree elevated angle on a clean white surface. "
            "Bright overhead lighting with two side fill lights to illuminate every compartment interior. "
            "Shot at f/8 with a 35mm lens to capture the full spread. "
            "The image clearly communicates the backpack's organizational capacity."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="backpack",
        sub_category_name="後背包",
    ),
    SceneTemplate(
        id="bag_bp_03_commute",
        name="通勤場景",
        name_en="Urban Commute",
        product_type="bags",
        description="後背包在城市通勤情境中的使用場景",
        prompt=(
            "A professional person wearing this backpack while walking briskly through a modern urban setting. "
            "The scene shows a clean city sidewalk with glass office buildings in the background. "
            "Morning commute lighting with warm golden sunlight at a low angle creating long shadows. "
            "The model wears business casual attire with the backpack on both shoulders. "
            "Shot from a three-quarter front angle at waist height, showing the backpack's profile. "
            "Use a 50mm lens at f/2.8 for pleasant background bokeh that suggests the urban environment. "
            "The image conveys a polished, productive urban lifestyle. "
            "Dynamic walking pose with confident stride."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="backpack",
        sub_category_name="後背包",
    ),
    SceneTemplate(
        id="bag_bp_04_laptop_fit",
        name="筆電收納",
        name_en="Laptop Fit",
        product_type="bags",
        description="展示筆電放入後背包的收納效果",
        prompt=(
            "A person sliding a 15-inch laptop into the dedicated padded laptop compartment of this backpack. "
            "The backpack is standing upright on a clean desk surface with the laptop sleeve unzipped and open. "
            "The laptop is halfway inserted, showing the protective padding and snug fit. "
            "Shot from a side angle at desk height to clearly show the insertion action. "
            "Bright, even lighting from an overhead softbox with a side fill card. "
            "Shot at f/5.6 with an 85mm lens. "
            "Focus is tack-sharp on the laptop, bag compartment, and the person's hands. "
            "The image clearly demonstrates the backpack's laptop protection capability."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="backpack",
        sub_category_name="後背包",
    ),
    SceneTemplate(
        id="bag_bp_05_outdoor_hike",
        name="戶外健行",
        name_en="Outdoor Hiking",
        product_type="bags",
        description="後背包在戶外健行步道中的使用場景",
        prompt=(
            "A hiker wearing this backpack on a scenic nature trail surrounded by lush green trees and mountain views. "
            "The model is walking along a well-maintained dirt path, photographed from behind at a slight angle. "
            "Natural golden hour sunlight filtering through tree canopy creates dappled light patterns. "
            "The backpack is the sharpest element against the softly blurred natural landscape. "
            "Shot at f/4 with a 70mm lens from a low angle to make the scene feel expansive. "
            "The image conveys adventure, freedom, and the backpack's outdoor durability. "
            "Warm, natural color tones with vibrant greens in the background."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="backpack",
        sub_category_name="後背包",
    ),
    # ===== Handbag (手提包) =====
    SceneTemplate(
        id="bag_hb_01_arm_carry",
        name="手挽展示",
        name_en="Arm Carry",
        product_type="bags",
        description="模特優雅地將手提包挽在手臂上的展示",
        prompt=(
            "An elegantly dressed model carrying this handbag on the crook of her arm in a classic pose. "
            "Shot from waist to knees, focusing on the arm and handbag with the model's body providing context. "
            "Clean, minimalist studio background in soft cream or light gray. "
            "Key light from a large octabox at 45 degrees camera left, with a silver reflector on the opposite side. "
            "The model wears a tailored coat or blazer in a complementary solid color. "
            "Shot at f/3.5 with a 85mm portrait lens. "
            "The handbag's shape, handle, and structure are clearly visible. "
            "The image exudes sophistication and timeless elegance."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="handbag",
        sub_category_name="手提包",
    ),
    SceneTemplate(
        id="bag_hb_02_desk_place",
        name="辦公桌擺放",
        name_en="Office Desk Placement",
        product_type="bags",
        description="手提包放在辦公桌上的商務使用場景",
        prompt=(
            "This handbag placed gracefully on a clean, modern executive office desk. "
            "The bag is positioned on one side of the desk, with a slim laptop, a coffee cup in a ceramic saucer, "
            "and a small potted plant providing workplace context. "
            "Large window with natural daylight from the left side casting soft directional shadows. "
            "The desk surface is light wood or white with minimal clutter. "
            "Shot at a 30-degree elevated angle with a 50mm lens at f/4. "
            "The handbag is the hero item, sharply focused with warm ambient tones. "
            "Professional lifestyle photography conveying a successful work-life aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="handbag",
        sub_category_name="手提包",
    ),
    SceneTemplate(
        id="bag_hb_03_evening",
        name="晚宴場景",
        name_en="Evening Scene",
        product_type="bags",
        description="手提包在優雅晚宴或晚餐場景中的展示",
        prompt=(
            "This handbag in an elegant evening dining setting. "
            "The bag rests on a white linen tablecloth beside a fine dining place setting with crystal glassware and candlelight. "
            "Warm, ambient lighting from candles and soft overhead downlights at a low color temperature of 3200K. "
            "The scene conveys luxury, romance, and sophistication. "
            "Shot at f/2.8 with a 50mm lens from a slightly low angle to elevate the bag's presence. "
            "Shallow depth of field with the glassware and background softly blurred. "
            "Rich warm tones with subtle golden highlights on the bag's hardware. "
            "Evening occasion lifestyle photography for a premium handbag."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="handbag",
        sub_category_name="手提包",
    ),
    SceneTemplate(
        id="bag_hb_04_interior",
        name="內裝展示",
        name_en="Interior Display",
        product_type="bags",
        description="打開手提包展示內部襯裡與口袋設計",
        prompt=(
            "This handbag shown wide open from above, revealing the interior lining, pockets, and organizational features. "
            "The bag is propped open with a support to show maximum internal space. "
            "Interior details are clearly visible: lining fabric pattern, zippered inner pocket, card slots, and key clip. "
            "Shot from directly above at 90 degrees on a clean white surface. "
            "Bright, shadowless lighting from a large overhead diffusion panel with two side fill lights angled inward. "
            "Shot at f/8 with a 50mm lens for edge-to-edge sharpness. "
            "Colors of the interior lining and hardware are accurately rendered. "
            "Professional product photography that communicates craftsmanship and practical design."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="handbag",
        sub_category_name="手提包",
    ),
    SceneTemplate(
        id="bag_hb_05_color_options",
        name="色系展示",
        name_en="Color Options",
        product_type="bags",
        description="多種顏色的手提包一起展示，呈現色系選擇",
        prompt=(
            "Three to four color variants of this handbag displayed together in a curated arrangement. "
            "The bags are positioned in a staggered diagonal line or gentle arc on a clean white surface. "
            "Each bag is at a slightly different angle to show dimensionality. "
            "Consistent, even studio lighting from a large overhead softbox ensures accurate color reproduction across all variants. "
            "Shot at f/8 with a 50mm lens from a 30-degree elevated angle. "
            "Color temperature precisely at 5500K for true-to-life colors. "
            "The composition is balanced and visually appealing, conveying variety and style choices. "
            "Professional product line photography for e-commerce catalog."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="handbag",
        sub_category_name="手提包",
    ),
]

TemplateRegistry.register("bags", BAG_TEMPLATES)
