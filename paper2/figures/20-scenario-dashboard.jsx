import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  scenA: "#44aaff",
  scenB: "#ff9944",
  scenC: "#55ff99",
  planck: "rgba(100,140,200,0.7)",
  lcdm: "rgba(100,140,200,0.4)",
  target: "rgba(255,200,60,0.5)",
  tension: "#ff5555",
  resolved: "#44ff88",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  axis: "rgba(100,140,200,0.3)",
};

const scenarios = {
  A: { name: "Scenario A", sub: "θ*-matched", xi: 0.470, H0: 69.5, age: 13.47, S8: 0.753,
       thetaOff: -0.5, Neff: 3.39, OmDM: 5.22, omch2: 0.117, omb: 0.02237, color: C.scenA },
  B: { name: "Scenario B", sub: "1/ξ² law", xi: 0.432, H0: 68.7, age: 13.47, S8: 0.785,
       thetaOff: 6.6, Neff: 3.31, OmDM: 5.36, omch2: 0.1199, omb: 0.02237, color: C.scenB },
  C: { name: "Scenario C", sub: "self-con. ω_b", xi: 0.4375, H0: 68.8, age: 13.60, S8: 0.754,
       thetaOff: 1.0, Neff: 3.32, OmDM: 5.36, omch2: 0.11524, omb: 0.02150, color: C.scenC },
};

const observables = [
  { key: "H0", label: "H₀ (km/s/Mpc)", min: 65, max: 75,
    refs: [{ val: 67.4, label: "Planck", c: C.planck }, { val: 73.0, label: "SH0ES", c: C.tension }, { val: 69.8, label: "TRGB", c: C.target }] },
  { key: "age", label: "Age (Gyr)", min: 12.5, max: 14.5,
    refs: [{ val: 13.80, label: "ΛCDM", c: C.planck }] },
  { key: "S8", label: "S8", min: 0.70, max: 0.88,
    refs: [{ val: 0.832, label: "Planck", c: C.planck }, { val: 0.776, label: "DES", c: C.resolved }, { val: 0.759, label: "KiDS", c: C.resolved }] },
  { key: "Neff", label: "N_eff", min: 2.6, max: 3.6,
    refs: [{ val: 3.044, label: "SM", c: C.planck }, { val: 2.86, label: "ACT DR6", c: C.tension }] },
  { key: "thetaOff", label: "θ* offset (\")", min: -10, max: 10,
    refs: [{ val: 0, label: "Planck", c: C.planck }] },
  { key: "OmDM", label: "Ω_DM/Ω_b", min: 4, max: 7,
    refs: [{ val: 5.36, label: "Observed", c: C.target }] },
];

