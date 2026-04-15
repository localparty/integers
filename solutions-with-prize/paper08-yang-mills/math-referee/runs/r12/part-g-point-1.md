## Part G, Point 1: Jaffe-Witten Requirements

**Weight:** HEAVY
**Verdict:** GENUINE GAP (sub-points b, d — gauge group coverage and Clay completeness); CLOSABLE GAP (sub-points a, c, e)

---

**Finding:**

This is the most critical point for Clay Prize eligibility.

**(a) The KK device and decoupling.** The proof uses the KK-enhanced theory as a proof device, then transfers the mass gap via Theorem 5. The final theory in the continuum limit is the standard $\mathrm{SU}(N)$ Wilson lattice Yang-Mills theory (Balaban's RG applies to this theory without KK enhancement). The KK-enhanced theory appears only at the starting lattice scale, to establish $\Delta_0^{\text{std}} > 0$ via Theorem 5.

The proof chain: $\Delta_0^{\text{KK}} > 0$ (Theorem 4, KK-enhanced) $\to$ $\Delta_0^{\text{std}} > 0$ (Theorem 5, IR equivalence) $\to$ $\Delta_\infty > 0$ (Sections 5.4–5.7, Balaban RG for standard theory). The continuum limit is constructed for the standard theory. The KK enhancement is fully decoupled in the final result: the continuum limit does not involve $\mathbb{CP}^{N-1}$ fields. The standard Yang-Mills theory on $\mathbb{R}^4$ has a mass gap. SOUND.

**(b) The gauge group — GENUINE GAP.** The Jaffe-Witten problem requires "any compact simple gauge group $G$." The preprint's coverage:

- **Main body and abstract**: Claims the result for "all SU($N$), $N \geq 2$" in some places, and "all compact simple Lie groups" in others.
- **I-gap-closures.md (Section I.4.3)**: Explicitly states: "We leave this program for future work and **restrict the present paper to $G = \mathrm{SU}(N)$**, $N \geq 2$."
- **I4-other-gauge-groups.md (Theorem I.4.1)**: Claims "Universal mass gap" for all compact simple Lie groups, but Step 3 says "A step-by-step verification... is provided in **Appendix K**" which does not exist in the document set.

This contradiction is definitive and un-closable without new work:
1. The restriction to SU($N$) is explicit in I-gap-closures.md.
2. The claim for general $G$ in I4-other-gauge-groups.md cites a non-existent Appendix K.
3. The compact simple Lie groups not covered by SU($N$): $\mathrm{SO}(N)$, $\mathrm{Sp}(N)$, and the exceptional groups $G_2$, $F_4$, $E_6$, $E_7$, $E_8$. For $G_2$, the construction would need an internal space $G_2/H$ with appropriate Weitzenböck bound; for exceptional groups, the KK device requires a suitable compact internal space.

The internal space $\mathbb{CP}^{N-1} = \mathrm{SU}(N)/\mathrm{U}(N-1)$ works specifically for $\mathrm{SU}(N)$: the structure group of the KK bundle matches $\mathrm{SU}(N)$. For other groups, the analog of $\mathbb{CP}^{N-1}$ would be a different homogeneous space, and the spectral gap calculation (Weitzenböck + Ikeda-Taniguchi) would need to be redone. This is substantial new work. GENUINE GAP.

For the Clay Prize: the current preprint proves the mass gap only for $\mathrm{SU}(N)$, $N \geq 2$. A complete solution to the Jaffe-Witten problem requires all compact simple groups. The preprint as written is a partial solution.

**(c) The lattice regulator and universality.** The continuum limit is constructed from the Wilson action (a specific lattice regularization). Whether the result is independent of the lattice regularization is the universality question (see Part F4). The preprint does not address universality. For the Clay Prize, the question is whether "a quantum Yang-Mills theory" constructed from any reasonable UV regularization has the same continuum limit. Given the expected universality of 4D pure gauge theory (all regularizations flow to the same IR fixed point), the result likely holds for other regularizations, but this is not proved. CLOSABLE GAP: add a paragraph discussing universality and citing the perturbative universality argument (all renormalizable gauge theories with the same gauge group flow to the same universal behavior under RG). Difficulty: **1 paragraph**.

**(d) The precise claim — the Clay problem interpretation.** What the preprint proves: "For $\mathrm{SU}(N)$, $N \geq 2$, starting from Wilson's lattice gauge theory, there exists a subsequential continuum limit $\{S_n\}$ satisfying OS1–OS5 with $\Delta_\infty > 0$, which by OS reconstruction gives a Wightman QFT."

What the Clay problem requires (Jaffe-Witten, 2000): "For any compact simple gauge group $G$, quantum Yang-Mills theory on $\mathbb{R}^4$ exists and has a mass gap $\Delta > 0$."

The gaps (comparing what is proved to what is required):
1. **"Any compact simple group"**: only $\mathrm{SU}(N)$ is proved.
2. **"Quantum Yang-Mills theory"**: the preprint proves existence of a QFT; whether it is the Yang-Mills theory is not proved (see F5d).
3. **"On $\mathbb{R}^4$"**: the preprint constructs a Wightman theory, which is indeed on $\mathbb{R}^{3,1}$ (Minkowski space via OS reconstruction). The Euclidean theory is on $\mathbb{R}^4$. ✓
4. **"Has a mass gap"**: proved via $\Delta_\infty > 0$. ✓
5. **Uniqueness**: not addressed.

Items 1, 2, and 5 are gaps. Item 1 requires new work for non-SU($N$) groups. Items 2 and 5 require proof of the YM equations of motion and universality respectively.

**(e) Quantitative predictions and their role.** The preprint makes quantitative predictions ($\sqrt{\sigma} = 437$ MeV, etc.). These are physically interesting but irrelevant to the mathematical proof and should not be used as evidence for correctness. The preprint does not use them as such — they appear in the Introduction as motivation. SOUND.

**Impact on the claimed result:** The most critical gap is sub-point (b): the preprint does not prove the mass gap for all compact simple gauge groups, despite the abstract's claim. For Clay Prize eligibility, this is a show-stopper. The proof for $\mathrm{SU}(N)$ is a substantial partial result, but the Clay problem requires all compact simple groups. The non-existent Appendix K makes the general-$G$ claim unsubstantiated.
