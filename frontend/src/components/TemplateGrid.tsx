"use client";

import { useMemo } from "react";
import type { SceneTemplate } from "@/types";
import TemplateCard from "./TemplateCard";
import SubCategoryTabs from "./SubCategoryTabs";

interface TemplateGridProps {
  templates: SceneTemplate[];
  selectedIds: Set<string>;
  customPrompts: Record<string, string>;
  activeSubCategory: string;
  onSubCategoryChange: (subCategory: string) => void;
  onPromptChange: (templateId: string, prompt: string | null) => void;
  onToggleSelect: (templateId: string) => void;
  onSelectAll: () => void;
  onSelectNone: () => void;
}

export default function TemplateGrid({
  templates,
  selectedIds,
  customPrompts,
  activeSubCategory,
  onSubCategoryChange,
  onPromptChange,
  onToggleSelect,
  onSelectAll,
  onSelectNone,
}: TemplateGridProps) {
  // Filter templates by active sub-category
  const filteredTemplates = useMemo(() => {
    if (activeSubCategory === "all") return templates;
    return templates.filter((t) => t.sub_category === activeSubCategory);
  }, [templates, activeSubCategory]);

  const filteredSelectedCount = filteredTemplates.filter((t) =>
    selectedIds.has(t.id)
  ).length;
  const allFilteredSelected =
    filteredTemplates.length > 0 &&
    filteredSelectedCount === filteredTemplates.length;
  const customCount = Object.keys(customPrompts).length;

  const handleSelectAllFiltered = () => {
    // Select all in the current filtered view
    for (const t of filteredTemplates) {
      if (!selectedIds.has(t.id)) {
        onToggleSelect(t.id);
      }
    }
  };

  const handleSelectNoneFiltered = () => {
    // Deselect all in the current filtered view
    for (const t of filteredTemplates) {
      if (selectedIds.has(t.id)) {
        onToggleSelect(t.id);
      }
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <h2 className="text-base font-bold text-gray-800">場景模板</h2>
          <span className="text-xs text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
            {selectedIds.size}/{templates.length} 已選
          </span>
          {customCount > 0 && (
            <span className="text-xs text-orange-500 bg-orange-50 px-2 py-0.5 rounded-full">
              {customCount} 自定義
            </span>
          )}
        </div>
        <div className="flex items-center gap-2">
          {activeSubCategory !== "all" && (
            <span className="text-[10px] text-gray-400">
              {filteredSelectedCount}/{filteredTemplates.length} 當前分類
            </span>
          )}
          <button
            onClick={
              allFilteredSelected
                ? handleSelectNoneFiltered
                : handleSelectAllFiltered
            }
            className="text-xs text-blue-500 hover:text-blue-700 font-medium transition-colors"
          >
            {allFilteredSelected ? "取消全選" : "全選"}
          </button>
        </div>
      </div>

      {/* Sub-category tabs */}
      <SubCategoryTabs
        templates={templates}
        activeSubCategory={activeSubCategory}
        onSubCategoryChange={onSubCategoryChange}
      />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2.5">
        {filteredTemplates.map((t, i) => (
          <TemplateCard
            key={t.id}
            template={t}
            index={i}
            selected={selectedIds.has(t.id)}
            customPrompt={customPrompts[t.id] || null}
            onPromptChange={onPromptChange}
            onToggleSelect={onToggleSelect}
          />
        ))}
      </div>

      {filteredTemplates.length === 0 && (
        <div className="text-center py-8 text-gray-400 text-sm">
          此分類暫無模板
        </div>
      )}
    </div>
  );
}
