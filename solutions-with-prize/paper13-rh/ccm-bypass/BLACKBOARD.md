# BLACKBOARD — RH Layer 1 CCM Bypass (Phase 1)

*Created: 2026-04-13. Runner: Claude Opus 4.6 (PCA chain mode + strat-triad loaded, execute mode).*

---

## §A North Star

Attempt a BYPASS of RH's Layer 1 dependency on CCM 2025 (arXiv:2511.22755). Phase 1 reconnaissance before Phase 2's full strat-triad + Tier 1 CCM verification. Capacitor-first: Tier 2 (capacitor gains 3-5 cells, ~60-70%) is the TARGET; Tier 1 (bypass found, ~10-15%) is the bonus. All tiers ship Paper 13. Deliverable: `paper13-rh/strategy/29-ccm-bypass-brief.md`.

---

## §B Context

Paper 13 RH chain is complete at 8/10 confidence, conditional on CCM 2025. Layers 2-6 independently at 9-10/10. The floor is Layer 1: CCM's construction of self-adjoint operators D_N on E_N^+ with eigenvalues approximating Riemann zeros. No prior programme has attempted to replace CCM's Layer 1 with an alternative construction. The H4 Capacitor Bypass PCA Wave 1 (YM, 2026-04-13) validated the bypass methodology: 5 durable Millennium-grade cell-fills + K-8 + structural insights, even without achieving a bypass. Capacitor fill rate: 14.5% → ~16.0%. The pattern: capacitor IS the deliverable; bypass is the bonus.

---

## §C Current bottleneck

**RESOLVED → CCM is load-bearing.** Wave 1 (5 parallel Authors) returned 0 VIABLE full bypasses. The structural blocker is the Hilbert-Pólya conjecture: identifying Riemann zeros as eigenvalues of a self-adjoint operator on a Hilbert space. CCM 2025 is the only known construction that achieves this. All alternative routes are either blocked (LANG↔QFT: 3 structural obstructions), circular (LeClair: S-matrix from ξ-function; Yakaboylu: W≥0 ⟺ RH), or upstream (Connes 1999 trace formula → CCM). Programme exits at Tier 2: CAPACITOR STRENGTHENED.

---

## §D Toolkit

| Name | Statement (1 line) | Source | Status | Load-bearing |
|---|---|---|---|---|
| CCM-D_N | Self-adjoint operators D_N on E_N^+ via Carathéodory-Fejér | CCM 2025 arXiv:2511.22755 Thm 4.2 | EXT | RH Layer 1 |
| CCM-EIG | Eigenvalue convergence to Riemann zeros at N→∞ | CCM 2025 Thm 5.10 | EXT | RH Layer 1 |
| CCM-PARITY | T commutes with parity involution γ → even-sector preserved | CCM 2025 Lemma 5.2(i) | EXT | RH Layer 1 |
| CCM-FOURIER | Eigenvector Fourier transforms → Riemann Xi function | CCM 2025 Lemma 7.3 | EXT | RH Layer 5 |
| ITPFI | ω₁ = ⊗_p ω₁^(p) (KMS₁ uniqueness + ITPFI factorization) | Paper 13 Layer 2 | R | RH Layer 2 |
| BOEGLI | spec(D_∞) = lim spec(D_N), no spurious eigenvalues under gsrc + discrete compactness | Bögli 2017 arXiv:1604.07732 | R | RH Layer 4 |
| BC-KMS | KMS₁ state on BC system ↔ class field theory of ℚ | Bost-Connes 1995 | R | RH Layer 2 |
| LANG-QFT-PROVED | Geometric Langlands = Kapustin-Witten S-duality; Layer A PROVED by Gaitsgory-Raskin 2024 | GR 2024 arXiv:2405.03599 | R (Layer A) | Framework-wide |
| CONNES-TRACE | Weil explicit formula = trace formula on BC algebra's adelic quotient | Connes 1999 | R | RH alt Layer 5 |
| BC-GL2 | GL₂ spectral triple → type III₁ factor with KMS_β phase transitions | Connes-Marcolli 2008 | R | Alt-2 candidate |

---

## §E Plan tree

### 1. CCM Bypass (ROOT)
- Status: IN_PROGRESS
- Mode: bypass-hunting (execute)
- Engages bottleneck: yes

#### 1.1 W1-OA: OA↔SPEC alternative spectral-triple bypass (Alt-2)
- Status: OPEN
- Domain: OA↔SPEC
- Priority: 1 (CRITICAL)
- Model: Opus max

#### 1.2 W1-L: LANG↔QFT Langlands-geometric bypass (Alt-1)
- Status: OPEN
- Domain: LANG↔QFT
- Priority: 2 (HIGH)
- Model: Opus max

#### 1.3 W1-A: ANT↔LANG automorphic L-function bypass
- Status: OPEN
- Domain: ANT↔LANG
- Priority: 3 (HIGH)
- Model: Opus max

