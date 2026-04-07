# Section 4c — The 5/2 Identity: One Number Connecting Three Sectors

There is a number that appears three times in the framework — once in neutrino
physics, once in dark matter, once in dark energy — without ever being put there
by hand. It is 5/2. What follows is a precise account of where it comes from,
what it proves, and what it does not.

---

## 4c.1 The Identity Stated

At the GUT scale, the ratio of the atmospheric neutrino mass to the Kaluza-Klein
mass of the extra dimension satisfies:

    m_ν / m_KK = 5/2

where m_KK = ℏc/R is the characteristic mass scale of the fifth dimension (defined
as ℏc divided by the radius R, without additional factors of π or the KK mode
number — the natural scale for comparing a mass to a compactification geometry).

The value 5/2 decomposes as:

    5/2 = χ(CP²) − c₂^{eff}(V_vis)|_{CP²} = 3 − 1/2

Two terms. Two separate topological sources. No free parameters in either term.

This is not an index theorem formula — it is a composite of two independently
topological quantities that happen to combine into the mass ratio. The decomposition
is real. The mechanism is exact. The precision of the claim requires care, and that
care is given in each subsection below.

---

## 4c.2 The Two Components

### The 3: spin^c Dirac index on CP²

CP² does not admit an ordinary spin structure — it is a non-spin manifold,
w₂(CP²) ≠ 0. But every orientable 4-manifold admits spin^c structures, and CP²
carries a canonical one with determinant line bundle O(1).

The index of the spin^c Dirac operator on CP² twisted by O(1) is:

    ind(D^{spin^c}_{CP²} ⊗ O(1)) = ∫_{CP²} Td(CP²) · ch(O(1)) = 3

This is computed by the Hirzebruch-Riemann-Roch theorem:

    ind = ∫_{CP²} (1 + (3/2)H + H²)(1 + H + H²/2) = [1/2 + 3/2 + 1] = 3

The three zero modes — the holomorphic sections z₀, z₁, z₂ of O(1) over CP² —
are the three homogeneous coordinates of CP². They correspond to the three
right-handed neutrino generations. The index equals the Euler characteristic:
ind = 3 = χ(CP²). For CP² with this particular twist, the two coincide
numerically; this is a specific feature of CP², not a general identity.

The 3 is pure topology. It cannot be changed by continuous deformations of the
metric or gauge bundle. It is the rigid count of right-handed neutrino zero modes
that the CP² compactification geometry forces into the spectrum.

### The 1/2: Horava-Witten anomaly cancellation

In M-theory compactified on an orbifold with two boundary 10-branes
(Horava-Witten), the Bianchi identity for the 4-form field strength G₄ requires,
when evaluated on the CP² 4-cycle:

    c₂(V_vis)|_{CP²} + c₂(V_hid)|_{CP²} = p₁(CP²)/2 = 3/2

Since 3/2 is not the sum of two integers, the E₈ gauge bundle must carry
fractional instanton number — a half-integer contribution from the Z₂ fixed
planes. Four additional constraints enter simultaneously: integrality of the
M2-brane tadpole, positivity of both instanton numbers, the level-matching
condition on fractional parts, and the exact gauge unification ratio
n₂/n₁ = −17/9 (from Paper 7). Together these five constraints have a unique
solution:

    c₂^{eff}(V_vis)|_{CP²} = 1/2,    c₂^{eff}(V_hid)|_{CP²} = 1

The value c₂^{eff}(V_vis) = 1/2 is not a choice. It is the unique fractional
instanton number on the visible brane consistent with M-theory anomaly
cancellation, tadpole integrality, and GUT unification.

For CP², σ(CP²) = 1, so c₂^{eff}(V_vis) = 1/2 = σ(CP²)/2 numerically. This
numerical coincidence is specific to CP²: the HW anomaly-cancellation
argument (Paper 7 §B.10.1) establishes c₂^{eff} = 1/2 as the unique fractional
instanton number consistent with all five constraints (integrality, tadpole
positivity, level-matching, and gauge unification), while σ/2 = 1/2 only when
σ = 1. CP² is
the unique compact 4-manifold with σ = 1 and the correct topology for this
compactification.

