## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Axial gauge fixing.**

Balaban uses axial gauge ($A_0 = 0$ in a time-like direction) as a computational device within the block-spin RG. On the lattice, axial gauge is well-defined and unique: fixing one link per site (the temporal link $U_{x,0} = \mathbf{1}$) completely determines the gauge, with no residual gauge freedom and no Faddeev-Popov ghosts (the FP determinant is trivial in axial gauge).

The continuum spurious singularities ($1/p_0^2$ poles in the axial gauge propagator) are lattice artifacts of taking $a \to 0$ in the propagator before completing the construction. On the finite lattice, the propagator is a finite matrix and has no poles. The continuum limit is taken for gauge-invariant quantities (Schwinger functions), which are independent of the gauge-fixing.

**(b) The Gribov problem.**

On a finite lattice with compact gauge group, axial gauge is complete: every gauge orbit has exactly one representative with $U_{x,0} = \mathbf{1}$ for all temporal links in a maximal tree. There are no Gribov copies in axial gauge on the lattice (unlike Coulomb or Landau gauge, which have multiple solutions). This is because the gauge condition fixes the link variables sequentially along the tree, with each step having a unique solution.

The block-spin transformation averages over fluctuations at scale $a_k$ and produces an effective action on the coarser lattice $\Lambda_{k+1}$. This averaging respects gauge invariance: the block variable $V_\ell$ on $\Lambda_{k+1}$ is defined as the gauge-covariant average of fine-lattice links, and the effective action $S_k[V]$ is gauge-invariant by construction (it is defined by integrating out fine-lattice variables with the gauge-invariant Haar measure and gauge-invariant Wilson action).

No Gribov-type ambiguities arise at intermediate scales because: (i) the averaging is gauge-covariant (not gauge-fixed); (ii) the gauge-fixing is applied only within each block for computational purposes and is undone when projecting back to gauge-invariant quantities.

**(c) Gauge invariance of the final result.**

The Schwinger functions are constructed from gauge-invariant observables (plaquette traces, Wilson loops). These are manifestly gauge-invariant regardless of the intermediate gauge-fixing. The RG effective action $S_k$ is gauge-invariant at each step (as proved by Balaban), but even if it were not, the final Schwinger functions depend only on the partition function and gauge-invariant insertions, both of which are gauge-invariant.

Could the gauge-fixed effective action have different properties than the gauge-invariant one? No, because Balaban's construction produces a gauge-invariant effective action at each step. The axial gauge is used only within the block-spin integration (to parametrize the fluctuation variables), and the result after integration is gauge-invariant. The operator classification (dimension-6, $\mathcal{C}$-even, gauge-invariant) applies to the gauge-invariant effective action. The deviation order argument uses only gauge-invariant operators.

If one were concerned about gauge-fixing artifacts, the key check is: does the effective action $S_k$ depend on the choice of axial gauge direction? Balaban proves that it does not: the block-spin construction is invariant under the lattice symmetries (including rotations that change the axial direction), and the effective action inherits this invariance.

**Impact on the claimed result:** None. Gauge invariance is maintained throughout by construction, and the axial gauge is a computational device that does not affect the gauge-invariant output.
