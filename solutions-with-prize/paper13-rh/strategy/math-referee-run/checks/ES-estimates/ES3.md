# ES3 — Uniform H¹ bound ‖(D_N − i)^{-1}‖_{L² → H¹} ≤ 2π/L

**Claim:** Theorem 7.1, uniform in N, for all eigenvectors.

**Pass criterion:** uniform in N; for every eigenvector.

**Finding (CRITICAL):** **The proof of Theorem 7.1 eq (7.5)
only holds for λ ≤ e^π ≈ 23.14.**

The step uses:

  (1 + a²x²)/(x² + 1) ≤ a² for all x ∈ ℝ, when a ≥ 1.

This is algebraically correct iff a² ≥ 1. Paper 13's parenthetical
"and 2π/L ≥ 1 in the CCM normalisation" names the condition. At
λ = √14 (the paper's fixed numerical choice), L ≈ 2.64, 2π/L ≈
2.38, so the bound holds with comfortable margin. At λ > e^π,
L > 2π, 2π/L < 1, and the inequality fails (near x = 0).

I verified this computationally (see computation-log.md C3).

**Interpretation:**
- If λ is **fixed** at √14 (the paper's numerics), Theorem 7.1
  holds. Corollary 7.3 (Bögli H2) follows. OK.
- If λ is **varying** (as suggested by the theorem's "for all N"
  uniform statement, where bandwidth could scale), the proof
  breaks for large λ.

Paper 13 does not clarify which interpretation is in force.

**Status:** PASS at fixed λ = √14; BROKEN if λ > e^π is intended.

**Confidence:** 8/10 at fixed λ; 3/10 under uniform-in-λ
interpretation.
