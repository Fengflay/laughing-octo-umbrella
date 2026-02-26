"use client";

import { useCallback, useEffect, useRef, useState } from "react";

interface BrushToolProps {
  /** The background-removed image URL to draw over */
  imageUrl: string;
  /** Called when mask changes */
  onMaskChange?: (canvas: HTMLCanvasElement) => void;
}

type BrushMode = "include" | "exclude";

interface HistoryEntry {
  data: ImageData;
}

export default function BrushTool({ imageUrl, onMaskChange }: BrushToolProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [brushSize, setBrushSize] = useState(20);
  const [brushMode, setBrushMode] = useState<BrushMode>("include");
  const [history, setHistory] = useState<HistoryEntry[]>([]);
  const [historyIndex, setHistoryIndex] = useState(-1);
  const [imageLoaded, setImageLoaded] = useState(false);
  const imgRef = useRef<HTMLImageElement | null>(null);

  // Load image and initialize canvas
  useEffect(() => {
    const img = new Image();
    img.crossOrigin = "anonymous";
    img.onload = () => {
      imgRef.current = img;
      const canvas = canvasRef.current;
      if (!canvas) return;

      // Fit canvas to container width while maintaining aspect ratio
      const container = containerRef.current;
      if (!container) return;
      const containerWidth = container.clientWidth;
      const scale = containerWidth / img.width;
      canvas.width = containerWidth;
      canvas.height = img.height * scale;

      const ctx = canvas.getContext("2d");
      if (!ctx) return;

      // Draw the image
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      setImageLoaded(true);

      // Save initial state
      const initialData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      setHistory([{ data: initialData }]);
      setHistoryIndex(0);
    };
    img.src = imageUrl;
  }, [imageUrl]);

  const getCanvasPoint = useCallback(
    (e: React.MouseEvent<HTMLCanvasElement> | React.TouchEvent<HTMLCanvasElement>) => {
      const canvas = canvasRef.current;
      if (!canvas) return null;
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;

      if ("touches" in e) {
        const touch = e.touches[0];
        return {
          x: (touch.clientX - rect.left) * scaleX,
          y: (touch.clientY - rect.top) * scaleY,
        };
      }
      return {
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY,
      };
    },
    [],
  );

  const drawBrush = useCallback(
    (x: number, y: number) => {
      const canvas = canvasRef.current;
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      if (!ctx) return;

      ctx.globalCompositeOperation =
        brushMode === "include" ? "source-over" : "destination-out";

      ctx.beginPath();
      ctx.arc(x, y, brushSize, 0, Math.PI * 2);

      if (brushMode === "include") {
        // Green tint for include
        ctx.fillStyle = "rgba(34, 197, 94, 0.3)";
      } else {
        // Eraser mode
        ctx.fillStyle = "rgba(255, 255, 255, 1)";
      }
      ctx.fill();

      // Reset composite operation
      ctx.globalCompositeOperation = "source-over";
    },
    [brushMode, brushSize],
  );

  const saveHistory = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const data = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const newHistory = history.slice(0, historyIndex + 1);
    newHistory.push({ data });
    setHistory(newHistory);
    setHistoryIndex(newHistory.length - 1);

    if (onMaskChange) {
      onMaskChange(canvas);
    }
  }, [history, historyIndex, onMaskChange]);

  const handlePointerDown = useCallback(
    (e: React.MouseEvent<HTMLCanvasElement>) => {
      const point = getCanvasPoint(e);
      if (!point) return;
      setIsDrawing(true);
      drawBrush(point.x, point.y);
    },
    [getCanvasPoint, drawBrush],
  );

  const handlePointerMove = useCallback(
    (e: React.MouseEvent<HTMLCanvasElement>) => {
      if (!isDrawing) return;
      const point = getCanvasPoint(e);
      if (!point) return;
      drawBrush(point.x, point.y);
    },
    [isDrawing, getCanvasPoint, drawBrush],
  );

  const handlePointerUp = useCallback(() => {
    if (isDrawing) {
      setIsDrawing(false);
      saveHistory();
    }
  }, [isDrawing, saveHistory]);

  const handleTouchStart = useCallback(
    (e: React.TouchEvent<HTMLCanvasElement>) => {
      e.preventDefault();
      const point = getCanvasPoint(e);
      if (!point) return;
      setIsDrawing(true);
      drawBrush(point.x, point.y);
    },
    [getCanvasPoint, drawBrush],
  );

  const handleTouchMove = useCallback(
    (e: React.TouchEvent<HTMLCanvasElement>) => {
      e.preventDefault();
      if (!isDrawing) return;
      const point = getCanvasPoint(e);
      if (!point) return;
      drawBrush(point.x, point.y);
    },
    [isDrawing, getCanvasPoint, drawBrush],
  );

  const handleTouchEnd = useCallback(() => {
    if (isDrawing) {
      setIsDrawing(false);
      saveHistory();
    }
  }, [isDrawing, saveHistory]);

  const undo = useCallback(() => {
    if (historyIndex <= 0) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const prevIndex = historyIndex - 1;
    ctx.putImageData(history[prevIndex].data, 0, 0);
    setHistoryIndex(prevIndex);
  }, [history, historyIndex]);

  const redo = useCallback(() => {
    if (historyIndex >= history.length - 1) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const nextIndex = historyIndex + 1;
    ctx.putImageData(history[nextIndex].data, 0, 0);
    setHistoryIndex(nextIndex);
  }, [history, historyIndex]);

  return (
    <div className="space-y-3">
      {/* Toolbar */}
      <div className="flex items-center justify-between flex-wrap gap-3 bg-gray-50 rounded-xl p-3">
        {/* Mode toggle */}
        <div className="flex items-center gap-1.5 bg-white rounded-lg p-1 border border-gray-200">
          <button
            onClick={() => setBrushMode("include")}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition-all ${
              brushMode === "include"
                ? "bg-green-500 text-white shadow-sm"
                : "text-gray-500 hover:text-gray-700"
            }`}
          >
            <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            画笔
          </button>
          <button
            onClick={() => setBrushMode("exclude")}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition-all ${
              brushMode === "exclude"
                ? "bg-red-500 text-white shadow-sm"
                : "text-gray-500 hover:text-gray-700"
            }`}
          >
            <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
            橡皮擦
          </button>
        </div>

        {/* Brush size */}
        <div className="flex items-center gap-2.5">
          <span className="text-xs text-gray-400">大小</span>
          <input
            type="range"
            min={5}
            max={60}
            value={brushSize}
            onChange={(e) => setBrushSize(Number(e.target.value))}
            className="w-24 sm:w-32 h-1.5 bg-gray-200 rounded-full appearance-none cursor-pointer accent-blue-500"
          />
          <span className="text-xs text-gray-500 font-mono w-6 text-right">{brushSize}</span>
        </div>

        {/* Undo/Redo */}
        <div className="flex items-center gap-1">
          <button
            onClick={undo}
            disabled={historyIndex <= 0}
            className="p-1.5 rounded-lg text-gray-400 hover:text-gray-700 hover:bg-white disabled:opacity-30 disabled:cursor-not-allowed transition-all"
            title="撤销"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 10h10a5 5 0 015 5v2M3 10l4-4M3 10l4 4" />
            </svg>
          </button>
          <button
            onClick={redo}
            disabled={historyIndex >= history.length - 1}
            className="p-1.5 rounded-lg text-gray-400 hover:text-gray-700 hover:bg-white disabled:opacity-30 disabled:cursor-not-allowed transition-all"
            title="重做"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 10H11a5 5 0 00-5 5v2m15-7l-4-4m4 4l-4 4" />
            </svg>
          </button>
        </div>
      </div>

      {/* Canvas area */}
      <div
        ref={containerRef}
        className="relative rounded-xl overflow-hidden border border-gray-200 checkerboard"
      >
        {!imageLoaded && (
          <div className="flex items-center justify-center h-64">
            <div className="relative w-6 h-6">
              <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
              <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
            </div>
          </div>
        )}
        <canvas
          ref={canvasRef}
          onMouseDown={handlePointerDown}
          onMouseMove={handlePointerMove}
          onMouseUp={handlePointerUp}
          onMouseLeave={handlePointerUp}
          onTouchStart={handleTouchStart}
          onTouchMove={handleTouchMove}
          onTouchEnd={handleTouchEnd}
          className={`w-full ${imageLoaded ? "block" : "hidden"}`}
          style={{ cursor: brushMode === "include" ? "crosshair" : "cell", touchAction: "none" }}
        />
      </div>

      {/* Hint */}
      <p className="text-xs text-gray-400 text-center">
        使用画笔添加需要保留的区域，使用橡皮擦去除多余部分
      </p>
    </div>
  );
}
