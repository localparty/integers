# 1. Introduction: Why Does CP² Have the Radius It Does?

Paper 1 of this series established that a single compact dimension
— the e-circle `S¹` — makes quantum mechanics geometric: the wave
function is the literal shape of a particle in ~~five-dimensional~~ 4+1 coordinate
spacetime.<!-- legacy 2026-04-15 Intervention 8 §0.10: "five-dimensional" → "4+1 coordinate" per Vocabulary Canon entry 1. --> Paper 4 showed that the e-circle embeds into a
7-dimensional internal manifold `CP² × S² × S¹`, whose isometries
produce exactly the Standard Model gauge group
`SU(3) × SU(2) × U(1)`. The CP² radius r₃ sets the GUT scale
`M_GUT = 1/r₃ ~ 2 × 10¹⁵ GeV`, the S² radius r₂ sets the weak
sector geometry, and the ratio r₂/r₃ = √3/2 is the condition for
gauge coupling unification (Paper 4, Appendix C). Papers 5 and 6
completed the perturbative story: confinement from the CP² holonomy,
the thermal history from the dilaton, and the cosmological constant
from the S¹ Casimir energy. But every paper left one question open:
**what determines r₃?**

---

## 1.M Methodology: The Framework's Reasoning Patterns

This paper is one of seven in a series. Each paper applies the same
small set of reasoning patterns to a different domain of physics.
The patterns are documented in full in `readme.md`; the relevant ones
for this paper are identified below. Understanding which pattern a
derivation uses lets you see *why* the result works, not just *that*
it works — and lets you apply the same move to new problems.

The six patterns of the framework:

| # | Name | Core move |
|---|------|-----------|
| 1 | **Geometric Reinterpretation** | A 4D mystery is a shadow of simpler 5D geometry |
| 2 | **Holonomy Correspondence** | Wilson line VEV around a compact dimension → gauge phase |
| 3 | **Casimir as Scale-Setter** | Quantum vacuum energy on a compact space → a fundamental scale |
| 4 | **Topological Rigidity** | Discrete invariant (winding number, χ, homotopy) → exact quantized result |
| 5 | **Zeta Regularization of KK Towers** | Compact → discrete KK sum → analytic continuation → finite result |
| 6 | **Projection Produces Apparent Pathology** | 4D looks broken because 4D is a partial trace over the geometry |

**Primary patterns in this paper:**

- **Pattern 4** gives gauge coupling unification: the flux ratio
  n₂/n₁ = −17/9 is determined by three interlocking discrete
  constraints (Kähler weights, G₂ torsion coefficients, group-
  theoretic unification condition). Each is topological or geometric
  and cannot be continuously adjusted. The integers 9 and 17 are
  as rigid as χ(CP²) = 3.

- **Pattern 4** (inverted) gives Theorem U*: the geometric inputs
  {n_i, χ_j, M_Pl} are all O(1) integers or small numbers. Any
  algebraic function of O(1) inputs produces an O(1) output.
  R_obs/l_P ~ 10³⁰ is therefore unreachable by algebraic derivation
  — the topological rigidity that makes other results exact also
  makes the CC value structurally inaccessible. This is a type error,
  not a fine-tuning.

- **Pattern 5** gives the spectral gap Δ_{5D} ≥ √5/r₃ > 0:
  the Lichnerowicz formula on Fubini-Study CP² with the canonical
  spin^c structure gives D² ≥ 5/r₃². Theorems K.1 and K.3 then
  make this gap perturbatively exact. The framework's non-perturbative
  stability follows without assuming M-theory.


---

## 1.1 The Scale Diagnosis

The answer does not lie in perturbation theory. Computing the
relevant scales from the framework's parameters reveals:

    M₁₁  = 5.52 × 10¹² GeV    (11D Planck scale)
    M_GUT = 2.0  × 10¹⁵ GeV    (CP² KK scale = 1/r₃)
    M_Pl  = 2.44 × 10¹⁸ GeV    (4D Planck scale)

    r₃/l₁₁ = r₃ × M₁₁ ≈ 0.003  ≪ 1

The CP² and S² internal manifolds are **sub-Planckian**: their radii
are smaller than the 11D Planck length. The Kaluza-Klein perturbative
expansion requires `r ≫ l₁₁` and is therefore invalid for these
cycles. M2-brane instantons on CP¹ ⊂ CP² have action
`S_M2 ~ (M₁₁/M_GUT)² × 10⁶` — enormously suppressed, not O(1). The
loop expansion parameter at the CP² scale is `(l₁₁/r₃)² ~ 10⁵ ≫ 1`.
Perturbation theory has broken down completely. The CP² and S² moduli
live in the M-theory **strong-coupling regime**.

## 1.2 The GVW Mechanism

The correct degree of freedom is the **G₄ four-form field strength**
of M-theory — the fundamental non-perturbative object in M-theory
compactifications. Its quantization condition `∫_{C₄} G₄ ∈ ℤ` over
any compact 4-cycle C₄ is the M-theory analog of Dirac flux
quantization. The Gukov-Vafa-Witten (2000) superpotential

    W_GVW = (1/l₁₁³) ∫_{M₇} G₄ ∧ Φ

generates a scalar potential for all moduli that couple to curved
4-cycles. For M-theory on `CP² × S² × S¹/Z₂`, the two independent
4-cycles are CP² itself and `CP¹ × S²`, carrying integer flux quanta
n₁ and n₂ respectively. The flux potential `V_flux(r₂, r₃)` fixes
both radii as functions of the flux ratio n₁/n₂.

## 1.3 The Decoupling

A crucial structural feature: G₄ couples to **curved, non-contractible
4-cycles** but not to the flat S¹. The S¹ has no 4-cycle (it is
1-dimensional), so G₄ flux cannot stabilize it. Conversely, the S¹
Casimir energy (Papers 1 and 6) is a perturbative effect that operates
in the super-Planckian regime `R/l₁₁ ~ 2.8 × 10²³ ≫ 1`, where the
KK expansion is perfectly valid. The two stabilization mechanisms
decouple cleanly:

- **S¹ radius R:** stabilized by the perturbative Casimir energy
  (Papers 1, 6), setting the dark energy density.
- **CP² radius r₃ and S² radius r₂:** stabilized by non-perturbative
  G₄ flux (this paper), setting the GUT scale and gauge coupling
  unification.

The hierarchy `R ≫ l₁₁ ≫ r₃` is natural: R is Casimir-frozen in the
perturbative regime, r₃ is flux-frozen in the strong-coupling regime.
The 38-order gap between the two energy scales is not a failure — it
is a **regime indicator**, reflecting the separation between
perturbative S¹ physics and non-perturbative CP²/S² physics.

## 1.4 Organization

Section 2 develops the explicit G₄ flux superpotential on
`CP² × S² × S¹/Z₂`, identifying the 4-cycles, their flux quanta,
and the Kahler potential for the moduli. Section 3 computes the flux
potential `V_flux(r₂, r₃)`, finds the minimum, and derives the GUT
unification condition r₂/r₃ = √3/2 as a function of the flux ratio
n₁/n₂. Section 4 checks the G₄ tadpole constraint and verifies
consistency with the Euler characteristic of the 8-manifold boundary.
Section 5 identifies the G₄ flux axion as the inflaton, connecting
to the inflation sector of Paper 6. Section 6 summarizes the
completed framework.
