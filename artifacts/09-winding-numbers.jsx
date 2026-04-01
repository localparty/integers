import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  bgPanel: "#0a0e16",
  grid: "rgba(40,60,100,0.30)",
  cylinder: "rgba(60,100,160,0.12)",
  cylinderEdge: "rgba(80,130,200,0.25)",
  helixInt: "#30e870",
  helixHalf: "#40a0ff",
  helixForbid: "#ff4040",
  gapMark: "#ff6060",
  eCircle: "rgba(180,80,255,0.6)",
  eCircleDim: "rgba(180,80,255,0.15)",
  dot: "#f0d040",
  dotGlow: "rgba(240,210,60,0.3)",
  antipode: "#40a0ff",
  checkMark: "#30e870",
  crossMark: "#ff4040",
  text: "rgba(180,210,240,0.75)",
  textDim: "rgba(100,140,180,0.45)",
  textBright: "rgba(220,235,255,0.9)",
  accent: "#f0a030",
  axis: "rgba(80,180,255,0.5)",
};

const WINDINGS = [
  { n: 0,     label: "n=0",   type: "integer" },
  { n: 0.5,   label: "n=1/2", type: "half" },
  { n: 1,     label: "n=1",   type: "integer" },
  { n: 1.5,   label: "n=3/2", type: "half" },
  { n: 2,     label: "n=2",   type: "integer" },
  { n: 1/3,   label: "n=1/3", type: "forbidden" },
];

// 3D projection helpers — match reference style
function rotY(x, y, z, a) {
  const c = Math.cos(a), s = Math.sin(a);
  return [x * c + z * s, y, -x * s + z * c];
}
function rotX(x, y, z, a) {
  const c = Math.cos(a), s = Math.sin(a);
  return [x, y * c - z * s, y * s + z * c];
}
function project(x, y, z, cx, cy, scale) {
  const persp = 600 / (600 + z);
  return [cx + x * scale * persp, cy - y * scale * persp, persp];
}

