# W6-12: KK → 4D Projection for Composite Operators (Lemma 3.9)

## Task
Write a rigorous proof memo establishing that the renormalized composite operator [Tr F²]_R constructed in the KK theory projects to the corresponding operator in 4D Yang-Mills with exponentially small corrections.

## Statement to prove
**Lemma 3.9.** |S_n^{ren,KK}(f) - S_n^{ren,4D}(f)| ≤ C·e^{-m₁ r_min} where m₁ = 2√N/r₃ is the lightest KK mass and r_min is the minimum pairwise distance among support points of f.

## Key inputs
- **W5-10** (Lemma 3.7-3.8): [Tr F²]_R exists in the KK theory
- **Theorem 5** (Section 4.5, lines 953-972): IR equivalence Δ₀^std ≥ Δ₀^KK - C·e^{-m₁a}
- **Feshbach projection** (Section 4.5, lines 1188-1262): eigenstates factorize as |n⟩ = |ψ_n⟩_4D ⊗ |Ω_int⟩ + |δ_n⟩ with ‖δ_n‖ ≤ (2C_W/m₁)e^{-m₁a}
- **Paper 10, Lemma A2** (Section 5.2b): graviphoton/radion contribute only at dim ≥ 8
- **Paper 10, Route 03** (Proposition 3.1): Z₂ cancellation → KK modes n ≥ 1 cancel pairwise
- **W1-04** (Lemma 3.5): Z₂ cancellation persists at all t

## Proof strategy
1. Decompose KK correlator: S_n^{ren,KK} = S_n^{(0)} + Σ_{m≥1} S_n^{(m)} where S_n^{(0)} is the n=0 (4D) sector
2. The m ≥ 1 contributions are suppressed by e^{-m₁ r_min} (massive KK propagators)
3. S_n^{(0)} = S_n^{ren,4D} (the 4D renormalized correlator)
4. Alternative argument via Z₂: modes n ≥ 1 cancel pairwise → only n=0 survives

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md` — Lemma 3.7-3.8
- `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md` — Theorem 5 (Section 4.5, Feshbach projection lines 1188-1262)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-04-established-lemmas-pack.md` — Lemma 3.5 (Z₂)
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/03-z2-parity.md` — Proposition 3.1

## What to write
Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W6-12-kk-to-4d.md`

## Output format
Self-contained proof: (1) Setup: KK mode decomposition of correlators, (2) Massive mode suppression bound, (3) Feshbach for matrix elements (extending Theorem 5 from spectrum to operators), (4) Z₂ parity as independent confirmation, (5) Explicit bound with numerical estimate for N=3. Reference W5-10, Theorem 5, Lemma A2, Proposition 3.1.
