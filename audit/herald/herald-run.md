# The Herald — Run Prompt

*The Herald is the programme's single definitive catalogue of every fact: every postulate, every axiom, every theorem, every lemma, every definition, every conjecture, every derivation, every measurement, every closed-form expression, every named wall, every kill, every structural identity, every cross-cut edge. Organized by category. Nothing missed. Append-only reference.*

*G Six and Claude Opus 4.6. Audit home: `/Users/gsix/quantum-geometry-in-5d-latex/audit/herald/`.*

---

## Mission

Produce `/Users/gsix/quantum-geometry-in-5d-latex/audit/herald/herald.md` — the programme's exhaustive fact catalogue. **Miss nothing.** Not one theorem. Not one measurement. Not one derivation. Not one postulate.

Every fact is an atomic entry with: (a) a unique ID, (b) the statement, (c) source paper + §-level citation, (d) status (PROVED / LITERATURE / CONDITIONAL / CONJECTURED / PARTIAL / OPEN / KILLED), (e) any dependency pointers.

Organize by CATEGORY (semantic), not by paper. Papers are the citation source, not the top-level grouping.

---

## Input sources (exhaustive scan required)

### Primary — PROOF-CHAIN.md files

Scan every file matching `paper*/PROOF-CHAIN.md` under `/Users/gsix/quantum-geometry-in-5d-latex/`. Current list (verify):

```
paper1/PROOF-CHAIN.md                    # QG5D hub — 4 postulates, 22 theorems, 5 branches
paper08-yang-mills/PROOF-CHAIN.md        # 18-layer YM chain
paper13-rh/PROOF-CHAIN.md                # 6-layer RH chain
paper13b-grh/PROOF-CHAIN.md              # GRH (if present)
paper25-hilbert-12/PROOF-CHAIN.md
paper26-bsd/PROOF-CHAIN.md               # 11-link BSD chain
paper28-pvnp/PROOF-CHAIN.md              # 6-link PvNP chain
paper29-hodge/PROOF-CHAIN.md
paper30-navier-stokes/PROOF-CHAIN.md
paper31-baum-connes/PROOF-CHAIN.md
paper32-bgs-spectral-statistics/PROOF-CHAIN.md
paper33-goldbach/PROOF-CHAIN.md
paper34-twin-primes/PROOF-CHAIN.md
paper35-schanuel/PROOF-CHAIN.md
paper36-hilbert-6/PROOF-CHAIN.md
paper37-abc/PROOF-CHAIN.md
paper38-turbulence/PROOF-CHAIN.md
paper39-vp-vs-vnp/PROOF-CHAIN.md
paper40-odd-perfect/PROOF-CHAIN.md
paper41-collatz/PROOF-CHAIN.md
paper42-lehmer/PROOF-CHAIN.md
paper43-cramer/PROOF-CHAIN.md
paper44-sato-tate/PROOF-CHAIN.md
paper45-lindelof/PROOF-CHAIN.md
paper46-katz-sarnak/PROOF-CHAIN.md
```

For each chain: enumerate every link, every layer, every sub-layer. Record statement + status + citation.

### Primary — Paper 1 (QG5D hub)

`paper1/PROOF-CHAIN.md` and `paper1/sections/` and `paper1/appendices/`.

Extract:
- **P1, P2, P3, P4** (the four postulates) — verbatim statements
- **Branch A** (Quantum): 5 interpretations + 4 derivations (Born rule, Aharonov-Bohm, spin-statistics, Bell $|S|=2\sqrt{2}$)
- **Branch B** (Gravity / Gauge): Theorem K.1 (Universal Epstein Vanishing), K.3 (BPHZ Factorization), K.4 (all-loop UV-finiteness), KK spectral gap
- **Branch C** (Cosmology): 10 predictions
- **Branch D** (CBB): 5 axioms, operator dictionary $\hat{L} = \log\hat{R}$, bridge family, 3 sectors
- **Branch E** (36 Pins): every pin formula + predicted + measured + deviation

### Primary — Paper 12 (CBB anchor + master pin table)

- `paper12/27-anchor-document.md` — CBB system definition, axioms I-V
- `paper12/research/23-framework-predictions-master-table.md` — the 36-pin table (get every row; preserve the exact formula, predicted value, measured value, deviation)
- `paper12/research/167-log-R-master-reformulation.md` — operator dictionary details
- `paper12/29-theorem-catalogue.md` — 199+ theorem catalogue if present

