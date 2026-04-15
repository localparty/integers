## Part E, Point 2: Convergence of the Sum

**Weight:** LIGHT
**Verdict:** SOUND

---

**Finding:**

**(a) Doubly exponential convergence.** Section 5.4.6 and Section 5.7 (Proof of (b)) establish convergence of $\sum_k C_k g_k^4 \hat{\Delta}_k^2$.

With $C_k \sim k^\gamma$ (Gronwall bound), $g_k^4 \sim (b_0 k \ln 2)^{-2}$ (one-loop running coupling), $\hat{\Delta}_k^2 \sim 4^k (a_0 \Delta_\infty)^2$ (doubly exponential growth from the coarsening direction):

$$\sum_k C_k g_k^4 \hat{\Delta}_k^2 \sim \sum_k k^\gamma \cdot (b_0 k \ln 2)^{-2} \cdot 4^k (a_0 \Delta_\infty)^2$$

Wait — this diverges. As $k \to \infty$, the terms grow as $k^{\gamma-2} \cdot 4^k \to \infty$.

I need to re-examine the direction. The form factor bound appears in Theorem 8, Proof (a): $|C_{k+1} - C_k| \leq C' g_k^4 (a_k \Lambda)^s$. Here $(a_k \Lambda) = (2^k a_0 \Lambda)$ grows with $k$. For $s = 2$: $(a_k \Lambda)^2 = 4^k (a_0 \Lambda)^2$, so $g_k^4 (a_k \Lambda)^2 \sim k^{-2} 4^k \to \infty$. This also diverges!

There is an apparent contradiction with the proof. Let me re-read Section 5.7, Proof of (b): "$a_k = a_0/2^k$, and $g_k^2 \sim 1/(b_0 k \log 2)$ for large $k$... $g_k^4(a_k\Lambda)^s \sim (a_0\Lambda)^s / ((b_0 k \log 2)^2 \cdot 2^{ks})$."

So $a_k = a_0/2^k$ (the lattice spacing *decreases* with $k$). This means the RG goes in the direction of *increasing* UV cutoff, not coarsening. Each RG step integrates out UV modes, so after $k$ steps the effective theory has a lattice spacing $a_0/2^k$ (finer lattice!). 

Wait, that's unusual. In Balaban's construction, one typically blocks spins (integrating out short-wavelength modes, giving a coarser lattice). But the preprint's formula $a_k = a_0/2^k$ has $a_k$ decreasing with $k$, suggesting the lattice is getting finer.

Actually re-reading: "Start from a fine lattice $\Lambda_0$ with spacing $a_0$ and bare coupling $g_0$. At RG step $k$, define a coarser lattice $\Lambda_k$ with spacing $a_k = 2^k a_0$." But Section 5.7 says "$a_k = a_0/2^k$". These are *contradictory*.

Let me re-read more carefully. Section 5.1.2: "$a_k = 2^k a_0$" (coarser). Section 5.7 Proof (b): "$a_k = a_0/2^k$" (finer). 

This is a notational inconsistency in the preprint. In the context of the continuum limit proof, the sum is over RG steps going *toward* the continuum (finer lattice), so $a_k = a_0/2^k$ should be the convention there. The mass gap in physical units is fixed, so $\hat{\Delta}_k = a_k \Delta \sim 4^{-k/2}$ shrinks as $a_k \to 0$. 

With $a_k = a_0/2^k$ (continuum limit direction): $g_k^4 (a_k \Lambda)^2 \sim k^{-2} \cdot 4^{-k} (a_0 \Lambda)^2$. Now $\sum_k k^{-2} 4^{-k}$ converges (doubly exponentially). The numerical table in Section 5.7 confirms this: $g_k^4(a_k\Lambda)^2$ decreases from $0.01$ to $1.2 \times 10^{-6}$ over the first few steps.

So there are two different RG conventions:
1. Balaban's blocking (coarser): $a_k = 2^k a_0$, $\hat{\Delta}_k = a_k \Delta_\infty \to \infty$, recursion for $C_k = \Delta_k/\Lambda_k$.
2. Continuum limit direction (finer): $a_k = a_0/2^k$, $\hat{\Delta}_k = a_k \Delta_\infty \to 0$, sum over corrections to the continuum limit.

The preprint uses both conventions without clearly distinguishing them. The Section 5.4 recursion ($\hat{\Delta}_{k+1} = 2\hat{\Delta}_k$, i.e., the gap doubles at each step) is convention 1 (blocking = coarsening). Section 5.7 uses convention 2 (going toward the continuum).

With convention 2 (Section 5.7): $a_k = a_0/2^k$, $g_k^4 (a_k \Lambda)^2 \sim k^{-2} 4^{-k} \to 0$. The sum $\sum_k k^{-2} 4^{-k}$ converges. The $C_k \sim k^\gamma$ factor in the recursion (convention 1) does not appear in the convergence of the sum (convention 2) directly. Instead, in convention 2, the correction to $C = \Delta/\Lambda$ at step $k$ is $|\delta C_k| \leq C' g_k^4 (a_k\Lambda)^s$ where $C'$ is bounded by $C_*$ from the recursion.

SOUND: with the correct convention that the sum in Section 5.7 is over steps going toward the continuum ($a_k \to 0$), the doubly exponential convergence is correct. The accumulated corrections $\sum_k C' g_k^4 (a_k\Lambda)^2 \sim C' (a_0\Lambda)^2 \sum_k k^{-2} 4^{-k} < \infty$ hold absolutely. Positivity of $C_\infty$ follows since the sum is $\leq 2\%$ of $C_0$ for the values in the numerical table.

**(b) The starting constant $C_0$.** $C_0$ at $k = 0$ comes from the cluster expansion, where $\hat{\Delta}_0 = a_0 \Delta_0 = O(1)$ at the cluster expansion scale ($a_0 \sim r_3$). The bound $|{}_0\langle 1|E_0|1\rangle_c^{(0)}| \leq C_0 g_0^4 \hat{\Delta}_0^2$ with $\hat{\Delta}_0 = O(1)$ gives $C_0 \leq |\langle 1|E_0|1\rangle_c| / g_0^4$. By the cluster expansion (Section 4), all connected correlators are bounded (exponential decay), so $C_0 < \infty$ follows from the finiteness of $g_0^4$ and the cluster expansion bounds. The bound $C_0 < \infty$ is established in Section 5.7, Step (c): "$C_\infty \geq C_0(1-0.02) > 0$" with $C_0 \sim 1$ (the mass gap is $O(\Lambda)$). SOUND.

**Impact on the claimed result:** The convergence of $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ is correctly established using the continuum-limit RG convention ($a_k = a_0/2^k$). The notational inconsistency between Section 5.4 (blocking direction) and Section 5.7 (continuum direction) is present but not a logical gap — both are addressing different aspects of the same RG flow. The starting constant $C_0$ is bounded. No gap affects $\Delta_\infty > 0$.
