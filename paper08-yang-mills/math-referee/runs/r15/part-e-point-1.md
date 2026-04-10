## Part E, Point 1: Inductive Stability of the RG Recursion

**Weight:** MEDIUM
**Verdict:** SOUND

---

### The Claim Under Review

Section 5.4 claims:

1. The RG recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)$ has a stable fixed point $C_* = (4/3)C_{\mathrm{new}}$.
2. The accumulated $O(g_k^2)$ corrections produce at most polynomial growth $C_k \sim k^\gamma$ with $\gamma = \alpha/(b_0 \ln 2)$.
3. The sum $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ despite this growth.

---

### Sub-point (a): Does the change of lattice introduce corrections beyond $O(g_k^2)$?

**Interrogation:** The factor $1/4$ comes from $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$, which is a kinematic identity for the dimensionless gap. But the matrix element $\langle 1|E_k^{\downarrow}(0)|1\rangle_c$ involves the old state $|1\rangle_k$ evaluated on the new lattice $\Lambda_{k+1}$. Does the change of lattice introduce additional corrections?

**Finding:** The paper's argument is more careful than the question suggests. The key passage (Section 5.4.3) states:

> "The coarsened operator $E_k^{\downarrow}$ on $\Lambda_{k+1}$ inherits the derivative structure of $E_k$, with coefficient $|c_{d_O}^{\downarrow}| \leq |c_{d_O}^{(k)}|(1+O(g_k^2))$."

The factor $(1+O(g_k^2))$ is precisely where the lattice change corrections enter. The term (A1) is the matrix element of the OLD operator $E_k^{\downarrow}$ in the OLD state $|1\rangle_k$. No re-expression of the state on a different lattice is performed at this stage. The state $|1\rangle_k$ lives on $\Lambda_k$; the operator $E_k^{\downarrow}$ is the restriction/coarsening of $E_k$ to the block field $V$ on $\Lambda_{k+1}$, but the matrix element is still computed on $\Lambda_k$. The only lattice change is in the bookkeeping: converting $\hat{\Delta}_k$ to $\hat{\Delta}_{k+1}$ variables via $\hat{\Delta}_k = \hat{\Delta}_{k+1}/2 + O(g_k^4 \hat{\Delta}_{k+1})$.

The $(1+O(g_k^2))$ factor on the coefficient $c_{d_O}^{\downarrow}$ accounts for the modification of the irrelevant operator's coefficient when expressed in terms of the block field. This is standard in Balaban's framework: the block-spin integration modifies irrelevant couplings by perturbative corrections at each step, and the leading correction is $O(g_k^2)$ (one-loop contribution). The $O(g_k^2)$ is correct because the leading correction comes from the one-loop fluctuation determinant, which carries one power of $g_k^2$ (the saddle-point expansion is in powers of $g_k^2$).

There is no hidden source of corrections beyond $O(g_k^2)$. The kinematic identity $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$ is exact at leading order; the $O(g_k^4)$ correction from $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k(1 + O(g_k^4))$ is subleading compared to $O(g_k^2)$ and is absorbed into the existing error term.

**Assessment: SOUND.** The factor $(1+O(g_k^2))$ correctly captures all corrections from the lattice coarsening.

---

### Sub-point (b): Is the gap condition for Kato perturbation satisfied?

**Interrogation:** Term (A2) uses $\|\delta 1\| \leq C g_k^4/\hat{\Delta}_k$ from Kato perturbation theory applied to $\|E_k\| \leq C g_k^4$. Kato perturbation theory for an isolated eigenvalue requires that the perturbation norm be small compared to the spectral gap. Is this condition verified?

**Finding:** This is the most substantive question in this point. Standard Kato perturbation theory (Kato, *Perturbation Theory for Linear Operators*, Chapter II, Theorem 6.8 and Section IV.3) for the eigenvector of an isolated simple eigenvalue gives:

