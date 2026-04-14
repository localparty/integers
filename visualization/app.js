// app.js — viewer logic
// Reads the global SHAPE_DATA from data.js (injected, not fetched) so this
// works under the file:// protocol without a server.
// ---------------------------------------------------------------------------

(function () {
  "use strict";

  const shapes = (typeof SHAPE_DATA !== "undefined" && SHAPE_DATA) || [];
  const N = shapes.length;
  const ARTIFACTS = (typeof ARTIFACT_BODIES !== "undefined" && ARTIFACT_BODIES) || {};
  const RUNG_NAMES = (typeof LADDER_NAMES !== "undefined" && LADDER_NAMES) || [
    "Strategy exists","Brief exists","X-Ray done","Compliance locked",
    "Bare locked","Full composed","Full locked","Zenodo published",
    "arXiv published","Journal published","Community accepted",
    "PROVED","UNIVERSALLY PROVED"
  ];

  const $ = (id) => document.getElementById(id);
  const slider      = $("shape-slider");
  const nameEl      = $("shape-name");
  const classEl     = $("shape-class");
  const positionEl  = $("shape-position");
  const canvas      = $("shape-canvas");
  const caption     = $("canvas-caption");
  const metricsEl   = $("metrics-panel");
  const footnotesEl = $("footnotes-panel");
  const buildInfo   = $("build-info");
  const pendingEl   = $("pending-counter");
  const shapeCount  = $("shape-counter");
  const prevBtn     = $("prev-btn");
  const nextBtn     = $("next-btn");
  const modalRoot   = $("modal-root");
  const modalBody   = $("modal-body");
  const modalTitle  = $("modal-title");
  const modalMeta   = $("modal-meta");

  if (slider) {
    slider.min = 0;
    slider.max = Math.max(0, N - 1);
    slider.value = 0;
  }

  if (buildInfo && typeof BUILD_TIMESTAMP !== "undefined") {
    buildInfo.textContent = "build " + BUILD_TIMESTAMP;
  }
  if (shapeCount) shapeCount.textContent = N + " shapes";
  if (pendingEl && typeof AUDIT_PENDING_COUNT !== "undefined") {
    pendingEl.textContent = AUDIT_PENDING_COUNT + " AUDIT PENDING";
  }

  // ---------- small SVG helpers ----------
  const SVG_NS = "http://www.w3.org/2000/svg";
  function svg(w, h, attrs) {
    let a = 'xmlns="' + SVG_NS + '" viewBox="0 0 ' + w + ' ' + h + '"';
    if (attrs) a += " " + attrs;
    return '<svg ' + a + '>';
  }
  const ESC = (s) => String(s).replace(/[&<>"']/g,
    (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));

  // Place N items around a circle centered at (cx,cy) radius r, starting at
  // angle0 (radians, default -pi/2 for top).
  function ringPoints(cx, cy, r, n, angle0) {
    const a0 = (angle0 === undefined) ? -Math.PI / 2 : angle0;
    const pts = [];
    for (let i = 0; i < n; i++) {
      const t = a0 + (2 * Math.PI * i) / n;
      pts.push({ x: cx + r * Math.cos(t), y: cy + r * Math.sin(t), angle: t });
    }
    return pts;
  }

  // ===========================================================================
  //   RENDERING — one function per class
  // ===========================================================================
  function auditPendingOverlay(W, H) {
    return (
      '<g class="pending-overlay">' +
      '  <rect x="' + (W/2 - 130) + '" y="' + (H/2 + 130) + '" width="260" height="36" rx="4" ' +
      '        fill="rgba(239,68,68,0.12)" stroke="#ef4444" stroke-width="1.2"/>' +
      '  <text x="' + (W/2) + '" y="' + (H/2 + 155) + '" text-anchor="middle">AUDIT PENDING</text>' +
      '</g>'
    );
  }

  function renderECircle(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2, r = 180;
    const faces = shape.faces || [];
    const pts = ringPoints(cx, cy, r, faces.length);
    let out = svg(W, H);
    // full-shape click zone (transparent rect over the canvas)
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // circle
    out += '<circle class="ecircle" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    // center label
    out += '<text x="' + cx + '" y="' + cy + '" text-anchor="middle" ' +
           'style="font-size:18px;fill:#7dd3fc" class="label-sans">S&#185;</text>';
    out += '<text x="' + cx + '" y="' + (cy + 22) + '" text-anchor="middle" fill="#a0a0b0">R &#8776; 10.10 &#956;m</text>';
    // face markers
    pts.forEach((p, i) => {
      out += '<g class="face-group" data-face="' + faces[i] + '">';
      out += '  <rect class="face-marker" x="' + (p.x - 9) + '" y="' + (p.y - 9) + '" ' +
             '        width="18" height="18" rx="3"/>';
      // Label position just outside the circle
      const lx = cx + (r + 30) * Math.cos(p.angle);
      const ly = cy + (r + 30) * Math.sin(p.angle) + 4;
      let anchor = "middle";
      if (Math.cos(p.angle) > 0.3) anchor = "start";
      else if (Math.cos(p.angle) < -0.3) anchor = "end";
      const conj = (shape.faceConjectures || {})[faces[i]] || "";
      out += '  <text class="face-label" x="' + lx + '" y="' + ly +
             '" text-anchor="' + anchor + '">' + ESC(faces[i]) + '</text>';
      out += '  <text class="face-label" x="' + lx + '" y="' + (ly + 12) +
             '" text-anchor="' + anchor + '" style="fill:#fbbf24">' + ESC(conj) + '</text>';
      out += '</g>';
    });
    out += '</svg>';
    return out;
  }

  function renderBouquet(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2;
    const rings = shape.rings || [];
    const pts = ringPoints(cx, cy, 170, rings.length);
    let out = svg(W, H);
    // Background click-zone (opens bouquet aggregate); individual rings
    // have their own data-jump-to zones on top.
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // lines from center to each ring
    pts.forEach(p => {
      out += '<line x1="' + cx + '" y1="' + cy + '" x2="' + p.x + '" y2="' + p.y +
             '" stroke="#262636" stroke-width="1"/>';
    });
    // each ring as a small circle — clickable
    pts.forEach((p, i) => {
      const rr = (i === 0) ? 60 : 40;
      const label = rings[i] || "";
      // Resolve ring label to a target shape
      const target = resolveBouquetTarget(label);
      const clickAttr = target != null ?
        ' data-jump-to="' + target + '" class="click-wrap"' : '';
      out += '<g' + clickAttr + '>';
      out += '<circle class="halo" cx="' + p.x + '" cy="' + p.y + '" r="' + rr + '"/>';
      out += '<circle class="click-halo" cx="' + p.x + '" cy="' + p.y + '" r="' + (rr+4) +
             '" fill="none" stroke="#7dd3fc" stroke-width="1.5"/>';
      const dash  = label.indexOf("—");
      const head  = (dash > 0) ? label.slice(0, dash).trim() : label;
      const tail  = (dash > 0) ? label.slice(dash + 1).trim() : "";
      out += '<text x="' + p.x + '" y="' + p.y + '" text-anchor="middle" ' +
             'fill="#e0e0e0" style="font-size:11px">' + ESC(head) + '</text>';
      if (tail) {
        out += '<text x="' + p.x + '" y="' + (p.y + 14) +
               '" text-anchor="middle" fill="#a0a0b0" style="font-size:10px">' +
               ESC(tail) + '</text>';
      }
      out += '</g>';
    });
    // central node — clickable (jumps to Core QG5D, pos 3)
    out += '<g data-jump-to="3" class="click-wrap">';
    out += '<circle class="click-halo" cx="' + cx + '" cy="' + cy + '" r="40" fill="none" stroke="#7dd3fc" stroke-width="1.5"/>';
    out += '<circle cx="' + cx + '" cy="' + cy + '" r="34" fill="#12121a" stroke="#7dd3fc" stroke-width="2"/>';
    out += '<text x="' + cx + '" y="' + (cy + 5) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc">QG5D</text>';
    out += '</g>';
    out += '</svg>';
    return out;
  }

  // Given a bouquet ring label, return the 1-based slider position of the
  // matching shape, or null.
  function resolveBouquetTarget(label) {
    const lo = label.toLowerCase();
    // Outer ring -> outer-ring-whole (position 43)
    if (lo.startsWith("outer")) return 43;
    // Branch A/B/C/D/E — match by innerRing key
    const tag = label.replace("—", "-").toLowerCase();
    const innerMap = {
      "branch a": 4, "branch b": 5, "branch c": 6, "branch d": 7, "branch e": 8,
    };
    for (const [k, pos] of Object.entries(innerMap)) {
      if (tag.includes(k)) return pos;
    }
    return null;
  }

  function renderCore(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2;
    const N_th = shape.theoremCount || 22;
    const pts = ringPoints(cx, cy, 200, N_th);
    let out = svg(W, H);
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // halo
    out += '<circle class="halo" cx="' + cx + '" cy="' + cy + '" r="220"/>';
    // each theorem dot
    pts.forEach((p, i) => {
      out += '<circle cx="' + p.x + '" cy="' + p.y + '" r="5" fill="#7dd3fc"/>';
      out += '<text x="' + p.x + '" y="' + (p.y - 10) +
             '" text-anchor="middle" style="font-size:9px;fill:#a0a0b0">T' + (i+1) + '</text>';
    });
    // Central point
    out += '<circle cx="' + cx + '" cy="' + cy + '" r="14" fill="#7dd3fc"/>';
    out += '<text x="' + cx + '" y="' + (cy + 40) + '" text-anchor="middle" class="label-sans" fill="#e0e0e0">Core QG5D</text>';
    out += '<text x="' + cx + '" y="' + (cy + 58) + '" text-anchor="middle" fill="#a0a0b0">M&#8309; = M&#8308; &times; S&#185;</text>';
    out += '<text x="' + cx + '" y="' + (cy + 76) + '" text-anchor="middle" fill="#a0a0b0">' + N_th + ' theorems proved</text>';
    out += '</svg>';
    return out;
  }

  function renderInnerRing(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2, r = 180;
    const n = shape.itemCount || 8;
    const pts = ringPoints(cx, cy, r, n);
    let out = svg(W, H);
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    out += '<circle class="ring" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    pts.forEach((p) => {
      out += '<circle cx="' + p.x + '" cy="' + p.y + '" r="6" fill="#7dd3fc"/>';
    });
    // center block
    out += '<text x="' + cx + '" y="' + (cy - 10) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc">' +
           ESC(shape.name) + '</text>';
    out += '<text x="' + cx + '" y="' + (cy + 14) + '" text-anchor="middle" fill="#a0a0b0">' + n + ' items</text>';
    if (shape.status === "AUDIT PENDING") out += auditPendingOverlay(W, H);
    out += '</svg>';
    return out;
  }

  function renderProjectionOp(shape) {
    const W = 640, H = 560;
    let out = svg(W, H);
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // 5D cube on left
    const cx = 150, cy = 250, s = 100, d = 40;
    const pts = [
      [cx - s/2,  cy - s/2],       [cx + s/2,  cy - s/2],
      [cx + s/2,  cy + s/2],       [cx - s/2,  cy + s/2],
      [cx - s/2 + d,  cy - s/2 - d], [cx + s/2 + d,  cy - s/2 - d],
      [cx + s/2 + d,  cy + s/2 - d], [cx - s/2 + d,  cy + s/2 - d],
    ];
    const path = (a, b) => '<line class="cube-wire" x1="' + pts[a][0] +
      '" y1="' + pts[a][1] + '" x2="' + pts[b][0] + '" y2="' + pts[b][1] + '"/>';
    // front square
    out += path(0,1) + path(1,2) + path(2,3) + path(3,0);
    // back square
    out += path(4,5) + path(5,6) + path(6,7) + path(7,4);
    // depth edges
    out += path(0,4) + path(1,5) + path(2,6) + path(3,7);
    out += '<text x="' + cx + '" y="' + (cy + 90) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc">5D</text>';
    out += '<text x="' + cx + '" y="' + (cy + 108) + '" text-anchor="middle" fill="#a0a0b0">M&#8308; &times; S&#185;</text>';

    // arrow
    const ax = 260, ay = cy - 10, bx = 410, by = cy - 10;
    out += '<line class="arrow" x1="' + ax + '" y1="' + ay + '" x2="' + bx + '" y2="' + by + '"/>';
    out += '<polygon fill="#fbbf24" points="' + bx + ',' + by + ' ' + (bx-10) + ',' + (by-5) + ' ' + (bx-10) + ',' + (by+5) + '"/>';
    out += '<text x="' + ((ax+bx)/2) + '" y="' + (ay - 10) + '" text-anchor="middle" class="label-sans" fill="#fbbf24">' +
           ESC(shape.projector || "P_X") + '</text>';

    // 4D shadow square
    const sx = 470, sy = 220, sw = 120, sh = 80;
    out += '<rect class="shadow-box" x="' + sx + '" y="' + sy + '" width="' + sw + '" height="' + sh + '"/>';
    out += '<text x="' + (sx + sw/2) + '" y="' + (sy + sh/2 + 4) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc">4D</text>';
    out += '<text x="' + (sx + sw/2) + '" y="' + (sy + sh + 18) + '" text-anchor="middle" fill="#a0a0b0">shadow</text>';

    // caption of what is preserved
    const preserve = {
      "P_A": "observable: H, {A,B}=iħ",
      "P_B": "gauge: mass gap &#916;_&#8734; > 0",
      "P_C": "cosmic: H_0, N_eff, t_0",
      "P_D": "CBB: modular flow (KMS)",
      "P_E": "spectral: 36 pins (Riemann)",
      "P_O": "conjecture: outer ring",
    }[shape.projector] || "";
    out += '<text x="' + W/2 + '" y="420" text-anchor="middle" fill="#e0e0e0" class="label-sans">preserves: ' + preserve + '</text>';
    const forget = {
      "P_A": "forgets: KK gap",
      "P_B": "forgets: 4D observables",
      "P_C": "forgets: strong-coupling",
      "P_D": "forgets: classical geometry",
      "P_E": "forgets: field content",
      "P_O": "forgets: internal structure",
    }[shape.projector] || "";
    out += '<text x="' + W/2 + '" y="444" text-anchor="middle" fill="#a0a0b0">' + forget + '</text>';
    out += '</svg>';
    return out;
  }

  function renderVerdictStack(dist, W, H, x, y) {
    // Vertical stacked bar.
    const total = (dist.total || (dist.PROVED + dist.PARTIAL + dist["OPEN-BUT-ADDRESSED"] + dist.SILENT)) || 1;
    const barH = H;
    const cls = ["proved", "partial", "open", "silent"];
    const counts = [dist.PROVED || 0, dist.PARTIAL || 0,
                    dist["OPEN-BUT-ADDRESSED"] || 0, dist.SILENT || 0];
    let out = "";
    let yy = y;
    for (let i = 0; i < 4; i++) {
      const h = barH * counts[i] / total;
      out += '<rect x="' + x + '" y="' + yy + '" width="' + W + '" height="' + h +
             '" class="verdict-seg verdict-' + cls[i] + '"/>';
      yy += h;
    }
    // overlay labels
    let yyy = y;
    for (let i = 0; i < 4; i++) {
      const h = barH * counts[i] / total;
      if (counts[i] > 0) {
        const txt = counts[i];
        out += '<text x="' + (x + W/2) + '" y="' + (yyy + h/2 + 4) +
               '" text-anchor="middle" style="font-size:10px;fill:#0a0a0f;font-weight:700">' + txt + '</text>';
      }
      yyy += h;
    }
    // frame
    out += '<rect x="' + x + '" y="' + y + '" width="' + W + '" height="' + barH +
           '" fill="none" stroke="#262636"/>';
    return out;
  }

  function renderRingVertex(shape) {
    const W = 640, H = 560, cx = W/2 - 60, cy = H/2, r = 150;
    let out = svg(W, H);
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // Main circle
    out += '<circle class="ecircle" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    // Vertex dot
    const cls = shape.millennium ? "vertex-dot millennium" : "vertex-dot";
    out += '<circle class="' + cls + '" cx="' + cx + '" cy="' + (cy - r) + '" r="10"/>';
    // Label in center
    out += '<text x="' + cx + '" y="' + (cy - 8) + '" text-anchor="middle" class="label-sans" style="font-size:22px;fill:#7dd3fc">' +
           ESC(shape.name) + '</text>';
    const paperShort = (shape.paper || "").replace("paper", "p");
    out += '<text x="' + cx + '" y="' + (cy + 14) + '" text-anchor="middle" fill="#a0a0b0">' + ESC(paperShort) + '</text>';
    if (shape.proofChainStatus) {
      const s = shape.proofChainStatus.length > 48 ?
                shape.proofChainStatus.slice(0, 48) + "…" : shape.proofChainStatus;
      out += '<text x="' + cx + '" y="' + (cy + 36) + '" text-anchor="middle" fill="#fbbf24" style="font-size:11px">' + ESC(s) + '</text>';
    }
    if (shape.millennium) {
      out += '<text x="' + cx + '" y="' + (cy + 56) + '" text-anchor="middle" fill="#a78bfa" style="font-size:10px;letter-spacing:0.08em;text-transform:uppercase">MILLENNIUM</text>';
    }

    // Verdict stacked bar on the right (if we have one)
    if (shape.verdictDist && shape.verdictDist.total) {
      const bx = cx + r + 90, by = cy - 130, bw = 28, bh = 260;
      out += renderVerdictStack(shape.verdictDist, bw, bh, bx, by);
      out += '<text x="' + (bx + bw/2) + '" y="' + (by - 10) + '" text-anchor="middle" fill="#e0e0e0" style="font-size:11px">verdicts</text>';
      out += '<text x="' + (bx + bw/2) + '" y="' + (by + bh + 18) + '" text-anchor="middle" fill="#a0a0b0" style="font-size:10px">' +
             shape.verdictDist.total + ' cells</text>';
    }

    // Primary face/projection badges
    if (shape.primary && shape.primary.face) {
      out += '<text x="60" y="30" fill="#a0a0b0" style="font-size:11px">primary face:</text>';
      out += '<text x="60" y="48" fill="#a78bfa" class="label-sans" style="font-size:14px">' +
             ESC(shape.primary.face) + '</text>';
    }
    if (shape.primary && shape.primary.projection) {
      out += '<text x="60" y="72" fill="#a0a0b0" style="font-size:11px">primary proj:</text>';
      out += '<text x="60" y="90" fill="#34d399" class="label-sans" style="font-size:14px">' +
             ESC(shape.primary.projection.replace(/\$/g, "")) + '</text>';
    }

    if (shape.status === "AUDIT PENDING") {
      out += auditPendingOverlay(W, H);
    }
    out += '</svg>';
    return out;
  }

  function classifyPin(i) {
    // Even though we don't have exact pin-to-domain data, we color by
    // position band: this is purely decorative — domains are listed in the
    // metrics panel with counts extracted from build.py.
    if (i < 10) return "pin-dot-cosmo";
    if (i < 18) return "pin-dot-qcd";
    if (i < 27) return "pin-dot-flavor";
    if (i < 32) return "pin-dot-ckm";
    return "pin-dot-other";
  }

  function render36Pin(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2, r = 200;
    const N_p = shape.pinCount || 36;
    const pts = ringPoints(cx, cy, r, N_p);
    let out = svg(W, H);
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    out += '<circle class="ecircle" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    pts.forEach((p, i) => {
      out += '<circle cx="' + p.x + '" cy="' + p.y + '" r="6" class="' + classifyPin(i) + '"/>';
      // Tick mark
      out += '<line x1="' + p.x + '" y1="' + p.y + '" x2="' +
             (cx + (r-12)*Math.cos(p.angle)) + '" y2="' +
             (cy + (r-12)*Math.sin(p.angle)) + '" stroke="#262636" stroke-width="1"/>';
      out += '<text x="' + (cx + (r+18)*Math.cos(p.angle)) + '" y="' +
             (cy + (r+18)*Math.sin(p.angle) + 4) +
             '" text-anchor="middle" style="font-size:9px;fill:#707088">#' + (i+1) + '</text>';
    });
    out += '<text x="' + cx + '" y="' + (cy-8) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc" style="font-size:24px">36 pins</text>';
    out += '<text x="' + cx + '" y="' + (cy+14) + '" text-anchor="middle" fill="#a0a0b0">sub-% predictions</text>';
    out += '<text x="' + cx + '" y="' + (cy+32) + '" text-anchor="middle" fill="#fbbf24" style="font-size:10px">0 free parameters</text>';
    // domain legend
    const legends = [
      ["pin-dot-cosmo", "cosmology"],
      ["pin-dot-qcd",   "QCD / flavour"],
      ["pin-dot-flavor","flavour"],
      ["pin-dot-ckm",   "CKM / PMNS"],
      ["pin-dot-other", "other"],
    ];
    legends.forEach((l, i) => {
      const ly = 30 + i * 18;
      out += '<circle cx="40" cy="' + ly + '" r="5" class="' + l[0] + '"/>';
      out += '<text x="52" y="' + (ly + 4) + '" fill="#a0a0b0" style="font-size:11px">' + l[1] + '</text>';
    });
    out += '</svg>';
    return out;
  }

  function renderChords(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2, r = 220;
    // 25 canonical vertex positions
    const order = [
      "qg5d", "ym", "rh", "grh", "lindelof", "bsd", "h12", "ns",
      "turbulence", "hodge", "baum-connes", "pvnp", "vp-vs-vnp",
      "bgs", "katz-sarnak", "twin-primes", "cramer", "goldbach",
      "abc", "opn", "collatz", "lehmer", "sato-tate", "schanuel",
      "hilbert-6",
    ];
    const pts = ringPoints(cx, cy, r, order.length);
    const idx = {};
    order.forEach((v, i) => idx[v] = i);

    let out = svg(W, H);
    // click on the center opens self (whole chord graph)
    out += '<rect data-open-self="1" x="' + (cx-60) + '" y="' + (cy-60) +
           '" width="120" height="120" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    out += '<circle class="ring" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';

    // chords
    const edges = shape.edges || [];
    edges.forEach(e => {
      const a = idx[e.from], b = idx[e.to];
      if (a === undefined || b === undefined) return;
      const pa = pts[a], pb = pts[b];
      // curved chord via quadratic Bezier through center offset
      const mx = (pa.x + pb.x) / 2, my = (pa.y + pb.y) / 2;
      // pull slightly toward center for visual curve
      const qx = cx + (mx - cx) * 0.25, qy = cy + (my - cy) * 0.25;
      out += '<path class="chord" d="M ' + pa.x + ' ' + pa.y +
             ' Q ' + qx + ' ' + qy + ' ' + pb.x + ' ' + pb.y + '"/>';
    });

    // vertex dots + labels — each clickable, jumps to that vertex's slider position
    pts.forEach((p, i) => {
      const v = order[i];
      const clss = (["ym","rh","bsd","ns","hodge","pvnp"].includes(v)) ?
                    "vertex-dot millennium" : "vertex-dot";
      const pos = positionForVertex(v);
      const hookAttr = pos != null ? ' data-jump-to="' + pos + '" class="click-wrap"' : '';
      out += '<g' + hookAttr + '>';
      out += '<circle class="click-halo" cx="' + p.x + '" cy="' + p.y + '" r="12" fill="none" stroke="#7dd3fc"/>';
      out += '<circle class="' + clss + '" cx="' + p.x + '" cy="' + p.y + '" r="5"/>';
      const lx = cx + (r + 18) * Math.cos(p.angle);
      const ly = cy + (r + 18) * Math.sin(p.angle) + 3;
      let anchor = "middle";
      if (Math.cos(p.angle) > 0.3) anchor = "start";
      else if (Math.cos(p.angle) < -0.3) anchor = "end";
      out += '<text x="' + lx + '" y="' + ly + '" text-anchor="' + anchor +
             '" style="font-size:9px;fill:#a0a0b0">' + ESC(v) + '</text>';
      out += '</g>';
    });

    out += '<text x="' + cx + '" y="' + (cy - 10) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc" style="font-size:20px">chord graph</text>';
    out += '<text x="' + cx + '" y="' + (cy + 14) + '" text-anchor="middle" fill="#a0a0b0" style="font-size:12px">' +
           edges.length + ' cross-cuts (atlas run-01)</text>';
    out += '</svg>';
    return out;
  }

  // Find the 1-based slider position for a vertex key. Memoized lookup.
  const _posByVertex = (function() {
    const m = {};
    shapes.forEach(s => {
      if (s.vertex) m[s.vertex] = s.position;
      if (s.name === "Core QG5D") m["qg5d"] = s.position;
    });
    return m;
  })();
  function positionForVertex(v) { return _posByVertex[v] || null; }

  function renderFaces(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2, r = 210;
    const faces = shape.faces || [];
    const pts = ringPoints(cx, cy, r, faces.length);
    const adj = shape.adjacency || [];
    const posByFace = {};
    faces.forEach((f, i) => posByFace[f] = pts[i]);

    let out = svg(W, H);
    out += '<rect data-open-self="1" x="' + (cx-40) + '" y="' + (cy-40) +
           '" width="80" height="80" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // adjacency edges
    adj.forEach(pair => {
      const a = posByFace[pair[0]], b = posByFace[pair[1]];
      if (!a || !b) return;
      out += '<line x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y +
             '" stroke="#fbbf24" stroke-opacity="0.5" stroke-width="1.2"/>';
    });
    // face nodes — clickable, jumps to the canonical conjecture shape
    const canonicalFaceVertex = {
      "TOPOLOGY": "lehmer", "DYNAMICS": "cramer", "HARMONICS": "collatz",
      "MEASURE": "sato-tate", "AMPLITUDE": "lindelof", "SYMMETRY": "katz-sarnak",
      "CURVATURE": "ym", "ARITHMETIC": "goldbach", "RESONANCE": "rh",
      "SPREAD": "bgs",
    };
    pts.forEach((p, i) => {
      const face = faces[i];
      const target = positionForVertex(canonicalFaceVertex[face]);
      const hookAttr = target != null ? ' data-jump-to="' + target + '" class="click-wrap"' : '';
      out += '<g' + hookAttr + '>';
      out += '<circle class="click-halo" cx="' + p.x + '" cy="' + p.y + '" r="24" fill="none" stroke="#a78bfa"/>';
      out += '<circle cx="' + p.x + '" cy="' + p.y + '" r="18" fill="#12121a" stroke="#a78bfa" stroke-width="2"/>';
      out += '<text x="' + p.x + '" y="' + (p.y + 4) +
             '" text-anchor="middle" style="font-size:9px;fill:#e0e0e0">' + ESC(face.slice(0,4)) + '</text>';
      const lx = cx + (r + 30) * Math.cos(p.angle);
      const ly = cy + (r + 30) * Math.sin(p.angle) + 4;
      let anchor = "middle";
      if (Math.cos(p.angle) > 0.3) anchor = "start";
      else if (Math.cos(p.angle) < -0.3) anchor = "end";
      out += '<text x="' + lx + '" y="' + ly + '" text-anchor="' + anchor +
             '" fill="#a0a0b0" style="font-size:10px">' + ESC(face) + '</text>';
      out += '</g>';
    });
    out += '<text x="' + cx + '" y="' + (cy + 4) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc" style="font-size:18px">10 faces</text>';
    out += '</svg>';
    return out;
  }

  function renderSouthTrough(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2;
    const a = 230, b = 150;  // wide, short
    let out = svg(W, H);
    out += '<rect data-open-self="1" x="0" y="0" width="' + W + '" height="' + H +
           '" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    // Trough shade under south of ellipse
    out += '<path class="trough-shade" d="M ' + (cx - a) + ' ' + cy +
           ' A ' + a + ' ' + b + ' 0 0 0 ' + (cx + a) + ' ' + cy +
           ' L ' + (cx + a) + ' ' + (cy + b) +
           ' L ' + (cx - a) + ' ' + (cy + b) + ' Z"/>';
    // Ellipse
    out += '<ellipse class="ellipse-curve" cx="' + cx + '" cy="' + cy + '" rx="' + a + '" ry="' + b + '"/>';
    // North pole ring of complete work
    const north = shape.northVertices || [];
    const south = shape.southVertices || [];
    // Draw north nodes along top half
    north.forEach((v, i) => {
      const t = -Math.PI/2 + (i - (north.length-1)/2) * (Math.PI/12);
      const x = cx + a * Math.cos(t), y = cy + b * Math.sin(t);
      out += '<circle cx="' + x + '" cy="' + y + '" r="7" fill="#7dd3fc"/>';
      out += '<text x="' + x + '" y="' + (y - 10) + '" text-anchor="middle" fill="#7dd3fc" style="font-size:10px">' + ESC(v) + '</text>';
    });
    south.forEach((v, i) => {
      const t = Math.PI/2 + (i - (south.length-1)/2) * (Math.PI/12);
      const x = cx + a * Math.cos(t), y = cy + b * Math.sin(t);
      out += '<circle cx="' + x + '" cy="' + y + '" r="7" fill="#ef4444"/>';
      out += '<text x="' + x + '" y="' + (y + 16) + '" text-anchor="middle" fill="#ef4444" style="font-size:10px">' + ESC(v) + '</text>';
    });
    // Labels
    out += '<text x="' + cx + '" y="' + (cy - b - 20) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc">NORTH POLE</text>';
    out += '<text x="' + cx + '" y="' + (cy - b - 4) + '" text-anchor="middle" fill="#a0a0b0" style="font-size:11px">completed work (protect)</text>';
    out += '<text x="' + cx + '" y="' + (cy + b + 30) + '" text-anchor="middle" class="label-sans" fill="#ef4444">SOUTH TROUGH</text>';
    out += '<text x="' + cx + '" y="' + (cy + b + 46) + '" text-anchor="middle" fill="#a0a0b0" style="font-size:11px">unthickened frontier (focus)</text>';
    out += '</svg>';
    return out;
  }

  function renderOuterRing(shape) {
    const W = 640, H = 560, cx = W/2, cy = H/2, r = 220;
    const order = shape.vertexOrder || [];
    const pts = ringPoints(cx, cy, r, order.length);

    let out = svg(W, H);
    out += '<rect data-open-self="1" x="' + (cx-60) + '" y="' + (cy-60) +
           '" width="120" height="120" fill="rgba(0,0,0,0)" style="cursor:pointer"/>';
    out += '<circle class="ring" cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    // Meta closure edge from #25 back to #1
    const a = pts[0], b = pts[pts.length - 1];
    out += '<path class="chord" d="M ' + a.x + ' ' + a.y + ' Q ' + cx + ' ' + cy + ' ' + b.x + ' ' + b.y + '" stroke="#a78bfa" stroke-opacity="0.7"/>';

    // simple skeleton of cross-cuts (visual only)
    const skeleton = [
      [1,2], [1,11], [1,6], [1,8], [2,3], [2,4], [2,16],
      [5,9], [7,10], [11,12], [14,15], [17,18], [19,20], [20,22],
    ];
    skeleton.forEach(e => {
      if (pts[e[0]] && pts[e[1]]) {
        out += '<line x1="' + pts[e[0]].x + '" y1="' + pts[e[0]].y + '" x2="' +
               pts[e[1]].x + '" y2="' + pts[e[1]].y +
               '" class="chord"/>';
      }
    });

    pts.forEach((p, i) => {
      const v = order[i];
      const mc = ["ym","rh","bsd","ns","hodge","pvnp"].includes(v);
      const target = positionForVertex(v);
      const hookAttr = target != null ? ' data-jump-to="' + target + '" class="click-wrap"' : '';
      out += '<g' + hookAttr + '>';
      out += '<circle class="click-halo" cx="' + p.x + '" cy="' + p.y + '" r="14" fill="none" stroke="#7dd3fc"/>';
      out += '<circle class="vertex-dot' + (mc ? " millennium" : "") +
             '" cx="' + p.x + '" cy="' + p.y + '" r="6"/>';
      const lx = cx + (r + 22) * Math.cos(p.angle);
      const ly = cy + (r + 22) * Math.sin(p.angle) + 4;
      let anchor = "middle";
      if (Math.cos(p.angle) > 0.3) anchor = "start";
      else if (Math.cos(p.angle) < -0.3) anchor = "end";
      out += '<text x="' + lx + '" y="' + ly + '" text-anchor="' + anchor +
             '" style="font-size:10px;fill:#a0a0b0">' + ESC(v) + '</text>';
      out += '</g>';
    });
    out += '<text x="' + cx + '" y="' + (cy - 6) + '" text-anchor="middle" class="label-sans" fill="#7dd3fc" style="font-size:20px">outer ring</text>';
    out += '<text x="' + cx + '" y="' + (cy + 14) + '" text-anchor="middle" fill="#a0a0b0" style="font-size:12px">25 vertices &middot; P_O projection</text>';
    out += '</svg>';
    return out;
  }

  // ---------------------------------------------------------------------
  function renderSVG(shape) {
    switch (shape.class) {
      case "e-circle":            return renderECircle(shape);
      case "bouquet":             return renderBouquet(shape);
      case "core":                return renderCore(shape);
      case "inner-ring":          return renderInnerRing(shape);
      case "projection-operator": return renderProjectionOp(shape);
      case "ring-vertex":         return renderRingVertex(shape);
      case "36-pin":              return render36Pin(shape);
      case "chord-graph":         return renderChords(shape);
      case "face-graph":          return renderFaces(shape);
      case "south-trough":        return renderSouthTrough(shape);
      case "outer-ring-whole":    return renderOuterRing(shape);
      default:
        return '<div style="padding:40px;color:#a0a0b0">No renderer for class: ' +
          ESC(shape.class) + '</div>';
    }
  }

  // ===========================================================================
  //   METRICS + FOOTNOTES
  // ===========================================================================

  function pct(n, d) {
    if (!d) return "–";
    return (100 * n / d).toFixed(1) + "%";
  }

  function renderVerdictLegend(dist) {
    if (!dist || !dist.total) return "";
    const total = dist.total;
    const segs = [
      ["PROVED",            "proved",   dist.PROVED || 0],
      ["PARTIAL",           "partial",  dist.PARTIAL || 0],
      ["OPEN-BUT-ADDRESSED","open",     dist["OPEN-BUT-ADDRESSED"] || 0],
      ["SILENT",            "silent",   dist.SILENT || 0],
    ];
    let bar = '<div class="verdict-bar">';
    segs.forEach(s => {
      const w = 100 * s[2] / total;
      bar += '<div class="verdict-seg verdict-' + s[1] +
             '" style="width:' + w + '%">' + (w > 8 ? s[2] : "") + '</div>';
    });
    bar += '</div>';
    let legend = '<div class="verdict-legend">';
    segs.forEach(s => {
      legend += '<div><span class="swatch verdict-' + s[1] + '"></span>' +
        '<span>' + s[0] + '</span>' +
        '<span style="color:#707088;margin-left:6px">' + s[2] +
        ' &middot; ' + pct(s[2], total) + '</span></div>';
    });
    legend += '</div>';
    return bar + legend;
  }

  function renderHistRow(label, val, maxv, className) {
    const w = maxv ? (100 * val / maxv) : 0;
    const cls = "hist-bar" + (val === 0 ? " zero" : "");
    return '<div class="' + cls + '">' +
      '<span class="hist-label">' + ESC(label) + '</span>' +
      '<span><span class="hist-fill ' + (className || "") + '" style="width:' + w + '%;display:inline-block;"></span></span>' +
      '<span class="hist-count">' + val + '</span>' +
      '</div>';
  }

  function renderFaceHistogram(hist) {
    if (!hist) return "";
    const keys = ["TOPOLOGY","DYNAMICS","HARMONICS","MEASURE","AMPLITUDE",
                  "SYMMETRY","CURVATURE","ARITHMETIC","RESONANCE","SPREAD"];
    const mx = Math.max(...keys.map(k => hist[k] || 0), 1);
    let out = '';
    keys.forEach(k => {
      out += renderHistRow(k, hist[k] || 0, mx, "face-" + k);
    });
    return out;
  }

  function renderProjHistogram(hist) {
    if (!hist) return "";
    const keys = ["P_A","P_B","P_C","P_D","P_E","P_O"];
    const mx = Math.max(...keys.map(k => hist[k] || 0), 1);
    let out = '';
    keys.forEach(k => {
      out += renderHistRow(k, hist[k] || 0, mx, "proj-" + k.replace("_",""));
    });
    return out;
  }

  function renderMetricsPanel(shape) {
    let h = "";
    h += '<h2>' + ESC(shape.name);
    if (shape.millennium) h += ' <span class="badge millennium">Millennium</span>';
    if (shape.status === "AUDIT PENDING") h += ' <span class="badge pending">Audit pending</span>';
    if (shape.sourceType === "Clay-Official") h += ' <span class="badge clay">Clay-Official</span>';
    h += '</h2>';

    const paperRef = shape.paper ? shape.paper : "–";
    h += '<div class="paper-ref">paper: ' + ESC(paperRef);
    if (shape.xRayPath) h += '<br>x-ray: ' + ESC(shape.xRayPath);
    if (shape.strategyDir) h += '<br>strategy: ' + ESC(shape.strategyDir);
    if (shape.latestRun) h += '<br>run: ' + ESC(shape.latestRun);
    h += '</div>';

    // Core metrics
    const rows = [];
    if (shape.sourceType) rows.push(["source type", shape.sourceType]);
    if (shape.nRequirements) rows.push(["requirements N", shape.nRequirements]);
    if (shape.matrixM && shape.matrixN)
      rows.push(["matrix size", shape.matrixM + " &times; " + shape.matrixN]);
    if (shape.proofChainLayers) rows.push(["chain layers", shape.proofChainLayers]);
    if (shape.proofChainStatus) rows.push(["chain status", shape.proofChainStatus]);
    if (shape.bareLineCount) rows.push(["bare lines", shape.bareLineCount]);
    if (shape.bareTheoremCount) rows.push(["bare theorems", shape.bareTheoremCount]);
    if (shape.bareDefinitionCount) rows.push(["bare definitions", shape.bareDefinitionCount]);
    if (shape.beyondLineCount) rows.push(["beyond lines", shape.beyondLineCount]);
    if (shape.crossCutCount) rows.push(["cross-cuts", shape.crossCutCount]);
    if (shape.primary && shape.primary.face) rows.push(["primary face", shape.primary.face]);
    if (shape.primary && shape.primary.projection) rows.push(["primary proj", shape.primary.projection.replace(/\$/g,"")]);
    if (shape.primary && shape.primary.branch) rows.push(["primary branch", shape.primary.branch]);
    if (shape.theoremCount) rows.push(["theorems (core)", shape.theoremCount]);
    if (shape.predictionCount) rows.push(["predictions", shape.predictionCount]);
    if (shape.pinCount) rows.push(["pins", shape.pinCount]);
    if (shape.edgeCount) rows.push(["chord edges", shape.edgeCount]);
    if (shape.radiusMicrons) rows.push(["radius R", shape.radiusMicrons + " &micro;m"]);

    if (rows.length) {
      h += '<dl class="metrics-row">';
      rows.forEach(r => {
        h += '<dt>' + r[0] + '</dt><dd>' + r[1] + '</dd>';
      });
      h += '</dl>';
    }

    // Verdict distribution
    if (shape.verdictDist && shape.verdictDist.total) {
      h += '<h3>verdict distribution</h3>';
      h += renderVerdictLegend(shape.verdictDist);
    }

    // Histograms
    if (shape.faceHistogram) {
      h += '<h3>face histogram</h3>';
      h += renderFaceHistogram(shape.faceHistogram);
    }
    if (shape.projectionHistogram) {
      h += '<h3>projection histogram</h3>';
      h += renderProjHistogram(shape.projectionHistogram);
    }

    // Pin domains
    if (shape.pinDomains) {
      h += '<h3>pin domains</h3>';
      const max = Math.max(...Object.values(shape.pinDomains), 1);
      Object.entries(shape.pinDomains).forEach(([k,v]) => {
        h += renderHistRow(k, v, max, "");
      });
    }

    // Progress ladder
    if (shape.ladder && shape.ladder.length) {
      h += '<h3>progress ladder</h3>';
      h += renderLadder(shape.ladder, shape.ladderDetections || {});
    }

    // Mode toggles
    if (shape.artifacts && Object.keys(shape.artifacts).length) {
      h += '<h3>mode toggles</h3>';
      h += renderModeToggles(shape.artifacts);
    }

    return h;
  }

  // ---------------- ladder rendering ----------------
  function renderLadder(ladder, detections) {
    let highest = -1;
    for (let i = 0; i < ladder.length; i++) {
      if (ladder[i]) highest = i;
    }
    let out = '<div class="ladder-block"><div class="ladder">';
    for (let i = 0; i < 13; i++) {
      const name = RUNG_NAMES[i] || ("Rung " + (i+1));
      const reached = !!ladder[i];
      const current = (i === highest);
      let cls = "ladder-rung";
      if (current) cls += " current";
      else if (reached) cls += " reached";
      const det = detections[(i+1) + ""];
      const tip = (i+1) + ". " + name + (reached ? " ✓" : " (not reached)") +
                  (det ? " — " + det : "");
      out += '<span class="' + cls + '" data-rung="' + (i+1) +
             '" title="' + ESC(tip) + '"></span>';
    }
    out += '</div><div class="ladder-caption">';
    if (highest >= 0) {
      out += '<span class="current-label">' + (highest+1) + '. ' +
             ESC(RUNG_NAMES[highest]) + '</span>';
      out += '<span>' + (highest+1) + '/13</span>';
    } else {
      out += '<span>— no rungs reached —</span><span>0/13</span>';
    }
    out += '</div></div>';
    return out;
  }

  // ---------------- mode toggle buttons ----------------
  function renderModeToggles(artifacts) {
    const modes = [
      ["bare", "Bare"],
      ["full", "Full"],
      ["compliance", "Compliance"],
      ["strategy", "Strategy"],
      ["x-ray", "X-Ray"],
      ["beyond-bare", "Beyond-Bare"],
      ["beyond-full", "Beyond-Full"],
    ];
    let out = '<div class="mode-toggles">';
    modes.forEach(([key, label]) => {
      const path = artifacts[key];
      if (path) {
        out += '<button type="button" class="mode-btn" ' +
               'data-mode-artifact="' + ESC(path) + '" ' +
               'data-mode-label="' + ESC(label) + '">' + label + '</button>';
      } else {
        out += '<button type="button" class="mode-btn" disabled title="artifact not present">' +
               label + '</button>';
      }
    });
    out += '</div>';
    return out;
  }

  function renderFootnotesPanel(shape) {
    let h = "";

    const desc = shape.description || shape.proofChainDescription || "";
    if (desc) {
      h += '<h3>description</h3>';
      h += '<p class="prose">' + ESC(desc) + '</p>';
    }

    if (shape.label) {
      h += '<h3>label</h3>';
      h += '<p class="prose">' + ESC(shape.label) + '</p>';
    }

    // Requirements list
    if (shape.nItems && shape.nItems.length) {
      h += '<h3>' + shape.nItems.length + ' requirements</h3>';
      h += '<ol>';
      shape.nItems.forEach(n => { h += '<li>' + ESC(n) + '</li>'; });
      h += '</ol>';
    }

    // Named walls
    if (shape.namedWalls && shape.namedWalls.length) {
      h += '<h3>named walls</h3>';
      h += '<ul>';
      shape.namedWalls.forEach(w => {
        h += '<li><strong>' + ESC(w.name) + '</strong>';
        if (w.status) h += ' — <em>' + ESC(w.status) + '</em>';
        if (w.bypass) h += ' — ' + ESC(w.bypass);
        h += '</li>';
      });
      h += '</ul>';
    }

    // Programme files
    const files = [];
    if (shape.paper) files.push(shape.paper);
    if (shape.paper && shape.class === "ring-vertex") files.push(shape.paper + "/PROOF-CHAIN.md");
    if (shape.strategyDir) files.push(shape.strategyDir + "/00-millenium-strategy.md");
    if (shape.strategyDir && shape.latestRun) {
      files.push(shape.strategyDir + "/pac-output/runs/" + shape.latestRun + "/compliance-map.md");
    }
    if (shape.xRayPath) files.push(shape.xRayPath);
    if (shape.pinTableRef) files.push(shape.pinTableRef);
    if (shape.crossCutRef) files.push(shape.crossCutRef);
    if (shape.sectionRef) files.push(shape.sectionRef);
    // de-dup preserving order
    const seen = new Set();
    const uniq = [];
    files.forEach(f => { if (f && !seen.has(f)) { seen.add(f); uniq.push(f); } });
    if (uniq.length) {
      h += '<h3>programme files</h3>';
      h += '<ul>';
      uniq.forEach(f => { h += '<li><span class="file-link">' + ESC(f) + '</span></li>'; });
      h += '</ul>';
    }

    // Face/conjecture correspondence table for e-circle
    if (shape.faceConjectures) {
      h += '<h3>face &rarr; conjecture</h3>';
      h += '<ul>';
      Object.entries(shape.faceConjectures).forEach(([f, c]) => {
        h += '<li><strong>' + ESC(f) + '</strong> &mdash; ' + ESC(c) + '</li>';
      });
      h += '</ul>';
    }

    return h || '<p class="prose" style="color:#707088">(no footnotes)</p>';
  }

  // ===========================================================================
  //  MODAL (click-to-xray deep dive)
  // ===========================================================================

  function openModal(shape) {
    if (!shape) return;
    modalTitle.textContent = shape.name || "";
    const meta = [];
    if (shape.class) meta.push(shape.class);
    if (shape.paper) meta.push(shape.paper);
    if (shape.vertex) meta.push("vertex: " + shape.vertex);
    if (shape.position) meta.push("#" + shape.position);
    modalMeta.textContent = meta.join("  ·  ");

    let body = "";
    const isRingVertex = (shape.class === "ring-vertex");
    const isConnecting = ["bouquet", "outer-ring-whole", "chord-graph",
                          "face-graph", "inner-ring", "projection-operator",
                          "36-pin"].includes(shape.class);

    // Description
    const desc = shape.description || shape.proofChainDescription || "";
    if (desc) {
      body += '<details class="modal-section" open><summary>Description</summary>';
      body += '<p class="subsection" style="font-family:var(--sans);font-size:12.5px;color:var(--text);line-height:1.55">' + ESC(desc) + '</p>';
      body += '</details>';
    }

    if (isRingVertex) {
      body += renderModalRingVertex(shape);
    } else if (isConnecting) {
      body += renderModalAggregate(shape);
    } else if (shape.faceConjectures) {
      body += renderModalECircle(shape);
    } else if (shape.class === "core") {
      body += renderModalCore(shape);
    } else if (shape.class === "south-trough") {
      body += renderModalSouthTrough(shape);
    } else {
      body += '<p class="subsection" style="color:var(--text-2)">No deep-dive content available for this shape class.</p>';
    }

    modalBody.innerHTML = body;
    modalRoot.hidden = false;
    document.body.style.overflow = "hidden";
    // Scroll to top
    modalBody.scrollTop = 0;
  }

  function closeModal() {
    modalRoot.hidden = true;
    document.body.style.overflow = "";
  }

  function renderModalRingVertex(shape) {
    let h = "";

    // Theorems
    const thms = shape.theoremsDetailed || [];
    if (thms.length) {
      h += '<details class="modal-section" open><summary>Theorems ' +
           '<span class="count">(' + thms.length + ')</span></summary>';
      thms.forEach(t => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(t.kind || "Theorem") + ' ' + ESC(t.number || "") + '</span>';
        if (t.name) h += '<span class="label">' + ESC(t.name) + '</span>';
        if (t.statement) h += '<div class="sublabel">' + ESC(t.statement) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Requirements
    const reqs = shape.requirementsDetailed || [];
    if (reqs.length) {
      h += '<details class="modal-section" open><summary>Requirements ' +
           '<span class="count">(' + reqs.length + ')</span></summary>';
      reqs.forEach(r => {
        h += '<div class="item">';
        h += '<span class="tag">#' + ESC(r.n || "") + '</span>';
        h += '<span class="label">' + ESC(r.label || "") + '</span>';
        if (r.description) h += '<div class="sublabel">' + ESC(r.description) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Proof-chain layers
    const layers = shape.chainLayers || [];
    const xrayLayers = shape.layerXray || [];
    const xrayById = {};
    xrayLayers.forEach(x => { xrayById[x.id] = x; });
    if (layers.length) {
      h += '<details class="modal-section" open><summary>Proof-chain layers ' +
           '<span class="count">(' + layers.length + ')</span></summary>';
      layers.forEach(l => {
        const xr = xrayById["L" + l.id] || xrayById[l.id];
        const statusClass = statusKind(l.status);
        h += '<div class="item">';
        h += '<span class="tag">L' + ESC(l.id) + '</span>';
        if (l.status) h += '<span class="tag status ' + statusClass + '">' + ESC(l.status) + '</span>';
        h += '<span class="label">' + ESC(l.statement) + '</span>';
        if (l.depends && l.depends !== "--") h += '<div class="sublabel">depends on: ' + ESC(l.depends) + '</div>';
        if (xr) {
          const bits = [];
          if (xr.face) bits.push("face: " + xr.face.split(" ")[0]);
          if (xr.projection) bits.push("proj: " + xr.projection.split(" ")[0]);
          if (xr.pattern) bits.push("pat: " + xr.pattern.split(" ")[0]);
          if (xr.invariant) bits.push("inv: " + xr.invariant);
          if (bits.length) h += '<div class="sublabel">' + ESC(bits.join("  ·  ")) + '</div>';
        }
        h += '</div>';
      });
      h += '</details>';
    }

    // X-Ray face/projection/pattern per layer (if no chainLayers, show xrayLayers)
    if (!layers.length && xrayLayers.length) {
      h += '<details class="modal-section" open><summary>X-Ray layers ' +
           '<span class="count">(' + xrayLayers.length + ')</span></summary>';
      xrayLayers.forEach(x => {
        h += '<div class="item">';
        h += '<span class="tag">' + ESC(x.id) + '</span>';
        if (x.status) h += '<span class="tag status ' + statusKind(x.status) + '">' + ESC(x.status) + '</span>';
        h += '<span class="label">' + ESC(x.title) + '</span>';
        const bits = [];
        if (x.face) bits.push("face: " + x.face.split(" ")[0]);
        if (x.projection) bits.push("proj: " + x.projection.split(" ")[0]);
        if (x.pattern) bits.push("pat: " + x.pattern.split(" ")[0]);
        if (x.invariant) bits.push("inv: " + x.invariant);
        if (bits.length) h += '<div class="sublabel">' + ESC(bits.join("  ·  ")) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Named walls
    const walls = shape.namedWalls || [];
    if (walls.length) {
      h += '<details class="modal-section" open><summary>Named walls ' +
           '<span class="count">(' + walls.length + ')</span></summary>';
      walls.forEach(w => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(w.name || "") + '</span>';
        if (w.topic) h += '<span class="label">' + ESC(w.topic) + '</span>';
        if (w.status) h += '<div class="sublabel"><strong>Status:</strong> ' +
                           '<span class="tag status ' + statusKind(w.status) + '">' +
                           ESC(w.status) + '</span></div>';
        if (w.statement) h += '<div class="sublabel"><strong>Statement:</strong> ' + ESC(w.statement) + '</div>';
        if (w.bypass) h += '<div class="sublabel"><strong>Bypass:</strong> ' + ESC(w.bypass) + '</div>';
        if (w.confidence) h += '<div class="sublabel"><strong>Confidence:</strong> ' + ESC(w.confidence) + '</div>';
        if (w.audit_pending) h += '<div class="sublabel"><strong>Audit pending:</strong> ' + ESC(w.audit_pending) + '</div>';
        if (w.effect_pass) h += '<div class="sublabel"><strong>Effect if audit passes:</strong> ' + ESC(w.effect_pass) + '</div>';
        if (w.effect_fail) h += '<div class="sublabel"><strong>Effect if audit fails:</strong> ' + ESC(w.effect_fail) + '</div>';
        if (w.chain_location) h += '<div class="sublabel"><strong>Chain location:</strong> ' + ESC(w.chain_location) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Cross-cuts
    const ccs = shape.crossCutsDetailed || [];
    if (ccs.length) {
      h += '<details class="modal-section"><summary>Cross-cut edges ' +
           '<span class="count">(' + ccs.length + ')</span></summary>';
      ccs.forEach(e => {
        const targetPos = positionForVertex(e.from === shape.vertex ? e.to : e.from);
        h += '<div class="item">';
        h += '<span class="tag">' + ESC(e.from) + ':' + ESC(e.from_layer) + '</span>';
        h += ' ↔ ';
        if (targetPos) {
          h += '<a class="jump-link" data-jump-to="' + targetPos + '">' +
               ESC(e.to) + (e.to_layer ? ':' + ESC(e.to_layer) : "") + '</a>';
        } else {
          h += '<span>' + ESC(e.to) + (e.to_layer ? ':' + ESC(e.to_layer) : "") + '</span>';
        }
        if (e.shared) h += '<div class="sublabel">shared: ' + ESC(e.shared) + '</div>';
        if (e.reason) h += '<div class="sublabel">' + ESC(e.reason) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Bonus theorems
    const bonus = shape.bonusTheorems || [];
    if (bonus.length) {
      h += '<details class="modal-section"><summary>Bonus theorems (beyond bare) ' +
           '<span class="count">(' + bonus.length + ')</span></summary>';
      bonus.forEach(t => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(t.kind || "Theorem") + ' ' + ESC(t.number || "") + '</span>';
        if (t.name) h += '<span class="label">' + ESC(t.name) + '</span>';
        if (t.statement) h += '<div class="sublabel">' + ESC(t.statement) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Numbers table
    const nums = shape.numbersTable || [];
    if (nums.length) {
      h += '<details class="modal-section"><summary>Numbers table ' +
           '<span class="count">(' + nums.length + ')</span></summary>';
      nums.forEach(n => {
        h += '<div class="item">';
        h += '<span class="tag">#' + ESC(n.n) + '</span>';
        h += '<span class="label">' + ESC(n.quantity) + '</span>';
        h += '<div class="sublabel"><strong>Value:</strong> ' + ESC(n.value) + '</div>';
        if (n.citation) h += '<div class="sublabel"><strong>Citation:</strong> ' + ESC(n.citation) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    return h || '<p class="subsection" style="color:var(--text-2)">No deep-dive content collected for this vertex yet.</p>';
  }

  function renderModalAggregate(shape) {
    let h = "";

    // Connected nodes (with jump links)
    const nodes = shape.connectedNodes || [];
    if (nodes.length) {
      h += '<details class="modal-section" open><summary>Connected nodes ' +
           '<span class="count">(' + nodes.length + ')</span></summary>';
      nodes.forEach(n => {
        h += '<div class="item">';
        h += '<span class="tag">' + ESC(n.class) + '</span>';
        if (n.position) {
          h += '<a class="jump-link" data-jump-to="' + n.position + '">' + ESC(n.name) + '</a>';
        } else {
          h += '<span class="label">' + ESC(n.name) + '</span>';
        }
        if (n.vertex) h += '<span class="src">(' + ESC(n.vertex) + ')</span>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Cross-cut edges (for chord graph)
    const ccAll = shape.aggregatedCrossCutsAll;
    if (ccAll && ccAll.length) {
      h += '<details class="modal-section" open><summary>All cross-cut edges ' +
           '<span class="count">(' + ccAll.length + ')</span></summary>';
      ccAll.forEach(e => {
        const fromPos = positionForVertex(e.from);
        const toPos = positionForVertex(e.to);
        h += '<div class="item">';
        if (fromPos) h += '<a class="jump-link" data-jump-to="' + fromPos + '">' + ESC(e.from) + '</a>';
        else h += ESC(e.from);
        h += ':' + ESC(e.from_layer) + ' ↔ ';
        if (toPos) h += '<a class="jump-link" data-jump-to="' + toPos + '">' + ESC(e.to) + '</a>';
        else h += ESC(e.to);
        if (e.to_layer) h += ':' + ESC(e.to_layer);
        if (e.shared) h += '<div class="sublabel">shared: ' + ESC(e.shared) + '</div>';
        if (e.reason) h += '<div class="sublabel">' + ESC(e.reason) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Face → vertices (for face-graph)
    if (shape.faceVertices) {
      h += '<details class="modal-section" open><summary>Face → vertices ' +
           '<span class="count">(10 faces)</span></summary>';
      Object.entries(shape.faceVertices).forEach(([face, vs]) => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(face) + '</span>';
        vs.forEach(v => {
          const p = positionForVertex(v);
          h += ' ';
          if (p) h += '<a class="jump-link" data-jump-to="' + p + '">' + ESC(v) + '</a>';
          else h += ESC(v);
        });
        h += '</div>';
      });
      h += '</details>';
    }

    // Pins (for 36-pin)
    const pins = shape.aggregatedPins || [];
    if (pins.length) {
      h += '<details class="modal-section" open><summary>Pins ' +
           '<span class="count">(' + pins.length + ')</span></summary>';
      pins.forEach((p, i) => {
        h += '<div class="item">';
        h += '<span class="tag">#' + (i+1) + '</span>';
        h += '<span class="label">' + ESC(p.parameter || "") + '</span>';
        if (p.measured) h += '<div class="sublabel"><strong>Measured:</strong> ' + ESC(p.measured) + '</div>';
        if (p.formula) h += '<div class="sublabel"><strong>Formula:</strong> ' + ESC(p.formula) + '</div>';
        if (p.error) h += '<div class="sublabel"><strong>Error:</strong> ' + ESC(p.error) + '</div>';
        if (p.gammas) h += '<div class="sublabel"><strong>γ\'s:</strong> ' + ESC(p.gammas) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Aggregated walls
    const walls = shape.aggregatedWalls || [];
    if (walls.length) {
      h += '<details class="modal-section"><summary>Aggregated walls ' +
           '<span class="count">(' + walls.length + ')</span></summary>';
      walls.forEach(w => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(w.name || "") + '</span>';
        if (w._source) h += '<span class="src">← ' + ESC(w._source) + '</span>';
        if (w.topic) h += '<span class="label">' + ESC(w.topic) + '</span>';
        if (w.status) h += '<div class="sublabel"><strong>Status:</strong> ' + ESC(w.status) + '</div>';
        if (w.statement) h += '<div class="sublabel">' + ESC(w.statement) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Aggregated theorems
    const thms = shape.aggregatedTheorems || [];
    if (thms.length) {
      h += '<details class="modal-section"><summary>Aggregated theorems ' +
           '<span class="count">(' + thms.length + ')</span></summary>';
      thms.forEach(t => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(t.kind || "Theorem") + ' ' + ESC(t.number || "") + '</span>';
        if (t._source) h += '<span class="src">← ' + ESC(t._source) + '</span>';
        if (t.name) h += '<span class="label">' + ESC(t.name) + '</span>';
        if (t.statement) h += '<div class="sublabel">' + ESC(t.statement) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Aggregated requirements
    const reqs = shape.aggregatedRequirements || [];
    if (reqs.length) {
      h += '<details class="modal-section"><summary>Aggregated requirements ' +
           '<span class="count">(' + reqs.length + ')</span></summary>';
      reqs.forEach(r => {
        h += '<div class="item">';
        h += '<span class="tag">#' + ESC(r.n || "") + '</span>';
        if (r._source) h += '<span class="src">← ' + ESC(r._source) + '</span>';
        h += '<span class="label">' + ESC(r.label || "") + '</span>';
        if (r.description) h += '<div class="sublabel">' + ESC(r.description) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Aggregated layers
    const layers = shape.aggregatedLayers || [];
    if (layers.length) {
      h += '<details class="modal-section"><summary>Aggregated chain layers ' +
           '<span class="count">(' + layers.length + ')</span></summary>';
      layers.forEach(l => {
        h += '<div class="item">';
        h += '<span class="tag">L' + ESC(l.id) + '</span>';
        if (l._source) h += '<span class="src">← ' + ESC(l._source) + '</span>';
        if (l.status) h += '<span class="tag status ' + statusKind(l.status) + '">' + ESC(l.status) + '</span>';
        h += '<span class="label">' + ESC(l.statement) + '</span>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Aggregated cross-cuts
    const cc = shape.aggregatedCrossCuts || [];
    if (cc.length) {
      h += '<details class="modal-section"><summary>Aggregated cross-cuts ' +
           '<span class="count">(' + cc.length + ')</span></summary>';
      cc.forEach(e => {
        h += '<div class="item">';
        if (e._source) h += '<span class="src">← ' + ESC(e._source) + '</span>';
        h += '<span class="label">' + ESC(e.from || "") + ':' + ESC(e.from_layer || "") +
             ' ↔ ' + ESC(e.to || "") + (e.to_layer ? ':' + ESC(e.to_layer) : "") + '</span>';
        if (e.shared) h += '<div class="sublabel">shared: ' + ESC(e.shared) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    // Aggregated bonus / numbers
    const bonus = shape.aggregatedBonus || [];
    if (bonus.length) {
      h += '<details class="modal-section"><summary>Aggregated bonus theorems ' +
           '<span class="count">(' + bonus.length + ')</span></summary>';
      bonus.forEach(t => {
        h += '<div class="item">';
        h += '<span class="tag kind">' + ESC(t.kind || "Theorem") + ' ' + ESC(t.number || "") + '</span>';
        if (t._source) h += '<span class="src">← ' + ESC(t._source) + '</span>';
        if (t.name) h += '<span class="label">' + ESC(t.name) + '</span>';
        if (t.statement) h += '<div class="sublabel">' + ESC(t.statement) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    const nums = shape.aggregatedNumbers || [];
    if (nums.length) {
      h += '<details class="modal-section"><summary>Aggregated numbers ' +
           '<span class="count">(' + nums.length + ')</span></summary>';
      nums.forEach(n => {
        h += '<div class="item">';
        h += '<span class="tag">#' + ESC(n.n) + '</span>';
        if (n._source) h += '<span class="src">← ' + ESC(n._source) + '</span>';
        h += '<span class="label">' + ESC(n.quantity) + '</span>';
        h += '<div class="sublabel">' + ESC(n.value) + '</div>';
        h += '</div>';
      });
      h += '</details>';
    }

    return h || '<p class="subsection" style="color:var(--text-2)">No aggregated content.</p>';
  }

  function renderModalECircle(shape) {
    let h = "";
    h += '<details class="modal-section" open><summary>Face → conjecture ' +
         '<span class="count">(10 faces)</span></summary>';
    Object.entries(shape.faceConjectures || {}).forEach(([face, conj]) => {
      h += '<div class="item">';
      h += '<span class="tag kind">' + ESC(face) + '</span>';
      h += '<span class="label">' + ESC(conj) + '</span>';
      h += '</div>';
    });
    h += '</details>';
    return h;
  }

  function renderModalCore(shape) {
    let h = "";
    if (shape.proofChainStatus) {
      h += '<details class="modal-section" open><summary>Core status</summary>';
      h += '<div class="subsection"><strong>Status:</strong> ' + ESC(shape.proofChainStatus) + '</div>';
      if (shape.theoremCount) h += '<div class="subsection"><strong>Theorems:</strong> ' + shape.theoremCount + '</div>';
      if (shape.predictionCount) h += '<div class="subsection"><strong>Predictions:</strong> ' + shape.predictionCount + '</div>';
      h += '</details>';
    }
    return h;
  }

  function renderModalSouthTrough(shape) {
    let h = "";
    h += '<details class="modal-section" open><summary>North pole (complete work)</summary>';
    (shape.northVertices || []).forEach(v => {
      const p = positionForVertex(v);
      h += '<div class="item">';
      if (p) h += '<a class="jump-link" data-jump-to="' + p + '">' + ESC(v) + '</a>';
      else h += '<span class="label">' + ESC(v) + '</span>';
      h += '</div>';
    });
    h += '</details>';
    h += '<details class="modal-section" open><summary>South trough (frontier)</summary>';
    (shape.southVertices || []).forEach(v => {
      const p = positionForVertex(v);
      h += '<div class="item">';
      if (p) h += '<a class="jump-link" data-jump-to="' + p + '">' + ESC(v) + '</a>';
      else h += '<span class="label">' + ESC(v) + '</span>';
      h += '</div>';
    });
    h += '</details>';
    return h;
  }

  function statusKind(s) {
    if (!s) return "";
    const u = s.toUpperCase();
    if (u.includes("PROVED") || u.includes("QED")) return "proved";
    if (u.includes("PARTIAL") || u.includes("LITERATURE") || u.includes("CONDITIONAL")) return "partial";
    if (u.includes("OPEN")) return "open";
    if (u.includes("SILENT") || u.includes("NEEDS") || u.includes("SPECULATIVE")) return "silent";
    return "";
  }

  // Open raw-markdown artifact view
  function openArtifact(path, label) {
    const art = ARTIFACTS[path];
    modalTitle.textContent = label;
    modalMeta.textContent = path + (art ? "  ·  " + (art.lines || 0) + " lines  ·  " + (art.size || 0) + " chars" : "");
    if (!art || !art.content) {
      modalBody.innerHTML = '<p class="subsection" style="color:var(--red)">Artifact content not collected at build time.</p>';
    } else {
      modalBody.innerHTML = '<div class="raw-markdown">' + highlightMarkdown(art.content) + '</div>';
    }
    modalRoot.hidden = false;
    document.body.style.overflow = "hidden";
    modalBody.scrollTop = 0;
  }

  // Minimal custom markdown highlighter.
  function highlightMarkdown(text) {
    // Escape HTML first
    let t = ESC(text);
    // Highlight verdict tags (PROVED / PARTIAL / OPEN / SILENT / CONDITIONAL)
    t = t.replace(/\b(PROVED|QED)\b/g, '<span class="md-tag-proved">$1</span>');
    t = t.replace(/\b(PARTIAL|LITERATURE)\b/g, '<span class="md-tag-partial">$1</span>');
    t = t.replace(/\b(OPEN-BUT-ADDRESSED|OPEN)\b/g, '<span class="md-tag-open">$1</span>');
    t = t.replace(/\b(SILENT|NEEDS-CONSTRUCTION|NEEDS-NUMERICAL-EXTRACT|SPECULATIVE)\b/g, '<span class="md-tag-silent">$1</span>');
    t = t.replace(/\bCONDITIONAL\b/g, '<span class="md-tag-conditional">CONDITIONAL</span>');
    // Headings
    t = t.replace(/^(####\s+)(.+)$/gm, '<span class="md-h4">$1$2</span>');
    t = t.replace(/^(###\s+)(.+)$/gm, '<span class="md-h3">$1$2</span>');
    t = t.replace(/^(##\s+)(.+)$/gm, '<span class="md-h2">$1$2</span>');
    t = t.replace(/^(#\s+)(.+)$/gm, '<span class="md-h1">$1$2</span>');
    // Inline code `foo`
    t = t.replace(/`([^`]+)`/g, '<span class="md-code">$1</span>');
    // Bold **foo**
    t = t.replace(/\*\*([^*\n]+)\*\*/g, '<span class="md-bold">$1</span>');
    // Italic *foo* (avoid ** already converted)
    t = t.replace(/(^|[^\*])\*([^*\n]+)\*/g, '$1<span class="md-italic">$2</span>');
    // Bullet lines — highlight the dash
    t = t.replace(/^(\s*)-\s/gm, '$1<span class="md-bullet">-</span> ');
    return t;
  }

  // Attach handlers to every `data-jump-to` element in the modal
  function hookupJumpLinks() {
    modalBody.querySelectorAll("[data-jump-to]").forEach(el => {
      el.addEventListener("click", function(ev) {
        ev.preventDefault();
        const pos = parseInt(el.getAttribute("data-jump-to"), 10);
        if (!isNaN(pos)) {
          closeModal();
          const idx = Math.max(0, Math.min(N - 1, pos - 1));
          slider.value = idx;
          render(idx);
        }
      });
    });
  }

  // Attach handlers to ladder rungs (for file linking)
  function hookupLadder() {
    metricsEl.querySelectorAll(".ladder-rung").forEach(el => {
      const rung = el.getAttribute("data-rung");
      el.addEventListener("click", function() {
        const shape = shapes[parseInt(slider.value, 10)];
        const det = (shape && shape.ladderDetections) || {};
        const path = det[rung];
        // No-op; just flash. (Could open modal here in the future.)
        if (path) {
          // Could open a viewer — for now, show inline tooltip alert
        }
      });
    });
  }

  // Attach handlers to mode toggle buttons
  function hookupModeToggles() {
    metricsEl.querySelectorAll("[data-mode-artifact]").forEach(el => {
      el.addEventListener("click", function() {
        const path = el.getAttribute("data-mode-artifact");
        const label = el.getAttribute("data-mode-label") || "Artifact";
        openArtifact(path, label);
      });
    });
  }

  // ===========================================================================
  function render(idx) {
    const shape = shapes[idx];
    if (!shape) return;
    nameEl.textContent = shape.name;
    classEl.textContent = shape.class;
    positionEl.textContent = (idx + 1) + "/" + N;

    canvas.innerHTML = renderSVG(shape);
    caption.textContent = shape.label || "";

    metricsEl.innerHTML = renderMetricsPanel(shape);
    footnotesEl.innerHTML = renderFootnotesPanel(shape);

    // Face-marker interactivity for e-circle
    if (shape.class === "e-circle") {
      canvas.querySelectorAll(".face-group .face-marker").forEach(el => {
        el.addEventListener("click", function(ev) {
          ev.stopPropagation();
          canvas.querySelectorAll(".face-marker").forEach(m => m.classList.remove("highlight"));
          el.classList.add("highlight");
        });
      });
    }

    // Click-to-xray: "open-self" zones open THIS shape in modal
    canvas.querySelectorAll("[data-open-self]").forEach(el => {
      el.addEventListener("click", function(ev) {
        ev.stopPropagation();
        openModal(shape);
      });
    });
    // "data-jump-to" zones (bouquet rings, chord endpoints, face nodes, outer-ring vertices)
    canvas.querySelectorAll("[data-jump-to]").forEach(el => {
      el.addEventListener("click", function(ev) {
        ev.stopPropagation();
        const pos = parseInt(el.getAttribute("data-jump-to"), 10);
        if (!isNaN(pos)) {
          const i = Math.max(0, Math.min(N - 1, pos - 1));
          slider.value = i;
          render(i);
        }
      });
    });

    hookupLadder();
    hookupModeToggles();
  }

  slider.addEventListener("input", (e) => {
    render(parseInt(e.target.value, 10));
  });

  prevBtn.addEventListener("click", () => {
    const v = Math.max(0, parseInt(slider.value, 10) - 1);
    slider.value = v; render(v);
  });
  nextBtn.addEventListener("click", () => {
    const v = Math.min(N - 1, parseInt(slider.value, 10) + 1);
    slider.value = v; render(v);
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modalRoot.hidden) {
      closeModal();
      return;
    }
    if (!modalRoot.hidden) return;  // don't navigate while modal open
    if (e.target && (e.target.tagName === "INPUT" && e.target !== slider)) return;
    if (e.key === "ArrowLeft") {
      const v = Math.max(0, parseInt(slider.value, 10) - 1);
      slider.value = v; render(v);
    } else if (e.key === "ArrowRight") {
      const v = Math.min(N - 1, parseInt(slider.value, 10) + 1);
      slider.value = v; render(v);
    }
  });

  // Modal close handlers
  modalRoot.querySelectorAll("[data-modal-close]").forEach(el => {
    el.addEventListener("click", closeModal);
  });
  // Observe the modal body for jump links after each content change
  const modalObserver = new MutationObserver(hookupJumpLinks);
  modalObserver.observe(modalBody, { childList: true, subtree: true });

  if (N > 0) render(0);
  else {
    canvas.innerHTML = '<div style="color:#ef4444;padding:40px">No shape data — run <code>python3 visualization/build.py</code></div>';
  }
})();
