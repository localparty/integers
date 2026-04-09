# Conjecture-to-Proof Landscape

## Status: Every conditional result in the 10-paper series, ranked by impact and tractability

---

## The Dependency Graph

The 9 conditional/conjectural results and 4 open conjectures (L.1-L.4) are not independent. They form a dependency graph with clear leverage points — proving one often upgrades several downstream results automatically.

```
    Three-Loop Mercedes (2-4 weeks)
               |
               v
    All-Orders BPHZ Factorization (L >= 3)
               |
               v
    UV Finiteness of 5D KK Gravity = UNCONDITIONAL AT ALL LOOP ORDERS


    OC-2: r_2 Casimir on S^2 (1-2 sessions)
               |
               v
    Higgs Mass = GENUINE PREDICTION (not consistency check)
               |
               v
    SM sector has ZERO free parameters beyond R


    Fast-Scrambler from e-Geometry (moderate effort)
               |
               v
    Page Curve = UNCONDITIONAL
               |
               v
    Black Hole Information Preservation = PROVED


    Non-Perturbative Decoupling via Spectral Methods (moderate effort)
               |
               v
    Theorem 5 (KK -> standard YM) = RIGOROUS
               |
               v
    Yang-Mills Mass Gap Proof Chain = FULLY NON-PERTURBATIVE


    L.1 Renormalised Composites (major effort — gradient flow route)
           /           |           \
          v            v            v
        L.2          L.3          L.4
     (AF match)   (Stress T)    (OPE)
          |            |            |
          v            v            v
    Clay Prize Structural Requirements = COMPLETE
```

---

## Full Inventory

### 1. BPHZ Factorization at L >= 3 (Theorem K.3)

**Paper:** 1 (Appendix K), 10
**Current status:** CONDITIONAL — proved at L = 1 (Appendix F), proved at L = 2 (Appendix G), conditional at L >= 3

**The claim:** At arbitrary loop order L, the BPHZ-subtracted amplitude factorises as (4D momentum integral) x E_L(-j; Q_L), where E_L is the Epstein zeta function of the KK mode sum. Since Theorem K.1 proves E_L(-j; Q) = 0 for all j >= 1, finiteness follows — but only if the factorisation holds.

**What's missing:** At L >= 3, overlapping subdivergences could in principle break the factorisation. The Weinberg locality argument supports it, but no explicit calculation exists beyond L = 2.

**What would close it:**
- **Route C (most concrete):** Compute the three-loop Mercedes diagram E_3(-1; Q_3) explicitly, where Q_3 is the FCC lattice quadratic form n_1^2 + n_2^2 + n_3^2 + n_1 n_2 + n_2 n_3 + n_1 n_3. Verify factorisation survives BPHZ subtraction at L = 3. Then extend to L = 4.
- **Route A (Kontsevich-Vishik):** Prove factorisation for general L using pseudodifferential operator theory. Multi-month effort.
- **Route B (BPHZ joint analyticity):** Prove via Epstein zeta's joint holomorphicity in Schwinger parameters. Multi-month effort.

**Attack plan:** Route C first (2-4 weeks for numerical value, 1-2 months for algebraic structure). Routes A/B informed by the L = 3 data.

**Downstream cascade:**
- All-orders UV finiteness of linearised 5D gravity becomes unconditional
- Paper 10's scheme-independence extends beyond two loops
- The quantum gravity result (Paper 1) goes from "proved through L = 2 and conditional beyond" to "proved at all orders"

**Estimated effort:** 2-4 weeks (numerical), 1-2 months (full algebraic proof)
**Location:** Paper 1 Appendix K Section K.2; attack plan at `etc/12-closing-the-open-problems-plan.md` Problem 1

---

### 2. Moduli Stabilisation OC-2: The S^2 Radius r_2

**Paper:** 4, 7
**Current status:** OPEN — r_2 is a free parameter

