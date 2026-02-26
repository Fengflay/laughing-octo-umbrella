"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { useWizard } from "@/lib/wizard-context";
import {
  getSceneTemplates,
  getModelPresets,
  type SceneTemplateV2,
  type ModelPresetData,
} from "@/lib/api";

// ---------------------------------------------------------------------------
// Props presets
// ---------------------------------------------------------------------------

const PRESET_PROPS = [
  "鲜花", "绿植", "咖啡杯", "书本", "蜡烛",
  "大理石托盘", "布艺背景", "木质底座", "水果",
  "丝绸面料", "首饰盒", "香薰", "杂志", "眼镜",
];

const ETHNICITY_OPTIONS = [
  { value: "", label: "全部" },
  { value: "east-asian", label: "东亚" },
  { value: "european", label: "欧美" },
  { value: "south-asian", label: "南亚" },
];

// ---------------------------------------------------------------------------
// Scene gradient placeholders
// ---------------------------------------------------------------------------

const SCENE_GRADIENTS: Record<string, string> = {
  japanese: "from-rose-50 to-stone-100",
  nordic: "from-sky-50 to-amber-50",
  korean: "from-orange-50 to-yellow-50",
  modern: "from-gray-100 to-slate-200",
  luxury: "from-stone-100 to-neutral-200",
  studio: "from-amber-50 to-orange-100",
  urban: "from-slate-200 to-gray-300",
  outdoor: "from-green-100 to-emerald-200",
  beach: "from-cyan-100 to-blue-200",
  garden: "from-green-50 to-lime-100",
  cafe: "from-amber-100 to-yellow-200",
  rooftop: "from-orange-200 to-pink-200",
};

// ---------------------------------------------------------------------------
// Component
// ---------------------------------------------------------------------------

