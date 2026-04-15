## Part A, Point 1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP (sub-point b); SOUND WITH CAVEAT (sub-point a)

---

**Finding:**

**(a) The spectral bound.** The Weitzenböck formula $\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$ is correctly applied. On $(\mathbb{CP}^{N-1}, g_\mathrm{FS})$ with holomorphic sectional curvature $4/r_3^2$, the Ricci tensor is Einstein with $R_{ab} = (2N/r_3^2)\,g_{ab}$ (Section 4.2, Step 2), yielding the lower bound $\mu_1 \geq 2N/r_3^2$.

For $N = 3$: $\mu_1 \geq 6/r_3^2$. The abstract writes "$\mu_1 \geq 6/r_3^2$" as the Weitzenböck bound — this is correct but applies only to $N = 3$. The general bound is $\mu_1 \geq 2N/r_3^2$, as Theorem 1's Remark 3 states. This holds for all $N \geq 2$ with the bound improving linearly in $N$. SOUND.

There is, however, an internal numerical error: Appendix I.3 (file `I3-N-dependence-tracking.md`) claims the exact first eigenvalue is $\mu_{\min}^{(1)} = 2(N+1)/r_3^2$ (citing Ikeda–Taniguchi 1978). For $N = 3$ this gives $8/r_3^2$. Appendix E (file `E-weitzenboeck.md`, Section G.5) contradicts this, stating $\mu_{\min}^{(1)} = 12/r_3^2$ for $\mathbb{CP}^2$. Section 4.2, Step 3 also states $12/r_3^2$ citing Ikeda–Taniguchi. The correct value for $\mathbb{CP}^{N-1}$ is $4N/r_3^2$ (matching $12/r_3^2$ for $N = 3$); the formula $2(N+1)/r_3^2$ in Appendix I.3 is wrong. This inconsistency propagates to I.3's KK mass formula ($m_1 = \sqrt{2(N+1)}/r_3$ vs. the correct $2\sqrt{N}/r_3$) and the Gronwall exponent sign. Closing requires: correct I.3's formula and verify the Ikeda–Taniguchi citation. Difficulty: **1 paragraph**.

**(b) The connection to KK mass.** The abstract states "$\mu_1 \geq 6/r_3^2$" and immediately concludes "$m_1 = 2\sqrt{3}/r_3$." These are numerically inconsistent: $\sqrt{6/r_3^2} = \sqrt{6}/r_3 \approx 2.45/r_3 \neq 2\sqrt{3}/r_3 \approx 3.46/r_3$.

The derivation path in the abstract is misleading. The quantity $m_1 = 2\sqrt{3}/r_3$ comes from the *exact* first eigenvalue $\mu_{\min}^{(1)} = 12/r_3^2 = 4N/r_3^2\vert_{N=3}$ (as documented in App E/Section 4.2 Step 3), not from the Weitzenböck lower bound $6/r_3^2$. Theorem 1's own Remark 2 is careful: "the proof only uses the Weitzenböck lower bound $\mu_1 = 6/r_3^2$. This builds in a safety factor of two." The proof therefore establishes bond activity bound $|g_b| \leq C_0 e^{-\sqrt{6}\,a/r_3}$ via the lower bound, but the abstract claims the tighter $e^{-2\sqrt{3}\,a/r_3}$ from the exact eigenvalue.

The discrepancy has no impact on the existence proof: using $m_1 = \sqrt{6}/r_3$ (lower bound) is more conservative and still gives doubly-exponential suppression. But the abstract's stated logical chain — "Weitzenböck gives $\mu_1 \geq 6/r_3^2$, therefore $m_1 = 2\sqrt{3}/r_3$" — is a non sequitur. There is also no proof that the KK mass for gauge fields equals $\sqrt{\mu_1}$ rather than something else; the relationship between the Hessian eigenvalue and the transfer-matrix spectral gap is assumed but not derived. Closing requires: either (i) remove $m_1 = 2\sqrt{3}/r_3$ from the abstract and use $m_1 \geq \sqrt{6}/r_3$ throughout, or (ii) cite the exact Ikeda–Taniguchi spectrum ($4N/r_3^2$) explicitly for the quantitative claim. Difficulty: **1 paragraph**.

**Impact on the claimed result:** Sub-point (a) inconsistency (I.3 formula error) affects quantitative constants in Appendix I.3 but not the existence proof. Sub-point (b) inconsistency (abstract's derivation path) is a presentation error that does not affect the main claim $\Delta_\infty > 0$. Both are closable.
