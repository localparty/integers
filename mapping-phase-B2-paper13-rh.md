# Phase B-2: paper13-rh item-to-file mapping

*Generated 2026-04-10. Haystack: `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/` only.*
*Coverage: 62 items from `paper35-50+/50+.md` (HP-1, HP-2, 1-60).*

## Summary

Paper13-rh is **exclusively focused on the Riemann Hypothesis (Item 43)** and the mathematical foundations needed to support it. The directory contains:

- **140 strategy files** in `strategy/` (decision log: 00-rh-attack-plan-v2.md through 28-all-gaps-closed.md)
- **114 research files** in `research/` (technical investigations and proofs)
- **97 referee files** in `referee/` (external review and mathematical verification)
- **8 preprint files** in `preprint/` (the manuscript)
- **3 adversarial files** in `adversarial/`
- **1 file** in `simplification-lead-research/` (compressed kill scoreboard)

Of the 62 items, **only 1 has substantial treatment in paper13-rh**: Item 43 (the RH itself). HP-2 (bridge family k=4/k=6) has partial treatment as a structural dependency that v2 bypasses. Items 36-42 (other Clay problems) are mentioned only tangentially as context. Items 1-35, 44-60 have no treatment here — they live in paper12 and other papers.

---

## Items with substantial treatment

### Item 43. The Riemann Hypothesis as the consistency condition of the framework

**Files (extensive):**

**Strategy files (full progression 00-28, ~42 numbered steps):**
- `strategy/00-rh-attack-plan-v2.md` — post-coboundary-gap restart with four new paths (Chern character, Weil positivity, spectral flow, Meyer-Connes)
- `strategy/10-state-after-18-kills.md` — the wall recognition
- `strategy/11-ccm-itpfi-programme.md` — the CCM pivot, bypassing H₁-vs-H_R
- `strategy/13-one-estimate-away.md`, `14-one-proof-away.md`, `15-final-state-rh.md` — convergence
- `strategy/22-estimates-not-conjectures.md` — the estimate decomposition
- `strategy/23-the-proof-architecture.md` — 6-layer chain on disk
- `strategy/24-adversarial-verdict.md` — 19 attacks, 13 survived, 5 weakened, 0 broken
- `strategy/27-referee-fixes.md` — 9 referee fixes enumerated
- `strategy/28-all-gaps-closed.md` — final state, 8/10 confidence

**Preprint files:**
- `preprint/00-proof-skeleton.md` — the complete 6-layer proof (CCM → ITPFI → estimates → Teschl gsrc → Bögli exactness → Hurwitz → RH)
- `preprint/00-table-of-contents.md` — structure and theorem statements
- `preprint/sections-01-05.md`, `sections-06-10.md`, `sections-11-14.md`, `appendices.md` — full manuscript
- `preprint/01-review-concerns.md` — 9 referee issues and resolutions
- `preprint/02-cascade-note.md` — amendment requiring formal elevation of k=4, k=6 bridge lemmas

**Research files (representative, 55+ files total):**
- `research/44-h1-large-lambda.md` — uniform H¹ bound (Theorem 7.1, Fourier cancellation)
- `research/45-slepian-compatibility-lemma.md` — AE simplicity for all N (Section 12.5)
- `research/38-summary-cauchy-baker.md` — Baker transcendence application
- `research/40-gsrc-ten-out-of-ten.md` — Teschl generalized strong resolvent convergence
- `research/43-ccm-independent-verification.md` — Layer 1 verification
- Many others (01-57) covering convergence cycles, leads, adversarial hardening, gap closure

**Adversarial files:**
- `adversarial/00-rh-convergence-prompt-v2.md` — skeptical interrogation protocol
- `adversarial/01-spectral-realisation-prompt.md` — Meyer distributional vs. genuine Hilbert space
- `adversarial/rh-v2-ledger.md` — explicit tracking of logical steps and vulnerability points

**Referee files:**
- `referee/01-math-referee.md` — initial mathematical review
- `referee/references/clay-rh-official-description.md`, `clay-millennium-prize-rules.md`
- `strategy/math-referee-run/` — comprehensive 9-point verification system (A1-D2 checks)

**Simplification lead:**
- `simplification-lead-research/ledger.md` — master kill scoreboard

