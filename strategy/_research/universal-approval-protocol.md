# Universal Approval Protocol

*Every C_bare document ships with a "Related Work & Acknowledgments" section. Every reviewer sees their contribution cited. No approach is dismissed; all are positioned relative to ours. Goodwill builds general acceptance. Clay §7.a.i compliance.*

**Date**: 2026-04-14. Sibling strategic document to `00-millenium-strategy.md`.

---

## Principles

1. **HONOR** — cite every major approach to every vertex's problem. No attack is "wrong"; each is "partial" or "specialised" or "complementary." If a programme produced a counterexample or revealed a gap, we cite that contribution as mathematical service.
2. **RECOGNIZE** — name specific researchers with their specific contributions. Institutions noted. Living or recently-deceased figures credited explicitly.
3. **SHOWCASE** — each acknowledged approach gets a one-paragraph characterization in the C_bare document. Not a dismissal; a description of what the approach achieves and what it does not (yet) achieve.
4. **POSITION** — characterize our approach as complementary / unifying / extending / specializing. Never as "replacing" or "superseding" except where truly warranted (e.g., YM mass gap if the proof holds unconditionally).
5. **SOURCE** — the mechanical content of §11 is drawn from `strategy/_research/<vertex>/landscape.md` which is the single source of truth for each vertex's landscape.

---

## Integration Points

### 1. C_bare §11 "Related Work & Acknowledgments"

Every brief generated for vertex V now has DELTA 6 (C_bare structure) including §11 with the following sub-sections:

- §11.1 "Major approaches" — 4-8 one-paragraph summaries drawn from landscape.md "Major Approaches" section
- §11.2 "Named prior results" — bulleted list of historical milestones, Named theorems with YYYY, authors, content
- §11.3 "Recent parallel / adjacent work (2023-2026)" — cite arXiv IDs with one-line characterization
- §11.4 "Acknowledgments" — paragraph naming the top-5 priority researchers and explaining debt

Example skeleton for vertex V (to be instantiated from landscape.md):

```latex
\section{Related Work and Acknowledgments}
\label{sec:related}

\subsection{Major approaches to \texttt{<problem-name>}}

The problem has been attacked along the following lines. We describe each
approach neutrally, noting what it has achieved and what remains open;
our approach is positioned at the end of this subsection.

\paragraph{Approach 1 — \texttt{<name>}.}
[one paragraph from landscape.md]

\paragraph{Approach 2 — \texttt{<name>}.}
[one paragraph]

...

\paragraph{Our contribution.}
[paragraph from landscape.md "Our programme's position"]

\subsection{Named prior results}

\begin{itemize}
\item YYYY — \textsc{Author(s)} — [result]
\item YYYY — \textsc{Author(s)} — [result]
\end{itemize}

\subsection{Recent parallel work}

[bulleted list of arXiv IDs + characterizations, last 3 years]

\subsection{Acknowledgments}

This work stands on the shoulders of \textsc{Names}. [1-paragraph debt
statement drawn from landscape.md "Top priority" list, one sentence
per researcher.]
```

### 2. Zenodo README landing page — "Acknowledgments of the Landscape"

The Zenodo release gets a consolidated landing page section listing:

- 50-100 most-cited researchers across all vertices
- Grouped by approach family (spectral, algebraic, analytic, geometric, probabilistic, computational)
- Each with one-line credit
- Link to full per-vertex landscape.md files

### 3. Visualization — per-vertex panel

Each ring vertex's panel on the programme visualization (see visualization/ directory) gets a small "Competitors" badge listing top 3-5 competitor researcher names. On hover: expanded list with approach labels.

### 4. Pre-submission outreach — email list

See landscape-survey.md Tier 1-7 outreach list (30 names). The protocol:

