"use client";

import { useMemo, useState } from "react";
import type { ProductTypeInfo } from "@/types";

interface ProductTypeSelectorProps {
  productTypes: ProductTypeInfo[];
  selected: string | null;
  onSelect: (typeId: string) => void;
}

export default function ProductTypeSelector({
  productTypes,
  selected,
  onSelect,
}: ProductTypeSelectorProps) {
  const [search, setSearch] = useState("");

  const filtered = useMemo(() => {
    if (!search.trim()) return productTypes;
    const q = search.toLowerCase();
    return productTypes.filter(
      (pt) =>
        pt.name.toLowerCase().includes(q) ||
        pt.name_en.toLowerCase().includes(q) ||
        pt.id.toLowerCase().includes(q)
    );
  }, [productTypes, search]);

  return (
    <div className="space-y-4">
      {/* Search bar */}
      {productTypes.length > 8 && (
        <div className="relative">
          <svg
            className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="搜尋品類... (例: 包包, shoes, 美妝)"
            className="w-full pl-10 pr-10 py-2.5 bg-white border border-gray-200 rounded-xl text-sm placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-400 transition-all"
          />
          {search && (
            <button
              onClick={() => setSearch("")}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600 transition-colors"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          )}
        </div>
      )}

      {/* Category info */}
      <div className="flex items-center justify-between">
        <p className="text-xs text-gray-400">
          {search ? `找到 ${filtered.length} 個品類` : `共 ${productTypes.length} 個品類`}
        </p>
        {selected && (
          <span className="text-xs text-blue-600 font-medium flex items-center gap-1">
            <svg className="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
            </svg>
            {productTypes.find((p) => p.id === selected)?.name}
          </span>
        )}
      </div>

      {/* Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2.5">
        {filtered.map((pt, i) => {
          const isSelected = selected === pt.id;
          return (
            <button
              key={pt.id}
              onClick={() => onSelect(pt.id)}
              className={`card-hover relative flex flex-col items-center gap-1.5 p-3 sm:p-3.5 rounded-xl border-2 text-center animate-fade-in ${
                isSelected
                  ? "border-blue-500 bg-blue-50 shadow-sm ring-1 ring-blue-200"
                  : "border-gray-100 bg-white hover:border-gray-200"
              }`}
              style={{ animationDelay: `${i * 30}ms` }}
            >
              {isSelected && (
                <div className="absolute top-1.5 right-1.5">
                  <svg className="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                </div>
              )}
              <span className="text-2xl sm:text-3xl leading-none">{pt.icon}</span>
              <span className={`font-semibold text-xs sm:text-sm leading-tight ${isSelected ? "text-blue-700" : "text-gray-700"}`}>
                {pt.name}
              </span>
              <span className="text-[10px] text-gray-400 leading-tight hidden sm:block">{pt.name_en}</span>
              <span className={`text-[10px] px-1.5 py-0.5 rounded-full ${
                isSelected ? "bg-blue-100 text-blue-600" : "bg-gray-50 text-gray-400"
              }`}>
                {pt.template_count} 場景
              </span>
            </button>
          );
        })}
      </div>

      {/* Empty state */}
      {filtered.length === 0 && (
        <div className="text-center py-8 animate-fade-in">
          <div className="text-3xl mb-2">🔍</div>
          <p className="text-gray-400 text-sm">找不到「{search}」相關品類</p>
          <button
            onClick={() => setSearch("")}
            className="mt-2 text-blue-500 text-sm hover:text-blue-700 transition-colors"
          >
            清除搜尋
          </button>
        </div>
      )}
    </div>
  );
}
