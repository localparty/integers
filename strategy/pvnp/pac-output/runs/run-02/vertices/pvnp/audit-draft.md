# PvNP Audit Draft — Author's first-pass verdicts

*Run-02 vertex artifact. 28 rows × 6 columns = 168 cells. Author-pass only (pre-critic, pre-arbiter).*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Method

For each (step, requirement) cell, the author assigned a verdict (P / Pa / O / S) plus a one-line citation. Verdicts align with the priors in `../../blackboard.md`:

- Req 1 (TM) and Req 2 (P/NP defs) are CENTRALIZED at Steps 16-20 via BZ backward/forward. Most chain layers construct operator-algebraic objects without directly touching TM-formal quantification — those cells get S (→ADR-1/2).
- Req 3 (3-SAT) is CENTRALIZED at Steps 17-20 + 23. Part (i) / Part (ii) construct the factor M_Bool^L for a generic CSP instance, not specifically for 3-SAT — upstream cells S (→ADR-3).
- Req 4 (non-relativization) is PERVASIVE Pa because Step 5's ω_1 dependence and the operator-algebraic construction are oracle-independent by nature. CENTRAL P at Step 22 (Houdayer-Marrakchi dichotomy).
- Req 5 (non-naturalness) is PERVASIVE Pa through factor-theoretic cells + non-amenability arguments. CENTRAL P at Steps 15 (Mar18 fullness) and 22 (HM dichotomy).
- Req 6 (non-algebrization) is DISTRIBUTED Pa across Steps 1, 2, 3, 5, 11, 18, 20, 22 — no single P cell; programme-level §6.3 is the addressing.

## Per-row verdict table (author draft, pre-critic)

See `../../compliance-map.md` §1 for the full author-arbiter table. This file records the author-draft versions for provenance.

| Step | Author-draft Req 1 | Req 2 | Req 3 | Req 4 | Req 5 | Req 6 |
|------|-------|-------|-------|-------|-------|-------|
| 1    | S | S | S | S | S | Pa |
| 2    | S | S | S | S | Pa | Pa |
| 3    | S | S | S | S | Pa | Pa |
| 4    | S | S | S | Pa | Pa | Pa |
| 5    | S | S | S | Pa | Pa | Pa |
| 6    | S | S | S | Pa | S | S |
| 7    | S | S | S | Pa | S | S |
| 8    | S | S | S | Pa | S | S |
| 9a   | S | S | S | S | Pa | S |
| 9b   | S | S | S | S | Pa | S |
| 9c   | S | S | S | S | Pa | S |
| 9*   | S | S | S | S | Pa | S |
| 10   | S | S | S | Pa | Pa | S |
| 11   | S | S | S | Pa | S | Pa |
| 12   | S | S | S | Pa | S | S |
| 13   | S | S | S | Pa | S | S |
| 13b  | S | S | S | Pa | S | S |
| 14   | S | S | S | Pa | Pa | S |
| 15   | S | S | S | Pa | P | S |
| CP-1 | S | S | S | Pa | Pa | S |
| 16   | Pa | Pa | Pa | S | S | S |
| 17   | Pa | P | P | S | S | S |
| 18   | P | P | P | Pa | S | Pa |
| 19   | S | S | Pa | Pa | Pa | S |
| 20   | S | P | P | Pa | S | Pa |
| 21   | S | S | Pa | Pa | Pa | S |
| 22   | S | S | Pa | P | P | Pa |
| 23   | Pa | Pa | P | Pa | Pa | Pa |

## Citations (one-liner per non-SILENT cell; full cites in compliance-map.md)

