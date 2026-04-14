# Navier-Stokes Clay Compliance Checklist — paper30-navier-stokes

**Programme paper:** `/Users/gsix/quantum-geometry-in-5d-latex/paper30-navier-stokes/` (the LIVE NS paper; `paper27-navier/` is an ORA/strategy-only stub with no PROOF-CHAIN.md — scaffolding, ignore for Clay)
**Source of truth:** `paper30-navier-stokes/PROOF-CHAIN.md`
**Last programme state:** 3/8 links proved (upgraded from 2 after W1/W2 closure). Confidence 4/10. Link 5 (BKM) has TWO published bypass routes.
**This file appended:** 2026-04-14

---

## Which NS paper is live?

- `paper27-navier/` — ORA-harness + strategy dirs only. No PROOF-CHAIN. Scaffolding only.
- **`paper30-navier-stokes/`** — LIVE, has PROOF-CHAIN.md. Treat as Clay-target paper.

## §4 Clay Gates

| Gate | Status | Notes |
|------|--------|-------|
| (a) Qualifying Outlet | [ ] NOT-STARTED | Cascade target: Annals / Inventiones / CPAM / CMP |
| (b) 2-year rule | [ ] CLOCK-NOT-STARTED | |
| (c) General acceptance | [ ] NOT-STARTED | |
| (d) Satisfactorily addresses official description | [ ] PARTIAL | See below |

## §5(b) special clause

NS admits resolution in EITHER direction (A+B smoothness OR C+D breakdown). Programme target: **(B)** existence & smoothness on T^3 (see below — mismatch with §5d check).

## §5d Fefferman requirement coverage

**Note: paper30 proves KK-5D version (M^4 × S^1/Z_2). Fefferman's problem is strictly R^3 or T^3 at viscosity ν > 0 WITHOUT 5D structure.** §5d-compliance requires either (i) reduction from KK 5D to 4D periodic Navier-Stokes, or (ii) explicit scope caveat that paper30 solves a different but related problem.

| # | Requirement | Verdict | Programme citation | Notes |
|---|---|---|---|---|
| A | R^3, smoothness, f≡0 | [ ] OUT OF CURRENT SCOPE | | paper30 targets T^3 via KK |
| B | T^3, smoothness, f≡0 | [ ] PARTIAL | PROOF-CHAIN.md links 1-8 | 3/8 proved; Link 5 (BKM) has two bypass routes (Camlin 2025, arXiv:2601.08854) |
| C | R^3, breakdown | [ ] NOT TARGETED | | |
| D | T^3, breakdown | [ ] NOT TARGETED | | |

Common requirements:
| # | Requirement | Verdict | Notes |
|---|---|---|---|
| 1 | ν > 0 | [x] | |
| 2 | n = 3 | [x] | |
| 3 | div u = 0 | [x] | |
| 4 | u° smooth div-free | [x] | |
| 5 | C^∞ solution | [ ] PARTIAL | Depends on Link 5 BKM closure |
| 6 | Bounded energy | [x] | Link 6 (conjectured) |

## The wall

**Link 5: BKM criterion.** Two published routes identified:
- Route A: Camlin 2025 (bounded Φ functional + Sundman temporal lifting)
- Route B: arXiv:2601.08854 (Jan 2026, cosphere-bundle microlocal regularity)

Both need adaptation to KK setting and integration with paper30's chain.

## §5d compliance verdict

**CRITICAL SCOPE ISSUE:** paper30's KK 5D framing must reduce cleanly to Fefferman's 4D T^3 setup, otherwise it is solving a different problem (§5d violation). The reduction is plausible (KK → 4D effective theory → NS on T^3) but must be EXPLICIT.

## Publication cascade

- [ ] Zenodo (after KK→4D reduction is explicit + BKM routes integrated)
- [ ] GitHub
- [ ] arXiv
- [ ] Journal submission
- [ ] 2-year clock

## Readiness: **NEEDS-MAJOR-WORK** (KK→4D-periodic reduction + Link 5 BKM integration)
