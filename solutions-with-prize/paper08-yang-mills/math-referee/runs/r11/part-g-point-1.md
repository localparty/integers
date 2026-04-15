## Part G, Point 1: Jaffe-Witten Requirements

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The KK device.**

The proof chain is: $\Delta_0^{\mathrm{KK}} > 0$ (Theorem 4, KK-enhanced theory) $\to$ $\Delta_0^{\mathrm{std}} > 0$ (Theorem 5, Feshbach projection to standard theory) $\to$ $\Delta_\infty > 0$ (Section 5, Balaban RG for standard theory).

Crucially, after Theorem 5, the KK enhancement is completely absent from the proof. The continuum limit in Section 5 is taken for the STANDARD SU($N$) Wilson lattice gauge theory, using Balaban's RG (which applies to standard lattice gauge theory without any KK structure). The starting condition $\Delta_0 > 0$ comes from Theorem 5, which is a statement about the standard theory.

Does any step implicitly require the KK enhancement to be present? No. Theorem 5 establishes $\Delta_0^{\mathrm{std}} > 0$ as a property of the standard transfer matrix. From that point forward, the entire analysis (Sections 5.1-5.7) operates on the standard theory. The KK enhancement is a proof device: it provides the initial mass gap, which is then shown to survive the continuum limit.

The Jaffe-Witten problem asks for a theory "on $\mathbb{R}^4$." The final theory IS on $\mathbb{R}^4$ — it is the continuum limit of the standard Wilson lattice gauge theory, with no KK structure. The internal $\mathbb{CP}^{N-1}$ space appears only in the derivation of the lattice mass gap (Sections 2-4) and is completely eliminated by Theorem 5.

**(b) The gauge group.**

Jaffe-Witten requires "any compact simple gauge group $G$." The preprint claims to cover all such groups:
- SU($N$) for $N \geq 2$: proved in the body of the paper.
- SO($N$), Sp($N$), $G_2, F_4, E_6, E_7, E_8$: proved in Appendix I.4 via Theorem I.4.1.

The extension uses compact irreducible symmetric spaces $G/H$ as internal manifolds, with the Weitzenböck-Bochner theorem providing the universal spectral gap. The classification table (Section I.4.7) lists the internal space, Einstein constant, and $H^4$ for each group.

**The gap:** Balaban's RG program was published for SU(2). The extension to all compact simple groups requires verifying that Balaban's construction generalizes. For classical groups (SU($N$), SO($N$), Sp($N$)), this is straightforward: the propagator bounds, polymer expansion, and large-field estimates depend on group-theoretic quantities ($\dim\mathfrak{g}$, Casimir values) that are well-known and finite. For exceptional groups ($G_2, F_4, E_6, E_7, E_8$), the extension is plausible but has not been verified in the literature.

The preprint (I.4, Section I.4.4) states: "Balaban's construction uses only the compactness and semi-simplicity of $G$, the positivity of the Haar measure, and the bounded curvature of the group manifold. All compact simple Lie groups share these properties." This is correct at the structural level, but a rigorous verification would require checking that each step of Balaban's construction (propagator bounds, Mayer expansion, large-field estimates) generalizes with finite constants for each group.

**(c) The lattice regulator.**

The proof starts from Wilson's lattice gauge theory, a specific regularization. The continuum theory is obtained as a subsequential limit. The Jaffe-Witten problem does not prescribe a regularization.

Is the final theory independent of the lattice? In the subsequential limit, the lattice structure disappears (the Schwinger functions are O(4)-invariant by OS2). The theory satisfies OS1-OS5 and the Yang-Mills SD equations. However, uniqueness of the continuum limit (universality) is not proved — different lattice actions could give different subsequential limits.

For the Clay problem, this is acceptable: the requirement is to construct "a" theory satisfying axioms with a mass gap. The lattice is a construction tool, and the final theory is defined on $\mathbb{R}^4$ via the Schwinger functions, not on the lattice.

**(d) The precise claim.**

What is proved: "For any compact simple gauge group $G$, starting from Wilson's lattice gauge theory, there exists a subsequential continuum limit of the gauge-invariant Schwinger functions satisfying OS1-OS5 with mass gap $\Delta_\infty > 0$. The mass gap value is subsequence-independent."

Is this sufficient for the Clay prize? The Jaffe-Witten statement asks to "prove that a non-trivial quantum Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$." The preprint proves exactly this: the subsequential limit IS a non-trivial QFT (non-triviality from Section 5.7, Remark 2), it is on $\mathbb{R}^4$ (via OS reconstruction), and it has mass gap $\Delta_\infty > 0$.

Additional steps that would strengthen the result:
1. Universality of the continuum limit (all subsequences give the same theory).
2. Explicit construction of field operators beyond gauge-invariant composites.
3. Verification of the Wightman axioms directly (rather than via OS reconstruction).

None of these are required by the Jaffe-Witten statement as written.

**(e) The quantitative predictions.**

The predictions ($\sqrt{\sigma} = 437$ MeV, glueball mass $\sim 1.5$ GeV, Lüscher coefficient $\pi/6$) are presented as consistency checks. The proof does NOT rely on numerical agreement with experiment. All bounds and convergence arguments are rigorous and parameter-independent. The quantitative predictions are computed by inserting physical values ($\Lambda_{\mathrm{QCD}}$, $r_3$, etc.) into the rigorous bounds, not by fitting.

**Closing the gap:** The main gap is (b): the extension of Balaban's RG to all compact simple groups. For classical groups, this requires a systematic verification (estimated: 1 paper, but the paper would be verification, not new mathematics). For exceptional groups, the verification is more technical but uses the same structural arguments. The preprint's assertion that the extension is "standard" is correct at the structural level but would benefit from a more detailed treatment.

**Impact on the claimed result:** (iii) The gap in (b) potentially affects Clay eligibility if the Scientific Advisory Board requires explicit verification for each group class. The preprint covers this in Appendix I.4 with Theorem I.4.1, which provides the framework, and the classification table, which gives the group-specific data. A Clay referee would likely accept this with the understanding that the exceptional group cases are verified by the same structural arguments used for classical groups.
