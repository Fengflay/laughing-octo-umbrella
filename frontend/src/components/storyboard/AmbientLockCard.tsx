"use client";

import { motion, AnimatePresence } from "framer-motion";
import {
  AMBIENT_PRESETS,
  useStoryboard,
} from "@/lib/storyboard-context";

export default function AmbientLockCard() {
  const {
    selectedAmbient,
    ambientLocked,
    setSelectedAmbient,
    setAmbientLocked,
  } = useStoryboard();

  const currentPreset = AMBIENT_PRESETS.find((p) => p.id === selectedAmbient);

  return (
    <div className="bg-white rounded-2xl border border-gray-200/80 shadow-sm overflow-hidden">
      {/* Header */}
      <div className="p-4 border-b border-gray-100">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center">
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
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
            </div>
            <div>
              <h3 className="text-sm font-bold text-gray-800">环境氛围</h3>
              <p className="text-[10px] text-gray-400">统一 9 张图的色温明暗</p>
            </div>
          </div>
          <button
            onClick={() => setAmbientLocked(!ambientLocked)}
            className={`flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
              ambientLocked
                ? "bg-amber-50 text-amber-700 border border-amber-200"
                : "bg-gray-50 text-gray-500 border border-gray-200 hover:bg-gray-100"
            }`}
          >
            {ambientLocked ? (
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
                  d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
                />
              </svg>
            ) : (
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
                  d="M8 11V7a4 4 0 118 0m-4 8v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2z"
                />
              </svg>
            )}
            {ambientLocked ? "已锁定" : "未锁定"}
          </button>
        </div>
      </div>

      {/* Current Selection */}
      <AnimatePresence mode="wait">
        {currentPreset && (
          <motion.div
            key={currentPreset.id}
            initial={{ opacity: 0, y: 4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -4 }}
            className="p-4 border-b border-gray-100"
          >
            <div className="flex items-center gap-3">
              <div
                className="w-12 h-12 rounded-xl shadow-inner shrink-0"
                style={{ background: currentPreset.colorTemp }}
              />
              <div className="min-w-0">
                <p className="text-sm font-semibold text-gray-800">
                  {currentPreset.name}
                </p>
                <p className="text-xs text-gray-400 truncate">
                  {currentPreset.description}
                </p>
              </div>
              {ambientLocked && (
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  className="ml-auto shrink-0"
                >
                  <div className="w-6 h-6 rounded-full bg-amber-100 flex items-center justify-center">
                    <svg
                      className="w-3 h-3 text-amber-600"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fillRule="evenodd"
                        d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </div>
                </motion.div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Preset Grid */}
      <div className="p-3 grid grid-cols-3 gap-2">
        {AMBIENT_PRESETS.map((preset) => {
          const isSelected = selectedAmbient === preset.id;
          return (
            <motion.button
              key={preset.id}
              whileHover={{ scale: 1.03 }}
              whileTap={{ scale: 0.97 }}
              onClick={() => setSelectedAmbient(preset.id)}
              className={`relative rounded-xl p-2 text-center transition-all ${
                isSelected
                  ? "bg-blue-50 border-2 border-blue-400 shadow-sm"
                  : "bg-gray-50 border-2 border-transparent hover:bg-gray-100"
              }`}
            >
              <div
                className="w-full aspect-square rounded-lg mb-1.5 shadow-inner"
                style={{ background: preset.colorTemp }}
              />
              <p
                className={`text-[10px] font-medium leading-tight ${
                  isSelected ? "text-blue-700" : "text-gray-600"
                }`}
              >
                {preset.name}
              </p>
              {isSelected && (
                <motion.div
                  layoutId="ambient-check"
                  className="absolute top-1 right-1 w-4 h-4 bg-blue-500 rounded-full flex items-center justify-center"
                >
                  <svg
                    className="w-2.5 h-2.5 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={3}
                      d="M5 13l4 4L19 7"
                    />
                  </svg>
                </motion.div>
              )}
            </motion.button>
          );
        })}
      </div>
    </div>
  );
}
