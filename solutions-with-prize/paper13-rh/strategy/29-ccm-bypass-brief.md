# RH Layer-1 CCM Bypass — PCA Deliverable (Phase 1: Reconnaissance Before Tier 1 CCM Verification)

*This file is the deliverable for a time-boxed PCA run attempting to BYPASS Layer 1's dependency on Connes-Consani-Moscovici 2025 (arXiv:2511.22755). The run is capacitor-first, not proof-first — the goal is to discover whether Layer 1 admits an alternative construction that doesn't route through CCM's specific spectral realization. A successful bypass makes RH unconditional on CCM; a CONJECTURED-NEGATIVE outcome confirms CCM is structurally load-bearing and sharpens Phase 2 (Tier 1 CCM verification + full strat-triad).*

*This is Phase 1 of a two-phase RH strengthening programme. Phase 1 runs bypass-first to inform Phase 2. Phase 2 (file `21-rh-chain-strat-triad-run.md`) runs the full VERIFY/EXCISE/CONSTRUCT strat-triad on all 6 layers + Tier 1 CCM verification, with scope calibrated by Phase 1's findings.*

---

## 1. What Layer 1 is and what it needs from CCM

**Layer 1 of the RH proof chain** (per `preprint/00-proof-skeleton.md`) establishes the spectral realization of Riemann zeros via self-adjoint operators $D_N$ on even-sector Hilbert spaces $E_N^+$. The construction uses:

| CCM result | Role in Layer 1 | Paper 13 usage |
|---|---|---|
| CCM Thm 4.2 (self-adjointness of $D_N$ via Carathéodory-Fejér) | Foundation — ensures $D_N$ is self-adjoint on $E_N^+$ | Every eigenvalue argument in Layers 1-5 assumes $D_N^* = D_N$ |
| CCM Thm 5.10 (eigenvalue convergence to Riemann zeros) | Finite-$N$ approximation fidelity | Underwrites the 55-digit numerical match at $N=6$ and the asymptotic zero-identification program |
| CCM Lemma 5.2(i) ($T$ commutes with parity involution $\gamma$) | Sector reduction — lets us work on $E_N^+$ only | Without this, the even-simple hypothesis cannot reduce to simple-on-$E_N^+$ |
| CCM Lemma 7.2 (eigenvector parity properties) | Fourier structure of eigenvectors | Load-bearing for Layer 5 Hurwitz convergence argument |
| CCM Lemma 7.3 (Fourier transforms of eigenvectors → Riemann Xi function) | The spectral-to-Xi bridge | The actual identification of $\text{spec}(D_\infty)$ with $\{\gamma_n\}$ |

**What we close (Paper 13 contribution)**: passing from finite $N$ to $D_\infty$ via ITPFI factorization + Teschl gsrc + Bögli spectral exactness (Layers 2-4), then Hurwitz zero convergence (Layer 5) → RH as consistency condition (Layer 6).

**What remains conditional**: CCM's construction of $D_N$ with the above properties. If CCM is right, RH falls via our chain (conditional on CCM). If CCM is wrong, Layer 1 has no foundation and RH ships with no chain at all.

**Why a bypass makes sense**: CCM 2025 is a preprint (arXiv:2511.22755), not peer-reviewed as of 2026-04-13. Before committing significant effort to verifying CCM (Phase 2 / Tier 1), we ask: can Layer 1 be built via a DIFFERENT construction that doesn't depend on CCM's specific machinery? If yes → CCM becomes optional, RH becomes unconditional on CCM. If no → CCM is structurally load-bearing, Phase 2's Tier 1 verification becomes the mandatory priority.

---

## 2. The bypass target — precisely

