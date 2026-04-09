# Research 139 — β = 1 + ε Postulate-Relaxation Experiment

*Date:* 2026-04-09
*Author:* postulate-relaxation agent (Claude Opus 4.6, 1M).
*Scope:* Test whether relaxing the β = 1 KMS postulate to β = 1 + ε
improves the global residual of the 36-formula master table
(`research/23`), and whether a single ε explains both the CC
5-ppb residual (`research/05`) and the (alleged) 2.2 % DM/hierarchy
residual (`research/39`).

## 1. Setup

Postulate under test: the QG5D framework uses the Bost–Connes KMS
state ω_1 at the distinguished inverse temperature β = 1. Relaxation:
β = 1 + ε, with ε small but nonzero. Standard KMS perturbation gives

F(β) ≈ F(1) + ε · F'(1) + O(ε²)

for any observable F whose computation flows through ω_β.

## 2. Structural observation (the key point)

**The 34/36 entries in the master table of `research/23` are
polynomial, rational, log, or root expressions in the Riemann
imaginary parts γ_n, π, e, γ_E, ζ(2), ζ(3).** They do not reference
β, ω_β, or any KMS expectation value explicitly. The γ_n are
intrinsic to ζ(s) and are β-independent; they enter the framework as
eigenvalues of the operator T_BC (or R̂ = (ℓ_P/π)·exp(T_BC·π²/2)),
not as expectations in ω_β.

Consequently, for 34 of 36 fitted formulas,

F'(1) = 0 identically.

The β perturbation has no leading-order effect. There is nothing to
fit: ε drops out of the residual function.

The two formulas with β-sensitivity are:

- **CC formula (r/05)**: the Rayleigh–Schrödinger PT corrections
  (−0.15/γ_2, +0.03/γ_3, −0.01·log(γ_2/γ_1)) arise from first- and
  second-order PT on an ω_β-dependent matrix element. A linear
  reweighting by (1 + ε) is a plausible ansatz.
- **m_H/M_Pl hierarchy (r/39 eq. 3.8)**: exp(−γ_6)·(2π/γ_5) involves
  a bare BC dilation scale exp(−γ_6). Under β → 1 + ε this becomes
  exp(−γ_6·(1 + ε)).

## 3. mpmath scan (50 dps)

Ran both β-sensitive observables over ε ∈ [−2·10⁻², 2·10⁻²].

| Observable | ε = 0 rel. err. | Best-fit ε | Rel. err. at best fit |
|:---|:---:|:---:|:---:|
| CC formula | −4.91·10⁻⁸ | −2·10⁻⁵ | 4.66·10⁻⁸ |
| m_H/M_Pl (r/39 3.8) | −1.12·10⁻¹ | −3.2·10⁻³ | 1.58·10⁻³ |
| All 34 others | varies | (ε-independent) | unchanged |

## 4. Does a single ε explain both residuals?

**No.** The CC formula prefers ε ~ −2·10⁻⁵, which is
indistinguishable from zero given its PT-coefficient uncertainty
(the CC formula is almost insensitive to ε because the
ε-dependent terms are themselves ~10⁻³ in magnitude). The
hierarchy (r/39 3.8) prefers ε ~ −3·10⁻³ — **two orders of
magnitude larger** than the CC preference.

More importantly: **the 2.2 % DM/hierarchy residual does not
exist.** `research/39` lines 336–344 contain an explicit round-3
erratum: the original (3.8) arithmetic was wrong. The correct
value of exp(−γ_6)·(2π/γ_5) is 9.058·10⁻¹⁸, residual **13.2 %**,
not 2 %. The "shared 2.2 % cross-phenomenon link" was retracted
(see `research/78`). The premise of the experiment — that CC 5 ppb
and DM/hierarchy 2.2 % might both be powers of the same ε —
collapses on inspection: one of the two numbers is a
computational artefact.

## 5. Verdict

**WORSE LEAD.** The β = 1 + ε relaxation:

1. Has **no effect** on 34/36 formulas (the γ_n are β-independent
   eigenvalues, not ω_β expectations).
2. Marginally improves the CC formula by one part in ~10⁹, at a
   preferred ε (~2·10⁻⁵) that is both fit-unstable and comparable
   to the rounding of the PT coefficients themselves — zero
   significance.
3. Cannot explain the hierarchy residual because that residual is
   **13 %**, not 2.2 %, and requires ε ~ 3·10⁻³, which would
   destroy the CC 5-ppb match if ε were truly global.
4. **Formulas improved: 0** (the CC "improvement" is in the
   coefficient-noise floor; the hierarchy fit is only improved if
   one abandons cross-formula consistency).

β = 1 is not a relaxable postulate here: it is **fixed by the BC
phase-transition structure** (the distinguished KMS state at the
critical temperature), not an empirical input with a residual budget.
The correct interpretation of the 5 ppb CC residual is that it is
the Rayleigh–Schrödinger higher-order PT truncation error on
H_R (see `research/05` §§7–9, `research/17`), not a thermodynamic
detuning of ω_1.

**One-sentence verdict.** β = 1 + ε is a NEUTRAL-to-WORSE lead: the
master-table formulas do not depend on β at leading order, the
alleged shared 2.2 % residual is an arithmetic error already
retracted in `research/39`, and no single ε can simultaneously
improve the CC and hierarchy residuals.
