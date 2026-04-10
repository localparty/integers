## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Lattice instantons.** The Bogomolny bound $E \geq (8\pi^2/g^2)|c_2|$ is a continuum result. On a finite lattice, the topological charge requires careful definition. The preprint uses Luscher's geometrical construction (CMP 85, 1982), which assigns an integer topological charge to lattice configurations whose plaquette variables are sufficiently close to unity. This definition is rigorous and agrees with the continuum topological charge for smooth configurations.

For rough lattice configurations ("dislocations") where plaquette variables are far from unity, the topological classification breaks down. However, these configurations are exponentially suppressed by the Wilson action: $e^{-\beta \sum_P(1 - \mathrm{Re}\,\mathrm{Tr}\,U_P/N)} \leq e^{-c\beta}$ when plaquettes deviate significantly from unity. In the weak-coupling regime where Balaban's small-field condition applies, only smooth configurations contribute to the functional integral, and Luscher's topological charge is well-defined.

The compatibility with Balaban's small-field condition is explicitly verified in the preprint (Section 4.4, Corollary): in the small-field region $\Omega_s$, all configurations satisfy the Luscher admissibility condition, so the topological charge is well-defined and the Bogomolny bound applies.

**(b) The restriction to $c_2 = 0$.** The restriction to the trivial topological sector ($c_2 = 0$) for internal connections on $\mathbb{CP}^{N-1}$ is dynamically stable because:

1. On a finite lattice with discrete path integral, topological sectors are defined by integer-valued charges. The lattice action $S[U, A]$ is a continuous function of the link variables $U$ and internal connections $A$. Quantum fluctuations cannot continuously interpolate between integer-valued topological charges.

2. Non-trivial sectors ($c_2 \neq 0$) are suppressed by the Bogomolny bound: $Z_{c_2}/Z_0 \leq C_{c_2}\,e^{-8\pi^2|c_2|\beta/N}$. This suppression grows exponentially with $\beta = 2N/g^2$.

3. The partition function decomposes as $Z = \sum_{c_2} Z_{c_2}$, and the $c_2 = 0$ sector dominates: $Z_0/Z \geq 1 - Ce^{-8\pi^2\beta/N}$. The mass gap in the full theory satisfies $\sigma(\beta) \geq \sigma_0(\beta)(1 - Ce^{-4\pi^2\beta/N}) > 0$ (Corollary to Theorem 4).

**Impact on the claimed result:** None. The topological sector decomposition is standard. The Bogomolny suppression of non-trivial sectors is rigorous on the lattice (using Luscher's construction), and the restriction to $c_2 = 0$ is justified by the exponential suppression of other sectors.