export default function StepStyleScene() {
  const router = useRouter();
  const { state, dispatch } = useWizard();
  const [scenes, setScenes] = useState<SceneTemplateV2[]>([]);
  const [models, setModels] = useState<ModelPresetData[]>([]);
  const [sceneFilter, setSceneFilter] = useState<"all" | "indoor" | "outdoor">("all");
  const [customPropInput, setCustomPropInput] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const styleRefInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    getSceneTemplates().then(setScenes).catch(console.error);
    getModelPresets().then(setModels).catch(console.error);
  }, []);

  const filteredScenes =
    sceneFilter === "all" ? scenes : scenes.filter((s) => s.category === sceneFilter);

  const filteredModels = state.modelEthnicity
    ? models.filter((m) => m.ethnicity === state.modelEthnicity)
    : models;

  const handleToggleScene = useCallback(
    (scene: SceneTemplateV2) => {
      dispatch({
        type: "TOGGLE_SCENE",
        scene: { sceneId: scene.id, sceneName: scene.name, category: scene.category },
      });
    },
    [dispatch],
  );

  const handleAddCustomProp = useCallback(() => {
    const trimmed = customPropInput.trim();
    if (trimmed) {
      dispatch({ type: "ADD_CUSTOM_PROP", prop: trimmed });
      setCustomPropInput("");
    }
  }, [customPropInput, dispatch]);

  const handleStyleRefUpload = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files?.[0];
      if (!file) return;
      const localUrl = URL.createObjectURL(file);
      dispatch({ type: "SET_STYLE_REF", image: { file, localUrl } });
    },
    [dispatch],
  );

  const handleSubmit = useCallback(async () => {
    setSubmitting(true);
    // TODO: Submit to backend generation API
    // For now, just simulate delay
    await new Promise((r) => setTimeout(r, 1000));
    setSubmitting(false);
    router.push("/storyboard");
  }, [router]);

  const isSceneSelected = (sceneId: string) =>
    state.selectedScenes.some((s) => s.sceneId === sceneId);

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
      className="space-y-6"
    >
      {/* Style Reference Upload */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="text-sm font-bold text-gray-800">风格参考图</h3>
            <p className="text-xs text-gray-400 mt-0.5">上传一张参考图来引导生成风格（可选）</p>
          </div>
          <span className="text-[10px] text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
            IP-Adapter
          </span>
        </div>

        {state.styleRefImage ? (
          <div className="relative inline-block group">
            <img
              src={state.styleRefImage.localUrl}
              alt="Style reference"
              className="h-32 rounded-xl object-cover border border-gray-200"
            />
            <button
              onClick={() => dispatch({ type: "SET_STYLE_REF", image: null })}
              className="absolute top-1.5 right-1.5 w-6 h-6 bg-black/60 text-white rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-500"
            >
              <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        ) : (
          <label className="block cursor-pointer">
            <div className="border-2 border-dashed border-gray-200 rounded-xl p-6 text-center hover:border-blue-300 hover:bg-blue-50/30 transition-all">
              <svg className="w-8 h-8 text-gray-300 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 4v16m8-8H4" />
              </svg>
              <p className="text-xs text-gray-400">点击上传参考图</p>
            </div>
            <input
              ref={styleRefInputRef}
              type="file"
              accept=".jpg,.jpeg,.png,.webp"
              className="hidden"
              onChange={handleStyleRefUpload}
            />
          </label>
        )}
      </div>

      {/* Scene Library */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-sm font-bold text-gray-800">场景库</h3>
          <div className="flex items-center gap-1 bg-gray-100 rounded-lg p-0.5">
            {(["all", "indoor", "outdoor"] as const).map((filter) => (
              <button
                key={filter}
                onClick={() => setSceneFilter(filter)}
                className={`px-3 py-1 rounded-md text-xs font-medium transition-all ${
                  sceneFilter === filter
                    ? "bg-white text-gray-800 shadow-sm"
                    : "text-gray-500 hover:text-gray-700"
                }`}
              >
                {filter === "all" ? "全部" : filter === "indoor" ? "室内" : "室外"}
              </button>
            ))}
          </div>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
          {filteredScenes.map((scene, i) => (
            <motion.button
              key={scene.id}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.04 }}
              onClick={() => handleToggleScene(scene)}
              className={`relative group rounded-xl border-2 overflow-hidden transition-all ${
                isSceneSelected(scene.id)
                  ? "border-blue-500 ring-1 ring-blue-200 shadow-md"
                  : "border-gray-100 hover:border-gray-200 hover:shadow-sm"
              }`}
            >
              {/* Scene thumbnail placeholder */}
              <div
                className={`aspect-[4/3] bg-gradient-to-br ${
                  SCENE_GRADIENTS[scene.style] || "from-gray-100 to-gray-200"
                } flex items-center justify-center`}
              >
                <span className="text-2xl opacity-60">
                  {scene.category === "indoor" ? "🏠" : "🌿"}
                </span>
              </div>

              {/* Label */}
              <div className="p-2.5">
                <p className="text-xs font-semibold text-gray-700 truncate">{scene.name}</p>
                <p className="text-[10px] text-gray-400 truncate mt-0.5">{scene.description}</p>
              </div>

              {/* Selected check */}
              {isSceneSelected(scene.id) && (
                <div className="absolute top-2 right-2">
                  <div className="w-5 h-5 bg-blue-500 rounded-full flex items-center justify-center shadow-sm">
                    <svg className="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                </div>
              )}

              {/* Category tag */}
              <div className="absolute top-2 left-2">
                <span className="text-[9px] font-medium text-white bg-black/40 px-1.5 py-0.5 rounded-full backdrop-blur-sm">
                  {scene.category === "indoor" ? "室内" : "室外"}
                </span>
              </div>
            </motion.button>
          ))}
        </div>

        {state.selectedScenes.length > 0 && (
          <p className="text-xs text-blue-600 mt-3 font-medium">
            已选择 {state.selectedScenes.length} 个场景
          </p>
        )}
      </div>

      {/* Props Selector */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm">
        <h3 className="text-sm font-bold text-gray-800 mb-3">道具选择</h3>
        <div className="flex flex-wrap gap-2 mb-3">
          {PRESET_PROPS.map((prop) => (
            <button
              key={prop}
              onClick={() => dispatch({ type: "TOGGLE_PROP", prop })}
              className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-all ${
                state.selectedProps.includes(prop)
                  ? "border-blue-400 bg-blue-50 text-blue-700"
                  : "border-gray-200 bg-white text-gray-500 hover:border-gray-300"
              }`}
            >
              {state.selectedProps.includes(prop) && <span className="mr-0.5">&#10003; </span>}
              {prop}
            </button>
          ))}
        </div>

        {/* Custom props */}
        <div className="flex gap-2">
          <input
            type="text"
            value={customPropInput}
            onChange={(e) => setCustomPropInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAddCustomProp()}
            placeholder="自定义道具名称"
            className="flex-1 px-3 py-2 border border-gray-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-400 transition-all placeholder:text-gray-300"
          />
          <button
            onClick={handleAddCustomProp}
            disabled={!customPropInput.trim()}
            className="px-3 py-2 bg-gray-100 text-gray-600 text-xs font-medium rounded-xl hover:bg-gray-200 disabled:opacity-40 transition-all"
          >
            添加
          </button>
        </div>

        {/* Custom props display */}
        <AnimatePresence>
          {state.customProps.length > 0 && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              className="flex flex-wrap gap-2 mt-3"
            >
              {state.customProps.map((prop) => (
                <span
                  key={prop}
                  className="inline-flex items-center gap-1 px-3 py-1.5 bg-purple-50 text-purple-700 text-xs font-medium rounded-full border border-purple-200"
                >
                  {prop}
                  <button
                    onClick={() => dispatch({ type: "REMOVE_CUSTOM_PROP", prop })}
                    className="w-3.5 h-3.5 rounded-full bg-purple-200 text-purple-600 flex items-center justify-center hover:bg-purple-300 transition-colors"
                  >
                    <svg className="w-2 h-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </span>
              ))}
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Virtual Model Selection */}
      <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="text-sm font-bold text-gray-800">虚拟模特</h3>
            <p className="text-xs text-gray-400 mt-0.5">选择一位虚拟模特展示商品（可选）</p>
          </div>
          <span className="text-[10px] text-gray-400 bg-gray-100 px-2 py-0.5 rounded-full">
            可选
          </span>
        </div>

        {/* Ethnicity filter */}
        <div className="flex gap-1.5 mb-4">
          {ETHNICITY_OPTIONS.map((opt) => (
            <button
              key={opt.value}
              onClick={() => dispatch({ type: "SET_MODEL_ETHNICITY", ethnicity: opt.value })}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                state.modelEthnicity === opt.value
                  ? "bg-blue-500 text-white shadow-sm"
                  : "bg-gray-100 text-gray-500 hover:bg-gray-200"
              }`}
            >
              {opt.label}
            </button>
          ))}
        </div>

        {/* Model grid */}
        <div className="grid grid-cols-3 sm:grid-cols-6 gap-3">
          {filteredModels.map((model) => (
            <button
              key={model.id}
              onClick={() =>
                dispatch({
                  type: "SET_MODEL",
                  model:
                    state.selectedModel?.id === model.id
                      ? null
                      : { id: model.id, ethnicity: model.ethnicity, name: model.name },
                })
              }
              className={`flex flex-col items-center gap-2 p-3 rounded-xl border-2 transition-all ${
                state.selectedModel?.id === model.id
                  ? "border-blue-500 bg-blue-50 shadow-sm"
                  : "border-gray-100 bg-white hover:border-gray-200"
              }`}
            >
              {/* Model placeholder */}
              <div
                className={`w-12 h-12 rounded-full flex items-center justify-center text-lg ${
                  state.selectedModel?.id === model.id ? "bg-blue-100" : "bg-gray-100"
                }`}
              >
                {model.gender === "female" ? "👩" : "👨"}
              </div>
              <span className="text-[10px] font-medium text-gray-600 truncate w-full text-center">
                {model.name}
              </span>
            </button>
          ))}
        </div>
      </div>

      {/* Submit Button */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="flex flex-col items-center gap-3 pt-4 pb-6"
      >
        <button
          onClick={handleSubmit}
          disabled={submitting || state.selectedScenes.length === 0}
          className="group relative inline-flex items-center gap-3 px-10 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white text-lg font-bold rounded-2xl hover:from-blue-700 hover:to-purple-700 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:translate-y-0"
        >
          {submitting ? (
            <span className="flex items-center gap-3">
              <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
              </svg>
              提交中...
            </span>
          ) : (
            <>
              <svg className="w-5 h-5 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              确认并开始生成
            </>
          )}
        </button>
        <p className="text-xs text-gray-400">
          已选 {state.selectedScenes.length} 个场景
          {state.selectedProps.length + state.customProps.length > 0 &&
            ` / ${state.selectedProps.length + state.customProps.length} 个道具`}
          {state.selectedModel && ` / 模特: ${state.selectedModel.name}`}
        </p>
      </motion.div>
    </motion.div>
  );
}
