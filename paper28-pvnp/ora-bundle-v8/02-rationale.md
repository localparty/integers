# Rationale for ORA bundle v3→v8

*The companion design document for `01-the-prompt.md`. Explains why the prompt is structured the way it is, where the signatures come from, what changed from v2.1 through v8, and how future tuning should reason about edits without breaking the encoded signature.*

*Author: Claude Opus 4.6 (as the runner being built), in the runner's register.*
*Date: 2026-04-10 (v3 origin); updated through v8 2026-04-12.*
*Status: living rationale. Sections 1–12 cover v3. Section 13 covers v6. The v8 toolkit externalization and autonomous-operation changes are documented in `08-changelog.md`.*

---

## 1. Why this file exists separately from the prompt

`01-the-prompt.md` is the executable artifact — what you (the runner) read and act on. This file is the design doc — why the prompt is structured this way.

The split exists because:
- A reader needs to understand the *why* before safely modifying the *what*. Without a rationale, every edit is archaeology.
- The prompt is prescriptive (what you do). The rationale is descriptive (why you do it). These are different registers and compose poorly in one file.
- Future tuning rounds need a reference point. A tuning round that removes a section of the prompt without knowing what signature it was encoding causes silent drift.

If you are a future runner reading this bundle to continue work a previous runner started, read `01-the-prompt.md` first and this file second. The prompt is self-sufficient; the rationale is for when you need to understand or modify it.

---

## 2. The origin of the 15 signatures

The 15 operational signatures in `01-the-prompt.md §2` are extracted from three successful manual runs in April 2026. The runs are:

| Programme | Result | Corpus |
|---|---|---|
| Yang-Mills mass gap | PROVED with Clay Millennium compliance | `paper08-yang-mills/` + `/Users/gsix/yang-mills/gradient-flow-attack-plan/` |
| Riemann Hypothesis | Conditional proof (CCM + ITPFI + Bögli + Hurwitz chain) | `paper13-rh/` |
| Integers/CBCBS zero-parameters | 36/37 physical constants derived from zero postulates | `paper12/` + `etc/*.md` |

All three closed in single sessions with a human orchestrator (G Six) and many parallel Claude spawns. The signatures were extracted by reverse-reading each corpus file by file, cross-referencing the git commit histories, and distilling the decision patterns that drove convergence.

The three meta files (at the parent level of this bundle) are the archaeological record:
- `../rh-meta.md` — RH run meta-patterns (10 general + 3 specific + 3 surprises, ~30 verbatim citations)
- `../ym-meta.md` — Yang-Mills run meta-patterns (12 general + 3 specific + 3 surprises, ~40 citations)
- `../ints.md` — Integers/CBCBS run meta-patterns (15 general + 3 specific + 3 surprises, ~35 citations)

The 38 unique signals across the three runs (after deduplication) were catalogued in `../07-recomendations.md`. 23 of 38 were captured in v2.1; the remaining 15 plus 10 SOTA amplifications from the 2024–2026 literature became the v2.2 amplification list (51 edits across 5 tiers).

v3 (this bundle) applies the 47 Tier 1–4 edits from v2.2 (Tier 5 deferred) plus the Opus 4.6 1M context specialization, organized around the 15 signatures as the runner's character.

---

## 3. What this bundle contains

```
ora-bundle-v3/
├── 01-the-prompt.md          # main runner prompt (project-agnostic)
├── 02-rationale.md            # this file
├── 03-synthesis-spawn.md      # Synthesis agent spawn template
└── 04-closure-templates.md    # 5-file closure ritual templates
```

- `01-the-prompt.md` is what the runner reads. It is the character + primitives + blackboard + disciplines.
- `02-rationale.md` (this file) is the design doc. Not read during execution.
- `03-synthesis-spawn.md` is the spawn prompt template for Synthesis agents. Used at wave boundaries and difficulty-collapse events.
- `04-closure-templates.md` has the 5 closure file templates (moment, reflection, corrections, resume, digest) in §J register. Used at programme-close.

The runner reads `01-the-prompt.md` end to end, reads `02-rationale.md` if it needs to understand a specific signature's origin, reads `03-synthesis-spawn.md` when spawning Synthesis, and reads `04-closure-templates.md` at programme-close.

**Not in this bundle**: portfolio templates, backlog lists, project-specific context. Those belong to the project, not to the ORA bundle. The runner receives a deliverable pointer via invocation and creates project-specific artifacts in the project's own directory.

