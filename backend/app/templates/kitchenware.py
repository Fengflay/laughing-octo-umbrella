from app.templates.registry import SceneTemplate, TemplateRegistry

KITCHENWARE_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="kitchenware_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="kitchenware",
        description="純白背景，廚具餐飲產品居中展示",
        prompt=(
            "Place this kitchenware product on a pure white background (RGB 255,255,255). "
            "Professional e-commerce product photography with a large softbox overhead at 45 degrees "
            "and two side fill lights for clean, even illumination. "
            "The product should be centered, occupying about 80% of the frame. "
            "Slight natural shadow beneath the product for grounding. "
            "Front-facing angle tilted 15 degrees to show form and dimension. "
            "Shot with a 70mm lens at f/9 for maximum depth of field across the entire product. "
            "Ultra-high resolution, crisp details on handle texture, surface finish, and material quality. "
            "No other objects in frame. Color accuracy is critical."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="kitchenware",
        description="2x2 拼圖佈局，展示材質、容量、功能等賣點",
        prompt=(
            "Create a professional product photography collage for this kitchenware item. "
            "Show 4 different views arranged in a clean 2x2 grid layout on a white background: "
            "1) Front view showing the main design, shape, and branding. "
            "2) Close-up of the material quality: non-stick coating, stainless steel finish, or ceramic glaze. "
            "3) Handle or grip detail showing ergonomic design and heat resistance. "
            "4) Interior or functional detail: capacity markings, pour spout, or lid mechanism. "
            "Each view clearly separated with clean white space between them. "
            "Professional studio lighting, consistent color temperature (5500K) across all shots. "
            "Shot with a 60mm lens at f/8 for uniform sharpness in every panel. "
            "The layout looks like a premium kitchenware product specification page."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_03_detail_closeup",
        name="細節特寫",
        name_en="Detail Close-up",
        product_type="kitchenware",
        description="微距特寫，展示材質表面、塗層、接合處品質",
        prompt=(
            "Extreme macro close-up photography of this kitchenware product showing material quality and craftsmanship. "
            "Split into 2-3 detail zones: surface coating or finish quality (non-stick, enamel, brushed steel), "
            "handle attachment and riveting detail, and edge finishing or rim quality. "
            "Shot with a 100mm macro lens at f/4, shallow depth of field with ring light illumination. "
            "The surface texture should be so detailed you can see the grain of the material. "
            "Focus stacking for maximum sharpness across detail zones. "
            "Professional kitchenware detail photography conveying food-safe quality and durability."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="kitchenware",
        description="與常見食材、餐具對比，直觀展示大小與容量",
        prompt=(
            "This kitchenware product photographed next to common reference objects for size: "
            "a standard dinner plate, a hand holding the product, or common food items like an apple or egg. "
            "All items arranged on a clean white surface with a subtle grid pattern for measurement reference. "
            "The kitchenware product is the hero element in the center. "
            "Clean white background, even studio lighting from an overhead softbox. "
            "Shot with a 50mm lens at f/11 to keep all objects tack-sharp. "
            "The items are proportionally realistic to each other. "
            "The composition clearly communicates the product's practical size and capacity."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_05_kitchen_scene",
        name="廚房場景",
        name_en="Kitchen Scene",
        product_type="kitchenware",
        description="現代廚房中的使用場景",
        prompt=(
            "This kitchenware product placed naturally in a bright, modern kitchen setting. "
            "A clean countertop with the product as the hero item, surrounded by fresh ingredients "
            "like herbs, vegetables, or spices adding natural color. "
            "Warm natural window light streaming in from the left mixed with soft under-cabinet lighting. "
            "The kitchen has clean marble or butcher-block countertops and modern fixtures in the background. "
            "Shot with a 35mm lens at f/2.8, shallow depth of field keeping the product sharp "
            "while the kitchen environment provides soft, inviting context. "
            "Camera angle slightly above at 25 degrees. Warm color tones around 5400K. "
            "Inviting culinary lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_06_dining_scene",
        name="餐桌場景",
        name_en="Dining Table Scene",
        product_type="kitchenware",
        description="餐桌擺設中的產品展示",
        prompt=(
            "This kitchenware product styled on an elegant dining table setting. "
            "A beautifully set table with linen napkins, complementary dinnerware, fresh flowers in a vase, "
            "and the product placed as the centerpiece or in active serving position. "
            "Soft natural light from a nearby window creating warm, inviting atmosphere. "
            "The table setting conveys a curated, elevated dining experience. "
            "Shot with a 50mm lens at f/2.4 for beautiful bokeh separating the product "
            "from the soft background of the dining room. "
            "Camera at eye level from a seated dining perspective. "
            "Warm, welcoming dining lifestyle photography with a 5500K color temperature."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_07_cooking_demo",
        name="烹飪展示",
        name_en="Cooking Demo",
        product_type="kitchenware",
        description="手持使用場景，展示烹飪中的產品",
        prompt=(
            "Hands actively using this kitchenware product during cooking in a well-lit kitchen. "
            "The product is in use: stirring in a pan, pouring from a vessel, cutting on a board, "
            "or serving from a bowl. Steam, fresh ingredients, or plated food visible in context. "
            "Dynamic action shot capturing the moment of use. "
            "Shot with a 45mm lens at f/3.2, fast shutter speed to freeze motion, "
            "with overhead pendant lighting and natural side light for depth. "
            "The product is the clear hero element, hands provide human scale and context. "
            "Warm cooking atmosphere, editorial food photography style. "
            "Camera angle slightly above at 35 degrees looking down at the cooking action."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_08_kitchen_set",
        name="廚具組合",
        name_en="Kitchen Set",
        product_type="kitchenware",
        description="廚具組合平拍，展示成套搭配",
        prompt=(
            "This kitchenware product arranged in an organized flat lay with complementary kitchen items: "
            "matching utensils, cutting board, measuring cups, spice jars, and a kitchen towel. "
            "Top-down perspective on a clean wooden or marble surface. "
            "Each item neatly spaced with intentional symmetrical arrangement. "
            "The hero product is centrally placed and visually prominent. "
            "Shot overhead with a 35mm lens at f/7.1, even diffused softbox lighting "
            "eliminating harsh shadows while preserving material textures on wood, steel, and ceramic. "
            "Professional kitchenware flat lay photography showing a complete culinary toolkit."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="kitchenware_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="kitchenware",
        description="展示品牌調性的精緻廚房生活美學",
        prompt=(
            "This kitchenware product styled in a warm, aspirational kitchen lifestyle scene. "
            "A rustic-modern kitchen vignette: the product on a beautiful countertop alongside "
            "artisan bread, a bottle of olive oil, fresh herbs in a ceramic pot, and a linen cloth. "
            "Warm morning light pouring through a window, creating soft highlights and gentle shadows. "
            "Shot with a 40mm lens at f/4.0 from a slightly low angle to give the scene grandeur. "
            "Rich, warm color palette with earthy tones and natural materials. "
            "The composition conveys artisan quality, home warmth, and culinary passion. "
            "Premium kitchenware brand campaign aesthetic with a cozy, editorial feel."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== cookware (鍋具) ====================
    SceneTemplate(
        id="kw_cook_01_cooking",
        name="烹飪中",
        name_en="Cooking in Progress",
        product_type="kitchenware",
        description="鍋具中正在烹飪食物的動態展示",
        prompt=(
            "This pot or pan in active use on a stove with food being cooked inside, steam rising gently from the surface. "
            "Fresh vegetables, seared protein, or a simmering sauce visible inside the cookware, showing its cooking performance. "
            "Shot from a 30-degree overhead angle with a 50mm lens at f/3.5, the cookware interior in sharp focus "
            "while the kitchen background falls into warm bokeh. "
            "Natural side light from a window mixed with the warm glow of the stovetop creates appetizing highlights "
            "on the food and cookware surface. "
            "The image conveys real culinary action, heat, aroma, and the cookware's functional excellence."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="cookware",
        sub_category_name="鍋具",
    ),
    SceneTemplate(
        id="kw_cook_02_stovetop",
        name="爐台展示",
        name_en="Stovetop Display",
        product_type="kitchenware",
        description="鍋具放在爐台上的廚房環境展示",
        prompt=(
            "This cookware piece placed prominently on a modern gas or induction stovetop in a clean, well-designed kitchen. "
            "The lid is slightly ajar or placed beside the pot, revealing the polished interior surface. "
            "Fresh ingredients like herbs, garlic, and olive oil are arranged nearby on the countertop. "
            "Shot with a 35mm lens at f/4.0 from a three-quarter front angle at stovetop height. "
            "Bright overhead kitchen lighting combined with natural window light from the side "
            "creates even illumination on the cookware's exterior finish and hardware. "
            "The scene feels like a premium kitchen ready for cooking, conveying quality and culinary aspiration."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="cookware",
        sub_category_name="鍋具",
    ),
    SceneTemplate(
        id="kw_cook_03_interior",
        name="內部塗層",
        name_en="Interior Coating Close-up",
        product_type="kitchenware",
        description="鍋具內部不沾或陶瓷塗層的特寫",
        prompt=(
            "Close-up shot looking directly into the interior of this cookware, showcasing the non-stick, ceramic, "
            "or stainless steel cooking surface in immaculate detail. "
            "The camera angle is from directly above at a slight tilt, revealing the full interior surface, "
            "coating texture, and any reinforcement layers visible along the sides. "
            "Shot with a 60mm macro lens at f/5.6, ring light illumination providing even, shadow-free coverage "
            "that highlights the smoothness and quality of the interior coating. "
            "A single drop of water or oil beading on the surface demonstrates the non-stick property. "
            "Professional product photography emphasizing food-safe coating quality and durability."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="cookware",
        sub_category_name="鍋具",
    ),
    SceneTemplate(
        id="kw_cook_04_set",
        name="整套展示",
        name_en="Cookware Set Display",
        product_type="kitchenware",
        description="整套鍋具堆疊或排列的展示",
        prompt=(
            "A complete cookware set professionally arranged: pots and pans neatly stacked by size "
            "with lids placed alongside, showing the full range of pieces in the collection. "
            "Set on a clean white or light marble surface with consistent studio lighting from above. "
            "The largest piece is at the back, graduating down to the smallest at front for a pyramid-like arrangement. "
            "Shot with a 50mm lens at f/8 from a slightly elevated front angle, ensuring all pieces are visible and sharp. "
            "Even diffused softbox lighting at 5500K highlights the uniform finish and matching design across the entire set. "
            "The image communicates completeness, value, and cohesive kitchen design."
        ),
        aspect_ratio="4:3",
        injection_level="none",
        sub_category="cookware",
        sub_category_name="鍋具",
    ),
    SceneTemplate(
        id="kw_cook_05_serving",
        name="上菜效果",
        name_en="Serving from Cookware",
        product_type="kitchenware",
        description="直接從鍋具上菜的場景展示",
        prompt=(
            "This cookware piece placed on a dining table trivet with a beautifully prepared dish inside, "
            "ready to be served directly to diners. A hand holding a serving spoon ladles food from the pot. "
            "The dining table setting includes linen placemats, wine glasses, and warm candlelight in the background. "
            "Shot with a 50mm lens at f/2.8 from a seated diner's perspective at a slight angle. "
            "Warm, golden ambient lighting from candles mixed with soft overhead light creates an intimate dining atmosphere. "
            "The cookware transitions seamlessly from stove to table, demonstrating its dual-purpose elegance "
            "and the beauty of farm-to-table style serving."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="cookware",
        sub_category_name="鍋具",
    ),
    # ==================== tableware (餐具) ====================
    SceneTemplate(
        id="kw_tab_01_table_set",
        name="餐桌擺設",
        name_en="Table Setting Display",
        product_type="kitchenware",
        description="餐具在完整餐桌擺設中的展示",
        prompt=(
            "This tableware arranged in a complete, elegant table setting for a formal dinner. "
            "Plates stacked with a charger at the base, flanked by polished silverware, "
            "crystal water glasses, linen napkins folded artfully, and a small floral centerpiece. "
            "Shot from a 25-degree overhead angle with a 35mm lens at f/3.5, the hero tableware in crisp focus "
            "while the extended table setting provides soft, luxurious depth. "
            "Soft natural window light from the left creates gentle highlights on the ceramic glaze and glass surfaces. "
            "The scene communicates refined taste and elevated everyday dining, "
            "showcasing the tableware as the foundation of a beautiful table."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="tableware",
        sub_category_name="餐具",
    ),
    SceneTemplate(
        id="kw_tab_02_close_up",
        name="花紋特寫",
        name_en="Pattern Detail Close-up",
        product_type="kitchenware",
        description="餐具花紋和設計細節的特寫",
        prompt=(
            "Macro close-up of this tableware piece focusing on the decorative pattern, glaze texture, "
            "and edge detailing such as gold rim, embossed design, or hand-painted motif. "
            "Shot with a 100mm macro lens at f/3.5, very shallow depth of field "
            "with the primary pattern area in razor-sharp focus and the rest of the plate curving into soft bokeh. "
            "Ring light illumination reveals the subtle texture of the ceramic glaze and any metallic accents. "
            "The color reproduction is accurate, capturing the true depth of the glaze color. "
            "Professional ceramic art photography conveying artisan craftsmanship and luxury dining aesthetics."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="tableware",
        sub_category_name="餐具",
    ),
    SceneTemplate(
        id="kw_tab_03_stacked",
        name="堆疊展示",
        name_en="Stacked Tableware Display",
        product_type="kitchenware",
        description="餐盤碗碟整齊堆疊的展示",
        prompt=(
            "This tableware collection neatly stacked in an attractive vertical arrangement: "
            "dinner plates at the base, salad plates, then bowls on top, slightly offset to show each piece's rim design. "
            "Set on a clean white or natural linen surface with soft, even studio lighting. "
            "Shot from a three-quarter front angle with a 70mm lens at f/5.6, "
            "the entire stack in sharp focus from bottom to top. "
            "Diffused overhead softbox at 5500K provides clean, shadow-free illumination "
            "that reveals the uniform glaze quality and consistent color across all pieces. "
            "The composition conveys quality, consistency, and the satisfying completeness of a matching tableware set."
        ),
        aspect_ratio="3:4",
        injection_level="none",
        sub_category="tableware",
        sub_category_name="餐具",
    ),
    SceneTemplate(
        id="kw_tab_04_food_served",
        name="盛菜效果",
        name_en="Food Served on Tableware",
        product_type="kitchenware",
        description="餐具上盛放精美料理的展示",
        prompt=(
            "A beautifully plated gourmet dish served on this tableware piece, showing how the plate's design "
            "complements and elevates the food presentation. "
            "The food is artfully arranged with colorful garnishes, sauces, and micro-herbs. "
            "Shot from a 35-degree overhead angle with a 50mm lens at f/2.8, "
            "the food and plate rim in sharp focus against a softly blurred dining table background. "
            "Warm, directional side light creates appetizing highlights on the food and subtle shadows "
            "that reveal the depth of the plate's form. "
            "Editorial food photography that showcases the tableware as the perfect canvas for culinary art."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="tableware",
        sub_category_name="餐具",
    ),
    SceneTemplate(
        id="kw_tab_05_collection",
        name="系列搭配",
        name_en="Tableware Collection",
        product_type="kitchenware",
        description="同系列餐具搭配展示",
        prompt=(
            "The complete matching tableware collection displayed together: dinner plates, side plates, bowls, "
            "cups and saucers, and a serving platter, all from the same design series. "
            "Arranged in a carefully composed flat lay on a natural linen tablecloth or light wooden surface. "
            "Shot from directly overhead with a 35mm lens at f/7.1, "
            "even diffused softbox lighting ensuring consistent color and glaze appearance across all pieces. "
            "Each piece is spaced with geometric precision, creating a visually satisfying pattern. "
            "The arrangement communicates the breadth of the collection and the design harmony "
            "that makes mixing and matching within the series effortless."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="tableware",
        sub_category_name="餐具",
    ),
    # ==================== baking (烘焙) ====================
    SceneTemplate(
        id="kw_bake_01_process",
        name="烘焙過程",
        name_en="Baking Process",
        product_type="kitchenware",
        description="烘焙工具在製作過程中的使用展示",
        prompt=(
            "This baking tool actively in use during the baking process: a whisk beating egg whites into stiff peaks, "
            "a rolling pin stretching dough on a floured marble surface, or a silicone spatula folding batter in a bowl. "
            "Flour dust and raw ingredients visible around the action area, conveying authentic baking energy. "
            "Shot with a 45mm lens at f/3.2 from a 30-degree overhead angle, hands and tool in sharp focus "
            "with the messy, flour-dusted kitchen counter providing warm context. "
            "Bright natural light from a side window creates a warm, inviting baking atmosphere. "
            "The image captures the joy and tactile satisfaction of hands-on baking with quality tools."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="baking",
        sub_category_name="烘焙",
    ),
    SceneTemplate(
        id="kw_bake_02_result",
        name="成品展示",
        name_en="Baked Result Display",
        product_type="kitchenware",
        description="烘焙成品與工具並排的展示",
        prompt=(
            "Freshly baked goods displayed beautifully with this baking tool placed nearby: "
            "golden croissants on a cooling rack, a decorated cake on a turntable, "
            "or muffins in a baking tin, still warm from the oven. "
            "The baking tool is positioned next to the finished product, showing the direct connection between tool and result. "
            "Shot with a 50mm lens at f/3.5 from a slight overhead angle, warm natural morning light "
            "creating golden highlights on the baked surfaces and casting soft shadows. "
            "The scene conveys the rewarding result of baking with the right equipment, "
            "evoking the warmth, aroma, and satisfaction of homemade baking."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="baking",
        sub_category_name="烘焙",
    ),
    SceneTemplate(
        id="kw_bake_03_ingredients",
        name="材料準備",
        name_en="Ingredients Preparation",
        product_type="kitchenware",
        description="烘焙工具與原料一起的準備場景",
        prompt=(
            "This baking tool arranged in a mise-en-place style with baking ingredients laid out neatly: "
            "measured flour in a bowl, eggs, butter, sugar, vanilla extract, and chocolate chips "
            "each in their own small container surrounding the hero tool. "
            "Shot from directly above with a 35mm lens at f/6.3, flat lay perspective on a clean marble countertop. "
            "Even, bright studio lighting at 5500K ensures all ingredients are clearly visible and colors are accurate. "
            "The tool is centrally placed as the key instrument that will bring all ingredients together. "
            "The composition conveys organized preparation, recipe-ready readiness, and baking anticipation."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="baking",
        sub_category_name="烘焙",
    ),
    SceneTemplate(
        id="kw_bake_04_display",
        name="工具排列",
        name_en="Baking Tools Arranged",
        product_type="kitchenware",
        description="烘焙工具整齊排列的展示",
        prompt=(
            "A collection of baking tools including this product neatly arranged in rows or a radial pattern "
            "on a clean white or light marble surface: spatulas, whisks, measuring spoons, cookie cutters, "
            "piping tips, and pastry brushes, all laid out with geometric precision. "
            "The hero tool is positioned centrally and is slightly larger in the composition. "
            "Shot from directly overhead with a 50mm lens at f/7.1, even diffused softbox lighting "
            "providing uniform illumination with no harsh shadows across all the metal, silicone, and wood textures. "
            "The arrangement resembles a professional baker's toolkit, conveying completeness and quality craftsmanship."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="baking",
        sub_category_name="烘焙",
    ),
    SceneTemplate(
        id="kw_bake_05_kids",
        name="親子烘焙",
        name_en="Family Baking Together",
        product_type="kitchenware",
        description="家長帶孩子一起使用烘焙工具的溫馨場景",
        prompt=(
            "A heartwarming scene of a parent and child baking together in a bright, cheerful kitchen, "
            "both using this baking tool collaboratively. The child watches with delight as the parent demonstrates, "
            "or the child's small hands are guided by the adult's to use the tool. "
            "Flour-dusted aprons, cookie dough, and colorful sprinkles add playful charm to the scene. "
            "Shot with a 35mm lens at f/2.4 from a slightly above eye level, warm natural kitchen light "
            "mixed with soft overhead lighting. Genuine smiles and engagement visible on both faces. "
            "The image conveys family bonding, joy, and creating memories through baking together."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="baking",
        sub_category_name="烘焙",
    ),
]

TemplateRegistry.register("kitchenware", KITCHENWARE_TEMPLATES)
