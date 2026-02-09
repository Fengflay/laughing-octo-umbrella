"use client";

import type { GeneratedImage } from "@/types";

interface GenerationProgressProps {
  progress: number;
  total: number;
  images: GeneratedImage[];
}

const statusConfig = {
  pending: { label: "等待中", color: "bg-gray-100 text-gray-500", dot: "bg-gray-300" },
  generating: { label: "生成中", color: "bg-blue-50 text-blue-600", dot: "bg-blue-500 animate-pulse" },
  completed: { label: "完成", color: "bg-emerald-50 text-emerald-600", dot: "bg-emerald-500" },
  failed: { label: "失敗", color: "bg-red-50 text-red-600", dot: "bg-red-500" },
};

export default function GenerationProgress({
  progress,
  total,
  images,
}: GenerationProgressProps) {
  const percent = total > 0 ? Math.round((progress / total) * 100) : 0;

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="relative w-5 h-5">
            <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
            <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
          </div>
          <h2 className="text-base font-bold text-gray-800">AI 生成中</h2>
        </div>
        <span className="text-sm font-semibold text-blue-600">
          {progress}/{total} ({percent}%)
        </span>
      </div>

      {/* Progress bar */}
      <div className="w-full bg-gray-100 rounded-full h-2.5 overflow-hidden">
        <div
          className="bg-gradient-to-r from-blue-500 to-blue-600 h-full rounded-full transition-all duration-700 ease-out relative"
          style={{ width: `${percent}%` }}
        >
          {percent > 0 && percent < 100 && (
            <div className="absolute inset-0 animate-shimmer rounded-full" />
          )}
        </div>
      </div>

      {/* Per-image status grid */}
      <div className="grid grid-cols-3 sm:grid-cols-3 gap-2">
        {images.map((img, i) => {
          const cfg = statusConfig[img.status];
          return (
            <div
              key={img.template_id}
              className={`rounded-xl p-2.5 text-center ${cfg.color} transition-all duration-300`}
            >
              <div className="flex items-center justify-center gap-1.5 mb-1">
                <div className={`w-1.5 h-1.5 rounded-full ${cfg.dot}`} />
                <span className="font-bold text-xs">#{i + 1}</span>
              </div>
              <div className="text-[10px] leading-tight truncate">{img.template_name}</div>
              <div className="text-[10px] mt-0.5 font-medium">{cfg.label}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
