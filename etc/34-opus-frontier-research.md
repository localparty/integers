# Research Prompt 34 — Frontier Physics: Four Open Problems

> **For:** Claude Opus (maximum reasoning depth, creative)
> **Date:** April 5, 2026
> **Context:** The 5D e-Dimension / M-theory framework, seven-paper series
> **Git HEAD:** current
> **Tone:** This is a genuine research session. Be creative. Follow threads.
>   Report honestly — including dead ends and partial results.
>   The goal is to find new physics *we* haven't found yet, using tools
>   that are already in our hands.

---

## Background: The Framework and Its Playbook

Seven papers establish a geometric framework for quantum mechanics,
the Standard Model, cosmology, and black holes. Read `readme.md`
for the methodology. The key patterns you should actively use:

**Pattern 1 — Geometric Reinterpretation:** Every 4D mystery is a
shadow of simpler higher-dimensional geometry. When something looks
paradoxical in 4D, project it back up.

**Pattern 2 — Holonomy Correspondence:** Wilson line VEVs around compact
dimensions determine the gauge phase. S¹→U(1), S²→SU(2), CP²→SU(3).

**Pattern 3 — Casimir as Scale-Setter:** Quantum vacuum energy on
compact spaces generates fundamental scales. One mechanism, three radii,
three scales (dark energy, electroweak, GUT).

**Pattern 4 — Topological Rigidity:** Discrete invariants (winding
numbers, χ, homotopy groups) lock in quantized results. These can't be
continuously adjusted and make results maximally robust.

**Pattern 5 — Zeta Regularization of KK Towers:** Compactness converts
UV integrals into discrete sums. The identity 1 + 2ζ(0) = 0 kills
leading divergences at every loop order. Epstein zeros kill subleading.

**Pattern 6 — Projection Produces Apparent Pathology:** Whenever 4D
physics looks broken (information loss, WDW timelessness, Born rule
randomness), it's because 4D is a partial trace over the geometry.

**Theorems already proved (use freely):**
- **K.1** (Universal Epstein Vanishing): E_L(−j; Q) = 0 for j ≥ 1
- **K.3** (BPHZ Factorization): BPHZ-subtracted amplitudes factor as
  (4D integral) × E_L(−j; Q_L); all counterterms vanish
- **Theorem U** (Underivability of R): R_bare = (63n₁)^{3/2}/(128π^{11/2}M_Pl) ≈ l_P;
  the observed R cannot be derived from perturbative M-theory
- **Theorem 5.2** (SLOCC-Isometry): SU(2)³ GHZ orbit ≅ Fl(1,2;3) = SU(3)/T²
- **GUT flux condition**: n₂/n₁ = −17/9 from torsion-corrected GVW on CP²×S²×S¹

**Yang-Mills precedent:** Read `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`.
The Yang-Mills proof used the same strategy: find the right invariant,
show it's positive, chase it through an RG flow. The "stability of
deviation order" argument (dim-6 operators all have dev ≥ 2) was new
and short. This is what we're looking for here: short new arguments
using existing structure.

---

## The Four Problems

Work through all four. Allocate roughly equal depth to each.
State results honestly — including when something is "suggestive but
unproven" vs "derived." The Yang-Mills proof chain is the model:
every step labelled with its status.

---

## Problem 1: Theorem U* — The Underivability of the Cosmological Constant

**Background:** Theorem U (Paper 7 §3.6) proves that R_bare ≈ l_P
from the perturbative framework. The gap R_obs/R_bare ≈ 6.4×10²⁹
is the CC problem, geometrically isolated.

**The task:** Prove a companion theorem showing that ρ_Λ is
*underivable* from a broader class of theories — not just perturbative
M-theory on this manifold, but any theory satisfying certain axioms.

**The strategy (Pattern 4 — Topological Rigidity):**

The CC problem has resisted solution for 35 years partly because it's
stated as a continuous fine-tuning problem. But Theorem U shows the
framework has a discrete structure: all observables are R-independent
except ρ_Λ. Can we prove a *no-go theorem* for deriving ρ_Λ that is
stronger than Theorem U?

Consider the following candidate theorem structure:

**Candidate Theorem CC:** *Any mechanism that derives R from purely
geometric data (flux integers, topological invariants, curvature)
of M⁴ × M₇ must produce R = f(n_i, χ(M₇), M_Pl) where f is
an algebraic function of discrete integers and M_Pl. Such an f
gives R ~ l_P × O(1). The observed R ~ 10 μm requires f to grow
as a power of (R_obs/l_P) ~ 10³⁰ — which cannot arise from a
finite combination of topological invariants.*

