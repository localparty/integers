## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Axial gauge fixing.**

Balaban uses axial gauge fixing ($U_{x,0} = \mathbf{1}$ for temporal links in each time slice) as a computational device to parametrize gauge orbits. In axial gauge:
- The Faddeev-Popov determinant is trivial (no ghost fields needed)
- The gauge is completely fixed on a finite lattice (no residual gauge freedom)

The axial gauge propagator in the continuum has $1/p_0^2$ poles (spurious singularities). On the lattice, these singularities are absent: the lattice propagator $G_k(V) = (-D^2[V] + m_W^2)^{-1}$ is well-defined (the lattice Laplacian is bounded, and $m_W^2 > 0$ ensures invertibility). The $1/p_0^2$ poles are continuum artifacts that do not appear on the lattice.

Balaban's construction operates entirely on the lattice, where the axial gauge is well-defined and smooth. The continuum limit is taken for gauge-invariant observables (not for gauge-fixed quantities), so the axial gauge singularities are irrelevant to the final result.

**(b) The Gribov problem.**

In non-abelian gauge theories, gauge-fixing conditions typically have multiple solutions (Gribov copies). On a finite lattice with compact gauge group:
- The gauge group $G^{|\Lambda|}$ acts on the finite-dimensional configuration space
- Axial gauge $U_{x,0} = \mathbf{1}$ selects a unique representative on each gauge orbit (for a simply connected group like SU($N$), the temporal gauge fixing is complete)

Balaban's block-spin transformation involves averaging over gauge orbits in a well-defined sense: the block link variables $V_\ell$ are defined by projecting averaged link variables onto the gauge group (the polar decomposition $A \mapsto A(A^\dagger A)^{-1/2}$). This projection is gauge-equivariant by construction: if $U \mapsto g U g'^\dagger$ under a gauge transformation, then $V \mapsto g V g'^\dagger$ under the corresponding block gauge transformation.

No Gribov-type ambiguity arises at intermediate scales because:
1. The axial gauge is unique (no Gribov copies) on each lattice $\Lambda_k$
2. The block-spin projection is a smooth, well-defined map (analytic for $\|A - \mathbf{1}\| < r_{\mathrm{proj}}$)
3. The effective action $S_k[V]$ is gauge-invariant at each step (by construction: it's obtained by integrating out fast modes with a gauge-invariant measure)

**(c) Gauge invariance of the final result.**

The Schwinger functions are constructed from gauge-invariant observables (plaquette traces $s_P$, Wilson loops $W_C$). These are manifestly gauge-invariant regardless of any intermediate gauge-fixing.

The concern: could the gauge-fixed effective action have different properties than the gauge-invariant one, affecting the operator classification or deviation order? The answer is no, for the following reason:

The operator classification (dimension-6 operators, $\mathcal{C}$-symmetry) operates on gauge-invariant operators. The effective action $S_k[V]$ is gauge-invariant at each step $k$ (proved by Balaban: the block-spin integration preserves gauge invariance). The axial gauge is used only as a parametrization device within each RG step — the input and output of each step are gauge-invariant functionals.

The deviation order argument operates on the spectral representation of gauge-invariant matrix elements $\langle 1|\mathcal{O}|1\rangle_c$, which are independent of any gauge-fixing. The gauge-fixed intermediate calculations (propagator bounds, Gaussian integration) produce gauge-invariant results because they are combined with the gauge-invariant measure and observables.

**Impact on the claimed result:**

None. Gauge invariance is maintained throughout the proof:
- The lattice theory is manifestly gauge-invariant
- Axial gauge is a computational device with no Gribov issues on the lattice
- The effective action is gauge-invariant at each RG step
- The Schwinger functions are gauge-invariant by construction
- The operator classification and deviation order arguments operate on gauge-invariant quantities
