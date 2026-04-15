## Part B, Point 2: The Fredenhagen-Marcu Criterion

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

**(a) Precise conditions.** The Fredenhagen-Marcu (FM) criterion (PRL 56, 1986) introduces an order parameter $\rho_{\mathrm{FM}}$ that vanishes in the confined phase. The preprint's use of FM is as a supplementary diagnostic, not as the primary proof mechanism. The mass gap $\Delta_0 > 0$ is established directly from the cluster expansion (Theorem 4(e)), which proves exponential decay of ALL connected correlators. FM provides additional physical interpretation.

The FM conditions are: (i) the Wilson loop expectation satisfies an area law, and (ii) the Polyakov loop expectation vanishes (on a finite-temperature lattice). Both are verified in the present setting: (i) follows from the cluster expansion (Theorem 4(d): $\sigma_0 > 0$), and (ii) follows from center symmetry.

**(b) Direction of implication.** There is a logical subtlety here. The FM criterion establishes:

$$\sigma > 0 \implies \rho_{\mathrm{FM}} = 0 \implies \text{confinement (no charged states at finite energy)}$$

Confinement alone does NOT automatically give $\Delta > 0$: a confining theory could in principle have massless neutral (singlet) states. A separate argument is needed to exclude massless glueballs.

However, the preprint does NOT rely on FM to prove $\Delta > 0$. The logical chain is:

1. Cluster expansion convergence $\implies$ exponential decay of all connected correlators $\implies$ $\Delta_0 > 0$ (directly from the spectral gap of the transfer matrix).
2. Separately, $\sigma > 0$ from the area law, and the flux tube argument (Appendix F) gives an independent estimate $\Delta \geq c\sqrt{\sigma}$.

Both routes give $\Delta_0 > 0$. The FM criterion is cited as a consistency check, not as a load-bearing step.

Appendix F provides the rigorous connection $\sigma > 0 \implies \Delta > 0$ via the Wilson loop spectral representation: the area law forces $\langle W_{C_{T,R}}\rangle \leq \|\Psi_R\|^2 e^{-\Delta T}$, with the static potential $V(R) = \sigma R$ implying a minimum-energy closed flux tube of mass $\geq c\sqrt{\sigma}$. This is a complete argument, though the Luscher correction is used only for quantitative estimates, not for the existence of the gap.

**Impact on the claimed result:** None. The mass gap is proved directly from the cluster expansion. FM is supplementary. The direction of implication is correctly identified and the proof does not rely on FM for the main claim.
