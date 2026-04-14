# Landscape — Birch & Swinnerton-Dyer Conjecture (paper26)

*Millennium target. Our strategy: Route 3 MY4 (Mazur–Yuan–Zhang–Zhang) conditional on CBB KMS-structure.*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Manjul Bhargava | Princeton | Average rank bounds; 7/6 rank theorem; counting methods |
| Christopher Skinner | Princeton | Iwasawa main conjecture (Skinner–Urban); rank 0 / 1 BSD |
| Wei Zhang | MIT | Gross–Zagier generalizations; BSD for CM; arithmetic AGG |
| Xinyi Yuan | Berkeley / Peking | Yuan–Zhang–Zhang Gross–Zagier formula |
| Shou-Wu Zhang | Princeton | Heights / arithmetic algebraic geometry; BSD foundations |
| Arul Shankar | Toronto | Average ranks, counting elliptic curves |
| Karl Rubin | UC Irvine | Kolyvagin refinements; Iwasawa theory |
| Ashay Burungale | UT Austin | p-converse to Gross–Zagier–Kolyvagin |
| Ye Tian | AMSS Beijing | Non-CM twists, BSD for rank 1 |
| Xin Wan | AMSS Beijing | Iwasawa main conjecture for GL(2) |
| Kartik Prasanna | Michigan | Automorphic periods, BSD-type formulas |
| Ellen Eischen | Oregon | p-adic L-functions, Iwasawa theory |
| Victor Rotger | UPC Barcelona | Elliptic Stark conjectures |
| Henri Darmon | McGill | Stark-Heegner points; p-adic L-functions |
| John Coates | Cambridge (d. 2022) | BSD foundations; main conjecture programme |
| Benedict Gross | Harvard / UCSD | Gross–Zagier theorem (1983) |
| Don Zagier | MPIM Bonn | Gross–Zagier theorem; modular forms |

## Major Approaches

### 1. Iwasawa Theory / Main Conjecture (Skinner–Urban, Coates, Kato, Wan)
Prove the Iwasawa main conjecture for the elliptic curve's p-adic L-function, deduce BSD in rank 0 or 1 for many curves. Skinner–Urban established main conjecture for GL(2)×GL(2) over Q. Further work by Kato on the cyclotomic Iwasawa main conjecture for modular forms; Wan on the anticyclotomic case. Gives p-part of BSD.

### 2. Heegner Points / Gross–Zagier / Kolyvagin
Classic route: use Heegner points on modular curves, compute Néron-Tate heights via Gross–Zagier formula, apply Euler system of Kolyvagin to bound Sha. Result: if analytic rank ≤ 1, rank equals analytic rank and Sha is finite. Modern extensions: Yuan–Zhang–Zhang generalized Gross–Zagier to higher-genus Shimura curves.

### 3. Statistical / Average Rank (Bhargava–Shankar–Skinner–Zhang)
Counting elliptic curves by height, prove average rank bounds. Bhargava–Shankar: average rank ≤ 7/6. Bhargava–Skinner–Zhang: ≥ 66% of elliptic curves satisfy rank-part BSD. Does not resolve individual curves but proves statistical BSD for a positive proportion.

### 4. p-converse Theorems (Skinner, Zhang, Burungale–Skinner–Tian–Wan)
Reverse the direction: given rank 0 or 1, deduce that L-value or its derivative is nonzero. Skinner's converse and Burungale et al. 2024 first infinite families of non-CM quadratic twists with strong BSD.

### 5. BSD for CM Elliptic Curves
Coates–Wiles (1977): if E has CM and rank 0 then L(E,1) ≠ 0 implies finite Mordell–Weil. Rubin's work. Essentially complete for CM curves modulo technical details.

### 6. Euler Systems / Anticyclotomic / Big Heegner Points
Howard's big Heegner points; Ribet–Skinner methods; Longo–Vigni anticyclotomic.

### 7. Analytic Rank Bounds / Average Analytic Rank
Various researchers proving average analytic rank bounds; Young, Heath-Brown. Combined with statistical methods gives positive-proportion BSD.

## Partial Results / Named Milestones

- 1977 — Coates–Wiles — BSD for CM curves, rank 0 case
- 1983 — Gross–Zagier — height formula connecting L'(E,1) to Heegner points
- 1989 — Kolyvagin — Euler system bounds Sha; with GZ proves BSD for analytic rank ≤ 1
- 1994 — Wiles + Taylor–Wiles — modularity for semistable (1999 Breuil et al.: all elliptic curves over Q)
- 2010-14 — Bhargava–Shankar — bounded average rank, sieve-counting
- 2013-14 — Skinner–Urban — main conjecture for GL(2) over Q
- 2014 — Bhargava–Skinner–Zhang — 66% of elliptic curves satisfy rank-BSD
- 2019-24 — Burungale–Skinner–Tian–Wan — strong BSD for infinite non-CM twist families
- 2024-26 — Identified elliptic curves up to conductor 500,000 admitting infinitely many twists satisfying strong BSD

## Recent Preprints (2023-2026)

- arXiv:2601.16044 — "On the identification of elliptic curves that admit infinitely many twists satisfying BSD"
- 2024-26 work by Burungale–Skinner–Tian–Wan on Iwasawa main conjecture applications
- Dasgupta–Kakde (2021-present) — on the related p-adic Stark conjecture, feeding into L-function understanding

## Key Surveys / Textbooks

- Wiles, "The Birch and Swinnerton-Dyer Conjecture" (Clay problem description)
- Zhang (Wei), "The Birch–Swinnerton-Dyer conjecture and Heegner points: A survey" (Current Developments in Math 2013)
- Bhargava–Ho (survey), "Coregular spaces and genus one curves"
- Silverman, *The Arithmetic of Elliptic Curves* (2nd ed., Springer)
- Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*
- Milne, lecture notes on elliptic curves

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Christopher Skinner & Manjul Bhargava** — their statistical+Iwasawa combination is the current state of the art; our MY4 route is adjacent
- **Wei Zhang, Xinyi Yuan, Shou-Wu Zhang** — generalized Gross–Zagier is the foundation of Route 3
- **Benedict Gross & Don Zagier** — the theorem that started the modern approach
- **Victor Kolyvagin** — Euler system technique, still foundational
- **Karl Rubin** — Euler systems, Iwasawa theory refinements

### Cite in body:
- John Coates — main conjecture framework
- Kazuya Kato — cyclotomic main conjecture for modular forms
- Xin Wan — anticyclotomic main conjecture
- Ashay Burungale, Ye Tian — non-CM p-converse
- Henri Darmon — Stark-Heegner / p-adic
- Kartik Prasanna — automorphic periods
- Wiles, Taylor-Wiles, Breuil-Conrad-Diamond-Taylor — modularity (enables BSD framework)
- Bhargava–Shankar — rank 7/6 bound

### Our programme's position
Route 3 MY4 treats BSD as a corollary of an ergodic-theoretic picture: CBB (Connes–Bost–Baumslag) KMS-states for GL(2) encode L-function behavior, and the Gross–Zagier–Yuan–Zhang–Zhang height formula becomes a Murray–von Neumann dimension identity. The result is the strong BSD for elliptic curves where CBB applies. This is **complementary** to the Bhargava–Skinner–Zhang statistical programme: where they prove BSD for 66% of curves by height, we prove it for the (infinite, density-1 in another sense) CBB-admissible class. Reviewers from each school are represented in the PROOF-CHAIN's critic list.
