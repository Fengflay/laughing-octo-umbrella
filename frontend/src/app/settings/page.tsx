"use client";

import { useCallback, useEffect, useState } from "react";
import { getApiKeysStatus, saveApiKeys } from "@/lib/api";
import type { ApiKeysStatus } from "@/types";

export default function SettingsPage() {
  const [status, setStatus] = useState<ApiKeysStatus | null>(null);
  const [geminiKey, setGeminiKey] = useState("");
  const [togetherKey, setTogetherKey] = useState("");
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getApiKeysStatus()
      .then((s) => {
        setStatus(s);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const handleSave = useCallback(async () => {
    setSaving(true);
    setMessage(null);

    try {
      const params: { gemini_api_key?: string; together_api_key?: string } = {};
      if (geminiKey.trim()) params.gemini_api_key = geminiKey.trim();
      if (togetherKey.trim()) params.together_api_key = togetherKey.trim();

      if (!params.gemini_api_key && !params.together_api_key) {
        setMessage({ type: "error", text: "請至少輸入一個 API Key" });
        setSaving(false);
        return;
      }

      const newStatus = await saveApiKeys(params);
      setStatus(newStatus);
      setGeminiKey("");
      setTogetherKey("");
      setMessage({ type: "success", text: "API Key 已儲存成功！" });
    } catch (err) {
      setMessage({
        type: "error",
        text: err instanceof Error ? err.message : "儲存失敗",
      });
    } finally {
      setSaving(false);
    }
  }, [geminiKey, togetherKey]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <p className="text-gray-500">載入中...</p>
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto space-y-8">
      <div className="flex items-center gap-4">
        <a
          href="/"
          className="text-blue-500 hover:text-blue-700 text-sm flex items-center gap-1"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          返回首頁
        </a>
      </div>

      <div>
        <h1 className="text-2xl font-bold">API Key 設定</h1>
        <p className="text-gray-500 text-sm mt-1">
          設定 AI 圖片生成服務的 API Key，儲存後即可開始使用
        </p>
      </div>

      {/* Current status */}
      {status && (
        <div className="bg-white rounded-xl border border-gray-200 p-5 space-y-4">
          <h2 className="font-semibold text-gray-700">目前狀態</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className={`rounded-lg p-4 ${status.gemini_configured ? "bg-green-50 border border-green-200" : "bg-red-50 border border-red-200"}`}>
              <div className="flex items-center gap-2 mb-1">
                <span className={`w-2.5 h-2.5 rounded-full ${status.gemini_configured ? "bg-green-500" : "bg-red-400"}`} />
                <span className="font-medium text-sm">Nano Banana Pro (Gemini)</span>
              </div>
              <p className="text-xs text-gray-500 font-mono">{status.gemini_key_preview}</p>
            </div>
            <div className={`rounded-lg p-4 ${status.together_configured ? "bg-green-50 border border-green-200" : "bg-yellow-50 border border-yellow-200"}`}>
              <div className="flex items-center gap-2 mb-1">
                <span className={`w-2.5 h-2.5 rounded-full ${status.together_configured ? "bg-green-500" : "bg-yellow-400"}`} />
                <span className="font-medium text-sm">Kimi K2.5 (Together AI)</span>
              </div>
              <p className="text-xs text-gray-500 font-mono">{status.together_key_preview}</p>
            </div>
          </div>
        </div>
      )}

      {/* Input form */}
      <div className="bg-white rounded-xl border border-gray-200 p-5 space-y-5">
        <h2 className="font-semibold text-gray-700">設定 API Key</h2>

        <div className="space-y-1">
          <label className="block text-sm font-medium text-gray-700">
            Gemini API Key
            <span className="text-red-500 ml-1">*</span>
          </label>
          <p className="text-xs text-gray-400">
            主要圖片生成服務，從{" "}
            <a
              href="https://aistudio.google.com/apikey"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-500 hover:underline"
            >
              Google AI Studio
            </a>
            {" "}取得
          </p>
          <input
            type="password"
            value={geminiKey}
            onChange={(e) => setGeminiKey(e.target.value)}
            placeholder="AIza..."
            className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
          />
        </div>

        <div className="space-y-1">
          <label className="block text-sm font-medium text-gray-700">
            Together AI API Key
            <span className="text-gray-400 ml-1 text-xs">(選填)</span>
          </label>
          <p className="text-xs text-gray-400">
            備選 Kimi K2.5 服務，從{" "}
            <a
              href="https://api.together.xyz/settings/api-keys"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-500 hover:underline"
            >
              Together AI
            </a>
            {" "}取得
          </p>
          <input
            type="password"
            value={togetherKey}
            onChange={(e) => setTogetherKey(e.target.value)}
            placeholder="tok_..."
            className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"
          />
        </div>

        {message && (
          <div
            className={`p-3 rounded-lg text-sm ${
              message.type === "success"
                ? "bg-green-50 text-green-700"
                : "bg-red-50 text-red-700"
            }`}
          >
            {message.text}
          </div>
        )}

        <button
          onClick={handleSave}
          disabled={saving || (!geminiKey.trim() && !togetherKey.trim())}
          className="w-full px-4 py-2.5 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
        >
          {saving ? "儲存中..." : "儲存 API Key"}
        </button>
      </div>
    </div>
  );
}
