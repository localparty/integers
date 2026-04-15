## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The $g_k^4$ factor.** The bound $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2$ is obtained by applying the spectral lemma to the dim-6 remainder:

1. **Operator norm:** $\|\delta E_k^{d=6}\| \leq C\,g_k^4$ (from Balaban's generic bound on the dim-6 remainder; this is the most conservative choice, using the full remainder norm rather than the leading coefficient).
2. **Deviation order:** $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ (from the stability argument, Point D2).
3. **Spectral lemma:** With $M = C\,g_k^4$ and $p = 2$: $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C\,g_k^4 \cdot \hat{\Delta}^2 = C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}^2$.

The $g_k^4$ comes from the operator norm, not from a perturbative coefficient identification. This is the conservative approach noted by the r06 referee (Point 8): a sharper bound $g_k^2$ from the one-loop coefficient is available but unnecessary. The extra factor of $g_k^2$ provides additional margin.

The constant $C_{\mathrm{new}} = C_2(N) \cdot C(N)$ is $k$-independent. It depends on $N$ through both $C_2$ (spectral lemma constant) and $C$ (Balaban remainder bound).

**(b) Non-perturbative corrections.** Two sources of non-perturbative corrections:

1. **Large-field contributions:** $O(e^{-c/g_k^{2\epsilon}})$ where $\epsilon > 0$ is Balaban's small-field parameter.
2. **Instanton contributions:** $O(e^{-8\pi^2/g_k^2})$ from non-trivial topological sectors.

Both must be negligible compared to $g_k^4\,\hat{\Delta}^2$. On the AF trajectory:

- $g_k^4\,\hat{\Delta}^2$: the $g_k^4$ factor is $\sim 1/(b_0 k)^2$ and $\hat{\Delta}^2$ involves the contraction factor from the recursion. The product $g_k^4\,\hat{\Delta}^2$ scales as $1/k^2$ times the recursion contraction.
- $e^{-c/g_k^{2\epsilon}} = e^{-c(b_0 k \ln 2)^{\epsilon}}$: decays faster than any power of $k$.
- $e^{-8\pi^2/g_k^2} = e^{-8\pi^2 b_0 k \ln 2}$: decays exponentially in $k$.

Both non-perturbative corrections are negligible:

$$\frac{e^{-c(b_0 k)^{\epsilon}}}{g_k^4\,\hat{\Delta}^2} \to 0 \quad\text{and}\quad \frac{e^{-8\pi^2 b_0 k \ln 2}}{g_k^4\,\hat{\Delta}^2} \to 0$$

as $k \to \infty$.

**Impact on the claimed result:** None. The single-step bound $C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}^2$ is correctly derived from the spectral lemma with conservative inputs. Non-perturbative corrections are negligible on the asymptotically free trajectory.
