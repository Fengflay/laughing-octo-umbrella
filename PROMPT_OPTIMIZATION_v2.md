# 電商產品圖片生成模板 - 優化版本

## 優化原則

1. **具體相機參數** - 指定相機型號、鏡頭、光圈、ISO
2. **精確光線設置** - 燈具類型、角度、色溫、光比
3. **產品特定細節** - 材質、紋理、五金、車線等
4. **否定提示** - 避免常見 AI 生成問題
5. **平台合規要素** - 白底純度、無水印、準確色彩

---

## 包包類 (Bags) - 優化提示詞

### 1. 白底主圖 (bag_01_white_bg)

**原始版本：**
```
Place this bag product on a pure white background (RGB 255,255,255). Professional e-commerce product photography with soft box lighting from above at 45 degrees and two side fill lights...
```

**優化版本：**
```
Professional e-commerce product photography of a bag on pure white background (RGB 255,255,255). 

Camera: Sony A7R V with 90mm macro lens at f/8, ISO 100, 1/160s. 

Lighting: Large octagonal softbox (48-inch) overhead at 45° (main light at 60% power), two strip boxes on sides at 30° for fill (ratio 2:1), white bounce cards below for shadow fill. Color temperature precisely 5500K ± 200K.

Composition: Product centered, occupying 75-85% of frame. Slight 15° tilt to show depth. 

Product details: Natural soft shadow beneath (feathered, not harsh), ultra-sharp focus on front surface, stitching details visible at 100% zoom. Material texture clearly rendered: leather grain visible, canvas weave pattern distinct, nylon sheen accurate. No color cast, true product colors.

NEGATIVE: No props, no text, no watermark, no reflections on white surface, no harsh shadows, no color tint, no blur, no background gradient, no visible dust or fingerprints.
```

### 2. 賣點標註圖 (bag_02_selling_points)

**優化版本：**
```
Four-panel professional product specification grid for a bag, clean 2x2 layout on pure white background (RGB 255,255,255).

Panel 1 (Top-Left): Front view at 10° angle showing overall silhouette and brand logo placement.
Panel 2 (Top-Right): Macro detail of material texture and stitching quality (8-10 stitches per inch visible).
Panel 3 (Bottom-Left): Hardware detail - zipper pull, buckle, metal clasp with visible metallic reflections.
Panel 4 (Bottom-Right): Strap and carrying mechanism from side angle, showing attachment points.

Camera: Sony A7 IV with 90mm lens at f/5.6, ISO 100, 1/200s for all panels.

Lighting: Consistent 5500K studio strobes across all panels, large octagonal softbox main light at 45°, two fill cards for even illumination. Each panel has 20px white space border.

NEGATIVE: No text overlays, no arrows, no inconsistent lighting between panels, no color variation between panels.
```

### 3. 細節特寫 (bag_03_detail_closeup)

**優化版本：**
```
Extreme macro detail photography of bag craftsmanship, focus stacking technique for maximum sharpness.

Camera: Canon EOS R5 with RF 100mm f/2.8L Macro at f/4, ISO 200, 1/200s, 15-frame focus stack.

Zone A: Material texture - leather grain at 1:1 magnification showing pore structure, OR canvas weave pattern with thread count visible, OR nylon ripstop texture with grid pattern.
Zone B: Precision stitching - even thread tension, consistent stitch length (8-10 SPI visible), thread color matching.
Zone C: Metal hardware - zipper teeth interlocking, pull tab engraving, buckle mechanism surface reflections.

Lighting: Ring light (18-inch, 4800K) for even illumination + single directional side light at 45° to reveal texture via micro-shadows. Neutral gray 18% card background.

NEGATIVE: No dust particles, no fingerprints on hardware, no loose threads, no uneven lighting, no color cast.
```

### 4. 尺寸參考圖 (bag_04_size_reference)

**優化版本：**
```
Bag photographed for precise size reference with standardized objects on pure white surface with millimeter grid pattern overlay.

Reference objects arranged symmetrically: 
- 15-inch laptop (MacBook Pro or equivalent) standing vertically on left
- iPhone 15 Pro (6.1-inch) placed horizontally on right
- Standard A4 sheet behind for additional scale

Camera: Sony A7 IV with 50mm lens at f/11, ISO 100, 1/125s, tripod at 90° overhead.

Lighting: Large rectangular softbox directly overhead + two side fill lights, 5500K even illumination.

Composition: All items proportionally accurate, bag centered as hero element. Grid lines visible at 1cm intervals for precise measurement reference.

NEGATIVE: No perspective distortion, no inconsistent scaling, no shadows obscuring reference objects.
```

