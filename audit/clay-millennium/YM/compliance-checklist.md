# YM Clay Compliance Checklist — paper08-yang-mills

**Programme paper:** `/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/`
**Source of truth for claims:** `solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md`, `solutions-with-prize/paper08-yang-mills/STATUS.md`
**Strategy file:** `strategy/ym/00-millenium-strategy.md`
**Last programme state:** 18 layers, 1 open wall (H4, addressed via Balaban RG + gradient flow bypass, Step 18', confidence 0.65, L.3.7 audit pending)
**This file appended:** 2026-04-14

---

## §4 Clay Gates (publication + process)

| Gate | Status | Notes |
|------|--------|-------|
| (a) Qualifying Outlet publication | [ ] NOT-STARTED | No journal submission yet. Cascade target: Annals / Inventiones / CMP tier. Zenodo + arXiv are PRIORITY but do not qualify. |
| (b) 2-year rule since publication | [ ] CLOCK-NOT-STARTED | Begins at Qualifying Outlet publication. |
| (c) General acceptance | [ ] NOT-STARTED | Requires independent publications, conference talks, awards. |
| (d) Satisfactorily addresses official description | [ ] PARTIAL | See §3 below. |

## §5d Jaffe-Witten 7-requirement coverage

Verdict classes: **PROVED** / **PARTIAL** / **OPEN-BUT-ADDRESSED (OBA)** / **SILENT** (§5d violation)

| # | Requirement | Verdict | Programme citation | Notes |
|---|---|---|---|---|
| 1 | Any compact simple gauge group G | [ ] AUDIT NEEDED | solutions-with-prize/paper08-yang-mills/PROOF-CHAIN.md | Likely tacitly SU(N); need explicit generality statement |
| 2 | On R^4 (infinite volume) | [ ] AUDIT NEEDED | PROOF-CHAIN.md | Explicit infinite-volume limit T^4 → R^4 is J-W §6-named hard problem |
| 3 | Mass gap Δ > 0, uniform in volume | [ ] PARTIAL/AUDIT | STATUS.md I.1 (lattice σ > 0, Δ > 0 for β < 10^14); PROOF-CHAIN layer for spectral gap | Uniformity in V = J-W §6-named hard problem |
| 4 | Full Wightman OR OS axioms | [ ] PARTIAL | Partial via CBB axioms (integers/paper01-qg5d/paper8 axioms) | Need explicit Wightman/OS axiom verification |
| 5 | AF match at short distance | [x] OPEN-BUT-ADDRESSED | H4 (Step 18') via Balaban RG + gradient flow, confidence 0.65 | L.3.7 audit pending; paper50-h4-replacement backup |
| 6 | Stress tensor + OPE with AF-prescribed singularities | [ ] AUDIT NEEDED | PROOF-CHAIN.md | Need explicit stress tensor + OPE construction |
| 7 | Non-triviality | [x] PROVED | SU(2) exact area law (STATUS.md I.2); lattice confinement | F ≠ 0; coupling nonzero |

## §5d silence audit (must all be addressed, even if not proved)

Any row marked "AUDIT NEEDED" above currently risks **SILENT** status — a §5d violation. These must be converted to at least OPEN-BUT-ADDRESSED (named wall with bypass route) before Clay submission.

**Priority audit actions:**
1. Explicit generality clause: "Theorem A holds for any compact simple G" OR "We prove it for SU(N); extension to any compact simple G is [discussed / conjectured / an open named wall]."
2. Infinite-volume limit: explicit thm statement + proof sketch OR named wall.
3. Uniform mass gap in V: explicit or named wall.
4. Stress tensor + OPE: explicit construction OR named wall.
5. Wightman/OS axiom-by-axiom verification table.

## Publication cascade status

Per `strategy/ym/00-millenium-strategy.md §9`:
- [ ] Zenodo bundle (bare + full)
- [ ] GitHub public
- [ ] arXiv via endorsement
- [ ] Journal submission (Qualifying Outlet)
- [ ] 2-year clock starts
- [ ] Community engagement (conferences, talks, independent discussion)
- [ ] Clay consideration (passive monitoring by CMI per §5e)

## Readiness: **NEEDS-WORK** (structural audit of requirements 1-4, 6 required before Zenodo)
