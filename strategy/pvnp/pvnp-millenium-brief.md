# PvNP Millennium Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Instructs the PAC to audit the PvNP chain against the 6 Cook Clay requirements (P ≠ NP direction per §5b), then synthesize B_bare + C_bare + internal artifacts. B_full and C_full DEFERRED until bare locks and parallel-agent composition-backward runs.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## GOAL

Produce a Clay-compliance-audited PvNP deliverable in **bare mode only** this run. Three concrete files at the end:

**A. Internal artifacts** — scaffolding (same as x-ray bundle pattern):
- `strategy/pvnp/pac-output/runs/run-NN/blackboard.md`
- `strategy/pvnp/pac-output/runs/run-NN/compliance-map.md` (23-node × 6-requirement, 138 cells)
- `strategy/pvnp/pac-output/runs/run-NN/vertices/pvnp/` (per-node artifacts)
- `strategy/pvnp/pac-output/runs/run-NN/kills.md`
- `strategy/pvnp/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/pvnp/pac-output/runs/run-NN/arbiter-decisions.md`
- `strategy/pvnp/pac-output/runs/run-NN/commit-memo.md`

**B_bare. Clay-shaped X-RAY** — `strategy/pvnp/deliverables/pvnp-clay-bare.md`:
- Formal theorem skeleton, ZERO prose paragraphs
- ≤ 15 pages of math-only content
- Structure mirrors Cook §1-§3 requirements 1:1
- **TM-model translation layer** explicit (operator-algebraic → Cook-formal)

**C_bare. Beyond-Clay X-RAY** — `strategy/pvnp/deliverables/pvnp-beyond-bare.md`:
- Bonus theorem skeleton (trinity dictionary, Boolean BC system, order-counting, cross-Clay, SAT vs TAUT, GCT)
- ZERO prose, ≤ 15 pages

**B_full and C_full are DEFERRED.** Do not write them this run. They are composed later by parallel agents from the 60-project reservoir once B_bare + C_bare LOCK.

---

## DELTA FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode

New dual mode: **compliance-audit + bare-deliverable-synthesis**.

- Read pvnp live PROOF-CHAIN + pvnp preprint PROOF-CHAIN + strategy doc + Cook §1-§3 + Clay Rules §4-§8
- Walk 23 proof-chain nodes × 6 Cook requirements = 138 audit cells
- Per cell: emit PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation
- Assemble compliance map
- Synthesize B_bare (Clay-shaped theorem skeleton)
- Synthesize C_bare (Beyond-Clay bonus skeleton)
- Defer B_full and C_full

### DELTA 2 — Primitives

- **VERIFY** — each node against each Cook requirement
- **DECOMPOSE** — SILENT verdicts to named walls or new layers
- **CONSTRUCT** — new layers needed to address SILENT gaps (bare: theorem statement + citation only; no prose)
- **BYPASS** — when direct construction fails, find alternate route via capacitor transposition
- **EXCISE** — NOT APPLICABLE (all 6 Cook requirements mandatory for P ≠ NP direction)
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
- **Citations** (every claim cites programme paper + specific proof location, e.g., "paper28 §4.5 Theorem PNP.1")

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
# PvNP Compliance Map — 23 proof-chain nodes × 6 Cook requirements

| Node | Req 1 (TM model) | Req 2 (P/NP defs) | Req 3 (NP-complete target) | Req 4 (relativization) | Req 5 (natural proofs) | Req 6 (algebrization) |
|------|------------------|-------------------|----------------------------|------------------------|------------------------|------------------------|
| N1   | PROVED [cite]    | ...               | ...                        | ...                    | ...                    | ...                    |
| N2   | ...              | ...               | ...                        | ...                    | ...                    | ...                    |
| ...  | ...              |                   |                            |                        |                        |                        |
| N23  | ...              |                   |                            |                        |                        |                        |

## Verdict summary per requirement

- Req 1: PROVED N% / PARTIAL N% / OPEN-BUT-ADDRESSED N% / SILENT N%
- Req 2: ...
- ...

## SILENT cells (new named walls)

- N.M vs Req.K: ... → new named wall W_N "..."
- ...

## Critic attacks + arbiter decisions

