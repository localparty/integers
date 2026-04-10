## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The $1/4$ contraction.** The factor $1/4$ arises from $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$, which follows from $\hat{\Delta}_k = a_k \Delta = (a_{k+1}/2)\Delta = \hat{\Delta}_{k+1}/2$. This is a kinematic identity: doubling the lattice spacing halves the dimensionless gap.

The concern about the change of lattice: the old state $|1\rangle_k$ on $\Lambda_k$ is related to $|1\rangle_{k+1}$ on $\Lambda_{k+1}$ by the wave function change $|\delta 1\rangle$. The matrix element $\langle 1|E_k^\downarrow(0)|1\rangle_c$ in the coarsened theory uses the old state evaluated on the new lattice. The additional corrections beyond $O(g_k^2)$ from the lattice change are accounted for in term (A2): the cross terms from $|\delta 1\rangle$ contribute $O(g_k^8/\hat{\Delta}_k)$, which is subleading on the AF trajectory.

**(b) The wave function correction.** Term (A2) uses $\|\delta 1\| \leq Cg_k^4/\hat{\Delta}_k$ from Kato perturbation theory. The gap condition for Kato perturbation IS satisfied: Kato perturbation requires $\|E_k\| < \hat{\Delta}_k/2$ (the perturbation must be smaller than the spectral gap of the unperturbed operator). With $\|E_k\| \leq Cg_k^4$ and $\hat{\Delta}_k \geq c \cdot 4^{-k/2}$ (from the doubling), the condition $Cg_k^4 < \hat{\Delta}_k/2$ becomes $Cg_k^4 < c \cdot 4^{-k/2}/2$. On the AF trajectory, $g_k^4 \sim 1/k^2$, so this requires $C/k^2 < c \cdot 4^{-k/2}/2$. This is satisfied for large $k$ (the exponential dominates) but may fail for the first few steps. The initial steps are handled non-perturbatively (Remark 1 of Section 5.7).

For large $k$, the bound $\|\delta 1\| \leq Cg_k^4/\hat{\Delta}_k$ is valid, and the cross term $|\langle \delta 1|E_k^\downarrow(0)|1\rangle_c| \leq \|E_k^\downarrow\| \cdot \|\delta 1\| = O(g_k^8/\hat{\Delta}_k)$ is subleading.

**(c) The Gronwall bound.** The product $\prod_{j=0}^{k-1}(1 + \alpha g_j^2) \leq k^{\alpha/(b_0 \ln 2)}$ gives polynomial growth with exponent $\gamma = \alpha/(b_0 \ln 2)$. For $b_0 = 11N/(48\pi^2)$: $\gamma = 48\pi^2 \alpha/(11N \ln 2)$.

The exponent $\gamma$ depends on $N$ through $b_0$, growing as $1/N$ for large $N$. For each fixed $N$, $\gamma$ is a finite constant. The convergence of $\sum C_k g_k^4 \hat{\Delta}_k^2 \sim \sum k^{\gamma-2} 4^{-k}$ is guaranteed for ALL $\gamma$ by the doubly exponential factor $4^{-k}$. Even for $\gamma = 100$ (which would require $N = 1$, not a valid SU($N$)), the series converges.

The constants become $N$-dependent but the mass gap $\Delta_\infty > 0$ holds for each fixed $N$. The Clay prize requires the result for each fixed $N$, not uniformly in $N$.

**Impact on the claimed result:** None. The inductive stability is robust.
