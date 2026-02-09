from app.templates.registry import SceneTemplate, TemplateRegistry

JEWELRY_TEMPLATES = [
    # ===== Common (通用場景) =====
    SceneTemplate(
        id="jewelry_01_white_bg",
        name="白底主圖",
        name_en="White Background",
        product_type="jewelry",
        description="純白背景，首飾居中，展現光澤與反射",
        prompt=(
            "Place this jewelry on a pure white background (RGB 255,255,255). "
            "Professional jewelry photography with precise studio lighting using soft boxes and reflectors. "
            "The jewelry should be centered, showing maximum sparkle and reflections. "
            "Slight natural shadow for depth. Ultra-sharp focus on every facet and detail. "
            "Shot at f/11 for maximum depth of field with a 100mm macro lens. "
            "Commercial e-commerce quality, the piece occupies about 80% of the frame."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_02_selling_points",
        name="賣點標註圖",
        name_en="Feature Highlights",
        product_type="jewelry",
        description="展示材質、工藝、寶石等核心賣點",
        prompt=(
            "Create a professional jewelry infographic for this piece. "
            "Show the jewelry at a slight angle on a clean white background. "
            "Add elegant thin callout lines pointing to 3-4 key features: "
            "the gemstone type and quality, the metal material (e.g. 925 silver, 18K gold), "
            "the clasp/closure mechanism, and any special craftsmanship details. "
            "Each callout has a minimal icon and short text in an elegant serif font. "
            "Use dual soft box lighting at 45-degree angles for even, shadow-free illumination. "
            "Luxury aesthetic with balanced, airy composition."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_03_macro_detail",
        name="細節特寫",
        name_en="Macro Detail",
        product_type="jewelry",
        description="微距特寫，展示寶石切面、金屬光澤、鑲嵌工藝",
        prompt=(
            "Extreme macro close-up of this jewelry piece at very high magnification. "
            "Show the intricate details: gemstone facets catching light, "
            "metal surface finish and polish, precise setting work and prong details. "
            "Shot with a dedicated macro lens at 1:1 magnification and focus stacking for edge-to-edge sharpness. "
            "Dramatic side lighting from a focused spot at a low 15-degree angle to emphasize texture and depth. "
            "Aperture at f/8 for optimal sharpness. "
            "The level of detail should showcase exceptional craftsmanship."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_04_size_reference",
        name="尺寸參考圖",
        name_en="Size Reference",
        product_type="jewelry",
        description="手指/脖子/手腕佩戴，直觀展示大小比例",
        prompt=(
            "This jewelry piece worn on a person to demonstrate its actual size and proportion. "
            "Close-up shot showing the jewelry on skin (finger, wrist, neck, or ear depending on type). "
            "Clean, uncluttered background. Soft natural lighting on the skin. "
            "The focus is on showing how the piece looks in terms of scale relative to the body. "
            "Shot at f/4 with a 85mm portrait lens to gently blur skin texture while keeping the jewelry tack-sharp. "
            "Elegant and natural pose, no distracting elements."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_05_model_wearing",
        name="模特佩戴",
        name_en="Model Wearing",
        product_type="jewelry",
        description="模特佩戴展示，展示上身整體效果",
        prompt=(
            "A beautiful model elegantly wearing this jewelry piece. "
            "Close-up portrait from shoulders up, the jewelry is the clear focal point. "
            "Soft, flattering studio lighting with a clean neutral background. "
            "Use a key light with a large octabox at 45 degrees and a fill reflector opposite for gentle contouring. "
            "Shot at f/2.8 with a 105mm lens for flattering compression and shallow depth of field on the model. "
            "Fashion editorial style. The model wears minimal makeup and simple clothing "
            "to keep attention on the jewelry. The image conveys elegance and sophistication."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_06_outfit_scene",
        name="穿搭場景",
        name_en="Outfit Styling",
        product_type="jewelry",
        description="搭配日常服裝，展示佩戴效果",
        prompt=(
            "This jewelry styled with a fashionable outfit in a lifestyle setting. "
            "Show a person wearing the jewelry while dressed in an elegant outfit: "
            "a silk blouse, knit sweater, or little black dress. "
            "The setting is a bright, well-decorated room or outdoor cafe. "
            "Shoot from a slightly elevated three-quarter angle to capture both the jewelry and outfit context. "
            "Lifestyle photography that helps buyers visualize daily wear. "
            "Warm, natural lighting with fashion magazine aesthetic, using a large diffusion panel to soften direct sunlight."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_07_gift_box",
        name="禮盒搭配",
        name_en="Gift Box Pairing",
        product_type="jewelry",
        description="精美禮盒包裝，適合送禮場景展示",
        prompt=(
            "This jewelry presented in or beside an elegant jewelry gift box with satin ribbon. "
            "Gift-giving concept with romantic, luxurious styling. "
            "Soft diffused lighting from an overhead strip softbox angled at 30 degrees, with a small accent light to add sparkle to the jewelry. "
            "Subtle props like dried flowers or rose petals. "
            "The box is open showing the jewelry nestled in cushion. "
            "Camera positioned at a 30-degree overhead angle, shot at f/5.6 for balanced depth of field. "
            "Perfect for conveying 'ready to gift' - ideal for holidays and special occasions. "
            "Premium packaging photography aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_08_collection",
        name="多件展示",
        name_en="Collection Display",
        product_type="jewelry",
        description="多件首飾排列，展示系列搭配效果",
        prompt=(
            "This jewelry piece as the centerpiece, artfully arranged with complementary pieces "
            "(matching earrings, bracelet, ring, or necklace) in a curated collection layout. "
            "Clean white or soft gray surface. Organized, symmetrical arrangement. "
            "Overhead shot taken directly at 90 degrees with a 50mm lens at f/8 showing how pieces complement each other. "
            "Professional jewelry collection photography with even, shadowless lighting from a large overhead diffusion panel."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    SceneTemplate(
        id="jewelry_09_lifestyle",
        name="品牌氛圍圖",
        name_en="Brand Lifestyle",
        product_type="jewelry",
        description="奢華氛圍場景，香水、鮮花等道具營造品牌感",
        prompt=(
            "This jewelry in a dreamy, luxurious vanity table setting. "
            "Styled with a perfume bottle, fresh peonies or roses, a small mirror, "
            "and soft fabric like silk or velvet. "
            "Warm golden hour lighting creating a romantic, feminine atmosphere, "
            "enhanced with a warm-toned LED panel at low intensity as fill light. "
            "The jewelry catches beautiful light reflections. "
            "Shot at f/2.8 with a 50mm lens from a low 20-degree angle to create an intimate, immersive perspective. "
            "Instagram-worthy lifestyle photography that conveys luxury and romance."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="common",
        sub_category_name="通用場景",
    ),
    # ===== Necklace (項鏈) =====
    SceneTemplate(
        id="jewel_neck_01_wearing",
        name="佩戴展示",
        name_en="Necklace Wearing",
        product_type="jewelry",
        description="模特佩戴項鏈的近距離展示，聚焦頸部與胸口",
        prompt=(
            "Close-up of a model wearing this necklace, framing from chin to upper chest. "
            "The necklace drapes naturally along the collarbone and neckline. "
            "The model wears a simple off-shoulder or V-neck top in a neutral solid color. "
            "Soft, flattering key light from a large octabox positioned high at 45 degrees camera right. "
            "A silver reflector on the left gently fills shadows on the skin. "
            "Shot at f/3.5 with a 105mm macro lens for beautiful compression and shallow depth of field. "
            "Skin tones are warm and natural, the necklace is tack-sharp with visible sparkle. "
            "Elegant jewelry portrait photography emphasizing how the piece enhances the wearer."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="necklace",
        sub_category_name="項鏈",
    ),
    SceneTemplate(
        id="jewel_neck_02_layering",
        name="疊戴搭配",
        name_en="Necklace Layering",
        product_type="jewelry",
        description="多條項鏈疊戴的搭配展示，呈現層次美感",
        prompt=(
            "A model wearing this necklace layered with two to three complementary necklaces at different lengths. "
            "Close-up from shoulders up, showing the layering effect with chains at choker, princess, and matinee lengths. "
            "The hero necklace is the most prominent piece, with the others providing complementary accent. "
            "Clean neutral studio background in soft beige. "
            "Dual soft box lighting at 45 degrees on each side for even, sparkle-enhancing illumination. "
            "Shot at f/4 with a 85mm lens, focus precisely on the main necklace with slight softness on others. "
            "Fashion editorial style showcasing modern layering trends. "
            "The image inspires buyers to create their own layered necklace combinations."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="necklace",
        sub_category_name="項鏈",
    ),
    SceneTemplate(
        id="jewel_neck_03_pendant_detail",
        name="墜飾特寫",
        name_en="Pendant Close-up",
        product_type="jewelry",
        description="項鏈墜飾的微距特寫，展示雕刻或鑲嵌細節",
        prompt=(
            "Extreme macro close-up of this necklace's pendant, filling 90% of the frame. "
            "Show the intricate details of the pendant: engraving patterns, gemstone setting, metal finish, "
            "and the bail connecting the pendant to the chain. "
            "Shot at 1:1 magnification with a dedicated macro lens and focus stacking for complete sharpness. "
            "Dramatic spot lighting from the upper right at a 30-degree angle to create depth and highlight facets. "
            "A small reflector card on the left prevents total shadow. "
            "Dark charcoal background to make the pendant pop. "
            "The level of detail makes the craftsmanship unmistakable. "
            "Professional macro jewelry photography."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="necklace",
        sub_category_name="項鏈",
    ),
    SceneTemplate(
        id="jewel_neck_04_occasion",
        name="場合搭配",
        name_en="Occasion Styling",
        product_type="jewelry",
        description="項鏈搭配正式或休閒服裝，展示不同場合的佩戴效果",
        prompt=(
            "A split-image showing this necklace styled for two different occasions. "
            "Left panel: the necklace worn with a casual daytime outfit - a linen shirt or cozy knit sweater, "
            "in a bright cafe or park setting with natural daylight. "
            "Right panel: the same necklace with an elegant evening outfit - a black dress or silk camisole, "
            "in a dimly lit restaurant with warm candlelight ambiance. "
            "Both panels show the model from shoulders up with the necklace as the focal point. "
            "Shot at f/4 with a 70mm lens, consistent composition across both panels. "
            "The image demonstrates the necklace's versatility from day to night."
        ),
        aspect_ratio="4:3",
        injection_level="full",
        sub_category="necklace",
        sub_category_name="項鏈",
    ),
    SceneTemplate(
        id="jewel_neck_05_packaging",
        name="精美包裝",
        name_en="Elegant Packaging",
        product_type="jewelry",
        description="項鏈在精美禮盒中的展示，適合送禮選購",
        prompt=(
            "This necklace beautifully presented inside an open velvet jewelry box. "
            "The necklace is arranged in a gentle curve on the satin cushion lining, showing its full length and pendant. "
            "The box lid is propped open at a 45-degree angle, displaying a branded interior. "
            "A small satin ribbon and dried flower sprig beside the box for gift-giving atmosphere. "
            "Shot from a 40-degree overhead angle on a clean cream surface. "
            "Soft directional lighting from the upper left using a strip softbox with a warm accent light for sparkle. "
            "Shot at f/5.6 with a 50mm lens. "
            "Premium unboxing photography that conveys luxury gifting experience."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="necklace",
        sub_category_name="項鏈",
    ),
    # ===== Ring (戒指) =====
    SceneTemplate(
        id="jewel_ring_01_hand_pose",
        name="手部展示",
        name_en="Hand Pose",
        product_type="jewelry",
        description="戒指佩戴在模特手上的優雅姿態展示",
        prompt=(
            "Close-up of a model's hand wearing this ring in an elegant, natural pose. "
            "The hand is gracefully positioned - perhaps resting on a silk fabric surface or lightly touching the collarbone. "
            "Soft, warm skin tones with the ring catching beautiful highlights. "
            "Shot with a 100mm macro lens at f/3.5 for shallow depth of field, with the ring in tack-sharp focus. "
            "Key light from a large softbox at 60 degrees camera right, with a small reflector card below the hand for fill. "
            "Clean, minimalist background in soft beige or white. "
            "Well-groomed nails with a subtle nude polish complement the ring. "
            "Jewelry hand model photography with an intimate, refined aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="ring",
        sub_category_name="戒指",
    ),
    SceneTemplate(
        id="jewel_ring_02_stacking",
        name="疊戴效果",
        name_en="Ring Stacking",
        product_type="jewelry",
        description="多個戒指疊戴在手指上的搭配效果",
        prompt=(
            "A model's hand wearing this ring stacked with two to three complementary rings on adjacent fingers. "
            "The hero ring is on the ring finger, with thinner bands on the index and middle fingers. "
            "The hand is held slightly raised with fingers gently spread to show each ring clearly. "
            "Clean light gray studio background. "
            "Dual soft spot lights at 45 degrees on each side for even illumination with sparkle. "
            "Shot at f/4 with a 100mm macro lens for beautiful subject isolation. "
            "Focus is sharpest on the hero ring with a gentle fall-off on adjacent rings. "
            "Modern jewelry styling trend photography that encourages buyers to mix and match."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="ring",
        sub_category_name="戒指",
    ),
    SceneTemplate(
        id="jewel_ring_03_stone_detail",
        name="寶石特寫",
        name_en="Gemstone Close-up",
        product_type="jewelry",
        description="戒指寶石與鑲嵌工藝的微距特寫",
        prompt=(
            "Ultra-macro close-up of this ring's gemstone and its setting, filling the entire frame. "
            "Show the stone's facets catching and refracting light into prismatic sparkles. "
            "The prong or bezel setting metalwork is visible in extreme detail. "
            "Shot with a macro lens at greater than 1:1 magnification with multi-frame focus stacking. "
            "A precisely aimed fiber optic spot light from the upper right creates dramatic brilliance in the stone. "
            "A secondary diffused fill from the left prevents harsh shadows on the metal setting. "
            "Dark background to maximize the stone's fire and brilliance. "
            "The image conveys the stone's quality and the precision of the setting craftsmanship."
        ),
        aspect_ratio="1:1",
        injection_level="light",
        sub_category="ring",
        sub_category_name="戒指",
    ),
    SceneTemplate(
        id="jewel_ring_04_couple",
        name="對戒展示",
        name_en="Couple Rings",
        product_type="jewelry",
        description="情侶對戒或婚戒的雙人展示",
        prompt=(
            "Two matching rings displayed as a couple or wedding set. "
            "One ring leaning against the other on a smooth white marble surface, "
            "positioned to show that they are a harmonious matching pair. "
            "Soft romantic lighting with a warm color temperature of 4500K. "
            "A subtle diffused spot light from above creates a gentle glow on the metal surfaces. "
            "Dried baby's breath flowers and a silk ribbon in the background for romantic atmosphere. "
            "Shot at f/5.6 with a 100mm macro lens from a low 15-degree angle to emphasize the pairing. "
            "Warm, intimate mood lighting that evokes love and commitment. "
            "Premium wedding jewelry photography."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="ring",
        sub_category_name="戒指",
    ),
    SceneTemplate(
        id="jewel_ring_05_comparison",
        name="尺寸對比",
        name_en="Size Comparison",
        product_type="jewelry",
        description="戒指與硬幣等物品對比，直觀展示實際大小",
        prompt=(
            "This ring placed next to a standard coin for precise size reference. "
            "Both items are placed on a clean white surface, shot from directly above at 90 degrees. "
            "The ring and coin are positioned side by side with a small gap between them. "
            "Bright, even overhead lighting from a large diffusion panel for accurate detail rendering. "
            "A subtle ruler or millimeter scale graphic visible at the bottom edge of frame for exact measurement. "
            "Shot at f/11 with a 100mm macro lens for maximum sharpness on both objects. "
            "Color accuracy is critical, no color cast. "
            "Clean, informational product photography for accurate online size communication."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="ring",
        sub_category_name="戒指",
    ),
    # ===== Earring (耳環) =====
    SceneTemplate(
        id="jewel_ear_01_profile",
        name="側臉展示",
        name_en="Profile View",
        product_type="jewelry",
        description="模特側臉展示耳環的佩戴效果",
        prompt=(
            "A model photographed in profile view, showing this earring worn on the visible ear. "
            "The frame captures from the top of the head to the shoulder, with the earring as the focal point. "
            "Hair is tucked behind the ear or styled in an updo to fully reveal the earring. "
            "Clean studio background in soft neutral gray. "
            "Key light from a large beauty dish at 45 degrees camera right, sculpting the profile and highlighting the earring. "
            "A rim light from behind separates the model from the background. "
            "Shot at f/2.8 with a 85mm portrait lens for beautiful subject isolation. "
            "The earring is the sharpest element, catching brilliant highlights. "
            "Elegant fashion editorial jewelry portrait."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="earring",
        sub_category_name="耳環",
    ),
    SceneTemplate(
        id="jewel_ear_02_pair_display",
        name="對稱展示",
        name_en="Symmetrical Pair Display",
        product_type="jewelry",
        description="一對耳環對稱排列的產品展示",
        prompt=(
            "A matching pair of these earrings displayed symmetrically on a clean surface. "
            "Both earrings are placed side by side with perfect mirror symmetry, hooks pointing outward. "
            "Smooth white marble or matte cream surface as the base. "
            "Overhead studio lighting from a large diffusion panel directly above for even, shadow-free illumination. "
            "A small accent light at a low angle from the front adds sparkle to gemstones or metal. "
            "Shot at f/8 with a 100mm macro lens from directly above at 90 degrees. "
            "The pair fills about 70% of the frame, perfectly centered. "
            "Clean, precise product photography showcasing the pair's matching symmetry and design."
        ),
        aspect_ratio="1:1",
        injection_level="none",
        sub_category="earring",
        sub_category_name="耳環",
    ),
    SceneTemplate(
        id="jewel_ear_03_dangle_motion",
        name="動態垂墜",
        name_en="Dangle Motion",
        product_type="jewelry",
        description="垂墜耳環帶有輕微動態模糊的動感展示",
        prompt=(
            "A dangling earring captured in gentle motion, showing a subtle motion blur on the lower elements "
            "while the ear post and upper section remain sharp. "
            "The model has just turned her head slightly, causing the earring to sway. "
            "Close-up framing on the ear and earring from a three-quarter angle. "
            "Shot at a slower shutter speed of 1/60s with a 85mm lens at f/3.5. "
            "Soft studio lighting with a key light from the left and hair light from behind for rim separation. "
            "The slight motion blur on the dangle conveys movement, lightness, and playful elegance. "
            "Hair pulled back with a few loose strands for a natural, dynamic feel. "
            "Fashion-forward jewelry photography with a sense of life and movement."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="earring",
        sub_category_name="耳環",
    ),
    SceneTemplate(
        id="jewel_ear_04_hair_style",
        name="髮型搭配",
        name_en="Hairstyle Pairing",
        product_type="jewelry",
        description="耳環搭配盤髮或束髮造型的展示",
        prompt=(
            "A model with an elegant updo hairstyle wearing this earring, photographed from a rear three-quarter angle. "
            "The hair is swept up in a low bun or French twist, fully exposing the ear and earring. "
            "The earring is the sharpest element in the frame, catching light beautifully. "
            "The updo hairstyle and the nape of the neck provide elegant context. "
            "Soft key light from a large octabox at 60 degrees camera left for flattering illumination. "
            "A warm-toned rim light from behind highlights the hair texture and earring edge. "
            "Shot at f/3.5 with a 105mm lens for intimate compression. "
            "Clean studio backdrop in warm taupe. "
            "The image conveys sophistication and inspires formal styling ideas."
        ),
        aspect_ratio="3:4",
        injection_level="full",
        sub_category="earring",
        sub_category_name="耳環",
    ),
    SceneTemplate(
        id="jewel_ear_05_mirror",
        name="鏡面反射",
        name_en="Mirror Reflection",
        product_type="jewelry",
        description="耳環透過鏡面反射展示雙角度視覺效果",
        prompt=(
            "This earring displayed next to a small round vanity mirror, showing both the actual earring "
            "and its reflection for a dual-angle view. "
            "The earring is placed on a smooth surface beside the mirror, angled so the reflection shows a different perspective. "
            "The actual earring shows the front face; the mirror reveals the side or back design. "
            "Soft, diffused overhead lighting with a small spot accent to create sparkle in both the earring and its reflection. "
            "Shot at f/5.6 with a 85mm lens from a 30-degree elevated angle. "
            "Clean, minimal styling with a soft fabric surface beneath. "
            "Creative product photography that cleverly shows multiple angles in a single frame. "
            "Warm, inviting tones with a hint of luxury vanity aesthetic."
        ),
        aspect_ratio="1:1",
        injection_level="full",
        sub_category="earring",
        sub_category_name="耳環",
    ),
]

TemplateRegistry.register("jewelry", JEWELRY_TEMPLATES)