[per-cell attack record]
```

### DELTA 5 — Output B_bare structure

Fixed 17-section structure for `strategy/pvnp/deliverables/pvnp-clay-bare.md`:

```
# PvNP Clay-Ready X-Ray (BARE MODE)

## §1 Statement of the Problem (Cook §1 verbatim)
[verbatim quote of "Problem Statement. Does P = NP?" plus formal TM-model setup; no prose commentary]

## §2 Main Theorem
[formal theorem statement: P ≠ NP; reference proof to programme papers]

## §3 Requirements Map (compliance overview)
[6-row table: Req | verdict | programme-paper citation(s)]

## §4 Definitions (Cook-formal)
[formal definitions: Σ, Σ*, L ⊆ Σ*, TM M, t_M(w), T_M(n), polynomial-time TM, P, checking relation R, NP, ≤_p many-one reduction, NP-complete, 3-SAT]

## §5 The Boolean BC System 𝒞_comp
[formal construction: 𝔹 Boolean function field; 𝒜_BC^Bool crossed product; σ_t^Bool modular flow; ω_1^Bool KMS state (KEY LEMMA); M_Bool = π_1(𝒜_BC^Bool)'' type III₁ factor; citation paper28 §3]

## §6 The Trinity Dictionary Functor Φ_comp
[theorem statement: functor from CBB quintuple to Boolean CBB quintuple preserves H²(S_n, U(1)); LEMMA 3.8.1-3.8.3 non-degeneracy + cocycle computation; citation paper28 §2, §3.8]

## §7 Bulatov-Zhuk CSP Dichotomy (external)
[theorem statement: forward (¬Taylor → NPC) + backward (P-time → Taylor); citation Bulatov 2017, Zhuk 2020]

## §8 Taylor gap = Spectral gap of M_Bool^Γ
[theorem statement; 6/6 Schaefer computational verification; citation paper28/code/ + preprint §5]

## §9 Part (i): Taylor → Non-full (Path B, UNCONDITIONAL)
[theorem statement + 10-step sub-chain: Clone Growth UA1 (exponential) + UA2 (linear); KEY LEMMA 3.4.3 (KMS₁ + type III₁); A2 membership; G4 tail = 0; pigeonhole on U(d); instance diversity (AND/OR, MAJORITY Berry-Esseen, XOR Lemma X); Marrakchi non-fullness criterion]
[citation preprint Steps 1-10]

## §10 Part (ii): Non-Taylor → Full (Route C, conditional on CP-1)
[theorem statement + 5-step sub-chain: Non-amenable G_L; trivial radical; essential freeness; strong ergodicity via Jones-Schmidt; fullness via Marrakchi 2018 Theorem B; CP-1 Laca-Raeburn dilation]
[NAMED WALL W2: KMS₁ uniqueness (downstream-insulated)]
[citation preprint Steps 11-15 + CP-1]

## §11 The Corollary: P = NP ⇒ ⊥ (with Link 5 backward disclosure)
[theorem statement + 8-step contradiction chain: assume P = NP; 3-SAT ∈ P; BZ backward → Taylor; Part (i) → non-full; but 3-SAT non-Taylor (BZ forward); Part (ii) → full; Houdayer-Marrakchi dichotomy; ⊥]
[explicit NAMED WALL W1: Link 5 backward (non-full → Taylor polymorphism)]
[bypass route citation: Route C via CP-1 (paper28 preprint Steps 11-15); 6 Critic repairs applied; aggregate 0.82]
[citation preprint Steps 16-23]

## §12 TM-Model Translation Layer
[theorem statement: the operator-algebraic non-fullness of M_Bool^{3-SAT} implies 3-SAT ∉ P in the Cook-formal TM sense]
[sub-steps: (a) fix multi-tape TM M; (b) M runs 3-SAT in T_M(n) ≤ n^k + k ⇒ induces polymorphism via BZ backward; (c) polymorphism is Taylor; (d) Part (i) gives non-full; (e) contradict Part (ii) fullness]
[citation Cook §1 Def; BZ backward; paper28 §4.6 Corollary]

