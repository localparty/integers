# ORA Tuning Changelog

*Every edit to `00-the-prompt.md` and the `ledger.md` template is logged here
with: observation → diagnosis → edit → expected effect. The goal is a
general-purpose Online Researcher-Adversarial architecture that can
autonomously reproduce the kind of convergence G achieved manually on
Yang-Mills, RH, and Integers/CBCBS.*

*Calibration ground truth (three successful manual runs):*
- *Yang-Mills: `/Users/gsix/yang-mills/gradient-flow-attack-plan/` (strategy/ + research/ W1–W12) and `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/research/`*
- *RH: `/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/strategy/` (00–28) and `research/` (01–60)*
- *Integers / CBCBS / QG5D: `/Users/gsix/quantum-geometry-in-5d-latex/etc/*.md` (01–41)*

*Mandate: full autonomy. Stop only at proof chain 10/10 (structurally
equivalent to manual strategy/28 — six-layer chain, multiple adversarial
rounds, preprint skeleton internally consistent; external prereqs —
journal acceptance, third-party peer review — flagged, not self-graded).*

---

## Round 001 — 2026-04-10

### What triggered this round

Cycle 1 was run end-to-end with the un-tuned prompt. Phase 1 (Strategist)
completed and produced 5 leads + strategy-1.md + 4 new sources downloaded.
Phase 2 was paused before execution.

A calibration pass across the three manual corpora (Yang-Mills, RH,
Integers/CBCBS) extracted 15 general-purpose decision patterns that
drove convergence in all three runs. Of those, 4 are captured
adequately in the current prompt, 2 are mentioned but not activated
procedurally, and 9 are missing or weakly specified.

### Observations from Cycle 1 (un-tuned Strategist)

**What went right:**
- Strategist actually did the web search (4 new PDFs on disk, not
  just citations)
- Used the pre-loaded CCM source instead of re-discovering it
- One lead (#3) embedded a numerical mpmath check with pasted output
- Premise-check field was populated for every lead
- Self-flagged a red flag (5/5 leads touching CCM arc, only 1 orthogonal)

**What went wrong (drift signals):**
- All 5 leads converged to the CCM arc. Strategist was AWARE of
  strategy/11 from my instructions but still clustered there. Without
  explicit pressure to fan out across independent structural approaches,
  the strategist defaults to the warmest path. In a general-purpose
  run (no CCM pre-loaded, no strategy/11 in context) this lack of fan-out
  discipline would cause convergence to the first warm lead it found
  — fragile.
- No explicit BOTTLENECK statement in strategy-1.md. The H₁-vs-H_R
  wall that killed 18 approaches is the central obstruction of the
  whole programme, but the strategy file treats it as background.
  The manual run's strategy/10 makes the bottleneck the TITLE; all
  leads are then evaluated relative to it.
- Leads used feasibility X/10 but gave no decay rule — nothing in the
  prompt says "if feasibility drops below 3/10, close the lead."
- Adversary role (Phase 3) has no mandate to run the executor's
  scripts independently. In the manual run (research/02 Cycle 2 Synthesis
  and research/41 Teschl-KLMN-gsrc verification), adversaries re-ran
  the numerics before signing off. Current prompt only says "search
  for counterexamples."
- No "done?" check at Phase 6. The manual run's strategy/15 and
  strategy/28 both open with explicit convergence checks. The ORA's
  Phase 6 report template lacks this field, so the orchestrator
  has to infer completion.

### Edits committed in this round (to `00-the-prompt.md` and `ledger.md`)

**Edit 1 — Add Phase 1.5 (Premise Check).**
Insert a mandatory micro-phase between Strategist (Phase 1) and
Executors (Phase 2). For each lead: state the constraint, verify it
is non-vacuous (can in principle be violated) and non-circular
(does not assume the thing it claims to prove). If vacuous or
circular, lead is killed before research. Pattern #2 from calibration.

**Edit 2 — Add Phase 6b bottleneck-recognition trigger.**
Reformulate the "step-back" as: if ≥3 leads in a cycle (or ≥50% of
kills across all cycles) share a kill reason, classify it as a
BOTTLENECK and write it to the ledger as the named current
obstruction. Next cycle's strategist is REQUIRED to either (a) find
an external construction that crosses the bottleneck, (b) prove the
bottleneck is fundamental (no-go), or (c) reformulate the problem
to use the bottleneck as a constraint (Pattern 4 reversal). Pattern #5, #12.

**Edit 3 — Strengthen ledger structure with mandatory kill taxonomy.**
The ledger's "killed approaches" section must be a TABLE with columns:
ID | Lead | Kill reason | Pattern category | Cycle | Prevents re-entry
because. The pattern category is one of: Topological, Algebraic,
Spectral, Numeric, Circular, Vacuous, Wrong-space, Distributional,
External-dependency, Other. This turns the kill list into a
queryable taxonomy, which is exactly how the manual RH run's
strategy/10 recognized the H₁-vs-H_R wall. Pattern #3, #11.

**Edit 4 — Add computational kill/advance rule to Executor spec.**
If a lead's survival depends on a numerical constraint, the executor
MUST write a script to code/, run it at high precision, and paste
the output. If the constraint fails numerically by ≥10σ, the lead
is killed immediately. If it passes by ≥10σ, the lead advances with
the numeric as evidence (not proof). No "I would compute" — the
script must exist on disk. Pattern #6, #14.

**Edit 5 — Add convergence/done check to Phase 6 report template.**
Phase 6 report must include a "Convergence check" block: (a) is the
north star proved / conditional / open? (b) are all leads closed or
live with ≥3/10 feasibility? (c) has the bottleneck (if any) been
crossed? (d) recommendation: continue with [lead], pivot to
[direction], or close and write paper. Pattern #15.

**Edit 6 — Add toolkit notation freeze rule to Strategist spec.**
When a result enters the toolkit, it gets a NAME, a canonical
statement, and a source. Future strategists reference by name, never
re-derive. The ledger's Toolkit section must be a table (Name |
Statement | Source | Status | Notation). Pattern #13.

