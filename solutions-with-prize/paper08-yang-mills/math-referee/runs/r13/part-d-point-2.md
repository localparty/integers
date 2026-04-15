## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The claim: the full non-perturbative operator delta E_k^{d=6} has dev(delta E_k^{d=6}) >= 2. This is the single most important technical innovation in the paper.

**(a) The definition of Boltzmann deviation order.** Definition D.2 defines dev(O) >= p via a factorization of the spectral weight: the weight W_alpha^{(m)}(n) can be written as tilde{W} times a product of at least p factors (e^{E_m - E_{n_j}} - 1), with |tilde{W}| bounded.

This definition is STRONGER than just "the connected matrix element is O(hat{Delta}^p)." It requires the factorization at the level of INDIVIDUAL spectral channels, not just the total matrix element. This is crucial for the linear combination lemma: individual channel factorization is preserved under summation, while a total O(hat{Delta}^p) bound could be lost through cancellations.

The spectral lemma then shows: dev >= p implies |<1|O|1>_c| <= C_p M hat{Delta}^p. The definition is fit for purpose.

**(b) The linear combination lemma.** If each O_i has dev >= p and Sum |c_i| ||O_i|| < infinity, then Sum c_i O_i has dev >= p. The proof: the spectral weight of the sum is the sum of individual spectral weights (linearity of the trace). Each individual weight has p extractable deviation factors. The absolute convergence Sum |c_i| ||O_i|| < infinity ensures the summed weight inherits the factorization.

Regarding operators with different temporal supports: operators O_i with temporal extent R_i are embedded into a common representation with R = max(R_i) by zero-padding (inserting identity time slices). This preserves the deviation structure because identity insertions add intermediate state sums that resolve as delta_{n_j, n_{j+1}}, which do not affect the deviation factors. Appendix G (multi-time-slice analysis) confirms this: extending temporal support by inserting identity slices is a neutral operation for deviation order.

The concern about cancellations: could dev >= 2 for each term but dev < 2 for the sum? No. The deviation factors are extracted BEFORE summing over intermediate states. Each spectral channel (n_1, ..., n_{2R-1}) in the sum inherits the factorization from the individual terms. The absolute convergence prevents any rearrangement issues. This is elementary — the deviation order is a pointwise property of the spectral weight, and pointwise properties are preserved under absolutely convergent sums.

**(c) The role of (B1) analyticity.** The analyticity with k-independent radius rho means delta E_k^{d=6} is a CONVERGENT sum of monomials (not a formal series). The spectral lemma requires the operator norm M = ||delta E_k^{d=6}||. In the small-field domain Omega_s, the analyticity gives M <= C g_k^4. The convergence of the Taylor expansion holds for all configurations with ||V - 1|| < rho.

Are typical configurations in the analyticity domain? In the gapped phase, field strength fluctuations satisfy <|F|^2> <= C g_k^2. For g_k small (on the AF trajectory), typical configurations have |F| = O(g_k), well within the analyticity domain rho > 0. The one-particle state |1> (the glueball) has support concentrated on typical configurations, so the matrix element <1|delta E_k^{d=6}|1>_c is dominated by configurations within the analyticity domain.

Configurations near the boundary of Omega_s (|F| ~ g_k^{3/4}) are suppressed by the Boltzmann weight but not yet in the large-field regime. The analyticity radius rho is independent of the small-field cutoff g_k^{3/4}, so as long as rho > 0 (which it is, k-independently), the expansion converges for all small-field configurations.

**(d) The transition from perturbative to non-perturbative.** The previous referee (r05, Point 1d) initially flagged this as a GENUINE GAP, then revised to CLOSABLE after re-examination. The key insight:

The classification is EXHAUSTIVE: every dim-6, C-even, gauge-invariant operator has dev >= 2 by STRUCTURAL properties (the two-derivative structure), not by perturbative identification. The non-perturbative operator delta E_k^{d=6} is, by construction, a dim-6, C-even, gauge-invariant operator (it's the dim-6 part of the C-invariant effective action, with dim-4 subtracted). Therefore it has dev >= 2.

The dimension projection is well-defined non-perturbatively because:
(i) The effective action is analytic (by (B1)), so the Taylor expansion is unique.
(ii) Each Taylor coefficient has a definite engineering dimension.
(iii) S_YM is the UNIQUE dim-4 operator (PROOF-CHAIN IV.3), so the dim-4 subtraction is exact.
(iv) The remainder at dim-6 is unambiguously defined.

The separation into "dim-4 + dim-6 + dim-8 + ..." is exact for an analytic function with convergent Taylor expansion. There is no mixing between dimensions — each monomial in the Taylor expansion has a definite dimension.

**(e) Structural zero vs. kinematic zero.** The diagonal vanishing (e^{E_1 - E_1} - 1)^2 = 0 is STRUCTURAL: it arises from the squared-derivative structure of dim-6 operators, not from a coincidence of energy levels.

The deviation order is a property of the operator class (all two-derivative operators have dev >= 2). For the non-perturbative delta E_k^{d=6}, the spectral weights are not computed explicitly — they are inferred from the classification: delta E_k^{d=6} is a convergent sum of operators with dev >= 2, and the linear combination lemma gives dev >= 2 for the sum.

Can a convergent sum have cancellations that change the spectral weight structure? No: the linear combination lemma shows that the deviation factors are preserved termwise. Each term contributes spectral weights with p >= 2 extractable deviation factors. The sum of these weights inherits the same factorization. Cancellations in the TOTAL matrix element cannot reduce the deviation order below 2, because the deviation order is defined at the level of individual spectral channels, and each channel inherits its factorization from the dominant term.

No error found. This is the most innovative and delicate part of the proof, and it is correct. The combination of exhaustive classification, analyticity, and the linear combination lemma provides a rigorous non-perturbative argument for dev >= 2.

**Impact on the claimed result:** This is the lynchpin of the proof. If this step were wrong, the entire RG preservation argument would collapse. It is sound.
