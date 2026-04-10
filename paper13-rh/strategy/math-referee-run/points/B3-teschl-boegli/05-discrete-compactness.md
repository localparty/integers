# B3.05 — Discrete Compactness (Bögli H2)

## Bögli's H2 hypothesis

From Paper 13 Appendix D.2 (paraphrase of Bögli 2017):

> **H2 (discrete compactness):** Every sequence {u_n} with
> u_n ∈ Dom(T_n), ‖u_n‖ ≤ 1, and ‖T_n u_n‖ ≤ C, has a convergent
> subsequence in H.

## Paper 13's verification

Theorem 7.1: ‖(D_N − i)^{−1}‖_{L² → H¹} ≤ 2π/L, uniform in N.

Corollary 7.3: every bounded sequence in L² (with bounded
‖D_N u_N‖) has a subsequence converging in L² via Rellich–
Kondrachov applied to the H¹ → L² embedding on [λ^{−1}, λ].

## Critical issue: the proof of Theorem 7.1 step (7.5)

Paper 13's proof of the resolvent bound uses:

> "(1 + (2π/L)² (γ_k^{(N)})²) / ((γ_k^{(N)})² + 1) ≤ (2π/L)²
> where the inequality holds because (1 + a²x²)/(x² + 1) ≤ a²
> for all x ∈ ℝ whenever a ≥ 1 (and 2π/L ≥ 1 in the CCM
> normalisation)."

**I computationally verified** (see computation-log.md C3):

  (1 + a²x²)/(x² + 1) ≤ a² for all x ∈ ℝ ⟺ a² ≥ 1.

So the inequality is correct **only when a = 2π/L ≥ 1**, i.e.,
when L ≤ 2π ≈ 6.28, i.e., when **λ ≤ e^π ≈ 23.14**.

| λ | L = 2 log λ | 2π/L | Inequality (7.5)? |
|:--|:-----------|:-----|:------------------|
| √14 ≈ 3.74 | 2.64 | 2.38 | **holds** |
| 10        | 4.61 | 1.36 | holds |
| 23.14 (= e^π) | 6.28 | 1.00 | borderline |
| 100       | 9.21 | 0.68 | **FAILS** |
| 1000      | 13.82 | 0.45 | **FAILS** |

**Finding:** Theorem 7.1 as proved only holds for λ ≤ e^π. For
larger λ, the proof breaks.

If λ is **fixed** at √14 (as in Appendix F's AE certification),
the bound is comfortably satisfied and Corollary 7.3 goes through.

If λ is treated as **varying** (which the notation of Theorem 7.1
suggests — it is stated uniformly in N, with L appearing as a
parameter), then the bound fails for λ > e^π. The "uniform in N"
assertion is either misleading (it is actually uniform in N at
fixed λ) or wrong (if λ is permitted to grow).

## Impact on Bögli H2

If Theorem 7.1 fails for large λ:

1. The H¹ → L² compactness embedding might still hold on
   [λ^{−1}, λ], but the uniform H¹ bound is not established.

2. Without a uniform H¹ bound, bounded sequences in L² with
   bounded D_N-images might not have subsequences converging in
   L² — exactly the failure mode Bögli H2 rules out.

3. Spectral pollution cannot be guaranteed.

**If λ is fixed**: this concern is moot. Theorem 7.1 holds with
margin at λ = √14, and Corollary 7.3 is valid. Bögli H2 holds.

**If λ is intended to grow**: the proof of Theorem 7.1 is
broken, and discrete compactness is not established.

## What the paper says about λ

Section 7.1 introduces L = "the period of the Chebyshev system on
[0, L]", with no explicit tie to λ. L appears as a fixed parameter
in the bound. Appendix A.2 has L = 2 log λ. So L grows with λ,
and the inequality bound requires small L.

Appendix F certifies AE simplicity at λ = √14. Numerical
verifications (Appendices A.5, G) use λ = √14 throughout. The
paper's entire numerical backbone is at **fixed λ = √14**.

Reading charitably, Paper 13's entire analysis is at the fixed
value λ = √14, and Theorem 7.1 works at that value. The Hurwitz
limit is over N → ∞, not λ → ∞.

**But this creates a contradiction with Section 6**, which
literally says "as λ → ∞" throughout. Either Section 6's λ is a
*different* parameter (spectral vs bandwidth), or Section 6's
analysis contradicts Section 7's fixed-λ assumption.

See B2 / 03-error-norm.md for the λ-vs-N conflation issue.

## Discrete compactness, if the H¹ bound holds

Rellich–Kondrachov: H¹([a, b]) embeds compactly into L²([a, b])
for bounded intervals. Standard.

If the uniform H¹ bound (Theorem 7.1) holds, discrete compactness
follows.

## Verdict on this subpoint

**Conditionally PASS at λ = √14** (the paper's fixed numerical
value): the H¹ bound holds comfortably, Rellich applies, Bögli
H2 is satisfied.

**FAILS as a uniform-in-λ bound** due to the concrete restriction
λ ≤ e^π from the algebraic inequality in the proof. If the paper
means to cover all λ, Theorem 7.1 must be re-proved.

The paper should state explicitly: "Throughout the proof, λ is
fixed at √14" (or any value ≤ e^π), and the bookkeeping in
Section 6 about "as λ → ∞" is either a separate variable or a
misuse of notation.

**This is one of the concrete technical findings of this review.**
See computation-log.md C3 for the numerical verification.
