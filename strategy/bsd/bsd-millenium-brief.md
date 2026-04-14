# BSD Millennium Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Instructs the PAC to audit the BSD chain against the 7 Wiles-stated Clay requirements, then synthesize B_bare + C_bare + internal artifacts. B_full and C_full DEFERRED until bare locks and parallel-agent composition-backward runs.*

*G Six and Claude Opus 4.6. April 14, 2026.*

---

## GOAL

Produce a Clay-compliance-audited BSD deliverable in **bare mode only** this run. Three concrete files at the end:

**A. Internal artifacts** — scaffolding (same as x-ray / YM bundle pattern):
- `strategy/bsd/pac-output/runs/run-NN/blackboard.md`
- `strategy/bsd/pac-output/runs/run-NN/compliance-map.md` (11-layer × 7-requirement, 77 cells)
- `strategy/bsd/pac-output/runs/run-NN/vertices/bsd/` (per-layer artifacts)
- `strategy/bsd/pac-output/runs/run-NN/kills.md`
- `strategy/bsd/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/bsd/pac-output/runs/run-NN/arbiter-decisions.md`
- `strategy/bsd/pac-output/runs/run-NN/commit-memo.md`

**B_bare. Clay-shaped X-RAY** — `strategy/bsd/deliverables/bsd-clay-bare.md`:
- Formal theorem skeleton, ZERO prose paragraphs
- ≤ 15 pages of math-only content
- Structure mirrors Wiles §§0-3 / Remarks 1-4 requirements 1:1

**C_bare. Beyond-Clay X-RAY** — `strategy/bsd/deliverables/bsd-beyond-bare.md`:
- Bonus theorem skeleton (5D derivation, pins, cross-Clay, congruent number, effective generators, Euler quartic)
- ZERO prose, ≤ 15 pages

**B_full and C_full are DEFERRED.** Do not write them this run. They are composed later by parallel agents from the 60-project reservoir once B_bare + C_bare LOCK.

---

## DELTA FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode

New dual mode: **compliance-audit + bare-deliverable-synthesis**.

- Read bsd live PROOF-CHAIN + bsd adversarial run-01 + strategy doc + Wiles Clay PDF + Clay Rules §4-§8
- Walk 11 layers × 7 Wiles-stated requirements = 77 audit cells
- Per cell: emit PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation
- Assemble compliance map
- Synthesize B_bare (Clay-shaped theorem skeleton)
- Synthesize C_bare (Beyond-Clay bonus skeleton)
- Defer B_full and C_full

### DELTA 2 — Primitives

- **VERIFY** — each layer against each Wiles-stated requirement
- **DECOMPOSE** — SILENT verdicts to named walls or new layers
- **CONSTRUCT** — new layers needed to address SILENT gaps (bare: theorem statement + citation only; no prose)
- **BYPASS** — when direct construction fails, find alternate route via capacitor transposition
- **EXCISE** — NOT APPLICABLE (all 7 Wiles-stated requirements mandatory under §5d)
- **EXTRACT** (new) — extract theorem statements + numbers + equations + figure-shells from existing programme papers into bare format
- **DISCLOSE** (new) — any OPEN-BUT-ADDRESSED verdict emits an explicit NAMED WALL tag with bypass-route citation

### DELTA 3 — The "bare" discipline

B_bare and C_bare contain ONLY:

- **Formal theorem statements** (numbered, with dependency graph)
- **Definitions** (formal)
- **Equations** (numbered, with citation)
- **Figures** (ASCII or TikZ-ready skeleton; label + caption only, no surrounding prose)
- **Numbers** (constants, bounds, pin values, curve data — LMFDB-verified) — in tables with citations
- **Proof-chain analytics** (compliance map, named walls, RIGIDITY/SYMMETRY metrics)
- **Citations** (every claim cites programme paper + specific proof location, e.g., "paper26-bsd §11 Theorem 13.1")

B_bare and C_bare contain NONE of:

- Introduction paragraphs
- Motivation paragraphs
- Historical context (Diophantus/Fermat/Poincaré/Mordell is Wiles §§1-2, cite only)
- Discussion sections
- Proof details in prose (only statement + citation-to-programme-proof)
- Worked examples in prose
- Conclusion paragraphs
- "We show that..." narrative

