# A3.01: The Four Cocycles

**k=2 at (2,7):** H^2(Z/2Z, U(1)) = Z/2Z. The Hasse invariant is 0, so the class is trivial. Both sides vanish. Correct and trivial.

**k=3 at (5,13):** ord_13(5) = 4, so k = phi(13)/4 = 3. The cyclic algebra has Hasse invariant 1/3 mod Z. The carry cocycle zeta_3^{floor((i+j)/3)} is correctly computed. The operator side (Jones subfactor at index 3 with outer Z/3Z action) produces the same carry cocycle. Pointwise identity verified on all 9 entries. This is the strongest bridge lemma.

**k=4 at (3,13):** ord_13(3) = 3, so k = 12/3 = 4. The paper computes the cosets explicitly: {1,3,9}, {2,5,6}, {4,10,12}, {7,8,11}. The generator tau = [2] has order 4 in the quotient. Hasse invariant 1/4 mod Z. The carry cocycle and coboundary check on all 64 triples are stated.

**k=6 at (7,19):** ord_19(7) = 3, so k = 18/3 = 6. Cosets explicitly computed. Hasse invariant 1/6 mod Z. Coboundary check on all 216 triples stated.

**Assessment:** The arithmetic computations (Frobenius orders, coset decompositions, Hasse invariants) are correct and verifiable. The operator side (Jones subfactors with outer cyclic group actions producing carry cocycles) relies on Ocneanu 1985 classification of outer actions on the hyperfinite II_1 factor.

**Concern:** The identification of the Fuglede-Kadison class with 1/k mod Z relies on a specific normalisation (Connes-Sukochev trace normalisation). The paper states this but does not derive it from first principles. For a proof of RH, every such identification must be airtight.

**Verdict: The k=3 lemma appears solid. The k=4 and k=6 lemmas follow the same template and appear correct, though they cite internal documents (research/263) rather than published references for full proofs.**
