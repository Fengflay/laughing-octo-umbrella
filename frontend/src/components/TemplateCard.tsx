"use client";

import { useState } from "react";
import type { SceneTemplate } from "@/types";

interface TemplateCardProps {
  template: SceneTemplate;
  index: number;
  selected: boolean;
  customPrompt: string | null;
  onPromptChange: (templateId: string, prompt: string | null) => void;
  onToggleSelect: (templateId: string) => void;
}

const ASPECT_RATIO_LABELS: Record<string, string> = {
  "1:1": "正方形",
  "4:3": "橫幅",
  "3:4": "直幅",
};

export default function TemplateCard({
  template,
  index,
  selected,
  customPrompt,
  onPromptChange,
  onToggleSelect,
}: TemplateCardProps) {
  const [editing, setEditing] = useState(false);
  const [editValue, setEditValue] = useState(customPrompt || template.prompt);

  const description = template.description || template.name;
  const ratioLabel = ASPECT_RATIO_LABELS[template.aspect_ratio] || template.aspect_ratio;

  const handleSave = () => {
    const val = editValue.trim();
    if (val === template.prompt) {
      onPromptChange(template.id, null);
    } else {
      onPromptChange(template.id, val);
    }
    setEditing(false);
  };

  const handleReset = () => {
    setEditValue(template.prompt);
    onPromptChange(template.id, null);
    setEditing(false);
  };

  return (
    <div
      className={`rounded-xl border p-4 space-y-2.5 transition-all duration-200 ${
        selected
          ? "bg-blue-50/80 border-blue-300 shadow-sm"
          : "bg-white border-gray-200 opacity-50 hover:opacity-70"
      }`}
    >
      {/* Header */}
      <div className="flex items-start justify-between gap-2">
        <div className="flex items-start gap-2.5 min-w-0">
          <input
            type="checkbox"
            checked={selected}
            onChange={() => onToggleSelect(template.id)}
            className="mt-0.5 w-4 h-4 rounded border-gray-300 text-blue-500 focus:ring-blue-500 cursor-pointer shrink-0"
          />
          <div className="min-w-0">
            <div className="flex items-center gap-2 flex-wrap">
              <span className="inline-flex items-center bg-gray-100 text-gray-600 text-[10px] px-1.5 py-0.5 rounded font-bold">
                #{index + 1}
              </span>
              <span className="font-semibold text-sm text-gray-800">{template.name}</span>
              <span className="text-gray-400 text-xs">{template.name_en}</span>
            </div>
            <p className="text-[11px] text-gray-400 mt-1 leading-relaxed">{description}</p>
          </div>
        </div>
        <div className="flex items-center gap-1.5 shrink-0">
          {customPrompt && (
            <span className="text-[10px] text-orange-500 bg-orange-50 px-1.5 py-0.5 rounded font-medium">
              已自定
            </span>
          )}
          <span className="text-[10px] text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded">
            {ratioLabel}
          </span>
        </div>
      </div>

      {/* Prompt editing */}
      {selected && (
        <>
          {editing ? (
            <div className="space-y-2">
              <textarea
                value={editValue}
                onChange={(e) => setEditValue(e.target.value)}
                rows={3}
                className="w-full text-xs border border-gray-300 rounded-lg p-2.5 focus:outline-none focus:ring-2 focus:ring-blue-500/30 focus:border-blue-400 resize-none"
                placeholder="輸入自定義提示詞..."
              />
              <div className="flex gap-1.5">
                <button
                  onClick={handleSave}
                  className="text-xs px-3 py-1.5 bg-blue-500 text-white rounded-lg hover:bg-blue-600 font-medium transition-colors"
                >
                  保存
                </button>
                <button
                  onClick={handleReset}
                  className="text-xs px-3 py-1.5 bg-gray-100 text-gray-600 rounded-lg hover:bg-gray-200 transition-colors"
                >
                  重置
                </button>
                <button
                  onClick={() => setEditing(false)}
                  className="text-xs px-3 py-1.5 text-gray-400 hover:text-gray-600 transition-colors"
                >
                  取消
                </button>
              </div>
            </div>
          ) : (
            <div className="group">
              <p className="text-[11px] text-gray-500 line-clamp-2 leading-relaxed">
                {customPrompt || template.prompt}
              </p>
              <button
                onClick={() => setEditing(true)}
                className="text-[11px] text-blue-500 hover:text-blue-700 mt-1 font-medium transition-colors"
              >
                編輯提示詞
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
}