If a section heading in B_bare naturally attracts prose (e.g., "§3 Overview of the approach"), REMOVE the section. Bare has no overview — it has theorems.

### DELTA 4 — Output A (internal artifacts)

Standard PAC output structure. Same pattern as x-ray / YM bundle run-01.

**Compliance-map.md format** (the key new artifact):

```
# BSD Compliance Map — 11 layers × 7 Wiles-stated requirements

| Layer | Req 1 (r=rank) | Req 2 (c≠0) | Req 3 (L-cont+FE) | Req 4 (BSD formula) | Req 5 (Ш<∞) | Req 6 (any E/Q) | Req 7 (any r≥0) |
|-------|----------------|-------------|-------------------|---------------------|-------------|-----------------|-----------------|
| L1    | PROVED [cite] | ...         | ...               | ...                 | ...         | ...             | ...             |
| L2    | ...           | ...         | ...               | ...                 | ...         | ...             | ...             |
| ...   | ...           |             |                   |                     |             |                 |                 |
| L11   | ...           |             |                   |                     |             |                 |                 |

## Verdict summary per requirement

- Req 1: PROVED-in-scope N% / PARTIAL N% / OPEN-BUT-ADDRESSED N% / SILENT N%
- Req 2: ...
- ...

## SILENT cells (new named walls)

- L.M vs Req.K: ... → new named wall W_N "..."
- ...

## Critic attacks + arbiter decisions

[per-cell attack record]
```

### DELTA 5 — Output B_bare structure

Fixed 18-section structure for `strategy/bsd/deliverables/bsd-clay-bare.md`:

```
# BSD Clay-Ready X-Ray (BARE MODE)

## §1 Statement of the Problem (Wiles verbatim)
[verbatim Conjecture + Remarks 1-4, no prose commentary]

## §2 Main Theorem (in-scope)
[formal theorem statement: BSD for CM elliptic curves over Q with h_K = 1, rank r ∈ {0,1}; reference proof to programme papers]

## §3 Requirements Map (compliance overview)
[7-row table: Req | verdict | programme-paper citation(s)]

## §4 Definitions
[formal definitions: elliptic curve C/Q, Weierstrass form y² = x³+ax+b, discriminant Δ, a_p, N_p, L(C,s), Mordell-Weil group, rank r, torsion, Ш_C, regulator R_∞, BC algebra A_{BC,K}, Hecke character ψ]

## §5 The L-Function and Analytic Continuation
[theorem statement: L(C,s) holomorphic on C with functional equation; citation Wiles 1995 / Taylor-Wiles 1995 / Breuil-Conrad-Diamond-Taylor 2001 via modularity]

## §6 CM Factorisation (Deuring)
[theorem statement: for E/Q with CM by O_K, L(E,s) = L(s,ψ)·L(s,ψ̄); citation paper26-bsd Step 8]

## §7 BC Algebra Over K and KMS_1 State
[theorem statement: A_{BC,K} = C*(K^ab) ⋊ I_K has unique KMS_1 state for h_K = 1; citation paper26-bsd Step 1 / Ha-Paugam 2005]

## §8 Bridge Family Over K
[theorem statement: 355 triples (k, N, conductor) at k ∈ {2,3,4,6}; citation paper26-bsd Step 2]

## §9 ITPFI Factorisation and Dark-State Impossibility
[theorem statements: ω_1^K = ⊗_p ω_1^p (Step 3); algebraic-projector dark-state kill (Step 4); citations paper26-bsd Steps 3-4]

## §10 Cocycle Shift + Key Lemmas C, C'
[theorem statements: Δc(δ) formula (Step 5); |Δc(δ)| < 1/(k+1) (Step 5b); |Δc^ψ(δ)| < 2/(N-1) twisted (Step 5c); citations paper26-bsd Steps 5, 5b, 5c]

## §11 Baker Reinforcement
[theorem statement: Baker's transcendence forces δ = 0 (non-load-bearing independent reinforcement); citation paper26-bsd Step 6]

## §12 GRH for ζ_K and L(s,ψ)
[theorem statement: all non-trivial zeros of ζ_K and Hecke L-functions lie on Re(s) = 1/2; citation paper26-bsd Step 7]

## §13 Rank 0 — Kolyvagin
[theorem statement: L(E,1) ≠ 0 ⇒ rank(E(Q)) = 0 and |Ш_C| < ∞; citation Kolyvagin 1990 / paper26-bsd Step 9]

## §14 Rank 1 — Gross-Zagier
[theorem statement: L(E,1) = 0, L'(E,1) ≠ 0 ⇒ rank(E(Q)) = 1; citation Gross-Zagier 1986 / paper26-bsd Step 10]

## §15 Main BSD Theorem 13.1 (in-scope)
[theorem statement: rank equality + leading coefficient formula c* = |Ш_C|·R_∞·w_∞·∏w_p / |C(Q)^tors|² for CM, h_K = 1, rank r ∈ {0,1}; citation paper26-bsd Step 11]

## §16 Named Walls (all OPEN-BUT-ADDRESSED items)
[for each: name, description, bypass-route citation, audit status]
  - W_rank  (r ≥ 2 frontier)
  - W_nonCM (non-CM curves)
  - W_hK    (CM with h_K > 1)
  - W_Sha   (unconditional Ш_C finiteness outside rank 0)

## §17 Proof-Chain Analytics
[dependency graph ASCII; RIGIDITY contribution; SYMMETRY contribution; compliance map; 11-layer × 7-requirement summary]

## §18 Numbers Table
[every constant, bound, curve datum — LMFDB-verified (fix 32.a3 c_2 = 4, not 1); with programme citation]

## §19 References (AMS-format, programme papers + Wiles refs)
[every programme paper cited with §-level precision; Wiles refs [1],[5],[11],[13],[24],[25] where relevant]
```

