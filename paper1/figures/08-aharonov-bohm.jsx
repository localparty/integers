import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;
const PI = Math.PI;

// Flux quantum
const PHI0 = 1.0; // normalized: Phi_0 = h/e = 1

function lerp(a, b, t) { return a + (b - a) * t; }
function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }

export default function AharonovBohm() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({
    time: 0,
    flux: 0,
    showPhases: true,
    animate: true,
  });

  const [flux, setFlux] = useState(0);
  const [showPhases, setShowPhases] = useState(true);
  const [animateElectrons, setAnimateElectrons] = useState(true);
  const dragging = useRef(false);
  const lastMouse = useRef({ x: 0, y: 0 });

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width;
    const H = canvas.height;
    const s = stateRef.current;

    ctx.clearRect(0, 0, W, H);

    // Background
    ctx.fillStyle = "#050709";
    ctx.fillRect(0, 0, W, H);

    // --- Layout ---
    const topH = H * 0.58;
    const topCx = W * 0.5;
    const topCy = topH * 0.48;
    const solenoidR = Math.min(W, topH) * 0.075;

    // Normalized flux
    const phi = s.flux;
    const phaseDiff = TAU * phi / PHI0;
    const fringeShift = phi / PHI0;

    // --- TOP PANEL: e-space topology ---

    // Subtle grid
    ctx.strokeStyle = "rgba(40,60,90,0.12)";
    ctx.lineWidth = 0.5;
    for (let gx = 0; gx < W; gx += 40) {
      ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, topH); ctx.stroke();
    }
    for (let gy = 0; gy < topH; gy += 40) {
      ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
    }

    // Panel label
    ctx.fillStyle = "rgba(80,160,255,0.45)";
    ctx.font = "bold 11px 'Courier New'";
    ctx.fillText("E-SPACE TOPOLOGY", 20, 28);

    // Solenoid (filled circle)
    const solGrad = ctx.createRadialGradient(topCx, topCy, 0, topCx, topCy, solenoidR);
    solGrad.addColorStop(0, "rgba(255,210,60,0.95)");
    solGrad.addColorStop(0.6, "rgba(220,170,30,0.75)");
    solGrad.addColorStop(1, "rgba(180,130,10,0.3)");
    ctx.beginPath();
    ctx.arc(topCx, topCy, solenoidR, 0, TAU);
    ctx.fillStyle = solGrad;
    ctx.fill();
    ctx.strokeStyle = "rgba(255,220,80,0.6)";
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Cross-hatch inside solenoid to show B field into page
    ctx.strokeStyle = "rgba(120,90,20,0.6)";
    ctx.lineWidth = 1;
    const crosses = 5;
    for (let ci = 0; ci < crosses; ci++) {
      const angle = (ci / crosses) * TAU + s.time * 0.3;
      const cr = solenoidR * 0.5 * (0.3 + 0.7 * (ci % 2 ? 0.5 : 0.8));
      const ccx = topCx + Math.cos(angle) * cr * 0.6;
      const ccy = topCy + Math.sin(angle) * cr * 0.6;
      const cs = 3.5;
      ctx.beginPath(); ctx.moveTo(ccx - cs, ccy - cs); ctx.lineTo(ccx + cs, ccy + cs); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(ccx + cs, ccy - cs); ctx.lineTo(ccx - cs, ccy + cs); ctx.stroke();
    }

    // Solenoid label
    ctx.fillStyle = "rgba(255,220,80,0.7)";
    ctx.font = "10px 'Courier New'";
    ctx.textAlign = "center";
    ctx.fillText("B \u2260 0", topCx, topCy + 4);
    ctx.fillText("solenoid", topCx, topCy + solenoidR + 16);
    ctx.textAlign = "left";

    // B = 0 outside label
    ctx.fillStyle = "rgba(100,140,180,0.4)";
    ctx.font = "10px 'Courier New'";
    ctx.fillText("B = 0 outside", topCx + solenoidR + 14, topCy - solenoidR + 4);
    ctx.fillText("A \u2260 0 (connection)", topCx + solenoidR + 14, topCy - solenoidR + 18);

    // Source and detector points
    const srcX = topCx - solenoidR * 4.5, srcY = topCy;
    const detX = topCx + solenoidR * 4.5, detY = topCy;
    ctx.fillStyle = "rgba(180,220,255,0.8)";
    ctx.font = "10px 'Courier New'";
    ctx.textAlign = "center";
    for (const [px, py, label] of [[srcX, srcY, "source"], [detX, detY, "detector"]]) {
      ctx.beginPath(); ctx.arc(px, py, 5, 0, TAU); ctx.fill();
      ctx.fillStyle = "rgba(150,200,255,0.6)";
      ctx.fillText(label, px, py + 18);
      ctx.fillStyle = "rgba(180,220,255,0.8)";
    }
    ctx.textAlign = "left";

    // Draw electron paths
    const pathSteps = 80;
    const spread = solenoidR * 1.8;

    function getPathPt(t, side) {
      // side: -1 = upper (blue), +1 = lower (red)
      const x = lerp(srcX, detX, t);
      const bulge = Math.sin(t * PI);
      const y = topCy + side * spread * bulge;
      return { x, y };
    }

    // Draw path curves
    for (const side of [-1, 1]) {
      const color = side < 0 ? "rgba(80,150,255," : "rgba(255,80,100,";
      ctx.beginPath();
      for (let i = 0; i <= pathSteps; i++) {
        const t = i / pathSteps;
        const pt = getPathPt(t, side);
        i === 0 ? ctx.moveTo(pt.x, pt.y) : ctx.lineTo(pt.x, pt.y);
      }
      ctx.strokeStyle = color + "0.5)";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Path arrows along the curve
      for (let ai = 1; ai < 6; ai++) {
        const t = ai / 6;
        const pt = getPathPt(t, side);
        const pt2 = getPathPt(t + 0.01, side);
        const angle = Math.atan2(pt2.y - pt.y, pt2.x - pt.x);
        ctx.save();
        ctx.translate(pt.x, pt.y);
        ctx.rotate(angle);
        ctx.beginPath();
        ctx.moveTo(6, 0);
        ctx.lineTo(-3, -3);
        ctx.lineTo(-3, 3);
        ctx.closePath();
        ctx.fillStyle = color + "0.4)";
        ctx.fill();
        ctx.restore();
      }

      // Path labels
      if (side < 0) {
        ctx.fillStyle = "rgba(80,150,255,0.6)";
        ctx.font = "10px 'Courier New'";
        ctx.textAlign = "center";
        ctx.fillText("path 1 (upper)", topCx, topCy - spread - 10);
      } else {
        ctx.fillStyle = "rgba(255,80,100,0.6)";
        ctx.font = "10px 'Courier New'";
        ctx.textAlign = "center";
        ctx.fillText("path 2 (lower)", topCx, topCy + spread + 20);
      }
    }
    ctx.textAlign = "left";

    // Animate electrons along paths
    if (s.animate) {
      s.time += 0.006;
    }
    const electronT = (s.time * 0.7) % 1.0;

    for (const side of [-1, 1]) {
      const pt = getPathPt(electronT, side);
      const color = side < 0 ? [80, 150, 255] : [255, 80, 100];

      // Electron glow
      const eGrad = ctx.createRadialGradient(pt.x, pt.y, 0, pt.x, pt.y, 14);
      eGrad.addColorStop(0, `rgba(${color.join(",")},0.8)`);
      eGrad.addColorStop(1, `rgba(${color.join(",")},0)`);
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, 14, 0, TAU);
      ctx.fillStyle = eGrad;
      ctx.fill();

      // Electron dot
      ctx.beginPath(); ctx.arc(pt.x, pt.y, 4, 0, TAU);
      ctx.fillStyle = `rgb(${color.join(",")})`; ctx.fill();

      // e-phase indicator (rotating clock hand showing accumulated phase)
      if (s.showPhases && electronT > 0.02) {
        const fluxContrib = side < 0 ? phaseDiff * 0.5 : -phaseDiff * 0.5;
        const currentPhase = electronT * TAU * 3 + fluxContrib * electronT;
        const phaseR = 12;
        const pcx = pt.x + (side < 0 ? -18 : 18), pcy = pt.y + (side < 0 ? -16 : 16);
        ctx.beginPath(); ctx.arc(pcx, pcy, phaseR, 0, TAU);
        ctx.fillStyle = "rgba(10,15,25,0.8)"; ctx.fill();
        ctx.strokeStyle = `rgba(${color.join(",")},0.4)`; ctx.lineWidth = 1; ctx.stroke();
        ctx.beginPath(); ctx.moveTo(pcx, pcy);
        ctx.lineTo(pcx + Math.cos(currentPhase) * (phaseR - 2), pcy + Math.sin(currentPhase) * (phaseR - 2));
        ctx.strokeStyle = `rgba(${color.join(",")},0.9)`; ctx.lineWidth = 2; ctx.stroke();
        ctx.beginPath(); ctx.arc(pcx, pcy, 2, 0, TAU);
        ctx.fillStyle = `rgb(${color.join(",")})`; ctx.fill();
      }
    }

    // Phase difference indicator (e-circle) at detector
    if (s.showPhases) {
      const pdR = 22, pdCx = detX + 45, pdCy = detY - 35;
      ctx.beginPath(); ctx.arc(pdCx, pdCy, pdR + 2, 0, TAU);
      ctx.fillStyle = "rgba(10,15,25,0.85)"; ctx.fill();
      ctx.strokeStyle = "rgba(120,160,200,0.3)"; ctx.lineWidth = 1; ctx.stroke();
      if (Math.abs(phaseDiff) > 0.01) {
        ctx.beginPath(); ctx.moveTo(pdCx, pdCy);
        ctx.arc(pdCx, pdCy, pdR, 0, phaseDiff % TAU, phaseDiff < 0);
        ctx.closePath(); ctx.fillStyle = "rgba(180,100,255,0.25)"; ctx.fill();
        ctx.beginPath(); ctx.arc(pdCx, pdCy, pdR, 0, phaseDiff % TAU, phaseDiff < 0);
        ctx.strokeStyle = "rgba(180,100,255,0.7)"; ctx.lineWidth = 2; ctx.stroke();
      }

      // Reference line (blue) and phase diff hand (red)
      ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(pdCx, pdCy); ctx.lineTo(pdCx + pdR, pdCy);
      ctx.strokeStyle = "rgba(80,150,255,0.6)"; ctx.stroke();
      const pdAngle = phaseDiff % TAU;
      ctx.beginPath(); ctx.moveTo(pdCx, pdCy);
      ctx.lineTo(pdCx + Math.cos(pdAngle) * pdR, pdCy + Math.sin(pdAngle) * pdR);
      ctx.strokeStyle = "rgba(255,80,100,0.8)"; ctx.stroke();
      // Label
      ctx.fillStyle = "rgba(180,140,255,0.7)";
      ctx.font = "9px 'Courier New'";
      ctx.textAlign = "center";
      ctx.fillText("e-circle", pdCx, pdCy + pdR + 14);
      ctx.fillText("\u0394\u03C6", pdCx, pdCy + pdR + 26);
      ctx.textAlign = "left";
    }

    // Divider line
    ctx.strokeStyle = "rgba(60,120,200,0.15)"; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(20, topH + 8); ctx.lineTo(W - 20, topH + 8); ctx.stroke();

    // --- BOTTOM PANEL: Interference pattern ---
    const botTop = topH + 24;
    const barX = W * 0.1;
    const barW = W * 0.8;
    const barY = botTop + 18;
    const barH = 50;
    const fringeCount = 12;

    ctx.fillStyle = "rgba(80,160,255,0.45)";
    ctx.font = "bold 11px 'Courier New'";
    ctx.fillText("INTERFERENCE PATTERN AT DETECTOR", barX, botTop + 8);

    // Draw interference pattern
    const patternResolution = Math.floor(barW);
    for (let px = 0; px < patternResolution; px++) {
      const x = barX + px;
      const y0 = (px / patternResolution - 0.5) * fringeCount * TAU;
      const shift = phaseDiff * 0.5;
      const intensity = Math.pow(Math.cos((y0 + shift) * 0.5), 2);
      const envelope = Math.exp(-Math.pow((px / patternResolution - 0.5) * 3.5, 2));
      const val = intensity * envelope;

      const r = Math.floor(lerp(5, 80, val) + lerp(0, 120, val * val));
      const g = Math.floor(lerp(7, 160, val) + lerp(0, 60, val * val));
      const b = Math.floor(lerp(9, 255, val));
      ctx.fillStyle = `rgb(${r},${g},${b})`;
      ctx.fillRect(x, barY, 1, barH);
    }

    // Border
    ctx.strokeStyle = "rgba(60,120,200,0.25)";
    ctx.lineWidth = 1;
    ctx.strokeRect(barX, barY, barW, barH);

    // Fringe position markers
    ctx.strokeStyle = "rgba(255,220,80,0.35)";
    ctx.lineWidth = 0.5;
    const markerY = barY + barH + 3;
    for (let fi = -Math.floor(fringeCount / 2); fi <= Math.floor(fringeCount / 2); fi++) {
      const basePos = 0.5 + fi / fringeCount;
      const shiftedPos = basePos - (phaseDiff / TAU) / fringeCount;
      if (shiftedPos > 0 && shiftedPos < 1) {
        const mx = barX + shiftedPos * barW;
        ctx.beginPath();
        ctx.moveTo(mx, barY + barH);
        ctx.lineTo(mx, markerY + 5);
        ctx.stroke();
      }
    }

    // Fringe labels
    ctx.fillStyle = "rgba(150,180,220,0.4)";
    ctx.font = "9px 'Courier New'";
    ctx.textAlign = "center";
    ctx.fillText("bright", barX + barW * 0.5, markerY + 16);
    ctx.fillText("dark", barX + barW * 0.35, markerY + 16);
    ctx.fillText("dark", barX + barW * 0.65, markerY + 16);
    ctx.textAlign = "left";

    // Shift indicator arrow
    if (Math.abs(phaseDiff) > 0.05) {
      const abx = barX + barW * 0.5, ary = barY - 8;
      const atx = abx + (phaseDiff / TAU) * (barW / fringeCount) * -0.5;
      const dir = atx > abx ? 1 : -1;
      ctx.strokeStyle = "rgba(255,180,80,0.6)"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(abx, ary); ctx.lineTo(atx, ary); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(atx, ary); ctx.lineTo(atx - dir * 5, ary - 3);
      ctx.lineTo(atx - dir * 5, ary + 3); ctx.closePath();
      ctx.fillStyle = "rgba(255,180,80,0.6)"; ctx.fill();
      ctx.fillStyle = "rgba(255,180,80,0.5)"; ctx.font = "9px 'Courier New'";
      ctx.textAlign = "center"; ctx.fillText("shift", (abx + atx) / 2, ary - 5); ctx.textAlign = "left";
    }

    // --- READOUTS ---
    const readY = botTop + barH + 52;
    const phasePi = (phaseDiff / PI).toFixed(2);
    const fringeVal = fringeShift.toFixed(3);

    ctx.fillStyle = "rgba(180,140,255,0.8)";
    ctx.font = "12px 'Courier New'";
    ctx.fillText(`Phase difference: \u0394\u03C6 = (e/\u210F)\u03A6 = ${phasePi}\u03C0`, barX, readY);

    ctx.fillStyle = "rgba(255,200,80,0.7)";
    ctx.fillText(`Fringe shift: ${fringeVal} fringes`, barX + barW * 0.48, readY);

    // Special state highlight
    const phiRatio = phi / PHI0;
    if (Math.abs(phiRatio - 1.0) < 0.02 || Math.abs(phiRatio - 2.0) < 0.02) {
      ctx.fillStyle = "rgba(80,255,120,0.6)";
      ctx.font = "11px 'Courier New'";
      ctx.fillText("\u2713 Pattern returned to original position (\u03A6 = n\u03A6\u2080)", barX, readY + 18);
    } else if (Math.abs(phiRatio - 0.5) < 0.02 || Math.abs(phiRatio - 1.5) < 0.02) {
      ctx.fillStyle = "rgba(255,120,80,0.6)";
      ctx.font = "11px 'Courier New'";
      ctx.fillText("\u2717 Maximum shift \u2014 fringes inverted (\u03A6 = (n+\u00BD)\u03A6\u2080)", barX, readY + 18);
    }

    // --- ANNOTATIONS ---
    const annotY = readY + 40;
    ctx.fillStyle = "rgba(120,155,195,0.42)";
    ctx.font = "11px 'Courier New'";

    const line1 = "The solenoid creates a topological defect in e-space. The magnetic field B = 0";
    const line2 = "outside, but the connection A \u2260 0. The two paths accumulate different e-phases";
    const line3 = "\u2014 the difference is (e/\u210F)\u03A6.";
    ctx.fillText(line1, 20, annotY);
    ctx.fillText(line2, 20, annotY + 15);
    ctx.fillText(line3, 20, annotY + 30);

    ctx.fillStyle = "rgba(255,210,80,0.38)";
    ctx.fillText("Flux quantum \u03A6\u2080 = h/e: one full revolution of the e-circle.", 20, annotY + 52);

    animRef.current = requestAnimationFrame(draw);
  }, [flux, showPhases, animateElectrons]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const resize = () => {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    };
    resize();
    window.addEventListener("resize", resize);
    animRef.current = requestAnimationFrame(draw);
    return () => {
      cancelAnimationFrame(animRef.current);
      window.removeEventListener("resize", resize);
    };
  }, [draw]);

  // Mouse drag adjusts flux
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const onDown = (e) => {
      dragging.current = true;
      lastMouse.current = { x: e.clientX, y: e.clientY };
    };
    const onMove = (e) => {
      if (!dragging.current) return;
      const dx = e.clientX - lastMouse.current.x;
      lastMouse.current = { x: e.clientX, y: e.clientY };
      const newFlux = clamp(stateRef.current.flux + dx * 0.004, 0, 2 * PHI0);
      stateRef.current.flux = newFlux;
      setFlux(newFlux);
    };
    const onUp = () => { dragging.current = false; };
    canvas.addEventListener("mousedown", onDown);
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
    return () => {
      canvas.removeEventListener("mousedown", onDown);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", onUp);
    };
  }, []);

  const setFluxValue = (v) => {
    stateRef.current.flux = v;
    setFlux(v);
  };

  const togglePhases = () => {
    const next = !showPhases;
    stateRef.current.showPhases = next;
    setShowPhases(next);
  };

  const toggleAnimate = () => {
    const next = !animateElectrons;
    stateRef.current.animate = next;
    setAnimateElectrons(next);
  };

  const btnStyle = (active) => ({
    padding: "5px 12px",
    fontSize: 11,
    letterSpacing: "0.08em",
    background: active ? "rgba(60,120,200,0.35)" : "rgba(30,50,80,0.3)",
    border: `1px solid ${active ? "rgba(80,160,255,0.6)" : "rgba(60,100,160,0.25)"}`,
    color: active ? "#80c0ff" : "rgba(120,160,200,0.6)",
    borderRadius: 4,
    cursor: "pointer",
    transition: "all 0.15s",
    fontFamily: "'Courier New', monospace",
  });

  const presetBtn = (label, val) => (
    <button
      key={label}
      onClick={() => setFluxValue(val)}
      style={btnStyle(Math.abs(flux - val) < 0.01)}
    >{label}</button>
  );

  // Slider tick marks
  const sliderTicks = [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0];

  return (
    <div style={{
      background: "#050709",
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      fontFamily: "'Courier New', monospace",
      color: "#a0c0e0",
      userSelect: "none",
    }}>
      {/* Header */}
      <div style={{
        padding: "18px 28px 10px",
        borderBottom: "1px solid rgba(60,120,200,0.2)",
        display: "flex",
        alignItems: "baseline",
        gap: 16,
      }}>
        <span style={{
          fontSize: 11,
          letterSpacing: "0.18em",
          color: "rgba(80,160,255,0.5)",
          textTransform: "uppercase",
        }}>Quantum Geometry in 5D</span>
        <span style={{ color: "rgba(80,160,255,0.2)", fontSize: 11 }}>|</span>
        <span style={{ fontSize: 13, color: "rgba(160,200,240,0.7)", letterSpacing: "0.05em" }}>
          Visualization 08 — The Aharonov-Bohm Effect
        </span>
      </div>

      {/* Canvas */}
      <canvas
        ref={canvasRef}
        style={{
          flex: 1,
          width: "100%",
          cursor: dragging.current ? "grabbing" : "ew-resize",
          display: "block",
        }}
      />

      {/* Controls */}
      <div style={{
        padding: "14px 28px 20px",
        borderTop: "1px solid rgba(60,120,200,0.15)",
        display: "flex",
        flexWrap: "wrap",
        gap: "18px 32px",
        alignItems: "center",
        background: "rgba(5,7,9,0.95)",
      }}>

        {/* Flux slider */}
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          <span style={{ fontSize: 10, letterSpacing: "0.15em", color: "rgba(100,160,220,0.5)", textTransform: "uppercase" }}>
            Magnetic Flux {"\u03A6"}
          </span>
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <span style={{ fontSize: 11, color: "rgba(255,210,80,0.6)", width: 18 }}>0</span>
            <div style={{ position: "relative", width: 200 }}>
              <input
                type="range" min={0} max={200} value={Math.round(flux * 100)}
                onChange={e => setFluxValue(Number(e.target.value) / 100)}
                style={{
                  width: 200,
                  accentColor: "#ffcc33",
                  cursor: "pointer",
                }}
              />
              {/* Tick labels */}
              <div style={{ display: "flex", justifyContent: "space-between", marginTop: 2, width: 200 }}>
                {sliderTicks.map(t => (
                  <span key={t} style={{
                    fontSize: 8,
                    color: "rgba(255,210,80,0.35)",
                    width: 0,
                    textAlign: "center",
                    position: "relative",
                    left: t === 0 ? 4 : t === 2.0 ? -4 : 0,
                  }}>{t}</span>
                ))}
              </div>
            </div>
            <span style={{ fontSize: 11, color: "rgba(255,210,80,0.6)", width: 32 }}>2{"\u03A6\u2080"}</span>
            <span style={{
              fontSize: 11,
              color: "rgba(255,210,80,0.8)",
              background: "rgba(80,60,0,0.3)",
              border: "1px solid rgba(200,160,40,0.3)",
              padding: "2px 8px",
              borderRadius: 3,
              minWidth: 72,
              textAlign: "center",
            }}>{"\u03A6/\u03A6\u2080"} = {(flux / PHI0).toFixed(2)}</span>
          </div>
        </div>

        {/* Preset buttons */}
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          <span style={{ fontSize: 10, letterSpacing: "0.15em", color: "rgba(100,160,220,0.5)", textTransform: "uppercase" }}>Presets</span>
          <div style={{ display: "flex", gap: 6 }}>
            {presetBtn("\u03A6 = 0", 0)}
            {presetBtn("\u03A6 = \u03A6\u2080/2", 0.5)}
            {presetBtn("\u03A6 = \u03A6\u2080", 1.0)}
          </div>
        </div>

        {/* Toggles */}
        <div style={{ display: "flex", gap: 10 }}>
          <button onClick={togglePhases} style={btnStyle(showPhases)}>
            {showPhases ? "\u25C9 e-phases" : "\u25CB e-phases"}
          </button>
          <button onClick={toggleAnimate} style={btnStyle(animateElectrons)}>
            {animateElectrons ? "\u25B6 Animating" : "\u25A0 Paused"}
          </button>
        </div>

        {/* Drag hint */}
        <span style={{ fontSize: 10, color: "rgba(80,120,160,0.45)", letterSpacing: "0.08em", marginLeft: "auto" }}>
          drag left/right to adjust flux
        </span>
      </div>
    </div>
  );
}
