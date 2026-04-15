## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The $g_k^4$ factor.** The bound $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$ follows from the spectral lemma (Section 5.5.3) applied with:

- $p = 2$ (Boltzmann deviation order dev $\geq 2$, from Part III of Section 5.6).
- $M = \|\delta E_k^{d=6}\| \leq Cg_k^4$ (Balaban's operator norm bound on the remainder per site).

The spectral lemma gives $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_2 M \hat{\Delta}^2 = C_2 \cdot Cg_k^4 \cdot \hat{\Delta}_{k+1}^2 = C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$.

The $g_k^4$ comes entirely from the operator norm bound, NOT from a product of one-loop coefficient and matrix element. The r06 referee confirmed this: "The $g_k^4$ factor comes from Balaban's operator norm bound on the total remainder." The spectral lemma provides the $\hat{\Delta}^2$ suppression independently of the coupling.

**(b) Non-perturbative corrections.** Two classes of corrections:

1. **Large-field contributions:** $O(e^{-c/g_k^{2\epsilon}})$ from the large-field region $\Omega_l$. On the AF trajectory with $g_k^2 \sim 1/(b_0 k \ln 2)$: $e^{-c/g_k^{2\epsilon}} = e^{-c(b_0 k \ln 2)^\epsilon}$. Compare with $g_k^4 \hat{\Delta}_{k+1}^2 \sim k^{-2} \cdot 4^{-k}$. For any $\epsilon > 0$, $e^{-ck^\epsilon}$ decays faster than $k^{-2}$ but slower than $4^{-k}$. However, the SUM $\sum_k e^{-ck^\epsilon}$ converges (comparison with $\int e^{-cx^\epsilon} dx < \infty$ for $\epsilon > 0$), so the large-field corrections make a finite total contribution to the mass gap shift. This contribution is negligible compared to the small-field sum.

2. **Instanton contributions:** $O(e^{-8\pi^2/g_k^2}) = O(e^{-8\pi^2 b_0 k \ln 2})$. This is doubly exponential in $k$ (faster than $4^{-k}$ for large enough $k$ since $8\pi^2 b_0 \ln 2 > \ln 4$ for $N \geq 2$). Negligible.

Both corrections are negligible compared to $g_k^4 \hat{\Delta}_{k+1}^2$ for large $k$. For small $k$, they are $O(1)$ and absorbed into $C_0$.

**Impact on the claimed result:** None. The single-step bound is correctly established.
