# 提示詞優化指南

## 優化前後對比

### 1. 相機參數（更專業）

**優化前：**
```
Professional e-commerce product photography...
```

**優化後：**
```
Camera: Sony A7R V with 90mm macro lens at f/8, ISO 100, 1/160s.
```

**為什麼更好：**
- 具體的相機型號讓 AI 知道圖片風格（Sony = 銳利現代，Hasselblad = 中片幅質感）
- 焦距決定透視（35mm = 自然，85mm = 人像，100mm macro = 微距）
- 光圈控制景深（f/1.4 = 淺景深，f/8 = 全景深）

---

### 2. 光線設置（更精確）

**優化前：**
```
soft box lighting from above at 45 degrees
```

**優化後：**
```
Large octagonal softbox overhead at 45° (main), 
two strip boxes on sides for fill (ratio 2:1), 
white bounce cards below for shadow fill. 
Color temperature 5500K ± 200K.
```

**為什麼更好：**
- 燈具類型決定光質（softbox = 柔和，ring light = 無陰影，bare bulb = 硬光）
- 光比控制對比度（2:1 = 溫和，4:1 = 戲劇性）
- 色溫確保色彩準確（5500K = 標準白光，3200K = 暖光）

---

### 3. 否定提示（避免問題）

**新增：**
```
NEGATIVE: No props, no text, no watermark, no reflections on white surface, 
no harsh shadows, no color tint, no blur, no background gradient.
```

**為什麼重要：**
- AI 常見問題：白底圖出現陰影或反射
- 電商要求：純白背景，無干擾元素
- 否定提示明確告訴 AI 不要生成什麼

---

### 4. 產品特定細節

**優化前：**
```
crisp details on stitching, hardware and material texture
```

**優化後：**
```
Zone A: Material texture - leather grain, canvas weave pattern, or nylon ripstop texture at 1:1 magnification.
Zone B: Precision stitching - even thread tension, consistent stitch length (8-10 stitches per inch visible).
Zone C: Metal hardware - zipper teeth, pull tab, buckle mechanism with surface reflections.
```

**為什麼更好：**
- 具體的細節描述讓 AI 知道要強調什麼
- 車線密度（8-10針/英寸）是真實產品細節
- 分區描述確保整個產品都被正確渲染

---

### 5. 色彩數值（風格一致性）

**優化前：**
```
pastel palette: blush pink, cream, lavender, and mint tones
```

**優化後：**
```
Color palette: Soft pastels - baby pink (#FFD1DC), lavender (#E6E6FA), mint (#F5FFFA), cream (#FFFDD0).
Background: Soft gradient from white to blush pink (#FFE4E1) or soft lavender (#E6E6FA).
```

**為什麼更好：**
- HEX 色碼確保 AI 生成準確的顏色
- 避免 AI 對「粉色」的不同理解
- 保持品牌色彩一致性

---

## 應用優化提示詞

### 步驟 1：備份原始檔案
```bash
cp bags.py bags_original.py
cp styles/korean_soft.py styles/korean_soft_original.py
```

### 步驟 2：查看優化檔案
我已經創建了兩個優化檔案：
- `bags_optimized.py` - 優化後的包包模板
- `styles/korean_soft_v2.py` - 優化後的韓系風格

### 步驟 3：整合到系統

**選項 A：直接替換（測試用）**
```python
# 在 __init__.py 中
# 把 from app.templates import bags
# 改成 from app.templates import bags_optimized as bags
```

**選項 B：新增優化風格**
```python
# 在 styles/__init__.py 中加入
from app.templates.styles import korean_soft_v2  # 會自動註冊 korean_soft_v2
```

**選項 C：漸進式更新**
```python
# 逐步替換單個模板
# 1. 先測試 bag_01_white_bg 優化版本
# 2. 確認效果後再更新其他模板
```

---

## 驗證優化效果

### 測試清單：

| 檢查項目 | 優化前 | 優化後 |
|---------|--------|--------|
| 白底純度 | 可能有灰或有陰影 | RGB 255,255,255 純白 |
| 產品銳利度 | 可能較軟 | 90mm macro f/8 超銳 |
| 色彩準確度 | 可能有色偏 | 5500K 標準白光 |
| 陰影控制 | 可能過重或過亂 | 柔和漸變陰影 |
| 細節呈現 | 可能模糊 | 車線、五金清晰 |

---

## 其他優化建議

### 1. 為每個品類創建專屬模板

目前所有包包共用模板，但可以細分：
- 皮革包：強調皮紋、縫線、金屬扣
- 帆布包：強調布料質感、印刷圖案
- 運動包：強調功能性、防水材質

### 2. 風格與產品匹配

| 產品類型 | 推薦風格 | 原因 |
|---------|---------|------|
| 精品包 | luxury_editorial | 突顯高級感 |
| 休閒包 | lifestyle_warm | 親和力強 |
| 文青包 | japanese_natural | 質感生活 |
| 時尚包 | korean_soft | 年輕潮流 |

### 3. 平台特定優化

**蝦皮 (Shopee)：**
- 白底主圖（符合平台規範）
- 高對比度（縮圖時更清晰）
- 加強賣點標註

**Instagram：**
- 正方形或 4:5 比例
- 生活場景為主
- 強調氛圍感

**品牌官網：**
- 高品質細節圖
- 多角度展示
- 品牌調性一致

---

## 需要我幫你做什麼？

1. **整合優化版本到系統** - 我幫你修改 __init__.py 啟用優化版本
2. **為其他品類優化** - 珠寶、服裝、3C 等
3. **創建新風格** - 特定品牌調性或季節風格
4. **測試優化效果** - 生成對比圖片驗證

請告訴我你想怎麼進行！
