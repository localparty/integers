# Full Review Cycle Runbook — QG5D Series (Papers 1–7)

This document describes the complete pre-submission stress-test pipeline for the
QG5D seven-paper series. Run it whenever the papers have been significantly
revised, before any new submission round.

The pipeline has five stages. Each stage must complete before the next begins.
All agents use `model: "sonnet"` and run in parallel within each stage.

---

## Stage 1 — Per-Paper Referee Reports

Launch one specialized referee agent per paper (papers 1–7) **in parallel**.
Each agent reads:
- `paperN/etc/01-journal-referee.md` (the referee identity and interrogation points)
- All source `.md` files in `paperN/`
- Key appendices

Each agent writes its report to:
- `paperN/journal-reviewer/report.md`

The referee prompts are at:
- `paper1/etc/01-journal-referee.md` — KK theory, zeta regularization, spin-statistics, Goroff-Sagnotti expert
- `paper2/etc/01-journal-referee.md` — CMB Boltzmann, leptogenesis, N_eff, S8/H0 tensions expert
- `paper3/etc/01-journal-referee.md` — Black hole information, Page curve, AMPS, island formula expert
- `paper4/etc/01-journal-referee.md` — KK reduction, Witten theorem, gauge-Higgs unification, Weinberg angle expert
- `paper5/etc/01-journal-referee.md` — Lattice QCD, string tension, confinement, baryon asymmetry expert
- `paper6/etc/01-journal-referee.md` — Inflationary cosmology, reheating, dilaton, EWPT, LISA expert
- `paper7/etc/01-journal-referee.md` — M-theory, G₄ flux, GVW superpotential, KKLT/LVS, tadpole expert

Each agent prompt should follow this structure:
> You are running a physics journal referee review. Read the referee prompt at
> `paperN/etc/01-journal-referee.md` in full and follow it precisely. Read all
> source `.md` files in `paperN/`. Write your complete report to
> `paperN/journal-reviewer/report.md`. Structure: 1. Executive summary
> 2. Point-by-point findings rated (A) GENUINE GAP / (B) CLOSABLE GAP /
> (C) SOUND with reasoning 3. Recommendation to editors.

**Wait for all 7 reports before proceeding.**

---

## Stage 2 — Per-Paper Gap Responses and Draft New Content

Launch one agent per paper (papers 1–7) **in parallel**.
Each agent reads:
- `paperN/journal-reviewer/report.md` (the Stage 1 report)
- All source `.md` files in `paperN/`

Each agent writes to:
- `paperN/journal-reviewer/gap-responses.md`

The gap-response file must contain, for every A-rated and B-rated finding:
1. An author response explaining the fix
2. Draft new content — the actual text, equations, and derivations to be added
   to the paper (written at publication quality, not as a sketch)

Each agent prompt:
> You are acting as the author of Paper N responding to a referee report.
> Read `paperN/journal-reviewer/report.md` in full. Read the relevant source
> `.md` files in `paperN/`. For every A-rated (GENUINE GAP) and B-rated
> (CLOSABLE GAP) finding, write: (a) an author response explaining the fix,
> and (b) draft new content at publication quality — the exact text, equations,
> and derivations to be inserted into the paper. Write the complete response to
> `paperN/journal-reviewer/gap-responses.md`. Do not skip any A or B finding.

**Wait for all 7 gap-response files before proceeding.**

---

## Stage 3 — Apply Fixes to Source Files

Launch one agent per paper (papers 1–7) **in parallel**.
Each agent reads:
- `paperN/journal-reviewer/gap-responses.md` (Stage 2 output)
- `paperN/journal-reviewer/report.md` (for context)
- All source `.md` files in `paperN/` (to find where to apply each fix)

Each agent edits the source `.md` files directly. It may also create new `.md`
files in `paperN/` if a gap response calls for a new section or appendix,
following the existing naming convention.

**Do not touch** `journal-reviewer/`, `etc/`, or `figures/` directories.

Each agent prompt:
> You are applying reviewer-mandated fixes to Paper N. Read
> `paperN/journal-reviewer/gap-responses.md` in full — it contains every
> A-rated and B-rated finding with proposed author responses and draft new
> content. Read `paperN/journal-reviewer/report.md` for context. For each
> finding, read the relevant source `.md` files in `paperN/` and apply the fix
> by editing those files directly. The draft new content is what goes into the
> paper — preserve mathematical content exactly. If a gap response calls for a
> new appendix or section, create it following the existing naming convention.
> Do not touch `journal-reviewer/`, `etc/`, or `figures/`. Apply every A and
> B finding without skipping any.

**Wait for all 7 fix agents before proceeding.**

---

## Stage 4 — Cross-Paper Consistency Review

Launch a single agent reading all 7 revised papers and all 7 reports.

The referee prompt is at:
- `paper9/etc/01-cross-paper-referee.md`

The agent writes to:
- `paper9/journal-reviewer/report.md`

Agent prompt:
> You are running a cross-paper consistency review for the QG5D 7-paper series.
> Read the full referee prompt at `paper9/etc/01-cross-paper-referee.md` and
> follow it precisely — it contains your identity, reading list, and all
> interrogation points (Parts A–G). Read all 7 individual referee reports at
> `paper{1-7}/journal-reviewer/report.md`, all 7 gap-response files at
> `paper{1-7}/journal-reviewer/gap-responses.md`, and the key source `.md`
> files from each paper listed in the referee prompt. The papers have been
> revised — assess cross-paper consistency of the current source files.
> Write your complete review to `paper9/journal-reviewer/report.md`. Structure:
> 1. Executive summary with priority-ordered issues 2. Point-by-point findings
> (A/B/C rated) for each Part 3. Parameter audit table tracking shared
> quantities (ξ, r₃, M_X, T_reh, R, N_eff, sin²θ_W, m_H) across all papers
> 4. Recommended submission order.

**Wait for the report before proceeding.**

---

## Stage 5 — Apply Cross-Paper Fixes

Launch one agent per paper that has findings requiring changes **in parallel**.
Read `paper9/journal-reviewer/report.md` first to identify which papers need
edits and exactly what changes are needed (specific sections and wording are
given in each finding's "What is needed" block).

For each paper with A or B findings:
> Apply the cross-paper consistency fixes to Paper N identified in
> `paper9/journal-reviewer/report.md`. For each finding affecting Paper N,
> read the relevant source `.md` file, then apply the targeted edit — typically
> one paragraph or a few sentences. Preserve all existing content; these are
> additions and clarifications, not rewrites. Do not touch `journal-reviewer/`,
> `etc/`, or `figures/`.

---

## Notes

- **Reviewer run archiving**: Each paper's referee prompt archives the previous `journal-reviewer/` output to `paperN/reviewer-runs/rNN/` before starting. Run history is preserved in these numbered directories (r00, r01, r02, ...) following the pattern at `~/yang-mills/math-referee-runs/`.

- **Delete any generated `.tex` files** before starting (they are regenerated):
  `find /Users/gsix/quantum-geometry-in-5d-latex -name "*.tex" -delete`

- **Source of truth**: the `.md` files in each `paperN/` directory. The
  `journal-reviewer/` subdirectory holds review artifacts only.

- **Model**: use `sonnet` for all agents in all stages.

- **Stages 1, 2, and 3** each have 7 parallel agents. Stages 4 and 5 are
  sequential (4 first, then 5).

- **Stage 5 agents** are parallel with each other but depend on Stage 4
  completing first.

- **Do not launch Stage 4** until all Stage 3 agents have written their fixes —
  the cross-paper reviewer reads the revised source files, not the pre-fix
  versions.
