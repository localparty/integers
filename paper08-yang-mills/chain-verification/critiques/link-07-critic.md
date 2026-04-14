# Link 7 Critic: Newton decomposition — n ≥ 2 survives

**Verdict: BROKEN**

## Finding

Link 7 is a ghost link. The claim "Newton decomposition: n ≥ 2 survives / Proved (exact) / Algebraic identity" appears only in summary tables (§5.5.5 line 1561, IV.1 line 1913) and a one-sentence gloss in I3 (§Step 7). There is no proof anywhere in the preprint.

Worse: Appendix G (`G-multi-time-slice-analysis.md`) is an explicit self-audit of Newton decomposition as a mechanism. Its conclusion at §3.4 and §7.3 is unambiguous: "the Newton decomposition is the wrong tool for extracting Δ̂ factors" — all n ≥ 1 derivative terms yield zero in energy eigenstates by time-translation invariance, not Δ̂². The appendix was written to document and correct this error.

## Consequence

What the paper actually uses to eliminate n = 1 (the Tr(F³) / cubic operators) is C-symmetry (Link 6, §5.3.1 — proved). What it uses to show surviving operators have dev ≥ 2 is the spectral intermediate-state mechanism (Link 8–9, §5.5.4 and Part III.3 — proved). Link 7 as a standalone step — "Newton decomposition produces n ≥ 2 as an algebraic identity" — has no proof body and the one extended treatment explicitly repudiates it.

**Attack vector that breaks it:** Vector 1/4 combined. The Newton identity framework is invoked without stating whether it acts on power sums or monomials, without handling non-abelian cyclic-trace asymmetry (vector 3), and Appendix G proves the mechanism produces zero, not Δ̂² (vector 4). The link should be removed or merged into Link 6 (C-elimination already does the work).
