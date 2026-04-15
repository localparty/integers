# Repair 3: Lemma 5.1, Proof 1 (Corrected)

**Programme:** Clone Growth <-> Fullness Bridge Theorem (Paper 28, P != NP)
**Document:** Repair 3 -- Corrected Proof 1 of Lemma 5.1 (Conditional expectation normality)
**Date:** 2026-04-11
**Replaces:** Lemma 5.1 Proof 2 citation "Bost-Connes 1995, Theorem 25" in Node 2.1-CP1-formal.md, lines 238--244
**Depends on:** KEY LEMMA 3.4.3 (faithful normal KMS_1 state on M_Bool); Takesaki II, Theorem IX.4.2
**CP-1 finding:** W1-4, Attack 2 -- the BC 1995 citation is inapplicable (that theorem concerns the original number-theoretic BC system over Q, not the Boolean BC system where all group elements are bijections with trivial modular weight)

---

## Lemma 5.1 (Conditional expectation: normality)

*The conditional expectation E_L : M_Bool -> M^L_Bool defined by Fourier truncation*

    E_L(sum_{g in G_Bool} a_g u_g) := sum_{h in G_L} a_h u_h

*is normal (sigma-weakly continuous).*

**Proof 1 (Modular triviality + trace property).** Let phi := omega^Bool_1 denote the KMS_1 state on M_Bool, which is faithful and normal by KEY LEMMA 3.4.3. We show phi(E_L(x)) = phi(x) for all x in M_Bool, then invoke Takesaki's uniqueness theorem.

*Step 1. The modular flow is trivial on group unitaries.* The modular automorphism group sigma_t of M_Bool acts on circuit operators by

    sigma_t(mu_C) = (size C)^{it} mu_C

where size C = |im C| / |dom C| is the measure-theoretic compression ratio. Every element g in G_Bool is a bijective circuit (by Lemma 4.2, PCirc^+_bi is a group), so size(g) = 1. Therefore

    sigma_t(u_g) = 1^{it} u_g = u_g    for all g in G_Bool, all t in R.

The modular flow is trivial on the group algebra C[G_Bool] inside M_Bool.

*Step 2. KMS_1 reduces to the trace on the crossed product.* Since sigma_t is trivial on every u_g, the KMS_1 condition omega_1(x sigma_i(y)) = omega_1(yx) applied with x = a in A := L^infty({0,1}^infty, mu_1) and y = u_g gives

    omega_1(a u_g) = omega_1(u_g a) = omega_1(alpha_g(a) u_g).

This is the trace condition: omega_1 restricted to A rtimes G_Bool acts as a trace on the group direction. The canonical trace on a crossed product A rtimes G (with G acting by measure-preserving transformations on (X, mu)) evaluates as

    tau(sum_g a_g u_g) = integral_X a_e d mu

killing all off-diagonal Fourier components (those with g != e). Since omega_1 satisfies the trace condition and is the unique KMS_1 state (KEY LEMMA 3.4.3), we have omega_1(sum_g a_g u_g) = integral a_e d mu_1.

*Step 3. phi-preservation.* For any x = sum_g a_g u_g in M_Bool:

    phi(E_L(x)) = phi(sum_{h in G_L} a_h u_h) = integral a_e d mu_1 = phi(x)

since e in G_L (the identity is always in the stabilizer group) and the trace kills all terms with h != e in the first equality, and all terms with g != e in the last.

*Step 4. Normality via Takesaki IX.4.2.* By Takesaki (Theory of Operator Algebras II, Theorem IX.4.2): given a faithful normal state phi on a von Neumann algebra M and a von Neumann subalgebra N, there exists at most one phi-preserving conditional expectation M -> N, and any such map is automatically normal. Since phi = omega^Bool_1 is faithful and normal on M_Bool, and E_L is a phi-preserving conditional expectation onto M^L_Bool, the map E_L is normal. QED.

---

**What changed from the original.** The original Proof 2 cited "Bost-Connes 1995, Theorem 25, transposed to the Boolean setting" for the claim that the KMS_1 state sees only the identity Fourier component. That theorem applies to the number-theoretic BC system where the semigroup N* contains non-invertible elements with size > 1, producing a non-trivial modular flow that forces off-diagonal KMS vanishing. In the Boolean setting, G_Bool consists entirely of bijections (size = 1), so the modular flow is trivial on all group unitaries. The corrected proof derives the off-diagonal vanishing directly: trivial modular flow implies KMS_1 = trace, and the trace on a group crossed product kills off-diagonal components by definition. The remainder of the proof (Takesaki IX.4.2) is unchanged.