**The claim:** The Higgs mass m_H ~ 125 GeV is consistent with observation for compactification scale M_KK ~ 1-2.5 TeV. But M_KK depends on r_2, which is not independently fixed.

**What's missing:** A stabilisation mechanism for r_2. Papers 1 and 7 fix r_1 (S^1, via dark energy Casimir match) and r_3 (CP^2, via G_4 flux quantization). r_2 is the orphan.

**What would close it:** Compute the one-loop Casimir energy of the SM field content on S^2. The Epstein vanishing theorem (Theorem K.1) kills all higher-loop corrections, so the one-loop result is exact. If V_Casimir(r_2) has a minimum at r_2 ~ 1/TeV, OC-2 is closed.

**The logic:**
1. Compute V_Casimir(r_2) = sum over SM fields of (+/-) zeta-regularised eigenvalues on S^2
2. Fermions (anti-periodic) contribute with opposite sign to bosons (periodic) — same mechanism as S^1
3. The top quark dominates (largest Yukawa) — its anti-periodic boundary conditions tilt the potential
4. If minimum exists at r_2 ~ 10^{-19} m, then M_KK ~ 1-2.5 TeV and m_H ~ 125 GeV is derived

**Downstream cascade:**
- Higgs mass becomes a genuine prediction, not a consistency check
- The "zero free parameters" claim for the SM sector becomes defensible
- Paper 4's reviewer criticism (r_2 unfixed, OC-2 open) is fully addressed
- The three-scale Casimir hierarchy (S^1 -> dark energy, S^2 -> EW scale, CP^2 -> GUT scale) is complete

**Estimated effort:** 1-2 sessions (spectral zeta on S^2 with SM content)
**Location:** Paper 4 Section 6.5b, 6.7; Paper 7 Section 6; attack plan at `etc/12-closing-the-open-problems-plan.md` Problem 2

---

### 3. Fast-Scrambler Property from e-Dimension Dynamics

**Paper:** 3
**Current status:** CONDITIONAL — Page curve (Theorem 7.1) assumes Sekino-Susskind fast-scrambler hypothesis

**The claim:** The entanglement entropy of Hawking radiation follows S_rad(t) = min[N_rad(t), N_BH(t)] x s_0, transitioning at the Page time t_Page ~ M^2. This reproduces the standard Page curve.

**What's missing:** The fast-scrambler property — that the e-sector evolves as a Haar-random unitary on the e-Hilbert space within the scrambling time t_scr ~ beta ln S_BH — is assumed, not derived.

**What would close it:** Derive the scrambling dynamics from the 5D theory:
1. The e-coordinates of Planck pixels on the horizon form a discrete dynamical system
2. The thermal dynamics (Hawking temperature T_H = 1/8piM) drive redistribution of e-values
3. The KK mode spectrum on S^1 gives a mixing rate calculable from the spectral gap
4. Show this mixing rate produces t_scr ~ beta ln S_BH

**The key insight (Pattern P1):** In the e-dimension framework, scrambling = redistribution of e-coordinates across horizon Planck pixels. This is a concrete dynamical system, not an abstract information-theoretic conjecture. The mixing time is a spectral gap computation on a finite graph (the Planck pixel lattice) with transition rates set by the Hawking temperature.

**Downstream cascade:**
- Page curve becomes unconditional (Theorem 7.1 upgraded)
- Black hole information preservation is fully proved, not just "conditional on scrambler"
- Paper 3 moves from "interesting proposal" to "rigorous resolution"
- The firewall resolution (already unconditional via Theorem 9.1) gains a complete dynamical picture

**Estimated effort:** Moderate — requires spectral analysis of the e-sector Hamiltonian on the horizon graph
**Location:** Paper 3 Section 7.6; Appendix A Sections A.2-A.9

---

### 4. Non-Perturbative Decoupling (Yang-Mills, Theorem 5)

**Paper:** 8
**Current status:** PROOF relies on Appelquist-Carazzone (1975), which is perturbative

