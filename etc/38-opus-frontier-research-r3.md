# Research Prompt 38 — Frontier Round 3: Three Targeted Proofs

> **For:** Claude Opus — maximum reasoning, fully agentic
> **Date:** April 6, 2026
> **Repository:** `/Users/gsix/quantum-geometry-in-5d-latex/`
> **Yang-Mills proof chain:** `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`
> **Session model:** Use local sub-agents per problem. Each sub-agent
>   reads its own file list, runs its own web searches, and writes
>   one output file. Stop and report honestly; no overclaiming.

---

## Before You Start — Read These First

Every argument in this framework was produced by one of six patterns.
Every proof that worked borrowed structure from the Yang-Mills proof.
Read both before doing any computation:

1. `etc/pattern-attribution-map.md` — the six patterns; which result
   each produced; which patterns remain unused on each open problem.
   **The unused pattern is usually the key.**

2. `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md` — the complete
   proof chain table. The five moves that unlocked it:
   - **Move 1:** Transfer matrix positivity → Δ₀^KK > 0
   - **Move 2:** Stability of deviation order → all dim-6 ops have dev ≥ 2
   - **Move 3:** Bogomolny/index bounding → non-trivial sectors suppressed
   - **Move 4:** Product manifold lemma → RP on M₁ × M₂
   - **Move 5:** Dim-6 classification → Newton decomposition exact

3. `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`
   — the product manifold RP proof. Lemma D.1 is the key lemma for
   Problem 1. Read the proof carefully; it applies directly.

4. `/Users/gsix/yang-mills/preprint/sections/C-transfer-matrix.md`
   — transfer matrix construction. The Feshbach projection argument
   for Problem 1 mirrors Theorem 5 of this appendix exactly.

The Yang-Mills proof's single new contribution was short:
"all dim-6 operators have dev ≥ 2." For each problem below, find
the analogous short structural argument that unlocks the proof.

---

## What Has Already Been Done — Do Not Redo

Round 2 (Prompt 37) established:

**Problem B (OS3) — partially done:**
- Exact OS3 for linearized 5D theory: **proved** (Theorem A.1,
  Paper 3 Appendix A §A.8 — via Lemma D.1 + FP determinant positivity)
- Exact OS3 for IR regime (E ≪ m_KK): **proved** (Theorem A.2 — via
  Feshbach projection + stability of deviation order)
- Exact OS3 for full nonlinear theory: **conditional** on one assumption:
  the gauge-fixed 5D Euclidean path integral measure is positive for
  all configurations with fixed M⁴ × S¹ topology.

The conditional assumption is what remains. Read the full argument
at `paper3/15-appendix-a-non-perturbative-completion.md` §A.8 before
continuing. The gap is precisely identified.

**Problem A (5/2 hint) — negative result reached:**
- The APS eta invariant η(D_{S¹/Z₂}) = −1/2 is exact.
- χ(CP²) + η = 5/2 is a mathematical identity.
- No physical mechanism produces this additive combination in the
  framework — index theorems give multiplicative contributions.
- Result filed in `etc/frontier-research/problem-A-overlap-5half.md`.
- A new route exists: the spin^c index on CP² × S¹/Z₂ with twisted
  Wilson line coefficients. Not computed. Could give non-integer results
  including half-integers if APS boundary corrections enter.

**Problem C (E₈ tadpole) — gap precisely identified:**
- I₈ = 0 for all natural 8-manifold candidates (proved).
- The 1/8 residue comes from the flux quantization, not the
  gravitational source.
- The E₈ gauge bundle c₂(V_vis) on CP² is the missing ingredient.
- The SM embedding E₈ → E₆ × SU(3) → SM is well-defined.
- Read `paper7/appendix-B-freed-witten.md` §B.6 for the current state.

---

## The Three Problems

---

## Problem 1: Discharge the OS3 Conditional Assumption

### What needs to be proved

The one remaining conditional in Theorem A.3 (Paper 3, Appendix A §A.8):

> *The gauge-fixed 5D Euclidean path integral measure on M⁴_E × S¹
> is positive for all field configurations with fixed M⁴ × S¹ topology.*

This is the full nonlinear extension of what is already proved at the
linearized level (FP determinant = 4π²R₀² > 0, exact and computable).

### The route most likely to work: Mazur-Mottola in 5D

