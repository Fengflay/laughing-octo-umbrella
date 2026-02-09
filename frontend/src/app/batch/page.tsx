"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import AuthGuard from "@/components/AuthGuard";
import { useApp } from "@/lib/store";

interface BatchItemPreview {
  sku_name: string;
  product_type: string;
  style: string | null;
  image_filename: string;
  estimated_credits: number;
}

interface BatchPreview {
  batch_id: string;
  total_skus: number;
  total_credits: number;
  items: BatchItemPreview[];
  errors: string[];
}

interface BatchItemStatus {
  sku_name: string;
  product_type: string;
  status: string;
  job_id: string | null;
  error: string | null;
}

interface BatchStatus {
  batch_id: string;
  status: string;
  total_skus: number;
  completed_skus: number;
  total_credits: number;
  error_message: string | null;
  items: BatchItemStatus[];
}

const PRODUCT_TYPE_NAMES: Record<string, string> = {
  bags: "包包", jewelry: "飾品", clothing: "服飾", shoes: "鞋子",
  electronics: "3C 電子", beauty: "美妝", home: "居家", toys: "玩具",
  sports: "運動", food: "食品", stationery: "文具", pets: "寵物",
  automotive: "汽車", phones: "手機", travel: "旅行", fashion_acc: "配飾",
  kitchenware: "廚房", health: "保健", hobbies: "興趣", motorcycle: "機車",
};

