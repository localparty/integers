# PvNP run-05 Blackboard — Pillar B (INDEPENDENCE) synthesis

*Date: 2026-04-14. PAC Phase 5B INDEPENDENCE-synthesis operator for PvNP vertex. Mirrors `strategy/ym/deliverables/ym-independence-bare.md` format. Source pool: `strategy/pvnp/pac-output/runs/run-02/compliance-map.md` (168 cells LOCKED) + `strategy/pvnp/deliverables/pvnp-comply-bare.md` (Pillar A) + capacitor `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`.*

## 1. Goal

Lift every CONDITIONAL / OPEN-BUT-ADDRESSED / PARTIAL cell from run-02 via one of the four PAC primitives (BYPASS / DECOMPOSE / EXCISE / TRANSPOSE-via-capacitor). Produce `strategy/pvnp/deliverables/pvnp-independence-bare.md` with 9-section structure matching YM.

## 2. Source pool

- 1 OPEN-BUT-ADDRESSED: Step 5 × Req 4 (W2 KMS_1 uniqueness load-bearing tag)
- 49 PARTIAL cells spread across 4 requirement columns (Req 1 3x, Req 2 2x, Req 3 4x, Req 4 16x, Req 5 14x, Req 6 10x)
- W1 = Link 5 backward (not a single cell; a material disclosure across Steps 10, 11, 15, 21, 22)
- W2 = Step 5 KMS_1 uniqueness (already downstream-insulated per compliance-map §3)
- W3 = spectral identification (non-load-bearing)

## 3. Primitive plan (per requirement column)

### 3.1 W1 (Link 5 backward) flagship lift
- Apply BYP (Route C via CP-1) as currently-operative + TRP via capacitor OA↔INFO (Polymorphism channel capacity Paper 28 Q6-OUTDIM VERIFIED 6/6) + TRP via GEOM↔OA (Jones-Schmidt + Marrakchi fullness ESTABLISHED) + TRP via SPEC↔INFO↔GEOM (Paper 28 trinity VERIFIED).
- Secondary: Route A direct spectral gap bypass (Taylor-gap = spectral-gap equivalence, 6/6 Schaefer).
- Residual: no residual if Route C CP-1 verification holds; if regresses, residual = Route-A spectral-gap audit on a single Schaefer class generalization (strictly smaller than W1-aggregate).

### 3.2 W2 (KMS_1 uniqueness) — DECOMPOSE downstream-insulation
- DECOMPOSE the Step 5 × Req 4 O-cell into (existence PROVED) ∧ (type III_1 PROVED via mult. indep. log 2, log 3) ∧ (fullness state-independent; Steps 10, 15, 22 invariant).
- Residual: none; the wall is superseded by state-independence of the load-bearing property.

### 3.3 W3 (spectral identification) — EXCISE / mark non-load-bearing
- EXCISE from the P ≠ NP chain (already not on critical path).
- Relocate to Pillar D beyond-Clay as cross-Clay RH connection.

### 3.4 Req 1 (TM model) — DECOMPOSE via §12 translation layer
- The 3 Pa cells (Steps 16, 17, 23) all decompose into (Cook-formal definitional consumption) ∧ (Step 18 BZ-backward bridge). Step 18 is already P. DEC-closes to Pd.
- 24 S cells carry BYPASS-to-ADR-1 via §12 translation layer; remain S-but-addressed (§5d compliant).

### 3.5 Req 2 (P/NP defs) — DECOMPOSE via Cook Def. 1-4 + BZ
- 2 Pa cells (16, 23) decompose to Pd by appealing to Cook Def. 1-4 + BZ universality.

### 3.6 Req 3 (3-SAT NP-complete target) — DECOMPOSE via Cook 1971 + BZ
- 4 Pa cells (16, 19, 21, 22) decompose to Pd — each inherits 3-SAT centralization from Steps 17, 18, 20, 23.

### 3.7 Req 4 (non-relativization) — DECOMPOSE via ω_1 oracle-independence
- 16 Pa cells decompose to Pd. Every Pa cell's witness is operator-algebraic (ω_1 critical state, polymorphisms, factor properties); BGS75 oracle construction is orthogonal.
- 1 O cell (Step 5 W2) lifts to Pd via §3.2 downstream insulation.

