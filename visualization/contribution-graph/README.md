# Contribution Graph Visualization

The programme's persuasion viz: across the 25-vertex ring, show what we COMPLY
with, what we lifted to be INDEPENDENT, and what we CONTRIBUTE back to the
field — in one picture.

## Files

- `index.html` — page shell (SVG ring + comparison panel + legend)
- `style.css` — dark theme (matches torus + main 43-shape viewer)
- `app.js` — vanilla JS rendering + interactions
- `build.py` — Python 3 stdlib; scans `strategy/` and emits `data.js`
- `data.js` — auto-generated; defines the global `CONTRIBUTION_DATA`
- `build.log` — last build's parse log (skips, anomalies, file sizes)

## Build

```sh
python3 visualization/contribution-graph/build.py
```

This walks every vertex directory under `strategy/`, parses the four
deliverables (`*-comply-bare.md`, `*-independence-bare.md`, `*-harden-bare.md`,
`*-beyond-bare.md`), the run-02 compliance map, the run-05 PAC primitive log,
the run-06 commit memo, and the x-ray cross-cut edges. Robust to missing
files; vertices without deliverables render as `AUDIT PENDING`.

## View

Open `visualization/contribution-graph/index.html` in any modern browser.
Pure `file://` access — no server required, no CDN.

## What the picture shows

- **25-vertex ring** — every programme target, in canonical order matching the
  torus visualization.
- **Three concentric layers per vertex**:
  - inner (slate)  = COMPLY baseline arc length scales with theorem count
  - middle (amber) = INDEPENDENT lift size scales with theorem count
  - outer (cyan)   = CONTRIBUTE gift size scales with theorem count
- **Cross-cut chords** (pink) — verified shared invariants between vertices;
  speculative edges drawn dashed/faint.
- **Hover** any vertex slot for a tooltip with per-pillar counts.
- **Click** any vertex for a side-by-side Comply/Independent/Contribute
  comparison: theorem counts, named walls (strictly narrowing across A→B→C),
  PAC primitive bar (BYP/DEC/EXC/TRP), externals inventoried, beyond-bonus,
  and landscape acknowledgments.

## Today's coverage

The six Millennium vertices ship a full 4-deliverable stack:
`ym`, `rh`, `bsd`, `pvnp`, `hodge`, `ns`.
The remaining 19 ring slots render as `AUDIT PENDING` (brief + strategy on
disk; deliverables queued).

## Color contract

| Color  | Pillar      | Meaning                                              |
|--------|-------------|------------------------------------------------------|
| slate  | COMPLY      | what the prize requires; what's already in the chain |
| amber  | INDEPENDENT | what we lifted (PAC primitives applied)              |
| cyan   | CONTRIBUTE  | what we gave back to the field (hardened externals)  |
| violet | BEYOND      | bonus cross-Clay theorems + acknowledgments          |
| pink   | edges       | cross-cut: verified solid, speculative dashed        |
| red    | named walls | the residual obstruction at each pillar              |