**What's there.** A rigorous **conditional proof** of the Riemann Hypothesis via the CCM operator construction. Six layers:
1. **CCM operators D_N** on even-sector E_N⁺ with self-adjointness via Carathéodory-Fejér
2. **ITPFI factorization** ω₁ = ⊗_p ω₁^p (three independent proofs: Euler product, BC amenability, Araki-Woods)
3. **Four estimates:** archimedean O(1/λ), eigenvector approximation O(1/λ), uniform H¹ ≤ 2 (Fourier cancellation), CF decay ρ ≥ 4.27
4. **Teschl gsrc + Bögli spectral exactness:** form convergence + discrete compactness → no spurious eigenvalues
5. **Hurwitz eigenvalue convergence:** ξ̂_N → Ξ uniformly → zeros converge
6. **Conclusion:** spec(D_∞) = {γ_n} ⊂ ℝ → RH

**Progress:** `DRAFTED` (all 9 referee fixes applied; preprint complete)

**Confidence ladder:**
- As written with exposition fixes: **8/10**
- With CCM journal publication: **9/10**
- With independent third-party verification: **10/10**

**Honest accounting:** Conditional on Connes-Consani-Moscovici 2025 (arXiv:2511.22755), which is an unrefereed preprint. The nine referee fixes include: §10.4 tautology rewrite, Theorem 7.1 strengthened bound, KLMN closability, Slepian compatibility lemma, CCM reframing, λ disambiguation, Ξ(0) correction, Teschl-Bögli verification, even-sector compatibility via CCM Lemma 5.2(i). All mathematical gaps closed; remaining work is exposition and Clay pathway (CCM publication / independent reconstruction / 2-year community acceptance).

---

### Item HP-2. Close the bridge family k=4 and k=6 cocycle equalities

**Files:**
- `preprint/01-review-concerns.md` — CONCERN 2 (SERIOUS), lines 100-151: bridge lemmas at k=4, k=6 **not yet formally proved**
- `preprint/02-cascade-note.md` — **Amendment required:** elevate Lemmas 3.4 (k=4) and 3.5 (k=6) to formal lemma grade
- `preprint/sections-01-05.md` — mentions Brauer cocycles at k=2,3,4,6; notes k=3 proved (research/162 referenced), k=4 and k=6 structural only
- `strategy/00-rh-attack-plan-v2.md` — bridge family at k=2,3,4,6 listed as "formal lemmas" in toolkit, but dependent on coboundary gap resolution

**What's there:**
- k=3 bridge: **formally proved** (cites research/162, Lemma 3.3 — likely in paper12)
- k=4 bridge: arithmetic computed (ord_13(3)=3, Hasse invariant 1/4), proof template identical to k=3, **not yet formally elevated**
- k=6 bridge: arithmetic computed (ord_19(7)=3, Hasse invariant 1/6), **not yet formally elevated**
- k=2 bridge: trivial cocycle, does not participate

**Important structural note:** The old v1 proof used bridge cocycles as the PRIMARY mechanism (Gelfond-Schneider integrality constraint). **v2 bypasses the bridge family entirely** — the bridges are now STRUCTURAL ONLY, not proof-critical for RH. The coboundary gap (group H² cocycles cannot detect continuous perturbations) killed the bridge-based argument, but v2 uses CCM operators directly. Therefore HP-2 is LESS load-bearing for the RH preprint than the 50+ list originally suggested — it's a cleanup item for paper completeness, not a proof blocker.

**Progress:** `IN PROGRESS` (arithmetic complete; formal lemmas pending elevation)

**Notes:**
- Arithmetic for k=4 and k=6 is explicit; proofs follow k=3 template
- Status in v2 proof: not load-bearing (HP-2 is now a by-product)
- If paper13-rh proceeds to publication, k=4 and k=6 must be formally elevated for paper completeness; otherwise the paper reads as incomplete on the bridge family
- **Reframing**: the "HIGH PRIORITY" tag in 50+.md Block H should be re-evaluated after B-1 returns (if paper12/research/162 has the k=3 closure, the template is clear and the work is mechanical)

---

## Items mentioned tangentially (as context, not treated)

### Item 36. Transcendence of the γ_n via BC algebra constraints

