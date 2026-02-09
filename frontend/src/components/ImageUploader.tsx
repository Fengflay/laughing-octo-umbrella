"use client";

import { useCallback, useRef, useState } from "react";

interface ImageUploaderProps {
  onUpload: (file: File) => void;
  uploading: boolean;
  previewUrl: string | null;
}

const SAMPLE_IMAGES = [
  { name: "designer bag.jpg", emoji: "👜", label: "包包" },
  { name: "pearl necklace.jpg", emoji: "💎", label: "首飾" },
  { name: "white sneakers.jpg", emoji: "👟", label: "球鞋" },
  { name: "skincare set.jpg", emoji: "💄", label: "美妝" },
  { name: "phone case.jpg", emoji: "📱", label: "手機殼" },
  { name: "kitchen tool.jpg", emoji: "🍳", label: "廚具" },
];

export default function ImageUploader({ onUpload, uploading, previewUrl }: ImageUploaderProps) {
  const [dragActive, setDragActive] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      e.stopPropagation();
      setDragActive(false);
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {
        onUpload(e.dataTransfer.files[0]);
      }
    },
    [onUpload],
  );

  const handleFileSelect = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      if (e.target.files && e.target.files[0]) {
        onUpload(e.target.files[0]);
      }
    },
    [onUpload],
  );

  const createSampleImage = useCallback((sample: typeof SAMPLE_IMAGES[0]) => {
    const canvas = document.createElement("canvas");
    canvas.width = 512;
    canvas.height = 512;
    const ctx = canvas.getContext("2d");
    if (ctx) {
      const gradient = ctx.createLinearGradient(0, 0, 512, 512);
      gradient.addColorStop(0, "#f8fafc");
      gradient.addColorStop(1, "#e2e8f0");
      ctx.fillStyle = gradient;
      ctx.fillRect(0, 0, 512, 512);
      ctx.font = "80px sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(sample.emoji, 256, 230);
      ctx.font = "bold 18px sans-serif";
      ctx.fillStyle = "#64748b";
      ctx.fillText(sample.label, 256, 330);
      canvas.toBlob((blob) => {
        if (blob) {
          const file = new File([blob], sample.name, { type: "image/jpeg" });
          onUpload(file);
        }
      }, "image/jpeg", 0.9);
    }
  }, [onUpload]);

  return (
    <div className="space-y-4">
      {/* Main upload area */}
      <div
        className={`
          relative overflow-hidden rounded-2xl transition-all duration-300
          ${dragActive
            ? "ring-2 ring-blue-400 ring-offset-2 scale-[1.005]"
            : "ring-1 ring-gray-200 hover:ring-gray-300"
          }
          ${uploading ? "opacity-60 pointer-events-none" : ""}
        `}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        {/* Gradient background for drag state */}
        <div
          className={`absolute inset-0 transition-opacity duration-300 ${dragActive ? "opacity-100" : "opacity-0"}`}
          style={{ background: "linear-gradient(135deg, rgba(59,130,246,0.06) 0%, rgba(147,51,234,0.06) 100%)" }}
        />

        <div className="relative bg-white/90">
          {previewUrl ? (
            /* Preview state */
            <label className="block cursor-pointer">
              <div className="flex flex-col items-center gap-3 p-6 sm:p-8">
                <div className="relative group">
                  <img
                    src={previewUrl}
                    alt="Product preview"
                    className="max-h-56 sm:max-h-64 rounded-xl object-contain shadow-lg transition-transform duration-300 group-hover:scale-[1.02]"
                  />
                  <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-all duration-300 rounded-xl flex items-center justify-center">
                    <span className="text-white text-sm font-medium opacity-0 group-hover:opacity-100 transition-opacity bg-black/60 px-4 py-2 rounded-full backdrop-blur-sm">
                      點擊替換圖片
                    </span>
                  </div>
                </div>
                <div className="flex items-center gap-2 text-sm text-emerald-600">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                  <span className="font-medium">上傳成功</span>
                  <span className="text-gray-400">|</span>
                  <span className="text-gray-400 text-xs">拖拽或點擊替換</span>
                </div>
              </div>
              <input
                ref={fileInputRef}
                type="file"
                accept=".jpg,.jpeg,.png,.webp"
                className="hidden"
                onChange={handleFileSelect}
                disabled={uploading}
              />
            </label>
          ) : (
            /* Empty state */
            <label className="block cursor-pointer">
              <div className="flex flex-col items-center gap-4 p-8 sm:p-12">
                <div className={`
                  w-16 h-16 sm:w-20 sm:h-20 rounded-2xl flex items-center justify-center transition-all duration-300
                  ${dragActive
                    ? "bg-blue-100 scale-110"
                    : "bg-gradient-to-br from-blue-50 to-purple-50"
                  }
                `}>
                  <svg
                    className={`w-8 h-8 sm:w-10 sm:h-10 transition-all duration-300 ${
                      dragActive ? "text-blue-500 -translate-y-1" : "text-gray-400"
                    }`}
                    fill="none" stroke="currentColor" viewBox="0 0 24 24"
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5}
                      d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                  {dragActive && (
                    <div className="absolute inset-0 rounded-2xl border-2 border-blue-400 animate-pulse" />
                  )}
                </div>

                <div className="text-center space-y-1.5">
                  <p className={`text-base sm:text-lg font-semibold transition-colors ${
                    dragActive ? "text-blue-600" : "text-gray-700"
                  }`}>
                    {dragActive ? "鬆開即可上傳" : "拖拽產品圖片到這裡"}
                  </p>
                  <p className="text-sm text-gray-400">
                    支援 JPG, PNG, WebP，最大 10MB
                  </p>
                </div>

                <div className="px-6 py-2.5 bg-gradient-to-r from-blue-500 to-blue-600 text-white text-sm font-medium rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:-translate-y-0.5">
                  選擇檔案上傳
                </div>
              </div>
              <input
                ref={fileInputRef}
                type="file"
                accept=".jpg,.jpeg,.png,.webp"
                className="hidden"
                onChange={handleFileSelect}
                disabled={uploading}
              />
            </label>
          )}
        </div>
      </div>

      {/* Upload spinner */}
      {uploading && (
        <div className="flex items-center justify-center gap-3 py-3 animate-fade-in">
          <div className="relative w-5 h-5">
            <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
            <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
          </div>
          <span className="text-sm font-medium text-blue-600">上傳中...</span>
        </div>
      )}

      {/* Sample gallery */}
      {!previewUrl && !uploading && (
        <div className="pt-1 animate-fade-in">
          <p className="text-xs text-gray-400 text-center mb-3">
            或使用範例快速體驗
          </p>
          <div className="flex justify-center flex-wrap gap-2">
            {SAMPLE_IMAGES.map((sample) => (
              <button
                key={sample.name}
                className="flex items-center gap-1.5 px-3 py-2 rounded-lg border border-gray-200 bg-white hover:border-blue-300 hover:bg-blue-50/50 transition-all duration-200 hover:-translate-y-0.5 hover:shadow-sm text-xs"
                title={`試用 ${sample.label}`}
                onClick={() => createSampleImage(sample)}
              >
                <span className="text-base">{sample.emoji}</span>
                <span className="text-gray-600 font-medium">{sample.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
