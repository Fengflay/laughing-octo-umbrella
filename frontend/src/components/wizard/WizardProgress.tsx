"use client";

import { motion } from "framer-motion";
import { useWizard } from "@/lib/wizard-context";

const STEPS = [
  { label: "模式选择", shortLabel: "模式" },
  { label: "上传与抠图", shortLabel: "上传" },
  { label: "商品属性", shortLabel: "属性" },
  { label: "风格与场景", shortLabel: "场景" },
];

export default function WizardProgress() {
  const { state, goToStep } = useWizard();
  const { currentStep } = state;

  // Don't show progress bar on step 0 (mode selection)
  if (currentStep === 0) return null;

  const progressPercent = ((currentStep) / (STEPS.length - 1)) * 100;

  return (
    <div className="mb-8">
      {/* Step indicators */}
      <div className="relative flex items-center justify-between">
        {/* Background line */}
        <div className="absolute top-4 left-0 right-0 h-0.5 bg-gray-200 rounded-full" />
        {/* Active line */}
        <motion.div
          className="absolute top-4 left-0 h-0.5 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full"
          initial={{ width: "0%" }}
          animate={{ width: `${progressPercent}%` }}
          transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
        />

        {STEPS.map((step, index) => {
          const isCompleted = index < currentStep;
          const isActive = index === currentStep;
          const isClickable = index < currentStep;

          return (
            <button
              key={index}
              onClick={() => isClickable && goToStep(index)}
              disabled={!isClickable}
              className={`relative z-10 flex flex-col items-center gap-1.5 ${
                isClickable ? "cursor-pointer" : "cursor-default"
              }`}
            >
              <motion.div
                initial={false}
                animate={{
                  scale: isActive ? 1.1 : 1,
                  backgroundColor: isCompleted
                    ? "#10b981"
                    : isActive
                      ? "#3b82f6"
                      : "#e2e8f0",
                }}
                transition={{ duration: 0.3 }}
                className="w-8 h-8 rounded-full flex items-center justify-center text-xs font-bold shadow-sm"
                style={{ color: isCompleted || isActive ? "#fff" : "#94a3b8" }}
              >
                {isCompleted ? (
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                  </svg>
                ) : (
                  index
                )}
              </motion.div>
              <span
                className={`text-[10px] font-medium transition-colors hidden sm:block ${
                  isActive ? "text-blue-600" : isCompleted ? "text-emerald-600" : "text-gray-400"
                }`}
              >
                {step.label}
              </span>
              <span
                className={`text-[10px] font-medium transition-colors sm:hidden ${
                  isActive ? "text-blue-600" : isCompleted ? "text-emerald-600" : "text-gray-400"
                }`}
              >
                {step.shortLabel}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
