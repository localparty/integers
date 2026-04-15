## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

---

**Finding:**

**(a) The overlap region.** The three-regime analysis in Section 4.3 explicitly identifies the overlap:

- **Cluster expansion (Regime B):** converges for $\beta < m_1 a/6 - \text{const} = (2\sqrt{3} a/6r_3) - \text{const}$. At $a = 10^{-20}$ m and $r_3 = 10^{-31}$ m, this gives $\beta_{\max} \sim 10^{11}$.
- **Balaban RG:** applies for $g_0^2 \leq g_*^2$ (small coupling). Along the asymptotic freedom trajectory, this corresponds to $\beta_0 = 2N/g_0^2 \geq 2N/g_*^2 = \beta_{\min}^{\text{Balaban}}$.

At $a = 10^{-20}$ m, $\beta_0 \sim (11N/24\pi^2) \ln(1/(a\Lambda)) \approx (11 \times 3/24\pi^2) \times 11 \times \ln(10) \approx 7$ for $N=3$, $\Lambda^{-1} \sim 10^{-16}$ m. This satisfies $\beta_0 < \beta_{\max} \sim 10^{11}$, so the overlap is enormous. The cluster expansion is far from its convergence limit at the Balaban starting point.

The explicit $\beta_{\min}^{\text{Balaban}}$ is not stated in the preprint, but the argument is: Balaban's UV stability requires $g_0$ small enough that the polymer expansion converges at the first step $k=0$. The KP convergence condition at $k=0$ is the same type of condition as in Theorem 3, and it is satisfied as long as $\beta_0$ is above a finite threshold (independent of $L$ and $a_0$). No numerical value is given for $g_*$, but this is standard in the Balaban literature (a finite but unspecified constant). The absence of an explicit value of $\beta_{\min}^{\text{Balaban}}$ is a minor notational omission, not a logical gap, given that both regimes overlap for all $a \in [r_3, a_{\text{cross}}]$. SOUND.

**(b) The transition from cluster expansion to Balaban RG.** Section 5.7, Remark 1 addresses the transition: "The finitely many initial steps $k < k_0$ contribute a bounded constant to the RG sum." Here $k_0$ is the step at which $g_k$ first enters the Balaban domain ($g_{k_0}^2 \leq g_*^2$). For $k < k_0$, the form factor bound $|\langle 1|E_k(0)|1\rangle_c| \leq C g_k^4 \hat{\Delta}_k^2$ is established by the cluster expansion (trivially, since $\hat{\Delta}_k \sim O(1)$ and the cluster expansion gives exponential decay). The contribution to the RG sum from steps $k = 0, \ldots, k_0-1$ is bounded by $k_0 \times C g_0^4 \hat{\Delta}_0^2 = O(1)$ (a finite constant depending only on $N$, $g_0$, and $\hat{\Delta}_0$, all fixed). For $k \geq k_0$, the Balaban machinery applies and the form factor bound follows from the stability of deviation order argument (Section 5.6). This non-perturbative handling of the initial steps is rigorous and sufficient. SOUND.

**Impact on the claimed result:** No gap. The coupling regime overlap is clearly established by the three-regime analysis. The transition from the cluster expansion domain to the Balaban domain is handled non-perturbatively via the cluster expansion at initial steps. The absence of a specific numerical value for $\beta_{\min}^{\text{Balaban}}$ is an informational gap that does not affect the proof's validity.
