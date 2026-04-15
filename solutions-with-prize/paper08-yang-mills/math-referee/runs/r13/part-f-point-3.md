## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: the limits a -> 0 and L -> infinity commute, via the Moore-Osgood theorem.

**(a) Uniformity in L.** The connected matrix element <1|E_k(0)|1>_c is claimed volume-independent. The argument:

The one-particle state |1> at zero spatial momentum has normalization |1> = (1/sqrt{V}) Sum_x |1, x> where V = L^3 is the spatial volume. The operator E_k(0) is local (supported near the origin). The connected matrix element:

  <1|E_k(0)|1>_c = (1/V) Sum_{x,y} <1,x|E_k(0)|1,y>_c

By translation invariance, the summand depends only on x - y. By exponential clustering (from the mass gap): |<1,x|E_k(0)|1,y>_c| <= C e^{-Delta|x-y|}. The double sum:

  (1/V) Sum_{x,y} f(x-y) = Sum_z f(z) (independent of V for V >> 1/Delta^3)

For L >> 1/Delta: the sum over z = x - y converges to the infinite-volume value, independent of V. The finite-volume correction is O(e^{-Delta L}).

This cancellation of the 1/V normalization with the spatial sum is standard in lattice field theory (linked cluster theorem). It is proved rigorously using the cluster expansion bounds.

**(b) The infinite-volume mass gap.** For fixed a, Delta(a, L) -> Delta(a, infinity) as L -> infinity. The rate of convergence is O(e^{-Delta(a, infinity) * L}).

Uniformity in a: on the AF trajectory, Delta(a, infinity) is bounded below by Delta_inf > 0 (the mass gap is preserved by the RG). For any a on the trajectory, Delta(a, infinity) >= Delta_inf - epsilon > 0 (from the convergence of the RG sum). So the rate e^{-Delta * L} is uniform in a: for L > L_0 = C/Delta_inf, the finite-volume correction is bounded by e^{-Delta_inf L/2} for all a on the trajectory.

**(c) Exponential clustering in finite volume.** On the periodic lattice (Z/LZ)^4, the spectrum is discrete (the transfer matrix on a compact space has discrete eigenvalues). The "mass gap" is the gap between the ground state and first excited state: Delta(L) = E_1(L) - E_0(L).

For L >> 1/Delta(infinity): the finite-volume spectral gap Delta(L) approaches Delta(infinity) with corrections O(e^{-Delta L}). This is because the finite-volume eigenstates are exponentially close to the infinite-volume eigenstates (by the cluster decomposition). The spectral gap is bounded below: Delta(L) >= Delta(infinity) - C e^{-Delta(infinity) L} > Delta(infinity)/2 for L > C'/Delta(infinity).

The uniformity in L is established: for L > L_0 (a fixed length scale determined by the mass gap), the finite-volume spectral gap is within a factor of 2 of the infinite-volume gap, uniformly in a.

The Moore-Osgood theorem then gives: lim_{a->0} lim_{L->infinity} S_n(a, L) = lim_{L->infinity} lim_{a->0} S_n(a, L) = S_n(infinity, infinity), provided both iterated limits exist and one of them is uniform. The uniformity in L (at fixed a) is established by the exponential clustering bounds.

No error found. The thermodynamic limit argument is standard lattice field theory.

**Impact on the claimed result:** None. The commutativity of limits is correctly established.
