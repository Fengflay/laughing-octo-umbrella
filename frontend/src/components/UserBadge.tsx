"use client";

import { useState } from "react";
import { logout } from "@/lib/auth";
import { useApp } from "@/lib/store";

/**
 * Header user badge: shows login/register links when not authenticated,
 * or user info + credits when authenticated.
 * Now uses the global AppProvider context instead of local state.
 */
export default function UserBadge() {
  const { user } = useApp();
  const [menuOpen, setMenuOpen] = useState(false);

  // Close menu on outside click
  if (typeof window !== "undefined") {
    // This is handled via onClick stopPropagation + document listener
  }

  if (!user) {
    return (
      <div className="flex items-center gap-2">
        <a
          href="/login"
          className="px-3 py-1.5 rounded-lg text-sm text-gray-600 hover:text-gray-800 hover:bg-gray-100/80 transition-all"
        >
          登入
        </a>
        <a
          href="/register"
          className="px-3 py-1.5 rounded-lg text-sm bg-gradient-to-r from-blue-500 to-purple-600 text-white hover:from-blue-600 hover:to-purple-700 shadow-sm transition-all"
        >
          免費註冊
        </a>
      </div>
    );
  }

  return (
    <div className="relative">
      <button
        onClick={(e) => {
          e.stopPropagation();
          setMenuOpen(!menuOpen);
        }}
        onBlur={() => setTimeout(() => setMenuOpen(false), 200)}
        className="flex items-center gap-2 px-3 py-1.5 rounded-xl hover:bg-gray-100/80 transition-all"
      >
        {/* Credits badge */}
        <a
          href="/credits"
          onClick={(e) => e.stopPropagation()}
          className="flex items-center gap-1 px-2 py-0.5 rounded-full bg-amber-50 border border-amber-200 text-amber-700 text-xs font-medium hover:bg-amber-100 transition-colors"
        >
          <svg className="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.736 6.979C9.208 6.193 9.696 6 10 6c.304 0 .792.193 1.264.979a1 1 0 001.715-1.029C12.279 4.784 11.232 4 10 4s-2.279.784-2.979 1.95c-.285.475-.507 1-.67 1.55H6a1 1 0 000 2h.013a9.358 9.358 0 000 1H6a1 1 0 100 2h.351c.163.55.385 1.075.67 1.55C7.721 15.216 8.768 16 10 16s2.279-.784 2.979-1.95a1 1 0 10-1.715-1.029c-.472.786-.96.979-1.264.979-.304 0-.792-.193-1.264-.979a5.95 5.95 0 01-.4-.821h2.564a1 1 0 000-2H8.057a7.224 7.224 0 010-1h3.843a1 1 0 000-2H8.336c.12-.292.264-.569.4-.821z" />
          </svg>
          {user.credits}
        </a>

        {/* User avatar */}
        <div className="w-7 h-7 rounded-full bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center text-white text-xs font-bold">
          {user.display_name.charAt(0).toUpperCase()}
        </div>
      </button>

      {/* Dropdown menu */}
      {menuOpen && (
        <div className="absolute right-0 top-full mt-1 w-56 bg-white rounded-xl border border-gray-200 shadow-lg py-1 z-50">
          <div className="px-4 py-3 border-b border-gray-100">
            <p className="text-sm font-medium text-gray-800 truncate">{user.display_name}</p>
            <p className="text-xs text-gray-400 truncate">{user.email}</p>
          </div>

          <a
            href="/credits"
            className="block px-4 py-2 border-b border-gray-100 hover:bg-gray-50 transition-colors"
          >
            <div className="flex items-center justify-between">
              <span className="text-xs text-gray-500">剩餘點數</span>
              <span className="text-sm font-semibold text-amber-600">{user.credits} 點</span>
            </div>
          </a>

          <button
            onClick={() => logout()}
            className="w-full text-left px-4 py-2.5 text-sm text-red-500 hover:bg-red-50 transition-colors"
          >
            登出
          </button>
        </div>
      )}
    </div>
  );
}
