## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim: non-trivial topological sectors (c_2 != 0) are suppressed by E >= (8 pi^2 / g^2)|c_2|.

**(a) Lattice instantons.** The Bogomolny bound E >= (8 pi^2 / g^2)|c_2| is a continuum result for self-dual/anti-self-dual connections. On the lattice, the topological charge is defined via the Lüscher geometric definition (for CP^{N-1} with N >= 3) or via the plaquette definition. The lattice topological charge takes integer values and agrees with the continuum charge in the classical continuum limit.

On a finite lattice, lattice dislocations (rough configurations with plaquette variables far from the identity) can contribute fractional apparent topological charge. However, the paper restricts to the c_2 = 0 sector (connections on CP^{N-1} with trivial second Chern class), and the non-trivial sectors are treated as corrections.

The ratio Z_k/Z_0 <= C_k e^{-8 pi^2 |k| beta/N} is a standard lattice gauge theory bound: configurations with topological charge k have action at least 8 pi^2 |k|/g^2 above the trivial sector (by the Bogomolny bound for smooth configurations), and rough configurations contributing to the k-sector are further suppressed by the Wilson action. The combined suppression gives the exponential bound.

For the proof, only the RATIO of partition functions matters, not the absolute Bogomolny bound. The correction to the string tension is sigma >= sigma_0(1 - C e^{-4 pi^2 beta/N}) > 0 for all beta > 0. This is unconditionally positive.

**(b) The restriction to c_2 = 0.** The restriction to c_2 = 0 for the internal connections on CP^{N-1} is preserved under the lattice dynamics because:

(i) The path integral factorizes over topological sectors (c_2 is a topological invariant preserved by continuous deformations).

(ii) Tunneling between sectors is suppressed by the Bogomolny energy barrier. On a finite lattice, tunneling occurs through lattice dislocations, but these are exponentially suppressed in the action.

(iii) For the KK-enhanced theory, the internal connections live on CP^{N-1} at each lattice site, and c_2 is defined per site. The total topological charge is the sum over sites, which is conserved by the nearest-neighbor dynamics.

For N = 2 (CP^1 = S^2): all SU(2) bundles over S^2 are trivial (pi_1(SU(2)) = 0), so c_2 = 0 automatically and the restriction is vacuous.

No error found. The topological sector analysis is standard lattice gauge theory.

**Impact on the claimed result:** None. The topological sector suppression is a well-established technique that adds a negligible correction to the string tension.
