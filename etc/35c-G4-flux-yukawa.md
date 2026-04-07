# G₄ Flux Quantization, Yukawa Couplings, and m_ν/m_KK = 5/2

> **Date:** April 7, 2026
> **Status:** Research investigation; verdicts marked [COMPUTED], [CONJECTURED], or [RULED OUT]
> **Question:** Can G₄ flux quantization in M-theory (Paper 7) fix the 5D Yukawa
>   coupling y_5D such that m_ν/m_KK = 5/2 exactly — without a free parameter?
> **Input files read:**
>   - paper7/00-abstract.md, 02-g4-flux-on-cp2-s2.md, 03-moduli-minimum.md,
>     04-tadpole.md, appendix-A-theorem-U-star.md, appendix-B-freed-witten.md
>   - paper4/07-predictions.md (§7.22)
>   - etc/34b-path2-R-from-neutrino-mass.md
>   - etc/35a-index-theorem-approach.md

---

## Executive Summary

Paper 7 does not compute any Yukawa coupling from G₄ flux. The flux sector fixes
the *moduli* (internal radii r₂, r₃) and the *gauge coupling ratio* (n₂/n₁ = −17/9),
but the Yukawa couplings are orthogonal degrees of freedom not constrained by the
G₄ superpotential. The neutrino mass prediction in Paper 4 (§7.22) is instead fixed
by *gauge-Higgs unification*: y₄ = g₂√2 from the Wilson line on S¹, giving
m_ν = 2g₂²v²/M_R = 51 meV with no free parameters.

The question of whether flux quantization *separately* fixes m_ν/m_KK = 5/2 is
therefore partly moot for the existing 51 meV prediction — which is already
parameter-free through a different mechanism. However, the flux connection to the
ratio 5/2 is worth investigating as an independent consistency check, and the
answers below reveal a precise structure and a proved obstruction.

---

## Question 1: Does Paper 7 Compute the Yukawa Coupling from G₄ Flux?

**[COMPUTED — Negative]**

Paper 7's G₄ flux sector is governed by the House-Micu superpotential:

    W_total = n₁ r₃² + n₂ r₂² + cR(6r₃²r₂² − 2r₃⁴)

The F-flatness conditions from this superpotential determine:
- The CP² radius: r₃² = n₁/(2cR)
- The radius ratio: ρ² = r₂²/r₃² = −2n₁/[3(n₁ + n₂)]

These are purely *geometric* constraints on the moduli. The superpotential depends
on r₂ and r₃ only — no fermion fields, no Yukawa vertices, no matter wavefunctions
appear in W_total. The Yukawa couplings arise from a separate sector (the fermionic
zero-mode overlap integrals on CP² × S¹/Z₂), which is not part of the G₄ flux
analysis.

**What G₄ flux does fix (Paper 7):**
- n₂/n₁ = −17/9 (GUT unification)
- r₃ ~ M_GUT⁻¹ ≈ 10⁻¹⁵ GeV⁻¹ (through r₃² = n₁/(2cR) with cR ∝ R)
- Inflaton parameters (n_s, r)
- N_M2 = 450 M2-brane charge (from Appendix B Route B: exact tadpole)

**What G₄ flux does NOT fix:**
- The 5D Yukawa coupling y_5D
- Any Yukawa coupling y_ijk from matter overlap integrals
- The seesaw mass directly

The Yukawa coupling in M-theory compactifications is schematically:

    y_ijk = ∫_M ω_i ∧ ω_j ∧ ω_k × (G₄-dependent normalization) / M_Pl^{3/2}

where ω_i are harmonic forms representing matter fields. Paper 7 does not compute
this integral for any specific matter embedding. The "G₄-dependent normalization"
is present in principle but is not evaluated.

**Conclusion:** No Yukawa formula is derived from G₄ flux in Paper 7. The flux
sector is cleanly decoupled from the Yukawa sector in the GVW superpotential.

---

## Question 2: Allowed G₄ Flux Values on CP²

**[COMPUTED — Exact, with Freed-Witten subtlety]**

The G₄ flux expands on two independent 4-cycle classes:

    G₄ = (2πl₁₁³)[n₁ δ_{CP²} + n₂ δ_{CP¹×S²}]

**For the CP² 4-cycle:**

