# PAC run-02 Blackboard (BSD Compliance Audit — Output A only)

*Date: 2026-04-14. Operator: PAC (Claude Opus 4.6 / G Six). Mode: compliance-audit, Output A ONLY (B_bare and C_bare DEFERRED to future run). Idempotent re-fire under universal-approval-run.md Phase 4.*

---

## Scope

- Build the 11-layer × 7 Wiles-stated requirement = **77-cell compliance map** for BSD.
- Produce author/critic/arbiter artifacts per layer, no SILENT cells at end.
- Disclose four NAMED WALLS (W_rank, W_nonCM, W_hK, W_Sha) per brief DELTA 10.
- Carry over the two BROKEN items from Paper 26 adversarial run-01 (conditionality framing + curve 32.a3 c_2 typo).
- DO NOT write B_bare or C_bare this run.

## Inputs consulted (mandatory)

1. strategy/bsd/00-millenium-strategy.md — §§1-12 the 4 Clay gates + 7 Wiles requirements + 4 named walls + output architecture
2. strategy/bsd/bsd-millenium-brief.md — DELTA 4 compliance-map format, DELTA 10 wall discipline, DELTA 11 run-01 carry-overs
3. solutions-with-prize/paper26-bsd/PROOF-CHAIN.md — 11/11 steps closed, confidence 9/10, Pin #6 J_CKM audit note included
4. solutions-with-prize/paper26-bsd/nodes/K-bsd-theorem.md — Theorem 13.1 statement; 32.a3 c_2 = 4 LMFDB already corrected in nodes; scope limits documented
5. solutions-with-prize/paper26-bsd/01-adversarial-proof-review.md — 15 attacks (8 SURVIVED / 5 WEAKENED / 2 BROKEN), carry-over list
6. strategy/ym/pac-output/runs/run-02/compliance-map.md — worked example; the YM pilot pattern
7. strategy/_research/birch-swinnerton-dyer/landscape.md — Bhargava/Skinner/Zhang/Rubin/Kolyvagin/GZ acknowledgments inventory
8. strategy/_research/birch-swinnerton-dyer/outlet.md — **ABSENT** (flag for Phase 2 research refresh; not blocking this audit because Wiles Clay PDF summary is already in the strategy doc §1)

## The 7 Wiles-stated requirements (columns)

| # | Short name | Wiles citation |
|---|---|---|
| 1 | Rank equality r = rank(C(Q)) = ord_{s=1} L(C,s) | Wiles p. 2 main conjecture |
| 2 | Leading coefficient c ≠ 0 | Wiles p. 2 Taylor expansion |
| 3 | L-function continuation + FE | Wiles p. 2 + refs [24],[25],[1] (BCDT 2001) |
| 4 | Strong form BSD formula (c* formula) | Wiles Remark 1, p. 2 |
| 5 | Ш_C finite (or integrality) | Wiles Remark 1, 4 |
| 6 | Any elliptic curve C/Q | Wiles Remark 2 |
| 7 | Any rank r ≥ 0 | Wiles p. 4 Theorem (m ∈ {0,1} currently; m ≥ 2 open) |

## The 11 layers (rows)

Straight from solutions-with-prize/paper26-bsd/PROOF-CHAIN.md (also mirrored as paper26 nodes A-K):

| Row | PROOF-CHAIN link | Node label | Statement |
|-----|------|------|---|
| L1  | Step 1  | A | BC algebra over K, unique KMS_1 state (h_K=1) |
| L2  | Step 2  | B | Bridge family over K (355 triples, k∈{2,3,4,6}) |
| L3  | Step 3  | C | ITPFI factorization ω_1^K = ⊗_p ω_1^p |
| L4  | Step 4  | D | Dark-state impossibility (algebraic projector) |
| L5  | Step 5  | E | Cocycle shift formula Δc(δ); Key Lemma C (5b); Key Lemma C' (5c) |
| L6  | Step 6  | F | Baker's theorem forces δ=0 (non-load-bearing) |
| L7  | Step 7  | G | GRH for ζ_K and L(s,ψ): zeros on Re(s)=1/2 |
| L8  | Step 8  | H | CM factorization L(E,s) = L(s,ψ)·L(s,ψ̄) [LITERATURE Deuring 1953] |
| L9  | Step 9  | I | Kolyvagin rank 0: L(E,1)≠0 ⇒ rank=0, |Sha|<∞ [LITERATURE Kolyvagin 1990] |
| L10 | Step 10 | J | Gross-Zagier rank 1: L'(E,1)≠0 ⇒ rank=1 (vacuous in scope) [LITERATURE GZ 1986] |
| L11 | Step 11 | K | BSD Theorem 13.1: rank equality + leading coefficient formula |

