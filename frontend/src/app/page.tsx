"use client";

import { useCallback, useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import ImageUploader from "@/components/ImageUploader";
import ProductTypeSelector from "@/components/ProductTypeSelector";
import StyleSelector from "@/components/StyleSelector";
import HistoryPanel from "@/components/HistoryPanel";
import { useApp } from "@/lib/store";
import { getApiKeysStatus, getProductTypes, getStylesForCategory, removeBackground, uploadImage } from "@/lib/api";
import type { ApiKeysStatus, ProductTypeInfo, StyleInfo, UploadResponse } from "@/types";

function StepHeader({
  step,
  title,
  subtitle,
  status,
}: {
  step: number;
  title: string;
  subtitle?: string;
  status: "done" | "active" | "pending";
}) {
  return (
    <div className="flex items-center gap-3 mb-4">
      <div
        className={`step-badge ${
          status === "done"
            ? "step-badge-done"
            : status === "active"
              ? "step-badge-active"
              : "step-badge-pending"
        }`}
      >
        {status === "done" ? (
          <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
          </svg>
        ) : (
          step
        )}
      </div>
      <div>
        <h2 className={`text-base sm:text-lg font-bold ${status === "pending" ? "text-gray-400" : "text-gray-800"}`}>
          {title}
        </h2>
        {subtitle && (
          <p className="text-xs text-gray-400 mt-0.5">{subtitle}</p>
        )}
      </div>
    </div>
  );
}

export default function HomePage() {
  const router = useRouter();
  const { user } = useApp();
  const [productTypes, setProductTypes] = useState<ProductTypeInfo[]>([]);
  const [styles, setStyles] = useState<StyleInfo[]>([]);
  const [uploading, setUploading] = useState(false);
  const [uploadResult, setUploadResult] = useState<UploadResponse | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [selectedType, setSelectedType] = useState<string | null>(null);
  const [selectedStyle, setSelectedStyle] = useState<string | null>(null);
  const [removeBg, setRemoveBg] = useState(true);
  const [removingBg, setRemovingBg] = useState(false);
  const [removedBgUrl, setRemovedBgUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [apiStatus, setApiStatus] = useState<ApiKeysStatus | null>(null);

  useEffect(() => {
    getProductTypes().then(setProductTypes).catch(console.error);
    getApiKeysStatus().then(setApiStatus).catch(console.error);
  }, []);

  // Load category-specific styles when product type changes
  useEffect(() => {
    if (selectedType) {
      getStylesForCategory(selectedType).then(setStyles).catch(console.error);
      setSelectedStyle(null); // Reset style when category changes
    } else {
      setStyles([]);
    }
  }, [selectedType]);

  const handleUpload = useCallback(async (file: File) => {
    setError(null);
    setUploading(true);
    setRemovedBgUrl(null);

    const localUrl = URL.createObjectURL(file);
    setPreviewUrl(localUrl);

    try {
      const result = await uploadImage(file);
      setUploadResult(result);
      setPreviewUrl(result.url);
    } catch (err) {
      setError(err instanceof Error ? err.message : "上傳失敗");
      setPreviewUrl(null);
    } finally {
      setUploading(false);
    }
  }, []);

  const handleRemoveBg = useCallback(async () => {
    if (!uploadResult) return;
    setRemovingBg(true);
    setError(null);

    try {
      const result = await removeBackground(uploadResult.image_id);
      setRemovedBgUrl(result.removed_bg_url);
    } catch (err) {
      setError(err instanceof Error ? err.message : "去背失敗");
    } finally {
      setRemovingBg(false);
    }
  }, [uploadResult]);

  const handleGenerate = () => {
    if (!uploadResult || !selectedType) return;
    const params = new URLSearchParams({
      image_id: uploadResult.image_id,
      product_type: selectedType,
      remove_bg: removeBg ? "1" : "0",
    });
    if (selectedStyle) {
      params.set("style", selectedStyle);
    }
    router.push(`/generate?${params.toString()}`);
  };

  const selectedTypeName = productTypes.find(p => p.id === selectedType)?.name;

  return (
    <div className="space-y-6">
      {/* API Key warning */}
      {apiStatus && !apiStatus.gemini_configured && (
        <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 flex items-center justify-between animate-slide-up">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-amber-100 rounded-lg flex items-center justify-center shrink-0">
              <svg className="w-4 h-4 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z" />
              </svg>
            </div>
            <div>
              <p className="font-semibold text-amber-800 text-sm">尚未設定 API Key</p>
              <p className="text-xs text-amber-600">需要先設定 Gemini API Key 才能生成圖片</p>
            </div>
          </div>
          <a
            href="/settings"
            className="px-4 py-1.5 bg-amber-500 text-white text-sm font-semibold rounded-lg hover:bg-amber-600 transition-colors shrink-0"
          >
            前往設定
          </a>
        </div>
      )}

      {/* Step 1: Upload */}
      <section className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm animate-fade-in">
        <StepHeader
          step={1}
          title="上傳產品圖片"
          subtitle="拖拽或點擊上傳你的產品照片"
          status={uploadResult ? "done" : "active"}
        />
        <ImageUploader
          onUpload={handleUpload}
          uploading={uploading}
          previewUrl={previewUrl}
        />
      </section>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3.5 rounded-xl text-sm flex items-center gap-2 animate-scale-in">
          <svg className="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {error}
        </div>
      )}

      {/* Background removal toggle */}
      {uploadResult && (
        <section className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm animate-slide-up">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-3">
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={removeBg}
                  onChange={(e) => setRemoveBg(e.target.checked)}
                  className="sr-only peer"
                />
                <div className="w-9 h-5 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-blue-500"></div>
              </label>
              <span className="font-semibold text-sm">自動去背</span>
              <span className="text-[10px] text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">建議開啟</span>
            </div>
            {removeBg && !removedBgUrl && (
              <button
                onClick={handleRemoveBg}
                disabled={removingBg}
                className="text-xs px-3 py-1.5 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 transition-colors font-medium"
              >
                {removingBg ? (
                  <span className="flex items-center gap-1.5">
                    <svg className="animate-spin h-3 w-3" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                    </svg>
                    處理中
                  </span>
                ) : "預覽去背"}
              </button>
            )}
          </div>

          {removedBgUrl && (
            <div className="grid grid-cols-2 gap-3">
              <div className="space-y-1.5">
                <p className="text-xs text-gray-500 text-center font-medium">原圖</p>
                <div className="border border-gray-200 rounded-xl overflow-hidden bg-gray-50">
                  <img src={uploadResult.url} alt="Original" className="w-full h-40 object-contain" />
                </div>
              </div>
              <div className="space-y-1.5">
                <p className="text-xs text-gray-500 text-center font-medium">去背後</p>
                <div className="border border-gray-200 rounded-xl overflow-hidden checkerboard">
                  <img src={removedBgUrl} alt="Background removed" className="w-full h-40 object-contain" />
                </div>
              </div>
            </div>
          )}
        </section>
      )}

      {/* Step 2: Select product type */}
      {uploadResult && (
        <section className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm animate-slide-up">
          <StepHeader
            step={2}
            title="選擇產品類型"
            subtitle="選擇最匹配你產品的品類，AI 將根據品類生成合適的場景"
            status={selectedType ? "done" : "active"}
          />
          <ProductTypeSelector
            productTypes={productTypes}
            selected={selectedType}
            onSelect={setSelectedType}
          />
        </section>
      )}

      {/* Step 3: Select visual style */}
      {uploadResult && selectedType && styles.length > 0 && (
        <section className="bg-white rounded-2xl border border-gray-200/80 p-5 sm:p-6 shadow-sm animate-slide-up">
          <StepHeader
            step={3}
            title="選擇視覺風格"
            subtitle={`為${selectedTypeName || "產品"}推薦的拍攝風格`}
            status="active"
          />
          <StyleSelector
            styles={styles}
            selected={selectedStyle}
            onSelect={setSelectedStyle}
          />
        </section>
      )}

      {/* Generate button */}
      {uploadResult && selectedType && (
        <section className="text-center py-4 animate-slide-up">
          <button
            onClick={handleGenerate}
            className="group relative inline-flex items-center gap-3 px-10 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white text-lg font-bold rounded-2xl hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5"
          >
            <svg className="w-5 h-5 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
            <span>一鍵生成 9 張產品圖</span>
            {selectedStyle && (
              <span className="text-sm opacity-80 font-normal">
                ({styles.find(s => s.id === selectedStyle)?.name})
              </span>
            )}
          </button>
          <p className="text-xs text-gray-400 mt-3">
            {selectedTypeName && (
              <>品類: <span className="text-gray-600">{selectedTypeName}</span> · </>
            )}
            {user ? (
              <>消耗約 9 點 · 餘額 <span className="text-amber-600 font-medium">{user.credits} 點</span> · </>
            ) : null}
            預計 1-3 分鐘完成
          </p>
        </section>
      )}

      {/* History */}
      <HistoryPanel />
    </div>
  );
}
