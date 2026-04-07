# Research Prompt 39 — Frontier Round 4: Two Proofs + One New Direction

> **For:** Claude Opus — maximum reasoning, fully agentic
> **Date:** April 6, 2026
> **Repository:** `/Users/gsix/quantum-geometry-in-5d-latex/`
> **Session model:** Sub-agents per problem. Each reads its file list,
>   searches the web, and writes one output .md file. Report honestly.
>   A dead end documented clearly is worth more than a forced result.

---

## Mandatory reading before any computation

1. `etc/pattern-attribution-map.md` — especially the Round 3 section.
   The pattern that worked three rounds in a row is **P4 inverted
   (Topological Ceiling)**: topology constraining what's achievable,
   not what's guaranteed. Look for where it hasn't been applied yet.

2. `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md` — the five moves.
   Round 3 used Moves 1, 2, 4 heavily. **Move 3 (Bogomolny/index
   bounding)** has not been applied to either open problem. Check
   whether it applies before computing.

3. `paper3/15-appendix-a-non-perturbative-completion.md` — especially
   §A.9 (just written). The one remaining conditional is the spectral
   bound on −∇²₅ − Ric₅. Read it precisely before working on Problem 1.

4. `paper7/appendix-B-freed-witten.md` — especially §B.9 (just written).
   The counterfactual (c₂ = 1/2 → N_{M2} = 450) and the two open routes
   (equivariant characteristic class; Hopkins-Singer) are described there.

---

## What has been proved — do not redo

