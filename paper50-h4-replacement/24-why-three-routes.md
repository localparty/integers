## §24 — Why Three Routes, Not One

*Insurance logic. H4 is hard enough that a one-route strategy is fragile. Three independent routes triangulate the target and reduce the probability of a common-mode failure.*

---

## 24.1. The base rate of wall-closures

H4 has resisted analysis for more than half a century. The IR renormalon obstruction (t'Hooft 1977, Parisi 1978) is not a technical inconvenience — it is a genuine structural statement about the non-Borel-summability of the pure-gauge perturbative series. Every attempt to close H4 by a single technique has either (i) failed to overcome the renormalon, (ii) worked only in 2D where the renormalon is absent, or (iii) produced partial results that match perturbation theory in some diagrams but not others.

The base rate of single-technique wall closures on problems of this age and depth is low. It is not zero — Deligne closed the Weil conjectures with one technique (étale cohomology and a purity argument), Wiles closed Fermat with one technique (a modularity lift). But the base rate across all comparably aged problems — RH, BSD, PvNP, YM — is that single-technique attempts fail more often than they succeed, and successful closures typically combine multiple frameworks. Wiles used Ribet's level lowering + Mazur's deformation theory + Galois representations + modular forms; Deligne used étale cohomology + Grothendieck's standard conjectures + Lefschetz trace formula + a miraculous positivity argument. "One technique" is a simplification even when retrospectively described.

For H4 specifically, the three decades of partial progress (Dyson-Schwinger truncations, instanton calculus, 2D precedent, resurgence theory, numerical lattice) have each produced something — none produced the match. This is evidence that H4 requires more than any single one of these frameworks. A three-route strategy is an empirical response to the observation that no one framework has sufficed.

---

## 24.2. The fragility of single-route attack

Suppose Paper 50 commits to a single route — say Route A (resurgence) — and an author team spends twenty-four months constructing the lateral Borel resummation of 4D YM. Two failure modes are plausible.

**Failure mode 1: internal obstruction.** The IR renormalon structure in 4D is qualitatively more severe than in 2D (Dunne-Unsal 2012 found obstructions that do not arise in the 2D precedent). After twenty-four months, the team discovers a technical obstruction that was not visible at the start. The paper is shelved. The programme has invested twenty-four months and gained a partial resurgent analysis but no H4 closure.

**Failure mode 2: external obsolescence.** The team produces a rigorous lateral Borel resummation, but during the twenty-four months a competing approach (via Langlands-Shahidi or Kapustin-Witten) closes H4 in parallel. The programme's result is mathematically sound but not the *first* such closure. The publication impact is reduced, and the programme's twenty-four-month investment produces a verification rather than a breakthrough.

Both failure modes have nonzero probability. With a single-route strategy, one failure mode has probability $p$; with three independent routes, the probability that *all three* fail simultaneously is $p^3$ (assuming independence, which §25 will nuance). The expected time-to-close is dominated by the *minimum* of three draws, which is faster than a single draw. The cost is the three-fold investment in parallel — but for a Clay-class problem, the cost of twenty-four idle months is higher than the cost of three parallel teams.

---

## 24.3. The insurance asymmetry

The asymmetry between Route success and Route failure is stark. If any one of A, B, C closes H4, the programme gains the second Clay Millennium problem (after BSD), the YM chain becomes 18/18 unconditional, and the Robustness-Circle Theorem gains its second unconditional pillar (§41). If all three fail, the programme has a 17/18 YM chain with honest documentation of three attempted routes — no worse than the status quo, and with three partial frameworks available for future iteration.

The asymmetry is: success pays out a Clay Prize; failure costs three teams' time and produces three partial results that document the difficulty. For a rational research agenda that values Clay-class outcomes highly (and the programme does), the asymmetry favours multi-route attack even at substantial parallel cost.

---

## 24.4. Why three, not two, not four

Why exactly three routes? Not an arbitrary number. The S-duality diagnostic (§30) identifies three distinct realizations of the functional equation:

- **Route A** — Borel-type summation structure (resurgence).
- **Route B** — Langlands functoriality (automorphic L-function transfer).
- **Route C** — Geometric Langlands (Kapustin-Witten + Gaitsgory-Raskin).

These are the three faces of S-duality that the programme can currently exploit. A fourth route (e.g., "direct lattice match at asymptotically small spacing") would not use S-duality — it would be a brute-force approach with lower a priori confidence. Fewer than three routes would leave an identified S-face unexploited, and the insurance argument weakens accordingly.

Three is the natural number because S-duality decomposes into three algebraic structures (Borel, functorial, geometric) that the programme has the infrastructure to pursue. Paper 60 §21 identified exactly these three. The three-route strategy is not arbitrary parallelism — it is the specific decomposition of the H4 target into its S-dual components.

---

## 24.5. Cross-route independence

The three routes are *not* perfectly independent (§25 will make the cross-references explicit). Routes A and B both involve Borel-type analytic structure (alien derivatives in A, symmetric-power L-functions in B share singularity structure). Routes B and C both involve functorial lifts (Kim-Sarnak's Sym$^k$ in B, Kapustin-Witten's twist correspondence in C). Route A and C share less — the resurgent transseries picture does not obviously talk to the geometric Langlands picture — but the programme's operator dictionary bridges them via the ITPFI factorization.

However, the routes are independent *enough* that a failure in one does not mechanically propagate. A technical obstruction in Route A's lateral Borel sum does not obstruct Route B's automorphic L-function construction (the analytic-structure overlap is shared *insight*, not shared *lemmas*). A failure of Route C's scale bridge does not obstruct Route A's resummation (they compute the same quantity via different means). The cross-references make the routes *mutually reinforcing* without making them mutually dependent.

The programme's insurance calculation therefore holds: three parallel routes give roughly independent tail-risk draws, with cross-route checks available when two or more succeed.

---

## 24.6. The honest statement

Paper 50 is a hard paper. Confidence at the start of the three-route attack is 3-4/10 — reflecting that none of the three routes has a complete proof, each has obstructions, and the collective probability of at least one closing is moderate rather than high. The insurance is not that three routes turn a hard problem into an easy one. The insurance is that three routes turn an unlikely single-draw win into a more likely multi-draw win, at the cost of three-fold parallel investment.

The programme commits to the three-route strategy because the probability calculation favours it, the S-duality diagnostic identifies exactly three natural routes, and the cost of being wrong is absorbable. Paper 50's job is to execute all three in parallel, ship whichever closes first (§26), and document the others as alternative verifications.

---

*Paper 50 §24. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
