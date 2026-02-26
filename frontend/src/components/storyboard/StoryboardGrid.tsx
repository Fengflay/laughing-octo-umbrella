"use client";

import { useState } from "react";
import {
  DndContext,
  closestCenter,
  PointerSensor,
  useSensor,
  useSensors,
  type DragEndEvent,
  type DragStartEvent,
  DragOverlay,
} from "@dnd-kit/core";
import {
  SortableContext,
  rectSortingStrategy,
} from "@dnd-kit/sortable";
import { motion } from "framer-motion";
import SortableCell from "./SortableCell";
import { useStoryboard, IMAGE_TYPE_LABELS, type ImageType } from "@/lib/storyboard-context";

export default function StoryboardGrid() {
  const { cells, swapCells, updateCellType } = useStoryboard();
  const [activeId, setActiveId] = useState<string | null>(null);
  const [typeMenuOpen, setTypeMenuOpen] = useState<string | null>(null);

  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: { distance: 8 },
    }),
  );

  const handleDragStart = (event: DragStartEvent) => {
    setActiveId(event.active.id as string);
    setTypeMenuOpen(null);
  };

  const handleDragEnd = (event: DragEndEvent) => {
    const { active, over } = event;
    setActiveId(null);

    if (!over || active.id === over.id) return;

    const fromIndex = cells.findIndex((c) => c.id === active.id);
    const toIndex = cells.findIndex((c) => c.id === over.id);

    if (fromIndex === -1 || toIndex === -1) return;
    // Don't allow swapping with locked cell (slot 0)
    if (cells[fromIndex].locked || cells[toIndex].locked) return;

    swapCells(fromIndex, toIndex);
  };

  const handleTypeChange = (cellId: string, newType: ImageType) => {
    updateCellType(cellId, newType);
    setTypeMenuOpen(null);
  };

  const activeCell = cells.find((c) => c.id === activeId);

  return (
    <div className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2.5">
          <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
            <svg
              className="w-3.5 h-3.5 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
              />
            </svg>
          </div>
          <div>
            <h2 className="text-base font-bold text-gray-800">
              故事板预览
            </h2>
            <p className="text-[10px] text-gray-400">
              拖拽交换位置 / 点击更换图片类型
            </p>
          </div>
        </div>
        <span className="text-xs text-gray-400 bg-gray-100 px-2.5 py-1 rounded-full">
          3 x 3
        </span>
      </div>

      <DndContext
        sensors={sensors}
        collisionDetection={closestCenter}
        onDragStart={handleDragStart}
        onDragEnd={handleDragEnd}
      >
        <SortableContext
          items={cells.map((c) => c.id)}
          strategy={rectSortingStrategy}
        >
          <div className="grid grid-cols-3 gap-3">
            {cells.map((cell) => (
              <SortableCell
                key={cell.id}
                cell={cell}
                isDragging={activeId === cell.id}
                typeMenuOpen={typeMenuOpen === cell.id}
                onToggleTypeMenu={() =>
                  setTypeMenuOpen(
                    typeMenuOpen === cell.id ? null : cell.id,
                  )
                }
                onTypeChange={(type) => handleTypeChange(cell.id, type)}
                onCloseTypeMenu={() => setTypeMenuOpen(null)}
              />
            ))}
          </div>
        </SortableContext>

        <DragOverlay>
          {activeCell ? (
            <motion.div
              initial={{ scale: 1.05 }}
              animate={{ scale: 1.08 }}
              className="aspect-square rounded-xl border-2 border-blue-400 bg-blue-50 shadow-2xl opacity-90 flex items-center justify-center"
            >
              <div className="text-center">
                <p className="text-sm font-bold text-blue-600">
                  {IMAGE_TYPE_LABELS[activeCell.imageType]}
                </p>
                <p className="text-[10px] text-blue-400 mt-0.5">
                  #{activeCell.index + 1}
                </p>
              </div>
            </motion.div>
          ) : null}
        </DragOverlay>
      </DndContext>
    </div>
  );
}
