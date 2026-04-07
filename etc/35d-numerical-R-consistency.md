# 35d. Numerical Consistency Check: m_ν/m_KK = 5/2 vs Dark Energy R₀

**Date:** 2026-04-07
**Status:** Numerical check complete — conjecture is INCONSISTENT with dark energy constraint

---

## Setup and Constants

- ħc = 0.19732698 eV·μm  (exactly: 197.3269804 MeV·fm)
- Δm²_{23} = 2.515 × 10⁻³ eV²  (NuFIT 5.3, 2023, best-fit atmospheric splitting)
- m_ν = √(Δm²_{23}) = 50.150 meV  (atmospheric scale)
- ρ_Λ = (2.25 meV)⁴ = 2.563 × 10⁻¹¹ eV⁴  (observed dark energy density)
- Casimir coefficient: 3ζ(5)/(64π⁶) = 5.0558 × 10⁻⁵  (with ζ(5) = 1.036928)

---

## Task 1: R from the Conjecture m_ν/m_KK = 5/2

**Conjecture:** m_ν^{atm} / m_KK = 5/2, with m_KK for the k=2 KK mode.

**KK mass formula:** For mode k on S¹ of radius R:

    m_KK = k / (2πR)

For k = 2:

    m_KK = 2 / (2πR) = 1 / (πR)

**Setting m_ν / m_KK = 5/2 and solving for R:**

    m_ν / (1/(πR)) = 5/2
    m_ν × πR = 5/2
    R = 5 / (2π m_ν)

**Converting to μm** using ħc = 0.19733 eV·μm (so R[μm] = R[eV⁻¹] × ħc):

    R [μm] = (5 / (2π)) × (ħc / m_ν)
           = 0.79577 × (0.19733 eV·μm / 0.050150 eV)
           = 0.79577 × 3.9348 μm

    **R_conj = 3.131 μm**

Step-by-step:
- 5/(2π) = 0.79577
- ħc/m_ν = 0.19733 / 0.050150 = 3.9348 μm
- R = 0.79577 × 3.9348 = 3.131 μm

---

## Task 2: Dark Energy Prediction for R₀

From paper4/07-predictions.md §7.21, the Casimir energy on S¹/Z₂ is:

    V_orb = −ΔN × 3ζ(5) / (64π⁶ R⁴)

where ΔN = N_B − (15/16)N_F. Setting |V_orb| = ρ_Λ = (2.25 meV)⁴:

    R⁴ = ΔN × 3ζ(5) / (64π⁶ ρ_Λ)

Computed results from paper (reproduced numerically):

| Field content | ΔN_eff | R (computed) |
|---|---|---|
| Orbifold: graviton + 3ν_R (15 d.o.f.) | 2.60 | 9.39 μm |
| **Witten-index-matched (55B = 55F)** | **3.44** | **10.07 μm** |
| 11D SUGRA circle (128B + 128F) | 8.00 | 12.44 μm |

The papers adopt **R₀ = 10.1 ± 1.5 μm** (central value from Witten-index calculation, §7.21.11).
The SUGRA result R* = 12.4 μm is described as the "rigorous" result in §7.21.4, but
the Witten-index-matched R = 10.1 μm is the central observational estimate.

The formula from paper6/02-dilaton-potential.md §2.3 is:

    ρ_Λ = V(R₀) = c/R₀⁴,    c = ΔN × 3ζ(5)/(64π⁶)

This determines R₀ from the observed ρ_Λ — it is an input constraint, not a prediction.

---

## Task 3: Consistency of the Two R Values

| Source | R value |
|---|---|
| m_ν/m_KK = 5/2 (m_ν = 50.15 meV, k=2) | **3.131 μm** |
| Dark energy, ΔN=3.44 (Witten central) | **10.07 μm** |
| Dark energy, ΔN=2.60 (orbifold lower) | 9.39 μm |
| Dark energy, ΔN=8.00 (SUGRA upper) | 12.44 μm |

    Ratio: R_conj / R_DE = 3.131 / 10.07 = 0.311

    Discrepancy: (R_conj − R_DE) / R_DE = −69.0%