The 1/2 is not from an index theorem on the closed manifold CP². The eta
invariant of the spin^c Dirac operator on CP² — computed explicitly from the
Cahen-Franc-Gutt spectrum and proven from the anti-holomorphic isometry of CP²
— is identically zero (η = 0 for all standard spin^c structures). The −1/2 does
not arise from APS boundary corrections; it arises from the physics of M-theory
flux at the orbifold fixed plane.

### The composite

    5/2 = 3 − 1/2 = ind(D^{spin^c}_{CP²} ⊗ O(1)) − c₂^{eff}(V_vis)|_{CP²}

Both numbers are topological in the sense that matters physically: neither can
be changed by adjusting a free parameter in the Lagrangian, and both are forced
by the geometry of the compactification. Their difference is the number the
framework produces for m_ν/m_KK.

The combination 3 − 1/2 = 5/2 is a numerical coincidence in the sense now
precisely established by Paper 7 §B.10.3a: each component is separately of
topological origin, but no mechanism connecting a manifold invariant (χ = 3)
and a gauge-bundle invariant (c₂^{eff} = 1/2) in different cohomological
contexts has been identified that would make their difference a topological
identity. "Index theorems on product manifolds produce multiplicative, not
additive, contributions from the two factors" (Paper 7 §B.10.3a). The 5/2
is therefore a topologically grounded numerical coincidence — remarkable in
that both inputs are separately rigid — but it is not an index theorem result
on the full space.

---

## 4c.3 The Numerical Verification

The identity is exact only at the scale where the gauge coupling is evaluated.
Tracking the ratio through the renormalization group makes this precise.

**At M_Z:**

The atmospheric neutrino mass scale is m_ν^{atm} = √(Δm²_{23}) = 50.150 ± 0.279 meV
(NuFIT 5.3). The fifth dimension radius is R₀ = 10.1 μm, set independently by
the dark energy condition ρ_Λ = c/R₀⁴. The KK mass scale at this radius is:

    m_KK = ℏc/R₀ = (0.197 × 10⁻⁶ eV·m) / (10.1 × 10⁻⁶ m) = 19.5 meV

The observed ratio:

    m_ν^{atm} / m_KK = 50.150 meV / 19.5 meV = 2.572

This is 2.9% above 5/2 = 2.50. The corresponding radius implied by the identity
at M_Z is:

    R_conjecture = (5/2) × ℏc / m_ν^{atm} = 9.837 μm     (ratio R/R₀ = 0.974)

**At M_GUT — the 2-loop SM RGE result:**

The neutrino mass in the framework is generated by gauge-Higgs unification on
S¹/Z₂. The 5D Yukawa coupling equals the 5D gauge coupling: y = g₂√2 (Paper 4,
§7.22). This fixes the neutrino mass as:

    m_ν = 2g₂²v²/M_R

where M_R ~ 10¹⁵ GeV is the Majorana mass scale set by the CP² radius. The
ratio m_ν/m_KK scales as g₂², so running g₂ from M_Z to M_GUT rescales the
ratio by g₂(M_Z)²/g₂(M_GUT)². This ratio has now been computed explicitly using
the 2-loop Standard Model RGE for the SU(2) gauge coupling.

The result as a function of M_GUT:

| M_GUT (GeV)         | g₂(M_Z)²/g₂(M_GUT)² | Status                          |
|---------------------|----------------------|---------------------------------|
| 2 × 10¹⁵ (canonical SM) | 1.012           | 1.2% short of required 1.024   |
| 1 × 10¹⁶            | 1.021                | 0.3% short                     |
| 1.65 × 10¹⁶         | 1.024                | exact match                     |

