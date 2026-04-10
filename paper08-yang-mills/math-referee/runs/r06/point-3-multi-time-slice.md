# Point 3: The Multi-Time-Slice Correction and Its Completeness

**Location:** Appendix G, Section 5.3.2, Section 5.5.4

**Verdict:** SOUND

**Finding:**

The paper correctly identifies and corrects a fundamental error in the earlier derivation. The Newton decomposition (rigid operator translation) gives zero in energy eigenstates, not $\hat{\Delta}^2$. The correct mechanism uses the spectral intermediate-state sum for the composite operator $\mathrm{Tr}(D_0 F)^2$. The correction is documented honestly in Appendix G and properly reflected in the current Sections 5.3.2 and 5.5.

---

## (a) Applicability to the full Balaban operator

**Claim under attack:** The spectral mechanism is verified only for $\mathrm{Tr}(D_0 F)^2$ explicitly; its extension to the full non-perturbative $\delta E_k^{d=6}$ relies on the stability lemma, which only establishes $\mathrm{dev} \geq 2$ (not $\mathrm{exc} \geq 2$ in the original sense).

**Finding: SOUND.**

The paper has moved from the original "excitation number" (exc) to "Boltzmann deviation order" (dev), precisely to address this concern. The distinction is stated explicitly in Section 5.5.2:

> "The converse is false: $\mathrm{dev} \geq p$ does not require the absence of low-excitation channels, only that their total weight vanishes to order $p$ at the diagonal."

The stability lemma (Section 5.6, Part III.3) establishes $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ through the operator classification, not through the original Definition 2.1 (excitation number). The spectral lemma (Section 5.5.3) uses $\mathrm{dev} \geq p$ as its hypothesis, not $\mathrm{exc} \geq p$.

The logical chain is self-consistent:
1. Classification: every $\mathcal{C}$-even dimension-6 operator has $\mathrm{dev} \geq 2$.
2. (B1): $\delta E_k^{d=6}$ is a convergent sum of such operators.
3. Linear combination lemma: the sum inherits $\mathrm{dev} \geq 2$.
4. Spectral lemma: $\mathrm{dev} \geq 2$ implies $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_2 M \hat{\Delta}^2$.

No step requires verifying Definition 2.1 for the non-perturbative operator. The deviation order is the correct notion throughout.

---

## (b) The vacuum intermediate vs. all channels

**Claim under attack:** Channels with $\#(\mathbf{n}) = 1$ must all be absent for the spectral lemma to give $O(\hat{\Delta}^2)$.

**Finding: SOUND.**

This concern is based on the original excitation number definition, which required the ABSENCE of low-excitation channels. The revised notion (Boltzmann deviation order) does NOT require their absence.

For $\mathrm{Tr}(D_0 F)^2$ with $R = 1$, the $n_1 = 0$ (vacuum intermediate) channel is present and has nonzero weight. But the weight factor $(e^{E_m - E_0} - 1)^2$ provides TWO vanishing powers at the diagonal. Specifically:

- For $m = 1$: $(e^{\hat{\Delta}} - 1)^2 = \hat{\Delta}^2(1 + O(\hat{\Delta}))$. Nonzero, but $O(\hat{\Delta}^2)$.
- For $m = 0$: $(e^0 - 1)^2 = 0$. Zero.

The $n_1 = 1$ channel contributes $(e^{E_1 - E_1} - 1)^2 = 0$ for $m = 1$. Higher channels $n_1 \geq 2$ are exponentially suppressed.

The spectral lemma bounds the TOTAL contribution, not individual channels. With $\mathrm{dev} \geq 2$, the total is $O(M\hat{\Delta}^2)$ regardless of which channels are present, because the deviation factors are extracted from the weight before summing.

---

## (c) The corrected mechanism vs. the Newton decomposition

**Claim under attack:** The identification of the non-perturbative operator with $\mathrm{Tr}(DF)^2$ is not made rigorous.

**Finding: SOUND.**

The paper makes this identification rigorous in Section 5.6, Part III.3--III.4, through the operator classification. The argument does NOT require identifying $\delta E_k^{d=6}$ with $\mathrm{Tr}(DF)^2$ at the level of individual matrix elements. Instead:

1. **Classification:** Every $\mathcal{C}$-even dimension-6 gauge-invariant operator is either (a) a two-derivative operator with the spectral structure of $\mathrm{Tr}(DF)^2$, giving $\mathrm{dev} \geq 2$, or (b) a three-or-more derivative operator with $\mathrm{dev} \geq 3$.

2. **Convergent expansion:** By (B1), $\delta E_k^{d=6}$ is a convergent sum of such operators (each monomial in the polymer expansion is a gauge-invariant lattice operator whose dimension-6 part falls into the classification).

3. **Linear combination lemma:** The convergent sum inherits $\mathrm{dev} \geq 2$.

The "inheritance" is at the level of the deviation order (a structural property), not at the level of numerical identification. The non-perturbative operator need not be "close" to $\mathrm{Tr}(DF)^2$; it need only be a $\mathcal{C}$-even dimension-6 gauge-invariant operator (which it is, by construction).

The EOM-related operator $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^{\nu}{}_\rho)$ is handled in Section 5.6, Part III.3 by the Bianchi identity decomposition: it equals $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ plus $\mathcal{C}$-odd commutator terms (which vanish in the effective action) plus higher-dimension lattice artifacts ($O(a^2)$, hence $\mathrm{dev} \geq 4$).

---

**Impact on the claimed result:** None. The multi-time-slice mechanism is correctly handled. The revision from Newton decomposition to spectral intermediate-state mechanism is sound, and the extension to the non-perturbative operator is achieved through the operator classification, not through a perturbative identification.
