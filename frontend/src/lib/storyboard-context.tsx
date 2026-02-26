"use client";

import {
  createContext,
  useCallback,
  useContext,
  useMemo,
  useState,
} from "react";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export type ImageType =
  | "white_bg"
  | "material"
  | "detail"
  | "scene"
  | "flat_lay"
  | "model";

export const IMAGE_TYPE_LABELS: Record<ImageType, string> = {
  white_bg: "白底图",
  material: "材质图",
  detail: "细节图",
  scene: "场景图",
  flat_lay: "平铺图",
  model: "模特图",
};

export interface GridCell {
  id: string;
  index: number;
  imageType: ImageType;
  previewUrl: string | null;
  resultUrl: string | null;
  status: "idle" | "preview" | "generating" | "completed" | "failed";
  progress: number;
  error: string | null;
  locked: boolean; // grid slot 1 is locked
}

export interface AmbientPreset {
  id: string;
  name: string;
  description: string;
  thumbnail: string;
  colorTemp: string; // CSS gradient for preview
}

export const AMBIENT_PRESETS: AmbientPreset[] = [
  {
    id: "warm_afternoon",
    name: "暖阳午后",
    description: "温暖的自然光线，金色调",
    thumbnail: "/placeholder-warm.jpg",
    colorTemp: "linear-gradient(135deg, #fbbf24, #f59e0b)",
  },
  {
    id: "cool_industrial",
    name: "清冷工业风",
    description: "冷色调，硬朗光影",
    thumbnail: "/placeholder-cool.jpg",
    colorTemp: "linear-gradient(135deg, #64748b, #475569)",
  },
  {
    id: "soft_natural",
    name: "自然柔光",
    description: "柔和的散射光，自然色调",
    thumbnail: "/placeholder-soft.jpg",
    colorTemp: "linear-gradient(135deg, #86efac, #67e8f9)",
  },
  {
    id: "studio_bright",
    name: "棚拍明亮",
    description: "专业影棚灯光，高亮度",
    thumbnail: "/placeholder-studio.jpg",
    colorTemp: "linear-gradient(135deg, #f8fafc, #e2e8f0)",
  },
  {
    id: "moody_dark",
    name: "暗调质感",
    description: "低调光线，深色背景",
    thumbnail: "/placeholder-moody.jpg",
    colorTemp: "linear-gradient(135deg, #1e293b, #0f172a)",
  },
  {
    id: "pink_dreamy",
    name: "梦幻粉调",
    description: "粉色柔和氛围，少女感",
    thumbnail: "/placeholder-pink.jpg",
    colorTemp: "linear-gradient(135deg, #fda4af, #f9a8d4)",
  },
];

export interface StoryboardState {
  // Grid cells
  cells: GridCell[];
  setCells: (cells: GridCell[]) => void;
  swapCells: (fromIndex: number, toIndex: number) => void;
  updateCellType: (cellId: string, newType: ImageType) => void;
  updateCellStatus: (
    cellId: string,
    status: GridCell["status"],
    data?: Partial<GridCell>,
  ) => void;

  // Ambient lock
  selectedAmbient: string | null;
  ambientLocked: boolean;
  setSelectedAmbient: (id: string | null) => void;
  setAmbientLocked: (locked: boolean) => void;

  // Generation
  phase: "storyboard" | "generating" | "results";
  setPhase: (phase: StoryboardState["phase"]) => void;
  taskId: string | null;
  setTaskId: (taskId: string | null) => void;

  // Results page - additional images
  additionalImages: GridCell[];
  addAdditionalImages: (images: GridCell[]) => void;

  // Wizard data bridge
  wizardData: WizardBridgeData | null;
  setWizardData: (data: WizardBridgeData | null) => void;

  // Reset
  reset: () => void;
}

export interface WizardBridgeData {
  imageId: string;
  productType: string;
  removeBg: boolean;
  style?: string;
  productDetails?: string;
}

// ---------------------------------------------------------------------------
// Default cells
// ---------------------------------------------------------------------------

const DEFAULT_IMAGE_TYPES: ImageType[] = [
  "white_bg",
  "scene",
  "detail",
  "material",
  "scene",
  "flat_lay",
  "model",
  "detail",
  "scene",
];