11 × 7 = **77 cells** exactly (no sub-layers here, unlike YM L1b/L10b).

## Verdict codes (same as YM pilot)

| Code | Meaning |
|------|---------|
| **P**  | PROVED — layer fully discharges requirement with direct programme citation |
| **Pa** | PARTIAL — layer partially addresses (e.g., within-scope only: CM / h_K=1 / rank r∈{0,1}) |
| **O**  | OPEN-BUT-ADDRESSED — named wall with bypass route + DELTA-10 disclosure |
| **S**  | SILENT — layer does not address requirement directly; BYPASS pointer to programme addressing |
| **L**  | LITERATURE-PROVED — fully discharged by cited external theorem (Deuring / Kolyvagin / GZ / modularity) |

## Global programme-level addressings (ADR)

- **ADR-1** (rank equality, Req 1): L11 Theorem 13.1 for CM / h_K=1 / rank∈{0,1}; out-of-scope → W_rank, W_nonCM, W_hK
- **ADR-2** (c ≠ 0, Req 2): L7 GRH for L(s,ψ) (forces L(E,1)≠0 in rank-0 scope); L11 leading-coefficient formula closure
- **ADR-3** (L-continuation + FE, Req 3): LITERATURE via modularity BCDT 2001 applied at L8 (Deuring factorization), L11 (BSD formula closure)
- **ADR-4** (BSD formula, Req 4): L11 Theorem 13.1 explicit formula c* = |Ш|·Ω·R·∏c_p / |tors|²
- **ADR-5** (Ш finite, Req 5): L9 Kolyvagin (rank 0 in scope); W_Sha for wider scope
- **ADR-6** (any E/Q, Req 6): In-scope CM-only at L1-L11; W_nonCM bypass via GL₂-BC + BCDT 2001
- **ADR-7** (any rank, Req 7): In-scope r∈{0,1} at L9-L10; W_rank bypass via p-adic L / Iwasawa / 5D KK-spectral

## Named walls (expected to materialize)

Per brief DELTA 10, the four walls:

- **W_rank** — high rank r ≥ 2 (Req 7 column)
- **W_nonCM** — non-CM elliptic curves (Req 6 column)
- **W_hK** — CM with h_K > 1 (bridge family construction; Req 6/7 related)
- **W_Sha** — unconditional Ш_C finiteness outside rank 0 (Req 5 column)

These are expected OPEN-BUT-ADDRESSED at L11 (Req 6, 7) and L9 (Req 5), with bypass routes per strategy doc §6 and brief DELTA 10.

## Verdict prior (before per-cell audit)

Global programme picture:

- **Req 1 (rank equality)**: PROVED-in-scope at L11 (via L7 GRH + L9 Kolyvagin + L10 GZ); OPEN-BUT-ADDRESSED outside via W_rank. Most intermediate layers SILENT with bypass pointer to L11.
- **Req 2 (c ≠ 0)**: PROVED-in-scope at L7-L11; SILENT upstream.
- **Req 3 (L-cont + FE)**: LITERATURE at L8 (Deuring needs L-function existence; modularity provides it unconditionally for E/Q via BCDT); inherits at L11; SILENT upstream.
- **Req 4 (BSD formula)**: PROVED-in-scope at L11; PARTIAL at L9 (Rubin 1991 Sha-formula in rank 0 CM); SILENT upstream.
- **Req 5 (Ш finite)**: LITERATURE/PROVED at L9 in rank-0 CM; OPEN-BUT-ADDRESSED (**W_Sha**) for wider scope; SILENT upstream.
- **Req 6 (any E/Q)**: OPEN-BUT-ADDRESSED (**W_nonCM** + **W_hK**) at L11; scope disclosure at L1-L11 CM-only.
- **Req 7 (any rank)**: OPEN-BUT-ADDRESSED (**W_rank**) at L11; PROVED-in-scope at L9/L10 for r∈{0,1}.

## DELTA 11 carry-overs

Two BROKEN from Paper 26 adversarial run-01 require propagation into audit framing:

