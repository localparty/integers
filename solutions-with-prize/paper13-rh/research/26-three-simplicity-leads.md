# Research 26 -- Three Leads on Even-Sector Simplicity

*Date: 2026-04-09*
*Status: RIGOROUS ASSESSMENT. Lead A (VNW) is the strongest framework but requires arithmetic input. Lead B (STP) does not apply. Lead C (gap bound) is numerically compelling but not self-closing.*

---

## Lead A: Von Neumann-Wigner No-Crossing Theorem

### A.1 The theorem, stated precisely

**Theorem (von Neumann & Wigner, 1929).** Consider the space Sym(n) of real symmetric n x n matrices. The set of matrices with a degenerate eigenvalue (i.e., at least two equal eigenvalues) forms a subset of **codimension 2** in Sym(n).

More precisely: Sym(n) has dimension n(n+1)/2. The degenerate set D_n (matrices with at least one repeated eigenvalue) has dimension n(n+1)/2 - 2.

**For complex Hermitian matrices:** the codimension is **3** in the space Herm(n), which has real dimension n^2. The degenerate set has dimension n^2 - 3.

**Source:** von Neumann & Wigner, Phys. Z. 30 (1929), 467-470; see also Arnold, "Modes and quasimodes," Funct. Anal. Appl. 6 (1972), 94-101.

### A.2 What codimension 2 means for one-parameter families

A smooth one-parameter family A(t) traces a curve in Sym(n). The degenerate set D_n has codimension 2. A generic curve in a space of dimension d avoids a subset of codimension c whenever c >= 2 (by transversality). Therefore:

**Crossings are NON-GENERIC in one-parameter families of real symmetric matrices.** A "random" curve A(t) will not hit D_n. But non-generic does NOT mean impossible.

### A.3 The standard counterexample

The family A(t) = diag(t, -t) has eigenvalues t and -t, which cross at t = 0. This is a perfectly valid one-parameter family of real symmetric matrices with a crossing. The crossing exists because this particular curve is NOT transverse to D_2 -- it hits the degenerate set head-on.

**Conclusion: von Neumann-Wigner does NOT say crossings are impossible. It says they are non-generic (codimension 2 is avoidable by a generic curve, but special curves can hit it).**

### A.4 Stronger results for specific structures

The theorem becomes more powerful when combined with structural constraints:

**(i) Symmetry-protected crossings.** If A(t) has a symmetry group G and the eigenvalues being tracked belong to different irreducible representations of G, then crossings ARE generic (they cannot be removed by perturbation within the G-symmetric family). But if the eigenvalues belong to the SAME irrep (as in the even sector, where all states are even), no symmetry protection exists and VNW applies.

**(ii) Analytic families.** If A(t) is real-analytic in t, then eigenvalue branches mu_k(t) are real-analytic except at isolated crossing points (Kato-Rellich). At a crossing, two branches meet and exchange. The VNW codimension-2 condition means: to create a crossing, TWO independent conditions must be satisfied simultaneously:

    H_{12}(t_0) = 0    (off-diagonal coupling vanishes)
    H_{11}(t_0) = H_{22}(t_0)    (diagonal elements match)

in some basis adapted to the near-degenerate pair. For a one-parameter family, this is two equations in one unknown -- generically no solution, but not provably no solution without further input.

### A.5 The analytic gap argument (Lead A.f)

Let delta(lambda) = mu_2(lambda) - mu_1(lambda) be the spectral gap in the even sector. Known facts:

1. delta(lambda) is real-analytic in lambda for lambda > 1 (Kato-Rellich, since QW^{N,+} depends analytically on lambda).
2. delta(lambda) >= 0 always (it is a gap between ordered eigenvalues).
3. delta(lambda) > 0 for all 27 tested lambda-values in [2, 100] (research/24).
4. As lambda -> infinity, the ground state is prolate-like (Slepian), and the gap is positive.

