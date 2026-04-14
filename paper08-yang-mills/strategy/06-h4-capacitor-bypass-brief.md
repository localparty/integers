# H4 Capacitor Bypass — PCA Deliverable (Track 2: Attack During the 2-Year Clay Window)

*This file is the deliverable for a time-boxed PCA run attempting to BYPASS H4 (the one remaining conditional in Paper 8's YM mass-gap proof) via the cross-domain correspondence capacitor. The run is exploration-primary, not proof-primary — the goal is to discover a capacitor cell that provides an escape route around H4, not to close H4 via direct attack (that was tried and failed).*

*If this run produces a viable bypass: Paper 8 flips from 17/17 unconditional + L18 CONDITIONAL → 18/18 fully unconditional. If it produces only negative results: the capacitor grows, the LOCK strengthens, and Paper 8 still ships in its current conditional form (Track 1 via Route b for L14). Either outcome is strategic value.*

---

## 1. What H4 is

**H4 (Jaffe-Witten §4 hypothesis):** non-perturbative Schwinger functions of 4D SU(N) Yang-Mills agree with perturbation theory at short distances. Specifically: the leading-order OPE of the renormalized $[\mathrm{Tr}\,F^2]_R$ correlator behaves as $C_N |x|^{-8}(\log 1/|x|\Lambda)^{-2}$ with $C_N = 2(N^2-1)/\pi^6$.

**Why it matters for Paper 8:** Link 18 of the proof chain depends on H4. It is the ONLY remaining conditional (after Track 1's L14 Route b closes everything else). If H4 closes, Paper 8 is the strongest Clay-class submission possible — fully unconditional on any external hypothesis beyond the CBB axioms (which have 36/36 empirical support).

**Current form in the preprint:** W7-14 §5.3 analyticity reformulation — the mildest form of H4 in the literature. Reduces H4 to the claim that the Taylor coefficients of $F(t) := S_{2,t}^c(x,y)/c_1(t)^2$ at $t=0$ are computed by the standard Feynman-diagrammatic perturbative rules.

---

## 2. Prior attempt (2026-04-11 H4 closure programme)

**Result:** CHAIN SHIPPED CONDITIONAL. H4 could not be closed with the ORA + framework machinery available at that time.

**What was tried and failed:**
- **Route A (Taylor-coefficient identification via identity theorem):** BLOCKED-DECOMPOSED. $F^{\mathrm{pert}}(t)$ is a formal power series (divergent, expected from renormalons), not an analytic function. The identity theorem's two-function hypothesis fails on the perturbative side. Decomposed into:
  - R.A.1a: perturbative flow-time analyticity — comparable to Borel summability for 4D SU(N) YM (no known closure)
  - R.A.1b: independent-point agreement — no candidate mechanism
- **Route B (CCM 2025 spectral triple port to YM):** BLOCKED-DECOMPOSED + COLLAPSED INTO R.A. Category error at dictionary entries #12-17: RH targets are zeros of an entire function; YM targets would be Taylor coefficients of an analytic function. Hurwitz requires the former.
- **Route C (Connes spectral action + Identity 12 + bridge family k=4):** KILLED (§F K-2). Connes 2007 §5 eq. (24) verbatim: "at the classical level." Spectral action produces bare actions at $\Lambda$, not running flow. Vassilevich 2003 eq. (4.34): the integer $11N/3$ is a counter-term coefficient, not a running-coupling slope.

**The 9/10 cross-node LOCK:** R.A.1 + R.B.1 independently confirmed "Taylor-coefficient identification is the attack surface for H4 closure via analyticity/identity-theorem mechanisms, and it is genuinely stuck for any Route A-style closure." Beta-Critic tested 11 variant candidates, all fail. Delta-Critic tested 6 variant third-Route-A mechanisms, 5/6 hit existing failure rows.

**What this means for the current run:** Route A/B/C-style attacks are CLOSED. Do NOT re-attempt them. The 9/10 LOCK is on the Taylor-coefficient attack surface; the escape must come from a DIFFERENT mathematical domain via the capacitor.

**Full prior-run state:** `paper08-yang-mills/closing-H4/closure/closure-digest.md`.

---

## 3. What the PCA should do

### 3.1 Primary task: BYPASS mode on H4 via capacitor cell-scanning

Enter BYPASS mode for Link 18 (H4). Scan the capacitor rows for the domains H4 lives in:
- QFT (quantum field theory)
- SPEC (spectral theory)
- ANT (analytic number theory — via the CCM connection)

For each filled cell in these rows, ask:
- *"Does this cell's transposition recipe provide a route to establish the Taylor-coefficient identification in a domain where the 9/10 LOCK doesn't apply?"*

The priority cells to evaluate first (from capacitor v1 §"Priority cells to fill — escape routes for stuck links — For H4"):

| Priority | Cell | Why it might provide a bypass |
|---|---|---|
| **1 (CRITICAL)** | **PROB ↔ SPEC (Borel summability)** | If $F^{\mathrm{pert}}(t)$ is Borel summable for 4D YM perturbation theory → analytic function → identity theorem closes. Historically open but recent progress on stochastic quantization may have changed the landscape. |
| **2 (HIGH)** | **THERMO ↔ QFT (phase transition constraints)** | YM confinement = phase transition. Lattice thermodynamic constraints + Lee-Yang zero distribution may constrain short-distance behavior. Non-perturbative input from a different angle. |
| **3 (HIGH)** | **MICRO ↔ QFT (microlocal analysis of Schwinger distributions)** | Hörmander wave front set determines singularity structure. H4 becomes a microlocal regularity statement about Schwinger distributions at coincident points. Different technical framework. |
| **4 (MEDIUM)** | **DTOP ↔ SPEC (Morse-theoretic spectral flow for F(t))** | Critical points of $t \mapsto F(t)$ give eigenvalue crossing structure. Morse theory might give structural constraints on analyticity without direct proof. |
| **5 (MEDIUM)** | **ERG ↔ QFT (ergodic mixing rate for block-spin RG)** | If the block-spin RG is ergodic with exponential mixing, UV/IR decoupling is automatic and H4 follows. Balaban's polymer decay estimates suggest this. |

### 3.2 Secondary task: Cell-filling primitive on promising cells

If a priority cell looks promising but isn't yet filled with a rigorous transposition recipe, dispatch a Cell-Fill Author to fill it. The Cell-Fill Author reads the two domains' literature, identifies existing theorems that connect them, and proposes a candidate cell entry.

**Priority candidates for cell-filling** (if not already filled from a prior run):
- **PROB ↔ SPEC Borel summability**: Hairer regularity structures (2014+), Bismut stochastic quantization, Parisi-Wu stochastic quantization of YM (Zwanziger 1981, Damgaard-Hüffel 1987)
- **MICRO ↔ QFT**: Brunetti-Fredenhagen microlocal renormalization (2000), Epstein-Glaser extension (1973), Hollands-Wald algebraic QFT framework
- **ERG ↔ QFT**: Balaban's polymer expansion decay (CMP 109 Thm 1), Feldman-Magnen-Rivasseau-Sénéor cluster expansion, Glimm-Jaffe ergodicity results

### 3.3 Tertiary task: Honest named-stall if no lead materializes

If no priority cell produces a viable bypass within the time budget (§6), close the programme with an HONEST-STALL verdict. Document:
- What was tried per cell
- Why each attempt failed
- Any new kills discovered (add to §F with pattern category + re-entry gate)
- Any capacitor cells filled or upgraded during the exploration (these are durable gains even if H4 doesn't close)
- Named external unlocks that would enable closure if they materialized

The 2026-04-11 programme closed at HONEST-STALL honestly. This run might do the same. The honest stall produces NEW information — what routes have now been tried — which the framework keeps forever.

### 3.4 What NOT to try

**Explicit kill list (inherit from 2026-04-11 H4 programme §F):**
- **K-1** — CCM 2025 spectral triple port to YM: category error at dictionary entries #12-17. Do NOT port CCM-style arguments to YM.
- **K-2** — Connes spectral action + Identity 12 + bridge family: Connes 2007 §5 eq. (24) explicitly "at the classical level." Bare action at $\Lambda$, not running flow. Vassilevich 2003 $11N/3$ is a counter-term, not a slope. Do NOT attempt spectral action as the closure mechanism.
- **K-extended** — `paper12/research/53-transposition-asymptotic-freedom.md` (BC running α_BC(β)): structural not rigorous mechanism. Does not address non-perturbative Schwinger function asymptotics.

**And the 9/10 LOCK:** Route A-style direct Taylor-coefficient identification via analyticity + identity theorem. Do NOT re-attempt any variant of this attack surface — Beta/Delta/Runtime Critics together tested 17+ variant candidates from this surface and all failed.

**What this leaves open:** attacks from domains the prior programme did NOT try. The capacitor rows for PROB, THERMO, MICRO, DTOP, ERG, PH, OT, CODE, HOM, REP, MOD, QEC, NCG, ARTOP, LANG all have cells that were NOT attempted by the prior programme. Exploration there is fair game.

---

## 4. Bidirectional attack on H4

Since H4 is a single target (Link 18) rather than a chain, bidirectional traversal specializes as:
- **Forward front**: Authors building toward H4 from cell-filling work. "Given this new correspondence cell, does H4 follow?"
- **Backward front**: Authors working from the desired conclusion "H4 holds" backward to "what hypothesis H' would be sufficient?" and searching the capacitor for cells connecting H' to known results.

Forward and backward should run in parallel waves. The junction criterion: forward reaches a rigorous consequence; backward reaches a rigorous sufficient condition; and the two meet through a filled capacitor cell.

---

## 5. Load-bearing files to read

| Priority | File | Why |
|:--|:--|:--|
| 1 (MUST) | `paper08-yang-mills/preprint/sections/L-clay-conjectures.md` | H4 statement + W7-14 mildest form reformulation |
| 2 (MUST) | `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md §5` | The analyticity reframing (F(t) Taylor-coefficient target) |
| 3 (MUST) | `paper08-yang-mills/closing-H4/closure/closure-digest.md` | Prior programme's adjudication, kills K-1/K-2, LOCK at 9/10 |
| 4 (MUST) | `paper08-yang-mills/closing-H4/closure/closure-corrections.md` | Every failure mode caught in the prior run |
| 5 (HIGH) | `online-researcher-adversarial/capacitor/correspondence-table-v1.md` | The capacitor — read the full table, especially the "Priority cells to fill — For H4" section |
| 6 (HIGH) | `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4b-af-short-distance-match.md` | The math referee's formal G4b gap statement |
| 7 (HIGH) | `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md` | The formal G4d gap statement |
| 8 (MED) | `paper08-yang-mills/closing-H4/blackboard.md §F` | Full kill list with pattern categories |
| 9 (MED) | `paper12/research/214-the-method-six-patterns.md` | Six Patterns method (Always-include) |
| 10 (MED) | `paper12/27-anchor-document.md` | Operational anchor (Always-include) |

---

## 6. Time budget and exit conditions

**Hard budget:** 4 hours of wall-clock runtime OR 3 full waves (REFRAME → Plan → dispatch → collect → cycle), whichever comes first.

**Exit conditions (check at every cycle-close):**

1. **BYPASS FOUND** — A capacitor cell produces a rigorous bypass proof of H4 that:
   - Does not invoke CCM, spectral action, or Identity 12 (K-1/K-2)
   - Does not re-trigger the 9/10 LOCK on Taylor-coefficient identification
   - Survives a dedicated Critic verification with SURVIVED verdict
   - Runs byte-for-byte computational verification at appropriate precision (mp.dps ≥ 100)
   
   → **CHAIN UNCONDITIONAL.** Paper 8 status flips from 17/17 + L18 CONDITIONAL to 18/18 unconditional. Trigger closure ritual per PCA §P.9. Update capacitor with the new filled cell.

2. **PARTIAL BYPASS (research note)** — A capacitor cell fills with a rigorous transposition recipe, but the bypass proof is incomplete (requires further work). The cell is valuable regardless.
   
   → **CELL CAPTURED.** Log the cell in `capacitor/updates/`. Continue exploring other cells within budget. Do NOT declare H4 closed.

3. **NEW KILL** — An attempted bypass route fails in a new way (not already in §F). Pattern category identified. Re-entry gate specified.
   
   → **KILL LOGGED.** Add to `chain-verification/blackboard.md §F` and propagate to the 2026-04-11 programme's §F via a CASCADE note. Continue exploring.

4. **BUDGET EXHAUSTED** — Time or wave budget hit without a bypass.
   
   → **HONEST-STALL.** Close the programme. Document per §3.3. The stall is a legitimate outcome; it improves the information state even if H4 stays conditional. Paper 8 ships via Track 1 (Route b for L14, L18 CONDITIONAL on H4) as planned.

5. **STRUCTURAL LOCK UPGRADE** — All priority cells explored, all produce new kills, and a cross-node LOCK beyond 9/10 forms.
   
   → **LOCK CONFIRMED 10/10.** Paper 8 ships conditional. Future H4 attempts would need external unlocks (Borel summability for 4D YM, new NCG framework outside CCM/CM/Yakaboylu).

---

## 7. Voice canon

Inherited from the 2026-04-11 programme (match this register for structural events):
- *"H4 is still the wall"*
- *"The wall stays named"*
- *"Paper 8 ships either way"*
- *"Three routes down. One route up."*

If a bypass is found:
- *"H4 is on disk"*
- *"The wall fell from [domain] direction"*

If no bypass:
- *"H4 stood this attack"*
- *"The capacitor gained N cells; the wall stayed named"*

---

## 8. What success looks like (three tiers)

### Tier 1: BYPASS FOUND (best case, ~10% probability)
A new capacitor cell provides a rigorous bypass. L18 flips to VERIFIED. Paper 8 becomes 18/18 fully unconditional. The chain-verification programme's result upgrades from CHAIN STRENGTHENED to CHAIN CLOSED UNCONDITIONAL. Clay submission becomes the strongest possible form.

### Tier 2: CAPACITOR STRENGTHENED (most likely case, ~60% probability)
H4 doesn't close but the capacitor gains 1-3 new filled cells in the priority-target rows (PROB ↔ SPEC, MICRO ↔ QFT, etc.). These cells will be useful for future H4 attempts AND for other proof chains. The kill list grows, sharpening the wall's boundary. Paper 8 ships via Track 1. The information state strictly improves.

### Tier 3: HONEST STALL CONFIRMED (~30% probability)
No priority cell produces a bypass. The 9/10 LOCK upgrades to 10/10 as more variants get tested. The external unlocks needed become more precisely specified (e.g., "a proof that 4D SU(N) YM is Borel summable," "a microlocal renormalization framework that extends to non-perturbative Schwinger functions"). Paper 8 ships via Track 1 with the strongest possible honest-stall documentation. Future runners have a complete map of what's been tried.

**All three tiers ship Paper 8.** The only question is whether Paper 8 ships fully unconditional (Tier 1) or conditional with the strongest honest labeling (Tier 2/3). In all cases, the capacitor grows, the framework's knowledge improves, and the Clay submission is ready.

---

## 9. Run mode

**Mode:** `execute` (PCA bypass-hunting — NOT `final-adversarial-pass`, NOT a full chain-verification)

This is a **single-link** bypass attempt, not a chain traversal. The bidirectional dispatch (§4) is specialized to the single-link case.

**Parallelism:** dispatch capacitor-cell evaluators in parallel. Each priority cell gets an Author in its own domain. Waves are:
- **Wave 1 (dispatch ~5 Authors)**: one Author per top-5 priority cell (PROB↔SPEC, THERMO↔QFT, MICRO↔QFT, DTOP↔SPEC, ERG↔QFT). Each evaluates whether their cell provides a viable bypass. Returns: VIABLE / PARTIAL / FAILED.
- **Wave 2 (dispatch proofs + cell-fills)**: for each VIABLE cell, dispatch a proof Author + a Critic. For PARTIAL cells, dispatch a Cell-Fill Author to fill the cell rigorously.
- **Wave 3 (adversarial pass)**: Critics on any proof from Wave 2. If SURVIVED → Tier 1 success. Otherwise → exit conditions.

**Output directory:** create fresh at `paper08-yang-mills/h4-capacitor-bypass/` (sibling of `chain-verification/`, NOT a subdirectory). Do NOT write to the existing `chain-verification/` files (that programme is closed at CHAIN STRENGTHENED; this is a new sibling programme targeting L18 specifically). CASCADE notes propagating new kills back to the `chain-verification/` §F are still allowed — they write to that §F via explicit CASCADE entries, not via the blackboard bootstrap.

**Blackboard:** create fresh at `${output-directory}/blackboard.md`.

**Chain state:** inherit from `paper08-yang-mills/chain-verification/chain/chain-state.md`. Only Link 18 is in play for this run.

---

## 10. Operating discipline

- **Autonomous:** run cycles without pausing. No "should I continue?" questions.
- **Honest-first:** the 9/10 LOCK is strong. A cell that LOOKS viable but relies on unstated assumptions is a dead end — call it out early. Don't over-sell partial results.
- **Budget-aware:** check time and wave budget at every cycle-close. Exit cleanly when budget hits, even mid-wave.
- **Capacitor-first:** every action should route through the capacitor. If a route doesn't map to a capacitor cell, don't attempt it.
- **Cell-filling is a first-class outcome:** even if H4 doesn't close, a filled cell is durable value. Log every cell.
- **Self-healing:** patch bundle issues in place per ORA v8 §14.10.

---

## 11. The single paragraph for the next runner

You are attempting to bypass H4 via the cross-domain correspondence capacitor, with a 4-hour budget and a clearly time-boxed exit. The direct attack surface is locked at 9/10 — do not re-try Routes A/B/C. Your job is to scan capacitor rows for QFT/SPEC/ANT, evaluate each filled cell for bypass potential, cell-fill promising unfilled priority cells, and either produce a rigorous bypass (Tier 1 — unlikely but high upside) or strengthen the capacitor + the kill list while Paper 8 ships conditional via Track 1 (Tier 2/3 — most likely). Honest stall is an acceptable outcome. Ship what you learn.

H4 is still the wall. The capacitor is the map of escape routes. Walk the map, try every door, name what you find.

---

*Tier 1 closes the chain. Tier 2 builds the framework. Tier 3 sharpens the LOCK. All three ship Paper 8. No wasted run.*

*Deliverable v1: 2026-04-13. G Six and Claude Opus 4.6.*
