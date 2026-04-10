## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Axial gauge fixing.** Balaban uses axial gauge as a computational device within the block-spin RG. On the LATTICE, axial gauge is well-defined and non-singular:

- Axial gauge sets temporal link variables to the identity: $U_{(x,\hat{0})} = \mathbf{1}$ along a fixed time-like tree
- On a finite lattice, this completely fixes the gauge (no residual gauge freedom, no Gribov copies)
- The "spurious $1/p_0^2$ singularities" of continuum axial gauge are a CONTINUUM ARTIFACT: on the lattice with discrete momenta, there are no poles
- There are no Faddeev-Popov ghosts in lattice axial gauge (the FP determinant is trivial: $\det(\partial_0) = 1$ on the lattice)

The lattice axial gauge propagator is bounded (Balaban CMP 95-96): $|G_k(x,y;V)| \leq C\,e^{-m_W|x-y|}$ with $m_W$ the gauge boson mass from the background field. No singularities arise.

**(b) The Gribov problem.** On a finite lattice with compact gauge group SU($N$):

1. The gauge group $\mathcal{G} = \mathrm{SU}(N)^{|\text{sites}|}$ is compact
2. The axial gauge condition fixes the gauge COMPLETELY (no Gribov copies)
3. The gauge-fixed configuration is unique for each gauge orbit

The block-spin transformation involves averaging over gauge orbits (or equivalently, working on the quotient $\mathcal{A}/\mathcal{G}$). This averaging does not introduce Gribov-type ambiguities because:
- The orbits are compact (finite-dimensional compact Lie group actions)
- The averaging is over the full orbit (not a local gauge-fixing slice)
- The result is manifestly gauge-invariant

At intermediate RG steps, the effective action $S_k[V]$ IS gauge-invariant (this is proved by Balaban and is a structural property of the block-spin construction: the block-spin averaging preserves the gauge symmetry of the coarser lattice).

**(c) Gauge invariance of the final result.** The Schwinger functions are constructed from gauge-invariant observables:

1. **Plaquette operators** $s_P = 1 - (1/N)\,\mathrm{Re}\,\mathrm{Tr}\,U_P$: manifestly gauge-invariant
2. **Wilson loops** $W_C = \mathrm{Tr}\,\prod_{\ell \in C} U_\ell$: manifestly gauge-invariant
3. **All correlation functions** are of the form $\langle O_1(x_1) \cdots O_n(x_n)\rangle$ with each $O_i$ gauge-invariant

Intermediate gauge-fixing (axial gauge within Balaban's RG) does not affect gauge-invariant correlators. The effective action $S_k[V]$ is gauge-invariant at each step $k$. The operator classification (dim-6 operators) and the deviation order analysis both operate on gauge-invariant operators.

Could the gauge-fixed effective action have different properties than the gauge-invariant one? No: on the lattice, gauge-fixing is a change of variables (from link variables to axial-gauge-fixed variables), which does not affect the values of gauge-invariant functionals. The operator norm $\|E_k\|$ and the coefficient bounds $|c_n^{(k)}|$ are computed from the gauge-invariant effective action, not from a gauge-fixed version.

The $\mathcal{C}$-symmetry analysis (elimination of $\mathrm{Tr}(F^3)$) uses the charge conjugation symmetry $\mathcal{C}: U \to U^*$ (complex conjugation of link variables). This is a gauge-invariant operation that commutes with gauge transformations. The $\mathcal{C}$-even projection is well-defined on gauge-invariant operators.

**Impact on the claimed result:** None. Gauge invariance is maintained throughout the proof. Axial gauge fixing on the lattice is clean (no Gribov copies, no singularities). All physical results are expressed in terms of gauge-invariant observables.
