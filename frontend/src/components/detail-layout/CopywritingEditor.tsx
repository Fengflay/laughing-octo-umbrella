"use client";

import { useState } from "react";
import { useTranslation } from "@/lib/i18n";
import { generateCopywriting, type MarketingCopy } from "@/lib/api";

interface CopywritingEditorProps {
  primaryColor: string;
}

export default function CopywritingEditor({ primaryColor }: CopywritingEditorProps) {
  const { t } = useTranslation();
  const [copy, setCopy] = useState<MarketingCopy | null>(null);
  const [generating, setGenerating] = useState(false);
  const [editingField, setEditingField] = useState<string | null>(null);

  const handleGenerate = async () => {
    setGenerating(true);
    try {
      const result = await generateCopywriting({
        productName: "示範商品",
        productType: "general",
      });
      setCopy(result);
    } finally {
      setGenerating(false);
    }
  };

  const handleEditField = (field: keyof MarketingCopy, value: string) => {
    if (!copy) return;
    setCopy({ ...copy, [field]: value });
  };

  const handleEditSellingPoint = (index: number, value: string) => {
    if (!copy) return;
    const updated = [...copy.sellingPoints];
    updated[index] = value;
    setCopy({ ...copy, sellingPoints: updated });
  };

  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5 shadow-sm">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <svg
            className="w-5 h-5"
            style={{ color: primaryColor }}
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
            />
          </svg>
          <h3 className="text-base font-semibold text-gray-800">
            {t.detailLayout.copywritingTitle}
          </h3>
        </div>
        <button
          onClick={handleGenerate}
          disabled={generating}
          className="px-4 py-1.5 text-xs font-medium rounded-lg text-white transition-all disabled:opacity-50"
          style={{ backgroundColor: primaryColor }}
        >
          {generating ? (
            <span className="flex items-center gap-1.5">
              <svg className="animate-spin h-3.5 w-3.5" viewBox="0 0 24 24">
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                  fill="none"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                />
              </svg>
              {t.common.loading}
            </span>
          ) : copy ? (
            t.detailLayout.regenerateCopy
          ) : (
            t.detailLayout.generateCopy
          )}
        </button>
      </div>

      {!copy ? (
        <div className="text-center py-8 text-gray-400">
          <svg
            className="w-10 h-10 mx-auto mb-2 text-gray-300"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
          <p className="text-sm">{t.detailLayout.copywritingPlaceholder}</p>
          <p className="text-xs mt-1">{t.detailLayout.copywritingHint}</p>
        </div>
      ) : (
        <div className="space-y-4 animate-fade-in">
          {/* Headline */}
          <div>
            <label className="text-[10px] text-gray-400 uppercase tracking-wider">
              Headline
            </label>
            {editingField === "headline" ? (
              <input
                type="text"
                value={copy.headline}
                onChange={(e) => handleEditField("headline", e.target.value)}
                onBlur={() => setEditingField(null)}
                autoFocus
                className="w-full mt-1 text-lg font-bold text-gray-900 border-b-2 border-blue-400 outline-none bg-transparent pb-1"
              />
            ) : (
              <p
                className="text-lg font-bold text-gray-900 mt-1 cursor-pointer hover:bg-gray-50 rounded px-1 -mx-1 transition-colors"
                onClick={() => setEditingField("headline")}
              >
                {copy.headline}
              </p>
            )}
          </div>

          {/* Subheadline */}
          <div>
            <label className="text-[10px] text-gray-400 uppercase tracking-wider">
              Subheadline
            </label>
            {editingField === "subheadline" ? (
              <input
                type="text"
                value={copy.subheadline}
                onChange={(e) =>
                  handleEditField("subheadline", e.target.value)
                }
                onBlur={() => setEditingField(null)}
                autoFocus
                className="w-full mt-1 text-sm text-gray-600 border-b-2 border-blue-400 outline-none bg-transparent pb-1"
              />
            ) : (
              <p
                className="text-sm text-gray-600 mt-1 cursor-pointer hover:bg-gray-50 rounded px-1 -mx-1 transition-colors"
                onClick={() => setEditingField("subheadline")}
              >
                {copy.subheadline}
              </p>
            )}
          </div>

          {/* Selling Points */}
          <div>
            <label className="text-[10px] text-gray-400 uppercase tracking-wider">
              Selling Points
            </label>
            <ul className="mt-2 space-y-2">
              {copy.sellingPoints.map((point, idx) => (
                <li key={idx} className="flex items-start gap-2">
                  <span
                    className="w-5 h-5 rounded-full flex items-center justify-center text-white text-[10px] font-bold shrink-0 mt-0.5"
                    style={{ backgroundColor: primaryColor }}
                  >
                    {idx + 1}
                  </span>
                  {editingField === `sp-${idx}` ? (
                    <input
                      type="text"
                      value={point}
                      onChange={(e) =>
                        handleEditSellingPoint(idx, e.target.value)
                      }
                      onBlur={() => setEditingField(null)}
                      autoFocus
                      className="flex-1 text-sm text-gray-700 border-b-2 border-blue-400 outline-none bg-transparent pb-0.5"
                    />
                  ) : (
                    <span
                      className="text-sm text-gray-700 cursor-pointer hover:bg-gray-50 rounded px-1 -mx-1 transition-colors"
                      onClick={() => setEditingField(`sp-${idx}`)}
                    >
                      {point}
                    </span>
                  )}
                </li>
              ))}
            </ul>
          </div>

          {/* CTA */}
          <div
            className="text-center py-3 rounded-lg text-white font-semibold text-sm"
            style={{ backgroundColor: primaryColor }}
          >
            {copy.callToAction}
          </div>

          <p className="text-[10px] text-gray-400 text-center">
            {t.detailLayout.copywritingHint}
          </p>
        </div>
      )}
    </div>
  );
}
