# W2-07: Independent Numerical Verification -- Summary

**Agent:** W2-07 (Wave 2 Computation)
**Date:** 2026-04-08
**Precision:** 50-digit mpmath arithmetic (mpmath 1.3.0)
**Method:** All code written from scratch; no Wave 1 code copied.

## Result: 9/9 PASS

| # | Check | Expected | Computed | Error | Verdict |
|---|-------|----------|----------|-------|---------|
| 1 | S_0 = 1 + 2 zeta(0) | 0 | 0.0 (exact) | 0 | PASS |
| 2 | E_2(-j; Q_0) = 0, j=1..10 | 0 for all j | |E_2| < 1e-40 | < 1e-40 | PASS |
| 3 | Z_2 parity cancellation | f_even + f_odd = 0 | |sum| < 1e-40 | < 1e-40 | PASS |
| 4 | Heat kernel factorization | K_5D = K_R4 * K_S1 | mode vs winding S1 | < 1e-41 | PASS |
| 5 | Analyticity radius r_t | ~3.16e-4 | 3.1575e-4 (SU2,SU3) | ~3e-9 vs W1 | PASS |
| 6 | Poisson bridge | ~1e-24 agreement | 1.09e-24 | matches Paper 10 | PASS |
| 7 | Eisenstein factorization | 6 zeta(s) L(s,chi_{-3}) | truncation-consistent | s=4: 2.7e-19 | PASS |
| 8 | Weyl anomaly sum | a=c=0 | 0.0 (exact) | 0 | PASS |
| 9 | Three-graviton vertex | pi R/4 | exact + num < 1e-51 | 5e-51 | PASS |

## Detailed Notes

### Checks 1, 8 (S_0 and Weyl anomaly)

S_0 = 1 + 2 zeta_R(0) = 1 + 2(-1/2) = 0 exactly at 50-digit precision.
This directly gives a_total = (43/360) x 0 = 0 and c_total = (87/20) x 0 = 0.
Both are algebraically exact once zeta(0) = -1/2 is established.

### Check 2 (Eisenstein complementary zeros)

E_2(-j; Q_0) = 6 zeta(-j) L(-j, chi_{-3}) vanishes for all j = 1..10 by complementary trivial zeros:
- j even: zeta(-j) = 0 (Riemann zeta trivial zeros at negative even integers)
- j odd: L(-j, chi_{-3}) = 0 (Dirichlet L trivial zeros for odd character at odd negative integers)

The L function was computed via Hurwitz zeta: L(s, chi_{-3}) = 3^{-s} [zeta(s, 1/3) - zeta(s, 2/3)].
For odd j, the numerical value is O(10^{-50}), consistent with the 50-digit working precision.

### Check 3 (Z_2 parity cancellation)

The identity cos^3(u) + sin^2(u) cos(u) = cos(u) implies the sum of even and odd
y-integrals equals integral_0^{pi R} cos(ny/R) dy = (R/n) sin(n pi) = 0.
Verified by direct quadrature: the identity integral is O(10^{-51}) for all n = 1..20.

### Check 4 (Heat kernel factorization)

Two independent representations of K_{S^1} were compared:
- Mode sum (Jacobi theta): K = (1/2piR) [1 + 2 sum exp(-n^2 t/R^2) cos(n dphi/R)]
- Winding sum (Poisson): K = (4 pi t)^{-1/2} sum_w exp(-(dphi + 2piRw)^2 / 4t)

Agreement to < 10^{-41} at all 6 test points, confirming the product structure
K_{R^4 x S^1}(t) = K_{R^4}(t) K_{S^1}(t).

### Check 5 (Analyticity radius)

The Combes-Thomas decay exponent is delta_0 = ln(1 + m_W^2 a^2/(4d)) = ln(1 + 1/16) = 0.06062462...
(not arccosh -- this was the source of the initial discrepancy with Wave 1).

Both SU(2) and SU(3) give r_t = rho/L_flow = 0.00031575..., with the Mayer convergence
condition kappa/(2d) as the binding constraint for rho. Agreement with Wave 1: |diff| < 4e-9,
limited by the 8-digit truncation of the reference value.

Key finding: r_t is independent of N for these parameters because the Mayer constraint
(kappa/(2d) = 0.00758) binds before the propagator constraint (m_W a/(2 C_D)) for both N=2 and N=3.
At larger N, the propagator constraint 1/(4(N^2-1)) would eventually bind, giving r_t ~ O(1/N^2).

### Check 6 (Poisson bridge)

At (k^2 = 4, R = 1, s = 3), the KK sum (N = 100,000 modes) and Poisson winding sum
(M = 150 terms) agree to relative error 1.09 x 10^{-24}. This exactly reproduces the
Paper 10 (Route 04) result.

The residual is dominated by the KK tail truncation. The winding sum converges exponentially
(last term ~ e^{-2pi*150*2} ~ 0) and is exact to machine precision. A refined tail
estimate gives the KK truncation error as O(N_KK^{-5}) ~ 10^{-25}.

The F_hat(0) Poisson term was independently cross-checked by numerical integration
of the Fourier transform; exact agreement (error 0.0) with the Gamma-function formula.

### Check 7 (Eisenstein factorization)

The identity E_2(s; n^2+nm+m^2) = 6 zeta(s) L(s, chi_{-3}) was verified by direct
double sum over |n|, |m| <= 1000. Truncation errors match the expected scaling:

- s = 2: rel_err = 4.86e-7 (expected O(N^{-2}) ~ 5e-7)
- s = 3: rel_err = 3.28e-13 (expected O(N^{-4}) ~ 2e-13)
- s = 4: rel_err = 2.67e-19 (expected O(N^{-6}) ~ 2e-19)

All errors are consistent with the tail truncation and confirm the factorization.

### Check 9 (Three-graviton vertex)

The integral I_{+++}(n1, n2, n1+n2) = integral_0^{piR} cos(n1 y/R) cos(n2 y/R) cos((n1+n2) y/R) dy
equals pi R/4 exactly, by the product-to-sum identity. The only surviving term is cos(0) = 1
from the decomposition a+b-c = 0 when c = a+b.

This was verified both analytically and numerically for (n1,n2) in {(1,1), (1,10), (5,5), (3,7), (100,200)}.
The numerical quadrature (with adaptive subdivision for high-frequency integrands) agrees to
relative error < 5.1e-51 for all test pairs, including (100, 200) which has oscillation
frequency 300/R in the fastest cosine mode.

The universality of I_{+++} = pi R/4 (independent of KK levels n1, n2) is the key input
to Theorem 1 of Paper 10: the three-graviton coupling is level-independent, and the
Goroff-Sagnotti coefficient factorizes as C_GS = g^2 J(0,0) S_0^2 = 0.

## Files

- Script: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/numerical-verify/compute.py`
- Results: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/numerical-verify/results.txt`
- This memo: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W2-07-numerical-verification.md`
