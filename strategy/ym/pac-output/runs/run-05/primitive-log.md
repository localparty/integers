# YM run-05 — Pillar B INDEPENDENCE primitive log

*Per-cell record of PAC primitive applications. Input: LOCKED 20×7 run-02 compliance-map (140 cells; 23 P / 43 Pa / 1 O / 73 S). Output: dep-free chain with one residual (L.3.7-audit).*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Cell-by-cell primitive application (44 attempts, 44 successes)

Primitive codes: **BYP** = BYPASS; **DEC** = DECOMPOSE; **EXC** = EXCISE; **TRP** = TRANSPOSE via capacitor cell.

### Group A — OPEN-BUT-ADDRESSED (H4 + fan-in)

| # | Cell | A-verdict | Primitive | Capacitor cell(s) | Route | B-verdict | Residual |
|---|------|-----------|-----------|-------------------|-------|-----------|----------|
| 1 | L18 × R5 | O | BYP + TRP | cap§GEOM↔QFT, cap§SPEC↔QFT, cap§QFT↔GEOM | Step 18' Balaban RG + gradient flow + Reisz + trace-anomaly + Callan-Symanzik | Pb | L.3.7-audit |
| 34 | L2 × R5 | Pa | BYP | (fan-in to Step 18') | Balaban g_k → 0 unconditional (paper11 K.4) | Pb | L.3.7-audit |
| 35 | L4 × R5 | Pa | BYP | (fan-in to Step 18') | Analyticity infrastructure p8L.3.1–L.3.9 | Pb | L.3.7-audit |
| 36 | L11 × R5 | Pa | BYP | (fan-in to Step 18') | g_k^4 AF power + Balaban g_k → 0 | Pb | L.3.7-audit |
| 37 | L12 × R5 | Pa | BYP | (fan-in to Step 18') | AF running through RG recursion | Pb | L.3.7-audit |
| 38 | L13 × R5 | Pa | BYP | (fan-in to Step 18') | Sum of AF-running g_k^4 terms | Pb | L.3.7-audit |
| 39 | L15 × R5 | Pa | BYP | (fan-in to Step 18') | Small-flow-time expansion L.3.1 | Pb | L.3.7-audit |
| 42a | L18 × R6 (AF-form component) | Pa | BYP | (fan-in to Step 18') | AF-log OPE form via Step 18' | Pb | L.3.7-audit |

Group-A subtotal: **8 cells**, all BYP (with TRP-subcomponents on the flagship), all sharing single residual L.3.7-audit.

### Group B — Group-generality PARTIALs (Req 1 DECOMPOSE lifts)

All lifts: SU(N)-explicit PROVED ∧ p8K.9 Summary Table (Balaban general G) ∧ p8I4.1 Theorem I.4.1 (universal mass gap). Pure DEC — no external.

| # | Cell | A-verdict | Primitive | Route | B-verdict |
|---|------|-----------|-----------|-------|-----------|
| 2  | L1  × R1 | Pa | DEC | p8§04 T4 ∧ p8I4.1 ∧ p8K.9 | Pd |
| 3  | L1b × R1 | Pa | DEC | p8§04 T5 ∧ p8I4.1 | Pd |
| 4  | L8  × R1 | Pa | DEC | p8§04 structural ∧ p8I.3 ∧ K.9 | Pd |
| 5  | L9  × R1 | Pa | DEC | dim-6 classification ∧ K.9 | Pd |
| 6  | L10 × R1 | Pa | DEC | non-pert extension ∧ K.9 | Pd |
| 7  | L10b × R1 | Pa | DEC | spectral lemma ∧ K.9 | Pd |
| 8  | L11 × R1 | Pa | DEC | form-factor ∧ K.9 | Pd |
| 9  | L12 × R1 | Pa | DEC | recursion coeffs ∧ K.9 | Pd |
| 10 | L13 × R1 | Pa | DEC | convergence ∧ K.9 | Pd |
| 11 | L15 × R1 | Pa | DEC | L.1.1 SU(N) ∧ p8I4 | Pd |
| 12 | L16 × R1 | Pa | DEC | OS reconstr SU(N) ∧ K.9 + I4.1 | Pd |
| 13 | L17 × R1 | Pa | DEC | Suzuki structural ∧ I4 | Pd |
| 14 | L18 × R1 | Pa | DEC | K.6 b_0(G) > 0 ∀G | Pd |

Group-B subtotal: **13 cells DEC**.

### Group C — Infinite-volume PARTIALs (Req 2 DECOMPOSE lifts)

All lifts: V-indep ingredient PROVED ∧ p8R§51 IV (Moore-Osgood interchange) ∧ §51 III (continuum) + §51 V (OS in continuum). Pure DEC.

| # | Cell | A-verdict | Primitive | Route | B-verdict |
|---|------|-----------|-----------|-------|-----------|
| 15 | L2  × R2 | Pa | DEC | V-indep κ ∧ §51 IV | Pd |
| 16 | L3  × R2 | Pa | DEC | V-indep ∧ §51 IV | Pd |
| 17 | L4  × R2 | Pa | DEC | V-indep analyticity ∧ §51 IV | Pd |
| 18 | L10 × R2 | Pa | DEC | V-indep Balaban ∧ §51 IV | Pd |
| 19 | L10b × R2 | Pa | DEC | V-indep constant ∧ §51 IV | Pd |
| 20 | L11 × R2 | Pa | DEC | §51 II.2 ∧ §51 IV | Pd |
| 21 | L12 × R2 | Pa | DEC | §51 II.2 ∧ §51 IV | Pd |
| 22 | L13 × R2 | Pa | DEC | §51 II.2 ∧ §51 IV | Pd |
| 23 | L18 × R2 | Pa | DEC | Inherits from L16/L17 | Pd |

Group-C subtotal: **9 cells DEC**.

### Group D — Uniform-V gap PARTIALs (Req 3 DECOMPOSE lifts)

All lifts: ingredient PROVED ∧ p8R§51 II.2 inductive bootstrap (already PROVED at L14). Pure DEC.

| # | Cell | A-verdict | Primitive | Route | B-verdict |
|---|------|-----------|-----------|-------|-----------|
| 24 | L1  × R3 | Pa | DEC | μ_1 ≥ 2N/r_3^2 (p60§13) ∧ transfer at L1b | Pd |
| 25 | L2  × R3 | Pa | DEC | UV stability ∧ §51 II.2 | Pd |
| 26 | L3  × R3 | Pa | DEC | k-indep κ ∧ §51 II.2 | Pd |
| 27 | L4  × R3 | Pa | DEC | analyticity ∧ §51 II.2 | Pd |
| 28 | L8  × R3 | Pa | DEC | dim-6 suppression ∧ §51 II.2 | Pd |
| 29 | L9  × R3 | Pa | DEC | uniform dev ∧ §51 II.2 | Pd |
| 30 | L15 × R3 | Pa | DEC | L.1.1(v) action decrease | Pd |
| 31 | L17 × R3 | Pa | DEC | renormalized ops inherit from L14 | Pd |

Group-D subtotal: **8 cells DEC**.

### Group E — OS/Wightman PARTIALs (Req 4 DECOMPOSE lifts)

| # | Cell | A-verdict | Primitive | Route | B-verdict |
|---|------|-----------|-----------|-------|-----------|
| 32 | L15 × R4 | Pa | DEC | L.2.1–L.2.4 feeding L16 OS | Pd |
| 33 | L18 × R4 | Pa | DEC | OS-reconstructed at L16 + AF content at L18 | Pd |

Group-E subtotal: **2 cells DEC**.

### Group F — Stress+OPE PARTIALs (Req 6 DEC + partial BYP)

| # | Cell | A-verdict | Primitive | Route | B-verdict |
|---|------|-----------|-----------|-------|-----------|
| 40 | L15 × R6 | Pa | DEC | p8L.1.1 + L.4.1 Suzuki enabler | Pd |
| 41 | L16 × R6 | Pa | DEC | L16 axioms enable L17 | Pd |
| 42b | L18 × R6 (power-law component) | Pa | DEC | L.4.3 unconditional power-law | Pd |

Group-F subtotal: **3 cells DEC** (power-law; AF-form component counted in Group A as cell 42a).

### Group G — Non-triviality PARTIALs (Req 7 DECOMPOSE lifts)

| # | Cell | A-verdict | Primitive | Route | B-verdict |
|---|------|-----------|-----------|-------|-----------|
| 43 | L16 × R7 | Pa | DEC | Sig (i) σ > 0 ∧ OS at L16 | Pd |
| 44 | L17 × R7 | Pa | DEC | Sig (ii) non-Gaussian connected + L17 | Pd |

Group-G subtotal: **2 cells DEC**.

---

## Totals

| Primitive | Count |
|-----------|------:|
| BYP | 8 (Group A: 7 BYP + 1 BYP-subcomponent of L18×R6) |
| DEC | 37 (13 + 9 + 8 + 2 + 3 + 2) |
| TRP | 3 capacitor cells tapped (sub-components of Group A cell 1) |
| EXC | 0 |
| **Cells attempted** | 44 |
| **Cells lifted** | 44 |
| **Success rate** | 100 % |

## Notes on cell-count arithmetic

Cell 42 is counted once as a Pillar-A PARTIAL but lifts to two independent components:
- 42a (AF-form logarithmic piece) → BYP, residual L.3.7
- 42b (power-law piece) → DEC, unconditional via L.4.3

Hence "44 cells" reflects the 44 distinct (cell, component) pairs lifted; the original run-02 matrix lists 43 Pa + 1 O = 44 cells needing attention. Every one has an applied primitive.

## Residual

Single residual after all 44 lifts: **W_1^B = L.3.7-audit** (paper08 Appendix L §L.3 Lemma L.3.7). Strictly smaller than Pillar-A H4. Shared across the 8 Group-A cells (row 1 + rows 34–39 + cell 42a). Queued to `strategy/externals-hardening/paper08-L3.7/` in the Pillar-C worklist.

---

*End of primitive-log.md.*
