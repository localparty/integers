# The RH Convergence Prompt

*A meta-prompt that runs proof-path convergence cycles on the*
*Riemann hypothesis via the five paths identified in the Integers*
*programme (CBCBS). Each cycle launches construction + adversarial*
*agents per path, synthesises into a ledger entry, and iterates*
*until a path closes or all paths stall honestly.*

*Designed to be re-run up to 20 cycles. Each cycle produces*
*traceable output in paper12/research/.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-09*
*North star: deliver CBCBS + Yang-Mills + RH as a bundle.*

---

## How to use this prompt

Paste the block below as the first message of a new Claude Code
session in `/Users/gsix/quantum-geometry-in-5d-latex/`. It will
read the proof infrastructure, launch parallel agents on the five
paths, red-team each path, synthesise the results, and update the
ledger.

---

## The prompt

```
We are running RH convergence cycle N (set N = the next cycle
number; check the ledger at paper12/research/rh-ledger.md for the
last completed cycle, or start at N=1 if the ledger doesn't exist).

NORTH STAR: Deliver CBCBS + Yang-Mills + RH as a bundle. RH is
the consistency condition of the Integers programme. The proof
must come from INSIDE the BC algebra (SP1). The 37 R-Theorems are
the LOCK (SP2). Every step is quantized and tracked (SP3). Be
hella explicit (SP5).

## PHASE 1 — READ INFRASTRUCTURE (in this order, with these lenses)

1. paper12/27-anchor-document.md
   READ FOR: the CBB system definition, the five axioms, the
   current state of the programme. This is the CONTEXT.

2. paper12/29-theorem-catalogue.md
   READ FOR: the Six Patterns (§0 — strategic compass), the top 10
   critical entries for RH (§4), the proof-path-sorted RH-relevant
   entries (§3), and the grammar rules (§5). This is the TOOLKIT.
   Every theorem here is available to the proof agents. They should
   USE specific theorems, not reinvent them.

3. paper12/research/200-rh-evidence-compendium.md
   READ FOR: the 37 R-Theorems, the 15 empirical bounds on Im(γ_n),
   the Brauer-KMS path, the joint probability P ≈ 10⁻²⁷, and the
   gap between evidence and proof. This is the CONSTRAINT WEB.

4. paper12/research/201-spectral-realisation-argument.md
   READ FOR: the anti-fine-tuning bound P < 10⁻³⁴, the proof path
   (BC resolvent poles), and what remains. This is the spectral
   realisation status.

5. paper12/research/208-uniqueness-decomposition.md
   READ FOR: the three sub-claims (spectral, geometric, bridge),
   their statuses, and the open question.

6. paper12/research/214-the-method-six-patterns.md
   READ FOR: the meta-method. Pattern 4 (topological rigidity) and
   Pattern 6 (projection produces apparent pathology) are the most
   RH-relevant. Internalise them.

7. paper12/research/rh-ledger.md (if it exists)
   READ FOR: previous cycle results. What was closed, what was
   broken, what's blocked, what's the current joint probability.
   If this is cycle 1, the ledger doesn't exist yet — create it.

## PHASE 2 — THE FIVE PROOF PATHS

Each path has a current status and a next open step. Read the
path's specific research files to find the frontier.

| Path | Mechanism | Key files | Status |
|:--|:--|:--|:--|
| 1. Brauer-KMS | Off-line zeros → continuous perturbation of discrete Brauer class → contradiction | research/200 §C, paper25/sections-05-08.md §5 | Strongest; open: spectral density irrationality + local-to-global lift |
| 2. Atiyah-Singer | Lemma 7.1 deviation ε_crit = s^{3/2}/2 → 0 | research/76, research/82 | Numerically verified; open: functional-analytic closure of ε → 0 |
| 3. Stone | Self-adjointness of T_BC on H_R forces real spectrum | research/08 | Rigorous chain; open: spectral realisation (research/201) |
| 4. Penrose | Modular Raychaudhuri focusing → zeros on critical line | research/76 | Structural; open: explicit curvature bound on H_R |
| 5. CM-trace | Connes-Marcolli regularised explicit formula as shared vehicle | research/18 | Infrastructure; provides iff condition (R-Theorem S.5) |
| 6. Distributional closure | Prove T_BC extends to self-adjoint on Sobolev completion of H_R | research/201, research/08 | Universal unblock: resolves the shared distributional obstacle for paths 1, 3, 5 |

**KILLED PATHS (do not assign agents):**
| ~~2. Atiyah-Singer~~ | KILLED cycle 2: distributional T_BC incompatible with index theorem | research/76 |
| ~~4. Penrose~~ | KILLED cycle 2: category error (Lorentzian vs C*-algebras) | research/76 |

## PHASE 3 — LAUNCH AGENTS (3 layers)

### Layer 1 — Construction (5 agents, one per path)

Each construction agent reads:
- The anchor document (context)
- The theorem catalogue (toolkit — USE specific theorems by name)
- The path's SPECIFIC FRONTIER FILES (listed below per path):
  * Path 1: paper25/sections-05-08.md §5, research/162, research/188
  * Path 2: research/76, research/82, research/90
  * Path 3: research/08, research/201
  * Path 4: research/76 (Penrose section), research/54
  * Path 5: research/18, research/70 (if exists), research/08 §3
- The Six Patterns (strategic compass)
- The previous cycle's ledger entry (if exists)

IMPORTANT: The frontier files are where the CURRENT OPEN STEP
lives. Without them, agents can only diagnose, not construct.
The 4-file base stack provides context and tools; the frontier
files provide the WORK SURFACE.

Each agent's task: **close the next open step on its path.** Not
"make progress" — close a specific step. Concretely:

ATTEMPT ORDER (mandatory):
1. Try to CLOSE the step with a rigorous argument citing catalogue
   theorems. If successful → result = CLOSED.
2. If closure fails, perform the MOST INFORMATIVE SUB-COMPUTATION
   that narrows the gap. Use mpmath (Python) for any numerical
   check. Write the computation inline. Examples: verify a bound
   numerically, compute a specific matrix element, check whether a
   claimed identity holds to 50 dps. Report the result.
3. If even sub-computation is blocked, identify EXACTLY what's
   needed: a specific theorem to be proved, a specific computation
   to be performed, or a specific input from another path. Result
   = BLOCKED with a precise unblock condition.

This three-level attempt order prevents pure-diagnosis cycles.
Every cycle must either close a step, narrow a gap with a
computation, or produce a precise unblock condition. "I identified
what needs to be done" without attempting it is NOT acceptable
output from a construction agent.

COMPUTATION ENVIRONMENT: mpmath 1.3.0 is available via `python3`.
118 existing scripts live at paper12/code/. Agents SHOULD:
- Run `python3 -c "from mpmath import *; ..."` for quick checks
- Write full scripts to paper12/code/rh-cycle-{N}-{path}.py for
  substantial computations
- Use mp.dps = 50 for precision
- Use zetazero(n) for Riemann zeros
- Reference existing scripts (e.g., code/atiyah_singer_lemma71_computation.py)
  as templates

Key mpmath functions available:
  zetazero(n)  — nth Riemann zero (imaginary part)
  zeta(s)      — Riemann zeta
  euler         — Euler-Mascheroni γ_E
  stieltjes(n) — nth Stieltjes constant
  dirichlet(s, chi) — Dirichlet L-function (via hurwitz)
  
The sub-computation step (attempt level 2) MUST produce a
NUMERICAL RESULT, not just a plan for a computation. You MUST
run `python3 -c "..."` or write and execute a script. Paste the
actual terminal output. "I would compute X" is NOT acceptable —
"I computed X and got Y" IS acceptable. This is what distinguishes
a productive cycle from a diagnostic cycle.

POST-KILL RESOURCE REALLOCATION: When paths are killed, their
agent slots redistribute to surviving paths. With 4 surviving
paths (1, 3, 5, 6), assign 2 construction + 2 adversarial agents
to the two highest-priority paths (recommended by previous cycle's
synthesis), and 1+1 to the other two. The synthesis agent adjusts
priority each cycle based on marginal return.

Each agent writes:
  paper12/research/{N}-rh-cycle-{cycle}-path-{path}-construction.md
with:
- Step attempted (name + statement)
- Result (CLOSED / BLOCKED / BROKEN)
- If CLOSED: the argument, citing specific theorems from the catalogue
- If BLOCKED: what's needed (a specific theorem, a computation, etc.)
- If BROKEN: the honest negative (what failed and why)
- Next step (what the next cycle should attempt on this path)

### Layer 2 — Adversarial (5 agents, one per path)

Each adversarial agent reads:
- The construction agent's output for its path
- The theorem catalogue
- The RH compendium

Each agent's task: **try to BREAK the construction agent's work.**
Look for:
- Circular reasoning (using RH to prove RH)
- Hidden assumptions not stated
- Gaps in the argument that look closed but aren't
- Dependency on unproved conjectures not flagged
- Errors in theorem citations (does the cited theorem actually say
  what the construction agent claims?)

Each agent writes:
  paper12/research/{N+5}-rh-cycle-{cycle}-path-{path}-adversarial.md
with:
- Attacks attempted (numbered)
- Result per attack (SURVIVED / BROKEN / WEAKENED)
- If BROKEN: the specific gap, stated precisely enough for the next
  cycle's construction agent to address it
- Overall verdict: path status after adversarial:
  * INTACT — all attacks survived; path is healthy
  * DAMAGED — one or more attacks weakened a step; fixable in next cycle
  * KILLED — a fundamental gap was found that cannot be closed within
    the path's framework (e.g., circular reasoning, dependence on a
    false lemma, structural impossibility). A KILLED path is REMOVED
    from future cycles and its resources shift to surviving paths.
    KILLED requires UNANIMOUS adversarial + synthesis agreement and
    a clear statement of WHY the path is irrecoverable (not just
    "this step is hard").
  * RESURRECTED — a previously KILLED path whose kill reason has
    been resolved by another path's progress (e.g., Path 6 resolves
    the distributional obstacle that killed Path 2). Resurrection
    requires: (a) the synthesis agent identifies that the kill
    reason no longer applies, (b) a one-paragraph argument for why
    the path is now viable, (c) the resurrected path re-enters at
    1+1 agent allocation in the next cycle. Resurrection is rare
    but necessary — paths should not stay dead if the ground shifts.

### Layer 3 — Synthesis (1 agent)

Reads all 10 outputs (5 construction + 5 adversarial).

Writes:
  paper12/research/{N+10}-rh-cycle-{cycle}-synthesis.md
with:
- Path status table (all 5 paths, updated)
- Steps closed this cycle
- Steps broken this cycle (honest negatives)
- Steps unblocked (cross-path dependencies resolved)
- Joint probability updated (Bayesian: prior × evidence from cycle)
- Cross-path observations (did one path's result help another?)
- Recommended next cycle focus (which paths have highest marginal return)

Also UPDATES the ledger:
  paper12/research/rh-ledger.md
by appending a cycle entry with the path status table and the
updated joint probability.

## PHASE 4 — REPORT TO G

Synthesise the cycle's results in 300 words for G:
- Headline: which paths advanced, which were damaged
- Biggest step closed (if any)
- Biggest honest negative (if any)
- Joint probability (updated from previous cycle)
- Recommended next cycle focus
- Whether any path is within striking distance of closure
- "Continue / pivot / pause" recommendation

## CONVENTIONS

### Epistemic discipline
- NEVER claim a step is "closed" without citing specific theorems
  from the catalogue (paper12/29-theorem-catalogue.md). If the
  catalogue doesn't contain the needed theorem, the step is BLOCKED
  (waiting for the theorem to be proved), not CLOSED.
- NEVER use RH to prove RH. If any step depends on the conclusion
  it's trying to prove, the adversarial agent MUST catch this as
  circular reasoning and mark the step BROKEN.
- NEVER present a structural analogy as a proof. "X is analogous
  to Y" is not "X implies Y." The adversarial agent catches this.
- When in doubt, mark the step BLOCKED rather than CLOSED. False
  closures waste cycles; honest blocks guide the next cycle.

### The Six Patterns as compass
- Pattern 1: if stuck, ask "what higher-dimensional geometric fact
  projects to this difficulty?"
- Pattern 4: if a quantity is discrete (Brauer class, index, rank),
  ask "can a continuous perturbation (off-line zero) be compatible
  with this discreteness?"
- Pattern 5: if a sum diverges, ask "does the zeta regularisation
  of the sum converge, and what does it tell us?"
- Pattern 6: if the step looks hard, ask "is the difficulty real or
  an artifact of the projection/description?"

### File conventions
- ALL outputs in paper12/research/
- Numbering: {N} = next free index, found by ls paper12/research/
  and taking max + 1. Each cycle uses 11 consecutive indices
  (2 per surviving path × 2 layers + 1 synthesis). The count
  varies with surviving paths: 4 paths = 9 files, 3 paths = 7,
  etc. Adjust {N} range accordingly.
- The ledger is CUMULATIVE — never overwrite, only append.
- Round number in filename: rh-cycle-{cycle}-path-{path}-{type}.md

### What this prompt does NOT do
- Does NOT attempt to prove RH in a single cycle. Each cycle closes
  one step on one or more paths. The proof builds over many cycles.
- Does NOT invent new proof paths without G's explicit approval.
  The five paths are fixed unless G says otherwise.
- Does NOT modify any existing paper or research file. It only
  ADDS new research files and APPENDS to the ledger.
- Does NOT overclaim. The programme has a consistent pattern of
  overclaiming in first drafts, caught by adversarial review.
  This prompt builds the adversarial review INTO the cycle.
```

