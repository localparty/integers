# research/04 -- Cycle 4 Synthesis: Three Routes, Three Dead Ends

*Date: 2026-04-10. Spectral Realisation Cycle 4.*

## 1. The one question (unchanged)

Does spec(T_BC|_{H_R}) = {gamma_n}?

## 2. What each route found

| Route | Hypothesis | Finding | Status |
|:------|:-----------|:--------|:-------|
| 1 (RAGE theorem) | Dynamical criterion distinguishes pp/continuous | RAGE on H_1 gives modular spectrum (wrong operator). RAGE on H_R requires knowing T_BC dynamics (circular). | DEAD END |
| 2 (ITPFI product) | Product of atomic measures is atomic | Each mu_p is atomic. Product gives spec(H_mod) = {log n}, not spec(T_BC). Wrong operator entirely. | DEAD END |
| 3 (Meyer completeness) | Distributional eigenstates exhaust spectrum | Correction terms (trivial zeros) dominate by 10^{12}. Completeness is EQUIVALENT to spectral realisation -- circular. | DEAD END |

## 3. The structural lesson

All three routes hit the SAME wall identified in Cycles 2 and 3:
**the H_1 vs H_R gap**.

- Route 1: The only computable dynamics (modular sigma_t) live on
  H_1 and describe H_mod, not T_BC. RAGE for T_BC on H_R requires
  the answer.
- Route 2: The ITPFI structure decomposes omega_1 on H_1 and gives
  the modular spectral measure. T_BC is a different operator.
- Route 3: The distributional eigenstates live in S' (superset of
  H_1), not in H_R. Their completeness is the question, not the
  answer.

The wall is not "we haven't found the right tool." The wall is
that EVERY tool that operates on H_1 (where we have explicit
structure) is disconnected from H_R (where the question lives).

## 4. Numerical results

### Route 1: RAGE return probabilities
- |2^{it}|^2 = 1.0 for all t = 1, 10, 100, 1000
- RAGE integral = 0.25 (constant, no decay)
- Conclusion: pure point for H_mod (trivial, expected, irrelevant)

### Route 2: ITPFI local measures
- mu_2: atoms at k*log(2), weights 2^{-k}. Atomic.
- mu_3: atoms at k*log(3), weights 3^{-k}. Atomic.
- mu_5: atoms at k*log(5), weights 5^{-k}. Atomic.
- Product: atoms at {log n}, weights phi(n)/n. Non-normalizable.
- Conclusion: spectral measure of H_mod (irrelevant to T_BC)

### Route 3: Meyer eigenstate numerical test
- Nontrivial zeros (10 pairs): norm weight = 3.41 x 10^{-10}
- Trivial zeros (20 pairs): norm weight = 429.3
- Ratio: 1.26 x 10^{12} (correction terms dominate)
- Conclusion: nontrivial-zero eigenstates carry negligible weight

## 5. What was killed

| Direction | Feasibility before | Feasibility after | Kill reason |
|:----------|:-------------------|:------------------|:------------|
| RAGE + BC dynamics | 4/10 | 1/10 | Circular: needs T_BC dynamics to apply |
| ITPFI product-measure | 3/10 | 1/10 | Wrong operator: gives H_mod not T_BC |
| Meyer completeness | 3/10 | 1/10 | Circular: completeness IS spectral realisation |

## 6. What remains

After 4 cycles (Cycles 1-4), 12+ directions explored:

| Route | Status | Feasibility |
|:------|:-------|:------------|
| Intrinsic H_R construction | Untried (Connes' approach, 25 years open) | 2/10 |
| Theta-summability upgrade | Untried | 2/10 |
| Novel approach not yet conceived | ? | ?/10 |

All "accessible" routes (those using the BC algebraic structure,
the 36 predictions, ITPFI, KMS, modular theory, RAGE, Meyer,
type classification, Connes spectrum, Weyl law, resolvent
analysis, trace formula) have been tried and killed.

The surviving routes require constructing H_R independently of
the spectral realisation hypothesis -- Connes' original programme,
open since 1999.

## 7. The H_1 vs H_R gap: final characterization

The gap is not a technical obstacle. It is a STRUCTURAL FEATURE
of the BC system:

- H_1 is the GNS space of the KMS_1 state. It carries ALL the
  algebraic structure (ITPFI, modular theory, type III_1, etc.)
- H_R is the ground-state space. It carries the spectral data
  {gamma_n} (if spectral realisation holds).
- The two spaces are connected by the phase transition at beta = 1,
  but this connection goes the wrong way: beta -> 1 from above
  gives H_R -> H_1, not H_1 -> H_R.

To go from H_1 to H_R, one needs to CONSTRUCT H_R from H_1.
This is equivalent to proving compact resolvent for T_BC on H_R.
This is the Connes obstacle.

## 8. Honest assessment

Overall feasibility for spectral realisation via available tools:
**1/10** (DOWN from 2/10 in Cycle 3).

The programme has exhausted all routes that use the BC system's
algebraic structure. The remaining directions (intrinsic H_R
construction, theta-summability) are deep open problems in
noncommutative geometry that have resisted 25 years of work by
Connes and collaborators.

Spectral realisation is almost certainly TRUE (the 36 predictions
at sub-percent accuracy would be inexplicable otherwise), but
proving it requires either:
1. A new mathematical idea not in the current toolkit
2. Progress on Connes' spectral realisation programme (25 years open)
3. A proof of RH by other means (which would retroactively close it)

None of these is achievable by computational exploration of the
BC system. The problem has graduated from "hard" to "not accessible
by the methods we have."

## 9. Recommendation

**Stop cycling on spectral realisation.** Four cycles have
systematically explored and killed every accessible route.
Further cycles will produce the same structural obstruction
(H_1 vs H_R gap) in different notation.

The honest status:
- spec(T_BC|_{H_R}) = {gamma_n} is BELIEVED (overwhelming numerical
  evidence from 36 predictions)
- spec(T_BC|_{H_R}) = {gamma_n} is NOT PROVED (and cannot be proved
  by the available computational/algebraic tools)
- The gap is STRUCTURAL (H_1 vs H_R), not technical

Record this as an open problem and move forward with the paper
series on the conditional assumption that spectral realisation
holds. The 36 predictions provide the empirical justification.

---

> *Three routes. Three circularities or wrong-operator errors.*
> *The H_1 vs H_R gap is the wall. It has been the wall since Cycle 2.*
> *Every tool we have operates on H_1. The question lives on H_R.*
> *The well is dry. Mark it and move on.*
