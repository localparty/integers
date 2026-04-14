# BSD Clay Compliance Checklist — paper26-bsd

**Programme paper:** `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/`
**Source of truth:** `paper26-bsd/PROOF-CHAIN.md`
**Last programme state:** 11/11 steps closed; no internal walls. Conditional only on CBB axioms (inherited). Current scope: **CM elliptic curves over Q with h_K = 1**.
**This file appended:** 2026-04-14

---

## §4 Clay Gates

| Gate | Status | Notes |
|------|--------|-------|
| (a) Qualifying Outlet | [ ] NOT-STARTED | Cascade target: Annals / Inventiones / JAMS |
| (b) 2-year rule | [ ] CLOCK-NOT-STARTED | |
| (c) General acceptance | [ ] NOT-STARTED | |
| (d) Satisfactorily addresses official description | [ ] PARTIAL (scope gap) | See below |

## §5d Wiles requirement coverage (Weak BSD — minimum)

| # | Requirement | Verdict | Programme citation | Notes |
|---|---|---|---|---|
| 1 | ord_{s=1} L(E, s) = rank E(Q), for every elliptic curve E/Q | [ ] SCOPE-LIMITED | PROOF-CHAIN.md Steps 7-11 | **Currently proved only for CM E/Q with h_K = 1.** Non-CM case + h_K > 1 case OPEN. |
| 2 | L(E, 1) = 0 ⇔ E(Q) infinite | [x] WITHIN SCOPE | Step 11 (Theorem 13.1) | Within the CM+h_K=1 scope |
| 3 | All ranks (not just r ≤ 1) | [ ] AUDIT | Steps 9-10 import Kolyvagin + Gross-Zagier which are r ≤ 1 | Need to document whether paper26 treats r ≥ 2 within scope |
| 4 | All elliptic curves over Q (CM and non-CM) | [ ] OUT OF SCOPE | | Major gap for full Clay; paper26 explicitly CM only |

## §5d Strong BSD (bonus)

| # | Requirement | Verdict | Notes |
|---|---|---|---|
| 5 | Leading-coefficient formula c* | [x] WITHIN SCOPE | Step 11 theorem states leading-coefficient formula |
| 6 | Finiteness of X_C | [x] WITHIN SCOPE | Step 9 (Kolyvagin gives |X_C| < ∞ in rank 0) |

## §5d compliance verdict

**OPEN-BUT-ADDRESSED — scope cleanly stated.** §5d compliant if the paper explicitly:
- States scope (CM E/Q with h_K = 1)
- Acknowledges extension to non-CM and h_K > 1 as a named wall
- Does not claim full BSD

**§5d VIOLATION if:** paper claims to prove full BSD without this scope caveat.

## External dependencies

- Deuring 1953 (CM factorization) — LITERATURE
- Kolyvagin 1990 (rank 0) — LITERATURE
- Gross-Zagier 1986 (rank 1) — LITERATURE
- Modularity of all E/Q — now theorem (BCDT)
- CBB axioms (programme-internal, paper 1 + paper 8 + paper 13)

## Publication cascade

- [ ] Zenodo
- [ ] GitHub
- [ ] arXiv
- [ ] Journal submission
- [ ] 2-year clock
- [ ] Community acceptance
- [ ] Clay consideration

## Readiness: **NEEDS-WORK** (scope-clarification required; "CM h_K=1 BSD" is a legitimate standalone result but not the full Millennium problem)
