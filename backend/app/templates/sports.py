from app.templates.registry import SceneTemplate, TemplateRegistry

SPORTS_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="sports_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="sports",
        description="純白背景，運動用品正面展示",
        prompt=(
            "This sports/outdoor product on a pure white background. "
            "Professional product photography with crisp, dynamic lighting. "
            "The product is centered, showing its design and form. "
            "Slight shadow for depth and energy. "
            "Occupies about 80% of the frame. "
            "Shot at f/9 with dual strip softboxes for clean highlights and defined edges. "
            "Clean, athletic commercial photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="sports",
        description="展示材質科技、功能性、耐用度等賣點",
        prompt=(
            "Create a professional sports product infographic. "
            "Show this product on a clean white or dark gradient background. "
            "Add dynamic callout elements pointing to key performance features: "
            "material technology (breathable, waterproof, lightweight), "
            "ergonomic design, durability, and any special performance features. "
            "Bold, sporty typography with energetic design. "
            "Flat even lighting to ensure all text and annotations remain sharp. "
            "Nike/Under Armour product page aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="sports",
        description="材質科技、拉鏈、縫線等細節特寫",
        prompt=(
            "Extreme close-up of this sports product showing material technology and build quality. "
            "Focus on: fabric technology (mesh ventilation, waterproof coating), "
            "reinforced stress points, zipper/buckle quality, grip textures. "
            "Macro photography with dramatic lighting emphasizing durability. "
            "Shot at f/3.5 with a 100mm macro lens to reveal fiber weave and stitching detail. "
            "Professional sports equipment detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="sports",
        description="穿戴/使用時展示大小比例",
        prompt=(
            "This sports product shown being worn or used by a person to demonstrate size. "
            "A fit person wearing or holding the product in a neutral studio setting. "
            "Clean background, the product's size relative to the body is clear. "
            "Shows how the product fits and looks in real use. "
            "Shot at eye level with a 50mm lens for natural body proportions. "
            "Athletic model photography for size reference."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_05_gym_scene",
        name="健身場景",
        name_en="Gym/Fitness Scene",
        product_type="sports",
        description="健身房/瑜伽室使用場景",
        prompt=(
            "This sports product in a modern gym or fitness studio setting. "
            "A person actively using the product during a workout. "
            "Dynamic angle capturing movement and energy. "
            "Clean, well-lit gym with professional equipment in background. "
            "Shot from a low three-quarter angle at f/2.8 to freeze motion with shallow depth of field. "
            "The product is the focal point during active use. "
            "Energetic sports lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_06_outdoor_action",
        name="戶外運動場景",
        name_en="Outdoor Action",
        product_type="sports",
        description="戶外跑步/登山/運動中使用場景",
        prompt=(
            "This sports product in an outdoor action setting: "
            "a trail, mountain path, beach, or open field. "
            "A person actively using the product in motion. "
            "Dynamic composition with sense of movement and adventure. "
            "Natural golden hour or bright daylight. "
            "Captured with a fast shutter speed at f/2.8, slight motion blur on limbs to convey speed. "
            "Inspirational outdoor fitness photography. "
            "The product enables peak performance."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_07_model_wearing",
        name="模特展示",
        name_en="Model Showcase",
        product_type="sports",
        description="模特穿戴展示，展示運動造型",
        prompt=(
            "An athletic model showcasing this sports product in a confident, powerful pose. "
            "Clean studio background with dramatic sports lighting. "
            "The model embodies fitness and determination. "
            "The product is prominently displayed and is the hero element. "
            "Lit with a hard key light and rim light at f/4 for chiseled contrast on the product. "
            "Professional sports apparel/gear campaign photography. "
            "Motivational and aspirational."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_08_equipment_combo",
        name="裝備搭配圖",
        name_en="Equipment Combo",
        product_type="sports",
        description="與其他運動裝備搭配展示",
        prompt=(
            "This sports product arranged with complementary fitness/outdoor gear "
            "in a motivational flat lay composition. "
            "Include items like water bottle, fitness tracker, towel, resistance band, or shoes. "
            "Clean surface (gym mat or light background). "
            "Top-down organized arrangement showing a complete workout kit. "
            "Shot overhead at f/7.1 with even softbox lighting for uniform sharpness across the spread. "
            "Energetic, goal-oriented fitness photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="sports_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="sports",
        description="展示健康活力生活方式",
        prompt=(
            "This sports product in an aspirational active lifestyle scene. "
            "A person with the product in a scenic outdoor location: "
            "mountain summit, beach sunrise, or urban rooftop. "
            "The image conveys achievement, health, and adventure. "
            "Cinematic composition with dramatic natural lighting. "
            "Wide-angle lens at f/4 with the subject silhouetted against a vivid sky for epic scale. "
            "Premium sportswear brand campaign aesthetic. "
            "Motivational and empowering."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== yoga (瑜伽) ====================
    SceneTemplate(
        id="sport_yoga_01_mat_pose",
        name="瑜伽墊姿勢",
        name_en="Yoga Mat Pose",
        product_type="sports",
        description="模特在瑜伽墊上做瑜伽姿勢",
        prompt=(
            "A model performing a graceful yoga pose on this yoga product in a serene, minimalist studio with light wood floors and floor-to-ceiling windows. "
            "The model holds a balanced warrior or tree pose, showcasing how the product supports and enhances the practice with stability and grip. "
            "Soft, diffused natural light pours through the windows creating long, gentle shadows and a calm, meditative atmosphere throughout the space. "
            "The yoga product's texture, thickness, and color are clearly visible beneath the model's hands and feet. "
            "Shot at 35mm f/2.8 from a low side angle to capture the full body pose, the mat surface detail, and the peaceful studio environment."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="yoga",
        sub_category_name="瑜伽",
    ),
    SceneTemplate(
        id="sport_yoga_02_props",
        name="輔助道具",
        name_en="Yoga Props Arrangement",
        product_type="sports",
        description="瑜伽磚、拉力帶、抱枕等輔助道具排列",
        prompt=(
            "A curated arrangement of yoga props including blocks, straps, bolsters, and this product neatly organized on a cork or bamboo surface in a bright yoga studio. "
            "Each prop is positioned with intentional spacing and angles to show its unique shape, color, and purpose in a yoga practice. "
            "The arrangement suggests a complete yoga toolkit, with the hero product placed centrally and slightly forward for visual emphasis. "
            "Even, warm overhead lighting fills the composition with a balanced glow that reveals material textures on each prop surface. "
            "Shot at 50mm f/5.6 from a 45-degree elevated angle to capture the depth and dimensionality of each prop in the organized layout."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="yoga",
        sub_category_name="瑜伽",
    ),
    SceneTemplate(
        id="sport_yoga_03_studio",
        name="瑜伽教室",
        name_en="Yoga Studio Setting",
        product_type="sports",
        description="明亮瑜伽教室中的產品展示",
        prompt=(
            "This yoga product placed in a beautiful, bright yoga studio with polished bamboo floors, mirrored walls, and abundant natural daylight streaming through large windows. "
            "The studio is clean and spacious with a few other rolled mats and props neatly stored on shelves in the background, establishing the professional practice environment. "
            "The product is unrolled or positioned in its ready-to-use state at the center of the studio floor, inviting the viewer to step onto it. "
            "Bright, airy lighting with high color temperature creates an energizing, uplifting atmosphere associated with morning yoga practice. "
            "Shot at 24mm f/4 from a low angle near floor level to capture the expansive studio space with the product as the welcoming focal point."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="yoga",
        sub_category_name="瑜伽",
    ),
    SceneTemplate(
        id="sport_yoga_04_outdoor",
        name="戶外瑜伽",
        name_en="Outdoor Yoga Practice",
        product_type="sports",
        description="在自然環境中練習瑜伽的場景",
        prompt=(
            "A model practicing yoga with this product in a stunning outdoor setting such as a wooden deck overlooking mountains, a beach at sunrise, or a peaceful garden. "
            "The model is in a meditative seated pose or gentle stretch, with the natural landscape creating a breathtaking backdrop of greens, blues, and golden light. "
            "Early morning or golden hour sunlight creates warm rim lighting on the model's silhouette and highlights the product's surface texture. "
            "The outdoor environment conveys freedom, mindfulness, and connection with nature as integral to the yoga experience. "
            "Shot at 35mm f/2.8 from a wide angle to capture both the model on the product and the expansive natural scenery behind."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="yoga",
        sub_category_name="瑜伽",
    ),
    SceneTemplate(
        id="sport_yoga_05_rolled",
        name="捲起收納",
        name_en="Rolled Storage Display",
        product_type="sports",
        description="瑜伽墊捲起搭配背帶展示",
        prompt=(
            "This yoga mat tightly rolled and secured with its carrying strap or sling, displayed upright on a clean surface next to a water bottle and a small towel. "
            "The rolled mat shows its thickness profile, color, and the quality of the carrying strap hardware including buckles and adjustable straps. "
            "The compact, portable configuration suggests convenience for commuting to the studio or traveling with the mat. "
            "Clean studio lighting with a single key light from the left highlights the cylindrical shape and strap details with defined shadows. "
            "Shot at 60mm f/4 from a three-quarter eye-level angle to show both the rolled diameter and the full length of the carrying strap system."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="yoga",
        sub_category_name="瑜伽",
    ),
    # ==================== camping (露營) ====================
    SceneTemplate(
        id="sport_camp_01_tent",
        name="帳篷場景",
        name_en="Campsite Tent Scene",
        product_type="sports",
        description="產品在帳篷或營地旁的展示",
        prompt=(
            "This camping product positioned near a pitched tent at a scenic campsite surrounded by tall pine trees and a distant mountain range. "
            "The tent is set up on flat ground with a campfire ring nearby, and the product is placed prominently in the foreground as essential camping gear. "
            "Warm late-afternoon sunlight filters through the tree canopy, casting dappled golden light on the campsite and the product surface. "
            "The scene evokes adventure, self-reliance, and the beauty of outdoor living with authentic camping accessories visible around the site. "
            "Shot at 28mm f/4 from a low ground-level angle to make the product appear heroic against the towering trees and expansive sky."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="camping",
        sub_category_name="露營",
    ),
    SceneTemplate(
        id="sport_camp_02_night",
        name="夜間使用",
        name_en="Nighttime Camping Use",
        product_type="sports",
        description="營火或燈籠旁的夜間使用場景",
        prompt=(
            "This camping product illuminated by the warm flickering glow of a campfire and a hanging LED lantern at a nighttime campsite under a star-filled sky. "
            "The fire's amber light creates dramatic, warm highlights on the product surface while the surrounding darkness adds mystery and adventure. "
            "A tent glows softly in the background from an interior light, and camping chairs or a log bench are visible beside the fire. "
            "The night sky above shows scattered stars and possibly the Milky Way, establishing the remote wilderness atmosphere. "
            "Shot at 24mm f/2.0 with a slow shutter to capture both the warm firelight on the product and the natural starlight in the sky above."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="camping",
        sub_category_name="露營",
    ),
    SceneTemplate(
        id="sport_camp_03_packing",
        name="收納打包",
        name_en="Packing and Storage",
        product_type="sports",
        description="露營裝備收納到背包中的展示",
        prompt=(
            "This camping gear being packed into or displayed next to an open hiking backpack on a clean surface, showing how compactly it fits for travel. "
            "The backpack is partially loaded with other camping essentials visible like a water bladder, first aid kit, and rain cover, demonstrating packing context. "
            "The product is shown both in its packed compressed form and alongside its full-size deployed form for size comparison. "
            "Bright, clean studio lighting ensures the packing details, compression straps, and storage bag are all clearly visible. "
            "Shot at 50mm f/5.6 from a slightly elevated angle to show the backpack interior, the product's packed size, and the complete packing arrangement."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="camping",
        sub_category_name="露營",
    ),
    SceneTemplate(
        id="sport_camp_04_cooking",
        name="野炊場景",
        name_en="Outdoor Cooking Scene",
        product_type="sports",
        description="戶外野炊搭配露營廚具的場景",
        prompt=(
            "This camping cooking product in active use at an outdoor campsite with a portable stove, fresh ingredients, and rustic cookware arranged on a folding camp table. "
            "Steam rises from a pot or pan as food is being prepared in the wilderness, with chopped vegetables and spices laid out on a cutting board nearby. "
            "The forest clearing setting features tall trees and a glimpse of a lake or meadow in the blurred background for scenic outdoor context. "
            "Warm, natural late-afternoon sunlight from the side highlights the steam and creates appetizing golden tones on the food and cookware. "
            "Shot at 40mm f/3.5 from table height to capture the cooking action, food details, and the beautiful outdoor setting in a single immersive frame."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="camping",
        sub_category_name="露營",
    ),
    SceneTemplate(
        id="sport_camp_05_nature",
        name="自然環境",
        name_en="Natural Environment Setting",
        product_type="sports",
        description="在山林自然環境中的產品展示",
        prompt=(
            "This camping product placed on a mossy rock or fallen log in a pristine mountain forest setting with a rushing stream or waterfall visible nearby. "
            "Lush green ferns, wildflowers, and towering old-growth trees frame the composition with rich natural textures and vibrant green tones. "
            "Soft, dappled forest light filters through the canopy creating natural spotlight patches on the product and surrounding mossy surfaces. "
            "Morning mist or humidity hangs faintly in the air, adding atmospheric depth and a sense of untouched wilderness. "
            "Shot at 35mm f/4 from a low angle near ground level to present the product embedded in the forest landscape with a majestic, adventurous perspective."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="camping",
        sub_category_name="露營",
    ),
    # ==================== fitness (健身) ====================
    SceneTemplate(
        id="sport_fit_01_gym",
        name="健身房場景",
        name_en="Gym Environment",
        product_type="sports",
        description="產品在健身房環境中的展示",
        prompt=(
            "This fitness product placed in a modern, well-equipped gym with polished floors, mirror walls, and rows of professional weight racks and machines in the background. "
            "The product is positioned on a gym bench or rubber floor mat as the central focus piece, with dumbbells and a water bottle nearby for context. "
            "Cool, crisp overhead fluorescent gym lighting mixed with warmer accent lights creates an energetic, motivating commercial gym atmosphere. "
            "The mirror in the background reflects the product from another angle, adding visual depth and showcasing the product from multiple perspectives. "
            "Shot at 35mm f/2.8 from a low three-quarter angle to make the product feel powerful and prominent in the professional fitness environment."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="fitness",
        sub_category_name="健身",
    ),
    SceneTemplate(
        id="sport_fit_02_workout",
        name="運動中使用",
        name_en="Active Workout Use",
        product_type="sports",
        description="模特在運動中使用產品的場景",
        prompt=(
            "An athletic model actively using this fitness product during an intense workout, captured mid-repetition with visible muscle engagement and determination. "
            "The model's form demonstrates proper technique with the product, showing both the functional use and ergonomic design in real action. "
            "Dynamic gym lighting with a hard key light from above creates sculpted shadows on the model's physique and dramatic highlights on the product surface. "
            "A slight motion blur on the moving parts conveys energy and power while the product remains tack-sharp to emphasize its build quality. "
            "Shot at 70mm f/2.8 from a slightly low angle to capture the powerful movement and the product interaction in a motivational sports campaign composition."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="fitness",
        sub_category_name="健身",
    ),
    SceneTemplate(
        id="sport_fit_03_home_gym",
        name="居家健身",
        name_en="Home Gym Setting",
        product_type="sports",
        description="居家健身環境中的產品展示",
        prompt=(
            "This fitness product set up in a clean, organized home gym corner of a modern apartment with a yoga mat, small weight rack, and wall-mounted mirror. "
            "The space is compact but well-designed, showing how the product fits perfectly into a home workout environment without taking excessive room. "
            "Large windows provide bright natural daylight that fills the space with an energizing, fresh morning workout atmosphere. "
            "A towel draped over a chair, a smartphone with a workout app, and a water bottle complete the relatable home fitness setup. "
            "Shot at 28mm f/4 from a wide angle to capture the entire home gym context with the product as the centerpiece of the personal fitness space."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="fitness",
        sub_category_name="健身",
    ),
    SceneTemplate(
        id="sport_fit_04_resistance",
        name="阻力訓練",
        name_en="Resistance Training",
        product_type="sports",
        description="阻力帶或重量訓練中的使用展示",
        prompt=(
            "A fit model performing a resistance exercise using this fitness product, with visible tension in the band or controlled weight movement showing proper form. "
            "The exercise demonstrates a common workout movement like a bicep curl, squat, or lateral raise with the product clearly integrated into the motion. "
            "Clean gym or home workout background with focused lighting that highlights the product's stretch, grip texture, or weight markings during active use. "
            "The model's engaged expression and controlled posture communicate proper technique and the product's effectiveness for strength training. "
            "Shot at 50mm f/3.5 from a side angle to show the full range of motion, product extension under load, and the model's form in a single dynamic frame."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="fitness",
        sub_category_name="健身",
    ),
    SceneTemplate(
        id="sport_fit_05_recovery",
        name="恢復放鬆",
        name_en="Post-Workout Recovery",
        product_type="sports",
        description="運動後恢復放鬆時使用產品的場景",
        prompt=(
            "A model using this fitness recovery product in a calm post-workout setting, seated on a gym mat or living room floor with relaxed body language. "
            "The model is using the product for stretching, foam rolling, or muscle recovery with a peaceful, satisfied expression after completing a workout. "
            "Warm, soft lighting creates a soothing atmosphere contrasting with the typical high-energy gym photography, emphasizing rest and recovery. "
            "A water bottle, towel, and perhaps a protein shake in the background suggest the transition from active exercise to intentional recovery. "
            "Shot at 50mm f/2.4 from a low, intimate angle to capture the quiet, restorative moment with the product as the key recovery tool."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="fitness",
        sub_category_name="健身",
    ),
]

TemplateRegistry.register("sports", SPORTS_TEMPLATES)
