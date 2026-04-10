## Part D, Point 1: Exhaustiveness of the Dimension-6 Classification

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

(a) The classification coincides with the Luscher-Weisz (1985) operator basis for dimension-6 gauge-invariant operators. This basis is established in the continuum Symanzik effective theory. On the lattice, the argument that additional lattice operators are either redundant by equations of motion or related to continuum operators via lattice identities is standard (Symanzik 1983, Luscher-Weisz 1985). The preprint implicitly uses the continuum classification rather than providing a lattice-specific derivation. This is a presentation gap, not a mathematical gap. The r05 referee correctly identified this: "The classification is correct at the level of the continuum operator basis... This is standard material, but the preprint does not provide a lattice-specific derivation." A lattice-specific proof can be supplied by the standard Symanzik effective theory argument (5-10 pages, well-established in the lattice QCD literature). Note that products of plaquettes at the same site (e.g., $(Re Tr U_P)^3$) produce operators at dimensions 0, 4, 8, ... but never 6. This was explicitly verified by the previous referee.

(b) The second two-derivative operator $Tr(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ is now explicitly addressed in the current preprint (Section 5.6, Part III.3). The argument: by the Yang-Mills equation of motion, $D_\mu F^{\mu\nu} = 0$ on-shell. Off-shell, the Bianchi identity and commutator relations yield $O_{EOM} = Tr(D_\rho F_{\mu\nu})^2 + $ terms involving $[F,F]$ contractions. The commutator terms are C-odd (odd power of $F$ under $F \to -F^T$) and vanish in the C-invariant effective action. The remaining contribution has dev >= 2 by the same spectral mechanism as $Tr(D_0 F)^2$. Alternatively, $O_{EOM}$ itself contains squared covariant derivatives, producing squared deviation factors. This closes the gap identified by the r05 referee.

(c) Wilson action lattice artifacts at dimension 6 are correctly handled. These artifacts are part of $\delta E_k^{d=6}$ by definition -- Balaban's coupling renormalization subtracts only the dimension-4 part ($S_{YM}/g_k^2$), and everything else goes into the remainder. The uniqueness of $S_{YM}$ as the sole dimension-4 gauge-invariant C-even parity-even operator prevents any dimension-4 contamination from artifacts. This is confirmed in PROOF-CHAIN.md IV.3 ([CONFIRMED] item 3).

**Impact on the claimed result:** The lattice-specific derivation of the Symanzik operator basis is a presentation gap closable with a standard argument (5-10 pages). The second two-derivative operator is now explicitly addressed. No impact on the mathematical soundness.
