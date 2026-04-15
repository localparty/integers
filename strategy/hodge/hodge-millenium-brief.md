# Hodge Millennium Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Instructs the PAC to audit the Hodge chain against the 6 Deligne Clay requirements, then synthesize B_bare + C_bare + internal artifacts. B_full and C_full DEFERRED until bare locks and parallel-agent composition-backward runs.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## GOAL

Produce a Clay-compliance-audited Hodge deliverable in **bare mode only** this run. Three concrete files at the end:

**A. Internal artifacts** — scaffolding (same as x-ray + ym bundle pattern):
- `strategy/hodge/pac-output/runs/run-NN/blackboard.md`
- `strategy/hodge/pac-output/runs/run-NN/compliance-map.md` (8-link × 6-requirement, 48 cells)
- `strategy/hodge/pac-output/runs/run-NN/vertices/hodge/` (per-link artifacts)
- `strategy/hodge/pac-output/runs/run-NN/kills.md`
- `strategy/hodge/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/hodge/pac-output/runs/run-NN/arbiter-decisions.md`
- `strategy/hodge/pac-output/runs/run-NN/commit-memo.md`

**B_bare. Clay-shaped X-RAY** — `strategy/hodge/deliverables/hodge-clay-bare.md`:
- Formal theorem skeleton, ZERO prose paragraphs
- ≤ 15 pages of math-only content
- Structure mirrors Deligne §1-§2 requirements 1:1

