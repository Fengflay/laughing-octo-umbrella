import type {
  ApiKeysStatus,
  CopywritingResponse,
  GeneratedImage,
  GenerateResultResponse,
  GenerateTaskResponse,
  HistoryItem,
  PaginatedHistory,
  ProductTypeInfo,
  RemoveBgResponse,
  SceneTemplate,
  SSEEvent,
  StyleInfo,
  UploadResponse,
} from "@/types";
import { authHeaders, clearAuth, getToken } from "@/lib/auth";

const API_BASE = "/api";

async function parseErrorResponse(res: Response, fallback: string): Promise<string> {
  try {
    const text = await res.text();
    try {
      const json = JSON.parse(text);
      if (typeof json.detail === "string") return json.detail;
      if (Array.isArray(json.detail)) return json.detail.map((d: { msg?: string }) => d.msg).join("; ");
      return fallback;
    } catch {
      return text || fallback;
    }
  } catch {
    return fallback;
  }
}

/**
 * Wrapper around fetch that automatically adds auth headers and handles 401.
 */
async function authFetch(url: string, options: RequestInit & { skipAuthRedirect?: boolean } = {}): Promise<Response> {
  const { skipAuthRedirect, ...fetchOptions } = options;
  const headers = {
    ...authHeaders(),
    ...(fetchOptions.headers || {}),
  };

  const res = await fetch(url, { ...fetchOptions, headers });

  // Auto-clear auth on 401 (token expired/invalid)
  if (res.status === 401) {
    clearAuth();
    // Only redirect if explicitly allowed (not skipped) and not already on auth pages
    if (!skipAuthRedirect && typeof window !== "undefined" && !window.location.pathname.startsWith("/login") && !window.location.pathname.startsWith("/register")) {
      window.location.href = "/login";
    }
  }

  return res;
}

export async function uploadImage(file: File): Promise<UploadResponse> {
  const formData = new FormData();
  formData.append("file", file);

  const res = await authFetch(`${API_BASE}/upload`, {
    method: "POST",
    body: formData,
    skipAuthRedirect: true, // Let the caller handle auth errors (demo mode)
  });

  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Upload failed");
    throw new Error(msg);
  }

  return res.json();
}

export async function removeBackground(imageId: string): Promise<RemoveBgResponse> {
  const res = await authFetch(`${API_BASE}/remove-bg/${imageId}`, {
    method: "POST",
    skipAuthRedirect: true, // Let the caller handle auth errors (demo mode)
  });

  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Background removal failed");
    throw new Error(msg);
  }

  return res.json();
}

export async function getStyles(): Promise<StyleInfo[]> {
  const res = await fetch(`${API_BASE}/styles`);
  if (!res.ok) throw new Error("Failed to fetch styles");
  return res.json();
}

export async function getStylesForCategory(productType: string): Promise<StyleInfo[]> {
  const res = await fetch(`${API_BASE}/styles/${productType}`);
  if (!res.ok) throw new Error("Failed to fetch styles for category");
  return res.json();
}

export async function getProductTypes(): Promise<ProductTypeInfo[]> {
  const res = await fetch(`${API_BASE}/product-types`);
  if (!res.ok) throw new Error("Failed to fetch product types");
  return res.json();
}

export async function getTemplates(productType: string): Promise<SceneTemplate[]> {
  const res = await fetch(`${API_BASE}/templates/${productType}`);
  if (!res.ok) throw new Error("Failed to fetch templates");
  return res.json();
}

export async function startGeneration(params: {
  image_id: string;
  product_type: string;
  remove_bg: boolean;
  style?: string;
  templates?: { template_id: string; custom_prompt?: string }[];
  selected_template_ids?: string[];
}): Promise<GenerateTaskResponse> {
  const res = await authFetch(`${API_BASE}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });

  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Generation failed");
    throw new Error(msg);
  }

  return res.json();
}

export function subscribeToGeneration(
  taskId: string,
  onEvent: (event: SSEEvent) => void,
  onError: (error: Error) => void,
): () => void {
  const MAX_RETRIES = 5;
  const BASE_DELAY = 2000; // 2 seconds
  let retryCount = 0;
  let currentSource: EventSource | null = null;
  let closed = false;

  function connect() {
    if (closed) return;

    // Add token as query param for SSE (EventSource can't set custom headers)
    const token = getToken();
    const tokenParam = token ? `?token=${encodeURIComponent(token)}` : "";
    const eventSource = new EventSource(`${API_BASE}/generate/${taskId}/status${tokenParam}`);
    currentSource = eventSource;

    eventSource.onmessage = (e) => {
      try {
        const data: SSEEvent = JSON.parse(e.data);
        retryCount = 0; // Reset retry count on successful message
        onEvent(data);

        if (data.event === "completed" || data.event === "error") {
          closed = true;
          eventSource.close();
        }
      } catch {
        // ignore parse errors
      }
    };

    eventSource.onerror = () => {
      eventSource.close();
      currentSource = null;

      if (closed) return;

      if (retryCount < MAX_RETRIES) {
        // Exponential backoff: 2s → 4s → 8s → 16s → 32s
        const delay = BASE_DELAY * Math.pow(2, retryCount);
        retryCount++;

        // Fetch latest state via REST before reconnecting SSE
        getResults(taskId)
          .then((result) => {
            if (result.status === "completed" || result.status === "failed" || result.status === "partial") {
              // Task already finished — emit final event
              closed = true;
              onEvent({
                event: "completed",
                task_id: taskId,
                progress: result.progress,
                total: result.total,
                results: result.images,
              });
            } else {
              // Task still running — emit progress and reconnect SSE
              onEvent({
                event: "progress",
                task_id: taskId,
                progress: result.progress,
                total: result.total,
                results: result.images,
              });
              setTimeout(connect, delay);
            }
          })
          .catch(() => {
            // REST fallback also failed — still try reconnecting SSE
            setTimeout(connect, delay);
          });
      } else {
        onError(new Error("SSE connection failed after retries"));
      }
    };
  }

  connect();

  return () => {
    closed = true;
    if (currentSource) {
      currentSource.close();
      currentSource = null;
    }
  };
}

export async function regenerateImage(
  taskId: string,
  templateId: string,
  customPrompt?: string,
): Promise<GeneratedImage> {
  const res = await authFetch(`${API_BASE}/generate/${taskId}/regenerate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ template_id: templateId, custom_prompt: customPrompt }),
  });
  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Regeneration failed");
    throw new Error(msg);
  }
  return res.json();
}