## §13 Three Barriers Cleared (Cook §3)
[three theorem statements:
 §13.1 Non-relativization: proof depends on ω_1 (pole of ζ at s=1), oracle-independent (paper28 §6.1; preprint §V)
 §13.2 Non-naturalness: fullness not a large-set property; Schur multiplier discrete (paper28 §6.2; preprint §V)
 §13.3 Non-algebrization: cyclotomic Galois cohomology + Schur multiplier above polynomial extensions (paper28 §6.3; preprint §V)]

## §14 NP-complete target: 3-SAT
[theorem statement: 3-SAT is NP-complete (Cook 1971); chain closes over 3-SAT via Steps 17-19; extends to any NP-complete L via Proposition 1(b)]
[citation Cook §2; paper28 §4.6]

## §15 Proof-Chain Analytics
[dependency graph ASCII; RIGIDITY contribution; SYMMETRY contribution; compliance map; face-histogram (RESONANCE/SYMMETRY/DYNAMICS/AMPLITUDE/ARITHMETIC/CURVATURE)]

## §16 Named Walls (all OPEN-BUT-ADDRESSED items)
[W1: Link 5 backward — non-full → Taylor; bypass Route C via CP-1; confidence 0.82; 6 Critics verified; seven bypass routes A-G enumerated
 W2: KMS₁ uniqueness — existence proved via compactness; uniqueness conditional; downstream insulated (fullness is state-independent property of factor)
 W3: Spectral identification H_R^Bool ↔ {γ_n · π²/2} — conjecture; possibly equivalent to RH for Boolean BC; non-load-bearing for P ≠ NP]

## §17 Numbers Table
[every constant, bound, probability — with programme citation:
 - λ ≥ 2^{2/9} (clone growth lower bound, UA1)
 - 2k+2 (clone growth upper bound for non-Taylor, UA2)
 - p = 0.82 (Part (i) 0.85 × Part (ii) 0.90 aggregate)
 - 6/6 Schaefer classes verified
 - 30 instances Spearman ρ = 1.000 (G4 tail = 0)
 - C/√k (Berry-Esseen constant, MAJORITY instance diversity)
 - 19 killed approaches, 16 waves, 47 agents, 4 repairs, 0 open gaps (closure)]

## §18 References (AMS-format, programme + Cook)
[every programme paper cited with §-level precision; Cook §1-§3; BZ; BGS; RR; AW; Houdayer-Marrakchi; Jones-Schmidt; Connes; Feldman-Moore; Laca-Raeburn]
```

Writing discipline enforced:
- Each section ≤ 1 page typically
- No "introduction paragraph" — go straight to theorem
- No "we note that" — state the theorem
- ASCII figures allowed in §15 analytics
- Number tables in §17 only
- §12 TM-Model Translation Layer is load-bearing — do not omit

### DELTA 6 — Output C_bare structure

Fixed 10-section structure for `strategy/pvnp/deliverables/pvnp-beyond-bare.md`:

```
# PvNP Beyond-Clay X-Ray (BARE MODE)

## §1 The Trinity Dictionary (full table)
[table: physics column | BC arithmetic column | computational column, rows 1-N from paper28 §2.3; spin-stats ↔ R-Theorem S.11 ↔ R-Theorem PNP.1 is the headline row]
[citation paper15 §2.1 (additive ↔ multiplicative recap); paper28 §2.2-§2.3]

## §2 R-Theorem PNP.1 (trinity version)
[theorem statement: Under Φ_comp, R-Theorem S.11 transposes to Jones index [M_Bool^NP : M_Bool^P] > 1; obstruction = non-trivial element of H²(S_n, U(1)) = ℤ/2]
[three-step proof citation: trinity functor; satisfiability operator SAT_n fermionic; Schur multiplier rigidity]
[citation paper28 §4.4-§4.5]

## §3 R-Theorem PNP.2 (order-counting / PNT version)
[theorem statement: PNT γ_n ~ 2π n / log n forces [M_Bool^NP : M_Bool^P] > 1]
[second independent derivation of P ≠ NP via Paper 17 §5.4.5 order-counting + von Mangoldt]
[citation paper17 §5.3.4, §5.4.5; paper28 §5]

