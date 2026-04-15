# Node 16 -- Continuum Flowed Schwinger Functions

**Chain step:** 16 of 18
**Rigor label:** [PROVED]
**Dependencies:** Step 15 (gradient flow), Step 14 ($\Delta_\infty > 0$)
**Status:** PROVED (Lemmas L.2.1--L.2.4)

---

## Statement

**Lemmas L.2.1--L.2.4 (Continuum flowed limit).** *At fixed flow time $t > 0$, the flowed Schwinger functions converge to a unique continuum limit (not merely subsequential) satisfying the Osterwalder--Schrader axioms OS0--OS4:*

*(i) Convergence (L.2.1--L.2.2): the lattice flowed Schwinger functions $S_{n,t}^{(K)}$ converge as $K \to \infty$, with doubly exponential rate inherited from Step 13.*

*(ii) Uniqueness (L.2.3): the limit is unique by a Cauchy argument --- the $K$-uniform Lipschitz bound from L.1.4 upgrades subsequential convergence to full convergence.*

*(iii) OS axioms (L.2.4): the limiting flowed Schwinger functions at fixed $t > 0$ satisfy OS0 (temperedness), OS1 (Euclidean invariance), OS2 (reflection positivity), OS3 (symmetry), OS4 (cluster decomposition).*

---

## Proof sketch

**L.2.1--L.2.2 (Convergence).** The flowed $n$-point function at lattice spacing $a_0(K)$ satisfies $|S_{n,t}^{(K+1)} - S_{n,t}^{(K)}| \leq C_n g_K^4 (a_0(K)\Lambda)^s$. By Step 13, the telescoping sum converges. The flow-time smearing $\sqrt{8t}$ provides a natural UV cutoff, ensuring all estimates are uniform in $K$.

**L.2.3 (Uniqueness).** The $K$-uniform Lipschitz constant in flow time (Lemma L.1.4) and the Moore--Osgood theorem give uniqueness of the double limit $(K \to \infty, t > 0)$ without subsequence extraction.

**L.2.4 (OS axioms).** Each axiom verified by taking the $K \to \infty$ limit of the corresponding lattice property:
- **OS0 (temperedness):** From polymer-decay bounds (uniform in $K$).
- **OS1 (Euclidean invariance):** From the isometry of the continuum action (lattice $H(4)$ symmetry upgrades to $O(4)$ in the limit).
- **OS2 (reflection positivity):** The lattice OS inequality $\sum_{i,j} \bar{c}_i c_j S(\theta f_i, f_j) \geq 0$ holds at each $K$. Since the Schwinger functions converge pointwise and the inequality is closed under pointwise limits, RP survives. **Note:** This uses that the convergence is of measures (not just correlation functions) in the appropriate topology — guaranteed by the polymer-decay uniform bounds providing tightness.
- **OS3 (symmetry):** Permutation symmetry of the measure.
- **OS4 (cluster decomposition):** From $\Delta_\infty > 0$ (the mass gap provides exponential decay of connected correlators at separation $\geq 1/\Delta_\infty$).

---

## Key point

The flow-time regularization at $t > 0$ makes all composites UV-finite (Luscher--Weisz), so the continuum limit exists without additional renormalization. The $t \to 0^+$ limit is handled in Steps 17--18.

---

## Sources

- **Preprint:** Appendix L, Section L.2
- **Proof chain:** PROOF-CHAIN.md, Step 16
