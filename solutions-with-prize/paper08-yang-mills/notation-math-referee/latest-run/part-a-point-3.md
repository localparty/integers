## Part A, Point 3: The Bogomolny Bound on the Lattice

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim is that non-trivial topological sectors ($c_2 \neq 0$) are suppressed by $E \geq (8\pi^2/g^2)|c_2|$, and that the restriction to $c_2 = 0$ is preserved under the dynamics.

**(a) Lattice instantons.** The Bogomolny bound is a continuum result. On a finite lattice, the paper addresses this through Lemma A3.1 (Lüscher admissibility under the cluster measure). The key insight: the cluster expansion measure concentrates on "admissible" configurations where $\mathrm{Tr}\{\mathbf{1} - U_P\} < \epsilon_L$ for all plaquettes, with probability at least $1 - C_\Lambda e^{-m_1 a_0/6 + 2\beta}$. On admissible configurations, Lüscher's geometric construction (CMP 85, 1982) provides a well-defined integer topological charge $Q_L$ agreeing with the continuum $c_2$ up to $O(a^2 \|F\|^2)$.

Rough configurations (violating admissibility) have ill-defined topological charge but are exponentially suppressed. The non-trivial sector correction is bounded by $|Z_{c_2 \neq 0}/Z_{c_2 = 0}| \leq C e^{-8\pi^2/g_0^2} + C_\Lambda e^{-m_1 a_0/6 + 2\beta}$, which is negligible at physical parameters ($\sim e^{-10^{14}}$).

The argument is self-contained and does not rely on Balaban's small-field condition at the bare cluster-expansion scale — it uses only the ingredients of Theorems 2 and 3.

**(b) The restriction to $c_2 = 0$.** The paper argues the restriction is preserved via the Bogomolny energy barrier: transition amplitudes between sectors with different $c_2$ are suppressed by $O(e^{-8\pi^2/g^2})$. The Corollary to Theorem 4 shows that $\sigma \geq \sigma_0(1 - Ce^{-4\pi^2\beta/N}) > 0$ for all $\beta > 0$, including the correction from non-trivial sectors.

A subtlety: on the lattice, "tunneling between topological sectors" is not well-defined in the same way as in the continuum. However, the Bogomolny suppression $e^{-8\pi^2|k|\beta/N}$ controls the partition function ratio $Z_k/Z_0$ directly, without needing a tunneling interpretation. The geometric sum over sectors converges and gives a positive correction factor. This is rigorous as stated.

The treatment of lattice topology is careful: Lüscher admissibility provides the bridge between lattice and continuum topological classification, and the cluster expansion ensures that the overwhelming majority of configurations are admissible.

**Impact on the claimed result:**
No impact. The restriction to $c_2 = 0$ is justified, and the correction from non-trivial sectors is under rigorous control.
