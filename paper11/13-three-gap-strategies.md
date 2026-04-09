# Attack Strategies for the Three Remaining Proof Gaps

**Date:** April 8, 2026

---

## Overview

Four proof gaps remained after this session. L.1-L.4 is on its way
via the gradient flow programme (17 research memos done, writing phase).
The three remaining gaps each require a different approach:

| Gap | Nature | Tool | Timeline |
|-----|--------|------|----------|
| CP² area law | Geometric proof of confinement | Holonomy + cluster expansion | Months |
| Adiabatic continuity N=3 | 2D sigma model mass gap | Computer-assisted rigorous numerics | 6-10 months |
| OC-2 / CC problem | Non-perturbative R derivation | M2-brane instantons | Research frontier |

---

## Gap 1: CP² Area Law — Proving Confinement from Geometry

### What It Is

Paper 5 proposes: chromoelectric flux on CP² is topologically
constrained by H₂(CP², Z) = Z, producing flux tubes with string tension
σ = (3/8π²) g₃²/r₃². The numerical match (√σ = 410-510 MeV vs
experiment 440 MeV) is excellent, but the formal proof that the CP²
topology FORCES the area law is missing.

Three specific things are unproved:
1. The 11D YM equations with quark sources have flux-tube solutions
2. These are the minimum-energy configurations
3. The energy grows linearly with quark separation

### Why It Matters

This would unify Papers 5, 8, and 11:
- Paper 8 proves the mass gap EXISTS (via KK topology)
- Paper 5 proposes the geometric MECHANISM (CP² holonomy)
- Paper 11 shows colour IS entanglement

Closing this gap would show: the entanglement patterns that define
colour (Paper 11) are confined (Paper 5/8) because the CP² topology
forces flux tubes. The entire strong-force story would be complete.

### The Strategy

**Route A: Variational Argument on CP²**

Use the Bogomolny bound (already in Paper 8) adapted to CP²:

1. **Write the energy functional.** For gauge field A on M⁴ × CP² with
   quark sources at positions x, y separated by distance R:

       E[A] = ∫_{M⁴×CP²} |F_A|² dvol

2. **Decompose by CP² topology.** Any gauge configuration with quark
   sources in the fundamental representation must carry a non-trivial
   CP¹ ⊂ CP² flux (by the non-trivial π₂(CP²) = Z). This flux cannot
   spread over more than one CP¹ cycle without increasing energy.

3. **Lower bound from topology.** The minimum energy of a configuration
   with one unit of CP¹ flux is:

       E_min(flux) = 8π²/g² (from Bogomolny)

   For a flux tube of length R and cross-section area A_⊥:

       E(R) ≥ σ × R    where    σ = E_min(flux) / A_⊥

4. **Upper bound from explicit construction.** Construct an explicit
   flux-tube ansatz (Abelian projection of the CP² gauge field) and
   compute its energy. Show E(R) ≤ σ' × R + const, with σ' matching
   the geometric prediction.

5. **Combine.** The linear lower and upper bounds give σ > 0, proving
   the area law.

**Route B: Transfer from Paper 8's Cluster Expansion**

Paper 8's cluster expansion proves σ > 0 for the KK-enhanced theory
at all physical β. The string tension is a function of β and r₃:

    σ_KK(β, r₃) = σ_geometric(r₃) × [1 + O(e^{-m₁a})]

where σ_geometric = (3/8π²) g₃²/r₃² is Paper 5's prediction.

The strategy:
1. Show the cluster expansion at strong coupling (small β) reproduces
   the leading-order string tension from the CP² Bogomolny bound.
2. Use the lattice-continuum transfer (Section 5 of Paper 8) to show
   σ survives the continuum limit.
3. Identify the physical string tension with the CP² geometric formula.

This would prove: the string tension computed by Paper 8's rigorous
methods EQUALS the string tension predicted by Paper 5's geometric
mechanism.

**Route C: 2D YM on CP¹ ⊂ CP² (the SU(2) warm-up)**

Paper 8 already has an exact SU(2) proof using 2D YM on S². The same
strategy applied to CP¹ ⊂ CP² (which is an S² with specific radius
r₃/√2):

1. The Wilson loop on CP¹ satisfies the exact area law σ = 3g²/8
   (from the Peter-Weyl theorem, Paper 8 Section 4.6).
2. The CP¹ ⊂ CP² embedding constrains the full CP² Wilson loop:
   any CP² Wilson loop contains a CP¹ Wilson loop as a sub-loop.
3. By monotonicity (Wilson loops on larger surfaces have larger
   area law constants), σ_{CP²} ≥ σ_{CP¹} > 0.

This is the most concrete route — it uses Paper 8's existing SU(2)
result as a sub-case.

### Concrete Steps