export default function WindingNumbers() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0, dragX: 0, dragY: 0, dragging: false, lastMx: 0, lastMy: 0 });
  const rotRef = useRef({ rx: 0.3, ry: -0.4 });

  const [winding, setWinding] = useState(1);
  const [autoRotate, setAutoRotate] = useState(true);
  const [show4pi, setShow4pi] = useState(false);
  const [showTable, setShowTable] = useState(false);

  const selected = WINDINGS.find(w => w.n === winding) || WINDINGS[2];
  const helixColor = selected.type === "integer" ? C.helixInt
    : selected.type === "half" ? C.helixHalf : C.helixForbid;

  // Mouse drag for 3D rotation
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const onDown = (e) => {
      const s = stateRef.current;
      s.dragging = true;
      s.lastMx = e.clientX;
      s.lastMy = e.clientY;
    };
    const onMove = (e) => {
      const s = stateRef.current;
      if (!s.dragging) return;
      const dx = e.clientX - s.lastMx;
      const dy = e.clientY - s.lastMy;
      rotRef.current.ry += dx * 0.005;
      rotRef.current.rx += dy * 0.005;
      rotRef.current.rx = Math.max(-1.2, Math.min(1.2, rotRef.current.rx));
      s.lastMx = e.clientX;
      s.lastMy = e.clientY;
    };
    const onUp = () => { stateRef.current.dragging = false; };
    canvas.addEventListener("mousedown", onDown);
    window.addEventListener("mousemove", onMove);
    window.addEventListener("mouseup", onUp);
    return () => {
      canvas.removeEventListener("mousedown", onDown);
      window.removeEventListener("mousemove", onMove);
      window.removeEventListener("mouseup", onUp);
    };
  }, []);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const s = stateRef.current;
    const rot = rotRef.current;

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    if (autoRotate && !s.dragging) {
      rot.ry += 0.003;
    }

    // Layout: main 3D view left 58%, e-circle right 22%, gap for panels
    const mainW = W * 0.58;
    const rightX = mainW + 16;
    const rightW = W * 0.22;
    const bottomY = H - 100;

    // ========== MAIN 3D VIEW — helix on cylinder ==========
    const cx = mainW * 0.5;
    const cy = H * 0.42;
    const cylR = Math.min(mainW, H) * 0.15;  // cylinder radius in 3D units
    const cylLen = Math.min(mainW, H) * 0.42; // cylinder half-length
    const sc = 1.0;

    // Determine how many periods to draw
    const periods = show4pi ? 2 : 1;
    const n = selected.n;
    const totalAngle = TAU * n * periods;  // total winding angle
    const steps = Math.max(200, Math.round(Math.abs(totalAngle) * 30 + 60));

    // Draw cylinder wireframe
    const cylSteps = 24;
    const axSteps = 8;
    ctx.lineWidth = 0.6;

    // Cylinder rings
    for (let ai = 0; ai <= axSteps; ai++) {
      const axFrac = ai / axSteps;
      const axPos = -cylLen + axFrac * 2 * cylLen;
      ctx.beginPath();
      let first = true;
      for (let ci = 0; ci <= cylSteps; ci++) {
        const theta = (ci / cylSteps) * TAU;
        let px3 = Math.cos(theta) * cylR;
        let py3 = Math.sin(theta) * cylR;
        let pz3 = axPos;
        [px3, py3, pz3] = rotX(px3, py3, pz3, rot.rx);
        [px3, py3, pz3] = rotY(px3, py3, pz3, rot.ry);
        const [sx, sy] = project(px3, py3, pz3, cx, cy, sc);
        if (first) { ctx.moveTo(sx, sy); first = false; }
        else ctx.lineTo(sx, sy);
      }
      ctx.strokeStyle = C.cylinder;
      ctx.stroke();
    }
    // Cylinder axis lines
    for (let ci = 0; ci < cylSteps; ci += 4) {
      const theta = (ci / cylSteps) * TAU;
      ctx.beginPath();
      for (let ai = 0; ai <= 1; ai++) {
        const axPos = -cylLen + ai * 2 * cylLen;
        let px3 = Math.cos(theta) * cylR;
        let py3 = Math.sin(theta) * cylR;
        let pz3 = axPos;
        [px3, py3, pz3] = rotX(px3, py3, pz3, rot.rx);
        [px3, py3, pz3] = rotY(px3, py3, pz3, rot.ry);
        const [sx, sy] = project(px3, py3, pz3, cx, cy, sc);
        if (ai === 0) ctx.moveTo(sx, sy);
        else ctx.lineTo(sx, sy);
      }
      ctx.strokeStyle = C.cylinder;
      ctx.stroke();
    }

    // Central axis arrow
    for (let end = 0; end <= 1; end++) {
      let ax = 0, ay = 0, az = (end === 0 ? -cylLen * 1.25 : cylLen * 1.25);
      [ax, ay, az] = rotX(ax, ay, az, rot.rx);
      [ax, ay, az] = rotY(ax, ay, az, rot.ry);
      const [sx, sy] = project(ax, ay, az, cx, cy, sc);
      if (end === 1) {
        ctx.beginPath();
        ctx.arc(sx, sy, 3, 0, TAU);
        ctx.fillStyle = C.axis;
        ctx.fill();
        ctx.fillStyle = C.axis;
        ctx.font = "bold 11px 'Courier New'";
        ctx.fillText("x (spatial)", sx + 8, sy + 4);
      }
    }

    // ---- Draw the helix ----
    if (n !== 0) {
      // Collect helix points for depth sorting
      const pts = [];
      for (let i = 0; i <= steps; i++) {
        const frac = i / steps;
        const axPos = -cylLen + frac * 2 * cylLen;
        const angle = frac * totalAngle;
        let px3 = Math.cos(angle) * cylR;
        let py3 = Math.sin(angle) * cylR;
        let pz3 = axPos;
        [px3, py3, pz3] = rotX(px3, py3, pz3, rot.rx);
        [px3, py3, pz3] = rotY(px3, py3, pz3, rot.ry);
        const [sx, sy, persp] = project(px3, py3, pz3, cx, cy, sc);
        pts.push({ sx, sy, persp, pz3 });
      }

      // Glow pass
      ctx.lineWidth = 6;
      for (let i = 0; i < pts.length - 1; i++) {
        const a = pts[i], b = pts[i + 1];
        const alpha = ((a.persp + b.persp) / 2) * 0.15;
        ctx.beginPath();
        ctx.moveTo(a.sx, a.sy);
        ctx.lineTo(b.sx, b.sy);
        ctx.strokeStyle = helixColor;
        ctx.globalAlpha = alpha;
        ctx.stroke();
      }
      ctx.globalAlpha = 1;

      // Main line pass
      ctx.lineWidth = 2.5;
      for (let i = 0; i < pts.length - 1; i++) {
        const a = pts[i], b = pts[i + 1];
        const depth = (a.persp + b.persp) / 2;
        const alpha = 0.25 + 0.75 * depth;
        ctx.beginPath();
        ctx.moveTo(a.sx, a.sy);
        ctx.lineTo(b.sx, b.sy);
        ctx.strokeStyle = helixColor;
        ctx.globalAlpha = alpha;
        ctx.stroke();
      }
      ctx.globalAlpha = 1;

      // Start and end markers
      const pStart = pts[0];
      const pEnd = pts[pts.length - 1];

      // Start dot (bright)
      ctx.beginPath();
      ctx.arc(pStart.sx, pStart.sy, 6, 0, TAU);
      ctx.fillStyle = C.dot;
      ctx.fill();
      ctx.beginPath();
      ctx.arc(pStart.sx, pStart.sy, 12, 0, TAU);
      const grd = ctx.createRadialGradient(pStart.sx, pStart.sy, 0, pStart.sx, pStart.sy, 12);
      grd.addColorStop(0, C.dotGlow);
      grd.addColorStop(1, "transparent");
      ctx.fillStyle = grd;
      ctx.fill();

      // End dot
      ctx.beginPath();
      ctx.arc(pEnd.sx, pEnd.sy, 5, 0, TAU);
      ctx.fillStyle = selected.type === "forbidden" ? C.helixForbid : helixColor;
      ctx.fill();

      // If forbidden: draw the gap
      if (selected.type === "forbidden") {
        ctx.beginPath();
        ctx.setLineDash([4, 4]);
        ctx.moveTo(pEnd.sx, pEnd.sy);
        ctx.lineTo(pStart.sx, pStart.sy);
        ctx.strokeStyle = "rgba(255,60,60,0.5)";
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.setLineDash([]);

        // Gap X mark
        const midGx = (pEnd.sx + pStart.sx) / 2;
        const midGy = (pEnd.sy + pStart.sy) / 2;
        ctx.font = "bold 18px 'Courier New'";
        ctx.fillStyle = C.crossMark;
        ctx.fillText("\u2717", midGx - 6, midGy + 6);
      }
    } else {
      // n=0: just a straight line along the axis
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      let a0 = [0, 0, -cylLen], a1 = [0, 0, cylLen];
      a0 = rotX(...a0, rot.rx); a0 = rotY(...a0, rot.ry);
      a1 = rotX(...a1, rot.rx); a1 = rotY(...a1, rot.ry);
      const [sx0, sy0] = project(...a0, cx, cy, sc);
      const [sx1, sy1] = project(...a1, cx, cy, sc);
      ctx.moveTo(sx0, sy0);
      ctx.lineTo(sx1, sy1);
      ctx.strokeStyle = C.helixInt;
      ctx.stroke();
      ctx.beginPath(); ctx.arc(sx0, sy0, 5, 0, TAU);
      ctx.fillStyle = C.dot; ctx.fill();
      ctx.beginPath(); ctx.arc(sx1, sy1, 5, 0, TAU);
      ctx.fillStyle = C.helixInt; ctx.fill();
    }

    // Label on main view
    ctx.fillStyle = "rgba(100,140,180,0.35)";
    ctx.font = "10px 'Courier New'";
    ctx.fillText("drag to rotate", 16, H * 0.82 - 18);
    ctx.fillText(show4pi ? "showing 4\u03C0 (two spatial periods)" : "showing 2\u03C0 (one spatial period)", 16, H * 0.82);

    // ========== RIGHT PANEL — e-circle closeup ==========
    const eCx = rightX + rightW * 0.5;
    const eCy = H * 0.32;
    const eR = Math.min(rightW * 0.38, H * 0.16);

    // Panel background
    ctx.fillStyle = "rgba(10,14,22,0.85)";
    ctx.fillRect(rightX - 8, 8, rightW + 16, H * 0.68);
    ctx.strokeStyle = "rgba(40,80,140,0.2)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(rightX - 8, 8);
    ctx.lineTo(rightX - 8, H * 0.68 + 8);
    ctx.stroke();

    // Panel title
    ctx.fillStyle = "rgba(180,80,255,0.8)";
    ctx.font = "bold 12px 'Courier New'";
    ctx.fillText("e-CIRCLE", rightX, 30);
    ctx.fillStyle = C.textDim;
    ctx.font = "10px 'Courier New'";
    ctx.fillText("extra dimension", rightX, 46);

    // Draw the e-circle
    ctx.beginPath();
    ctx.arc(eCx, eCy, eR, 0, TAU);
    ctx.strokeStyle = C.eCircle;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Tick marks every 1/6 of circle
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * TAU - Math.PI / 2;
      const inner = eR - 4, outer = eR + 4;
      ctx.beginPath();
      ctx.moveTo(eCx + Math.cos(a) * inner, eCy + Math.sin(a) * inner);
      ctx.lineTo(eCx + Math.cos(a) * outer, eCy + Math.sin(a) * outer);
      ctx.strokeStyle = C.eCircleDim;
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    // Starting position (top of circle)
    const startAngle = -Math.PI / 2;
    const startDx = eCx + Math.cos(startAngle) * eR;
    const startDy = eCy + Math.sin(startAngle) * eR;

    ctx.beginPath();
    ctx.arc(startDx, startDy, 6, 0, TAU);
    ctx.fillStyle = C.dot;
    ctx.fill();
    ctx.fillStyle = C.dot;
    ctx.font = "bold 10px 'Courier New'";
    ctx.fillText("START", startDx + 10, startDy + 4);

    // Show antipodal point for reference
    const antiAngle = startAngle + Math.PI;
    const antiDx = eCx + Math.cos(antiAngle) * eR;
    const antiDy = eCy + Math.sin(antiAngle) * eR;
    ctx.beginPath();
    ctx.setLineDash([2, 3]);
    ctx.arc(antiDx, antiDy, 5, 0, TAU);
    ctx.strokeStyle = C.antipode;
    ctx.lineWidth = 1.2;
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = C.antipode;
    ctx.font = "9px 'Courier New'";
    ctx.fillText("antipode", antiDx + 9, antiDy + 3);

    // Animate the dot moving around e-circle based on winding
    const animPhase = show4pi ? (s.time * 0.4) % 1 : (s.time * 0.5) % 1;
    const travelAngle = animPhase * TAU * n * periods;
    const dotAngle = startAngle + travelAngle;
    const dotEx = eCx + Math.cos(dotAngle) * eR;
    const dotEy = eCy + Math.sin(dotAngle) * eR;

    // Draw the arc swept so far
    if (n !== 0) {
      ctx.beginPath();
      ctx.arc(eCx, eCy, eR - 10, startAngle, dotAngle, false);
      ctx.strokeStyle = helixColor;
      ctx.lineWidth = 3;
      ctx.globalAlpha = 0.4;
      ctx.stroke();
      ctx.globalAlpha = 1;
    }

    // Moving dot
    ctx.beginPath();
    ctx.arc(dotEx, dotEy, 5, 0, TAU);
    ctx.fillStyle = helixColor;
    ctx.fill();
    const glowCol = selected.type === "integer" ? "rgba(48,232,112,0.3)"
      : selected.type === "half" ? "rgba(64,160,255,0.3)" : "rgba(255,64,64,0.3)";
    const grd2 = ctx.createRadialGradient(dotEx, dotEy, 0, dotEx, dotEy, 14);
    grd2.addColorStop(0, glowCol);
    grd2.addColorStop(1, "transparent");
    ctx.beginPath();
    ctx.arc(dotEx, dotEy, 14, 0, TAU);
    ctx.fillStyle = grd2;
    ctx.fill();

    // End position after full period(s) - static marker
    const endTravelAngle = TAU * n * periods;
    const endAngle = startAngle + endTravelAngle;
    const endEx = eCx + Math.cos(endAngle) * eR;
    const endEy = eCy + Math.sin(endAngle) * eR;

    // Fractional position around circle
    const fracAround = (n * periods) % 1;
    const closesAtStart = Math.abs(fracAround) < 0.001 || Math.abs(fracAround - 1) < 0.001;
    const closesAtAnti = Math.abs(fracAround - 0.5) < 0.001;
    const closes = closesAtStart || closesAtAnti;

    // End position indicator
    if (n !== 0) {
      ctx.beginPath();
      ctx.arc(endEx, endEy, 8, 0, TAU);
      ctx.strokeStyle = closes ? C.checkMark : C.crossMark;
      ctx.lineWidth = 2;
      ctx.stroke();

      // Check or X
      ctx.font = "bold 16px 'Courier New'";
      if (closes) {
        ctx.fillStyle = C.checkMark;
        ctx.fillText("\u2713", endEx + 12, endEy + 6);
      } else {
        ctx.fillStyle = C.crossMark;
        ctx.fillText("\u2717", endEx + 12, endEy + 6);
      }
    }

    // Info text below e-circle
    const infoY = eCy + eR + 36;
    ctx.font = "10px 'Courier New'";
    if (selected.type === "integer") {
      ctx.fillStyle = C.helixInt;
      const fullTurns = Math.round(n * periods);
      ctx.fillText(`${periods === 2 ? "4\u03C0" : "2\u03C0"}: ${fullTurns} full turn${fullTurns !== 1 ? "s" : ""}`, rightX, infoY);
      ctx.fillStyle = C.checkMark;
      ctx.fillText("Returns to START", rightX, infoY + 16);
    } else if (selected.type === "half") {
      ctx.fillStyle = C.helixHalf;
      if (!show4pi) {
        ctx.fillText("2\u03C0: reaches ANTIPODE", rightX, infoY);
        ctx.fillStyle = C.textDim;
        ctx.fillText("(enable 4\u03C0 test to", rightX, infoY + 16);
        ctx.fillText(" see full return)", rightX, infoY + 30);
      } else {
        ctx.fillText("4\u03C0: full return!", rightX, infoY);
        ctx.fillStyle = C.checkMark;
        ctx.fillText("Returns to START", rightX, infoY + 16);
      }
    } else {
      ctx.fillStyle = C.helixForbid;
      const fracDisplay = (fracAround * 100).toFixed(0);
      ctx.fillText(`${periods === 2 ? "4\u03C0" : "2\u03C0"}: ${fracDisplay}% around`, rightX, infoY);
      ctx.fillStyle = C.crossMark;
      ctx.fillText("DOES NOT CLOSE", rightX, infoY + 16);
      ctx.fillStyle = C.textDim;
      ctx.fillText("Not start or antipode", rightX, infoY + 30);
    }

    // ========== CLASSIFICATION TABLE (toggleable) ==========
    if (showTable) {
      const tblX = rightX;
      const tblY = eCy + eR + 90;
      const rowH = 18;
      const colW = [38, 72, 82];

      ctx.fillStyle = "rgba(10,14,22,0.9)";
      ctx.fillRect(tblX - 6, tblY - 6, 200, rowH * 5 + 12);

      ctx.fillStyle = C.accent;
      ctx.font = "bold 10px 'Courier New'";
      ctx.fillText("TOPOLOGICAL CLASSIFICATION", tblX, tblY);

      const header = ["dim", "\u03C0\u2081(SO(d))", "allowed n"];
      const rows = [
        ["d=1", "trivial", "any real"],
        ["d=2", "\u2124", "any \u2192 anyons"],
        ["d\u22653", "\u2124\u2082", "\u00BDZ (boson/fermion)"],
      ];

      ctx.font = "bold 9px 'Courier New'";
      ctx.fillStyle = C.textDim;
      let cx2 = tblX;
      header.forEach((h, i) => {
        ctx.fillText(h, cx2, tblY + rowH);
        cx2 += colW[i];
      });

      rows.forEach((row, ri) => {
        let cx3 = tblX;
        const ry = tblY + rowH * (ri + 2);
        ctx.font = "9px 'Courier New'";
        row.forEach((cell, ci) => {
          ctx.fillStyle = ri === 2 ? "rgba(180,210,240,0.85)" : C.textDim;
          if (ci === 2 && ri === 2) ctx.fillStyle = C.helixInt;
          ctx.fillText(cell, cx3, ry);
          cx3 += colW[ci];
        });
      });
    }

    // ========== BOTTOM PANEL — status text ==========
    ctx.fillStyle = "rgba(7,9,14,0.95)";
    ctx.fillRect(0, bottomY, W, H - bottomY);
    ctx.strokeStyle = "rgba(40,80,140,0.15)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, bottomY);
    ctx.lineTo(W, bottomY);
    ctx.stroke();

    const txY = bottomY + 22;
    const txX = 28;

    if (selected.type === "integer") {
      ctx.fillStyle = C.helixInt;
      ctx.font = "bold 12px 'Courier New'";
      ctx.fillText(`Winding number ${selected.label} (integer).`, txX, txY);
      ctx.fillStyle = C.text;
      ctx.font = "11px 'Courier New'";
      ctx.fillText("The helix closes after one spatial period (2\u03C0 rotation).", txX, txY + 20);
      ctx.fillStyle = C.textDim;
      ctx.fillText("Bosonic statistics: exchange phase = +1.", txX, txY + 38);
    } else if (selected.type === "half") {
      ctx.fillStyle = C.helixHalf;
      ctx.font = "bold 12px 'Courier New'";
      ctx.fillText(`Winding number ${selected.label} (half-integer).`, txX, txY);
      ctx.fillStyle = C.text;
      ctx.font = "11px 'Courier New'";
      ctx.fillText("The helix reaches the antipodal point after one period; closes after two periods (4\u03C0 / 720\u00B0).", txX, txY + 20);
      ctx.fillStyle = C.textDim;
      ctx.fillText("Fermionic statistics: exchange phase = \u22121.", txX, txY + 38);
    } else {
      ctx.fillStyle = C.helixForbid;
      ctx.font = "bold 12px 'Courier New'";
      ctx.fillText(`Winding number ${selected.label} (FORBIDDEN in d \u2265 3).`, txX, txY);
      ctx.fillStyle = C.text;
      ctx.font = "11px 'Courier New'";
      ctx.fillText("The helix does not close: a 4\u03C0 rotation returns to 2/3 around the e-circle, not to the start.", txX, txY + 20);
      ctx.fillStyle = C.textDim;
      ctx.fillText("\u03C0\u2081(SO(d)) = \u2124\u2082 allows only integer and half-integer windings.", txX, txY + 38);
    }

    s.time += 0.016;
    animRef.current = requestAnimationFrame(draw);
  }, [winding, autoRotate, show4pi, showTable, selected, helixColor]);

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

  const labelStyle = {
    fontSize: 10,
    letterSpacing: "0.15em",
    color: "rgba(100,160,220,0.5)",
    textTransform: "uppercase",
    fontFamily: "'Courier New', monospace",
    display: "block",
    marginBottom: 6,
  };

  const btnStyle = (active, accent) => ({
    padding: "5px 13px",
    fontSize: 11,
    letterSpacing: "0.07em",
    fontFamily: "'Courier New', monospace",
    background: active ? `rgba(${accent},0.2)` : "rgba(20,35,60,0.5)",
    border: `1px solid ${active ? `rgba(${accent},0.6)` : "rgba(50,90,150,0.25)"}`,
    color: active ? `rgba(${accent},1)` : "rgba(120,160,200,0.5)",
    borderRadius: 3,
    cursor: "pointer",
  });

  const windingBtnColor = (w) => {
    if (w.type === "integer") return "48,232,112";
    if (w.type === "half") return "64,160,255";
    return "255,64,64";
  };

  return (
    <div style={{
      background: C.bg,
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      fontFamily: "'Courier New', monospace",
      color: C.text,
      userSelect: "none",
    }}>
      {/* Header */}
      <div style={{
        padding: "16px 28px 10px",
        borderBottom: "1px solid rgba(60,100,180,0.18)",
        display: "flex",
        alignItems: "baseline",
        gap: 14,
      }}>
        <span style={{ fontSize: 11, letterSpacing: "0.18em", color: "rgba(240,160,40,0.45)", textTransform: "uppercase" }}>
          Quantum Geometry in 5D
        </span>
        <span style={{ color: "rgba(80,120,180,0.3)", fontSize: 11 }}>|</span>
        <span style={{ fontSize: 13, color: "rgba(200,210,230,0.65)", letterSpacing: "0.05em" }}>
          Visualization 09 — Topological Winding Numbers
        </span>
      </div>

      {/* Canvas */}
      <canvas ref={canvasRef} style={{ flex: 1, width: "100%", display: "block", cursor: "grab" }} />

      {/* Controls */}
      <div style={{
        padding: "14px 28px 18px",
        borderTop: "1px solid rgba(60,100,180,0.15)",
        display: "flex",
        flexWrap: "wrap",
        gap: "16px 36px",
        alignItems: "flex-start",
        background: "rgba(5,7,9,0.97)",
      }}>

        {/* Winding number selector */}
        <div>
          <span style={labelStyle}>Winding Number</span>
          <div style={{ display: "flex", gap: 5, flexWrap: "wrap" }}>
            {WINDINGS.map((w) => (
              <button
                key={w.label}
                onClick={() => setWinding(w.n)}
                style={{
                  ...btnStyle(winding === w.n, windingBtnColor(w)),
                  ...(w.type === "forbidden" ? {
                    borderStyle: winding === w.n ? "solid" : "dashed",
                  } : {}),
                }}
              >
                {w.label}
                {w.type === "forbidden" ? " !" : ""}
              </button>
            ))}
          </div>
        </div>

        {/* Toggles */}
        <div>
          <span style={labelStyle}>Options</span>
          <div style={{ display: "flex", gap: 8 }}>
            <button onClick={() => setShow4pi(v => !v)}
              style={btnStyle(show4pi, "180,80,255")}>
              {show4pi ? "Showing" : "Show"} 4{"\u03C0"} rotation test
            </button>
            <button onClick={() => setAutoRotate(v => !v)}
              style={btnStyle(autoRotate, "80,160,255")}>
              {autoRotate ? "Auto-rotating" : "Auto-rotate"}
            </button>
            <button onClick={() => setShowTable(v => !v)}
              style={btnStyle(showTable, "240,160,40")}>
              {showTable ? "Hide" : "Show"} classification table
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
