## Point D3(a): The Gross-Zagier Formula

**The question:**
Does the Gross-Zagier formula apply to CM curves over Q(i)? Is the imaginary quadratic field for the Heegner point the same as the CM field, or must it be different?

**Finding:**
The Gross-Zagier formula (Theorem 12.1) requires an imaginary quadratic field K satisfying the Heegner hypothesis: every prime dividing the conductor N splits in K.

For E: y^2 = x^3 - x with conductor N = 32 = 2^5, the CM field is Q(i). The prime 2 RAMIFIES in Q(i) (not splits), so Q(i) itself does NOT satisfy the classical Heegner hypothesis for this curve.

The preprint (Section 12.2) addresses this correctly by providing two alternatives:
1. Use the generalized Gross-Zagier formula of Yuan-Zhang-Zhang (2013), which removes the Heegner hypothesis.
2. Use an auxiliary field Q(sqrt{-7}) (discriminant -7, coprime to 32), which satisfies the classical hypothesis since 2 splits in Q(sqrt{-7}) (because -7 = 1 mod 8).

Both approaches are valid. The Yuan-Zhang-Zhang generalization is a well-established result published in the Annals of Mathematics Studies.

**Critical subtlety:** The Heegner point P_K lives in E(K) where K is the auxiliary imaginary quadratic field used for the Gross-Zagier formula -- NOT necessarily the CM field. For the rank-1 argument, one needs P_K to have infinite order in E(Q), not just E(K). The CM descent argument (Section 12.3) handles this.

**Verdict for this sub-question:**
SOUND -- The Heegner hypothesis issue is correctly identified and resolved via Yuan-Zhang-Zhang or an auxiliary field. The treatment is careful and correct.
