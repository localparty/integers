# W8-17: Independent Computation Audit -- Final Verification

**Date:** 2026-04-08
**Precision:** 50 decimal digits (mpmath 1.3.0)
**Runtime:** 79.42 s

## Overview

All 15 numerical checks (9 reproductions + 6 new) were implemented from scratch and executed at 50-digit mpmath precision. Every check passed. The results are fully consistent with Wave 1 and Wave 2 computations.

## Summary Table

| # | Check | Expected | Computed | Error | Verdict |
|---|-------|----------|----------|-------|---------|
| 1 | S_0 = 1 + 2 zeta(0) | 0 | 0.0 (exact) | 0 | PASS |
| 2 | E_2(-j; Q_0) = 0, j=1..20 | 0 for all j | 0 for all j | 0 (exact) | PASS |
| 3 | Z_2 parity f_even + f_odd = 0, n=1..50 | 0 for all n | max |sum| ~ 1.1e-55 | < 1e-40 | PASS |
| 4 | Heat kernel factorization | K_mode = K_wind | Agreement at 5 points | < 1.5e-47 | PASS |
| 5 | Analyticity radius r_t | r_t > 0, match prior | SU(2): 3.16e-4, SU(3): 3.16e-4 | diff ~ 3e-9 | PASS |
| 6 | Poisson bridge | KK ~ winding to 1e-24 | rel_err = 1.09e-24 | 1.09e-24 | PASS |
| 7 | Eisenstein zeta factorization | Direct sum ~ 6*z*L | s=2: 4.9e-7, s=3: 3.3e-13, s=4: 2.7e-19 | truncation-limited | PASS |
| 8 | Weyl anomaly a = c = 0 | 0 | 0.0 (exact) | 0 | PASS |
| 9 | I_{+++} = pi*R/4, 10 pairs | pi/4 for all | Agreement for all 10 pairs | max 3.9e-56 | PASS |
| 10 | (NEW) Seeley-DeWitt a_4 | 0 (flat orbifold) | 0 | 0 | PASS |
| 11 | (NEW) Sunset Eisenstein j=11..20 | 0 for all j | 0 (exact) for all j | 0 | PASS |
| 12 | (NEW) Figure-eight 2*zeta(-2j) | 0 for j=1..10 | 0 (exact) for all j | 0 | PASS |
| 13 | (NEW) Ghost Q=2*Q_0 homogeneity | E(s;2Q) = 2^{-s}*E(s;Q) | Exact agreement at s=2,3,4 | 0 | PASS |
| 14 | (NEW) Wilson coefficient c_1(t) | prefactor/(4*pi*b_0) = 1 | 1.0 (exact) | 0 | PASS |
| 15 | (NEW) Convergence rate with flow | doubly-exponential in K | log|term_K| ~ -4^K confirmed | ratio grows by 4x | PASS |

## Overall Verdict

**ALL 15 CHECKS PASS.**

## Detailed Notes

### Reproduced results (Checks 1-9)

**Check 1 (S_0):** The KK mode count 1 + 2*zeta_R(0) = 1 + 2*(-1/2) = 0 is exact in mpmath. This underpins Lemma 3.4.

**Check 2 (Eisenstein zeros, extended to j=20):** For even j, zeta(-j)=0 (trivial Riemann zeros). For odd j, L(-j, chi_{-3})=0 (trivial Dirichlet zeros for odd character). The product 6*zeta(-j)*L(-j,chi_{-3}) = 0 for all j=1..20 is exact to full precision. The mechanism is complementary trivial zeros. This confirms Lemma 3.6.

**Check 3 (Z_2 parity, extended to n=50):** The identity cos^3(u) + sin^2(u)*cos(u) = cos(u) integrates to 0 over [0, pi*R]. Numerical quadrature confirms |sum| < 1.1e-55 for all n, consistent with machine epsilon at 55-digit internal precision.

