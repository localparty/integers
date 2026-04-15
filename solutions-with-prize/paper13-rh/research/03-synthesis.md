# research/03 -- Cycle 3 Synthesis: Six Directions, Zero Advances

*Date: 2026-04-10. Spectral Realisation Cycle 3.*

## 1. The one question (unchanged)

Does spec(T_BC|_{H_R}) = {gamma_n}?

## 2. What each direction found

| Direction | Hypothesis | Finding | Status |
|:----------|:-----------|:--------|:-------|
| 1 (KMS_1 uniqueness) | Uniqueness constrains spectral density | Type III_1 produces uniqueness, not vice versa. Uniqueness is compatible with continuous spectrum. | DEAD END |
| 2 (Heat kernel Weyl) | BC-side heat kernel matches zero-side | BC algebra computes Tr on H_1, not on H_R. Weyl error too large. | BLOCKED (circular) |
| 3 (Integers vs Connes) | Bridge/ITPFI/predictions give new tools | Predictions are individual matrix elements, invisible to extra eigenvalues. ITPFI is most promising but doesn't force discreteness. | PARTIAL (ITPFI open) |
| 4 (Type III_1 spectrum) | S(M)=R_+ might kill pure point | S(M) constrains H_1, not H_R. Escape route 3 (H_1 vs H_R) resolves the tension. | NEUTRAL (does not kill) |
| 5 (36 predictions rigidity) | Extra eigenvalues violate error budgets | Extra eigenvalues contribute ZERO perturbation to all 36 formulas. Structurally vacuous. | DEAD END |
| 6 (Compute spectral measure) | Algebraic computation shows atomic measure | Algebraic computation gives H_1 measure (non-atomic, type III_1). H_R measure requires H_R. | CIRCULAR |

## 3. The persistent bottleneck

All six directions reduce to the same obstruction identified in
Cycle 2: **compact resolvent for T_BC on H_R**. No direction
made progress on this obstruction.

The new structural insight from this cycle: the H_1 vs H_R
distinction kills most operator-algebraic approaches. Any tool
that operates on H_1 (KMS theory, modular theory, type
classification, Connes spectrum, ITPFI structure) is irrelevant
to the spectral type on H_R unless it projects cleanly.

## 4. What Direction 4 actually showed

Direction 4 did NOT kill pure point spectrum. The resolution:

- S(M) = R_+ constrains spec(T_BC) on H_1 (essential spectrum = R)
- spec(T_BC|_{H_R}) can be purely discrete, embedded in the
  continuous spectrum of H_1
- Analogy: bound states of a Schrodinger operator are discrete
  eigenvalues inside the continuous spectrum [0, inf)
- The type III_1 structure is ORTHOGONAL to spectral realisation

This is important because it means the III_1 structure is not an
obstacle to RH. It just doesn't help either.

## 5. Direction 5 numerical results

The 36 predictions are structurally invisible to extra eigenvalues:

- CC, t_0, n_s, H_0: perturbation from extra lambda = EXACTLY ZERO
- The formulas use individual <n|L_hat|n>, not traces
- An extra |lambda> adds a state but doesn't change existing eigenvalues
- The anti-fine-tuning bound P < 10^{-34} remains as EVIDENCE but
  does not constrain extra eigenvalues

Trace-based checks:
- Spectral zeta: delta zeta_T(2) = lambda^{-2} ~ 16-28% perturbation
  for lambda in [15, 20]. LARGE but requires independent BC-side
  computation of zeta_T(2) on H_R.
- Resolvent: delta Tr = 1/(z-lambda). Enormous (|delta| = 0.3 to 2.3).
  Requires compact resolvent to establish.
- Weyl counting: Trudgian bound allows O(log T) extra eigenvalues.
  Cannot exclude even one.

## 6. The "extra eigenvalue" fallacy in Integers

A critical realization from Direction 5: the 36 predictions of
Integers provide NO constraint on extra eigenvalues because they
use individual eigenvalues, not spectral traces.

