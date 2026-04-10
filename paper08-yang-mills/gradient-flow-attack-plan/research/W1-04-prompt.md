# W1-04: Established Lemmas Verification Pack (Lemmas 3.2--3.6)

## Task
Write verification memos for five already-proved lemmas, collecting the precise references and confirming each result is established. These are all rated E (established) — the proofs exist in the mass gap preprint and Paper 10. Your job is to verify the references, state each result precisely, and confirm it applies to the gradient-flow context.

## The five lemmas

### Lemma 3.2: No operator mixing at dimension 4
**Claim:** The unique local, gauge-invariant, C-even, parity-even operator of engineering dimension 4 on the 4D hypercubic lattice is S_YM = Σ_P s_P. The mixing matrix at dimension 4 is 1×1.
**Source:** Mass gap preprint, Section 5.3.1 (lines 393-488): C-elimination of Tr(F³) + dimensional analysis.
**Gradient-flow relevance:** The small-flow-time expansion at dimension 4 involves only [Tr F²]_R — no mixing.

### Lemma 3.3: Deviation order dev ≥ 2 at dimension ≥ 6
**Claim:** Every C-even, gauge-invariant, dimension-6 operator has Boltzmann deviation order dev ≥ 2.
**Source:** Mass gap preprint, Section 5.6, Part III (lines 1737-1891). Four-class classification.
**Gradient-flow relevance:** Subleading terms in small-flow-time expansion are suppressed by g_k⁴ Δ̂².

### Lemma 3.4: KK mode sum vanishing at t = 0
**Claim:** E_L(-j; Q) = 0 for all positive-definite Q and j ≥ 1.
**Source:** Paper 1, Appendix K, Section K.7b (Theorem K.1). Mechanism: 1/Γ(-j) = 0.
**Gradient-flow relevance:** At t = 0, KK mode sums vanish → F(0) is finite.

### Lemma 3.5: Z₂ parity cancellation persists at all t
**Claim:** f_even(n) + f_odd(n) = 0 at each KK level n ≥ 1, for all flow times t ≥ 0.
**Source:** Paper 10, Route 03, Proposition 3.1 (Section 3.3, lines 106-114).
**Gradient-flow relevance:** Cancellation is t-independent → persists through t → 0 limit.

### Lemma 3.6: Goroff-Sagnotti coefficient vanishes in all schemes
**Claim:** C_GS = 0 on M⁴ × S¹/Z₂ in all regularization schemes.
**Source:** Paper 10, Theorem 1 (Section 4.6, lines 274-279). Proof chain: Lemma A1 + A2 + A3.
**Gradient-flow relevance:** Two-loop UV finiteness at t = 0 is scheme-independent.

## What to read
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Sections 5.3.1, 5.5.3, 5.5.4, 5.6
- `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md` — Theorem K.1
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/03-z2-parity.md` — Proposition 3.1
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md` — Theorem 1

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-04-established-lemmas-pack.md`
2. Code: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/established-pack/` — Verify numerically: (a) Epstein zeta E₂(-j; Q₀) = 0 for j=1..10 via the Eisenstein factorization 6ζ(s)L(s,χ₋₃), (b) S₀ = 1+2ζ(0) = 0

## Output format
Five self-contained verification memos (one per lemma), each with: Statement, Source Reference (exact section/line), Verification that the result applies to gradient-flow context, Any numerical checks. Then a summary table.
