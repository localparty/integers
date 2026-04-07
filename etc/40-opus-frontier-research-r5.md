# Research Prompt 40 — Frontier Round 5: Two Concrete Computations

> **For:** Claude Opus — maximum reasoning, fully agentic
> **Date:** April 6, 2026
> **Repository:** `/Users/gsix/quantum-geometry-in-5d-latex/`
> **Session model:** Two sub-agents, one per computation. Each reads
>   its file list, searches the web, computes, and writes one output.
>   These are not exploratory problems — the structure is known and
>   the missing piece is identified. The goal is to execute the
>   computation, not to discover new directions.

---

## Mandatory reading before any computation

1. `etc/pattern-attribution-map.md` — especially the Round 3 and
   Round 4 additions. Know which patterns have been used and which
   results are already proved before computing.

2. `etc/frontier-research/problem-2-equivariant-c2.md` (Computation 1)
   — read in full. Section 4 ("Resolution: The Geometry-Dependent
   Correction") sets up the computation exactly. Section 9 ("What
   Would Make It Airtight") lists what is needed. Do not redo the
   work already done there.

3. `etc/frontier-research/problem-3-leptogenesis.md` (Computation 2)
   — read in full. Section 3 ("Critical Examination") identifies the
   gaps precisely. Section 7 ("What Would Make It Airtight") lists
   the four items needed. Items 1 and 2 (the near-degeneracy and M₃
   hierarchy) are for this round.

---

## What has been established — do not redo

**OS3 (Paper 3 Appendix A §A.9):**
Full proof chain complete in the semiclassical regime. Proposition P
(FP operator positive for Λ < 1/R₀) was proved in Round 4 using the
KK decomposition: n ≥ 1 modes protected by the S¹ spectral gap
(margin of 10⁶⁰), n = 0 mode handled by the Mazur-Mottola De Witt
measure mechanism (proved Rounds 2–3). Theorem A.3* is unconditional
for Λ < 1/R₀; Theorem A.3 (full theory) is covered by M-theory above
the KK scale. The OS3 chain is complete. **No further work on OS3.**

**Tadpole / GUT unification (Paper 7 Appendix B §B.9):**
- Anomaly cancellation forces c₂(V₁) + c₂(V₂) = p₁(CP²)/2 = 3/2
  on CP². Two smooth-bundle integers cannot sum to 3/2.
- Therefore: on the Z₂ orbifold S¹/Z₂, at least one E₈ factor must
  have half-integer equivariant c₂^{eff} on CP².
- The minimal solution c₂^{eff}(V_vis) = 1/2 gives: exact ratio
  n₂/n₁ = −17/9, flux pair (n₁^{int}, n₂) = (17, −34), n₁^{phys} = 18,
  N_flux = −450, N_{M2} = 450 (integer, positive). Everything closes.
- The Conrad formula (derived for T⁴/Z₂) gives {k} ∈ {1/4, 3/4}
  for Z₂ twists in E₈ — never 1/2. But this formula applies to a
  different manifold; the CP² geometry requires a separate computation.
- What is missing: the equivariant eta-invariant of the E₆ × SU(3)
  involution τ₃ on CP² tells us whether the orbifold correction lands
  at 1/2 or some other half-integer.

**Leptogenesis (etc/frontier-research/problem-3-leptogenesis.md):**
- The leptogenesis scale is M_R = 1/r₃ ~ 10¹⁵ GeV (CP² seesaw), NOT
  1/R ~ 20 meV (e-circle). The Davidson-Ibarra bound at the correct
  scale allows |ε| ≤ 0.1, which is easily satisfied.
- The Round 1 result (ε = 4.7 × 10⁻⁵, K = 47, η_B ~ 10⁻¹⁰) is
  physically sound at the correct scale.
- Two unresolved gaps: (a) the mass splitting Δ/Γ ~ 1 is assumed, not
  derived; (b) why M₃ is hierarchically different from M₁ ~ M₂ is
  not explained despite the Z₃ orbifold treating all three equally at
  leading order. The "factor of 3" accuracy is an overstatement; the
  honest range is "within an order of magnitude" after spectator processes.

---

## Computation 1: The Equivariant Eta-Invariant of τ₃ on CP²

### What this computation is

On the Horava-Witten orbifold M^{10} × S¹/Z₂, the E₈ gauge bundle
on the visible wall must have c₂^{equivariant}(V_vis)|_{CP²} = 1/2
to close the tadpole with exact GUT unification. Round 4 established
that the anomaly cancellation FORCES the equivariant c₂ to be
half-integer. The question is: which half-integer?

The equivariant c₂^{eff} on CP² from the Z₂ orbifold is (from
§4.2 of problem-2-equivariant-c2.md):

    c₂^{eff}(V)|_{CP²} = c₂^{bulk}(V)|_{CP²} + delta_{orbifold}(τ)|_{CP²}

With c₂^{bulk} = 0 (no smooth instantons), the orbifold correction is:

    delta_{orbifold}|_{CP²} = 2 × (1/2) × eta(τ, CP²)

where the factor 2 is from two fixed points of S¹/Z₂, the 1/2 is
the orbifold weight 1/|Z₂|, and eta(τ, CP²) is the APS-type
eta-invariant of the E₈ involution τ acting on the boundary CP².

For the E₆ × SU(3)-preserving involution τ₃:

    c₂^{eff} = eta(τ₃, CP²)

We need this to equal 1/2 for the tadpole to close.

### The computation

**Step 1: Set up the equivariant index theorem.**

On a manifold M with Z₂ group action g with fixed-point set F, the
equivariant index theorem (Atiyah-Segal-Singer) gives:

    ind_g(D) = ind(D|_M) + sum_f contribution(f, g)

where each fixed-point component contributes a term involving the
action of g on the normal bundle and on the bundle of spinors.

For our case: M = CP² (the boundary at each orbifold fixed point),
g = τ₃ acting ONLY on the E₈ fiber (not on CP² itself — the Z₂
acts only on the S¹ direction), F = all of CP² (the fixed set is
the entire boundary).

Because τ₃ acts trivially on CP² and non-trivially only on the
fiber, the equivariant index formula simplifies to the twisted index:

    ind_{τ₃}(D_{CP², E}) = ind(D_{CP², E_+}) - ind(D_{CP², E_-})

where E_+ is the +1 eigenspace of τ₃ on the E₈ fiber (dim = 86
for τ₃) and E_- is the −1 eigenspace (dim = 162).

**Step 2: Compute ind(D_{CP², E_+}) and ind(D_{CP², E_-}).**

Using the Hirzebruch-Riemann-Roch theorem on CP² with the canonical
spin^c structure (determinant bundle L = O(3)):

    ind(D^{spin^c}_{O(3)} ⊗ E) = ∫_{CP²} Td(CP²) · ch(E)

For a flat bundle (the fiber representation at the fixed point),
ch(E) = dim(E). So:

    ind(D^{spin^c}_{O(3)} ⊗ E_+) = ∫_{CP²} Td(CP²) · dim(E_+)
                                   = dim(E_+) · ∫_{CP²} Td(CP²)

But ∫_{CP²} Td(CP²) = 1 (the holomorphic Euler characteristic of
CP² is χ_h = 1). Therefore:

    ind(D^{spin^c} ⊗ E_+) = dim(E_+) = 86
    ind(D^{spin^c} ⊗ E_-) = dim(E_-) = 162

Wait — this can't be right for a flat bundle. A flat bundle E on
CP² has first Chern class c₁(E) = 0 (flatness) and higher Chern
classes may also vanish. Let me be more careful.

For a FLAT bundle E (connection with zero curvature), ch(E) = dim(E)
(the Chern character of a flat bundle is just its rank, because all
Chern classes above c₀ = rank vanish for flat bundles). So the HRR
gives:

    ind(D ⊗ E_flat) = ∫_{CP²} Td(CP²) · ch(E_flat) = dim(E) · ∫_{CP²} Td(CP²)

Now ∫_{CP²} Td(CP²) = ∫_{CP²} (1 + (3/2)H + H²) = 0 + 0 + 1 = 1.
(The first two terms integrate to zero since H is a non-top-degree
form on CP²; only H² integrates to 1.)

So: ind = dim(E) × 1 = dim(E).

For twisted index: ind_{τ₃}(D) = 86 - 162 = -76.

But this is just the trace of τ₃ on the adjoint of E₈, which from
§1.2 of problem-2-equivariant-c2.md is 86 - 162 = -76. Confirmed.

**Step 3: Relate to the instanton number correction.**

The equivariant second Chern class from the fixed-point correction is:

    c₂^{fix}(τ₃, CP²) = (1/(8π²)) × (1/2) × ∫_{CP²} ch₂(twisted bundle)

For the twist by τ₃, the relevant ch₂ involves the curvature of
the bundle restricted to the eigenspaces. For a flat bundle:

    ch₂(E_flat) = 0

This gives c₂^{fix} = 0 again — the flat bundle contribution
vanishes. This is the same obstacle found in problem-2-equivariant-c2.md
§3.3.

The resolution (from §3.4): the fractional instanton number comes
not from the local curvature of a flat bundle but from **global
topology** — specifically from the level-matching condition and the
McKay correspondence.

**Step 4: The McKay correspondence approach.**

The McKay correspondence for the Z₂ orbifold relates the instanton
number on the orbifold to the representation theory of Z₂ in E₈.
For the orbifold C²/Z₂ (local model near each HW fixed point), the
Kronheimer-Nakajima construction gives ADHM data for instantons
with fractional instanton number.

The key formula (from Intriligator 1997, Douglas 1996, and the
McKay graph of E₈):

For a Z₂ orbifold with regular representation R_reg of Z₂ in E₈,
the fractional instanton contribution at each fixed point is:

    δc₂ = (1/2) |R_-|/|G|

where |R_-| is the dimension of the Z₂-odd representation (the −1
eigenspace of τ in E₈) and |G| = 2 (the order of Z₂).

For τ₃ (E₆ × SU(3) involution): |R_-| = dim(E_-) = 162.

    δc₂ = (1/2) × 162/2 = 81/2

This is 81/2, not 1/2. Something is wrong — the formula needs
renormalization by the full E₈ adjoint dimension.

The correct normalization (using the HW-normalized trace where
Tr_{248}(F²) = 30 F^a F^a):

    δc₂^{E₈} = (1/30) × (1/2) × Tr_{248}(τ₃ - id)/2

    Tr_{248}(τ₃ - id)/2 = (Tr_{248}(τ₃) - dim(248))/2
                         = (Tr_{248}(τ₃) - 248)/2

For τ₃ with Tr_{248}(τ₃) = 86 - 162 = -76:

    δc₂^{E₈} = (1/30) × (1/2) × ((-76) - 248)/2
             = (1/30) × (1/2) × (-324/2)
             = (1/30) × (1/2) × (-162)
             = -162/60
             = -27/10

This is not 1/2 either.

**Step 5: Search the literature for the correct formula.**

Web search for:
- "equivariant instanton number E8 Z2 orbifold McKay correspondence
  fractional"
- "Horava-Witten boundary E8 bundle half-integer second Chern class
  CP2 fixed point correction"
- "APS eta invariant E8 involution spin^c manifold equivariant"
- arXiv:hep-th/9603167 (Douglas-Moore) — get the exact formula for
  fractional instanton numbers from D-branes on orbifolds
- arXiv:hep-th/9507158 (Douglas 1995, D-branes and discrete torsion)
- arXiv:hep-th/0009251 (Conrad, heterotic orbifolds) — the exact
  level-matching formula for E₈ × E₈

Specifically look for: on what orbifold geometries does the fractional
instanton number land at exactly 1/2? What is the condition on the
representation theory of the orbifold group?

**Step 6: The level-matching shortcut.**

From §3.4 and §4.4 of problem-2-equivariant-c2.md, the argument
from anomaly cancellation already tells us:

    {c₂^{eff}(V₁)} + {c₂^{eff}(V₂)} = 1/2  (mod 1)   on CP²

This holds for any consistent HW compactification on CP² × S²
× S¹/Z₂ with no 5-branes. The question reduces to: given this
constraint, is the minimal solution c₂^{eff} = 1/2 achievable?

The answer from the literature on T⁴/Z₂ orbifolds is: the possible
fractional values of c₂^{eff} for E₈ bundles on Z₂ orbifolds form
a discrete set determined by the allowed gauge twists. For T⁴/Z₂,
Conrad's formula gives {k} ∈ {1/4, 3/4}.

But the CP² geometry modifies this. The key difference: CP² has
Euler characteristic χ(CP²) = 3, while T² has χ(T²) = 0. The
gravitational contribution to the fractional part shifts by χ/24.

**The correct formula for CP²:**

    {c₂^{eff}(V)|_{CP²}} = {k_{twist}} + χ(CP²)/24 × (some correction)

For χ(CP²) = 3: the gravitational shift is 3/24 = 1/8.

If the pure gauge twist gives {k_{twist}} = 3/8 (from some specific
E₈ involution), then:

    {c₂^{eff}} = {3/8 + 1/8} = {1/2} = 1/2

Search for whether any E₈ involution gives k_{twist} = 3/8, and
whether the gravitational correction from χ(CP²)/24 applies.

**Step 7: Compile and state the result.**

After the computation and literature search, state:

(a) **If c₂^{eff} = 1/2 is confirmed:** State the specific
    E₈ involution τ (or bundle construction) that achieves it.
    Identify the formula (McKay, APS eta-invariant, or level-matching)
    that pins the value. Write the complete proof: tadpole closes
    with N_{M2} = 450, exact GUT unification, and identify the
    pattern used.

(b) **If c₂^{eff} = 1/2 is not achievable:** State which
    half-integer value the orbifold gives for each E₈ involution.
    Identify whether 3/2, 5/2, etc. would also close the tadpole
    (check: for c₂^{eff} = 3/2, shift s = 0 → exact ratio requires
    no FW shift → same as the smooth-bundle case, which was already
    shown to work at leading order). State the residual gap.

(c) **If the computation is ambiguous or the formula depends on
    the specific CP² geometry in a way not resolved by existing
    literature:** State exactly what further input is needed
    (e.g., a specific ADHM calculation on the Eguchi-Hanson space
    for E₈ bundles, or an explicit eta-invariant computation).

**Deliverable:** `etc/frontier-research/computation-1-eta-invariant.md`

**Required structure:**
- Key result (one sentence): does c₂^{eff} = 1/2?
- The formula used and its derivation
- Step-by-step proof chain with status for each step
- Literature citations with arXiv IDs where possible
- Honest confidence table
- Pattern attribution: P2 (holonomy — τ is a holonomy element in E₈),
  P4 (topological rigidity — the McKay correspondence gives discrete
  fractional values), P6 (projection — the integer obstruction was an
  artifact of ignoring the Z₂ action)

---

## Computation 2: The Z₃ Breaking Pattern and Leptogenesis Precision

### What this computation is

The leptogenesis calculation in Round 1 (oi1-boltzmann-equations.md)
gives η_B within an order of magnitude of the observed value, but
relies on two unresolved assumptions:

1. **The mass splitting Δ/Γ ~ 1** is assumed (making the leptogenesis
   marginally resonant), but should be derivable from the Z₃ breaking
   pattern in the CP² compactification.

2. **The M₃ hierarchy** — why is N₃ (the third right-handed neutrino)
   hierarchically heavier than N₁ ~ N₂, when the Z₃ orbifold gives
   all three CP² fixed points equal mass at leading order?

Resolving these would either: (a) sharpen η_B to within a factor of 3
with no free parameters, or (b) reveal a genuine tension between
the framework and observation.

This computation is different in character from Computation 1: it is
a physical argument about the compactification dynamics, not a pure
mathematical calculation. The Z₃ structure of CP² and its breaking
pattern at the HW boundaries are the inputs.

### The CP² fixed-point structure and three generations

Read `paper4/appendix-A-anomaly-cancellation.md` and
`paper4/06-the-higgs-mechanism-electroweak-symmetry-breaking-.md`
for the Yukawa coupling structure.

The three right-handed neutrinos N₁, N₂, N₃ arise from the three
fixed points of the Z₃ action on CP². At each fixed point, the local
geometry is C²/Z₃ (an orbifold singularity). The mass of each Nᵢ
is:

    Mᵢ = cᵢ/r₃

where cᵢ is a dimensionless coefficient from the boundary conditions
at the i-th fixed point and r₃ = 1/M_R is the CP² radius.

At leading order in the Z₃ symmetric limit, c₁ = c₂ = c₃ and all
three masses are equal. The Z₃ breaking comes from:
- The gauge flux n₂ on CP¹ × S² (not Z₃ symmetric)
- The Higgs VEV (Wilson line on S², breaks Z₃ at the electroweak scale)
- Boundary conditions at the HW walls (the Z₂ orbifold structure)

### Step 1: Why M₁ ~ M₂ but M₃ ≠ M₁

The three CP² fixed points are at the three C²/Z₃ singularities of
CP² in homogeneous coordinates. In the coordinate patch, these are:
- p₁ = [1:0:0]
- p₂ = [0:1:0]
- p₃ = [0:0:1]

The G₄ flux n₁ on CP² is uniform — it treats all three fixed points
equally (it is the pullback of the Kähler form, which is Z₃ symmetric).

The G₄ flux n₂ on CP¹ × S² breaks the Z₃: it lives on a specific
CP¹ ⊂ CP², which selects one of the three coordinate lines. The
natural choice is the line through p₁ and p₂ (the CP¹ in the [1:z:0]
family), which would differentiate p₃ from {p₁, p₂}.

**This is the breaking mechanism:** the flux n₂ on CP¹ × S² picks a
preferred CP¹ in CP², breaking Z₃ → Z₂ (the residual symmetry
exchanging p₁ ↔ p₂ while fixing p₃). The mass splitting is:

    M₃ - M₁ = M₃ - M₂ ~ n₂/r₃ × (correction factor)
    M₁ = M₂   (residual Z₂ symmetry)

The correction factor from n₂ depends on the overlap integral between
the G₄ flux on CP¹ × S² and the local geometry at each fixed point.

**Compute this overlap integral.** The mass correction to the
boundary condition cᵢ from the flux n₂ is:

    δcᵢ = n₂ × ∫_{Bᵢ} G₄|_{CP¹ × S²} × (boundary state at pᵢ)

where Bᵢ is the local ball around the i-th fixed point. For p₁ and
p₂ (on the preferred CP¹): δc₁ = δc₂ = n₂/(2r₃²) (equal contributions
from the two endpoints of the preferred CP¹). For p₃ (off the CP¹):
δc₃ ~ 0 (no local flux).

So the mass splitting is:

    M₁ = M₂ ~ c₀/r₃ + n₂/(2r₃³)
    M₃ ~ c₀/r₃

This gives M₁ - M₃ ~ n₂/(2r₃³) × r₃ = n₂/(2r₃²) ~ n₂ M_R².

For n₂ = −17 (the exact flux) or n₂ = −18 (the FW-shifted approximate
flux): M₁ - M₃ ~ 17 M_R² / (2r₃²) = 17 M_R²/r₃² × (1/2).

In units where M_R = 1/r₃: M₁ - M₃ ~ 17/2 M_R.

This means M₃ is lighter than M₁ by about 8 × M_R — they are NOT
hierarchically separated, they are of the same order. So N₃ is NOT
negligible in the leptogenesis calculation.

**Verify:** Is this consistent with the Round 1 claim that N₃ is
hierarchically heavier? Check the Round 1 analysis (oi1) for how M₃
is set.

Read `etc/frontier-research/oi1-boltzmann-equations.md` for the
exact claim about M₃.

### Step 2: The Z₃ Yukawa structure and mass splitting Δ/Γ

The near-degeneracy M₁ ~ M₂ determines the resonance parameter:

    Δ = M₂ - M₁ ~ n₂/(2r₃³) × (some small correction)

The decay width:

    Γ(N₁ → Lh) = y²M₁/(8π) where y = g₂√2

The resonance condition Δ ~ Γ gives:

    n₂/(2r₃³) ~ g₂²M₁/(4π)

For M₁ = 1/r₃ = M_R:

    n₂/(2r₃²) ~ g₂²/(4π) = g₂²/(4π)

This is a relation between the flux quantum n₂ and the gauge coupling.
Check whether this is satisfied by the framework's values:

    n₂ = 17 or 18 (from flux quantization)
    g₂ ~ 0.65 at M_R (gauge coupling at the GUT scale)
    g₂²/(4π) ~ 0.65²/(12.57) ~ 0.034

    n₂/(2r₃²) ~ 18/(2r₃²)

In dimensionless units (setting r₃ M_R = 1): n₂/2 = 9 or 8.5.

This gives Δ/Γ ~ n₂/2 / (g₂²/4π) ~ 9/0.034 ~ 265.

This is NOT ~ 1 — it's ~265, meaning the resonance condition is
far from satisfied by the geometric values. The leptogenesis is
non-resonant at the natural scale.

**What does non-resonant leptogenesis give?**

For non-resonant leptogenesis with K ~ 50 (strong washout):

    ε_CP ~ (3/16π) × (Im(Y†Y)₁₂ × M₁)/(Y†Y)₁₁ × M₁/M₂

    For Δ = M₂ - M₁ >> Γ: ε_CP ~ (3/16π) × y² × (Δ/M₁)

    With Δ/Γ ~ 265: ε_CP ~ (3/16π) × g₂² × 265 × (Γ/M₁)
                         = (3/16π) × g₂² × 265 × g₂²/(8π)
                         = (3 × 265 × g₂⁴)/(128π²)

    With g₂ ~ 0.65: ε_CP ~ (3 × 265 × 0.18)/(1263) ~ 0.11

Wait — this seems too large. Let me check the formula.

Actually for the two-body case (N₁ decaying, N₂ propagating in the
loop), the standard result at large splitting Δ >> Γ is:

    ε₁ = (3/16π) × Im[(Y†Y)²₁₂] / (Y†Y)₁₁ × M₁/M₂ × Γ/Δ

For Γ/Δ ~ 1/265, this gives ε₁ ~ (3/16π) × (Y†Y)₁₂² / (Y†Y)₁₁ × (1/265).

With the Z₃ democratic Yukawa matrix, (Y†Y)₁₂ ~ (Y†Y)₁₁ × xi where
xi is the Z₃ breaking parameter. With xi ~ g₂²/(4π) ~ 0.034:

    ε₁ ~ (3/16π) × 0.034 × (1/265) × (CP phase)

For maximal CP violation (sin δ = 1):

    ε₁ ~ (3/16π) × 0.034/265 ~ (3/16π) × 1.3 × 10⁻⁴
       ~ 7.7 × 10⁻⁶

This is smaller than the Round 1 value (4.7 × 10⁻⁵) by a factor of 6.
Combined with the washout factor κ ~ 10⁻³ (for K ~ 47):

    η_B ~ (28/51) × ε₁ × κ ~ 0.55 × 7.7×10⁻⁶ × 10⁻³ ~ 4 × 10⁻⁹

This is above the observed value (6 × 10⁻¹⁰) by a factor of 7,
in the right ballpark.

**Step 3: Reconcile with Round 1.**

The Round 1 result assumed Δ/Γ ~ 1 (resonant regime), giving
ε₁ = 4.7 × 10⁻⁵. The geometric computation above gives Δ/Γ ~ 265
(non-resonant), giving ε₁ ~ 8 × 10⁻⁶. The η_B results:

- Round 1 (resonant, assumed): η_B ~ 10⁻¹⁰ (factor 2-6 below observed)
- Geometric (non-resonant, derived): η_B ~ 4 × 10⁻⁹ (factor 7 above observed)

The truth is likely between these, depending on the exact value of
Δ/Γ. The geometric value Δ/Γ ~ 265 is an overestimate if there are
additional mass-splitting contributions that reduce Δ.

**Step 4: Additional mass-splitting contributions.**

Search for mechanisms that could reduce the mass splitting Δ = M₂ - M₁
below the naive geometric value n₂ M_R²/r₃²:

(a) **Casimir corrections to the boundary conditions.** The Casimir
    energy on CP² shifts the mass of each Nᵢ by a term proportional
    to the local curvature at pᵢ. Near the fixed points, the curvature
    diverges (orbifold singularity), potentially providing a large
    negative correction to the splitting.

(b) **Z₂ boundary corrections from S¹/Z₂.** The HW boundaries modify
    the mass matrix at order (volume of 11D space)^{-1}. These are
    suppressed by M_Pl/M_R ~ 10³ and could shift Δ.

(c) **Radiative corrections.** At one-loop in the 4D effective theory,
    the mass splitting receives corrections proportional to y²M₁/(16π²).
    For y ~ 0.65: δΔ/Γ ~ 0.15. This makes the splitting even larger, not smaller.

The most natural source of reduction is (a), but computing the
Casimir correction at the fixed points requires knowledge of the
orbifold spectrum on C²/Z₃ × (S¹/Z₂ background), which is
complicated.

**Step 5: Web search.**

Search for:
- "Z3 orbifold CP2 leptogenesis mass splitting right-handed neutrino"
- "resonant leptogenesis near-degenerate right-handed neutrino
  gauge-Higgs unification GUT scale"
- "leptogenesis dark dimension KK neutrino tower 2022 2023 2024"
- "leptogenesis extra dimensions TeV GUT scale seesaw orbifold"
- "Yukawa texture Z3 orbifold baryon asymmetry"

The goal: find whether any existing paper has computed the mass
splitting for right-handed neutrinos from a Z₃ orbifold compactification
at the GUT scale and whether the resonant condition can be satisfied.

**Step 6: Write the conclusion honestly.**

(a) **If the geometric Δ/Γ ~ 265 is correct (non-resonant):**
    - Report ε₁ ~ 8 × 10⁻⁶ (non-resonant value)
    - Report η_B ~ 4 × 10⁻⁹ (factor 7 above observed)
    - State that this is an overproduction problem, not an underproduction
    - Identify what additional suppression could bring η_B to the
      observed value: either the CP phase is smaller than maximal,
      or the washout K is larger than 47, or there is an additional
      dilution mechanism
    - Note that K larger means more washout: for K ~ 500 (if Δ/Γ
      modifies the effective decay rate), κ ~ 10⁻⁴ gives η_B ~ 4 × 10⁻¹⁰

(b) **If the geometric Δ/Γ can be made ~1 by an additional mechanism:**
    - Identify the mechanism
    - Show that it is consistent with the compactification
    - Report the resulting η_B range

(c) **In either case, state clearly:**
    - What "within a factor of 3" should be replaced with
    - What the honest precision of the leptogenesis prediction is
    - What further calculation would tighten it

**Deliverable:** `etc/frontier-research/computation-2-leptogenesis-z3.md`

**Required structure:**
- Key result (one sentence): what is Δ/Γ from the Z₃ geometry?
- The Z₃ breaking pattern and M₃ vs M₁ ~ M₂
- The resulting ε_CP and η_B (with the geometric Δ/Γ)
- Comparison with Round 1 and the honest accuracy of the prediction
- What would tighten the calculation
- Pattern attribution: P4 (Z₃ topology fixes the mass ratios),
  P3 (Casimir as scale-setter — the corrections are Casimir-based),
  P1 (geometric reinterpretation — the CP violation is geometric)

---

## Files to read per sub-agent

**Sub-agent 1 (equivariant eta-invariant):**
- `etc/frontier-research/problem-2-equivariant-c2.md` — in full
- `etc/frontier-research/problem-3-e8-tadpole.md` — §6.6–6.10
- `paper7/appendix-B-freed-witten.md` — §B.9
- `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md` — for proof chain format

**Sub-agent 2 (Z₃ breaking and leptogenesis):**
- `etc/frontier-research/problem-3-leptogenesis.md` — in full
- `etc/frontier-research/oi1-boltzmann-equations.md` — in full
- `paper4/06-the-higgs-mechanism-electroweak-symmetry-breaking-.md`
- `paper4/07-predictions.md`
- `paper4/appendix-A-anomaly-cancellation.md`

---

## Output files

Write two files in `etc/frontier-research/`:

1. `computation-1-eta-invariant.md` — equivariant eta-invariant result
2. `computation-2-leptogenesis-z3.md` — Z₃ breaking and η_B precision

Each must contain:
- **Key result (one sentence)**
- **Proof chain** with step | statement | status | source
- **Pattern attribution** (which of P1–P6, which Yang-Mills moves)
- **Honest confidence table**
- **What would make it airtight**

---

## Priority and time

1. **Computation 1 (eta-invariant)** — 60 min. Web search is essential
   first. The Conrad formula (from hep-th/0009251) is the starting
   point; find how it modifies for CP² geometry. The anomaly
   cancellation constraint is already known — the question is pinning
   the value to exactly 1/2.

2. **Computation 2 (Z₃ leptogenesis)** — 60 min. The geometric mass
   splitting calculation (Step 1–2 above) is the core. The result
   — resonant or non-resonant — determines whether the framework
   predicts η_B accurately or approximately. Either answer is
   physically meaningful and should be stated clearly.

---

## What hangs on these computations

**Computation 1:** If c₂^{eff} = 1/2 is confirmed, Paper 7 Appendix B
is complete, the tadpole closes exactly, GUT unification is exact (not
0.31% approximate), and N_{M2} = 450. The seven papers have zero
remaining open items. If c₂^{eff} ≠ 1/2, the approximate solution
(19/2, −18) with 0.31% deviation stands as the framework's prediction.

**Computation 2:** This determines whether the leptogenesis section of
Paper 4 should claim "within a factor of 3" (Round 1's overstatement),
"within an order of magnitude" (Round 4's assessment), or something
more precise. If Δ/Γ ~ 265 is correct and the leptogenesis overproduces
by a factor of 7, the paper needs to explain the additional suppression
mechanism. If Δ/Γ can be reduced to O(1) by a geometric argument, the
calculation tightens significantly.

---

## The structure of both computations

Both computations have the same logical form: **the framework
determines a quantity that was previously treated as a free parameter,
and the value either matches observation (closing the problem) or
mismatches (creating a constraint that must be explained).**

For the eta-invariant: the orbifold structure determines c₂^{eff};
the question is whether it is exactly 1/2.

For leptogenesis: the CP² flux structure determines Δ/Γ; the question
is whether the resulting η_B matches observation with no free parameters.

In both cases, the honest answer — whatever it is — is the right answer.
A mismatch that is clearly understood and stated is more valuable than
a claimed match based on a free parameter.
