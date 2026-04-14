import React, { useState } from "react";
import type { RiemannZero, CompilationResult } from "./types";

// Static data — first 15 Riemann zeros with metadata
const STATIC_REGISTERS: RiemannZero[] = [
  { n: 1, value: 14.1347, frequency: 11, role: "FOUNDATIONAL", sm_interpretation: "U(1) singlet", gauge_distinguished: true, formulas_using: ["log_CC","1/alpha","xi","J_CKM","m_u","m_s","sin2_theta12_PMNS","delta_CP_PMNS"] },
  { n: 2, value: 21.0220, frequency: 4, role: "Higgs/EW", sm_interpretation: "Higgs scalar", gauge_distinguished: false, formulas_using: ["log_CC","m_H","m_W","sin2_theta12_PMNS"] },
  { n: 3, value: 25.0109, frequency: 3, role: "3rd gen", sm_interpretation: "Generation 3", gauge_distinguished: false, formulas_using: ["log_CC","m_t","sin2_theta12_PMNS"] },
  { n: 4, value: 30.4249, frequency: 3, role: "EW partner of γ₁", sm_interpretation: "EW unbroken", gauge_distinguished: true, formulas_using: ["1/alpha","m_t_over_m_W","m_u"] },
  { n: 5, value: 32.9351, frequency: 3, role: "Mirror brane", sm_interpretation: "5D compact", gauge_distinguished: false, formulas_using: ["xi","m_W_over_m_Z","V_us_over_V_cb"] },
  { n: 6, value: 37.5862, frequency: 6, role: "EW WORKHORSE", sm_interpretation: "Z₆ center", gauge_distinguished: true, formulas_using: ["N_eff","m_H","m_c","1/alpha_2","sin_theta23_CKM","m_W_over_m_Z"] },
  { n: 7, value: 40.9187, frequency: 2, role: "Lepton", sm_interpretation: "Lepton sector", gauge_distinguished: false, formulas_using: ["t_0","m_tau","m_mu"] },
  { n: 8, value: 43.3271, frequency: 4, role: "SU(3) ADJOINT", sm_interpretation: "8 gluons", gauge_distinguished: true, formulas_using: ["m_t","m_tau","m_mu","m_d","m_tau_over_m_mu"] },
  { n: 9, value: 48.0052, frequency: 6, role: "QUARK/COSMO HUB", sm_interpretation: "Quark-cosmo bridge", gauge_distinguished: false, formulas_using: ["n_s","m_c","m_d","Dm2_ratio","sin2_2theta12_PMNS","delta_CP_PMNS"] },
  { n: 10, value: 49.7738, frequency: 5, role: "EW breaking", sm_interpretation: "EW breaking scale", gauge_distinguished: false, formulas_using: ["n_s","v","m_t_over_m_b","sin_theta12_CKM","delta_CP_CKM","sum_m_nu"] },
  { n: 11, value: 52.9703, frequency: 4, role: "H₀/m_Z/α₃", sm_interpretation: "Strong-cosmo link", gauge_distinguished: false, formulas_using: ["H_0","m_Z","1/alpha_3","sin_theta12_CKM"] },
  { n: 12, value: 56.4462, frequency: 2, role: "PMNS", sm_interpretation: "Neutrino sector", gauge_distinguished: false, formulas_using: ["sin2_2theta12_PMNS"] },
  { n: 13, value: 59.3470, frequency: 3, role: "Weak/cosmo", sm_interpretation: "Weak-cosmo bridge", gauge_distinguished: false, formulas_using: ["m_W","Y_p","delta_CP_CKM","sin2_2theta13_PMNS"] },
  { n: 14, value: 60.8318, frequency: 1, role: "Baryogenesis", sm_interpretation: "Baryogenesis", gauge_distinguished: false, formulas_using: ["eta_10"] },
  { n: 15, value: 65.1125, frequency: 4, role: "Heavy quark", sm_interpretation: "Heavy quark-ν link", gauge_distinguished: false, formulas_using: ["m_b","m_s","sin2_2theta13_PMNS","sum_m_nu"] },
];

interface Props {
  registers?: RiemannZero[];
  highlightedRegisters?: number[];
  onSelectRegister?: (n: number) => void;
}

/** Panel 1: Register File — γ_n nodes on a number line */
export function RegisterFile({ registers = STATIC_REGISTERS, highlightedRegisters = [], onSelectRegister }: Props) {
  const [selected, setSelected] = useState<number | null>(null);

  const minVal = 12;
  const maxVal = 68;
  const range = maxVal - minVal;

  const handleClick = (n: number) => {
    setSelected(n === selected ? null : n);
    onSelectRegister?.(n);
  };

  const selectedReg = registers.find((r) => r.n === selected);

  return (
    <div style={{ background: "#111118", borderRadius: 8, padding: 16, height: "100%" }}>
      <h3 style={{ margin: "0 0 8px", color: "#8af", fontSize: 13, letterSpacing: 1 }}>
        REGISTER FILE — γ₁…γ₁₅
      </h3>

      {/* Number line */}
      <svg viewBox="0 0 400 80" style={{ width: "100%", height: 60 }}>
        {/* Axis */}
        <line x1="20" y1="40" x2="380" y2="40" stroke="#333" strokeWidth="1" />

        {/* Zero nodes */}
        {registers.map((r) => {
          const x = 20 + ((r.value - minVal) / range) * 360;
          const isHighlighted = highlightedRegisters.includes(r.n);
          const isSelected = r.n === selected;
          const radius = r.gauge_distinguished ? 7 : 5;
          const color = isSelected ? "#fff" : isHighlighted ? "#ff0" : r.gauge_distinguished ? "#f44" : "#4fc3f7";

          return (
            <g key={r.n} onClick={() => handleClick(r.n)} style={{ cursor: "pointer" }}>
              <circle cx={x} cy={40} r={radius} fill={color} opacity={isHighlighted || isSelected ? 1 : 0.7} />
              <text x={x} y={25} textAnchor="middle" fill="#888" fontSize="8">
                γ_{r.n}
              </text>
              <text x={x} y={58} textAnchor="middle" fill="#555" fontSize="7">
                {r.value.toFixed(1)}
              </text>
            </g>
          );
        })}
      </svg>

      {/* Selected register info */}
      {selectedReg && (
        <div style={{ fontSize: 11, color: "#aaa", marginTop: 4, lineHeight: 1.6 }}>
          <div><strong style={{ color: "#fff" }}>γ_{selectedReg.n}</strong> = {selectedReg.value.toFixed(4)}</div>
          <div>Role: {selectedReg.role} | Freq: {selectedReg.frequency}</div>
          <div>SM: {selectedReg.sm_interpretation}</div>
          <div style={{ color: "#666" }}>
            Used in: {selectedReg.formulas_using.slice(0, 5).join(", ")}
            {selectedReg.formulas_using.length > 5 ? "..." : ""}
          </div>
        </div>
      )}
    </div>
  );
}
