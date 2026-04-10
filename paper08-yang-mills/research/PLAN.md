# Plan: From 90 Files to a Submittable Paper + the Computation

We have 90 files, 155K words, and nine agents worth of exploration.
The mathematical content is there. What's needed now:

1. Consolidate into a single submittable paper
2. Design and execute the computer-assisted proof
3. Test the Lüscher prediction against lattice data


---

## Phase 1: Paper Consolidation (write)

The 90 files contain four proved theorems, multiple dead ends (honestly
documented), and deep explorations. A submittable paper extracts the
proved results and states the open frontier clearly.

### Target structure: one paper, ~40 pages

**Title:** "Confinement at All Couplings and the Yang-Mills Mass Gap"

| Section | Content | Source files |
|---------|---------|-------------|
| 1. Introduction | The problem, the approach, what's proved | 02-introduction (rewrite) |
| 2. The KK-enhanced lattice theory | Definitions, CP^{N-1} geometry | 03-the-11d-arena, 21-rigorous-proof §I |
| 3. The SU(2) proof | Complete: 2D YM exact solution | 20-appendix-H (compress) |
| 4. The SU(N) proof | Cluster expansion: Lemma III.1, Theorem IV.1 | 25-cluster-expansion-proof |
| 5. The screening obstruction | Theorem B.1, Bogomolny suppression | 23-key-lemma-proof Parts B-C |
| 6. IR equivalence and the standard theory | Corollary V.2 (decoupling) | 25 §V |
| 7. The continuum limit | What's proved, what's open, the worldsheet reduction | 32-three-paths, 33-convergence-synthesis |
| 8. The 2D adiabatic continuity problem | Precise statement, three attacks, feasibility | 34-six-agent-synthesis, 35-final-verdict |
| 9. Quantitative predictions | σ = 437 MeV, c_eff(R) > 2 at intermediate R, glueball spectrum | 08-quantitative-results, 37-luscher-test-plan |
| 10. Conclusion | Four theorems, one computation | 35-final-verdict §VI |
| App A | CP² Laplacian spectrum | 12-appendix-A |
| App B | Bogomolny bound on CP² | 13-appendix-B |
| App C | Area law implies mass gap | 17-appendix-F |
| App D | Weitzenböck formula | 18-appendix-G |
| App E | 2D YM exact solution (full derivation) | 20-appendix-H §H.6 |
| App F | Vortex free energy calculation | attack-2 files |
| References | ~60 citations | 19-references (update) |

### Files to DROP (dead ends, superseded)

- 01-strategy.md (planning document, not paper content)
- 04-existence.md (superseded by §2 + lattice approach)
- 05-the-mass-gap.md §4.5 original (superseded by 25)
- 06-osterwalder-schrader.md (superseded: RP from Osterwalder-Seiler)
- 07-the-kk-bridge.md (eliminated: KK bridge was circular)
- 09-why-previous-approaches-failed.md (trim to one paragraph in intro)
- 10-open-problems.md (superseded by §8)
- 22-closing-the-gaps.md (absorbed into the rewrite)
- 24-continuum-limit.md (absorbed into §7)
- 26-proof-status.md (absorbed into §10)
- 27-continuum-limit-uniqueness.md (RETRACTED — circular)
- 28-continuum-without-lattice.md (creative exploration, not paper)
- 29-large-order-behavior.md (killed Borel approach, cite in §7)
- 30-final-synthesis.md (planning document)
- 31-decoupling-proof.md (RETRACTED — circular)

### Tasks

- [ ] Write consolidated Sections 1-10 + Appendices A-F
- [ ] Compile reference list
- [ ] Write LaTeX version (for arXiv submission)


---

## Phase 2: The Lüscher Test (compute, fast)

The fastest GO/NO-GO for the worldsheet path. Uses existing published
lattice data. Cost: zero. Timeline: 1-2 weeks.

### The corrected prediction

**IMPORTANT CORRECTION:** Nambu-Goto in d = 4 has d - 2 = 2 transverse
modes, giving Lüscher term -π(d-2)/(24R) = -π/(12R) and effective
central charge c_eff = 2. Our framework ALSO gives c_eff → 2 at large
R (the CP^{N-1} modes decouple).

