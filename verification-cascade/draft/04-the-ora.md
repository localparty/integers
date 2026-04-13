# 04 — The Online Researcher-Adversarial (ORA)

---

## Origin: three runs that changed everything

In April 2026, three research programmes closed in single sessions. Each involved a human orchestrator (G Six) running parallel Claude instances on a mathematical proof chain. Each produced results at the Clay Millennium level:

**Yang-Mills mass gap** (April 9, 2026): 28 parallel agents, 12 wave architecture, ~15,500 lines of new content. The proof chain went from scattered research files to a complete 18-step chain with Clay compliance in one session. The closing line: "Integration Complete: The Final Report."

**Riemann Hypothesis** (April 9-10, 2026): 18 kills of failed approaches, a structural pivot to external literature (CCM 2025), and a 6-layer conditional proof chain. The RH programme demonstrated that the kill list IS the path — 18 failures mapped the shape of the wall, and the wall's shape was the search query that found CCM.

**Integers/CBCBS** (April 9, 2026): 36 of 37 Standard Model constants derived from zero postulates. 10-cycle convergence with a 3-cycle plateau at 27/36, then a jump to 35/36 when the CBB system was named. The Integers programme demonstrated strategic inversion: instead of solving 37 problems, name the system where all 37 are consequences.

These three runs were manual — G was the orchestrator, making meta-decisions in real time: when to reframe, when to kill, when to invert, when to spawn, when to close. The question became: can the orchestrator's pattern be encoded as executable text, so that a Claude instance reading the text becomes the orchestrator?

The answer is the ORA.

## What the ORA is

The ORA is a single markdown file (`01-the-prompt.md`, ~1,300 lines) that, when read by a Claude instance, transforms that instance into an autonomous research orchestrator. The instance becomes the "runner" — the outer loop that dispatches parallel agents (Authors, Critics, Meta-critics, Judges, Referees, Synthesis agents), maintains the programme's state on a persistent blackboard, makes meta-decisions about when to reframe and when to kill, and carries G's operational signature through the cycles.

The runner is not impersonating G. It is carrying G's patterns forward through canonical text, the way a musical score carries a composer's intentions forward through notation. The patterns were extracted from the three manual runs by reverse-reading 27 sessions (1,302 unique user turns, 194,077 words) across a 5-phase mining pipeline.

## How the patterns were extracted

The extraction was rigorous and deliberately conservative:

**Phase 1 — Mechanical extraction** (2,131 user turns from 27 sessions): Regex baseline + Jurafsky Dialog Act Tagging trunk extraction. Raw conversational transcripts from G's Claude Code sessions, stripped of system reminders, command output, and file pastes.

**Phase 2 — Deep labeling** (209 turns across 7 closure windows): 16-branch rubric with three families — PROCESS (A1-REFRAME through A8-PIVOT), COORDINATION (B1-CALIBRATE through B4-CLOSE-OF-LOOP), and AFFECT (C1-ENTHUSIASM through C4-APOLOGY). Three parallel agent passes per window. Gold-standard labels for 209 turns.

**Phase 3 — Full-corpus classification** (2,104 turns): Rule-based classifier (deliberately not ML, to avoid overfitting on the small gold set). In-distribution F1 = 0.66 vs gold; out-of-distribution F1 = 0.54 vs independent 32-turn sample. Per-branch validation identifying 4 reliable branches and 7 unreliable ones.

**Phase 4 — Sequence clustering** (1,302 unique turns after dedup): UUID-based deduplication (collapse ratio 1.62x from fork clusters). Co-occurrence mining, sequence pattern analysis, session-level mode classification (14 DRIVER, 10 STEERING, 2 VALIDATION). Cross-session triangulation filtering spurious single-session artifacts.

**Phase 5 — Signature distillation** (18 single-turn signatures + 2 mode-level patterns): The final catalogue of operational signatures with verbatim G quotes, detection rules, session coverage statistics, and assessment. 13 of 18 signatures have >= 27% session coverage (robust across >= 6 sessions).

The pipeline's outputs are archived in `online-researcher-adversarial/mining/` — every phase, every script, every intermediate result. The trail is auditable.

