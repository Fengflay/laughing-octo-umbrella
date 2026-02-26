"use client";

import { useTranslation } from "@/lib/i18n";

interface ViewToggleProps {
  viewMode: "single" | "long";
  onChangeView: (mode: "single" | "long") => void;
}

export default function ViewToggle({ viewMode, onChangeView }: ViewToggleProps) {
  const { t } = useTranslation();

  return (
    <div className="flex items-center bg-gray-100 rounded-xl p-1">
      <button
        onClick={() => onChangeView("single")}
        className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
          viewMode === "single"
            ? "bg-white text-gray-900 shadow-sm"
            : "text-gray-500 hover:text-gray-700"
        }`}
      >
        <svg
          className="w-3.5 h-3.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M4 6a2 2 0 012-2h12a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V6z"
          />
        </svg>
        {t.detailLayout.singleView}
      </button>
      <button
        onClick={() => onChangeView("long")}
        className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
          viewMode === "long"
            ? "bg-white text-gray-900 shadow-sm"
            : "text-gray-500 hover:text-gray-700"
        }`}
      >
        <svg
          className="w-3.5 h-3.5"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M4 6a2 2 0 012-2h12a2 2 0 012 2v12a2 2 0 01-2 2H6a2 2 0 01-2-2V6z"
          />
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M4 12h16"
          />
        </svg>
        {t.detailLayout.longView}
      </button>
    </div>
  );
}
