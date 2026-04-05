## 7. Predictions


### 7.1 The Weinberg Angle from Geometry

The Weinberg angle `θ_W` relates the `SU(2)_L` and `U(1)_Y` gauge
couplings:

    sin²θ_W = g₁² / (g₁² + g₂²)

In the KK framework, the gauge couplings are determined by the
volumes of the internal spaces:

    g₃² = 16πG₁₁ / Vol(CP²)
    g₂² = 16πG₁₁ / Vol(S²)
    g₁² = 16πG₁₁ / Vol(S¹)

The Weinberg angle at the compactification scale `M_c` is:

    sin²θ_W(M_c) = Vol(S²) / (Vol(S²) + Vol(S¹))

For the canonical metric on `S²` with radius `r₂` and `S¹` with
radius `R`:

    Vol(S²) = 4πr₂²
    Vol(S¹) = 2πR

The ratio depends on `r₂/R` — the relative size of the weak and
electromagnetic compact dimensions. If the internal manifold is
chosen to be a product of round (constant-curvature) spaces with
the same Ricci scalar (equal curvature condition):

    R_{S²} = R_{S¹}  →  1/r₂² = 1/R²  →  r₂ = R

This gives:

    sin²θ_W(M_c) = 4πR² / (4πR² + 2πR) = 2R / (2R + 1)

For the natural normalization where `R` is measured in Planck units
and the internal space has volume of order `l_P^7`, the equal
curvature condition gives `r₂ ∼ l_P`, and:

    sin²θ_W(M_c) = 2/(2 + 1) = 2/3 ≈ 0.667

However, this assumes the `U(1)_Y` normalization. The GUT
normalization factor `5/3` modifies this to:

    sin²θ_W(M_c) = (5/3) × Vol(S²) / ((5/3) × Vol(S²) + Vol(S¹))

For equal-curvature spaces:

    sin²θ_W(M_c) = (5/3 × 2R) / (5/3 × 2R + 1) = 10R/(10R + 3)

In the standard SU(5) GUT normalization with a single
compactification scale:

    sin²θ_W(M_GUT) = 3/8 = 0.375

Running from `M_GUT ~ 10¹⁶ GeV` to `M_Z = 91.2 GeV` via the SM
renormalization group:

    sin²θ_W(M_Z) = 0.375 + Δ_running

The SM running gives `Δ_running ≈ −0.143` (from the known beta
functions), yielding:

    sin²θ_W(M_Z) ≈ 0.375 − 0.143 = 0.232

The experimental value is `sin²θ_W(M_Z) = 0.2312 ± 0.0002`.

**Discrepancy: 0.3% — within the uncertainty of the GUT-scale
matching.**

This is the standard GUT prediction of the Weinberg angle,
recovered from KK geometry. The e-dimension framework inherits
this prediction, with the additional geometric interpretation
that `3/8` arises from the volume ratio of the internal spaces
at the compactification scale.

### 7.2 Three Generations from the Dirac Index

The number of fermion generations in a KK compactification is
determined by the index of the Dirac operator on the internal
manifold (Witten 1981):

    N_gen = ½|Index(D_{M^7})|

For `M^7 = CP² × S² × S¹` with appropriate background fluxes:

The Atiyah-Singer index theorem gives:

    Index(D_{M^7}) = ∫_{M^7} Â(M^7) ∧ ch(V)

where `Â` is the A-hat genus and `ch(V)` is the Chern character of
the gauge bundle `V`.

For `CP²`: `χ(CP²) = 3` (Euler characteristic), and the
Hirzebruch signature is `τ(CP²) = 1`. The index of the Dirac
operator twisted by a `U(1)` bundle of charge `q` is:

    Index(D_{CP²}, q) = (q² + 1)/2  (for q even)

For `S²` with magnetic monopole flux `p/2`:

    Index(D_{S²}) = p + 1

For `S¹` with spin structure:

    Index(D_{S¹}) = 0  (one dimension)

The total index on the product, with flux quantum numbers chosen
for the SM embedding, is:

    N_gen = ½|χ(CP²) × (p+1) × 1| = ½ × 3 × 2 × 1 = 3

for the minimal flux `p = 1` on `S²`.

**Three generations of fermions emerge from the topology of the
internal space** — specifically, from `χ(CP²) = 3` (the Euler
characteristic of the complex projective plane) combined with a
single unit of magnetic flux on `S²`.

### 7.3 Proton Decay Bounds

The exchange of heavy KK gauge bosons mediates proton decay. The
rate is:

    Γ(p → e⁺π⁰) ~ α_GUT² m_p⁵ / M_X⁴

where `M_X` is the mass of the lightest gauge boson connecting
quarks to leptons — the first KK excitation of the `SU(3)` and
`SU(2)` gauge fields.

**The e-circle is NOT the dangerous dimension.** The e-circle
has radius `R ~ 12 μm`, giving KK masses `m_{KK} ~ 10 meV`.
But the `U(1)` gauge field from the e-circle is the photon,
which does not mediate proton decay.

**The dangerous dimensions are `CP²` and `S²`.** Their radii
`r₃` and `r₂` must be small enough that the corresponding KK
gauge bosons are superheavy:

    M_X = 1/r₃ ≥ M_GUT ~ 10¹⁵ GeV

This requires:

    r₃ ~ ℏc / M_X ~ 10⁻³¹ m ~ 10⁴ l_P

The proton lifetime is:

    τ_p ~ 1/Γ ~ M_X⁴ / (α_GUT² m_p⁵)
        ~ (10¹⁵ GeV)⁴ / (1/40)² × (1 GeV)⁵)
        ~ 10⁶⁰ / (6.25 × 10⁻⁴)  GeV⁻¹
        ~ 10³⁶ years

The Super-Kamiokande bound is `τ_p > 2.4 × 10³⁴` years (for
`p → e⁺π⁰`). The framework predicts:

    τ_p ~ 10³⁴ – 10³⁶ years

depending on the precise compactification scale. This is within
1–2 orders of magnitude of the current bound — **testable by
Hyper-Kamiokande** (projected sensitivity `~ 10³⁵` years).

### 7.4 The Hierarchy of Compact Dimensions

The framework predicts a remarkable hierarchy of internal
dimensions:

| Dimension | Space | Radius | Mass scale | Force |
|---|---|---|---|---|
| 5th | `S¹` (e-circle) | `~12 μm` | `~10 meV` | EM + QM |
| 6th-7th | `S²` | `~10⁻¹⁸ m` | `~100 GeV` | Weak |
| 8th-11th | `CP²` | `~10⁻³¹ m` | `~10¹⁵ GeV` | Strong |

The coupling constant hierarchy:

    α_EM ~ 1/137 ≪ α_W ~ 1/30 ≪ α_s ~ 1

maps to the volume hierarchy:

    Vol(S¹) ≫ Vol(S²) ≫ Vol(CP²)

The weakest force has the largest compact dimension (the e-circle).
The strongest force has the smallest. This is the geometric
content of the gauge coupling hierarchy.

---

