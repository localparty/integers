# C1.01 — The Uniform Convergence

## Question

Hurwitz requires uniform-on-compacts convergence of holomorphic
functions. Paper 13 claims ξ̂_N → Ξ uniformly on compact subsets
of {|Im z| < 1/2}. How is this established?

## The two-step chain

**Step 1 (CCM Lemma 7.3).** k̂_λ → Ξ uniformly on closed
substrips of {|Im z| < 1/2}. Paper 13 Appendix A takes this from
CCM. The convergence rate is O(λ^{−3/2+ε}) per CCM.

**Step 2 (Paper 13 Corollary 6.6).** |ξ̂_N(z) − c · k̂_λ(z)| =
O(1/λ) uniformly on compact subsets of the strip. This uses
Estimate (b) (Theorem 6.4, ‖ξ_λ − c·k_λ‖_{L²} = O(1/λ)) combined
with a Paley–Wiener / Cauchy–Schwarz bound that upgrades L² on
the compact support interval to L^∞ on compact subsets of the
complex strip.

Combining Steps 1 and 2:
  |ξ̂_N − c · Ξ|_{L^∞(K)} ≤ |ξ̂_N − c · k̂_λ|_{L^∞(K)} + |c| · |k̂_λ − Ξ|_{L^∞(K)}
                        = O(1/λ) + O(λ^{−3/2+ε})
                        → 0.

So the convergence holds.

## Concerns

### C1.01.a — Which limit? λ → ∞ or N → ∞?

Both Step 1 (CCM Lemma 7.3) and Step 2 (Corollary 6.6) are stated
as limits "as λ → ∞". But the downstream Bögli spectral exactness
is a statement about "N → ∞". If λ and N are independent
parameters, the two limits are different and do not
automatically commute.

Paper 13 does not cleanly resolve this. My reading: in practice,
the paper is taking a single-parameter limit where λ and N grow
together (e.g., λ = λ(N) → ∞), and all estimates are uniform in
the coupling. But this is nowhere stated.

### C1.01.b — The constant C_K in Corollary 6.6

The Paley–Wiener upgrade |f̂(z)| ≤ C_α · ‖f‖_{L²} for
|Im z| ≤ α < 1/2 gives a constant C_α that depends on the
half-strip height α and the support of f. For f supported on
[−λ, λ] or [λ^{−1}, λ], C_α depends on λ via
∫_{−λ}^λ e^{−2α|t|} dt → 1/α as λ → ∞. So C_α is bounded in λ,
which is the good news.

But: the constant C_K for K ⊂ {|Im z| < 1/2} compact depends on
α = dist(K, {|Im z| = 1/2}). For K approaching the boundary, α
→ 0 and C_K blows up. The uniform convergence holds on **any
fixed compact** K, but not on the full open strip.

This is fine for Hurwitz: Hurwitz cares about "every compact
subset", not the whole open set. Zeros of Ξ in the strip are a
discrete set; each is in some compact subset.

### C1.01.c — What about zeros of Ξ near the boundary |Im z| = 1/2?

These correspond to zeros of ζ with Re s near 0 or Re s near 1
(i.e., at the edge of the critical strip). RH asserts Re s = 1/2
for all non-trivial zeros, so these edge cases are not where
off-line zeros actually hide (which would be at Re s = 1/2 + δ,
|δ| small). So the convergence on compact subsets not reaching
the boundary is sufficient.

### C1.01.d — Corollary 6.6 as a pointwise-in-N upgrade

Corollary 6.6 gives, at each fixed N and large λ, a bound on
|ξ̂_N(z) − c · k̂_λ(z)|. To conclude ξ̂_N(z) → Ξ(z), we need
this to go to 0 as **something grows**. The "something" could
be either λ or N. The paper writes "as λ → ∞" but the downstream
use is "as N → ∞". Conflation.

## Verdict on this subpoint

**Mostly pass, with λ–N conflation.** The uniform-on-compacts
convergence is plausibly established at the shape level:
Paley–Wiener gives L² → L^∞ on compacts, Estimate (b) and CCM
Lemma 7.3 jointly give the L² rate. The surviving concern is
the limit-parameter ambiguity.

If λ is fixed and N → ∞: Corollary 6.6 gives a bounded (not
vanishing) error, which is insufficient for Hurwitz. We need a
joint-limit version.

If λ = λ(N) → ∞ with N → ∞: the estimates must be uniform in N
for each specific coupling. Paper 13 does not verify this.

**Required fix:** state the coupling λ = λ(N) explicitly and
verify that the estimates in Sections 5–7 survive. Alternatively,
state all estimates at fixed λ and use a different argument
(not "λ → ∞") to run the Hurwitz limit as N → ∞.
