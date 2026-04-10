# B2.01: The Factorization

Three proofs are given:

**Proof 1 (KMS uniqueness):** Each A_p has a unique KMS_1 state omega_1^p (Laca-Raeburn 1996). The product state tensor_p omega_1^p satisfies KMS_1 (Bratteli-Robinson Prop 5.3.23). By uniqueness of KMS_1 on A_BC (BC 1995 Theorem 25), the product state equals omega_1.

This proof is CORRECT. Each cited result is standard and correctly applied.

**Proof 2 (Euler product):** For beta > 1, the Gibbs state factorizes via the Euler product. At beta = 1, multiplicativity of n -> 1/n gives omega_1(mu_n mu_n*) = product_p omega_1^p(mu_p^{v_p(n)} mu_p^{*v_p(n)}). This is the arithmetic identity 1/n = product_p 1/p^{v_p(n)}.

This proof is CORRECT for diagonal elements. It does not immediately extend to all of M_1, but combined with Proof 1, it provides independent confirmation.

**Proof 3 (Numerical):** Verified to 50 digits on 135 pairs. Not a proof but a sanity check.

**Verdict: CORRECT.** The ITPFI factorization is solidly established by standard operator algebra results.