Writing discipline enforced:
- Each section ≤ 1 page typically
- No "introduction paragraph" — go straight to theorem
- No "we note that" — state the theorem
- ASCII figures allowed in §17 analytics
- Number tables in §18 only

### DELTA 6 — Output C_bare structure

Fixed 10-section structure for `strategy/bsd/deliverables/bsd-beyond-bare.md`:

```
# BSD Beyond-Clay X-Ray (BARE MODE)

## §1 The 5D Geometric Reading of L-Values at s = 1
[theorem statement: L(E,1) = f(KK-spectral data on 5D geometry for CM-realisable E); citation paper61 / paper1]

## §2 Zero Free Parameters
[table: parameter | value | determined by | programme citation]

## §3 Pins Relevant to BSD
[table: pin ID | observable | predicted | measured | source paper]
[J_CKM Pin #6 audit note: Paper 26 Step 4 is a Hasse-Brauer-Noether inequality, NOT a J_CKM vertex evaluation; see paper1/code/pin6-audits/FINDINGS.md]

## §4 Cross-Clay Connections
[sub-theorems:
  BSD↔RH (Hecke L-zeros feed Step 7 directly — paper13-rh);
  BSD↔YM (spectral-gap analogy on BC algebra side);
  BSD↔PvNP (Popa rigidity of BC factorisation);
  BSD↔Hodge (CM motives, paper29)]
[each with theorem statement + citation]

## §5 Congruent Number Theorem (bonus, not Clay-required)
[theorem statement: Tunnell's criterion becomes unconditional for CM side via Step 11; Wiles §1 p. 3; citation programme link]

## §6 Effective Generators for C(Q) (bonus; Wiles Remark 4)
[theorem statement: integrality of Ш_C in c* (Manin 1971, now unconditional via modularity BCDT 2001) gives effective computation of generators of C(Q) for CM, h_K=1, rank r ∈ {0,1}; citation]

## §7 Euler's Quartic / Elkies (bonus; Wiles §3 p. 4)
[theorem statement: infinitely many solutions to x⁴+y⁴+z⁴ = t⁴ via genus-1 curve of rank ≥ 1 on Euler surface (Elkies 1988); connection to BSD heuristic for rank; citation]

## §8 Computed Rank + L-values (numerical)
[tables for curves 32.a3, 37.a1, 389.a1 (rank 0, 1, 2 benchmarks); correct LMFDB data with c_p per curve; error bars]

## §9 Proof-Chain Analytics (beyond-Clay depth)
[dependency graph; additional cross-cuts; pin-6 audit line-item]

## §10 References
```