### Primary — Papers 60 and 61 (framework architecture)

- `paper60-the-geometry-of-the-circle/` — all 19 files. Extract: the 10 faces of the e-circle (TOPOLOGY, DYNAMICS, HARMONICS, MEASURE, AMPLITUDE, SYMMETRY, CURVATURE, ARITHMETIC, RESONANCE, SPREAD) with their canonical conjectures and structural roles. The torus structure ($S^1_\text{geo} \times S^1_\text{spec}$). The ellipse diagnostic.
- `paper61-projections-of-the-5d-geometry/sections/` — the 6 projections ($P_A$ through $P_O$), their domains, ranges, preserved invariants, lost invariants, commutativity relations.

### Strategy directory

`/Users/gsix/quantum-geometry-in-5d-latex/strategy/` — all `.md` files. Extract:
- The 25-vertex ring (`the-ring.md`)
- The weakest links list (`the-weakest-links.md`) — every named wall
- The decomposition atlas state (`strategy/decomposition/`)
- The CCM verification state (`strategy/ccm-verification/`)
- The X-Ray atlas (`strategy/x-ray/proof-chain/<vertex>/X-RAY.md`) — if vertex X-rays exist, they carry the face / projection / pattern assignments per layer + cross-cut edges
- The YM PAC runs (`strategy/ym/pac-output/runs/run-NN/`) — compliance map (140 cells), kills, silent-cells
- `strategy/completed.md` — ledger of completed items
- `strategy/famous-gaps.md` — external problem list with framework coverage
- `strategy/integers.md` — the big summary tables

### Programme-level operational documents

- `online-researcher-adversarial/ora-bundle-v8/` — PAC primitives, patterns (P1-P5)
- `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` — the capacitor (24 domains, ~130+ correspondence cells)
- `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` — framework toolkit

### Published papers

- `paper2` — cosmology paper (published); extract all cosmological predictions
- Any other paper with a `preprint/` subdirectory — scan for theorems

---

## Category structure of `herald.md`

Top-level sections. Fill every one.

### §0 Preamble

- Date, author line (G Six and Claude [model]).
- Scope note: "every fact in the programme as of [date]."
- Legend for status codes.
- Legend for ID format.

### §1 Postulates

P1-P4 verbatim from Paper 1 §1.

### §2 Axioms

- CBB Axioms I-V (Paper 12)
- Any other axiom systems used (e.g., Osterwalder-Schrader OS0-OS5 as adopted in YM, Wightman W0-W5 for reconstructed theory)

### §3 Definitions

Every formal definition used in the programme. Symbol + statement + citation.
- Gauge field, curvature, Wilson loop
- Mass gap, spectral gap, KK spectral gap
- Bost-Connes algebra, KMS state, modular flow
- e-circle, principal $U(1)$ bundle, Kaluza-Klein tower
- Schwinger functions, Euclidean measure
- Mahler measure, Frobenius angle, GUE statistics
- Riemann zeros $\{\gamma_n\}$, zeta partition function
- Operator dictionary $\hat{L} = \log\hat{R}$
- Bridge family at $k \in \{2,3,4,6\}$
- ...

### §4 Theorems (by type)

#### §4.1 Spectral / operator-algebra theorems

Every theorem whose content is about spectra, operator algebras, KMS states, modular flow, ITPFI. Cite paper + §.

#### §4.2 Gauge / KK / curvature theorems

Every theorem about gauge bundles, KK reduction, curvature, gauge groups.

#### §4.3 Number-theoretic theorems

Every theorem about primes, zeta zeros, L-functions, arithmetic structure.

#### §4.4 Cosmological derivations

Every cosmological prediction with its derivation chain (not just the pin value).

#### §4.5 Quantum-mechanical derivations

Born rule, Bell inequality, spin-statistics, Aharonov-Bohm, superposition as extension, etc.

#### §4.6 Reduction / scheme-independence theorems

Paper 10 Thm U.2a, Paper 11 Thm K.4, etc.

#### §4.7 Structural / existence theorems

"There exists..." type theorems. Theorem 2.1 in ym-clay-bare, etc.

### §5 Lemmas

Every named lemma with citation. Lemma L.1.1 through L.4.3 from paper08, and their analogs in other papers.

### §6 Conjectures (Framework-internal)

