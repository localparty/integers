# Clay Mandatory Checklist (C1–C11)

For each item from the script's "Mandatory checks against the official statement" table, this document records the verdict (PASS / FAIL / PARTIAL) with a brief justification.

| # | Requirement | Verdict | Justification |
|:--|:------------|:--------|:--------------|
| C1 | Compact simple gauge group $G$ — *all*, not just SU(N) | **FAIL** | The body of the proof works only for SU(N). Appendix I.4 + K *sketch* the extension to SO(N), Sp(N), $G_2, F_4, E_6, E_7, E_8$ but do not execute it. The claim "for any compact simple gauge group" in the abstract is overstated. See Point G1(b). |
| C2 | Non-trivial (not free/Gaussian) | **PARTIAL** | §5.7(f) Proposition (Non-triviality) gives three signatures: (i) string tension $\sigma > 0$, (ii) non-zero connected 2-point function, (iii) asymptotic freedom. Of these, (i) and (iii) genuinely exclude the Gaussian case; (ii) does NOT (a free massive scalar has non-zero 2-point). The preprint's logic that "(ii) alone suffices" is wrong; only (i) and (iii) work. With (i) and (iii), non-triviality is established. See Point F5(c). |
| C3 | Wightman/OS axioms | **PARTIAL** | OS1–OS5 are verified at the lattice level (uniformly in $a$) and propagated to the limit via Banach–Alaoglu + Portmanteau. The corrected OS0' linear-growth condition is verified. Wightman axioms W0–W5 follow from OS via the standard reconstruction. **However**, the verification depends on the K-vs-k issue (Point C1) being resolved, and on coincident-point singularities being controlled (which requires an OPE — see C9). |
| C4 | $\mathrm{spec}(H) \subseteq \{0\} \cup [\Delta, \infty)$, $\Delta > 0$ AND $m < \infty$ | **PARTIAL** | The $\Delta > 0$ part is the main claim, conditional on Point C1. The $m < \infty$ part (a one-particle state of finite mass exists) is implicitly given by the spectral decomposition (the lattice has eigenvalues $E_n$ and the lightest excited state is $E_1 = \hat\Delta_k$, finite). The continuum lightest excited state is the lightest glueball, which has finite mass by the cluster expansion. Granted Point C1, this is satisfied. |
| C5 | No weak-existence-only solution | **PARTIAL** | The continuum limit *is* obtained via Banach–Alaoglu (a weak compactness argument), but the proof's "Addressing the Jaffe–Witten caution" remark explicitly invokes the §6.6 footnote 2 *exception*: properties of the limit are established by *additional techniques* (the RG telescoping sum), not just by compactness. The mass gap value $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ is shown to be subsequence-independent because both factors are determined by the convergent RG flow. **This is the right strategy in principle**, but its validity depends on the RG sum actually converging — i.e., on Point C1. |
| C6 | Local field operators in correspondence with $\mathrm{Tr}\,F_{ij}F_{kl}$ etc. | **FAIL** | The preprint constructs Schwinger functions of gauge-invariant lattice observables (plaquette traces, Wilson loops) but does NOT construct *operator-valued distributions* corresponding to the renormalized composite curvature polynomials. The lattice plaquette $s_P(x)/(a^4 g^2/(2N))$ does not converge to a finite operator on the GNS Hilbert space without multiplicative renormalization, and no renormalization $Z_O(a)$ is constructed. **GENUINE GAP** — see Point G4(a). |
| C7 | Short-distance match to perturbative AF | **FAIL** | The preprint's two-point function bound $|S_2(x,y)| \leq C|x-y|^{-2} e^{-\Delta|x-y|}$ uses the *free* propagator singularity, not the AF-corrected one. There is no comparison with the perturbative one-loop QCD result for $\langle \mathrm{Tr}\,F_{\mu\nu}(x) \mathrm{Tr}\,F_{\rho\sigma}(y)\rangle$, and the asymptotic-freedom logarithmic running of correlators is not matched. **GENUINE GAP** — see Point G4(b). |
| C8 | Stress tensor exists | **FAIL** | The preprint does not construct, mention, or even allude to a stress-energy tensor $T_{\mu\nu}(x)$. For gauge theories, the canonical stress tensor is gauge-non-invariant and an "improved" (gauge-invariant) version must be constructed. **Not addressed at all.** **GENUINE GAP** — see Point G4(c). |
| C9 | OPE with prescribed AF singularities | **FAIL** | The preprint asserts an OPE in the §5.7(f) "Coincident-point singularities" lemma but does not construct one. The lemma's bound is *conjectured* to follow from "the OPE", which has not been built. No OPE coefficients are computed, no short-distance expansion is established. **GENUINE GAP** — see Point G4(d). |
| C10 | RP preserved or recovered through every regularization step | **PASS** | RP holds for the Wilson action (Osterwalder–Seiler 1978). The KK enhancement preserves RP (Appendix D Lemma D.2 verifies this for the bond couplings via Bochner). RP is preserved in the continuum limit by the Portmanteau theorem (§5.7(f) OS3). Intermediate Balaban steps are not relied on for RP — only lattice RP and continuum RP via weak limits. See Point F2. |
| C11 | $\mathbb{T}^4 \to \mathbb{R}^4$ with volume-uniform mass gap | **PARTIAL** | The volume-cancellation lemma (§5.7(e)) shows the connected matrix element is volume-independent for $L \gg 1/m$. Finite-volume corrections are bounded by $e^{-mL}$. Moore–Osgood gives commutation of the $L \to \infty$ and $a \to 0$ limits *provided* uniform convergence in $L$ as $k \to \infty$, which depends on the K-vs-k issue (Point C1). The clarification of the mass parameter $m$ is correctly handled (avoiding circularity). Granted Point C1, this is satisfied. See Point F3. |

## Summary

| Verdict | Count | Items |
|:--------|:------|:------|
| **PASS** | 1 | C10 |
| **PARTIAL** | 5 | C2, C3, C4, C5, C11 |
| **FAIL** | 5 | C1, C6, C7, C8, C9 |

**Score: 1 PASS, 5 PARTIAL, 5 FAIL out of 11.**

The PARTIALs are mostly conditional on resolving the K-vs-k notation issue (Point C1). If that is resolved, several would upgrade to PASS.

The FAILs split into two groups:
- **C1** (all groups) is a *scope* failure — the proof addresses SU(N) only, with sketches for other groups.
- **C6, C7, C8, C9** are all aspects of the same *structural* failure: the proof constructs Schwinger functions but does not construct renormalized local field operators, a stress tensor, or an OPE, and does not match the short-distance AF perturbative behavior.

**Bottom line:** The proof, even granted the K-vs-k fix, addresses **roughly half** of the Clay requirements. The half it addresses (mass gap, OS axioms, RP) is the *headline* property, but the other half (local operators, stress tensor, OPE, AF matching) is the *structural QFT framework* that Jaffe–Witten asks for. The Clay statement is a *conjunction* of these requirements; failing any of them is a failure of the full statement.
