# Research 54 -- N2: Pseudo-Random Eigenvalue Gaps via Prime Equidistribution

*Date: 2026-04-09. Structure: DEVELOPMENT (A) then ADVERSARIAL (B).*
*Depends on: ledger (Step 10 wall), research/48 (fatal gap at Step 10), research/52 (I2 eigenvalue estimates)*

---

## PART A: Development

### 1. The Tao-Vu / Nguyen-Vu framework

Tao-Vu (Annals of Probability, 2015) and Nguyen-Vu (Annals of Probability, 2017): let A be an n x n deterministic symmetric matrix and X an n x n random symmetric matrix with iid entries (up to symmetry) satisfying subgaussian tail bounds and the anti-concentration property P(|xi - t| <= eps) <= C eps for all t. Then with probability at least 1 - n^{-D}, the eigenvalue gaps satisfy |lambda_i - lambda_{i+1}| >= n^{-C} for all i, where C, D > 0 are absolute constants. The key mechanism: random perturbations prevent eigenvalue collisions because no single direction in eigenspace is favored. The anti-concentration condition ensures the perturbation "spreads" across all spectral directions.

### 2. QW^N as base-plus-perturbation

Write QW^N = QW^0 + sum_{p <= P_N} alpha_p v_p v_p^T, where QW^0 is the archimedean contribution, alpha_p = (log p)/sqrt{p}, and v_p is the prime vector with entries v_p[i] = cos(x_i log p) at the Chebyshev nodes {x_i}_{i=1}^n. Each rank-one term alpha_p v_p v_p^T is deterministic. But the collection {v_p : p prime} has pseudo-random properties inherited from the distribution of primes.

### 3. Equidistribution of prime vectors

For fixed Chebyshev nodes {x_i} and varying prime p: each entry v_p[i] = cos(x_i log p). By Weyl's equidistribution theorem, the sequence {x_i log p mod 2pi}_{p prime} is equidistributed in [0, 2pi) for each fixed i, because x_i log p / (2pi) has irrationally-spaced increments along primes (log p_{k+1} - log p_k ~ 1/p_k by PNT). Therefore v_p[i] equidistributes in [-1, 1] with the arcsine measure. The pairwise correlation v_p[i] v_p[j] = (1/2)[cos((x_i - x_j) log p) + cos((x_i + x_j) log p)]. Each cosine term equidistributes to mean zero, so the off-diagonal correlations average to zero. The Erdos-Turan inequality gives quantitative discrepancy: D_P = O(1/log P) for primes up to P, where D_P measures deviation from equidistribution.

### 4. Anti-concentration from equidistribution

The Tao-Vu mechanism requires anti-concentration: the perturbation should not concentrate in any single spectral direction. For our prime vectors, this means: for any unit vector u in R^n, the projections <v_p, u> = sum_i u_i cos(x_i log p) should not systematically concentrate near a single value. Since <v_p, u> is a trigonometric polynomial in log p with coefficients u_i, Weyl equidistribution gives that these projections equidistribute (with the distribution of the trig polynomial evaluated at equidistributed points). Provided u is not a coordinate vector (which would reduce <v_p, u> to a single cosine), the projection has a continuous distribution function with bounded density. This is the anti-concentration property.

### 5. The pseudo-random gap conjecture

If the prime vectors {v_p} behave sufficiently like random vectors with respect to anti-concentration, then the eigenvalue gaps of QW^N should satisfy a polynomial lower bound: |lambda_k^N - lambda_{k+1}^N| >= N^{-C} for some absolute C > 0 and all k. This bound would be UNIFORM in N (not decaying exponentially). Step 10 requires exactly this: a gap bound that does not collapse as N -> infinity. The pseudo-random structure would provide the "arithmetic repulsion" that the ledger identifies as equivalent to the Connes 25-year obstacle.

---

## PART B: Adversarial

### 6. Attack: Tao-Vu axioms are not met

Tao-Vu requires the perturbation entries to be RANDOM with specific distributional properties: (i) independence of entries, (ii) subgaussian tails, (iii) anti-concentration with quantitative constants. The prime vectors are deterministic. Equidistribution gives STATISTICAL properties that resemble randomness, but the Tao-Vu proof uses probabilistic tools (epsilon-net arguments, union bounds over subspaces) that require genuine randomness at a technical level. No published extension of Tao-Vu applies to deterministic sequences with equidistribution properties. The gap between "statistically random-looking" and "random" is precisely where number theory lives, and closing it for eigenvalue problems is not a soft step.

