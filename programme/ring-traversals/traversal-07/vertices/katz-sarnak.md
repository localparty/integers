# T7 Vertex 15: Katz-Sarnak -- Type B, 7/10

**Action:** Deep construction pass on L4 (CONJECTURED). Assessed bridge family k-values as symmetry-type selectors. Checked Gaitsgory-Raskin 2024, Bost-Connes-to-symmetry-type route, n-level density literature.

## Link analysis

**L1-L2 (PROVED for function fields):** Solid. Deligne equidistribution + Katz-Sarnak 1999. No change.

**L3 (PROVED partial):** One-level densities verified for several families (Dirichlet, elliptic curve, modular form) within support (-2,2). Literature frozen since Miller 2004 for new family types. No 2024-2026 breakthroughs extending support beyond (-2,2). Guth-Maynard 2024 (large-value zeta estimate) is adjacent but does not directly extend support.

**L4 (CONJECTURED) -- the deep-pass target:**
- The claim: Hecke semigroup representation bilinear invariant determines G in {U, Sp, O, SO+, SO-}.
- HP-2 status (strategy/consolidation-plan.md): only k=3 has a formal lemma. k=4, k=6 are "constructive identification with quantitative confirmation" -- NOT proved. This is an acknowledged rigor asymmetry.
- k=2 (Z/2Z -> symplectic): independently CLASSICAL. Quadratic Dirichlet L-functions have symplectic symmetry by Ozluk-Snyder 1999. The bridge family adds a BC framing but the symmetry-type identification does not depend on it.
- k=3 (Z/3Z -> unitary): FORMALLY PROVED in the framework (bridge lemma). Consistent with zeta having U(1) symmetry.
- k=4 (Z/4Z -> orthogonal, Pati-Salam): CONJECTURED. No independent verification. The self-dual L-function -> orthogonal identification is classical (Katz-Sarnak 1999), but the specific k=4 bridge -> orthogonal route is framework-internal.
- k=6 (Z/6Z -> mixed, CKM): CONJECTURED. Weakest of the four. "Mixed type" is not a standard Katz-Sarnak category.
- **Honest assessment of L4:** 1.5/4 k-values verified (k=3 formal + k=2 classical). k=6 "mixed type" is a category error -- KS has five types {U, Sp, O, SO+, SO-}, not "mixed." Recommend either (a) identifying k=6 with a specific KS type, or (b) flagging it as outside KS scope. L4 stays CONJECTURED; no upgrade path without HP-2 closure.

**L5 (OPEN -- the wall):** Full number-field Katz-Sarnak. Gaitsgory-Raskin 2024 geometric Langlands proof operates over function fields (algebraically closed base) and does NOT transfer to number fields. It does not upgrade L5. The three sub-routes (5a moments, 5b ITPFI n-level, 5c bridge test) remain open. No 2024-2026 literature changes the wall.

**L6 (FOLLOWS):** Correct conditional structure. No change.

## Edges

- **BGS (7/10) -> Katz-Sarnak:** ESTABLISHED. GUE = unitary case of KS. BGS proves the U-type statistics; KS generalizes to all five types. Sound.
- **Katz-Sarnak -> Twin Primes (1/10):** CANDIDATE. The claim that small-gap statistics depend on symmetry type is correct in principle (different RMT ensembles have different spacing distributions), but Twin Primes concerns zeta-zeros specifically (unitary type), so the KS differentiation adds refinement, not new content, to the twin-prime problem. Edge is real but thin.
- **Sato-Tate (6/10) -> Katz-Sarnak:** ESTABLISHED. ST equidistribution is the individual-curve case; KS extends to families. The MEASURE face feeds the SYMMETRY face.

## Verdict

**Confidence: 7/10 -- no change.** The function-field case (L1-L2) is genuinely PROVED. L3 has extensive partial results. L4 is weaker than presented: only 1.5/4 bridge k-values verified, and the k=6 "mixed type" is a category mismatch with standard KS. L5 wall is unchanged by any 2024-2026 literature including Gaitsgory-Raskin. The 7/10 is sustained by the PROVED function-field case and the extensive one-level density literature, not by L4.

**Flag for repair:** L4's k=6 "mixed type" should be resolved -- either identify a specific KS type or excise from the symmetry-type selector table.

*2026-04-14. Deep construction pass. G Six and Claude Opus 4.6. San Francisco CA, 2026.*