export interface VariantResult {
  variant_index: number;
  url: string | null;
  error?: string;
}

export async function generateVariants(
  taskId: string,
  templateId: string,
): Promise<{ variants: VariantResult[] }> {
  const res = await authFetch(`${API_BASE}/generate/${taskId}/variants/${templateId}`, {
    method: "POST",
  });
  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Variant generation failed");
    throw new Error(msg);
  }
  return res.json();
}

export async function selectVariant(
  taskId: string,
  templateId: string,
  variantIndex: number,
): Promise<GeneratedImage> {
  const res = await authFetch(`${API_BASE}/generate/${taskId}/select-variant`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ template_id: templateId, variant_index: variantIndex }),
  });
  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Variant selection failed");
    throw new Error(msg);
  }
  return res.json();
}

export async function getResults(taskId: string): Promise<GenerateResultResponse> {
  const res = await authFetch(`${API_BASE}/generate/${taskId}/results`);
  if (!res.ok) throw new Error("Failed to fetch results");
  return res.json();
}

export function getDownloadUrl(taskId: string, platform: string = "general"): string {
  return `${API_BASE}/download/${taskId}?platform=${platform}`;
}

export async function compositeGrid(
  taskId: string,
  params: {
    layout?: string;
    image_order?: string[];
    cell_size?: number;
    gap?: number;
    bg_color?: string;
  } = {},
): Promise<Blob> {
  const res = await authFetch(`${API_BASE}/composite/${taskId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });
  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Composite failed");
    throw new Error(msg);
  }
  return res.blob();
}

export async function getApiKeysStatus(): Promise<ApiKeysStatus> {
  const res = await fetch(`${API_BASE}/settings/api-keys`);
  if (!res.ok) throw new Error("Failed to fetch API keys status");
  return res.json();
}

export async function generateCopy(params: {
  product_details: string;
  product_type: string;
  scenes: { name: string; name_en: string; description: string }[];
}): Promise<CopywritingResponse> {
  const res = await authFetch(`${API_BASE}/generate-copy`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });
  if (!res.ok) {
    const msg = await parseErrorResponse(res, "文案生成失敗");
    throw new Error(msg);
  }
  return res.json();
}

export async function saveApiKeys(params: {
  gemini_api_key?: string;
  together_api_key?: string;
}): Promise<ApiKeysStatus> {
  const res = await fetch(`${API_BASE}/settings/api-keys`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });

  if (!res.ok) {
    const msg = await parseErrorResponse(res, "Failed to save API keys");
    throw new Error(msg);
  }

  return res.json();
}

// ---------------------------------------------------------------------------
// History API
// ---------------------------------------------------------------------------

export async function getHistory(page = 1, pageSize = 20): Promise<PaginatedHistory> {
  const res = await authFetch(`${API_BASE}/history?page=${page}&page_size=${pageSize}`);
  if (!res.ok) {
    // If not authenticated, return empty
    if (res.status === 401) {
      return { items: [], total: 0, page: 1, page_size: pageSize };
    }
    throw new Error("Failed to fetch history");
  }
  return res.json();
}

// ---------------------------------------------------------------------------
// Wizard V2 API (mock / placeholder)
// ---------------------------------------------------------------------------

export interface MaterialSample {
  id: string;
  name: string;
  nameEn: string;
  thumbnail: string;
  description: string;
  promptHint: string;
  textureKeywords: string[];
}

export interface SceneTemplateV2 {
  id: string;
  name: string;
  nameEn: string;
  category: "indoor" | "outdoor";
  style: string;
  thumbnail: string;
  description: string;
  prompt: string;
  aspectRatio: string;
  injectionLevel: "none" | "light" | "full";
  lightingTip: string;
  suitableFor: string[];
}

export interface ModelPresetData {
  id: string;
  name: string;
  nameEn: string;
  ethnicity: string;
  thumbnail: string;
  gender: "male" | "female";
  bodyType: string;
  styleDescription: string;
  poseHint: string;
  ageRange: string;
}

export interface AnalyzeProductResult {
  suggestedName: string;
  suggestedCategory: string;
  suggestedMaterial: string;
  suggestedTags: string[];
}

/** AI product analysis - placeholder */
export async function analyzeProduct(_imageId: string): Promise<AnalyzeProductResult> {
  // TODO: connect to real API
  return {
    suggestedName: "",
    suggestedCategory: "",
    suggestedMaterial: "",
    suggestedTags: [],
  };
}

/** Get scene templates for wizard — rich prompt data matching V1 quality */
export async function getSceneTemplates(): Promise<SceneTemplateV2[]> {
  return [
    // === Indoor Scenes ===
    {
      id: "scene-jp-minimal",
      name: "日系极简",
      nameEn: "Japanese Minimal",
      category: "indoor",
      style: "japanese",
      thumbnail: "",
      description: "清新自然的日式简约风格，天然材质与留白美学",
      prompt:
        "Product displayed in a serene Japanese minimalist interior setting. " +
        "Clean tatami or light hinoki wood surface with plenty of negative space. " +
        "Muted earth tones — warm beige, off-white, and soft gray. " +
        "A single ikebana arrangement or ceramic tea bowl as subtle accent. " +
        "Soft natural light streaming through shoji paper screens creating gentle diffused illumination. " +
        "Shot with a 50mm lens at f/4, camera at 30-degree angle for intimate perspective. " +
        "Wabi-sabi aesthetic — the beauty of imperfection and simplicity. " +
        "Color palette inspired by Muji and Kinfolk magazine.",
      aspectRatio: "4:3",
      injectionLevel: "light",
      lightingTip: "自然光透过障子纸的柔和漫射光，色温约 5200K",
      suitableFor: ["家居", "文具", "茶具", "香薰", "餐具"],
    },
    {
      id: "scene-nordic",
      name: "北欧风",
      nameEn: "Nordic Style",
      category: "indoor",
      style: "nordic",
      thumbnail: "",
      description: "温暖木质与白色的北欧美学，Hygge 舒适感",
      prompt:
        "Product placed in a bright Scandinavian-style interior with white-washed walls and warm oak furniture. " +
        "A cozy sheepskin throw draped over a light wood chair nearby. " +
        "Soft wool textiles in muted pastels — dusty pink, sage green, or soft blue. " +
        "Large window with sheer linen curtains letting in abundant Nordic daylight. " +
        "A ceramic mug or small potted eucalyptus as lifestyle accent. " +
        "Even, shadow-free lighting from a large north-facing window, supplemented by a warm-toned table lamp. " +
        "Shot with an 85mm lens at f/3.5 for gentle background separation. " +
        "Hygge atmosphere — warm, inviting, and effortlessly stylish.",
      aspectRatio: "4:3",
      injectionLevel: "light",
      lightingTip: "大面积北向窗户光，配合暖色台灯补光，色温 4800K-5500K",
      suitableFor: ["家居", "织物", "蜡烛", "厨具", "装饰品"],
    },
    {
      id: "scene-kr-cream",
      name: "韩系奶油风",
      nameEn: "Korean Cream",
      category: "indoor",
      style: "korean",
      thumbnail: "",
      description: "柔和奶油色调的韩式风格，甜美温柔",
      prompt:
        "Product in a dreamy Korean cream-tone interior setting. " +
        "Soft butter yellow walls, ivory linen tablecloth, and warm beige wooden surfaces. " +
        "Delicate dried flower arrangement in a ceramic vase as background accent. " +
        "A croissant on a white plate or a glass of oat milk latte to set the cafe mood. " +
        "Warm, enveloping light with almost no harsh shadows — like being inside a soft cloud. " +
        "Natural window light from the left, diffused through sheer curtains, creating a glowing cream atmosphere. " +
        "Shot with a 50mm lens at f/2.8, slight overexposure for an airy, ethereal feel. " +
        "Korean Instagram aesthetic — soft, feminine, and lifestyle-driven.",
      aspectRatio: "1:1",
      injectionLevel: "light",
      lightingTip: "暖调窗光配合柔光反射板，微过曝 +0.5EV，色温 4500K",
      suitableFor: ["美妆", "饰品", "手机壳", "文具", "甜品"],
    },
    {
      id: "scene-modern-loft",
      name: "现代LOFT",
      nameEn: "Modern Loft",
      category: "indoor",
      style: "modern",
      thumbnail: "",
      description: "工业风格的现代阁楼空间，裸露砖墙与金属元素",
      prompt:
        "Product displayed in a modern industrial loft space. " +
        "Exposed red brick wall as backdrop, polished concrete floor, and black iron shelving units. " +
        "Vintage Edison bulb string lights adding warm amber accents. " +
        "Dark leather sofa or distressed wood table nearby for context. " +
        "Dramatic directional lighting: strong key light from a large factory-style window creating bold shadows. " +
        "Fill light from ambient bounce off the concrete floor. " +
        "Shot with a 35mm lens at f/5.6 for wide environmental context showing the loft architecture. " +
        "Contemporary urban sophistication with raw industrial textures.",
      aspectRatio: "4:3",
      injectionLevel: "light",
      lightingTip: "大型工厂窗户侧光，形成明显明暗对比，色温 5000K-5500K",
      suitableFor: ["3C数码", "皮具", "手表", "音箱", "运动装备"],
    },
    {
      id: "scene-luxury-marble",
      name: "奢华大理石",
      nameEn: "Luxury Marble",
      category: "indoor",
      style: "luxury",
      thumbnail: "",
      description: "大理石质感的高端展示台面，金色点缀",
      prompt:
        "Product elegantly placed on a luxurious Calacatta marble surface with dramatic gray and gold veining. " +
        "Brushed gold accents — a small tray, geometric sculpture, or jewelry stand nearby. " +
        "Deep emerald green velvet or navy blue silk fabric draped artfully as a color accent. " +
        "Soft overhead studio lighting with a large parabolic reflector creating luminous, even illumination. " +
        "Subtle specular highlights on the marble surface convey the premium polished finish. " +
        "Shot with an 85mm lens at f/4, camera at 25-degree angle for an elevated luxury perspective. " +
        "Color grading with slightly cool whites and warm gold tones. " +
        "Five-star hotel lobby aesthetic — opulent, refined, and aspirational.",
      aspectRatio: "1:1",
      injectionLevel: "light",
      lightingTip: "顶部柔光箱 + 侧面补光，突出大理石光泽与金属反射",
      suitableFor: ["珠宝", "手表", "香水", "高端护肤", "奢侈品"],
    },
    {
      id: "scene-warm-studio",
      name: "暖光棚拍",
      nameEn: "Warm Studio",
      category: "indoor",
      style: "studio",
      thumbnail: "",
      description: "温暖灯光的专业摄影棚，均匀柔光",
      prompt:
        "Product centered on a clean seamless studio backdrop in warm off-white. " +
        "Professional e-commerce photography setup with dual strip softboxes at 45 degrees for even illumination. " +
        "A subtle warm color temperature (4800K) giving the image a welcoming, inviting feel. " +
        "Gentle gradient shadow beneath the product for depth and grounding. " +
        "Product occupies 80% of frame, perfectly centered with balanced negative space. " +
        "Shot with a 70mm lens at f/8 for maximum product sharpness edge-to-edge. " +
        "Camera at waist height for a natural, eye-level perspective. " +
        "High-end commercial product photography suitable for hero image placement.",
      aspectRatio: "1:1",
      injectionLevel: "none",
      lightingTip: "双条形柔光箱 45 度对称布光，色温 4800K 暖调",
      suitableFor: ["全品类", "主图", "白底图", "产品展示"],
    },
    {
      id: "scene-white-bg",
      name: "纯白主图",
      nameEn: "Pure White Background",
      category: "indoor",
      style: "white",
      thumbnail: "",
      description: "纯白背景电商标准主图，突出产品本身",
      prompt:
        "Product displayed on a pure white (#FFFFFF) background. " +
        "Professional e-commerce hero image photography. " +
        "The item is perfectly centered showing its most attractive angle. " +
        "Crisp studio lighting with dual strip softboxes at 45 degrees for even, shadow-free illumination. " +
        "Product occupies approximately 85% of the frame. " +
        "Shot overhead at optimal angle with a 50mm lens at f/8 for maximum sharpness. " +
        "Pure white seamless background with no visible horizon line. " +
        "Ultra-clean, commercial quality photography meeting marketplace standards.",
      aspectRatio: "1:1",
      injectionLevel: "none",
      lightingTip: "均匀柔光确保纯白背景无色偏，双侧 45 度布光",
      suitableFor: ["全品类", "电商主图", "平台标准图"],
    },
    {
      id: "scene-detail-macro",
      name: "细节微距",
      nameEn: "Detail Macro",
      category: "indoor",
      style: "macro",
      thumbnail: "",
      description: "材质纹理与工艺细节的微距特写",
      prompt:
        "Extreme close-up macro photography of product details showing material texture and craftsmanship. " +
        "Multiple detail zones: surface finish, stitching or seam quality, hardware or embellishment, edge finishing. " +
        "Shot with a 100mm macro lens at f/5.6, sharp focus revealing material quality at high magnification. " +
        "Directional side lighting from a focused spot at a low 15-degree angle to emphasize surface texture. " +
        "A secondary overhead diffused fill prevents excessive contrast while maintaining dimensionality. " +
        "The fabric/material fills the entire frame. " +
        "Professional product detail photography that communicates quality and hand-feel to online buyers.",
      aspectRatio: "1:1",
      injectionLevel: "light",
      lightingTip: "低角度侧光（15°）突出纹理，顶部柔光补光防止过暗",
      suitableFor: ["全品类", "面料展示", "工艺细节", "材质特写"],
    },
    // === Outdoor Scenes ===
    {
      id: "scene-street",
      name: "城市街景",
      nameEn: "Urban Street",
      category: "outdoor",
      style: "urban",
      thumbnail: "",
      description: "时尚都市街头场景，现代建筑与人行道",
      prompt:
        "Product photographed in a stylish urban street setting. " +
        "Clean modern city architecture as backdrop — glass storefronts, minimalist concrete facades, or a trendy neighborhood. " +
        "The sidewalk is clean, possibly wet from recent rain for reflective appeal. " +
        "Morning golden hour light filtering between buildings creating long warm shadows. " +
        "Slight motion blur of passing pedestrians adds metropolitan energy. " +
        "Shot with an 85mm lens at f/2.8 for shallow depth of field isolating the product against blurred city life. " +
        "Camera at eye level for a relatable street-style perspective. " +
        "Fashion editorial street photography vibe — Highsnobiety or Hypebeast aesthetic.",
      aspectRatio: "3:4",
      injectionLevel: "full",
      lightingTip: "清晨或傍晚侧逆光，利用建筑间隙形成戏剧性光影",
      suitableFor: ["服装", "鞋靴", "包袋", "手表", "太阳镜"],
    },
    {
      id: "scene-camping",
      name: "露营野趣",
      nameEn: "Camping Adventure",
      category: "outdoor",
      style: "outdoor",
      thumbnail: "",
      description: "户外露营自然场景，帐篷与森林",
      prompt:
        "Product placed in an outdoor camping scene surrounded by nature. " +
        "A stylish canvas bell tent or modern camping setup as background. " +
        "Pine trees and dappled forest light creating a warm, adventurous atmosphere. " +
        "A campfire with soft warm glow, enamel mugs, and a weathered wood log table nearby. " +
        "Morning mist or golden afternoon light filtering through the tree canopy. " +
        "Shot with a 35mm lens at f/4 for wide environmental context. " +
        "Earthy color palette: forest green, warm brown, burnt orange, and natural khaki. " +
        "Aspirational outdoor lifestyle photography — REI or Snow Peak catalog aesthetic.",
      aspectRatio: "4:3",
      injectionLevel: "light",
      lightingTip: "树冠透射的斑驳光影，暖色调约 4000K-4500K",
      suitableFor: ["户外装备", "保温杯", "背包", "运动服饰", "工具"],
    },
    {
      id: "scene-beach",
      name: "海滨度假",
      nameEn: "Beachside Resort",
      category: "outdoor",
      style: "beach",
      thumbnail: "",
      description: "清爽海边度假风格，沙滩与海浪",
      prompt:
        "Product displayed in a beautiful beachside setting with fine white sand and turquoise ocean water. " +
        "A rattan beach chair or white linen towel as a styling surface. " +
        "Tropical green palm fronds casting dappled shadows. " +
        "A straw hat, coral seashell, or coconut drink as lifestyle accents. " +
        "Bright, high-key tropical sunlight with a slight golden warmth. " +
        "Shot with a 50mm lens at f/4, camera at 30-degree angle. " +
        "The ocean sparkles with golden sun reflections in the soft-focused background. " +
        "Maldives resort or Tulum beach house aesthetic — relaxed, luxurious, and sun-kissed.",
      aspectRatio: "4:3",
      injectionLevel: "light",
      lightingTip: "正午侧光 + 沙滩自然反射补光，高色温 5800K-6200K",
      suitableFor: ["泳装", "太阳镜", "防晒", "度假服饰", "沙滩配件"],
    },
    {
      id: "scene-garden",
      name: "花园庭院",
      nameEn: "Botanical Garden",
      category: "outdoor",
      style: "garden",
      thumbnail: "",
      description: "绿意盎然的花园场景，鲜花与藤蔓",
      prompt:
        "Product placed in a lush botanical garden setting with abundant greenery. " +
        "Flowering bushes — roses, hydrangeas, or lavender — creating a romantic backdrop. " +
        "A weathered stone bench or wrought iron garden table as display surface. " +
        "Climbing ivy or wisteria vine framing the scene from above. " +
        "Soft dappled sunlight filtering through the garden canopy creating painterly light patterns. " +
        "Shot with an 85mm lens at f/2.8 for dreamy background bokeh filled with green and floral colors. " +
        "Gentle breeze captured through slightly swaying flowers. " +
        "English cottage garden aesthetic — romantic, verdant, and timeless.",
      aspectRatio: "4:3",
      injectionLevel: "light",
      lightingTip: "树荫下的漫射光 + 斑驳光斑，色温约 5500K",
      suitableFor: ["香水", "花卉礼品", "园艺工具", "帽子", "丝巾"],
    },
    {
      id: "scene-cafe",
      name: "文艺咖啡厅",
      nameEn: "Artisan Cafe",
      category: "outdoor",
      style: "cafe",
      thumbnail: "",
      description: "文艺咖啡厅露天座位，木桌与拿铁拉花",
      prompt:
        "Product on a rustic wooden cafe table at an artisan coffee shop's outdoor terrace. " +
        "A perfect latte art cappuccino in a ceramic cup and a fresh croissant on a white plate as lifestyle accents. " +
        "The cafe facade features dark green paint, chalkboard menu signs, and hanging potted ferns. " +
        "Warm morning sunlight casting long soft shadows across the table. " +
        "Bokeh lights from string bulbs above the terrace visible in the background. " +
        "Shot with a 50mm lens at f/2.8 for atmospheric depth. " +
        "Camera slightly above eye level looking down at the table arrangement. " +
        "Parisian cafe or Melbourne brunch culture aesthetic — intellectual, stylish, and relaxed.",
      aspectRatio: "1:1",
      injectionLevel: "light",
      lightingTip: "户外自然光 + 暖色调氛围灯补光，色温 4500K",
      suitableFor: ["手机壳", "笔记本", "钱包", "眼镜", "手表"],
    },
    {
      id: "scene-rooftop",
      name: "天台夕阳",
      nameEn: "Rooftop Golden Hour",
      category: "outdoor",
      style: "rooftop",
      thumbnail: "",
      description: "城市天台日落场景，金色天际线",
      prompt:
        "Product photographed on a chic urban rooftop during golden hour. " +
        "City skyline softly blurred in the background with warm sunset colors — amber, coral, and deep purple. " +
        "Modern outdoor lounge furniture, string lights, and potted olive trees as scene elements. " +
        "The warm golden-hour sunlight backlights the product creating a luminous halo and rim light effect. " +
        "A reflector from the front fills in the product shadow side with warm light. " +
        "Shot with a 70mm lens at f/3.5 for cinematic background compression. " +
        "Low camera angle slightly looking up for a powerful, aspirational composition. " +
        "High-end rooftop bar aesthetic — sophisticated, warm, and metropolitan.",
      aspectRatio: "16:9",
      injectionLevel: "light",
      lightingTip: "黄金时刻逆光 + 正面反射板补光，色温 3200K-3800K",
      suitableFor: ["酒具", "音箱", "香薰", "服饰", "珠宝"],
    },
    {
      id: "scene-mountain",
      name: "山野徒步",
      nameEn: "Mountain Trail",
      category: "outdoor",
      style: "mountain",
      thumbnail: "",
      description: "苍翠山间步道，户外探险氛围",
      prompt:
        "Product placed in a scenic mountain trail setting with panoramic valley views. " +
        "Rugged rock formations and alpine wildflowers frame the scene. " +
        "Early morning mist rising from the valley below, crisp mountain air feeling. " +
        "A weathered wooden trail marker or cairn stones nearby for authentic trail context. " +
        "Bright directional sunlight from the east with long shadows across the terrain. " +
        "Shot with a 24mm wide-angle lens at f/8 for deep focus capturing both product and expansive landscape. " +
        "Epic, sweeping composition that conveys adventure and freedom. " +
        "National Geographic or Patagonia campaign aesthetic — wild, authentic, and inspiring.",
      aspectRatio: "16:9",
      injectionLevel: "light",
      lightingTip: "清晨强侧光，山谷雾气自然漫射，色温 5500K-6000K",
      suitableFor: ["登山装备", "户外服饰", "水壶", "背包", "运动鞋"],
    },
    {
      id: "scene-night-neon",
      name: "霓虹夜景",
      nameEn: "Neon Night City",
      category: "outdoor",
      style: "neon",
      thumbnail: "",
      description: "赛博朋克霓虹灯光下的夜间都市",
      prompt:
        "Product photographed in a vibrant neon-lit urban nightscape. " +
        "Colorful neon signs in pink, cyan, and purple reflecting off wet asphalt streets. " +
        "Cyberpunk-inspired cityscape with glowing shop signs and LED strips. " +
        "Light trails from passing vehicles add dynamic energy. " +
        "Mixed color temperature: warm incandescent from shops and cool neon from signs. " +
        "Shot with a 35mm lens at f/2.0 for dramatic shallow depth of field with neon bokeh. " +
        "Low camera angle for a cinematic, immersive street-level perspective. " +
        "Blade Runner meets Tokyo Kabukicho aesthetic — electric, moody, and futuristic.",
      aspectRatio: "3:4",
      injectionLevel: "light",
      lightingTip: "混合色温霓虹光源，低角度拍摄突出光影反射",
      suitableFor: ["潮牌服饰", "电子产品", "运动鞋", "配饰", "手机壳"],
    },
  ];
}

/** Get material samples for wizard — rich data with prompt hints */
export async function getMaterialSamples(): Promise<MaterialSample[]> {
  return [
    {
      id: "mat-leather",
      name: "真皮",
      nameEn: "Genuine Leather",
      thumbnail: "",
      description: "意大利植鞣牛皮，触感温润，随时间使用产生独特光泽",
      promptHint: "rich genuine leather texture with natural grain patterns, warm brown tones, subtle sheen from oils and age",
      textureKeywords: ["grain", "patina", "supple", "warm"],
    },
    {
      id: "mat-canvas",
      name: "帆布",
      nameEn: "Heavy Canvas",
      thumbnail: "",
      description: "16 安士重磅帆布，经典耐用，石磨水洗做旧质感",
      promptHint: "heavy-duty washed canvas fabric with visible woven texture, slightly faded and worn for vintage character",
      textureKeywords: ["woven", "rugged", "matte", "durable"],
    },
    {
      id: "mat-metal",
      name: "精铸金属",
      nameEn: "Cast Metal Alloy",
      thumbnail: "",
      description: "锌合金精密压铸，电镀拉丝表面处理",
      promptHint: "brushed metal surface with fine directional grain lines, cool silver or gunmetal tone, subtle specular highlights",
      textureKeywords: ["brushed", "reflective", "cool-toned", "industrial"],
    },
    {
      id: "mat-ceramic",
      name: "手工陶瓷",
      nameEn: "Handmade Ceramic",
      thumbnail: "",
      description: "高温柴烧窑变釉面，每件独一无二",
      promptHint: "handcrafted ceramic with organic kiln-fired glaze variations, subtle crazing and depth in the glaze surface",
      textureKeywords: ["glaze", "organic", "earthy", "handmade"],
    },
    {
      id: "mat-wood",
      name: "实木",
      nameEn: "Solid Hardwood",
      thumbnail: "",
      description: "北美黑胡桃木，纹理细致，色泽沉稳温润",
      promptHint: "rich walnut wood grain with flowing dark and light streaks, warm chocolate tones, smooth satin finish",
      textureKeywords: ["grain", "warm", "natural", "satin"],
    },
    {
      id: "mat-glass",
      name: "硼硅玻璃",
      nameEn: "Borosilicate Glass",
      thumbnail: "",
      description: "高硼硅耐热玻璃，晶莹剔透，耐温差 150°C",
      promptHint: "crystal-clear borosilicate glass with light refracting through its transparent body, subtle caustic light patterns",
      textureKeywords: ["transparent", "refractive", "pristine", "smooth"],
    },
    {
      id: "mat-silk",
      name: "真丝",
      nameEn: "Mulberry Silk",
      thumbnail: "",
      description: "100% 桑蚕丝，轻若无物，如水般垂坠",
      promptHint: "luxurious mulberry silk with fluid drape and luminous sheen, light dancing across its surface in waves",
      textureKeywords: ["lustrous", "fluid", "delicate", "luminous"],
    },
    {
      id: "mat-bamboo",
      name: "竹纤维",
      nameEn: "Bamboo Fiber",
      thumbnail: "",
      description: "天然竹纤维，抑菌透气，柔软亲肤",
      promptHint: "natural bamboo fiber textile with soft matte surface, light and breathable weave structure visible at close range",
      textureKeywords: ["natural", "soft", "breathable", "eco"],
    },
    {
      id: "mat-recycled-nylon",
      name: "再生尼龙",
      nameEn: "Recycled Nylon",
      thumbnail: "",
      description: "ECONYL 再生尼龙，防水耐磨，环保永续",
      promptHint: "technical recycled nylon fabric with tight ripstop weave, water beading on its surface, matte military-grade finish",
      textureKeywords: ["technical", "waterproof", "durable", "eco"],
    },
    {
      id: "mat-stainless",
      name: "不锈钢",
      nameEn: "Stainless Steel 304",
      thumbnail: "",
      description: "食品级 304 不锈钢，镜面抛光，耐腐蚀易清洁",
      promptHint: "mirror-polished stainless steel surface with perfect reflections and clean metallic sheen, fingerprint-free finish",
      textureKeywords: ["mirror", "reflective", "hygienic", "cool"],
    },
    {
      id: "mat-linen",
      name: "亚麻",
      nameEn: "French Linen",
      thumbnail: "",
      description: "法国诺曼底亚麻，自然褶皱纹理，透气舒适",
      promptHint: "natural French linen with characteristic slubby texture, soft wrinkles and creases adding organic character",
      textureKeywords: ["textured", "natural", "breathable", "rustic"],
    },
    {
      id: "mat-resin",
      name: "环氧树脂",
      nameEn: "Epoxy Resin",
      thumbnail: "",
      description: "透明环氧树脂，可封装花朵或颜料，晶莹如宝石",
      promptHint: "crystal-clear epoxy resin with embedded elements visible inside, glass-like clarity with smooth polished surface",
      textureKeywords: ["transparent", "glossy", "artistic", "deep"],
    },
  ];
}

/** Get model presets for wizard — detailed model descriptions */
export async function getModelPresets(): Promise<ModelPresetData[]> {
  return [
    {
      id: "model-ea-f-01",
      name: "清新甜美",
      nameEn: "Fresh & Sweet",
      ethnicity: "east-asian",
      thumbnail: "",
      gender: "female",
      bodyType: "纤细",
      styleDescription: "韩系清新甜美风格，邻家女孩气质，自然妆容，微卷长发",
      poseHint: "Natural standing pose with soft smile, one hand slightly touching hair, relaxed and approachable",
      ageRange: "20-25",
    },
    {
      id: "model-ea-f-02",
      name: "知性优雅",
      nameEn: "Elegant & Refined",
      ethnicity: "east-asian",
      thumbnail: "",
      gender: "female",
      bodyType: "标准",
      styleDescription: "日系知性优雅风格，成熟质感，低马尾或齐肩短发，精致淡妆",
      poseHint: "Confident three-quarter pose with arms at sides, poised expression, elegant posture with chin slightly lifted",
      ageRange: "28-35",
    },
    {
      id: "model-ea-m-01",
      name: "阳光运动",
      nameEn: "Athletic & Bright",
      ethnicity: "east-asian",
      thumbnail: "",
      gender: "male",
      bodyType: "健美",
      styleDescription: "阳光运动型男，短发干净利落，健康小麦肤色，自信笑容",
      poseHint: "Dynamic casual stance with hands in pockets or arms crossed, confident broad smile, athletic energy",
      ageRange: "25-32",
    },
    {
      id: "model-ea-m-02",
      name: "文艺书生",
      nameEn: "Literary & Gentle",
      ethnicity: "east-asian",
      thumbnail: "",
      gender: "male",
      bodyType: "纤细",
      styleDescription: "文艺书生气质，中分微长发，白皙肤色，金丝眼镜",
      poseHint: "Thoughtful pose looking slightly away from camera, one hand adjusting glasses, intellectual and calm demeanor",
      ageRange: "22-30",
    },
    {
      id: "model-eu-f-01",
      name: "时尚超模",
      nameEn: "High Fashion",
      ethnicity: "european",
      thumbnail: "",
      gender: "female",
      bodyType: "高挑",
      styleDescription: "欧美高级时装风格，高颧骨轮廓分明，金棕长发，高冷气场",
      poseHint: "Editorial fashion pose with strong angles, one hip slightly forward, piercing gaze, editorial model confidence",
      ageRange: "22-30",
    },
    {
      id: "model-eu-m-01",
      name: "都市雅痞",
      nameEn: "Urban Sophisticate",
      ethnicity: "european",
      thumbnail: "",
      gender: "male",
      bodyType: "标准",
      styleDescription: "都市雅痞风格，轮廓清晰，深色短发梳理整齐，轻度胡须",
      poseHint: "Relaxed standing pose with jacket over shoulder or leaning against wall, charismatic half-smile",
      ageRange: "30-38",
    },
    {
      id: "model-sa-f-01",
      name: "异域风情",
      nameEn: "Exotic Beauty",
      ethnicity: "south-asian",
      thumbnail: "",
      gender: "female",
      bodyType: "标准",
      styleDescription: "异域风情美感，深色大波浪长发，蜜色皮肤，明亮大眼",
      poseHint: "Graceful pose with flowing hair movement, warm genuine smile, vibrant and energetic expression",
      ageRange: "23-30",
    },
    {
      id: "model-mixed-f-01",
      name: "混血时尚",
      nameEn: "Mixed Heritage Chic",
      ethnicity: "east-asian",
      thumbnail: "",
      gender: "female",
      bodyType: "标准",
      styleDescription: "混血模特气质，融合东西方特征，五官精致立体，短发干练",
      poseHint: "Modern and edgy pose, hands on hips or one hand behind head, strong eye contact, contemporary fashion attitude",
      ageRange: "22-28",
    },
  ];
}

// ---------------------------------------------------------------------------
// Storyboard V2 API (mock implementations)
// ---------------------------------------------------------------------------

export interface StoryboardPreviewRequest {
  image_id: string;
  product_type: string;
  remove_bg: boolean;
  style?: string;
  ambient?: string;
  cells: { index: number; image_type: string }[];
}

export interface StoryboardPreviewResponse {
  task_id: string;
  previews: { index: number; preview_url: string }[];
}

export interface ConfirmGenerationRequest {
  task_id: string;
  ambient?: string;
  cells: { index: number; image_type: string }[];
}

export interface ConfirmGenerationResponse {
  task_id: string;
  status: string;
  total: number;
}

export interface RegenerateSingleRequest {
  seed?: number;
  style?: string;
  scene?: string;
  image_type?: string;
}

export interface InpaintRequest {
  mask_data: string; // base64 encoded mask
  prompt?: string;
}

export interface GenerateAdditionalRequest {
  image_type: string;
  count: number;
  angle?: string;
  lighting?: string;
}

export interface GenerateAdditionalResponse {
  task_id: string;
  images: GeneratedImage[];
}

/** Generate low-res preview sketches for the 9-grid storyboard */
export async function generatePreview(
  params: StoryboardPreviewRequest,
): Promise<StoryboardPreviewResponse> {
  // Mock: simulate preview generation
  await new Promise((r) => setTimeout(r, 800));

  // Map image types to seeded picsum URLs for realistic previews
  const PREVIEW_SEEDS: Record<string, string> = {
    white_bg: "preview_whitebg",
    scene: "preview_scene",
    detail: "preview_detail",
    material: "preview_material",
    flat_lay: "preview_flatlay",
    model: "preview_model",
  };

  const previews = params.cells.map((cell, idx) => ({
    index: cell.index,
    preview_url: `https://picsum.photos/seed/${PREVIEW_SEEDS[cell.image_type] || "preview_misc"}_${idx}/400/400`,
  }));
  return { task_id: `preview-${Date.now()}`, previews };
}

