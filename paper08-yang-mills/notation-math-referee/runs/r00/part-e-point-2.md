## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** GENUINE GAP (same K-vs-k issue as E1; the sum *would* converge if $\hat\Delta_k^2 \sim 4^{-k}$, but the §5.4.1 setup gives $\hat\Delta_k^2 \sim 4^{+k}$, making the actual sum divergent)

**Finding:**

(a) **The doubly-exponential convergence.** Under the assumption $\hat\Delta_k^2 \sim 4^{-k}$ (which is what §5.4.6 wants), the sum is
$$\sum_k C_k g_k^4 \hat\Delta_k^2 \sim \sum_k k^{\gamma-2} \cdot 4^{-k}$$
which converges (verified computationally; ratio test gives $1/4 < 1$). This is fine as an algebraic computation under the assumed scaling.

But the assumed scaling **contradicts §5.4.1's** $\hat\Delta_{k+1} = 2 \hat\Delta_k$, which gives $\hat\Delta_k^2 \sim 4^{+k}$. Under the §5.4.1 convention, the sum is
$$\sum_k C_k g_k^4 \cdot 4^{+k} \sim \sum_k k^{\gamma-2} \cdot 4^{+k}$$
which **diverges** (verified computationally; ratio test gives $4 > 1$).

So the §5.4.6 convergence claim is conditional on the *opposite* convention from §5.4.1. As written, the proof contradicts itself.

(b) **The starting constant $C_0$.** Under the *bare-refinement* (corrected) convention, $C_0 = C_{K=0}$ is the form-factor constant of the starting (coarsest) bare theory. It is bounded by the cluster expansion of Section 4 (since the cluster expansion regime covers the coarsest bare scale where $g_0$ may be O(1)). So $C_0 < \infty$ unconditionally. Sound under the corrected convention.

The fixed point $C_* = (4/3) C_{\mathrm{new}}$ and the geometric convergence $C_K = C_* + (C_0 - C_*) 4^{-K}$ both presume $\hat\Delta_K^2 \sim 4^{-K}$ (refining), in which case the recursion $C_{K+1} = C_K/4 + C_{\mathrm{new}}$ has the $1/4$ contraction *as a stable contraction*, with attractor $C_*$.

Under the §5.4.1 (Balaban inner) convention, the recursion would be $C_{k+1} = 4 C_k + C_{\mathrm{new}}$ — a *blow-up*, not a contraction. So the proof's "stable fixed point" is also conditional on the corrected convention.

**Impact on the claimed result:** The same as E1. The convergence sum, as actually computed under §5.4.1, is divergent. Re-stating in the script's $K$ convention recovers the correct convergence, but the proof never makes this distinction.