## §4 Cross-Clay Connections
[sub-theorems:
 §4.1 PvNP ↔ RH: Boolean BC entropy operator S_BC^Bool has spectrum {γ_n · π²/2} on H_R^Bool (conjectural Hilbert-Pólya); citation paper17 + paper13
 §4.2 PvNP ↔ YM: Popa cocycle superrigidity is a candidate Link 5 backward bypass (Route D in seven-bypass list); YM mass gap's spectral structure mirrors M_Bool spectrum; citation paper08 + paper28
 §4.3 PvNP ↔ BSD: channel correspondence via conditional expectation (Link 5 Route C); L-function channel capacity from Paper 26; citation paper26 + paper28
 §4.4 PvNP ↔ QG5D: trinity dictionary is the cube-shadow pattern repeated; H²(S_n, U(1)) is the hidden volume; citation paper1 + paper23]

## §5 SAT vs TAUT Discrimination (LEMMA 3.8.4)
[theorem statement: W_SAT and W_TAUT are distinct odd-sector operators related by De Morgan involution θ; PNP.1 establishes P ≠ NP and P ≠ coNP as single ℤ/2 fact; NOT NP ≠ coNP (would need ℤ/4 or larger)]
[citation paper28 §3.8.4-§3.8.5]

## §6 The Non-degeneracy Corollary (LEMMA 3.8.2-3.8.3)
[theorem statement: Φ_comp's induced map on H² is the identity (not just a group homomorphism); operational witness W_SAT ≠ 0; algebraic via category theory; cocycle computation via inflation H²(ℤ/2) → H²(S_n) + Clifford anti-commutation]
[citation paper28 §3.8.1-§3.8.3]

## §7 GCT Comparison
[table: Mulmuley-Sohoni orbit closure | trinity dictionary object; permanent vs determinant ↔ W_SAT vs W_TAUT; GCT obstruction (conjectural) vs Schur multiplier H²(S_n, U(1)) (recognized here)]
[citation Mulmuley-Sohoni 2001; Mulmuley 2012; paper28 §4.7]

## §8 Boolean BC System 𝒞_comp (definition supplement)
[formal construction of quintuple (H_R^Bool, R̂_Bool, ω_1^Bool, M_comp, {β_k^Bool}); functorial equivalence with CBB quintuple 𝒞; moduli M_comp = poly-time circuit configuration space]
[citation paper23 §4.1; paper28 §3.7]

## §9 Proof-Chain Analytics (beyond-Clay depth)
[dependency graph; additional cross-cuts; framework-predictions table rows relevant to PvNP (if any)]

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
- `[M_Bool^NP : M_Bool^P] > 1` (paper28-pvnp §4.4 Theorem PNP.1)
- `λ ≥ 2^{2/9}` (solutions-with-prize/paper28-pvnp/preprint §2 Theorem UA1; Step 2)
- `Bulatov-Zhuk forward (¬Taylor ⇒ NPC)` (Bulatov 2017 / Zhuk 2020; cited paper28 preprint Step 20)

Uncited claim = FAIL. Arbiter returns B_bare for revision.

### DELTA 9 — Publication override

Same as sibling bundles. OVERRIDES `publishing/strategy.md`:
- Zenodo first (priority timestamp)
- GitHub public (code + data + proofs)
- arXiv via referral (easier once Zenodo public)
- Journal submission (starts Clay 2-year clock; Annals / JAMS / Inventiones / Acta tier)
- No direct Clay submission (CMI §5e)

See `00-millenium-strategy.md` §9 for full cascade.

### DELTA 10 — W1 (Link 5 backward) disclosure discipline

W1 must be explicitly disclosed in B_bare §11 and §16 as NAMED WALL. Required fields:

- **Name**: W1 (Link 5 backward / non-full → Taylor polymorphism)
- **Status**: OPEN-BUT-ADDRESSED
- **Forward direction**: UNCONDITIONAL (Path B, Steps 1-10, 6/6 Schaefer computationally verified)
- **Backward bypass route**: Route C via CP-1 (Laca-Raeburn dilation → Feldman-Moore groupoid → Jones-Schmidt strong ergodicity → Marrakchi 2018 fullness)
- **Bypass citation**: solutions-with-prize/paper28-pvnp/preprint Steps 11-15 + CP-1; independent 6-Critic verification (Wave 1, 2 SURVIVED / 3 WEAKENED repaired / 1 BROKEN on Route D only)
- **Aggregate confidence**: p = 0.82 (Part (i) 0.85 × Part (ii) 0.90)
- **Alternate bypass routes enumerated** (A-G from paper28 PROOF-CHAIN.md): (A) direct spectral gap [highest priority if C fails]; (B) universal-algebraic; (D) Popa cocycle superrigidity; (E) Kazhdan/Haagerup bridge; (F) trinity dictionary inversion; (G) conditional fallback
- **Effect if CP-1 audit regresses**: Route A (direct spectral gap bypass) takes over; does not invalidate chain; Part (i) remains UNCONDITIONAL
- **Effect if Route C fully repairs**: W1 upgrades to PROVED

Secondary walls (also disclose in §16):
- **W2**: KMS₁ uniqueness (KEY LEMMA 3.4.3) — existence PROVED, uniqueness conditional; downstream INSULATED (fullness state-independent)
- **W3**: Spectral identification H_R^Bool ↔ {γ_n · π²/2} — CONJECTURE; possibly equivalent to RH for Boolean BC; non-load-bearing for P ≠ NP main theorem

Transparency here is what makes §5d compliance work. Silence here fails §5d.

Additional translation-layer disclosure (DELTA 10 continued):

- Any SILENT in Req 1 (TM model) or Req 2 (P/NP definitions) → insert §12 TM-Model Translation Layer as bridge (see DELTA 5). This is not optional: Cook §1-§2 require the P/NP concepts to be stated in the TM / language-theoretic formulation, and the operator-algebraic chain must be shown to imply the Cook-formal separation, not just an operator-algebraic dichotomy.

---

## PROCEDURE

### Step 1 — Read inputs (mandatory, in order)

1. `strategy/pvnp/00-millenium-strategy.md` — the strategy doc (sibling of this brief)
2. `solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md` — the 6-link live chain (top-level)
3. `solutions-with-prize/paper28-pvnp/preprint/PROOF-CHAIN.md` — the 23-node expanded chain (Part (i) Path B + Part (ii) Route C + Corollary)
4. `solutions-with-prize/paper28-pvnp/draft/00-table-of-contents.md` — the 7-section paper skeleton
5. Cook §1-§3 (the Clay PDF; summary in strategy doc §1)
6. Clay Rules §4-§8 (summary in strategy doc §2)

### Step 2 — Build compliance map

For each (node, requirement) cell in the 23 × 6 = 138-cell matrix:
- Author: VERIFY whether the node addresses the requirement; emit verdict + citation
- Critic: attack the verdict; propose alternative
- Arbiter: decide; record rejected alternative as footnote

Write `compliance-map.md`. Summarize by requirement (percentage of each verdict class).

### Step 3 — Address SILENT verdicts

For each SILENT cell:
- DECOMPOSE into a new named wall OR
- CONSTRUCT a new layer with theorem statement + citation OR
- BYPASS via capacitor transposition (cite capacitor cell)

Priority: insert §12 TM-Model Translation Layer if Req 1 / Req 2 is SILENT. Update compliance map. No cell may remain SILENT at end of this step.

### Step 4 — Synthesize B_bare

Walk the 18-section structure (§1-§18). Each section pulls from relevant compliance-map cells.

Enforce bare discipline: zero prose paragraphs. Theorem statements only.

Target: ≤ 15 pages (estimated ~400-600 lines of markdown).

Write to `strategy/pvnp/deliverables/pvnp-clay-bare.md`.

### Step 5 — Synthesize C_bare

Walk the 10-section structure. Draw from:
- Paper 15 (transposition dictionary, R-Theorem S.11)
- Paper 17 (entropy operator, order-counting principle)
- Paper 23 (CBB quintuple, bridge family)
- Paper 26 (BSD transposition mechanics)
- Paper 28 (PvNP itself — draft + preprint sections)
- Cross-Clay x-ray cross-cuts (when available)
- Programme 36-pins / framework-predictions tables if any rows relevant to PvNP

Enforce bare discipline. Zero prose.

Write to `strategy/pvnp/deliverables/pvnp-beyond-bare.md`.

### Step 6 — Verification pass

Critic examines B_bare + C_bare for:
- Any prose paragraph (FAIL if found)
- Any uncited claim (FAIL)
- Any SILENT Cook requirement (FAIL)
- Any named wall without bypass-route disclosure (FAIL)
- Missing §12 TM-Model Translation Layer (FAIL — Cook Req 1/2 coverage)
- Page count > 15 per document (WARN; target = 15)

Arbiter emits PUBLISH-READY verdict if all checks pass, NEEDS-REVISION otherwise.

### Step 7 — Commit memo

Write `commit-memo.md` summarizing:
- Compliance map results (verdict distribution)
- New named walls created
- New layers constructed (especially TM-Model Translation Layer)
- Cells remaining in each status
- B_bare + C_bare page counts
- Lock status (LOCKED / NOT-LOCKED with reason)
- Recommendation for next step (composition-backward? more compliance work?)

---

## SUCCESS CRITERIA

- Compliance map 23×6 complete; every cell has verdict + citation + arbiter decision
- Zero SILENT cells in final state
- B_bare written, ≤ 15 pages, zero prose, every claim cited
- B_bare §12 TM-Model Translation Layer present and load-bearing
- C_bare written, ≤ 15 pages, zero prose, every claim cited
- W1 (Link 5 backward) explicitly disclosed with all required fields including seven-route bypass list
- W2 (KMS₁ uniqueness) and W3 (spectral identification) disclosed with insulation notes
- All three barriers (Cook §3) addressed in B_bare §13
- All programme papers referenced have §-level precision
- Critic pass: PUBLISH-READY verdict

A run FAILS if:
- Any SILENT cell remains
- Any prose paragraph appears in B_bare or C_bare
- Any claim lacks citation
- Named walls lack bypass-route disclosure
- §12 TM-Model Translation Layer missing

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

the current run brief (PVNP MILLENNIUM DELTA) is
strategy/pvnp/pvnp-millenium-brief.md

the strategy document is
strategy/pvnp/00-millenium-strategy.md

the live chain files are
solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md
solutions-with-prize/paper28-pvnp/preprint/PROOF-CHAIN.md

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see 00-millenium-strategy.md §9 for Zenodo-first cascade.)