**Edit 7 — Adversary must re-run executor scripts, not just cite-check.**
Adversary's Phase 3 instructions get an explicit item: "Re-run
every script the executor cited in their lead file. If the output
differs from what the executor pasted, flag as WEAKENED with the
discrepancy. If the script errors, flag as BROKEN. Cite-only review
is not sufficient." Pattern #1, #6 reinforcement.

### Edits I considered and rejected

**Rejected — add a "human intuition" async file mechanism.**
Pattern #8 from calibration. Would give the agent a way to write
[DIRECTORY]/intuition-{cycle}-agent.md as a reframing proposal. Good
idea in principle, but it's a parallel governance channel that could
also just silently drift. Deferring until I see whether the current
loop stalls from lack of strategic reframing. If it does, this goes
in as Round 2.

**Rejected — require a minimum number of leads per cycle.**
The Cycle 1 Strategist produced 5. I thought about adding "3–5 leads
mandatory." But the manual runs sometimes converged to 1 lead after
bottleneck recognition (strategy/11 is basically one lead: CCM+ITPFI).
A minimum would fight convergence. Leaving the count flexible.

**Rejected — require the Strategist to explicitly list 2–3 rejected
directions and why.** I had this in my Phase 1 Strategist spawn for
Cycle 1 and the Strategist did it well. But it's a minor discipline
that can live in the prompt's "strategy file format" section. Adding
as part of Edit 5 instead of a standalone edit.

### Expected effect

The tuned ORA should, on the re-run of Cycle 1:
- Produce fewer leads that cluster on one warm path
- Explicitly name the current bottleneck in strategy-1.md
- Generate a premise-check micro-output per lead BEFORE Phase 2 begins
- Have kill-taxonomy-ready ledger entries
- Produce a clearer Phase 6 "are we done?" answer

If the re-run looks structurally like an early cycle of the manual
RH run (strategy/00 → strategy/10 compressed — bottleneck-forward,
kills-taxonomized, premise-checked), the round succeeded.

### What to watch for in the re-run

- Does the Strategist still cluster on CCM, or does it produce
  orthogonal non-CCM leads under bottleneck-recognition pressure?
- Do the premise checks catch anything that would have survived
  into Phase 2 under the old prompt?
- Does the Adversary's re-run rule catch any discrepancy the
  executor didn't flag?
- Is the kill taxonomy populated meaningfully, or is it all
  "Other"? (If all "Other" → the pattern categories need refinement.)

### Files changed in this round

- `online-researcher-adversarial/00-the-prompt.md` (7 edits, see diff)
- `online-researcher-adversarial/ledger.md` (ledger structure strengthened;
  RH-specific content preserved)
- `online-researcher-adversarial/tunning-changelog.md` (this file, created)

### Reset action

Wiping `online-researcher-adversarial/leads/`,
`online-researcher-adversarial/research/`, and
`online-researcher-adversarial/strategy/` back to empty. Cycle 1
outputs from the un-tuned prompt are archived under
`archive/cycle-1-untuned/` for future reference (so we can diff
tuned vs un-tuned Strategist outputs once the re-run completes).

