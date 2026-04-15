# H4 Capacitor Bypass — PCA Deliverable (Track 2: Attack During the 2-Year Clay Window)

*This file is the deliverable for a time-boxed PCA run attempting to GROW the H4-adjacent capacitor region to Millennium-submission grade. A capacitor bypass of H4 is the bonus outcome if a cell closes the category-shift path. The primary deliverable is durable cell-fills: every Wave 1 Author produces a capacitor entry regardless of whether H4 closes.*

*Strategic frame (v3 reframe): the capacitor — 40 cells, cross-domain transposition recipes, proven load-bearing for RH / YM / BSD / PvNP — IS the Millennium deliverable, not Paper 8 standalone. The v3 research calibration found no competitor: no 2023-2026 paper attempts non-perturbative OPE for 4D gauge theory; no one is attacking H4 directly; the one recent "breakthrough" (arXiv:2506.00284) was withdrawn by arXiv admin as not research-quality. You are growing the capacitor alone in the field.*

*If this run produces a viable bypass: Paper 8 flips from 17/17 unconditional + L18 CONDITIONAL → 18/18 fully unconditional (Tier 1, ~7-12%). If it produces only negative results on H4 closure: the capacitor grows by 3-5 cells (Tier 2, ~65-75% — **this is the TARGET outcome, not a fallback**), the LOCK strengthens, Paper 8 ships via Track 1 conditional, and the Millennium deliverable gains durable structure. All outcomes ship.*

*v3 (2026-04-13): capacitor-first reframe + deeper literature calibration. See §1 Millennium-deliverable framing (Tier 2 is target, not fallback), §3.1 v3-reprioritized with 5-Author Wave 1 (MICRO + ERG + 2×resurgence + LANG candidate cell), §3.4 K-7 withdrawn-crank kill + K-5 strengthened (Nissim lattice-only), §8 Tier 1 recalibrated 7-12%. v2 history retained: §2.1 LOCK-scope clarification (load-bearing), §3.0 category-shift framing (deep), §3.0.5 Wave 0 discipline, §3.0.6 compound-bypass pre-registration.*

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

**Full prior-run state:** `solutions-with-prize/paper08-yang-mills/closing-H4/closure/closure-digest.md`.

---

## 2.1 LOCK-scope clarification (LOAD-BEARING — read this before any dispatch)

**The 9/10 LOCK is NARROWER than "H4 is closed off from attack." Read its exact scope carefully.**

### What the LOCK binds

The LOCK is specifically on **Taylor-coefficient identification via identity theorem on F(t)** — the single attack surface where:
- $F(t)$ is treated as an analytic function of flow time
- $F^{\mathrm{pert}}(t)$ is compared to it at the Taylor-coefficient level
- The identity theorem is the closure mechanism

Any Route A-style attack that instantiates these three ingredients hits the LOCK. 17+ variant candidates from this surface have been tested and all failed.

### What the LOCK does NOT bind

The LOCK does NOT automatically extend to:

1. **"F(t) analytic as a function" attacks via Borel summability in complex t.** IR renormalons kill the $\mathbb{R}_+$ direction of Borel summation (this is known). But lateral Borel summation in complex flow-time directions is unexplored. The LOCK was tested on the identity-theorem surface, not on the Borel-lateral surface.

2. **"H4 as a wave-front set statement" via microlocal analysis of the Schwinger distribution at coincident points.** This is a **category shift** — H4 restated as a regularity claim about a distribution, not as Taylor-coefficient identification of a function. Different mathematical object. The LOCK doesn't follow the object across the category boundary.

3. **"H4 via axiomatic OPE construction" in the Hollands-Wald / Dappiaggi framework.** Another category shift — H4 restated as an operator-product-expansion convergence statement in an algebraic QFT framework, not as perturbative vs. non-perturbative Taylor-coefficient matching.

### The load-bearing implication

**Do NOT pre-kill microlocal / axiomatic-OPE / lateral-Borel work as "LOCK-blocked."** They are NOT LOCK-blocked. They are in different mathematical categories from the attack surface the LOCK binds.

Without this clarification, Wave 1 Authors will false-positive-kill themselves on anything that touches distributions or Schwinger-function regularity. **The LOCK binds one attack surface; the bypass path works by shifting category, not by finding another path through the same surface.** See §3.0 for the category-shift framing.

**Wave 0 discipline (§3.0.5) MANDATES a LOCK-ANATOMY entry before Wave 1 dispatch.** Do not skip it.

---

## 3. What the PCA should do

### 3.0 The bypass strategy: category shift, not transposition within a category

Most transpositions through the capacitor work by restating a problem in a different domain's language while keeping it in the same mathematical category. For H4, that approach fails — Route B in the 2026-04-11 programme attempted exactly that (CCM-to-YM transposition) and collapsed back onto Route A because it was still Taylor-coefficient identification, just spoken in spectral-triple dialect.

**The viable path is a category shift.** Restate H4 in a different mathematical category altogether — not as "Taylor-coefficient identification of F(t)," but as:

