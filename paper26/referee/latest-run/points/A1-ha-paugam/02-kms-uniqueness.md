## Point A1(b): KMS Uniqueness

**The question:**
The unique KMS_1 state requires h_K = 1. For K = Q(i), h_K = 1 is a classical fact. But does the KMS analysis follow the same pattern as for Q? The class group is trivial, but the unit group of Q(i) is {+/-1, +/-i} -- larger than {+/-1} for Q. Does this affect the KMS classification?

**Finding:**
The preprint claims (Proposition 3.4) that KMS_1 is unique for K = Q(i) and cites h_K = 1 as the essential input. The proof sketch says the argument is "identical to Bost-Connes (1995), Theorem 25."

The unit group issue is addressed in Section 17.2 (Attack 2): the extra units +/-i contribute to the Dirichlet regulator, which for imaginary quadratic fields is trivial (R_K = 1 by convention, since the unit group is finite). The preprint claims this does not obstruct KMS uniqueness.

This is correct. In the Ha-Paugam framework, the KMS states at beta > 1 are parametrized by elements of Gal(K^{ab}/K), which by class field theory is isomorphic to the idele class group. The number of extremal KMS_1 states (at the phase transition) is controlled by the class number h_K: when h_K = 1, there is a unique KMS_1 state, regardless of the unit group size. The unit group affects the structure at beta > 1 (where KMS states are parametrized by the Galois group) but not the uniqueness at beta = 1.

The formula for the KMS_1 state given in Proposition 3.4 --
omega_1^K(e_a) = (1/zeta_K(1+epsilon)) sum_b N(b)^{-(1+epsilon)} as epsilon -> 0^+
-- is the standard trace-state formula, normalized by the pole of zeta_K at s = 1.

**Potential concern:** The Laca-Raeburn analysis that underlies the KMS classification was originally done for the rational BC system. Its extension to Ha-Paugam systems over number fields is claimed but not as thoroughly documented in the literature. However, for h_K = 1 fields (PIDs), the semigroup structure of ideals is isomorphic to the semigroup structure over Q (every ideal is principal), so the Laca-Raeburn arguments transfer directly.

**Verdict for this sub-question:**
SOUND — KMS_1 uniqueness for K = Q(i) follows from h_K = 1 by the standard argument. The unit group does not obstruct. The analysis is correct.