function createDefaultCells(): GridCell[] {
  return DEFAULT_IMAGE_TYPES.map((type, i) => ({
    id: `cell-${i}`,
    index: i,
    imageType: type,
    previewUrl: null,
    resultUrl: null,
    status: "idle" as const,
    progress: 0,
    error: null,
    locked: i === 0, // first cell is locked as white_bg
  }));
}

// ---------------------------------------------------------------------------
// Context
// ---------------------------------------------------------------------------

const StoryboardContext = createContext<StoryboardState | null>(null);

export function StoryboardProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  const [cells, setCellsRaw] = useState<GridCell[]>(createDefaultCells);
  const [selectedAmbient, setSelectedAmbient] = useState<string | null>(
    "warm_afternoon",
  );
  const [ambientLocked, setAmbientLocked] = useState(false);
  const [phase, setPhase] = useState<StoryboardState["phase"]>("storyboard");
  const [taskId, setTaskId] = useState<string | null>(null);
  const [additionalImages, setAdditionalImages] = useState<GridCell[]>([]);
  const [wizardData, setWizardData] = useState<WizardBridgeData | null>(null);

  const setCells = useCallback((newCells: GridCell[]) => {
    setCellsRaw(newCells);
  }, []);

  const swapCells = useCallback((fromIndex: number, toIndex: number) => {
    setCellsRaw((prev) => {
      const next = [...prev];
      const temp = next[fromIndex];
      next[fromIndex] = { ...next[toIndex], index: fromIndex };
      next[toIndex] = { ...temp, index: toIndex };
      // Preserve locked status based on position (slot 0 is always locked)
      next[0] = { ...next[0], locked: true };
      if (fromIndex !== 0 && toIndex !== 0) {
        next[fromIndex] = { ...next[fromIndex], locked: false };
        next[toIndex] = { ...next[toIndex], locked: false };
      }
      return next;
    });
  }, []);

  const updateCellType = useCallback(
    (cellId: string, newType: ImageType) => {
      setCellsRaw((prev) =>
        prev.map((cell) =>
          cell.id === cellId ? { ...cell, imageType: newType } : cell,
        ),
      );
    },
    [],
  );

  const updateCellStatus = useCallback(
    (
      cellId: string,
      status: GridCell["status"],
      data?: Partial<GridCell>,
    ) => {
      setCellsRaw((prev) =>
        prev.map((cell) =>
          cell.id === cellId ? { ...cell, status, ...data } : cell,
        ),
      );
    },
    [],
  );

  const addAdditionalImages = useCallback((images: GridCell[]) => {
    setAdditionalImages((prev) => [...prev, ...images]);
  }, []);

  const reset = useCallback(() => {
    setCellsRaw(createDefaultCells());
    setSelectedAmbient("warm_afternoon");
    setAmbientLocked(false);
    setPhase("storyboard");
    setTaskId(null);
    setAdditionalImages([]);
  }, []);

  const value = useMemo<StoryboardState>(
    () => ({
      cells,
      setCells,
      swapCells,
      updateCellType,
      updateCellStatus,
      selectedAmbient,
      ambientLocked,
      setSelectedAmbient,
      setAmbientLocked,
      phase,
      setPhase,
      taskId,
      setTaskId,
      additionalImages,
      addAdditionalImages,
      wizardData,
      setWizardData,
      reset,
    }),
    [
      cells,
      setCells,
      swapCells,
      updateCellType,
      updateCellStatus,
      selectedAmbient,
      ambientLocked,
      setSelectedAmbient,
      setAmbientLocked,
      phase,
      setPhase,
      taskId,
      setTaskId,
      additionalImages,
      addAdditionalImages,
      wizardData,
      setWizardData,
      reset,
    ],
  );

  return (
    <StoryboardContext.Provider value={value}>
      {children}
    </StoryboardContext.Provider>
  );
}

export function useStoryboard(): StoryboardState {
  const ctx = useContext(StoryboardContext);
  if (!ctx) {
    throw new Error("useStoryboard must be used within StoryboardProvider");
  }
  return ctx;
}