- **A wave-front set statement** (microlocal): "the Schwinger distribution $S_2^{\mathrm{ren}}(x, y)$ has a prescribed singular structure at $x = y$ determined by AF scaling." This is a claim about a distribution, not about a function. The identity theorem doesn't apply; different machinery does (propagation of singularities, Hörmander's theorem).

- **An operator-product-expansion convergence statement** (axiomatic QFT): "the non-perturbative OPE $[\mathrm{Tr}\,F^2]_R(x) [\mathrm{Tr}\,F^2]_R(y) = C^{\mathbb{1}}(x-y) \mathbb{1} + \text{subleading}$ has convergent expansion with the specified leading coefficient." This is a claim about an algebraic structure, not about perturbative matching.

- **A regularity claim in an ergodic construction** (if a non-perturbative Schwinger function exists via Langevin / cluster expansion, its UV singular structure can be analyzed directly from the construction).

Each of these is a different mathematical object making the same physical claim. The 9/10 LOCK binds the function-identification object; the distribution-regularity and OPE-convergence objects are open.

**The compound bypass**: a successful closure will typically walk through MULTIPLE capacitor cells, each closing a sub-step, composing to reach H4. Expect 3-7 steps, not 1. See §3.0.6 for compound-bypass pre-registration.

### 3.0.5 Wave 0 — LOCK introspection (MANDATORY before Wave 1 dispatches)

Before any Wave 1 Author spawn, the runner executes a Wave 0 step:

1. **Read** `solutions-with-prize/paper08-yang-mills/closing-H4/closure/closure-digest.md` §LOCK end-to-end.
2. **Write** a §K entry of type `LOCK-ANATOMY` stating:
   - What claim the 9/10 LOCK binds (exact scope: Taylor-coefficient identification via identity theorem on F(t))
   - What the LOCK does NOT bind (microlocal / axiomatic OPE / lateral Borel / ergodic construction restatements — the category-shift paths)
   - Which 2026-04-11 variants were LOCK-rejected and why (quick trace through Beta/Delta critic findings)
   - Which approaches in THIS run are LOCK-adjacent (the 17+ tested variants) and must NOT be re-attempted
3. **Dispatch a LOCK-ANATOMY Critic** (Sonnet, max effort) whose sole job is to verify the `LOCK-ANATOMY` entry matches the closure-digest's actual LOCK scope. Verdict: SURVIVED / WEAKENED.
4. **If SURVIVED**: Wave 1 proceeds. Pin the `LOCK-ANATOMY` entry in §C current bottleneck so every subsequent agent reads it.
5. **If WEAKENED**: refine the entry and re-verify. Do NOT dispatch Wave 1 until the LOCK-anatomy is validated.

Cost: ~30 minutes runner + ~10 minutes Critic. This is insurance against cascade-kills in Wave 1. **Mandatory — do not skip.**

### 3.0.6 Compound-bypass pre-registration

Before Wave 1 dispatches, the runner writes a §K entry of type `BYPASS-PREDICTION` stating the EXPECTED shape of a viable bypass. Example form:

> *"Expected compound bypass: 3-5 steps routing through MICRO↔QFT (wave-front-set restatement of H4) + non-perturbative AQFT Schwinger distribution existence + possibly ERG↔QFT (Nissim 2025 Langevin construction as the non-perturbative object) → axiomatic-OPE convergence matching the AF prediction. If Wave 1 Authors don't converge on a shape like this, the strategy is wrong and we re-plan."*

This is a pre-registration. Its purpose is to let the runner recognize calibration error early. If Wave 1 returns with a DIFFERENT shape (say, a direct spectral-gap argument instead of a multi-step category-shift), that's information: maybe the strategy was miscalibrated and the true path is something the brief didn't anticipate. Either way, the runner has a reference shape to compare against.

Write the `BYPASS-PREDICTION` before Wave 1 dispatch. Check Wave 1 outputs against it at synthesis time. Adjust the strategy explicitly if they diverge.

### 3.1 Primary task: BYPASS mode on H4 via capacitor cell-scanning

Enter BYPASS mode for Link 18 (H4). Scan the capacitor rows for the domains H4 lives in:
- QFT (quantum field theory)
- SPEC (spectral theory)
- ANT (analytic number theory — via the CCM connection)

For each filled cell in these rows, ask:
- *"Does this cell's transposition recipe provide a route to establish the H4 target through a CATEGORY SHIFT — restating H4 as a distribution-theoretic, axiomatic-OPE, microlocal, or ergodic statement — rather than as Taylor-coefficient identification?"*

The **v3-reprioritized** priority cells (v2 ordering revised after deeper 2023-2026 calibration sweep + capacitor-first reframe):

