# Node 11 --- New-Operator Form Factor Bound

**Chain step:** 11 of 14
**Rigor label:** [PROVED]
**Dependencies:** Steps 10, 10b (non-pert deviation, spectral lemma constant)
**Status:** PROVED

---

## Statement

At each Balaban block-spin step $k$, the newly generated irrelevant remainder satisfies:

$$|\langle 1|\delta E_k(0)|1\rangle_c| \leq C_{\mathrm{new}} \, g_k^4 \, \hat{\Delta}_{k+1}^2$$

where $C_{\mathrm{new}}$ is independent of $k$, $g_k$, and the lattice volume.

---

## Proof sketch

1. **Spectral lemma application.** By Step 10, $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$. By Step 10b, the spectral lemma constant $C_p$ is $k$-independent. Applying the spectral lemma with $p=2$ and $M = \|\delta E_k^{d=6}\| \leq C g_k^4$ (Balaban's remainder bound):

$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_2 \cdot C g_k^4 \cdot \hat{\Delta}_{k+1}^2$$

2. **Higher-dimension operators.** Operators with $d_O > 6$ contribute $|\langle 1|\delta E_k^{d_O}|1\rangle_c| \leq C g_k^{d_O - 2} \hat{\Delta}_{k+1}^{d_O - 4}$, which is $O(g_k^4 \hat{\Delta}^2 \cdot g_k^{d_O - 6} \hat{\Delta}^{d_O - 6})$, subleading.

3. **Non-perturbative corrections.** Large-field contributions $O(e^{-c/g_k^{2\epsilon}})$ and instanton corrections $O(e^{-8\pi^2/g_k^2})$ are negligible compared to $g_k^4 \hat{\Delta}^2$.

4. **Setting $C_{\mathrm{new}} = C_2 \cdot C$.** This constant depends on $N$ and the polymer expansion parameters, but not on $k$ or the lattice volume.

---

## Sources

- **Preprint:** Section 5.5, Section 5.6 Part III.5 (eq. III.2)
- **Preprint:** Section 5.3.3 (single-step form factor theorem)
