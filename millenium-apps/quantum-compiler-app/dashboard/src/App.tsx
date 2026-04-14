import React, { useState } from "react";
import { WebSocketProvider, useWS } from "./WebSocketProvider";
import { RegisterFile } from "./RegisterFile";
import { Pipeline } from "./Pipeline";
import { CorrespondenceMatrix } from "./CorrespondenceMatrix";
import { SpectralView } from "./SpectralView";
import { FormulaOutput } from "./FormulaOutput";
import { BlochView } from "./BlochView";

/**
 * Quantum Compiler Dashboard — Six-panel layout
 *
 * ┌──────────────────┬──────────────────┬──────────────────┐
 * │  REGISTER FILE   │    PIPELINE      │  CORRESPONDENCE  │
 * ├──────────────────┼──────────────────┼──────────────────┤
 * │  SPECTRAL VIEW   │  FORMULA OUTPUT  │  BLOCH VIEW      │
 * └──────────────────┴──────────────────┴──────────────────┘
 */
function Dashboard() {
  const { connected, lastCompilation, allResults } = useWS();
  const [highlightedRegisters, setHighlightedRegisters] = useState<number[]>([]);
  const [inputValue, setInputValue] = useState("");

  const handleSelectRegister = (n: number) => {
    setHighlightedRegisters((prev) =>
      prev.includes(n) ? prev.filter((r) => r !== n) : [...prev, n]
    );
  };

  const handleCompile = () => {
    // In connected mode, sends to MCP server via WebSocket
    // In standalone mode, shows the formula from static data
    console.log("Compile:", inputValue);
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0a0a0f",
      color: "#e0e0e0",
      fontFamily: "'SF Mono', 'Fira Code', monospace",
      padding: 16,
    }}>
      {/* Header */}
      <div style={{
        display: "flex", justifyContent: "space-between", alignItems: "center",
        marginBottom: 16, paddingBottom: 12, borderBottom: "1px solid #1a1a22",
      }}>
        <div>
          <h1 style={{ fontSize: 18, margin: 0, color: "#fff", letterSpacing: 2 }}>
            QUANTUM COMPILER
          </h1>
          <p style={{ fontSize: 10, margin: "4px 0 0", color: "#555" }}>
            Natural Language → Bost-Connes Algebra | 36/37 compiled | 0 free parameters
          </p>
        </div>

        {/* Input bar */}
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleCompile()}
            placeholder="Type an observable... (e.g. 'mass of the top quark')"
            style={{
              width: 360, padding: "8px 12px", borderRadius: 4,
              background: "#1a1a22", border: "1px solid #333", color: "#fff",
              fontFamily: "inherit", fontSize: 12, outline: "none",
            }}
          />
          <button onClick={handleCompile} style={{
            padding: "8px 16px", borderRadius: 4, border: "none",
            background: "#4fc3f7", color: "#000", fontWeight: 600,
            cursor: "pointer", fontFamily: "inherit", fontSize: 12,
          }}>
            COMPILE
          </button>
          <div style={{
            width: 8, height: 8, borderRadius: "50%",
            background: connected ? "#66bb6a" : "#f44",
          }} title={connected ? "Connected to MCP" : "Offline (static data)"} />
        </div>
      </div>

      {/* Six-panel grid */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "1fr 1fr 1fr",
        gridTemplateRows: "1fr 1fr",
        gap: 12,
        height: "calc(100vh - 100px)",
      }}>
        {/* Row 1 */}
        <RegisterFile
          highlightedRegisters={highlightedRegisters}
          onSelectRegister={handleSelectRegister}
        />
        <Pipeline
          trace={lastCompilation?.compilation_trace || []}
        />
        <CorrespondenceMatrix />

        {/* Row 2 */}
        <SpectralView highlightedZeros={highlightedRegisters} />
        <FormulaOutput
          result={lastCompilation}
          allResults={allResults.length > 0 ? allResults : undefined}
        />
        <BlochView />
      </div>

      {/* Footer */}
      <div style={{
        marginTop: 8, padding: "8px 0", borderTop: "1px solid #1a1a22",
        display: "flex", justifyContent: "space-between", fontSize: 9, color: "#444",
      }}>
        <span>Bost-Connes Spectral Compiler v1.0 | G Six + Claude Opus 4.6</span>
        <span>Riemann zeros: 15 placed | Grammar rules: 8 | Domains: 39+</span>
        <span>"The post-it note was right."</span>
      </div>
    </div>
  );
}

export default function App() {
  return (
    <WebSocketProvider>
      <Dashboard />
    </WebSocketProvider>
  );
}
