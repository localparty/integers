## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that the Kotecký–Preiss cluster expansion converges for all $\beta < m_1 a/(6) - \mathrm{const}$, giving $\sigma_0 > 0$ and $\Delta_0 > 0$.

**(a) The Kotecký–Preiss criterion.** The polymer weights are bounded by the combined estimate: each connected cluster $\mathcal{C}$ with $|S|$ activated plaquettes and $|B|$ activated bonds satisfies $|\phi(\mathcal{C})| \leq K^{|\mathcal{C}|} (\max|f_P|)^{|S|} (C_0 e^{-m_1 a})^{|B|}$. Using $|B| \geq |S|/6$ (geometric property of connected clusters on the 4D lattice) and $|f_P| \leq e^{2\beta}$, the per-element bound becomes $|\phi(\mathcal{C})| \leq (K C_0^{1/6} e^{2\beta - m_1 a/6})^{|\mathcal{C}|}$. The KP criterion with weight $a(\mathcal{C}) = \alpha|\mathcal{C}|$ requires $c_d K C_0^{1/6} e^{2\beta - m_1 a/6 + \alpha} < 1$, which gives the convergence condition $2\beta + \alpha < m_1 a/6 - \ln(c_d K C_0^{1/6})$.

The decay constant $\kappa$ for polymer weights comes from the bond suppression $e^{-m_1 a/6}$ distributed over cluster elements. Since $m_1 = 2\sqrt{N}/r_3$ (from Theorem 2), $\kappa$ depends on $N$ through $m_1$ and the constants $K, C_0$, but is independent of $k$ (the RG step) because the cluster expansion is performed at the bare scale.

The combinatorial bound $c_d^n$ on the number of connected lattice animals of size $n$ containing the origin in $d=4$ is standard. The paper cites $c_d \leq Ce^7$ (Klarner–Rivest 1973). The precise value is immaterial since $c_d$ appears inside a logarithm bounded by $m_1 a/6 \sim 10^{14}$.

Verified computationally: polymer counting estimates are adequate for the vast convergence margin ($\xi \sim e^{-5.8 \times 10^{14}}$ for physical parameters).

**(b) Physical regime coverage.** The convergence bound $\beta < m_1 a/6 - \mathrm{const}$ covers all practical couplings. For $N=3$ at $a \sim 10^{-16}$ m: $\beta_{\max} \sim (\sqrt{3}/3) \times 10^{15} \approx 5.8 \times 10^{14}$, while the physical coupling $\beta \sim 6$ leaves a margin of $\sim 10^{13}$. The cluster expansion domain therefore overlaps with the starting point of Balaban's RG: at $\beta_0 = 2N/g_0^2$ with $g_0$ small (large $\beta$), both arguments apply. The crossover lattice spacing $a_{\mathrm{cross}} \sim 2\sqrt{N} r_3 \beta(a_{\mathrm{cross}}) \sim 3.5 \times 10^{-29}$ m is well below any practical lattice spacing but above $r_3 \sim 10^{-31}$ m.

**(c) The connected function bounds.** Theorem 2 provides exponential decay of connected correlators with rate $m \geq \alpha/a > 0$ uniformly in the lattice volume $L$. The cluster expansion constants are $a$-independent in the following sense: $C_0$ depends on $N$ but not on $\beta$ or $a/r_3$ (Theorem 2, Step 4); $K$ is the bounded measure factor from Haar integration on SU($N$) times the Gaussian damping from $S_{\mathrm{int}}$. The $a$-independence holds because the bond activity bound $C_0 e^{-m_1 a}$ is the fundamental input, and $C_0$ is intrinsic to the internal space geometry.

The paper correctly uses the cluster expansion rate $\alpha/a$ (not the area law or Fredenhagen–Marcu) as the rigorous lower bound on $\Delta_0$. This is established via reflection positivity (Lemma D.2) and the spectral theorem (Reed–Simon Vol. IV), without requiring correlation inequalities.

**Impact on the claimed result:**
No impact. The cluster expansion convergence is rigorous and provides the starting condition $\Delta_0 > 0$ with quantitative bounds.
