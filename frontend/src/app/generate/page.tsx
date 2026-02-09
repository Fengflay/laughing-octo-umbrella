"use client";

import { Suspense, useCallback, useEffect, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import TemplateGrid from "@/components/TemplateGrid";
import GenerationProgress from "@/components/GenerationProgress";
import ResultGrid from "@/components/ResultGrid";
import DownloadPanel from "@/components/DownloadPanel";
import DetailGridBuilder from "@/components/DetailGridBuilder";
import ProductDetailInput from "@/components/ProductDetailInput";
import CopywritingPanel from "@/components/CopywritingPanel";
import {
  getResults,
  getTemplates,
  startGeneration,
  subscribeToGeneration,
} from "@/lib/api";
import { saveToHistory } from "@/components/HistoryPanel";
import { useApp } from "@/lib/store";
import type { GeneratedImage, SceneTemplate, SSEEvent } from "@/types";

type Phase = "templates" | "generating" | "done";

function GenerateContent() {
  const searchParams = useSearchParams();
  const { user, refreshUser } = useApp();
  const imageId = searchParams.get("image_id") || "";
  const productType = searchParams.get("product_type") || "";
  const removeBgParam = searchParams.get("remove_bg") !== "0";
  const styleParam = searchParams.get("style") || undefined;
  const recoveryTaskId = searchParams.get("task_id") || null;

  const [templates, setTemplates] = useState<SceneTemplate[]>([]);
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [customPrompts, setCustomPrompts] = useState<Record<string, string>>({});
  const [activeSubCategory, setActiveSubCategory] = useState("all");
  const [productDetails, setProductDetails] = useState("");
  const [phase, setPhase] = useState<Phase>("templates");
  const [taskId, setTaskId] = useState<string | null>(null);
  const [progress, setProgress] = useState(0);
  const [total, setTotal] = useState(0);
  const [images, setImages] = useState<GeneratedImage[]>([]);
  const [error, setError] = useState<string | null>(null);
  const unsubRef = useRef<(() => void) | null>(null);

  useEffect(() => {
    if (productType) {
      getTemplates(productType)
        .then((t) => {
          setTemplates(t);
          // By default select only "common" templates (the universal 9)
          const commonIds = t
            .filter((tpl) => tpl.sub_category === "common")
            .map((tpl) => tpl.id);
          setSelectedIds(new Set(commonIds));
          setActiveSubCategory("all");
        })
        .catch(console.error);
    }
  }, [productType]);

  // Recovery: if task_id in URL, attempt to restore previous generation
  useEffect(() => {
    if (!recoveryTaskId) return;

    let cancelled = false;
    getResults(recoveryTaskId)
      .then((result) => {
        if (cancelled) return;
        setTaskId(recoveryTaskId);
        setImages(result.images);
        setProgress(result.progress);
        setTotal(result.total);

        if (result.status === "completed" || result.status === "partial" || result.status === "failed") {
          setPhase("done");
        } else if (result.status === "running" || result.status === "starting") {
          // Task still running — reconnect SSE
          setPhase("generating");
          const unsub = subscribeToGeneration(
            recoveryTaskId,
            (event: SSEEvent) => {
              if (event.progress !== undefined) setProgress(event.progress);
              if (event.total !== undefined) setTotal(event.total);
              if (event.results) setImages(event.results);
              if (event.event === "completed") {
                setPhase("done");
                const completedImages = (event.results || []).filter(
                  (r) => r.status === "completed",
                );
                const firstUrl = completedImages.find((r) => r.url)?.url || undefined;
                saveToHistory({
                  taskId: recoveryTaskId,
                  productType,
                  style: styleParam,
                  timestamp: Date.now(),
                  imageCount: completedImages.length,
                  firstImageUrl: firstUrl,
                });
              }
            },
            (err) => {
              setError(err.message);
              setPhase("done");
            },
          );
          unsubRef.current = unsub;
        }
      })
      .catch(() => {
        // Task not found (expired) — fall back to template selection
        if (!cancelled) {
          setPhase("templates");
        }
      });

    return () => {
      cancelled = true;
    };
  }, [recoveryTaskId]); // eslint-disable-line react-hooks/exhaustive-deps

  const handlePromptChange = useCallback(
    (templateId: string, prompt: string | null) => {
      setCustomPrompts((prev) => {
        const next = { ...prev };
        if (prompt === null) {
          delete next[templateId];
        } else {
          next[templateId] = prompt;
        }
        return next;
      });
    },
    [],
  );

  const handleToggleSelect = useCallback((templateId: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(templateId)) {
        next.delete(templateId);
      } else {
        next.add(templateId);
      }
      return next;
    });
  }, []);

  const handleSelectAll = useCallback(() => {
    setSelectedIds(new Set(templates.map((t) => t.id)));
  }, [templates]);

  const handleSelectNone = useCallback(() => {
    setSelectedIds(new Set());
  }, []);

  const handleImageUpdated = useCallback((updatedImage: GeneratedImage) => {
    setImages((prev) =>
      prev.map((img) =>
        img.template_id === updatedImage.template_id
          ? { ...updatedImage, url: updatedImage.url ? `${updatedImage.url}?t=${Date.now()}` : null }
          : img,
      ),
    );
  }, []);

  const selectedCount = selectedIds.size;

  const handleGenerate = useCallback(async () => {
    if (selectedCount === 0) {
      setError("請至少選擇一個場景模板");
      return;
    }

    setError(null);
    setPhase("generating");

    try {
      const templateOverrides = Object.entries(customPrompts)
        .filter(([id]) => selectedIds.has(id))
        .map(([template_id, custom_prompt]) => ({ template_id, custom_prompt }));

      const selectedTemplateIds = Array.from(selectedIds);

      const task = await startGeneration({
        image_id: imageId,
        product_type: productType,
        remove_bg: removeBgParam,
        style: styleParam,
        templates: templateOverrides.length > 0 ? templateOverrides : undefined,
        selected_template_ids: selectedTemplateIds.length < templates.length ? selectedTemplateIds : undefined,
      });

      setTaskId(task.task_id);
      setTotal(task.total);

      // Refresh user credits after charge
      refreshUser();

      const selectedTemplates = templates.filter((t) => selectedIds.has(t.id));
      const initialImages: GeneratedImage[] = selectedTemplates.map((t) => ({
        template_id: t.id,
        template_name: t.name,
        status: "pending" as const,
        url: null,
        error: null,
      }));
      setImages(initialImages);

      // Persist taskId in URL hash for refresh recovery
      window.history.replaceState(
        null,
        "",
        `${window.location.pathname}?${searchParams.toString()}&task_id=${task.task_id}`,
      );

      const unsub = subscribeToGeneration(
        task.task_id,
        (event: SSEEvent) => {
          if (event.progress !== undefined) setProgress(event.progress);
          if (event.total !== undefined) setTotal(event.total);
          if (event.results) {
            setImages(event.results);
          }
          if (event.event === "completed") {
            setPhase("done");
            // Save to history
            const completedImages = (event.results || []).filter(
              (r) => r.status === "completed",
            );
            const firstUrl = completedImages.find((r) => r.url)?.url || undefined;
            saveToHistory({
              taskId: task.task_id,
              productType,
              style: styleParam,
              timestamp: Date.now(),
              imageCount: completedImages.length,
              firstImageUrl: firstUrl,
            });
          }
        },
        (err) => {
          setError(err.message);
          setPhase("done");
        },
      );
      unsubRef.current = unsub;
    } catch (err) {
      setError(err instanceof Error ? err.message : "生成失敗");
      setPhase("templates");
    }
  }, [imageId, productType, removeBgParam, styleParam, customPrompts, templates, selectedIds, selectedCount]);

  useEffect(() => {
    return () => {
      if (unsubRef.current) unsubRef.current();
    };
  }, []);

  const hasCompletedImages = images.some((img) => img.status === "completed");

  // Guard: missing required params
  if (!imageId || !productType) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-4 animate-fade-in">
        <div className="w-16 h-16 bg-gray-100 rounded-2xl flex items-center justify-center">
          <svg className="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
          </svg>
        </div>
        <div className="text-center">
          <p className="text-gray-600 text-lg font-semibold">缺少必要參數</p>
          <p className="text-gray-400 text-sm mt-1">請先上傳產品圖片並選擇產品類型</p>
        </div>
        <a
          href="/"
          className="px-6 py-2.5 bg-blue-600 text-white rounded-xl hover:bg-blue-700 font-medium transition-colors"
        >
          返回首頁上傳
        </a>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Top bar */}
      <div className="flex items-center justify-between">
        <a
          href="/"
          className="text-gray-500 hover:text-blue-600 text-sm flex items-center gap-1.5 transition-colors"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          返回
        </a>
        <div className="flex items-center gap-2 text-xs text-gray-400">
          <span className="bg-gray-100 px-2 py-0.5 rounded-full">{productType}</span>
          {styleParam && <span className="bg-purple-50 text-purple-500 px-2 py-0.5 rounded-full">{styleParam}</span>}
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3.5 rounded-xl text-sm flex items-center gap-2 animate-scale-in">
          <svg className="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {error}
        </div>
      )}

      {/* Phase: Templates */}
      {phase === "templates" && templates.length > 0 && (
        <div className="space-y-6 animate-fade-in">
          {/* Product Details Input */}
          <div className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm">
            <ProductDetailInput
              value={productDetails}
              onChange={setProductDetails}
              productType={productType}
            />
          </div>

          <div className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm">
            <TemplateGrid
              templates={templates}
              selectedIds={selectedIds}
              customPrompts={customPrompts}
              activeSubCategory={activeSubCategory}
              onSubCategoryChange={setActiveSubCategory}
              onPromptChange={handlePromptChange}
              onToggleSelect={handleToggleSelect}
              onSelectAll={handleSelectAll}
              onSelectNone={handleSelectNone}
            />
          </div>
          <div className="text-center space-y-2">
            <button
              onClick={handleGenerate}
              disabled={selectedCount === 0 || (user !== null && user.credits < selectedCount)}
              className="group inline-flex items-center gap-3 px-10 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white text-lg font-bold rounded-2xl hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:translate-y-0"
            >
              <svg className="w-5 h-5 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              開始生成 {selectedCount} 張圖
              {selectedCount > 0 && (
                <span className="text-sm opacity-80 font-normal">
                  ({selectedCount} 點)
                </span>
              )}
            </button>
            {selectedCount === 0 && (
              <p className="text-sm text-gray-400">請至少勾選一個場景模板</p>
            )}
            {user && selectedCount > 0 && (
              <p className="text-xs text-gray-400">
                消耗 <span className="text-amber-600 font-medium">{selectedCount} 點</span>
                {" · "}
                目前餘額 <span className={`font-medium ${user.credits < selectedCount ? "text-red-500" : "text-amber-600"}`}>{user.credits} 點</span>
                {user.credits < selectedCount && (
                  <span className="text-red-500 ml-1">（點數不足）</span>
                )}
              </p>
            )}
            {!user && (
              <p className="text-xs text-gray-400">
                需要<a href="/login" className="text-blue-500 hover:text-blue-600 mx-0.5">登入</a>才能生成圖片
              </p>
            )}
          </div>
        </div>
      )}

      {/* Phase: Generating */}
      {phase === "generating" && (
        <div className="space-y-6 animate-fade-in">
          <div className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm">
            <GenerationProgress progress={progress} total={total} images={images} />
          </div>
          <ResultGrid images={images} taskId={taskId || ""} />
        </div>
      )}

      {/* Phase: Done */}
      {phase === "done" && (
        <div className="space-y-6 animate-fade-in">
          <ResultGrid
            images={images}
            taskId={taskId || ""}
            onImageUpdated={handleImageUpdated}
          />
          <CopywritingPanel
            productDetails={productDetails}
            productType={productType}
            templates={templates}
            images={images}
          />
          <DetailGridBuilder images={images} taskId={taskId || ""} />
          <DownloadPanel taskId={taskId || ""} hasResults={hasCompletedImages} />

          <div className="flex items-center justify-center gap-3 py-2">
            <button
              onClick={() => {
                setPhase("templates");
                setImages([]);
                setProgress(0);
              }}
              className="px-6 py-2.5 bg-white border border-gray-200 text-gray-700 rounded-xl hover:bg-gray-50 hover:border-gray-300 transition-all font-medium text-sm"
            >
              重新生成
            </button>
            <a
              href="/"
              className="inline-flex items-center gap-2 px-6 py-2.5 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-colors font-medium text-sm"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
              </svg>
              上傳新產品
            </a>
          </div>
        </div>
      )}
    </div>
  );
}

export default function GeneratePage() {
  return (
    <Suspense
      fallback={
        <div className="flex items-center justify-center h-64">
          <div className="flex flex-col items-center gap-3">
            <div className="relative w-8 h-8">
              <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
              <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
            </div>
            <p className="text-gray-400 text-sm">載入中...</p>
          </div>
        </div>
      }
    >
      <GenerateContent />
    </Suspense>
  );
}