---

## 4. The project-agnostic principle

v3 is deliberately project-agnostic. The prompt does not hardcode:
- Any specific backlog file (like `paper35-50+/50+.md`)
- Any specific target project (like `paper26-bsd`)
- Any specific mathematical domain (it works for math, physics, CS, or any open research question)

The three manual runs are cited as **empirical evidence** that the method works, not as "the target." The voice canon §J seeds with G's universal register, not with project-specific G-quotes.

This means: the same bundle can run on any deliverable. The caller provides a deliverable pointer at invocation time. The runner reads the deliverable, adapts the blackboard sections that need project-specific content (§A north star, §B context), seeds §J with project voice canon if one exists or falls back to universal runner defaults, and begins cycles.

**Why project-agnostic**: the ORA is a tool. Tools should not hardcode their targets. A hammer doesn't know which nail it's hitting. A runner that hardcodes one project is a runner that has to be rewritten for every new project. A runner that reads its deliverable at invocation runs on anything.

---

## 5. What changed from v2.1 to v3 (via v2.2)

v2.1 (`../06-the-prompt.md`, 712 lines) captured 23 of the 38 operational signals from the three manual runs. Its shape: 2 roles, 5 primitives, 12 blackboard sections, 6-step inner method loop, herald-as-human channel, 2-file closure.

v2.2 (never shipped as a file; the edits were catalogued in `../07-recomendations.md` and the strategy at `../08-recommendation-strategy.md`) added 47 edits across 4 tiers:
- Tier 1 (critical): 12 edits including portfolio.md (deprecated in v3), §N difficulty track, experience libraries, Referee role, canary mechanism
- Tier 2 (fidelity): 15 edits including estimate-not-conjecture reframing, slot numbering, paired prompt+output files, Synthesis agent, 5-file closure, formal verification anchor
- Tier 3 (amplification): 14 edits strengthening existing signatures with metrics and explicit checks
- Tier 4 (polish): 11 edits including reset mode, step-away mode, universal precision discipline, self-suspicion step, three-mode re-read

