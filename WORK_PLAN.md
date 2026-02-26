# 電商產品圖生成器 — 提示詞工程工作文檔

## 一、專案定位

這是一個 **AI 電商產品攝影圖片生成 SaaS**，使用者上傳一張產品原圖，系統自動生成 9 張專業電商場景圖（白底圖、場景圖、細節圖、材質圖、平鋪圖、模特圖）。

**核心流程：** 上傳產品圖 → 嚮導選擇（品類/材質/場景/模特）→ 故事板預覽 → 確認生成高清圖 → 結果頁下載/編輯 → 詳情頁排版

**目前狀態：** 前後端 UI 已完成，但所有提示詞模板是 **mock 數據**，需要改成真正可以應用到 AI 圖片生成 API 的提示詞。

---

## 二、系統架構中的提示詞位置

```
使用者操作                     對應提示詞模板                        所在檔案
─────────────────────────────────────────────────────────────────────────────
Step 1: 選擇品類              → V1 品類模板 (20 品類)              backend/app/templates/*.py
Step 2: 選擇材質              → 材質提示詞 (12 種)                 frontend/src/lib/api.ts + backend/analysis.py
Step 3: 選擇場景              → 場景提示詞 (16 場景)               frontend/src/lib/api.ts + backend/scenes.py
Step 3: 選擇模特              → 模特提示詞 (8 預設)                frontend/src/lib/api.ts + backend/analysis.py
Step 3: 選擇氛圍              → 氛圍光照提示詞 (10 預設)           backend/atmosphere.py
Step 3: 選擇節日主題          → 節日主題提示詞 (7 主題)            backend/themes.py
故事板: 9 宮格圖片類型        → 圖片類型提示詞 (9 類型)            backend/storyboard.py
生成: AI 出圖                 → 組合提示詞 = 品類 + 材質 + 場景 + 氛圍 + 圖片類型
```

---

## 三、提示詞模板清單（現狀）

### A. 前端 V2 場景模板（16 個）

| # | ID | 名稱 | 分類 | 提示詞長度 | 現狀評估 |
|---|-----|------|------|-----------|---------|
| 1 | scene-jp-minimal | 日系極簡 | indoor | ~200 字 | ✅ 已有詳細提示詞 |
| 2 | scene-nordic | 北歐風 | indoor | ~200 字 | ✅ 已有詳細提示詞 |
| 3 | scene-kr-cream | 韓系奶油風 | indoor | ~200 字 | ✅ 已有詳細提示詞 |
| 4 | scene-modern-loft | 現代 LOFT | indoor | ~200 字 | ✅ 已有詳細提示詞 |
| 5 | scene-luxury-marble | 奢華大理石 | indoor | ~180 字 | ✅ 已有詳細提示詞 |
| 6 | scene-warm-studio | 暖光棚拍 | indoor | ~180 字 | ✅ 已有詳細提示詞 |
| 7 | scene-white-bg | 純白主圖 | indoor | ~150 字 | ✅ 已有詳細提示詞 |
| 8 | scene-detail-macro | 細節微距 | indoor | ~180 字 | ✅ 已有詳細提示詞 |
| 9 | scene-street | 城市街景 | outdoor | ~200 字 | ✅ 已有詳細提示詞 |
| 10 | scene-camping | 露營野趣 | outdoor | ~200 字 | ✅ 已有詳細提示詞 |
| 11 | scene-beach | 海濱度假 | outdoor | ~200 字 | ✅ 已有詳細提示詞 |
| 12 | scene-garden | 花園庭院 | outdoor | ~200 字 | ✅ 已有詳細提示詞 |
| 13 | scene-cafe | 文藝咖啡廳 | outdoor | ~200 字 | ✅ 已有詳細提示詞 |
| 14 | scene-rooftop | 天台夕陽 | outdoor | ~200 字 | ✅ 已有詳細提示詞 |
| 15 | scene-mountain | 山野徒步 | outdoor | ~180 字 | ✅ 已有詳細提示詞 |
| 16 | scene-night-neon | 霓虹夜景 | outdoor | ~180 字 | ✅ 已有詳細提示詞 |

**檔案位置：** `frontend/src/lib/api.ts` 第 434-790 行

---

