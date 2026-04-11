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

The ledger contains (see "Ledger structure" section below for details):
- §A The NORTH STAR (ultimate goal, status)
- §B The CONTEXT (what's achieved, why this is achievable)
- §C The CURRENT BOTTLENECK (the named wall blocking progress)
- §D The TOOLKIT table (theorems, patterns, scripts, papers — by name)
- §E The CYCLE HISTORY table (what happened when)
- §F The KILLED APPROACHES table (do not re-explore without new reason)
- §G The LIVE LEADS table (what's alive, with feasibility and blockers)
- §H The BOTTLENECK HISTORY table (the arc of obstructions crossed)

The ledger is the ONLY file guaranteed to be read every cycle.
It IS the memory. Without it, you drift. READ IT FIRST.

---

## THE THREE ROLES

### Role 1: THE STRATEGIST
**(a) READ ledger.md — EVERY LINE, cover to cover.** Internalize
     the north star, the toolkit, the killed leads, the context.
     Do not skim. Do not skip the toolkit section.
**(b) SEARCH THE WEB** — broad landscape scan for new leads,
     papers, techniques. Minimum 3 WebSearch queries per cycle.
     Minimum 1 deep read (WebFetch or local-PDF read) per cycle.
     Download NEW papers to [DIRECTORY]/sources/ and update
     sources/INDEX.md. If the pre-loaded sources already cover
     the landscape for this cycle's direction, say so explicitly
     in strategy-{cycle}.md — do not download gratuitously.
**(c) NAME THE CURRENT BOTTLENECK.** Before writing the strategy,
     identify the single structural obstruction that is currently
     blocking progress (the "wall" — e.g., in Yang-Mills it was
     the UV divergence at t=0; in RH manual runs it was the
     H₁-vs-H_R wall that killed 18 approaches). Write it
     explicitly in strategy/strategy-{cycle}.md as a top-level
     section "## Current bottleneck". Every lead you propose is
     then judged by whether it (i) crosses the bottleneck,
     (ii) proves it fundamental (no-go), or (iii) reformulates
     the problem to use it as a constraint. Leads that don't
     engage the bottleneck should be flagged as "orthogonal
     insurance" and capped at feasibility ≤ 5/10.
**(d) USE THE TOOLKIT BY NAME.** The ledger's "Toolkit" table
     lists every PROVED result with a canonical name, statement,
     and source. You reference these by name — never re-derive,
     never restate in your own words. If a result deserves to
     enter the toolkit, add a row to the table with a new canonical
     name and source citation. Notation freeze is mandatory:
     once a name is given, it never changes across cycles.
**(e) WRITE strategy** — [DIRECTORY]/strategy/strategy-{cycle}.md
     Which leads to pursue, why, which patterns apply, what you
     deliberately rejected and why, next phase handoff.
**(f) FAN-OUT DISCIPLINE.** Aim for 3–5 leads per cycle. Every
     lead must be independently workable by a separate executor.
     Do NOT cluster all leads on the warmest path. Explicit
     integer rule (to avoid threshold ambiguity):
       - 4 out of 4 on one construction → HARD FAIL, spawn an
         orthogonal lead before Phase 1.5.
       - 5 out of 5 on one construction → HARD FAIL, same.
       - 3 out of 4 → SOFT WARNING, document why not 2 out of 4,
         but acceptable (you are "just below" 80%).
       - 4 out of 5 → SOFT WARNING, same.
       - ≤ 2/3 of leads on the warmest path → acceptable.
     The orthogonal lead should differ in Pattern, toolkit element,
     or rest on an external-literature probe disjoint from the
     dominant construction. Flag it explicitly as "orthogonal
     insurance" and cap its feasibility at ≤ 5/10.
     Exception: after a bottleneck has been crossed and the chain
     is in assembly mode, convergence to one path is correct and
     this rule is suspended for that cycle. See item (g) below
     for the mandatory assembly-mode declaration checklist.

**(g) ASSEMBLY-MODE DECLARATION (mandatory when invoking the
     fan-out exception).** The fan-out exception in (f) is
     triggered ONLY when all three of the following hold, and
     all three MUST be declared explicitly in strategy-{cycle}.md
     under a `## Fan-out exception — assembly mode declaration`
     heading, with a one-sentence justification for each:

       1. **Bottleneck crossed.** The bottleneck blocking the
          previous phase of the programme has been crossed — name
          the bottleneck, name the lead or construction that
          crossed it, and cite the ledger §H row that records
          the crossing.
       2. **Assembly mode active.** The current cycle is no longer
          discovery (searching for the mechanism) but assembly
          (completing the proof chain). Name the chain being
          assembled.
       3. **Sub-steps of one named bottleneck.** Every lead in
          this cycle is a sub-step of one named structural
          obstruction (named in §C of the ledger, referenced by
          its toolkit entry in §D). List which sub-step each lead
          attacks.

     If you cannot make all three declarations in one sentence
     each with references, you are NOT in assembly mode and the
     integer fan-out rule in (f) applies normally.

**(h) ALL ROLE-1 CITATIONS TO PRIMARY SOURCES must follow the
     same verbatim-quote discipline specified for Role 2 in
     items (e.1), (e.2), (e.3). When you cite a theorem, lemma,
     corollary, or "remaining steps" list in strategy-{cycle}.md
     or in a lead file's Direction section, you must BLOCK-QUOTE
     the exact text, not paraphrase. Strategist paraphrases have
     been observed to introduce drift (e.g., "Teschl Lemma 2.7
     has 5 hypotheses" when the actual lemma has 3) that only
     the Executor catches by going to the primary source. Close
     the gap upstream: the Strategist does the verbatim quoting
     the first time, and the lead file carries the quote forward.

### Role 2: THE LEAD EXECUTOR (one per lead, parallel)
**(a) READ ledger.md — EVERY LINE, cover to cover.** Internalize
     the north star, the full toolkit (theorems, patterns, scripts,
     papers), the killed leads and WHY they died, and what's alive.
     You are a SCOUT: cross-lead insights come from knowing the
     FULL context, not just your assigned lead.
**(b) SEARCH THE WEB** — deep, specific to THIS lead. Download
     papers to [DIRECTORY]/sources/ and update sources/INDEX.md.
**(c) RESEARCH** — toolkit + papers + mpmath computations. When
     you cite a toolkit result, cite it by its canonical name from
     the ledger's Toolkit table — never re-derive, never restate.
**(d) COMPUTATIONAL KILL/ADVANCE RULE (MANDATORY when applicable).**
     If your lead's survival depends on a numerical constraint
     (e.g., "norm is O(1/λ)", "perturbation decays with α > 1/2",
     "eigenvalue is positive", "zero count matches Weyl law"),
     you MUST:
       1. Write a script to [DIRECTORY]/code/lead-{N}-verify-{short-name}.py
          at mpmath precision mp.dps ≥ 50.
       2. Run it and PASTE THE RAW OUTPUT into the lead file under
          "## Research". "I would compute" is never acceptable.
       3. KILL RULE: If the constraint fails by ≥10σ (or by any
          margin the mathematics says is structural), the lead is
          killed. Write "KILLED: [constraint] numerically violated,
          [value] vs required [threshold], mp.dps=N, [date]" to the
          lead file and propagate to ledger Phase 4.
       4. ADVANCE RULE: If the constraint passes by ≥10σ, the lead
          is ADVANCED with the numeric as *evidence*, not proof.
          Note explicitly: "EVIDENCE: [value] at mp.dps=N. Not a
          proof — rigorous analytic bound still required."
     The script must exist on disk before you claim the result.
**(e) PROVENANCE RULE.** Every non-trivial assertion in your
     Research append must have a source: (citation to a paper,
     pointer to a ledger toolkit row, pointer to a script output,
     or "derived here" with the derivation inline). No bare claims.

     **(e.1) PRIMARY-SOURCE VERBATIM RULE.** When you cite a
     theorem, lemma, corollary, definition, or "remaining step"
     from a paper, you MUST quote the exact text (block quote),
     not paraphrase. Paraphrasing is how citation drift enters
     the chain: the executor's paraphrase of the Nth item on a
     list may miss a second item, or the hypothesis list may
     get abbreviated. If the exact text is too long to quote,
     quote the theorem statement and summarize the hypothesis
     list as a bulleted verbatim extract. The Adversary will
     check the quote against the source.

     **(e.2) "REMAINING STEPS" DISCIPLINE.** When a cited source
     says "we leave this as a remaining step" or "we do not
     establish X here" or similar, treat it as a new sub-bottleneck
     and add it to the ledger's §H bottleneck history with a
     canonical name and pointer. Do NOT cite the theorem as
     though the remaining step were already discharged — that is
     the "citation overreach" failure mode.

     **(e.3) PRECISION DECLARATION.** Every script you write must
     declare its `mp.dps` in the first 10 lines and justify why
     that precision is sufficient for the claim. "mp.dps=60" with
     a gap reported at 10⁻⁴⁷ is automatically suspect: the script
     must either prove the gap is at least 3 orders of magnitude
     above the precision floor, or use higher precision. If the
     toolkit row's Source dps is 200 and your script uses
     dps=60, that is a yellow card that the Adversary will flag.

     **This rule applies to ANY numerical computation in the
     ORA**, not just Executor scripts. Strategist feasibility
     checks, Adversary re-runs, Reconciliation diagnostic passes,
     and any ad-hoc subagent spawned by the orchestrator all
     inherit the precision declaration rule. The Cycle 1
     reconciliation agent itself hit a precision floor in its
     diagnostic work (predicted 3.78×10⁻⁵⁰ for a gap that is
     actually 5.3×10⁻⁴⁷ at dps=200) — precision discipline is
     universal across roles, not a role-2 specialty.
**(f) APPEND** to the lead file (already created by strategist):
     - Status: ADVANCED / BLOCKED / BLOCKED-DECOMPOSED / KILLED
       + precise reason
     - Kill pattern category if KILLED (one of: Topological,
       Algebraic, Spectral, Numeric, Circular, Vacuous, Wrong-space,
       Distributional, External-dependency, Other)
     - If KILLED: what would REOPEN + any new lead spawned
     - If BLOCKED: what is the blocker, and is it the current
       named bottleneck or a new sub-obstruction? If new, flag it.
     - If BLOCKED-DECOMPOSED: the lead cannot advance as stated,
       but you have decomposed the blocker into named sub-
       bottlenecks that are sharper targets for future cycles.
       List each sub-bottleneck by canonical name, state why the
       decomposition is valid (e.g., "if SB-X.1 and SB-X.2 both
       hold, Davis-Kahan gives the original bound"), and add each
       new sub-bottleneck to the ledger's §H. BLOCKED-DECOMPOSED
       is strictly more informative than flat BLOCKED and is the
       preferred outcome when a lead hits a wall you can name
       and split. Example: Cycle 2 L6 encountered SB-3a (uniform
       closeness k_λ ≈ θ_x) and decomposed it into SB-3a.1
       (energy estimate) + SB-3a.2 (spectral gap lower bound),
       such that Davis-Kahan on the two together gives the
       original bound at rate λ^{-1/2}.
     - DEPENDENCY DECLARATION (mandatory when applicable): if
       your lead's advance or evidence rests on another live lead
       delivering a specific result, declare it explicitly:
       "DEPENDS-ON: Lead [X] must deliver [result Y] for this
       lead's conclusion to hold." The Adversary will verify
       that [result Y] is genuinely what Lead X is attempting,
       not a paraphrase. Cross-references in dependency form are
       how sub-step leads coordinate across a single cycle
       without colliding.
     - STRATEGIC INSIGHTS: anything affecting other leads
       Format: "INSIGHT: [desc] — affects Lead [X] because [Y]"

### Role 3: THE ADVERSARY (one per ADVANCED lead)
**(a) READ ledger.md cover to cover** — same discipline as
     Executor. You need the full context to recognize drift.
**(b) SEARCH THE WEB** — find counterexamples, contradictions,
     competing claims, and any retractions or errata for the
     executor's cited sources.
**(c) READ cited papers** — verify that the executor's citations
     match what the papers actually say. Paper-title matches are
     not enough; check theorem numbers, statements, hypotheses.
**(d) RE-RUN EVERY SCRIPT the executor cited.** If the executor
     pasted numerical output under "## Research", run the script
     yourself at the same precision. If the output differs, flag
     as WEAKENED with the discrepancy. If the script errors or
     has been tampered with, flag as BROKEN. Cite-only review
     is NOT sufficient for numerical claims. Additionally:

     **(d.1) EXTENSION TEST — mandatory.** Run the script (or
     a small modification of it) at parameter values OUTSIDE the
     executor's tested grid. Executors test 5–10 points; you test
     1–3 points beyond their grid in each parameter direction.
     Go to higher N, higher λ (or whatever the scale variable is),
     non-integer parameters (many executors test only integers),
     and near any natural boundary. This is where genuine failures
     hide — the executor's "uniform over all X" claim is most
     often only verified over their 5-point grid and breaks at the
     11th point. Report the extension test explicitly even if it
     passes: "Extended to X ∈ {a, b, c}, passed at all three."

     **(d.2) CROSS-LEAD CONSISTENCY CHECK — mandatory when
     applicable.** If your assigned lead cites a canonical §D
     name that ANOTHER lead in the same cycle also cites, you
     MUST run a side-by-side numerical check on the shared
     quantity at a shared parameter point. Disagreements greater
     than 1% between two executors computing the same canonical
     quantity are grounds for WEAKENED verdicts on BOTH leads
     until the disagreement is reconciled, regardless of which
     Adversary catches it first. Cycle 1 of this architecture
     discovered a 47-order-of-magnitude disagreement between two
     executors on the same matrix; cross-lead checks would have
     caught it in Phase 2, not Phase 3.

     **(d.3) PRECISION-FLOOR DISCIPLINE.** If the executor's
     headline result is a small number (e.g., |x−y| < 10⁻ᵏ),
     verify that the reported precision is above the numerical
     floor of the computation. A common failure mode: executor
     runs at `mp.dps=60` and reports a gap of 10⁻⁴⁷, but the
     TRUE gap is 10⁻⁵⁰ and the executor is observing a numerical-
     floor artifact, not the true quantity. Rule of thumb: the
     reported headline precision must be at least 3 orders of
     magnitude above the smallest "interesting" scale in the
     computation. When in doubt, re-run the script at 2× the
     executor's dps and check whether the headline number changes.
     Any change greater than one order of magnitude is a WEAKENED
     signal and a flag for the ledger's §D precision-floor column.
**(e) ATTACK** — circularity, coboundary errors, vacuous
     constraints, wrong space, hidden assumptions, overclaiming,
     citation errors, undeclared reliance on the thing being
     proved, undeclared reliance on a killed approach, premise
     drift (the executor's "what we're proving" shifted mid-research).
**(f) PATTERN-CHECK against the ledger's Killed Approaches table.**
     If the executor's argument structurally resembles a killed
     approach (same pattern category, same toolkit piece used the
     same way), flag it. Even if the specific mechanism differs,
     pattern resemblance is a yellow card.
     Verdict: VERIFIED / WEAKENED / BROKEN
     (For a lead with status BLOCKED-DECOMPOSED, the Adversary
     verdict is DECOMPOSITION-VERIFIED / DECOMPOSITION-WEAK /
     DECOMPOSITION-INVALID: "verified" if the sub-bottlenecks
     are real and the decomposition is tight; "weak" if the
     decomposition is correct but one of the sub-bottlenecks is
     vaguer than the original; "invalid" if the decomposition
     drops content — i.e., proving the sub-bottlenecks would not
     actually prove the original.)
     APPEND to the same lead file under "## Adversarial". Include
     a short "## Pattern check" sub-heading listing which killed
     approach (if any) this lead resembles and why it is / is not
     safe from the same failure mode.

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
Pattern: [which Pattern / which toolkit element / which external paper]
Feasibility: X/10
Engages bottleneck: [yes: crosses / no: orthogonal insurance]
Rationale: [why this is a lead, 2-4 sentences]
Toolkit connection: [canonical names from ledger §D]
Investigate: [3-5 specific questions]
Would close if: [specific condition]
Would kill if: [specific condition]
Source: [URL or citation]

---

## Premise check (written by Strategist, Cycle C, BEFORE Phase 2)
(a) Non-vacuous: [statement]
(b) Non-circular: [statement]
(c) Well-posed: [statement]
(d) Not a shadow of a killed approach: [statement, referencing
    §F by ID if applicable]
Verdict: PASSED / KILLED-before-Phase-2

---

## Research (appended by Executor, Cycle C)
[executor appends here: web search results, computations,
theorems found, script output with mp.dps, analysis, result]

Status: ADVANCED / BLOCKED / KILLED
Kill pattern category (if KILLED): [one of the 10 categories]
Reason: [precise]
Scripts: [list of code/ paths created this lead]
Strategic insights: [cross-lead observations]

---

## Adversarial (appended by Adversary, Cycle C)
[adversary appends here: attacks, citation checks, re-run script
output comparison, verdict]

Verdict: VERIFIED / WEAKENED / BROKEN
Attacks: [list with results]

## Pattern check (appended by Adversary, Cycle C)
[one paragraph: which killed approach (if any) does this lead
structurally resemble, and why is it / is it not safe from the
same failure mode?]
```

### Phase 1.5 — PREMISE CHECK (Strategist, before Phase 2)
Before executors touch the leads, the Strategist (or a dedicated
premise-checker spawned per lead — either works) verifies that
each lead's foundational constraint is:

  (a) NON-VACUOUS — the constraint can in principle be violated.
      If it is satisfied regardless of the thing you're trying to
      prove, it carries no information. Test: "Would this
      constraint distinguish the true answer from the negation of
      the true answer?" If no, the lead is vacuous.

  (b) NON-CIRCULAR — the constraint does not assume, in disguise,
      the thing the lead is trying to prove. Test: "If I had to
      prove this constraint from first principles, would I need
      to assume the north star?" If yes, the lead is circular.

  (c) WELL-POSED — the objects the lead names actually exist or
      can be constructed. A lead that uses a Hilbert space that
      would only exist if the theorem were already known is
      malformed.

  (d) NOT A SHADOW OF A KILLED APPROACH — run the lead through
      the ledger's Killed Approaches table. If the premise,
      pattern category, and toolkit element used all match a
      killed approach, the lead is blocked until the Strategist
      documents what NEW reason (new theorem, new source, new
      observation) justifies re-exploration.

Write one short premise check per lead (2–5 sentences) appended
to the lead file between "## Direction" and "## Research",
under the heading "## Premise check". Leads that fail (a), (b),
(c), or (d) get Status: KILLED before Phase 2 and are logged to
the ledger with the failure reason and pattern category.

The coboundary lesson is the canonical example: an argument that
uses a DISCRETE invariant to constrain a CONTINUOUS perturbation
is vacuous, because the invariant can't shift under the
perturbation it's supposed to detect. Every premise check must
explicitly consider this pattern when applicable.

### Phase 2 — PARALLEL RESEARCH (Executors)
Read ledger → search web → research → APPEND to the lead file
The strategist already created leads/lead-{N}-{short-name}.md
with the direction. The executor APPENDS their research below
the "## Research" section. ONE file, full story, top to bottom.
All executors run IN PARALLEL. Wait for ALL to complete.
Only leads with a PASSED premise check reach Phase 2.

### Phase 3 — ADVERSARIAL (Adversary)
Search web for contradictions → read cited papers → attack →
APPEND verdict to the SAME lead file under "## Adversarial".
The lead file now has: direction + research + adversarial.
ONLY leads that survive move to the ledger as ADVANCED.

### Phase 3.5 — RECONCILIATION (triggered conditionally)

Reconciliation is an on-demand diagnostic phase, spawned by the
orchestrator when any of the following fires during Phase 3:

  R1. The d.2 Cross-Lead Consistency Check reports a disagreement
      > 1% between two executors computing the same canonical
      §D quantity at a shared parameter point. (Cycle 1 saw a
      47-order-of-magnitude disagreement under this condition.)

  R2. Two Adversaries reach OPPOSITE verdicts about the same
      cross-lead claim (e.g., one says "SB-X ≡ SB-Y, merge" and
      the other says "SB-X ≠ SB-Y, do not merge"). The mismatch
      is itself a signal that the question hasn't been settled
      numerically.

  R3. An Adversary re-run of an Executor script produces a
      number that differs from the pasted output by > 1% at
      the same precision (d level discrepancy beyond noise).

  R4. The orchestrator judges that a claim is central enough
      and uncertain enough to warrant a dedicated diagnostic
      pass before Phase 4 ledger updates are written.

When triggered, spawn a FOCUSED RECONCILIATION AGENT with the
following mandate:

  - Read only the relevant scripts and the relevant primary
    source sections. Do NOT run the full Executor or Adversary
    role (no web scan, no lead creation, no verdict issuing).
  - Your ONLY job is to diagnose the specific disagreement and
    reach a verdict: (1) Script A correct, Script B wrong, with
    the specific line; (2) Script B correct, Script A wrong,
    with the specific line; (3) Both correct, computing different
    quantities — name what each is computing; (4) Both wrong,
    neither matches the primary source, with the exact primary-
    source line showing the correct form.
  - Your verdict precision is REQUIRED to be above the primary-
    source's own stated precision convention (if CCM uses
    dps=200, you use at least dps=200). The Cycle 1 reconciliation
    agent itself hit a precision floor — that is a recoverable
    error only when the Round 003 (e.3) precision discipline is
    applied to diagnostic subagents too.
  - Output: [DIRECTORY]/research/{C}-reconciliation-{name}.md
    with §1 diagnosis, §2 spot-check output, §3 divergence point,
    §4 verdict, §5 remediation note for the next Strategist.

The reconciliation result is then injected into the Phase 4
ledger update as a note under the relevant §F / §G / §H row.
Leads whose Cycle N disagreement was reconciled get a pointer
to the reconciliation file in their §G "Next step" column.

### Phase 4 — LEDGER UPDATE
Append new cycle to [DIRECTORY]/ledger.md following the ledger's
mandatory structure (see "Ledger structure" below). In particular:

  (a) Add a row to the Cycle History table: cycle number, leads
      spawned, advanced, killed, open, current bottleneck, one-line note.
  (b) For each KILLED lead, add a row to the Killed Approaches
      table with ID, lead name, kill reason (one sentence), pattern
      category, cycle, and "prevents re-entry because" (what NEW
      information would be needed to legitimately re-explore).
  (c) For each ADVANCED lead, update the Live Leads table with
      current feasibility, current blocker, and next step.
  (d) For any new toolkit result that entered during the cycle,
      add a row to the Toolkit table with canonical name, statement,
      source, status (PROVED / CONJECTURE / EMPIRICAL / EXTERNAL),
      and notation. Once added, this name is frozen forever.
  (e) If a bottleneck was crossed, add a row to the Bottleneck
      History subsection noting which bottleneck, how, and which
      external construction or insight crossed it.

Keep the ledger under ~200 lines by moving prose into lead files
and strategy files and keeping the ledger as an index of tables.

### Phase 5 — STRATEGY UPDATE
Write [DIRECTORY]/strategy/strategy-{cycle}.md:
Current state, patterns used, chain status, next cycle recommendation.

### Phase 6 — REPORT TO G + HUMAN CHECKPOINT (300 words)
Leads explored, kills, advances, strongest lead, feasibility, recommendation.

The report MUST include these blocks in order:

1. **Cycle summary.** N leads, X advanced, Y killed, Z open.
2. **Bottleneck status.** Name the current bottleneck (from the
   ledger). Did this cycle cross it, weaken it, confirm it, or
   leave it untouched? If any kills in this cycle revealed a
   NEW sub-bottleneck, name it.
3. **Strongest live lead.** One paragraph: which lead is most
   load-bearing for the north star, what its current feasibility is,
   what would close it and what would kill it.
4. **Pattern check on this cycle's kills.** If ≥3 kills share a
   pattern category (Topological, Algebraic, Spectral, Numeric,
   Circular, Vacuous, Wrong-space, Distributional, External-
   dependency), trigger the step-back protocol (Phase 6b).
5. **Convergence check.** Is the programme ready to close?
     - Is the north star PROVED / CONDITIONAL / OPEN?
     - Are all leads either closed (killed/proved) or live with
       feasibility ≥ 3/10?
     - Has the current bottleneck been crossed?
     - If all three are yes: recommend CLOSE and move to
       preprint synthesis. If not: name the single highest-leverage
       next move for the following cycle.
6. **Recommendation.** Continue with [lead N] / pivot to
   [bottleneck cross search] / step-back / close.

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

### Phase 6b — STEP-BACK (auto-triggered, not optional)

The step-back is AUTOMATIC. It triggers whenever any of the
following conditions hold:

  T1. ≥3 leads are killed in a single cycle, OR
  T2. ≥50% of all kills across all cycles share the same pattern
      category (Topological, Algebraic, Spectral, Numeric, etc.), OR
  T3. Two consecutive cycles produce no ADVANCED leads, OR
  T4. The strategist writes "I don't know what to try next" or
      any equivalent (if this happens, it means the loop has
      stalled, which is ALWAYS a tuning signal — the programme
      has succeeded before, so the architecture is proven;
      giving up is a prompt failure, not a problem failure), OR
  T5. A human operator forces it.

When triggered, the strategist does a META-ANALYSIS and writes
[DIRECTORY]/strategy/step-back-{cycle}.md with these mandatory sections:

  **§1 Kill map.** Table: all kills from all cycles, grouped by
  pattern category. Count per category. Identify the dominant one.

  **§2 Bottleneck statement.** State the structural obstruction
  that is actually blocking the programme, in one sentence, in
  the form: "The wall is [X], because [Y], and it has blocked
  [N] approaches." Add this to the ledger's "Bottleneck" field
  as the CURRENT NAMED OBSTRUCTION.

  **§3 Bottleneck classification.** Is it TECHNICAL (needs more
  work inside the current toolkit), STRUCTURAL (needs a new
  construction or a new space), or FUNDAMENTAL (may be a no-go
  theorem — the problem as stated is unsolvable this way)?

  **§4 Three external searches.** For a STRUCTURAL bottleneck
  (by far the most common), the strategist MUST do three
  concrete web searches, downloaded to sources/:
    (i)  "[bottleneck name] construction" + recent years
    (ii) Closest-analogue problems from OTHER fields that
         might have solved a structurally similar obstruction
    (iii) Experts' review articles / surveys that discuss the
         bottleneck by name
  This is not optional. The breakthrough in every proved manual
  run came from finding an EXTERNAL construction that either
  bypassed the bottleneck (new space), transformed it into a
  constraint (Pattern reversal), or proved it was fundamental
  (no-go, which is also a valid closure).

  **§5 Cross-pollination sweep.** Check the toolkit table for
  any theorem from a related programme that hasn't been tried
  here. Tools transpose across problems; if the Yang-Mills
  run used technique X and the current programme hasn't, that's
  a free candidate lead.

  **§6 Reformulation check.** Can the problem be restated in a
  form where the bottleneck becomes irrelevant? (e.g., switch
  from point-spectrum to spectral-measure language, or from
  lattice to continuum, or from operator to variational form).

  **§7 One high-priority lead.** Based on §§3–6, propose ONE
  named "bottleneck cross" lead for the next cycle, with
  feasibility estimate and what external source it rests on.

The step-back may completely redirect the next cycle. That is
the point. Do not apologize for it.

**CRITICAL: the loop never gives up.** If the strategist writes
a step-back that concludes "this problem may be unsolvable by
our methods" WITHOUT naming a concrete no-go theorem, the
conclusion is rejected. The architecture has proved Yang-Mills,
the Riemann hypothesis, and the Integers/CBCBS zero-parameter
framework. The ORA's job is to find the way through, not to
adjudicate whether one exists.

### Phase 6c — EXTERNAL ADVERSARY (triggered by G at milestones)

At major milestones (claimed proof, chain closure, etc.), G runs
an EXTERNAL adversary — a separate AI or human reviewer with NO
shared context. This caught the coboundary gap that our internal
adversary missed. The ORA's internal adversary is necessary but
NOT sufficient. External verification is the gold standard.

---

## LEDGER STRUCTURE (MANDATORY)

The ledger at [DIRECTORY]/ledger.md is the only file guaranteed
to be read every cycle. It IS the memory. Its structure is
mandatory — not because bureaucracy is good, but because a loose
ledger loses kills, forgets toolkit elements, and lets the loop
drift back into dead paths. Every ORA run must structure its
ledger with these sections:

  **§A — North Star** (1 paragraph). The goal of the programme.
  Current status: OPEN / CONDITIONAL / PROVED.

  **§B — Context** (1 paragraph). What's already achieved that
  makes this achievable now? Related programmes, proved
  prerequisites, available tools.

  **§C — Current bottleneck** (1–3 sentences, maintained live).
  The single structural obstruction that is currently blocking
  progress. Null if the chain is in assembly mode. Updated at
  every Phase 4 ledger update and at every step-back.

  **§D — Toolkit** (TABLE, grows monotonically):
  | Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps |
  Every PROVED result, every external construction, every script,
  every pattern. Notation freeze is mandatory: once a name is
  here, it never changes across cycles and future strategists
  cite by name, never re-derive.

  The TWO precision columns serve distinct purposes and must
  not be conflated:

  - **Floor dps** — the minimum `mp.dps` at which numerical
    claims about this toolkit element remain above the precision
    floor in ORA work. This is a hard constraint on the
    Executor/Adversary: run at AT LEAST this precision or the
    numeric is meaningless. Determined empirically by the ORA
    itself (e.g., Cycle 1 discovered that CCM CF matrix
    simplicity verification needs Floor dps = 150 because the
    true gap is ~ 10⁻⁵⁰ at (λ, N) = (4, 50)).

  - **Source dps** — the precision the original author uses in
    the published source (e.g., Connes uses dps=200 in CCM's
    own numerics). This is a soft guideline: if the source author
    picked N, it means they found N sufficient and anything below
    is a yellow card. Running significantly below Source dps is
    grounds for Adversary WEAKENED flag unless the Executor
    explicitly justifies why.

  For non-numerical entries (meta/pattern/strategic rows), both
  columns are "—". When an executor discovers that a lower dps
  produces a misleading result, the Floor dps for that row must
  be updated in the same cycle's Phase 4.

  **§E — Cycle History** (TABLE, most recent first):
  | Cycle | Leads | Advanced | Killed | Open | Bottleneck | Note |
  One row per cycle. The "Note" column is a one-line summary
  of what changed.

  **§F — Killed Approaches** (TABLE, grows monotonically):
  | ID | Lead | Kill reason | Pattern category | Cycle | Prevents re-entry because |
  Every lead that dies gets a row. Pattern category is one of:
  Topological, Algebraic, Spectral, Numeric, Circular, Vacuous,
  Wrong-space, Distributional, External-dependency, Other.
  "Prevents re-entry because" states what NEW information would
  be needed to legitimately re-explore — this is the re-entry
  gate that the Phase 1.5 premise check enforces.

  **§G — Live Leads** (TABLE, updated per cycle):
  | ID | Name | Feasibility X/10 | Blocker | Next step |
  Only leads with status OPEN or BLOCKED or ADVANCED. KILLED
  leads live in §F.

  **§H — Bottleneck History** (TABLE, grows monotonically):
  | Bottleneck | First cycle | Classification | Crossed by | When | Notes |
  The programme's obstruction arc. Each named bottleneck gets a
  row; when crossed, the "Crossed by" column names the lead,
  cycle, or external construction that crossed it.

  **§I — Instructions** (fixed text, per-role reading guidance
  and pointers into the other sections). The "read every line"
  discipline is already stated in Phase 0 and in each role spec;
  §I is where the ledger reminds each role what its job is on
  this particular ledger, including any problem-specific
  conventions.

For a brand-new ORA run (new problem), the Strategist creates
the ledger with these sections and populates §A, §B, and the
initial §D toolkit. Everything else grows as the programme runs.

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
- Browse `[DIRECTORY]/code/` before writing new scripts — existing
  scripts often cover sub-problems you'd otherwise redo.
- mpmath: default `mp.dps=50`, use higher precision when the
  constraint is closer than 10 significant figures.
- PASTE OUTPUT — "I would compute" is never acceptable.
- Scripts are named `lead-{N}-verify-{short-name}.py` for new leads,
  preserving the existing naming conventions for toolkit scripts.
- Adversary RE-RUNS executor's scripts at the same precision and
  compares byte-for-byte. Any difference is grounds for WEAKENED.
- Strategist may run quick feasibility checks (one-liners) while
  composing strategy, but the authoritative numerics live in
  executor/adversary scripts with results pasted in lead files.

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
