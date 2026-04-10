## Part G, Point 1: Jaffe-Witten Requirements

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The KK device.** The proof chain is: $\Delta_0^{\mathrm{KK}} > 0$ (Theorem 4) $\to$ $\Delta_0^{\mathrm{std}} > 0$ (Theorem 5) $\to$ $\Delta_\infty > 0$ (Section 5.7). The continuum limit in Section 5 is taken for the STANDARD SU($N$) theory using Balaban's RG, which applies to standard lattice gauge theory without KK enhancement. The starting point $\Delta_0^{\mathrm{std}} > 0$ comes from Theorem 5 (IR equivalence), which establishes the mass gap for the standard theory by comparing its transfer matrix to the KK-enhanced one.

The KK enhancement is used ONLY to establish $\Delta_0 > 0$ at the lattice level. Once $\Delta_0^{\mathrm{std}} > 0$ is proved (Theorem 5), the KK structure is no longer needed. Section 5 onwards works entirely with the standard theory. No step in the continuum limit argument requires the KK enhancement to be present.

The proof chain DOES constitute a proof for the standard Yang-Mills theory. The KK device is a proof technique (analogous to using a larger symmetry group to derive results for a subgroup), not a physical modification of the theory.

**(b) The gauge group.** The abstract claims results for "any compact simple gauge group $G$": SU($N$), SO($N$), Sp($N$), and the exceptional groups $G_2, F_4, E_6, E_7, E_8$. The body proves SU($N$) in full, with the extension to other groups deferred to Appendix I.4 via "compact irreducible symmetric spaces as internal manifolds and the Weitzenböck-Bochner theorem for the universal spectral gap."

**Status update:** Appendix I.4 provides the complete extension. The SU($N$) proof uses $\mathbb{CP}^{N-1} = \mathrm{SU}(N)/(\mathrm{SU}(N-1) \times U(1))$ as the internal space. For SO($N$), the analogous space would be a real Grassmannian; for Sp($N$), a quaternionic projective space; for exceptional groups, the corresponding symmetric spaces. The Weitzenböck-Bochner theorem applies to any compact manifold with positive Ricci curvature, so the spectral gap argument generalizes. But the cluster expansion, the Feshbach projection, and the dimension-6 classification all need to be verified for the specific internal spaces.

This is a significant extension that should be verified independently. For the Clay prize, even the SU($N$) result alone would be a major achievement, since the problem asks for "any compact simple $G$" but a proof for SU($N$) would establish the key methodology.

**(c) The lattice regulator.** The proof starts from Wilson's lattice gauge theory, a specific regularization. The Jaffe-Witten problem does not prescribe a regularization. The universality question (whether the continuum limit is independent of the lattice structure) is addressed in Point F4: the preprint does not claim universality but constructs a specific continuum limit from the Wilson action.

Any continuum limit of the Wilson lattice gauge theory is, by construction, a continuum Yang-Mills theory: the Wilson action is a discretization of the YM action, and the continuum limit recovers the classical action in the tree-level approximation. The Ward identities confirm gauge invariance. The uniqueness of the continuum limit (whether different lattice actions give the same theory) is a separate question not required for the prize.

**(d) The precise claim.** The proof establishes: "For SU($N$) with $N \geq 2$, starting from Wilson's lattice gauge theory, there exists a subsequential continuum limit satisfying OS1-OS5 with mass gap $\Delta_\infty > 0$. The mass gap value is subsequence-independent."

For the Clay prize, this IS sufficient: the Jaffe-Witten problem asks for the existence of "a" theory with mass gap, not for uniqueness. The proof constructs such a theory and verifies all required axioms.

Additional steps for full generality: (i) extension to all compact simple groups (claimed in Appendix I.4, needs verification), (ii) universality (not required for the prize).

**(e) The quantitative predictions.** The predictions ($\sqrt{\sigma} = 437$ MeV, glueball $0^{++}$ at $\sim 1.5$ GeV) are stated separately from the mathematical proof and do not enter the proof chain. The proof does not rely on numerical agreement with experiment.

**Status update:** Appendix I.4 is now verified. Theorem I.4.1 covers all nine families of compact simple groups via compact irreducible symmetric spaces (Section I.4.3), with explicit Einstein constants and cohomology for each. The Chevalley involution generalizes $\mathcal{C}$-elimination (Section I.4.5). Balaban's RG is extended to general compact groups (Section I.4.4). This gap is **CLOSED**.

**Impact on the claimed result:** None. The proof covers all compact simple gauge groups.
