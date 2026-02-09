"use client";

import { useCallback, useRef, useState } from "react";

interface ProductDetailInputProps {
  value: string;
  onChange: (value: string) => void;
  productType?: string;
}

interface CategoryHint {
  placeholder: string;
  suggestions: string[];
}

const CATEGORY_HINTS: Record<string, CategoryHint> = {
  bags: {
    placeholder: "例：真皮材質，手工縫製，可調式肩帶，容量約 5L，內部三層分隔...",
    suggestions: ["材質（真皮/帆布/尼龍）", "尺寸容量", "肩帶設計", "內部分層", "五金配件", "適用場合"],
  },
  jewelry: {
    placeholder: "例：925純銀，鋯石鑲嵌，過敏友善，鏈長45cm，附精美禮盒...",
    suggestions: ["材質（純銀/K金/合金）", "寶石鑲嵌", "尺寸重量", "過敏友善", "包裝禮盒", "保養方式"],
  },
  clothing: {
    placeholder: "例：100%純棉，透氣舒適，修身版型，M-3XL，四季皆宜...",
    suggestions: ["材質成分", "版型剪裁", "尺碼範圍", "洗滌方式", "適合季節", "穿搭建議"],
  },
  shoes: {
    placeholder: "例：透氣網布鞋面，減震中底，防滑橡膠大底，輕量化設計...",
    suggestions: ["鞋面材質", "鞋底設計", "尺碼範圍", "重量", "適合場景", "特殊功能（防水/透氣）"],
  },
  electronics: {
    placeholder: "例：藍牙5.3，主動降噪-42dB，40小時續航，IPX5防水...",
    suggestions: ["核心規格", "電池續航", "連接方式", "防水等級", "重量尺寸", "相容裝置"],
  },
  beauty: {
    placeholder: "例：玻尿酸精華，30ml，適合乾性肌膚，無添加酒精香精...",
    suggestions: ["主要成分", "容量規格", "適用膚質", "使用方式", "無添加項目", "功效特點"],
  },
  home: {
    placeholder: "例：竹木材質，可折疊設計，承重50kg，免安裝即用...",
    suggestions: ["材質", "尺寸規格", "承重/容量", "安裝方式", "適用空間", "特殊功能"],
  },
  toys: {
    placeholder: "例：ABS環保材質，適合3歲以上，含120片零件，附圖解說明書...",
    suggestions: ["材質安全性", "適用年齡", "零件數量", "教育功能", "包裝內容", "認證標準"],
  },
  sports: {
    placeholder: "例：高密度TPE瑜伽墊，厚度6mm，防滑紋路，附收納袋...",
    suggestions: ["材質", "尺寸規格", "適合運動類型", "防滑設計", "收納方式", "耐用度"],
  },
  food: {
    placeholder: "例：台灣高山烏龍茶，手採一芯二葉，150g/罐，冷泡熱沖皆宜...",
    suggestions: ["原料產地", "淨含量", "口味特點", "保存方式", "沖泡/食用方法", "認證（有機/無添加）"],
  },
  stationery: {
    placeholder: "例：0.5mm中性筆芯，速乾墨水，矽膠握套，書寫順滑不斷墨...",
    suggestions: ["規格尺寸", "材質", "墨水/筆芯類型", "特殊功能", "適用場景", "包裝數量"],
  },
  pets: {
    placeholder: "例：天然雞肉凍乾，無穀配方，適合全犬種，500g/包...",
    suggestions: ["成分配方", "適合寵物類型", "淨含量", "營養特點", "適用年齡", "餵食建議"],
  },
  automotive: {
    placeholder: "例：碳纖維紋路，適用特斯拉Model 3/Y，3M背膠免拆裝...",
    suggestions: ["材質", "適用車型", "安裝方式", "尺寸規格", "耐溫範圍", "功能特點"],
  },
  phones: {
    placeholder: "例：MagSafe磁吸，軍規防摔認證，透明PC背板，適用iPhone 16...",
    suggestions: ["適用機型", "材質", "防護等級", "特殊功能", "厚度重量", "認證標準"],
  },
  travel: {
    placeholder: "例：PC材質，20吋登機箱，TSA海關鎖，360度萬向輪，擴展層設計...",
    suggestions: ["材質", "尺寸容量", "輪子設計", "鎖具類型", "重量", "特殊功能（擴展/防盜）"],
  },
  fashion_acc: {
    placeholder: "例：100%羊毛，手工編織，秋冬保暖，多色可選...",
    suggestions: ["材質", "工藝", "尺寸", "適用季節", "顏色選擇", "搭配建議"],
  },
  kitchenware: {
    placeholder: "例：304不鏽鋼，三層複合底，電磁爐適用，附玻璃鍋蓋...",
    suggestions: ["材質", "容量規格", "適用爐具", "不沾塗層", "耐熱溫度", "配件內容"],
  },
  health: {
    placeholder: "例：聲波震動，5種清潔模式，IPX7全機防水，續航30天...",
    suggestions: ["技術原理", "功能模式", "防水等級", "電池續航", "配件內容", "適用人群"],
  },
  hobbies: {
    placeholder: "例：1:64合金車模，可開門設計，含展示底座，限量3000台...",
    suggestions: ["比例/規格", "材質", "細節工藝", "配件內容", "限量資訊", "收藏價值"],
  },
  motorcycle: {
    placeholder: "例：DOT認證安全帽，雙鏡片設計，可拆洗內襯，通風系統...",
    suggestions: ["安全認證", "材質", "適用車型", "尺寸規格", "特殊功能", "安裝方式"],
  },
};

