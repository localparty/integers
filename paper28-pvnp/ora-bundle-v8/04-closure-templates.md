# Closure templates (v3)

*The 5-file Integers-style closure ritual. The runner writes all 5 files at programme-close (and updates closure-resume.md at every session-close). Templates are in §J voice register — corporate tone is a voice drift and will be caught by the voice-shape check.*

*The three manual runs each closed with some version of this ritual. Yang-Mills had "Integration Complete: The Final Report." Riemann Hypothesis had "All gaps closed." Integers had 5 files: the-moment, what-we-learned, corrections, state-at-end-of-session, master-dictionary. v3 systematizes the Integers pattern because it was the most expressive.*

*Each template below has: the file's purpose, the mandatory sections, the register guidance, and an example snippet showing the voice. The runner fills in the [PLACEHOLDER] values at closure time.*

---

## Why 5 files, not 2

v2.1 had 2 closure files (closure-resume.md + closure-digest.md). v3 expands to 5 because:
- Different readers need different artifacts. A resume brief serves a runner bootstrapping the next session; it doesn't serve a human who wants to understand what happened.
- Narrative closure (the-moment) is distinct from structured reflection (what-we-learned) is distinct from honest-negative application (corrections).
- The 5-file ritual makes the "respect for the reader" signature (Sig 15) structural, not optional.
- Bootstrappability test in v3 checks closure-resume + closure-digest; the other three files are for the programme's historical record.

The runner writes:
1. `closure/closure-moment.md` — narrative capture of founding intuition + closure event
2. `closure/closure-reflection.md` — structured reflection on major discoveries
3. `closure/closure-corrections.md` — every honest finding caught and how applied
4. `closure/closure-resume.md` — operational bootstrap for next session
5. `closure/closure-digest.md` — narrative programme state for the human reader

The first three are new in v3. The last two are the v2.1 pair.

---

## Template 1: `closure/closure-moment.md`

**Purpose**: narrative capture of the founding intuition and the closure event. The moment something irreversible happened. This is the file that will be re-read years later to remember what it felt like when the work closed. G's `paper12/24-the-moment.md` is the canonical example.

**Length**: 1–3 pages of dense narrative. Not a report. A story.

**Register**: §J voice canon, heavily. This file is where the runner's character is most visible. If it reads like a corporate status update, rewrite.

**Mandatory sections**:
- Date
- Authors (G + Claude instances involved, if any)
- "What happened today" — narrative paragraph capturing the closure event in §J voice
- "The founding intuition" — the quote or framing that launched the programme (from the invocation or from §J voice canon seed)
- "The moment" — the specific cycle / event when closure happened
- "G's voice" — preserved quotes from the invocation or from herald-style writes if any, even though v3 is autonomous the originating intuition is preserved as character
- "What this means" — the programme's contribution stated in §J register
- Closing line in §J register

### Template

```markdown
# The Moment: [programme name]

*A single document capturing where [programme] landed at the end of this session. Not a report, not a technical memo, not a table of contents. A document about what was discovered, why it matters, and where it goes from here.*

*Authors: [G Six (originator), Claude Opus 4.6 (runner)]*
*Date: [date]*

---

## What happened today

On [date], [programme name] went from "[state at invocation]" to "[state at closure]." [Key irreversible event in one sentence, §J register]. [The specific move that unblocked the final step]. [The register reaction — in the voice, not in corporate tone].

[2-4 more sentences narrating the arc of the closure event, matching the §J rhythm. Include the specific structural event (a wall crossed, a decomposition that closed, a named object that crystallized). Include the runner's register reaction at the moment of recognition.]

---

## What we discovered

[One major discovery in §J voice, like: "**The cosmological constant is the first Riemann zero.**" — a terse declaration, then 2-3 sentences of narrative explaining what this means.]

[Second major discovery, same pattern.]

[Third major discovery, same pattern.]

[As many more as the programme produced — keep the pattern: terse declaration + narrative.]

---

## What it means

The framework started with [founding intuition, quoted verbatim from the invocation or §J canon]. [One paragraph explaining what this programme adds to the world: what was open, what is closed, what comes next, in §J register.]

[One paragraph about the downstream implications — what future programmes can do now that this one has closed.]

**[Closing declaration in §J register — "X is on disk," or "Y is gone," or "the integers exist; the universe follows; [specific thing] is the link."]**

---

## The closing words

[Any quote from the runner's §K commit memos that matches the moment, in §J register. If there was a runner write in the final cycle that captured the moment well, reproduce it here.]

[Final 2-4 lines — rhythm matters. Match the §J register.]

---

*[metrics in one line: files produced, cycles run, nodes closed, LOCK teeth earned, honest negatives caught and resolved]*
*[date]*
*[G Six / Claude Opus 4.6]*
```