**The claim:** The mass gap proved in the KK-enhanced theory (M^4 x CP^{N-1}) transfers to the standard 4D Yang-Mills theory. The KK modes decouple in the IR, leaving only the 4D gauge dynamics.

**What's missing:** Appelquist-Carazzone decoupling is a perturbative result. Its validity non-perturbatively is "not established" — flagged by reviewers as "the most significant logical gap in the proof chain."

**What would close it:** A spectral argument, not a perturbative one:
1. The Feshbach projection (Theorem 5) already defines the reduced transfer matrix T_red acting on the 4D Hilbert space
2. The KK modes have mass m_1 = 2sqrt(N)/r_3, giving exponential suppression e^{-m_1 a}
3. Show: the spectral gap of T_red is bounded below by the spectral gap of T_full minus O(e^{-m_1 a})
4. This is an operator inequality, not a perturbative expansion — it's non-perturbative by construction

**The key insight (Pattern P4):** The transfer matrix is a positive operator. Positivity + spectral gap = exponential decay of correlations. This is a theorem about operators, not about Feynman diagrams. The KK modes contribute to the transfer matrix with weight e^{-m_1 a} ~ e^{-10^{15}}, which is below any physical threshold.

**Current partial result:** IR equivalence already proved to 10^{-26} precision (sigma_std = sigma_KK + O(e^{-m_1 a})). The gap is upgrading this from "exponentially accurate numerical bound" to "rigorous operator inequality."

**Downstream cascade:**
- Yang-Mills mass gap proof chain becomes fully non-perturbative
- The most significant reviewer criticism is addressed
- Paper 8's claim "Proved" in the status table becomes airtight

**Estimated effort:** Moderate — requires functional analysis of the reduced transfer matrix
**Location:** Paper 8 Section 4.5 (Theorem 5); reviewer flag at `math-referee/runs/r03/verification-section4.md`

---

### 5. CP^2 Flux Tube Formation (Confinement Mechanism)

**Paper:** 5
**Current status:** CONJECTURED — geometric mechanism proposed, not proved

**The claim:** Chromoelectric flux is topologically constrained by the non-trivial 2-cycle structure of CP^2 (H_2(CP^2, Z) = Z), producing flux tubes with string tension sigma = (3/8pi^2) x g_3^2(M_3) / r_3^2.

**What's missing:** Three things, each explicitly identified as open:
1. Solve the 11D Yang-Mills equations with quark sources on M^4 x CP^2
2. Demonstrate the minimum-energy solution has a flux-tube profile
3. Show the energy grows linearly with quark separation (area law)

**What would close it:** A variational argument:
1. Write the 11D energy functional with quark boundary conditions
2. Show that the CP^2 2-cycle topology forces flux to concentrate (the flux cannot spread — it wraps the non-trivial cycle)
3. Demonstrate linear growth via a lower bound: E(R) >= sigma x R from the topological constraint

**Self-consistency evidence (not proof):**
- String tension formula gives sqrt(sigma) in [410, 510] MeV; experiment is 440 MeV
- Luscher coefficient prediction matches lattice at ~4%
- The holonomy correspondence (P2) correctly identifies the confining phase

**Downstream cascade:**
- Paper 5 moves from "proposes a geometric mechanism" to "derives confinement from geometry"
- The holonomy table (S^1 -> Coulomb, S^2 -> Higgs, CP^2 -> Confining) becomes a theorem, not a pattern
- Connects to Paper 8 (mass gap) — the CP^2 mechanism becomes the physical explanation for the mathematical result

**Estimated effort:** Major — this is essentially proving a version of confinement from geometry
**Location:** Paper 5 Section 2.3a, 3; reviewer responses at `reviewer-runs/r00/gap-responses.md`

---

### 6. OS3 Reflection Positivity (Exact, Full Non-Linear)

