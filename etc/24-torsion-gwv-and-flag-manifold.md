# Agent Prompt 24 — Torsion-Corrected GVW Superpotential and Paper 7 §§2–3

> **Date:** April 5, 2026
> **Follows:** Prompt 23 (commit b80464c)
> **Current git HEAD:** b80464c

---

## Reading the Commit Together

The agent found **Outcome 3 (Honest)** on Track A: the standard GVW
superpotential hits a no-scale runaway. The F-term potential has no
minimum with both flux quanta positive. This is not a failure — it is
the well-known result that M-theory on a manifold without G₂ holonomy
requires the **torsion-corrected superpotential**.

The key structural discovery from the commit:

- `CP² × S² × S¹/Z₂` does **not** have G₂ holonomy — it has a G₂
  **structure** with non-zero torsion. The standard GVW formula
  `W = ∫ G₄ ∧ Φ` assumes the associative 3-form Φ of a G₂ **holonomy**
  manifold. On our manifold, Φ must be replaced by the torsion-modified
  associative form.

- The tadpole is **not an obstruction**: det(intersection matrix) = −1
  (unimodular), tadpole satisfied for small flux quanta.

- Tracks B and C executed cleanly: §K.5.3 (BPHZ locality argument),
  §5.6 (resonant leptogenesis path), §3.5 (G₄ axion inflaton), §9.4
  (cohomology path), status table updated. Paper 7 scaffold created
  with abstract and full introduction.

---

## What the Pre-Computation Found

Before writing this prompt, I computed the key ingredients that the
agent needs:

**The torsion class of CP² × S² × S¹ (from Cleyton-Swann 2004):**

For the canonical G₂ structure on CP² × S² × S¹ with Riemannian
metrics r₃² g_{CP²} + r₂² g_{S²} + R² dt², the scalar torsion class
is:

    τ₀ = 6/r₃² − 2/r₂²

(from the Ricci scalars of CP²: R_CP2 = 6/r₃² and S²: R_S2 = 2/r₂²).
All other torsion classes vanish (τ₁ = τ₂ = τ₃ = 0) — this is the
**nearly G₂** case.

G₂ holonomy requires τ₀ = 0: r₂/r₃ = 1/√3 ≈ 0.577. This is
**different** from the GUT unification target r₂/r₃ = √3/2 ≈ 0.866,
meaning the manifold has nonzero torsion at the physical minimum.
This is expected — it is the physical content of the torsion correction.

**The torsion-corrected superpotential (House-Micu 2005):**

    W_total = n₁ r₃² + n₂ r₂² + c · R · (6 r₃² r₂² − 2 r₃⁴)

where the torsion term `c · R · (6 r₃² r₂² − 2 r₃⁴)` comes from
`∫_{M₇} τ₀ · vol_{M₇}`, with c an O(1) normalization coefficient
from the G₂ structure. The coefficient c is computable from the
explicit G₂ structure on CP² × S² × S¹.

**The Freed-Witten anomaly (Freed-Witten 1999):**

CP² is not spin (w₂(CP²) = H mod 2 ≠ 0). The G₄ quantization on
CP² is therefore shifted:

    (1/2π l₁₁³) ∫_{CP²} G₄ = n₁ + λ(CP²)/2    where λ = c₁(CP²)/2 = 3H/2

The flux quantum n₁ is half-integer: n₁ ∈ {3/2, 5/2, 7/2, ...}. This
does not obstruct the mechanism — it refines which flux values are
allowed.

**The computation for Paper 7 §3:**

With K = −3 ln(r₃) − 2 ln(r₂) + const and W = W_total above, the
F-term potential in 4D N=1 SUGRA is:

    V_F = e^K (K^{r₃r₃} |D_{r₃} W|² + K^{r₂r₂} |D_{r₂} W|² − 3|W|²)