the run output directory is
strategy/pvnp/pac-output/runs/run-NN/

outputs:
- Output A (internal) → strategy/pvnp/pac-output/runs/run-NN/
- Output B_bare (Clay-shaped skeleton) → strategy/pvnp/deliverables/pvnp-clay-bare.md
- Output C_bare (Beyond-Clay skeleton) → strategy/pvnp/deliverables/pvnp-beyond-bare.md

DO NOT produce B_full or C_full this run. DEFERRED to composition-backward.

MODE: compliance-audit + bare-deliverable-synthesis.

Run plan:
1. Read inputs (§1-§6 above)
2. Build 23×6 compliance map (138 cells)
3. Address SILENT verdicts (no cell silent at end); insert §12 TM-Model Translation Layer
4. Synthesize B_bare (18 sections, ≤ 15 pages, zero prose)
5. Synthesize C_bare (10 sections, ≤ 15 pages, zero prose)
6. Verification pass (critic → arbiter PUBLISH-READY)
7. Commit memo with lock status + recommendation

Begin.
```

---

## INVOCATION STYLE B — Agent-tool spawning

Self-contained for claude-code sub-agent spawning. Parameters: `<RUN-NN>`.

```
You are the PAC operator running on the PvNP Millennium bundle. This is run <RUN-NN>. Produce a Clay-compliance-audited PvNP deliverable in BARE MODE ONLY. B_full and C_full are DEFERRED.