**Paper:** 3 (Appendix A)
**Current status:** CONDITIONAL on Assumption (A') — exact for linearised theory; approximate to 10^{-60} unconditionally

**The claim:** The 5D path integral satisfies Osterwalder-Schrader reflection positivity, required for constructive QFT axioms.

**What's missing:** The reduced assumption (A'): the operator -nabla^2_5 - Ric_5 has spectrum bounded below by zero on the e-Hilbert space. Three of four sub-assumptions proved; this spectral bound is the last.

**What would close it:** A Lichnerowicz-type inequality on the internal manifold. Since CP^2 x S^2 x S^1 has positive Ricci curvature (Fubini-Study on CP^2, round metric on S^2), the spectral bound should follow from standard differential geometry.

**Practical note:** The result is already unconditionally satisfied to (delta R / R_0)^2 < 10^{-60} precision — 47 orders of magnitude below any physical threshold. The remaining gap is mathematical completeness, not physical relevance.

**Downstream cascade:**
- Constructive QFT axiom verification becomes exact
- Paper 3's path integral formulation is fully rigorous

**Estimated effort:** Moderate — standard spectral geometry on compact manifolds with positive curvature
**Location:** Paper 3 Appendix A, Sections A.2-A.9; reduced assumption at Section A.9.6

---

### 7. Gauge Group from Entanglement Geometry (Global Topology)

**Paper:** 4
**Current status:** ESTABLISHED at Lie algebra level (Theorem 5.2); CONJECTURED at global topology

**The claim:** The non-abelian internal dimensions CP^2 x S^2 arise from the entanglement geometry of three fermionic generations. The SLOCC tangent space at the GHZ point carries the A_2 root system, matching su(3) + su(2) + u(1).

**What's missing:** The global topology — whether the internal manifold is precisely CP^2 x S^2 x S^1 or the flag manifold Fl(1,2;3). The Lie algebra match is proved; the Lie group match is conjectured.

**What would close it:** The Kirillov orbit method — show SU(2)^3/(Z_2)^3 -> SU(3) x SU(2) x U(1)/Z_6 via exceptional isomorphisms. This would answer "why SU(3) x SU(2) x U(1)?" — the deepest question in the series.

**Downstream cascade:**
- The Standard Model gauge group is derived from entanglement, not assumed
- The "why these symmetries?" question has a geometric answer
- Potentially a standalone paper

**Estimated effort:** 2-3 sessions for linear algebra (Steps 1-3); multiple sessions for orbit-method proof (Step 4)
**Location:** Paper 4 Section 5.4-5.5; attack plan at `etc/12-closing-the-open-problems-plan.md` Problem 4

---

### 8. L.1-L.4: The Four Clay Structural Conjectures (Yang-Mills)

**Paper:** 8 (Appendix L)
**Current status:** OPEN — four conjectures, each of comparable difficulty to known unsolved problems in constructive QFT

**The dependency chain:**
```
L.1 (Renormalised Composites) — FOUNDATIONAL, gates everything
  |
  +---> L.2 (Asymptotic Freedom Match) — mildest downstream; standard hypothesis once L.1 granted
  |
  +---> L.3 (Stress-Energy Tensor) — easiest downstream; Suzuki formula; 2-3 months after L.1
  |
  +---> L.4 (Operator Product Expansion) — hardest; remains open even with L.1-L.3
```

#### L.1: Renormalised Composite Operators

**What's proved:** Bare lattice operators are gauge-invariant with correct classical limit. Trace-anomaly identity exact in continuum perturbation theory. Lattice perturbative anomalous dimension matches continuum.

**What's open:** Non-perturbative existence of the continuum limit Z_O(a)^2 <O^bare(x) O^bare(y)> as a -> 0. No precedent in 4D non-Abelian YM.

**Attack route:** Gradient-flow regularisation (Suzuki, Makino-Suzuki). The flow operator O_t(x) = integral K(t,x,y) O(y) dy is automatically UV-finite at t > 0. The small-flow-time expansion O_t -> Z(t) [O]_R + ... gives the renormalised operator. Prove convergence non-perturbatively using the spectral data from the main body (mass gap + OS axioms).

