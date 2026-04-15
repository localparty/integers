## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Axial gauge fixing.** Balaban uses axial gauge ($A_0 = 0$) as a computational device. On the lattice, axial gauge is well-defined: it completely fixes the gauge by setting all temporal link variables to the identity. The continuum spurious singularities ($1/p_0^2$ poles) are lattice artifacts of the continuum axial gauge propagator and do not appear on the lattice where the temporal direction is discrete. The Faddeev–Popov determinant is trivial in axial gauge on the lattice (the gauge group is completely fixed, with no residual gauge freedom to generate ghosts).

**(b) The Gribov problem.** On a finite lattice, axial gauge fixes the gauge uniquely: given a lattice configuration $\{U_\ell\}$, the axial gauge-fixed configuration is obtained by a unique sequence of gauge transformations that sets all temporal links to $\mathbf{1}$. There are no Gribov copies. The block-spin transformation averages over the gauge-fixed fast variables and projects the result back onto SU($N$); this procedure respects gauge invariance because the block-spin averaging commutes with gauge transformations (Balaban, CMP 95, Section 2). No Gribov-type ambiguities arise at intermediate scales.

**(c) Gauge invariance of the final result.** The Schwinger functions are constructed from gauge-invariant observables (plaquette traces, Wilson loops), which are manifestly gauge-invariant regardless of intermediate gauge-fixing. The effective action $S_k$ at intermediate steps is defined in axial gauge but the gauge-invariant observables extracted from it are independent of the gauge choice (by construction of the block-spin integration). The operator classification and deviation order argument (Part D) use gauge-invariant operators exclusively: $\mathrm{Tr}(F^3)$, $\mathrm{Tr}(DF)^2$, etc. are all gauge-invariant by construction. The gauge-fixing at intermediate steps does not affect the gauge-invariant content of the effective action.

**Impact on the claimed result:**
No impact. Gauge invariance is preserved through the construction by the standard mechanism: work in axial gauge for computational convenience, extract gauge-invariant results at the end.
