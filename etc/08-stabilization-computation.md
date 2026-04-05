# The Stabilization Computation: Results

*Computed April 4, 2026.*

---

## 1. S² Tower Casimir (Route C, §8.3): Does NOT Stabilize

### The result

The S² KK modes at mass `m_l = √(l(l+1))/r₂` contribute to
the S¹ Casimir with exponential suppression `exp(−2πm_l R)`.
The contribution is ALWAYS NEGATIVE (same sign as the zero-mode
Casimir) and decays exponentially for R >> r₂.

V(R) is monotonically increasing from −∞ (at R → 0) to 0 (at
R → ∞). **No minimum.**

### Why: SUSY is exact on S²

S² is simply connected (`π₁(S²) = 0`). There is no
Scherk-Schwarz mechanism on S². SUSY is unbroken for the S²
sector: `N_B(l) = N_F(l)` at every S² level `l`.

Therefore `ΔN_S²(l) = 0` at every level. The S² tower
contributes EXACTLY ZERO to the Casimir.

The same applies to CP²: no spin structure, no SUSY breaking,
no net Casimir. Only S¹ breaks SUSY (through anti-periodic
fermions), and only the S¹ zero modes contribute.

This is exactly what Paper 4 §7.21.2 stated: *"CP²/S²
contributions are SUSY-protected."*

---

## 2. Goldberger-Wise Stabilization (Route C, §4.2): Requires μ ~ 0.4 eV

### The GW potential

    V_total(R) = A exp(−2μπR) − c/R⁴

where `A ~ m_H² M₅²` (from the Higgs-dilaton coupling) and
`c = ΔN × 3ζ(5)/(64π⁶)` (from the Casimir).

The minimum is at:

    R_min ≈ ln(A/c) / (2μπ)

### The numbers

    A ~ (125 GeV)² × (2.5 × 10⁸ GeV)² ~ 10⁵⁷ eV⁴
    c ~ 1.74 × 10⁻⁴ eV⁴
    ln(A/c) ≈ 140

For R_min = 10 μm = 51 eV⁻¹:

    **μ = 140/(2π × 51) = 0.44 eV**

### What this means

The bulk scalar mass μ ~ 0.4 eV is at the meV-eV scale — the
same scale as dark energy (`ρ_Λ^{1/4} = 2.25 meV`) and neutrino
masses (`m_ν ~ 50 meV`).

This is **prima facie circular**: we need μ ~ 1/R to stabilize
R, and 1/R is what we're trying to determine.

But there's a non-circular reading: **the hierarchy R/l_P comes
from the logarithm ln(A/c) ≈ 140.** The GW mechanism generates
an exponentially large R from a modest logarithm of the ratio
of the Higgs scale to the Casimir scale.

| μ (bulk scalar) | R_min | Scale |
|---|---|---|
| m_H = 125 GeV | 3.5 × 10⁻¹⁷ m | weak scale |
| m_b = 4.2 GeV | 10⁻¹⁵ m | fm scale |
| 1 MeV | 4.4 × 10⁻¹² m | pm scale |
| 1 keV | 4.4 × 10⁻⁹ m | nm scale |
| **1 eV** | **4.4 × 10⁻⁶ m = 4.4 μm** | **target** |
| **0.44 eV** | **10 μm** | **target** |
| 50 meV | 88 μm | too large |
| 20 meV | 220 μm | too large |

---

## 3. The Real Question: What Sets μ?

### Option A: μ from the neutrino sector

If the bulk scalar couples to the right-handed neutrino
(which is also a bulk field), its mass could be:

    μ ~ m_ν = 50 meV

But this gives R ~ 88 μm (too large by 10×).

### Option B: μ from the electroweak phase transition

The EW phase transition at T ~ 100 GeV generates a VEV change
Δ⟨H⟩ = v = 246 GeV. The dilaton coupling to Δ⟨H⟩ gives:

    μ² ~ λ_{φH} v² / M₅²

