"use client";

import { createContext, useCallback, useContext, useEffect, useState } from "react";
import type { AuthUser } from "@/lib/auth";
import { clearAuth, getMe, getStoredUser, isLoggedIn, setStoredUser } from "@/lib/auth";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

interface AppState {
  /** Current user or null if not logged in */
  user: AuthUser | null;
  /** Whether auth check is in progress */
  loading: boolean;
  /** Refresh user data from server (credits, etc.) */
  refreshUser: () => Promise<void>;
  /** Update user locally (e.g. after credit deduction) */
  updateUser: (user: AuthUser) => void;
  /** Clear user state (logout) */
  clearUser: () => void;
}

const AppContext = createContext<AppState>({
  user: null,
  loading: true,
  refreshUser: async () => {},
  updateUser: () => {},
  clearUser: () => {},
});

// ---------------------------------------------------------------------------
// Provider
// ---------------------------------------------------------------------------

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [loading, setLoading] = useState(true);

  // Initial auth check
  useEffect(() => {
    // Quick render from localStorage cache
    const cached = getStoredUser();
    if (cached) setUser(cached);

    // Then verify with server
    if (isLoggedIn()) {
      getMe()
        .then((u) => {
          if (u) {
            setUser(u);
          } else {
            setUser(null);
          }
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const refreshUser = useCallback(async () => {
    if (!isLoggedIn()) {
      setUser(null);
      return;
    }
    const u = await getMe();
    if (u) {
      setUser(u);
    } else {
      setUser(null);
    }
  }, []);

  const updateUser = useCallback((u: AuthUser) => {
    setUser(u);
    setStoredUser(u);
  }, []);

  const clearUser = useCallback(() => {
    setUser(null);
    clearAuth();
  }, []);

  return (
    <AppContext.Provider value={{ user, loading, refreshUser, updateUser, clearUser }}>
      {children}
    </AppContext.Provider>
  );
}

// ---------------------------------------------------------------------------
// Hook
// ---------------------------------------------------------------------------

export function useApp(): AppState {
  return useContext(AppContext);
}