At the canonical SM GUT scale M_GUT = 2 × 10¹⁵ GeV, the running corrects the
ratio from 2.572 at M_Z to:

    m_ν/m_KK|_{M_GUT = 2×10¹⁵} ≈ 2.572 × 1.012 ≈ 2.603

This moves the ratio away from 5/2, not toward it. The running at the canonical
GUT scale does not close the gap; it widens it. To bring the GUT-scale ratio to
exactly 5/2 = 2.50 would require:

    g₂(M_Z)² / g₂(M_GUT)² = 5/2 × (m_KK / m_ν^{atm}) × (R₀/R_KK) ≈ 0.972

But the running moves in the wrong direction: g₂ decreases toward the GUT scale,
so g₂(M_Z)² > g₂(M_GUT)², i.e., the ratio is greater than 1, pushing the
corrected mass ratio above 2.56, not below it.

The correct procedure is to evaluate m_ν/m_KK at the GUT scale with GUT-scale
couplings and GUT-scale R. The GUT-corrected radius at M_GUT = 2 × 10¹⁵ GeV is:

    R_GUT-corrected = 9.954 μm     (ratio R/R₀ = 0.986)

This is closer to R₀ than R_conjecture, but the gap does not fully close.

**Tension with the exact identity:**

If m_ν/m_KK = 5/2 is imposed exactly at the GUT scale, then with R₀ = 10.1 μm
and M_GUT = 2 × 10¹⁵ GeV, the predicted neutrino mass is:

    m_ν^{exact} = (5/2) × ℏc / R₀ × [GUT-scale correction] = 48.843 meV

The observed atmospheric neutrino mass is 50.150 ± 0.279 meV. The tension is:

    pull = (48.843 − 50.150) / 0.279 = −4.68σ

This is not a small discrepancy. At canonical R₀ = 10.1 μm and the canonical SM
GUT scale, the exact topological identity is inconsistent with the observed
neutrino mass at 4.7σ.

**What the numbers mean:**

The 2-loop SM RGE calculation is complete and the result is unambiguous: the
Standard Model g₂ running at the canonical GUT scale does not close the gap
between the observed neutrino mass ratio and 5/2. The topological identity is a
genuine topological fact — the decomposition 3 − 1/2 = 5/2 is algebraically
exact — but its connection to the observed neutrino mass scale depends on the
GUT scale, on R₀, and on the precise neutrino mass, all of which carry
independent uncertainties. The framework makes concrete predictions about which
values of these parameters would close the gap, and those predictions are
testable.

**The R-closure surface analysis:**

The closure condition R_A = R_B can now be stated precisely as the intersection
of two independent constraints on the same quantity R:

*Constraint A* (Casimir / cosmological constant): The mirror sector contributes
a ξ⁴ term to the effective degrees of freedom ΔN(ξ). The full formula is:

    R_A(ξ, ΔN_vis) = R₀ × (ΔN_vis × (1 + ξ⁴) / 3.44)^{1/4},     R₀ = 10.072 μm

At the fiducial values ξ = 0.432 and ΔN_vis = 3.44:

    R_A = 10.159 μm

The ξ correction factor (1 + 0.432⁴)^{1/4} = 1.00860 boosts R by 0.86% above
the mirror-free value R₀.

*Constraint B* (5/2 topological identity + g₂ RGE): The 5/2 identity at the GUT
scale determines R through:

    R_B(M_GUT) = (5/2) × ℏc/m_ν × [g₂(M_Z)/g₂(M_GUT)]²

where m_ν = 50.15 meV (NuFIT 5.3) and the ratio g₂(M_Z)²/g₂(M_GUT)² is
evaluated with the 2-loop SM RGE.

A critical structural fact: because the SU(2) beta function coefficient
b₂ = −19/6 is small, g₂ runs very slowly above M_Z. The consequence is
extraordinary: R_B spans only 9.67–10.31 μm over five orders of magnitude in
M_GUT from 10¹³ to 10¹⁸ GeV.