CP² is NOT a spin manifold (w₂(CP²) ≠ 0). The Freed-Witten anomaly (Witten 1996,
DMW 2003) shifts the flux quantization condition from integer to half-integer on
non-spin cycles:

    [G₄/(2π)] − p₁(X)/4 ∈ H⁴(X, ℤ)

For CP², p₁ = 3H², giving a shift of 3/4 of the generator. The physical consequence
is:

    n₁^{phys} = n_{1,int} + 1/2,    n_{1,int} ∈ ℤ

The **minimum non-zero flux on CP²** (absolute value) is:
- n₁^{phys} = 1/2 (from n_{1,int} = 0)

This is a **half-integer shift**, not a choice: n₁ = 1/2 is the minimal allowed
flux.

**For the CP¹ × S² cycle:**

Both CP¹ and S² are spin manifolds (w₂ = 0), so no Freed-Witten shift:

    n₂^{phys} = n_{2,int} ∈ ℤ

**The exact GUT solution (Paper 7, Appendix B, Route B):**

When the five constraints (HW anomaly, level matching, positivity, tadpole
integrality, exact GUT ratio) are imposed simultaneously, the unique solution is:

    c₂^{eff}(V_vis)|_{CP²} = 1/2   →   DMW shift s = 1   →   n₁^{phys} = n_{1,int} + 1 = 18

Specifically: n₁^{int} = 17, n₂ = −34, so physical fluxes are (18, −34) with
ratio −34/18 = −17/9 (exact). N_M2 = 450 (integer, positive).

**Summary of allowed values:**

| Cycle | Spin? | FW shift | Minimum |n| | Physical quanta for GUT |
|-------|-------|----------|-----------------|------------------------|
| CP² | No | +1/2 or +1 (bundle-dependent) | 1/2 | n₁^{phys} = 18 |
| CP¹ × S² | Yes | 0 | 1 | n₂ = −34 |

---

## Question 3: Does the Minimum Flux Give m_ν/m_KK = 5/2?

**[CONJECTURED — not derived, but structure is suggestive]**

This question requires connecting flux quanta to Yukawa couplings, which Paper 7
does not do. However, we can ask whether the *GUT flux configuration* (n₁ = 18,
n₂ = −34) produces a natural Yukawa that gives m_ν/m_KK = 5/2.

**The actual prediction (Paper 4, §7.22):**

The Yukawa coupling in the framework is fixed by gauge-Higgs unification on S¹,
*not* by G₄ flux on CP²:

    y₄ = g₂√2 = 0.92

This gives:

    m_ν = 2g₂²v²/M_R = 2 × (0.65)² × (246 GeV)² / (10¹⁵ GeV) = **51 meV**
    m_KK = ℏc/R = 19.5 meV  (at R = R₀ = 10.1 μm)
    m_ν/m_KK = 51/19.5 = **2.61**

The 5/2 conjecture gives a ratio of 2.50. The discrepancy is 4%.

**If instead one tries to derive y_5D from flux:**

The condition m_ν/m_KK = 5/2 requires (from etc/35a, Step 3):

    F_c² × y_5D² × v² / (π × M_R) = 5/2

with F_c² = 0.659, M_R = 10¹⁵ GeV, v = 246 GeV:

    y_5D² = (5/2) × π × M_R / (F_c² × v²)
           = (5/2) × π × 10¹⁵ / (0.659 × 6.05 × 10⁴)
           = 1.97 × 10¹¹ GeV⁻¹

This is not generated by the GUT flux configuration n₁ = 18. There is no formula
in Paper 7 connecting these numbers.

**Tentative connection (speculative):**

If a flux-Yukawa formula of the form:

    y_5D² ~ n₁^{phys} / (M_Pl × r₃²) ~ 18 / (M_Pl / M_GUT²)

were derived from the G₄ superpotential, it would give a Yukawa at the GUT scale —
but a numerical evaluation shows this does not reproduce y_5D² = 1.97 × 10¹¹ GeV⁻¹
for any natural coefficient. The flux integers alone are insufficient without the
full M-theory three-form overlap integral.

---

## Question 4: The Majorana Mass M_R — Current Value and Origin

**[COMPUTED — from Paper 4]**

The Majorana mass M_R arises from the CP² compactification scale:

    M_R = 1/r₃ ~ M_GUT ~ 10¹⁵ GeV

