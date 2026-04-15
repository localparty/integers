import { useRef, useEffect, useState, useCallback } from "react";

const TAU = Math.PI * 2;

const C = {
  bg: "#050709",
  panelBg: "rgba(6,8,14,0.97)",
  lcdm: "rgba(100,140,200,0.7)",
  framework: "#ff9944",
  frameworkGlow: "rgba(255,150,60,0.15)",
  desi: "#55ff99",
  trgb: "#ff55ff",
  shoes: "#ff5555",
  planck: "#44aaff",
  axis: "rgba(100,140,200,0.4)",
  text: "rgba(170,200,235,0.75)",
  textDim: "rgba(75,115,165,0.45)",
  gold: "#ffcc44",
};

// Simplified H(z) computation (close to CAMB for flat LCDM/wCDM)
function Hz(z, H0, Om, Or, w0, wa) {
  const Ode = 1 - Om - Or;
  const a = 1 / (1 + z);
  const weff = w0 + wa * (1 - a);
  const deRatio = Math.pow(1 + z, 3 * (1 + w0 + wa)) * Math.exp(-3 * wa * z / (1 + z));
  return H0 * Math.sqrt(Or * Math.pow(1 + z, 4) + Om * Math.pow(1 + z, 3) + Ode * deRatio);
}

function ageIntegrand(z, H0, Om, Or, w0, wa) {
  return 1 / ((1 + z) * Hz(z, H0, Om, Or, w0, wa));
}

// Simple trapezoidal integration
function integrate(f, a, b, n) {
  const dx = (b - a) / n;
  let s = 0.5 * (f(a) + f(b));
  for (let i = 1; i < n; i++) s += f(a + i * dx);
  return s * dx;
}

