# T8 Compositional Triangle Fills

*For each triangle (prev, current, next) where 2/3 edges are filled, propose the third.*

---

## Triangle 1: RH (2) — Lindelöf (3) — GRH (4)

- RH→Lindelöf: STRONG (filled T7 ext)
- Lindelöf→GRH: PARTIAL (filled T7 ext)
- RH→GRH: **already FILLED** (original ring edge, STRONG — character-twisted extension)

Result: **SKIP** (all 3 edges already filled). Triangle is CLOSED.

## Triangle 2: BGS (14) — Katz-Sarnak (15) — Twin Primes (16)

- BGS→KS: STRONG (filled T7 ext)
- KS→Twin Primes: CANDIDATE (filled T7 ext)
- BGS→Twin Primes: **already FILLED** (original ring edge from T4 — GUE small-gap tail → prime gaps)

Result: **SKIP** (all 3 filled). Triangle CLOSED.

## Triangle 3: Lehmer (22) — Sato-Tate (23) — Schanuel (24)

- Lehmer→ST: PARTIAL (filled T7 ext)
- ST→Schanuel: SPECULATIVE (filled T7 ext)
- Lehmer→Schanuel: **already FILLED** (original ring edge from T7 — CANDIDATE: Mahler measure gap → algebraic independence)

Result: **SKIP** (all 3 filled). Triangle CLOSED.

## Triangle 4: Lindelöf (3) — GRH (4) — BSD (5)

- Lindelöf→GRH: PARTIAL (filled T7 ext)
- GRH→BSD: PARTIAL (original ring edge — Dirichlet L → Hecke L)
- Lindelöf→BSD: **EMPTY** → COMPOSE

**Compositional proposal**: Lindelöf controls amplitude on the critical line for ζ(s). The character-twisted extension (Lindelöf→GRH) gives GLH for L(s,χ). GRH→BSD transfers to Hecke L-functions L(s,ψ). Composing: Lindelöf for Hecke L-functions controls the convergence rate of the Euler product that BSD's rank formula depends on. Specifically, |L(1/2+it,ψ)| = O((Nf·t)^ε) ensures the analytic continuation of L(E,s) is well-behaved at the central point.

**Status**: CANDIDATE (valid composition but each step adds conditions)

## Triangle 5: RH (2) — Lindelöf (3) — Cramér (17)

- RH→Lindelöf: STRONG
- Lindelöf→Cramér: STRONG (filled T8 chord)
- RH→Cramér: **already FILLED** (hub chord — zeros ARE eigenvalues → gap statistics)

Result: **SKIP** (all 3 filled). But note: the composition RH→Lindelöf→Cramér is now a VERIFIED 2-step path, stronger than the direct RH→Cramér chord which is more speculative.

## Triangle 6: Katz-Sarnak (15) — Twin Primes (16) — Cramér (17)

- KS→Twin Primes: CANDIDATE
- Twin Primes→Cramér: PARTIAL (ring edge — min gap ↔ max gap)
- KS→Cramér: **EMPTY** → COMPOSE

**Compositional proposal**: KS symmetry type determines the extreme-value distribution of zero gaps. For ζ(s) (unitary type): the Tracy-Widom distribution governs the max gap (Ben Arous-Bourgade). Different symmetry types have different extreme-value distributions. KS→Cramér: the symmetry type constrains the Cramér constant. For unitary type: 2e^{−γ} (Granville) is the GUE prediction.

**Status**: CANDIDATE (compositionally valid; the Tracy-Widom connection is classical)

## Triangle 7: Sato-Tate (23) — Schanuel (24) — Hilbert 6 (25)

- ST→Schanuel: SPECULATIVE
- Schanuel→Hilbert 6: CANDIDATE (ring edge)
- ST→Hilbert 6: **EMPTY** → COMPOSE

**Compositional proposal**: Sato-Tate equidistribution of Frobenius angles → Schanuel algebraic independence of exp values → Hilbert 6 axiom completeness via the e-circle. The composition: if the Frobenius angles are equidistributed (ST) and their exponentials are algebraically independent (Schanuel), then the e-circle's description is complete (Hilbert 6 closure).

**Status**: SPECULATIVE (each link is weak; composition doesn't strengthen)

## Summary

| Triangle | Third edge | Status | New cell? |
|---|---|---|---|
| Lindelöf-GRH-BSD | Lindelöf→BSD | CANDIDATE | Yes |
| KS-TwinPrimes-Cramér | KS→Cramér | CANDIDATE | Yes |
| ST-Schanuel-H6 | ST→Hilbert 6 | SPECULATIVE | Yes |

**3 new compositional cells.** Plus 7 chord cells from direct fills = **10 new cells total in T8.**
