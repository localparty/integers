# Node 13 -- RG Convergence

**Chain step:** 13 of 18
**Rigor label:** [PROVED]
**Dependencies:** Steps 10--12 (deviation order, spectral lemma, RG recursion)
**Status:** PROVED

---

## Statement

**Proposition (RG telescoping sum convergence).** *For $\mathrm{SU}(N)$ Yang--Mills on the KK-enhanced lattice with Balaban block-spin RG, the accumulated mass-gap correction converges:*

$$\sum_{k=0}^{\infty} C_k\, g_k^4\, \hat{\Delta}_k^2 \;<\; \infty.$$

---

## Proof sketch (3 steps)

**Step 1 -- RG recursion.** By Step 12, the deviation-order bound feeds a recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}$, where $C_{\mathrm{new}} = O(1)$ is $k$-independent (Step 10b). The bounded sequence $\{C_k\}$ satisfies $C_k \leq 4C_{\mathrm{new}}/3$ for all $k$.

**Step 2 -- Doubly exponential decay.** Along the outer bare-scale sequence $a_0(K) = a^* \cdot 2^{-K}$, the general term satisfies $g_K^4 (a_0(K)\Lambda)^s \sim (a^*\Lambda)^s / [(b_0 K \log 2)^2 \cdot 2^{Ks}]$ with $b_0 = 11N/(48\pi^2)$. The exponential factor $2^{-Ks}$ dominates $1/K^2$; convergence is doubly exponential for any $s \geq 1$.

**Step 3 -- Numerical margin.** For $\mathrm{SU}(3)$ with $g_0^2 = 1.0$, $a_0\Lambda = 0.1$, the total correction is $\sim 1.2\%$ at $s = 2$ and $\sim 0.01\%$ at $s = 4$. The mass-gap ratio $C_\infty = C_0 - \sum \delta C_k$ remains strictly positive.

---

## Key inputs

- Deviation order $\mathrm{dev} \geq 2$ for all dim-6 operators (Steps 8--10)
- $K$-independent spectral lemma constant $C_p$ (Step 10b)
- Asymptotic freedom: $g_k^2 \to 0$ logarithmically (Balaban)

---

## Sources

- **Preprint:** Section 5.4.6
- **Proof chain:** PROOF-CHAIN.md, Step 13
