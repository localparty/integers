## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Axial gauge fixing.** Balaban uses axial gauge as a computational device. In axial gauge on the lattice, the link variables along a chosen direction (say $\hat{0}$) are set to the identity: $U_{(x,\hat{0})} = \mathbf{1}$. This completely fixes the gauge (no residual gauge freedom, no Gribov copies on the lattice). The Faddeev-Popov determinant is trivial (equal to 1), so there are no ghost fields.

The continuum axial gauge has spurious $1/p_0^2$ singularities (the axial gauge propagator has poles at $p_0 = 0$). On the lattice, these singularities are absent: the lattice propagator is a finite sum over a discrete momentum space, with no poles. The lattice axial gauge is clean. The $1/p_0^2$ singularities are a continuum artifact that does not appear at any finite lattice spacing.

**(b) The Gribov problem.** On a finite lattice with compact gauge group SU($N$), axial gauge completely fixes the gauge: given the link variables in all directions except $\hat{0}$ and the boundary conditions, the axial gauge condition determines a unique representative from each gauge orbit. There are no Gribov copies.

Balaban's block-spin transformation does not introduce Gribov-type ambiguities. The block-spin averages over fine-link products within a block, then projects to SU($N$) via the polar decomposition. This averaging is performed in a fixed gauge (axial gauge at each scale), and the projection is unique (the nearest SU($N$) element to the average is unique for averages near the identity, which is guaranteed in the small-field region).

**(c) Gauge invariance of the final result.** The Schwinger functions are constructed from gauge-invariant observables (plaquette traces, Wilson loops). These are manifestly gauge-invariant regardless of intermediate gauge-fixing. The effective action $S_k[V]$ is gauge-invariant at each step (Balaban, CMP 109, Section 2): the block-spin integration is performed over gauge orbits, and the result depends only on the gauge-invariant content of the block link variables.

The concern about gauge-fixed effective action having different properties: the operator classification (Section 5.6, Part III.3) is performed on gauge-invariant operators. The $\mathcal{C}$-even condition, the dimension counting, and the deviation order are all properties of gauge-invariant operators. The gauge-fixing affects only the intermediate computation, not the classification of the final gauge-invariant remainder $E_k[V]$.

**Impact on the claimed result:** None. Gauge invariance is correctly maintained throughout the construction.