### B. 前端 V2 材質模板（12 個）

| # | ID | 名稱 | promptHint 長度 | 現狀評估 |
|---|-----|------|----------------|---------|
| 1 | mat-leather | 真皮 | ~20 字 | ✅ 已有 |
| 2 | mat-canvas | 帆布 | ~20 字 | ✅ 已有 |
| 3 | mat-metal | 精鑄金屬 | ~20 字 | ✅ 已有 |
| 4 | mat-ceramic | 手工陶瓷 | ~20 字 | ✅ 已有 |
| 5 | mat-wood | 實木 | ~20 字 | ✅ 已有 |
| 6 | mat-glass | 硼矽玻璃 | ~20 字 | ✅ 已有 |
| 7 | mat-silk | 真絲 | ~20 字 | ✅ 已有 |
| 8 | mat-bamboo | 竹纖維 | ~20 字 | ✅ 已有 |
| 9 | mat-nylon | 再生尼龍 | ~20 字 | ✅ 已有 |
| 10 | mat-steel | 不鏽鋼 | ~20 字 | ✅ 已有 |
| 11 | mat-linen | 亞麻 | ~20 字 | ✅ 已有 |
| 12 | mat-resin | 環氧樹脂 | ~20 字 | ✅ 已有 |

**檔案位置：** `frontend/src/lib/api.ts` 第 793-904 行

---

### C. 前端 V2 模特預設（8 個）

| # | ID | 名稱 | 性別 | 族裔 | 年齡 | 現狀評估 |
|---|-----|------|-----|------|-----|---------|
| 1 | model-ea-f-01 | 清新甜美 | 女 | 東亞 | 20-25 | ✅ 已有 poseHint |
| 2 | model-ea-f-02 | 知性優雅 | 女 | 東亞 | 28-35 | ✅ 已有 poseHint |
| 3 | model-ea-m-01 | 陽光運動 | 男 | 東亞 | 25-32 | ✅ 已有 poseHint |
| 4 | model-ea-m-02 | 文藝書生 | 男 | 東亞 | 22-30 | ✅ 已有 poseHint |
| 5 | model-eu-f-01 | 時尚超模 | 女 | 歐美 | 22-30 | ✅ 已有 poseHint |
| 6 | model-eu-m-01 | 都市雅痞 | 男 | 歐美 | 30-38 | ✅ 已有 poseHint |
| 7 | model-sa-f-01 | 異域風情 | 女 | 南亞 | 23-30 | ✅ 已有 poseHint |
| 8 | model-mixed-f-01 | 混血時尚 | 女 | 混血 | 22-28 | ✅ 已有 poseHint |

**檔案位置：** `frontend/src/lib/api.ts` 第 907-1006 行

---

### D. 後端氛圍光照預設（10 個）

| # | ID | 名稱 | 色溫 | 亮度 | prompt_modifier | 現狀評估 |
|---|-----|------|-----|------|----------------|---------|
| 1 | atm_warm_afternoon | 暖陽午後 | 4500K | 0.85 | ✅ 已有 | ✅ |
| 2 | atm_cold_industrial | 清冷工業風 | 6500K | 0.70 | ✅ 已有 | ✅ |
| 3 | atm_natural_soft | 自然柔光 | 5000K | 0.80 | ✅ 已有 | ✅ |
| 4 | atm_golden_hour | 黃金時刻 | 3500K | 0.75 | ✅ 已有 | ✅ |
| 5 | atm_studio_bright | 攝影棚亮光 | 5500K | 1.00 | ✅ 已有 | ✅ |
| 6 | atm_moody_dark | 暗調氛圍 | 4000K | 0.45 | ✅ 已有 | ✅ |
| 7 | atm_pastel_dream | 粉彩夢境 | 5200K | 0.90 | ✅ 已有 | ✅ |
| 8 | atm_neon_night | 霓虹夜景 | 7000K | 0.55 | ✅ 已有 | ✅ |
| 9 | atm_sunrise_fresh | 清晨日出 | 5800K | 0.75 | ✅ 已有 | ✅ |
| 10 | atm_candlelight | 燭光晚餐 | 2700K | 0.40 | ✅ 已有 | ✅ |

**檔案位置：** `backend/app/routers/atmosphere.py` 第 23-114 行

