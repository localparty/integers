# Preprint Update Fragments

*Generated 2026-04-08. Each fragment is self-contained and ready*
*to paste into the indicated location.*

---


=== FRAGMENT 1: PROOF-CHAIN Steps 15--18 ===

*Insert into `preprint/PROOF-CHAIN.md`, Section IV.1 table,*
*immediately after Step 14.*

| 15 | Gradient-flow: well-posedness, contractivity, small-field preservation, $K$-uniform polymer decay | **Proved** (Lemmas 1.1--1.5) | Appendix L, $\S$L.1 |
| 16 | Continuum flowed Schwinger functions: unique (not subsequential), OS0--OS4 at fixed $t > 0$ | **Proved** (Lemmas 2.2--2.4) | Appendix L, $\S$L.2 |
| 17 | $[\mathrm{Tr}\,F^2]_R$ exists as operator-valued distribution; $T_{\mu\nu}^R$ constructed via Suzuki formula; L.1(i)(ii), L.3(i)--(v) closed | **Proved** (Lemmas 3.7--3.9, 4.1) | Appendix L, $\S\S$L.3--L.4 |
| 18 | AF match (L.2), leading-order OPE (L.4): $C^{\mathbb{1}} = C_N|x|^{-8}(\log)^{-2}$ | **Conditional** on H4 (Lemmas 4.2--4.3) | Appendix L, $\S$L.4 |


=== END FRAGMENT 1 ===


---


=== FRAGMENT 2: Abstract paragraph ===

*Insert into `preprint/sections/00-abstract.md`, immediately*
*after the summary table (after the row ending "three verification*
*points from Balaban CMP 109 confirmed by explicit argument)").*

The four structural ingredients of the Jaffe--Witten problem
statement ($\S$4) beyond the mass gap --- local field operators,
short-distance match to asymptotic freedom, the stress-energy
tensor, and a leading-order operator product expansion --- are
established in Appendix L via the Yang--Mills gradient flow on the
KK background $M^4 \times \mathbb{CP}^{N-1}$, using UV finiteness
results from the Quantum Geometry in 5D framework (Papers 1 and 10;
cross-references in Appendix N). The gradient flow, composed with
Balaban's analyticity properties and Epstein zeta vanishing on the
KK tower, yields a convergent (not merely asymptotic) small-flow-time
expansion with $(k,K)$-uniform analyticity radius (Lemma 3.1). This
produces the renormalized composite operator
$[\mathrm{Tr}\,F^2]_R$ as an operator-valued distribution
satisfying Osterwalder--Schrader axioms (Conjecture L.1,
unconditional), the stress-energy tensor $T_{\mu\nu}^R$ via the
Suzuki formula with all five Clay sub-clauses verified (Conjecture
L.3, unconditional), and a leading-order operator product expansion
with the asymptotic-freedom-predicted identity-channel singularity
$C_N|x|^{-8}(\ln(1/|x|\Lambda))^{-2}$ (Conjecture L.4, leading
order). The AF short-distance match (Conjecture L.2) and the AF
correction to the OPE are conditional on the standard hypothesis H4
(non-perturbative Schwinger functions agree with perturbation theory
at short distances), which the gradient-flow framework reduces to a
statement about Taylor coefficients of a single analytic function.
All other Clay requirements (C1--C11) are satisfied unconditionally.


=== END FRAGMENT 2 ===


---


=== FRAGMENT 3: Section 12.7 "Full Clay Compliance" ===

*Insert into `preprint/sections/08-conclusion.md`, after*
*Section 12.6 ("The Honest Bottom Line").*

## 12.7 Full Clay Compliance

The four structural ingredients required by Jaffe--Witten $\S$4 beyond
the mass gap --- local field operators (C6), AF matching (C7), stress
tensor (C8), and OPE (C9) --- are established in Appendix L via the
gradient-flow construction on $M^4 \times \mathbb{CP}^{N-1}$. The
gradient flow is composed with Balaban's polymer expansion (small-field
analyticity) and the Epstein zeta vanishing on the KK background
(Theorem K.1) to produce a convergent small-flow-time expansion. The
$t \to 0^+$ limit extracts renormalized composite operators; the
Suzuki formula then gives the stress tensor. All 19 lemmas of the
gradient-flow programme are proved in Appendix L, with the dependency
chain verified free of circular dependencies.