### 5. 日常場景 (bag_05_daily_scene)

**優化版本：**
```
Lifestyle product photography of bag in modern premium cafe setting.

Scene setup: Light oak wooden table (natural finish), MacBook Pro partially visible in background, ceramic coffee cup (8oz, white ceramic) with latte art nearby, small succulent in 3-inch white pot as accent.

Camera: Sony A7 IV with 35mm f/1.4 at f/2.8, ISO 400, 1/125s.

Lighting: Natural window light from left side (5600K, soft diffused through sheer white curtain). Gentle shadows on right side, fill reflector card on right at 20% intensity.

Composition: Bag placed naturally on table, slightly angled toward camera (30° from front), as if just set down. Shallow depth of field: bag in sharp focus, background softly blurred (circular bokeh visible). 

Color palette: Warm neutrals (#F5F5DC cream, #D2B48C tan, #8B7355 brown), green plant accent (#6B8E6B).

Mood: Productive morning, aspirational yet relatable lifestyle.

NEGATIVE: No harsh artificial lighting, no cluttered background, no competing colors, no plastic-looking props.
```

### 6. 戶外場景 (bag_06_outdoor_scene)

**優化版本：**
```
Outdoor lifestyle product photography of bag in urban park setting.

Location: Clean wooden park bench or natural stone ledge, city street or manicured park visible in soft-focus background.

Time: Golden hour (sunset, ~6:30 PM, 45 minutes before sunset).

Camera: Sony A7 IV with 85mm f/1.4 at f/2.0, ISO 200, 1/250s.

Lighting: Golden hour natural light from left at 30° angle, creating warm tones (3200K) and gentle shadows. Natural rim light on bag edges.

Composition: Bag is hero subject, sharply focused against dreamy bokeh background (f/2.0). Travel and adventure lifestyle mood.

Atmosphere: Warm tones, aspirational outdoor lifestyle, wanderlust aesthetic.

NEGATIVE: No harsh midday shadows, no overexposed highlights, no distracting background elements.
```

### 7. 模特展示 (bag_07_model_carry)

**優化版本：**
```
Fashion editorial photography: model wearing/carrying bag as hero accessory.

Camera: Hasselblad X2D with 80mm f/1.9 at f/4, ISO 100, 1/250s.

Studio setup: 
- Large octabox (60-inch) as key light camera left at 45°, 60% power
- White fill card camera right at 20% reflectivity
- Hair light from behind for separation
- Gray seamless backdrop (#808080)

Model styling: Simple solid-color clothing (black #000000, white #FFFFFF, or beige #F5F5DC) that doesn't compete with bag. Minimal accessories.

Pose: Natural confident stance, 3/4 view to camera, bag clearly visible at chest/hip level. Hand position shows natural carrying gesture.

Focus: Critical sharpness on bag surface and hardware, slight softness on model's face acceptable.

Color grading: Neutral with slight warmth (+10 yellow), maintaining bag's true colors.

NEGATIVE: No busy patterns on clothing, no distracting jewelry, no harsh shadows on bag.
```

### 8. 容量展示 (bag_08_capacity_show)

**優化版本：**
```
Top-down flat lay of bag showing organized interior capacity.

Contents arranged: Smartphone (iPhone), leather wallet, keychain with 3 keys, sunglasses in case, reusable water bottle (500ml), Moleskine notebook (pocket size), wireless earphones, cosmetic pouch.

Arrangement: Items color-coded and evenly spaced with intentional white space. Each item partially overlapping bag edges to show depth.

Camera: Sony A7 IV with 35mm lens at f/8, ISO 100, 1/160s, tripod at 90° overhead.

Lighting: Large rectangular softbox directly overhead (5500K), two side fill lights at 45° for even illumination with no harsh shadows.

Background: Pure white surface (RGB 255,255,255).

NEGATIVE: No messy arrangement, no items outside bag frame, no inconsistent spacing.
```

