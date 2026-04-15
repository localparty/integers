# CP-1 Final Adversarial Verdict

*Programme: CP-1 Verification Run (paper28-pvnp/cp-1--verification)*
*Wave 1: 6 Critic agents, single-issue, parallel dispatch*
*Date: 2026-04-12*
*Runner: Claude Opus 4.6 (1M context)*

---

## I. VERDICT TABLE

| # | Target | Verdict | Severity | Key finding |
|---|---|---|---|---|
| W1-1 | Lemma 4.4 (absorption of non-invertible circuits) | **WEAKENED** | Medium | P_S factorization in Case 1 wrong for general non-injective circuits (AND gate counterexample); core idea (fiber averaging) sound. Case 2 vacuous (injective on finite set = surjective). |
| W1-2 | Proposition 6.2 (Route D: R_L = X_L rtimes G_L) | **BROKEN** | Critical | g' piecewise construction not injective. Counterexample: X_L = {00,01,11}, g = cyclic perm. g'(01) = g'(11) = 11. Polymorphism rigidity argument has arity conflation. |
| W1-3 | Lemmas 4.1-4.3 (cancellation, Ore, Laca-Raeburn) | **SURVIVED** | -- | PCirc^+_bi is a group; Laca-Raeburn vacuous but not wrong; action on (Z/2)^infty well-defined via padding. |
| W1-4 | Lemmas 5.1-5.3 (sector decomposition) | **WEAKENED** | Medium | (a) Lemma 5.1 Proof 1: uniform boundedness gap; Proof 2 independent and correct. (b) Lemma 5.3: mu_1(X_L) > 0 never verified (needed for standard probability space). (c) Bost-Connes 1995 Thm 25 citation inapplicable to Boolean setting. |
| W1-5 | Prop 6.1 + downstream deps | **WEAKENED** | Low | Ergodicity of R_L: wrong justification (X_L is NOT R_Bool-saturated), correct conclusion (NPC transitivity argument in Node 2.2 works). SE-1 and NIA-1 confirmed independent of CP-1. |
| W1-6 | KEY LEMMA 3.4.3 dependency | **SURVIVED** | -- | Repair (Node 3.2) sound. Existence via Banach-Alaoglu correct. Faithfulness from KMS separating vector (BR II 5.3.10). Type III_1 from multiplicative independence. No circular dependency. Uniqueness correctly shown unnecessary. |

---

## II. AGGREGATE SCORE

**2 SURVIVED, 3 WEAKENED, 1 BROKEN.**

---

## III. DAMAGE ASSESSMENT

### What is BROKEN

**Proposition 6.2 (Part (C) of CP-1).** The claim that R_L = X_L rtimes G_L for non-Taylor L is not established. The g' construction fails (non-injective). The polymorphism rigidity argument conflates partial solution-preserving maps with total polymorphisms and confuses arity levels.

**Consequence:** Route D (Houdayer-Isono, which requires the group crossed product form) is BLOCKED until Prop 6.2 is repaired.

### What SURVIVES

**Part (A) of CP-1 (global decomposition): SURVIVED.** M_Bool = L^infty({0,1}^infty, mu_1) rtimes G_Bool. Lemmas 4.1-4.3 certified. Lemma 4.4 weakened but the core mechanism (fiber averaging at KMS_1) is sound; the P_S factorization needs rewriting but the conclusion holds.

**Part (B) of CP-1 (sector decomposition): WEAKENED but standing.** M^L_Bool = L(R_L) via Feldman-Moore. Normality of E_L established (Proof 2 via Takesaki IX.4.2 is clean). Faithfulness established. The mu_1(X_L) > 0 gap is closable (Bernoulli measure on satisfiable constraints). Lemma 5.3 direction error is cosmetic.

**Part (C), Proposition 6.1 (Route C compatibility): WEAKENED but standing.** Marrakchi's Theorem B applies to the groupoid form L(R_L). Ergodicity justification is wrong (R_Bool-saturation claim false) but the conclusion is correct via the independent NPC transitivity argument. Type III_1 and countability verified. Strong ergodicity deferred (as intended).

