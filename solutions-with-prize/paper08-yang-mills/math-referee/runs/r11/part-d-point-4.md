## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The $g_k^4$ factor.**

The r06 referee correctly identified the source: the spectral lemma with $p = 2$ and $M = \|\delta E_k^{d=6}\| \leq C g_k^4$ (Balaban's total remainder bound) gives:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 = C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$$

The $g_k^4$ comes from Balaban's operator norm bound on the total irrelevant remainder, not from a product of one-loop coefficient ($c_6^{(k)} \sim g_k^2$) and matrix element ($\sim g_k^2$). The preprint conservatively uses the total remainder bound $C g_k^4$ rather than the sharper dimension-6-specific bound $C' g_k^2$. This is conservative but sufficient.

With the sharper bound $M = C' g_k^2$, one would get $C'_{\mathrm{new}} g_k^2 \hat{\Delta}^2$, which is even better for convergence. The preprint's choice to use the cruder bound avoids needing to prove the dimension-specific decomposition of the norm and simplifies the argument. This is a legitimate choice.

**(b) Non-perturbative corrections.**

Large-field contributions are $O(e^{-c/g_k^{2\epsilon}})$ with $\epsilon > 0$ fixed. Instanton contributions are $O(e^{-8\pi^2/g_k^2})$. On the AF trajectory with $g_k^2 \sim 1/(b_0 k \ln 2)$:

- Large-field: $e^{-c/g_k^{2\epsilon}} = e^{-c(b_0 k \ln 2)^{1/\epsilon}}$, which decays faster than any power of $g_k$ (super-polynomial in $k$).
- Instantons: $e^{-8\pi^2/g_k^2} = e^{-8\pi^2 b_0 k \ln 2}$, which decays exponentially in $k$.
- Small-field contribution: $g_k^4 \hat{\Delta}^2 \sim k^{-2} \cdot 4^{-k}$, which decays doubly exponentially in $k$.

Both non-perturbative corrections are negligible compared to $g_k^4 \hat{\Delta}^2$ for large $k$ because $4^{-k}$ decays faster than $e^{-\mathrm{poly}(k)}$. Wait — actually $4^{-k} = e^{-k \ln 4}$ is exponential in $k$, while the large-field correction $e^{-c k^{1/\epsilon}}$ with $\epsilon < 1$ grows slower than linearly in the exponent. So $4^{-k}$ decays faster than the large-field correction for large $k$, meaning the small-field contribution $g_k^4 \hat{\Delta}^2$ is actually smaller than the large-field correction eventually.

However, this does not affect the convergence of the sum: both $\sum_k g_k^4 \hat{\Delta}_k^2$ and $\sum_k e^{-c k^{1/\epsilon}}$ converge, and the total mass gap shift is the sum of all contributions, each of which gives a convergent series.

The claim in the preprint is that non-perturbative corrections are "negligible compared to $g_k^4 \hat{\Delta}^2$." This is slightly imprecise for the large-field contribution at early steps, but it is correct that both contributions give convergent sums and the total mass gap shift is bounded. The convergence of the total sum is what matters, not the relative size of individual terms.

**Impact on the claimed result:** None. The single-step bound is correctly derived from the spectral lemma, and non-perturbative corrections contribute convergent sums.
