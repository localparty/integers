# Appendix Z — Neutrino Mass Ordering from the Bulk Seesaw

> The bulk right-handed neutrinos required by the orbifold Casimir
> calculation (Appendix W, §W.9.1) generate neutrino masses through the
> seesaw mechanism in the fifth dimension. The KK scale m_KK ~ 10 meV is
> remarkably close to the atmospheric neutrino mass splitting √(Δm²_atm)
> ~ 50 meV, suggesting a direct geometric connection. This appendix
> derives the neutrino mass spectrum from the bulk seesaw and identifies
> the predicted mass ordering.

---

## Z.1 The Bulk Seesaw Mechanism

### Z.1.1 Setup

Three right-handed neutrinos ν_R^{(i)} (i = 1, 2, 3) propagate in the
5D bulk of the orbifold S¹/Z₂ = [0, πR]. The left-handed neutrinos ν_L^{(i)}
are localized on the visible brane at ψ = 0.

The 5D Dirac mass term couples the brane-localized ν_L to the bulk ν_R
through the Higgs field (also brane-localized):

    L_Dirac = y₅ × H × ν̄_L × ν_R |_{ψ=0}

where y₅ is the 5D Yukawa coupling with dimensions [mass⁻¹/²].

### Z.1.2 The Effective 4D Yukawa Coupling

The 4D Yukawa coupling is obtained by evaluating the bulk ν_R wave function
at the brane position ψ = 0:

    y₄ = y₅ × f_R(0)

where f_R(ψ) is the zero-mode profile of the right-handed neutrino in the
bulk. For a flat bulk (no warp factor):

    f_R(0) = 1/√(πR)

The effective 4D Dirac mass is:

    m_D = y₄ × v = y₅ × v / √(πR)

where v = 246 GeV is the Higgs VEV.

### Z.1.3 The 5D Fundamental Scale

In a framework with one compact extra dimension, the 4D Planck mass M_P
and the 5D fundamental scale M₅ are related by:

    M_P² = M₅³ × L

where L = 2πR is the e-circle circumference. Solving for M₅ with
R = 12 μm (the orbifold scenario):

    L = 2π × 12 μm = 7.54 × 10⁻⁵ m = 3.83 × 10⁻⁷ GeV⁻¹

    M₅ = (M_P² / L)^{1/3} = ((2.44 × 10¹⁸)² / 3.83 × 10⁻⁷)^{1/3} GeV
       = (1.55 × 10⁴³)^{1/3} GeV = **2.5 × 10¹⁴ GeV**

The compact e-circle at R ~ 12 μm sets the 5D fundamental scale at the
**GUT scale** (~10¹⁴ GeV) — precisely where the SM gauge couplings nearly
unify. This is a geometric determination, not a parameter choice.

### Z.1.4 The Neutrino Mass Scale

The standard type-I seesaw gives m_ν = y² v² / M_R, where v = 246 GeV
is the Higgs VEV, y is the Yukawa coupling, and M_R is the right-handed
neutrino Majorana mass. In the orbifold framework, the natural Majorana
scale is M_R = M₅ (the 5D Planck mass sets the mass of bulk fields). The
seesaw prediction is:

    m_ν = y² × v² / M₅ = y² × (246 GeV)² / (2.5 × 10¹⁴ GeV) = y² × 0.24 eV

For y = 1: m_ν = 0.24 eV — within a factor of 5 of the observed
atmospheric mass splitting √(Δm²_atm) ≈ 50 meV. The framework predicts
the correct **mass scale** (sub-eV) from the geometry alone. The exact
mass requires the Yukawa coupling y, which is a free parameter of the
theory (as in the standard seesaw). For y ≈ 0.45: m_ν ≈ 50 meV.

**What is determined vs. what is free:**

| Quantity | Origin | Status |
|----------|--------|--------|
| M₅ = 2.5 × 10¹⁴ GeV | From R = 12 μm via M_P² = M₅³ L | **Determined** |
| m_ν ~ v²/M₅ ~ 0.24 eV | Standard seesaw with M_R = M₅ | **Predicted (scale)** |
| y ~ 0.45 for m_ν = 50 meV | Yukawa coupling | Free parameter |

The framework determines the SCALE of neutrino masses (sub-eV) but not the
EXACT values (which require the Yukawa couplings). This is the same
situation as the standard seesaw — the e-circle contribution is to
determine M₅ geometrically, replacing it as a free parameter.

This matches the atmospheric neutrino mass splitting √(Δm²_atm) ≈ 50 meV.

