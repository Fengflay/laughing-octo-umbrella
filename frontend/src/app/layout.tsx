import type { Metadata } from "next";
import "./globals.css";
import { AppProvider } from "@/lib/store";
import LayoutShell from "@/components/LayoutShell";

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
          <LayoutShell>{children}</LayoutShell>
        </AppProvider>
      </body>
    </html>
  );
}