For λ_{φH} ~ 1 and M₅ = 2.5 × 10⁸ GeV:
μ ~ v/M₅ = 246/(2.5 × 10⁸) ~ 10⁻⁶ → μ ~ 1 μeV

Too small (gives R ~ 4 km).

### Option C: μ from the species scale

The species scale (Vafa 2022):

    Λ_species = M_Pl / √(M_Pl R) = M_Pl^{1/2} / R^{1/2}

If μ = Λ_species:
    R = ln(A/c)/(2π Λ_species) = ln(A/c) R^{1/2} / (2π M_Pl^{1/2})

    R^{1/2} = ln(A/c)/(2π M_Pl^{1/2})

    R = [ln(A/c)]² / (4π² M_Pl)

    R = 140² / (4π² × 2.44 × 10²⁷ eV)
      = 19600 / (9.6 × 10²⁸)
      = 2.04 × 10⁻²⁵ eV⁻¹ = 4.0 × 10⁻³² m

Way too small (near Planck scale).

### Option D: μ is a DERIVED quantity

The 140 = ln(A/c) is the large number. The physical content is:

    ln(A/c) = ln(m_H² M₅² / ΔN_Casimir_coeff)

    = 2 ln(m_H) + 2 ln(M₅) − ln(ΔN × 3ζ(5)/(64π⁶))

    = 2 ln(125 GeV) + 2 ln(2.5 × 10⁸ GeV) − ln(1.74 × 10⁻⁴)

    = 2(4.83 + 18.7 × 2.303) + 8.66

    ≈ 2 × 53 + 9 = 115 ... (order of magnitude)

The large logarithm comes from the hierarchy M₅/m_H ~ 10⁶
(the hierarchy between the 5D Planck scale and the Higgs mass).

This is the SAME hierarchy that the Randall-Sundrum model
addresses. In RS: kπR ≈ ln(M_Pl/TeV) ≈ 35. In our framework:
2μπR ≈ ln(A/c) ≈ 140 — about 4× larger because A involves
M₅² rather than M_Pl².

---

## 4. The Honest Assessment

The independent determination of R through stabilization requires
identifying what sets the bulk scalar mass μ ~ 0.4 eV. Three
scenarios:

1. **μ is a new parameter** — the framework trades ρ_Λ for μ.
   This is not a genuine prediction but a reparameterization. The
   CC problem becomes "why is μ ~ 0.4 eV?" — a simpler question
   (only 10 orders from the EW scale, not 122 from Planck).

2. **μ is computed from the framework** — if the dilaton potential
   V_GW arises from a specific coupling (e.g., to the neutrino
   sector or the Higgs), μ is determined. This requires computing
   the dilaton effective potential from the full 11D theory.

3. **μ is unnecessary** — the stabilization comes from a different
   mechanism entirely (flux stabilization, anthropic, Swampland).
   The Vafa Dark Dimension scenario argues for R ~ μm from quantum
   gravity consistency without specifying μ.

**The framework's honest position:** R ~ 10 μm is determined by
ρ_Λ through the Casimir formula (the current approach). The GW
stabilization WOULD give an independent R if μ were determined,
but μ at 0.4 eV requires explanation. The species bound (Route E)
provides a consistency check but not a precise value.

The computation to close this gap: derive V_GW from the 11D dilaton
effective potential, including all brane couplings. This is a
specific, well-defined calculation in 5D supergravity.

---

## 5. What This Teaches Us

The S¹ Casimir can determine ρ_Λ given R, OR determine R given ρ_Λ.
It cannot determine both — one must come from elsewhere.

The framework currently uses ρ_Λ (observed) to fix R. A fully
predictive theory would use the stabilization potential to fix R
and predict ρ_Λ. The gap is the bulk scalar mass μ.

If μ is eventually determined from the 11D geometry, the chain:

    11D SUGRA → ΔN = 8 → Casimir coefficient
    11D dilaton coupling → μ → GW stabilization → R_min
    R_min + ΔN → ρ_Λ = (2 meV)⁴ (PREDICTED)

would be the first derivation of the cosmological constant from
first principles. The CC problem would be solved.
