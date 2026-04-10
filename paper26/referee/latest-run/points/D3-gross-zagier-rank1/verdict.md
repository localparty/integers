## Point D3: Gross-Zagier + Kolyvagin for Rank 1 -- Verdict

**Weight:** HEAVY
**Overall verdict:** CLOSABLE GAP (with significant caveat about vacuity)

**Sub-question verdicts:**
- (a): SOUND -- Heegner hypothesis correctly handled via Yuan-Zhang-Zhang or auxiliary field.
- (b): SOUND -- Kolyvagin's upper bound correctly stated.
- (c): SOUND but potentially VACUOUS -- Construction correct, but rank 1 may not occur.
- (d): CLOSABLE GAP -- No explicit numerical verification for rank-1 curve.
- (e): SOUND -- Uniform extension to nine fields.

**Combined finding:**
The Gross-Zagier + Kolyvagin machinery for rank 1 is correctly assembled. The Heegner hypothesis issue is carefully addressed. However, the most important finding is the question raised in D2(b): if GRH for L(s, psi) implies L(1, psi) != 0, then ALL CM curves in scope have analytic rank 0 over Q, and the entire rank-1 construction is vacuously true. The preprint should either confirm this vacuity or explain why rank 1 can occur.

**If this is a gap:**
- **Difficulty:** 1 paragraph clarification + potentially 1 page of analysis
- **What is needed:** Determine the set of CM curves over Q with CM by class-number-1 fields that have analytic rank >= 1 over Q. If this set is empty, state so explicitly.

**Impact on the claimed result:**
Does not invalidate the proof but significantly affects the scope claim. If rank 1 never occurs, the paper proves BSD for ALL CM curves over Q with CM by class-number-1 fields (not just rank 0 and 1) -- which is actually a stronger statement.