Same bare discipline — zero prose.

### DELTA 7 — Composition-backward deferral

B_full and C_full are **NOT PRODUCED THIS RUN**. They are DEFERRED until:

1. B_bare and C_bare LOCK (no SILENT verdicts, structure correct, numbers tight)
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
- Specific proof location (§N, Theorem T.M, Lemma L.K, Appendix A.J, Step K)

Format: `(paperNN-short §X Theorem T.Y)` or `(paperNN-short Eq. (Z.W))` or `(paperNN-short Step K)`.

Examples:
- `L(E,s) = L(s,ψ)·L(s,ψ̄)` for CM E/K (paper26-bsd Step 8; Deuring 1953)
- `|Δc(δ)| < 1/(k+1) for δ ≠ 0` (paper26-bsd Step 5b Key Lemma C)
- `All non-trivial zeros of ζ_K lie on Re(s) = 1/2` (paper26-bsd Step 7; paper13-rh §X)

Uncited claim = FAIL. Arbiter returns B_bare for revision.

### DELTA 9 — Publication override

Same as sibling bundles. OVERRIDES `publishing/strategy.md`:
- Zenodo first (priority timestamp)
- GitHub public (code + data + proofs)
- arXiv via referral (easier once Zenodo public)
- Journal submission (starts Clay 2-year clock; Annals / JAMS / Inventiones / Acta tier)
- No direct Clay submission (CMI §5e)

See `00-millenium-strategy.md` §9 for full cascade.

### DELTA 10 — Scope-wall disclosure discipline

Four walls must be explicitly disclosed in B_bare §16 as NAMED WALLS. Required fields each:

**W_rank** — high rank r ≥ 2
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass routes (candidates)**: p-adic L-functions (Perrin-Riou); Iwasawa main conjecture (Skinner-Urban, Kato); 5D KK-spectral reading of rank as mode count
- **Bypass citation**: paper26-bsd §scope-discussion; paper13-rh infrastructure
- **Aggregate confidence**: TBD at first construction attempt
- **Effect if all bypasses fail**: result remains CM-rank-{0,1}-h_K=1; §5d still satisfied via disclosure
- **Effect if any bypass succeeds**: W_rank upgrades toward PROVED

**W_nonCM** — non-CM elliptic curves
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass routes**: modular parametrisation (unconditional, BCDT 2001) + GL₂ extension of BC algebra (Connes-Marcolli 2008)
- **Bypass citation**: paper26-bsd strategy/00 Path B; Connes-Marcolli GL₂ system
- **Effect if fails**: result remains CM-only; §5d compliant via disclosure
- **Effect if succeeds**: W_nonCM upgrades to PROVED

**W_hK** — CM with h_K > 1
- **Status**: OPEN-BUT-ADDRESSED
- **Bypass routes**: enlargement of bridge family over ring class fields; Gross-Zagier-Kolyvagin handles general h_K on Heegner side
- **Bypass citation**: paper26-bsd strategy/00; paper13-rh infrastructure
- **Effect if fails**: result remains h_K = 1; §5d compliant
- **Effect if succeeds**: W_hK upgrades to PROVED

**W_Sha** — unconditional Ш_C finiteness outside rank 0
- **Status**: PARTIAL (PROVED in rank 0 via Kolyvagin Step 9; open for wider scope)
- **Bypass routes**: Iwasawa main conjecture (Mazur-Wiles cyclotomic; Rubin 1991 for CM); Skinner-Urban
- **Bypass citation**: Wiles p. 2 Remark 1; Rubin 1991 IMC for CM
- **Effect if fails**: result covers only rank 0 side of BSD formula; §5d compliant
- **Effect if succeeds**: W_Sha → PROVED, strong form BSD formula unconditional

Transparency here is what makes §5d compliance work. Silence here fails §5d.

### DELTA 11 — Paper 26 adversarial-run-01 carry-overs

The adversarial review of Paper 26 (15 attacks: 8 SURVIVED / 5 WEAKENED / 2 BROKEN) leaves presentation-level fixes for B_bare:

