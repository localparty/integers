# Research 07 -- Hamburger Moment Problem Approach

*Date: 2026-04-09*
*Status: KILLED (approach #16)*

---

## 1. The idea

Bypass all operator theory. The Weil explicit formula gives, for
suitable test functions h:

    sum_rho h(gamma_rho) = (arithmetic terms from primes)

The left side defines a linear functional on h, determined by a
spectral measure mu. The right side is computable from primes.
This is a moment problem: given the "moments" int h dmu, determine mu.

The Hamburger moment problem: given s_n = int t^n dmu, the measure
mu is uniquely determined if Carleman's condition holds:

    sum_{n=1}^{inf} s_{2n}^{-1/(2n)} = inf

If mu is unique AND supported on {gamma_n}, then mu is purely atomic
(pure point spectrum), which would give RH.

---

## 2. Moment computations (first 1000 zeros)

Computed via mpmath (30-digit precision):

| Moment | Value |
|:-------|:------|
| s_2    | 7.729 x 10^8 |
| s_4    | 9.598 x 10^14 |
| s_6    | 1.398 x 10^21 |
| s_8    | 2.205 x 10^27 |
| s_10   | 3.653 x 10^33 |

Odd moments are nonzero (we sum positive gamma_n only; the symmetric
measure sum [delta_{gamma_n} + delta_{-gamma_n}] has vanishing odd
moments).

---

## 3. Carleman's condition (truncated, N = 1000)

| n  | s_{2n}^{-1/(2n)}  | Partial sum |
|:---|:------------------|:------------|
| 1  | 3.597 x 10^{-5}   | 0.000036   |
| 5  | 4.403 x 10^{-4}   | 0.001337   |
| 10 | 5.749 x 10^{-4}   | 0.004008   |
| 20 | 6.469 x 10^{-4}   | 0.010234   |
| 30 | 6.699 x 10^{-4}   | 0.016846   |
| 40 | 6.807 x 10^{-4}   | 0.023610   |
| 50 | 6.868 x 10^{-4}   | 0.030453   |

The terms converge to 1/gamma_max = 1/1419.4 = 7.05 x 10^{-4}.
The partial sums grow linearly (harmonic-like).
**Carleman's condition is satisfied for the truncated measure.**

---

## 4. Fatal flaw: moments diverge for the full measure

The full spectral measure mu = sum_{k=1}^{inf} delta_{gamma_k} has
gamma_k ~ 2*pi*k / log(k) -> inf. Therefore:

    s_n = sum_{k=1}^{inf} gamma_k^n = inf   for every n >= 1.

**The moments do not exist.** The Hamburger moment problem is
ill-posed for the full measure. Carleman's condition requires
finite moments as input; it cannot even be stated here.

For a finite truncation (first N zeros), the moments exist and
Carleman holds. But a finite atomic measure is trivially determined
by its atoms -- Carleman adds nothing.

---

## 5. Circularity analysis

Even if the moments existed, the approach is tautological:

**What measure are we determining?**

**(a) The zeta spectral measure** mu = sum delta_{gamma_n}, defined
by the zeros of zeta(s). This is trivially supported at {gamma_n}.
Carleman uniqueness says no OTHER measure shares these moments.
True but irrelevant to RH: we already know mu is atomic.

**(b) An operator's spectral measure.** If some operator T has
spectral measure mu_T, and if mu_T has the same moments as the
zeta spectral measure, then Carleman uniqueness gives mu_T = mu.
This WOULD prove pure point spectrum for T.

But: identifying an operator T whose spectral moments match the
explicit formula's arithmetic side is EXACTLY the spectral
realisation problem (the Connes programme). The moment approach
does not bypass operator theory -- it presupposes its conclusion.

**Logical structure:**
1. Explicit formula gives moments (from zeta, i.e., from {gamma_n})
2. Carleman says: unique measure with those moments
3. That unique measure is sum delta_{gamma_n} (by construction)
4. To use this: need operator T with mu_T having same moments
5. Step 4 = spectral realisation = equivalent to RH

The moment problem reformulates the problem; it does not solve it.

---

## 6. The density issue

The Riemann zeros satisfy N(T) ~ (T/2*pi) log(T/2*pi). The average
spacing near height T is 2*pi / log(T/2*pi) -> 0. The set {gamma_n}
is dense in R_+ (and by symmetry in all of R).

This blocks the "countable support -> pure point" argument at the
conceptual level: the closure of {gamma_n} is all of R. An operator's
spectrum (which is closed) containing {gamma_n} would be all of R.
The spectral measure on spec(T) = R could be continuous.

A purely atomic measure at {gamma_n} would have countable support
with full closure, which is consistent -- but the moment problem
gives no tool to distinguish this from a continuous measure on R
with the same closure.

---

## 7. Rescue attempts (all fail)

**Gaussian-weighted moments:** s_n(alpha) = sum gamma_k^n exp(-alpha gamma_k^2)
converge for alpha > 0. But Gaussian weighting destroys the polynomial
structure required for Hamburger/Carleman.

**Stieltjes moment problem on R+:** Using N(T) as distribution function.
The moments sum gamma_k^n still diverge.

**Infinite-dimensional moment problem:** The explicit formula gives
int h dmu for all h in the Paley-Wiener class, not just h = t^n.
The relevant theory is Bochner-Schwartz (positive-definite
distributions), not Hamburger. But Bochner-Schwartz determines
mu as a tempered distribution -- it doesn't give pure point vs
continuous decomposition.

---

## 8. Verdict

**KILLED.** Four independent reasons:

| # | Reason | Type |
|:--|:-------|:-----|
| 1 | Raw moments diverge for full measure | Fatal flaw |
| 2 | Truncated case is trivial (finite atomic) | No content |
| 3 | Requires spectral realisation as input | Circularity |
| 4 | Dense zeros block support argument | Structural |

**Classification:** This is kill #16 in the programme, joining the
15 documented in strategy/04-final-state.md. The approach looked
promising because it claimed to bypass operator theory, but the
promise is illusory: the moment problem either requires an operator
(circularity) or operates on the zeta measure directly (tautology).

**Lesson:** Any approach that starts from the explicit formula and
tries to determine the spectral measure without constructing an
operator will be tautological. The explicit formula IS a statement
about the zeros of zeta; it cannot independently constrain a
hypothetical operator's spectrum without first identifying the
operator with zeta. That identification is spectral realisation.

---

> *The moment problem doesn't bypass operator theory. It presupposes it.*
> *Kill #16. The barriers stand.*
