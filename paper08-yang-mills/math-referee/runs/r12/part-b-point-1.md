## Part B, Point 1: Cluster Expansion Convergence

**Weight:** MEDIUM
**Verdict:** SOUND

---

**Finding:**

**(a) The Kotecký-Preiss criterion.** Theorem 3 (Section 4.3) gives an explicit derivation of the convergence condition using the Kotecký-Preiss (KP) criterion (Kotecký–Preiss, CMP 103, 1986). The derivation:

1. Each connected cluster $\mathcal{C}$ on the 4D hypercubic lattice satisfies $|B_\mathcal{C}| \geq |S_\mathcal{C}|/6$ (each plaquette touches at most 6 bonds).
2. Using the bond activity bound $|g_b| \leq C_0 e^{-m_1 a}$ (Theorem 2) and plaquette activity bound $|f_P| \leq e^{2\beta}$, each cluster element carries weight $\leq (K C_0^{1/6} e^{2\beta - m_1 a/6})^{|\mathcal{C}|}$.
3. The KP convergence criterion requires $c_d K C_0^{1/6} e^{2\beta - m_1 a/6 + \alpha} < 1$, giving the claimed condition.

The lattice animal constant $c_d$ for $d=4$ is $c_d \leq Ce^7$ (Klarner–Rivest 1973), which is a finite computable constant. The $N$-dependence of $C_0$ and $K$ (through the Haar measure normalization and Gaussian damping from $S_{\text{int}}$) enters only as $\ln(c_d K C_0^{1/6})$ in the convergence condition, which is at most logarithmic in $N$. With $m_1 a/6 \sim 5.8 \times 10^{14}$ at physical scales, the convergence domain is effectively unlimited in $N$ and $\beta$.

The KP criterion is applied correctly. The combinatorial bound on lattice animals is standard and correct for $d=4$. SOUND.

**(b) Physical regime coverage and the gap between regimes.** The preprint's three-regime analysis (Section 4.3) addresses whether the cluster expansion overlaps with the Balaban RG regime:

- **Regime A** (strong coupling, $\beta < \beta_c$): standard OS cluster expansion converges; KK enhancement unnecessary.
- **Regime B** (moderate coupling, $a \gg r_3$): KK bond suppression overwhelms plaquette growth; main new result.
- **Regime C** (ultra-fine lattice, $a \lesssim r_3$): KK expansion fails; requires Balaban's RG.

The crossover between Regimes B and C occurs at $a_{\text{cross}} \approx 2\sqrt{3} r_3 \beta(a_{\text{cross}})$. At physical $r_3 \sim 10^{-31}$ m and $\beta \sim 100$, $a_{\text{cross}} \sim 3.5 \times 10^{-29}$ m. At $a = a_{\text{cross}}$, $\beta_{\text{Balaban}}$ requires $g_0$ small, which is satisfied. So the regimes overlap.

More precisely: at $a \sim 10^{-20}$ m (10 orders of magnitude above $r_3$), the KK cluster expansion gives $\beta_{\max} \sim m_1 a/6 \sim 10^{11}$. Along the asymptotic freedom trajectory, $\beta(a) \sim (11N/24\pi^2) \ln(1/a\Lambda) \sim O(10)$ at $a\Lambda \sim 0.1$. The cluster expansion domain ($\beta < 10^{11}$) contains the entire Balaban starting point ($\beta \sim O(10)$). The transition from cluster expansion to Balaban RG is handled in Section 5.7, Remark 1: the finitely many initial RG steps $k < k_0$ (where $g_k^4 = O(1)$) are handled non-perturbatively via the cluster expansion, and the Balaban machinery takes over for $k \geq k_0$ where $g_k$ is small. This is a standard strategy (Seiler 1982; Glimm–Jaffe 1987, Ch. 17). SOUND.

**(c) Connected function bounds and the starting condition $C_0$.** Theorem 4 item (c) establishes exponential decay of connected correlators with rate $m \geq \alpha/a > 0$, uniform in the spatial volume $L$. The decay rate enters the OS1 temperedness bound as the mass gap $\Delta_0 > 0$. The cluster expansion constants ($c_d$, $K$, $C_0$) are all $a$-independent because they come from the KK spectrum (a property of $\mathbb{CP}^{N-1}$, not of the 4D lattice spacing). The starting condition $C_0$ for the RG recursion (Section 5.4) is the connected matrix element of $E_0$ in the one-particle state, which is $O(\Delta_0) = O(1)$ by the cluster expansion. The bound $C_0 < \infty$ follows from $\Delta_0 > 0$ and the operator norm bound $\|E_0\| \leq C g_0^4$. SOUND.

**Impact on the claimed result:** No gap. The cluster expansion convergence is rigorously established via the Kotecký-Preiss criterion, with all constants explicitly bounded. The mass gap $\Delta_0 > 0$ at the starting lattice spacing is the core result of Part B, and Theorem 3 provides the convergence proof.
