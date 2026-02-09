"use client";

import { getDownloadUrl } from "@/lib/api";

interface DownloadPanelProps {
  taskId: string;
  hasResults: boolean;
}

const platforms = [
  { id: "shopee", name: "蝦皮 Shopee", size: "800x800", emoji: "🟠" },
  { id: "momo", name: "MOMO", size: "1000x1000", emoji: "🟣" },
  { id: "instagram", name: "IG 貼文", size: "1080x1080", emoji: "📸" },
  { id: "ig_story", name: "IG 限動", size: "1080x1920", emoji: "📱" },
  { id: "facebook", name: "FB 貼文", size: "1200x630", emoji: "🔵" },
  { id: "line", name: "LINE 購物", size: "800x800", emoji: "🟢" },
  { id: "general", name: "通用高畫質", size: "1024x1024", emoji: "⬇️" },
];

export default function DownloadPanel({ taskId, hasResults }: DownloadPanelProps) {
  if (!hasResults) return null;

  return (
    <div className="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
      <div className="px-5 py-4 border-b border-gray-100">
        <div className="flex items-center gap-2">
          <svg className="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3M3 17v3a2 2 0 002 2h14a2 2 0 002-2v-3" />
          </svg>
          <h2 className="text-base font-semibold text-gray-800">批量下載</h2>
          <span className="text-xs text-gray-400 ml-auto hidden sm:inline">按平台規格打包 ZIP</span>
        </div>
      </div>
      <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2.5 p-4">
        {platforms.map((p) => (
          <a
            key={p.id}
            href={getDownloadUrl(taskId, p.id)}
            download
            className="flex flex-col items-center gap-1.5 p-3 sm:p-4 rounded-xl border border-gray-200 bg-gray-50 hover:border-blue-400 hover:bg-blue-50 transition-all hover:shadow-sm text-center"
          >
            <span className="text-lg">{p.emoji}</span>
            <span className="font-medium text-xs sm:text-sm">{p.name}</span>
            <span className="text-xs text-gray-400">{p.size}</span>
          </a>
        ))}
      </div>
    </div>
  );
}
