## Check SC4: The claim matches what is proved -- no overstatement

**Group:** SC
**Source:** Abstract, Section 13
**Pass criterion (from prompt):** Verified by inspection.

**Verdict:** PARTIAL

**Justification:**
The main theorem (Theorem 13.1) claims BSD for CM curves with analytic rank 0 or 1. The proof establishes this for rank 0. For rank 1, there is a significant logical subtlety: if GRH for L(s, psi) implies L(1, psi) != 0 (as it should, since Re(1) = 1 != 1/2), then L(E, 1) = L(1, psi) * L(1, psi-bar) != 0 for ALL CM curves in scope, meaning all such curves have analytic rank 0. The rank-1 case would then be vacuously true.

The preprint should clarify whether CM curves over Q with CM by class-number-1 fields can have analytic rank >= 1 over Q. If not, the rank-1 machinery (Gross-Zagier) is vacuous and the statement should be simplified.

The "two Millennium Problems" framing in the abstract and conclusion is directionally accurate but risks overstatement, since the BSD result covers CM curves only (measure zero among all elliptic curves).

**Cross-references:**
- Per-Point file(s): points/D2-kolyvagin-rank0/02-grh-implies.md, points/E1-complete-chain/05-two-millennium.md
