## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: Balaban's block-spin preserves gauge invariance: the effective action S_k[V] is gauge-invariant at each step k.

**(a) Axial gauge fixing.** Balaban uses axial gauge (temporal gauge, A_0 = 0 on the tree) as a computational device. On the lattice:

  - No FP ghosts: the Faddeev-Popov determinant in axial gauge is trivial (det = 1), because axial gauge is a complete gauge fixing on the lattice (no residual gauge freedom).
  
  - No spurious singularities: the continuum axial gauge propagator has 1/p_0^2 poles (the "spurious" singularities), but on the lattice, these are absent — the lattice discretization replaces 1/p_0^2 with 1/(4 sin^2(p_0 a/2)/a^2), which is bounded.
  
  - The axial gauge is used only within each block-spin step to organize the perturbative expansion of the fluctuation integral. The final result (the effective action S_k[V]) is gauge-invariant regardless of the intermediate gauge choice.

**(b) The Gribov problem.** On a finite lattice with compact gauge group, the gauge orbit is compact and the number of Gribov copies is finite. Axial gauge is unique on the lattice: it completely fixes the gauge by setting link variables on a maximal tree to the identity. There are no Gribov copies in axial gauge on a finite lattice.

The block-spin transformation averages over fluctuations within each block, not over gauge orbits. The gauge is fixed (axially) within each block, the fluctuation integral is performed, and the result is expressed in terms of gauge-invariant block variables V. No Gribov ambiguity arises because the gauge fixing is complete and unique at each step.

**(c) Gauge invariance of the final result.** The Schwinger functions are constructed from gauge-invariant observables (plaquette traces s_P = 1 - (1/N) Re Tr U_P, Wilson loops W(C)). These are manifestly gauge-invariant at each lattice spacing and in the continuum limit.

The proof uses the structure of the effective action S_k (which is gauge-fixed at intermediate steps in the perturbative expansion). But the RESULTS — the operator norms, the deviation orders, the spectral gap — are gauge-invariant properties of the transfer matrix (which is gauge-invariant by construction).

Specifically: the deviation order dev(O) is a property of the gauge-invariant operator O, computed using the gauge-invariant transfer matrix hat{T}. The classification of dim-6 operators is performed on gauge-invariant operators. The spectral lemma is applied to gauge-invariant matrix elements. No step requires the gauge-fixed effective action to have special properties beyond those established by Balaban.

The gauge choice (axial vs. Coulomb vs. Lorenz) affects the organization of the perturbative expansion but not the final gauge-invariant results. This is a standard feature of Balaban's construction and is well-understood in constructive QFT.

No error found. Gauge invariance is maintained throughout the construction.

**Impact on the claimed result:** None. Gauge invariance is a built-in feature of the lattice gauge theory framework.
