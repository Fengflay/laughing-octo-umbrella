"use client";

import { createContext, useCallback, useContext, useMemo, useReducer } from "react";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

export type WizardMode = "auto" | "expert" | null;

export interface UploadedImage {
  file: File;
  localUrl: string;
  imageId?: string;
  serverUrl?: string;
}

export interface MaskEdit {
  paths: { x: number; y: number }[][];
  mode: "include" | "exclude";
}

export interface ProductAttributes {
  name: string;
  category: string;
  subCategory: string;
  material: string;
  color: string;
  audience: "male" | "female" | "unisex" | "";
  tags: string[];
  coreViewpoints: string[];
}

export interface SceneSelection {
  sceneId: string;
  sceneName: string;
  category: "indoor" | "outdoor";
}

export interface ModelPreset {
  id: string;
  ethnicity: string;
  name: string;
}

export interface WizardState {
  /** Current wizard step: 0=mode, 1=upload, 2=attributes, 3=style */
  currentStep: number;
  /** Selected mode: auto / expert */
  mode: WizardMode;
  /** Uploaded product images (multi-angle) */
  uploadedImages: UploadedImage[];
  /** Background-removed image URL */
  removedBgUrl: string | null;
  /** Whether AI bg removal is in progress */
  removingBg: boolean;
  /** Canvas mask edits for brush tool */
  maskEdits: MaskEdit[];
  /** Subject confirmed by user */
  subjectConfirmed: boolean;
  /** Product attributes */
  attributes: ProductAttributes;
  /** Style reference image */
  styleRefImage: UploadedImage | null;
  /** Selected scenes */
  selectedScenes: SceneSelection[];
  /** Selected props */
  selectedProps: string[];
  /** Custom props added by user */
  customProps: string[];
  /** Selected virtual model */
  selectedModel: ModelPreset | null;
  /** Model ethnicity filter */
  modelEthnicity: string;
  /** Error message */
  error: string | null;
}

// ---------------------------------------------------------------------------
// Actions
// ---------------------------------------------------------------------------

type WizardAction =
  | { type: "SET_STEP"; step: number }
  | { type: "SET_MODE"; mode: WizardMode }
  | { type: "ADD_IMAGE"; image: UploadedImage }
  | { type: "REMOVE_IMAGE"; index: number }
  | { type: "UPDATE_IMAGE"; index: number; updates: Partial<UploadedImage> }
  | { type: "SET_REMOVED_BG"; url: string | null }
  | { type: "SET_REMOVING_BG"; removing: boolean }
  | { type: "ADD_MASK_EDIT"; edit: MaskEdit }
  | { type: "UNDO_MASK_EDIT" }
  | { type: "CLEAR_MASK_EDITS" }
  | { type: "CONFIRM_SUBJECT"; confirmed: boolean }
  | { type: "UPDATE_ATTRIBUTES"; updates: Partial<ProductAttributes> }
  | { type: "SET_STYLE_REF"; image: UploadedImage | null }
  | { type: "TOGGLE_SCENE"; scene: SceneSelection }
  | { type: "TOGGLE_PROP"; prop: string }
  | { type: "ADD_CUSTOM_PROP"; prop: string }
  | { type: "REMOVE_CUSTOM_PROP"; prop: string }
  | { type: "SET_MODEL"; model: ModelPreset | null }
  | { type: "SET_MODEL_ETHNICITY"; ethnicity: string }
  | { type: "SET_ERROR"; error: string | null }
  | { type: "RESET" };

// ---------------------------------------------------------------------------
// Initial state
// ---------------------------------------------------------------------------

const initialAttributes: ProductAttributes = {
  name: "",
  category: "",
  subCategory: "",
  material: "",
  color: "#FFFFFF",
  audience: "",
  tags: [],
  coreViewpoints: [],
};

const initialState: WizardState = {
  currentStep: 0,
  mode: null,
  uploadedImages: [],
  removedBgUrl: null,
  removingBg: false,
  maskEdits: [],
  subjectConfirmed: false,
  attributes: initialAttributes,
  styleRefImage: null,
  selectedScenes: [],
  selectedProps: [],
  customProps: [],
  selectedModel: null,
  modelEthnicity: "",
  error: null,
};