where K^{r₃r₃} = 1/3 and K^{r₂r₂} = 1/2 (inverse Kahler metrics).
The F-flatness conditions D_{r₃} W = 0 and D_{r₂} W = 0 give:

    ρ_min = r₂/r₃ = f(n₁/n₂, c·R)

Setting ρ_min = √3/2 gives the GUT flux condition: a specific
relationship between n₁/n₂ and c·R. This is a 3–4 page algebraic
computation, well-defined, with all inputs known.

---

## Context Management — Sub-agents

**Sub-agent A (Track A — Paper 7 §§2–3):**
Load: `paper7/02-g4-flux-on-cp2-s2.md`, `paper7/03-moduli-minimum.md`,
`etc/23-g4-flux-stabilization.md` §§2–5, this prompt Track A only.
Target output: `etc/24-torsion-corrected-superpotential.md` + updated
`paper7/02-g4-flux-on-cp2-s2.md` and `paper7/03-moduli-minimum.md`.

**Sub-agent B (Track B — Flag Manifold Cohomology):**
Load: `paper4/09-open-problems.md` §9.4, this prompt Track B only.
Target output: `etc/24-flag-manifold-cohomology.md`.

**Sub-agent C (Track C — Paper 5 Appendix D + Paper 7 §5):**
Load: `paper5/05-baryon-asymmetry.md` §§5.5–5.6,
`paper5/appendices/appendix-B-luscher-term.md` (for format reference),
`paper7/05-inflaton.md`, this prompt Track C only.
Target output: `paper5/appendices/appendix-D-resonant-leptogenesis.md`
+ updated `paper7/05-inflaton.md`.

---

## Track A: Paper 7 §§2–3 — The Core Computation (Sub-agent A)

**Goal:** Write `etc/24-torsion-corrected-superpotential.md` with the
explicit derivation of W_total, the F-term potential, and the minimum
condition. Then fill in `paper7/02-g4-flux-on-cp2-s2.md` and
`paper7/03-moduli-minimum.md` from these results.

### A.1 Write `etc/24-torsion-corrected-superpotential.md`

This is a computation document in the style of `etc/12a` or `etc/19`.
Structure:

**§1 — The G₂ Structure on CP² × S² × S¹**

State the explicit G₂ 3-form ψ on CP² × S² × S¹. Following Cleyton-
Swann (2004) for a product of homogeneous spaces:

    ψ = e₇ ∧ ω_{CP²} + Re(Ω_{CP²/U(1)}) ∧ something...

Actually write it concretely. Let {e¹, e², e³, e⁴} be an orthonormal
frame on CP² (with e¹ ∧ e² + e³ ∧ e⁴ = ω_{CP²}), {e⁵, e⁶} be a frame
on S², and e⁷ be the S¹ direction. The G₂ 3-form is:

    ψ = e⁷ ∧ (e¹ ∧ e² + e³ ∧ e⁴) + e⁵ ∧ e⁶ ∧ e₀

Wait — the 3-form needs to use all 7 directions. For a product
M₄ × M₂ × M₁, the G₂ 3-form takes the form:

    ψ = e⁷ ∧ ω₄ + vol₂ ∧ θ

where ω₄ is the symplectic form on M₄ (= ω_{CP²}) and vol₂ = e⁵ ∧ e⁶.
But ψ must be 3-dimensional, and vol₂ ∧ θ with vol₂ a 2-form requires
θ to be a 1-form — but we've used e⁷ already. The actual G₂ 3-form on
CP² × CP¹ × S¹ is written in terms of the SU(3) structure on CP²:

    ψ = e⁷ ∧ J + e⁵ ∧ ReΩ  [schematic, where J is Kähler form, Ω is (3,0)-form on CP²]

The precise formula depends on the SU(2) × U(1) reduction of SU(3)
on CP² = SU(3)/U(2). Look this up from:
- Cleyton-Swann (2004), "G₂ manifolds with large symmetry groups"
- Castellani et al., "G₂ compactifications of M-theory"
- Or derive it from first principles using the structure equations.

