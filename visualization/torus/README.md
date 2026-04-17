# Torus Visualization -- Paper 60

An interactive 3D view of the torus defined in paper 60
("The Geometry of the Circle") of the quantum-geometry-in-5D programme.

This is a companion to the main projections viewer. Where the main viewer
shows the 25-vertex ring projected flat, this viewer shows the ring **on
the torus surface** together with:

- the 10 faces of the e-circle (5 geometric + 5 spectral + SPREAD bridging)
- the two generating circles (geometric / spectral)
- the Riemann-zero intersection points
- the south trough and the ellipse diagnostic
- cross-cut chords between S-dual face pairs
- poloidal / toroidal direction labels

Built from what paper 60 actually says about the torus, sections 17-22 and 28.

## Files

```
visualization/torus/
├── index.html        -- page shell
├── style.css         -- dark-theme styling
├── app.js            -- SVG renderer + controls
├── build.py          -- scans paper 60, emits data.js
├── data.js           -- generated TORUS_DATA constant
├── build.log         -- generator log (parse uncertainties)
└── README.md         -- this file
```

Everything is vanilla HTML/CSS/JS and Python 3 stdlib. No frameworks, no
npm, no CDN, no external dependencies. Works from `file://` directly.

## How to open

1. Open `visualization/torus/index.html` in any modern browser
   (macOS: `open visualization/torus/index.html`).
2. Drag the torus with the mouse to rotate. Mouse-wheel or the slider to
   zoom. Click `auto-rotate` for a slow automatic spin.
3. Toggle layers with the checkboxes.
4. Step through the 7-step explanation with the `<-` / `->` buttons in
   the side panel (or arrow keys on the keyboard).

## How to regenerate data.js

If paper 60 changes (new faces, revised confidence scores, new quotes),
rerun:

```bash
python3 visualization/torus/build.py
```

This reads every markdown file in `integers/paper60-geometry-of-circle/`
and rewrites `data.js`. Parse uncertainties are logged to `build.log`.

## What the torus means (paper 60 summary)

Paper 60's central insight: the programme's geometry is **T^2 = S^1_geo x
S^1_spec**, a torus formed by two circles.

- **The geometric circle (S^1_geo)** is the e-dimension -- Paper 1's
  U(1) fiber of five-dimensional spacetime, physical radius
  R ~ 10.10 um. It is where things LIVE. Five faces sit along it:
  TOPOLOGY (Lehmer), HARMONICS (Collatz), MEASURE (Sato-Tate),
  CURVATURE (Yang-Mills), and half of SPREAD (QUE).

- **The spectral circle (S^1_spec)** is the modular flow sigma_t on
  the BC algebra at the KMS_1 critical inverse temperature. It is HOW
  the flow traverses. Five faces sit along it: DYNAMICS (Cramer),
  AMPLITUDE (Lindeloef), SYMMETRY (Katz-Sarnak), ARITHMETIC (Goldbach/
  Twin Primes), RESONANCE (Selberg). Plus the other half of SPREAD.

- **The crossed product** A_BC x_sigma R IS the torus -- operator-
  algebraically, the type II_infinity unfolding of the type III_1 BC
  factor encodes both circles simultaneously.

- **The Riemann zeros** are where the two generating circles cross on
  the surface. RH says those crossings are transversal. If RH fails,
  the torus degenerates.

- **The 25 ring vertices** are the programme's methodological stops.
  Their confidence distribution is lopsided -- an ellipse with NORTH
  (QG5D 10/10) and SOUTH (Goldbach, Twin Primes, Schanuel, VP all 1/10)
  poles. The major axis of the ellipse points SOUTH -- the direction
  the programme must focus on.

## Geometric conventions

The renderer uses a standard torus parametrisation:

```
x = (R + r cos v) cos u
y = (R + r cos v) sin u
z = r sin v
```

where u in [0, 2pi) runs around the major (toroidal / geometric) loop
and v in [0, 2pi) runs around the tube (poloidal / spectral) cross-
section. Radii R, r are visual defaults (3.0, 1.0); paper 60 gives
R ~ 10.10 um for the physical e-circle but does not give a numerical
tube radius, so the visualization uses aesthetic values.

Faces are placed at:

- geometric face: v = +pi/2  (top of tube, outer-top arc)
- spectral face:  v = -pi/2  (bottom of tube, outer-bottom arc)
- both (SPREAD):  v =  0     (equator -- bridging)

Ring vertices are placed around the major loop at 25 equi-spaced
positions, with tube-coordinate v offset by zone:

- NORTH zone: v = +0.35 (pushed outward-top)
- SOUTH zone: v = -0.35 (pushed inward-bottom)
- EAST / WEST: v = 0 (equator)

This makes the ellipse visible as a 3D distortion of the ring.

Riemann zeros are placed at v = 0 -- the equator, which paper 60/18
identifies as the critical-line intersection locus. The first 12
zero ordinates gamma_n are wrapped mod 2pi around the major loop.

## Controls reference

| Control | Action |
|---|---|
| Mouse drag on torus | Rotate (X drag = yaw, Y drag = pitch) |
| Mouse wheel on torus | Zoom |
| rotate X / Y sliders | Rotate via slider |
| zoom slider | Zoom via slider |
| Layer checkboxes | Toggle individual overlays |
| auto-rotate button | Start / stop slow rotation |
| reset view button | Return to default view |
| Arrow keys / step nav | Next / previous explanation step |

## Layers

| Layer | What it shows | Colour |
|---|---|---|
| torus mesh | Wireframe of the torus surface | cyan |
| geometric circle | The major generating loop | green |
| spectral circle | The minor (tube) generating loop | violet |
| 10 faces | Face markers + labels | green / violet / amber |
| 25 ring vertices | Ring vertices sized by confidence | zone-colour |
| Riemann zeros | First 12 gamma_n at the equator | white on amber |
| south trough | Pink dashed arc + ellipse rings | pink |
| cross-cut chords | S-dual face-pair chords | amber |
| poloidal / toroidal labels | Direction labels | tinted |

## The 7 explanation steps

1. Start from M^5 = M^4 x S^1
2. Add the modular flow -- the second circle
3. The crossed product IS the torus
4. The 10 faces live on the torus surface
5. The 25 ring vertices sit on the major loop
6. The south trough + ellipse diagnostic
7. Riemann zeros are the intersection points

Each step cites paper 60 sections and highlights the corresponding
overlay automatically.

## Parse uncertainties

See `build.log`. Any probe that failed to match its expected text in
paper 60 is flagged `NEEDS-VERIFICATION`. Current run: all 7 headline
quote probes passed; R ~ 10.10 um confirmed; face/vertex/zone data is
hand-transcribed from paper60/17 grid and paper60/28 diagram (not
regex-extracted -- those diagrams are ASCII tables, so the positions
are encoded directly in `FACES_CANONICAL` and `RING_VERTICES_CANONICAL`
in build.py).

## Source papers

- paper60/00-table-of-contents.md    -- overview
- paper60/17-two-circles-one-torus.md   -- definition (core)
- paper60/18-riemann-zeros-as-intersection.md -- zeros
- paper60/19-rh-as-existence-of-the-torus.md  -- RH
- paper60/20-the-ellipse-and-the-missing-faces.md -- ellipse + 10 faces
- paper60/28-the-south-trough-needs-lifting.md    -- south trough
- paper60/07 through /14                   -- individual face files
- paper60/21-the-s-duality.md              -- S-dual pairs (chords)

## License / context

Part of the quantum-geometry-in-5d-latex programme.
G Six (originator) and Claude Opus 4.6 (collaborator). San Francisco CA, 2026.