The distinguishing signature is NOT the asymptotic coefficient but the
**R-dependence**: our framework predicts c_eff(R) > 2 at intermediate R
(massive CP^{N-1} modes partially active), approaching 2 from above.
Nambu-Goto predicts c_eff = 2 flat at all R.

### The quantitative prediction (SU(3), N = 3)

The CP^{N-1} worldsheet adds 2(N-1) = 4 massive internal modes with
mass m_int ≈ √σ ≈ 440 MeV. Their contribution to c_eff depends on
m_int × R:

| R√σ | Nambu-Goto c_eff | CP^{N-1} c_eff | Difference |
|-----|------------------|----------------|------------|
| 0.5 | 2.0 | ~2.9 | +0.9 (45%) |
| 1.0 | 2.0 | ~2.4 | +0.4 (20%) |
| 1.5 | 2.0 | ~2.15 | +0.15 (8%) |
| 2.0 | 2.0 | ~2.03 | +0.03 (1.5%) |
| ∞   | 2.0 | 2.0 | 0 |

Detectable at 3σ: need 6% precision on c_eff at R√σ ~ 1.

### The existing evidence (encouraging)

Multiple lattice groups have ALREADY found deviations from Nambu-Goto
at intermediate R:
- Caselle et al (2016): deviations at R√σ < 1, not fully explained by
  higher-order NG corrections
- Athenodorou-Teper (2017): excited string spectrum shows extra degrees
  of freedom beyond NG
- Dubovsky-Gorbenko-Mirbabayi (2015-2018): "axionic string" model with
  massive worldsheet modes improves fit to lattice data

These findings are CONSISTENT with massive CP^{N-1} modes. Our
framework may already be confirmed — the test is making it quantitative.

### The analysis plan

**Option A: Reanalyze published data (1-2 weeks, zero cost)**

1. Extract V(R) data from Caselle et al (2016) and Athenodorou-Teper
   (2017) published tables/supplementary materials
2. Define c_eff(R) = -(12/π) R [V(R) - σR - μ] at each R
3. Fit two models:
   - Model NG: c_eff = 2 (constant, 2 free params: σ, μ)
   - Model CP: c_eff = 2 + Σ (12/π) f(m_int R) with m_int ≈ √σ
     (3 free params: σ, μ, m_int)
4. Compare χ² — does the CP^{N-1} model fit better?
5. Extract m_int from the fit — does m_int ≈ √σ (the geometric
   prediction)?

**Option B: New dedicated simulation (2-4 weeks, modest cost)**

If published data lacks precision at R√σ ~ 0.5-1.5:
- SU(3) quenched, β = 6.2 (a ≈ 0.07 fm)
- Lattice 48³ × 96, APE-smeared Wilson loops
- V(R) at R/a = 3-10 (R = 0.2-0.7 fm)

### Decision criteria

- c_eff(R√σ ~ 1) = 2.4 ± 0.13 → **GO** (framework confirmed, proceed
  to Phase 3)
- c_eff(R√σ ~ 1) = 2.0 ± 0.13 → **STOP** (Path C fails, fall back to
  Path A multi-scale RG)
- Inconclusive → Option B (dedicated simulation)

### Tasks

- [ ] Collect published V(R) data (Caselle 2016, Athenodorou-Teper 2017)
- [ ] Compute c_eff(R) from the data at multiple R values
- [ ] Fit Model NG and Model CP to the data
- [ ] Compare χ² and extract m_int
- [ ] Write up result: "Evidence for CP^{N-1} modes on the QCD string"


---

## Phase 3: The 2D Computation (compute, 6-10 months)

The computer-assisted proof of the 2D CP² mass gap in the crossover
regime. This would close the continuum limit.

### Design (from Attack 1 agent)

1. **The transfer matrix** of the 2D CP² model on a strip of width
   $N_s$ sites with Z₃-twisted boundary conditions.

2. **Truncation:** CP² harmonics at $l_{max} = 4$ (error $6 \times
   10^{-17}$). Symmetry reduction by Z₃ × translation × C × P
   (factor ~12 N_s).

