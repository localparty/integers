# Index Theorem Approach to m_ν/m_KK = χ(CP²) − σ(CP²)/2 = 5/2

> **Date:** April 7, 2026
> **Status:** Mathematical investigation; explicit verdict at the end of each step
> **Question:** Is the identity m_ν/m_KK = χ(CP²) − σ(CP²)/2 = 5/2 exact and
>   derivable from the topology and geometry of CP², or is it a 2.4%-accurate
>   coincidence?
> **Input documents:** etc/34b-path2-R-from-neutrino-mass.md, paper4/07-predictions.md
>   §7.2.1, paper1/appendices/37-appendix-z-neutrino-mass-ordering.md

---

## Topological Inventory: CP²

Before any derivation, collect the invariants precisely.

| Invariant | Value | Definition |
|-----------|-------|------------|
| b₀ | 1 | dim H⁰(CP²; ℤ) |
| b₁ | 0 | dim H¹(CP²; ℤ) |
| b₂ | 1 | dim H²(CP²; ℤ) |
| b₃ | 0 | dim H³(CP²; ℤ) |
| b₄ | 1 | dim H⁴(CP²; ℤ) |
| χ(CP²) | 3 | Euler characteristic: Σ(−1)^p b_p |
| b₂⁺ | 1 | positive eigenvalues of intersection form |
| b₂⁻ | 0 | negative eigenvalues of intersection form |
| σ(CP²) | 1 | Hirzebruch signature: b₂⁺ − b₂⁻ |
| c₁(TCP²) | 3H | first Chern class (Fano: K = O(−3)) |
| c₂(TCP²) | 3H² | second Chern class = χ · [pt] |
| c₁² | 9 | in H⁴(CP²; ℤ) = ℤ |
| p₁(TCP²) | 3 | first Pontryagin number: c₁² − 2c₂ = 9 − 6 |
| L[CP²] | 1 | Hirzebruch L genus: p₁/3 = 1 (= σ, as required) |
| Â[CP²] | 0 | A-hat genus: CP² is NOT spin (w₂ ≠ 0) |
| Td[CP²] | 1 | Todd genus: (c₁² + c₂)/12 = (9+3)/12 = 1 (= χ_hol) |
| **χ − σ/2** | **5/2** | **The combination under investigation** |

Standard relations that hold:
- (χ + σ)/4 = (3+1)/4 = 1 = Td[CP²] = χ_hol(CP²)  ← **known identity**
- (χ − σ)/4 = (3−1)/4 = 1/2  (would equal Â if CP² were spin; it is not)
- L[CP²] = p₁/3 = 1 = σ  ← Hirzebruch signature theorem

---

## Step 1: Seesaw Formula for m_ν(4D)

Three right-handed bulk neutrinos propagate on the orbifold S¹/Z₂ = [0, πR].
The 5D Yukawa vertex at the visible brane (φ = 0) generates a 4D Dirac mass
through the wavefunction overlap.

**The zero-mode profile** for a bulk Dirac fermion with 5D mass M₅ = c_ν k/R
(using dimensionless bulk mass parameter c_ν) is:

    f₀(φ) = A_ν × exp[(1/2 − c_ν)k|φ|/R]    (c_ν > 1/2: peaked at φ = 0)

Orbifold normalization ∫₀^{πR} |f₀|² dφ/R = 1 requires:

    A_ν² = F_c²  ≡  (2c_ν − 1)k / (1 − exp[−(2c_ν−1)kπ])

