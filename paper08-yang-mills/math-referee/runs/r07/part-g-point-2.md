# G2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND

---

## Part G2, Point (a): Axial Gauge Fixing

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

Balaban's RG program uses axial gauge as a computational device. On the lattice, axial gauge sets all temporal links to the identity: U_{x,0} = 1. This is a legitimate gauge choice with several important properties:

1. **No Faddeev-Popov ghosts.** The FP determinant is trivial in axial gauge on the lattice. This eliminates an entire layer of complexity present in covariant gauges.

2. **No 1/p_0^2 singularities.** The notorious infrared singularities of the axial gauge propagator (1/p_0^2 poles) are continuum artifacts. On the lattice, all momenta are bounded by pi/a, so these singularities simply do not appear. The lattice provides a natural regulator for the axial gauge pathologies that plague continuum perturbation theory.

3. **Complete gauge fixing.** Axial gauge on the lattice fixes the gauge completely -- there is no residual gauge freedom to manage.

The choice of axial gauge is not merely convenient but strategically essential for Balaban's program: it provides a clean starting point for the multi-scale analysis without introducing the complications of ghost fields or gauge-fixing ambiguities.

**Impact on the claimed result:**

None. Axial gauge on the lattice is mathematically well-defined, introduces no artifacts, and is a standard tool in constructive lattice gauge theory.

---

## Part G2, Point (b): Gribov Problem

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The Gribov problem -- the existence of multiple gauge-equivalent configurations satisfying the same gauge condition -- is absent in this setting for the following reasons:

1. **Complete gauge fixing in axial gauge.** On a finite lattice with axial gauge (all temporal links set to identity), the gauge is completely fixed. There is a unique representative from each gauge orbit. No Gribov copies exist.

2. **Block-spin transformation structure.** The block-spin RG transformation averages over gauge orbits at the sub-block level. This averaging is performed by integrating over fine-lattice links with the gauge-fixed measure. At each RG step, the effective action on the coarse lattice is gauge-invariant by construction: the block-spin integration respects the gauge orbit structure because it integrates over all fine-lattice configurations consistent with the coarse-lattice boundary conditions.

3. **No Gribov ambiguities introduced at any step.** Since the initial gauge fixing is complete and each RG step preserves gauge invariance of the effective action, no Gribov copies are introduced at any stage of the multi-scale analysis.

This should be contrasted with continuum non-abelian gauge theories in Coulomb or Lorenz gauge, where the Gribov problem is a genuine obstruction. The lattice + axial gauge combination avoids this entirely.

**Impact on the claimed result:**

None. The Gribov problem does not arise in this framework.

---

## Part G2, Point (c): Gauge Invariance of the Final Result

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The gauge invariance of the final physical results is ensured through a clean separation between computational method and physical output:

1. **Schwinger functions from gauge-invariant observables.** The continuum Schwinger functions are constructed as correlation functions of gauge-invariant observables (Wilson loops, plaquette correlators, etc.). These are manifestly gauge-invariant quantities.

2. **Operator classification on gauge-invariant action.** The operator classification and deviation order argument -- which establishes that only dim-6, C-even operators contribute to the effective action at leading order -- is applied to the gauge-invariant effective action S_k[V], NOT to the gauge-fixed intermediate action. This is a crucial distinction: the classification constrains the space of gauge-invariant operators, not gauge-dependent computational intermediates.

3. **Intermediate gauge-fixing is transparent.** The axial gauge fixing at intermediate RG steps affects the computational method (how integrals are evaluated, how propagators are bounded) but not the final results. This is the standard principle that physical observables are independent of gauge choice, here made rigorous by the lattice framework.

The logical structure is: gauge-fix for computation, integrate out fine modes, obtain gauge-invariant effective action on coarser lattice, classify gauge-invariant operators, extract gauge-invariant Schwinger functions in the continuum limit.

**Impact on the claimed result:**

None. The proof correctly maintains gauge invariance of all physical quantities while using gauge-fixing only as a computational tool at intermediate steps.

---

## Overall Assessment

**Verdict: SOUND**

The treatment of gauge invariance through the RG flow is mathematically rigorous. Axial gauge on the lattice is a clean gauge choice with no pathologies (no ghosts, no Gribov copies, no infrared singularities). The block-spin RG preserves gauge invariance of the effective action at each scale. The final Schwinger functions and mass gap are constructed from gauge-invariant quantities, ensuring that the intermediate gauge-fixing does not contaminate the physical results. No issues found.