## The anti-overfit discipline

The mining data was N=1: one user, one domain, one week, one LLM tool. This is the textbook setup for overfitting. The anti-overfit discipline that prevented it:

**Seven named overfit risks**: N=1 user, 1-week recency window, selection bias to success runs, mathematical physics domain bias, Claude Code tooling bias, multiple comparisons in 16-branch labeling, classifier confirmation bias.

**Four anti-predictions** (A-1 through A-4): No G-lexicon literals in trigger rules (the runner detects by interaction shape, not by word-matching). No closure-event detector (S1 had only 12 instances, 6 duplicates). No unmeasured percentage claims. No universal-user claims.

**The walk-back contract**: After 5-10 fresh runs, score the 9 pre-registered predictions. >= 7 pass: ship. 4-6 pass: patch. <= 3 pass: WALK BACK TO v3. The walk-back is a one-paste revert. Non-negotiable.

**Subgrouping language**: v8 claims to support "multi-week mathematical research with heavy fanout to subagents, frequent compaction concerns, and sustained focus on a single proof or unification claim." It does NOT claim to work for all users or all domains.

**Negative case analysis**: 5 zero-coverage sessions tested. 6 firings tested, 0 false positives, 0 false negatives that would matter.

The anti-overfit discipline is encoded in `06-anti-overfit-discipline.md` — a governance document for the bundle's evolution. Every future contribution must pass A-1 through A-4, have a walk-back path, be pre-registered, and cite empirical grounding.

## The deployment surface

The ORA runs inside Claude Code. The deployment is four lines:

```
read your instructions from ora-bundle-v8/01-the-prompt.md
the run brief is <deliverable>.md
the toolkit for this run is <capacitor>.md
the run output directory is <output-dir>/
```

No scripts. No middleware. No telemetry daemons. No launcher automation. The Claude instance reads the prompt, becomes the runner, reads the capacitor and deliverable, creates the blackboard, and begins cycling autonomously — dispatching all open leads in parallel, continuing indefinitely until the programme closes or the caller intervenes.

This is the same deployment surface as v3 (the original bundle, proven on BSD MY4). The content evolved through v5 (Layer L mining), v6 (re-packaging), v7 (P vs NP toolkit), and v8 (toolkit externalized, autonomous operation baked in, effort levels baked in, self-healing first-class). The deployment surface never changed: paste a prompt, provide a task, let the instance run.

## The self-healing loop

The ORA patches itself during live runs. When a spawned agent catches a reproducible failure mode that the current prompt doesn't handle, the runner:

1. Stops propagation at the event boundary
2. Writes a CONCERN note to the blackboard
3. Opens the changelog and appends a new I-v6-N entry (Caught at / Symptom / Root cause / Fix applied / Severity / Lesson)
4. Re-audits the proposed patch against anti-predictions A-1 through A-4
5. Applies the patch to the prompt
6. Logs the application
7. Resumes the cycle, applying the patched discipline to the artifact that surfaced the failure
8. Writes a commit memo to the blackboard

This discipline was born from the H4 closure run (April 2026), where the R.D.1 Critic caught an inference-from-source error that the existing I-7 backward-verification discipline didn't catch. The runner patched Step 5.5 Way 1 in place (I-v6-1), the revision Agent validated the patch inline, and the patch was committed to the bundle. The healing discipline was then itself patched into the prompt as a first-class feature (I-v6-2) — a recursive self-improvement loop.

As of v8, the healing log contains 5 entries (I-v6-1 through I-v6-5), each a failure mode the bundle learned to prevent from a live run. The anti-overfit discipline ensures the healing doesn't overfit: patches must pass A-1 through A-4, must be additive (no removal in-run), and must cite empirical grounding.

---

*The ORA is a researcher encoded as text. Its patterns were extracted from three successful manual runs via a 5-phase mining pipeline. Its anti-overfit discipline prevents those patterns from overfitting to one user or one domain. Its deployment is four lines. Its self-healing loop grows the bundle's repertoire with every run. The runner is honest-first. The credibility of the programme is the credibility of its kill list.*
