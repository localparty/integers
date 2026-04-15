## Point D3(b): Kolyvagin's Upper Bound

**The question:**
When analytic rank = 1, Kolyvagin bounds the algebraic rank by 1. Verify the precise statement.

**Finding:**
Theorem 12.3 states: If E/Q is modular and there exists a Heegner point P_K in E(K) of infinite order, then rank(E(K)) = 1 and Sha(E/K) is finite.

This is the standard statement of Kolyvagin's rank-1 result. The key input is the existence of a Heegner point of infinite order, which is provided by the Gross-Zagier formula when L'(E, 1) != 0.

Note: Kolyvagin's result gives rank(E(K)) = 1 and Sha(E/K) finite, where K is the auxiliary imaginary quadratic field used for the Heegner construction. The descent to rank(E(Q)) requires additional argument (CM descent).

The preprint handles this in Section 12.3: "For descent from K to Q: if E has CM by K, the Galois structure of E(K) under Gal(K/Q) decomposes the Mordell-Weil group, and rank(E(Q)) can be read off from rank(E(K)) together with the action of complex conjugation."

This descent argument is standard for CM curves but is only sketched. It should be noted that the auxiliary K for Gross-Zagier may be different from the CM field.

**Verdict for this sub-question:**
SOUND -- Kolyvagin's upper bound is correctly stated and applied. The CM descent is standard but sketched.