### 9. 品牌氛圍圖 (bag_09_lifestyle)

**優化版本：**
```
Elegant flat lay brand lifestyle arrangement with bag as hero product.

Accessories: Designer sunglasses (black frame), luxury watch (minimalist dial), leather passport holder, fresh peonies (pink #FFB6C1) in small ceramic vase.

Surface: Carrara marble or clean cream-colored linen (#FFFDD0).

Camera: Hasselblad X2D with 80mm at f/5.6, ISO 100, 1/200s, tripod at 90° overhead.

Lighting: Soft directional light from upper left at 45°, subtle shadows creating depth. Fill reflector on right at 30%.

Color palette: Cohesive warm tones - cream (#FFFDD0), soft pink (#FFB6C1), gold accents (#FFD700), black (#000000).

Composition: Rule of thirds, bag at left intersection point. Each object placed with intentional spacing (2-3 inches between items).

Mood: Premium quality, aspirational lifestyle, luxury travel aesthetic.

NEGATIVE: No clutter, no competing colors, no harsh shadows.
```

---

## 飾品類 (Jewelry) - 優化提示詞

### 1. 白底主圖 (jewelry_01_white_bg)

**優化版本：**
```
Professional high-jewelry photography on pure white background (RGB 255,255,255).

Camera: Phase One XF with 120mm macro lens at f/16, ISO 50, 1/125s.

Lighting: Dual large softboxes at 45° angles + overhead diffusion panel. Fiber optic spot lights for controlled sparkle on gemstones. Color temperature 5500K.

Special technique: Focus stacking (20+ frames) for complete sharpness from front to back. LED light panel for controlled reflections.

Product: Jewelry centered, 80% of frame. Maximum sparkle and fire visible in gemstones. Metal surfaces showing polish quality.

NEGATIVE: No dust particles, no fingerprints, no unwanted reflections, no color cast.
```

### 2. 細節特寫 (jewelry_03_macro_detail)

**優化版本：**
```
Ultra-macro jewelry photography at 2:1 magnification.

Camera: Canon EOS R5 with MP-E 65mm f/2.8 1-5x Macro at 3x magnification, f/8, ISO 400, focus stacking 30+ frames.

Details visible: 
- Gemstone facets (57 facets on brilliant cut diamond)
- Pavilion and crown angles
- Inclusion clarity characteristics
- Prong setting precision
- Metal surface polish (mirror finish)

Lighting: Fiber optic dual-arm illuminator with diffusers. Cross-polarization to eliminate metal glare while maintaining gemstone sparkle.

Background: Deep black velvet (#000000) for maximum contrast.

NEGATIVE: No dust, no lint fibers, no smudges, no shallow depth of field.
```

---

## 風格定義優化

### 韓系柔光 (Korean Soft)

**優化版本 - LIGHT 等級：**
```
Korean beauty aesthetic product photography with soft, dreamy qualities.

Lighting: 18-inch ring light directly in front at 1-meter distance, two small LED panels (Bi-color 3200K-5600K) on sides at 30° for subtle fill, set to 4500K.

Color palette: Soft pastels - baby pink (#FFD1DC), lavender (#E6E6FA), mint (#F5FFFA), cream (#FFFDD0).

Props (select 1-2): Dried baby's breath in small ceramic vase (white or blush pink), thin satin ribbon (2cm width, champagne color), small pearl dish (3-inch), clear glass with sparkling water.

Camera: 85mm lens at f/2.8 for gentle background blur.

Post-processing: Lifted blacks (+20), reduced contrast (-15), subtle pink tint in highlights (+10 magenta), soft highlight roll-off.

NEGATIVE: No harsh shadows, no dark backgrounds, no warm orange tones, no cluttered composition.
```