---

### E. 後端節日主題（7 個）

| # | ID | 名稱 | prompt_modifier | 現狀評估 |
|---|-----|------|----------------|---------|
| 1 | theme_double11 | 雙 11 購物節 | ✅ 已有 | ✅ |
| 2 | theme_mid_autumn | 中秋節 | ✅ 已有 | ✅ |
| 3 | theme_spring_new | 春季新品 | ✅ 已有 | ✅ |
| 4 | theme_christmas | 聖誕節 | ✅ 已有 | ✅ |
| 5 | theme_lunar_new_year | 農曆新年 | ✅ 已有 | ✅ |
| 6 | theme_valentines | 情人節 | ✅ 已有 | ✅ |
| 7 | theme_summer_sale | 夏日特賣 | ✅ 已有 | ✅ |

**檔案位置：** `backend/app/routers/themes.py` 第 23-94 行

---

### F. 後端 V1 品類模板（20 品類，~120+ 模板）

| # | 檔案 | 品類 | 模板數量 | 提示詞品質 |
|---|------|------|---------|-----------|
| 1 | clothing.py | 服飾 | ~8 模板 | ✅ 專業級提示詞 |
| 2 | bags.py | 包包 | ~8 模板 | ✅ 專業級提示詞 |
| 3 | jewelry.py | 飾品 | ~8 模板 | ✅ 專業級提示詞 |
| 4 | shoes.py | 鞋子 | ~8 模板 | ✅ 專業級提示詞 |
| 5 | electronics.py | 3C 電子 | ~8 模板 | ✅ 專業級提示詞 |
| 6 | beauty.py | 美妝 | ~6 模板 | ✅ 專業級提示詞 |
| 7 | home.py | 居家 | ~6 模板 | ✅ 專業級提示詞 |
| 8 | toys.py | 玩具 | ~6 模板 | ✅ 專業級提示詞 |
| 9 | sports.py | 運動 | ~6 模板 | ✅ 專業級提示詞 |
| 10 | food.py | 食品 | ~6 模板 | ✅ 專業級提示詞 |
| 11 | stationery.py | 文具 | ~6 模板 | ✅ 專業級提示詞 |
| 12 | pets.py | 寵物 | ~6 模板 | ✅ 專業級提示詞 |
| 13 | automotive.py | 汽車 | ~6 模板 | ✅ 專業級提示詞 |
| 14 | phones.py | 手機 | ~6 模板 | ✅ 專業級提示詞 |
| 15 | travel.py | 旅行 | ~6 模板 | ✅ 專業級提示詞 |
| 16 | fashion_acc.py | 配飾 | ~6 模板 | ✅ 專業級提示詞 |
| 17 | kitchenware.py | 廚房 | ~8 模板 | ✅ 專業級提示詞 |
| 18 | health.py | 保健 | ~8 模板 | ✅ 專業級提示詞 |
| 19 | hobbies.py | 興趣 | ~8 模板 | ✅ 專業級提示詞 |
| 20 | motorcycle.py | 機車 | ~8 模板 | ✅ 專業級提示詞 |

**檔案位置：** `backend/app/templates/*.py`

---

### G. 故事板 9 宮格圖片類型（9 類型）

| # | 圖片類型 | 中文描述 | 攝影指導 |
|---|---------|---------|---------|
| 1 | 主圖 - 白底正面 | 純白背景居中展示 | 雙側柔光箱 45° 均勻照明 |
| 2 | 主圖 - 白底 45° | 白底 45 度側面展示 | 突出產品輪廓與立體感 |
| 3 | 情境圖 - 生活場景 | 日常使用情境 | 自然光環境，增強購買代入感 |
| 4 | 情境圖 - 使用場景 | 展示產品功能與使用方式 | 突出實際體驗效果 |
| 5 | 細節圖 - 材質特寫 | 100mm 微距鏡頭近攝 | 低角度側光突顯紋理與工藝品質 |
| 6 | 細節圖 - 功能展示 | 拉鍊、扣環、口袋等功能部件特寫 | 展示設計巧思 |
| 7 | 模特圖 - 正面穿搭 | 虛擬模特全身正面展示 | 自然站姿配合專業棚拍燈光 |
| 8 | 尺寸對比圖 | 產品搭配常見物品尺寸參照 | 直觀展示實際大小 |
| 9 | 包裝展示圖 | 禮盒或包裝全景 | 展示開箱體驗與品牌質感 |

