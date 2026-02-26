"use client";

import { useTranslation } from "@/lib/i18n";
import { HexColorPicker } from "react-colorful";
import { useState } from "react";

interface StyleCustomizerProps {
  primaryColor: string;
  onColorChange: (color: string) => void;
  layoutTemplate: string;
  onTemplateChange: (template: string) => void;
}

const PRESET_COLORS = [
  "#3b82f6",
  "#8b5cf6",
  "#ec4899",
  "#ef4444",
  "#f97316",
  "#eab308",
  "#22c55e",
  "#14b8a6",
  "#06b6d4",
  "#1e293b",
];

export default function StyleCustomizer({
  primaryColor,
  onColorChange,
  layoutTemplate,
  onTemplateChange,
}: StyleCustomizerProps) {
  const { t } = useTranslation();
  const [showPicker, setShowPicker] = useState(false);

  const templates = [
    { id: "classic", label: t.detailLayout.templateClassic },
    { id: "minimal", label: t.detailLayout.templateMinimal },
    { id: "bold", label: t.detailLayout.templateBold },
    { id: "grid", label: t.detailLayout.templateGrid },
  ];

  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-4 shadow-sm space-y-4">
      {/* Color Scheme */}
      <div>
        <div className="flex items-center gap-2 mb-3">
          <svg
            className="w-4 h-4"
            style={{ color: primaryColor }}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
            />
          </svg>
          <h3 className="text-sm font-semibold text-gray-800">
            {t.detailLayout.colorScheme}
          </h3>
        </div>

        {/* Preset colors */}
        <div className="flex flex-wrap gap-2 mb-3">
          {PRESET_COLORS.map((color) => (
            <button
              key={color}
              onClick={() => onColorChange(color)}
              className={`w-7 h-7 rounded-lg border-2 transition-all hover:scale-110 ${
                primaryColor === color
                  ? "border-gray-800 ring-2 ring-gray-300"
                  : "border-transparent"
              }`}
              style={{ backgroundColor: color }}
              title={color}
            />
          ))}
        </div>

        {/* Custom color picker toggle */}
        <button
          onClick={() => setShowPicker(!showPicker)}
          className="flex items-center gap-2 text-xs text-gray-500 hover:text-gray-700 transition-colors"
        >
          <div
            className="w-4 h-4 rounded border border-gray-300"
            style={{ backgroundColor: primaryColor }}
          />
          {primaryColor}
        </button>

        {showPicker && (
          <div className="mt-2 animate-scale-in">
            <HexColorPicker color={primaryColor} onChange={onColorChange} />
          </div>
        )}
      </div>

      {/* Layout Template */}
      <div>
        <div className="flex items-center gap-2 mb-3">
          <svg
            className="w-4 h-4 text-gray-500"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"
            />
          </svg>
          <h3 className="text-sm font-semibold text-gray-800">
            {t.detailLayout.layoutTemplate}
          </h3>
        </div>

        <div className="grid grid-cols-2 gap-2">
          {templates.map((tmpl) => (
            <button
              key={tmpl.id}
              onClick={() => onTemplateChange(tmpl.id)}
              className={`px-3 py-2.5 text-xs font-medium rounded-xl border transition-all ${
                layoutTemplate === tmpl.id
                  ? "border-blue-400 bg-blue-50 text-blue-700 ring-1 ring-blue-200"
                  : "border-gray-200 text-gray-600 hover:border-gray-300 hover:bg-gray-50"
              }`}
            >
              {tmpl.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
