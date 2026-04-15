import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  orbital: "#44aaff",
  orbitalGlow: "rgba(68,170,255,0.12)",
  eWinding: "#ffcc44",
  eWindingGlow: "rgba(255,204,68,0.1)",
  proton: "#ff5555",
  energy: "#55ff99",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  grid: "rgba(30,50,90,0.15)",
};

// Hydrogen energy levels (eV) for n=1..4
const E_n = [0, -13.6, -3.4, -1.51, -0.85];

export default function Hydrogen5D() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });
  const [view, setView] = useState("orbital"); // orbital | levels | separation

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.015;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    if (view === "orbital") drawOrbital(ctx, W, H, st.time);
    else if (view === "levels") drawLevels(ctx, W, H, st.time);
    else drawSeparation(ctx, W, H, st.time);

    animRef.current = requestAnimationFrame(draw);
  }, [view]);

  useEffect(() => {
    animRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(animRef.current);
  }, [draw]);

  function drawOrbital(ctx, W, H, t) {
    const cx = W / 2 - 50, cy = H / 2 + 10;

    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("The Hydrogen Atom in 5D: Electron as Helical Path", W / 2, 28);
    ctx.font = "11px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("The electron orbits in (x,y,z) while winding around the e-circle", W / 2, 46);

    // Proton at center
    ctx.fillStyle = C.proton;
    ctx.shadowColor = "rgba(255,85,85,0.3)";
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.arc(cx, cy, 8, 0, TAU);
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = C.text;
    ctx.font = "10px monospace";
    ctx.fillText("p\u207a", cx, cy + 22);

    // Electron orbital (circular for s-state, shown from side to reveal helix)
    const orbitR = 100;
    const nPoints = 200;
    const helixAmp = 30; // amplitude of e-dimension oscillation

    // Draw the helix: orbit in (x,y) while oscillating in e
    ctx.strokeStyle = C.orbital;
    ctx.lineWidth = 2;
    ctx.shadowColor = C.orbitalGlow;
    ctx.shadowBlur = 8;
    ctx.beginPath();
    for (let i = 0; i <= nPoints; i++) {
      const frac = i / nPoints;
      const angle = frac * TAU * 2 + t * 0.5; // 2 full orbits
      const x = cx + orbitR * Math.cos(angle);
      const eOffset = helixAmp * Math.sin(angle * 1); // n=1/2 winding
      const y = cy + orbitR * Math.sin(angle) * 0.4 + eOffset * 0.3;
      if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Electron position (animated)
    const eAngle = t * 1.5;
    const ex = cx + orbitR * Math.cos(eAngle);
    const eOff = helixAmp * Math.sin(eAngle);
    const ey = cy + orbitR * Math.sin(eAngle) * 0.4 + eOff * 0.3;

    ctx.fillStyle = C.orbital;
    ctx.shadowColor = C.orbitalGlow;
    ctx.shadowBlur = 12;
    ctx.beginPath();
    ctx.arc(ex, ey, 5, 0, TAU);
    ctx.fill();
    ctx.shadowBlur = 0;

    // e-circle at electron position
    const ecR = 15;
    ctx.strokeStyle = C.eWinding;
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.arc(ex, ey, ecR, 0, TAU);
    ctx.stroke();

    // Phase marker on e-circle
    const ePhi = eAngle * 0.5; // spin-1/2: half winding per orbit
    const epx = ex + ecR * Math.cos(ePhi);
    const epy = ey + ecR * Math.sin(ePhi);
    ctx.fillStyle = C.eWinding;
    ctx.beginPath();
    ctx.arc(epx, epy, 3, 0, TAU);
    ctx.fill();

    // Annotations on right
    const rx = W - 280, ry = 80;
    ctx.textAlign = "left";

    ctx.fillStyle = C.orbital;
    ctx.font = "12px monospace";
    ctx.fillText("Spatial orbit: \u03c8(r)", rx, ry);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("Standard Coulomb solution", rx, ry + 16);
    ctx.fillText("E_n = -13.6/n\u00b2 eV", rx, ry + 32);

    ctx.fillStyle = C.eWinding;
    ctx.font = "12px monospace";
    ctx.fillText("e-winding: e^{in\u03c8}", rx, ry + 62);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("n = \u00b11/2 (spin-1/2 electron)", rx, ry + 78);
    ctx.fillText("E_e = n\u00b2\u210f\u00b2/(2mR\u00b2)", rx, ry + 94);
    ctx.fillText("= constant shift (spin energy)", rx, ry + 110);

    ctx.fillStyle = C.energy;
    ctx.font = "bold 12px monospace";
    ctx.fillText("5D equation separates cleanly:", rx, ry + 145);
    ctx.fillStyle = C.text;
    ctx.font = "11px monospace";
    ctx.fillText("\u03a8(r,\u03c8) = \u03c8_spatial(r) \u00b7 e^{in\u03c8}", rx, ry + 163);
    ctx.fillStyle = C.textDim;
    ctx.fillText("Spatial part = standard hydrogen", rx, ry + 183);
    ctx.fillText("e-part = spin quantum number", rx, ry + 199);

    ctx.fillStyle = C.energy;
    ctx.font = "12px monospace";
    ctx.fillText("Result: all 12 decimal places", rx, ry + 232);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("preserved from standard QM", rx, ry + 248);

    // Bottom
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("The 5D Schr\u00f6dinger equation separates on the e-circle \u2014 the spatial part IS the standard hydrogen equation", W / 2, H - 30);
  }

  function drawLevels(ctx, W, H, t) {
    const cx = W / 2;

    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Hydrogen Energy Levels from 5D Geometry", cx, 28);

    // Energy level diagram
    const mL = 120, mR = 350, mT = 70, mB = 60;
    const pW = W - mL - mR, pH = H - mT - mB;

    // y-axis: energy (eV)
    const eMin = -15, eMax = 1;
    const toY = (e) => mT + (1 - (e - eMin) / (eMax - eMin)) * pH;

    // Draw levels
    for (let n = 1; n <= 4; n++) {
      const y = toY(E_n[n]);
      const lw = 150;
      const lx = mL + (n - 1) * 55;

      // Level line
      ctx.strokeStyle = C.orbital;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(lx, y);
      ctx.lineTo(lx + lw, y);
      ctx.stroke();

      // Labels
      ctx.fillStyle = C.text;
      ctx.font = "12px monospace";
      ctx.textAlign = "right";
      ctx.fillText(`n=${n}`, lx - 8, y + 4);

      ctx.textAlign = "left";
      ctx.fillStyle = C.energy;
      ctx.fillText(`${E_n[n].toFixed(2)} eV`, lx + lw + 8, y + 4);

      // e-winding indicator (small circles)
      const eR = 8;
      for (let ms = -1; ms <= 1; ms += 2) {
        const ecx = lx + lw / 2 + ms * 20;
        const ecy = y - 15;

        ctx.strokeStyle = C.eWinding;
        ctx.lineWidth = 0.8;
        ctx.globalAlpha = 0.6;
        ctx.beginPath();
        ctx.arc(ecx, ecy, eR, 0, TAU);
        ctx.stroke();

        // Phase dot
        const phi = t + ms * 1.5;
        ctx.fillStyle = C.eWinding;
        ctx.beginPath();
        ctx.arc(ecx + eR * 0.7 * Math.cos(phi), ecy + eR * 0.7 * Math.sin(phi), 2, 0, TAU);
        ctx.fill();
        ctx.globalAlpha = 1;
      }
    }

    // Transition arrows
    ctx.strokeStyle = C.eWinding;
    ctx.lineWidth = 1;
    const transitions = [[2, 1], [3, 1], [3, 2], [4, 2]];
    const tNames = ["Lyman-\u03b1", "Lyman-\u03b2", "Balmer-\u03b1", "Balmer-\u03b2"];
    transitions.forEach(([ni, nf], idx) => {
      const y1 = toY(E_n[ni]);
      const y2 = toY(E_n[nf]);
      const ax = mL + 320 + idx * 30;

      ctx.beginPath();
      ctx.moveTo(ax, y1);
      ctx.lineTo(ax, y2);
      ctx.stroke();

      // Arrowhead
      ctx.beginPath();
      ctx.moveTo(ax - 4, y2 + 8);
      ctx.lineTo(ax, y2);
      ctx.lineTo(ax + 4, y2 + 8);
      ctx.stroke();
    });

    // Right annotation
    const rx = W - 310, ry = 80;
    ctx.textAlign = "left";

    ctx.fillStyle = C.text;
    ctx.font = "bold 13px monospace";
    ctx.fillText("What the 5D framework adds:", rx, ry);

    ctx.font = "11px monospace";
    ctx.fillStyle = C.eWinding;
    ctx.fillText("Each level has spin degeneracy", rx, ry + 25);
    ctx.fillStyle = C.textDim;
    ctx.fillText("from e-winding n = \u00b11/2", rx, ry + 41);

    ctx.fillStyle = C.eWinding;
    ctx.fillText("Spin is not ad hoc", rx, ry + 70);
    ctx.fillStyle = C.textDim;
    ctx.fillText("it is angular momentum in", rx, ry + 86);
    ctx.fillText("the e-dimension (Appendix B)", rx, ry + 102);

    ctx.fillStyle = C.energy;
    ctx.font = "12px monospace";
    ctx.fillText("All spectral predictions", rx, ry + 135);
    ctx.fillText("identical to standard QM", rx, ry + 151);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("because the 5D equation", rx, ry + 171);
    ctx.fillText("separates exactly.", rx, ry + 187);
    ctx.fillText("The spatial part IS the", rx, ry + 207);
    ctx.fillText("standard Schr\u00f6dinger equation.", rx, ry + 223);

    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("The e-dimension provides the geometric origin of spin \u2014 the spectrum is inherited exactly", cx, H - 30);
  }

  function drawSeparation(ctx, W, H, t) {
    const cx = W / 2;

    ctx.font = "bold 15px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("5D \u2192 4D: How the Equation Separates", cx, 28);

    // Show the separation visually
    const bw = 350, bh = 55, gap = 20;
    const startY = 75;

    // Box 1: Full 5D equation
    let y = startY;
    ctx.strokeStyle = C.text;
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.roundRect(cx - bw / 2, y, bw, bh, 6); ctx.stroke();
    ctx.fillStyle = C.text;
    ctx.font = "13px monospace";
    ctx.fillText("5D Schr\u00f6dinger on P(M\u00b3, U(1))", cx, y + 22);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("-(\u210f\u00b2/2m)[\u2207\u00b2\u2083 + (1/R\u00b2)\u2202\u00b2/\u2202\u03c8\u00b2]\u03a8 + V\u03a8 = E\u03a8", cx, y + 42);

    // Arrow down
    y += bh + gap;
    ctx.fillStyle = C.eWinding;
    ctx.beginPath();
    ctx.moveTo(cx, y - gap + 5);
    ctx.lineTo(cx - 8, y - 5);
    ctx.lineTo(cx + 8, y - 5);
    ctx.fill();
    ctx.font = "11px monospace";
    ctx.textAlign = "right";
    ctx.fillText("Separate: \u03a8 = \u03c8(r) \u00b7 e^{in\u03c8}", cx - 15, y - 7);
    ctx.textAlign = "center";

    // Box 2: Spatial part
    ctx.strokeStyle = C.orbital;
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.roundRect(cx - bw / 2 - 80, y, bw - 40, bh, 6); ctx.stroke();
    ctx.fillStyle = C.orbital;
    ctx.font = "13px monospace";
    ctx.textAlign = "center";
    const spatialCx = cx - 80;
    ctx.fillText("Spatial part (standard hydrogen)", spatialCx, y + 22);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("-(\u210f\u00b2/2m)\u2207\u00b2\u03c8 - e\u00b2/(4\u03c0\u03b5r)\u03c8 = E_n\u03c8", spatialCx, y + 42);

    // Box 3: e-part
    const eCx = cx + bw / 2 - 40;
    ctx.strokeStyle = C.eWinding;
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.roundRect(eCx - 80, y, 160, bh, 6); ctx.stroke();
    ctx.fillStyle = C.eWinding;
    ctx.font = "13px monospace";
    ctx.textAlign = "center";
    ctx.fillText("e-part (spin)", eCx, y + 22);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("E_e = n\u00b2\u210f\u00b2/2mR\u00b2", eCx, y + 42);

    // Arrows down from both
    y += bh + gap;

    // Result box
    ctx.strokeStyle = C.energy;
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.roundRect(cx - bw / 2, y, bw, bh + 10, 6); ctx.stroke();
    ctx.fillStyle = C.energy;
    ctx.font = "bold 14px monospace";
    ctx.textAlign = "center";
    ctx.fillText("E_total = -13.6/n\u00b2 + n\u00b2\u210f\u00b2/(2mR\u00b2)", cx, y + 25);
    ctx.fillStyle = C.textDim;
    ctx.font = "11px monospace";
    ctx.fillText("Coulomb spectrum + constant spin energy (same for all levels)", cx, y + 48);

    // Final annotation
    y += bh + gap + 20;
    ctx.fillStyle = C.text;
    ctx.font = "13px monospace";
    ctx.fillText("The 5D framework does not modify the hydrogen spectrum.", cx, y + 20);
    ctx.fillStyle = C.textDim;
    ctx.font = "12px monospace";
    ctx.fillText("It explains WHERE spin comes from: angular momentum in the e-dimension.", cx, y + 42);
    ctx.fillText("All 12 decimal places of spectral agreement are preserved exactly.", cx, y + 62);

    ctx.fillStyle = C.energy;
    ctx.font = "11px monospace";
    ctx.fillText("This is the framework's core design principle: reproduce all of QM, then explain its geometric origin.", cx, y + 90);
  }

  const btn = (active) => ({
    background: active ? "rgba(68,170,255,0.2)" : "transparent",
    color: active ? "#44aaff" : C.textDim,
    border: `1px solid ${active ? "#44aaff" : "rgba(100,140,200,0.2)"}`,
    padding: "4px 12px", fontSize: 12, fontFamily: "monospace",
    borderRadius: 3, cursor: "pointer",
  });

  return (
    <div style={{ background: C.bg, minHeight: "100vh", display: "flex", flexDirection: "column", alignItems: "center", padding: 20 }}>
      <canvas ref={canvasRef} width={900} height={520} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <button style={btn(view === "orbital")} onClick={() => setView("orbital")}>Helical Orbital</button>
        <button style={btn(view === "levels")} onClick={() => setView("levels")}>Energy Levels</button>
        <button style={btn(view === "separation")} onClick={() => setView("separation")}>5D Separation</button>
      </div>
    </div>
  );
}
