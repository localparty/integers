# Projections of the 5D Geometry — Viewer

An interactive HTML visualization of the programme's projection inventory.
Every mathematical shape we see is a projection of the 5D geometry
$M^5 = M^4 \times S^1$ into 4D. A slider walks through 43 shapes — the
e-circle, the bouquet of six rings, the core QG5D node, five inner-ring
branches (A–E), six projection operators $(P_A,\dots,P_O)$, twenty-four
outer-ring conjectures, and five composite shapes.

All data is extracted **dynamically** from `strategy/` and `paper*`
directories by `build.py`. Nothing is hardcoded — running build.py again
tomorrow after new audit runs land will pick up the new data automatically.

## Quick start

```bash
# 1. Regenerate data.js from the current repo state
python3 visualization/build.py

# 2. Open the viewer in a browser (works under file://)
#    macOS:
open visualization/index.html
#    Linux:
xdg-open visualization/index.html
#    or: drag-and-drop visualization/index.html onto any browser window
```

No server, no npm, no CDN, no internet. Pure HTML + CSS + vanilla JS +
Python 3 stdlib.

## Files

| File           | Purpose                                                |
|----------------|--------------------------------------------------------|
| `index.html`   | Viewer page — slider, canvas panel, metrics, footnotes |
| `style.css`    | Dark theme                                             |
| `app.js`       | Slider logic + per-class SVG rendering                 |
| `build.py`     | Scans programme, emits `data.js`                       |
| `data.js`      | Generated — contains the global `SHAPE_DATA`           |
| `build.log`    | Generated — per-run parse log                          |
| `README.md`    | This file                                              |

## Controls

- Drag the slider, or use **←** / **→** arrow keys, or the **←** / **→**
  buttons in the top bar.
- On the e-circle view, click a face marker to highlight that face.

## Shape inventory (43 positions)

### Row 1 — Foundational (3)
1. e-circle ($S^1$, $R \approx 10.10$ μm) — paper60
2. Bouquet topology (6-ring wedge sum) — paper61
3. Core QG5D ($M^5 = M^4 \times S^1$, 22 theorems) — paper1

### Row 2 — Inner rings (5)
4. Branch A — Quantum (9 items)
5. Branch B — Gravity (4 items)
6. Branch C — Cosmology (10 items)
7. Branch D — CBB (5 axioms + operator dictionary)
8. Branch E — 36 Pins (36 sub-percent predictions)

### Row 3 — Projection operators (6)
9. $P_A$ Quantum projection
10. $P_B$ Gravity projection
11. $P_C$ Cosmology projection
12. $P_D$ CBB projection
13. $P_E$ Pins projection
14. $P_O$ Outer projection

### Row 4 — Outer-ring vertices (24)
15. YM (Millennium) — 16. RH (Millennium) — 17. GRH — 18. Lindelöf —
19. BSD (Millennium) — 20. H12 — 21. NS (Millennium) — 22. Turbulence —
23. Hodge (Millennium) — 24. Baum-Connes — 25. PvNP (Millennium) —
26. VP-vs-VNP — 27. BGS — 28. Katz-Sarnak — 29. Twin Primes —
30. Cramér — 31. Goldbach — 32. ABC — 33. OPN — 34. Collatz —
35. Lehmer — 36. Sato-Tate — 37. Schanuel — 38. Hilbert 6

(The hub vertex qg5d is already at position 3 above.)

### Row 5 — Composite shapes (5)
39. 36-pin circle (pin constellation)
40. Chord graph (cross-cuts between vertices)
41. Face graph (10 faces of the e-circle)
42. South trough / ellipse (loopsidedness diagnostic — paper60 §28)
43. Outer ring as a whole (25-vertex ring + chord overlay)

## Data sources

For each shape, `build.py` pulls from whichever of these canonical
sources apply:

- **Ring-vertex audit bundles** (`strategy/<vertex>/`):
  - `00-millenium-strategy.md` — source type, N requirements, named walls
  - `pac-output/runs/run-NN/compliance-map.md` — M × N matrix size,
    verdict distribution (PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT)
  - `deliverables/*-bare.md` / `*-beyond-bare.md` — line / theorem counts
- **X-ray atlas** (`strategy/x-ray/proof-chain/<vertex>/X-RAY.md`):
  - §5 face histogram (TOPOLOGY … SPREAD)
  - §6 projection histogram ($P_A, P_B, \dots$)
  - Cross-cut count, primary face / projection / branch
- **Cross-cut edges** (`strategy/x-ray/pac-output/runs/run-01/cross-cut-edges.md`)
- **Live paper chains** (`paperNN/PROOF-CHAIN.md`):
  - Status line, layer count, first-paragraph description
- **Pin master table** (`paper12/research/23-framework-predictions-master-table.md`)
- **Paper 60 (e-circle geometry)** — faces, south-trough diagnostic
- **Paper 61 (projections)** — bouquet, P_X projection operators

When data is missing, the shape falls back to an **AUDIT PENDING**
placeholder with the paper reference preserved. The build always
succeeds.

## Regeneration workflow

After new audit runs, new PROOF-CHAINs, new x-ray entries, or new
strategy bundles are added:

```bash
python3 visualization/build.py
# inspect:
tail visualization/build.log
# then reload the browser tab
```

The current build produces **43 shapes** with **5 AUDIT PENDING**
placeholders (the five inner-ring branches A–E, which don't yet have
filled `strategy/inner-rings/branch-*/pac-output/` bundles).

## Design notes

- Dark theme: `#0a0a0f` background with SF Mono / Fira Code / Consolas
  for data and Inter for labels.
- Verdict palette: cyan (PROVED) / amber (PARTIAL) /
  pink (OPEN-BUT-ADDRESSED) / red (SILENT) — chosen to match the
  programme's standard.
- Millennium problems are marked with a violet dot and badge.
- The e-circle has 10 clickable face markers (paper60 §13).
- `data.js` is a JS file defining a global `const SHAPE_DATA`; this
  avoids `fetch()` so the viewer works under the `file://` protocol
  without a server.