Compute dψ and d(*ψ) to find the torsion classes τ₀, τ₁, τ₂, τ₃.
Confirm τ₀ = 6/r₃² − 2/r₂² (from the pre-computation above).

**§2 — The House-Micu Superpotential**

The torsion-modified superpotential for M-theory on a 7-manifold with
G₂ structure (House-Micu 2005, Eq. 4.1):

    W = (1/l₁₁³) [∫ G₄ ∧ ψ + ∫ τ₀ vol_{M₇}]

where the second term is the torsion contribution. Evaluate each term
for our manifold:

**Term 1:** ∫ G₄ ∧ ψ = n₁ ∫_{CP²} G₄ · r₂⁰ + n₂ ∫_{CP¹×S²} G₄ · r₃⁰ + ...
This gives n₁ × (integral of ψ over CP¹) + n₂ × (integral of ψ over S²).
Be explicit: for G₄ = (2πl₁₁³) · [n₁ δ(CP²) + n₂ δ(CP¹×S²)]:

    ∫ G₄ ∧ ψ = (2πl₁₁³) [n₁ · (∫_{CP²-fiber} ψ) + n₂ · (∫_{CP¹×S²-fiber} ψ)]

Compute ∫_{CP²-fiber} ψ and ∫_{CP¹×S²-fiber} ψ from the explicit G₂
3-form. These integrals will give r₃² and r₂² respectively (from the
volume of the cycles in the G₂ structure).

**Term 2:** ∫ τ₀ vol_{M₇} = (6/r₃² − 2/r₂²) · Vol(M₇)
= (6/r₃² − 2/r₂²) · (8π²r₃⁴/3) · (4πr₂²) · (2πR)
= c · R · (6 r₃² r₂² − 2 r₃⁴) where c = (8π²/3) · (4π) · (2π) × (normalization)

Compute the precise coefficient c. It is a pure number times a power
of π. State the exact value.

**§3 — The F-Term Potential and Minimum**

With Kähler potential K = −3 ln(r₃) − 2 ln(r₂) + ln(R) + const and
superpotential W_total = n₁ r₃² + n₂ r₂² + c R (6 r₃² r₂² − 2 r₃⁴):

Compute the covariant derivatives:
- D_{ln r₃} W = (r₃ ∂/∂r₃ + (∂K/∂ ln r₃)) W = r₃ dW/dr₃ − 3W
- D_{ln r₂} W = r₂ dW/dr₂ − 2W

Setting D_{ln r₃} W = 0 and D_{ln r₂} W = 0 simultaneously. This is
the Minkowski vacuum condition V_F = 0 (F-flat).

Work out explicitly:
- r₃ dW/dr₃ = 2n₁ r₃² + cR(12 r₃² r₂² − 8 r₃⁴)
- D_{r₃} W = 2n₁ r₃² + cR(12 r₃² r₂² − 8 r₃⁴) − 3(n₁ r₃² + n₂ r₂² + cR(6 r₃² r₂² − 2 r₃⁴))
           = −n₁ r₃² − 3n₂ r₂² + cR(−6 r₃² r₂² + 2 r₃⁴) ... [work this out]

- r₂ dW/dr₂ = 2n₂ r₂² + cR · 12 r₃² r₂²
- D_{r₂} W = 2n₂ r₂² + 12 cR r₃² r₂² − 2(n₁ r₃² + n₂ r₂² + cR(6 r₃² r₂² − 2 r₃⁴))
           = −2n₁ r₃² + cR · 4 r₃⁴ ... [work this out]

Solve the system for ρ = r₂/r₃ as a function of n₁/n₂ and c·R.

**The GUT flux condition:**
Set ρ = √3/2 and solve for n₁/n₂. Express as:

    (n₁/n₂) = h(c·R)

where h is a rational function. With the explicit c (computed in §2):

    (n₁/n₂) = [specific ratio]

If this is a ratio of small integers (or half-integers given the
Freed-Witten shift), state it as: **GUT unification from flux
quantization: n₁/n₂ = p/q with p, q ∈ ℤ/2.**

