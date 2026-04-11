# Point D2 — Kolyvagin at rank 0: Verdict

**Weight:** MEDIUM
**Location in preprint:** §11
**Overall rigor label:** **[THEOREM]** (Kolyvagin 1990) + **[LEMMA]**
(application conditional on GRH from earlier steps)
**Overall verdict:** PASS, modulo the upstream GRH dependency

## Sub-question verdicts

- **(a) Kolyvagin hypotheses.** [THEOREM] — Kolyvagin 1990:
  for modular E/ℚ with L(E, 1) ≠ 0, rank(E(ℚ)) = 0 and Ш(E/ℚ)
  is finite. Modularity for CM curves is classical (Hecke theta
  series). Correctly stated.

- **(b) GRH → L(E, 1) ≠ 0 at analytic rank 0.** [LEMMA] — This
  is nearly tautological: analytic rank = 0 IS the definition
  of L(E, 1) ≠ 0. The subtlety GRH adds is ensuring the
  analytic rank is well-defined (no hidden zeros on the critical
  line at s = 1 that would be "hidden" if GRH failed). Since
  s = 1 has Re(s) = 1 ≠ 1/2, GRH (Re of zeros = 1/2) implies
  s = 1 is not a zero — which is exactly "analytic rank = 0
  iff L(E,1) ≠ 0." The logical chain is correct but the paper's
  narrative slightly oversells GRH's role here.

- **(c) BSD formula at rank 0.** [LEMMA] — With Kolyvagin's
  finiteness of Ш and Rubin 1991's p-part result for p > 7,
  the BSD formula at rank 0 for CM curves closes. The numerical
  check for y² = x³ − x (with corrected c_2 = 4 per LMFDB) goes
  through — see computation log C4. **Omega formula is written
  wrong** (C4a: Γ(1/4)²/(2π)^{3/2} is off by π, should be
  Γ(1/4)²/(2√(2π))), but numerical value is right.

## Combined finding

Kolyvagin at rank 0 is correctly cited and correctly applied
within its actual scope. Modularity for CM curves is classical
(no Wiles needed). The application depends on GRH providing
L(E, 1) ≠ 0 (which it does, conditionally on the upstream
chain).

**The BSD formula at rank 0 closes** for the canonical test
curve y² = x³ − x with c_2 = 4 (the corrected LMFDB value),
modulo an editorial error in the Ω formula.

## Impact on the claimed result

**Low severity.** This step is standard once GRH is in place.
The concerns are all upstream (Points A3, B2) in the
GRH-for-CM-L-functions chain.

## Action items

1. **Fix the Ω formula** in §13.3 (LC4): replace
   `Γ(1/4)²/(2π)^{3/2}` with `Γ(1/4)²/(2√(2π))`. Numerical value
   and BSD closure are correct.
2. Reinforce that Rubin 1991's p-part result applies only for
   p > 7, leaving the small-prime part of BSD needing separate
   citation.
