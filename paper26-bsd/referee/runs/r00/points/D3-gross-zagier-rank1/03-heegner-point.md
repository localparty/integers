## Point D3(c): The Heegner Point Construction

**The question:**
Is the auxiliary imaginary quadratic field correctly identified?

**Finding:**
As noted in (a), for E: y^2 = x^3 - x with N = 32, the preprint proposes Q(sqrt{-7}) as the auxiliary field. The verification: 2 splits in Q(sqrt{-7}) because -7 = 1 mod 8 implies (2) = p1 * p2 in Z[(1+sqrt{-7})/2]. The only prime dividing N = 32 is p = 2, and it splits in Q(sqrt{-7}). So the Heegner hypothesis is satisfied.

The Heegner point is then constructed via the modular parametrization X_0(32) -> E and CM points on X_0(32) associated to Q(sqrt{-7}).

**However:** As identified in Point D2(b), there is a question of whether CM curves over Q with CM by class-number-1 fields can have analytic rank 1. If they cannot (because L(1, psi) != 0 implies L(E, 1) != 0), then this entire construction is vacuous -- there are no rank-1 curves to apply it to.

The Heegner point construction itself is standard and correct. The question is whether it is ever needed.

**Verdict for this sub-question:**
SOUND (the construction is correct) -- but potentially VACUOUS (the rank-1 case may not occur for CM curves over Q with CM by class-number-1 fields). See Point D2(b).
