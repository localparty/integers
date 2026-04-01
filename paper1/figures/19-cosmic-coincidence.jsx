import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  visible: "#44aaff",
  dark: "#ff5555",
  ratio: "#ffcc44",
  ratioGlow: "rgba(255,200,60,0.15)",
  entropy: "#55ff99",
  washout: "#ff88ff",
  formula: "#ffaa44",
  axis: "rgba(100,140,200,0.4)",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  target: "rgba(255,200,60,0.5)",
};

export default function CosmicCoincidence() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0, flowPhase: 0 });

  const [xi, setXi] = useState(43);
  const [view, setView] = useState("overview"); // overview | mechanism | prediction

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const cx = W / 2, cy = H / 2;
    const st = stateRef.current;
    st.time += 0.015;
    st.flowPhase = (st.flowPhase + 0.005) % 1;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    const xiVal = xi / 100;
    const ratio = 1 / (xiVal * xiVal);

    if (view === "overview") {
      // The question and the answer in one visual

      // Visible matter bar
      const barY = cy - 60;
      const barH = 40;
      const visW = 80;
      const darkW = visW * ratio;
      const totalW = visW + darkW;
      const startX = cx - totalW / 2;

      // Visible
      ctx.fillStyle = C.visible;
      ctx.fillRect(startX, barY, visW, barH);
      ctx.strokeStyle = "rgba(40,140,255,0.6)";
      ctx.lineWidth = 1;
      ctx.strokeRect(startX, barY, visW, barH);
      ctx.fillStyle = C.visible;
      ctx.font = "13px monospace";
      ctx.textAlign = "center";
      ctx.fillText("Visible matter", startX + visW / 2, barY - 8);
      ctx.fillText("Ω_b", startX + visW / 2, barY + barH / 2 + 5);

      // Dark
      ctx.fillStyle = C.dark;
      ctx.fillRect(startX + visW, barY, darkW, barH);
      ctx.strokeStyle = "rgba(255,60,60,0.6)";
      ctx.strokeRect(startX + visW, barY, darkW, barH);
      ctx.fillStyle = C.dark;
      ctx.fillText("Dark matter (mirror baryons)", startX + visW + darkW / 2, barY - 8);
      ctx.fillText("Ω_DM", startX + visW + darkW / 2, barY + barH / 2 + 5);

      // Ratio annotation
      ctx.fillStyle = C.ratio;
      ctx.font = "18px monospace";
      ctx.fillText(`Ω_DM / Ω_b = ${ratio.toFixed(1)}×`, cx, barY + barH + 35);

      // The formula chain
      const chainY = barY + barH + 70;
      ctx.font = "14px monospace";
      ctx.fillStyle = C.text;
      ctx.fillText("WHY is dark matter ~5× more abundant than visible?", cx, chainY);

      ctx.font = "16px monospace";
      ctx.fillStyle = C.formula;
      ctx.fillText("Ω_DM / Ω_b = 1/ξ²", cx, chainY + 35);

      ctx.font = "13px monospace";
      ctx.fillStyle = C.entropy;
      ctx.fillText("1/ξ³  (entropy dilution)", cx - 120, chainY + 65);
      ctx.fillStyle = C.washout;
      ctx.fillText("×  1/ξ²  (weaker washout)", cx + 80, chainY + 65);

      ctx.fillStyle = C.text;
      ctx.fillText("× ξ³  (density normalization)  =  1/ξ²", cx, chainY + 90);

      ctx.fillStyle = C.ratio;
      ctx.font = "15px monospace";
      ctx.fillText(`ξ = ${xiVal.toFixed(3)}  →  Ω_DM/Ω_b = ${ratio.toFixed(2)}`, cx, chainY + 125);

      ctx.fillStyle = C.textDim;
      ctx.font = "12px monospace";
      ctx.fillText("The cosmic coincidence is a GEOMETRIC CONSEQUENCE of the two-brane thermal history", cx, chainY + 155);
      ctx.textAlign = "left";
    }

    if (view === "mechanism") {
      // Show the three factors visually

      const boxW = 200, boxH = 140;
      const gap = 30;
      const startX = cx - 1.5 * boxW - gap;
      const boxY = 60;

      const boxes = [
        { title: "Entropy Dilution", factor: "1/ξ³", value: (1 / Math.pow(xiVal, 3)).toFixed(1),
          color: C.entropy, desc: ["Mirror sector has", "fewer photons →", "same baryon number", "= higher η_B'"] },
        { title: "Weaker Washout", factor: "1/ξ²", value: (1 / Math.pow(xiVal, 2)).toFixed(1),
          color: C.washout, desc: ["Colder brane →", "earlier freeze-out →", "less washout →", "more asymmetry"] },
        { title: "Density Ratio", factor: "× ξ³", value: Math.pow(xiVal, 3).toFixed(3),
          color: C.visible, desc: ["Convert baryon", "asymmetry ratio", "to matter density", "ratio"] },
      ];

      for (let i = 0; i < 3; i++) {
        const bx = startX + i * (boxW + gap);
        const b = boxes[i];

        ctx.strokeStyle = b.color;
        ctx.lineWidth = 2;
        ctx.strokeRect(bx, boxY, boxW, boxH);
        ctx.fillStyle = `${b.color}11`;
        ctx.fillRect(bx, boxY, boxW, boxH);

        ctx.fillStyle = b.color;
        ctx.font = "13px monospace";
        ctx.textAlign = "center";
        ctx.fillText(b.title, bx + boxW / 2, boxY + 20);
        ctx.font = "20px monospace";
        ctx.fillText(b.factor, bx + boxW / 2, boxY + 50);
        ctx.font = "16px monospace";
        ctx.fillText(`= ${b.value}`, bx + boxW / 2, boxY + 75);

        ctx.fillStyle = C.textDim;
        ctx.font = "10px monospace";
        for (let j = 0; j < b.desc.length; j++) {
          ctx.fillText(b.desc[j], bx + boxW / 2, boxY + 95 + j * 12);
        }

        // Multiplication signs between boxes
        if (i < 2) {
          ctx.fillStyle = C.text;
          ctx.font = "20px monospace";
          ctx.fillText("×", bx + boxW + gap / 2, boxY + boxH / 2);
        }
      }

      // Result arrow
      const resultY = boxY + boxH + 30;
      ctx.strokeStyle = C.ratio;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx, resultY);
      ctx.lineTo(cx, resultY + 25);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(cx - 8, resultY + 17);
      ctx.lineTo(cx, resultY + 25);
      ctx.lineTo(cx + 8, resultY + 17);
      ctx.fill();

      // Result box
      ctx.fillStyle = "rgba(255,200,60,0.08)";
      ctx.fillRect(cx - 200, resultY + 30, 400, 60);
      ctx.strokeStyle = C.ratio;
      ctx.strokeRect(cx - 200, resultY + 30, 400, 60);
      ctx.fillStyle = C.ratio;
      ctx.font = "18px monospace";
      ctx.fillText("Ω_DM / Ω_b = (1/ξ³)(1/ξ²)(ξ³) = 1/ξ²", cx, resultY + 55);
      ctx.font = "15px monospace";
      ctx.fillText(`= 1/${xiVal.toFixed(2)}² = ${ratio.toFixed(2)}`, cx, resultY + 78);

      // Observed value comparison
      ctx.fillStyle = C.textDim;
      ctx.font = "13px monospace";
      ctx.fillText(`Observed: Ω_DM/Ω_b = 5.36    Predicted: ${ratio.toFixed(2)}    Match: ${(Math.abs(ratio - 5.36) / 5.36 * 100).toFixed(1)}%`, cx, resultY + 110);
      ctx.textAlign = "left";
    }

    if (view === "prediction") {
      // Plot 1/xi^2 vs xi with the observed value marked
      const mL = 80, mR = 40, mT = 60, mB = 80;
      const pW = W - mL - mR, pH = H - mT - mB;

      // Axes
      ctx.strokeStyle = C.axis;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(mL, mT); ctx.lineTo(mL, mT + pH); ctx.lineTo(mL + pW, mT + pH);
      ctx.stroke();

      const xiMin = 0.3, xiMax = 0.55;
      const rMin = 0, rMax = 12;
      const toX = (x) => mL + ((x - xiMin) / (xiMax - xiMin)) * pW;
      const toY = (r) => mT + pH - ((r - rMin) / (rMax - rMin)) * pH;

      // The 1/xi^2 curve
      ctx.beginPath();
      const nPts = 200;
      for (let i = 0; i <= nPts; i++) {
        const x = xiMin + (i / nPts) * (xiMax - xiMin);
        const y = 1 / (x * x);
        if (i === 0) ctx.moveTo(toX(x), toY(y));
        else ctx.lineTo(toX(x), toY(y));
      }
      ctx.strokeStyle = C.formula;
      ctx.lineWidth = 3;
      ctx.stroke();

      // Observed value horizontal line
      ctx.strokeStyle = C.target;
      ctx.lineWidth = 1.5;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(mL, toY(5.36)); ctx.lineTo(mL + pW, toY(5.36));
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = C.target;
      ctx.font = "12px monospace";
      ctx.textAlign = "right";
      ctx.fillText("Observed: 5.36", mL - 8, toY(5.36) + 4);

      // Intersection point
      const xiPred = 1 / Math.sqrt(5.36);
      ctx.beginPath();
      ctx.arc(toX(xiPred), toY(5.36), 8, 0, TAU);
      ctx.fillStyle = C.ratio;
      ctx.fill();
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Vertical line to intersection
      ctx.strokeStyle = C.ratio;
      ctx.lineWidth = 1;
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(toX(xiPred), toY(5.36));
      ctx.lineTo(toX(xiPred), mT + pH);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = C.ratio;
      ctx.font = "14px monospace";
      ctx.textAlign = "center";
      ctx.fillText(`ξ = ${xiPred.toFixed(3)}`, toX(xiPred), mT + pH + 22);
      ctx.fillText("PREDICTED", toX(xiPred), mT + pH + 40);

      // Current xi slider position
      const curR = 1 / (xiVal * xiVal);
      ctx.beginPath();
      ctx.arc(toX(xiVal), toY(curR), 5, 0, TAU);
      ctx.fillStyle = C.framework;
      ctx.fill();

      // Labels
      ctx.fillStyle = C.formula;
      ctx.font = "16px monospace";
      ctx.fillText("Ω_DM / Ω_b = 1/ξ²", cx, mT - 10);

      ctx.fillStyle = C.textDim;
      ctx.font = "12px monospace";
      ctx.fillText("ξ = T_hidden / T_visible", mL + pW / 2, mT + pH + 60);
      ctx.textAlign = "left";
      ctx.fillText("Ω_DM / Ω_b", 15, mT + pH / 2);

      // Y-axis ticks
      for (let r = 2; r <= 10; r += 2) {
        ctx.fillStyle = C.textDim;
        ctx.font = "10px monospace";
        ctx.fillText(r.toFixed(0), mL - 20, toY(r) + 4);
      }

      // X-axis ticks
      for (let x = 0.3; x <= 0.55; x += 0.05) {
        ctx.fillText(x.toFixed(2), toX(x) - 10, mT + pH + 15);
      }
    }

    animRef.current = requestAnimationFrame(draw);
  }, [xi, view]);

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
        <strong>19 — The Cosmic Coincidence Explained: Ω_DM/Ω_b = 1/ξ²</strong>
        <span style={{ color: C.textDim, marginLeft: 12 }}>Paper 2, Appendix E</span>
      </div>
      <canvas ref={canvasRef} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 10, marginTop: 8, alignItems: "center", flexWrap: "wrap" }}>
        {["overview", "mechanism", "prediction"].map(v => (
          <button key={v} onClick={() => setView(v)}
            style={{
              background: view === v ? "rgba(60,120,200,0.3)" : "rgba(30,40,60,0.5)",
              color: C.text, border: `1px solid ${view === v ? "rgba(100,160,255,0.5)" : "rgba(60,80,120,0.3)"}`,
              borderRadius: 6, padding: "5px 12px", cursor: "pointer", fontFamily: "monospace", fontSize: 11,
            }}>
            {v === "overview" ? "The question" : v === "mechanism" ? "The three factors" : "The prediction"}
          </button>
        ))}
        <label style={{ color: C.ratio, fontFamily: "monospace", fontSize: 13, display: "flex", alignItems: "center", gap: 6 }}>
          ξ: <input type="range" min={30} max={55} value={xi} onChange={e => setXi(+e.target.value)}
            style={{ width: 110 }} /> <strong>{(xi / 100).toFixed(2)}</strong>
          <span style={{ color: C.textDim, fontSize: 11 }}>→ Ω_DM/Ω_b = {(1 / (xi / 100) ** 2).toFixed(2)}</span>
        </label>
      </div>
    </div>
  );
}
