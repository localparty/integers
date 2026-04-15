# A1.05 — Preprint Risk

## Question

arXiv:2511.22755 is by Connes, Consani, and Moscovici but is not yet
refereed. Could there be errors in the preprint? What specific claims
does this proof rely on? If any of those claims turn out to be wrong,
does the entire chain collapse?

## Finding

Paper 13's dependence on CCM is **deep and irreducible**. The
specific CCM claims used are:

| CCM claim | Where Paper 13 uses it | Load-bearing? |
|:----------|:-----------------------|:--------------|
| Theorem 4.2: D' self-adjoint in T-inner product | Sec 3.3, 11.2 | YES (for spec ⊂ ℝ at each N) |
| Theorem 5.10(i): eigenvalues real/simple in even sector | Sec 3.4, 11.2, 12 | YES (for AE simplicity framework) |
| Theorem 5.10(ii): O(ρ^{−N}) approximation, ρ ≥ 4.27 | Sec 3.4 | PARTIAL (paper uses uniform CF decay, not the direct eigenvalue bound) |
| Theorem 5.10(iii): zeros of ξ̂_N = spec(D_log) | Sec 6, 10, 11 | YES (the Hurwitz argument is routed through this) |
| Lemma 7.2: ‖h_λ − h‖_∞ ≤ cλ^{−2} | Sec 6 (Lemma 6.3) | YES (ITPFI-triangle estimate) |
| Lemma 7.3: k̂_λ → Ξ uniformly on substrips | Sec 10 (Thm 10.1) | YES (core Hurwitz input) |
| Proposition 3.3: QW_λ bounded below | Appendix C.3 | YES (KLMN closability) |
| Proposition 4.2, 4.3, Lemma 4.1 (matrix elements) | Appendix A.2 | YES (construction of forms) |
| Definition 5.3 (even-simple hypothesis) | Sec 12 | YES (framework) |
| 10^{−55} numerical match | Sec 1, 3, 11, abstract | MOTIVATIONAL (not used in proof) |

If Theorem 5.10(iii) or Lemma 7.3 is wrong, the entire chain
collapses. Theorems 4.2 and 5.10(i) are standard enough in
structure (self-adjointness via CF, finite-dim spectral theory)
that independent reconstruction is plausible; Lemma 7.3 is the
genuinely novel piece, because it is the statement that makes the
Hurwitz argument possible at all.

## The "Preprint by Connes" argument

Paper 13 implicitly relies on the reputation of the authors
("Connes has spent 25+ years on this"). This is a social argument,
not a mathematical one. Two observations:

1. Connes' own 1999 paper on the trace formula approach (often
   cited as "Connes' programme") has been studied by experts for
   25+ years without producing a refereed RH proof. Connes himself
   has repeatedly described the programme as stuck at precisely the
   spectral-realization step that Paper 13 attempts to close.

2. The CCM paper is **very new** (2025). Experts have not had time
   to vet it. Theorem 5.10(iii) in particular is the kind of
   statement where a subtle identification can hide a
   hidden-hypothesis error that takes months of reading to
   locate.

Paper 13 is honest about this: the 8/10 confidence rating is
explicitly justified by CCM's preprint status.

## Collapse scenarios

- **CCM Theorem 5.10(iii) is wrong, or holds only with additional
  hypotheses not satisfied in the even sector.** Hurwitz
  identification fails. Layer 5 collapses. RH conclusion unreachable.

- **CCM Lemma 7.3 is wrong, or the convergence k̂_λ → Ξ holds in
  a weaker topology than claimed.** Uniform-on-compacts hypothesis
  of Hurwitz fails. Same outcome as above.

- **CCM Theorem 4.2 is wrong, or self-adjointness fails on the
  even-sector modification.** D_N is not self-adjoint; spec(D_N)
  is not necessarily real; the entire argument for spec(D_∞) ⊂ ℝ
  collapses. Same outcome.

- **"δ_N(ξ) ≠ 0" asserted-but-unproven item fails.** A degeneracy
  in the rank-one perturbation; Theorem 4.2 breaks. Collapse.

In every case, **Paper 13 has no independent backup**. There is
no alternative construction of D_N in the paper. The synthesis is
ITPFI + Boegli + Hurwitz, but the synthesis operates on operators
that CCM supplies.

## What would mitigate the risk

1. **Refereeing of CCM.** This is outside Paper 13's control but
   is the honest path to 9/10.

2. **Independent reconstruction of the relevant CCM results.** The
   paper does not attempt this. A refereeable version would either
   reconstruct Theorem 5.10(iii) and Lemma 7.3 from first
   principles, or cite a separate published source for each.

3. **Independent numerical reproduction of 10^{−55} at N = 6.**
   Paper 13 does not do this. It would be a straightforward several
   hours of mpmath work and would at least confirm that the CCM
   numerical claims can be independently verified.

## Verdict on this subpoint

**Load-bearing external dependency.** The proof is not self-
contained. At least four distinct CCM results are irreducibly
load-bearing, and all rest on an unrefereed 2025 preprint. Paper 13
acknowledges this in its 8/10 rating. The rating is honest, but
calling the result a *proof of RH* (as in the abstract and
Theorem 1.1) is stronger than the evidence supports. A reframing
as "conditional on CCM" would be more honest — see D2-ccm-dependency.
