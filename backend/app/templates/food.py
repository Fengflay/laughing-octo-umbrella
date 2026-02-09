from app.templates.registry import SceneTemplate, TemplateRegistry

FOOD_TEMPLATES = [
    # ==================== common (通用場景) ====================
    SceneTemplate(
        id="food_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="food",
        description="純白背景，食品包裝正面展示",
        prompt=(
            "This food/beverage product on a pure white background. "
            "Professional food packaging photography with clean, bright lighting. "
            "The product is centered, showing the label and packaging clearly. "
            "Colors appear appetizing and accurate. "
            "Occupies about 80% of the frame. "
            "Shot at f/8 with a beauty dish for crisp label detail and soft shadow. "
            "Commercial food product photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="food",
        description="多角度展示食品包裝與內容物的拼圖佈局",
        prompt=(
            "Create a professional food product photography collage. "
            "Show 4 different views of this food product in a clean 2x2 grid layout on a white background: "
            "1) Front packaging view showing the label clearly. "
            "2) Side or back view showing nutritional information area. "
            "3) The product poured out or opened, showing the actual food contents. "
            "4) Close-up of the food texture, showing quality and freshness. "
            "Each view is clearly separated with clean white space between them. "
            "Bright, appetizing lighting with warm tones. "
            "Consistent even illumination across all four panels for a cohesive look. "
            "The overall layout looks like a premium product specification page."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_03_contents_display",
        name="內容物展示",
        name_en="Contents Display",
        product_type="food",
        description="打開包裝展示食品的真實樣貌",
        prompt=(
            "This food product shown with its packaging opened, revealing the actual contents. "
            "The food is displayed in an appetizing way: poured into a bowl, "
            "arranged on a plate, or shown fresh out of the package. "
            "Clean surface, bright natural lighting that makes the food look delicious. "
            "Shot at a 45-degree overhead angle at f/4 to keep the food sharp with a creamy background. "
            "The image shows buyers exactly what they'll receive. "
            "Professional food photography with appealing presentation."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_04_ingredients",
        name="原料展示圖",
        name_en="Ingredients Showcase",
        product_type="food",
        description="與原料食材一起展示，強調天然新鮮",
        prompt=(
            "This food product surrounded by its raw natural ingredients: "
            "fresh fruits, nuts, herbs, grains, or spices depending on the product. "
            "Arranged on a rustic wood board or clean marble surface. "
            "Bright, natural lighting emphasizing freshness and quality. "
            "Shot from slightly above at f/5.6 with a reflector fill to bring out ingredient colors. "
            "The composition tells the story of natural, quality ingredients. "
            "Premium food ingredient storytelling photography."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_05_table_scene",
        name="餐桌場景",
        name_en="Table Setting Scene",
        product_type="food",
        description="餐桌上的搭配場景，展示食用情境",
        prompt=(
            "This food product in an inviting table setting scene. "
            "A beautifully set table with plates, utensils, and the product served attractively. "
            "Warm, natural lighting creating a cozy dining atmosphere. "
            "Fresh garnishes, complementary foods, and beverages nearby. "
            "Shot at a 30-degree angle with a 35mm lens at f/3.5 for an immersive perspective. "
            "The scene makes viewers want to taste the product immediately. "
            "Appetizing food lifestyle photography."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_06_serving_suggestion",
        name="食用建議圖",
        name_en="Serving Suggestion",
        product_type="food",
        description="展示推薦的食用/飲用方式",
        prompt=(
            "This food product shown in its ideal serving presentation. "
            "Beautifully plated or poured into an attractive glass/cup/bowl. "
            "Garnished with fresh ingredients for visual appeal. "
            "The preparation looks easy yet gourmet. "
            "Bright, clean food photography with shallow depth of field at f/2.8. "
            "Use a side key light with a bounce card to create appetizing highlights and texture. "
            "The image inspires buyers to try the product themselves."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_07_lifestyle_eating",
        name="享用場景",
        name_en="Enjoying Scene",
        product_type="food",
        description="手部特寫享用食品的溫馨場景",
        prompt=(
            "A close-up of hands reaching for or holding this food/beverage product. "
            "Only hands and forearms visible, no face shown. "
            "One hand is picking up or pouring the product, the other steadies the package. "
            "Warm, cozy setting: a wooden breakfast table with soft morning light. "
            "A cup of coffee or tea and a linen napkin visible in the soft background. "
            "The hands look natural and inviting, with warm skin tones. "
            "Shallow depth of field at f/2.4 focusing on the product and hands. "
            "Lit by diffused window light with a warm color temperature around 3500K. "
            "The image conveys a moment of simple everyday enjoyment and comfort. "
            "Professional food lifestyle photography with warm, golden tones."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_08_variety_display",
        name="多口味展示",
        name_en="Variety Display",
        product_type="food",
        description="展示多種口味/規格選擇",
        prompt=(
            "This food product shown as part of a product line with multiple varieties "
            "or flavors arranged in an attractive display. "
            "Different flavors or variants side by side or in a fan arrangement. "
            "Clean background, each variant clearly distinguishable. "
            "Shot at f/7.1 from a slightly elevated angle with balanced fill lighting on each item. "
            "The layout shows the breadth of choice available. "
            "Professional product line-up photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="food_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="food",
        description="展示品牌調性的質感美食照",
        prompt=(
            "This food product in a warm, atmospheric kitchen or cafe setting. "
            "Styled with rustic elements: wooden cutting board, linen napkin, "
            "fresh herbs, vintage utensils, and warm ambient lighting. "
            "Steam or condensation visible for freshness cues. "
            "The composition tells a story of artisan quality and tradition. "
            "Shot with a 50mm prime at f/2.8, backlit by warm window light to catch steam and texture. "
            "High-end food brand editorial photography with rich, warm tones."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ==================== tea (茶飲) ====================
    SceneTemplate(
        id="food_tea_01_brewing",
        name="沖泡過程",
        name_en="Tea Brewing Process",
        product_type="food",
        description="茶葉在茶壺中沖泡的過程",
        prompt=(
            "This tea product being brewed in a clear glass teapot, with hot water being poured over the tea leaves showing the beautiful unfurling and color diffusion process. "
            "The amber or green tea liquor is visible through the glass as the leaves steep, creating a mesmerizing gradient of color in the water. "
            "Wisps of steam rise elegantly from the teapot spout, backlit by warm side lighting to create a dreamy, aromatic atmosphere. "
            "A clean bamboo or dark slate surface grounds the scene with a small tea cup waiting beside the pot. "
            "Shot at 60mm f/2.8 from a low side angle to capture the water pour, steam wisps, and the tea color developing through the transparent pot."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="tea",
        sub_category_name="茶飲",
    ),
    SceneTemplate(
        id="food_tea_02_set",
        name="茶具搭配",
        name_en="Tea Set Pairing",
        product_type="food",
        description="茶產品搭配成套茶具展示",
        prompt=(
            "This tea product displayed alongside a matching traditional or modern teaware set including a teapot, sharing pitcher, and small tasting cups on a tea tray. "
            "The tea packaging is positioned as the central element with the teaware arranged artfully around it in a balanced, harmonious composition. "
            "Warm, directional lighting from the left casts elegant shadows across the tea tray surface and creates subtle highlights on the ceramic glaze. "
            "The overall aesthetic suggests the ritualistic nature of tea preparation with cultural refinement and attention to craft. "
            "Shot at 50mm f/4 from a 45-degree angle to capture the depth of the tea set arrangement and the relationship between the product and its serving accessories."
        ),
        aspect_ratio="4:3",
        injection_level="light",
        sub_category="tea",
        sub_category_name="茶飲",
    ),
    SceneTemplate(
        id="food_tea_03_afternoon",
        name="下午茶",
        name_en="Afternoon Tea Setting",
        product_type="food",
        description="優雅的下午茶搭配點心的場景",
        prompt=(
            "This tea product served in an elegant afternoon tea setting with fine china, a tiered dessert stand holding petit fours and scones, and fresh flowers on a linen tablecloth. "
            "A cup of freshly brewed tea with the product's distinctive color is prominently placed in the foreground with steam gently rising. "
            "Soft, diffused natural light streams through sheer curtains, creating a bright and airy European cafe or garden party atmosphere. "
            "Delicate lace, silver spoons, and a small jar of honey or clotted cream complete the refined afternoon tea experience. "
            "Shot at 35mm f/3.2 from a slightly elevated dining perspective to capture the full spread with the tea cup and product as the focal centerpiece."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="tea",
        sub_category_name="茶飲",
    ),
    SceneTemplate(
        id="food_tea_04_leaves",
        name="茶葉特寫",
        name_en="Dried Tea Leaves Close-up",
        product_type="food",
        description="乾燥茶葉的微距特寫展示",
        prompt=(
            "An extreme close-up macro shot of dried tea leaves from this product scattered on a clean dark slate or bamboo surface, revealing their twist, curl, and color variations. "
            "The individual leaves show detailed texture including dried veins, silvery tips, or rolled shapes characteristic of the tea variety. "
            "A small pile of leaves is artfully arranged with a few individual leaves separated to show size and quality up close. "
            "Controlled side lighting rakes across the leaf surfaces to accentuate their three-dimensional texture, glossy or matte finish, and natural color depth. "
            "Shot at 100mm macro f/4 from directly above to capture the intricate leaf details that communicate premium quality and careful processing."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="tea",
        sub_category_name="茶飲",
    ),
    SceneTemplate(
        id="food_tea_05_zen",
        name="禪意氛圍",
        name_en="Zen Tea Ceremony",
        product_type="food",
        description="禪意冥想風格的茶道場景",
        prompt=(
            "This tea product in a serene, minimalist zen tea ceremony setting with a handcrafted ceramic tea bowl on a low wooden table in a tatami or meditation room. "
            "The space is sparse and intentional with a single ikebana flower arrangement, a burning incense stick with a thin smoke trail, and soft natural light. "
            "The tea is prepared in a traditional manner, with matcha powder, chasen whisk, or gaiwan visible depending on the tea type. "
            "Warm, muted earth tones dominate the palette with the green of the tea providing the only vivid color accent in the contemplative scene. "
            "Shot at 40mm f/2.4 from a low, seated perspective to immerse the viewer in the meditative tea ceremony experience with the product at its spiritual center."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="tea",
        sub_category_name="茶飲",
    ),
    # ==================== snacks (零食) ====================
    SceneTemplate(
        id="food_snk_01_open",
        name="開袋展示",
        name_en="Opened Package Display",
        product_type="food",
        description="打開包裝展示零食內容物",
        prompt=(
            "This snack product with its packaging torn open at the top, revealing the contents spilling out onto a clean surface in an appetizing cascade. "
            "A few pieces of the snack are artfully scattered in front of the bag, showing their shape, color, coating, and texture in mouthwatering detail. "
            "The packaging label and branding are still clearly visible on the bag while the opened top creates a casual, inviting feel. "
            "Bright, warm overhead lighting creates appetizing golden tones on the snack surfaces with slight specular highlights on any glazed or seasoned textures. "
            "Shot at 50mm f/3.5 from a 45-degree angle to show both the package design and the spilled-out contents in a single appetizing composition."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="snacks",
        sub_category_name="零食",
    ),
    SceneTemplate(
        id="food_snk_02_serving",
        name="擺盤呈現",
        name_en="Serving Plate Arrangement",
        product_type="food",
        description="零食擺盤在精美餐盤上的展示",
        prompt=(
            "This snack product beautifully arranged on an artisan ceramic plate or wooden serving board, styled as an appetizing appetizer or party platter presentation. "
            "The snacks are neatly arranged in concentric circles or artistic patterns that highlight their uniform shape, vibrant color, and premium quality. "
            "Small dipping sauces, fresh herbs, or fruit garnishes are placed alongside to suggest serving ideas and flavor pairings. "
            "Soft, warm side lighting from the left creates gentle shadows beneath each piece and highlights the surface texture of every snack. "
            "Shot at 50mm f/4 from a top-down overhead angle to present the platter arrangement as a satisfying visual feast with the product packaging visible at the edge."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="snacks",
        sub_category_name="零食",
    ),
    SceneTemplate(
        id="food_snk_03_movie",
        name="追劇場景",
        name_en="Movie Night Snacking",
        product_type="food",
        description="看電影或追劇時享用零食的場景",
        prompt=(
            "This snack product placed on a cozy living room coffee table in front of a TV or laptop screen showing a blurred movie scene, creating a perfect movie night atmosphere. "
            "A soft throw blanket drapes over the couch armrest, and a bowl filled with the snack sits next to the open package with a hand reaching in to grab a piece. "
            "Warm, low ambient living room lighting with the cool glow of the screen providing subtle fill, creating an intimate and relaxing evening-at-home mood. "
            "A drink glass or can is visible nearby, completing the snacking-while-streaming lifestyle scene. "
            "Shot at 35mm f/2.4 from a low sofa-level angle to immerse the viewer in the cozy movie night experience with the snack as the essential companion."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="snacks",
        sub_category_name="零食",
    ),
    SceneTemplate(
        id="food_snk_04_sharing",
        name="分享場景",
        name_en="Sharing Scene",
        product_type="food",
        description="多人分享零食的社交場景",
        prompt=(
            "Multiple hands reaching into a central bowl or package of this snack product during a casual social gathering around a table. "
            "The scene captures a moment of shared enjoyment with three to four different hands visible, each grabbing a piece of the snack simultaneously. "
            "The table setting includes drinks, napkins, and other party elements visible in the soft background, establishing a fun social occasion. "
            "Warm, festive lighting creates a convivial atmosphere with the snack bowl as the bright focal point drawing everyone together. "
            "Shot at 35mm f/2.8 from directly above the table to capture all the reaching hands, the full snack bowl, and the social dining context."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="snacks",
        sub_category_name="零食",
    ),
    SceneTemplate(
        id="food_snk_05_ingredients",
        name="原料展示",
        name_en="Raw Ingredients Display",
        product_type="food",
        description="零食搭配原料食材一起展示",
        prompt=(
            "This snack product placed at the center surrounded by its key raw ingredients such as whole nuts, cocoa beans, dried fruits, sea salt crystals, or fresh grains spread on a rustic surface. "
            "Each ingredient is arranged in small clusters radiating outward from the product, visually connecting the finished snack to its natural source materials. "
            "Bright, clean overhead lighting with a subtle warm tone brings out the natural colors and textures of both the raw ingredients and the finished snack product. "
            "The composition emphasizes quality sourcing, natural processing, and premium ingredient selection for health-conscious buyers. "
            "Shot directly overhead at f/5.6 to create a magazine-style flat lay that keeps every ingredient and the central product uniformly sharp and detailed."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="snacks",
        sub_category_name="零食",
    ),
    # ==================== supplements (保健食品) ====================
    SceneTemplate(
        id="food_sup_01_daily",
        name="每日服用",
        name_en="Daily Routine Setting",
        product_type="food",
        description="搭配水杯的每日服用場景",
        prompt=(
            "This supplement product placed on a clean white kitchen counter beside a tall glass of water and a small breakfast setting suggesting a healthy morning routine. "
            "The supplement bottle or package is open with the daily dose of capsules or tablets placed neatly on a small ceramic dish ready for consumption. "
            "Bright, fresh morning sunlight streams through a kitchen window, casting clean shadows and creating an energizing start-of-day atmosphere. "
            "A fresh fruit, a small plant, or a daily planner in the background reinforces the disciplined, health-conscious daily wellness routine. "
            "Shot at 50mm f/3.5 from a countertop-level angle to present the supplement as a natural, integrated part of the viewer's morning health ritual."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="supplements",
        sub_category_name="保健食品",
    ),
    SceneTemplate(
        id="food_sup_02_capsule",
        name="膠囊特寫",
        name_en="Capsule Close-up",
        product_type="food",
        description="膠囊或錠劑在白色背景上的特寫",
        prompt=(
            "A close-up of individual capsules or tablets from this supplement product arranged in a clean geometric pattern on a pristine white surface. "
            "The capsules show their translucent gel shell with visible powder or liquid fill inside, or the tablets display their smooth compressed surface and color. "
            "Clinical, bright, even lighting from a ring light overhead eliminates all shadows and provides medical-grade clarity for the product close-up. "
            "The product bottle is partially visible at the edge of the frame for brand reference while the capsule detail dominates the composition. "
            "Shot at 90mm macro f/4 from directly above to capture the precise shape, color, size, and surface quality of each individual dose unit."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="supplements",
        sub_category_name="保健食品",
    ),
    SceneTemplate(
        id="food_sup_03_natural",
        name="天然成分",
        name_en="Natural Ingredients Scene",
        product_type="food",
        description="產品搭配天然草本或原料展示",
        prompt=(
            "This supplement product surrounded by its natural source ingredients such as fresh turmeric roots, spirulina powder, ginseng, berries, or fish oil capsules with omega-rich salmon. "
            "The natural ingredients are arranged on a clean wooden surface or marble slab, creating a visual connection between the supplement and its botanical or nutritional origins. "
            "Soft, warm natural lighting highlights the vivid colors of the fresh ingredients and the premium packaging design of the supplement product. "
            "Small green leaves, a mortar and pestle, or a glass dropper add apothecary-style authenticity to the natural wellness composition. "
            "Shot at 45mm f/4.5 from a 45-degree angle to show both the three-dimensional supplement packaging and the spread of natural ingredients in a single cohesive frame."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="supplements",
        sub_category_name="保健食品",
    ),
    SceneTemplate(
        id="food_sup_04_gym",
        name="運動搭配",
        name_en="Fitness Context",
        product_type="food",
        description="保健食品在健身運動環境中的展示",
        prompt=(
            "This supplement product placed on a gym bench or locker room shelf next to a shaker bottle, resistance bands, and a clean towel in an active fitness environment. "
            "The supplement packaging is clearly visible with the cap open, suggesting it was just used as part of a pre-workout or post-workout nutrition routine. "
            "Cool, energetic gym lighting with overhead fluorescents and warm accent lighting creates a motivating athletic wellness atmosphere. "
            "A filled shaker bottle or protein shake glass beside the product shows the supplement mixed and ready to drink for immediate use context. "
            "Shot at 35mm f/3.5 from a low three-quarter angle to position the supplement as an essential tool in the fitness lifestyle toolkit."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="supplements",
        sub_category_name="保健食品",
    ),
    SceneTemplate(
        id="food_sup_05_comparison",
        name="成分圖表",
        name_en="Ingredient Info Visual",
        product_type="food",
        description="產品搭配成分資訊的視覺展示",
        prompt=(
            "This supplement product displayed on a clean white surface alongside a visually clear infographic-style layout showing key nutritional facts and active ingredient percentages. "
            "The product bottle stands upright with its nutrition facts label facing the camera, while illustrated icons represent vitamins, minerals, or herbal extracts around it. "
            "Clean, bright clinical lighting ensures the product label text and surrounding informational graphics are perfectly legible and professional. "
            "The overall composition resembles a premium health product specification page with scientific credibility and transparent ingredient communication. "
            "Shot at 50mm f/5.6 from a straight-on eye-level angle to keep the product label and surrounding informational elements uniformly sharp and readable."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="supplements",
        sub_category_name="保健食品",
    ),
]

TemplateRegistry.register("food", FOOD_TEMPLATES)