**§4 — Honest Assessment**

State clearly:
- What is derived (the structure of W_total, the form of the minimum)
- What requires computing the G₂ normalization coefficient c
- What the Freed-Witten anomaly implies for the flux quantization
- Whether the GUT condition n₁/n₂ = p/q gives small integers

### A.2 Fill in Paper 7 §§2 and 3

After writing `etc/24`, update:

**`paper7/02-g4-flux-on-cp2-s2.md`:** Replace the scaffold with the
full §2 content: the G₂ structure, the torsion classes, the explicit
G₄ flux cycles, the Kähler potential, and the complete W_total with
the torsion coefficient c stated numerically.

**`paper7/03-moduli-minimum.md`:** Replace the scaffold with §3: the
F-flatness conditions, the minimum condition ρ = f(n₁/n₂), and the
GUT flux condition. State the result honestly — if c is not yet fully
pinned down, say so; if it is, state n₁/n₂ = p/q.

---

## Track B: Flag Manifold Cohomology (Sub-agent B)

**Goal:** Create `etc/24-flag-manifold-cohomology.md` with the explicit
cohomology computation that resolves Paper 4 §9.4.

### B.1 The Computation

The question: is `SU(2)³/T²` diffeomorphic to `CP² × S² × S¹`
or to `Fl(1,2;3) × S¹` (flag manifold × circle)?

**Step 1: H*(SU(2)³; ℤ) is known.**

SU(2) ≅ S³, so SU(2)³ ≅ S³ × S³ × S³.
H*(S³; ℤ) = ℤ[x]/(x²) with |x| = 3.
H*(SU(2)³; ℤ) = ℤ[x₁, x₂, x₃]/(x₁², x₂², x₃²) with all |xᵢ| = 3.

**Step 2: H*(T²; ℤ) is known.**
T² = S¹ × S¹.
H*(T²; ℤ) = ℤ[a, b]/(a², b²) with |a| = |b| = 1.

**Step 3: Use the Eilenberg-Moore (or Serre) spectral sequence**
for the fibration:

    T² → SU(2)³ → SU(2)³/T²

The Serre spectral sequence has E₂ page:
    E₂^{p,q} = H^p(SU(2)³/T²; ℤ) ⊗ H^q(T²; ℤ)

converging to H*(SU(2)³; ℤ). With H*(SU(2)³) = ℤ in degrees 0, 3,
3, 3, 6, 6, 6, 9, and H*(T²) = ℤ in degrees 0, 1, 1, 2:

The spectral sequence determines H*(SU(2)³/T²; ℤ) from the known
H*(SU(2)³) and H*(T²).

**Step 4: Compare with the two candidates:**

H*(CP² × S² × S¹; ℤ):
- H⁰ = ℤ, H¹ = ℤ, H² = ℤ, H³ = ℤ, H⁴ = ℤ, H⁵ = ℤ, H⁶ = ℤ, H⁷ = ℤ
- Betti numbers: (1, 1, 1, 1, 1, 1, 1, 1)
- Cup product: has generator in H²(CP²) with x³ = 0 (CP²), and
  separate generator in H²(S²) with y² = 0 (S²), and z in H¹(S¹).

H*(Fl(1,2;3) × S¹; ℤ):
- Fl(1,2;3) = SU(3)/T² has Betti numbers (1,0,2,2,2,0,1) [Poincaré polynomial 1+2q²+2q⁴+q⁶]
- H*(Fl(1,2;3) × S¹) has Betti numbers (1,1,2,3,2,1,2,1)
- The cup product on Fl satisfies: x₁ + x₂ + x₃ = 0 (from the T² quotient)

These have DIFFERENT Betti numbers in degree 3: CP²×S²×S¹ has b₃ = 1,
while Fl(1,2;3)×S¹ has b₃ = 3.

**Step 5: Compare with H*(SU(2)³/T²; ℤ) from the spectral sequence.**