**How it is fixed:**

r₃ is the CP² radius, determined by the flux minimum equation:

    r₃² = n₁ / (2 cR)

where cR = (64π⁵ c₀/3l₁₁³) × R, with c₀ = 1/42 (G₂ torsion coefficient).

At R = R_obs = 10.1 μm and n₁ = 18 (exact FW solution):

    r₃ ~ (n₁/(2cR))^{1/2} → M_GUT = r₃⁻¹ ≈ 2 × 10¹⁵ GeV

The G₄ flux integer n₁ thus sets M_R through the moduli stabilization.
Doubling n₁ (from 9 to 18 due to the FW exact solution) gives M_GUT ∝ √(n₁)
— the exact GUT solution increases M_GUT by a factor √2 relative to the naive
estimate.

**M_R and G₄ flux — the indirect connection:**

M_R is NOT directly computed from G₄ flux quanta; rather, G₄ flux fixes r₃
(through the F-flat equation), and r₃ then determines M_R geometrically. There
is no direct formula M_R = f(n₁, n₂). The connection is:

    G₄ flux quanta (n₁, n₂)
        → F-flat conditions
        → r₃ (CP² radius)
        → M_R = 1/r₃

This is a two-step indirect chain, not a direct flux-mass formula.

---

## Question 5: A Single Flux Configuration That Fixes y_5D, sin²θ_W, and α_s Simultaneously?

**[PARTIALLY COMPUTED — gauge couplings yes; y_5D no]**

**What the exact GUT flux (n₁ = 18, n₂ = −34) already fixes:**

| Observable | Fixed by flux? | How |
|------------|---------------|-----|
| n₂/n₁ = −17/9 | **Yes** | F-flat conditions, exact |
| ρ = r₂/r₃ = √3/2 | **Yes** | Equivalent to flux ratio |
| α₃/α₂ = 1 at M_GUT | **Yes** | From ρ = √3/2 (Paper 4) |
| sin²θ_W ≈ 0.231 | **Yes** | From SU(5) unification at M_GUT = 1/r₃ |
| α_s(M_Z) | **Yes (indirectly)** | From M_GUT + RG running |
| r₃ ~ 10⁻¹⁵ GeV⁻¹ | **Yes** | r₃² = n₁/(2cR) at R = R_obs |
| y₄ = g₂√2 | **No** | From gauge-Higgs on S¹, not from G₄ |
| y_5D (free parameter) | **No** | Not constrained by Paper 7 flux analysis |
| m_ν/m_KK = 5/2 | **No** | Not derivable from flux alone |

The flux integers (18, −34) do simultaneously fix sin²θ_W, α_s at M_GUT, and
the GUT scale. But the Yukawa sector requires an additional input (gauge-Higgs
unification on S¹) that is independent of the G₄ flux on CP² × S².

**The gauge-Higgs mechanism rescues the parameter count:**

The crucial insight is that in the framework the 5D Yukawa IS fixed — but by a
different topological mechanism than G₄ flux:

    y₅D^{gauge-Higgs} = g₅ = g₂ √(2πR)

The 5D gauge coupling g₅ is the bulk coupling, and in gauge-Higgs unification the
Yukawa vertex equals the gauge vertex. This gives y₄ = g₂√2 exactly (Paper 4,
§7.22.1), independent of flux quanta. So the single-configuration dream is
*realized* — not by flux alone, but by flux plus gauge-Higgs:

    (G₄ flux: n₁=18, n₂=−34) ∪ (gauge-Higgs: y=g₂√2) → all couplings fixed

---

## Question 6: Is m_ν/m_KK = Minimum G₄ Flux Quantum on CP²?

**[RULED OUT in one form; SUGGESTIVE in another]**

**The direct version is ruled out:**

If the statement were "m_ν/m_KK = the minimum physical flux quantum on CP²," then
since the minimum flux is n₁^{phys,min} = 1/2 (from n_{1,int} = 0 with FW shift),
we would need:

    m_ν/m_KK = 1/2 ??

But the observed ratio is 2.56, not 1/2. This literal interpretation fails.

**The GUT flux version:**

The GUT flux has n₁^{phys} = 18 (exact solution) or n₁^{phys} = 19/2 (approximate
FW solution). Neither equals 5/2.

