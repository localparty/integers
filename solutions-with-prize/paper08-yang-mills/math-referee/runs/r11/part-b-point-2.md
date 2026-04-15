## Part B, Point 2: The Fredenhagen-Marcu Criterion

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The precise conditions.**

The preprint invokes the Fredenhagen-Marcu (FM) theorem to conclude that $\sigma > 0 \Rightarrow \Delta > 0$. However, the FM theorem (PRL 56, 223, 1986; CMP 92, 81, 1983) does not directly prove this implication in the form stated. The FM criterion defines an order parameter $\rho_{\mathrm{FM}}$ that distinguishes confined from deconfined phases. The connection to the mass gap is more nuanced: the FM order parameter detects absence of isolated charged states, which is related to but not identical to the mass gap.

The preprint's Appendix F (Theorem F.1) actually provides the implication via a different route: it uses the area law ($\sigma > 0$) plus the OS axioms to derive $\Delta \geq c\sqrt{\sigma}$ through the transfer matrix. The argument is: the area law for time-$T$ Wilson loops gives $\langle W_{T,R} \rangle \leq K e^{-\sigma T R}$, which via the spectral decomposition of the transfer matrix implies that states of non-zero flux have energy $\geq c\sqrt{\sigma}$ (closed flux tube argument). The lightest glueball is a closed flux tube of minimal length, with energy $E_{\min} = 2\sqrt{\pi\sigma/3}$ including the Lüscher correction.

This argument in Appendix F is self-contained and does not rely on the FM theorem per se. It relies on: (i) the area law from the cluster expansion, (ii) the transfer matrix (from OS reflection positivity), and (iii) the closed string energy estimate.

**(b) The direction of implication.**

The preprint uses two separate arguments:
1. Cluster expansion $\Rightarrow$ $\sigma > 0$ (Theorem 4(d)).
2. $\sigma > 0$ $\Rightarrow$ $\Delta > 0$ (Appendix F, Theorem F.1, via closed flux tube).

The FM criterion is cited but is not load-bearing. The actual logical chain uses the area law $\to$ flux tube energy $\to$ mass gap, which is a standard argument in constructive QFT (Seiler 1982; Borgs-Seiler 1986).

**The gap:** The citation of "Fredenhagen-Marcu theorem" is somewhat misleading — the FM work provides an order parameter and a framework, but the actual $\sigma > 0 \Rightarrow \Delta > 0$ implication uses a separate argument (closed flux tube). The preprint should clarify that the mass gap follows from the transfer matrix and the area law directly, with the FM criterion as a consistency check rather than the primary logical pathway.

**Closing the gap:** This requires 1 paragraph of clarification distinguishing the FM order parameter from the direct $\sigma > 0 \Rightarrow \Delta > 0$ argument. The mathematical content is already present in Appendix F; only the attribution needs correction.

**Impact on the claimed result:** (ii) Affects a subsidiary claim (the attribution), not the main result $\Delta_\infty > 0$. The mass gap conclusion follows from Appendix F regardless of how the FM theorem is cited.
