## 9. Open Problems


### 9.1 Moduli Stabilization

The Epstein zeros mechanism (Structural Zero Theorem, Paper 1
§K.7b) does NOT extend to `S²` and `CP²`. On `S¹`, eigenvalues are
`n²` (perfect squares), and the spectral zeta reduces to Epstein
zeta functions whose zeros kill all counterterms. On `S²` and `CP²`,
the eigenvalues are `l(l+1)` and `k(k+2)` respectively — shifted
squares, not perfect squares. The corresponding spectral zeta
functions `Z_{S²}(-j)` and `Z_{CP²}(-j)` do NOT vanish at negative
integers.

This gives a geometric principle: **flat dimensions freeze, curved
dimensions stabilize.**

- **`R` (S¹, flat):** Frozen by Hubble friction. The exact Casimir
  energy is finite (Epstein zeros kill all counterterms), and the
  Casimir potential has a minimum that locks `R` at the Planck scale.
  No dynamical stabilization needed — the modulus is inert.

- **`r₂` (S², curved):** Dynamically stabilized. Because
  `Z_{S²}(-j) ≠ 0`, finite two-loop corrections generate a
  non-trivial effective potential for `r₂`. The curved geometry
  provides its own stabilization mechanism.

- **`r₃` (CP², curved):** Dynamically stabilized similarly. Because
  `Z_{CP²}(-j) ≠ 0`, the spectral zeta values are non-vanishing and
  generate a potential that fixes the Kähler modulus.

The gauge coupling hierarchy `g₃ > g₂ > g₁` is potentially
derivable from the spectral zeta values of the three factors: the
non-zero `Z_{S²}` and `Z_{CP²}` values at the relevant loop orders
set the relative magnitudes of the gauge couplings at the
compactification scale.

See `etc/12b-moduli-freezing-analysis.md` for the full analysis.

### 9.2 The SLOCC-Isometry Map

Making Conjecture 5.1 rigorous requires an explicit map from the
SLOCC classification of 3-qubit entanglement to the isometry
algebra of `CP² × S² × S¹`. The tangent space calculation
(Section 5.5) is the key step. If successful, this would establish
that the SM gauge group is determined by entanglement geometry —
arguably the deepest result in the series.

### 9.3 Non-Perturbative Completion

The non-perturbative status of the framework rests on a
three-layer argument established across Papers 1 and 3.

**Layer 1 — Perturbative finiteness (Paper 1, proved).** Theorem
S.1 establishes that the `L`-loop effective action is finite at
every order under spectral zeta regularization. The two-loop `R³`
counterterm vanishes identically at every order in the mass
expansion, via complementary trivial zeros of `ζ(s)` and
`L(s, χ₋₃)`. Because the cancellation is number-theoretic — not
an artifact of the regularization scheme — the result is
scheme-independent for all subleading terms. The theory is
predictive to all orders with no free parameters beyond `G₄`
and `L`.

**Layer 2 — Non-perturbative stability (Paper 1 Appendix J,
proved).** Every known non-perturbative instability is controlled
by the single ratio `R / l_P ~ 10³⁰`:

- Witten bubble of nothing: suppressed by `exp(−10³⁰)` via
  Casimir stabilization of the e-circle.
- Gravitational instantons: Euclidean action `~ 10⁶⁰`,
  contributing `exp(−10⁶⁰)`.
- KK monopoles: mass `~ 10²² kg`, unproducible at any accessible
  energy.
- Topology change: suppressed by both the Casimir barrier and the
  instanton action.

The perturbative result IS the physical answer to `10³⁰`-digit
precision. The M-brane sector is fully classified (Appendix B):
all M2-M5 bound states are identified, the M2-brane tension
reproduces the QCD string tension (Paper 5, §3), and all exotic
composites lie at or above `M_{GUT}`.

**Layer 3 — M-theory completion (formal).** The e-circle is the
M-theory circle (§2.3). M-theory therefore provides the formal
non-perturbative definition of the 5D path integral. This is not
a rescue mechanism — it is a seal on a theory that is already
self-consistent to `exp(−10³⁰)`.

