# B1 — Archimedean Estimate [MEDIUM]

## Claim (Proposition 5.1)

For λ = γ_n with n ≥ 2,

  ‖τ^{(ℝ)}(λ)‖ / ‖Σ_p τ^{(p)}(λ)‖ = O(1/λ).

Here τ^{(ℝ)} is the archimedean (gamma-factor) component of the
Weil test function decomposition τ = τ^{(ℝ)} + Σ_p τ^{(p)}, and
the norms are operator norms on the relevant form domain.

The role in the chain: this estimate feeds Lemma 6.1 (eigenvector
perturbation via Davis–Kahan), which in turn feeds Theorem 6.4
(Estimate (b): eigenvector approximation by ITPFI product
vectors), which feeds the Fourier transform bound Corollary 6.6,
which feeds the Hurwitz argument.

## Why MEDIUM

Not as load-bearing as CCM or Teschl–Boegli, but the whole
eigenvector-approximation chain of Sections 5–6 depends on this
bound. If it is wrong (wrong rate, wrong uniformity, wrong
direction), the Fourier transform convergence downstream degrades
or fails.
