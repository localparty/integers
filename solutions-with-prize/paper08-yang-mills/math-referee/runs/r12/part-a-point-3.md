## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** SOUND

---

**Finding:**

**(a) Lattice instantons and the topological charge.** The Bogomolny bound $E \geq (8\pi^2/g^2)|c_2|$ is a continuum result. On the finite lattice, topological charge must be defined with care. The preprint uses Lüscher's geometrical construction (Lüscher, CMP 85, 1982; cited explicitly in the Corollary proof in Section 4.4): for configurations in the small-field region $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$, the lattice topological charge $Q_L$ is an integer that coincides with the continuum $c_2$ up to $O(a^2\|F\|^2)$ corrections.

The preprint states: "Lüscher's construction (CMP 85, 1982, properties (i)–(v)) assigns an integer topological charge $Q_L[U]$ to any lattice configuration $U$ for which the plaquette variables satisfy $\|1 - U_P\| < \epsilon_L$... Balaban's small-field condition $\Omega_s = \{|F_{\mu\nu}| < g_k^{1-\epsilon}\}$ implies $\|1 - U_P\| \leq Ca^2 g_k^{1-\epsilon} < \epsilon_L$ for $g_k$ sufficiently small."

This correctly handles the "dislocation" issue: rough lattice configurations that would evade topological classification (Lüscher's dislocations) lie outside $\Omega_s$ and are exponentially suppressed by $O(e^{-c/g_k^{2\epsilon}})$. The preprint explicitly states this: "configurations outside $\Omega_s$ contribute to all observables at the level $O(e^{-c/g_k^{2\epsilon}})$, which is negligible compared to any power of $g_k$ on the AF trajectory." This is correct and standard (see Brydges–Seiler–Zitter 1983 for similar suppression arguments). SOUND.

**(b) The restriction to $c_2 = 0$ and tunneling.** The proof restricts to the $k=0$ topological sector ($c_2 = 0$, continuously deformable to $A=0$). The extension to the full theory uses the Bogomolny energy bound: non-trivial sectors carry energy $E \geq (8\pi^2/g^2)|c_2|$, suppressing contributions by $Z_{c_2}/Z_0 \leq C_{c_2} e^{-8\pi^2|c_2|\beta/N}$.

The Corollary after Theorem 4 gives the string tension bound:
$$\sigma \geq \sigma_0 - \frac{1}{TR}\ln\Bigl(1 + \textstyle\sum_{k \neq 0} C_k e^{-8\pi^2|k|\beta/N}\Bigr).$$
The geometric sum gives factor $(1 - Ce^{-4\pi^2\beta/N})$, strictly positive for all $\beta > 0$. Combined with $\sigma_0 > 0$, this gives $\sigma > 0$. SOUND.

The Bogomolny bound on the lattice is not used as a rigorous operator inequality — it enters only through the partition function suppression $e^{-8\pi^2\beta/N}$, which is a standard weak-coupling estimate (Berg–Lüscher 1981; Seiler 1982 Ch. 5). Quantum tunneling between sectors is suppressed by this factor, and the cluster expansion is performed entirely within the $c_2 = 0$ sector. The extension to the full theory via the Corollary argument is correct.

**Impact on the claimed result:** No gap. The topological sector analysis is handled correctly using Lüscher's construction for small-field configurations and the Bogomolny partition function suppression for non-trivial sectors. The restriction to $c_2 = 0$ is justified and the correction to the string tension is controlled.
