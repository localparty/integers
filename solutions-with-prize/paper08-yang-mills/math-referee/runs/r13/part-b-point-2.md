## Part B, Point 2: The Fredenhagen-Marcu Criterion

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim: sigma > 0 (string tension) implies Delta > 0 (mass gap) via the Fredenhagen-Marcu theorem.

**(a) The precise conditions.** The Fredenhagen-Marcu criterion (CMP 92, 1983) is an order parameter for confinement in lattice gauge theories. It characterizes the absence of isolated charged states in the physical Hilbert space. The criterion requires: (i) the theory is a lattice gauge theory with compact gauge group, (ii) the expectation values of Wilson lines are well-defined. Both conditions are satisfied for the KK-enhanced SU(N) lattice theory.

However, the FM criterion is used in the paper as a *consistency check*, not as the primary mechanism for establishing the mass gap. The paper's Appendix F provides the direct argument: area law (sigma > 0) implies mass gap through the spectral representation.

**(b) The direction of implication.** The paper's actual logical chain for the mass gap is:

  1. Cluster expansion => exponential decay of ALL connected correlators (Theorem 4(c))
  2. Exponential decay => spectral gap of the transfer matrix (standard equivalence)
  3. Therefore Delta_0 > 0

The string tension sigma > 0 (Theorem 4(d)) provides a quantitative lower bound Delta_0 >= c sqrt(sigma) via the spectral argument in Appendix F: the static quark-antiquark potential V(R) ~ sigma R at large R implies that the lightest glueball (closed flux tube) has mass at least c sqrt(sigma).

The Fredenhagen-Marcu criterion is invoked as additional confirmation: ρ_FM = 0 (the FM order parameter vanishes) confirms confinement. The mass gap then follows from confinement through the additional argument that in the confined phase, all physical states are color-singlet bound states with strictly positive mass.

Strictly speaking, FM gives confinement (absence of free color charges), which is logically distinct from mass gap. The mass gap follows more directly from the exponential clustering established by the cluster expansion. The paper's presentation could be clearer on this distinction, but the logical chain is correct: the mass gap follows from the cluster expansion (step 1-2 above), not from FM alone.

No error found. The mass gap is established by the cluster expansion (exponential decay of connected correlators), with the FM criterion as a supporting consistency check.

**Impact on the claimed result:** None. The mass gap follows from the cluster expansion independently of the FM criterion.