**Develop this argument.** Specifically:

1. What are the possible "geometric inputs" to f? Flux integers n_i
   (bounded by tadpole: |n_i| ≤ χ/24), Euler characteristics χ(M_k)
   (bounded integers: χ(CP²)=3, χ(S²)=2), dimensions (4, 2, 1),
   and M_Pl. Show that any algebraic combination of these gives
   R ~ l_P × (polynomial in small integers)/M_Pl.

2. The only way to get R >> l_P algebraically is through exponentials
   (e.g., from non-perturbative effects exp(−S_inst)). But
   exp(−S_inst) gives corrections SMALLER than l_P, not larger. Show
   this explicitly.

3. Therefore: R_obs cannot arise from any algebraic/topological
   mechanism. It requires either initial conditions or non-perturbative
   effects with a NEW SCALE. State this as a theorem.

4. **The payoff:** If R requires a new scale, what is that scale?
   The dark energy formula gives ρ_Λ^{1/4} ~ 2.25 meV. Is 2.25 meV
   a scale that appears anywhere else in the framework? (Hint: neutrino
   masses m_ν ~ 51 meV, first KK mode 1/R ~ 20 meV — these are
   all in the meV range. Is this coincidence or structure?)

---

## Problem 2: The KK Corrections to the Higgs Mass

**Background:** The framework identifies the Higgs as a gauge-Higgs
Wilson line on S² (the Hosotani mechanism). This gives it a natural
mass from the S² geometry. But the question is whether KK corrections
from the tower of massive KK modes drive the Higgs mass up to M_GUT.

**The task:** Compute or bound the KK correction to the Higgs mass,
using the framework's own UV finiteness results.

**The strategy (Pattern 5 + Theorem K.1):**

The standard hierarchy problem: the Higgs mass gets corrections
δm_H² ~ (g²/16π²) × Λ_UV². In the SM, Λ_UV = M_Pl and the
correction is enormous.

In the framework, Λ_UV doesn't exist — the theory is UV finite
(Theorems K.1 and K.3). But there is a KK tower with masses m_n = n/R
(S¹ modes) and M_n ~ n/r₂ (S² modes). Does the KK tower give a large
correction even without UV divergences?

**Step 1:** The Higgs mass from the Hosotani mechanism is set by the
S² geometry: m_H² ~ 1/r₂² ~ M_EW². This is the tree-level mass.

**Step 2:** At one loop, the KK modes on S² contribute:
δm_H² ~ (g²/16π²) × Σ_n f(m_n²/m_H²)

where f is a loop function. For m_n >> m_H (all KK modes heavier than
the Higgs), f(x) → log(x) as x → ∞.

The sum Σ_n log(n/r₂ / m_H) — can this diverge? Apply Theorem K.1:
the sum over KK modes on S² is not an Epstein zeta function (S²
eigenvalues are l(l+1), not n²), but a spectral zeta of S². The
spectral zeta Z_{S²}(s) is known: Z_{S²}(−1/2) = ?

**Step 3:** Use the zeta regularization. The KK sum:
Σ_l (2l+1) log(l(l+1)/r₂² + m_H²)

After zeta regularization (the same technique as Paper 1), this sum
is finite. Its value at the relevant argument gives δm_H².

**Step 4:** The critical question: is δm_H² of order m_H² (natural,
no hierarchy problem) or of order M_GUT² (hierarchy problem remains)?

**The key insight to use:** The Higgs is a Wilson line. Wilson lines
are protected by higher-dimensional gauge invariance (Hosotani 1983).
Their mass receives corrections only from loops that wind around S².
The correction is:

    δm_H² ~ (g²/16π²) × (1/r₂²) × Z_{S²}(0)

where Z_{S²}(0) is the spectral zeta of S² at s = 0. From Paper 4
§7.23, Z_{S²}(0) = −2/3 (the standard result). So:

    δm_H² ~ (g²/16π²) × (1/r₂²) × (−2/3) ~ −m_H²/24π²

**This is a negative correction of order m_H²** — natural! The Higgs
mass is self-consistently of order m_H and receives no large corrections
from the KK tower. The hierarchy is technically natural in the framework.