**OS3 (Paper 3 Appendix A):**
- Exact OS3, linearized theory: **Proved** (Theorem A.1)
- Exact OS3, IR regime: **Proved** (Theorem A.2)
- De Witt Jacobian positive in 5D: **Proved** (§A.9.2, Mottola 1995)
- Conformal-dilaton non-propagating: **Proved** (§A.9.3, Mazur-Mottola 5D)
- No topology change: **Proved** (§A.9.4)
- FP det positive for near-product metrics: **Proved** (§A.9.5, Prop A.2)
- Full nonlinear OS3: **Conditional on reduced assumption (A')**

**E₈ tadpole (Paper 7 Appendix B):**
- Dynkin index Tr₂₄₈(F²) = 30: **Proved** (§B.9.2)
- c₂(E₈) ∈ ℤ universally: **Proved** (π₃(E₈) = ℤ, §B.9.3)
- Diophantine obstruction universal: **Proved** (§B.9.3)
- Counterfactual c₂ = 1/2 → exact unif. + N_{M2} = 450: **Computed** (§B.9.4)

**5/2 thread: CLOSED.** No further work needed.

---

## Problem 1: Prove the Spectral Bound (A') — DEC → Ric₅ ≥ 0

### What (A') says

The reduced conditional assumption from §A.9.6:

> The operator −∇²₅ − Ric₅, acting on divergence-free vector fields
> on (M⁴ × S¹, g), has no negative eigenvalues for all smooth metrics g
> with: (i) fixed M⁴ × S¹ topology, (ii) ‖Ric₅‖ bounded,
> (iii) R(x) > 0 everywhere.

If (A') holds, Theorem A.3 becomes unconditional: the full nonlinear 5D
theory has exact OS3. This would be the first unconditional constructive
definition of quantum gravity without assuming M-theory.

### The Bochner-Weitzenböck route

The Bochner-Weitzenböck identity on a Riemannian manifold (M, g):

    −∇² V − Ric(V, ·) = (dd* + d*d)V    [for V a 1-form]

The right side is the Hodge Laplacian, which is non-negative on a compact
manifold. This immediately gives −∇² − Ric ≥ 0 when Ric ≥ 0.

**The question:** Does Ric₅ ≥ 0 hold for all physical (finite-action)
configurations on M⁴ × S¹ with the Casimir energy source?

**Step 1: The Einstein equations with the Casimir source.**

The 5D Einstein equations are:

    Ric_{AB} − (1/2) g_{AB} R₅ = 8πG₅ T_{AB}

For the Casimir energy (a cosmological constant form, but with the
correct sign ρ < 0 since Casimir on S¹ is attractive):

    T_{AB} = −ρ_Cas g_{AB},    ρ_Cas = −ΔN × 3ζ(5)/(64π⁶R⁵) < 0

The Einstein equations give:

    Ric_{AB} = 8πG₅(T_{AB} − (1/3)g_{AB}T)
             = 8πG₅(−ρ_Cas g_{AB} + (1/3)(5ρ_Cas)g_{AB})
             = 8πG₅ ρ_Cas (−1 + 5/3) g_{AB}
             = (16πG₅/3) ρ_Cas g_{AB}

Since ρ_Cas < 0:

    Ric_{AB} = −(16πG₅/3)|ρ_Cas| g_{AB} < 0

Wait — the Casimir energy is NEGATIVE (attractive), so ρ < 0, and
Ric < 0. This is the WRONG sign for the Bochner-Weitzenböck bound.

**Re-examine:** The convention matters. The dark energy density is
positive: ρ_Λ > 0. The Casimir formula gives ρ_Λ = ΔN × 3ζ(5)/(64π⁶R⁴)
where ΔN = N_bos − N_ferm. For the framework, ΔN > 0 (net bosonic
contribution after the Z₂ projection), so ρ_Λ > 0. The pressure:

For Casimir energy on S¹ (1D compact space), the equation of state is
w = −1 (from the exact Epstein zeta mechanism, Paper 1 Appendix S).
So T_{AB} = −ρ g_{AB} with ρ = ρ_Λ > 0. Then:

    Ric_{AB} = −(16πG₅/3) ρ_Λ g_{AB} < 0    (NEGATIVE Ricci)

This is bad for Bochner-Weitzenböck. **On-shell, Ric₅ < 0.**

**Step 2: Does this invalidate (A')?**

Not necessarily. The Bochner-Weitzenböck argument requires Ric ≥ 0 on
a COMPACT manifold. M⁴ is not compact. On non-compact M⁴ × S¹, the
spectral theory of the FP operator is more subtle:

The operator −∇²₅ − Ric₅ on M⁴ × S¹ with Ric₅ < 0 might still be
positive if the S¹ provides sufficient spectral gap. Specifically:

    λ_min(−∇²₅ − Ric₅) ≥ λ_min(−∇²₅) − ‖Ric₅‖

For the S¹ contribution: λ_min(−∂²_ψ) = 1/R₀² (first nonzero mode).
For the M⁴ contribution: the 4D Laplacian has continuous spectrum
from 0. So λ_min(−∇²₅) = 0 (the zero modes on M⁴).

If ‖Ric₅‖ > 0, the operator can have negative eigenvalues. The on-shell
Ric₅ = −(16πG₅/3)ρ_Λ g_{AB} gives ‖Ric₅‖ = (16πG₅/3)ρ_Λ.

In Planck units: ρ_Λ ~ 10⁻¹²² M_Pl⁴, so ‖Ric₅‖ ~ 10⁻¹²² M_Pl².
The smallest FP eigenvalue is 1/R₀² ~ (20 meV)² ~ 10⁻³⁰ eV².
In Planck units: 1/R₀² ~ 10⁻⁶² M_Pl².

Since ‖Ric₅‖ = 10⁻¹²² M_Pl² ≪ 1/R₀² = 10⁻⁶² M_Pl²:

    λ_min(−∇²₅ − Ric₅) ≥ 1/R₀² − ‖Ric₅‖ ≈ 1/R₀² > 0

**The on-shell Ric₅ is so small (~ 10⁻¹²² in Planck units) that it
cannot overcome the spectral gap of the S¹ KK modes (~ 10⁻⁶²).**

**Step 3: Off-shell configurations.**

Off-shell, the metric can have arbitrary Ric₅. The question is whether
any off-shell configuration has both:
(a) ‖Ric₅‖ > 1/R₀² (large enough to flip the FP sign), AND
(b) finite Euclidean action (contributing to the path integral)

The Euclidean action for a metric perturbation with ‖Ric₅‖ ~ κ is:

    S_E ~ M_Pl² R₀² (κ R₀²)² Vol(M⁴)

For ‖Ric₅‖ > 1/R₀²: κR₀² > 1, so S_E > M_Pl² R₀² ~ 10⁴⁰.
These configurations are suppressed by exp(−10⁴⁰).

**Step 4: Write the argument formally.**

Can you convert the semiclassical dominance argument into a rigorous
statement? The goal:

**Proposition P.** For all metrics g on M⁴ × S¹ with:
- Fixed M⁴ × S¹ topology
- ‖Ric₅‖ ≤ Λ² (some UV cutoff Λ < 1/R₀)
- R(x) > R_min > 0 (positive circumference)

the operator −∇²₅ − Ric₅ on divergence-free vector fields has no
negative eigenvalues.

*Proof approach:* The eigenvalues of −∇²₅ − Ric₅ are bounded below by
λ_min(−∇²₅) − ‖Ric₅‖ = 1/R₀² − Λ² > 0 for Λ < 1/R₀. This uses
the min-max principle and the spectral gap of −∇²₅ on S¹. QED.

If this works, (A') holds for all UV-cutoff metrics with Λ < 1/R₀
(which covers the entire semiclassical domain), and Theorem A.3
becomes unconditional in the semiclassical regime.

**Step 5: Web search.**
- "Bochner-Weitzenbock non-compact manifold spectral bound curvature"
- "Faddeev-Popov determinant sign gravity Kaluza-Klein compact"
- "gravity path integral measure positivity curvature bound"
- "dominant energy condition Ricci curvature Kaluza-Klein S1"
- "spectral gap Ricci compact factor product manifold"

**Step 6: Write the full argument.** If Proposition P holds:
- Update Theorem A.3 to be unconditional in the semiclassical regime
- State precisely what "semiclassical regime" means (Λ < 1/R₀)
- Discuss whether the full UV theory (Λ > 1/R₀) is covered by the
  M-theory embedding (which provides the non-perturbative UV completion)

**Deliverable:** `etc/frontier-research/problem-1-OS3-spectral-bound.md`

Proof chain format. Goal: upgrade Step 9d' from "Conditional" to
"Proved in semiclassical regime" or better.

**Patterns:** P4 (spectral gap of S¹ is a topological rigidity result),
P5 (zeta regularization of eigenvalue products), P6 (the curvature
problem is a long-distance / UV issue; the compact S¹ provides the
short-distance bound that makes it tractable).

---

## Problem 2: Equivariant Characteristic Classes on S¹/Z₂

### What needs to be computed

From §B.9.4 (Paper 7 Appendix B): exact GUT unification requires
c₂^{eff}|_{CP²} = 1/2. For a smooth E₈ bundle this is forbidden by
π₃(E₈) = ℤ. But the HW setup has a Z₂ orbifold structure (S¹/Z₂ is
the HW interval), and at the two Z₂ fixed points (the HW walls), the
E₈ bundle lives on a boundary 10-manifold M^{10}. On a boundary, the
instanton number can receive contributions from boundary terms, and
for orbifold bundles the equivariant second Chern class can take
half-integer values.

**The question:** Does the Z₂ orbifold of S¹ allow an equivariant E₈
bundle with c₂^{equivariant}|_{CP²} = 1/2?

### Step 1: What is an equivariant bundle?

A Z₂-equivariant E₈ bundle on S¹ with Z₂ action φ → −φ is an E₈
bundle P on S¹ together with a lift of the Z₂ action to P. At the
fixed points (φ = 0 and φ = π), the Z₂ acts on the fiber by an
element τ ∈ E₈ with τ² = 1 (an involution in E₈).

The equivariant instanton number (equivariant second Chern class) for
such a bundle is:

    c₂^{equivariant} = c₂(P) + (1/|Z₂|) × (boundary corrections)
                      = integer + (contributions from fixed points)

The boundary corrections at each fixed point are related to the
representation of τ ∈ E₈ acting on the fiber. For involutions τ ∈ E₈,
the relevant invariant is the McKay index:

    c_τ = (1/|Z₂|) Tr_{adj}(τ) × η(D_{CP²}) / something

**Step 2: Classify Z₂ involutions in E₈.**

E₈ has a finite number of conjugacy classes of involutions. The main ones:

- τ₁: the "symmetric" involution with fixed-point subgroup E₇ × SU(2)
- τ₂: the involution with fixed-point subgroup SO(16)
- τ₃: the involution with fixed-point subgroup E₆ × SU(3) × U(1)

For each involution τ_i, the decomposition of the adjoint 248 under
the fixed-point subgroup gives the equivariant correction.

For τ₃ (E₆ × SU(3) × U(1) fixed point — most relevant for the SM embedding):

    248 = adjoint of (E₆ × SU(3) × U(1)) + off-diagonal

The correction to c₂ from the fixed-point contribution is:

    δc₂ = (1/2) × (trace of τ₃ on 248) × (some topological factor)

**Step 3: Compute the McKay contribution.**

Search for and use the formula for the orbifold gauge bundle second
Chern class. The relevant result in string theory is (Douglas-Moore 1996,
arXiv:hep-th/9603167; Johnson-Myers 1996, arXiv:hep-th/9610140):

For a Z_N orbifold with gauge group G and involution γ ∈ G:

    c₂^{orb} = c₂^{bulk} + (1/N) Σ_{fixed pts} (fractional instanton contribution)

where the fractional instanton contribution at each fixed point is:

    contribution = (1/N) Tr_R(γ^k) × (curvature form integrals)

For Z₂ (N = 2) and the involution τ₃ with Tr_{248}(τ₃):

Compute Tr_{248}(τ₃) = Tr_{adj(E₆×SU(3)×U(1))}(1) − Tr_{off-diag}(1)

Actually: τ₃ acts as +1 on the fixed-point subgroup and as some
phase on the off-diagonal. For a real involution (order 2), the
trace over the adjoint is:

    Tr_{248}(τ₃) = dim(fixed-point subgroup) − dim(off-diagonal)
                  = dim(E₆) + dim(SU(3)) + 1 − (248 − 80)
                  = 78 + 8 + 1 − 168 = −81

The equivariant c₂ correction at each fixed point:

    δc₂ = (1/2) × (something involving Tr_{248}(τ₃)/30)
         = (1/2) × (−81/30) × (normalization)

This requires more care with the normalization. The key question is
whether the result is ±1/2.

**Step 4: Look for the direct answer in the literature.**

The computation of fractional instantons on ALE spaces (orbifold
resolutions) is well-studied. For C²/Z₂ (the simplest orbifold),
fractional instantons with instanton number 1/2 are known to exist
(Kronheimer-Nakajima 1990). The S¹/Z₂ × CP² geometry might provide
a similar mechanism.

**Web search — critical:**
- "fractional instanton E8 Z2 orbifold half-integer second Chern class"
- "equivariant second Chern class orbifold E8 bundle boundary"
- "Douglas Moore fractional instantons orbifold gauge bundle"
- "Horava-Witten boundary E8 bundle half-integer instanton number"
- arXiv:hep-th/9603167 (Douglas-Moore) — key paper on orbifold bundles
- "McKay correspondence E8 Z2 involution 248 decomposition"
- "string theory fractional D-brane instanton orbifold c2 half integer"

If fractional instantons with c₂ = 1/2 exist in the Z₂ orbifold
context, the exact GUT ratio is achievable and N_{M2} = 450.

**Step 5: If c₂^{eff} = 1/2 is achievable:**

- Identify the specific equivariant E₈ bundle that provides it
- Verify c₂^{equivariant}|_{CP²} = 1/2 from the fixed-point contribution
- Recompute the tadpole with this bundle: N_{M2} = 450 (already verified)
- State the flux configuration: (n₁^{int}, n₂) = (17, −34)
- Conclude: exact GUT unification is achievable in the equivariant setting

**Step 6: If c₂^{eff} = 1/2 is not achievable:**

- State the obstruction precisely: what topological invariant blocks it
- Identify whether the Hopkins-Singer differential cohomology route
  (the other escape route from §B.9.6) is more promising
- Leave the tadpole as the approximate solution (19/2, −18) with 0.31%

**Deliverable:** `etc/frontier-research/problem-2-equivariant-c2.md`

**Patterns:** P4 (Topological Rigidity — equivariant characteristic
classes are topological; the McKay correspondence provides exact values).
P2 (Holonomy Correspondence — the Z₂ involution is a holonomy element
in E₈; its fixed-point algebra determines the correction). P6 (the
half-integer is hidden in the orbifold structure; restoring the Z₂ action
reveals it).

---

## Problem 3: New Direction — The Leptogenesis Boltzmann Equations

### Why this now

The novelty audit (Problem D, Round 2) identified that the leptogenesis
calculation (oi1-boltzmann-equations.md from Round 1) gives the correct
baryon asymmetry **within a factor of 3**. This is the weakest quantitative
result in the framework — all other predictions are exact or within percent.
The factor-of-3 gap comes from approximating the Boltzmann equations at
strong washout; full numerical integration would either close the gap or
reveal a genuine discrepancy.

Read `etc/frontier-research/oi1-boltzmann-equations.md` before starting.

### The specific computation

The framework predicts resonant leptogenesis from the KK tower of sterile
neutrinos on S¹. The baryon asymmetry:

    η_B ~ ε_CP × κ_eff

where ε_CP is the CP asymmetry from the KK-split Majorana neutrinos and
κ_eff is the efficiency factor from the Boltzmann equations.

The Round 1 calculation found ε_CP × κ_eff ~ O(10⁻¹⁰) within a factor
of 3 of the observed η_B = 6.1 × 10⁻¹⁰. The approximation: strong washout
regime with κ_eff ~ ε_CP × 1/K where K is the washout factor. Full
numerical integration of the Boltzmann equations would replace the
approximation.

**Step 1: Write down the Boltzmann equations precisely.**

For the KK spectrum of right-handed neutrinos with masses M_n = n/R (KK
level n) and Yukawa coupling y_ν from the gauge-Higgs seesaw:

The relevant equations are (for the n = 1 dominant mode):

    dN_{N₁}/dz = −(D + S)(N_{N₁} − N_{N₁}^{eq})
    dN_{B-L}/dz = −ε_CP D(N_{N₁} − N_{N₁}^{eq}) − W N_{B-L}

where z = M₁/T, D is the decay rate, S is the scattering rate, and W
is the washout rate. The efficiency factor:

    κ_eff = −(g_* / g_*s) ∫_0^∞ dz (dN_{N₁}/dz) e^{-S(z)}

**Step 2: Identify the framework-specific inputs.**

From the framework (Paper 4, §7.22):
- M₁ = 1/R = m_KK ~ 20 meV (the lightest KK neutrino mass)
- m_ν = 51 meV (from gauge-Higgs seesaw)
- Yukawa coupling: y_ν² v²/(2M₁) = m_ν
  → y_ν = √(2 m_ν M₁)/v = √(2 × 51meV × 20meV)/(174GeV)
         = √(2040 meV²)/(1.74×10⁵ MeV)
         ~ 4.5×10⁻¹³/MeV × MeV = 4.5×10⁻¹³

This is the input to the Boltzmann equations.

**Step 3: Compute the washout parameter K.**

K = Γ(N₁ → Lh)/H(T = M₁) where H is the Hubble rate at T = M₁.

    Γ(N₁) = y_ν² M₁/(8π) ~ (4.5×10⁻¹³)² × 20meV/(8π) ~ 10⁻²⁵ meV

    H(T = M₁) = π√(g_*/90) M₁²/M_Pl ~ 1.66√(10⁶.75) × (20meV)²/M_Pl
              ~ 3.5 × (4×10⁻⁴ eV²)/(10¹⁸ GeV)
              ~ 10⁻²⁸ eV

    K = Γ/H ~ 10⁻²⁵ meV / (10⁻²⁸ eV) = 10⁻²⁵⁺²⁸ × 10³ = 10⁶

K >> 1: very strong washout. This is the regime where the approximation
κ_eff ~ 1/(K × ln K) is known to be accurate to better than 30%.

**Step 4: Compute ε_CP for the KK tower.**

For resonant leptogenesis from the n=1 and n=2 KK modes:

The CP asymmetry from the self-energy diagram (resonant contribution):

    ε_CP = (3/16π) × Im(y_ν†y_ν)²/(y_ν†y_ν) × M₁/(M₂² − M₁²) × M₁

For M₁ = 1/R, M₂ = 2/R (second KK mode):

    ε_CP ~ (3/16π) × y_ν² × M₁³/(3M₁²) × (something from CP phases)

The CP phases in the framework come from the Wilson line VEV (the Higgs
field in gauge-Higgs unification). The relevant phase:

    Im(y_ν†y_ν)² / (y_ν†y_ν) ∝ sin(2θ_CP)

where θ_CP is the CP-violating phase from the Wilson line. In the
framework, θ_CP is related to the Higgs VEV, which is set by the EWSB
condition. The maximal CP violation (sin(2θ_CP) ~ 1) gives the largest
ε_CP.

**Step 5: Full numerical result.**

With K ~ 10⁶ (strong washout):

    κ_eff ~ 2/(z_B K) where z_B ~ ln(K/z_B)

For K = 10⁶: z_B ~ 20, κ_eff ~ 2/(20 × 10⁶) = 10⁻⁷

For ε_CP ~ 10⁻³ (maximal CP violation at resonance):

    η_B ~ (28/51) ε_CP κ_eff ~ 0.55 × 10⁻³ × 10⁻⁷ = 5.5 × 10⁻¹¹

This is within factor 10 of η_B = 6.1 × 10⁻¹⁰. The strong washout is
suppressing the asymmetry by more than expected.

**The issue:** K ~ 10⁶ is too large. Check whether the KK tower
contributions (summing over n = 1, 2, 3, ...) modify the effective
washout. The collective contribution from the KK tower can enhance ε_CP
while the washout from higher KK modes is suppressed at T < M_n.

**Step 6: Refined treatment of the KK tower.**

At temperature T ~ M₁ (relevant for leptogenesis), only the n = 1 KK
mode contributes to washout (n ≥ 2 modes are Boltzmann-suppressed by
exp(−M_n/T) = exp(−n)). The resonant enhancement comes from the
near-degeneracy M₂ − M₁ = M₁ (not resonant — the resonance condition
requires M₂ ≈ M₁). For exact resonance, two KK modes must be nearly
degenerate.

**Can two KK modes be nearly degenerate in the framework?**

The KK spectrum is M_n = n/R (exactly spaced). There is no degeneracy
between KK levels in the unperturbed theory. But if the Casimir
potential shifts the mass slightly (by δM ~ m_eff × (δR/R)):

    M₁ = 1/R + δM₁,   M₂ = 2/R + δM₂

For resonant leptogenesis, need |M₂ − M₁| ≲ Γ_N (the decay width):

    |M₂ − M₁| ~ 1/R = 20 meV
    Γ_N ~ y_ν² M₁/(8π) ~ 10⁻²⁵ meV

The resonance condition is not satisfied: M₂ − M₁ ≫ Γ_N. The leptogenesis
is therefore **non-resonant**, and ε_CP takes the standard (non-resonant)
value ~ 10⁻⁶ or smaller.

**Web search for correct values:**
- "Boltzmann equations resonant leptogenesis strong washout numerical"
- "KK neutrino leptogenesis Kaluza-Klein extra dimension baryon asymmetry"
- "dark dimension leptogenesis meV neutrino mass sterile KK tower"
- "non-resonant leptogenesis CP asymmetry KK tower"

**Deliverable:** `etc/frontier-research/problem-3-leptogenesis.md`

Goal: either:
(a) Identify the mechanism that gives η_B within factor 3 (as Round 1
    found), and understand whether the factor-of-3 gap is a numerical
    approximation or a genuine deficit in the framework
(b) Find the correct CP asymmetry for non-resonant leptogenesis from
    the KK tower and determine whether the observed η_B can be produced
    with maximal CP violation

**Patterns:** P3 (Casimir as scale-setter — the KK masses set the
washout scale). P1 (Geometric Reinterpretation — the CP phases arise
from the Wilson line geometry). P6 (the strong washout is a 4D
projection of a KK tower effect — summing the tower may change the
effective K).

---

## Output files

Write three files in `etc/frontier-research/`:

1. `problem-1-OS3-spectral-bound.md` — the DEC → Ric₅ bound
2. `problem-2-equivariant-c2.md` — equivariant E₈ bundle on S¹/Z₂
3. `problem-3-leptogenesis.md` — Boltzmann equations and η_B

Each file must contain:
- **Key new insight (one sentence)**
- **Proof chain** — each step: Proved / Literature / New / Open
- **Pattern attribution** — which of P1–P6 and which Yang-Mills moves
- **Honest assessment** — confidence table
- **What would make it airtight** — the minimal missing input

---

## Priority and time allocation

1. **Problem 1 (OS3 spectral bound)** — 50 min. The Proposition P
   argument using the S¹ spectral gap bounding the Ric₅ perturbation
   is already nearly written. The on-shell calculation shows Ric₅ is
   10⁻⁶⁰ times smaller than the S¹ gap. The key: can this be stated
   as a rigorous bound in the semiclassical regime?

2. **Problem 2 (equivariant c₂)** — 60 min. Requires web search first.
   The Douglas-Moore paper (hep-th/9603167) and the literature on
   fractional instantons on orbifolds is the key reference. If fractional
   instantons with c₂ = 1/2 exist for the appropriate involution in E₈,
   this closes the tadpole completely.

3. **Problem 3 (leptogenesis)** — 50 min. The Round 1 result (within
   factor 3) is real but needs verification. The strong washout with
   K ~ 10⁶ suppresses the asymmetry more than estimated. Find the correct
   washout factor and determine whether the framework genuinely produces
   η_B ~ 6 × 10⁻¹⁰ or whether it falls short.

---

## Files to read per sub-agent

**Sub-agent 1 (OS3 spectral bound):**
- `paper3/15-appendix-a-non-perturbative-completion.md` (§A.8–A.9)
- `etc/frontier-research/problem-1-OS3-nonlinear.md` (Round 3)
- `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`

**Sub-agent 2 (equivariant c₂):**
- `paper7/appendix-B-freed-witten.md` (§B.9)
- `etc/frontier-research/problem-3-e8-tadpole.md` (Round 3)
- `etc/frontier-research/oi2-freed-witten-tadpole.md` (Round 1)

**Sub-agent 3 (leptogenesis):**
- `etc/frontier-research/oi1-boltzmann-equations.md` (Round 1)
- `paper4/07-predictions.md`
- `paper4/06-the-higgs-mechanism-electroweak-symmetry-breaking-.md`

---

## The underlying logic of this round

Round 3 proved: (1) three of four OS3 components; (2) exact GUT ratio
universally obstructed by E₈ topology; (3) 5/2 thread closed.

Round 4 pursues the two remaining openings:

**Problem 1** converts the quantitative argument (Ric₅ on-shell is
10⁻⁶⁰ × spectral gap) into a rigorous Proposition, making OS3
unconditional in the semiclassical regime. The gap to full
unconditional OS3 would then be only the deep UV regime (E > 1/R₀),
which is covered by the M-theory embedding.

**Problem 2** looks for the topological mechanism (equivariant
characteristic class on the Z₂ orbifold) that would provide the
half-integer instanton number the tadpole needs. If it exists, the
framework closes completely. If it doesn't, the 0.31% deviation is a
definitive, permanent prediction.

**Problem 3** is different in character — it's a quantitative
calculation, not a topological proof. It tests whether the framework
is quantitatively accurate at the level of cosmological observations,
independent of the structural questions in Problems 1 and 2.

*In physics, the most satisfying results are when the algebra says
"impossible" and then the geometry shows "unless." Round 3 found the
impossible; Round 4 looks for the "unless."*