| Step | What | Effort | Dependencies |
|------|------|--------|-------------|
| 1 | Write the CP² energy functional with quark sources | 1 session | Paper 5 §2-3 |
| 2 | Derive the topological lower bound (Bogomolny on CP¹ ⊂ CP²) | 1 session | Paper 8 §4.6 |
| 3 | Construct the explicit flux-tube ansatz | 1-2 sessions | Paper 5 §3 |
| 4 | Prove the upper bound (linear energy growth) | 1-2 sessions | Step 3 |
| 5 | Connect to Paper 8's cluster expansion (Route B) | 1 session | Paper 8 §4 |
| 6 | Monotonicity argument (Route C) | 1 session | Paper 8 §4.6 |

**Estimated total:** 4-6 sessions. Most tractable of the three gaps.

**Recommended route:** C first (quickest, uses existing SU(2) result),
then A for the full geometric picture.

---

## Gap 2: Adiabatic Continuity at N=3

### What It Is

The continuum limit of the Yang-Mills mass gap (Paper 8, Section 5)
requires showing the 2D CP^{N-1} sigma model on a finite torus has
a mass gap that persists through the weak-to-strong coupling crossover
at N=3. This is the bottleneck for Δ_∞ > 0.

Proved at N = ∞ (Witten 1979) and N = 2 (Ünsal 2012). Open at N = 3.

### Why It Matters

Without adiabatic continuity, the continuum limit argument has a
conditional step: it assumes no phase transition occurs in the
crossover regime mL ~ 1. The lattice mass gap (Theorem 4) and the
IR equivalence (Theorem 5) are unconditional — only the continuum
limit (Section 5) depends on this.

### The Strategy

**Route A: Computer-Assisted Rigorous Numerics (READY)**

This is the most concrete route. The STATUS.md in the Yang-Mills
directory identifies this as "ready, 6-10 months, 60 core-days":

1. **Discretise the CP² sigma model** on a finite lattice
   (L × L torus, L = 8, 12, 16, 24, 32).
2. **Compute the mass gap** m(g², L) at each coupling g² and
   lattice size L using Monte Carlo with cluster algorithm.
3. **Verify no phase transition:** Show m(g², L) > 0 for all g²
   in the crossover regime (g² from 0 to ∞), with controlled
   error bars.
4. **Rigorous error bounds:** Use interval arithmetic to make the
   Monte Carlo results rigorous (Lanford-style computer-assisted
   proof).

**Hardware:** ~60 core-days on modern hardware. Feasible on a
university cluster.

**Route B: Center Vortex Free Energy (PARTIAL)**

The center vortex approach computes the free energy F_v of a Z₃
vortex threading the spatial torus:

1. F_v^(0) > 0 is already PROVED (all Matsubara terms individually
   positive, Paper 8 research notes).
2. F_v^(1) at mL ~ 1 (the crossover) is OPEN.
3. If F_v > 0 for all L, then the mass gap persists (no
   deconfinement transition).

**What's needed:** Compute F_v^(1) in the crossover regime.
This is a 1D integral that can be evaluated numerically with
rigorous error bounds.

**Route C: Monotonicity m(N) ≥ m(∞) (BLOCKED)**

The idea: if m(N) ≥ m(∞) for all N, and m(∞) > 0 (Witten), then
m(3) > 0. But the effective potential has a cubic term that makes
it non-monotone. Existing correlation inequalities are insufficient.

**Status:** Blocked. Not recommended unless new inequalities are found.

### Concrete Steps

| Step | What | Effort | Route |
|------|------|--------|-------|
| 1 | Set up CP² lattice sigma model code | 2-3 sessions | A |
| 2 | Run at L = 8, 12 (fast sanity check) | 1 session + compute | A |
| 3 | Compute F_v^(1) in crossover | 1-2 sessions | B |
| 4 | Full production runs L = 16, 24, 32 | Weeks of compute | A |
| 5 | Rigorous error analysis | 2-3 sessions | A |
| 6 | Write up as computer-assisted proof | 1-2 sessions | A |

**Estimated total:** 6-10 months (dominated by compute time).

**Recommended route:** A (computer-assisted) as the main track,
with B (center vortex) as a fast check. Route C is abandoned.

---

## Gap 3: OC-2 / The Cosmological Constant Problem

### What It Is

Theorem U (Paper 7) proves:

    R_bare = (63 n₁)^{3/2} / (128 π^{11/2} M_Pl) ≈ l_P

The observed R_obs ≈ 10.1 μm is 10³⁰ times larger. No perturbative
M-theory calculation can bridge this gap. The ratio R_obs/R_bare ≈ 10³⁰
is the cosmological constant problem (since ρ_Λ ∝ R⁻⁴, the ratio in
energy density is 10¹²⁰).

### Why It Matters

Solving OC-2 would:
1. Remove the last free parameter from the framework
2. Solve the cosmological constant problem
3. Predict the Higgs mass from first principles (M_KK = 1/r₂ derived)
4. Complete the framework: everything from one geometry, zero parameters

### The Strategy

**Route A: M2-Brane Instantons**

