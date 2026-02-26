"use client";

import { useCallback, useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  StoryboardProvider,
  useStoryboard,
  IMAGE_TYPE_LABELS,
  type GridCell,
  type ImageType,
} from "@/lib/storyboard-context";
import InpaintCanvas from "@/components/storyboard/InpaintCanvas";
import RegeneratePanel from "@/components/storyboard/RegeneratePanel";
import AdditionalGenPanel from "@/components/storyboard/AdditionalGenPanel";
import {
  regenerateSingle,
  inpaintImage,
  generateAdditional,
} from "@/lib/api";

// ---------------------------------------------------------------------------
// Mock data for demo (when navigated directly)
// ---------------------------------------------------------------------------

// Curated e-commerce product photography from Unsplash — per image type
const DEMO_RESULT_IMAGES: Record<string, string> = {
  // #1 白底圖：手錶白色背景正面展示
  "white_bg-0": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=800&fit=crop",
  // #2 場景圖：運動鞋生活場景
  "scene-1": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=800&h=800&fit=crop",
  // #3 細節圖：服裝面料特寫
  "detail-2": "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=800&h=800&fit=crop",
  // #4 材質圖：皮革紋理質感
  "material-3": "https://images.unsplash.com/photo-1558171813-4c088753af8f?w=800&h=800&fit=crop",
  // #5 場景圖：商品零售展示空間
  "scene-4": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&h=800&fit=crop",
  // #6 平鋪圖：鞋子俯拍陳列
  "flat_lay-5": "https://images.unsplash.com/photo-1512374382149-233c42b6a83b?w=800&h=800&fit=crop",
  // #7 模特圖：時尚穿搭展示
  "model-6": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800&h=800&fit=crop",
  // #8 細節圖：牛仔布料紋理
  "detail-7": "https://images.unsplash.com/photo-1588186939549-c2b4b9df1f69?w=800&h=800&fit=crop",
  // #9 場景圖：產品氛圍展示
  "scene-8": "https://images.unsplash.com/photo-1560343090-f0409e92791a?w=800&h=800&fit=crop",
};

const MOCK_RESULTS: GridCell[] = [
  "white_bg",
  "scene",
  "detail",
  "material",
  "scene",
  "flat_lay",
  "model",
  "detail",
  "scene",
].map((type, i) => ({
  id: `result-${i}`,
  index: i,
  imageType: type as ImageType,
  previewUrl: null,
  resultUrl: DEMO_RESULT_IMAGES[`${type}-${i}`] || `https://picsum.photos/seed/res_${type}_${i}/800/800`,
  status: "completed" as const,
  progress: 100,
  error: null,
  locked: i === 0,
}));

// ---------------------------------------------------------------------------
// Results content
// ---------------------------------------------------------------------------

