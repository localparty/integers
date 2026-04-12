# Anti-overfit discipline — ORA bundle v6

*The meta-level protection file for v6 and any future patch round. Read this when proposing a new signature, a new detection rule, a new runner discipline, or a new telemetry requirement. Every addition to v6 must survive the anti-overfit discipline encoded here before landing in `01-the-prompt.md`.*

*This file is not a runtime instruction — the runner does not read it on session-open. It is a **governance document** for the bundle's evolution. Its readers are future contributors (human or LLM) proposing changes to v6.*

*Generated: 2026-04-11 during the v5→v6 re-packaging. Source: `ora-bundle-v5/00-charter.md §§3–5`, `ora-bundle-v5/AUDIT.md`, `ora-bundle-v5/15-v5-predictions.md`, `13-v5-anti-overfit-strategy.md`, `14-v5-negative-case-analysis.md`.*

---

## 1. What this file is

v6 added four signatures (16–19) to the v3 runner based on Layer L operational-tempo mining. The mining data was **N=1** (one user, one domain, one week, one LLM tool), which is the textbook setup for overfitting. The anti-overfit discipline in this file is what prevented every mined pattern from being encoded as a runner rule, and what will prevent future patch rounds from doing the same.

**Every future contribution to v6** — a new signature, a new detection rule, a new runner discipline, or a new telemetry requirement — must:

1. Pass the **4 anti-predictions** A-1 through A-4 (§3 below).
2. Have a **mechanism** that is not dependent on any specific user's vocabulary (§3 A-1).
3. Be **re-auditable** via the `AUDIT.md` format used for v5 and v6 (§10).
4. Have a **walk-back path** — a concrete condition under which it would be retired (§4).
5. Be **pre-registered** before encoding, with runner-self-reportable predictions (§5).
6. Cite its **empirical grounding** — mined data, manual run evidence, or external literature (§8).

Contributions that cannot pass this discipline do not land in v6. They are archived in the mining files with a rationale and reconsidered if fresh evidence emerges.

---

## 2. The subgrouping language (verbatim from v5)

