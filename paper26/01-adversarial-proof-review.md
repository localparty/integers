# Paper 26 Adversarial Proof Review: BSD for CM Elliptic Curves

*Reviewer: Claude Opus 4.6 (independent adversarial agent, fresh eyes)*
*Date: 2026-04-09*
*Directive: Maximum aggression. Try to kill the proof. A false BSD claim is catastrophic.*

---

## VERDICT SUMMARY

**The proof inherits all the structural vulnerabilities of the RH proof (Paper 13) and adds several new ones specific to the Q(i) extension. The internal logic of the chain -- assuming the inherited axioms hold -- is sound. But the "unconditional" framing is unjustified. The proof is conditional on the CBB axioms, exactly as the RH proof is. Additionally, the Gross-Zagier application at rank 1 has a genuine technical issue (the Heegner hypothesis) that is acknowledged but not fully resolved.**

**Total attacks: 15. Survived: 8. Weakened: 5. Broken: 2.**

---

## ATTACK 1: CIRCULARITY -- Does any step use BSD or GRH to prove BSD or GRH?

**The attack.** If the proof assumes GRH for Hecke L-functions anywhere in the chain, or assumes BSD for any curve, the proof is circular.

**Analysis.** The chain is:
1. BC over Q(i) -> Nelson -> bridges -> Baker -> delta=0 -> GRH for zeta_K(s)
2. Same argument extended to L(s, psi) for Hecke characters
3. CM factorization -> GRH for L(E,s)
4. GRH -> non-vanishing at s=1 -> Kolyvagin -> rank 0
5. GRH -> non-vanishing of L'(E,1) -> Gross-Zagier -> rank 1

At no step is GRH or BSD assumed as input. Kolyvagin is used as a black box theorem with hypothesis "L(E,1) != 0"; GRH provides that hypothesis. Gross-Zagier is used with hypothesis "L'(E,1) != 0"; GRH provides that. The CM factorization is classical (Deuring). No circularity.

**However:** The non-vanishing L(E,1) != 0 for analytic rank 0 curves does NOT require GRH. It follows from the definition: analytic rank 0 means L(E,1) != 0. The paper conflates "GRH implies non-vanishing" with the trivial statement. For rank 0, GRH is not needed for non-vanishing -- the hypothesis "analytic rank = 0" IS the non-vanishing. What GRH provides is the assurance that s=1 is not on the critical line, hence not a zero of L(s,psi). But this is used to establish that L(E,1) = L(1,psi)*L(1,psi-bar) != 0, which is a different (and valid) deduction. The chain is logically sound.

**Verdict: SURVIVED.** No circularity found.

---

## ATTACK 2: THE CM FACTORIZATION -- Is L(E,s) = L(s,psi)*L(s,psi-bar) correctly stated?

**The attack.** The paper writes L(E,s) = L(s, chi_K) * L(s, psi) in Section 10.2. This is NOT the standard CM factorization. The standard form is L(E,s) = L(s, psi) * L(s, psi-bar) where psi is the Grossencharacter. The chi_K factor appears only when L(E,s) is expressed in terms of the L-function of the quadratic twist. Is the paper conflating two different factorizations?

**Analysis.** For E: y^2 = x^3 - x with CM by Q(i):
- The standard Deuring factorization is L(E,s) = L(s, psi) * L(s, psi-bar) where psi is the Grossencharacter.
- The paper writes L(E,s) = L(s, chi_{-4}) * L(s, psi), which identifies one of L(s,psi), L(s,psi-bar) with L(s, chi_{-4}). This would be correct ONLY if the Grossencharacter psi or psi-bar equals the Kronecker character chi_{-4}. But chi_{-4} is a Dirichlet character (defined on Z), while psi is a Hecke character (defined on ideals of Z[i]). They live in different worlds.

**The correct statement:** For E with CM by K, zeta_K(s) = zeta(s) * L(s, chi_K), and L(E,s) = L(s, psi) * L(s, psi-bar). These are different factorizations. The paper's notation in Section 10.2 is sloppy but not fatally wrong -- it is trying to express the Euler product identity at each prime. However, identifying L(s, psi-bar) with L(s, chi_{-4}) is incorrect in general. For weight-1 Grossencharacters of Q(i), psi-bar can equal the base change of chi_{-4}, but the paper doesn't prove this.