$$\|\delta \psi\| \leq \frac{\|V\|}{\mathrm{dist}(\lambda, \sigma \setminus \{\lambda\})}$$

where $V$ is the perturbation, $\lambda$ is the isolated eigenvalue, and $\sigma \setminus \{\lambda\}$ is the rest of the spectrum. The condition for this to be a valid first-order estimate is $\|V\| \ll \mathrm{dist}(\lambda, \sigma \setminus \{\lambda\})$.

In the present context:
- The perturbation is $E_k$ with $\|E_k\| \leq C g_k^4$ per site.
- The eigenvalue is $E_1 = \hat{\Delta}_k$ (the one-particle energy).
- The relevant spectral gap is $\min(E_1 - E_0, E_2 - E_1) = \min(\hat{\Delta}_k, E_2 - E_1)$.

From Section 5.5.3, Step 3 (which I verified independently), $E_2 - E_1 \geq \hat{\Delta}_k/2$ for $g_k$ sufficiently small. The gap below $E_1$ is $E_1 - E_0 = \hat{\Delta}_k$. So the relevant spectral gap is $\hat{\Delta}_k/2$.

The Kato condition requires $C g_k^4 \ll \hat{\Delta}_k/2$, i.e., $g_k^4/\hat{\Delta}_k \ll 1$. On the asymptotically free trajectory, $g_k^2 \sim 1/(b_0 k \ln 2)$, so $g_k^4 \sim 1/(b_0 k \ln 2)^2$. Meanwhile, $\hat{\Delta}_k$ is bounded below by $\hat{\Delta}_\infty > 0$ (the dimensionless gap has a positive limit, since $\hat{\Delta}_k = a_k \Delta_k$ with $\Delta_k \to \Delta_\infty > 0$ and $a_k = 2^k a_0$ growing, so actually $\hat{\Delta}_k$ GROWS with $k$). Wait -- this requires care. $\hat{\Delta}_k = a_k \Delta_k$, with $a_k = 2^k a_0$ and $\Delta_k \to \Delta_\infty$. So $\hat{\Delta}_k \sim 2^k a_0 \Delta_\infty$, which grows exponentially. The ratio $g_k^4 / \hat{\Delta}_k \sim 1/(k^2 \cdot 2^k) \to 0$ rapidly. The Kato condition is satisfied for all $k \geq k_0$ with $k_0$ depending on the initial conditions.

For finitely many initial steps $k < k_0$ where the condition might not hold, the paper addresses this in Section 5.7, Remark 1: "At $k = 0,1,2$ where $g_k^4 = O(1)$, first-order perturbation is not a priori justified. These finitely many steps are handled non-perturbatively via the cluster expansion, with bounded total contribution $K_0$ absorbed into $C_0$." This is legitimate: finitely many bounded contributions to an inductive sequence do not affect the convergence of the series.

The bound $\|\delta 1\| \leq C g_k^4 / \hat{\Delta}_k$ is the standard Kato resolvent estimate for eigenvector perturbation. The gap condition IS satisfied (eventually, and the finite initial segment is handled separately).

**Assessment: SOUND.** The gap condition for Kato perturbation theory is satisfied for all $k \geq k_0$ on the asymptotically free trajectory, and the finitely many initial steps are handled non-perturbatively.

---

### Sub-point (c): Is the exponent $\gamma$ bounded for all $N$?

**Interrogation:** The product $\prod(1 + \alpha g_j^2) \leq k^{\alpha/(b_0 \ln 2)}$ gives polynomial growth with exponent $\gamma = \alpha/(b_0 \ln 2)$. If $\gamma$ grows with $N$, does this jeopardize convergence?

**Finding:** Appendix I.3 (Section I.3.2, item 9) addresses this directly:

> "$\gamma \sim N^2 / N = N$"

