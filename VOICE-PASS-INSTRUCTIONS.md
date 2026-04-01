# Voice Pass Instructions — Quantum Geometry in 5D

> **For the agent doing the voice consistency pass.**
> Read this file completely before touching anything.
> The human will review all changes before committing.

---

## What This Project Is

A theoretical physics paper claiming perturbative finiteness of 5D
Kaluza-Klein quantum gravity via the Epstein-Terras theorem. This is a
serious result. The mathematics is correct and has been verified. Your
job is NOT to change the physics — only to make the prose consistent.

**Do not modify any equation, claim, theorem, appendix reference, or
citation. Do not add or remove physics content. Only fix prose.**

---

## The Problem

The main paper sections (1-8 and 5X) were written across multiple sessions
by multiple agents. The voice is inconsistent. Some sections are more formal,
some more conversational, some use "we" consistently, some switch to "I" or
passive voice. Some have leftover draft notes that need to be removed.

The appendices are deliberately NOT part of this pass — they are technical
documents and their voice variation is acceptable.

---

## The Target Voice

Read the abstract first (`paper/abstract.md`) — this is the gold standard
voice for the paper. Then read Section 5.X (`paper/paper-section-5x-quantization-bridge.md`) — this is the best-written main section.

The voice is:
- First person plural: "we propose," "we establish," "we show"
- Direct and confident — no hedging words like "perhaps" or "it seems"
- Precise — every claim is labeled (established / proposed / conjectured)
- Readable by an advanced physics graduate student
- NOT overly formal or stilted — it reads, it flows
- Technical terms used correctly without excessive explanation

---

## Files to Touch (in this order)

1. `paper/abstract.md` — already good, read-only reference, DO NOT change
2. `paper/paper-section-1-introduction.md` — fix voice, remove draft notes
3. `paper/paper-section-2-framework.md` — fix voice, remove draft notes
4. `paper/paper-section-3-five-phenomena.md` — fix voice
5. `paper/paper-section-4-1-aharonov-bohm.md` — fix voice
6. `paper/paper-section-4-2-spin-statistics.md` — fix voice
7. `paper/paper-section-5-gravity-bridge.md` — fix voice, remove draft notes
8. `paper/paper-section-5x-quantization-bridge.md` — already best, minimal fixes
9. `paper/paper-section-6-connections.md` — fix voice
10. `paper/paper-section-7-philosophy.md` — fix voice
11. `paper/paper-section-8-conclusion.md` — fix voice

**DO NOT touch:**
- `paper/abstract.md` (reference only)
- `paper/appendices/` (all appendices — leave completely alone)
- Any `.md` file in the root directory
- Any file in `paper/sources/`
- `00-discovery-log.md`
- `PROJECT-MASTER.md`

---

## Specific Things to Fix

### 1. Remove all draft notes sections

Every section has a `## Notes for Revision` block at the bottom with
checklist items like `- [ ] Fix this` or `- [ ] Add that`. These are
internal working notes and must be removed from the final paper.

Look for sections that start with `## Notes for Revision` or
`## Notes for Review` and delete everything from that header to the end
of the file (or to the next real section, whichever comes first).

Also remove the frontmatter status blocks at the top of each section
that look like:
```
> **Status:** First full draft
> **Audience:** Advanced undergraduates...
> **Goal:** ...
```
These are also internal notes, not paper content.

### 2. Fix voice inconsistencies

- Use "we" throughout (not "I", not passive voice where avoidable)
- "The framework proposes" → "We propose"
- "It can be shown" → "We show"
- "One might argue" → remove or rewrite directly
- "It is worth noting" → remove, just say the thing
- "Interestingly," → remove, let the content be interesting

### 3. Fix tense consistency

- Past tense for things we've already established: "we showed," "we proved"
- Present tense for things that are true: "the e-dimension is," "spin is"
- Future tense only for genuine predictions: "short-range gravity experiments will test"

### 4. Remove redundant preambles

Phrases like "In this section, we will..." or "We now turn to..." at the
start of sections — cut them. Start with the content.

### 5. Normalize section headers

All section headers should be title case:
- "The Framework" not "The framework"
- "Toward Quantum Gravity" not "toward quantum gravity"

---

## What NOT to Do

- Do not change any equation
- Do not change any citation or reference
- Do not add new content or new claims
- Do not remove any physics content — only prose scaffolding and draft notes
- Do not change appendix cross-references (e.g., "Appendix B" stays "Appendix B")
- Do not change section numbering
- Do not rewrite entire paragraphs — targeted fixes only
- Do not "improve" the physics arguments — they are correct as written

---

## How to Work

1. Read the file fully before editing anything
2. Make edits using the filesystem edit tool (targeted replacements)
3. After editing each file, do a final read to check the edit landed correctly
4. Do NOT commit anything — the human will review and commit

---

## The One Paragraph Summary of What the Paper Claims

(So you understand what you're editing and can maintain appropriate tone)

Reality is five-dimensional: (x, y, z, t, e). The fifth dimension e is
circular — a compact U(1) fiber. Quantum mechanics is the quantum theory
of the e-circle. The 5D Einstein equations produce gravity and
electromagnetism from the same geometric object. The compact e-circle
converts the non-renormalizable divergences of 4D quantum gravity into
finite quantities via the Epstein-Terras theorem: the leading UV
divergence vanishes at every loop order (S₀^L = 0), and subleading terms
are Epstein zeta values at non-positive integers — always finite. The
Goroff-Sagnotti divergence that proved 4D gravity non-renormalizable in
1986 vanishes in the 5D theory. The theory is perturbatively finite and
predictive. A testable prediction: gravitational deviations at ~21 μm.

---

## When You're Done

Leave all files saved but do NOT run git add or git commit.
Write a brief summary of what you changed in each file.
The human will review the diff and commit themselves.
