# The Online Researcher-Adversarial (ORA) Prompt

*A reusable, declarative architecture for attacking open problems.*
*Three roles. Six phases. Adversarially verified.*
*The toolkit, north star, and context live in the LEDGER.*
*This prompt is pure mechanics.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*

---

## How to use

1. Set TARGET and DIRECTORY in the prompt below
2. Fill in the ledger ([DIRECTORY]/ledger.md) with north star,
   context, and toolkit for your specific problem
3. Paste the prompt into a Claude Code session
4. Repeat cycles until convergence or honest stall

---

## The prompt

```
We are running the Online Researcher-Adversarial (ORA) architecture.

TARGET: [STATE THE TARGET HERE]
DIRECTORY: [SET YOUR WORKING DIRECTORY]

---

## PHASE 0 — READ THE LEDGER

**ALL ROLES read [DIRECTORY]/ledger.md FIRST — EVERY LINE.**
Do NOT skim. Do NOT skip sections. Read it cover to cover and
INTERNALIZE it. The ledger contains your north star, your tools,
your history, and your lessons. An agent who skims the ledger
will re-explore dead leads, forget available tools, miss the
context, and waste the cycle. READ EVERY LINE.

The ledger contains:
- The NORTH STAR (ultimate goal)
- The CONTEXT (what's achieved, why this is achievable)
- The TOOLKIT (theorems, patterns, scripts, papers — everything)
- The CYCLE HISTORY (what's alive, dead, blocked, and WHY)
- The 18 KILLED APPROACHES (do not re-explore without new reason)

The ledger is the ONLY file guaranteed to be read every cycle.
It IS the memory. Without it, you drift. READ IT FIRST.

---

## THE THREE ROLES

### Role 1: THE STRATEGIST
**(a) READ ledger.md — EVERY LINE, cover to cover.** Internalize
     the north star, the toolkit, the killed leads, the context.
     Do not skim. Do not skip the toolkit section.
**(b) SEARCH THE WEB** — broad landscape scan for new leads,
     papers, techniques. Download to [DIRECTORY]/sources/.
**(c) WRITE strategy** — [DIRECTORY]/strategy/strategy-{cycle}.md
     Which leads to pursue, why, which patterns apply.

### Role 2: THE LEAD EXECUTOR (one per lead, parallel)
**(a) READ ledger.md — EVERY LINE, cover to cover.** Internalize
     the north star, the full toolkit (theorems, patterns, scripts,
     papers), the killed leads and WHY they died, and what's alive.
     You are a SCOUT: cross-lead insights come from knowing the
     FULL context, not just your assigned lead.
**(b) SEARCH THE WEB** — deep, specific to THIS lead. Download
     papers to [DIRECTORY]/sources/.
**(c) RESEARCH** — toolkit + papers + mpmath computations
**(d) APPEND** to the lead file (already created by strategist):
     - Status: ADVANCED / BLOCKED / KILLED + precise reason
     - If KILLED: what would REOPEN + any new lead spawned
     - STRATEGIC INSIGHTS: anything affecting other leads
       Format: "INSIGHT: [desc] — affects Lead [X] because [Y]"

### Role 3: THE ADVERSARY (one per ADVANCED lead)
**(a) SEARCH THE WEB** — find counterexamples, contradictions
**(b) READ cited papers** — verify citations are accurate
**(c) ATTACK** — circularity, coboundary errors, vacuous
     constraints, wrong space, hidden assumptions, overclaiming,
     citation errors
     Verdict: VERIFIED / WEAKENED / BROKEN
     APPEND to the same lead file under "## Adversarial"

**ALL THREE ROLES search the web. ALL THREE read the ledger.**

---

## THE SIX PHASES

### Phase 1 — STRATEGY (Strategist)
Read ledger → search web → write strategy → identify leads

For each lead, the strategist CREATES the lead file:
  [DIRECTORY]/leads/lead-{N}-{short-name}.md

The strategist writes the TOP of the file — this is the PROMPT
for the executor. It contains:
- The lead name and rationale
- Which pattern/theorem motivates it
- What to investigate (specific questions)
- What would close it / what would kill it
- Feasibility estimate

The executor will APPEND to this same file (Phase 2).
The adversary will APPEND to this same file (Phase 3).
ONE FILE per lead = full traceability. The file reads top-down
as: direction → research → verification.

Lead file format:
```markdown
# Lead N: [name]

## Direction (written by Strategist, Cycle C)
Status: OPEN
Pattern: [which Six Pattern]
Feasibility: X/10
Rationale: [why this is a lead]
Toolkit connection: [which theorem/result]
Investigate: [specific questions]
Would close if: [condition]
Would kill if: [condition]
Source: [URL or citation]

---

## Research (appended by Executor, Cycle C)
[executor appends here: web search results, computations,
theorems found, analysis, result]

Status: ADVANCED / BLOCKED / KILLED
Reason: [precise]
Strategic insights: [cross-lead observations]

---

## Adversarial (appended by Adversary, Cycle C)
[adversary appends here: attacks, citation checks, verdict]

