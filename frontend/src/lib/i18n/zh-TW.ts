const zhTW = {
  // ---- Common / Navigation ----
  common: {
    appName: "AI 電商產品圖生成器",
    appNameShort: "AI 產品圖",
    appDesc: "上傳一張圖 → 生成 9 張專業場景圖",
    credits: "點數",
    settings: "設定",
    login: "登入",
    register: "註冊",
    logout: "登出",
    cancel: "取消",
    confirm: "確認",
    save: "儲存",
    delete: "刪除",
    edit: "編輯",
    close: "關閉",
    loading: "載入中",
    error: "錯誤",
    success: "成功",
    retry: "重試",
    download: "下載",
    upload: "上傳",
    preview: "預覽",
    back: "返回",
    next: "下一步",
    previous: "上一步",
    search: "搜尋",
    noData: "暫無資料",
    footerText: "AI 驅動 · 支援 20 種產品品類 · 180 種場景模板",
    language: "語言",
    switchLang: "切換語言",
  },

  // ---- Home / Wizard ----
  home: {
    apiKeyWarningTitle: "尚未設定 API Key",
    apiKeyWarningDesc: "需要先設定 Gemini API Key 才能生成圖片",
    goToSettings: "前往設定",
    step1Title: "上傳產品圖片",
    step1Subtitle: "拖拽或點擊上傳你的產品照片",
    step2Title: "選擇產品類型",
    step2Subtitle: "選擇最匹配你產品的品類，AI 將根據品類生成合適的場景",
    step3Title: "選擇視覺風格",
    step3SubtitlePrefix: "為",
    step3SubtitleSuffix: "推薦的拍攝風格",
    autoBgRemove: "自動去背",
    recommended: "建議開啟",
    previewBgRemove: "預覽去背",
    processing: "處理中",
    original: "原圖",
    bgRemoved: "去背後",
    generateButton: "一鍵生成 9 張產品圖",
    categoryLabel: "品類",
    costLabel: "消耗約 9 點",
    balanceLabel: "餘額",
    balanceUnit: "點",
    estimateTime: "預計 1-3 分鐘完成",
    uploadFailed: "上傳失敗",
    bgRemoveFailed: "去背失敗",
  },

  // ---- Image Uploader ----
  uploader: {
    dragOrClick: "拖拽或點擊上傳",
    supportedFormats: "支援 JPG、PNG、WebP 格式",
    maxSize: "最大 10MB",
    uploading: "上傳中...",
    changeImage: "更換圖片",
  },

  // ---- Generate / Results ----
  generate: {
    title: "生成結果",
    generating: "生成中",
    regenerating: "重新生成中",
    waiting: "等待中",
    failed: "生成失敗",
    retryAll: "重試失敗的",
    retryAllSuffix: "張",
    retrying: "重試中...",
    downloadThis: "下載此圖",
    regenerateThis: "重新生成此圖",
    generateVariants: "生成 4 張變體選最佳",
    selectBestVariant: "選擇最佳變體",
    selectThis: "選擇此張",
    replacing: "替換中...",
    variant: "變體",
    generatingVariants: "正在生成 4 張變體...",
    variantEstimate: "預計 30-60 秒",
    clickToReplace: "點擊任一張變體即可替換原圖",
    lightboxNav: "使用 ← → 鍵切換，Esc 關閉",
    prevImage: "上一張",
    nextImage: "下一張",
  },

  // ---- Download / Export ----
  download: {
    title: "批量下載",
    subtitle: "按平台規格打包 ZIP",
    shopee: "蝦皮 Shopee",
    momo: "MOMO",
    instagram: "IG 貼文",
    igStory: "IG 限動",
    facebook: "FB 貼文",
    line: "LINE 購物",
    general: "通用高畫質",
  },

  // ---- Detail Layout ----
  detailLayout: {
    title: "智慧詳情頁排版",
    singleView: "單圖預覽",
    longView: "長圖排版",
    heroModule: "首屏模組",
    heroDesc: "品牌海報 — 場景圖 + 商品名稱",
    sellingPoints: "賣點展示區",
    sellingPointsDesc: "細節圖與材質圖配對，自動標註功能說明",
    multiDisplay: "多維度展示區",
    multiDisplayDesc: "場景圖和平鋪圖排列",
    specFooter: "規格底部",
    specFooterDesc: "白底圖作為規格參考",
    addModule: "新增模組",
    removeModule: "移除模組",
    moveUp: "上移",
    moveDown: "下移",
    dragToReorder: "拖拽以調整順序",
    copywritingTitle: "AI 營銷文案",
    copywritingPlaceholder: "AI 將自動生成繁體中文營銷文案...",
    generateCopy: "生成文案",
    regenerateCopy: "重新生成",
    copywritingHint: "強調質感、CP值、必買理由",
    colorScheme: "色系選擇",
    layoutTemplate: "排版模板",
    templateClassic: "經典排版",
    templateMinimal: "極簡排版",
    templateBold: "大氣排版",
    templateGrid: "網格排版",
  },

  // ---- Festival Themes ----
  themes: {
    title: "節慶主題",
    subtitle: "一鍵切換詳情頁裝飾風格",
    noTheme: "無主題",
    double11: "雙 11 大促風",
    midAutumn: "中秋賞月風",
    springNew: "春季新品風",
    christmas: "聖誕節風",
    lunarNewYear: "農曆新年風",
    currentTheme: "目前主題",
    switchTheme: "切換主題",
    previewTheme: "預覽主題",
  },

  // ---- Export / Multi-platform ----
  export: {
    title: "多平台一鍵導出",
    subtitle: "勾選目標平台，一鍵生成各規格圖片",
    selectPlatforms: "選擇目標平台",
    shopee: "蝦皮 Shopee",
    shopeeSpec: "1:1 (800x800 / 1000x1000)",
    momo: "MOMO",
    momoSpec: "平台特定比例",
    pchome: "PChome",
    pchomeSpec: "平台特定比例",
    igPost: "Instagram 貼文",
    igPostSpec: "1:1 或 4:5",
    igStory: "Instagram 限動 / TikTok",
    igStorySpec: "9:16（需 AI 擴圖）",
    lineAd: "Line 營銷圖",
    lineAdSpec: "帶邊框海報規格",
    facebook: "Facebook",
    facebookSpec: "1:1 或 16:9",
    upscale4K: "4K 超分辨率修復",
    upscale4KDesc: "提升圖片至 4K 解析度（API 預留）",
    exportAll: "一鍵導出",
    exporting: "導出中...",
    previewCrop: "預覽裁切效果",
    needsOutpaint: "需 AI 擴圖",
    exportSuccess: "導出成功",
  },

  // ---- Storyboard / Scene names ----
  scenes: {
    lifestyle: "生活場景",
    flatlay: "平鋪擺拍",
    studio: "棚拍風格",
    outdoor: "戶外場景",
    detail: "細節特寫",
    whiteBackground: "白底圖",
    materialClose: "材質特寫",
    contextual: "情境搭配",
    packaging: "包裝展示",
  },

  // ---- Materials ----
  materials: {
    wood: "原木",
    marble: "大理石",
    fabric: "布料",
    metal: "金屬",
    leather: "皮革",
    ceramic: "陶瓷",
    glass: "玻璃",
    concrete: "水泥",
  },

  // ---- Atmosphere / Environment ----
  atmosphere: {
    warm: "溫暖柔光",
    cool: "冷調清新",
    natural: "自然光線",
    dramatic: "戲劇性光影",
    soft: "柔和朦朧",
    bright: "明亮通透",
  },

  // ---- Image Types ----
  imageTypes: {
    sceneImage: "場景圖",
    detailImage: "細節圖",
    materialImage: "材質圖",
    whiteImage: "白底圖",
    flatlayImage: "平鋪圖",
    lifestyleImage: "生活圖",
  },

  // ---- Auth ----
  auth: {
    loginTitle: "登入帳戶",
    registerTitle: "建立帳戶",
    email: "電子郵件",
    password: "密碼",
    confirmPassword: "確認密碼",
    displayName: "顯示名稱",
    loginButton: "登入",
    registerButton: "註冊",
    noAccount: "還沒有帳戶？",
    hasAccount: "已有帳戶？",
    loginFailed: "登入失敗",
    registerFailed: "註冊失敗",
  },

  // ---- Settings ----
  settingsPage: {
    title: "設定",
    apiKeySection: "API 金鑰設定",
    geminiKey: "Gemini API Key",
    togetherKey: "Together API Key",
    configured: "已設定",
    notConfigured: "未設定",
    saveKeys: "儲存金鑰",
  },

  // ---- Credits ----
  creditsPage: {
    title: "點數管理",
    balance: "目前餘額",
    unit: "點",
    history: "消費紀錄",
    noHistory: "暫無消費紀錄",
  },

  // ---- History ----
  history: {
    title: "歷史紀錄",
    noHistory: "暫無歷史紀錄",
    viewResult: "查看結果",
    imagesCount: "張圖片",
    creditsCost: "消耗點數",
  },

  // ---- Batch ----
  batch: {
    title: "批次處理",
    uploadMultiple: "上傳多張圖片",
    startBatch: "開始批次生成",
  },

  // ---- Projects ----
  projects: {
    title: "我的專案",
    newProject: "新建專案",
    noProjects: "暫無專案",
  },
} as const;

// Recursively widen all string literals to `string` so zh-CN can use different text
type DeepString<T> = {
  [K in keyof T]: T[K] extends string ? string : DeepString<T[K]>;
};

export type TranslationKeys = DeepString<typeof zhTW>;
export default zhTW as TranslationKeys;
