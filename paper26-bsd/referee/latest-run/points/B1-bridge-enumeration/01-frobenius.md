## Point B1(a): The Frobenius Computation

**The question:**
For each Gaussian prime p, the Frobenius element Frob_p lives in Gal(K(zeta_N)/K). Is this correctly computed for all 355 triples?

**Finding:**
The Frobenius computation (Definition 4.1) defines Frob_p via the congruence Frob_p(zeta_N) = zeta_N^{N(p)} mod p. The order of Frob_p in (Z/N(N)Z)* determines the bridge index k = phi(N(N)) / ord(Frob_p).

The key verification is Lemma 4.4: for p = (3+2i) with N(p) = 13, Frob_{(3+2i)} = 13 = 6 = -1 mod 7, which has order 2 in (Z/7Z)*, giving k = phi(7)/2 = 3. This is correct: 13 mod 7 = 6 = -1, and (-1)^2 = 1, so the order is indeed 2.

For p = (1+i) with N(p) = 2: in (Z/3Z)*, 2 has order 2, so k = phi(3)/2 = 1. Wait -- this gives k = 1, but the table says k = 2 at conductor 3. Let me check: phi(3) = 2, ord(2 mod 3) = 2 (since 2^1 = 2, 2^2 = 4 = 1 mod 3). So k = phi(3)/ord(2) = 2/2 = 1, not 2.

This is a potential discrepancy. The table in Proposition 4.3 says k = 2 at ((1+i), (3)) with ord(2) = 1 in (Z/3Z)*. But ord(2 mod 3) = 2, not 1: 2^1 = 2 (not 1 mod 3), 2^2 = 4 = 1 mod 3. So ord = 2 and k = phi(3)/2 = 1.

However, the bridge definition restricts k to {2, 3, 4, 6}. If k = 1, this triple would not be a bridge triple. The table entry may contain an error in the stated order, or there may be a different convention for the Frobenius computation over K versus Q.

Actually, re-reading the table: it says "ord(2) = 1 in (Z/3Z)*" which is incorrect. Over Q, Frob_2 mod 3 has order 2 (as computed above). Over K = Q(i), the Frobenius at (1+i) in Gal(Q(i)(zeta_3)/Q(i)) may behave differently because Q(i) already contains certain roots of unity. Q(i) contains i but not zeta_3. So the Frobenius computation is: Frob_{(1+i)}(zeta_3) = zeta_3^{N(1+i)} = zeta_3^2. The order of zeta_3 -> zeta_3^2 is: (zeta_3^2)^1 = zeta_3^2, (zeta_3^2)^2 = zeta_3^4 = zeta_3, (zeta_3^2)^3 = zeta_3^6 = 1. So ord = 3. But Gal(Q(i)(zeta_3)/Q(i)) has order phi(3) = 2, so ord <= 2. Since zeta_3^2 = -1 - zeta_3 which is a conjugate of zeta_3, the Frobenius has order 2 in the Galois group. Then k = 2/2 = 1 again.

This issue needs computational verification. The stated k = 2 at this triple may be using a different convention. Without running the enumeration code, I flag this as requiring verification.

**Verdict for this sub-question:**
CLOSABLE GAP -- The specific table entry for ((1+i), (3)) with k = 2 appears to contain an error in the stated Frobenius order. The count of 355 bridge triples and the minimal conductor product 105 cannot be verified without running the enumeration code. The gap is closable by running the computational verification.
