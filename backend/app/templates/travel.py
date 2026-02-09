from app.templates.registry import SceneTemplate, TemplateRegistry

TRAVEL_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="travel_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="travel",
        description="純白背景，旅行用品居中，清晰展示產品外觀",
        prompt=(
            "This travel/luggage product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with soft box lighting from above at 45 degrees and two side fill lights. "
            "The product is centered, occupying about 85% of the frame. "
            "Slight natural shadow beneath the product for depth and grounding. "
            "Front-facing angle slightly tilted 20 degrees to show depth, dimension, and construction. "
            "Shot with a 85mm lens at f/9 for maximum depth of field across the entire product. "
            "Ultra-high resolution, crisp details on zippers, wheels, handles, and material texture. "
            "No other objects in frame. Color accuracy is critical."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="travel",
        description="展示輪子、拉桿、材質、鎖具等核心賣點",
        prompt=(
            "Create a professional product photography collage for this travel/luggage product. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the full product design, branding, and overall silhouette. "
            "2) Close-up of the wheel system: 360-degree spinner wheels or rugged terrain wheels. "
            "3) Handle and lock mechanism: telescoping handle, TSA-approved lock, or grip comfort. "
            "4) Material durability: scratch-resistant polycarbonate shell, water-resistant fabric, or reinforced corners. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "Shot at f/6.3 with a 60mm lens for uniform clarity. "
            "The layout conveys durability, smart design, and travel readiness."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="travel",
        description="微距特寫，展示拉鍊品質、輪子結構、材質紋理",
        prompt=(
            "Extreme macro close-up photography of this travel/luggage product showing build quality details. "
            "Split into 2-3 detail zones: zipper teeth and pull tab precision (YKK or equivalent quality), "
            "wheel bearing and housing construction showing smooth rotation capability, "
            "and shell or fabric material texture showing scratch resistance and durability. "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The texture should convey travel-grade ruggedness and premium craftsmanship. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional luggage product macro photography for e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="travel",
        description="與人體、登機規格等對比，直觀展示大小",
        prompt=(
            "This travel/luggage product photographed next to common reference objects for size comparison: "
            "a standing person's silhouette or legs, a standard carry-on size reference frame, and a laptop bag. "
            "All items on a clean white surface with a subtle grid pattern for scale reference. "
            "The travel product is the central hero element. "
            "If a suitcase, show it standing upright with the handle extended. "
            "Clean white background, even studio lighting from above. "
            "Shot straight-on at f/11 with a 50mm lens to keep all objects tack-sharp. "
            "The composition clearly communicates the product's size relative to airline carry-on standards. "
            "Items proportionally realistic to each other."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_05_airport_scene",
        name="機場場景",
        name_en="Airport Scene",
        product_type="travel",
        description="行李箱在機場或飯店大廳的使用場景",
        prompt=(
            "This travel/luggage product in a bright, modern airport terminal or luxury hotel lobby. "
            "The luggage is standing upright on polished floors with the handle extended, ready for travel. "
            "Blurred departure boards, large windows, or elegant lobby architecture in the background. "
            "Bright, even ambient lighting with natural daylight streaming through large glass panels. "
            "Shot at 35mm f/2.8 with shallow depth of field, the luggage sharp against the dreamy bokeh background. "
            "Camera at a low 20-degree angle to make the luggage look impressive and substantial. "
            "The scene conveys travel excitement, sophistication, and reliability. "
            "Aspirational travel lifestyle photography with clean, modern tones."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_06_travel_scene",
        name="旅行場景",
        name_en="Travel Scene",
        product_type="travel",
        description="產品在旅行途中的實際使用情境",
        prompt=(
            "This travel/luggage product in an authentic travel context. "
            "The product placed in a charming cobblestone street, a train platform, or a scenic hotel balcony. "
            "Natural surroundings suggesting an exciting travel destination. "
            "Golden hour natural lighting creating warm, adventurous tones and gentle shadows. "
            "Shot at 40mm f/2.4 with the background softly blurred to emphasize the product. "
            "Camera at eye level for a natural traveler's perspective. "
            "The luggage is the hero subject, sharply focused against the scenic bokeh background. "
            "Aspirational wanderlust travel photography with warm, inviting colors."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_07_packing_demo",
        name="收納展示",
        name_en="Packing Demo",
        product_type="travel",
        description="展示內部收納空間與打包組織效果",
        prompt=(
            "This travel/luggage product shown open from a slightly elevated angle revealing its interior organization. "
            "Neatly packed with folded clothing, packing cubes, toiletry bags, and travel accessories. "
            "The interior compartments, dividers, and mesh pockets are clearly visible and well-utilized. "
            "Clean, bright lighting ensuring every interior detail is visible. "
            "Professional lighting: two softboxes at 45 degrees from above with a reflector below to fill shadows inside. "
            "Shot at 50mm f/5.6 for good depth of field showing both the interior and exterior. "
            "Camera at a 45-degree elevated angle looking down into the open luggage. "
            "The image conveys smart packing, generous capacity, and thoughtful organization design."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_08_travel_bundle",
        name="旅行組合",
        name_en="Travel Bundle",
        product_type="travel",
        description="旅行必備用品的平鋪組合展示",
        prompt=(
            "This travel product shown in a curated flat lay arrangement with essential travel items: "
            "a passport and passport holder, a neck pillow, sunglasses, a travel-size toiletry set, "
            "a luggage tag, and a travel adapter plug. "
            "Top-down overhead perspective on a clean white or light canvas surface. "
            "Items arranged with intentional spacing in a balanced, pleasing composition. "
            "The hero product is centrally positioned and visually prominent. "
            "Shot directly overhead at f/7.1 with even diffused softbox lighting from above. "
            "Bright, organized aesthetic that conveys travel readiness and completeness. "
            "Professional travel product flat lay photography with cohesive earth-tone palette."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="travel_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="travel",
        description="展示旅行品牌探索精神與品質調性",
        prompt=(
            "This travel/luggage product styled in an aspirational lifestyle arrangement. "
            "The product placed on a vintage world map or weathered wood surface alongside "
            "a leather-bound journal, a vintage compass, a straw hat, and a film camera. "
            "Shot from directly above on a textured, storied surface. "
            "Cohesive warm adventure color palette with browns, tans, and muted greens. "
            "Soft directional lighting from upper left creating evocative shadows. "
            "Shot at f/3.5 with a 50mm lens for natural perspective. "
            "The composition conveys wanderlust, exploration, and premium travel quality. "
            "Each object placed with precise intentional spacing following rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== luggage (行李箱) ====================
    SceneTemplate(
        id="travel_lug_01_packed",
        name="打包展示",
        name_en="Packed Suitcase",
        product_type="travel",
        description="行李箱打開展示整齊打包的內部空間",
        prompt=(
            "This suitcase opened flat on a bed or clean floor, revealing a perfectly organized interior with neatly folded clothing, packing cubes in coordinating colors, and toiletry bags secured in mesh pockets. "
            "One side shows the main compartment with compression straps holding clothes flat, the other side reveals zippered dividers and accessory pockets. "
            "Shot from a 50-degree elevated angle at 35mm f/4.5 to capture the full interior layout in a single frame. "
            "Bright, even lighting from two overhead softboxes ensures every compartment and pocket is clearly visible without shadows. "
            "The clothing and accessories are color-coordinated for visual appeal, suggesting an organized traveler's curated wardrobe. "
            "The composition proves the suitcase's generous capacity and smart interior organization system."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="luggage",
        sub_category_name="行李箱",
    ),
    SceneTemplate(
        id="travel_lug_02_airport",
        name="機場場景",
        name_en="Airport Terminal",
        product_type="travel",
        description="行李箱在機場航站樓的旅行場景",
        prompt=(
            "This suitcase standing upright with its telescoping handle fully extended in a bright, modern airport terminal. "
            "The polished terrazzo floor reflects the suitcase's silhouette, and large floor-to-ceiling windows reveal aircraft on the tarmac behind. "
            "A departure information board is softly blurred in the background, evoking the excitement of imminent travel. "
            "Shot at 50mm f/2.8 from a low 15-degree angle, making the suitcase appear tall and impressive against the grand terminal architecture. "
            "Bright natural daylight flooding through the terminal windows provides clean, even illumination. "
            "The aspirational airport scene connects the suitcase to the thrill of travel and positions it as a premium, reliable companion."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="luggage",
        sub_category_name="行李箱",
    ),
    SceneTemplate(
        id="travel_lug_03_wheels",
        name="滾輪特寫",
        name_en="Wheel Close-up",
        product_type="travel",
        description="行李箱滾輪與拉桿的細節特寫",
        prompt=(
            "An extreme close-up of this suitcase's wheel assembly and telescoping handle mechanism, showing the engineering quality. "
            "The 360-degree spinner wheel is captured mid-rotation with its smooth bearing and rubber tread visible in sharp macro detail. "
            "The telescoping handle's locking button, aluminum tubing, and ergonomic grip are shown in a secondary detail zone. "
            "Shot at 100mm macro f/4.0 with focus stacking, ring light illumination highlighting the metallic finish and mechanical precision. "
            "Clean white background isolates the wheel and handle components for maximum clarity. "
            "The technical macro photography builds buyer confidence in the luggage's rolling performance and handle durability."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="luggage",
        sub_category_name="行李箱",
    ),
    SceneTemplate(
        id="travel_lug_04_stack",
        name="套裝展示",
        name_en="Nested Luggage Set",
        product_type="travel",
        description="多件行李箱的套裝組合展示",
        prompt=(
            "A complete luggage set of three sizes (carry-on, medium, and large) arranged in a staggered diagonal line from smallest to largest. "
            "Each suitcase stands upright with its handle extended to a different height, showing the graduated sizing. "
            "The smallest case is positioned slightly in front, creating visual depth and emphasizing the nesting capability. "
            "Shot at 50mm f/5.6 from a 20-degree angle on a clean white background with soft gradient. "
            "Even studio lighting from both sides ensures consistent color and finish across all three cases. "
            "The set composition helps buyers visualize the complete travel system and encourages purchasing the full set rather than individual pieces."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="luggage",
        sub_category_name="行李箱",
    ),
    SceneTemplate(
        id="travel_lug_05_durability",
        name="耐用展示",
        name_en="Durability Showcase",
        product_type="travel",
        description="展示行李箱材質強度與角落保護設計",
        prompt=(
            "A close-up showcasing this suitcase's durability features: reinforced corner guards, scratch-resistant shell material, and heavy-duty zipper track. "
            "The corner protector is photographed showing its thickness and impact-absorbing design. "
            "The shell surface displays its texture up close, with a subtle scratch test area showing resistance. "
            "Shot at 85mm f/4.5 from multiple tight angles combined into a 2-3 zone detail layout on a white background. "
            "Professional studio lighting with ring light for the macro zones and dual softboxes for the overall shell texture. "
            "The technical showcase reassures buyers that this luggage withstands the rigors of airline baggage handling and frequent travel."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="luggage",
        sub_category_name="行李箱",
    ),
    # ==================== travel_acc (旅行配件) ====================
    SceneTemplate(
        id="travel_acc_01_packing",
        name="收納分裝",
        name_en="Packing Organization",
        product_type="travel",
        description="收納袋或分裝瓶在行李箱內的使用展示",
        prompt=(
            "This travel accessory (packing cubes, compression bags, or toiletry bottles) arranged inside an open suitcase, demonstrating organized packing. "
            "The cubes or bags are color-coded and labeled, each containing different categories: clothes, electronics, toiletries. "
            "The suitcase interior is neat and maximally utilized, proving the accessories enable efficient space management. "
            "Shot from a 45-degree overhead angle at 35mm f/4.0, capturing the full open suitcase with accessories in context. "
            "Bright, even lighting from above ensures every compartment and label is clearly visible inside the suitcase. "
            "The composition demonstrates how these accessories transform chaotic packing into an organized, stress-free system."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="travel_acc",
        sub_category_name="旅行配件",
    ),
    SceneTemplate(
        id="travel_acc_02_airplane",
        name="機上使用",
        name_en="In-Flight Use",
        product_type="travel",
        description="旅行枕或眼罩在飛機上的使用展示",
        prompt=(
            "This travel comfort accessory (neck pillow, eye mask, or blanket) being used by a relaxed traveler in an airplane seat. "
            "The person is comfortably reclined with the product in use, eyes closed in peaceful rest. "
            "The airplane window with a cloud view, overhead reading light, and armrest are visible for context. "
            "Shot at 50mm f/2.8 from the adjacent seat perspective, the traveler and product in sharp focus with the cabin softly blurred. "
            "Warm cabin lighting with the window providing a soft natural glow creates a tranquil in-flight atmosphere. "
            "The scene demonstrates real in-flight comfort and positions the accessory as essential for long-haul travelers."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="travel_acc",
        sub_category_name="旅行配件",
    ),
    SceneTemplate(
        id="travel_acc_03_hotel",
        name="飯店場景",
        name_en="Hotel Room Scene",
        product_type="travel",
        description="旅行配件在飯店房間中的使用場景",
        prompt=(
            "This travel accessory displayed in a clean, modern hotel room: on the vanity counter, bedside table, or bathroom shelf. "
            "The hotel environment includes crisp white bedding, a reading lamp, and a window with city skyline visible. "
            "The travel accessory is unpacked and in its natural use position as if the traveler just arrived. "
            "Shot at 35mm f/3.2 from a natural standing perspective in the hotel room, the accessory in sharp focus. "
            "Warm hotel room lighting from bedside lamps mixed with cool daylight from the window. "
            "The lifestyle scene connects the accessory to the premium hotel travel experience, appealing to frequent travelers."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="travel_acc",
        sub_category_name="旅行配件",
    ),
    SceneTemplate(
        id="travel_acc_04_organizer",
        name="證件收納",
        name_en="Document Organizer",
        product_type="travel",
        description="護照夾或證件收納展示內部功能",
        prompt=(
            "This travel document organizer (passport holder, RFID wallet, or travel wallet) opened to reveal its interior compartments. "
            "A passport, boarding pass, credit cards, and foreign currency bills are neatly organized in their designated slots. "
            "The organizer is held open at a natural angle on a clean surface, showing both the exterior design and interior capacity. "
            "Shot at 60mm f/4.0 from a 30-degree angle, both the exterior and interior in sharp focus. "
            "Even studio lighting at 5500K ensures the leather or fabric texture and interior organization are clearly visible. "
            "The composition helps buyers understand exactly how many documents and cards the organizer accommodates."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="travel_acc",
        sub_category_name="旅行配件",
    ),
    SceneTemplate(
        id="travel_acc_05_essentials",
        name="必備清單",
        name_en="Travel Essentials Flat Lay",
        product_type="travel",
        description="旅行必備物品的完整平鋪展示",
        prompt=(
            "A comprehensive flat lay of travel essentials centered around this hero travel accessory: passport, sunglasses, earbuds, travel adapter, "
            "mini toiletries, a phone charger, a luggage tag, snacks, and a small notebook with pen. "
            "All items arranged in a balanced grid pattern on a clean white or natural linen surface from directly overhead. "
            "The hero travel accessory is positioned in the center, slightly larger or elevated on a subtle platform. "
            "Shot at f/7.1 with a 50mm lens, even diffused lighting from two overhead softboxes for shadow-free coverage. "
            "The curated arrangement communicates preparedness and helps buyers visualize a complete travel packing list. "
            "Cohesive warm earth-tone palette with natural textures conveying adventure readiness."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="travel_acc",
        sub_category_name="旅行配件",
    ),
    # ==================== travel_bag (旅行包) ====================
    SceneTemplate(
        id="travel_bag_01_carry_on",
        name="登機手提",
        name_en="Carry-On at Gate",
        product_type="travel",
        description="旅行包作為登機手提在登機門的場景",
        prompt=(
            "This travel bag placed on a seat at an airport boarding gate, positioned as a carry-on ready for boarding. "
            "The gate area has large windows showing an aircraft at the jet bridge, with seat rows and other travelers softly blurred behind. "
            "The bag's size clearly fits within carry-on dimensions, with its handles and straps neatly arranged. "
            "Shot at 40mm f/2.8 from a seated perspective, the bag in sharp focus against the airy gate area bokeh. "
            "Bright terminal lighting with natural daylight through the floor-to-ceiling windows creates an optimistic travel mood. "
            "The composition positions the bag as the perfect carry-on companion, sized right and stylish enough for gate-side display."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="travel_bag",
        sub_category_name="旅行包",
    ),
    SceneTemplate(
        id="travel_bag_02_gym_dual",
        name="健身兩用",
        name_en="Gym Travel Dual Use",
        product_type="travel",
        description="旅行包兼作健身包的多功能展示",
        prompt=(
            "This travel bag shown in a dual-use context: one half of the image shows it packed with gym gear (water bottle, towel, sneakers peeking out), "
            "the other half shows the same bag packed for a weekend trip (rolled clothes, toiletry pouch, book). "
            "The bag sits on a clean gym bench or modern entryway console, demonstrating its versatile capacity. "
            "Shot at 40mm f/3.5 from a slight 25-degree angle, the bag and its contents in sharp focus. "
            "Bright, energetic lighting at 5500K conveys an active, on-the-go lifestyle. "
            "The composition communicates versatility: one bag that handles both daily fitness and weekend travel, maximizing value for the buyer."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="travel_bag",
        sub_category_name="旅行包",
    ),
    SceneTemplate(
        id="travel_bag_03_capacity",
        name="容量展示",
        name_en="Capacity Interior View",
        product_type="travel",
        description="旅行包打開展示內部空間與收納設計",
        prompt=(
            "This travel bag fully unzipped and opened wide, revealing its spacious interior with all compartments, pockets, and organizer sections visible. "
            "The main compartment holds folded clothes and a laptop sleeve is shown with a device partially inserted. "
            "Side pockets contain a water bottle and umbrella, while interior zip pockets hold a phone and wallet. "
            "Shot from a 40-degree overhead angle at 35mm f/5.6, capturing the entire open bag and its organized contents. "
            "Bright, even lighting from above with a reflector below to illuminate the bag's interior without deep shadows. "
            "The comprehensive interior view helps buyers understand the bag's true capacity and intelligent pocket layout."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="travel_bag",
        sub_category_name="旅行包",
    ),
    SceneTemplate(
        id="travel_bag_04_shoulder",
        name="肩背展示",
        name_en="Shoulder Carry",
        product_type="travel",
        description="模特兒肩背旅行包的穿搭展示",
        prompt=(
            "A person carrying this travel bag on their shoulder while walking through a modern urban setting or transit station. "
            "The bag's strap sits comfortably across the shoulder with the bag at hip height, showing its natural carrying position. "
            "The person is dressed in smart casual travel attire, with the bag complementing their outfit. "
            "Shot at 85mm f/2.8 from a three-quarter front angle, the person and bag in sharp focus against an urban bokeh background. "
            "Natural golden hour light creates warm highlights on the bag's material and the person's silhouette. "
            "The lifestyle image shows how the bag looks when carried, its proportional size on the body, and its style appeal."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="travel_bag",
        sub_category_name="旅行包",
    ),
    SceneTemplate(
        id="travel_bag_05_weekend",
        name="週末旅行",
        name_en="Weekend Getaway",
        product_type="travel",
        description="旅行包打包準備週末旅行的場景",
        prompt=(
            "This travel bag sitting on a hotel bed or apartment entryway bench, packed and ready for a weekend getaway. "
            "A few items peek out from the slightly unzipped top: a rolled sweater, a paperback book, and sunglasses. "
            "A room key card, coffee cup, and a folded map or phone showing a map app are placed beside the bag. "
            "Shot at 35mm f/3.2 from a natural 30-degree angle, the packed bag as the hero subject with a cozy room blurred behind. "
            "Warm morning light streaming through curtains creates an inviting weekend departure atmosphere. "
            "The scene captures the anticipation of a short trip and positions the bag as the ideal size for spontaneous weekend adventures."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="travel_bag",
        sub_category_name="旅行包",
    ),
]

TemplateRegistry.register("travel", TRAVEL_TEMPLATES)
