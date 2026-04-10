## Part F, Point 5: OS Reconstruction to Wightman Theory

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

The claim is that OS reconstruction gives a Wightman QFT with mass gap.

**(a) The OS reconstruction theorem — which version?** The paper uses the corrected 1975 version. OS0' (linear growth condition) is explicitly verified: $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$, which satisfies OS0' after the passage to Schwartz seminorms noted in Point F1(a). The paper is explicit about using the corrected theorem.

**(b) The Hilbert space and gauge theory.** The reconstructed Hilbert space $\mathcal{H}$ is obtained from the GNS construction using the Schwinger functions of gauge-invariant observables (Wilson loops, plaquette traces). This bypasses the gauge/Hilbert space issue: since the input observables are gauge-invariant, the output Hilbert space carries no unphysical degrees of freedom. There are no Faddeev–Popov ghosts or indefinite-norm states.

However, the "field operators" in the Wightman theory are those constructed from the Schwinger functions of gauge-invariant observables. These are operator-valued distributions $\mathcal{O}(x)$ corresponding to gauge-invariant combinations like $\mathrm{Tr}(F_{\mu\nu}^2)(x)$ — but the reconstruction gives operators for whatever observables were used to define the Schwinger functions. If only Wilson loops were used, the reconstruction gives Wilson loop operators, which are non-local. The Jaffe–Witten problem requires **local** field operators in correspondence with $\mathrm{Tr}\,F_{ij}F_{kl}(x)$.

**Gap:** The paper acknowledges this in Appendix L (Conjecture L.1): the construction of local field operators $[\mathrm{Tr}\,F^2]_R(x)$ as limits of multiplicatively renormalized lattice operators is stated as an open problem. This is a genuine requirement of Jaffe–Witten §4 that is not met by the current proof. See Point G4 for the detailed assessment.

**(c) Non-triviality.** The paper must show that the theory is non-trivial (not free/Gaussian). A free theory has a mass gap but is not Yang–Mills. Non-triviality can be established by showing that some connected $n$-point function with $n \geq 4$ is nonzero. The paper does not explicitly verify this.

**Gap:** The non-triviality should be established by computing the connected 4-point function of plaquette operators at leading order. In lattice perturbation theory, the connected 4-point function is $O(g^2) \neq 0$. Since the theory has asymptotic freedom, the coupling does not vanish in the continuum limit — it runs logarithmically. The connected 4-point function should therefore be nonzero. Closable in **1 paragraph**.

**(d) The Yang–Mills equations of motion.** The reconstructed Wightman theory satisfies the Yang–Mills equations only if the lattice Ward identities (from gauge invariance of the Wilson action) survive the continuum limit. The paper does not establish Ward identities for the limiting theory. This is part of the field operator / OPE structure deferred to Conjectures L.1–L.4.

**Impact on the claimed result:**
**(b) and (d)** affect (iii) Clay prize eligibility through the field operator and OPE requirements. **(c)** is a closable gap (1 paragraph). The mass gap claim $\Delta_\infty > 0$ and OS axiom verification are not affected.