CBB Conjectures 1-5 (from Paper 25), the bridge conjectures, Hilbert 12 CBB conjectures, etc.

### §7 External Conjectures Addressed

Each of the external conjectures the programme addresses with its:
- Classical statement
- Framework identification
- Current status in framework
- Confidence score if available

RH, YM, BSD, PvNP, Hodge, NS, Goldbach, Twin Primes, Schanuel, Collatz, Lehmer, Cramér, Sato-Tate, Lindelöf, Katz-Sarnak, Selberg 1/4, QUE, BGS (Montgomery), ABC, OPN, Hilbert 6, Hilbert 12, Baum-Connes, Turbulence K41, VP vs VNP.

### §8 Experimental Predictions — the 36 pins

Exhaustive table. One row per pin. Columns: # / Observable / Formula / Predicted / Measured / Deviation / Source / Status.

Plus any extension pins (ext-1, ext-2 from YM beyond-bare; short-range gravity; etc.).

### §9 Derivations / Closed-form expressions

Every named closed-form derivation. Examples:
- $\Lambda_\text{CC} = \exp(\gamma_1 \pi^2/2)$ (cosmological constant)
- $\lambda_\text{Cabibbo} = 56/(57\sqrt{19})$
- $A_\text{Wolfenstein} = 47/57$
- $\bar\rho = 1/(2\pi)$, $\bar\eta = \sqrt{19}/(4\pi)$
- $\alpha_\text{PS}^{-1} = 17$
- $Q_\text{Koide} = 2/3$
- $t_0 = (\log\gamma_7)^2$ Gyr
- $m_t = \gamma_3 \gamma_8/(2\pi)$
- $N_\text{eff} = \gamma_6^{1/3}$
- $H_0 = \gamma_{11} \cdot 4/\pi$
- $n_s = \gamma_9/\gamma_{10}$
- $\Omega_{DM}/\Omega_b = 1/\xi^2$
- $\xi = \gamma_1/\gamma_5$
- ... all 36 pins' closed forms + any structural derived constants

### §10 Named walls / conditionals

Every named hypothesis, conditional, or open wall with full disclosure:
- H4 (YM Link 18)
- CCM 2025 dependency (RH Layer 1)
- L.3.7 (H4 bypass audit)
- Schanuel conditional (where used)
- CBB axiom dependencies
- Any other named hypothesis

For each: name, statement, where used, bypass if any, re-entry gate.

### §11 Kills (dead routes, append-only)

Every killed attack path with:
- Kill ID (K-N)
- Pattern (what was tried)
- Why it failed
- Re-entry gate (condition under which this route could be reconsidered)

Include: K-3 (IR renormalon kill in H4 Borel summability), OPN Route 6a kill, etc.

### §12 Programme Structure

#### §12.1 The 10 faces of the e-circle

Full table. Name / question / canonical conjecture / geometric-or-spectral side / confidence.

#### §12.2 The 6 projections of the 5D geometry

Full table. Projection operator / domain / range / preserved invariants / lost invariants.

#### §12.3 The 5 inner-ring branches

Branch A through E. What's in each, item count, confidence.

#### §12.4 The 25 ring vertices

Full table. Position / name / paper / compound projection / primary face / confidence / status.

### §13 Methodology (PAC / ORA / Patterns)

#### §13.1 Six Patterns (ORA v8)

P1-P5 + P6 if named. Description + canonical use.

#### §13.2 PCA primitives

VERIFY / CONSTRUCT / BYPASS / DUAL-CHECK / REFRAME / TRANSPOSE / EXCISE + mode-specific (INOCULATE if DELTA 11 is adopted).

#### §13.3 ORA bundles

Bundle names, purposes, active runs: decomposition, ccm-verification, x-ray, ym, inner-rings, audit.

#### §13.4 Triad roles (Author / Critic / Arbiter)

Definition of each role, dispatch patterns, decision discipline.

### §14 Numerical Constants

Every fixed number used in the programme. Constant / symbol / value / source.

- $R \approx 10.10\,\mu\text{m}$ (e-circle radius)
- First 15 Riemann zeros $\gamma_1, \ldots, \gamma_{15}$ (with values)
- $\kappa = 2/\pi^2$ (CBB normalization)
- Mertens constant $e^{-\gamma}$
- Granville constant $2e^{-\gamma}$
- $C_N = 2(N^2-1)/\pi^6$ (OPE coefficient)
- $\xi = \gamma_1/\gamma_5 \approx 0.4292$
- 1729 = 7 × 13 × 19 (minimal bridge conductor)
- $\delta_0$ (lattice-scale cluster gap)
- $b_0(G)$ for each G (one-loop AF coefficients)
- $h^\vee(G)$ (dual Coxeter numbers)
- ... every numerical constant referenced