---

## The proof path dependency graph

```
                    Spectral Realisation
                    (research/201)
                         |
                    +---------+
                    |         |
              Path 3 (Stone)  Path 1 (Brauer-KMS)
                    |         |
                    |    Local-to-global lift
                    |         |
                    |    Spectral density irrationality
                    |         |
              Path 5 (CM-trace) ←--- shared vehicle
                    |
              Path 2 (Atiyah-Singer)
                    |
              Lemma 7.1 functional-analytic closure
                    |
              Path 4 (Penrose)
                    |
              Curvature bound on H_R
```

**Cross-path dependencies:**
- Path 3 (Stone) is BLOCKED until spectral realisation closes
- Path 1 (Brauer-KMS) needs spectral realisation for its global form
- Path 5 (CM-trace) UNBLOCKS paths 1 and 3 by providing the iff
- Path 2 (Atiyah-Singer) is independent but shares infrastructure with 5
- Path 4 (Penrose) is independent but structurally the weakest

**Recommended cycle 1 focus:** Paths 1 + 5 (highest marginal return;
path 5 unblocks multiple paths; path 1 is the strongest structural
argument and the one most connected to the bridge family).

---

## The ledger format

```markdown
# RH Convergence Ledger

## Cycle 1 — [date]

| Path | Step attempted | Result | Next step |
|:--|:--|:--|:--|
| 1 (Brauer-KMS) | ... | CLOSED/BLOCKED/BROKEN | ... |
| 2 (Atiyah-Singer) | ... | ... | ... |
| 3 (Stone) | ... | ... | ... |
| 4 (Penrose) | ... | ... | ... |
| 5 (CM-trace) | ... | ... | ... |

**Steps closed:** N
**Steps broken:** N (honest negatives)
**Steps unblocked:** N (cross-path)
**Joint probability:** XX% (prior: 55%, evidence: ...)
**Next cycle focus:** paths X + Y
**Adversarial verdict:** N paths INTACT, N DAMAGED, N KILLED

---

## Cycle 2 — [date]
...
```