Mazur and Mottola (Nucl. Phys. B 341, 187, 1990) showed in pure 4D:

> *The generally covariant functional measure on the space of 4D metrics
> renders the conformal mode non-propagating via a nonlocal field
> redefinition χ = √(−∇²) σ, giving a convergent Euclidean path integral.*

In the 5D framework, the conformal mode IS the KK dilaton δR. The 5D
analog would show that the 5D generally covariant functional measure
renders δR non-propagating — making the wrong-sign 4D kinetic term an
artifact of a non-covariant gauge choice (4D Einstein frame), not a
feature of the physical measure.

**The specific task:**

Step 1. Read Mazur-Mottola (1990) — abstract and key sections. The paper
is well-known; search arXiv for "Mazur Mottola conformal factor gravity
path integral" to find related work and modern treatments.

Step 2. Identify the key structural fact that makes Mazur-Mottola work
in 4D. Is it: (a) the non-compactness of the conformal group, (b) the
specific form of the De Witt metric on the space of metrics, (c) the
covariance argument, or (d) something else?

Step 3. Ask: does the 5D version on M⁴ × S¹ inherit this structure?
The S¹ factor provides compactness in one direction — does this help
or hurt the Mazur-Mottola argument?

Specifically: in 5D, the "space of metrics" on M⁴ × S¹ is fibered
over the S¹ modulus R. The De Witt supermetric in 5D restricted to
the S¹ breathing mode is:

    G_{δR,δR} ∝ Vol(M⁴) / R^{5-4} = Vol(M⁴) / R

(from the general (n+1)D De Witt supermetric with n = 4). The
Mazur-Mottola nonlocal field redefinition for δR would be:

    χ_R = √(−∇²_{M⁴}) δR    (the nonlocal version of δR)

Does the Euclidean action for χ_R have the correct (positive) sign?

Step 4. **The Yang-Mills analog.** The Yang-Mills proof used the compact
gauge group to ensure the FP determinant is positive. In 5D gravity, the
relevant "gauge group" for the dilaton is the S¹ reparametrization
group. This group IS compact (it is the diffeomorphism group of S¹,
which is Diff(S¹), and its connected component Diff₀(S¹) is the loop
group). The compactness of S¹ means the FP determinant for the
harmonic gauge on S¹ is a product of discrete positive eigenvalues —
already proved (Proposition A.1 in Paper 3 §A.8). The nonlinear
extension should inherit this positivity from the compactness of S¹.

Write the argument: the gauge group for the nonlinear dilaton is
Diff(S¹) (the group of ψ-reparametrizations at each 4D point). Unlike
the 4D conformal group (non-compact), Diff(S¹) has a natural compact
subgroup structure. The De Witt-Faddeev-Popov procedure for Diff(S¹)
gives a FP determinant that is positive by the Lichnerowicz-type bound
on S¹ (Ric(S¹) = 0, so −∇²_{S¹} ≥ 0, and the restricted determinant
excludes the zero mode).

Step 5. **Web search:** Search for:
- "Mazur Mottola conformal factor 5D Kaluza-Klein" (direct extension)
- "functional measure gravity compact extra dimension" (relevant work)
- "Diff(S1) Faddeev-Popov determinant gravity" (the gauge group)
- "string theory partition function compact dimension conformal mode"
  (string theory handles this; what is their mechanism?)
- "gravitational path integral product manifold positivity" (anyone proved RP for gravity?)

Step 6. **Write up the argument.** If the Mazur-Mottola extension to 5D
works for δR, Theorem A.3 becomes unconditional. If it doesn't work
directly, identify the minimal additional input needed.

**Deliverable:** `etc/frontier-research/problem-1-OS3-nonlinear.md`

Proof chain format (from PROOF-CHAIN.md):

    Step | Statement | Status | Source

Goal: make Step 9 of the current chain (5D measure positivity) change
from "Assumption" to "Proved" or "Conditional on X" with X explicitly
smaller than the current assumption.

**Pattern to use:** P6 (Projection Produces Pathology) is the primary
pattern — the conformal problem IS the 4D projection. P4 (Topological
Rigidity) for the compactness of Diff(S¹). P5 (Zeta Regularization)
for the FP determinant.

---

