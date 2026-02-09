from app.templates.registry import SceneTemplate, TemplateRegistry

STATIONERY_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="stationery_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="stationery",
        description="純白背景，文具產品居中，色彩精準呈現",
        prompt=(
            "This stationery product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with dual softbox lighting at 45 degrees from both sides and a top fill light. "
            "The product is centered, occupying about 80% of the frame. "
            "Subtle natural shadow beneath for grounding. "
            "Slight 15-degree tilt to show dimension and form. "
            "Shot with a 90mm lens at f/8 for full depth of field, ensuring crisp details on textures, branding, and fine print. "
            "Ultra-high resolution, accurate color reproduction critical for pen inks and notebook covers. "
            "No other objects in frame."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="stationery",
        description="展示筆尖、墨水、紙質、機構等核心賣點",
        prompt=(
            "Create a professional product photography collage for this stationery item. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the full product design and branding. "
            "2) Close-up of the functional mechanism (pen tip, binding, blade edge, clip). "
            "3) Material quality detail showing texture and finish. "
            "4) Ergonomic grip or key differentiating feature. "
            "Each view is clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all four shots. "
            "Shot at f/5.6 with a 60mm macro lens for clarity. "
            "The overall layout looks like a premium specification page."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="stationery",
        description="微距特寫，展示筆尖出墨、紙張紋理、刀刃鋒利度",
        prompt=(
            "Extreme macro close-up photography of this stationery product showing fine craftsmanship details. "
            "Split into 2-3 detail zones: functional tip or edge quality, material surface texture and finish, "
            "and mechanical joints or precision engineering. "
            "Shot with a 100mm macro lens at f/3.5, shallow depth of field with ring light illumination. "
            "If a pen, show ink flow at the nib tip; if scissors, the blade edge sharpness; if a notebook, the paper grain and binding. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional product detail photography for premium stationery e-commerce."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="stationery",
        description="與手掌、A4紙張、手機等常見物品對比大小",
        prompt=(
            "This stationery product photographed next to common reference objects for size: "
            "a human hand holding the product naturally, an A4 sheet of paper, and a smartphone. "
            "All items on a clean white surface with a subtle grid pattern for scale. "
            "The stationery item is the central hero element. "
            "Clean white background, even studio lighting from above. "
            "Shot from a slightly elevated 30-degree angle at f/11 with a 50mm lens to keep all objects tack-sharp. "
            "The composition clearly communicates the product's practical everyday size. "
            "Proportionally realistic relationships between all items."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_05_office_desk_scene",
        name="辦公桌場景",
        name_en="Office Desk Scene",
        product_type="stationery",
        description="整潔辦公桌上搭配筆記本的使用情境",
        prompt=(
            "This stationery product placed naturally on a clean, modern office desk. "
            "A leather-bound notebook open nearby, a cup of coffee on a coaster, and a laptop partially visible. "
            "Warm natural window light streaming in from the left side mixing with a warm desk lamp. "
            "The stationery item is the clear hero product, placed prominently. "
            "Shot at 35mm f/2.8 with shallow depth of field creating soft bokeh on the background. "
            "Camera angle slightly above at 30 degrees, conveying a productive, organized workspace. "
            "Warm color tones around 5600K, professional yet inviting atmosphere."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_06_school_scene",
        name="學校場景",
        name_en="School Scene",
        product_type="stationery",
        description="教室或書房的學習使用環境",
        prompt=(
            "This stationery product in a bright, cheerful study environment. "
            "A student's desk with textbooks, colorful sticky notes, and a pencil case nearby. "
            "Bright natural daylight from a large window creating an energetic study atmosphere. "
            "The stationery product is prominently placed as the focal point on the desk. "
            "Shot at 40mm f/2.4 with the background gently blurred showing bookshelves or a classroom setting. "
            "Camera at eye level from a seated perspective. "
            "Fresh, youthful color palette with blues and greens. "
            "Aspirational back-to-school lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_07_writing_demo",
        name="書寫展示",
        name_en="Writing Demo",
        product_type="stationery",
        description="手持書寫或使用產品的實際展示",
        prompt=(
            "A person's hand elegantly holding and using this stationery product in action. "
            "If a pen or marker, showing smooth ink flow on premium paper with visible written lines. "
            "If scissors or a ruler, demonstrating precise cutting or measuring. "
            "Shot from a slightly elevated angle looking down at the hands and product. "
            "Clean neutral background (light wood desk or white surface). "
            "Professional lighting: key light at 45 degrees from upper left with soft fill from the right. "
            "Shot at 85mm f/2.0 for beautiful separation, sharp focus on the product and hand. "
            "The image conveys precision, quality, and effortless usability."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_08_stationery_set",
        name="文具組合",
        name_en="Stationery Set",
        product_type="stationery",
        description="多件文具產品的平鋪組合展示",
        prompt=(
            "This stationery product shown in a beautiful flat lay arrangement with complementary office supplies: "
            "colored pens, a ruler, sticky notes, paper clips, washi tape, and a small notebook. "
            "Top-down overhead perspective on a clean white or light wood surface. "
            "Items arranged with intentional spacing following a pleasing geometric pattern. "
            "The hero product is centrally positioned and slightly larger in the composition. "
            "Shot directly overhead at f/7.1 with even diffused softbox lighting from above. "
            "Bright, organized aesthetic that conveys completeness and coordination. "
            "Professional stationery flat lay photography with cohesive color palette."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="stationery_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="stationery",
        description="展示文具品牌調性的精緻擺拍，提升品牌感",
        prompt=(
            "This stationery product styled in an elegant flat lay arrangement with premium lifestyle accessories: "
            "a leather journal, a ceramic coffee cup, fresh eucalyptus sprigs, and reading glasses. "
            "Shot on a clean marble or linen surface from directly above. "
            "Cohesive muted earth-tone color palette, editorial lifestyle mood board aesthetic. "
            "Soft directional lighting from upper left creating subtle shadows. "
            "Shot at f/4.0 with a 50mm lens for natural perspective from overhead. "
            "The composition conveys creativity, sophistication, and thoughtful design. "
            "Each object placed with precise intentional spacing following rule of thirds."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== pens (筆類) ====================
    SceneTemplate(
        id="stat_pen_01_writing",
        name="書寫場景",
        name_en="Writing Scene",
        product_type="stationery",
        description="筆在紙上書寫的特寫，展示墨水流動與書寫手感",
        prompt=(
            "A close-up of this pen writing elegant cursive text on premium cream-colored cotton paper. "
            "The ink flows smoothly from the nib, leaving a rich, consistent line with subtle sheen. "
            "Shot at 100mm macro f/2.8 from a low 20-degree angle capturing the pen tip contact point with the paper surface. "
            "Soft directional lighting from the upper left highlights the ink's wet gloss and paper texture. "
            "Shallow depth of field keeps the nib and fresh ink line razor-sharp while the written text trails into soft focus behind. "
            "The warm ambient tones of 5500K convey a refined, contemplative writing moment."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="pens",
        sub_category_name="筆類",
    ),
    SceneTemplate(
        id="stat_pen_02_collection",
        name="系列展示",
        name_en="Pen Collection Display",
        product_type="stationery",
        description="多支筆在收納盒或皮套中的系列展示",
        prompt=(
            "A curated collection of pens including this hero pen displayed in an open leather or velvet-lined pen case. "
            "The pens are arranged in parallel rows with even spacing, caps aligned, showing the full range of colors or finishes. "
            "Shot from a 35-degree elevated angle on a dark walnut wood surface with soft studio lighting from two sides at 45 degrees. "
            "The hero pen is positioned in the center row, slightly pulled forward to draw the viewer's eye. "
            "Shot at 60mm f/5.6 for good depth across all pens while maintaining a clean blurred background. "
            "Rich, warm color tones emphasize the premium materials and collector's appeal of the pen series."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pens",
        sub_category_name="筆類",
    ),
    SceneTemplate(
        id="stat_pen_03_desk_setup",
        name="桌面搭配",
        name_en="Desk Setup with Pen",
        product_type="stationery",
        description="筆搭配筆記本和規劃本的桌面使用場景",
        prompt=(
            "This pen placed diagonally across an open Moleskine-style notebook on a clean minimalist desk. "
            "A weekly planner, a small potted succulent, and a ceramic pen holder are arranged nearby. "
            "Warm natural window light from the left creates soft directional shadows and a cozy productivity atmosphere. "
            "Shot at 35mm f/2.8 from a 40-degree overhead angle, the pen and open notebook page in sharp focus. "
            "The desk surface is light birch wood or white laminate for a clean Scandinavian aesthetic. "
            "The composition communicates organized daily planning and the joy of analog writing tools in a modern workspace."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pens",
        sub_category_name="筆類",
    ),
    SceneTemplate(
        id="stat_pen_04_nib_detail",
        name="筆尖特寫",
        name_en="Nib Detail Macro",
        product_type="stationery",
        description="筆尖或筆頭的超微距特寫，展示工藝精度",
        prompt=(
            "An extreme macro photograph of this pen's nib or tip at 3:1 magnification, revealing the precision engineering. "
            "The iridium tipping, ink channel, breather hole, and tine alignment are all visible in stunning detail. "
            "Shot with a 100mm macro lens at f/4 with focus stacking across 15 frames for edge-to-edge sharpness. "
            "Ring light illumination combined with a small reflector below to fill shadows in the nib's curves. "
            "A tiny bead of ink sits at the tip, catching the light with a jewel-like glint. "
            "Dark neutral background isolates the nib completely, emphasizing the metallic finish and micro-engraving details."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="pens",
        sub_category_name="筆類",
    ),
    SceneTemplate(
        id="stat_pen_05_gift",
        name="禮品包裝",
        name_en="Gift Packaging",
        product_type="stationery",
        description="筆在高級禮品盒中的精美包裝展示",
        prompt=(
            "This pen presented in its premium gift box, lid opened at a 45-degree angle revealing the pen on a satin cushion. "
            "The box is crafted from rigid board with a soft-touch matte finish and embossed logo on the lid interior. "
            "A small certificate of authenticity or brand card rests beside the pen inside the box. "
            "Shot at 60mm f/4.0 from a 30-degree elevated front angle on a dark marble or velvet surface. "
            "Dramatic key lighting from the upper right highlights the box's premium materials and the pen's metallic sheen. "
            "The composition conveys luxury gifting, with warm tones and rich contrast suitable for special occasion promotions."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="pens",
        sub_category_name="筆類",
    ),
    # ==================== organizer (收納文具) ====================
    SceneTemplate(
        id="stat_org_01_desk",
        name="桌面收納",
        name_en="Desk Organizer",
        product_type="stationery",
        description="收納文具放在桌面上，內含各種文具的使用場景",
        prompt=(
            "This stationery organizer placed on a tidy modern office desk, filled with pens, markers, scissors, and sticky notes. "
            "The organizer's compartments are clearly visible, each holding different types of supplies in an orderly arrangement. "
            "A laptop screen edge, a small desk plant, and a coffee mug are partially visible in the background. "
            "Warm natural light from a window on the left mixed with soft overhead LED panel lighting at 5000K. "
            "Shot at 40mm f/3.5 from a 30-degree elevated angle, the organizer in sharp focus with gentle background blur. "
            "The scene communicates workspace efficiency and the satisfaction of a well-organized desktop."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="organizer",
        sub_category_name="收納文具",
    ),
    SceneTemplate(
        id="stat_org_02_school",
        name="學生場景",
        name_en="School Setting",
        product_type="stationery",
        description="鉛筆盒或文具袋在學生書桌上的使用場景",
        prompt=(
            "This pencil case or stationery pouch on a student's desk surrounded by textbooks, a notebook with handwritten notes, and colorful highlighters. "
            "The case is partially unzipped showing an array of pens, erasers, and a small ruler peeking out. "
            "Bright, cheerful classroom-like lighting from overhead fluorescents mixed with daylight from a nearby window. "
            "Shot at 35mm f/2.8 from a seated eye-level perspective, the pencil case as the sharp hero subject. "
            "A backpack strap is visible at the frame edge, reinforcing the school context. "
            "Youthful, energetic color palette with bright blues, yellows, and greens conveying a fun back-to-school mood."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="organizer",
        sub_category_name="收納文具",
    ),
    SceneTemplate(
        id="stat_org_03_contents",
        name="內容展示",
        name_en="Contents Display",
        product_type="stationery",
        description="收納文具打開展示內部容量與分隔設計",
        prompt=(
            "This stationery organizer fully opened and laid flat, revealing all interior compartments, elastic loops, mesh pockets, and zippered sections. "
            "Each compartment is filled with representative items: pens in loops, erasers in pockets, a calculator in the main section. "
            "Shot directly overhead at f/7.1 on a clean white surface with even diffused softbox lighting from above. "
            "The full interior layout is visible in a single frame, demonstrating the product's generous capacity and smart design. "
            "A 50mm lens provides distortion-free rendering of the organizer's true proportions. "
            "Clean, informative product photography that helps buyers understand exactly how much the organizer can hold."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="organizer",
        sub_category_name="收納文具",
    ),
    SceneTemplate(
        id="stat_org_04_comparison",
        name="尺寸對比",
        name_en="Size Comparison",
        product_type="stationery",
        description="收納文具與常見物品的尺寸對比展示",
        prompt=(
            "This stationery organizer photographed next to everyday reference objects: a standard smartphone, a 15cm ruler, and a paperback book. "
            "All items arranged on a clean white surface with a subtle centimeter grid printed underneath for precise scale reference. "
            "The organizer is the central hero product, positioned prominently with the reference objects flanking it. "
            "Shot from directly above at f/9 with a 50mm lens ensuring all objects remain tack-sharp and proportionally accurate. "
            "Even studio lighting from twin softboxes eliminates shadows that could distort perceived size. "
            "The composition is designed to give online shoppers an instant, intuitive understanding of the product's real-world dimensions."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="organizer",
        sub_category_name="收納文具",
    ),
    SceneTemplate(
        id="stat_org_05_stacked",
        name="堆疊展示",
        name_en="Stacked Display",
        product_type="stationery",
        description="多個收納文具的堆疊或排列展示",
        prompt=(
            "Multiple units of this stationery organizer stacked or arranged in a visually appealing cascading formation. "
            "Three to four organizers in different colors are staggered diagonally, each slightly overlapping the next. "
            "The front organizer is partially open to reveal interior contents while the others show exterior design variety. "
            "Shot at 50mm f/5.6 from a 25-degree angle on a clean light gray surface with soft gradient background. "
            "Dual softbox lighting at 45 degrees from both sides provides even illumination across all units without harsh shadows. "
            "The arrangement emphasizes the product's color options and stackable design, ideal for showcasing a full product line."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="organizer",
        sub_category_name="收納文具",
    ),
    # ==================== gift_wrap (禮品包裝) ====================
    SceneTemplate(
        id="stat_gift_01_wrapping",
        name="包裝過程",
        name_en="Wrapping Process",
        product_type="stationery",
        description="雙手使用包裝材料包裝禮物的過程展示",
        prompt=(
            "A pair of hands in the process of wrapping a small gift box using this wrapping paper and ribbon. "
            "The scene is captured mid-action: one hand holds the paper in place while the other pulls a satin ribbon taut. "
            "Scissors, tape dispenser, and extra ribbon spools are scattered naturally around the work area on a light wood table. "
            "Shot from a 45-degree overhead angle at 35mm f/3.2, the hands and wrapping materials in sharp focus. "
            "Warm, inviting lighting from a window on the left creates gentle shadows that add depth to the paper's texture. "
            "The image conveys the joyful, creative process of gift preparation with the wrapping materials as the hero product."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="gift_wrap",
        sub_category_name="禮品包裝",
    ),
    SceneTemplate(
        id="stat_gift_02_finished",
        name="完成效果",
        name_en="Finished Gift",
        product_type="stationery",
        description="使用包裝材料完成的精美禮品展示",
        prompt=(
            "A beautifully wrapped gift box using this wrapping paper, topped with a perfectly tied bow and a decorative gift tag. "
            "The finished gift sits on a clean white marble surface with a sprig of dried flowers beside it. "
            "The wrapping paper's pattern and texture are clearly visible, showcasing its premium quality and design. "
            "Shot at 60mm f/3.5 from a 20-degree front angle, the wrapped gift as the sole sharp subject against a soft pastel background. "
            "Soft key light from the upper right creates a gentle highlight on the ribbon and a subtle shadow on the surface. "
            "The composition evokes elegance and the excitement of receiving a thoughtfully wrapped present."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="gift_wrap",
        sub_category_name="禮品包裝",
    ),
    SceneTemplate(
        id="stat_gift_03_materials",
        name="材料展示",
        name_en="Materials Display",
        product_type="stationery",
        description="包裝紙、緞帶、蝴蝶結等材料的平鋪展示",
        prompt=(
            "A flat lay arrangement of this gift wrapping collection: sheets of wrapping paper partially unrolled, coils of satin and grosgrain ribbon, pre-made bows, and gift tags. "
            "All materials laid out on a clean white surface from a directly overhead perspective. "
            "The wrapping paper is fanned to show its full pattern repeat, with ribbon colors coordinating harmoniously. "
            "Shot at f/7.1 with a 50mm lens and even diffused lighting from two overhead softboxes for shadow-free coverage. "
            "Each item is spaced with intentional precision, creating a visually satisfying grid that highlights the collection's cohesive design. "
            "Professional product photography that helps buyers see the complete set of materials included in the packaging kit."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="gift_wrap",
        sub_category_name="禮品包裝",
    ),
    SceneTemplate(
        id="stat_gift_04_occasion",
        name="節慶場景",
        name_en="Holiday Occasion",
        product_type="stationery",
        description="禮品包裝在節慶場景中的應用展示",
        prompt=(
            "Wrapped gifts using this wrapping paper arranged beneath a decorated Christmas tree or beside festive holiday decor. "
            "Multiple gifts of varying sizes showcase the paper's versatility, surrounded by ornaments, pine cones, and string lights. "
            "Warm golden fairy light bokeh fills the background, creating a magical holiday atmosphere. "
            "Shot at 35mm f/2.4 from a low angle looking slightly upward at the gift arrangement. "
            "The warm color temperature of 3500K enhances the cozy festive mood with rich reds, golds, and greens. "
            "The composition connects the wrapping materials to the emotional joy of holiday gift-giving and celebration."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="gift_wrap",
        sub_category_name="禮品包裝",
    ),
    SceneTemplate(
        id="stat_gift_05_variety",
        name="花色展示",
        name_en="Pattern Variety",
        product_type="stationery",
        description="多種花色與設計的包裝紙排列展示",
        prompt=(
            "Multiple sheets of this wrapping paper collection displayed in an overlapping fan arrangement showing all available patterns and colors. "
            "Each sheet is partially visible, angled at 15-degree increments to reveal a different design: florals, geometric, stripes, and solids. "
            "Shot directly overhead at f/8 with a 50mm lens on a clean neutral gray background. "
            "Even diffused lighting from above ensures accurate color reproduction across every pattern with no hot spots or shadows. "
            "The papers are arranged from light to dark tones in a pleasing gradient progression. "
            "Clean, catalog-style product photography designed to help customers compare and choose their preferred pattern at a glance."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="gift_wrap",
        sub_category_name="禮品包裝",
    ),
]

TemplateRegistry.register("stationery", STATIONERY_TEMPLATES)
