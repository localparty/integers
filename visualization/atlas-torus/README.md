# Atlas Torus Proof-Chain Composer

*The Integers programme's primary interactive delivery artifact. 25 ring-vertex proof chains on the surface of a torus T² = S¹ × S¹. Shipped as part of the "Integers — First Release" Zenodo bundle.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Ship target

**`ux-strategy-E-composition.html`** — the final, polished visualization. Open directly:

```
open visualization/atlas-torus/ux-strategy-E-composition.html
```

File:// compatible (Three.js via CDN import-map from unpkg). No dev server required. Dark theme.

---

## Design iteration trail

Seven HTML files document the design evolution from first prototype to ship-ready artifact. Each iteration isolates one rendering or interaction concern. The trail is preserved intentionally — it demonstrates iterative human-driven engineering discipline, not single-shot generation.

| # | File | Size | What it solved |
|---|---|---|---|
| 0 | `index.html` | 66 KB | **First prototype.** Joint build (G + Claude Opus). Three.js + OrbitControls, 247 nodes on torus surface, 4-column panel, 4 mode toggles, free-form CONNECT workflow, proximity-select while spinning, auto-rotate + auto-tube (Clifford flow). Adversarial-tested: 2,052 actions, 0 errors, converged. |
| — | `ux-strategy.html` | 115 KB | **UX redesign.** Compact layout, Controls + Slides bottom panel, 14-slide educational deck, camera sliders (pitch/yaw/roll/posX/Y/Z/zoom/tube), speed control, reset/animate buttons. |
| A | `ux-strategy-A-instanced.html` | 117 KB | **Instanced rendering.** Node meshes switched to InstancedMesh for GPU-efficient rendering of 247 spheres. Performance baseline for all subsequent iterations. |
| B | `ux-strategy-B-lazy-paths.html` | 118 KB | **Lazy path computation.** Chain-curve geometry computed on demand (when solution activated), not at load time. Reduces initial load + memory footprint. Responsiveness improved for multi-solution activation. |
| C | `ux-strategy-C-shader-surface.html` | 117 KB | **Shader-based torus surface.** Replaced wireframe with custom ShaderMaterial — torus rendered as a cloud of tiny dots (point-cloud aesthetic). Nodes and curves stand out against the star-field-like surface. Visual quality leap. |
| D | `ux-strategy-D-shader-surface.html` | 117 KB | **Shader refinement.** Alpha compositing, depth-sorting, and blending fixes for the point-cloud surface. Stability pass — eliminates z-fighting and transparency artifacts from iteration C. |
| E | `ux-strategy-E-composition.html` | 127 KB | **Final compositing.** Hose/tube curves (volumetric chain rendering), alpha=1/N brightness scaling for multi-solution overlap visibility, √multiplicity line thickness, 1.4× node invariant sizing, hover-freeze interaction, scroll+flash feedback, dispose discipline for GPU memory. **Ship target.** |

### What the iteration trail proves

- **Human-driven design**: each iteration name (A through E) was chosen by G to isolate a specific rendering concern. The progression shows deliberate architectural refinement.
- **AI-assisted implementation**: Claude Opus assisted with data extraction (25 X-RAY.md → atlas-torus-data.js), interaction logic (modes, connect, proximity-select), and slide content. The rendering innovations (shader surface, hose curves, compositing) are G's design decisions.
- **Engineering discipline**: no "generate everything in one shot" pattern. Five named checkpoints, each verifiable by opening the file in a browser.
- **Adversarial testing**: the prototype (`index.html`) was tested to convergence (2,052 actions, 0 errors). The ship target (`E-composition`) inherits the same interaction logic + is being tested separately.

### For reviewers / auditors

Open any file in the sequence to see the progression. Each is self-contained (file:// compatible, same data file). The visual difference between `index.html` (wireframe torus, thin-line arcs) and `E-composition` (point-cloud surface, hose curves, shared-path visibility) is the design evolution visible at a glance.

---

## Data

| File | Description |
|---|---|
| `atlas-torus-data.js` | 247 nodes, 861 edges, 102 Integers-original, 7 bypass-routes. Generated from 25 X-RAY.md files. |
| `build-atlas-torus.py` | Python build script. Parses `strategy/x-ray/proof-chain/*/X-RAY.md` → emits `atlas-torus-data.js`. |

Rebuild data:
```
cd /Users/gsix/quantum-geometry-in-5d-latex
python3 visualization/atlas-torus/build-atlas-torus.py
```

---

## 14-slide educational deck (embedded in the viz)

The Slides panel (bottom-right of the viz, expand via ▾ tab) contains 14 slides that explain Integers to a first-time visitor:

| # | Title | What it covers |
|---|---|---|
| 1 | Integers | Programme intro — derivation from ℤ, rung-7 necessity |
| 2 | The Torus | T² = S¹ × S¹, geometric + spectral circles, 10 faces |
| 3 | The Physics | Paper 1, M⁵ = M⁴ × S¹, Universal Epstein Vanishing |
| 4 | The Six Projections | P_A..P_E..P_O, every node carries its operator |
| 5 | The 25 Solutions | 6 Clay + 2 additional + 17 community-standard |
| 6 | How to Operate | Click / watch / toggle / compose interaction tour |
| 7 | The Four Modes | Compliance / Independence / Contribution / Geodesic |
| 8 | The Golden Dots | Color legend with inline dots — Gold / Sky-blue / Rose / Violet / Green / Teal |
| 9 | The Hub is Different | qg5d zigzag = branched tree, not linear chain |
| 10 | Two Classes Become Visible | Prize-paper structural law: advanced (76-85% gold) vs frontier (≤13% gold) |
| 11 | The Three Pillars | Compliance / Independence / Contribution per vertex |
| 12 | Pillar D — Derive-and-Offer | Community-led external rederivation from ℤ + ZFC |
| 13 | Reciprocity | HONOR / RECOGNIZE / SHOWCASE / POSITION / SOURCE |
| 14 | How to Engage | Audit / Criticize / Cite / Collaborate |

---

## Sibling visualizations

| Viz | Path | Role |
|---|---|---|
| Main 43-shape viewer | `visualization/index.html` | Programme-wide shape browser |
| Torus (Paper 60) | `visualization/torus/index.html` | Paper 60 §17 torus with 10 faces |
| Clifford torus | `visualization/clifford-torus.html` | Paper 60 geometric torus viewer |
| Hub explorer (Pillar D) | `visualization/pillar-d-hub-explorer.html` | Hub-cluster comparison for Pillar D direction |

---

## Strategy documents

- `strategy/atlas-torus-run.md` — orchestrator run prompt (Phase A ship / Phase B enhance / Phase C door)
- `strategy/north-star.md` §2.5 — The Atlas Opener (settled strategy)
- `strategy/pillar-d/00-architecture.md` — Pillar D architecture (community-led)
- `strategy/independent-rewrite-roadmap.md` — Prize-paper rewrite sequencing

---

*The atlas torus IS the delivery artifact. Operate it, don't read about it.*