// ---------------------------------------------------------------------------
// Reducer
// ---------------------------------------------------------------------------

function wizardReducer(state: WizardState, action: WizardAction): WizardState {
  switch (action.type) {
    case "SET_STEP":
      return { ...state, currentStep: action.step, error: null };
    case "SET_MODE":
      return { ...state, mode: action.mode };
    case "ADD_IMAGE":
      return { ...state, uploadedImages: [...state.uploadedImages, action.image] };
    case "REMOVE_IMAGE":
      return {
        ...state,
        uploadedImages: state.uploadedImages.filter((_, i) => i !== action.index),
      };
    case "UPDATE_IMAGE": {
      const images = [...state.uploadedImages];
      images[action.index] = { ...images[action.index], ...action.updates };
      return { ...state, uploadedImages: images };
    }
    case "SET_REMOVED_BG":
      return { ...state, removedBgUrl: action.url };
    case "SET_REMOVING_BG":
      return { ...state, removingBg: action.removing };
    case "ADD_MASK_EDIT":
      return { ...state, maskEdits: [...state.maskEdits, action.edit] };
    case "UNDO_MASK_EDIT":
      return { ...state, maskEdits: state.maskEdits.slice(0, -1) };
    case "CLEAR_MASK_EDITS":
      return { ...state, maskEdits: [] };
    case "CONFIRM_SUBJECT":
      return { ...state, subjectConfirmed: action.confirmed };
    case "UPDATE_ATTRIBUTES":
      return {
        ...state,
        attributes: { ...state.attributes, ...action.updates },
      };
    case "SET_STYLE_REF":
      return { ...state, styleRefImage: action.image };
    case "TOGGLE_SCENE": {
      const exists = state.selectedScenes.some((s) => s.sceneId === action.scene.sceneId);
      return {
        ...state,
        selectedScenes: exists
          ? state.selectedScenes.filter((s) => s.sceneId !== action.scene.sceneId)
          : [...state.selectedScenes, action.scene],
      };
    }
    case "TOGGLE_PROP": {
      const exists = state.selectedProps.includes(action.prop);
      return {
        ...state,
        selectedProps: exists
          ? state.selectedProps.filter((p) => p !== action.prop)
          : [...state.selectedProps, action.prop],
      };
    }
    case "ADD_CUSTOM_PROP":
      if (state.customProps.includes(action.prop)) return state;
      return { ...state, customProps: [...state.customProps, action.prop] };
    case "REMOVE_CUSTOM_PROP":
      return {
        ...state,
        customProps: state.customProps.filter((p) => p !== action.prop),
      };
    case "SET_MODEL":
      return { ...state, selectedModel: action.model };
    case "SET_MODEL_ETHNICITY":
      return { ...state, modelEthnicity: action.ethnicity };
    case "SET_ERROR":
      return { ...state, error: action.error };
    case "RESET":
      return initialState;
    default:
      return state;
  }
}

// ---------------------------------------------------------------------------
// Context
// ---------------------------------------------------------------------------

interface WizardContextValue {
  state: WizardState;
  dispatch: React.Dispatch<WizardAction>;
  // Convenience helpers
  goToStep: (step: number) => void;
  nextStep: () => void;
  prevStep: () => void;
}

const WizardContext = createContext<WizardContextValue>({
  state: initialState,
  dispatch: () => {},
  goToStep: () => {},
  nextStep: () => {},
  prevStep: () => {},
});

export function WizardProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(wizardReducer, initialState);

  const goToStep = useCallback(
    (step: number) => dispatch({ type: "SET_STEP", step }),
    [],
  );

  const nextStep = useCallback(() => {
    dispatch({ type: "SET_STEP", step: state.currentStep + 1 });
  }, [state.currentStep]);

  const prevStep = useCallback(() => {
    if (state.currentStep > 0) {
      dispatch({ type: "SET_STEP", step: state.currentStep - 1 });
    }
  }, [state.currentStep]);

  const value = useMemo(
    () => ({ state, dispatch, goToStep, nextStep, prevStep }),
    [state, goToStep, nextStep, prevStep],
  );

  return (
    <WizardContext.Provider value={value}>{children}</WizardContext.Provider>
  );
}

export function useWizard(): WizardContextValue {
  return useContext(WizardContext);
}
