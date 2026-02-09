export interface UploadResponse {
  image_id: string;
  filename: string;
  url: string;
}

export interface RemoveBgResponse {
  image_id: string;
  original_url: string;
  removed_bg_url: string;
}

export interface SubCategoryInfo {
  id: string;
  name: string;
}

export interface ProductTypeInfo {
  id: string;
  name: string;
  name_en: string;
  icon: string;
  template_count: number;
  sub_categories: SubCategoryInfo[];
}

export interface SceneTemplate {
  id: string;
  name: string;
  name_en: string;
  product_type: string;
  prompt: string;
  description: string;
  aspect_ratio: string;
  recommended_provider: string;
  injection_level: "none" | "light" | "full";
  sub_category: string;
  sub_category_name: string;
}

export interface StyleInfo {
  id: string;
  name: string;
  name_en: string;
  description: string;
  icon: string;
  preview_color: string;
}

export interface GenerateTaskResponse {
  task_id: string;
  status: string;
  total: number;
  credits_charged?: number;
  credits_remaining?: number;
}

// --- History ---

export interface HistoryItem {
  job_id: string;
  product_type: string;
  style: string | null;
  status: string;
  total_images: number;
  completed_images: number;
  credits_charged: number;
  created_at: string;
  first_image_url: string | null;
}

export interface PaginatedHistory {
  items: HistoryItem[];
  total: number;
  page: number;
  page_size: number;
}

export type ImageStatus = "pending" | "generating" | "completed" | "failed";

export interface GeneratedImage {
  template_id: string;
  template_name: string;
  status: ImageStatus;
  url: string | null;
  error: string | null;
}

export interface GenerateResultResponse {
  task_id: string;
  status: string;
  progress: number;
  total: number;
  images: GeneratedImage[];
}

export interface SSEEvent {
  event: string;
  task_id: string;
  progress?: number;
  total?: number;
  status?: string;
  results?: GeneratedImage[];
}

export interface PlatformSpec {
  name: string;
  width: number;
  height: number;
}

export interface ApiKeysStatus {
  gemini_configured: boolean;
  together_configured: boolean;
  gemini_key_preview: string;
  together_key_preview: string;
}

// --- Copywriting ---

export interface CopyItem {
  scene_index: number;
  title: string;
  subtitle: string;
  description: string;
  hashtags: string[];
}

export interface CopywritingResponse {
  copies: CopyItem[];
  raw?: string;
}

// --- Auth ---

export interface AuthUser {
  user_id: string;
  email: string;
  display_name: string;
  credits: number;
}

export interface AuthResponse extends AuthUser {
  token: string;
}

export interface CreditTransaction {
  id: number;
  amount: number;
  balance_after: number;
  description: string;
  job_id: string | null;
  created_at: string;
}