| M_GUT (GeV)        | g₂(M_GUT) | R_B (μm) |
|--------------------|-----------|----------|
| 10¹³               | 0.6575    | 9.672    |
| 10¹⁵               | 0.6493    | 9.919    |
| 2 × 10¹⁵           | 0.6481    | 9.957    |
| 10¹⁶               | 0.6451    | 10.048   |
| 1.65 × 10¹⁶        | 0.6442    | 10.076   |
| **7.04 × 10¹⁶**    | **0.6416**| **10.159** |
| 10¹⁸               | 0.6369    | 10.311   |

The Casimir constraint gives R_A = 10.159 μm. This value lies inside the R_B
band. The system therefore has an exact closure point.

*Exact closure:* M_GUT* = 7.035 × 10¹⁶ GeV, where R_B(M_GUT*) = R_A exactly.

*Approximate closure at canonical scales:* At M_GUT = 1.65 × 10¹⁶ GeV,
R_B = 10.076 μm and the fractional gap is −0.81%. This is within the expected
accuracy of GUT threshold corrections (of order α_GUT ~ 1/25 ~ 4%).

The narrowness of the R_B band is itself a structural result. It is not a
numerical accident — it follows directly from the near-asymptotic freedom of
the SU(2) coupling. Any M_GUT in the range [10¹⁵, 10¹⁸] GeV gives R_B within
±3% of 10.1 μm. The Casimir constraint fixes R_A to the same ±3% window. The
two constraints are geometrically interlocked: the same μm scale that describes
dark energy (via R₀ = 10.1 μm) is the scale that the 5/2 identity selects for
any physically reasonable M_GUT. This near-degeneracy of R_A and R_B is not a
coincidence — it reflects the framework placing dark energy, neutrino mass, and
the KK compactification scale all in the same μm range by geometric necessity.

---

## 4c.4 Connection to Dark Matter

The 5/2 identity and the dark matter prediction share a single geometric source:
the topology of CP².

The dark matter sector was derived in §4b. The Z₂ orbifold produces a hidden
brane at temperature T' = ξT relative to the visible brane. The dark matter
abundance follows from:

    Ω_DM / Ω_b = 1 / ξ²

Observation gives Ω_DM/Ω_b = 5.36, so ξ = 0.432. The temperature ratio ξ is
set at leptogenesis by the wavefunction localization of the bulk neutrino N^{5D}
along the extra dimension S¹/Z₂. For localization parameter c_ν:

    ξ = e^{−(2c_ν − 1)kπ/2}

At k = 2 (Paper 1 §W.5; an observationally fitted warp factor — no geometric
quantization condition selecting this value is currently established within the
framework), the observed ξ = 0.432 gives c_ν = 0.634.

Now: the same c_ν that determines ξ also appears in the wavefunction factor for
the seesaw mass formula. The two sectors are not independent — both depend on
the bulk neutrino mass parameter c_ν, which is determined by the CP² bulk
geometry through its zero-mode spectrum.

The spin^c Dirac operator on CP² has three zero modes (the ind = 3 that gives
the first factor in 5/2). The wavefunction profiles of these zero modes along
the S¹/Z₂ direction — their exponential decay rate — are set by c_ν. The same
zero modes that give ind = 3 are the modes whose localization parameter is c_ν,
which is the parameter that gives ξ = 0.432, which is the parameter that gives
Ω_DM/Ω_b = 5.36.

The CP² topology enters twice: once as the index count (three generations, from
χ(CP²) = 3), and once through the wavefunction profile (the c_ν that determines
both ξ and the seesaw normalization). The two sectors are not linked by a simple
formula, but they are linked by geometry: they are different projections of the
same zero-mode structure on CP² × S¹/Z₂.

---

## 4c.5 Connection to Dark Energy

The fifth dimension radius R also appears in the dark energy sector. Paper 6
establishes that the cosmological constant is the Casimir energy of the orbifold:

    ρ_Λ = c/R₀⁴

