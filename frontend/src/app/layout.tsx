import type { Metadata } from "next";
import "./globals.css";
import UserBadge from "@/components/UserBadge";
import { AppProvider } from "@/lib/store";

export const metadata: Metadata = {
  title: "AI 電商產品圖生成器",
  description: "上傳一張產品圖，AI 自動生成 9 張專業電商場景圖",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-Hant">
      <body className="bg-gray-50 text-gray-900 min-h-screen flex flex-col">
        <AppProvider>
          {/* Header */}
          <header className="border-b border-gray-200/80 sticky top-0 z-40 glass">
            <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 sm:h-16 flex items-center justify-between">
              <a href="/" className="flex items-center gap-2.5 group">
                <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center shadow-sm group-hover:shadow-md transition-shadow">
                  <svg className="w-4 h-4 sm:w-5 sm:h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
                <div className="flex flex-col">
                  <span className="text-sm sm:text-base font-bold tracking-tight leading-tight">
                    <span className="hidden sm:inline">AI 電商產品圖生成器</span>
                    <span className="sm:hidden">AI 產品圖</span>
                  </span>
                  <span className="text-[10px] sm:text-xs text-gray-400 leading-tight hidden sm:block">
                    上傳一張圖 → 生成 9 張專業場景圖
                  </span>
                </div>
              </a>
              <div className="flex items-center gap-2">
                <a
                  href="/credits"
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm text-gray-500 hover:text-gray-700 hover:bg-gray-100/80 transition-all"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  <span className="hidden sm:inline">點數</span>
                </a>
                <a
                  href="/settings"
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm text-gray-500 hover:text-gray-700 hover:bg-gray-100/80 transition-all"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.066 2.573c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.573 1.066c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.066-2.573c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                  <span className="hidden sm:inline">設定</span>
                </a>
                <UserBadge />
              </div>
            </div>
          </header>

          {/* Main content */}
          <main className="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-8">
            {children}
          </main>

          {/* Footer */}
          <footer className="border-t border-gray-100 py-4 mt-auto">
            <div className="max-w-6xl mx-auto px-4 sm:px-6 text-center">
              <p className="text-xs text-gray-400">
                AI 驅動 · 支援 20 種產品品類 · 180 種場景模板
              </p>
            </div>
          </footer>
        </AppProvider>
      </body>
    </html>
  );
}
