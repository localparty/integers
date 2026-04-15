## Part G, Point 1: Jaffe–Witten Requirements

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP (for the mass gap claim) / GENUINE GAP (for full Clay compliance)

**Finding:**

**(a) The KK device.** The KK enhancement is fully decoupled in the final theory. The proof chain is: $\Delta_0^{\mathrm{KK}} > 0$ (Theorem 4, KK-enhanced theory) → $\Delta_0^{\mathrm{std}} > 0$ (Theorem 5, standard theory via Feshbach) → $\Delta_\infty > 0$ (Sections 5.1–5.7, Balaban RG applied to standard theory). Theorem 5 explicitly transfers the mass gap to the **standard** SU($N$) Wilson lattice gauge theory, and the continuum limit (Section 5) is performed entirely within the standard theory using Balaban's RG. No step after Theorem 5 requires the KK enhancement. The KK device is a proof technique, not part of the final theory.

**(b) The gauge group.** The paper claims the result for all compact simple Lie groups (abstract, Appendix I.4, Theorem I.4.1). For SU($N$), $N \geq 2$: the proof is given in the body. For SO($N$), Sp($N$), and exceptional groups: the extension in Appendix I.4 uses compact irreducible symmetric spaces as internal manifolds and the Weitzenböck–Bochner theorem for the universal spectral gap. This is plausible but the extension relies on the SU($N$) → general $G$ extension of Balaban's UV stability (Point C1), which is the closable gap identified there.

**(c) The lattice regulator.** The proof starts from Wilson's lattice gauge theory. The continuum limit is obtained as a subsequential limit. Universality (independence of the lattice regularization) is not proved but is expected from perturbative AF and not required by Jaffe–Witten.

**(d) The precise claim.** What is proved: "For SU($N$) with $N \geq 2$, starting from Wilson's lattice gauge theory on $\Lambda_L$ in the physical regime ($a \gg r_3$), there exists a subsequential continuum limit $\{S_n\}$ satisfying OS1–OS5 with mass gap $\Delta_\infty > 0$."

Is this sufficient for Clay? The mass gap and OS axiom requirements are met. However, Jaffe–Witten §4 also requires:
- Local field operators in correspondence with curvature polynomials (Conjecture L.1 — open)
- Short-distance match to perturbative AF (Conjecture L.2 — open)
- Stress tensor (Conjecture L.3 — open)
- OPE with prescribed singularities (Conjecture L.4 — open)

These four items are explicitly acknowledged as open in PROOF-CHAIN IV.5 and Appendix L. The paper states: "A Clay submission cannot honestly claim that any of L.1–L.4 are established by the main body."

**(e) The quantitative predictions.** The predictions ($\sqrt{\sigma} = 437$ MeV, glueball $0^{++}$ at ~1.5 GeV) are consistency checks derived from the mass gap value. The proof does not rely on numerical agreement with experiment. These are valuable for physics but irrelevant for the mathematical proof.

**Impact on the claimed result:**
The mass gap claim $\Delta_\infty > 0$ with OS axioms is established (modulo the K-uniformity condition discussed below). For **full** Clay compliance, the four structural ingredients L.1–L.4 constitute a **GENUINE GAP** — the paper honestly acknowledges this. The paper positions these as a "follow-up research programme" of comparable difficulty to known unsolved problems in 4D CQFT.
