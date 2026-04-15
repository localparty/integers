## Part B, Point 2: The Fredenhagen-Marcu Criterion

**Weight:** LIGHT
**Verdict:** CLOSABLE GAP

---

**Finding:**

**(a) The logical chain $\sigma > 0 \to \Delta > 0$.** The preprint's "logical chain for item 4" in Section 4.4 reads: "The area law $\sigma_0 > 0$ (item 3) implies a mass gap $\Delta_0 > 0$ via the transfer matrix and flux tube energy (Appendix F, Theorem F.1)." This chain presents $\Delta_0 > 0$ as a consequence of $\sigma_0 > 0$, which is not the primary route.

The primary route in the proof is different: item (c) of Theorem 4 establishes exponential decay of connected correlators with rate $m > 0$ via the cluster expansion directly. By the transfer matrix spectral theorem, exponential decay of connected two-point functions of a gauge-invariant local observable $\mathcal{O}$ at rate $m$ implies the spectral gap of the transfer matrix is at least $m$. This is the mass gap $\Delta_0 \geq m > 0$. This argument is rigorous and does not require the area law.

The area law $\sigma_0 > 0$ and the FM criterion are derived *consequences* of the cluster expansion, not inputs to the mass gap proof. The quantitative bound $\Delta_0 \geq c\sqrt{\sigma_0}$ in item (e) relies on Appendix F (Theorem F.1), which Appendix F.3 (noted in summary context) establishes via a heuristic "closed flux tube" energy minimization: the flux tube energy for a circular loop of radius $R$ is $E(R) = 2\pi \sigma R + T_0/(2\pi R) \geq \min_R E(R) \approx c\sqrt{\sigma T_0}$. This Nambu–Goto string energy argument is standard physics but not a rigorous operator argument. Appendix F.5 says "The mass gap is a direct consequence of the string tension, which is a direct consequence of the area law, which is a direct consequence of $\mathbb{CP}^2$ topology." This causal chain is presented as the proof structure but inverts the actual logical dependency.

**(b) The direction of Fredenhagen-Marcu.** The FM criterion (Fredenhagen–Marcu, CMP 92, 1983) establishes *confinement* via the FM order parameter $\rho_{\mathrm{FM}} = 0$ when $\sigma > 0$. Confinement means the absence of isolated fractionally-charged (colored) states in the superselection sectors of the Hilbert space. This is consistent with $\Delta > 0$ but does not directly imply it: a confining theory could in principle have a continuum of massive glueball states starting at $\Delta = 0^+$ (no isolated eigenvalue). FM confinement rules out massless *charged* excitations but does not rule out massless *neutral* excitations (glueballs).

The preprint's claim that "FM confinement certifies the absence of deconfined charged states" is correct, but the step "FM confinement $\Rightarrow$ mass gap $\Delta > 0$" is not a theorem in the FM paper (CMP 92, 1983). Fredenhagen–Marcu prove a confinement criterion, not a mass gap criterion.

**Summary.** The mass gap $\Delta_0 > 0$ is rigorously proved via exponential decay of connected correlators (Theorem 4c), which does not rely on the area law, FM, or Appendix F. The presentation of the logical chain in Section 4.4 (items 3→4) obscures this by placing the heuristic flux tube argument as the primary route. This is a presentation error with no impact on the validity of the existence proof, but it is misleading in a Clay Prize context. Closing requires: reorder the logical chain in Section 4.4 to make clear that $\Delta_0 > 0$ follows from item (c) (exponential decay) directly, and relabel items (d)–(e) (area law, FM, quantitative $\Delta \geq c\sqrt{\sigma}$) as supplementary corollaries with the heuristic flux tube argument in Appendix F explicitly flagged. Difficulty: **1 paragraph** plus annotation of Appendix F.

**Impact on the claimed result:** The mass gap $\Delta_0 > 0$ is established by item (c) of Theorem 4 (exponential decay), independently of the FM criterion and Appendix F. The heuristic in Appendix F.3 does not affect $\Delta_0 > 0$. The gap here is a logical presentation error, not a mathematical error. Clay Prize eligibility requires the logical chain to be unambiguous; as written, a reviewer could object that the primary mass gap argument relies on a heuristic.