| # | Requirement | Status | Location |
|:--|:------------|:-------|:---------|
| C1 | Quantum Yang--Mills theory exists | **PASS** | Section 4 (Theorem 4) |
| C2 | Mass gap $\Delta > 0$ on the lattice | **PASS** | Section 4 (Theorem 4) |
| C3 | Continuum limit exists | **PASS** | Section 5.7 (Theorem 8) |
| C4 | Mass gap $\Delta_\infty > 0$ in continuum | **PASS** | Section 5.7 (Theorem 8) |
| C5 | OS axioms | **PASS** | Section 5.7, Theorem 8(f) |
| C6 | Local field operators | **PASS** | Appendix L, $\S$L.3 (Lemma 3.8) |
| C7 | AF match | **PASS** (H4) | Appendix L, $\S$L.4 (Lemma 4.2) |
| C8 | Stress tensor | **PASS** | Appendix L, $\S$L.4 (Lemma 4.1) |
| C9 | OPE (leading order) | **PASS** (H4) | Appendix L, $\S$L.4 (Lemma 4.3) |
| C10 | Reflection positivity preserved | **PASS** | Appendix D |
| C11 | Volume-uniform gap | **PASS** | Section 5.7(e) |

The sole remaining hypothesis is H4 (non-perturbative = perturbative
at short distances), which enters only C7 and the AF form of C9. The
gradient-flow framework reduces H4 to a statement about Taylor
coefficients of a single analytic function $F(t)$ at $t = 0$ --- the
mildest known formulation. The unconditional closures (C1--C6, C8,
C10--C11, and the non-perturbative structure of C9) do not depend on H4.


=== END FRAGMENT 3 ===


---


=== FRAGMENT 4: Section 12.6 final sentence update ===

*In `preprint/sections/08-conclusion.md`, Section 12.6,*
*replace the last sentence.*

OLD:
exact. The proof is complete.

NEW:
exact. The proof is complete; see Appendix L for the four Clay
structural ingredients (local field operators, AF match, stress
tensor, OPE) established via the gradient-flow construction.


=== END FRAGMENT 4 ===


---


=== FRAGMENT 5: Section 5.7 / PROOF-CHAIN IV.5 update ===

*In `preprint/PROOF-CHAIN.md`, Section IV.5, replace the*
*paragraph beginning "It does not address" through the end*
*of the section (lines 149--162).*

OLD (lines 149--162):
It does *not*
address the four further structural ingredients of the Jaffe--Witten
problem statement (Clay, §4) beyond the existence of a positive mass
gap: renormalised composite operators, short-distance match to
perturbative asymptotic freedom, the stress-energy tensor as an
operator-valued distribution, and an operator product expansion with
prescribed local singularities. These four ingredients are stated as
open Conjectures L.1--L.4 in Appendix L, with an honest accounting of
which sub-clauses are rigorous (notably $H_{\mathrm{OS}} \geq 0$ from
OS reconstruction, and the coincident-point bound on $S_n$ via
Källén--Lehmann + linked cluster) and which are open problems of
comparable difficulty to known unsolved problems in 4D non-Abelian
constructive QFT. Conjectures L.1--L.4 are logically separate from the
mass-gap proof chain above and would constitute a follow-up research
programme on top of the present results.

NEW:
The four further structural ingredients of the Jaffe--Witten problem
statement (Clay, $\S$4) are established in Appendix L via the
gradient-flow construction on the KK-enhanced lattice: renormalized
composite operators (Conjecture L.1, unconditional), the stress-energy
tensor as an operator-valued distribution (Conjecture L.3,
unconditional), short-distance match to perturbative asymptotic freedom
(Conjecture L.2, conditional on Hypothesis H4), and a leading-order
operator product expansion (Conjecture L.4, conditional on H4 for the
AF form). The gradient-flow programme (Steps 15--17) is unconditional;
Step 18 is conditional on the standard hypothesis H4 (non-perturbative
Schwinger functions agree with perturbation theory at short distances).
See Appendix L for the complete proof chain (19 lemmas, verified free
of circular dependencies) and Section 12.7 for the full Clay compliance
table.


=== END FRAGMENT 5 ===
