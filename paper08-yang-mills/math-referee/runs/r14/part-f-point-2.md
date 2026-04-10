## Part F, Point 2: Reflection Positivity -- The Full Chain

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Lattice reflection positivity.** The Osterwalder-Seiler theorem (1978) establishes RP for the Wilson plaquette action via the checkerboard decomposition. The preprint's KK-enhanced theory has action:

$$S = S_{4D}[U] + \sum_x S_{\mathrm{YM}}^{\mathrm{int}}(A_x) + \sum_\ell V_\ell(U_\ell, A_x, A_{x+\hat\mu})$$

Appendix D (Lemma D.2) proves RP for the FULL action using three ingredients:

1. **Wilson plaquette part** $e^{-S_{4D}[U]}$: Satisfies the checkerboard decomposition by the original OS theorem. This is specific to the Wilson action.

2. **Internal action** $\prod_x e^{-S_{\mathrm{YM}}^{\mathrm{int}}(A_x)}$: A product of positive on-site factors. These do not couple to the time-reflection and contribute positively.

3. **Bond couplings** $e^{-V_\ell}$: The coupling $V_\ell = (1/a^2)\int \|A_{x+\hat\mu} - U_\ell^{-1}A_x U_\ell\|^2$ is a positive semi-definite quadratic form. The Boltzmann weight $e^{-V_{(x,\hat{0})}}$ is a Gaussian kernel coupling adjacent time slices. The proof that this kernel is of positive type uses:
   - The adjoint action $A \mapsto UAU^{-1}$ is an isometry of the internal configuration space
   - $e^{2c\langle A', B\rangle}$ is positive-type by Bochner's theorem (characteristic function of a Gaussian measure)
   - Reference: Glimm-Jaffe 1987, Chapter 6; Seiler 1982, Theorem 6.1

The key technical point: the temporal bond $V_{(x,\hat{0})}$ couples $A_x$ (on the time-zero slice) to $A_{x+\hat{0}}$ (one step in the future) through the temporal link $U_{(x,\hat{0})}$. The Gaussian structure of this coupling, combined with the isometric nature of the adjoint action, ensures the checkerboard decomposition extends to the full KK-enhanced action.

This is a GENUINE PROOF of RP for the KK-enhanced action, not merely a citation of OS78. It extends OS78 to include the internal degrees of freedom.

**(b) RP through the RG.** Balaban's block-spin transformation may NOT preserve RP at intermediate RG steps. The effective action $S_k$ after $k$ block-spin steps is not necessarily the action of a reflection-positive measure: block-spin averaging can introduce non-local terms and modify the temporal structure.

However, the proof does NOT require RP at intermediate scales. The logical structure is:

- RP holds at the STARTING lattice (Lemma D.2) $\implies$ the transfer matrix is self-adjoint and positive $\implies$ spectral decomposition is valid $\implies$ the spectral lemma applies.
- RP holds in the CONTINUUM LIMIT (by weak-limit argument) $\implies$ OS3 is satisfied $\implies$ OS reconstruction applies.

Intermediate RP is irrelevant. The RG analysis operates on the effective action (not on the RP structure), and the spectral lemma uses the transfer matrix of the STARTING theory (with corrections from the effective action treated perturbatively via Kato theory).

**(c) RP in the continuum limit.** The preprint uses the Portmanteau theorem (a standard result in weak convergence of measures): if $\mu_n \to \mu$ weakly and $\langle \theta f, f\rangle_{\mu_n} \geq 0$ for all $n$, then $\langle \theta f, f\rangle_\mu \geq 0$.

The conditions for the Portmanteau theorem:
- **Boundedness:** The functional $\theta f \cdot f$ is bounded because the lattice fields are SU($N$)-valued (compact group, all matrix entries bounded by 1).
- **Continuity:** For Schwartz-class $f$, the functional $\theta f \cdot f$ as a function of the field configuration is continuous in the topology of weak convergence of distributions. This follows from the uniform bounds on lattice Schwinger functions.

The argument is: for each Schwartz $f$ supported in the positive half-space, define $\Phi_f[\phi] = \langle \theta f, f\rangle$. This is a bounded continuous functional. If $\Phi_f \geq 0$ under each lattice measure $\mu_{a_j}$, then $\Phi_f \geq 0$ under the limit measure $\mu$.

More precisely, RP is a condition on the Schwinger functions: $\sum_{m,n} S_{m+n}(\theta g_m^* \otimes g_n) \geq 0$ for all sequences $\{g_n\} \subset \mathcal{S}(\mathbb{R}_+^{4n})$. This is a countable family of inequalities (for rational linear combinations of test functions), each preserved under weak limits.

**Impact on the claimed result:** None. Lattice RP is proved in Appendix D for the full KK-enhanced action. Intermediate RP is not needed. Continuum RP follows from weak limits by the Portmanteau theorem. The full chain is rigorous.
