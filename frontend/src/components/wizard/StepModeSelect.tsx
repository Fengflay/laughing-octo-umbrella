"use client";

import { motion } from "framer-motion";
import { useWizard } from "@/lib/wizard-context";

const cardVariants = {
  hidden: { opacity: 0, y: 40 },
  visible: (i: number) => ({
    opacity: 1,
    y: 0,
    transition: { delay: 0.15 + i * 0.12, duration: 0.5, ease: [0.22, 1, 0.36, 1] as const },
  }),
};

export default function StepModeSelect() {
  const { dispatch, nextStep } = useWizard();

  const selectMode = (mode: "auto" | "expert") => {
    dispatch({ type: "SET_MODE", mode });
    nextStep();
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] px-4">
      {/* Title */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
        className="text-center mb-10"
      >
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-900 mb-3">
          选择你的创作模式
        </h1>
        <p className="text-sm sm:text-base text-gray-400 max-w-md mx-auto">
          无论是快速出图还是精细调控，AI 都会为你生成专业的商品场景图
        </p>
      </motion.div>

      {/* Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 sm:gap-6 w-full max-w-2xl">
        {/* Auto Mode Card */}
        <motion.button
          custom={0}
          variants={cardVariants}
          initial="hidden"
          animate="visible"
          whileHover={{ y: -6, boxShadow: "0 20px 40px -12px rgba(59, 130, 246, 0.2)" }}
          whileTap={{ scale: 0.98 }}
          onClick={() => selectMode("auto")}
          className="relative group bg-white rounded-2xl border-2 border-gray-100 p-6 sm:p-8 text-left transition-colors hover:border-blue-300 overflow-hidden"
        >
          {/* Background gradient */}
          <div className="absolute inset-0 bg-gradient-to-br from-blue-50/80 to-purple-50/50 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

          <div className="relative">
            {/* Icon */}
            <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center mb-5 shadow-lg shadow-blue-500/20 group-hover:shadow-blue-500/30 transition-shadow">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>

            {/* Tag */}
            <span className="inline-block text-[10px] font-bold text-blue-600 bg-blue-100 px-2.5 py-0.5 rounded-full mb-3 uppercase tracking-wide">
              推荐新手
            </span>

            <h2 className="text-lg sm:text-xl font-bold text-gray-900 mb-2">
              一键全自动
            </h2>
            <p className="text-sm text-gray-500 leading-relaxed">
              上传商品图即可，AI 自动识别商品属性并匹配最优场景，快速生成专业级商品图
            </p>

            {/* Features */}
            <div className="mt-5 space-y-2">
              {["AI 智能识别商品", "自动匹配最优场景", "一键生成高品质图片"].map((feature) => (
                <div key={feature} className="flex items-center gap-2 text-xs text-gray-400">
                  <svg className="w-3.5 h-3.5 text-blue-400 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  {feature}
                </div>
              ))}
            </div>
          </div>
        </motion.button>

        {/* Expert Mode Card */}
        <motion.button
          custom={1}
          variants={cardVariants}
          initial="hidden"
          animate="visible"
          whileHover={{ y: -6, boxShadow: "0 20px 40px -12px rgba(147, 51, 234, 0.15)" }}
          whileTap={{ scale: 0.98 }}
          onClick={() => selectMode("expert")}
          className="relative group bg-white rounded-2xl border-2 border-gray-100 p-6 sm:p-8 text-left transition-colors hover:border-purple-300 overflow-hidden"
        >
          {/* Background gradient */}
          <div className="absolute inset-0 bg-gradient-to-br from-purple-50/80 to-pink-50/50 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

          <div className="relative">
            {/* Icon */}
            <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-purple-500 to-purple-600 flex items-center justify-center mb-5 shadow-lg shadow-purple-500/20 group-hover:shadow-purple-500/30 transition-shadow">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
              </svg>
            </div>

            {/* Tag */}
            <span className="inline-block text-[10px] font-bold text-purple-600 bg-purple-100 px-2.5 py-0.5 rounded-full mb-3 uppercase tracking-wide">
              精细控制
            </span>

            <h2 className="text-lg sm:text-xl font-bold text-gray-900 mb-2">
              专家自定义
            </h2>
            <p className="text-sm text-gray-500 leading-relaxed">
              完整的分步引导流程，精确控制商品属性、场景风格、道具搭配与虚拟模特
            </p>

            {/* Features */}
            <div className="mt-5 space-y-2">
              {["手动调节抠图细节", "精确设定商品属性", "自选场景与道具搭配"].map((feature) => (
                <div key={feature} className="flex items-center gap-2 text-xs text-gray-400">
                  <svg className="w-3.5 h-3.5 text-purple-400 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  {feature}
                </div>
              ))}
            </div>
          </div>
        </motion.button>
      </div>
    </div>
  );
}
