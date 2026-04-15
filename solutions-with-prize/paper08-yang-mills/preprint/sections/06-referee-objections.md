# Section 6: Addressing Technical Objections

Seven specific technical objections were raised during the mathematical review of this proof. We address each one, stating the objection, its resolution status, and where the resolution appears.

---

## Objection A: Vacuum Subtraction

**The objection.** Step 2 of the continuum limit argument claims that $\hat{E}_k(0) = \sum_x E_k(x) = 0$ as an operator identity, asserting that the spatial integral of the irrelevant remainder $E_k$ vanishes on every gauge field configuration. However, Balaban's decomposition subtracts the vacuum energy as a field-independent constant $\mathcal{E}_0 \cdot V$, which ensures only the vacuum expectation $\langle 0|\hat{E}_k(0)|0\rangle = 0$. This is categorically different from the operator identity the proof requires; without it, the Taylor bound loses one power of $|q|$, degrading the suppression from $(a\Lambda)^4$ to $(a\Lambda)^2$.

**Resolution status:** RESOLVED

**Where resolved:** The operator identity $\hat{E}_k(0) = 0$ was disproved (Section 5.2). The correct mechanism uses the spectral intermediate-state decomposition (Section 5.5), bypassing the operator identity entirely.

---

## Objection B: Parity of $E_k$

**The objection.** Step 3 asserts that $\partial_\mu \hat{E}_k(0) = i\sum_x x_\mu E_k(x) = 0$ because $E_k$ is parity-even under $\mathcal{P}_\mu: x_\mu \to -x_\mu$. The concern is that Balaban's block-spin transformation involves gauge-fixing and averaging procedures that might break parity, even if the original Wilson action is parity-symmetric. If parity is broken at any RG step, the vanishing of the first moment fails and the Taylor bound loses an additional power of $|q|$.

**Resolution status:** RESOLVED

**Where resolved:** Theorem 6(a) in Section 5.2 proves parity vanishing exactly.

---

## Objection C: Locality and Support Radius

**The objection.** Step 4 uses a Taylor bound involving a Hessian constant $C_{\text{Hess}} = C g_k^4 \times R_O^2 \times |B_{R_O}|$ that depends on the support radius $R_O$ of $E_k(x)$. Since $E_k$ lives on the block lattice of spacing $L^k a_0$, the concern is that $R_O$ grows as $L^k$ in original lattice units, causing the Hessian constant to diverge exponentially with $k$ and invalidating the Taylor bound. The key question is whether the support radius is measured in original lattice units (where it grows) or block lattice units (where it is constant).

**Resolution status:** RESOLVED

**Where resolved:** Section 5.6, Part I, Step (c) confirms $R_O$ is $O(1)$ in block lattice units with $k$-independent bounds from Balaban's polymer expansion.

---

## Objection D: Momentum-Space Convolution

**The objection.** Step 6 bounds the connected self-energy using a momentum-space convolution formula. This approach has three independent flaws: (1) translation invariance makes the connected matrix element $\langle 1|E_k(x)|1\rangle_c$ constant in $x$ for a zero-momentum state, eliminating any momentum-space structure to exploit; (2) the one-particle wave function has power-law (Lorentzian) tails in momentum space, invalidating the sharp support assumption $\|\tilde{\psi}\|_1^2 \leq \hat{\Delta}^3$; and (3) the proof conflates the particle's spatial momentum (sharp at $p=0$) with the glueball's internal structure. Without the form factor bound, neither the spectral perturbation bound nor the clustering bound gives a convergent sum for the continuum limit.

**Resolution status:** RESOLVED

**Where resolved:** The flawed momentum-space convolution was replaced by the spectral intermediate-state mechanism (Section 5.5, Appendix G). The $\hat{\Delta}^2$ suppression comes from the vacuum intermediate state in the composite operator, not from momentum-space wave function support.

---

## Objection E: First-Order Perturbation Theory

**The objection.** Step 7 uses first-order perturbation theory to relate the coefficient change $\delta c$ (bounded by $C g_k^4$ from Balaban) to the mass gap shift. At the first few RG steps ($k = 0, 1, 2$), the coupling $g_k^2$ is $O(1)$ or larger, and $g_k^4 \geq 0.1$, so first-order perturbation theory is not justified a priori. The ratio of the perturbation to the spectral gap is $O(1)$ at these early steps, meaning the first-order formula may have $O(1)$ corrections.

**Resolution status:** RESOLVED

**Where resolved:** Section 5.4 shows the RG recursion has a 1/4 contraction factor that absorbs $O(1)$ corrections at the first few steps.

---

## Objection F: Inductive Stability

**The objection.** The proof tracks $|\delta\hat{\Delta}_k|/\hat{\Delta}_k \leq C' g_k^4 (a_k\Lambda)^4$ at each step and sums. The form factor bound in Step 6 depends on $\hat{\Delta}_k$ (the current mass gap), creating a potential feedback loop: if $\hat{\Delta}$ decreases, the form factor bound weakens, allowing further decrease. The concern is whether a self-reinforcing downward spiral could drive the mass gap to zero in finitely many steps, and whether establishing a uniform lower bound requires circular reasoning.

**Resolution status:** RESOLVED

**Where resolved:** Section 5.4 proves the recursion $C_{k+1} = C_k/4 + C_{\text{new}}$ has a stable fixed point. Section 5.6 Part III proves the stability of deviation order.

---

## Objection G: Balaban Applicability to KK Theory

**The objection.** Balaban 1987 proves the bound $\|E_k(x)\| \leq C g_k^4$ per lattice site for pure $SU(N)$ Yang-Mills on a 4D lattice. The proof here uses a KK-enhanced theory on $M^4 \times \mathbb{CP}^{N-1}$ with additional KK mode fields. While the KK modes are ultra-heavy ($m_1 a \sim 10^{15}$) at all physically relevant lattice spacings, verifying that the effective 4D action from the cluster expansion satisfies Balaban's input requirements requires an explicit check. Additionally, the crossover regime ($a \sim r_3$) where Balaban does not apply and the theory becomes effectively higher-dimensional requires a separate argument.

**Resolution status:** [CONFIRMED] -- See verification report (`preprint-verification/verify-balaban-items.md`) and Appendix H for explicit confirmation of all three Balaban analyticity properties.

**Where resolved:** Sections 5.6, Parts I-II extract (B1)-(B2) from Balaban's published work. Three reading exercises remain (Appendix H).

---
