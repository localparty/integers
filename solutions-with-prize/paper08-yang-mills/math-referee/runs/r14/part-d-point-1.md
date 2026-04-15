## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The Luscher-Weisz basis.** The classification of dimension-6 operators follows Symanzik (1983) and Luscher-Weisz (CMP 97, 1985). In the continuum Symanzik effective theory, the independent $\mathcal{C}$-even, gauge-invariant operators of dimension 6 are:

- $\mathcal{O}_1 = \mathrm{Tr}(D_\rho F_{\mu\nu})^2$ (two-derivative operator)
- $\mathcal{O}_2 = \mathrm{Tr}(D_\mu F^{\mu\rho}\,D_\nu F^\nu{}_\rho)$ (equations-of-motion operator)

The zero-derivative operators ($\mathrm{Tr}(F^3)$, $d^{abc}F^a F^b F^c$) are $\mathcal{C}$-odd and eliminated. One-derivative operators of dimension 5 do not exist in the $\mathcal{C}$-even sector.

The lattice-specific analysis (Appendix J, Theorem J.1) provides a self-contained six-step proof:

1. Zero-derivative dim-6: $\mathrm{Tr}(FFF)$ is $\mathcal{C}$-odd $\implies$ eliminated
2. One-derivative (dim-5): All odd-power traces are $\mathcal{C}$-odd $\implies$ absent
3. Two-derivative dim-6: Survive; form the Luscher-Weisz basis
4. Three-or-more derivatives: Dimension $\geq 7$ $\implies$ not dim-6
5. Lattice-specific O(4)-breaking operators: Share two-derivative structure $\implies$ same $\mathrm{dev} \geq 2$
6. EOM-redundant operators: Absorbed by field redefinition; both independent operators have $\mathrm{dev} \geq 2$

On the lattice, additional operators could arise that vanish in the continuum limit (O(4)-breaking contractions like $\sum_\mu \mathrm{Tr}(D_\mu F_{\mu\nu})^2$ without summation on repeated $\mu$). These are explicitly classified in Step 5 of Appendix J: they have the same two-derivative structure as the continuum operators and therefore the same $\mathrm{dev} \geq 2$.

The Symanzik argument (that lattice-specific operators are redundant by equations of motion) is not merely cited as standard -- it is proved for the specific Wilson lattice action in Appendix J. The proof references Luscher-Weisz (CMP 97, 1985; erratum CMP 98, 1985) and Weisz-Wohlert (Nucl. Phys. B 236, 1984).

**(b) The second two-derivative operator.** The operator $\mathcal{O}_2 = \mathrm{Tr}(D_\mu F^{\mu\rho}\,D_\nu F^\nu{}_\rho)$ is handled in Section 5.6, Part III.3. The proof decomposes $\mathcal{O}_2$ into:

$$\mathcal{O}_2 = \mathcal{O}_1 + [\text{$\mathcal{C}$-odd commutator terms}] + [\text{dim-8 terms}]$$

via the equation of motion $D_\mu F^{\mu\nu} = g[A_\mu, F^{\mu\nu}]$ (which holds as an operator identity, not only on-shell). The $\mathcal{C}$-odd terms vanish in $\mathcal{C}$-even matrix elements. The dim-8 terms have $\mathrm{dev} \geq 2$ (since they have even more derivatives). So $\mathrm{dev}(\mathcal{O}_2) \geq 2$.

The r05 referee initially flagged that $\mathrm{dev} \geq 2$ was verified only for $\mathcal{O}_1$, not for $\mathcal{O}_2$. The current preprint closes this gap via the EOM decomposition above. This is a one-paragraph argument, as noted in the r05 report.

**(c) Lattice artifacts at dimension 6.** The Wilson action introduces $O(a^2)$ lattice artifacts. Under Balaban's block-spin integration, these propagate but are classified by engineering dimension. The key argument: products of $n$ plaquettes at a vertex have leading dimension $4n$. To reach dimension 6 from plaquette products requires $n = 3/2$, which is impossible. Therefore dim-6 operators NECESSARILY involve lattice finite differences (which become covariant derivatives in the continuum).

This structural argument ensures clean separation: dim-4 operators are purely from $S_{\mathrm{YM}}$ (no contamination from dim-6), and dim-6 operators are purely two-derivative (no contamination from dim-4 through operator mixing). Balaban's coupling renormalization, which defines $g_{k+1}$ as the coefficient of $S_{\mathrm{YM}}$, performs an exact subtraction of the unique dim-4 operator (confirmed in PROOF-CHAIN.md IV.3).

**Impact on the claimed result:** None. The dimension-6 classification is exhaustive, both in the continuum (Luscher-Weisz) and on the lattice (Appendix J). The gap flagged by the r05 referee regarding $\mathcal{O}_2$ is closed in the current preprint.
