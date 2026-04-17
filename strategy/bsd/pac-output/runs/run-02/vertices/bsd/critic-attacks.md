# BSD Compliance Audit — Critic Attacks (run-02)

*Per-cell critic alternatives to the author draft. Agreement is acceptable (not every cell needs a dissent); at minimum the critic verified each cell.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Summary

- Cells reviewed: 77
- Dissents raised: **8**
- Agreements: 69
- Critic bias: WEAKEN by default; uses programme-paper citations to press status down (matches YM pilot protocol).

---

## Dissents

### Dissent 1 — L1 Req 6 (author: S; critic: Pa)

**Author**: SILENT — layer is about BC algebra structure over K, no mention of elliptic curves E/Q breadth.

**Critic**: The h_K = 1 hypothesis is a SCOPE RESTRICTION visible at this layer. It is not silence; it is an explicit fingerprint of where the chain narrows. Per YM pilot discipline (L1 Req 3 "spectral gap not uniform"), visible scope restrictions at the layer that they originate are **Pa**, not S. Bypass → W_hK (and W_nonCM via scope-restriction visibility at L11).

**Proposed verdict**: **Pa**

### Dissent 2 — L2 Req 6 (author: S; critic: Pa)

**Author**: SILENT — bridge family is a construction.

**Critic**: The 355 triples enumerate CM data over K. This is Pa: scope-restriction fingerprint (W_hK, W_nonCM visible).

**Proposed verdict**: **Pa**

### Dissent 3 — L7 Req 2 (author: Pa; critic: P)

**Author**: Pa — GRH zero-localisation feeds L(E, 1) ≠ 0 within scope, but full c ≠ 0 discharge is at L11.

**Critic**: GRH ⇒ s = 1 is not on Re(s) = 1/2 critical line ⇒ s = 1 is not a zero ⇒ L(E, 1) ≠ 0 **directly**. This IS c ≠ 0 in the analytic-rank-0 case. The L11 closure is a convenience collecting c in the formula; the actual c ≠ 0 claim lives at L7 in scope. Per YM pilot discipline (L14 Req 7 "non-triv signature (i) σ > 0"), a direct signature IS P-class at its layer of origin, not Pa.

**Proposed verdict**: **P** (conditional on CBB per BROKEN 1)

### Dissent 4 — L7 Req 3 (author: S; critic: Pa)

**Author**: SILENT — L-continuation is a separate claim (at L8).

**Critic**: L7 USES the continuation (to assert zero localisation on the critical strip). This is Pa (ingredient role with explicit dependence), not S. YM pilot analogue: L15 Req 6 Pa "Suzuki formula enabler for T_μν at L17" — ingredient dependency rated Pa.

**Proposed verdict**: **Pa**

### Dissent 5 — L8 Req 3 (author: Pa; critic: L)

**Author**: Pa — CM factorisation is partial contribution to L-continuation.

**Critic**: STRONGER — modularity BCDT 2001 + Wiles 1995 + Taylor-Wiles 1995 gives L-continuation + FE for EVERY E/Q **unconditionally**. This is LITERATURE-class discharge (L code), not Pa. The Hecke L(s, ψ) continuation is classical (Hecke 1918 + generalisations).

**Proposed verdict**: **L** (LITERATURE)

### Dissent 6 — L9 Req 5 (author: Pa; critic: L)

**Author**: Pa — Kolyvagin gives |Sha| < ∞ in rank-0 scope.

**Critic**: STRONGER — Kolyvagin 1990 is a LITERATURE theorem, fully published and widely cited. The rank-0 CM case (within scope) is FULLY discharged. LITERATURE discharge = L, not Pa. YM pilot analogue: the "LITERATURE (Deuring 1953)" badge in paper26 PROOF-CHAIN matches this discipline.

**Proposed verdict**: **L**

### Dissent 7 — L10 Req 7 (author: O; critic: Pa)

**Author**: OPEN-BUT-ADDRESSED — rank 1 case.

**Critic**: L10 PROVES rank 1 via GZ + Kol. This is not OPEN; it's Pa (rank 1 in scope; r ≥ 2 is W_rank at L11, not at L10). The O status belongs at L11 where the scope-wall lives, not at the underlying rank-1 machinery.

**Proposed verdict**: **Pa**

### Dissent 8 — L11 Req 4 conditionality language (author: "unconditional"; critic: "conditional on CBB")

**Author**: First draft language: "unconditional BSD formula at rank 0 via Kolyvagin + modularity."

**Critic**: Paper 26 adversarial run-01 BROKEN 1. The entire chain inherits CBB axioms from Paper 13 RH infrastructure. No "unconditional" claim for L11. Must say: "conditional on CBB axioms (Paper 23), same status as Paper 13 RH chain." The verdict **P** stands; only the rider changes.

**Proposed verdict**: **P (conditional on CBB)**

---

## Agreements (sample — not all 69 enumerated)

- L3, L4, L5, L6 all-reqs: S or Pa per author; infrastructure layers correctly rated.
- L9 Req 1: Pa (rank-0 case in scope; full rank equality closed at L11).
- L9 Req 2: Pa (agrees).
- L10 vacuous-in-scope treatment: critic agrees all Pa cells.
- L11 Req 1 P: rank equality in scope; conditionality rider applied.
- L11 Req 5 Pa: rank-0 side (L9) closed; W_Sha for wider scope agreed.
- L11 Req 6 O: W_nonCM, W_hK agreed.
- L11 Req 7 O: W_rank agreed.

---

## Critic summary statement

The author draft is substantively correct. The critic's 8 dissents are:
- 3 UPGRADES (L1 Req 6 S→Pa, L2 Req 6 S→Pa, L7 Req 3 S→Pa) — scope-restriction fingerprint and ingredient-dependency should be Pa, not S.
- 1 UPGRADE (L7 Req 2 Pa→P) — GRH directly discharges c ≠ 0 at L7 in scope.
- 2 UPGRADES (L8 Req 3 Pa→L, L9 Req 5 Pa→L) — LITERATURE-class theorems (modularity, Kolyvagin) fully discharge.
- 1 DOWNGRADE (L10 Req 7 O→Pa) — rank 1 is proved; O belongs at the wall.
- 1 CLARIFICATION (L11 Req 4 unconditional → conditional on CBB) — BROKEN 1 carry-over.

All 8 dissents reflect discipline / precision tightening, not chain invalidation.

---

*End of critic-attacks.md. Next: arbiter decisions at `arbiter-decisions.md`.*
