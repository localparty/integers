# Landscape — P vs NP (paper28)

*Millennium target. Our strategy: spectral-gap + Popa rigidity + channel correspondence (paper28 brainstorm); the "wrong cohomology" (Schur) corrected to "right" (spectral gap).*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Ketan Mulmuley | U. Chicago | Geometric Complexity Theory (GCT); plethysms |
| Milind Sohoni | IIT Bombay | GCT co-founder |
| Peter Bürgisser | TU Berlin | GCT; no-occurrence-obstruction theorem (with Ikenmeyer, Panova) |
| Christian Ikenmeyer | Warwick / Liverpool | GCT obstructions; representation theory |
| Greta Panova | USC | GCT obstructions; algebraic combinatorics |
| Avi Wigderson | IAS | Natural proofs; algebrization; computational barriers; hardness-vs-randomness |
| Scott Aaronson | UT Austin | Algebrization barrier; quantum complexity; pedagogy |
| Ryan Williams | MIT | NEXP ⊄ ACC^0 circuit lower bound; algorithmic method |
| Alexander Razborov | U. Chicago | Natural proofs (w/ Rudich); monotone circuit lower bounds |
| Steven Rudich | CMU | Natural proofs barrier |
| Russell Impagliazzo | UCSD | Hardness-vs-randomness; worlds of complexity |
| Leslie Valiant | Harvard | VP vs VNP; holographic algorithms |
| Joshua Grochow | UC Boulder | GCT unification framework |
| Josh Alman | Columbia | Matrix multiplication; algebraic lower bounds |
| Virginia Vassilevska Williams | MIT | Fine-grained complexity; matrix multiplication |
| Subhash Khot | NYU | Unique Games Conjecture; hardness of approximation |
| Luca Trevisan | Bocconi (d. 2024) | Pseudorandomness; expanders (in memoriam) |
| Neeraj Kayal | MSR India | Arithmetic circuit lower bounds |
| Shubhangi Saraf | Toronto | Depth-4 arithmetic lower bounds |
| Nutan Limaye | IT University Copenhagen | Arithmetic circuit lower bounds (Limaye-Srinivasan-Tavenas 2021: superpoly depth-3) |
| Srikanth Srinivasan | Aarhus | Constant-depth arithmetic lower bounds |

## Major Approaches

### 1. Geometric Complexity Theory (Mulmuley–Sohoni)
Embed P vs NP (or VP vs VNP) into representation theory of GL_{n²}(C). Prove lower bound via "obstructions" — irreducible representations appearing in one orbit closure but not another. Bürgisser–Ikenmeyer–Panova (2017-19) proved the basic "occurrence obstruction" approach cannot separate permanent from determinant; Mulmuley has shifted focus to multiplicity obstructions. Long-term programme; Mulmuley himself estimates 100 years. Connected to century-old plethysm positivity problems.

### 2. Circuit Lower Bounds / Algorithmic Method (Williams)
Show limits of circuits directly. Ryan Williams (2011): NEXP ⊄ ACC^0 via SAT-algorithm-implies-lower-bound reduction. Recent superpolynomial lower bounds for low-depth algebraic circuits (Limaye–Srinivasan–Tavenas 2021). Still exponentially below "NP requires superpolynomial size" target.

### 3. Natural Proofs Barrier (Razborov–Rudich)
Meta-theorem: any "natural" lower-bound argument that is constructive + large + useful cannot break pseudorandom functions. If PRFs exist (widely believed), natural proofs can't separate P from NP. Forces non-natural methods.

### 4. Relativization + Algebrization Barriers (Baker–Gill–Solovay, Aaronson–Wigderson)
Relativization (1975): diagonalization-style proofs can't resolve P vs NP because there are oracles both ways. Algebrization (2008): adding low-degree extensions doesn't help either. Any proof must avoid all three barriers.

### 5. VP vs VNP / Valiant's Algebraic Complexity
The algebraic analog of P vs NP: is permanent essentially harder than determinant? Progress on restricted models (monotone VP < VNP; depth-4 lower bounds). Main conjecture still open.

### 6. Unique Games / PCP / Approximation (Khot, Raghavendra, Dinur)
Even assuming P ≠ NP, what's hard to approximate? Unique Games Conjecture would explain many tight hardness results. KKMO (Khot–Kindler–Mossel–O'Donnell) on 2-to-1 games. Dinur's PCP combinatorial proof. Strong 2-to-1 Games Theorem (2017-18) halfway to UGC.

