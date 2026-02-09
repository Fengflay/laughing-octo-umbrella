"use client";

import { useCallback, useState } from "react";
import { generateCopy } from "@/lib/api";
import type { CopyItem, GeneratedImage, SceneTemplate } from "@/types";

interface CopywritingPanelProps {
  productDetails: string;
  productType: string;
  templates: SceneTemplate[];
  images: GeneratedImage[];
}

function CopyCard({
  copy,
  sceneName,
  imageUrl,
}: {
  copy: CopyItem;
  sceneName: string;
  imageUrl: string | null;
}) {
  const [copiedField, setCopiedField] = useState<string | null>(null);

  const handleCopy = (text: string, field: string) => {
    navigator.clipboard.writeText(text);
    setCopiedField(field);
    setTimeout(() => setCopiedField(null), 1500);
  };

  const allText = `${copy.title}\n${copy.subtitle}\n\n${copy.description}\n\n${copy.hashtags.map((h) => `#${h}`).join(" ")}`;

  return (
    <div className="bg-white rounded-xl border border-gray-200 overflow-hidden hover:shadow-md transition-shadow">
      {/* Scene header */}
      <div className="flex items-center gap-3 px-4 py-2.5 bg-gray-50 border-b border-gray-100">
        {imageUrl && (
          <img
            src={imageUrl}
            alt={sceneName}
            className="w-10 h-10 rounded-lg object-cover border border-gray-200"
          />
        )}
        <div className="min-w-0 flex-1">
          <p className="text-xs font-medium text-gray-600 truncate">{sceneName}</p>
        </div>
        <button
          onClick={() => handleCopy(allText, "all")}
          className="shrink-0 text-[10px] px-2.5 py-1 bg-blue-50 text-blue-600 rounded-lg hover:bg-blue-100 transition-colors font-medium"
        >
          {copiedField === "all" ? "已複製!" : "複製全部"}
        </button>
      </div>

      {/* Copy content */}
      <div className="p-4 space-y-3">
        {/* Title */}
        <div
          className="group cursor-pointer"
          onClick={() => handleCopy(copy.title, "title")}
        >
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-purple-500 font-medium">標題</span>
            {copiedField === "title" && (
              <span className="text-[10px] text-green-500">已複製</span>
            )}
          </div>
          <p className="text-base font-bold text-gray-800 mt-0.5 group-hover:text-blue-600 transition-colors">
            {copy.title}
          </p>
        </div>

        {/* Subtitle */}
        <div
          className="group cursor-pointer"
          onClick={() => handleCopy(copy.subtitle, "subtitle")}
        >
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-purple-500 font-medium">副標題</span>
            {copiedField === "subtitle" && (
              <span className="text-[10px] text-green-500">已複製</span>
            )}
          </div>
          <p className="text-sm text-gray-600 mt-0.5 group-hover:text-blue-600 transition-colors">
            {copy.subtitle}
          </p>
        </div>

        {/* Description */}
        <div
          className="group cursor-pointer"
          onClick={() => handleCopy(copy.description, "desc")}
        >
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-purple-500 font-medium">描述</span>
            {copiedField === "desc" && (
              <span className="text-[10px] text-green-500">已複製</span>
            )}
          </div>
          <p className="text-sm text-gray-500 mt-0.5 leading-relaxed group-hover:text-blue-600 transition-colors">
            {copy.description}
          </p>
        </div>

        {/* Hashtags */}
        {copy.hashtags.length > 0 && (
          <div
            className="group cursor-pointer"
            onClick={() =>
              handleCopy(
                copy.hashtags.map((h) => `#${h}`).join(" "),
                "tags"
              )
            }
          >
            <div className="flex items-center justify-between">
              <span className="text-[10px] text-purple-500 font-medium">標籤</span>
              {copiedField === "tags" && (
                <span className="text-[10px] text-green-500">已複製</span>
              )}
            </div>
            <div className="flex flex-wrap gap-1.5 mt-1">
              {copy.hashtags.map((tag) => (
                <span
                  key={tag}
                  className="text-[11px] bg-purple-50 text-purple-600 px-2 py-0.5 rounded-full"
                >
                  #{tag}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default function CopywritingPanel({
  productDetails,
  productType,
  templates,
  images,
}: CopywritingPanelProps) {
  const [copies, setCopies] = useState<CopyItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [generated, setGenerated] = useState(false);

  const completedImages = images.filter((img) => img.status === "completed");

  const handleGenerate = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const scenes = completedImages.map((img) => {
        const tpl = templates.find((t) => t.id === img.template_id);
        return {
          name: tpl?.name || img.template_name,
          name_en: tpl?.name_en || "",
          description: tpl?.description || "",
        };
      });

      const result = await generateCopy({
        product_details: productDetails.trim() || "(未提供詳情)",
        product_type: productType,
        scenes,
      });

      setCopies(result.copies);
      setGenerated(true);
    } catch (err) {
      setError(err instanceof Error ? err.message : "文案生成失敗");
    } finally {
      setLoading(false);
    }
  }, [productDetails, productType, templates, completedImages]);

  const handleCopyAll = () => {
    const allText = copies
      .map(
        (c, i) =>
          `【${completedImages[i]?.template_name || `場景${c.scene_index}`}】\n${c.title}\n${c.subtitle}\n${c.description}\n${c.hashtags.map((h) => `#${h}`).join(" ")}`
      )
      .join("\n\n---\n\n");
    navigator.clipboard.writeText(allText);
  };

  return (
    <div className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl flex items-center justify-center">
            <svg
              className="w-4 h-4 text-white"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
              />
            </svg>
          </div>
          <div>
            <h3 className="font-bold text-gray-800">繁體中文行銷文案</h3>
            <p className="text-[11px] text-gray-400">
              根據產品詳情為每張圖生成專屬文案
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {generated && copies.length > 0 && (
            <button
              onClick={handleCopyAll}
              className="text-xs px-3 py-1.5 bg-gray-100 text-gray-600 rounded-lg hover:bg-gray-200 transition-colors font-medium"
            >
              複製全部文案
            </button>
          )}
          <button
            onClick={handleGenerate}
            disabled={loading || completedImages.length === 0}
            className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-purple-600 to-pink-600 text-white text-sm font-bold rounded-xl hover:from-purple-700 hover:to-pink-700 shadow-sm hover:shadow-md transition-all disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? (
              <>
                <svg
                  className="animate-spin h-4 w-4"
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
                生成中...
              </>
            ) : generated ? (
              "重新生成文案"
            ) : (
              <>
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
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
                {productDetails.trim()
                  ? `生成文案 (${completedImages.length} 張)`
                  : `自動生成文案 (${completedImages.length} 張)`}
              </>
            )}
          </button>
        </div>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-600 p-3 rounded-xl text-sm">
          {error}
        </div>
      )}

      {/* Copy cards */}
      {copies.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {copies.map((copy, idx) => {
            const img = completedImages[idx];
            return (
              <CopyCard
                key={copy.scene_index}
                copy={copy}
                sceneName={img?.template_name || `場景 ${copy.scene_index}`}
                imageUrl={img?.url || null}
              />
            );
          })}
        </div>
      )}
    </div>
  );
}
