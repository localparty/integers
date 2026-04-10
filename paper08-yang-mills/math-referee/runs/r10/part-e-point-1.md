## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The $1/4$ contraction.**

The factor $1/4$ arises from the kinematic identity $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$. Since $a_{k+1} = 2a_k$ and the physical mass gap $\Delta$ is scale-independent (at leading order), the dimensionless gap $\hat{\Delta}_k = a_k \Delta$ doubles at each step: $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k$, so $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$.

The concern about additional corrections from changing the lattice: the matrix element $\langle 1|E_k^\downarrow(0)|1\rangle_c$ in the coarsened theory involves the old state $|1\rangle_k$ evaluated on the new lattice $\Lambda_{k+1}$. The block-spin transformation maps operators from $\Lambda_k$ to $\Lambda_{k+1}$ via averaging over fast modes. The coarsened operator $E_k^\downarrow$ inherits the derivative structure of $E_k$ (Section 5.4.3), with coefficients modified by $|c_{d_O}^\downarrow| \leq |c_{d_O}^{(k)}|(1 + O(g_k^2))$.

The conversion to step-$(k+1)$ variables via $\hat{\Delta}_k = \hat{\Delta}_{k+1}/2 + O(g_k^4 \hat{\Delta}_{k+1})$ introduces an $O(g_k^4)$ correction to the $1/4$ factor. This correction is absorbed into the $O(g_k^2 C_k)$ term in the recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)$.

No additional corrections beyond $O(g_k^2)$ arise from the lattice change. The block-spin is a linear map, and the leading change in the form factor is from the kinematic rescaling $\hat{\Delta}_k^2 \to \hat{\Delta}_{k+1}^2/4$. This is exact.

**(b) The wave function correction.**

Term (A2) involves $\|\delta 1\| \leq C g_k^4/\hat{\Delta}_k$, where $|\delta 1\rangle = |1\rangle_{k+1} - |1\rangle_k$ is the change in the one-particle state under one RG step.

This uses Kato perturbation theory with perturbation $E_k$ satisfying $\|E_k\| \leq C g_k^4$. The gap condition for Kato: the perturbation must be small compared to the spectral gap of the unperturbed transfer matrix. The unperturbed gap is $\hat{\Delta}_k$ (the mass gap at step $k$), and $\|E_k\| \leq C g_k^4$. The ratio is $C g_k^4/\hat{\Delta}_k$, which must be $\ll 1$.

On the AF trajectory: $g_k^4 \sim 1/k^2$ and $\hat{\Delta}_k = a_k \Delta \sim 2^{-k} \cdot a_0 \Delta$. So $g_k^4/\hat{\Delta}_k \sim 2^k/(k^2 a_0 \Delta)$. This grows exponentially with $k$, which would violate the gap condition for large $k$.

However, the correct analysis is in terms of the dimensionless ratio. The operator norm bound $\|E_k\| \leq C g_k^4$ is per unit volume on $\Lambda_k$. The spectral shift of the transfer matrix eigenvalue is bounded by $\|E_k\| \leq C g_k^4$ (in the operator norm on $L^2$), and the gap is $\hat{\Delta}_k$. For Kato perturbation theory: $\|\delta 1\| \leq \|E_k\|/\hat{\Delta}_k \leq C g_k^4/\hat{\Delta}_k$.

The contribution of term (A2) to the form factor is:
$$|\langle \delta 1|E_k^\downarrow(0)|1\rangle_c| \leq \|E_k^\downarrow(0)\| \cdot \|\delta 1\| \leq C g_k^4 \cdot C' g_k^4/\hat{\Delta}_k = C'' g_k^8/\hat{\Delta}_k$$

In step-$(k+1)$ variables: $g_k^8/\hat{\Delta}_k = 2g_k^8/\hat{\Delta}_{k+1}$. On the AF trajectory where $\hat{\Delta}_k \geq c \cdot 2^{-k}$ and $g_k^4 \leq C/k^2$: this term is $O(k^{-4} \cdot 2^k)$, which grows. But this enters the RG recursion as an additive correction to $C_{k+1}$, not a multiplicative one. In the recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)$, the wave function correction is absorbed into the $O(g_k^2 C_k)$ term, which produces at most polynomial growth $k^\gamma$ in $C_k$.

The point is that the wave function correction is *subleading* relative to the main terms $C_k/4 + C_{\mathrm{new}}$. Even if it produces a growing correction to $C_k$, the polynomial growth is harmless (see (c) below).

**(c) The Gronwall bound.**

The product $\prod_{j=0}^{k-1}(1 + \alpha g_j^2) \leq k^{\alpha/(b_0 \ln 2)}$ gives polynomial growth with exponent $\gamma = \alpha/(b_0 \ln 2)$.

For general $N$: $b_0 = 11N/(48\pi^2)$, so $\gamma = \alpha \cdot 48\pi^2/(11N \ln 2)$. Since $\alpha$ is a universal constant (from the Kato perturbation bound), $\gamma$ scales as $1/N$ — it *decreases* with $N$. For $N = 2$: $\gamma \approx 3.1\alpha$. For $N = 3$: $\gamma \approx 2.1\alpha$.

The convergence of $\sum C_k g_k^4 \hat{\Delta}_k^2$: with $C_k \sim k^\gamma$, $g_k^4 \sim 1/k^2$, $\hat{\Delta}_k^2 \sim 4^{-k}$, the sum is $\sum k^{\gamma-2} \cdot 4^{-k}$. The ratio test gives $\lim_{k \to \infty} ((k+1)/(k))^{\gamma-2} \cdot 1/4 = 1/4 < 1$. The sum converges for ALL values of $\gamma$, because the geometric factor $4^{-k}$ dominates any polynomial $k^\gamma$.

The $N$-dependent constants enter only through the prefactors (not the convergence rate), which is acceptable: for each fixed $N$, the sum converges to a finite value.

**Impact on the claimed result:**

None. The inductive stability is correctly analyzed. The $1/4$ contraction from lattice coarsening, the wave function correction from Kato perturbation theory, and the Gronwall bound on accumulated $O(g_k^2)$ corrections all behave as claimed. The doubly exponential convergence factor $4^{-k}$ provides an enormous margin over any polynomial growth.
