# Closing the Open Problems: A Development Plan

*Story document. Five open problems, what's needed to close each,
and the dependencies between them.*
*Written April 5, 2026.*

---

## Overview

Five open problems remain across Papers 1–4. They range from a
specific three-loop computation to a deep mathematical conjecture
about entanglement and gauge groups. This document lays out what
each problem IS, what would close it, what tools we have, and
where the genuine unknowns lie.

| # | Problem | Paper | Difficulty | Impact |
|---|---|---|---|---|
| 1 | L = 3 explicit loop calculation | Paper 1 | Medium | High — strengthens all-orders conjecture |
| 2 | Moduli stabilization / freezing | Paper 4 §9.1 | Medium | High — resolves the hierarchy question |
| 3 | Update §9.3 (non-perturbative) | Paper 4 §9.3 | Low | Medium — consistency across papers |
| 4 | SLOCC-isometry map | Paper 4 §9.2 | High | **Critical** — deepest result in series |
| 5 | All-orders proof (general L) | Paper 1, Appendix K | High | High — theorem vs conjecture |

---

## Problem 1: The Three-Loop Explicit Calculation

### What It Is

Appendix K §K.2 identifies the Mercedes diagram as the key
three-loop topology. It has quadratic form:

    Q₃(n₁,n₂,n₃) = n₁² + n₂² + n₃² + n₁n₂ + n₂n₃ + n₁n₃

with Gram matrix:

         ⎛  1   1/2  1/2 ⎞
    A₃ = ⎜ 1/2   1   1/2 ⎟
         ⎝ 1/2  1/2   1  ⎠

det(A₃) = 1/2, eigenvalues 1/2, 1/2, 2, positive definite.

The Epstein zeta E₃(s; Q₃) has its pole at s = 3/2. The needed
values at s = 0, −1, −2, ... are finite (proved by Epstein-Terras).
The FINITENESS is guaranteed. The question is: **do they VANISH?**

At L = 2, the vanishing came from the factorization:

    E₂(s; Q₀) = 6 ζ(s) L(s, χ₋₃)

where Q₀ = n² + nm + m² is the norm form of the Eisenstein integers
Z[ω]. The complementary trivial zeros of ζ and L covered every
negative integer.

### What Needs to Be Done

**Step 1: Identify the lattice.**

The form 2Q₃ can be rewritten as:

    2Q₃ = (n₁+n₂)² + (n₂+n₃)² + (n₁+n₃)²

This is a sum of three squares of pairwise sums — related to the
D₃ lattice (= A₃ lattice in 3D). The question: does Q₃ correspond
to a lattice whose theta function factorizes through known
L-functions?

The D₃/A₃ lattice is the FCC lattice, whose theta function is:

    Θ_{D₃}(q) = (1/2)[θ₃(q)³ + θ₄(q)³]

where θ₃, θ₄ are Jacobi theta functions. The Epstein zeta is the
Mellin transform of this theta function. Whether it factorizes into
Dirichlet series (as the Eisenstein lattice did) depends on the
arithmetic of the lattice.

**Step 2: Compute E₃(−1; Q₃) explicitly.**

Use the functional equation of the Epstein zeta:

    π⁻ˢ Γ(s) E₃(s; Q₃) = det(A₃)⁻¹/² π⁻⁽³/²⁻ˢ⁾ Γ(3/2−s) E₃(3/2−s; Q₃⁻¹)

At s = −1: the left side has a pole from Γ(−1), the right side
evaluates E₃(5/2; Q₃⁻¹) which is an absolutely convergent sum.
The regularized value:

    E₃(−1; Q₃) = [−1/1!] × det(A₃)⁻¹/² × π⁻⁵/² × Γ(5/2) × E₃(5/2; Q₃⁻¹)

This is a specific number. Compute it. If it's zero: the
complementary-zeros mechanism extends to L = 3. If nonzero: the
three-loop counterterm coefficient is finite but nonzero — the
theory is still predictive but the complete vanishing story changes.