export default function ExpansionHistory() {
  const canvasRef = useRef(null);
  const animRef = useRef(null);
  const stateRef = useRef({ time: 0 });

  const [xi, setXi] = useState(43); // * 0.01
  const [view, setView] = useState("Hz"); // Hz | ratio | age | h0
  const [showDESI, setShowDESI] = useState(true);

  const draw = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width, H = canvas.height;
    const st = stateRef.current;
    st.time += 0.015;

    ctx.fillStyle = C.bg;
    ctx.fillRect(0, 0, W, H);

    const xiVal = xi / 100;
    const DN = 6.14 * Math.pow(xiVal, 4);
    const H0_fw = 67.4 + 6.3 * DN;
    const Neff_fw = 3.044 + 0.05 + DN;
    const omch2_fw = 0.02237 / (xiVal * xiVal);
    const h_fw = H0_fw / 100;
    const Om_fw = (0.02237 + omch2_fw + 0.06 / 93.14) / (h_fw * h_fw);
    const Or_fw = 4.15e-5 * (Neff_fw / 3.044) / (h_fw * h_fw);

    // LCDM reference
    const H0_lcdm = 67.4, Om_lcdm = 0.315, Or_lcdm = 9.14e-5;

    const mL = 80, mR = 30, mT = 55, mB = 60;
    const pW = W - mL - mR, pH = H - mT - mB;

    // Axes
    ctx.strokeStyle = C.axis;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(mL, mT); ctx.lineTo(mL, mT + pH); ctx.lineTo(mL + pW, mT + pH);
    ctx.stroke();

    if (view === "Hz" || view === "ratio") {
      const zMax = 3, nPts = 200;

      // Compute H(z) for both models
      const lcdmH = [], fwH = [];
      for (let i = 0; i <= nPts; i++) {
        const z = (i / nPts) * zMax;
        lcdmH.push(Hz(z, H0_lcdm, Om_lcdm, Or_lcdm, -1, 0));
        fwH.push(Hz(z, H0_fw, Om_fw, Or_fw, -1.0, 0));
      }

      const toX = (i) => mL + (i / nPts) * pW;

      if (view === "Hz") {
        const hMax = Math.max(...fwH, ...lcdmH) * 1.1;
        const toY = (h) => mT + pH - (h / hMax) * pH;

        // LCDM
        ctx.beginPath();
        for (let i = 0; i <= nPts; i++) {
          if (i === 0) ctx.moveTo(toX(i), toY(lcdmH[i]));
          else ctx.lineTo(toX(i), toY(lcdmH[i]));
        }
        ctx.strokeStyle = C.lcdm;
        ctx.lineWidth = 2;
        ctx.setLineDash([6, 4]);
        ctx.stroke();
        ctx.setLineDash([]);

        // Framework
        ctx.beginPath();
        for (let i = 0; i <= nPts; i++) {
          if (i === 0) ctx.moveTo(toX(i), toY(fwH[i]));
          else ctx.lineTo(toX(i), toY(fwH[i]));
        }
        ctx.strokeStyle = C.framework;
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Labels
        ctx.font = "12px monospace";
        ctx.fillStyle = C.lcdm;
        ctx.fillText("ΛCDM (H₀=67.4)", mL + pW - 160, toY(lcdmH[nPts]) - 15);
        ctx.fillStyle = C.framework;
        ctx.fillText(`5D (ξ=${xiVal.toFixed(2)}, H₀=${H0_fw.toFixed(1)})`, mL + pW - 210, toY(fwH[nPts]) + 20);

        ctx.fillStyle = C.textDim;
        ctx.textAlign = "center";
        ctx.fillText("H(z) [km/s/Mpc]", 35, mT + pH / 2);
        ctx.fillText("Redshift z", mL + pW / 2, mT + pH + 35);
        ctx.textAlign = "left";

        // Y-axis ticks
        for (let h = 0; h <= hMax; h += 50) {
          ctx.fillStyle = C.textDim;
          ctx.font = "10px monospace";
          ctx.fillText(h.toFixed(0), mL - 35, toY(h) + 4);
        }
      }

      if (view === "ratio") {
        const toY = (r) => mT + pH - ((r - 0.96) / 0.12) * pH;

        // Ratio line
        ctx.beginPath();
        for (let i = 0; i <= nPts; i++) {
          const ratio = fwH[i] / lcdmH[i];
          if (i === 0) ctx.moveTo(toX(i), toY(ratio));
          else ctx.lineTo(toX(i), toY(ratio));
        }
        ctx.strokeStyle = C.framework;
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Reference line at 1
        ctx.strokeStyle = C.lcdm;
        ctx.lineWidth = 1;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(mL, toY(1)); ctx.lineTo(mL + pW, toY(1));
        ctx.stroke();
        ctx.setLineDash([]);

        // Peak annotation
        let maxRatio = 0, maxI = 0;
        for (let i = 0; i <= nPts; i++) {
          const r = fwH[i] / lcdmH[i];
          if (r > maxRatio) { maxRatio = r; maxI = i; }
        }
        const peakZ = (maxI / nPts) * zMax;
        ctx.fillStyle = C.gold;
        ctx.font = "12px monospace";
        ctx.fillText(`Peak: ${((maxRatio - 1) * 100).toFixed(1)}% above ΛCDM at z ≈ ${peakZ.toFixed(1)}`, toX(maxI) - 60, toY(maxRatio) - 15);

        ctx.beginPath();
        ctx.arc(toX(maxI), toY(maxRatio), 5, 0, TAU);
        ctx.fillStyle = C.gold;
        ctx.fill();

        ctx.fillStyle = C.textDim;
        ctx.textAlign = "center";
        ctx.fillText("H(z) / H_ΛCDM(z)", 35, mT + pH / 2);
        ctx.fillText("Redshift z", mL + pW / 2, mT + pH + 35);
        ctx.textAlign = "left";

        // DESI data points (approximate BAO measurements)
        if (showDESI) {
          const desiZ = [0.3, 0.5, 0.7, 1.0, 1.5, 2.3];
          const desiErr = 0.015; // ~1.5% precision
          ctx.fillStyle = C.desi;
          ctx.font = "10px monospace";
          for (const z of desiZ) {
            const i = Math.round((z / zMax) * nPts);
            const r = fwH[i] / lcdmH[i];
            ctx.beginPath();
            ctx.arc(toX(i), toY(r), 4, 0, TAU);
            ctx.fill();
            // Error bar
            ctx.strokeStyle = C.desi;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(toX(i), toY(r - desiErr));
            ctx.lineTo(toX(i), toY(r + desiErr));
            ctx.stroke();
          }
          ctx.fillStyle = C.desi;
          ctx.fillText("DESI BAO (projected)", mL + 10, mT + 20);
        }
      }
    }

    if (view === "age" || view === "h0") {
      // xi sweep plot
      const nXi = 100;
      const xiMin = 0.3, xiMax = 0.55;

      const values = [];
      for (let i = 0; i <= nXi; i++) {
        const x = xiMin + (i / nXi) * (xiMax - xiMin);
        const dn = 6.14 * Math.pow(x, 4);
        const h0 = 67.4 + 6.3 * dn;
        const h = h0 / 100;
        const oc = 0.02237 / (x * x);
        const om = (0.02237 + oc + 0.06 / 93.14) / (h * h);
        const or_ = 4.15e-5 * ((3.094 + dn) / 3.044) / (h * h);

        // Age integral (approximate)
        const ageSec = integrate(
          (z) => ageIntegrand(z, h0, om, or_, -1.0, 0),
          0, 1000, 500
        );
        const ageGyr = ageSec * 3.086e19 / 3.156e16; // Mpc/km * s/Gyr
        values.push({ xi: x, h0, age: ageGyr, om, neff: 3.044 + 0.05 + dn, dmRatio: 1 / (x * x) });
      }

      const toX = (i) => mL + (i / nXi) * pW;

      if (view === "h0") {
        const h0s = values.map(v => v.h0);
        const hMin = 66, hMax = 72;
        const toY = (h) => mT + pH - ((h - hMin) / (hMax - hMin)) * pH;

        // Framework curve
        ctx.beginPath();
        for (let i = 0; i <= nXi; i++) {
          if (i === 0) ctx.moveTo(toX(i), toY(h0s[i]));
          else ctx.lineTo(toX(i), toY(h0s[i]));
        }
        ctx.strokeStyle = C.framework;
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Reference lines
        const refs = [
          { val: 67.4, label: "Planck ΛCDM", color: C.planck },
          { val: 69.8, label: "TRGB/CCHP", color: C.trgb },
          { val: 73.0, label: "SH0ES Cepheids", color: C.shoes },
        ];
        for (const ref of refs) {
          if (ref.val < hMin || ref.val > hMax) continue;
          ctx.strokeStyle = ref.color;
          ctx.lineWidth = 1;
          ctx.setLineDash([4, 4]);
          ctx.beginPath();
          ctx.moveTo(mL, toY(ref.val)); ctx.lineTo(mL + pW, toY(ref.val));
          ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = ref.color;
          ctx.font = "11px monospace";
          ctx.fillText(ref.label, mL + pW - 140, toY(ref.val) - 5);
        }

        // Current xi marker
        const curIdx = Math.round(((xiVal - xiMin) / (xiMax - xiMin)) * nXi);
        if (curIdx >= 0 && curIdx <= nXi) {
          ctx.beginPath();
          ctx.arc(toX(curIdx), toY(h0s[curIdx]), 6, 0, TAU);
          ctx.fillStyle = C.gold;
          ctx.fill();
          ctx.fillStyle = C.gold;
          ctx.font = "12px monospace";
          ctx.fillText(`ξ=${xiVal.toFixed(2)} → H₀=${h0s[curIdx].toFixed(1)}`, toX(curIdx) + 10, toY(h0s[curIdx]) - 8);
        }

        ctx.fillStyle = C.textDim;
        ctx.textAlign = "center";
        ctx.fillText("H₀ (km/s/Mpc)", 30, mT + pH / 2);
        ctx.fillText("ξ = T_hidden / T_visible", mL + pW / 2, mT + pH + 35);
        ctx.textAlign = "left";
      }

      if (view === "age") {
        const ages = values.map(v => v.age);
        const aMin = 12.5, aMax = 15;
        const toY = (a) => mT + pH - ((a - aMin) / (aMax - aMin)) * pH;

        ctx.beginPath();
        for (let i = 0; i <= nXi; i++) {
          if (i === 0) ctx.moveTo(toX(i), toY(ages[i]));
          else ctx.lineTo(toX(i), toY(ages[i]));
        }
        ctx.strokeStyle = C.framework;
        ctx.lineWidth = 2.5;
        ctx.stroke();

        // Planck age
        ctx.strokeStyle = C.planck;
        ctx.lineWidth = 1;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(mL, toY(13.8)); ctx.lineTo(mL + pW, toY(13.8));
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = C.planck;
        ctx.font = "11px monospace";
        ctx.fillText("Planck ΛCDM: 13.80 Gyr", mL + pW - 200, toY(13.8) - 5);

        // Current xi marker
        const curIdx = Math.round(((xiVal - xiMin) / (xiMax - xiMin)) * nXi);
        if (curIdx >= 0 && curIdx <= nXi) {
          ctx.beginPath();
          ctx.arc(toX(curIdx), toY(ages[curIdx]), 6, 0, TAU);
          ctx.fillStyle = C.gold;
          ctx.fill();
          ctx.fillStyle = C.gold;
          ctx.font = "12px monospace";
          ctx.fillText(`ξ=${xiVal.toFixed(2)} → t₀=${ages[curIdx].toFixed(2)} Gyr`, toX(curIdx) + 10, toY(ages[curIdx]) - 8);
        }

        ctx.fillStyle = C.textDim;
        ctx.textAlign = "center";
        ctx.fillText("Age (Gyr)", 30, mT + pH / 2);
        ctx.fillText("ξ = T_hidden / T_visible", mL + pW / 2, mT + pH + 35);
        ctx.textAlign = "left";
      }
    }

    // X-axis labels for Hz/ratio views
    if (view === "Hz" || view === "ratio") {
      ctx.font = "10px monospace";
      ctx.fillStyle = C.textDim;
      for (let z = 0; z <= 3; z += 0.5) {
        const x = mL + (z / 3) * pW;
        ctx.fillText(z.toFixed(1), x - 8, mT + pH + 18);
      }
    }

    // Title
    ctx.font = "14px monospace";
    ctx.fillStyle = C.text;
    ctx.textAlign = "center";
    const titles = {
      Hz: "Expansion History H(z): 5D Framework vs ΛCDM",
      ratio: "H(z) Ratio to ΛCDM — The Framework's Fingerprint",
      age: "Age of the Universe vs ξ",
      h0: "Hubble Constant H₀ vs ξ",
    };
    ctx.fillText(titles[view], W / 2, 25);
    ctx.textAlign = "left";

    // Live readout
    ctx.fillStyle = C.panelBg;
    ctx.fillRect(W - 220, 8, 210, 80);
    ctx.font = "11px monospace";
    ctx.fillStyle = C.framework;
    ctx.fillText(`ξ = ${xiVal.toFixed(3)}`, W - 210, 28);
    ctx.fillText(`H₀ = ${H0_fw.toFixed(1)} km/s/Mpc`, W - 210, 44);
    ctx.fillText(`N_eff = ${Neff_fw.toFixed(3)}`, W - 210, 60);
    ctx.fillText(`Ω_DM/Ω_b = ${(1/xiVal/xiVal).toFixed(2)}`, W - 210, 76);

    animRef.current = requestAnimationFrame(draw);
  }, [xi, view, showDESI]);

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
        <strong>17 — Expansion History: One Parameter Determines the Universe</strong>
        <span style={{ color: C.textDim, marginLeft: 12 }}>Paper 2</span>
      </div>
      <canvas ref={canvasRef} style={{ borderRadius: 8 }} />
      <div style={{ display: "flex", gap: 10, marginTop: 8, alignItems: "center", flexWrap: "wrap" }}>
        {["Hz", "ratio", "h0", "age"].map(v => (
          <button key={v} onClick={() => setView(v)}
            style={{
              background: view === v ? "rgba(60,120,200,0.3)" : "rgba(30,40,60,0.5)",
              color: C.text, border: `1px solid ${view === v ? "rgba(100,160,255,0.5)" : "rgba(60,80,120,0.3)"}`,
              borderRadius: 6, padding: "5px 12px", cursor: "pointer", fontFamily: "monospace", fontSize: 11,
            }}>
            {v === "Hz" ? "H(z)" : v === "ratio" ? "Ratio to ΛCDM" : v === "h0" ? "H₀ vs ξ" : "Age vs ξ"}
          </button>
        ))}
        <label style={{ color: C.gold, fontFamily: "monospace", fontSize: 13, display: "flex", alignItems: "center", gap: 6 }}>
          ξ: <input type="range" min={25} max={55} value={xi} onChange={e => setXi(+e.target.value)}
            style={{ width: 120 }} /> <strong>{(xi / 100).toFixed(2)}</strong>
        </label>
        {view === "ratio" && (
          <label style={{ color: C.textDim, fontFamily: "monospace", fontSize: 11 }}>
            <input type="checkbox" checked={showDESI} onChange={e => setShowDESI(e.target.checked)} /> DESI BAO points
          </label>
        )}
      </div>
    </div>
  );
}
