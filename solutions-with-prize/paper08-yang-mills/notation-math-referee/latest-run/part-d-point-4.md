## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim is $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$.

**(a) The $g_k^4$ factor.** The factor $g_k^4$ comes from Balaban's total remainder bound $\|\delta E_k^{d=6}\| \leq \|E_k\| \leq C g_k^4$ per unit volume (Section 5.1.3). The spectral lemma with $M = C g_k^4$ and $\mathrm{dev} \geq 2$ gives $C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 = C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$, where $C_{\mathrm{new}} = C_2 \cdot C$ is a product of the spectral lemma constant $C_2$ (independent of $k$, $g_k$, volume) and the Balaban remainder constant $C$ (independent of $k$). This is correct.

**(b) Non-perturbative corrections.** Large-field contributions are $O(e^{-c/g_k^{2\epsilon}})$ with $\epsilon = 0.49$. Instanton contributions are $O(e^{-8\pi^2/g_k^2})$.

Verified computationally on the AF trajectory: for $k \geq 1$, both $e^{-c/g_k^{2\epsilon}}$ and $e^{-8\pi^2/g_k^2}$ are negligible compared to $g_k^4 \hat{\Delta}^2 \sim 4^{-k}/k^2$. At $k = 1$ (strong coupling), $e^{-8\pi^2/g_k^2} \approx 0.02$ while $g_k^4 \hat{\Delta}^2 \approx 107$, so the instanton contribution is negligible. For $k \geq 5$, both non-perturbative corrections are astronomically small ($< 10^{-9}$). The first few strong-coupling steps are handled non-perturbatively via the cluster expansion (Section 5.4.6), so the comparison is only needed for $k \geq k_0$ where $g_k$ is small.

**Impact on the claimed result:**
No impact. The single-step bound follows directly from the spectral lemma (D3) and the deviation order (D2), with non-perturbative corrections verified to be negligible.