**BYPASS vs EXCISE distinction**:
- **BYPASS** (this run's mode): find an alternative Layer 1 that reaches Layer 2's input WITHOUT requiring CCM's specific spectral realization. The step "Layer 1 via CCM" becomes obsolete; a different Layer-1-replacement takes its place.
- **EXCISE** (out of scope for this run): prove exactly what CCM proves via our own machinery. This would be a full reconstruction of CCM's Theorems 4.2, 5.10 and Lemmas 5.2(i), 7.2, 7.3 in our own framework — a much larger task than bypass.

**Phase 1 target (this run)**: attempt BYPASS. Phase 2 handles EXCISE as part of the strat-triad if bypass fails.

**What Layer 2 actually needs from Layer 1** (the real interface — bypass must reproduce THIS, not CCM specifically):

Layer 2 (ITPFI factorization) receives from Layer 1:
1. A sequence of self-adjoint operators $D_N$ on Hilbert spaces $E_N^+$ converging to $D_\infty$ on $E_\infty^+$ in the generalized strong resolvent sense (gsrc)
2. $D_N$ with eigenvalues that, in the $N \to \infty$ limit, coincide with the non-trivial Riemann zeros $\{\gamma_n\}$
3. Uniform $H^1$ bounds on eigenvectors (for discrete compactness → Bögli spectral exactness in Layer 4)
4. The KMS$_1$ state structure on the BC algebra side that makes ITPFI factorization possible

**Any Layer-1-replacement that delivers (1)-(4) works — CCM's specific construction is NOT required.**

---

## 3. The capacitor-first framing (from H4 run lessons)

The H4 bypass run proved a pattern: **the capacitor is the real deliverable; successful bypass is the bonus.** Wave 1 returned 5 CONJECTURED-NEGATIVE verdicts for H4 and STILL produced Millennium-grade cell-fills + K-8 + $C_N$ orthogonality insight + Gaitsgory-Raskin 2024 PROVED status. Capacitor fill rate grew 14.5% → 16.3%. The wall stayed named; the framework gained substantially.

**This run inherits that frame**:
- **Tier 2 (target, ~60-75%)**: capacitor gains 3-5 new cells in SPEC / OA / ANT / LANG / MICRO rows relevant to Layer 1. RH stays conditional on CCM; Phase 2 follows with Tier 1 CCM verification.
- **Tier 1 (bonus, ~10-15%)**: a compound bypass produces a Layer-1-replacement that delivers items 1-4 from §2 without CCM. RH becomes unconditional on CCM; Phase 2's Tier 1 CCM verification becomes optional.
- **Tier 3 (avoid, ~15-25%)**: no cell-fills, no kills, no structural insights. §3.3 discipline (mandatory cell-fill per Author) exists precisely to prevent this.

**All three tiers ship Paper 13.** The only question is whether Paper 13 ships with CCM conditional (Tier 2/3) or CCM unconditional (Tier 1). In all cases the capacitor grows and Phase 2's planning is sharpened.

---

## 4. What the PCA should do

### 4.1 Wave 0 — LOCK introspection (unlike H4, minimal)

**Unlike H4, there is no prior LOCK on CCM bypass attempts.** No prior programme has tried to replace CCM's Layer 1 with an alternative construction. Wave 0 produces:

1. **LOCK-ANATOMY entry** stating: *"No 9/10 LOCK exists for CCM bypass. The prior Paper 13 strategy programme (`solutions-with-prize/paper13-rh/strategy/00-28`) converged on CCM as the Layer 1 foundation without attempting alternatives. 18+ kills in `strategy/10-state-after-18-kills.md` are kills of ESTIMATE tightening attempts, not bypass attempts."*
2. **BYPASS-PREDICTION entry** pre-registering the expected compound bypass shapes (two candidates — see §6 below).

No LOCK-ANATOMY Critic dispatch needed (there's nothing to verify against). Runner proceeds to Wave 1 directly after §K entries written.

### 4.2 Wave 1 — 5 parallel Author dispatch

The target is Layer 1's CCM dependency. Priority capacitor cells (post-H4-integration):

| Priority | Cell | Why it might provide a Layer-1-replacement | Live literature |
|---|---|---|---|
| **1 (CRITICAL)** | **OA↔SPEC** (operator algebras ↔ spectral theory) | Alternative spectral-triple constructions for BC algebras. Jaffe-Stoytchev (1997), Bost-Connes type III_1 realizations, Connes-Marcolli crossed-product constructions. Layer 1 could route through an alternative spectral triple without CCM's specific prolate-operator machinery. | Connes-Marcolli 2008 (GL_2 system); Bost-Connes 1995; Jaffe-Stoytchev 1997; Meyer 2005 |
| **2 (HIGH)** | **LANG↔QFT** (Kapustin-Witten / Gaitsgory-Raskin 2024) | Post-2024: geometric Langlands is PROVED. If RH has a Langlands-adjacent formulation (automorphic L-function zeros on critical line), the proved toolkit is now available. Could give an alternative Layer 1 via automorphic methods entirely. | Gaitsgory-Raskin 2024 (arXiv:2405.03599–2409.09856); Kapustin-Witten 2007; Frenkel lectures |
| **3 (HIGH)** | **ANT↔LANG** (automorphic ↔ Galois) | Functoriality conjecture + L-function factorization. Combined with Gaitsgory-Raskin 2024, opens a geometric-arithmetic route to Layer 1's spectral-realization requirement without CCM. | Classical Langlands + Gaitsgory-Raskin 2024 geometric side |
| **4 (MEDIUM)** | **MICRO↔QFT** (microlocal / axiomatic QFT) | If Layer 1 requires a self-adjoint operator with specific eigenvalue structure, microlocal propagation-of-singularities techniques could construct such an operator via non-perturbative AQFT-style argument. Framework tool from H4 run (W1-M). | BFR 2025 §4 (scalar-only); Hollands-Wald 2024; Dappiaggi 2023-2024 |
| **5 (LONG-SHOT)** | **Candidate cell (W1-C pick)** | Author chooses from capacitor v1 §"Candidate cells" — NCG, HOM, ARTOP, or a cross-product cell. Pure capacitor exploration for RH. | Runtime pick |

Each Author produces a cell-fill entry per §3.3 v2 discipline (Statement / Mechanism / Source / Status / Verification / Load-bearing / Transposition recipe) regardless of bypass verdict.

### 4.3 Wave 2 — proof expansion + cell-fills

For each VIABLE Wave 1 verdict, dispatch proof Author + Critic pair. For PARTIAL verdicts, dispatch Cell-Fill Author to complete the cell. For FAILED verdicts, confirm cell-fill entries are complete with CONJECTURED-NEGATIVE status.

### 4.4 Wave 3 — adversarial pass

Critics on any proposed bypass from Wave 2. Each step of a compound bypass gets its own Critic. If EVERY step SURVIVED → Tier 1 success. Otherwise → Tier 2 / exit.

---

## 5. Pre-registered expected bypass shapes

### Alternative-1: Langlands-geometric Layer 1 replacement

Using Gaitsgory-Raskin 2024 proved toolkit:

- **Step 1**: Restate Layer 1's spectral realization requirement as a statement about automorphic L-function zeros (Artin-reciprocity shell)
- **Step 2**: Apply geometric Langlands (now PROVED) to map to a Hitchin-moduli-space statement on the dual side
- **Step 3**: Use Kapustin-Witten type structure to produce the required self-adjoint operator family
- **Step 4**: Verify gsrc convergence + discrete compactness conditions (which Bögli/Layer 4 needs) from the dual-side construction
- **Step 5**: Connect back to BC algebra KMS$_1$ state for Layer 2's ITPFI entry point

Risk: topological twist lossy (same K-4-analog from H4 run). The short-distance spectral information may be killed by twist. Probability: MEDIUM-LOW.

### Alternative-2: Alternative spectral-triple Layer 1 replacement

Using OA↔SPEC cell:

- **Step 1**: Use Bost-Connes / Connes-Marcolli GL_2 spectral triple construction (type III_1 factor, KMS_\beta phase transitions)
- **Step 2**: Show the phase transition at $\beta=1$ produces a self-adjoint operator family $\tilde{D}_N$ with Riemann-zero eigenvalues (this would be a NEW result, but plausible given the Bost-Connes framework explicitly realizes Galois action on zeros)
- **Step 3**: Verify $\tilde{D}_N \to \tilde{D}_\infty$ gsrc convergence
- **Step 4**: Match eigenvectors' $H^1$ bounds for Layer 4 Bögli hypothesis
- **Step 5**: Confirm KMS_1 state structure is compatible with Layer 2 ITPFI

Risk: the Bost-Connes construction naturally produces Galois data, but the Riemann-zero identification step (§2) is exactly what CCM spent 30 pages proving. An OA↔SPEC alternative would need to prove it differently. Probability: MEDIUM.

### Alternative-3: Framework-native Layer 1 via BC algebra directly

Using the Integers programme (Paper 12) + CBB system (Paper 23, 24, 25):

- **Step 1**: Use the 5-axiom CBB system definition (research/213, integers/paper12-cbb-system/27-anchor-document.md) to directly characterize $D_N$ via the critical operator $L̂ = \log R̂$ on $H_R \subset H_1$
- **Step 2**: Show the framework's own spectral data {$\gamma_n \pi^2/2$} provides the eigenvalue structure Layer 2 needs
- **Step 3**: Verify KMS_1 state structure matches (this is literally what the CBB system axiomatizes)
- **Step 4**: Connect via Identity 14 (the unitary bridge $V: H_{CCM} \to H_R$) to show the framework's $L̂$ plays the role of CCM's $D_N$ asymptotically
- **Step 5**: Feed into Layer 2's ITPFI entry point (the framework already uses ITPFI for the CBB system)

Risk: Identity 14 is an isomorphism between CCM side and BC side — so using it would make the framework ROUTE THROUGH CCM (dependency preserved). Need to verify Identity 14 can be replaced by an independent construction. Probability: HIGH IF Identity 14 replacement exists; UNKNOWN otherwise.

**If Wave 1 returns shapes DIFFERENT from Alt-1/2/3, the strategy is miscalibrated and runner re-plans.**

---

## 6. What NOT to try (kill list, inherited + anticipated)

**Inherited from H4 run:**
- **K-1 through K-7**: CCM → YM port errors, spectral action traps, etc. These are H4-specific but the PATTERNS (external-source-inconsistency, category-substitution-error, shortcut-through-perturbative-matching) apply. Author self-suspicion should test for each pattern.
- **K-8 (transseries-reads-$C_N$ trap)**: structural-conflation pattern. For RH, the analog warning: do NOT conflate "Riemann-zero ambiguity magnitude" with "specific Riemann-zero values" if anyone tries a transseries-style route.

**Anticipated for RH-specific work:**
- **K-RH-A (pre-registered)**: Do NOT attempt to "prove CCM's Theorems 4.2, 5.10 ourselves" in this Phase 1 run — that's EXCISE mode and is scoped for Phase 2. If an Author finds themselves reconstructing CCM's specific proof, they have drifted out of BYPASS mode into EXCISE mode. Flag and STOP — return to the BYPASS framing.
- **K-RH-B (pre-registered)**: Do NOT claim bypass success if the alternative construction SECRETLY ROUTES THROUGH CCM (e.g., via Identity 14 as in Alt-3 risk analysis). The bypass must produce Layer-1-inputs for Layer 2 WITHOUT requiring CCM as a logical antecedent. Check: can the Author state the alternative Layer 1 construction using only references that do NOT cite CCM 2025 or CCM precursors (Connes-Consani 2016, Connes-Consani 2023)?

Authors add to §F in real-time as new kills emerge.

---

## 7. Load-bearing files to read

| Priority | File | Why |
|:--|:--|:--|
| 1 (MUST) | `solutions-with-prize/paper13-rh/preprint/00-proof-skeleton.md` | The 6-layer chain + Layer 1 description |
| 2 (MUST) | `solutions-with-prize/paper13-rh/preprint/sections-01-05.md` | Setup, BC algebra, GNS, Meyer distributional, CCM interface |
| 3 (MUST) | `solutions-with-prize/paper13-rh/preprint/sections-06-10.md` | CCM operators, ITPFI factorization, Bögli compactness, Hurwitz |
| 4 (MUST) | `solutions-with-prize/paper13-rh/preprint/PROOF-CHAIN.md` | The proof-chain summary file |
| 5 (HIGH) | `solutions-with-prize/paper13-rh/strategy/28-all-gaps-closed.md` | The closing artifact + Layer status |
| 6 (HIGH) | `solutions-with-prize/paper13-rh/strategy/11-ccm-itpfi-programme.md` + `12-ccm-itpfi-current-state.md` | CCM programme state history |
| 7 (HIGH) | `solutions-with-prize/paper13-rh/strategy/05-literature-leads.md` | Alternative spectral-triple candidates; the literature survey |
| 8 (HIGH) | `solutions-with-prize/paper13-rh/strategy/02-where-we-stand.md` + `15-final-state-rh.md` | Where the programme converged and why CCM became the foundation |
| 9 (HIGH) | `online-researcher-adversarial/capacitor/correspondence-table-v1.md` (post-H4 update) | The capacitor with LANG↔QFT PROVED, MICRO↔QFT framework, etc. |
| 10 (MED) | `solutions-with-prize/paper08-yang-mills/h4-capacitor-bypass/synthesis/wave1-synthesis.md` | H4 run's synthesis for pattern-learning (Author format compliance, coordination insights) |
| 11 (MED) | `solutions-with-prize/paper08-yang-mills/h4-capacitor-bypass/capacitor/updates/wave1-cell-fills.md` | 5 new cells + K-8 from H4 run |
| 12 (MED) | `integers/paper12-cbb-system/27-anchor-document.md` | CBB system 5-axiom definition (Alt-3 candidate) |
| 13 (MED) | `integers/paper12-cbb-system/research/214-the-method-six-patterns.md` | Six Patterns method (Always-include) |
| 14 (LOW) | `solutions-with-prize/paper13-rh/strategy/10-state-after-18-kills.md` | Prior kill list — none are bypass kills but pattern-useful |

**Plus (runtime)** — primary-source verification for any CCM alternatives proposed. If an Author cites "Bost-Connes 1995" or "Connes-Marcolli 2008", they MUST fetch the paper via WebFetch or read from `solutions-with-prize/paper13-rh/math-referee/` cached PDFs if available, and produce verbatim supporting quotes.

---

## 8. Time budget and exit conditions

**Hard budget:** 4 hours of wall-clock runtime OR 3-4 full waves (Wave 0 + dispatch/collect cycle ×3), whichever comes first.

**Exit conditions (check at every cycle-close):**

1. **BYPASS FOUND** — compound bypass produces a Layer-1-replacement that:
   - Delivers items 1-4 from §2 (self-adjoint $D_N$ family, Riemann-zero eigenvalue limit, $H^1$ bounds, KMS_1 compatibility)
   - Does not logically depend on CCM 2025 or precursors (verified by K-RH-B check)
   - Survives Critic adversarial pass for every step
   - Computational verification at mp.dps ≥ 50 where numerical content exists
   
   → **RH CCM-UNCONDITIONAL.** Paper 13 Layer 1 has an alternative foundation. Phase 2's Tier 1 CCM verification becomes optional. Update capacitor with new filled cells. Cascade-note the finding to `solutions-with-prize/paper13-rh/preprint/00-proof-skeleton.md` for the next preprint revision.

2. **PARTIAL BYPASS** — a cell fills with a rigorous transposition recipe that COULD become a bypass but requires additional steps (typical: a valid alternative but it matches CCM only asymptotically, or requires an upstream lemma that's not yet proved).
   
   → **CELL CAPTURED + NAMED UNLOCK.** Log the cell + the unlock needed. Continue exploring other cells within budget. Do NOT declare CCM bypassed. Feed into Phase 2 planning.

3. **NEW KILL** — attempted bypass route fails in a new way. Pattern + re-entry gate.
   
   → **KILL LOGGED.** Add to `ccm-bypass/blackboard.md §F`. CASCADE-note to the canonical capacitor's kill list.

4. **BUDGET EXHAUSTED** — time or wave budget hit without bypass.
   
   → **TIER 2 HONEST STALL.** Close at CAPACITOR STRENGTHENED verdict. Every Wave 1 Author produced a cell-fill (per §3.3 v2). Phase 2 proceeds with CCM treated as structurally load-bearing — Tier 1 CCM verification becomes the mandatory priority.

5. **STRUCTURAL LOCK UPGRADE** — all priority cells explored, all CONJECTURED-NEGATIVE with clear structural reasons, a cross-node LOCK forms on "Layer 1 bypass is genuinely stuck."
   
   → **LOCK NAMED.** Phase 2 proceeds knowing CCM is load-bearing at a ≥9/10 level (analog to H4 LOCK for YM). Phase 2's Tier 1 CCM verification becomes critical path for the entire Paper 13 programme.

---

## 9. Voice canon (RH-specific)

Inherited from Paper 13 programme:
- *"Every gap closed via operator algebras"*
- *"RH as consistency condition"*
- *"Conditional on CCM"*

New for this run (if successful):
- *"RH unconditional on CCM"*
- *"Layer 1 rerouted via [domain]"*

If no bypass:
- *"CCM is load-bearing"*
- *"The capacitor gained N cells; Paper 13 ships conditional on CCM"*

---

## 10. What success looks like (three tiers)

### Tier 1: BYPASS FOUND (~10-15% probability)
Compound bypass of 3-7 steps through Alt-1 (Langlands-geometric), Alt-2 (OA spectral triple), Alt-3 (framework-native BC), or an unpredicted Wave-1-discovered shape. RH becomes unconditional on CCM. Phase 2 scope reduces dramatically — Tier 1 CCM verification becomes a nice-to-have rather than a ship-blocker.

### Tier 2: CAPACITOR STRENGTHENED (~60-70% probability — TARGET OUTCOME)
RH stays conditional on CCM. Capacitor gains 3-5 new cells in OA↔SPEC, LANG↔QFT (RH-specific application), ANT↔LANG, MICRO↔QFT (RH application), plus the Candidate cell. Kill list grows with RH-specific patterns. Paper 13 ships conditional on CCM via Track 1 (the existing state). Phase 2 proceeds with CCM treated as load-bearing. Fill rate target: 16.3% → 19-20%.

### Tier 3: HONEST STALL CONFIRMED (~15-25% probability)
No cell produces even a PARTIAL bypass. A 9/10 LOCK-level confirmation that Layer 1 is genuinely stuck on CCM — i.e., no other mathematical framework in 2024-2026 literature can produce the required self-adjoint-operator-with-Riemann-zero-eigenvalue structure. Paper 13 ships conditional on CCM with strongest-possible honest-stall documentation. Phase 2's Tier 1 CCM verification becomes the mandatory critical path.

**All three tiers keep Paper 13 shippable.** The only question is whether CCM becomes optional (Tier 1), load-bearing-to-verify (Tier 2), or structurally-locked-in (Tier 3). In all cases the capacitor grows and Phase 2 is informed.

---

## 11. Run mode

**Mode:** `execute` (PCA bypass-hunting — NOT `final-adversarial-pass`, NOT strat-triad; that's Phase 2)

This is a **single-link (Layer 1) bypass attempt** on RH, targeting the CCM external dependency.

**Waves:**

- **Wave 0 (~20 min)**: LOCK introspection (minimal — no prior LOCK exists). Runner writes LOCK-ANATOMY + BYPASS-PREDICTION §K entries. Proceeds to Wave 1.

- **Wave 1 (5 parallel Authors, Opus max for P1-P3, Sonnet max for P4-P5)**:
  - **W1-OA (OA↔SPEC, Opus max)**: Bost-Connes / Connes-Marcolli alternative spectral-triple path (Alt-2)
  - **W1-L (LANG↔QFT, Opus max)**: Gaitsgory-Raskin 2024 toolkit → Layer 1 via Langlands-geometric (Alt-1)
  - **W1-A (ANT↔LANG, Opus max)**: classical Langlands + automorphic L-function approach
  - **W1-MI (MICRO↔QFT, Sonnet max)**: microlocal/AQFT construction of the operator family
  - **W1-C (Candidate cell, Sonnet max)**: Author chooses from capacitor §Candidates (NCG / HOM / ARTOP / cross-product); pure capacitor exploration

  Each Author produces a cell-fill entry regardless of verdict. Expected runtime: ~90 min parallel.

- **Wave 2 (proof expansion + cell-fills, 2-5 agents)**: for each VIABLE Wave 1 verdict, proof Author + Critic. For PARTIAL, Cell-Fill Author. For FAILED, confirm cell-fill completeness.

- **Wave 3 (adversarial pass, 2-5 Critics)**: on any proposed bypass. Each compound-bypass step gets its own Critic. Every step must SURVIVE for Tier 1.

**Output directory:** `solutions-with-prize/paper13-rh/ccm-bypass/` (sibling pattern like `solutions-with-prize/paper08-yang-mills/h4-capacitor-bypass/`). Do NOT write to existing `solutions-with-prize/paper13-rh/preprint/` or `solutions-with-prize/paper13-rh/strategy/` files. CASCADE-notes to `preprint/00-proof-skeleton.md` are allowed via explicit CASCADE entries, not blackboard bootstrap.

**Blackboard:** create fresh at `${output-directory}/BLACKBOARD.md`.

**Chain state:** inherit from `solutions-with-prize/paper13-rh/preprint/00-proof-skeleton.md` (Layer statuses). Only Layer 1 is in play for this run.

**Pre-flight check (before Wave 0)**: the capacitor must be at v2 state with H4 Wave 1 updates merged (5 new Tier 1 cells + K-8). If not merged → runner merges first, or uses `h4-capacitor-bypass/capacitor/updates/wave1-cell-fills.md` as an override supplement.

---

## 12. Operating discipline

- **Autonomous**: run cycles without pausing. No "should I continue?" questions.
- **Capacitor-first**: Tier 2 is the target. Tier 1 is the bonus. Every Author produces a durable cell-fill regardless of verdict.
- **BYPASS ≠ EXCISE**: stay in BYPASS framing. If an Author starts reconstructing CCM's specific proof (EXCISE mode), flag (K-RH-A) and reset to BYPASS framing.
- **No secret CCM dependencies**: every proposed alternative must pass the K-RH-B check (can it be stated without citing CCM 2025 or precursors?).
- **Budget-aware**: check time + wave budget at every cycle-close. Exit cleanly at budget.
- **Self-healing**: patch bundle issues in place per ORA v8 §14.10.
- **Honest-first**: CCM being load-bearing is a real finding worth naming. Don't force a weak bypass just to avoid Tier 2.

---

## 13. The single paragraph for the next runner

You are attempting a BYPASS of RH's Layer 1 dependency on CCM 2025, with a 4-hour budget and a clearly time-boxed exit. This is Phase 1 reconnaissance before Phase 2's full strat-triad + Tier 1 CCM verification. No prior LOCK exists — CCM bypass has not been attempted. Wave 0 writes a minimal LOCK-ANATOMY (documenting the absence of prior attempts) + BYPASS-PREDICTION (pre-registering Alt-1/2/3 shapes). Wave 1 dispatches 5 parallel Authors: OA↔SPEC (Bost-Connes alternative spectral triple), LANG↔QFT (Gaitsgory-Raskin 2024 toolkit), ANT↔LANG (classical Langlands), MICRO↔QFT (microlocal operator construction), and a Candidate cell (Author pick). Each Author produces a durable capacitor cell-fill regardless of verdict. Expected compound bypasses: 3-7 steps through 2-4 capacitor cells. If a bypass lands → RH unconditional on CCM. If not → capacitor grows, Phase 2 proceeds with CCM as load-bearing. Tier 2 (capacitor gains, ~60-70%) is the TARGET; Tier 1 (bypass found, ~10-15%) is the bonus. The wall is CCM. The capacitor is the map of potential alternative foundations. Walk the map, test each door, name what you find.

---

*Tier 1 unconditionalizes RH. Tier 2 builds the framework. Tier 3 names the LOCK. All three ship Paper 13 via Track 1. No wasted run.*

*Deliverable v1: 2026-04-13. Phase 1 of RH strengthening programme. G Six and Claude Opus 4.6.*
