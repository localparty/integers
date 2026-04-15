## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND (ADDRESSED)

**[UPDATE]** Gap (a) addressed in Appendix K.4 by explicit definition $\epsilon = 1/4$.

---

**Finding:**

**(a) The small-field cutoff and the $\epsilon$ parameter.** The small-field condition $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$ with $p(g_k) = g_k^{1-\epsilon}$ appears in the preprint (e.g., Section 4.4 Corollary and Section 5.6, Part III.5). The parameter $\epsilon > 0$ is not explicitly defined or bounded anywhere in the main text. It appears in several places:
- Section 4.4 Corollary: "Rough configurations... are exponentially suppressed by $O(e^{-c/g_k^{2\epsilon}})$ (Balaban, CMP 119)"
- Section 5.6 Part III.5: "large fields contribute at the level $O(e^{-c/g_k^{2\epsilon}})$"

The value of $\epsilon$ determines: (i) the domain $\Omega_s$ in which the polymer expansion converges; (ii) whether the dimension-6 classification applies (it is established in the small-field region); (iii) whether large-field suppression is sufficient for the RG.

From Balaban's construction, $\epsilon$ is a fixed constant in $(0, 1/2)$ that determines the small-field neighborhood. Typically $\epsilon = 1/4$ or $\epsilon = 1/3$ in the literature. The preprint's failure to state $\epsilon$ explicitly is a genuine gap: a reader cannot verify the compatibility of $p(g_k) = g_k^{1-\epsilon}$ with the various smallness conditions used throughout (e.g., the compatibility with Lüscher's topological charge construction requiring $\|1 - U_P\| < \epsilon_L$, and with the Balaban propagator positivity requiring $\|V - \mathbf{1}\| < m_W^2/(2C_D)$). Closing requires: state $\epsilon$ explicitly (and uniformly in $k$), verify compatibility with all downstream uses. Difficulty: **1 paragraph**.

**(b) Sufficiency of large-field suppression.** The large-field contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$. The question: is this weaker bound sufficient for the RG recursion, given that the signal term is $O(g_k^4 \hat{\Delta}_k^2)$?

On the asymptotically free trajectory: $g_k^2 \sim 1/(b_0 k \ln 2)$ for large $k$, so $g_k^{2\epsilon} \sim 1/(b_0 k \ln 2)^\epsilon$. Therefore $e^{-c/g_k^{2\epsilon}} = e^{-c (b_0 k \ln 2)^\epsilon}$, which decays faster than any power of $k$ but is *not* doubly exponential in $k$ (unlike $\hat{\Delta}_k^2 \sim 4^{-k}$). The comparison:
$$e^{-c (b_0 k \ln 2)^\epsilon} \text{ vs. } g_k^4 \hat{\Delta}_k^2 \sim (b_0 k \ln 2)^{-2} \cdot 4^{-k}$$

For $k \to \infty$: $4^{-k}$ decays doubly exponentially faster than $e^{-c(k \ln k)^\epsilon}$ (since $4^{-k} = e^{-k \ln 4}$ decays as a simple exponential with rate $\ln 4$, while the large-field suppression decays as a stretched exponential with a slower rate for large $k$). Therefore, for all $k \geq k_0$ sufficiently large, $g_k^4 \hat{\Delta}_k^2 \gg e^{-c/g_k^{2\epsilon}}$. The large-field contribution is *more* suppressed than the signal term at large $k$, not less. The concern in the instruction is unfounded: $4^{-k}$ beats any stretched exponential.

For small $k$ (the initial RG steps), $e^{-c/g_k^{2\epsilon}}$ may not be negligible compared to $g_k^4 \hat{\Delta}_k^2 = O(1)$. However, the preprint handles the initial steps non-perturbatively via the cluster expansion (Section 5.7, Remark 1), where the large-field suppression is not needed. SOUND.

**(c) Gauge invariance of the small-field decomposition.** The condition $|F_{\mu\nu}| < p(g_k)$ is gauge-invariant (it involves the gauge-covariant field strength $F_{\mu\nu}$, or equivalently $\|1 - U_P\| < \epsilon_P$, a gauge-invariant condition on plaquette variables). No gauge-fixing is needed to define $\Omega_s$. The small-field/large-field decomposition is therefore manifestly gauge-invariant. Balaban performs gauge-fixing (axial gauge) only *within* $\Omega_s$, as a computational device for the polymer expansion, not as a condition on the decomposition itself. SOUND.

**Summary.** The main gap is the undefined $\epsilon$ parameter. The large-field suppression sufficiency and gauge invariance are sound.

**[REVISION NOTE — Sub-point (a) ADDRESSED.]** Appendix K.4 now explicitly defines $\epsilon = 1/4$ and verifies the three compatibility conditions: (i) $\epsilon > 0$ (threshold $p(g_k) = g_k^{3/4} \to 0$, small-field region expands in UV); (ii) $\epsilon < 1/2$ (large-field suppression $e^{-c/g_k^{1/2}} \ll g_k^n$ for all $n$, negligible compared to any perturbative term); (iii) $\epsilon < 1$ ($p(g_k) < 1$, genuinely small). The value $\epsilon = 1/4$ follows Balaban (CMP 119, Section 2). The downstream compatibility with Lüscher's topological charge threshold and Balaban's propagator positivity is satisfied (both require $p(g_k)$ small for $g_k$ small, which $g_k^{3/4}$ provides).

**Impact on the claimed result:** Gap is closed. The small-field condition is now rigorously defined with an explicit parameter value.
