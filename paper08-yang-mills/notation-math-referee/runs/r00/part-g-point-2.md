## Part G, Point 2: Gauge Invariance Through the RG

**Weight:** MEDIUM
**Verdict:** SOUND (Balaban's RG preserves gauge invariance by construction; axial gauge is used as a computational device but the final effective action $S_k[V]$ is gauge-invariant)

**Finding:**

(a) **Axial gauge fixing.** Balaban's CMP series uses axial gauge for the propagator computation. In axial gauge, the Faddeev–Popov determinant is trivial, so there are no ghosts. The block-spin transformation produces an effective action $S_k[V]$ that is gauge-invariant *as a functional of the block link variables $V_\ell$*, regardless of the intermediate gauge fixing. This is a standard property of lattice block-spin RG (Balaban CMP 109 §2; Wilson–Kogut 1974).

The axial gauge "spurious singularities" (the $1/p_0^2$ poles in the continuum axial gauge propagator) are *not present on the lattice*: the lattice axial gauge propagator is well-defined for any non-zero spatial momentum, and the temporal axial gauge corresponds to a specific choice of link variables that makes the time-direction links trivial. This is fine.

Sound.

(b) **Gribov problem.** On a finite lattice, the gauge group is compact and the gauge orbits are closed manifolds. Axial gauge in the lattice is a *complete* gauge fixing (it picks a unique representative on each orbit by setting time-direction links to identity). There are no Gribov copies in lattice axial gauge.

For other gauge fixings (Landau, Coulomb, etc.), Gribov copies exist but the preprint does not use these. Sound.

The block-spin transformation averages over fluctuations and could in principle introduce Gribov-like ambiguities at intermediate scales, but the construction is performed in the same axial gauge throughout, so the issue does not arise.

(c) **Gauge invariance of the final result.** The Schwinger functions used in OS reconstruction are constructed from gauge-invariant observables (plaquette traces $\mathrm{Tr}(U_P)$, Wilson loops $W_C$, etc.). These are gauge-invariant by construction (under the SU(N) gauge transformations $U_\ell \to \Omega_x U_\ell \Omega_y^{-1}$), independent of the gauge fixing used internally. Sound.

The Ward identities are derived in §5.7(f) "Remark (Ward identities)" using the invariance of Haar measure under group translations:
$$\langle \mathcal{O}[U^\Omega]\rangle = \langle \mathcal{O}[U]\rangle$$
This is exact for all $a > 0$ on the lattice, and converges to the continuum Ward identities in the $a \to 0$ limit (as distributions). Sound.

The Schwinger–Dyson equations (§5.7(f) lattice SD argument) similarly use Haar invariance and translate to continuum SD equations in the limit. The "scope" remark correctly notes that the SD equation applies to *gauge-invariant* observables and that $A_\mu^a(x)$ is not a Hilbert-space operator. This is the correct interpretation for a confining theory.

**Impact on the claimed result:** Sound. Gauge invariance is preserved throughout the construction. The axial gauge is used as a computational device in Balaban's RG, but the physical observables and the final effective action are gauge-invariant.
