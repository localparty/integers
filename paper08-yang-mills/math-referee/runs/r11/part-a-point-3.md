## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Lattice instantons.**

The Bogomolny bound $E \geq (8\pi^2/g^2)|c_2|$ is a continuum result from the inequality $\|F\|^2 \geq \|F \pm \tilde{F}\|^2 \mp 2\langle F, \tilde{F}\rangle$, where the topological charge $\langle F, \tilde{F}\rangle = 8\pi^2 c_2$. On the lattice, the situation is more subtle: lattice configurations can have fractional or ambiguous topological charge, and "dislocations" (lattice artifacts with action $O(1/g^2)$ but ill-defined topology) exist.

However, the preprint handles this correctly. The topological classification is on the internal $\mathbb{CP}^{N-1}$, not on the 4D lattice. Since $\mathbb{CP}^{N-1}$ is treated as a continuous manifold (the KK fiber at each lattice site), the Chern-Weil classification of connections on $\mathbb{CP}^{N-1}$ is exact. The topological charge $c_2 \in \mathbb{Z}$ is well-defined for smooth connections on $\mathbb{CP}^{N-1}$, and the Bogomolny bound holds as a continuum statement on the fiber. Lattice artifacts on the 4D lattice do not affect the internal topology.

The non-trivial sectors contribute to the partition function with weight $e^{-8\pi^2|c_2|\beta/N}$, which is exponentially suppressed at weak coupling ($\beta$ large). This suppression is used in the Corollary to Theorem 4 to show that non-trivial sectors give negligible corrections.

**(b) The restriction to $c_2 = 0$.**

The proof works primarily in the $c_2 = 0$ sector. The restriction is justified because: (i) the partition function decomposes as a sum over topological sectors $Z = \sum_{c_2} Z_{c_2}$; (ii) each sector with $c_2 \neq 0$ contributes $O(e^{-8\pi^2|c_2|\beta/N})$ relative to the trivial sector; (iii) the free energy is dominated by $c_2 = 0$.

Can quantum fluctuations tunnel between sectors? On a lattice with fixed topology of the internal space at each site, tunneling between sectors requires the internal connection to pass through a singular (infinite-action) configuration. In the continuum path integral on $\mathbb{CP}^{N-1}$, different topological sectors are summed over, but each with the appropriate Boltzmann suppression. The dynamics does not mix sectors at the level of the transfer matrix — the transfer matrix preserves the topological charge of the internal connection because a single time step cannot change the topology without paying an energy $\geq 8\pi^2/g^2$.

The restriction to $c_2 = 0$ is preserved under the dynamics, and the corrections from $c_2 \neq 0$ are exponentially small in $\beta$. On the asymptotically free trajectory, these corrections are $O(e^{-\mathrm{const}/g_k^2})$, far smaller than any power of $g_k$.

**Impact on the claimed result:** None. The Bogomolny bound is used correctly, and the topological sector restriction is justified.