**The two values differ by a factor of 3.23.** They are NOT consistent.

The conjecture R ≈ 9.87 μm cited in the task preamble cannot be correct for
m_ν = 50 meV with k=2. A value near 9.87 μm would require m_ν ≈ 15.8 meV
(see Task 5 below).

---

## Task 4: Implied ρ_Λ if R = R_conj = 3.131 μm

If R = 3.131 μm, the Casimir energy gives (using ΔN = 3.44):

    R_conj in eV⁻¹: 3.131 μm / 0.19733 eV·μm = 15.868 eV⁻¹
    
    ρ_Λ(implied) = 3.44 × 5.0558×10⁻⁵ / (15.868)⁴
                 = 1.739×10⁻⁴ / 6.336×10⁴
                 = 2.743 × 10⁻⁹ eV⁴

    ρ_Λ(implied)^{1/4} = 7.24 meV

**Comparison:**

    Observed:  ρ_Λ^{1/4} = 2.25 meV
    Implied:   ρ_Λ^{1/4} = 7.24 meV    (if R = 3.131 μm)
    
    Ratio: 7.24 / 2.25 = 3.22×

The implied dark energy density is ρ_Λ ∝ R⁻⁴, so the ratio of densities is:

    ρ_Λ(implied) / ρ_Λ(obs) = (R_DE/R_conj)⁴ = (10.1/3.131)⁴ = 108×

If R = 3.131 μm (from m_ν/m_KK = 5/2 with m_ν = 50 meV), the implied dark energy
density is **108× larger** than observed. The framework is not consistent.

---

## Task 5: Scan — Can Both Constraints Be Simultaneously Satisfied?

For simultaneous satisfaction of both m_ν/m_KK = 5/2 AND ρ_Λ = c/R⁴ (at observed ρ_Λ),
we need R_conj = R_DE = 10.1 μm:

    R = 5ħc / (2π m_ν) = 10.1 μm
    m_ν = 5ħc / (2π × 10.1 μm)
        = 5 × 0.19733 / (2π × 10.1)
        = 0.98665 / 63.46
        = 0.015547 eV = **15.55 meV**

The atmospheric neutrino mass is 50.15 meV, which is **3.23× larger** than required.

**Scan table** (all rows satisfy m_ν/m_KK = 5/2 exactly by construction):

| m_ν (meV) | R_conj (μm) | m_KK (meV) | impl. ρ_Λ^{1/4} (meV) |
|---|---|---|---|
| 10.0 | 15.70 | 4.00 | 1.44 |
| 15.5 | 10.13 | 6.22 | 2.25 ← **simultaneous solution** |
| 20.0 | 7.85 | 8.00 | 2.89 |
| 30.0 | 5.23 | 12.00 | 4.33 |
| 50.0 | 3.14 | 20.00 | 7.22 |
| 86.0 | 1.83 | 34.40 | 12.41 |
| 100.0 | 1.57 | 40.00 | 14.43 |

**Key finding:** The unique m_ν where both constraints are simultaneously satisfied is
**m_ν = 15.55 meV**. This is not the atmospheric mass scale (50 meV), but it lies
within the range of possible normal-ordering neutrino masses (the lightest neutrino
mass could be anywhere from 0 to ~50 meV in NH). However, √(Δm²_{23}) = 50 meV
is the atmospheric splitting, not the lightest mass — so the conjecture would need
to reference a different neutrino mass eigenstate.

---

## Task 6: Actual Ratio m_ν/m_KK at R₀ = 10.1 μm

