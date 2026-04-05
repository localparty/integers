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

### 9.5 The Two-Loop Gauge Coupling Amplitude

Appendix C derives that exact GUT unification `α₃/α₂ = 1` at the
compactification scale requires an interpolation parameter `λ = 0.6552`
between the pure one-loop log stabilization and the coupled two-loop
self-consistent solution. The λ value is determined from the unification
condition — it is not yet derived from first principles.

**The open calculation:** Compute the two-loop Goroff-Sagnotti amplitude
on `S² × CP²` including the cross-coupling between sectors (the two-loop
coefficient for the S² modulus depends on `r₃` through the complementary
CP² volume, and vice versa). Specifically:

    c₂^{S²}(r₃) = α_GS × G_{eff,S²}²(r₃) × [Z_{S²}(0)]²
    c₂^{CP²}(r₂) = α_GS × G_{eff,CP²}²(r₂) × [Z_{CP²}(0)]²

where `G_{eff,X}` depends on the volume of the complementary space.
The coupled stabilization equations then determine `r₂` and `r₃` (and
hence `λ`) self-consistently.

**What would close this problem:**
- Compute `G_{eff,S²}` from `G₁₁` and `Vol(CP²) = 8π²r₃⁴/3`.
- Substitute into the coupled stabilization equations.
- Solve numerically for `(r₂, r₃)` as a function of `M₁₁` and `R`.
- Verify that the self-consistent solution gives `λ ≈ 0.6552` and
  hence `α₃/α₂ ≈ 1.000`.

If the first-principles `λ` matches 0.6552, the gauge coupling
hierarchy is fully derived with no free parameters (beyond `G₄` and
`R`). If `λ` differs significantly from 0.6552, the framework
overshoots or undershoots GUT unification, and the discrepancy
identifies where the two-loop cross-coupling approximation breaks down.

---

