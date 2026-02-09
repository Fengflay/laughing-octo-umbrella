from app.templates.registry import SceneTemplate, TemplateRegistry

AUTOMOTIVE_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="automotive_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="automotive",
        description="純白背景，汽車配件居中，清晰展示產品外觀",
        prompt=(
            "This automotive accessory product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with dual softbox lighting at 45 degrees and overhead fill. "
            "The product is centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding and depth. "
            "Front-facing angle slightly tilted 20 degrees to show dimension and construction. "
            "Shot with a 90mm lens at f/9 for maximum depth of field across the entire product. "
            "Ultra-high resolution, crisp details on material texture, logos, and hardware components. "
            "No other objects in frame. Color accuracy is critical."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="automotive",
        description="展示材質耐用性、防水性、安裝便利等核心賣點",
        prompt=(
            "Create a professional product photography collage for this automotive accessory. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the full product design and branding. "
            "2) Close-up of the durable material: UV-resistant fabric, scratch-proof coating, or reinforced construction. "
            "3) Functional mechanism: mounting clip, suction cup, elastic strap, or adjustable buckle. "
            "4) Compatibility feature: universal fit system, size adjustment, or vehicle-specific design. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "Shot at f/6.3 with a 60mm lens for uniform clarity. "
            "The layout conveys durability, quality, and practical functionality."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="automotive",
        description="微距特寫，展示材質紋理、縫線品質、五金耐用度",
        prompt=(
            "Extreme macro close-up photography of this automotive accessory showing build quality details. "
            "Split into 2-3 detail zones: material surface texture showing durability and weather resistance, "
            "reinforced stitching or heat-welded seams at stress points, "
            "and hardware quality (stainless steel clips, heavy-duty zippers, or precision-molded plastic components). "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The texture should convey automotive-grade ruggedness and quality. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional automotive product macro photography for e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="automotive",
        description="與方向盤、車鑰匙等常見車用物品對比大小",
        prompt=(
            "This automotive accessory photographed next to common reference objects for size comparison: "
            "a car key fob, a standard water bottle, and a smartphone. "
            "All items on a clean white surface with a subtle grid pattern for scale reference. "
            "The automotive product is the central hero element. "
            "Clean white background, even studio lighting from above. "
            "Shot from a slightly elevated 30-degree angle at f/11 with a 50mm lens to keep all objects tack-sharp. "
            "The composition clearly communicates the product's practical size for vehicle owners. "
            "Items proportionally realistic to each other."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_05_car_interior_scene",
        name="車內場景",
        name_en="Car Interior Scene",
        product_type="automotive",
        description="產品安裝在車內的實際使用場景",
        prompt=(
            "This automotive accessory installed and in use inside a modern car interior. "
            "The product is mounted on the dashboard, steering wheel, seat, or windshield in its correct position. "
            "Clean, modern car interior with leather seats and a contemporary dashboard visible. "
            "Natural daylight streaming through the windshield providing bright, even illumination. "
            "Shot at 24mm f/3.5 wide-angle to capture both the product and the car interior context. "
            "Camera positioned from the passenger seat perspective looking across naturally. "
            "The product is the clear focal point, sharp and prominent in the frame. "
            "Professional automotive lifestyle photography with clean, modern aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_06_car_care_scene",
        name="洗車場景",
        name_en="Car Care Scene",
        product_type="automotive",
        description="使用產品進行車輛清潔保養的場景",
        prompt=(
            "This automotive accessory being used in a car care context on a clean vehicle exterior. "
            "A person's hands using or applying the product on a shiny car surface in a bright driveway or garage. "
            "The car paint is glossy and reflective, showing the product's effectiveness. "
            "Bright natural outdoor lighting with soft shadows, golden hour warmth. "
            "Shot at 50mm f/2.8 with shallow depth of field, the product and hands in sharp focus. "
            "Camera at a natural working angle, slightly below eye level. "
            "The scene conveys ease of use and professional-grade car care results. "
            "Clean, aspirational automotive maintenance photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_07_installation",
        name="安裝展示",
        name_en="Installation Demo",
        product_type="automotive",
        description="展示產品安裝過程或安裝後效果",
        prompt=(
            "A person's hands installing or adjusting this automotive accessory on a vehicle. "
            "The installation process is clear and looks effortless. "
            "Shot from a close perspective showing both the product and the mounting point on the vehicle. "
            "Clean, well-lit garage or driveway setting with good overhead lighting. "
            "Professional lighting: key light at 45 degrees from upper left with fill light to eliminate harsh shadows. "
            "Shot at 50mm f/2.8 for sharp focus on the hands and product with soft background. "
            "Camera at a natural viewing angle, slightly elevated. "
            "The image conveys easy, tool-free or simple installation that any car owner can do."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_08_accessory_bundle",
        name="配件組合",
        name_en="Accessory Bundle",
        product_type="automotive",
        description="多件汽車配件的搭配組合展示",
        prompt=(
            "This automotive accessory shown in a curated flat lay arrangement with complementary car care items: "
            "a microfiber cloth, a car air freshener, a phone mount, a key organizer, and a cleaning spray bottle. "
            "Top-down overhead perspective on a clean dark gray or matte black surface. "
            "Items arranged with intentional spacing in a structured grid pattern. "
            "The hero product is centrally positioned and visually prominent. "
            "Shot directly overhead at f/7.1 with even diffused softbox lighting from above. "
            "Professional, masculine aesthetic with dark tones and subtle highlights. "
            "Automotive product flat lay photography conveying a complete car care solution."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="automotive_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="automotive",
        description="展示汽車配件品牌調性的精緻擺拍",
        prompt=(
            "This automotive accessory styled in a premium lifestyle arrangement. "
            "The product placed on a polished concrete or dark leather surface alongside luxury car keys, "
            "designer sunglasses, a premium watch, and a leather driving glove. "
            "Shot from directly above on a dark, sophisticated surface. "
            "Cohesive dark color palette with metallic accents, editorial automotive mood. "
            "Dramatic directional lighting from upper left creating bold shadows and highlights. "
            "Shot at f/3.5 with a 50mm lens for natural perspective. "
            "The composition conveys automotive luxury, performance, and premium quality. "
            "Each object placed with precise intentional spacing following rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== interior (車內配件) ====================
    SceneTemplate(
        id="auto_int_01_installed",
        name="安裝效果",
        name_en="Installed in Interior",
        product_type="automotive",
        description="配件安裝在車內的實際效果展示",
        prompt=(
            "This interior car accessory properly installed in a modern vehicle cabin, showing how it integrates with the existing dashboard and console design. "
            "The accessory is positioned in its correct mounting location: center console, sun visor, headrest, or door pocket. "
            "The surrounding car interior is clean, modern, with leather trim and brushed aluminum accents visible. "
            "Shot at 24mm f/3.5 wide-angle from the rear seat or passenger perspective to capture the full interior context. "
            "Natural daylight through the windshield provides even, bright illumination without harsh glare. "
            "The composition demonstrates seamless integration and proves the accessory enhances rather than clutters the cabin aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="interior",
        sub_category_name="車內配件",
    ),
    SceneTemplate(
        id="auto_int_02_driver_view",
        name="駕駛視角",
        name_en="Driver Perspective",
        product_type="automotive",
        description="從駕駛座視角展示配件的使用效果",
        prompt=(
            "This car interior accessory photographed from the driver's seated perspective, showing exactly how it looks during normal driving. "
            "The steering wheel is partially visible at the bottom of the frame, the dashboard ahead, and the accessory in its installed position. "
            "Through the windshield, a blurred suburban road or parking lot is visible, grounding the scene in reality. "
            "Shot at 20mm f/4.0 ultra-wide to capture the full driver's field of view with the accessory naturally in frame. "
            "Even interior lighting with no harsh reflections on the windshield or dashboard surfaces. "
            "The image proves the accessory is within easy reach and does not obstruct visibility or driving controls."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="interior",
        sub_category_name="車內配件",
    ),
    SceneTemplate(
        id="auto_int_03_organizer",
        name="車內收納",
        name_en="Car Organizer in Use",
        product_type="automotive",
        description="車內收納配件裝滿物品的使用展示",
        prompt=(
            "This car organizer accessory installed in a vehicle, filled with everyday driving essentials: sunglasses, phone, water bottle, tissues, and coins. "
            "The organizer hangs from the back of a seat, sits in the console, or attaches to the visor with all compartments visible and utilized. "
            "The interior is a clean, modern car cabin with leather seats and ambient lighting visible. "
            "Shot at 35mm f/3.2 from a natural passenger or rear-seat perspective showing the organizer in context. "
            "Bright interior lighting from overhead dome light supplemented by daylight through side windows. "
            "The composition demonstrates practical storage capacity and easy accessibility while driving."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="interior",
        sub_category_name="車內配件",
    ),
    SceneTemplate(
        id="auto_int_04_comfort",
        name="舒適展示",
        name_en="Comfort Showcase",
        product_type="automotive",
        description="坐墊或靠墊在車座上的舒適使用展示",
        prompt=(
            "This car comfort accessory (seat cushion, lumbar support, or neck pillow) placed on a leather car seat, showing its ergonomic fit. "
            "The cushion conforms naturally to the seat contour, with its memory foam or gel structure slightly visible at the edges. "
            "The car seat's headrest, seatbelt, and center console are partially visible for context. "
            "Shot at 50mm f/3.5 from a side angle at door level, showing the cushion's profile and thickness on the seat. "
            "Soft natural light from the open car door illuminates the scene with warm, inviting tones. "
            "The image communicates premium comfort, proper lumbar support, and a significant upgrade to the driving experience."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="interior",
        sub_category_name="車內配件",
    ),
    SceneTemplate(
        id="auto_int_05_night",
        name="夜間效果",
        name_en="Night Ambient Effect",
        product_type="automotive",
        description="車內配件在夜間環境燈光下的效果展示",
        prompt=(
            "This car interior accessory photographed inside a vehicle at night, showcasing its appearance under ambient cabin lighting. "
            "The dashboard instruments glow softly in blue or orange, LED strip lights outline the console, and the accessory catches the ambient light beautifully. "
            "If the product has its own LED feature, it is illuminated in a complementary color. "
            "Shot at 35mm f/2.0 with a slow shutter to capture the ambient glow, camera mounted on the dashboard or headrest. "
            "The exterior through the windows is dark with distant city lights creating bokeh points. "
            "The moody, atmospheric composition demonstrates how the accessory enhances the premium nighttime driving experience."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="interior",
        sub_category_name="車內配件",
    ),
    # ==================== exterior (車外配件) ====================
    SceneTemplate(
        id="auto_ext_01_installed",
        name="外裝效果",
        name_en="Exterior Installed",
        product_type="automotive",
        description="配件安裝在車輛外部的實際效果展示",
        prompt=(
            "This exterior car accessory mounted on a clean, polished vehicle: on the roof rack, side mirror, bumper, or trunk lid. "
            "The car's body paint is glossy and reflective, contrasting with the accessory's matte or textured finish. "
            "The vehicle is parked in a clean driveway or parking structure with even natural daylight. "
            "Shot at 50mm f/4.0 from a three-quarter front angle showing both the accessory and the car's profile. "
            "Bright overcast sky provides soft, shadowless lighting that accurately shows the accessory's color and contour. "
            "The composition demonstrates professional-grade fitment and how the accessory complements the vehicle's exterior design."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="exterior",
        sub_category_name="車外配件",
    ),
    SceneTemplate(
        id="auto_ext_02_close_up",
        name="細節特寫",
        name_en="Exterior Detail Close-up",
        product_type="automotive",
        description="車外配件細節與材質的特寫展示",
        prompt=(
            "A tight close-up of this exterior car accessory focusing on its surface finish, mounting hardware, and construction quality. "
            "The car's body panel serves as a sleek backdrop, with the accessory's edge or mounting bracket clearly visible. "
            "Surface details like carbon fiber weave, chrome plating, or UV-resistant rubber gaskets are magnified. "
            "Shot at 100mm macro f/4.0 with focus stacking for edge-to-edge sharpness across the accessory's surface. "
            "Natural outdoor light from an overcast sky provides even illumination without harsh reflections on chrome or glass surfaces. "
            "The macro perspective communicates premium build quality and weather-resistant materials to discerning car enthusiasts."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="exterior",
        sub_category_name="車外配件",
    ),
    SceneTemplate(
        id="auto_ext_03_wash",
        name="洗車場景",
        name_en="Car Wash Scene",
        product_type="automotive",
        description="車外配件在洗車場景中的展示",
        prompt=(
            "This exterior car accessory visible on a vehicle during a hand wash: water beading on its surface demonstrates water resistance. "
            "Suds cascade around the accessory while a microfiber mitt glides nearby, showing the product's easy-clean properties. "
            "The car is positioned in a bright outdoor wash bay or sunny driveway with water spray catching the light. "
            "Shot at 50mm f/3.5 from a close angle focusing on the accessory and the water interaction. "
            "Bright midday sunlight creates sparkle on water droplets and highlights the accessory's surface durability. "
            "The composition proves the accessory withstands regular washing and maintains its appearance under wet conditions."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="exterior",
        sub_category_name="車外配件",
    ),
    SceneTemplate(
        id="auto_ext_04_weather",
        name="全天候",
        name_en="All-Weather Protection",
        product_type="automotive",
        description="車外配件在不同天氣條件下的保護效果",
        prompt=(
            "This exterior car accessory protecting a vehicle in challenging weather: heavy rain, bright sun, or light snow on the car surface. "
            "Rain droplets bead and roll off the accessory's hydrophobic surface, or UV rays are visually blocked by a sun shade or cover. "
            "The vehicle is parked outdoors with the weather condition clearly visible in the environment. "
            "Shot at 35mm f/4.0 from a low angle emphasizing the accessory's protective coverage against the dramatic sky. "
            "Natural environmental lighting appropriate to the weather condition: overcast gray for rain, bright harsh sun for UV protection. "
            "The dramatic composition communicates all-season durability and reliable protection for the vehicle."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="exterior",
        sub_category_name="車外配件",
    ),
    SceneTemplate(
        id="auto_ext_05_comparison",
        name="安裝對比",
        name_en="Before After Installation",
        product_type="automotive",
        description="配件安裝前後的對比效果展示",
        prompt=(
            "A split-composition or side-by-side comparison showing the vehicle area before and after installing this exterior accessory. "
            "The left half shows the bare car surface, while the right half shows the same area with the accessory professionally installed. "
            "Both halves share identical lighting, angle, and background for a fair visual comparison. "
            "Shot at 50mm f/5.6 from a straight-on angle ensuring both sides are equally sharp and well-lit. "
            "Clean studio-quality lighting with dual softboxes at 45 degrees ensures consistent color and shadow across the split frame. "
            "The before-and-after format clearly communicates the visual upgrade and protection the accessory provides."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="exterior",
        sub_category_name="車外配件",
    ),
    # ==================== maintenance (保養用品) ====================
    SceneTemplate(
        id="auto_maint_01_using",
        name="使用過程",
        name_en="Product in Use",
        product_type="automotive",
        description="展示使用保養產品進行車輛清潔的過程",
        prompt=(
            "A person's hand actively using this car maintenance product on a vehicle surface: applying polish, spraying cleaner, or buffing with a pad. "
            "The hand motion suggests smooth, effortless application with the product clearly visible and labeled. "
            "The car panel being treated shows a visible difference where the product has been applied versus untreated areas. "
            "Shot at 60mm f/2.8 from a close working angle, sharp focus on the product and application zone. "
            "Bright garage lighting from overhead fluorescents mixed with natural light from an open garage door. "
            "The action shot conveys professional-quality results achievable by everyday car owners with this product."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="maintenance",
        sub_category_name="保養用品",
    ),
    SceneTemplate(
        id="auto_maint_02_before_after",
        name="效果對比",
        name_en="Before After Results",
        product_type="automotive",
        description="使用保養產品前後的效果對比展示",
        prompt=(
            "A dramatic before-and-after comparison showing this car maintenance product's effectiveness on a vehicle surface. "
            "The left side shows a dirty, dull, or scratched surface, while the right side shows the same surface after treatment: gleaming, restored, and protected. "
            "A clear dividing line runs down the center where the product application stopped, making the contrast unmistakable. "
            "Shot at 60mm f/5.6 from a 20-degree angle with the product bottle positioned at the bottom of the frame. "
            "Even studio lighting from both sides ensures the before-and-after difference is clearly attributable to the product, not lighting tricks. "
            "The powerful visual comparison is the most convincing sales tool for car care products."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="maintenance",
        sub_category_name="保養用品",
    ),
    SceneTemplate(
        id="auto_maint_03_kit",
        name="整套展示",
        name_en="Complete Kit Display",
        product_type="automotive",
        description="整套車輛保養用品的完整展示",
        prompt=(
            "A complete car maintenance kit spread out in an organized arrangement: this hero product flanked by complementary items such as microfiber towels, applicator pads, detailing brushes, spray bottles, and a carry case. "
            "All items arranged in a structured flat lay on a dark matte surface from directly overhead. "
            "Each item is clearly identifiable with labels facing the camera where applicable. "
            "Shot at f/8 with a 50mm lens and even diffused softbox lighting from above for consistent illumination across all items. "
            "The hero product is slightly elevated or positioned at the center of the arrangement for visual prominence. "
            "The composition communicates a complete, professional-grade detailing solution ready for immediate use."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="maintenance",
        sub_category_name="保養用品",
    ),
    SceneTemplate(
        id="auto_maint_04_detail",
        name="細節清潔",
        name_en="Detail Cleaning",
        product_type="automotive",
        description="使用產品進行車輛細部清潔的特寫展示",
        prompt=(
            "A close-up of this car maintenance product being used to clean a specific vehicle detail area: leather seat stitching, air vent slats, wheel spokes, or door jamb crevices. "
            "A small detailing brush or microfiber cloth applies the product to the tight area with precision. "
            "The before-and-after difference is visible within the same frame as the cleaning progresses across the surface. "
            "Shot at 100mm macro f/3.5 from a tight angle focusing on the exact detail area being cleaned. "
            "Bright, even lighting from a portable LED panel ensures the crevices and details are fully illuminated. "
            "The macro perspective proves the product works effectively even on the most intricate and hard-to-reach areas of the vehicle."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="maintenance",
        sub_category_name="保養用品",
    ),
    SceneTemplate(
        id="auto_maint_05_garage",
        name="車庫場景",
        name_en="Home Garage Scene",
        product_type="automotive",
        description="保養用品在家庭車庫中的陳列場景",
        prompt=(
            "This car maintenance product displayed on a clean metal garage shelf or workbench alongside other organized car care supplies. "
            "The garage is tidy and well-lit, with a vehicle partially visible in the background and tools hung neatly on a pegboard wall. "
            "The hero product is positioned front and center with its label clearly visible, surrounded by complementary detailing items. "
            "Shot at 35mm f/3.2 from a natural standing eye-level perspective in the garage. "
            "Overhead fluorescent workshop lighting mixed with daylight from the open garage door creates an authentic home garage atmosphere. "
            "The lifestyle scene positions the product as an essential part of a car enthusiast's well-equipped home garage setup."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="maintenance",
        sub_category_name="保養用品",
    ),
]

TemplateRegistry.register("automotive", AUTOMOTIVE_TEMPLATES)
