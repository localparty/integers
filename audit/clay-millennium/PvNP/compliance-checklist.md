# P vs NP Clay Compliance Checklist — paper28-pvnp

**Programme paper:** `/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/`
**Source of truth:** `paper28-pvnp/PROOF-CHAIN.md`
**Last programme state:** 5/6 links closed. Link 5 BACKWARD (non-full → Taylor polymorphism) is the wall. Seven bypass routes attempted.
**This file appended:** 2026-04-14

---

## §4 Clay Gates

| Gate | Status | Notes |
|------|--------|-------|
| (a) Qualifying Outlet | [ ] NOT-STARTED | Cascade target: Annals / JAMS / FOCS/STOC companion paper |
| (b) 2-year rule | [ ] CLOCK-NOT-STARTED | |
| (c) General acceptance | [ ] NOT-STARTED | |
| (d) Satisfactorily addresses official description | [ ] PARTIAL | See below |

## §5(b) special clause

P vs NP admits resolution in EITHER direction. Programme target: **P ≠ NP** (standard expectation).

## §5d Cook requirement coverage

| # | Requirement | Verdict | Programme citation | Notes |
|---|---|---|---|---|
| 1 | Turing machine model, Σ finite, |Σ| ≥ 2 | [x] BY CONSTRUCTION | PROOF-CHAIN Link 1 (Boolean BC system) | Implicit in Boolean framing |
| 2 | P defined via polynomial-time TM | [x] STANDARD | | |
| 3 | NP defined via polynomial-time checking relation | [x] STANDARD | | |
| 4 | Decide P = NP or P ≠ NP | [ ] PARTIAL | Link 6 CONDITIONAL on Link 5 backward | Link 5 backward = the wall |
| 5 | General Σ | [x] STANDARD | | |

## Obstruction navigation (informal §5d)

| # | Obstruction | Status | Notes |
|---|---|---|---|
| 6 | Non-relativizing | [ ] AUDIT | Does trinity dictionary relativize? Must address explicitly |
| 7 | Non-natural | [ ] AUDIT | Is spectral-gap/Taylor-gap property "natural" in Razborov-Rudich sense? Must address |
| 8 | Non-algebrizing | [ ] AUDIT | Aaronson-Wigderson algebrization: must address |

Obstructions #6-#8 are not prize gates but are §5d-suspect SILENCES if unaddressed. Paper must explicitly discuss.

## The wall

**Link 5 backward: non-full → Taylor polymorphism.**
Going from infinite-dimensional operator-algebraic property (non-fullness of type III_1 factor) to finite-domain algebraic property (Taylor operation). Seven routes attempted:
- (A) direct spectral gap bypass [highest priority]
- (B) universal-algebraic
- (C) channel correspondence via conditional expectation
- (D) Popa cocycle superrigidity
- (E) Kazhdan/Haagerup bridge
- (F) trinity dictionary inversion
- (G) conditional fallback [current state]

## §5d compliance verdict

**OPEN-BUT-ADDRESSED provided the paper transparently:**
- States Link 5 backward as a named wall
- Discusses the 7 attempted routes
- Explicitly addresses relativization / natural / algebrization (currently AUDIT)

**§5d VIOLATION if:** paper silently skips the wall or the three obstructions.

## Publication cascade

- [ ] Zenodo
- [ ] GitHub
- [ ] arXiv
- [ ] Journal submission
- [ ] 2-year clock
- [ ] Community acceptance
- [ ] Clay consideration

## Readiness: **NEEDS-WORK** (close Link 5 backward OR present as transparent OPEN-BUT-ADDRESSED with obstruction-navigation audit)
