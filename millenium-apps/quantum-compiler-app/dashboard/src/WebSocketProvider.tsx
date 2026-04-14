import React, { createContext, useContext, useEffect, useRef, useState, useCallback } from "react";
import type { CompilationResult, CapacitorState, RiemannZero } from "./types";

interface WSState {
  connected: boolean;
  registers: RiemannZero[];
  lastCompilation: CompilationResult | null;
  capacitor: CapacitorState | null;
  allResults: CompilationResult[];
  send: (msg: Record<string, unknown>) => void;
}

const WSContext = createContext<WSState>({
  connected: false,
  registers: [],
  lastCompilation: null,
  capacitor: null,
  allResults: [],
  send: () => {},
});

export const useWS = () => useContext(WSContext);

interface Props {
  url?: string;
  children: React.ReactNode;
}

/**
 * WebSocket provider for real-time dashboard updates.
 * Connects to the MCP server's WebSocket endpoint.
 * Falls back gracefully when server is not running.
 */
export function WebSocketProvider({ url = "ws://localhost:8765", children }: Props) {
  const ws = useRef<WebSocket | null>(null);
  const [connected, setConnected] = useState(false);
  const [registers, setRegisters] = useState<RiemannZero[]>([]);
  const [lastCompilation, setLastCompilation] = useState<CompilationResult | null>(null);
  const [capacitor, setCapacitor] = useState<CapacitorState | null>(null);
  const [allResults, setAllResults] = useState<CompilationResult[]>([]);

  const send = useCallback((msg: Record<string, unknown>) => {
    if (ws.current?.readyState === WebSocket.OPEN) {
      ws.current.send(JSON.stringify(msg));
    }
  }, []);

  useEffect(() => {
    try {
      ws.current = new WebSocket(url);
      ws.current.onopen = () => setConnected(true);
      ws.current.onclose = () => setConnected(false);
      ws.current.onerror = () => setConnected(false);
      ws.current.onmessage = (event) => {
        const data = JSON.parse(event.data);
        switch (data.type) {
          case "registers":
            setRegisters(data.payload);
            break;
          case "compilation":
            setLastCompilation(data.payload);
            setAllResults((prev) => [...prev, data.payload]);
            break;
          case "capacitor":
            setCapacitor(data.payload);
            break;
          case "all_results":
            setAllResults(data.payload);
            break;
        }
      };
    } catch {
      setConnected(false);
    }

    return () => {
      ws.current?.close();
    };
  }, [url]);

  return (
    <WSContext.Provider value={{ connected, registers, lastCompilation, capacitor, allResults, send }}>
      {children}
    </WSContext.Provider>
  );
}