### 7. Hardness vs Randomness / Derandomization (Impagliazzo–Wigderson)
Strong enough circuit lower bounds imply P = BPP. Conversely, derandomization programs would yield lower bounds. Williams' program exploits this.

### 8. Quantum Complexity / MIP* = RE (Ji–Natarajan–Vidick–Wright–Yuen 2020)
MIP* = RE settles a long-standing question; indirectly constrains NP quantum analogs. Aaronson's oracle separations.

### 9. Fine-Grained Complexity (V.V. Williams, Indyk)
Accepting NP-hardness, classify polynomial-time problems under conditional reductions (SETH, 3-SUM). Exponential time hypothesis (Impagliazzo–Paturi) as operational version.

## Partial Results / Named Milestones

- 1971 — Cook / Levin — NP-completeness of SAT
- 1975 — Baker–Gill–Solovay — relativization barrier
- 1985-87 — Razborov — exponential lower bounds for monotone circuits
- 1989 — Håstad — parity requires exponential-size AC^0 circuits
- 1994 — Razborov–Rudich — natural proofs barrier
- 1999 — Shor — quantum algorithms; quantum challenge to complexity beliefs
- 2001-07 — Mulmuley–Sohoni — GCT papers I–VII
- 2008 — Aaronson–Wigderson — algebrization barrier
- 2011 — Williams — NEXP ⊄ ACC^0
- 2017-19 — Bürgisser–Ikenmeyer–Panova — no occurrence obstructions for permanent vs determinant
- 2020 — Ji–Natarajan–Vidick–Wright–Yuen — MIP* = RE (disproves Connes embedding for group C*-algebras)
- 2021 — Limaye–Srinivasan–Tavenas — superpoly lower bound for constant-depth arithmetic
- 2024-26 — New algebrization barriers via communication complexity (ITCS 2026)

## Recent Preprints (2023-2026)

- arXiv Limaye–Srinivasan–Tavenas (2021) and extensions
- ITCS 2026 "New Algebrization Barriers to Circuit Lower Bounds via Communication Complexity of Missing-String"
- GCT papers by Mulmuley, Bürgisser, Ikenmeyer, Panova throughout 2023-2026

## Key Surveys / Textbooks

- Aaronson, "P =? NP" survey (Open Problems in Mathematics, 2016)
- Arora–Barak, *Computational Complexity: A Modern Approach* (Cambridge, 2009)
- Mulmuley (2012 CACM), "The GCT program toward the P vs. NP problem"
- Bürgisser–Clausen–Shokrollahi, *Algebraic Complexity Theory*
- Wigderson, *Mathematics and Computation* (Princeton, 2019)
- Grochow, "Unifying known lower bounds via GCT"

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Ketan Mulmuley** — GCT is the most mature geometric attack on P vs NP; we share an interest in operator-algebraic structure
- **Alexander Razborov & Steven Rudich** — natural proofs barrier defines what our approach must avoid
- **Avi Wigderson & Scott Aaronson** — algebrization barrier; shape of viable proof strategies
- **Ryan Williams** — algorithmic method / circuit lower bounds; rare non-natural technique
- **Peter Bürgisser, Christian Ikenmeyer, Greta Panova** — BIP theorem showed GCT-obstruction must be multiplicity-level, sharpened the target

### Cite in body:
- Cook, Levin — NP-completeness
- Karp — 21 problems
- Håstad — parity lower bounds
- Baker–Gill–Solovay — relativization
- Impagliazzo–Wigderson — hardness/randomness
- Valiant — VP vs VNP
- Khot, Raghavendra, Dinur — UGC / PCP
- Ji–Natarajan–Vidick–Wright–Yuen — MIP* = RE (our operator-algebra connection)
- Limaye–Srinivasan–Tavenas — recent arithmetic lower bounds
- V.V. Williams — fine-grained

### Our programme's position
Paper 28 treats P vs NP as an *operator-algebraic spectral-gap* problem: the "gap" between deterministic and nondeterministic polynomial-time is a spectral gap in a specific correspondence of von Neumann algebras, with Popa's rigidity theorem supplying the bound. This is neither a GCT-style algebraic-geometric attack nor a natural-proofs-vulnerable combinatorial argument: it evades the natural proofs barrier because pseudorandom functions do not satisfy the Popa rigidity hypothesis, and it evades algebrization because the operator-algebraic structure is not a low-degree extension. The *MIP* = RE* result (JNVWY 2020) directly motivates this direction — the non-embeddability of Connes algebras links quantum computational power with C*-algebraic rigidity. Our approach is therefore complementary to GCT (both geometric, different categories) and specifically designed to be non-natural.