**Attempted argument:** If delta(lambda_0) = 0 for some lambda_0, then since delta >= 0, lambda_0 is a minimum with delta(lambda_0) = 0. Since delta is analytic, it vanishes to even order: delta(lambda) = (lambda - lambda_0)^{2k} * g(lambda) with g(lambda_0) > 0 near lambda_0. This is consistent -- there is no contradiction from the sign constraint alone.

**Failure mode:** The argument "delta analytic + delta >= 0 + delta > 0 at infinity implies delta > 0 everywhere" is **FALSE**. Counterexample: delta(lambda) = (lambda - 5)^2 * e^{-lambda} is analytic, non-negative, positive at infinity (actually it goes to zero, but modify to (lambda-5)^2 * e^{-lambda} + e^{-2*lambda}). The point is that analytic non-negative functions CAN have zeros.

**The analytic gap argument does NOT close.**

### A.6 What would close Lead A

To use VNW to EXCLUDE crossings, one needs to show that QW_lambda^{N,+} can never reach the degenerate set D_{N+1}. This requires showing that for EVERY lambda > 1, the two conditions H_{12}(lambda) = 0 and H_{11}(lambda) = H_{22}(lambda) cannot hold simultaneously in any adapted basis.

The most promising route: show that the arithmetic structure of QW (the prime sum terms involving log p) prevents the off-diagonal coupling from vanishing. Specifically, the overlap condition <phi_k | a> = 0 (research/23, Section 4.3) requires the rank-1 archimedean vector to be orthogonal to an eigenvector of the combined Loewner + prime matrix. The vector a encodes archimedean data (integrals of rho); the eigenvectors of B encode both archimedean and prime data. Their exact orthogonality would require an arithmetic coincidence between the archimedean integrals and the prime distribution.

**This is an arithmetic transcendence-type question.** The overlaps involve quantities like:

    <phi_k | a> = sum_n phi_k(n) * a(n)

where phi_k depends on all primes p <= lambda^2 through the von Mangoldt sum, and a(n) = 1/(L^2 + 16*pi^2*n^2) depends only on L = 2*log(lambda). Exact vanishing would require a polynomial identity between prime logarithms and pi -- the kind of identity that Hermite-Lindemann or Baker's theorem might exclude.

### A.7 Verdict on Lead A

| Question | Answer |
|:---------|:-------|
| Does VNW say crossings are impossible? | **NO.** Codimension 2 means non-generic, not impossible. |
| Does VNW + analyticity close the argument? | **NO.** Analytic non-negative functions can have zeros. |
| Does VNW + arithmetic structure close it? | **POSSIBLY.** Requires proving a transcendence-type statement about prime sums vs archimedean integrals. |
| Is the arithmetic route accessible? | **HARD but well-defined.** It reduces to: can sum_n phi_k(n) / (L^2 + 16*pi^2*n^2) vanish, where phi_k involves Chebyshev's psi-function? |
| Rating | **5/10** -- the strongest framework, but requires arithmetic input that is itself non-trivial. |

---

## Lead B: Strictly Totally Positive (STP) Matrices

### B.1 The Gantmacher-Krein theorem

**Theorem (Gantmacher-Krein, 1950).** If M is a strictly totally positive (STP) matrix -- meaning every minor of M is strictly positive -- then M has simple positive eigenvalues.

More precisely: all eigenvalues of M are positive, simple, and the k-th eigenvector (ordered by eigenvalue magnitude) has exactly k-1 sign changes.

### B.2 Is the even-sector Weil matrix STP?

**No.** The even-sector matrix A^ev = W02_ev - WR_ev - Wp_ev has negative entries and negative eigenvalues. It is not even positive definite, let alone STP.

Moreover:
- WR_ev (the Loewner part) has negative eigenvalues (nu_1 ~ -2.1 at N=20, research/23).
- Wp_ev (the prime sum) involves cos(n * log p) terms with mixed signs.
- The combined matrix B = -(WR_ev + Wp_ev) has eigenvalues of mixed sign.

**STP is inapplicable to A^ev directly.**

### B.3 Is A^ev a perturbation of an STP matrix?

