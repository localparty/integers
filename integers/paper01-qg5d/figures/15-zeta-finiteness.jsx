import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  partial: "#ff5555",
  zeta: "#44ff88",
  zetaGlow: "rgba(40,255,120,0.15)",
  mode: "#44aaff",
  modeGlow: "rgba(40,140,255,0.12)",
  axis: "rgba(100,140,200,0.5)",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  gold: "#ffcc44",
};

export default function ZetaFiniteness() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0, revealN: 0 });

  const [view, setView] = useState("sum"); // sum | oneloop | twoloop
  const [maxN, setMaxN] = useState(30);
  const [animating, setAnimating] = useState(true);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.02;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    if (animating && st.revealN < maxN) {
      st.revealN += 0.15;
    }
    const showN = Math.min(Math.floor(st.revealN), maxN);

    if (view === "sum") {
      // Main visualization: the KK mode sum converging under zeta regularization
      const marginL = 80, marginR = 40, marginT = 70, marginB = 110;
      const plotW = W - marginL - marginR;
      const plotH = H - marginT - marginB;

      // Axes
      ctx.strokeStyle = C.axis;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(marginL, marginT);
      ctx.lineTo(marginL, marginT + plotH);
      ctx.lineTo(marginL + plotW, marginT + plotH);
      ctx.stroke();

      ctx.font = "12px monospace";
      ctx.fillStyle = C.textDim;
      ctx.fillText("Number of KK modes N", marginL + plotW / 2 - 80, marginT + plotH + 30);
      ctx.save();
      ctx.translate(25, marginT + plotH / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText("Partial sum S_N", -40, 0);
      ctx.restore();

      // Compute partial sums
      // S_N = sum_{n=1}^{N} 1 (the divergent sum)
      // Under zeta regularization: 1 + 2*zeta(0) = 1 + 2*(-1/2) = 0
      const partials = [];
      let sum = 0;
      for (let n = 0; n <= maxN; n++) {
        sum = n; // S_N = N (just counting)
        partials.push(sum);
      }
      const maxSum = maxN;
      const zetaValue = 0; // The regularized answer

      // Y scale: show from -2 to maxN+2
      const yMin = -3, yMax = maxSum + 3;
      const toX = (n) => marginL + (n / maxN) * plotW;
      const toY = (s) => marginT + plotH - ((s - yMin) / (yMax - yMin)) * plotH;

      // Draw zeta-regularized value
      ctx.setLineDash([5, 5]);
      ctx.strokeStyle = C.zeta;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(marginL, toY(zetaValue));
      ctx.lineTo(marginL + plotW, toY(zetaValue));
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = C.zeta;
      ctx.font = "14px monospace";
      ctx.fillText("ζ-regularized: Σ 1 = 1 + 2ζ(0) = 0", marginL + plotW - 280, toY(zetaValue) - 10);

      // Draw partial sums (the diverging series)
      ctx.beginPath();
      for (let n = 0; n <= showN; n++) {
        const x = toX(n);
        const y = toY(partials[n]);
        if (n === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.strokeStyle = C.partial;
      ctx.lineWidth = 2.5;
      ctx.stroke();

      // Dots at each partial sum
      for (let n = 0; n <= showN; n++) {
        const x = toX(n);
        const y = toY(partials[n]);
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, TAU);
        ctx.fillStyle = C.partial;
        ctx.fill();
      }

      // Annotation
      ctx.fillStyle = C.partial;
      ctx.font = "13px monospace";
      if (showN > 5) {
        ctx.fillText(`S_${showN} = ${partials[showN]} (diverges!)`, toX(showN) + 10, toY(partials[showN]));
      }

      // The "magic": arrow from divergent sum to zero
      if (showN >= maxN * 0.8) {
        const arrowPhase = Math.sin(st.time * 2) * 0.5 + 0.5;
        ctx.strokeStyle = `rgba(255,200,60,${0.3 + 0.5 * arrowPhase})`;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(toX(showN) - 10, toY(partials[showN]));
        ctx.quadraticCurveTo(toX(showN) + 60, toY(partials[showN] / 2), toX(showN) - 10, toY(0));
        ctx.stroke();
        ctx.fillStyle = C.gold;
        ctx.font = "12px monospace";
        ctx.fillText("zeta regularization", toX(showN) + 15, toY(partials[showN] / 2));
      }

      // Y-axis labels
      ctx.font = "10px monospace";
      ctx.fillStyle = C.textDim;
      for (let y = 0; y <= maxSum; y += 5) {
        ctx.fillText(y.toString(), marginL - 25, toY(y) + 4);
        ctx.beginPath();
        ctx.moveTo(marginL - 3, toY(y));
        ctx.lineTo(marginL + 3, toY(y));
        ctx.strokeStyle = C.axis;
        ctx.stroke();
      }
    }

    if (view === "oneloop") {
      // One-loop: show the KK sum structure
      const cx = W / 2, cy = H / 2 - 20;

      // Loop diagram
      ctx.beginPath();
      ctx.arc(cx, cy, 80, 0, TAU);
      ctx.strokeStyle = C.mode;
      ctx.lineWidth = 3;
      ctx.stroke();

      // KK modes flowing around the loop
      const nModes = 12;
      for (let i = 0; i < nModes; i++) {
        const angle = (i / nModes) * TAU + st.time;
        const px = cx + 80 * Math.cos(angle);
        const py = cy + 80 * Math.sin(angle);
        const grd = ctx.createRadialGradient(px, py, 0, px, py, 12);
        grd.addColorStop(0, C.modeGlow);
        grd.addColorStop(1, "transparent");
        ctx.fillStyle = grd;
        ctx.fillRect(px - 12, py - 12, 24, 24);
        ctx.beginPath();
        ctx.arc(px, py, 4, 0, TAU);
        ctx.fillStyle = C.mode;
        ctx.fill();
        ctx.fillStyle = C.textDim;
        ctx.font = "9px monospace";
        ctx.fillText(`n=${i}`, px + 8, py + 3);
      }

      // External legs
      ctx.strokeStyle = C.axis;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx - 180, cy); ctx.lineTo(cx - 80, cy);
      ctx.moveTo(cx + 80, cy); ctx.lineTo(cx + 180, cy);
      ctx.stroke();
      ctx.fillStyle = C.text;
      ctx.font = "13px monospace";
      ctx.fillText("graviton", cx - 180, cy - 10);
      ctx.fillText("graviton", cx + 120, cy - 10);

      // Formula
      ctx.fillStyle = C.text;
      ctx.font = "14px monospace";
      ctx.textAlign = "center";
      ctx.fillText("One-loop: Γ₁ ~ Σ_{n∈Z} ∫ d⁴k / (k² + n²/R²)", cx, cy + 130);
      ctx.fillStyle = C.zeta;
      ctx.fillText("KK sum: Σ 1 = 1 + 2ζ(0) = 0  →  FINITE", cx, cy + 155);
      ctx.fillStyle = C.gold;
      ctx.fillText("The compact e-circle makes gravity finite at one loop", cx, cy + 185);
      ctx.textAlign = "left";
    }

    if (view === "twoloop") {
      // Two-loop: Goroff-Sagnotti topology
      const cx = W / 2, cy = H / 2 - 30;

      // Sunset diagram: two loops sharing a propagator
      ctx.lineWidth = 3;
      // Top loop
      ctx.beginPath();
      ctx.arc(cx - 40, cy - 20, 50, -0.3, Math.PI + 0.3);
      ctx.strokeStyle = C.mode;
      ctx.stroke();
      // Bottom loop
      ctx.beginPath();
      ctx.arc(cx + 40, cy + 20, 50, Math.PI - 0.3, TAU + 0.3);
      ctx.strokeStyle = C.partial;
      ctx.stroke();
      // Shared propagator
      ctx.beginPath();
      ctx.moveTo(cx - 40, cy + 30); ctx.lineTo(cx + 40, cy - 30);
      ctx.strokeStyle = C.axis;
      ctx.lineWidth = 2;
      ctx.stroke();

      // External legs
      ctx.beginPath();
      ctx.moveTo(cx - 180, cy); ctx.lineTo(cx - 80, cy);
      ctx.moveTo(cx + 80, cy); ctx.lineTo(cx + 180, cy);
      ctx.strokeStyle = C.axis;
      ctx.stroke();

      // KK modes animated
      for (let loop = 0; loop < 2; loop++) {
        const loopCx = loop === 0 ? cx - 40 : cx + 40;
        const loopCy = loop === 0 ? cy - 20 : cy + 20;
        const loopR = 50;
        for (let i = 0; i < 6; i++) {
          const angle = (i / 6) * TAU + st.time * (loop === 0 ? 1 : -1);
          const px = loopCx + loopR * Math.cos(angle);
          const py = loopCy + loopR * Math.sin(angle);
          ctx.beginPath();
          ctx.arc(px, py, 3, 0, TAU);
          ctx.fillStyle = loop === 0 ? C.mode : C.partial;
          ctx.fill();
        }
      }

      // The key: Goroff-Sagnotti
      ctx.fillStyle = C.text;
      ctx.font = "14px monospace";
      ctx.textAlign = "center";
      ctx.fillText("Two-loop (Goroff-Sagnotti): R³ counterterm", cx, cy + 100);
      ctx.fillStyle = C.partial;
      ctx.fillText("In 4D: DIVERGES → gravity non-renormalizable (1986)", cx, cy + 125);
      ctx.fillStyle = C.zeta;
      ctx.fillText("In 5D on S¹: Epstein zeta E₂(s; n²+nm+m²) = 0", cx, cy + 150);
      ctx.fillStyle = C.gold;
      ctx.fillText("The R³ coefficient vanishes identically at every mass order", cx, cy + 175);
      ctx.fillText("→ 5D gravity on the e-circle is two-loop FINITE", cx, cy + 200);
      ctx.textAlign = "left";
    }

    // Info panel
    ctx.fillStyle = C.panelBg;
    ctx.fillRect(12, H - 82, 420, 70);
    ctx.font = "13px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "left";

    if (view === "sum") {
      ctx.fillText("The KK mode sum Σ_{n∈Z} 1 diverges classically", 20, H - 62);
      ctx.fillStyle = C.zeta;
      ctx.fillText("Zeta regularization: 1 + 2ζ(0) = 1 + 2(−½) = 0", 20, H - 42);
      ctx.fillStyle = C.textDim;
      ctx.fillText("Same math as the Casimir effect — physically justified by S¹ compactness", 20, H - 22);
    } else if (view === "oneloop") {
      ctx.fillText("One-loop graviton self-energy: KK modes circulate", 20, H - 62);
      ctx.fillStyle = C.zeta;
      ctx.fillText("Discrete sum replaces continuous integral → finite", 20, H - 42);
      ctx.fillStyle = C.textDim;
      ctx.fillText("The e-circle compactness is the UV regulator", 20, H - 22);
    } else {
      ctx.fillText("Goroff-Sagnotti (1986): proved 4D gravity non-renormalizable", 20, H - 62);
      ctx.fillStyle = C.zeta;
      ctx.fillText("On M⁴ × S¹: the SAME counterterm VANISHES by Epstein zeta zeros", 20, H - 42);
      ctx.fillStyle = C.textDim;
      ctx.fillText("Eisenstein lattice structure forces cancellation at every order", 20, H - 22);
    }

    animRef.current = requestAnimationFrame(draw);
  }, [view, maxN, animating]);

  useEffect(() => {
    const canvas = canvasRef.current;
    const dpr = window.devicePixelRatio || 1;
    canvas.width = 800 * dpr; canvas.height = 550 * dpr;
    canvas.style.width = "800px"; canvas.style.height = "550px";
    canvas.getContext("2d").scale(dpr, dpr);
    stateRef.current.revealN = 0;
    animRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(animRef.current);
  }, [draw]);

  return (
    <div style={{ background: C.bg, padding: 16, borderRadius: 12, display: "inline-block" }}>
      <div style={{ color: C.text, fontFamily: "monospace", fontSize: 15, marginBottom: 8 }}>
        <strong>15 — Perturbative Finiteness: Zeta Regularization</strong>
        <span style={{ color: C.textDim, marginLeft: 12 }}>Appendices F, G, K</span>
      </div>
      <canvas ref={canvasRef} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 12, marginTop: 8, alignItems: "center", flexWrap: "wrap" }}>
        {["sum", "oneloop", "twoloop"].map(v => (
          <button key={v} onClick={() => { setView(v); stateRef.current.revealN = 0; }}
            style={{
              background: view === v ? "rgba(60,120,200,0.3)" : "rgba(30,40,60,0.5)",
              color: C.text, border: `1px solid ${view === v ? "rgba(100,160,255,0.5)" : "rgba(60,80,120,0.3)"}`,
              borderRadius: 6, padding: "5px 14px", cursor: "pointer", fontFamily: "monospace", fontSize: 12,
            }}>
            {v === "sum" ? "KK mode sum → 0" : v === "oneloop" ? "One-loop diagram" : "Goroff-Sagnotti (two-loop)"}
          </button>
        ))}
        {view === "sum" && (
          <label style={{ color: C.textDim, fontFamily: "monospace", fontSize: 12, display: "flex", alignItems: "center", gap: 6 }}>
            Max N: <input type="range" min={10} max={60} value={maxN} onChange={e => { setMaxN(+e.target.value); stateRef.current.revealN = 0; }}
              style={{ width: 80 }} />
          </label>
        )}
        <button onClick={() => { stateRef.current.revealN = 0; setAnimating(true); }}
          style={{ background: "rgba(30,40,60,0.5)", color: C.text, border: "1px solid rgba(60,80,120,0.3)",
            borderRadius: 6, padding: "5px 14px", cursor: "pointer", fontFamily: "monospace", fontSize: 12 }}>
          Replay
        </button>
      </div>
    </div>
  );
}
