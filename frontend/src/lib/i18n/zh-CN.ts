import type { TranslationKeys } from "./zh-TW";

const zhCN: TranslationKeys = {
  // ---- Common / Navigation ----
  common: {
    appName: "AI 电商产品图生成器",
    appNameShort: "AI 产品图",
    appDesc: "上传一张图 → 生成 9 张专业场景图",
    credits: "点数",
    settings: "设置",
    login: "登录",
    register: "注册",
    logout: "退出",
    cancel: "取消",
    confirm: "确认",
    save: "保存",
    delete: "删除",
    edit: "编辑",
    close: "关闭",
    loading: "加载中",
    error: "错误",
    success: "成功",
    retry: "重试",
    download: "下载",
    upload: "上传",
    preview: "预览",
    back: "返回",
    next: "下一步",
    previous: "上一步",
    search: "搜索",
    noData: "暂无数据",
    footerText: "AI 驱动 · 支持 20 种产品品类 · 180 种场景模板",
    language: "语言",
    switchLang: "切换语言",
  },

  // ---- Home / Wizard ----
  home: {
    apiKeyWarningTitle: "尚未设置 API Key",
    apiKeyWarningDesc: "需要先设置 Gemini API Key 才能生成图片",
    goToSettings: "前往设置",
    step1Title: "上传产品图片",
    step1Subtitle: "拖拽或点击上传你的产品照片",
    step2Title: "选择产品类型",
    step2Subtitle: "选择最匹配你产品的品类，AI 将根据品类生成合适的场景",
    step3Title: "选择视觉风格",
    step3SubtitlePrefix: "为",
    step3SubtitleSuffix: "推荐的拍摄风格",
    autoBgRemove: "自动去背",
    recommended: "建议开启",
    previewBgRemove: "预览去背",
    processing: "处理中",
    original: "原图",
    bgRemoved: "去背后",
    generateButton: "一键生成 9 张产品图",
    categoryLabel: "品类",
    costLabel: "消耗约 9 点",
    balanceLabel: "余额",
    balanceUnit: "点",
    estimateTime: "预计 1-3 分钟完成",
    uploadFailed: "上传失败",
    bgRemoveFailed: "去背失败",
  },

  // ---- Image Uploader ----
  uploader: {
    dragOrClick: "拖拽或点击上传",
    supportedFormats: "支持 JPG、PNG、WebP 格式",
    maxSize: "最大 10MB",
    uploading: "上传中...",
    changeImage: "更换图片",
  },

  // ---- Generate / Results ----
  generate: {
    title: "生成结果",
    generating: "生成中",
    regenerating: "重新生成中",
    waiting: "等待中",
    failed: "生成失败",
    retryAll: "重试失败的",
    retryAllSuffix: "张",
    retrying: "重试中...",
    downloadThis: "下载此图",
    regenerateThis: "重新生成此图",
    generateVariants: "生成 4 张变体选最佳",
    selectBestVariant: "选择最佳变体",
    selectThis: "选择此张",
    replacing: "替换中...",
    variant: "变体",
    generatingVariants: "正在生成 4 张变体...",
    variantEstimate: "预计 30-60 秒",
    clickToReplace: "点击任一张变体即可替换原图",
    lightboxNav: "使用 ← → 键切换，Esc 关闭",
    prevImage: "上一张",
    nextImage: "下一张",
  },

  // ---- Download / Export ----
  download: {
    title: "批量下载",
    subtitle: "按平台规格打包 ZIP",
    shopee: "虾皮 Shopee",
    momo: "MOMO",
    instagram: "IG 帖子",
    igStory: "IG 快拍",
    facebook: "FB 帖子",
    line: "LINE 购物",
    general: "通用高画质",
  },

  // ---- Detail Layout ----
  detailLayout: {
    title: "智慧详情页排版",
    singleView: "单图预览",
    longView: "长图排版",
    heroModule: "首屏模块",
    heroDesc: "品牌海报 — 场景图 + 商品名称",
    sellingPoints: "卖点展示区",
    sellingPointsDesc: "细节图与材质图配对，自动标注功能说明",
    multiDisplay: "多维度展示区",
    multiDisplayDesc: "场景图和平铺图排列",
    specFooter: "规格底部",
    specFooterDesc: "白底图作为规格参考",
    addModule: "新增模块",
    removeModule: "移除模块",
    moveUp: "上移",
    moveDown: "下移",
    dragToReorder: "拖拽以调整顺序",
    copywritingTitle: "AI 营销文案",
    copywritingPlaceholder: "AI 将自动生成中文营销文案...",
    generateCopy: "生成文案",
    regenerateCopy: "重新生成",
    copywritingHint: "强调品质、性价比、必买理由",
    colorScheme: "色系选择",
    layoutTemplate: "排版模板",
    templateClassic: "经典排版",
    templateMinimal: "极简排版",
    templateBold: "大气排版",
    templateGrid: "网格排版",
  },

  // ---- Festival Themes ----
  themes: {
    title: "节庆主题",
    subtitle: "一键切换详情页装饰风格",
    noTheme: "无主题",
    double11: "双 11 大促风",
    midAutumn: "中秋赏月风",
    springNew: "春季新品风",
    christmas: "圣诞节风",
    lunarNewYear: "农历新年风",
    currentTheme: "当前主题",
    switchTheme: "切换主题",
    previewTheme: "预览主题",
  },

  // ---- Export / Multi-platform ----
  export: {
    title: "多平台一键导出",
    subtitle: "勾选目标平台，一键生成各规格图片",
    selectPlatforms: "选择目标平台",
    shopee: "虾皮 Shopee",
    shopeeSpec: "1:1 (800x800 / 1000x1000)",
    momo: "MOMO",
    momoSpec: "平台特定比例",
    pchome: "PChome",
    pchomeSpec: "平台特定比例",
    igPost: "Instagram 帖子",
    igPostSpec: "1:1 或 4:5",
    igStory: "Instagram 快拍 / TikTok",
    igStorySpec: "9:16（需 AI 扩图）",
    lineAd: "Line 营销图",
    lineAdSpec: "带边框海报规格",
    facebook: "Facebook",
    facebookSpec: "1:1 或 16:9",
    upscale4K: "4K 超分辨率修复",
    upscale4KDesc: "提升图片至 4K 分辨率（API 预留）",
    exportAll: "一键导出",
    exporting: "导出中...",
    previewCrop: "预览裁切效果",
    needsOutpaint: "需 AI 扩图",
    exportSuccess: "导出成功",
  },

  // ---- Storyboard / Scene names ----
  scenes: {
    lifestyle: "生活场景",
    flatlay: "平铺摆拍",
    studio: "棚拍风格",
    outdoor: "户外场景",
    detail: "细节特写",
    whiteBackground: "白底图",
    materialClose: "材质特写",
    contextual: "情境搭配",
    packaging: "包装展示",
  },

  // ---- Materials ----
  materials: {
    wood: "原木",
    marble: "大理石",
    fabric: "布料",
    metal: "金属",
    leather: "皮革",
    ceramic: "陶瓷",
    glass: "玻璃",
    concrete: "水泥",
  },

  // ---- Atmosphere / Environment ----
  atmosphere: {
    warm: "温暖柔光",
    cool: "冷调清新",
    natural: "自然光线",
    dramatic: "戏剧性光影",
    soft: "柔和朦胧",
    bright: "明亮通透",
  },

  // ---- Image Types ----
  imageTypes: {
    sceneImage: "场景图",
    detailImage: "细节图",
    materialImage: "材质图",
    whiteImage: "白底图",
    flatlayImage: "平铺图",
    lifestyleImage: "生活图",
  },

  // ---- Auth ----
  auth: {
    loginTitle: "登录账户",
    registerTitle: "创建账户",
    email: "电子邮件",
    password: "密码",
    confirmPassword: "确认密码",
    displayName: "显示名称",
    loginButton: "登录",
    registerButton: "注册",
    noAccount: "还没有账户？",
    hasAccount: "已有账户？",
    loginFailed: "登录失败",
    registerFailed: "注册失败",
  },

  // ---- Settings ----
  settingsPage: {
    title: "设置",
    apiKeySection: "API 密钥设置",
    geminiKey: "Gemini API Key",
    togetherKey: "Together API Key",
    configured: "已设置",
    notConfigured: "未设置",
    saveKeys: "保存密钥",
  },

  // ---- Credits ----
  creditsPage: {
    title: "点数管理",
    balance: "当前余额",
    unit: "点",
    history: "消费记录",
    noHistory: "暂无消费记录",
  },

  // ---- History ----
  history: {
    title: "历史记录",
    noHistory: "暂无历史记录",
    viewResult: "查看结果",
    imagesCount: "张图片",
    creditsCost: "消耗点数",
  },

  // ---- Batch ----
  batch: {
    title: "批次处理",
    uploadMultiple: "上传多张图片",
    startBatch: "开始批次生成",
  },

  // ---- Projects ----
  projects: {
    title: "我的项目",
    newProject: "新建项目",
    noProjects: "暂无项目",
  },
} as const;

export default zhCN;