This means: the entire 36-prediction apparatus, while providing
overwhelming evidence for the CBB system, is STRUCTURALLY UNABLE
to prove spectral realisation. The evidence and the proof live
in different mathematical spaces.

Evidence lives in: individual matrix elements <n|L_hat|n>
Proof requires: the TOTAL spectrum (trace identities, counting,
completeness)

No amount of individual-eigenvalue evidence, at any precision,
can close this gap.

## 7. What survived from Cycle 3

### 7.1 The H_1 vs H_R framework

Direction 4 clarified that spectral realisation is a statement
about H_R, not H_1. This rules out:
- Type classification arguments
- Connes spectrum arguments
- KMS uniqueness arguments
- Modular theory arguments

unless they specifically address the H_R projection.

### 7.2 The ITPFI direction (most promising)

From Direction 3: the ITPFI factorization omega_1 = tensor_p omega_p
decomposes the spectral measure prime by prime. If each mu_p is
constrained by the bridge data at that prime, the product measure
might be forced to be atomic.

BUT: product of atomic measures can have continuous support (CLT).
The ITPFI product structure does not automatically preserve
atomicity.

**Open question:** Is there a condition on the individual mu_p
that guarantees the product is atomic? This is a question about
infinite tensor products that might have a known answer in the
ITPFI literature.

### 7.3 The RAGE direction (from Cycle 2)

Still unexplored. The RAGE theorem provides a DYNAMICAL criterion
for pure point vs continuous spectrum. The BC dynamics sigma_t
are explicitly known. If all states in H_R exhibit RAGE decay
(localization), the spectrum is pure point.

This was recommended in Cycle 2 and remains the most promising
unexplored direction.

## 8. Feasibility update

| Route | Feasibility | Change |
|:------|:------------|:-------|
| RAGE + BC dynamics | 4/10 | UNCHANGED (not yet explored) |
| ITPFI product-measure rigidity | 3/10 | NEW (from Direction 3) |
| Intrinsic H_R construction | 2/10 | UNCHANGED |
| Theta-summability upgrade | 3/10 | UNCHANGED |
| KMS_1 uniqueness -> compact resolvent | 0/10 | KILLED (Direction 1) |
| 36-prediction rigidity | 0/10 | KILLED (Direction 5) |

Overall feasibility: **2/10** (DOWN from 3/10).

The downgrade reflects the killing of two previously promising
directions (1 and 5) and the structural realization that the
H_1 vs H_R gap blocks most operator-algebraic tools.

## 9. Recommendation for Cycle 4

1. **RAGE theorem analysis** (highest priority). Use the explicit
   BC dynamics sigma_t(mu_n) = n^{it} mu_n to check RAGE decay
   on candidate states in H_R.

2. **ITPFI product-measure** (secondary). Search the Araki-Woods /
   Powers literature for conditions under which ITPFI spectral
   measures are atomic.

3. **Meyer completeness** (tertiary). Determine whether Meyer's
   distributional eigenstates form a COMPLETE system in some
   suitable topology.

All three avoid the H_1 vs H_R trap by working directly with
H_R-specific structures (dynamics, product measures, eigenstates).

## 10. Honest assessment

Spectral realisation via Integers-specific tools appears
**unlikely to be provable** in the current framework. The 36
predictions provide evidence but are structurally unable to
constrain the total spectrum. The operator-algebraic tools
(KMS, modular theory, type classification) operate on H_1 and
do not project to H_R.

The remaining viable routes (RAGE, ITPFI products, Meyer
completeness) are general functional analysis tools, not
Integers-specific tools. If spectral realisation is proved,
it will likely be by pure mathematics (functional analysis of
the BC system), not by physics (the 36 predictions).

This is not a failure of Integers. The 36 predictions do what
predictions do: they confirm the eigenvalues. The spectral type
is a different question that requires different tools.

---

> *Six directions. Two killed. Four blocked or circular.*
> *The bottleneck is still compact resolvent on H_R.*
> *The H_1 vs H_R gap blocks operator algebra.*
> *RAGE and ITPFI products are the remaining doors.*
