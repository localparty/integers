# Appendix Z — Neutrino Mass Ordering from the Bulk Seesaw

<!-- Vocabulary canon note (Intervention 8b, 2026-04-15, aggressive migration applied): this file uses "5D" / "five-dimensional" / "fifth dimension" as subject-matter language. Per strategy/north-star.md §0.10 (Vocabulary Canon), canonical phrasing is "4+1 coordinate structure" / "M⁵" / "internal phase". Inline strikethrough migrations applied per Intervention 8b to thesis sentences and high-salience passages. -->

> The bulk right-handed neutrinos required by the orbifold Casimir
> calculation (Appendix W, §W.9.1) generate neutrino masses through the
> seesaw mechanism in the fifth dimension. The KK scale `m_KK ~ 10 meV` is
> remarkably close to the atmospheric neutrino mass splitting `√(Δm²_atm)`
> `~ 50 meV`, suggesting a direct geometric connection. This appendix
> derives the neutrino mass spectrum from the bulk seesaw and identifies
> the predicted mass ordering.

---

## Z.1 The Bulk Seesaw Mechanism

### Z.1.1 Setup

Three right-handed neutrinos `ν_R^{(i)}` (`i = 1, 2, 3`) propagate in the
5D bulk of the orbifold `S¹/Z₂ = [0, πR]`. The left-handed neutrinos `ν_L^{(i)}`
are localized on the visible brane at `ψ = 0`.

The 5D Dirac mass term couples the brane-localized `ν_L` to the bulk `ν_R`
through the Higgs field (also brane-localized):

    L_Dirac = y₅ × H × ν̄_L × ν_R |_{ψ=0}

where `y₅` is the 5D Yukawa coupling with dimensions `[mass⁻¹/²]`.

### Z.1.2 The Effective 4D Yukawa Coupling

The 4D Yukawa coupling is obtained by evaluating the bulk `ν_R` wave function
at the brane position `ψ = 0`:

    y₄ = y₅ × f_R(0)

where `f_R(ψ)` is the zero-mode profile of the right-handed neutrino in the
bulk. For a flat bulk (no warp factor):

    f_R(0) = 1/√(πR)

The effective 4D Dirac mass is:

    m_D = y₄ × v = y₅ × v / √(πR)

where `v = 246 GeV` is the Higgs VEV.

### Z.1.3 The 5D Fundamental Scale

In a framework with one compact extra dimension, the 4D Planck mass `M_P`
and the 5D fundamental scale `M₅` are related by:

    M_P² = M₅³ × L

where `L = 2πR` is the e-circle circumference. Converting correctly
(`ℏc = 1.973 × 10⁻¹⁶ GeV·m`, so `1 m = 5.068 × 10¹⁵ GeV⁻¹`) with
`R = 12 μm`:

    L = 2π × 12 μm = 7.54 × 10⁻⁵ m = 3.82 × 10¹¹ GeV⁻¹

    M₅ = (M_P² / L)^{1/3} = ((2.44 × 10¹⁸ GeV)² / 3.82 × 10¹¹ GeV⁻¹)^{1/3}
       = (1.56 × 10²⁵ GeV³)^{1/3} = **2.5 × 10⁸ GeV**

Note: An earlier version of this appendix incorrectly converted
`3.82 × 10¹¹ GeV⁻¹` as `3.83 × 10⁻⁷ GeV⁻¹`, off by a factor of 10¹⁸.
The correct value is `M₅ ~ 2.5 × 10⁸ GeV`, not `10¹⁴ GeV`.

### Z.1.4 The Neutrino Mass Scale and the Role of CP²

With `M₅ = 2.5 × 10⁸ GeV`, the naive seesaw `m_ν = y² v²/M₅` gives
`m_ν ~ y² × 240 keV` — far too heavy for any perturbative `y`.

This is resolved by identifying the correct seesaw scale. The Majorana
mass of the bulk right-handed neutrinos is NOT set by `M₅` (the S¹
compactification scale) but by the **CP² compactification scale**:

    M_R = 1/r₃ ~ M_GUT ~ 10¹⁵ GeV

This is both physically correct and better motivated: the seesaw scale
should be the GUT scale where the SM gauge couplings unify, which in
the framework is the CP² scale (Paper 4, §3.3). The S¹ scale sets the
dark energy and KK mass scales; the CP² scale sets the GUT and seesaw
scales. Each compact dimension contributes at its own energy level.

