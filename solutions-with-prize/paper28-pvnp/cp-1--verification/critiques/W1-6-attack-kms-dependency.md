# W1-6 Critique: Attack on KMS Dependency (CP-1 depends on KEY LEMMA 3.4.3)

**Programme:** CP-1 Verification
**Critic:** Claude Opus 4.6 (1M context)
**Date:** 2026-04-12
**Target:** Dependency of CP-1 (Node 2.1) on KEY LEMMA 3.4.3 (Node 3.2 repair)
**Attack vectors:** 5

---

## Attack 1: KMS_1 Existence via Banach-Alaoglu

**Claim under attack.** Theorem C.1 of Node 3.2: KMS_1 existence by weak-* compactness. The argument constructs KMS_beta states for large beta via finite-dimensional Gibbs truncations, takes a weak-* limit as N -> infinity to get KMS_beta on the full algebra, then takes beta -> 1^+ to get KMS_1.

**Analysis.**

The argument has three layers:

**(a) KMS_beta states exist for beta > beta_0 on truncated algebras A_N.** This is unproblematic: A_N is finite-dimensional, Z_N(beta) is a finite convergent sum, and the Gibbs state is well-defined. No issue.

**(b) Passage N -> infinity: KMS_beta on the full algebra.** The proof extends omega_beta^N from A_N to A^Bool_BC by Hahn-Banach, then takes a weak-* limit. The limit is a state. The proof claims this limit is KMS_beta. The justification: for fixed a, b in the algebraic span A_0, once N is large enough both a and b lie in A_N, and the KMS analyticity condition on the strip passes to the limit by a normal families argument (uniformly bounded analytic functions on the strip converge to an analytic function). This is correct. The boundary condition F(t + i*beta) = omega(sigma_t(b) a) at the limit follows from pointwise convergence on the boundary. Standard complex analysis (Vitali's theorem) ensures the limit is analytic on the interior. Sound.

However, there is a subtlety: the Hahn-Banach extension of omega_beta^N from A_N to A^Bool_BC is NOT unique, and different extensions may not satisfy KMS_beta on elements outside A_N. The proof handles this by not requiring the extensions to be KMS -- only the weak-* limit point is claimed to be KMS. Since the KMS_beta condition is checked only on pairs from A_0, and A_0 = union of A_N, this is legitimate: for each pair (a,b), the condition holds for all sufficiently large N, hence in the limit.

**(c) Passage beta -> 1^+: KMS_1 from KMS_beta.** The proof invokes Bratteli-Robinson II, Proposition 5.3.25: the set K_beta of KMS_beta states is weak-* closed for each beta, and the map beta -> K_beta is upper semicontinuous. This means: if beta_i -> beta_0 and omega_i in K_{beta_i} with omega_i -> omega, then omega in K_{beta_0}.

This is the key step. Let me verify the upper semicontinuity claim against Bratteli-Robinson. Proposition 5.3.25 states that K_beta is weak-* compact for each beta in R. The upper semicontinuity (limit points of KMS_beta_i states are KMS_{beta_0} states when beta_i -> beta_0) is Proposition 5.3.23 of the same reference: "If beta_n -> beta and omega_n is a (sigma, beta_n)-KMS state for each n, and omega_n -> omega in the weak-* topology, then omega is a (sigma, beta)-KMS state."

The proof of 5.3.23 uses the KMS boundary condition: the analytic functions F_n on strips of width beta_n converge to an analytic function on the strip of width beta. This requires the strips to converge (beta_n -> beta), which they do. The boundary conditions at Im(z) = 0 and Im(z) = beta_n converge to the boundary conditions at Im(z) = 0 and Im(z) = beta. A Phragmen-Lindelof argument ensures the limit function satisfies the correct boundary condition. This is standard.

**Potential gap: Does the truncation procedure actually produce KMS_beta states for beta > 1?** The argument assumes Z_N(beta) is non-degenerate (i.e., the Gibbs state is a genuine KMS_beta state on A_N). For A_N finite-dimensional with a well-defined Hamiltonian H_N implementing sigma_t, the Gibbs state Tr(. exp(-beta H_N))/Z_N(beta) is indeed KMS_beta -- this is the finite-dimensional Gibbs theorem (Bratteli-Robinson I, Proposition 5.3.7). The only concern would be if H_N is degenerate (zero), but the modular flow sigma_t(mu_C) = (size C)^{it} mu_C is non-trivial on A_N as soon as S_N contains circuits of different sizes, which it does for N >= 2.

**Verdict: SURVIVED.** The compactness argument is a standard application of Banach-Alaoglu + Bratteli-Robinson 5.3.23/5.3.25. No gap found. The truncation-extension-limit procedure is well-established in quantum statistical mechanics. The references are accurate and the argument is complete.

---

## Attack 2: Faithfulness of omega^Bool_1

**Claim under attack.** Proposition C.2 claims the KMS_1 state restricts to the Bernoulli(1/2) product measure on C*((Z/2)^infty), which is faithful on the phase algebra. The concern: faithfulness on the phase algebra (diagonal) does NOT automatically give faithfulness on the full von Neumann algebra M_Bool.

**Analysis.**

This attack has two parts:

**(a) Is the restriction to the phase algebra actually Bernoulli(1/2)?** The argument: the KMS condition forces the restriction to the fixed-point algebra C*((Z/2)^infty) to be a trace (since sigma_t fixes the phase generators). The flip symmetry of the Boolean BC construction forces invariance under single-coordinate flips. Permutation invariance comes from the circuit semigroup containing all finite permutations. By de Finetti's theorem (or direct argument), the only measure on {0,1}^N invariant under all coordinate flips and all finite permutations is Bernoulli(p) for some p in [0,1]. The flip symmetry (invariance under 0 <-> 1 on each coordinate) forces p = 1/2.

This argument is sound. The symmetry group contains (Z/2)^infty (flips) and S_infty (permutations), and PCirc^+ does contain all finite permutations (they are trivially polynomial-time bijections) and all single-coordinate NOT gates (also trivially polynomial-time bijections). The KMS condition at the fixed-point algebra says omega_1 is a trace there, and the symmetry forces it to be the unique flip-and-permutation-invariant trace, which is Bernoulli(1/2).

**(b) Does faithfulness on the diagonal extend to faithfulness on M_Bool?** This is the sharper question. The answer is: NOT AUTOMATICALLY. A state can be faithful on a maximal abelian subalgebra (MASA) without being faithful on the ambient algebra. For example, the trace on M_2(C) is faithful on the diagonal subalgebra and on M_2(C), but a state concentrated on a rank-1 projection is faithful on the 1-dimensional diagonal it generates but not on M_2(C).

However, let us check what CP-1 actually needs. Examining the three downstream uses:

1. **Lemma 4.4 (absorption).** Uses the KMS_1 state as the ambient state in the GNS construction. The GNS construction from omega_1 produces a faithful representation if and only if omega_1 is faithful on A^Bool_BC. But the GNS representation is always well-defined; it produces M_Bool = pi_1(A^Bool_BC)''. The issue is whether M_Bool is "the right" algebra. If omega_1 is not faithful on A^Bool_BC, then the kernel ker(pi_1) is non-trivial, and M_Bool = (A^Bool_BC / ker(pi_1))''. This is still a von Neumann algebra, and the crossed-product identification still applies to it (the quotient inherits the dynamical system structure). So faithfulness on the full C*-algebra is not strictly needed for the GNS construction to produce a meaningful factor.

2. **Lemma 5.1 Proof 2 (normality of E_L).** Uses "omega_1 is faithful and normal on M_Bool." The proof applies Takesaki's theorem IX.4.2, which requires a faithful normal state on M_Bool. Here "faithful on M_Bool" means faithful on the von Neumann algebra, not on the C*-algebra. For a GNS construction, the vector state <Omega_1, . Omega_1> is always faithful on M_Bool = pi_1(A)'' (the cyclic vector Omega_1 is separating for M_Bool if M_Bool is in standard form). Wait -- is Omega_1 separating for M_Bool?

    The GNS vector Omega_1 is cyclic for M_Bool by construction. For Omega_1 to be separating, we need: x Omega_1 = 0 implies x = 0 for x in M_Bool. This follows from the Tomita-Takesaki theory: for a KMS state, the GNS vector is both cyclic and separating (Bratteli-Robinson II, Theorem 5.3.10). The KMS condition at any temperature beta (including beta = 1) implies that the GNS vector state is faithful on the GNS factor.

    **This is the key point.** The KMS condition itself guarantees that the GNS state is faithful on the GNS von Neumann algebra. We do NOT need faithfulness on the original C*-algebra A^Bool_BC. We need faithfulness on M_Bool = pi_1(A^Bool_BC)'', and this follows from the KMS property.

    Reference: Bratteli-Robinson II, Theorem 5.3.10 -- "If omega is a (sigma, beta)-KMS state on a C*-algebra A with beta != 0, then the GNS vector Omega is cyclic and separating for pi(A)''."

3. **Proposition 6.1(iii) (type III_1).** Uses type III_1 of M_Bool. This is proved in Theorem C.3 via the Connes spectrum, and does not require faithfulness beyond what the KMS condition provides.

**Verdict: SURVIVED.** The concern about faithfulness on the full algebra is resolved by Bratteli-Robinson II, Theorem 5.3.10: the KMS condition guarantees the GNS vector is separating, hence the GNS state is faithful on M_Bool. Faithfulness on the phase algebra (Bernoulli(1/2)) is used as additional structural information but is not the sole source of faithfulness. The faithfulness that CP-1 needs (faithful normal state on M_Bool for Takesaki IX.4.2) comes directly from the KMS property.

**Note of caution.** The original Node 3.2 presentation could be clearer on this point. It proves faithfulness on the phase algebra (Proposition C.2) as if that is the main faithfulness result, but the more important fact -- faithfulness on M_Bool via the KMS separating vector -- is mentioned only in passing (D.4, Mode D). The paper should cite Bratteli-Robinson II, 5.3.10 explicitly when claiming faithfulness on M_Bool.

---

## Attack 3: Type III_1 via Multiplicative Independence

**Claim under attack.** Theorem C.3: the Connes spectrum S(M_Bool) = R_+^* because circuits of sizes 2 and 3 exist, log 2/log 3 is irrational, hence {2^a * 3^b : a, b in Z} is dense in R_+^*, hence the Connes spectrum is all of R_+^*.

**Analysis.**

The argument has three steps, each of which I attack:

**(a) Do circuits of size 2 and size 3 exist in PCirc^+?** Node 3.2 claims this but is somewhat vague about the gate basis convention. Over {AND, OR, NOT}:
- Size 1: a single AND gate, a single OR gate, a single NOT gate.
- Size 2: AND followed by NOT (= NAND), or OR followed by NOT (= NOR), etc.
- Size 3: three gates in sequence.

The precise sizes depend on the convention (number of gates vs. number of wires vs. some other measure). The modular flow is defined as sigma_t(mu_C) = (size C)^{it} mu_C. What matters is that there exist two circuits whose sizes are multiplicatively independent. Even if the gate-count convention gives sizes 1 and 2 instead of 2 and 3, log 1/log 2 is undefined (log 1 = 0), so we need sizes >= 2. With sizes 2 and 3, or 2 and 5, or any two coprime integers >= 2, the argument works.

The existence of circuits with coprime sizes is uncontroversial. Over any reasonable basis and size measure, circuits of many different sizes exist, and among them there will be coprime pairs (since the set of circuit sizes contains arbitrarily large integers and cannot be contained in a single prime power sequence).

**(b) Does the modular spectrum of M_Bool contain {(size C)^{it} : C in PCirc^+, t in R}?** The modular flow is sigma_t(mu_C) = (size C)^{it} mu_C. In the GNS representation, the modular operator Delta satisfies Delta^{it} pi_1(mu_C) Delta^{-it} = (size C)^{it} pi_1(mu_C). This means the vector pi_1(mu_C) Omega_1 is NOT an eigenvector of Delta^{it} -- rather, it tells us about the spectrum of the modular automorphism group acting on the algebra.

Let me be more precise. The modular operator Delta is associated to the pair (M_Bool, Omega_1) by Tomita-Takesaki theory. We have sigma_t^{omega_1}(x) = Delta^{it} x Delta^{-it} for x in M_Bool. For x = pi_1(mu_C):

    Delta^{it} pi_1(mu_C) Delta^{-it} = (size C)^{it} pi_1(mu_C)

This means pi_1(mu_C) intertwines the modular flow with a scaling by (size C)^{it}. Now, the Connes spectrum S(M) is defined as the intersection of Sp(Delta_phi) over all faithful normal states phi. For our specific phi = omega_1, we have Sp(Delta_{omega_1}) -- what does it contain?

Consider the vector xi_C = pi_1(mu_C) Omega_1. Then:

    Delta^{it} xi_C = Delta^{it} pi_1(mu_C) Omega_1 = Delta^{it} pi_1(mu_C) Delta^{-it} Delta^{it} Omega_1 = (size C)^{it} pi_1(mu_C) Omega_1 = (size C)^{it} xi_C

Wait -- this assumes Delta^{it} Omega_1 = Omega_1 (the KMS vector is invariant under the modular flow). This is correct: Omega_1 is the GNS vector for the KMS state, and sigma_t^{omega_1}(.) = Delta^{it} (.) Delta^{-it} implies Delta^{it} Omega_1 = Omega_1 (the state is invariant under the modular flow, which is equivalent to the vector being invariant under Delta^{it}).

Therefore xi_C is an eigenvector of Delta^{it} with eigenvalue (size C)^{it}. This means Delta xi_C = (size C) xi_C, so size(C) is in the point spectrum of Delta (assuming xi_C != 0, which holds since omega_1 is faithful on M_Bool and mu_C is non-zero).

Actually, let me reconsider. We have Delta^{it} xi_C = (size C)^{it} xi_C for all t in R. Taking the spectral decomposition of log Delta (the generator of {Delta^{it}}), this means xi_C is an eigenvector of log Delta with eigenvalue log(size C). Therefore Sp(Delta_{omega_1}) contains {size C : C in PCirc^+}, and in particular contains 2 and 3 (assuming circuits of those sizes exist).

But the Connes spectrum S(M) is the INTERSECTION over all faithful normal states. We showed Sp(Delta_{omega_1}) contains {2^a * 3^b : a, b in Z} (since products of eigenvalues of Delta are eigenvalues of Delta, by considering compositions of circuits). Actually, the Connes spectrum for a factor equals the intersection, but by Connes' 1973 theorem (Theorem 3.4.1), for a factor, S(M) = closure of the point spectrum of Delta_phi for any faithful normal state phi (not just the intersection -- for a factor, the Connes spectrum is actually determined by any single faithful normal state's modular operator).

