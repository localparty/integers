# OC-2 Status: Blocked by Theorem U

**Date:** April 8, 2026

---

## The Question

Open Calculation 2 (OC-2) asks: what is the absolute scale of r_2 (the
S^2 compactification radius)? Equivalently: what is M_KK = 1/r_2, the
Kaluza-Klein scale that determines the Higgs mass?

This was identified as a Tier 1 target — a concrete computation expected
to take 1-2 sessions.

## What We Found

OC-2 is not a missing computation. It is a fundamental physics gap.

### The Chain (All Derived)

| Step | Equation | Status |
|------|----------|--------|
| 1 | c_0 = 1/42 (G_2 torsion, FKMS 1997) | Computed |
| 2 | cR = (64 pi^5 / (126 l_{11}^3)) x R | Derived |
| 3 | r_3^2 = n_1 / (2 cR) = 9 / (2 cR) | Derived (F-flatness) |
| 4 | r_2 / r_3 = sqrt(3)/2 | Derived (GUT condition) |
| 5 | n_2 / n_1 = -17/9 | Derived (flux quantization) |
| 6 | M_Pl^2 = M_{11}^9 x Vol_7 | Physical law |

### The Algebraic Closure (Theorem U)

Substituting Steps 2-5 into Step 6, all internal geometry cancels:

    R_bare = (63 n_1)^{3/2} / (128 pi^{11/2} M_Pl)

Numerically: R_bare ~ 0.975 l_P ~ 1.6 x 10^{-35} m.

The system of equations is **algebraically degenerate**: l_{11} (the 11D
Planck length) drops out of the combined system. The only solution is
R ~ l_P, not R ~ 10 um. The ratio R_obs / R_bare ~ 6.4 x 10^{29}
cannot be bridged by perturbative physics.

### What This Means

The absolute scale of r_2 requires knowing R. Since R is fixed by dark
energy matching (R_obs = 10.1 um), M_KK is determined as a function
of R — but R itself is not derived from first principles.

| Aspect | Status |
|--------|--------|
| Ratio r_2/r_3 = sqrt(3)/2 | DERIVED (topological) |
| Functional form M_KK proportional to R^{1/2} | DERIVED |
| Absolute value of r_2 | BLOCKED (Theorem U) |
| M_KK ~ 1-2.5 TeV | CONSISTENT (given R_obs), not predicted |

## Why This Is Not a Failure

Theorem U is not a bug. It is a feature.

1. **It precisely isolates the CC problem.** The cosmological constant
   problem — why is the vacuum energy 10^{120} times smaller than the
   Planck scale? — is reduced to one geometric question: why is R ~ 10 um
   instead of R ~ l_P?

2. **All other observables are R-independent.** The gauge group, coupling
   ratios, flux integers, neutrino mass ratios, spectral indices —
   everything except the absolute energy scale — is determined without
   knowing R.

3. **It points toward non-perturbative physics.** Theorem U proves that
   no perturbative M-theory calculation can derive R. This is a
   directional signal: the mechanism must be non-perturbative.

## Connection to Paper 11

OC-2 is the cosmological constant problem in geometric form. Solving it
requires the non-perturbative mechanism from Paper 11 Candidate C:

> M2-brane instantons wrapping the e-circle generate:
>     R_obs / R_bare ~ exp(S_{instanton})
> If S_{instanton} ~ 70 (natural in M-theory), then exp(70) ~ 10^{30}.

This would simultaneously:
- Close OC-2 (derive M_KK from first principles)
- Solve the cosmological constant problem (derive R from M2-instantons)
- Complete the framework (remove the last free parameter)

## Revised Classification

OC-2 moves from Tier 1 (high tractability) to Tier 3 (research frontier).
The tractability assessment was an illusion: the computation doesn't
exist because the perturbative physics doesn't exist.

The path forward is Paper 11 Candidate C.

---

*One number. One theorem. One problem left.*
