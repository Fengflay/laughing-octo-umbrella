"use client";

import { useState, useCallback } from "react";
import { useTranslation } from "@/lib/i18n";
import { exportForPlatform } from "@/lib/api";
import { motion, AnimatePresence } from "framer-motion";

// ---------------------------------------------------------------------------
// Platform definitions
// ---------------------------------------------------------------------------

interface PlatformDef {
  id: string;
  nameKey: string;
  specKey: string;
  emoji: string;
  width: number;
  height: number;
  needsOutpaint?: boolean;
}

const PLATFORMS: PlatformDef[] = [
  {
    id: "shopee",
    nameKey: "shopee",
    specKey: "shopeeSpec",
    emoji: "🟠",
    width: 1000,
    height: 1000,
  },
  {
    id: "momo",
    nameKey: "momo",
    specKey: "momoSpec",
    emoji: "🟣",
    width: 1000,
    height: 1000,
  },
  {
    id: "pchome",
    nameKey: "pchome",
    specKey: "pchomeSpec",
    emoji: "🔴",
    width: 800,
    height: 800,
  },
  {
    id: "ig-post",
    nameKey: "igPost",
    specKey: "igPostSpec",
    emoji: "📸",
    width: 1080,
    height: 1350,
  },
  {
    id: "ig-story",
    nameKey: "igStory",
    specKey: "igStorySpec",
    emoji: "📱",
    width: 1080,
    height: 1920,
    needsOutpaint: true,
  },
  {
    id: "line-ad",
    nameKey: "lineAd",
    specKey: "lineAdSpec",
    emoji: "🟢",
    width: 800,
    height: 1200,
  },
  {
    id: "facebook",
    nameKey: "facebook",
    specKey: "facebookSpec",
    emoji: "🔵",
    width: 1200,
    height: 1200,
  },
];

// ---------------------------------------------------------------------------
// Page
// ---------------------------------------------------------------------------