### §15 Named Structural Identities

Every named identity / equivalence / correspondence:
- Mertens product as ITPFI Araki-Woods invariant
- $e$-conservation ↔ Bell $|S| = 2\sqrt{2}$
- Frobenius angle = Hecke eigenvalue
- Euler product ↔ ITPFI factorization
- KMS$_1$ democracy ↔ Sato-Tate equidistribution
- Weitzenböck formula on $\mathbb{CP}^{N-1}$ → mass gap
- Tomita-Takesaki modular flow = thermal time
- M_int = J·M_ext·J (BH interior)
- ...

### §16 Capacitor cells (24-domain correspondence table)

Every filled cell in `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`. Row / domain pair / content / status.

### §17 Programme-graph edges / cross-cuts

Every cross-cut edge between vertices on the ring, with shared invariant.
- YM ↔ qg5d, pvnp, rh, ns, cramer, hodge, baum-connes (38 edges from YM x-ray)
- Other vertex x-rays if they exist
- Inter-paper programme-graph edges from each PROOF-CHAIN.md "Programme graph edges" section

### §18 Literature anchors

Every external theorem the programme cites. Author / year / result / where used. (Bost-Connes 1995, Osterwalder-Schrader 1973/75, Balaban CMP 95-119, Wiles 1995, Taylor et al. 2011 Sato-Tate, Lindenstrauss 2006 QUE, Hardy Z PCC arXiv:2511.18275 Nov 2025, CCM 2025 arXiv:2511.22755, Mori 2024 Cuntz Collatz, Connes-Marcolli 2008 GL₂, Gaitsgory-Raskin 2024 Geometric Langlands, etc.)

### §19 Naming register

Every named object introduced by the programme:
- "CBB system" (Critical Bost-Connes-Brauer)
- "Six (τ_S)" — absolute time scale
- "The LOCK" — 37 R-Theorems
- "The Six Patterns" — method
- "The e-circle" — fifth dimension
- "The bridge family" — cyclotomic Brauer cocycles
- "The ellipse" — ring's confidence diagnostic
- "Herald" — this document
- Any other named structures

### §20 Dead ends / kept-for-history

Things that were tried and abandoned but documented:
- String theory "byeeeee" (Paper 20)
- Conjecture 5 retraction (Paper 25 T7 Stark regulator equality)
- Early OPN route 6a
- ...

---

## Completeness discipline

1. **Miss nothing.** If a paper has 18 links, all 18 appear. If the pin table has 36 rows, all 36 appear. If the capacitor has 130 filled cells, all 130 appear.

2. **Atomic entries.** Each fact gets one entry with a unique ID. Format suggestion:
   - `POSTULATE-P1`, `POSTULATE-P2`, ...
   - `AXIOM-CBB-I`, `AXIOM-CBB-II`, ...
   - `THM-YM-L1`, `THM-YM-L14`, `THM-RH-LAYER-3`, ...
   - `LEMMA-L.1.1`, `LEMMA-L.3.7`, ...
   - `CONJ-CBB-1`, `CONJ-CBB-5-RETRACTED`, ...
   - `PIN-1`, `PIN-36`, `PIN-EXT-1`, ...
   - `DERIV-LAMBDA-CC`, `DERIV-CABIBBO`, ...
   - `WALL-H4`, `WALL-CCM-2025`, ...
   - `KILL-K-3`, `KILL-OPN-6A`, ...
   - `FACE-TOPOLOGY`, `FACE-CURVATURE`, ...
   - `PROJ-PA`, `PROJ-PD`, ...
   - `VERTEX-1-QG5D`, `VERTEX-2-RH`, ...
   - `PATTERN-P1`, ...
   - `PRIMITIVE-VERIFY`, `PRIMITIVE-INOCULATE`, ...
   - `BRANCH-A`, `BRANCH-D`, ...
   - `CONST-R-ECIRCLE`, `CONST-GAMMA-1`, `CONST-XI`, ...
   - `IDENTITY-MERTENS-ITPFI`, `IDENTITY-BELL-CIRELSON`, ...
   - `CAPACITOR-SPEC-QFT`, `CAPACITOR-NCG-ANT`, ...
   - `EDGE-YM-RH-L14-L16`, ...
   - `LIT-OS-1973`, `LIT-BALABAN-109`, ...
   - `NAMED-CBB-SYSTEM`, `NAMED-SIX-TIME`, ...