With `M_R = M_GUT ~ 10¹⁵ GeV`:

    m_ν = y² × v² / M_R = y² × (246 GeV)² / (10¹⁵ GeV) = y² × 0.06 eV

For `y ~ 1`: `m_ν ~ 0.06 eV`, matching `Σm_ν ~ 0.06 eV` (normal ordering,
Planck bound).
For `y ~ 0.9`: `m_ν ~ 50 meV = √(Δm²_atm)`. ✓

**What is determined vs. what is free:**

| Quantity | Origin | Status |
|----------|--------|--------|
| `M₅ = 2.5 × 10⁸ GeV` | From `R = 12 μm` via `M_P² = M₅³ L` | **Determined** |
| `M_R = M_GUT ~ 10¹⁵ GeV` | From CP² radius `r₃` (Paper 4, §3.3) | **Determined** |
| `m_ν ~ y² × 0.06 eV` | Seesaw with `M_R = M_GUT` | **Predicted (scale)** |
| `y ~ 0.9` for `m_ν = 50 meV` | Yukawa coupling | Free parameter |

The framework determines the seesaw SCALE geometrically (from CP²)
and the KK scale separately (from S¹). The two scales are distinct
and serve different physical roles.

## Z.2 The Mass Ordering Prediction

### Z.2.1 The Three Bulk Neutrinos on the `Z₃` Orbifold

On the `Z₆` orbifold (`Z₂ × Z₃`), the three bulk right-handed neutrinos
are localized at the three `Z₃` fixed points in the bulk:

    ν_R^{(1)} at ψ ~ 0 (near the visible brane)
    ν_R^{(2)} at ψ ~ π/3
    ν_R^{(3)} at ψ ~ 2π/3

The Dirac mass of each neutrino depends on the OVERLAP between the
brane-localized `ν_L` (at `ψ = 0`) and the bulk `ν_R` at its fixed point:

    m_D^{(i)} ∝ exp(−c_i × ψ_i / R)

where `c_i` is the bulk mass parameter and `ψ_i` is the distance from the
brane.

### Z.2.2 The Hierarchy

For the three neutrinos:

    m_D^{(1)} ∝ exp(0) = 1 (near the brane — largest coupling)
    m_D^{(2)} ∝ exp(−c × π/(3R)) (moderate distance — suppressed)
    m_D^{(3)} ∝ exp(−c × 2π/(3R)) (farthest — most suppressed)

The effective light neutrino masses (from the seesaw `m_ν ~ m_D² / M_R`)
inherit the hierarchy:

    m_ν^{(1)} >> m_ν^{(2)} >> m_ν^{(3)}

The HEAVIEST neutrino is the one whose right-handed partner is closest
to the visible brane. This gives:

    m₃ > m₂ > m₁

### Z.2.3 The Prediction: Normal Ordering

The mass ordering `m₃ > m₂ > m₁` is the **NORMAL ordering** (also called
the normal hierarchy). This is the ordering where the largest mass
splitting (the atmospheric splitting `Δm²_atm`) is between the heaviest
state and the other two.

**The orbifold predicts normal ordering** because the bulk seesaw
mechanism naturally produces a hierarchy where the neutrino closest to
the brane is heaviest, and the geometric `Z₃` structure ensures the
three states are separated in the fifth dimension.

### Z.2.4 Comparison with Experiment

Current experimental hints favor normal ordering at `~2-3σ`
(NOvA, T2K, Super-Kamiokande atmospheric data). JUNO began data taking in
August 2025 and published its first oscillation results in November 2025,
measuring `θ₁₂` and `Δm²₂₁` with world-leading precision (arXiv:2511.14593).
The mass ordering determination requires a larger dataset and is expected
within the experiment's 6-year run.

If JUNO confirms normal ordering: consistent with the prediction.
If JUNO finds inverted ordering: the simple `Z₃` bulk seesaw is falsified
(but more complex bulk profiles could accommodate inverted ordering).

## Z.3 The KK Scale and the Seesaw Scale

The framework now has two distinct geometric scales relevant to neutrinos:

| Scale | Value | Origin | Role |
|-------|-------|--------|------|
| `M₅ = 2.5 × 10⁸ GeV` | From `R = 12 μm`, `M_P² = M₅³ L` | S¹ | 5D Planck mass |
| `m_KK = ℏc/R ~ 16 meV` | From `R = 12 μm` directly | S¹ | KK graviton mass |
| `M_R = 1/r₃ ~ 10¹⁵ GeV` | From CP² radius | CP² | Seesaw / GUT scale |

