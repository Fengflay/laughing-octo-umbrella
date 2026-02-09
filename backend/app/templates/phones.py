from app.templates.registry import SceneTemplate, TemplateRegistry

PHONES_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="phones_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="phones",
        description="純白背景，手機配件居中，清晰展示產品外觀",
        prompt=(
            "This phone/tablet accessory on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with dual softbox lighting at 45 degrees and overhead fill. "
            "The product is centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding. "
            "Front-facing angle slightly tilted 15 degrees to show depth and design details. "
            "Shot with a 90mm lens at f/8 for full depth of field across the entire product. "
            "Ultra-high resolution, crisp details on material texture, connectors, and branding. "
            "No phone or other objects in frame. Clean tech product photography with accurate colors."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="phones",
        description="展示充電速度、保護等級、相容性等核心賣點",
        prompt=(
            "Create a professional product photography collage for this phone/tablet accessory. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the complete product design and branding. "
            "2) Close-up of the key technical feature: fast-charging chip, tempered glass layers, or shock-absorbing material. "
            "3) Connector or interface detail: USB-C port, Lightning connector, MagSafe alignment, or wireless charging coil. "
            "4) Compatibility showcase: universal fit design, adjustable mechanism, or multi-device support. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "Shot at f/5.6 with a 60mm lens for consistent sharpness. "
            "Modern tech aesthetic matching Apple or Samsung product page styling."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="phones",
        description="微距特寫，展示接口品質、材質紋理、保護結構",
        prompt=(
            "Extreme macro close-up photography of this phone/tablet accessory showing build quality. "
            "Split into 2-3 detail zones: connector or interface precision (gold-plated contacts, reinforced cables), "
            "material surface quality (aramid fiber weave, TPU texture, tempered glass edge), "
            "and structural engineering (air cushion corners, multi-layer protection, heat dissipation design). "
            "Shot with a 100mm macro lens at f/3.5, shallow depth of field with ring light illumination. "
            "The detail level should convey premium tech accessory quality. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional tech product macro photography for e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="phones",
        description="與手機、信用卡等常見物品對比大小",
        prompt=(
            "This phone/tablet accessory photographed next to common reference objects for size comparison: "
            "a standard smartphone (iPhone or similar), a credit card, and a coin. "
            "All items on a clean white surface with a subtle grid pattern for scale reference. "
            "The phone accessory is the central hero element. "
            "If it is a case, show it next to the phone it fits. If a charger or cable, show its compact size. "
            "Clean white background, even studio lighting from above. "
            "Shot from directly above at f/11 with a 50mm lens to keep all objects tack-sharp. "
            "The composition clearly communicates the product's practical size and compatibility."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_05_desk_scene",
        name="桌面場景",
        name_en="Desk Scene",
        product_type="phones",
        description="手機搭配配件在桌面上的使用場景",
        prompt=(
            "This phone accessory in use on a clean, modern desk setup. "
            "A smartphone with the accessory attached or nearby, alongside a laptop, wireless earbuds, and a coffee cup. "
            "Minimalist workspace with warm natural window light from the left mixing with cool monitor glow. "
            "The phone accessory is the hero item, prominently placed and in sharp focus. "
            "Shot at 35mm f/2.8 with shallow depth of field creating soft bokeh on the background. "
            "Camera angle slightly above at 25 degrees, conveying a productive tech-savvy workspace. "
            "Modern tech lifestyle photography with clean lines and organized aesthetic. "
            "Warm color tones around 5600K."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_06_charging_scene",
        name="充電場景",
        name_en="Charging Scene",
        product_type="phones",
        description="產品正在為手機充電或連接使用的場景",
        prompt=(
            "This phone accessory actively in use: charging a smartphone or connected to a device. "
            "A bedside table or desk at night with the phone's screen softly glowing while charging. "
            "Warm ambient lighting from a bedside lamp creating a cozy nighttime atmosphere. "
            "The charging indicator light (if applicable) visible and glowing. "
            "Shot at 50mm f/2.0 for cinematic shallow depth of field and warm bokeh. "
            "Camera at a natural eye-level perspective from the side. "
            "The scene conveys convenience, reliable power, and seamless integration into daily life. "
            "Lifestyle tech photography with warm, intimate evening tones."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_07_hand_holding",
        name="手持展示",
        name_en="Hand Holding",
        product_type="phones",
        description="手持手機搭配配件的實際使用展示",
        prompt=(
            "A person's hand naturally holding a smartphone equipped with this phone accessory. "
            "The grip is natural and comfortable, showing the product's ergonomic fit. "
            "If a case, show how it feels in hand; if a grip or stand, show it deployed and in use. "
            "Clean neutral background (light gray or soft white studio backdrop). "
            "Professional lighting: key light at 45 degrees from upper right with soft fill from the left. "
            "Shot at 85mm f/2.0 for beautiful background separation with sharp focus on the hand and product. "
            "Camera at a slight upward angle to show the phone screen and accessory together. "
            "The image conveys comfort, style, and practical everyday usability."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_08_accessory_bundle",
        name="配件全家福",
        name_en="Accessory Bundle",
        product_type="phones",
        description="手機配件的平鋪組合展示",
        prompt=(
            "This phone accessory shown in a curated flat lay arrangement with complementary tech items: "
            "a charging cable, wireless earbuds case, a screen protector, a phone stand, and a cable organizer. "
            "Top-down overhead perspective on a clean white or light gray surface. "
            "Items arranged with intentional spacing in a clean geometric grid pattern. "
            "The hero product is centrally positioned and visually prominent. "
            "Shot directly overhead at f/7.1 with even diffused softbox lighting from above. "
            "Modern, minimalist tech aesthetic with monochrome and accent color coordination. "
            "Professional tech accessory flat lay photography conveying a complete mobile setup."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="phones_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="phones",
        description="展示手機配件品牌科技感與生活調性",
        prompt=(
            "This phone accessory styled in a sleek, modern lifestyle arrangement. "
            "The product placed on a clean marble or dark slate surface alongside designer sunglasses, "
            "a premium watch, a minimalist wallet, and a small succulent plant. "
            "Shot from directly above on a sophisticated surface. "
            "Cohesive modern color palette with subtle metallic accents, editorial tech lifestyle mood. "
            "Dramatic directional lighting from upper left creating sophisticated shadows. "
            "Shot at f/3.5 with a 50mm lens for natural perspective. "
            "The composition conveys modern innovation, premium quality, and curated lifestyle. "
            "Each object placed with precise intentional spacing following rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== phone_case (保護殼) ====================
    SceneTemplate(
        id="phone_case_01_on_phone",
        name="裝機展示",
        name_en="Case on Phone",
        product_type="phones",
        description="保護殼安裝在手機上的多角度展示",
        prompt=(
            "This phone case installed on a smartphone, displayed from three angles: front three-quarter view showing the case edge and screen, "
            "back view revealing the full case design and camera cutout alignment, and side profile showing the slim fit and button covers. "
            "All three views arranged cleanly on a white background with consistent spacing. "
            "Shot at 60mm f/6.3 with even studio lighting at 5500K ensuring accurate color reproduction of the case material. "
            "Each angle is sharply focused with subtle shadows grounding the phone on the white surface. "
            "The multi-angle composition gives buyers a complete understanding of the case's design, fit, and coverage from every perspective."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="phone_case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="phone_case_02_drop",
        name="防摔設計",
        name_en="Drop Protection Design",
        product_type="phones",
        description="展示保護殼的防摔與角落保護設計",
        prompt=(
            "A close-up of this phone case's corner and edge protection system, showing the reinforced air-cushion corners and raised lip around the screen. "
            "The case is photographed at a dramatic low angle emphasizing the corner thickness and shock-absorbing material layers. "
            "A cross-section view or cutaway reveals the multi-layer internal structure: hard polycarbonate shell over soft TPU inner. "
            "Shot at 100mm macro f/4.0 with ring light illumination highlighting the engineering details of the protection system. "
            "Clean white background isolates the case corner for maximum clarity on the protective features. "
            "The technical close-up builds buyer confidence in the case's ability to protect their expensive device from drops and impacts."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="phone_case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="phone_case_03_grip",
        name="手持展示",
        name_en="Grip Demonstration",
        product_type="phones",
        description="手持裝有保護殼的手機展示握持手感",
        prompt=(
            "A person's hand comfortably gripping a smartphone with this case installed, demonstrating the ergonomic hold and textured grip surface. "
            "The hand position is natural, with fingers wrapped around the case edges and thumb resting on the screen. "
            "The case's grip texture, side button accessibility, and slim profile are all clearly visible. "
            "Shot at 85mm f/2.4 from a slight side angle, sharp focus on the hand and case with a soft neutral gray background. "
            "Professional lighting: key light at 45 degrees from the right, soft fill from the left to show the case's surface texture. "
            "The image communicates comfortable daily use, secure grip, and the case's ability to enhance rather than hinder phone handling."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="phone_case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="phone_case_04_collection",
        name="系列色彩",
        name_en="Color Collection",
        product_type="phones",
        description="多款顏色保護殼的排列展示",
        prompt=(
            "Multiple color variants of this phone case arranged in a visually striking fan or grid pattern on a clean white surface. "
            "Five to eight cases in different colors are spread out, each showing its back design with consistent angle and spacing. "
            "The colors progress in a pleasing gradient: from light pastels through vibrant hues to deep dark tones. "
            "Shot directly overhead at f/8 with a 50mm lens and perfectly even dual-softbox lighting for accurate color reproduction. "
            "Each case casts a minimal, consistent shadow ensuring the colors appear true-to-life and unaffected by lighting bias. "
            "The collection display helps buyers compare colors at a glance and encourages purchase of multiple variants."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="phone_case",
        sub_category_name="保護殼",
    ),
    SceneTemplate(
        id="phone_case_05_slim_profile",
        name="超薄側面",
        name_en="Slim Side Profile",
        product_type="phones",
        description="保護殼側面展示超薄設計與按鍵覆蓋",
        prompt=(
            "This phone case on a smartphone photographed from a direct side profile, emphasizing its ultra-slim thickness and precise button covers. "
            "The case is stood upright on its bottom edge, showing the minimal added bulk compared to the phone itself. "
            "Volume buttons and power button covers are clearly visible and precisely aligned with the phone's hardware buttons. "
            "Shot at 90mm f/5.6 from exactly 90 degrees to the phone's side, on a clean white background with subtle gradient. "
            "Professional side lighting creates a thin highlight line along the case edge, accentuating its sleek profile. "
            "The composition proves the case adds protection without sacrificing the phone's slim, pocketable form factor."
        ),
        aspect_ratio="3:4",
        injection_level="light",
        sub_category="phone_case",
        sub_category_name="保護殼",
    ),
    # ==================== phone_charger (充電器) ====================
    SceneTemplate(
        id="phone_chg_01_charging",
        name="充電場景",
        name_en="Charging in Action",
        product_type="phones",
        description="充電器正在為設備充電的桌面場景",
        prompt=(
            "This phone charger actively powering a smartphone on a clean modern desk or bedside table. "
            "The phone screen displays a charging animation or battery percentage, confirming active power delivery. "
            "The charger is connected via its cable with the LED indicator glowing green or blue. "
            "Shot at 50mm f/2.8 from a 25-degree angle, the charger and phone in sharp focus against a softly blurred room background. "
            "Warm ambient lighting from a desk lamp creates a comfortable evening productivity or bedtime charging atmosphere. "
            "The lifestyle composition demonstrates seamless everyday charging integration and reliable power delivery."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_charger",
        sub_category_name="充電器",
    ),
    SceneTemplate(
        id="phone_chg_02_ports",
        name="多口展示",
        name_en="Multi-Port Display",
        product_type="phones",
        description="展示充電器的多種接口與輸出規格",
        prompt=(
            "A close-up of this charger's port panel showing all available outputs: USB-C, USB-A, and wireless charging surface. "
            "Each port is labeled with its wattage output or charging standard (PD, QC, PPS) in the image context. "
            "Multiple cables of different types are partially inserted into the ports, demonstrating multi-device capability. "
            "Shot at 100mm macro f/4.5 with ring light illumination ensuring the port interiors and labeling are clearly visible. "
            "Clean white background with the charger angled slightly to show the port panel as the primary focal point. "
            "The technical close-up helps buyers quickly understand the charger's versatility and compatibility with their device ecosystem."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="phone_charger",
        sub_category_name="充電器",
    ),
    SceneTemplate(
        id="phone_chg_03_travel",
        name="旅行攜帶",
        name_en="Travel Portable",
        product_type="phones",
        description="充電器放在旅行包或收納袋中的攜帶展示",
        prompt=(
            "This compact phone charger tucked into a travel pouch or organizer alongside cables, earbuds, and a passport. "
            "The charger's small size is evident compared to the other travel essentials surrounding it. "
            "The organizer is partially unzipped on a clean surface, ready for packing into a carry-on bag visible in the background. "
            "Shot at 40mm f/3.5 from a 35-degree angle, the charger in sharp focus as the hero item within the travel kit. "
            "Bright, even lighting at 5500K ensures the charger's compact dimensions are accurately represented. "
            "The travel context positions the charger as an essential, space-efficient companion for mobile professionals and travelers."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_charger",
        sub_category_name="充電器",
    ),
    SceneTemplate(
        id="phone_chg_04_speed",
        name="快充效果",
        name_en="Fast Charge Indicator",
        product_type="phones",
        description="展示快速充電效果與電量指示",
        prompt=(
            "A smartphone connected to this fast charger, with the phone screen displaying a rapid charging animation and rising battery percentage. "
            "The charger's fast-charge LED indicator is glowing prominently, and the cable connection point is clearly visible. "
            "A subtle motion blur or energy glow effect around the charging cable suggests high-speed power transfer. "
            "Shot at 60mm f/2.8 from a slight side angle on a dark surface, creating a dramatic tech atmosphere. "
            "Cool-toned lighting with blue accent highlights emphasizes the high-tech fast-charging capability. "
            "The image visually communicates speed and efficiency, making the charger's performance advantage immediately apparent to buyers."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_charger",
        sub_category_name="充電器",
    ),
    SceneTemplate(
        id="phone_chg_05_size",
        name="尺寸比較",
        name_en="Size Comparison",
        product_type="phones",
        description="充電器與信用卡或硬幣的尺寸對比",
        prompt=(
            "This phone charger photographed next to a standard credit card and a coin to demonstrate its remarkably compact size. "
            "All three items are arranged on a clean white surface with a subtle centimeter grid for precise scale reference. "
            "The charger is positioned between the card and coin, making its small footprint immediately obvious. "
            "Shot from directly above at f/9 with a 50mm lens, all objects tack-sharp with even diffused studio lighting. "
            "No shadows or perspective distortion to ensure the size comparison is fair and accurate. "
            "The composition is designed to impress buyers with the charger's miniaturized design despite its high power output."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="phone_charger",
        sub_category_name="充電器",
    ),
    # ==================== phone_mount (支架) ====================
    SceneTemplate(
        id="phone_mount_01_desk",
        name="桌面使用",
        name_en="Desk Stand in Use",
        product_type="phones",
        description="手機支架放在辦公桌上的使用場景",
        prompt=(
            "This phone mount/stand holding a smartphone upright on a clean modern office desk, positioned beside a laptop and a coffee mug. "
            "The phone screen is clearly visible and angled at an optimal viewing angle for the seated user. "
            "The stand's base sits securely on the desk surface with its adjustment mechanism clearly visible. "
            "Shot at 35mm f/2.8 from a seated eye-level perspective, the phone and stand in sharp focus against a softly blurred office background. "
            "Warm natural window light from the left mixed with cool monitor glow creates a productive workspace ambiance. "
            "The composition demonstrates the stand's practical utility for hands-free phone viewing during work hours."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_mount",
        sub_category_name="支架",
    ),
    SceneTemplate(
        id="phone_mount_02_car",
        name="車用場景",
        name_en="Car Mount Scene",
        product_type="phones",
        description="手機支架安裝在車內的使用場景",
        prompt=(
            "This phone mount installed on a car dashboard or air vent, securely holding a smartphone displaying a navigation map. "
            "The car interior is modern with leather steering wheel and clean dashboard visible around the mount. "
            "Through the windshield, a blurred road ahead is visible, establishing the driving context. "
            "Shot at 24mm f/3.5 wide-angle from the driver's perspective showing the mount in its natural use position. "
            "Bright natural daylight through the windshield provides even illumination without glare on the phone screen. "
            "The image proves the mount is securely positioned, easily visible, and does not obstruct the driver's view."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_mount",
        sub_category_name="支架",
    ),
    SceneTemplate(
        id="phone_mount_03_adjustable",
        name="角度調整",
        name_en="Adjustable Angles",
        product_type="phones",
        description="展示支架的多角度調節功能",
        prompt=(
            "Three instances of this phone mount shown side by side, each adjusted to a different angle: portrait mode tilted back, landscape mode for video, and flat for typing. "
            "Each position holds a smartphone securely, demonstrating the mount's flexible joint or hinge mechanism. "
            "The three positions are arranged on a clean white background with consistent spacing and even lighting. "
            "Shot at 50mm f/7.1 from a slight 15-degree elevated angle ensuring all three positions are equally sharp. "
            "Dual softbox lighting at 5500K provides shadow-free illumination across all three configurations. "
            "The triple-view composition clearly communicates the stand's versatile adjustability for different use scenarios."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="phone_mount",
        sub_category_name="支架",
    ),
    SceneTemplate(
        id="phone_mount_04_video",
        name="視頻通話",
        name_en="Video Call Scene",
        product_type="phones",
        description="手機支架用於視頻通話的使用場景",
        prompt=(
            "This phone mount holding a smartphone at the perfect eye-level angle for a video call, with a person visible on the phone screen. "
            "The setup is on a home office desk with a ring light reflected in the phone screen and a tidy bookshelf behind. "
            "The mount positions the phone at face height, demonstrating hands-free video calling convenience. "
            "Shot at 40mm f/2.8 from a slight side angle showing both the phone screen content and the mount's stable base. "
            "Bright, professional lighting simulating a video call setup at home with warm ambient tones. "
            "The scene positions the mount as essential for remote workers, content creators, and anyone who video calls regularly."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_mount",
        sub_category_name="支架",
    ),
    SceneTemplate(
        id="phone_mount_05_kitchen",
        name="廚房食譜",
        name_en="Kitchen Recipe Stand",
        product_type="phones",
        description="手機支架在廚房中顯示食譜的使用場景",
        prompt=(
            "This phone mount on a kitchen countertop holding a smartphone that displays a cooking recipe, surrounded by fresh ingredients and cooking utensils. "
            "Chopped vegetables, a wooden cutting board, olive oil bottle, and herbs are arranged naturally around the stand. "
            "The phone screen shows a recipe with clear text, proving the mount keeps the phone at a readable angle while cooking. "
            "Shot at 35mm f/3.2 from a natural standing angle in the kitchen, the phone and mount in sharp focus. "
            "Bright kitchen overhead lighting mixed with warm window light creates an appetizing culinary atmosphere. "
            "The composition demonstrates a practical everyday use case: hands-free recipe following while cooking a meal."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="phone_mount",
        sub_category_name="支架",
    ),
]

TemplateRegistry.register("phones", PHONES_TEMPLATES)
