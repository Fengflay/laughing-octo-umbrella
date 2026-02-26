"use client";

import {
  createContext,
  useCallback,
  useContext,
  useState,
  type ReactNode,
} from "react";
import React from "react";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export interface FestivalTheme {
  id: string;
  nameKey: string; // i18n key in themes.*
  borderStyle: string; // CSS border style
  backgroundColor: string; // CSS bg color
  accentColor: string; // CSS accent
  decorationElements: string[]; // CSS classes for decorations
  previewImage: string; // placeholder
}

interface ThemeState {
  currentTheme: FestivalTheme | null;
  themes: FestivalTheme[];
  setTheme: (themeId: string | null) => void;
}

// ---------------------------------------------------------------------------
// Pre-built theme slots
// ---------------------------------------------------------------------------

export const festivalThemes: FestivalTheme[] = [
  {
    id: "double11",
    nameKey: "double11",
    borderStyle: "3px solid #ff2442",
    backgroundColor: "#fff0f0",
    accentColor: "#ff2442",
    decorationElements: ["theme-deco-double11"],
    previewImage: "/themes/double11-preview.png",
  },
  {
    id: "mid-autumn",
    nameKey: "midAutumn",
    borderStyle: "3px solid #d4a574",
    backgroundColor: "#fdf6ec",
    accentColor: "#d4a574",
    decorationElements: ["theme-deco-mid-autumn"],
    previewImage: "/themes/mid-autumn-preview.png",
  },
  {
    id: "spring-new",
    nameKey: "springNew",
    borderStyle: "3px solid #4ade80",
    backgroundColor: "#f0fdf4",
    accentColor: "#4ade80",
    decorationElements: ["theme-deco-spring"],
    previewImage: "/themes/spring-preview.png",
  },
  {
    id: "christmas",
    nameKey: "christmas",
    borderStyle: "3px solid #dc2626",
    backgroundColor: "#fef2f2",
    accentColor: "#dc2626",
    decorationElements: ["theme-deco-christmas"],
    previewImage: "/themes/christmas-preview.png",
  },
  {
    id: "lunar-new-year",
    nameKey: "lunarNewYear",
    borderStyle: "3px solid #ef4444",
    backgroundColor: "#fef2f2",
    accentColor: "#ef4444",
    decorationElements: ["theme-deco-lunar"],
    previewImage: "/themes/lunar-preview.png",
  },
];

// ---------------------------------------------------------------------------
// Context
// ---------------------------------------------------------------------------

const ThemeContext = createContext<ThemeState>({
  currentTheme: null,
  themes: festivalThemes,
  setTheme: () => {},
});

// ---------------------------------------------------------------------------
// Provider
// ---------------------------------------------------------------------------

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [currentTheme, setCurrentTheme] = useState<FestivalTheme | null>(null);

  const setTheme = useCallback((themeId: string | null) => {
    if (!themeId) {
      setCurrentTheme(null);
      return;
    }
    const found = festivalThemes.find((t) => t.id === themeId);
    setCurrentTheme(found ?? null);
  }, []);

  return React.createElement(
    ThemeContext.Provider,
    { value: { currentTheme, themes: festivalThemes, setTheme } },
    children,
  );
}

// ---------------------------------------------------------------------------
// Hook
// ---------------------------------------------------------------------------

export function useTheme(): ThemeState {
  return useContext(ThemeContext);
}
