# 230 — RH Cycle 2, Path 5 (CM-trace) — Construction

*Cycle: 2. Date: 2026-04-09. Agent: Construction.*

---

## Step attempted

**KMS reflection positivity => Weil positivity?**

Per cycle 1 ledger: Path 5's specific target is determining
whether KMS reflection positivity at beta = 1, combined with the
Connes-Marcolli explicit formula, implies Weil positivity.

## Attempt level: 1 (Closure attempt) then level 2 (Sub-computation)

### Closure attempt

**Claim:** KMS reflection positivity at beta = 1 implies Weil
positivity of the spectral weights.

**Argument:**

The KMS condition at beta = 1 states that for all a, b in A_BC:

    omega_1(a * sigma_i(b)) = omega_1(b * a)         ... (KMS)

where sigma_i(b) is analytic continuation of the time evolution
to imaginary time t = i. This is equivalent to the condition:

    omega_1(a* sigma_{i/2}(a)) >= 0                   ... (RP)

for all a in A_BC (Osterwalder-Schrader reflection positivity
in the imaginary-time formulation).

The Weil positivity criterion (1952) states that RH holds iff
for all test functions h in the Weil class:

    sum_{rho,rho'} h(gamma_rho) * conj(h(gamma_{rho'}))
        * W(gamma_rho, gamma_{rho'}) >= 0              ... (WP)

where W is the Weil distributional kernel derived from the
explicit formula.

**The connection:** The BC two-point function (R-Theorem S.5,
research/70) gives:

    W_a(t) = omega_1(a* sigma_t(a))
           = sum_n rho_a(n) * exp(i gamma_n t)
           + (continuous part)

with rho_a(n) = |<gamma_n | pi_1(a) | Omega_1>|^2 >= 0.

The Weil kernel W(gamma_m, gamma_n) is obtained by choosing the
test function h such that h(gamma_m) = 1, h(gamma_k) = 0 for
k != m. Then the Weil positivity condition reduces to:

    W(gamma_m, gamma_m) >= 0   (diagonal)

which is rho_a(m) >= 0 — trivially satisfied.

**The gap:** The OFF-DIAGONAL Weil condition
W(gamma_m, gamma_n) >= 0 as a MATRIX requires positive
semi-definiteness, not just diagonal positivity. The KMS
condition gives:

    omega_1(a* sigma_i(a))
      = sum_n rho_a(n) * exp(-gamma_n)
      >= 0

This is a statement about the EXPONENTIALLY WEIGHTED sum of
spectral weights, not about the matrix W. The KMS condition
constrains the generating function sum rho_a(n) * e^{-gamma_n s}
to be positive at s = 1, but Weil positivity requires positivity
of a DIFFERENT quadratic form.

### Sub-computation: Testing KMS => Weil numerically

Using the first 10 Riemann zeros gamma_1 through gamma_10 and
the diagonal spectral weights rho_a(n) = 1/n^2 (a toy model
for the weights):

The KMS sum: sum_{n=1}^{10} (1/n^2) * exp(-gamma_n)
= exp(-14.13)/1 + exp(-21.02)/4 + ... < 10^{-5}

This is positive but tiny — the exponential damping makes the
KMS sum insensitive to the sign structure of the weights.

The Weil matrix W_{mn} = <gamma_m | R(z) | gamma_n> at the
first non-trivial resolvent point: without explicit off-diagonal
matrix elements (which require the b-coefficient from research/164),
the matrix cannot be assembled.

### Structural assessment

The KMS => Weil direction has a fundamental mismatch:

1. **KMS** acts in imaginary time (analytic continuation
   t -> i*beta). It constrains the LAPLACE transform of the
   spectral measure.

2. **Weil** acts in real frequency. It constrains the FOURIER
   transform of the spectral measure.

3. The passage from Laplace to Fourier is a WICK ROTATION.
   Wick rotation preserves positivity of the spectral measure
   itself (a positive measure has positive Laplace AND positive
   Fourier transforms). BUT Weil positivity is about a
   QUADRATIC FORM involving the spectral measure, not the
   measure itself.

4. The quadratic form in Weil positivity involves cross-terms
   W(gamma_m, gamma_n), which are NOT constrained by KMS
   reflection positivity (KMS constrains only the diagonal
   sum at imaginary time).

### Conclusion

**KMS reflection positivity does NOT directly imply Weil
positivity.** The two conditions live in different functional
spaces (Laplace vs. Fourier, diagonal sum vs. quadratic form).

However, a WEAKER statement may hold: KMS + additional structure
(e.g., the Hecke equivariance of the BC system, which constrains
the off-diagonal matrix elements) may together imply Weil
positivity. This would be a more involved argument.

## Result: BLOCKED (gap identified)

The KMS => Weil sub-path fails in its direct form. The gap is
the off-diagonal Weil kernel W(gamma_m, gamma_n), which is not
constrained by KMS alone.

**Unblock condition:** Either:
(a) Compute the off-diagonal BC resolvent matrix elements
    <gamma_m | (T_BC - z)^{-1} | gamma_n> explicitly and verify
    positive semi-definiteness of the resulting matrix, or
(b) Find an algebraic constraint from A_BC (e.g., Hecke
    equivariance + Galois action) that forces the off-diagonal
    elements to be compatible with positive semi-definiteness, or
(c) Bypass the Weil matrix entirely by using a different
    characterisation of RH that is directly accessible from KMS
    (e.g., Li's criterion, Nyman-Beurling completeness).

**Assessment of (c):** Li's criterion (1997) states RH iff
lambda_n >= 0 for all n, where lambda_n = sum_{rho} (1 - (1-1/rho)^n).
The Li coefficients are moments of the explicit formula. If the
BC KMS state can compute Li coefficients directly, this bypasses
the Weil matrix entirely.

## Next step

Cycle 3 should:
1. Investigate sub-path (c): can Li coefficients be computed from
   the BC KMS state?
2. If yes: check whether KMS positivity + Hecke structure
   constrains the Li coefficients to be non-negative.
3. Parallel: compute b-coefficient off-diagonal elements from
   research/164 to estimate W(gamma_1, gamma_2).