**Effort:** Multiple original papers. This is the bottleneck.

#### L.2: Short-Distance Match to Asymptotic Freedom

**What's proved:** Continuum perturbative result (textbook). Reisz lattice power-counting theorem.

**What's open:** Non-perturbative = perturbative at short distances. Never proved for 4D non-Abelian YM. Standard assumption in all lattice QCD, never verified.

**Effort:** Conditional on L.1. Once L.1 is granted, L.2 reduces to one standard hypothesis.

#### L.3: Stress-Energy Tensor

**What's proved unconditionally:** Positivity H_OS >= 0 with H_OS Omega = 0 (reflection positivity + Osterwalder-Seiler). Conservation as Schwinger-Dyson Ward identity.

**What's open:** Operator-level identification H_OS = integral T_00 d^3x. Trace anomaly as exact operator identity.

**Attack route:** Suzuki gradient-flow construction gives automatically UV-finite T_μν at flow time t > 0. Take small-t limit. Ward identity fixes coefficients (Del Debbio-Patella-Rago).

**Effort:** 2-3 months follow-up, conditional on L.1. Easiest of the four.

#### L.4: Operator Product Expansion

**What's proved:** Coincident-point bound on n-point Schwinger functions (without OPE). Perturbative leading coefficients to 3 loops.

**What's open:** Non-perturbative OPE structure. Never constructed for 4D non-Abelian YM.

**Effort:** Hardest of the four. Multiple years or reduced to leading-order version.

**Location:** Paper 8 Appendix L (`preprint/sections/L-clay-conjectures.md`); gradient flow attack at `gradient-flow-attack-plan/`

---

### 9. Adiabatic Continuity for CP^2 Sigma Model at N = 3

**Paper:** 8
**Current status:** OPEN — proved at N = infinity (Witten 1979) and N = 2 (Unsal 2012), open at N = 3

**The claim:** The 2D CP^{N-1} sigma model on a finite torus has a mass gap that persists through the crossover from weak to strong coupling, with no phase transition.

**Why it matters:** This is the key step in the continuum limit argument for the Yang-Mills mass gap. The lattice proof (Section 4) establishes sigma > 0 and Delta > 0 at all physical couplings. The continuum limit (Section 5) requires adiabatic continuity to connect lattice to continuum.

**Three attacks explored:**
| Attack | Status | Key finding |
|--------|--------|-------------|
| Computer-assisted rigorous numerics | Ready to execute | 6-10 months, 60 core-days feasible |
| Center vortex F_v calculation | Partial | F_v^(0) > 0 proved; F_v^(1) at mL ~ 1 open |
| Monotonicity m(N) >= m(infinity) | Blocked | Potential is indefinite (cubic term); inequalities insufficient |

**Hardest link:** The crossover regime mL ~ 1 on finite torus. All three attacks converge here.

**Downstream cascade:**
- Continuum limit of Yang-Mills mass gap becomes unconditional
- Paper 8 Section 5 status table: "Proved (see Section 5.6)" becomes airtight

**Estimated effort:** 6-10 months (computer-assisted route); longer for analytic proof
**Location:** Paper 8 Section 5; STATUS.md; research notes on three attacks

---

## Priority Ranking

### Tier 1: High Impact, High Tractability (Do First)

| # | Target | Effort | What It Upgrades |
|---|--------|--------|------------------|
| **1** | Three-loop Mercedes E_3 | 2-4 weeks | All-orders UV finiteness: conditional -> verified at L=1,2,3 |
| **2** | OC-2: S^2 Casimir | 1-2 sessions | Higgs mass: consistency check -> prediction |

These are independent — they can run in parallel. Both are concrete computations with known methods. Either result, positive or negative, is informative.

### Tier 2: High Impact, Moderate Tractability (Next)

