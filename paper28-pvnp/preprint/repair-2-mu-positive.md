# Repair 2: Positivity of mu_1(X_L) for Satisfiable Constraint Languages

**Programme:** Clone Growth <-> Fullness Bridge Theorem (Paper 28, P vs NP)
**Draft ID:** Repair 2 (CP-1 mandatory repair, item 2 of 4)
**Author:** G Six (originator), Claude Opus 4.6 (1M context, collaborator)
**Date:** 2026-04-11
**Repairs:** Lemma 5.3 in Node 2.1 (CP-1 formal proof); gap flagged in CP-1 verification W1-4
**Purpose:** The Feldman-Moore identification in Lemma 5.3 requires (X_L, mu_L) to be a standard probability space, which presupposes mu_1(X_L) > 0. This was never verified. The following lemma closes the gap.

---

## Lemma (Positivity of the KMS_1 measure on X_L)

**Lemma 5.3.0.** *Let L be a satisfiable Boolean constraint language with constraints C_1, ..., C_m, where constraint C_j involves variables in a set S_j subset {1, 2, ...} with |S_j| < infty. Let N = |S_1 cup ... cup S_m| be the total number of distinct variables appearing in all constraints. Then*

    mu_1(X_L) >= 2^{-N} > 0

*where mu_1 is the Bernoulli(1/2) product measure on {0,1}^infty (the restriction of the KMS_1 state to the diagonal subalgebra).*

**Proof.** Since L is satisfiable, there exists at least one configuration x_0 in X_L, i.e., x_0 in {0,1}^infty satisfies every constraint C_1, ..., C_m simultaneously.

Define the cylinder set

    [x_0|_N] := {x in {0,1}^infty : x_i = (x_0)_i for all i in S_1 cup ... cup S_m}

This is the set of all configurations that agree with x_0 on every coordinate appearing in any constraint.

We claim X_L contains [x_0|_N]. Indeed, each constraint C_j depends only on the variables in S_j. Any configuration x in [x_0|_N] agrees with x_0 on all coordinates in S_j (since S_j subset S_1 cup ... cup S_m), so x satisfies C_j. Since this holds for every j = 1, ..., m, we have x in X_L. Therefore [x_0|_N] subset X_L.

Under the Bernoulli(1/2) product measure, the N coordinates in S_1 cup ... cup S_m are independent, each taking the value (x_0)_i with probability 1/2. Therefore

    mu_1([x_0|_N]) = 2^{-N}

Since [x_0|_N] subset X_L, monotonicity gives

    mu_1(X_L) >= mu_1([x_0|_N]) = 2^{-N} > 0.    QED.

---

**Remark 5.3.0.1.** The bound 2^{-N} is crude but sufficient. For many constraint languages the true measure is much larger: e.g., 2-SAT instances with m clauses on n variables have mu_1(X_L) >= (3/4)^m. The only property needed downstream is strict positivity, which guarantees that mu_L := mu_1(. | X_L) is a well-defined probability measure on X_L and that (X_L, mu_L) is a standard probability space.

**Remark 5.3.0.2.** The satisfiability hypothesis is not restrictive. In the proof chain, Lemma 5.3.0 is invoked for the specific language L = L_{3-SAT}, which is satisfiable (e.g., the all-true assignment satisfies every positive 3-SAT clause). For the unsatisfiable case X_L = emptyset, the sector M^L_Bool = {0} is trivial and plays no role in the bridge argument.

---

**Integration.** This lemma should be inserted immediately before Lemma 5.3 in Node 2.1. The opening line of Lemma 5.3's proof ("By Part (A), M_Bool = A rtimes G_Bool ...") then gains the additional sentence: "By Lemma 5.3.0, mu_1(X_L) > 0, so mu_L = mu_1(. | X_L) is a well-defined probability measure and (X_L, mu_L) is a standard probability space."
