from app.templates.registry import SceneTemplate, TemplateRegistry

MOTORCYCLE_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="motorcycle_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="motorcycle",
        description="純白背景，摩托車配件居中展示",
        prompt=(
            "Place this motorcycle accessory on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with a large softbox overhead at 45 degrees "
            "and two side fill lights for clean, even illumination. "
            "The product should be centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding and depth. "
            "Front-facing angle tilted 15 degrees to show form, vents, and hardware detail. "
            "Shot with a 70mm lens at f/9 for maximum depth of field across the entire product. "
            "Ultra-high resolution, crisp details on shell finish, visor clarity, mounting hardware, and material texture. "
            "No other objects in frame. Color accuracy is critical for safety gear."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="motorcycle",
        description="2x2 拼圖佈局，展示安全認證、材質、功能等賣點",
        prompt=(
            "Create a professional product photography collage for this motorcycle accessory. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the main design, brand logo, and overall form. "
            "2) Close-up of the safety feature: shell material, DOT/ECE certification label, or reinforcement. "
            "3) Mounting mechanism, adjustment system, or ventilation detail. "
            "4) Interior lining, padding comfort, or weatherproofing detail. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all shots. "
            "Shot with a 60mm lens at f/8 for uniform sharpness in every panel. "
            "The layout conveys rugged reliability and safety-certified quality."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="motorcycle",
        description="微距特寫，展示安全結構、材質、扣件等細節",
        prompt=(
            "Extreme macro close-up photography of this motorcycle accessory showing build quality and safety details. "
            "Split into 2-3 detail zones: shell material thickness or surface coating quality, "
            "buckle/strap/mounting mechanism precision and metal hardware, "
            "and interior padding or weatherproof seal quality. "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The detail level should convey industrial-grade durability and safety engineering. "
            "Focus stacking technique for maximum sharpness across detail zones. "
            "Professional automotive accessory macro photography with bold contrast."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="motorcycle",
        description="與摩托車部件或手部對比，直觀展示大小",
        prompt=(
            "This motorcycle accessory photographed next to reference objects for size comparison: "
            "a hand gripping or holding the product, and a motorcycle handlebar section "
            "or helmet placed nearby for scale. "
            "All items arranged on a clean white surface or garage-style concrete floor. "
            "The product is the hero element in the center. "
            "Clean background, even studio lighting from an overhead softbox. "
            "Shot with a 50mm lens at f/11 to keep all objects tack-sharp. "
            "The items are proportionally realistic to each other. "
            "The composition clearly communicates the product's real-world fitment size."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_05_riding_scene",
        name="騎行場景",
        name_en="Riding Scene",
        product_type="motorcycle",
        description="騎行中展示安裝在摩托車上的配件",
        prompt=(
            "This motorcycle accessory in action on a motorcycle during a ride. "
            "A rider on a sport or adventure motorcycle on an open road with scenic mountain "
            "or coastal highway in the soft-focus background. "
            "The accessory is clearly visible and functional: mounted on the bike, worn by the rider, "
            "or actively in use during motion. "
            "Dynamic angle from a slightly low three-quarter perspective conveying speed and freedom. "
            "Shot with a 70mm lens at f/2.8 with a fast shutter speed to freeze motion, "
            "golden hour sidelight creating dramatic highlights on the accessory. "
            "Aspirational motorcycle lifestyle photography with an adventurous, open-road feel."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_06_parking_scene",
        name="停車場景",
        name_en="Parking Scene",
        product_type="motorcycle",
        description="停放摩托車上的配件展示",
        prompt=(
            "This motorcycle accessory displayed on a parked motorcycle in a stylish setting. "
            "A clean, well-maintained motorcycle parked on a polished garage floor "
            "or an urban alleyway with exposed brick walls in the background. "
            "The accessory is the focal point, clearly installed or placed on the bike. "
            "Dramatic side lighting from a large window or garage door "
            "creating bold highlights on the chrome and accessory surfaces. "
            "Shot with a 50mm lens at f/2.4, the accessory and nearby bike area in sharp focus "
            "with the environment falling into cinematic bokeh. "
            "Camera at handlebar height for an authentic rider's perspective. "
            "Moody, premium motorcycle culture photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_07_installation",
        name="安裝展示",
        name_en="Installation Showcase",
        product_type="motorcycle",
        description="展示產品安裝過程或穿戴效果",
        prompt=(
            "A rider or mechanic actively installing or wearing this motorcycle accessory. "
            "Hands-on demonstration showing the product being mounted to a motorcycle, "
            "adjusted for fit, or worn as protective gear. "
            "Clean, well-lit garage or workshop setting with tools visible in the background. "
            "The product and hands are in sharp focus, clearly showing the installation process. "
            "Shot with a 45mm lens at f/3.5, overhead workshop pendant light "
            "combined with natural light from a garage door for depth. "
            "Camera angle at working height, slightly above looking down at the installation area. "
            "The image conveys easy installation and practical functionality. "
            "Authentic motorcycle maintenance photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_08_gear_bundle",
        name="裝備組合",
        name_en="Gear Bundle",
        product_type="motorcycle",
        description="摩托車裝備平拍，展示騎行套裝搭配",
        prompt=(
            "This motorcycle accessory arranged in a rugged flat lay with complementary riding gear: "
            "gloves, key fob, action camera, tool kit, and a riding jacket folded nearby. "
            "Top-down perspective on a dark concrete or brushed metal surface. "
            "Each item neatly spaced with intentional geometric arrangement. "
            "The hero product is centrally placed and visually prominent. "
            "Shot overhead with a 35mm lens at f/7.1, even diffused softbox lighting "
            "with a subtle spotlight accent on the hero product for emphasis. "
            "Professional motorcycle gear flat lay photography showing a complete rider's kit. "
            "Bold, masculine aesthetic with industrial material textures."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="motorcycle_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="motorcycle",
        description="展示品牌調性的騎士生活美學",
        prompt=(
            "This motorcycle accessory styled in an aspirational rider's lifestyle scene. "
            "A moody garage or loft vignette: the product on a weathered wooden workbench "
            "alongside vintage motorcycle goggles, a leather-bound journal, "
            "a whiskey glass, and an old road map spread out beneath. "
            "Dramatic warm side lighting from a single industrial pendant lamp, "
            "creating deep shadows and rich amber highlights. "
            "Shot with a 40mm lens at f/4.0 from a slightly low angle to give the scene gravitas. "
            "Rich, warm color palette with deep leather browns, aged metal, and amber tones. "
            "The composition conveys freedom, adventure, and the romance of the open road. "
            "Premium motorcycle culture brand aesthetic with cinematic, editorial mood."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== helmet (頭盔) ====================
    SceneTemplate(
        id="moto_helm_01_wearing",
        name="佩戴展示",
        name_en="Helmet Wearing Display",
        product_type="motorcycle",
        description="騎士佩戴頭盔的展示",
        prompt=(
            "A motorcycle rider wearing this helmet in a confident, forward-facing pose "
            "with the visor slightly raised to show the face partially or visor down for a sleek aerodynamic look. "
            "The helmet fits snugly on the rider's head, showing correct fitment and chin strap secured. "
            "Shot with a 70mm lens at f/2.8 from a three-quarter front angle against a clean dark studio backdrop. "
            "Fashion editorial motorcycle lighting: key light at 45 degrees creating bold highlights "
            "on the helmet shell and visor, with a rim light from behind for dramatic separation. "
            "The rider wears a dark riding jacket that complements the helmet without competing. "
            "Bold, confident motorcycle safety gear photography with premium brand aesthetic."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="helmet",
        sub_category_name="頭盔",
    ),
    SceneTemplate(
        id="moto_helm_02_visor",
        name="面罩特寫",
        name_en="Visor Detail Close-up",
        product_type="motorcycle",
        description="頭盔面罩和護目鏡片的特寫",
        prompt=(
            "Close-up photography of this helmet's visor and shield mechanism in detail: "
            "the optical clarity of the lens, anti-fog coating surface, the pivot mechanism, "
            "and the visor lock system visible from a side-angle perspective. "
            "Shot with a 85mm macro lens at f/3.5, shallow depth of field with the visor surface in sharp focus "
            "and the helmet shell falling into soft bokeh behind. "
            "Studio lighting positioned to create a subtle reflection across the visor surface "
            "showing its clarity and anti-scratch finish. "
            "A slight environment reflection in the visor adds realism. "
            "Professional helmet detail photography emphasizing optical quality and safety engineering."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="helmet",
        sub_category_name="頭盔",
    ),
    SceneTemplate(
        id="moto_helm_03_interior",
        name="內襯展示",
        name_en="Interior Lining Display",
        product_type="motorcycle",
        description="頭盔可拆卸內襯的展示",
        prompt=(
            "This helmet turned upside down or at an angle to reveal its interior lining system: "
            "the removable and washable cheek pads, moisture-wicking fabric, "
            "the EPS foam safety liner, and the comfort padding. "
            "One cheek pad is partially removed and placed beside the helmet to show the detachable design. "
            "Shot with a 50mm lens at f/4.5 from a front overhead angle, "
            "even studio lighting at 5500K illuminating the interior cavity clearly. "
            "The fabric texture and padding density are clearly visible. "
            "The composition communicates comfort, hygiene through removable liners, "
            "and the multi-layer safety construction of a premium motorcycle helmet."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="helmet",
        sub_category_name="頭盔",
    ),
    SceneTemplate(
        id="moto_helm_04_safety",
        name="安全認證",
        name_en="Safety Certification Display",
        product_type="motorcycle",
        description="頭盔安全認證標籤清晰可見的展示",
        prompt=(
            "This helmet photographed at an angle that prominently shows the safety certification labels: "
            "DOT, ECE 22.06, or SNELL sticker clearly visible on the back or chin area of the helmet. "
            "The helmet shell material quality and construction are also visible from this rear-quarter angle. "
            "Shot with a 60mm lens at f/5.6, the certification label in tack-sharp focus "
            "with the helmet's aerodynamic profile providing visual context. "
            "Clean, bright studio lighting at 5500K ensures the certification text and logos are perfectly legible. "
            "The image builds buyer confidence by prominently featuring verified safety standards, "
            "communicating that this helmet meets or exceeds international safety requirements."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="helmet",
        sub_category_name="頭盔",
    ),
    SceneTemplate(
        id="moto_helm_05_rack",
        name="架上展示",
        name_en="Helmet on Display Rack",
        product_type="motorcycle",
        description="頭盔放在展示架或掛鉤上的展示",
        prompt=(
            "This helmet displayed on a professional helmet stand or wall-mounted hook "
            "in a clean garage or rider's den setting. "
            "The helmet is positioned at a dynamic three-quarter angle showing its design profile, "
            "with the visor slightly open for visual interest. "
            "A motorcycle handlebar or tank is visible in the soft background for context. "
            "Shot with a 50mm lens at f/3.0, the helmet in sharp focus "
            "with the garage environment providing atmospheric depth. "
            "Warm side lighting from a garage window creates dramatic highlights on the helmet shell "
            "and bold shadows that emphasize its aerodynamic shape. "
            "The image conveys a rider's ready-to-go lifestyle and premium gear organization."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="helmet",
        sub_category_name="頭盔",
    ),
    # ==================== moto_parts (車身配件) ====================
    SceneTemplate(
        id="moto_part_01_installed",
        name="安裝效果",
        name_en="Part Installed on Motorcycle",
        product_type="motorcycle",
        description="配件安裝在摩托車上的效果展示",
        prompt=(
            "This motorcycle part installed on a bike, photographed to show the finished installation result. "
            "The camera focuses on the specific area where the part is mounted: mirror, guard, exhaust, "
            "or body panel, clearly visible and perfectly fitted on the motorcycle. "
            "Shot with a 50mm lens at f/3.2 from an angle that best showcases the part's integration with the bike. "
            "The motorcycle is parked in a clean garage or studio with controlled lighting. "
            "Focused spotlight on the installed part with ambient fill lighting on the surrounding bike area. "
            "The image demonstrates perfect fitment, quality finish matching the motorcycle, "
            "and the visual upgrade the part provides to the overall bike aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="moto_parts",
        sub_category_name="車身配件",
    ),
    SceneTemplate(
        id="moto_part_02_before_after",
        name="安裝對比",
        name_en="Before and After Installation",
        product_type="motorcycle",
        description="配件安裝前後的對比展示",
        prompt=(
            "A side-by-side or split-frame comparison showing the motorcycle before and after installing this part. "
            "The left side shows the stock or bare mounting area, and the right side shows the same angle "
            "with the part professionally installed, highlighting the visual and functional improvement. "
            "Both shots taken from the identical camera angle with a 50mm lens at f/5.6 "
            "for consistent sharpness and perspective across both frames. "
            "Even studio lighting at 5500K ensures accurate color matching between the before and after. "
            "A clean dividing line separates the two images. "
            "The composition clearly communicates the upgrade value and aesthetic improvement this part delivers."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="moto_parts",
        sub_category_name="車身配件",
    ),
    SceneTemplate(
        id="moto_part_03_detail",
        name="工藝特寫",
        name_en="Part Craftsmanship Close-up",
        product_type="motorcycle",
        description="配件材質和做工品質的特寫",
        prompt=(
            "Extreme macro close-up of this motorcycle part showing its material quality and manufacturing precision: "
            "CNC-machined aluminum surface finish, carbon fiber weave pattern, "
            "anodized coloring depth, or stainless steel weld quality. "
            "Shot with a 100mm macro lens at f/3.5, very shallow depth of field "
            "isolating the material texture in pin-sharp focus with surrounding areas in soft blur. "
            "Ring light illumination reveals the grain, finish, and surface treatment quality. "
            "The detail level communicates aerospace-grade manufacturing and premium material sourcing. "
            "Professional automotive parts macro photography with bold industrial aesthetics."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="moto_parts",
        sub_category_name="車身配件",
    ),
    SceneTemplate(
        id="moto_part_04_tools",
        name="安裝工具",
        name_en="Part with Installation Tools",
        product_type="motorcycle",
        description="配件與安裝所需工具的展示",
        prompt=(
            "This motorcycle part laid out alongside the tools required for installation: "
            "Allen keys, socket wrenches, torque wrench, thread locker, and any included mounting hardware. "
            "Arranged in a clean flat lay on a dark workshop surface or rubber mat. "
            "The part is centrally placed as the hero item with tools fanned out around it. "
            "Shot from directly overhead with a 35mm lens at f/7.1, "
            "even bright studio lighting at 5500K ensuring all tool markings and part details are sharp. "
            "The composition serves as a practical pre-installation reference, "
            "communicating that the buyer will need specific tools and showing the straightforward installation scope."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="moto_parts",
        sub_category_name="車身配件",
    ),
    SceneTemplate(
        id="moto_part_05_package",
        name="包裝內容",
        name_en="Package Contents Display",
        product_type="motorcycle",
        description="配件完整包裝內容物的展示",
        prompt=(
            "All contents from this motorcycle part's packaging displayed in an organized flat lay: "
            "the main part, mounting brackets, bolt kits, rubber gaskets, instruction sheet, "
            "and any included stickers or brand materials, all laid out neatly. "
            "The original packaging box is positioned at the top of the frame with contents spread below. "
            "Shot from directly overhead with a 35mm lens at f/7.1 on a clean dark surface. "
            "Even, bright studio lighting at 5500K ensures every small component is clearly visible. "
            "Each item is labeled or grouped logically for easy identification. "
            "The composition communicates complete package contents, build quality of included hardware, "
            "and reassures buyers that everything needed for installation is included."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="moto_parts",
        sub_category_name="車身配件",
    ),
    # ==================== riding_gear (騎行裝備) ====================
    SceneTemplate(
        id="moto_gear_01_wearing",
        name="穿戴展示",
        name_en="Riding Gear Wearing Display",
        product_type="motorcycle",
        description="騎士穿戴騎行裝備的展示",
        prompt=(
            "A motorcycle rider wearing this riding gear in a strong, confident standing pose "
            "beside their parked motorcycle in a clean garage or urban setting. "
            "The gear fits properly, showing its silhouette, styling, and functional design elements. "
            "Shot with a 50mm lens at f/2.8 from a three-quarter front angle, full body or waist up, "
            "the gear in sharp focus with the motorcycle providing soft, contextual background. "
            "Dramatic side lighting from a large window creates bold highlights on the gear's textile "
            "and protective panel surfaces. "
            "The rider appears confident and road-ready. "
            "Bold motorcycle lifestyle photography conveying safety, style, and riding culture."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="riding_gear",
        sub_category_name="騎行裝備",
    ),
    SceneTemplate(
        id="moto_gear_02_protection",
        name="防護展示",
        name_en="Protection Features Display",
        product_type="motorcycle",
        description="騎行裝備的防護墊和護甲展示",
        prompt=(
            "This riding gear displayed to highlight its protective features: "
            "the jacket or pants opened or unzipped to reveal the internal CE-rated armor, "
            "removable shoulder and elbow protectors placed beside the garment, "
            "and the abrasion-resistant outer material visible. "
            "Shot with a 45mm lens at f/4.5 from a front angle on a clean white or gray surface. "
            "Even studio lighting at 5500K ensures the armor material, protective padding density, "
            "and textile construction are all clearly visible. "
            "The composition serves as a safety features overview, communicating the multi-layer protection system "
            "and the engineering that goes into keeping riders safe."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="riding_gear",
        sub_category_name="騎行裝備",
    ),
    SceneTemplate(
        id="moto_gear_03_weather",
        name="全天候",
        name_en="All-Weather Riding Gear",
        product_type="motorcycle",
        description="騎行裝備在不同天氣條件下的展示",
        prompt=(
            "This riding gear shown in a dramatic weather context: a rider standing by their motorcycle "
            "in light rain or mist, the gear's waterproof membrane visibly repelling water droplets on the surface. "
            "Alternatively, the rider in bright sunshine with ventilation panels open for airflow. "
            "Shot with a 70mm lens at f/2.8, the gear and water beading in sharp focus "
            "against a moody, overcast sky or dramatic weather backdrop in soft bokeh. "
            "Dramatic natural lighting with overcast diffusion creating even, cinematic illumination. "
            "The image communicates all-weather versatility, waterproofing performance, "
            "and the gear's ability to keep riders comfortable in any riding condition."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="riding_gear",
        sub_category_name="騎行裝備",
    ),
    SceneTemplate(
        id="moto_gear_04_storage",
        name="收納展示",
        name_en="Gear Storage and Pockets",
        product_type="motorcycle",
        description="騎行裝備的收納口袋展示",
        prompt=(
            "This riding gear displayed with all storage features highlighted: "
            "multiple pockets unzipped to show their depth and contents such as a phone, wallet, and keys, "
            "internal waterproof pockets visible, and any special compartment for back protectors or communication devices. "
            "The gear is laid flat or draped over a stand showing both front and internal pocket layout. "
            "Shot with a 45mm lens at f/5.0 from a slight overhead angle, "
            "even bright studio lighting at 5500K ensuring all pocket interiors and zipper details are visible. "
            "The composition serves as a practical storage guide, communicating the gear's organizational features "
            "and convenient access to essentials while riding."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="riding_gear",
        sub_category_name="騎行裝備",
    ),
    SceneTemplate(
        id="moto_gear_05_riding",
        name="騎行場景",
        name_en="Riding in Gear Scene",
        product_type="motorcycle",
        description="穿戴裝備實際騎行中的場景",
        prompt=(
            "A rider wearing this gear while actively riding their motorcycle on a scenic mountain road "
            "or winding coastal highway, captured in a dynamic action shot. "
            "The gear is clearly visible on the rider, showing how it looks and moves during actual riding. "
            "Shot from a chase vehicle or trackside with a 70mm lens at f/2.8, "
            "fast shutter speed freezing the motion with the road and scenery in motion blur behind. "
            "Golden hour warm sidelight creates dramatic highlights across the gear's surface and the bike's bodywork. "
            "The camera angle is from a low three-quarter perspective for a heroic, cinematic feel. "
            "Aspirational motorcycle adventure photography conveying freedom, performance, and ultimate riding style."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="riding_gear",
        sub_category_name="騎行裝備",
    ),
]

TemplateRegistry.register("motorcycle", MOTORCYCLE_TEMPLATES)