3. **Grid:** ~20 values of L in the crossover interval
   $mL \in [0.5, 5]$.

4. **Method:** Lanczos iteration with interval arithmetic (Krawczyk
   verification of eigenvalues). Certified gap = ln(λ₁/λ₂).

5. **Hardware:** 64-core node, 32 GB RAM. ~60 core-days for N_s = 16.

### Implementation plan

| Month | Task |
|-------|------|
| 1-2 | Implement CP² lattice action with Z₃ twist |
| 2-3 | Implement transfer matrix construction with truncation |
| 3-4 | Implement interval arithmetic eigenvalue solver (Krawczyk) |
| 4-5 | Validate against known CP² lattice data (Campostrini-Rossi) |
| 5-6 | Pilot computation: N_s = 4, 8 (direct diagonalization) |
| 6-8 | Production: N_s = 16 at 20 values of L |
| 8-9 | Analyze: certified m(L) > 0 at all grid points |
| 9-10 | Interpolate: analyticity + Lipschitz bounds fill gaps |

### Software

- Language: C++ or Rust (for performance)
- Interval arithmetic: Arb (C) or INTLAB (MATLAB)
- Eigenvalue solver: custom Lanczos with directed rounding
- Verification: two independent implementations + Monte Carlo cross-check

### Tasks

- [ ] Set up the 2D CP² lattice code
- [ ] Implement transfer matrix with CP² harmonics
- [ ] Implement interval arithmetic eigenvalue bounds
- [ ] Run pilot computation (N_s = 4, 8)
- [ ] Run production computation (N_s = 16)
- [ ] Write up the computer-assisted proof


---

## Phase 4: The Analytical Proof (research, longer term)

In parallel with the computation, pursue the analytical approaches:

### 4a. Monotonicity via the unitary trick

Generalize O(N) Griffiths inequalities to CP^{N-1} by embedding
CP^{N-1} → S^{2N-1}/U(1). Bound the gauge-orbit correction.
If successful: m(N) ≥ m(∞) = Λ > 0 for all N.

### 4b. Resurgence for the undeformed CP² model

Prove adiabatic continuity via the resurgent trans-series. Requires
proving the deformed → undeformed connection for N = 3.

### 4c. Center vortex free energy at mL ~ 1

Evaluate F_v^(1) numerically in the crossover regime. If
F_v^(1) > -3 F_v^(0) ≈ -1.18, adiabatic continuity follows.

### Tasks

- [ ] Investigate the unitary trick for CP² Griffiths inequalities
- [ ] Study adiabatic continuity for the deformed CP² model
- [ ] Numerically evaluate F_v^(1) at mL ~ 1


---

## Timeline and Order of Operations

| Order | Phase | Duration | Outcome |
|-------|-------|----------|---------|
| **NOW** | 2. Lüscher test | 1-2 weeks | GO/NO-GO for worldsheet path |
| **NOW** | 1. Paper consolidation | 2-4 weeks (parallel with Phase 2) | Submittable paper on arXiv |
| **IF GO** | 3. 2D computation | 6-10 months | Computer-assisted proof of 2D gap |
| **PARALLEL** | 4. Analytical proof | 1-3 years | Full analytical closure |

**Phase 2 comes FIRST** — it costs nothing (uses published data), takes
1-2 weeks, and is decisive. If c_eff(R) > 2 at intermediate R, the
worldsheet path is validated and Phases 3-4 are worth the investment.
If c_eff = 2 flat, Path C fails and we redirect to Path A (multi-scale
RG), saving 6-10 months.

**Phase 1 runs in parallel** with Phase 2. The four proved theorems are
independent of the Lüscher test — they stand regardless.

**Phase 3 starts only after Phase 2 gives GO.** The 6-10 month
investment in the 2D computer-assisted proof is justified only if the
worldsheet is confirmed to be CP^{N-1}.

**Phase 4 runs in parallel** with Phase 3. A purely analytical proof
(via Griffiths inequalities, resurgence, or anomaly matching) would be
more satisfying but is longer-term.
