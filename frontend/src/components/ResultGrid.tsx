"use client";

import { useCallback, useEffect, useState } from "react";
import type { GeneratedImage } from "@/types";
import { generateVariants, regenerateImage, selectVariant } from "@/lib/api";
import type { VariantResult } from "@/lib/api";

interface ResultGridProps {
  images: GeneratedImage[];
  taskId: string;
  onImageUpdated?: (updatedImage: GeneratedImage) => void;
}

export default function ResultGrid({ images, taskId, onImageUpdated }: ResultGridProps) {
  const [selectedIndex, setSelectedIndex] = useState<number | null>(null);
  const [regeneratingId, setRegeneratingId] = useState<string | null>(null);
  const [retryingAll, setRetryingAll] = useState(false);
  const [variantTemplateId, setVariantTemplateId] = useState<string | null>(null);
  const [variants, setVariants] = useState<VariantResult[]>([]);
  const [generatingVariants, setGeneratingVariants] = useState(false);
  const [selectingVariant, setSelectingVariant] = useState(false);
  const completedImages = images.filter((img) => img.status === "completed");
  const failedImages = images.filter((img) => img.status === "failed");

  // Get current lightbox image
  const selectedImage = selectedIndex !== null ? images[selectedIndex] : null;

  const handleRegenerate = async (templateId: string) => {
    setRegeneratingId(templateId);
    try {
      const updated = await regenerateImage(taskId, templateId);
      onImageUpdated?.(updated);
    } catch (err) {
      console.error("Regenerate failed:", err);
    } finally {
      setRegeneratingId(null);
    }
  };

  const handleRetryAllFailed = async () => {
    if (!onImageUpdated || failedImages.length === 0) return;
    setRetryingAll(true);
    for (const img of failedImages) {
      setRegeneratingId(img.template_id);
      try {
        const updated = await regenerateImage(taskId, img.template_id);
        onImageUpdated(updated);
      } catch (err) {
        console.error(`Retry failed for ${img.template_id}:`, err);
      }
    }
    setRegeneratingId(null);
    setRetryingAll(false);
  };

  const handleGenerateVariants = async (templateId: string) => {
    setVariantTemplateId(templateId);
    setVariants([]);
    setGeneratingVariants(true);
    try {
      const result = await generateVariants(taskId, templateId);
      setVariants(result.variants);
    } catch (err) {
      console.error("Generate variants failed:", err);
      setVariantTemplateId(null);
    } finally {
      setGeneratingVariants(false);
    }
  };

  const handleSelectVariant = async (templateId: string, variantIndex: number) => {
    if (!onImageUpdated) return;
    setSelectingVariant(true);
    try {
      const updated = await selectVariant(taskId, templateId, variantIndex);
      onImageUpdated(updated);
      setVariantTemplateId(null);
      setVariants([]);
    } catch (err) {
      console.error("Select variant failed:", err);
    } finally {
      setSelectingVariant(false);
    }
  };

  // Navigate lightbox
  const goToNext = useCallback(() => {
    if (selectedIndex === null) return;
    const nextCompleted = images.findIndex(
      (img, i) => i > selectedIndex && img.status === "completed" && img.url
    );
    if (nextCompleted !== -1) setSelectedIndex(nextCompleted);
  }, [selectedIndex, images]);

  const goToPrev = useCallback(() => {
    if (selectedIndex === null) return;
    let prevIdx = -1;
    for (let i = selectedIndex - 1; i >= 0; i--) {
      if (images[i].status === "completed" && images[i].url) {
        prevIdx = i;
        break;
      }
    }
    if (prevIdx !== -1) setSelectedIndex(prevIdx);
  }, [selectedIndex, images]);

  const closeLightbox = useCallback(() => setSelectedIndex(null), []);

  // Keyboard navigation for lightbox
  useEffect(() => {
    if (selectedIndex === null) return;

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
    // Prevent body scroll when lightbox is open
    document.body.style.overflow = "hidden";

    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.body.style.overflow = "";
    };
  }, [selectedIndex, closeLightbox, goToPrev, goToNext]);

  // Check if prev/next navigation is possible
  const hasPrev = selectedIndex !== null && images.slice(0, selectedIndex).some(img => img.status === "completed" && img.url);
  const hasNext = selectedIndex !== null && images.slice(selectedIndex + 1).some(img => img.status === "completed" && img.url);

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold">
          生成結果 ({completedImages.length}/{images.length})
        </h2>
        {onImageUpdated && failedImages.length > 0 && (
          <button
            onClick={handleRetryAllFailed}
            disabled={retryingAll}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium bg-red-50 text-red-600 border border-red-200 rounded-lg hover:bg-red-100 disabled:opacity-50 transition-colors"
          >
            {retryingAll ? (
              <>
                <svg className="animate-spin h-3.5 w-3.5" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                </svg>
                重試中...
              </>
            ) : (
              <>
                <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                重試失敗的 {failedImages.length} 張
              </>
            )}
          </button>
        )}
      </div>

      {/* Responsive Grid: 1 col mobile, 2 col tablet, 3 col desktop */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {images.map((img, i) => {
          const isRegenerating = regeneratingId === img.template_id;

          return (
            <div
              key={img.template_id}
              className="relative aspect-square rounded-xl overflow-hidden border border-gray-200 bg-gray-100 group"
            >
              {(img.status === "completed" && !isRegenerating) && img.url ? (
                <>
                  <img
                    src={img.url}
                    alt={img.template_name}
                    loading="lazy"
                    decoding="async"
                    className="w-full h-full object-cover cursor-pointer hover:scale-105 transition-transform duration-300"
                    onClick={() => setSelectedIndex(i)}
                  />
                  <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/60 to-transparent text-white text-xs p-3 pt-6 text-center">
                    <span className="font-medium">{img.template_name}</span>
                  </div>
                  {/* Action buttons - visible on hover */}
                  <div className="absolute top-2 right-2 flex gap-1.5 opacity-0 group-hover:opacity-100 transition-opacity">
                    <a
                      href={img.url}
                      download={`${img.template_id}.png`}
                      className="bg-white/90 hover:bg-white rounded-full p-1.5 shadow-md backdrop-blur-sm"
                      onClick={(e) => e.stopPropagation()}
                      title="下載此圖"
                    >
                      <svg className="w-4 h-4 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3M3 17v3a2 2 0 002 2h14a2 2 0 002-2v-3" />
                      </svg>
                    </a>
                    {onImageUpdated && (
                      <>
                        <button
                          onClick={(e) => { e.stopPropagation(); handleGenerateVariants(img.template_id); }}
                          className="bg-white/90 hover:bg-white rounded-full p-1.5 shadow-md backdrop-blur-sm"
                          title="生成 4 張變體選最佳"
                        >
                          <svg className="w-4 h-4 text-gray-700" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <rect x="2" y="2" width="20" height="20" rx="3" strokeWidth="2" />
                            <circle cx="8" cy="8" r="1.5" fill="currentColor" stroke="none" />
                            <circle cx="16" cy="8" r="1.5" fill="currentColor" stroke="none" />
                            <circle cx="8" cy="16" r="1.5" fill="currentColor" stroke="none" />
                            <circle cx="16" cy="16" r="1.5" fill="currentColor" stroke="none" />
                          </svg>
                        </button>
                        <button
                          onClick={(e) => { e.stopPropagation(); handleRegenerate(img.template_id); }}
                          className="bg-white/90 hover:bg-white rounded-full p-1.5 shadow-md backdrop-blur-sm"
                          title="重新生成此圖"
                        >
                          <svg className="w-4 h-4 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                          </svg>
                        </button>
                      </>
                    )}
                  </div>
                  {/* Sequence number badge */}
                  <div className="absolute top-2 left-2 bg-black/50 text-white text-xs px-2 py-0.5 rounded-full backdrop-blur-sm">
                    #{i + 1}
                  </div>
                </>
              ) : (img.status === "generating" || isRegenerating) ? (
                <div className="flex items-center justify-center h-full">
                  <div className="text-center">
                    <svg className="animate-spin h-8 w-8 text-blue-500 mx-auto" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                    </svg>
                    <p className="text-xs text-gray-500 mt-2">
                      #{i + 1} {isRegenerating ? "重新生成中" : "生成中"}
                    </p>
                    <p className="text-xs text-gray-400 mt-1">{img.template_name}</p>
                  </div>
                </div>
              ) : img.status === "failed" ? (
                <div className="flex items-center justify-center h-full">
                  <div className="text-center text-red-500">
                    <svg className="w-8 h-8 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <p className="text-xs mt-1 font-medium">#{i + 1} 生成失敗</p>
                    <p className="text-xs text-gray-400 mt-0.5">{img.template_name}</p>
                    {img.error && (
                      <p className="text-xs text-red-400 mt-1 max-w-[150px] truncate" title={img.error}>
                        {img.error}
                      </p>
                    )}
                    {onImageUpdated && (
                      <button
                        onClick={() => handleRegenerate(img.template_id)}
                        className="mt-2 text-xs px-3 py-1 bg-red-100 text-red-600 rounded-lg hover:bg-red-200"
                      >
                        重試
                      </button>
                    )}
                  </div>
                </div>
              ) : (
                <div className="flex items-center justify-center h-full">
                  <div className="text-center">
                    <div className="w-8 h-8 mx-auto rounded-full border-2 border-dashed border-gray-300 flex items-center justify-center">
                      <span className="text-gray-400 text-xs font-medium">{i + 1}</span>
                    </div>
                    <p className="text-xs text-gray-400 mt-2">等待中</p>
                    <p className="text-xs text-gray-300 mt-0.5">{img.template_name}</p>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Variant picker panel */}
      {variantTemplateId && (
        <div className="bg-white rounded-2xl border border-blue-200 p-4 shadow-sm animate-slide-up">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-2">
              <svg className="w-5 h-5 text-blue-500" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <rect x="2" y="2" width="20" height="20" rx="3" strokeWidth="2" />
                <circle cx="8" cy="8" r="1.5" fill="currentColor" stroke="none" />
                <circle cx="16" cy="8" r="1.5" fill="currentColor" stroke="none" />
                <circle cx="8" cy="16" r="1.5" fill="currentColor" stroke="none" />
                <circle cx="16" cy="16" r="1.5" fill="currentColor" stroke="none" />
              </svg>
              <h3 className="text-sm font-semibold text-gray-800">
                選擇最佳變體 — {images.find(img => img.template_id === variantTemplateId)?.template_name}
              </h3>
            </div>
            <button
              onClick={() => { setVariantTemplateId(null); setVariants([]); }}
              className="text-gray-400 hover:text-gray-600 transition-colors"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          {generatingVariants ? (
            <div className="flex items-center justify-center py-8">
              <div className="text-center">
                <svg className="animate-spin h-8 w-8 text-blue-500 mx-auto" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                </svg>
                <p className="text-sm text-gray-500 mt-2">正在生成 4 張變體...</p>
                <p className="text-xs text-gray-400 mt-1">預計 30-60 秒</p>
              </div>
            </div>
          ) : (
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              {variants.map((v) => (
                <div key={v.variant_index} className="relative group/variant">
                  {v.url ? (
                    <button
                      onClick={() => handleSelectVariant(variantTemplateId, v.variant_index)}
                      disabled={selectingVariant}
                      className="w-full aspect-square rounded-xl overflow-hidden border-2 border-gray-200 hover:border-blue-500 transition-all hover:shadow-md disabled:opacity-50"
                    >
                      <img
                        src={`${v.url}?t=${Date.now()}`}
                        alt={`變體 ${v.variant_index + 1}`}
                        className="w-full h-full object-cover"
                      />
                      <div className="absolute inset-0 bg-blue-500/0 group-hover/variant:bg-blue-500/10 transition-colors flex items-center justify-center">
                        <span className="opacity-0 group-hover/variant:opacity-100 transition-opacity bg-blue-500 text-white text-xs font-medium px-3 py-1 rounded-full shadow-lg">
                          {selectingVariant ? "替換中..." : "選擇此張"}
                        </span>
                      </div>
                    </button>
                  ) : (
                    <div className="w-full aspect-square rounded-xl border-2 border-red-200 flex items-center justify-center bg-red-50">
                      <p className="text-xs text-red-400">生成失敗</p>
                    </div>
                  )}
                  <p className="text-xs text-gray-400 text-center mt-1">變體 {v.variant_index + 1}</p>
                </div>
              ))}
            </div>
          )}

          <p className="text-xs text-gray-400 mt-3 text-center">
            點擊任一張變體即可替換原圖
          </p>
        </div>
      )}

      {/* Lightbox with keyboard navigation */}
      {selectedImage && selectedImage.url && (
        <div
          className="fixed inset-0 bg-black/85 z-50 flex items-center justify-center p-2 sm:p-4"
          onClick={closeLightbox}
        >
          {/* Previous button */}
          {hasPrev && (
            <button
              onClick={(e) => { e.stopPropagation(); goToPrev(); }}
              className="absolute left-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 rounded-full p-3 transition-colors backdrop-blur-sm z-10"
              title="上一張 (←)"
            >
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
            </button>
          )}

          {/* Next button */}
          {hasNext && (
            <button
              onClick={(e) => { e.stopPropagation(); goToNext(); }}
              className="absolute right-4 top-1/2 -translate-y-1/2 bg-white/20 hover:bg-white/40 rounded-full p-3 transition-colors backdrop-blur-sm z-10"
              title="下一張 (→)"
            >
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          )}

          <div className="relative max-w-4xl max-h-[90vh]" onClick={(e) => e.stopPropagation()}>
            <img
              src={selectedImage.url}
              alt={selectedImage.template_name}
              className="max-w-full max-h-[85vh] object-contain rounded-lg shadow-2xl"
            />
            {/* Top bar with actions */}
            <div className="absolute top-0 right-0 flex gap-2 p-3">
              <a
                href={selectedImage.url}
                download={`${selectedImage.template_id}.png`}
                className="bg-white/90 hover:bg-white rounded-full p-2 shadow-lg backdrop-blur-sm transition-colors"
                title="下載"
              >
                <svg className="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 10v6m0 0l-3-3m3 3l3-3M3 17v3a2 2 0 002 2h14a2 2 0 002-2v-3" />
                </svg>
              </a>
              <button
                onClick={closeLightbox}
                className="bg-white/90 hover:bg-white rounded-full p-2 shadow-lg backdrop-blur-sm transition-colors"
                title="關閉 (Esc)"
              >
                <svg className="w-5 h-5 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            {/* Bottom info */}
            <div className="text-center mt-3 space-y-1">
              <p className="text-white text-sm font-medium">
                {selectedImage.template_name}
              </p>
              <p className="text-white/50 text-xs">
                {selectedIndex !== null ? selectedIndex + 1 : 0} / {images.length} &middot; 使用 ← → 鍵切換，Esc 關閉
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