**The ratio-of-flux version:**

However, a more interesting coincidence: the Diophantine obstruction analysis
(Paper 7, Appendix B) shows that the exact GUT condition forces:

    n₁^{int} = 17,   n₂ = −34,   n₁^{phys} = 18

and the Freed-Witten shift to the CP² cycle is +1 (when c₂^{eff} = 1/2). The
ratio of the two physical fluxes is:

    |n₁^{phys}| / |n₂| = 18/34 = 9/17

while the ratio m_ν/m_KK = 2.61 ≈ 5/2 = 2.5. These numbers are not equal.

**What IS 5/2 in the flux context?**

From Paper 7, Appendix B, Table B.10.2: the number 450 = N_M2 = 2 × 225 = 2 × 15²
is the M2-brane charge. Note 450/180 = 5/2. The number 180 would be (n₁ × n₂ product
in some normalization), but this is post-hoc numerology.

More precisely: the GUT flux integers satisfy:

    n₁^{phys} + |n₂| = 18 + 34 = 52
    n₁^{phys} × |n₂| = 18 × 34 = 612

The tadpole N_M2 = 450. None of these directly gives 5/2.

**The structure that IS exact (from Paper 7, Appendix A, §A.5.3):**

    χ(CP²) + η(D_{S¹/Z₂}) = 3 + (−1/2) = **5/2**

where:
- χ(CP²) = 3: Euler characteristic of CP² (counts generations)
- η(D_{S¹/Z₂}) = ζ_R(0) = −1/2: Riemann zeta function at 0, the spectral
  asymmetry (eta invariant) of the Dirac operator on the S¹/Z₂ orbifold with
  Neumann boundary conditions. This is **exact** (not approximate).

This identity is mathematically exact and involves genuine topological/spectral
invariants of the two spaces. The number 5/2 IS the additive combination of:
- A CP² topology number (χ = 3)
- An S¹/Z₂ spectral number (η = −1/2)

However, Paper 7 (Appendix A, §A.5.4) also PROVES that this additive combination
**cannot arise from any spin^c index theorem on CP² × S¹/Z₂**, because:

1. Arithmetic obstruction: spin^c index on CP² twisted by O(k) equals
   (k+1)(k+2)/2; the Kawasaki orbifold halving gives (k+1)(k+2)/4; setting
   this to 5/2 requires (k+1)(k+2) = 10, which has no integer solution.

2. APS boundary correction: for η = −1/2, the APS correction is −(h+η)/2 = +1/4
   (for h = 0), not +1/2.

3. Wilson line independence: flat U(1) bundles do not change the topological index.

**Verdict:** The statement "m_ν/m_KK = χ(CP²) + η(S¹/Z₂)" is an exact mathematical
identity, but CANNOT be derived as the output of an index theorem in the framework.
The additive combination is not achievable from any natural index theory. It remains
a coincidence (at 4% accuracy for the gauge-Higgs value, or 2.4% for the seesaw
value with free Yukawa) without a physical mechanism.

---

## Synthesis: What Flux Does and Does Not Fix

### The complete picture of what G₄ flux quantization fixes:

**Fixed by flux (Paper 7, all derived):**

    n₂/n₁ = −17/9     →  gauge coupling unification
    r₃² = n₁/(2cR)    →  GUT scale M_GUT = 1/r₃
    ρ = r₂/r₃ = √3/2  →  sin²θ_W, α_s at M_GUT
    N_M2 = 450         →  tadpole cancellation

**Fixed by gauge-Higgs on S¹ (Paper 4, independent of flux):**

    y₄ = g₂√2         →  Yukawa coupling (from Wilson line, not G₄)
    m_ν = 2g₂²v²/M_R  →  51 meV, zero free parameters

**Not fixed by either (open):**

    m_ν/m_KK = 5/2 exact   →  4% from gauge-Higgs prediction (2.61)
                                 2.4% from free-Yukawa seesaw (2.56)

### The key structural fact:

The framework already achieves a zero-free-parameter neutrino mass prediction
*without* using flux-Yukawa coupling. The G₄ flux is responsible for M_R (via r₃),
while the gauge-Higgs mechanism on S¹ is responsible for y₄. These are two
orthogonal mechanisms:

    G₄ on CP²: fixes M_R = 1/r₃ ~ 10¹⁵ GeV
    Wilson line on S¹: fixes y₄ = g₂√2
    Together: m_ν = 2g₂²v²r₃ = 51 meV