**Check 4 (Heat kernel factorization):** K_{R^4 x S^1} = K_{R^4} * K_{S^1} verified at 5 test points. Mode sum and winding sum for K_{S^1} agree to < 1.5e-47 relative error, with exact agreement at phi=pi (antipodal point) limited only by the exponential smallness of the kernel there.

**Check 5 (Analyticity radius):** Using the Combes-Thomas formula delta_0 = min(log(1 + m_W^2/(4d)), 1) from Appendix K, with kappa = delta_0 and the Mayer convergence constraint rho = kappa/(2d), we obtain r_t = rho/L_flow = 3.1575e-4 for both SU(2) and SU(3), matching Waves 1-2 to 9 significant figures (difference ~ 3e-9 from rounding in the 8-digit reported values).

**Check 6 (Poisson bridge):** KK sum (N=100000) and Poisson winding sum (M=150) agree to relative error 1.09e-24, consistent with the O(N^{-5}) KK truncation tail. This confirms the Poisson resummation identity used in the KK-to-winding correspondence.

**Check 7 (Eisenstein factorization):** Direct double sum over the hexagonal lattice agrees with 6*zeta(s)*L(s,chi_{-3}) at s=2,3,4 with truncation errors scaling as O(N^{-(2s-2)}), confirming the factorization theorem for the Eisenstein quadratic form.

**Check 8 (Weyl anomaly):** a_total = (43/360)*S_0 = 0 and c_total = (87/20)*S_0 = 0 exactly, since S_0 = 0. The 5D anomaly cancellation follows from the KK mode count vanishing.

**Check 9 (Three-graviton vertex):** The product-to-sum identity gives I_{+++} = pi*R/4 analytically, independent of (n1,n2). Numerical quadrature with adaptive subdivision confirms this for all 10 test pairs including (100,200), with maximum error 3.9e-56.

### New checks (Checks 10-15)

**Check 10 (Seeley-DeWitt a_4):** On flat M^4 x S^1/Z_2, all bulk curvature invariants vanish, and the orbifold fixed-point boundaries have zero extrinsic curvature, giving a_4 = 0. The heat trace asymptotics confirm: residual after subtracting the leading (1/2)*sqrt(pi/t) + 1/2 is O(10^{-54}), consistent with no subleading corrections.

**Check 11 (Sunset Eisenstein j=11..20):** Extension of Check 2 to j=11..20. Same mechanism of complementary trivial zeros gives exactly 0 for all values.

**Check 12 (Figure-eight topology):** Each one-loop factor gives 2*zeta(-2j) = 0 for j=1..10, exact in mpmath. Trivial Riemann zeros at all negative even integers.

**Check 13 (Ghost contribution):** The ghost quadratic form Q = 2*(n^2+nm+m^2) satisfies E(s; 2Q_0) = 2^{-s} * E(s; Q_0) by homogeneity, verified exactly at s=2,3,4 by direct double sum. Since E(-j; Q_0) = 0, the ghost contribution inherits the same cancellation: 2^j * 0 = 0.

**Check 14 (Wilson coefficient c_1):** The Luscher-Weisz one-loop prefactor (11N)/(12*pi) equals 4*pi*b_0 exactly, confirming consistency between the gradient flow Wilson coefficient and the perturbative beta function. Verified for both SU(2) and SU(3).

**Check 15 (Convergence rate):** The telescoping sum without flow factor converges only polynomially (log10|term_K| ~ -0.66*K). With the flow factor exp(-t/a_K^2), the convergence is doubly exponential: log10|term_K| ~ -4^K. At K=5, the flowed term is already O(10^{-226}). The ratio test confirms: log10(term_{K+1}/term_K) grows by a factor of ~4 at each step, consistent with the exp(-3*t*4^K) decay of the ratio.

## Files

- Computation script: `code/final-audit/compute.py`
- Raw results: `code/final-audit/results.txt`
- This summary: `research/W8-17-computation-audit.md`