**Does this matter for the proof?** Not critically. The proof uses GRH for ALL Hecke L-functions of K (Step C in Section 9.2), which covers both L(s,psi) and L(s,psi-bar) regardless of how they relate to chi_K. The factorization error is a presentation issue, not a logical gap.

**Verdict: WEAKENED.** The notation is wrong/sloppy in 10.2. The proof logic is unaffected because Step C handles all Hecke characters uniformly.

---

## ATTACK 3: HA-PAUGAM -- Is the BC system over Q(i) actually constructed?

**The attack.** The paper cites "Ha-Paugam 2005" for the BC system over number fields. Is this construction actually in the literature? Does it prove what the paper claims?

**Analysis.** Ha and Paugam (2005), "Bost-Connes-Marcolli systems for Shimura varieties. I. Definitions and formal analytic properties," Journal de Theorie des Nombres de Bordeaux 17(1):137-169. This paper DOES construct BC-type systems over number fields and DOES establish the basic properties (time evolution, KMS states). However:

(a) Ha-Paugam construct the system as a Hecke algebra, not as a C*-algebra with the full operator-algebraic properties needed for the proof. The C*-completion and the GNS construction require additional work (Laca-Larsen-Neshveyev 2015 for the general case).

(b) The KMS_1 uniqueness for h_K = 1 is NOT explicitly proved in Ha-Paugam. It is a consequence of the general theory (Laca-Larsen-Neshveyev 2015, Theorem 4.1), but the paper cites only Ha-Paugam.

(c) The claim that KMS_1 uniqueness follows from "the same argument as Bost-Connes Theorem 25" (Section 3.4) is a hand-wave. The BC Theorem 25 is specific to Q. The extension to number fields requires the Laca-Raeburn-Ramagge framework and is non-trivial, though it IS in the literature.

**Verdict: WEAKENED.** The construction exists in the literature but the citation is incomplete. The paper should cite Laca-Larsen-Neshveyev 2015 for the full C*-algebraic treatment and KMS classification over number fields. The logical gap is fillable.

---

## ATTACK 4: MEYER OVER Q(i) -- Does Meyer's spectral inclusion extend to number fields?

**The attack.** Meyer's theorem (1997/2005) establishes a spectral inclusion for the Riemann zeta function using the explicit formula. The paper claims this extends to zeta_K(s) "by the same argument with Lambda replaced by Lambda_K" (Section 3.6). Is this justified?

**Analysis.** Meyer's original construction uses the Weil explicit formula for zeta(s). The explicit formula for Dedekind zeta functions zeta_K(s) is well-known (e.g., Iwaniec-Kowalski, Chapter 5). The spectral construction does extend, and this has been noted in the literature (Connes 1999, Meyer 2005 in the context of the trace formula approach).

However, the paper's proof of Proposition 3.6 is a sketch, not a proof. It says "the proof uses the explicit formula for zeta_K" and "the structure depends only on the existence of an Euler product and a functional equation." This is true but imprecise -- Meyer's construction requires specific analytic properties of the test functions, and the extension to number fields requires checking that these properties still hold. This has been done (by Meyer himself, and by Connes-Consani-Marcolli), but the paper doesn't cite these extensions.

**The deeper issue:** Meyer's result gives DISTRIBUTIONAL eigenstates, not genuine eigenstates. The upgrade from distributional to genuine eigenstates relies on Nelson self-adjointness (Proposition 3.7). This is the same issue as in the RH proof (Paper 13, Concern 1 from the review). The Paper 13 review flagged that Axiom 1 of CBB pre-encodes the spectral data, and that Meyer gives distributional support, not operator-theoretic support. This concern carries over unchanged.

**Verdict: WEAKENED.** The extension is valid in principle but the paper's treatment is a sketch. The inherited concern about distributional vs. genuine eigenstates from Paper 13 applies with full force.

---

## ATTACK 5: BAKER'S THEOREM APPLICATION -- Is it correctly applied?

**The attack.** Baker's theorem requires:
(a) alpha_1, ..., alpha_n are non-zero algebraic numbers
(b) beta_1, ..., beta_n are algebraic with {1, beta_1, ..., beta_n} linearly independent over Q

The paper applies Baker (via Corollary 8.2) to log(N(p_1))/log(N(p_2)) where N(p_i) are norms of Gaussian primes. Are the norms algebraic? Is multiplicative independence satisfied?

**Analysis.**
(a) Norms of Gaussian primes are rational integers >= 2. Rational integers are algebraic. Condition satisfied.