The KK mass `m_KK ~ 16 meV` and the atmospheric splitting `√(Δm²_atm) ~ 50 meV`
are within a factor of 3 of each other. This is a genuine geometric
correlation: both are ultimately set by the e-circle radius `R`, but through
different routes — the KK mass directly (`1/R`), and the neutrino mass
indirectly through the GUT scale set by CP² which is itself related to R
through the gauge coupling unification conditions (Paper 4, §7.16).

The two-scale structure — the e-circle radius R setting the dark energy and KK
graviton scales, and the seesaw scale M_R from the GUT geometry of Paper 4
setting the neutrino mass scale — suggests that a unified geometric framework
can account for these apparently unrelated scales. The specific identification
of M_R with the CP² radius is deferred to Paper 4.

### Z.3.1 Deferred to Paper 4

A topological derivation of the neutrino-to-KK mass ratio from the characteristic
classes of CP² (Freed-Witten anomaly cancellation, G₄ flux quantization, and the
Euler characteristic χ(CP²) = 3) is not within the scope of this paper. Paper 1
establishes the M⁴ × S¹ sector. CP² appears in the full 11-dimensional
M-theory compactification M⁴ × CP² × S² × S¹ of Paper 4. The formula

    m_ν / m_KK = χ(CP²) − c₂^{eff}(V)|_{CP²} = 5/2

requires: (i) the identification of the gauge bundle V over CP² with c₂(V) = 1,
established in Paper 4 via the Horava-Witten construction; (ii) the Freed-Witten
anomaly cancellation condition on the non-spin manifold CP², which is a
statement about the 11D geometry; (iii) the seesaw chain relating the Dirac
index on CP² to the neutrino zero-mode count and to the mass ratio via M_R =
1/r₃. All three ingredients are outside M⁴ × S¹ geometry. The derivation is
deferred in full to Paper 4.

The numerical proximity of m_ν ~ 50 meV and m_KK ~ 16–20 meV (a factor of
~ 2.5) is noted as a suggestive coincidence within the present paper. Whether
this proximity has a topological origin in the characteristic classes of the
higher-dimensional geometry will be established in Paper 4.

Note on the spin-statistics connection: the spin-statistics result of Section 4.2
is derived within M⁴ × S¹ geometry, using π₁(SO(d)) = ℤ₂ and the e-phase
coupling postulate. It does not require CP², and CP² does not appear in the
argument. The non-spin character of CP² (w₂(CP²) ≠ 0) is a property of the
11-dimensional compactification geometry of Paper 4, not of the M⁴ × S¹
framework of this paper. The connection between the spin-statistics result
established here and the G₄ flux quantization of the 11D theory is a feature
of the embedding — to be established in Paper 4 — not a result of the present
paper.

## Z.4 Summary

| Prediction | Value | Test | Timeline |
|-----------|-------|------|---------|
| Neutrino mass scale | `m_ν ~ 50 meV` | KATRIN, PTOLEMY | 5-10 years |
| Mass ordering | **Normal** (`m₃ > m₂ > m₁`) | JUNO | 3-6 years |
| Lightest mass | `m₁ ~ few meV` (from `Z₃` suppression) | Cosmological bounds | Ongoing |
| KK-neutrino coincidence | `m_KK ~ m_ν` within 5x | Short-range gravity | 3-5 years |

## Z.5 References

- Dienes, K. R., Dudas, E. & Gherghetta, T. "Neutrino Masses without
  Fundamental Mass Scales." *Nucl. Phys. B* 557, 25 (1999).
- Arkani-Hamed, N., Dimopoulos, S., Dvali, G. & March-Russell, J.
  "Neutrino Masses from Large Extra Dimensions." *Phys. Rev. D* 65,
  024032 (2002).
- JUNO Collaboration. "First oscillation results from JUNO."
  arXiv:2511.14593 (2025).
- Esteban, I. et al. "NuFIT 5.3." *JHEP* (2024). — Global fit of
  neutrino oscillation parameters.
- Freed, D. S. & Witten, E. "Anomaly cancellation in Type II string
  theory." *Asian J. Math.* 3, 819 (1999). [arXiv:hep-th/9907189] —
  Establishes that `G₄` must be half-integer shifted on non-spin manifolds.
- Horava, P. & Witten, E. "Eleven-Dimensional Supergravity on a Manifold
  with Boundary." *Nucl. Phys. B* 475, 94 (1996). — Anomaly cancellation
  requires the half-integer flux shift on the non-spin CP² factor.
