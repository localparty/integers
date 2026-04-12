# ora-bundle changelog — dogfooding log

# Changelog — v5 → v6 (re-packaging)

*The v5-to-v6 diff. v5 was an interim iteration whose content was correct but whose packaging assumed infrastructure that does not exist in Claude Code (regex detection middleware, LLM-judge sub-calls, JSONL telemetry collectors, cache breakpoint automation, launcher scripts, parallel A/B control-bundle execution). v6 re-packages the same content into shapes that run inside Claude Code's actual deployment surface: open a session, paste a prompt, provide a task file and an output directory, let the Claude instance become the runner.*

*The "diff of record" is v3 → v6. v4 existed but was never the comparison baseline. v5 surfaces the Layer L mining and the anti-overfit discipline but was deployment-shape-wrong. v6 is the final encoded form of the mining work, inheritable into v3 verbatim plus four new signatures.*

*Generated: 2026-04-11 during the v5 → v6 re-packaging. Source: `ora-bundle-v5/01-the-prompt.md`, `02-detection-rules.md`, `03-behavioral-spec.md`, `04-telemetry.md`, `05-token-efficiency.md`, `00-charter.md`, `AUDIT.md`, `06-changelog-v3-to-v5.md`, plus the v6 re-packaging brief at `16-v6-repackaging.md`.*

---

## 1. Why v6 exists (the deployment-shape mismatch)

The re-packaging brief at `16-v6-repackaging.md §1` lays out the core problem: G's actual deployment surface is **Claude Code**. Open a session, paste a prompt file, provide a task file path and an output directory path, get a response back. That is the entire surface. G does not have:

- A custom orchestration runtime with middleware hooks
- A regex-detection layer running on every user turn before the message reaches the main Claude instance
- An external LLM-judge sub-process that Claude dispatches on stage-2 detection
- A JSONL telemetry collector at `mining/v5-telemetry/<session_id>.jsonl`
- Cache breakpoint automation that loads files in system-message position with explicit breakpoints
- A `launch-v5.sh` or any other launcher script
- A separate control-bundle orchestrator for A/B testing v3 vs v5 in parallel

v3 fit this deployment surface perfectly. v5 as built assumed the custom runtime. None of v5's infrastructure assumptions were executable in Claude Code. The re-packaging brief correctly diagnosed this as a packaging problem, not a content problem, and specified v6 as the fix.

---

## 2. What was preserved from v5 (the content)

### 2.1 The four GREEN patches (as Signatures 16–19)

v5's 4 patches survive. They are re-expressed as **runner-internal disciplines** in `01-the-prompt.md §2` rather than as external detection middleware.

