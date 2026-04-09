# Research 165 — Paper-11 CP² and S² Geometric Corrections on the 9 PDG Stragglers

*Follow-up to research/154 (the partition) and research/156 (KK on S¹
fails). Cycle 5.*

*Date:* 2026-04-09
*Author:* Claude Opus 4.6 (1M), with G Six.

---

## 1. Setup

The 9 PDG-precision observables that no multiplicative envelope
(research/152 Laurent, research/156 KK-on-S¹, research/156 Frobenius,
research/160 conductor lift) has closed are all electroweak/lepton.
Paper 11's geometry is **M⁴ × CP² × S² × S¹**; the spectral BC sector
only sees S¹. CP² is the gauge sector (SU(3)×SU(2)×U(1)/Z₆ from KK,
χ(CP²) = 3 generations, CP¹ holonomy), S² is the Higgs/EW sector
(Casimir on S² sets r₂ ~ 1/TeV, fixing v and m_H).

## 2. Sector assignment

| # | observable      | residual (%) | sector | Paper-11 origin                 |
|:-:|:---             |---:          |:---    |:---                              |
| 1 | m_τ             | −0.167       | S²     | Yukawa = overlap on S² (EW VEV)  |
| 2 | m_μ             | −0.584       | S²     | Yukawa overlap on S²             |
| 3 | m_Z             | +0.080       | S²     | EW gauge boson, m_Z ∝ v          |
| 4 | m_H             | +0.397       | S²     | Higgs = Casimir minimum on S²    |
| 5 | m_W/m_Z         | −0.503       | CP²    | Weinberg angle from CP² holonomy |
| 6 | v               | +0.100       | S²     | EW VEV = S² Casimir scale        |
| 7 | 1/α             | +0.050       | CP²    | U(1)_Y coupling from CP² U(1)    |
| 8 | m_τ/m_μ         | +0.420       | S²     | ratio of S² Yukawa overlaps      |
| 9 | sin θ_12 CKM    | +0.499       | CP²    | CP² geometric (Berry) phase      |

S² sector: 6 entries; CP² sector: 3 entries.

## 3. CP² correction (gauge sector)

CP² with Fubini–Study radius r₃ ~ 10⁻³¹ m carries
R_CP² = 24/r₃² (scalar curvature) and topological data
H²(CP²,ℤ) = ℤ, χ = 3. The mass-scale parameter x = m·r₃ is O(10⁻¹⁷)
for any EW mass, so a *smooth* curvature correction κ·(m r₃)² is
numerically zero (~10⁻³⁴). The only non-vanishing CP² contribution is
**topological/holonomy**, i.e. integer Chern-class shifts in the gauge
coupling and CP¹ Berry phases in the mixing matrices.

Fitting a single CP² holonomy coupling to the three CP² entries:
required shifts (−residual) are **{+0.503, −0.050, −0.499}** %.
These are **mixed-sign with O(1) spread**. No single topological
coefficient (which is sign-locked by the orientation of CP¹) can
reproduce both +0.5% and −0.5% shifts simultaneously. **0 / 3 closed.**

## 4. S² correction (EW/Higgs/lepton sector)

S² with radius r₂ ~ 10⁻¹⁹ m gives x = m·r₂ of order 10⁻¹ at the EW
scale. Casimir on S² (ζ-regulated) produces the multiplicative
envelope

  F_S²(m) = 1 + κ_S² · (m r₂)²  + O((mr₂)⁴),

with κ_S² = 1/(4π) from the S² heat kernel. Calibrating κ_S² r₂² to
close m_H gives 1/r₂ ≈ 561 GeV, the correct ballpark for the Paper 11
Higgs-Casimir minimum (**internal consistency check: passes**).

Applying the *same* (κ_S², r₂) to the other five S² entries:

| observable   | predicted % | target % | closes?              |
|:---          |---:         |---:      |:---                  |
| m_τ          | +0.0001     | +0.167   | no (scales with m²)  |
| m_μ          | +0.0000     | +0.584   | no                   |
| m_Z          | +0.210      | −0.080   | no (wrong sign)      |
| m_H          | +0.397      | −0.397   | **by construction**  |
| v            | +1.534      | −0.100   | no (4× too large)    |
| m_τ/m_μ      | +0.007      | −0.420   | no                   |

The (mr₂)² envelope **scales with mass²**, so leptons receive O(10⁻⁶)
shifts against 10⁻¹% targets, m_Z and v are the wrong sign relative
to m_H, and m_τ/m_μ as a ratio sees near-zero. **1 / 6 closed** (m_H,
and only by the single free parameter used to fit it).

## 5. Sign-consistency audit within each sector

Required shifts per sector:

- S²:  {+0.167, +0.584, −0.080, −0.397, −0.100, −0.420} — **mixed sign**.
- CP²: {+0.503, −0.050, −0.499} — **mixed sign**.

Any *single* geometric coupling per sector (additive, multiplicative,
curvature-induced, or holonomy) is sign-locked within that sector.
Mixed signs inside a sector rule out the sector-uniform correction
hypothesis **before** any numerical fit.

## 6. Tally

| sector | count | closed below PDG error |
|:---    |:-:    |:-:                      |
| CP²    | 3     | 0                       |
| S²     | 6     | 1 (m_H, tautological)   |
| **total** | **9** | **0 / 9 rigorous, 1 / 9 tautological** |

## 7. Verdict

**Paper-11 CP² and S² geometric envelopes do not close the 9 PDG
stragglers.** The sector partition is physically correct (each
observable has a clean Paper-11 origin), but the required residual
shifts carry **mixed signs within each sector**, which is
incompatible with any single CP²- or S²-uniform coefficient. The
S² Casimir envelope is mass²-suppressed and cannot touch lepton
residuals. The CP² correction is topological and sign-locked, and
cannot deliver both +0.5% and −0.5% simultaneously.

Together with research/152 (2nd-order Laurent), research/156 (S¹ KK
and Frobenius), and research/160 (conductor lift), this closes the
**envelope-class** of closure mechanisms for the 9 stragglers. The
residual pattern is **formula-specific, not sector-uniform**: each
straggler must be corrected by a structure that knows its individual
γ-index and gauge decoration. The next candidate (deferred to
research/166) is **off-diagonal KK-mode mixing** between CP² and S²
towers at the level of the single-operator matrix element
(research/163), which is naturally formula-specific and carries
independent signs per (i, j) entry.

### One-sentence summary

CP² and S² give the right physical sector assignments for the 9 PDG
stragglers but no single uniform CP² or S² coupling can close them,
because the required shifts have mixed signs inside each sector —
the closure mechanism must be off-diagonal CP²–S² KK mixing at the
matrix-element level, not a sector-uniform geometric envelope.