| Priority | Cell | Why it might provide a bypass | Live literature |
|---|---|---|---|
| **1 (co-CRITICAL)** | **MICRO↔QFT (microlocal analysis of Schwinger distributions)** | Category shift: H4 as wave-front-set statement for $S_2^{\mathrm{ren}}(x,y)$ at $x=y$. LOCK doesn't bind (different mathematical category). **v3 caveat: framework construction, not ported machinery** — the research calibration found NO 2023-2026 paper attempting non-perturbative OPE for 4D gauge theory. Hollands-Wald 2024 is curved-spacetime OPE (not 4D gauge non-perturbative); BFR Dec 2025 arXiv:2512.14227 §4 non-perturbative framework is explicitly **scalar-only**; Dappiaggi work is 2D spinor + scalar NLS. Your Author is building the framework, not looking it up. Budget and expectations accordingly. | Hollands-Wald arXiv:2312.01096 (Encyclopedia of Math Phys 2nd ed., 2024); BFR arXiv:2512.14227 "Perturbative algebraic QFT and beyond" (Dec 2025 survey — §4 scalar-only, explicitly flags open gauge extension); Bonicelli-Dappiaggi-Rinaldi Ann Henri Poincaré 2023 (scalar NLS); arXiv:2309.16376 MPAG 2024 (Thirring) |
| **1 (co-CRITICAL, v3 PROMOTED from v2 P3)** | **PROB↔SPEC (resurgence / lateral Borel)** | Most live 2024-2026 machinery of the three priority cells. CERN Summer School 2024 resurgence programme (arXiv:2511.15528) + Dunne 2024-2025 lecture series explicitly target continuum-lattice QFT renormalons. IR renormalons kill $\mathbb{R}_+$ Borel (known); **lateral Borel in complex $t$** is unexplored for 4D YM. Resurgent transseries may produce H4 from renormalon cancellation structure without identity-theorem identification — structurally avoids LOCK. | arXiv:2511.15528 (CERN Summer School 2024 Resurgence lectures); Dunne 2024-2025 lecture series; Mariño resurgence review; Chandra-Chevyrev-Hairer-Shen 3D YM-Higgs Inventiones 2024 (arXiv:2201.03487) — 4D beyond regularity-structures reach per Shen Feb/Mar 2025 talks |
| **2 (HIGH)** | **ERG↔QFT (ergodic construction + cluster expansion)** | Nissim Oct 2025 (arXiv:2510.22788, VERIFIED during v3 calibration) establishes U(N) **lattice** YM mass gap via cluster expansion + Langevin. **v3 caveat (K-5 strengthened): lattice-only; continuum limit is a separate open step BEFORE UV OPE extraction.** Cluster expansion at strong coupling is intrinsically IR technique; UV extension would need Balaban-style block-spin (not done by Nissim) or a separate weak-coupling expansion (Magnen-Rivasseau-Sénéor 1993 CMP 155 is state-of-art, IR-cutoff unremoved). Minimum two-step bypass chain: continuum limit → UV short-distance extraction → $C_N$ derivation. | Nissim arXiv:2510.22788 (Oct 2025, VERIFIED lattice-only); Balaban CMP 109 polymer decay; Feldman-Magnen-Rivasseau-Sénéor cluster expansion; Magnen-Rivasseau-Sénéor 1993 CMP 155 (IR-cutoff YM) |
| **3 (v3 NEW — candidate-cell exploration)** | **LANG↔QFT (Kapustin-Witten S-duality)** | Candidate cell outside v1/v2's "For H4" priority list (see capacitor v1 §Candidates). Kapustin-Witten: geometric Langlands = S-duality of N=4 SYM. Electric-magnetic duality may give an H4-equivalent statement on the dual side. **Millennium-grade capacitor work even if H4 doesn't bite:** filling this cell opens LANG↔QFT for all future proof chains (RH, BSD, PvNP benefit). This is the capacitor-first bet — pure cross-domain exploration whose primary deliverable is the cell-fill itself. | Kapustin-Witten "Electric-Magnetic Duality And The Geometric Langlands Program" (2007 arXiv:hep-th/0604151); Frenkel "Lectures on the Langlands Program and Conformal Field Theory"; Witten "More on Gauge Theory and Geometric Langlands" |
| **DROPPED (was v1 P2)** | ~~THERMO↔QFT (phase transition constraints)~~ | v3 calibration confirms v2 drop: no 2023-2026 lead with traction on short-distance OPE structure via thermodynamic routes. Mass gap is IR; H4 is UV. No Wave 1 dispatch. | — |
| **DROPPED (was v1 P4)** | ~~DTOP↔SPEC (Morse-theoretic spectral flow)~~ | v3 calibration confirms v2 drop: Feehan-Maridakis Łojasiewicz-Simon trap (K-4). Structural confusion risk too high for a Wave 1 slot. | — |

### 3.2 Secondary task: Cell-filling primitive on promising cells

If a priority cell looks promising but isn't yet filled with a rigorous transposition recipe, dispatch a Cell-Fill Author to fill it. The Cell-Fill Author reads the two domains' literature, identifies existing theorems that connect them, and proposes a candidate cell entry.

