# ORA bundle v6 — README

*v6 is a re-packaging of v5's content into a shape that actually runs inside Claude Code. v3's deployment surface is preserved exactly: open a Claude Code session, paste or reference `01-the-prompt.md`, provide a deliverable path and an output directory, let the Claude instance become the runner. No scripts, no middleware, no telemetry daemons, no launcher automation.*

*The content is the same as v5's: 4 GREEN Layer-L-mined signatures (P4 ledger-write, P5 resume protocol, P7 yes-and flow protection, P8 cross-domain analogue lookup), the anti-overfit discipline, the walk-back contract, the 9 pre-registered predictions, the RED / YELLOW deferral list, the subgrouping language, the mining provenance. Only the packaging changed.*

---

## 1. Quick start

To run v6 in a Claude Code session:

```
1. Open a new Claude Code session.
2. Paste or reference: ora-bundle-v6/01-the-prompt.md
   (You can either paste the contents at the top of your first user message,
   or reference the file and let Claude read it via the Read tool. Both work.)
3. Provide the deliverable file path, e.g.:
   "deliverable is /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/04-closing-my4.md"
4. Provide the output directory path, e.g.:
   "output directory is /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4/"
5. Let the Claude instance read the prompt and become the runner.
```

That is the entire deployment story. No setup steps. No launcher scripts. No external processes. No cache breakpoint configuration. The Claude instance reads the prompt, internalizes the 19 operational signatures (15 from v3 + 4 from v6 Layer L mining), reads the deliverable, creates or reads the blackboard at `<run-dir>/blackboard.md`, and begins cycles.

v6 inherits v3's deployment model exactly. If you have run v3 before, v6 runs the same way. If you have not run v3 before, the steps above are everything.

---

## 2. What v6 does that v3 does not

| Signature | Trigger | Action |
|---|---|---|
| **16 (P4)** — Ledger-write reflex | User issues a write directive (explicit or implicit) with a path | Runner writes the file in a single Write call on the same turn |
| **17 (P5)** — Resume re-anchor | User returns from a ≥30 min absence with a resume marker | Runner reads the most recent ledger and produces a 3–5 line "where we left off" summary before answering |
| **18 (P7)** — Yes-and flow protection | User has affirmed 3+ consecutive turns without correction | Runner suppresses confirmation questions in the next response and commits to producing. 5-turn cooldown. |
| **19 (P8)** — Cross-domain analogue surfacing | User makes a cross-domain reference ("just like X", "comparable to Y") | Runner locates the referenced thing, reads 30–100 lines, surfaces a 1–3 sentence summary before continuing |

For everything else, v6 behaves exactly like v3. The 4 new signatures are *additive enhancements*, not replacements.

---

## 3. What v6 does NOT do

Per the anti-predictions in `06-anti-overfit-discipline.md §3`:

- ❌ No closure-event detector (S1 was RED — overfit risk, 12 instances / 3 sessions with 6 duplicates)
- ❌ No G-lexicon literal triggers ("first move", "for life", "M4 x CP2", "we are gonna be famous")
- ❌ No tier-1 prioritization tracker (S14 was YELLOW, deferred to v6.1)
- ❌ No driver-vs-steering mode switch (M1 YELLOW, deferred to v6.1)
- ❌ No soft-lock 2-turn delay (M2 YELLOW, deferred to v6.1)
- ❌ No closure dwell-time parameter (S5 YELLOW, concept adopted without a magic number)
- ❌ No claims of "% improvement" over v3 or v5 (no baseline measurement)
- ❌ No claims of universal applicability ("all users", "any researcher")

v6.0 is the minimum viable encoding of the strongest Layer L evidence. The 4 GREEN signatures have ≥27% session coverage in the mined corpus, clear universal mechanisms, and low lexical dependence on any specific user's vocabulary.

---

## 4. The walk-back contract

After 5–10 fresh v6 sessions, the 9 pre-registered predictions in `06-anti-overfit-discipline.md §5` are scored against the runner's end-of-session self-reported notes collected via the protocol in `§6` of that file:

| Result | Action |
|---|---|
| ≥7 ✅, ≤2 ❌ | Ship v6.0, consider v6.1 with YELLOW patches |
| 4–6 ✅, 3–4 ❌ | Patch failing predictions in place, retest before v6.1 |
| ≤3 ✅, ≥5 ❌ | **Walk back to v3** by re-pasting v3's `01-the-prompt.md` instead of v6's — same deployment surface, one-paste revert |

The walk-back option is non-negotiable. v3 stays alive throughout v6 evaluation precisely so this option is executable.

---

## 5. File index

### Runtime files (the runner reads these)

| File | Lines | Purpose | Load when |
|---|---:|---|---|
| `01-the-prompt.md` | ~1235 | The main runner prompt — 19 operational signatures, blackboard §A–§O, 6 primitives, 6 agent roles, 6-step method loop, §10 Opus 4.6 specialization, §13 closure ritual, §14 conventions. Inherits all 11 v3 patches (I-1 through I-11). | Always — this is what the runner loads at session-open |
| `03-synthesis-spawn.md` | 240 | Synthesis agent spawn template — used at wave boundaries and difficulty-collapse events. Byte-for-byte inherited from v3. | When dispatching Synthesis |
| `04-closure-templates.md` | 637 | The 5-file closure ritual templates (moment, reflection, corrections, resume, digest). Byte-for-byte inherited from v3. | At programme-close |
| `05-framework-tools.md` | 348 | Inventory of the framework's compiled master files with the selective-inclusion table. Byte-for-byte inherited from v3. | When spawning Author, Critic, or Synthesis |

