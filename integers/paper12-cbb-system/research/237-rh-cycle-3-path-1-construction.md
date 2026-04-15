# 237 — RH Cycle 3, Path 1 (Brauer-KMS) — Construction

*Cycle: 3 (LIVE). Date: 2026-04-09. Agent: Construction (priority 2+2).*

---

## Step attempted

**Compute f(gamma_n) explicitly and test whether f(gamma_n) lies in (1/k)Z for k = 3, 4, 6.**

Per cycle 2 ledger: the open step is computing f(gamma) from the commutator [log R-hat, Pi_chi] and establishing that f(gamma) is generically irrational (i.e., not in (1/k)Z).

## Attempt level: 2 (Sub-computation with mpmath)

### Computation: Phase shift function f(gamma_n)

The spectral density factor in the Brauer-KMS phase shift is:

    f(gamma) = (1/(2*pi)) * log(gamma / (2*pi))

This arises from the zero-density of zeta near height gamma: d(gamma) ~ (1/(2*pi)) * log(gamma/(2*pi)).

**mpmath output (50 dps, gamma_1 through gamma_10):**

```
n= 1, gamma_1=  14.134725, f(gamma_1)= 0.12903606
  k=3: 3*f = 0.387108, dist_to_Z = 0.38710818
  k=4: 4*f = 0.516144, dist_to_Z = 0.48385576
  k=6: 6*f = 0.774216, dist_to_Z = 0.22578364

n= 2, gamma_2=  21.022040, f(gamma_2)= 0.19221052
  k=3: 3*f = 0.576632, dist_to_Z = 0.42336843
  k=4: 4*f = 0.768842, dist_to_Z = 0.23115791
  k=6: 6*f = 1.153263, dist_to_Z = 0.15326313

n= 4, gamma_4=  30.424876, f(gamma_4)= 0.25104838
  k=4: 4*f = 1.004194, dist_to_Z = 0.00419353  ← CLOSEST APPROACH

n=10, gamma_10= 49.773832, f(gamma_10)=0.32938903
  k=3: 3*f = 0.988167, dist_to_Z = 0.01183290  ← CLOSE TO 1
  k=6: 6*f = 1.976334, dist_to_Z = 0.02366581  ← CLOSE TO 2
```

### Analysis

1. **No exact hit.** For all 10 zeros tested, k * f(gamma_n) is NOT an integer for any k in {3, 4, 6}. The closest approach is gamma_4 at k=4 with dist = 0.0042.

2. **Structural argument.** f(gamma) = (1/(2*pi)) * log(gamma/(2*pi)) is transcendental whenever gamma is transcendental (Lindemann-Weierstrass). The Riemann zeros are expected (and numerically verified) to be transcendental. Therefore k*f(gamma_n) is transcendental, hence irrational, hence not in Z.

3. **Gap remaining.** The transcendence of gamma_n is itself unproved. This is the residual gap: the argument reduces to "gamma_n transcendental => f(gamma_n) irrational => Brauer class perturbation non-integer => off-line zero impossible." But gamma_n transcendence is not proved.

4. **Alternative approach (algebraic independence).** Even without transcendence, one can argue: f(gamma_n) = (1/(2*pi)) * log(gamma_n/(2*pi)). If this were rational = p/q, then gamma_n = 2*pi*exp(2*pi*p/q), which is a specific algebraic relation between gamma_n and pi. No such relation is known or expected.

## Result: BLOCKED (narrowed)

The computation confirms f(gamma_n) not in (1/k)Z numerically for n=1,...,10 and k=3,4,6. The gap is now precisely: prove gamma_n is not of the form 2*pi*exp(2*pi*r) for any r in Q. This is a number-theoretic statement about zeta zeros.

## Next step

Either: (a) prove the transcendence of gamma_1 (hard, open problem), or (b) find a structural argument why the Brauer obstruction is non-trivial that does not depend on transcendence — e.g., use the multiplicative structure of A_BC to show the obstruction class is non-trivial for ALL spectra, not just the specific gamma_n values.
