from app.templates.registry import SceneTemplate, TemplateRegistry

BEAUTY_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="beauty_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="beauty",
        description="純白背景，產品正面展示，展現包裝設計",
        prompt=(
            "This beauty/skincare product on a pure white background. "
            "Professional cosmetics photography with soft, even lighting. "
            "The product is centered, showing the label and packaging design clearly. "
            "Slight reflection on a glossy surface for luxury feel. "
            "Ultra-sharp focus on the product and text. "
            "Shot at f/8 with a 90mm tilt-shift lens to keep the label perfectly flat and readable. "
            "Commercial beauty product photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="beauty",
        description="展示核心成分、功效等賣點",
        prompt=(
            "Create a professional beauty product infographic. "
            "Show this product on a soft pastel or white background. "
            "Add elegant callout elements highlighting 3-4 key selling points: "
            "key active ingredients, skin benefits, texture/formula type, "
            "and any certifications (organic, cruelty-free, dermatologist tested). "
            "Feminine, clean design with elegant serif or script typography. "
            "Use diffused front lighting to eliminate harsh shadows on the packaging. "
            "Beauty brand product page aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_03_texture_closeup",
        name="質地特寫",
        name_en="Texture Close-up",
        product_type="beauty",
        description="展示產品質地、顏色、延展性",
        prompt=(
            "Close-up of this beauty product showing its texture and consistency. "
            "A swatch or dollop of the product on clean skin or a glass surface. "
            "Shows the product's color, texture (creamy, gel, liquid, powder). "
            "Macro photography with beautiful lighting that captures the product's quality. "
            "Shot at f/2.8 with a dedicated macro lens, using side lighting to reveal surface texture. "
            "The image helps buyers understand the product's feel and consistency. "
            "Luxurious beauty product texture photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_04_ingredients",
        name="成分展示圖",
        name_en="Ingredients Showcase",
        product_type="beauty",
        description="與天然成分（花、植物、水果）一起展示",
        prompt=(
            "This beauty product surrounded by its natural key ingredients: "
            "fresh flowers, herbs, fruits, honey, aloe vera, or botanical elements "
            "depending on the product type. "
            "Arranged on a clean marble or wood surface. "
            "Soft, natural lighting with a fresh, organic feel. "
            "Shot overhead at f/5.6 to keep both the product and scattered ingredients in focus. "
            "The composition communicates natural, effective ingredients. "
            "Premium beauty brand ingredient storytelling photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_05_vanity_scene",
        name="梳妝台場景",
        name_en="Vanity Scene",
        product_type="beauty",
        description="梳妝台/浴室等日常使用場景",
        prompt=(
            "This beauty product on an elegant vanity table or bathroom shelf. "
            "Styled with a mirror, other beauty items, and fresh flowers. "
            "Soft, warm lighting creating a pampering, spa-like atmosphere. "
            "The product is the hero, placed prominently in the foreground. "
            "Shot at 50mm f/2.0 to create a dreamy bokeh around the surrounding vanity items. "
            "Lifestyle beauty photography that evokes self-care and luxury. "
            "Instagram-worthy beauty shelfie aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_06_application",
        name="使用效果圖",
        name_en="Application Scene",
        product_type="beauty",
        description="模特使用/塗抹產品的場景",
        prompt=(
            "A model applying or using this beauty product in a natural, elegant way. "
            "Close-up of the application process showing the product in use. "
            "Soft, flattering lighting on clear, healthy skin. "
            "Clean background, the focus is on the product interaction with skin. "
            "Shot at 85mm f/1.8 for flattering compression and creamy skin-tone bokeh. "
            "The image helps buyers visualize using the product themselves. "
            "Professional beauty campaign photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_07_before_after",
        name="效果對比圖",
        name_en="Before & After",
        product_type="beauty",
        description="使用前後效果對比（概念展示）",
        prompt=(
            "A conceptual before-and-after visual for this beauty product. "
            "Split composition: one side shows dull, dry skin tone; "
            "the other side shows radiant, glowing skin. "
            "The product is placed in the center as the transformative element. "
            "Clean, clinical yet aspirational photography. "
            "Lit with a large octabox overhead for even, shadow-free skin illumination. "
            "Subtle visual cues showing improvement. "
            "Professional beauty results photography."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_08_gift_set",
        name="禮盒套裝圖",
        name_en="Gift Set Display",
        product_type="beauty",
        description="展示產品套裝或搭配組合",
        prompt=(
            "This beauty product presented as part of a curated gift set or skincare routine. "
            "Arranged with complementary products in a beautiful gift box or tray. "
            "Satin ribbon, tissue paper, or dried flowers as elegant props. "
            "The arrangement suggests a complete beauty ritual. "
            "Soft, luxurious lighting. Premium gift-worthy presentation. "
            "Shot at a 45-degree angle at f/4 to capture depth while keeping all items legible. "
            "Beauty set photography for holiday and gift marketing."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="beauty_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="beauty",
        description="展示品牌調性的質感美妝照",
        prompt=(
            "This beauty product in a dreamy, aspirational setting. "
            "Styled on a marble surface with gold accents, fresh peonies, "
            "a silk scarf, and soft candlelight. "
            "Warm, golden tones creating a luxurious, feminine atmosphere. "
            "The product catches beautiful light highlights. "
            "Shot at 35mm f/2.0 from a low angle to make the product feel grand and editorial. "
            "High-end beauty brand editorial photography "
            "that conveys indulgence and premium quality."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== skincare (護膚品) ====================
    SceneTemplate(
        id="beauty_skin_01_routine",
        name="護膚步驟",
        name_en="Skincare Routine Order",
        product_type="beauty",
        description="產品按護膚步驟排列展示",
        prompt=(
            "A curated collection of skincare products arranged in correct routine order on a clean marble vanity surface. "
            "The hero product is highlighted with a subtle spotlight while cleanser, toner, serum, moisturizer, and SPF are lined up sequentially. "
            "Each bottle is slightly angled to show its label, with small numbered indicators suggesting the order of application. "
            "Soft diffused overhead lighting creates gentle reflections on the glass bottles. "
            "Shot at 50mm f/4 from a 30-degree elevated angle to capture the full lineup with even sharpness across all products."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="skincare",
        sub_category_name="護膚品",
    ),
    SceneTemplate(
        id="beauty_skin_02_texture",
        name="質地展示",
        name_en="Texture Swatch Display",
        product_type="beauty",
        description="乳霜/精華液質地在皮膚上的展示",
        prompt=(
            "A close-up macro shot of cream or serum texture swatched across the back of a hand or inner forearm with clean, healthy skin. "
            "The swatch shows the product's consistency, color, and spreadability in a smooth gradient from thick dollop to thin spread. "
            "Raking side light at a low angle reveals the product's glossy or matte finish and micro-texture details. "
            "The background is a soft, out-of-focus neutral tone that keeps full attention on the swatch. "
            "Shot at f/2.8 with a 100mm macro lens for extreme detail on the product's formulation quality."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="skincare",
        sub_category_name="護膚品",
    ),
    SceneTemplate(
        id="beauty_skin_03_ingredients",
        name="成分展示",
        name_en="Natural Ingredients Scene",
        product_type="beauty",
        description="產品搭配天然成分一起展示",
        prompt=(
            "This skincare product placed at the center of a flat lay surrounded by its key natural ingredients such as sliced aloe vera, fresh rose petals, vitamin C orange slices, and green tea leaves. "
            "Each ingredient is artfully scattered on a white marble slab with small water droplets for a fresh, dewy feel. "
            "Bright, even overhead lighting with a large softbox ensures no harsh shadows on the product label. "
            "The composition radiates purity, natural efficacy, and botanical luxury. "
            "Shot directly overhead at f/5.6 to keep all elements crisp and in focus."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="skincare",
        sub_category_name="護膚品",
    ),
    SceneTemplate(
        id="beauty_skin_04_before_after",
        name="使用前後",
        name_en="Before & After Skin",
        product_type="beauty",
        description="使用前後皮膚狀態的分屏對比",
        prompt=(
            "A split-screen conceptual image showing skin condition improvement with this skincare product. "
            "The left half shows dull, textured, uneven skin tone under flat clinical lighting, while the right half reveals radiant, smooth, glowing skin with a healthy luminosity. "
            "The skincare product bottle is placed at the center dividing line as the transformative hero element. "
            "Clean, clinical white background with professional dermatological photography lighting using a ring light for even skin illumination. "
            "Shot at 85mm f/4 for consistent sharpness across both halves of the comparison."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="skincare",
        sub_category_name="護膚品",
    ),
    SceneTemplate(
        id="beauty_skin_05_night_routine",
        name="晚間護理",
        name_en="Night Routine Setting",
        product_type="beauty",
        description="溫暖燈光下的晚間護膚場景",
        prompt=(
            "This skincare product in a cozy nighttime self-care setting on a bedside table or bathroom vanity with warm amber lighting. "
            "A scented candle glows softly beside the product, with a silk sleep mask and a small jade roller as styling props. "
            "The warm color temperature around 2700K creates an intimate, relaxing atmosphere that evokes a luxurious evening wind-down ritual. "
            "Shallow depth of field draws the eye to the product while the candlelit background melts into a soft golden bokeh. "
            "Shot at 50mm f/1.8 from a low angle to give the product a prominent, editorial presence in the scene."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="skincare",
        sub_category_name="護膚品",
    ),
    # ==================== makeup (彩妝) ====================
    SceneTemplate(
        id="beauty_mk_01_swatch",
        name="色號展示",
        name_en="Color Swatches",
        product_type="beauty",
        description="手臂或手背上的色號試色展示",
        prompt=(
            "Multiple color swatches of this makeup product applied in clean, parallel stripes along the inner forearm against warm skin tones. "
            "Each swatch is clearly separated and shows the pigment's true color, opacity, and finish from sheer to full coverage. "
            "Bright, neutral-temperature studio lighting with a large overhead softbox to ensure accurate color reproduction without any color cast. "
            "The forearm rests on a clean white surface, and each swatch is evenly applied for consistency. "
            "Shot at f/4 with a 90mm lens from directly above the arm to minimize perspective distortion on the color comparison."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="makeup",
        sub_category_name="彩妝",
    ),
    SceneTemplate(
        id="beauty_mk_02_application",
        name="上妝過程",
        name_en="Makeup Application",
        product_type="beauty",
        description="模特正在使用產品上妝的過程",
        prompt=(
            "A model in the process of applying this makeup product, captured mid-action with a brush or applicator touching the face. "
            "The shot frames from the chin to the forehead, showing the model's focused expression and the product making contact with flawless skin. "
            "Soft beauty lighting with a large octabox positioned slightly above and in front to eliminate under-eye shadows. "
            "The makeup product and its packaging are visible in the model's other hand for brand recognition. "
            "Shot at 85mm f/2.0 for flattering facial compression with a creamy, out-of-focus pastel background."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="makeup",
        sub_category_name="彩妝",
    ),
    SceneTemplate(
        id="beauty_mk_03_palette",
        name="眼影盤展開",
        name_en="Open Palette Display",
        product_type="beauty",
        description="打開的眼影盤展示所有色號",
        prompt=(
            "An open eyeshadow or makeup palette laid flat on a reflective dark surface, displaying all color pans in their full range. "
            "Each shade catches the studio light differently, revealing shimmer, matte, satin, and glitter finishes across the palette. "
            "A few complementary brushes are placed alongside the palette at artistic angles for context. "
            "Overhead ring light provides perfectly even illumination across every pan with no hot spots or color shifts. "
            "Shot directly overhead at f/5.6 with a 60mm lens to keep every shade uniformly sharp and color-accurate."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="makeup",
        sub_category_name="彩妝",
    ),
    SceneTemplate(
        id="beauty_mk_04_look",
        name="完妝效果",
        name_en="Finished Makeup Look",
        product_type="beauty",
        description="模特完成妝容的效果展示",
        prompt=(
            "A striking close-up portrait of a model showcasing a finished makeup look created with this product. "
            "The camera captures the face from a slight three-quarter angle, highlighting the eye makeup, lip color, and overall complexion. "
            "Professional beauty dish lighting from above and slightly to the side creates sculpted cheekbone highlights and a catchlight in the eyes. "
            "The model's skin appears flawless with the makeup product's effect clearly visible and aspirational. "
            "Shot at 105mm f/2.8 for a tight beauty portrait with smooth skin tones and a clean, solid-color background."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="makeup",
        sub_category_name="彩妝",
    ),
    SceneTemplate(
        id="beauty_mk_05_tools",
        name="工具搭配",
        name_en="Product with Tools",
        product_type="beauty",
        description="彩妝產品搭配刷具/海綿展示",
        prompt=(
            "This makeup product artfully arranged with professional application tools including brushes, beauty blenders, and sponges on a clean marble or acrylic surface. "
            "The tools fan out from the product in a visually balanced composition, each tool suggesting a different application technique. "
            "Soft lateral lighting from the left creates gentle shadows that add depth and dimension to the bristle textures and sponge surfaces. "
            "A light dusting of powder or pigment is scattered on the surface for an authentic, editorial touch. "
            "Shot at a 45-degree angle at f/4 with a 50mm lens to capture the full arrangement with pleasing depth."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="makeup",
        sub_category_name="彩妝",
    ),
    # ==================== tools (美容工具) ====================
    SceneTemplate(
        id="beauty_tool_01_usage",
        name="使用示範",
        name_en="Tool Usage Demo",
        product_type="beauty",
        description="模特使用美容工具的示範",
        prompt=(
            "A model demonstrating this beauty tool in use on her face or body, showing the correct technique and application area. "
            "The shot is framed from the shoulders up, with the tool making gentle contact with the skin in a natural, relaxed pose. "
            "Soft beauty lighting with a key light at 45 degrees and a fill reflector to show both the tool details and the model's skin texture. "
            "The model's expression conveys relaxation and self-care enjoyment. "
            "Shot at 70mm f/2.4 to keep the tool and contact area in sharp focus while softening the background into a clean bokeh."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="tools",
        sub_category_name="美容工具",
    ),
    SceneTemplate(
        id="beauty_tool_02_before_after",
        name="效果對比",
        name_en="Tool Before & After",
        product_type="beauty",
        description="使用美容工具前後的效果對比",
        prompt=(
            "A split-composition image showing the visible results of using this beauty tool, with a before state on the left and an after state on the right. "
            "The before side shows the natural baseline skin or hair condition under flat, neutral lighting. "
            "The after side reveals the improved result with a subtle glow, smoother texture, or more defined features after tool usage. "
            "The beauty tool is placed at the center dividing line as the key element connecting both halves. "
            "Shot at 85mm f/4 with consistent, calibrated studio lighting on both sides to ensure a fair, professional comparison."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="tools",
        sub_category_name="美容工具",
    ),
    SceneTemplate(
        id="beauty_tool_03_portable",
        name="便攜展示",
        name_en="Portable Display",
        product_type="beauty",
        description="美容工具放在化妝包或旅行袋中展示",
        prompt=(
            "This beauty tool tucked neatly inside an open designer makeup bag or travel pouch, showing its compact and portable size. "
            "The pouch sits on a clean surface with a few other travel-sized beauty essentials peeking out for lifestyle context. "
            "A passport, sunglasses, or boarding pass in the soft background suggests travel readiness and on-the-go convenience. "
            "Bright, natural window light from the side creates an airy, editorial travel lifestyle feel. "
            "Shot at 35mm f/3.5 from a slightly elevated angle to show the interior of the pouch and the tool's size relative to other items."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="tools",
        sub_category_name="美容工具",
    ),
    SceneTemplate(
        id="beauty_tool_04_charging",
        name="充電展示",
        name_en="Charging Display",
        product_type="beauty",
        description="美容工具在充電座上展示",
        prompt=(
            "This electronic beauty tool elegantly positioned on its charging dock or base station on a clean, minimalist vanity surface. "
            "A small LED indicator light glows softly, signaling the charging status and adding a modern tech-forward accent. "
            "The sleek design of the tool and dock are highlighted by controlled studio lighting with a subtle rim light outlining the product silhouette. "
            "The background is a soft gradient or clean wall, keeping the focus entirely on the product's premium industrial design. "
            "Shot at 60mm f/3.5 at a low eye-level angle to emphasize the product's upright stance and sophisticated charging station design."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="tools",
        sub_category_name="美容工具",
    ),
    SceneTemplate(
        id="beauty_tool_05_accessories",
        name="配件展示",
        name_en="Tool Accessories Display",
        product_type="beauty",
        description="美容工具搭配替換頭和配件展示",
        prompt=(
            "This beauty tool displayed with all its interchangeable heads, attachments, and accessories arranged in a neat, organized layout around the main device. "
            "Each replacement head is placed with clear spacing, showing different functions such as cleansing, exfoliating, massaging, and toning. "
            "A clean white or light gray surface provides maximum contrast for each small accessory piece. "
            "Bright, even overhead lighting from a large diffusion panel eliminates shadows and ensures every detail is visible. "
            "Shot directly overhead at f/7.1 with a 50mm lens for a satisfying flat-lay composition with uniform sharpness across all pieces."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="tools",
        sub_category_name="美容工具",
    ),
]

TemplateRegistry.register("beauty", BEAUTY_TEMPLATES)