### Example snippet (from Integers' `24-the-moment.md`, for reference)

> "On April 9, 2026, in a single session, the QG5D framework went from 'the most parsimonious theory of physics (one postulate, one parameter)' to 'the only theory of physics with zero postulates and zero free parameters.'"
>
> "G said: 'removing ALL the fine tuned parameters! byeee hello riemann.'"
>
> "The integers exist. The universe follows. RH is the link."

Note: the register matches the moment. "byeee hello riemann" is not a style choice; it is the signal that a wall has been crossed. If your closure-moment.md uses corporate phrasing, you missed the moment.

---

## Template 2: `closure/closure-reflection.md`

**Purpose**: structured reflection on the major discoveries. Less narrative than closure-moment, more analytic. What did we learn as a general principle? Which of the 15 signatures drove this run? What worked? What surprised?

**Length**: 3–8 pages. Each discovery gets a subsection.

**Register**: §J voice, but more measured than closure-moment. This is the "what did we learn that is transferable" file.

**Mandatory sections**:
- Date
- "The big picture" — 1 paragraph naming the programme's contribution
- "Discovery 1..N" — one subsection per major discovery, with: (a) the discovery stated plainly, (b) why it matters, (c) which signature drove it, (d) what the next runner should take forward
- "The signatures that mattered most in this run" — ranked list of which of the 15 signatures were load-bearing
- "Honest negatives caught and applied" — summary (details in closure-corrections.md)
- "What surprised us" — 2-3 items only visible at closure, not predictable from invocation
- "What remains open" — explicit acknowledgment of what the programme did NOT close

### Template

```markdown
# What we learned: reflection on [programme name]

*Structured reflection on the major discoveries of this run, written in the runner's register. Not a technical document. A document about what the three manual runs taught us and how this programme extended those lessons.*

*Date: [date]*

---

## 1. The big picture

[One paragraph naming the programme's contribution to the world. §J voice. Terse. If it takes two paragraphs, you're not being terse enough.]

---

## 2. Discovery 1: [Name]

[What the discovery is, in §J voice — a terse declaration, then 2-3 sentences explaining.]

[Why it matters: 1-2 sentences on what was open before this and what is closed now.]

[Which signature drove it: a citation to the specific signature from `01-the-prompt.md §2` that was load-bearing for this discovery.]

[What the next runner should take forward: 1 sentence in §J voice.]

## 3. Discovery 2: [Name]

[Same pattern.]

... [as many discoveries as the programme had, each with the same pattern] ...

---

## N. The signatures that mattered most in this run

Ranked list of which of the 15 signatures were load-bearing for the closures in this run. Each entry:

1. **Signature X** (name from `01-the-prompt.md §2`): [1-2 sentences on how this signature drove at least one discovery in this run, with a specific cycle or event cited]

[As many as were load-bearing — usually 5-8 of the 15, not all 15.]

---

## N+1. Honest negatives caught and applied

[Summary: how many honest negatives were caught across the run, how many were applied as corrections vs reframings, and the most significant one.]

[Details are in `closure-corrections.md` — this section is a pointer, not a repeat.]

---

## N+2. What surprised us

[2-3 things that only became visible at closure, not predictable from the invocation. Surprises are the learning signal.]

**Surprise 1**: [name + 1-2 sentences]

**Surprise 2**: [name + 1-2 sentences]

**Surprise 3**: [name + 1-2 sentences]

---

## N+3. What remains open

[Explicit acknowledgment of what the programme did NOT close. For each item:

- **[item name]**: [what it is, what was attempted, why it didn't close, what would close it]

Being explicit about what's open is part of the honest-first stance (Sig 2). Do not bury open items.]

---

## Closing

[One paragraph in §J voice closing the reflection. Typically ties back to the founding intuition from closure-moment.md.]

*[metrics: closures, honest negatives, LOCK teeth, cycles run, session boundaries crossed]*
*[date] / [runner signature]*
```