**Remaining open problem.** The genuinely open question is the
`L ≥ 3` overlapping-subdivergences gap (Appendix K, §K.5.2):
whether subleading loop integrals reduce to Epstein zeta values,
or whether a broader class of automorphic forms is required. This
is a technical gap in the all-orders proof, not a threat to
finiteness — the number-theoretic zeros that kill the leading
divergence are present at every loop order.

### 9.4 Global Topology of the SLOCC-Isometry Correspondence

Theorem 5.2 establishes the SLOCC-isometry correspondence at the Lie
algebra level: the tangent space to the GHZ SLOCC orbit under `SU(2)³`
carries the weight system of the `A₂` root system, matching the
isometry tangent weights of `CP² × S² × S¹` under the identification
Slot k ↔ root α_k.

What remains open is the global topology. The SLOCC orbit is
`SU(2)³ / T²` (where `T²` is the 2D stabilizer torus), which locally
looks like `SU(3)/T² × S¹` — the complete flag manifold of `C³` times
a circle. The flag manifold `Fl(1,2;3) = SU(3)/T²` is an S²-bundle
over CP², but the bundle is **non-trivial** (it is the projectivization
of the tautological rank-2 bundle over CP², not the trivial product).

The product `CP² × S² × S¹`, by contrast, is the trivial S²-bundle
over `CP²` times `S¹`.

**What would close this problem:**
1. Compute `H*(SU(2)³/T²; Z)` and compare with `H*(CP² × S² × S¹; Z)`
   and `H*(Fl(1,2;3) × S¹; Z)`.
2. Determine whether the `(Z₂)²` discrete quotient (from the GHZ
   stabilizer) trivializes the S²-bundle over CP².
3. If it does: `SU(2)³/(T² × (Z₂)²) ≅ CP² × S² × S¹` globally.
4. If not: the correspondence holds at the Lie algebra level; the
   global topology of the internal manifold must be taken as CP² × S²
   × S¹ (as an independent physical input), with the SLOCC structure
   explaining the gauge algebra but not the fiber bundle geometry.

**Physical significance:** This distinction affects the allowed fermion
representations (zero-mode spectrum depends on the spin structure of the
internal space), but not the gauge group or coupling predictions.

**The resolution via cohomology.** The two candidate manifolds have
different cohomology rings:

    H*(CP² × S² × S¹; ℤ) = ℤ[x,y,z] / (x³, y², z²)
        with |x| = 2, |y| = 2, |z| = 1. Product structure is trivial.

    H*(Fl(1,2;3) × S¹; ℤ) = H*(Fl(1,2;3)) ⊗ H*(S¹)
        where H*(Fl(1,2;3)) has a non-trivial cup product structure
        from the fibration S² → Fl(1,2;3) → CP².

The flag manifold satisfies: `x₁ + x₂ + x₃ = 0` (from the Borel
presentation), making `H*(Fl)` NOT a polynomial ring — it is a
truncated polynomial ring with relations. This distinguishes it
from the product `CP² × S²`.

**Computation:** Compute `H*(SU(2)³/T²; ℤ)` using the Eilenberg-Moore
spectral sequence for the fibration `T² → SU(2)³ → SU(2)³/T²`. If
the result matches `H*(CP² × S² × S¹)`, Conjecture 5.1 is globally
true. If it matches `H*(Fl(1,2;3) × S¹)`, the correspondence is
Lie-algebraic only (which is still sufficient for the gauge algebra
derivation). This is a finite computation in algebraic topology —
to be developed in `etc/24-flag-manifold-cohomology.md`.

### 9.5 Gauge Coupling Unification and the Moduli Potential

Appendix C derives that exact GUT unification `α₃/α₂ = 1` at the
compactification scale requires an interpolation parameter `λ = 0.6552`
between the pure one-loop log stabilization and the coupled two-loop
self-consistent solution. The coupled Casimir + Goroff-Sagnotti system
(`etc/21`) exhibits a saddle-node bifurcation at `κ_bif = 3.477 × 10⁻²`,
with GUT unification requiring `κ_* = 3.545 × 10⁻²`.

