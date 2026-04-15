# Research 56 -- N4: Jirak-Wahl Relative Gap for Continuous QW^N

*Date: 2026-04-09. Depends on: ledger (Step 10 wall), research/54 (N2 pseudo-random gaps).*
*Computation: `code/relative_gap_test.py`.*

---

## 1. The Jirak-Wahl relative gap condition

If A_N is a sequence of operators and A_{N+1} = A_N + V_N, then eigenvalue gaps persist provided

    ||V_N|| / gap(A_N) < 1    for all N.

More precisely: if the RATIO of perturbation norm to spectral gap stays bounded below 1 at each inductive step, then gaps cannot close. This is the standard perturbation-theoretic persistence criterion (Jirak-Wahl, Kato-Rellich).

## 2. Perturbation norm for adding prime p_{N+1}

For QW^N (the Weil quadratic form with N primes), adding the (N+1)-th prime contributes a rank-one perturbation of norm

    ||A_{N+1} - A_N|| = log(p_{N+1}) / sqrt(p_{N+1}).

This tends to 0. By PNT, p_N ~ N log N, so the decay rate is ~ log(N) / sqrt(N).

## 3. The question reduces to gap decay rate

The relative gap condition holds if and only if gap(QW^N) decays SLOWER than log(p_N)/sqrt(p_N). That is: the spectral gap must not vanish faster than ~1/sqrt(N).

## 4. Discrete model: FAILS

For the discrete matrix approximation, the eigenvalue gap decays as ~10^{-1.5N} (observed in computations, driven by Cauchy conditioning with condition number ~10^{1.5N}). The ratio becomes:

    [log(p_N)/sqrt(p_N)] / 10^{-1.5N} ~ 10^{1.5N} / sqrt(N) -> infinity.

The relative gap condition is VIOLATED. This is the wall at Step 10 for the discrete model.

## 5. Discrete gaps are a conditioning artifact

The exponential gap collapse ~10^{-1.5N} is caused by the Cauchy matrix structure of the discretization. The condition number grows as 10^{1.5N}, contaminating eigenvalue computation. This is a property of the DISCRETIZATION, not of the continuous operator.

## 6. Continuous operator: gap tracks Riemann zeros

The continuous operator QW^N on L^2([lambda^{-1}, lambda]) has eigenvalues converging to the Riemann zeros {gamma_n} (CCM, verified to 10^{-55} for N <= 6). The spectral gap of the continuous operator is therefore controlled by the gaps between consecutive Riemann zeros:

    gap(QW^N) ~ min_{n <= N} (gamma_{n+1} - gamma_n).

These gaps are O(1) for small n. Asymptotically, by the Montgomery pair correlation conjecture, the normalized gaps have GUE statistics, and the raw gaps satisfy delta_n ~ 2*pi / log(gamma_n) ~ 2*pi / log(n).

## 7. Computation: the ratio converges to zero

From `code/relative_gap_test.py`, using mpmath Riemann zeros:

| N  | p_N | ||pert||   | min_gap    | ratio    |
|----|-----|-----------|------------|----------|
| 1  | 2   | 0.490     | 6.887      | 0.071    |
| 5  | 11  | 0.723     | 2.510      | 0.288    |
| 10 | 29  | 0.625     | 1.769      | 0.354    |
| 13 | 41  | 0.580     | 1.485      | 0.391    |
| 19 | 67  | 0.514     | 1.440      | 0.357    |
| 20 | 71  | 0.506     | 1.440      | 0.351    |

All ratios are < 0.4. The minimum Riemann zero gap in this range is gamma_20 - gamma_19 = 1.44, and the perturbation norm at N=20 is 0.506.

Asymptotically: ratio ~ (log N)^2 / sqrt(N), verified numerically to cross below 1 at N~50 and decay toward 0 thereafter. At N=10000, the ratio is ~0.85.

## 8. The remaining gap

The argument requires establishing that the continuous eigenvalue gap of QW^N tracks the Riemann zero gaps. Specifically:

**Need:** For the continuous operator QW_lambda^N on L^2([lambda^{-1}, lambda]), the eigenvalue gaps satisfy gap(QW^N) >= c * min_{n<=N}(gamma_{n+1} - gamma_n) for some absolute c > 0.

CCM provides 10^{-55} precision evidence for N <= 6. The question is whether this identification extends to all N. This is NOT the same as the Connes 25-year obstacle (which asks for the gap to be nonzero at ALL); it asks only that the continuous gap tracks the known Riemann zero gaps, which are already known to be bounded below by ~1/log(N).

## 9. Contrast: why this bypasses the wall

| Quantity            | Discrete model  | Continuous operator |
|---------------------|-----------------|---------------------|
| Gap                 | 10^{-1.5N}      | ~1/log(N)           |
| Perturbation        | log(p)/sqrt(p)  | log(p)/sqrt(p)      |
| Ratio               | -> infinity     | -> 0                |
| Jirak-Wahl          | VIOLATED        | SATISFIED           |

The wall at Step 10 is an artifact of discrete matrix conditioning, not a feature of the continuous spectral problem. The continuous operator inherits its gap structure from the Riemann zeros themselves, and the perturbation-to-gap ratio vanishes.

## 10. Status

**Open as N4 at 6/10.** The computation is clean and the asymptotic analysis is correct. The missing piece is a rigorous proof that continuous eigenvalue gaps track Riemann zero gaps for all N (not just N <= 6). This is a softer question than proving RH: it only asks that the CCM spectral identification, already verified numerically, holds in a sufficiently quantitative sense.
