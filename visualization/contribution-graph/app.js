/* contribution-graph -- vanilla JS renderer.
 *
 * CONTRIBUTION_DATA is loaded from data.js (window-global, file:// safe).
 * Renders a 25-vertex ring with three concentric layers per vertex:
 *
 *    inner ring (radius 250-280) = COMPLY  baseline (slate)
 *    mid   ring (radius 290-320) = INDEPENDENT lift (amber)
 *    outer ring (radius 330-365) = CONTRIBUTE  gift (cyan)
 *
 * Per-vertex sector arc length scales with the count of theorems / cells in
 * that pillar.  Hovering shows tooltip; clicking opens the comparison panel.
 *
 * Cross-cut chords drawn between vertex centers (radius ~ 240).
 */
(function () {
  "use strict";

  const D = (typeof CONTRIBUTION_DATA !== "undefined")
              ? CONTRIBUTION_DATA
              : (typeof window !== "undefined" ? window.CONTRIBUTION_DATA : null);
  if (!D) {
    document.body.innerHTML =
      '<pre style="color:#f87171;padding:24px">data.js missing or malformed -- run python3 visualization/contribution-graph/build.py</pre>';
    return;
  }

  const SVG_NS = "http://www.w3.org/2000/svg";
  const svg = document.getElementById("ring-svg");

  // Geometry constants (matches viewBox -500..500).
  const R_RING_BASE     = 240;     // chord endpoints + label baseline radius
  const R_COMPLY_INNER  = 250;
  const R_COMPLY_OUTER  = 278;
  const R_INDEP_INNER   = 286;
  const R_INDEP_OUTER   = 314;
  const R_CONTRIB_INNER = 322;
  const R_CONTRIB_OUTER = 360;
  const R_LABEL         = 400;
  const SECTOR_WIDTH_FRACTION = 0.85;  // of the available 2pi/N slot

  const N = D.vertices.length;
  const SECTOR_ARC = (2 * Math.PI / N) * SECTOR_WIDTH_FRACTION;

  // Build an index by key for fast lookup.
  const byKey = {};
  D.vertices.forEach((v) => { byKey[v.key] = v; });

  // ---------- maths helpers ----------
  function polar(r, theta) {
    return [r * Math.cos(theta), r * Math.sin(theta)];
  }

  /** SVG arc path describing a sector ring slice from angle a0 to a1, between radii r0 and r1. */
  function sectorPath(a0, a1, r0, r1) {
    const [x0o, y0o] = polar(r1, a0);
    const [x1o, y1o] = polar(r1, a1);
    const [x0i, y0i] = polar(r0, a0);
    const [x1i, y1i] = polar(r0, a1);
    const large = (a1 - a0) > Math.PI ? 1 : 0;
    return [
      "M", x0o, y0o,
      "A", r1, r1, 0, large, 1, x1o, y1o,
      "L", x1i, y1i,
      "A", r0, r0, 0, large, 0, x0i, y0i,
      "Z",
    ].join(" ");
  }

  /** Quadratic Bezier chord from p0 to p1 curving toward origin. */
  function chordPath(p0, p1, sag = 0.55) {
    // Control point pulls toward origin, scaled by sag.
    const cx = (p0[0] + p1[0]) * 0.5 * (1 - sag);
    const cy = (p0[1] + p1[1]) * 0.5 * (1 - sag);
    return `M ${p0[0]} ${p0[1]} Q ${cx} ${cy} ${p1[0]} ${p1[1]}`;
  }

  function el(tag, attrs, parent) {
    const e = document.createElementNS(SVG_NS, tag);
    for (const k in attrs) {
      if (attrs[k] !== undefined && attrs[k] !== null) e.setAttribute(k, attrs[k]);
    }
    if (parent) parent.appendChild(e);
    return e;
  }

  // ---------- size of each pillar's sector arc fraction ----------
  // Use the count of theorems (or sections) to scale the sector's arc fraction.
  function pillarFraction(v, pillar) {
    if (!v[pillar] || !v[pillar].present) return 0;
    const t = v[pillar].theorems || 0;
    const s = v[pillar].sections || 0;
    // map by sqrt to keep big pillars from drowning small ones
    const score = Math.sqrt(Math.max(1, t + 0.5 * s));
    return Math.min(1.0, score / 6.0);  // 6 keeps arc <= full slot
  }

  // ---------- render groups ----------
  function setupSvgLayers() {
    // background reference rings (faint)
    [R_COMPLY_INNER, R_COMPLY_OUTER, R_INDEP_OUTER, R_CONTRIB_OUTER].forEach((r) => {
      el("circle", { cx: 0, cy: 0, r, class: "ring-base" }, svg);
    });

    return {
      gEdges:   el("g", { id: "g-edges" },   svg),
      gPillars: el("g", { id: "g-pillars" }, svg),
      gVertices:el("g", { id: "g-vertices" },svg),
      gLabels:  el("g", { id: "g-labels" },  svg),
      gHits:    el("g", { id: "g-hits" },    svg),
    };
  }

  function renderEdges(layer) {
    D.edges.forEach((e) => {
      const a = byKey[e.src], b = byKey[e.dst];
      if (!a || !b) return;
      const p0 = polar(R_RING_BASE - 6, a.theta);
      const p1 = polar(R_RING_BASE - 6, b.theta);
      const cls = (e.status === "verified") ? "edge-verified" : "edge-spec";
      const path = el("path", {
        d: chordPath(p0, p1),
        class: cls,
        "data-edge": `${e.src}--${e.dst}`,
      }, layer);
      // tooltip on hover (native browser <title>)
      const t = el("title", {}, path);
      t.textContent = `${a.name} (${e.src_layer || "?"}) <-> ${b.name} (${e.dst_layer || "?"})\nshared: ${e.shared}\n${e.reason}`;
    });
  }

  function renderPillarSectors(layer) {
    D.vertices.forEach((v) => {
      const t0 = v.theta - SECTOR_ARC / 2;
      const tEnd = v.theta + SECTOR_ARC / 2;

      const fComp = pillarFraction(v, "comply");
      const fIndep = pillarFraction(v, "independent");
      const fContrib = pillarFraction(v, "contribute");

      const slotMid = v.theta;
      function arcSpan(frac) {
        const span = SECTOR_ARC * Math.max(0.05, frac);  // never zero -- show a sliver
        return [slotMid - span / 2, slotMid + span / 2];
      }

      // Pillar A
      if (v.comply.present) {
        const [a0, a1] = arcSpan(fComp);
        el("path", {
          d: sectorPath(a0, a1, R_COMPLY_INNER, R_COMPLY_OUTER),
          class: "vtx-comply",
          "data-vtx": v.key,
          opacity: 0.85,
        }, layer);
      }

      // Pillar B
      if (v.independent.present) {
        const [a0, a1] = arcSpan(fIndep);
        el("path", {
          d: sectorPath(a0, a1, R_INDEP_INNER, R_INDEP_OUTER),
          class: "vtx-indep",
          "data-vtx": v.key,
          opacity: 0.85,
        }, layer);
      }

      // Pillar C
      if (v.contribute.present) {
        const [a0, a1] = arcSpan(fContrib);
        el("path", {
          d: sectorPath(a0, a1, R_CONTRIB_INNER, R_CONTRIB_OUTER),
          class: "vtx-contrib",
          "data-vtx": v.key,
          opacity: 0.9,
        }, layer);
      }

      // For audit-pending: dashed sector across all three rings
      if (v.status === "AUDIT PENDING") {
        const [a0, a1] = [v.theta - SECTOR_ARC * 0.3, v.theta + SECTOR_ARC * 0.3];
        el("path", {
          d: sectorPath(a0, a1, R_COMPLY_INNER, R_CONTRIB_OUTER),
          class: "vtx-pending",
          "data-vtx": v.key,
        }, layer);
      }
    });
  }

  function renderVertexDots(layer) {
    D.vertices.forEach((v) => {
      const [x, y] = polar(R_RING_BASE, v.theta);
      // Mill ring marker
      if (v.is_millennium) {
        el("circle", { cx: x, cy: y, r: 6, class: "vtx-mill", "data-vtx": v.key }, layer);
      }
      // central dot
      el("circle", {
        cx: x, cy: y,
        r: v.is_millennium ? 3.5 : 2.4,
        fill: v.status === "FULL" ? "var(--pillar-contrib)" :
              v.status === "PARTIAL" ? "var(--pillar-indep)" :
              "#3b3b55",
        "data-vtx": v.key,
      }, layer);
    });
  }

  function renderLabels(layer) {
    D.vertices.forEach((v) => {
      const [x, y] = polar(R_LABEL, v.theta);
      // Rotation: keep upright on top half, flip on bottom half so labels read normally.
      let angleDeg = v.theta * 180 / Math.PI;
      let rotate = angleDeg;
      let anchor = "start";
      if (angleDeg > 90 || angleDeg < -90) {
        rotate = angleDeg + 180;
        anchor = "end";
      }
      const t = el("text", {
        x, y,
        "text-anchor": anchor,
        "dominant-baseline": "middle",
        transform: `rotate(${rotate} ${x} ${y})`,
        class: v.is_millennium ? "vtx-label" : "vtx-label-dim",
        "data-vtx": v.key,
      }, layer);
      t.textContent = v.name;
    });
  }

  function renderHits(layer) {
    // Big invisible click target per vertex covering its sector.
    D.vertices.forEach((v) => {
      const t0 = v.theta - SECTOR_ARC / 2;
      const t1 = v.theta + SECTOR_ARC / 2;
      const path = el("path", {
        d: sectorPath(t0, t1, R_COMPLY_INNER - 4, R_LABEL + 10),
        class: "vtx-hit",
        "data-vtx": v.key,
      }, layer);
    });
  }

  // ---------- interactions ----------
  const tooltip = document.getElementById("tooltip");
  const hud = document.getElementById("hud-label");

  function showTooltip(v, evt) {
    const ext = v.contribute.externals ? v.contribute.externals.length : 0;
    const prims = v.independent.primitives || {};
    const primTotal = (prims.BYPASS||0)+(prims.DECOMPOSE||0)+(prims.EXCISE||0)+(prims.TRANSPOSE||0);
    tooltip.innerHTML = `
      <h4>${v.name} <small>(${v.key})</small></h4>
      <div class="row"><b>status</b><span>${v.status}</span></div>
      <div class="row"><b>COMPLY</b><span>${v.comply.present ? `${v.comply.theorems} thms / ${v.comply.sections} §` : '—'}</span></div>
      <div class="row"><b>INDEPENDENT</b><span>${v.independent.present ? `${v.independent.theorems} thms · ${primTotal} prims` : '—'}</span></div>
      <div class="row"><b>CONTRIBUTE</b><span>${v.contribute.present ? `${v.contribute.theorems} thms · ${ext} externals` : '—'}</span></div>
      <div class="row"><b>BEYOND</b><span>${v.beyond.present ? `${v.beyond.theorems} thms` : '—'}</span></div>
      <small>click for side-by-side comparison</small>
    `;
    tooltip.hidden = false;
    const rect = svg.getBoundingClientRect();
    let x = evt.clientX - rect.left + 12;
    let y = evt.clientY - rect.top + 12;
    if (x + 320 > rect.width) x = rect.width - 330;
    if (y + 200 > rect.height) y = rect.height - 210;
    tooltip.style.left = x + "px";
    tooltip.style.top  = y + "px";
    hud.textContent = `${v.name} — ${v.status}`;
  }

  function hideTooltip() {
    tooltip.hidden = true;
    hud.textContent = "hover a vertex";
  }

  function highlightVertex(key) {
    document.querySelectorAll(".is-selected").forEach((n) => n.classList.remove("is-selected"));
    document.querySelectorAll(`[data-vtx="${key}"]`).forEach((n) => {
      if (n.classList.contains("vtx-hit")) return;
      n.classList.add("is-selected");
    });
  }

  function attachHandlers() {
    document.querySelectorAll(".vtx-hit").forEach((node) => {
      const key = node.getAttribute("data-vtx");
      const v = byKey[key];
      node.addEventListener("mousemove", (e) => showTooltip(v, e));
      node.addEventListener("mouseleave", hideTooltip);
      node.addEventListener("click", () => {
        highlightVertex(key);
        renderComparison(v);
      });
    });
  }

  // ---------- comparison panel ----------
  function statText(v, pillar) {
    const p = v[pillar];
    if (!p || !p.present) return [["status", "AUDIT PENDING"]];
    const arr = [
      ["lines", p.lines],
      ["sections", p.sections],
      ["theorems", p.theorems],
    ];
    if (pillar === "comply" && p.layers !== undefined) arr.push(["layers", p.layers]);
    if (pillar === "contribute" && p.externals !== undefined) arr.push(["externals", p.externals.length]);
    return arr;
  }

  function fillStats(ulId, pairs) {
    const ul = document.getElementById(ulId);
    ul.innerHTML = "";
    pairs.forEach(([k, v]) => {
      const li = document.createElement("li");
      li.innerHTML = `${k}: <b>${v}</b>`;
      ul.appendChild(li);
    });
  }

  function fillWalls(divId, walls) {
    const d = document.getElementById(divId);
    d.innerHTML = "";
    if (!walls || !walls.length) return;
    walls.forEach((w) => {
      const span = document.createElement("span");
      span.className = "wall-tag";
      span.textContent = w;
      d.appendChild(span);
    });
  }

  function fillPrimitiveBar(divId, prims) {
    const d = document.getElementById(divId);
    d.innerHTML = "";
    const total = (prims.BYPASS||0)+(prims.DECOMPOSE||0)+(prims.EXCISE||0)+(prims.TRANSPOSE||0);
    if (!total) {
      d.innerHTML = '<div style="font-size:11px;color:var(--fg-hushed)">no primitive log</div>';
      return;
    }
    const segs = [
      ["BYP", "seg-byp", prims.BYPASS||0],
      ["DEC", "seg-dec", prims.DECOMPOSE||0],
      ["EXC", "seg-exc", prims.EXCISE||0],
      ["TRP", "seg-trp", prims.TRANSPOSE||0],
    ];
    segs.forEach(([label, cls, n]) => {
      if (!n) return;
      const div = document.createElement("div");
      div.className = "seg " + cls;
      div.style.flexBasis = ((100 * n / total).toFixed(1)) + "%";
      div.textContent = `${label} ${n}`;
      div.title = `${label} = ${n}`;
      d.appendChild(div);
    });
  }

  function fillExternals(divId, externals) {
    const d = document.getElementById(divId);
    d.innerHTML = "";
    if (!externals || !externals.length) {
      d.innerHTML = '<div style="font-size:11px;color:var(--fg-hushed)">no externals inventoried</div>';
      return;
    }
    externals.forEach((e) => {
      const row = document.createElement("div");
      row.className = "ext-row";
      row.innerHTML = `<b>${e.id}</b><span class="ext-name">${e.name}</span><span class="ext-auth">${e.authors||""}</span>`;
      d.appendChild(row);
    });
  }

  function fillBeyond(ulId, v) {
    const ul = document.getElementById(ulId);
    ul.innerHTML = "";
    if (!v.beyond.present) {
      const li = document.createElement("li");
      li.textContent = "no beyond-bonus deliverable";
      ul.appendChild(li);
      return;
    }
    [
      ["lines", v.beyond.lines],
      ["sections", v.beyond.sections],
      ["theorems", v.beyond.theorems],
    ].forEach(([k, val]) => {
      const li = document.createElement("li");
      li.textContent = `${k}: ${val}`;
      ul.appendChild(li);
    });
    const cm = v.compliance;
    if (cm) {
      const li = document.createElement("li");
      li.innerHTML = `compliance map verdicts: <b>${cm.PROVED}P</b> / ${cm.PARTIAL}Pa / ${cm.OPEN_BUT_ADDRESSED}O / ${cm.SILENT}S`;
      ul.appendChild(li);
    }
  }

  function fillAcks(ulId, names) {
    const ul = document.getElementById(ulId);
    ul.innerHTML = "";
    if (!names || !names.length) {
      ul.innerHTML = '<li style="color:var(--fg-hushed)">no landscape file</li>';
      return;
    }
    names.forEach((n) => {
      const li = document.createElement("li");
      li.textContent = n;
      ul.appendChild(li);
    });
  }

  function renderComparison(v) {
    document.getElementById("placeholder").hidden = true;
    document.getElementById("comparison").hidden = false;

    document.getElementById("cmp-name").textContent = v.name;
    const status = document.getElementById("cmp-status");
    status.textContent = v.status;
    status.className = "cmp-status " + (
      v.status === "FULL" ? "full" :
      v.status === "PARTIAL" ? "partial" : "pending"
    );

    document.getElementById("cmp-thm").textContent = v.comply.main_theorem || "(no main theorem extracted)";

    fillStats("comply-stats",  statText(v, "comply"));
    fillStats("indep-stats",   statText(v, "independent"));
    fillStats("contrib-stats", statText(v, "contribute"));

    fillWalls("comply-walls", v.comply.named_walls);
    fillWalls("indep-walls",  v.independent.named_walls);

    fillPrimitiveBar("indep-prims", v.independent.primitives || {});
    fillExternals("contrib-externals", v.contribute.externals || []);

    fillBeyond("cmp-beyond", v);
    fillAcks("cmp-acks", v.acknowledgments);

    document.getElementById("comparison-title").textContent = `${v.name} — three pillars`;
  }

  // ---------- toggles ----------
  function setupToggles() {
    document.getElementById("toggle-edges").addEventListener("change", (e) => {
      document.getElementById("g-edges").style.display = e.target.checked ? "" : "none";
    });
    document.getElementById("toggle-spec").addEventListener("change", (e) => {
      document.querySelectorAll(".edge-spec").forEach((n) => {
        n.style.display = e.target.checked ? "" : "none";
      });
    });
    document.getElementById("toggle-labels").addEventListener("change", (e) => {
      document.getElementById("g-labels").style.display = e.target.checked ? "" : "none";
    });
  }

  // ---------- header summary ----------
  function fillSummary() {
    document.getElementById("ct-vertices").textContent = D.counts.vertices;
    document.getElementById("ct-mill").textContent     = D.counts.fully_authored;
    document.getElementById("ct-edges").textContent    = D.counts.edges;
    document.getElementById("ct-pending").textContent  = D.counts.audit_pending;
    document.getElementById("built-at").textContent    = D.generated_at;
  }

  // ---------- boot ----------
  const layers = setupSvgLayers();
  renderEdges(layers.gEdges);
  renderPillarSectors(layers.gPillars);
  renderVertexDots(layers.gVertices);
  renderLabels(layers.gLabels);
  renderHits(layers.gHits);
  attachHandlers();
  setupToggles();
  fillSummary();

  // Auto-open YM as a demo on load.
  if (byKey["ym"]) {
    highlightVertex("ym");
    renderComparison(byKey["ym"]);
  }
})();
