import React from "react";
import type { CompilationResult } from "./types";
import { SECTOR_COLORS, RULE_NAMES } from "./types";

// Static master table results for initial display
const STATIC_RESULTS: CompilationResult[] = [
  { name: "log_CC", description: "cosmological constant", formula: "γ₁·π²/2 − 0.15/γ₂ + 0.03/γ₃ − 0.01·ln(γ₂/γ₁)", rule: 4, registers_used: [1,2,3], compiled_value: 69.7421690, experimental: 69.7421709, deviation_pct: 0.0000047, unit: "", verdict: "PASS" },
  { name: "m_W", description: "W boson mass", formula: "γ₂ + γ₁₃", rule: 1, registers_used: [2,13], compiled_value: 80.3691, experimental: 80.3692, deviation_pct: 0.012, unit: "GeV", verdict: "PASS" },
  { name: "N_eff", description: "neutrino species", formula: "γ₆^(1/3)", rule: 6, registers_used: [6], compiled_value: 3.34973, experimental: 3.35, deviation_pct: 0.0082, unit: "", verdict: "PASS" },
  { name: "m_t", description: "top quark mass", formula: "γ₃·γ₈/(2π)", rule: "3a", registers_used: [3,8], compiled_value: 172.468, experimental: 172.76, deviation_pct: 0.17, unit: "GeV", verdict: "PASS" },
  { name: "1/alpha", description: "fine structure constant", formula: "γ₁·γ₄/π + 0.1·log(π)", rule: 2, registers_used: [1,4], compiled_value: 137.003, experimental: 137.036, deviation_pct: 0.024, unit: "", verdict: "PASS" },
  { name: "m_b", description: "bottom quark mass", formula: "log(γ₁₅)", rule: 5, registers_used: [15], compiled_value: 4.17612, experimental: 4.18, deviation_pct: 0.093, unit: "GeV", verdict: "PASS" },
  { name: "n_s", description: "spectral tilt", formula: "γ₉/γ₁₀", rule: 7, registers_used: [9,10], compiled_value: 0.96447, experimental: 0.965, deviation_pct: 0.056, unit: "", verdict: "PASS" },
  { name: "m_d", description: "down quark mass", formula: "γ₉ − γ₈", rule: 8, registers_used: [9,8], compiled_value: 4.67808, experimental: 4.67, deviation_pct: 0.17, unit: "MeV", verdict: "PASS" },
];

interface Props {
  result?: CompilationResult | null;
  allResults?: CompilationResult[];
}

/** Panel 5: Compiled formula output — LaTeX + value vs experiment */
export function FormulaOutput({ result, allResults = STATIC_RESULTS }: Props) {
  const display = result || allResults[0];
  const sectorColor = display ? SECTOR_COLORS[display.verdict === "PASS" ? "C" : "D"] : "#666";

  return (
    <div style={{ background: "#111118", borderRadius: 8, padding: 16, height: "100%" }}>
      <h3 style={{ margin: "0 0 8px", color: "#8af", fontSize: 13, letterSpacing: 1 }}>
        FORMULA OUTPUT
      </h3>

      {display && (
        <div style={{ marginBottom: 12 }}>
          {/* Main formula */}
          <div style={{ fontSize: 16, color: "#fff", fontWeight: 700, marginBottom: 4 }}>
            {display.name}
            <span style={{ fontSize: 11, color: "#888", fontWeight: 400, marginLeft: 8 }}>
              {display.description}
            </span>
          </div>

          {/* Formula expression */}
          <div style={{
            padding: "8px 12px", borderRadius: 4, background: "#1a1a22",
            fontFamily: "'Fira Code', monospace", fontSize: 14, color: "#4fc3f7",
            border: "1px solid #333", marginBottom: 8,
          }}>
            {display.formula}
          </div>

          {/* Value comparison */}
          <div style={{ display: "flex", gap: 20, fontSize: 12 }}>
            <div>
              <div style={{ color: "#666", fontSize: 9, marginBottom: 2 }}>COMPILED</div>
              <div style={{ color: "#66bb6a", fontWeight: 600 }}>
                {typeof display.compiled_value === "number"
                  ? display.compiled_value.toPrecision(7)
                  : display.compiled_value}
                {display.unit && <span style={{ color: "#888", marginLeft: 4 }}>{display.unit}</span>}
              </div>
            </div>
            <div>
              <div style={{ color: "#666", fontSize: 9, marginBottom: 2 }}>MEASURED</div>
              <div style={{ color: "#ffa726", fontWeight: 600 }}>
                {display.experimental}
                {display.unit && <span style={{ color: "#888", marginLeft: 4 }}>{display.unit}</span>}
              </div>
            </div>
            <div>
              <div style={{ color: "#666", fontSize: 9, marginBottom: 2 }}>MATCH</div>
              <div style={{
                color: display.deviation_pct < 0.1 ? "#66bb6a" : "#ffa726",
                fontWeight: 600,
              }}>
                {display.deviation_pct < 0.001
                  ? `${(display.deviation_pct * 10000).toFixed(1)} ppm`
                  : `${display.deviation_pct.toFixed(3)}%`}
              </div>
            </div>
            <div>
              <div style={{ color: "#666", fontSize: 9, marginBottom: 2 }}>RULE</div>
              <div style={{ color: "#ab47bc", fontWeight: 600 }}>
                {RULE_NAMES[display.rule] || display.rule}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Results list */}
      <div style={{ maxHeight: 100, overflowY: "auto", fontSize: 10 }}>
        {allResults.map((r) => (
          <div key={r.name} style={{
            display: "flex", justifyContent: "space-between", padding: "2px 0",
            borderBottom: "1px solid #1a1a22", color: "#888",
          }}>
            <span style={{ color: r.verdict === "PASS" ? "#66bb6a" : "#f44" }}>
              {r.verdict === "PASS" ? "✓" : "✗"} {r.name}
            </span>
            <span>{r.formula}</span>
            <span style={{ color: r.deviation_pct < 0.1 ? "#66bb6a" : "#ffa726" }}>
              {r.deviation_pct < 0.001
                ? `${(r.deviation_pct * 10000).toFixed(0)} ppm`
                : `${r.deviation_pct.toFixed(3)}%`}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
