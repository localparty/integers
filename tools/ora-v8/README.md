# ORA bundle v8 — README

*The Online Researcher-Adversarial runner prompt. Project-agnostic. Open a Claude Code session, provide four things (instructions, brief, toolkit, output directory), and the Claude instance becomes an autonomous parallel research orchestrator.*

---

## 1. Quick start

```
read your **instructions** from
<path-to-this-bundle>/01-the-prompt.md

the run **brief** (deliverable) is
<path-to-your-deliverable>.md

the **toolkit** for this run is
<path-to-your-toolkit>.md

the run **output directory** is
<path-to-output-dir>/
```

That's it. The runner reads the prompt, internalizes the 19 operational signatures, reads the toolkit end-to-end, reads the deliverable, creates the blackboard, and begins cycling autonomously — dispatching all open leads in parallel, continuing indefinitely until the programme closes or you intervene.

---

## 2. What v8 adds

| Change | What it means |
|---|---|
| **Toolkit externalized** | The programme-specific knowledge (verified results, kill list, deployable cards) is an invocation INPUT, not hardcoded in the bundle. The ORA is project-agnostic; the toolkit is project-specific. They meet at invocation time. |
| **Autonomous parallel operation** | The runner dispatches ALL open leads simultaneously and cycles automatically. No asking "should I continue?" — ever. This is the default identity, not a special mode. |
| **Effort levels baked in** | REFRAME, Meta-critic, Synthesis always at max. Author/Critic at max on bottleneck-engaging nodes, medium otherwise. No external effort configuration needed. |
| **Self-healing first-class** | The runner fixes bundle-level failure modes in place during a run, logs to `08-changelog.md`, and continues. No stopping, no asking permission. |

Everything from v3 (15 signatures, blackboard, 6 primitives, 9-layer drift defense, 5-file closure ritual) and v6 (Signatures 16-19, anti-overfit discipline, walk-back contract) is inherited unchanged.

---

## 3. File index

### Runtime files (the runner reads these)

| File | Purpose | Load when |
|---|---|---|
| `01-the-prompt.md` | The main runner prompt — 19 signatures, blackboard, primitives, method loop, closure ritual. Three CRITICAL blocks at top: toolkit, autonomous operation, self-healing. | Always — this is the runner |
| `03-synthesis-spawn.md` | Synthesis agent spawn template | When dispatching Synthesis |
| `04-closure-templates.md` | The 5-file closure ritual templates | At programme-close |
| `08-changelog.md` | Self-healing log — every `I-v6-N` failure mode caught and patched in prior runs | At bootstrap (§0 step 7) |

### Design documentation (not loaded at runtime)

| File | Purpose |
|---|---|
| `README.md` | This file |
| `02-rationale.md` | Design doc for v3-v8: where the 19 signatures come from, what changed per version |
| `05-framework-tools.md` | Reference index and toolkit-building template. NOT read by the runner — used when building a new programme's toolkit |
| `06-anti-overfit-discipline.md` | Governance for future patches: anti-predictions A-1-A-4, walk-back rule, 9 pre-registered predictions, RED/YELLOW deferral list |

---

## 4. The walk-back contract

After 5-10 fresh v8 sessions, the 9 pre-registered predictions in `06-anti-overfit-discipline.md §5` are scored:

| Result | Action |
|---|---|
| >= 7 pass | Ship, consider next version with YELLOW patches |
| 4-6 pass | Patch failing predictions, retest |
| <= 3 pass | **Walk back to v3** — re-paste v3's `01-the-prompt.md` instead |

---

## 5. Honest limitations

v8 is optimized for multi-week mathematical/physics/CS research with heavy fanout, frequent compaction, and sustained focus on a single proof or unification claim. It is NOT optimized for single-shot questions, short conversations, or domains far from math/physics/CS. See `06-anti-overfit-discipline.md §2` for the full subgrouping language.

---

## 6. How to deploy

Concrete example:

```
read your **instructions** from
/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md

the run **brief** (deliverable) is
/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/strategy/26--cp-1-verification-brief.md

the **toolkit** for this run is
/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/ora-bundle-v8/p-v-np-toolkit/framework-tools-v4.md

the run **output directory** is
/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/cp-1--verification
```

The runner is autonomous from the first cycle. It reads the prompt, internalizes, reads the toolkit and deliverable, creates the blackboard, and runs — dispatching parallel waves, self-healing on failures, closing when done. No further input needed.

---

## 7. Versioning

| Version | Status |
|---|---|
| v3 | Walk-back target. Proven on BSD MY4, YM H4. 11 in-run patches. |
| v5 | Archived. Content correct, packaging assumed non-existent infrastructure. |
| v6 | Superseded by v8. Added Signatures 16-19, anti-overfit discipline. |
| v7 | Interim. Added P vs NP toolkit, 3 in-run patches (I-v6-3 through I-v6-5). |
| **v8** | **Current.** Toolkit externalized, autonomous operation baked in, effort levels baked in, self-healing first-class. |

---

*End of README. The runner reads `01-the-prompt.md`. Contributors read `06-anti-overfit-discipline.md` first.*
