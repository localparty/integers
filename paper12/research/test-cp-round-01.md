# Meta-report: Convergence Prompt Round 1 Test

*Test of `paper12/26-convergence-prompt.md`, round 1.*
*Tester:* Claude Opus 4.6 (1M), 2026-04-09.
*Output produced:* `paper12/research/192-convergence-round-1.md`.

## 1. Did the prompt run end-to-end?

**Partial.** Phases 1 (read state) and Phase 4 (report-back) completed.
Phase 2 (pull experimental updates) was NOT possible — no web access in
this environment. Phase 3 (parallel agents A–F/G) was SIMULATED
sequentially in one pass; no real Task sub-agents were launched. The
final output file was produced, but it is a *baseline σ-tally against
stale 2023/2018 data*, not the "new-data-in" round the prompt envisages.

## 2. Where did it fail or get stuck?

- **Phase 2, lines 82–100:** the prompt instructs "Pull in the latest
  experimental measurements from CMB-S4, LiteBIRD, DESI, …". No
  fallback instruction for the (very common) case of no web access. I
  had to invent the fallback myself (use the existing research/23
  baseline).
- **Phase 3, lines 102–135:** "LAUNCH PARALLEL CYCLE (5-7 agents)". The
  prompt does not say whether to use Claude Code's Task tool, nor what
  to do when that tool is unavailable. I simulated sequentially.
- **Agent A, lines 104–107:** asks for "full mpmath precision (50 dps)"
  recompute of all 36 formulas. This is ~30 min of computation and the
  prompt doesn't state whether round 1 must recompute or may inherit
  from research/23. I inherited and flagged it.
- **Agent B, lines 108–111:** asks for σ-ratios, but research/23 does
  not carry a σ_exp column — it carries rel. err. only. I had to
  back-derive σ from memory of PDG central values. This is the biggest
  structural gap.
- **Phase 3 Agent E vs §"What it does NOT do" (lines 179–180):**
  **internal contradiction.** Agent E is told to "surface up to 3 new
  postulate relaxations", but the later section forbids new postulate
  relaxations. I resolved by declining Agent E.
- **Output path, line 127 & 174:** `research/{N}-convergence-round-{round}.md`.
  N is ambiguous — is it the next research-note index (192) or the
  round number? I used "next index" convention (192), matching the
  existing research/ numbering.

## 3. What was unclear?

- Whether "σ_exp" means the PDG 1σ uncertainty on the measurement, or
  the framework's own internal uncertainty band.
- Whether round 1 should audit research/190's "36/36 below σ_exp" claim
  or take it as gospel. I audited and surfaced an apparent bookkeeping
  gap at m_Z and 1/α_3.
- Whether "baseline" means research/190 (converged state) or research/23
  (raw formulas). These two disagree for m_Z.
- "Match register from research/24" — I have not read research/24; the
  prompt does not tell me I must, only that I should match its
  "register". Unclear whether that's stylistic or substantive.

## 4. What was missing?

- **A σ_exp column.** Without it, the prompt's core deliverable (the
  N-σ score table) cannot be computed rigorously. The prompt needs to
  either require a prior refactor of research/23 to carry σ_exp, or
  give a fallback heuristic.
- **A "no web access" fallback.** Critical — most test environments
  won't have live WebFetch for CMB-S4 etc.
- **Clear N-naming convention** for the output file.
- **An explicit tool spec** for Phase 3 (Task tool? sequential sim?
  how many tokens per sub-agent?).
- **Round-0 seed file.** There is no prior round for this round to
  diff against, but the prompt's "biggest improvement vs previous
  round" assumes one exists. First-run handling is not specified.
- **Resolution of the Agent E / §"Does NOT do" contradiction.**
- **Instructions for m_Z / 1/α_3 apparent tensions** — does the prompt
  want me to flag bookkeeping gaps or to silently trust research/190?

## 5. Output quality

**5/10.** The output file is structurally correct and surfaces one
real finding (the research/23 ↔ research/190 bookkeeping gap at m_Z).
But the core deliverable — the N-σ score table — is populated with
"est." values because the σ_exp data is not in the input files and web
is not available. G would read it and say: "this is a dry run, not a
convergence round." That's fine for round 1, but the prompt should
state it up-front.

## 6. Top 3 fixes for round 2

1. **Add a σ_exp column to research/23** (or point the prompt at a new
   file, e.g. `research/23-sigma-exp.md`) so Agent B can compute N-σ
   ratios directly without memory-based back-derivation. Right now Phase
   3 / Agent B (prompt lines 108–111) has no way to succeed rigorously.
2. **Add an explicit "no web access" fallback block** after Phase 2
   (insert at prompt line 101). Specify: if no web, (a) use research/23
   baseline, (b) flag the round as "baseline σ-tally", (c) skip Agent
   D, (d) proceed to Agent B anyway.
3. **Resolve the Agent E vs §"What it does NOT do" contradiction**
   (prompt lines 122–124 vs 179–180). Either remove Agent E from the
   default cycle, or reframe it as "surface but do not test new
   relaxations; log them for a separate postulate round".

### Bonus fix (4th):
- **Specify N-naming**: "N = next free research-note index at time of
  run; round = 1,2,3…". Prompt lines 127 and 174 are ambiguous.

---

## The single biggest weakness

**The prompt's core deliverable (N-σ score table) cannot be computed
from the input files it tells you to read.** research/23 carries rel.
err., not σ_exp. Without a σ column or a live PDG fetch, Phase 3
Agent B is structurally under-specified. Everything else is fixable
with small edits; this one requires either a data refactor or a web-
fetch dependency that the prompt does not currently declare.
