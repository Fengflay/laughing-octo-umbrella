"use client";

import { useState, useCallback } from "react";
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
  type DragEndEvent,
} from "@dnd-kit/core";
import {
  arrayMove,
  SortableContext,
  sortableKeyboardCoordinates,
  verticalListSortingStrategy,
} from "@dnd-kit/sortable";
import { useTranslation } from "@/lib/i18n";
import { ThemeProvider } from "@/lib/themes";
import SortableModule from "@/components/detail-layout/SortableModule";
import CopywritingEditor from "@/components/detail-layout/CopywritingEditor";
import ThemePicker from "@/components/detail-layout/ThemePicker";
import StyleCustomizer from "@/components/detail-layout/StyleCustomizer";
import ViewToggle from "@/components/detail-layout/ViewToggle";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface LayoutModule {
  id: string;
  type: "hero" | "selling-points" | "multi-display" | "spec-footer";
  images: string[]; // placeholder URLs
}

const DEFAULT_MODULES: LayoutModule[] = [
  {
    id: "mod-hero",
    type: "hero",
    images: [
      "https://picsum.photos/seed/hero_banner/800/400",
    ],
  },
  {
    id: "mod-selling",
    type: "selling-points",
    images: [
      "https://picsum.photos/seed/detail_sp1/400/400",
      "https://picsum.photos/seed/material_sp1/400/400",
    ],
  },
  {
    id: "mod-multi",
    type: "multi-display",
    images: [
      "https://picsum.photos/seed/scene_md1/400/400",
      "https://picsum.photos/seed/flatlay_md1/400/400",
      "https://picsum.photos/seed/scene_md2/400/400",
    ],
  },
  {
    id: "mod-spec",
    type: "spec-footer",
    images: [
      "https://picsum.photos/seed/spec_footer/800/400",
    ],
  },
];

// ---------------------------------------------------------------------------
// Page
// ---------------------------------------------------------------------------

export default function DetailLayoutPage() {
  const { t } = useTranslation();
  const [modules, setModules] = useState<LayoutModule[]>(DEFAULT_MODULES);
  const [viewMode, setViewMode] = useState<"single" | "long">("long");
  const [primaryColor, setPrimaryColor] = useState("#3b82f6");
  const [layoutTemplate, setLayoutTemplate] = useState("classic");

  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 8 } }),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    }),
  );

  const handleDragEnd = useCallback(
    (event: DragEndEvent) => {
      const { active, over } = event;
      if (over && active.id !== over.id) {
        setModules((prev) => {
          const oldIndex = prev.findIndex((m) => m.id === active.id);
          const newIndex = prev.findIndex((m) => m.id === over.id);
          return arrayMove(prev, oldIndex, newIndex);
        });
      }
    },
    [],
  );

  const handleRemoveModule = useCallback((id: string) => {
    setModules((prev) => prev.filter((m) => m.id !== id));
  }, []);

  const handleAddModule = useCallback(
    (type: LayoutModule["type"]) => {
      const placeholderMap: Record<LayoutModule["type"], string[]> = {
        hero: [
          `https://picsum.photos/seed/new_hero_${Date.now()}/800/400`,
        ],
        "selling-points": [
          `https://picsum.photos/seed/new_detail_${Date.now()}/400/400`,
          `https://picsum.photos/seed/new_material_${Date.now()}/400/400`,
        ],
        "multi-display": [
          `https://picsum.photos/seed/new_scene_${Date.now()}/400/400`,
          `https://picsum.photos/seed/new_flatlay_${Date.now()}/400/400`,
        ],
        "spec-footer": [
          `https://picsum.photos/seed/new_spec_${Date.now()}/800/400`,
        ],
      };

      setModules((prev) => [
        ...prev,
        {
          id: `mod-${type}-${Date.now()}`,
          type,
          images: placeholderMap[type],
        },
      ]);
    },
    [],
  );

  return (
    <ThemeProvider>
      <div className="space-y-6 animate-fade-in">
        {/* Page Header */}
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <h1 className="text-xl sm:text-2xl font-bold text-gray-900">
              {t.detailLayout.title}
            </h1>
            <p className="text-sm text-gray-500 mt-1">
              {t.detailLayout.dragToReorder}
            </p>
          </div>
          <ViewToggle viewMode={viewMode} onChangeView={setViewMode} />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Left: Module layout area */}
          <div className="lg:col-span-2 space-y-4">
            {/* Modules with drag-and-drop */}
            <div
              className="rounded-2xl border border-gray-200 bg-white p-4 shadow-sm overflow-hidden transition-colors duration-500"
              style={{
                borderColor: `${primaryColor}30`,
              }}
            >
              <DndContext
                sensors={sensors}
                collisionDetection={closestCenter}
                onDragEnd={handleDragEnd}
              >
                <SortableContext
                  items={modules.map((m) => m.id)}
                  strategy={verticalListSortingStrategy}
                >
                  <div
                    className={
                      viewMode === "long"
                        ? "space-y-3"
                        : "space-y-3"
                    }
                  >
                    {modules.map((mod) => (
                      <SortableModule
                        key={mod.id}
                        module={mod}
                        primaryColor={primaryColor}
                        viewMode={viewMode}
                        layoutTemplate={layoutTemplate}
                        onRemove={handleRemoveModule}
                      />
                    ))}
                  </div>
                </SortableContext>
              </DndContext>

              {/* Add module button */}
              <div className="mt-4 flex flex-wrap gap-2">
                <span className="text-xs text-gray-400 self-center mr-1">
                  {t.detailLayout.addModule}:
                </span>
                {(
                  [
                    { type: "hero" as const, label: t.detailLayout.heroModule },
                    { type: "selling-points" as const, label: t.detailLayout.sellingPoints },
                    { type: "multi-display" as const, label: t.detailLayout.multiDisplay },
                    { type: "spec-footer" as const, label: t.detailLayout.specFooter },
                  ] as const
                ).map((opt) => (
                  <button
                    key={opt.type}
                    onClick={() => handleAddModule(opt.type)}
                    className="px-3 py-1.5 text-xs font-medium rounded-lg border border-dashed border-gray-300 text-gray-500 hover:border-blue-400 hover:text-blue-600 hover:bg-blue-50 transition-all"
                  >
                    + {opt.label}
                  </button>
                ))}
              </div>
            </div>

            {/* Copywriting Section */}
            <CopywritingEditor primaryColor={primaryColor} />
          </div>

          {/* Right Sidebar: Theme + Style */}
          <div className="space-y-4">
            <ThemePicker />
            <StyleCustomizer
              primaryColor={primaryColor}
              onColorChange={setPrimaryColor}
              layoutTemplate={layoutTemplate}
              onTemplateChange={setLayoutTemplate}
            />
          </div>
        </div>
      </div>
    </ThemeProvider>
  );
}
