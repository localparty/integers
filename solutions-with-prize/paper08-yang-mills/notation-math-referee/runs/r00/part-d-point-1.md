## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** SOUND (the second two-derivative operator is now explicitly verified, addressing the prior r05 closable gap)

**Finding:**

(a) **The Lüscher–Weisz basis.** The continuum dimension-6 basis after $\mathcal{C}$-elimination contains only the two-derivative operators
$$\mathcal{O}_1 = \mathrm{Tr}(D_\rho F_{\mu\nu})^2, \qquad \mathcal{O}_2 = \mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$$
related by the YM equations of motion modulo $\mathrm{Tr}(F^3)$ commutators (which are $\mathcal{C}$-odd and absent in the $\mathcal{C}$-invariant effective action). This is standard Symanzik (1983)/Lüscher–Weisz (1985) and is correct.

The lattice-specific classification is given in **Appendix J** ("Lattice Symanzik basis") and **Appendix I.2**. The argument is the standard one: any lattice operator built from products of plaquette variables admits a Symanzik expansion in continuum operators of increasing dimension; the leading terms are dimension 0 (vacuum energy), dimension 4 ($S_{\mathrm{YM}}$, absorbed into coupling renormalization), and dimension 6 (the Lüscher–Weisz basis). Lattice-specific operators (e.g., $\hat\nabla^2 - D^2$) are dimension 8 or higher.

(b) **The second two-derivative operator $\mathcal{O}_2$.** Section 5.6 Part III.3 paragraph "The second two-derivative operator" gives an explicit spectral verification:
$$\mathcal{O}_2 = \sum_\rho (\sum_\mu D_\mu F^{\mu\rho})(\sum_\nu D_\nu F^{\nu\rho})$$
The spatial components ($\mu = j$) contribute zero in the zero-momentum state by translation invariance, and the temporal component ($\mu = 0$) gives $D_0 F^{0\rho} \to (e^{E_m - E_n} - 1)$, which gives a *squared* deviation factor in the product of two $D$ insertions. Therefore $\mathrm{dev}(\mathcal{O}_2) \geq 2$ by direct spectral verification.

This addresses the gap flagged in r05 Point 1(d): the second two-derivative operator's dev is now verified explicitly, not just by appeal to equations of motion. Sound.

(c) **Lattice artifacts at dimension 6.** The Wilson action's $O(a^2)$ artifacts are dimension-6 corrections by the standard Symanzik counting. They contribute to $\delta E_k^{d=6}$ as part of the irrelevant remainder. The classification handles these because they are gauge-invariant, $\mathcal{C}$-even, and dimension-6 — i.e., they fall into the same Lüscher–Weisz basis. There is no operator mixing into dimension 4 because $S_{\mathrm{YM}}$ is the unique dimension-4 $\mathcal{C}$-even gauge-invariant operator (Appendix I.2 verifies this).

A subtle point that the preprint addresses correctly: products of plaquettes at the same site ($s_P^2$, $s_P^3$, ...) have *leading* terms at dimensions $0, 4, 8, 12, \ldots$ (from $s_P \sim a^4 \mathrm{Tr}\,F^2$), *not* at dimension 6. So they do not produce zero-derivative dim-6 contributions that would evade the $\mathcal{C}$-elimination. This was a concern in r05 and is addressed in I.2 Step 3.

**Impact on the claimed result:** Sound. The classification is exhaustive and the dim-6 part of the effective action satisfies $\mathrm{dev} \geq 2$ as a structural property of the operator class.
