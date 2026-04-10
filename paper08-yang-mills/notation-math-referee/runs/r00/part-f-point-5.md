## Part F, Point 5: OS Reconstruction to Wightman Theory

**Weight:** HEAVY
**Verdict:** PARTIAL — OS1–OS5 verified at the lattice level and propagated to the limit; the reconstruction is invoked correctly; **but** the resulting "Wightman theory" lacks local field operators in the Jaffe–Witten sense (Wilson-loop expectation values are not field operators), see Point G4.

**Finding:**

(a) **OS reconstruction theorem.** §5.7(f) cites the corrected Osterwalder–Schrader 1975 paper (CMP 42, 281–305), which uses the linear growth condition OS0' rather than the original OS0. This is the correct version. Sound.

The verification of OS0' is in §5.7(f) "Lemma (OS0' verification)", which I have already analyzed in Point F1.

(b) **The Hilbert space.** The reconstructed Hilbert space is the GNS space of the algebra of gauge-invariant local observables (continuum limits of plaquette traces, glueball interpolating fields, Wilson loops). Because these observables are *gauge-invariant from the outset*, the Hilbert space is positive-definite by construction. The preprint correctly notes that this bypasses the indefinite-metric issue for gauge fields:

> "The construction bypasses the well-known difficulty of formulating Wightman axioms for gauge fields in indefinite-metric spaces (Strocchi 2013, Chapter 7): by working exclusively with gauge-invariant observables from the outset, the inner product on $\mathcal{H}$ is positive-definite by construction."

Sound. This is the standard "physical observables are gauge-invariant" approach used in lattice gauge theory.

**Subtlety:** What are the "field operators" in the resulting Wightman theory? The preprint says:

> "The reconstructed Wightman theory has field operators that are gauge-invariant composite operators — the continuum limits of plaquette traces $\mathrm{Tr}(F_{\mu\nu}^2(x))$, higher Casimir operators $\mathrm{Tr}(F^n(x))$, Wilson loops $W_C$, and products thereof — rather than fundamental gluon fields $A_\mu^a(x)$."

This is *not* what Jaffe–Witten asks for. Jaffe–Witten §4 (verbatim):

> "one should define a quantum field theory ... with **local quantum field operators** in correspondence with the gauge-invariant local polynomials in the curvature $F$ and its covariant derivatives, such as $\mathrm{Tr}\,F_{ij}F_{kl}(x)$."

The phrase "local quantum field operators in correspondence with..." is asking for *operator-valued distributions* $\mathrm{Tr}\,F_{ij}F_{kl}(x) : \mathcal{S}(\mathbb{R}^4) \to \mathrm{Op}(\mathcal{H})$, not just *vacuum expectation values* $\langle \Omega | \mathrm{Tr}\,F_{ij}F_{kl}(x) | \Omega \rangle$ obtained as continuum limits of lattice observables.

The preprint's approach gives *Schwinger functions* (Euclidean correlators) and uses OS reconstruction to obtain a Hilbert space + Hamiltonian + vacuum, but the resulting "field operators" are constructed from *the algebra of gauge-invariant local operators on the GNS space*. Whether this algebra contains specific operators corresponding to $\mathrm{Tr}\,F_{ij}F_{kl}(x)$ as operator-valued distributions is a separate question.

For lattice operators $\hat{O} = \mathrm{Tr}(U_P)$ and similar, the continuum limit gives *Schwinger functions* of the form $\langle \mathrm{Tr}(U_P(x_1)) \cdots \mathrm{Tr}(U_P(x_n))\rangle$, and the GNS reconstruction gives operators on $\mathcal{H}$ acting on the vacuum to produce one-glueball, multi-glueball states. These operators *do* exist as elements of the algebra of physical observables. So in this sense, the preprint *does* give "field operators in correspondence with curvature polynomials."

But the *correspondence* is loose: $\mathrm{Tr}(U_P(x))$ and $\mathrm{Tr}\,F_{\mu\nu}F^{\mu\nu}(x)$ differ by an $O(a^2)$ continuum limit, and the *normalization* of the limiting operator (multiplicative renormalization, anomalous dimension) is not addressed. For Clay, this matters.