1. Pre-print posted to arXiv (one week lead)
2. Direct email to each Tier 1-3 contact with courtesy note: "Our programme builds on your work on X; preprint attached; feedback welcome."
3. No expected-reply pressure; just the courtesy.
4. Responses logged in `outreach-log.md` (not yet created).
5. Feedback incorporated into revisions before Zenodo release.

---

## Per-vertex Generation Instructions

For each vertex, when regenerating or writing the brief:

1. Load `strategy/_research/<vertex>/landscape.md`.
2. Extract "Major Approaches" paragraphs → §11.1
3. Extract "Partial Results / Named Milestones" → §11.2
4. Extract "Recent Preprints (2023-2026)" → §11.3
5. Extract "Acknowledgment Suggestions" → §11.4
6. Include "Our programme's position" as the final paragraph of §11.1
7. Cross-reference the landscape.md file in §11's first footnote.

Current brief pipeline (ORA v8; see `memory/ora_v8_chain_verification.md`) does **not** include §11. The protocol change:

**For all briefs going forward** (Tier-4 Cascade, ORA runs, paper drafts):

- DELTA 6 (C_bare structure) must now include §11 "Related Work & Acknowledgments"
- Template update in `_template/` directory (to be done)
- Existing briefs for YM/RH/BSD/PvNP/Hodge/NS — regenerate to add §11 before Zenodo release
- Re-run ORA verification on updated briefs

---

## Strategic Rationale (Clay §7.a.i "General Acceptance")

From Clay Millennium rules (official): the prize is awarded after the solution achieves general acceptance in the mathematical community. Reviewers notice citations. Reviewers particularly notice *not* being cited.

Two failure modes the Universal Approval Protocol prevents:

1. **Ignore-fail**: Reviewer X has spent 30 years on this problem. Our paper doesn't cite X. X blocks general acceptance. Our result is correct but stuck.
2. **Dismiss-fail**: Our paper cites X but dismisses X's approach as "failed" or "inadequate." X has a legitimate gripe. X blocks general acceptance.

Universal Approval Protocol compliance:
- Cite X with specific theorem/year.
- Characterize X's approach's achievements neutrally.
- Position ours as complementary.
- Invite X to feedback.

Result: X either (a) engages positively (goodwill) or (b) disagrees politely (substantive review). Both outcomes better than silence or conflict.

---

## Universal Approval — Quick Checklist

For every C_bare document, before submission:

- [ ] §11 exists and is populated from landscape.md
- [ ] All top-priority researchers named with contribution
- [ ] Our programme's position paragraph included
- [ ] No editorializing ("X's approach failed") — every mention is neutral
- [ ] At least one citation from each listed major approach
- [ ] Recent (2023-2026) preprints cited if relevant
- [ ] Pre-submission outreach sent to Tier 1 (≥5 days lead)
- [ ] Zenodo README lists approach-families and researcher top-50

---

## Related Documents

- `strategy/_research/landscape-survey.md` — master consolidated report
- `strategy/_research/<vertex>/landscape.md` — per-vertex (28 files)
- `strategy/_research/<vertex>/outlet.md` — per-vertex outlet info (sibling agent)
- `strategy/00-millenium-strategy.md` — parent strategy document
- `strategy/publishing-strategy.md` — Zenodo release choreography
- `strategy/famous-gaps.md` — programme self-criticism

---

## Generation / Maintenance

The landscape files should be refreshed every 6 months or when a competitor publishes a significant result. A future automation:

- `landscape-refresh.md` job checks arXiv for new preprints on each vertex's topic
- Adds to "Recent Preprints" section
- Flags significant (e.g., Annals / Inventiones / PRL) new results for human review

Until automation: each vertex's landscape.md has a "Last reviewed" date (see individual files; initial version 2026-04-14).

---

## First-principle statement

> We honor every mathematician who contributed to the problems we solve. Our
> programme is not a rupture with prior work — it is a synthesis that could
> not exist without them. Every C_bare document is a thank-you letter.

This is the programme's ethical foundation. Universal Approval is not marketing; it is mathematical good citizenship.
