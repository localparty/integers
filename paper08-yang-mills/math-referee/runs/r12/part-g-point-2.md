## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

---

**Finding:**

**(a) Axial gauge fixing.** Balaban uses axial gauge fixing as a computational device within the small-field region $\Omega_s$. In axial gauge, the temporal link variables are fixed: $U_{x,\hat{0}} = \mathbf{1}$ for all $x$, reducing the gauge freedom to spatial gauge transformations. This avoids Faddeev-Popov ghosts (the FP determinant is trivial for axial gauge).

On the lattice, the axial gauge condition $U_{x,\hat{0}} = \mathbf{1}$ is a lattice constraint, not a differential equation. There are no propagator singularities of the type $1/p_0^2$ on the lattice (the temporal link is simply absent). The axial gauge is well-defined and free of the $1/p_0^2$ singularities that appear in the continuum formulation. SOUND.

**(b) The Gribov problem.** On a finite lattice, the gauge group is compact ($\mathrm{SU}(N)$ valued at each link), so the gauge orbit is compact. Axial gauge (fixing all temporal links to $\mathbf{1}$) is a complete gauge-fixing on the lattice: it uniquely determines a representative in each gauge orbit (up to the residual spatial gauge freedom, which is treated separately). There are no Gribov copies for axial gauge on the finite lattice. SOUND.

The block-spin transformation involves averaging over gauge orbits (integrating out UV fluctuations with a gauge-equivariant averaging kernel). This averaging is gauge-equivariant: the block-averaged field $V$ transforms under gauge transformations in the same way as the original field $U$. The integral over gauge orbits is equivariant, not gauge-fixed, so no Gribov-type ambiguity is introduced at the block-spin level. After blocking, a fresh axial gauge can be chosen for the coarser lattice.

The relevant concern would be if Balaban's construction fixed a unique gauge at one level and then the block-spin averaging broke this gauge choice. This does not happen because the averaging kernel is gauge-equivariant (Balaban, CMP 98). SOUND.

**(c) Gauge invariance of the final result.** The Schwinger functions are built from gauge-invariant observables (Wilson loops, plaquette traces). These are gauge-invariant by construction, regardless of the intermediate gauge-fixing steps. The final Wightman QFT is built from these gauge-invariant Schwinger functions via OS reconstruction. The gauge symmetry is manifest at the level of the physical observables.

The dimension-6 operator classification (Part D1) uses $\mathcal{C}$-symmetry to eliminate the $\mathrm{Tr}(F^3)$ operators. This argument is performed in the gauge-invariant effective action, not in a gauge-fixed one. Balaban's effective action $S_k[V]$ is gauge-invariant at each step (CMP 109, Section 1: the effective action is constructed to be gauge-invariant under the residual gauge freedom). The operator classification applies to the gauge-invariant $S_k$.

For the spectral lemma: the operators $E_k(x)$ are gauge-invariant (constructed from gauge-invariant block-averaged fields $V$). The one-particle state $|1\rangle$ is a gauge-invariant glueball state. The matrix element $\langle 1|E_k(0)|1\rangle_c$ is a gauge-invariant quantity. None of the spectral lemma arguments require gauge-fixing. SOUND.

**Impact on the claimed result:** No gap. Gauge invariance is maintained throughout the proof via two mechanisms: (i) Balaban's block-spin preserves gauge invariance of the effective action at each step, and (ii) the final Schwinger functions are built from gauge-invariant observables. The intermediate axial gauge fixing is a computational device that does not affect gauge-invariant conclusions.