**Step 3: Check the other three-loop topologies.**

The sunset-bubble factorizes into a one-loop × two-loop product.
Since both factors vanish (the one-loop from S₀ = 0, the two-loop
from the complementary zeros), the product vanishes. ✓

The triple-bubble is (one-loop)³ = 0³ = 0. ✓

Only the Mercedes diagram is non-trivial.

**Step 4: If E₃(−1; Q₃) ≠ 0, characterize what happens.**

The theory is still finite (Epstein-Terras guarantees this). The
counterterm coefficient is a specific calculable number. The theory
remains predictive with no free parameters. What changes is the
narrative: "identically zero at every order" becomes "finite and
calculable at every order, with complete vanishing at L = 1, 2 and
specific nonzero values at L ≥ 3."

This is still a dramatic improvement over 4D gravity (where the
coefficients are divergent and undetermined).

### Tools Available

- Sage/Mathematica: Epstein zeta computation via theta function
  Mellin transforms
- LMFDB (L-functions and Modular Forms DataBase): lattice theta
  functions, Dirichlet series
- The Chowla-Selberg formula generalizes to ternary forms via
  Siegel's mass formula — may give closed-form expressions

### Estimated Effort

The numerical computation of E₃(−1; Q₃) is straightforward
(convergent series, computable to arbitrary precision). The
algebraic identification of the lattice and its L-function
factorization is the harder part. **1–2 sessions for the numerical
result; 1–2 more for the algebraic structure.**

---

## Problem 2: Moduli Stabilization (or Freezing)

### What It Is

Paper 4 §9.1 lists the moduli of CP² × S² × S¹:
- R (e-circle radius): stabilized/frozen by Casimir (Paper 1)
- r₂ (S² radius): **to be stabilized**
- r₃ (CP² Kähler modulus): **to be stabilized**
- Cross-moduli (shape deformations): **to be stabilized**

The original expectation was Casimir + Goldberger-Wise stabilization.
But Paper 6 §2.3 revealed: the perturbative Casimir potential
V = −c/R⁴ is EXACT (no Goldberger-Wise term at any perturbative
order). The potential has NO minimum. The dilaton is frozen by
Hubble friction at ε ~ 10⁻⁵².

### The Key Insight

If the Epstein zeros mechanism kills higher-loop corrections for
the e-circle, **it should kill them for ALL the internal moduli**.
The same structural argument applies:

- On S²: the KK masses are m_l = l(l+1)/r₂². The spectral zeta
  on S² sums over angular momentum modes. The leading sum
  Σ_l (2l+1) is the zeta-regularized mode count on S², which
  should also vanish under the appropriate spectral zeta.

- On CP²: the KK spectrum is labeled by SU(3) representations.
  The spectral zeta involves sums over Casimir eigenvalues of
  SU(3), which are polynomials in two quantum numbers.

If the higher-loop corrections vanish for ALL internal dimensions,
then:

    V(R, r₂, r₃) = V_Casimir(R, r₂, r₃) = −c(r₂, r₃)/R⁴ − c'(R, r₃)/r₂⁴ − c''(R, r₂)/r₃⁴ + ...

is the EXACT potential. No minimum exists for any modulus. ALL
moduli are frozen by Hubble friction.

### What Needs to Be Done

**Step 1: Compute the one-loop Casimir energy on CP² × S² × S¹.**

The heat kernel on a product manifold factorizes:

    K_{CP² × S² × S¹}(t) = K_{CP²}(t) × K_{S²}(t) × K_{S¹}(t)

The spectral zeta functions for each factor are known:
- S¹: Riemann zeta (Paper 1, Appendix F)
- S²: Hurwitz zeta from angular momentum sum
- CP²: zeta function of the Laplacian on CP² (known in the
  mathematical literature, e.g., Berger 1965, Ikeda & Taniguchi 1978)

