"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { isLoggedIn } from "@/lib/auth";
import { getHistory } from "@/lib/api";
import type { HistoryItem } from "@/types";

// Legacy localStorage-based history (kept for migration / fallback)
export interface HistoryEntry {
  taskId: string;
  productType: string;
  style?: string;
  timestamp: number;
  imageCount: number;
  firstImageUrl?: string;
}

const HISTORY_KEY = "ecom-gen-history";
const MAX_HISTORY = 20;

/** Save a generation entry to localStorage history (still used during generation). */
export function saveToHistory(entry: HistoryEntry) {
  try {
    const existing = getLocalHistory();
    const filtered = existing.filter((e) => e.taskId !== entry.taskId);
    filtered.unshift(entry);
    const trimmed = filtered.slice(0, MAX_HISTORY);
    localStorage.setItem(HISTORY_KEY, JSON.stringify(trimmed));
  } catch {
    // ignore
  }
}

function getLocalHistory(): HistoryEntry[] {
  try {
    const raw = localStorage.getItem(HISTORY_KEY);
    if (!raw) return [];
    return JSON.parse(raw) as HistoryEntry[];
  } catch {
    return [];
  }
}

export function clearHistory() {
  try {
    localStorage.removeItem(HISTORY_KEY);
  } catch {
    // ignore
  }
}

// Product type display names map
const PRODUCT_TYPE_NAMES: Record<string, string> = {
  bags: "包包",
  jewelry: "飾品",
  clothing: "服飾",
  shoes: "鞋子",
  electronics: "3C 電子",
  beauty: "美妝",
  home: "居家",
  toys: "玩具",
  sports: "運動",
  food: "食品",
  stationery: "文具",
  pets: "寵物",
  automotive: "汽車",
  phones: "手機",
  travel: "旅行",
  fashion_acc: "配飾",
  kitchenware: "廚房",
  health: "保健",
  hobbies: "興趣",
  motorcycle: "機車",
};

// Unified display item type
interface DisplayEntry {
  id: string;
  productType: string;
  imageCount: number;
  firstImageUrl?: string | null;
  timestamp: number;
  source: "api" | "local";
}

export default function HistoryPanel() {
  const router = useRouter();
  const [entries, setEntries] = useState<DisplayEntry[]>([]);
  const [showClearConfirm, setShowClearConfirm] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      // If logged in, fetch from server API
      if (isLoggedIn()) {
        try {
          const result = await getHistory(1, 20);
          if (cancelled) return;
          const apiEntries: DisplayEntry[] = result.items.map((item: HistoryItem) => ({
            id: item.job_id,
            productType: item.product_type,
            imageCount: item.completed_images,
            firstImageUrl: item.first_image_url,
            timestamp: new Date(item.created_at).getTime(),
            source: "api" as const,
          }));
          setEntries(apiEntries);
        } catch {
          // Fallback to localStorage on API failure
          if (!cancelled) {
            const local = getLocalHistory();
            setEntries(
              local.map((e) => ({
                id: e.taskId,
                productType: e.productType,
                imageCount: e.imageCount,
                firstImageUrl: e.firstImageUrl,
                timestamp: e.timestamp,
                source: "local" as const,
              })),
            );
          }
        }
      } else {
        // Not logged in → use localStorage
        const local = getLocalHistory();
        setEntries(
          local.map((e) => ({
            id: e.taskId,
            productType: e.productType,
            imageCount: e.imageCount,
            firstImageUrl: e.firstImageUrl,
            timestamp: e.timestamp,
            source: "local" as const,
          })),
        );
      }
      if (!cancelled) setLoading(false);
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  if (loading) return null;
  if (entries.length === 0) return null;

  const handleNavigate = (id: string) => {
    router.push(`/generate?task_id=${id}`);
  };

  const handleClear = () => {
    clearHistory();
    setEntries([]);
    setShowClearConfirm(false);
  };

  const formatTime = (ts: number) => {
    const d = new Date(ts);
    const now = new Date();
    const diffMs = now.getTime() - d.getTime();
    const diffMins = Math.floor(diffMs / 60000);
    if (diffMins < 1) return "剛剛";
    if (diffMins < 60) return `${diffMins} 分鐘前`;
    const diffHours = Math.floor(diffMins / 60);
    if (diffHours < 24) return `${diffHours} 小時前`;
    const diffDays = Math.floor(diffHours / 24);
    if (diffDays < 7) return `${diffDays} 天前`;
    return `${d.getMonth() + 1}/${d.getDate()}`;
  };

  // Only show clear button for localStorage entries
  const hasLocalEntries = entries.some((e) => e.source === "local");

  return (
    <section className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm animate-fade-in">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <h2 className="text-base font-semibold text-gray-800">最近生成</h2>
          <span className="text-xs text-gray-400">{entries.length} 筆</span>
        </div>
        {hasLocalEntries && (
          showClearConfirm ? (
            <div className="flex items-center gap-2">
              <span className="text-xs text-red-500">確定清除？</span>
              <button
                onClick={handleClear}
                className="text-xs px-2 py-0.5 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-colors"
              >
                確定
              </button>
              <button
                onClick={() => setShowClearConfirm(false)}
                className="text-xs px-2 py-0.5 bg-gray-200 text-gray-600 rounded-lg hover:bg-gray-300 transition-colors"
              >
                取消
              </button>
            </div>
          ) : (
            <button
              onClick={() => setShowClearConfirm(true)}
              className="text-xs text-gray-400 hover:text-red-500 transition-colors"
            >
              清除歷史
            </button>
          )
        )}
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
        {entries.slice(0, 8).map((entry) => (
          <button
            key={entry.id}
            onClick={() => handleNavigate(entry.id)}
            className="text-left group rounded-xl border border-gray-200 bg-gray-50 hover:border-blue-400 hover:bg-blue-50 transition-all hover:shadow-sm overflow-hidden"
          >
            {/* Thumbnail */}
            <div className="aspect-square bg-gray-100 relative overflow-hidden">
              {entry.firstImageUrl ? (
                <img
                  src={entry.firstImageUrl}
                  alt="Generated"
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  onError={(e) => {
                    (e.target as HTMLImageElement).style.display = "none";
                  }}
                />
              ) : (
                <div className="w-full h-full flex items-center justify-center">
                  <svg className="w-8 h-8 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
              )}
              {/* Image count badge */}
              <div className="absolute top-1.5 right-1.5 bg-black/50 text-white text-[10px] px-1.5 py-0.5 rounded-full backdrop-blur-sm">
                {entry.imageCount} 張
              </div>
            </div>

            {/* Info */}
            <div className="p-2.5">
              <p className="text-xs font-medium text-gray-700 truncate">
                {PRODUCT_TYPE_NAMES[entry.productType] || entry.productType}
              </p>
              <p className="text-[10px] text-gray-400 mt-0.5">
                {formatTime(entry.timestamp)}
              </p>
            </div>
          </button>
        ))}
      </div>

      {entries.length > 8 && (
        <p className="text-xs text-gray-400 text-center mt-3">
          顯示最近 8 筆，共 {entries.length} 筆記錄
        </p>
      )}
    </section>
  );
}
