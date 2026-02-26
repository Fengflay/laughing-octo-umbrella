"use client";

import { motion } from "framer-motion";
import { useStoryboard, IMAGE_TYPE_LABELS } from "@/lib/storyboard-context";

export default function GenerationProgressV2() {
  const { cells } = useStoryboard();

  const completedCount = cells.filter((c) => c.status === "completed").length;
  const totalCount = cells.length;
  const percent =
    totalCount > 0 ? Math.round((completedCount / totalCount) * 100) : 0;
  const allDone = completedCount === totalCount;

  return (
    <div className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm space-y-5">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          {allDone ? (
            <div className="w-6 h-6 rounded-full bg-emerald-500 flex items-center justify-center">
              <svg
                className="w-3.5 h-3.5 text-white"
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
            </div>
          ) : (
            <div className="relative w-6 h-6">
              <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
              <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
            </div>
          )}
          <h2 className="text-base font-bold text-gray-800">
            {allDone ? "生成完成" : "高清渲染中"}
          </h2>
        </div>
        <span className="text-sm font-semibold text-blue-600">
          {completedCount}/{totalCount} ({percent}%)
        </span>
      </div>

      {/* Global progress bar */}
      <div className="w-full bg-gray-100 rounded-full h-2.5 overflow-hidden">
        <motion.div
          className="bg-gradient-to-r from-blue-500 to-blue-600 h-full rounded-full relative"
          initial={{ width: 0 }}
          animate={{ width: `${percent}%` }}
          transition={{ duration: 0.7, ease: "easeOut" }}
        >
          {percent > 0 && percent < 100 && (
            <div className="absolute inset-0 animate-shimmer rounded-full" />
          )}
        </motion.div>
      </div>

      {/* Per-cell progress grid */}
      <div className="grid grid-cols-3 gap-3">
        {cells.map((cell, i) => {
          const isGenerating = cell.status === "generating";
          const isCompleted = cell.status === "completed";
          const isFailed = cell.status === "failed";

          return (
            <motion.div
              key={cell.id}
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: i * 0.05 }}
              className={`relative aspect-square rounded-xl border-2 overflow-hidden transition-all ${
                isCompleted
                  ? "border-emerald-300 bg-emerald-50"
                  : isGenerating
                    ? "border-blue-300 bg-blue-50"
                    : isFailed
                      ? "border-red-300 bg-red-50"
                      : "border-gray-200 bg-gray-50"
              }`}
            >
              {/* Result image */}
              {isCompleted && cell.resultUrl ? (
                <img
                  src={cell.resultUrl}
                  alt={IMAGE_TYPE_LABELS[cell.imageType]}
                  className="w-full h-full object-cover"
                />
              ) : (
                <div className="flex items-center justify-center h-full">
                  <div className="text-center space-y-1.5">
                    {isGenerating ? (
                      <>
                        {/* Circular progress */}
                        <div className="relative w-10 h-10 mx-auto">
                          <svg className="w-10 h-10 -rotate-90" viewBox="0 0 40 40">
                            <circle
                              cx="20"
                              cy="20"
                              r="16"
                              fill="none"
                              stroke="#dbeafe"
                              strokeWidth="3"
                            />
                            <motion.circle
                              cx="20"
                              cy="20"
                              r="16"
                              fill="none"
                              stroke="#3b82f6"
                              strokeWidth="3"
                              strokeLinecap="round"
                              strokeDasharray={100}
                              initial={{ strokeDashoffset: 100 }}
                              animate={{
                                strokeDashoffset: 100 - cell.progress,
                              }}
                              transition={{ duration: 0.5 }}
                            />
                          </svg>
                          <span className="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-blue-600">
                            {cell.progress}%
                          </span>
                        </div>
                        <p className="text-[10px] text-blue-500 font-medium">
                          渲染中
                        </p>
                      </>
                    ) : isFailed ? (
                      <>
                        <svg
                          className="w-7 h-7 mx-auto text-red-400"
                          fill="none"
                          stroke="currentColor"
                          viewBox="0 0 24 24"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                          />
                        </svg>
                        <p className="text-[10px] text-red-500 font-medium">
                          失败
                        </p>
                      </>
                    ) : (
                      <>
                        <div className="w-8 h-8 mx-auto rounded-full border-2 border-dashed border-gray-300 flex items-center justify-center">
                          <span className="text-gray-400 text-xs font-medium">
                            {i + 1}
                          </span>
                        </div>
                        <p className="text-[10px] text-gray-400">等待中</p>
                      </>
                    )}
                  </div>
                </div>
              )}

              {/* Type label overlay */}
              <div className="absolute bottom-1.5 left-1.5">
                <span className="inline-flex px-1.5 py-0.5 rounded text-[9px] font-medium bg-black/40 text-white backdrop-blur-sm">
                  #{i + 1} {IMAGE_TYPE_LABELS[cell.imageType]}
                </span>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