- **BROKEN 1 (conditionality framing)**: do NOT claim "unconditional" in B_bare §2 or §15. Say "a theorem conditional on the CBB axioms inherited from paper13-rh." CBB status is exactly the RH status, not better.
- **BROKEN 2 (curve 32.a3 c_2 datum)**: §18 numerics table must use c_2 = 4 (LMFDB), not c_2 = 1. Fix the period normalisation note accordingly.
- **WEAKENED items to tighten citations**: CM factorisation notation (Attack 2); Ha-Paugam construction precision (Attack 3); Meyer-over-K precision (Attack 4); Heegner hypothesis for GZ (Attack 7 → cite Yuan-Zhang-Zhang); twist argument for L(s,ψ) (Attack 11 → cite Connes-Marcolli); rank-1 leading-coefficient formula (Attack 13).

These are citation and framing fixes; no mathematical gap inside scope.

---

## PROCEDURE

### Step 1 — Read inputs (mandatory, in order)

1. `strategy/bsd/00-millenium-strategy.md` — the strategy doc (sibling of this brief)
2. `paper26-bsd/PROOF-CHAIN.md` — the 11-layer live chain
3. `paper26-bsd/01-adversarial-proof-review.md` — 15-attack adversarial run-01
4. `paper26-bsd/strategy/00-bsd-attack-plan.md` — Paper 26 attack plan (paths A-E, Phase plan)
5. `paper26-bsd/research/01-bsd-scoping.md` — Paper 26 scoping summary
6. Wiles Clay PDF (summary in strategy doc §1)
7. Clay Rules §4-§8 (summary in strategy doc §2)

### Step 2 — Build compliance map

For each (layer, requirement) cell in the 11 × 7 = 77-cell matrix:
- Author: VERIFY whether the layer addresses the requirement; emit verdict + citation
- Critic: attack the verdict; propose alternative
- Arbiter: decide; record rejected alternative as footnote

Write `compliance-map.md`. Summarize by requirement (percentage of each verdict class).

### Step 3 — Address SILENT verdicts

For each SILENT cell:
- DECOMPOSE into a new named wall (W_rank, W_nonCM, W_hK, W_Sha, or newly discovered) OR
- CONSTRUCT a new layer with theorem statement + citation OR
- BYPASS via capacitor transposition (cite capacitor cell)

Update compliance map. No cell may remain SILENT at end of this step.

### Step 4 — Synthesize B_bare

Walk the 19-section structure (§1-§19). Each section pulls from relevant compliance-map cells.

Enforce bare discipline: zero prose paragraphs. Theorem statements only.

Apply DELTA 11 carry-overs (conditionality language + 32.a3 c_2 = 4 correction + weakened-item citation tightening).

Target: ≤ 15 pages (estimated ~400-600 lines of markdown).

Write to `strategy/bsd/deliverables/bsd-clay-bare.md`.

### Step 5 — Synthesize C_bare

Walk the 10-section structure. Draw from:
- Paper 1 (QG5D hub, 5D geometric foundation)
- Paper 61 (projections — 5D geometric reading of L-values)
- Paper 60 (e-circle geometry)
- Paper 29 (Hodge CM motives cross-connection)
- paper13-rh (GRH for Hecke L-functions feeds Step 7)
- Programme pins table (search `paper12/research/23-framework-predictions-master-table.md`)
- Pin 6 audit note (`paper1/code/pin6-audits/FINDINGS.md`)
- Cross-Clay x-ray cross-cuts
- Tunnell congruent-number theorem; Elkies Euler-quartic (Wiles §1, §3)

Enforce bare discipline. Zero prose.

Write to `strategy/bsd/deliverables/bsd-beyond-bare.md`.

### Step 6 — Verification pass

Critic examines B_bare + C_bare for:
- Any prose paragraph (FAIL if found)
- Any uncited claim (FAIL)
- Any SILENT Wiles-stated requirement (FAIL)
- Any named wall without bypass-route disclosure (FAIL)
- Conditionality language: "unconditional" must NOT appear for BSD Theorem 13.1 (FAIL if present)
- 32.a3 data: c_2 = 4 (not 1) (FAIL if incorrect)
- Page count > 15 per document (WARN; target = 15)