The full Casimir energy as a function of (R, r₂, r₃) is the product
of these. Compute it. Determine whether it has a minimum or whether
all three moduli run away (as R does).

**Step 2: Apply the Epstein zeros argument to each factor.**

At two loops, the complementary zeros killed the corrections for
the S¹ factor. Check whether analogous zeros exist for:
- The S² spectral zeta: sums over l(l+1) with degeneracy (2l+1)
- The CP² spectral zeta: sums over SU(3) Casimirs

If the zeros persist: the one-loop Casimir energy is exact for all
moduli. No minimum. All frozen by Hubble friction.

If the zeros DON'T persist for S² or CP²: higher-loop corrections
exist and could create a minimum. This would stabilize r₂ and r₃
at specific values — computable from the Epstein zeta values.

**Step 3: Address the hierarchy R ≫ r₂ ≫ r₃.**

If all moduli are frozen: the hierarchy R ≫ r₂ ≫ r₃ is set by
initial conditions at the compactification phase transition.
This is less satisfying than a dynamical stabilization, but it's
honest. The hierarchy becomes a question about cosmological
initial conditions, not about the potential.

If r₂ and r₃ ARE stabilized (at minima of the Casimir + higher-loop
potential): the hierarchy is dynamical and potentially calculable.
This would be a major result — deriving the gauge coupling hierarchy
from the Casimir energy.

### Estimated Effort

Step 1 is a definite computation using known spectral data.
**1–2 sessions.** Step 2 requires understanding the arithmetic of
the S² and CP² spectral zeta functions — whether their Dirichlet
series have complementary zeros. **1–2 sessions.** Step 3 depends
on the outcomes.

---

## Problem 3: Update Paper 4 §9.3

### What It Is

Paper 4 §9.3 (Non-Perturbative Completion) was partially updated
during the M-brane classification work but should now reference:

1. Paper 3, Appendix A's three-layer argument (perturbative
   finiteness → non-perturbative stability → M-theory completion)
2. The exp(−10³⁰) suppression of all non-perturbative effects
   (Paper 1, Appendix J)
3. The M-brane classification (Paper 4, Appendix B)

### What Needs to Be Done

Rewrite §9.3 to reflect the current state. The "non-perturbative
completion" is no longer a single open question — it's a three-layer
structure where two layers are established and one (the formal
M-theory path integral) is inherited.

The section should also note: if Problems 1 and 2 above are resolved,
the perturbative side becomes even stronger (explicit L = 3
calculation + moduli understanding).

### Estimated Effort

**1 hour.** Straightforward rewrite using existing material.

---

## Problem 4: The SLOCC-Isometry Map

### What It Is

Conjecture 5.1 (Paper 4, §5.4) claims: the entanglement geometry
of three fermionic generations on the e-circle spans the internal
space CP² × S², with the gauge group emerging as the isometry group.

The mathematical content (§5.5): the tangent space to the SLOCC
orbit at the GHZ point should have the same Lie algebra structure
as the isometry algebra of CP² × S² × S¹.

This draws on Szangolies (2025), who showed that three qubits in
(9+1)D reduce to 3+1D with residual gauge group
SU(3) × SU(2) × U(1)/Z₆.

### What Needs to Be Done

**Step 1: The tangent space calculation.**

At the GHZ state |GHZ⟩ = (|000⟩ + |111⟩)/√2, compute the tangent
space to the SLOCC orbit:

    T_{GHZ} = {(A₁ ⊗ I ⊗ I + I ⊗ A₂ ⊗ I + I ⊗ I ⊗ A₃)|GHZ⟩ : Aᵢ ∈ sl(2,C)}

This is a linear algebra calculation in C⁸. The tangent space has
dimension 14 (= 3 × 6 − 4 stabilizer directions). Its structure
as a representation of the stabilizer (Z₂)³ determines the
decomposition.

**Step 2: The isometry algebra decomposition.**