## GOAL

Three deliverables:
A. Internal artifacts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/pac-output/runs/<RUN-NN>/
B_bare. Clay-shaped X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/deliverables/pvnp-clay-bare.md
C_bare. Beyond-Clay X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/deliverables/pvnp-beyond-bare.md

## READ FIRST (in order)

1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/00-millenium-strategy.md (strategy doc)
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/pvnp-millenium-brief.md (this brief)
3. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper28-pvnp/PROOF-CHAIN.md (6-link top-level chain)
4. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper28-pvnp/preprint/PROOF-CHAIN.md (23-node expanded chain)
5. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper28-pvnp/draft/00-table-of-contents.md (paper skeleton)

## READ AS NEEDED

- /Users/gsix/quantum-geometry-in-5d-latex/paper15/ (transposition dictionary + R-Theorem S.11)
- /Users/gsix/quantum-geometry-in-5d-latex/paper17/ (entropy operator + order-counting principle)
- /Users/gsix/quantum-geometry-in-5d-latex/paper23/ (CBB quintuple + bridge family)
- /Users/gsix/quantum-geometry-in-5d-latex/paper26/ (BSD transposition mechanics)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/PROOF-CHAIN.md (QG5D hub; for trinity dictionary + cube-shadow)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper13-rh/PROOF-CHAIN.md (for cross-Clay RH connection)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md (for cross-Clay YM connection)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper26-bsd/PROOF-CHAIN.md (for cross-Clay BSD connection)
- /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/ (ORA patterns)
- /Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md (capacitor)

