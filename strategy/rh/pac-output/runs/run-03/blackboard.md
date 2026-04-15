# RH PAC run-03 — Blackboard

*Phase 5A COMPLY synthesis (Pillar A). Produces `rh-comply-bare.md`. BARE MODE ONLY. Inputs: run-02 LOCKED compliance map; paper13-rh PROOF-CHAIN; brief DELTA 5.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Plan

1. Mirror the 17-section DELTA-5 structure from the RH brief.
2. Pull verdicts for §3 Requirements Map verbatim from run-02 `compliance-map.md` §1 + §2.
3. Extract theorem statements from `solutions-with-prize/paper13-rh/PROOF-CHAIN.md` link-by-link:
   - L1 → §7 (CCM operators D_N on E_N^+; EXTERNAL arXiv:2511.22755; W1)
   - L2 → §8 (ITPFI + Weil form convergence)
   - L3a-d → §9 (Tail estimates)
   - L4a-c → §10 (Boegli spectral exactness; W1 disclosure block)
   - L5 → §11 (Hurwitz uniform convergence)
   - L6 → §12 (QED)
4. Classical requirements:
   - §5 Analytic continuation + FE — Bombieri §I Eq. (1) + classical citation
   - §6 Trivial vs non-trivial zeros — L1 E_N^+ Γ(s/2)-pole exclusion + L6 spec match
   - §13 PNT equivalence — Bombieri §I + Riemann-von Mangoldt
   - §14 Numerical evidence — van de Lune / te Riele / Winter + Odlyzko + Conrey
5. §15 Proof-chain analytics — 14-node dependency graph + compliance summary.
6. §16 Named Walls — W1 CCM (all 12 DELTA-10 fields) + W2 CF uniformity RESOLVED.
7. §17 References — programme papers with §-level; external only arXiv:2511.22755.

## Discipline enforcement

- Zero prose paragraphs. Theorem statements, definitions, equations, tables, figures, citations only.
- Every theorem cites (paper13 §LX) or (paper13 §LX Theorem T.Y).
- External citation allowed ONLY for arXiv:2511.22755 (CCM) at §7 + §10 + §16.
- Target: ~400-600 lines markdown, ≤ 15 pages.

## W1 12-field disclosure checklist (DELTA 10)

1. Name
2. Location in chain
3. Statement
4. Status (OPEN-BUT-ADDRESSED)
5. External citation (arXiv:2511.22755)
6. Bypass route (Verification Cascade)
7. Bypass citation (strategy/ccm-verification/)
8. Aggregate confidence (8/10 conditional; 9-10/10 layers 2-6)
9. Effect if CCM 2025 journal-accepts
10. Effect if CCM 2025 retracts
11. Audit pending
12. §5d compliance / standing independence

## Verdict distribution (from run-02 LOCKED)

| Req | P | Pa | O | S | Non-S |
|-----|--:|--:|--:|--:|------:|
| 1 | 0 | 1 | 2 | 11 | 21.4% |
| 2 | 0 | 1 | 0 | 13 | 7.1% |
| 3 | 0 | 2 | 0 | 12 | 14.3% |
| 4 | 2 | 2 | 0 | 10 | 28.6% |
| 5 | 2 | 2 | 0 | 10 | 28.6% |
| 6 | 0 | 0 | 0 | 14 | 0% (optional) |
| 7 | 1 | 1 | 0 | 12 | 14.3% |
| TOTAL (98) | 5 | 9 | 2 | 82 | 16.3% |

§5d: PASS on Core 1-5.

## Scheduled outputs

1. `strategy/rh/deliverables/rh-comply-bare.md` — the primary deliverable (17 sections, bare mode)
2. `strategy/rh/pac-output/runs/run-03/vertices/rh/comply-bare-draft.md` — author draft mirror
3. `strategy/rh/pac-output/runs/run-03/vertices/rh/critic-attacks.md` — critic pass
4. `strategy/rh/pac-output/runs/run-03/vertices/rh/arbiter-decisions.md` — arbiter verdicts
5. `strategy/rh/pac-output/runs/run-03/commit-memo.md` — PUBLISH-READY verdict

## Key structural choice

Follow DELTA-5 section structure verbatim; the deliverable filename is `rh-comply-bare.md` (per `strategy/universal-approval-run.md` three-pillar naming), not `rh-clay-bare.md` (brief's older one-pillar name).

## Execution order

1. Draft `rh-comply-bare.md` in deliverables/ directly (single source of truth).
2. Mirror to `vertices/rh/comply-bare-draft.md`.
3. Run critic pass → critic-attacks.md.
4. Run arbiter pass → arbiter-decisions.md.
5. Write commit-memo.md with lock status.

---

*End blackboard.*