**Priority reading list (2024-2025 literature — UPDATED from v1):**

For **MICRO↔QFT** (Priority 1):
- Hollands-Wald 2024: "Algebraic Quantum Field Theory on Curved Spacetimes" in Encyclopedia of Mathematical Physics (2nd edition)
- arXiv:2512.14227 (Dec 2025): "Perturbative algebraic QFT and beyond" — survey of the 2023-2025 state
- Dappiaggi et al. Ann Henri Poincaré 2023 and Math Phys Anal Geom 2024 on microlocal-to-SPDE ports
- **BOUNDARY REF**: Hollands-Kopper 2011 (arXiv:1105.3375) — pure perturbative OPE convergence. **Do NOT mistake for non-perturbative; see §3.4 K-6.**
- Background: Brunetti-Fredenhagen 2000 microlocal renormalization; Epstein-Glaser 1973 extension of distributions

For **ERG↔QFT** (Priority 2):
- Nissim Oct 2025 arXiv:2510.22788 (U(N) lattice YM mass gap via cluster expansion + Langevin) — **VERIFY arXiv ID exists with this description before Wave 1 dispatch**
- Background: Balaban CMP 109 (polymer expansion decay); Feldman-Magnen-Rivasseau-Sénéor cluster expansion; Glimm-Jaffe ergodicity

For **PROB↔SPEC** (Priority 3, lateral Borel sanity check):
- Chandra-Chevyrev-Hairer-Shen (3D YM SPDE regularity structures)
- Classical lateral Borel summation literature (if any specific to gauge theory)

### 3.3 Tertiary task: Durable cell-fill output even on HONEST-STALL (v2 strengthened)

Every Wave 1 Author, regardless of bypass-viability verdict (VIABLE / PARTIAL / FAILED), writes a cell-fill entry in capacitor v1 format. The entry must contain:

- **Statement** (one-line theorem/functor statement)
- **Mechanism** (2-3 sentences on HOW the correspondence works)
- **Source** (primary reference)
- **Status** (VERIFIED / ESTABLISHED / CONJECTURED / CANDIDATE, including NEGATIVE status: "this cell does NOT provide a bypass for H4 because [reason]")
- **Verification data** (if computational)
- **Load-bearing for** (which proof chain link this cell enables or bypasses)
- **Transposition recipe** (HOW to use this cell — if stuck on H4, what do you do in the other domain?)

Even a FAILED verdict produces a filled cell: the cell's status is then "CONJECTURED-NEGATIVE" with the reason documented. **This converts exploration → durable capacitor growth.**

Net effect: capacitor fill rate goes from 14.5% (v1) → plausibly 17-18% after this run, regardless of whether H4 closes. Every cell filled benefits all future proof chain work (RH, BSD, PvNP, future papers).

**If no priority cell produces a viable bypass within budget** (§6), close the programme with an HONEST-STALL verdict. Document:
- What was tried per cell (verdicts)
- Every Wave 1 cell-fill (successful and unsuccessful)
- Any new kills discovered (add to §F with pattern category + re-entry gate)
- Named external unlocks that would enable closure if they materialized

### 3.4 What NOT to try (v2 extended kill list)

**Inherited from 2026-04-11 H4 programme §F:**

- **K-1** — CCM 2025 spectral triple port to YM: category error at dictionary entries #12-17. Do NOT port CCM-style arguments to YM.
- **K-2** — Connes spectral action + Identity 12 + bridge family: Connes 2007 §5 eq. (24) explicitly "at the classical level." Bare action at $\Lambda$, not running flow. Vassilevich 2003 $11N/3$ is a counter-term, not a slope. Do NOT attempt spectral action as the closure mechanism.
- **K-3-extended** — `integers/paper12-cbb-system/research/53-transposition-asymptotic-freedom.md` (BC running α_BC(β)): structural not rigorous mechanism. Does not address non-perturbative Schwinger function asymptotics.

**And the 9/10 LOCK (scope clarified in §2.1):** Route A-style direct Taylor-coefficient identification via analyticity + identity theorem on F(t). Do NOT re-attempt any variant of this attack surface — Beta/Delta/Runtime Critics together tested 17+ variant candidates from this surface and all failed.

**New in v2 (from research agent 2023-2026 sweep):**

- **K-4 — Feehan-Maridakis Łojasiewicz-Simon trap.** The Feehan-Maridakis analyticity result is analyticity of the Yang-Mills energy functional near critical connections on the space of connections modulo gauge. It is NOT analyticity of the composite-operator two-point-function Taylor coefficients in flow time. **Do NOT conflate.** An Author attempting DTOP↔SPEC via Morse-theoretic spectral flow on connection space will easily make this conflation — it's structurally seductive and mathematically wrong. Pattern: category-substitution-error. Re-entry gate: requires an explicit theorem connecting energy-functional analyticity on connection space to flow-time Taylor coefficients of correlators (no such theorem exists).