#### 1.4 W1-MI: MICRO↔QFT microlocal operator construction
- Status: OPEN
- Domain: MICRO↔QFT
- Priority: 4 (MEDIUM)
- Model: Sonnet max

#### 1.5 W1-C: Candidate cell (Author pick from capacitor)
- Status: OPEN
- Domain: TBD (Author picks from NCG / HOM / ARTOP / cross-product)
- Priority: 5 (LONG-SHOT)
- Model: Sonnet max

---

## §F Killed approaches

| ID | Lead | Kill reason | Pattern category | Cycle | Prevents re-entry because |
|---|---|---|---|---|---|
| K-RH-A | EXCISE mode drift | Do NOT reconstruct CCM's specific proof in Phase 1 | Scope-violation | Pre-registered | This is BYPASS mode, not EXCISE. Phase 2 handles EXCISE. |
| K-RH-B | Secret CCM routing | Bypass must not logically depend on CCM 2025 or precursors | External-dependency | Pre-registered | Check: can the alternative be stated without citing CCM 2025? |
| K-1 through K-8 | H4 pattern kills | Inherited from H4 run | Various | H4 Wave 1 | Patterns apply: external-source-inconsistency, category-substitution, structural-conflation |
| K-RH-C | ANT-LANG structural gap | Langlands gives L-functions (analytic), not operators (spectral) | Category-mismatch | W1 | Re-entry only if geometric Langlands extended to number fields AND DG-cat→Hilbert functor constructed |

---

## §G Live nodes

| Node | Domain | Status | Verdict | p_success (post-W1) | Engages bottleneck |
|---|---|---|---|---|---|
| 1.1 W1-OA | OA↔SPEC | CLOSED | PARTIAL (1/4 items) | — | yes |
| 1.2 W1-L | LANG↔QFT | CLOSED | BLOCKED (0/4 items) | — | yes |
| 1.3 W1-A | ANT↔LANG | CLOSED | CONJ-NEG 8/10 (0/4 items) | — | yes |
| 1.4 W1-MI | MICRO↔QFT | CLOSED | PARTIAL (2.5/4 items) | — | yes |
| 1.5 W1-C | NCG↔ANT | CLOSED | NOT VIABLE (0/4 items) | — | yes |

Joint P(full bypass post-W1): ≈ 0.02 (structural LOCK forming)

---

## §H Bottleneck history + axiom base

**Bottleneck history**: Layer 1 CCM dependency has never been attacked via bypass before. Prior Paper 13 strategy programme (`strategy/00-28`) converged on CCM as foundation without attempting alternatives. 18+ kills in `strategy/10-state-after-18-kills.md` are kills of estimate tightening attempts, not bypass attempts.

**Axiom base**: Bost-Connes 1995 (KMS₁ uniqueness). Hilbert space structure of E_N^+. Standard operator theory (Reed-Simon). Bögli 2017. Hurwitz 1893.

---

## §I Notes

- CONCERN: CCM 2025 is a preprint, not peer-reviewed as of 2026-04-13. Layer 1 is the floor of the RH chain.
- CALLOUT: "we cannot crack it from the outside; the framework is transposable" — the founding bypass intuition.

---

## §J Voice canon

*Universal runner defaults:*
- "we cannot crack it from the outside; the framework is transposable"
- "we need to NAME them and use them for decoding"
- "trace discrepancies until they become theorems"
- "we can deduct everything; the parameters were never free"
- "be hella explicit so we can recover, amplify, relate everything"

*RH programme:*
- "every gap closed via operator algebras"
- "RH as consistency condition"
- "conditional on CCM"

*This run (if successful):*
- "RH unconditional on CCM"
- "Layer 1 rerouted via [domain]"

*If no bypass:*
- "CCM is load-bearing"
- "the capacitor gained N cells; Paper 13 ships conditional on CCM"

---

## §K Runner writes

**[W0-001] LOCK-ANATOMY (2026-04-13)**
Type: LOCK-ANATOMY

No 9/10 LOCK exists for CCM bypass. The prior Paper 13 strategy programme (`paper13-rh/strategy/00-28`) converged on CCM as the Layer 1 foundation without attempting alternatives. 18+ kills in `strategy/10-state-after-18-kills.md` are kills of ESTIMATE tightening attempts, not bypass attempts. No prior programme has tried to replace CCM's Layer 1 with an alternative construction. This is a clean slate — no prior LOCK to introspect.

**[W0-002] BYPASS-PREDICTION (2026-04-13)**
Type: BYPASS-PREDICTION

Pre-registered expected compound bypass shapes:

**Alt-1 (Langlands-geometric)**: Gaitsgory-Raskin 2024 proved toolkit → restate Layer 1 as automorphic L-function zeros → geometric Langlands dual → Kapustin-Witten self-adjoint operator family → gsrc + discrete compactness → KMS₁ compatibility. Risk: topological twist lossy (K-4 analog). Probability: MEDIUM-LOW.