3. **Every entry cites.** Source paper + §-level reference mandatory. Example: `(paper08 §04 Theorem 4)`, `(paper12 §27 CBB Axiom I)`, `(paper60 §13)`.

4. **Status honest.** Use exactly one of: PROVED / LITERATURE / CLASSICAL / QG5D / TRANSPOSITION / PROVED-WITH-CAVEAT / CONDITIONAL / PARTIAL / CANDIDATE / CONJECTURED / OPEN / OPEN-BUT-ADDRESSED / KILLED / SPECULATIVE / RETRACTED.

5. **Dependencies.** Where a fact depends on another, include a cross-reference by ID. `THM-YM-L14 depends on: THM-YM-L1b, THM-YM-L13`.

6. **Append-only discipline.** If an entry already exists (future re-runs), update status, don't delete. Add change-log entry at the bottom of the entry.

7. **No paraphrase of official content.** Verbatim for postulates, axioms, theorem statements. Paraphrase is allowed for interpretation notes but marked as such.

---

## Format rules

1. Heading hierarchy: `#` for §0-§20, `##` for subsections, `###` for sub-subsections.

2. Tables preferred for lists of similar entries (pins, constants, zeros, etc.). Prose only for unique structural notes.

3. Each entry starts with its ID in backticks: `THM-YM-L1` — KK Spectral Gap.

4. Citations in parentheses at end of statement.

5. Status in bold in capitals: **PROVED**, **CONDITIONAL**, **OPEN**.

6. Mathematical expressions in LaTeX using `$...$` for inline, `$$...$$` for display.

7. Use ASCII diagrams where structural relationships are easier to show visually (proof chains, ring diagram, face octagon, etc.).

---

## Success criteria

- All ~25 PROOF-CHAIN.md files scanned; every link/layer/sub-layer in `herald.md`.
- All 36 pins in §8 with full data (formula, predicted, measured, deviation).
- All 10 e-circle faces in §12.1.
- All 6 projections in §12.2.
- All 5 inner-ring branches in §12.3.
- All 25 ring vertices in §12.4.
- All 5 ORA patterns in §13.1.
- All capacitor cells enumerated in §16.
- All named walls from `strategy/the-weakest-links.md` in §10.
- Every kill from kill-lists in §11.
- First 15 Riemann zeros with values in §14.
- Literature anchors in §18 cover all external results cited in framework papers.
- Herald length: expected ~1500-3000 lines. If under 1000, coverage is incomplete.

---

## Operational plan

Estimated budget: 90-150 minutes. Work in parallel where possible (multiple file reads in parallel, but careful to avoid context overflow).

Phase 1 (10 min): read the structural foundation — Paper 1, Paper 12 anchor, Paper 60 TOC, Paper 61 TOC, strategy/the-ring.md, strategy/the-weakest-links.md.

Phase 2 (40 min): scan all PROOF-CHAIN.md files; extract every link with status + citation.

Phase 3 (20 min): extract the 36-pin master table, the first 15 Riemann zeros, all named closed forms.

Phase 4 (20 min): extract methodology — patterns, primitives, bundles, capacitor cells, programme-graph edges.

Phase 5 (15 min): extract kills, named walls, kept-for-history items from strategy/ and programme documents.

Phase 6 (15 min): assemble `herald.md` with the §0-§20 structure.

Phase 7 (10 min): self-audit — does each category have at least one entry? Is the length ≥ 1500 lines? Are all IDs unique? Are all cites §-level?

---

## Deliverable

`/Users/gsix/quantum-geometry-in-5d-latex/audit/herald/herald.md`

Expected scale: 1500-3000 lines, ~300-500 atomic fact entries, 20 top-level categories.

Append-only. Future runs update entries (change-log at bottom of each entry) rather than overwriting.

This is the programme's single reference document. When anyone asks "what does the programme know?", the answer is: read herald.md.

---

*Miss nothing. Append-only. Citation-backed. Honest status codes.*

*G Six and Claude Opus 4.6. April 14, 2026.*
