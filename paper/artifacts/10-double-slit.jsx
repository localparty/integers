import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(8,11,20,0.95)",
  grid: "rgba(30,50,90,0.25)",
  slit1: "#4af",             // slit 1 — blue
  slit1Glow: "rgba(40,170,255,0.25)",
  slit2: "#f55",             // slit 2 — red
  slit2Glow: "rgba(255,80,80,0.25)",
  constructive: "#c0ffa0",   // bright fringe — green
  destructive: "rgba(255,60,80,0.7)",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(90,130,175,0.45)",
  eCircle: "rgba(80,220,160,0.6)",
  barrier: "rgba(140,160,180,0.85)",
  screen: "rgba(200,220,240,0.4)",
  source: "rgba(255,220,60,0.85)",
};

function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
function lerp(a, b, t) { return a + (b - a) * t; }

export default function DoubleSlit() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });
  const dragRef = useRef({ dragging: false });

  const [slitSep, setSlitSep] = useState(50);       // slit separation d (20-100)
  const [wavelength, setWavelength] = useState(40);  // wavelength lambda (15-80)
  const [whichPath, setWhichPath] = useState(false);
  const [showEnvelope, setShowEnvelope] = useState(false);
  const [cursorY, setCursorY] = useState(0.0);       // normalized -1..1 along detector

  const resetDefaults = () => {
    setSlitSep(50);
    setWavelength(40);
    setWhichPath(false);
    setShowEnvelope(false);
    setCursorY(0.0);
  };

  // --- mouse interaction for dragging cursor on bottom panel ---
  const handleMouseDown = useCallback((e) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const sx = canvas.width / rect.width;
    const sy = canvas.height / rect.height;
    const mx = (e.clientX - rect.left) * sx;
    const my = (e.clientY - rect.top) * sy;
    const H = canvas.height;
    const bottomTop = H * 0.72;
    const bottomBot = H * 0.95;
    if (my >= bottomTop && my <= bottomBot) {
      dragRef.current.dragging = true;
      const W = canvas.width;
      const plotL = W * 0.12;
      const plotR = W * 0.88;
      const frac = clamp((mx - plotL) / (plotR - plotL), 0, 1);
      setCursorY(frac * 2 - 1);
    }
  }, []);

  const handleMouseMove = useCallback((e) => {
    if (!dragRef.current.dragging) return;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const rect = canvas.getBoundingClientRect();
    const sx = canvas.width / rect.width;
    const mx = (e.clientX - rect.left) * sx;
    const W = canvas.width;
    const plotL = W * 0.12;
    const plotR = W * 0.88;
    const frac = clamp((mx - plotL) / (plotR - plotL), 0, 1);
    setCursorY(frac * 2 - 1);
  }, []);

  const handleMouseUp = useCallback(() => { dragRef.current.dragging = false; }, []);

  // --- main draw loop ---
  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width;
    const H = canvas.height;
    const s = stateRef.current;
    const t = s.time;

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    const d = slitSep;       // slit separation in pixels
    const lam = wavelength;  // wavelength in pixels

    // ============================================================
    //  TOP PANEL — Experiment side view (y = 0..H*0.42)
    // ============================================================
    const topH = H * 0.40;
    const topCy = topH * 0.5;

    // source, barrier, screen positions (x coords)
    const srcX = W * 0.08;
    const barX = W * 0.38;
    const scrX = W * 0.82;

    // slit y-positions
    const slitHalf = d * 0.5;

    // --- background grid ---
    ctx.strokeStyle = C.grid;
    ctx.lineWidth = 0.5;
    for (let gy = 0; gy < topH; gy += 30) {
      ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
    }
    for (let gx = 0; gx < W; gx += 30) {
      ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, topH); ctx.stroke();
    }

    // --- barrier ---
    ctx.fillStyle = C.barrier;
    ctx.fillRect(barX - 3, 0, 6, topCy - slitHalf - 4);
    ctx.fillRect(barX - 3, topCy - slitHalf + 4, 6, slitHalf * 2 - 8);
    ctx.fillRect(barX - 3, topCy + slitHalf - 4 + 8, 6, topH - (topCy + slitHalf + 4));

    // slit labels
    ctx.font = "bold 10px 'Courier New'";
    ctx.fillStyle = C.slit1;
    ctx.fillText("slit 1", barX + 10, topCy - slitHalf - 2);
    ctx.fillStyle = C.slit2;
    ctx.fillText("slit 2", barX + 10, topCy + slitHalf + 12);

    // --- detector screen ---
    ctx.fillStyle = C.screen;
    ctx.fillRect(scrX, 2, 3, topH - 4);
    ctx.font = "9px 'Courier New'";
    ctx.fillStyle = C.textDim;
    ctx.fillText("detector", scrX - 8, topH - 6);

    // --- source ---
    ctx.beginPath();
    ctx.arc(srcX, topCy, 6, 0, TAU);
    ctx.fillStyle = C.source;
    ctx.fill();
    ctx.font = "9px 'Courier New'";
    ctx.fillStyle = C.source;
    ctx.fillText("source", srcX - 12, topCy + 18);

    // --- helix/wave from source to barrier ---
    ctx.beginPath();
    ctx.strokeStyle = "rgba(255,220,60,0.5)";
    ctx.lineWidth = 1.5;
    for (let px = srcX + 8; px < barX - 6; px += 1) {
      const phase = (px - srcX) / lam * TAU - t * 3;
      const yy = topCy + Math.sin(phase) * 4;
      if (px === srcX + 8) ctx.moveTo(px, yy); else ctx.lineTo(px, yy);
    }
    ctx.stroke();

    // --- wavefronts from slits ---
    const slit1Y = topCy - slitHalf;
    const slit2Y = topCy + slitHalf;
    const maxR = (scrX - barX) * 1.3;
    const waveSpeed = lam * 0.8;
    const numWaves = 12;

    for (let wi = 0; wi < numWaves; wi++) {
      const r = ((t * waveSpeed + wi * lam) % (maxR + lam));
      if (r < 2) continue;
      const fade = clamp(1 - r / maxR, 0, 0.7);

      // slit 1 wavefront
      ctx.beginPath();
      ctx.arc(barX + 4, slit1Y, r, -Math.PI * 0.48, Math.PI * 0.48);
      ctx.strokeStyle = `rgba(40,170,255,${fade * 0.55})`;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // slit 2 wavefront
      ctx.beginPath();
      ctx.arc(barX + 4, slit2Y, r, -Math.PI * 0.48, Math.PI * 0.48);
      ctx.strokeStyle = `rgba(255,80,80,${fade * 0.55})`;
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // --- interference coloring on screen ---
    for (let sy = 4; sy < topH - 4; sy += 2) {
      const dy = sy - topCy;
      const sinTheta = dy / Math.sqrt((scrX - barX) ** 2 + dy ** 2);
      const deltaPhi = (TAU / lam) * d * sinTheta;
      let intensity;
      if (whichPath) {
        // two single-slit patterns summed (no interference)
        const sinc1 = dy === 0 ? 1 : Math.sin(Math.PI * 8 * sinTheta) / (Math.PI * 8 * sinTheta);
        intensity = 0.35 + 0.3 * sinc1 * sinc1;
      } else {
        intensity = Math.cos(deltaPhi / 2) ** 2;
        if (showEnvelope) {
          const slitWidth = 8;
          const beta2 = (Math.PI / lam) * slitWidth * sinTheta;
          const sinc2 = beta2 === 0 ? 1 : Math.sin(beta2) / beta2;
          intensity *= sinc2 * sinc2;
        }
      }
      const bright = Math.round(intensity * 255);
      ctx.fillStyle = `rgb(${bright},${Math.round(bright * 0.95)},${Math.round(bright * 0.85)})`;
      ctx.fillRect(scrX, sy, 8, 2);
    }

    // --- phase indicators on wavefronts (small circles) ---
    const indicatorR = 4;
    for (let si = 0; si < 2; si++) {
      const slitY = si === 0 ? slit1Y : slit2Y;
      const col = si === 0 ? C.slit1 : C.slit2;
      const phaseR = ((t * waveSpeed + 2 * lam) % (maxR + lam));
      if (phaseR < 10 || phaseR > maxR * 0.8) continue;
      const angles = [-0.3, 0, 0.3];
      for (const ang of angles) {
        const ix = barX + 4 + Math.cos(ang) * phaseR;
        const iy = slitY + Math.sin(ang) * phaseR;
        if (ix < barX + 10 || ix > scrX - 10) continue;
        const phase = (phaseR / lam) * TAU - t * 3;
        ctx.beginPath();
        ctx.arc(ix, iy, indicatorR + 1, 0, TAU);
        ctx.fillStyle = C.bg;
        ctx.fill();
        ctx.beginPath();
        ctx.arc(ix, iy, indicatorR, 0, TAU);
        ctx.strokeStyle = col;
        ctx.lineWidth = 1;
        ctx.stroke();
        // phase hand
        ctx.beginPath();
        ctx.moveTo(ix, iy);
        ctx.lineTo(ix + Math.cos(phase) * indicatorR, iy - Math.sin(phase) * indicatorR);
        ctx.strokeStyle = col;
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }

    // --- cursor line on detector (from bottom panel cursorY) ---
    const cursorScreenY = topCy + cursorY * (topH * 0.42);
    ctx.beginPath();
    ctx.moveTo(scrX - 4, cursorScreenY);
    ctx.lineTo(scrX + 14, cursorScreenY);
    ctx.strokeStyle = C.constructive;
    ctx.lineWidth = 2;
    ctx.setLineDash([4, 3]);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.constructive;
    ctx.beginPath();
    ctx.moveTo(scrX + 14, cursorScreenY - 4);
    ctx.lineTo(scrX + 20, cursorScreenY);
    ctx.lineTo(scrX + 14, cursorScreenY + 4);
    ctx.fill();

    // --- panel separator ---
    ctx.beginPath();
    ctx.moveTo(0, topH + 1);
    ctx.lineTo(W, topH + 1);
    ctx.strokeStyle = "rgba(40,80,140,0.25)";
    ctx.lineWidth = 1;
    ctx.stroke();

    // ============================================================
    //  MIDDLE PANEL — E-circle view (y = topH+2 .. H*0.70)
    // ============================================================
    const midTop = topH + 2;
    const midH = H * 0.30;
    const midBot = midTop + midH;
    const eCircR = midH * 0.32;
    const eCx = W * 0.25;
    const eCy = midTop + midH * 0.52;

    // compute phase difference at cursor position
    const cursorDy = cursorY * (topH * 0.42);
    const sinTheta = cursorDy / Math.sqrt((scrX - barX) ** 2 + cursorDy ** 2);
    const deltaPhi = (TAU / lam) * d * sinTheta;

    // phase of slit 1 at cursor
    const dist1 = Math.sqrt((scrX - barX) ** 2 + (cursorDy + slitHalf) ** 2);
    const dist2 = Math.sqrt((scrX - barX) ** 2 + (cursorDy - slitHalf) ** 2);
    const phi1 = (dist1 / lam) * TAU - t * 3;
    const phi2 = (dist2 / lam) * TAU - t * 3;

    // background
    ctx.fillStyle = "rgba(6,9,16,0.8)";
    ctx.fillRect(0, midTop, W, midH);

    // e-circle
    ctx.beginPath();
    ctx.arc(eCx, eCy, eCircR, 0, TAU);
    ctx.strokeStyle = C.eCircle;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // label
    ctx.font = "bold 11px 'Courier New'";
    ctx.fillStyle = C.eCircle;
    ctx.fillText("e-circle", eCx - 25, midTop + 14);
    ctx.font = "9px 'Courier New'";
    ctx.fillStyle = C.textDim;
    ctx.fillText("(extra-dimension phase)", eCx - 60, midTop + 26);

    // arc between dots showing phase difference
    let dispPhi1, dispPhi2;
    if (whichPath) {
      // random scrambled phases
      dispPhi1 = t * 7.3 + Math.sin(t * 3.1) * 2;
      dispPhi2 = t * 4.7 + Math.cos(t * 2.3) * 3;
    } else {
      dispPhi1 = phi1;
      dispPhi2 = phi2;
    }

    // draw arc from phi1 to phi2
    const arcStart = -dispPhi1;
    const arcEnd = -dispPhi2;
    ctx.beginPath();
    ctx.arc(eCx, eCy, eCircR + 6, arcStart, arcEnd, arcEnd < arcStart);
    ctx.strokeStyle = "rgba(200,220,160,0.4)";
    ctx.lineWidth = 3;
    ctx.stroke();

    // delta-phi label on arc
    const arcMid = (arcStart + arcEnd) / 2;
    const labelR = eCircR + 18;
    ctx.font = "10px 'Courier New'";
    ctx.fillStyle = "rgba(200,220,160,0.7)";
    ctx.fillText("\u0394\u03C6", eCx + Math.cos(arcMid) * labelR - 6, eCy + Math.sin(arcMid) * labelR + 4);

    // slit 1 dot (blue)
    const d1x = eCx + Math.cos(-dispPhi1) * eCircR;
    const d1y = eCy + Math.sin(-dispPhi1) * eCircR;
    ctx.beginPath(); ctx.arc(d1x, d1y, 5, 0, TAU);
    ctx.fillStyle = C.slit1; ctx.fill();
    ctx.font = "9px 'Courier New'"; ctx.fillStyle = C.slit1;
    ctx.fillText("1", d1x + 8, d1y + 3);

    // slit 2 dot (red)
    const d2x = eCx + Math.cos(-dispPhi2) * eCircR;
    const d2y = eCy + Math.sin(-dispPhi2) * eCircR;
    ctx.beginPath(); ctx.arc(d2x, d2y, 5, 0, TAU);
    ctx.fillStyle = C.slit2; ctx.fill();
    ctx.font = "9px 'Courier New'"; ctx.fillStyle = C.slit2;
    ctx.fillText("2", d2x + 8, d2y + 3);

    // --- label: constructive / destructive ---
    const absDelta = Math.abs(((deltaPhi % TAU) + TAU) % TAU);
    const nearZero = absDelta < 0.5 || absDelta > TAU - 0.5;
    const nearPi = Math.abs(absDelta - Math.PI) < 0.5;
    const cosHalf = Math.cos(deltaPhi / 2);
    const intensityAtCursor = whichPath ? 0.5 : cosHalf * cosHalf;

    const textX = W * 0.46;
    ctx.font = "bold 12px 'Courier New'";
    if (whichPath) {
      ctx.fillStyle = "rgba(255,160,40,0.8)";
      ctx.fillText("DECOHERED — no fixed phase relationship", textX, midTop + 24);
      ctx.font = "10px 'Courier New'";
      ctx.fillStyle = "rgba(255,160,40,0.55)";
      const lines = [
        "Which-path measurement entangles the",
        "particle's e-coordinate with the detector,",
        "scrambling the phase relationship.",
        "Interference destroyed.",
      ];
      lines.forEach((ln, i) => ctx.fillText(ln, textX, midTop + 44 + i * 15));
    } else {
      if (nearZero) {
        ctx.fillStyle = C.constructive;
        ctx.fillText("Constructive \u2014 bright fringe", textX, midTop + 24);
        ctx.font = "10px 'Courier New'";
        ctx.fillStyle = "rgba(192,255,160,0.5)";
        ctx.fillText("e-phases match: dots overlap on e-circle", textX, midTop + 40);
      } else if (nearPi) {
        ctx.fillStyle = C.destructive;
        ctx.fillText("Destructive \u2014 dark fringe", textX, midTop + 24);
        ctx.font = "10px 'Courier New'";
        ctx.fillStyle = "rgba(255,80,80,0.5)";
        ctx.fillText("e-values differ by \u03C0: dots antipodal", textX, midTop + 40);
      } else {
        ctx.fillStyle = C.text;
        ctx.fillText("Partial interference", textX, midTop + 24);
        ctx.font = "10px 'Courier New'";
        ctx.fillStyle = C.textDim;
        ctx.fillText("e-phase difference between 0 and \u03C0", textX, midTop + 40);
      }

      // phase difference readout
      ctx.font = "10px 'Courier New'";
      ctx.fillStyle = "rgba(170,210,240,0.6)";
      const dPhiVal = deltaPhi.toFixed(3);
      const dPhiPi = (deltaPhi / Math.PI).toFixed(2);
      ctx.fillText(`Phase difference at cursor: \u0394\u03C6 = (2\u03C0/\u03BB)\u00B7d\u00B7sin\u03B8 = ${dPhiVal} rad (${dPhiPi}\u03C0)`, textX, midTop + 62);
      ctx.fillText(`I(y) = I\u2080 cos\u00B2(\u03C0d sin\u03B8/\u03BB) = ${intensityAtCursor.toFixed(3)}`, textX, midTop + 78);
    }

    // --- annotation text ---
    ctx.font = "10px 'Courier New'";
    ctx.fillStyle = C.textDim;
    const annLines = [
      "Interference is the geometric overlap of a single",
      "particle's e-structure arriving via two paths.",
      "Bright fringes: same e-coordinate.",
      "Dark fringes: antipodal e-coordinates.",
    ];
    annLines.forEach((ln, i) => ctx.fillText(ln, textX, midBot - 52 + i * 14));

    // --- panel separator ---
    ctx.beginPath();
    ctx.moveTo(0, midBot);
    ctx.lineTo(W, midBot);
    ctx.strokeStyle = "rgba(40,80,140,0.25)";
    ctx.lineWidth = 1;
    ctx.stroke();

    // ============================================================
    //  BOTTOM PANEL — Interference pattern (y = midBot .. H*0.96)
    // ============================================================
    const botTop = midBot + 2;
    const botH = H * 0.24;
    const plotL = W * 0.12;
    const plotR = W * 0.88;
    const plotW = plotR - plotL;
    const plotCy = botTop + botH * 0.52;
    const plotAmp = botH * 0.38;

    // label
    ctx.font = "bold 11px 'Courier New'";
    ctx.fillStyle = "rgba(170,210,240,0.6)";
    ctx.fillText("Intensity pattern  I(y)", plotL, botTop + 12);
    ctx.font = "9px 'Courier New'";
    ctx.fillStyle = C.textDim;
    ctx.fillText("drag cursor \u2190\u2192", plotR - 80, botTop + 12);

    // axes
    ctx.beginPath();
    ctx.moveTo(plotL, plotCy + plotAmp + 6);
    ctx.lineTo(plotR, plotCy + plotAmp + 6);
    ctx.strokeStyle = "rgba(100,140,190,0.3)";
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.font = "9px 'Courier New'";
    ctx.fillStyle = C.textDim;
    ctx.fillText("detector position y", plotL + plotW * 0.35, plotCy + plotAmp + 18);

    // center mark
    ctx.beginPath();
    ctx.moveTo(plotL + plotW / 2, plotCy - plotAmp - 4);
    ctx.lineTo(plotL + plotW / 2, plotCy + plotAmp + 6);
    ctx.strokeStyle = "rgba(100,140,190,0.15)";
    ctx.lineWidth = 1;
    ctx.setLineDash([3, 3]);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillText("0", plotL + plotW / 2 - 3, plotCy + plotAmp + 18);

    // intensity curve
    ctx.beginPath();
    let started = false;
    for (let px = 0; px <= plotW; px++) {
      const yNorm = (px / plotW) * 2 - 1;  // -1..1
      const sinT = yNorm * 0.6;
      const dPhi = (TAU / lam) * d * sinT;
      let intens;
      if (whichPath) {
        const sinc1 = sinT === 0 ? 1 : Math.sin(Math.PI * 8 * sinT) / (Math.PI * 8 * sinT);
        intens = 0.3 + 0.25 * sinc1 * sinc1;
      } else {
        intens = Math.cos(dPhi / 2) ** 2;
        if (showEnvelope) {
          const slitWidth = 8;
          const b2 = (Math.PI / lam) * slitWidth * sinT;
          const sinc2 = b2 === 0 ? 1 : Math.sin(b2) / b2;
          intens *= sinc2 * sinc2;
        }
      }
      const py = plotCy + plotAmp - intens * plotAmp * 2;
      if (!started) { ctx.moveTo(plotL + px, py); started = true; }
      else ctx.lineTo(plotL + px, py);
    }
    ctx.strokeStyle = whichPath ? "rgba(255,160,40,0.7)" : "rgba(160,220,255,0.85)";
    ctx.lineWidth = 2;
    ctx.stroke();

    // fill under curve with glow
    ctx.lineTo(plotR, plotCy + plotAmp);
    ctx.lineTo(plotL, plotCy + plotAmp);
    ctx.closePath();
    ctx.fillStyle = whichPath ? "rgba(255,160,40,0.06)" : "rgba(80,180,255,0.08)";
    ctx.fill();

    // single-slit envelope overlay
    if (showEnvelope && !whichPath) {
      ctx.beginPath();
      started = false;
      for (let px = 0; px <= plotW; px++) {
        const yNorm = (px / plotW) * 2 - 1;
        const sinT = yNorm * 0.6;
        const slitWidth = 8;
        const b2 = (Math.PI / lam) * slitWidth * sinT;
        const sinc2 = b2 === 0 ? 1 : Math.sin(b2) / b2;
        const env = sinc2 * sinc2;
        const py = plotCy + plotAmp - env * plotAmp * 2;
        if (!started) { ctx.moveTo(plotL + px, py); started = true; }
        else ctx.lineTo(plotL + px, py);
      }
      ctx.strokeStyle = "rgba(255,220,60,0.4)";
      ctx.lineWidth = 1.5;
      ctx.setLineDash([6, 4]);
      ctx.stroke();
      ctx.setLineDash([]);
      // label
      ctx.font = "9px 'Courier New'";
      ctx.fillStyle = "rgba(255,220,60,0.5)";
      ctx.fillText("sinc\u00B2 envelope", plotR - 100, botTop + 24);
    }

    // fringe labels (bright/dark marks)
    const numFringes = 6;
    for (let fi = -numFringes; fi <= numFringes; fi++) {
      // bright fringe at sin theta = fi * lambda / d
      const sinT = (fi * lam) / d;
      if (Math.abs(sinT) > 0.6) continue;
      const yNorm = sinT / 0.6;
      const px = plotL + (yNorm + 1) * 0.5 * plotW;
      ctx.beginPath();
      ctx.moveTo(px, plotCy + plotAmp + 6);
      ctx.lineTo(px, plotCy + plotAmp + 11);
      ctx.strokeStyle = whichPath ? "rgba(255,160,40,0.3)" : "rgba(160,255,200,0.4)";
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    // --- cursor on pattern ---
    const cursorPx = plotL + (cursorY + 1) * 0.5 * plotW;
    ctx.beginPath();
    ctx.moveTo(cursorPx, botTop + 18);
    ctx.lineTo(cursorPx, plotCy + plotAmp + 6);
    ctx.strokeStyle = "rgba(192,255,160,0.7)";
    ctx.lineWidth = 1.5;
    ctx.stroke();
    // cursor handle
    ctx.beginPath();
    ctx.arc(cursorPx, botTop + 22, 5, 0, TAU);
    ctx.fillStyle = C.constructive;
    ctx.fill();

    // cursor intensity readout
    const curSinT = cursorY * 0.6;
    const curDPhi = (TAU / lam) * d * curSinT;
    let curInt;
    if (whichPath) {
      const s2 = curSinT === 0 ? 1 : Math.sin(Math.PI * 8 * curSinT) / (Math.PI * 8 * curSinT);
      curInt = 0.3 + 0.25 * s2 * s2;
    } else {
      curInt = Math.cos(curDPhi / 2) ** 2;
      if (showEnvelope) {
        const b2 = (Math.PI / lam) * 8 * curSinT;
        const sinc2 = b2 === 0 ? 1 : Math.sin(b2) / b2;
        curInt *= sinc2 * sinc2;
      }
    }
    // intensity dot on curve
    const curDotY = plotCy + plotAmp - curInt * plotAmp * 2;
    ctx.beginPath();
    ctx.arc(cursorPx, curDotY, 4, 0, TAU);
    ctx.fillStyle = C.constructive;
    ctx.fill();
    ctx.beginPath();
    ctx.arc(cursorPx, curDotY, 7, 0, TAU);
    ctx.strokeStyle = "rgba(192,255,160,0.4)";
    ctx.lineWidth = 1;
    ctx.stroke();

    // advance time
    s.time += 0.016;
    animRef.current = requestAnimationFrame(draw);
  }, [slitSep, wavelength, whichPath, showEnvelope, cursorY]);

  // --- lifecycle ---
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const resize = () => { canvas.width = canvas.offsetWidth; canvas.height = canvas.offsetHeight; };
    resize();
    window.addEventListener("resize", resize);
    animRef.current = requestAnimationFrame(draw);
    return () => { cancelAnimationFrame(animRef.current); window.removeEventListener("resize", resize); };
  }, [draw]);

  useEffect(() => {
    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("mouseup", handleMouseUp);
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
    };
  }, [handleMouseMove, handleMouseUp]);

  // --- styles ---
  const label = {
    fontSize: 10, letterSpacing: "0.14em", color: "rgba(90,140,190,0.5)",
    textTransform: "uppercase", fontFamily: "'Courier New', monospace",
    display: "block", marginBottom: 5,
  };
  const btn = (active, col) => ({
    padding: "5px 13px", fontSize: 11, letterSpacing: "0.06em",
    fontFamily: "'Courier New', monospace",
    background: active ? `rgba(${col},0.18)` : "rgba(16,28,52,0.6)",
    border: `1px solid ${active ? `rgba(${col},0.55)` : "rgba(40,80,140,0.22)"}`,
    color: active ? `rgba(${col},1)` : "rgba(110,150,195,0.5)",
    borderRadius: 3, cursor: "pointer",
  });
  const sliderBox = {
    display: "flex", alignItems: "center", gap: 8,
  };

  return (
    <div style={{
      background: C.bg, minHeight: "100vh", display: "flex", flexDirection: "column",
      fontFamily: "'Courier New', monospace", color: C.text, userSelect: "none",
    }}>
      {/* header */}
      <div style={{
        padding: "15px 26px 9px",
        borderBottom: "1px solid rgba(40,80,140,0.18)",
        display: "flex", alignItems: "baseline", gap: 14,
      }}>
        <span style={{ fontSize: 11, letterSpacing: "0.18em", color: "rgba(80,220,160,0.4)", textTransform: "uppercase" }}>
          Quantum Geometry in 5D
        </span>
        <span style={{ color: "rgba(60,100,160,0.3)" }}>|</span>
        <span style={{ fontSize: 13, color: "rgba(190,215,240,0.65)", letterSpacing: "0.05em" }}>
          Visualization 10 — Double-Slit Interference as e-Phase Overlap
        </span>
      </div>

      {/* canvas */}
      <canvas
        ref={canvasRef}
        style={{ flex: 1, width: "100%", display: "block" }}
        onMouseDown={handleMouseDown}
      />

      {/* control panel */}
      <div style={{
        padding: "13px 26px 17px",
        borderTop: "1px solid rgba(40,80,140,0.15)",
        display: "flex", flexWrap: "wrap", gap: "15px 32px",
        alignItems: "flex-start", background: "rgba(6,8,16,0.97)",
      }}>
        {/* slit separation */}
        <div>
          <span style={label}>Slit separation d</span>
          <div style={sliderBox}>
            <input type="range" min={20} max={100} step={1} value={slitSep}
              onChange={e => setSlitSep(Number(e.target.value))}
              style={{ width: 140, cursor: "pointer", accentColor: "#4af" }} />
            <span style={{
              fontSize: 11, color: "rgba(180,210,240,0.6)",
              background: "rgba(20,35,60,0.5)", border: "1px solid rgba(60,100,160,0.25)",
              padding: "2px 8px", borderRadius: 3, minWidth: 30, textAlign: "center",
            }}>{slitSep}</span>
          </div>
        </div>

        {/* wavelength */}
        <div>
          <span style={label}>Wavelength {"\u03BB"}</span>
          <div style={sliderBox}>
            <input type="range" min={15} max={80} step={1} value={wavelength}
              onChange={e => setWavelength(Number(e.target.value))}
              style={{ width: 140, cursor: "pointer", accentColor: "#f55" }} />
            <span style={{
              fontSize: 11, color: "rgba(180,210,240,0.6)",
              background: "rgba(20,35,60,0.5)", border: "1px solid rgba(60,100,160,0.25)",
              padding: "2px 8px", borderRadius: 3, minWidth: 30, textAlign: "center",
            }}>{wavelength}</span>
          </div>
        </div>

        {/* which-path toggle */}
        <div>
          <span style={label}>Which-path detector</span>
          <div style={{ display: "flex", gap: 8 }}>
            <button onClick={() => setWhichPath(false)}
              style={btn(!whichPath, "80,220,160")}>OFF</button>
            <button onClick={() => setWhichPath(true)}
              style={btn(whichPath, "255,160,40")}>ON</button>
          </div>
        </div>

        {/* envelope toggle */}
        <div>
          <span style={label}>Single-slit envelope</span>
          <div style={{ display: "flex", gap: 8 }}>
            <button onClick={() => setShowEnvelope(!showEnvelope)}
              style={btn(showEnvelope, "255,220,60")}>
              {showEnvelope ? "Showing" : "Hidden"}
            </button>
          </div>
        </div>

        {/* reset */}
        <div>
          <span style={label}>Defaults</span>
          <button onClick={resetDefaults} style={btn(false, "120,160,220")}>
            {"\u21BA"} Reset
          </button>
        </div>

        <span style={{
          fontSize: 10, color: "rgba(60,100,150,0.4)", letterSpacing: "0.07em",
          marginLeft: "auto", alignSelf: "flex-end", paddingBottom: 2,
        }}>
          blue = slit 1 path {"\u00B7"} red = slit 2 path {"\u00B7"} green = e-circle phase
        </span>
      </div>
    </div>
  );
}
