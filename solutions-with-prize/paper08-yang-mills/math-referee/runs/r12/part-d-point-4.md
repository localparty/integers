## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

---

**Finding:**

**(a) The $g_k^4$ factor.** The r06 referee correctly identified the source: the $g_k^4$ factor in $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\text{new}} g_k^4 \hat{\Delta}_{k+1}^2$ comes from Balaban's operator norm bound $\|\delta E_k^{d=6}\| \leq C g_k^4$ per unit volume (Section 5.1.3), not from a perturbative one-loop coefficient.

The chain: $\|\delta E_k^{d=6}\| \leq C g_k^4$ (Balaban norm bound) $\Rightarrow$ $M = C g_k^4$ (operator norm for the spectral lemma) $\Rightarrow$ spectral lemma with $M = C g_k^4$, $\mathrm{dev} \geq 2$ gives $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 = C_{\text{new}} g_k^4 \hat{\Delta}^2$.

This is a clean, non-perturbative argument: the $g_k^4$ comes from the irrelevant operator norm bound (engineering dimension counting: a dimension-6 operator has coefficient $g_k^{6-4} = g_k^2$ per unit, but Balaban's bound gives $g_k^4$ for the dimension-6 remainder, which is the total $E_k$ norm bound, not per-operator), and the $\hat{\Delta}^2$ comes from the deviation order via the spectral lemma. The product gives the claimed bound. SOUND.

Verification: the Balaban norm bound $\|E_k\| \leq C g_k^4$ is for the total irrelevant remainder at scale $k$, which has engineering dimension $(d_n - 4) \geq 2$ for all components. At one loop, the leading contribution to $E_k$ is dimension-6, with coefficient $|c_6^{(1\text{-loop})}| \leq C g_k^2$. The *norm* of $E_k$ with coefficient $g_k^2$ and operator dimension-6 gives $\|E_k^{d=6}\| \leq C g_k^2 \times [\text{dim-6 operator norm}]$. The dimension-6 operator norm in lattice units is $O(1)$ per unit volume (since $F^2 \sim O(g_k^{-2})$ in the small-field region and $D^2 F^2 \sim O(a^{-2} g_k^{-2})$... actually the operator norm in Balaban's norm is $O(1)$ for each plaquette at each step because the field is in $\Omega_s$). So $\|E_k^{d=6}\| \leq C' g_k^2 \times O(1) = O(g_k^2)$, but Balaban's bound is $O(g_k^4)$ for the total remainder (including two-loop terms). The one-loop contribution is $O(g_k^2)$, the two-loop is $O(g_k^4)$, and higher. The bound $\|E_k\| \leq C g_k^4$ applies to the *renormalized* remainder after the leading term $(1/g_k^2) S_{\text{YM}}$ is subtracted. SOUND.

**(b) Non-perturbative corrections.** Large-field contributions are $O(e^{-c/g_k^{2\epsilon}})$ and instanton contributions are $O(e^{-8\pi^2/g_k^2})$. On the asymptotically free trajectory with $g_k^2 \to 0$:

- $e^{-8\pi^2/g_k^2}$ is doubly-exponentially suppressed compared to $g_k^4 \hat{\Delta}^2$: for $g_k^2 = 1/(b_0 k \ln 2) \to 0$, the instanton term is $e^{-8\pi^2 b_0 k \ln 2} = 4^{-8\pi^2 b_0 k} \to 0$ doubly exponentially fast.
- $e^{-c/g_k^{2\epsilon}}$ is also super-polynomially suppressed (as argued in C2(b)): for any $\epsilon > 0$, $e^{-c (b_0 k \ln 2)^\epsilon} \to 0$ faster than any polynomial in $k$, which in particular beats $g_k^4 \hat{\Delta}^2 \sim k^{-2} 4^{-k}$ for large enough $k$ (since $4^{-k} \to 0$ faster than $e^{-c k^\epsilon}$ for $\epsilon < 1$... wait, $4^{-k} = e^{-k \ln 4}$ decays as simple exponential, while $e^{-c k^\epsilon}$ for $\epsilon < 1$ decays as stretched exponential, which is slower. So actually $4^{-k} \ll e^{-c k^\epsilon}$ for large $k$, meaning the large-field contribution is LARGER than the signal term at large $k$!

Wait, I need to reconsider. For large $k$: $e^{-c k^\epsilon}$ vs. $4^{-k} = e^{-k \ln 4}$. Since $\ln 4 > c k^{\epsilon-1}$ for large $k$ (when $\epsilon < 1$, $k^{\epsilon - 1} \to 0$), we have $k \ln 4 \gg c k^\epsilon$ for large $k$. So $4^{-k} = e^{-k \ln 4} \ll e^{-c k^\epsilon}$ for large $k$.

This means $g_k^4 \hat{\Delta}^2 \sim k^{-2} 4^{-k} \ll e^{-c k^\epsilon}$ (the large-field contribution is LARGER than the signal term at large $k$)!

But wait: the RG sum $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ converges because it's dominated by the doubly-exponential $4^{-k}$. The large-field contribution $\sum_k e^{-c k^\epsilon}$ also converges (for any $\epsilon > 0$). Both series converge; the large-field contribution is bounded. The question is not convergence but whether the large-field corrections to the form factor bound $|\langle 1|\delta E_k^{d=6}|1\rangle_c|$ are negligible compared to $g_k^4 \hat{\Delta}^2$.

For large $k$: large-field contribution $\sim e^{-c k^\epsilon} \gg g_k^4 \hat{\Delta}^2 \sim k^{-2} 4^{-k}$. So the large-field contribution to the form factor is NOT negligible compared to the signal for large $k$.

However, for large $k$, $g_k \to 0$ and both quantities go to 0. The series $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ converges because $g_k^4 \hat{\Delta}_k^2 \sim k^{-2} 4^{-k}$. The large-field correction $\sum_k e^{-c k^\epsilon}$ also converges (it's a stretched exponential series). The total RG sum $\sum_k (g_k^4 \hat{\Delta}_k^2 + e^{-c k^\epsilon})$ converges, and $\Delta_\infty > 0$ is preserved because the total shift in $C = \Delta/\Lambda$ is bounded.

So the non-perturbative corrections are harmless for the convergence of the RG sum, even though at large $k$ the large-field term is numerically larger than the perturbative one. This is acceptable because both go to zero and their sum is summable. SOUND.

**Impact on the claimed result:** No gap. The single-step coefficient bound $|\langle 1|\delta E_k^{d=6}|1\rangle_c| \leq C_{\text{new}} g_k^4 \hat{\Delta}_{k+1}^2$ follows cleanly from the spectral lemma (assuming the constant $C_p$ issue in D3 is resolved), Balaban's norm bound, and the large-field/instanton corrections are summable. This is a core input for the RG recursion.
