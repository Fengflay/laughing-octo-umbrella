"use client";

import { useCallback, useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { HexColorPicker } from "react-colorful";
import { useWizard } from "@/lib/wizard-context";
import { getMaterialSamples, type MaterialSample } from "@/lib/api";

// ---------------------------------------------------------------------------
// Mock data for categories
// ---------------------------------------------------------------------------

const CATEGORIES = [
  { id: "bag", name: "箱包", icon: "bag" },
  { id: "jewelry", name: "珠宝首饰", icon: "jewelry" },
  { id: "shoes", name: "鞋靴", icon: "shoes" },
  { id: "cosmetics", name: "美妆护肤", icon: "cosmetics" },
  { id: "electronics", name: "3C 数码", icon: "electronics" },
  { id: "home", name: "家居用品", icon: "home" },
  { id: "food", name: "食品饮料", icon: "food" },
  { id: "clothing", name: "服装", icon: "clothing" },
  { id: "accessories", name: "配饰", icon: "accessories" },
  { id: "toys", name: "玩具", icon: "toys" },
];

const CATEGORY_ICONS: Record<string, string> = {
  bag: "M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z",
  jewelry: "M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5",
  shoes: "M13 10V3L4 14h7v7l9-11h-7z",
  cosmetics: "M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01",
  electronics: "M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z",
  home: "M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6",
  food: "M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
  clothing: "M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z",
  accessories: "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z",
  toys: "M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
};

const TAGS = [
  "轻奢", "性价比", "手工", "环保", "限量", "新品",
  "爆款", "网红同款", "高端", "日常", "礼品", "便携",
];

// ---------------------------------------------------------------------------
// Component
// ---------------------------------------------------------------------------

export default function StepAttributes() {
  const { state, dispatch, nextStep } = useWizard();
  const { attributes, removedBgUrl, uploadedImages } = state;
  const [materials, setMaterials] = useState<MaterialSample[]>([]);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [showColorPicker, setShowColorPicker] = useState(false);

  useEffect(() => {
    getMaterialSamples().then(setMaterials).catch(console.error);
  }, []);

  const updateAttr = useCallback(
    (updates: Partial<typeof attributes>) => {
      dispatch({ type: "UPDATE_ATTRIBUTES", updates });
    },
    [dispatch],
  );

  const toggleTag = useCallback(
    (tag: string) => {
      const current = attributes.tags;
      const next = current.includes(tag) ? current.filter((t) => t !== tag) : [...current, tag];
      updateAttr({ tags: next });
    },
    [attributes.tags, updateAttr],
  );

  const toggleCoreViewpoint = useCallback(
    (tag: string) => {
      const current = attributes.coreViewpoints;
      const next = current.includes(tag) ? current.filter((t) => t !== tag) : [...current, tag];
      updateAttr({ coreViewpoints: next });
    },
    [attributes.coreViewpoints, updateAttr],
  );

  const previewImage = removedBgUrl || uploadedImages[0]?.serverUrl || uploadedImages[0]?.localUrl;

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
    >
      {/* Two-column layout */}
      <div className="flex flex-col lg:flex-row gap-6">
        {/* Left: Preview */}
        <div className="lg:w-2/5 shrink-0">
          <div className="sticky top-24">
            <div className="bg-white rounded-2xl border border-gray-200/80 p-4 shadow-sm">
              <h3 className="text-sm font-semibold text-gray-700 mb-3">商品预览</h3>
              <div className="aspect-square rounded-xl overflow-hidden border border-gray-100 checkerboard">
                {previewImage ? (
                  <img
                    src={previewImage}
                    alt="Product preview"
                    className="w-full h-full object-contain"
                  />
                ) : (
                  <div className="w-full h-full flex items-center justify-center text-gray-300">
                    <svg className="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                    </svg>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>

        {/* Right: Attributes Panel */}
        <div className="lg:w-3/5 space-y-5">
          {/* Core Layer */}
          <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm space-y-5">
            <h3 className="text-sm font-bold text-gray-800">基本信息</h3>

            {/* Product Name */}
            <div>
              <label className="block text-xs font-medium text-gray-500 mb-1.5">商品名称</label>
              <input
                type="text"
                value={attributes.name}
                onChange={(e) => updateAttr({ name: e.target.value })}
                placeholder="例如：意大利真皮手提包"
                className="w-full px-4 py-2.5 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-400 transition-all placeholder:text-gray-300"
              />
            </div>

            {/* Category Selector */}
            <div>
              <label className="block text-xs font-medium text-gray-500 mb-2">商品类目</label>
              <div className="grid grid-cols-5 gap-2">
                {CATEGORIES.map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => updateAttr({ category: cat.id })}
                    className={`flex flex-col items-center gap-1.5 p-2.5 rounded-xl border-2 transition-all text-center ${
                      attributes.category === cat.id
                        ? "border-blue-500 bg-blue-50 shadow-sm"
                        : "border-gray-100 bg-white hover:border-gray-200 hover:bg-gray-50"
                    }`}
                  >
                    <svg
                      className={`w-5 h-5 ${
                        attributes.category === cat.id ? "text-blue-500" : "text-gray-400"
                      }`}
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={1.5}
                        d={CATEGORY_ICONS[cat.icon] || CATEGORY_ICONS.bag}
                      />
                    </svg>
                    <span
                      className={`text-[10px] font-medium leading-tight ${
                        attributes.category === cat.id ? "text-blue-700" : "text-gray-500"
                      }`}
                    >
                      {cat.name}
                    </span>
                  </button>
                ))}
              </div>
            </div>

            {/* Material Selector */}
            <div>
              <label className="block text-xs font-medium text-gray-500 mb-2">核心材质</label>
              <div className="grid grid-cols-5 gap-2">
                {materials.map((mat) => (
                  <button
                    key={mat.id}
                    onClick={() => updateAttr({ material: mat.id })}
                    className={`relative flex flex-col items-center gap-1.5 p-2.5 rounded-xl border-2 transition-all ${
                      attributes.material === mat.id
                        ? "border-blue-500 bg-blue-50 shadow-sm"
                        : "border-gray-100 bg-white hover:border-gray-200"
                    }`}
                  >
                    {/* Material thumbnail placeholder */}
                    <div
                      className={`w-8 h-8 rounded-lg ${
                        attributes.material === mat.id ? "bg-blue-100" : "bg-gray-100"
                      } flex items-center justify-center`}
                    >
                      <span className="text-xs text-gray-400">{mat.name.charAt(0)}</span>
                    </div>
                    <span
                      className={`text-[10px] font-medium ${
                        attributes.material === mat.id ? "text-blue-700" : "text-gray-500"
                      }`}
                    >
                      {mat.name}
                    </span>
                    {attributes.material === mat.id && (
                      <div className="absolute -top-1 -right-1">
                        <svg className="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                          <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                        </svg>
                      </div>
                    )}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Advanced Layer (Collapsible) */}
          <div className="bg-white rounded-2xl border border-gray-200/80 shadow-sm overflow-hidden">
            <button
              onClick={() => setShowAdvanced(!showAdvanced)}
              className="w-full flex items-center justify-between p-5 hover:bg-gray-50/50 transition-colors"
            >
              <div className="flex items-center gap-2">
                <h3 className="text-sm font-bold text-gray-800">高级设置</h3>
                <span className="text-[10px] text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
                  可选
                </span>
              </div>
              <motion.svg
                animate={{ rotate: showAdvanced ? 180 : 0 }}
                transition={{ duration: 0.2 }}
                className="w-4 h-4 text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </motion.svg>
            </button>

            <AnimatePresence>
              {showAdvanced && (
                <motion.div
                  initial={{ height: 0, opacity: 0 }}
                  animate={{ height: "auto", opacity: 1 }}
                  exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
                  className="overflow-hidden"
                >
                  <div className="px-5 pb-5 space-y-5 border-t border-gray-100 pt-4">
                    {/* Color Picker */}
                    <div>
                      <label className="block text-xs font-medium text-gray-500 mb-2">商品主色</label>
                      <div className="relative">
                        <button
                          onClick={() => setShowColorPicker(!showColorPicker)}
                          className="flex items-center gap-3 px-4 py-2.5 border border-gray-200 rounded-xl hover:border-gray-300 transition-colors w-full"
                        >
                          <div
                            className="w-6 h-6 rounded-lg border border-gray-200 shadow-inner"
                            style={{ backgroundColor: attributes.color }}
                          />
                          <span className="text-sm text-gray-600 font-mono">{attributes.color}</span>
                        </button>
                        <AnimatePresence>
                          {showColorPicker && (
                            <motion.div
                              initial={{ opacity: 0, y: -10 }}
                              animate={{ opacity: 1, y: 0 }}
                              exit={{ opacity: 0, y: -10 }}
                              className="absolute top-full mt-2 z-20 bg-white rounded-xl border border-gray-200 p-3 shadow-xl"
                            >
                              <HexColorPicker
                                color={attributes.color}
                                onChange={(color) => updateAttr({ color })}
                              />
                              <input
                                type="text"
                                value={attributes.color}
                                onChange={(e) => updateAttr({ color: e.target.value })}
                                className="mt-2 w-full px-3 py-1.5 border border-gray-200 rounded-lg text-xs font-mono text-center focus:outline-none focus:ring-2 focus:ring-blue-500/20"
                              />
                            </motion.div>
                          )}
                        </AnimatePresence>
                      </div>
                    </div>

                    {/* Audience */}
                    <div>
                      <label className="block text-xs font-medium text-gray-500 mb-2">受众定位</label>
                      <div className="flex gap-2">
                        {[
                          { value: "female" as const, label: "女性" },
                          { value: "male" as const, label: "男性" },
                          { value: "unisex" as const, label: "通用" },
                        ].map((option) => (
                          <button
                            key={option.value}
                            onClick={() => updateAttr({ audience: option.value })}
                            className={`flex-1 py-2.5 rounded-xl border-2 text-sm font-medium transition-all ${
                              attributes.audience === option.value
                                ? "border-blue-500 bg-blue-50 text-blue-700"
                                : "border-gray-100 bg-white text-gray-500 hover:border-gray-200"
                            }`}
                          >
                            {option.label}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Tags */}
                    <div>
                      <label className="block text-xs font-medium text-gray-500 mb-2">功能标签</label>
                      <div className="flex flex-wrap gap-2">
                        {TAGS.map((tag) => (
                          <button
                            key={tag}
                            onClick={() => toggleTag(tag)}
                            className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${
                              attributes.tags.includes(tag)
                                ? "border-blue-400 bg-blue-50 text-blue-700"
                                : "border-gray-200 bg-white text-gray-500 hover:border-gray-300"
                            }`}
                          >
                            {tag}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Core Viewpoints / Selling Points */}
                    <div>
                      <label className="block text-xs font-medium text-gray-500 mb-1.5">
                        卖点权重
                        <span className="text-gray-300 ml-1.5">点击标记为核心视角</span>
                      </label>
                      <div className="flex flex-wrap gap-2">
                        {attributes.tags.length > 0 ? (
                          attributes.tags.map((tag) => (
                            <button
                              key={tag}
                              onClick={() => toggleCoreViewpoint(tag)}
                              className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${
                                attributes.coreViewpoints.includes(tag)
                                  ? "border-amber-400 bg-amber-50 text-amber-700 ring-1 ring-amber-200 shadow-sm"
                                  : "border-gray-200 bg-white text-gray-500 hover:border-gray-300"
                              }`}
                            >
                              {attributes.coreViewpoints.includes(tag) && (
                                <span className="mr-1">&#9733;</span>
                              )}
                              {tag}
                            </button>
                          ))
                        ) : (
                          <p className="text-xs text-gray-300">请先选择功能标签</p>
                        )}
                      </div>
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </div>

          {/* Next Step Button */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
            className="flex justify-center pt-2"
          >
            <button
              onClick={nextStep}
              disabled={!attributes.name || !attributes.category}
              className="group inline-flex items-center gap-2.5 px-8 py-3.5 bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold rounded-2xl hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:translate-y-0"
            >
              下一步：选择风格与场景
              <svg className="w-4 h-4 transition-transform group-hover:translate-x-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </button>
          </motion.div>
        </div>
      </div>
    </motion.div>
  );
}
