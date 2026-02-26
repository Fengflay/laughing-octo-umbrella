"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import type { ImageType } from "@/lib/storyboard-context";
import { IMAGE_TYPE_LABELS } from "@/lib/storyboard-context";

interface RegeneratePanelProps {
  imageType: ImageType;
  onRegenerate: (options: { mode: "same_seed" | "tweak"; tweaks?: { scene?: string; style?: string; imageType?: string } }) => void;
  onClose: () => void;
  regenerating?: boolean;
}

const SCENE_OPTIONS = [
  "日系极简",
  "北欧风",
  "韩系奶油风",
  "现代LOFT",
  "奢华大理石",
  "暖光棚拍",
  "城市街景",
  "花园庭院",
];

const STYLE_OPTIONS = [
  "明亮清新",
  "暗调质感",
  "暖色调",
  "冷色调",
  "复古胶片",
  "高对比度",
];

export default function RegeneratePanel({
  imageType,
  onRegenerate,
  onClose,
  regenerating,
}: RegeneratePanelProps) {
  const [mode, setMode] = useState<"same_seed" | "tweak">("same_seed");
  const [selectedScene, setSelectedScene] = useState<string | null>(null);
  const [selectedStyle, setSelectedStyle] = useState<string | null>(null);

  const handleSubmit = () => {
    if (mode === "same_seed") {
      onRegenerate({ mode: "same_seed" });
    } else {
      onRegenerate({
        mode: "tweak",
        tweaks: {
          scene: selectedScene || undefined,
          style: selectedStyle || undefined,
        },
      });
    }
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
            <h3 className="text-sm font-bold text-gray-800">重新生成</h3>
            <p className="text-[10px] text-gray-400 mt-0.5">
              当前类型: {IMAGE_TYPE_LABELS[imageType]}
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

        {/* Mode selection */}
        <div className="p-4 space-y-4">
          <div className="flex gap-2">
            <button
              onClick={() => setMode("same_seed")}
              className={`flex-1 p-3 rounded-xl border-2 text-left transition-all ${
                mode === "same_seed"
                  ? "border-blue-400 bg-blue-50"
                  : "border-gray-200 bg-white hover:bg-gray-50"
              }`}
            >
              <div className="flex items-center gap-2 mb-1">
                <svg
                  className={`w-4 h-4 ${mode === "same_seed" ? "text-blue-600" : "text-gray-400"}`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                  />
                </svg>
                <span className={`text-xs font-semibold ${mode === "same_seed" ? "text-blue-700" : "text-gray-700"}`}>
                  原参数重拍
                </span>
              </div>
              <p className="text-[10px] text-gray-400">
                保持属性不变，更换随机种子
              </p>
            </button>
            <button
              onClick={() => setMode("tweak")}
              className={`flex-1 p-3 rounded-xl border-2 text-left transition-all ${
                mode === "tweak"
                  ? "border-blue-400 bg-blue-50"
                  : "border-gray-200 bg-white hover:bg-gray-50"
              }`}
            >
              <div className="flex items-center gap-2 mb-1">
                <svg
                  className={`w-4 h-4 ${mode === "tweak" ? "text-blue-600" : "text-gray-400"}`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
                  />
                </svg>
                <span className={`text-xs font-semibold ${mode === "tweak" ? "text-blue-700" : "text-gray-700"}`}>
                  微调重拍
                </span>
              </div>
              <p className="text-[10px] text-gray-400">
                修改场景、风格等参数
              </p>
            </button>
          </div>

          {/* Tweak options */}
          {mode === "tweak" && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              className="space-y-3"
            >
              {/* Scene selection */}
              <div>
                <label className="text-xs font-semibold text-gray-700 mb-1.5 block">
                  场景 (可选)
                </label>
                <div className="flex flex-wrap gap-1.5">
                  {SCENE_OPTIONS.map((scene) => (
                    <button
                      key={scene}
                      onClick={() =>
                        setSelectedScene(
                          selectedScene === scene ? null : scene,
                        )
                      }
                      className={`px-2.5 py-1 rounded-lg text-[11px] font-medium transition-all ${
                        selectedScene === scene
                          ? "bg-blue-500 text-white"
                          : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                      }`}
                    >
                      {scene}
                    </button>
                  ))}
                </div>
              </div>

              {/* Style selection */}
              <div>
                <label className="text-xs font-semibold text-gray-700 mb-1.5 block">
                  风格 (可选)
                </label>
                <div className="flex flex-wrap gap-1.5">
                  {STYLE_OPTIONS.map((style) => (
                    <button
                      key={style}
                      onClick={() =>
                        setSelectedStyle(
                          selectedStyle === style ? null : style,
                        )
                      }
                      className={`px-2.5 py-1 rounded-lg text-[11px] font-medium transition-all ${
                        selectedStyle === style
                          ? "bg-purple-500 text-white"
                          : "bg-gray-100 text-gray-600 hover:bg-gray-200"
                      }`}
                    >
                      {style}
                    </button>
                  ))}
                </div>
              </div>
            </motion.div>
          )}
        </div>

        {/* Actions */}
        <div className="border-t border-gray-100 p-4 flex justify-end gap-2">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm text-gray-600 bg-gray-100 rounded-xl hover:bg-gray-200 font-medium transition-colors"
          >
            取消
          </button>
          <button
            onClick={handleSubmit}
            disabled={regenerating}
            className="px-5 py-2 text-sm text-white bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl hover:from-blue-700 hover:to-blue-800 font-semibold shadow-sm disabled:opacity-50 transition-all flex items-center gap-2"
          >
            {regenerating ? (
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
              "开始重生成"
            )}
          </button>
        </div>
      </motion.div>
    </motion.div>
  );
}
