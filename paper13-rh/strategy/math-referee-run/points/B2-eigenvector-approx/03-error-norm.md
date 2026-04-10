# B2.03 — Error Norm and Fourier Transform

## Question

Is ‖ξ_λ − c · k_λ‖ = O(1/λ) in L² norm? In H¹? Does the norm
choice matter for the Hurwitz application?

## Finding

Paper 13 Theorem 6.4 does not specify the norm explicitly. From
context (the Hilbert space is E_N^+ ⊂ L²([λ^{−1}, λ])), it is
the L² norm on the underlying interval.

For the Hurwitz application, Corollary 6.6 (Fourier transform
approximation) upgrades L² to uniform on compact subsets of the
strip |Im z| < 1/2:

  |ξ̂_λ(z) − c · k̂_λ(z)| ≤ C_K · ‖ξ_λ − c · k_λ‖_{L²} = O(1/λ),

uniform in z ∈ K, where C_K depends only on K.

## The Paley–Wiener / Cauchy–Schwarz step

The proof of Corollary 6.6 uses:

  |f̂(z)| = |∫ f(t) e^{−izt} dt| ≤ ‖f‖_{L²} · (∫ e^{−2α|t|} dt)^{1/2}
         = C_α · ‖f‖_{L²},

for |Im z| ≤ α < 1/2. Here:
- f is the difference ξ_λ − c · k_λ,
- the integral is over the support of f, which is the compact
  interval [λ^{−1}, λ] (or possibly [−λ, λ] depending on the
  conventions),
- α < 1/2 is the height within the strip.

For f compactly supported on a bounded interval, the integral
∫ e^{−2α|t|} dt over that interval is bounded, giving the Paley–
Wiener-type estimate. This is correct for compactly supported
square-integrable functions.

**But** the estimate depends on the support interval. If f is
supported on [−λ, λ] (an interval growing with λ), then
∫_{−λ}^λ e^{−2α|t|} dt = (1 − e^{−2αλ})/α → 1/α as λ → ∞. So
C_α is bounded as λ → ∞. Good.

If instead f is supported on [λ^{−1}, λ] (the CCM Sonin interval),
similar argument: bounded constant.

So the constant C_K depends on K (the choice of compact subset
in the strip) but not on λ, which is what the paper claims. This
step is OK.

## The uniformity issue persists

Corollary 6.6 gives:

  |ξ̂_λ(z) − c · k̂_λ(z)| ≤ C_K · ‖ξ_λ − c · k_λ‖_{L²} = O(1/λ),

*at fixed N and as λ → ∞*. This is an L² → L^∞ (on K) upgrade. It
is correct within the (λ, N) at which Theorem 6.4 is stated.

**But the Hurwitz argument in Section 10 takes the limit "as the
eigenvalues of D_N converge to {γ_n}", which is the limit
N → ∞**, not λ → ∞. The rates in Section 5–6 are all stated as
λ → ∞. How are these two limits connected?

If λ is held fixed at √14 (or any fixed value) as N → ∞, the
estimate ‖ξ_λ − c · k_λ‖ = O(1/λ) gives a *bounded* error (since
λ is fixed), not a vanishing one. The Fourier transform
convergence that Hurwitz needs is therefore not obtainable at
fixed λ from this estimate alone.

If λ grows with N (e.g., λ ∼ P_N or λ ∼ N^{c}), then the paper
needs to specify the relationship and verify that the estimate
survives jointly. It does neither.

## What the paper is actually claiming (charitable reading)

Perhaps Paper 13 intends "λ" in Section 6 as the "bandwidth" tied
monotonically to N (so λ(N) → ∞ as N → ∞), and the O(1/λ) rate
becomes an O(1/λ(N)) rate that vanishes as N → ∞. But this
identification is never made, and the estimates in Section 6 are
stated "at fixed truncation level N, for λ sufficiently large",
which contradicts the monotonic tying.

## Verdict on this subpoint

**Weakened.** The L²-to-uniform upgrade via Paley–Wiener is fine.
The structural issue is that Theorem 6.4 is an estimate as λ → ∞
at fixed N, while the downstream Hurwitz argument wants an
estimate as N → ∞ (possibly at fixed λ or with λ = λ(N) growing).
The two are conflated. The paper must state clearly which limit
is intended and prove uniformity across the other parameter.

See D1-assembly/03-interface-gaps.md for the full picture.
