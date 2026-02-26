"use client";

import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { useTranslation } from "@/lib/i18n";
import { useTheme } from "@/lib/themes";
import type { LayoutModule } from "@/app/detail-layout/page";

interface SortableModuleProps {
  module: LayoutModule;
  primaryColor: string;
  viewMode: "single" | "long";
  layoutTemplate: string;
  onRemove: (id: string) => void;
}

export default function SortableModule({
  module,
  primaryColor,
  viewMode,
  layoutTemplate,
  onRemove,
}: SortableModuleProps) {
  const { t } = useTranslation();
  const { currentTheme } = useTheme();
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging,
  } = useSortable({ id: module.id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    opacity: isDragging ? 0.5 : 1,
  };

  const themeStyle = currentTheme
    ? {
        border: currentTheme.borderStyle,
        backgroundColor: currentTheme.backgroundColor,
      }
    : {};

  const moduleLabels: Record<LayoutModule["type"], { title: string; desc: string }> = {
    hero: { title: t.detailLayout.heroModule, desc: t.detailLayout.heroDesc },
    "selling-points": {
      title: t.detailLayout.sellingPoints,
      desc: t.detailLayout.sellingPointsDesc,
    },
    "multi-display": {
      title: t.detailLayout.multiDisplay,
      desc: t.detailLayout.multiDisplayDesc,
    },
    "spec-footer": {
      title: t.detailLayout.specFooter,
      desc: t.detailLayout.specFooterDesc,
    },
  };

  const label = moduleLabels[module.type];

  const gridClass =
    layoutTemplate === "grid"
      ? "grid grid-cols-2 gap-2"
      : layoutTemplate === "minimal"
        ? "flex flex-col gap-2"
        : module.type === "hero" || module.type === "spec-footer"
          ? "flex flex-col gap-2"
          : "grid grid-cols-2 gap-2";

  return (
    <div
      ref={setNodeRef}
      style={{ ...style, ...themeStyle }}
      className={`rounded-xl border border-gray-200 bg-white overflow-hidden transition-all duration-300 ${
        isDragging ? "shadow-lg ring-2 ring-blue-400" : "shadow-sm"
      } ${currentTheme ? currentTheme.decorationElements.join(" ") : ""}`}
    >
      {/* Module header */}
      <div className="flex items-center justify-between px-3 py-2 bg-gray-50/80 border-b border-gray-100">
        <div className="flex items-center gap-2">
          {/* Drag handle */}
          <button
            {...attributes}
            {...listeners}
            className="cursor-grab active:cursor-grabbing p-1 rounded hover:bg-gray-200 transition-colors touch-none"
            title={t.detailLayout.dragToReorder}
          >
            <svg
              className="w-4 h-4 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 8h16M4 16h16"
              />
            </svg>
          </button>
          <div>
            <span
              className="text-xs font-semibold"
              style={{ color: primaryColor }}
            >
              {label.title}
            </span>
            <span className="text-[10px] text-gray-400 ml-2">
              {label.desc}
            </span>
          </div>
        </div>
        <button
          onClick={() => onRemove(module.id)}
          className="p-1 rounded hover:bg-red-50 text-gray-400 hover:text-red-500 transition-colors"
          title={t.detailLayout.removeModule}
        >
          <svg
            className="w-4 h-4"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      {/* Module content */}
      <div className="p-3">
        <div className={gridClass}>
          {module.images.map((img, idx) => (
            <div
              key={idx}
              className={`rounded-lg overflow-hidden border border-gray-100 bg-gray-50 ${
                viewMode === "single" ? "max-h-[300px]" : ""
              }`}
            >
              <img
                src={img}
                alt={`${label.title} ${idx + 1}`}
                className="w-full h-full object-cover"
                loading="lazy"
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