1. **Conditionality framing**: chain is NOT "unconditional"; it is conditional on CBB axioms (same status as Paper 13 RH). Any author verdict that says "unconditional" in L11 gets WEAKENED by critic to "conditional on CBB." Document in kills.md.
2. **Curve 32.a3 c_2 datum**: numerical verification uses c_2 = 4 (LMFDB), not c_2 = 1. Already corrected in solutions-with-prize/paper26-bsd/nodes/K-bsd-theorem.md (row: "Tamagawa $c_2$ | 4 (LMFDB 32.a3; corrected from earlier draft)"). Flag resolved in kills.md; does not affect this audit's cell verdicts.

Plus 5 WEAKENED items to tighten citations (brief DELTA 11):
- CM factorization notation (Attack 2) → cite Deuring 1953 explicitly at L8
- Ha-Paugam construction precision (Attack 3) → cite Ha-Paugam 2005 at L1
- Meyer-over-K precision (Attack 4) → cite Connes-Marcolli extension at L5
- Heegner hypothesis for GZ (Attack 7) → cite Yuan-Zhang-Zhang at L10
- Twist argument for L(s,ψ) (Attack 11) → cite Connes-Marcolli twist at L7
- Rank-1 leading coefficient (Attack 13) → cite Rubin 1991 at L9 / L11

## Plan (execution order)

1. Draft author-verdicts for all 77 cells — walk L1→L11 by Wiles requirement.
2. Critic pass: propose alternative per cell (at least one proposal, agreement acceptable).
3. Arbiter: decide per cell; record rejected alternatives.
4. Assemble `compliance-map.md` with matrix + distributions + named-wall disclosure + SILENT enumeration.
5. Write `vertices/bsd/audit-draft.md` / `critic-attacks.md` / `arbiter-decisions.md`.
6. Write `kills.md` (conditionality + 32.a3 + 5 WEAKENEDs from run-01 carry-over).
7. Write `silent-cells.md` (every SILENT cell with BYPASS action to ADR-N).
8. Write `commit-memo.md` with verdict distributions, SILENT count, LOCKED status, next-run recommendation.

## Expected SILENT count

~35-45 of 77 cells expected SILENT at first pass. Most intermediate layers (L2-L6) address intermediate structure (bridge family, cocycle shift, Baker reinforcement) and do not individually close Wiles requirements. Those close at L7 (GRH via ADR-2), L8-L11 (rank + BSD formula), with bypass pointers upstream.

**Critical check**: every Wiles requirement column must have ≥ 1 non-SILENT cell. Otherwise §5d violation and new NAMED WALL required.

Prediction: all 7 columns will have non-SILENT cells (PROVED-in-scope at L7/L8/L9/L10/L11 feeds every requirement to some verdict class). No new named walls beyond W_rank / W_nonCM / W_hK / W_Sha.

## Open questions / flags

- **Outlet.md missing** for BSD (flag for Phase 2 research; not blocking this audit).
- **Pin #6 J_CKM audit** (PROOF-CHAIN §"Known gap"): not in the 7-requirement audit; record as a side-note in commit-memo for completeness. No link status change.
- **CBB-axiom status**: same as Paper 13/RH. Stated per Paper 26 adversarial run-01 BROKEN 1. All "unconditional" claims tempered to "conditional on CBB (same status as Paper 13 RH)."

## Success criteria

- 77 cells audited, each with verdict + citation + arbiter decision.
- Zero SILENT cells at end (every SILENT has BYPASS action).
- Four named walls disclosed with DELTA-10 fields (status / bypass routes / bypass citation / aggregate confidence / effect-if-fails / effect-if-succeeds).
- §5d compliance: every Wiles requirement column has ≥ 1 non-SILENT cell.
- commit-memo.md records LOCKED.

## Runtime decision log

- 2026-04-14, t=0: plan set. Begin per-layer author-verdict drafting.
- 2026-04-14, t=1: matrix built, 77 cells verdicts drafted; critic pass dispatched in single sweep (simulated three-voice: author/critic/arbiter as a single-operator internal debate).
- 2026-04-14, t=2: arbiter resolutions logged; kills.md from run-01 carry-overs + new WEAKEN.
- 2026-04-14, t=3: silent-cells.md enumerated, BYPASS actions all point to PROVED/LITERATURE/OPEN-BUT-ADDRESSED cells in the chain.
- 2026-04-14, t=4: commit-memo LOCKED. Recommendation: proceed to B_bare + C_bare synthesis (run-03 + run-04).

---

*End of blackboard. Compliance audit begins.*
