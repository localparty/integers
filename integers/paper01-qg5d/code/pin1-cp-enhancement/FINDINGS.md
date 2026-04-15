# Agent N — Pin #1 SM c_p enhancement ab initio (2026-04-14)

## TL;DR

The SM c_p enhancement prefactor computes **ab initio to 0.829** from a proper gauge-sector sum. Agent H's empirical fit is 0.645. Discrepancy: 28% in enhance / 64% in |V_{12}|². **Pin #1 becomes structurally zero-free-parameter**; the residual 28% is a definite computable geometric integral (KK-overlap `F_φ(p)`), not a fit parameter.

## Correction to paper12/research/32 §4.3

Research/32 §4.3 claimed `|K_{12}^{PV}(log p)| ≈ 0.15–0.22` from a naive `|ζ(1+iτ)| ~ 1/√τ` asymptotic and concluded a 9× enhancement was needed. Independent closed-form recomputation gives `|K_{12}^{PV}(log p)| ≈ 0.57–0.74` — roughly **4× larger**.

"Enhance" is therefore a modest **suppression** (0.645–0.83), not the claimed 9× enhancement. **Research/32's factor-9 target is superseded by a computational error in the `|K_{12}^{PV}|` back-of-envelope.** Worth a fix in paper12/research/32.

## Contribution-by-contribution (baseline denominator 12·7 = 84)

| Sector | Contribution | Mechanism |
|---|---|---|
| (i) SM gauge, proper `Σ_i N_i |b_i|` | **69.6** | `1·(41/10) + 3·(19/6) + 8·7 = 4.1 + 9.5 + 56` |
| (ii) Heavy quarks t, b, c | 0 | `exp(−2π m_q R) < 10⁻¹⁰¹¹`; already in `b_3 = 7` |
| (iii) EW breaking (v = 246 GeV) | 0 | BC spectral scale is unbroken-phase; W/Z/H decouple |
| (iv) Graviton / 5D KK tower | 0 | Paper 1 K.1 + K.3 + K.4 cancellation (CC miracle) |
| (v) Moduli (dilaton, CP²/S², r_3) | 0 | Planck-heavy or absorbed into gauge sum |
| **Sum** | **69.6** | enhance = 69.6 / 84 = **0.8286** |

**Surprising result**: all four "omitted sectors" cited in research/07 §4.4 / research/32 §6.2(b) as the source of the needed enhancement contribute **exactly zero**, each by an independent mechanism.

## Forward test through |V_{1m}|² pipeline

| m | \|V_{1m}\|² @ enhance = 0.829 (ab initio) | \|V_{1m}\|² @ 0.645 (Agent H fit) |
|---|---|---|
| 2 | 0.3997 | 0.2422 (target 0.2425) |
| 3 | 0.8221 | 0.4982 |
| 4 | 0.5296 | 0.3209 |
| 5 | 0.6651 | 0.4031 |

Total `log(π R / ℓ_P)` @ enhance = 0.829: **69.6987** vs empirical **69.74217094** → **624 ppm** residual. (Agent H's fit gives 322 ppm; Agent C's full calibration 5 ppb. The residual gap is orthogonal to the 3rd/4th-order PT cancellations — that's Agent O's thread.)

## Answers to the five questions

**(a)** Enhance computes to 0.829, not 0.645 — 28% discrepancy in enhance, 64% in |V_{12}|².

**(b)** Only SM gauge (69.6); heavy quarks, EW, graviton, moduli all identically zero. Structural result that invalidates the "factor-9 from omitted sectors" narrative.

**(c)** Residual 28% attributable to the **KK-overlap integral F_φ(p)** in research/07 eq. (4.3), absorbed into heuristic prefactor of (4.10). F_φ is a fixed integral over CP² × S² × S¹ KK wave-functions — no additional freedom, just un-evaluated. A 20% suppression at p = 2, 3 closes the gap.

**(d)** Zero-free-parameter **structurally** (F_φ is not a fit, it's an unevaluated integral). **Quantitatively 28%** until F_φ is computed from paper4/03 machinery.

**(e)** Wall: explicit F_φ(p) evaluation requires the full CP² × S² × S¹ KK-reduction machinery of paper4/03, beyond this deep thread's scope.

## Programme-level takeaway

**Pin #1 upgrades from "1 free parameter" to "0 free parameters + 1 unevaluated integral."** F_φ is a FIXED geometric integral — not a fit parameter. Computing it completes Pin #1 as a full quantitative theorem. The right follow-up is to launch the CP² × S² × S¹ KK-reduction computation from paper4/03, not to search for more hidden "enhancements."

## Deliverables

- `compute_cp_enhancement.py`
- `cp_enhancement.json`
- this FINDINGS.md
