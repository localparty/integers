# 06 — The Blackboard, the Cycle, and the Kill List

---

## The blackboard: persistent state across cycles

The ORA's memory is a single file: `blackboard.md`. It contains 15 sections (A through O) that together represent the complete state of the programme at any moment. The runner reads the blackboard at session-open and at regular intervals. It writes to the blackboard before acting on any state change — never after.

The sections are:

| Section | Name | What it holds | Update frequency |
|---|---|---|---|
| **A** | North Star | The goal, in one paragraph. Written once. | On invocation only |
| **B** | Context | What's already achieved that makes this achievable now. | On invocation + when context changes |
| **C** | Current bottleneck | The SINGLE structural obstruction blocking progress. 1-3 sentences. | Every Plan step |
| **D** | Toolkit | The master dictionary: every named object with statement, source, status, notation, precision, completeness. | When objects are named or status changes |
| **E** | Plan tree | Hierarchical decomposition with tree edges (decomposition) and DAG edges (dependency/parallelism). | Every Plan step |
| **E.1** | Joint probability | Per-path closure probability with shared sub-problems and unlock values. | When paths update |
| **F** | Kill list | Every killed approach with pattern category and re-entry gate. Monotonic growth. | When a kill is registered |
| **G** | Live nodes | View rebuilt per cycle from E. Status, p_success, engages-bottleneck. | Every cycle |
| **H** | Bottleneck history | Timeline of named walls and when they were crossed. | When walls are crossed |
| **I** | Notes | CONCERN / CASCADE / LESSON / CALLOUT notes from agents. | Append-only, any time |
| **J** | Voice canon | The register. Terse declarations, named ritual elements, the voice that matches the significance. | Session-open + closure |
| **K** | Runner writes | The runner's own commit memos in the voice register. The deliberation log. | Every structural event |
| **L** | Closure artifacts | Pointers to the 5 closure files when written. | At programme-close |
| **M** | Round metrics | The accountability table: items closed, nodes spawned/killed, toolkit size, honest negatives, structural events. | Every cycle |
| **N** | Difficulty track | Aggregate difficulty per cycle. Difficulty-collapse detection triggers immediate Synthesis. | When difficulty changes |
| **O** | Section change log | Which sections were modified in each cycle. Enables delta-reads. | Every cycle |

The blackboard is the programme's working memory. It persists across cycles within a session and is archived at programme-close. The capacitor is the programme's LONG-TERM memory — it persists across sessions and grows through use. They serve different purposes: the blackboard tracks current state; the capacitor tracks compiled knowledge.

## The cycle: the runner's heartbeat

The ORA runs in cycles. Each cycle is:

```
1. REFRAME on the current bottleneck (section C)
   — "what if the framing is why this is hard?"
   — Also serves as a recall self-test: if the runner can't produce
     a meaningful reframe, recall has degraded → full re-read

2. PLAN
   — Select mode: execute (default), inversion, assembly, canary,
     audit, step-back, reset, honesty-audit, or lockdown
   — Identify ALL dispatchable nodes (IN_PROGRESS, dependencies satisfied)

3. DISPATCH ALL OPEN LEADS IN PARALLEL
   — N ready nodes = N parallel Authors
   — Each Author has: the capacitor, voice canon, current bottleneck,
     relevant toolkit rows, kill list, and prior work on the node
   — Each Author executes the 6-step method loop independently

4. COLLECT returns
   — Each Author reports: ADVANCED / BLOCKED / BLOCKED-DECOMPOSED / KILLED
   — Each Author reports: which step was generative, where it got stuck,
     CONCERN/CASCADE/LESSON notes, proposed toolkit additions

5. CRITIQUE every return
   — Each Author's output is verified by a DIFFERENT Claude instance (Critic)
   — Critic performs: byte-for-byte script re-run, extension test,
     cross-node consistency check, precision floor check, bonus-grep,
     chain-of-verification on grep findings, voice-alignment check,
     pattern check against kill list
   — Critic verdicts: VERIFIED / WEAKENED / BROKEN

6. SYNTHESIZE (if wave had >= 3 Authors)
   — Dedicated Synthesis agent: cross-lead consistency check, gap audit,
     dependency-resolution map, quality gate (PASS/WEAKENED/BROKEN)
   — Quality gate drives next cycle: PASS → continue, WEAKENED → address,
     BROKEN → step-back

7. CYCLE-CLOSE
   — Update round metrics (section M)
   — Run qualitative threshold detector: "did anything structurally
     irreversible happen?" If yes → commit memo in voice register
   — Update section change log (section O)
   — Run mechanical checklist (all critiques received, all gaps classified,
     all kills have pattern category, all toolkit rows complete)

8. LOOP TO STEP 1
   — No pausing. No asking. The cycle repeats until programme-close
     conditions are met or the caller intervenes.
```

