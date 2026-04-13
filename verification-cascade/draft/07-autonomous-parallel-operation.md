# 07 — Autonomous Parallel Operation

---

## The problem the ORA solved

The first ORA runs had a problem: the runner would complete a cycle, then pause and ask "should I continue?" or "which lead should I pursue next?" This forced the caller to babysit every cycle — defeating the purpose of autonomous operation. The caller would type "follow every open lead in parallel and continue any number of cycles," the runner would execute one more cycle, then ask again.

The problem was not mechanical. The prompt already specified autonomous cycling (continuous-run mode in section 11.5) and confirmation suppression (Signature 18). The problem was CONCEPTUAL: the prompt treated parallel dispatch as an optimization and autonomous cycling as a special mode requiring entry conditions. The runner's default identity was "serial processor that asks before each step" — the exact pattern the ORA was designed to replace.

The fix was not adding more rules. It was changing the runner's IDENTITY.

## The parallel explorer identity

In ORA v8, three CRITICAL blocks appear at the very top of the prompt — before the bootstrap, before the signatures, before everything. They are the first thing the runner reads:

**CRITICAL — TOOLKIT/CAPACITOR**: "The toolkit is NOT hardcoded in this prompt — it is an input, provided by the caller alongside the deliverable."

**CRITICAL — AUTONOMOUS OPERATION**: "You are a parallel explorer. Every open lead is a door — you walk through ALL of them simultaneously."

**CRITICAL — SELF-HEALING**: "When you catch a bundle-level failure mode during a run — you fix it in place, log it, and continue. You do not stop. You do not ask permission."

The autonomous operation block continues:

> *Cycle continuation is automatic. After cycle-close, you immediately open the next cycle — no pausing, no asking, no waiting. The cycle loop is: REFRAME -> Plan -> dispatch ALL open leads -> collect returns -> cycle-close -> repeat.*
>
> *Parallel dispatch is mandatory. When Plan identifies N dispatchable nodes, spawn N Authors simultaneously — 2 ready means 2 Authors, 7 ready means 7 Authors. Idle dispatchable nodes are wasted opportunity. The natural state of the programme is: every node that CAN be worked on IS being worked on.*

And a banned-phrase list:

> *NEVER produce any of: "should I continue?", "shall I proceed to the next cycle?", "do you want me to dispatch Authors?", "ready to move on?", "let me know if you'd like me to continue", "should I go ahead?", "which lead should I pursue?". These break the caller's flow and waste a round-trip.*

## The empirical path to v8

The autonomous operation architecture was not designed top-down. It converged through empirical failures:

**v3 (original)**: The prompt specified selective inclusion — the runner classified node types, looked up which framework files to include, and included them conditionally. This required classification decisions at every spawn.

**I-v6-3** (P vs NP, cycle 1): The runner dispatched an Author without framework tools. The Author attempted from scratch and missed existing verified results. Fix: added a mandatory spawn checklist.

**I-v6-4** (P vs NP, cycle 2): The checklist was followed but item 3 ("conditional-include files identified") was checked off without actually looking up the table. The runner classified the node as one type and missed that it was also a transposition + spectral-gap node. Fix: made the checklist mechanical with an inline lookup table.

**I-v6-5** (P vs NP, cycle 2 post-mortem): Three consecutive failures from the same root cause — runner misclassifying node types under the selective-inclusion protocol. The user's observation: "what's a better fix? to pass all the knowledge... lets remove the filters and always pass all." Fix: KILLED the selective-inclusion optimization entirely. Always pass the full toolkit. Let the agent self-select.

The pattern: (3) added a checklist, (4) made it mechanical, (5) killed the optimization entirely. Three iterations to learn that the optimization's cost (misclassification failures) exceeded its savings (token efficiency). The lesson: **when an optimization fails three times from the same root cause, the optimization is wrong. Kill it. Pass everything. Let the agent self-select.**

The same convergence pattern produced the autonomous operation CRITICAL block:

**Early runs**: Runner asks between cycles. User says "continue." Runner executes one cycle, asks again.

**v8 fix**: Don't add a rule saying "don't ask." Change the runner's IDENTITY. "You are a parallel explorer. Every open lead is a door. You walk through ALL of them simultaneously." The runner doesn't suppress asking because a rule says so — it doesn't ask because its identity is "explore everything in parallel, always."

