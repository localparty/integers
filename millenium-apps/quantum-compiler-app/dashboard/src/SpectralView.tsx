import React from "react";

// Precomputed eigenvalue data for visualization
const ZEROS = [
  14.1347, 21.0220, 25.0109, 30.4249, 32.9351,
  37.5862, 40.9187, 43.3271, 48.0052, 49.7738,
  52.9703, 56.4462, 59.3470, 60.8318, 65.1125,
];

// Spacings between consecutive zeros
const SPACINGS = ZEROS.slice(1).map((z, i) => z - ZEROS[i]);

interface Props {
  highlightedZeros?: number[];
}

/** Panel 4: Eigenvalue distribution — spectral view of placed zeros */
export function SpectralView({ highlightedZeros = [] }: Props) {
  const maxZero = 68;
  const barHeight = 200;

  return (
    <div style={{ background: "#111118", borderRadius: 8, padding: 16, height: "100%" }}>
      <h3 style={{ margin: "0 0 8px", color: "#8af", fontSize: 13, letterSpacing: 1 }}>
        SPECTRAL VIEW
      </h3>

      <svg viewBox="0 0 300 220" style={{ width: "100%", height: 180 }}>
        {/* Eigenvalue bars */}
        {ZEROS.map((z, i) => {
          const x = 15 + (z / maxZero) * 270;
          const isHighlighted = highlightedZeros.includes(i + 1);
          const gaugeDistinguished = [1, 4, 6, 8].includes(i + 1);

          return (
            <g key={i}>
              {/* Eigenvalue line */}
              <line
                x1={x} y1={20} x2={x} y2={barHeight - 10}
                stroke={isHighlighted ? "#ff0" : gaugeDistinguished ? "#f44" : "#4fc3f7"}
                strokeWidth={isHighlighted ? 2 : 1}
                opacity={isHighlighted ? 1 : 0.5}
              />
              {/* Star for placed zeros */}
              <text x={x} y={15} textAnchor="middle" fontSize="8"
                    fill={gaugeDistinguished ? "#f44" : "#4fc3f7"}>
                ★
              </text>
              {/* Label */}
              <text x={x} y={barHeight + 5} textAnchor="middle" fontSize="7" fill="#555">
                {i + 1}
              </text>
            </g>
          );
        })}

        {/* Spacing histogram at bottom */}
        <text x="150" y={barHeight + 18} textAnchor="middle" fontSize="8" fill="#555">
          Zero spacings (GUE statistics)
        </text>
        {SPACINGS.map((s, i) => {
          const x = 25 + i * 19;
          const h = (s / 8) * 30;
          return (
            <rect key={i} x={x} y={barHeight + 22} width={14} height={h}
                  rx={1} fill="#4fc3f7" opacity={0.3} />
          );
        })}
      </svg>

      {/* Stats */}
      <div style={{ display: "flex", gap: 16, fontSize: 10, color: "#666", marginTop: 4 }}>
        <span>Placed: 15/∞</span>
        <span>Gauge: {"{1,4,6,8}"}</span>
        <span>Mean spacing: {(SPACINGS.reduce((a, b) => a + b) / SPACINGS.length).toFixed(2)}</span>
      </div>
    </div>
  );
}