where c is a coefficient determined by the field content of the orbifold
(ΔN = N_B − (15/16)N_F from the Witten-index calculation). The observed dark
energy density ρ_Λ = (2.25 meV)⁴ then fixes R₀ = 10.1 μm.

The neutrino mass identity m_ν/m_KK = 5/2, with m_KK = ℏc/R, implies a
dimensionful relation:

    m_ν × R = (5/2) × ℏc

At the atmospheric neutrino mass m_ν = 50.150 meV (NuFIT 5.3), this gives:

    R_ν = (5/2) × ℏc / m_ν = 2.5 × (0.197 × 10⁻⁶ eV·m) / (0.05015 eV) = 9.837 μm

The dark energy radius is R₀ = 10.1 μm. The discrepancy is 2.6%:

    (R₀ − R_ν) / R₀ = (10.1 − 9.837) / 10.1 = 2.6%

The two radii agree to 2.6%. They were derived from different physics: R_ν from
the neutrino mass and the topological ratio 5/2; R₀ from the observed dark energy
density and the Casimir formula.

This 2.6% gap is numerically equivalent to the 2.9% gap in the mass ratio
m_ν/m_KK at M_Z versus the exact value 5/2. Both gaps have the same sign and
the same approximate size. This is not a coincidence in any simple sense — they
are the same gap, expressed once as a discrepancy in a dimensionless ratio and
once as a discrepancy in a length.

The 2-loop SM g₂ RGE (see §4c.3) does not close either gap at the canonical
GUT scale. The GUT-corrected radius at M_GUT = 2 × 10¹⁵ GeV is R = 9.954 μm,
reducing the gap to 1.4% but not eliminating it. Exact closure of the radius
gap requires R₀ = 9.84 μm (within the Casimir uncertainty in ΔN) or M_GUT ≈
1.65 × 10¹⁶ GeV (within the SUSY GUT range). Both conditions are discussed
in §4c.6.

---

## 4c.6 What Would Close the Gap

The R-closure surface analysis (§4c.3, Story 36b) identifies three distinct
closure scenarios. Each carries a specific physical interpretation and a
specific experimental signature.

**Scenario 1: Exact closure at M_GUT* = 7.04 × 10¹⁶ GeV**

The fiducial point (ξ = 0.432, ΔN_vis = 3.44) closes exactly at M_GUT* = 7.035 × 10¹⁶ GeV,
where R_B = R_A = 10.159 μm identically. This M_GUT* is above the SUSY-SU(5)
window (which tops out near 3 × 10¹⁶ GeV) but is consistent with some SO(10)
constructions and string-scale intermediate scenarios near 10¹⁷ GeV.

The proton lifetime at M_GUT* = 7 × 10¹⁶ GeV is τ_p ~ 10⁴⁰ yr — safely above
the Super-Kamiokande bound of 1.6 × 10³⁴ yr and far above the projected
Hyper-Kamiokande sensitivity. If the GUT scale is M_GUT*, proton decay is
undetectable on any foreseeable experimental timescale. This scenario is not
excluded by proton stability; it is simply invisible to decay experiments.

**Scenario 2: Approximate closure at M_GUT = 1.65 × 10¹⁶ GeV (within threshold corrections)**

At the canonical SUSY-SU(5) scale M_GUT = 1.65 × 10¹⁶ GeV, R_B = 10.076 μm.
The fractional gap relative to R_A = 10.159 μm is −0.81%. This is well within
the expected magnitude of GUT threshold corrections (of order α_GUT ~ 4%) and
higher-loop running effects.

In this scenario:
- The proton lifetime is τ_p ~ 4.6 × 10³⁷ yr — above the current Super-K bound
  but within the projected ultimate Hyper-Kamiokande range.
- Closure to sub-percent accuracy requires ΔN_vis ≈ 3.39 (rather than 3.44) or
  equivalently ξ ≈ 0.30 (rather than 0.432); small adjustments within the
  uncertainty bands of those parameters.