The exponent $\gamma$ grows linearly with $N$. The parameter $\alpha$ involves the adjoint Casimir $C_2(G) = N$ and additional group-theoretic factors, giving $\alpha \sim N^2$; meanwhile $b_0 = 11N/(48\pi^2) \sim N$, so $\gamma \sim N$.

The critical question is whether this $N$-dependent $\gamma$ breaks convergence. It does not. The sum $\sum_k k^{\gamma - 2} \cdot 4^{-k}$ converges for ALL finite $\gamma$, by the ratio test:

$$\frac{(k+1)^{\gamma-2} \cdot 4^{-(k+1)}}{k^{\gamma-2} \cdot 4^{-k}} = \frac{1}{4}\left(\frac{k+1}{k}\right)^{\gamma-2} \to \frac{1}{4} < 1$$

The ratio limit $1/4$ is independent of $\gamma$ (and hence of $N$). The VALUE of the sum depends on $N$ -- for larger $N$, more terms are needed before the geometric decay dominates the polynomial growth -- but the sum converges for every fixed $N$.

Appendix I.3 makes this point precisely (Lemma I.3.1):

> "Since $\gamma(N)$ is finite for each fixed $N$, the ratio test limit is $1/4 < 1$ regardless of the value of $\gamma(N)$, and the sum converges absolutely."

The paper does not claim uniformity in $N$. The theorem is stated for each fixed $N \geq 2$, and the mass gap $\Delta_\infty(N) > 0$ is established independently for each $N$. The Clay problem asks for $\Delta_\infty > 0$ for any compact simple gauge group; it does not require the gap to be uniform in the rank. The paper's approach -- proving $\Delta_\infty(N) > 0$ for each fixed $N$ -- is sufficient.

The constants become $N$-dependent: $C_*(N) = (4/3) C_{\mathrm{new}}(N)$ with $C_{\mathrm{new}}(N) \leq \exp(C' N^2)$ (from the Combes-Thomas bound on $\zeta(N)$). This enters as a multiplicative prefactor in the convergent sum and does not affect the convergence ratio. The final bound is:

$$\sum_{k=1}^{\infty} C_k g_k^4 \hat{\Delta}_k^2 \leq \frac{C_*(N)}{(b_0(N) \ln 2)^2} \sum_{k=1}^{\infty} k^{\gamma(N)-2} \cdot 4^{-k} < \infty$$

for each fixed $N$.

**Assessment: SOUND.** The $N$-dependence of $\gamma$ does not affect convergence. The proof is correct for each fixed $N$, which is what is required.

---

### Overall Verdict for E1

**Verdict: SOUND**

All three sub-points check out:

(a) The $(1+O(g_k^2))$ factor correctly captures lattice coarsening corrections; no hidden contributions exist beyond the stated order.

(b) The Kato gap condition $\|E_k\| \ll \hat{\Delta}_k$ is satisfied for all sufficiently large $k$ on the asymptotically free trajectory, with finitely many initial steps handled non-perturbatively via the cluster expansion.

(c) The exponent $\gamma \sim N$ grows with $N$ but cannot defeat the geometric convergence factor $4^{-k}$. The proof works for each fixed $N \geq 2$.

The RG recursion analysis is mathematically clean. The contraction factor $1/4$ is a robust geometric property of the $L=2$, $d=4$ blocking, not sensitive to perturbative corrections. The fixed-point structure $C_* = (4/3)C_{\mathrm{new}}$ with geometric approach $C_k = C_* + (C_0 - C_*) \cdot 4^{-k}$ (at leading order) is a standard result for affine contractions. The Gronwall-type bound converting multiplicative $O(g_k^2)$ corrections into polynomial growth is textbook (the discrete Gronwall inequality with $\sum g_j^2 = O(\ln k)$ giving $k^{\gamma}$ growth is a direct consequence of $\exp(\sum_{j=1}^{k} 1/j) \sim k$).

**Impact on the claimed result:** None. This component of the proof is correct.
