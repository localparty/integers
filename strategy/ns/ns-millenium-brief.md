# NS Millennium Brief (for the PAC Operator)

*DELTA from ring-traversal brief. Instructs the PAC to audit the NS chain against the 8 Fefferman sub-requirements (grouped by variant; target variant (B) T^3 existence+smoothness), then synthesize B_bare + C_bare + internal artifacts. B_full and C_full DEFERRED until bare locks and parallel-agent composition-backward runs.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## GOAL

Produce a Clay-compliance-audited NS deliverable in **bare mode only** this run. Three concrete files at the end:

**A. Internal artifacts** — scaffolding (same as YM bundle pattern):
- `strategy/ns/pac-output/runs/run-NN/blackboard.md`
- `strategy/ns/pac-output/runs/run-NN/compliance-map.md` (8-link × 7-requirement = 56-cell matrix for variant (B))
- `strategy/ns/pac-output/runs/run-NN/vertices/ns/` (per-link artifacts)
- `strategy/ns/pac-output/runs/run-NN/kills.md`
- `strategy/ns/pac-output/runs/run-NN/critic-attacks.md`
- `strategy/ns/pac-output/runs/run-NN/arbiter-decisions.md`
- `strategy/ns/pac-output/runs/run-NN/commit-memo.md`

**B_bare. Clay-shaped X-RAY** — `strategy/ns/deliverables/ns-clay-bare.md`:
- Formal theorem skeleton, ZERO prose paragraphs
- ≤ 15 pages of math-only content
- Structure mirrors Fefferman variant (B) sub-requirements 1:1