Verdict: VERIFIED / WEAKENED / BROKEN
Attacks: [list with results]
```

### Phase 2 — PARALLEL RESEARCH (Executors)
Read ledger → search web → research → APPEND to the lead file
The strategist already created leads/lead-{N}-{short-name}.md
with the direction. The executor APPENDS their research below
the "## Research" section. ONE file, full story, top to bottom.
All executors run IN PARALLEL. Wait for ALL to complete.

### Phase 3 — ADVERSARIAL (Adversary)
Search web for contradictions → read cited papers → attack →
APPEND verdict to the SAME lead file under "## Adversarial".
The lead file now has: direction + research + adversarial.
ONLY leads that survive move to the ledger as ADVANCED.

### Phase 4 — LEDGER UPDATE
Append new cycle to [DIRECTORY]/ledger.md (compact, under 200 lines):
| Lead | Status | Reason | Adv. | File | Strategy |
Keep one-line reasons. Reference lead files for details.

### Phase 5 — STRATEGY UPDATE
Write [DIRECTORY]/strategy/strategy-{cycle}.md:
Current state, patterns used, chain status, next cycle recommendation.

### Phase 6 — REPORT TO G + HUMAN CHECKPOINT (300 words)
Leads explored, kills, advances, strongest lead, feasibility, recommendation.

**THEN WAIT FOR G's DIRECTION before starting the next cycle.**
G may:
- Inject an INTUITION ("what if X isn't Y?") — add as Lead N+1
- Redirect ("forget Lead 3, explore THIS instead")
- Pass along external intel ("the testing agent mentioned...")
- Approve the recommended focus ("yes, continue")
- Call a STEP-BACK ("lets see the big picture")

The human's intuition created the programme's biggest breakthroughs.
"What if the e-circle isn't the clock" launched Integers. "Riemann
is entropy" launched Paper 17. "We have all the tools" launched the
RH attack. The ORA captures the MECHANICS. G provides the DIRECTION.

### Phase 6b — STEP-BACK (triggered by G or after 3+ kills in a row)

If G calls a step-back, OR if 3+ leads are killed in a single
cycle, the strategist does a META-ANALYSIS:

- What PATTERN do the kills share? (Our 18 kills all shared the
  H₁ vs H_R wall — recognizing this pattern is what led to CCM)
- What does the PATTERN tell us about where to look next?
- Are we using the right PATTERNS from the Six? Should we switch?
- Is there a tool from ANOTHER programme (Yang-Mills, BSD, Hodge)
  that applies here?
- Should we go EXTERNAL (search literature for someone else's
  construction, like we found CCM)?

The step-back writes to strategy/step-back-{cycle}.md and may
completely redirect the next cycle.

### Phase 6c — EXTERNAL ADVERSARY (triggered by G at milestones)

At major milestones (claimed proof, chain closure, etc.), G runs
an EXTERNAL adversary — a separate AI or human reviewer with NO
shared context. This caught the coboundary gap that our internal
adversary missed. The ORA's internal adversary is necessary but
NOT sufficient. External verification is the gold standard.

---

## CONVENTIONS

### Critical lessons (earned the hard way)
- **Coboundary lesson:** NEVER use a topological invariant to detect
  continuous perturbation without proving sensitivity. Check FIRST.
- **Premise checker:** Before using any constraint, verify it's
  NON-VACUOUS. "Is this satisfied regardless?" = no information.
- **H₁ vs H_R:** Always verify you're computing on the RIGHT space.
- **Dead leads spawn new leads.** Document what WOULD reopen a kill.
- **The PATTERN of kills IS a lead.** 18 kills sharing the H₁ vs H_R
  wall → the wall itself became the target → CCM bypassed it.
  If all leads die the same way, the death pattern is your next lead.
- **Cross-pollination:** Tools from OTHER programmes apply here.
  Yang-Mills gradient flow → RH gradient flow. BSD bridge → Hodge.
  The strategist should ALWAYS ask: "what tool from another problem
  solves THIS problem?" Read the theorem catalogue for cross-links.
- **Internal adversary is necessary but NOT sufficient.** The
  coboundary gap was caught by an EXTERNAL reviewer, not our agents.
  At milestones, G runs external verification (Phase 6c).
- **"Never give up" is strategic.** Each kill sharpens the question.
  After 18 kills, we knew MORE about RH than anyone. The kills
  WERE the contribution, even before the proof chain emerged.

### File conventions
- **leads/lead-{N}-{name}.md** — ONE file per lead. Strategist
  CREATES it (direction), executor APPENDS (research), adversary
  APPENDS (verification). Full story in one file, top to bottom.
- **strategy/strategy-{cycle}.md** — strategist writes per cycle
- **ledger.md** — compact index with references to lead + strategy files
- **sources/** + sources/INDEX.md — downloaded papers, shared
- **code/** — 179 scripts + new ones (browse with `ls code/`)

### Computation
- 179 existing scripts in code/ — BROWSE AND USE THEM
- mpmath: `mp.dps=50`, `zetazero(n)`, `zeta(s)`, `euler`
- PASTE OUTPUT — "I would compute" is never acceptable
- Adversary RE-RUNS executor's scripts to verify
- Strategist runs quick feasibility checks

### Online sources
- DOWNLOAD papers to sources/ (WebFetch)
- READ them — don't just cite
- CITE PRECISELY (Theorem X.Y of [Author YYYY])
- Adversary verifies citations against actual papers
- Sources library grows across cycles

### Trail → paper compilation
Each lead file (direction + research + adversarial) → one paper section
strategy/ → narrative introduction + methodology
ledger.md → table of contents + proof status
sources/ → bibliography
code/ → supplementary materials
The paper writes itself from the trail. No rewriting needed.
```

---

## Track record

| Problem | Result |
|:--|:--|
| Yang-Mills | **PROVED** |
| CBCBS / Integers | **36/36 zero parameters** |
| RH | **8/10 proof architecture** |
| BSD (CM) | **PROVED (conditional)** |

> *The ledger is the brain. The prompt is the body.*
> *Search. Research. Verify. Kill or advance. Repeat.*