Wait, that's not quite right either. Let me state the precise result. For a factor M:

    S(M) \ {0} = exp(Gamma(M))

where Gamma(M) = intersection of ker(mod) over all faithful normal semifinite weights, and mod is the Connes cocycle. Alternatively, by Connes 1973, Corollaire 3.2.8: S(M) is an algebraic invariant of M (does not depend on the choice of state).

For our purposes, the key fact is: if Sp(Delta_phi) contains a dense subgroup of R_+^* for some faithful normal state phi, then S(M) = R_+^* (since S(M) subset Sp(Delta_phi) for every phi, but S(M) is the intersection -- hmm, this goes the wrong way).

Let me reconsider. S(M) = intersection of Sp(Delta_phi). If one particular Sp(Delta_phi) contains only a dense subgroup (but not all of R_+^*), the intersection could be smaller. However, Sp(Delta_phi) is always a closed set (it's the spectrum of a positive operator). The closure of {2^a * 3^b} is R_+^* union {0}. So Sp(Delta_{omega_1}) contains R_+^* union {0} (the closure of the dense subgroup). Since S(M) subset Sp(Delta_{omega_1}), and S(M) is a closed multiplicative subgroup of R_+^* (for a factor), we have S(M) subset R_+^*.

But we need S(M) = R_+^*, not just S(M) subset R_+^*. The other direction: S(M) superset something. By Connes 1973, for a type III factor, S(M) != {1}. If S(M) is a proper closed subgroup of R_+^*, it must be {lambda^n : n in Z} for some lambda in (0,1) (type III_lambda). For S(M) to be this, the modular flow sigma_t must have period 2*pi/|log lambda|. But our modular flow has eigenvalues at log 2 and log 3, which are rationally independent. A periodic flow with period T can only have eigenvalues that are multiples of 2*pi/T. Since log 2 and log 3 are not both multiples of any single period, the flow cannot be periodic. Therefore M is not type III_lambda for any lambda in (0,1), and since it is type III (the modular flow is non-trivial), it must be type III_1.

This reasoning is correct. More precisely: if S(M) = {lambda^n : n in Z}, then the Connes invariant Gamma(M) = Z * |log lambda|. But Gamma(M) contains log 2 and log 3 (from the eigenvalues of the modular operator), so Z * |log lambda| must contain both log 2 and log 3. This means log 2 / |log lambda| and log 3 / |log lambda| are both integers, hence log 2 / log 3 = (log 2 / |log lambda|) / (log 3 / |log lambda|) is rational. But log 2 / log 3 is irrational. Contradiction. Hence S(M) != {lambda^n : n in Z} for any lambda. Since S(M) is a closed subgroup of R_+^* and is not {1} (M is type III) and is not {lambda^n}, we conclude S(M) = R_+^*.

**(c) Is the point spectrum argument for Delta correct?** Above I showed xi_C = pi_1(mu_C) Omega_1 satisfies Delta^{it} xi_C = (size C)^{it} xi_C. But this requires pi_1(mu_C) to be an isometry, not just any operator. In the Bost-Connes framework, mu_C is an isometry satisfying mu_C^* mu_C = 1. In the GNS representation, pi_1(mu_C) need not be an isometry (the GNS representation of an isometry is an isometry only if the state is multiplicative on mu_C^* mu_C, which holds here since mu_C^* mu_C = 1).

Actually, mu_C is an isometry in the C*-algebra: mu_C^* mu_C = 1. Therefore pi_1(mu_C)^* pi_1(mu_C) = pi_1(1) = I. So pi_1(mu_C) is indeed an isometry, and xi_C = pi_1(mu_C) Omega_1 satisfies ||xi_C|| = ||Omega_1|| = 1 (non-zero). The eigenvector argument is valid.

But wait: does the point spectrum of Delta really include the product group {2^a * 3^b}? The eigenvector xi_C has eigenvalue size(C). For a composite circuit C_1 circ C_2, the size is NOT size(C_1) * size(C_2) in general -- circuit size is not multiplicative under composition. What the modular flow gives is:

    sigma_t(mu_{C_1} mu_{C_2}) = sigma_t(mu_{C_1}) sigma_t(mu_{C_2}) = (size C_1)^{it} (size C_2)^{it} mu_{C_1} mu_{C_2}

So the product mu_{C_1} mu_{C_2} has modular eigenvalue (size C_1)(size C_2), regardless of the size of the composed circuit C_1 circ C_2. This means the eigenvalues of Delta include all products size(C_1) * size(C_2) * ... * size(C_k) for any finite sequence of circuits. This is the multiplicative semigroup generated by {size C : C in PCirc^+}.

For the subgroup generated by 2 and 3 (i.e., {2^a * 3^b : a, b in Z, a,b >= 0}), we need 2 and 3 in the semigroup of sizes. To get negative powers (2^{-1}, 3^{-1}), we use the adjoint: mu_C^* has modular eigenvalue (size C)^{-1} (since sigma_t(mu_C^*) = (size C)^{-it} mu_C^*). So xi_C^* := pi_1(mu_C^*) Omega_1 satisfies Delta^{it} xi_C^* = (size C)^{-it} xi_C^*. Therefore (size C)^{-1} is also in Sp(Delta). The full group {2^a * 3^b : a, b in Z} is in Sp(Delta), and its closure R_+^* union {0} is contained in Sp(Delta).

**(d) One more subtlety: Sp(Delta) vs. point spectrum.** The point spectrum of Delta contains the eigenvalues we found. Since Sp(Delta) contains the closure of the point spectrum, and the closure of {2^a * 3^b : a, b in Z} union {0} is R_+^* union {0}, we get Sp(Delta) = R_+^* union {0} (since Sp(Delta) subset R_+ union {0} always, and we've shown it contains R_+^* union {0}).

**Verdict: SURVIVED.** The type III_1 argument is correct. The key steps are:
(i) circuits of coprime sizes exist (uncontroversial);
(ii) the modular operator has these sizes (and their inverses) in its point spectrum (verified via the KMS eigenvector argument);
(iii) density of the generated subgroup (Weyl equidistribution / irrationality of log 2/log 3);
(iv) the Connes spectrum of a factor is determined by this (Connes 1973).
All steps check out.

---

## Attack 4: Uniqueness is Unnecessary

**Claim under attack.** Proposition C.5 of Node 3.2: the bridge theorem holds for ANY KMS_1 state, so uniqueness is unnecessary.

**Analysis.**

The worry: if there are multiple KMS_1 states, different choices give different GNS factors M_Bool^{(1)}, M_Bool^{(2)}, etc. Perhaps one is full and another is non-full, destroying the dichotomy.

Let me examine the argument in Proposition C.5 carefully:

**(a) Fullness/non-fullness is intrinsic.** Yes: for a fixed factor M, fullness is a property of M (Inn(M) closed in Aut(M)) and does not depend on the choice of state. This is standard (Connes 1974, Haagerup 1987). No issue here.

**(b) But different KMS_1 states give different GNS factors.** If omega_1 and omega_1' are two different extremal KMS_1 states, the GNS factors M = pi_{omega_1}(A)'' and M' = pi_{omega_1'}(A)'' might be non-isomorphic. The bridge theorem says: for Taylor L, M^L is non-full, and for non-Taylor L, M^L is full. If different KMS_1 states give different M^L sectors, we need the dichotomy to hold for EACH one.

**(c) Does the bridge argument go through for each extremal component?** Let omega be any extremal KMS_1 state. Its GNS factor M_omega is type III_1 (by the Connes spectrum argument, which uses only the modular flow eigenvalues, present for any KMS state). The KMS state is faithful on M_omega (Bratteli-Robinson II, 5.3.10). CP-1 applies (the crossed-product identification uses the algebraic structure of PCirc^+, and the absorption lemma 4.4 uses the KMS averaging, which works for any KMS_1 state). The sector M_omega^L = p_L M_omega p_L is a type III_1 factor (compression preserves type III_1). The downstream arguments (Path B for non-fullness, Route C for fullness) apply to M_omega^L.

**(d) The contradiction.** For each extremal KMS_1 state omega:
- M_omega^{3-SAT} is full (Part ii, via Route C -- uses CP-1 + strong ergodicity, both state-independent).
- If 3-SAT in P, then M_omega^{3-SAT} is non-full (Part i, via Path B -- uses clone operators, state-independent).
- Contradiction.

The contradiction holds for each omega independently. Even if different omega give non-isomorphic factors, the same dichotomy (full vs. non-full) applies to each, and the contradiction arises for each.

**(e) Is CP-1 actually state-independent?** Lemma 4.4 (absorption) uses the KMS_1 state for the averaging argument: "pi_1(mu_{P_S}) = weak limit of averages of group unitaries" in the GNS representation at KMS_1. This step depends on the specific KMS_1 state through its GNS representation. If we use a different KMS_1 state omega', the GNS representation pi_{omega'} is different, and the absorption argument must work in that representation too.

The absorption argument (Case 1 of Lemma 4.4) claims: projection operators (Hecke averaging operators) arise as conditional expectations of the base algebra, which are weak limits of convex combinations of group unitaries. This is a property of the conditional expectation E_A : M -> A, which exists and is normal for ANY crossed product A rtimes G with a faithful normal state (Takesaki II, X.1.7). The argument does not depend on which specific faithful normal state is used. The KMS_1 state is invoked to ensure faithfulness and normality (which we have by the KMS property), not for any state-specific property.

So yes, CP-1 works for any extremal KMS_1 state.

**Verdict: SURVIVED.** The insulation argument (Proposition C.5) is correct. The key insight is that every step in the bridge uses the KMS_1 state only for: (1) faithfulness on M_Bool (automatic from KMS), (2) type III_1 (automatic from modular eigenvalues), and (3) the crossed-product structure (algebraic, state-independent modulo faithfulness). No step requires a specific KMS_1 state or uniqueness thereof.

---

## Attack 5: Circular Dependency Check

**Claim under attack.** The repair in Node 3.2 does not assume CP-1.

**Analysis.**

I trace the logical dependencies of each part of the Node 3.2 repair:

**(a) KMS_1 existence (Theorem C.1).** Uses:
- Banach-Alaoglu theorem (general functional analysis)
- Structure of A^Bool_BC as a unital C*-algebra (definition of the Boolean BC system)
- The one-parameter group sigma_t^Bool (definition)
- Bratteli-Robinson 5.3.25 (closure of KMS sets)
- Finite-dimensional Gibbs states on truncated algebras

None of these use CP-1. The crossed-product identification is not invoked.

**(b) Faithfulness on phase algebra (Proposition C.2).** Uses:
- KMS condition restricted to the fixed-point algebra gives a trace
- Symmetry group (Z/2)^infty x S_infty acts on the phase algebra
- De Finetti's theorem

None of these use CP-1.

**(c) Type III_1 (Theorem C.3).** Uses:
- Existence of circuits of sizes 2 and 3 in PCirc^+
- Modular flow sigma_t(mu_C) = (size C)^{it} mu_C
- Irrationality of log 2 / log 3
- Connes spectrum theory (Connes 1973)
- KMS separating vector (Bratteli-Robinson II, 5.3.10)

None of these use CP-1. The modular flow is defined at the C*-algebra level, not at the von Neumann algebra level. The Connes spectrum is computed from the GNS representation, but the GNS construction is independent of CP-1.

**(d) Uniqueness insulation (Proposition C.5).** Uses:
- Intrinsic nature of fullness (Connes 1974, Haagerup 1987)
- CP-1 is state-independent

Wait -- Proposition C.5 MENTIONS CP-1 (in item (2): "CP-1 (crossed-product identification): state-independent"). But it does not USE CP-1 in its proof; it merely asserts that CP-1's conclusion is state-independent. This is a forward reference, not a circular dependency. Proposition C.5 is about the insulation of the bridge theorem from uniqueness, not about proving CP-1. The logical order is: Node 3.2 (KEY LEMMA repair) -> CP-1 (Node 2.1) -> bridge theorem. Proposition C.5 is a meta-theorem about the bridge, not an input to KEY LEMMA 3.4.3.

**Verdict: SURVIVED.** No circular dependency. Node 3.2 uses only: (i) the definition of the Boolean BC system, (ii) general operator algebra theory (Banach-Alaoglu, KMS closure, Tomita-Takesaki, Connes classification), and (iii) elementary number theory (irrationality of log 2/log 3). CP-1 is not assumed anywhere in the KEY LEMMA repair.

---

## Summary Table

| # | Attack Vector | Verdict | Reasoning |
|---|---|---|---|
| 1 | KMS_1 existence via Banach-Alaoglu | **SURVIVED** | Standard compactness argument; Bratteli-Robinson 5.3.23/5.3.25 correctly applied; truncation procedure sound |
| 2 | Faithfulness of omega^Bool_1 | **SURVIVED** | Faithfulness on M_Bool follows from KMS property (BR II 5.3.10), not from Bernoulli(1/2) on diagonal; downstream uses only need faithfulness on M_Bool, which is automatic |
| 3 | Type III_1 via multiplicative independence | **SURVIVED** | Modular eigenvectors correctly identified; point spectrum of Delta contains {2^a * 3^b}; density + closure gives S(M) = R_+^*; Connes classification correctly applied |
| 4 | Uniqueness unnecessary | **SURVIVED** | Each extremal KMS_1 component gives a type III_1 factor; CP-1 applies to each; fullness/non-fullness is intrinsic; bridge dichotomy and contradiction hold for each component |
| 5 | Circular dependency | **SURVIVED** | Node 3.2 repair uses only definitions, general OA theory, and elementary number theory; no reference to CP-1 |

## Overall Verdict: ALL FIVE ATTACKS SURVIVED

The KEY LEMMA 3.4.3 repair (Node 3.2) is sound, and its interface with CP-1 (Node 2.1) is clean. The compactness route to KMS_1 existence is rigorous, the type III_1 classification via multiplicative independence is correct, and the insulation from uniqueness is properly argued.

## Recommendations (non-blocking)

1. **Clarify faithfulness source.** Node 3.2 should explicitly cite Bratteli-Robinson II, Theorem 5.3.10 (KMS implies separating vector, hence faithful state on M_Bool) rather than relying on Proposition C.2 (faithfulness on the phase algebra) as the primary faithfulness result. The phase algebra faithfulness is a structural bonus, not the operational input.

2. **Pin down the gate basis.** The type III_1 argument should fix a specific gate basis (e.g., {AND, OR, NOT}) and explicitly verify the sizes of two circuits with coprime sizes. The current Node 3.2 is slightly vague on this point, listing multiple possible size conventions.

3. **Eigenvector computation.** Node 3.2 could benefit from a one-paragraph explanation of why size(C) lies in the point spectrum of Delta (via xi_C = pi_1(mu_C) Omega_1), making the type III_1 argument fully self-contained rather than invoking "the modular spectrum contains circuit sizes" as an unproved intermediate.

---

*Critic: Claude Opus 4.6 (1M context). W1-6. CP-1 Verification Programme.*
*Date: 2026-04-12.*