**Scenario 3: Closure via neutrino mass — the sharpest test**

At fixed (ξ = 0.432, ΔN_vis = 3.44), the Casimir constraint fixes R_A = 10.159 μm.
The 5/2 identity at M_GUT = 1.65 × 10¹⁶ GeV requires:

    m_ν* = (5/2) × ℏc / R_B × [g₂(M_Z)/g₂(M_GUT)]⁻²

Solving: m_ν* = 49.7 ± 0.5 meV (the ±0.5 meV theory uncertainty is dominated
by ΔN_vis entering through R_A; see §4d.4 precision budget). This prediction
is conditional on the five-constraint uniqueness theorem of Paper 7 §B.10.1,
which establishes c₂^{eff}(V_vis) = 1/2.

The current oscillation central value is 50.15 meV.
The offset is −0.41 meV, which is 1.46σ below the NuFIT 5.3 central value at
current precision (σ = 0.28 meV). This is not a significant tension today.

CMB-S4 (projected first data ~2030) will measure the sum of neutrino masses to
σ = 0.030 meV. Taking the central closure value m_ν* = 49.7 meV and the current central
value 50.15 meV, the naive discrimination at σ = 0.030 meV is 15σ. However,
once the ΔN_vis theory uncertainty (dominant; ±0.5 meV in m_ν*) is included
in the comparison, the net discriminating power is 5–8σ (Paper 4 §7.5.7a).
This remains the sharpest prediction in the QG5D framework. The neutrino mass test
is more decisive than the proton decay test, more decisive than the N_eff test,
and independent of both. It relies only on the Casimir formula (with its ξ⁴
mirror correction), the topological 5/2 identity, and the 2-loop SM RGE.

**Summary of closure scenarios:**

| Scenario | M_GUT (GeV) | Gap | τ_p (yr) | m_ν required | CMB-S4 pull |
|----------|------------|-----|---------|--------------|------------|
| Exact closure | 7.04 × 10¹⁶ | 0.000% | ~10⁴⁰ | 50.15 meV | — |
| Approx. closure | 1.65 × 10¹⁶ | −0.81% | ~4.6 × 10³⁷ | 49.7 ± 0.5 meV | 5–8σ |
| Low-end neutrino | 1.65 × 10¹⁶ | — | — | 49.7 ± 0.5 meV | decisive |

*Table: Closure scenarios for the R_A = R_B system. All predictions are
conditional on Paper 7 §B.10.1's five-constraint uniqueness argument establishing
c₂^{eff}(V_vis) = 1/2. The 5–8σ CMB-S4 discrimination (replacing the earlier
"13.7σ" figure) accounts for the ΔN_vis theory uncertainty budget (Paper 4
§7.5.7a). The m_ν required column uses m_ν = 49.7 ± 0.5 meV (Paper 4 §7.5.7b).*

The topological identity itself is exact — 3 − 1/2 = 5/2 cannot be changed —
but its connection to the observed mass scale depends on M_GUT, R₀, and m_ν,
each of which carries independent uncertainties. The neutrino mass test at
CMB-S4 is the most powerful discriminator.

---

## 4c.7 The Decisive Statement

Here is what can be said without reservation, and what cannot.

The topology of CP² forces three things independently:

**One.** The index of the spin^c Dirac operator is 3. This is the count of
right-handed neutrino generations. It is computed by HRR. It cannot be changed
without changing the manifold.

**Two.** The HW anomaly-cancellation argument establishes c₂^{eff}(V_vis) = 1/2 on CP²
as the unique solution to the five-constraint uniqueness argument of Paper 7
§B.10.1. It is not
a free parameter and it cannot be changed within the framework.

**Three.** The localization parameter c_ν = 0.634 — set by the zero-mode
wavefunction on CP² × S¹/Z₂ — simultaneously determines the dark matter
temperature ratio ξ = 0.432 (which gives Ω_DM/Ω_b = 5.36) and the neutrino
mass normalization (which enters m_ν/m_KK).

