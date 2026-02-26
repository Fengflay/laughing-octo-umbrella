"use client";

import { useTranslation } from "@/lib/i18n";
import { useTheme, type FestivalTheme } from "@/lib/themes";

export default function ThemePicker() {
  const { t } = useTranslation();
  const { currentTheme, themes, setTheme } = useTheme();

  const getThemeName = (theme: FestivalTheme) => {
    const key = theme.nameKey as keyof typeof t.themes;
    return t.themes[key] || theme.nameKey;
  };

  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-4 shadow-sm">
      <div className="flex items-center gap-2 mb-3">
        <svg
          className="w-5 h-5 text-amber-500"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"
          />
        </svg>
        <h3 className="text-sm font-semibold text-gray-800">
          {t.themes.title}
        </h3>
      </div>
      <p className="text-xs text-gray-400 mb-3">{t.themes.subtitle}</p>

      <div className="space-y-2">
        {/* No theme option */}
        <button
          onClick={() => setTheme(null)}
          className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl border transition-all text-left ${
            !currentTheme
              ? "border-blue-400 bg-blue-50 ring-1 ring-blue-200"
              : "border-gray-200 hover:border-gray-300 hover:bg-gray-50"
          }`}
        >
          <div className="w-8 h-8 rounded-lg bg-gray-100 border border-gray-200 flex items-center justify-center">
            <svg
              className="w-4 h-4 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"
              />
            </svg>
          </div>
          <span className="text-xs font-medium text-gray-600">
            {t.themes.noTheme}
          </span>
        </button>

        {/* Theme options */}
        {themes.map((theme) => (
          <button
            key={theme.id}
            onClick={() => setTheme(theme.id)}
            className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl border transition-all text-left ${
              currentTheme?.id === theme.id
                ? "border-blue-400 bg-blue-50 ring-1 ring-blue-200"
                : "border-gray-200 hover:border-gray-300 hover:bg-gray-50"
            }`}
          >
            <div
              className="w-8 h-8 rounded-lg border flex items-center justify-center"
              style={{
                backgroundColor: theme.backgroundColor,
                borderColor: theme.accentColor,
              }}
            >
              <div
                className="w-3 h-3 rounded-full"
                style={{ backgroundColor: theme.accentColor }}
              />
            </div>
            <span className="text-xs font-medium text-gray-700">
              {getThemeName(theme)}
            </span>
          </button>
        ))}
      </div>

      {currentTheme && (
        <div className="mt-3 pt-3 border-t border-gray-100">
          <p className="text-[10px] text-gray-400">
            {t.themes.currentTheme}: {getThemeName(currentTheme)}
          </p>
        </div>
      )}
    </div>
  );
}
