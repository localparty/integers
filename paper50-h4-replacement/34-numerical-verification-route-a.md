## §34 — Numerical Verification of Route A

*Transseries computation at specific loop orders. Borel-sum estimates. Lattice QCD cross-check on Schwinger functions. The numerical programme that accompanies Route A's analytic construction.*

---

## 34.1. The verification target

Route A's analytic construction produces a lateral Borel resummation of the perturbative Yang-Mills series $S_n^{\mathrm{PT}}(g)$, claimed to equal the non-perturbative Schwinger functions $S_n$ at short distances. Verification of this claim requires *numerical corroboration*: the resummed series, computed at specific loop orders, must match the non-perturbative Schwinger functions, computed by lattice QCD, at the same short-distance configurations.

The verification has three components:

**V-A1 (Transseries computation).** Compute the first $L$ transseries coefficients of $S_2^{\mathrm{PT}}$ (two-point Schwinger function) for $L$ up to at least 4 (four-loop order). Each coefficient is a specific integral over Feynman-diagram momentum space, computed via dimensional regularization.

**V-A2 (Borel-sum estimate).** Construct the Borel transform $B(\zeta)$ of the series, identify its singularities in the complex $\zeta$-plane (IR renormalons at $\zeta_k = 2\pi k / \beta_0$, UV renormalons at negative locations), and perform the lateral Borel sum along a contour $\theta = \pm \epsilon$ avoiding the singularities. The result is a family of analytic functions $S_2^{[\pm]}(g)$ whose difference on the positive real axis is the non-perturbative ambiguity.

**V-A3 (Lattice QCD cross-check).** Compute the two-point Schwinger function $S_2(x, y)$ on a fine lattice for short separations $|x - y|$, using state-of-the-art lattice QCD with $\mathcal{O}(a)$ improvement. Compare to $S_2^{[\pm]}(g)$ at corresponding $\mu = 1/|x - y|$ scales. The match should be within the combined lattice statistical error and perturbative truncation error.

All three components together verify Route A's analytic claim at the numerical level.

---

## 34.2. Transseries computation (V-A1)

The perturbative coefficients of $S_2^{\mathrm{PT}}$ are computed by Feynman diagrams. At one loop, the coefficient is the standard gluon-vacuum-polarization result. At two loops, it involves the two-loop beta-function coefficient $\beta_1$ and specific scalar integrals. At three and four loops, it requires multi-loop master integrals.

**Tools.** Modern tools (FORM, Mathematica + HepMath, diagrammatic automation via qgraf + form) can compute four-loop coefficients for specific observables in pure YM. For SU(3), the four-loop beta function is known (van Ritbergen, Vermaseren, Larin 1997; Herzog et al. 2017). Five-loop is available for specific gauge-invariant observables (Baikov, Chetyrkin, Kühn 2017).

**Expected output for Route A.** A table of coefficients $\{a_k\}$ for $k = 0, 1, 2, 3, 4$ (possibly 5), with known rational and transcendental constants (zeta values, multiple zeta values) appearing with known exponents. The coefficients exhibit the factorial growth $a_k \sim k! / (\beta_0)^k$ predicted by Lipatov 1977 — this is the factorial growth that signals IR renormalons.

**Transseries structure.** Beyond the perturbative coefficients $\{a_k\}$, the transseries includes non-perturbative sectors indexed by "instanton number" $n$ (or more precisely, by the action of the saddle point at which the sector lives):

$$S_2^{\mathrm{trans}}(g) = \sum_{n = 0}^{\infty} c_n e^{-S_n / g^2} g^{\gamma_n} \sum_{k \geq 0} a_k^{(n)} g^{2k},$$

where $S_n$ is the action of the $n$-th sector's saddle, $\gamma_n$ is its anomalous dimension, and $\{a_k^{(n)}\}$ are the sector-$n$ coefficients. Route A's full transseries computation must determine the $c_n, S_n, \gamma_n, a_k^{(n)}$ for enough sectors to produce the match.

---

## 34.3. Borel-sum estimate (V-A2)

The Borel transform of the perturbative sector is

$$B(\zeta) = \sum_{k \geq 0} \frac{a_k}{k!} \zeta^k,$$

a power series with finite radius of convergence (precisely the distance to the nearest singularity, which for pure YM is the first IR renormalon at $\zeta_1 = 2\pi / \beta_0$).

**Singularities.** IR renormalons at $\zeta_k = 2\pi k / \beta_0$ for $k = 1, 2, 3, \dots$ UV renormalons at negative locations $\zeta_k = -2\pi k / \beta_0$. Instanton-antiinstanton poles at specific locations computed via the dilute-instanton-gas approximation.

**Lateral Borel sum.** The integral

$$S_2^{[\pm]}(g) = \int_0^{\infty e^{\pm i \epsilon}} B(\zeta) e^{-\zeta / g^2} d\zeta$$

is performed along a contour tilted by $\pm \epsilon$ from the positive real axis, avoiding the real-axis singularities. The result is a complex function of $g$ whose imaginary part is a Stokes discontinuity at $\epsilon = 0$. The real part is the resummation; the imaginary part signals a non-perturbative sector.