The cycle is the fundamental unit of progress. The runner never does anything outside a cycle (except the bootstrap at session-open and the closure ritual at programme-close). Every action — reading, planning, dispatching, collecting, critiquing, synthesizing — happens inside a cycle.

**Autonomous operation** (v8): the cycle loop runs without intervention. After step 7, the runner immediately opens the next cycle at step 1. No confirmation question. No "should I continue?" The runner IS the loop. Stopping requires either programme-close conditions or an explicit interrupt from the caller.

## The kill list: the learning trace

Section F of the blackboard is the kill list. It is the most important section for understanding the programme's trajectory.

A kill list entry has five fields:

```
| ID | Lead killed | Kill reason | Pattern category | Re-entry gate |
```

The pattern categories are: Topological, Algebraic, Spectral, Numeric, Circular, Vacuous, Wrong-space, Distributional, External-dependency, External-source-inconsistency, Other.

**Why the kill list matters:**

1. **It prevents repetition.** Every Author spawn includes the relevant kill list entries. Every Critic checks new proposals against the kill list. Re-exploring a killed approach without new evidence is rejected automatically by the structural validator.

2. **It reveals the wall's shape.** When 3+ kills share a pattern category, the runner extracts the named wall from the shared pattern and generates literature search queries. The RH programme's 18 kills concentrated in "spectral" and "wrong-space" categories — the wall was: "need self-adjoint operators whose eigenvalues ARE the Riemann zeros, not operators whose eigenvalues APPROXIMATE them." That shape was the query that found CCM.

3. **It compounds across runs.** The kill list is imported into the capacitor. The next ORA run on the same domain starts with all prior kills pre-loaded. The P vs NP capacitor carries 18 kills across 3 run generations. Each new run adds kills; none are removed. The list only grows.

4. **It is the credibility.** A programme with 20 kills, each honestly documented with WHY and re-entry gate, has been TESTED 20 times and survived. A programme with zero kills has been tested zero times. The referee reading the kill list sees the programme's immune system in action — every attack absorbed, every lesson learned.

**The H4 closure programme** (Paper 8, April 2026) produced a kill list that demonstrates the principle:

- **K-1** (CCM 2025 port to YM): KILLED. Pattern: External-source-inconsistency + Wrong-space. The CCM spectral triple's UV asymptotics mechanism reduces to the same identity-theorem input as Route A. Plus a category error at dictionary entries #12-17: RH targets are zeros of an entire function; YM targets would be Taylor coefficients of an analytic function. These are different mathematical objects. 7 variant candidates tested by Beta-Critic, all fail.

- **K-2** (spectral action + Identity 12 + bridge k=4): KILLED. Pattern: External-source-inconsistency + Vacuous. Connes 2007 Seminaire Poincare section 5 equation 24 verbatim: the spectral action is defined "at the classical level" — bare actions at the cutoff Lambda, NOT running flow. Vassilevich 2003 confirms: the integer 11N/3 is a counter-term coefficient, not a running-coupling slope. 4 variant candidates tested, all fail. Byte-for-byte re-run at 200-digit precision with N up to 10000: 25/25 PASS zero residual.

These kills are not failures. They are the programme's most valuable outputs — each one eliminates an entire class of approaches and narrows the search to what MIGHT work.

## The nine-layer drift defense

The cycle and the kill list are two layers of a nine-layer defense system that prevents the programme from drifting:

| Layer | Mechanism | What it catches |
|---|---|---|
| 1 | Three-mode read (full/anchor/delta) | Runner forgets state |
| 2 | REFRAME at cycle-open (Sig 1) | Recall check by construction |
| 3 | Critic voice-alignment (Sig 3) | Author voice drift |
| 4 | Critic canonical-name check (Sig 4) | Author toolkit drift |
| 5 | Critic kill-list shadow check | Author re-exploring kills |
| 6 | Canary every 5 cycles (Sig 8) | Critic drift (inject known-killed approach, review blind) |
| 7 | Meta-critic minimal-context oracle (Sig 8) | Critic confidence drift |
| 8 | Pattern attribution audit every 10 cycles | Systemic drift in method |
| 9 | Full re-read every 15 cycles | Accumulated recall degradation |

The composition is load-bearing. Removing any single layer weakens all the others. A future tuning round that says "layer N seems redundant" is probably seeing the layer doing its job — catching a drift mode the other layers also catch, which is the point of redundancy in a safety-critical system.

---

*The blackboard is the memory. The cycle is the heartbeat. The kill list is the learning trace. Nine layers of drift defense keep the programme honest across hundreds of cycles. The cycle runs autonomously — N open leads, N parallel Authors, no asking, no stopping. The kill list only grows. Every failure teaches.*