**C_bare. Beyond-Clay X-RAY** — `strategy/hodge/deliverables/hodge-beyond-bare.md`:
- Bonus theorem skeleton (~~5D derivation~~ M⁵ derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D derivation" → "M⁵ derivation" -->, pins, cross-Clay, Tate parallel, André motivated, intermediate Jacobian)
- ZERO prose, ≤ 15 pages

**B_full and C_full are DEFERRED.** Do not write them this run. They are composed later by parallel agents from the 60-project reservoir once B_bare + C_bare LOCK.

---

## DELTA FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode

New dual mode: **compliance-audit + bare-deliverable-synthesis**.

- Read hodge live PROOF-CHAIN + strategy doc + Deligne §1-§5 + Clay Rules §4-§8
- Walk 8 links × 6 Deligne requirements = 48 audit cells
- Per cell: emit PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation
- Assemble compliance map
- Synthesize B_bare (Clay-shaped theorem skeleton)
- Synthesize C_bare (Beyond-Clay bonus skeleton)
- Defer B_full and C_full

Note: unlike YM, no prior X-RAY run exists for hodge. If an x-ray run is desired as scaffolding, construct it first under `strategy/x-ray/proof-chain/hodge/` before compliance mapping.

### DELTA 2 — Primitives

- **VERIFY** — each link against each Deligne requirement
- **DECOMPOSE** — SILENT verdicts to named walls or new links
- **CONSTRUCT** — new links needed to address SILENT gaps (bare: theorem statement + citation only; no prose)
- **BYPASS** — when direct construction fails, find alternate route via capacitor transposition (e.g., Route A → Route B substitution)
- **EXCISE** — NOT APPLICABLE (all 6 Deligne requirements mandatory)
- **EXTRACT** (new) — extract theorem statements + dimensions + equations + figure-shells from existing programme papers into bare format
- **DISCLOSE** (new) — any OPEN-BUT-ADDRESSED verdict emits an explicit NAMED WALL tag with bypass-route citation

### DELTA 3 — The "bare" discipline

B_bare and C_bare contain ONLY:

- **Formal theorem statements** (numbered, with dependency graph)
- **Definitions** (formal)
- **Equations** (numbered, with citation)
- **Figures** (ASCII or TikZ-ready skeleton; label + caption only, no surrounding prose)
- **Numbers** (dimensions, codimensions, scope bounds, known-cases enumeration, confidence percentages) — in tables with citations
- **Proof-chain analytics** (compliance map, named walls, RIGIDITY/SYMMETRY metrics)
- **Citations** (every claim cites programme paper + specific proof location, e.g., "paper29-hodge Link 3" or "paper31 §A.3 Theorem T.7.2")

B_bare and C_bare contain NONE of:

- Introduction paragraphs
- Motivation paragraphs
- Historical context
- Discussion sections
- Proof details in prose (only statement + citation-to-programme-proof)
- Worked examples in prose
- Conclusion paragraphs
- "We show that..." narrative

If a section heading in B_bare naturally attracts prose (e.g., "§3 Overview of the approach"), REMOVE the section. Bare has no overview — it has theorems.

### DELTA 4 — Output A (internal artifacts)

Standard PAC output structure. Same pattern as x-ray bundle run-01 and ym bundle.

**Compliance-map.md format** (the key new artifact):

```
# Hodge Compliance Map — 8 links × 6 Deligne requirements

| Link | Req 1 (proj non-sing / C) | Req 2 (Hodge decomp + filt + Griff) | Req 3 (rational, AH obstr) | Req 4 (cl(Z) / Chern / analytic) | Req 5 (main assertion) | Req 6 (all codim p, all dim N) |
|------|---------------------------|-------------------------------------|----------------------------|-----------------------------------|------------------------|-------------------------------|
| L1   | PROVED [cite]             | ...                                 | ...                        | ...                               | ...                    | ...                           |
| L2   | ...                       | ...                                 | ...                        | ...                               | ...                    | ...                           |
| ...  | ...                       |                                     |                            |                                   |                        |                               |
| L8   | ...                       |                                     |                            |                                   |                        |                               |

## Verdict summary per requirement

- Req 1: PROVED N% / PARTIAL N% / OPEN-BUT-ADDRESSED N% / SILENT N%
- Req 2: ...
- ...

## SILENT cells (new named walls)

- L.M vs Req.K: ... → new named wall W_N "..."
- ...

## Critic attacks + arbiter decisions

[per-cell attack record]
```

### DELTA 5 — Output B_bare structure

Fixed 16-section structure for `strategy/hodge/deliverables/hodge-clay-bare.md`:

```
# Hodge Clay-Ready X-Ray (BARE MODE)

## §1 Statement of the Problem (Deligne §1 verbatim)
[verbatim quote; include Hodge decomposition isomorphism (Eq. 1), Hodge filtration F^p, Hodge class group H^{2p}(X, Q) ∩ H^{p,p}(X); no prose commentary]

## §2 Main Theorem
[formal theorem statement; reference proof to programme papers paper29-hodge + paper31-baum-connes]

## §3 Requirements Map (compliance overview)
[6-row table: Req | verdict | programme-paper citation(s)]

## §4 Definitions
[formal definitions: projective non-singular variety X, Hodge decomposition H^n = ⊕H^{p,q}, Hodge filtration F^p, Hodge class, algebraic cycle, cl(Z), intermediate Jacobian J_p(X)^0, motivic Galois group G_mot, BC-motivated class]

## §5 Scope (projective non-singular, NOT Kähler)
[theorem statement that scope is projective smooth /C; cite Chow + GAGA; acknowledge Zucker counterexample for Kähler (ref [11] in Deligne)]

## §6 Hodge Structure on Cohomology
[theorem statement of Hodge decomposition + filtration + Griffiths transversality; citation]

## §7 Hodge Classes (rational, not integral)
[definition + AH-obstruction acknowledgement; citation]

## §8 Algebraic Cycles / cl(Z) / Chern correspondence
[theorem statement connecting cl(Z) ↔ Chern classes of algebraic vector bundles (Deligne Remark ii); citation]

## §9 Main Assertion — Every Hodge class is rational-algebraic
[theorem statement; dependency on Links 1-8; explicit NAMED WALLS W1, W2, W3]

## §10 Route A — Endomotive construction (Links 1-5) (with W1 disclosure)
[theorem statements per link + explicit NAMED WALL for W1 (Links 3-4 motivic Hodge filtration / standard conjecture D)]
[bypass route citation: paper31-baum-connes motivic BC extension + arXiv:2510.21562 for abelian-variety-powers slice]
[audit status: OPEN for generic BC-motivated class]

## §11 Route B — Geometric Langlands → Hitchin → Hodge (Link 6)
[theorem statement; cite Gaitsgory-Raskin 2024 (arXiv:2405.03599)]

## §12 Route Composition (Link 7, with W3 disclosure)
[theorem statement + explicit NAMED WALL for W3 (Route A + Route B compose via 2025 preprint 5-step algorithm); audit status: OPEN]

## §13 Motivic Functoriality to all Smooth Projective (Link 8, with W2 disclosure)
[theorem statement + explicit NAMED WALL for W2 (hardest wall, arguably as hard as full Hodge); bypass: restriction to BC-motivated + André motivated recovery for abelian varieties]

## §14 Coverage by Codimension / Dimension
[table: codim p | dim N range | verdict (PROVED / PARTIAL / OPEN-BUT-ADDRESSED) | citation]
[p=1 all N: PROVED (Kodaira-Spencer, Lefschetz (1,1))]
[abelian varieties all (p,N): PROVED via André motivated / absolutely Hodge]
[CM elliptic curves → abelian-variety-powers slice: PROVED (arXiv:2510.21562)]
[generic projective, p≥2: OPEN-BUT-ADDRESSED via Routes A+B]

## §15 Named Walls (all OPEN-BUT-ADDRESSED items)
[for each: name, description, bypass-route citation, audit status]

## §16 Numbers Table
[every dimension bound, codimension, confidence, known-cases count — with programme citation]

## §17 References (AMS-format, programme papers only)
[every programme paper cited with §-level precision; Deligne reference list [1]-[11] from Deligne §6 for external context only]
```

Writing discipline enforced:
- Each section ≤ 1 page typically
- No "introduction paragraph" — go straight to theorem
- No "we note that" — state the theorem
- ASCII figures allowed in §3 / §14 analytics
- Number tables in §14 and §16 only

### DELTA 6 — Output C_bare structure

Fixed 10-section structure for `strategy/hodge/deliverables/hodge-beyond-bare.md`:

```
# Hodge Beyond-Clay X-Ray (BARE MODE)

## §1 The ~~5D Geometric Derivation~~ M⁵ Geometric Derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Geometric" → "M⁵ Geometric" --> of Hodge Filtration
[theorem statement: F^p on H^n(X, C) arises from the ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> projection P_B / P_D / P_O filter; KK-spectrum decomposition induces Hodge grading; citation paper1 + paper61]

## §2 Zero Free Parameters
[table: parameter | value | determined by | programme citation; emphasize that codimension-p grading is geometric not chosen]

## §3 Programme Pins Relevant to Hodge / Period Side
[table: pin ID | observable / motivic datum | predicted | measured / classical value | source paper]
[include period ratios for abelian varieties, CM L-values relevant to BSD cross-cut, Chern-class integer indices]

## §4 Cross-Clay Connections
[sub-theorems:
  Hodge ↔ RH (endomotives / BC spectral data, Link 1);
  Hodge ↔ BSD (CM abelian varieties, motivated classes inherit arXiv:2510.21562);
  Hodge ↔ YM (Chern-K-theoretic anomaly cancellation);
  Hodge ↔ Baum-Connes (K-theory ↔ algebraic vector bundles via Chern character);
  Hodge ↔ Schanuel (period relations constrained by algebraic independence);
  Hodge ↔ P vs NP (spectral-gap / Popa rigidity — if applicable via motivic channel)]
[each with theorem statement + citation]

## §5 Tate Conjecture Parallel (bonus, related problem)
[theorem statement: Tate over number fields K shares motivic structure; Galois ↔ Hodge parallel; citation]

## §6 Absolutely Hodge / André Motivated (bonus recovery)
[theorem statement: on abelian varieties, Hodge classes are "absolutely Hodge" (Deligne [3]) and "motivated" (André [1]); our framework recovers this unconditionally for the CM-abelian slice; citation]

## §7 Intermediate Jacobian / Griffiths Group Structure (Deligne §3)
[theorem statements on J_p(X) = extension of (p,p) classes by J_p(X)^0 = H^{2p-1}(X,Z) \ H^{2p-1}(X,C)/F^p; Griffiths subgroup A_p(X); Voisin infinite-rank quotient [9]; citation]

## §8 Computed Examples (numerical / explicit)
[table: variety | dim | codim p | Hodge classes identified | algebraic cycle | citation]
[include: Example 1 (Künneth components cl(Δ)_{a,b}); Example 2 (hard Lefschetz inverse class z)]

## §9 Proof-Chain Analytics (beyond-Clay depth)
[dependency graph between 8 links + two routes; additional cross-cuts to 6 programme vertices]

## §10 References
```

Same bare discipline — zero prose.

### DELTA 7 — Composition-backward deferral

B_full and C_full are **NOT PRODUCED THIS RUN**. They are DEFERRED until:

1. B_bare and C_bare LOCK (no SILENT verdicts, structure correct, routes reconciled)
2. User triggers parallel-agent composition-backward step

When composition-backward fires (future run):
- Index the 60-project reservoir (all Papers, session logs, PROOF-CHAIN.md files, X-Ray transcripts)
- Per-section retrieval: each B_bare/C_bare section gets its related material pulled
- Per-section composition: parallel agents (one per section) compose prose from retrieved material
- Integration pass: arbiter stitches sections into final LaTeX

This run produces ONLY bare. Do not attempt to write prose in this run.

### DELTA 8 — Citation discipline

Every theorem, definition, equation, number, figure in B_bare and C_bare must cite:
- Programme paper reference (paperNN-short-name)
- Specific proof location (§N, Theorem T.M, Lemma L.K, Link N, Appendix A.J)

Format: `(paperNN-short §X Theorem T.Y)` or `(paperNN-short Link N)` or `(paperNN-short Eq. (Z.W))`.

Examples:
- `H^2 case follows from exp exact sequence 0 → Z → O → O* → 0` (paper29-hodge Link 5; classical Kodaira-Spencer [7])
- `Standard conjecture D holds on abelian-variety powers` (paper29-hodge Link 4; arXiv:2510.21562)
- `Endomotives encode Artin motives` (paper29-hodge Link 1; CCM arXiv:math/0512138)
- `Geometric Langlands proved` (paper29-hodge Link 6; Gaitsgory-Raskin arXiv:2405.03599)

Uncited claim = FAIL. Arbiter returns B_bare for revision.

### DELTA 9 — Publication override

Same as sibling bundles. OVERRIDES `publishing/strategy.md`:
- Zenodo first (priority timestamp)
- GitHub public (code + data + proofs)
- arXiv via referral (easier once Zenodo public)
- Journal submission (starts Clay 2-year clock; Annals / JAMS / Inventiones / Acta tier)
- No direct Clay submission (CMI §5e)

See `00-millenium-strategy.md` §9 for full cascade.

### DELTA 10 — Named-wall disclosure discipline

The Hodge chain has THREE named walls (not one as in YM). Each must be explicitly disclosed in B_bare §10-§13 and §15 as NAMED WALL. Required fields for each:

**W1 — Motivic Hodge Filtration (Links 3-4)**
- **Name**: W1 (motivic Galois acts on de Rham respecting Hodge filtration + standard conjecture D for BC-motivated)
- **Status**: OPEN-BUT-ADDRESSED (PARTIAL for abelian-variety-powers slice)
- **Bypass route**: Motivic Baum-Connes extension + 2024 std conjecture D result for ab var powers
- **Bypass citation**: paper31-baum-connes; arXiv:2510.21562; paper29-hodge Links 3-4
- **Closure scope**: BC-motivated class (BSD-CM slice inherits)
- **Audit pending**: generic BC-motivated extension; full G_mot Hodge-filtration compatibility
- **Effect if audit fails**: restrict claim to abelian-variety slice + André motivated recovery
- **Effect if audit passes**: W1 upgrades to PROVED for BC-motivated class

**W2 — Motivic Functoriality to All Smooth Projective (Link 8)**
- **Name**: W2 (extension from BC-motivated class to ALL smooth projective varieties)
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass route**: restrict Clay claim to BC-motivated class, disclose residual scope; André motivated recovery covers abelian-variety slice
- **Bypass citation**: paper29-hodge Link 8; Deligne §5 (motivic functor fully faithful equivalence)
- **Closure scope**: acknowledged-hard (arguably as hard as Hodge itself per PROOF-CHAIN comment)
- **Audit pending**: any route to functoriality
- **Effect if audit fails**: Clay submission claims Hodge for BC-motivated class, not full statement; residual scope disclosed
- **Effect if audit passes**: full Hodge conjecture

**W3 — Route Composition (Link 7)**
- **Name**: W3 (Routes A endomotive + B geometric Langlands compose to Hodge for BC-motivated class)
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass route**: 2025 preprint's 5-step algorithm
- **Bypass citation**: paper29-hodge Link 7; 2025 preprint (L^2 Hodge theory + Lefschetz sl_2 + Chow-motivic integration)
- **Closure scope**: BC-motivated class
- **Audit pending**: 5-step algorithm verification end-to-end
- **Effect if audit fails**: individual routes still valid; no composite conclusion
- **Effect if audit passes**: Route-A + Route-B composite delivers Hodge for BC-motivated class

Transparency on all three walls is what makes §5d compliance work. Silence here fails §5d.

---

## PROCEDURE

### Step 1 — Read inputs (mandatory, in order)

1. `strategy/hodge/00-millenium-strategy.md` — the strategy doc (sibling of this brief)
2. `solutions-with-prize/paper29-hodge/PROOF-CHAIN.md` — the 8-link live chain
3. `solutions/paper31-baum-connes/PROOF-CHAIN.md` — motivic BC extension (Route A support)
4. Deligne's "The Hodge Conjecture" §1-§6 (extract from the Clay PDF or verbatim in strategy doc §1)
5. Clay Rules §4-§8 (summary in strategy doc §2)
6. If hodge x-ray exists under `strategy/x-ray/proof-chain/hodge/` — read it; if not, note absence and proceed

### Step 2 — Build compliance map

For each (link, requirement) cell in the 8 × 6 = 48-cell matrix:
- Author: VERIFY whether the link addresses the requirement; emit verdict + citation
- Critic: attack the verdict; propose alternative
- Arbiter: decide; record rejected alternative as footnote

Write `compliance-map.md`. Summarize by requirement (percentage of each verdict class).

### Step 3 — Address SILENT verdicts

For each SILENT cell:
- DECOMPOSE into a new named wall OR
- CONSTRUCT a new link with theorem statement + citation OR
- BYPASS via capacitor transposition (cite capacitor cell)

Update compliance map. No cell may remain SILENT at end of this step.

### Step 4 — Synthesize B_bare

Walk the 17-section structure (§1-§17). Each section pulls from relevant compliance-map cells.

Enforce bare discipline: zero prose paragraphs. Theorem statements only.

Target: ≤ 15 pages (estimated ~400-600 lines of markdown).

Write to `strategy/hodge/deliverables/hodge-clay-bare.md`.

### Step 5 — Synthesize C_bare

Walk the 10-section structure. Draw from:
- Paper 1 (QG5D hub, ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> foundation)
- Paper 61 (projections — the ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> derivation of filtrations)
- Paper 60 (e-circle geometry)
- Paper 26 (BSD, CM abelian-variety link)
- Paper 31 (Baum-Connes, Chern-character bridge)
- Paper 13 (RH, endomotive spectral data)
- Paper 35 (Schanuel, period relations)
- Programme 36-pins table if applicable (search `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md`)
- Cross-Clay x-ray cross-cuts (when hodge x-ray lands)

Enforce bare discipline. Zero prose.

Write to `strategy/hodge/deliverables/hodge-beyond-bare.md`.

### Step 6 — Verification pass

Critic examines B_bare + C_bare for:
- Any prose paragraph (FAIL if found)
- Any uncited claim (FAIL)
- Any SILENT Deligne requirement (FAIL)
- Any named wall without bypass-route disclosure (FAIL)
- Page count > 15 per document (WARN; target = 15)

Arbiter emits PUBLISH-READY verdict if all checks pass, NEEDS-REVISION otherwise.

### Step 7 — Commit memo

Write `commit-memo.md` summarizing:
- Compliance map results (verdict distribution per requirement)
- New named walls created (beyond W1-W3)
- New links constructed (if any)
- Cells remaining in each status
- B_bare + C_bare page counts
- Lock status (LOCKED / NOT-LOCKED with reason)
- Recommendation for next step (composition-backward? more compliance work? hodge x-ray run?)

---

## SUCCESS CRITERIA

- Compliance map 8×6 complete; every cell has verdict + citation + arbiter decision
- Zero SILENT cells in final state
- B_bare written, ≤ 15 pages, zero prose, every claim cited
- C_bare written, ≤ 15 pages, zero prose, every claim cited
- W1, W2, W3 explicitly disclosed with all required fields
- All programme papers referenced have §-level (or Link-level) precision
- Critic pass: PUBLISH-READY verdict

A run FAILS if:
- Any SILENT cell remains
- Any prose paragraph appears in B_bare or C_bare
- Any claim lacks citation
- Any of W1/W2/W3 lacks bypass-route disclosure

---

## INVOCATION

```
read your instructions from <ora-bundle-v8>/01-the-prompt.md

the chain mode extension is
<pca-extension>/07-proof-chain-adversarial.md

the strategic triad extension is
<pca-extension>/12-prf-chain-advr-strat-triad.md

the chessboard layer extension is
<pca-extension>/13-chessboard-layer.md

the parent brief is
<pca-extension>/30-ring-traversal-brief.md

the current run brief (HODGE MILLENNIUM DELTA) is
strategy/hodge/hodge-millenium-brief.md

the strategy document is
strategy/hodge/00-millenium-strategy.md

the hodge live proof chain is
solutions-with-prize/paper29-hodge/PROOF-CHAIN.md

the motivic BC support chain is
solutions/paper31-baum-connes/PROOF-CHAIN.md

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see 00-millenium-strategy.md §9 for Zenodo-first cascade.)

the run output directory is
strategy/hodge/pac-output/runs/run-NN/

outputs:
- Output A (internal) → strategy/hodge/pac-output/runs/run-NN/
- Output B_bare (Clay-shaped skeleton) → strategy/hodge/deliverables/hodge-clay-bare.md
- Output C_bare (Beyond-Clay skeleton) → strategy/hodge/deliverables/hodge-beyond-bare.md

DO NOT produce B_full or C_full this run. DEFERRED to composition-backward.

MODE: compliance-audit + bare-deliverable-synthesis.

Run plan:
1. Read inputs (§1-§6 above)
2. Build 8×6 compliance map (48 cells)
3. Address SILENT verdicts (no cell silent at end)
4. Synthesize B_bare (17 sections, ≤ 15 pages, zero prose)
5. Synthesize C_bare (10 sections, ≤ 15 pages, zero prose)
6. Verification pass (critic → arbiter PUBLISH-READY)
7. Commit memo with lock status + recommendation

Begin.
```

---

## INVOCATION STYLE B — Agent-tool spawning

Self-contained for claude-code sub-agent spawning. Parameters: `<RUN-NN>`.

```
You are the PAC operator running on the Hodge Millennium bundle. This is run <RUN-NN>. Produce a Clay-compliance-audited Hodge deliverable in BARE MODE ONLY. B_full and C_full are DEFERRED.

## GOAL

Three deliverables:
A. Internal artifacts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/pac-output/runs/<RUN-NN>/
B_bare. Clay-shaped X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/deliverables/hodge-clay-bare.md
C_bare. Beyond-Clay X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/deliverables/hodge-beyond-bare.md

## READ FIRST (in order)

1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/00-millenium-strategy.md (strategy doc)
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/hodge-millenium-brief.md (this brief)
3. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper29-hodge/PROOF-CHAIN.md (8-link live chain)
4. /Users/gsix/quantum-geometry-in-5d-latex/solutions/paper31-baum-connes/PROOF-CHAIN.md (motivic BC extension — Route A)
5. Deligne's "The Hodge Conjecture" §1-§6 (verbatim in strategy doc §1)

## READ AS NEEDED

- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/PROOF-CHAIN.md (QG5D hub; for group/~~5D derivation~~ M⁵ derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D derivation" → "M⁵ derivation" --> + scheme independence)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper61-projections-5d/sections/ (for ~~5D derivation~~ M⁵ derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D derivation" → "M⁵ derivation" --> bonus / Hodge filtration geometry)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper26-bsd/PROOF-CHAIN.md (for CM-abelian slice + BSD cross-Clay)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/PROOF-CHAIN.md (for RH cross-Clay endomotive connection)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions/paper35-schanuel/PROOF-CHAIN.md (for period-relation cross-cut)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md (for YM cross-Clay Chern-K connection)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md (for potential PvNP cross-cut)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper12-cbb-system/research/23-framework-predictions-master-table.md (pins table)
- /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/ (ORA patterns)
- /Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md (capacitor)

## WRITE (required files)

Primary deliverables:
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/deliverables/hodge-clay-bare.md
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/deliverables/hodge-beyond-bare.md

Run transcripts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/hodge/pac-output/runs/<RUN-NN>/:
- blackboard.md
- compliance-map.md (8-link × 6-requirement = 48-cell matrix)
- vertices/hodge/ (per-link artifacts)
- kills.md, critic-attacks.md, arbiter-decisions.md
- commit-memo.md

## HARD DISCIPLINE

1. **BARE MODE ONLY.** B_bare and C_bare contain ZERO prose paragraphs. Theorem statements + definitions + equations + figures + numbers + citations only. No "introduction," no "motivation," no "discussion," no prose proofs, no "we show that," no "note that." If a section attracts prose, REMOVE the section.

2. **Compliance map 8×6 mandatory.** Every cell verdict: PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation. Zero SILENT at end.

3. **Citations per claim.** Every theorem, number, equation cites programme paper + specific proof location (paperNN §X Theorem T.Y format, or Link N for the hodge chain).

4. **W1, W2, W3 explicit disclosure** in B_bare §10, §12, §13 and §15: NAMED WALL, bypass route (motivic BC extension / André motivated recovery / 2025 5-step algorithm), closure scope (BC-motivated vs all smooth projective), audit status.

5. **≤ 15 pages per bare document.** Target ~400-600 lines markdown.

6. **Page count is a quality proxy.** If you find yourself writing a full page on one theorem's prose, you've left bare mode.

7. **Not Kähler.** The scope requirement is projective non-singular over C. Zucker counterexample cites must appear; if any theorem statement generalizes to Kähler without justification, FAIL.

8. **Rational, not integral.** The Atiyah-Hirzebruch obstruction must appear explicitly in §7. Any theorem statement claiming integral Hodge conclusion is wrong; FAIL.

9. **B_full and C_full NOT produced this run.** DEFERRED to composition-backward (future run using parallel agents on 60-project reservoir).

## SUCCESS CRITERIA

- Compliance map complete, zero SILENT
- B_bare + C_bare written, bare discipline enforced
- Every claim cited
- W1, W2, W3 disclosed with all required fields
- Scope = projective non-singular over C (not Kähler) stated explicitly
- Rational (not integral) stated explicitly with AH obstruction
- Critic PUBLISH-READY verdict
- Commit memo records lock status

If blocked (ambiguous verdict, missing citation, etc.): log in blackboard, DO YOUR BEST, flag NEEDS-REVIEW, continue. Don't block on perfection. The next run iterates.

Begin by reading the 5 mandatory files in order. Then plan in blackboard. Then execute.
```

---

*End of brief. Bare-first, prose-deferred. B_full and C_full composed backward by parallel agents after bare locks. The cascade begins with Zenodo. The Clay 2-year clock starts at journal publication. W1-W3 (motivic Hodge filtration / motivic functoriality / route composition) work in parallel, non-blocking. Scope is projective not Kähler. Conclusion is rational not integral.*

*G Six and Claude Opus 4.6. April 14, 2026.*
