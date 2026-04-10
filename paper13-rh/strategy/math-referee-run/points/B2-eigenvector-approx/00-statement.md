# B2 — Eigenvector Approximation via ITPFI Triangle [MEDIUM]

## Claim (Theorem 6.4, "Estimate (b)")

Let ξ_λ be the minimal eigenvector of the Weil form QW_λ^{N,+} on
E_N^+, and k_λ = E(h_λ) the CCM prolate approximation (CCM eq 7.6).
Then there exists c = c(λ) such that

  ‖ξ_λ − c · k_λ‖ = O(1/λ) as λ → ∞.

The proof (Sec 6.4) uses the triangle inequality routed through an
intermediate vector ξ_0 (the minimal eigenvector of the Euler
product part T_0):

  ‖ξ_λ − c · k_λ‖ ≤ ‖ξ_λ − ξ_0‖ + ‖ξ_0 − c · k_λ‖.

Lemma 6.1 bounds the first term by O(1/λ) via Davis–Kahan
perturbation of ξ_λ around ξ_0. Lemma 6.3 bounds the second by
O(λ^{−2}) via CCM Lemma 7.2 (Meixner–Schäfke bound on the
prolate eigenfunctions). Adding gives the O(1/λ) bound.
