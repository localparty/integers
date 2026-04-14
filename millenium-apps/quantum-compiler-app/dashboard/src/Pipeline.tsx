import React from "react";
import type { TraceStep } from "./types";

const STAGES = [
  { id: "LEXER", label: "LEXER", sub: "Six Patterns", color: "#4fc3f7" },
  { id: "PARSER", label: "PARSER", sub: "Zero Selection", color: "#66bb6a" },
  { id: "TYPE_CHECKER", label: "TYPE", sub: "Grammar Rules", color: "#ab47bc" },
  { id: "CODE_GEN", label: "CODEGEN", sub: "Transposition", color: "#ffa726" },
  { id: "OPTIMIZER", label: "OPTIMIZE", sub: "LOCK Verify", color: "#ef5350" },
  { id: "LINKER", label: "LINKER", sub: "39+ Domains", color: "#26c6da" },
];

interface Props {
  trace?: TraceStep[];
  activeStage?: string;
}

/** Panel 2: Animated compilation pipeline — NL → BC algebra */
export function Pipeline({ trace = [], activeStage }: Props) {
  return (
    <div style={{ background: "#111118", borderRadius: 8, padding: 16, height: "100%" }}>
      <h3 style={{ margin: "0 0 12px", color: "#8af", fontSize: 13, letterSpacing: 1 }}>
        COMPILATION PIPELINE
      </h3>

      <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
        {STAGES.map((stage, i) => {
          const traceEntry = trace.find((t) => t.stage === stage.id);
          const isActive = activeStage === stage.id;
          const isDone = traceEntry !== undefined;

          return (
            <div key={stage.id} style={{ display: "flex", alignItems: "center", gap: 8 }}>
              {/* Stage indicator */}
              <div style={{
                width: 8, height: 8, borderRadius: "50%",
                background: isDone ? stage.color : isActive ? "#fff" : "#333",
                boxShadow: isActive ? `0 0 8px ${stage.color}` : "none",
                transition: "all 0.3s",
              }} />

              {/* Stage box */}
              <div style={{
                flex: 1, padding: "6px 10px", borderRadius: 4,
                background: isDone ? `${stage.color}15` : "#1a1a22",
                border: `1px solid ${isDone ? stage.color + "40" : "#222"}`,
                transition: "all 0.3s",
              }}>
                <div style={{ fontSize: 11, fontWeight: 600, color: isDone ? stage.color : "#666" }}>
                  {stage.label}
                  <span style={{ fontWeight: 400, marginLeft: 8, color: "#555", fontSize: 10 }}>
                    {stage.sub}
                  </span>
                </div>
                {traceEntry && (
                  <div style={{ fontSize: 9, color: "#888", marginTop: 2, maxHeight: 30, overflow: "hidden" }}>
                    {JSON.stringify(traceEntry).slice(0, 100)}...
                  </div>
                )}
              </div>

              {/* Arrow */}
              {i < STAGES.length - 1 && (
                <div style={{ color: isDone ? stage.color : "#333", fontSize: 10 }}>▼</div>
              )}
            </div>
          );
        })}
      </div>

      {/* Input/output labels */}
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 12, fontSize: 10 }}>
        <span style={{ color: "#4fc3f7" }}>SOURCE: Natural Language</span>
        <span style={{ color: "#26c6da" }}>TARGET: BC Algebra</span>
      </div>
    </div>
  );
}
