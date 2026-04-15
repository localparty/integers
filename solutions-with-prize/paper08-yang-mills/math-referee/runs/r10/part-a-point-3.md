## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Lattice instantons.**

The Bogomolny bound $E \geq (8\pi^2/g^2)|c_2|$ is a continuum result. On a finite lattice, the topological classification of gauge field configurations is non-trivial because rough lattice configurations (dislocations) can evade smooth topological classification.

The preprint addresses this via Lüscher's geometrical construction (CMP 85, 1982, Theorem 1). Lüscher assigns an integer topological charge $Q_L[U]$ to any lattice configuration $U$ satisfying $\|1 - U_P\| < \epsilon_L$, where $\epsilon_L > 0$ is a fixed geometric threshold depending only on $d$ and $G$, not on $a$ or coupling.

The connection to Balaban's construction is explicit:
- In the small-field region $\Omega_s = \{|F_{\mu\nu}| < g_k^{1-\epsilon}\}$, plaquette variables satisfy $\|1 - U_P\| \leq Ca^2 g_k^{1-\epsilon} < \epsilon_L$ for small $g_k$
- Therefore every configuration in $\Omega_s$ carries a well-defined Lüscher topological charge agreeing with the continuum $c_2$
- Configurations in the large-field region $\Omega_l$ (including rough lattice dislocations) contribute at level $O(e^{-c/g_k^{2\epsilon}})$ by Balaban's large-field bounds (CMP 119)

The partition function decomposes as $Z = \sum_k Z_k$ with $Z_k/Z_0 \leq C_k e^{-8\pi^2|k|\beta/N}$, so non-trivial sectors are exponentially suppressed. The string tension correction is bounded:

$$\sigma \geq \sigma_0\left(1 - C\,e^{-4\pi^2\beta/N}\right) > 0$$

This handles the lattice instanton issue completely. Rough lattice configurations that would evade topological classification are in $\Omega_l$ and contribute negligibly.

**(b) The restriction to $c_2 = 0$.**

The restriction to the trivial topological sector is justified dynamically, not imposed ad hoc. The Bogomolny bound $E \geq (8\pi^2/g^2)|c_2|$ provides exponential suppression of all non-trivial sectors: the ratio $Z_{c_2}/Z_0 \leq C e^{-8\pi^2|c_2|\beta/N}$ makes $c_2 \neq 0$ sectors negligible at any finite $\beta$.

Quantum tunneling between sectors: on the lattice with compact gauge group, there is no tunneling obstruction (all sectors are connected in field space). However, tunneling amplitudes are suppressed by the instanton action $e^{-8\pi^2/g^2}$. The preprint correctly accounts for this: the instanton contribution to the mass gap shift is $O(e^{-8\pi^2/g_k^2})$, which on the asymptotically free trajectory ($g_k^2 \sim 1/(b_0 k \ln 2)$) decays faster than any power of $g_k$. This is negligible compared to the $g_k^4 \hat{\Delta}_k^2$ bound from the dimension-6 operators.

The dynamics preserves the sector decomposition in the following sense: the $c_2 = 0$ sector dominates the partition function, and the mass gap established in the $c_2 = 0$ sector is corrected by instanton contributions that are negligibly small. The corrected mass gap remains strictly positive.

**Impact on the claimed result:**

None. The Bogomolny bound on the lattice is correctly handled via Lüscher's geometrical construction, and the topological sector restriction is dynamically justified with rigorous bounds on instanton corrections.