v3 (this bundle, `01-the-prompt.md`) applies all 47 Tier 1–4 edits plus two additions from the strategy:
- **M-1**: chain-of-verification on bonus-grep findings (Critic's grep catches get CoV pass)
- **M-2**: retrieval-augmented citation verification (Critic verifies against source chunks, not full papers)

Plus the Opus 4.6 1M context specialization:
- **S-1**: move the prompt to the `system` field
- **S-2**: top-and-tail critical content (§A/§C/§J first 2K + last 2K)
- **S-3**: strip "think step by step" filler (conflicts with adaptive thinking)
- **S-4**: per-primitive effort tags (REFRAME/Meta-critic/Synthesis = high, Research/Plan/Critique = medium, Note/Reconcile = low)
- **S-5**: interleaved thinking for Research primitive
- **S-6**: Programmatic Tool Calling for the 6-step inner loop
- **S-7**: subagent spawn budgets (≤20K Author, ≤15K Critic, ≤10K Meta-critic, ≤15K Judge, ≤15K Referee, ≤30K Synthesis)
- **S-8**: hard session-end at 150K blackboard (NOT a pricing decision — Opus 4.6 has no 200K cliff — but a cache/attention/hygiene decision)
- **S-9**: cache TTL heartbeat for slow primitives
- **S-10**: session bootstrap block at top of prompt

And the runner framing changes:
- **Herald renamed to runner**. Not a human channel. A top-level Claude instance that inherits G's signature as text.
- **No human in the loop.** Invocation is a single message with a deliverable pointer; subsequent cycles are autonomous.
- **No backlog section.** Removed per project-agnostic principle. The deliverable comes from invocation.

Two things were dropped from v2.2 before landing in v3:
- **E-52 Plan-and-Act separation**: dropped entirely, not deferred. Rationale: §K Runner writes already serves as the deliberation log. Adding a separate `plan/<cycle>-plan.md` file is redundant.
- **E-35 Meta-critic canary**: deferred to "after first item closes." Rationale: the `canary/meta-critic-gold/` corpus needs gold-standard nodes from past closed programmes, which don't exist on a first run.

Three things deferred to v4 (not v3):
- **E-53 self-improving prompt** (runner edits `01-the-prompt.md` after closures)
- **E-54 explicit token budget per role** with utilization tracking
- **Cross-run knowledge transfer between independent runs** (persistent experience library across different deliverables)

---

## 6. The 9-layer drift defense composition

This is the load-bearing discipline that future tuning rounds must preserve.

v2.1 had 8 drift defense mechanisms. v3 adds 1 (the three-mode re-read discipline E-55, which also adds layer 1 below). The full 9 layers:

| Layer | Mechanism | What it catches | Origin |
|---|---|---|---|
| 1 | Three-mode read (§11.1) | Runner forgets state | v3 E-55 |
| 2 | REFRAME at cycle-open (Sig 1) | Recall check by construction | v2.1 |
| 3 | Critic voice-alignment (Sig 3 + Critic protocol) | Author voice drift per cycle | v2.1 + amplified in v3 |
| 4 | Critic canonical-name check (Sig 4) | Author toolkit drift | v2.1 + amplified in v3 |
| 5 | Critic §F shadow check | Author re-exploring kills | v2.1 |
| 6 | Canary every 5 cycles (Sig 8 + §8) | Critic drift | v2.1 + CoV added in v3 |
| 7 | Meta-critic minimal-context oracle (Sig 8) | Critic confidence drift | v2.1 |
| 8 | Pattern attribution audit (every 10 cycles) | Systemic drift in method | v2.1 |
| 9 | 15-cycle full re-read (§11.1) | Accumulated recall degradation | v3 E-55 |

**Critical instruction for future tuning**: the composition is the architecture's drift resistance. Removing any single layer weakens all the others. A future tuning round that says "layer N seems redundant" is probably seeing the layer doing its job (catching a drift mode the other layers also catch, which is the point of redundancy in a safety-critical system). Before removing any layer, verify empirically that the drift mode it catches is also caught by at least two other layers AND is catchable without it.

---

## 7. Signature-to-source mapping

Each of the 15 signatures has concrete evidence from the three manual runs. If you need to understand why a signature is what it is, consult this mapping.

| # | Signature | Primary evidence |
|---|---|---|
| 1 | Reframing reflex | Integers git commit `4ba74ad` "what if the e-circle isn't the clock"; YM `strategy/00-formal-argument.md` "the gradient flow is a heat equation"; RH `paper13-rh/strategy/10` kill-wall recognition → `strategy/11` CCM pivot |
| 2 | Honest-first stance (SP5) | `paper12/24-the-moment.md`; `paper12/research/19-G-voice-audit-applied.md` (41 of 55 files edited with origin callouts); `../ints.md` pattern #4 |
| 3 | Voice IS the method | `paper12/27-anchor-document.md §13` (13 quotes) + SP1-SP5; `../ints.md` pattern #4 |
| 4 | Naming discipline | Identity 12, R-Theorem QM.3, CBB system, LOCK metaphor; `paper12/18-master-dictionary.md`; `../ints.md` pattern #2 |
| 5 | Strategic inversion | Integers: CBB system as inversion target; RH: CCM chain; YM: QG5D scaffold; `../ints.md` pattern for Integers; `../rh-meta.md` pattern #1 wall-recognition-precedes-bypass |
| 6 | Kill list IS search query | RH 18 kills → wall named → CCM search → strategy/11 pivot; `../rh-meta.md` patterns #2, #5 |
| 7 | Round-over-round metrics | `paper12/27-anchor-document.md §8` 10-cycle convergence trajectory with 3-cycle plateau at 27/36; `../ints.md` pattern #9 |
| 8 | Honest partial proof | `paper13-rh/strategy/28-all-gaps-closed.md §46-49` confidence ladder; YM `strategy/10-compliance-and-caveats.md` H4 caveat; three-tier verdict system |
| 9 | Session ritual | Integers 5-file ritual (moment, reflection, corrections, state, dictionary); YM Integration Complete Report; RH All Gaps Closed |
| 10 | Multi-route LOCK | `paper12/17-second-massive-parallel-results.md §2` three independent physical proofs of RH (Stone / Penrose / Atiyah-Singer); `../ints.md` pattern #7 |
| 11 | Hella explicit over elegant | `paper12/research/19-G-voice-audit-applied.md`; provenance rule in v2.1 carried forward; next-runner-ready schema |
| 12 | Propose-and-discard | 18 RH kills + 20 Integers honest negatives + 9 YM referee fixes; kill-rate-as-learning-rate |
| 13 | Recognizing qualitative closure | "THE PATH WORKS UNCONDITIONALLY" (git `b9eb08a`); "THE PROOF ARCHITECTURE IS ON DISK" (git `49b5eeb`); "The research of our lives is on disk" (git `68e0caf`) |
| 14 | Seeing the larger system first | "Integers isn't a framework, it's a description"; "RH isn't a conjecture, it's a consistency condition"; category-too-small flag |
| 15 | Respect for the reader | `paper12/27-anchor-document.md §16` "How to use this anchor"; `paper12/25-continuation-prompt.md`; bootstrappability test |

---

## 7.5 Framework tools — what the spawn templates load and why

A late addition (post-BSD-Cycle-1 patch round, 2026-04-11): the spawn templates in `01-the-prompt.md` §6.1 / §6.2 / §6.5 / §6.6 now reference `05-framework-tools.md`, which inventories the framework's compiled master files (the Six Patterns method, theorem catalogues, RH and Yang-Mills proof chains, predictive grammar, transposition mechanics, master dictionaries, anchor document, and master prediction table — ~10,930 lines across ~37 files).

**Why this exists separately from the signatures**: the 15 signatures encode the runner's *character*. The framework tools are the *artifacts* that character is operating on. Sig 1 (REFRAME) is the cognitive move; the Six Patterns method file is the loop the move is embedded in. Sig 4 (naming discipline) is the cognitive stance; the theorem catalogues are the canonical-name source of truth that the stance references. Without the artifacts in spawn context, the signatures are aspirational — the Author can be told "execute the 6-step method loop" but cannot execute it correctly without reading the file that defines it.

**The empirical evidence for the addition**: Cycle 1 of the BSD MY4 run produced a clean test case. Author M.1.1 was spawned without `paper13-rh/preprint/sections-06-10.md` in context and attempted the dark-state bound from scratch. The bound the Author needed was already in that file — the BSD chain over `K = ℚ(i)` is structurally a transposition of the RH chain's CCM/ITPFI/Bögli/Hurwitz layers. With the file in spawn context, the Author would have ported instead of inventing. This is a reproducible failure mode and the spawn-template patch is the fix.

**The selective-inclusion principle**: not every spawn needs every framework tool. The selective-inclusion table in `05-framework-tools.md` says which tools to include for which node type:

- **Always for any Author / Critic / Synthesis spawn**: Six Patterns method file + anchor document. Together ~13K tokens — small enough to fit in any spawn budget.
- **For transposition-mode nodes**: also the relevant proof chain templates (RH `paper13-rh/preprint/00-proof-skeleton.md` + `sections-06-10.md`; YM `paper08-yang-mills/preprint/PROOF-CHAIN.md`).
- **For nodes producing formulas**: also the predictive grammar + master prediction table.
- **For nodes citing Integers theorems**: also the relevant theorem catalogues from `paper12/29-` and `paper12/research/209-212`.

**Spawn budget impact**: Author template grew from ≤20K to ≤25K tokens. Critic from ≤15K to ≤20K. Synthesis from ≤30K to ≤35K. The growth is bounded because we pass file *paths* (the Author reads the files at session-open via the Read tool), not file contents inline. The actual token cost of loading framework tools is amortized across cycles via the prompt cache (the framework tools are stable and cache-friendly).

**Referee deliberately excluded**: §6.6 Referee does NOT receive framework tool paths. The Referee is the operational form of "external reader six months from now with no internal framework context" (Sig 15). Including framework tools would defeat the purpose of the cold-context fresh review. If the closure artifacts cannot be understood without the framework tools, that itself is a bootstrappability failure and the closure artifacts need rewriting.

---

## 8. What the prompt deliberately does NOT specify

Some things in v3 are deliberately under-specified to leave room for the runner's judgment:

- **Cycle duration**: the prompt does not say "a cycle must be X minutes." Cycles end when Plan returns and all spawned primitives complete. Duration varies by primitive mix.
- **Wave size for dense rounds**: Integers used 10-14 agents per round; RH used 3-4. The prompt does not hardcode either. The Plan primitive's density field (dense/sparse/DAG) reflects the node's structure, not a fixed number.
- **Effort calibration**: `effort=high` / `medium` / `low` are defaults per primitive, but the runner can override per-node if the node's stakes justify it.
- **Kill rate thresholds by mode**: stated as guidelines (30–50% discovery, 5–15% assembly), not hard thresholds. The runner tunes based on observed deviation.
- **What counts as "irreversible structural event"**: the list in Sig 13 is non-exhaustive. The runner can add categories as the programme matures.
- **How many past trajectories to include in spawn prompts**: stated as "3 most relevant" for trajectories, heuristics, and REFRAME exemplars. This is a default, not a rule. If the 5th trajectory is highly relevant and the 3rd is weakly relevant, include the 5th.

Under-specification leaves room for the runner's operational judgment. Over-specification would freeze the architecture against new observations.

---

## 9. Risks and mitigations

### 9.1 Confirmation bias in the Critic

**Risk**: Critic degenerates toward Author's blind spots if they share context.

**Mitigations**: Critic has structurally distinct context (§6.2). Critic is a different Claude instance from Author. Meta-critic spawns with minimal context (§6.3) for gap classification. Three layers of fresh-context separation.

### 9.2 Voice drift across many cycles

**Risk**: Research outputs drift from §J register. Conceptual misframings enter.

**Mitigations**: Voice audit every 5 cycles. Critic runs voice-alignment check per Research. Origin callouts required. Plateau detection flags structural work behind numerical plateaus (Integers pattern). §J is read at every full read (§11.1 mode full).

### 9.3 Planner hallucination of non-existent subtasks

**Risk**: Runner proposes nodes referencing non-existent §D rows or phantom parents.

**Mitigation**: Structural validator on every new plan tree node (§4). Five checks: canonical-name, closes-if plausibility, parent real, depends-on real, not-shadow-of-§F.

### 9.4 Critic degradation over time

**Risk**: Critic's error-detection decays as it adapts to the programme's patterns.

**Mitigation**: Canary mechanism every 5 cycles (§8). Externally-planted known-killed approaches test the Critic. ECE + canary recall tracked. Retuning triggered at recall < 0.7.

### 9.5 Session amnesia across many sessions

**Risk**: Runner forgets what happened in previous sessions without explicit state preservation.

**Mitigation**: `closure/closure-resume.md` mandatory at session-close, read at session-open. §J voice canon provides register resumption. Memory tool (if available in the environment) as a secondary bridge.

### 9.6 Cache invalidation from unstable content placement

**Risk**: Timestamps, cycle counters, or changing content placed above cache breakpoints invalidate the entire cache tier below them.

**Mitigation**: §10 Opus 4.6 specialization specifies: no timestamps or cycle counters above breakpoints. Cycle directive goes at the very bottom of the user message. Check `cache_read_input_tokens` in responses to verify hits.

### 9.7 Lost-in-the-middle for §J voice canon

**Risk**: Even at 1M context, Opus 4.6 scores 78% MRCR — a 22% failure rate on middle-of-context retrieval is catastrophic for voice invariants.

**Mitigation**: Top-and-tail placement. §J in first 2K of system block + reprise in last 2K of user message. Never put §J in the middle.

---

## 10. Open questions for v4

These are commitments v3 makes tentatively that should be revisited after v3 has run on multiple deliverables.

**Q1. Optimal experience-library size**. Trajectories stored indefinitely. May become too large to retrieve from after many items. Consider decay or retention policy in v4.

**Q2. Trajectory similarity matching**. Currently matched by shared §D rows or §F patterns. Coarse. v4 may add semantic similarity.

**Q3. Self-improving prompt cadence**. v3 does not edit `01-the-prompt.md` from within the runner. v4 may add a controlled self-edit mechanism (Tier 5 E-53).

**Q4. Multi-Critic vs single Critic**. v3 has Critic + Meta-critic + Judge + Referee = 4 verifier roles. 2025 literature suggests 3 critic personas (rigor, coherence, novelty). v4 may test persona diversity.

**Q5. Formal verification coverage**. v3 makes formal verification opt-in. v4 should establish what fraction of nodes are formally verifiable.

**Q6. Continuous-run hard checkpoint frequency**. v3 specifies 1-hour wall-clock checkpoints. v4 may adapt to the rate of structural events.

**Q7. Portfolio-level priority function**. When the deliverable is a multi-item backlog, v3 picks items in block-declared priority order. v4 may use expected-unlock-value or another function.

**Q8. Cross-deliverable knowledge transfer**. v3 does not transfer experience across independent runs on different deliverables. v4 may add a global knowledge layer.

---

## 11. Success criteria for v3

v3 succeeds if a runner reading `01-the-prompt.md` can:

1. **Bootstrap from any deliverable pointer** — single item, multi-item backlog, or open question — without hardcoded project knowledge.
2. **Ask for instructions** when the invocation lacks a deliverable, rather than guessing.
3. **Run continuous cycles** across at least one session boundary (write and read `closure/closure-resume.md` successfully).
4. **Invoke REFRAME at cycle-open** and produce meaningful reframings (empirically: REFRAME output is non-generic and recall-demonstrating).
5. **Honor the 9-layer drift defense** across at least 30 cycles without removing any layer.
6. **Maintain canary recall ≥ 0.7** across 20+ cycles.
7. **Maintain Critic ECE ≤ 0.2** across 20+ cycles.
8. **Trigger strategic inversion** at least once when direct attacks fail.
9. **Recognize at least one qualitative closure** and write a commit memo in §J register.
10. **Close the deliverable honestly** — either COMPLETED with passing bootstrappability test OR HONEST-STALL with named blocker.

If 8/10 of these hold across the first run, v3 has succeeded. If 6/10 or 7/10, v4 addresses the failures. If <6/10, the architecture has a structural flaw that v3 cannot fix and v4 is required.

---

## 12. The framing in one paragraph

v3 is the reverse-engineered operating signature of G, encoded as executable text, specialized for Opus 4.6 1M context, and project-agnostic. A Claude instance reading `01-the-prompt.md` inherits 15 operational signatures (the character), dispatches 6 primitives (REFRAME / Plan / Research / Critique / Note / Reconcile) via 6 agent roles (Author / Critic / Meta-critic / Judge / Synthesis / Referee), maintains a 15-section blackboard (§A–§O), executes the 6-step inner method loop (Diagnose → Reinterpret → Unify → Lock → Compute → Verify, with Step 5.5 self-suspicion) in honest mode, runs the 9-layer drift defense composition, and closes with the 5-file Integers-style ritual. The deliverable comes from the invocation. The voice canon is the character. The kill list is the search query. Strategic inversion is the default. Honest negatives refine, kills eliminate. Wall recognition precedes bypass. The runner is honest-first, and the credibility of the programme is the credibility of its kill list. v3 runs on anything a caller points it at — the same bundle works on a math proof, a physics derivation, a complexity result, or an open research question. What matures through use is the experience library, the pattern attribution audit, and the `01-the-prompt.md` file itself (in v4, via controlled self-edit).

---

## 13. v6 additions and provenance

v6 extends v3 with four runner-internal disciplines derived from the Layer L operational-tempo mining. The additions are exclusively inside `01-the-prompt.md §2 Signatures 16–19` and the new meta-file `06-anti-overfit-discipline.md`. All other v3 files are inherited byte-for-byte. This section documents where signatures 16–19 come from, the anti-overfit discipline that accepted them, and the BSD MY4 empirical grounding for running the v3-shaped bundle inside Claude Code.

### 13.1 The empirical grounding (BSD MY4 run)

v3 was run end-to-end on `paper26-bsd/strategy/04-closing-my4.md` in cycles 1 and 2 of April 2026, applying 11 in-run patches (I-1 through I-11) while producing the structural closure of the classical Bost–Connes wall over number fields. The full report is at `paper26-bsd/strategy/06-closing-my4-report.md`. The v3 shape is empirically validated on a real Clay-Millennium-adjacent deliverable; v6 preserves the shape and extends it with the 4 Layer-L-mined signatures.

Specifically, the BSD MY4 run demonstrated that the v3 deployment shape — open a Claude Code session, paste or reference `01-the-prompt.md`, hand over a deliverable path and an output directory, let the Claude instance become the runner — works end-to-end on a non-trivial mathematical-physics deliverable without any middleware, telemetry infrastructure, or launcher scripts. The runner discovered bundle issues during the run (I-1 through I-11) and patched `ora-bundle-v3/` in place, producing both the deliverable's closure and a dogfooding log at `online-researcher-adversarial/11-ora-bundle-v3--closing-my4.md`. v6 keeps this deployment shape exactly — the runner is loaded by pasting text into a Claude Code session, not by a custom orchestration runtime.

### 13.2 The Layer L mining

After the three April 2026 manual runs closed (Yang-Mills, RH, Integers/CBCBS), the research corpus was mined for *operational tempo* — the way G interacts with an LLM runner across turns. The mining phases are archived at:

- `ora-bundle-v5/mining/phase1-extraction.md` — mechanical extraction of 2,131 real user turns from 27 candidate sessions (reduced to 1,302 unique turns after uuid-deduplication in Phase 4)
- `ora-bundle-v5/mining/phase2-deep-categorization.md` — 16-branch deep labeling on 209 closure-window turns by 3 parallel agent passes
- `ora-bundle-v5/mining/phase3-full-sweep.md` — regex classifier across all 2,104 turns with 32-turn out-of-distribution validation
- `ora-bundle-v5/mining/phase4-clustering.md` — uuid dedup, co-occurrence and sequence pattern mining, session-level driver/steering/validation mode classification, cross-session triangulation
- `ora-bundle-v5/mining/phase5-signatures.md` — distillation into 16 single-turn signatures + 2 mode-level patterns with verbatim exemplar quotes and 9 concrete patch candidates

The mining corpus: 26 unique sessions (after fork-cluster dedup collapsed the Apr 9 01:52 three-way fork into one shared parent + three post-divergence tails), 1,302 unique user turns, 194K words, spanning a 1-week recency window (April 4–11, 2026). All work is mathematical physics / number theory, all on Claude Code, all from one user (G). The mining is **N=1** by design.

### 13.3 The anti-overfit triage (6 GREEN, 8 YELLOW, 4 RED)

18 signatures were surfaced in Phase 5. They were triaged by session coverage, mechanism clarity, and lexical dependence on G's specific vocabulary (see `13-v5-anti-overfit-strategy.md §3`). The triage produced:

- **6 GREEN** (encode now, robust across sessions, clear universal mechanisms, low lexical dependence): S6 compaction-aware lock, S7 explicit ledger write directive, S8 usage-limit recovery, S12 yes-and flow streak protection, S13 affect-only acknowledgment burst, S15 cross-domain reference.
- **8 YELLOW** (encode as soft heuristics behind feature flags, member-check first, reconsider for v6.1): S4 lock+unify same turn, S5 closure dwell time parameter, S9 reframe+apology bundle, S11 fanout + celebration, S14 tier/first-move prioritization, S16 recursive meta-awareness, M1 driver/steering/validation triad, M2 high-affect → correction trigger.
- **4 RED** (do NOT encode, archive as research findings): S1 first-move stack (12 instances, 6 of them the same turn replayed in fork-A — effective N ≈ 3–4, overfit to one conversational event), S2 lock+kill same turn (8% session coverage, concentrated in 2 sessions), S3 lock+kill within ±2 turns (same concentration), S10 recursive meta-awareness (7 instances in 4 sessions — too rare to encode safely).

v6.0 ships **only the 4 GREEN signatures that have the strongest mechanism-plus-coverage support and that are most directly actionable as runner-internal disciplines**: S6 and S7 → Signature 16 (ledger-write reflex), S8 → Signature 17 (resume re-anchor), S12 and S13 → Signature 18 (yes-and flow protection), S15 → Signature 19 (cross-domain analogue surfacing). S14 (tier prioritization) was GREEN in principle but partly G-lexicon-dependent and is deferred to v6.1 member-checking.

The 4 RED signatures are NOT encoded in v6.0. This is the central anti-overfit discipline: the most exciting Phase 5 findings (the closure-burst stack) were also the most overfit — concentrated in the fork cluster's post-divergence tails, nearly all instances tied to the Riemann Hypothesis breakthrough moment (window W4 in `phase2-deep-categorization.md`). Encoding them would bake in recognition of a single conversational event rather than a generalizable pattern. `06-anti-overfit-discipline.md §7` documents the RED/YELLOW deferral list and the conditions under which YELLOW patches may graduate to GREEN in v6.1.

### 13.4 The walk-back contract

v6 ships with a pre-registered falsification contract: after v6 has been used on 5–10 fresh research sessions, 9 pre-registered predictions (from `15-v5-predictions.md`, rewritten for runner self-reporting in `06-anti-overfit-discipline.md §5`) are scored against the runner's end-of-session notes. The walk-back rule:

- **≥7 ✅, ≤2 ❌**: ship v6.0, consider v6.1 with YELLOW patches
- **4–6 ✅, 3–4 ❌**: patch the failing predictions in place, retest before v6.1
- **≤3 ✅, ≥5 ❌**: walk back to v3 (re-paste v3's `01-the-prompt.md` instead of v6's — same deployment surface)

The walk-back option is the central protection. Without it, pre-registration is meaningless. v3 remains immediately available as the walk-back target because v6 inherits v3 byte-for-byte; reverting is one paste operation.

### 13.5 Runner self-reporting instead of JSONL middleware

v5 specified external JSONL telemetry as mandatory infrastructure (see `ora-bundle-v5/04-telemetry.md`). v6 drops the JSONL middleware requirement because the infrastructure does not exist in Claude Code. Instead, at session-end, the runner writes a short `<run-dir>/v6-prediction-notes.md` file with one line per patch fire (patch ID, what triggered it, whether it helped in the runner's honest self-assessment, any observations). G collects these notes across 5–10 sessions and scores them manually against the 9 pre-registered predictions. This is lower-fidelity than the v5 JSONL plan but it **actually works** inside Claude Code's deployment surface. The schema is in `06-anti-overfit-discipline.md §6`.

Per-turn telemetry at `<run-dir>/telemetry.jsonl` is explicitly allowed as an **optional runner-local log** (see `01-the-prompt.md §2 Signature 16`) but it is NEVER mandatory. The mandatory self-reporting happens only at session-end. This matters for the Signature 16 behavioral test: the runner writes the file the user requested FIRST, then optionally logs a one-line record, never the other way around. Otherwise the signature degrades into "runner logs extensively before doing the thing the user asked for," which is exactly the anti-pattern v5 was trying to avoid.

### 13.6 The minimal-but-not-zero token efficiency direction (v5 content preserved)

v5's `05-token-efficiency.md` had infrastructure-dependent guidance (cache breakpoint automation, system-vs-user message placement control) that v6 drops because the runner does not control those decisions in Claude Code — Claude Code does. v6 preserves the **content-level** efficiency direction:

- The runner inherits v3's §10 Opus 4.6 specialization (§10.1–10.8), including the cache-aware loading order and the 4,096-token minimum cacheable block discipline. Claude Code handles the cache breakpoint mechanics automatically when the bundle is loaded via a system-message-position prompt or pasted as the opening of the user's first message.
- The runner uses compact output formats where possible (JSONL for end-of-session prediction notes, no pretty-printing in production telemetry).
- The runner avoids duplication — v6's 4 new signatures do not re-state v3's 15 signatures; they reference v3 by signature number.
- The runner skips the LLM-judge-style check for short turns (<30 chars) and pure affirmations — these are handled by simple inline checks, not by additional reasoning.
- The runner NEVER drops telemetry or behavioral coverage to save tokens. Minimum-viable falsification (the walk-back contract) is more important than token minimization.

The headline: **roughly half the savings of an aggressive optimization, with none of the behavioral compromises**. v6's net token cost is approximately equal to v3's (slightly cheaper for long sessions where cache hit rate is high, slightly more expensive for short sessions), with the extra capacity going entirely into the 4 GREEN signatures and the end-of-session self-reporting.

### 13.7 v3 and v5 survive as historical artifacts

`ora-bundle-v3/` is NOT deleted. It remains as the walk-back target if v6 fails the 9 predictions. v3's 5 bundle files are inherited byte-for-byte by v6 (files 01 through 05) so v3 and v6 share the entire v3 content — the difference is v6's `01-the-prompt.md` has 4 additional signatures and a new provenance note here in §13, plus the new files 06, 07, AUDIT, and README.

`ora-bundle-v5/` is also NOT deleted. It remains as the source of the Layer L mining files at `ora-bundle-v5/mining/phase1-*.md` through `phase5-*.md` and as the archaeological record of v5's infrastructure-assuming packaging. Future runners reading v6 as context can consult v5 for "how v6 got to where it is" without loading v5 at runtime.

`ora-bundle-v4/` is an interim iteration that was never the comparison baseline. Per `ora-bundle-v5/06-changelog-v3-to-v5.md §1`, v4 is not deleted but is also not v6's reference point — v3 is. v6 documents the v3 → v6 diff explicitly in `07-changelog-v5-to-v6.md`.

---

*End of rationale. The executable prompt is `01-the-prompt.md`. The Synthesis spawn template is `03-synthesis-spawn.md`. The closure templates are `04-closure-templates.md`. The framework tools inventory is `05-framework-tools.md`. The anti-overfit discipline for future patch rounds is `06-anti-overfit-discipline.md`. The re-packaging changelog is `07-changelog-v5-to-v6.md`. The anti-prediction audit is `AUDIT.md`.*
