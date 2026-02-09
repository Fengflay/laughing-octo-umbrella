"use client";

import { useMemo } from "react";
import type { SceneTemplate } from "@/types";

interface SubCategoryTabsProps {
  templates: SceneTemplate[];
  activeSubCategory: string;
  onSubCategoryChange: (subCategory: string) => void;
}

export default function SubCategoryTabs({
  templates,
  activeSubCategory,
  onSubCategoryChange,
}: SubCategoryTabsProps) {
  // Extract unique sub-categories from templates, preserving order
  const subCategories = useMemo(() => {
    const seen = new Map<string, { id: string; name: string; count: number }>();
    for (const t of templates) {
      const existing = seen.get(t.sub_category);
      if (existing) {
        existing.count++;
      } else {
        seen.set(t.sub_category, {
          id: t.sub_category,
          name: t.sub_category_name,
          count: 1,
        });
      }
    }
    return Array.from(seen.values());
  }, [templates]);

  // Don't render tabs if there's only one sub-category (common)
  if (subCategories.length <= 1) return null;

  return (
    <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-hide">
      {/* "All" tab */}
      <button
        onClick={() => onSubCategoryChange("all")}
        className={`shrink-0 px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-200 ${
          activeSubCategory === "all"
            ? "bg-blue-500 text-white shadow-sm"
            : "bg-gray-100 text-gray-600 hover:bg-gray-200"
        }`}
      >
        全部
        <span className="ml-1 opacity-70">{templates.length}</span>
      </button>

      {/* Sub-category tabs */}
      {subCategories.map((sub) => (
        <button
          key={sub.id}
          onClick={() => onSubCategoryChange(sub.id)}
          className={`shrink-0 px-3 py-1.5 rounded-lg text-xs font-medium transition-all duration-200 ${
            activeSubCategory === sub.id
              ? "bg-blue-500 text-white shadow-sm"
              : "bg-gray-100 text-gray-600 hover:bg-gray-200"
          }`}
        >
          {sub.name}
          <span className="ml-1 opacity-70">{sub.count}</span>
        </button>
      ))}
    </div>
  );
}