/** Confirm storyboard and start high-res rendering */
export async function confirmGeneration(
  params: ConfirmGenerationRequest,
): Promise<ConfirmGenerationResponse> {
  // Mock: simulate generation start
  await new Promise((r) => setTimeout(r, 500));
  return {
    task_id: params.task_id || `gen-${Date.now()}`,
    status: "running",
    total: params.cells.length,
  };
}

/** Regenerate a single image with optional adjustments */
export async function regenerateSingle(
  taskId: string,
  templateId: string,
  options?: RegenerateSingleRequest,
): Promise<GeneratedImage> {
  // Mock: simulate regeneration
  await new Promise((r) => setTimeout(r, 1500));
  return {
    template_id: templateId,
    template_name: options?.image_type || "重生成图",
    status: "completed",
    url: `https://picsum.photos/seed/regen_${templateId}_${Date.now()}/800/800`,
    error: null,
  };
}

/** Inpaint (partial repaint) a specific region of an image */
export async function inpaintImage(
  taskId: string,
  imageId: string,
  maskData: InpaintRequest,
): Promise<GeneratedImage> {
  // Mock: simulate inpainting
  await new Promise((r) => setTimeout(r, 2000));
  return {
    template_id: imageId,
    template_name: "修复图",
    status: "completed",
    url: `https://picsum.photos/seed/inpaint_${imageId}_${Date.now()}/800/800`,
    error: null,
  };
}