## Problem 2: The Spin^c Index on CP² × S¹/Z₂ with Twisted Coefficients

### What the 5/2 really is

Round 2 established the mathematical identity:

    χ(CP²) + η(D_{S¹/Z₂}) = 3 + (−1/2) = 5/2

where η(D_{S¹/Z₂}) = ζ_R(0) = −1/2 is exact. The APS theorem
(manifold with boundary) gives:

    ind(D_M) = ∫_M Â(M) − (h + η)/2

For M = CP² × [0, πR] (the product of CP² with the HW interval):

- Bulk term: ∫ Â(CP²) × Â([0,πR]) = (−1/8) × 1 = −1/8
  (CP² is not spin; with spin^c structure, use Todd class instead)
- Boundary term at φ = 0: contributions from the Z₂ fixed point
- Boundary term at φ = πR: the other orbifold boundary

**The question:** Is there a choice of twisting bundle E on
CP² × S¹/Z₂ such that:

    ind(D^{spin^c}_{CP² × S¹/Z₂, E}) = 5/2

or a related physical quantity equals 5/2?

### What to compute

Step 1. **The spin^c Dirac operator on CP².**

CP² has a unique spin^c structure (since it is simply connected with
H²(CP², ℤ) = ℤ). The canonical spin^c line bundle is L = O(3) (the
anticanonical bundle). The spin^c Dirac operator D^{spin^c}_L has:

    ind(D^{spin^c}_L) = χ(CP²) = 3    (Todd class computation)

This recovers the generation count — already known. No 5/2 here.

Step 2. **Twist by a Wilson line bundle.**

The Wilson line on S¹ with holonomy θ corresponds to a flat line bundle
L_θ on S¹. On the product CP² × S¹/Z₂, the twist E = L_θ contributes:

    ch(L_θ) = 1 + θ/2π + (θ/2π)²/2 + ...

for a U(1) bundle with connection A = θ/(2πR). The twisted index:

    ind(D^{spin^c}_{CP² × S¹/Z₂, E}) = ∫ Td(CP²) × ch(L_θ) × (S¹/Z₂ contribution)

For θ = 0 (no EWSB): ind = 3 × 1 × (interval contribution).
For θ = π (maximal EWSB, the Higgs VEV in the framework):

The key: at θ = π, the Wilson line line bundle on S¹/Z₂ has holonomy
−1, which in the APS framework contributes to the η invariant of the
boundary. The boundary η invariant shifts to:

    η(D_{S¹/Z₂, θ=π}) = η₀ + (shift from Wilson line)

Compute this shift. The relevant formula (Atiyah-Patodi-Singer): the
spectral flow as θ goes from 0 to π.

Step 3. **The spectral flow.**

The Dirac operator on S¹/Z₂ with a U(1) Wilson line A_ψ = θ/(2πR)
has eigenvalues:

    λ_n = (n + θ/(2π))/R    (for Neumann BC)

As θ increases from 0 to π, the n = 0 eigenvalue moves from 0 to
1/(2R). No eigenvalue crosses zero (since θ/2π < 1). Therefore
the spectral flow is 0.

However, for the **Z₂-twisted** boundary conditions (where the Z₂
orbifold projects the spectrum), the eigenvalue structure changes.
On S¹/Z₂ with Z₂-odd boundary conditions:

    λ_n = (n + 1/2)/R    (half-integer modes only)

With the Wilson line, these shift to:

    λ_n = (n + 1/2 + θ/(2π))/R

At θ = π: λ_n = (n + 1)/R. The spectral asymmetry:

    η(θ=π) = Σ_n sign(λ_n)|λ_n|^{-s}|_{s=0}

All eigenvalues are positive (n + 1 > 0 for n ≥ 0), so:

    η(D_{S¹/Z₂, θ=π}) = ζ_{S¹/Z₂}(0) for positive spectrum = −1/2

The η invariant is unchanged! The spectral flow is zero for this
particular trajectory.

Step 4. **The index on CP² × S¹/Z₂ with EWSB Wilson line.**

With η unchanged and the bulk term:

    ind = Td(CP²)[CP²] × (S¹/Z₂ contribution) − (h + η)/2

For the Higgs Wilson line (θ = π) and standard embedding:

    ind = 3 × (S¹/Z₂ contribution) − (0 + (−1/2))/2
        = 3 × (interval term) + 1/4