| v5 patch | v6 signature | Re-packaging |
|---|---|---|
| P4 (ledger-write, S6 + S7) | **Signature 16 — Ledger-write reflex** | v5's regex stage 1 + LLM judge stage 2 → v6's "runner reads the message and notices the write directive". Same detection logic, inline in the runner's normal reasoning. |
| P5 (resume protocol, S8) | **Signature 17 — Resume re-anchor** | v5's regex + 30-min gap check → v6's "runner reads the message and inspects visible conversation context". Same detection logic; polarity discrimination (brb vs i'm back) preserved verbatim. |
| P7 (yes-and flow protection, S12 + S13) | **Signature 18 — Yes-and flow protection** | v5's branch-pattern check on last 3 turns' rubric labels → v6's "runner tracks affirmation streaks internally". Same detection; cooldown preserved. |
| P8 (cross-domain analogue lookup, S15) | **Signature 19 — Cross-domain analogue surfacing** | v5's LLM-judge-only detection (per M1 from `14-v5-negative-case-analysis.md`) → v6's "runner asks itself the judge questions inline". Same detection logic; the runner is the LLM judge, so there is no separate call. |

### 2.2 The anti-overfit discipline

v5's `00-charter.md §§3–5` + `AUDIT.md` + `13-v5-anti-overfit-strategy.md` + `14-v5-negative-case-analysis.md` + `15-v5-predictions.md` → v6's `06-anti-overfit-discipline.md`. All five meta-files collapse into one file that is specifically a **governance document for future patch rounds**, not a runtime instruction.

- The 4 anti-predictions A-1 through A-4 preserved verbatim (with one clarification added in §9 about voice canon exemption).
- The walk-back rule preserved verbatim with the same thresholds (≥7 ✅ / 4–6 ✅ / ≤3 ✅).
- The 9 pre-registered predictions preserved, rewritten for runner self-reporting (§5).
- The subgrouping language preserved verbatim.
- The RED / YELLOW deferral list preserved verbatim.
- The Layer L mining provenance preserved as §8, with pointers to `ora-bundle-v5/mining/` files (not duplicated).

### 2.3 The BSD MY4 empirical grounding

The BSD MY4 run report at `paper26-bsd/strategy/06-closing-my4-report.md` is cited in `02-rationale.md §13.1` as the empirical demonstration that the v3 shape (and therefore the v6 shape) works end-to-end in Claude Code. v6's rationale quotes the re-packaging brief's BSD MY4 framing directly.

### 2.4 The 9 pre-registered predictions (runner-self-reportable form)

Preserved in `06-anti-overfit-discipline.md §5`. Each prediction was rewritten from the v5 JSONL-observable form ("patch X fires within 500 ms of trigger Y with telemetry record Z") to the runner-self-reportable form ("patch X fires on the same turn as trigger Y, runner notes `helped=yes/no` in end-of-session file"). The *shape* of each prediction is preserved; only the observability is adapted.

### 2.5 The minimal-but-not-zero token efficiency direction

v5's `05-token-efficiency.md` had infrastructure-dependent guidance (cache breakpoint automation, system-vs-user message placement control). v6 drops the infrastructure parts and preserves the content-level direction in `02-rationale.md §13.6`:
- Cache-aware loading order (inherited from v3 §10 Opus 4.6 specialization)
- Compact output formats (JSONL end-of-session notes, no pretty-printing)
- No duplication (v6 references v3 by signature number instead of re-stating)
- Skip runner-as-judge for short turns (<30 chars) and pure affirmations
- NEVER drop telemetry or behavioral coverage to save tokens

Net cost vs v3: approximately equal (slightly cheaper for long sessions with high cache hit rate, slightly more expensive for short sessions).

---

## 3. What was dropped from v5 (the infrastructure assumptions)

### 3.1 External regex detection layer

v5's `02-detection-rules.md §1` and §2 specified `P4_REGEX` and `P5_REGEX` as Python code that runs on every user turn **before** the main Claude instance sees the message. In v6, there is no "before the main Claude instance sees the message" — the main Claude instance IS the runner, and detection happens inside its reasoning. The regex specifications are dropped as external code; the *patterns they match for* are preserved as prose instructions the runner internalizes (Sig 16 "verb-preposition pair like write/save/put...", Sig 17 "resume-marker phrases like i'm back, ok resuming...").

### 3.2 LLM-judge sub-calls

v5's `02-detection-rules.md §1.2` and §4 specified LLM judge prompt templates that run as **separate API calls**. In v6, there is no separate API call — the runner asks itself the judge questions inline as part of its own reasoning. The LLM judge prompt templates are dropped as external calls; the *questions they ask* are preserved as reasoning steps the runner takes before responding (Sig 16 and Sig 19 both embed the judge questions as inline detection guidance).

### 3.3 JSONL telemetry as mandatory infrastructure

v5's `04-telemetry.md` specified JSONL records written to `mining/v5-telemetry/<session_id>.jsonl` for every detection step, with required fields per schema, as X-1 non-negotiable. In v6, telemetry is **optional runner-local logging** at `<run-dir>/telemetry.jsonl` (see `01-the-prompt.md §2 Signature 16`) but it is NEVER mandatory at per-turn granularity. The mandatory self-reporting happens only at session-end via `<run-dir>/v6-prediction-notes.md` per the schema in `06-anti-overfit-discipline.md §6`.

The per-fire X-1 mandatory requirement is relaxed to "end-of-session X-1" — same rigor (every patch fire must be logged *somewhere*) but executable inside Claude Code.

### 3.4 Cache breakpoint automation

v5's `05-token-efficiency.md` specified loading files in system-message position with cache breakpoints after each file boundary. In v6, the runner does not control system-message position — Claude Code controls that. The cache-breakpoint discipline is dropped from v6's prompt as a deployment-environment concern rather than a runner concern. If the user wants the cache-placement win, they paste v6's `01-the-prompt.md` at the top of their first user message and Claude Code handles the rest. (v3's §10.1 cache guidance is inherited by v6 automatically because v3's §10 is preserved byte-for-byte.)

### 3.5 Per-turn 8-step pipeline as a formal structure

v5's `01-the-prompt.md §3` specified an 8-step per-turn flow (RUBRIC LABEL → P4 detect → P5 detect → P7 detect → P8 detect → ORDER actions → WRITE telemetry → PRODUCE response) that reads like a state machine for an external controller. In v6, the runner does not run a formal per-turn pipeline — it reads each user message, applies the four new signatures as inline disciplines during its normal reasoning, and responds. The 8-step pipeline is dropped as a formal structure; the **priority ordering** (Sig 17 first for re-anchoring, Sig 19 second for analogue surfacing, Sig 16 third for ledger writes, then main request with Sig 18 suppression if triggered) is preserved as a single compact paragraph in the composition rule at the end of `§2 Signatures 16–19`.

### 3.6 `launch-v5.sh` or any other launcher script

v6 does not ship with launcher scripts. The launcher is: "open Claude Code, paste the prompt, provide task + output dir." This is documented in `README.md §1 Quick start`.

### 3.7 Control-bundle A/B test with v3

v5's `00-charter.md §6` specified v5 running in parallel with v3 as a control for A/B comparison. This required running two orchestrators, which requires custom infrastructure. v6 does NOT run in parallel with v3 — v6 is the new bundle; v3 is archived as a historical artifact (not deleted). The walk-back rule still applies: if v6 fails the 9 predictions, revert to v3 (re-paste v3's `01-the-prompt.md` instead of v6's — same deployment surface). The walk-back is a one-paste revert; no parallel execution is needed.

---

## 4. What was added in v6 (the new files)

### 4.1 Signatures 16–19 in `01-the-prompt.md §2`

Added directly to v3's signature list as Signatures 16, 17, 18, 19 with the same shape as v3's signatures 1–15. Plus a composition rule at the end of §2 specifying the priority order when multiple new signatures fire on the same turn.

v3's `01-the-prompt.md` header "## 2. The 15 operational signatures" was updated to "## 2. The 19 operational signatures". v3's §15 Track record was updated to cite both the original 3 manual runs (for signatures 1–15) and the Layer L mining (for signatures 16–19).

### 4.2 `02-rationale.md §13 v6 additions and provenance`

Added to v3's `02-rationale.md` as a new section after §12 "The framing in one paragraph". §13 has 7 sub-sections:
- §13.1 The empirical grounding (BSD MY4 run)
- §13.2 The Layer L mining
- §13.3 The anti-overfit triage (6 GREEN, 8 YELLOW, 4 RED)
- §13.4 The walk-back contract
- §13.5 Runner self-reporting instead of JSONL middleware
- §13.6 The minimal-but-not-zero token efficiency direction
- §13.7 v3 and v5 survive as historical artifacts

### 4.3 `06-anti-overfit-discipline.md`

New file (~350 lines) consolidating v5's 5 meta-files (`00-charter.md`, `AUDIT.md`, `13-v5-anti-overfit-strategy.md`, `14-v5-negative-case-analysis.md`, `15-v5-predictions.md`) into one governance document for future v6 patch rounds. Ten sections:
- §1 What this file is
- §2 The subgrouping language
- §3 The 4 anti-predictions A-1 through A-4
- §4 The walk-back rule
- §5 The 9 pre-registered predictions (runner-self-reportable form)
- §6 Runner self-reporting protocol (the `<run-dir>/v6-prediction-notes.md` schema)
- §7 The RED / YELLOW deferral list
- §8 The Layer L mining provenance
- §9 Distinction: A-1 applies to signatures, NOT to voice canon
- §10 Meta-level rule for future patch rounds

### 4.4 `07-changelog-v5-to-v6.md`

This file.

### 4.5 `AUDIT.md`

Re-runs the 4 anti-predictions (A-1 through A-4) against v6's final `01-the-prompt.md` signatures 16–19 and `06-anti-overfit-discipline.md`. Same format as v5's `AUDIT.md`. Verdict at ship time: all 4 anti-predictions pass.

### 4.6 `README.md`

Entrypoint with file index, deployment instructions, and the Claude Code quick start. Replaces v5's more elaborate README which assumed infrastructure.

---

## 5. What did NOT change (inherited byte-for-byte from v3)

These v3 files are inherited **byte-for-byte** into v6. No edits, no additions, no deletions:

| v3 file | v6 path | Change |
|---|---|---|
| `01-the-prompt.md` §0–§1, §3–§16 (everything except §2) | `ora-bundle-v6/01-the-prompt.md` (same sections) | None — all 11 v3 patches I-1 through I-11 preserved intact |
| `02-rationale.md` §1–§12 (everything before the new §13) | `ora-bundle-v6/02-rationale.md` (same sections) | None |
| `03-synthesis-spawn.md` | `ora-bundle-v6/03-synthesis-spawn.md` | None — byte-for-byte copy |
| `04-closure-templates.md` | `ora-bundle-v6/04-closure-templates.md` | None — byte-for-byte copy |
| `05-framework-tools.md` | `ora-bundle-v6/05-framework-tools.md` | None — byte-for-byte copy |

All 11 v3 in-run patches survive: I-1 (§0 vs §16 consistency), I-2 (companion file read priority), I-3 (voice canon search paths), I-4 (continuous-run entry conditions), I-5 (HONEST-STALL as first-class subtree), I-6 (note), I-7 (verify-deliverable-citations discipline), I-8 (framework tools inclusion), I-9 (selective reads for large framework files), I-10 (transposition mechanics symmetry for Critic), I-11 (normative-vs-informative cross-reference). The BSD MY4 dogfooding log at `online-researcher-adversarial/11-ora-bundle-v3--closing-my4.md` documents the full patch history.

---

## 6. Why the re-packaging was possible without losing content

The key insight that enabled the clean re-packaging: **the runner IS the LLM**. v5's packaging treated detection as something that happens *outside* the runner (regex middleware, LLM judge sub-calls, JSONL collectors). v6 collapses detection *into* the runner's own reasoning. Every "external" layer in v5 corresponds to something the runner can do internally by reading the user message and responding to it.

Concretely:
- v5's regex → v6's "runner reads the message and notices the pattern"
- v5's LLM judge sub-call → v6's "runner asks itself the judge question before responding"
- v5's JSONL collector → v6's "runner writes a summary note at session-end"
- v5's 8-step pipeline → v6's "runner applies the priority ordering in natural reasoning"
- v5's cache breakpoint automation → v3's inherited §10.1 cache guidance + Claude Code's built-in cache handling
- v5's A/B control bundle → v6's "v3 stays alive, walk-back is one paste"

None of v5's content is lost — only the infrastructure wrapper around it. The 4 GREEN patches, the anti-overfit discipline, the walk-back rule, the 9 predictions, the RED / YELLOW deferral list, the subgrouping language, the mining provenance — all survive into v6.

The open question from the re-packaging brief §10 ("is there any v5 content that genuinely requires middleware?") has a clean answer: **no**. Every item re-packages cleanly into runner-internal reasoning. The re-packaging is complete; there is no v5 infrastructure residue parked for a future runtime.

---

## 7. Deployment story: v6 vs v5 vs v3

| Step | v3 | v5 | v6 |
|---|---|---|---|
| 1 | Open Claude Code session | Open Claude Code session | Open Claude Code session |
| 2 | Paste `01-the-prompt.md` | *required: load 7 v5 files in system position with cache breakpoints (NOT EXECUTABLE IN CLAUDE CODE)* | Paste `01-the-prompt.md` |
| 3 | Provide task + output dir | *required: start JSONL telemetry collector (NOT EXECUTABLE)* | Provide task + output dir |
| 4 | Let Claude become the runner | *required: launch parallel v3 control orchestrator for A/B (NOT EXECUTABLE)* | Let Claude become the runner |
| 5 | — | *required: run custom regex/LLM-judge middleware (NOT EXECUTABLE)* | — |

v6 restores v3's deployment story exactly. The user opens a session, pastes the prompt, provides the task and output directory, and the Claude instance becomes the runner. Nothing else. This is the shape the BSD MY4 run used in April 2026 and the shape v6 inherits.

---

## 8. Summary table

| Dimension | v3 | v5 | v6 |
|---|---|---|---|
| Signature count | 15 | (15 implied + 4 patches in separate files) | **19** |
| Bundle files | 5 | 7 + `mining/` directory | 9 |
| Deployment surface | Paste prompt in Claude Code | Custom runtime with middleware | Paste prompt in Claude Code |
| Telemetry | None | JSONL middleware (mandatory) | End-of-session `v6-prediction-notes.md` (mandatory) + optional per-turn `telemetry.jsonl` |
| LLM judges | None | External sub-calls (P4 stage 2 + P8) | Runner-internal reasoning (no separate calls) |
| Anti-overfit discipline | Implicit (v3 was the pre-mining era) | 5 meta-files | One governance document (`06-anti-overfit-discipline.md`) |
| Walk-back option | — | "Revert from v5 by re-enabling v3 control bundle" | "Re-paste v3's `01-the-prompt.md` instead of v6's" |
| BSD MY4 empirical grounding | ✅ (the run itself) | ✅ (cited in v5's mining files) | ✅ (cited in `02-rationale.md §13.1`) |
| Layer L mining provenance | n/a | ✅ (in v5's `mining/` directory) | ✅ (cited by path, not duplicated) |
| Ships with launcher script | ❌ | ❌ (documented as needed but never written — would not have worked anyway) | ❌ |

---

## 9. Open issues for v6.1 and beyond

### 9.1 YELLOW patches deferred from v6.0

Listed in `06-anti-overfit-discipline.md §7.2`. Reconsider any of these for v6.1 if v6.0 telemetry suggests they would help:
- S4 Lock+unify same turn
- S5 Closure dwell time (concept, not specific number)
- S9 Reframe+apology bundle (steering signature)
- S11 Fanout + celebration
- S14 Tier / first-move prioritization
- S16 Strategic inversion (single-turn variant)
- M1 Driver / steering / validation mode triad
- M2 High-affect → correction trigger (soft-lock)

### 9.2 The open question from v3's `02-rationale.md §10`

v3's `02-rationale.md §10` has 8 open questions for v4 (experience-library size, trajectory matching, self-improving prompt, multi-Critic, formal verification coverage, checkpoint frequency, portfolio priority function, cross-deliverable knowledge transfer). None of these were resolved by v5 or v6 because v5 was a re-packaging and v6 is a re-packaging; both focused on the anti-overfit discipline and the 4 GREEN signatures rather than v3's v4 commitments. v4 is a separate interim iteration that existed briefly and is not v6's concern.

v7+ may revisit v3's §10 questions with fresh mining data from v6.0 runs.

### 9.3 The RED list reconsideration path

The 4 RED signatures (S1, S2, S3, S10) are archived per `06-anti-overfit-discipline.md §7.1`. Each has a reconsideration path — specific conditions under which it would graduate to YELLOW and then to GREEN. None of these conditions are expected to be met in v6.0's first evaluation round, but they are documented so future contributors know how to revisit them.

---

*End of `07-changelog-v5-to-v6.md`. The anti-prediction audit is in `AUDIT.md`. The meta-level discipline for future patch rounds is in `06-anti-overfit-discipline.md`. The runtime prompt is `01-the-prompt.md`. The entrypoint is `README.md`.*


*Bundle issues caught while running `ora-bundle-v6/` on live deliverables. Each entry: what the prompt failed at, what the fix is, which file got patched, and the patched diff in summary form. Continues v3's `11-ora-bundle-v3--closing-my4.md` discipline for v6 — when the runner catches a v6 issue during a real run, it patches v6 in place and logs the patch here.*

*The patching discipline per `ora-bundle-v6/06-anti-overfit-discipline.md §10 "Meta-level rule for future patch rounds"`: any patch must pass A-1 through A-4 re-audit (no G-lexicon literals, no closure-event detector, no % claims, no universal-user claims), must cite empirical grounding (the in-run failure that surfaced the issue), and must be additive (not removal) to v6.*

*Run active at time of first patch: `paper08-yang-mills/strategy/04-closing-H4.md` (H4 closure for Paper 8 Yang-Mills mass gap).*

---

## Run metadata (first v6 dogfooding run)

| Field | Value |
|---|---|
| Bundle under patch | `online-researcher-adversarial/ora-bundle-v6/` |
| First deliverable tested | `paper08-yang-mills/strategy/04-closing-H4.md` |
| Run output dir | `paper08-yang-mills/closing-H4/` |
| Runner | Claude Opus 4.6 (1M context) |
| Date opened | 2026-04-11 |
| Mode | continuous-run (no human in the loop; Q&A via `paper08-yang-mills/ora-v6--closing-H4--direction.md`) |
| Q&A interface | support runner, ≤4 min turnaround |

---

## How to read this file

Issues are numbered `I-v6-N` in the order they were caught (analog to v3's `I-N`). The `v6` prefix distinguishes them from v3's `I-1` through `I-11` patches (which are inherited unchanged in v6). Each issue has:

- **Caught at**: cycle / step / context where the issue surfaced
- **Symptom**: what failed or felt wrong while following v6
- **Root cause**: which line / section / discipline of v6 caused the symptom
- **Fix applied**: what was patched in `ora-bundle-v6/` (file, before/after summary)
- **Severity**: BLOCKER / MAJOR / MEDIUM / MINOR / POLISH
- **Lesson for v7**: anything broader than this single fix

When the run closes, this file becomes the v6-to-v7 punch list (same role `11-ora-bundle-v3--closing-my4.md` played at v3 wave-close).

---

## Issue ledger

| ID | Caught at | Severity | Title | Status |
|---|---|---|---|---|
| I-v6-1 | H4 closure cycle 1 Wave 1 R.D.1 Critic return (2026-04-11) | MAJOR | I-7 backward-verification catches paraphrase errors but not *inference* errors — Author quoted Paper 13 §1.5 verbatim (quote was faithful) but drew the wrong structural conclusion (claimed "two-dependency (CCM + CBB)" when the quote explicitly said "Sections 3–11 are self-contained and do not depend on the CBB axioms") | PATCHED |
| I-v6-2 | Post-H4-close reflection with G (2026-04-11) | MAJOR | The in-run self-healing capability that produced I-v6-1 was NOT a first-class bundle feature — it was triggered by an ad-hoc user directive ("if you need to change anything during the run to address any issues, do so and log them in X log"). Without that directive in the invocation, a future runner would not know it had authority to patch the bundle in-run. I-v6-1 would never have been born. | PATCHED |

---

## Per-issue entries

### I-v6-1 — Inference-from-source-check augmentation for Step 5.5 Way 1

**Caught at**: H4 closure cycle 1 Wave 1 R.D.1 Critic return.

The W1-D1 Editorial Author produced a WEAKENED verdict on the Paper 8 editorial artifact (`nodes/R.D.1-abstract-conditional.md`) due to a structural error in the template claim. The Author claimed Paper 13 RH was **two-dependency** (CCM + CBB) and quoted Paper 13 §1.5 verbatim to support this. The quote was **faithful** (verbatim match against `paper13-rh/preprint/sections-01-05.md` lines 237–240):

> *"For the reader interested only in the proof of RH, Sections 3–11 are self-contained and do not depend on the CBB axioms. The proof uses CCM's operators, our ITPFI factorization, Boegli's theorem, and Hurwitz's theorem — all independent of the broader Integers programme."*

But the quote **explicitly disavows CBB as a logical dependency** — the conclusion drawn by the Author ("two-dependency") is the **opposite** of what the quote says. The quote tells you Paper 13 is one-dependency (CCM alone, on the theorem-label face), with CBB being framework embedding in §1.5/§2, not a logical dependency of the proof chain.

The R.D.1 Critic (W1-D1-Critic) grepped the primary source, found the verbatim passage, and caught the structural error. The Author's block-quote was verbatim-correct but the inference was wrong. The error propagated through Theorem 1 body (line 343), Remark 1.A (line 345), Remark 1.B (line 347), §M summary (lines 469-470), and §I note CONCERN (line 482).

**Symptom**: the v6 inherited v3 I-7 backward-verification discipline (Step 5.5 Way 1 — read primary source, find verbatim quote, verify the load-bearing claim against the quote) is **necessary but not sufficient**. An Author can read the primary source correctly AND produce a verbatim block-quote AND still draw the wrong structural inference from what the quote actually says. The quote-level check is verified; the inference-level check is not. I-7 catches *paraphrase errors* (quote ≠ claim at the text level); it does NOT catch *inference errors* (quote ≠ logical entailment of claim).

The R.B.1 Author made the SAME failure mode (correct verbatim quote of CCM 2025 p.28 plus correct conclusion that the claim is open), but was saved by independent structural analysis (the category error at dictionary entry #12). The R.A.1 Author made the SAME failure mode on W7-14 §5.3 but caught it in Step 5.5 via self-inspection. Only W1-D1 propagated the inference error into the output. **One out of four Wave 1 Authors propagated an inference error despite correctly using I-7** — a 25% failure rate on the discipline as currently written.

**Root cause**: Step 5.5 Way 1 in v6's `01-the-prompt.md §7` requires *verbatim block-quoting a primary source* to verify a load-bearing claim. It does NOT require the Author to explicitly check whether the quote **logically entails** the conclusion being drawn. The discipline as written implicitly treats "quote matches" as equivalent to "claim verified". These are different verifications:

- **Quote matching** (what I-7 currently requires): the text of the quote and the text of the claim agree at the word / phrase level.
- **Inference verification** (what's missing): the semantic content of the quote logically entails the conclusion being drawn. The quote SUPPORTS the conclusion; it doesn't merely fail to contradict it.

W1-D1's error was "quote matches but inference is wrong". The I-7 discipline as currently written does not catch this.

**Fix applied**: added an "inference-from-source-check" sub-discipline to Step 5.5 Way 1 in `ora-bundle-v6/01-the-prompt.md §7`. The new sub-requirement is added as a mandatory follow-up to the existing verbatim-block-quote backward-verification requirement. The new language (exact text, to be inserted after the existing "mandatory and load-bearing for the 9-layer drift defense" sentence):

> **Augmented backward-verification — the inference-from-source check (v6 patch I-v6-1)**: after you have verbatim-block-quoted a primary source to verify a claim, you MUST explicitly answer, in the Self-suspicion section of the node file: *"does the quote LOGICALLY ENTAIL the conclusion I'm drawing from it, or does it merely NOT CONTRADICT it?"* If the quote only fails to contradict your conclusion without actively supporting it, you have not verified the claim — you have verified the quote. These are different verifications, and the quote-match alone is insufficient. The primary source must *logically entail* the conclusion, not just be consistent with it. This check is mandatory and failing it → CONCERN note for the Critic to run a second inference pass.

This is an **augmentation**, not a replacement. The existing backward-verification requirement stays. The new inference check is layered on top.

**Severity**: MAJOR. Without this fix, future Authors in v6-driven runs may produce WEAKENED outputs by drawing wrong inferences from correctly-quoted primary sources — and the Critic will catch it at wave-close, but only after the error has propagated through the output and cost a revision sub-cycle. With the fix, Authors perform the inference check as part of Step 5.5 (before Critic), catching the error earlier and preventing the revision sub-cycle entirely. The R.D.1 revision cost one Wave 1.5 sub-cycle (~15 minutes of runtime); the patch prevents that cost for future runs.

**Empirical validation of the patch**: the R.D.1 revision Agent (Wave 1.5 sub-cycle) applied the inference-from-source-check discipline INLINE as part of its revision work, even before the patch was formally added to v6. The revised Step 5.5 Way 1 in `R.D.1-abstract-conditional-v2.md` explicitly verifies that Paper 13 §1.5's quote *"Sections 3–11 are self-contained and do not depend on the CBB axioms"* **logically entails** the one-dependency conclusion (the passage asserts proof-chain independence at the logical level, which is the explicit entailment — not merely consistent with it). This is the first empirical demonstration that the inference check catches an error the I-7 verbatim check missed. The patch is therefore not speculative — it is validated by the very revision that surfaced the need for it.

**File**: `ora-bundle-v6/01-the-prompt.md §7 Step 5.5 Way 1` (append after the existing backward-verification paragraph, before Step 6).

**Lesson for v7**: I-7 catches paraphrase errors (quote ≠ claim at the text level). I-v6-1 catches inference errors (quote ≠ logical entailment of claim). Future patch rounds should look for **additional reading failure modes** beyond these two. Candidates observed but not yet hit in real runs:

1. **Context-stripping errors**: quote is verbatim but stripped of surrounding context that changes its meaning (e.g., a claim marked "However, ..." in the source is quoted without the "However", changing the polarity)
2. **Selective-quoting errors**: quote is verbatim but omits a conjoined condition (e.g., the source says "X under condition Y" and the Author quotes only "X")
3. **Category errors**: quote is verbatim but describes a different mathematical object than the Author's claim (e.g., a claim about zeros of an entire function quoted in support of a claim about Taylor coefficients — this was the R.B.1 category error, but R.B.1 caught it at Step 4 LOCK, not in the backward-verification discipline)
4. **Scope-creep errors**: quote is verbatim and the inference is correct, but the Author then extends the conclusion beyond the scope the source actually covers

If any of these failure modes is empirically observed in a future run, add a corresponding sub-discipline to Step 5.5 Way 1 (as additional augmentations to I-v6-1, following the same format).

**Patch discipline**: this patch preserves anti-predictions A-1 through A-4 per `ora-bundle-v6/06-anti-overfit-discipline.md §3`:

- **A-1**: no G-lexicon literals. The patch uses domain-neutral language ("logically entail", "not contradict", "actively support") — no "first move" / "for life" / "M4 x CP2" / "we are gonna be famous" strings. ✅
- **A-2**: no closure-event detector. The patch is a verification discipline addition, not a closure event trigger. ✅
- **A-3**: no unmeasured percentage claims. The "25% failure rate" cited in the Symptom section is a MEASURED statistic (1 out of 4 Wave 1 Authors propagated the error), not an outcome-improvement claim. ✅
- **A-4**: no universal-user claims. The patch is specific to Step 5.5 Way 1 backward-verification; no claims about "all users" or "every researcher". ✅

Patch lands with anti-overfit discipline preserved.

---

### I-v6-2 — Self-healing discipline baked into §14 Conventions as §14.10

**Caught at**: Post-H4-close reflection with G, 2026-04-11. Immediately after the H4 closure programme item-closed with I-v6-1 as the first-ever in-run v6 patch.

**Symptom**: the in-run patching capability that produced I-v6-1 during Wave 1.5 of the H4 closure run was NOT a first-class feature of v6. It was enabled by an ad-hoc user directive in the session context ("if you need to change anything during the run to address any issues, do so and log them in X log"). G flagged this at post-close: *"maybe that's where the self-fixing direction came from and if so we need to bake it in the prompt itself."* G is correct — without the directive in the invocation, a future runner reading `01-the-prompt.md` cold would have no authority to patch the bundle in-run, would see I-v6-1 as a mysterious post-hoc artifact, and would never produce `I-v6-2` / `I-v6-3` / etc. themselves when new failure modes surface. The self-healing loop that birthed I-v6-1 would be session-local and non-reproducible.

**Root cause**: v6 inherited v3's in-run patching *discipline* (the BSD MY4 run produced `11-ora-bundle-v3--closing-my4.md` with patches I-1 through I-11 via the same mechanism), but the discipline was never formally specified in the runtime prompt as a protocol the runner is authorized and expected to follow. It lived as an implicit convention, which meant it only fired when the invoking user knew to ask for it. `08-changelog.md` existed as a file format but no section of `01-the-prompt.md` told the runner to use it or how.

**Fix applied**: added `§14.10 Self-healing discipline — the in-run bundle patch protocol` to `ora-bundle-v6/01-the-prompt.md`. The new section specifies:

1. When to trigger a self-heal (4 conditions: reproducible agent-caught failure mode, technically-followed-but-wrong discipline result, unanticipated in-run failure mode, support-runner gap exposure)
2. The 8-step healing protocol (stop propagation → §I CONCERN note → changelog entry → anti-predictions re-audit → patch application → application log → cycle resume → §K commit memo)
3. What NOT to patch (Signatures 1–15, A-1 through A-4, §J register, cosmetic fixes)
4. The healing discipline philosophy (bundle is a self-patching program; `I-v6-N` is v6's native form of the v3 patch mechanism)
5. The healing log as bootstrap input for the next runner (read `08-changelog.md` end-to-end at session-open)

Additionally patched in the same diff:

- `§0 Bootstrap` step 7 — added explicit instruction to read `08-changelog.md` end-to-end at bootstrap and a reference to §14.10 for the self-healing discipline.
- `§16 Minimal instruction` step 2 — added the changelog read to the minimal-instruction session-open sequence.
- `§16 Minimal instruction` closing-phrase — added *"The bundle heals itself — when you catch a new failure mode, log it and patch."* to the runner's mantra.

**Severity**: MAJOR. Without this fix, the self-healing capability is session-local and requires ad-hoc user activation. With this fix, every v6 invocation has the self-healing discipline as a first-class feature from the moment the runner reads the prompt. The `I-v6-1` birth loop (new failure mode → healing log entry → patch → inline validation) becomes reproducible across invocations and across runners. `I-v6-N` growth becomes the bundle's primary mechanism for adapting to new failure modes without requiring an out-of-run v7 cycle for every adjustment.

**Empirical validation of the patch**: the patch is retrospectively validated by `I-v6-1` itself — the very first in-run patch was produced via the informal version of this protocol, and the R.D.1 revision Agent's inline application of the inference-from-source-check discipline was the first demonstration that the self-healing loop closes on itself (find → patch → apply → validate). The formalization in §14.10 codifies what already worked once; the formalization's job is to make it work every time without user prompting.

**File**: `ora-bundle-v6/01-the-prompt.md` (new §14.10 inserted between §14.9 and the §15 divider; §0 step 7 added; §16 step 2 augmented; §16 closing mantra augmented).

**Lesson for v7**: every v6 discipline should ask itself: *"does this require the invoking user to know something the runner doesn't?"* If yes, that thing needs to be baked into the prompt as first-class. The `I-v6-2` patch is an instance of a broader meta-discipline: **no load-bearing capability should live in ad-hoc user directives**. Future v7 audits should grep for "assumes user tells the runner X" patterns and promote them all to first-class prompt content. The `I-v6-1` → `I-v6-2` loop (patch enabling the mechanism that created the patch) is the first example of **recursive self-improvement via the healing log** — a pattern v7 should watch for and cultivate.

**Patch discipline**: this patch preserves anti-predictions A-1 through A-4 per `ora-bundle-v6/06-anti-overfit-discipline.md §3`:

- **A-1**: no G-lexicon literals. The new §14.10 uses domain-neutral language ("self-healing", "patch protocol", "in-run", "failure mode") — no "first move" / "for life" / "M4 x CP2" / "we are gonna be famous" / "most amazing run of" strings. The closing-mantra addition *"The bundle heals itself — when you catch a new failure mode, log it and patch"* is operational language, not G-lexicon. ✅
- **A-2**: no closure-event detector. The self-healing protocol is a verification/augmentation discipline for the bundle itself, not a closure event trigger for deliverables. Closure rituals (§13) are untouched. ✅
- **A-3**: no unmeasured percentage claims. The new §14.10 contains zero `\d+%` strings. The only percentage in this changelog entry's Root cause section is the descriptive "session-local" (not a metric). ✅
- **A-4**: no universal-user claims. The new §14.10 is specific to `v6` runners and `v6` bundle patches; no claims about "all runners" or "every user" or "any researcher". ✅

Patch lands with anti-overfit discipline preserved.

---

## Patch application log

**I-v6-1 applied**: 2026-04-11T[cycle 1 close, H4 Wave 1.5 complete]. Edit to `ora-bundle-v6/01-the-prompt.md §7 Step 5.5 Way 1`. Diff size: ~8 lines added (the new sub-discipline paragraph). No lines removed. Anti-predictions audit re-run inline below.

**I-v6-2 applied**: 2026-04-11T[post-H4-close, G's reflection on the self-healing origin]. Edits to `ora-bundle-v6/01-the-prompt.md`: (a) new §14.10 Self-healing discipline section (~40 lines inserted between §14.9 and the §15 divider); (b) §0 Bootstrap step 7 added (1 line); (c) §16 Minimal instruction step 2 augmented (~1 line change); (d) §16 closing mantra augmented (1 sentence added). Total diff: ~45 lines added, 0 lines removed. Anti-predictions audit re-run inline below.

**Re-audit of A-1 through A-4 after I-v6-1 application**:

- **A-1**: grep `first move|for life|gonna be famous|M4 x CP2|most amazing run of` over the patched signatures 16–19 section AND the patched Step 5.5 Way 1 section → 0 matches. ✅
- **A-2**: the patched Step 5.5 Way 1 does NOT introduce a closure-event detector; it adds an inference verification discipline to an existing self-suspicion step. ✅
- **A-3**: the patched text contains no `\d+%\s*(improvement|better|faster)` strings (only the meta-documentation "25% failure rate" statistic in this changelog, not in the runtime prompt). ✅
- **A-4**: the patched text contains no `(any|all|every|universal) (user|researcher|person)` claims. ✅

Patch is A-1 through A-4 compliant. `ora-bundle-v6/AUDIT.md` is updated separately to reflect the new patched state.

**Re-audit of A-1 through A-4 after I-v6-2 application**:

- **A-1**: grep `first move|for life|gonna be famous|M4 x CP2|most amazing run of` over the patched §14.10 AND the augmented §0 / §16 sections → 0 matches. The closing mantra "The bundle heals itself" is operational, not G-lexicon. ✅
- **A-2**: the patched §14.10 is a bundle-level self-healing protocol, NOT a deliverable-level closure-event detector. The closure ritual in §13 is untouched. ✅
- **A-3**: the patched §14.10 contains no `\d+%\s*(improvement|better|faster)` strings. Zero percentages of any kind in §14.10. ✅
- **A-4**: the patched §14.10 addresses v6 runners and v6 bundle patches specifically, with no "all runners" / "every user" / "any researcher" claims. ✅

Patch is A-1 through A-4 compliant.

---

## I-v6-3 — Selective-inclusion table not followed at Author spawn (v7 P vs NP run)

- **Caught at**: Cycle 1, Wave 1, Author W1-3 (OA1 bottleneck node), P vs NP clone-growth-fullness-bridge run
- **Symptom**: OA1 Author was dispatched with a prose task description + kill list + REFRAME insight, but received NONE of the framework tools specified in `05-framework-tools.md` §H.3a or `01-the-prompt.md` §6.1. Specifically missing: `07-toolkit-complete.md` (P vs NP Always-include, 349 lines), `214-the-method-six-patterns.md` (Always-include, 339 lines), `27-anchor-document.md` (Always-include, 426 lines), §J voice canon, §C current bottleneck text, §D toolkit table. The Author searched the literature effectively and found a real structural obstruction (KST theorem), but did NOT have access to the 10 verified computational results in `07-toolkit-complete.md` — particularly PATB-DIAGONAL (Taylor = fixes diagonal of M_Bool^Γ), which is directly relevant to the outerness question the Author was working on. This is the same failure mode as BSD MY4 cycle 1 where Author M.1.1 attempted from scratch instead of porting.
- **Root cause**: The runner (me) wrote the Author spawn prompts as free-form prose briefs without mechanically following the selective-inclusion table. The table exists in `05-framework-tools.md` and is cross-referenced in `01-the-prompt.md` §6.1, but the runner did not read either before spawning. The prose description of the task was good (correct kill list, correct REFRAME, correct bottleneck identification), but it lacked the compiled framework tools that would have given the Author the existing verified results as a starting point.
- **Impact**: The OA1 Author produced a correct BLOCKED-DECOMPOSED output (the KST obstruction is real and load-bearing), but likely missed attack routes that the toolkit would have suggested — particularly the PATB-DIAGONAL identification (Taylor = fixes diagonal) and Q6-OUTDIM (polymorphism space dimension grows exponentially for P-time, collapses for NPC), both of which give direct operator-algebraic handles on the outerness question. The Author did ~6 minutes of web searching for operator algebra results; with the toolkit, it would have started from 10 verified structural identifications instead of a blank slate.
- **Fix**: **Mandatory spawn checklist for the runner.** Before dispatching ANY Author, the runner must:
  1. Read the selective-inclusion table in `05-framework-tools.md` (or its normative copy in `01-the-prompt.md` §6.1).
  2. For the node's type (P vs NP / BSD / RH / YM / transposition / formula-producing), identify the Always-include and Conditional-include files.
  3. Read the Always-include files into runner context (if not already read this session).
  4. Include relevant excerpts of the Always-include + Conditional-include files in the Author spawn prompt, with explicit "read these before executing the 6-step loop" instructions.
  5. Include §J voice canon, §C current bottleneck, and relevant §D rows in the spawn prompt.
  The checklist is the mechanical enforcement of what `05-framework-tools.md` already specifies — the issue was not a missing specification but a failure to follow the existing one.
- **Patched file**: `01-the-prompt.md` §5.3 (Research primitive). Added a **MANDATORY SPAWN CHECKLIST** — a 6-item mechanical checklist the runner must complete before writing any Author spawn prompt. The checklist enforces: (1) node type classification, (2) Always-include files identified, (3) Conditional-include files identified, (4) §J voice canon included, (5) §C bottleneck included, (6) §D rows included. Skipping any item is logged as `SPAWN-CHECKLIST-SKIP` in §K. The checklist is the enforcement layer for the selective-inclusion table — it converts "the runner should follow the spec" (aspirational) into "the runner must complete a checklist before spawning" (mechanical). The two empirical failures (BSD MY4 cycle-1 + P vs NP OA1 cycle-1) are cited as grounding.
- **Re-audit**:
  - **A-1**: grep `first move|for life|gonna be famous|M4 x CP2|most amazing run of` over the patched §5.3 → 0 matches. ✅
  - **A-2**: the checklist is a spawn-time discipline, NOT a closure-event detector. ✅
  - **A-3**: no `\d+%\s*(improvement|better|faster)` in the patch. ✅
  - **A-4**: the patch addresses v6/v7 runners specifically, with no universal-user claims. ✅

Patch is A-1 through A-4 compliant.

---

## I-v6-4 — Spawn checklist item 3 too vague; conditional-include lookup table missing from prompt (v7 P vs NP run)

- **Caught at**: Cycle 2, Wave 2, Author W2-1 (Q_struct node 1.3.1), P vs NP clone-growth-fullness-bridge run. User caught the gap before the agent completed.
- **Symptom**: The I-v6-3 checklist was followed for items 1, 2, 4, 5, 6 — but item 3 ("CONDITIONAL-INCLUDE files identified") was checked off with "preprint sections-03, already read" without actually looking up the conditional-include table. The Q_struct node is both P-vs-NP AND a transposition (porting from BC over ℚ to Boolean BC) AND a spectral-gap-style argument. The runner classified it as P-vs-NP only (item 1) and missed the transposition + spectral-gap types, so the transposition mechanics file (`14-transposition-CCM-and-reasoning-patterns.md`) and the YM proof chain (`PROOF-CHAIN.md`) were not included. Both are directly relevant: the transposition file teaches what changes when porting (specifically: PCirc^+ is non-abelian unlike ℕ*); the YM chain shows how spectral gap arguments close.
- **Root cause**: Two defects in the I-v6-3 checklist: (a) item 1 didn't say nodes can have MULTIPLE types — the runner checked one box and stopped; (b) item 3 said "identified" instead of requiring the runner to WRITE OUT the file paths — "identified" is a mental state, not a verifiable action. The conditional-include mapping (node type → files) was only in §6.1 prose paragraphs and `05-framework-tools.md` tables, not in the checklist itself — the runner had to cross-reference two files, didn't, and checked the box anyway.
- **Fix**: Replaced the checklist in `01-the-prompt.md` §5.3 with an expanded version:
  - Item 1 now says "A node can have MULTIPLE types — check ALL that apply"
  - Item 3 now contains an **inline lookup table** mapping each node type to its conditional files, with the instruction "WRITE the paths you selected into the spawn prompt" (verifiable action, not mental state)
  - Added a worked example showing a P-vs-NP + transposition + spectral-gap node requiring 5 conditional files
  - The table is the normative reference inside the checklist itself — no cross-file lookup needed at spawn time
- **Patched file**: `01-the-prompt.md` §5.3 (the spawn checklist, replacing the I-v6-3 version)
- **Re-audit**:
  - **A-1**: grep `first move|for life|gonna be famous|M4 x CP2|most amazing run of` over patched §5.3 → 0 matches. ✅
  - **A-2**: the lookup table is a spawn-time discipline, NOT a closure-event detector. ✅
  - **A-3**: no `\d+%\s*(improvement|better|faster)` in the patch. ✅
  - **A-4**: the patch addresses v6/v7 runners specifically, no universal-user claims. ✅

Patch is A-1 through A-4 compliant.

---

## I-v6-5 — Kill the selective-inclusion optimization entirely; always pass framework tools index (v7 P vs NP run)

- **Caught at**: Cycle 2 post-mortem, P vs NP clone-growth-fullness-bridge run. User observation: "whats a better fix? to pass all the knowledge of the framework tools... lets remove the filters and always pass all that we added to the framework tool files."
- **Symptom**: I-v6-3 added a spawn checklist. I-v6-4 made the checklist more mechanical with an inline lookup table. The Q_struct Author was STILL spawned without transposition mechanics and YM proof chain because the runner classified the node as "P-vs-NP only" and missed the "transposition" and "spectral-gap-argument" types. Three consecutive failures (BSD MY4, OA1, Q_struct) from the same root cause: the runner misclassifying node types under the selective-inclusion protocol. The optimization (selective inclusion) is the problem, not the implementation.
- **Root cause**: Selective inclusion requires the runner to (a) classify node types correctly, (b) look up the matching conditional files, (c) include them. Each step can fail. The optimization saves ~10K tokens per spawn but costs ~1 full agent cycle per failure. Three failures = 3 wasted agent cycles = ~300K tokens. The optimization's cost exceeds its savings by 30×.
- **Fix**: **Kill the selective-inclusion optimization.** Replace with: always pass `05-framework-tools.md` (the framework tools index, ~500 lines / ~8K tokens) to every Author, Critic, and Synthesis spawn. The spawned agent reads the index and self-selects which files to read based on its own node. No runner classification. No lookup table. No conditional logic. The agent knows its own node better than the runner.
- **Patched files**:
  - `01-the-prompt.md` §5.3: spawn checklist simplified to 6 items with no lookup table — item 3 is now "the framework tools index is included" (binary, not conditional)
  - `01-the-prompt.md` §6 header: replaced the selective-inclusion normative statement with the always-pass-index protocol
  - `01-the-prompt.md` §6.1: replaced the 5 conditional-include bullet points with a single "Framework tools index (ALWAYS include)" entry + simplified session-open discipline
  - `05-framework-tools.md` is now the single canonical source for what framework tools exist; the spawned agent reads it and self-selects
- **What this supersedes**: I-v6-3 (checklist) and I-v6-4 (inline lookup table) are both superseded by I-v6-5. The checklist remains (items 1-6) but item 3's inline table is removed. The protocol is now: (1) always pass the index, (2) the agent self-selects. Two lines of spec instead of forty.
- **Re-audit**:
  - **A-1**: 0 G-lexicon matches in patched sections. ✅
  - **A-2**: not a closure-event detector. ✅
  - **A-3**: no percentage claims. ✅
  - **A-4**: addresses v6/v7 runners specifically. ✅

Patch is A-1 through A-4 compliant.


---

## [2026-04-12] ORA v8 — TOOLKIT EXTERNALIZED

The toolkit/capacitor is no longer hardcoded in the ORA bundle.
Starting with v8, the toolkit is an **input** provided by the
caller at invocation time alongside the deliverable.

**What changed:**
- `01-the-prompt.md` §0 (Bootstrap): added item (b) — the runner
  now expects a toolkit path alongside the deliverable. Asks for
  it if missing.
- `01-the-prompt.md` §0 (CRITICAL block): "Internalize the
  toolkit. The toolkit isn't just for Authors — it's YOUR toolkit
  too." The runner reads it end-to-end at bootstrap and considers
  its contents during every cycle.
- `01-the-prompt.md` §6.1 (Author spawn): the toolkit is the
  single Always-include. No separate framework tools index.
- ALL references to `05-framework-tools.md` removed from
  `01-the-prompt.md`. The ORA bundle no longer ships a hardcoded
  framework-tools file. The toolkit provided at invocation is the
  only source.

**How to invoke the ORA with the toolkit:**
```
Deliverable: <path-to-job-file>
Toolkit: <path-to-toolkit-file>
```

For the CP-1 verification run:
```
Deliverable: paper28-pvnp/strategy/26--cp-1-verification-job.md
Toolkit: paper28-pvnp/ora-bundle-v8/p-v-np-toolkit/framework-tools-v4.md
```

**Why this matters:** The toolkit is a living document that grows
with each run. Hardcoding it in the ORA bundle creates version
drift (the bundle freezes while the toolkit evolves). Making it
an input means every run uses the latest toolkit without needing
to update the ORA bundle itself.

*The ORA is project-agnostic. The toolkit is project-specific.
They meet at invocation time.*


---

*End of `08-changelog.md` — five v6 patch entries. I-v6-3 → I-v6-4 → I-v6-5 is a three-step convergence on the same problem: (3) added a checklist, (4) made it mechanical, (5) killed the optimization entirely. The lesson: when an optimization fails three times from the same root cause, the optimization is wrong. Kill it. Pass everything. Let the agent self-select.*