The isometry algebra of CP² × S² × S¹ is:

    su(3) ⊕ su(2) ⊕ u(1) = 8 + 3 + 1 = 12 dimensions

The tangent space to the internal manifold at a point is
7-dimensional (4 from CP², 2 from S², 1 from S¹). The isometry
algebra acts on this tangent space. Decompose the 7D tangent space
under su(3) ⊕ su(2) ⊕ u(1).

**Step 3: Match the two decompositions.**

Show that the SLOCC tangent space decomposition (Step 1) and the
isometry tangent space decomposition (Step 2) are isomorphic as
representations of the stabilizer/gauge group.

This is the key calculation. If the decompositions match, the
conjecture is proved — the gauge group IS the entanglement geometry.

**Step 4: Understand the Z₆ quotient.**

Szangolies gets SU(3) × SU(2) × U(1)/Z₆ — with the Z₆ quotient.
The Z₆ in the SM is the kernel of the hypercharge embedding. Show
this quotient arises naturally from the SLOCC stabilizer structure
(Z₂)³ → Z₆ through the specific identification of qubits with
generations.

### What's Hard

The challenge is not the individual calculations (Steps 1–3 are
linear algebra). The challenge is the IDENTIFICATION: why should
the SLOCC equivalence classes of three qubits map to the isometry
classes of 7-manifolds? The Szangolies result shows they DO (as a
mathematical fact). The framework claims they do because
entanglement IS geometry (Papers 1–3). Turning this philosophical
claim into a theorem requires showing that the e-dimension
identification (entanglement = e-conservation) IMPLIES the SLOCC-
isometry correspondence.

### Possible Route

The most promising route is through the orbit method (Kirillov):

1. SLOCC orbits in (C²)⊗³ are coadjoint orbits of SL(2,C)³
2. The orbit through GHZ has stabilizer (Z₂)³
3. The quotient SL(2,C)³/(Z₂)³ acts on the 14D orbit
4. The COMPACT real form of this quotient is SU(2)³/(Z₂)³
5. The residual symmetry on the 7D physical space (after removing
   the 7 gauge directions from the 14D orbit) is:
   SU(2)³/(Z₂)³ acting on 7 dimensions

The question: is SU(2)³/(Z₂)³ → SU(3) × SU(2) × U(1)/Z₆ a
known mathematical correspondence? This would connect to the
exceptional isomorphisms of low-dimensional Lie groups.

### Estimated Effort

Steps 1–3 are concrete calculations: **2–3 sessions.** Step 4 and
the orbit-method route are deeper: **multiple sessions, potentially
a standalone paper.** This is the deepest open problem in the series
and the one most worth solving.

---

## Problem 5: All-Orders Proof (General L)

### What It Is

The all-orders finiteness conjecture (Appendix K, §K.6) has three
parts:
- (i) S₀^L = 0: **proved**
- (ii) Subleading terms reduce to Epstein zeta at s ≤ 0: **unproved
  for L ≥ 3** (the overlapping subdivergences gap, §K.5.2)
- (iii) Epstein zeta is finite at s ≤ 0: **proved** (Epstein-Terras)

The gap is (ii): showing that the BPHZ forest formula preserves the
Epstein zeta structure at L ≥ 3.

### What Needs to Be Done

**Route A: The spectral zeta approach (Appendix S §S.5).**

On any compact Riemannian manifold, the one-loop effective action
ζ'(0) is finite because s = 0 is below the smallest spectral zeta
pole at s = 1/2. The multi-loop generalization would use the
Kontsevich-Vishik (1995) theory of generalized zeta functions for
pseudodifferential operators.

The claim to establish: the L-loop gravitational kinetic operator
on M⁴ × S¹ satisfies the Kontsevich-Vishik symbol class conditions.
This is a statement about the symbol of the operator (its leading
behavior in momentum space), which is determined by the principal
symbol of the 5D d'Alembertian — a standard pseudodifferential
operator.

