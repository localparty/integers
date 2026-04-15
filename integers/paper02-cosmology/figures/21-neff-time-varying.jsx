import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  mirror: "#44aaff",
  mirrorGlow: "rgba(68,170,255,0.15)",
  sm: "rgba(100,140,200,0.6)",
  act: "#ff5555",
  shoes: "#44ff88",
  planck: "rgba(100,140,200,0.4)",
  suppression: "#ffcc44",
  axis: "rgba(100,140,200,0.3)",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  grid: "rgba(30,50,90,0.2)",
};

// Precomputed N_eff data from CAMB analysis (xi = 0.47)
// z, delta_neff, suppression_factor
const DATA_047 = [
  [1e-1, 0.361, 0.490], [1, 0.361, 0.490], [10, 0.361, 0.490],
  [100, 0.361, 0.490], [1090, 0.361, 0.490], [1e4, 0.361, 0.490],
  [1e5, 0.361, 0.490], [1e6, 0.361, 0.490], [1e7, 0.361, 0.490],
  [1e8, 0.361, 0.490], [5e8, 0.42, 0.57], [1e9, 0.506, 0.686],
  [3e9, 0.72, 1.0], [5e9, 0.88, 1.2], [1e10, 1.101, 1.494],
];

const DATA_043 = [
  [1e-1, 0.258, 0.490], [1, 0.258, 0.490], [10, 0.258, 0.490],
  [100, 0.258, 0.490], [1090, 0.258, 0.490], [1e4, 0.258, 0.490],
  [1e5, 0.258, 0.490], [1e6, 0.258, 0.490], [1e7, 0.258, 0.490],
  [1e8, 0.258, 0.490], [5e8, 0.30, 0.57], [1e9, 0.338, 0.642],
  [3e9, 0.50, 1.0], [5e9, 0.63, 1.2], [1e10, 0.784, 1.490],
];

function lerp(a, b, t) { return a + (b - a) * t; }

function lerpData(data, logZ) {
  for (let i = 0; i < data.length - 1; i++) {
    const lz0 = Math.log10(data[i][0]);
    const lz1 = Math.log10(data[i + 1][0]);
    if (logZ >= lz0 && logZ <= lz1) {
      const t = (logZ - lz0) / (lz1 - lz0);
      return [lerp(data[i][1], data[i + 1][1], t), lerp(data[i][2], data[i + 1][2], t)];
    }
  }
  return [data[data.length - 1][1], data[data.length - 1][2]];
}

