"use client";

import { useTranslation } from "@/lib/i18n";

export default function SettingsPage() {
  const { t } = useTranslation();

  return (
    <div className="max-w-2xl mx-auto space-y-8 animate-fade-in">
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
        <h1 className="text-2xl font-bold text-gray-900">{t.common.settings}</h1>
        <p className="text-gray-500 text-sm mt-1">
          系统设置与服务状态
        </p>
      </div>

      {/* AI Service Status */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-6 shadow-sm space-y-5">
        <h2 className="font-semibold text-gray-800">AI 服务状态</h2>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {/* Gemini */}
          <div className="rounded-xl p-4 bg-green-50 border border-green-200">
            <div className="flex items-center gap-2.5 mb-2">
              <div className="w-3 h-3 rounded-full bg-green-500 shadow-sm shadow-green-500/30" />
              <span className="font-semibold text-sm text-gray-800">Gemini Nano Banana Pro</span>
            </div>
            <p className="text-xs text-green-700 font-medium">✓ 已启用，无需配置</p>
            <p className="text-[11px] text-gray-400 mt-1">主要图片生成服务</p>
          </div>

          {/* Together AI */}
          <div className="rounded-xl p-4 bg-gray-50 border border-gray-200">
            <div className="flex items-center gap-2.5 mb-2">
              <div className="w-3 h-3 rounded-full bg-gray-300" />
              <span className="font-semibold text-sm text-gray-800">Kimi K2.5 (Together AI)</span>
            </div>
            <p className="text-xs text-gray-500">备用服务（可选）</p>
            <p className="text-[11px] text-gray-400 mt-1">高级场景生成备选方案</p>
          </div>
        </div>
      </div>

      {/* System Info */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-6 shadow-sm space-y-4">
        <h2 className="font-semibold text-gray-800">系统信息</h2>
        <div className="space-y-3">
          {[
            { label: "版本", value: "v1.0.0" },
            { label: "前端框架", value: "Next.js 15 + React 19" },
            { label: "后端框架", value: "FastAPI + SQLAlchemy" },
            { label: "AI 引擎", value: "Gemini Nano Banana Pro" },
          ].map((item) => (
            <div key={item.label} className="flex items-center justify-between py-2 border-b border-gray-100 last:border-0">
              <span className="text-sm text-gray-500">{item.label}</span>
              <span className="text-sm font-medium text-gray-800">{item.value}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
