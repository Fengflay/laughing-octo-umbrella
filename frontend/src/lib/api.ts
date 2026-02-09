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
async function authFetch(url: string, options: RequestInit = {}): Promise<Response> {
  const headers = {
    ...authHeaders(),
    ...(options.headers || {}),
  };

  const res = await fetch(url, { ...options, headers });

  // Auto-clear auth on 401 (token expired/invalid)
  if (res.status === 401) {
    clearAuth();
    // Only redirect if we're in the browser and not already on auth pages
    if (typeof window !== "undefined" && !window.location.pathname.startsWith("/login") && !window.location.pathname.startsWith("/register")) {
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