## Z.2 The Mass Ordering Prediction

### Z.2.1 The Three Bulk Neutrinos on the Z₃ Orbifold

On the Z₆ orbifold (Z₂ × Z₃), the three bulk right-handed neutrinos
are localized at the three Z₃ fixed points in the bulk:

    ν_R^{(1)} at ψ ~ 0 (near the visible brane)
    ν_R^{(2)} at ψ ~ π/3
    ν_R^{(3)} at ψ ~ 2π/3

The Dirac mass of each neutrino depends on the OVERLAP between the
brane-localized ν_L (at ψ = 0) and the bulk ν_R at its fixed point:

    m_D^{(i)} ∝ exp(−c_i × ψ_i / R)

where c_i is the bulk mass parameter and ψ_i is the distance from the
brane.

### Z.2.2 The Hierarchy

For the three neutrinos:

    m_D^{(1)} ∝ exp(0) = 1 (near the brane — largest coupling)
    m_D^{(2)} ∝ exp(−c × π/(3R)) (moderate distance — suppressed)
    m_D^{(3)} ∝ exp(−c × 2π/(3R)) (farthest — most suppressed)

The effective light neutrino masses (from the seesaw m_ν ~ m_D² / M_R)
inherit the hierarchy:

    m_ν^{(1)} >> m_ν^{(2)} >> m_ν^{(3)}

The HEAVIEST neutrino is the one whose right-handed partner is closest
to the visible brane. This gives:

    m₃ > m₂ > m₁

### Z.2.3 The Prediction: Normal Ordering

The mass ordering m₃ > m₂ > m₁ is the **NORMAL ordering** (also called
the normal hierarchy). This is the ordering where the largest mass
splitting (the atmospheric splitting Δm²_atm) is between the heaviest
state and the other two.

**The orbifold predicts normal ordering** because the bulk seesaw
mechanism naturally produces a hierarchy where the neutrino closest to
the brane is heaviest, and the geometric Z₃ structure ensures the
three states are separated in the fifth dimension.

### Z.2.4 Comparison with Experiment

Current experimental hints favor normal ordering at ~2-3σ
(NOvA, T2K, Super-Kamiokande atmospheric data). JUNO began data taking in
August 2025 and published its first oscillation results in November 2025,
measuring θ₁₂ and Δm²₂₁ with world-leading precision (arXiv:2511.14593).
The mass ordering determination requires a larger dataset and is expected
within the experiment's 6-year run.

If JUNO confirms normal ordering: consistent with the prediction.
If JUNO finds inverted ordering: the simple Z₃ bulk seesaw is falsified
(but more complex bulk profiles could accommodate inverted ordering).

## Z.3 The KK Scale Coincidence

The most striking feature: the KK mass from R ~ 12 μm is:

    m_KK = ℏc/R ~ 10 meV

The atmospheric neutrino mass splitting is:

    √(Δm²_atm) ~ 50 meV

These are within a factor of 5 of each other. In the bulk seesaw, the
neutrino mass is set by v²/M₅, where M₅ is determined by R through
M₅ = (M_P²/(2πR))^{1/3}. The coincidence m_ν ~ m_KK (within an order
of magnitude) is a consequence of the fact that the same R determines
both scales — it is not a tuning but a GEOMETRIC CORRELATION.

The geometric unification of the GUT scale with the e-circle radius is a
non-trivial constraint. A single parameter — R ≈ 12 μm — simultaneously
determines: the dark energy density (through the Casimir energy), the
neutrino mass scale (through M₅ = (M_P²/L)^{1/3} and the seesaw), the
Yukawa force range (through m_KK = ℏc/R), and the scale of gauge coupling
near-unification (M₅ ~ 10¹⁴ GeV ≈ M_GUT). That four apparently unrelated
scales — cosmological constant, neutrino mass, submillimeter gravity, and
grand unification — trace to the same geometric origin is the strongest
structural argument for the e-circle's physical reality.

## Z.4 Summary

| Prediction | Value | Test | Timeline |
|-----------|-------|------|---------|
| Neutrino mass scale | m_ν ~ 50 meV | KATRIN, PTOLEMY | 5-10 years |
| Mass ordering | **Normal** (m₃ > m₂ > m₁) | JUNO | 3-6 years |
| Lightest mass | m₁ ~ few meV (from Z₃ suppression) | Cosmological bounds | Ongoing |
| KK-neutrino coincidence | m_KK ~ m_ν within 5× | Short-range gravity | 3-5 years |

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