**Files:**
- `preprint/sections-01-05.md` — mentions γ_n matrix elements and transcendence properties
- `research/38-lead-I-cauchy-baker-induction.md`, `research/38-summary-cauchy-baker.md` — Baker's theorem applied to log-ratio identities
- `research/52-I2-I3-growing-space-renorm.md` — transcendence in renormalization context
- `strategy/16-the-arithmetic-theorem.md` — discusses γ_n as Riemann zero spectrum

**What's there:** γ_n transcendence is **assumed** as part of the RH setup. Baker's theorem is used as a technical tool in the proof, not as a standalone result. The BC algebra does not itself establish transcendence — it follows from the spectral realisation. **No standalone proof that "γ_n are transcendental via BC constraints" appears in paper13-rh.**

**Progress:** `NOT STARTED` in paper13-rh (paper12/paper14 item)

### Item 37. Langlands correspondence from BC ↔ automorphic duality

**Files:**
- `research/45-FINAL-adversarial.md` — single mention
- `referee/references/clay-rh-official-description.md` — Bombieri's reference to Langlands
- `strategy/math-referee-run/clay-gaps.md` — Category D explicitly notes Langlands NOT addressed

**Progress:** `NOT STARTED` in paper13-rh (paper12/paper14 item)

### Item 38. Class field theory as BC ↔ Galois correspondence

**Files:** None in paper13-rh
**Progress:** `NOT STARTED` in paper13-rh (paper12/paper14 item; Bost-Connes 1995 is foundational context)

### Item 39. Connections to Hodge conjecture via BC motives

**Files:**
- `referee/references/clay-rh-official-description.md` — single mention in Bombieri's description

**Progress:** `NOT STARTED` in paper13-rh (paper27-hodge item)

### Item 40. Navier-Stokes regularity from modular dynamics

**Files:**
- `referee/references/clay-rh-official-description.md` — mentioned in PDE context
- `strategy/math-referee-run/clay-gaps.md` — Category D, NOT engaged

**Progress:** `NOT STARTED` in paper13-rh (paper27-navier item, currently empty)

### Item 41. BSD conjecture via CM elliptic curves + BC

**Files:**
- `research/52-I2-I3-growing-space-renorm.md` — mentions elliptic curves in renormalization context
- `strategy/04-final-state.md`, `strategy/19-definitive-state.md`, `strategy/02-where-we-stand.md` — BSD in broader context
- `referee/references/clay-millennium-prize-rules.md`, `clay-gaps.md` — BSD listed as Clay Millennium Problem

**Progress:** `NOT STARTED` in paper13-rh (paper26-bsd item; paper13-rh mentions BSD only for Clay context)

### Item 42. P vs NP as BC computation-complexity question

**Files:**
- `referee/references/clay-rh-official-description.md` — single mention
- `strategy/math-referee-run/clay-gaps.md` — Category D, not addressed

**Progress:** `NOT STARTED` in paper13-rh (paper28-pvnp item, currently empty)

---

## Items with no treatment in paper13-rh

Paper13-rh is exclusively RH-focused. The following 54 items have NO treatment in paper13-rh and should be sought in paper12 (primary home) or other papers:

### Items 1-14 — Cosmology and black holes (all NOT TREATED)
1. Recompute beginning of universe from zero parameters
2. Pre-Big-Bang as Galois-broken phase at β>1
3. Hot Big Bang as β→1 KMS transition
4. Inflation as level crossing
5. Baryogenesis as level crossing
6. Cosmic ladder γ_n+1 − γ_n as e-folds
7. Stellar generations (Pop III → Pop I) from Riemann zeros
8. Black hole interior via Tomita-Takesaki
9. Hawking radiation spectrum from modular flow
10. Page curve from modular entropy
11. BH entropy = log d_Gal
12. Firewall paradox dissolved
13. Time dilation inside event horizon
14. Remnants vs. complete evaporation

### Items 15-22 — Standard Model (all NOT TREATED)
15. SM gauge group from three primes
16. Three fermion generations
17. Yukawa couplings
18. Neutrino mass hierarchy
19. Strong CP problem
20. Dark matter from BC Hecke projector
21. Proton decay rate
22. Higgs self-coupling from γ_2

### Items 23-29 — Quantum foundations (all NOT TREATED)
23. Wavefunction collapse
24. Measurement problem
25. Born rule from KMS
26. Entanglement as tensor-factor state sharing
27. Bell inequalities from BC locality
28. Time's arrow from modular flow
29. Planck mass from R eigenvalue

