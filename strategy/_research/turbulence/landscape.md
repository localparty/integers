# Landscape — Turbulence / Onsager / K41 (paper38)

*Ring vertex. Our strategy: geometric turbulence via 5D regularization.*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Gregory Eyink | JHU | Onsager's "ideal turbulence" theory; dissipation anomaly |
| Philip Isett | Caltech | Proof of Onsager's 1/3 threshold |
| Camillo De Lellis | IAS | Convex integration; Onsager |
| László Székelyhidi | Leipzig | Convex integration; Onsager |
| Tristan Buckmaster | Princeton / NYU | Onsager; convex integration |
| Vlad Vicol | Courant | Onsager; energy dissipation |
| Nigel Goldenfeld | UCSD | Turbulence statistics; symmetry approaches |
| Dan Eyink | JHU | (same as Gregory above) |
| Edriss Titi | Cambridge | Shell models; turbulence |
| Uriel Frisch | Obs. Côte d'Azur | Kolmogorov K41; intermittency |
| Luca Biferale | Rome Tor Vergata | DNS; shell models |
| Roberto Benzi | Rome Tor Vergata | Multifractals |
| Katepalli Sreenivasan | NYU | Experimental turbulence; K41 |
| Gregory Falkovich | Weizmann | Turbulence theory; intermittency |
| Alexei Mailybaev | IMPA | Exact solutions, turbulence |
| Gregory Eyink | JHU | Ideal turbulence |
| Susan Kurien | LANL | Computational turbulence |
| Vladimir Sverak | Minnesota | Rigorous NS; connection to turbulence |

## Major Approaches

### 1. Onsager's Conjecture (Isett 2018; De Lellis–Székelyhidi, Buckmaster–Vicol)
Onsager conjectured 1949: 1/3 Hölder regularity is the sharp threshold for conservation of energy in Euler equations. Below: anomalous dissipation; above: conserved. Isett (2018) proved the sharp 1/3 threshold; before that De Lellis–Székelyhidi had convex integration constructions below 1/10.

### 2. Convex Integration / Dissipative Euler Solutions
Construct Hölder 1/3 - ε dissipative solutions (Buckmaster–De Lellis–Székelyhidi–Vicol). Shows Onsager's threshold is sharp both ways.

### 3. K41 / Kolmogorov Scaling
Predictions: structure functions scale with exponents n/3. Experimentally verified but exhibits intermittency corrections. Rigorous derivation missing.

### 4. Multifractal / Intermittency (Parisi–Frisch, Benzi–Biferale)
K41 corrected by multifractal spectrum. She–Leveque formula for structure functions.

### 5. Dyadic / Shell Models (Eyink, Titi, Katz-Pavlovic)
Simplified nonlinear ODE models that mimic turbulence. Easier to analyze rigorously.

### 6. Stochastic / Random Cascade (Flandoli, Kupiainen)
Stochastic NS/Euler as turbulence model.

### 7. Experimental / Wind Tunnel / DNS
Benchmark data; high-Reynolds simulations (Kaneda, Ishihara).

## Partial Results / Named Milestones

- 1941 — Kolmogorov — K41 theory
- 1949 — Onsager — anomalous dissipation conjecture, 1/3 threshold
- 1994 — Eyink — partial Onsager for smooth approximations
- 1994 — Constantin–E–Titi — above 1/3 energy is conserved
- 2008 — De Lellis–Székelyhidi — convex integration for Euler (below 1/10)
- 2017-18 — Isett — Onsager 1/3 proof (sharpness)
- 2024 — Eyink — Onsager's ideal turbulence review

## Recent Preprints (2023-2026)

- arXiv:2404.10084 — Eyink, "Onsager's 'Ideal Turbulence' Theory"
- msp.org APDE 2024 — endpoint regularity in Onsager's conjecture
- Convex integration refinements by Buckmaster–Masmoudi–Novack–Vicol

## Key Surveys / Textbooks

- Frisch, *Turbulence: The Legacy of A.N. Kolmogorov* (Cambridge 1995)
- Monin–Yaglom, *Statistical Fluid Mechanics*
- Eyink "Onsager's 'Ideal Turbulence'" (2024)
- Buckmaster–Vicol survey

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Lars Onsager** (1903-76) — originator of the anomalous-dissipation conjecture
- **Gregory Eyink** — modern Onsager theory
- **Philip Isett, De Lellis, Székelyhidi** — 1/3 theorem
- **Uriel Frisch, Katepalli Sreenivasan** — experimental/K41

### Cite in body:
- Kolmogorov — K41 origin
- Constantin, E, Titi — above-threshold conservation
- Buckmaster, Vicol, Masmoudi — convex integration refinements
- Benzi, Parisi, Frisch, Biferale — multifractals

### Our programme's position
Our contribution is geometric: turbulence is treated as the projection of smooth 5D flow onto 3+1D spacetime, with Onsager's 1/3 threshold recovered as the regularity gained under projection. We cite Isett/Eyink as the definitive statement of the Onsager threshold and show our 5D flow satisfies the required regularity without convex integration tricks.