## WRITE (required files)

Primary deliverables:
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/deliverables/pvnp-clay-bare.md
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/deliverables/pvnp-beyond-bare.md

Run transcripts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/pvnp/pac-output/runs/<RUN-NN>/:
- blackboard.md
- compliance-map.md (23-node × 6-requirement = 138-cell matrix)
- vertices/pvnp/ (per-node artifacts)
- kills.md, critic-attacks.md, arbiter-decisions.md
- commit-memo.md

## HARD DISCIPLINE

1. **BARE MODE ONLY.** B_bare and C_bare contain ZERO prose paragraphs. Theorem statements + definitions + equations + figures + numbers + citations only. No "introduction," no "motivation," no "discussion," no prose proofs, no "we show that," no "note that." If a section attracts prose, REMOVE the section.

2. **Compliance map 23×6 mandatory.** Every cell verdict: PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation. Zero SILENT at end.

3. **Citations per claim.** Every theorem, number, equation cites programme paper + specific proof location (paperNN §X Theorem T.Y format).

4. **W1 (Link 5 backward) explicit disclosure** in B_bare §11 and §16: NAMED WALL, Route C bypass via CP-1, seven alternate bypass routes A-G enumerated, aggregate confidence p = 0.82, CP-1 6-Critic verification status.

5. **W2 and W3 disclosure with insulation notes** in B_bare §16: W2 downstream-insulated, W3 non-load-bearing.

6. **§12 TM-Model Translation Layer LOAD-BEARING** in B_bare. This is the bridge from operator-algebraic non-fullness to Cook-formal P ≠ NP. Must cite Cook Def.~1-~4 + BZ backward + paper28 §4.6 Corollary.

7. **Three barriers addressed** in B_bare §13: non-relativization, non-naturalness, non-algebrization.

8. **≤ 15 pages per bare document.** Target ~400-600 lines markdown.

9. **Page count is a quality proxy.** If you find yourself writing a full page on one theorem's prose, you've left bare mode.

10. **B_full and C_full NOT produced this run.** DEFERRED to composition-backward (future run using parallel agents on 60-project reservoir).

## SUCCESS CRITERIA

- Compliance map complete, zero SILENT
- B_bare + C_bare written, bare discipline enforced
- Every claim cited
- W1 disclosed with all required fields (including seven bypass routes)
- W2 / W3 disclosed with insulation notes
- §12 TM-Model Translation Layer present
- §13 all three barriers cleared
- Critic PUBLISH-READY verdict
- Commit memo records lock status

If blocked (ambiguous verdict, missing citation, etc.): log in blackboard, DO YOUR BEST, flag NEEDS-REVIEW, continue. Don't block on perfection. The next run iterates.

Begin by reading the 5 mandatory files in order. Then plan in blackboard. Then execute.
```

---

*End of brief. Bare-first, prose-deferred. B_full and C_full composed backward by parallel agents after bare locks. The cascade begins with Zenodo. The Clay 2-year clock starts at journal publication. Link 5 backward runs in parallel, non-blocking.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