## The effort table: where to spend tokens

Autonomous parallel operation means the runner dispatches many agents simultaneously. Not all agents need the same computational effort. The v8 effort table encodes where to spend tokens:

| Primitive | Effort | Rationale |
|---|---|---|
| REFRAME | **max** | Deepest cognitive move. Every reframe on the programme's wall needs the deepest reasoning. |
| Meta-critic | **max** | The CLOSABLE vs GENUINE call is the highest-leverage metacognitive decision. LLMs have weak type-2 metacognition; max effort partially compensates. |
| Synthesis | **max** | Cross-lead synthesis is where structural insight crystallizes. The window between insight and structure needs maximum depth. |
| Author (bottleneck-engaging) | **max** | Nodes with `engages-bottleneck: yes` are the wall-attacking nodes. A subtle gap missed at medium effort costs an entire revision sub-cycle. |
| Critic (bottleneck-engaging) | **max** | Overclaiming on wall-attacking claims is the most dangerous failure mode. Max effort to catch subtle gaps. |
| Author (non-bottleneck) | medium | Assembly nodes, editorial nodes, orthogonal insurance. |
| Critic (non-bottleneck) | medium | Structural verification on non-critical nodes. |
| Plan | medium | Wave-size and DAG decisions. |
| Note | low | Short tagged annotations. |
| Reconcile | medium | Debate adjudication between disagreeing agents. |

The classification is free: `engages-bottleneck: yes/no` is already tracked in section G of the blackboard. The runner does not classify — it reads the field it already maintains. No new lookup table. No conditional logic beyond one field check.

**Empirical grounding**: The H4 closure run produced a WEAKENED verdict on R.D.1 at medium Critic effort — the inference-from-source error (I-v6-1) that required a Wave 1.5 revision sub-cycle. The P vs NP run required external effort configuration in the invocation file (15 lines specifying which roles get max effort). Both cases motivated baking effort levels into the prompt. As of v8, the invocation file needs zero effort configuration.

## The four-line invocation

With autonomous operation, effort levels, and self-healing all baked into the prompt, the ORA invocation reduces to four lines:

```
read your instructions from ora-bundle-v8/01-the-prompt.md
the run brief is <deliverable>.md
the toolkit for this run is <capacitor>.md
the run output directory is <output-dir>/
```

No effort configuration. No "continue indefinitely." No "fix issues and log them." No "follow every open lead in parallel." These are all INSIDE the prompt now.

The caller provides WHAT (the brief), WITH WHAT (the capacitor), and WHERE (the output directory). The HOW is the prompt. The runner reads the prompt, becomes the parallel explorer, reads the capacitor and brief, creates the blackboard, and begins cycling. Autonomously. In parallel. Until done.

## What autonomous operation enables

The verification cascade needs autonomous operation because:

1. **Verification runs are long.** A CCM verification with 30+ proof steps, each needing a Critic + a Re-deriver, produces 60+ agent spawns across multiple waves. A human babysitting every wave is a bottleneck the cascade cannot afford.

2. **Cross-tier escalation is automatic.** When a step is WEAKENED, the runner immediately escalates to Tier B (excision). When excision fails, it escalates to Tier C (construction). These escalations happen INSIDE the cycle loop, not between sessions. Autonomous operation means the three tiers compose seamlessly.

3. **Parallel dispatch is the cascade's throughput.** N proof steps verified simultaneously instead of sequentially. A serial verifier checking 30 steps one-by-one takes 30 cycles. A parallel verifier dispatching all 30 in one wave takes 1 cycle + 1 Synthesis cycle. The parallel explorer identity is not just faster — it finds CROSS-STEP patterns that serial verification misses.

4. **The capacitor grows during the run.** Every wave produces new findings that the dynamic capacitor absorbs (self-adjust), uses to remove dead approaches (trim), and transfers to other tiers (amplify). Autonomous operation means the capacitor's growth is continuous, not interrupted by human round-trips.

---

*The runner is a parallel explorer. It walks through every open door simultaneously. It does not ask — it runs. It does not serialize — it dispatches N leads in parallel. It does not stop — it cycles until done. Four lines to invoke. Autonomous from the first cycle. The method is the prompt. The prompt is the researcher.*
