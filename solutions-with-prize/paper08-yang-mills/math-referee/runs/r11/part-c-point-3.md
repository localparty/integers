## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The overlap region.**

The cluster expansion (Theorem 4) applies for $\beta < \beta_{\max}(a) \approx 5.8 \times 10^{14}$ (for $N = 3$). Balaban's weak-coupling RG applies for $g_0$ sufficiently small, which corresponds to $\beta = 2N/g_0^2$ sufficiently large. The precise threshold $\beta_{\min}^{\mathrm{Balaban}}$ is not stated explicitly in Balaban's papers as a numerical value, but the construction requires $g_0^2 \leq c$ for some universal constant $c > 0$ (typically $c \sim O(1)$). This gives $\beta_{\min}^{\mathrm{Balaban}} \sim 2N/c \sim O(N)$.

The overlap region is $\beta \in [\beta_{\min}^{\mathrm{Balaban}}, \beta_{\max}(a)]$, which for $N = 3$ is approximately $\beta \in [O(10), 5.8 \times 10^{14}]$. This is an enormous overlap — the two regimes cover the same range of couplings with a margin of $\sim 14$ orders of magnitude.

**(b) The transition.**

At $k = 0$, the coupling may be $g_0 = O(1)$ (not necessarily small). The first few RG steps coarsen the lattice, and the coupling decreases: $g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$. After $k_0 \sim 1/(b_0 g_0^2 \ln 2)$ steps, $g_k$ becomes small enough for the perturbative $\beta$-function to control the flow.

The preprint handles the initial non-perturbative steps as follows: for $k < k_0$, the cluster expansion provides the mass gap and correlation bounds non-perturbatively (Theorem 4 applies at each $a_k$ since $\beta < \beta_{\max}(a_k)$ and $\beta_{\max}$ grows with $a_k$). The form factor bound at these steps uses the full cluster expansion, not perturbative estimates. The starting constant $C_0$ absorbs all contributions from $k < k_0$.

For $k \geq k_0$, Balaban's perturbative RG takes over, and the recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)$ applies with the perturbative estimates for $C_{\mathrm{new}}$ and the correction term.

The transition is justified because: (i) the cluster expansion and Balaban's RG give compatible bounds in the overlap region; (ii) the RG recursion is formulated in terms of $C_k$ (a ratio), which is bounded at $k_0$ by the cluster expansion; (iii) the recursion for $k \geq k_0$ is a contraction with the $1/4$ factor, so any initial condition converges to $C_* = 4C_{\mathrm{new}}/3$.

**Impact on the claimed result:** None. The coupling regime overlap is vast, and the transition from non-perturbative to perturbative regime is handled correctly.
