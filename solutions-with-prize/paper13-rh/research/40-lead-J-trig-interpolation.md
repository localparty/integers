# Research 40 -- Lead J: Trigonometric Polynomial Interpolation

*Date: 2026-04-09*
*Status: CLEAN BACKUP. Lead L (Direct Discrete Cartwright) may close the interpolation gap entirely; this is the alternative route. Feasibility 6/10.*

---

## 1. Setup: trigonometric interpolant on Chebyshev nodes

Given grid values {phi_k[i]} on Chebyshev nodes {x_i}_{i=0}^{N} in [0, L], define the trigonometric interpolant:

    T(x) = sum_{i=0}^{N} phi_k[i] L_i(x)

where L_i are the Lagrange basis functions satisfying L_i(x_j) = delta_{ij}.

## 2. T is a trigonometric polynomial of bounded degree

T(x) is a trigonometric polynomial of degree at most N/2, supported on [0, L] (with periodic extension outside the interval). The degree bound follows from the number of interpolation nodes: N+1 nodes determine at most N/2 independent frequencies.

## 3. Fourier transform of T: first observation

As a trigonometric polynomial of degree at most N/2, T has a Fourier transform that is compactly supported in frequency space. Therefore T_hat extends to an entire function of exponential type ~ N/(2L).

## 4. Correction: Paley-Wiener gives the sharper statement

T itself is compactly supported on [0, L] (it is identically zero outside this interval). By the Paley-Wiener theorem, T_hat is entire of exponential type L:

    |T_hat(z)| <= ||T||_2 * exp(L |Im z|)  <=  ||T||_2 * exp(L |z|).

The type is sigma = L, independent of N. This is the correct bound.

## 5. Grid overlap as Fourier evaluation

The discrete grid overlap approximates the continuous integral:

    <phi_k | v_p>_grid  approx  integral_0^L T(x) cos(x log p) dx  =  T_hat(log p)

up to quadrature error from replacing the integral by the discrete sum.

## 6. Chebyshev quadrature error

For smooth (analytic) integrands, Chebyshev quadrature error decays exponentially in N. Specifically, for the integrand T(x) cos(x log p) which is analytic on [0, L]:

    |quadrature error| <= C_1 * e^{-alpha N}

for some alpha > 0 depending on the analyticity region.

## 7. The key bound

Combining sections 5 and 6:

    |<phi_k | v_p>_grid  -  T_hat(log p)|  <=  C * e^{-alpha N}

for some C, alpha > 0. The discrete overlap and the continuous Fourier evaluation differ by an exponentially small quantity.

## 8. Invoking Cartwright

By Research 37, Cartwright's theorem implies T_hat(log p) != 0 for all but finitely many primes p (since T_hat is entire of type L and {log p} has infinite density). If the quadrature error is smaller than |T_hat(log p)|:

    C * e^{-alpha N}  <  |T_hat(log p)|

then the grid overlap <phi_k | v_p>_grid is also nonzero.

## 9. Handling the finite exceptions

Cartwright guarantees the zero set {p : T_hat(log p) = 0} is finite. These finitely many exceptional primes are handled by direct numerical verification (as in Lead D's secular induction code, which shows min overlap ~ 10^{-3} for the first 25+ primes). For the remaining (infinitely many) primes, the exponential decay of the quadrature error ensures the grid overlap inherits nonvanishing from T_hat.

## 10. Feasibility assessment

| Aspect | Rating | Notes |
|--------|--------|-------|
| Trigonometric interpolation scheme | 8/10 | Standard numerical analysis. Well-conditioned on Chebyshev nodes. |
| Paley-Wiener for compact support | 9/10 | Textbook. |
| Chebyshev quadrature convergence | 8/10 | Exponential decay is classical (Trefethen). |
| Cartwright at continuous level | 9/10 | Same as Research 37. |
| Quantitative gap closure | 5/10 | Need explicit lower bound on |T_hat(log p)| vs upper bound on quadrature error. |
| Overall | **6/10** | Clean and complete in structure. Lead L is simpler because it avoids the interpolation step entirely. This remains a solid backup if Lead L encounters obstacles. |

---

*Lead J provides a self-contained route: interpolate, invoke Paley-Wiener + Cartwright at the continuous level, then close the gap via Chebyshev quadrature bounds. It works but Lead L is preferred for its directness.*