**The three-equation system (`etc/22`).** The coupled stabilization
equations for `S²` and `CP²`, together with the Planck mass constraint
`M_Pl² = M₁₁⁹ × Vol(CP² × S² × S¹)` and R fixed by dark energy,
form a self-consistent system that determines `κ` without free
parameters. The computation (`etc/22-three-equation-system.md`) shows
that this system does **not** close:

- The Planck + dark energy constraints give
  `χ = R/l₁₁ ~ 2.4 × 10¹⁸`, forcing
  `κ = α_GS/(4π²χ²) ~ 3 × 10⁻⁴⁰`.
- This is **38 orders of magnitude** below `κ_bif`, far outside the
  regime where Branch 1 solutions exist.
- The physical origin is the hierarchy `R/l₁₁ ~ 10¹⁸`: the
  Goroff-Sagnotti two-loop correction scales as `G_eff² ~ (l₁₁/r)¹⁸`
  and is negligible at the physical compactification scale.
- In the pure one-loop regime (`κ → 0`), each modulus is stabilized
  independently by the logarithmic mechanism at `Q_X(ln x_X) = 0`,
  giving `ρ ≈ 17` and `α₃/α₂ ≈ 391`.

**The G₄ flux mechanism.** The CP² and S² moduli are sub-Planckian
(`r₃/l₁₁ ≈ 0.003`), placing their stabilization entirely in the
M-theory strong-coupling regime where G₄ flux dominates. The
perturbative Casimir + Goroff-Sagnotti potential is irrelevant: the
loop expansion parameter `(l₁₁/r₃)² ~ 10⁵ ≫ 1` at the CP² scale
(see `etc/22-three-equation-system.md` for the full diagnosis).

The correct stabilization mechanism is the Gukov-Vafa-Witten (GVW)
superpotential:

    W_GVW = (1/l₁₁³) ∫_{M₇} G₄ ∧ Φ

with two independent flux quanta:
- `n₁ = (1/2πl₁₁³) ∫_{CP²} G₄` (CP² flux)
- `n₂ = (1/2πl₁₁³) ∫_{CP¹×S²} G₄` (mixed flux)

The S¹ radius `R` is unaffected — G₄ does not couple to flat cycles
(S¹ contributes no 4-cycle to `H₄(M₇, ℤ)`). The dark energy
mechanism (S¹ Casimir, Paper 1) and the GUT scale (CP²/S² flux) are
stabilized by entirely independent mechanisms.

The F-term scalar potential `V_flux(r₂, r₃)` from the two flux
quanta has the structure (`etc/23-g4-flux-stabilization.md` §2.5):

    V = (8V₀/3) e^{−3σ−2τ} [5a² + 3ab + 3b²]

where `a = n₁ e^{2τ−4σ}`, `b = n₂ e^{−2τ}`, and `σ = ln(r₃/l₁₁)`,
`τ = ln(r₂/l₁₁)`. The minimum determines `r₂/r₃ = F(n₁/n₂)` as a
function of the flux ratio. The condition `F = √3/2` (GUT unification,
`α₃/α₂ = 1`) constrains the flux ratio to a specific value.

**What remains open:** The product manifold CP² × S² × S¹/Z₂ does
not have G₂ holonomy — it has a G₂ structure with intrinsic torsion.
The diagonal-Kähler GVW formula gives a runaway in the σ direction;
the torsion-corrected superpotential (House-Micu 2005, Behrndt-Jeschek
2005) provides the additional curvature-flux balance needed for
stabilization. The explicit computation of the torsion classes and
the resulting F-term minimum is identified as the central computation
for Paper 7. The tadpole constraint (`etc/23` §4) is not an
obstruction for small flux quanta.

The spectral zeta data (Z(−2), Z'(−2), Z(0)) and the gauge coupling
formula `α₃/α₂ = (4/3)ρ²` remain exact. The `etc/21` bifurcation
analysis correctly characterizes the perturbative sector (which is
now understood to be physically irrelevant at the CP²/S² scale).

---

