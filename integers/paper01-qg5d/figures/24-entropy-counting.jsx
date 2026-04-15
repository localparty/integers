import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  planck: "#44aaff",
  planckGlow: "rgba(68,170,255,0.1)",
  ePhase: "#ffcc44",
  ePhaseGlow: "rgba(255,204,68,0.1)",
  horizon: "#ff5555",
  result: "#55ff99",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  grid: "rgba(30,50,90,0.15)",
};

export default function EntropyCounting() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });
  const [gridSize, setGridSize] = useState(6);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.012;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    // Title
    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Bekenstein-Hawking Entropy: S = A/4 from e-Circle State Counting", W / 2, 28);
    ctx.font = "11px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("Each Planck pixel on S\u00b2 carries one e-circle \u2014 each e-circle carries one bit", W / 2, 46);

    // LEFT: The horizon grid (Planck pixels on S^2)
    const gx = 100, gy = 90;
    const cellSize = Math.min(40, 280 / gridSize);
    const gridW = gridSize * cellSize;
    const gridH = gridSize * cellSize;

    ctx.fillStyle = C.textDim;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("Horizon surface (S\u00b2)", gx + gridW / 2, gy - 10);
    ctx.fillText(`${gridSize}\u00d7${gridSize} = ${gridSize * gridSize} Planck pixels`, gx + gridW / 2, gy + gridH + 18);

    // Draw grid of Planck pixels, each with a phase indicator
    for (let row = 0; row < gridSize; row++) {
      for (let col = 0; col < gridSize; col++) {
        const px = gx + col * cellSize;
        const py = gy + row * cellSize;
        const idx = row * gridSize + col;

        // Planck pixel
        ctx.strokeStyle = C.planck;
        ctx.lineWidth = 0.8;
        ctx.strokeRect(px, py, cellSize, cellSize);

        // e-circle inside each pixel
        const ecx = px + cellSize / 2;
        const ecy = py + cellSize / 2;
        const eR = cellSize * 0.3;

        ctx.strokeStyle = C.ePhase;
        ctx.lineWidth = 0.8;
        ctx.globalAlpha = 0.5;
        ctx.beginPath();
        ctx.arc(ecx, ecy, eR, 0, TAU);
        ctx.stroke();
        ctx.globalAlpha = 1;

        // Phase marker (the information bit)
        const phi = Math.sin(idx * 1.7 + st.time * 0.5) * Math.PI;
        const mx = ecx + eR * 0.7 * Math.cos(phi);
        const my = ecy + eR * 0.7 * Math.sin(phi);

        ctx.fillStyle = C.ePhase;
        ctx.beginPath();
        ctx.arc(mx, my, 2, 0, TAU);
        ctx.fill();
      }
    }

    // Area label
    ctx.fillStyle = C.planck;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    const areaText = `A = ${gridSize * gridSize} l\u209a\u00b2`;
    ctx.fillText(areaText, gx + gridW / 2, gy + gridH + 36);

    // RIGHT: The counting argument
    const rx = 480, ry = 90;

    ctx.fillStyle = C.text;
    ctx.font = "bold 13px monospace";
    ctx.textAlign = "left";
    ctx.fillText("The counting argument:", rx, ry);

    ctx.font = "12px monospace";
    ctx.fillStyle = C.planck;
    ctx.fillText("1. Horizon area = N Planck pixels", rx, ry + 30);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText(`   N = A / l\u209a\u00b2 = ${gridSize * gridSize}`, rx, ry + 48);

    ctx.fillStyle = C.ePhase;
    ctx.font = "12px monospace";
    ctx.fillText("2. Each pixel carries one e-circle S\u00b9", rx, ry + 78);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("   horizon topology: S\u00b2 \u00d7 S\u00b9", rx, ry + 96);

    ctx.fillStyle = C.ePhase;
    ctx.font = "12px monospace";
    ctx.fillText("3. Each e-circle encodes one bit", rx, ry + 126);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("   \u03c6 \u2208 {0, \u03c0} after decoherence", rx, ry + 144);
    ctx.fillText("   (binary: up or down on e-circle)", rx, ry + 160);

    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.fillText("4. Total information capacity:", rx, ry + 195);

    // The big result
    ctx.fillStyle = C.result;
    ctx.font = "bold 20px monospace";
    ctx.fillText("S = N bits = A / l\u209a\u00b2", rx, ry + 225);

    ctx.font = "14px monospace";
    ctx.fillText("= A / 4  (in Planck units)", rx, ry + 252);

    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("The factor 1/4 arises from the definition", rx, ry + 280);
    ctx.fillText("l\u209a\u00b2 = 4G\u210f/c\u00b3 in the Planck area", rx, ry + 296);

    // Arrow connecting grid to formula
    ctx.strokeStyle = C.textDim;
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(gx + gridW + 10, gy + gridH / 2);
    ctx.lineTo(rx - 15, gy + gridH / 2);
    ctx.stroke();
    ctx.setLineDash([]);

    // Bottom comparison
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";

    const by = H - 80;
    ctx.fillText("Standard derivation: S = A/4 from Euclidean path integral (Gibbons-Hawking 1977)", W / 2, by);
    ctx.fillStyle = C.result;
    ctx.fillText("e-dimension: S = A/4 because information IS the e-coordinate at each Planck pixel", W / 2, by + 20);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("The Bekenstein-Hawking formula counts something physical: the number of e-circle states on the horizon surface", W / 2, by + 44);

  }, [gridSize]);

  useEffect(() => {
    const id = requestAnimationFrame(function loop() {
      draw();
      animRef.current = requestAnimationFrame(loop);
    });
    return () => cancelAnimationFrame(animRef.current || id);
  }, [draw]);

  const btn = (active) => ({
    background: active ? "rgba(68,170,255,0.2)" : "transparent",
    color: active ? C.planck : C.textDim,
    border: `1px solid ${active ? C.planck : "rgba(100,140,200,0.2)"}`,
    padding: "4px 12px", fontSize: 12, fontFamily: "monospace",
    borderRadius: 3, cursor: "pointer",
  });

  return (
    <div style={{ background: C.bg, minHeight: "100vh", display: "flex", flexDirection: "column", alignItems: "center", padding: 20 }}>
      <canvas ref={canvasRef} width={900} height={520} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 8, marginTop: 12, alignItems: "center" }}>
        <span style={{ color: C.textDim, fontFamily: "monospace", fontSize: 12 }}>Horizon size:</span>
        {[4, 6, 8, 10].map(n => (
          <button key={n} style={btn(gridSize === n)} onClick={() => setGridSize(n)}>
            {n}\u00d7{n}
          </button>
        ))}
      </div>
    </div>
  );
}