function BatchContent() {
  const { user, refreshUser } = useApp();
  const [phase, setPhase] = useState<"upload" | "preview" | "running" | "done">("upload");
  const [preview, setPreview] = useState<BatchPreview | null>(null);
  const [batchStatus, setBatchStatus] = useState<BatchStatus | null>(null);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const csvRef = useRef<HTMLInputElement>(null);
  const zipRef = useRef<HTMLInputElement>(null);
  const pollRef = useRef<NodeJS.Timeout | null>(null);

  // Cleanup polling on unmount
  useEffect(() => {
    return () => {
      if (pollRef.current) clearInterval(pollRef.current);
    };
  }, []);

  const handleUpload = useCallback(async () => {
    const csvFile = csvRef.current?.files?.[0];
    const zipFile = zipRef.current?.files?.[0];
    if (!csvFile || !zipFile) {
      setError("請同時選擇 CSV 和 ZIP 檔案");
      return;
    }

    setError(null);
    setUploading(true);

    try {
      const token = localStorage.getItem("auth_token");
      const formData = new FormData();
      formData.append("csv_file", csvFile);
      formData.append("zip_file", zipFile);

      const res = await fetch("/api/batch/upload", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.detail || "上傳失敗");
      }

      const data: BatchPreview = await res.json();
      setPreview(data);
      setPhase("preview");
    } catch (err) {
      setError(err instanceof Error ? err.message : "上傳失敗");
    } finally {
      setUploading(false);
    }
  }, []);

  const handleStart = useCallback(async () => {
    if (!preview) return;
    setError(null);

    try {
      const token = localStorage.getItem("auth_token");
      const res = await fetch(`/api/batch/${preview.batch_id}/start`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
      });

      if (!res.ok) {
        const data = await res.json().catch(() => ({}));
        throw new Error(data.detail || "啟動失敗");
      }

      setPhase("running");
      refreshUser();

      // Start polling
      pollRef.current = setInterval(async () => {
        try {
          const statusRes = await fetch(`/api/batch/${preview.batch_id}/status`, {
            headers: { Authorization: `Bearer ${token}` },
          });
          if (statusRes.ok) {
            const statusData: BatchStatus = await statusRes.json();
            setBatchStatus(statusData);
            if (["completed", "partial", "failed"].includes(statusData.status)) {
              if (pollRef.current) clearInterval(pollRef.current);
              setPhase("done");
              refreshUser();
            }
          }
        } catch {
          // ignore polling errors
        }
      }, 3000);
    } catch (err) {
      setError(err instanceof Error ? err.message : "啟動失敗");
    }
  }, [preview, refreshUser]);

  const handleDownload = useCallback(() => {
    if (!preview) return;
    const token = localStorage.getItem("auth_token");
    window.open(`/api/batch/${preview.batch_id}/download?token=${token}`, "_blank");
  }, [preview]);

  return (
    <div className="space-y-6 max-w-3xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-xl font-bold text-gray-800">批量生成</h1>
          <p className="text-sm text-gray-400 mt-1">上傳 CSV + ZIP，一次生成多個 SKU 的產品圖</p>
        </div>
        <a href="/" className="text-sm text-gray-400 hover:text-blue-500 transition-colors">← 返回</a>
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-3.5 rounded-xl text-sm">
          {error}
        </div>
      )}

      {/* Phase: Upload */}
      {phase === "upload" && (
        <div className="bg-white rounded-2xl border border-gray-200/80 p-6 shadow-sm space-y-5">
          <div>
            <h2 className="text-base font-semibold text-gray-800 mb-1">1. 準備檔案</h2>
            <p className="text-xs text-gray-400">
              CSV 格式：<code className="bg-gray-100 px-1.5 py-0.5 rounded text-gray-600">sku_name,product_type,style</code>
              （第一行為標題）
            </p>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">CSV 檔案</label>
              <input
                ref={csvRef}
                type="file"
                accept=".csv"
                className="block w-full text-sm text-gray-500 file:mr-3 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-600 hover:file:bg-blue-100 transition-colors"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">圖片 ZIP</label>
              <input
                ref={zipRef}
                type="file"
                accept=".zip"
                className="block w-full text-sm text-gray-500 file:mr-3 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-600 hover:file:bg-blue-100 transition-colors"
              />
            </div>
          </div>

          <div className="bg-gray-50 rounded-xl p-4 text-xs text-gray-500 space-y-1">
            <p><strong>CSV 範例：</strong></p>
            <pre className="bg-white rounded-lg p-3 text-gray-600 overflow-x-auto">
{`sku_name,product_type,style
leather_bag_01,bags,western
gold_ring_01,jewelry,korean
sneaker_pro,shoes,japanese`}
            </pre>
            <p className="mt-2">ZIP 中的圖片檔名須與 sku_name 對應（例如 leather_bag_01.jpg）</p>
          </div>

          <button
            onClick={handleUpload}
            disabled={uploading}
            className="w-full py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 disabled:opacity-50 transition-colors"
          >
            {uploading ? "上傳中..." : "上傳並預覽"}
          </button>
        </div>
      )}

      {/* Phase: Preview */}
      {phase === "preview" && preview && (
        <div className="space-y-4">
          <div className="bg-white rounded-2xl border border-gray-200/80 p-6 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-base font-semibold text-gray-800">預覽確認</h2>
              <div className="flex items-center gap-3 text-sm">
                <span className="text-gray-500">{preview.total_skus} 個 SKU</span>
                <span className="text-amber-600 font-semibold">{preview.total_credits} 點</span>
              </div>
            </div>

            {preview.errors.length > 0 && (
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-3 mb-4">
                <p className="text-xs font-medium text-amber-700 mb-1">部分 SKU 有問題：</p>
                {preview.errors.map((err, i) => (
                  <p key={i} className="text-xs text-amber-600">{err}</p>
                ))}
              </div>
            )}

            <div className="divide-y divide-gray-100 max-h-80 overflow-y-auto">
              {preview.items.map((item) => (
                <div key={item.sku_name} className="py-2.5 flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-700">{item.sku_name}</p>
                    <p className="text-xs text-gray-400">
                      {PRODUCT_TYPE_NAMES[item.product_type] || item.product_type}
                      {item.style && ` · ${item.style}`}
                    </p>
                  </div>
                  <span className="text-xs text-gray-400">{item.estimated_credits} 點</span>
                </div>
              ))}
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={() => setPhase("upload")}
              className="flex-1 py-3 bg-white border border-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-50 transition-colors"
            >
              返回修改
            </button>
            <button
              onClick={handleStart}
              disabled={!user || user.credits < preview.total_credits}
              className="flex-1 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 disabled:opacity-50 transition-colors"
            >
              確認生成（{preview.total_credits} 點）
            </button>
          </div>

          {user && user.credits < preview.total_credits && (
            <p className="text-center text-xs text-red-500">
              點數不足：需要 {preview.total_credits} 點，目前餘額 {user.credits} 點
            </p>
          )}
        </div>
      )}

      {/* Phase: Running */}
      {phase === "running" && (
        <div className="bg-white rounded-2xl border border-gray-200/80 p-6 shadow-sm">
          <div className="text-center space-y-4">
            <div className="inline-flex items-center justify-center w-16 h-16 bg-blue-50 rounded-2xl">
              <svg className="w-8 h-8 text-blue-500 animate-spin" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
              </svg>
            </div>
            <div>
              <p className="text-lg font-semibold text-gray-800">批量生成中</p>
              <p className="text-sm text-gray-400 mt-1">
                {batchStatus
                  ? `${batchStatus.completed_skus} / ${batchStatus.total_skus} SKU 完成`
                  : "排隊處理中..."}
              </p>
            </div>
            {batchStatus && (
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-blue-500 h-2 rounded-full transition-all duration-500"
                  style={{ width: `${(batchStatus.completed_skus / batchStatus.total_skus) * 100}%` }}
                />
              </div>
            )}
          </div>
        </div>
      )}

      {/* Phase: Done */}
      {phase === "done" && batchStatus && (
        <div className="space-y-4">
          <div className="bg-white rounded-2xl border border-gray-200/80 p-6 shadow-sm">
            <div className="text-center space-y-3 mb-6">
              <div className={`inline-flex items-center justify-center w-16 h-16 rounded-2xl ${
                batchStatus.status === "completed" ? "bg-green-50" : "bg-amber-50"
              }`}>
                {batchStatus.status === "completed" ? (
                  <svg className="w-8 h-8 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                ) : (
                  <svg className="w-8 h-8 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                )}
              </div>
              <p className="text-lg font-semibold text-gray-800">
                {batchStatus.status === "completed" ? "全部完成" : `部分完成 (${batchStatus.completed_skus}/${batchStatus.total_skus})`}
              </p>
            </div>

            <div className="divide-y divide-gray-100 max-h-60 overflow-y-auto">
              {batchStatus.items.map((item) => (
                <div key={item.sku_name} className="py-2.5 flex items-center justify-between">
                  <div>
                    <p className="text-sm font-medium text-gray-700">{item.sku_name}</p>
                    <p className="text-xs text-gray-400">{PRODUCT_TYPE_NAMES[item.product_type] || item.product_type}</p>
                  </div>
                  <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${
                    item.status === "completed" ? "bg-green-50 text-green-600" :
                    item.status === "failed" ? "bg-red-50 text-red-500" : "bg-gray-100 text-gray-500"
                  }`}>
                    {item.status === "completed" ? "完成" : item.status === "failed" ? "失敗" : item.status}
                  </span>
                </div>
              ))}
            </div>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={handleDownload}
              className="flex-1 py-3 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 transition-colors"
            >
              下載全部結果（ZIP）
            </button>
            <button
              onClick={() => { setPhase("upload"); setPreview(null); setBatchStatus(null); }}
              className="flex-1 py-3 bg-white border border-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-50 transition-colors"
            >
              新批量任務
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default function BatchPage() {
  return (
    <AuthGuard required>
      <BatchContent />
    </AuthGuard>
  );
}
