# ES1 — Archimedean sub-leading O(1/λ)

**Claim:** ‖τ^{(ℝ)}‖ / ‖Σ_p τ^{(p)}‖ = O(1/λ).

**Pass criterion:** bound holds for ALL eigenvalues λ; constant effective.

**Finding:**
- Paper 13's Section 5.2 sketch uses Stirling asymptotics for the
  archimedean scalar (correct: O(log λ)).
- The lower bound ‖Σ_p τ^{(p)}‖ ≥ c·λ·log λ is a hand-wave ("by
  the explicit formula"), not proved.
- Section 5.2 and Section 6.2 give **different formulations**:
  Section 5 says ratio = O(1/λ); Section 6 says ‖τ^{(ℝ)}‖ ≤ 5.5
  (constant) and gap(T_0) ≥ C''·λ. The two are not
  mathematically the same, and the paper conflates them.
- Proposition 5.1 explicitly excludes n = 1 (so not ALL
  eigenvalues).
- Constants inherited from research/20, not in preprint.

**Status:** WEAKENED — not rigorous as stated; inherits from
internal research notes.

**Confidence:** 5/10. See points/B1-archimedean/ for details.
