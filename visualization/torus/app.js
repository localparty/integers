/* app.js -- torus visualization renderer
 *
 * Pure vanilla. No frameworks. Reads global TORUS_DATA (from data.js).
 * SVG-based 3D projection of the torus with overlays for the paper 60 structure.
 */

(function () {
  "use strict";

  // ---------------------------------------------------------------------
  // Data guards
  // ---------------------------------------------------------------------
  if (typeof TORUS_DATA === "undefined") {
    document.body.innerHTML = "<pre>TORUS_DATA not loaded. Run: python3 visualization/torus/build.py</pre>";
    return;
  }
  const D = TORUS_DATA;

  // ---------------------------------------------------------------------
  // Constants -- torus geometry
  // ---------------------------------------------------------------------
  const MAJOR_R = (D.radii && D.radii.major_R_visual) || 3.0;   // big loop radius
  const MINOR_R = (D.radii && D.radii.minor_r_visual) || 1.0;   // tube radius
  const U_STEPS = 36;    // segments around major loop
  const V_STEPS = 14;    // segments around tube
  // (36 * 14 = 504 quads; plenty of resolution, renders snappily)

  const TWO_PI = Math.PI * 2;

  // ---------------------------------------------------------------------
  // State
  // ---------------------------------------------------------------------
  const state = {
    rotX: 25 * Math.PI / 180,   // degrees -> radians
    rotY: -30 * Math.PI / 180,
    zoom: 1.0,                  // multiplier on projection
    stepIdx: 0,
    animating: false,
    animHandle: null,
    layers: {
      mesh: true,
      geoCircle: true,
      specCircle: true,
      faces: true,
      vertices: true,
      zeros: false,
      south: false,
      chords: false,
      dirs: false,
    },
  };

  // ---------------------------------------------------------------------
  // 3D math utilities
  // ---------------------------------------------------------------------
  function torusPoint(u, v, R, r) {
    const cu = Math.cos(u), su = Math.sin(u);
    const cv = Math.cos(v), sv = Math.sin(v);
    return {
      x: (R + r * cv) * cu,
      y: (R + r * cv) * su,
      z: r * sv,
    };
  }

  function rotateXY(p, rx, ry) {
    // Rotate around X axis then Y axis.
    const cosX = Math.cos(rx), sinX = Math.sin(rx);
    const cosY = Math.cos(ry), sinY = Math.sin(ry);
    // X-rotation: y,z -> (y cos - z sin, y sin + z cos)
    let y = p.y * cosX - p.z * sinX;
    let z = p.y * sinX + p.z * cosX;
    let x = p.x;
    // Y-rotation: x,z -> (x cos + z sin, -x sin + z cos)
    const nx = x * cosY + z * sinY;
    const nz = -x * sinY + z * cosY;
    return { x: nx, y: y, z: nz };
  }

  function project(p) {
    // Simple orthographic projection after rotation.
    // SVG viewBox is -400..400; torus has R+r ~ 4; scale = 70 by default.
    const S = 70 * state.zoom;
    return {
      sx: p.x * S,
      sy: -p.y * S,     // flip y for SVG screen coordinates
      depth: p.z,       // used for z-sort
    };
  }

  function to3D(u, v) {
    const p = torusPoint(u, v, MAJOR_R, MINOR_R);
    return rotateXY(p, state.rotX, state.rotY);
  }

  function toScreen(u, v) {
    const pr = project(to3D(u, v));
    return pr;
  }

  // ---------------------------------------------------------------------
  // SVG element builders (namespaced)
  // ---------------------------------------------------------------------
  const SVG_NS = "http://www.w3.org/2000/svg";
  function el(tag, attrs) {
    const e = document.createElementNS(SVG_NS, tag);
    if (attrs) {
      for (const k in attrs) {
        if (attrs[k] == null) continue;
        e.setAttribute(k, attrs[k]);
      }
    }
    return e;
  }
  function txt(parent, s) {
    parent.appendChild(document.createTextNode(s));
    return parent;
  }

  // ---------------------------------------------------------------------
  // Rendering
  // ---------------------------------------------------------------------
  const svg = document.getElementById("torus-svg");
  const hudAngles = document.getElementById("hud-angles");

  function clearSVG() {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
  }

  function buildMesh() {
    // Build quads covering the torus surface. For each quad, compute centroid
    // z in rotated coords; sort back-to-front for hidden-surface handling.
    const quads = [];
    for (let i = 0; i < U_STEPS; i++) {
      for (let j = 0; j < V_STEPS; j++) {
        const u0 = (i / U_STEPS) * TWO_PI;
        const u1 = ((i + 1) / U_STEPS) * TWO_PI;
        const v0 = (j / V_STEPS) * TWO_PI;
        const v1 = ((j + 1) / V_STEPS) * TWO_PI;
        const p00 = to3D(u0, v0);
        const p10 = to3D(u1, v0);
        const p11 = to3D(u1, v1);
        const p01 = to3D(u0, v1);
        const cz = (p00.z + p10.z + p11.z + p01.z) / 4;
        quads.push({
          d: path4(p00, p10, p11, p01),
          depth: cz,
        });
      }
    }
    quads.sort((a, b) => a.depth - b.depth);  // back first
    return quads;
  }

  function path4(p00, p10, p11, p01) {
    const s00 = project(p00), s10 = project(p10),
          s11 = project(p11), s01 = project(p01);
    return "M " + s00.sx.toFixed(2) + " " + s00.sy.toFixed(2) +
           " L " + s10.sx.toFixed(2) + " " + s10.sy.toFixed(2) +
           " L " + s11.sx.toFixed(2) + " " + s11.sy.toFixed(2) +
           " L " + s01.sx.toFixed(2) + " " + s01.sy.toFixed(2) + " Z";
  }

  function renderMesh(g) {
    if (!state.layers.mesh) return;
    const quads = buildMesh();
    // Split by sign of depth -- back half gets dashed subdued style.
    const mid = quads.length / 2;
    quads.forEach((q, i) => {
      const isBack = i < mid;
      g.appendChild(el("path", {
        d: q.d,
        class: "mesh-quad" + (isBack ? " back" : ""),
      }));
    });
  }

  function sampleLoopMajor(v_const, n) {
    // Sample the major (geometric) circle at a fixed v.
    const pts = [];
    for (let i = 0; i <= n; i++) {
      const u = (i / n) * TWO_PI;
      const p = to3D(u, v_const);
      pts.push({ ...project(p), depth: p.z });
    }
    return pts;
  }

  function sampleLoopMinor(u_const, n) {
    const pts = [];
    for (let i = 0; i <= n; i++) {
      const v = (i / n) * TWO_PI;
      const p = to3D(u_const, v);
      pts.push({ ...project(p), depth: p.z });
    }
    return pts;
  }

  function drawPolyline(g, pts, cls) {
    // Split into front and back segments by sign of depth so dashed back and
    // solid front render cleanly.
    let curFront = [];
    let curBack = [];
    let currentMode = null;
    function flush() {
      if (currentMode === "front" && curFront.length > 1) {
        g.appendChild(el("path", {
          d: "M " + curFront.map(p => p.sx.toFixed(2) + " " + p.sy.toFixed(2)).join(" L "),
          class: cls,
        }));
      } else if (currentMode === "back" && curBack.length > 1) {
        g.appendChild(el("path", {
          d: "M " + curBack.map(p => p.sx.toFixed(2) + " " + p.sy.toFixed(2)).join(" L "),
          class: cls + " back",
        }));
      }
      curFront = [];
      curBack = [];
    }

    for (const p of pts) {
      const mode = p.depth >= 0 ? "front" : "back";
      if (mode !== currentMode) {
        flush();
        currentMode = mode;
      }
      if (mode === "front") curFront.push(p);
      else curBack.push(p);
    }
    flush();
  }

  function renderGeometricCircle(g) {
    // The "geometric" generating circle sits at v = 0 (outer equator of tube
    // times the major loop -- i.e. the classical major circle at the outer
    // side of the tube). We draw it at the equator v=0 for visual clarity.
    if (!state.layers.geoCircle) return;
    const pts = sampleLoopMajor(0, 160);
    drawPolyline(g, pts, "geo-circle");
  }

  function renderSpectralCircle(g) {
    // The "spectral" generating circle is one poloidal loop. Draw at u=0.
    if (!state.layers.specCircle) return;
    const pts = sampleLoopMinor(0, 80);
    drawPolyline(g, pts, "spec-circle");
  }

  function renderFaces(g) {
    if (!state.layers.faces) return;
    // Gather, z-sort, then draw.
    const items = D.faces.map(f => {
      const p = to3D(f.u, f.v);
      const s = project(p);
      return { f, s, depth: p.z };
    });
    items.sort((a, b) => a.depth - b.depth);
    for (const { f, s, depth } of items) {
      const r = 6;
      const opacityMod = depth < 0 ? 0.5 : 1.0;
      const circle = el("circle", {
        cx: s.sx.toFixed(2),
        cy: s.sy.toFixed(2),
        r: r,
        class: "face-marker " + f.circle,
        "fill-opacity": opacityMod,
      });
      circle.dataset.key = f.key;
      g.appendChild(circle);

      const lab = el("text", {
        x: s.sx.toFixed(2),
        y: (s.sy - 11).toFixed(2),
        class: "face-label " + f.circle,
        "fill-opacity": opacityMod,
      });
      txt(lab, f.key + " (" + f.conj + ")");
      g.appendChild(lab);
    }
  }

  function renderVertices(g) {
    if (!state.layers.vertices) return;
    const items = D.vertices.map(v => {
      const p = to3D(v.u, v.v);
      const s = project(p);
      return { v, s, depth: p.z };
    });
    items.sort((a, b) => a.depth - b.depth);
    for (const { v, s, depth } of items) {
      // radius scales with confidence
      const r = 2.5 + 0.5 * Math.max(1, v.conf);
      const opacityMod = depth < 0 ? 0.4 : 1.0;
      const circle = el("circle", {
        cx: s.sx.toFixed(2),
        cy: s.sy.toFixed(2),
        r: r.toFixed(2),
        class: "vertex-marker " + v.zone,
        "fill-opacity": opacityMod,
      });
      g.appendChild(circle);
      const lab = el("text", {
        x: s.sx.toFixed(2),
        y: (s.sy - r - 3).toFixed(2),
        class: "vertex-label",
        "fill-opacity": opacityMod,
      });
      txt(lab, v.name + " " + v.conf.toFixed(0));
      g.appendChild(lab);
    }
  }

  function renderZeros(g) {
    if (!state.layers.zeros) return;
    // Zeros on the equator (intersection locus).
    const items = D.zeros.map(z => {
      const p = to3D(z.u, z.v);
      const s = project(p);
      return { z, s, depth: p.z };
    });
    items.sort((a, b) => a.depth - b.depth);
    for (const { z, s, depth } of items) {
      const opacityMod = depth < 0 ? 0.35 : 1.0;
      g.appendChild(el("circle", {
        cx: s.sx.toFixed(2),
        cy: s.sy.toFixed(2),
        r: 3,
        class: "zero-marker",
        "fill-opacity": opacityMod,
      }));
      const lab = el("text", {
        x: s.sx.toFixed(2),
        y: (s.sy + 10).toFixed(2),
        class: "vertex-label",
        "fill-opacity": opacityMod,
      });
      txt(lab, "\u03b3" + z.index);
      g.appendChild(lab);
    }
  }

  function renderSouth(g) {
    if (!state.layers.south) return;
    // Draw the south-trough arc: the part of the major loop where SOUTH
    // vertices cluster. Per the vertex data, southern vertices are those with
    // zone === "SOUTH". We draw (1) a highlighted arc on the tube south
    // (v = -pi/2) covering the u-range of south vertices, and (2) an ellipse
    // silhouette on a 2D inset showing the confidence distribution.
    const southPts = [];
    for (let i = 0; i <= 120; i++) {
      const u = (i / 120) * TWO_PI;
      const p = to3D(u, -Math.PI / 2);
      southPts.push({ ...project(p), depth: p.z });
    }
    drawPolyline(g, southPts, "south-arc");

    // Also mark each south vertex with a pink ring pulse.
    for (const v of D.vertices) {
      if (v.zone !== "SOUTH") continue;
      const p = to3D(v.u, -0.6);  // pushed deeper south for emphasis
      const s = project(p);
      g.appendChild(el("circle", {
        cx: s.sx.toFixed(2),
        cy: s.sy.toFixed(2),
        r: 8,
        class: "south-ellipse",
      }));
    }
  }

  function renderChords(g) {
    if (!state.layers.chords) return;
    // Cross-cut chords: draw a handful of characteristic face-to-face links.
    // The two most interesting: S-duality pairs (geometric <-> spectral in
    // the same column). Those pass through the tube interior.
    const byCol = {};
    for (const f of D.faces) {
      if (!byCol[f.col]) byCol[f.col] = [];
      byCol[f.col].push(f);
    }
    const chordPairs = [];
    for (const col in byCol) {
      const fs = byCol[col];
      if (fs.length === 2) chordPairs.push([fs[0], fs[1]]);
    }
    for (const [a, b] of chordPairs) {
      const pa = to3D(a.u, a.v);
      const pb = to3D(b.u, b.v);
      const sa = project(pa), sb = project(pb);
      // Chord is "hidden" if midpoint behind the torus (depth < 0).
      const midZ = (pa.z + pb.z) / 2;
      g.appendChild(el("line", {
        x1: sa.sx.toFixed(2), y1: sa.sy.toFixed(2),
        x2: sb.sx.toFixed(2), y2: sb.sy.toFixed(2),
        class: "chord" + (midZ < 0 ? " hidden-chord" : ""),
      }));
    }
  }

  function renderDirs(g) {
    if (!state.layers.dirs) return;
    // Label toroidal (major / geometric) and poloidal (minor / spectral).
    // Place labels at specific landmark points.
    const toroidalP = to3D(Math.PI / 2, 0);   // quarter around major
    const toroidalS = project(toroidalP);
    const t1 = el("text", {
      x: toroidalS.sx.toFixed(2),
      y: (toroidalS.sy - 16).toFixed(2),
      class: "dir-label geo",
    });
    txt(t1, "toroidal \u2192 geometric (e-circle)");
    g.appendChild(t1);

    const poloidalP = to3D(0, Math.PI);   // far side of tube at u=0
    const poloidalS = project(poloidalP);
    const t2 = el("text", {
      x: poloidalS.sx.toFixed(2),
      y: (poloidalS.sy - 10).toFixed(2),
      class: "dir-label spec",
    });
    txt(t2, "poloidal \u2192 spectral (modular flow)");
    g.appendChild(t2);
  }

  function render() {
    clearSVG();

    // Group container (helps with future transforms).
    const g = el("g", { id: "scene" });
    svg.appendChild(g);

    // Order matters (back to front):
    renderMesh(g);

    // Generating circles on back side first (z-sort inside each).
    // Our drawPolyline splits into front/back automatically.
    renderGeometricCircle(g);
    renderSpectralCircle(g);

    // Overlays rendered front-to-back at sort time.
    renderChords(g);
    renderSouth(g);
    renderZeros(g);
    renderFaces(g);
    renderVertices(g);
    renderDirs(g);

    // Apply highlight pulse based on current step.
    applyStepHighlight();

    // HUD.
    hudAngles.textContent =
      "pitch " + rad2deg(state.rotX).toFixed(0) + "\u00b0" +
      " \u00b7 yaw " + rad2deg(state.rotY).toFixed(0) + "\u00b0" +
      " \u00b7 zoom " + state.zoom.toFixed(2);
  }

  function rad2deg(r) { return r * 180 / Math.PI; }

  // ---------------------------------------------------------------------
  // Step-driven highlight
  // ---------------------------------------------------------------------
  function applyStepHighlight() {
    const steps = D.explanation || [];
    if (!steps.length) return;
    const step = steps[state.stepIdx];
    if (!step || !step.highlight) return;
    // Pulse certain elements based on highlight key.
    const highlight = step.highlight;
    switch (highlight) {
      case "geometric_circle":
        svg.querySelectorAll(".geo-circle").forEach(e => e.classList.add("highlight-pulse"));
        break;
      case "spectral_circle":
        svg.querySelectorAll(".spec-circle").forEach(e => e.classList.add("highlight-pulse"));
        break;
      case "torus_surface":
        svg.querySelectorAll(".mesh-quad").forEach(e => e.classList.add("highlight-pulse"));
        break;
      case "faces":
        svg.querySelectorAll(".face-marker, .face-label").forEach(e => e.classList.add("highlight-pulse"));
        break;
      case "vertices":
        svg.querySelectorAll(".vertex-marker").forEach(e => e.classList.add("highlight-pulse"));
        break;
      case "south_trough":
        svg.querySelectorAll(".south-arc, .south-ellipse").forEach(e => e.classList.add("highlight-pulse"));
        // also auto-enable south layer when viewing this step
        break;
      case "zeros":
        svg.querySelectorAll(".zero-marker").forEach(e => e.classList.add("highlight-pulse"));
        break;
    }
  }

  function renderStep() {
    const steps = D.explanation || [];
    if (!steps.length) return;
    const n = steps.length;
    state.stepIdx = ((state.stepIdx % n) + n) % n;
    const step = steps[state.stepIdx];
    document.getElementById("step-title").textContent = "Step " + step.idx + ". " + step.title;
    document.getElementById("step-text").textContent = step.body;
    document.getElementById("step-cite").textContent = step.cite || "";
    document.getElementById("step-counter").textContent = "step " + (state.stepIdx + 1) + " / " + n;

    // Auto-toggle overlays based on step highlight so the user sees the story.
    const h = step.highlight;
    if (h === "south_trough") {
      setLayer("south", true);
    } else if (h === "zeros") {
      setLayer("zeros", true);
    } else if (h === "vertices") {
      setLayer("vertices", true);
    } else if (h === "faces") {
      setLayer("faces", true);
    }

    render();
  }

  function setLayer(key, on) {
    state.layers[key] = on;
    const cb = document.getElementById("layer-" + keyToId(key));
    if (cb) cb.checked = on;
  }

  function keyToId(key) {
    // Map internal camel keys to DOM ids.
    const map = {
      mesh: "mesh",
      geoCircle: "geo-circle",
      specCircle: "spec-circle",
      faces: "faces",
      vertices: "vertices",
      zeros: "zeros",
      south: "south",
      chords: "chords",
      dirs: "dirs",
    };
    return map[key] || key;
  }

  // ---------------------------------------------------------------------
  // Controls: sliders, checkboxes, mouse drag, wheel
  // ---------------------------------------------------------------------
  function attachSliders() {
    const rotX = document.getElementById("rot-x");
    const rotY = document.getElementById("rot-y");
    const zoom = document.getElementById("zoom");
    rotX.addEventListener("input", e => {
      state.rotX = parseFloat(e.target.value) * Math.PI / 180;
      render();
    });
    rotY.addEventListener("input", e => {
      state.rotY = parseFloat(e.target.value) * Math.PI / 180;
      render();
    });
    zoom.addEventListener("input", e => {
      state.zoom = parseFloat(e.target.value) / 100;
      render();
    });
  }

  function attachCheckboxes() {
    const pairs = [
      ["layer-mesh", "mesh"],
      ["layer-geo-circle", "geoCircle"],
      ["layer-spec-circle", "specCircle"],
      ["layer-faces", "faces"],
      ["layer-vertices", "vertices"],
      ["layer-zeros", "zeros"],
      ["layer-south", "south"],
      ["layer-chords", "chords"],
      ["layer-dirs", "dirs"],
    ];
    for (const [id, key] of pairs) {
      const el = document.getElementById(id);
      if (!el) continue;
      el.addEventListener("change", e => {
        state.layers[key] = e.target.checked;
        render();
      });
    }
  }

  function attachDrag() {
    let dragging = false;
    let lastX = 0, lastY = 0;

    function start(e) {
      dragging = true;
      const t = e.touches ? e.touches[0] : e;
      lastX = t.clientX; lastY = t.clientY;
      if (e.preventDefault) e.preventDefault();
    }
    function move(e) {
      if (!dragging) return;
      const t = e.touches ? e.touches[0] : e;
      const dx = t.clientX - lastX;
      const dy = t.clientY - lastY;
      lastX = t.clientX; lastY = t.clientY;
      state.rotY += dx * 0.01;
      state.rotX += dy * 0.01;
      // Clamp for readability
      state.rotX = clamp(state.rotX, -Math.PI / 2 + 0.05, Math.PI / 2 - 0.05);
      document.getElementById("rot-x").value = rad2deg(state.rotX).toFixed(0);
      document.getElementById("rot-y").value = rad2deg(state.rotY).toFixed(0);
      render();
    }
    function end() { dragging = false; }

    svg.addEventListener("mousedown", start);
    window.addEventListener("mousemove", move);
    window.addEventListener("mouseup", end);
    svg.addEventListener("touchstart", start, { passive: false });
    window.addEventListener("touchmove", move, { passive: false });
    window.addEventListener("touchend", end);

    svg.addEventListener("wheel", e => {
      e.preventDefault();
      const delta = e.deltaY > 0 ? -0.05 : 0.05;
      state.zoom = clamp(state.zoom + delta, 0.4, 2.2);
      document.getElementById("zoom").value = Math.round(state.zoom * 100);
      render();
    }, { passive: false });
  }

  function clamp(x, lo, hi) { return x < lo ? lo : x > hi ? hi : x; }

  function attachStepNav() {
    document.getElementById("prev-step").addEventListener("click", () => {
      state.stepIdx--;
      renderStep();
    });
    document.getElementById("next-step").addEventListener("click", () => {
      state.stepIdx++;
      renderStep();
    });
    document.addEventListener("keydown", e => {
      if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName)) return;
      if (e.key === "ArrowLeft") { state.stepIdx--; renderStep(); }
      if (e.key === "ArrowRight") { state.stepIdx++; renderStep(); }
    });
  }

  function attachActions() {
    const animBtn = document.getElementById("btn-anim");
    const resetBtn = document.getElementById("btn-reset");

    animBtn.addEventListener("click", () => {
      state.animating = !state.animating;
      animBtn.classList.toggle("active", state.animating);
      if (state.animating) {
        tickAnimation();
      } else if (state.animHandle) {
        cancelAnimationFrame(state.animHandle);
      }
    });

    resetBtn.addEventListener("click", () => {
      state.rotX = 25 * Math.PI / 180;
      state.rotY = -30 * Math.PI / 180;
      state.zoom = 1.0;
      document.getElementById("rot-x").value = 25;
      document.getElementById("rot-y").value = -30;
      document.getElementById("zoom").value = 100;
      render();
    });
  }

  function tickAnimation() {
    if (!state.animating) return;
    state.rotY += 0.006;
    if (state.rotY > Math.PI) state.rotY -= 2 * Math.PI;
    document.getElementById("rot-y").value = rad2deg(state.rotY).toFixed(0);
    render();
    state.animHandle = requestAnimationFrame(tickAnimation);
  }

  // ---------------------------------------------------------------------
  // Populate side panels (definition, quotes, sources)
  // ---------------------------------------------------------------------
  function populatePanels() {
    const def = D.definition || {};
    document.getElementById("def-one-line").textContent = def.one_line || "";
    document.getElementById("def-crossed").textContent = def.crossed_product || "";

    const defQuotes = document.getElementById("def-quotes");
    defQuotes.innerHTML = "";
    (def.quotes || []).forEach(q => {
      const li = document.createElement("li");
      const src = document.createElement("span");
      src.className = "quote-source";
      src.textContent = q.source;
      li.appendChild(src);
      li.appendChild(document.createTextNode(q.text));
      defQuotes.appendChild(li);
    });

    // Headline quotes.
    const qList = document.getElementById("quotes-list");
    qList.innerHTML = "";
    (D.quotes || []).forEach(q => {
      const li = document.createElement("li");
      const src = document.createElement("span");
      src.className = "quote-source";
      src.textContent = q.source;
      li.appendChild(src);
      li.appendChild(document.createTextNode(q.text));
      qList.appendChild(li);
    });

    // Source files.
    const sList = document.getElementById("sources-list");
    sList.innerHTML = "";
    (D.source_files || []).forEach(f => {
      const li = document.createElement("li");
      li.textContent = f;
      sList.appendChild(li);
    });

    // Factoids.
    const geoN = D.faces.filter(f => f.circle === "geometric").length;
    const specN = D.faces.filter(f => f.circle === "spectral").length;
    const bothN = D.faces.filter(f => f.circle === "both").length;
    document.getElementById("fact-faces").textContent =
      D.faces.length + " faces / " +
      geoN + " geometric / " + specN + " spectral / " + bothN + " bridge";

    document.getElementById("fact-vertices").textContent =
      D.vertices.length + " vertices / " +
      "NORTH avg " + (D.south_trough ? D.south_trough.avg_conf_north : "?") + " / " +
      "SOUTH avg " + (D.south_trough ? D.south_trough.avg_conf_south : "?");

    const r = D.radii || {};
    document.getElementById("fact-radii").textContent =
      "physical R = " + (r.physical_R_microns != null ? r.physical_R_microns + " um" : "N/A") +
      " / visual R=" + (r.major_R_visual || "?") + " r=" + (r.minor_r_visual || "?");

    document.getElementById("built-at").textContent = D.generated_at || "?";
  }

  // ---------------------------------------------------------------------
  // Init
  // ---------------------------------------------------------------------
  function init() {
    populatePanels();
    attachSliders();
    attachCheckboxes();
    attachDrag();
    attachStepNav();
    attachActions();
    renderStep();    // render first step and view
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
