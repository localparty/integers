## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND (the bound follows from the spectral lemma + dev $\geq 2$ + Balaban operator norm)

**Finding:**

(a) **The $g_k^4$ factor.** The proof's logic is:
$$\|\delta E_k^{d=6}\| \leq C g_k^4 \quad \text{(Balaban operator norm)}$$
$$\mathrm{dev}(\delta E_k^{d=6}) \geq 2 \quad \text{(stability of dev order, Point D2)}$$
Spectral lemma with $M = C g_k^4$, $p = 2$ gives:
$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat\Delta_{k+1}^2 = C_{\mathrm{new}} g_k^4 \hat\Delta_{k+1}^2$$

This is correct as a *combination* of the previously-verified bounds. The $g_k^4$ comes from the operator-norm bound $\|\delta E_k\| \leq C g_k^4$, which is Balaban's standard estimate (extracted in Appendix H). The $\hat\Delta_{k+1}^2$ comes from the spectral lemma's $\hat\Delta^p$ with $p = 2$. The $C_{\mathrm{new}} = C_2 \cdot C$ is a $k$-independent constant (with N-dependent magnitude).

(b) **Non-perturbative corrections.** Large-field $O(e^{-c/g_k^{2\epsilon}})$ and instanton $O(e^{-8\pi^2/g_k^2})$ contributions are claimed negligible. As discussed in Point C2, the large-field bound is borderline at moderate $g_k$, but uniformly small at small $g_k$ on the AF trajectory. The instanton contribution is genuinely smaller than any power of $g_k$. Sound.

**Impact on the claimed result:** Sound. This is the assembly point of the dev $\geq 2$ classification (D2) and the spectral lemma (D3). The single-step bound is the input to the RG recursion (E1), which then needs the K-vs-k separation to converge.