export default function ExportPage() {
  const { t } = useTranslation();
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [upscale, setUpscale] = useState(false);
  const [exporting, setExporting] = useState(false);
  const [previewPlatform, setPreviewPlatform] = useState<string | null>(null);

  const togglePlatform = useCallback((id: string) => {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  }, []);

  const selectAll = useCallback(() => {
    setSelected(new Set(PLATFORMS.map((p) => p.id)));
  }, []);

  const deselectAll = useCallback(() => {
    setSelected(new Set());
  }, []);

  const handleExport = async () => {
    if (selected.size === 0) return;
    setExporting(true);
    try {
      const result = await exportForPlatform({
        taskId: "demo-task", // In real usage, this comes from the generation task
        platforms: Array.from(selected),
        upscale4K: upscale,
      });
      // Trigger download
      if (result.downloadUrl) {
        const link = document.createElement("a");
        link.href = result.downloadUrl;
        link.download = "export.zip";
        link.click();
      }
    } finally {
      setExporting(false);
    }
  };

  const getNameForKey = (key: string) => {
    return (t.export as Record<string, string>)[key] ?? key;
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Page Header */}
      <div>
        <h1 className="text-xl sm:text-2xl font-bold text-gray-900">
          {t.export.title}
        </h1>
        <p className="text-sm text-gray-500 mt-1">{t.export.subtitle}</p>
      </div>

      {/* Platform Selection */}
      <div className="bg-white rounded-2xl border border-gray-200 p-5 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-base font-semibold text-gray-800">
            {t.export.selectPlatforms}
          </h2>
          <div className="flex items-center gap-2 text-xs">
            <button
              onClick={selectAll}
              className="text-blue-600 hover:text-blue-700 font-medium"
            >
              {t.common.confirm} ({PLATFORMS.length})
            </button>
            <span className="text-gray-300">|</span>
            <button
              onClick={deselectAll}
              className="text-gray-500 hover:text-gray-700"
            >
              {t.common.cancel}
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {PLATFORMS.map((platform) => {
            const isSelected = selected.has(platform.id);
            return (
              <button
                key={platform.id}
                onClick={() => togglePlatform(platform.id)}
                className={`relative flex items-center gap-3 p-4 rounded-xl border-2 transition-all text-left ${
                  isSelected
                    ? "border-blue-400 bg-blue-50/50 ring-1 ring-blue-200"
                    : "border-gray-200 hover:border-gray-300 hover:bg-gray-50"
                }`}
              >
                {/* Checkbox */}
                <div
                  className={`w-5 h-5 rounded-md border-2 flex items-center justify-center shrink-0 transition-colors ${
                    isSelected
                      ? "bg-blue-500 border-blue-500"
                      : "border-gray-300"
                  }`}
                >
                  {isSelected && (
                    <svg
                      className="w-3 h-3 text-white"
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
                  )}
                </div>

                {/* Emoji icon */}
                <span className="text-2xl">{platform.emoji}</span>

                {/* Info */}
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-gray-800">
                    {getNameForKey(platform.nameKey)}
                  </p>
                  <p className="text-[11px] text-gray-400 mt-0.5">
                    {getNameForKey(platform.specKey)}
                  </p>
                  {platform.needsOutpaint && (
                    <span className="inline-flex items-center gap-1 mt-1 px-2 py-0.5 rounded-full bg-amber-50 text-amber-600 text-[10px] font-medium">
                      <svg
                        className="w-3 h-3"
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
                      {t.export.needsOutpaint}
                    </span>
                  )}
                </div>

                {/* Preview button */}
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setPreviewPlatform(
                      previewPlatform === platform.id ? null : platform.id,
                    );
                  }}
                  className="shrink-0 p-1.5 rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-colors"
                  title={t.export.previewCrop}
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
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                    />
                  </svg>
                </button>
              </button>
            );
          })}
        </div>

        {/* Crop preview */}
        <AnimatePresence>
          {previewPlatform && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              className="overflow-hidden"
            >
              <div className="mt-4 p-4 bg-gray-50 rounded-xl border border-gray-200">
                <div className="flex items-center justify-between mb-3">
                  <h3 className="text-sm font-medium text-gray-700">
                    {t.export.previewCrop} -{" "}
                    {getNameForKey(
                      PLATFORMS.find((p) => p.id === previewPlatform)
                        ?.nameKey ?? "",
                    )}
                  </h3>
                  <button
                    onClick={() => setPreviewPlatform(null)}
                    className="text-gray-400 hover:text-gray-600"
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
                        d="M6 18L18 6M6 6l12 12"
                      />
                    </svg>
                  </button>
                </div>
                {(() => {
                  const p = PLATFORMS.find(
                    (pl) => pl.id === previewPlatform,
                  );
                  if (!p) return null;
                  const ratio = p.width / p.height;
                  const maxW = 200;
                  const w = maxW;
                  const h = maxW / ratio;
                  return (
                    <div className="flex justify-center">
                      <div
                        className="border-2 border-dashed border-gray-300 rounded-lg bg-white flex items-center justify-center text-xs text-gray-400"
                        style={{ width: `${w}px`, height: `${h}px`, maxHeight: "350px" }}
                      >
                        {p.width} x {p.height}
                      </div>
                    </div>
                  );
                })()}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Options */}
      <div className="bg-white rounded-2xl border border-gray-200 p-5 shadow-sm">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <label className="relative inline-flex items-center cursor-pointer">
              <input
                type="checkbox"
                checked={upscale}
                onChange={(e) => setUpscale(e.target.checked)}
                className="sr-only peer"
              />
              <div className="w-9 h-5 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-blue-500" />
            </label>
            <div>
              <p className="text-sm font-medium text-gray-800">
                {t.export.upscale4K}
              </p>
              <p className="text-xs text-gray-400">
                {t.export.upscale4KDesc}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Export Button */}
      <div className="text-center py-4">
        <button
          onClick={handleExport}
          disabled={selected.size === 0 || exporting}
          className="group relative inline-flex items-center gap-3 px-10 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white text-lg font-bold rounded-2xl hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 disabled:opacity-50 disabled:hover:translate-y-0 disabled:hover:shadow-lg"
        >
          {exporting ? (
            <>
              <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
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
              {t.export.exporting}
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
                  d="M12 10v6m0 0l-3-3m3 3l3-3M3 17v3a2 2 0 002 2h14a2 2 0 002-2v-3"
                />
              </svg>
              {t.export.exportAll}
              {selected.size > 0 && (
                <span className="text-sm opacity-80 font-normal">
                  ({selected.size} {t.export.selectPlatforms})
                </span>
              )}
            </>
          )}
        </button>
        {selected.size === 0 && (
          <p className="text-xs text-gray-400 mt-3">
            {t.export.selectPlatforms}
          </p>
        )}
      </div>
    </div>
  );
}
