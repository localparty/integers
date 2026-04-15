# BSD Compliance Audit — Arbiter Decisions (run-02)

*Arbiter resolution of the 8 dissents raised by the critic in `critic-attacks.md`. Each decision records the rejected alternative.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Summary

- Dissents resolved: 8
- Critic-win: 8 (all upgrades / tightenings accepted — they strengthen rather than weaken the map and match YM-pilot discipline)
- Author-win: 0 (author draft was a valid starting point; no genuine disagreements after deliberation)
- Net effect: verdict map slightly STRENGTHENED in coverage (scope fingerprints Pa rather than S; LITERATURE-class L where applicable); 32.a3 BROKEN-2 confirmed resolved; CBB conditionality rider propagated.

---

## Decision 1 — L1 Req 6 S → Pa (critic-win)

**Arbiter reasoning**: The h_K = 1 hypothesis is an OPEN and VISIBLE restriction at the layer of origin. YM pilot discipline (L1 Req 3 "μ₁ KK gap is V-independent") rates such scope-fingerprints as Pa not S. Author's S verdict conflated "silent on the requirement in scope" with "silent on the requirement's open frontier"; the latter is Pa because the layer's construction carries the scope-visibility.

**Final**: **Pa** with bypass to W_hK and W_nonCM at L11.

**Rejected**: author S (downgrades visibility to silence).

## Decision 2 — L2 Req 6 S → Pa (critic-win)

**Arbiter reasoning**: Same logic as Decision 1. The 355-triple enumeration encodes specific-K / h_K=1 data; scope visible at layer.

**Final**: **Pa**

**Rejected**: author S.

## Decision 3 — L7 Req 2 Pa → P (critic-win)

**Arbiter reasoning**: GRH's zero-localisation on Re(s) = 1/2 directly implies L(E, 1) ≠ 0 because s = 1 has real part 1, not 1/2. This is the c ≠ 0 condition in the analytic-rank-0 case (the scope of Theorem 13.1). YM pilot discipline (L14 Req 7 signature (i) σ > 0 is P-class at origin) matches. The CBB-conditionality rider is separate and applies to all L7+ verdicts; it does not change P → Pa, it just riders the P claim.

**Final**: **P (conditional on CBB p23)**

**Rejected**: author Pa (under-credits the direct implication).

## Decision 4 — L7 Req 3 S → Pa (critic-win)

**Arbiter reasoning**: L7 USES L-continuation as an input (to speak of zeros on the critical strip). Ingredient-dependence is Pa, not S. YM pilot analogue: L15 Req 6 Pa "Suzuki formula enabler for T_μν".

**Final**: **Pa** (ingredient role; continuation provided by L8 via modularity BCDT)

**Rejected**: author S (treats "uses an input" as silence).

## Decision 5 — L8 Req 3 Pa → L (critic-win)

**Arbiter reasoning**: Modularity BCDT 2001 + Wiles 1995 + Taylor-Wiles 1995 is a published, widely-cited, unconditional LITERATURE theorem that gives L-continuation + FE for every E/Q. This is the strongest discharge available and must be rated L (LITERATURE), not Pa. The chain inherits this discharge at L11 (also L-class).

**Final**: **L**

**Rejected**: author Pa (under-credits an unconditional LITERATURE theorem).

## Decision 6 — L9 Req 5 Pa → L (critic-win)

**Arbiter reasoning**: Kolyvagin 1990 |Sha(E/Q)| < ∞ for rank-0 curves is a LITERATURE theorem. Within the chain's rank-0 CM scope, this is full discharge. Pa is the right class for the WIDER scope (W_Sha at L11), but at L9 in-scope the theorem fully applies. YM pilot: "LITERATURE (Kolyvagin 1990)" badge in paper26 PROOF-CHAIN matches this rating.

**Final**: **L**

**Rejected**: author Pa (under-credits the literature-class discharge in scope).

## Decision 7 — L10 Req 7 O → Pa (critic-win)

**Arbiter reasoning**: L10 proves rank 1 via GZ + Kolyvagin (literature-backed). The chain is PROVED at rank 1, not OPEN. The O status belongs at L11 where the scope-wall W_rank is disclosed (for r ≥ 2). Pa is correct here: rank 1 in scope; r ≥ 2 bypass is W_rank at L11.

**Final**: **Pa**

**Rejected**: author O (misplaces the wall at the wrong layer).

## Decision 8 — L11 conditionality language "unconditional" → "conditional on CBB p23" (critic-win)

**Arbiter reasoning**: Paper 26 adversarial run-01 BROKEN 1 is binding. The chain inherits CBB axioms from Paper 13 RH infrastructure and is conditional on them, with same status as Paper 13 RH. The verdict **P** for Req 1, 2, 4 at L11 stands unchanged; only the rider changes. Similarly for L11 Req 5 Pa.

**Final for L11 Req 1**: **P (conditional on CBB)**
**Final for L11 Req 2**: **P (conditional on CBB)**
**Final for L11 Req 4**: **P (conditional on CBB)**

**Rejected**: author "unconditional" framing (BROKEN 1).

**Propagation**: All L7, L8 (non-LITERATURE cells), L9 (non-LITERATURE cells), L10, L11 P/Pa verdicts carry the implicit conditionality rider. LITERATURE-class L cells (L8 Req 3, L9 Req 5, L11 Req 3) are unconditional because modularity / Kolyvagin are unconditional theorems.

---

## Net effect on verdict map

| Before | After | Count |
|--------|-------|-------|
| Author S → Arbiter Pa (scope fingerprint) | | 2 (L1 Req 6, L2 Req 6) |
| Author S → Arbiter Pa (ingredient-dependency) | | 1 (L7 Req 3) |
| Author Pa → Arbiter P (direct discharge) | | 1 (L7 Req 2) |
| Author Pa → Arbiter L (LITERATURE-class) | | 2 (L8 Req 3, L9 Req 5) |
| Author O → Arbiter Pa (wall misplaced) | | 1 (L10 Req 7) |
| Author "unconditional" → Arbiter rider applied | | 3 (L11 Req 1, 2, 4) |

All changes STRENGTHEN coverage visibility (more non-SILENT cells) AND preserve honesty (CBB rider propagated).

Per brief DELTA 11: WEAKENED items (Attacks 2, 3, 4, 7, 11, 13) citation-tightenings are applied in audit-draft per-cell notes; no further arbiter action required.

---

## §5d compliance verification

After arbiter pass, every Wiles requirement column has ≥ 1 non-SILENT cell:

- Req 1: 4/11 non-SILENT
- Req 2: 7/11 non-SILENT (STRENGTHENED by Decision 3)
- Req 3: 3/11 non-SILENT (STRENGTHENED by Decisions 4, 5)
- Req 4: 4/11 non-SILENT
- Req 5: 3/11 non-SILENT (STRENGTHENED by Decision 6)
- Req 6: 5/11 non-SILENT (STRENGTHENED by Decisions 1, 2)
- Req 7: 4/11 non-SILENT (adjusted by Decision 7, unchanged in column)

§5d PASS.

---

*End of arbiter-decisions.md. Final distribution + lock status at `compliance-map.md` §6.*
