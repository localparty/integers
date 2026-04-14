import React, { useRef } from "react";

/**
 * Panel 6: Three-primes 3-qubit Bloch view.
 *
 * Visualizes the {2, 3, 5} prime structure that generates
 * 3 generations via the Bost-Connes Hecke algebra.
 *
 * Uses SVG for a simplified Bloch-sphere-like representation
 * (Three.js version can be added later for full 3D interaction).
 */

interface Props {
  activeGenerations?: number[];
}

const PRIMES = [
  { p: 2, label: "p=2", generation: "1st", operation: "DIFFERENCE", color: "#4fc3f7", angle: 0 },
  { p: 3, label: "p=3", generation: "2nd", operation: "RATIO", color: "#66bb6a", angle: 120 },
  { p: 5, label: "p=5", generation: "3rd", operation: "PRODUCT", color: "#ffa726", angle: 240 },
];

export function BlochView({ activeGenerations = [1, 2, 3] }: Props) {
  const cx = 150, cy = 100, r = 70;

  return (
    <div style={{ background: "#111118", borderRadius: 8, padding: 16, height: "100%" }}>
      <h3 style={{ margin: "0 0 8px", color: "#8af", fontSize: 13, letterSpacing: 1 }}>
        THREE-PRIMES VIEW — {"{2, 3, 5}"}
      </h3>

      <svg viewBox="0 0 300 200" style={{ width: "100%", height: 170 }}>
        {/* Outer circle (Bloch sphere projection) */}
        <circle cx={cx} cy={cy} r={r + 10} fill="none" stroke="#222" strokeWidth="1" />
        <circle cx={cx} cy={cy} r={r - 20} fill="none" stroke="#1a1a22" strokeWidth="1" strokeDasharray="4 4" />

        {/* Connecting lines */}
        {PRIMES.map((p, i) => {
          const next = PRIMES[(i + 1) % 3];
          const x1 = cx + r * Math.cos((p.angle - 90) * Math.PI / 180);
          const y1 = cy + r * Math.sin((p.angle - 90) * Math.PI / 180);
          const x2 = cx + r * Math.cos((next.angle - 90) * Math.PI / 180);
          const y2 = cy + r * Math.sin((next.angle - 90) * Math.PI / 180);
          return (
            <line key={`line-${i}`} x1={x1} y1={y1} x2={x2} y2={y2}
                  stroke="#333" strokeWidth="1" />
          );
        })}

        {/* Prime nodes */}
        {PRIMES.map((p, i) => {
          const x = cx + r * Math.cos((p.angle - 90) * Math.PI / 180);
          const y = cy + r * Math.sin((p.angle - 90) * Math.PI / 180);
          const isActive = activeGenerations.includes(i + 1);

          return (
            <g key={p.p}>
              {/* Glow */}
              {isActive && (
                <circle cx={x} cy={y} r={20} fill={p.color} opacity={0.1} />
              )}
              {/* Node */}
              <circle cx={x} cy={y} r={12} fill={p.color}
                      opacity={isActive ? 0.9 : 0.3} />
              {/* Prime label */}
              <text x={x} y={y + 4} textAnchor="middle" fontSize="11"
                    fill="#000" fontWeight="700">
                {p.p}
              </text>
              {/* Generation label */}
              <text x={x} y={y + 26} textAnchor="middle" fontSize="8"
                    fill={p.color}>
                {p.generation} gen
              </text>
              {/* Operation label */}
              <text x={x} y={y + 36} textAnchor="middle" fontSize="7"
                    fill="#555">
                {p.operation}
              </text>
            </g>
          );
        })}

        {/* Center label */}
        <text x={cx} y={cy - 2} textAnchor="middle" fontSize="9" fill="#666">
          Hecke
        </text>
        <text x={cx} y={cy + 8} textAnchor="middle" fontSize="9" fill="#666">
          algebra
        </text>

        {/* Conductor */}
        <text x={cx} y={190} textAnchor="middle" fontSize="8" fill="#444">
          Minimal conductor: 1729 = 7 x 13 x 19
        </text>
      </svg>
    </div>
  );
}