**With m_ν = 50 meV (approximate) and k=2 (m_KK = 1/(πR)):**

    R₀ = 10.1 μm
    R₀ in eV⁻¹ = 10.1 / 0.19733 = 51.18 eV⁻¹
    
    m_KK(k=2) = 1/(π × 51.18 eV⁻¹) = 6.219 × 10⁻³ eV = 6.219 meV
    
    m_ν / m_KK = 50.00 meV / 6.219 meV = 8.040

**With m_ν = √(Δm²_{23}) = 50.150 meV (NuFIT 5.3 exact):**

    m_ν / m_KK = 50.150 meV / 6.219 meV = **8.064**

**With k=1 (lightest KK mode, m_KK = 1/(2πR)):**

    m_KK(k=1) = 1/(2π × 51.18 eV⁻¹) = 3.110 meV
    m_ν / m_KK(k=1) = 50.150 / 3.110 = **16.13**

**Summary of actual ratio:**

    Conjectured:    m_ν/m_KK = 5/2 = 2.500
    Actual (k=2):   m_ν/m_KK = 8.064   (222.6% above 5/2)
    Actual (k=1):   m_ν/m_KK = 16.13   (545% above 5/2)

The actual ratio at the dark energy radius is **8.06**, not 5/2.

---

## Error Analysis: Where Did the Preamble Go Wrong?

The task preamble states: "m_ν/m_KK = 5/2 → R = 9.87 μm (2.3% lower than 10.1 μm)".
This is numerically incorrect. Tracing the algebra:

1. **Correct formula:** From m_ν/m_KK = 5/2 with m_KK = 1/(πR):
   R = 5/(2π m_ν) = 5ħc/(2π m_ν) in μm

2. **With m_ν = 50 meV:**
   R = 5 × 0.19733 / (2π × 0.050) = 0.9867 / 0.3142 = **3.14 μm**

3. **The ~9.87 μm value** cannot come from this formula with m_ν = 50 meV.
   It would require either:
   - A different ratio (not 5/2), OR
   - A factor-of-π² error in the numerics (3.14 × π ≈ 9.87), OR
   - Using m_ν = 15.5 meV instead of 50 meV

4. **The coincidence:** 3.14 μm × π = 9.87 μm exactly. This suggests a missing
   factor of π in an earlier derivation — likely from confusing R vs 2πR
   (circumference vs radius) in the KK mass formula.

---

## Conclusions

1. **R from m_ν/m_KK = 5/2** (m_ν = 50.15 meV, k=2): R = **3.131 μm**

2. **R from dark energy** (Witten-index central value, ΔN = 3.44): R₀ = **10.1 μm**

3. **Discrepancy:** factor of 3.23 (ratio 0.310), the conjecture gives R that is
   69% below the dark energy value. The two are NOT consistent.

4. **Implied dark energy if R = 3.13 μm:** ρ_Λ^{1/4} = 7.24 meV (vs observed 2.25 meV).
   The implied ρ_Λ is 108× larger than observed.

5. **Simultaneous solution:** Both constraints (m_ν/m_KK = 5/2 AND ρ_Λ = c/R⁴) can
   only be satisfied simultaneously if m_ν = **15.55 meV**. This is not the atmospheric
   splitting scale; it could however correspond to the lightest neutrino mass in
   normal hierarchy, but would require a different physical identification.

6. **Actual ratio at R₀ = 10.1 μm:** m_ν/m_KK = **8.06** (not 5/2).

7. **Path 2 agent error:** The claimed "R = 9.87 μm" appears to contain a stray factor
   of π — the actual formula gives 3.14 μm, and 3.14 × π ≈ 9.87. This is likely a
   confusion between the KK mass formula m_KK = k/(2πR) vs k/(R).

---

*Computed with: `/Users/gsix/quantum-geometry-in-5d/etc/age/.venv/bin/python3`*
*Source data: paper4/07-predictions.md §7.21, paper6/02-dilaton-potential.md §2.3*
*NuFIT 5.3 (2023): Δm²_{32} = 2.515 × 10⁻³ eV²*