function ResultsContent() {
  const {
    cells,
    setCells,
    updateCellStatus,
    additionalImages,
    addAdditionalImages,
    taskId,
  } = useStoryboard();

  // Try restoring cells from sessionStorage (persisted by storyboard page)
  const hasResults = cells.some((c) => c.status === "completed");

  useEffect(() => {
    if (hasResults) return;

    try {
      const stored = sessionStorage.getItem("storyboard_results");
      if (stored) {
        const parsed = JSON.parse(stored) as { taskId?: string; cells?: GridCell[] };
        if (parsed.cells && parsed.cells.length > 0) {
          setCells(parsed.cells);
          return;
        }
      }
    } catch {
      // ignore parse errors
    }

    // Fall back to mock data when nothing is available
    setCells(MOCK_RESULTS);
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const allImages = hasResults ? cells : MOCK_RESULTS;
  const displayImages = [...allImages, ...additionalImages];

  // UI state
  const [lightboxIndex, setLightboxIndex] = useState<number | null>(null);
  const [inpaintTarget, setInpaintTarget] = useState<GridCell | null>(null);
  const [regenTarget, setRegenTarget] = useState<GridCell | null>(null);
  const [additionalOpen, setAdditionalOpen] = useState(false);
  const [regenerating, setRegenerating] = useState(false);
  const [inpainting, setInpainting] = useState(false);
  const [generatingAdditional, setGeneratingAdditional] = useState(false);

  // Lightbox navigation
  const completedImages = displayImages.filter(
    (img) => img.status === "completed" && img.resultUrl,
  );

  const lightboxImage =
    lightboxIndex !== null ? completedImages[lightboxIndex] : null;

  const goToNext = useCallback(() => {
    if (lightboxIndex === null) return;
    if (lightboxIndex < completedImages.length - 1) {
      setLightboxIndex(lightboxIndex + 1);
    }
  }, [lightboxIndex, completedImages.length]);

  const goToPrev = useCallback(() => {
    if (lightboxIndex === null) return;
    if (lightboxIndex > 0) {
      setLightboxIndex(lightboxIndex - 1);
    }
  }, [lightboxIndex]);

  const closeLightbox = useCallback(() => setLightboxIndex(null), []);

  // Keyboard navigation
  useEffect(() => {
    if (lightboxIndex === null) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      switch (e.key) {
        case "Escape":
          closeLightbox();
          break;
        case "ArrowLeft":
          goToPrev();
          break;
        case "ArrowRight":
          goToNext();
          break;
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    document.body.style.overflow = "hidden";

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.body.style.overflow = "";
    };
  }, [lightboxIndex, closeLightbox, goToPrev, goToNext]);

  // Action handlers
  const handleRegenerate = useCallback(
    async (options: {
      mode: "same_seed" | "tweak";
      tweaks?: { scene?: string; style?: string; imageType?: string };
    }) => {
      if (!regenTarget) return;
      setRegenerating(true);
      try {
        const result = await regenerateSingle(
          taskId || "demo",
          regenTarget.id,
          {
            image_type: regenTarget.imageType,
            scene: options.tweaks?.scene,
            style: options.tweaks?.style,
          },
        );
        updateCellStatus(regenTarget.id, "completed", {
          resultUrl: result.url || regenTarget.resultUrl,
        });
        setRegenTarget(null);
      } catch (err) {
        console.error("Regenerate failed:", err);
      } finally {
        setRegenerating(false);
      }
    },
    [regenTarget, taskId, updateCellStatus],
  );

  const handleInpaint = useCallback(
    async (maskDataUrl: string) => {
      if (!inpaintTarget) return;
      setInpainting(true);
      try {
        const result = await inpaintImage(
          taskId || "demo",
          inpaintTarget.id,
          { mask_data: maskDataUrl },
        );
        updateCellStatus(inpaintTarget.id, "completed", {
          resultUrl: result.url || inpaintTarget.resultUrl,
        });
        setInpaintTarget(null);
      } catch (err) {
        console.error("Inpaint failed:", err);
      } finally {
        setInpainting(false);
      }
    },
    [inpaintTarget, taskId, updateCellStatus],
  );

  const handleAdditionalGen = useCallback(
    async (params: {
      imageType: ImageType;
      count: number;
      angle?: string;
      lighting?: string;
    }) => {
      setGeneratingAdditional(true);
      try {
        const result = await generateAdditional(taskId || "demo", {
          image_type: params.imageType,
          count: params.count,
          angle: params.angle,
          lighting: params.lighting,
        });
        const newCells: GridCell[] = result.images.map((img, i) => ({
          id: img.template_id,
          index: displayImages.length + i,
          imageType: params.imageType,
          previewUrl: null,
          resultUrl: img.url,
          status: "completed" as const,
          progress: 100,
          error: null,
          locked: false,
        }));
        addAdditionalImages(newCells);
        setAdditionalOpen(false);
      } catch (err) {
        console.error("Additional generation failed:", err);
      } finally {
        setGeneratingAdditional(false);
      }
    },
    [taskId, displayImages.length, addAdditionalImages],
  );

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Top bar */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <a
            href="/storyboard"
            className="text-gray-500 hover:text-blue-600 text-sm flex items-center gap-1.5 transition-colors"
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
                d="M15 19l-7-7 7-7"
              />
            </svg>
            返回故事板
          </a>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={() => setAdditionalOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-blue-600 text-white text-xs font-semibold rounded-lg hover:bg-blue-700 transition-colors shadow-sm"
          >
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
            新增图片
          </button>
        </div>
      </div>

      {/* Results header */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm">
        <div className="flex items-center gap-2.5 mb-1">
          <div className="w-7 h-7 rounded-lg bg-gradient-to-br from-emerald-500 to-emerald-600 flex items-center justify-center">
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
          <h1 className="text-base font-bold text-gray-800">
            生成结果
          </h1>
          <span className="text-xs text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
            {completedImages.length} 张
          </span>
        </div>
        <p className="text-xs text-gray-400 ml-[38px]">
          点击图片放大查看 / 悬停显示操作按钮
        </p>
      </div>

      {/* 9-grid results */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {displayImages.map((cell, globalIdx) => {
          const isCompleted =
            cell.status === "completed" && cell.resultUrl;

          return (
            <motion.div
              key={cell.id}
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: globalIdx * 0.04 }}
              className="relative aspect-square rounded-xl overflow-hidden border border-gray-200 bg-gray-100 group"
            >
              {isCompleted ? (
                <>
                  <img
                    src={cell.resultUrl!}
                    alt={IMAGE_TYPE_LABELS[cell.imageType]}
                    loading="lazy"
                    decoding="async"
                    className="w-full h-full object-cover cursor-pointer hover:scale-105 transition-transform duration-300"
                    onClick={() => {
                      const compIdx = completedImages.findIndex(
                        (c) => c.id === cell.id,
                      );
                      if (compIdx !== -1) setLightboxIndex(compIdx);
                    }}
                  />

                  {/* Bottom label */}
                  <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/60 to-transparent text-white text-xs p-3 pt-6 text-center">
                    <span className="font-medium">
                      {IMAGE_TYPE_LABELS[cell.imageType]}
                    </span>
                  </div>

                  {/* Index badge */}
                  <div className="absolute top-2 left-2 bg-black/50 text-white text-xs px-2 py-0.5 rounded-full backdrop-blur-sm">
                    #{globalIdx + 1}
                  </div>

                  {/* Action buttons on hover */}
                  <div className="absolute top-2 right-2 flex flex-col gap-1.5 opacity-0 group-hover:opacity-100 transition-opacity">
                    {/* Download */}
                    <a
                      href={cell.resultUrl!}
                      download={`${cell.imageType}-${globalIdx + 1}.png`}
                      className="bg-white/90 hover:bg-white rounded-full p-1.5 shadow-md backdrop-blur-sm"
                      onClick={(e) => e.stopPropagation()}
                      title="下载"
                    >
                      <svg
                        className="w-4 h-4 text-gray-700"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M12 10v6m0 0l-3-3m3 3l3-3M3 17v3a2 2 0 002 2h14a2 2 0 002-2v-3"
                        />
                      </svg>
                    </a>

                    {/* Regenerate */}
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setRegenTarget(cell);
                      }}
                      className="bg-white/90 hover:bg-white rounded-full p-1.5 shadow-md backdrop-blur-sm"
                      title="重新生成"
                    >
                      <svg
                        className="w-4 h-4 text-gray-700"
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
                    </button>

                    {/* Inpaint */}
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setInpaintTarget(cell);
                      }}
                      className="bg-white/90 hover:bg-white rounded-full p-1.5 shadow-md backdrop-blur-sm"
                      title="画笔修复"
                    >
                      <svg
                        className="w-4 h-4 text-gray-700"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                        />
                      </svg>
                    </button>
                  </div>
                </>
              ) : (
                <div className="flex items-center justify-center h-full">
                  <div className="text-center">
                    <div className="w-8 h-8 mx-auto rounded-full border-2 border-dashed border-gray-300 flex items-center justify-center">
                      <span className="text-gray-400 text-xs font-medium">
                        {globalIdx + 1}
                      </span>
                    </div>
                    <p className="text-xs text-gray-400 mt-2">
                      {cell.status === "failed"
                        ? "生成失败"
                        : "等待中"}
                    </p>
                  </div>
                </div>
              )}
            </motion.div>
          );
        })}

        {/* Add more button as a grid item */}
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={() => setAdditionalOpen(true)}
          className="aspect-square rounded-xl border-2 border-dashed border-gray-300 bg-gray-50 hover:bg-gray-100 hover:border-gray-400 transition-all flex items-center justify-center"
        >
          <div className="text-center space-y-2">
            <div className="w-10 h-10 mx-auto rounded-xl bg-gray-200 flex items-center justify-center">
              <svg
                className="w-5 h-5 text-gray-400"
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
            </div>
            <p className="text-xs text-gray-400 font-medium">新增图片</p>
          </div>
        </motion.button>
      </div>

      {/* Bottom actions */}
      <div className="flex items-center justify-center gap-3 py-2">
        <a
          href="/storyboard"
          className="px-6 py-2.5 bg-white border border-gray-200 text-gray-700 rounded-xl hover:bg-gray-50 hover:border-gray-300 transition-all font-medium text-sm"
        >
          返回编辑
        </a>
        <a
          href="/"
          className="inline-flex items-center gap-2 px-6 py-2.5 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-colors font-medium text-sm"
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
              d="M12 4v16m8-8H4"
            />
          </svg>
          上传新产品
        </a>
      </div>

      {/* Lightbox */}
      <AnimatePresence>
        {lightboxImage && lightboxImage.resultUrl && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black/85 z-50 flex items-center justify-center p-2 sm:p-4"
            onClick={closeLightbox}
          >
            {/* Prev button */}
            {lightboxIndex !== null && lightboxIndex > 0 && (
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  goToPrev();
                }}
                className="absolute left-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 rounded-full p-3 transition-colors backdrop-blur-sm z-10"
                title="上一张"
              >
                <svg
                  className="w-6 h-6 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M15 19l-7-7 7-7"
                  />
                </svg>
              </button>
            )}

            {/* Next button */}
            {lightboxIndex !== null &&
              lightboxIndex < completedImages.length - 1 && (
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    goToNext();
                  }}
                  className="absolute right-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 rounded-full p-3 transition-colors backdrop-blur-sm z-10"
                  title="下一张"
                >
                  <svg
                    className="w-6 h-6 text-white"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </button>
              )}

            <div
              className="relative max-w-4xl max-h-[90vh]"
              onClick={(e) => e.stopPropagation()}
            >
              <img
                src={lightboxImage.resultUrl}
                alt={IMAGE_TYPE_LABELS[lightboxImage.imageType]}
                className="max-w-full max-h-[85vh] object-contain rounded-lg shadow-2xl"
              />

              {/* Top bar with actions */}
              <div className="absolute top-0 right-0 flex gap-2 p-3">
                <a
                  href={lightboxImage.resultUrl}
                  download={`${lightboxImage.imageType}.png`}
                  className="bg-white/90 hover:bg-white rounded-full p-2 shadow-lg backdrop-blur-sm transition-colors"
                  title="下载"
                >
                  <svg
                    className="w-5 h-5 text-gray-700"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M12 10v6m0 0l-3-3m3 3l3-3M3 17v3a2 2 0 002 2h14a2 2 0 002-2v-3"
                    />
                  </svg>
                </a>
                <button
                  onClick={() => {
                    closeLightbox();
                    setRegenTarget(lightboxImage);
                  }}
                  className="bg-white/90 hover:bg-white rounded-full p-2 shadow-lg backdrop-blur-sm transition-colors"
                  title="重新生成"
                >
                  <svg
                    className="w-5 h-5 text-gray-700"
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
                </button>
                <button
                  onClick={() => {
                    closeLightbox();
                    setInpaintTarget(lightboxImage);
                  }}
                  className="bg-white/90 hover:bg-white rounded-full p-2 shadow-lg backdrop-blur-sm transition-colors"
                  title="画笔修复"
                >
                  <svg
                    className="w-5 h-5 text-gray-700"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                    />
                  </svg>
                </button>
                <button
                  onClick={closeLightbox}
                  className="bg-white/90 hover:bg-white rounded-full p-2 shadow-lg backdrop-blur-sm transition-colors"
                  title="关闭 (Esc)"
                >
                  <svg
                    className="w-5 h-5 text-gray-700"
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

              {/* Bottom info */}
              <div className="text-center mt-3 space-y-1">
                <p className="text-white text-sm font-medium">
                  {IMAGE_TYPE_LABELS[lightboxImage.imageType]}
                </p>
                <p className="text-white/50 text-xs">
                  {lightboxIndex !== null ? lightboxIndex + 1 : 0} /{" "}
                  {completedImages.length} · 使用方向键切换，Esc 关闭
                </p>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Inpaint canvas overlay */}
      <AnimatePresence>
        {inpaintTarget && inpaintTarget.resultUrl && (
          <InpaintCanvas
            imageUrl={inpaintTarget.resultUrl}
            onSubmit={handleInpaint}
            onClose={() => setInpaintTarget(null)}
            submitting={inpainting}
          />
        )}
      </AnimatePresence>

      {/* Regenerate panel */}
      <AnimatePresence>
        {regenTarget && (
          <RegeneratePanel
            imageType={regenTarget.imageType}
            onRegenerate={handleRegenerate}
            onClose={() => setRegenTarget(null)}
            regenerating={regenerating}
          />
        )}
      </AnimatePresence>

      {/* Additional generation panel */}
      <AnimatePresence>
        {additionalOpen && (
          <AdditionalGenPanel
            onGenerate={handleAdditionalGen}
            onClose={() => setAdditionalOpen(false)}
            generating={generatingAdditional}
          />
        )}
      </AnimatePresence>
    </div>
  );
}

export default function ResultsPage() {
  return (
    <StoryboardProvider>
      <ResultsContent />
    </StoryboardProvider>
  );
}
