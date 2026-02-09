from app.templates.registry import SceneTemplate, TemplateRegistry

TOYS_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="toys_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="toys",
        description="純白背景，玩具正面展示，色彩鮮明",
        prompt=(
            "This toy/baby product on a pure white background. "
            "Professional toy photography with bright, cheerful lighting. "
            "The product is centered, showing its colorful design and appeal. "
            "Colors should appear vivid and accurate. "
            "Occupies about 80% of the frame. "
            "Shot at f/8 for maximum sharpness across the entire product. "
            "Fun, inviting commercial product photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="toys",
        description="展示安全材質、教育功能、適用年齡等賣點",
        prompt=(
            "Create a professional toy/baby product infographic. "
            "Show this product on a soft pastel or white background. "
            "Add friendly, colorful callout elements pointing to key features: "
            "safety material certification, age recommendation, educational benefits, "
            "and special features (washable, non-toxic, battery-free). "
            "Fun, parent-friendly design with rounded, soft typography. "
            "Even diffused lighting to ensure all callout labels are clearly legible. "
            "Child-safe and trustworthy aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="toys",
        description="材質安全性、做工品質、小零件細節",
        prompt=(
            "Close-up detail shots of this toy/baby product showing quality and safety. "
            "Focus on: smooth edges (no sharp points), material quality, "
            "stitching or assembly quality, paint finish (non-toxic), and any safety features. "
            "Bright, clean photography with even lighting. "
            "Shot with a macro lens at f/4 to isolate fine textures and seams. "
            "The details should reassure parents about safety and quality. "
            "Professional baby/toy product detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="toys",
        description="孩子手中展示，直觀展示大小比例",
        prompt=(
            "This toy/baby product shown with a child's hands or next to common objects "
            "to demonstrate its actual size. "
            "A child's hands gently holding or touching the product. "
            "Clean, soft background. Warm, gentle lighting. "
            "Straight-on angle at the child's eye level for natural perspective. "
            "The image clearly shows the product's scale for parents. "
            "Safe, warm, and inviting photography aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_05_play_scene",
        name="遊戲場景",
        name_en="Play Scene",
        product_type="toys",
        description="孩子開心玩耍的場景",
        prompt=(
            "A happy child playing with this toy in a bright, cheerful playroom. "
            "The child is engaged and smiling, showing genuine enjoyment. "
            "Colorful but not cluttered background with child-friendly decor. "
            "Warm, natural lighting creating a joyful atmosphere. "
            "Shot from a low angle at the child's level, f/2.8 to softly blur the background. "
            "The image captures the fun and educational value of the toy. "
            "Authentic family lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_06_nursery_scene",
        name="兒童房場景",
        name_en="Nursery Scene",
        product_type="toys",
        description="兒童房/遊戲區擺放效果",
        prompt=(
            "This toy/baby product styled in a beautiful nursery or children's room. "
            "Pastel colors, cute decor, organized toy shelf or play area. "
            "The product is placed naturally in the child's space. "
            "Soft, warm lighting creating a safe, cozy atmosphere. "
            "Wide-angle composition at f/5.6 to show the room context while keeping the product sharp. "
            "Interior styling photography for parents who care about aesthetics. "
            "Modern nursery design magazine aesthetic."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_07_educational",
        name="教育展示",
        name_en="Educational Value",
        product_type="toys",
        description="展示教育功能、益智效果",
        prompt=(
            "This toy/baby product shown in an educational context. "
            "A child focused and learning while interacting with the product. "
            "Clean, organized learning space with books and art supplies nearby. "
            "The image conveys cognitive development, creativity, or motor skill building. "
            "Bright, encouraging photography style with soft window light from the side. "
            "Shallow depth of field at f/2.8 keeping the child and product in focus. "
            "Educational toy marketing photography."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_08_package_contents",
        name="配件全家福",
        name_en="Package Contents",
        product_type="toys",
        description="展示包裝內所有配件和玩法",
        prompt=(
            "Complete contents of this toy/baby product neatly arranged on a clean surface. "
            "Show: the main product and all included pieces, accessories, and instructions. "
            "Top-down flat lay with cheerful, colorful arrangement. "
            "Each piece clearly visible and separated. "
            "Shot directly overhead at f/8 with diffused softbox lighting for even coverage. "
            "The layout shows everything the buyer will receive. "
            "Bright, fun 'what's in the box' photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="toys_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="toys",
        description="溫馨家庭互動場景，展示品牌溫度",
        prompt=(
            "A warm family scene with parent and child enjoying this toy together. "
            "Bright, airy living room with natural sunlight. "
            "Genuine smiles and connection between parent and child. "
            "The toy facilitates bonding and shared joy. "
            "Shot at golden hour with backlight streaming through windows, f/2.4 for dreamy bokeh. "
            "Emotional, heartwarming family lifestyle photography. "
            "The image conveys love, safety, and quality family time."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== blocks (積木) ====================
    SceneTemplate(
        id="toy_blk_01_built",
        name="成品展示",
        name_en="Completed Build Display",
        product_type="toys",
        description="積木成品的完整展示",
        prompt=(
            "A fully assembled block construction displayed on a clean white or light wood surface, showcasing the completed model in all its colorful detail. "
            "The build is positioned at a dynamic three-quarter angle to reveal the structure's depth, architectural details, and interlocking precision. "
            "Bright, even lighting from a large overhead softbox ensures vivid, accurate colors with no harsh shadows obscuring any part of the build. "
            "A subtle reflection on the glossy surface adds a premium product photography feel to the toy presentation. "
            "Shot at 60mm f/5.6 to capture the entire structure with edge-to-edge sharpness and a clean, distraction-free background."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="blocks",
        sub_category_name="積木",
    ),
    SceneTemplate(
        id="toy_blk_02_process",
        name="拼搭過程",
        name_en="Building Process",
        product_type="toys",
        description="孩子正在拼搭積木的過程",
        prompt=(
            "A child's hands actively connecting and stacking building blocks on a play mat, captured mid-construction with a partially completed model visible. "
            "Colorful loose blocks are scattered around the build area, and the child's focused fingers are pressing a piece into place with concentration. "
            "Warm, natural playroom light from a nearby window illuminates the scene with a cheerful, inviting glow on the bright plastic surfaces. "
            "The background shows a tidy playroom environment slightly out of focus to maintain context without distraction. "
            "Shot at 50mm f/2.8 from the child's table-level perspective to create an immersive, engaging view of the building activity."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="blocks",
        sub_category_name="積木",
    ),
    SceneTemplate(
        id="toy_blk_03_pieces",
        name="零件展示",
        name_en="Pieces Spread Display",
        product_type="toys",
        description="所有積木零件整齊排列展示",
        prompt=(
            "All building block pieces from this set spread out neatly on a clean white surface in an organized flat-lay arrangement sorted by color, size, or type. "
            "Each piece group is clearly separated with consistent spacing, creating a satisfying visual grid that shows the full scope of the set. "
            "Small count labels or grouping lines subtly indicate quantities for each unique piece type in the collection. "
            "Bright, perfectly even overhead studio lighting ensures every piece casts minimal shadow and displays its true color accurately. "
            "Shot directly overhead at f/8 with a 35mm lens to capture the entire spread with uniform sharpness across hundreds of individual pieces."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="blocks",
        sub_category_name="積木",
    ),
    SceneTemplate(
        id="toy_blk_04_instruction",
        name="說明書展示",
        name_en="Instruction Manual Display",
        product_type="toys",
        description="積木搭配說明書一起展示",
        prompt=(
            "This building block set displayed alongside its open instruction manual, with the manual showing a colorful step-by-step build guide. "
            "The partially assembled model sits next to the booklet, with some loose pieces arranged nearby ready for the next building step. "
            "The instruction page is clearly legible with bright diagrams, and the blocks match the colors shown in the guide for visual consistency. "
            "Warm overhead lighting provides even illumination on both the printed manual pages and the glossy block surfaces without glare. "
            "Shot at 45mm f/4 from a 45-degree angle to show both the manual content and the three-dimensional block assembly in a single frame."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="blocks",
        sub_category_name="積木",
    ),
    SceneTemplate(
        id="toy_blk_05_display",
        name="展示架",
        name_en="Display Shelf Showcase",
        product_type="toys",
        description="完成的積木模型放在展示架上",
        prompt=(
            "A completed building block model proudly displayed on a clean floating shelf or glass display case in a child's bedroom or living room. "
            "The model is centered on the shelf with subtle accent lighting from a small LED strip below, giving it a collectible, museum-quality presentation. "
            "Other completed builds or books are visible on adjacent shelves in the soft background, suggesting a collection and hobby lifestyle. "
            "Warm room lighting creates a cozy, lived-in atmosphere that contextualizes the display as part of everyday home decor. "
            "Shot at 50mm f/2.4 from eye level to frame the shelf and model with a naturally blurred background that emphasizes the showcase presentation."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="blocks",
        sub_category_name="積木",
    ),
    # ==================== puzzle (益智玩具) ====================
    SceneTemplate(
        id="toy_puz_01_playing",
        name="遊玩場景",
        name_en="Playing Scene",
        product_type="toys",
        description="孩子正在玩益智玩具的場景",
        prompt=(
            "A young child deeply engaged in playing with this puzzle toy on a soft play mat in a bright, cheerful playroom with pastel-colored walls. "
            "The child's expression shows concentration and delight as they manipulate the puzzle pieces with small, careful hands. "
            "Colorful puzzle components are spread in front of the child, with some pieces already correctly placed and others waiting to be solved. "
            "Soft natural daylight from a large window fills the room with warm, even illumination that highlights the child's features and toy colors. "
            "Shot at 50mm f/2.4 from the child's seated level to capture their genuine engagement with the puzzle in an authentic, relatable moment."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="puzzle",
        sub_category_name="益智玩具",
    ),
    SceneTemplate(
        id="toy_puz_02_educational",
        name="教育場景",
        name_en="Educational Context",
        product_type="toys",
        description="益智玩具在教育學習環境中的展示",
        prompt=(
            "This puzzle toy placed on a small children's desk in a Montessori-style learning environment alongside alphabet cards, counting beads, and crayons. "
            "The educational setting features natural wood furniture, organized low shelves with labeled bins, and child-height accessibility throughout. "
            "The puzzle toy is positioned as the centerpiece learning tool with its educational function clearly visible and inviting interaction. "
            "Bright, clean classroom lighting with large windows providing abundant natural light and a positive, stimulating learning atmosphere. "
            "Shot at 35mm f/4 from a child's eye-level perspective to present the learning space as a child would experience it."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="puzzle",
        sub_category_name="益智玩具",
    ),
    SceneTemplate(
        id="toy_puz_03_family",
        name="親子互動",
        name_en="Parent-Child Play",
        product_type="toys",
        description="父母和孩子一起玩益智玩具的場景",
        prompt=(
            "A parent and child sitting together on a cozy living room rug, collaborating on this puzzle toy with smiles and engaged body language. "
            "The parent is pointing at a piece or gently guiding the child's hand, showing a warm teaching moment and emotional connection. "
            "The puzzle pieces are spread between them on the carpet, with the partially solved puzzle visible as shared progress. "
            "Golden afternoon light streams through sheer curtains, bathing the family scene in warm, inviting tones that evoke comfort and bonding. "
            "Shot at 35mm f/2.8 from a low angle to capture both faces and the puzzle activity in a heartwarming family lifestyle composition."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="puzzle",
        sub_category_name="益智玩具",
    ),
    SceneTemplate(
        id="toy_puz_04_difficulty",
        name="難度展示",
        name_en="Difficulty Levels Display",
        product_type="toys",
        description="展示益智玩具不同難度等級",
        prompt=(
            "Multiple difficulty levels of this puzzle toy arranged side by side from simplest to most complex on a clean white surface. "
            "Each difficulty level is clearly labeled with age-appropriate indicators, progressing from large simple shapes to intricate multi-step challenges. "
            "Color coding or visual markers distinguish each level, making the progression path intuitive and visually appealing for parent buyers. "
            "Bright, even studio lighting with a large diffusion panel ensures every detail of each difficulty level is clearly visible and color-accurate. "
            "Shot overhead at f/7.1 from directly above to present all difficulty levels in a clean, organized comparison layout."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="puzzle",
        sub_category_name="益智玩具",
    ),
    SceneTemplate(
        id="toy_puz_05_collection",
        name="系列收集",
        name_en="Collection Display",
        product_type="toys",
        description="多款益智玩具系列展示",
        prompt=(
            "A curated collection of puzzle toys from the same product series displayed on a low shelf or play table, each one showing a different theme or challenge. "
            "The collection is arranged in a visually pleasing grid or arc formation, with each toy angled slightly to show its unique design and color scheme. "
            "Small plant pots, children's books, and a wooden toy box in the background suggest a well-curated playroom environment. "
            "Warm, natural lighting fills the scene with a cheerful ambiance, making the collection look inviting and collectible. "
            "Shot at 35mm f/4 from a slightly elevated angle to capture the full collection breadth while showing each toy's dimensional details."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="puzzle",
        sub_category_name="益智玩具",
    ),
    # ==================== baby (嬰幼兒玩具) ====================
    SceneTemplate(
        id="toy_baby_01_crib",
        name="嬰兒床場景",
        name_en="Crib Setting",
        product_type="toys",
        description="玩具在嬰兒床中或附近的場景",
        prompt=(
            "This baby toy placed inside or hanging from a beautiful white wooden crib in a softly decorated nursery with pastel walls and a mobile overhead. "
            "The crib has clean white linens and a small knitted blanket, creating a safe, cozy environment where the toy looks naturally at home. "
            "A gentle nightlight or diffused lamp casts a warm, soothing glow across the crib area with no harsh shadows to disturb the peaceful setting. "
            "Soft plush elements and a small stuffed animal nearby add context without cluttering the serene nursery composition. "
            "Shot at 40mm f/2.8 from a parent's eye-level looking down into the crib, capturing the intimate perspective of checking on a sleeping baby's space."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="baby",
        sub_category_name="嬰幼兒玩具",
    ),
    SceneTemplate(
        id="toy_baby_02_teething",
        name="咬咬樂",
        name_en="Teething Toy Close-up",
        product_type="toys",
        description="嬰兒安全咬咬樂玩具的特寫",
        prompt=(
            "A close-up of this baby-safe teething toy on a clean, soft surface showing its smooth, rounded edges and food-grade silicone material. "
            "The teething ring or toy is slightly angled to display the textured surfaces designed for soothing baby gums during teething. "
            "Soft, diffused lighting from above reveals the translucent or matte material quality with gentle pastel colors that appeal to parents. "
            "A small BPA-free or safety certification icon is subtly suggested by the overall clinical yet friendly presentation. "
            "Shot at 90mm macro f/3.5 to capture the fine texture details and material quality that reassure parents about the product's safety."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="baby",
        sub_category_name="嬰幼兒玩具",
    ),
    SceneTemplate(
        id="toy_baby_03_sensory",
        name="感官探索",
        name_en="Sensory Exploration Toy",
        product_type="toys",
        description="色彩豐富的感官探索玩具展示",
        prompt=(
            "A vibrant, colorful sensory toy displayed on a soft white play mat, showing its variety of textures, crinkle areas, and tactile elements in vivid detail. "
            "Each section of the toy features a different material such as smooth satin, bumpy silicone, crinkly fabric, and soft velour for multi-sensory stimulation. "
            "Bright, cheerful overhead lighting makes every color pop while maintaining a soft, baby-friendly warmth in the overall image tone. "
            "The toy is slightly compressed or manipulated to show its squeezable, flexible nature and the various interactive elements. "
            "Shot at 50mm f/4 from a 45-degree angle to capture the three-dimensional textures and the playful, engaging design from a parent's browsing perspective."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="baby",
        sub_category_name="嬰幼兒玩具",
    ),
    SceneTemplate(
        id="toy_baby_04_bath",
        name="洗澡玩具",
        name_en="Bath Toy Scene",
        product_type="toys",
        description="洗澡玩具在泡泡水中的場景",
        prompt=(
            "This colorful bath toy floating in a baby bathtub filled with warm, bubbly water and soft white foam on the surface. "
            "Gentle soap bubbles catch the light around the toy, creating a playful, joyful bath time atmosphere with iridescent reflections. "
            "The bathtub edge and a rubber duck or small towel are partially visible as context props for the bathing scenario. "
            "Warm overhead bathroom lighting with a slight side fill creates appealing highlights on the wet toy surfaces and water droplets. "
            "Shot at 50mm f/3.2 from just above water level to capture the toy floating among the bubbles with a shallow depth of field that isolates the product."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="baby",
        sub_category_name="嬰幼兒玩具",
    ),
]

TemplateRegistry.register("toys", TOYS_TEMPLATES)