**Severity: HIGH.** The analogy is suggestive but the proof technology does not transfer. A "deterministic Tao-Vu" theorem would be a major new result in random matrix theory.

### 7. Attack: structured correlations in prime vectors

All prime vectors share the form cos(x_i log p). This means: (a) the vectors live on a low-dimensional manifold in R^n parametrized by the single variable log p, (b) nearby primes (p, q with |p-q| small) give highly correlated vectors (since log p ~ log q), (c) the rank-one perturbations alpha_p v_p v_p^T have a specific algebraic structure (outer products of evaluations of a SINGLE trigonometric function at different frequencies). True random matrices have entries that are structurally independent. The prime vectors have entries that are all cosines of the SAME variable x_i scaled by the SAME log p. This coherence could create systematic spectral alignment -- eigenvectors of QW^N might align with specific trigonometric directions, causing gaps to close along those directions even as generic gaps remain open.

**Severity: HIGH.** The one-parameter family structure (all vectors are cos(x_i * t) evaluated at t = log p) is a strong constraint that random matrix theory does not account for.

### 8. Attack: equidistribution is average-case, not worst-case

Equidistribution guarantees that MOST primes contribute well-behaved perturbations. But eigenvalue gaps are controlled by the WORST prime, not the average prime. A single prime p_bad where v_{p_bad} nearly aligns with the gap between two eigenvalue branches could close that gap, regardless of how well-behaved all other primes are. The Erdos-Turan discrepancy O(1/log P) controls the fraction of bad primes (it is small), but does not exclude their existence. For Step 10, we need |lambda_k^N - lambda_{k+1}^N| > 0 for ALL N, which requires ALL primes to be non-catastrophic. One exceptional prime suffices to kill the gap.

**Severity: MODERATE-HIGH.** Quantitative equidistribution bounds the NUMBER of bad primes but not their EFFECT. A single bad prime contributing a large rank-one perturbation in the wrong direction could close a spectral gap that took many good primes to open.

### 9. Quantitative path: Erdos-Turan with explicit constants

The Erdos-Turan inequality with M exponential sum terms gives discrepancy D_P <= C(1/M + (1/pi(P)) sum_{m=1}^M (1/m) |sum_{p<=P} e^{2pi i m x_j log p}|). The inner exponential sums are related to prime number theorem in arithmetic progressions and the distribution of log p modulo 1. Vinogradov-type estimates give |sum_{p<=P} e^{i t log p}| << P / (log P)^A for any fixed A, provided t is bounded. This could yield an EFFECTIVE discrepancy bound, and from it an effective anti-concentration estimate. But translating effective anti-concentration into effective eigenvalue gap bounds requires the full Tao-Vu machinery, which (per Attack 6) assumes randomness. The quantitative Erdos-Turan bound is useful context but does not bridge the deterministic-to-random gap.

**Severity of remaining gap: HIGH.** The number theory is available; the random matrix bridge is not.

---

## VERDICT

**Feasibility: 4/10.** Genuinely new direction with a clear mechanism (pseudo-random anti-concentration from prime equidistribution could provide arithmetic eigenvalue repulsion). The equidistribution of prime vectors is a REAL phenomenon backed by Weyl + Erdos-Turan + Vinogradov. The connection to Tao-Vu eigenvalue gap theory is conceptually compelling.

**But:** No existing theorem covers deterministic pseudo-random perturbations (Attack 6). The structured one-parameter family of prime vectors is far from the iid assumption (Attack 7). Worst-case vs average-case is a serious obstacle (Attack 8). Closing any of these would constitute original contributions to random matrix theory, not routine applications.

**What would advance this:** (a) A "deterministic Tao-Vu" theorem for perturbations satisfying quantitative equidistribution and anti-concentration, without requiring genuine randomness. (b) Explicit computation showing that the one-parameter structure cos(x_i log p) does NOT create systematic spectral alignment for QW^N. (c) A hybrid argument using Erdos-Turan to handle most primes probabilistically, combined with explicit spectral computation for the finitely many potentially bad primes (echoing the Cartwright counting argument from Steps 6-7).

**Confidence:** 4/10 that this direction can close Step 10 within a dedicated research programme. 7/10 that the equidistribution observation is mathematically correct and relevant. 2/10 that existing tools suffice without a new deterministic RMT result.

**Recommendation:** Open as N2 at 4/10. The pseudo-random angle is the first proposed mechanism for WHERE the uniform gap bound might come from. Worth a dedicated cycle to test whether the one-parameter structure (Attack 7) is fatal or manageable. Priority: check whether cos(x_i log p) vectors for consecutive primes can systematically align with eigenvalue gap directions of QW^N.
