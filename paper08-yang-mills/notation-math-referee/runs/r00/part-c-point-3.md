## Part C, Point 3: The Coupling Regime Overlap

**Weight:** LIGHT
**Verdict:** GENUINE GAP — the cluster-expansion regime and the Balaban-RG regime are *not* shown to overlap quantitatively, and the K-vs-k issue makes the "transition" between them ill-defined.

**Finding:**

(a) **The overlap region.** The cluster expansion of Section 4 converges in the regime $\beta < \beta_{\max}(a) \sim a/(2\sqrt{N} r_3)$. In the physical regime $a/r_3 \sim 10^{15}$ this allows $\beta$ up to $\sim 10^{14}$. But Balaban's RG requires $g_0$ "sufficiently small" — typically $g_0 \lesssim 1$, i.e., $\beta_0 \gtrsim 2N$.

The intersection of these two regimes is *non-empty* for very large $\beta$ (small coupling), but the *physical regime* $\beta \sim 6$ (typical for SU(3) lattice QCD simulations) is in the Balaban regime, not in the cluster-expansion regime *unless* $a$ is so coarse that $\beta_{\max}(a) \gg 6$.

(b) **The transition.** Section 5.1 explicitly says: "The condition $g_0$ small corresponds to $\beta_0 = 2N/g_0^2$ large, *compatible with* the lattice mass gap of Section 4 (which holds for $\beta < a_0/(2\sqrt{3} r_3)$, satisfied when $a_0/r_3 \gg 1$)."

But "compatible with" is not "covered by." For the cluster expansion to apply *at the bare lattice scale where Balaban's RG starts*, we need $\beta_0 < a_0/(2\sqrt{N} r_3)$, i.e., $2N/g_0^2 < a_0/(2\sqrt{N} r_3)$, i.e., $g_0^2 > 4N\sqrt{N}r_3/a_0$. For $a_0/r_3 \sim 10^{15}$, this gives $g_0^2 > 10^{-14}$, which is satisfied at any reasonable $g_0$. So in the *physical* regime (large $a/r_3$), the cluster expansion *does* cover the bare scale $g_0$. Sound at the level of the regime intersection.

(c) **The K-vs-k confusion strikes again.** §5.7 Remark 1 says:
> "At $k = 0, 1, 2$ where $g_k^4 = O(1)$, first-order perturbation is not a priori justified. These finitely many steps are handled non-perturbatively via the cluster expansion, with bounded total contribution $K_0$ absorbed into $C_0$."

This is conceptually muddled. In the Balaban inner-$k$ convention, $k = 0$ is the *bare* (finest) lattice with the *largest* $g_0$, and $k \to \infty$ is the IR effective theory. The first few RG steps are at large $g_k$, where perturbation is not justified. The proof claims to handle these via "the cluster expansion," but the cluster expansion is not a substitute for Balaban's RG: it is a *parallel* method that controls the *bare* lattice mass gap at *coarse* lattices. It does NOT control the *RG flow* of the effective action.

Concretely: when the proof says "the first few steps are handled by the cluster expansion," it presumably means that the cluster expansion gives a starting condition $C_0 = O(1)$ and the RG recursion takes over from $k \geq k_0$ where $g_k$ is small enough for Balaban. But the *whole* RG flow from $k = 0$ to $k = \infty$ is then a hybrid: cluster expansion at the start, Balaban after that. The transition is not made rigorous.

Worse: under the K-vs-k confusion, "the cluster expansion at $k = 0$" could mean (a) cluster expansion at the bare coarse lattice $a_0(K=0)$ in the script's $K$ convention, or (b) cluster expansion at the fine bare lattice $a_0$ in the Balaban inner-$k$ convention. These are different objects. The preprint never disambiguates.

**To close:** state explicitly which $k=0$ is meant in §5.7 Remark 1 (the script's $K = 0$, presumably), and verify that the cluster expansion *and* Balaban's RG are valid in the SAME physical regime at the SAME scale. **Difficulty: 1–2 pages, assuming the K-vs-k notation is fixed first per Point C1.**

**Impact on the claimed result:** Significant, given Point C1. The proof's "regime overlap" argument depends on the K-vs-k separation being clean, which it currently is not.
