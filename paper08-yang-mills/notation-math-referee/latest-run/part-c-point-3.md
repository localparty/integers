## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim is that the cluster expansion domain and Balaban's RG domain overlap.

**(a) The overlap region.** The cluster expansion applies for $\beta < m_1 a/6 - \mathrm{const}$, i.e., for all $\beta$ up to $\sim 10^{14}$ in the physical regime. Balaban's RG applies for $g_0$ sufficiently small (large $\beta$). The overlap region is $\beta_{\min}^{\mathrm{Balaban}} < \beta < \beta_{\max}^{\mathrm{cluster}}$. Both $\beta_{\min}^{\mathrm{Balaban}}$ and $\beta_{\max}^{\mathrm{cluster}}$ are finite constants, and the cluster expansion margin ($\sim 10^{14}$) vastly exceeds any conceivable $\beta_{\min}^{\mathrm{Balaban}}$. The overlap is enormous.

**(b) The transition.** At $k = 0$, the coupling $g_0$ may not be small. The Cluster–Balaban Handoff Lemma (Section 5.4.5) handles this rigorously: the cluster expansion at the bare scale provides polymer activities satisfying the Kotecký–Preiss criterion, which serve as valid initial conditions for Balaban's inductive construction. The rate compatibility condition (H3) — that the cluster expansion decay rate exceeds Balaban's required rate — is automatic in the physical regime ($\sim 10^{13}$ margin for $N = 3$).

The first few RG steps ($k < k_0$) where $g_k^4 = O(1)$ are handled non-perturbatively via the cluster expansion (Section 5.4.6), with their total contribution bounded by a $K$-independent constant absorbed into $C_0^{\mathrm{cl}}$. The crossover step $k_0(K)$ is non-increasing in $K$ (since $g_K$ decreases on the AF trajectory), so for large $K$, $k_0 = 0$ and the strong-coupling block is empty.

**Impact on the claimed result:**
No impact. The coupling regimes overlap with vast margin, and the transition is handled by the Cluster–Balaban Handoff Lemma.
