## Part G, Point 3: $N$-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** SOUND for the SU(N) case (constants are finite for each fixed $N$, the doubly-exponential convergence factor absorbs polynomial $N$-growth) — but conditional on the K-vs-k issue (Point C1), and the "doubly-exponential factor $4^{-k}$" is contradicted by §5.4.1's setup.

**Finding:**

(a) **N-dependent constants.** Appendix I.3 catalogs all N-dependent constants:

| Constant | $N$-scaling | Direction | Impact |
|---|---|---|---|
| Spectral gap $\mu_1$ | $\sim N$ | Favorable | Larger gap |
| KK mass $m_1$ | $\sim \sqrt N$ | Favorable | Stronger decay |
| Bond constant $C_0$ | $\leq \exp(\text{poly}(N))$ | Unfavorable | Absorbed by $e^{-m_1 a}$ |
| Polymer decay $\kappa$ | Weakly $N$-dep | Unfavorable | Finite for each $N$ |
| Analyticity radius $\rho$ | $O(1/N^2)$ | Unfavorable | Positive for each $N$ |
| $\beta$-function $b_0$ | $\sim N$ | Favorable | Faster AF |
| Gronwall $\gamma$ | $\sim N$ | Unfavorable | Absorbed by $4^{-k}$ |
| Spectral lemma $C_p$ | $\leq \exp(C N^2)$ | Unfavorable | Finite for each $N$ |
| Fixed point $C_*$ | $\leq \exp(C' N^2)$ | Unfavorable | Finite for each $N$ |

**Important sub-issue:** the I.3.2 item 1 formula "actual $\mu_{\min}^{(1)} = 4N/r_3^2$" is N=3-correct but does not match Appendix H's value $2/r_2^2$ for the SU(2) case ($\mathbb{CP}^1 = S^2$). The "$4N/r_3^2$" formula for $N=2$ gives $8/r_3^2$, four times the value $2/r_3^2$ in Appendix H. The discrepancy is not addressed and is presumably due to a convention difference in the meaning of "$r_3$" between sections. See Point A1 for full details.

(b) **SU(2) special properties.** SU(2) has $d^{abc} = 0$ (the cubic Casimir vanishes), so the operators $\mathcal{O}_3 = d^{abc} F^a F^b F^c$ vanish identically. The proof handles this by noting that for $N=2$, the entire $\mathcal{C}$-elimination is automatic (no cubic operator to eliminate). For $N \geq 3$, the $\mathcal{C}$-elimination is needed.

$\mathbb{CP}^1 = S^2$ is a special case (round sphere instead of higher-dimensional Kähler manifold). Appendix H gives an *independent* proof for SU(2) using 2D Yang–Mills exact solvability:
$$\sigma_{SU(2)} = 3g^2/8, \quad \Delta_{SU(2)} = 2\sqrt{\pi\sigma/3}$$
This uses the heat kernel on $SU(2)$ and the exact 2D YM partition function on $S^2$.

**However**, this independent proof uses a *fundamentally different* construction: a 6-dimensional KK reduction on $S^2$, not the 4D Wilson lattice gauge theory of Section 4.1. The two constructions are not obviously equivalent, and the SU(2) result via 2D YM does NOT follow from the proof's main framework.

The "exact area law $\sigma = 3g^2/8$" derived in Appendix H is for *2D Yang–Mills on $S^2$*, not for *4D Yang–Mills with $S^2$ as internal*. The argument that 2D YM on $S^2$ has area law (via Peter–Weyl + heat kernel) is a known result, but the leap to "4D YM on $S^2$ inheri ts the area law" is not justified in Appendix H. The KK reduction argument is presented as physics intuition, not as a rigorous mathematical step.

**This is a real issue for SU(2).** The "warm-up" appendix provides a cleaner SU(2) proof in spirit but does not deliver a rigorous SU(2) mass gap via the same proof structure as SU(N). The two are different constructions with different rigor levels.

(c) **Error compounding.** The proof has ~14 steps. Each step's constant has some N-dependence. The worst-case constant is the Combes–Thomas $\zeta(N) \leq \exp(C R_0^3 N^2)$, which enters $C_p(N) \sim \exp(C R_0^4 N^2)$. This is *exponential in $N^2$*, but only as a multiplicative constant — it does not affect the convergence ratio $1/4$ in the RG sum.

The $4^{-k}$ doubly-exponential decay (under the bare-refinement convention; Point C1) absorbs any polynomial or sub-exponential $N$-dependence. But, as noted in Points C1, E1, E2, the "$4^{-k}$" itself is contradicted by §5.4.1's $a_k = 2^k a_0$ convention. So the N-dependence absorption argument is contingent on Point C1.

**For the SU(N) proof to work uniformly across all $N \geq 2$**, the Combes–Thomas exponent $C R_0^4 N^2$ must be finite (which it is for each fixed $N$) and the convergence factor $1/4$ must be effective (which requires the K-vs-k separation).

**Impact on the claimed result:** SOUND for each fixed $N$ separately, modulo the K-vs-k issue and the unverified SU(2) "warm-up" using a different construction. The proof does NOT establish $\Delta_\infty(N) > 0$ uniformly in $N$ (no large-$N$ limit is claimed), but for each $N \geq 2$ the argument is structurally complete.
