## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

(a) Axial gauge fixing: On the LATTICE, axial gauge is implemented by fixing temporal link variables to the identity ($U_{(x,\hat{0})} = \mathbf{1}$). This is a complete gauge fixing — every lattice gauge configuration has a unique representative in axial gauge. There are no Gribov copies (the gauge orbit is completely fixed). The lattice axial gauge propagator does not have the $1/p_0^2$ singularities of the continuum axial gauge — these are continuum artifacts arising from the non-compact nature of the continuum gauge group action. On a finite lattice with compact gauge group, the gauge fixing is smooth and complete. Balaban uses axial gauge as a computational device in his construction of the fluctuation integral. In axial gauge, the Faddeev-Popov determinant is trivial (= 1), so there are no ghost fields. SOUND.

(b) The Gribov problem is absent on the finite lattice in axial gauge because axial gauge is a complete gauge fixing (no Gribov copies). Balaban's block-spin transformation preserves gauge invariance: the block-averaged field $V_B$ is defined via gauge-equivariant averaging followed by SU(N) projection, which is gauge-covariant by construction. At each blocking step, the gauge fixing is applied to the fine fields (which are integrated out), while the block fields retain their gauge freedom. The effective action $S_k[V]$ is a gauge-invariant functional of the block link variables. No Gribov ambiguities are introduced at intermediate scales. SOUND.

(c) The gauge invariance of the final result is guaranteed because: (i) the Schwinger functions are constructed from gauge-invariant observables (Wilson loops, plaquette traces); (ii) the effective action $S_k[V]$ is gauge-invariant at each step (Balaban's construction preserves this); (iii) the gauge fixing is a computational device used within the block-spin integration but does not affect the gauge-invariant output. The operator classification (dimension-6 operators) is performed on gauge-invariant operators, so the gauge-fixed intermediate structure does not affect the deviation order argument. The perturbative gauge-fixing artifacts (propagator poles, ghost loops) are absent because: (i) there are no ghosts in axial gauge; (ii) the propagator is defined non-perturbatively via the resolvent $(-D^2[V] + m_W^2)^{-1}$, which is smooth and bounded in the small-field region. SOUND.

**Impact on the claimed result:** None. Gauge invariance is maintained throughout the construction by standard mechanisms: axial gauge on the lattice (complete, no Gribov copies), gauge-equivariant block-spin, and gauge-invariant observables.