(c) **Non-triviality.** §5.7(f) "Proposition (Non-triviality)" gives three signatures:
1. String tension $\sigma > 0$ (Theorem 4).
2. Non-vanishing connected 2-point function $S_2^c(0, t) \geq |\langle 1|s_P|0\rangle|^2 e^{-\Delta t} > 0$.
3. Asymptotic freedom $b_0 > 0$ (which a free theory does not have).

The proof of $\langle 1|s_P|0\rangle \neq 0$ uses a strong-coupling lower bound (Haar variance) + spectral contradiction + Kato analytic perturbation. This is rigorous (subject to verifying the cluster-expansion temporal-tube weight) and gives a lower bound on the matrix element that survives the continuum limit.

The "non-trivial connected 2-point function" is *weaker* than Jaffe–Witten asks: J–W requires "*Some connected $n$-point with $n \geq 4$ shown nonzero, or interacting S-matrix*" (per the script's C2 criterion). A non-zero 2-point function is automatic for any field theory; what makes a theory "interacting" is non-trivial higher correlators or a non-trivial S-matrix.

The proof does *not* establish a non-trivial 4-point function explicitly. It claims:

> "the connected 4-point function of Wilson loops is nonzero (it encodes the confining potential), but an explicit computation of the continuum $\langle W_{C_1} W_{C_2} W_{C_3} W_{C_4}\rangle_c$ is not required for non-triviality — the 2-point bound (ii) already excludes the Gaussian case."

But the 2-point bound *does NOT* exclude the Gaussian case. A free massive scalar field has $\langle \phi(x) \phi(y)\rangle$ non-zero. The 2-point function alone is not sufficient. The preprint's logic is wrong here.

What *would* exclude the Gaussian case: a non-zero connected 4-point or higher (which a Gaussian theory has zero), OR an asymptotic-freedom argument (since Gaussian theories don't run with logarithmic running). The preprint mentions asymptotic freedom (signature iii) and says "Any one of (i) or (ii) alone suffices", which is incorrect — only (i) and (iii) genuinely exclude the Gaussian case.

**To close:** Either explicitly construct a non-zero connected 4-point function (e.g., from the cluster expansion's lattice 4-point function bounded below by an explicit positive quantity), or rely on signature (i) (string tension) or (iii) (asymptotic freedom) alone. **Difficulty: 1 page.**

(d) **Yang–Mills equations of motion.** §5.7(f) "Schwinger–Dyson equations and Yang–Mills dynamics" derives the lattice Schwinger–Dyson equation
$$\langle \partial_{U_\ell}^a \mathcal{O}\rangle = -\langle \mathcal{O} \cdot \partial_{U_\ell}^a S_W\rangle$$
and shows $-\partial_{U_\ell}^a S_W = a^2 (D_\nu F^{a, \nu\mu})(x) + O(a^4)$. In the continuum limit, this gives the formal SD equation for Yang–Mills.

The argument is correct in structure but the convergence of the lattice SD equation to the continuum SD equation requires the Schwinger functions to converge as distributions and the lattice artifact $O(a^4)$ to vanish uniformly. The preprint asserts these without detailed verification. Standard but should be tightened.

The "Scope" remark correctly notes that the SD equation applies to gauge-invariant observables, and the fundamental gluon field $A_\mu^a$ is *not* an operator on the physical Hilbert space — it is only a lattice integration variable. This is the correct interpretation for a confining theory.

**Impact on the claimed result:** PARTIAL. The OS reconstruction is invoked correctly and the GNS-Hilbert-space construction is sound. The non-triviality argument has a logical hole (the 2-point bound does not exclude Gaussian). The "field operators in correspondence with curvature polynomials" requirement of Jaffe–Witten is *partially* addressed: lattice plaquette traces converge to *some* limit operators, but the precise correspondence with $\mathrm{Tr}\,F_{\mu\nu}F^{\mu\nu}(x)$ involves multiplicative renormalization that is not addressed. See Point G4 for the full critique.