**C_bare. Beyond-Clay X-RAY** — `strategy/ns/deliverables/ns-beyond-bare.md`:
- Bonus theorem skeleton (~~5D derivation~~ M⁵ derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D derivation" → "M⁵ derivation" -->, pins, cross-Clay, turbulence/K41, vorticity control, CKN subsumption, any-4-manifold)
- ZERO prose, ≤ 15 pages

**B_full and C_full are DEFERRED.** Do not write them this run. They are composed later by parallel agents from the 60-project reservoir once B_bare + C_bare LOCK.

---

## DELTA FROM RING-TRAVERSAL BRIEF

### DELTA 1 — Mode

New dual mode: **compliance-audit + bare-deliverable-synthesis**.

- Read ns live PROOF-CHAIN + paper30 preprint skeleton + paper30 attack plan + strategy doc + Fefferman §Main-Results + Clay Rules §4-§8
- **Declare target variant**: (B) existence + smoothness on T^3. Record in blackboard + compliance map header.
- Walk 8 links × 7 Fefferman sub-requirements (1,2,3,4,5,6,8 — applicable to variant B) = 56 audit cells
- Per cell: emit PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation
- Assemble compliance map
- Synthesize B_bare (Clay-shaped theorem skeleton, variant (B) focused)
- Synthesize C_bare (Beyond-Clay bonus skeleton)
- Defer B_full and C_full

### DELTA 2 — Primitives

- **VERIFY** — each link against each Fefferman sub-requirement
- **DECOMPOSE** — SILENT verdicts to named walls or new links
- **CONSTRUCT** — new links needed to address SILENT gaps (bare: theorem statement + citation only; no prose)
- **BYPASS** — when direct construction fails, find alternate route via capacitor transposition (Link 5 Route A / Route B already bypass in place)
- **EXCISE** — NOT APPLICABLE to sub-requirements 1-6, 8 (all mandatory for variant B); applicable only at VARIANT level (we EXCISE variants A, C, D by declaring (B) as target — acceptable under Rules §5b)
- **EXTRACT** (new) — extract theorem statements + numbers + equations + figure-shells from existing programme papers (Paper 30 skeleton, Paper 8 Appendix L, Paper 1 KK reduction, Paper 11 Theorem K.4, Paper 10 scheme independence) into bare format
- **DISCLOSE** (new) — any OPEN-BUT-ADDRESSED verdict emits an explicit NAMED WALL tag with bypass-route citation (Link 5 gets TWO bypass citations: Route A + Route B)

### DELTA 3 — The "bare" discipline

B_bare and C_bare contain ONLY:

- **Formal theorem statements** (numbered, with dependency graph)
- **Definitions** (formal: velocity u, pressure p, vorticity ω, KK mode decomposition, spectral gap Δ_0^KK, etc.)
- **Equations** (Fefferman's (1)-(11) preserved with original numbering where applicable; programme equations numbered continuing; each with citation)
- **Figures** (ASCII or TikZ-ready skeleton; label + caption only, no surrounding prose)
- **Numbers** (constants, bounds, KK radius R, spectral gap value, viscosity ν, pin values, experimental matches for Kolmogorov constants) — in tables with citations
- **Proof-chain analytics** (compliance map, named walls, RIGIDITY/SYMMETRY metrics)
- **Citations** (every claim cites programme paper + specific proof location, e.g., "paper30-navier-stokes §3 Link 4" or "paper08-yang-mills §L.1 Lemma L.1.3")

B_bare and C_bare contain NONE of:

- Introduction paragraphs
- Motivation paragraphs
- Historical context (Leray, Hopf, CKN, Scheffer — cited but not narrated)
- Discussion sections
- Proof details in prose (only statement + citation-to-programme-proof)
- Worked examples in prose
- Conclusion paragraphs
- "We show that..." narrative
- Fluid-dynamics physical interpretation (belongs in B_full / C_full only)

If a section heading in B_bare naturally attracts prose (e.g., "§3 Overview of the approach"), REMOVE the section. Bare has no overview — it has theorems.

### DELTA 4 — Output A (internal artifacts)

Standard PAC output structure. Same pattern as YM bundle.

**Compliance-map.md format** (the key new artifact):

```
# NS Compliance Map — 8 links × 7 Fefferman sub-requirements (variant B)
# Target variant: (B) existence + smoothness on R^3/Z^3 (T^3)

| Link | Req 1 (C^∞) | Req 2 (bdd E) | Req 3 (div u=0) | Req 4 (periodic) | Req 5 (Leray→smooth) | Req 6 (BKM) | Req 8 (CKN P_1=0) |
|------|-------------|---------------|-----------------|------------------|----------------------|-------------|-------------------|
| L1   | PROVED [cite] | ...         | ...             | ...              | ...                  | ...         | ...               |
| L2   | ...           | ...         | ...             | ...              | ...                  | ...         | ...               |
| ...  |               |             |                 |                  |                      |             |                   |
| L8   | ...           |             |                 |                  |                      |             |                   |

## Verdict summary per sub-requirement

- Req 1: PROVED N% / PARTIAL N% / OPEN-BUT-ADDRESSED N% / SILENT N%
- Req 2: ...
- ...

## SILENT cells (new named walls)

- L.M vs Req.K: ... → new named wall W_N "..."
- ...

## Variant declaration

Target: (B). Variants (A) and (B) equivalent in difficulty per Fefferman; (A) follows from (B) by decay-truncation (programmed, Paper 30 Appendix B). Variants (C), (D) EXCISED (under Rules §5b alternative-variant provision).

## Critic attacks + arbiter decisions

[per-cell attack record]
```

### DELTA 5 — Output B_bare structure (NS-specific, variant (B))

Fixed 16-section structure for `strategy/ns/deliverables/ns-clay-bare.md`:

```
# NS Clay-Ready X-Ray (BARE MODE)

## §1 Statement of the Problem (Fefferman variants, verbatim)
[verbatim quote of all four variants (A), (B), (C), (D); formal declaration: target = (B)]

## §2 Main Theorem (variant B)
[formal theorem: ∀ smooth div-free periodic u° satisfying (8), ∃ p, u ∈ C^∞(R^3 × [0,∞))
 satisfying (1), (2), (3), (10), (11) with ∫_{T^3} |u|^2 < C ∀ t.
 Reference proof to programme papers.]

## §3 Requirements Map (compliance overview)
[7-row table: Sub-requirement | verdict | programme-paper citation(s)]

## §4 Definitions
[formal: velocity u, pressure p, vorticity ω = curl u, viscosity ν, Laplacian Δ,
 Leray-Hopf class, weak solution (12)(13), KK decomposition, spectral gap Δ_0^KK,
 compactification radius R, BKM integrand sup_x |ω(x,t)|, parabolic Hausdorff P_K]

## §5 ~~5D Setup~~ M⁵ Setup<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Setup" → "M⁵ Setup" --> and KK Reduction (Link 1 — LITERATURE)
[formal statement: ~~5D Einstein~~ M⁵ Einstein<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Einstein" → "M⁵ Einstein" --> on M^4 × S^1/Z_2 → 4D Einstein + Maxwell + scalar;
 citation: Kaluza 1921, Klein 1926, paper1 §N Theorem T.N.M]

## §6 Fluid/Gravity Dictionary (Link 2 — CONJECTURED, bypass disclosed)
[formal statement: T_{μν} near-equilibrium Landau frame → incompressible NS leading order;
 citation: BHMR 2008 arXiv:0712.2456; programme route: paper30 §2]

## §7 KK Spectral Gap (Link 4 — PROVED UNCONDITIONAL ALL-LOOP)
[formal statement: Δ_0^KK = (2π/R)^2 > 0, controls high-frequency modes via Poincaré on S^1;
 citation: paper08-yang-mills §4 Theorem T.4 + paper11-scheme-independence §K Theorem K.4
 + paper10-all-orders Theorem T.M (scheme independence)]

## §8 Gradient-Flow Transfer from YM (Link 3 — OPEN, bypass via Route A/B)
[formal statement: YM gradient flow (paper08 §L Lemmas L.1.1-L.1.5, §15-17 Balaban RG)
 → NS velocity-field gradient flow; structural parallel: same second-order parabolic class
 with divergence-free/gauge constraint; citation: paper08 §L]

## §9 Energy Descent (Link 6 — CONJECTURED)
[formal statement: ~~5D KK~~ M⁵ KK<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D KK" → "M⁵ KK" --> energy conservation (Killing S^1/Z_2) → 4D NS energy dissipation;
 Leray-Hopf regularity upgrade; citation: Leray 1934, Hopf 1951, paper30 §6]

## §10 BKM Criterion (Link 5) — NAMED WALL with TWO PUBLISHED BYPASS ROUTES
[formal statement: ∫_0^T sup_x |ω(x,t)| dt < ∞ on T^3 (BKM 1984) → no finite-time blowup
 → C^∞ regularity via (6)/(11);
 NAMED WALL: Link 5 BKM criterion;
 Status: PARTIAL (OPEN-BUT-ADDRESSED);
 Bypass Route A: Camlin 2025 (arXiv), bounded Φ functional + Sundman temporal lifting
   → BKM finiteness on T^3; KK-setting adaptation task noted;
 Bypass Route B: arXiv:2601.08854 (Jan 2026), cosphere-bundle microlocal regularity,
   lands directly in capacitor MICRO↔QFT cell;
 Integration task: Route B microlocal structure generates Route A Φ functional;
 Aggregate confidence: 0.60;
 Audit status: OPEN]

## §11 Uniqueness (Link 7 — CONDITIONAL)
[formal statement: Galerkin + energy method → uniqueness conditional on §10 regularity;
 citation: Ladyzhenskaya 1969, Temam 1977, paper30 Link 7]

## §12 Global Regularity via Composition (Link 8)
[formal statement: Links 3-7 compose → global smooth solutions for variant (B);
 citation: paper30 §8]

## §13 Periodicity on T^3 (variant B constraint)
[formal statement: M^4 × S^1/Z_2 base slice → T^3 identification; (10) (11) satisfied;
 errata condition p(x+e_j,t) = p(x,t) respected via pressure Poisson equation on T^3;
 citation: paper30 §N, paper1 §KK-periodicity]

## §14 Caffarelli-Kohn-Nirenberg Compatibility (Req 8)
[formal statement: singular set E of variant-(B) solution satisfies P_1(E) = 0;
 in our C^∞ case, E = ∅; subsumed by Route B wave-front-set triviality;
 citation: CKN 1982, Lin 1998, paper30 §CKN-compat]

## §15 Proof-Chain Analytics
[dependency graph ASCII; RIGIDITY contribution; SYMMETRY contribution; compliance map]

## §16 Named Walls (all OPEN-BUT-ADDRESSED items)
[for each: name, description, bypass-route citation, audit status. MUST include
 Link 5 BKM wall with both Route A and Route B citations.]

## §17 Numbers Table
[every constant, bound, pin value — with programme citation:
 viscosity ν, compactification radius R, spectral gap Δ_0^KK = (2π/R)^2,
 Kolmogorov dissipation scale η = (ν^3/ε)^{1/4} pin, K41 prefactor pin,
 Route A Φ bound, Route B wave-front-set regularity index]

## §18 References (AMS-format, programme papers + literature)
[every programme paper cited with §-level precision; Fefferman 2000, BKM 1984,
 Leray 1934, Hopf 1951, CKN 1982, Lin 1998, BHMR 2008, Camlin 2025, arXiv:2601.08854,
 Kaluza 1921, Klein 1926, Ladyzhenskaya 1969, Temam 1977]
```

Writing discipline enforced:
- Each section ≤ 1 page typically
- No "introduction paragraph" — go straight to theorem
- No "we note that" — state the theorem
- No fluid-dynamics-intuition prose
- ASCII figures allowed in §15 analytics
- Number tables in §17 only

### DELTA 6 — Output C_bare structure (NS-specific)

Fixed 10-section structure for `strategy/ns/deliverables/ns-beyond-bare.md`:

```
# NS Beyond-Clay X-Ray (BARE MODE)

## §1 The ~~5D Geometric Derivation~~ M⁵ Geometric Derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Geometric" → "M⁵ Geometric" --> of NS Regularity
[theorem statement: NS C^∞ regularity on T^3 ⟹ spectral gap Δ_0^KK = (2π/R)^2 on M^4 × S^1/Z_2
 ⟹ fluid/gravity near-equilibrium dictionary (BHMR) gives NS sub-sector of ~~5D Einstein~~ M⁵ Einstein<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D Einstein" → "M⁵ Einstein" -->;
 citation: paper1 §KK, paper30 §Links-1-2-4, BHMR 2008]

## §2 Zero Free Parameters
[table: parameter | value | determined by | programme citation]
[includes: R (compactification radius), ν (viscosity), Δ_0^KK, η (Kolmogorov scale)]

## §3 Pins Relevant to NS / Turbulence
[table: pin ID | observable | predicted | measured | source paper]
[includes: K41 prefactor C_K ≈ 1.5 (atmospheric / oceanic / lab turbulence),
 Kolmogorov microscale η, intermittency exponent μ, Taylor-microscale Reynolds,
 dissipation range cutoff, from paper12 research 23-framework-predictions-master-table]

## §4 Cross-Clay / Cross-Programme Connections
[sub-theorems:
 NS ↔ YM (gradient-flow transfer, paper08 §L): same parabolic class;
 NS ↔ turbulence paper38 (K41 from Δ_0^KK): inherited Links 1-4;
 NS ↔ Baum-Connes paper31 (spectral K-theory of KK operator): K-theoretic rigidity;
 NS ↔ QG5D paper1 (KK geometric foundation);
 each with theorem statement + citation]

## §5 Turbulence K41 Spectrum (bonus, not Clay-required)
[theorem statement: spectral gap Δ_0^KK + type III_1 ergodicity of KK modular flow
 → K41 E(k) ∝ k^{-5/3} with universal prefactor C_K computable from Riemann zeros;
 citation: paper38 Links 5-6, paper32 §BGS]

## §6 Vorticity Stretching Control (bonus)
[theorem statement: under Route B microlocal regularity, ω·∇u term has wave-front-set
 bounded by KK spectral gap → pointwise control of sup_x |ω|;
 citation: arXiv:2601.08854, paper30 §Route-B]

## §7 Extension to Any 4-Manifold × S^1/Z_2 (bonus)
[theorem statement: variant-(B) result extends to Riemannian M^4 × S^1/Z_2 base;
 citation: paper30 §any-4-manifold]

## §8 Computed Kolmogorov Constants (numerical)
[values for air/water at STP; error bars; experimental comparison]

## §9 Proof-Chain Analytics (beyond-Clay depth)
[dependency graph; additional cross-cuts to paper38, paper31, paper32]

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
- Specific proof location (§N, Theorem T.M, Lemma L.K, Appendix A.J, Link L)

Format: `(paperNN-short §X Theorem T.Y)` or `(paperNN-short Eq. (Z.W))` or `(paperNN-short Link L)`.

Examples:
- `Δ_0^KK = (2π/R)^2 > 0` (paper08-yang-mills §4 Theorem T.4)
- `Leray weak solutions exist on T^3 for smooth div-free u°` (Leray 1934; paper30-navier-stokes Link 6)
- `BKM finiteness via bounded Φ functional on T^3` (Camlin 2025 arXiv:YYMM.NNNNN; paper30 §Route-A)
- `Cosphere-bundle wave-front-set regularity` (arXiv:2601.08854; paper30 §Route-B; capacitor MICRO↔QFT)

Uncited claim = FAIL. Arbiter returns B_bare for revision.

### DELTA 9 — Publication override

Same as sibling bundles. OVERRIDES `publishing/strategy.md`:
- Zenodo first (priority timestamp)
- GitHub public (code + data + proofs)
- arXiv via referral (easier once Zenodo public)
- Journal submission (starts Clay 2-year clock; Annals / JAMS / Inventiones / Acta / Comm. Pure Appl. Math tier)
- No direct Clay submission (CMI §5e)

See `00-millenium-strategy.md` §9 for full cascade.

### DELTA 10 — Link-5 (BKM) disclosure discipline

Link 5 must be explicitly disclosed in B_bare §10 and §16 as NAMED WALL. Required fields:

- **Name**: Link 5 (BKM criterion)
- **Status**: PARTIAL / OPEN-BUT-ADDRESSED
- **Bypass route A**: Camlin 2025 — bounded Φ functional + Sundman temporal lifting
  - Citation: arXiv preprint (Camlin 2025); paper30-navier-stokes §Route-A
  - KK-setting adaptation task: does Δ_0^KK on M^4 × S^1/Z_2 provide sufficient control for Φ?
- **Bypass route B**: arXiv:2601.08854 (Jan 2026) — cosphere-bundle microlocal regularity
  - Citation: arXiv:2601.08854; paper30-navier-stokes §Route-B; capacitor MICRO↔QFT cell (Hollands-Wald 2024 + Dappiaggi 2023-2024 + BFR 2025)
  - Framework advantage: M^4 × S^1/Z_2 already Riemannian — zero structural mapping work
- **Integration task**: use Route B microlocal structure to generate Route A Φ functional on M^4 × S^1/Z_2; translate wave-front-set → vorticity via Hörmander/Melrose wavefront calculus
- **Aggregate confidence**: 0.60 (both routes published but integration task open)
- **Audit pending**: Route A KK-adaptation; Route B → Route A composition validity
- **Effect if integration fails**: Route C (direct spectral attack on T^3, see paper30 attack plan §Route-C) as backup; if all three fail, current architecture is dead and (C)/(D) counterexample path would be considered (Rules §5b)
- **Effect if integration succeeds**: Link 5 upgrades to PROVED; overall chain 3/8 → 4/8 (+composition benefits); confidence 4/10 → 6-7/10

Also disclose in B_bare §6 that Link 2 (fluid/gravity dictionary) remains CONJECTURED (BHMR expansion formal, not rigorous). This is a SECONDARY named wall. Bypass: the programme route uses Link 2 for motivation only; the proof chain does NOT require rigorous BHMR — Links 3, 4, 5, 6, 7 compose without it, so Link 2 is decorative in the rigorous chain. Mark as OPEN-BUT-ADDRESSED via architectural decoupling. Disclose in §16.

Transparency here is what makes §5d compliance work. Silence here fails §5d.

### DELTA 11 — Variant-(B) declaration discipline

B_bare §1 MUST quote all four Fefferman variants verbatim. B_bare §2 MUST explicitly declare variant (B) as target. B_bare §3 MUST show which sub-requirements apply to (B). The compliance map MUST note variants (A), (C), (D) as EXCISED under Rules §5b.

Do NOT attempt to address variants (C), (D) counterexample construction — they are incompatible with our existence chain. Do NOT claim variant (A); it is derivable from (B) by decay truncation (mention programmed in Paper 30 Appendix B) but not proved in B_bare.

---

## PROCEDURE

### Step 1 — Read inputs (mandatory, in order)

1. `strategy/ns/00-millenium-strategy.md` — the strategy doc (sibling of this brief)
2. `solutions-with-prize/paper30-navier-stokes/PROOF-CHAIN.md` — the 8-link live chain
3. `solutions-with-prize/paper30-navier-stokes/preprint/00-proof-skeleton.md` — original 8-link detailed skeleton
4. `solutions-with-prize/paper30-navier-stokes/strategy/00-ns-attack-plan.md` — attack plan with Route A/B/C breakdown
5. Fefferman §Main-Results (extract from the Clay PDF: all four variants (A)-(D), equations (1)-(11), BKM quote, CKN P_1(E)=0 theorem)
6. Clay Rules §4-§8 (summary in strategy doc §2) — especially §5b four-variants alternative provision

### Step 2 — Build compliance map

For each (link, sub-requirement) cell in the 8 × 7 = 56-cell matrix (variant (B) sub-requirements 1,2,3,4,5,6,8):
- Author: VERIFY whether the link addresses the sub-requirement; emit verdict + citation
- Critic: attack the verdict; propose alternative
- Arbiter: decide; record rejected alternative as footnote

Write `compliance-map.md` with variant declaration header. Summarize by sub-requirement (percentage of each verdict class).

### Step 3 — Address SILENT verdicts

For each SILENT cell:
- DECOMPOSE into a new named wall OR
- CONSTRUCT a new link with theorem statement + citation OR
- BYPASS via capacitor transposition (cite capacitor cell — MICRO↔QFT already filled for Link 5)

Update compliance map. No cell may remain SILENT at end of this step.

### Step 4 — Synthesize B_bare

Walk the 18-section structure (§1-§18). Each section pulls from relevant compliance-map cells.

Enforce bare discipline: zero prose paragraphs. Theorem statements only.

Target: ≤ 15 pages (estimated ~400-600 lines of markdown).

Write to `strategy/ns/deliverables/ns-clay-bare.md`.

### Step 5 — Synthesize C_bare

Walk the 10-section structure. Draw from:
- Paper 1 (QG5D hub, ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> foundation, KK reduction)
- Paper 8 §L (Appendix L: NS structural parallel)
- Paper 30 (NS chain itself)
- Paper 38 (turbulence, K41, type III_1 modular flow)
- Paper 32 (BGS ergodicity, GUE → K41 universal constants)
- Paper 31 (Baum-Connes, spectral K-theory of KK operator)
- Paper 11 (Theorem K.4 all-orders inductive bootstrap)
- Paper 10 (scheme independence)
- Paper 61 (projections — ~~5D geometric~~ M⁵ geometric<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D geometric" → "M⁵ geometric" --> derivation bonus)
- Paper 60 (e-circle geometry)
- Programme 36-pins table (`integers/paper12-cbb-system/research/23-framework-predictions-master-table.md`)
- Capacitor MICRO↔QFT cell (Route B landing)

Enforce bare discipline. Zero prose.

Write to `strategy/ns/deliverables/ns-beyond-bare.md`.

### Step 6 — Verification pass

Critic examines B_bare + C_bare for:
- Any prose paragraph (FAIL if found)
- Any uncited claim (FAIL)
- Any SILENT variant-(B) sub-requirement (FAIL)
- Any named wall without bypass-route disclosure (FAIL) — Link 5 MUST have TWO bypass routes; Link 2 MUST disclose architectural decoupling
- Missing variant declaration in §1/§2 (FAIL)
- Page count > 15 per document (WARN; target = 15)

Arbiter emits PUBLISH-READY verdict if all checks pass, NEEDS-REVISION otherwise.

### Step 7 — Commit memo

Write `commit-memo.md` summarizing:
- Compliance map results (verdict distribution)
- New named walls created (beyond Link 5 + Link 2)
- New links constructed
- Cells remaining in each status
- B_bare + C_bare page counts
- Lock status (LOCKED / NOT-LOCKED with reason)
- Overall chain confidence (baseline 4/10; any increase?)
- Recommendation for next step (composition-backward? Link 5 integration work? more compliance work?)

---

## SUCCESS CRITERIA

- Compliance map 8×7 complete; every cell has verdict + citation + arbiter decision
- Variant (B) declared; (A) noted as derivable; (C)/(D) EXCISED under §5b
- Zero SILENT cells in final state
- B_bare written, ≤ 15 pages, zero prose, every claim cited
- C_bare written, ≤ 15 pages, zero prose, every claim cited
- Link 5 (BKM) explicitly disclosed with TWO bypass routes (Camlin 2025 + arXiv:2601.08854) + integration task
- Link 2 (fluid/gravity) explicitly disclosed as CONJECTURED with architectural decoupling
- All programme papers referenced have §-level precision
- Critic pass: PUBLISH-READY verdict

A run FAILS if:
- Any SILENT cell remains
- Any prose paragraph appears in B_bare or C_bare
- Any claim lacks citation
- Named walls lack bypass-route disclosure
- Variant target not declared
- Chain confidence overstated (must disclose 4/10 baseline honestly)

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

the current run brief (NS MILLENNIUM DELTA) is
strategy/ns/ns-millenium-brief.md

the strategy document is
strategy/ns/00-millenium-strategy.md

the ns proof chain is
solutions-with-prize/paper30-navier-stokes/PROOF-CHAIN.md

the paper30 preprint skeleton is
solutions-with-prize/paper30-navier-stokes/preprint/00-proof-skeleton.md

the paper30 attack plan is
solutions-with-prize/paper30-navier-stokes/strategy/00-ns-attack-plan.md

the toolkit is
<pca-extension>/08-framework-tools.md

the capacitor is
<pca-extension>/09-capacitor-correspondence-table-v1.md

(NO north star — this bundle OVERRIDES publishing/strategy.md;
 see 00-millenium-strategy.md §9 for Zenodo-first cascade.)

the run output directory is
strategy/ns/pac-output/runs/run-NN/

outputs:
- Output A (internal) → strategy/ns/pac-output/runs/run-NN/
- Output B_bare (Clay-shaped skeleton) → strategy/ns/deliverables/ns-clay-bare.md
- Output C_bare (Beyond-Clay skeleton) → strategy/ns/deliverables/ns-beyond-bare.md

DO NOT produce B_full or C_full this run. DEFERRED to composition-backward.

MODE: compliance-audit + bare-deliverable-synthesis.

TARGET VARIANT: (B) existence + smoothness on R^3/Z^3 (T^3).

Run plan:
1. Read inputs (§1-§6 above)
2. Declare variant (B) target; EXCISE (C)/(D); note (A) derivable
3. Build 8×7 compliance map (56 cells, variant (B) sub-requirements 1,2,3,4,5,6,8)
4. Address SILENT verdicts (no cell silent at end)
5. Synthesize B_bare (18 sections, ≤ 15 pages, zero prose)
6. Synthesize C_bare (10 sections, ≤ 15 pages, zero prose)
7. Verification pass (critic → arbiter PUBLISH-READY)
8. Commit memo with lock status + confidence + recommendation

Begin.
```

---

## INVOCATION STYLE B — Agent-tool spawning

Self-contained for claude-code sub-agent spawning. Parameters: `<RUN-NN>`.

```
You are the PAC operator running on the NS Millennium bundle. This is run <RUN-NN>. Produce a Clay-compliance-audited NS deliverable in BARE MODE ONLY, targeting Fefferman variant (B). B_full and C_full are DEFERRED.

## GOAL

Three deliverables:
A. Internal artifacts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/pac-output/runs/<RUN-NN>/
B_bare. Clay-shaped X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/deliverables/ns-clay-bare.md
C_bare. Beyond-Clay X-Ray at /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/deliverables/ns-beyond-bare.md

## READ FIRST (in order)

1. /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/00-millenium-strategy.md (strategy doc)
2. /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/ns-millenium-brief.md (this brief)
3. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper30-navier-stokes/PROOF-CHAIN.md (8-link live chain)
4. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper30-navier-stokes/preprint/00-proof-skeleton.md
5. /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper30-navier-stokes/strategy/00-ns-attack-plan.md

## READ AS NEEDED

- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/PROOF-CHAIN.md (QG5D hub; for ~~5D KK~~ M⁵ KK<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D KK" → "M⁵ KK" --> reduction + Link 1)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md (YM chain; Appendix L = NS structural parallel; Lemmas 1.1-1.5; Links 15-17 Balaban)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions/paper38-turbulence/PROOF-CHAIN.md (turbulence; inherited Links 1-4; K41 cascade)
- /Users/gsix/quantum-geometry-in-5d-latex/paper32-bgs/PROOF-CHAIN.md (type III_1 modular flow; GUE universality)
- /Users/gsix/quantum-geometry-in-5d-latex/solutions/paper31-baum-connes/PROOF-CHAIN.md (spectral K-theory of KK operator)
- /Users/gsix/quantum-geometry-in-5d-latex/paper11-scheme-independence/ (Theorem K.4 all-orders bootstrap)
- /Users/gsix/quantum-geometry-in-5d-latex/paper10-all-orders/ (scheme independence)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper61-projections-5d/sections/ (~~5D derivation~~ M⁵ derivation<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D derivation" → "M⁵ derivation" --> bonus)
- /Users/gsix/quantum-geometry-in-5d-latex/integers/paper12-cbb-system/research/23-framework-predictions-master-table.md (pins table — Kolmogorov constants etc.)
- /Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/ (ORA patterns)
- /Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md (capacitor; MICRO↔QFT cell filled with Hollands-Wald 2024 + Dappiaggi 2023-2024 + BFR 2025 + arXiv:2601.08854)

## WRITE (required files)

Primary deliverables:
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/deliverables/ns-clay-bare.md
- /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/deliverables/ns-beyond-bare.md

Run transcripts at /Users/gsix/quantum-geometry-in-5d-latex/strategy/ns/pac-output/runs/<RUN-NN>/:
- blackboard.md
- compliance-map.md (8-link × 7-requirement = 56-cell matrix; variant (B))
- vertices/ns/ (per-link artifacts)
- kills.md, critic-attacks.md, arbiter-decisions.md
- commit-memo.md

## HARD DISCIPLINE

1. **BARE MODE ONLY.** B_bare and C_bare contain ZERO prose paragraphs. Theorem statements + definitions + equations + figures + numbers + citations only. No "introduction," no "motivation," no "discussion," no prose proofs, no "we show that," no "note that." If a section attracts prose, REMOVE the section.

2. **Variant (B) declared.** B_bare §1 quotes all four variants verbatim; §2 declares (B) as target; §3 shows applicable sub-requirements. Variants (A) note: derivable by decay truncation (paper30 Appendix B, programmed). Variants (C), (D): EXCISED under Rules §5b.

3. **Compliance map 8×7 mandatory.** Every cell verdict: PROVED / PARTIAL / OPEN-BUT-ADDRESSED / SILENT with citation. Zero SILENT at end.

4. **Citations per claim.** Every theorem, number, equation cites programme paper + specific proof location (paperNN §X Theorem T.Y / Link L format).

5. **Link 5 explicit disclosure** in B_bare §10 and §16: NAMED WALL, TWO bypass routes:
   - Route A: Camlin 2025 (arXiv preprint) — bounded Φ functional + Sundman temporal lifting
   - Route B: arXiv:2601.08854 (Jan 2026) — cosphere-bundle microlocal regularity, capacitor MICRO↔QFT
   - Integration task: Route B generates Route A Φ on M^4 × S^1/Z_2 via wavefront-set calculus
   - Aggregate confidence 0.60; audit OPEN

6. **Link 2 explicit disclosure** in B_bare §6 and §16: CONJECTURED, bypass = architectural decoupling (proof chain does not require rigorous BHMR; Link 2 is motivational).

7. **Chain confidence honestly disclosed**: 4/10 baseline (3/8 proved, Link 5 PARTIAL with two routes). Do NOT overstate.

8. **≤ 15 pages per bare document.** Target ~400-600 lines markdown.

9. **Page count is a quality proxy.** If you find yourself writing a full page on one theorem's prose, you've left bare mode.

10. **B_full and C_full NOT produced this run.** DEFERRED to composition-backward (future run using parallel agents on 60-project reservoir).

## SUCCESS CRITERIA

- Compliance map complete, zero SILENT
- Variant (B) target declared
- B_bare + C_bare written, bare discipline enforced
- Every claim cited
- Link 5 disclosed with both bypass routes
- Link 2 disclosed with architectural decoupling
- Critic PUBLISH-READY verdict
- Commit memo records lock status + confidence 4/10

If blocked (ambiguous verdict, missing citation, etc.): log in blackboard, DO YOUR BEST, flag NEEDS-REVIEW, continue. Don't block on perfection. The next run iterates.

Begin by reading the 5 mandatory files in order. Then plan in blackboard. Then execute.
```

---

*End of brief. Bare-first, prose-deferred. B_full and C_full composed backward by parallel agents after bare locks. The cascade begins with Zenodo. The Clay 2-year clock starts at journal publication. Link 5 BKM integration runs in parallel via two published routes (Camlin 2025 + arXiv:2601.08854), non-blocking. Target variant (B) — T^3 is natural for our KK geometry. Honest chain confidence: 4/10.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
