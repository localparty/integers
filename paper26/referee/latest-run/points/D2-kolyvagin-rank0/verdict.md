## Point D2: Kolyvagin for Rank 0 -- Verdict

**Weight:** MEDIUM
**Overall verdict:** CLOSABLE GAP

**Sub-question verdicts:**
- (a): SOUND -- Kolyvagin correctly stated and applied.
- (b): CLOSABLE GAP -- Significant logical subtlety: GRH for L(s, psi) may imply ALL CM curves over Q have rank 0, making the rank-1 result vacuous. Needs clarification.
- (c): SOUND -- BSD formula at rank 0 verified numerically.

**Combined finding:**
Kolyvagin's theorem is correctly used for rank 0. The BSD formula verification is correct. However, there is a logical subtlety: if GRH for the Hecke L-functions L(s, psi) implies L(1, psi) != 0 (which it does, since Re(1) = 1 != 1/2), and if L(E, 1) = L(1, psi) * L(1, psi-bar), then L(E, 1) != 0 for ALL CM curves in scope. This would make the rank-1 case vacuously true.

Note: this does not invalidate the proof -- it strengthens it (all CM curves have rank 0 over Q). But the preprint's claim to prove BSD "for rank 0 and 1" is misleading if rank 1 never occurs in this setting.

**If this is a gap:**
- **Difficulty:** 1 paragraph of clarification
- **What is needed:** Determine whether CM curves over Q with CM by class-number-1 fields can have analytic rank >= 1. If not, state explicitly that the rank-1 case is vacuous.

**Impact on the claimed result:**
Does not invalidate any claim, but affects the scope description (Section 15). If rank 1 never occurs, the result is "BSD for CM curves over Q with CM by class-number-1 fields" without the rank qualifier -- which is actually a cleaner statement.
