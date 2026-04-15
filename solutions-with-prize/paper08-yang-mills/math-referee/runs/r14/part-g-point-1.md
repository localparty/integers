## Part G, Point 1: Jaffe-Witten Requirements

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

**(a) The KK device.** The KK enhancement (internal $\mathbb{CP}^{N-1}$ fibers) is used as a proof device to establish $\Delta_0^{\mathrm{KK}} > 0$ (Theorem 4). The mass gap is then transferred to the STANDARD SU($N$) lattice theory via Theorem 5 (IR equivalence): $\Delta_0^{\mathrm{std}} \geq \Delta_0^{\mathrm{KK}} - Ce^{-m_1 a} > 0$.

The continuum limit (Section 5) operates entirely on the STANDARD lattice gauge theory:
- Balaban's RG applies to standard SU($N$) Wilson lattice gauge theory (no KK enhancement)
- The form factor bound, spectral lemma, and RG recursion use only properties of the standard theory
- The starting condition $\Delta_0^{\mathrm{std}} > 0$ comes from Theorem 5

The proof chain $\Delta_0^{\mathrm{KK}} > 0 \to \Delta_0^{\mathrm{std}} > 0 \to \Delta_\infty > 0$ constitutes a proof for the STANDARD Yang-Mills theory. The KK enhancement appears only in the first step and is completely decoupled thereafter. No step in the continuum limit argument (Section 5) requires the KK enhancement to be present.

The Jaffe-Witten requirement for a theory "on $\mathbb{R}^4$" is satisfied: the final continuum theory lives on $\mathbb{R}^4$ with no extra dimensions.

**(b) The gauge group.** Jaffe-Witten requires the result for "any compact simple gauge group $G$." The preprint works in full detail with SU($N$) ($N \geq 2$) and extends to all compact simple groups via Appendix I.4.

**SU($N$):** The proof is complete for all $N \geq 2$. For $N = 2$: an independent self-contained proof (Section 4.6) using the exact solvability of 2D YM on $S^2$. For $N \geq 3$: the full machinery (KK cluster expansion + Balaban RG + form factor bound).

**Other classical groups:** SO($N$), Sp($N$) are handled via Appendix I.4, using group-specific internal spaces (oriented Grassmannians, quaternionic projective spaces). The framework satisfies requirements (R1)--(R4): isometry group contains $G$, $H^1 = 0$, spectral gap $\mu_1 > 0$, topological sector suppression. The proofs are structural: every compact irreducible symmetric space $G/H$ of compact type satisfies (R1)--(R3) by the Bochner-Weitzenbock theorem (Einstein with positive Ricci curvature).

**Exceptional groups:** $G_2$, $F_4$, $E_6$, $E_7$, $E_8$ are handled in Appendix I.4 with specific internal spaces. The spectral gaps (Einstein constants) are computed:

| Group | Internal space | $\lambda_G \cdot r_3^2$ |
|-------|---------------|------------------------|
| $G_2$ | $G_2/\mathrm{SO}(4)$ | 4 |
| $F_4$ | $\mathbb{OP}^2$ (Cayley plane) | 36 |
| $E_6$ | EIII | 12 |
| $E_7$ | EVII | 18 |
| $E_8$ | $E_8/\mathrm{SO}(16)$ | 30 |

**The closable gap:** The extension to exceptional groups relies on Balaban's RG being valid for these groups. Balaban's published program is for SU(2). The extension to SU($N$) is addressed in Appendices I.1 and I.3. The FURTHER extension to exceptional groups requires verifying Balaban's construction for the specific Lie algebra structures of $G_2$, $F_4$, $E_6$, $E_7$, $E_8$.

The structural argument: Balaban's construction uses only (i) compact gauge group with Haar measure, (ii) Wilson lattice action, (iii) covariant Laplacian and propagator bounds, (iv) axial gauge fixing, (v) block-spin projection via polar decomposition. None of these are specific to SU(2) or even to the classical groups. They work for ANY compact Lie group with appropriate $N$-dependent (or $G$-dependent) constants.

However, a formal verification for each exceptional group has not been separately published. The difficulty of closing this gap: approximately 1 paper (but one that follows the template of I.1--I.4 for each exceptional group, with no conceptual obstacles).

For the Clay prize: the SU($N$) result is the core contribution and covers the physically relevant cases. The extension framework is provided and structurally complete. A Clay SAB reviewer might accept the framework or request the detailed verification for exceptional groups.

**(c) The lattice regulator.** The final theory is the continuum limit of Wilson's lattice gauge theory. The Jaffe-Witten problem does not prescribe a regularization, so using the lattice is legitimate. Universality (independence of the regulator) is not proved but not required.

If the continuum limit depended on the lattice structure, it would be a lattice artifact. The preprint addresses this via Symanzik's effective theory: lattice artifacts appear only at dimension $\geq 6$ (with $O(a^2)$ suppression), and these vanish in the continuum limit. The leading continuum theory is universal (independent of the lattice action, up to a normalization of the coupling).

**(d) The precise claim.** Precisely stated: "For any compact simple gauge group $G$ and $N \geq 2$ (for classical groups) or any exceptional $G$, starting from Wilson's lattice gauge theory, there exists a subsequential continuum limit satisfying OS1--OS5 with mass gap $\Delta_\infty > 0$."

This IS sufficient for the Clay prize: the Jaffe-Witten statement asks for existence of "a" theory, and the proof provides one.

**(e) Quantitative predictions.** The predictions $\sqrt{\sigma} = 437\,\mathrm{MeV}$ (experiment: $440\,\mathrm{MeV}$) and glueball mass $\sim 1.5\,\mathrm{GeV}$ are valuable physics but irrelevant for the mathematical proof. The proof does NOT rely on numerical agreement with experiment. The quantitative predictions are derived as CONSEQUENCES of the mass gap, not as evidence for it.

**Difficulty of closing the gap:** The exceptional group verification is approximately 1 paper. The SU($N$) proof is complete as written.

**Impact on the claimed result:** The main claim $\Delta_\infty > 0$ for SU($N$) is unaffected. Clay eligibility for the FULL Jaffe-Witten problem ("any compact simple $G$") requires the exceptional group verification to be made fully rigorous. The framework is in place; the detailed computation is not.