Arbiter emits PUBLISH-READY verdict if all checks pass, NEEDS-REVISION otherwise.

### Step 7 — Commit memo

Write `commit-memo.md` summarizing:
- Compliance map results (verdict distribution)
- New named walls created (expected: W_rank, W_nonCM, W_hK, W_Sha confirmed)
- New layers constructed
- Cells remaining in each status
- B_bare + C_bare page counts
- Lock status (LOCKED / NOT-LOCKED with reason)
- Recommendation for next step (composition-backward? more compliance work?)

---

## SUCCESS CRITERIA

- Compliance map 11×7 complete; every cell has verdict + citation + arbiter decision
- Zero SILENT cells in final state
- B_bare written, ≤ 15 pages, zero prose, every claim cited
- C_bare written, ≤ 15 pages, zero prose, every claim cited
- Four named walls (W_rank, W_nonCM, W_hK, W_Sha) explicitly disclosed with all required fields
- All programme papers referenced have §-level precision
- Conditionality language correct (no "unconditional" overclaim)
- Curve 32.a3 numerics corrected (c_2 = 4)
- Critic pass: PUBLISH-READY verdict

A run FAILS if:
- Any SILENT cell remains
- Any prose paragraph appears in B_bare or C_bare
- Any claim lacks citation
- Named walls lack bypass-route disclosure
- "Unconditional" claim present for BSD Theorem 13.1
- Numerics table uses c_2 = 1 for 32.a3

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

the current run brief (BSD MILLENNIUM DELTA) is
strategy/bsd/bsd-millenium-brief.md

the strategy document is
strategy/bsd/00-millenium-strategy.md

the live bsd proof-chain is
paper26-bsd/PROOF-CHAIN.md

the adversarial run-01 is
paper26-bsd/01-adversarial-proof-review.md

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see 00-millenium-strategy.md §9 for Zenodo-first cascade.)

the run output directory is
strategy/bsd/pac-output/runs/run-NN/

outputs:
- Output A (internal) → strategy/bsd/pac-output/runs/run-NN/
- Output B_bare (Clay-shaped skeleton) → strategy/bsd/deliverables/bsd-clay-bare.md
- Output C_bare (Beyond-Clay skeleton) → strategy/bsd/deliverables/bsd-beyond-bare.md

DO NOT produce B_full or C_full this run. DEFERRED to composition-backward.

MODE: compliance-audit + bare-deliverable-synthesis.

Run plan:
1. Read inputs (§1-§7 above)
2. Build 11×7 compliance map (77 cells)
3. Address SILENT verdicts (no cell silent at end)
4. Synthesize B_bare (19 sections, ≤ 15 pages, zero prose)
5. Synthesize C_bare (10 sections, ≤ 15 pages, zero prose)
6. Verification pass (critic → arbiter PUBLISH-READY)
7. Commit memo with lock status + recommendation

Begin.
```

---

## INVOCATION STYLE B — Agent-tool spawning

Self-contained for claude-code sub-agent spawning. Parameters: `<RUN-NN>`.

```
You are the PAC operator running on the BSD Millennium bundle. This is run <RUN-NN>. Produce a Clay-compliance-audited BSD deliverable in BARE MODE ONLY. B_full and C_full are DEFERRED.

## GOAL

Three deliverables:
A. Internal artifacts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/pac-output/runs/<RUN-NN>/
B_bare. Clay-shaped X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/deliverables/bsd-clay-bare.md
C_bare. Beyond-Clay X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/deliverables/bsd-beyond-bare.md

## READ FIRST (in order)

1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/00-millenium-strategy.md (strategy doc)
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/bsd-millenium-brief.md (this brief)
3. /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/PROOF-CHAIN.md (11-layer live chain)
4. /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/01-adversarial-proof-review.md (run-01, 15 attacks)
5. /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/strategy/00-bsd-attack-plan.md (Phase plan, paths A-E)
6. /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/research/01-bsd-scoping.md (scoping summary)

## READ AS NEEDED