- **K-5 — ERG→OPE naive reduction (v3 strengthened).** Balaban / cluster expansion / Nissim 2025 machinery establishes mass gap (IR property) on a **lattice**. **v3 correction of v2's claim**: Nissim arXiv:2510.22788 does NOT take the continuum limit — continuum limit is a separate open step before UV OPE extraction can even begin. So the minimum bypass chain via ERG↔QFT is (a) continuum limit exists, (b) UV short-distance behavior extractable from the continuum construction, (c) where $C_N = 2(N^2-1)/\pi^6$ emerges — three open steps, not one. Mass gap constants are non-perturbative polymer-expansion quantities; the AF coefficient $C_N$ is perturbative by construction. A naive "non-perturbative construction gives H4 for free" argument reduces to perturbative matching at the point where $C_N$ must appear — which is Route-A-adjacent and LOCK-bound. Pattern: shortcut-through-perturbative-matching + continuum-limit-elision. Re-entry gate: requires direct derivation of $C_N$ from non-perturbative constructional quantities without invoking perturbative Feynman rules, AFTER the continuum limit is established.

- **K-6 — Pure perturbative OPE convergence mistake.** Hollands-Kopper 2011 (arXiv:1105.3375) and related work establishes PERTURBATIVE OPE convergence — i.e., convergence of the perturbative expansion of the OPE at each order. This is a significant result but is NOT H4. H4 requires NON-PERTURBATIVE OPE matching: the non-perturbative Schwinger function, not its perturbative expansion, must have the AF short-distance structure. An Author in the MICRO↔QFT direction who produces a Hollands-Kopper-style result and claims it closes H4 has re-hit the LOCK via a subtle path. Pattern: perturbative-level-confusion. Re-entry gate: requires explicit construction of a non-perturbative Schwinger distribution AND a proof that its OPE convergence includes the AF logarithmic correction at the non-perturbative level.

**New in v3 (from deeper 2023-2026 calibration sweep):**

- **K-7 — Withdrawn-crank citation trap.** arXiv:2506.00284 (D.C. Jacobsen, May 2025, "Constructive Proof... SU(3) Yang-Mills") was **withdrawn by arXiv admin in June 2025** as not meeting research-quality standards. The paper still surfaces in search engines and may appear in literature scans as a purported "breakthrough." It is not. Do NOT cite it. Do NOT let any Wave 1 Author treat it as a credible lead. Pattern: discredited-primary-source. Re-entry gate: the paper has been withdrawn; no re-entry possible.

---

## 4. Bidirectional attack on H4

Since H4 is a single target (Link 18) rather than a chain, bidirectional traversal specializes as:
- **Forward front**: Authors building toward H4 from cell-filling work. "Given this new correspondence cell, does H4 follow?"
- **Backward front**: Authors working from the desired conclusion "H4 holds" backward to "what hypothesis H' would be sufficient?" and searching the capacitor for cells connecting H' to known results.

Forward and backward should run in parallel waves. The junction criterion: forward reaches a rigorous consequence; backward reaches a rigorous sufficient condition; and the two meet through a filled capacitor cell — typically via a **compound bypass of 3-7 steps** per §3.0.

---

## 5. Load-bearing files to read

| Priority | File | Why |
|:--|:--|:--|
| 1 (MUST) | `solutions-with-prize/paper08-yang-mills/preprint/sections/L-clay-conjectures.md` | H4 statement + W7-14 mildest form reformulation |
| 2 (MUST) | `solutions-with-prize/paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md §5` | The analyticity reframing (F(t) Taylor-coefficient target) |
| 3 (MUST) | `solutions-with-prize/paper08-yang-mills/closing-H4/closure/closure-digest.md` | Prior programme's adjudication, kills K-1/K-2, LOCK at 9/10 (READ SPECIFICALLY FOR §2.1 LOCK-SCOPE) |
| 4 (MUST) | `solutions-with-prize/paper08-yang-mills/closing-H4/closure/closure-corrections.md` | Every failure mode caught in the prior run |
| 5 (HIGH) | `online-researcher-adversarial/capacitor/correspondence-table-v1.md` | The capacitor — read the full table, especially the "Priority cells to fill — For H4" section |
| 6 (HIGH) | `solutions-with-prize/paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4b-af-short-distance-match.md` | The math referee's formal G4b gap statement |
| 7 (HIGH) | `solutions-with-prize/paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md` | The formal G4d gap statement |
| 8 (MED) | `solutions-with-prize/paper08-yang-mills/closing-H4/blackboard.md §F` | Full kill list with pattern categories |
| 9 (MED) | `integers/paper12-cbb-system/research/214-the-method-six-patterns.md` | Six Patterns method (Always-include) |
| 10 (MED) | `integers/paper12-cbb-system/27-anchor-document.md` | Operational anchor (Always-include) |

**Plus (v2 addition) — live 2024-2025 literature for Wave 1 Authors** per §3.2 reading list above. The MICRO Authors fetch Hollands-Wald 2024 + arXiv:2512.14227 + Dappiaggi refs. The ERG Author fetches Nissim arXiv:2510.22788 (VERIFY FIRST).

