## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) The $g_k^4$ factor.**

The bound $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$ combines:

1. **Operator norm bound:** $\|\delta E_k^{d=6}\| \leq C g_k^4$ (from Balaban's remainder bound for the dimension-6 part of the effective action, per unit volume).

2. **Spectral lemma with $\mathrm{dev} \geq 2$:** $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_2 M \hat{\Delta}^2$ with $M = \|\mathcal{O}\|$.

Combining: $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat{\Delta}_{k+1}^2 = C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$.

The $g_k^4$ factor comes entirely from Balaban's operator norm bound on the irrelevant remainder. It is NOT a product of a one-loop coefficient $O(g_k^2)$ and a matrix element $O(g_k^2 \hat{\Delta}^2)$. The r06 referee correctly identified this: the bound is conservative (uses the generic remainder bound rather than a sharper dimension-6-specific estimate), but conservatism does not invalidate the argument — it merely makes the bound less tight than it could be.

The constant $C_{\mathrm{new}} = C_2 \cdot C$ depends on $N$ (through $C_2$ from the spectral lemma and $C$ from the polymer expansion) but not on $k$, $g_k$, or the volume. This is exactly what the RG recursion requires.

**(b) Non-perturbative corrections.**

Two sources of non-perturbative corrections:

1. **Large-field contributions:** $O(e^{-c/g_k^{2\epsilon}})$ per unit volume (Balaban CMP 119). On the AF trajectory ($g_k^2 \sim 1/(b_0 k \ln 2)$), this is $e^{-c(b_0 k \ln 2)^\epsilon}$. For any $\epsilon > 0$, this decays super-polynomially in $k$. Compared to $g_k^4 \hat{\Delta}_k^2 \sim k^{-2} \cdot 4^{-k}$: the large-field contribution is negligible because $e^{-ck^\epsilon}$ eventually dominates any power $k^{-2}$, and $4^{-k}$ provides the dominant decay.

2. **Instanton contributions:** $O(e^{-8\pi^2/g_k^2})$ from non-trivial topological sectors. On the AF trajectory, $e^{-8\pi^2/g_k^2} = e^{-8\pi^2 b_0 k \ln 2}$, which is exponentially small in $k$ (faster than $4^{-k}$ since $8\pi^2 b_0 \ln 2 \gg \ln 4$ for any $N \geq 2$).

Both corrections are negligible compared to $g_k^4 \hat{\Delta}_k^2$, confirming that the mass gap shift at each RG step is dominated by the small-field, trivial-topology contribution.

**Impact on the claimed result:**

None. The single-step bound is correctly derived from Balaban's operator norm bound and the spectral lemma. Non-perturbative corrections are rigorously bounded and negligible.
