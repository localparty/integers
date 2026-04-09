# 138 — Two-Clock Hypothesis Test

**Date:** 2026-04-09
**Agent:** postulate-relaxation experiment (Opus 4.6, 1M ctx)

## Hypothesis

The e-circle S¹ of Papers 1–11 is **not** a time clock; it is a charge /
U(1)-phase circle. The true clock is the modular flow
σ_t = Δ_{ω_1}^{it} of the Bost–Connes critical state at β=1 (Paper 17).
The two clocks coincide on-shell at β=1, but the mismatch may appear as
common residuals in formulas carrying explicit 2π or π² factors tied to
the e-circle.

Operationally we test two relaxations:

1. **Winding relaxation.** Replace each 2π factor by (2π · w), with
   w rational (num/den, 1..5), per formula.
2. **Universal modular shift.** Replace the geometric 2π by
   (2π)(1+δ), with a single δ fit jointly across all affected
   formulas. Here δ measures a systematic mismatch between the
   e-circle clock and the modular clock.

All arithmetic at mpmath 50 dps using high-precision Riemann zeros γ_n.

## Formulas tested (from research/23)

| name | measured | framework formula | e-circle power p |
|---|---|---|---|
| m_t | 172.76 GeV | γ_3·γ_8/(2π) | +1 |
| m_H | 125.10 GeV | γ_2·γ_6/(2π) | +1 |
| 1/α_3 | 8.475 | γ_11/(2π) | +1 |
| m_s | 93.4 MeV | γ_1·γ_15/π² | +2 |
| H_0 | 67.4 km/s/Mpc | γ_11·4/π | −1 |
| N_inflation | 58.79 | (γ_5−γ_2)·π²/2 | +2 (mult) |
| CC hierarchy | 2×10³⁰ | exp(γ_1·π²/2) | inside exp |

## Results — Winding relaxation

For every formula, the optimum over rational w ∈ {1/5 … 5} is **w=1**.
Formulas are already calibrated at unit winding; no rational w ≠ 1
improves any residual. Expected, but rules out a simple integer-winding
reinterpretation.

## Results — Universal modular shift

Joint least-squares fit of a single δ across the 5 pure-power formulas
(m_t, m_H, 1/α_3, m_s, H_0):

    δ_best = +6.992 × 10⁻⁴    (i.e. (2π)_eff = 2π × 1.000699)

| formula | old residual | new residual | change |
|---|---|---|---|
| m_t | 1.691e-3 | 2.389e-3 | worse |
| m_H | 5.231e-3 | 4.529e-3 | **SHRANK** |
| 1/α_3 | 5.252e-3 | 5.947e-3 | worse |
| m_s | 1.598e-3 | 2.993e-3 | worse |
| H_0 | 6.515e-4 | 1.351e-3 | worse |

RMS residual: 3.487e-3 → 3.804e-3 (**up 9 %**).
Shrinks: **1 / 5**.

N_inflation and CC hierarchy: residuals are already ≲10⁻⁵ and sit
inside an exponential; no meaningful universal shift can improve them
without destroying N_inf, so they are excluded from the joint fit.

## Interpretation

The residuals of the 2π-bearing formulas have **mixed signs**
(log γ_3γ_8/(2π·m_t) is negative while log γ_11/(2π·1/α_3⁻¹) is
positive, etc.). No universal rescaling of 2π can simultaneously
shrink opposite-sign residuals; this is why the joint fit degrades
overall. The relaxation therefore cannot be the origin of the common
2.2 % DM/hierarchy residual (research/39).

The one formula that does shrink (m_H) does so only marginally
(5.23e-3 → 4.53e-3) and at the cost of degrading four others — this
is a fit artefact, not a signal.

## Verdict

**WORSE.** The two-clock relaxation, in either the winding-number or
universal-modular-shift form, fails to reduce residuals across the
formulas that explicitly carry e-circle 2π/π² factors. The mixed-sign
residual pattern is incompatible with a single clock-mismatch
parameter. The postulate "e-circle = time clock" is (empirically, at
this level of test) not the source of the framework's sub-percent
residuals; they must arise from independent per-γ effects.

Not worth pursuing as a lead; the e-circle-as-charge vs e-circle-as-clock
distinction, if physically real, is degenerate with w=1 on-shell and
produces no testable residual at the current measurement precision.