### Design documentation (read for context, not loaded at runtime)

| File | Lines | Purpose |
|---|---:|---|
| `README.md` | ~250 | This file — entrypoint, deployment story, file index |
| `02-rationale.md` | ~470 | The design doc for v3 + the new §13 "v6 additions and provenance" |
| `06-anti-overfit-discipline.md` | ~350 | Governance document for future v6 patch rounds. Anti-predictions, walk-back rule, pre-registered predictions, runner self-reporting protocol, RED / YELLOW deferral list, mining provenance |
| `07-changelog-v5-to-v6.md` | ~320 | The re-packaging changelog — what was preserved from v5, what was dropped, what was added, and why v6 exists |
| `AUDIT.md` | ~150 | Re-run of the 4 anti-predictions against v6's final bundle. Verdict at ship time: all 4 pass. |

### Inherited context (outside this bundle)

| File | Purpose |
|---|---|
| `ora-bundle-v3/` (5 files) | v3 bundle — immediately available as the walk-back target |
| `ora-bundle-v5/mining/phase1–5-*.md` | The Layer L mining archive — raw evidence for v6's 4 new signatures |
| `paper26-bsd/strategy/06-closing-my4-report.md` | The BSD MY4 run report — empirical demonstration that the v3 shape works in Claude Code |
| `11-ora-bundle-v3--closing-my4.md` | v3's dogfooding log — 11 in-run patches (I-1 through I-11) with per-issue entries |

---

## 6. Versioning

| Version | Status | Rationale |
|---|---|---|
| **v3** | **Active, control bundle, walk-back target** | Original release, proven end-to-end on BSD MY4, 11 patches applied |
| v4 | Interim, not the comparison baseline | Existed briefly, never compared against v5 or v6 |
| v5 | Archived (content preserved, packaging wrong-shaped) | Contained the Layer L mining and the anti-overfit discipline but assumed infrastructure that does not exist in Claude Code |
| **v6.0** | **Current, runs on paste-the-prompt deployment surface** | 4 GREEN signatures as runner-internal disciplines, anti-overfit discipline in meta-file, walk-back one-paste-revert |
| v6.1 | Future — adds YELLOW patches if v6.0 telemetry confirms them | After 5–10 sessions of runner self-reported notes, score predictions, decide |
| v6.2+ | Speculative — fresh mining on v6.0 runs | Requires a new mining round, re-audit, new pre-registered predictions |

v3 stays alive until v6 passes the behavioral test (the 9 predictions). Until then, v3 is the walk-back option one paste away.

---

## 7. Honest limitations (subgrouping language)

v6 is a *subgroup-level* tool, not a *universal* one. The mining data was **N=1** — one user, one project domain (mathematical physics / number theory), one LLM tool (Claude Code), one week (April 4–11, 2026), only success runs (no failure cases mined).

v6 is optimized for:

- ✅ Multi-week mathematical / physics / CS research with heavy fanout to subagents
- ✅ Frequent compaction concerns and explicit ledger management
- ✅ Sustained focus on a single proof or unification claim
- ✅ Users who explicitly manage context drift

v6 is NOT optimized for:

- ❌ Single-shot questions or short conversations
- ❌ Short conversations without fanout
- ❌ Domains far from math / physics / CS
- ❌ Users who don't write ledger files

A different user, a different domain, or a different work shape should not expect v6 to help. Use v3 instead — v3 is project-agnostic and has no Layer-L-mined tempo assumptions. v6 is v3 plus 4 additional disciplines that help the specific kind of work above.

---

## 8. How to deploy v6 to a fresh research run

Concrete example matching the user's actual invocation pattern:

```
Open Claude Code.

First user message:

---
Follow your instructions from
/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v6/01-the-prompt.md

The brief (deliverable) is
/Users/gsix/quantum-geometry-in-5d-latex/paper<N>/strategy/<deliverable-name>.md

Output directory is
/Users/gsix/quantum-geometry-in-5d-latex/paper<N>/<run-name>/

Begin.
---
```

The Claude instance reads `01-the-prompt.md` end-to-end, internalizes the 19 signatures, reads the deliverable, creates or reads `<output-dir>/blackboard.md`, and starts cycles. At session-end, the runner writes `<output-dir>/v6-prediction-notes.md` with one line per patch fire (see `06-anti-overfit-discipline.md §6`).

The runner is autonomous from the first cycle — it detects continuous-run mode from the invocation pattern (v3 patch I-4) and applies the full 9-layer drift defense, the 5-file closure ritual, the §O section change log for delta reads, and everything else v3 specifies.

---

## 9. Where to start reading

If you are a **user running v6 for the first time**, you only need to know steps 1–5 in §1 above. Everything else is self-sufficient.

If you are a **contributor proposing a patch to v6**, read in this order:
1. `06-anti-overfit-discipline.md` — the governance document
2. `07-changelog-v5-to-v6.md` — what changed and why
3. `AUDIT.md` — the anti-prediction audit format
4. `02-rationale.md §13` — the v6 additions provenance
5. `01-the-prompt.md §2 Signatures 16–19` — the new signatures
6. `ora-bundle-v5/mining/phase5-signatures.md` — the mining archive

If you are the **Claude instance loading v6 as the runner**, read `01-the-prompt.md` end-to-end. Everything else is referenced from there.

---

*End of `README.md`. Next file in reading order is `01-the-prompt.md` for the runner, or `06-anti-overfit-discipline.md` for a contributor.*
