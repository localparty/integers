# Proof: Q5-RIEMANN -- TGap Exponent = 2/(gamma_6 - gamma_5)

*Independent re-verification*
*Date: 2026-04-12*

---

## Claim

The TGap scaling exponent for 3-SAT (TGap ~ n^alpha) equals 2/(gamma_6 - gamma_5) = 0.430004273... where gamma_5, gamma_6 are the imaginary parts of the 5th and 6th non-trivial Riemann zeta zeros.

## Part (a): Riemann zero computation

Computed using `mpmath.zetazero()` at 120 decimal digits working precision.

| Quantity | Value (50 digits) |
|----------|-------------------|
| gamma_5  | 32.935061587739189690662368964074903488812715603517 |
| gamma_6  | 37.586178158825671257217763480705332821405597350831 |
| gamma_6 - gamma_5 | 4.6511165710864815665553945166304293325928817473138 |
| 2/(gamma_6 - gamma_5) | 0.43000427304551695718862473741375482116386159926961 |

Cross-check: the existing code `test_tgap_exponent_riemann.py` used hard-coded 30-digit values for gamma_5 and gamma_6. The mpmath.zetazero() computation agrees to all 30 digits, confirming the Riemann zero values.

Note on numbering: the original proof sketch stated "gamma_5 = 30.4249..., gamma_6 = 35.0762..." which does not match any standard Riemann zero table. The actual computation uses the correct standard numbering: gamma_5 = 32.935..., gamma_6 = 37.586..., consistent with mpmath and LMFDB. The proof sketch text had a typo.

## Part (b): Independent TGap measurement

**Methodology**: Generated 50 random 3-SAT instances at critical ratio m/n = 4.267 for each n. Brute-force enumerated all solutions. Tested all 61 non-projection idempotent ternary Boolean operations for polymorphism preservation.

| n  | m  | Median TGap | Mean TGap | Std  | SAT instances |
|----|-----|------------|-----------|------|---------------|
|  8 |  34 | 0.7377     | 0.4822    | 0.467 | 46/50        |
| 10 |  43 | 0.8115     | 0.5205    | 0.469 | 36/50        |
| 12 |  51 | 0.9836     | 0.6230    | 0.462 | 37/50        |
| 14 |  60 | 0.8689     | 0.5840    | 0.461 | 37/50        |
| 16 |  68 | 0.9836     | 0.7173    | 0.414 | 41/50        |

**Fit**: log(TGap) vs log(n) linear regression gives:

- alpha = 0.383 +/- 0.142
- R^2 = 0.709
- p-value = 0.074

**Honest assessment**: The scaling exponent is NOT well-determined from this data. The standard error (0.142) spans the range [0.24, 0.53], which includes the target 0.430 but also a wide band of alternatives. The fundamental problem is:

1. At critical ratio 4.267, most instances have very few solutions (median 2-3 across all n tested).
2. With so few solutions, almost no ternary operation preserves the solution set, saturating TGap near 1.0.
3. The scaling regime has not been reached at n = 8-16.

The fitted alpha = 0.383 is nominally 10.9% below the predicted 0.430, but within the 1-sigma confidence interval. The data does not contradict the claim, but it does not confirm it either.

## Part (c): Formula uniqueness search

Searched three formula families over first 15 Riemann zeros with 7 constants {1, 2, 3, 1/2, 1/pi, pi, log 2}:

- a/(gamma_i - gamma_j): 15*14*7 = 1470 formulas
- a*gamma_i/gamma_j: 15*14*7 = 1470 formulas
- a/(gamma_i + gamma_j): 15*15/2*7 = 840 formulas

**Total formulas tested: 3780**

**Matches within 0.01% of 2/(gamma_6 - gamma_5) = 0.430004273...**

| Rank | % deviation | Value | Formula |
|------|-------------|-------|---------|
| 1    | 0.000000%   | 0.430004273046 | 2/(gamma_6 - gamma_5) |

No other formula matches within 0.01%.

The next-closest formula from the broader search (results_tgap_exponent.md) is `gamma_14/gamma_12 * 1/sqrt(2*pi)` at 0.0145% -- an order of magnitude worse and involving an unrelated constant.

**Conclusion on uniqueness**: Within the tested formula families, 2/(gamma_6 - gamma_5) is unique at the 0.01% level. The runner-up is 14.5x worse in relative precision.

## Comparison with original

The original test (`test_tgap_exponent_riemann.py`) searched ~5000 formula structures across 8 families and found 398 matches in [0.41, 0.45]. This re-verification confirms:

1. The Riemann zero computation is correct (independently reproduced via mpmath.zetazero to 100 digits).
2. The formula uniqueness holds: 2/(gamma_6 - gamma_5) is the only formula within 0.01% of 0.430004273.
3. The proof sketch contained a typo in the stated values of gamma_5 and gamma_6, but the actual computation was correct.

## Verdict: WEAKENED

**The Riemann zero formula 2/(gamma_6 - gamma_5) = 0.430004273... is mathematically precise and unique among simple Riemann-zero formulas.**

However, the independent TGap measurement cannot confirm the exponent to the claimed 0.001% precision. The brute-force measurement at n = 8-16 gives alpha = 0.38 +/- 0.14, which is consistent with 0.43 but far too noisy to distinguish it from other values. The claimed 0.001% match between alpha_measured and alpha_formula rests entirely on prior literature values for the 3-SAT scaling exponent (alpha ~ 0.43 from larger-scale computational studies), not on this small-n direct measurement.

**Status**: The formula-side claim (uniqueness of 2/(gamma_6 - gamma_5) at 0.01%) is CONFIRMED. The measurement-side claim (alpha = 0.43 to 0.001%) is NOT INDEPENDENTLY VERIFIED by this small-n computation and relies on external numerical evidence.

---
*Generated by reverify_q5_riemann.py*
*Verification code: paper28-pvnp/code/reverify_q5_riemann.py*
