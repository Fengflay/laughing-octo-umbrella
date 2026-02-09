"use client";

import { useCallback, useRef, useState } from "react";
import { compositeGrid } from "@/lib/api";
import type { GeneratedImage } from "@/types";

interface DetailGridBuilderProps {
  images: GeneratedImage[];
  taskId: string;
}

type LayoutMode = "grid3x3" | "detail_long" | "hero_center";
type ExportMode = "server" | "client";

const LAYOUTS: { id: LayoutMode; name: string; desc: string; icon: string }[] = [
  { id: "grid3x3", name: "3x3 九宮格", desc: "經典社群媒體佈局", icon: "⊞" },
  { id: "detail_long", name: "詳情長圖", desc: "電商豎版長圖", icon: "▥" },
  { id: "hero_center", name: "主圖高亮", desc: "主圖放大+細節環繞", icon: "◫" },
];

export default function DetailGridBuilder({ images, taskId }: DetailGridBuilderProps) {
  const [layout, setLayout] = useState<LayoutMode>("grid3x3");
  const [imageOrder, setImageOrder] = useState<number[]>(() =>
    images.map((_, i) => i)
  );
  const [dragIdx, setDragIdx] = useState<number | null>(null);
  const [exporting, setExporting] = useState(false);
  const [exportMode, setExportMode] = useState<ExportMode>("server");
  const [collapsed, setCollapsed] = useState(false);
  const canvasRef = useRef<HTMLCanvasElement>(null);

  const completedImages = images.filter((img) => img.status === "completed" && img.url);

  // Drag & drop reordering
  const handleDragStart = useCallback((idx: number) => {
    setDragIdx(idx);
  }, []);

  const handleDragOver = useCallback((e: React.DragEvent, idx: number) => {
    e.preventDefault();
    if (dragIdx === null || dragIdx === idx) return;
    setImageOrder((prev) => {
      const next = [...prev];
      const dragItem = next[dragIdx];
      next.splice(dragIdx, 1);
      next.splice(idx, 0, dragItem);
      return next;
    });
    setDragIdx(idx);
  }, [dragIdx]);

  const handleDragEnd = useCallback(() => {
    setDragIdx(null);
  }, []);

  // Get ordered template IDs for server-side composite
  const getOrderedTemplateIds = useCallback(() => {
    return imageOrder
      .map((i) => images[i])
      .filter((img) => img && img.status === "completed" && img.url)
      .map((img) => img.template_id);
  }, [imageOrder, images]);

  // Server-side composite export
  const handleServerExport = useCallback(async () => {
    if (completedImages.length === 0) return;
    setExporting(true);

    try {
      const orderedIds = getOrderedTemplateIds();
      const blob = await compositeGrid(taskId, {
        layout,
        image_order: orderedIds,
        cell_size: 800,
        gap: 8,
      });

      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `product_grid_${taskId}_${layout}.png`;
      a.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      console.error("Server composite failed:", err);
      // Fall back to client-side
      await handleClientExport();
    } finally {
      setExporting(false);
    }
  }, [completedImages, taskId, layout, getOrderedTemplateIds]);

  // Client-side canvas export (fallback)
  const handleClientExport = useCallback(async () => {
    if (completedImages.length === 0) return;
    setExporting(true);

    try {
      const canvas = canvasRef.current;
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      if (!ctx) return;

      const count = Math.min(completedImages.length, 9);
      const cols = 3;
      const cellSize = 800;
      const gap = 8;

      const loadImg = (url: string): Promise<HTMLImageElement> =>
        new Promise((resolve, reject) => {
          const img = new window.Image();
          img.crossOrigin = "anonymous";
          img.onload = () => resolve(img);
          img.onerror = reject;
          img.src = url;
        });

      const orderedImages = imageOrder
        .map((i) => images[i])
        .filter((img) => img.status === "completed" && img.url);

      if (layout === "detail_long") {
        // --- True vertical long image: single column, preserve aspect ratio ---
        const targetW = cellSize;
        const loaded: HTMLImageElement[] = [];
        for (const img of orderedImages.slice(0, count)) {
          if (!img.url) continue;
          try {
            loaded.push(await loadImg(img.url));
          } catch {
            // skip failed images
          }
        }
        // Calculate scaled heights
        const scaledHeights = loaded.map((img) => {
          const scale = targetW / img.width;
          return Math.round(img.height * scale);
        });
        const totalH = scaledHeights.reduce((s, h) => s + h, 0) + gap * (loaded.length - 1);
        canvas.width = targetW;
        canvas.height = totalH;
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(0, 0, targetW, totalH);

        let yOffset = 0;
        for (let i = 0; i < loaded.length; i++) {
          const img = loaded[i];
          const h = scaledHeights[i];
          ctx.drawImage(img, 0, 0, img.width, img.height, 0, yOffset, targetW, h);
          yOffset += h + gap;
        }
      } else {
        // --- grid3x3 & hero_center ---
        const rows = layout === "hero_center" ? 3 : Math.ceil(count / cols);
        const totalW = cols * cellSize + (cols - 1) * gap;
        const totalH = rows * cellSize + (rows - 1) * gap;
        canvas.width = totalW;
        canvas.height = totalH;
        ctx.fillStyle = "#ffffff";
        ctx.fillRect(0, 0, totalW, totalH);

        for (let i = 0; i < Math.min(orderedImages.length, count); i++) {
          const img = orderedImages[i];
          if (!img.url) continue;

          try {
            const loadedImg = await loadImg(img.url);

            let col: number, row: number, w: number, h: number;

            if (layout === "hero_center" && i === 0) {
              col = 0; row = 0;
              w = cellSize * 2 + gap; h = cellSize * 2 + gap;
            } else if (layout === "hero_center" && i > 0) {
              const positions = [
                [2, 0], [2, 1], [2, 2],
                [0, 2], [1, 2],
              ];
              const pos = positions[(i - 1) % positions.length];
              col = pos[0]; row = pos[1];
              w = cellSize; h = cellSize;
            } else {
              col = i % cols;
              row = Math.floor(i / cols);
              w = cellSize; h = cellSize;
            }

            const x = col * (cellSize + gap);
            const y = row * (cellSize + gap);

            const scale = Math.max(w / loadedImg.width, h / loadedImg.height);
            const sw = w / scale;
            const sh = h / scale;
            const sx = (loadedImg.width - sw) / 2;
            const sy = (loadedImg.height - sh) / 2;
            ctx.drawImage(loadedImg, sx, sy, sw, sh, x, y, w, h);
          } catch {
            ctx.fillStyle = "#f3f4f6";
            const col2 = i % cols;
            const row2 = Math.floor(i / cols);
            ctx.fillRect(col2 * (cellSize + gap), row2 * (cellSize + gap), cellSize, cellSize);
          }
        }
      }

      canvas.toBlob((blob) => {
        if (!blob) return;
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = `product_grid_${taskId}_${layout}.png`;
        a.click();
        URL.revokeObjectURL(url);
      }, "image/png");
    } catch (err) {
      console.error("Client export failed:", err);
    } finally {
      setExporting(false);
    }
  }, [completedImages, imageOrder, images, layout, taskId]);

  const handleExport = exportMode === "server" ? handleServerExport : handleClientExport;

  if (completedImages.length === 0) return null;

  return (
    <div className="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm">
      {/* Header — collapsible */}
      <button
        onClick={() => setCollapsed(!collapsed)}
        className="w-full flex items-center justify-between px-5 py-4 hover:bg-gray-50 transition-colors"
      >
        <div className="flex items-center gap-3">
          <span className="text-xl">🖼️</span>
          <div className="text-left">
            <h2 className="text-base font-semibold text-gray-800">九宮格 / 詳情圖構建器</h2>
            <p className="text-xs text-gray-400">拖拽調整順序，選擇佈局後導出合成圖</p>
          </div>
        </div>
        <svg
          className={`w-5 h-5 text-gray-400 transition-transform duration-300 ${collapsed ? "" : "rotate-180"}`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {!collapsed && (
        <div className="px-5 pb-5 space-y-4">
          {/* Layout selector */}
          <div className="flex gap-2">
            {LAYOUTS.map((l) => (
              <button
                key={l.id}
                onClick={() => setLayout(l.id)}
                className={`flex-1 px-3 py-2.5 rounded-xl text-center transition-all ${
                  layout === l.id
                    ? "bg-blue-50 border-2 border-blue-400 text-blue-700 shadow-sm"
                    : "bg-gray-50 border border-gray-200 text-gray-600 hover:border-gray-300 hover:bg-gray-100"
                }`}
              >
                <div className="text-lg">{l.icon}</div>
                <div className="text-sm font-medium mt-0.5">{l.name}</div>
                <div className="text-[10px] text-gray-400 mt-0.5">{l.desc}</div>
              </button>
            ))}
          </div>

          {/* Preview grid with drag reorder */}
          <div className={`grid gap-1.5 bg-gray-100 p-2 rounded-xl ${
            layout === "detail_long"
              ? "grid-cols-1 max-w-[280px] mx-auto"
              : layout === "hero_center"
                ? "grid-cols-3 grid-rows-3"
                : "grid-cols-3"
          }`}>
            {imageOrder.slice(0, 9).map((origIdx, displayIdx) => {
              const img = images[origIdx];
              if (!img || img.status !== "completed" || !img.url) {
                return (
                  <div
                    key={displayIdx}
                    className="aspect-square bg-gray-200 rounded-lg flex items-center justify-center"
                  >
                    <span className="text-gray-400 text-xs">空</span>
                  </div>
                );
              }

              const isHero = layout === "hero_center" && displayIdx === 0;

              return (
                <div
                  key={img.template_id}
                  draggable
                  onDragStart={() => handleDragStart(displayIdx)}
                  onDragOver={(e) => handleDragOver(e, displayIdx)}
                  onDragEnd={handleDragEnd}
                  className={`
                    relative overflow-hidden rounded-lg cursor-move
                    transition-all duration-200
                    ${isHero ? "col-span-2 row-span-2" : "aspect-square"}
                    ${dragIdx === displayIdx ? "opacity-50 scale-95" : "hover:ring-2 hover:ring-blue-300"}
                  `}
                >
                  <img
                    src={img.url}
                    alt={img.template_name}
                    className="w-full h-full object-cover"
                    draggable={false}
                  />
                  <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/60 to-transparent text-white text-[10px] px-1.5 py-1 text-center truncate">
                    {img.template_name}
                  </div>
                  <div className="absolute top-1 left-1 bg-black/50 backdrop-blur-sm text-white text-[10px] w-5 h-5 rounded-full flex items-center justify-center font-medium">
                    {displayIdx + 1}
                  </div>
                </div>
              );
            })}
          </div>

          {/* Export controls */}
          <div className="flex gap-2 items-center">
            {/* Export mode toggle */}
            <div className="flex rounded-lg border border-gray-200 text-xs overflow-hidden">
              <button
                onClick={() => setExportMode("server")}
                className={`px-3 py-1.5 transition-colors ${
                  exportMode === "server"
                    ? "bg-blue-500 text-white"
                    : "bg-white text-gray-500 hover:bg-gray-50"
                }`}
              >
                伺服器合成
              </button>
              <button
                onClick={() => setExportMode("client")}
                className={`px-3 py-1.5 transition-colors ${
                  exportMode === "client"
                    ? "bg-blue-500 text-white"
                    : "bg-white text-gray-500 hover:bg-gray-50"
                }`}
              >
                本地合成
              </button>
            </div>

            {/* Export button */}
            <button
              onClick={handleExport}
              disabled={exporting || completedImages.length === 0}
              className="flex-1 px-6 py-2.5 bg-gradient-to-r from-purple-500 to-pink-500 text-white font-semibold rounded-xl hover:from-purple-600 hover:to-pink-600 shadow-md hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed text-sm"
            >
              {exporting ? (
                <span className="flex items-center justify-center gap-2">
                  <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  合成中...
                </span>
              ) : (
                <span className="flex items-center justify-center gap-2">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  導出{LAYOUTS.find(l => l.id === layout)?.name}合成圖
                </span>
              )}
            </button>
          </div>
        </div>
      )}

      {/* Hidden canvas for client-side export */}
      <canvas ref={canvasRef} className="hidden" />
    </div>
  );
}
