# RH PAC run-02 — Kills (Claims Weakened During Audit)

*7 claims weakened from author first-pass to arbiter final. No chain-validity or §5d-compliance impact.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Summary

- **Total kills**: 7
- **Net direction**: 6 Pa→S (author overstated ambient prerequisite as "partial addressing"), 1 P→Pa (author overstated "use of FE" as "proof of FE")
- **Net upgrades** (not kills, but recorded for balance): 1 Pa→P (L3d Req 5)
- **§5d impact**: NONE. All Core 1–5 requirements retain ≥ 1 non-SILENT cell post-arbiter. Chain remains LOCKED.

---

## Kill 1: L1 Req 3 — Pa → S

- **Author**: Pa. Rationale: "L1 construction uses ξ-structure (Γ(s/2), Eq. (1)); CCM constructs D_N on E_N^+ where E_N^+ inherits FE symmetry."
- **Critic**: S. Rationale: "FE is ambient prerequisite, not L1 content."
- **Arbiter**: S. Rationale: rubric distinguishes "addresses requirement" (Pa) from "uses as ambient prerequisite" (S with BYPASS). L1 is the latter.
- **Kill character**: downgrade of overstated partial-addressing.
- **Citation post-kill**: bypass→ADR-3 (classical FE at programme-entry / B_bare §5).
- **Impact on §5d**: none (Req 3 retains L5 Pa, L6 Pa).

## Kill 2: L2 Req 3 — Pa → S

- **Author**: Pa. Rationale: "KMS_1 uniqueness uses FE via analytic continuation of local ζ-factors."
- **Critic**: S. Rationale: "FE is ambient; L2 content is ITPFI product structure."
- **Arbiter**: S. Rationale: same as Kill 1.
- **Citation post-kill**: bypass→ADR-3.
- **Impact**: none.

## Kill 3: L3a Req 3 — Pa → S

- **Author**: Pa. Rationale: "Γ-factor structure from FE enters archimedean tail estimate."
- **Critic**: S. Rationale: "Tail bound; FE is ambient, not in L3a content."
- **Arbiter**: S.
- **Citation post-kill**: bypass→ADR-3.
- **Impact**: none.

## Kill 4: L3b Req 5 — Pa → S

- **Author**: Pa. Rationale: "O(log λ / λ) rate consistent with Odlyzko numerical precision."
- **Critic**: S. Rationale: "Chain-internal quality metric, not numerical-consistency anchor."
- **Arbiter**: S. Rationale: the numerical-consistency axis tests against ζ-zero tables, not chain-internal approximation rates.
- **Citation post-kill**: bypass→ADR-5 (L6 output match).
- **Impact**: none (Req 5 still has L3d P, L6 P, L5 Pa, S1 Pa).

## Kill 5: L4c Req 1 — Pa → S

- **Author**: Pa. Rationale: "Spectral exactness feeds directly into L6 RH QED."
- **Critic**: S. Rationale: "Feeds ≠ addresses; RH at L6 only."
- **Arbiter**: S. Rationale: "feeds into" is not "partially addresses" at the axis level.
- **Citation post-kill**: bypass→ADR-1 (L6).
- **Impact**: none (Req 1 retains L1 O, L5 Pa, L6 O).

## Kill 6: L5 Req 3 — P → Pa

- **Author**: P. Rationale: "Hurwitz uses Ξ(t) with FE Eq. (1) — THE layer where FE is used structurally."
- **Critic**: Pa. Rationale: "Uses ≠ proves the FE."
- **Arbiter**: Pa. Rationale: L5 uses the FE most visibly in the chain but doesn't re-derive it. FE is classical input at B_bare §5 programme entry.
- **Kill character**: downgrade of "locus-of-use" to "partial-using" (within non-SILENT).
- **Citation post-kill**: p13§L5 Hurwitz uses Ξ which is FE-symmetric; FE itself cited at B_bare §5 classical (Edwards / Titchmarsh / Bombieri §I Eq. (1)).
- **Impact**: none (remains Pa, non-SILENT).

## Kill 7: L5 Req 7 — Pa → S

- **Author**: Pa. Rationale: "Ξ carries Weil-explicit-formula-dual structure via Mellin duality."
- **Critic**: S. Rationale: "Indirect carrying is too weak for Pa at the axis level."
- **Arbiter**: S. Rationale: Weil EF anchor is at L2 (not L5). L5 propagates the structure but doesn't re-anchor it.
- **Citation post-kill**: bypass→ADR-7 (L2).
- **Impact**: none (Req 7 retains L2 P, L6 Pa).

---

## Upgrades (recorded for balance; not kills)

### Upgrade 1: L3d Req 5 — Pa → P

- **Author**: Pa. Rationale: "ρ ≥ 4.27 consistency pin."
- **Critic**: P. Rationale: "Quantitative pin ρ ≥ 4.27 uniform in N is a concrete predictive anchor."
- **Arbiter**: P. Rationale: chain-derived quantitative pin aligned with empirical CF spectra is stronger than "consistency". Upgrading makes Req 5 anchor at L3d in addition to L6.
- **Impact**: strengthens §5d on Req 5 (now 2 P: L3d, L6).

---

## Kill category distribution

- **Overstated-ambient-prerequisite** (Pa→S): 4 (Kill 1, 2, 3 all L1-level-Req-3 / L3a-Req-3 variants; Kill 5 L4c-Req-1)
- **Overstated-chain-internal-metric** (Pa→S): 1 (Kill 4 L3b-Req-5)
- **Overstated-indirect-carrying** (Pa→S): 1 (Kill 7 L5-Req-7)
- **Overstated-locus-of-use as "proof"** (P→Pa): 1 (Kill 6 L5-Req-3)

All kills reflect sharpening of the rubric distinction:

- **Pa** requires the layer's own content to partially address the requirement (not merely use the requirement as ambient input).
- **P** requires the layer's own content to fully establish the requirement at the axis level (not merely use it as an ingredient).

Four L1-L3a cells were author-generous on this distinction; critic corrected. Arbiter agreed.

---

## Verdict movement summary

| Cell | Author | Arbiter | Movement |
|------|--------|---------|----------|
| L1 Req 3 | Pa | S | kill |
| L1 Req 4 | P | P | (author confirmed) |
| L2 Req 3 | Pa | S | kill |
| L3a Req 3 | Pa | S | kill |
| L3b Req 5 | Pa | S | kill |
| L3d Req 5 | Pa | P | upgrade |
| L4c Req 1 | Pa | S | kill |
| L5 Req 3 | P | Pa | kill (within non-SILENT) |
| L5 Req 5 | Pa | Pa | confirm (strengthen-cite) |
| L5 Req 7 | Pa | S | kill |
| S1 Req 5 | Pa | Pa | confirm (strengthen-cite) |

Net: 7 kills, 1 upgrade, 2 strengthen-cite confirmations, 1 author-confirmed-over-critic (L1 Req 4).

## §5d post-kill check

All Core 1-5 retain non-SILENT coverage:

- **Req 1**: 3 non-SILENT (L1 O, L5 Pa, L6 O) — PASS
- **Req 2**: 1 non-SILENT (L6 Pa) — PASS
- **Req 3**: 2 non-SILENT (L5 Pa, L6 Pa) — PASS
- **Req 4**: 4 non-SILENT (L1 P, L4c Pa, L5 Pa, L6 P) — PASS
- **Req 5**: 4 non-SILENT (L3d P, L5 Pa, S1 Pa, L6 P) — PASS

No §5d regression. Chain LOCKED.

---

*End of kills.md.*