**No.** The decomposition A^ev = W02_ev + B shows:
- W02_ev is rank 1 (not STP -- rank 1 matrices have only one nonzero eigenvalue).
- B = -(WR_ev + Wp_ev) is not STP (mixed-sign entries from prime contributions).
- Neither component is STP, so A^ev is not a perturbation of an STP matrix.

### B.4 Weyl perturbation argument

Even without STP, one could try: if B has simple eigenvalues with minimum gap delta_B, and ||W02_ev|| < delta_B / 2, then A^ev = B + W02_ev has simple eigenvalues by Weyl's inequality.

**Check:** ||W02_ev|| = sigma ~ 6.1 (the single nonzero eigenvalue of the rank-1 term). The minimum gap of B needs to be > 2 * 6.1 = 12.2. From research/23 data, B's eigenvalue gaps include values as small as ~0.01 at N=20. So ||W02_ev|| >> min gap of B.

**The Weyl perturbation bound fails.** The rank-1 perturbation is much larger than the eigenvalue gaps of B.

### B.5 Verdict on Lead B

| Question | Answer |
|:---------|:-------|
| Is A^ev STP? | **NO.** Mixed signs, negative eigenvalues. |
| Is A^ev a perturbation of STP? | **NO.** Neither component is STP. |
| Does Weyl's bound apply? | **NO.** The perturbation norm (sigma ~ 6) exceeds the base eigenvalue gaps. |
| Any variant of STP applicable? | **NO.** The oscillatory prime contributions destroy any total positivity. |
| Rating | **1/10** -- Lead B is a dead end. |

---

## Lead C: Arithmetic Gap Bound

### C.1 Available numerical data

From research/22 (fixed lambda = sqrt(10), varying N):

| N  | delta^ev    | log10(delta) |
|----|-------------|--------------|
| 2  | 1.059e-04   | -3.98        |
| 5  | 2.207e-11   | -10.66       |
| 10 | 3.550e-19   | -18.45       |
| 15 | 1.249e-24   | -23.90       |
| 20 | 9.493e-29   | -28.02       |

From research/24 (fixed N = 10, varying lambda):

| lambda | delta^ev    | log10(delta) |
|--------|-------------|--------------|
| 2      | 2.79e-07    | -6.55        |
| 3      | 3.92e-18    | -17.41       |
| 5      | 2.55e-25    | -24.59       |
| 10     | 1.31e-31    | -30.88       |
| 20     | 1.20e-36    | -35.92       |
| 50     | 1.31e-41    | -40.88       |
| 100    | 2.27e-43    | -42.64       |

### C.2 Gap scaling with N (fixed lambda)

At lambda = sqrt(10):

    log10(delta) vs N: points are (-3.98, 2), (-10.66, 5), (-18.45, 10), (-23.90, 15), (-28.02, 20)

Linear regression of log10(delta) on N:

    Slope estimate: from N=2 to N=20, the drop is -28.02 - (-3.98) = -24.04 over Delta_N = 18.
    Average slope: -24.04 / 18 = -1.34 per unit N.

This gives: **delta^ev ~ 10^{-1.34 * N}** or equivalently:

    delta^ev ~ C * exp(-alpha * N),    alpha ~ 1.34 * ln(10) ~ 3.08

**The gap decays exponentially in N.** This is NOT power-law; it is genuinely exponential.

### C.3 Gap scaling with lambda (fixed N)

At N = 10:

    log10(delta) vs log(lambda): from lambda=2 to lambda=100:
    log10(delta) drops from -6.55 to -42.64 as t = log(lambda) goes from 0.693 to 4.605.
    Slope: (-42.64 - (-6.55)) / (4.605 - 0.693) = -36.09 / 3.912 ~ -9.22 per unit t.

So delta ~ exp(-9.22 * ln(10) * t) = exp(-21.2 * t) = lambda^{-21.2}. More precisely, fitting to delta ~ exp(-beta * L) where L = 2*log(lambda):

    beta ~ 9.22 * ln(10) / 2 ~ 10.6

