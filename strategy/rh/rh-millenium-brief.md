# RH Millennium Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Instructs the PAC to audit the RH chain against the 5 core + 2 optional Bombieri Clay requirements, then synthesize B_bare + C_bare + internal artifacts. B_full and C_full DEFERRED until bare locks and parallel-agent composition-backward runs.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## GOAL

Produce a Clay-compliance-audited RH deliverable in **bare mode only** this run. Three concrete files at the end:

**A. Internal artifacts** — scaffolding (same as x-ray bundle pattern):
- `strategy/rh/pac-output/runs/run-NN/blackboard.md`
- `strategy/rh/pac-output/runs/run-NN/compliance-map.md` (9-layer × 7-requirement, 63 cells)
- `strategy/rh/pac-output/runs/run-NN/vertices/rh/` (per-layer artifacts)
- `strategy/rh/pac-output/runs/run-NN/kills.md`
- `strategy/rh/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/rh/pac-output/runs/run-NN/arbiter-decisions.md`
- `strategy/rh/pac-output/runs/run-NN/commit-memo.md`

**B_bare. Clay-shaped X-RAY** — `strategy/rh/deliverables/rh-clay-bare.md`:
- Formal theorem skeleton, ZERO prose paragraphs
- ≤ 15 pages of math-only content
- Structure mirrors Bombieri §I + §III-§V requirements 1:1