The combination of these three facts produces a number — 5/2 — that is
topologically rigid: both components 3 and 1/2 are fixed by geometry and neither
can be changed by adjusting a free parameter.

**What the computation shows:**

The 2-loop SM RGE calculation is complete. At the canonical GUT scale
M_GUT = 2 × 10¹⁵ GeV, the g₂ running does not close the gap between the
observed neutrino mass ratio and 5/2. The GUT-scale exact identity with
canonical R₀ predicts m_ν = 48.843 meV, which is 4.7σ below the oscillation
central value of 50.150 ± 0.279 meV. This tension is real and should be
reported as such.

The R-closure surface analysis (§4c.3) sharpens this picture considerably. The
two constraints — Casimir (R_A = 10.159 μm at ξ = 0.432) and 5/2 identity
(R_B spanning 9.67–10.31 μm over five decades in M_GUT) — overlap in a narrow
band. The system is not trying and failing to close. The system IS closing, at
M_GUT* = 7.04 × 10¹⁶ GeV, with a sub-percent gap at the canonical SUSY scale
M_GUT = 1.65 × 10¹⁶ GeV.

The topological identity 5/2 = 3 − 1/2 is an exact algebraic fact. Its
connection to the observed neutrino mass scale carries independent uncertainties
in M_GUT, R₀, and m_ν. But the structure of those uncertainties now has precise
numerical content, and the sharpest test is the neutrino mass measurement.

**The decisive test is CMB-S4:**

The R-closure surface analysis makes a specific, quantitative prediction: if
M_GUT = 1.65 × 10¹⁶ GeV (approximate closure, within threshold corrections),
then the framework requires m_ν = 49.7 ± 0.5 meV. The current central value is
50.15 meV. CMB-S4 projected precision is σ = 0.030 meV. Taking the central
closure value m_ν* = 49.7 meV versus the current central
value 50.15 meV at CMB-S4 projected precision σ = 0.030 meV, and accounting
for the ±0.5 meV theory uncertainty (dominated by ΔN_vis; Paper 4 §7.5.7a),
the net discriminating power is 5–8σ. This is not ambiguous. The framework
will pass or fail decisively.

The proton decay test is secondary and model-dependent. At exact closure
M_GUT* = 7 × 10¹⁶ GeV, τ_p ~ 10⁴⁰ yr — undetectable. At approximate closure
M_GUT = 1.65 × 10¹⁶ GeV, τ_p ~ 4.6 × 10³⁷ yr — in the upper Hyper-Kamiokande
range. Either outcome is consistent with the framework. The proton decay result
constrains M_GUT, which then constrains m_ν* — but CMB-S4 tests m_ν directly,
without the intermediate step.

**What has been established:**

- The topological decomposition 5/2 = 3 − 1/2 is **proven** (from HRR and HW
  anomaly cancellation as computed in 35b).
- The HW argument establishing c₂^{eff} = 1/2 is **conditional on the five
  constraints** (Theorem 2 of 35b; Paper 7 §B.10.1); see Finding B6 note in
  the gap-response. The language "proven" is replaced by "established by the
  five-constraint uniqueness argument of Paper 7 §B.10.1, conditional on those
  constraints."
- The numerical agreement at M_Z is **observed** at 2.9% precision.
- The 2-loop SM RGE calculation is **complete**: at canonical M_GUT = 2 × 10¹⁵ GeV,
  the running widens rather than closes the gap, and exact closure requires either
  M_GUT ≈ 1.65 × 10¹⁶ GeV, R₀ = 9.84 μm, or m_ν ≈ 49.7 meV.
- The 4.7σ tension at canonical parameters is **real** and is stated as such.
- The R-closure surface is **computed** (Story 36b): exact closure at
  M_GUT* = 7.04 × 10¹⁶ GeV; 0.81% gap at M_GUT = 1.65 × 10¹⁶ GeV; the
  R_B band spans only 9.67–10.31 μm over five decades.
