# Link 7 Wave 3 Critic: Collapse Proposal — Newton decomposition

**Verdict: SURVIVED (with one editorial flag)**

**Wave:** 3
**Critic:** Claude Sonnet 4.6, 2026-04-13
**Input:** `nodes/L7-collapse.md` (Wave 2 Author proposal), `critiques/link-07-critic.md` (Wave 1 BROKEN)
**Scope:** Attack the collapse proposal, not the original link.

---

## Attack Vector A — Dependency check

**Claim under attack:** Zero downstream links cite L7 as upstream.

**Independent verification method:** Grep of all 19 Wave 1 critique files
(`critiques/link-01-critic.md` through `link-17-critic.md`) for the patterns
`Link 7`, `L7`, `Newton decomp`, `Newton`, and `Step 7`.

**Result:** The grep returns zero hits across links 01, 01b, 02, 03, 04, 05,
06, 08, 09, 10, 10b, 11, 12, 13, 14, 15, 16, 17. The only file returning hits
is `link-07-critic.md` itself (the Wave 1 verdict being collapsed).

**Bonus — preprint body text:** A separate grep of all `preprint/sections/`
files for "Newton" returns exactly four locations:

| Location | Content |
|:---------|:--------|
| `05-continuum-limit.md` line 1561 | Summary table row (the entry being deleted) |
| `05-continuum-limit.md` line 1913 | In-section duplicate table row (also being deleted) |
| `I3-N-dependence-tracking.md` lines 382-386 | Step 7 gloss (being merged into Step 6) |
| `G-multi-time-slice-analysis.md` lines 57-378 | Appendix G internal audit only |

No Newton invocation appears in the §5.5 or §5.6 proof body, in any lemma
statement, or in any intermediate derivation. The Author's dependency-check
claim is **rigorously correct**. Zero downstream links depend on L7.

**Vector A: PASSES.**

---

## Attack Vector B — Appendix G content and the Author's reading of the quotes

**Claim under attack:** The Author's three quoted passages from Appendix G
are verbatim and support the conclusion that Newton decomposition "is the
wrong tool" for extracting Δ̂ factors.

**Independent verification:** Direct read of
`G-multi-time-slice-analysis.md` at the cited sections.

**§3.4 verbatim (lines 153-157):**
> "If all derivative terms vanish and $\mathcal{M}^{(0)} = 0$ by
> $\mathcal{C}$-symmetry, we get
> $\langle 1|\delta E_k^{d=6}(0)|1\rangle_c = 0$ -- too strong.
> This means the Newton decomposition is the wrong tool for extracting
> $\hat{\Delta}$ factors. Something else produces them."

Author's quoted form matches verbatim except minor formatting (em-dash
rendered as `--` in source). **Quote verified.**

**§7.3 verbatim (lines 377-383):**
> "Conjecture 1 at $d_O = 6$ stands, but the derivation of Mechanism 2
> requires correction. The Newton decomposition is valid as dimension
> counting. The $\hat{\Delta}^2$ suppression comes from the spectral
> gap in the intermediate-state sum of the composite operator, not from
> lattice forward differences acting on the external state."

Author's quoted form matches. **Quote verified.**

**§6.2 verbatim (lines 300-308):**
> "**Lemma 2.1 (Newton decomposition):** Valid as dimension-counting.
> Correctly identifies derivative content. Does not directly produce
> $\hat{\Delta}$ factors.
> **$\mathcal{C}$-symmetry elimination:** Valid and exact..."
> "**Steps 5-7 (operator norm bounds):** Valid as stated."

Author's quoted form matches. **Quote verified.**

**Does Appendix G have a different conclusion — Newton decomposition right
for one use, wrong for another?** Yes, and the Author correctly identifies
this nuance. Appendix G explicitly assigns three residual validities to
Newton decomposition (dimension counting; C-parity argument; Steps 5-7
operator norm bounds). The Author explicitly acknowledges all three at
§Step 6/§Integrity check and correctly shows they are absorbed into L6,
L8-9, and L11 respectively. No single one constitutes a standalone proof
link. The Author's reading of Appendix G is correct and complete.