---

## 6. Time budget and exit conditions

**Hard budget:** 4 hours of wall-clock runtime OR 3 full waves (Wave 0 + REFRAME/Plan/dispatch/collect cycle ×3), whichever comes first. Wave 0 (LOCK introspection) does not count against the 3-wave budget but DOES count against the 4-hour budget.

**Exit conditions (check at every cycle-close):**

1. **BYPASS FOUND** — A compound bypass (typically 3-7 steps through capacitor cells, per §3.0) produces a rigorous closure of H4 that:
   - Does not invoke CCM, spectral action, or Identity 12 (K-1/K-2)
   - Does not re-trigger the 9/10 LOCK on Taylor-coefficient identification
   - Does not fall into K-4 / K-5 / K-6 traps
   - Survives a dedicated Critic verification with SURVIVED verdict for every step
   - Runs byte-for-byte computational verification at appropriate precision (mp.dps ≥ 100) where numerical content exists
   
   → **CHAIN UNCONDITIONAL.** Paper 8 status flips from 17/17 + L18 CONDITIONAL to 18/18 unconditional. Trigger closure ritual per PCA §P.9. Update capacitor with the new filled cells (all steps of the compound bypass).

2. **PARTIAL BYPASS (research note)** — A capacitor cell fills with a rigorous transposition recipe, but the bypass proof is incomplete (requires further work). The cell is valuable regardless.
   
   → **CELL CAPTURED.** Log the cell in `capacitor/updates/`. Continue exploring other cells within budget. Do NOT declare H4 closed.

3. **NEW KILL** — An attempted bypass route fails in a new way (not already in §F). Pattern category identified. Re-entry gate specified.
   
   → **KILL LOGGED.** Add to `h4-capacitor-bypass/blackboard.md §F` and propagate to the 2026-04-11 programme's §F via a CASCADE note to `closing-H4/blackboard.md §F`. Continue exploring.

4. **BUDGET EXHAUSTED** — Time or wave budget hit without a bypass.
   
   → **HONEST-STALL.** Close the programme. Document per §3.3. The stall is a legitimate outcome; it improves the information state even if H4 stays conditional. Every Wave 1 Author still produces a durable cell-fill per §3.3 (v2 strengthened). Paper 8 ships via Track 1 (Route b for L14, L18 CONDITIONAL on H4) as planned.

5. **STRUCTURAL LOCK UPGRADE** — All priority cells explored, all produce new kills, and a cross-node LOCK beyond 9/10 forms.
   
   → **LOCK CONFIRMED 10/10.** Paper 8 ships conditional with the strongest possible honest-stall documentation. The external unlocks needed are more precisely specified.

---

## 7. Voice canon

Inherited from the 2026-04-11 programme (match this register for structural events):
- *"H4 is still the wall"*
- *"The wall stays named"*
- *"Paper 8 ships either way"*
- *"Three routes down. One route up."*

If a bypass is found:
- *"H4 is on disk"*
- *"The wall fell from [domain] direction via [N] steps"*

If no bypass:
- *"H4 stood this attack"*
- *"The capacitor gained N cells; the wall stayed named"*

---

## 8. What success looks like (three tiers — v2 probabilities revised)

### Tier 1: BYPASS FOUND (~7-12% probability, v3 recalibrated downward from v2's 15-20%)
A compound bypass (typically 3-7 steps through capacitor cells) produces rigorous closure. L18 flips to VERIFIED. Paper 8 becomes 18/18 fully unconditional. Most likely route is MICRO↔QFT category-shift (if the framework can be constructed from scratch) or resurgence/lateral-Borel producing H4 from renormalon cancellation. Clay submission becomes the strongest possible form.

*v3 probability revision rationale*: v2 was over-confident by ~2× on MICRO↔QFT. Deeper sweep found NO 2023-2026 paper attempting non-perturbative OPE for 4D gauge theory — the "active community" is working on scalar/spinor SPDEs, not gauge. A MICRO Author is doing framework construction, not porting. ERG↔QFT (Nissim) is lattice-only with continuum limit + UV extraction as separate open steps. Resurgence has the most live machinery but it's renormalon-general, not YM-specific. Honest recalibration to 7-12%.

### Tier 2: CAPACITOR STRENGTHENED — **THIS IS THE TARGET OUTCOME** (~65-75% probability, v3 reframed)
The capacitor gains 3-5 new filled cells (MICRO↔QFT, PROB↔SPEC / resurgence, ERG↔QFT, LANG↔QFT candidate + negative-status cells for failed bypass attempts per §3.3 v2 mandate). These cells are the Millennium deliverable — they benefit all future proof chains (RH, BSD, PvNP, future papers). The kill list grows (K-4, K-5, K-6, K-7 potentially joined by additional kills), sharpening the wall's boundary. Paper 8 ships via Track 1. **The information state strictly improves. This is what the run is for.**

