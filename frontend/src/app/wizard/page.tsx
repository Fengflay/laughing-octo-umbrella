"use client";

import { AnimatePresence, motion } from "framer-motion";
import { WizardProvider, useWizard } from "@/lib/wizard-context";
import WizardProgress from "@/components/wizard/WizardProgress";
import StepModeSelect from "@/components/wizard/StepModeSelect";
import StepUpload from "@/components/wizard/StepUpload";
import StepAttributes from "@/components/wizard/StepAttributes";
import StepStyleScene from "@/components/wizard/StepStyleScene";

function WizardContent() {
  const { state, prevStep } = useWizard();
  const { currentStep } = state;

  return (
    <div className="min-h-[60vh]">
      {/* Progress bar */}
      <WizardProgress />

      {/* Back button (shown after step 0) */}
      {currentStep > 0 && (
        <motion.button
          initial={{ opacity: 0, x: -10 }}
          animate={{ opacity: 1, x: 0 }}
          onClick={prevStep}
          className="flex items-center gap-1.5 text-sm text-gray-400 hover:text-gray-700 mb-4 transition-colors group"
        >
          <svg
            className="w-4 h-4 transition-transform group-hover:-translate-x-0.5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          返回上一步
        </motion.button>
      )}

      {/* Step content */}
      <AnimatePresence mode="wait">
        {currentStep === 0 && (
          <motion.div key="step-0">
            <StepModeSelect />
          </motion.div>
        )}
        {currentStep === 1 && (
          <motion.div key="step-1">
            <StepUpload />
          </motion.div>
        )}
        {currentStep === 2 && (
          <motion.div key="step-2">
            <StepAttributes />
          </motion.div>
        )}
        {currentStep === 3 && (
          <motion.div key="step-3">
            <StepStyleScene />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export default function WizardPage() {
  return (
    <WizardProvider>
      <WizardContent />
    </WizardProvider>
  );
}
