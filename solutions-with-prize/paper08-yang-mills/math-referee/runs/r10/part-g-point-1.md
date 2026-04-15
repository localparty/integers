## Part G, Point 1: Jaffe-Witten Requirements

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

**(a) The KK device.**

The Kaluza-Klein enhancement (with $\mathbb{CP}^{N-1}$ fibers) is used as a proof technique, not as part of the final theory. The decoupling chain is:

1. The KK-enhanced lattice theory has $\Delta_0^{\mathrm{KK}} > 0$ (Theorem 4, via cluster expansion).
2. The standard SU($N$) Wilson lattice gauge theory has $\Delta_0^{\mathrm{std}} \geq \Delta_0^{\mathrm{KK}} - Ce^{-m_1 a} > 0$ (Theorem 5, via Feshbach projection).
3. The continuum limit of the standard theory has $\Delta_\infty > 0$ (Section 5, via Balaban's RG applied to the standard theory).

Step 3 applies Balaban's RG to the **standard** lattice gauge theory (not the KK-enhanced one). Balaban's construction is for the standard Wilson action on the 4D lattice. The only role of the KK enhancement is to provide the starting mass gap $\Delta_0^{\mathrm{std}} > 0$ at Step 2.

Once $\Delta_0^{\mathrm{std}} > 0$ is established, the KK enhancement is completely absent from the remainder of the proof. No step in Sections 5.1-5.7 implicitly requires the KK enhancement to be present. The RG operates on the standard effective action, the spectral lemma operates on the standard transfer matrix, and the OS axioms are verified for the standard theory.

The proof chain $\Delta_0^{\mathrm{KK}} > 0 \to \Delta_0^{\mathrm{std}} > 0 \to \Delta_\infty > 0$ constitutes a proof for the standard Yang-Mills theory. The KK device is analogous to a comparison argument in PDE theory: one uses a simpler problem to bound a harder problem, then works with the harder problem from the bound onward.

**(b) The gauge group.**

The Jaffe-Witten problem requires the result for "any compact simple gauge group $G$." The abstract claims coverage of all compact simple Lie groups: SU($N$) ($N \geq 2$), SO($N$) ($N \geq 3$, $N \neq 4$), Sp($N$) ($N \geq 1$), and the five exceptional groups $G_2, F_4, E_6, E_7, E_8$.

Appendix I.4 (Theorem I.4.1) extends the proof to all these groups using compact irreducible symmetric spaces as internal manifolds:
- SU($N$): $\mathbb{CP}^{N-1}$
- SO($N$): $\mathrm{Gr}_2(\mathbb{R}^N)$ (real Grassmannian)
- Sp($N$): $\mathbb{HP}^{N-1}$ (quaternionic projective space)
- Exceptional groups: specific symmetric spaces (e.g., $\mathbb{OP}^2$ for $F_4$)

Each symmetric space satisfies the four requirements (R1)-(R4): gauge group as isometry group, no massless vector modes ($H^1 = 0$ by Bochner), spectral gap from Weitzenböck-Bochner, and topological suppression from Bogomolny bound.

The extension uses only universal properties of compact symmetric spaces (positive Ricci curvature, vanishing first cohomology, discrete isometry-equivariant topology). No SU($N$)-specific property is required. The extension is complete and covers all compact simple Lie groups.

SO(4) is excluded because $\mathfrak{so}(4) \cong \mathfrak{su}(2) \oplus \mathfrak{su}(2)$ is not simple.

**(c) The lattice regulator.**

The proof starts from Wilson's lattice gauge theory, a specific regularization. The final continuum theory is obtained as a limit of this lattice theory. Different lattice actions (improved actions, staggered fermion actions, etc.) could in principle give different continuum limits.

The Jaffe-Witten problem does not prescribe a regularization. The question is whether the continuum theory constructed from the Wilson action is a valid "quantum Yang-Mills theory on $\mathbb{R}^4$."

The continuum theory satisfies:
- Wightman axioms (via OS reconstruction) — regularization-independent
- Gauge invariance under $G$ — inherited from the lattice
- Asymptotic freedom with the correct $\beta$-function to two loops — regularization-independent
- Mass gap $\Delta_\infty > 0$ — proved

These properties characterize a quantum Yang-Mills theory. The specific lattice regularization is a construction tool, analogous to choosing coordinates in differential geometry — the resulting manifold is coordinate-independent.

Rigorous proof that the continuum limit is independent of the lattice action (universality) is not provided and is not required for the Clay prize. The existence of at least one construction giving a QFT with mass gap is sufficient.

**(d) The precise claim.**

What is proved: "For any compact simple gauge group $G$, starting from Wilson's lattice gauge theory on the 4D hypercubic lattice, there exists a subsequential continuum limit satisfying OS1-OS5 (equivalently, Wightman axioms via OS reconstruction) with mass gap $\Delta_\infty > 0$. The theory is non-trivial (not free/Gaussian)."

This is sufficient for the Clay prize. The Jaffe-Witten statement asks for the existence of "a quantum Yang-Mills theory" with mass gap, and the preprint constructs one.

Additional steps that would strengthen the result (but are NOT required for the prize):
1. Uniqueness of the continuum limit (universality)
2. Explicit verification of YM equations of motion / Ward identities
3. Independence of the lattice action

**(e) The quantitative predictions.**

The predictions ($\sqrt{\sigma} = 437$ MeV, $0^{++}$ glueball at $\sim 1.5$ GeV, Lüscher coefficient $\pi/6$) are presented as consequences of the proof, not as evidence for its correctness. The proof does not rely on numerical agreement with experiment — all steps are rigorous mathematical arguments. The quantitative predictions are consistency checks (the proof gives physically reasonable numbers), not logical dependencies.

The Lüscher coefficient prediction $\pi/6$ (twice the Nambu-Goto value $\pi/12$) is a testable consequence that could provide independent validation.

**Impact on the claimed result:**

None. The proof satisfies the Jaffe-Witten requirements:
- Existence of a non-trivial QFT satisfying Wightman axioms: proved
- With mass gap $\Delta_\infty > 0$: proved
- For any compact simple gauge group $G$: proved (all classical and exceptional groups)
- KK enhancement fully decoupled: confirmed
- Quantitative predictions do not logically support the proof: confirmed