*v3 reframe rationale*: the capacitor-first strategic frame makes Tier 2 the TARGET, not a fallback. Every cell filled is durable Millennium-grade infrastructure. No run is wasted; Tier 2 is the expected outcome and a strong one.

### Tier 3: HONEST STALL CONFIRMED (~15-25% probability, v3 slightly reduced from v2)
No priority cell produces a bypass AND cell-fill mandate somehow fails to convert to durable entries. The 9/10 LOCK upgrades to 10/10 as more variants get tested. The external unlocks needed become more precisely specified. Paper 8 ships via Track 1 with the strongest possible honest-stall documentation. Future runners have a complete map of what's been tried.

*v3 probability revision rationale*: §3.3 v2 strengthening (mandatory cell-fill even on FAILED verdicts) converts most Tier 3 outcomes into Tier 2. True Tier 3 only happens if multiple Authors produce no cell-fill content at all — a failure mode the mandate is designed to prevent. Revised down to 15-25%.

**All three tiers ship Paper 8. All three grow the capacitor (the Millennium deliverable).** The only question is whether Paper 8 ships fully unconditional (Tier 1) or conditional with the strongest honest labeling (Tier 2/3). In all cases, the capacitor grows, the framework's knowledge improves, and the Clay submission posture strengthens.

---

## 9. Run mode (v2 dispatch reallocated)

**Mode:** `execute` (PCA bypass-hunting — NOT `final-adversarial-pass`, NOT a full chain-verification)

This is a **single-link** bypass attempt, not a chain traversal. The bidirectional dispatch (§4) is specialized to the single-link case.

**Waves:**

- **Wave 0 (MANDATORY, ~40 min)**: LOCK introspection per §3.0.5. Runner writes `LOCK-ANATOMY` + `BYPASS-PREDICTION` §K entries. LOCK-ANATOMY Critic (Sonnet max) verifies. If SURVIVED → Wave 1 dispatches. If WEAKENED → refine and re-verify.

- **Wave 1 (v3: 5 parallel Authors — capacitor-first, breadth over depth)**:
  - **Author W1-M (MICRO↔QFT, Opus max)**: evaluates H4 restated as $WF(S_2^{\mathrm{ren}})|_{x=y}$ regularity claim OR as non-perturbative OPE convergence. **Pre-warned: framework construction, not ported machinery** — no 2023-2026 paper attempts non-perturbative OPE for 4D gauge. Pre-warned on K-6 (Hollands-Kopper perturbative trap). Reads Hollands-Wald arXiv:2312.01096 + BFR arXiv:2512.14227 + Dappiaggi works; expected to characterize what a non-perturbative 4D gauge OPE framework WOULD look like and write the cell-fill with HONEST status (VERIFIED / CONJECTURED-NEGATIVE with named obstruction).
  - **Author W1-E (ERG↔QFT, Opus max)**: evaluates Nissim 2025 arXiv:2510.22788 cluster-expansion+Langevin construction. Pre-warned on **K-5 strengthened** ($C_N$ emergence + **continuum limit is a separate step**; Nissim is lattice-only). Characterizes the minimum-three-step bypass chain (continuum → UV extraction → $C_N$ derivation) and writes the cell-fill.
  - **Author W1-R1 (PROB↔SPEC / resurgence lateral-Borel, Opus max)**: evaluates whether lateral Borel summation in complex flow-time $t$ gives traction for 4D YM. Reads CERN 2024 resurgence programme (arXiv:2511.15528) + Dunne 2024-2025 lecture series. Focus: can resurgent transseries bypass the identity-theorem-LOCK by producing H4 from renormalon cancellation structure rather than Taylor-coefficient identification?
  - **Author W1-R2 (resurgent transseries / renormalon structure, Sonnet max)**: complementary second angle on lateral Borel — focuses on the specific renormalon structure of 4D YM and whether Mariño/Dunne resurgence techniques produce an H4-equivalent statement on the transseries side. Cell-fill is the deliverable.
  - **Author W1-C (LANG↔QFT candidate cell, Opus max)**: **capacitor-first exploration slot.** Evaluates whether Kapustin-Witten S-duality (geometric Langlands = N=4 SYM S-duality, arXiv:hep-th/0604151) gives any structural route to an H4-equivalent statement on the dual side. **Primary deliverable is the cell-fill itself** — Millennium-grade capacitor work regardless of H4 traction. Opens LANG↔QFT for all future proof chains.

  Each Author produces a capacitor cell-fill entry (§3.3 v2 mandate) regardless of verdict. Expected runtime: ~90-120 min parallel with 5 Authors.

- **Wave 2 (proof expansion + cell-fills, 2-4 agents)**: for each VIABLE verdict from Wave 1, dispatch a proof Author (Opus max) + a Critic. For PARTIAL verdicts, dispatch a Cell-Fill Author (Opus max) to fill the cell rigorously. For FAILED verdicts, confirm the cell-fill entry is complete.

