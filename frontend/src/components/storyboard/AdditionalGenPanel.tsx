"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import type { ImageType } from "@/lib/storyboard-context";
import { IMAGE_TYPE_LABELS } from "@/lib/storyboard-context";

interface AdditionalGenPanelProps {
  onGenerate: (params: {
    imageType: ImageType;
    count: number;
    angle?: string;
    lighting?: string;
  }) => void;
  onClose: () => void;
  generating?: boolean;
}

const SELECTABLE_TYPES: ImageType[] = [
  "material",
  "detail",
  "scene",
  "flat_lay",
  "model",
];

const ANGLE_OPTIONS = ["正面", "45度", "侧面", "俯拍", "仰拍"];
const LIGHTING_OPTIONS = ["自然光", "暖光", "冷光", "侧光", "逆光"];

export default function AdditionalGenPanel({
  onGenerate,
  onClose,
  generating,
}: AdditionalGenPanelProps) {
  const [selectedType, setSelectedType] = useState<ImageType>("scene");
  const [count, setCount] = useState(2);
  const [selectedAngle, setSelectedAngle] = useState<string | null>(null);
  const [selectedLighting, setSelectedLighting] = useState<string | null>(null);

  const handleSubmit = () => {
    onGenerate({
      imageType: selectedType,
      count,
      angle: selectedAngle || undefined,
      lighting: selectedLighting || undefined,
    });
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 bg-black/60 z-50 flex items-center justify-center p-4"
      onClick={onClose}
    >
      <motion.div
        initial={{ scale: 0.95, y: 20 }}
        animate={{ scale: 1, y: 0 }}
        exit={{ scale: 0.95, y: 20 }}
        className="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="p-4 border-b border-gray-100 flex items-center justify-between">
          <div>
            <h3 className="text-sm font-bold text-gray-800">定向增补</h3>
            <p className="text-[10px] text-gray-400 mt-0.5">
              选择类型和数量，生成更多图片
            </p>
          </div>
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-gray-600 transition-colors"
          >
            <svg
              className="w-5 h-5"
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

        <div className="p-4 space-y-4">
          {/* Type selection */}
          <div>
            <label className="text-xs font-semibold text-gray-700 mb-2 block">
              图片类型
            </label>
            <div className="grid grid-cols-5 gap-2">
              {SELECTABLE_TYPES.map((type) => (
                <button
                  key={type}
                  onClick={() => setSelectedType(type)}
                  className={`p-2.5 rounded-xl border-2 text-center transition-all ${
                    selectedType === type
                      ? "border-blue-400 bg-blue-50"
                      : "border-gray-200 bg-white hover:bg-gray-50"
                  }`}
                >
                  <div
                    className={`w-8 h-8 mx-auto rounded-lg mb-1 flex items-center justify-center ${
                      selectedType === type ? "bg-blue-100" : "bg-gray-100"
                    }`}
                  >
                    <svg
                      className={`w-4 h-4 ${selectedType === type ? "text-blue-600" : "text-gray-400"}`}
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                      />
                    </svg>
                  </div>
                  <p
                    className={`text-[10px] font-medium ${
                      selectedType === type
                        ? "text-blue-700"
                        : "text-gray-500"
                    }`}
                  >
                    {IMAGE_TYPE_LABELS[type]}
                  </p>
                </button>
              ))}
            </div>
          </div>

          {/* Count */}
          <div>
            <label className="text-xs font-semibold text-gray-700 mb-2 block">
              数量
            </label>
            <div className="flex gap-2">
              {[1, 2, 3, 4, 5].map((n) => (
                <button
                  key={n}
                  onClick={() => setCount(n)}
                  className={`w-10 h-10 rounded-xl font-semibold text-sm transition-all ${
                    count === n
                      ? "bg-blue-500 text-white shadow-sm"
                      : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                  }`}
                >
                  {n}
                </button>
              ))}
            </div>
          </div>

          {/* Angle (optional) */}
          <div>
            <label className="text-xs font-semibold text-gray-700 mb-1.5 block">
              角度 <span className="text-gray-400 font-normal">(可选)</span>
            </label>
            <div className="flex flex-wrap gap-1.5">
              {ANGLE_OPTIONS.map((angle) => (
                <button
                  key={angle}
                  onClick={() =>
                    setSelectedAngle(
                      selectedAngle === angle ? null : angle,
                    )
                  }
                  className={`px-2.5 py-1 rounded-lg text-[11px] font-medium transition-all ${
                    selectedAngle === angle
                      ? "bg-emerald-500 text-white"
                      : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                  }`}
                >
                  {angle}
                </button>
              ))}
            </div>
          </div>

          {/* Lighting (optional) */}
          <div>
            <label className="text-xs font-semibold text-gray-700 mb-1.5 block">
              光影 <span className="text-gray-400 font-normal">(可选)</span>
            </label>
            <div className="flex flex-wrap gap-1.5">
              {LIGHTING_OPTIONS.map((light) => (
                <button
                  key={light}
                  onClick={() =>
                    setSelectedLighting(
                      selectedLighting === light ? null : light,
                    )
                  }
                  className={`px-2.5 py-1 rounded-lg text-[11px] font-medium transition-all ${
                    selectedLighting === light
                      ? "bg-amber-500 text-white"
                      : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                  }`}
                >
                  {light}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Actions */}
        <div className="border-t border-gray-100 p-4 flex items-center justify-between">
          <p className="text-xs text-gray-400">
            将生成 {count} 张{IMAGE_TYPE_LABELS[selectedType]}
          </p>
          <div className="flex items-center gap-2">
            <button
              onClick={onClose}
              className="px-4 py-2 text-sm text-gray-600 bg-gray-100 rounded-xl hover:bg-gray-200 font-medium transition-colors"
            >
              取消
            </button>
            <button
              onClick={handleSubmit}
              disabled={generating}
              className="px-5 py-2 text-sm text-white bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl hover:from-blue-700 hover:to-blue-800 font-semibold shadow-sm disabled:opacity-50 transition-all flex items-center gap-2"
            >
              {generating ? (
                <>
                  <svg className="animate-spin h-3.5 w-3.5" viewBox="0 0 24 24">
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                      fill="none"
                    />
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                    />
                  </svg>
                  生成中...
                </>
              ) : (
                <>
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
                      d="M12 4v16m8-8H4"
                    />
                  </svg>
                  开始生成
                </>
              )}
            </button>
          </div>
        </div>
      </motion.div>
    </motion.div>
  );
}
