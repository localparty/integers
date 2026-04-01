import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  grid: "rgba(20,35,65,0.3)",
  particleA: "#ff5555",
  particleB: "#44aaff",
  glowA: "rgba(255,60,60,0.18)",     // used in helix glow passes
  glowB: "rgba(40,160,255,0.18)",
  boson: "rgba(80,255,160,0.9)",
  fermion: "rgba(255,60,80,0.9)",
  axis: "rgba(100,140,200,0.5)",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  ring: "rgba(60,100,180,0.3)",
};

function rotateY(x, y, z, a) {
  return [x * Math.cos(a) + z * Math.sin(a), y, -x * Math.sin(a) + z * Math.cos(a)];
}
function rotateX(x, y, z, a) {
  return [x, y * Math.cos(a) - z * Math.sin(a), y * Math.sin(a) + z * Math.cos(a)];
}
function project3d(x, y, z, fov = 420, camZ = 5) {
  const s = fov / (fov + z + camZ);
  return { px: x * s, py: y * s, s, z };
}

function lerp(a, b, t) {
  return a + (b - a) * t;
}

export default function ExchangePath() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({
    time: 0,
    rotY: 0.4,
    rotX: 0.25,
    exchangeT: 0,       // 0..1 animation progress
    exchanging: false,
    exchangeDone: false,
  });

  const [mode, setMode] = useState("fermion");   // boson | fermion
  const [autoRotate, setAutoRotate] = useState(true);
  const [showTrail, setShowTrail] = useState(true);

  const dragging = useRef(false);
  const lastMouse = useRef({ x: 0, y: 0 });

  const startExchange = useCallback(() => {
    const s = stateRef.current;
    s.exchangeT = 0;
    s.exchanging = true;
    s.exchangeDone = false;
  }, []);

  const resetExchange = useCallback(() => {
    const s = stateRef.current;
    s.exchangeT = 0;
    s.exchanging = false;
    s.exchangeDone = false;
  }, []);

  // Winding number: 1 for boson, 0.5 for fermion
  function getWinding() {
    return mode === "boson" ? 1.0 : 0.5;
  }

  // Draw a particle dot in 3D
  function drawParticle(ctx, cx, cy, x3, y3, z3, rotXa, rotYa, scale, isA) {
    let [rx, ry, rz] = rotateY(x3, y3, z3, rotYa);
    [rx, ry, rz] = rotateX(rx, ry, rz, rotXa);
    const p = project3d(rx * scale, ry * scale, rz * scale);

    const gr = ctx.createRadialGradient(cx + p.px, cy - p.py, 0, cx + p.px, cy - p.py, 16);
    gr.addColorStop(0, isA ? "rgba(255,80,80,0.6)" : "rgba(40,180,255,0.6)");
    gr.addColorStop(1, "rgba(0,0,0,0)");
    ctx.beginPath();
    ctx.arc(cx + p.px, cy - p.py, 16, 0, TAU);
    ctx.fillStyle = gr;
    ctx.fill();

    ctx.beginPath();
    ctx.arc(cx + p.px, cy - p.py, 6, 0, TAU);
    ctx.fillStyle = isA ? C.particleA : C.particleB;
    ctx.fill();

    // Label
    ctx.fillStyle = isA ? "rgba(255,120,120,0.7)" : "rgba(100,180,255,0.7)";
    ctx.font = "bold 11px 'Courier New'";
    ctx.textAlign = "center";
    ctx.fillText(isA ? "A" : "B", cx + p.px, cy - p.py - 14);
    ctx.textAlign = "left";
  }

  // Draw the e-circle indicator
  function drawECircle(ctx, cx, cy, radius, phaseA, phaseB, winding, exchangeT, done) {
    // Background ring
    ctx.beginPath();
    ctx.arc(cx, cy, radius, 0, TAU);
    ctx.strokeStyle = C.ring;
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Tick marks at 0, pi/2, pi, 3pi/2
    for (let i = 0; i < 4; i++) {
      const a = i * Math.PI / 2;
      const inner = radius - 5;
      const outer = radius + 5;
      ctx.beginPath();
      ctx.moveTo(cx + inner * Math.cos(a), cy - inner * Math.sin(a));
      ctx.lineTo(cx + outer * Math.cos(a), cy - outer * Math.sin(a));
      ctx.strokeStyle = "rgba(80,130,200,0.35)";
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    // Labels around the ring
    ctx.fillStyle = "rgba(120,160,210,0.45)";
    ctx.font = "9px 'Courier New'";
    ctx.textAlign = "center";
    ctx.fillText("0", cx + radius + 14, cy + 4);
    ctx.fillText("\u03C0", cx - radius - 14, cy + 4);
    ctx.fillText("\u03C0/2", cx, cy - radius - 8);
    ctx.fillText("3\u03C0/2", cx, cy + radius + 14);

    // Arc showing traversed phase for particle A
    if (exchangeT > 0) {
      const arcEnd = phaseA;
      ctx.beginPath();
      ctx.arc(cx, cy, radius, 0, -arcEnd, true);
      ctx.strokeStyle = "rgba(255,80,80,0.3)";
      ctx.lineWidth = 3;
      ctx.stroke();

      // Arc for particle B
      ctx.beginPath();
      ctx.arc(cx, cy, radius, -Math.PI, -Math.PI - (phaseB - Math.PI), true);
      ctx.strokeStyle = "rgba(40,160,255,0.3)";
      ctx.lineWidth = 3;
      ctx.stroke();
    }

    // Marker for particle A
    const axA = cx + radius * Math.cos(-phaseA);
    const ayA = cy + radius * Math.sin(-phaseA);
    ctx.beginPath();
    ctx.arc(axA, ayA, 7, 0, TAU);
    ctx.fillStyle = C.particleA;
    ctx.fill();
    ctx.beginPath();
    ctx.arc(axA, ayA, 7, 0, TAU);
    ctx.strokeStyle = "rgba(255,255,255,0.3)";
    ctx.lineWidth = 1;
    ctx.stroke();

    // Marker for particle B
    const axB = cx + radius * Math.cos(-phaseB);
    const ayB = cy + radius * Math.sin(-phaseB);
    ctx.beginPath();
    ctx.arc(axB, ayB, 7, 0, TAU);
    ctx.fillStyle = C.particleB;
    ctx.fill();
    ctx.beginPath();
    ctx.arc(axB, ayB, 7, 0, TAU);
    ctx.strokeStyle = "rgba(255,255,255,0.3)";
    ctx.lineWidth = 1;
    ctx.stroke();

    // Title
    ctx.fillStyle = "rgba(180,200,235,0.6)";
    ctx.font = "bold 11px 'Courier New'";
    ctx.textAlign = "center";
    ctx.fillText("e-circle", cx, cy - radius - 24);
    ctx.textAlign = "left";

    // Phase angle readout
    const sWinding = winding;
    const totalPhaseA = exchangeT * sWinding * Math.PI;
    const degA = (totalPhaseA / Math.PI * 180).toFixed(0);

    ctx.fillStyle = "rgba(160,200,240,0.55)";
    ctx.font = "10px 'Courier New'";
    ctx.textAlign = "center";
    ctx.fillText(`\u03B8_A = ${degA}\u00B0`, cx, cy + radius + 30);
    ctx.fillText(`\u03B8_B = ${degA}\u00B0`, cx, cy + radius + 44);

    // Result indicator when done
    if (done) {
      const isBoson = winding === 1.0;
      ctx.fillStyle = isBoson ? C.boson : C.fermion;
      ctx.font = "bold 12px 'Courier New'";
      ctx.fillText(
        isBoson ? "Phase = +1" : "Phase = -1",
        cx, cy + radius + 62
      );
    }

    ctx.textAlign = "left";
  }

  // Draw semicircular exchange paths in 3D (x-z plane)
  function drawExchangeArc(ctx, cx, cy, rotXa, rotYa, scale, t, isA, sepDist) {
    if (t <= 0) return;
    const steps = Math.floor(t * 60);
    const dir = isA ? 1 : -1;
    let prev = null;

    for (let i = 0; i <= steps; i++) {
      const frac = i / 60;
      const angle = frac * Math.PI;
      const ax = dir * sepDist * Math.cos(angle);
      const az = sepDist * Math.sin(angle) * 0.3;  // slight depth for 3D effect
      const ay = 0;

      let [rx, ry, rz] = rotateY(ax, ay, az, rotYa);
      [rx, ry, rz] = rotateX(rx, ry, rz, rotXa);
      const p = project3d(rx * scale, ry * scale, rz * scale);

      if (prev) {
        const depth = (rz + 2) / 4;
        const a = 0.3 + 0.7 * depth;
        ctx.beginPath();
        ctx.moveTo(cx + prev.px, cy - prev.py);
        ctx.lineTo(cx + p.px, cy - p.py);
        ctx.strokeStyle = isA ? C.particleA : C.particleB;
        ctx.globalAlpha = a * 0.6;
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 3]);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.globalAlpha = 1;
      }
      prev = { px: p.px, py: p.py };
    }
  }

  // Draw axes
  function drawAxes(ctx, cx, cy, rotXa, rotYa, scale) {
    const axisLen = 1.2;
    const axes = [
      { dir: [axisLen, 0, 0], label: "x", color: "rgba(200,100,100,0.35)" },
      { dir: [0, axisLen, 0], label: "e", color: "rgba(100,200,100,0.45)" },
      { dir: [0, 0, axisLen], label: "y", color: "rgba(100,100,200,0.35)" },
    ];

    axes.forEach(({ dir, label, color }) => {
      let [rx, ry, rz] = rotateY(dir[0], dir[1], dir[2], rotYa);
      [rx, ry, rz] = rotateX(rx, ry, rz, rotXa);
      const p = project3d(rx * scale, ry * scale, rz * scale);

      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + p.px, cy - p.py);
      ctx.strokeStyle = color;
      ctx.lineWidth = 1;
      ctx.setLineDash([3, 3]);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = color;
      ctx.font = "bold 11px 'Courier New'";
      ctx.textAlign = "center";
      ctx.fillText(label, cx + p.px * 1.12, cy - p.py * 1.12 + 4);
      ctx.textAlign = "left";
    });
  }

  // Draw a helix segment wound around the e-axis (vertical)
  function drawEHelix(ctx, cx, cy, rotXa, rotYa, scale, eStart, eEnd, spatialOffset, isA, alpha) {
    const steps = 100;
    const helixRadius = 0.2;
    let prev = null;

    for (let i = 0; i <= steps; i++) {
      const t = i / steps;
      const e = lerp(eStart, eEnd, t);
      const angle = e;   // e-coordinate IS the angle around the helix
      const hx = spatialOffset + helixRadius * Math.cos(angle);
      const hz = helixRadius * Math.sin(angle);
      const hy = e / (TAU) * 0.8;  // vertical position proportional to e

      let [rx, ry, rz] = rotateY(hx, hy, hz, rotYa);
      [rx, ry, rz] = rotateX(rx, ry, rz, rotXa);
      const p = project3d(rx * scale, ry * scale, rz * scale);

      if (prev) {
        const depth = (rz + 2) / 4;
        const a = (0.2 + 0.8 * depth) * alpha;
        ctx.beginPath();
        ctx.moveTo(cx + prev.px, cy - prev.py);
        ctx.lineTo(cx + p.px, cy - p.py);

        // Glow
        ctx.strokeStyle = isA
          ? `rgba(255,60,60,${a * 0.12})`
          : `rgba(40,160,255,${a * 0.12})`;
        ctx.lineWidth = 5;
        ctx.stroke();

        ctx.strokeStyle = isA ? C.particleA : C.particleB;
        ctx.globalAlpha = a;
        ctx.lineWidth = 1.8;
        ctx.stroke();
        ctx.globalAlpha = 1;
      }
      prev = { px: p.px, py: p.py };
    }
  }

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width;
    const H = canvas.height;
    const s = stateRef.current;

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    // Auto rotation
    if (autoRotate) s.rotY += 0.005;

    // Exchange animation
    if (s.exchanging) {
      s.exchangeT = Math.min(1, s.exchangeT + 0.005);
      if (s.exchangeT >= 1) {
        s.exchanging = false;
        s.exchangeDone = true;
      }
    }

    const winding = getWinding();
    const eT = s.exchangeT;

    // Layout: main 3D scene on left ~60%, e-circle on right ~25%, info panel overlaid
    const infoW = W * 0.24;
    const mainCx = infoW + (W - infoW) * 0.38;
    const mainCy = H * 0.46;
    const scale = Math.min(W - infoW, H) * 0.18;

    // e-circle position
    const eCircleCx = W - 110;
    const eCircleCy = H * 0.32;
    const eCircleR = 55;

    // Separation distance for the two particles
    const sepDist = 0.6;

    // Particle positions during exchange:
    // They start at (+sep, 0, 0) and (-sep, 0, 0)
    // Exchange via semicircular paths in the x-z plane
    const exchangeAngle = eT * Math.PI;
    const posAx = sepDist * Math.cos(exchangeAngle);
    const posAz = sepDist * Math.sin(exchangeAngle) * 0.3;
    const posBx = -sepDist * Math.cos(exchangeAngle);
    const posBz = -sepDist * Math.sin(exchangeAngle) * 0.3;

    // e-coordinates advance by s*pi during exchange
    const ePhaseA = eT * winding * Math.PI;
    const ePhaseB = Math.PI + eT * winding * Math.PI;

    // Vertical positions (e-axis shown as vertical)
    const posAy = ePhaseA / TAU * 0.8;
    const posBoffset = Math.PI;
    const posByInit = posBoffset / TAU * 0.8;
    const posBy = (ePhaseB) / TAU * 0.8;

    // ---- Draw Axes ----
    drawAxes(ctx, mainCx, mainCy, s.rotX, s.rotY, scale);

    // ---- Draw helix trails (the e-dimension paths) ----
    if (showTrail && eT > 0.01) {
      drawEHelix(ctx, mainCx, mainCy, s.rotX, s.rotY, scale, 0, ePhaseA, sepDist, true, 0.7);
      drawEHelix(ctx, mainCx, mainCy, s.rotX, s.rotY, scale, Math.PI, ePhaseB, -sepDist, false, 0.7);
    }

    // ---- Draw exchange arcs (spatial paths) ----
    drawExchangeArc(ctx, mainCx, mainCy, s.rotX, s.rotY, scale, eT, true, sepDist);
    drawExchangeArc(ctx, mainCx, mainCy, s.rotX, s.rotY, scale, eT, false, sepDist);

    // ---- Draw initial position markers (faded if exchanging) ----
    if (eT < 0.1) {
      drawParticle(ctx, mainCx, mainCy, sepDist, 0, 0, s.rotX, s.rotY, scale, true);
      drawParticle(ctx, mainCx, mainCy, -sepDist, posByInit, 0, s.rotX, s.rotY, scale, false);
    }

    // ---- Draw current particle positions ----
    if (eT > 0) {
      drawParticle(ctx, mainCx, mainCy, posAx, posAy, posAz, s.rotX, s.rotY, scale, true);
      drawParticle(ctx, mainCx, mainCy, posBx, posBy, posBz, s.rotX, s.rotY, scale, false);
    }

    // ---- Draw the base plane (faint grid) ----
    const gridSize = 1.4;
    const gridSteps = 6;
    for (let i = -gridSteps; i <= gridSteps; i++) {
      const frac = i / gridSteps * gridSize;
      // Lines along x
      let [rx1, ry1, rz1] = rotateY(-gridSize, -0.05, frac, s.rotY);
      [rx1, ry1, rz1] = rotateX(rx1, ry1, rz1, s.rotX);
      let [rx2, ry2, rz2] = rotateY(gridSize, -0.05, frac, s.rotY);
      [rx2, ry2, rz2] = rotateX(rx2, ry2, rz2, s.rotX);
      const p1 = project3d(rx1 * scale, ry1 * scale, rz1 * scale);
      const p2 = project3d(rx2 * scale, ry2 * scale, rz2 * scale);
      ctx.beginPath();
      ctx.moveTo(mainCx + p1.px, mainCy - p1.py);
      ctx.lineTo(mainCx + p2.px, mainCy - p2.py);
      ctx.strokeStyle = C.grid;
      ctx.lineWidth = 0.5;
      ctx.stroke();

      // Lines along z
      [rx1, ry1, rz1] = rotateY(frac, -0.05, -gridSize, s.rotY);
      [rx1, ry1, rz1] = rotateX(rx1, ry1, rz1, s.rotX);
      [rx2, ry2, rz2] = rotateY(frac, -0.05, gridSize, s.rotY);
      [rx2, ry2, rz2] = rotateX(rx2, ry2, rz2, s.rotX);
      const p3 = project3d(rx1 * scale, ry1 * scale, rz1 * scale);
      const p4 = project3d(rx2 * scale, ry2 * scale, rz2 * scale);
      ctx.beginPath();
      ctx.moveTo(mainCx + p3.px, mainCy - p3.py);
      ctx.lineTo(mainCx + p4.px, mainCy - p4.py);
      ctx.strokeStyle = C.grid;
      ctx.lineWidth = 0.5;
      ctx.stroke();
    }

    // ---- Draw e-circle ----
    drawECircle(ctx, eCircleCx, eCircleCy, eCircleR, ePhaseA, ePhaseB, winding, eT, s.exchangeDone);

    // ---- Phase formula display ----
    const formulaX = eCircleCx;
    const formulaY = eCircleCy + eCircleR + 85;

    ctx.textAlign = "center";
    ctx.fillStyle = "rgba(180,200,235,0.55)";
    ctx.font = "11px 'Courier New'";
    ctx.fillText("Exchange phase:", formulaX, formulaY);

    const sLabel = mode === "boson" ? "s = 1" : "s = 1/2";
    ctx.fillStyle = "rgba(140,180,220,0.5)";
    ctx.font = "10px 'Courier New'";
    ctx.fillText(`winding ${sLabel}`, formulaX, formulaY + 16);

    if (s.exchangeDone) {
      const isBoson = winding === 1.0;
      ctx.font = "bold 13px 'Courier New'";
      ctx.fillStyle = isBoson ? C.boson : C.fermion;
      const phaseStr = isBoson
        ? "e^(i\u00B72\u03C0\u00B71) = +1"
        : "e^(i\u00B72\u03C0\u00B7\u00BD) = -1";
      ctx.fillText(phaseStr, formulaX, formulaY + 38);
    } else if (eT > 0) {
      const currentPhase = eT * winding * Math.PI;
      const deg = (currentPhase / Math.PI * 180).toFixed(0);
      ctx.fillStyle = "rgba(160,200,240,0.5)";
      ctx.font = "11px 'Courier New'";
      ctx.fillText(`\u03B8 = ${deg}\u00B0`, formulaX, formulaY + 38);
    }
    ctx.textAlign = "left";

    // ---- INFO PANEL (left side) ----
    ctx.fillStyle = C.panelBg;
    ctx.fillRect(0, 0, infoW, H);
    ctx.strokeStyle = "rgba(35,65,125,0.2)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(infoW, 0);
    ctx.lineTo(infoW, H);
    ctx.stroke();

    const ip = { x: 14, y: 20 };
    ctx.fillStyle = mode === "boson" ? "rgba(80,255,160,0.7)" : "rgba(255,100,100,0.7)";
    ctx.font = "bold 13px 'Courier New'";
    ctx.fillText("EXCHANGE PATH", ip.x, ip.y + 14);
    ctx.fillStyle = C.textDim;
    ctx.font = "10px 'Courier New'";
    ctx.fillText("particle exchange in 5D", ip.x, ip.y + 28);

    const lines = mode === "fermion"
      ? [
          "Two identical fermions",
          "(s = 1/2) exchange",
          "positions in space.",
          "",
          "In 5D, their worldlines",
          "are helices through the",
          "compact e-dimension.",
          "",
          "During exchange, each",
          "particle's e-coordinate",
          "advances by s\u03C0 = \u03C0/2.",
          "",
          "Total phase accumulated:",
          "2 \u00D7 \u03C0/2 = \u03C0",
          "",
          "\u2192 e^(i\u03C0) = -1",
          "\u2192 antisymmetric \u03C8",
          "\u2192 Pauli exclusion",
          "",
          "The sign flip is NOT",
          "imposed \u2014 it follows",
          "from the geometry.",
        ]
      : [
          "Two identical bosons",
          "(s = 1) exchange",
          "positions in space.",
          "",
          "In 5D, their worldlines",
          "are helices through the",
          "compact e-dimension.",
          "",
          "During exchange, each",
          "particle's e-coordinate",
          "advances by s\u03C0 = \u03C0.",
          "",
          "Total phase accumulated:",
          "2 \u00D7 \u03C0 = 2\u03C0",
          "",
          "\u2192 e^(i\u00B72\u03C0) = +1",
          "\u2192 symmetric \u03C8",
          "\u2192 bunching allowed",
          "",
          "Integer winding returns",
          "the e-phase to its",
          "starting point.",
        ];

    ctx.fillStyle = C.textDim;
    ctx.font = "11px 'Courier New'";
    lines.forEach((l, i) => ctx.fillText(l, ip.x, ip.y + 55 + i * 16));

    // ---- BOTTOM ANNOTATION PANEL ----
    const annotY = H - 60;
    ctx.fillStyle = "rgba(5,7,9,0.95)";
    ctx.fillRect(0, annotY - 8, W, 70);
    ctx.strokeStyle = "rgba(30,60,120,0.15)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(0, annotY - 8);
    ctx.lineTo(W, annotY - 8);
    ctx.stroke();

    ctx.textAlign = "left";
    if (mode === "fermion") {
      ctx.fillStyle = C.fermion;
      ctx.font = "bold 11px 'Courier New'";
      ctx.fillText("Half-integer winding (fermion)", infoW + 14, annotY + 8);
      ctx.fillStyle = "rgba(170,200,235,0.5)";
      ctx.font = "10px 'Courier New'";
      ctx.fillText(
        "Each particle's e-coordinate reaches the antipodal point. Phase = -1. Antisymmetric wavefunction. Pauli exclusion follows.",
        infoW + 14, annotY + 26
      );
    } else {
      ctx.fillStyle = C.boson;
      ctx.font = "bold 11px 'Courier New'";
      ctx.fillText("Integer winding (boson)", infoW + 14, annotY + 8);
      ctx.fillStyle = "rgba(170,200,235,0.5)";
      ctx.font = "10px 'Courier New'";
      ctx.fillText(
        "Each particle's e-coordinate completes a full revolution during exchange. Phase = +1. Symmetric wavefunction.",
        infoW + 14, annotY + 26
      );
    }

    // ---- Progress bar for exchange ----
    if (eT > 0 && eT < 1) {
      const barX = infoW + 14;
      const barY = annotY + 42;
      const barW = W - infoW - 140;
      const barH = 4;

      ctx.fillStyle = "rgba(30,50,80,0.5)";
      ctx.fillRect(barX, barY, barW, barH);

      const progressColor = mode === "boson" ? "rgba(80,255,160,0.7)" : "rgba(255,80,100,0.7)";
      ctx.fillStyle = progressColor;
      ctx.fillRect(barX, barY, barW * eT, barH);

      ctx.fillStyle = "rgba(140,180,220,0.4)";
      ctx.font = "9px 'Courier New'";
      ctx.fillText(`${(eT * 100).toFixed(0)}%`, barX + barW + 8, barY + 4);
    }

    // ---- Scene title labels ----
    ctx.textAlign = "center";
    ctx.fillStyle = "rgba(120,160,210,0.35)";
    ctx.font = "10px 'Courier New'";
    ctx.fillText("(x, y, e)-space", mainCx, mainCy + scale * 1.2 + 24);

    if (!s.exchanging && !s.exchangeDone && eT === 0) {
      ctx.fillStyle = "rgba(140,180,220,0.3)";
      ctx.font = "11px 'Courier New'";
      ctx.fillText("Press Exchange to begin", mainCx, mainCy + scale * 1.2 + 44);
    }

    if (s.exchangeDone) {
      const isBoson = winding === 1.0;
      ctx.fillStyle = isBoson ? C.boson : C.fermion;
      ctx.font = "bold 14px 'Courier New'";
      const label = isBoson
        ? "Exchange complete: phase = +1"
        : "Exchange complete: phase = -1";
      ctx.fillText(label, mainCx, mainCy - scale * 1.15 - 10);

      ctx.fillStyle = "rgba(160,200,240,0.35)";
      ctx.font = "10px 'Courier New'";
      const sublabel = isBoson
        ? "Particles swapped, wavefunction unchanged"
        : "Particles swapped, wavefunction sign-flipped";
      ctx.fillText(sublabel, mainCx, mainCy - scale * 1.15 + 8);
    }
    ctx.textAlign = "left";

    s.time += 0.016;
    animRef.current = requestAnimationFrame(draw);
  }, [mode, autoRotate, showTrail]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const resize = () => { canvas.width = canvas.offsetWidth; canvas.height = canvas.offsetHeight; };
    resize();
    window.addEventListener("resize", resize);
    animRef.current = requestAnimationFrame(draw);
    return () => { cancelAnimationFrame(animRef.current); window.removeEventListener("resize", resize); };
  }, [draw]);

  // Mouse drag for rotation
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const onDown = e => {
      dragging.current = true;
      lastMouse.current = { x: e.clientX, y: e.clientY };
      setAutoRotate(false);
    };
    const onMove = e => {
      if (!dragging.current) return;
      const dx = e.clientX - lastMouse.current.x;
      const dy = e.clientY - lastMouse.current.y;
      stateRef.current.rotY += dx * 0.009;
      stateRef.current.rotX += dy * 0.009;
      lastMouse.current = { x: e.clientX, y: e.clientY };
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

  const label = {
    fontSize: 10, letterSpacing: "0.14em", color: "rgba(75,120,175,0.5)",
    textTransform: "uppercase", fontFamily: "'Courier New', monospace",
    display: "block", marginBottom: 5,
  };
  const btn = (active, col) => ({
    padding: "5px 12px", fontSize: 11, letterSpacing: "0.06em",
    fontFamily: "'Courier New', monospace",
    background: active ? `rgba(${col},0.18)` : "rgba(12,20,40,0.7)",
    border: `1px solid ${active ? `rgba(${col},0.55)` : "rgba(30,60,120,0.22)"}`,
    color: active ? `rgba(${col},1)` : "rgba(95,140,190,0.5)",
    borderRadius: 3, cursor: "pointer",
  });

  return (
    <div style={{
      background: C.bg, minHeight: "100vh", display: "flex",
      flexDirection: "column", fontFamily: "'Courier New', monospace",
      color: C.text, userSelect: "none",
    }}>

      <div style={{
        padding: "15px 26px 9px",
        borderBottom: "1px solid rgba(30,60,120,0.18)",
        display: "flex", alignItems: "baseline", gap: 14,
      }}>
        <span style={{
          fontSize: 11, letterSpacing: "0.18em",
          color: mode === "boson" ? "rgba(80,255,160,0.4)" : "rgba(255,100,100,0.4)",
          textTransform: "uppercase",
        }}>
          Quantum Geometry in 5D
        </span>
        <span style={{ color: "rgba(45,80,140,0.3)" }}>|</span>
        <span style={{
          fontSize: 13, color: "rgba(185,215,245,0.65)",
          letterSpacing: "0.05em",
        }}>
          Visualization 06 — Exchange Path &amp; Statistics
        </span>
      </div>

      <canvas ref={canvasRef} style={{
        flex: 1, width: "100%", display: "block", cursor: "grab",
      }} />

      <div style={{
        padding: "13px 26px 17px",
        borderTop: "1px solid rgba(30,60,120,0.15)",
        display: "flex", flexWrap: "wrap", gap: "15px 30px",
        alignItems: "flex-start", background: "rgba(5,7,9,0.98)",
      }}>

        {/* Particle type */}
        <div>
          <span style={label}>Statistics</span>
          <div style={{ display: "flex", gap: 6 }}>
            <button
              onClick={() => { setMode("fermion"); resetExchange(); }}
              style={btn(mode === "fermion", "255,80,100")}
            >
              Half-integer (fermion)
            </button>
            <button
              onClick={() => { setMode("boson"); resetExchange(); }}
              style={btn(mode === "boson", "80,255,160")}
            >
              Integer (boson)
            </button>
          </div>
        </div>

        {/* Exchange controls */}
        <div>
          <span style={label}>Animation</span>
          <div style={{ display: "flex", gap: 6 }}>
            <button onClick={startExchange} style={{
              ...btn(true, mode === "boson" ? "80,255,160" : "255,80,100"),
              fontWeight: "bold",
            }}>
              Exchange
            </button>
            <button onClick={resetExchange} style={btn(false, "100,150,220")}>
              Reset
            </button>
          </div>
        </div>

        {/* Toggles */}
        <div style={{ display: "flex", gap: 8, alignItems: "flex-end", paddingBottom: 1 }}>
          <button
            onClick={() => setAutoRotate(v => !v)}
            style={btn(autoRotate, "80,200,160")}
          >
            {autoRotate ? "\u27F3 rotating" : "\u25B7 rotate"}
          </button>
          <button
            onClick={() => setShowTrail(v => !v)}
            style={btn(showTrail, "180,140,255")}
          >
            Trails {showTrail ? "on" : "off"}
          </button>
          <span style={{
            fontSize: 10, color: "rgba(60,100,150,0.4)",
            alignSelf: "center", marginLeft: 4,
          }}>
            drag to rotate
          </span>
        </div>
      </div>
    </div>
  );
}