**檔案位置：** `backend/app/routers/storyboard.py` 第 43-53 行

---

## 四、需要確認的問題

### 問題 1：提示詞的應用目標
目前提示詞存在 mock 數據中。要讓它們真正「應用」，需要做以下哪些？

- [ ] **A. 組合提示詞邏輯**：在生成 API 中，自動將「場景 + 材質 + 氛圍 + 節日主題 + 品類模板」組合成最終的完整提示詞，送給 Gemini API
- [ ] **B. 提示詞品質優化**：對現有提示詞內容進行專業級改寫，確保每條提示詞都能產出高品質電商圖
- [ ] **C. 提示詞工程化**：加入負面提示詞（negative prompt）、品質控制參數、風格一致性控制等
- [ ] **D. 前後端打通**：將前端選擇的場景/材質/模特/氛圍傳遞到後端，後端組裝完整提示詞後呼叫 AI API

### 問題 2：AI 生成引擎
- 目前後端已配置 Gemini API Key (`AIzaSyDBQnuu9lV8JVGGoOuMrtXiqvy-6j_P_Ho`)
- 是否要接通 Gemini Imagen API 真正生成圖片？還是先完善提示詞模板，圖片生成後續再接？

### 問題 3：Demo 展示圖片
- 在 AI 生成功能接通之前，前端的 demo 圖片需要用什麼樣的圖？
- 是否需要我用固定的產品圖（例如一個包包）作為主題，所有 demo 圖都圍繞這個產品展示？

---

## 五、提示詞組合邏輯（建議方案）

當使用者在嚮導中選擇完所有選項後，最終送給 AI 的提示詞應該這樣組合：

```
最終提示詞 = [品類基礎模板.prompt]
           + [場景模板.prompt]
           + [材質.promptHint]
           + [氛圍.prompt_modifier]
           + [節日主題.prompt_modifier]（如有選擇）
           + [模特.poseHint]（如有選擇）
           + [圖片類型攝影指導]
           + [品質控制語句]
```

**範例組合（包包 + 日系極簡場景 + 真皮材質 + 暖陽午後氛圍）：**

```
[品類] A premium leather handbag displayed in professional e-commerce photography style.

[場景] Product displayed in a serene Japanese minimalist interior setting. Clean tatami
or light hinoki wood surface with plenty of negative space. Muted earth tones — warm beige,
off-white, and soft gray. Soft natural light streaming through shoji paper screens.

[材質] Rich genuine leather texture with natural grain patterns, warm brown tones, subtle
sheen from oils and age.

[氛圍] Warm afternoon sunlight at 4500K color temperature, soft golden side lighting,
cozy and inviting atmosphere.

[品質] Shot with a 50mm lens at f/4. Ultra high resolution, 8K commercial product photography,
professionally color-graded, no watermarks, clean composition.
```

---

## 六、統計摘要

| 模組 | 數量 | 提示詞狀態 | 需要修改 |
|------|------|-----------|---------|
| V2 場景模板 | 16 | ✅ 已有詳細提示詞 | 待確認是否需優化 |
| V2 材質模板 | 12 | ✅ 已有 promptHint | 待確認是否需優化 |
| V2 模特預設 | 8 | ✅ 已有 poseHint | 待確認是否需優化 |
| 氛圍光照 | 10 | ✅ 已有 prompt_modifier | 待確認是否需優化 |
| 節日主題 | 7 | ✅ 已有 prompt_modifier | 待確認是否需優化 |
| V1 品類模板 | ~120+ | ✅ 已有專業提示詞 | 待確認是否需優化 |
| 故事板圖片類型 | 9 | ✅ 已有攝影指導 | 待確認是否需優化 |
| **組合邏輯** | — | ❌ 尚未實作 | **核心待開發** |
| **AI API 串接** | — | ❌ 尚未串接 | **核心待開發** |
| **Demo 展示圖** | — | ⚠️ 使用隨機圖片 | 需替換為產品圖 |

---

**請確認以上內容後，告訴我你想先從哪個部分開始。**