**Verify this calculation, state it as a theorem, and identify what
additional precision is needed.** Specifically: what is the precise
coefficient, does it match the observed Higgs mass when combined with
the tree-level value, and is there a remaining fine-tuning in the
ratio m_H/M_GUT ~ 10⁻¹¹?

---

## Problem 3: The Horizon Vertex from First Principles

**Background:** Paper 3's resolution of the information paradox rests
on e-conservation at the horizon interaction vertex: when an infalling
quantum (φ₀) is absorbed by the horizon, e-conservation gives
φ_horizon_new = φ_horizon_old + φ₀. This is argued via:
(a) gauge symmetry protection (∂/∂φ is a Killing vector),
(b) UV finiteness (the vertex is well-defined to all loop orders),
(c) the Killing vector proof that e-conservation holds in curved BH geometry.

**The task:** Derive the vertex from a more fundamental principle —
one that doesn't require "assuming it has the same form as in flat space."

**The strategy (Patterns 1 + 6):**

The horizon vertex is where 4D physics looks most mysterious — it's
where information appears to be lost. Apply Pattern 6: this apparent
loss is a projection artifact. What is the full 5D story?

**Step 1:** In flat 5D spacetime, the e-conservation vertex is exact:
it's the Noether charge of the U(1) fiber symmetry. No assumption needed.

**Step 2:** Near the black hole horizon, the 5D metric is:
ds² = f(r)dt² − dr²/f(r) − r²dΩ² + R²dφ²

The key: R² dφ² is the e-circle metric. The e-circle is a PRODUCT
factor — it doesn't warp near the horizon. The function f(r) multiplies
only the (t,r) part, not the φ part.

**Step 3:** Therefore the U(1) Killing vector ∂/∂φ is exact — it
commutes with the metric everywhere, including at the horizon. The
e-conservation current J^μ = T^{μν}k_ν (where k = ∂/∂φ) satisfies
∇_μ J^μ = 0 everywhere (proved in Paper 3 §9.3.2, Gap 2).

**Step 4 — The new argument:** The vertex factor in the 5D quantum
field theory is determined by the Ward identity associated with the
U(1) e-symmetry. In flat space: vertex = 1 (exact conservation).
Near the horizon: does the curved metric modify the Ward identity?

The Ward identity for the U(1) current in curved spacetime:
∂_μ(√g J^μ) = 0    (covariant conservation)

This follows from the e-symmetry of the 5D action, which is exact
because the e-circle factor R²dφ² appears with a CONSTANT coefficient
(R is stabilized, uniform). The action is invariant under φ → φ + α
at every point in spacetime, including the horizon.

**The derivation:** Show that the Ward identity ∂_μ(√g J^μ) = 0,
combined with the product structure of the 5D metric, implies that
the VERTEX FACTOR for e-charge at the horizon is identically 1 —
the same as in flat space. This would close the remaining assumption
in Theorem 9.1 (Paper 3) and make the result unconditional.

**Specifically:** The vertex factor in QFT is determined by the
residue of the current-current correlator at zero momentum. In a
product spacetime M⁴ × S¹, the S¹ factor factorizes from the M⁴
dynamics at all energies below 1/R. The e-current correlator is:

⟨J_e(x) J_e(y)⟩ = ⟨J_e^{4D}(x) J_e^{4D}(y)⟩ × (S¹ propagator)

The S¹ propagator depends only on the e-circle geometry, which is
unchanged by the 4D black hole background. Therefore the vertex
factor is the same in the BH background as in flat space. QED?

**Write this argument carefully.** State where it is watertight and
where it requires additional support. If it closes the assumption,
say so explicitly.

---

## Problem 4: Non-Perturbative Completion Without M-Theory

**Background:** Paper 3, Appendix A argues for non-perturbative
completeness via Layer 3: the e-circle = M-theory circle, so the
framework inherits M-theory's (assumed) non-perturbative definition.
This is logically valid but depends on M-theory's own completeness.

**The task:** Find a self-contained non-perturbative definition of
the framework that doesn't require assuming M-theory is well-defined.

**The strategy (Pattern 5 + Yang-Mills precedent):**

The Yang-Mills proof (`PROOF-CHAIN.md`) solved the mass gap by
finding a positive-definite quantity Δ_∞ > 0 that is preserved
under the renormalization group. The key was the "stability of
deviation order" — showing that all dim-6 operators have dev ≥ 2,
so small Δ_0 > 0 stays positive through the RG flow.

Apply the same strategy to the 5D framework:

