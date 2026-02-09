"use client";

import type { StyleInfo } from "@/types";

interface StyleSelectorProps {
  styles: StyleInfo[];
  selected: string | null;
  onSelect: (styleId: string | null) => void;
}

export default function StyleSelector({
  styles,
  selected,
  onSelect,
}: StyleSelectorProps) {
  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between">
        <p className="text-xs text-gray-400">
          選擇視覺風格，讓所有場景圖帶有統一的美學調性
        </p>
        <span className="text-[10px] text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">可選</span>
      </div>
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
        {/* Default style */}
        <button
          onClick={() => onSelect(null)}
          className={`card-hover relative flex flex-col items-center gap-2 p-3.5 rounded-xl border-2 transition-all ${
            selected === null
              ? "border-blue-500 bg-blue-50 shadow-sm"
              : "border-gray-100 bg-white hover:border-gray-200"
          }`}
        >
          <div
            className="w-10 h-10 rounded-full flex items-center justify-center text-lg shadow-inner"
            style={{ background: "linear-gradient(135deg, #f3f4f6, #e5e7eb)" }}
          >
            🎨
          </div>
          <span className="font-semibold text-sm">預設</span>
          <span className="text-[10px] text-gray-400 leading-tight text-center">
            原始模板設定
          </span>
        </button>

        {styles.map((style, index) => (
          <button
            key={style.id}
            onClick={() => onSelect(style.id)}
            className={`card-hover relative flex flex-col items-center gap-2 p-3.5 rounded-xl border-2 transition-all ${
              selected === style.id
                ? "border-blue-500 bg-blue-50 shadow-sm ring-1 ring-blue-200"
                : "border-gray-100 bg-white hover:border-gray-200"
            }`}
          >
            {/* Recommended badge on first style */}
            {index === 0 && (
              <div className="absolute -top-1.5 left-1/2 -translate-x-1/2">
                <span className="text-[9px] font-bold text-white bg-gradient-to-r from-orange-400 to-pink-400 px-2 py-0.5 rounded-full shadow-sm whitespace-nowrap">
                  推薦
                </span>
              </div>
            )}
            {selected === style.id && (
              <div className="absolute top-1.5 right-1.5">
                <svg className="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
              </div>
            )}
            <div
              className="w-10 h-10 rounded-full flex items-center justify-center text-lg shadow-inner"
              style={{ backgroundColor: style.preview_color }}
            >
              {style.icon}
            </div>
            <span className="font-semibold text-sm">{style.name}</span>
            <span className="text-[10px] text-gray-400 leading-tight text-center line-clamp-2">
              {style.description}
            </span>
          </button>
        ))}
      </div>
    </div>
  );
}