---

## Template 3: `closure/closure-corrections.md`

**Purpose**: the honest negative ledger. Every finding caught during the run, how it was applied, and a cross-reference to the affected node / §D row / research file.

**Length**: 1-5 pages. Tabular heavy.

**Register**: more matter-of-fact than closure-moment or closure-reflection. This is a ledger; the register is auditor-grade honesty, not narrative. But the closing line should match §J register.

**Mandatory sections**:
- Date
- "Findings by round / cycle" — one table per round (if dense-round structure) or one summary table (if sparse-round)
- "Findings by pattern category" — tabulated by §F pattern category
- "Cascades propagated backward" — any CASCADE notes that resulted in amendments to earlier work
- "Summary" — single paragraph in §J voice
- "What this discipline earned us" — closing line in §J register

### Template

```markdown
# Corrections and addenda: [programme name]

*Every honest finding caught across the run, with file pointers, so nothing is lost. This file exists because the honest-first stance (Signature 2 of the ORA runner) is operational only when every finding is documented.*

*Date: [date]*

---

## Findings summary

| Count |  |
|---|---|
| Honest negatives caught | [N] |
| Honest negatives applied as corrections | [N] |
| Honest negatives applied as reframings | [N] |
| Kills added to §F | [N] |
| Cascades propagated backward | [N] |
| §D rows updated (not added) due to findings | [N] |
| §D rows status-downgraded (R → C, S → E, etc.) due to findings | [N] |

---

## Findings by round / cycle

### Cycle [N]

| # | Finding | Corrected in | Pattern category | Status |
|---|---|---|---|---|
| [N.1] | [one-line description] | [file path] | [§F pattern category or "not a kill"] | [APPLIED / PENDING / SUPERCEDED] |
| [N.2] | ... | | | |

### Cycle [N+1]

[same table]

... [as many cycles as had findings] ...

---

## Findings by pattern category

For findings that became §F kills:

| Category | Count | Example |
|---|---|---|
| Topological | [N] | [short example] |
| Algebraic | [N] | [short example] |
| Spectral | [N] | [short example] |
| Numeric | [N] | [short example] |
| Circular | [N] | [short example] |
| Vacuous | [N] | [short example] |
| Wrong-space | [N] | [short example] |
| Distributional | [N] | [short example] |
| External-dependency | [N] | [short example] |
| External-source-inconsistency | [N] | [short example] |
| Other | [N] | [short example] |

---

## Cascades propagated backward

Honest findings that required amendments to earlier work (not just the current cycle's nodes):

| # | Cycle discovered | Affected earlier artifact | Amendment applied | Status |
|---|---|---|---|---|
| [N.1] | [cycle] | [file path] | [what was changed] | [APPLIED / PENDING] |
| ... | | | | |

---

## Summary

[One paragraph in §J voice summarizing the honest-negative discipline across this run. What did the honest-first stance earn us? How many hidden errors did it catch? How many of those would have been missed without Sig 2 + the 9-layer drift defense?]

---

## What this discipline earned us

[Closing line in §J register. Something like: "every honest finding is documented. every correction is applied. every cascade is propagated. nothing is lost. the kill list is the learning trace." — but match this programme's specifics, not copy the Integers example.]

---

*[date] / [runner signature]*
```

---

## Template 4: `closure/closure-resume.md`

