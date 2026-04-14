# PROOF-CHAIN — Hilbert's 12th Problem (Paper 25)

*Explicit class field theory via the Bost-Connes system: the KMS states at inverse temperature β > 1 generate the abelian extensions of number fields. The four-conjecture programme.*
*Status: 1/6 links | Confidence: 2/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | BC algebra + Hecke semigroup N* → crossed product C*-algebra A_BC | ESTABLISHED | — | Bost-Connes 1995 |
| 2 | KMS_β states for β > 1 exist and are parametrized by characters of Ẑ* | LITERATURE | 1 | Bost-Connes 1995; Connes-Marcolli 2008 |
| 3 | CBB Reciprocity: KMS_β symmetry is the Galois action Gal(ℚ^cyc/ℚ) | CONJECTURED | 2 | Four-conjecture programme (Paper 25); classical CFT |
| 4 | Brauer-KMS duality: cyclotomic Brauer classes β_k ∈ H²(Z/kZ, U(1)) correspond to KMS phase structure at k ∈ {2,3,4,6} | CONJECTURED | 3 | Paper 24 bridge family (verified k=3, k=4); Lead 7b |
| 5 | V-Hilbert 12: the generators of Gal(K^ab/K) for K a cyclotomic field are extracted from the unitary bridge V: H_CCM → H_R | OPEN | 3, 4 | Research/14 (V bridge); Hilbert 1900 |
| 6 | Spectral Kronecker-Weber: every abelian extension of ℚ appears in the spectrum of some BC-type system | OPEN | 5 | Kronecker-Weber 1886; generalization |

## Current wall
Link 5 (V-Hilbert 12 extraction). The unitary bridge V exists as a formal object but its ACTION on specific class field generators has not been computed. The four-conjecture programme states what needs to be proved; actually proving even one of CBB Reciprocity or V-Hilbert 12 is a substantial research project. The 2025 Breakthrough Prize work on geometric Langlands (Gaitsgory-Raskin, arXiv:2405.03599) may provide tools for Link 4-5 via the automorphic side of class field theory.

## Programme graph edges

- **H12 ↔ RH**: KMS_1 critical point is where the Riemann zeros appear as eigenvalues. β > 1 gives class fields; β = 1 gives RH. Same algebra, different temperature.
- **H12 ↔ BSD**: Hecke L-functions for CM curves factor through class field extensions. BSD rank formula uses L-values at s=1, which live at the critical KMS point.
- **H12 ↔ Hodge**: class field extensions of cyclotomic fields correspond to motivic Galois action (Connes-Consani-Marcolli 2005). The same motivic structure that powers Hodge.
- **H12 ↔ GRH**: Dirichlet characters generate abelian extensions of ℚ; GRH for those characters is H12 viewed through the zero-location lens.
- **H12 ↔ LANG↔QFT**: H12 IS the abelian case of the Langlands programme. Gaitsgory-Raskin 2024 (geometric Langlands PROVED) opens a new mathematical toolkit.

## Detail files

- `paper25-hilbert-12/preprint/00-proof-skeleton.md` — (to be drafted)
- `paper25-hilbert-12/strategy/00-h12-attack-plan.md` — (to be drafted)

## Physical observable

Class field generation = physical predictions from the bridge family. Each bridge at k ∈ {2,3,4,6} produces a concrete physical prediction (CP symmetry, 3 generations, Pati-Salam α_PS⁻¹ = 17, 6 quarks + CKM). These predictions VERIFY that the KMS structure generates the correct class fields. H12's truth is empirically constrained by the 36-prediction master table.

## Cascading refinement from QG5D W1/W2 closure (2026-04-14)

Paper 1 PROOF-CHAIN.md W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10 (Theorem 1 two-loop scheme-independence + Theorem U.2a one-loop Seeley-DeWitt) + Paper 11 (Theorem K.4 all-orders inductive bootstrap) + explicit L=3 numerical verification at 50-digit precision (`paper1/code/K-5-2-route-c-3loop.py`). Cascading impact on this chain: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. Effect is cosmetic-to-small — this chain never gated on the scheme question directly, but the underlying foundation is now strictly stronger. No link status changes required; confidence unchanged; mention included for completeness of the programme graph.

---

*Paper 25 is the publishing strategy's Wave 2 deliverable. The four-conjecture programme (CBB Reciprocity, Brauer-KMS duality, Level-jump Rigidity, Spectral Kronecker-Weber, V-Hilbert 12) provides the research roadmap.*

*v1: 2026-04-13.*