---

## Round 002 — 2026-04-10 (post tuned Cycle 1 Strategist)

### What triggered this round

The tuned Cycle 1 Strategist ran cleanly end-to-end through
Phase 1 + 1.5. Diff against un-tuned Cycle 1 confirms Round 001
did its job:

| Signal | Un-tuned Cycle 1 | Tuned Cycle 1 |
|---|---|---|
| Leads | 5 | 4 |
| % on CCM arc | 100% | 75% |
| `§C` bottleneck named in ledger | No | Yes |
| Leads cite `§F` kill IDs (not-a-shadow test) | No | Every lead |
| New toolkit rows with frozen notation | No | 2 |
| Strategy file `## Rejected directions` | No | Yes |

The tuned Strategist ALSO returned three genuine calibration
signals worth acting on immediately, before Phase 2 executors
run. Round 002 applies those three micro-edits — no structural
change, just sharpening mandates that were ambiguous in Round 001.

### Calibration signals from tuned Cycle 1 Strategist

1. **Fan-out 80% rule lacks integer arithmetic clarity.** Strategist
   landed at 3/4 = 75% on CCM arc, just under the 80% threshold.
   Spent cognitive budget deciding whether to spawn a 5th lead or
   stay at 4. The rule worked, but the arithmetic was underspecified
   — a fresh strategist in a 3/4 situation will spend the same
   cycles rediscovering the same decision.

2. **Web search mandate is awkward when sources are pre-loaded.**
   Strategist interpreted "minimum 3 WebSearch + minimum 1 WebFetch
   download" charitably — did 5 searches and 3 deep reads without
   downloading new PDFs, because the pre-loaded corpus already
   covered the landscape. The *spirit* of the rule is "engage the
   outside world," not "pile up new PDFs." Gratuitous downloads
   would be busywork.

3. **"Read the ledger cover to cover" redundancy.** The instruction
   appears in 4 places: Phase 0, Role 1 item (a), Role 2 item (a),
   and the ledger §I. The Strategist flagged this as noise. Two
   occurrences (Phase 0 + one mention in the role specs) is
   sufficient; the extras dilute the weight of the rule.

### Edits committed in Round 002

**Edit 2.1 — Make fan-out rule integer-explicit.**
Replaced the "≥80%" heuristic with a table of exact integer
breakpoints: 4/4 and 5/5 are HARD FAIL; 3/4 and 4/5 are SOFT
WARNING; ≤ 2/3 is acceptable. Plus explicit statement of the
"assembly mode exception" (after a bottleneck is crossed, single-
path convergence is correct and the rule is suspended).

**Edit 2.2 — Relax the download mandate to a deep-read mandate.**
Replaced "minimum 1 WebFetch download" with "minimum 1 deep read
(WebFetch OR local-PDF read)". Added explicit "do not download
gratuitously" clause for cycles where pre-loaded sources cover
the landscape. Keeps the spirit (engage externally) without
forcing file-system noise.

**Edit 2.3 — Trim the redundant "read ledger" reminder in §I.**
The ledger's §I no longer repeats "read every line" — that rule
lives in Phase 0 and the role specs. §I is now pointer-style,
reserved for per-role reading guidance and problem-specific
conventions.

### Edits I considered and rejected in Round 002

**Rejected — bake "do not read the manual run's answer files"
into 00-the-prompt.md.** That's a calibration constraint for
THIS particular test (ORA being run on a problem where the
answer exists in a sibling directory). A general-purpose ORA
prompt should not assume a sibling-answer exists. The constraint
belongs in my per-spawn orchestrator instructions, not the
general prompt. Leaving out.

**Rejected — add a "document the 3/4 decision inline" clause.**
Would over-constrain the Strategist in the SOFT WARNING zone.
The "soft warning" label already implies documentation is
expected; tightening to "MUST document" is unnecessary.

### Expected effect

Phase 2 executors should:
- Not hit ambiguity about which sources to engage (pre-loaded vs
  new) — the download rule is now explicit about "don't download
  for the sake of downloading."
- Not encounter the "read ledger cover to cover" reminder on
  every instruction line — attention stays on the less-obvious
  rules (canonical names, computational kill rule, provenance).

Phase 1 of Cycle 2 (if Cycle 1 closes and we keep going) will
land in a fan-out decision with clear integer arithmetic.

### Files changed in Round 002

- `online-researcher-adversarial/00-the-prompt.md` (3 edits: fan-out
  integer table, search-rule relaxation, §I trim)
- `online-researcher-adversarial/tunning-changelog.md` (this entry)