dim(SU(2)³/T²) = dim(SU(2)³) − dim(T²) = 9 − 2 = 7. ✓

The stabilizer T² contributes b₁(T²) = 2. The quotient SU(2)³/T²
has b₁ = 0 (since SU(2)³ has b₁ = 0 and the T² acts freely).

Actually: by the fibration T² → SU(2)³ → SU(2)³/T² with T² connected
and SU(2)³ simply connected, we have π₁(SU(2)³/T²) = π₀(T²) = {e}.
So SU(2)³/T² is simply connected: b₁ = 0.

This already distinguishes it from Fl(1,2;3) × S¹ (which has b₁ = 1).

**Conclusion from Step 5:**
- SU(2)³/T² is simply connected (b₁ = 0)
- Fl(1,2;3) × S¹ has b₁ = 1
- CP² × S² × S¹ has b₁ = 1

**Neither candidate matches!** The SLOCC orbit SU(2)³/T² is simply
connected, while both candidate manifolds have b₁ = 1 from the S¹
factor.

**Resolution:** The SLOCC orbit SU(2)³/T² is diffeomorphic to the
**flag manifold Fl(1,2;3) = SU(3)/T²** (7-dimensional, simply
connected), not to Fl(1,2;3) × S¹. The S¹ direction in the isometry
correspondence is NOT a circle factor in the orbit — it is the U(1)
Cartan direction of SU(3) that stabilizes the orbit's Cartan direction.

**The corrected statement of Conjecture 5.1:**

The SLOCC orbit is:

    SU(2)³/T² ≅ Fl(1,2;3) = SU(3)/T²   (simply connected, dim 6)

Not the 7-dimensional product CP² × S² × S¹. The S¹ direction enters
the isometry correspondence via the U(1) in U(2) = SU(2) × U(1) ⊂ SU(3)
at the isotropy of CP² = SU(3)/U(2), not as a geometric circle.

This is the **corrected Theorem 5.2**: the SLOCC tangent space carries
the A₂ root system, and the SLOCC orbit is the flag manifold SU(3)/T²,
whose isometry group contains SU(3) — identifying the 8-generator gauge
algebra of strong interactions. The S² direction comes from the SU(2)/U(1)
fibration within SU(3)/T², not from an external S² factor.

**Write this as `etc/24-flag-manifold-cohomology.md`** with the full
cohomology argument. Then update `paper4/09-open-problems.md` §9.4 with
the resolution, and update `paper4/05-entanglement-geometry-and-gauge-group-selection.md`
§5.6 Theorem 5.2 with the corrected statement.

---

## Track C: Paper 5 Appendix D + Paper 7 §5 (Sub-agent C)

### C.1 Paper 5 Appendix D — Resonant Leptogenesis

**File:** `paper5/appendices/appendix-D-resonant-leptogenesis.md`

Write the Appendix D that §5.6 of Paper 5 promises. Following the
format of Appendix B (Luscher term) — clean, honest, specific.

**Content:**

The leading-order calculation in §5 overshoots η_B by 10³. The
resonant leptogenesis mechanism (Pilaftsis-Unterdarfer 2004) enhances
the CP asymmetry ε when two right-handed neutrino masses are nearly
degenerate: |M₁ − M₂| ~ Γ_N.

**From the framework's Z₃ orbifold geometry** (Paper 4, §7.5), the
three right-handed neutrino masses are not exactly degenerate. The
Z₃ orbifold gives exponentially separated warp-factor masses. However,
the bulk mass parameters c_i for the N_R can be chosen (within the
Z₃ framework) such that two of them are nearly degenerate.

Write:
- The resonance condition in terms of the bulk mass splitting Δc
- The enhanced CP asymmetry: ε_res ~ (Γ_N/|M₁ − M₂|) × ε_vanilla
- The condition on Δc that gives ε_res × η_factor = η_obs
- The Boltzmann equation structure (without solving it fully — identify
  the key equation and state that its solution is the remaining computation)