/** Generate additional images of a specific type */
export async function generateAdditional(
  taskId: string,
  params: GenerateAdditionalRequest,
): Promise<GenerateAdditionalResponse> {
  // Mock: simulate additional generation
  await new Promise((r) => setTimeout(r, 1200));
  const ts = Date.now();
  const images: GeneratedImage[] = Array.from(
    { length: params.count },
    (_, i) => ({
      template_id: `additional-${ts}-${i}`,
      template_name: `${params.image_type} #${i + 1}`,
      status: "completed" as const,
      url: `https://picsum.photos/seed/additional_${params.image_type}_${i}_${ts}/800/800`,
      error: null,
    }),
  );
  return { task_id: taskId, images };
}

// ---------------------------------------------------------------------------
// Detail Layout - Marketing Copywriting (mock)
// ---------------------------------------------------------------------------

export interface CopywritingGenerateParams {
  productName: string;
  productType: string;
  features?: string[];
}

export interface MarketingCopy {
  headline: string;
  subheadline: string;
  sellingPoints: string[];
  callToAction: string;
}

export async function generateCopywriting(
  params: CopywritingGenerateParams,
): Promise<MarketingCopy> {
  // Mock response - will connect to real API later
  await new Promise((r) => setTimeout(r, 1000));
  return {
    headline: `${params.productName} — 質感生活的首選`,
    subheadline: "高品質工藝，讓每一天都充滿儀式感",
    sellingPoints: [
      "嚴選頂級材質，觸感細膩溫潤",
      "極致 CP 值，高級感不必花大錢",
      "簡約設計百搭日常，質感升級必買理由",
    ],
    callToAction: "立即選購，感受生活的美好",
  };
}

// ---------------------------------------------------------------------------
// Multi-platform Export (mock)
// ---------------------------------------------------------------------------

export interface PlatformExportParams {
  taskId: string;
  platforms: string[];
  upscale4K?: boolean;
}

export async function exportForPlatform(
  params: PlatformExportParams,
): Promise<{ downloadUrl: string }> {
  // Mock - will use real download endpoint later
  await new Promise((r) => setTimeout(r, 800));
  return {
    downloadUrl: getDownloadUrl(params.taskId, "general"),
  };
}

// ---------------------------------------------------------------------------
// 4K Upscale (stub)
// ---------------------------------------------------------------------------

export async function upscale4K(
  imageId: string,
): Promise<{ url: string; status: string }> {
  void imageId;
  return { url: "", status: "not_implemented" };
}

// ---------------------------------------------------------------------------
// AI Outpaint to 9:16 (stub)
// ---------------------------------------------------------------------------

export async function outpaintImage(
  imageId: string,
  targetRatio: string,
): Promise<{ url: string; status: string }> {
  void imageId;
  void targetRatio;
  return { url: "", status: "not_implemented" };
}
