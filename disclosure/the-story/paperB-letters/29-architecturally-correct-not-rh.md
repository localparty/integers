# 29 — Architecturally correct but not RH

**Speaker:** Claude (Opus 4.6, session 75273c7a).
**Date:** 2026-04-10, 21:07 UTC.
**Context:** Claude ran a math-referee pass on the RH preprint with 96 output files.

> Review complete — 96 files written across `points/`, `checks/`, plus `clay-checklist.md`, `summary.md`, `INDEX.md`, and `computation-log.md` at `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/strategy/math-referee-run/`.
>
> ## Headline findings
>
> **Verdict: The proof is architecturally correct but not rigorously executed. Not RH.**
>
> The six-layer chain (CCM + ITPFI + estimates + Teschl/Bögli + Hurwitz) is the right shape, but there are concrete rigor gaps:
>
> 1. **Section 10.4 Step 4 (final deduction) is tautological as written.** "{γ_n} = spec(D_∞) ⊂ ℝ, therefore γ_n ∈ ℝ" — but γ_n are *defined* in Section 1 as imaginary parts of critical-line zeros, so this contains no information. The logically sufficient argument (Hurwitz in the complex plane applied to the real-zero property of ξ̂_N) is implicit but never explicit.
>
> 2. **Theorem 7.1's proof only holds for λ ≤ e^π ≈ 23.14** — I verified this algebraically and computationally. The step "(1+a²x²)/(x²+1) ≤ a² when a ≥ 1" requires 2π/L ≥ 1. At the paper's fixed λ = √14 it's fine, but any uniform-in-λ reading breaks.
>
> [...]
>
> **Paper's self-rating 8/10 vs my rating 6-7/10 as written.** The paper attributes its gap entirely to CCM's preprint status; I find significant Layer 3-5 issues independent of CCM.

The exact hostile reviewer G had asked Claude to be. Specific. Concrete. Numbered. Not a vague sense of concern but *Section 10.4 Step 4 is tautological as written* — with the reason.

The penultimate line is load-bearing: *The paper attributes its gap entirely to CCM's preprint status; I find significant Layer 3-5 issues independent of CCM.* A rating conflict, published by the model against its own earlier optimism.

*Next: [30-honest-weakenings.md](30-honest-weakenings.md).*
