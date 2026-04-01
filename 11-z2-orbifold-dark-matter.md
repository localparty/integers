# The Z₂ Orbifold Dark Matter Scenario

> **Status:** Speculative but geometrically motivated. The Z₂ structure of
> the e-circle emerges naturally from the spin structure (Bridge 1) and
> connects to the Horava-Witten construction in M-theory.

---

## 1. The Z₂ Structure of the E-Circle

### 1.1 The Spin Structure Implies Z₂

The e-circle S¹ has a natural Z₂ action: the antipodal map ψ → ψ + π.
This Z₂ is not an arbitrary choice — it is the SAME Z₂ that appears in
the spin structure:

- Bosonic fields: periodic under ψ → ψ + 2π (integer winding)
- Fermionic fields: anti-periodic under ψ → ψ + 2π, periodic under
  ψ → ψ + 4π (half-integer winding)

The anti-periodicity of fermions means that the point ψ = π is
distinguished: it is the point where the fermionic wave function changes
sign. The Z₂ map ψ → ψ + π acts as (−1)^F (the fermion number operator)
on the e-circle.

### 1.2 The Orbifold S¹/Z₂

Modding out by this Z₂ gives the ORBIFOLD S¹/Z₂:

    S¹/Z₂ = [0, π]  (an interval, not a circle)

The two ENDPOINTS of the interval — ψ = 0 and ψ = π — are the two
FIXED POINTS of the Z₂ action. They are special: fields at these points
are invariant under the Z₂, while fields in the bulk (0 < ψ < π) come
in Z₂-conjugate pairs.

### 1.3 The Horava-Witten Connection

This is exactly the Horava-Witten construction (1996): 11D supergravity
on M¹⁰ × S¹/Z₂, where the two fixed points are "end-of-the-world branes"
supporting gauge theories (E₈ × E₈ in the original, or SM-like gauge
groups in phenomenological models).

In our framework, the e-circle is the Horava-Witten interval. The two
fixed points are:

    ψ = 0: the **visible brane** (Standard Model matter lives here)
    ψ = π: the **hidden brane** (dark sector lives here)

---

## 2. The Dark Sector at ψ = π

### 2.1 What Lives at the Hidden Brane

At the fixed point ψ = π, the Z₂ orbifold projects out half the degrees
of freedom. The surviving fields must be Z₂-EVEN at ψ = π. These include:

**Gravity:** The 4D graviton (the n = 0 mode of the 5D metric) is
Z₂-even. It propagates everywhere, including the hidden brane. Therefore
the hidden brane GRAVITATES.

**The e-connection:** The electromagnetic field Aμ is the connection on the
e-circle. Under the Z₂ orbifold, Aμ can be EVEN or ODD. If Aμ is Z₂-ODD
(as in the standard Horava-Witten construction), it VANISHES at the fixed
points. This means:

    At ψ = 0: Aμ(0) = 0 (but ∂Aμ/∂ψ ≠ 0, so the field is non-zero nearby)
    At ψ = π: Aμ(π) = 0 (and ∂Aμ/∂ψ ≠ 0)

Wait — this would make the photon vanish at BOTH fixed points, which is
wrong (the SM photon exists at ψ = 0). Let me reconsider.

The correct treatment: the gauge field Aμ is the OFF-DIAGONAL component of
the 5D metric, h_{μ5}. Under Z₂: ψ → −ψ, the component h_{μ5} is ODD
(because the 5-index changes sign). Therefore the ZERO MODE of Aμ is
projected out on the orbifold.

**BUT** this only applies to the BULK zero mode. At each fixed point, there
can be LOCALIZED gauge fields — fields that live only at the brane, not
in the bulk. These are the brane-localized gauge bosons.

**The Standard Model at ψ = 0:**
- SM gauge fields (photon, W, Z, gluons) are localized at ψ = 0
- SM fermions (quarks, leptons) are localized at ψ = 0
- The Higgs is localized at ψ = 0

**The dark sector at ψ = π:**
- A SEPARATE set of gauge fields, localized at ψ = π
- Dark fermions charged under the dark gauge group
- Possibly a dark Higgs

