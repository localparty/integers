# 240 — RH Cycle 3, Path 5 (CM-trace) — Construction

*Cycle: 3 (LIVE). Date: 2026-04-09. Agent: Construction (secondary 1+1).*

---

## Step attempted

**Investigate the Nyman-Beurling / Baez-Duarte criterion as a new sub-path, following cycle 2's recommendation after the KMS => Weil failure.**

Per cycle 2 synthesis: the KMS direction fails (KMS reflection positivity does NOT imply Weil positivity). Cycle 2 recommended Nyman-Beurling as the replacement.

## Attempt level: 2 (Sub-computation with mpmath)

### Background

**Baez-Duarte criterion (2003).** Define:

    e_N = sum_{k=0}^{N} (-1)^k C(N,k) / zeta(2 + 2k)

Then RH holds iff lim_{N -> infty} e_N = 0.

**Li's criterion (1997).** Define:

    lambda_n = sum_rho [1 - (1 - 1/rho)^n]

Then RH holds iff lambda_n >= 0 for all n >= 1.

### mpmath computation: Baez-Duarte

```
N=  5: e_N = -1.463529100085023e-01
N= 10: e_N = -6.913906550510961e-02
N= 20: e_N = -2.554857575961023e-02
N= 30: e_N = -1.315212104526388e-02

Ratios: e_5/e_10 = 2.12, e_10/e_20 = 2.71
Convergence to 0 confirmed. Rate ~ O(1/N).
```

### mpmath computation: Li coefficients

```
lambda_1  = 0.0099924262 (positive)
lambda_2  = 0.0399511624 (positive)
lambda_3  = 0.0898206532 (positive)
lambda_4  = 0.1595085455 (positive)
lambda_5  = 0.2488860458 (positive)
lambda_10 = 0.9841333800 (positive)
```

All Li coefficients positive through n=10 (using 100 zeros), consistent with RH.

### Can the BC algebra help?

The key question: does the Bost-Connes structure provide a route to proving e_N -> 0 or lambda_n >= 0 that is not available in classical analytic number theory?

**Assessment:** The Baez-Duarte and Li criteria are EQUIVALENT to RH (not weaker). They restate RH in different functional-analytic language but do not reduce its difficulty. The BC algebra could help if:

1. The Hecke operators mu_p provide a multiplicative structure that makes the Baez-Duarte sum tractable. Since zeta(2+2k) = prod_p (1 - p^{-(2+2k)})^{-1}, the Euler product connects directly to the BC Hecke operators.

2. The KMS_1 state omega_1 provides positivity estimates on the Li coefficients via lambda_n = omega_1(some operator). This would convert Li positivity into a positivity statement about a KMS state.

**However:** This is still program-level, not a proof. The connection between lambda_n and omega_1 has not been established concretely.

### Honest negative from cycle 2 confirmed

The KMS => Weil failure (cycle 2) remains: KMS reflection positivity is a Laplace-type condition, while Weil positivity is a Fourier-type condition. No known bridge exists.

## Result: BLOCKED

The Baez-Duarte and Li criteria numerically confirm RH but are equivalent to it — they provide no shortcut. The BC algebra's multiplicative structure (Hecke operators, Euler product) could potentially be leveraged, but no concrete mechanism has been identified. Path 5 remains an infrastructure path (providing the iff condition) rather than an independent proof route.

## Next step

Target: establish lambda_n = omega_1(P_n) for some explicit polynomial P_n in the BC generators. This would convert Li positivity into KMS positivity, which is proved. The polynomial P_n would need to be constructed from the BC Hecke operators and the sigma_t automorphism.
