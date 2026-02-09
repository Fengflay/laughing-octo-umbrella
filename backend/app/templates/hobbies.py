from app.templates.registry import SceneTemplate, TemplateRegistry

HOBBIES_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="hobbies_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="hobbies",
        description="純白背景，興趣文娛產品居中展示",
        prompt=(
            "Place this hobby/entertainment product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with a large softbox overhead at 45 degrees "
            "and two side fill lights for clean, even illumination. "
            "The product should be centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding and depth. "
            "Front-facing angle tilted 15 degrees to show details and dimension. "
            "Shot with a 70mm lens at f/9 for maximum depth of field across the entire product. "
            "Ultra-high resolution, crisp details on paint finish, molding quality, and printed surfaces. "
            "No other objects in frame. Color accuracy is critical for collectibles."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="hobbies",
        description="2x2 拼圖佈局，展示工藝、材質、功能等賣點",
        prompt=(
            "Create a professional product photography collage for this hobby/entertainment product. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the main design, artwork, and brand details. "
            "2) Close-up of the material quality: paint finish, plastic molding, or printed detail. "
            "3) Special feature: moving parts, hidden compartment, interactive mechanism, or accessory. "
            "4) Packaging or contents overview showing what is included. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all shots. "
            "Shot with a 60mm lens at f/8 for uniform sharpness in every panel. "
            "The layout conveys fun, quality, and attention to detail."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="hobbies",
        description="微距特寫，展示做工、塗裝、印刷等細節",
        prompt=(
            "Extreme macro close-up photography of this hobby/entertainment product showing craftsmanship details. "
            "Split into 2-3 detail zones: paint application quality and color gradients, "
            "sculpting or molding precision with sharp edges and fine details, "
            "and surface texture or printed artwork clarity. "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The detail level should showcase the product's premium craftsmanship. "
            "Focus stacking technique for maximum sharpness across detail zones. "
            "Professional collectible/hobby product macro photography with vivid color reproduction."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="hobbies",
        description="與手掌、硬幣等常見物品對比，直觀展示大小",
        prompt=(
            "This hobby/entertainment product photographed next to common reference objects for size: "
            "a hand holding or placed beside the product, a standard coin, "
            "and a smartphone or ruler nearby for scale comparison. "
            "All items arranged on a clean white surface with a subtle grid pattern for measurement. "
            "The product is the hero element in the center. "
            "Clean white background, even studio lighting from an overhead softbox. "
            "Shot with a 50mm lens at f/11 to keep all objects tack-sharp. "
            "The items are proportionally realistic to each other. "
            "The composition clearly communicates the product's actual physical size."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_05_display_scene",
        name="展示場景",
        name_en="Display Scene",
        product_type="hobbies",
        description="書架或桌面展示場景",
        prompt=(
            "This hobby/entertainment product displayed on a stylish wooden shelf or clean desk setup. "
            "The product is the hero piece, placed prominently on a shelf alongside books, "
            "small potted plants, and tasteful decor items that complement without competing. "
            "Warm ambient room lighting with a focused spotlight accent on the product. "
            "The background shows a cozy living room or study with soft bokeh. "
            "Shot with a 50mm lens at f/2.8, shallow depth of field keeping the product sharp "
            "while the room environment provides warm, lived-in context. "
            "Camera at product eye level for an intimate perspective. "
            "Warm color tones around 4800K. Collector's display lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_06_play_scene",
        name="玩樂場景",
        name_en="Play Scene",
        product_type="hobbies",
        description="人們享受產品的歡樂使用場景",
        prompt=(
            "People actively enjoying this hobby/entertainment product in a natural, fun setting. "
            "A bright living room or game table with the product being used: "
            "hands interacting with a board game, a model being assembled, or a collectible being admired. "
            "Genuine expressions of joy and engagement visible on faces. "
            "Warm, cheerful natural window light mixed with cozy interior lighting. "
            "Shot with a 35mm lens at f/2.4 for an intimate, documentary feel "
            "with beautiful background separation. "
            "Camera at table level, capturing the moment of interaction. "
            "The product is the center of activity. Authentic hobby lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_07_collection_display",
        name="收藏展示",
        name_en="Collection Display",
        product_type="hobbies",
        description="產品作為收藏品的精美展示",
        prompt=(
            "This hobby/entertainment product showcased as a prized collectible in an elegant display setting. "
            "The product placed on a glass shelf or in a display case with dramatic museum-style lighting: "
            "focused spotlight from above creating a halo effect, "
            "with subtle blue or amber accent lighting from below. "
            "Other collection pieces visible but soft in the background. "
            "Shot with an 85mm lens at f/3.2 for stunning subject isolation, "
            "the product appears luminous and precious against a dark background. "
            "Low camera angle at 15 degrees looking slightly upward for a heroic perspective. "
            "Premium collector's item photography with gallery-worthy presentation."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_08_gift_bundle",
        name="禮品組合",
        name_en="Gift Bundle",
        product_type="hobbies",
        description="禮品包裝展示，適合送禮場景",
        prompt=(
            "This hobby/entertainment product styled as a gift-ready package in a festive flat lay. "
            "The product displayed alongside gift wrapping elements: "
            "a decorative gift box, ribbon, tissue paper, a handwritten gift tag, and confetti. "
            "Top-down perspective on a clean cream or kraft paper surface. "
            "Each item neatly spaced with intentional arrangement suggesting a curated gift. "
            "The hero product is centrally placed and unwrapped, showing its full appeal. "
            "Shot overhead with a 35mm lens at f/7.1, even diffused softbox lighting "
            "for uniform sharpness and vibrant colors on wrapping materials. "
            "Professional gift photography conveying celebration and thoughtful giving."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="hobbies_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="hobbies",
        description="展示品牌調性的興趣生活美學",
        prompt=(
            "This hobby/entertainment product styled in a cozy, aspirational lifestyle scene. "
            "A warm evening vignette: the product on a leather-topped desk or vintage wooden table "
            "alongside a cup of tea, an open journal, reading glasses, and warm fairy lights in the background. "
            "Golden hour or warm lamp light creating rich amber tones and intimate shadows. "
            "Shot with a 40mm lens at f/4.0 from a slightly elevated angle. "
            "Rich, warm color palette with deep wood tones and soft amber highlights. "
            "The composition conveys personal passion, relaxation, and the joy of hobbies. "
            "Premium lifestyle brand aesthetic with a nostalgic, editorial warmth."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== models (模型) ====================
    SceneTemplate(
        id="hobby_mod_01_built",
        name="成品展示",
        name_en="Completed Model Display",
        product_type="hobbies",
        description="完成組裝的模型成品展示",
        prompt=(
            "A fully assembled and painted model displayed on a professional turntable or acrylic riser "
            "against a clean gradient background transitioning from dark gray to black. "
            "The model is positioned at a dynamic three-quarter angle showing its best features and detail work. "
            "Shot with an 85mm lens at f/4.0, focused spotlight from above-left creating dramatic highlights "
            "on the model's painted surfaces and casting defined shadows for dimensionality. "
            "A subtle rim light from behind separates the model from the dark background. "
            "Every painted detail, decal, and weathering effect is visible in ultra-high resolution. "
            "Professional scale model photography with gallery-quality presentation and museum lighting."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="models",
        sub_category_name="模型",
    ),
    SceneTemplate(
        id="hobby_mod_02_building",
        name="組裝過程",
        name_en="Model Building Process",
        product_type="hobbies",
        description="模型正在被組裝的過程展示",
        prompt=(
            "A model kit being actively assembled on a well-organized hobby workbench: "
            "hands holding tweezers or a hobby knife, carefully attaching a part to the partially built model. "
            "Modeling tools scattered nearby: cutting mat, cement glue, paint jars, and a magnifying lamp. "
            "The partially completed model shows the progression from kit to finished piece. "
            "Shot with a 45mm lens at f/3.2 from a slight overhead angle at workbench height, "
            "the hands and model in sharp focus while tools and parts provide contextual depth. "
            "Warm desk lamp lighting creates an intimate workshop atmosphere. "
            "The image captures the meditative focus and craftsmanship of the model building hobby."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="models",
        sub_category_name="模型",
    ),
    SceneTemplate(
        id="hobby_mod_03_parts",
        name="零件展示",
        name_en="Model Parts Display",
        product_type="hobbies",
        description="模型零件和水口板的平鋪展示",
        prompt=(
            "All model kit parts and sprues laid out in an organized flat lay on a clean cutting mat surface. "
            "The sprues are arranged by runner letter or type, with the instruction manual open nearby "
            "and a few key parts already clipped and cleaned, placed beside the uncut runners for contrast. "
            "Shot from directly overhead with a 35mm lens at f/7.1, "
            "even diffused studio lighting at 5500K ensuring every part number and detail is clearly readable. "
            "The arrangement shows the full scope and complexity of the kit. "
            "Professional hobby product photography that communicates part count, quality of molding, "
            "and the satisfying challenge awaiting the builder."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="models",
        sub_category_name="模型",
    ),
    SceneTemplate(
        id="hobby_mod_04_shelf",
        name="展示櫃",
        name_en="Model Display Cabinet",
        product_type="hobbies",
        description="模型收藏品在展示櫃中的陳列",
        prompt=(
            "This completed model displayed inside a glass display cabinet alongside other finished models, "
            "arranged on multiple shelves with LED strip lighting illuminating each shelf from above. "
            "The hero model is on the center shelf at eye level, slightly forward for prominence. "
            "Shot with a 50mm lens at f/2.8 through the glass door, the hero model in sharp focus "
            "while other collection pieces provide soft, colorful background depth. "
            "The cabinet LEDs create warm, even illumination on each model surface. "
            "Camera at straight-on eye level for a natural viewing perspective. "
            "The image conveys a proud collector's display, organized passion, and the reward of completed builds."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="models",
        sub_category_name="模型",
    ),
    SceneTemplate(
        id="hobby_mod_05_detail",
        name="細節塗裝",
        name_en="Painted Detail Close-up",
        product_type="hobbies",
        description="模型塗裝細節的微距特寫",
        prompt=(
            "Extreme macro close-up of this model's painted surface showing the artistry of hand-painted details: "
            "panel line wash accents, weathering effects, decal placement precision, and color transitions. "
            "Shot with a 100mm macro lens at f/3.2, very shallow depth of field "
            "isolating a specific detail area such as a cockpit, face, weapon, or engine section. "
            "Ring light illumination reveals the subtle layering of paint, wash, and dry-brush techniques. "
            "The level of detail visible demonstrates master-level craftsmanship and justifies premium model quality. "
            "Professional scale model macro photography with accurate color reproduction and precise highlight control."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="models",
        sub_category_name="模型",
    ),
    # ==================== board_games (桌遊) ====================
    SceneTemplate(
        id="hobby_bg_01_playing",
        name="遊玩場景",
        name_en="Board Game Playing Scene",
        product_type="hobbies",
        description="人們圍坐遊玩桌遊的歡樂場景",
        prompt=(
            "A group of friends gathered around a table actively playing this board game, "
            "with game pieces moved into mid-game positions and players deliberating their next moves. "
            "Hands reaching for dice, cards, or game pieces create dynamic energy in the frame. "
            "Shot with a 35mm lens at f/2.4 from a slightly elevated table-corner angle, "
            "the game board and nearest player's hands in sharp focus with other players softly blurred. "
            "Warm overhead pendant lighting and natural window light create a cozy game night atmosphere. "
            "Genuine expressions of concentration, excitement, and laughter visible. "
            "The image captures the social joy and engagement that this board game creates."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="board_games",
        sub_category_name="桌遊",
    ),
    SceneTemplate(
        id="hobby_bg_02_setup",
        name="開局擺放",
        name_en="Board Game Setup",
        product_type="hobbies",
        description="桌遊完整開局擺放的俯視展示",
        prompt=(
            "This board game fully set up and ready to play, photographed from directly overhead. "
            "All pieces, tokens, cards, and dice placed in their starting positions on the game board. "
            "Player areas arranged around the board with score tracks reset and card decks shuffled. "
            "Shot with a 35mm lens at f/6.3 from a top-down perspective, "
            "even diffused studio lighting at 5500K ensuring all text, artwork, and components are clearly legible. "
            "The game board fills most of the frame with a clean table surface visible at the edges. "
            "The composition showcases the game's visual design, component quality, and the excitement "
            "of a fresh game about to begin."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="board_games",
        sub_category_name="桌遊",
    ),
    SceneTemplate(
        id="hobby_bg_03_components",
        name="配件展示",
        name_en="Game Components Display",
        product_type="hobbies",
        description="桌遊所有配件整齊展開的展示",
        prompt=(
            "All game components from this board game spread out in an organized flat lay: "
            "the game board unfolded at center, surrounded by sorted piles of cards, miniatures or tokens, "
            "dice, player boards, instruction booklet, and any special accessories. "
            "Shot from directly overhead with a 35mm lens at f/7.1 on a clean dark felt or wooden surface. "
            "Even, bright studio lighting at 5500K ensures every component is clearly visible. "
            "Each component group is neatly arranged with intentional spacing for easy identification. "
            "The composition serves as a complete contents overview, communicating the game's depth, "
            "component quality, and impressive value for the price."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="board_games",
        sub_category_name="桌遊",
    ),
    SceneTemplate(
        id="hobby_bg_04_cards",
        name="卡牌展示",
        name_en="Card Game Display",
        product_type="hobbies",
        description="卡牌遊戲的卡片展開展示",
        prompt=(
            "A selection of cards from this card game fanned out in an attractive arc or spread pattern, "
            "showing the front artwork of five to seven key cards with vibrant illustrations visible. "
            "The cards rest on a dark velvet or wooden surface that makes the artwork pop. "
            "Shot with a 50mm lens at f/4.0 from a 25-degree overhead angle, "
            "the front cards in sharp focus with the fanned ends falling into gentle bokeh. "
            "Warm spotlight illumination from above highlights the card art and foil or holographic elements. "
            "The composition showcases the artistic quality of the card design, printing precision, "
            "and the visual excitement of discovering the game's characters or abilities."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="board_games",
        sub_category_name="桌遊",
    ),
    SceneTemplate(
        id="hobby_bg_05_box",
        name="盒裝展示",
        name_en="Game Box Display",
        product_type="hobbies",
        description="桌遊盒裝打開展示內容物",
        prompt=(
            "The game box opened at an attractive angle with the lid leaning against the base, "
            "revealing the organized interior with components visible inside: card dividers, "
            "plastic trays holding miniatures, and neatly packed rulebooks. "
            "The box cover artwork is prominently displayed on the tilted lid. "
            "Shot with a 50mm lens at f/4.5 from a three-quarter front angle at table height, "
            "the box and its contents in sharp focus against a clean, slightly blurred background. "
            "Even studio lighting at 5500K highlights the box art quality and the premium unboxing experience. "
            "The image communicates premium packaging, organized contents, and the thrill of opening a new game."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="board_games",
        sub_category_name="桌遊",
    ),
    # ==================== collectibles (收藏品) ====================
    SceneTemplate(
        id="hobby_col_01_display",
        name="展示擺放",
        name_en="Collectible on Display",
        product_type="hobbies",
        description="收藏品放在展示架上的精美展示",
        prompt=(
            "This collectible item placed on an elegant acrylic riser or wooden display stand "
            "against a clean dark gradient background, museum-style presentation. "
            "Dramatic focused spotlight from above-left creates strong highlights on the collectible's surface "
            "with a subtle fill light from the right preventing harsh shadows. "
            "Shot with an 85mm lens at f/3.5 from a slightly low angle for a heroic, imposing perspective. "
            "The collectible appears luminous and precious, every surface detail rendered in sharp focus. "
            "A subtle reflection on the acrylic base adds depth. "
            "Premium collectible display photography with gallery-worthy lighting and composition."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="collectibles",
        sub_category_name="收藏品",
    ),
    SceneTemplate(
        id="hobby_col_02_unboxing",
        name="開箱展示",
        name_en="Collectible Unboxing",
        product_type="hobbies",
        description="收藏品開箱瞬間的展示",
        prompt=(
            "This collectible being unboxed: the premium packaging opened with tissue paper pulled aside, "
            "the collectible partially lifted from its molded foam insert, revealing the moment of discovery. "
            "The box, protective materials, certificate of authenticity, and any accessories are all visible. "
            "Shot with a 50mm lens at f/3.5 from a slight overhead angle, "
            "the collectible and hands in sharp focus with the packaging providing premium context. "
            "Warm, inviting lighting creates excitement and anticipation in the frame. "
            "The image captures the premium unboxing experience, communicating quality packaging, "
            "collector-grade protection, and the excitement of adding a new piece to a collection."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="collectibles",
        sub_category_name="收藏品",
    ),
    SceneTemplate(
        id="hobby_col_03_detail",
        name="細節特寫",
        name_en="Collectible Detail Close-up",
        product_type="hobbies",
        description="收藏品工藝細節的微距特寫",
        prompt=(
            "Extreme macro close-up of this collectible showing its finest craftsmanship details: "
            "hand-painted facial expressions, sculpted fabric texture, metallic finish quality, "
            "or intricate base diorama elements. "
            "Shot with a 100mm macro lens at f/3.0, very shallow depth of field "
            "with the key detail area in pin-sharp focus and surrounding areas artistically blurred. "
            "Ring light with a warm gel provides even illumination that reveals paint layering and surface quality. "
            "The level of micro-detail visible justifies the collectible's premium value "
            "and showcases the artisan craftsmanship involved in its creation."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="collectibles",
        sub_category_name="收藏品",
    ),
    SceneTemplate(
        id="hobby_col_04_shelf",
        name="收藏牆",
        name_en="Collection Display Wall",
        product_type="hobbies",
        description="收藏品在展示牆上的整體陳列",
        prompt=(
            "A dedicated display wall or shelving unit filled with collectible items from this series, "
            "with the hero piece positioned at the prime center-eye-level location. "
            "LED strip lighting illuminates each shelf, and the collection is organized by theme or series. "
            "Shot with a 35mm lens at f/3.5 from a straight-on perspective, "
            "the hero collectible in sharp focus while the surrounding collection provides impressive depth and scale. "
            "The warm LED lighting creates an inviting collector's room atmosphere. "
            "The image conveys the pride of a curated collection, the visual impact of a display wall, "
            "and the aspirational goal of building a complete set."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="collectibles",
        sub_category_name="收藏品",
    ),
    SceneTemplate(
        id="hobby_col_05_comparison",
        name="尺寸對比",
        name_en="Size Comparison",
        product_type="hobbies",
        description="收藏品與日常物品的尺寸對比",
        prompt=(
            "This collectible placed next to a common everyday object for intuitive size reference: "
            "a soda can, a smartphone, or a standard ballpoint pen positioned alongside. "
            "Both items rest on a clean white surface with subtle shadow grounding. "
            "Shot with a 50mm lens at f/6.3 from a front angle at the collectible's eye level, "
            "both the collectible and reference object in sharp focus with clean white background. "
            "Even studio lighting at 5500K provides accurate color and consistent illumination on both objects. "
            "The composition clearly and immediately communicates the collectible's real-world physical scale, "
            "helping online buyers understand exactly what size to expect."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="collectibles",
        sub_category_name="收藏品",
    ),
]

TemplateRegistry.register("hobbies", HOBBIES_TEMPLATES)
