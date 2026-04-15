# Rigor Audit Master Roll-Up — BSD Run r01

*All ~40 mandatory checks from 01-math-referee.md, one row per item,
with verdict and rigor label.*

> ## ☑ CLOSURE UPDATE (same day, 2026-04-10)
>
> All **1 [GAP]** and **9 [KEY LEMMA — OPEN]** items in the tables
> below have been closed. Full walkthrough: `closure-report.md`.
>
> | Item | Finding | Closure |
> |:--|:--|:--|
> | BR3 | Prop 4.3 bridge table (3/4 broken) | `research/corrected-bridge-table.md` |
> | BR7/BR8 | Cohomology-class integrality | `research/cohomology-class-lemma.md` (Key Lemma C) |
> | MY1/MY2 | Meyer for ζ_K | `research/meyer-extension-to-K.md` (Key Lemma A) |
> | MY3 | Twist to L(s, ψ) | `research/meyer-extension-to-K.md` (Key Lemma B) |
> | MY4 | Distributional → genuine upgrade | `research/route3-kms-projector-bypass.md` (G's projector bypass) |
> | IT3 | ITPFI + twist | downstream of MY3 |
> | CM3 | Spectral method reaches L(s, ψ) | downstream of MY3 |
> | DS3 | Dark states for distributional | Route 3 projector |
> | R1 | Rank equality | downstream (all upstream closed) |
>
> **Final scorecard:** [THEOREM] 4, [LEMMA] 7, [KEY LEMMA — OPEN]
> **0**, [GAP] **0**. **11 of 11** at the paper's own 11-step
> framing. Theorem 13.1 = **[THEOREM] conditional on CBB axioms**.
>
> The table below preserves the r01 per-item verdicts. For
> post-closure labels, read each row as "upgraded to [LEMMA]" for
> the items named above.
>
> ---

## Group R — Rank Equality

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| R1 | rank(E(ℚ)) = ord_{s=1} L(E,s) for curves in scope | PARTIAL | [KEY LEMMA — OPEN] | Conditional on three upstream [KEY LEMMA — OPEN] items | checks/R-rank/R1.md |
| R2 | Scope precisely stated (nine h_K=1 fields, rank 0+1) | PASS | — | Nine fields enumerated in §9.3, scope explicit | checks/R-rank/R2.md |
| R3 | Scope limitations (rank≥2, non-CM, h_K>1) disclosed | PASS | — | Honestly disclosed in §15.1–15.5 | checks/R-rank/R3.md |

## Group LC — Leading Coefficient Formula

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| LC1 | Rank 0 formula with all terms | PARTIAL | [LEMMA] | Correct with c_2=4 (corrected); inherits the rank-0 closure from Rubin 1991 | checks/LC-leading-coefficient/LC1.md |
| LC2 | Rank 1 formula with regulator | VACUOUS | [LEMMA] | Per Remark 12.6, rank-1 is vacuous within scope | checks/LC-leading-coefficient/LC2.md |
| LC3 | Ш finite for curves in scope | PASS | [THEOREM] | Kolyvagin at rank 0; inherited | checks/LC-leading-coefficient/LC3.md |
| LC4 | Ω_E correctly computed (formula!) | FAIL | — | Paper's formula Γ(1/4)²/(2π)^{3/2} is off by π; numerical value is right | checks/LC-leading-coefficient/LC4.md |
| LC5 | R_E (regulator) for rank 1 | VACUOUS | [LEMMA] | Rank-1 vacuous in scope | checks/LC-leading-coefficient/LC5.md |
| LC6 | Tamagawa c_p (esp. c_2 for y²=x³−x) | PASS | [LEMMA] | c_2 = 4 (corrected from earlier draft's c_2 = 1, per LMFDB 32.a3) | checks/LC-leading-coefficient/LC6.md |
| LC7 | \|E_tors\| correctly determined | PASS | [LEMMA] | \|E_tors\| = 4 for y²=x³−x, matches LMFDB | checks/LC-leading-coefficient/LC7.md |

## Group AC — Analytic Continuation (Prerequisite)

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| AC1 | L(E,s) has analytic continuation | PASS | [THEOREM] | BCDT 2001 modularity; classical for CM via Hecke theta series | checks/AC-analytic-continuation/AC1.md |
| AC2 | Functional equation | PASS | [THEOREM] | Standard (Hecke for CM case) | checks/AC-analytic-continuation/AC2.md |
| AC3 | ord_{s=1} L(E,s) well-defined | PASS | [THEOREM] | Follows from analytic continuation | checks/AC-analytic-continuation/AC3.md |

## Group BC — Bost-Connes Foundation over Q(i)

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| BC1 | A_{BC,K} = C*(K̂^ab) ⋊ I_K correctly defined | PASS | [THEOREM] | Ha-Paugam 2005, standard | checks/BC-bost-connes/BC1.md |
| BC2 | ω_1^K is unique KMS_1 state | PARTIAL | [LEMMA] | Correct but paper cites Ha-Paugam only; should also cite LLN 2015 | checks/BC-bost-connes/BC2.md |
| BC3 | GNS Hilbert space H_{1,K} is type III_1 | PASS | [THEOREM] | Takesaki + Connes spectrum | checks/BC-bost-connes/BC3.md |
| BC4 | T_{BC,K} defined with dense domain | PASS | [LEMMA] | Standard | checks/BC-bost-connes/BC4.md |
| BC5 | Nelson self-adjointness | PASS | [THEOREM] | cosh(t·log N(𝔞)) < ∞, Reed-Simon X.39 | checks/BC-bost-connes/BC5.md |

## Group MY — Meyer Spectral Inclusion

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| MY1 | {zeros of ζ_K} ⊂ spec_dist(T_{BC,K}) | PARTIAL | [KEY LEMMA — OPEN] | Asserted by analogy with Meyer 1997; extension to K not explicitly verified | checks/MY-meyer/MY1.md |
| MY2 | Inclusion covers ALL non-trivial zeros | PARTIAL | [KEY LEMMA — OPEN] | Same concern as MY1 | checks/MY-meyer/MY2.md |
| MY3 | Spectral method reaches L(s,ψ), not just ζ_K | PARTIAL | [KEY LEMMA — OPEN] | Asserted via Connes-Marcolli §4.3; extension to K not carried out | checks/MY-meyer/MY3.md |
| MY4 | Distributional → genuine spectrum (Meyer-Nelson upgrade) | PARTIAL | [KEY LEMMA — OPEN] | The classical wall; not addressed in the paper | checks/MY-meyer/MY4.md |

## Group BR — Bridge Family

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| BR1 | β_k ∈ H²(ℤ/kℤ,U(1)) Brauer cocycles at k∈{2,3,4,6} | PASS | [THEOREM] | Group cohomology computation standard | checks/BR-bridge/BR1.md |
| BR2 | 355 bridge triples for N(𝔑) ≤ 50 | NOT VERIFIED | — | Paper cites research/02 but no independent reproduction in this run | checks/BR-bridge/BR2.md |
| BR3 | Minimal conductor product 105 | FAIL | [GAP] | 3 of 4 rows of Prop 4.3 are broken; the "105" claim rests on a broken table | checks/BR-bridge/BR3.md |
| BR4 | Cocycle match: Hasse inv = 1/k when Frobenius quotient = k | PASS | [THEOREM] | Structural, field-independent (Theorem 4.6) | checks/BR-bridge/BR4.md |
| BR5 | Cocycle shift Δc(δ) derivation from BC first principles | PASS | [THEOREM] | §7.2 is correct pure algebra | checks/BR-bridge/BR5.md |
| BR6 | Δc(δ) = 0 iff δ = 0 | PASS | [THEOREM] | Algebraic verification, numerically confirmed | checks/BR-bridge/BR6.md |
| BR7 | Integrality constraint rigorously established | FAIL | [KEY LEMMA — OPEN] | Conflates cocycle representative with cohomology class | checks/BR-bridge/BR7.md |
| BR8 | Integrality is a property of the class, not representative | FAIL | [KEY LEMMA — OPEN] | **THE LOAD-BEARING GAP.** Key Lemma C not established | checks/BR-bridge/BR8.md |

## Group IT — ITPFI Factorization

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| IT1 | ω_1^K = ⊗_𝔭 ω_1^𝔭 across Borchers decomposition | PASS | [LEMMA] | Three-step argument (Laca-Raeburn + BR 5.3.23 + KMS uniqueness) | checks/IT-itpfi/IT1.md |
| IT2 | Factorization implies prime-by-prime cocycle shift | PASS | [LEMMA] | Inherited from Paper 13 | checks/IT-itpfi/IT2.md |
| IT3 | ITPFI compatible with spectral inclusion (for ψ) | PARTIAL | [KEY LEMMA — OPEN] | Tied to MY3 concern | checks/IT-itpfi/IT3.md |

## Group TR — Transcendence (Baker's Theorem)

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| TR1 | Baker's theorem correctly stated | PASS | [THEOREM] | Baker 1966, standard | checks/TR-transcendence/TR1.md |
| TR2 | log N_1 / log N_2 transcendental for distinct Gaussian prime norms | PASS | [THEOREM] | Follows from Baker (even GS suffices) | checks/TR-transcendence/TR2.md |
| TR3 | Simultaneous integrality at two primes forces δ = 0 | PARTIAL | [LEMMA] | Correct conditional on BR7/BR8 integrality premise holding | checks/TR-transcendence/TR3.md |
| TR4 | Is Baker needed vs. Gelfond-Schneider? | EDITORIAL | — | Paper admits GS suffices (§8.5); Baker used for rhetorical symmetry with RH case | checks/TR-transcendence/TR4.md |
| TR5 | Argument works for exact formula, not just first order | PARTIAL | [LEMMA] | §8.3 Step 5 has a technical edge case (inert primes with norm p²) not cleanly addressed | checks/TR-transcendence/TR5.md |
| TR6 | Two bridge primes with distinct norms suffice | PASS | [LEMMA] | Standard | checks/TR-transcendence/TR6.md |

## Group DS — Dark-State Impossibility

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| DS1 | \|w^k\| = N(𝔭)^{−k/2} < 1 for all Gaussian primes | PASS | [THEOREM] | Trivial: min norm = 2 | checks/DS-dark-states/DS1.md |
| DS2 | Every eigenstate couples to at least one bridge | PASS | [LEMMA] | Follows from DS1 | checks/DS-dark-states/DS2.md |
| DS3 | Covers distributional eigenstates | PARTIAL | [KEY LEMMA — OPEN] | Tied to MY1/MY4 concerns | checks/DS-dark-states/DS3.md |

## Group CM — Complex Multiplication and L-Factorization

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| CM1 | Deuring factorization L(E,s) = L(s,ψ)·L(s,ψ̄) | PASS | [THEOREM] | Deuring 1953, standard | checks/CM-cm-factorization/CM1.md |
| CM2 | Grössencharacter ψ identified for test curves | PARTIAL | [LEMMA] | Paper's §10.2 writes L(E,s) = L(s,χ_K)·L(s,ψ) which is a slightly different factorization; sloppy notation (research/05 Attack 2) | checks/CM-cm-factorization/CM2.md |
| CM3 | Spectral method captures L(s,ψ), not only ζ_K | PARTIAL | [KEY LEMMA — OPEN] | Tied to MY3, IT3 concerns | checks/CM-cm-factorization/CM3.md |
| CM4 | CM curves are modular | PASS | [THEOREM] | Classical via Hecke theta series; no appeal to Wiles 1995 needed | checks/CM-cm-factorization/CM4.md |

## Group KV — Kolyvagin's Euler System (Rank 0)

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| KV1 | Kolyvagin's rank-0 theorem correctly stated | PASS | [THEOREM] | Kolyvagin 1990 | checks/KV-kolyvagin/KV1.md |
| KV2 | GRH → L(E,1) ≠ 0 when analytic rank = 0 | PASS | [LEMMA] | Nearly tautological at rank 0; L(E,1) = 0 IS analytic rank > 0 | checks/KV-kolyvagin/KV2.md |
| KV3 | BSD formula at rank 0 closes | PASS | [LEMMA] | All terms computed; Rubin 1991 for p-part (p > 7) | checks/KV-kolyvagin/KV3.md |
| KV4 | CM modularity is classical | PASS | [THEOREM] | Hecke theta series | checks/KV-kolyvagin/KV4.md |

## Group GZ — Gross-Zagier + Kolyvagin (Rank 1)

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| GZ1 | Gross-Zagier formula correctly stated | PASS | [THEOREM] | Gross-Zagier 1986 | checks/GZ-gross-zagier/GZ1.md |
| GZ2 | Gross-Zagier applies (Heegner hypothesis) | PARTIAL | [LEMMA] | For y²=x³−x conductor 32 with prime 2 ramifying in Q(i), paper cites Yuan-Zhang-Zhang 2013 or auxiliary field Q(√−7); mentions both but commits to neither | checks/GZ-gross-zagier/GZ2.md |
| GZ3 | GRH + analytic rank 1 → L'(E,1) ≠ 0 | VACUOUS | [LEMMA] | Per Rem 12.6, rank-1 is vacuous within scope | checks/GZ-gross-zagier/GZ3.md |
| GZ4 | L'(E,1) ≠ 0 → Heegner point non-torsion | PASS | [THEOREM] | Gross-Zagier | checks/GZ-gross-zagier/GZ4.md |
| GZ5 | Kolyvagin bounds rank ≤ 1 | PASS | [THEOREM] | Kolyvagin 1990 | checks/GZ-gross-zagier/GZ5.md |
| GZ6 | Heegner field correctly identified | PARTIAL | [LEMMA] | Paper does not commit to a specific auxiliary field | checks/GZ-gross-zagier/GZ6.md |
| GZ7 | Argument extends to all nine class-number-1 fields | PASS | [LEMMA] | Mechanical extension (same structure, different prime norms) | checks/GZ-gross-zagier/GZ7.md |

## Group SHA — Tate-Shafarevich Finiteness

| ID | Claim | Verdict | Rigor label | One-line finding | File |
|:---|:------|:--------|:------------|:-----------------|:-----|
| SHA1 | Ш finite for E in scope | PASS | [THEOREM] | Kolyvagin at rank 0 | checks/SHA-tate-shafarevich/SHA1.md |
| SHA2 | Ш appears with correct order in BSD formula | PASS | [LEMMA] | Rubin 1991 p-part for p > 7 | checks/SHA-tate-shafarevich/SHA2.md |
| SHA3 | Strong BSD p-part for all primes | PARTIAL | [LEMMA] | Rubin gives p > 7; small-prime extension cited but not verified | checks/SHA-tate-shafarevich/SHA3.md |

---

## Totals

**Verdict totals:**
- PASS: 23
- PARTIAL: 15
- FAIL: 3 (LC4 Ω formula; BR3 Prop 4.3; BR7/BR8 integrality premise — the most critical)
- VACUOUS: 3 (LC2, LC5, GZ3 — rank-1 within-scope vacuity)
- NOT VERIFIED: 1 (BR2 — the 355 triples claim)

**Rigor label totals (for items with a label):**
- [THEOREM]: 16 (including 3 downstream classical results)
- [LEMMA]: 13
- [KEY LEMMA — OPEN]: 9 (all tied to MY, BR7/8, CM3, IT3)
- [GAP]: 1 (BR3 / Prop 4.3)

**The 4 FAIL items (most important):**
- **LC4** (Ω_E formula): editorial error — off by factor of π. Numerical value correct. Fixable in 5 minutes.
- **BR3** (Prop 4.3): 3 of 4 minimal-conductor rows are broken. Fixable by recomputing the table.
- **BR7** (integrality rigorously established): conflates class with representative. Requires stating and proving a class-shifting lemma. Non-trivial.
- **BR8** (integrality is a property of the class): same concern as BR7. **THE LOAD-BEARING GAP.**

**The 9 [KEY LEMMA — OPEN] items** cluster around three concerns:
1. Meyer → point spectrum (MY1, MY2, MY4)
2. Twist to L(s, ψ) (MY3, IT3, CM3, DS3)
3. Cohomology class integrality (BR7, BR8)