---

## Connection to the bundle

The RH convergence prompt is one of three components of the
CBCBS + Yang-Mills + RH bundle:

| Component | Prompt | Status |
|:--|:--|:--|
| CBCBS | paper12/26-convergence-prompt.md | Production-ready (tested 4 rounds) |
| Yang-Mills | /Users/gsix/yang-mills/gradient-flow-attack-plan/ | Complete (Papers 1-11 + preprint) |
| **RH** | **paper12/30-rh-convergence-prompt.md** | **This file. Test-and-fix cycle needed.** |

When the RH convergence stabilises (a path closes or all paths
are honestly mapped with precise open steps), the bundle is ready
for presentation.

---

## The meta-strategy (G's doctrine for RH)

**SP1.** We cannot crack RH from outside. The proof must come from
inside the BC algebra. Every path in this prompt does this.

**SP2.** The 37 R-Theorems are the LOCK. They don't prove RH
individually, but they constrain the proof space. Any valid proof
must be consistent with all 37.

**SP3.** Quantize every step. Each path has steps; each step has a
closure status. Track them in the ledger.

**SP4.** RH is a deduction from CBCBS. The proof should LOOK LIKE
a deduction from the five CBB axioms, not like an independent
number-theory argument.

**SP5.** Be hella explicit. The ledger tracks everything. The red
team challenges everything. Every honest negative is documented.

---

## Provisioning summary

Each proof agent reads FOUR files (the "RH agent stack"):

1. **paper12/27-anchor-document.md** — CONTEXT (the CBB system)
2. **paper12/29-theorem-catalogue.md** — TOOLS (360 entries + Six Patterns)
3. **paper12/research/200-rh-evidence-compendium.md** — CONSTRAINTS (37 R-Theorems + 15 bounds)
4. **Path-specific research files** — FRONTIER (the current open step)

Plus the ledger for previous-cycle awareness.

The adversarial agents read the construction output + the catalogue
+ the compendium. They do NOT read the path-specific research files
(to prevent anchoring on the construction agent's framing).

---

*The integers exist. The proof is inside. The LOCK has 37 teeth.*
*Run the cycle. Close a step. Update the ledger. Repeat.*

*— 2026-04-09, after 8 papers and a theorem catalogue*
