import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  horizon: "#ff5555",
  horizonGlow: "rgba(255,85,85,0.12)",
  eCircle: "#44aaff",
  eCircleGlow: "rgba(68,170,255,0.15)",
  info: "#ffcc44",
  infoGlow: "rgba(255,204,68,0.15)",
  hawking4d: "#ff9944",
  hawking5d: "#55ff99",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  grid: "rgba(30,50,90,0.15)",
};

export default function BlackHoleInformation() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });
  const [view, setView] = useState("mechanism"); // mechanism | hawking | comparison

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.015;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    if (view === "mechanism") drawMechanism(ctx, W, H, st.time);
    else if (view === "hawking") drawHawking(ctx, W, H, st.time);
    else drawComparison(ctx, W, H, st.time);

    animRef.current = requestAnimationFrame(draw);
  }, [view]);

  useEffect(() => {
    animRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(animRef.current);
  }, [draw]);

  function drawMechanism(ctx, W, H, t) {
    const cx = W / 2, cy = H / 2 + 10;

    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Information Encoding on the Horizon: S\u00b2 \u00d7 S\u00b9", cx, 28);
    ctx.font = "11px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("The horizon is not a 2-sphere \u2014 it is a 2-sphere crossed with the e-circle", cx, 46);

    // Draw the black hole (dark circle)
    const bhR = 100;
    const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, bhR);
    grad.addColorStop(0, "rgba(0,0,0,1)");
    grad.addColorStop(0.7, "rgba(10,5,15,1)");
    grad.addColorStop(1, "rgba(20,10,30,0.8)");
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(cx, cy, bhR, 0, TAU);
    ctx.fill();

    // Horizon ring (pulsing)
    const pulse = 0.8 + 0.2 * Math.sin(t * 2);
    ctx.strokeStyle = C.horizon;
    ctx.lineWidth = 2.5 * pulse;
    ctx.shadowColor = C.horizonGlow;
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.arc(cx, cy, bhR, 0, TAU);
    ctx.stroke();
    ctx.shadowBlur = 0;

    // e-circles attached to horizon points (showing S^2 x S^1)
    const nCircles = 8;
    for (let i = 0; i < nCircles; i++) {
      const angle = (i / nCircles) * TAU + t * 0.3;
      const hx = cx + bhR * Math.cos(angle);
      const hy = cy + bhR * Math.sin(angle);

      // Small e-circle at this horizon point
      const eR = 12;
      ctx.strokeStyle = C.eCircle;
      ctx.lineWidth = 1.2;
      ctx.globalAlpha = 0.5 + 0.3 * Math.sin(t * 3 + i);
      ctx.beginPath();
      ctx.arc(hx, hy, eR, 0, TAU);
      ctx.stroke();

      // Phase marker on the e-circle
      const phi = t * 0.5 + i * 0.8; // different phase at each point
      const px = hx + eR * Math.cos(phi);
      const py = hy + eR * Math.sin(phi);
      ctx.fillStyle = C.info;
      ctx.beginPath();
      ctx.arc(px, py, 2.5, 0, TAU);
      ctx.fill();
      ctx.globalAlpha = 1;
    }

    // Infalling quantum (animated)
    const fallPhase = (t * 0.4) % 1;
    const fallStartX = cx + 280;
    const fallStartY = cy - 80;
    const fallEndX = cx + bhR + 15;
    const fallEndY = cy;
    const fx = fallStartX + (fallEndX - fallStartX) * fallPhase;
    const fy = fallStartY + (fallEndY - fallStartY) * fallPhase;

    if (fallPhase < 0.9) {
      // Draw infalling particle
      ctx.fillStyle = C.info;
      ctx.shadowColor = C.infoGlow;
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(fx, fy, 5, 0, TAU);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Trail
      ctx.strokeStyle = C.info;
      ctx.lineWidth = 1;
      ctx.globalAlpha = 0.3;
      ctx.setLineDash([3, 4]);
      ctx.beginPath();
      ctx.moveTo(fallStartX, fallStartY);
      ctx.lineTo(fx, fy);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.globalAlpha = 1;

      // Label
      ctx.fillStyle = C.info;
      ctx.font = "11px monospace";
      ctx.textAlign = "left";
      ctx.fillText("infalling quantum", fallStartX + 5, fallStartY - 12);
      ctx.fillText("\u03c6 = \u03c6\u2080", fallStartX + 5, fallStartY + 2);
    }

    // Impact flash at horizon
    if (fallPhase > 0.85 && fallPhase < 0.95) {
      const flashAlpha = 1 - Math.abs(fallPhase - 0.9) / 0.05;
      ctx.fillStyle = `rgba(255,204,68,${flashAlpha * 0.4})`;
      ctx.beginPath();
      ctx.arc(fallEndX, fallEndY, 25, 0, TAU);
      ctx.fill();
    }

    // Annotations
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "left";

    // Left side: mechanism description
    const lx = 30, ly = 100;
    ctx.fillStyle = C.horizon;
    ctx.fillText("Horizon = S\u00b2 \u00d7 S\u00b9", lx, ly);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("2-sphere \u00d7 e-circle", lx, ly + 16);

    ctx.fillStyle = C.info;
    ctx.font = "12px monospace";
    ctx.fillText("Step 1: Quantum approaches", lx, ly + 50);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("carrying e-coordinate \u03c6\u2080", lx, ly + 66);

    ctx.fillStyle = C.info;
    ctx.font = "12px monospace";
    ctx.fillText("Step 2: Horizon grows by 1 Planck area", lx, ly + 96);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("\u03c6_horizon \u2192 \u03c6_horizon + \u03b4\u03c6", lx, ly + 112);

    ctx.fillStyle = C.info;
    ctx.font = "12px monospace";
    ctx.fillText("Step 3: Information imprinted", lx, ly + 142);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("\u03b4\u03c6 = \u03c6\u2080 (by e-conservation)", lx, ly + 158);

    ctx.fillStyle = C.eCircle;
    ctx.font = "12px monospace";
    ctx.fillText("Key: e-dim has no causal structure", lx, ly + 195);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("\u03b4\u03c6 propagates across entire horizon", lx, ly + 211);
    ctx.fillText("instantaneously (geometric, not signal)", lx, ly + 227);

    // Right label
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("Information never crosses the horizon", cx, H - 40);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("The horizon grows to incorporate it \u2014 encoded in e-coordinate shifts", cx, H - 22);
  }

  function drawHawking(ctx, W, H, t) {
    const cx = W / 2, cy = H / 2;

    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Hawking Radiation: Thermal in 4D, Structured in 5D", cx, 28);

    // Black hole
    const bhR = 80;
    ctx.fillStyle = "rgba(0,0,0,0.9)";
    ctx.beginPath();
    ctx.arc(cx, cy, bhR, 0, TAU);
    ctx.fill();
    ctx.strokeStyle = C.horizon;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(cx, cy, bhR, 0, TAU);
    ctx.stroke();

    // Hawking quanta emanating outward
    const nQuanta = 12;
    for (let i = 0; i < nQuanta; i++) {
      const angle = (i / nQuanta) * TAU + t * 0.2;
      const phase = (t * 0.3 + i * 0.7) % 1;
      const dist = bhR + 15 + phase * 180;

      if (dist < bhR + 190) {
        const qx = cx + dist * Math.cos(angle);
        const qy = cy + dist * Math.sin(angle);

        // 4D: thermal (random colors, no structure)
        const thermalColor = `hsl(${(i * 137 + t * 50) % 360}, 60%, 60%)`;

        // Particle
        ctx.fillStyle = thermalColor;
        ctx.globalAlpha = 1 - phase * 0.7;
        ctx.beginPath();
        ctx.arc(qx, qy, 3, 0, TAU);
        ctx.fill();

        // e-coordinate marker (the hidden structure)
        const ePhi = i * 0.523 + Math.sin(i * 2.1) * 0.8; // deterministic, not random!
        const eR = 8;
        const ex = qx + eR * Math.cos(ePhi);
        const ey = qy + eR * Math.sin(ePhi);

        ctx.strokeStyle = C.eCircle;
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.arc(qx, qy, eR, 0, TAU);
        ctx.stroke();

        ctx.fillStyle = C.hawking5d;
        ctx.beginPath();
        ctx.arc(ex, ey, 2, 0, TAU);
        ctx.fill();

        ctx.globalAlpha = 1;
      }
    }

    // Left panel: 4D projection (thermal)
    ctx.fillStyle = C.hawking4d;
    ctx.font = "bold 13px monospace";
    ctx.textAlign = "center";
    ctx.fillText("4D Projection", 110, 90);

    ctx.font = "11px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("Integrating over e:", 110, 110);
    ctx.fillStyle = C.hawking4d;
    ctx.fillText("\u03c1_rad = Tr_e [|\u03c8\u27e9\u27e8\u03c8|]", 110, 128);
    ctx.fillStyle = C.textDim;
    ctx.fillText("= thermal (Planck spectrum)", 110, 146);
    ctx.fillText("= Hawking's result exactly", 110, 162);

    // Draw thermal spectrum sketch
    ctx.strokeStyle = C.hawking4d;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (let x = 0; x < 140; x++) {
      const freq = x / 30;
      const planck = freq * freq * freq / (Math.exp(freq) - 1 + 0.001);
      ctx.lineTo(40 + x, 240 - planck * 25);
    }
    ctx.stroke();
    ctx.fillStyle = C.textDim;
    ctx.font = "10px monospace";
    ctx.fillText("Planck spectrum", 110, 255);
    ctx.fillText("(no information)", 110, 268);

    // Right panel: 5D full state (structured)
    ctx.fillStyle = C.hawking5d;
    ctx.font = "bold 13px monospace";
    ctx.textAlign = "center";
    ctx.fillText("5D Full State", W - 110, 90);

    ctx.font = "11px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("Including e-coordinates:", W - 110, 110);
    ctx.fillStyle = C.hawking5d;
    ctx.fillText("|\u03c8(x,y,z,t,e)\u27e9", W - 110, 128);
    ctx.fillStyle = C.textDim;
    ctx.fillText("= pure state (unitary)", W - 110, 146);
    ctx.fillText("= complete information", W - 110, 162);

    // Draw structured spectrum sketch (same envelope but with structure)
    ctx.strokeStyle = C.hawking5d;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (let x = 0; x < 140; x++) {
      const freq = x / 30;
      const planck = freq * freq * freq / (Math.exp(freq) - 1 + 0.001);
      const structure = 1 + 0.3 * Math.sin(freq * 8) * Math.cos(freq * 3);
      ctx.lineTo(W - 180 + x, 240 - planck * structure * 25);
    }
    ctx.stroke();
    ctx.fillStyle = C.textDim;
    ctx.font = "10px monospace";
    ctx.fillText("Structured in e", W - 110, 255);
    ctx.fillText("(full information)", W - 110, 268);

    // Bottom
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("Hawking's calculation is correct \u2014 and it is a projection.", cx, H - 40);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("The 4D thermal result is the shadow of a 5D pure state. Information lives in the e-coordinates.", cx, H - 22);
  }

  function drawComparison(ctx, W, H, t) {
    const cx = W / 2;

    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("The Page Curve from e-Dimension Geometry", cx, 28);

    // Draw Page curve
    const mL = 100, mR = 60, mT = 70, mB = 80;
    const pW = W - mL - mR, pH = H - mT - mB;
    const toX = (frac) => mL + frac * pW;
    const toY = (s) => mT + (1 - s) * pH;

    // Axes
    ctx.strokeStyle = C.grid;
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(mL, mT); ctx.lineTo(mL, mT + pH); ctx.lineTo(mL + pW, mT + pH); ctx.stroke();

    ctx.fillStyle = C.text;
    ctx.font = "11px monospace";
    ctx.textAlign = "center";
    ctx.fillText("Time / Evaporation fraction", cx, H - 20);
    ctx.save();
    ctx.translate(25, mT + pH / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText("S_rad (entanglement entropy)", 0, 0);
    ctx.restore();

    // Page time marker
    const pageX = toX(0.5);
    ctx.strokeStyle = C.textDim;
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(pageX, mT); ctx.lineTo(pageX, mT + pH); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.textDim;
    ctx.fillText("Page time", pageX, mT + pH + 18);

    // Hawking curve (monotonically increasing — wrong)
    ctx.strokeStyle = C.hawking4d;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let i = 0; i <= 100; i++) {
      const frac = i / 100;
      const s = frac * 0.85; // monotonic rise
      ctx.lineTo(toX(frac), toY(s));
    }
    ctx.stroke();
    ctx.fillStyle = C.hawking4d;
    ctx.font = "12px monospace";
    ctx.textAlign = "right";
    ctx.fillText("Hawking (4D only)", mL + pW - 10, toY(0.82));
    ctx.font = "10px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("monotonic rise \u2192 information lost", mL + pW - 10, toY(0.82) + 14);

    // Page curve (correct — rises then falls)
    const animFrac = Math.min(1, (t * 0.1) % 2);
    ctx.strokeStyle = C.hawking5d;
    ctx.lineWidth = 2.5;
    ctx.shadowColor = "rgba(85,255,153,0.2)";
    ctx.shadowBlur = 6;
    ctx.beginPath();
    for (let i = 0; i <= 100; i++) {
      const frac = i / 100;
      if (frac > animFrac) break;
      // Page curve: rises to peak at 0.5, falls back to 0
      let s;
      if (frac < 0.5) {
        s = frac * 2 * 0.7; // rise to 0.7
      } else {
        s = (1 - frac) * 2 * 0.7; // fall back to 0
      }
      ctx.lineTo(toX(frac), toY(s));
    }
    ctx.stroke();
    ctx.shadowBlur = 0;

    ctx.fillStyle = C.hawking5d;
    ctx.font = "12px monospace";
    ctx.textAlign = "left";
    ctx.fillText("5D framework (Page curve)", mL + 10, toY(0.65));
    ctx.font = "10px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("rises \u2192 peaks \u2192 falls to zero", mL + 10, toY(0.65) + 14);
    ctx.fillText("information preserved", mL + 10, toY(0.65) + 28);

    // Mechanism annotations
    ctx.fillStyle = C.eCircle;
    ctx.font = "11px monospace";
    ctx.textAlign = "center";

    // Before Page time
    ctx.fillText("N_rad \u226a N_BH", toX(0.25), toY(0.9) + 20);
    ctx.fillStyle = C.textDim;
    ctx.fillText("e-info accumulates", toX(0.25), toY(0.9) + 34);
    ctx.fillText("in radiation", toX(0.25), toY(0.9) + 48);

    // After Page time
    ctx.fillStyle = C.eCircle;
    ctx.fillText("N_rad \u226b N_BH", toX(0.75), toY(0.9) + 20);
    ctx.fillStyle = C.textDim;
    ctx.fillText("e-correlations", toX(0.75), toY(0.9) + 34);
    ctx.fillText("purify the state", toX(0.75), toY(0.9) + 48);

    // Bottom
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("S = A/4 counts e-coordinate states on S\u00b2 \u00d7 S\u00b9: one bit per Planck pixel per e-circle state", cx, H - 45);
  }

  const btn = (active) => ({
    background: active ? "rgba(255,85,85,0.15)" : "transparent",
    color: active ? C.horizon : C.textDim,
    border: `1px solid ${active ? C.horizon : "rgba(100,140,200,0.2)"}`,
    padding: "4px 12px", fontSize: 12, fontFamily: "monospace",
    borderRadius: 3, cursor: "pointer",
  });

  return (
    <div style={{ background: C.bg, minHeight: "100vh", display: "flex", flexDirection: "column", alignItems: "center", padding: 20 }}>
      <canvas ref={canvasRef} width={900} height={520} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <button style={btn(view === "mechanism")} onClick={() => setView("mechanism")}>Information Encoding</button>
        <button style={btn(view === "hawking")} onClick={() => setView("hawking")}>4D Thermal vs 5D Structured</button>
        <button style={btn(view === "comparison")} onClick={() => setView("comparison")}>Page Curve Recovery</button>
      </div>
    </div>
  );
}
