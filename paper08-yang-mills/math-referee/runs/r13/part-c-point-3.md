## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim: the cluster expansion applies for all beta < 10^{14}. Balaban's RG applies for g_0 small. These overlap.

**(a) The overlap region.** The cluster expansion converges for beta < beta_max(a) = m_1 a/6 - ln(c_d K C_0^{1/6}). In the physical regime a/r_3 ~ 10^{15}, this gives beta_max ~ 10^{14} (a very large number).

Balaban's RG applies for g_0 "sufficiently small," i.e., beta_0 = 2N/g_0^2 > beta_min^{Balaban}. Balaban does not state an explicit beta_min — the condition is qualitative ("g_0 small enough that the polymer expansion converges at step k = 0"). In practice, beta_min is of order 1-100 (the weak-coupling regime begins well before beta ~ 10^{14}).

The overlap region is [beta_min, beta_max] with beta_min ~ O(1-100) and beta_max ~ 10^{14}. This is a vast overlap. There is no gap between the two regimes.

**(b) The transition.** At k = 0, the coupling is g_0 = sqrt(2N/beta_0). For beta_0 in the overlap region, g_0 is already small (g_0 << 1). The first few RG steps maintain g_k small (since g_{k+1}^2 = g_k^2 - b_0 g_k^4 ln 2 < g_k^2, the coupling decreases monotonically).

The paper's Section 5.7, Remark 1 addresses the transition: for the starting lattice spacing a_0 with beta_0 in the convergence domain of both the cluster expansion AND Balaban's RG, the mass gap Delta_0 > 0 is established by the cluster expansion (Section 4), and the RG preservation (Section 5) takes over immediately. No intermediate regime is uncovered.

For very strong coupling (beta_0 close to 0), only the cluster expansion applies. But the paper does not need to prove the mass gap for all beta — it needs Delta_0(a_0) > 0 at one starting point (a_0, beta_0) on the AF trajectory, and then the RG preserves it as a -> 0. The choice beta_0 in the overlap region provides this.

No error found. The overlap is comfortable and the transition is seamless.

**Impact on the claimed result:** None. The regime overlap is established with enormous margin.
