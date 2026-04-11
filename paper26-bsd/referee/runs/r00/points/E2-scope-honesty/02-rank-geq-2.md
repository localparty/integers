## Point E2(b): Rank >= 2

**The question:**
Is the rank >= 2 limitation correctly scoped?

**Finding:**
Section 15.2 correctly identifies that the bridge provides GRH for ALL CM curves regardless of rank, but Kolyvagin's Euler system only handles rank 0 and 1. For rank >= 2, higher Heegner cycles (Zhang's programme) or Bloch-Kato would be needed.

This is accurate. The limitation is in the downstream machinery, not in the bridge.

As noted in Point D2(b), there is a question of whether CM curves over Q with CM by class-number-1 fields can have rank >= 2 over Q. If GRH for L(s, psi) implies L(1, psi) != 0, then all such curves have analytic rank 0, and rank >= 2 cannot occur. In this case, the rank >= 2 limitation is moot.

**Verdict for this sub-question:**
SOUND -- The limitation is correctly identified. It may be moot if rank >= 1 does not occur for the curves in scope.