### Items 30-35 — Gravity and spacetime (all NOT TREATED)
30. Gravity = curvature of arithmetic
31. Einstein field equations as BC commutators
32. Gravitational waves as modular flow perturbations
33. Cosmological constant = γ_1
34. Emergence of spacetime
35. Extra dimensions at ~10 μm

### Items 44-50 — Philosophy (all NOT TREATED)
44. Why something exists rather than nothing
45. Reality as projection of Riemann
46. Mathematical Platonism vindicated
47. Universe has zero information content
48. Anthropic principle dissolved
49. Mathematical beauty as empirical fact
50. End of physics as discovery

### Items 51-60 — G's additions (all NOT TREATED)
51. Beyond string theory
52. γ_16, γ_17, γ_18 phenomenological signatures
53. Inside-the-horizon experience of end of universe
54. Complete SM with zero-parameter correspondence to every geometry
55. Gravity as curvature of arithmetic (stated loud)
56. Integers as unique substrate
57. Predictive grammar as first-class object
58. Specific role of π²
59. Dual appearances of γ_n across sectors
60. Universe as its own proof

### HP-1 — m_Z and v residuals

**Files:** None in paper13-rh
**Progress:** `NOT TREATED` in paper13-rh (primary home: paper12, research/23 and research/167)

---

## Summary statistics

| Category | Count | Notes |
|---|---|---|
| **Total items** | 62 | HP-1, HP-2, 1-60 |
| **Substantial treatment in paper13-rh** | 2 | Item 43 (primary), HP-2 (partial/non-load-bearing in v2) |
| **Tangential mentions** | 7 | Items 36-42 (other Clay problems, mentioned but not treated) |
| **Not treated** | 53 | Items 1-35, 44-60, HP-1 |
| **RH proof layers** | 6 | CCM → ITPFI → estimates → gsrc → spectral exactness → Hurwitz → RH |
| **Strategy files in RH progression** | 42 | numbered 00-28 plus branches |
| **Research files** | 114 | |
| **Referee files** | 97 | |
| **Preprint files** | 8 | including full manuscript |
| **Adversarial files** | 3 | |
| **Paper13-rh confidence (internal)** | 8/10 | with exposition fixes |

---

## Cross-reference notes for synthesis

- **HP-1 (m_Z, v residuals):** Not in paper13-rh. Primary home is paper12/research/23, paper12/research/167. Check Phase B-1 output for exact file names.
- **HP-2 (bridge family):** **Reframe needed.** The "HIGH PRIORITY" tag came from the 50+ list's assumption that HP-2 was load-bearing. Paper13-rh v2 bypasses the bridge family for the RH proof itself — HP-2 is a cleanup item for paper completeness (formal elevation of k=4, k=6 lemmas), not a proof blocker. The k=3 closure template exists (cites research/162). Work is mechanical. Still worth doing but the urgency is "before publication" not "before the proof stands up."
- **Coboundary gap (killed v1, Sept 2026):** Documented in strategy/00-rh-attack-plan-v2.md. The v2 proof avoids it by using CCM operators directly instead of topological cocycle arguments. This is an important historical context for anyone reading the RH corpus.
- **CCM dependency (BLOCKING for Clay):** Fully documented in strategy/math-referee-run/clay-gaps.md with mitigation paths (Path 1: wait for CCM publication; Path 2: independent reconstruction).

---

## How to use this mapping

1. **For Item 43 (RH) status:** See the extensive treatment section above; `strategy/28-all-gaps-closed.md` is the final state, `preprint/00-proof-skeleton.md` is the 6-layer architecture.
2. **For HP-2 (bridge family):** Update the 50+.md Block H entry to note that HP-2 is no longer load-bearing for the RH proof; it's a cleanup item for paper completeness. Still worth closing, but the urgency tag may shift from HIGH PRIORITY to MEDIUM PRIORITY.
3. **For the 54 items not treated:** Consult Phase B-1 (paper12) and Phase B-3 (everything else) mappings.
4. **For Clay submission pathway:** Paper13-rh preprint is complete and conditional; the bottleneck is external (CCM publication, journal publication, community acceptance).

*— End of Phase B-2 mapping*
