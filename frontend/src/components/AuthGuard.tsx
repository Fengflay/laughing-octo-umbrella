"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { isLoggedIn, getMe } from "@/lib/auth";

interface AuthGuardProps {
  children: React.ReactNode;
  /** If true, redirect to /login when not authenticated. Default: false (Phase 1 optional). */
  required?: boolean;
}

/**
 * Authentication guard component.
 *
 * Phase 1 (optional auth):
 *   - Wraps pages that benefit from auth but don't require it
 *   - Shows content immediately, auth check runs in background
 *
 * Phase 2 (required auth):
 *   - Set required={true} to enforce login
 *   - Redirects to /login if user is not authenticated
 */
export default function AuthGuard({ children, required = false }: AuthGuardProps) {
  const router = useRouter();
  const [checking, setChecking] = useState(required);

  useEffect(() => {
    if (!required) return;

    // Check if user is logged in
    if (!isLoggedIn()) {
      router.replace("/login");
      return;
    }

    // Verify token is still valid
    getMe()
      .then((user) => {
        if (!user) {
          router.replace("/login");
        } else {
          setChecking(false);
        }
      })
      .catch(() => {
        router.replace("/login");
      });
  }, [required, router]);

  if (checking) {
    return (
      <div className="min-h-[40vh] flex items-center justify-center">
        <div className="flex items-center gap-3 text-gray-400">
          <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
          </svg>
          <span className="text-sm">驗證登入中...</span>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