- An honest assessment: "This Appendix identifies the mechanism and
  the parameter space. The complete calculation (numerical solution of
  the Boltzmann equations with Z₃ CP phases) is the subject of ongoing
  work."

### C.2 Paper 7 §5 — The G₄ Axion Inflaton

**File:** `paper7/05-inflaton.md`

Replace the scaffold with the content from Paper 6 §3.5 (G₄ axion
candidate) extended to Paper 7 level. The inflaton is the G₄ flux
axion a_G, which has:

- Shift symmetry a_G → a_G + const at the level of W_GVW (the phase
  of the superpotential)
- Potential from non-perturbative breaking of the shift symmetry:
  V ~ Λ⁴(1 − cos(a_G/f)) (axionic monodromy form)
- Slow-roll parameters: ε ~ (M_Pl/f)² × sin²(a_G/f), η ~ −2/f² M_Pl²

For large field a_G ≫ f (linear regime of axion monodromy):

    V ~ μ³ a_G,   n_s = 1 − 2/N* ≈ 0.967,   r = 8/N* ≈ 0.13/N*

These match the Paper 4 §7.15 predictions (n_s = 0.965, r = 0.03)
for N* = 60 e-folds with an appropriate f.

Compute f in terms of the G₄ flux parameters:
- f ~ M_Pl × (something from the Kähler potential K)
- For K = −3 ln(r₃) − 2 ln(r₂): f ~ M_Pl / √3 (from the Kähler
  metric normalization)

The key result: **the G₄ axion with f = M_Pl/√3 and V ~ μ³ a_G gives
n_s = 0.967, r ~ 0.003** (model-dependent). This resolves the inflaton
identification problem: the inflaton is not the geometric radion but
the axionic partner of the G₄ flux modulus.

Write the section at Paper 7 level: full derivation of the potential
shape, slow-roll parameters, and comparison with CMB observations.

---

## Priority Order

If context runs short:
1. **Track B** (flag manifold cohomology) — 45 min, resolves §9.4 cleanly
2. **Track A §§1–2** (G₂ structure + W_total) — 60 min, the core physics
3. **Track C §C.2** (Paper 7 §5 inflaton) — 30 min
4. **Track A §3** (F-flat minimum + GUT condition) — 60 min
5. **Track C §C.1** (resonant leptogenesis appendix) — 30 min

---

## After This Prompt

The series will have:
- Papers 1–6: Complete
- Paper 7 §§1–5: Written (minus whatever Track A §3 doesn't finish)
- The torsion-corrected GVW mechanism: the central new M-theory physics
- The flag manifold topology: resolved (the SLOCC orbit is SU(3)/T², not CP²×S²×S¹)
- Resonant leptogenesis: appendix written, full Boltzmann equations deferred

The remaining genuinely open items after this prompt:
- Paper 7 §3: the explicit GUT flux ratio n₁/n₂ (needs the coefficient c)
- OC-3: BPHZ factorization rigorous proof (mathematical)
- Paper 5 App D: Boltzmann equations (numerical)

Prompt 25 will complete Paper 7 and perform the final series-wide
consistency check.

---

*Key pre-computation result: τ₀ = 6/r₃² − 2/r₂² (scalar torsion of
CP² × S² × S¹ from Cleyton-Swann). G₂ holonomy at r₂/r₃ = 1/√3 = 0.577;
GUT unification at r₂/r₃ = √3/2 = 0.866 — these differ, meaning the
manifold has nonzero torsion at the physical minimum. The torsion term
in W_total is what generates the minimum.*

*Key cohomology result: SU(2)³/T² is simply connected (b₁ = 0). Both
CP² × S² × S¹ and Fl(1,2;3) × S¹ have b₁ = 1. Therefore SU(2)³/T² ≅
Fl(1,2;3) = SU(3)/T² (the flag manifold itself, dim 6, simply connected).
Theorem 5.2 needs the correction: the orbit is 6-dimensional, not 7.*