**優化版本 - FULL 等級：**
```
Korean K-beauty editorial lifestyle photography with complete immersion.

Scene: Bright, airy pastel-toned space. Light marble surface (white with gray veining #F5F5F5). Background soft gradient from white to blush pink (#FFE4E1) or lavender (#E6E6FA).

Lighting: 48-inch octagonal softbox directly overhead + two large diffused panels on sides. Ring light as fill to eliminate all shadows. 5500K pure white.

Camera: Sony A7 IV with 50mm f/1.2 at f/2.0, ISO 100, 1/160s. Angle: 30° above horizontal.

Props arrangement (choose 2-3): 
- Dried flower arrangement: baby's breath, cotton stems, pampas grass in ceramic vase (white, 4-inch)
- Satin ribbon: 2cm width, champagne or blush, loosely draped in S-curve
- Pearl accents: small dish (3-inch) with 3-5 scattered pearls
- Pastel ceramic tray: hexagonal in mint or pink
- Clear glass: sparkling water with lemon slice

Composition: Asymmetrical balance, product as hero at left-third intersection. Rule of thirds applied.

Background: Soft gaussian blur (bokeh circles visible), dreamy ethereal quality.

Color grade: Lifted blacks (+25), reduced contrast (-20), highlights tinted pink (+15 magenta), shadows slightly blue/cyan (+10), overall saturation reduced (-10), clarity reduced (-10) for soft glow.

Mood: Youthful elegance, curated lifestyle, innocent romance, aspirational femininity.

NEGATIVE: No harsh directional lighting, no deep shadows, no dark wood, no metallic industrial props, no bold/contrasting colors, no text overlays, no messy clutter, no yellow/orange color cast.
```

### 日系自然 (Japanese Natural)

**優化版本 - LIGHT 等級：**
```
Japanese natural aesthetic product photography with wabi-sabi philosophy.

Color palette: Warm earth tones - raw wood (#D2B48C), natural linen (#F5F5DC), muted greens (#8FBC8F), cream (#FFFDD0).

Lighting: Soft ambient window light, gentle golden warmth (4200K), no direct sunlight.

Textures: Natural wood grain visible, linen weave texture, handmade ceramic imperfections.

Composition: Asymmetric, off-center (rule of thirds), embracing gentle imperfection. Negative space appreciated.

Mood: Tranquil, meditative, understated elegance, clean simplicity.

NEGATIVE: No harsh artificial lighting, no bright saturated colors, no perfect symmetry, no plastic materials.
```

**優化版本 - FULL 等級：**
```
Japanese zakka and Muji-inspired lifestyle photography with complete wabi-sabi immersion.

Scene: Beside window with soft, diffused natural light streaming from left. Raw light-oak wood table surface (#D2B48C), natural linen or cotton cloth as backdrop accent (#F5F5DC).

Time: Warm, unhurried morning (9-10 AM), soft light.

Props: Single seasonal accent - small ceramic tea cup (handmade), sprig of dried pampas grass, linen napkin, or handmade pottery plate.

Lighting: Natural window light only, no artificial lights. Warm golden light (4000K) with soft shadows from window frame.

Camera: 50mm lens at f/2.8, natural perspective.

Color grading: Warm midtones, slightly desaturated (-15%), creamy highlights, lifted blacks (+15), reduced contrast (-10).

Mood: Handcrafted quality, mindful living, calm, editorial, zakka-magazine composition.

NEGATIVE: No harsh artificial light, no saturated colors, no perfect geometric arrangements, no modern synthetic materials visible.
```

---

## 使用說明

### 1. 提示詞結構

每個優化後的提示詞包含：
- **相機參數**: 具體型號、鏡頭、光圈、ISO、快門
- **光線設置**: 燈具類型、位置、功率、色溫
- **構圖細節**: 角度、比例、位置
- **產品細節**: 材質、紋理、特定特徵
- **否定提示**: 避免常見問題

### 2. 風格注入機制

根據模板定義的 `injection_level`：
- **none**: 不使用風格修飾（白底圖、尺寸圖）
- **light**: 輕量風格提示（細節特寫）
- **full**: 完整風格沉浸（生活場景、模特展示）

### 3. 平台適配

- **蝦皮/淘寶**: 強調白底純度、高對比度
- **Instagram**: 正方形或 4:5，生活場景為主
- **品牌官網**: 高品質細節，多角度展示

---

## 下一步建議

1. **批次優化**: 我可以繼續優化其他品類（服飾、鞋子、3C 等）
2. **風格擴展**: 創建更多風格（歐美極簡、中式古典、工業風等）
3. **CSV 匯出**: 將優化版本匯出為可更新的 CSV 檔案

需要我繼續優化哪些品類？
