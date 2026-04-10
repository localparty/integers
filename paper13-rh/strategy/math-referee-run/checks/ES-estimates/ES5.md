# ES5 — Rank-one stabilization ‖Δ_N‖ ≤ C · ρ^{-N}

**Claim:** research/40 Lemma 1, ρ = 19.54 numerical, ρ ≥ 4 analytical.

**Pass criterion:** operator norm (not Frobenius); rank-one structure proved; decay holds.

**Finding:**
- The "rank-one" claim is imprecise: Δ_N = |σ_N|·|ξ_N⟩⟨ξ_N| −
  |σ_∞|·|ξ_∞⟩⟨ξ_∞| is a difference of two rank-one operators,
  which is **rank ≤ 2**, not rank-1. The norm bound is the same
  shape (bounded by 2·‖ξ_N − ξ_∞‖ + scalar differences) but the
  structural claim is loose.
- The decay ρ = 19.54 numerically verified at N ∈ {10, 20, 30}
  (see Remark 9.4 table, Paper 13). Consistent with a ρ^{−N}
  decay pattern.
- The analytical lower bound ρ ≥ 4 is attributed to
  research/40 Lemma 1, **which is not in the preprint**. I
  cannot verify.

**Status:** CONDITIONALLY PASS — numerical data at small N
matches the claim, but the analytical guarantee and the full
lemma are not in the paper.

**Confidence:** 6/10.