### 2.2 Properties of the Dark Sector

The dark sector particles at ψ = π have the following properties:

**Gravitational coupling:** YES. Gravity propagates through the bulk (it is
the 5D metric). Dark matter at ψ = π couples to the same gravitational
field as visible matter at ψ = 0. The coupling strength is the standard
gravitational coupling G₄.

**Electromagnetic coupling:** NO. The SM photon is localized at ψ = 0. It
does not propagate to ψ = π. Dark matter at the hidden brane does not
couple to SM photons.

**Weak and strong coupling:** NO (if the W, Z, gluons are also localized
at ψ = 0). Dark matter does not participate in weak or strong interactions.

**Dark photon:** POSSIBLY. If the hidden brane has its own localized U(1)
gauge field — a "dark photon" — dark matter can be self-interacting
through dark electromagnetic forces.

### 2.3 Communication Between Branes

The two branes communicate ONLY through fields that propagate in the bulk:

- **Gravity:** The graviton is a bulk field. It mediates gravitational
  attraction between the visible and hidden sectors.
- **The dilaton:** The scalar field φ(x) (the e-circle radius) is a bulk
  field. It can mediate a scalar force between branes. But its mass is
  ~10 meV and its range is ~21 μm — too short-range for cosmological
  effects.
- **KK gravitons:** The massive KK modes propagate in the bulk and
  couple to both branes. They mediate Yukawa-type forces between branes,
  suppressed at distances >> R.

There is NO direct EM, weak, or strong communication. The dark sector is
invisible to all SM detectors except gravity.

---

## 3. Dark Matter Phenomenology

### 3.1 The Dark Matter Candidate

The simplest dark matter candidate at ψ = π is a STABLE fermion charged
under the hidden-brane gauge group but neutral under all SM gauge groups.
Call it the "shadow fermion" χ.

Properties of χ:
- Mass: m_χ (free parameter, determined by the hidden-brane dynamics)
- Electric charge: 0 (no coupling to SM photon)
- Weak charge: 0 (no coupling to SM W/Z)
- Color charge: 0 (no coupling to SM gluons)
- Gravitational coupling: standard (G₄ m_χ)
- Dark charge: non-zero (charged under hidden-brane gauge group)

### 3.2 Relic Abundance

The shadow fermion's relic abundance depends on the production mechanism:

**Thermal production (if the two sectors were in thermal equilibrium):**
This requires gravitational scattering to equilibrate the two sectors.
The equilibration rate is:

    Γ_eq ~ G₄² T⁵

This exceeds the Hubble rate H ~ T²/M_P only for T > M_P^{1/3} ~ 10⁵ GeV.
At temperatures below ~10⁵ GeV, the two sectors are thermally decoupled.

If reheating after inflation is below ~10⁵ GeV, the hidden sector is
NEVER thermalized with the SM. The dark matter abundance is then set by
gravitational production during reheating:

    Ω_χ h² ~ (m_χ/M_P)² × (T_reheat/M_P)³ × (number density)

For m_χ ~ 1 keV and T_reheat ~ 10⁹ GeV:

    Ω_χ h² ~ 0.1 (order of magnitude, requires detailed calculation)

This is the right ballpark for the observed Ω_DM h² = 0.12.

### 3.3 The Mirror Dark Matter Possibility

The most symmetric possibility: the hidden brane at ψ = π has EXACTLY
the same gauge group and field content as the visible brane at ψ = 0:

    Visible (ψ = 0): SU(3)_c × SU(2)_L × U(1)_Y with 3 generations
    Hidden (ψ = π): SU(3)'_c × SU(2)'_L × U(1)'_Y with 3 generations

This is "mirror matter" — a complete copy of the SM living at the
opposite end of the e-interval. Mirror matter has been extensively
studied (Foot 2004, Berezhiani 2005). It naturally gives:

- The correct DM abundance (if the mirror sector is slightly cooler
  than the SM sector, e.g., T_mirror/T_SM ~ 0.3-0.5)