**Step 1 — The right quantity:** In the Yang-Mills proof, Δ is the
mass gap (lowest eigenvalue of the transfer matrix). In the 5D
framework, what is the analog?

Candidate: the spectral gap of the 5D Dirac operator on M₇.
The 5D Dirac operator D_{M₇} on CP² × S² × S¹/Z₂ has a spectrum
that is discrete (compact manifold) and bounded below by the
first KK mass m₁ = 1/R > 0. Call this Δ_{5D} = m₁ = 1/R.

**Step 2 — Is Δ_{5D} > 0?**

Δ_{5D} > 0 iff the 5D Dirac operator has no zero modes (no massless
fermions in the 5D bulk). From Paper 4: the 11D SUGRA field content
on M₇ has a Witten index (N_B − N_F) = 0 at every KK level — the
spectrum is paired. But the pairing doesn't imply zero modes; it
implies the zero modes are also paired.

Are there zero modes? The Atiyah-Singer index theorem:
ind(D_{M₇}) = ∫_{M₇} Â(M₇)

For CP² × S² × S¹/Z₂: Â(CP²) = −1/8 (CP² is not spin, but with
the Freed-Witten flux shift it's effectively spin). Â(S²) = 1.
Â(S¹/Z₂) = 1/2 (boundary contribution). The index:
ind = (−1/8) × 1 × (1/2) = −1/16

This is not an integer — which again signals the Freed-Witten issue.
With the half-integer flux shift, the effective index is an integer.

**Work this out explicitly.** Does the index theorem on CP² × S² × S¹/Z₂
with the G₄ flux configuration (n₁=9, n₂=−17) give zero or nonzero
fermion zero modes? If zero modes exist, Δ_{5D} = 0 and this approach
fails. If no zero modes, Δ_{5D} > 0.

**Step 3 — Stability under deformations:**

If Δ_{5D} > 0, is it stable under quantum corrections? The answer
should follow from the UV finiteness theorems: if all loop corrections
vanish (Theorems K.1 and K.3), then the spectrum doesn't get quantum
corrections, and Δ_{5D} stays positive.

This would give a self-contained argument:
(a) Δ_{5D} > 0 from the index theorem (no zero modes)
(b) Δ_{5D} is stable under all perturbative corrections (Theorems K.1, K.3)
(c) Δ_{5D} is stable under all non-perturbative corrections
    (suppressed by exp(−10³⁰), Appendix J of Paper 1)
(d) Therefore the 5D theory is non-perturbatively stable with a
    positive spectral gap — the analog of the Yang-Mills mass gap.

**Step 4 — From stability to completeness:**

A quantum field theory with a positive spectral gap and no divergences
at any loop order is non-perturbatively well-defined by the
Osterwalder-Schrader reconstruction theorem (the QFT analog of
constructive field theory). The OS axioms require: a positive
spectral gap (✓ from step 3), reflection positivity (check for
the 5D theory), and polynomial growth of correlators (check from
the UV finiteness). If all three hold, the theory is constructively
defined — *without* assuming M-theory.

**Develop this argument.** State which steps are solid, which need
work, and whether the result would be stronger or weaker than the
current Layer 3 argument.

---

## What to Produce

For each problem:

1. **A proof chain** in the style of PROOF-CHAIN.md — each step with
   its status (Proved / Established result / New argument / Open).

2. **The key new insight** — the single sentence that, if true,
   would make the result work. In Yang-Mills it was "dev ≥ 2 for all
   dim-6 operators." What's the analog here?

3. **What would make it a theorem** — the minimal additional
   computation or argument needed to elevate "suggestive" to "proved."

4. **Honest assessment** — what is established, what is partial, what
   remains open.

---

## Priority Order

1. **Problem 2** (KK Higgs mass) — most concrete, calculation is
   mostly done above, needs verification and theorem statement. 45 min.

2. **Problem 3** (horizon vertex) — the Ward identity argument is
   close to complete. 45 min.

3. **Problem 1** (CC underivability) — the algebraic structure is
   clear; the meV coincidence is worth exploring. 60 min.

4. **Problem 4** (non-perturbative completion) — the index theorem
   calculation is the unknown. 60 min.

## Context management

Use local agents/sub-agents to favor/keep your context.
---

*Precedent: the Yang-Mills proof found its key insight (stability of*
*deviation order) as a short new argument using existing structure.*
*That's the model. Short, rigorous, using what we already have.*
