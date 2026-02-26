"use client";

import { useCallback, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { motion, AnimatePresence } from "framer-motion";
import { useWizard } from "@/lib/wizard-context";
import { uploadImage, removeBackground } from "@/lib/api";
import BrushTool from "./BrushTool";

const IMAGE_LABELS = ["正面图", "侧面图", "斜面图"];

export default function StepUpload() {
  const router = useRouter();
  const { state, dispatch, nextStep } = useWizard();
  const [dragActive, setDragActive] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [showBrush, setShowBrush] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFiles = useCallback(
    async (files: FileList | File[]) => {
      const fileArray = Array.from(files).slice(0, 3 - state.uploadedImages.length);
      if (fileArray.length === 0) return;

      setUploading(true);
      dispatch({ type: "SET_ERROR", error: null });

      for (const file of fileArray) {
        const localUrl = URL.createObjectURL(file);
        const imageIndex = state.uploadedImages.length;
        dispatch({ type: "ADD_IMAGE", image: { file, localUrl } });

        try {
          const result = await uploadImage(file);
          dispatch({
            type: "UPDATE_IMAGE",
            index: imageIndex,
            updates: { imageId: result.image_id, serverUrl: result.url },
          });
        } catch (err) {
          // Demo mode fallback: catch network errors, auth errors, and backend issues
          const errMsg = err instanceof Error ? err.message : String(err);
          const isRecoverable =
            err instanceof TypeError ||
            /fetch|network|ECONNREFUSED|未登入|401|登入|Upload failed/i.test(errMsg);
          if (isRecoverable) {
            dispatch({
              type: "UPDATE_IMAGE",
              index: imageIndex,
              updates: { imageId: `demo-${Date.now()}` },
            });
            dispatch({
              type: "SET_ERROR",
              error: "使用演示模式（未登入或后端未就绪，可继续体验完整流程）",
            });
          } else {
            dispatch({
              type: "SET_ERROR",
              error: errMsg || "上传失败",
            });
          }
        }
      }

      setUploading(false);
    },
    [state.uploadedImages.length, dispatch],
  );

  const handleDrag = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") setDragActive(true);
    else if (e.type === "dragleave") setDragActive(false);
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault();
      e.stopPropagation();
      setDragActive(false);
      if (e.dataTransfer.files?.length) handleFiles(e.dataTransfer.files);
    },
    [handleFiles],
  );

  const handleFileSelect = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      if (e.target.files?.length) handleFiles(e.target.files);
    },
    [handleFiles],
  );

  const handleRemoveBg = useCallback(async () => {
    const firstImage = state.uploadedImages[0];
    if (!firstImage?.imageId) return;

    dispatch({ type: "SET_REMOVING_BG", removing: true });
    dispatch({ type: "SET_ERROR", error: null });

    try {
      const result = await removeBackground(firstImage.imageId);
      dispatch({ type: "SET_REMOVED_BG", url: result.removed_bg_url });
    } catch (err) {
      const errMsg = err instanceof Error ? err.message : String(err);
      const isRecoverable =
        err instanceof TypeError ||
        /fetch|network|ECONNREFUSED|未登入|401|登入|Background removal failed/i.test(errMsg);
      if (isRecoverable) {
        // Demo mode: use the original image as the "removed bg" result
        dispatch({ type: "SET_REMOVED_BG", url: firstImage.localUrl });
        dispatch({
          type: "SET_ERROR",
          error: "使用演示模式（未登入或服务未就绪，以原图代替抠图结果）",
        });
      } else {
        dispatch({
          type: "SET_ERROR",
          error: errMsg || "抠图失败",
        });
      }
    } finally {
      dispatch({ type: "SET_REMOVING_BG", removing: false });
    }
  }, [state.uploadedImages, dispatch]);

  const handleConfirmSubject = useCallback(() => {
    dispatch({ type: "CONFIRM_SUBJECT", confirmed: true });
    if (state.mode === "auto") {
      router.push("/storyboard");
    } else {
      nextStep();
    }
  }, [dispatch, nextStep, state.mode, router]);

  const hasImages = state.uploadedImages.length > 0;
  const hasServerImage = state.uploadedImages.some((img) => img.imageId);
  const canUploadMore = state.uploadedImages.length < 3;

  return (
    <motion.div
      initial={{ opacity: 0, x: 40 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -40 }}
      transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
      className="space-y-6"
    >
      {/* Upload area */}
      {!hasImages && (
        <div
          className={`relative overflow-hidden rounded-2xl transition-all duration-300 ${
            dragActive
              ? "ring-2 ring-blue-400 ring-offset-2 scale-[1.005]"
              : "ring-1 ring-gray-200 hover:ring-gray-300"
          } ${uploading ? "opacity-60 pointer-events-none" : ""}`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
        >
          <div
            className={`absolute inset-0 transition-opacity duration-300 pointer-events-none ${
              dragActive ? "opacity-100" : "opacity-0"
            }`}
            style={{
              background:
                "linear-gradient(135deg, rgba(59,130,246,0.06) 0%, rgba(147,51,234,0.06) 100%)",
            }}
          />

          <label className="block cursor-pointer bg-white/90">
            <div className="flex flex-col items-center gap-4 p-10 sm:p-16">
              <div
                className={`w-20 h-20 rounded-2xl flex items-center justify-center transition-all duration-300 ${
                  dragActive
                    ? "bg-blue-100 scale-110"
                    : "bg-gradient-to-br from-blue-50 to-purple-50"
                }`}
              >
                <svg
                  className={`w-10 h-10 transition-all duration-300 ${
                    dragActive ? "text-blue-500 -translate-y-1" : "text-gray-400"
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={1.5}
                    d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                  />
                </svg>
              </div>

              <div className="text-center space-y-2">
                <p
                  className={`text-lg font-semibold transition-colors ${
                    dragActive ? "text-blue-600" : "text-gray-700"
                  }`}
                >
                  {dragActive ? "松开即可上传" : "拖拽商品图片到这里"}
                </p>
                <p className="text-sm text-gray-400">
                  支持上传多张参考图（正面、侧面、斜面），最多 3 张
                </p>
                <p className="text-xs text-gray-300">JPG, PNG, WebP，单张最大 10MB</p>
              </div>

              <div className="px-8 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white text-sm font-medium rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:-translate-y-0.5">
                选择文件上传
              </div>
            </div>
            <input
              ref={fileInputRef}
              type="file"
              accept=".jpg,.jpeg,.png,.webp"
              multiple
              className="hidden"
              onChange={handleFileSelect}
              disabled={uploading}
            />
          </label>
        </div>
      )}

      {/* Upload spinner */}
      {uploading && (
        <div className="flex items-center justify-center gap-3 py-3 animate-fade-in">
          <div className="relative w-5 h-5">
            <div className="absolute inset-0 rounded-full border-2 border-blue-200" />
            <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
          </div>
          <span className="text-sm font-medium text-blue-600">上传中...</span>
        </div>
      )}

      {/* Uploaded images grid */}
      <AnimatePresence>
        {hasImages && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="space-y-4"
          >
            <div className="flex items-center justify-between">
              <h3 className="text-sm font-semibold text-gray-700">已上传的商品图</h3>
              {canUploadMore && (
                <label className="text-xs text-blue-500 hover:text-blue-700 cursor-pointer font-medium transition-colors">
                  + 添加更多
                  <input
                    type="file"
                    accept=".jpg,.jpeg,.png,.webp"
                    multiple
                    className="hidden"
                    onChange={handleFileSelect}
                  />
                </label>
              )}
            </div>

            <div className="grid grid-cols-3 gap-3">
              {state.uploadedImages.map((img, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: index * 0.1 }}
                  className="relative group"
                >
                  <div className="aspect-square rounded-xl overflow-hidden border border-gray-200 bg-gray-50">
                    <img
                      src={img.serverUrl || img.localUrl}
                      alt={`Product ${index + 1}`}
                      className="w-full h-full object-contain"
                    />
                  </div>
                  {/* Label */}
                  <span className="absolute bottom-1.5 left-1.5 text-[10px] bg-black/60 text-white px-2 py-0.5 rounded-full backdrop-blur-sm">
                    {IMAGE_LABELS[index] || `参考图 ${index + 1}`}
                  </span>
                  {/* Remove button */}
                  <button
                    onClick={() => dispatch({ type: "REMOVE_IMAGE", index })}
                    className="absolute top-1.5 right-1.5 w-6 h-6 bg-black/60 text-white rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-500"
                  >
                    <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                  {/* Upload status indicator */}
                  {!img.imageId && (
                    <div className="absolute inset-0 bg-white/50 flex items-center justify-center rounded-xl">
                      <div className="relative w-5 h-5">
                        <div className="absolute inset-0 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
                      </div>
                    </div>
                  )}
                </motion.div>
              ))}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* AI Background Removal */}
      {hasServerImage && !state.removedBgUrl && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm"
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-semibold text-gray-700">AI 智能抠图</h3>
              <p className="text-xs text-gray-400 mt-0.5">自动去除背景，保留商品主体</p>
            </div>
            <button
              onClick={handleRemoveBg}
              disabled={state.removingBg}
              className="px-4 py-2 bg-gradient-to-r from-blue-500 to-blue-600 text-white text-sm font-medium rounded-xl hover:from-blue-600 hover:to-blue-700 disabled:opacity-50 transition-all shadow-sm hover:shadow-md"
            >
              {state.removingBg ? (
                <span className="flex items-center gap-2">
                  <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  处理中...
                </span>
              ) : (
                "开始抠图"
              )}
            </button>
          </div>
        </motion.div>
      )}

      {/* Background removed preview + brush tool */}
      <AnimatePresence>
        {state.removedBgUrl && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="space-y-4"
          >
            {/* Before/After comparison */}
            {!showBrush && (
              <div className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm">
                <div className="flex items-center justify-between mb-3">
                  <h3 className="text-sm font-semibold text-gray-700">抠图结果</h3>
                  <button
                    onClick={() => setShowBrush(true)}
                    className="text-xs text-blue-500 hover:text-blue-700 font-medium flex items-center gap-1 transition-colors"
                  >
                    <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                    </svg>
                    手动修正
                  </button>
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <div className="space-y-1.5">
                    <p className="text-xs text-gray-500 text-center font-medium">原图</p>
                    <div className="border border-gray-200 rounded-xl overflow-hidden bg-gray-50 aspect-square">
                      <img
                        src={state.uploadedImages[0]?.serverUrl || state.uploadedImages[0]?.localUrl}
                        alt="Original"
                        className="w-full h-full object-contain"
                      />
                    </div>
                  </div>
                  <div className="space-y-1.5">
                    <p className="text-xs text-gray-500 text-center font-medium">抠图后</p>
                    <div className="border border-gray-200 rounded-xl overflow-hidden checkerboard aspect-square">
                      <img
                        src={state.removedBgUrl}
                        alt="Background removed"
                        className="w-full h-full object-contain"
                      />
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* Brush tool */}
            {showBrush && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                className="bg-white rounded-2xl border border-gray-200/80 p-5 shadow-sm"
              >
                <div className="flex items-center justify-between mb-3">
                  <h3 className="text-sm font-semibold text-gray-700">手动修正抠图</h3>
                  <button
                    onClick={() => setShowBrush(false)}
                    className="text-xs text-gray-400 hover:text-gray-600 font-medium transition-colors"
                  >
                    完成修正
                  </button>
                </div>
                <BrushTool imageUrl={state.removedBgUrl} />
              </motion.div>
            )}

            {/* Confirm button */}
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.3 }}
              className="flex justify-center pt-2"
            >
              <button
                onClick={handleConfirmSubject}
                className="group inline-flex items-center gap-2.5 px-8 py-3.5 bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold rounded-2xl hover:from-blue-700 hover:to-blue-800 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5"
              >
                <svg className="w-5 h-5 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                </svg>
                确认主体，进入下一步
              </button>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Error display */}
      <AnimatePresence>
        {state.error && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.95 }}
            className="bg-red-50 border border-red-200 text-red-700 p-3.5 rounded-xl text-sm flex items-center gap-2"
          >
            <svg className="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            {state.error}
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