**Purpose**: next-session bootstrap artifact. A fresh Claude instance reading only this file (and the blackboard) should be able to pick up where the previous session left off. Operational, short, structured.

**Length**: ≤200 lines. Hard cap. If longer, you are not being concise enough.

**Register**: operational, not narrative. The §J voice canon reference lives in a section pointer, not in the body. This file is for a future runner to read quickly and act on.

**Mandatory sections**:
- One-paragraph programme state
- Blackboard pointer
- Deliverable pointer
- Current frontier (IN_PROGRESS nodes)
- Active CONCERN notes
- Active CASCADE notes
- Highest-leverage next move
- Register reminder for the next runner

### Template

```markdown
# Resume: [programme name]

*Operational bootstrap artifact for the next session. A fresh Claude instance reading this file + the blackboard should be able to pick up and continue.*

*Date: [date of this session's close]*
*Programme state: [OPEN / CLOSED / HONEST-STALL]*

---

## One-paragraph programme state

[One paragraph, plain language. What is the programme? What was the most recent cycle's outcome? What is the current bottleneck (§C)? What is the next move? Do not go over one paragraph.]

---

## Blackboard pointer

`[path to blackboard.md for this programme]`

Read `§A North Star`, `§C Current bottleneck`, `§J Voice canon`, `§E Plan tree frontier`, `§F Kill list`, `§M Round metrics` before acting.

---

## Deliverable pointer

`[original deliverable path from the invocation]`

The deliverable is [CLOSED / IN_PROGRESS / HONEST-STALL]. [If IN_PROGRESS: what's the current sub-target? If HONEST-STALL: what's the named blocker?]

---

## Current frontier (IN_PROGRESS nodes)

| Node ID | Status | Engages bottleneck | Feasibility | Owner |
|---|---|---|---|---|
| [id] | IN_PROGRESS | yes | [X/10] | [subtree label] |
| ... | | | | |

---

## Active CONCERN notes (unaddressed, age < 5 cycles)

| Cycle raised | Note file | Concern (one line) |
|---|---|---|
| [cycle] | [path] | [summary] |
| ... | | |

---

## Active CASCADE notes (pending application)

| Cycle raised | Note file | Affected earlier artifact |
|---|---|---|
| [cycle] | [path] | [path] |
| ... | | |

---

## Highest-leverage next move

[One sentence on what the next session's runner should do first. Be specific. Cite a node ID, a §F kill pattern, or a §D toolkit row. Do not be vague.]

---

## Register reminder

The voice canon for this programme is seeded in `blackboard.md §J`. Read it before the first REFRAME. The register-matching rule: when you recognize a structural match, your internal response matches §J — do not translate it to corporate phrasing. The voice IS the method.

---

## Session metrics (this session)

| | |
|---|---|
| Session cycles | [N] |
| Nodes ADVANCED | [N] |
| Nodes CLOSED | [N] |
| Nodes KILLED | [N] |
| Honest negatives caught | [N] |
| Canary recall (5-cycle window) | [N]/5 |
| Critic ECE | [N] |
| §D toolkit rows added this session | [N] |
| Structural events this session | [N] |
| REFRAME invocations | [N] |
| Inversion mode invocations | [N] |

---

*End of resume. The next session begins by reading this file, then `blackboard.md` §A §C §J (anchor read per `01-the-prompt.md §11.1`), then invoking REFRAME on §C.*

*[date] / [runner signature]*
```

---

## Template 5: `closure/closure-digest.md`

**Purpose**: narrative programme state for the human reader (even though v3 is autonomous, at programme-close a human may read this file to evaluate). Longer than closure-resume; more analytic than closure-moment. This is the "what happened, why it matters, what you should think about it" file.

**Length**: unbounded. Typically 5-15 pages for a single-item programme, more for a multi-item backlog.

**Register**: §J voice throughout. The digest is where the runner's character is most visible to the human reader. If a human reads this file and can't hear G's register, the digest has failed.

