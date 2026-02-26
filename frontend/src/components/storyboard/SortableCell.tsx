"use client";

import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import { motion, AnimatePresence } from "framer-motion";
import type { GridCell, ImageType } from "@/lib/storyboard-context";
import { IMAGE_TYPE_LABELS } from "@/lib/storyboard-context";

interface SortableCellProps {
  cell: GridCell;
  isDragging: boolean;
  typeMenuOpen: boolean;
  onToggleTypeMenu: () => void;
  onTypeChange: (type: ImageType) => void;
  onCloseTypeMenu: () => void;
}

const ALL_IMAGE_TYPES: ImageType[] = [
  "white_bg",
  "material",
  "detail",
  "scene",
  "flat_lay",
  "model",
];

export default function SortableCell({
  cell,
  isDragging,
  typeMenuOpen,
  onToggleTypeMenu,
  onTypeChange,
  onCloseTypeMenu,
}: SortableCellProps) {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
  } = useSortable({
    id: cell.id,
    disabled: cell.locked,
  });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
  };

  const typeColor: Record<ImageType, string> = {
    white_bg: "bg-gray-100 text-gray-600 border-gray-200",
    material: "bg-amber-50 text-amber-700 border-amber-200",
    detail: "bg-cyan-50 text-cyan-700 border-cyan-200",
    scene: "bg-emerald-50 text-emerald-700 border-emerald-200",
    flat_lay: "bg-purple-50 text-purple-700 border-purple-200",
    model: "bg-pink-50 text-pink-700 border-pink-200",
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      className={`relative aspect-square rounded-xl border-2 transition-all duration-200 ${
        isDragging
          ? "border-dashed border-blue-400 bg-blue-50/50 opacity-40"
          : cell.locked
            ? "border-gray-200 bg-gray-50"
            : "border-gray-200 bg-white hover:border-gray-300 hover:shadow-md cursor-grab active:cursor-grabbing"
      }`}
      {...(cell.locked ? {} : { ...attributes, ...listeners })}
    >
      {/* Preview image or placeholder */}
      {cell.previewUrl ? (
        <img
          src={cell.previewUrl}
          alt={IMAGE_TYPE_LABELS[cell.imageType]}
          className="w-full h-full object-cover rounded-[10px]"
          draggable={false}
        />
      ) : (
        <div className="flex items-center justify-center h-full">
          <div className="text-center space-y-1.5">
            <div className="w-10 h-10 mx-auto rounded-xl bg-gray-100 flex items-center justify-center">
              <span className="text-lg text-gray-300 font-bold">
                {cell.index + 1}
              </span>
            </div>
            <p className="text-[10px] text-gray-400">
              {IMAGE_TYPE_LABELS[cell.imageType]}
            </p>
          </div>
        </div>
      )}

      {/* Type badge */}
      <div className="absolute top-2 left-2">
        <span
          className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-md text-[10px] font-semibold border ${typeColor[cell.imageType]}`}
        >
          {IMAGE_TYPE_LABELS[cell.imageType]}
        </span>
      </div>

      {/* Index badge */}
      <div className="absolute top-2 right-2">
        <span className="inline-flex items-center justify-center w-5 h-5 rounded-full bg-black/40 text-white text-[10px] font-bold backdrop-blur-sm">
          {cell.index + 1}
        </span>
      </div>

      {/* Lock indicator */}
      {cell.locked && (
        <div className="absolute bottom-2 left-2">
          <span className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-gray-200 text-gray-500 text-[9px] font-medium">
            <svg
              className="w-2.5 h-2.5"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fillRule="evenodd"
                d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                clipRule="evenodd"
              />
            </svg>
            固定
          </span>
        </div>
      )}

      {/* Change type button (not for locked cells) */}
      {!cell.locked && (
        <div className="absolute bottom-2 right-2">
          <button
            onClick={(e) => {
              e.stopPropagation();
              onToggleTypeMenu();
            }}
            onPointerDown={(e) => e.stopPropagation()}
            className="flex items-center gap-1 px-2 py-1 rounded-lg bg-white/90 border border-gray-200 text-[10px] text-gray-600 font-medium hover:bg-white hover:border-gray-300 shadow-sm backdrop-blur-sm transition-all"
          >
            <svg
              className="w-3 h-3"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"
              />
            </svg>
            更换
          </button>
        </div>
      )}

      {/* Type dropdown menu */}
      <AnimatePresence>
        {typeMenuOpen && (
          <>
            <div
              className="fixed inset-0 z-40"
              onClick={onCloseTypeMenu}
            />
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 4 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 4 }}
              className="absolute bottom-10 right-2 z-50 bg-white rounded-xl border border-gray-200 shadow-xl py-1.5 min-w-[120px]"
              onPointerDown={(e) => e.stopPropagation()}
            >
              {ALL_IMAGE_TYPES.filter((t) => t !== "white_bg").map(
                (type) => (
                  <button
                    key={type}
                    onClick={() => onTypeChange(type)}
                    className={`w-full text-left px-3 py-1.5 text-xs flex items-center gap-2 transition-colors ${
                      cell.imageType === type
                        ? "bg-blue-50 text-blue-700 font-semibold"
                        : "text-gray-600 hover:bg-gray-50"
                    }`}
                  >
                    <span
                      className={`w-2 h-2 rounded-full shrink-0 ${
                        cell.imageType === type
                          ? "bg-blue-500"
                          : "bg-gray-300"
                      }`}
                    />
                    {IMAGE_TYPE_LABELS[type]}
                  </button>
                ),
              )}
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}
