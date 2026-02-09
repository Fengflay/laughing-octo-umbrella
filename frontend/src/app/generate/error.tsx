"use client";

import { useEffect } from "react";

export default function GenerateError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("Generate page error:", error);
  }, [error]);

  return (
    <div className="flex flex-col items-center justify-center h-64 space-y-4">
      <svg
        className="w-16 h-16 text-red-300"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth={1.5}
          d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z"
        />
      </svg>
      <h2 className="text-xl font-semibold text-gray-700">
        生成過程發生錯誤
      </h2>
      <p className="text-gray-500 text-sm max-w-md text-center">
        {error.message || "圖片生成時出現問題，請嘗試重新操作"}
      </p>
      <div className="flex gap-3">
        <button
          onClick={reset}
          className="px-6 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700"
        >
          重試
        </button>
        <a
          href="/"
          className="px-6 py-2 bg-gray-100 text-gray-700 rounded-xl hover:bg-gray-200"
        >
          重新上傳
        </a>
      </div>
    </div>
  );
}
