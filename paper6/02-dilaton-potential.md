# 2. The Dilaton Potential

## 2.1 The Two Terms

The dilaton potential is the sum of two contributions, both
derived in Paper 1:

**The Casimir term** (Paper 1, §6.6):

    V_Casimir(φ) = V₀/φ⁴

This is the vacuum energy of bulk fields (graviton + 3 bulk
right-handed neutrinos) on the e-circle of radius `R = R₀φ`.
It scales as `1/R⁴ ∝ 1/φ⁴` — a steep, repulsive potential that
dominates at small `φ` (small e-circle radius).

**The Goldberger-Wise term** (Paper 1, §6.6; Goldberger & Wise 1999):

    V_GW(φ) = A φ⁴ (ln φ)²

This is the stabilization potential from a bulk scalar with boundary
conditions on the Z₂ orbifold fixed points. It grows at large `φ`
(large radius), providing the restoring force that prevents the
e-circle from expanding indefinitely.

**The full potential:**

    V(φ) = V₀/φ⁴ + A φ⁴ (ln φ)²

## 2.2 The Minimum

The minimum at `φ = φ_min = 1` (by normalization convention)
satisfies `V'(φ_min) = 0`:

    −4V₀/φ_min⁵ + 4Aφ_min³(ln φ_min)² + 2Aφ_min³ ln φ_min = 0

At `φ_min = 1`: `ln(1) = 0`, so the equation reduces to
`V₀ = 0` — which means we need `φ_min` slightly away from 1.
The exact location depends on the ratio `V₀/A`. The minimum is
at `φ_min` where the Casimir repulsion balances the GW attraction.

The mass at the minimum:

    m_φ² = V''(φ_min) ~ V₀/φ_min⁶ ~ ℏc/R₀⁴ × (R₀/l_Pl)²

For `R₀ ≈ 10 μm`: `m_φ ~ 10–20 meV` (Paper 1, Appendix I).

## 2.3 The Three Regimes — Mapped onto Cosmology

**Regime I: The Casimir plateau** (`φ ≪ φ_min`)

For `φ → 0`, the potential approaches `V → V₀/φ⁴ → ∞`. But for
moderate `φ ≪ φ_min`, the potential is nearly flat: `V ≈ V₀ ×`
(slowly varying function). This flat plateau supports slow-roll
inflation. The e-circle is LARGE during inflation — the fifth
dimension is macroscopic.

**Regime II: The oscillation basin** (`φ ≈ φ_min`)

After inflation, the dilaton rolls into the potential minimum and
oscillates. These oscillations are the reheating phase — the
dilaton's kinetic energy is converted to particle production
through its gravitational coupling to the Standard Model. The
e-circle settles to its equilibrium size `R₀ ≈ 10 μm`.

**Regime III: The thawing slope** (`φ > φ_min`)

At late times (the current epoch), the dilaton has rolled slightly
past the minimum and is slowly climbing the GW potential on the
other side. This slow roll produces the dark energy equation of
state `w₀ = −0.85`, `w_a = −0.23` (Paper 2, Appendix F). The
e-circle is slowly growing — the fifth dimension is expanding.
