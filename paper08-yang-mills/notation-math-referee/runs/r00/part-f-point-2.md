## Part F, Point 2: Reflection Positivity — The Full Chain

**Weight:** MEDIUM
**Verdict:** SOUND for the lattice level (Osterwalder–Seiler applies, including the KK enhancement), and SOUND for the continuum limit by the Portmanteau theorem.

**Finding:**

(a) **Lattice reflection positivity.** The Osterwalder–Seiler theorem (1978) gives RP for the Wilson plaquette action via the checkerboard decomposition. The KK-enhanced theory adds two pieces:
- On-site internal action $S_{\mathrm{YM}}^{\mathrm{int}}(A_x)$, which is a positive on-site factor and trivially preserves the time-slab decomposition.
- Bond couplings $V_\ell(U_\ell, A_x, A_{x+\hat\mu}) = (1/a^2)\int \|A_{x+\hat\mu} - U_\ell^{-1} A_x U_\ell\|^2$, which is a Gaussian kernel coupling fields at adjacent sites.

Appendix D Lemma D.2 verifies RP for the full KK theory by showing each Boltzmann factor is of "positive type" in the sense required by Osterwalder–Seiler. The argument for the Gaussian bond kernel is via Bochner's theorem and the Schur product (positive-type kernels are closed under products and series). Sound.

This is *not* a generic argument — it depends specifically on the bond coupling being a Gaussian (positive-definite quadratic form). If the coupling were higher-order or had non-trivial kernel structure, RP could fail. The preprint's specific choice of coupling is engineered to preserve RP.

(b) **RP through the RG.** Balaban's block-spin transformation may not preserve RP at intermediate steps. The preprint does NOT claim RP at intermediate Balaban steps. Section 5.7(f) OS3 only claims RP at the *lattice level* (Osterwalder–Seiler) and at the *continuum limit* (lower semicontinuity). Intermediate Balaban steps are bypassed: the RP property is preserved from the lattice action through the Banach–Alaoglu limit, not through the Balaban block-spin flow.

This is correct in structure: as long as RP holds for the *measure* at each lattice spacing $a$, and the limit is a weak limit of these measures, the limit measure inherits RP. Balaban's RG is used internally to control the *spectral* properties of the effective action, not to preserve RP step by step.

(c) **RP in the continuum limit via Portmanteau.** §5.7(f) Step 2 (OS3) uses the Portmanteau theorem (Billingsley 1999, Theorem 2.1; Kallenberg 2002, Lemma 4.3): if $\mu_a \to \mu$ weakly and $F_f$ is a bounded continuous function on field space, then $\int F_f d\mu_a \to \int F_f d\mu$, hence the non-negativity of $\int F_f d\mu_a$ for all $a$ is inherited by $\int F_f d\mu$.

The argument requires $F_f(\phi) = \overline{f[\phi|_+]} \cdot f[\theta^* \phi|_+]$ to be (i) bounded and (ii) continuous on field space. Boundedness is from $\|f\|_\infty < \infty$. Continuity is on the topology of field space (presumably the weak-$*$ topology on tempered distributions, on which the sequence $\mu_{a_j}$ converges weakly).

**Subtlety:** The "field space" is, for the lattice theory, the compact $\mathrm{SU}(N)^{|\Lambda^1|}$ group manifold. For the continuum theory, it is a space of distributional gauge connections, which is much larger. Continuity of $F_f$ requires the test function $f$ to be sufficiently regular (Schwartz class). The preprint's argument is that "continuity follows from the Schwartz-class decay of $f$ and the topology on field space" — without fully specifying the topology. This is a presentation gap; the argument is correct in spirit but the precise functional-analytic setup is glossed over.

**To close:** specify the topology on field space and verify continuity of the bilinear form $\langle \theta f, f \rangle$ on this topology. Standard but should be made explicit. **Difficulty: 1 page.**

**Impact on the claimed result:** Sound. RP is preserved through the chain: lattice (Osterwalder–Seiler) → weak limit (Portmanteau). The internal Balaban steps are not relied upon for RP.