If the symbol class conditions are satisfied, the generalized zeta
function is well-defined and holomorphic at s = 0, giving finiteness
at every loop order — without needing to reduce to Epstein zeta
functions at all. This would bypass the overlapping subdivergences
issue entirely.

**Route B: The BPHZ forest formula approach.**

Show directly that the BPHZ counterterm subtraction preserves the
factorization into 4D momentum integrals × KK mode sums. The key
property to establish: after subtracting all subdivergence
counterterms via the forest formula, the FINITE remainder at L
loops has KK mode sums that are polynomial in the KK masses
m_n² = n²/R² — ensuring that the Seeley-DeWitt mass expansion
structure is preserved.

This is a statement about the polynomial structure of the BPHZ
R-operation applied to KK Feynman integrals. It may follow from
the locality of the counterterms (counterterms are polynomial in
momenta and masses by Weinberg's theorem) combined with the
product manifold structure (KK masses enter only through the
internal spectrum).

**Route C: Prove it at L = 3 explicitly (Problem 1), then L = 4.**

If the factorization holds at L = 3 (verified by explicit
computation), and at L = 4, the pattern becomes compelling. The
conjecture would then rest on L = 1, 2, 3, 4 explicit checks plus
the structural argument — much stronger than L = 1, 2 plus
structure.

### The Honest Assessment

Route A (Kontsevich-Vishik) would give the cleanest result but
requires expertise in pseudodifferential operator theory. Route B
(BPHZ factorization) is more hands-on but technically demanding.
Route C (explicit computation) is the most concrete but doesn't
give a general proof.

The most realistic path: **do Route C first** (resolve Problem 1),
then attempt Route A or B informed by the explicit structure seen
at L = 3.

### Estimated Effort

Route C (L = 3 explicit): tied to Problem 1. **2–4 sessions.**
Route A (Kontsevich-Vishik): **substantial** — requires reading
the KV paper and translating to the KK context. Multiple sessions.
Route B (BPHZ factorization): **substantial** — multi-loop
renormalization theory. Multiple sessions.

---

## Dependencies and Priority Order

```
Problem 3 (update §9.3) ← standalone, do anytime
     ↑
Problem 1 (L=3 explicit) → feeds into → Problem 5 (all-orders)
     ↑                                        ↑
Problem 2 (moduli)  ← partially independent   |
     ↑                                        |
[Spectral zeta on S², CP²]                   |
                                              |
Problem 4 (SLOCC map) ← independent     Route A (KV theory)
```

**Recommended execution order:**

1. **Problem 3** first — quick, brings §9.3 up to date
2. **Problem 1** next — the L = 3 calculation is the highest-value
   move, concrete and informative regardless of outcome
3. **Problem 2** in parallel with 1 — the spectral zeta on S² and
   CP² can be computed independently
4. **Problem 5** after 1 — informed by whatever the L = 3
   calculation reveals
5. **Problem 4** when ready — the deepest problem, potentially a
   standalone paper, can proceed in parallel with everything else

---

## What Success Looks Like

**If Problems 1–3 are resolved:**

The framework has explicit perturbative finiteness through 3 loops,
the moduli are understood (either frozen or stabilized), and the
papers are internally consistent. The all-orders conjecture rests
on L = 1, 2, 3 explicit checks — strong evidence.

**If Problem 4 is resolved:**

The Standard Model gauge group is derived from entanglement geometry.
This is arguably the deepest result in theoretical physics: why
SU(3) × SU(2) × U(1) is answered by "because that's the geometry
of three-qubit entanglement." The framework goes from "a geometric
account of quantum mechanics that happens to embed in M-theory" to
"the reason the laws of physics have the structure they do."

**If Problem 5 is resolved:**

The perturbative finiteness of 5D KK gravity becomes a THEOREM,
not a conjecture. The e-circle that explains quantum mechanics also
solves the UV divergence problem of quantum gravity — rigorously,
at all orders.

---