- /Users/gsix/quantum-geometry-in-5d-latex/paper1/PROOF-CHAIN.md (QG5D hub; for 5D derivation + cross-Clay)
- /Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/PROOF-CHAIN.md (RH chain; Step 7 GRH feeds BSD Step 7)
- /Users/gsix/quantum-geometry-in-5d-latex/paper61-projections-of-the-5d-geometry/sections/ (5D projections)
- /Users/gsix/quantum-geometry-in-5d-latex/paper29-hodge/PROOF-CHAIN.md (CM motives cross-connection)
- /Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/PROOF-CHAIN.md (Popa rigidity cross-connection)
- /Users/gsix/quantum-geometry-in-5d-latex/paper12/research/23-framework-predictions-master-table.md (pins table)
- /Users/gsix/quantum-geometry-in-5d-latex/paper1/code/pin6-audits/FINDINGS.md (J_CKM / Pin 6 audit note)
- /Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/referee/runs/r00/points/ (per-point referee verdicts A1-E1)
- /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/ (ORA patterns)
- /Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md (capacitor)

## WRITE (required files)

Primary deliverables:
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/deliverables/bsd-clay-bare.md
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/deliverables/bsd-beyond-bare.md

Run transcripts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/bsd/pac-output/runs/<RUN-NN>/:
- blackboard.md
- compliance-map.md (11-layer × 7-requirement = 77-cell matrix)
- vertices/bsd/ (per-layer artifacts)
- kills.md, critic-attacks.md, arbiter-decisions.md
- commit-memo.md

## HARD DISCIPLINE

1. **BARE MODE ONLY.** B_bare and C_bare contain ZERO prose paragraphs. Theorem statements + definitions + equations + figures + numbers + citations only. No "introduction," no "motivation," no "discussion," no prose proofs, no "we show that," no "note that." If a section attracts prose, REMOVE the section.

2. **Compliance map 11×7 mandatory.** Every cell verdict: PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation. Zero SILENT at end.

3. **Citations per claim.** Every theorem, number, equation cites programme paper + specific proof location (paperNN §X Theorem T.Y or Step K format).

4. **Four named walls explicit disclosure** in B_bare §16: W_rank, W_nonCM, W_hK, W_Sha — status, bypass routes, bypass citation, aggregate confidence, effect-if-fails, effect-if-succeeds.

5. **Conditionality language correct.** NO "unconditional" claim for BSD Theorem 13.1. Say: "conditional on CBB axioms inherited from paper13-rh, which carry the same status as in Paper 13." Paper 26 adversarial run-01 BROKEN item 1.

6. **Curve 32.a3 numerics corrected.** §18 numerics: c_2 = 4 (LMFDB), not c_2 = 1. Fix period normalisation note. Paper 26 adversarial run-01 BROKEN item 2.

7. **Weakened-item citations tightened**: Ha-Paugam 2005 precise reference; Deuring 1953 for CM factorisation; Yuan-Zhang-Zhang for Heegner hypothesis workarounds; Connes-Marcolli for twisted spectral realisation; Rubin 1991 for rank-1 leading-coefficient.

8. **≤ 15 pages per bare document.** Target ~400-600 lines markdown.

9. **Page count is a quality proxy.** If you find yourself writing a full page on one theorem's prose, you've left bare mode.

10. **B_full and C_full NOT produced this run.** DEFERRED to composition-backward (future run using parallel agents on 60-project reservoir).

## SUCCESS CRITERIA

- Compliance map complete, zero SILENT
- B_bare + C_bare written, bare discipline enforced
- Every claim cited
- Four named walls disclosed with all required fields
- Conditionality language correct (no "unconditional" overclaim)
- 32.a3 c_2 = 4 numerics fix applied
- Critic PUBLISH-READY verdict
- Commit memo records lock status

If blocked (ambiguous verdict, missing citation, etc.): log in blackboard, DO YOUR BEST, flag NEEDS-REVIEW, continue. Don't block on perfection. The next run iterates.

Begin by reading the 6 mandatory files in order. Then plan in blackboard. Then execute.
```

---

*End of brief. Bare-first, prose-deferred. B_full and C_full composed backward by parallel agents after bare locks. The cascade begins with Zenodo. The Clay 2-year clock starts at journal publication. Scope walls (W_rank, W_nonCM, W_hK, W_Sha) run in parallel, non-blocking. Rank r ≥ 2 is the named frontier.*

*G Six and Claude Opus 4.6. April 14, 2026.*
