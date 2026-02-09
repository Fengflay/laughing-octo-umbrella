# ecom-image-gen — AI 電商產品圖生成器

> 上傳一張產品照片，一鍵生成 9 張不同場景的電商展示圖。
> 支援 10 大產品類別 + 4 種視覺風格（歐美/日系/韓系/中式）。

---

## 目錄

- [功能概覽](#功能概覽)
- [技術棧](#技術棧)
- [快速開始](#快速開始)
- [專案結構](#專案結構)
- [後端架構](#後端架構)
- [前端架構](#前端架構)
- [風格系統](#風格系統)
- [API 文檔](#api-文檔)
- [模板系統](#模板系統)
- [部署指南](#部署指南)

---

## 功能概覽

| 功能 | 說明 |
|------|------|
| 多品類支援 | 包包、首飾、服裝、鞋類、3C、美妝、家居、母嬰、運動、食品 共 10 類 |
| AI 圖片生成 | Google Gemini + Together AI (Kimi K2.5) 雙引擎 |
| 視覺風格 | 歐美極簡 / 日式侘寂 / 韓系夢幻 / 新中式國風 |
| 智慧去背 | 基於 rembg 的 ML 自動去背景 |
| 即時進度 | Server-Sent Events (SSE) 即時推送生成進度 |
| 批次生成 | 每個品類 9 種場景模板一次生成 |
| 選擇性生成 | 可勾選需要的場景，不必全部生成 |
| 單張重新生成 | 對不滿意的結果重新生成，支援自訂 Prompt |
| 平台導出 | 蝦皮 / 淘寶 / Amazon 等平台尺寸自動適配 |
| API Key 管理 | 網頁 UI 設定 API Key，無需手動編輯 .env |

### 使用流程

```
上傳產品圖 → 選擇產品類型 → 選擇視覺風格（可選）→ 一鍵生成 9 張圖 → 下載 ZIP
```

---

## 技術棧

| 層級 | 技術 |
|------|------|
| 前端框架 | Next.js 15 (App Router) |
| UI 框架 | React 19 + TypeScript |
| CSS | Tailwind CSS v4 |
| 後端框架 | FastAPI (Python) |
| AI 引擎 | Google Gemini (`gemini-2.5-flash-image`) |
| AI 備援 | Together AI (Kimi K2.5) |
| 去背景 | rembg 2.0 (ML 模型) |
| 圖片處理 | Pillow 11 |
| 伺服器 | Uvicorn (ASGI) |
| 即時通訊 | Server-Sent Events (SSE) |

---

## 快速開始

### 前提條件

- Python 3.11+
- Node.js 18+
- Google Gemini API Key（[取得方式](https://aistudio.google.com/apikey)）
- Together AI API Key（可選，用於 Kimi 備援引擎）

### 1. 安裝後端

```bash
cd backend

# 建立虛擬環境
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate    # Windows

# 安裝依賴
pip install -r requirements.txt

# 設定環境變數（或透過網頁 UI 設定）
cp .env.example .env
# 編輯 .env 填入 GEMINI_API_KEY
```

### 2. 安裝前端

```bash
cd frontend
npm install
```

### 3. 啟動服務

```bash
# 終端 1 — 啟動後端 (port 8000)
cd backend
./venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 終端 2 — 啟動前端 (port 3000)
cd frontend
npm run dev -- -H 0.0.0.0
```

### 4. 開啟瀏覽器

```
http://localhost:3000
```

首次使用請先到 `/settings` 頁面設定 Gemini API Key。

---

## 專案結構

```
ecom-image-gen/
├── frontend/                          # Next.js 前端
│   ├── src/
│   │   ├── app/                       # 頁面路由
│   │   │   ├── layout.tsx             # 全域佈局（Header + Main）
│   │   │   ├── page.tsx               # 首頁（上傳 + 選擇）
│   │   │   ├── error.tsx              # 全域錯誤邊界
│   │   │   ├── generate/
│   │   │   │   ├── page.tsx           # 生成頁（SSE + 結果）
│   │   │   │   └── error.tsx          # 生成頁錯誤邊界
│   │   │   └── settings/
│   │   │       └── page.tsx           # API Key 設定頁
│   │   ├── components/                # React 組件
│   │   │   ├── ImageUploader.tsx      # 拖放上傳組件
│   │   │   ├── ProductTypeSelector.tsx# 產品類型選擇器
│   │   │   ├── StyleSelector.tsx      # 視覺風格選擇器
│   │   │   ├── TemplateGrid.tsx       # 模板選擇網格
│   │   │   ├── TemplateCard.tsx       # 單張模板卡片
│   │   │   ├── GenerationProgress.tsx # 生成進度條
│   │   │   ├── ResultGrid.tsx         # 結果圖片網格 + Lightbox
│   │   │   └── DownloadPanel.tsx      # 下載面板
│   │   ├── lib/
│   │   │   └── api.ts                 # API 客戶端封裝
│   │   └── types/
│   │       └── index.ts               # TypeScript 型別定義
│   ├── next.config.ts                 # API 代理重寫
│   └── package.json
│
└── backend/                           # FastAPI 後端
    ├── app/
    │   ├── main.py                    # FastAPI 應用入口
    │   ├── config.py                  # 環境配置
    │   ├── models/
    │   │   └── schemas.py             # Pydantic 資料模型
    │   ├── routers/
    │   │   ├── upload.py              # 上傳 + 去背 API
    │   │   ├── generate.py            # 生成 + 下載 API
    │   │   └── settings.py            # API Key 管理 API
    │   ├── services/
    │   │   ├── generation_service.py  # 核心生成管線
    │   │   ├── gemini_service.py      # Gemini API 整合
    │   │   ├── kimi_service.py        # Together AI 整合
    │   │   └── background_removal.py  # rembg 去背景
    │   └── templates/
    │       ├── registry.py            # 模板註冊中心
    │       ├── bags.py … food.py      # 10 個品類模板（每個 9 場景）
    │       └── styles/
    │           ├── registry.py        # 風格註冊 + prompt 組裝
    │           ├── western.py         # 歐美極簡風格
    │           ├── japanese.py        # 日式侘寂風格
    │           ├── korean.py          # 韓系夢幻風格
    │           └── chinese.py         # 新中式國風風格
    ├── requirements.txt
    ├── uploads/                       # 上傳的圖片
    └── outputs/                       # 生成的圖片
```

---

## 後端架構

### 核心流程

```
POST /api/generate
    ↓
GenerationService.create_task()     ← 建立任務，過濾模板
    ↓
GET /api/generate/{task_id}/status  ← SSE 連線
    ↓
GenerationService.run_generation()  ← 非同步並行生成
    ↓
  ┌─ 對每個模板：
  │   1. 取得 base prompt
  │   2. StyleRegistry.assemble_prompt()  ← 注入風格修飾
  │   3. 呼叫 Gemini / Kimi API
  │   4. 儲存輸出 PNG
  │   5. 更新進度 → SSE 推送
  └─
    ↓
ZIP 打包下載（可選平台尺寸適配）
```

### 任務管理

- 記憶體內 `OrderedDict` 儲存（非持久化）
- 自動清理：任務超過 1 小時過期 / 總數超過 200 則清除最舊的
- 併發控制：`asyncio.Semaphore` 限制最多 3 個同時生成
- SSE 重入防護：狀態機 `pending → starting → running → completed`

### AI Provider 選擇

每個模板有 `recommended_provider` 欄位：
- `"gemini"`（預設）— 使用 Google Gemini
- `"kimi"` — 使用 Together AI (Kimi K2.5)

生成失敗時自動用**同一 Provider** 重試一次。

---

## 前端架構

### 頁面流程

```
首頁 (page.tsx)
├── Step 1: ImageUploader → 上傳圖片
├── Step 2: ProductTypeSelector → 選擇品類
├── Step 3: StyleSelector → 選擇風格（可選）
└── Step 4: 一鍵生成按鈕 → 跳轉 /generate

生成頁 (generate/page.tsx)
├── Phase 1: TemplateGrid → 選擇模板
├── Phase 2: GenerationProgress + ResultGrid → 生成中
└── Phase 3: ResultGrid + DownloadPanel → 完成
```

### 狀態管理

純 React Hooks，無外部狀態庫：
- `useState` — 各步驟的本地狀態
- `useCallback` — 函數穩定引用
- `useEffect` — 副作用（API 呼叫、鍵盤事件監聽）
- `useRef` — SSE 取消訂閱函數引用

### SSE 即時通訊

```typescript
subscribeToGeneration(taskId, onEvent, onError)
// 事件類型：
// - "started"   → 開始生成
// - "progress"  → 單張完成，推送當前結果
// - "completed" → 全部完成
// - "error"     → 發生錯誤
```

### Lightbox 功能

- 點擊圖片放大檢視
- `←` `→` 鍵盤切換前後張
- `Esc` 關閉
- 顯示 N/M 圖片序號
- 下載、關閉按鈕

---

## 風格系統

### 設計理念

風格是**正交修飾層 (Orthogonal Modifier Layer)**，不與模板做笛卡爾乘積。

```
最終 prompt = style_prefix + base_template_prompt + style_suffix
```

### 三級注入機制

並非所有模板都適合注入風格。依據模板角色分三級：

| 注入等級 | 對應模板 | 行為 |
|---------|---------|------|
| `none` | 01 白底主圖、02 賣點標註、04 尺寸參考 | **不注入**風格（保持功能性） |
| `light` | 03 細節特寫、08 容量/多件展示 | **輕量注入**（影響光線、材質感） |
| `full` | 05-07 場景/模特、09 品牌氛圍 | **完整注入**（改變整體場景設定） |

### 四種風格定義

| 風格 | ID | 視覺特徵 |
|------|----|---------|
| 歐美極簡 | `western` | 北歐風、大量留白、柔和自然光、中性色調 |
| 日式侘寂 | `japanese` | 侘寂美學、溫潤素材、禪意空間、季節元素 |
| 韓系夢幻 | `korean` | 粉彩色調、無影打光、乾燥花、浪漫精緻 |
| 新中式國風 | `chinese` | 朱紅金墨、東方元素、戲劇光影、文化自信 |

### 新增風格

在 `backend/app/templates/styles/` 下新增 Python 檔：

```python
# styles/tropical.py
from app.templates.styles.registry import StyleDefinition, StyleRegistry, InjectionLevel

_style = StyleDefinition(
    id="tropical",
    name="熱帶度假",
    name_en="Tropical Resort",
    description="熱帶度假風，棕櫚葉、海灘、明亮飽和色",
    icon="🌴",
    preview_color="#00BFA5",
    modifiers={
        InjectionLevel.LIGHT: {
            "prefix": "Tropical resort photography. Bright, saturated colors. ",
            "suffix": " Palm leaves and natural sunlight accents.",
        },
        InjectionLevel.FULL: {
            "prefix": "Tropical resort lifestyle product photography. Beach setting... ",
            "suffix": " Coconut, tropical flowers, turquoise water in background...",
        },
    },
)

StyleRegistry.register_style(_style)
```

然後在 `styles/__init__.py` 加一行 import 即可生效。

---

## API 文檔

### 上傳

```http
POST /api/upload
Content-Type: multipart/form-data

file: <binary>
```

**回應：**
```json
{
  "image_id": "a1b2c3d4",
  "filename": "product.jpg",
  "url": "/api/uploads/a1b2c3d4.jpg"
}
```

### 去背景

```http
POST /api/remove-bg/{image_id}
```

**回應：**
```json
{
  "image_id": "a1b2c3d4",
  "original_url": "/api/uploads/a1b2c3d4.jpg",
  "removed_bg_url": "/api/uploads/a1b2c3d4_nobg.png"
}
```

### 取得風格列表

```http
GET /api/styles
```

**回應：**
```json
[
  {
    "id": "western",
    "name": "歐美極簡",
    "name_en": "Western Minimalist",
    "description": "乾淨明亮的北歐極簡風格...",
    "icon": "🇺🇸",
    "preview_color": "#F5F0EB"
  }
]
```

### 取得產品類型

```http
GET /api/product-types
```

**回應：**
```json
[
  {
    "id": "bags",
    "name": "包包/背包",
    "name_en": "Bags & Backpacks",
    "icon": "👜",
    "template_count": 9
  }
]
```

### 取得模板列表

```http
GET /api/templates/{product_type}
```

### 啟動生成

```http
POST /api/generate
Content-Type: application/json

{
  "image_id": "a1b2c3d4",
  "product_type": "bags",
  "remove_bg": true,
  "style": "japanese",
  "selected_template_ids": ["bag_01_white_bg", "bag_05_daily_scene"]
}
```

**回應：**
```json
{
  "task_id": "f9e8d7c6b5a4",
  "status": "pending",
  "total": 2
}
```

### SSE 即時進度

```http
GET /api/generate/{task_id}/status
Accept: text/event-stream
```

**事件流：**
```
data: {"event": "started", "task_id": "...", "total": 9}

data: {"event": "progress", "task_id": "...", "progress": 3, "total": 9, "results": [...]}

data: {"event": "completed", "task_id": "...", "status": "completed", "results": [...]}
```

### 下載 ZIP

```http
GET /api/download/{task_id}?platform=shopee
```

平台選項：`shopee` (800x800) / `taobao` (800x800) / `amazon` (1000x1000) / `general` (1024x1024)

### 單張重新生成

```http
POST /api/generate/{task_id}/regenerate
Content-Type: application/json

{
  "template_id": "bag_05_daily_scene",
  "custom_prompt": "This bag on a wooden desk in a cozy home office..."
}
```

### API Key 管理

```http
GET  /api/settings/api-keys       # 查詢狀態
POST /api/settings/api-keys       # 儲存 Key
```

---

## 模板系統

### 9 種場景角色

每個產品類別都有 9 個場景模板，角色固定：

| # | 角色 | 說明 | 注入等級 |
|---|------|------|---------|
| 01 | 白底主圖 | 純白背景產品照，符合平台主圖規範 | none |
| 02 | 賣點標註 | 2x2 多角度拼圖展示核心賣點 | none |
| 03 | 細節特寫 | 微距特寫材質、工藝、配件細節 | light |
| 04 | 尺寸參考 | 與常見物品對比展示實際大小 | none |
| 05 | 日常場景 | 咖啡廳/辦公室等日常使用情境 | full |
| 06 | 戶外場景 | 街頭/公園/旅行等戶外使用 | full |
| 07 | 模特展示 | 真人模特使用/佩戴/穿搭展示 | full |
| 08 | 容量/多件 | 展示內部空間或系列搭配 | light |
| 09 | 品牌氛圍 | 精緻擺拍，營造品牌調性 | full |

### 新增產品類別

1. 在 `backend/app/templates/` 下建立 `newcategory.py`
2. 定義 9 個 `SceneTemplate`，遵循 ID 命名規範 `{type}_{##}_{scene}`
3. 呼叫 `TemplateRegistry.register("newcategory", templates)`
4. 在 `templates/__init__.py` 加 import
5. 在 `registry.py` 的 `product_type_info` dict 加中英文名稱和 icon
6. 在 `schemas.py` 的 `ProductType` enum 加新值

---

## 部署指南

### 環境變數

```env
# 必填
GEMINI_API_KEY=your_gemini_api_key

# 可選
TOGETHER_API_KEY=your_together_api_key
CORS_ORIGINS=http://localhost:3000,https://your-domain.com
```

### 生產環境部署

```bash
# 後端
cd backend
./venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 2

# 前端
cd frontend
npm run build
npm start
```

### 注意事項

- 後端使用記憶體內任務儲存，重啟後任務丟失
- 生成的圖片儲存在 `outputs/` 目錄，需要定期清理
- rembg 首次使用會下載約 170MB 的 ML 模型
- Gemini API 有速率限制，`MAX_CONCURRENT_GENERATIONS` 預設為 3
- 前端透過 `next.config.ts` 的 rewrites 代理 API 請求到後端

---

## 授權

本專案僅供學習與商業使用。
