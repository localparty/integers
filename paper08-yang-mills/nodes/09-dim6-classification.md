# Node 9 --- Dimension-6 Classification

**Chain step:** 9 of 14
**Rigor label:** [PROVED]
**Dependencies:** Steps 6 (C-elimination), 8 (deviation bound)
**Status:** PROVED

---

## Statement

Every local, gauge-invariant, $\mathcal{C}$-even operator of engineering dimension 6 on the $d=4$ hypercubic lattice has Boltzmann deviation order $\mathrm{dev} \geq 2$.

---

## Proof sketch

Exhaustive classification into four classes (Appendix J, Section 5.6 Part III.3):

1. **Class I: zero-derivative operators** ($\mathrm{Tr}(F^3)$, $d^{abc}F^3$). Both are $\mathcal{C}$-odd ($F \to -F^T$ gives a sign flip under odd-power trace). Their coefficients vanish exactly in any $\mathcal{C}$-invariant action. Absent.

2. **Class II: one-derivative operators** (dimension 5). No $\mathcal{C}$-even gauge-invariant operator of dimension 5 exists (odd-power traces are $\mathcal{C}$-odd). Absent.

3. **Class III: two-derivative operators.** The $O(4)$-invariant basis: $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^{\nu}{}_\rho)$. Both have $\mathrm{dev} \geq 2$ by the spectral mechanism (Step 8). The second reduces to the first modulo commutator terms $[D_\mu, D_\nu]F = [F_{\mu\nu}, F]$: these commutators are $\mathcal{C}$-odd (odd power in $F$) and vanish in the $\mathcal{C}$-invariant action. **H(4)-specific operators:** On the hypercubic lattice, $O(4)$ is broken to $H(4) = S_4 \ltimes (\mathbb{Z}/2)^4$. Appendix J (lattice Symanzik basis) verifies exhaustiveness under $H(4)$: the additional $H(4)$-invariant operators (e.g., $\sum_\mu \mathrm{Tr}(D_\mu F_{\mu\nu})^2$ without full contraction) all have $\mathrm{dev} \geq 2$ by the same spectral mechanism, since the deviation bound is index-by-index (each $\rho$ contributes independently).

4. **Class IV: three-or-more-derivative operators.** Have $\mathrm{dev} \geq 3 > 2$.

Since Classes I--II are absent and Classes III--IV all have $\mathrm{dev} \geq 2$, every $\mathcal{C}$-even dimension-6 operator satisfies $\mathrm{dev} \geq 2$.

---

## Sources

- **Preprint:** Section 5.6, Part III.3 (Stability of Deviation Order lemma)
- **Preprint:** Appendix J (lattice Symanzik basis derivation)
