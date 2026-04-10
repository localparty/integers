# A2.02: Distributional vs Genuine Eigenvalues

This is the central technical issue of the entire paper.

**The distinction:** A distributional eigenvalue lambda of T on the Gel'fand triple S subset H subset S' means there exists phi in S' with T phi = lambda phi in the distributional sense. This does NOT imply lambda is in the spectrum of T or any self-adjoint extension of T on H.

**Standard counterexamples:**
- The position operator X on L^2(R) has distributional eigenstates delta(x - x_0) at every x_0 in R, but its spectrum is all of R (continuous, no point spectrum at all).
- The momentum operator P = -i d/dx has distributional eigenstates e^{ipx} at every p in R, again with purely continuous spectrum.

In both cases, distributional eigenvalues exist at every real number, but there are NO genuine eigenvalues. The distributional spectrum is all of R while the point spectrum is empty.

**The paper's claim (Section 1.3, Appendix B.5):** The distributional eigenvalues transfer to the self-adjoint closure via "approximate spectrum preservation." The chain is: gamma_n in approx-spec(T_BC|_S) implies gamma_n in spec(T-bar_BC).

**Assessment:** The claim about approximate spectrum preservation is CORRECT as a general principle: if lambda is in the approximate spectrum of T restricted to a core domain, then lambda is in the spectrum of the closure. The question is whether Meyer's distributional eigenstates actually give approximate eigenvalues.

A distributional eigenstate phi_n in S' satisfying T phi_n = gamma_n phi_n does NOT automatically give an approximate eigenvector in H_1. For that, you need a SEQUENCE {f_k} in H_1 with ||f_k|| = 1 and ||(T - gamma_n)f_k|| -> 0. This is a strictly stronger condition than having a distributional eigenstate.

**The gap:** The paper asserts but does not prove that Meyer's distributional eigenstates yield approximate eigenvectors in H_1. This step requires showing that the distributions phi_n can be regularized (e.g., by convolution with a smooth kernel) to produce a Weyl sequence in H_1. This is plausible but non-trivial, and the paper does not provide this argument.

**Verdict: GAP.** The upgrade from distributional spectrum to approximate spectrum (and hence to spectrum of the closure) is asserted but not proved.
