# HZ1 — ξ̂_N → Ξ uniformly on compacts of {|Im z| < 1/2}

**Claim:** Theorem 10.1, from CCM Lemma 7.3 + Estimate (b).

**Pass criterion:** Uniform on compacts; L² → sup-norm upgrade rigorous.

**Finding:**
- Step 1 (CCM Lemma 7.3: k̂_λ → Ξ uniformly on substrips):
  taken from CCM, not re-derived.
- Step 2 (Corollary 6.6: |ξ̂_λ − c k̂_λ| = O(1/λ) on compacts):
  uses Paley-Wiener upgrade from L² (on the compact support
  interval) to sup-norm (on compact subsets of the strip).
  Rigorous at fixed N.
- **Concern (λ vs N):** Step 2 is stated "as λ → ∞" at fixed N,
  but the downstream Hurwitz step wants a limit as N → ∞. The
  connection between these two limits is not clear.
- If λ is held fixed and N → ∞, Estimate (b) gives a bounded
  (not vanishing) error, insufficient for Hurwitz.
- If λ = λ(N) → ∞ coupled, the estimate must be uniform in N;
  not clearly established.

**Status:** CONDITIONAL — structurally plausible; the limit-
parameter ambiguity needs resolution.

**Confidence:** 7/10 conditional on resolving the λ-N issue.
See points/C1-hurwitz/01-uniform-convergence.md.
