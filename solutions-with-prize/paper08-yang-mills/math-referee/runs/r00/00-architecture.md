# Proof of the Yang-Mills Mass Gap: Architecture

## Structure

The proof has two parts and one conditional step.

**Part 1 (Proved): Lattice mass gap.**
The KK cluster expansion proves $\Delta_0 > 0$ at the starting
lattice spacing $a_0$, for all practical couplings $\beta < 10^{14}$.

**Part 2 (Proved): Balaban's UV stability.**
Balaban's renormalization group controls the effective action at
each RG step, with irrelevant operator coefficients bounded by
$O(g_k^4)$.

**Part 3 (Proved): RG preservation mechanism.**
The RG recursion $C_{k+1} = C_k/4 + C_{\text{new}} + O(g_k^2 C_k)$
has a stable fixed point. The contraction factor $1/4$ prevents
blow-up. The continuum limit reduces to bounding $C_{\text{new}}$
at a single block-spin step.

**Part 4 (Proved): Dimension-6 operator analysis.**
All dimension-6 operators are classified. Non-derivative operators
($\mathrm{Tr}\,F^3$, $d^{abc}F^3$) vanish exactly by charge
conjugation symmetry. The derivative operator $\mathrm{Tr}(DF)^2$
has form factor $O(\hat{\Delta}^2)$ by translation invariance +
spectral gap — two exact, non-perturbative mechanisms.

**Conditional Step: The continuum limit.**
If the non-perturbative single-step form factor bound holds at
$d_O = 6$ (Conjecture 1), then $\Delta_\infty > 0$.


---

## Status Table

| Result | Status | Section |
|:-------|:-------|:--------|
| Weitzenboeck gap: $\mu_1 \geq 6/r_3^2$ | **Theorem 1** | 02 |
| Bond activity bound: $\|g_b\| \leq C_0 e^{-m_1 a}$ | **Theorem 2** | 03 |
| Cluster expansion convergence | **Theorem 3** | 03 |
| Lattice mass gap: $\Delta_0 > 0$ | **Theorem 4** | 04 |
| IR equivalence: $\sigma_{\text{std}} = \sigma_{\text{KK}} + O(e^{-m_1 a})$ | **Theorem 5** | 05 |
| Balaban: effective action bounded, coupling renormalized | **Literature** | 06 |
| Parity vanishing: $\nabla_q \hat{E}_k(0) = 0$ | **Theorem 6(a)** | 07 |
| Operator identity $\hat{E}_k(0) = 0$ | **False** (disproved) | 07 |
| RG preservation: contraction $C_{k+1} = C_k/4 + C_{\text{new}}$ | **Proved** | rg-pres. |
| $\mathrm{Tr}(F^3)$, $d^{abc}F^3$: coefficient and form factor | **Exactly 0** (C-symmetry) | case-b |
| $\mathrm{Tr}(DF)^2$: form factor $O(\hat{\Delta}^2)$ | **Proved** (exact mechanisms) | single-step |
| Form factor bound (perturbative, all orders) | **Theorem 7** | 08 |
| Non-perturbative small-field bound at $d_O = 6$ | **Conjecture 1** | 08 |
| Continuum mass gap: $\Delta_\infty > 0$ | **Theorem 8** (conditional on Conj. 1) | 09 |


---

## The Proof Chain

```
Weitzenboeck gap (Thm 1)
    |
    v
Bond activity bound (Thm 2)
    |
    v
Kotecky-Preiss convergence (Thm 3)
    |
    v
Lattice mass gap Delta_0 > 0 (Thm 4) --------+
    |                                          |
    v                                          |
IR equivalence (Thm 5):                        |
  standard YM has same gap                     |
                                               |
Balaban's RG (Literature) ---------------------+
    |                                          |
    v                                          |
Dimension-6 operator classification:           |
  Tr(F^3) = 0 exactly (C-symmetry)            |
  Tr(DF)^2: two exact suppression mechanisms   |
    - spatial D_rho |1> = 0 (translation inv)  |
    - temporal D_0 |1> = hat{Delta} (spectral) |
    |                                          |
    v                                          |
RG preservation (contraction 1/4 per step)     |
    |                                          |
    v                                          |
Single-step bound: C_new at one block-spin     |
  Perturbative: O(g_k^4 hat{Delta}^2) [PROVED]|
  Non-perturbative small-field [CONJECTURE 1]  |
    |                                          |
    v                                          |
Continuum mass gap (Thm 8, conditional) <------+
  Delta_infty > 0
```