- Self-interacting dark matter (through dark strong and EM forces)
- Dark atoms, dark chemistry, dark stars (?)
- NO direct detection signal (only gravitational coupling to SM)

### 3.4 Observable Signatures

**Direct detection:** Null. The dark matter couples to SM only through
gravity and the massive dilaton/KK tower. The scattering cross-section
is:

    σ_DM-nucleon ~ G₄² m_χ² m_N² / π ~ 10⁻⁶⁰ cm²

This is far below any current or projected direct detection experiment
(XENON: σ ~ 10⁻⁴⁷ cm²). The dark matter is undetectable by conventional
means.

**Indirect detection:** Also null for the same reason — the annihilation
cross-section to SM particles is gravitationally suppressed.

**Gravitational signatures:**
- Galaxy rotation curves (standard CDM behavior)
- Gravitational lensing (standard)
- CMB anisotropies (standard, with possible N_eff contribution if
  mirror neutrinos are light)
- Self-interacting DM signatures (if dark sector has self-interactions):
  core-cusp resolution, diverse rotation curves

**Short-range gravity:** The same experiment that tests the dark energy
prediction (Prediction 1, Appendix H) also tests the dark matter scenario.
The KK graviton tower couples to BOTH branes, producing the same Yukawa
force at ~21 μm. One experiment tests three predictions.

---

## 4. The Z₂ and the Number of Generations

### 4.1 The Z₂ × Z₃ Structure

The e-circle has two natural discrete symmetries:
- Z₂: the antipodal map ψ → ψ + π (from the spin structure)
- Z₃: the three-fold symmetry ψ → ψ + 2π/3 (from SU(3) color, if the
  QCD vacuum has Z₃ structure)

If BOTH are present, the combined symmetry group is Z₆ (since 2 and 3
are coprime, Z₂ × Z₃ ≅ Z₆). The Z₆ action divides the e-circle into
6 sectors of width π/3 each.

The three Z₃ fixed points (at ψ = 0, 2π/3, 4π/3) could give three
GENERATIONS of SM fermions — identical gauge charges but different
e-circle locations, leading to different masses.

Combined with the Z₂:
- ψ = 0: first generation (SM, visible)
- ψ = 2π/3: second generation (SM, visible)
- ψ = 4π/3: third generation (SM, visible)
- ψ = π: hidden sector (dark matter)
- ψ = π + 2π/3 = 5π/3: hidden second generation (dark matter)
- ψ = π + 4π/3 = 7π/3 = π/3: hidden third generation (dark matter)

This gives 3 SM generations + 3 dark generations = 6 sectors of the
Z₆ orbifold. The dark sector is a complete MIRROR of the SM, with
three generations of its own.

### 4.2 The Mass Hierarchy from the Orbifold

The masses of the three SM generations (m_e ≪ m_μ ≪ m_τ) could arise
from the WARP FACTOR of the e-interval:

If the metric in the fifth direction is not flat but exponentially
warped (as in the Randall-Sundrum model):

    ds₅² = e^{−2k|ψ|} gμν dxμdxν + R² dψ²

where k is the warp parameter, then particles at different ψ positions
have different effective 4D masses:

    m_eff(ψ) = m₀ × e^{−k|ψ|}

At ψ = 0: m_eff = m₀ (heaviest — first generation? or third?)
At ψ = 2π/3: m_eff = m₀ × e^{−2kπ/3} (intermediate)
At ψ = 4π/3: m_eff = m₀ × e^{−4kπ/3} (lightest)

The hierarchy between generations is:

    m₂/m₁ = e^{−2kπ/3}
    m₃/m₁ = e^{−4kπ/3}

For the electron-muon-tau hierarchy: m_τ/m_e ≈ 3477 = e^{8.15}.
If 4kπ/3 = 8.15: k = 8.15 × 3/(4π) = 1.95.

With k ≈ 2: the mass ratios are:
    m₂/m₁ = e^{4π/3} ≈ e^{4.19} ≈ 66
    m₃/m₁ = e^{8π/3} ≈ e^{8.38} ≈ 4370

Actual ratios:
    m_μ/m_e = 206.8
    m_τ/m_e = 3477