The interval term for S¹/Z₂ with product metric: the index of D on
the interval [0, πR] contributes a factor related to the boundary
conditions at both ends.

**The computation you need:** What is the APS index on CP² × [0, πR]
with:
- Spin^c structure on CP² (canonical, L = O(3))
- Wilson line boundary condition at φ = 0 and φ = πR
- The HW orbifold identification (fields even/odd under Z₂)

Does this index equal 5/2 for any natural choice of boundary data?

Step 5. **Web search:**
- "APS index theorem orbifold boundary eta invariant" (extensions of APS to orbifolds)
- "spin^c Dirac operator CP2 S1 product index" (direct computation)
- "Atiyah-Patodi-Singer eta invariant Wilson line compact dimension"
- "index theorem half-integer Horava-Witten orbifold" (relevant M-theory context)
- "spectral flow Wilson line CP2 gauge Higgs unification" (any prior computation in this context)

Step 6. **If the index equals 5/2 for some natural choice:**
- State the exact boundary conditions that produce it
- Identify the physical meaning: what observable in the framework
  corresponds to this index?
- Can m_ν/m_KK = ind(D)? Write the chain: index = 5/2 → R = 5/(4m_ν) → ρ_Λ predicted

Step 7. **If no natural choice gives 5/2:**
- Enumerate what values the index takes for all natural boundary data
- State precisely why 5/2 cannot arise from an index on this manifold
- Close the thread definitively: the 5/2 coincidence has no topological
  explanation, only a spectral one (χ + η = 5/2 is a mathematical fact
  without physical mechanism)

**Deliverable:** `etc/frontier-research/problem-2-spinc-index-5half.md`

**Pattern to use:** P4 (Topological Rigidity) — index theorems produce
discrete values; if 5/2 appears, it's topologically locked. P5 (Zeta
Regularization) — spectral flow and η invariants use ζ functions. P6 —
if 5/2 doesn't appear, it's because the 4D shadow misses the S¹ structure.

---

## Problem 3: The E₈ Bundle and Tadpole Integrality

### The specific computation

The HW tadpole anomaly cancellation condition (Horava-Witten 1996, Eq. 3.13):

    N_flux + N_{M2} = (1/2) ∫_{CP² × S²} [tr(F₁²)/λ + tr(F₂²)/λ − tr(R²)/4π²]

where F₁, F₂ are the E₈ gauge field strengths on the two boundaries
and the normalization λ absorbs factors of 2π. The gravitational
source is NOT χ/24 but the characteristic class combination from DMW.

We know:
- N_flux = −1007/8 for Solution II (n₁ = 19/2, n₂ = −18)
- N_{M2} must be a non-negative integer
- The gravitational term I₈ = 0 for natural 8-manifold candidates
- The 1/8 residue must come from the gauge bundle terms

For N_{M2} to be an integer, the gauge bundle contribution must satisfy:

    (1/2) ∫_{CP² × S²} [tr(F₁²) + tr(F₂²)] = integer + 1/8

The visible E₈ bundle is constrained by the anomaly cancellation on the
visible wall. For the Standard Model embedding:

    E₈ → E₆ × SU(3) → [SU(3) × SU(2) × U(1)] × E₆

The Standard Model gauge group is embedded in E₈ via E₆ × SU(3), where
SU(3) is the color group. The visible bundle V₁ on CP² × S² has structure
group SU(3) × SU(2) × U(1) ⊂ E₈.

### Step 1: Identify the embedding index

The second Chern class c₂(V₁) for a bundle in representation R of E₈
satisfies:

    tr_{E₈}(F²) = λ(R) × tr_{fund}(F²)

where λ(R) is the Dynkin index of the representation. For the standard
embedding SU(3) ↪ E₈ via the decomposition E₈ → SU(3) × E₆:

    adjoint(E₈) = (8,1) + (1,78) + (3,27) + (3̄,27̄)

The SU(3) factor contributes:
- c₂(SU(3) on CP²) = instanton number k on CP²
- The standard embedding: k = p₁(CP²)/2 = 3/2

This is half-integer — consistent with CP² being non-spin (the
bundle can have half-integer instanton number).

### Step 2: Compute the gauge bundle term