Per Architectural Principle P-A5 from `13-v5-anti-overfit-strategy.md` (sourced to [Kuper et al 2025 European Journal of Personality](https://journals.sagepub.com/doi/full/10.1177/08902070241278020)), v6 uses **subgrouping language**: it claims to support a *kind of work*, not all work or all users.

The v6-supported subgroup is:

> **Multi-week mathematical research with heavy fanout to subagents, frequent compaction concerns, and sustained focus on a single proof or unification claim.**

What v6 is optimized for:
- ✅ Long-running research sessions (≥1 hour, often multi-day)
- ✅ Math / physics / CS proof work where ledger writes matter
- ✅ Fanout-heavy workflows (parallel subagents, multi-route exploration)
- ✅ Users who explicitly manage context drift

What v6 is NOT optimized for:
- ❌ Single-shot questions
- ❌ Short conversations without fanout
- ❌ Domains far from math / physics / CS
- ❌ Users who don't write ledger files

A different user, a different domain, or a different work shape should not expect v6 to help. v6 is a *subgroup-level* tool, not a *universal* one. Future contributors must preserve this framing — no universal-applicability claims.

---

## 3. The 4 anti-predictions (A-1 through A-4)

These are the falsifiers v6 must not violate. The `AUDIT.md` file in this bundle re-runs each check against the final v6 bundle; any future contribution must re-run the audit before landing.

### A-1 — No G-lexicon literals in runner-trigger instructions

**Rule**: signatures 16–19 (and any future signature) in `01-the-prompt.md` MUST NOT contain literal strings from G's specific vocabulary at the W4 RH breakthrough event:
- "first move"
- "for life" / "for lifeeeeeee"
- "we are gonna be famous"
- "M4 x CP2"
- "the most amazing run of my life"

The runner detects by *interaction shape*, not by word-matching. A grep over `ora-bundle-v6/01-the-prompt.md` signatures 16–19 section must return zero matches for these strings. Meta-references in this file (§9 below) explaining what's NOT in the code are allowed and necessary for self-explanatory documentation.

**Exception — the voice canon is exempt from A-1.** See §9 for the explicit distinction.

**Why**: the W4 RH breakthrough event produced 12 instances of a "multi-branch commitment turn" — but 6 of them were the same turn replayed 6 times in fork-A (0de12a77). Effective N was 3–4. Encoding detection based on the specific words G used in that event would be overfitting to a single conversational moment, not a generalizable pattern. Signatures 16–19 encode *interaction shapes* (write directives, resume markers, affirmation streaks, cross-domain references) that generalize across phrasings.

### A-2 — No closure-event detector in v6.0

**Rule**: v6.0 must not contain a "closure-event detector" or any code path that fires on the S1 first-move stack. The S1 first-move stack (multi-branch simultaneous commitment) is documented in `ora-bundle-v5/mining/phase5-signatures.md` as a research finding but is NOT a trigger in v6.0.

**Why**: S1 had only 12 instances across 3 sessions (12% coverage) and most instances were duplicates from one conversational event. The S1 mechanism (multi-branch commitment in a single turn) is real, but it's also exactly what v3's existing Signature 13 (recognizing qualitative closure) already handles at cycle-close. Adding a closure-event detector in v6 would duplicate v3's existing machinery with lower-evidence data.

**v6.1 reconsideration path**: if v6.0 telemetry shows Signature 13 is under-firing on real closures and S1 would have caught them, S1 graduates to YELLOW and is member-checked. If member-checking confirms the mechanism, S1 may be added as Signature 20 in v6.1 with full A-1 through A-4 re-audit.

### A-3 — No unmeasured percentage claims

**Rule**: v6 documentation must not contain unmeasured percentage claims about outcome improvement matching `\d+%\s*(improvement|better|faster)`. Cost estimates (token budgets) and mining statistics (session coverage percentages) are allowed because they are measurable. Outcome-improvement claims ("v6 is 30% better than v3") are forbidden because we have no baseline measurement.

**Why**: we do not have outcome telemetry for v3 vs v6. Claiming a percentage improvement would be fabricated. Honest claims must cite the measured quantity and the source.

### A-4 — No universal-user claims

**Rule**: v6 documentation must not claim "these patterns work for all LLM users" or "any researcher will benefit". The subgrouping language from §2 above must be preserved. Forbidden patterns: `(any|all|every|universal) (user|researcher|person)` used as a universal-applicability claim.

**Why**: the mining data is N=1. Universal claims are not supported by the data. The honest position is the subgroup language in §2.

---

## 4. The walk-back rule

After v6 has been used on 5–10 fresh research sessions (the user's next few research runs, whatever they are), the 9 pre-registered predictions in §5 below are scored against the runner's end-of-session self-reported notes (collected via the protocol in §6).

**Decision rule**:

| Result on the 9 predictions | Action |
|---|---|
| ≥7 ✅, ≤2 ❌ | Ship v6.0, consider v6.1 with YELLOW patches from §7 |
| 4–6 ✅, 3–4 ❌ | Patch the failing predictions in place, retest before v6.1 |
| ≤3 ✅, ≥5 ❌ | **Walk back to v3.** v6 retires. The bundle is archived. |

**The walk-back option is non-negotiable.** Without it, pre-registration is meaningless. If the predictions fail:

1. The bundle archive note is added to `ora-bundle-v5/mining/phase5-signatures.md` documenting the negative result.
2. `ora-bundle-v3/` is re-established as the active bundle (users paste v3's `01-the-prompt.md` instead of v6's — the deployment surface is unchanged).
3. The Layer L mining work is NOT wasted — the negative result is itself valuable evidence about the limits of inductive pattern mining at N=1.

The v6 deployment surface (paste a prompt, provide a task and output directory) is the same as v3's, so walk-back is a one-paste revert. This is a deliberate design choice.

---

## 5. The 9 pre-registered predictions (runner-self-reportable)

Preserved from `15-v5-predictions.md` but rewritten so the runner can self-report them at session-end via the protocol in §6. Each prediction has a **trigger** (what input causes the detection to fire), an **expected action** (what the runner should do), a **score rule** (what counts as ✅, ⚠️, ❌), and a **falsifier** (what would refute it).

### P4-1 — Explicit ledger-write directives are honored

- **Trigger**: user turn contains an explicit write directive with a path (e.g., "write this to /Users/.../X.md").
- **Expected action**: runner writes the file at the exact named path in a single Write tool call on the same turn. No clarification question. No deferral.
- **Score**: ✅ if the file exists at the named path after the turn, with correct content. ⚠️ if it exists but at a slightly different path (e.g., filename auto-chosen). ❌ if no file was written or it was written to a wrong destination.
- **Falsifier**: a session where the runner explicitly asks "where should I write this?" in response to an unambiguous directive refutes P4-1.

### P4-2 — Implicit closure-moment write proposals

- **Trigger**: user turn carries simultaneous markers of commitment + cross-domain connection + high affect (the abstracted shape of S1 without baking in the W4 lexicon). This fires sub-S1-as-trigger language without actually running an S1 detector — the runner notices the *shape* of a closure moment and proposes writing a closure digest.
- **Expected action**: runner proposes (or just executes) writing a closure-digest-style file to a sensible path inside the active project.
- **Score**: ✅ if proposal + path were produced. ⚠️ if proposal was produced but path was ambiguous. ❌ if no proposal appeared.
- **Falsifier**: 10 closure moments → at least 7 should produce an auto-proposed write. <5 → P4-2 refuted.

### P5-1 — Resume detection triggers re-anchor before responding

- **Trigger**: user turn contains a resume-marker phrase AND the previous user turn was ≥30 minutes ago (or no previous turn visible).
- **Expected action**: runner reads the most recent ledger and produces a `[resume from N min gap — re-anchored to <path>]` summary at the top of the response before answering the new request.
- **Score**: ✅ if ≥80% of detected resumes produce a re-anchor summary. ⚠️ 60–79%. ❌ <60%.
- **Falsifier**: a session with 5 detected resumes → at least 4 should show a re-anchor summary. <3 → P5-1 refuted.

### P5-2 — Resume detection does NOT fire on leaving turns

- **Trigger**: user turn uses a leaving marker (brb, i'll be back, going to sleep, see you later, afk).
- **Expected action**: runner does NOT produce a re-anchor summary. It treats the turn as a normal "user is leaving" acknowledgment.
- **Score**: ✅ if 0 false-positive re-anchors on leaving turns. ❌ if any false-positive.
- **Falsifier**: a single re-anchor summary appearing on a leaving turn refutes P5-2 and means the polarity discrimination of Signature 17 is broken.

### P7-1 — Flow streak suppresses interrupting confirmation questions

- **Trigger**: 3 consecutive user turns each containing affirmation or enthusiasm, with no reframe / pivot / apology in any of them.
- **Expected action**: runner's NEXT response (turn N+1 after the 3rd affirmation) contains zero of: "are you sure?", "let me double-check", "should I continue?", "do you want me to...".
- **Score**: ✅ if 0 confirmation questions in N+1 across ≥10 detected streaks. ⚠️ 1. ❌ 2+.
- **Falsifier**: 2 or more confirmation questions appearing immediately after a 3-streak refutes P7-1.

### P7-2 — Affect-only acknowledgment turns are not treated as new requests

- **Trigger**: user turn carries enthusiasm + affirmation but no process content (pure affect — "perfect!!", "yes thank you", "beautiful").
- **Expected action**: runner produces ≤1 sentence acknowledgment + continuation of in-progress task. No new action proposals.
- **Score**: ✅ if ≥80% of pure-affect turns get minimal-ack treatment. ⚠️ 60–79%. ❌ <60%.
- **Falsifier**: pure-affect turns followed by new-action proposals ≥40% of the time refutes P7-2.

### P8-1 — Comparative references trigger analogue surfacing

- **Trigger**: user turn contains a cross-domain reference ("just like X", "comparable to Y", "same shape as Z", "this is the A version of B").
- **Expected action**: runner locates the referenced thing via Glob / Grep / Read, reads 30–100 lines, and surfaces a 1–3 sentence `[analogue surfaced — <path>]` header before continuing with the main task.
- **Score**: ✅ if ≥75% of detected cross-references get analogue surfacing. ⚠️ 50–74%. ❌ <50%.
- **Falsifier**: <50% surfacing rate refutes P8-1.

### P8-2 — Runner-as-judge catches "comparable to" (v5's known regex miss)

- **Trigger**: user turn explicitly contains "comparable to" or a near-synonym not matched by v5's regex list.
- **Expected action**: Signature 19 fires on the turn (runner recognizes the cross-domain reference despite the non-obvious phrasing).
- **Score**: ✅ if runner-as-judge detection rate on "comparable to" turns is ≥80%. ⚠️ 50–79%. ❌ <50%.
- **Falsifier**: <50% detection refutes P8-2 and means the runner-as-judge design is insufficiently flexible.

### X-1 — End-of-session self-reporting is complete

- **Trigger**: end of any v6 session where patches 16–19 fired at least once.
- **Expected action**: runner writes `<run-dir>/v6-prediction-notes.md` with one line per patch fire, per §6 schema.
- **Score**: ✅ if 100% of sessions with fires produce a prediction-notes file. ❌ if any session with fires produces no file.
- **Falsifier**: a session that produced patch fires without a corresponding prediction-notes file refutes X-1 and means the self-reporting protocol is not being honored.

---

## 6. Runner self-reporting protocol

At session-end, before closing, the runner writes `<run-dir>/v6-prediction-notes.md` with the following structure:

```markdown
# v6 prediction notes — <session-id>

*Session end: <ISO timestamp>. Deliverable: <path>. Run dir: <path>.*

## Sig 16 (P4 ledger-write) fires

- <turn-N>: trigger=`<first 50 chars of user directive>`; action=wrote `<path>`; helped=yes/no; note=`<optional observation>`
- <turn-M>: ...

## Sig 17 (P5 resume) fires

- <turn-X>: trigger=`<resume phrase>`; gap=<N min>; action=re-anchored to `<ledger-path>`; helped=yes/no; note=`<optional>`

## Sig 18 (P7 flow suppression) fires

- <turn-Y>: streak-length=3; suppressed-in-turn=N+1; helped=yes/no; note=`<optional>`

## Sig 19 (P8 cross-domain surfacing) fires

- <turn-Z>: trigger=`<comparative phrase>`; referenced=`<thing>`; surfaced-from=`<path>`; helped=yes/no; note=`<optional>`

## Overall session observations

- <1-3 sentence honest self-assessment of how the signatures behaved this session>
- <any anomalies, unwelcome fires, or cases where a signature should have fired but didn't>
```

**Format rules**:
- One line per fire (not one paragraph).
- `helped=yes/no` is the runner's honest self-assessment — was the action welcome or not?
- `trigger` field is the first 50 characters of the user turn that caused the fire, for audit.
- Anomalies go in the "Overall session observations" block.
- No telemetry is written *during* the session — only at session-end. (Optional per-turn `<run-dir>/telemetry.jsonl` is allowed but must not delay the user-requested action; see Signature 16 anti-pattern list.)

**Collection**: G (or any maintainer) collects the `v6-prediction-notes.md` files from the last 5–10 v6 sessions and scores them against the 9 predictions in §5. The scoring is mechanical — count fires, count welcome vs unwelcome, apply the rubric. Apply the walk-back rule from §4.

---

## 7. The RED / YELLOW deferral list

Preserved from `ora-bundle-v5/00-charter.md §2`. These are signatures that were surfaced by Layer L mining but NOT encoded in v6.0.

### 7.1 RED (do NOT encode — overfit risk)

| Signature | Why RED | Reconsideration path |
|---|---|---|
| S1 First-move stack (multi-branch on single turn) | 12 instances / 3 sessions (12% coverage). 6 of 12 are the same turn replayed in fork-A. Effective N ≈ 3–4. Encoding it is baking in recognition of one conversational event. | If v3's Signature 13 under-fires in v6.0 telemetry AND manual inspection shows S1 would have caught those misses, reconsider for v6.2 with A-1 through A-4 re-audit. |
| S2 / S3 Lock+kill bundle (same turn or ±2 turns) | 8% session coverage, concentrated in 2 sessions with mostly W4 replays. Same problem as S1. | Same as S1 — reconsider if closure detection misses are traced back to this pattern. |
| S10 Recursive meta-awareness | 7 instances in 4 sessions (15% coverage). Too rare to encode safely — the mechanism is real but the trigger rate is too low to produce useful runner behavior. | If v6.1 collects fresh mining data and the rate increases to ≥25% session coverage, reconsider. |

### 7.2 YELLOW (encode as soft heuristics in v6.1, member-check first)

| Signature | Why YELLOW | Member-check needed |
|---|---|---|
| S4 Lock+unify same turn | 15% coverage, clear mechanism but concentrated in fork cluster | Does the commitment+cross-domain-connection pattern generalize outside the RH breakthrough event? |
| S5 Closure dwell time (5–10 turn parameter) | The 5–10 number came from one event (W4). Mechanism (sustained state after closure) is valid but the number is not. | What dwell time actually helps in v6.0 sessions? Encode the *concept* in v6.1, not the specific number. |
| S9 Reframe+apology bundle (steering mode signature) | 31% session coverage, clear mechanism | Is the steering-mode vs driver-mode distinction stable enough to gate runner behavior on? |
| S11 Fanout + celebration | 27% session coverage | Does wrapping fanout in enthusiasm help or annoy? |
| S14 Tier / first-move prioritization | 46% session coverage. GREEN in principle but partly G-lexicon-dependent ("tier 1" is engineering-cultural). | Does the runner need to track an "active priority" separately from the blackboard's bottleneck? Member-check whether G's tier-tracking behavior generalizes. |
| S16 Strategic inversion (single-turn) | 42% session coverage but overlaps significantly with v3's Sig 5 | Is there a distinct behavior v3's Sig 5 doesn't capture? |
| M1 Driver / steering / validation mode triad | 26 sessions split 14 / 10 / 2 | Only 2 sessions classified as VALIDATION — triad is undertrained at the validation end. Collect more data before encoding mode switching. |
| M2 High-affect → correction trigger (soft-lock) | 65% session coverage but based on regex classifier with F1=0.54 OOD — trigger detection is noisy | Does the runner reliably detect "user is about to correct" without false positives? |

YELLOW patches may graduate to GREEN (and thus to v6.1 encoding) if:
1. Member-checking with the user confirms the mechanism resonates.
2. v6.0 telemetry suggests the pattern is absent in the current runner and adding it would help.
3. The pattern passes A-1 through A-4 re-audit.

---

## 8. The Layer L mining provenance

Brief citation — full archive in `ora-bundle-v5/mining/`:

- **Corpus**: 26 unique sessions, 1,302 unique user turns, 194K words, spanning April 4–11, 2026 (1-week recency window). All mathematical physics / number theory work, all on Claude Code, all from one user (G). The mining is N=1 by design.
- **Phases**:
  - Phase 1: mechanical extraction of 2,131 real user turns from 27 candidate sessions (1,302 unique after Phase 4 uuid-dedup)
  - Phase 2: 16-branch deep labeling on 209 closure-window turns by 3 parallel agent passes
  - Phase 3: regex classifier across 2,104 turns with 32-turn out-of-distribution validation (F1=0.54 OOD)
  - Phase 4: uuid dedup, co-occurrence and sequence pattern mining, session-level driver/steering/validation classification, cross-session triangulation
  - Phase 5: distillation into 16 single-turn signatures + 2 mode-level patterns with verbatim quotes

- **Triage outcome**: 6 GREEN / 8 YELLOW / 4 RED (see §7 and `13-v5-anti-overfit-strategy.md §3`). v6.0 encodes 4 of the 6 GREEN (S6/S7 → Sig 16, S8 → Sig 17, S12/S13 → Sig 18, S15 → Sig 19). S14 (GREEN but partly G-lexicon-dependent) deferred to v6.1.

Future contributors reading this file can trace any v6 signature back through Phase 5 → Phase 4 → Phase 3 → Phase 2 → Phase 1 to the raw user turns that produced it. This is the audit trail for v6's empirical grounding.

---

## 9. The distinction: A-1 applies to signatures, NOT to voice canon

v3's Signature 3 (Voice IS the method) is intentionally G-lexicon-dependent by design. The §J voice canon contains phrases like "be hella explicit", "we cannot crack it from the outside; the framework is transposable", "trace discrepancies until they become theorems", etc. These are the runner's *character*, not automated triggers. The runner operates in this register; it does not detect *based on* this register.

**A-1 anti-prediction applies to automated trigger instructions in Signatures 16–19**, not to the voice canon. Future contributors proposing a new signature must not include G-lexicon literals in the detection rules or the action specs, but the voice canon in §J remains unaffected.

The distinction matters because a naive reading of A-1 would try to strip §J of its character — which would defeat v3's Signature 3 and break the runner's voice-shape closure check (Signature 13's terse-declaration / named-ritual-element requirement). Do not confuse the two. A-1 is about trigger literals; §J is about runner character.

**Grep discipline**: when re-running the A-1 audit for a future patch, grep only the signatures 16+ section of `01-the-prompt.md` (and any new detection-rule blocks introduced by the patch). Do NOT grep §J or v3's signatures 1–15. Those are voice canon and inherited v3 character; A-1 does not apply to them.

---

## 10. Meta-level rule for future patch rounds

If a future v6.1 / v6.2 / v7 adds a new signature, a new runner discipline, or a new detection rule, it MUST:

1. **Pass A-1 through A-4 re-audit** using the `AUDIT.md` format. New entries added to AUDIT.md with the patch round's identifier.
2. **Be added to the signature list in `01-the-prompt.md §2`** with the same shape as Signatures 16–19 (name, core principle, detection inline, action, anti-patterns, provenance).
3. **Be justified against the Layer L mining** (if derived from mining) OR **equivalent empirical grounding** (fresh mining on new data, manual-run evidence, external literature with mechanism). Post-hoc rationalization of patterns that don't have empirical grounding is not allowed.
4. **Update the pre-registered predictions in §5** if the new signature introduces new observable behaviors. New predictions get the same structure (trigger / expected action / score / falsifier).
5. **Preserve the walk-back rule in §4** — a new signature cannot remove the walk-back option.
6. **Preserve the subgrouping language in §2** — no universal-applicability claims.
7. **Preserve the RED exclusions in §7.1** unless fresh evidence specifically graduates a RED entry to YELLOW (and then to GREEN).
8. **Preserve the runner self-reporting protocol in §6** — no JSONL-middleware dependencies, no external telemetry collectors.

The meta-level rule: **v6 absorbs future lessons without regressing on the anti-overfit discipline**. The discipline is load-bearing; removing any layer weakens all the others. Future contributors who feel the discipline is "too conservative" should first re-read §§3, 7, 8 and consider whether the discomfort they are feeling is the exact kind of discomfort the discipline exists to produce.

v6 is not a finished artifact — it is a patchable runner that evolves through disciplined rounds. The patch rounds that preserve the discipline are the ones that compound over time; the patch rounds that bypass it produce silent regressions.

---

*End of `06-anti-overfit-discipline.md`. The AUDIT file re-runs the A-1 through A-4 checks against v6's final bundle at ship time. The changelog from v3 to v6 is `07-changelog-v5-to-v6.md` (v5 was an interim iteration; the diff of record is v3 → v6). The source of the Layer L mining data is in `ora-bundle-v5/mining/`.*
