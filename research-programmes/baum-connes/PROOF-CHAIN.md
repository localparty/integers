# PROOF-CHAIN -- Baum-Connes for the BC Algebra

*The Baum-Connes assembly map mu: K_*(BG) -> K_*(C*_r(G)) is an isomorphism for G = Q*/Z* (s.d.p.) N* acting on the BC algebra. Guaranteed by amenability (Higson-Kasparov 2001); the work is making it explicit and extracting K-theoretic constraints on spectral structure.*
*Status: 1/6 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | Group identification: G = Q*/Z* (s.d.p.) N* acting on A_BC | KNOWN | -- |
| 2 | Classifying space BG for proper G-actions | OPEN | 1 |
| 3 | K-homology K_*(BG) via Atiyah-Hirzebruch spectral sequence | OPEN | 2 |
| 4 | K-theory K_*(C*_r(G)) via Pimsner-Voiculescu | OPEN | -- |
| 5 | Assembly map mu: isomorphism (follows from amenability) | OPEN | 3, 4 |
| 6 | K-theoretic constraints on spectral structure via Chern character -> cyclic cohomology -> Connes trace formula | OPEN | 5 |

## Current wall
**Links 3-4 (K-theory computation).** Computing K_*(BG) and K_*(C*_r(G)) explicitly for the BC semigroup group. The semigroup structure complicates the classifying space (need Luck's approach). Link 6 (the payoff: K-constraints on spectral data) requires new ideas beyond standard Baum-Connes machinery.

## Programme graph edges
- **QG5D (Paper 1):** spectral triple (A,H,D) on BC algebra encodes 5D geometry
- **YM (Paper 8):** anomaly cancellation index(D_A)=0 is a K-theory pairing
- **RH (Paper 13):** Chern character -> cyclic cohomology -> Connes trace formula -> zeros
- **Hodge (Paper 29):** which K-theory classes come from algebraic vector bundles?
- *Universal connector:* K-theory is the receptacle for all index-theoretic invariants