export default function NeffTimeVarying() {
  const canvasRef = useRef(null);
  const [xi, setXi] = useState(0.47);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    // Layout
    const mL = 80, mR = 40, mT = 60, mB = 60;
    const pW = W - mL - mR, pH = H - mT - mB;

    // Axes: x = log10(z) from -1 to 10, y = N_eff from 2.5 to 4.5
    const xMin = -1, xMax = 10, yMin = 2.5, yMax = 4.5;
    const toX = (logZ) => mL + (logZ - xMin) / (xMax - xMin) * pW;
    const toY = (neff) => mT + (1 - (neff - yMin) / (yMax - yMin)) * pH;

    // Grid
    ctx.strokeStyle = C.grid;
    ctx.lineWidth = 0.5;
    for (let lz = 0; lz <= 10; lz += 2) {
      ctx.beginPath(); ctx.moveTo(toX(lz), mT); ctx.lineTo(toX(lz), mT + pH); ctx.stroke();
    }
    for (let n = 2.5; n <= 4.5; n += 0.5) {
      ctx.beginPath(); ctx.moveTo(mL, toY(n)); ctx.lineTo(mL + pW, toY(n)); ctx.stroke();
    }

    // Axis labels
    ctx.fillStyle = C.text;
    ctx.font = "13px monospace";
    ctx.textAlign = "center";
    for (let lz = 0; lz <= 10; lz += 2) {
      ctx.fillText(`10^${lz}`, toX(lz), mT + pH + 20);
    }
    ctx.fillText("Redshift z", mL + pW / 2, H - 10);

    ctx.textAlign = "right";
    for (let n = 2.5; n <= 4.5; n += 0.5) {
      ctx.fillText(n.toFixed(1), mL - 8, toY(n) + 4);
    }
    ctx.save();
    ctx.translate(15, mT + pH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.textAlign = "center";
    ctx.fillText("Effective N_eff", 0, 0);
    ctx.restore();

    // Reference lines
    // SM N_eff = 3.044
    ctx.strokeStyle = C.sm;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([6, 4]);
    ctx.beginPath(); ctx.moveTo(mL, toY(3.044)); ctx.lineTo(mL + pW, toY(3.044)); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.sm;
    ctx.textAlign = "left";
    ctx.fillText("SM  3.044", mL + 5, toY(3.044) - 6);

    // ACT DR6 band: 2.86 +/- 0.13
    ctx.fillStyle = "rgba(255,85,85,0.08)";
    ctx.fillRect(mL, toY(2.86 + 0.13), pW, toY(2.86 - 0.13) - toY(2.86 + 0.13));
    ctx.strokeStyle = C.act;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 3]);
    ctx.beginPath(); ctx.moveTo(mL, toY(2.86)); ctx.lineTo(mL + pW, toY(2.86)); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.act;
    ctx.fillText("ACT DR6  2.86 \u00b1 0.13", mL + 5, toY(2.86) + 14);

    // SH0ES+CMB joint: 3.43 +/- 0.13
    ctx.fillStyle = "rgba(68,255,136,0.06)";
    ctx.fillRect(mL, toY(3.43 + 0.13), pW, toY(3.43 - 0.13) - toY(3.43 + 0.13));
    ctx.strokeStyle = C.shoes;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 3]);
    ctx.beginPath(); ctx.moveTo(mL, toY(3.43)); ctx.lineTo(mL + pW, toY(3.43)); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.shoes;
    ctx.fillText("CMB+SH0ES  3.43 \u00b1 0.13", mL + 5, toY(3.43) - 6);

    // Draw N_eff(z) curve
    const data = xi > 0.45 ? DATA_047 : DATA_043;
    ctx.strokeStyle = C.mirror;
    ctx.lineWidth = 2.5;
    ctx.shadowColor = C.mirrorGlow;
    ctx.shadowBlur = 8;
    ctx.beginPath();
    const steps = 200;
    for (let i = 0; i <= steps; i++) {
      const logZ = xMin + (xMax - xMin) * i / steps;
      const [dneff] = lerpData(data, logZ);
      const neff = 3.044 + dneff;
      const x = toX(logZ), y = toY(neff);
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Epoch markers
    ctx.fillStyle = C.suppression;
    ctx.font = "11px monospace";
    ctx.textAlign = "center";

    // Recombination
    const xRec = toX(Math.log10(1090));
    ctx.strokeStyle = C.suppression;
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(xRec, mT); ctx.lineTo(xRec, mT + pH); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillText("Recombination", xRec, mT - 8);
    ctx.fillText("z \u2248 1090", xRec, mT - 22);

    // BBN
    const xBBN = toX(9.6); // z ~ 4e9
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(xBBN, mT); ctx.lineTo(xBBN, mT + pH); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillText("BBN", xBBN, mT - 8);
    ctx.fillText("z \u2248 4\u00d710\u2079", xBBN, mT - 22);

    // Mirror e+/- annihilation zone
    const xAnnL = toX(8.5), xAnnR = toX(10);
    ctx.fillStyle = "rgba(255,204,68,0.06)";
    ctx.fillRect(xAnnL, mT, xAnnR - xAnnL, pH);
    ctx.fillStyle = C.suppression;
    ctx.font = "10px monospace";
    ctx.fillText("mirror e\u00b1", (xAnnL + xAnnR) / 2, mT + pH - 20);
    ctx.fillText("transition", (xAnnL + xAnnR) / 2, mT + pH - 8);

    // Suppression annotation
    const [dnRec] = lerpData(data, Math.log10(1090));
    const neffRec = 3.044 + dnRec;
    ctx.fillStyle = C.mirror;
    ctx.font = "12px monospace";
    ctx.textAlign = "left";
    ctx.fillText(`\u0394N_eff(rec) = ${dnRec.toFixed(3)}`, xRec + 10, toY(neffRec) - 12);
    ctx.fillText(`total N_eff = ${neffRec.toFixed(2)}`, xRec + 10, toY(neffRec) + 4);
    ctx.fillStyle = C.suppression;
    ctx.fillText(`suppression: 0.49\u00d7`, xRec + 10, toY(neffRec) + 20);

    // Title
    ctx.fillStyle = C.text;
    ctx.font = "bold 15px monospace";
    ctx.textAlign = "center";
    ctx.fillText(`Time-Varying \u0394N_eff from Mirror e\u00b1 Annihilation (\u03be = ${xi})`, W / 2, 22);

    ctx.font = "11px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("Mirror e\u00b1 are relativistic at BBN but fully annihilated by recombination \u2014 N_eff is epoch-dependent", W / 2, 40);

  }, [xi]);

  useEffect(() => { draw(); }, [draw]);

  const btn = (active) => ({
    background: active ? "rgba(68,170,255,0.2)" : "transparent",
    color: active ? C.mirror : C.textDim,
    border: `1px solid ${active ? C.mirror : "rgba(100,140,200,0.2)"}`,
    padding: "4px 12px", fontSize: 12, fontFamily: "monospace",
    borderRadius: 3, cursor: "pointer",
  });

  return (
    <div style={{ background: C.bg, minHeight: "100vh", display: "flex", flexDirection: "column", alignItems: "center", padding: 20 }}>
      <canvas ref={canvasRef} width={900} height={520} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <button style={btn(xi === 0.47)} onClick={() => setXi(0.47)}>{"\u03be"} = 0.47 (Scenario A)</button>
        <button style={btn(xi === 0.432)} onClick={() => setXi(0.432)}>{"\u03be"} = 0.432 (Scenario B)</button>
      </div>
    </div>
  );
}