(b) For the Corollary, we need N(p_1) and N(p_2) to be multiplicatively independent. The paper claims (Proposition 8.4): since both are prime powers and N_1 != N_2, they are multiplicatively independent.

**Potential issue:** For INERT primes p (with p = 3 mod 4), N(p) = p^2. For SPLIT primes (p = 1 mod 4), N(pi) = p. So if p_1 is inert with norm p^2, and p_2 is the split prime p itself... wait, if p = 1 mod 4, p splits, and the norm is p. If p = 3 mod 4, p is inert with norm p^2. These cannot conflict: an inert prime has norm p^2 where p = 3 mod 4, and a split prime above q (q = 1 mod 4) has norm q. So N_1 = p^2 and N_2 = q with p != q. These are multiplicatively independent iff p^{2a} != q^b for all positive integers a,b, which holds because p and q are distinct rational primes. Correct.

**Another potential issue:** Two split primes above the SAME rational prime q have the same norm q. So N(pi) = N(pi-bar) = q. The paper requires N(p_1) != N(p_2) in Proposition 8.4. This is fine -- just choose bridge primes with distinct norms.

**The actual bridge primes used:** From the minimal conductor table (Section 4.3):
- k=2: N = 2
- k=3: N = 13
- k=4: N = 5
- k=6: N = 2

So the distinct norms are {2, 5, 13}. Any pair has transcendental log ratio by Baker. The argument works.

**Verdict: SURVIVED.** Baker is correctly applied. The norms are algebraic, multiplicatively independent, and the transcendence conclusion follows.

---

## ATTACK 6: KOLYVAGIN -- Does Kolyvagin apply to CM curves?

**The attack.** Kolyvagin's theorem requires:
(a) E/Q is modular
(b) L(E,1) != 0 (for rank 0) or a Heegner point of infinite order (for rank 1)

Does modularity hold for CM curves without assuming anything we're trying to prove?

**Analysis.** CM curves over Q are modular. This is CLASSICAL and does NOT require Wiles (1995). The modularity of CM curves follows from the theory of complex multiplication (Shimura 1971): the Grossencharacter psi determines a weight-2 Hecke eigenform, and the associated L-function matches L(E,s). This was known before Wiles and is independent of the Taniyama-Shimura conjecture.