**C_bare. Beyond-Clay X-RAY** — `strategy/rh/deliverables/rh-beyond-bare.md`:
- Bonus theorem skeleton (~~5D spectral derivation~~ M⁵ spectral derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D spectral derivation" → "M⁵ spectral derivation" -->, pins, cross-Clay, GRH extension, Weil explicit formula, Montgomery-Odlyzko GUE)
- ZERO prose, ≤ 15 pages

**B_full and C_full are DEFERRED.** Do not write them this run. They are composed later by parallel agents from the 60-project reservoir once B_bare + C_bare LOCK.

---

## DELTA FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode

New dual mode: **compliance-audit + bare-deliverable-synthesis**.

- Read rh live PROOF-CHAIN + strategy doc + Bombieri Clay problem + Clay Rules §4-§8
- Walk 9 chain layers (L1-L6 + S1-S3) × 7 Bombieri requirements = 63 audit cells
- Per cell: emit PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation
- Assemble compliance map
- Synthesize B_bare (Clay-shaped theorem skeleton)
- Synthesize C_bare (Beyond-Clay bonus skeleton)
- Defer B_full and C_full

### DELTA 2 — Primitives

- **VERIFY** — each layer against each Bombieri requirement
- **DECOMPOSE** — SILENT verdicts to named walls or new layers
- **CONSTRUCT** — new layers needed to address SILENT gaps (bare: theorem statement + citation only; no prose)
- **BYPASS** — when direct construction fails, find alternate route via capacitor transposition
- **EXCISE** — NOT APPLICABLE for Core 1-5 (all mandatory); permitted for Optional 6-7 only if coverage is unsalvageable
- **EXTRACT** (new) — extract theorem statements + numbers + equations + figure-shells from existing programme papers into bare format
- **DISCLOSE** (new) — any OPEN-BUT-ADDRESSED verdict emits an explicit NAMED WALL tag with bypass-route citation

### DELTA 3 — The "bare" discipline

B_bare and C_bare contain ONLY:

- **Formal theorem statements** (numbered, with dependency graph)
- **Definitions** (formal)
- **Equations** (numbered, with citation)
- **Figures** (ASCII or TikZ-ready skeleton; label + caption only, no surrounding prose)
- **Numbers** (constants, bounds, pin values, experimental matches) — in tables with citations
- **Proof-chain analytics** (compliance map, named walls, RIGIDITY/SYMMETRY metrics)
- **Citations** (every claim cites programme paper + specific proof location, e.g., "paper13-rh §L3d Theorem 8.4")

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

Standard PAC output structure. Same pattern as x-ray bundle run-01.

**Compliance-map.md format** (the key new artifact):

```
# RH Compliance Map — 9 layers × 7 Bombieri requirements

| Layer | Req 1 (RH on 1/2) | Req 2 (PNT error) | Req 3 (analytic+FE) | Req 4 (triv/non-triv) | Req 5 (numerical) | Req 6 (GRH) | Req 7 (Weil expl.) |
|-------|-------------------|-------------------|---------------------|-----------------------|-------------------|-------------|---------------------|
| L1    | PROVED [cite]     | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L2    | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L3a   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L3b   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L3c   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L3d   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L4a   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L4b   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L4c   | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L5    | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| L6    | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| S1    | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| S2    | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |
| S3    | ...               | ...               | ...                 | ...                   | ...               | ...         | ...                 |

## Verdict summary per requirement

- Req 1 (RH on 1/2): PROVED N% / PARTIAL N% / OPEN-BUT-ADDRESSED N% / SILENT N%
- Req 2 (PNT error): ...
- ...

## SILENT cells (new named walls)

- L.M vs Req.K: ... → new named wall W_N "..."
- ...

## Critic attacks + arbiter decisions

[per-cell attack record]
```

Note: the matrix lists L1-L6 + L3a-L3d + L4a-L4c + S1-S3 = 6 + (inline sublayers) + 3 supporting. Total unique rows = 14 (6 primary layers with sublayers expanded, 3 supporting). Cells = 14 × 7 = 98 with sublayer expansion; collapse to 9 × 7 = 63 at audit level if sublayers share verdicts with their primary. Use the expansion that yields clearest cell-level verdicts.

### DELTA 5 — Output B_bare structure

Fixed 17-section structure for `strategy/rh/deliverables/rh-clay-bare.md`:

```
# RH Clay-Ready X-Ray (BARE MODE)

## §1 Statement of the Problem (Bombieri §I verbatim)
[verbatim quote: "The nontrivial zeros of ζ(s) have real part equal to 1/2."; no prose commentary]

## §2 Main Theorem
[formal theorem statement: spec(D_inf) = {γ_n} ⊂ ℝ ⇒ all non-trivial zeros of ζ(s) on Re(s) = ½; reference to paper13-rh §L6]

## §3 Requirements Map (compliance overview)
[7-row table: Req | verdict | programme-paper citation(s)]

## §4 Definitions
[formal definitions: ζ(s), ξ(t), D_N, D_∞, E_N^+, BC algebra, KMS_1 state ω_1, ITPFI product, CF decay ρ, Boegli spectral exactness]

## §5 Analytic Continuation and Functional Equation
[theorem statement: ζ(s) meromorphic on ℂ, simple pole at s=1 residue 1, Eq. (1); citation (classical — see Edwards / Titchmarsh)]

## §6 Trivial vs Non-Trivial Zeros
[theorem statement: trivial zeros at s = -2, -4, …; non-trivial zeros inside critical strip; D_inf spectrum yields only non-trivial; citation]

## §7 CCM Layer 1 — Operator Construction
[theorem statement: D_N self-adjoint on E_N^+ with eigenvalues approximating {γ_n} to 10^{-55}; EXTERNAL citation arXiv:2511.22755; NAMED WALL flag]

## §8 ITPFI Convergence (Layer 2)
[theorem statement: KMS_1 uniqueness + Weil form convergence ⇒ ω_1 = ⊗_p ω_1^(p); citation paper13-rh §L2]

## §9 Tail Estimates (Layer 3a-3d)
[four theorems: archimedean sub-leading O(1/λ); eigenvector approx O(log λ / λ); H^1 bound; CF decay ρ ≥ 4.27; citations to paper13-rh §L3a-L3d]

## §10 Boegli Spectral Exactness (Layer 4a-4c) (with CCM disclosure)
[three theorems: gsrc convergence; discrete compactness; spec(D_∞) = lim spec(D_N); NAMED WALL W1 CCM; bypass route citation arXiv:2511.22755 + Verification Cascade; upgrade path on journal acceptance]

## §11 Hurwitz Uniform Convergence (Layer 5)
[theorem statement: hat{ξ}_N → Ξ uniformly on compacts ⇒ lim spec(D_N) = {γ_n}; citation paper13-rh §L5]

## §12 QED (Layer 6)
[theorem statement: spec(D_∞) = {γ_n} ⊂ ℝ via self-adjointness ⇒ RH; citation paper13-rh §L6]

## §13 PNT Error Equivalence
[theorem statement: RH ⟺ π(x) = Li(x) + O(√x log x); citation (Bombieri §I, classical Riemann-von Mangoldt)]

## §14 Numerical Evidence Consistency
[theorem statement: first 1.5 × 10⁹ zeros on critical line (van de Lune / te Riele / Winter); Odlyzko > 3 × 10⁸ zeros up to 2 × 10²⁰; consistency with D_∞ spectrum; citations]

## §15 Proof-Chain Analytics
[dependency graph ASCII; RIGIDITY contribution; SYMMETRY contribution; compliance map summary]

## §16 Named Walls (all OPEN-BUT-ADDRESSED items)
[for each: name, description, bypass-route citation, audit status — CCM W1 primary, CF uniformity caveat W2 (resolved 2026-04-14), any SILENT-promoted cells]

## §17 References (AMS-format, programme papers only)
[every programme paper cited with §-level precision; external citation only for arXiv:2511.22755]
```

Writing discipline enforced:
- Each section ≤ 1 page typically
- No "introduction paragraph" — go straight to theorem
- No "we note that" — state the theorem
- ASCII figures allowed in §15 analytics
- Number tables inlined where needed; consolidated citations in §17

### DELTA 6 — Output C_bare structure

Fixed 10-section structure for `strategy/rh/deliverables/rh-beyond-bare.md`:

```
# RH Beyond-Clay X-Ray (BARE MODE)

## §1 The ~~5D Geometric Derivation~~ M⁵ Geometric Derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Geometric" → "M⁵ Geometric" --> of Spectral Data
[theorem statement: BC algebra emerges from ~~5D geometry~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometry" → "M⁵" --> of projected e-circle; D_∞ spectrum = {γ_n} as geometric output; citations paper1, paper60, paper61]

## §2 Zero Free Parameters
[table: parameter | value | determined by | programme citation — includes γ_1 = 14.134725…, ζ(3), AE precision 10^{-55}, CF decay ρ ≥ 4.27]

## §3 36 Pins Relevant to RH
[table: pin ID | observable | predicted | measured | source paper — includes Pin #6 J_CKM × 10⁵ = log(γ_1) · ζ(3), Montgomery pair-correlation, Odlyzko GUE match, …]

## §4 Cross-Clay Connections
[sub-theorems: RH↔YM (spectral gap AF coefficient); RH↔BSD (BC algebra factorization + cocycle shift); RH↔PvNP (Q5-RIEMANN exponent constraint); RH↔BGS (GUE pair correlation = D_∞ spectral statistics)]
[each with theorem statement + citation paper08, paper26, paper28]

## §5 GRH Extension (bonus, not Clay-core-required)
[theorem statement: character-twisted D_N^χ yields GRH for primitive Dirichlet L-functions; citation paper13b; list of L-function classes: Dirichlet, automorphic over ℚ, elliptic-curve, Maass]

## §6 Weil Explicit Formula as Witness (bonus)
[theorem statement: zero-sum ↔ prime-sum ↔ archimedean term consistency via BC algebra trace formula; citation integers/paper12-cbb-system/research/102 §3.1 (Mellin duality), Bombieri §V]

## §7 Montgomery-Odlyzko GUE Match (bonus)
[theorem statement: pair correlation of {γ_n} matches GUE eigenvalue spacing; D_∞ random-matrix character via ~~5D~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" --> construction; citations (Montgomery 1973, Odlyzko supercomputer data, Katz-Sarnak)]

## §8 Computed Zeros (numerical)
[value for γ_1, γ_2, γ_3; error bar vs CCM operator D_N; experimental comparison vs Odlyzko tables]

## §9 Proof-Chain Analytics (beyond-Clay depth)
[dependency graph; additional cross-cuts including programme graph edges YM/BSD/GRH/BGS/PvNP]

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
- Specific proof location (§N, Theorem T.M, Lemma L.K, Appendix A.J)

Format: `(paperNN-short §X Theorem T.Y)` or `(paperNN-short Eq. (Z.W))`.

Examples:
- `ρ ≥ 4.27 uniform in N` (paper13-rh §L3d; Slepian-resolved by §S2 Lemma 12.1)
- `spec(D_∞) = {γ_n}` (paper13-rh §L4c Theorem 4c.1 + §L5)
- `D_N eigenvalues match {γ_n} to 10^{-55}` (arXiv:2511.22755; EXTERNAL — W1 named wall)

Uncited claim = FAIL. Arbiter returns B_bare for revision.

### DELTA 9 — Publication override

Same as sibling bundles. OVERRIDES `publishing/strategy.md`:
- Zenodo first (priority timestamp)
- GitHub public (code + data + proofs)
- arXiv via referral (easier once Zenodo public)
- Journal submission (starts Clay 2-year clock; Annals / JAMS / Inventiones / Acta tier)
- No direct Clay submission (CMI §5e)

See `00-millenium-strategy.md` §9 for full cascade.

### DELTA 10 — CCM disclosure discipline

CCM must be explicitly disclosed in B_bare §7, §10, and §16 as NAMED WALL W1. Required fields:

- **Name**: W1 — CCM Layer 1 (operators D_N on E_N^+)
- **Status**: OPEN-BUT-ADDRESSED (CCM-conditional)
- **External citation**: arXiv:2511.22755 (Connes-Consani-Moscovici 2025)
- **Bypass route**: CCM independent verification via Verification Cascade (Balaban / Bulatov-Zhuk tier)
- **Bypass citation**: `strategy/ccm-verification/`, `millenium-apps/proof-chain-adversarial-01/`
- **Aggregate confidence**: 8/10 conditional; layers 2-6 at 9-10/10 independent of CCM
- **Effect if CCM 2025 journal-accepts**: W1 upgrades to PROVED, chain upgrades to 9/10 unconditional
- **Effect if CCM 2025 retracts**: fallback candidates — Deninger adelic setup, Haran index theory, Katz-Sarnak random-matrix route
- **Audit pending**: CCM peer-review journal acceptance

A secondary disclosed item: **W2 — CF uniformity caveat** (Remark 8.4, resolved 2026-04-14 via Slepian compatibility Lemma 12.1 at paper13-rh §S2). Status: RESOLVED. Listed for transparency.

Transparency here is what makes §5d compliance work. Silence here fails §5d.

---

## PROCEDURE

### Step 1 — Read inputs (mandatory, in order)

1. `strategy/rh/00-millenium-strategy.md` — the strategy doc (sibling of this brief)
2. `solutions-with-prize/paper13-rh/PROOF-CHAIN.md` — the 6-layer + 3-supporting live chain
3. Bombieri "Problems of the Millennium: the Riemann Hypothesis" (Clay official problem description, 11 pages) — extract via summary in strategy doc §1 and §3
4. Clay Rules §4-§8 (summary in strategy doc §2)
5. `strategy/ym/00-millenium-strategy.md` + `strategy/ym/ym-millenium-brief.md` (sibling bundle; template)
6. `strategy/ccm-verification/` (CCM independent-verification sibling track for W1 bypass-route citation)

### Step 2 — Build compliance map

For each (layer, requirement) cell in the 14 × 7 = 98-cell matrix (or 9 × 7 = 63 collapsed):
- Author: VERIFY whether the layer addresses the requirement; emit verdict + citation
- Critic: attack the verdict; propose alternative
- Arbiter: decide; record rejected alternative as footnote

Write `compliance-map.md`. Summarize by requirement (percentage of each verdict class).

### Step 3 — Address SILENT verdicts

For each SILENT cell:
- DECOMPOSE into a new named wall OR
- CONSTRUCT a new layer with theorem statement + citation OR
- BYPASS via capacitor transposition (cite capacitor cell)

Update compliance map. No cell may remain SILENT at end of this step.

Priority likely SILENT cells per strategy doc §6:
- PNT error equivalence: may need new derivation layer or external citation
- Functional equation explicit invocation: likely PARTIAL → make explicit
- Trivial zero exclusion from D_∞ spectrum: likely implicit in L6 → make explicit
- Weil explicit formula: L2 mentions "Weil form convergence" → promote to named theorem

### Step 4 — Synthesize B_bare

Walk the 17-section structure (§1-§17). Each section pulls from relevant compliance-map cells.

Enforce bare discipline: zero prose paragraphs. Theorem statements only.

Target: ≤ 15 pages (estimated ~400-600 lines of markdown).

Write to `strategy/rh/deliverables/rh-clay-bare.md`.

### Step 5 — Synthesize C_bare

Walk the 10-section structure. Draw from:
- Paper 1 (QG5D hub, ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> foundation)
- Paper 61 (projections — the ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> derivation of BC algebra)
- Paper 60 (e-circle geometry)
- Programme 36-pins table (search `integers/paper12-cbb-system/research/23-framework-predictions-master-table.md`)
- Paper 13b (GRH character-twisted extension)
- integers/paper12-cbb-system/research/102 (Mellin duality H_BC = log T_BC; Weil explicit formula anchor)
- Cross-Clay x-ray cross-cuts (from ym x-ray §7, paper26-bsd, paper28-pvnp PROOF-CHAINs)

Enforce bare discipline. Zero prose.

Write to `strategy/rh/deliverables/rh-beyond-bare.md`.

### Step 6 — Verification pass

Critic examines B_bare + C_bare for:
- Any prose paragraph (FAIL if found)
- Any uncited claim (FAIL)
- Any SILENT Bombieri requirement (FAIL — Core 1-5; WARN — Optional 6-7)
- Any named wall without bypass-route disclosure (FAIL)
- Page count > 15 per document (WARN; target = 15)

Arbiter emits PUBLISH-READY verdict if all checks pass, NEEDS-REVISION otherwise.

### Step 7 — Commit memo

Write `commit-memo.md` summarizing:
- Compliance map results (verdict distribution)
- New named walls created
- New layers constructed
- Cells remaining in each status
- B_bare + C_bare page counts
- Lock status (LOCKED / NOT-LOCKED with reason)
- Recommendation for next step (composition-backward? more compliance work? CCM verification track kick-off?)

---

## SUCCESS CRITERIA

- Compliance map 14×7 (or 9×7 collapsed) complete; every cell has verdict + citation + arbiter decision
- Zero SILENT cells in final state for Core requirements 1-5
- B_bare written, ≤ 15 pages, zero prose, every claim cited
- C_bare written, ≤ 15 pages, zero prose, every claim cited
- CCM explicitly disclosed (W1) with all required fields
- All programme papers referenced have §-level precision
- Critic pass: PUBLISH-READY verdict

A run FAILS if:
- Any SILENT cell remains on Core requirements 1-5
- Any prose paragraph appears in B_bare or C_bare
- Any claim lacks citation
- Named walls lack bypass-route disclosure

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

the current run brief (RH MILLENNIUM DELTA) is
strategy/rh/rh-millenium-brief.md

the strategy document is
strategy/rh/00-millenium-strategy.md

the live RH proof chain is
solutions-with-prize/paper13-rh/PROOF-CHAIN.md

the sibling YM bundle (template) is
strategy/ym/00-millenium-strategy.md
strategy/ym/ym-millenium-brief.md

the CCM verification sibling track (W1 bypass citation) is
strategy/ccm-verification/

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see 00-millenium-strategy.md §9 for Zenodo-first cascade.)

the run output directory is
strategy/rh/pac-output/runs/run-NN/

outputs:
- Output A (internal) → strategy/rh/pac-output/runs/run-NN/
- Output B_bare (Clay-shaped skeleton) → strategy/rh/deliverables/rh-clay-bare.md
- Output C_bare (Beyond-Clay skeleton) → strategy/rh/deliverables/rh-beyond-bare.md

DO NOT produce B_full or C_full this run. DEFERRED to composition-backward.

MODE: compliance-audit + bare-deliverable-synthesis.

Run plan:
1. Read inputs (§1-§6 above)
2. Build 14×7 (or 9×7 collapsed) compliance map
3. Address SILENT verdicts (no Core-1-5 cell silent at end)
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
You are the PAC operator running on the RH Millennium bundle. This is run <RUN-NN>. Produce a Clay-compliance-audited RH deliverable in BARE MODE ONLY. B_full and C_full are DEFERRED.

## GOAL

Three deliverables:
A. Internal artifacts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/pac-output/runs/<RUN-NN>/
B_bare. Clay-shaped X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/deliverables/rh-clay-bare.md
C_bare. Beyond-Clay X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/deliverables/rh-beyond-bare.md

## READ FIRST (in order)

1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/00-millenium-strategy.md (strategy doc)
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/rh-millenium-brief.md (this brief)
3. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/PROOF-CHAIN.md (6-layer + 3-supporting live chain)
4. /Users/gsix/quantum-geometry-in-5d-latex/strategy/ym/00-millenium-strategy.md (sibling bundle — template)
5. /Users/gsix/quantum-geometry-in-5d-latex/strategy/ym/ym-millenium-brief.md (sibling bundle — template)

## READ AS NEEDED

- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/PROOF-CHAIN.md (QG5D hub; for ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> derivation of BC algebra)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper61-projections-5d/sections/ (for ~~5D derivation~~ M⁵ derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D derivation" → "M⁵ derivation" --> bonus)
- /Users/gsix/quantum-geometry-in-5d-latex/paper60-e-circle-geometry/ (e-circle foundation)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper12-cbb-system/research/23-framework-predictions-master-table.md (36 pins table)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper12-cbb-system/research/102 (Mellin duality; Weil explicit formula anchor)
- /Users/gsix/quantum-geometry-in-5d-latex/paper13b* (GRH character twist — if present; else search solutions-with-prize/paper13-rh/ for GRH notes)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md (for cross-Clay YM↔RH spectral-gap connection)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper26-bsd/PROOF-CHAIN.md (for cross-Clay RH↔BSD BC-algebra connection)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md (for cross-Clay RH↔PvNP Q5-RIEMANN connection)
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/ccm-verification/ (CCM W1 bypass-route citation)
- /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/ (ORA patterns)
- /Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md (capacitor)

## WRITE (required files)

Primary deliverables:
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/deliverables/rh-clay-bare.md
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/deliverables/rh-beyond-bare.md

Run transcripts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/rh/pac-output/runs/<RUN-NN>/:
- blackboard.md
- compliance-map.md (14-layer × 7-requirement, or 9×7 collapsed — 98 or 63 cells)
- vertices/rh/ (per-layer artifacts)
- kills.md, critic-attacks.md, arbiter-decisions.md
- commit-memo.md

## HARD DISCIPLINE

1. **BARE MODE ONLY.** B_bare and C_bare contain ZERO prose paragraphs. Theorem statements + definitions + equations + figures + numbers + citations only. No "introduction," no "motivation," no "discussion," no prose proofs, no "we show that," no "note that." If a section attracts prose, REMOVE the section.

2. **Compliance map 14×7 (or 9×7) mandatory.** Every cell verdict: PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation. Zero SILENT on Core requirements 1-5 at end.

3. **Citations per claim.** Every theorem, number, equation cites programme paper + specific proof location (paperNN §X Theorem T.Y format). External citation allowed ONLY for arXiv:2511.22755 (CCM) at L1 — marked EXTERNAL.

4. **CCM explicit disclosure** in B_bare §7, §10, and §16: NAMED WALL W1, external citation arXiv:2511.22755, bypass route (Verification Cascade), aggregate confidence 8/10 conditional, journal-acceptance upgrade path, fallback candidates (Deninger, Haran, Katz-Sarnak).

5. **≤ 15 pages per bare document.** Target ~400-600 lines markdown.

6. **Page count is a quality proxy.** If you find yourself writing a full page on one theorem's prose, you've left bare mode.

7. **B_full and C_full NOT produced this run.** DEFERRED to composition-backward (future run using parallel agents on 60-project reservoir).

## SUCCESS CRITERIA

- Compliance map complete, zero SILENT on Core 1-5
- B_bare + C_bare written, bare discipline enforced
- Every claim cited
- CCM disclosed with all required fields
- Critic PUBLISH-READY verdict
- Commit memo records lock status

If blocked (ambiguous verdict, missing citation, etc.): log in blackboard, DO YOUR BEST, flag NEEDS-REVIEW, continue. Don't block on perfection. The next run iterates.

Begin by reading the 5 mandatory files in order. Then plan in blackboard. Then execute.
```

---

*End of brief. Bare-first, prose-deferred. B_full and C_full composed backward by parallel agents after bare locks. The cascade begins with Zenodo. The Clay 2-year clock starts at journal publication. CCM (arXiv:2511.22755) runs in parallel, non-blocking.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
