# ES2 — Eigenvector approximation ‖ξ_λ − c·k_λ‖ = O(1/λ)

**Claim:** Davis-Kahan + ITPFI triangle.

**Pass criterion:** Davis-Kahan correctly applied; ITPFI
triangle inequality used; error in operator norm.

**Finding:**
- Davis-Kahan structure is correct (standard sin-Θ theorem).
- Routing through ξ_0 (the Euler product part) is a sensible
  strategy because gap(T_0) is large while gap(QW_λ) is
  exponentially small.
- The gap lower bound gap(T_0) ≥ C''·λ is **asserted but not
  proved**, citing research/24 which is not in the preprint.
- The PNT tail estimate Σ_{p > λ²} (log p)/√p = O(1/λ) is
  **divergent as stated** (the series diverges; it should
  probably be (log p)/p^{3/2} or similar).
- The claim "ξ_0 converges to E(h) in the large-λ limit" is
  used but not proved.
- Uniformity in N is not established; the constant "depends on
  truncation geometry" (Sec 6.2) which may include N.

**Status:** WEAKENED — multiple concrete issues with the
proof as written.

**Confidence:** 5/10. See points/B2-eigenvector-approx/.