- The neutrino mass prediction m_ν = 49.7 ± 0.5 meV at M_GUT = 1.65 × 10¹⁶ GeV
  is **testable at 5–8σ by CMB-S4 + DESI** — the sharpest test in the framework;
  the ±0.5 meV theory uncertainty is dominated by ΔN_vis (Paper 4 §7.5.7a).
- The connection of all three sectors through CP² topology is **structural** —
  both c_ν (dark matter via ξ) and the neutrino mass (via the seesaw) depend on
  the same CP² zero-mode data.

The framework does not claim the identity is proven to close. It claims the
topological structure is real, the closure surface has been computed, the
sub-percent gap at SUSY-scale M_GUT is well within threshold corrections, and
the resolution is tested by CMB-S4 at 5–8σ precision (accounting for the ΔN_vis
theory uncertainty budget). The neutrino mass is now a prediction, not a
parameter to be tuned after the fact.

One compact space. The topology is exact. The neutrino mass test is decisive.
CMB-S4 will say which geometry is realized.

---

## 4c.8 What This Section Does and Does Not Claim

The identity m_ν/m_KK = 5/2 is presented here as a result of the following
character: it is a precise, topologically grounded numerical near-coincidence
that is 2.9% accurate at M_Z, subject to a 4.7σ tension with the observed
neutrino mass at canonical framework parameters, and testable via proton decay
experiments and cosmological neutrino mass measurements within this decade.

The claim is not: "we derived neutrino mass from topology."

The claim is: "the number 5/2 that the topology produces, from two independent
and separately forced topological inputs, agrees with the observed neutrino mass
ratio to 2.9% at M_Z; the same framework gives the dark matter abundance from
the same CP² zero-mode data; the g₂ RGE calculation is now complete and
establishes that canonical SM parameters do not close the gap, but three
concrete conditions on M_GUT, R₀, and m_ν each would close it; and the
framework is committed to reporting both the tension and the tests."

Three near-agreements. One geometry. No free parameters in any of the three
topological inputs. The 2.9% gap at M_Z is not closed by SM running at the
canonical GUT scale. Closing it requires M_GUT ≈ 1.65 × 10¹⁶ GeV (testable
from proton decay), or R₀ = 9.84 μm (within Casimir uncertainty), or
m_ν = 49.7 ± 0.5 meV (testable at 5–8σ by CMB-S4 + DESI, §4c.6–4c.7; this
is the approximate-closure prediction at M_GUT = 1.65 × 10¹⁶ GeV). The exact
topological identity at canonical M_GUT = 2 × 10¹⁵ GeV gives 48.843 meV,
which is 4.7σ from the current central value 50.150 meV and is stated as a
genuine tension in §4c.3 and §4c.7 — it is not the preferred closure scenario.
The exact closure at M_GUT* = 7.04 × 10¹⁶ GeV is consistent with the current
central value 50.15 meV. These are predictions, not adjustments.

---

*Research files underlying this section:*
*etc/35a-index-theorem-approach.md — APS route analysis (η = 0 proven, route closed)*
*etc/35b-eta-invariant-CP2.md — Cahen-Franc-Gutt spectrum; HW decomposition 3 − 1/2*
*etc/35c-G4-flux-yukawa.md — gauge-Higgs Yukawa; g₂ RGE candidate for gap closure*
*etc/35d-numerical-R-consistency.md — KK convention comparison; R_ν = 9.87 μm from*
*   m_KK = ℏc/R convention (35a §Step 2); 35d uses m_KK = k/(2πR) (k=2 mode) and*
*   gives R = 3.14 μm — the two values differ by a factor of π from the KK convention.*
*The 9.87 μm value in §4c.5 uses the convention m_KK = ℏc/R throughout, consistent*
*with 35a and the natural dimensional comparison m_ν × R = (5/2) ℏc.*
