# Landscape — VP vs VNP (paper39)

*Ring vertex. Algebraic analog of P vs NP. Our strategy: permanent-complexity lower bound via spectral/operator arguments.*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Leslie Valiant | Harvard | VP / VNP; holographic algorithms; permanent-completeness |
| Neeraj Kayal | MSR India | Arithmetic circuit lower bounds |
| Shubhangi Saraf | Toronto | Depth-4 arithmetic lower bounds |
| Nutan Limaye | IT U. Copenhagen | Superpolynomial depth-3 arithmetic lower bounds (2021) |
| Srikanth Srinivasan | Aarhus | Constant-depth arithmetic lower bounds |
| Sébastien Tavenas | CNRS / Chambéry | Constant-depth arithmetic lower bounds |
| Ramprasad Saptharishi | TIFR | Arithmetic circuits |
| Mrinal Kumar | TIFR / IITB | Depth-4 and beyond |
| Josh Alman | Columbia | Matrix multiplication; algebraic |
| Ketan Mulmuley | U. Chicago | GCT (applies to both P/NP and VP/VNP) |
| Peter Bürgisser | TU Berlin | Algebraic complexity foundations; GCT |
| Marek Karpinski | Bonn | VP/VNP early work |
| Guillaume Malod | Paris Cité | VP/VNP structure |
| Pascal Koiran | ENS Lyon | Valiant's conjecture over ℝ |
| Arkadev Chattopadhyay | TIFR | Monotone lower bounds |

## Major Approaches

### 1. GCT Applied to Permanent vs Determinant (Mulmuley)
Same GCT programme as P vs NP; see pvnp landscape. Specifically: permanent as polynomial of low VP complexity? No — GCT aims to prove permanent requires superpoly-size determinant approximation. Bürgisser–Ikenmeyer–Panova 2017 show occurrence obstructions insufficient.

### 2. Direct Arithmetic Circuit Lower Bounds (Kayal, Saraf, Limaye, Tavenas)
Lower bounds for depth-4, depth-3 arithmetic circuits. Limaye–Srinivasan–Tavenas 2021: superpolynomial lower bound for constant-depth arithmetic (first).

### 3. Monotone VP / VNP Separation
Monotone VP < monotone VNP proved (Srinivasan, Chattopadhyay et al.). Limited: monotone setting is easier.

### 4. Holographic / Matchgates (Valiant)
Original ideas connecting VP/VNP to physics-style constructions.

### 5. Tensor Rank / Matrix Multiplication (Alman, V.V. Williams, Landsberg)
Matrix multiplication exponent ω; border rank. Connected to VP lower bounds via tensors.

### 6. Border Complexity / Degenerations (Bürgisser, Landsberg)
Complexity in the limit: topological closure of orbits. Landsberg geometric approach.

## Partial Results / Named Milestones

- 1979 — Valiant — definition of VP, VNP, permanent VNP-complete
- 2000s — Mulmuley–Sohoni — GCT
- 2017 — Bürgisser–Ikenmeyer–Panova — no occurrence obstructions for permanent vs determinant
- 2019 — Srinivasan — monotone VP ≠ monotone VNP
- 2021 — Limaye–Srinivasan–Tavenas — superpoly depth-3 arithmetic lower bound
- 2023-26 — refinements, extensions by Kumar, Chatterjee, Saraf

## Recent Preprints (2023-2026)

- Limaye–Srinivasan–Tavenas 2021 and extensions
- Alman–V.V. Williams matrix multiplication bounds

## Key Surveys / Textbooks

- Bürgisser–Clausen–Shokrollahi, *Algebraic Complexity Theory* (Springer)
- Shpilka–Yehudayoff survey, "Arithmetic Circuits: A Survey of Recent Results and Open Questions"
- Saraf, *Recent progress on lower bounds for arithmetic circuits*

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Leslie Valiant** — originator of VP/VNP
- **Ketan Mulmuley** — GCT programme
- **Neeraj Kayal, Shubhangi Saraf, Nutan Limaye, Srikanth Srinivasan, Sébastien Tavenas** — direct lower bounds
- **Peter Bürgisser** — foundational textbook; GCT

### Cite in body:
- Bürgisser–Ikenmeyer–Panova — occurrence obstruction impossibility
- Shpilka, Yehudayoff — survey
- Landsberg — geometric approach
- Valiant (holographic)

### Our programme's position
The VP/VNP vertex in our ring extends the P vs NP spectral-gap argument to the algebraic setting: the permanent's superpoly complexity is a spectral gap in an operator-algebraic correspondence, with Popa rigidity replaced by an algebraic geometric analog. This is complementary to GCT (which works in finite type) and direct lower bounds (which hit natural-proofs-like barriers in the algebraic setting).