**Numerical method.** Truncate the Borel series at order $N$, compute the finite-$N$ Borel transform, and perform the contour integral numerically. The truncation error is bounded by the size of the $(N+1)$-th Borel coefficient times the suppression factor $e^{-\zeta_1 / g^2}$. For $g$ in the asymptotic-freedom regime ($g \lesssim 0.5$), the truncation converges rapidly.

**Expected output.** A table of $S_2^{[\pm]}(g)$ values for $g$ ranging over $(0.05, 0.5)$, with error bars from truncation. The values should match the lattice-computed $S_2(|x-y|)$ at $|x-y| = 1/\mu$ with $g = g(\mu)$.

---

## 34.4. Lattice QCD cross-check (V-A3)

Lattice QCD computes Schwinger functions non-perturbatively. For the verification of Route A, the relevant lattice observables are:

**Short-distance two-point function.** The correlator $\langle \mathrm{Tr} F^2(x) \mathrm{Tr} F^2(y) \rangle$ at pairwise separation $|x - y| \in (0.01, 0.1)$ fm, computed on a fine lattice ($a \leq 0.02$ fm, $L \geq 2$ fm, $\sim 10^6$ configurations for statistical control).

**Running coupling.** The scheme-matched running coupling $g(\mu)$ from the gradient-flow (Lüscher 2010) or the SF-coupling (Lüscher-Weisz-Wolff 1991), extrapolated to the continuum limit.

**State-of-the-art.** As of 2026, lattice QCD computations of gauge-invariant two-point functions at $|x - y| \sim 0.05$ fm with ~1% statistical accuracy are achievable (PACS-CS, RBC-UKQCD, FLAG averages). The computational cost is $\mathcal{O}(10^5)$ core-hours on modern supercomputers per observable per lattice spacing.

**Comparison protocol.** For each lattice configuration, compute $S_2^{\mathrm{lattice}}(|x-y|)$. Match against $S_2^{[\pm]}(g(\mu = 1/|x-y|))$. The match should hold at the level of combined errors: lattice statistical (~1%), lattice discretization (~1% at $a = 0.02$ fm), continuum extrapolation residual (~0.5%), perturbative truncation at four loops (~5% at $g = 0.3$, smaller at higher $\mu$).

**Expected match quality.** At short distances ($|x-y| \leq 0.05$ fm), the match should be within ~5-7% combined error. If Route A's analytic construction is correct, the match is within error. If Route A has a subtle gap (e.g., missed a sub-leading transseries sector), the match is worse than expected, signaling a repair target.

---

## 34.5. Cross-check against Route B

Route A's numerical verification can be cross-checked against Route B's L-function values. Specifically, the Wilson-loop L-function $L(s, W)$ at specific $s$ values (e.g., $s = 1, 2, 1/2$) has a numerical value that Route B predicts via Kim-Sarnak-Shahidi methods. Route A's Borel-sum estimate of the Wilson-loop two-point function should be consistent with this L-function value under the standard Mellin-transform relation.

Consistency between Routes A and B at the numerical level is an additional validation beyond V-A3's lattice match. Inconsistency flags a gap in one of the two routes, driving author-team repair.

---

## 34.6. Numerical infrastructure and cost

The numerical verification is computationally expensive but feasible with current resources.

- **Transseries computation:** ~100 CPU-days on a modest cluster (1000 cores for 2-3 months), using existing tools (FORM, qgraf).
- **Borel-sum estimate:** ~10 CPU-days of high-precision arithmetic (mpmath in Python, or Arb).
- **Lattice QCD cross-check:** ~$10^5$ core-hours on a DOE or RIKEN supercomputer, or partnership with an existing lattice collaboration (PACS-CS, RBC-UKQCD, BMW).

The programme's partnership strategy (existing lattice collaborations have overlapping research interests) reduces the direct computational cost for the programme to a small fraction of the total. The partnership strategy makes the numerical verification feasible within Paper 50's horizon.

---

## 34.7. Publication of V-A results

The numerical verification is not a separate paper — it is an appendix or supplementary section of Paper 50 if Route A is the primary closure. The verification section includes:

- The transseries coefficients up to the loop order computed.
- The Borel-sum estimates at representative $g$ values.
- The lattice comparison data with error bars.
- A discussion of match quality and any residual discrepancies.

If Route A is not the primary closure (Routes B or C close first), V-A is documented as a verification of Route A's partial claims, supporting Route A's eventual closure as an alternative verification (§26).

---

## 34.8. Summary

Route A's numerical verification has three components: transseries computation at 4-5 loops (V-A1), Borel-sum estimate with lateral integration (V-A2), and lattice QCD cross-check at short distances (V-A3). The expected match quality is ~5-7% at short distances, within combined errors. Cross-check against Route B's L-function values provides additional validation. The numerical infrastructure is feasible with current lattice-QCD resources and programme partnerships. The verification is published as part of Paper 50 when Route A is primary, or as alternative-verification support otherwise.

---

*Paper 50 §34. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