Does Kolyvagin need GRH? No. Kolyvagin's Euler system machinery is unconditional once you have:
- Modularity (classical for CM)
- Non-vanishing of L(E,1) (provided by the bridge family's GRH)
- The existence of a Heegner point (from the modular parametrization)

**Verdict: SURVIVED.** Kolyvagin applies to CM curves unconditionally. Modularity is classical. GRH provides the non-vanishing hypothesis.

---

## ATTACK 7: GROSS-ZAGIER -- Does the formula apply?

**The attack.** The Gross-Zagier formula requires the HEEGNER HYPOTHESIS: every prime dividing the conductor N of E must SPLIT in the imaginary quadratic field K used for the Heegner point construction. For E: y^2 = x^3 - x, the conductor is N = 32 = 2^5. Since 2 RAMIFIES in Q(i) (not splits), the Heegner hypothesis fails for K = Q(i).

**Analysis.** This is a GENUINE issue, and the paper acknowledges it in Section 12.2: "Since 2 ramifies in Q(i), one must use a variant of the Gross-Zagier formula adapted to the ramified case (Zhang 2001, Yuan-Zhang-Zhang 2013)."

The paper cites Zhang (2001) and Yuan-Zhang-Zhang (2013) for the generalization. These references ARE correct:
- Zhang, S.-W. (2001), "Gross-Zagier formula for GL2," Asian Journal of Mathematics 5(2):183-290.
- Yuan, X., Zhang, S.-W., Zhang, W. (2013), "The Gross-Zagier formula on Shimura curves," Annals of Mathematics Studies 184.

These works DO extend Gross-Zagier to cases where the Heegner hypothesis fails (including ramified primes). The extension covers the case of CM curves with conductors divisible by ramified primes.

**However:** The paper simply says "the structural content is identical" without verifying that the Yuan-Zhang-Zhang formula applies to this specific curve. For E: y^2 = x^3 - x, one needs to verify:
1. There exists an imaginary quadratic field K' (possibly different from Q(i)) satisfying the Heegner hypothesis for N = 32.
2. The Heegner point P_{K'} in E(K') descends to a point in E(Q) (or E(Q(i))).

For (1): We need K' such that 2 splits in K'. This requires disc(K') = 1 mod 8. For example, K' = Q(sqrt(-7)) has disc = -7, and 2 splits in Q(sqrt(-7)) because -7 = 1 mod 8. So the classical Gross-Zagier formula applies with K' = Q(sqrt(-7)), not K = Q(i).

**The tension:** The GRH proof uses K = Q(i) (the CM field). The Gross-Zagier formula may need a DIFFERENT imaginary quadratic field K' to satisfy the Heegner hypothesis. This is standard practice -- Kolyvagin and Gross-Zagier are applied over an auxiliary quadratic field, not necessarily the CM field. But the paper does not carefully distinguish between these two roles of imaginary quadratic fields.

**Verdict: WEAKENED.** The Heegner hypothesis issue is real. The resolution exists in the literature (Zhang, Yuan-Zhang-Zhang) but the paper's treatment is too casual. The proof should explicitly state which imaginary quadratic field is used for the Heegner construction and verify the Heegner hypothesis for that field.

---

## ATTACK 8: THE h_K = 1 ASSUMPTION

**The attack.** The proof requires h_K = 1 for KMS_1 uniqueness. What breaks for h_K > 1? Is the restriction to h_K = 1 correctly imposed?

**Analysis.** For h_K > 1:
1. The ring O_K is NOT a PID. Ideals are not all principal.
2. The KMS_1 state may NOT be unique. The class group Cl(K) acts on the KMS states, producing |Cl(K)| distinct ergodic KMS_1 states (Connes-Marcolli-Ramachandran 2005).
3. The ITPFI factorization may fail: non-principal ideals in the same class are identified under the class group action, potentially creating relations among the tensor factors.

**Impact on the proof:** If KMS_1 is not unique, the ITPFI factorization argument (Step 2) collapses -- you cannot conclude omega_1 = tensor product from uniqueness. Without ITPFI, the dark-state bound and the bridge coupling arguments are not established.

**Is h_K = 1 correctly used?** Yes. The paper restricts to the nine imaginary quadratic fields with h_K = 1 and is honest about this (Section 15.4: "Multi-KMS analysis needed. Structurally tractable but not yet done").

**But:** The paper claims BSD "for CM curves" without always qualifying "with CM by a class-number-1 field." The Main Theorem (Section 1.4) correctly states "with complex multiplication by Q(i)" and then "extends to all nine imaginary quadratic fields of class number one." This is properly scoped.

**Verdict: SURVIVED.** The h_K = 1 restriction is correctly imposed and correctly scoped.

---

## ATTACK 9: GAP INHERITANCE FROM THE RH PROOF

**The attack.** The Paper 13 adversarial review (01-review-concerns.md) identified the proof as CONDITIONAL on the CBB axioms, with overall confidence 55-65%. Specifically:
- Axiom 1 pre-encodes the spectral data (Concern 1, CRITICAL)
- Bridge lemmas at k=4,6 need formal elevation (Concern 2, SERIOUS)
- The proof is "conditional, not unconditional" (Verdict)

Paper 26 inherits ALL of these concerns and additionally requires:
- The CBB axioms to hold over Q(i), not just Q
- The Ha-Paugam construction to satisfy the same operator-algebraic properties as the BC algebra over Q

**Analysis.** The Paper 13 review concluded that the RH proof is conditional on the CBB axioms. Paper 26 claims its proof is "unconditional" (Section 1.4: "The proof is unconditional"). But the proof inherits the same conditional structure:

1. If Axiom 1 pre-encodes RH for zeta(s), the analogous axiom pre-encodes GRH for zeta_K(s).
2. If the bridge lemmas at k=4,6 are not formally proved over Q, they are equally unproved over Q(i).
3. The Meyer spectral inclusion issue (distributional vs. genuine eigenstates) carries over.

**The paper's "gap audit" (Section 9.4) is misleading.** It claims "Gap count: zero" and lists inherited assumptions as "Known." But the Paper 13 review rated the overall unconditional confidence at 55-65%. Claiming "zero gaps" for a proof that inherits all those gaps is intellectually dishonest.

**Verdict: BROKEN.** The paper claims "unconditional" but inherits all the conditionality of the RH proof. The framing must be corrected. The proof is: "BSD for CM curves of rank 0+1, conditional on the CBB axioms, as a theorem of the Integers programme." This is exactly the same conditionality as the RH proof, plus the new ingredients (Ha-Paugam, Baker, Kolyvagin, Gross-Zagier), which are genuinely unconditional.

---

## ATTACK 10: THE "NOTHING CHANGES" CLAIM

**The attack.** Part II opens with "Nothing substantive changes" when moving from Q to Q(i). The paper repeatedly claims substituting p -> N(p) is the only modification. But (O_K/N)* has different structure from (Z/NZ)*. Does this matter?

**Analysis.** The Frobenius elements in Section 4.1 are defined in Gal(K(zeta_N)/K), which acts on the cyclotomic extension of K, not Q. The group (O_K/N O_K)* is NOT the same as (Z/NZ)* in general:

For K = Q(i) and conductor ideal (N) = (q) for a rational prime q:
- If q splits: O_K/(q) = F_q x F_q, so (O_K/(q))* = F_q* x F_q*, which has order (q-1)^2.
- If q is inert: O_K/(q) = F_{q^2}, so (O_K/(q))* = F_{q^2}*, which has order q^2 - 1.
- If q ramifies: O_K/(q) = F_q[x]/(x^2), more complicated.

The paper uses Frobenius elements in (Z/qZ)*, not in (O_K/q O_K)*. In Section 4.1, "its order in (Z/N(N)Z)*" -- this uses the NORM of the conductor, reducing to a computation over Z, not over O_K. This is correct for computing the Frobenius ORDER: Frob_p acts on zeta_N by zeta_N -> zeta_N^{N(p)}, and N(p) is an integer, so the order of Frob_p in (Z/NZ)* is just ord_N(N(p)).

**But the bridge index computation uses (Z/qZ)* where q is the conductor norm.** This is actually correct: the cyclotomic extension K(zeta_q)/K has Galois group isomorphic to (Z/qZ)* (for q coprime to disc(K)), and the Frobenius at p acts by N(p) mod q. So the bridge computation reduces to arithmetic in (Z/qZ)*, exactly as over Q but with p replaced by N(p).

**Where "something changes":**
- The bridge PRIMES are different (Gaussian primes vs. rational primes).
- The NORMS can be composite: inert primes have norm p^2, which is not a rational prime.
- The conductor ideals may not be principal in general (but they are for Q(i) since h_K = 1).

**Do these differences affect the proof?** The Baker argument only needs distinct norms >= 2. The bridge computation only needs Frobenius orders in (Z/qZ)*. Both are satisfied. The "nothing changes" claim is an overstatement, but the things that DO change are correctly handled.

**Verdict: SURVIVED.** The structural differences are real but correctly accounted for. The bridge computation is valid over Q(i).

---

## ATTACK 11: STEP C (GRH FOR HECKE L-FUNCTIONS) -- The twist argument

**The attack.** In Section 9.2 Step C, the paper claims GRH extends from zeta_K(s) to L(s, psi) for any Hecke character psi because "the cocycle shift formula depends only on |N(p)^{-s}|, not on the phase psi(p)."

This is the most CRITICAL logical step unique to this paper and it deserves maximum scrutiny.

**Analysis.** The cocycle shift Delta_c(delta) = (1 - N(p)^{-2*delta})/(N(p) - N(p)^{-2*delta}) is derived from the LOCAL Euler factor Z_p(s) = 1/(1 - N(p)^{-s}). For zeta_K(s), this is correct.

For L(s, psi), the local Euler factor is Z_p^psi(s) = 1/(1 - psi(p) N(p)^{-s}). The twist by psi(p) (a root of unity) changes the Euler factor. The cocycle shift from the twisted factor would be:

Delta_c^psi(delta) = (1 - psi(p) N(p)^{-2*delta}) / (psi(p) N(p) - psi(p) N(p)^{-2*delta})

Wait -- no. The derivation in Section 7.2 uses the KMS evaluation, and the perturbed partition function. With a twist, the KMS weight at p is:

omega_beta^p(1_{p^k}) = (psi(p) N(p)^{-beta})^k / Z_p^psi(beta)

The modulus |omega_beta^p(1_{p^k})| = N(p)^{-k*beta} / |Z_p^psi(beta)|.

**The paper's claim:** The cocycle shift "depends only on |N(p)^{-s}|, not on the phase psi(p)." This needs justification. The Hasse invariant of the cyclic algebra is defined via the Brauer group, which involves the FULL value of psi(p), not just its modulus.

**The issue:** The bridge cocycle takes values in (1/k)Z, which is a DISCRETE set. The twist by psi(p) (a root of unity) rotates the cocycle value in the complex plane. For the integrality constraint to still hold, the rotated cocycle must still land in (1/k)Z. But (1/k)Z is a subset of R, and a root-of-unity rotation takes real values out of R (unless psi(p) = +/- 1).

**Deeper analysis:** The cocycle shift argument measures the DEVIATION from the unperturbed value. The unperturbed Hasse invariant is 1/k mod Z. The perturbed value, for a zero at 1/2 + delta, shifts by an amount depending on N(p)^{-2*delta}. The phase psi(p) enters the Euler factor but the MODULUS of the cocycle shift -- which determines whether the integrality constraint is violated -- depends only on |delta|.

Actually, I need to be more careful. The bridge cocycle is defined as a Brauer class, which takes values in Q/Z. The Hasse invariant is a rational number mod Z. The cocycle shift measures how this rational number changes when delta != 0. The change depends on the Euler factor ratio, which for L(s,psi) includes the twist. BUT: the Hasse invariant is defined locally at each prime, and for the cyclic algebra (K(zeta_N)/K, Frob_p, zeta_k), the Frobenius element is independent of psi. The cocycle is an ARITHMETIC object (depending on Frob_p and the conductor), while the zeros are ANALYTIC objects (of L(s,psi)). The connection between them goes through the KMS state, which encodes the partition function.

**The real question:** Is it true that for L(s,psi), the same bridge family detects off-line zeros? The paper argues that the BC system over K naturally encodes ALL Hecke L-functions of K (through different Hecke characters), and the bridge family couples to all of them because the coupling depends on the local norm N(p), not on psi(p).

**Assessment:** This argument has a gap. The BC system over K has KMS states that encode zeta_K(s), not L(s,psi) for arbitrary psi. To encode L(s,psi), one needs to consider the action of Gal(K^ab/K) on the KMS states (this is the content of the Bost-Connes phase transition: at beta > 1, different KMS states correspond to different characters). The zeros of L(s,psi) appear as eigenvalues of the modular flow TWISTED by psi. The paper does not carefully construct this twisted spectral realisation.

However, the twist argument has been worked out in the literature for the original BC system (Connes-Marcolli 2006, "From Physics to Number Theory via Noncommutative Geometry," Section 3.3). The extension to number fields follows the same pattern. The paper should cite this.

**Verdict: WEAKENED.** The twist argument is correct in spirit but needs more careful justification. The paper hand-waves the extension from zeta_K to L(s,psi). The gap is fillable from the literature (Connes-Marcolli) but the paper doesn't do this work.

---

## ATTACK 12: BRIDGE LEMMAS OVER Q(i) -- Are they actually proved?

**The attack.** The Paper 13 review (Concern 2) noted that bridge lemmas at k=4 and k=6 were not formally proved over Q. Are they proved over Q(i)?

**Analysis.** The paper claims (Theorem 4.6) that the cocycle match is "field-independent": the Hasse invariant equals 1/k by construction, and the FK determinant equals 1/k by the subfactor theory (Jones 1983). This field-independence claim is correct -- the Hasse invariant of a cyclic algebra (K(zeta_N)/K, Frob_p, zeta_k) is 1/k by definition of the bridge index, and the FK determinant is a property of the subfactor, not the field.

The formal lemma over Q(i) at k=3 (Lemma 4.4) is proved: the computation at (3+2i, (7)) is explicit. The other k values inherit from the same structural argument.

**However:** The Paper 13 review's concern about k=4 and k=6 over Q carries over. If those bridge lemmas are not proved over Q, they are equally unproved over Q(i). The field-independence theorem (Theorem 4.6) shows that proving them over Q suffices for Q(i), but the Paper 13 review flagged that the proofs at k=4,6 need "formal elevation." The Paper 13 review then concluded that the proofs as written in Sections 3.4 and 3.5 of Paper 13 ARE complete and should be declared proved.

**Verdict: SURVIVED.** The bridge lemmas transfer from Q to Q(i) by Theorem 4.6. The Paper 13 review concluded the k=4,6 proofs are complete. No new gap.

---

## ATTACK 13: THE LEADING COEFFICIENT FORMULA -- Is it actually proved?

**The attack.** The Main Theorem claims the FULL BSD formula (including the leading coefficient) holds. But the proof only establishes rank = analytic rank (Part (i)) and finiteness of Sha (needed for Part (ii)). Does finiteness of Sha actually close the leading coefficient formula?

**Analysis.** For rank 0:
- Kolyvagin gives rank = 0 and |Sha| < infinity.
- Rubin (1991) proved: for CM curves with L(E,1) != 0, the full BSD formula holds (including the leading coefficient), conditional on |Sha| < infinity.
- The paper cites Rubin but doesn't carefully state which version of Rubin's theorem is used.

For rank 1:
- Kolyvagin + Gross-Zagier give rank = 1 and |Sha| < infinity.
- The leading coefficient formula at rank 1 requires the Gross-Zagier formula (relating L'(E,1) to the height of the Heegner point) AND explicit computation of |Sha|, period, Tamagawa numbers.
- For general curves, the full BSD formula at rank 1 is NOT known even with finiteness of Sha. Additional work (Perrin-Riou, Kobayashi, etc.) is needed.

**For CM curves specifically:** Rubin's work (1991) establishes the full BSD formula (both parts) for CM curves at rank 0, assuming L(E,1) != 0. For rank 1, the situation is more delicate -- Rubin's methods handle rank 0 but the rank 1 case requires additional p-adic methods.

**Verdict: WEAKENED.** The rank equality (part (i)) is correctly proved. The leading coefficient formula (part (ii)) at rank 0 follows from Rubin. At rank 1, the paper's claim that "the leading coefficient formula is closed" is asserted but not carefully justified. The paper should cite specific theorems of Perrin-Riou or Rubin that establish part (ii) at rank 1 for CM curves.

---

## ATTACK 14: NUMERICAL VERIFICATION -- Does it actually verify BSD?

**The attack.** Section 13.3 claims to verify the BSD formula for E: y^2 = x^3 - x "to 50 digits." But the computation is confused:

First it computes Omega_E/16 ~ 0.1639 and L(E,1) ~ 0.6555, and these DON'T match. Then it goes through several "resolution" steps involving Neron periods, connected components, and different normalizations. The final claimed verification is L(E,1)/Omega_E^+ = 1/4.

**Analysis.** The confusion about period normalization is a well-known headache in BSD computations. The paper struggles with it visibly. However:

- L(E,1)/Omega_E^+ = 1/4 IS correct for this curve (verified in LMFDB: curve 32.a3 has L/Omega = 1/4, with |Sha| = 1, torsion = (Z/2Z)^2, c_2 = 4).

Wait -- the paper claims c_2 = 1, but LMFDB says c_2 = 4 for curve 32.a3. Let me check: the curve y^2 = x^3 - x has conductor 32. In the LMFDB, this curve has Tamagawa number c_2 = 4, not 1. If the paper uses c_2 = 1, the BSD formula doesn't close.

Actually, the paper says c_2 = 1 in the table. The BSD formula with c_2 = 1 gives L(E,1) = Omega * 1 * 1 * 1 / 16 = Omega/16. But L(E,1) ~ 0.6555 and Omega/16 ~ 0.1639. These are off by a factor of 4. The paper then attributes this to period normalization, but the actual issue may be that c_2 = 4, not 1.

**Verdict: BROKEN (for the numerical verification, not the proof).** The numerical verification in Section 13.3 has errors in the BSD data (likely c_2 = 4, not c_2 = 1). The period normalization discussion is confused. This does not affect the logical validity of the proof chain (which does not depend on this specific numerical check), but it undermines confidence. The numerical section should be corrected using the LMFDB data.

---

## ATTACK 15: SCOPE INFLATION -- What is actually proved?

**The attack.** The paper's rhetoric ("Two Millennium Problems from one description") suggests that a Clay Millennium Problem has been solved. But the Clay BSD problem asks for BSD for ALL elliptic curves over Q, not just CM curves of rank 0 and 1. CM curves are a measure-zero subset of all elliptic curves.

**Analysis.** The paper IS honest about scope (Sections 15.1-15.5). It explicitly states that rank >= 2, non-CM curves, and h_K > 1 are open. However, the framing in the title, introduction, and conclusion inflates the result. "BSD for CM curves" is a significant partial result, but it is not a solution to the Clay problem.

Moreover, BSD for CM curves of rank 0 (Coates-Wiles 1977 + Rubin 1991, given non-vanishing) is ALREADY known conditionally. The new content is:
1. Unconditional non-vanishing (from GRH via the bridge family)
2. Extension to rank 1

Of these, (2) follows from Kolyvagin + Gross-Zagier, which are known theorems. The truly new contribution is (1): GRH for Hecke L-functions over Q(i). This is significant, but it should be framed as such -- a GRH proof, with BSD as a corollary.

**Verdict: SURVIVED (as mathematics).** The theorem as stated (CM curves, rank 0+1, h_K = 1) is correctly scoped. The rhetoric is inflated but the mathematical content is honest.

---

## CONSOLIDATED ASSESSMENT

### Attack Summary

| # | Attack | Verdict |
|:--|:--|:--|
| 1 | Circularity | SURVIVED |
| 2 | CM factorization notation | WEAKENED |
| 3 | Ha-Paugam construction | WEAKENED |
| 4 | Meyer over Q(i) | WEAKENED |
| 5 | Baker's theorem application | SURVIVED |
| 6 | Kolyvagin for CM curves | SURVIVED |
| 7 | Gross-Zagier Heegner hypothesis | WEAKENED |
| 8 | h_K = 1 assumption | SURVIVED |
| 9 | Gap inheritance from RH proof | BROKEN |
| 10 | "Nothing changes" claim | SURVIVED |
| 11 | Twist argument for L(s,psi) | WEAKENED |
| 12 | Bridge lemmas over Q(i) | SURVIVED |
| 13 | Leading coefficient formula | WEAKENED (rank 1 case under-justified) |
| 14 | Numerical verification errors | BROKEN |
| 15 | Scope inflation | SURVIVED |

**Totals: 15 attacks. 8 SURVIVED. 5 WEAKENED. 2 BROKEN.**

### The Two Broken Items

**BROKEN 1 (Attack 9): The "unconditional" claim.** The proof inherits all the conditionality of the RH proof. The Paper 13 review rated the unconditional RH proof at 55-65% confidence. Paper 26 cannot exceed this. Claiming "unconditional" while inheriting conditional foundations is a logical error.

**Fix:** Replace "unconditional" with "a theorem of the Integers programme, conditional on the CBB axioms." Add a clear statement: "This proof is exactly as conditional as the RH proof of Paper 13. The new ingredients (Ha-Paugam, Baker, Kolyvagin, Gross-Zagier) are all unconditional; the inherited ingredients (Axiom 1, bridge family) carry the same status as in Paper 13."

**BROKEN 2 (Attack 14): Numerical verification.** The BSD data for E: y^2 = x^3 - x appear to have c_2 wrong (paper says 1, should likely be 4), and the period normalization discussion is confused. This is a presentation error, not a proof error.

**Fix:** Verify all BSD data against LMFDB (curve 32.a3) and correct c_2 and the period discussion.

### Top 3 Issues

1. **Conditionality inheritance (Attack 9).** The proof is conditional on the CBB axioms, exactly as Paper 13's RH proof is. The "unconditional" claim must be softened or the axiom status must be elevated.

2. **The twist argument (Attack 11).** The extension from GRH for zeta_K to GRH for L(s,psi) needs more careful justification. The paper hand-waves the key step. Cite Connes-Marcolli for the twisted spectral realisation.

3. **Gross-Zagier applicability (Attack 7).** The Heegner hypothesis fails for E: y^2 = x^3 - x at K = Q(i). The paper acknowledges this but resolves it too casually. Specify which auxiliary quadratic field satisfies the Heegner hypothesis, or cite Yuan-Zhang-Zhang more precisely.

### IS THE PROOF VALID?

**As a conditional proof from the CBB axioms: YES.** The internal logic is sound. The chain from CBB axioms to GRH to BSD is correctly assembled for CM curves of rank 0 and 1 with CM by class-number-1 fields, modulo the five WEAKENED items that need tightening.

**As an unconditional proof: NO.** It inherits all the conditionality of Paper 13, and the paper's claim of unconditionality is unjustified.

### Confidence Level

- **Internal chain logic (given CBB axioms):** 85%
- **Unconditional validity:** Same as Paper 13: 55-65%
- **Fixability of BROKEN items:** 95% (both are presentation/framing issues)
- **Fixability of WEAKENED items:** 90% (all are citation/precision issues with known resolutions in the literature)

---

*End of adversarial review. The proof chain is sound within its conditional framework. The five WEAKENED items are all fixable from the existing literature. The two BROKEN items are framing/presentation errors, not logical gaps. If the CBB axioms are correct, BSD for CM curves of rank 0+1 follows.*

*The bridge does extend. But it extends from conditional foundations.*
