## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that $C_{K+1} = C_K/4 + C_{\mathrm{new}} + O(g_K^2 C_K)$ has a stable fixed point $C_* = (4/3)C_{\mathrm{new}}$ with polynomial growth $C_K \sim K^\gamma$.

**(a) The $1/4$ contraction.** The factor $1/4$ is the kinematic identity $\hat{\Delta}_{K+1}^2 = \hat{\Delta}_K^2/4$ from the bare refinement $a_0(K+1) = a_0(K)/2$ (Section 5.4.3, equation 5.4.1a). It is NOT a physical contraction from Wilsonian flow — it arises because the dimensionless gap $\hat{\Delta}_K = a_0(K) \Delta_{\mathrm{phys}}$ shrinks when the lattice is refined. The paper is explicit about this distinction.

The physical matrix element $\langle 1|E_k^\downarrow(0)|1\rangle_c$ is unchanged when re-expressed in the new lattice units; the $1/4$ appears only in the bookkeeping of the dimensionless coefficient $C_K$. The change of lattice introduces corrections only through the coupling change $g_K \to g_{K+1}$ and the wave function correction (term A2), both of which are $O(g_K^2)$ and absorbed into the error term. No additional lattice artifacts beyond $O(g_K^2)$ are introduced.

**(b) The wave function correction.** Term (A2) satisfies $|\langle\delta 1|E_k^\downarrow(0)|1\rangle_k^c| \leq C'' g_k^8/\hat{\Delta}_k$. This uses Kato perturbation theory with gap condition $\|E_k\| \ll \hat{\Delta}_k$. On the AF trajectory where $\hat{\Delta}_k \gtrsim g_k^{4/3}$, the term is $O(g_k^4 \hat{\Delta}_{k+1}^2 \cdot g_k^4/\hat{\Delta}_k^3)$, subleading relative to the (A1) contribution. The Kato gap condition requires $\|E_k\| = O(g_k^4) \ll \hat{\Delta}_k$; since $\hat{\Delta}_k \gg g_k^4$ on the AF trajectory for large $k$, this is satisfied.

**(c) The Gronwall bound.** The product $\prod(1 + \alpha g_j^2) \leq k^{\alpha/(b_0 \ln 2)}$ gives polynomial growth $C_K \sim K^\gamma$ with $\gamma = \alpha/(b_0 \ln 2)$. For SU($N$): $b_0 = 11N/(48\pi^2)$, so $\gamma = 48\pi^2 \alpha/(11N \ln 2)$. If $\alpha$ is $N$-independent, $\gamma$ decreases with $N$ — the growth is milder for larger $N$. If $\alpha$ has polynomial $N$-dependence (as tracked in Appendix I.3), $\gamma$ could grow, but the convergence of $\sum K^{\gamma-2} 4^{-K}$ is guaranteed for any finite $\gamma$ by the doubly exponential factor $4^{-K}$.

Verified computationally: the fixed point $C_* = 4C_{\mathrm{new}}/3$ and the geometric convergence rate $1/4$ per step. The sum $\sum K^{\gamma-2} 4^{-K}$ converges for all $\gamma$ tested ($\gamma = 0, 1, 2, 5, 10$).

**Impact on the claimed result:**
No impact. The recursion algebra is straightforward and correct. The $1/4$ contraction is kinematic and robust.