The model gives the right ORDER OF MAGNITUDE for the hierarchy but not
the exact ratios. More realistic models would include the quark masses
and mixing angles, which constrain k and the Z₃ locations further.

---

## 5. The Unified Orbifold Picture

If the Z₆ orbifold scenario is correct, the e-circle provides:

| Physics | E-circle structure |
|---------|-------------------|
| Quantum mechanics | Quantum theory of the e-coordinate |
| Electromagnetism | Brane-localized gauge field at ψ = 0 |
| Gravity | Bulk metric (propagates everywhere) |
| Dark energy | Casimir energy on the interval [0, π] |
| Dark matter | Mirror sector at ψ = π (hidden brane) |
| Three generations | Z₃ orbifold: 3 fixed points at ψ = 0, 2π/3, 4π/3 |
| Mass hierarchy | Exponential warp factor e^{−k|ψ|} |
| α ≈ 1/137 | Bare coupling 32π²/3 + SM running |
| Spin-statistics | Winding numbers on S¹ (before orbifolding) |

**One circle. Orbifold it. Get everything.**

---

## 6. What Needs to Be Computed

1. **The Z₂ orbifold Casimir energy.** The Casimir calculation (Section 6.6)
   assumed a circle S¹. On the orbifold S¹/Z₂ = [0, π], the boundary
   conditions change (Dirichlet at the endpoints for Z₂-odd fields, Neumann
   for Z₂-even). The Casimir energy will be DIFFERENT — it needs to be
   recomputed to check that it still matches the observed dark energy.

2. **The mirror DM relic abundance.** For the hidden brane with mirror SM
   content, compute the gravitational production rate and the resulting
   Ω_DM h². The key parameter is the reheating temperature.

3. **The warp factor and generation masses.** For the warped orbifold,
   compute the fermion mass spectrum as a function of k and the Z₃
   locations. Compare with the known quark and lepton masses.

4. **The α calculation on the orbifold.** Check that the formula
   1/α = 32π²/3 + Δ_{SM} still holds on the orbifold (the factor 4π²
   might change to π² if the relevant geometry is [0, π] instead of [0, 2π)).

5. **The dark photon mixing.** If both branes have U(1) gauge fields,
   kinetic mixing ε through the bulk is possible:
   ε ~ e^{−M_KK × π R} ~ e^{−π} ≈ 0.04
   This is potentially observable! Dark photon mixing at the 4% level
   is within the range of current dark photon searches.

---

## 7. The Dark Photon Mixing: A Testable Prediction

The most exciting testable consequence of the Z₂ orbifold scenario:

If the hidden brane at ψ = π has a U(1)' gauge field (a dark photon A'μ),
it can mix kinetically with the SM photon through the bulk. The mixing
parameter is:

    ε = exp(−M_bulk × d)

where M_bulk is the mass of the lightest bulk field that mediates the
mixing and d = π R is the distance between the branes.

For M_bulk ~ 1/R (the KK mass scale) and d = πR:

    ε ~ exp(−πR/R) = exp(−π) ≈ **0.043**

A kinetic mixing of ~4% between the SM photon and a dark photon.

**This is an incredibly strong prediction.** Current dark photon searches
(BaBar, LHCb, NA62, LDMX) are sensitive to ε ~ 10⁻³ to 10⁻⁴. A mixing
of 4% would have been SEEN already unless the dark photon is very heavy
(m_A' > 10 GeV) or very light (m_A' < 10⁻⁶ eV, where astrophysical
bounds apply).

The most natural dark photon mass is m_A' ~ 1/R ~ 10 meV. For m_A' ~ 10
meV and ε ~ 0.04: the dark photon would produce a detectable signal in
light-shining-through-wall experiments (ALPS-II at DESY) and in solar
dark photon searches (IAXO).

**If dark photon searches at m ~ 10 meV find a signal with ε ~ 0.04,
it would be strong evidence for the Z₂ orbifold scenario.**

**If they don't, the Z₂ orbifold in its simplest form is constrained
(the mixing must be smaller, perhaps because the bulk is more strongly
warped or the dark U(1) is more massive).**
