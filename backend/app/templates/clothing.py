from app.templates.registry import SceneTemplate, TemplateRegistry

CLOTHING_TEMPLATES = [
    # ===== Common (通用場景) =====
    SceneTemplate(
        id="clothing_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="clothing",
        description="純白背景，服裝平鋪或掛拍，展示整體設計",
        prompt=(
            "This clothing item displayed on a pure white background. "
            "Professional e-commerce flat lay or ghost mannequin photography. "
            "The garment is neatly arranged showing its full shape and design. "
            "Crisp studio lighting with dual strip softboxes at 45 degrees for even, wrinkle-free illumination. "
            "Centered composition, the clothing occupies about 85% of the frame. "
            "Shot overhead at 90 degrees with a 50mm lens at f/8 for maximum sharpness. "
            "Ultra-clean, commercial quality fashion photography."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="clothing",
        description="展示面料、版型、口袋等設計亮點",
        prompt=(
            "Create a professional fashion infographic for this clothing item. "
            "Display the garment on a clean white background with elegant callout lines "
            "pointing to 3-4 key features: fabric composition and feel, "
            "special design details (collar, buttons, pockets), fit and cut style, "
            "and any functional features (stretch, waterproof, pockets). "
            "Modern minimalist design with clean typography. "
            "Lit with a large overhead softbox for flat, shadow-free detail rendering. "
            "Style reference: Uniqlo or Muji product detail page."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_03_detail_closeup",
        name="細節特寫",
        name_en="Fabric & Detail Close-up",
        product_type="clothing",
        description="面料紋理、車縫線、鈕扣等細節特寫",
        prompt=(
            "Extreme close-up of this clothing item showing fabric texture and construction quality. "
            "Multiple detail zones: fabric weave/knit texture, stitching quality, "
            "button or zipper hardware, collar/cuff finishing. "
            "Macro photography with a 100mm macro lens at f/5.6, sharp focus revealing material quality. "
            "Directional side lighting from a focused spot at a low angle to emphasize weave texture and thread detail. "
            "Professional product photography lighting that emphasizes texture. "
            "The viewer should be able to appreciate the fabric quality."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_04_size_reference",
        name="尺寸版型圖",
        name_en="Size & Fit Guide",
        product_type="clothing",
        description="展示衣長、肩寬、胸圍等尺寸標註",
        prompt=(
            "This clothing item laid flat on a clean white surface with clear measurement reference points. "
            "Show the garment from the front with visual indicators for key measurements: "
            "shoulder width, chest width, body length, and sleeve length. "
            "Clean, diagram-like presentation with the garment neatly spread. "
            "A measuring tape or ruler visible for scale reference. "
            "Shot directly overhead at 90 degrees with a wide-angle lens at f/11 for corner-to-corner sharpness. "
            "Professional technical flat lay photography."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_05_daily_scene",
        name="日常穿搭",
        name_en="Daily Outfit",
        product_type="clothing",
        description="日常穿著場景，展示搭配效果",
        prompt=(
            "A model wearing this clothing item in a casual daily setting: "
            "walking on a clean city street, sitting in a bright cafe, or at a modern office. "
            "Natural, relaxed pose that shows how the garment drapes and fits in real life. "
            "Natural daylight photography with soft shadows. "
            "Shot at f/2.8 with an 85mm lens for a pleasing background bokeh that isolates the model. "
            "Camera at eye level for a natural, relatable perspective. "
            "The outfit is styled with simple complementary pieces. "
            "Lifestyle fashion photography that helps buyers visualize wearing it."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_06_styled_scene",
        name="穿搭場景",
        name_en="Styled Look",
        product_type="clothing",
        description="精心搭配的穿搭造型，展示不同風格",
        prompt=(
            "A fashion editorial style shot of a model wearing this clothing item "
            "as part of a complete, carefully curated outfit. "
            "The setting is a stylish location: rooftop, art gallery, or boutique hotel. "
            "Professional fashion photography with creative lighting using a key light with beauty dish and rim light for separation. "
            "Shot from a slightly low angle at f/4 with a 70mm lens to add presence and stature to the model. "
            "The image conveys a specific style mood: sophisticated, casual-chic, or trendy. "
            "Magazine-quality composition and color grading."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_07_model_front_back",
        name="正反面展示",
        name_en="Front & Back View",
        product_type="clothing",
        description="模特正面和背面，展示完整版型",
        prompt=(
            "A model showcasing this clothing item from the front view, "
            "standing with a natural, confident pose against a clean studio background. "
            "Full body shot from head to mid-thigh showing the complete garment silhouette. "
            "Even studio lighting with a large parabolic softbox as key and two strip lights for edge definition. "
            "Shot at f/5.6 with a 70mm lens at waist height for accurate body proportions without distortion. "
            "The model's pose clearly shows the fit, drape, and proportions of the garment. "
            "Professional fashion catalog photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_08_flat_lay_combo",
        name="平鋪搭配圖",
        name_en="Flat Lay Styling",
        product_type="clothing",
        description="衣服與配件平鋪搭配，展示整套造型",
        prompt=(
            "This clothing item in a stylish flat lay arrangement with complementary accessories: "
            "shoes, bag, belt, watch, sunglasses, and/or jewelry. "
            "Neatly arranged on a clean white or light wood surface. "
            "Top-down photography shot at exactly 90 degrees overhead with a 35mm lens at f/8. "
            "Cohesive color palette, fashion mood board aesthetic. "
            "Bright, even lighting from a large rectangular softbox directly above. Each item placed with intentional spacing."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="clothing_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="clothing",
        description="展示品牌調性的質感穿搭照",
        prompt=(
            "A model wearing this clothing item in an aspirational lifestyle setting. "
            "The scene conveys the brand's aesthetic: could be a minimalist apartment, "
            "a sunlit garden, or an urban rooftop at golden hour. "
            "Cinematic color grading with warm tones. "
            "Shot at f/2.0 with a 50mm prime lens for a cinematic shallow depth of field. "
            "Camera positioned at a candid three-quarter angle to capture movement and atmosphere. "
            "The clothing is the star but the environment tells a story. "
            "High-end fashion brand campaign photography aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ===== Tops (上衣) =====
    SceneTemplate(
        id="cloth_top_01_flat_lay",
        name="平鋪展示",
        name_en="Top Flat Lay",
        product_type="clothing",
        description="上衣平鋪搭配配飾的精緻擺拍展示",
        prompt=(
            "This top garment laid flat in a curated flat lay arrangement on a clean white surface. "
            "The top is neatly spread showing its full shape, collar, and sleeve design. "
            "Styled with complementary accessories placed around it: a pair of sunglasses near the collar, "
            "a minimalist watch beside one sleeve, and a small clutch bag at the bottom. "
            "Shot from directly overhead at 90 degrees with a 35mm lens at f/8 for uniform sharpness. "
            "Bright, even lighting from a large rectangular overhead softbox. "
            "The arrangement follows a balanced composition with intentional white space. "
            "Fashion mood board aesthetic that inspires outfit combinations."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="tops",
        sub_category_name="上衣",
    ),
    SceneTemplate(
        id="cloth_top_02_hanger",
        name="衣架展示",
        name_en="Hanger Display",
        product_type="clothing",
        description="上衣掛在高級木質衣架上的展示",
        prompt=(
            "This top displayed on a premium natural wood hanger against a clean white or light gray wall. "
            "The hanger is a thick, sculpted wooden design that gives the garment a boutique feel. "
            "The top drapes naturally from the hanger, showing its silhouette and fabric weight. "
            "Shot straight-on at eye level with a 85mm lens at f/4. "
            "Soft directional lighting from the left using a large strip softbox, "
            "creating gentle shadows that reveal the fabric's drape and texture. "
            "A subtle shadow of the hanger on the wall adds depth. "
            "Minimalist retail presentation photography for premium fashion e-commerce."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="tops",
        sub_category_name="上衣",
    ),
    SceneTemplate(
        id="cloth_top_03_tucked_in",
        name="紮入穿搭",
        name_en="Tucked-In Style",
        product_type="clothing",
        description="模特將上衣紮入褲子的穿搭展示",
        prompt=(
            "A model wearing this top neatly tucked into high-waisted trousers or a skirt. "
            "Shot from waist up showing the tucked-in styling that defines the waistline. "
            "The model stands in a natural, confident three-quarter pose. "
            "Clean studio background in soft neutral beige. "
            "Fashion lighting with a key softbox at 45 degrees and a fill reflector for gentle shadow control. "
            "Shot at f/4 with a 70mm lens at waist height. "
            "The image clearly shows how the top looks when styled tucked in, "
            "including the fabric's behavior at the waist and the overall silhouette proportion. "
            "Modern fashion catalog photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="tops",
        sub_category_name="上衣",
    ),
    SceneTemplate(
        id="cloth_top_04_layering",
        name="層次搭配",
        name_en="Layering Look",
        product_type="clothing",
        description="上衣搭配外套或開衫的層次穿搭展示",
        prompt=(
            "A model wearing this top layered under an open jacket, cardigan, or blazer. "
            "The outer layer is unbuttoned or unzipped to clearly reveal the top underneath. "
            "Shot from chest level up in a three-quarter front angle. "
            "The layering creates visual depth and shows how the top works as a versatile base piece. "
            "Clean studio or minimal indoor setting. "
            "Professional fashion lighting with a large octabox key light and edge light for separation. "
            "Shot at f/3.5 with a 85mm lens for subject isolation. "
            "The image demonstrates the top's layering versatility and inspires styling ideas."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="tops",
        sub_category_name="上衣",
    ),
    SceneTemplate(
        id="cloth_top_05_fabric_detail",
        name="面料特寫",
        name_en="Fabric Detail",
        product_type="clothing",
        description="上衣面料紋理與編織工藝的微距特寫",
        prompt=(
            "Extreme macro close-up of this top's fabric, showing the weave pattern, yarn quality, and texture at high magnification. "
            "The fabric fills the entire frame, revealing whether it is woven, knitted, ribbed, or has a special finish. "
            "Shot with a 100mm macro lens at f/5.6 with focus stacking for maximum sharpness across the fabric surface. "
            "Directional raking light from the right side at a very low 10-degree angle to accentuate every thread and fiber. "
            "The color accuracy is precise, showing the true hue without any cast. "
            "A secondary overhead diffused fill prevents excessive contrast. "
            "Professional textile detail photography that communicates the fabric's quality and hand-feel."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="tops",
        sub_category_name="上衣",
    ),
    # ===== Pants (褲裝) =====
    SceneTemplate(
        id="cloth_pants_01_full_body",
        name="全身展示",
        name_en="Full Body Shot",
        product_type="clothing",
        description="模特穿著褲裝的全身展示，展示整體比例",
        prompt=(
            "A model wearing these pants in a full-body standing shot from head to shoes. "
            "Natural, relaxed standing pose with weight on one leg for a casual silhouette. "
            "The pants' fit, drape, and length are clearly visible from waist to ankle. "
            "Clean studio background in light gray or white. "
            "Even studio lighting with a large parabolic softbox as key light and two strip lights for edge definition. "
            "Shot at f/5.6 with a 50mm lens at waist height to avoid perspective distortion. "
            "The model wears a simple solid-color top that complements but doesn't distract from the pants. "
            "Professional fashion catalog photography showing accurate fit and proportion."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="pants",
        sub_category_name="褲裝",
    ),
    SceneTemplate(
        id="cloth_pants_02_fold_detail",
        name="褲腳細節",
        name_en="Hem Detail",
        product_type="clothing",
        description="褲腳反折、縫邊等細節特寫",
        prompt=(
            "Close-up detail shot of these pants' hem and cuff area. "
            "Show the stitching quality, hem finishing, and any design details like cuff rolls or raw edges. "
            "The pants are worn on a model, shot from knee-down with shoes visible for styling context. "
            "Shot with a 100mm macro lens at f/4 for shallow depth of field isolating the hem detail. "
            "Side lighting from a focused strip softbox at a 30-degree angle to reveal thread texture and construction quality. "
            "Clean floor surface in light wood or white. "
            "The image communicates attention to detail and quality finishing. "
            "Professional garment detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="pants",
        sub_category_name="褲裝",
    ),
    SceneTemplate(
        id="cloth_pants_03_pocket",
        name="口袋展示",
        name_en="Pocket Display",
        product_type="clothing",
        description="展示褲裝口袋設計與實際深度",
        prompt=(
            "A model wearing these pants with one hand casually inserted into the front pocket, "
            "demonstrating the pocket's depth and accessibility. "
            "Shot from waist to mid-thigh at a slightly angled front view. "
            "A smartphone partially visible in the other pocket shows practical capacity. "
            "Clean studio background in neutral off-white. "
            "Soft overhead key light with a gentle side fill to define the pocket contours. "
            "Shot at f/4 with a 70mm lens at hip height. "
            "The image clearly communicates the pocket design, depth, and everyday practicality. "
            "Functional fashion photography for e-commerce."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="pants",
        sub_category_name="褲裝",
    ),
    SceneTemplate(
        id="cloth_pants_04_stretch",
        name="彈力展示",
        name_en="Stretch Demo",
        product_type="clothing",
        description="展示褲裝的彈力與舒適活動度",
        prompt=(
            "A model demonstrating the stretch and flexibility of these pants through natural movement poses. "
            "The model is shown in a mid-step stride or slight lunge, with the fabric visibly stretching around the knee and thigh. "
            "Shot from a side angle at hip height to clearly show the fabric's elastic recovery. "
            "Clean studio backdrop in white. "
            "Dynamic fashion photography lighting with a fast strobe key light for motion-freezing sharpness. "
            "Shot at f/5.6 with a 50mm lens. "
            "The image clearly demonstrates comfort, mobility, and the four-way stretch capability of the fabric. "
            "Active lifestyle fashion photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="pants",
        sub_category_name="褲裝",
    ),
    SceneTemplate(
        id="cloth_pants_05_matching",
        name="上下搭配",
        name_en="Top-Bottom Pairing",
        product_type="clothing",
        description="褲裝搭配不同上衣的穿搭效果展示",
        prompt=(
            "A diptych or split layout showing these pants paired with two different tops for contrasting styles. "
            "Left panel: the pants with a crisp button-down shirt tucked in for a smart casual work look. "
            "Right panel: the same pants with a relaxed graphic t-shirt or hoodie for a casual weekend look. "
            "Both panels show the model from waist to shoes in a natural standing pose. "
            "Consistent studio backdrop and lighting across both panels using matched softboxes at 5500K. "
            "Shot at f/5.6 with a 70mm lens. "
            "The layout demonstrates the pants' versatility for different occasions and personal styles."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pants",
        sub_category_name="褲裝",
    ),
    # ===== Dress (洋裝) =====
    SceneTemplate(
        id="cloth_dress_01_twirl",
        name="裙擺飄動",
        name_en="Dress Twirl",
        product_type="clothing",
        description="模特輕轉身展示洋裝裙擺的飄動效果",
        prompt=(
            "A model in a gentle mid-twirl, the skirt of this dress fanning out beautifully to show its volume and flow. "
            "The model is captured in a graceful spinning motion, with the fabric creating elegant circular movement. "
            "Shot at 1/250s shutter speed to freeze the fabric movement while maintaining a sense of dynamism. "
            "Clean studio background in soft off-white. "
            "Multiple studio strobes: key light from the front, two rim lights from behind to illuminate the flowing fabric edges. "
            "Shot at f/4 with a 50mm lens at waist height. "
            "The image captures the dress's movement, lightness, and feminine grace. "
            "Editorial fashion photography with a joyful, energetic mood."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="dress",
        sub_category_name="洋裝",
    ),
    SceneTemplate(
        id="cloth_dress_02_back",
        name="背面設計",
        name_en="Back Design",
        product_type="clothing",
        description="洋裝背面設計展示，包括拉鏈與剪裁細節",
        prompt=(
            "A model photographed from behind showing the back design of this dress. "
            "The full back view reveals zipper placement, back neckline, strap design, and any cutout or lace details. "
            "The model stands with a natural posture, arms slightly away from the body to show the complete back silhouette. "
            "Clean studio background in light gray. "
            "Professional lighting with a large overhead softbox as fill and two side strip lights to define the dress contours. "
            "Shot at f/5.6 with a 70mm lens at torso height. "
            "Hair is styled up or swept to one side to fully expose the dress back. "
            "Detailed fashion catalog photography showing construction and design from behind."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="dress",
        sub_category_name="洋裝",
    ),
    SceneTemplate(
        id="cloth_dress_03_seated",
        name="坐姿展示",
        name_en="Seated Pose",
        product_type="clothing",
        description="模特坐姿展示洋裝的垂墜與舒適感",
        prompt=(
            "A model seated elegantly on a minimalist chair or bench, wearing this dress. "
            "The seated pose shows how the dress drapes, folds, and falls when sitting. "
            "The model sits with crossed ankles or legs angled to one side for a graceful silhouette. "
            "Shot from a slightly elevated three-quarter angle with a 70mm lens at f/3.5. "
            "Clean studio backdrop in warm beige. "
            "Soft key light from a large octabox at 45 degrees with warm fill for flattering skin tones. "
            "The image demonstrates the dress's comfort and elegance in seated positions, "
            "which is important for buyers considering the garment for dining or office wear."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="dress",
        sub_category_name="洋裝",
    ),
    SceneTemplate(
        id="cloth_dress_04_outdoor",
        name="戶外寫真",
        name_en="Outdoor Portrait",
        product_type="clothing",
        description="洋裝在花園或戶外場景中的自然寫真",
        prompt=(
            "A model wearing this dress in a beautiful outdoor garden setting. "
            "Surrounded by lush green hedges, blooming flowers, or a vine-covered archway. "
            "Golden hour sunlight filtering through leaves creates a warm, romantic atmosphere. "
            "The model walks along a stone path or stands near a garden bench in a natural pose. "
            "Shot at f/2.8 with a 85mm lens for creamy background bokeh that makes the dress pop. "
            "A portable reflector fills shadows on the dress for even detail visibility. "
            "The dress fabric catches the golden light beautifully. "
            "Romantic outdoor fashion photography with a dreamy, editorial quality."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="dress",
        sub_category_name="洋裝",
    ),
    SceneTemplate(
        id="cloth_dress_05_accessories",
        name="配飾搭配",
        name_en="Accessories Pairing",
        product_type="clothing",
        description="洋裝搭配鞋子、包包、飾品的完整造型展示",
        prompt=(
            "This dress styled as a complete look with matching accessories: "
            "a pair of elegant heels or sandals placed beside the dress, a complementary handbag, "
            "and a few jewelry pieces (necklace, bracelet, earrings) arranged in a curated flat lay. "
            "The dress is the central hero element, with accessories radiating around it. "
            "Shot from directly overhead at 90 degrees on a clean white surface. "
            "Bright, even lighting from a large overhead diffusion panel at 5500K for accurate colors. "
            "Shot at f/8 with a 35mm lens. "
            "Fashion mood board styling that inspires complete outfit planning."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="dress",
        sub_category_name="洋裝",
    ),
]

TemplateRegistry.register("clothing", CLOTHING_TEMPLATES)