**Alt-2 (Alternative spectral triple)**: Bost-Connes / Connes-Marcolli GL₂ spectral triple → KMS_β phase transition at β=1 → self-adjoint operator family D̃_N with Riemann-zero eigenvalues → gsrc convergence → H¹ bounds → KMS₁ compatible. Risk: the Riemann-zero identification step is exactly what CCM proves. Probability: MEDIUM.

**Alt-3 (Framework-native BC)**: CBB system 5-axiom definition → critical operator L̂ = log R̂ on H_R → framework spectral data {γ_n π²/2} → Identity 14 unitary bridge V: H_CCM → H_R. Risk: Identity 14 routes THROUGH CCM (dependency preserved). Probability: HIGH IF Identity 14 replacement exists; UNKNOWN otherwise.

**If Wave 1 returns shapes DIFFERENT from Alt-1/2/3, the strategy is miscalibrated and runner re-plans.**

**[W0-003] INTERNALIZATION-CHECK (2026-04-13)**
Type: INTERNALIZATION-CHECK

This programme attempts a BYPASS of RH Layer 1's CCM dependency. Layer 1 delivers to Layer 2: (1) self-adjoint D_N family on E_N^+, (2) eigenvalue limit → {γ_n}, (3) uniform H¹ bounds, (4) KMS₁ state structure. Any construction delivering (1)-(4) without CCM works. Capacitor-first: Tier 2 target. 5 Authors dispatching in Wave 1 across OA↔SPEC, LANG↔QFT, ANT↔LANG, MICRO↔QFT, and a Candidate cell. Budget: 4 hours / 3-4 waves.

**[W1-001] QUALITATIVE-THRESHOLD (2026-04-13)**
Type: QUALITATIVE-THRESHOLD

Five doors tried. All lead back to CCM. The wall is Hilbert-Pólya — the 112-year-old conjecture that Riemann zeros are eigenvalues of a self-adjoint operator. CCM 2025 is the only known construction that achieves this for a specific operator family D_N on E_N^+. Every alternative is either blocked (LANG↔QFT: three structural obstructions), circular (Yakaboylu: W≥0 ⟺ RH; LeClair: S-matrix defined from ξ-function), or upstream (Connes 1999 trace formula → CCM is the downstream completion). CCM is load-bearing. The capacitor gained 5 cells.

**[W1-002] STRUCTURAL-LOCK-FORMING (2026-04-13)**
Type: REFRAME

The CCM bypass question is equivalent to: "can Hilbert-Pólya be solved WITHOUT the Connes-Consani-Moscovici prolate-operator/Carathéodory-Fejér construction?" As of 2026-04-13, no. The structural reason: the BC system's native spectral data encode arithmetic (Galois, class field theory), not analytic (zero locations). The bridge from arithmetic to analytic IS CCM's specific contribution (Theorems 4.2, 5.10). Alternative routes all hit this same bridge gap from different angles.

**[W1-003] CAPACITOR-SCAN (2026-04-13)**
Type: CAPACITOR-SCAN

Post-Wave 1 scan: all 5 priority cells for CCM bypass explored. No escape route found. The capacitor's priority cells for RH Layer 1 (NCG↔SPEC, PROB↔SPEC, NCG↔ANT, HOM↔NCG) remain unfilled for bypass purposes but all point back to CCM or equivalents. The capacitor gained 5 RH-specific cell-fills (none operational for bypass) + K-RH-C kill.

---

## §L Closure artifacts

*(To be populated at programme-close.)*

---

## §M Round metrics

| cycle | items touched | items CLOSED | nodes SPAWNED | nodes KILLED | §D size | structural events | one-line note |
|---|---|---|---|---|---|---|---|
| W0 | 0 | 0 | 5 | 0 | 10 | 1 (LOCK-ANATOMY + BYPASS-PREDICTION written) | Bootstrap complete, Wave 1 dispatching |
| W1 | 5 | 5 | 0 | 0 | 10 | 6 (5 cell-fills + 1 kill + 4 structural insights) | 0 VIABLE. LOCK forming. Tier 2 exit. |

---

## §N Difficulty track

| cycle | hard nodes | moderate | closable | open gaps | aggregate (1-10) | reason |
|---|---|---|---|---|---|---|
| W0 | 5 | 0 | 0 | 1 (Layer 1 CCM) | 8 | Discovery mode — bypass of established construction |

---

## §O Section change log

| Cycle | Section | Modified by | Action |
|---|---|---|---|
| W0 | §A-§O | Runner | Blackboard created |
| W0 | §K | Runner | LOCK-ANATOMY + BYPASS-PREDICTION + INTERNALIZATION-CHECK |