**One potential attack: does Appendix G §6.2 "Steps 5-7 (operator norm
bounds) valid as stated" constitute a standalone link?** The bounds are
*algebraic* (the word "algebraic" is explicit in §6.2), and their output
— $\|\mathcal{M}^{(2)}_{00}\| \leq C'' g_k^4$ — feeds into L11
(C_new g_k^4 Δ̂² bound). The Author notes this at §Step 6/Integrity check
item 3: "absorbed into Link 11 source." That absorption is defensible;
the bound does not independently produce the n ≥ 2 survival claim L7
asserts. This is a weakening risk but not a breakage: Steps 5-7 appear
in Appendix G as supporting commentary, not as a proof chain link, and
the L11 source field in PROOF-CHAIN.md already cites §5.5.

**Vector B: PASSES. Minor residual risk: Appendix G §6.2 Steps 5-7 have
non-trivial content that feeds L11. The Author's absorption is defensible
but a referee may ask for explicit attribution. Flag as editorial note,
not a structural defect.**

---

## Attack Vector C — Renumbering proposal

**Claim under attack:** Renumbering old L8-L18 → new L7-L17 is the right
editorial choice; the alternative (italic note-row keeping L7 as a tombstone)
is inferior.

**Cross-reference exposure:** Grep of the entire preprint for "Link 8",
"Link 9", ... "Link 18" (both in `preprint/` and `chain-verification/`)
returns **zero hits** in preprint body text. The only numbered-link
citations appear in:
- `PROOF-CHAIN.md` §IV.1 table (the table being rewritten)
- `preprint/sections/05-continuum-limit.md` lines 1561 and 1913 (the
  rows being deleted/rewritten)
- `chain-verification/critiques/link-*.md` (the critic files, which
  will themselves be renumbered or archived as part of the editorial pass)

This finding **strengthens** the Author's renumbering case: there are
zero in-text cross-references of the form "Link 8" anywhere in the preprint
sections. Renumbering the table is fully contained. The downstream critic
files use filenames `link-08-critic.md` etc. but these are archival records,
not cited text. No reader cross-reference is broken.

**Is the "italic note row" approach safer?** No. The Author's three
justifications are valid: a tombstone row creates a visible gap in a
numbered proof chain; calling what is now the first spectral step "Link 8"
immediately after a blank/tombstone "Link 7" is editorially confusing; and
the chain's §IV.4 and §IV.5 already describe the sequence as numbered steps.
The cleaner editorial choice is renumbering.

**One residual risk the Author misses:** The Author proposes that in the
renumbered table, Link 11's source field change from "Steps 10, 10b" to
"Steps 9, 10" (old-L10 → new-L9, old-L10b → new-L10). This is internally
consistent. However, §IV.4 of PROOF-CHAIN.md contains a free-text sentence:
> "using the $K$-uniform spectral lemma constant established via
> Hastings-Koma exponential clustering (\S5.5.3 Step 3(i))"

This refers to "Step 3(i)" — a sub-step label internal to §5.5.3, not a
proof-chain step number. It is unaffected by renumbering. No impact.

The Author also does not audit the §IV.5 free-text sentences for "steps
6--14" and "Steps 15--17":
> "the continuum mass gap $\Delta_\infty > 0$ unconditionally (steps 6--14)"
> "The gradient-flow programme (Steps 15--17) is unconditional"

After renumbering, what were steps 6-14 (L6 through old-L14) become steps
6-13 (L6 through new-L13). The continuum mass gap is now established through
step 13 (new numbering for old step 14, Δ∞ > 0). The Author's renumbered
table shows Δ∞ > 0 at new L14 (= old L14, no shift because 10b absorbs the
slot). Wait — re-examining: old L10b → new L10 (not shifted), so new L11
= old L11, new L12 = old L12, new L13 = old L13, new L14 = old L14, etc.
The Author's own renumbered table confirms new L14 = Δ∞ > 0. So "steps
6-14" in §IV.5 free text remains accurate after renumbering. No impact.
Steps 15-17 also map identically (old 15, 16, 17 → new 15, 16, 17). No
impact. The free-text sentences are safe.

**Vector C: PASSES. The Author's renumbering proposal is correct and the
one free-text risk I identified (§IV.4 "Step 3(i)") is a subsection label,
not a chain step. No free-text breakage.**

---

## Attack Vector D — LaTeX compilation of PROOF-CHAIN.md

**Claim under attack:** If PROOF-CHAIN.md is LaTeX-compiled, the italic
note row must become a footnote.

**Search method:** `find /Users/gsix/quantum-geometry-in-5d-latex/ -name "*.tex"` returns **no results**. There are no `.tex` files anywhere in the
`paper08-yang-mills` tree or the broader `quantum-geometry-in-5d-latex`
directory.

