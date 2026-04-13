# Appendix Index -- Paper 28 (P != NP)

Maps each appendix letter to its ORA node file or repair draft, with a one-line description.
All paths are relative to `paper28-pvnp/`.

---

## A--B: Universal Algebra Proofs

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **A** | `clone-growth-fullness-bridge/nodes/1.1-UA1.md` | Taylor implies exponential clone growth (Bulatov--Zhuk dichotomy lifts to clone counting). |
| **B** | `clone-growth-fullness-bridge/nodes/1.2-UA2.md` | Non-Taylor Boolean clone has linear growth (Post's lattice classification). |

## C--D: Operator Algebra Constructions

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **C** | `clone-growth-fullness-bridge/nodes/1.3.1-Q_struct.md` | Non-injectivity of M_Bool^L: structural analysis of the Boolean BC factor. |
| **D** | `clone-growth-fullness-bridge/nodes/3.2-KEY-LEMMA-repair.md` | KEY LEMMA 3.4.3 repair: Boolean partition function asymptotics and KMS state construction. |

## E: CP-1 Proof with Repairs

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **E.1** | `clone-growth-fullness-bridge/nodes/2.1-CP1-formal.md` | Crossed-product identification M_Bool = L^infty(X_Bool) rtimes G_Bool (formal proof). |
| **E.2** | `preprint/repair-1-lemma-44.md` | Lemma 4.4 repair: non-invertible circuit absorption via fiber-averaging (replaces coordinate-projection). |
| **E.3** | `preprint/repair-2-mu-positive.md` | Positivity of mu_1(X_L) for satisfiable constraint languages (Feldman--Moore prerequisite). |
| **E.4** | `preprint/repair-3-lemma-51.md` | Lemma 5.1 repair: conditional expectation normality via Takesaki (replaces inapplicable BC 1995 citation). |
| **E.5** | `preprint/repair-4-prop-61.md` | Proposition 6.1(ii) repair: ergodicity of R_L via Toffoli universality (replaces wrong R_Bool-saturation argument). |
| **E.6** | `preprint/repair-4b-transitivity-gap.md` | Transitivity gap closure for Proposition 6.1(ii) at all clause densities (Feldman--Moore + Marrakchi). |
| **E.7** | `clone-growth-fullness-bridge/nodes/1.3.5.9-sector5.md` | SECTOR-5: conditional expectation E_L preserves the crossed-product decomposition. |

## F--G: Bridge Theorem Proofs

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **F** | `clone-growth-fullness-bridge/nodes/2.3-PathB-assembly.md` | Path B assembly: Taylor implies M_Bool^L is non-full (complete, unconditional proof of Part (i)). |
| **F.1** | `clone-growth-fullness-bridge/nodes/1.3.5.8-pathB-gaps.md` | Path B gap closure: A2 membership and uniform non-scalarity. |
| **F.2** | `preprint/p1-lemma-a-star-propagation.md` | Corrected Lemma A* propagation through Path B (two-sub-case proof). |
| **G** | `clone-growth-fullness-bridge/nodes/2.2-RouteC-assembly.md` | Route C assembly: non-Taylor implies M_Bool^L is full (Part (ii) via Marrakchi equivalence-relation formulation). |
| **G.1** | `clone-growth-fullness-bridge/nodes/1.3.5.6-biexact-repair.md` | Bi-exactness repair: fullness of G_L without V-embedding (Route C bypasses bi-exactness entirely). |
| **G.2** | `clone-growth-fullness-bridge/nodes/1.3.5.11-SE1-freeness.md` | SE-1: essential freeness of the G_L action on A|_L for non-Taylor constraint languages. |
| **G.3** | `clone-growth-fullness-bridge/nodes/1.3.5.12-NIA1-radical.md` | NIA-1: trivial amenable radical Rad(G_L) = {e} for non-Taylor languages (three independent proofs). |
| **G.4** | `clone-growth-fullness-bridge/nodes/1.3.5.5-gap-beta-fullness.md` | Gap Beta: three-route attack establishing fullness of M_Bool^L for NPC languages. |
| **G.5** | `clone-growth-fullness-bridge/nodes/1.3.5.13-area-law-fullness.md` | Area law as independent fifth route to Gap Beta (transposes YM mass gap argument). |
| **G.6** | `clone-growth-fullness-bridge/nodes/2.4-E1-string-tension.md` | E-1: string tension convergence (sigma_inf = 0.006 > 0). |

## H--I: Instance Diversity and Berry--Esseen

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **H** | `clone-growth-fullness-bridge/nodes/3.3-instance-diversity-formal.md` | Formal proof of the Instance Diversity Lemma (Lemma 2.6.4) via Phase Incoherence Condition (ID). |
| **H.1** | `clone-growth-fullness-bridge/nodes/1.3.5.10-instance-diversity-repair.md` | Instance diversity gap closure: computational validation that separation increases with arity. |
| **H.2** | `clone-growth-fullness-bridge/nodes/4.1-ID-approach1-explicit.md` | Explicit phase computation closing Condition (ID) via non-proportional rotation angles. |
| **H.3** | `clone-growth-fullness-bridge/nodes/4.2-ID-approach2-structural.md` | Structural proof of (ID) via Post's lattice; discovers and corrects Lemma A for the affine clone class. |
| **H.4** | `clone-growth-fullness-bridge/nodes/4.3-ID-approach3-bypass.md` | Approach 3: modified Marrakchi criterion (attempted bypass of instance diversity; reduces to known). |
| **I** | `preprint/p2-berry-esseen-writeup.md` | Berry--Esseen estimate for non-proportional rotation angles (rigorous backing for Condition (ID) closure). |

## J: Ergodicity via Feldman--Moore

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **J** | `preprint/repair-4b-transitivity-gap.md` | Closing the transitivity gap at all clause densities via Feldman--Moore 1977 + Jones--Schmidt 1987. |
| **J.1** | `preprint/repair-4-prop-61.md` | Corrected ergodicity argument for Proposition 6.1(ii) using Toffoli universality and Bennett reversibility. |

## K: CP-1 Independent Verification Verdict

| Appendix | Source file | Description |
|----------|-------------|-------------|
| **K** | `cp-1--verification/critiques/CP1-final-verdict.md` | Final adversarial verdict from 6 independent Critic agents (Wave 1 verification run). |

## L: Computational Scripts and Results Summary

All scripts are in `clone-growth-fullness-bridge/code/`. Key scripts:

| Script | Description |
|--------|-------------|
| `gap_alpha_compute.py` | Gap Alpha transfer matrix computation for 2-SAT (Node 1.3.5.1). |
| `gap_alpha_arity_scan.py` | Arity scan revealing rank-1 collapse of T_f at high arity. |
| `gap_alpha_residual.py` | Residual spectral gap analysis after rank-1 collapse. |
| `gap_alpha_multislot.py` | Multi-slot extension of Gap Alpha computation. |
| `gap_alpha_multislot_residual.py` | Multi-slot residual spectral gap analysis. |
| `instance_diversity_test.py` | Computational verification of instance diversity (Lemma 2.6.4). |
| `area_law_large_n.py` | Large-n area law computation (string tension convergence). |
| `phase_incoherence_test.py` | Phase incoherence condition (ID) numerical verification. |

### Supporting ORA node files for computational results

| Node file | Description |
|-----------|-------------|
| `nodes/1.3.5.1-gap-alpha-compute.md` | Gap Alpha killed: rank-1 collapse of T_maj at high arity. |
| `nodes/1.3.5.2-gap-alpha-multislot.md` | Multi-slot Gap Alpha extension. |
| `nodes/1.3.5.3-gap-alpha-residual.md` | Residual spectral gap after rank-1 collapse. |
| `nodes/1.3.5.4-gap-alpha-multislot-residual.md` | Multi-slot residual spectral gap. |
| `nodes/3.1-corollary-repair.md` | Corollary repair and partition function analysis (responds to Attacks 5 and 8). |

---

### Nodes not assigned to appendices (superseded or intermediate)

These nodes were consumed by the assembly nodes above and do not need separate appendix entries:

- `nodes/1.3-OA1.md` -- Polymorphism lift to outer automorphism (BLOCKED; superseded by spectral gap bypass 1.3.5).
- `nodes/1.3.2-construction-verify.md` -- Construction verification of alpha_f (partial; subsumed by CP-1).
- `nodes/1.3.3-outerness.md` -- Outerness of the polymorphism lift (conditional; subsumed by CP-1 + SECTOR-5).
- `nodes/1.3.5-spectral-gap-bypass.md` -- Master spectral gap bypass node (architectural; content distributed across sub-nodes).
- `nodes/1.3.5.7-CP1-crossed-product.md` -- CP-1 research node (superseded by formal proof 2.1-CP1-formal.md).
