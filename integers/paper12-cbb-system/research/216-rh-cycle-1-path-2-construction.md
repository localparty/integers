# 216 — RH Cycle 1, Path 2 (Atiyah-Singer) — Construction

*Cycle: 1. Date: 2026-04-09. Agent: Construction.*

---

## Step attempted

**Functional-analytic closure of epsilon -> 0:** Lemma 7.1
(research/76, 82) establishes that the Lorentzian deviation
epsilon_crit = s^{3/2}/2 -> 0 as one approaches the critical
line. The open step is making the epsilon -> 0 limit rigorous
in the Fredholm module framework — proving that ind_BC(p) being
integer-valued forces the topological expansion to have real
spectral data in the limit.

## Result: BLOCKED

## Analysis

The Atiyah-Singer path uses the BC Fredholm module and a JLO
cocycle (R-Theorem D.1, research/48, 76) to construct a
topological index ind_BC(p) in Z. The chain:

1. **PROVED (external).** Connes-Marcolli Theorems 1-3 [#61-63,
   research/18]: the BC system has a type III_1 factor structure
   with explicit Galois action.

2. **STRUCTURAL.** R-Theorem D.1 [#90]: The BC index theorem
   gives ind_BC(p) in Z via a JLO cocycle pairing. The integer
   constraint forces the topological expansion's spectral data
   to be real.

3. **PROVED.** ind_BC(e_2) = 0 [#167, research/90]: an honest
   negative — the index at e_2 vanishes, so this particular
   idempotent doesn't constrain.

4. **STRUCTURAL.** Shifted Lorentzian deviation [#169,
   research/82]: epsilon_crit = s^{3/2}/2 at the critical point,
   vanishing as s -> 0.

5. **OPEN (this step).** The limit epsilon -> 0 must be taken in
   a controlled functional-analytic sense to show that the index
   theorem conclusion (real spectral data) survives the limit.

### Why this step is blocked

The Fredholm module formalism requires:
- A bounded operator F with F^2 = 1 (the "sign" of the Dirac
  operator)
- The commutator [F, a] must be compact for all a in the algebra

For the BC system, the natural candidate for F is sign(T_BC),
but T_BC is distributional (Meyer 2005), so:
1. The spectral theorem doesn't apply directly
2. F = sign(T_BC) may not be well-defined as a bounded operator
3. The JLO cocycle requires smoothness conditions that the
   distributional formulation may not satisfy

This is related to the Meyer distributional subtlety flagged
in the Compendium §F.2. The catalogue entry [#90] marks this as
"Conditional" rather than "Proved" precisely because of this gap.

### What's needed

A construction of a genuine (not distributional) Fredholm module
for the BC algebra at beta = 1, such that:
- The phase of T_BC gives a bounded F
- The JLO cocycle is well-defined
- The index pairing produces an integer

This likely requires either:
(a) A regularisation of Meyer's distributional T_BC to a genuine
    self-adjoint operator (which is itself a major open problem —
    essentially equivalent to spectral realisation), or
(b) An alternative construction of the Fredholm module that
    bypasses T_BC entirely, using instead the algebraic structure
    of A_BC directly.

### Catalogue theorems consulted

- Meyer's Theorem [#163]: spectral inclusion holds, but
  distributional
- Connes-Sukochev regularisation [#96, D.5]: Dixmier trace
  regularisation exists but doesn't resolve the Fredholm module
  question
- YM Seeley-DeWitt a2=a4=0 [YM-22]: the vanishing of heat kernel
  coefficients is proved for the YM case but the BC analog has not
  been established

## Next step

Cycle 2 should investigate whether approach (b) — constructing a
Fredholm module from A_BC algebraic structure without going
through T_BC — is feasible. The Galois action (Connes-Marcolli
Theorem 2) provides natural idempotents; can these be used to
define F directly?