The question "does G₄ flux fix y_5D?" has a clean answer: no, and it doesn't need
to — the Yukawa is fixed by a different geometric mechanism.

---

## The Conjecture: Can Flux Simultaneously Fix m_ν/m_KK = 5/2?

**[OPEN — requires new mechanism not in Paper 7]**

For the exact ratio 5/2 to emerge from flux quantization without free parameters,
one would need a mechanism that:

1. Modifies the gauge-Higgs Yukawa from y₄ = g₂√2 (giving m_ν/m_KK = 2.61)
   to y₄_corr such that m_ν/m_KK = 2.50 exactly; or

2. Provides a flux-dependent correction to M_R that shifts the effective seesaw
   scale by the 4% needed; or

3. Shows that the correct M_R to use is not r₃⁻¹ = M_GUT but instead a quantity
   involving both n₁ and the APS boundary data.

**Candidate mechanism (speculative):**

The exact GUT solution (Appendix B Route B) gives n₁^{phys} = 18 and N_M2 = 450.
The M2-brane contribution to the effective potential may shift M_R slightly. If:

    M_R^{eff} = M_GUT × (1 + δ_{M2})

where δ_{M2} ~ N_M2 × l₁₁⁶/r₃⁶ is the M2-brane backreaction, then the ratio
m_ν/m_KK would shift. A 4% shift in m_ν/m_KK requires δ_{M2} ~ 4% in the Yukawa
square, or ~2% in M_R. This is not obviously available from N_M2 = 450 without
a full computation.

**The RG-correction route:**

Paper 7 (Appendix A, §A.5.3) notes that m_ν/m_KK = 2.61 improves to 2.50 "at
TeV-scale RG corrections to g₂." The SU(2) coupling g₂ runs from M_GUT to M_EW.
If the effective g₂ entering the Yukawa is evaluated at the seesaw scale (M_R ~
10¹⁵ GeV) rather than M_Z:

    g₂(M_GUT) ≈ 0.633  (running from 0.65 at M_Z to 0.633 at M_GUT)

    m_ν/m_KK = 2g₂(M_GUT)² v² r₃ R = 2 × (0.633)² × ... = 2.47 ≈ 5/2

This is a 1% correction in the right direction, potentially closing the gap.
This is **not speculative** — it is a standard RG effect whose sign and order
of magnitude are correct. It would mean:

    **m_ν/m_KK = 5/2 exact at the GUT scale**

The 4% discrepancy between 2.61 and 2.50 is absorbed by running g₂ from M_Z to
M_GUT. This is the most concrete candidate for closing the ratio.

---

## What Would Constitute a Proof of m_ν/m_KK = 5/2

Three requirements (following etc/35a):

**Requirement 1:** Confirm the gauge-Higgs Yukawa formula with g₂ evaluated at
the GUT scale. This is a standard RG computation. If g₂(M_GUT) = 0.630 exactly
(the unified value), the ratio becomes exactly 5/2 at GUT precision.

**Requirement 2:** Show that the G₄ flux fixing r₃ (and hence M_R = 1/r₃)
is self-consistent with m_ν = 5/2 × m_KK at GUT scale. This would make m_ν/m_KK
a prediction of the flux data (n₁, n₂) = (18, −34) combined with gauge-Higgs.

**Requirement 3 (optional — for the deeper identity):** Compute the eta invariant
η(∂(CP² × S¹/Z₂)) at the hidden brane. If η = σ(CP²) = 1, the APS index gives
ind_APS = 3 − 1/2 = 5/2 as a topological statement. But Paper 7, Appendix A,
§A.5.4 proves this is arithmetically obstructed as a spin^c index. Requirements 1
and 2 are therefore the viable path.

---

## Summary Table