M2-branes can wrap the e-circle S¹. The instanton action is:

    S_M2 = T_M2 × Vol(S¹) = (2π/l₁₁³) × (2πR)

where T_M2 = 2π/l₁₁³ is the M2-brane tension and l₁₁ is the 11D
Planck length.

The instanton generates a non-perturbative contribution to the
effective potential:

    V_np(R) ~ exp(-S_M2) = exp(-4π²R/l₁₁³)

At R = R_bare ~ l_P and l₁₁ ~ l_P:
    S_M2 ~ 4π² ≈ 39.5

This gives exp(S_M2) ~ 10¹⁷ — not quite 10³⁰.

**The refinement:** Multiple M2-brane species wrapping S¹. With
k species (from the M-theory compactification):

    S_total = k × S_M2

For k = 2: S_total ~ 79, exp(79) ~ 10³⁴. Close to 10³⁰.

The precise calculation requires:
1. Count M2-brane species on CP² × S² × S¹/Z₂
2. Compute the one-instanton determinant (prefactor)
3. Sum over multi-instanton sectors
4. Find the minimum of V_pert(R) + V_np(R)

**Route B: Tunnelling from R_bare to R_obs**

The Casimir potential V(R) = c/R⁴ has no minimum (monotonically
decreasing). But the M2-instanton potential V_np(R) grows
exponentially for large R. The combined potential:

    V_total(R) = c/R⁴ + A exp(-B/R)

may have a minimum at R_obs if A and B are the right values.

The tunnelling from R_bare (the perturbative value) to R_obs
(the minimum of V_total) occurs via Coleman-De Luccia bubble
nucleation. The tunnelling rate determines whether the universe
has had time to reach R_obs (it has — the universe is 13.8 Gyr old).

**Route C: The Bousso-Polchinski Mechanism Adapted**

The Bousso-Polchinski (2000) discretuum mechanism uses multiple
flux quanta to scan the cosmological constant. In the e-dimension
framework, the fluxes are the G₄ flux integers n₁ = 9, n₂ = -17.
These are FIXED by gauge coupling unification — no scanning.

However, the M2-brane charge N_M2 (from the tadpole condition,
Paper 7 Section 4) IS a free integer. Different N_M2 give different
R through the M2-instanton mechanism. The correct R_obs selects
a specific N_M2.

This is NOT the landscape (there is no landscape of 10⁵⁰⁰ vacua).
There is one manifold, one set of fluxes, and one integer N_M2
selected by the CC matching.

### Concrete Steps

| Step | What | Effort | Route |
|------|------|--------|-------|
| 1 | Count M2-brane species on CP²×S²×S¹/Z₂ | 1-2 sessions | A |
| 2 | Compute S_M2 for each species | 1 session | A |
| 3 | One-instanton determinant (prefactor) | 2-3 sessions | A |
| 4 | Combined potential V_pert + V_np | 1 session | B |
| 5 | Find minimum: does R_obs emerge? | 1 session | B |
| 6 | Coleman-De Luccia tunnelling rate | 1-2 sessions | B |
| 7 | N_M2 determination from CC matching | 1 session | C |

**Estimated total:** 5-8 sessions for the computation. The
conceptual breakthrough (does it work?) comes at Step 5.

**Recommended route:** A+B combined. Start with the instanton
action (Route A), then construct the combined potential (Route B).
If V_total has a minimum at R ~ 10 μm, the CC problem is solved.

---

## Priority and Dependencies

```
                    L.1-L.4 (ON ITS WAY — writing phase)
                        |
                        v
                 Appendix L rewrite → Clay submission
                 (independent of below)


    CP² Area Law ←──── most tractable (4-6 sessions)
         |              uses Paper 8's SU(2) result
         v              completes the confinement story
    Confinement proved


    Adiabatic N=3 ←──── longest timeline (6-10 months)
         |              compute-dominated
         v              independent track
    Continuum limit unconditional


    OC-2 / CC ←──── highest impact, highest risk
         |          non-perturbative M-theory
         v          the summit
    Zero free parameters
```

### Recommended Order

1. **CP² area law** — most tractable, highest connection to today's work
2. **Adiabatic N=3** — start the computation pipeline (runs in background)
3. **OC-2 / CC** — attempt after the others, when all perturbative gaps are closed

### Independence

All three are independent of each other and of L.1-L.4. They can
proceed in parallel. The CP² area law is the only one likely to yield
results in a single focused session.

---

## What Closing Each Gap Achieves

| Gap closed | Framework status |
|-----------|-----------------|
| CP² area law | Confinement PROVED from geometry. Papers 5, 8, 11 unified. |
| Adiabatic N=3 | Continuum limit UNCONDITIONAL. YM mass gap fully rigorous. |
| OC-2 / CC | ZERO free parameters. CC problem solved. The summit. |
| All three | The framework is COMPLETE. Every result proved. Every parameter derived. |

---

*Three gaps. Three strategies. One geometry left to complete.*
