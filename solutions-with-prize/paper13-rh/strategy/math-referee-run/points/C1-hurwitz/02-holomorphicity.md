# C1.02 — Holomorphicity of ξ̂_N

## Question

Hurwitz requires the sequence and the limit to be holomorphic on
a connected open set. Are ξ̂_N holomorphic?

## Finding

### Pattern 1: From the CCM formula

CCM's Theorem 5.10(iii) (Paper 13 Appendix A.4) gives the explicit
formula:

  ξ̂(z) = 2 L^{−1/2} sin(zL/2) · Σ_{j=−N}^N ξ_j / (z − 2π j/L).

As a function of z ∈ ℂ:
- sin(zL/2) is entire.
- Σ_j ξ_j / (z − 2π j/L) is a rational function with simple poles
  at z = 2π j/L for j = −N, ..., N.
- The sine has zeros at z = 2π n/L for all integer n; these
  cancel the poles at |j| ≤ N (provided ξ_j ≠ 0, which is
  generically true).

After cancellation, ξ̂_N is an entire function (a polynomial
times sin times a rational whose poles are cancelled). Or it may
be meromorphic with residual zeros of the sine at |n| > N — these
are real zeros at 2π n/L.

**Verdict:** ξ̂_N is either entire or meromorphic with simple
real zeros and no poles. In either case, Hurwitz applies in any
connected open set that avoids the (non-existent) poles.

### Pattern 2: From the L² eigenvector

The eigenvector ξ_λ is an L² function on the support interval
(e.g., [λ^{−1}, λ]). Its Fourier transform extends to an entire
function on ℂ (Paley–Wiener theorem for compactly supported L²
functions): the Fourier transform of a compactly supported L²
function is entire and of exponential type.

Both patterns give holomorphicity in the strip {|Im z| < 1/2} (or
indeed on all of ℂ).

## Consistency with the real-zero property

Does the "entire, of exponential type, with only real zeros"
structure check out?

Entire functions of finite exponential type with only real zeros
are of "real type" (Levin's theory of entire functions of type
zero or exponential type). Ξ itself is such a function — it is
entire of order 1, and RH asserts its real-type nature.

For finite-dim ξ̂_N: the explicit formula makes it clear that
every zero of the "rational factor" Σ_j ξ_j/(z − 2π j/L) (after
cancellation with the sine) is real, because it is the root of a
real polynomial with real coefficients (ξ_j are real). The sine
factor has only real zeros. So the zero set of ξ̂_N is a subset
of ℝ.

**This is the critical real-zero property.** Paper 13 never states
it as a named proposition, but it is implicit in CCM Theorem
5.10(iii) and is what makes the Hurwitz argument work.

## Verdict on this subpoint

**Pass on holomorphicity.** ξ̂_N is holomorphic (indeed entire or
meromorphic with removable singularities) on ℂ. It fits the
Hurwitz framework.

**Pass on the implicit real-zero property.** This follows from
CCM's identification plus the explicit formula. It should be
stated as a lemma in Paper 13 but is not.
