# Point 8: The Dimension-6 Coefficient -- Which Bound Is Used?

**Location:** Section 5.3.2, 5.6 Part III.5

**Verdict:** SOUND

**Finding:**

The paper claims the single-step bound $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_\mathrm{new} g_k^4 \hat{\Delta}_{k+1}^2$. The $g_k^4$ factor and its accounting are examined in detail.

---

## (a) The $O(g_k^2)$ matrix element

**Claim under attack:** The matrix element $|\langle 1|s_P(0)|1\rangle_c| = O(g_k^2)$ is a perturbative estimate; non-perturbatively it could be $O(1)$.

**Finding: SOUND -- the distinction does not affect the final bound.**

The paper's final bound (Section 5.6, Part III.5) uses the spectral lemma, which does NOT require an estimate on the matrix element of $s_P$. The bound is:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot M \cdot \hat{\Delta}_{k+1}^2$$

where $M = \|\delta E_k^{d=6}\|$ is the operator norm and $C_2$ is the spectral lemma constant. The spectral lemma provides the $\hat{\Delta}^2$ suppression from the deviation order; the operator norm provides the prefactor.

The value of $M$ is:

$$M = \|\delta E_k^{d=6}\| \leq C g_k^4 \quad \text{(from Balaban)}$$

This gives $C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 = C_\mathrm{new} g_k^4 \hat{\Delta}^2$.

The matrix element $|\langle 1|s_P(0)|1\rangle_c|$ does not appear anywhere in the final bound. Whether it is $O(g_k^2)$ (perturbative) or $O(1)$ (non-perturbative) is irrelevant. The bound is obtained entirely from:

1. $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ (from the operator classification)
2. $\|\delta E_k^{d=6}\| \leq C g_k^4$ (from Balaban's remainder estimate)
3. The spectral lemma: $C_p M \hat{\Delta}^p$

As the question itself observes, even if the matrix element were $O(1)$ and the bound became $C g_k^2 \hat{\Delta}^2$ (one less power of $g_k$), the convergence sum $\sum g_k^2 \hat{\Delta}_k^2 \sim \sum (1/k) \cdot 4^{-k}$ still converges. The $g_k^4$ vs. $g_k^2$ distinction is numerically inconsequential.

---

## (b) The coefficient bound

**Claim under attack:** The $g_k^4$ in the final bound: does it come from the one-loop-coefficient-times-matrix-element product, or from Balaban's generic bound alone?

**Finding: SOUND.** The $g_k^4$ comes from Balaban's **operator norm bound on the total remainder**, not from a product of coefficient and matrix element.

The accounting is as follows:

1. **Balaban's generic coefficient bound** (Section 5.1.3): For an irrelevant operator of engineering dimension $d_O$, the coefficient satisfies $|c_{d_O}^{(k)}| \leq C g_k^{d_O - 4}$. For $d_O = 6$: $|c_6| \leq C g_k^2$.

2. **Operator norm in the small-field region.** The lattice operator $\mathcal{O}_6$ (e.g., $\mathrm{Tr}(DF)^2$) has a norm per site that depends on the field strength within the small-field region $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$ where $p(g_k) = g_k^{1-\epsilon}$. The norm per site is:

$$\|\mathcal{O}_6\|_\mathrm{per\,site} = O(p(g_k)^{2+\delta}) = O(g_k^{2(1-\epsilon)+\delta})$$

since $\mathrm{Tr}(DF)^2$ involves four powers of $F$ (two from $F$ and two from the derivatives acting on $F$).

3. **Total norm per site:** $\|\delta E_k^{d=6}\|_\mathrm{per\,site} = |c_6| \cdot \|\mathcal{O}_6\|_\mathrm{per\,site} = O(g_k^2) \cdot O(g_k^{2(1-\epsilon)}) = O(g_k^{4-2\epsilon})$.

For $\epsilon \to 0$, this is $O(g_k^4)$, consistent with Balaban's total remainder bound $\|E_k\| \leq C g_k^4$ per site.

4. **The spectral lemma input.** The spectral lemma takes $M = \|\delta E_k^{d=6}\| \leq C g_k^4$ (the operator norm per site, which includes both the coefficient and the operator's field-strength content within the small-field region). The bound:

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 = C_\mathrm{new} g_k^4 \hat{\Delta}^2$$

**To summarize the accounting precisely:**

| Factor | Source | Value |
|:-------|:-------|:------|
| $c_6$ (one-loop coefficient) | Heat kernel / Seeley--DeWitt | $O(g_k^2)$ |
| $\|\mathcal{O}_6\|$ in $\Omega_s$ | Small-field condition $|F| < g_k^{1-\epsilon}$ | $O(g_k^{2-2\epsilon})$ |
| $M = c_6 \cdot \|\mathcal{O}_6\|$ | Product | $O(g_k^{4-2\epsilon}) \leq C g_k^4$ |
| $\hat{\Delta}^2$ | Spectral lemma (dev $\geq 2$) | $\hat{\Delta}_{k+1}^2$ |
| Final bound | $C_2 M \hat{\Delta}^2$ | $C_\mathrm{new} g_k^4 \hat{\Delta}^2$ |

The $g_k^4$ comes from the product of the one-loop coefficient ($g_k^2$) and the field-strength normalization within the small-field domain ($g_k^{2-2\epsilon}$). Balaban's generic bound absorbs the $\epsilon$ into the constant $C$. The theorem statement accurately reflects the bound used.

---

**Impact on the claimed result:** None. The $g_k^4$ accounting is consistent, and the final bound $C_\mathrm{new} g_k^4 \hat{\Delta}^2$ is correctly derived. The convergence of the RG sum is robust to any weakening of the $g_k$ exponent (even $g_k^2$ would suffice).
