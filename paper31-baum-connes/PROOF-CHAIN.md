# PROOF-CHAIN -- Baum-Connes for the BC Algebra (Paper 31)

*The Baum-Connes assembly map mu: K_*(BG) -> K_*(C*_r(G)) is an isomorphism for G = Q*/Z* (s.d.p.) N* acting on the BC algebra. The work is making it explicit and extracting K-theoretic constraints on spectral structure.*
*Status: 1/6 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Identify G = Q*/Z* (s.d.p.) N* acting on BC algebra | ESTABLISHED | -- | Bost-Connes 1995 |
| 2 | Compute classifying space BG for proper G-actions | OPEN | 1 | Standard algebraic topology (Luck's approach for semigroups) |
| 3 | K-homology K_*(BG) via AHSS | OPEN | 2 | Atiyah-Hirzebruch spectral sequence |
| 4 | K-theory K_*(C*_r(G)) | OPEN | -- | **Cuntz-Li method for semigroup C*-algebras -- directly applicable to BC algebra's Hecke semigroup N*** |
| 5 | Assembly map mu is isomorphism | OPEN | 3, 4 | **Dec 2025: proved for relatively hyperbolic groups (arXiv:2512.21169) -- check if BC's group is in this class** |
| 6 | K-theoretic constraints on spectral structure | OPEN | 5 | Chern character -> cyclic cohomology -> Connes trace formula |

## Current wall
**Links 3-4 (K-theory computation).** Computing K_*(BG) and K_*(C*_r(G)) explicitly for the BC semigroup group. The Cuntz-Li method for semigroup C*-algebras is directly applicable to the Hecke semigroup N* and provides the best route to Link 4. For Link 5, the Dec 2025 result (arXiv:2512.21169) proves Baum-Connes for relatively hyperbolic groups -- determining whether Q*/Z* (s.d.p.) N* falls in this class would close Link 5 immediately.

## Programme graph edges
- **QG5D (paper1):** spectral triple (A,H,D) on BC algebra encodes 5D geometry
- **YM (paper08-yang-mills):** anomaly cancellation index(D_A)=0 is a K-theory pairing
- **RH (paper13-rh):** Chern character -> cyclic cohomology -> Connes trace formula -> zeros
- **Hodge (paper29-hodge):** which K-theory classes come from algebraic vector bundles?
- **BGS (paper32-bgs-spectral-statistics):** K-theoretic constraints feed spectral statistics
- *Universal connector:* K-theory is the receptacle for all index-theoretic invariants