**Confirmation:** PROOF-CHAIN.md is 182 lines of pure Markdown with no
LaTeX preamble, no `\documentclass`, no `\begin{document}`. The file is
Markdown-only. The preprint sections are all `.md` files.

**Consequence:** The Author's S2 self-suspicion caveat ("if PROOF-CHAIN.md
feeds a LaTeX pipeline, replace the italic note row with a footnote") is
rendered moot. There is no LaTeX pipeline. The italic note row is
editorially acceptable as-is for the Markdown-format file.

**However:** A secondary risk exists that was not raised by the Author.
The italic note row in a Markdown pipe table is non-standard. GitHub-
flavored Markdown and Pandoc both render it, but the row's cells are
`*[note]*` and `*The n ≥ 2 survival....*`. If a pipeline converts the
`.md` to PDF via Pandoc with LaTeX backend (common for preprint
submission), the inline italic markdown inside a table cell may render
incorrectly depending on the Pandoc version and table style. This is a
minor submission-tooling risk, not a structural defect. The fix (if
needed) is trivial: replace the note row with a paragraph directly
following the table.

**Vector D: PASSES on the structural question (no .tex pipeline exists).
Minor Pandoc-rendering risk noted; not a breakage.**

---

## Attack Vector E — Bonus grep: "n ≥ 2" and "Newton" across preprint

**"Newton" across all preprint sections:** 14 hits, all in Appendix G
(internal audit) and the three table rows / I3 gloss being removed.
No body-text invocations in §5.5 or §5.6 lemmas.

**"n ≥ 2" as a quoted or standalone mathematical expression:**
The grep for `n ≥ 2` in `05-continuum-limit.md` returns only lines 1561
and 1913 (the table rows). No intermediate lemma in §5.5 or §5.6 states
"n ≥ 2 survives" as a result derived from Newton decomposition. The n ≥ 2
lower bound appears in §5.5.4 (dev(Tr(DF)²) ≥ 2) and Part III.3 (dim-6
classification), but those are attributed to the spectral mechanism and
Symanzik classification, not to Newton decomposition.

**Vector E: PASSES. No additional Newton or n ≥ 2 locations would be
affected by the collapse beyond the four explicitly enumerated by the
Author.**

---

## One Attack the Author Did Not Anticipate

**The I3 Step 7 gloss mis-states the Newton claim.** I3 lines 382-386 state:

> "For $\mathrm{SU}(N)$, the trace $\mathrm{Tr}(F^3)$ vanishes by
> $\mathcal{C}$-symmetry for all $N$."

This is a **C-symmetry** result, not a Newton decomposition result. The I3
gloss is using "Newton decomposition" as a label for a step whose content
is actually C-parity elimination. The Author proposes merging this gloss
into I3 Step 6 (C-elimination) — which is exactly right. But the Author
does not call out that the I3 gloss misattributes the mechanism. This
misattribution is not a defect in the collapse proposal; it confirms it.
Newton decomposition is invoked in I3 as a step label whose mathematical
content already belongs to Step 6. The collapse is correct.

---

## Summary

The Wave 2 Author's collapse proposal for Link 7 is **structurally sound**
on all five attack vectors. The dependency claim is independently verified
(zero downstream citations, confirmed by exhaustive grep of all 17 other
critic files and all preprint section bodies). The three Appendix G quotes
are verbatim-verified. The renumbering proposal is feasible and free-text
safe. PROOF-CHAIN.md is Markdown-only; no LaTeX pipeline caveat applies.
The bonus grep finds no additional affected locations.

**Two residual notes (editorial, not structural):**

1. Appendix G §6.2 "Steps 5-7 operator norm bounds" feeds L11; the
   Author's absorption is defensible but an explicit attribution note
   in L11's source field ("+ Appendix G §6.2 algebraic bounds") would
   preempt a referee question.

2. The italic note row in a Markdown pipe table carries a minor
   Pandoc-to-PDF rendering risk. If the preprint is submitted via a
   Pandoc pipeline, replace the note row with a paragraph following
   the table.

Neither note is a structural defect in the collapse. Link 7 was a ghost.
The collapse removes it cleanly. The chain is 17 proved links.

**Verdict: SURVIVED.**

---

*Wave 3 adversarial critic, chain-verification run, Yang-Mills Paper 08.*
*Voice register: §J canon.*
