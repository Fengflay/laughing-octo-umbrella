from app.templates.registry import SceneTemplate, TemplateRegistry

HOME_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="home_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="home",
        description="純白背景，家居用品正面展示",
        prompt=(
            "This home product on a pure white background. "
            "Professional product photography with soft, even studio lighting. "
            "The product is centered, showing its form and design clearly. "
            "Slight shadow for natural grounding. "
            "Occupies about 80% of the frame. "
            "Shot at f/9 with dual strip softboxes for even, wrap-around illumination. "
            "Clean, crisp commercial e-commerce photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="home",
        description="展示材質、功能、容量等核心賣點",
        prompt=(
            "Create a professional home product infographic. "
            "Show this product on a clean white background with elegant callout lines "
            "pointing to 3-4 key features: material quality, functional design elements, "
            "capacity/dimensions, and any special features (eco-friendly, foldable, waterproof). "
            "Clean Scandinavian design aesthetic with modern typography. "
            "Use flat, diffused lighting to minimize glare on text callouts. "
            "Style reference: IKEA or MUJI product feature page."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="home",
        description="材質紋理、做工細節、五金配件特寫",
        prompt=(
            "Close-up detail shots of this home product showing quality and craftsmanship. "
            "Focus on: material texture (wood grain, fabric weave, ceramic glaze), "
            "connection joints, hardware quality, and finish details. "
            "Macro photography with precise lighting. "
            "Shot at f/2.8 with raking side light to accentuate surface texture and grain. "
            "The details should convey quality and durability. "
            "Professional product detail photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="home",
        description="放在房間中或與常見物品對比大小",
        prompt=(
            "This home product placed in context to show its real-world size. "
            "Shown on a table, shelf, or counter with common household items nearby for scale: "
            "a coffee mug, books, or a plant. "
            "Clean, minimalist setting. Bright, natural lighting. "
            "Shot from a straight-on eye-level angle at f/8 for uniform sharpness across all items. "
            "The composition clearly communicates the product's dimensions. "
            "Practical e-commerce size reference photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_05_living_room",
        name="客廳場景",
        name_en="Living Room Scene",
        product_type="home",
        description="客廳/書房使用場景展示",
        prompt=(
            "This home product styled in a beautiful, modern living room setting. "
            "Scandinavian or Japanese minimalist interior design aesthetic. "
            "Natural window light filling the space with warmth. "
            "The product is placed naturally among other tasteful decor items. "
            "Shot at 24mm f/2.8 to capture the room context while keeping the product as the focal point. "
            "Lifestyle interior photography that helps buyers visualize the product in their home. "
            "Warm, inviting atmosphere."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_06_kitchen_bath",
        name="廚房/浴室場景",
        name_en="Kitchen or Bath Scene",
        product_type="home",
        description="廚房或浴室中的使用場景",
        prompt=(
            "This home product in a clean, modern kitchen or bathroom setting. "
            "Bright, well-organized space with natural or warm artificial lighting. "
            "The product is placed in its intended use location. "
            "Other complementary items visible (plants, towels, cooking utensils). "
            "Shot at 35mm f/3.5 with window backlight for a bright, airy editorial feel. "
            "Interior styling photography with a fresh, clean aesthetic. "
            "The image helps buyers imagine the product in their own space."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_07_in_use",
        name="使用展示",
        name_en="In Use Demonstration",
        product_type="home",
        description="展示產品實際使用的效果",
        prompt=(
            "A person using this home product in a natural, everyday scenario. "
            "The image clearly demonstrates the product's function and ease of use. "
            "Bright, clean setting with natural lighting. "
            "The person's interaction with the product looks effortless and natural. "
            "Shot at 50mm f/2.0 with the subject and product in sharp focus against a softly blurred room. "
            "Lifestyle photography that communicates practical value. "
            "Warm, relatable home life aesthetic."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_08_organization",
        name="收納/組合圖",
        name_en="Organization Display",
        product_type="home",
        description="展示收納效果或產品組合搭配",
        prompt=(
            "This home product shown in an organized arrangement, "
            "demonstrating its storage capacity or how it works as part of a set. "
            "Items neatly organized inside or arranged alongside the product. "
            "Clean, top-down or slight angle photography. "
            "Shot overhead at f/5.6 with a large diffusion panel for soft, even illumination. "
            "The image communicates order, efficiency, and good design. "
            "Satisfying organizational photography aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="home_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="home",
        description="展示品質生活的居家氛圍照",
        prompt=(
            "This home product in a beautifully styled interior vignette. "
            "Curated arrangement with complementary decor: plants, candles, "
            "books, ceramic pieces, creating a cohesive home aesthetic. "
            "Warm golden hour light streaming through a window. "
            "Shot at 40mm f/1.8 from a low angle to give the product a heroic, editorial presence. "
            "The composition tells a story of a refined, comfortable lifestyle. "
            "High-end home decor brand editorial photography."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== storage (收納) ====================
    SceneTemplate(
        id="home_stor_01_closet",
        name="衣櫥收納",
        name_en="Closet Organization",
        product_type="home",
        description="收納產品在衣櫥中整理衣物的場景",
        prompt=(
            "This storage product inside a well-organized walk-in closet or wardrobe, neatly holding folded clothes, accessories, or shoes. "
            "The closet features clean white shelving with the storage product prominently displayed at eye level, filled with color-coordinated garments. "
            "Bright, even overhead closet lighting combined with soft ambient fill to eliminate deep shadows inside the compartments. "
            "The surrounding closet is tidy and aspirational, showcasing a decluttered, organized lifestyle. "
            "Shot at 35mm f/4 from a straight-on angle to show the full depth and capacity of the storage product in its intended environment."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="storage",
        sub_category_name="收納",
    ),
    SceneTemplate(
        id="home_stor_02_desk",
        name="桌面整理",
        name_en="Desk Organization",
        product_type="home",
        description="桌面收納盒搭配文具用品展示",
        prompt=(
            "This desk organizer placed on a clean, modern workspace filled with neatly arranged stationery items including pens, scissors, sticky notes, and paper clips. "
            "The desk surface is light wood or white laminate with a laptop partially visible in the background for scale and context. "
            "A small potted succulent and a coffee cup add lifestyle warmth to the minimalist workspace scene. "
            "Natural window light from the left side creates soft directional shadows that add depth without harshness. "
            "Shot at 50mm f/3.5 from a 45-degree elevated angle to clearly show the organizer compartments and their contents."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="storage",
        sub_category_name="收納",
    ),
    SceneTemplate(
        id="home_stor_03_bathroom",
        name="浴室收納",
        name_en="Bathroom Storage",
        product_type="home",
        description="浴室場景中的收納產品展示",
        prompt=(
            "This storage product mounted on a bathroom wall or placed on a bathroom shelf, organizing toiletries such as shampoo bottles, cotton pads, and skincare items. "
            "The bathroom features clean white tiles, a modern faucet, and a small eucalyptus branch in a vase for a fresh, spa-like aesthetic. "
            "Bright, crisp lighting simulating daylight-balanced bathroom illumination with soft reflections on the tile surfaces. "
            "The organized arrangement contrasts with the clean, empty counter space around it to emphasize the product's tidying capability. "
            "Shot at 28mm f/5.6 to capture the bathroom context while keeping the storage product and its contents sharply in focus."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="storage",
        sub_category_name="收納",
    ),
    SceneTemplate(
        id="home_stor_04_stacked",
        name="堆疊展示",
        name_en="Stackable Display",
        product_type="home",
        description="可堆疊收納容器的堆疊展示",
        prompt=(
            "Multiple units of this stackable storage container stacked three to four levels high on a clean floor or shelf surface, demonstrating the modular stacking design. "
            "Each container is slightly offset or in different colors to show variety, with one unit open to reveal neatly folded items inside. "
            "Labels or tags are visible on the front of each container for organizational reference. "
            "Even studio lighting with dual softboxes ensures the stacking structure casts clean, defined shadows showing the dimensional stability. "
            "Shot at 50mm f/5.6 from a low three-quarter angle to emphasize the vertical stacking height and stability of the modular system."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="storage",
        sub_category_name="收納",
    ),
    SceneTemplate(
        id="home_stor_05_before_after",
        name="收納前後",
        name_en="Before & After Organization",
        product_type="home",
        description="使用收納產品前後的對比展示",
        prompt=(
            "A side-by-side comparison showing a cluttered, messy space on the left and the same space perfectly organized with this storage product on the right. "
            "The before side features scattered items, tangled accessories, and an overwhelmed drawer or shelf with chaotic piles. "
            "The after side shows the same items neatly contained, labeled, and accessible inside the storage product with satisfying visual order. "
            "Consistent overhead lighting across both halves ensures a fair comparison with identical color temperature and brightness. "
            "Shot at 35mm f/5.6 from directly above to provide a clear top-down view of both the messy and organized states."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="storage",
        sub_category_name="收納",
    ),
    # ==================== kitchen (廚具) ====================
    SceneTemplate(
        id="home_kit_01_cooking",
        name="烹飪場景",
        name_en="Active Cooking Scene",
        product_type="home",
        description="廚具在烹飪過程中的使用場景",
        prompt=(
            "This kitchenware product in active use during a cooking scene on a modern gas or induction stovetop with fresh ingredients being prepared. "
            "Vibrant vegetables, herbs, or proteins are visible in or near the cookware, with a wooden spoon or spatula resting alongside. "
            "Warm kitchen lighting with a combination of overhead range light and natural side window light creating an inviting, homey atmosphere. "
            "A slight wisp of steam or sizzle effect suggests the cooking action is happening in real time. "
            "Shot at 50mm f/2.8 from a slightly elevated angle to capture both the food inside the cookware and the kitchen counter context."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="kitchen",
        sub_category_name="廚具",
    ),
    SceneTemplate(
        id="home_kit_02_hanging",
        name="掛架展示",
        name_en="Hanging Rack Display",
        product_type="home",
        description="廚具掛在廚房掛架或掛鉤上展示",
        prompt=(
            "This kitchen utensil or cookware hanging from a stylish wall-mounted rack or hooks in a well-designed kitchen with white subway tile backsplash. "
            "Multiple utensils are arranged on the rack with the hero product in the center position, catching the most light. "
            "Copper, stainless steel, or matte black finishes gleam under warm pendant lighting from above. "
            "The composition shows the kitchen wall context with a marble countertop edge visible at the bottom of the frame. "
            "Shot at 40mm f/4 from a straight-on eye-level angle to present the hanging display as a buyer would see it in their own kitchen."
        ),
        aspect_ratio="3:4",
        injection_level="light",
        sub_category="kitchen",
        sub_category_name="廚具",
    ),
    SceneTemplate(
        id="home_kit_03_ingredients",
        name="食材搭配",
        name_en="Kitchenware with Ingredients",
        product_type="home",
        description="廚具搭配新鮮食材展示",
        prompt=(
            "This kitchenware product surrounded by fresh, colorful ingredients on a rustic wooden cutting board or clean marble countertop. "
            "Ripe tomatoes, fresh basil, olive oil in a small dish, garlic cloves, and artisan bread are scattered artfully around the product. "
            "The ingredients suggest a delicious meal about to be prepared, with the kitchenware as the essential tool in the process. "
            "Bright natural light from a nearby window with a subtle backlight glow on the translucent ingredients like herbs and oil. "
            "Shot overhead at f/4.5 to create a food magazine flat-lay composition with the kitchenware as the central hero element."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="kitchen",
        sub_category_name="廚具",
    ),
    SceneTemplate(
        id="home_kit_04_steam",
        name="蒸氣效果",
        name_en="Steam Ambiance Shot",
        product_type="home",
        description="鍋具搭配蒸氣的氛圍展示",
        prompt=(
            "This pot or pan on a stovetop with beautiful wisps of steam rising from the surface, creating an atmospheric and appetizing culinary scene. "
            "The steam is backlit by warm kitchen lighting, making it glow and swirl dramatically against the darker background. "
            "The cookware lid is slightly ajar or just lifted, releasing the aromatic steam in a visually compelling way. "
            "Dark, moody kitchen background with focused warm spotlight on the cookware to create a professional food photography ambiance. "
            "Shot at 85mm f/2.8 from a low side angle to capture the full height of the rising steam column with beautiful bokeh in the background."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="kitchen",
        sub_category_name="廚具",
    ),
    SceneTemplate(
        id="home_kit_05_set_display",
        name="整套展示",
        name_en="Complete Kitchen Set",
        product_type="home",
        description="整套廚具系列的完整展示",
        prompt=(
            "A complete kitchen product set laid out on a clean counter or table surface, showing every piece in the collection arranged from largest to smallest. "
            "Each item is slightly separated and angled to display its unique shape, with handles pointing in the same direction for visual consistency. "
            "The set includes pots, pans, lids, utensils, or accessories depending on the product line, all matching in finish and design. "
            "Even, bright studio lighting from a large overhead softbox ensures uniform illumination across every piece without hot spots. "
            "Shot at 35mm f/7.1 from a slightly elevated angle to capture the full breadth of the set while maintaining sharpness on every item."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="kitchen",
        sub_category_name="廚具",
    ),
    # ==================== bathroom (浴室用品) ====================
    SceneTemplate(
        id="home_bath_01_shower",
        name="淋浴場景",
        name_en="Shower Setting",
        product_type="home",
        description="浴室淋浴區域中的產品展示",
        prompt=(
            "This bathroom product placed in a modern walk-in shower setting with glass panels, rainfall showerhead, and clean stone or tile walls. "
            "Water droplets on the glass and subtle moisture in the air create an authentic, fresh shower atmosphere. "
            "The product sits on a built-in shower niche or teak bench, positioned as the hero element in the wet environment. "
            "Bright, diffused lighting simulating daylight through a frosted bathroom window for a clean, spa-like illumination. "
            "Shot at 28mm f/4 from a low angle inside the shower to capture the full setting context while the product remains the focal point."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="bathroom",
        sub_category_name="浴室用品",
    ),
    SceneTemplate(
        id="home_bath_02_towel_setup",
        name="毛巾擺設",
        name_en="Towel Arrangement",
        product_type="home",
        description="毛巾在浴室中的精美擺設展示",
        prompt=(
            "Luxurious towels neatly folded and arranged on a bathroom shelf, ladder rack, or rolled in a woven basket in an elegant bathroom setting. "
            "The towels showcase their plush texture, color, and thickness with one towel slightly unfolded to reveal the soft terry cloth interior. "
            "A sprig of dried lavender, a bar of artisan soap, and a small candle are styled alongside for a premium spa aesthetic. "
            "Warm, soft lighting from recessed bathroom fixtures creates a cozy, welcoming atmosphere with gentle shadows in the fabric folds. "
            "Shot at 50mm f/3.2 from a three-quarter angle to capture the towel stack depth and the plush texture with inviting detail."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="bathroom",
        sub_category_name="浴室用品",
    ),
    SceneTemplate(
        id="home_bath_03_soap_dispenser",
        name="洗手台",
        name_en="Bathroom Counter Display",
        product_type="home",
        description="洗手液或皂液器在洗手台上的展示",
        prompt=(
            "This soap dispenser or bathroom counter accessory placed beside a clean, modern vessel sink with a brushed nickel or matte black faucet. "
            "The counter is uncluttered with just the product, a small tray, and perhaps a ring dish or hand cream as complementary styling. "
            "A frameless mirror reflects soft, even lighting from above, adding depth and dimension to the simple composition. "
            "The overall aesthetic is minimalist luxury with clean lines and a neutral color palette of whites, grays, and natural stone. "
            "Shot at 40mm f/3.5 from a slight side angle to capture the sink faucet, mirror reflection, and product in a single cohesive frame."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="bathroom",
        sub_category_name="浴室用品",
    ),
    SceneTemplate(
        id="home_bath_04_spa",
        name="SPA 氛圍",
        name_en="Spa Atmosphere",
        product_type="home",
        description="SPA 般的浴室氛圍營造",
        prompt=(
            "This bathroom product in a luxurious spa-inspired setting with a freestanding bathtub partially filled with milky water and scattered flower petals. "
            "Flickering candles in glass holders line the tub edge, casting warm amber light and gentle reflections across the water surface. "
            "Eucalyptus branches hang from the shower fixture, and a bamboo bath tray holds the product alongside a book and a cup of herbal tea. "
            "The lighting is warm and low-key with a color temperature around 2800K, creating an intimate, deeply relaxing mood. "
            "Shot at 24mm f/2.8 from a wide elevated angle to capture the full bathtub scene with the product as the centerpiece of the self-care ritual."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="bathroom",
        sub_category_name="浴室用品",
    ),
    SceneTemplate(
        id="home_bath_05_accessories",
        name="配件組合",
        name_en="Bathroom Accessories Set",
        product_type="home",
        description="成套浴室配件的組合展示",
        prompt=(
            "A complete set of matching bathroom accessories including soap dispenser, toothbrush holder, soap dish, tumbler, and tray arranged on a clean marble counter. "
            "Each piece shares the same material finish and design language, displayed with even spacing to emphasize the cohesive collection. "
            "The background features a neutral bathroom wall with subtle texture, keeping the focus on the product set's design consistency. "
            "Bright, balanced studio lighting with a large overhead diffuser ensures each piece is evenly lit with no harsh shadows between items. "
            "Shot at 45mm f/5.6 from a slightly elevated three-quarter angle to show the shapes, heights, and design details of every piece in the set."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="bathroom",
        sub_category_name="浴室用品",
    ),
]

TemplateRegistry.register("home", HOME_TEMPLATES)