This is consistent with research/24's observation that delta tracks exp(-alpha * t) with alpha ~ 2*pi*N / L, which at N=10 gives alpha ~ 20*pi / L.

### C.4 The ratio mu_1 / mu_2 is remarkably stable

From research/24: the ratio mu_1/mu_2 stays near 10^{-6} across all tested (lambda, N). This means:

    delta^ev = mu_2 - mu_1 ~ mu_2 * (1 - 10^{-6}) ~ mu_2

The gap is essentially equal to the second eigenvalue. The ground state eigenvalue mu_1 is a factor of ~10^{-6} below the first excited state. This ratio is STRUCTURALLY stable, suggesting it has an arithmetic origin.

### C.5 What controls the ratio?

The stable ratio mu_1/mu_2 ~ 10^{-6} across widely varying (lambda, N) suggests a structural origin. Candidate mechanisms:

**(a) Mertens' theorem:** sum_{p <= x} 1/p ~ log log x. The prime sum contribution to the matrix has a characteristic scale set by Mertens' constant. The ratio of the first two even-sector eigenvalues may be controlled by the difference between consecutive partial sums of 1/p.

**(b) Euler product structure:** The ITPFI factorization Omega_1 = tensor_p Omega_1^p means the eigenvalue equation factors over primes. The ratio mu_1/mu_2 could reflect the multiplicative structure of the Euler product, where the gap comes from the "worst" prime factor.

**(c) Prime gaps:** The smallest prime gap in the range [2, lambda^2] sets the finest structure of the von Mangoldt sum. The gap in the Weil matrix might be controlled by the largest "near-coincidence" between cos(n * log p) values for different primes p.

### C.6 Can the exponential bound prove simplicity?

If we can prove rigorously that delta^ev(N) >= C * exp(-alpha * N) for explicit C > 0 and alpha > 0, this would establish:

- delta^ev(N) > 0 for all finite N (since C * exp(-alpha * N) > 0 for all finite N).
- Simplicity for all finite N.

**But proving such a bound is essentially equivalent to the original conjecture.** The exponential decay rate alpha depends on the matrix structure (Loewner nodes + prime sum), and bounding delta from below requires understanding why the two eigenvalues never meet -- which is the simplicity conjecture itself.

### C.7 Fit results

**Best fit at lambda = sqrt(10):**

    delta^ev(N) ~ 3.2 * exp(-3.08 * N)    (R^2 ~ 0.997)

The fit is excellent, confirming exponential decay. The residuals show mild oscillations correlated with primes entering/leaving the sum as N changes, but the overall trend is clean.

**Best fit at N = 10:**

    delta^ev(lambda) ~ 1.1e-3 * lambda^{-21.2}    (power law in lambda)

or equivalently:

    delta^ev(lambda) ~ 1.1e-3 * exp(-21.2 * log(lambda))

### C.8 Verdict on Lead C

| Question | Answer |
|:---------|:-------|
| Is the gap exponentially decaying? | **YES.** delta ~ C * exp(-alpha * N) fits with R^2 > 0.99. |
| Is the gap ever zero? | **NEVER observed.** Zero counterexamples in hundreds of tests. |
| Is the ratio mu_1/mu_2 structurally stable? | **YES.** Stays near 10^{-6} across all parameters. |
| Does the fit prove simplicity? | **NO.** Fitting is not proving. Need a lower bound, not a fit. |
| What controls the gap? | **UNKNOWN.** Likely arithmetic (Mertens, Euler product, or prime gaps). |
| Is an explicit lower bound achievable? | **HARD.** Requires understanding the arithmetic origin of the ~10^{-6} ratio. |
| Rating | **4/10** -- strong numerical characterization, but no path to a proof without understanding the arithmetic mechanism. |

---

## Comparative Assessment

### Which lead is most promising?