| # | Target | Effort | What It Upgrades |
|---|--------|--------|------------------|
| **3** | Fast-scrambler from e-dynamics | Weeks-months | Page curve: conditional -> unconditional |
| **4** | Non-pert. decoupling (Paper 8) | Weeks-months | YM proof chain: perturbative gap -> spectral bound |
| **5** | OS3 reflection positivity | Weeks | Constructive QFT axioms: approximate -> exact |

Items 3, 4, 5 are independent of each other. Item 3 uses Pattern P1 (geometric reinterpretation). Item 4 uses Pattern P4 (topological rigidity). Item 5 is standard spectral geometry.

### Tier 3: High Impact, Major Effort (Strategic Investments)

| # | Target | Effort | What It Upgrades |
|---|--------|--------|------------------|
| **6** | L.1 via gradient flow | Months-years | Gates L.2, L.3, L.4 -> Clay completion |
| **7** | Gauge group from entanglement | Months | "Why SU(3) x SU(2) x U(1)?" -> answered |
| **8** | CP^2 area law | Months-years | Confinement: proposed -> derived |
| **9** | Adiabatic continuity N=3 | 6-10 months | Continuum limit: conditional -> unconditional |

Items 6 and 9 connect: both involve the gradient flow programme already started in `gradient-flow-attack-plan/`. Item 7 is independent and could be a standalone paper. Item 8 is the deepest — essentially a geometric proof of confinement.

### Tier 4: Already Proved or Nearly Closed

| Item | Status |
|------|--------|
| Theorem K.1 (Epstein vanishing) | PROVED unconditional |
| Theorem 9.1 (firewall resolution) | PROVED unconditional (upgraded from Working Assumption) |
| Paper 4 Section 9.3 rewrite | Quick (1 hour) — bring text into coherence |

---

## The Cascade Effect

If Tier 1 and Tier 2 are closed, here is what the series looks like:

| Paper | Current strongest claim | After upgrades |
|-------|----------------------|----------------|
| 1 | UV finiteness proved at L=1,2; conditional at L>=3 | Verified at L=1,2,3; conditional only at L>=4 (much stronger) |
| 3 | Page curve conditional on fast-scrambler; firewall unconditional | Page curve unconditional; black hole information fully resolved |
| 4 | Higgs mass consistent for M_KK ~ 1-2.5 TeV (free parameter) | Higgs mass predicted from S^2 Casimir minimum |
| 5 | Confinement mechanism proposed | (Unchanged — Tier 3) |
| 8 | Mass gap proved; decoupling perturbative | Mass gap proved; decoupling non-perturbative |
| 10 | Scheme-independence at 1-loop and 2-loop | Extended toward all orders |

Five papers upgraded. The framework goes from "conditional in several places" to "conditional only on the deepest mathematical questions (area law, OPE, adiabatic continuity)."

---

## Execution Roadmap

```
Week 1-2:    Paper 4 Section 9.3 rewrite (1 hour, quick win)
             Begin Three-Loop Mercedes computation (Problem 1)
             Begin S^2 Casimir computation (Problem 2)
                  [parallel tracks]

Week 3-6:    Complete Mercedes E_3 numerical value
             Complete S^2 Casimir: does V(r_2) have a minimum?
             Begin fast-scrambler spectral analysis (Problem 3)

Month 2-3:   Mercedes algebraic structure (full factorisation proof at L=3)
             Non-perturbative decoupling spectral bound (Problem 4)
             OS3 spectral bound on Ric_5 (Problem 5)

Month 3-6:   Gradient flow programme: L.1 attack via Suzuki construction
             SLOCC-isometry orbit method (Problem 7, independent track)
             Adiabatic continuity: computer-assisted route (Problem 9)

Month 6+:    All-orders BPHZ factorisation (informed by L=3 data)
             L.3 stress tensor (conditional on L.1 progress)
             CP^2 area law variational argument (Problem 8)
```

---

*Nine gaps. Six patterns. One geometry. The machine is ready — point it at the gaps.*
