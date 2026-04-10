# research/01 -- Cycle 1 Synthesis

*Date: 2026-04-10. Status: All premise checks complete.*

## Summary

The v2 premise checker killed three of four paths before any
construction was attempted. This validates the methodological
upgrade from v1: checking premises prevents wasted cycles.

## The deeper finding

Paths A, B, C all fail for a reason that transcends the specific
mechanisms. The failure is not that our invariants are too stable
(v1 coboundary) or too weak. The failure is that the operator
formalism itself -- T_BC self-adjoint by Stone's theorem -- already
excludes off-line zeros. Every attempt to "detect" off-line zeros
within the formalism is detecting something that cannot exist in
the formalism.

This means:
- **If the Stone chain is valid**, RH is already proved (research/08).
- **If the Stone chain has a gap**, the gap is in the spectral
  realisation step (distributional vs point spectrum), not in the
  detection mechanism.

All four paths collapse to one question: **is the Riemann-Weil
inclusion an inclusion of eigenvalues or of distributional spectral
values?**

## The spectral realisation gap (the REAL problem)

The Connes programme establishes:
1. T_BC exists and is self-adjoint (Stone, rigorous)
2. spec(T_BC) is real (spectral theorem, rigorous)
3. {gamma_n} is in spec(T_BC) (Meyer 2005, rigorous distributionally)
4. Therefore gamma_n are real (logic)

The gap is in step 3: "in spec" means distributional spectrum, which
includes resonances. For the conclusion gamma_n in R, we need either:
(a) gamma_n are eigenvalues (point spectrum) of T_BC, or
(b) the distributional spectrum of a self-adjoint operator is always
    contained in R (which is true -- the distributional spectrum IS
    a subset of R for self-adjoint operators by definition).

Wait. (b) is actually true. The distributional spectrum of a
self-adjoint operator T is defined as {z : (T-z)^{-1} does not
extend to a bounded operator near z}, and for self-adjoint T this
is always a subset of R.

So the Stone chain IS valid if the Riemann-Weil inclusion places
gamma_n in the distributional spectrum of T_BC (which Meyer 2005
proves). The "gap" may be smaller than previously assessed.

The subtlety: Meyer 2005 proves a distributional identity that
IDENTIFIES the spectral side with the sum over zeros. This is
not a statement about individual gamma_n being spectral values
of T_BC; it is a statement about the distribution
sum_n delta(x - gamma_n) being related to the spectral measure of T_BC.

For self-adjoint T_BC, the spectral measure is supported on R.
The Riemann-Weil identity equates a function of the spectral measure
with a sum over zeros. If the zeros were off the critical line
(gamma_n complex), the sum over zeros would have support off R,
contradicting the support of the spectral measure on R.

THIS IS THE ARGUMENT. It is not circular. It is the content of
the Stone chain. The distributional identity is the link.

## Assessment

The Stone chain may actually be closer to a valid proof than
previously thought. The key step -- that the distributional identity
constrains the support of the zero-sum to R -- is a consequence of
self-adjointness and the Riemann-Weil formula. The question is
whether this argument is rigorous enough for Clay-level acceptance.

Feasibility of closing the remaining gap: 4/10.
This is higher than the 3/10 assigned to Path D because the
distributional argument may be sufficient.
