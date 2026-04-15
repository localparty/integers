# Point 2: The Spectral Lemma -- Step 5 (Exponential to Polynomial)

**Location:** Section 5.5.3, Steps 1--4 (the revised proof has no separate Step 5)

**Verdict:** CLOSABLE GAP (for sub-point (c)); SOUND (for (a) and (b))

**Finding:**

The revised proof (Section 5.5.3) no longer contains a separate "Step 5" for converting exponential to polynomial bounds. The polynomial bound $\hat{\Delta}^p$ now emerges directly from Step 1 (deviation extraction), where $p$ factors of $(e^{E_m - E_{n_j}} - 1)$ are extracted from the spectral weight, each bounded by $C\hat{\Delta}$. The proof is cleaner and more direct than the earlier version.

---

## (a) The general case

**Claim under attack:** For general multi-time-slice operators with $\mathrm{dev} \geq p$, cross terms between different excitations in different time slots might contribute $O(\hat{\Delta}^{p-1})$.

**Finding: SOUND.**

The revised definition of Boltzmann deviation order (Definition D.2, Section 5.5.2) handles the general case precisely. The definition requires:

> The total weight $W_\alpha^{(m)}(\mathbf{n}) \cdot e^{-E(\mathbf{n})}$, viewed as a function of the energy differences $\delta_j = E_m - E_{n_j}$, vanishes to order $\geq p$ at the diagonal $\delta_j = 0$ for all $j$ simultaneously.

This means $p$ powers of $(e^{E_m - E_{n_j}} - 1)$ can be factored out from the weight, with bounded residual. The $p$ factors may be distributed across different slots; what matters is the total vanishing order.

The cross terms are handled by the summation in Step 3. After extracting $p$ deviation factors (each bounded by $C\hat{\Delta}$), the remaining sum over intermediate states is controlled by the residual weight and the completeness relation:

$$\sum_{n_j} |\tilde{W}| \cdot e^{-\max(E_{n_j} - E_1, 0)} \leq \|\hat{A}^{(s)}\| \cdot (1 + \zeta)$$

The cross terms between different excitations cannot produce $O(\hat{\Delta}^{p-1})$ because the factorization (D.2) has already extracted $p$ deviation powers. The residual $\tilde{W}$ is bounded uniformly, and the remaining Boltzmann factors are $O(1)$ (they can only contribute additional suppression, not enhancement).

---

## (b) The baseline

**Claim under attack:** Double-counting between the vacuum subtraction (connected part) and the "deviation" argument.

**Finding: SOUND.**

There is no double-counting. The proof bounds $|\langle m|\mathcal{O}|m\rangle|$ for each $m \in \{0, 1\}$ separately (Step 3, bound (S3.1)), and then uses the triangle inequality:

$$|\langle 1|\mathcal{O}|1\rangle_c| = |\langle 1|\mathcal{O}|1\rangle - \langle 0|\mathcal{O}|0\rangle| \leq |\langle 1|\mathcal{O}|1\rangle| + |\langle 0|\mathcal{O}|0\rangle|$$

The deviation structure is used once, in Step 1, to extract $p$ powers of $\hat{\Delta}$ from the spectral weight. The vacuum subtraction is a separate operation in Step 4. The "baseline" in the deviation structure refers to the diagonal configuration $\mathbf{n} = (m, \ldots, m)$ in the spectral sum -- this is NOT the vacuum subtraction. The deviation from the diagonal gives $\hat{\Delta}^p$; the vacuum subtraction gives the connected part. These are independent operations acting on different aspects of the spectral sum.

---

## (c) The bound $C_p$

**Claim under attack:** The factor $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ could diverge if the spectral gap above $E_1$ closes.

**Finding: CLOSABLE GAP.**

The bound $C_p = 2(1+\zeta)^{2R-1}(C\hat{\Delta})^p$ involves $\zeta$, which depends on the spectral gap $E_2 - E_1$ above the one-particle state. The paper states (Section 5.5.3, Step 3):

> "By locality (hypothesis (ii)), $\zeta$ is bounded by a constant $\zeta(R_0, N)$ independent of the volume (using the cluster property in the gapped phase)."

This statement is correct but incomplete. The argument requires:

1. **$E_2 - E_1 > 0$** at each RG step $k$. In a confining gauge theory, the two-particle threshold is at approximately $2\Delta$ (for non-interacting glueballs), giving $E_2 - E_1 \geq \Delta > 0$. The spectral gap above $E_1$ is bounded below by the mass gap itself.

2. **$\zeta$ is $k$-independent.** For a local operator with support radius $R_0$, the number of states contributing significantly to the spectral sum is bounded by the local degrees of freedom (depending on $R_0$ and $N$). The cluster property in the gapped phase ensures that $\zeta$ does not grow with the volume.

**What is missing:** The paper does not explicitly state that $E_2 - E_1 \geq c\Delta > 0$ is maintained throughout the RG flow, or that the spectral density above $E_1$ is controlled. The required argument is short: in the weak-coupling regime where Balaban's framework applies, the spectrum is perturbatively controlled, and the two-particle threshold $E_2 \approx 2E_1$ gives $E_2 - E_1 \approx E_1 = \Delta > 0$. Binding-energy corrections are $O(g_k^2 \Delta)$, which shift $E_2 - E_1$ by a relative $O(g_k^2)$ -- this does not close the gap.

**Closing the gap requires:** A one-paragraph argument stating that $E_2 - E_1 \geq c\Delta_k > 0$ (with $c$ independent of $k$) follows from the perturbative spectrum in Balaban's small-field domain, plus the inductive hypothesis $\Delta_k > 0$.

**UPDATE:** This gap has been closed. Section 5.5.3, Step 3 now contains an explicit argument establishing: (i) volume independence of $\zeta$ via the Combes--Thomas estimate and locality, and (ii) $k$-independence via the two-particle threshold bound $E_2 - E_1 \geq \hat{\Delta}_k(1 - C_B g_k^4) \geq \hat{\Delta}_k/2$ in the weak-coupling regime.

---

**Impact on the claimed result:** Sub-point (c) identifies a gap in the argument for the $k$-independence of $C_p$. This gap does NOT invalidate the main claim $\Delta_\infty > 0$: the required bound on $E_2 - E_1$ follows from standard spectral theory in the gapped phase and can be closed with a short additional argument. The convergence of $\sum C_k g_k^4 \hat{\Delta}_k^2$ is robust to polynomial growth in $C_p$ (the doubly exponential $4^{-k}$ factor overwhelms any polynomial).