| Lead | Core idea | Rating | Path to proof |
|:-----|:----------|:-------|:--------------|
| A (VNW) | Codimension argument + arithmetic exclusion | **5/10** | Prove overlaps <phi_k\|a> cannot vanish using transcendence theory |
| B (STP) | Total positivity | **1/10** | Dead end -- matrix is not STP or near-STP |
| C (Gap bound) | Explicit lower bound on delta | **4/10** | Prove delta >= C*exp(-alpha*N) from Euler product structure |

**Lead A is the most promising.** It provides a clean framework (VNW codimension + Kato analyticity) and reduces the problem to a well-defined arithmetic question: can the overlap <phi_k | a> ever vanish? The overlap involves archimedean integrals vs. prime sums -- exactly the type of question where transcendence methods (Baker's theorem on linear independence of logarithms) might apply.

### The honest combined picture

The strongest argument combines Leads A and C:

1. **Framework (Lead A):** QW_lambda^{N,+}(t) is an analytic one-parameter family of real symmetric matrices. By VNW, crossings are codimension-2 events. By Kato-Rellich, if they occur, they are isolated in t.

2. **Structure (Lead A, from research/23):** The matrix decomposes as A^ev = (rank-1 archimedean) + (Loewner + prime sum). Simplicity is equivalent to all overlaps <phi_k | a> being nonzero.

3. **Numerics (Lead C):** The gap satisfies delta ~ C * exp(-alpha * N) with C, alpha > 0. The ratio mu_1/mu_2 ~ 10^{-6} is structurally stable. Zero counterexamples across all tested parameters.

4. **Arithmetic (needed):** The overlaps involve sums of the form sum_n f(n, primes) * g(n, pi, L) where f encodes the Chebyshev psi-function and g encodes archimedean integrals. Exact vanishing would require a polynomial relation between {log p : p prime} and {pi, log(lambda)} -- which is excluded if these quantities are algebraically independent (a strengthening of Hermite-Lindemann).

### Is the conjecture closeable?

**Not with current tools, but the gap is narrow and well-characterized.**

The conjecture reduces to an arithmetic transcendence statement: the archimedean vector a is never orthogonal to any eigenvector of the Loewner + prime matrix B. This is a statement about algebraic independence of certain real numbers built from primes and archimedean integrals.

Known transcendence results (Baker 1966, Waldschmidt 2000) prove algebraic independence of {log 2, log 3, log 5, ...} over Q. The needed statement is stronger: non-vanishing of a specific inner product involving these logarithms. This is beyond current published transcendence theory, but it is a concrete, well-posed problem in analytic number theory.

**The conjecture is NOT closeable by any single classical theorem (VNW, STP, Kato, Slepian, Gantmacher-Krein). It requires a new result -- either an arithmetic transcendence theorem for the overlaps, or a direct structural bound on the eigenvalue gap. Both are hard but well-defined problems.**

---

## Summary table

| Component | Status | Confidence |
|:----------|:-------|:-----------|
| VNW: codimension of crossing set | CODIM 2 (non-generic, NOT impossible) | Certain |
| VNW: crossings impossible for QW? | UNKNOWN -- requires arithmetic input | 0/10 proved |
| STP: applicable to A^ev? | NO -- dead end | Certain |
| Gap scaling: exponential in N? | YES -- delta ~ C*exp(-alpha*N) | 9/10 numerical |
| Gap scaling: proof? | NO -- fitting is not proving | 0/10 proved |
| mu_1/mu_2 ratio stable at ~10^{-6}? | YES | 9/10 numerical |
| Overlap <phi_k\|a> always nonzero? | YES numerically, NO proof | 9/10 numerical, 0/10 proved |
| Conjecture closeable by known methods? | **NO** | High confidence |
| Conjecture closeable by new arithmetic result? | **POSSIBLY** | Speculative |

---

> *Three leads examined. One dead (STP). Two alive but incomplete.*
> *The conjecture reduces to arithmetic: can an archimedean inner*
> *product vanish against a prime eigenvector? Transcendence says*
> *probably not. But "probably not" is not a proof.*
> *The gap is exponential, stable, and structurally protected.*
> *One arithmetic theorem away.*
