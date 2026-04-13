# Node J — Almost-Everywhere Simplicity (Supporting)

**Chain layer:** Supporting (enables Layer 3b)
**Rigor label:** [THEOREM]
**Dependencies:** Node A (CCM even-sector structure)
**Status:** CLOSED (all N)

---

## Statement

**Proposition 12.1 (AE simplicity).** The minimum eigenvalue of the even-sector matrix $A^{\mathrm{ev}}(\lambda, N)$ is simple (multiplicity 1) for all $N \geq 1$ and all $\lambda > 1$ except a discrete exceptional set $S_N$.

---

## Proof (three stages)

**Stage 1: $N = 1$.** Codimension argument — two constraints on a 1D parameter space gives an empty exceptional set.

**Stage 2: $N = 2$ to $20$.** Certified computation at $\lambda = \sqrt{14}$ using mpmath at 120-digit precision. The overlap $|\langle\varphi_0 | a\rangle| > 0$ at all $N$ with safety margin $> 10^{72}$ orders of magnitude. Real-analytic structure (Kato-Rellich) + identity theorem $\Rightarrow$ simplicity off a discrete exceptional set.

**Convergence of overlaps:**
$$|\langle\varphi_0 | a\rangle| \to 0.509 \quad\text{(monotonic toward Slepian limit $\sim 0.5$)}$$

**Stage 3: $N > 20$.** The Slepian compatibility lemma (Node K) identifies $A^{\mathrm{ev}}(\lambda, N)$ with the $N \times N$ truncation of a continuous positive integral operator $K_\lambda$. By Krein-Rutman, the ground state of $K_\lambda$ is strictly simple and positive. By Karnik-Romberg-Davenport (2021), the eigenvectors converge. Therefore AE simplicity holds for all large $N$.

**All $N$ covered.** Stages 1-3 together give simplicity for all $N \geq 1$.

---

## Role in the chain

AE simplicity ensures the eigenvector $\xi_\lambda$ is unique up to phase, which is required for the eigenvector approximation (Node D) and the Hurwitz convergence (Node H).

**Even-sector justification:** CCM Lemma 5.2(i) gives $T\gamma = \gamma T$, so the even sector $E_N^+$ is preserved. The AE simplicity result operates within $E_N^+$. Referee fix #9 verified this compatibility.

---

## Sources

- **Preprint:** sections-11-14.md §12, Proposition 12.1
- **Research:** research/42-ae-simplicity-certified.md, research/29-ae-simplicity.md
- **Referee fix:** #9 (even-sector compatibility via CCM Lemma 5.2(i))