| Question | Finding | Status |
|----------|---------|--------|
| **Q1: Does Paper 7 compute Yukawa from G₄?** | No. Flux sector fixes moduli only. | [COMPUTED — Negative] |
| **Q2: Minimum flux on CP²** | n_min = 1/2 (FW shift); GUT solution has n₁^{phys} = 18 | [COMPUTED — Exact] |
| **Q3: Does n_min give m_ν/m_KK = 5/2?** | No direct connection. Yukawa not computed from flux. | [COMPUTED — No] |
| **Q4: M_R value and origin** | M_R = 1/r₃ ~ 10¹⁵ GeV; fixed indirectly via r₃² = n₁/(2cR) | [COMPUTED] |
| **Q5: Single flux configuration for all couplings?** | Flux fixes gauge couplings; Yukawa fixed separately by gauge-Higgs | [PARTIALLY COMPUTED] |
| **Q6: m_ν/m_KK = minimum G₄ quantum?** | Literal version ruled out. Additive identity χ+η = 5/2 exact but not index-theoretic | [RULED OUT (literal) / EXACT (mathematical identity)] |
| **RG-correction route** | g₂(M_GUT) running closes 4% gap → m_ν/m_KK = 5/2 at GUT scale | [OPEN — most viable candidate] |

---

## Open Questions and Next Steps

1. **Compute g₂(M_GUT):** Run g₂ from M_Z to M_GUT using the SM/GUT beta functions.
   Check whether g₂(M_GUT)² = g₂(M_Z)² × (5/2)/(2.61) = 0.399 → g₂(M_GUT) = 0.632.
   This is a concrete calculation that directly tests whether the ratio is exact at
   the GUT scale.

2. **M2-brane backreaction:** Compute the N_M2 = 450 M2-brane contribution to M_R.
   If δ_{M2} ~ 4% in the right direction, this would constitute a flux-driven
   correction to m_ν/m_KK.

3. **Flux-Yukawa overlap integral:** Compute ∫_{CP²×S²} ω_ν ∧ ω_H ∧ G₄/M_Pl^{3/2}
   explicitly for the GUT flux (18, −34) and the zero-mode wavefunctions of ν_R and H.
   This is the M-theory formula for the Yukawa coupling and has not been done in the
   framework.

4. **Check whether 5/2 enters the flux algebra differently:** The tadpole
   N_M2 = 450 = 2 × 9 × 25 = 2 × 225. The flux ratio 18:34 = 9:17. Neither
   immediately produces 5/2. But: 450/180 = 5/2 (where 180 = 10 × 18 = the flux
   integer 18 scaled by the Dynkin index 30/... ). This is numerology, not physics,
   without a derivation.

---

## Speculative Statement Requested (Q6 creative version)

The most precise statement that can be made without a proof:

> *The number 5/2 appears in the framework in three distinct ways:*
> *(a) Numerically: m_ν/m_KK ≈ 2.56 (gauge-Higgs, g₂ at M_Z) or 2.50 (at GUT scale);*
> *(b) Topologically: χ(CP²) + η(D_{S¹/Z₂}) = 3 + (−1/2) = 5/2, combining*
>     *the Euler characteristic of the generation-counting space with the spectral*
>     *asymmetry of the orbifold boundary;*
> *(c) Diophantinely: the GUT flux condition n₂/n₁ = −17/9 involves the integers*
>     *17 and 9, whose sum is 26 and ratio is ≈ 1.89; the fraction (b₂⁺ + b₂⁻)/2 = 1/2*
>     *on CP² is the same 1/2 that appears in the eta invariant.*
>
> *If the three occurrences are related by a unified mechanism — a flux-weighted*
> *index theorem on the orbifold with G₄ insertions — then m_ν/m_KK = 5/2 would*
> *be simultaneously a topological identity and a prediction of flux quantization.*
> *No such theorem currently exists. Its proof or disproof would constitute a*
> *decisive step in understanding the neutrino mass hierarchy.*

---

*Analysis conducted April 7, 2026.*
*Primary finding: G₄ flux in Paper 7 does not compute Yukawa couplings. The*
*51 meV prediction uses gauge-Higgs on S¹ for the Yukawa (y₄ = g₂√2) and G₄*
*flux for the seesaw scale (M_R = 1/r₃). The ratio m_ν/m_KK = 2.61 at M_Z,*
*potentially 2.50 at M_GUT (RG running of g₂). The 5/2 identity is exact*
*mathematically as χ(CP²) + η(S¹/Z₂) but cannot arise from any index theorem*
*on the compactification space (proved in Paper 7, Appendix A, §A.5.4).*
