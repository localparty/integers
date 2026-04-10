## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

(a) The $g_k^4$ factor comes from Balaban's operator norm bound $\|\delta E_k^{d=6}\| \leq C g_k^4$ per site. The spectral lemma with $M = C g_k^4$ and dev >= 2 gives $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 = C_{new} g_k^4 \hat{\Delta}^2$. The r06 referee confirmed this derivation. Note that $g_k^4$ is the FULL operator norm bound, not a product of a one-loop coefficient and a matrix element -- the spectral lemma bypasses the need to compute individual matrix elements. The bound is: operator norm x spectral suppression from deviation order.

(b) Non-perturbative corrections: large-field contributions are $O(e^{-c/g_k^{2\epsilon}})$ and instanton contributions are $O(e^{-8\pi^2/g_k^2})$. Both are negligible compared to $g_k^4 \hat{\Delta}^2$ on the asymptotically free trajectory. Explicitly: $g_k^4 \hat{\Delta}_k^2 \sim 4^{-k}/k^2$ (geometric times polynomial decay), while $e^{-c/g_k^{2\epsilon}} \sim e^{-c k^\epsilon}$ (stretched exponential) and $e^{-8\pi^2/g_k^2} \sim e^{-c' k}$ (exponential). Both non-perturbative corrections decrease faster than $g_k^4 \hat{\Delta}^2$ for all $k$ sufficiently large, with the finitely many initial terms contributing a bounded constant.

**Impact on the claimed result:** None. The single-step bound follows directly from the spectral lemma and Balaban's norm bound.
