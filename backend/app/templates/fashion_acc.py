from app.templates.registry import SceneTemplate, TemplateRegistry

FASHION_ACC_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="fashion_acc_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="fashion_acc",
        description="純白背景，配飾居中展示，符合各平台主圖規範",
        prompt=(
            "Place this fashion accessory on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with a large octagonal softbox overhead at 45 degrees "
            "and two side fill lights for even illumination. "
            "The accessory should be centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding and depth. "
            "Front-facing angle tilted 10 degrees to show texture and dimension. "
            "Shot with an 85mm lens at f/8 for maximum sharpness across the entire product. "
            "Ultra-high resolution, crisp details on fabric weave, embroidery, buckle, and material texture. "
            "No other objects in frame. Color accuracy is critical."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="fashion_acc",
        description="2x2 拼圖佈局，多角度展示配飾核心賣點",
        prompt=(
            "Create a professional product photography collage for this fashion accessory. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the main design, pattern, and brand details. "
            "2) Close-up of the premium material texture and craftsmanship quality. "
            "3) Hardware detail shot: clasp, buckle, or decorative element with metallic shine visible. "
            "4) Side or back view showing thickness, lining, or construction. "
            "Each view is clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "Shot with a 90mm macro lens at f/7.1 for tack-sharp detail in every panel. "
            "The overall layout is balanced and looks like a premium product specification page."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="fashion_acc",
        description="微距特寫，展示材質紋理、車線、五金扣件",
        prompt=(
            "Extreme macro close-up photography of this fashion accessory showing fine craftsmanship details. "
            "Split into 2-3 detail zones: fabric or leather texture and weave pattern, "
            "precise stitching and edge finishing, and metal hardware/clasp quality with reflections. "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The texture should be so detailed you can feel the material quality through the image. "
            "Focus stacking technique for maximum sharpness across detail zones. "
            "Professional accessory detail photography for luxury e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="fashion_acc",
        description="與手掌、手機等常見物品對比，直觀展示大小",
        prompt=(
            "This fashion accessory photographed from a straight-on angle next to common reference items: "
            "a hand wearing the accessory or holding it, and a smartphone placed nearby for scale. "
            "All items resting on a clean white surface with a subtle grid pattern for measurement reference. "
            "The accessory is the hero element in the center. "
            "Clean white background, even studio lighting from overhead softbox. "
            "Shot with a 60mm lens at f/11 to keep all items tack-sharp. "
            "The items are proportionally realistic to each other. "
            "The composition clearly communicates the accessory's wearable size and proportions."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_05_outfit_scene",
        name="穿搭場景",
        name_en="Outfit Styling Scene",
        product_type="fashion_acc",
        description="配飾搭配整體穿搭，展示時尚風格",
        prompt=(
            "This fashion accessory styled as the focal point of a complete outfit ensemble. "
            "A person wearing the accessory with a coordinated outfit in a bright, airy dressing room "
            "or boutique setting with soft natural window light from the left side. "
            "The accessory stands out as the hero piece that elevates the entire look. "
            "Shot with a 50mm lens at f/2.8 with shallow depth of field, "
            "the accessory in razor-sharp focus while the clothing provides soft context. "
            "Camera angle at eye level, warm color tones around 5600K. "
            "Fashion editorial styling photography with aspirational mood."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_06_street_style",
        name="街拍場景",
        name_en="Street Style Scene",
        product_type="fashion_acc",
        description="戶外街拍情境，展示配飾日常搭配",
        prompt=(
            "This fashion accessory captured in an outdoor street style context. "
            "A stylish person wearing the accessory while walking along a charming urban sidewalk, "
            "cafe terrace, or tree-lined boulevard with soft bokeh city background. "
            "Golden hour natural lighting creating warm highlights and gentle shadows on the accessory. "
            "The accessory is clearly visible and is the standout element. "
            "Shot at 85mm f/2.0 from a slightly low angle for a flattering fashion perspective. "
            "Street fashion editorial photography with confident, effortless style. "
            "Aspirational daily wear context."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_07_model_showcase",
        name="模特展示",
        name_en="Model Showcase",
        product_type="fashion_acc",
        description="模特佩戴配飾，展示實際穿戴效果",
        prompt=(
            "A model elegantly wearing this fashion accessory in a confident, natural pose. "
            "Shot from chest up or waist up depending on accessory type, "
            "the accessory is clearly visible and is the absolute focal point. "
            "Clean neutral background: light beige or soft gray studio backdrop. "
            "Fashion editorial lighting setup: key light at 45 degrees with a large softbox, "
            "fill light at 30 degrees opposite side, and a hair/rim light from behind. "
            "Shot with a 70mm lens at f/3.5 for beautiful subject separation. "
            "The model wears simple, solid-color clothing that complements without competing. "
            "Sharp focus on the accessory with slight softness on the background."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_08_accessory_collection",
        name="配飾組合",
        name_en="Accessory Collection",
        product_type="fashion_acc",
        description="多件配飾平拍，展示搭配組合",
        prompt=(
            "This fashion accessory arranged in an elegant flat lay with complementary accessories: "
            "coordinating hat, scarf, belt, sunglasses, or jewelry pieces. "
            "Top-down perspective on a clean marble or cream-colored surface. "
            "Each item neatly spaced with intentional geometric arrangement. "
            "The hero accessory is centrally placed and slightly larger in frame. "
            "Shot overhead with a 35mm lens at f/7.1, even diffused softbox lighting "
            "eliminating harsh shadows while preserving subtle material textures. "
            "Professional fashion flat lay photography showing a curated accessory wardrobe."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="fashion_acc_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="fashion_acc",
        description="展示品牌調性的精緻擺拍，提升品牌質感",
        prompt=(
            "This fashion accessory styled in a luxurious lifestyle flat lay composition "
            "with premium elements: designer sunglasses, a fine leather wallet, "
            "a bouquet of dried flowers, and a fashion magazine on a textured linen or marble surface. "
            "Shot from directly above with a 35mm lens at f/5.6. "
            "Soft directional lighting from upper left creating refined shadows. "
            "Cohesive warm earthy color palette with editorial fashion mood board aesthetic. "
            "The composition conveys premium quality, curated taste, and aspirational lifestyle. "
            "Each object placed with precise intentional spacing following the rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== hats (帽子) ====================
    SceneTemplate(
        id="facc_hat_01_wearing",
        name="佩戴展示",
        name_en="Hat Wearing Display",
        product_type="fashion_acc",
        description="模特佩戴帽子，面部部分可見，展示整體效果",
        prompt=(
            "A model wearing this hat in a natural, confident pose with their face partially visible below the brim. "
            "The hat is the hero element, positioned perfectly on the head showing the correct fit and silhouette. "
            "Shot from a three-quarter front angle with an 85mm lens at f/2.8, the hat in razor-sharp focus "
            "against a soft, neutral light gray studio backdrop. "
            "Fashion editorial lighting with a large key softbox at 45 degrees from the right and a subtle fill light opposite. "
            "Warm skin tones complement the hat's color. The model wears minimal solid-color clothing "
            "so the hat commands full attention as the styling centerpiece."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="hats",
        sub_category_name="帽子",
    ),
    SceneTemplate(
        id="facc_hat_02_collection",
        name="系列展示",
        name_en="Hat Collection Display",
        product_type="fashion_acc",
        description="多款帽子掛在掛鉤上展示系列風格",
        prompt=(
            "Multiple hat styles from this collection displayed on a row of elegant wall-mounted hooks "
            "against a clean white or light wood-paneled wall. "
            "Each hat hangs naturally, showing its unique silhouette and design character side by side. "
            "The hero hat is positioned at center and slightly forward from the others for visual prominence. "
            "Shot with a 50mm lens at f/5.6 from eye level, even diffused studio lighting "
            "providing consistent illumination across all hats with no harsh shadows. "
            "The arrangement creates a boutique retail display aesthetic, conveying variety and curated style."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="hats",
        sub_category_name="帽子",
    ),
    SceneTemplate(
        id="facc_hat_03_outdoor",
        name="戶外場景",
        name_en="Outdoor Hat Scene",
        product_type="fashion_acc",
        description="模特在戶外陽光下佩戴帽子",
        prompt=(
            "A person wearing this hat outdoors in bright natural sunshine, walking through a sunlit park path "
            "or along a golden wheat field with soft bokeh foliage in the background. "
            "The hat provides attractive shade, with dappled sunlight playing across the brim. "
            "Golden hour warm light from the side creates beautiful rim lighting on the hat edges. "
            "Shot with a 70mm lens at f/2.0 for creamy background separation, camera angle slightly below eye level "
            "for an aspirational perspective. The hat is in perfect focus, showing its shape, color, and sun-protective qualities. "
            "Lifestyle outdoor fashion photography conveying adventure, warmth, and effortless summer style."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="hats",
        sub_category_name="帽子",
    ),
    SceneTemplate(
        id="facc_hat_04_detail",
        name="細節特寫",
        name_en="Hat Detail Close-up",
        product_type="fashion_acc",
        description="帽子材質、車線、標籤的近距離特寫",
        prompt=(
            "Extreme close-up macro photography of this hat highlighting craftsmanship details. "
            "Show the weave pattern or fabric texture of the hat body, the precise stitching along the brim edge, "
            "and the embroidered or woven brand label on the interior or sweatband. "
            "Shot with a 100mm macro lens at f/3.5, ring light providing even illumination across the textile surface. "
            "Shallow depth of field draws the eye to the focal detail area while surrounding material falls into soft blur. "
            "The texture is rendered so clearly you can count individual thread crossings. "
            "Professional hat detail photography for premium e-commerce product pages."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="hats",
        sub_category_name="帽子",
    ),
    SceneTemplate(
        id="facc_hat_05_seasonal",
        name="季節搭配",
        name_en="Seasonal Hat Coordination",
        product_type="fashion_acc",
        description="帽子搭配當季穿搭的造型展示",
        prompt=(
            "This hat styled as part of a complete seasonal outfit on a model in a lifestyle setting. "
            "The model wears a coordinated seasonal look: light linen and sunglasses for summer, "
            "or a wool coat and scarf for autumn, with the hat as the defining accent piece. "
            "Set in a charming seasonal backdrop such as an outdoor cafe terrace or a leaf-covered park lane. "
            "Shot with a 50mm lens at f/2.4 from waist up, warm natural light illuminating the ensemble. "
            "The hat is the visual anchor that ties the entire outfit together, clearly in sharp focus "
            "while the environment provides soft seasonal atmosphere and color harmony."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="hats",
        sub_category_name="帽子",
    ),
    # ==================== scarves (圍巾) ====================
    SceneTemplate(
        id="facc_scarf_01_wrapped",
        name="圍繞展示",
        name_en="Scarf Wrapped Display",
        product_type="fashion_acc",
        description="圍巾優雅地繞在脖子上的穿戴展示",
        prompt=(
            "A model with this scarf elegantly wrapped around their neck in a classic loop tie, "
            "the fabric draping naturally and showing both the outer pattern and a glimpse of the reverse side. "
            "Shot from chest level upward with a 70mm lens at f/2.8, the scarf in tack-sharp focus "
            "against a minimal light beige studio backdrop. "
            "Soft directional key light from the left at 45 degrees highlights the fabric's texture and color depth. "
            "The model wears a simple dark solid-color top to let the scarf be the undeniable focal point. "
            "Fashion editorial photography conveying warmth, luxury, and effortless draping style."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="scarves",
        sub_category_name="圍巾",
    ),
    SceneTemplate(
        id="facc_scarf_02_drape",
        name="披掛方式",
        name_en="Scarf Draping Styles",
        product_type="fashion_acc",
        description="展示圍巾不同的佩戴和披掛方式",
        prompt=(
            "A professional collage showing three to four different ways to wear and drape this scarf, "
            "arranged in a clean grid layout on a white background. "
            "Each panel shows the same scarf styled differently: looped around the neck, "
            "draped over one shoulder as a shawl, tied in a French knot, and loosely wrapped as a cowl. "
            "Consistent soft studio lighting at 5500K across all panels with even illumination. "
            "Shot with a 60mm lens at f/5.6, each draping style clearly visible on a model or mannequin bust. "
            "The layout serves as a practical styling guide while showcasing the scarf's versatility and premium quality."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="scarves",
        sub_category_name="圍巾",
    ),
    SceneTemplate(
        id="facc_scarf_03_fabric",
        name="面料展示",
        name_en="Scarf Fabric Texture",
        product_type="fashion_acc",
        description="圍巾面料紋理和圖案的近距離展示",
        prompt=(
            "Close-up photography of this scarf's fabric showing the richness of its textile texture and pattern detail. "
            "The scarf is gently gathered to create natural folds that reveal both the surface pattern and the fabric weight. "
            "Shot with a 100mm macro lens at f/4.0, shallow depth of field with the central pattern area in razor-sharp focus "
            "and the edges falling into soft bokeh. "
            "Ring light illumination brings out every thread and weave detail in the fabric. "
            "The color reproduction is precise, showing the true hue and saturation of dyes. "
            "Professional textile macro photography for luxury fabric appreciation."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="scarves",
        sub_category_name="圍巾",
    ),
    SceneTemplate(
        id="facc_scarf_04_folded",
        name="折疊展示",
        name_en="Scarf Folded Display",
        product_type="fashion_acc",
        description="圍巾整齊折疊展示完整圖案",
        prompt=(
            "This scarf neatly folded into a square or rectangle on a clean white marble surface, "
            "displaying the full pattern and design from directly above. "
            "The fold is precise, with one corner slightly turned to reveal the reverse side and fabric weight. "
            "Shot overhead with a 50mm lens at f/7.1, even diffused softbox lighting "
            "eliminating shadows while preserving the subtle texture of the fabric surface. "
            "The entire pattern is visible and the colors are true to life with accurate white balance at 5500K. "
            "Product photography that communicates the scarf's complete design, generous dimensions, and premium folding quality."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="scarves",
        sub_category_name="圍巾",
    ),
    SceneTemplate(
        id="facc_scarf_05_winter",
        name="冬日場景",
        name_en="Winter Scarf Scene",
        product_type="fashion_acc",
        description="在寒冷天氣環境中佩戴溫暖圍巾",
        prompt=(
            "A person bundled up in this warm scarf on a cold winter day, walking through a charming snow-dusted street "
            "or standing by a frosted window of a cozy cafe with warm interior light glowing behind them. "
            "The scarf is wrapped snugly and prominently, clearly the warmest and most stylish element of the winter outfit. "
            "Cool ambient daylight mixed with warm interior tones creates a beautiful color contrast on the scarf. "
            "Shot with an 85mm lens at f/2.0, the scarf and face area in crisp focus with the wintry background in soft bokeh. "
            "Camera at eye level for a personal, intimate perspective. "
            "Winter fashion lifestyle photography evoking coziness, warmth, and seasonal style."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="scarves",
        sub_category_name="圍巾",
    ),
    # ==================== hair_acc (髮飾) ====================
    SceneTemplate(
        id="facc_hair_01_wearing",
        name="配戴展示",
        name_en="Hair Accessory Wearing",
        product_type="fashion_acc",
        description="髮飾佩戴在造型好的頭髮上的展示",
        prompt=(
            "This hair accessory beautifully placed in a model's styled hair, shown from a flattering three-quarter rear angle "
            "that highlights both the accessory and the hairstyle it complements. "
            "The hair is neatly styled to showcase the accessory: an updo for clips, flowing waves for headbands, "
            "or a half-up style for barrettes. "
            "Shot with a 70mm lens at f/2.8, the accessory in tack-sharp focus against softly blurred hair and skin tones. "
            "Soft key light from above-right simulates natural daylight, with a subtle fill from the opposite side. "
            "The model's hair color and style are chosen to provide maximum contrast and visibility for the accessory."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="hair_acc",
        sub_category_name="髮飾",
    ),
    SceneTemplate(
        id="facc_hair_02_variety",
        name="款式展示",
        name_en="Hair Accessory Variety",
        product_type="fashion_acc",
        description="多款髮飾整齊排列展示不同款式",
        prompt=(
            "Multiple hair accessories from this collection arranged in a visually appealing flat lay pattern "
            "on a soft blush pink or white velvet surface. "
            "The accessories are spaced evenly in rows or a radial pattern, each piece clearly visible and distinct. "
            "The hero piece is centered and slightly elevated on a small fabric cushion for prominence. "
            "Shot from directly overhead with a 50mm lens at f/6.3, even diffused softbox lighting "
            "capturing the sparkle of crystals, the sheen of metal, and the texture of fabric elements. "
            "The arrangement feels curated and boutique-like, conveying variety, craftsmanship, and feminine elegance."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="hair_acc",
        sub_category_name="髮飾",
    ),
    SceneTemplate(
        id="facc_hair_03_close_up",
        name="設計特寫",
        name_en="Hair Accessory Design Close-up",
        product_type="fashion_acc",
        description="髮飾設計細節的微距特寫",
        prompt=(
            "Extreme macro shot of this hair accessory revealing its intricate design details: "
            "crystal or pearl settings, metal filigree work, enamel coloring, or hand-stitched fabric elements. "
            "Shot with a 100mm macro lens at f/3.2, very shallow depth of field with the key design element in pin-sharp focus "
            "and surrounding details falling into artistic blur. "
            "Ring light provides even illumination that captures the sparkle and reflections of decorative elements. "
            "The level of detail visible conveys premium craftsmanship and justifies the product's value. "
            "Professional jewelry-grade macro photography with vivid color reproduction and precise highlight control."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="hair_acc",
        sub_category_name="髮飾",
    ),
    SceneTemplate(
        id="facc_hair_04_occasion",
        name="場合搭配",
        name_en="Hair Accessory for Occasion",
        product_type="fashion_acc",
        description="特殊場合佩戴髮飾的造型展示",
        prompt=(
            "A model wearing this hair accessory dressed for a special occasion: an elegant evening event, "
            "a wedding, or a formal dinner with a sophisticated hairstyle and coordinated outfit. "
            "The hair accessory is the defining finishing touch, catching the light beautifully "
            "in a warmly lit ballroom, garden party, or elegant venue with soft bokeh fairy lights in the background. "
            "Shot with an 85mm lens at f/2.0 from a slightly elevated angle looking down at the accessory in the hair. "
            "Warm golden lighting creates luxurious highlights on the accessory. "
            "The photograph conveys special-occasion glamour and shows how the piece elevates formal styling."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="hair_acc",
        sub_category_name="髮飾",
    ),
    SceneTemplate(
        id="facc_hair_05_display",
        name="收納展示",
        name_en="Hair Accessory Display Stand",
        product_type="fashion_acc",
        description="髮飾放在展示架或托盤上的收納展示",
        prompt=(
            "This hair accessory and complementary pieces arranged on a beautiful display stand, "
            "ceramic jewelry tray, or velvet-lined organizer box on a vanity table. "
            "The hero accessory is placed prominently at the front of the arrangement with other pieces "
            "providing visual context without competing. "
            "A small mirror, perfume bottle, or fresh flowers nearby create a feminine dressing table vignette. "
            "Shot with a 50mm lens at f/3.5 from a slightly elevated angle, soft window light from the left. "
            "The scene feels organized, luxurious, and aspirational, suggesting a curated accessory collection "
            "and an elegant daily getting-ready ritual."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="hair_acc",
        sub_category_name="髮飾",
    ),
]

TemplateRegistry.register("fashion_acc", FASHION_ACC_TEMPLATES)