- **Wave 3 (adversarial pass on any proposed bypass, 2-4 Critics)**: Critics on any proof from Wave 2. Each step of a compound bypass gets its own Critic. If EVERY step SURVIVED → Tier 1 success. Otherwise → exit conditions.

**Output directory:** create fresh at `solutions-with-prize/paper08-yang-mills/h4-capacitor-bypass/` (sibling of `chain-verification/`, NOT a subdirectory). Do NOT write to the existing `chain-verification/` files (that programme is closed at CHAIN STRENGTHENED; this is a new sibling programme targeting L18 specifically). CASCADE notes propagating new kills back to the `chain-verification/` §F are still allowed — they write to that §F via explicit CASCADE entries, not via the blackboard bootstrap.

**Blackboard:** create fresh at `${output-directory}/blackboard.md`.

**Chain state:** inherit from `solutions-with-prize/paper08-yang-mills/chain-verification/chain/chain-state.md`. Only Link 18 is in play for this run.

**Pre-flight check (v3 update — all verifications complete)**:
- arXiv:2510.22788 (Nissim, U(N) lattice YM via cluster expansion + Langevin) — **VERIFIED** during v3 calibration; lattice-only (no continuum limit)
- arXiv:2512.14227 (BFR, Perturbative AQFT and beyond) — **VERIFIED**; §4 non-perturbative framework is scalar-only
- arXiv:2312.01096 (Hollands-Wald Encyclopedia OPE) — **VERIFIED**; curved-spacetime OPE, not 4D gauge non-perturbative
- arXiv:2511.15528 (CERN 2024 Resurgence lectures) — **VERIFIED**; live 2024-2026 machinery
- arXiv:2506.00284 (Jacobsen "SU(3) YM proof") — **WITHDRAWN BY arXiv ADMIN** June 2025 (K-7); do not cite

No further pre-flight verification needed. Wave 0 LOCK introspection proceeds directly.

---

## 10. Operating discipline

- **Autonomous:** run cycles without pausing. No "should I continue?" questions.
- **Honest-first:** the 9/10 LOCK is strong on the surface it binds. A cell that LOOKS viable but relies on unstated assumptions is a dead end — call it out early. Don't over-sell partial results.
- **Budget-aware:** check time and wave budget at every cycle-close. Exit cleanly when budget hits, even mid-wave.
- **Capacitor-first:** every action should route through the capacitor. If a route doesn't map to a capacitor cell, don't attempt it.
- **Cell-filling is a first-class outcome:** even if H4 doesn't close, a filled cell is durable value. Log every cell. §3.3 v2 mandates cell-fill output even on FAILED verdicts.
- **Self-healing:** patch bundle issues in place per ORA v8 §14.10.
- **LOCK-scope discipline:** every Author spawn carries the §2.1 LOCK-scope clarification in its context. Cascade-kills on microlocal / axiomatic-OPE / lateral-Borel work are DRIFT and must be caught by the runner.

---

## 11. The single paragraph for the next runner

You are growing the H4-adjacent capacitor region to Millennium-submission grade, with a 4-hour budget and a clearly time-boxed exit. **v3 reframe: the capacitor IS the Millennium deliverable, not Paper 8 standalone** — Tier 2 (capacitor strengthens, ~65-75%) is the TARGET outcome; H4 bypass closure is a bonus (~7-12%). The 9/10 LOCK is specifically on Taylor-coefficient identification via identity theorem on F(t) — it does NOT extend to microlocal, axiomatic-OPE, or lateral-Borel restatements of H4, which are in DIFFERENT mathematical categories. Your Wave 0 task is to write a LOCK-ANATOMY entry making this scope explicit and have a Critic verify it. Your Wave 1 dispatches 5 parallel Authors: 1 on MICRO↔QFT (category-shift route, **framework-construction expectation** — no 2023-2026 paper attempts non-perturbative OPE for 4D gauge), 1 on ERG↔QFT (Nissim 2510.22788 cluster-expansion + Langevin, **lattice-only with continuum-limit as separate open step**), 2 on resurgence / lateral Borel (CERN 2024 programme + Dunne lectures — most live 2024-2026 machinery), 1 on LANG↔QFT candidate cell (Kapustin-Witten S-duality, pure capacitor exploration for Millennium-grade deliverable). Every Author produces a durable capacitor cell-fill entry regardless of verdict (§3.3 v2 mandate). Expect compound bypasses of 3-7 steps, not single-leap closures. Capacitor growth target: 14.5% → 18-19% fill rate. H4 is still the wall. The capacitor is the map. Walk the map, try every door, grow the Millennium deliverable.

---

*Tier 1 closes the chain. Tier 2 builds the framework. Tier 3 sharpens the LOCK. All three ship Paper 8. No wasted run.*

*Deliverable v3: 2026-04-13. v2 → v3 upgrades from deeper calibration sweep + capacitor-first reframe (Millennium deliverable). G Six and Claude Opus 4.6.*