export default function ScenarioDashboard() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });

  const [highlight, setHighlight] = useState("all"); // all | A | B | C

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.01;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    const mL = 130, mR = 20, mT = 50, mB = 30;
    const pW = W - mL - mR;
    const rowH = (H - mT - mB) / observables.length;

    // Title
    ctx.font = "15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Three Scenarios: Complete Cosmological Dashboard", W / 2, 25);
    ctx.textAlign = "left";

    for (let i = 0; i < observables.length; i++) {
      const obs = observables[i];
      const yCenter = mT + (i + 0.5) * rowH;

      // Row label
      ctx.font = "12px monospace";
      ctx.fillStyle = C.text;
      ctx.textAlign = "right";
      ctx.fillText(obs.label, mL - 10, yCenter + 4);
      ctx.textAlign = "left";

      // Axis line
      ctx.strokeStyle = C.axis;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(mL, yCenter); ctx.lineTo(mL + pW, yCenter);
      ctx.stroke();

      const toX = (v) => mL + ((v - obs.min) / (obs.max - obs.min)) * pW;

      // Reference values
      for (const ref of obs.refs) {
        const rx = toX(ref.val);
        ctx.strokeStyle = ref.c;
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(rx, yCenter - rowH * 0.35);
        ctx.lineTo(rx, yCenter + rowH * 0.35);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = ref.c;
        ctx.font = "9px monospace";
        ctx.textAlign = "center";
        ctx.fillText(ref.label, rx, yCenter - rowH * 0.35 - 4);
        ctx.textAlign = "left";
      }

      // Scenario markers
      for (const [key, sc] of Object.entries(scenarios)) {
        if (highlight !== "all" && highlight !== key) continue;
        const val = sc[obs.key];
        if (val === undefined) continue;
        const sx = toX(val);
        const alpha = highlight === "all" ? 0.9 : (highlight === key ? 1.0 : 0.2);

        // Diamond marker
        ctx.save();
        ctx.translate(sx, yCenter);
        ctx.rotate(Math.PI / 4);
        const size = 6;
        ctx.fillStyle = sc.color;
        ctx.globalAlpha = alpha;
        ctx.fillRect(-size, -size, size * 2, size * 2);
        ctx.globalAlpha = 1;
        ctx.restore();

        // Value label
        if (highlight === key || (highlight === "all" && key === "B")) {
          ctx.fillStyle = sc.color;
          ctx.font = "10px monospace";
          ctx.textAlign = "center";
          const yOff = key === "A" ? -14 : key === "C" ? 16 : -14;
          ctx.fillText(typeof val === "number" ? (Math.abs(val) < 20 ? val.toFixed(2) : val.toFixed(1)) : val, sx, yCenter + yOff);
          ctx.textAlign = "left";
        }
      }

      // Axis ticks
      const nTicks = 5;
      for (let t = 0; t <= nTicks; t++) {
        const val = obs.min + (t / nTicks) * (obs.max - obs.min);
        const tx = toX(val);
        ctx.fillStyle = C.textDim;
        ctx.font = "8px monospace";
        ctx.textAlign = "center";
        ctx.fillText(val.toFixed(val < 10 ? 2 : 1), tx, yCenter + rowH * 0.35 + 10);
        ctx.textAlign = "left";
      }
    }

    // Legend
    const legY = H - 25;
    const legX = mL;
    for (const [key, sc] of Object.entries(scenarios)) {
      const x = legX + (key === "A" ? 0 : key === "B" ? 220 : 440);
      ctx.save();
      ctx.translate(x, legY);
      ctx.rotate(Math.PI / 4);
      ctx.fillStyle = sc.color;
      ctx.fillRect(-4, -4, 8, 8);
      ctx.restore();
      ctx.fillStyle = sc.color;
      ctx.font = "11px monospace";
      ctx.fillText(`${sc.name} (${sc.sub})`, x + 10, legY + 4);
    }

    // Status badges for highlighted scenario
    if (highlight !== "all") {
      const sc = scenarios[highlight];
      ctx.fillStyle = C.panelBg;
      ctx.fillRect(W - 250, mT, 240, 200);
      ctx.strokeStyle = sc.color;
      ctx.lineWidth = 1;
      ctx.strokeRect(W - 250, mT, 240, 200);

      ctx.fillStyle = sc.color;
      ctx.font = "14px monospace";
      ctx.fillText(sc.name, W - 240, mT + 22);
      ctx.font = "11px monospace";
      ctx.fillStyle = C.text;

      const items = [
        `ξ = ${sc.xi}`,
        `H₀ = ${sc.H0} km/s/Mpc`,
        `t₀ = ${sc.age} Gyr`,
        `S8 = ${sc.S8}`,
        `θ* offset = ${sc.thetaOff > 0 ? "+" : ""}${sc.thetaOff}"`,
        `N_eff = ${sc.Neff}`,
        `Ω_DM/Ω_b = ${sc.OmDM}`,
        `ω_b h² = ${sc.omb}`,
      ];
      for (let i = 0; i < items.length; i++) {
        ctx.fillText(items[i], W - 240, mT + 44 + i * 18);
      }

      // ACT tension
      const actTension = ((sc.Neff - 2.86) / 0.13).toFixed(1);
      ctx.fillStyle = C.tension;
      ctx.fillText(`ACT DR6 tension: ${actTension}σ`, W - 240, mT + 44 + items.length * 18);
    }

    animRef.current = requestAnimationFrame(draw);
  }, [highlight]);

  useEffect(() => {
    const canvas = canvasRef.current;
    const dpr = window.devicePixelRatio || 1;
    canvas.width = 800 * dpr; canvas.height = 500 * dpr;
    canvas.style.width = "800px"; canvas.style.height = "500px";
    canvas.getContext("2d").scale(dpr, dpr);
    animRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(animRef.current);
  }, [draw]);

  return (
    <div style={{ background: C.bg, padding: 16, borderRadius: 12, display: "inline-block" }}>
      <div style={{ color: C.text, fontFamily: "monospace", fontSize: 15, marginBottom: 8 }}>
        <strong>20 — Three-Scenario Dashboard</strong>
        <span style={{ color: C.textDim, marginLeft: 12 }}>Paper 2 Summary</span>
      </div>
      <canvas ref={canvasRef} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 10, marginTop: 8, alignItems: "center", flexWrap: "wrap" }}>
        {["all", "A", "B", "C"].map(v => (
          <button key={v} onClick={() => setHighlight(v)}
            style={{
              background: highlight === v ? "rgba(60,120,200,0.3)" : "rgba(30,40,60,0.5)",
              color: v === "all" ? C.text : scenarios[v]?.color || C.text,
              border: `1px solid ${highlight === v ? "rgba(100,160,255,0.5)" : "rgba(60,80,120,0.3)"}`,
              borderRadius: 6, padding: "5px 14px", cursor: "pointer", fontFamily: "monospace", fontSize: 12,
            }}>
            {v === "all" ? "All scenarios" : `${scenarios[v].name} (${scenarios[v].sub})`}
          </button>
        ))}
      </div>
    </div>
  );
}