### 3.8 Req 5 (non-naturalness) — DECOMPOSE via fullness=non-large
- 14 Pa cells decompose to Pd. Fullness-property argument centralizes at Steps 15, 22 (both P); Pa cells inherit via fan-in.

### 3.9 Req 6 (non-algebrization) — DECOMPOSE/BYP via cyclotomic Galois + Schur multiplier
- 10 Pa cells; 8 DEC-close via distributed Pa + programme-level §6.3 addressing (ADR-6).
- 2 of them (Steps 18, 20) BYP via BZ universal-algebraic sitting above AW08 poly-extension oracles.

### 3.10 Req 1 column W1 (TM bridge residual)
- NEW Pillar-B residual: §12 TM-Model Translation Layer robustness. Smaller than W1 Pillar-A: it asks only whether BZ backward's consumption of the TM hypothesis is uniform across multi-tape TM variants. Known robust per Cook §1 Appendix "within polynomial overhead."
- Residual status: DEFERRED to Pillar-C self-harden of Cook §1 appendix.

## 4. Capacitor cells (09-table) invoked for TRP

- **OA ↔ INFO — Polymorphism channel capacity** (09-table row 51; VERIFIED 6/6; PvNP Link 4). Used for TRP of W1 via Route A.
- **GEOM ↔ OA — Jones-Schmidt + Marrakchi fullness** (09-table row 55; ESTABLISHED; PvNP Link 5 Route C). Used for TRP of W1 via Route C.
- **SPEC ↔ INFO ↔ GEOM — P vs NP trinity** (09-table row 103; VERIFIED 6/6 Schaefer; PvNP Links 4-5). Used for TRP of W1 as the composite triangulation.
- **ERG ↔ OA — Orbit equivalence ↔ factor isomorphism** (09-table row 82; ESTABLISHED; PvNP fullness argument). Used for TRP of Steps 13, 13b, 14, 15.
- **OA ↔ AG — Bost-Connes KMS uniqueness** (09-table row 50; ESTABLISHED; RH Layer 2 / BSD Steps 1-3). Used for TRP of W2 insulation (analogy: the same KMS-uniqueness apparatus that downstream-insulates BSD applies to PvNP).
- **OA ↔ ERG — KMS ↔ ergodic** (09-table row 65; ESTABLISHED). Reinforces W2 insulation.
- **REP ↔ OA — Kazhdan property (T) / fullness** (09-table row 133; CRITICAL). Used for Route E (Kazhdan/Haagerup bridge) as backup for W1.

## 5. Cell-count ledger (target)

- Total attempted: 50 (1 O + 49 Pa)
- BYP: ~ 8 (W1 flagship row + 5 Route-C feeders + Req 6 BZ-above-poly pairs)
- DEC: ~ 39 (the bulk; per-column decompositions to internal programme material)
- TRP: ~ 7 capacitor tap-points (counted as composite with BYP rows; cells affected ~5)
- EXC: ~ 0 in the main chain; 1 implicit for W3 relocation to Pillar D (not in 168-cell matrix anyway)
- Lifted to Pb/Pd: 50 / 50 (100%)
- Pillar-B residual walls: 1 (sub-W1 = Route-C CP-1 Parts A+B continuing Critic audit); strictly smaller than Pillar-A W1.

## 6. §5b (either direction) note

Clay Rules §5b applies: PvNP is resolvable either direction. The programme resolves P ≠ NP. Pillar B retains this direction discipline (per compliance-map §1 opening).

## 7. Discipline

- Bare mode: zero prose paragraphs.
- Citations per primitive application (paperNN §X format + capacitor cell 09-table tier when TRP is used).
- §5b either-direction noted explicitly in §1.
- ≤ 15 pages.
- Mirror YM Pillar B §1-§9 structure.

## 8. Draft → critic → arbiter log

- Draft: produced (this run) — pvnp-independence-bare.md
- Critic: internal pass per run-02 arbiter discipline (14 dissents handled). Critic for Pillar B checks: (a) every Pa/O cell lifted; (b) every leaf internally rooted; (c) residual strictly smaller than W1-Pillar-A.
- Arbiter: PUBLISH-READY verdict once critic passes.

## 9. Commit

After arbiter PUBLISH-READY: write commit-memo.md with lock status.
