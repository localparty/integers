## Part F, Point 2: Reflection Positivity — The Full Chain

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Lattice reflection positivity.**

The Osterwalder-Seiler theorem (1978) establishes RP for the Wilson plaquette action via the checkerboard decomposition. This theorem is specific to nearest-neighbor actions with a product structure across time slices.

The KK-enhanced theory (with internal $\mathbb{CP}^{N-1}$ connections at each site) is addressed in Appendix D (Lemma D.2). The full action decomposes into three components on each time slab $[t, t+a]$:

1. **Wilson plaquettes:** Satisfy the original Osterwalder-Seiler checkerboard. The temporal plaquettes factor as $e^{-\beta s_P} = e^{-\beta(1 - (1/N)\mathrm{Re}\,\mathrm{Tr}\,U_P)}$, and $U_P = U_{x,\mu}U_{x+\hat{\mu},0}U_{x+\hat{0},\mu}^{-1}U_{x,0}^{-1}$ involves link variables from exactly two adjacent time slices.

2. **Internal action:** $\prod_x e^{-S_{\mathrm{YM}}^{\mathrm{int}}(A_x)}$ is a product of on-site factors, each positive and supported on a single time slice. On-site factors trivially satisfy RP (they are diagonal in the time-slice decomposition).

3. **Bond couplings:** $V_\ell = (1/a^2)\int_{\mathbb{CP}^{N-1}} \|A_{x+\hat{\mu}} - U_\ell^{-1}A_x U_\ell\|^2\,\mathrm{dvol}$ is a positive-definite quadratic form. Temporal bonds (coupling fields at times $t$ and $t+a$) have the nearest-neighbor structure required by Osterwalder-Seiler. Spatial bonds (within a time slice) contribute positive factors to the time-slice Boltzmann weight.

The product of these three components has the checkerboard structure: the action on each time slab decomposes into factors depending on at most two adjacent time slices, with positive-definite Gaussian kernels for the internal degrees of freedom. Lemma D.1 (Product Manifold Lemma) confirms: if $M_1$ satisfies RP and $M_2$ is compact with positive-definite metric, then $M_1 \times M_2$ satisfies RP.

The full action $S_{\mathrm{4D}} + S_{\mathrm{int}}$ has the checkerboard structure required for Osterwalder-Seiler. RP holds for the KK-enhanced lattice theory.

**(b) RP through the RG.**

Balaban's block-spin transformation may not preserve RP at intermediate steps: the effective action $S_k$ is not necessarily reflection-positive (it may contain higher-order terms that violate the checkerboard structure).

This is irrelevant. The proof requires RP only at two points:
1. **The lattice level** ($a$ fixed): RP holds by Osterwalder-Seiler for the original Wilson action (not the RG-evolved effective action).
2. **The continuum limit** ($a \to 0$): RP is preserved by lower semicontinuity of the weak limit.

The RG analysis (Sections 5.1-5.6) operates on the effective action to bound the mass gap shift, but it does NOT require RP at intermediate RG steps. The mass gap analysis uses spectral properties of the transfer matrix (which exists by RP of the original action) and bounds the eigenvalue shifts. The spectral gap at each RG step $k$ is a property of the physical transfer matrix (defined by the original action at lattice spacing $a_k = 2^k a_0$), not of the effective action.

The intermediate violation of RP by the RG-evolved effective action is harmless because the effective action is a computational tool, not the physical measure. The physical measure at each scale is defined by the original Wilson action, which is reflection-positive at all scales.

**(c) RP in the continuum limit.**

The lower semicontinuity argument: if $\mu_n \to \mu$ weakly and $\langle \theta f, f\rangle_{\mu_n} \geq 0$ for all $n$, then $\langle \theta f, f\rangle_\mu \geq 0$.

This requires $\theta f \cdot f$ to be a continuous bounded function of the field configuration. For Schwartz-class test functions $f$ and lattice gauge fields (which take values in the compact group SU($N$)):

- **Boundedness:** The lattice fields are SU($N$)-valued (compact), so any polynomial function of the fields (including Wilson loops and plaquette traces used to define the Schwinger functions) is bounded. Therefore $\theta f \cdot f$ (which is a product of Schwinger functions smeared against test functions) is bounded.

- **Continuity:** On the space of lattice gauge field configurations (a product of compact groups), polynomial functions of the link variables are continuous. The weak limit of measures on this space preserves integrals of continuous bounded functions by definition.

For the continuum limit: the lattice Schwinger functions converge weakly in $\mathcal{S}'(\mathbb{R}^{4n})$ (by Banach-Alaoglu). The RP condition $\langle \theta f, f\rangle \geq 0$ is a closed condition in the weak-$*$ topology (it's the non-negativity of a continuous functional), so it passes to the limit.

**Impact on the claimed result:**

None. Reflection positivity is correctly established at the lattice level (Osterwalder-Seiler, including the KK-enhanced theory), and correctly preserved in the continuum limit (lower semicontinuity). The intermediate RG steps need not preserve RP.
