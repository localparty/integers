# Node 01 --- KK Spectral Gap

**Chain step:** 1 of 18
**Rigor label:** [PROVED] (Theorem 4)
**Dependencies:** None (base case)
**Status:** PROVED

---

## Statement

**Theorem 4.** For $\mathrm{SU}(N)$ lattice gauge theory on $\Lambda_L$ enhanced with $\mathbb{CP}^{N-1}$ harmonics in the $k=0$ sector, with $r_3/a < \sqrt{3/(4N)}$ and $\beta < \beta_{\max}(a) \equiv m_1 a/6 - \ln(c_d K C_0^{1/6})$:

$$\Delta_0^{\mathrm{KK}} \;\geq\; \alpha/a \;>\; 0$$

where $\alpha$ is the Kotecky--Preiss exponential weight and $m_1 = 2\sqrt{N}/r_3$ is the lightest KK mass.

---

## Proof sketch

1. **Weitzenbock spectral gap (Thm 1).** The Hodge Laplacian on 1-forms on $\mathbb{CP}^{N-1}$ satisfies $\Delta_{\mathrm{Hodge}} \geq 2N/r_3^2$ (Weitzenbock + Einstein metric $R_{ab} = (2N/r_3^2)g_{ab}$, plus $b_1 = 0$). This gives KK mass $m_1 = \sqrt{\lambda_1^{(1)}}/r_3 \geq 2\sqrt{N}/r_3$.

2. **Bond activity bound (Thm 2).** In the $k=0$ sector, the integrated bond activity satisfies $|g_b| \leq C_0 e^{-m_1 a}$, via the lattice propagator transfer-matrix representation and Weyl-law summation over KK modes.

3. **Cluster convergence (Thm 3).** The Kotecky--Preiss criterion is met when $2\beta + \alpha < m_1 a/6 - \ln(c_d K C_0^{1/6})$. At physical values ($a/r_3 \sim 10^{15}$), this holds by a factor $\sim 10^{13}$.

4. **Mass gap.** Convergent cluster expansion + reflection positivity (Lemma D.2) gives exponential decay of connected correlators at rate $m \geq \alpha/a > 0$, uniformly in volume.

---

## Sources

- **Preprint:** Section 4 (Theorems 1--4), Appendix D (reflection positivity)
- **Literature:** Kotecky--Preiss 1986, Osterwalder--Seiler 1978, Luscher 1977