- **Step 1 Req 6**: Post's lattice is finite-algebra above oracle poly extensions; BBBKZ 2024 / AW08
- **Step 2 Req 5**: UA1 exponential clone growth is cohomological, non-density; p28§2 Thm UA1
- **Step 2 Req 6**: Clone growth encodes Schur multiplier structure; p28§6.3
- **Step 3 Req 5**: UA2 linear bound is combinatorial non-natural witness
- **Step 3 Req 6**: Post's lattice above poly extensions; p28§2 Thm UA2
- **Step 4 Req 4**: Thompson's V non-amenability + Connes 1976, oracle-independent; p28 Node 1.3.1
- **Step 4 Req 5**: Non-amenability of G_Bool is not RR97-large
- **Step 4 Req 6**: Thompson's V + cyclotomic field structure above poly extensions
- **Step 5 Req 4**: KMS_1 on ω_1 critical state, oracle-independent; p28§3.4.3 — **W2 disclosure (existence PROVED, uniqueness CONDITIONAL)**
- **Step 5 Req 5**: Type III_1 factor class is not "large"; multiplicative independence log 2, log 3
- **Step 5 Req 6**: Multiplicative independence of logs is Baker-style above poly extensions
- **Step 6-8 Req 4**: Oracle-independent ingredients (polar decomposition, Sol preservation, pigeonhole on U(d))
- **Step 9a-9c Req 5**: Instance-specific coordinate-frequency / Berry-Esseen / V_XOR rank-1 structure, non-large
- **Step 9* Req 5**: Lemma A* monotone restriction is non-natural correction
- **Step 10 Req 4**: Marrakchi criterion Inn not closed, oracle-independent
- **Step 10 Req 5**: Fullness/non-fullness intrinsic factor property; p28§6.2; HM
- **Step 11 Req 4**: Non-amenable G_L from Toffoli F_2 (CSP-structural, oracle-independent)
- **Step 11 Req 6**: Toffoli gate universality above poly extensions
- **Step 12 Req 4**: Trivial radical via Furstenberg + C*-simplicity + Jordan
- **Step 13 Req 4**: Essential freeness via modular invariant + stabilizer + Bernoulli
- **Step 13b Req 4**: Feldman-Moore factoriality
- **Step 14 Req 4**: Jones-Schmidt 1987
- **Step 14 Req 5**: Strong ergodicity not a large-set property
- **Step 15 Req 4**: Marrakchi 2018 Theorem B
- **Step 15 Req 5**: Fullness from strong ergodicity = CORE ADR-5 discharge (P)
- **CP-1 Req 4**: Laca-Raeburn dilation + Feldman-Moore, 6-Critic verified
- **CP-1 Req 5**: Groupoid identification, non-large
- **Step 16 Req 1**: P = NP hypothesis uses Cook-formal classes
- **Step 16 Req 2**: Hypothesis references Cook Def.~1-~4
- **Step 16 Req 3**: Universal over NP reducing to 3-SAT
- **Step 17 Req 1**: 3-SAT ∈ P uses poly-time TM
- **Step 17 Req 2**: Cook 1971 NP-completeness of 3-SAT (P)
- **Step 17 Req 3**: 3-SAT as NP-complete target (P)
- **Step 18 Req 1**: **BZ backward consumes Req 1 TM hypothesis + Cook §1 TM model (P)** — THE TRANSLATION POINT
- **Step 18 Req 2**: **BZ backward consumes P definition per Cook (P)** — TRANSLATION LAYER CELL
- **Step 18 Req 3**: Applied to L_{3-SAT} producing Taylor polymorphism (P)
- **Step 18 Req 4**: BZ backward CSP-theoretic, not oracle-diagonalization
- **Step 18 Req 6**: BZ universal-algebraic above poly extensions per AW08
- **Step 19 Req 3**: Applied to M_Bool^{3-SAT} via Path B
- **Step 19 Req 4**: Part (i) UNCONDITIONAL; ω_1-dependent Step 5
- **Step 19 Req 5**: Non-fullness via Path B; ADR-5 load-bearing
- **Step 20 Req 2**: **BZ forward consumes NP-hardness (P)** — second translation point
- **Step 20 Req 3**: **3-SAT non-Taylor = NP-complete (P)**
- **Step 20 Req 4**: BZ forward oracle-independent
- **Step 20 Req 6**: BZ above poly extensions per AW08
- **Step 21 Req 3**: Applied to M_Bool^{3-SAT} via Route C
- **Step 21 Req 4**: Part (ii) Route C via CP-1
- **Step 21 Req 5**: Fullness via Route C; ADR-5
- **Step 22 Req 3**: 3-SAT factor both full AND non-full
- **Step 22 Req 4**: **Houdayer-Marrakchi dichotomy factor-theoretic, oracle-independent (P)**
- **Step 22 Req 5**: **Fullness dichotomy for type III_1 factor = central ADR-5 (P)**
- **Step 22 Req 6**: Factor dichotomy sits above poly extensions
- **Step 23 Req 1**: QED yields 3-SAT ∉ P in Cook-formal TM sense via Step 18 contrapositive
- **Step 23 Req 2**: QED yields P ≠ NP in Cook Def.~1-~4 sense
- **Step 23 Req 3**: **3-SAT as specific NP-complete target separator (P)**
- **Step 23 Req 4-6**: Inherit ADR-4/5/6 via Steps 5, 10, 15, 22, 2, 18, 20

---

*End of audit-draft.md. Critic-pass now in critic-attacks.md; arbiter resolutions in arbiter-decisions.md.*
