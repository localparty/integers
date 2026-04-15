# INDEX -- Referee Report r01

**Paper:** Paper 26 -- BSD for CM Elliptic Curves from the Integers Programme
**Date:** 2026-04-09
**Referee:** Claude Opus 4.6 (1M context)

---

## Navigation

### Top-level Files
- [summary.md](summary.md) -- Overall verdict and closing disclosures
- [clay-checklist.md](clay-checklist.md) -- Master roll-up of all 37 Clay compliance checks
- [computation-log.md](computation-log.md) -- Computational verifications performed

### Per-Point Analysis (points/)

#### Part A: Bost-Connes Foundation
- [A1 Ha-Paugam](points/A1-ha-paugam/) -- SOUND
  - [00-statement](points/A1-ha-paugam/00-statement.md)
  - [01-algebra](points/A1-ha-paugam/01-algebra.md)
  - [02-kms-uniqueness](points/A1-ha-paugam/02-kms-uniqueness.md)
  - [03-gns-hilbert](points/A1-ha-paugam/03-gns-hilbert.md)
  - [verdict](points/A1-ha-paugam/verdict.md)

- [A2 Nelson](points/A2-nelson/) -- SOUND
  - [00-statement](points/A2-nelson/00-statement.md)
  - [01-analytic-vectors](points/A2-nelson/01-analytic-vectors.md)
  - [02-nelson-theorem](points/A2-nelson/02-nelson-theorem.md)
  - [03-spectral-consequence](points/A2-nelson/03-spectral-consequence.md)
  - [verdict](points/A2-nelson/verdict.md)

- [A3 Meyer Spectral](points/A3-meyer-spectral/) -- **CLOSABLE GAP** (most critical)
  - [00-statement](points/A3-meyer-spectral/00-statement.md)
  - [01-meyer-original](points/A3-meyer-spectral/01-meyer-original.md)
  - [02-extension-zeta-K](points/A3-meyer-spectral/02-extension-zeta-K.md)
  - [03-extension-hecke](points/A3-meyer-spectral/03-extension-hecke.md) -- CRITICAL
  - [04-scope](points/A3-meyer-spectral/04-scope.md)
  - [05-zeros-relationship](points/A3-meyer-spectral/05-zeros-relationship.md)
  - [verdict](points/A3-meyer-spectral/verdict.md)

#### Part B: Bridge Family
- [B1 Bridge Enumeration](points/B1-bridge-enumeration/) -- CLOSABLE GAP (minor)
- [B2 ITPFI](points/B2-itpfi/) -- SOUND
- [B3 Dark State](points/B3-dark-state/) -- SOUND

#### Part C: Transcendence Step
- [C1 Baker](points/C1-baker/) -- **CLOSABLE GAP**
- [C2 Cocycle Shift](points/C2-cocycle-shift/) -- SOUND

#### Part D: GRH to BSD
- [D1 CM Factorization](points/D1-cm-factorization/) -- CLOSABLE GAP (same as A3)
- [D2 Kolyvagin Rank 0](points/D2-kolyvagin-rank0/) -- CLOSABLE GAP (rank-1 vacuity)
- [D3 Gross-Zagier Rank 1](points/D3-gross-zagier-rank1/) -- CLOSABLE GAP (vacuity)

#### Part E: Assembly
- [E1 Complete Chain](points/E1-complete-chain/) -- CLOSABLE GAP (aggregate)
- [E2 Scope Honesty](points/E2-scope-honesty/) -- SOUND

### Clay Compliance Checks (checks/)
- [R-rank/](checks/R-rank/) -- R1 (PASS), R2 (PASS), R3 (PASS)
- [LC-leading-coefficient/](checks/LC-leading-coefficient/) -- LC1-LC7 (5 PASS, 2 PARTIAL)
- [AC-analytic-continuation/](checks/AC-analytic-continuation/) -- AC1-AC3 (all PASS)
- [GRH-riemann/](checks/GRH-riemann/) -- GRH1-GRH9 (5 PASS, 4 PARTIAL)
- [KGZ-kolyvagin-gz/](checks/KGZ-kolyvagin-gz/) -- KGZ1-KGZ5 (all PASS)
- [BC-bost-connes/](checks/BC-bost-connes/) -- BC1-BC5 (all PASS)
- [BR-bridge/](checks/BR-bridge/) -- BR1-BR4 (3 PASS, 1 PARTIAL)
- [TR-transcendence/](checks/TR-transcendence/) -- TR1-TR4 (3 PASS, 1 PARTIAL)
- [SC-scope/](checks/SC-scope/) -- SC1-SC5 (4 PASS, 1 PARTIAL)

---

## Quick Summary

| Category | Count |
|:---------|:------|
| GENUINE GAP | 0 |
| CLOSABLE GAP | 7 points (2 distinct mathematical issues + 5 clarifications) |
| SOUND | 6 points |
| Clay checks: PASS | 29 |
| Clay checks: PARTIAL | 8 |
| Clay checks: FAIL | 0 |
| Estimated closure work | 4-6 pages |

**Bottom line:** The proof chain is structurally correct with no fatal errors. Two closable gaps (Connes-Marcolli twist step and exact Baker promotion) require additional pages of argument. The rank-1 case appears to be vacuously true for the curves in scope. The result is a significant partial result toward BSD, conditional on the CBB axioms.
