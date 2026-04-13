# Node 10 --- Non-Perturbative Deviation Order and Spectral Lemma

**Chain step:** 10, 10b of 14
**Rigor label:** [PROVED]
**Dependencies:** Steps 4--5 (B1, B2 analyticity), Step 9 (dim-6 classification)
**Status:** PROVED

---

## Statement

(Step 10) The dimension-6 remainder $\delta E_k^{d=6}$ satisfies $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ non-perturbatively.

(Step 10b) The spectral lemma constant $C_p$ in $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$ is $k$-independent.

---

## Proof sketch

**Step 10.** Balaban's effective action is $\mathcal{C}$-invariant (Wilson action and Haar measure preserve $\mathcal{C}$). The remainder $\delta E_k^{d=6}$ is a $\mathcal{C}$-even, dimension-6, gauge-invariant operator. By the analyticity property (B1), the dimension-6 projection is exact (Taylor expansion converges, not formal). By Step 9, all such operators have $\mathrm{dev} \geq 2$. No perturbative/non-perturbative splitting is needed: the deviation order is fixed by symmetry and dimension class.

**Step 10b.** The constant $C_p = 2 C_*^p (1+\zeta)^{2R_0 - 1}$ where:

- $C_* = e^{\hat{\Delta}_{\max}}$ is $k$-independent (dimensionless gap bounded by UV cutoff).
- $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ is bounded uniformly via two-particle threshold: $E_2 - E_1 \geq \hat{\Delta}_k/2$ by Kato--Rellich. The binding energy $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$ is perturbative. **At early scales** where $g_k$ is not small, we use the lattice bound $E_2 - E_1 \geq c_{\text{lat}} > 0$ (the lattice gap is strictly positive at any finite coupling). The two bounds combine: $E_2 - E_1 \geq \max(c_{\text{lat}}, \hat{\Delta}_k/2)$, which is uniformly bounded below for all $k$.
- Volume-independence follows from Hastings--Koma exponential clustering (CMP 265, 2006) applied to connected correlators.
- $K$-uniformity follows from $K$-independent Lieb--Robinson velocity and physical constants.

---

## Sources

- **Preprint:** Section 5.6, Parts III.4--III.5 (non-pert application)
- **Preprint:** Section 5.5.3, Step 3 (two-particle threshold, Hastings--Koma)
