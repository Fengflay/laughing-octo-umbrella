"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { StoryboardProvider, useStoryboard } from "@/lib/storyboard-context";
import StoryboardGrid from "@/components/storyboard/StoryboardGrid";
import AmbientLockCard from "@/components/storyboard/AmbientLockCard";
import GenerationProgressV2 from "@/components/storyboard/GenerationProgressV2";
import {
  generatePreview,
  confirmGeneration,
  subscribeToGeneration,
} from "@/lib/api";
import type { SSEEvent } from "@/types";

function StoryboardContent() {
  const router = useRouter();
  const {
    cells,
    setCells,
    updateCellStatus,
    phase,
    setPhase,
    taskId,
    setTaskId,
    selectedAmbient,
    ambientLocked,
    wizardData,
  } = useStoryboard();

  const [loadingPreview, setLoadingPreview] = useState(false);
  const [confirming, setConfirming] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Load previews on mount
  useEffect(() => {
    if (phase !== "storyboard") return;
    // Auto-generate previews with placeholder data
    const loadPreviews = async () => {
      setLoadingPreview(true);
      try {
        const result = await generatePreview({
          image_id: wizardData?.imageId || "demo",
          product_type: wizardData?.productType || "general",
          remove_bg: wizardData?.removeBg ?? true,
          style: wizardData?.style,
          ambient: selectedAmbient || undefined,
          cells: cells.map((c) => ({
            index: c.index,
            image_type: c.imageType,
          })),
        });
        setCells(
          cells.map((cell) => {
            const preview = result.previews.find(
              (p) => p.index === cell.index,
            );
            return preview
              ? { ...cell, previewUrl: preview.preview_url, status: "preview" as const }
              : cell;
          }),
        );
      } catch (err) {
        setError(err instanceof Error ? err.message : "预览加载失败");
      } finally {
        setLoadingPreview(false);
      }
    };
    loadPreviews();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const handleConfirmGenerate = useCallback(async () => {
    setConfirming(true);
    setError(null);

    try {
      const result = await confirmGeneration({
        task_id: taskId || `gen-${Date.now()}`,
        ambient: ambientLocked ? (selectedAmbient || undefined) : undefined,
        cells: cells.map((c) => ({
          index: c.index,
          image_type: c.imageType,
        })),
      });

      setTaskId(result.task_id);
      setPhase("generating");

      // Set all cells to generating
      cells.forEach((cell) => {
        updateCellStatus(cell.id, "generating", { progress: 0 });
      });

      // Demo image pool — curated e-commerce product photography from Unsplash
      const DEMO_IMAGES: Record<string, string[]> = {
        white_bg: [
          // 白底圖：白色背景產品正面展示
          "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=800&fit=crop",
        ],
        scene: [
          // 場景圖：生活情境中的產品展示
          "https://images.unsplash.com/photo-1491553895911-0055eca6402d?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1560343090-f0409e92791a?w=800&h=800&fit=crop",
        ],
        detail: [
          // 細節圖：產品材質工藝特寫
          "https://images.unsplash.com/photo-1547949003-9792a18a2601?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1588186939549-c2b4b9df1f69?w=800&h=800&fit=crop",
        ],
        material: [
          // 材質圖：面料質地紋理展示
          "https://images.unsplash.com/photo-1558171813-4c088753af8f?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=800&h=800&fit=crop",
        ],
        flat_lay: [
          // 平鋪圖：俯拍產品搭配陳列
          "https://images.unsplash.com/photo-1512374382149-233c42b6a83b?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1556906781-9a412961c28c?w=800&h=800&fit=crop",
        ],
        model: [
          // 模特圖：模特穿搭展示
          "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=800&h=800&fit=crop",
          "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=800&h=800&fit=crop",
        ],
      };

      const getDemoImage = (imageType: string, idx: number) => {
        const pool = DEMO_IMAGES[imageType] || DEMO_IMAGES.scene;
        return pool[idx % pool.length];
      };

      // Simulate rendering progress for each cell
      let completedCount = 0;
      const totalCells = cells.length;

      const interval = setInterval(() => {
        if (completedCount >= totalCells) {
          clearInterval(interval);
          setPhase("results");

          // Persist cells & taskId to sessionStorage for the Results page
          try {
            sessionStorage.setItem(
              "storyboard_results",
              JSON.stringify({ taskId: result.task_id, cells }),
            );
          } catch {
            // ignore storage errors
          }

          router.push("/results");
          return;
        }

        const currentCell = cells[completedCount];
        if (currentCell) {
          updateCellStatus(currentCell.id, "completed", {
            progress: 100,
            resultUrl: getDemoImage(currentCell.imageType, completedCount),
          });
          completedCount++;
        }
      }, 800);
    } catch (err) {
      setError(err instanceof Error ? err.message : "生成启动失败");
      setPhase("storyboard");
    } finally {
      setConfirming(false);
    }
  }, [cells, taskId, selectedAmbient, ambientLocked, router, setPhase, setTaskId, updateCellStatus]);

  // Phase: Storyboard editing
  if (phase === "storyboard") {
    return (
      <div className="space-y-6 animate-fade-in">
        {/* Top bar */}
        <div className="flex items-center justify-between">
          <a
            href="/"
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
            返回
          </a>
          <div className="flex items-center gap-2 text-xs text-gray-400">
            <span className="bg-blue-50 text-blue-500 px-2 py-0.5 rounded-full font-medium">
              故事板
            </span>
            {wizardData?.productType && (
              <span className="bg-gray-100 px-2 py-0.5 rounded-full">
                {wizardData.productType}
              </span>
            )}
          </div>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 p-3.5 rounded-xl text-sm flex items-center gap-2 animate-scale-in">
            <svg
              className="w-4 h-4 shrink-0"
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
            {error}
          </div>
        )}

        {/* Loading indicator */}
        {loadingPreview && (
          <div className="bg-blue-50 border border-blue-200 text-blue-700 p-3.5 rounded-xl text-sm flex items-center gap-2 animate-slide-up">
            <div className="relative w-4 h-4">
              <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
              <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
            </div>
            正在生成低清预览草图...
          </div>
        )}

        {/* Main content: Grid + Ambient card */}
        <div className="flex gap-5 flex-col lg:flex-row">
          {/* Grid area */}
          <div className="flex-1 min-w-0">
            <StoryboardGrid />
          </div>

          {/* Ambient lock card - sidebar */}
          <div className="w-full lg:w-72 shrink-0">
            <div className="lg:sticky lg:top-20">
              <AmbientLockCard />
            </div>
          </div>
        </div>

        {/* Confirm button */}
        <div className="text-center py-4">
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={handleConfirmGenerate}
            disabled={confirming}
            className="group relative inline-flex items-center gap-3 px-10 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white text-lg font-bold rounded-2xl hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-300 disabled:opacity-50"
          >
            {confirming ? (
              <>
                <svg
                  className="animate-spin h-5 w-5"
                  viewBox="0 0 24 24"
                >
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
                启动中...
              </>
            ) : (
              <>
                <svg
                  className="w-5 h-5 transition-transform group-hover:scale-110"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
                确认生成 9 张高清图
              </>
            )}
          </motion.button>
          <p className="text-xs text-gray-400 mt-3">
            确认后开始高清渲染，预计 2-5 分钟完成
            {ambientLocked && selectedAmbient && (
              <span className="text-amber-600"> / 氛围已锁定</span>
            )}
          </p>
        </div>
      </div>
    );
  }

  // Phase: Generating
  if (phase === "generating") {
    return (
      <div className="space-y-6 animate-fade-in">
        <div className="flex items-center justify-between">
          <h1 className="text-lg font-bold text-gray-800">高清渲染中</h1>
          <span className="text-xs text-gray-400 bg-gray-100 px-2.5 py-1 rounded-full">
            请勿离开页面
          </span>
        </div>
        <GenerationProgressV2 />
      </div>
    );
  }

  // Phase: Results -> redirect
  return null;
}

export default function StoryboardPage() {
  return (
    <StoryboardProvider>
      <StoryboardContent />
    </StoryboardProvider>
  );
}
