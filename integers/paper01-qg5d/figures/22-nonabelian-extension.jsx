import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  u1: "#44aaff",
  su2: "#ff9944",
  su3: "#55ff99",
  mtheory: "#ffcc44",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  axis: "rgba(100,140,200,0.3)",
  grid: "rgba(30,50,90,0.15)",
  glow: "rgba(68,170,255,0.1)",
};

export default function NonAbelianExtension() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });
  const [view, setView] = useState("tower"); // tower | gaugebosons | convergence

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.015;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    if (view === "tower") drawTower(ctx, W, H, st.time);
    else if (view === "gaugebosons") drawGaugeBosons(ctx, W, H, st.time);
    else drawConvergence(ctx, W, H, st.time);

    animRef.current = requestAnimationFrame(draw);
  }, [view]);

  useEffect(() => {
    animRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(animRef.current);
  }, [draw]);

  function drawTower(ctx, W, H, t) {
    // The dimensional tower: M^4 x S^1 x S^2 x CP^2 = 11
    const cx = W / 2, cy = H / 2 - 20;

    ctx.font = "bold 16px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("The Minimal Geometric Extension to the Standard Model", cx, 30);

    ctx.font = "12px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("Each gauge factor requires its own compact geometry", cx, 50);

    // Draw stacked dimension blocks
    const blocks = [
      { label: "M\u2074", sub: "spacetime", dim: 4, color: "rgba(100,140,200,0.3)", w: 200 },
      { label: "S\u00b9", sub: "e-circle \u2192 U(1)", dim: 1, color: C.u1, w: 60 },
      { label: "S\u00b2", sub: "2-sphere \u2192 SU(2)", dim: 2, color: C.su2, w: 110 },
      { label: "\u2102P\u00b2", sub: "complex projective \u2192 SU(3)", dim: 4, color: C.su3, w: 200 },
    ];

    const totalH = 300;
    const blockGap = 8;
    const totalDim = blocks.reduce((s, b) => s + b.dim, 0);
    let yOff = cy - totalH / 2;

    blocks.forEach((b, i) => {
      const bh = (b.dim / totalDim) * (totalH - blockGap * (blocks.length - 1));
      const bw = b.w;
      const bx = cx - bw / 2;

      // Pulsing glow
      const pulse = 0.7 + 0.3 * Math.sin(t * 2 + i * 1.5);

      // Block
      ctx.fillStyle = typeof b.color === "string" && b.color.startsWith("rgba")
        ? b.color : b.color + Math.round(pulse * 40).toString(16).padStart(2, "0");
      ctx.strokeStyle = b.color;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(bx, yOff, bw, bh, 4);
      ctx.fill();
      ctx.stroke();

      // Labels
      ctx.fillStyle = C.text;
      ctx.font = "bold 14px monospace";
      ctx.textAlign = "center";
      ctx.fillText(b.label, cx, yOff + bh / 2 - 6);

      ctx.font = "11px monospace";
      ctx.fillStyle = C.textDim;
      ctx.fillText(b.sub, cx, yOff + bh / 2 + 10);

      // Dimension count on right
      ctx.fillStyle = b.color;
      ctx.font = "bold 18px monospace";
      ctx.textAlign = "left";
      ctx.fillText(`${b.dim}`, cx + bw / 2 + 20, yOff + bh / 2 + 6);

      yOff += bh + blockGap;
    });

    // Total = 11
    ctx.strokeStyle = C.mtheory;
    ctx.lineWidth = 2;
    const sumX = cx + blocks[0].w / 2 + 20;
    ctx.beginPath();
    ctx.moveTo(sumX + 15, cy - totalH / 2);
    ctx.lineTo(sumX + 25, cy - totalH / 2);
    ctx.lineTo(sumX + 25, cy + totalH / 2);
    ctx.lineTo(sumX + 15, cy + totalH / 2);
    ctx.stroke();

    ctx.fillStyle = C.mtheory;
    ctx.font = "bold 28px monospace";
    ctx.textAlign = "left";
    ctx.fillText("= 11", sumX + 35, cy + 10);

    ctx.font = "13px monospace";
    ctx.fillText("M-theory dimensionality", sumX + 35, cy + 30);

    // Gauge bosons on left
    ctx.textAlign = "right";
    ctx.font = "11px monospace";
    const leftX = cx - blocks[0].w / 2 - 20;

    ctx.fillStyle = C.u1;
    ctx.fillText("1 photon / B boson", leftX, cy - totalH / 2 + 95);
    ctx.fillStyle = C.su2;
    ctx.fillText("W\u207a, W\u207b, Z\u2070", leftX, cy - totalH / 2 + 170);
    ctx.fillStyle = C.su3;
    ctx.fillText("8 gluons", leftX, cy + totalH / 2 - 40);

    ctx.fillStyle = C.textDim;
    ctx.fillText("= 12 gauge bosons", leftX, cy + totalH / 2 + 10);

    // Bottom annotation
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("The e-circle (S\u00b9) of Papers 1\u20133 is one factor of a larger internal geometry.", cx, H - 50);
    ctx.fillStyle = C.mtheory;
    ctx.fillText("Five independent arguments converge on D = 11.", cx, H - 30);
  }

  function drawGaugeBosons(ctx, W, H, t) {
    const cx = W / 2, cy = H / 2;

    ctx.font = "bold 16px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Gauge Bosons from Internal Geometry", cx, 30);

    ctx.font = "12px monospace";
    ctx.fillStyle = C.textDim;
    ctx.fillText("Killing vectors of the internal manifold become gauge fields", cx, 50);

    // Three circles representing the three gauge factors
    const groups = [
      { label: "U(1)", geom: "S\u00b9", dim: 1, bosons: ["photon / B"], color: C.u1, r: 40, x: cx - 220 },
      { label: "SU(2)", geom: "S\u00b2", dim: 2, bosons: ["W\u207a", "W\u207b", "Z\u2070"], color: C.su2, r: 60, x: cx },
      { label: "SU(3)", geom: "\u2102P\u00b2", dim: 4, bosons: ["g\u2081","g\u2082","g\u2083","g\u2084","g\u2085","g\u2086","g\u2087","g\u2088"], color: C.su3, r: 90, x: cx + 230 },
    ];

    groups.forEach((g) => {
      const gy = cy - 30;

      // Rotating manifold representation
      ctx.strokeStyle = g.color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(g.x, gy, g.r, 0, TAU);
      ctx.stroke();

      // Orbiting dots (Killing vectors)
      g.bosons.forEach((b, i) => {
        const angle = t * 1.5 + (i / g.bosons.length) * TAU;
        const bx = g.x + g.r * 0.7 * Math.cos(angle);
        const by = gy + g.r * 0.7 * Math.sin(angle);
        ctx.fillStyle = g.color;
        ctx.beginPath();
        ctx.arc(bx, by, 4, 0, TAU);
        ctx.fill();
      });

      // Labels
      ctx.fillStyle = g.color;
      ctx.font = "bold 16px monospace";
      ctx.textAlign = "center";
      ctx.fillText(g.label, g.x, gy - g.r - 15);

      ctx.font = "12px monospace";
      ctx.fillStyle = C.text;
      ctx.fillText(g.geom, g.x, gy + g.r + 20);
      ctx.fillText(`${g.dim}D`, g.x, gy + g.r + 36);
      ctx.fillStyle = C.textDim;
      ctx.fillText(`${g.bosons.length} boson${g.bosons.length > 1 ? "s" : ""}`, g.x, gy + g.r + 52);
    });

    // Connection arrows
    ctx.strokeStyle = C.textDim;
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.moveTo(cx - 160, cy - 30); ctx.lineTo(cx - 70, cy - 30); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(cx + 70, cy - 30); ctx.lineTo(cx + 130, cy - 30); ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = C.textDim;
    ctx.font = "10px monospace";
    ctx.textAlign = "center";
    ctx.fillText("\u00d7", cx - 115, cy - 34);
    ctx.fillText("\u00d7", cx + 100, cy - 34);

    // Bottom: total
    ctx.fillStyle = C.text;
    ctx.font = "13px monospace";
    ctx.fillText("Total: 1 + 3 + 8 = 12 gauge bosons = the Standard Model", cx, H - 60);

    ctx.fillStyle = C.mtheory;
    ctx.font = "12px monospace";
    ctx.fillText("Baptista (2024): metric instabilities on the SU(3) group manifold produce exactly (SU(3)\u00d7SU(2)\u00d7U(1))/Z\u2086", cx, H - 35);
  }

  function drawConvergence(ctx, W, H, t) {
    const cx = W / 2;

    ctx.font = "bold 16px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    ctx.fillText("Five Independent Arguments \u2192 D = 11", cx, 30);

    const args = [
      { year: "1978", author: "Nahm", text: "Maximum dimension for supergravity without spin > 2", color: "rgba(170,200,235,0.6)" },
      { year: "1978", author: "Cremmer-Julia-Scherk", text: "11D supergravity: unique maximal SUGRA", color: "rgba(170,200,235,0.6)" },
      { year: "1981", author: "Witten", text: "Minimum KK dimension for SM gauge group", color: "rgba(170,200,235,0.6)" },
      { year: "1995", author: "Witten", text: "M-theory: strong coupling limit of type IIA", color: "rgba(170,200,235,0.6)" },
      { year: "2026", author: "This work", text: "Minimal extension of e-circle to SM: M\u2074 \u00d7 S\u00b9 \u00d7 S\u00b2 \u00d7 \u2102P\u00b2", color: C.mtheory },
    ];

    const lineH = 65;
    const startY = 80;
    const timelineX = 180;

    // Timeline line
    ctx.strokeStyle = C.axis;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(timelineX, startY);
    ctx.lineTo(timelineX, startY + args.length * lineH);
    ctx.stroke();

    args.forEach((a, i) => {
      const y = startY + i * lineH + lineH / 2;
      const pulse = 0.7 + 0.3 * Math.sin(t * 2 + i);

      // Dot on timeline
      ctx.fillStyle = a.color;
      ctx.beginPath();
      ctx.arc(timelineX, y, 6 * pulse, 0, TAU);
      ctx.fill();

      // Year
      ctx.font = "bold 13px monospace";
      ctx.textAlign = "right";
      ctx.fillStyle = a.color;
      ctx.fillText(a.year, timelineX - 20, y + 5);

      // Author + text
      ctx.textAlign = "left";
      ctx.font = "bold 13px monospace";
      ctx.fillText(a.author, timelineX + 20, y - 4);
      ctx.font = "11px monospace";
      ctx.fillStyle = C.textDim;
      ctx.fillText(a.text, timelineX + 20, y + 14);
    });

    // All point to 11
    const arrowX = W - 120;
    const arrowY = startY + (args.length * lineH) / 2;

    ctx.fillStyle = C.mtheory;
    ctx.font = "bold 64px monospace";
    ctx.textAlign = "center";
    ctx.globalAlpha = 0.6 + 0.4 * Math.sin(t);
    ctx.fillText("11", arrowX, arrowY + 20);
    ctx.globalAlpha = 1;

    ctx.font = "14px monospace";
    ctx.fillText("dimensions", arrowX, arrowY + 45);

    // Convergence arrows
    ctx.strokeStyle = C.mtheory;
    ctx.lineWidth = 1;
    ctx.globalAlpha = 0.3;
    args.forEach((a, i) => {
      const y = startY + i * lineH + lineH / 2;
      ctx.beginPath();
      ctx.moveTo(timelineX + 450, y);
      ctx.lineTo(arrowX - 40, arrowY);
      ctx.stroke();
    });
    ctx.globalAlpha = 1;

    // Bottom
    ctx.fillStyle = C.text;
    ctx.font = "12px monospace";
    ctx.textAlign = "center";
    ctx.fillText("Either this is the most remarkable numerical coincidence in physics, or it is telling us something.", cx, H - 30);
  }

  const btn = (active) => ({
    background: active ? "rgba(68,170,255,0.2)" : "transparent",
    color: active ? "#44aaff" : C.textDim,
    border: `1px solid ${active ? "#44aaff" : "rgba(100,140,200,0.2)"}`,
    padding: "4px 14px", fontSize: 12, fontFamily: "monospace",
    borderRadius: 3, cursor: "pointer",
  });

  return (
    <div style={{ background: C.bg, minHeight: "100vh", display: "flex", flexDirection: "column", alignItems: "center", padding: 20 }}>
      <canvas ref={canvasRef} width={900} height={520} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <button style={btn(view === "tower")} onClick={() => setView("tower")}>Dimensional Tower</button>
        <button style={btn(view === "gaugebosons")} onClick={() => setView("gaugebosons")}>Gauge Bosons</button>
        <button style={btn(view === "convergence")} onClick={() => setView("convergence")}>Five Arguments \u2192 11</button>
      </div>
    </div>
  );
}