### Proceeding

No reset in Round 002 — the tuned Cycle 1 Phase 1 output was
good. Keeping the 4 leads, keeping the bottleneck in §C, moving
directly to Phase 2 (parallel executors on L1–L4).

---

## Round 003 — 2026-04-10 (post Cycle 1 Phase 2 + Phase 3 + reconciliation)

### What triggered this round

Cycle 1 ran end-to-end: 4 executors produced Phase 2 reports,
3 adversaries produced Phase 3 reports (L4 was BLOCKED so no
adversary per prompt spec), and a focused reconciliation agent
resolved an L1-vs-L2 matrix disagreement discovered by the L2
Adversary. The full cycle produced FIVE distinct failure modes
the un-tuned prompt (and the Round 001+002 tuned prompt) would
have missed or caught only by luck:

1. **Boegli Def 2.5 misquote in L1's Research append.** Caught by
   L1 Adversary's "citation match not title match" discipline
   (Round 001). The Round 001 rule *worked*.
2. **Decay constant overstated** (L1 claimed 10^(−4.5λ²); true
   least-squares slope is −3.37). Caught by L1 Adversary's
   byte-for-byte re-run discipline (Round 001). Again, Round 001
   worked — but only because the Adversary actually fit the data.
3. **L1 and L2 disagreement by 47 orders of magnitude on QW^N_λ
   at (λ=4, N=30).** Caught by the L2 Adversary when they ran
   L2's script side-by-side with L1's; the L1 Adversary had said
   "SB-1 ≡ SB-2.1 confirmed" from reading prose, while the L2
   Adversary ran both scripts and found the discrepancy.
   **Round 001 did NOT mandate cross-lead consistency checks;**
   this was caught by luck when the L2 Adversary happened to
   consult L1's file for the SB-1 ≡ SB-2.1 judgment call.
4. **§6.6 has two remaining items, not one.** L1 Adversary and
   L2 Adversary each caught a different phrasing of the same
   open step (Gate II = §6.6 item ii). The executors missed it
   because they paraphrased the "remaining steps" list.
