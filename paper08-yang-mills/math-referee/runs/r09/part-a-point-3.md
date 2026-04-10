## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) Lattice instantons.** The Bogomolny bound $E \geq (8\pi^2/g^2)|c_2|$ is a continuum result. On the lattice, the topological charge is defined via Lüscher's geometrical construction (Lüscher, CMP 85, 1982). The preprint addresses this explicitly in the "From the $k=0$ Sector to the Full Theory" corollary (Section 4.4):

> "For configurations in the small-field region $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$, the lattice topological charge $Q_L$ is an integer that coincides with the continuum $c_2$ up to corrections of order $O(a^2 \|F\|^2)$."

Rough lattice configurations with ill-defined topological charge lie in the large-field region $\Omega_l$ and are exponentially suppressed by $O(e^{-c/g_k^{2\epsilon}})$ (Balaban, CMP 119). The Bogomolny bound therefore applies to the dominant configurations in the path integral.

**The gap:** The treatment of "dislocations" — lattice configurations that evade smooth topological classification — is handled only implicitly via the large-field suppression. A more explicit statement that the lattice topological charge agrees with the continuum classification for all configurations contributing non-negligibly to the path integral would strengthen this point. This requires only clarifying the scope of Lüscher's construction relative to Balaban's small-field condition.

**(b) The restriction to $c_2 = 0$.** The restriction to $c_2 = 0$ is preserved under the dynamics by the Bogomolny energy barrier: transition amplitudes between topological sectors are suppressed by $O(e^{-8\pi^2/g^2})$ at weak coupling. The preprint states:

> "The Bogomolny energy barrier $E \geq (8\pi^2/g^2)|c_2|$ prevents tunneling between topological sectors."

This is physically correct but stated without full rigor. In the lattice path integral, tunneling between sectors is not literally prevented — configurations with any $c_2$ contribute. What is true is that the $c_2 \neq 0$ contributions are exponentially suppressed relative to $c_2 = 0$. The corollary makes this precise: $Z_k/Z_0 \leq C_k e^{-8\pi^2|k|\beta/N}$, which gives $\sigma \geq \sigma_0(1 - Ce^{-4\pi^2\beta/N}) > 0$.

The analysis is correct but compressed. A reader unfamiliar with lattice topology would benefit from a more explicit treatment of the lattice-continuum correspondence for the topological charge.

**Closable with:** 1 paragraph clarifying the scope of Lüscher's lattice topological charge construction and its compatibility with the small-field condition. The mathematical content is already present; it needs explicit statement.

**Impact on the claimed result:** None if closed. The Bogomolny suppression of non-trivial sectors is not on the critical path — the mass gap is established primarily in the $c_2 = 0$ sector, and the non-trivial sectors provide only exponentially small corrections.