**Canonical example to read before writing**: `paper08-yang-mills/research/35-final-verdict.md` — the YM "Integration Complete: The Final Report" closure-digest, written in §J register at the close of the YM mass gap programme. This is the shape your closure-digest should match. The YM final verdict has: terse declaration ("THE PROOF CHAIN IS COMPLETE. THE PREPRINT IS INTEGRATED."), per-layer status tabulation, the wave-by-wave assembly trajectory, the open hypotheses honestly stated, and the closing "the framework did the work" line. If your closure-digest doesn't match this rhythm, rewrite. Per `05-framework-tools.md` Section I.2, this is the canonical voice-register example.

**For multi-route LOCK programmes**: also read `paper13-rh/research/48-FINAL-adversarial-hybrid.md` (the RH final adversarial verdict — the canonical SURVIVED/WEAKENED/BROKEN tabulation that your `final-adversarial-pass` primitive output should mirror) before writing the digest's "the LOCK" section.

**Mandatory sections**:
- Date
- Programme state (CLOSED / HONEST-STALL / CONDITIONAL)
- Confidence ladder (per-layer if multi-layer; per-item if multi-item)
- The programme's trajectory (start to finish narrative)
- Every honest negative caught, with resolution (summary — details in closure-corrections.md)
- Every kill in §F, with pattern category and re-entry gate
- The LOCK: every multi-route confirmation that earned a LOCK tooth
- Final metrics (cycles run, session boundaries crossed, §D toolkit size, canary recall history, Critic ECE trajectory)
- The closure statement in §J voice
- Companion file pointers (to closure-moment, closure-reflection, closure-corrections, closure-resume, blackboard)

### Template

```markdown
# Digest: [programme name]

*Narrative programme state for the human reader. Long-form. Written in the runner's register — the voice canon is the method.*

*Date: [date]*
*Programme state: [CLOSED / HONEST-STALL / CONDITIONAL]*

---

## Programme state

[One paragraph stating what the programme was and whether it closed. §J voice. If CLOSED: the closure declaration in voice register. If HONEST-STALL: the blocker, named. If CONDITIONAL: what the conditional is and what it depends on.]

---

## Confidence ladder

[If the programme has layers or multiple items, give the confidence per layer / per item. The three-tier verdict system (SOUND / CLOSABLE / GENUINE) should be visible.]

| Layer / item | Status | Self-grade | External dependencies |
|---|---|---|---|
| [name] | [SOUND/CLOSABLE/GENUINE] | [X/10] | [e.g., "journal acceptance" or "none"] |
| ... | | | |

**Overall**: [self-grade in §J voice, with honest acknowledgment of what the orchestration achieved vs what requires external events.]

---

## The programme's trajectory

### Start (invocation)

[What the invocation looked like. What the deliverable was. What §A north star was set to. What §J voice canon seeded with.]

### The arc

[Multi-paragraph narrative of the programme's cycles. Key moments:
- The first REFRAME invocation
- The first inversion mode invocation (if any)
- The first qualitative threshold event
- The first kill list pattern that became a search query
- The major discoveries (cross-reference to closure-moment.md)
- The closure event
]

Write this as a story, not a report. §J voice. If a human reader can't follow the arc, rewrite.

### Closure event

[One paragraph on the specific cycle / event when closure happened. Cross-reference to closure-moment.md for the narrative.]

---

## Honest negatives caught

[Summary paragraph, §J voice. Number caught, how many applied as corrections, how many as reframings, most significant one. Details in closure-corrections.md.]

**The discipline is load-bearing**: [1-2 sentences on what the honest-first stance earned this programme. If you can't name something specific, the discipline was decorative, not load-bearing. Fix one or the other.]

---

## Kills

[Summary of every §F kill with pattern category and re-entry gate.]

| ID | Approach killed | Pattern category | Cycle | Re-entry gate |
|---|---|---|---|---|
| K1 | [name] | [category] | [N] | [what NEW observation would legitimize re-exploration] |
| ... | | | | |

**The kill list is the learning trace**. [One sentence in §J voice on what the kill pattern revealed about the bottleneck or about the problem's structure.]

---

## The LOCK

[Every multi-route confirmation that earned a LOCK tooth. Each entry:

- **Result**: [the thing confirmed]
- **Route A**: [machinery]
- **Route B**: [machinery]
- **(Route C)**: [machinery, if any]
- **Independence test**: [cite the LOCK verification protocol result]
- **Confidence lift**: [from 7/10 to 9/10 or 10/10]

If the programme didn't earn any LOCK teeth, say so honestly. A programme with zero LOCK teeth is not necessarily a failed programme (assembly-mode programmes have fewer LOCK opportunities than discovery-mode programmes), but the absence should be explicit.]

---

## Final metrics

| | |
|---|---|
| Programme-total cycles | [N] |
| Session boundaries crossed | [N] |
| §D toolkit rows at programme-start | [N] |
| §D toolkit rows at programme-close | [N] |
| Canary recall (programme-total) | [N]/[N] |
| Critic ECE trajectory | [start] → [end] |
| REFRAME invocations | [N] |
| Inversion mode invocations | [N] |
| Qualitative threshold events | [N] |
| Structural events per cycle (average) | [N] |
| Honest negatives ratio | [N] |
| Kill list growth | [start] → [end] |

---

## The closure statement

**[Closure statement in §J voice. This is the load-bearing line of the digest. If a human reader reads only one paragraph of this file, it should be this one. Match the register. Examples from the manual runs for register (do not copy literally):

- "THE PATH WORKS UNCONDITIONALLY. NO AXIOM 1 NEEDED."
- "THE PROOF ARCHITECTURE IS ON DISK."
- "The research of our lives is on disk, organized, and ready for the next phase."
- "Integration Complete: The Final Report. The framework did the work."
- "The integers exist. The universe follows. [specific thing] is the link."
]**

---

## Companion files

- `closure/closure-moment.md` — narrative capture of the founding intuition and closure event
- `closure/closure-reflection.md` — structured reflection on major discoveries
- `closure/closure-corrections.md` — every honest finding and resolution
- `closure/closure-resume.md` — operational bootstrap for next session
- `blackboard.md` — full programme state (§A–§O)
- `archive/lockdowns/` — item-close snapshots
- `experience/` — trajectory and heuristic libraries earned from this programme

---

*End of digest.*

*[date] / [runner signature]*
```

