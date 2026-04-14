/** Data model for the quantum compiler dashboard. */

export interface RiemannZero {
  n: number;
  value: number;
  frequency: number;
  role: string;
  sm_interpretation: string;
  gauge_distinguished: boolean;
  formulas_using: string[];
}

export interface CompilationResult {
  name: string;
  description: string;
  formula: string;
  rule: string | number;
  registers_used: number[];
  compiled_value: number;
  experimental: number;
  deviation_pct: number;
  unit: string;
  verdict: "PASS" | "FAIL";
  compilation_trace?: TraceStep[];
}

export interface TraceStep {
  stage: string;
  [key: string]: unknown;
}

export interface CorrespondenceCell {
  concept: string;
  domain: string;
  image: string | null;
  status: "FILLED" | "PARTIAL" | "BLANK";
}

export interface CapacitorState {
  version: number;
  formulas_compiled: number;
  blank_cells: number;
  kills: number;
  cards: number;
  correspondences: number;
  last_update: string | null;
}

export interface ModularFlowResult {
  n: number;
  t: number;
  L_n: string;
  phase: string;
  phase_mod_2pi: string;
  cos_phase: string;
  sin_phase: string;
}

/** Sector color mapping */
export const SECTOR_COLORS: Record<string, string> = {
  A: "#4fc3f7",  // cosmology — cyan
  B: "#ab47bc",  // couplings — purple
  C: "#66bb6a",  // masses — green
  D: "#ffa726",  // mixing — orange
};

/** Grammar rule names */
export const RULE_NAMES: Record<string | number, string> = {
  1: "SUM",
  2: "PRODUCT",
  "3a": "YUKAWA (quark)",
  "3b": "YUKAWA (lepton)",
  4: "EXPONENTIAL",
  5: "LOG",
  6: "FRACTIONAL",
  7: "RATIO",
  8: "DIFFERENCE",
  compound: "COMPOUND",
};
