# Paper 6 — Section 2: The Dilaton Potential

## 2.1 Derivation from the 5D Action

The 5D Einstein-Hilbert action on `M⁴ × S¹/Z₂` reduces (Paper 1,
Appendix D) to a 4D effective action containing the dilaton `φ`:

    S_4D = ∫ d⁴x √(−g) [M_Pl²/2 × R₄ − (1/2)(∂φ)² − V(φ)]

where the dilaton kinetic term is canonically normalized by the field
redefinition `φ = M_Pl × ln(R/R_Pl)` (R = e-circle radius).

## 2.2 The Casimir Contribution

The Casimir energy of bulk fields on `S¹/Z₂` (Paper 1 Appendix W,
§W.9.2) gives:

    V_Cas(R) = −π²/(768(πR)⁴) × (ℏc)³

In terms of the canonically normalized dilaton `φ`:

    V_Cas(φ) = −C × e^{−4φ/M_Pl}    (for φ/M_Pl ≫ 1)
             ≈ −C/φ⁴                  (approximate form for slow-roll)

where `C = π²/(768π⁴) × M_Pl⁴` in natural units.

This potential is:
- **Negative at large φ**: attractive, pulling φ toward smaller values
- **Flat at large φ**: the `1/φ⁴` decay makes it an excellent inflation plateau
- **Diverges at φ = 0**: prevents the e-circle from collapsing

## 2.3 The Goldberger-Wise Contribution

A bulk scalar field `Φ(x, φ)` with brane-localized potentials
(Goldberger & Wise 1999) generates an additional dilaton potential:

    V_GW(φ) = m_φ²/2 × (φ − φ_min)² + λ_4(φ − φ_min)⁴ + ...

where:
- `φ_min = M_Pl × ln(R_min/R_Pl)` is the stabilization point
- `m_φ = V_GW''(φ_min)^{1/2}` is the dilaton mass
- The parameters are fixed by the dark energy condition:
  `V(φ_min) = ρ_Λ = (2 meV)⁴`

## 2.4 The Combined Potential

    V(φ) = −C/φ⁴ + m_φ²(φ − φ_min)²/2

**Regions:**

| φ range | Dominant term | Physics |
|---------|---------------|---------|
| `φ ≪ φ_min` | `−C/φ⁴` (Casimir) | Inflation plateau |
| `φ ≈ φ_min` | `m_φ²(Δφ)²/2` | Stable minimum |
| `φ slightly > φ_min` | Thawing | Dark energy `w → −0.85` |

## 2.5 The Dilaton Mass

From the stabilization condition `V'(φ_min) = 0` and `V(φ_min) = ρ_Λ`:

    m_φ² = 4C/φ_min⁵ = 4ρ_Λ/φ_min ~ (H_0 M_Pl)

    m_φ ~ √(H_0 M_Pl) ~ √(10⁻³³ eV × 10²⁸ eV) ~ 10⁻³ eV ~ meV

The dilaton mass is at the **meV scale** — exactly the dark energy
scale. This is the same scale as the neutrino mass (Paper 2, Appendix Z)
and the Casimir energy scale (Paper 1, §6.6). One radius, three
manifestations of the same scale.

This mass is far below current laboratory constraints on new light
scalars (`m > few meV` from fifth-force experiments at the e-circle
scale `R ~ 8.5 μm`). The dilaton is light enough to roll today.