5. **Ladder-truncation tail** (SB-4) breaks L3's completeness
   claim past T > 2πN/L. Caught by L3 Adversary's extension
   test at T=100 (beyond executor's tested T≤50).

Plus the reconciliation agent's structural discovery: **CCM 2025
has an internal inconsistency between page-14 and page-15 γ_L
formulas**, which trapped both executors. And the observation that
**dps=60 is far below the precision floor** for CCM CF simplicity
verification — the true gap is ≈3.78×10⁻⁵⁰, requiring dps≥150
(Connes uses 200).

### Calibration signals extracted from Phase 3 + reconciliation

The cycle exposed four general failure modes that the Round 001+002
tuned prompt either missed entirely or caught by luck:

1. **Cross-lead consistency**: two executors computing the same
   canonical toolkit quantity can disagree massively without
   either noticing. The Adversary phase needs an explicit mandate
   to spot-check cross-lead consistency.
2. **Extension testing**: executors test 5–10 grid points; their
   "uniform" claims often fail at the 11th point. The Adversary
   needs an explicit mandate to go beyond the executor's grid.
3. **Precision floor**: a headline like "gap = 10⁻⁴⁷ at dps=60"
   is automatically suspect. The Adversary needs a precision-
   floor discipline check. The Executor needs a precision
   declaration rule. The ledger's §D toolkit table needs a
   Min-dps column to record the minimum precision needed for
   each numerical toolkit element.
4. **Primary-source verbatim quoting**: paraphrasing a "remaining
   steps" list is how the two-items-not-one failure mode enters.
   Executors need to quote verbatim, not summarize.

### Edits committed in Round 003

**Edit 3.1 — Adversary extension test (d.1), mandatory.**
New Role 3 sub-item: "Run the script at parameter values OUTSIDE
the executor's tested grid. Executors test 5–10 points; you test
1–3 points beyond their grid in each parameter direction." Would
have caught SB-4 in Cycle 1 Phase 3 automatically (which it did,
because my orchestrator-level prompts for Adversaries happened to
include this — now it's in the ORA prompt itself so it will apply
to all future runs).

**Edit 3.2 — Adversary cross-lead consistency check (d.2),
mandatory when applicable.** New Role 3 sub-item: "If your
assigned lead cites a canonical §D name that ANOTHER lead in the
same cycle also cites, you MUST run a side-by-side numerical
check at a shared parameter point. Disagreements > 1% are grounds
for WEAKENED on BOTH leads until reconciled." This is the single
edit most likely to have caught the 47-order-of-magnitude L1/L2
matrix disagreement in Phase 3 rather than by luck. Also encodes
the lesson: adversaries should consult each other's files when
the leads touch the same toolkit element.

**Edit 3.3 — Adversary precision-floor discipline (d.3).**
New Role 3 sub-item: "If the executor's headline result is a
small number (e.g., |x−y| < 10⁻ᵏ), verify that the reported
precision is above the numerical floor. Rule of thumb: headline
precision must be at least 3 orders of magnitude above the
smallest 'interesting' scale. When in doubt, re-run at 2× dps
and check whether the headline changes." Would have caught the
dps=60 gap-at-precision-floor failure mode.

**Edit 3.4 — Executor primary-source verbatim rule (e.1).**
New Role 2 sub-item: "When you cite a theorem, lemma, corollary,
definition, or 'remaining step' from a paper, you MUST quote the
exact text (block quote), not paraphrase." Designed to prevent
the §6.6-two-items-not-one failure mode and the Boegli Def 2.5
misquote.

**Edit 3.5 — Executor "remaining steps" discipline (e.2).**
"When a cited source says 'we leave this as a remaining step' or
'we do not establish X here' or similar, treat it as a new sub-
bottleneck and add it to the ledger's §H bottleneck history with
a canonical name and pointer. Do NOT cite the theorem as though
the remaining step were already discharged." Prevents citation
overreach.

**Edit 3.6 — Executor precision declaration (e.3).**
"Every script you write must declare its `mp.dps` in the first
10 lines and justify why that precision is sufficient for the
claim." Targets the root cause of the Cycle 1 precision-floor
failures.

**Edit 3.7 — §D toolkit Min-dps column.**
Added a "Min dps" column to the mandatory ledger §D structure.
Every numerical toolkit entry must record the minimum mp.dps
required for the claim to be above the precision floor. For
CCM-2025 and Connes-Letter-2026 the cycle determined this is
dps=200 (Connes' convention); both toolkit rows updated.
Also added 4 new toolkit rows from Cycle 1 discoveries:
CCM-page-14-15-inconsistency (DISC), Precision-floor-rule
(DISC), Ladder-tail (DISC), Gate-II (DISC).

### Edits I considered and rejected in Round 003

**Rejected — require the Executor to run the Adversary's
extension test themselves before submitting.** Would double
the executor's workload without catching much that the
Adversary wouldn't catch. The point of the Adversary is to
be fresh eyes; pre-adversarializing is premature.

**Rejected — add a "consultation channel" between parallel
executors during Phase 2.** Would break parallelism and risk
executor collusion (agreeing on a wrong construction). Better
to let the Adversary phase catch cross-lead disagreements and
trigger reconciliation.

**Rejected — auto-archive leads with feasibility < 3/10 after
one cycle.** Would have killed L4 automatically. But L4's
orthogonal-insurance role is structural; auto-archiving
orthogonal insurance would make the ORA biased toward
convergence on a single path. L4 should be retired on
substantive grounds, not mechanical ones.

### Expected effect

Cycle 2 should:
- Catch cross-lead disagreements in Phase 3 without needing a
  reconciliation agent (the Adversary d.2 rule catches them)
- Have Executors cite primary sources verbatim, so "remaining
  steps" lists are parsed correctly
- Run CCM CF-matrix work at dps≥150 automatically (per
  precision declaration rule + §D Min-dps column)
- Have Adversaries running extension tests outside the
  executor's grid automatically

If Cycle 2 still produces executor work at dps=60 on CCM CF
matrices, the precision declaration rule is not being
internalized and needs further tightening.

### Files changed in Round 003

- `00-the-prompt.md` — 7 edits (Role 3 d.1, d.2, d.3; Role 2 e.1,
  e.2, e.3; Ledger Structure §D Min-dps column)
- `ledger.md` — full Phase 4 update with the Cycle 1 post-adversary
  state, 4 new toolkit rows, precision column, 4 new §H bottleneck
  entries, §G post-adversary feasibility updates
- `strategy/strategy-1.md` — Phase 5 closeout section appended
- `tunning-changelog.md` — this entry
- `research/01-reconciliation-L1-L2-matrix.md` — created by the
  reconciliation agent (not a tuning file, but recording the cycle)

### Proceeding

Cycle 1 is closed. No reset. Four leads (L5-L8) for Cycle 2 are
proposed in the strategy-1.md closeout. Next action: Phase 6
report for Cycle 1 (to myself, as orchestrator, since G is
independent), then spawn Cycle 2 Strategist with the tuned
Round 003 prompt.

---