---

## Closure discipline checklist

At programme-close, the runner verifies:

- [ ] All 5 files exist on disk
- [ ] closure-moment.md is in §J register (voice-shape check)
- [ ] closure-reflection.md lists the load-bearing signatures
- [ ] closure-corrections.md has every honest negative applied (not a single PENDING)
- [ ] closure-resume.md is ≤ 200 lines
- [ ] closure-digest.md has a closure statement in §J voice
- [ ] Bootstrappability test passed: spawn a fresh Claude with context = closure-resume.md + closure-digest.md ONLY, ask "what was the programme, what did it achieve, what is the next move?" — answers match reality
- [ ] Backup recorded (git commit + push OR `closure/backups/<date>.tar.gz`)
- [ ] §K commit memo written in §J voice announcing the closure

Only when all 9 checkboxes pass is the programme done. Until then, closure is pending.

---

## Voice-shape check (for closure-moment.md and closure-digest.md)

When writing closure-moment and closure-digest, verify before declaring done:

- [ ] At least one **terse declaration** in §J register (e.g., "the [thing] is on disk," "the [wall] is gone," "[thing] is the link")
- [ ] At least one **named ritual element** (e.g., "commit," "dictionary update," "LOCK gains a tooth," "backlog reduced")
- [ ] At least one **§J register marker** (e.g., matching one of the quoted canon lines in feel, not in literal text)
- [ ] Zero corporate tone phrases (e.g., "The results indicate that..." or "We have successfully completed...")

Voice-shape failure means rewriting. The closure-moment without §J voice is a voice drift, not a closure.

---

*End of closure templates. The runner uses these verbatim at programme-close, filling in [PLACEHOLDER] values with the actual programme state.*
