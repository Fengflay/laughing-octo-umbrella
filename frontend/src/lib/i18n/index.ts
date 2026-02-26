"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from "react";
import React from "react";
import zhTW, { type TranslationKeys } from "./zh-TW";
import zhCN from "./zh-CN";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export type Locale = "zh-TW" | "zh-CN";

interface I18nState {
  locale: Locale;
  t: TranslationKeys;
  setLocale: (locale: Locale) => void;
}

// ---------------------------------------------------------------------------
// Translation map
// ---------------------------------------------------------------------------

const translations: Record<Locale, TranslationKeys> = {
  "zh-TW": zhTW,
  "zh-CN": zhCN,
};

// ---------------------------------------------------------------------------
// LocalStorage key
// ---------------------------------------------------------------------------

const LOCALE_KEY = "app_locale";

function getStoredLocale(): Locale {
  if (typeof window === "undefined") return "zh-TW";
  const stored = localStorage.getItem(LOCALE_KEY);
  if (stored === "zh-TW" || stored === "zh-CN") return stored;
  return "zh-TW";
}

function storeLocale(locale: Locale): void {
  localStorage.setItem(LOCALE_KEY, locale);
}

// ---------------------------------------------------------------------------
// Context
// ---------------------------------------------------------------------------

const I18nContext = createContext<I18nState>({
  locale: "zh-TW",
  t: zhTW,
  setLocale: () => {},
});

// ---------------------------------------------------------------------------
// Provider
// ---------------------------------------------------------------------------

export function I18nProvider({ children }: { children: ReactNode }) {
  const [locale, setLocaleState] = useState<Locale>("zh-TW");

  useEffect(() => {
    setLocaleState(getStoredLocale());
  }, []);

  const setLocale = useCallback((l: Locale) => {
    setLocaleState(l);
    storeLocale(l);
    // Update html lang attribute
    document.documentElement.lang = l === "zh-TW" ? "zh-Hant" : "zh-Hans";
  }, []);

  const value: I18nState = {
    locale,
    t: translations[locale],
    setLocale,
  };

  return React.createElement(I18nContext.Provider, { value }, children);
}

// ---------------------------------------------------------------------------
// Hook
// ---------------------------------------------------------------------------

export function useTranslation() {
  const ctx = useContext(I18nContext);
  return ctx;
}

export { type TranslationKeys };
