from app.templates.registry import SceneTemplate, TemplateRegistry

PETS_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="pets_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="pets",
        description="純白背景，寵物用品居中，清晰展示產品外觀",
        prompt=(
            "This pet product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with soft box lighting from above at 45 degrees and two side fill lights. "
            "The product is centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for depth. "
            "Front-facing angle slightly tilted 15 degrees to show depth and dimension. "
            "Shot with a 85mm lens at f/8 for maximum depth of field, ensuring crisp details on materials, buckles, and textures. "
            "Ultra-high resolution, accurate color reproduction. "
            "No animals or other objects in frame. Clean commercial product photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="pets",
        description="展示安全材質、耐咬設計、清洗方式等核心賣點",
        prompt=(
            "Create a professional product photography collage for this pet product. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the complete product design and branding. "
            "2) Close-up of the safety material and construction quality (non-toxic, durable). "
            "3) Functional detail: buckle mechanism, dispensing system, or interactive feature. "
            "4) Cleaning or maintenance feature: washable surface, removable cover, or dishwasher-safe component. "
            "Each view is clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "Shot at f/5.6 with a 60mm lens for consistent clarity. "
            "The overall layout is balanced and trustworthy for pet owners."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="pets",
        description="微距特寫，展示材質安全性、縫線品質、五金耐用度",
        prompt=(
            "Extreme macro close-up photography of this pet product showing quality and safety details. "
            "Split into 2-3 detail zones: material surface texture showing non-toxic food-grade or pet-safe finish, "
            "reinforced stitching or welded seams for durability, "
            "and hardware quality (stainless steel buckles, rust-proof snaps, or BPA-free plastic joints). "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The texture should convey durability and pet-safe quality. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional pet product detail photography for premium e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="pets",
        description="與常見物品或寵物剪影對比，直觀展示大小",
        prompt=(
            "This pet product photographed next to common reference objects for size comparison: "
            "a standard tennis ball, a human hand, and a smartphone. "
            "All items on a clean white surface with a subtle grid pattern for scale reference. "
            "The pet product is the central hero element. "
            "Clean white background, even studio lighting from above. "
            "Shot from a slightly elevated 25-degree angle at f/11 with a 50mm lens to keep all objects tack-sharp. "
            "The composition clearly communicates the product's actual size for pet owners. "
            "Items proportionally realistic to each other."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_05_pet_interaction_scene",
        name="寵物互動",
        name_en="Pet Interaction",
        product_type="pets",
        description="寵物正在使用或穿戴產品的互動場景",
        prompt=(
            "An adorable pet actively using or wearing this pet product. "
            "A happy dog or cat interacting naturally with the product: eating from the bowl, wearing the harness, "
            "playing with the toy, or resting in the bed. "
            "Bright, warm natural lighting from a nearby window. "
            "Clean living room or garden background with soft bokeh. "
            "Shot at 70mm f/2.8 to isolate the pet and product from the background. "
            "Camera at the pet's eye level for an engaging, intimate perspective. "
            "The image captures genuine joy and comfort. "
            "Professional pet lifestyle photography with warm color tones around 5800K."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_06_home_scene",
        name="居家場景",
        name_en="Home Scene",
        product_type="pets",
        description="產品在居家寵物角落的使用情境",
        prompt=(
            "This pet product placed naturally in a cozy home environment with a dedicated pet area. "
            "A well-organized pet corner in a modern living room with the product as the centerpiece. "
            "Warm ambient lighting from table lamps mixed with soft natural window light. "
            "The pet area includes a pet bed, water bowl, and a few toys arranged neatly. "
            "Shot at 28mm f/4.0 for a wider environmental view showing the home context. "
            "Camera angle at a natural standing perspective looking slightly downward. "
            "The scene conveys a loving, pet-friendly home with stylish organization. "
            "Interior lifestyle photography with warm, inviting color palette."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_07_pet_showcase",
        name="寵物展示",
        name_en="Pet Showcase",
        product_type="pets",
        description="寵物搭配產品的正式展示照",
        prompt=(
            "A beautiful, well-groomed pet posing elegantly with this pet product. "
            "The pet is calm and photogenic, wearing or positioned next to the product. "
            "Clean neutral background (soft beige or light gray studio backdrop). "
            "Professional pet photography lighting: key light at 45 degrees with soft fill and catchlight in the pet's eyes. "
            "The pet and product are both in sharp focus as co-subjects. "
            "Shot at 85mm f/2.8 for beautiful portrait-style bokeh on the background. "
            "The image conveys quality, care, and the bond between pets and their accessories. "
            "Editorial pet photography with warm, affectionate mood."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_08_pet_bundle",
        name="寵物組合",
        name_en="Pet Bundle",
        product_type="pets",
        description="多件寵物用品的搭配組合展示",
        prompt=(
            "This pet product shown in a curated flat lay arrangement with complementary pet supplies: "
            "a leash, treats, a grooming brush, a toy, and a feeding bowl. "
            "Top-down overhead perspective on a clean white or light wood surface. "
            "Items arranged with intentional spacing in a pleasing circular or grid pattern. "
            "The hero product is centrally positioned and visually prominent. "
            "Shot directly overhead at f/7.1 with even diffused softbox lighting from above. "
            "Bright, organized aesthetic that conveys a complete pet care solution. "
            "Professional pet product flat lay photography with cohesive color coordination."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="pets_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="pets",
        description="展示寵物品牌溫馨調性的精緻擺拍",
        prompt=(
            "This pet product styled in a warm, heartfelt lifestyle arrangement. "
            "The product placed on a soft knitted blanket alongside a small potted plant, "
            "a ceramic treat jar, and a pet bandana, creating an artful vignette. "
            "Shot on a natural wood or warm linen surface from directly above. "
            "Cohesive warm earth-tone color palette with touches of green and cream. "
            "Soft directional lighting from upper left creating gentle shadows. "
            "Shot at f/3.5 with a 50mm lens for natural perspective. "
            "The composition conveys love, warmth, and premium care for pets. "
            "Each object placed with precise intentional spacing following rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== pet_food (寵物食品) ====================
    SceneTemplate(
        id="pet_food_01_bowl",
        name="餐碗餵食",
        name_en="Food in Bowl",
        product_type="pets",
        description="寵物食品倒入碗中，展示食物質感與份量",
        prompt=(
            "This pet food product served in a clean ceramic or stainless steel pet bowl on a light wood kitchen floor. "
            "The kibble or wet food is mounded generously in the bowl, showing its color, shape, and appetizing texture. "
            "A few pieces are scattered artfully beside the bowl to show individual piece detail. "
            "Shot at 60mm f/3.5 from a 30-degree elevated angle, the food in sharp focus with the kitchen background softly blurred. "
            "Warm natural light from a window creates a fresh morning feeding atmosphere at 5500K color temperature. "
            "The composition communicates freshness, quality nutrition, and proper serving presentation for pet owners."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="pet_food",
        sub_category_name="寵物食品",
    ),
    SceneTemplate(
        id="pet_food_02_ingredients",
        name="成分展示",
        name_en="Ingredients Showcase",
        product_type="pets",
        description="寵物食品搭配真實肉類蔬菜展示成分來源",
        prompt=(
            "This pet food package surrounded by its key natural ingredients: fresh chicken breast, salmon fillet, sweet potato, blueberries, and spinach leaves. "
            "The ingredients are arranged in a semicircle around the product on a clean white marble surface. "
            "Each ingredient is fresh, vibrant, and photogenic, conveying the premium quality of the food's recipe. "
            "Shot from directly overhead at f/6.3 with a 50mm lens, even softbox lighting ensuring accurate color reproduction. "
            "The pet food package is centered with its label clearly readable, surrounded by the real food ingredients. "
            "The composition builds trust by visually connecting the packaged product to wholesome, recognizable natural ingredients."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="pet_food",
        sub_category_name="寵物食品",
    ),
    SceneTemplate(
        id="pet_food_03_pouring",
        name="倒出展示",
        name_en="Pouring Display",
        product_type="pets",
        description="食品從包裝倒出的動態展示",
        prompt=(
            "This pet food being poured from its package into a clean pet bowl, captured in a dynamic mid-pour moment. "
            "The kibble cascades in a stream from the tilted bag, with individual pieces frozen in mid-air showing their shape and coating. "
            "The package label is partially visible and clearly branded as the source. "
            "Shot at 85mm f/4.0 with a fast shutter speed of 1/1000s to freeze the falling food mid-motion. "
            "Professional studio lighting with a key light from the upper left and a fill light to illuminate the falling pieces. "
            "The dynamic composition conveys freshness, generous portions, and the satisfying ritual of feeding time."
        ),
        aspect_ratio="3:4",
        injection_level="light",
        sub_category="pet_food",
        sub_category_name="寵物食品",
    ),
    SceneTemplate(
        id="pet_food_04_happy_pet",
        name="寵物進食",
        name_en="Happy Pet Eating",
        product_type="pets",
        description="寵物開心享用食品的溫馨場景",
        prompt=(
            "A happy, healthy dog or cat eagerly eating this pet food from a bowl in a bright, clean kitchen setting. "
            "The pet's body language conveys enthusiasm: tail up, ears forward, head lowered to the bowl with visible enjoyment. "
            "The product package is positioned nearby on the kitchen counter, label facing the camera for brand visibility. "
            "Shot at 70mm f/2.8 from the pet's eye level, creating an intimate perspective with the kitchen blurred softly behind. "
            "Warm natural morning light streaming through a window bathes the scene in a wholesome 5800K glow. "
            "The image tells a story of mealtime joy and the trust pet owners place in choosing quality nutrition."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_food",
        sub_category_name="寵物食品",
    ),
    SceneTemplate(
        id="pet_food_05_nutrition",
        name="營養標示",
        name_en="Nutrition Info",
        product_type="pets",
        description="包裝背面營養標示的清晰展示",
        prompt=(
            "The back panel of this pet food package displayed at a slight 10-degree angle, with the nutrition facts and ingredient list clearly legible. "
            "The package is propped upright on a clean white surface with a small measuring scoop of food beside it for feeding guide context. "
            "Shot at 90mm f/7.1 for edge-to-edge sharpness ensuring every line of text is readable in the final image. "
            "Even dual softbox lighting at 45 degrees from both sides eliminates glare and reflection on the package surface. "
            "A subtle shadow grounds the package naturally on the white background. "
            "Clean, informative product photography designed to help pet owners make informed nutrition decisions before purchase."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="pet_food",
        sub_category_name="寵物食品",
    ),
    # ==================== pet_toys (寵物玩具) ====================
    SceneTemplate(
        id="pet_toy_01_playing",
        name="玩耍場景",
        name_en="Playing Scene",
        product_type="pets",
        description="寵物正在開心玩耍玩具的活潑場景",
        prompt=(
            "An energetic dog or playful cat actively engaged with this pet toy in a bright living room or sunny backyard. "
            "The pet is mid-play: tugging, chasing, pouncing, or fetching the toy with visible excitement and joy. "
            "Motion blur on the pet's tail or paws conveys dynamic energy while the toy remains in sharp focus. "
            "Shot at 70mm f/2.8 with a fast shutter speed to capture the action, camera at the pet's eye level. "
            "Warm natural afternoon light creates a cheerful, lively atmosphere with golden highlights on the pet's fur. "
            "The composition captures the irresistible fun factor that makes this toy a must-have for engaged pet owners."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_toys",
        sub_category_name="寵物玩具",
    ),
    SceneTemplate(
        id="pet_toy_02_durable",
        name="耐咬展示",
        name_en="Durability Showcase",
        product_type="pets",
        description="展示玩具耐用材質與咬合設計的特寫",
        prompt=(
            "A close-up of this pet toy showing its durable construction: reinforced stitching, tough rubber compound, or multi-layer fabric. "
            "The toy is photographed at a slight angle on a clean white surface revealing its texture, thickness, and build quality. "
            "One section is gently compressed or stretched to demonstrate the material's resilience and bounce-back. "
            "Shot at 100mm macro f/4.0 with ring light illumination highlighting the surface texture and construction details. "
            "Focus stacking ensures the entire toy surface is razor-sharp from front to back. "
            "The image communicates long-lasting durability and safe, non-toxic materials that withstand aggressive chewing."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="pet_toys",
        sub_category_name="寵物玩具",
    ),
    SceneTemplate(
        id="pet_toy_03_variety",
        name="系列展示",
        name_en="Toy Collection",
        product_type="pets",
        description="多款玩具的系列排列展示",
        prompt=(
            "A collection of pet toys from this product line arranged in a visually appealing grid or circular pattern on a clean white surface. "
            "Five to seven toys in different shapes, colors, and sizes are spaced evenly, showing the full range of the collection. "
            "The hero toy is positioned in the center, slightly larger or elevated on a small platform. "
            "Shot directly overhead at f/8 with a 50mm lens and even diffused lighting from two overhead softboxes. "
            "Each toy casts a subtle, consistent shadow for depth without obscuring neighboring items. "
            "The arrangement highlights the variety and playfulness of the entire toy line, encouraging multi-piece purchases."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="pet_toys",
        sub_category_name="寵物玩具",
    ),
    SceneTemplate(
        id="pet_toy_04_indoor",
        name="室內場景",
        name_en="Indoor Scene",
        product_type="pets",
        description="玩具放在客廳地板上的居家場景",
        prompt=(
            "This pet toy placed on a soft living room rug next to a cozy sofa, creating a warm indoor play environment. "
            "A pet bed is visible in the corner, and natural light filters through sheer curtains casting soft patterns on the floor. "
            "The toy is the sharp focal point in the foreground, positioned as if just dropped during a play session. "
            "Shot at 35mm f/2.4 from a low ground-level angle, giving the viewer a pet's-eye perspective of the room. "
            "Warm interior lighting at 4500K creates a comfortable, homey atmosphere with soft amber tones. "
            "The scene communicates that this toy belongs naturally in a stylish, modern pet-friendly home."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_toys",
        sub_category_name="寵物玩具",
    ),
    SceneTemplate(
        id="pet_toy_05_size",
        name="尺寸展示",
        name_en="Size Reference with Pet",
        product_type="pets",
        description="玩具與寵物的尺寸對比展示",
        prompt=(
            "This pet toy photographed next to a medium-sized dog or cat to clearly demonstrate the toy's proportional size. "
            "The pet sits calmly beside the toy on a clean neutral surface, both facing the camera. "
            "A standard tennis ball is also included as a universal size reference point. "
            "Shot at 50mm f/5.6 from a 20-degree elevated angle with even studio lighting from both sides. "
            "Both the pet and toy are in sharp focus, with a clean light gray background behind. "
            "The composition helps online shoppers instantly understand whether this toy is appropriately sized for their pet's breed and weight."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_toys",
        sub_category_name="寵物玩具",
    ),
    # ==================== pet_clothing (寵物服飾) ====================
    SceneTemplate(
        id="pet_cloth_01_wearing",
        name="穿著展示",
        name_en="Pet Wearing Outfit",
        product_type="pets",
        description="寵物穿戴服飾的正面展示照",
        prompt=(
            "An adorable dog or cat wearing this pet clothing item, standing or sitting in a natural pose on a clean studio backdrop. "
            "The garment fits well, with the cut, pattern, and details clearly visible from a front three-quarter angle. "
            "The pet looks comfortable and confident, ears perked and expression relaxed. "
            "Shot at 85mm f/3.2 with professional pet photography lighting: key light at 45 degrees with catchlight in the pet's eyes. "
            "Soft beige or white background with gentle gradient, the pet and outfit in crisp focus. "
            "The image showcases the clothing's fit, style, and the pet's comfort, building buyer confidence in the product."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="pet_clothing",
        sub_category_name="寵物服飾",
    ),
    SceneTemplate(
        id="pet_cloth_02_seasonal",
        name="季節場景",
        name_en="Seasonal Outdoor Scene",
        product_type="pets",
        description="寵物穿著季節性服飾的戶外場景",
        prompt=(
            "A pet wearing this seasonal clothing item outdoors in a setting that matches the season: autumn leaves, winter snow, or spring flowers. "
            "The pet stands on a park path or garden walkway, the seasonal environment providing natural context for the outfit. "
            "Shot at 70mm f/2.8 from eye level, the pet and outfit sharply focused against beautifully blurred seasonal bokeh. "
            "Natural golden hour light enhances the seasonal colors and the garment's texture and details. "
            "The pet's body language is relaxed and happy, demonstrating comfortable movement in the clothing. "
            "The composition connects the outfit to its intended season, helping buyers envision their pet wearing it in real-world conditions."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_clothing",
        sub_category_name="寵物服飾",
    ),
    SceneTemplate(
        id="pet_cloth_03_flat_lay",
        name="平鋪展示",
        name_en="Flat Lay Display",
        product_type="pets",
        description="服飾平鋪搭配配件的展示拍攝",
        prompt=(
            "This pet clothing item laid flat on a clean white surface, neatly arranged to show its full shape, pattern, and construction. "
            "Matching accessories like a leash, bandana, bow tie, or collar are arranged harmoniously around the garment. "
            "The clothing is smoothed and styled to display design details: buttons, zippers, reflective strips, or embroidery. "
            "Shot directly overhead at f/7.1 with a 50mm lens and even diffused softbox lighting for shadow-free coverage. "
            "Each item is spaced with intentional precision in a balanced composition. "
            "Professional flat lay photography that clearly communicates the garment's design, size, and available coordinating accessories."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="pet_clothing",
        sub_category_name="寵物服飾",
    ),
    SceneTemplate(
        id="pet_cloth_04_measurement",
        name="尺寸指南",
        name_en="Measurement Guide",
        product_type="pets",
        description="展示如何量測寵物尺寸以選擇合適服飾",
        prompt=(
            "A gentle demonstration of measuring a calm dog or cat for this pet clothing item using a soft measuring tape. "
            "The tape is wrapped around the pet's chest girth while a person's hands hold it in place, showing the correct measurement technique. "
            "The pet clothing item is laid beside the pet for visual size comparison. "
            "Shot at 50mm f/4.0 from a 30-degree elevated angle with bright, even lighting at 5500K. "
            "Clean neutral background ensures focus remains on the measuring process and the garment. "
            "The educational composition helps buyers understand exactly how to measure their pet for a perfect fit before ordering."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_clothing",
        sub_category_name="寵物服飾",
    ),
    SceneTemplate(
        id="pet_cloth_05_walking",
        name="散步場景",
        name_en="Walking Scene",
        product_type="pets",
        description="寵物穿著服飾散步的動態場景",
        prompt=(
            "A dog wearing this pet clothing item walking happily alongside its owner on a tree-lined sidewalk or park path. "
            "The dog is mid-stride, the clothing moving naturally with its body, demonstrating unrestricted comfortable movement. "
            "The owner is partially visible from the waist down, holding a leash connected to the dressed pet. "
            "Shot at 70mm f/2.8 from a low angle at the dog's eye level, with the path stretching into soft bokeh behind. "
            "Warm golden hour light creates a pleasant walking atmosphere with long gentle shadows. "
            "The image proves the clothing allows full range of motion during daily walks and outdoor activities."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pet_clothing",
        sub_category_name="寵物服飾",
    ),
]

TemplateRegistry.register("pets", PETS_TEMPLATES)
