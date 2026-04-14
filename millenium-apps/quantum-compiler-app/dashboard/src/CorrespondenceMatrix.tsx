import React, { useState } from "react";

// Core domains × key observables
const DOMAINS = ["spectral", "geometric", "algebraic", "number_theoretic", "topological", "thermodynamic"];
const OBSERVABLES = ["m_t", "m_W", "1/alpha", "N_eff", "log_CC", "n_s"];

// Status data (from correspondence.py)
const MATRIX: Record<string, Record<string, "FILLED" | "PARTIAL" | "BLANK">> = {
  m_t:       { spectral: "FILLED", geometric: "FILLED", algebraic: "FILLED", number_theoretic: "FILLED", topological: "FILLED", thermodynamic: "FILLED" },
  m_W:       { spectral: "FILLED", geometric: "FILLED", algebraic: "PARTIAL", number_theoretic: "FILLED", topological: "PARTIAL", thermodynamic: "BLANK" },
  "1/alpha": { spectral: "FILLED", geometric: "FILLED", algebraic: "FILLED", number_theoretic: "FILLED", topological: "BLANK", thermodynamic: "BLANK" },
  N_eff:     { spectral: "FILLED", geometric: "FILLED", algebraic: "BLANK", number_theoretic: "FILLED", topological: "FILLED", thermodynamic: "BLANK" },
  log_CC:    { spectral: "FILLED", geometric: "FILLED", algebraic: "BLANK", number_theoretic: "FILLED", topological: "BLANK", thermodynamic: "FILLED" },
  n_s:       { spectral: "FILLED", geometric: "FILLED", algebraic: "BLANK", number_theoretic: "FILLED", topological: "BLANK", thermodynamic: "FILLED" },
};

const STATUS_COLORS = {
  FILLED: "#66bb6a",
  PARTIAL: "#ffa726",
  BLANK: "#333",
};

interface Props {
  onClickBlank?: (concept: string, domain: string) => void;
}

/** Panel 3: Domain × concept correspondence matrix */
export function CorrespondenceMatrix({ onClickBlank }: Props) {
  const [hoveredCell, setHoveredCell] = useState<string | null>(null);

  return (
    <div style={{ background: "#111118", borderRadius: 8, padding: 16, height: "100%" }}>
      <h3 style={{ margin: "0 0 8px", color: "#8af", fontSize: 13, letterSpacing: 1 }}>
        CORRESPONDENCE MATRIX
      </h3>

      <div style={{ overflowX: "auto" }}>
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 10 }}>
          <thead>
            <tr>
              <th style={{ padding: 4, textAlign: "left", color: "#666" }}></th>
              {DOMAINS.map((d) => (
                <th key={d} style={{ padding: 4, textAlign: "center", color: "#888", fontSize: 8, maxWidth: 50 }}>
                  {d.replace("_", "\n")}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {OBSERVABLES.map((obs) => (
              <tr key={obs}>
                <td style={{ padding: "4px 6px", color: "#aaa", fontWeight: 600, fontSize: 10 }}>
                  {obs}
                </td>
                {DOMAINS.map((domain) => {
                  const status = MATRIX[obs]?.[domain] || "BLANK";
                  const key = `${obs}-${domain}`;
                  const isHovered = hoveredCell === key;

                  return (
                    <td
                      key={domain}
                      style={{ padding: 2, textAlign: "center" }}
                      onMouseEnter={() => setHoveredCell(key)}
                      onMouseLeave={() => setHoveredCell(null)}
                      onClick={() => status === "BLANK" && onClickBlank?.(obs, domain)}
                    >
                      <div style={{
                        width: 18, height: 18, borderRadius: 3, margin: "0 auto",
                        background: STATUS_COLORS[status],
                        opacity: isHovered ? 1 : 0.7,
                        cursor: status === "BLANK" ? "pointer" : "default",
                        transition: "all 0.2s",
                        border: isHovered ? "1px solid #fff" : "1px solid transparent",
                      }} />
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Legend */}
      <div style={{ display: "flex", gap: 12, marginTop: 8, fontSize: 9, color: "#666" }}>
        {Object.entries(STATUS_COLORS).map(([status, color]) => (
          <div key={status} style={{ display: "flex", alignItems: "center", gap: 4 }}>
            <div style={{ width: 8, height: 8, borderRadius: 2, background: color }} />
            {status}
          </div>
        ))}
        <span style={{ marginLeft: "auto", color: "#555" }}>Click blank cells to explore</span>
      </div>
    </div>
  );
}
