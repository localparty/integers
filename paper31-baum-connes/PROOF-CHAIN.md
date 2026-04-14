# PROOF-CHAIN -- Baum-Connes for the BC Algebra (Paper 31)

*The Baum-Connes assembly map mu: K_*(BG) -> K_*(C*_r(G)) is an isomorphism*
*for G = Q*/Z* (s.d.p.) N* acting on the BC algebra.*
*The work is computing both sides explicitly and extracting K-theoretic*
*constraints on spectral structure.*

*Status: 1/6 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Identify G = Q*/Z* (s.d.p.) N* acting on BC algebra | ESTABLISHED | -- | Bost-Connes 1995 |
| 2 | Compute classifying space BG for proper G-actions | OPEN | 1 | Standard alg. topology (Luck for semigroups) |
| 3 | K-homology K_*(BG) via AHSS | OPEN | 2 | Atiyah-Hirzebruch spectral sequence |
| 4 | K-theory K_*(C*_r(G)) | OPEN | -- | **Cuntz-Li: semigroup C*-algebras -> directly applicable to N*** |
| 5 | Assembly map mu is isomorphism | OPEN | 3, 4 | **Dec 2025: proved for rel. hyperbolic groups (arXiv:2512.21169)** |
| 6 | K-theoretic constraints on spectral structure | OPEN | 5 | Chern -> cyclic cohomology -> Connes trace formula |

## Current wall

**Links 3-4 (explicit K-theory computation).** Two approaches:

1. **Link 4 via Cuntz-Li:** The Cuntz-Li method for semigroup C*-algebras
   is directly applicable to the BC algebra's Hecke semigroup N*. This
   computes K_*(C*_r(G)) without needing the classifying space first.

2. **Link 5 via Dec 2025 result:** The proof of Baum-Connes for relatively
   hyperbolic groups (arXiv:2512.21169) could close Link 5 immediately --
   but only if Q*/Z* (s.d.p.) N* is relatively hyperbolic. This group is
   amenable (Higson-Kasparov 2001 applies), so BC holds in principle;
   the issue is making the assembly map *explicit* enough for Link 6.

Link 6 (the payoff) requires new ideas beyond standard Baum-Connes:
extracting spectral constraints from K-theory via Chern character and
cyclic cohomology.

## Programme graph edges

- **QG5D (paper1):** spectral triple (A,H,D) on BC algebra encodes 5D geometry
- **YM (paper08-yang-mills):** anomaly cancellation index(D_A)=0 is a K-theory pairing
- **RH (paper13-rh):** Chern character -> cyclic cohomology -> Connes trace formula -> zeros
- **Hodge (paper29-hodge):** which K-theory classes come from algebraic vector bundles?
- **BGS (paper32-bgs-spectral-statistics):** K-theoretic constraints feed spectral statistics
- *Universal connector:* K-theory is the receptacle for all index-theoretic invariants
