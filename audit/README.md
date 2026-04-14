# QG5D Audit Home

*Compliance-audit infrastructure for the quantum-geometry-in-5D programme. Built 2026-04-14.*

*This directory is READ-ONLY for the rest of the programme — do not modify existing paper directories from within /audit/. This is the audit's home; findings live here, not in the papers.*

---

## What is this?

A compliance-audit home for the QG5D programme's target prizes and target venues.

Goal: for every programme paper (50+ of them) and every prize/venue (20+ of them), a clean "does this paper qualify here, and what's the gap?" answer.

Modeled on the Jaffe-Witten 7-requirement itemization in `../strategy/ym/00-millenium-strategy.md §3`. What that document does for YM, this directory does for all six Clay problems plus a dozen other prizes/venues.

## How to use

### Question: "What does Clay require for Yang-Mills?"
→ `clay-millennium/YM/00-problem-statement.md` (verbatim Jaffe-Witten)
→ `clay-millennium/YM/requirements.md` (7-requirement itemization)
→ `clay-millennium/YM/compliance-checklist.md` (our paper08 vs. requirements)

### Question: "Can paper13 go to Annals?"
→ `venues/annals-of-math/submission.md` (Annals guidelines, including AI policy)
→ `per-paper/paper13-rh.md` (paper13's target venues + readiness)

### Question: "What's the readiness of the entire programme?"
→ `compliance-matrix.md` (rows = papers, columns = prizes + venues)

### Question: "What sources were consulted?"
→ `research-log.md` (every web source + finding, timestamped)

## Directory layout

```
audit/
├── README.md                       (this file)
├── compliance-matrix.md            (master table, paper × prize/venue)
├── research-log.md                 (append-only source log)
│
├── clay-millennium/                (six Clay problems + rules)
│   ├── 00-clay-rules/              (verbatim rules + problem-statement PDFs + text extracts)
│   │   ├── clay-rules.md           (Clay §§1-8 verbatim)
│   │   ├── clay-rules-2018.pdf + v2.pdf + .txt
│   │   ├── yang-mills-jaffe-witten.pdf + .txt
│   │   ├── riemann-bombieri.pdf + .txt
│   │   ├── bsd-wiles.pdf + .txt
│   │   ├── hodge-deligne.pdf + .txt
│   │   ├── navier-stokes-fefferman.pdf + .txt
│   │   └── pvnp-cook.pdf + .txt
│   ├── YM/                         (Yang-Mills)
│   ├── RH/                         (Riemann Hypothesis)
│   ├── BSD/                        (Birch-Swinnerton-Dyer)
│   ├── PvNP/                       (P vs NP)
│   ├── Hodge/                      (Hodge Conjecture)
│   └── NS/                         (Navier-Stokes)
│   (each contains: 00-problem-statement.md + requirements.md + compliance-checklist.md)
│
├── prizes-other/
│   ├── breakthrough-mathematics/
│   ├── breakthrough-physics/
│   ├── abel/
│   ├── shaw/
│   ├── wolf-mathematics/
│   ├── wolf-physics/
│   ├── fields/
│   └── nobel-physics/
│
├── venues/
│   ├── arxiv/                      (submission-rules, endorsement, moderation-and-ai-policy, withdrawal-policy)
│   ├── zenodo/
│   ├── annals-of-math/
│   ├── inventiones/
│   ├── jams/
│   ├── cmp/
│   ├── forum-pi/
│   ├── jhep/
│   └── physical-review/
│
└── per-paper/                      (one file per programme paper; 53 files)
    ├── paper1.md
    ├── paper2.md
    ├── ...
    └── paper61-projections-of-the-5d-geometry.md
```

## Key findings at a glance

### Clay gates (from `clay-millennium/00-clay-rules/clay-rules.md`)
1. **Qualifying Outlet publication** — refereed, named editorial board, MathSciNet-indexed.
2. **2-year rule** since Qualifying Outlet publication.
3. **General acceptance** in global mathematics community.
4. **Satisfactorily addresses** the official problem description (§5d — silence is a violation).

### Publication cascade (from `strategy/ym/00-millenium-strategy.md §9`)
```
ZENODO (DOI + timestamp)
   ↓
GITHUB (code + proofs public)
   ↓
ARXIV (via endorser)
   ↓
QUALIFYING OUTLET JOURNAL (starts Clay 2-year clock)
   ↓
COMMUNITY ENGAGEMENT
   ↓
CLAY 2-YEAR MINIMUM
   ↓
CMI PASSIVE MONITORING (no direct submission per §5e)
   ↓
CLAY PRIZE CONSIDERATION
```

### Critical discipline: §5d

Every requirement of the official problem description MUST be addressed. Silence = violation. Named-wall disclosure + bypass route = compliant. This is what `strategy/ym/00-millenium-strategy.md §3-§6` exemplifies.

### Critical venue constraint: AI policy

- **Annals of Mathematics:** "does not consider papers generated using AI products." Strictest.
- **arXiv:** significant AI use must be declared; AI cannot be a named author.
- **Springer journals (Inventiones, CMP):** AI use must be declared (Springer umbrella policy).
- **APS journals (PRD, PRL):** AI use must be declared.
- **JHEP, Forum Pi:** policies less explicit; assume declaration required.

**Implication for QG5D:** Claude Opus 4.6 contribution must be DECLARED transparently, and the mathematical content must be verifiably human-understandable / human-checkable. Heavy-AI-generation papers risk Annals rejection.

## Honest-first discipline

Any claim in this audit is either:
- Cited verbatim to an official source (preferred).
- Synthesized from WebSearch abstracts when the source was inaccessible, with "content synthesized" noted.
- Flagged "NOT FOUND — needs manual check" when the source could not be reached at all.

No requirements are fabricated. Re-fetch flagged items with a browser (Playwright MCP or similar) for paranoid verification.

## Known blockers encountered (2026-04-14)

- `claymath.org` PDF binary extraction: initial WebFetch returned binary preview. Mitigated by direct `curl` + `pdftotext`.
- `claymath.org/millennium/p-vs-np-problem/` returned 404; PDF link located via WebSearch.
- `abelprize.no` nomination page WebFetch timeout.
- `link.springer.com` submission-guidelines pages return 303 redirects or 403 on WebFetch.
- `journals.aps.org` returns 403 on WebFetch.

Essentials captured via WebSearch abstracts; re-fetch pass via browser recommended for paranoid verbatim quotes.
