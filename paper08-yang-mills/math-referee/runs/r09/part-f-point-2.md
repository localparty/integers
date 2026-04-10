## Part F, Point 2: Reflection Positivity — The Full Chain

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Lattice reflection positivity.** The Wilson plaquette action satisfies RP by the Osterwalder-Seiler theorem (1978). The KK-enhanced theory satisfies RP by Lemma D.2 (Appendix D), which extends the Osterwalder-Seiler argument to the full action $S = S_{\mathrm{4D}}[U] + S_{\mathrm{int}}[U, A]$.

The key concern is whether the KK-enhanced theory has the checkerboard decomposition structure required by Osterwalder-Seiler. Lemma D.2 verifies this for three types of contributions:

(i) **Wilson plaquette part:** Standard Osterwalder-Seiler. Temporal plaquettes couple links in adjacent time slices; spatial plaquettes are within a single time slice.

(ii) **Internal action:** On-site factors $e^{-S_{\mathrm{YM}}^{\mathrm{int}}(A_x)}$ are positive, local, and trivially satisfy the time-slab decomposition.

(iii) **Bond couplings:** The coupling $V_\ell(U_\ell, A_x, A_{x+\hat\mu}) = (1/a^2)\int \|A_{x+\hat\mu} - U_\ell^{-1} A_x U_\ell\|^2$ is positive semi-definite quadratic. For temporal bonds ($\mu = 0$), this couples fields at times $t$ and $t+a$ — the nearest-neighbor structure required by Osterwalder-Seiler. The Boltzmann weight is a Gaussian kernel with positive-definite exponent, which is of positive type (Bochner's theorem).

The full action decomposes as a product of factors of types (i)-(iii), each satisfying the nearest-neighbor time-slab structure. By the Osterwalder-Seiler theorem, the product satisfies RP. This argument is correct and complete.

**(b) RP through the RG.** The preprint does NOT require RP at intermediate RG steps. Balaban's effective action $S_k$ after $k$ RG steps may not be reflection-positive (the block-spin integration can introduce non-local temporal couplings). However, RP is needed only at the endpoints:

- At the lattice level ($a > 0$): RP holds by Lemma D.2 / Osterwalder-Seiler.
- In the continuum limit ($a \to 0$): RP is preserved by the weak-limit argument (OS3).

The intermediate violation of RP during the RG is harmless because the RG is used only to control the mass gap through the spectral lemma (which requires the transfer matrix, not RP). The RP of the final theory is established independently.

**(c) RP in the continuum limit.** The lower semicontinuity argument: if $\mu_n \to \mu$ weakly and $\langle \theta f, f \rangle_{\mu_n} \geq 0$ for all $n$, then $\langle \theta f, f \rangle_\mu \geq 0$. This requires $\theta f \cdot f$ to be a continuous bounded function under weak convergence.

For Schwartz-class $f$ supported in $\{x_0 > 0\}$: the functional $\langle \theta f, f \rangle_\mu = \int S_2(\theta x, y) f(x) f(y) dx\,dy$ is a continuous linear functional of the Schwinger function $S_2$. Since $S_2^{(a)} \to S_2$ in the weak-$*$ topology on tempered distributions (by the Banach-Alaoglu extraction), the integral converges.

The boundedness concern: on the lattice, the gauge fields are $\mathrm{SU}(N)$-valued (compact), so all observables are bounded. The functional $\theta f \cdot f$ is a product of smeared observables in opposite half-spaces, hence bounded. In the continuum limit, the smearing by Schwartz functions ensures boundedness of the integrated quantity.

The preprint's argument is correct. The lower semicontinuity of non-negative quadratic forms under weak convergence is a standard result in functional analysis.

**Impact on the claimed result:** None. Reflection positivity is correctly established throughout the chain.
