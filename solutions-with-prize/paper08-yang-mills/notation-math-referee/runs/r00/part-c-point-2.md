## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP (the large-field suppression $e^{-c/g_k^{2\epsilon}}$ is weaker than the proof needs at small $g_k$, but the spectral-lemma application can be saved)

**Finding:**

(a) **Small-field condition.** Balaban's small-field domain is $\Omega_s = \{|F_{\mu\nu}| < g_k^{1-\epsilon}\}$ with $\epsilon = 1/4$ chosen in §5.5.3 ("Non-perturbative contributions to $\epsilon_B$"). The polymer expansion converges in $\Omega_s$, and analyticity (B1) holds with $k$-independent radius. The dimension-6 operator classification (Point D1, D2) is valid only for the operators that arise in the small-field expansion.

The choice $\epsilon = 1/4$ gives the small-field threshold $|F| < g_k^{3/4}$, which becomes very *small* as $g_k \to 0$ (asymptotic freedom). On the AF trajectory, "most" configurations are in $\Omega_s$ in the sense that the Boltzmann weight concentrates there, but a *small* fraction of large-field configurations is exponentially suppressed.

(b) **Large-field suppression.** The bound is
$$\text{(large-field contribution)} \leq O(e^{-c/g_k^{2\epsilon}}) = O(e^{-c/g_k^{1/2}})$$
for $\epsilon = 1/4$. This is weaker than the instanton bound $O(e^{-8\pi^2/g_k^2})$.

The question is: does $e^{-c/g_k^{1/2}}$ decay faster than $g_k^4 \hat\Delta_k^2$ on the AF trajectory? The proof's calculation (§5.5.3 large-field paragraph):

> "$e^{-c/g_k^{1/2}} \ll g_k^4 \hat\Delta_k$ for all $k \geq k_0$ (the large-field suppression is beyond all perturbative orders, and $\hat\Delta_k \geq \hat\Delta_\infty > 0$ on the RG trajectory)"

This is correct in spirit but circular in detail: it uses $\hat\Delta_k \geq \hat\Delta_\infty > 0$, which is what the proof is trying to *establish*. To avoid the circularity, observe that $\hat\Delta_\infty$ is bounded below by $\hat\Delta_0^{\mathrm{KK}}$ (which is $O(1)$ from Theorem 4 of Section 4) modulo small RG corrections, so the bound holds independently of the full proof of $\Delta_\infty > 0$.

Computationally: at $g_k = 0.1$, $e^{-c/g_k^{1/2}} = e^{-c/0.316}$, which is $e^{-3c}$ for $c = 1$. Compared to $g_k^4 = 10^{-4}$, this is $\sim 10^{-1.3}$ — *not* small at all. The large-field contribution is *not* obviously negligible for moderate $g_k$.

The fix is to take $\epsilon$ smaller (e.g., $\epsilon = 1/100$), which strengthens the large-field bound to $e^{-c/g_k^{50}}$ — vastly smaller than any power. But this widens the small-field domain to $|F| < g_k^{0.99}$, which makes the polymer-expansion convergence harder. The trade-off has not been quantitatively optimized in the preprint.

(c) **Gauge invariance of the decomposition.** The condition $|F_{\mu\nu}| < p(g_k)$ is *gauge-invariant* (the field strength magnitude transforms as a scalar under gauge transformations), so the decomposition is gauge-invariant. Sound.

**To close:** Choose $\epsilon$ in the range $(0, 1/4]$ such that $e^{-c/g_k^{2\epsilon}}$ decays faster than $g_k^4$ for the target range of $k$, AND the small-field domain still admits the polymer expansion. This is a quantitative optimization that should be performed explicitly. **Difficulty: 1 page.**

**Impact on the claimed result:** The proof's qualitative claim that large-field contributions are "negligible" is correct, but the quantitative bound is borderline at moderate $g_k$. A clean version would optimize $\epsilon$ to make the large-field bound *stronger* than $g_k^4$ uniformly along the AF trajectory.