---

## Conjecture 1 — The Precisely Identified Remaining Problem

**Statement.** At a single block-spin step in Balaban's RG, the
newly generated dimension-6 irrelevant remainder satisfies:

$$\bigl|\langle 1 \,|\, \delta E_k(0) \,|\, 1 \rangle_c\bigr|
  \;\leq\; C_{\text{new}}\,g_k^4\,\hat{\Delta}_k^2$$

non-perturbatively in the small-field region, where $C_{\text{new}}$
is independent of $k$, $g_k$, and the volume.

**What is proved:**
- The bound holds perturbatively to all orders in $g_k$ (Theorem 7)
- The $\hat{\Delta}^2$ arises from two exact mechanisms that are
  non-perturbative (translation invariance + spectral gap)
- Non-derivative operators ($\mathrm{Tr}\,F^3$) are eliminated exactly
  by charge conjugation
- Non-perturbative corrections from large-field configurations and
  instantons are exponentially suppressed

**What is open:**
- Whether Balaban's small-field resummation (which reorganizes the
  fluctuation integral into a convergent polymer expansion) preserves
  the derivative structure that produces $\hat{\Delta}^2$
- This is a verification within Balaban's existing framework, not a
  new conceptual problem

**If Conjecture 1 holds:** The RG recursion closes with stable fixed
point $C_* = (4/3)\,C_{\text{new}}$, the sum
$\sum_k g_k^4 \hat{\Delta}_k^2$ converges, and $\Delta_\infty > 0$.


---

## Files

| File | Contents |
|:-----|:---------|
| **Core proof (Sections 00-10)** | |
| 00-architecture.md | This file |
| 01-setup.md | Mathematical setup: lattice, KK enhancement, action |
| 02-spectral-gap.md | Theorem 1: Weitzenboeck spectral gap |
| 03-cluster-expansion.md | Theorems 2-3: bond activities + convergence |
| 04-lattice-mass-gap.md | Theorem 4: $\Delta_0 > 0$ (the main proved result) |
| 05-decoupling.md | Theorem 5: IR equivalence with standard YM |
| 06-balaban-descent.md | Balaban's RG: what we use from the literature |
| 07-power-counting.md | Theorem 6: parity proved, operator identity disproved |
| 08-form-factor.md | Theorem 7 + Conjecture 1: the form factor bound |
| 09-continuum-limit.md | Theorem 8: $\Delta_\infty > 0$ (conditional) |
| 10-open-problem.md | The remaining problem and paths to resolution |
| **Continuum limit investigation** | |
| the-zero-mode-lemma.md | Definitive: operator identity is false; correct target identified |
| rg-preservation.md | RG recursion with $1/4$ contraction; reduces to single step |
| single-step-computation.md | $\mathrm{Tr}(DF)^2$: exact suppression mechanisms |
| single-step-case-b.md | $\mathrm{Tr}(F^3)$: eliminated by charge conjugation |
| **Path investigations** | |
| path-1-balaban-three-point.md | Extending Balaban's cluster expansion to 3-point functions |
| path-1a-integration-by-parts.md | Lattice IBP on polymers |
| path-1b-operator-decomposition.md | Operator basis and derivative structure |
| path-2-spectral-perturbation.md | Dimension-sensitive spectral perturbation theorem |
| path-2a-regularity-estimate.md | Regularity estimate for connected kernel |
