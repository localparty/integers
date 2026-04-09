# Research 04: OC-2 — Theorem U Blockage and the CC Problem

**Date:** April 8, 2026
**Status:** DIAGNOSED (not closeable by computation)
**Result:** OC-2 is blocked by Theorem U; connects to Paper 11 Candidate C
**Detailed status:** `05-oc2-theorem-u-status.md`

---

## Problem Statement

Open Calculation 2 (OC-2): What is the absolute scale of r_2 (S^2 radius)?
Equivalently: what is M_KK = 1/r_2, the KK mass that determines m_H?

Initial assessment: Tier 1 target, 1-2 sessions, compute Casimir minimum.

---

## The Chain of Equations (All Derived)

### Step 1: G_2 torsion coefficient

    c_0 = 1/42    (from FKMS 1997 classification)
    cR = (64pi^5/(126 l_11^3)) x R

Source: Paper 7, Section 2 (`paper7/02-g4-flux-on-cp2-s2.md`)

### Step 2: GVW superpotential

    W_total = n_1 r_3^2 + n_2 r_2^2 + cR(6 r_3^2 r_2^2 - 2 r_3^4)

Source: Paper 7, Section 3 (`paper7/03-moduli-minimum.md`)

### Step 3: F-flatness (r_3)

From D_{r_2} W = 0:

    r_3^2 = n_1/(2cR) = 9/(2cR)

Key property: the equation for D_{r_2} W contains NO r_2 dependence
(exact cancellation between torsion and Kahler terms). This gives
r_3 directly.

### Step 4: Radius ratio (topological)

From D_{r_3} W = 0:

    rho^2 = r_2^2/r_3^2 = -2n_1/[3(n_1 + n_2)]

Critical: **cR cancels completely.** The ratio is topological.

### Step 5: GUT condition (flux quantization)

Setting rho = sqrt(3)/2 (gauge coupling unification):

    n_2/n_1 = -17/9
    n_1 = 9, n_2 = -17 (coprime integers)

### Step 6: Planck mass constraint

    M_Pl^2 = M_11^9 x Vol_7 = M_11^9 x (64pi^5/3) r_3^4 r_2^2 R

### Step 7: Theorem U — the algebraic closure

Substituting Steps 2-5 into Step 6, ALL internal geometry cancels:

    R_bare = (63 n_1)^{3/2} / (128 pi^{11/2} M_Pl)

Numerically: R_bare ~ 0.975 l_P ~ 1.6 x 10^{-35} m.

The 11D Planck length l_11 drops out of the combined system. The
observed R_obs ~ 10.1 um is 30 orders of magnitude larger than R_bare.

---

## Why This Is Not a Missing Computation

The algebraic system (F-flatness + Planck mass + torsion) is
**degenerate**: it determines R uniquely, but gives R ~ l_P.
There is no additional equation that could fix R at 10 um.
No perturbative M-theory calculation can produce the ratio
R_obs/R_bare ~ 10^30.

This is not a bug — it is the **cosmological constant problem**
in geometric form:

    rho_Lambda = c/R^4
    rho_Lambda(R_bare) ~ M_Pl^4  (catastrophically large)
    rho_Lambda(R_obs) ~ (2.25 meV)^4  (observed)
    rho_bare/rho_obs ~ 10^{120}

The hierarchy R_obs/R_bare ~ 10^30 IS the CC hierarchy rho_bare/rho_obs ~ 10^{120}
(since rho ~ R^{-4}, the ratio in R is the fourth root of the ratio in rho).

---

## What IS Determined

| Quantity | Status | Depends on R? |
|----------|--------|--------------|
| r_2/r_3 = sqrt(3)/2 | **DERIVED** | No (topological) |
| n_2/n_1 = -17/9 | **DERIVED** | No (Diophantine) |
| M_KK proportional to R^{1/2} | **DERIVED** | Yes (functional form only) |
| M_GUT proportional to R^{1/2} | **DERIVED** | Yes |
| M_KK ~ 1-2.5 TeV | **CONSISTENT** | Given R_obs = 10.1 um |
| m_H ~ 125 GeV | **CONSISTENT** | Given M_KK |

---

## Connection to Paper 11

OC-2 connects directly to Paper 11 Candidate C:

> "The Cosmological Constant from Non-Perturbative e-Circle Dynamics"
>
> M2-brane instantons wrapping the e-circle generate:
>     R_obs/R_bare ~ exp(S_instanton)
> If S_instanton ~ 70 (natural in M-theory), then exp(70) ~ 10^30.

Solving OC-2 = solving the CC problem = deriving R from non-perturbative
M-theory.

---

## Revised Classification

OC-2 moved from Tier 1 (1-2 sessions) to Tier 3 (research frontier).

---

## References

- Paper 7, Section 2-3 (GVW superpotential, moduli minimum)
- Paper 7, Appendix A (Theorem U*)
- Paper 4, Section 6 (Higgs mechanism, OC-2 statement)
- Paper 4, Appendix D (Higgs naturalness)
- `etc/frontier-research/problem2-higgs-mass.md` (existing analysis)
- `etc/12-closing-the-open-problems-plan.md` Problem 2
