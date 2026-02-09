from app.templates.registry import SceneTemplate, TemplateRegistry

ELECTRONICS_TEMPLATES = [
    # ===== Common (通用場景) =====
    SceneTemplate(
        id="electronics_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="electronics",
        description="純白背景，產品正面 45 度角展示",
        prompt=(
            "This electronic product on a pure white background at a 3/4 angle. "
            "Professional tech product photography with clean, even lighting. "
            "The product is centered, occupying about 80% of the frame. "
            "Shows LED indicators, buttons, and ports clearly. "
            "Ultra-sharp focus, no reflections on screens. "
            "Shot at f/8 for maximum depth of field across the entire product. "
            "Apple-style clean product photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="electronics",
        description="展示規格、接口、功能等技術賣點",
        prompt=(
            "Create a professional tech product infographic for this electronic device. "
            "Show the product on a dark gradient or clean white background. "
            "Add sleek callout lines pointing to 4-5 key technical features: "
            "processor/chipset, battery capacity, connectivity ports, "
            "special features (waterproof, noise cancelling, fast charging, etc). "
            "Modern tech aesthetic with futuristic typography. "
            "Use rim lighting to separate the product from the background. "
            "Style reference: Apple or Samsung product feature page."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="electronics",
        description="接口、按鍵、螢幕等細節特寫",
        prompt=(
            "Extreme close-up of this electronic product showing build quality details. "
            "Focus on: port/connector quality, button tactile design, "
            "surface finish and material (aluminum, plastic quality), LED indicators. "
            "Macro photography with precise studio lighting. "
            "Shot at f/2.8 with a 100mm macro lens for razor-thin focus plane. "
            "The detail level should convey premium build quality. "
            "Professional tech product macro photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="electronics",
        description="與手機、手掌等常見物品對比大小",
        prompt=(
            "This electronic product placed next to common reference objects for size: "
            "a smartphone, a hand, a coin, or a credit card. "
            "Clean white background, the items arranged to clearly show relative dimensions. "
            "Overhead or slight angle view. "
            "Bright, even lighting for accurate size perception. "
            "Shot from directly above at f/11 to keep all objects tack-sharp. "
            "E-commerce size comparison photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_05_desk_scene",
        name="桌面場景",
        name_en="Desk Setup Scene",
        product_type="electronics",
        description="辦公桌/書桌使用場景",
        prompt=(
            "This electronic product in a clean, modern desk setup. "
            "A minimalist workspace with a laptop, coffee cup, and notebook nearby. "
            "Natural window light mixing with warm desk lamp glow. "
            "The electronic product is the hero item, placed prominently. "
            "Shot at 35mm f/2.8 with shallow depth of field to separate the product from the background. "
            "Tech lifestyle photography with a productive, organized aesthetic. "
            "Clean lines, modern workspace."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_06_usage_scene",
        name="使用場景",
        name_en="Usage Scene",
        product_type="electronics",
        description="實際使用中的場景展示",
        prompt=(
            "A person actively using this electronic product in a natural setting. "
            "The scene clearly demonstrates the product's primary use case. "
            "Natural lighting, lifestyle photography style. "
            "The person's hands and the product are in sharp focus. "
            "Shot at 50mm f/1.8 for cinematic bokeh in the background. "
            "The background provides context but doesn't distract. "
            "Authentic, relatable usage photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_07_multi_angle",
        name="多角度展示",
        name_en="Multi-Angle View",
        product_type="electronics",
        description="正面、背面、側面等多角度展示",
        prompt=(
            "This electronic product shown from 3-4 different angles in a composed layout: "
            "front view, back view, side view, and top/bottom view. "
            "Clean white background, consistent lighting across all angles. "
            "Grid or staggered arrangement showing every design detail. "
            "Each angle lit with matched dual softboxes for consistency. "
            "Professional tech product photography revealing the complete design."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_08_package_contents",
        name="配件全家福",
        name_en="Package Contents",
        product_type="electronics",
        description="展示包裝內所有配件，一覽無遺",
        prompt=(
            "Complete unboxing layout: this electronic product with all included accessories "
            "neatly arranged on a clean white surface. "
            "Show: the main product, charging cable, manual, carrying case/pouch, "
            "and any other included items. "
            "Top-down organized flat lay, each item clearly separated. "
            "Professional 'what's in the box' photography. "
            "Shot overhead at f/8 with even diffused lighting to eliminate shadows. "
            "Bright, even lighting."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="electronics_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="electronics",
        description="科技感生活方式照，展示品牌調性",
        prompt=(
            "This electronic product in a sleek, modern lifestyle setting. "
            "Premium environment: marble desk, designer furniture, or minimalist room. "
            "Dramatic lighting with subtle colored accents (warm amber or cool blue). "
            "The product appears as a premium lifestyle object. "
            "Shot at a low 15-degree angle with a 85mm lens for an editorial perspective. "
            "High-end tech brand campaign aesthetic. "
            "The composition conveys innovation and sophistication."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ===== Earbuds (耳機) =====
    SceneTemplate(
        id="elec_ear_01_case_open",
        name="充電盒展開",
        name_en="Case Open",
        product_type="electronics",
        description="耳機充電盒打開展示耳機的擺放狀態",
        prompt=(
            "This pair of earbuds with the charging case open, showing both earbuds nestled in their compartments. "
            "The case lid is open at a 90-degree angle, revealing the earbuds and LED charging indicators. "
            "Shot from a 30-degree elevated front angle on a clean white or dark gradient surface. "
            "Professional product lighting with a large overhead softbox and a small accent spot from the front "
            "to illuminate the case interior and create subtle reflections on the earbuds. "
            "Shot at f/5.6 with a 90mm macro lens for sharp detail on the earbuds and case. "
            "The image clearly shows the earbuds' shape, the case design, and the magnetic charging alignment. "
            "Premium tech product photography with Apple-inspired clean aesthetics."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="earbuds",
        sub_category_name="耳機",
    ),
    SceneTemplate(
        id="elec_ear_02_wearing",
        name="佩戴展示",
        name_en="Wearing Display",
        product_type="electronics",
        description="模特側面佩戴耳機的展示效果",
        prompt=(
            "A model wearing these earbuds, photographed in side profile from ear level. "
            "Close-up framing from the ear to mid-cheek, showing how the earbud fits in the ear canal. "
            "The earbud is tack-sharp, showing its shape, finish, and how it sits flush or extends from the ear. "
            "Clean, neutral studio background. "
            "Key light from a large softbox at 45 degrees camera right with a subtle rim light from behind for separation. "
            "Shot at f/3.5 with a 100mm macro lens for shallow depth of field isolating the ear and earbud. "
            "Skin tones are natural and warm. "
            "The image demonstrates comfortable, secure fit and the earbud's discreet or stylish appearance when worn."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="earbuds",
        sub_category_name="耳機",
    ),
    SceneTemplate(
        id="elec_ear_03_workout",
        name="運動場景",
        name_en="Workout Scene",
        product_type="electronics",
        description="耳機在運動或跑步時的使用場景",
        prompt=(
            "A person wearing these earbuds during an intense workout: running on a trail, "
            "lifting weights in a gym, or doing yoga in a bright studio. "
            "The earbuds are visible and secure in the ears despite active movement. "
            "A slight sheen of sweat on skin suggests active use. "
            "Shot at a dynamic three-quarter angle at f/2.8 with a 70mm lens. "
            "Natural bright lighting from gym windows or outdoor daylight. "
            "Motion is frozen with a fast 1/500s shutter speed to show the earbuds staying in place during movement. "
            "The image communicates secure fit, sweat resistance, and workout-ready performance. "
            "Active lifestyle tech photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="earbuds",
        sub_category_name="耳機",
    ),
    SceneTemplate(
        id="elec_ear_04_commute",
        name="通勤使用",
        name_en="Commute Scene",
        product_type="electronics",
        description="耳機在通勤或搭乘大眾運輸時的使用場景",
        prompt=(
            "A person wearing these earbuds while commuting: sitting on a modern subway train, "
            "standing at a bus stop, or walking through a train station. "
            "The model has a relaxed, focused expression, enjoying music or a podcast. "
            "The earbuds are clearly visible in the ears, shot from a three-quarter front angle. "
            "Ambient urban transit lighting with warm overhead lights and cool daylight from windows. "
            "Shot at f/2.8 with a 50mm lens for natural perspective and soft background bokeh. "
            "The transit environment provides lifestyle context without overwhelming the product focus. "
            "The image conveys the earbuds' noise isolation capability and daily commute comfort. "
            "Urban tech lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="earbuds",
        sub_category_name="耳機",
    ),
    SceneTemplate(
        id="elec_ear_05_waterproof",
        name="防水展示",
        name_en="Waterproof Display",
        product_type="electronics",
        description="耳機搭配水花飛濺展示防水等級",
        prompt=(
            "These earbuds photographed with dynamic water splashes around them, demonstrating IPX water resistance. "
            "The earbuds are suspended or placed on a dark surface with water droplets splashing upward around them. "
            "High-speed flash photography freezes the water droplets in mid-air at 1/4000s. "
            "Dramatic side lighting from the right with a focused spot creates brilliant highlights on the water drops. "
            "A blue-tinted accent light adds a cool, water-themed atmosphere. "
            "Shot at f/8 with a 100mm macro lens for sharp detail on both the earbuds and frozen water. "
            "The image powerfully communicates water resistance and durability. "
            "Dynamic tech product photography with dramatic water effects."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="earbuds",
        sub_category_name="耳機",
    ),
    # ===== Charger (充電配件) =====
    SceneTemplate(
        id="elec_chg_01_desktop",
        name="桌面充電",
        name_en="Desktop Charging",
        product_type="electronics",
        description="充電器在桌面上為裝置充電的使用場景",
        prompt=(
            "This charger placed on a clean, modern desk with one or two devices actively being charged. "
            "A smartphone and a tablet connected via cables, with their screens showing charging indicators. "
            "The charger is the hero product, positioned prominently in the center-left of frame. "
            "Clean, organized desk with minimal accessories: a notebook, a pen, a small plant. "
            "Natural window light from the left mixed with warm desk lamp glow. "
            "Shot at f/4 with a 35mm lens from a slightly elevated 30-degree angle for full desk context. "
            "The image demonstrates the charger's multi-device capability and clean desk integration. "
            "Tech lifestyle photography with a productive workspace aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="charger",
        sub_category_name="充電配件",
    ),
    SceneTemplate(
        id="elec_chg_02_ports",
        name="接口展示",
        name_en="Port Display",
        product_type="electronics",
        description="充電器所有接口類型的近距離展示",
        prompt=(
            "Close-up shot of this charger's port side, clearly showing all available ports: "
            "USB-C, USB-A, Lightning, or any other connector types. "
            "Each port is well-lit and clearly identifiable by its shape and markings. "
            "The charger is angled to show the port face straight-on. "
            "Shot with a 100mm macro lens at f/5.6 for sharp detail across all ports. "
            "Bright, even lighting from a ring light or dual side softboxes to illuminate the port interiors. "
            "Clean white background. "
            "Labels or subtle indicators near each port for identification. "
            "Professional tech product detail photography for specification communication."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="charger",
        sub_category_name="充電配件",
    ),
    SceneTemplate(
        id="elec_chg_03_travel",
        name="旅行攜帶",
        name_en="Travel Portable",
        product_type="electronics",
        description="充電器在旅行場景中展示便攜性",
        prompt=(
            "This charger packed inside an open travel pouch or organizer bag alongside other travel essentials: "
            "a passport, cables, adapter plugs, and a small notebook. "
            "The compact size of the charger is evident next to these familiar travel items. "
            "Shot from a 45-degree overhead angle on a clean surface with a travel-themed backdrop "
            "(wooden table at an airport lounge or hotel desk). "
            "Warm, ambient overhead lighting with soft natural window light. "
            "Shot at f/5.6 with a 50mm lens. "
            "The image communicates the charger's compact portability and travel-readiness. "
            "Travel tech lifestyle flat lay photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="charger",
        sub_category_name="充電配件",
    ),
    SceneTemplate(
        id="elec_chg_04_fast_charge",
        name="快充展示",
        name_en="Fast Charge Display",
        product_type="electronics",
        description="充電器連接手機展示快速充電效果",
        prompt=(
            "This charger connected to a smartphone via cable, with the phone screen visible showing "
            "a fast charging indicator or battery percentage climbing rapidly. "
            "The charger and phone are placed on a clean white or dark surface. "
            "Shot from a slight side angle at desk height to show both the charger and phone screen clearly. "
            "A subtle glow effect or light trail along the cable suggests energy flow and speed. "
            "Clean studio lighting with a key softbox overhead and a small accent light on the charging indicator. "
            "Shot at f/4 with a 50mm lens. "
            "The image visually communicates fast charging speed and efficient power delivery. "
            "Dynamic tech product photography with energy visualization."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="charger",
        sub_category_name="充電配件",
    ),
    SceneTemplate(
        id="elec_chg_05_comparison",
        name="尺寸對比",
        name_en="Size Comparison",
        product_type="electronics",
        description="充電器與硬幣或信用卡對比展示輕巧體積",
        prompt=(
            "This charger placed next to a standard credit card and a coin for precise size reference. "
            "All items are arranged side by side on a clean white surface with subtle grid lines for scale. "
            "Shot from directly above at 90 degrees with even, bright overhead lighting. "
            "A ruler or centimeter scale is visible along the bottom edge of the frame. "
            "Shot at f/11 with a 50mm lens for maximum sharpness across all objects. "
            "The charger's compact dimensions are immediately apparent compared to the familiar reference items. "
            "Color-accurate lighting at 5500K with no color cast. "
            "Clean, informational product photography emphasizing the charger's compact form factor."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="charger",
        sub_category_name="充電配件",
    ),
    # ===== Case (保護殼) =====
    SceneTemplate(
        id="elec_case_01_on_device",
        name="裝機展示",
        name_en="On Device",
        product_type="electronics",
        description="保護殼安裝在裝置上的完整展示",
        prompt=(
            "This protective case installed on a device (phone/tablet), shown from a three-quarter front angle. "
            "The device screen is visible with a clean wallpaper, and the case wraps around the edges seamlessly. "
            "Shot from a slightly elevated 20-degree angle to show both the case front edge and side profile. "
            "Clean white or light gray background. "
            "Professional product lighting with a large overhead softbox and side fill for even illumination. "
            "Shot at f/5.6 with an 85mm lens. "
            "The image clearly shows the case's precise cutouts for buttons, cameras, and ports. "
            "The fit looks seamless and premium. "
            "Professional tech accessory photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="elec_case_02_drop_test",
        name="防摔展示",
        name_en="Drop Protection",
        product_type="electronics",
        description="保護殼從多角度展示防護效果",
        prompt=(
            "This protective case shown from multiple angles highlighting its protective features. "
            "Display the case from three perspectives: corner protection close-up, raised lip around the screen edge, "
            "and the reinforced back panel. "
            "Arranged in a clean layout on a white background. "
            "Each angle has clear visual emphasis on the protective engineering: thick corners, lip elevation, shock-absorbing material. "
            "Bright, even studio lighting from a large overhead diffusion panel. "
            "Shot at f/8 with a 90mm lens for maximum detail across all views. "
            "The image communicates robust protection capability and engineering quality. "
            "Technical product photography for protective accessories."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="elec_case_03_grip",
        name="手持握感",
        name_en="Hand Grip",
        product_type="electronics",
        description="手持裝置展示保護殼的握感與手感",
        prompt=(
            "A hand naturally gripping a device with this protective case installed. "
            "The hand holds the device in a typical one-handed usage position, showing how the case feels in the palm. "
            "The case's texture, grip pattern, and ergonomic contours are visible along the sides. "
            "Shot from a side angle at hand height with a 85mm lens at f/3.5 for shallow depth of field. "
            "Clean neutral background. "
            "Soft key light from the left with a fill reflector on the right for natural skin tones. "
            "The image demonstrates comfortable grip, slim profile, and tactile case texture. "
            "Lifestyle tech accessory photography emphasizing everyday hand-feel."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="elec_case_04_pattern",
        name="圖案展示",
        name_en="Pattern Display",
        product_type="electronics",
        description="保護殼背面圖案設計的展示",
        prompt=(
            "The back of this protective case displayed face-up, showing the full design, pattern, or artwork. "
            "The case is placed flat on a clean surface with the back panel filling about 80% of the frame. "
            "Shot from directly above at 90 degrees to show the pattern without perspective distortion. "
            "Bright, even lighting from a large overhead diffusion panel at 5500K for accurate color reproduction. "
            "The camera cutout, logo, and every design detail are sharply rendered. "
            "Shot at f/8 with a 50mm lens. "
            "A subtle shadow at the edges gives the case dimensionality against the surface. "
            "Professional product photography showcasing the case's visual design and aesthetic appeal."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="elec_case_05_slim",
        name="超薄展示",
        name_en="Slim Profile",
        product_type="electronics",
        description="保護殼側面展示超薄輪廓",
        prompt=(
            "This protective case shown in side profile on a device, emphasizing its slim, minimal thickness. "
            "The device with case is positioned on its side or held at eye level to show the edge-on profile. "
            "The thin profile of the case is the clear focus, with the screen and back visible in the composition. "
            "Shot at f/4 with a 100mm macro lens from exact side-on level for accurate thickness representation. "
            "A ruler or millimeter reference near the edge for precise thickness visualization. "
            "Clean white background with soft side lighting that accentuates the thin edge line. "
            "A subtle rim light from behind creates definition along the case edge. "
            "Professional tech product photography emphasizing ultra-slim design and minimal added bulk."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="case",
        sub_category_name="保護殼",
    ),
]

TemplateRegistry.register("electronics", ELECTRONICS_TEMPLATES)