For the standard embedding on the visible wall:

    (1/2) ∫_{CP² × S²} tr(F₁²) = (1/2) × λ(embedding) × c₂(SU(3) on CP²) × χ(S²)
                                  = (1/2) × 1 × (3/2) × 2
                                  = (1/2) × 3 = 3/2

And for the hidden wall (zero instanton number on CP², from anomaly
cancellation in Appendix C of Paper 7):

    (1/2) ∫_{CP² × S²} tr(F₂²) = 0

Total gauge contribution: 3/2.

With N_flux = −1007/8 and gauge contribution 3/2 = 12/8:

    N_{M2} = 3/2 + 1007/8 − I₈
           = 12/8 + 1007/8 − 0
           = 1019/8

Still not an integer! Try: maybe the normalization is different.

### Step 3: Check the normalization conventions

The standard HW normalization (from Horava-Witten 1996) uses:

    (1/8π²) ∫ tr(F²) vs (1/16π²) ∫ tr(F²)

depending on whether F is normalized as a Lie-algebra-valued form with
generators in the fundamental or adjoint. The tadpole formula changes
by factors of 2 depending on the convention.

Search arXiv for: "Horava-Witten tadpole normalization E8 CP2 second
Chern class" and find the explicit formula with all factors specified.

### Step 4: The Freed-Witten corrected formula

The full DMW-corrected tadpole on a non-spin manifold is (from
Hopkins-Singer 2005, arXiv:math/0211216):

    q(G₄) + N_{M2} = I₈ + (gauge bundle terms with FW shift)

where q(G₄) is the quadratic refinement:

    q(G₄) = (1/2)G₄² + (1/2)G₄ · (λ/2)

with λ/2 = p₁/4 on CP². Compute:

    (1/2) G₄ · (p₁(CP²)/4) = (1/2)(19/2)(3/4) × 2  [× χ(S²) = 2]
                            = (1/2)(19/2)(3/4)(2)
                            = 57/16

Then:

    N_{M2} = I₈ + gauge − N_flux − (1/2)G₄ · (λ/2)
           = 0 + (gauge) + 1007/8 − 57/16

For N_{M2} integer: gauge contribution must have residue such that
gauge + 1007/8 − 57/16 ∈ ℤ₊.

Compute: 1007/8 − 57/16 = 2014/16 − 57/16 = 1957/16. Need gauge
contribution to have fractional part 16 − (1957 mod 16)/16 = ?

1957 = 122 × 16 + 5, so 1957 mod 16 = 5.
Need gauge contribution to have fractional part 11/16.

What gauge bundle gives c₂ with fractional part 11/16?

With Dynkin index λ = 1 and instanton number k = 3/2 on CP² and
something on S², the gauge contribution is:

    (1/2)(k × χ(S²)) = (1/2)(3/2 × 2) = 3/2 = 24/16

24/16 mod 1 = 8/16 = 1/2. Not 11/16.

Try with the SU(5) embedding (a GUT embedding):
E₈ → SU(5) × SU(5): the visible SU(5) with instanton number k on CP²
and the hidden SU(5) with instanton number k' on CP²:

    anomaly cancellation: k + k' = p₁(CP²)/2 = 3/2

With k = 3/2 (standard): k' = 0. With k = 1: k' = 1/2.

For k = 1, the gauge contribution changes. Map out what values of k
and Dynkin index λ give the needed fractional part 11/16.

### Step 5: Web search

Search for:
- "Horava-Witten tadpole E8 bundle CP2 non-spin half-integer instanton"
- "M-theory anomaly cancellation CP2 S2 E8 gauge bundle standard model"
- "Freed-Witten tadpole non-spin boundary E8 bundle 2003"
- arXiv:hep-th/9603142 (the original HW paper) — what is the exact
  tadpole formula in their notation?
- "standard embedding E8 CP2 Pontryagin class tadpole M-theory"

The goal is to find the exact normalization convention used in HW and
DMW for the gauge bundle term, then evaluate whether it can give the
needed 11/16 fractional part.

### Step 6: State the result

Either:
(a) **The tadpole closes.** A specific E₈ embedding gives integer N_{M2}.
    State the embedding, the instanton numbers, and the final N_{M2} value.
    This closes the last open item in Paper 7.

