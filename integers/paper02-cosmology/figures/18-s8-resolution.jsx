import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  planck: "#4488ff",
  planckBand: "rgba(40,100,255,0.12)",
  des: "#44cc77",
  kids: "#cc77ff",
  hsc: "#ffaa44",
  framework: "#ff6644",
  frameworkA: "#ff9944",
  frameworkB: "#ff6644",
  frameworkC: "#ffcc44",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  axis: "rgba(100,140,200,0.4)",
  resolved: "rgba(80,255,120,0.25)",
};

export default function S8Resolution() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0, reveal: 0 });

  const [showFramework, setShowFramework] = useState(true);
  const [animate, setAnimate] = useState(true);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.015;
    if (animate && st.reveal < 1) st.reveal += 0.008;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    const mL = 60, mR = 250, mT = 50, mB = 60;
    const pW = W - mL - mR, pH = H - mT - mB;

    // S8 axis (horizontal)
    const s8Min = 0.68, s8Max = 0.90;
    const toX = (s8) => mL + ((s8 - s8Min) / (s8Max - s8Min)) * pW;
    const rowH = 42;

    // Data points
    const data = [
      { name: "Planck 2018 (CMB)", s8: 0.832, err: 0.013, color: C.planck, y: 0 },
      { name: "DES Y3 (Weak Lensing)", s8: 0.776, err: 0.017, color: C.des, y: 1 },
      { name: "KiDS-1000 (WL)", s8: 0.759, err: 0.024, color: C.kids, y: 2 },
      { name: "HSC Y3 (WL)", s8: 0.763, err: 0.020, color: C.hsc, y: 3 },
    ];

    const fwData = [
      { name: "5D Scenario A (ξ=0.47)", s8: 0.753, color: C.frameworkA, y: 5 },
      { name: "5D Scenario B (ξ=0.432)", s8: 0.785, color: C.frameworkB, y: 6 },
      { name: "5D Scenario C (self-con.)", s8: 0.754, color: C.frameworkC, y: 7 },
    ];

    // Title
    ctx.font = "15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("S8 Tension: RESOLVED by the 5D Framework", W / 2, 30);
    ctx.textAlign = "left";

    // Planck band
    const planckL = toX(0.832 - 0.013);
    const planckR = toX(0.832 + 0.013);
    ctx.fillStyle = C.planckBand;
    ctx.fillRect(planckL, mT, planckR - planckL, pH);

    // WL consensus band
    const wlL = toX(0.755);
    const wlR = toX(0.795);
    ctx.fillStyle = "rgba(80,200,120,0.06)";
    ctx.fillRect(wlL, mT, wlR - wlL, pH);

    // Axis
    ctx.strokeStyle = C.axis;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(mL, mT + pH); ctx.lineTo(mL + pW, mT + pH);
    ctx.stroke();

    // X-axis labels
    ctx.font = "10px monospace";
    ctx.fillStyle = C.textDim;
    ctx.textAlign = "center";
    for (let s = 0.70; s <= 0.88; s += 0.02) {
      const x = toX(s);
      ctx.fillText(s.toFixed(2), x, mT + pH + 18);
      ctx.beginPath();
      ctx.moveTo(x, mT + pH - 3); ctx.lineTo(x, mT + pH + 3);
      ctx.strokeStyle = C.axis;
      ctx.stroke();
    }
    ctx.fillStyle = C.textDim;
    ctx.fillText("S8 = σ₈ × √(Ω_m / 0.3)", mL + pW / 2, mT + pH + 40);
    ctx.textAlign = "left";

    // Draw observational data
    for (const d of data) {
      const yPos = mT + 30 + d.y * rowH;
      const xPos = toX(d.s8);

      // Error bar
      ctx.strokeStyle = d.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(toX(d.s8 - d.err), yPos);
      ctx.lineTo(toX(d.s8 + d.err), yPos);
      ctx.stroke();
      // Caps
      ctx.beginPath();
      ctx.moveTo(toX(d.s8 - d.err), yPos - 5);
      ctx.lineTo(toX(d.s8 - d.err), yPos + 5);
      ctx.moveTo(toX(d.s8 + d.err), yPos - 5);
      ctx.lineTo(toX(d.s8 + d.err), yPos + 5);
      ctx.stroke();

      // Point
      ctx.beginPath();
      ctx.arc(xPos, yPos, 6, 0, TAU);
      ctx.fillStyle = d.color;
      ctx.fill();

      // Label
      ctx.fillStyle = d.color;
      ctx.font = "12px monospace";
      ctx.fillText(`${d.name}: ${d.s8.toFixed(3)} ± ${d.err.toFixed(3)}`, mL + pW + 15, yPos + 4);
    }

    // Separator
    const sepY = mT + 30 + 4.2 * rowH;
    ctx.strokeStyle = C.axis;
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.beginPath();
    ctx.moveTo(mL, sepY); ctx.lineTo(mL + pW, sepY);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.textDim;
    ctx.font = "10px monospace";
    ctx.fillText("5D Framework predictions ↓", mL + 5, sepY + 14);

    // Draw framework predictions (animated reveal)
    if (showFramework) {
      for (const d of fwData) {
        const yPos = mT + 30 + d.y * rowH;
        const xTarget = toX(d.s8);
        const xStart = toX(0.832); // Start from Planck position
        const xPos = xStart + (xTarget - xStart) * Math.min(1, st.reveal);

        // Animated trail
        if (st.reveal < 1) {
          ctx.strokeStyle = `rgba(255,100,60,${0.3 * (1 - st.reveal)})`;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(xStart, yPos); ctx.lineTo(xPos, yPos);
          ctx.stroke();
        }

        // Diamond marker
        ctx.save();
        ctx.translate(xPos, yPos);
        ctx.rotate(Math.PI / 4);
        ctx.fillStyle = d.color;
        ctx.fillRect(-5, -5, 10, 10);
        ctx.restore();

        // Label
        ctx.fillStyle = d.color;
        ctx.font = "11px monospace";
        ctx.fillText(`${d.name}: ${d.s8.toFixed(3)}`, mL + pW + 15, yPos + 4);
      }
    }

    // "TENSION" and "RESOLVED" annotations
    const tensionX = (toX(0.832) + toX(0.76)) / 2;
    const tensionY = mT + 30 + 1.5 * rowH;

    // Tension arrow
    ctx.strokeStyle = "rgba(255,80,80,0.4)";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(toX(0.819), tensionY - 30);
    ctx.lineTo(toX(0.795), tensionY - 30);
    ctx.stroke();
    ctx.fillStyle = "rgba(255,80,80,0.6)";
    ctx.font = "11px monospace";
    ctx.textAlign = "center";
    ctx.fillText("4σ tension", tensionX, tensionY - 38);

    // "RESOLVED" banner
    if (showFramework && st.reveal > 0.8) {
      const alpha = Math.min(1, (st.reveal - 0.8) * 5);
      ctx.fillStyle = `rgba(80,255,120,${0.12 * alpha})`;
      const bannerY = mT + 30 + 5.5 * rowH;
      ctx.fillRect(toX(0.74), bannerY - 15, toX(0.80) - toX(0.74), 30);
      ctx.fillStyle = `rgba(80,255,120,${0.8 * alpha})`;
      ctx.font = "14px monospace";
      ctx.fillText("RESOLVED", (toX(0.74) + toX(0.80)) / 2, bannerY + 5);
    }
    ctx.textAlign = "left";

    // Band labels
    ctx.font = "10px monospace";
    ctx.fillStyle = C.planck;
    ctx.save();
    ctx.translate(planckR + 3, mT + 10);
    ctx.rotate(Math.PI / 2);
    ctx.fillText("Planck 1σ", 0, 0);
    ctx.restore();

    animRef.current = requestAnimationFrame(draw);
  }, [showFramework, animate]);

  useEffect(() => {
    const canvas = canvasRef.current;
    const dpr = window.devicePixelRatio || 1;
    canvas.width = 800 * dpr; canvas.height = 450 * dpr;
    canvas.style.width = "800px"; canvas.style.height = "450px";
    canvas.getContext("2d").scale(dpr, dpr);
    stateRef.current.reveal = 0;
    animRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(animRef.current);
  }, [draw]);

  return (
    <div style={{ background: C.bg, padding: 16, borderRadius: 12, display: "inline-block" }}>
      <div style={{ color: C.text, fontFamily: "monospace", fontSize: 15, marginBottom: 8 }}>
        <strong>18 — S8 Tension Resolution</strong>
        <span style={{ color: C.textDim, marginLeft: 12 }}>Paper 2, Appendix C</span>
      </div>
      <canvas ref={canvasRef} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 12, marginTop: 8, alignItems: "center" }}>
        <label style={{ color: C.textDim, fontFamily: "monospace", fontSize: 12 }}>
          <input type="checkbox" checked={showFramework} onChange={e => { setShowFramework(e.target.checked); stateRef.current.reveal = 0; }} /> Show framework predictions
        </label>
        <button onClick={() => { stateRef.current.reveal = 0; }}
          style={{ background: "rgba(30,40,60,0.5)", color: C.text, border: "1px solid rgba(60,80,120,0.3)",
            borderRadius: 6, padding: "5px 14px", cursor: "pointer", fontFamily: "monospace", fontSize: 12 }}>
          Replay animation
        </button>
      </div>
    </div>
  );
}
