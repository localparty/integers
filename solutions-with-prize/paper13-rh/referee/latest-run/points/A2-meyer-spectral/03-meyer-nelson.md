# A2.03: Meyer-Nelson Compatibility

The paper claims (Section 1.3, research/266) that Meyer's distributional framework and Nelson's self-adjointness theorem are "compatible." The chain is:

1. GNS(omega_1) -> H_1
2. T_BC symmetric on S subset H_1
3. Analytic vectors dense in H_1
4. Nelson -> T-bar_BC self-adjoint
5. Meyer: gamma_n in approx-spec(T_BC|_S)
6. Approximate spectrum preserved under closure: gamma_n in spec(T-bar_BC)

**Assessment of each step:**

Steps 1-4 are internally consistent IF T_BC is correctly defined as a symmetric operator on S. However, the paper never establishes that T_BC (the operator whose distributional spectrum contains the Riemann zeros via Meyer) is the SAME operator as the one that acts by multiplication by gamma_n on the {e_n} basis of H_R. The paper uses "T_BC" to denote both, but these are two different constructions:

(a) Meyer's T_BC is the generator of the scaling automorphism sigma_t restricted to the GNS space H_1 of omega_1. Its distributional spectral inclusion uses the Weil explicit formula.

(b) The paper's T_BC (from Proposition 8.1) is defined by T_BC e_n = gamma_n e_n on the Hilbert space H_R from Axiom 1.

The identification of (a) and (b) IS Axiom 1. It is not proved.

Step 5 is the critical gap identified in A2.02.

Step 6 is standard functional analysis, but only applies if Step 5 holds.

**Verdict: The Meyer-Nelson compatibility argument has a structural gap.** It conflates two different operators and two different Hilbert spaces, with the identification assumed via Axiom 1 rather than proved.