(b) **The tadpole does not close with standard embeddings.** The
    residue arithmetic fails for all standard SM-in-E₈ embeddings.
    State precisely what embedding would be needed (what Dynkin index,
    what instanton number). This is the remaining open item.

(c) **The normalization is ambiguous.** Different conventions in the
    literature give different results. Map the conventions, identify
    which one is physically correct, and state which case applies.

**Deliverable:** `etc/frontier-research/problem-3-e8-tadpole.md`

**Pattern to use:** P4 (Topological Rigidity) — characteristic classes
are exact integers or half-integers; the arithmetic is rigid. P5 (Zeta
Regularization) — the characteristic class computation uses Chern-Weil
theory, which is the index theorem version of zeta regularization.

---

## Output Files

Write three files in `etc/frontier-research/`:

1. `problem-1-OS3-nonlinear.md` — the Mazur-Mottola extension
2. `problem-2-spinc-index-5half.md` — the spin^c index computation
3. `problem-3-e8-tadpole.md` — the E₈ bundle tadpole

Each file must contain:
- **Key new insight (one sentence)** — the short argument that does it
- **Methodology** — which patterns (P1–P6) were used and how
- **Proof chain** — each step with status (Proved / Literature / New / Open)
- **What would make it airtight** — the minimal missing input
- **Honest assessment** — confidence table per claim
- **Pattern attribution** — explicitly state which Yang-Mills move was applied

---

## Priority Order

1. **Problem 1 (OS3)** — the Mazur-Mottola extension is the most likely
   to yield an unconditional theorem. The argument structure is clearest.
   45 min. If it works: Theorem A.3 in Paper 3 becomes unconditional,
   which is the strongest result possible for the non-perturbative
   completion of quantum gravity in this framework.

2. **Problem 3 (E₈ tadpole)** — pure arithmetic once the normalization
   convention is pinned down. Web search first; compute second.
   45 min. Closes Paper 7's last open item.

3. **Problem 2 (spin^c index)** — either closes the 5/2 thread
   definitively or opens a new route to predicting ρ_Λ. High value
   in either direction. 60 min.

---

## Critical Context: What's at Stake

If Problem 1 succeeds: the 5D framework has exact OS3 unconditionally
for the linearized + IR theory and unconditionally for the full
nonlinear theory. The non-perturbative completion of quantum gravity
in this framework would be complete. This would be the first rigorous
constructive definition of a quantum gravity theory without assuming
M-theory.

If Problem 2 finds 5/2 from the spin^c index: ρ_Λ becomes a
prediction. The cosmological constant would be the first quantity in
the history of physics derived from a topological index theorem. This
would resolve the hardest problem in theoretical physics.

If Problem 3 closes: Paper 7 has no remaining open items. The seven
papers are complete and ready for arXiv submission.

---

## Files to Read per Sub-Agent

**Sub-agent 1 (Problem 1 — OS3):**
- `paper3/15-appendix-a-non-perturbative-completion.md` (§A.7–A.8)
- `etc/frontier-research/problem-B-exact-OS3.md`
- `etc/frontier-research/oi3-reflection-positivity.md`
- `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`
- `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`

**Sub-agent 2 (Problem 2 — spin^c index):**
- `etc/frontier-research/problem-A-overlap-5half.md`
- `paper4/appendix-E-spectral-gap.md`
- `paper7/appendix-A-theorem-U-star.md` (§A.5)
- `paper4/06-the-higgs-mechanism-electroweak-symmetry-breaking-.md`

**Sub-agent 3 (Problem 3 — E₈ tadpole):**
- `paper7/appendix-B-freed-witten.md`
- `etc/frontier-research/oi2-freed-witten-tadpole.md`
- `etc/frontier-research/problem-C-dmw-tadpole.md`
- `paper7/04-tadpole.md`

---

*The Yang-Mills proof's central insight was a classification argument:*
*"all dim-6 operators have dev ≥ 2." Short. Structural. Using existing*
*tools. Each of the three problems above has a candidate for that kind*
*of argument:*
*Problem 1: the compactness of Diff(S¹) gives positivity of the FP determinant*
*Problem 2: the APS boundary term gives 1/4, not ±1/2 — definite obstruction*
*Problem 3: the Dynkin index of SM ↪ E₈ is fixed; the arithmetic either closes or doesn't*
*Find the argument. Write it down. Be honest about what you find.*
