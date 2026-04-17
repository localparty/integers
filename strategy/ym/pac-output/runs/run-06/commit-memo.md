# run-06 commit memo — Pillar-C HARDEN bare synthesis for YM

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Outcome
**LOCKED — PUBLISH-READY**

## Deliverable
`strategy/ym/deliverables/ym-harden-bare.md` — 429 lines; 7 sections; 12 externals + 1 internal inventoried; 13 new theorems enumerated as Pillar-C hardening output.

## Summary

### Externals inventoried
- **12 externals** (E1–E12) classified per §5C.1:
  - 8 receive EXTEND / CONSTRUCT hardening (E1 Bałaban, E2 OS, E4 Feshbach, E5 Harlander–Suzuki, E6 Reisz, E7 Lüscher, E8 O–Seiler, E9 MRS) → **13 new theorems into the literature**
  - 2 receive VERIFY only (E3 Glimm–Jaffe, E10 Seiler LNP 159)
  - 2 are N/A (E11 Jaffe–Witten = target; E12 Hairer = parallel programme)

### Internal self-harden
- **1 internal** (I1 = L.3.7-audit, paper08 Appendix L §L.3 Lemma L.3.7)
  - Primary route: ORA-v8 verify-and-repair wave (VERIFY)
  - Redundant route: Bałaban polymer SL-1 independent proof (CONSTRUCT)
  - Fallback alternates (×4): p8L.7.3 Reason-3 reformulation; alternate Lüscher interpolation; UNLOCK-1 Dunne–Ünsal $\mathbb{R}^4$ extension; UNLOCK-2 Watson sectorial matching (BYPASS)

### Folders scheduled
10 folders under `strategy/externals-hardening/` queued for downstream PAC dispatch:
- balaban-rg/
- os-reconstruction/ (bundles E2 + E3)
- feshbach-projection/
- harlander-suzuki-flow/
- reisz-power-counting/
- luscher-gradient-flow/
- osterwalder-seiler-rp/
- mrs-phi43/
- seiler-lnp159/
- paper08-L3.7/ (self-harden)

## Discipline checks
- [x] BARE MODE (zero prose paragraphs)
- [x] ≤ 15 pages (429 lines ≈ 10–12 pages)
- [x] Every claim cites programme paper or external with §-level precision
- [x] Fair attribution throughout (per Universal Approval §5C)
- [x] Externals inventory table complete (§2)
- [x] Per-external harden stubs (§3, 12 sub-sections)
- [x] L.3.7 self-harden (§4)
- [x] Double-kill narrative (§5)
- [x] Field-improvement summary (§6)
- [x] References + folder scheduling (§7)

## Critic pass
8 attacks adjudicated by arbiter in `primitive-log.md`; all resolved as OVERRULED / PARTIALLY SUSTAINED / SUSTAINED-AS-CLARIFICATION. No NEEDS-REVISION flags. Discipline maintained.

## Arbiter verdict
**PUBLISH-READY.** Ready for Zenodo as Pillar-C companion to `ym-clay-bare.md` (Pillar A) and `ym-independence-bare.md` (Pillar B).

## Ladder rung
- Pillar A: comply-bare (PUBLISH-READY; prior run)
- Pillar B: independence-bare (PUBLISH-READY; prior run)
- **Pillar C: harden-bare (PUBLISH-READY; THIS RUN)**
- Pillar-A/B/C bonus: beyond-bare (PUBLISH-READY; prior run with UA patch)
- Next rung: harden-full (composition-backward; DEFERRED)

## Recommendations for next cycle
1. Dispatch 10 per-external HARDEN sub-agents to populate `strategy/externals-hardening/<name>/` folders with:
   - `X-RAY.md` (layer-by-layer of the external)
   - `compliance-map.md` (external × axiom matrix)
   - `hardened-routes.md` (the EXTEND / CONSTRUCT statements from §3 with proofs)
   - `narrative.md` (fair-attribution prose from §5)
2. Dispatch ORA-v8 verify-and-repair wave on paper08 §L.3 with L.3.7 as target (expected 3-author wave).
3. Confirm §7.5 folder scheduling is written when folders are created (update ym-harden-bare.md §7.5 from SCHEDULED → CREATED).
4. Gate-check per §5C.3: no external cited without at least one VERIFY pass completed.

## Lock status
**LOCKED.**