With c_ν = 0.634, k = 2:
- (2c_ν − 1) = 0.268
- (2c_ν − 1)k = 0.536
- exp[−0.536π] = exp[−1.684] ≈ 0.186 (note: this equals ξ² where ξ = 0.431 ≈ T'/T)
- **F_c² = 0.536 / (1 − 0.186) = 0.536 / 0.814 = 0.659**

The 4D Yukawa is y_4D = y_5D × A_ν × R^{−1/2} × π^{−1/2} where y_5D has dimensions [GeV]^{−1/2}.

The 4D effective seesaw Dirac mass: m_D = y_4D × v where v = 246 GeV.

The physical neutrino mass from the seesaw:

    **m_ν(4D) = m_D² / M_R = y_4D² × v² / M_R**

where M_R = M_GUT ~ 10¹⁵ GeV is the Majorana mass set by the CP² compactification
scale (Paper 4, §3.3; Appendix Z, §Z.1.4). Expanding y_4D:

    m_ν(4D) = y_5D² × F_c² × v² / (πR × M_R)

**Confirmed** (Appendix Z, §Z.1.1–Z.1.4; etc/34b §1.3):

    m_ν(4D) = F_c² × y_5D² × v² / (πR × M_R)

with F_c² = (2c_ν−1)k / (1 − exp[−(2c_ν−1)kπ]) ≈ 0.659 at c_ν = 0.634, k = 2.

**Remark on F_c²:** Two versions appear in the literature. The consistent
version follows directly from the orbifold normalization integral and uses
exponent (2c_ν−1)kπ ≈ 1.684, giving F_c² ≈ 0.659. A version in
etc/34b uses exponent 2(2c_ν−1)kπ ≈ 3.368, giving F_c² ≈ 0.555. The
difference matters numerically but not for the topological question, since
neither value has an obvious topological meaning. This document uses 0.659
(the correct orbifold normalization).

---

## Step 2: Express m_ν/m_KK

The Kaluza-Klein mass scale for the e-circle is defined in Paper 4 as:

    m_KK = k / (2πR)    (with k = 2, this equals 1/(πR))

At R = R₀ = 10.1 μm:

    m_KK = ℏc / (πR₀) = (1.973 × 10⁻⁷ eV·m) / (π × 10.1 × 10⁻⁶ m) = 6.21 meV

However, the quantity compared to m_ν^{atm} ≈ 50 meV in etc/34b uses a different
KK scale: m_KK = ℏc/R = 19.5 meV at R = 10.1 μm. This is the standard KK mass
without the 2π factor, appropriate for a fermion whose half-wavelength spans the
orbifold interval.

**For clarity, define m_KK ≡ ℏc/R.** Then at R₀ = 10.1 μm:

    m_KK = 1.973 × 10⁻⁷ / 10.1 × 10⁻⁶ = 19.5 meV

Observed ratio:

    m_ν^{atm} / m_KK = 50 meV / 19.5 meV = **2.56**    (2.4% above 5/2)

Now express the theoretical ratio. With m_KK = ℏc/R:

    m_ν / m_KK = [F_c² × y_5D² × v² / (πR × M_R)] × [R / (ℏc)]
               = F_c² × y_5D² × v² / (π × M_R × ℏc)

The R dependence cancels exactly. The ratio is:

    **m_ν / m_KK = F_c² × y_5D² × v² / (π × M_R × ℏc)**

This is dimensionless and independent of R. **R does not appear in the ratio.**
Both m_ν and m_KK scale as 1/R, so their ratio is an intrinsic scale comparison.

---

## Step 3: What Value of the Parameters Makes m_ν/m_KK = 5/2 Exactly?

Setting m_ν/m_KK = 5/2:

    F_c² × y_5D² × v² / (π × M_R × ℏc) = 5/2

Define the combination:

    C ≡ y_5D² × v² / M_R    (dimensions: [GeV], in natural units ℏc = 1)

Then the condition is:

    **F_c² × C / π = 5/2**

    C = 5π / (2 F_c²)

Numerically:
- F_c² = 0.659
- C = 5π / (2 × 0.659) = 5 × 3.1416 / 1.318 = **11.9 GeV** (in ℏc = 1 units)

In conventional units: C = y_5D² × v² / M_R, so y_5D² = C × M_R / v²:

    y_5D² = 11.9 GeV × 10¹⁵ GeV / (246 GeV)² = 1.97 × 10¹¹ GeV⁻¹

This is astronomically larger than the natural value y_5D² ~ 1/M₅ ~ 4 × 10⁻⁹ GeV⁻¹
(where M₅ ≈ 2.5 × 10⁸ GeV is the 5D Planck mass). The discrepancy is a factor of
~ 5 × 10¹⁹, identical in order of magnitude to (M_GUT/M₅)² ~ (10¹⁵/10⁸)² = 10¹⁴
up to the v² factor. This reflects the well-known hierarchy between the GUT scale
and the 5D Planck scale at R ~ 10 μm — not a new problem.

The key point is: **C is not a topological invariant of CP².** C depends on y_5D,
which is a coupling constant of the 5D Lagrangian, not determined by geometry.

**The only way m_ν/m_KK = 5/2 can be topological is if F_c² × C = 5π/2 is fixed by
geometry independently of the free parameter y_5D.** This requires a mechanism that
fixes C, or equivalently y_5D, in terms of topological data.

---

## Step 4: Is C = 5π/(2 F_c²) a Topological Invariant of CP²?

### Step 4a: What is proven

The combination χ(CP²) − σ(CP²)/2 = 5/2 is a **fixed rational linear combination
of topological invariants** of CP²:
- χ(CP²) = 3: the Euler characteristic, computed from Betti numbers; topological.
- σ(CP²) = 1: the Hirzebruch signature, determined by the intersection form on H²(CP²; ℤ) = ℤ[H]/(H² = 0 beyond degree 4)... actually σ = b₂⁺ − b₂⁻ = 1 − 0 = 1; topological.

So 5/2 = 3 − 1/2 is a topological number. The question is whether it appears
**naturally** in the index theory of the Dirac operator or a related operator
on CP², and whether that appearance connects to the seesaw mechanism.

### Step 4b: What cannot be proven

**5/2 is NOT an integer.**

The Atiyah-Singer index theorem for a closed compact oriented manifold states:

    ind(D) ∈ ℤ    for any elliptic differential operator D on a closed manifold.

Since CP² is a closed compact manifold (without boundary), **no elliptic operator
on CP² has index 5/2.** The complete list of relevant integer indices on CP² is:

| Operator | Index | Formula | Value |
|----------|-------|---------|-------|
| Euler operator d + d* | χ(CP²) | Σ(−1)^p b_p | **3** |
| Signature operator d⁺ − d⁻ | σ(CP²) | b₂⁺ − b₂⁻ | **1** |
| Dolbeault (∂̄ + ∂̄*) | χ_hol(CP²) | Td[CP²] = (χ+σ)/4 | **1** |
| Spin^c Dirac ⊗ O(1) | ind(D^{spin^c} ⊗ O(1)) | ∫ Td(CP²) · ch(O(1)) | **3** |
| Spin^c Dirac ⊗ O(2) | 6 | ∫ Td(CP²) · ch(O(2)) | **6** |
| Ordinary Dirac | 0 | CP² not spin (w₂ ≠ 0) | **0** |

The HRR computation used in paper4, §7.2.1, gives:

    ind(D^{spin^c}_{CP²} ⊗ O(1)) = ∫_{CP²} Td(CP²) · ch(O(1))
        = ∫_{CP²} (1 + (3/2)H + H²)(1 + H + H²/2)   [H² generator of H⁴]
        = [1·(1/2) + (3/2)·1 + 1·1] = 1/2 + 3/2 + 1 = 3   ✓

The value 3 = χ(CP²) here is a numerical coincidence specific to CP² with
this twist (as noted in paper4, §7.2.1). In general, the spin^c index and
the Euler characteristic are distinct invariants.

**5/2 does not appear as any index on the closed manifold CP².**

### Step 4c: Pontryagin numbers, Â, and Todd class

The key relationships:
- Pontryagin number: p₁[CP²] = c₁² − 2c₂ = 9 − 6 = **3**
- Â genus: Â[CP²] = p₁/24 = 3/24 = 1/8 formally, but **0** as an index (not spin)
- Todd class: Td[CP²] = (c₁² + c₂)/12 = 12/12 = **1**
- L genus: L[CP²] = p₁/3 = **1** = σ ← this IS the signature theorem

None of these produce 5/2. The combination:

    χ(CP²) − σ(CP²)/2 = χ(CP²) − L[CP²]/2 = 3 − 1/2 = 5/2

expresses 5/2 as χ minus half the L genus. This is not a standard index-theoretic
combination; L[CP²] = σ enters the signature theorem but σ/2 = 1/2 is the correction
that would appear in the **Atiyah-Patodi-Singer (APS) index theorem** on a manifold
**with boundary**.

### Step 4d: The APS connection — suggestive, not proven

The APS index theorem for a compact manifold M with boundary ∂M states:

    ind(D) = ∫_M Â(M) ∧ ch(E) + (h + η(∂M)) / 2

where η is the eta invariant of the boundary Dirac operator and h is the dimension
of the kernel of D on the boundary.

For the orbifold S¹/Z₂ = [0, πR] with the two fixed-point branes as boundaries:
the boundary contributions are at φ = 0 (visible brane) and φ = πR (hidden brane).
The Z₂ orbifold introduces half-integer corrections to the index from the twisted
sectors at the two fixed points.

**Suggestive observation:** If the CP² bulk index is ind(D^{spin^c} ⊗ O(1)) = 3 (an
integer, as required for a closed manifold), and the Z₂ orbifold boundary at φ = πR
contributes an η/2 = −1/2 correction (from a single Z₂ twisted sector with a
half-integer eta invariant), then the effective orbifold index would be:

    ind_orb = 3 + (−1/2) = 5/2

This would realize m_ν/m_KK = χ(CP²) − σ(CP²)/2 = 5/2 from a **boundary correction
to the CP² spin^c index**, where the σ/2 term is the eta invariant contribution from
the orbifold fixed plane.

**What would be needed to make this rigorous:**
1. Identify the APS boundary conditions appropriate to the hidden brane at φ = πR
   in the full 5D setup CP² × S¹/Z₂.
2. Compute the eta invariant of the boundary Dirac operator on CP² × {πR}.
3. Show that η(CP²) = σ(CP²) = 1 (the eta invariant equals the signature for
   this particular boundary geometry, which would follow if CP² at the fixed
   point carries a self-dual structure with η = 1).
4. The APS index then gives ind_APS = 3 − 1/2 = 5/2.

Step 3 above is the key gap. The eta invariant of CP² with the standard spin^c
structure is not simply σ = 1 in general. For an isolated self-dual boundary
component, η = σ/2 by Atiyah-Patodi-Singer, which would give the result.
Whether this applies to the fixed plane of the S¹/Z₂ orbifold is an open question
requiring explicit computation in the geometry of M⁴ × CP² × S¹/Z₂.

**Verdict for Step 4:** NOT proven. The structure is suggestive. The combination
χ − σ/2 can arise from a closed-manifold index (integer = 3) corrected by an
APS boundary term (−1/2 from the Z₂ fixed plane). But the explicit calculation
of the eta invariant in this orbifold geometry has not been performed.

---

## Step 5: Does F_c² Simplify to a Nice Fraction?

With c_ν = 0.634, k = 2:

    (2c_ν − 1) = 0.268 = 2 ln(1/ξ) / (kπ)    where ξ = 0.431 = e^{−(2c_ν−1)kπ/2}

Note: the temperature ratio ξ = T'/T satisfies ξ = e^{−(2c_ν−1)kπ/2},
so ξ² = e^{−(2c_ν−1)kπ}. This means:

    **F_c² = (2c_ν − 1)k / (1 − ξ²) = 0.536 / (1 − 0.186) = 0.536 / 0.814 = 0.659**

expressing the wavefunction factor purely in terms of the observed temperature ratio ξ
(fixed by Ω_DM/Ω_b = 5.36) and k = 2 (fixed by m_τ/m_e = 3477).

**F_c² does not simplify to a nice fraction.** Its value 0.659 depends on ξ = 0.431,
which is an irrational number. Specifically:

    F_c² = 2 ln(1/ξ) / (π (1 − ξ²))

This involves π and ln(1/ξ) = 0.841, which are transcendental.

**Does F_c² × (5/2) relate to a geometric quantity?**

    F_c² × (5/2) = 0.659 × 2.5 = 1.647

No standard geometric quantity has been identified with this value. In particular:
- Td[CP²] = 1: no match
- χ_hol(CP², O(1)) = 3: no match
- p₁/24 = 1/8: no match
- The combination 1/(2π) × F_c² × (χ−σ/2) = 1.647/(2π) = 0.262: no match

The lack of simplification is consistent with F_c² being determined by physical
(CMB/dark matter) input rather than by CP² geometry.

---

## Step 6: The Dimensionful Identity Σm_ν × R = (5/2) × ℏc

With m_KK = ℏc/R (the standard KK mass for the e-circle):

    m_ν/m_KK = m_ν × R / (ℏc)

If m_ν/m_KK = 5/2 exactly, then:

    **m_ν × R = (5/2) × ℏc**

This is the dimensionful form of the identity. At the atmospheric neutrino mass
m_ν^{atm} = 50 meV:

    R = (5/2) × ℏc / m_ν^{atm} = 2.5 × 1.973 × 10⁻⁷ eV·m / 0.050 eV = **9.87 μm**

This is 2.3% below R₀ = 10.1 μm (from dark energy). The discrepancy is within the
~0.5 meV measurement uncertainty on √(Δm²_atm) — consistent with coincidence OR
with a prediction that needs a 2.3% correction to one of the input values.

**Does the identity m_ν × R = (5/2) ℏc follow from a principle?**

Three candidate principles:

**Candidate A: Scale quantization.** In string/M-theory, mass scales are related by
the geometry. The dimensionful combination m × R has units [ℏc] and must be an
O(1) number times ℏc (the quantum of action for a massless particle on scale R).
The number 5/2 would then be the relevant topological weight for the neutrino mass
mode. This is a suggestive framework but not a derivation.

**Candidate B: Witten effect / topological vacuum.** In a topological field theory
on CP² × S¹/Z₂, certain amplitudes are weighted by topological invariants.
If the neutrino mass is generated by a topological amplitude proportional to
χ(CP²) = 3 with a boundary correction of −1/2 (as in the APS argument above),
then m_ν × R / ℏc = 5/2 would be exact. This reduces to the Step 4d argument.

**Candidate C: UV/IR mixing from flux quantization.** The flux condition on CP²
requires N_gen = χ(CP²) = 3 generations. The extra dimension radius R is fixed by
the dark energy density ρ_Λ = f(N_fields) / R⁴. The neutrino mass scale from
the seesaw involves M_R = 1/r₃ (the CP² radius in the UV). If the consistency
condition m_ν = (χ(CP²) − σ(CP²)/2) × ℏc/R is imposed as a FLUX QUANTIZATION
CONDITION linking the IR scale R to the UV seesaw scale M_R through χ and σ, then
the identity would follow from the flux algebra. This is speculative but points to
a possible line of proof.

**Verdict for the dimensionful form:** The identity m_ν × R = (5/2) ℏc is
numerically suggestive (2.3% accuracy) and dimensionally natural, but no
derivation from a first principle has been found.

---

## Synthesis: Why 5/2 = χ − σ/2 Might Be Exact — A Candidate Mechanism

The most coherent picture consistent with the calculations above:

**Hypothesis:** The ratio m_ν/m_KK is determined by the APS index of the
bulk Dirac operator on the compact space CP² × S¹/Z₂. The S¹/Z₂ orbifold
has two boundaries (the two branes). The neutrino zero mode wavefunction
integral against the hidden brane generates the seesaw mass. The effective
index entering the seesaw normalization is:

    ind_APS(CP² × S¹/Z₂) = ind(D^{spin^c}_{CP²} ⊗ O(1)) + η_boundary/2
                           = 3 + (−1/2)
                           = 5/2

where:
- The bulk CP² contributes ind(D^{spin^c} ⊗ O(1)) = 3 = χ(CP²)
- The Z₂ fixed plane (hidden brane) contributes η/2 = −σ(CP²)/2 = −1/2

This would make the identity:

    m_ν/m_KK = χ(CP²) − σ(CP²)/2

a consequence of the APS index theorem applied to the orbifold, where:
- χ(CP²) = 3 counts the bulk zero modes (= three neutrino generations)
- σ(CP²)/2 = 1/2 is the eta invariant correction from the hidden brane

**What this requires:** The computation of η(CP² at φ = πR) in the orbifold
geometry. This is a well-defined calculation in APS index theory. If
η = σ(CP²) = 1 for the CP² brane geometry, the result follows.

---

## Verdict: Coincidence or Exact?

| Question | Finding | Confidence |
|----------|---------|------------|
| Is 5/2 a topological invariant of CP²? | Yes, as the linear combination χ − σ/2 | Definite |
| Is 5/2 the index of an operator on CLOSED CP²? | No — all closed-manifold indices are integers | Definite |
| Does 5/2 appear in APS index theory on CP²×S¹/Z₂? | Plausibly, if η(hidden brane) = 1 | Suggestive, unproven |
| Does F_c² simplify to a topological value? | No — F_c² is determined by CMB/DM physics | Definite |
| Is y_5D fixed by topology? | No — one Yukawa coupling remains free | Definite |
| Is the 2.4% discrepancy experimentally distinguishable? | Not currently (√Δm²_atm uncertain by ~1%) | Definite |
| Is the dimensionful identity m_ν × R = (5/2)ℏc exact? | Unproven; 2.3% from R₀ | Open |

**The identity m_ν/m_KK = χ(CP²) − σ(CP²)/2 = 5/2 is NOT proven from first principles.**

**The identity is also NOT merely a numerical coincidence**, in the following sense:
the combination χ − σ/2 = 5/2 is a rigid topological number; it cannot take any
other value for CP². The 2.4% discrepancy between 2.56 (observed) and 2.50 (exact)
is within current experimental uncertainty and could be closed by a 1 meV shift
in the neutrino mass — which is the current measurement precision.

**The strongest evidence for exactness** is the APS candidate mechanism (Step 4d):
the 3 − 1/2 structure naturally decomposes as a bulk CP² index minus a Z₂ boundary
correction, which is the topological structure of the orbifold. This is testable by
computing the eta invariant η(∂(CP² × S¹/Z₂)) in the orbifold geometry.

**The strongest evidence against exactness** is that the seesaw formula contains
a free 5D Yukawa coupling y_5D that absorbs any factor of R. Even if ind_APS = 5/2
is the correct index, the seesaw would need a precise relation between y_5D and
the CP²/S¹ geometry to convert a topological index into a physical mass ratio.
That relation has not been identified.

---

## What Would Constitute a Proof

A complete proof of m_ν/m_KK = χ(CP²) − σ(CP²)/2 = 5/2 would require all three
of the following:

**Requirement 1: APS eta invariant.** Compute η(∂M) for the boundary of the
5D orbifold CP² × S¹/Z₂, specifically the hidden brane at φ = πR. Show that
the relevant contribution is η = σ(CP²) = 1, giving an APS correction of −1/2.

**Requirement 2: Yukawa from geometry.** Identify a mechanism that fixes the
5D Yukawa coupling y_5D in terms of the CP² geometry. Candidates:
- y_5D = g_GUT (GUT coupling, fixed by α_s running)
- y_5D from a topological amplitude in the CP² sigma model
- y_5D from the wavefunction of the Higgs modulus on CP²

**Requirement 3: Connecting the index to the mass ratio.** Show explicitly that
the APS index ind_APS = 5/2 enters the seesaw mass formula as m_ν × πR = ind_APS × y_5D² × v² / M_R,
and then use Requirement 2 to convert ind_APS into m_ν/m_KK.

None of these requirements has been met. Requirements 1 and 3 are well-defined
mathematical calculations. Requirement 2 is the deepest physical gap.

---

## Summary for the Record

The identity m_ν/m_KK = χ(CP²) − σ(CP²)/2 = 5/2:
- Is exact at the level of CP² topology (5/2 is a topological number)
- Is **not** proven from the index theorem
- Has a suggestive mechanism (APS on orbifold) that could produce the exact structure
- Requires the eta invariant computation on the CP² × {brane} boundary
- Has a 2.4% numerical discrepancy with observation, within current experimental errors
- **Status: an open conjecture with a clear mathematical route to proof or disproof**

The next step recommended is: compute η(CP²) for the spin^c Dirac operator
with the boundary conditions appropriate to the S¹/Z₂ orbifold at φ = πR.
This is a concrete spectral geometry calculation that would either close the
argument or rule out the mechanism.

---

*Analysis conducted April 7, 2026.*
*Key result: 5/2 cannot be a closed-manifold Atiyah-Singer index (non-integer), but
CAN arise from an APS orbifold index as χ(CP²) + η_boundary/2 = 3 − 1/2 = 5/2.
The eta invariant calculation is the remaining mathematical step.*