const DEFAULT_HINT: CategoryHint = {
  placeholder: "例：描述產品的材質、尺寸、功能、特色等資訊...",
  suggestions: ["材質", "尺寸規格", "主要功能", "特色賣點", "適用場景", "包裝內容"],
};

export default function ProductDetailInput({
  value,
  onChange,
  productType,
}: ProductDetailInputProps) {
  const [focused, setFocused] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const hint = (productType && CATEGORY_HINTS[productType]) || DEFAULT_HINT;

  const handleSuggestionClick = useCallback(
    (suggestion: string) => {
      const separator = value.trim() ? "，" : "";
      const newValue = value.trim() + separator + suggestion + "：";
      onChange(newValue);
      // Focus textarea after inserting
      setTimeout(() => textareaRef.current?.focus(), 50);
    },
    [value, onChange],
  );

  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-6 h-6 bg-purple-100 rounded-lg flex items-center justify-center">
            <svg
              className="w-3.5 h-3.5 text-purple-600"
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
          </div>
          <span className="text-sm font-semibold text-gray-700">
            產品詳情
          </span>
          <span className="text-[10px] text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded">
            選填 — 不填也能自動生成文案
          </span>
        </div>
        {value.length > 0 && (
          <span className="text-[10px] text-gray-400">
            {value.length} 字
          </span>
        )}
      </div>

      <div
        className={`relative rounded-xl border transition-all duration-200 ${
          focused
            ? "border-purple-400 ring-2 ring-purple-500/20"
            : "border-gray-200 hover:border-gray-300"
        }`}
      >
        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onFocus={() => setFocused(true)}
          onBlur={() => setFocused(false)}
          rows={3}
          placeholder={hint.placeholder}
          className="w-full text-sm rounded-xl px-4 py-3 bg-transparent focus:outline-none resize-none text-gray-700 placeholder:text-gray-300"
        />
      </div>

      {/* Clickable suggestion tags */}
      <div className="flex flex-wrap gap-1.5">
        <span className="text-[10px] text-gray-400 leading-6">建議填寫：</span>
        {hint.suggestions.map((suggestion) => (
          <button
            key={suggestion}
            type="button"
            onClick={() => handleSuggestionClick(suggestion)}
            className="text-[11px] px-2.5 py-0.5 bg-purple-50 text-purple-600 rounded-full hover:bg-purple-100 hover:text-purple-700 transition-colors cursor-pointer"
          >
            + {suggestion}
          </button>
        ))}
      </div>

      <p className="text-[11px] text-gray-400 leading-relaxed">
        填寫越詳細，AI 生成的文案越精準。不填寫也可根據產品類型自動生成基礎文案
      </p>
    </div>
  );
}
