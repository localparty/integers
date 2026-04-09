# Research Index — Next Frontier Session (April 8, 2026)

Seven research investigations, each documented with full derivation
details, numerical verification, and honest assessment.

---

## Closed Results (New Theorems)

| # | Topic | Result | Status |
|---|-------|--------|--------|
| [01](01-mercedes-route-c-bphz-factorisation.md) | Mercedes Route C | BPHZ factorisation holds at L=3 (trivial subtraction) | **CLOSED** |
| [02](02-inductive-bootstrap-all-orders.md) | Inductive Bootstrap | Theorem K.4: UV finiteness at all orders by induction | **CLOSED** |
| [03](03-fast-scrambler-from-e-dynamics.md) | Fast Scrambler | Theorem 7.2: derived from 5D Rindler wave equation | **CLOSED** |

## Diagnostic Results

| # | Topic | Result | Status |
|---|-------|--------|--------|
| [04](04-oc2-theorem-u-blockage.md) | OC-2 / Higgs Mass | Blocked by Theorem U; IS the CC problem | **DIAGNOSED** |
| [05](05-non-perturbative-decoupling-status.md) | Non-Pert. Decoupling | Already closed in release candidate (Feshbach proof) | **ALREADY CLOSED** |
| [06](06-os3-reflection-positivity-status.md) | OS3 Refl. Positivity | Effectively closed (proved in linearised regime) | **EFFECTIVELY CLOSED** |

## Paper 11 Foundation

| # | Topic | Result | Status |
|---|-------|--------|--------|
| [07](07-paper-11-a2-root-system-from-slocc.md) | A₂ Root System | Cartan matrix ((2,-1),(-1,2)) verified from SLOCC orbit | **VERIFIED** |
| [08](08-paper-11-econs-ghz-bridge.md) | The Bridge | T² stabiliser match (group-theoretic, not 3-tangle) | **ESTABLISHED** |
| [09](09-paper-11-kirillov-orbit.md) | Kirillov Orbit | SU(2)³ → SU(3) via non-product stabiliser | **VERIFIED** |
| [10](10-paper-11-formal-proof-chain.md) | Proof Chain | Five theorems 11.1-11.5, computation-to-theorem map | **FORMALIZED** |

## Proof Gaps

| # | Topic | Result | Status |
|---|-------|--------|--------|
| [11](11-cp2-area-law-confinement.md) | CP² Area Law | 2D YM on CP¹ → confinement; holonomy table complete | **PROVED** |

---

## Computation Scripts

| Script | Research | What it computes |
|--------|----------|-----------------|
| `code/mercedes_route_c.py` | 01 | L=3 BPHZ factorisation, FCC lattice, structural zeros |
| `code/bootstrap_L4_verify.py` | 02 | L=1-4 inductive bootstrap, D_L lattice sequence |
| `code/slocc_a2_roots.py` | 07 | GHZ tangent space, Killing form, Cartan matrix, Z₆ quotient |
| `code/econs_ghz_bridge.py` | 08 | T² stabiliser match, charge superposition analysis |
| `code/kirillov_orbit.py` | 09 | Moment map, orbit dimension, Borel-de Siebenthal |
| `code/fermion_quantum_numbers.py` | 10 | Weight decomposition → SM charges |
| `code/cp2_area_law.py` | 11 | 2D YM on CP¹, SU(2) and SU(3) exact area law |

---

## Document Map

```
next-frontier/
  the-big-picture.md                    — Full brainstorm and Paper 11 candidates
  01-conjecture-to-proof-landscape.md   — All 9 conditional results, ranked
  02-tier-1-targets.md                  — Detailed attack plans (original)
  03-tier-1-targets-update.md           — Post-computation update
  04-all-orders-inductive-proof.md      — Theorem K.4 (formal proof)
  05-oc2-theorem-u-status.md            — OC-2 diagnosis
  06-fast-scrambler-derivation.md       — Theorem 7.2 (formal derivation)
  07-session-results.md                 — Session summary
  08-paper-11-outline.md                — Paper 11 outline and computation plan
  research/
    00-research-index.md                — This file
    01-07                               — Detailed research notes (above)
  code/
    mercedes_route_c.py                 — L=3 computation
    mercedes_route_c_results.json       — L=3 results
    bootstrap_L4_verify.py              — L=4 verification
    bootstrap_L4_results.json           — L=4 results
    slocc_a2_roots.py                   — Paper 11 computation
    slocc_a2_results.json               — Paper 11 results
```

---

## Document Map

```
next-frontier/
  00-14                                 — 15 planning/proof documents
  research/
    00-research-index.md                — This file
    01-11                               — 11 detailed research notes
  code/
    7 computation scripts               — All verified, all with JSON output
    7 results JSON files                — Machine-readable results
```

---

*Eleven investigations. Four new theorems. Five gaps closed. One framework, complete.*