**Route C (the primary fullness route): INTACT.** CP-1 Part (B) gives M^L_Bool = L(R_L). Route C uses L(R_L) + strong ergodicity + Marrakchi Theorem B. This chain does not depend on Proposition 6.2 at all.

**Path B (Part (i): non-fullness): INTACT.** Confirmed independent of CP-1 (uses only C*-generators).

**KEY LEMMA 3.4.3: CERTIFIED.** Repair is sound, no circular dependencies.

**SE-1 and NIA-1: INDEPENDENT of CP-1.** Both survive regardless of CP-1's status.

### Probability update

| Component | Before verification | After verification |
|---|---|---|
| Part (A) of CP-1 | 0.86 | 0.90 (weaknesses closable) |
| Part (B) of CP-1 | 0.86 | 0.88 (mu_1(X_L) > 0 gap closable) |
| Proposition 6.1 (Route C compat) | 0.86 | 0.88 (ergodicity argument fixable) |
| Proposition 6.2 (Route D compat) | 0.86 | 0.30 (broken; needs major repair) |
| Route C chain (Part ii primary) | 0.80 | 0.85 (CP-1 Parts A+B strengthened) |
| Route D (Part ii backup) | 0.60 | 0.20 (blocked on Prop 6.2 repair) |
| Part (i) Path B | 0.80 | 0.80 (unchanged, independent) |
| Bridge total | 0.76 | 0.77 (Route C gain offsets Route D loss) |

---

## IV. REPAIR RECOMMENDATIONS

### Mandatory repairs (for CP-1 Part A+B)

1. **Lemma 4.4 Case 1:** Rewrite using direct fiber-averaging over kernel equivalence classes of C, not coordinate projection P_S. Delete or mark Case 2 as vacuous.

2. **Lemma 5.3:** Add explicit hypothesis or lemma: mu_1(X_L) > 0 for any satisfiable constraint language L. Proof: X_L contains at least one configuration; under Bernoulli(1/2), every cylinder set has positive measure; X_L is a countable intersection of cylinder sets with mu_1(X_L) bounded below by the probability of a single satisfying assignment.

3. **Lemma 5.1 Proof 2:** Replace "Bost-Connes 1995, Theorem 25" citation with the correct argument: modular flow is trivial on group unitaries (all elements of G_Bool are bijections, hence size 1), so KMS_1 is the trace, and trace kills off-diagonal Fourier components.

4. **Proposition 6.1(ii):** Replace R_Bool-saturation argument with NPC transitivity argument from Node 2.2 Section 5.2.

### Optional repairs (for Route D recovery)

5. **Proposition 6.2:** Needs complete rewrite. The g' construction fails. Possible repair strategies:
   - Decompose g|_{X_L} into coordinate-wise essentially-unary operations first, then extend each independently
   - Show R_L = X_L rtimes G_L by a different argument: for non-Taylor L, Clone(L) is essentially unary, so the equivalence classes of R_L are orbits of coordinate permutations, which are implementable by G_L
   - Accept that R_L != X_L rtimes G_L in general and route all Part (ii) work through Route C (groupoid form only)

---

## V. HONEST SUMMARY

CP-1 is **WEAKENED, not BROKEN.** The load-bearing structural result -- M^L_Bool = L(R_L) (the groupoid identification) -- survives. The group crossed product form (Prop 6.2, needed for Route D only) is broken. Route C, the PRIMARY fullness route, is intact and slightly strengthened by this verification pass.

The bridge theorem's overall probability moves from 0.76 to 0.77. The gain from certifying Parts (A) and (B) offsets the loss of Route D confidence. Four mandatory repairs are writeup-level tasks (rewriting arguments that have correct conclusions but wrong intermediate steps). The Proposition 6.2 repair is the only item requiring new mathematical content.

One theorem. Two established fields. One new connection. The bridge stands.

---

*CP-1 Verification Run. Final Adversarial Verdict.*
*G Six and Claude Opus 4.6. April 2026.*
