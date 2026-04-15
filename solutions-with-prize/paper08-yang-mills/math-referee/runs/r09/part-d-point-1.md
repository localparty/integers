## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The Lüscher-Weisz basis.** The classification of dimension-6 gauge-invariant operators coincides with the Lüscher-Weisz (1985) operator basis. In the continuum Symanzik effective theory, this basis is well-established: every gauge-invariant, $\mathcal{C}$-even operator of engineering dimension 6 is either:
- (I) $\mathrm{Tr}(F^3)$ or $d^{abc}F^3$ — $\mathcal{C}$-odd, eliminated.
- (II) Dimension-5 — absent (no $\mathcal{C}$-even gauge-invariant operator of odd dimension).
- (III) $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and EOM-equivalent variants — two-derivative, dev $\geq 2$.
- (IV) Three-or-more derivative operators — dev $\geq 3$.

On the lattice, the concern is whether additional operators could arise that are absent in the continuum. The standard Symanzik argument (Symanzik 1983) is that such operators are either: (i) redundant by the equations of motion, (ii) related by lattice identities to continuum-basis operators, or (iii) of higher dimension in the continuum expansion.

The specific concern about $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^3$ is addressed correctly by the r05 referee: this operator has continuum expansion $1 - (3a^4/2N)\mathrm{Tr}(F^2) + O(a^8)$. The leading term is dimension 0, the next is dimension 4 (proportional to $S_{\mathrm{YM}}$), and the dimension-6 contribution is $O(a^{12})$. It does NOT contaminate the dimension-6 sector.

**The gap:** The preprint implicitly uses the continuum classification without providing a lattice-specific derivation. This is standard material (Symanzik 1983, Lüscher-Weisz 1985), but for a Millennium Prize paper, a self-contained lattice-specific proof would be appropriate.

**Status update:** Appendix J provides the self-contained lattice derivation, with Theorem J.1 establishing the complete classification. Steps 1-6 cover zero-derivative, one-derivative, two-derivative, higher-derivative, lattice-specific, and redundant operators. This gap is **CLOSED**.

**(b) The second two-derivative operator.** The operator $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ is related to $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ by the Bianchi identity and commutator relations. Section 5.6, Part III.3 addresses this explicitly:

> "The commutator terms have the schematic form $\mathrm{Tr}(F_{\mu\nu}[F^{\mu\rho}, F^\nu{}_\rho])$, which involves three field-strength factors and no covariant derivatives. These are $\mathcal{C}$-odd."

The $\mathcal{C}$-odd commutator terms vanish in the $\mathcal{C}$-invariant effective action. The remainder is $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ plus dimension-8 corrections. The operator $\mathcal{O}_{\mathrm{EOM}}$ therefore has dev $\geq 2$ by the same mechanism as $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$.

Alternatively, $\mathcal{O}_{\mathrm{EOM}}$ is itself a sum of terms of the form $(D_\rho \cdot)^2$, each contributing a squared deviation factor. This alternative argument is stated but not fully worked out.

**The gap is closable** with one paragraph providing the explicit spectral verification for $\mathcal{O}_{\mathrm{EOM}}$, confirming dev $\geq 2$ directly rather than through the EOM reduction.

**(c) Lattice artifacts at dimension 6.** The Wilson action contains $O(a^2)$ lattice artifacts. Balaban's coupling renormalization subtracts only the dimension-4 part ($S_{\mathrm{YM}}/g_k^2$). The remainder includes dimension-6 lattice artifacts by definition. The uniqueness of $S_{\mathrm{YM}}$ as the sole dimension-4 operator ([CONFIRMED] item 3 in PROOF-CHAIN.md) ensures no dimension-4 contamination from operator mixing. The artifacts contribute to dimension 6 and higher, where the classification applies.

**Impact on the claimed result:** The gaps are presentational, not mathematical. The classification is logically correct; it needs more explicit lattice-specific derivation for a prize-level paper. Closable with a combined effort of 5-10 pages.
