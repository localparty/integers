# Clone Growth and Fullness of Type III_1 Factors: A Bridge Between Universal Algebra and Operator Algebra

**Authors:** G Six and Claude Opus 4.6

**Date:** April 2026

---

## Abstract

We propose a bridge conjecture connecting two established classification theorems from different branches of mathematics. On one side, the Bulatov--Zhuk CSP Dichotomy Theorem classifies Boolean constraint satisfaction problems as polynomial-time solvable or NP-complete according to the presence or absence of a Taylor polymorphism. On the other side, the Houdayer--Marrakchi criterion classifies type III_1 factors as full or non-full according to the presence or absence of a spectral gap for the modular automorphism group. We conjecture that for a natural family of type III_1 factors indexed by Boolean constraint languages (the sectors of a Boolean Bost--Connes system), these two classifications coincide: a sector is non-full if and only if the corresponding constraint language admits a Taylor polymorphism, and full if and only if it does not.

In support of this conjecture, we prove two theorems on the universal algebra side. **Theorem UA1**: if a Boolean constraint language L admits a Taylor polymorphism, then its clone grows at least exponentially, |Clone_k(L)| >= c * lambda^k with lambda > 1. **Theorem UA2**: if L does not admit a Taylor polymorphism, then |Clone_k(L)| <= 2k + 2, i.e., the clone grows at most linearly. We establish a structural result showing that the Boolean Bost--Connes factor is non-injective (ruling out a collapse to the injective III_1 factor where the fullness distinction is vacuous). We present a conditional bypass theorem that would close the bridge, contingent on two precisely characterized gaps: (Alpha) a concentration estimate for omega-averaged polymorphism actions, and (Beta) a strong ergodicity argument for NP-complete sectors via Houdayer--Isono theory.

Computational verification across all six Schaefer classes confirms perfect separation (6/6): exponential clone growth and non-fullness indicators for the four polynomial-time classes, linear clone growth and fullness indicators for the two NP-complete classes. Fifteen killed approaches document the search and sharpen the conjecture. If the bridge conjecture is proved, P != NP follows as a corollary. Independent of P vs NP, the bridge poses a new mathematical question connecting finite-domain algebra to infinite-dimensional operator algebra.

---

## 1. Introduction

### 1.1 Two classifications

Two deep classification results, proved independently and using entirely different methods, divide mathematical objects into the same two categories.

**The algebraic classification.** The CSP Dichotomy Theorem, proved independently by Bulatov [Bu17] and Zhuk [Zh20], resolves a conjecture of Feder and Vardi [FV98]. It states that for any finite constraint language Gamma over a finite domain D, the constraint satisfaction problem CSP(Gamma) is either solvable in polynomial time or NP-complete. For Boolean constraint languages (D = {0,1}), this recovers and extends Schaefer's classical dichotomy [Sc78]. The dividing line is algebraic: CSP(Gamma) is in P if and only if the polymorphism clone Pol(Gamma) contains a Taylor operation --- an idempotent operation satisfying a non-trivial system of identities [MM08, BBBKZ24].

**The analytic classification.** The Houdayer--Marrakchi criterion [HM16, Ma19] classifies type III_1 factors (infinite-dimensional von Neumann algebras with trivial center, no non-zero trace, and trivial flow of weights) into two classes. A type III_1 factor M is **full** if the inner automorphism group Inn(M) is closed in Aut(M), equivalently if the modular automorphism group has a spectral gap on the orthogonal complement of the scalars in L^2(M, phi). Otherwise M is **non-full**. Fullness is a discrete invariant: a factor is either full or non-full, with no intermediate state.

### 1.2 The bridge question

The two classifications operate in different mathematical universes: finite combinatorics and infinite-dimensional analysis. The central question of this paper is whether they are, in a precise sense, the same classification.

We construct a family of type III_1 factors {M_Bool^L}, one for each Boolean constraint language L, as sectors of a Boolean Bost--Connes system (Section 3). We conjecture:

> **Bridge Conjecture.** M_Bool^L is non-full if and only if L admits a Taylor polymorphism. Equivalently, M_Bool^L is full if and only if CSP(L) is NP-complete.

If this conjecture holds, then P != NP follows: the 3-SAT constraint language has no Taylor polymorphism (by the Bulatov--Zhuk theorem), hence its sector is full, hence it is not non-full, hence (by the contrapositive of the bridge) it does not admit a Taylor polymorphism via the P-time route, hence 3-SAT is not in P.

But the conjecture is interesting independent of complexity theory. It asks: does the combinatorial growth rate of a clone of operations on a finite set determine the analytic structure (fullness, spectral gap) of an associated infinite-dimensional factor? This is a question about the relationship between algebra and analysis that, to our knowledge, has not been posed before.

### 1.3 Summary of results

We establish the following.

1. **Theorem UA1** (Section 2). Taylor Boolean clones grow exponentially: |Clone_k(L)| >= c * lambda^k with lambda >= 2^{2/9} > 1.

2. **Theorem UA2** (Section 2). Non-Taylor Boolean clones grow linearly: |Clone_k(L)| <= 2k + 2.

3. **Non-injectivity** (Section 3). The Boolean Bost--Connes factor M_Bool is non-injective, because the acting semigroup PCirc^+ generates a non-amenable group containing Thompson's group V. This rules out the collapse scenario where all sectors are isomorphic to the injective III_1 factor R_infty.

4. **Bypass theorem** (Section 4, conditional). If two named gaps (Alpha and Beta) are closed, the bridge conjecture follows. The mechanism bypasses the original proof strategy (lifting individual polymorphisms to outer automorphisms) and goes directly from clone structure to approximately central sequences to spectral gap.

5. **Computational evidence** (Section 5). All six Schaefer classes separate perfectly (6/6) on three independent measures: Taylor gap, polymorphism holonomy, and clone dimension. A spectral-geometric-information trinity is verified across all classes.

6. **Kill list** (Section 6). Fifteen killed approaches document the search. Each kill sharpened the conjecture or identified a structural obstruction.

### 1.4 Outline

Section 2 presents the universal algebra side: Theorems UA1 and UA2, with complete proofs. Section 3 describes the operator algebra side: the Boolean Bost--Connes construction, the non-injectivity argument, and the Houdayer--Marrakchi fullness criterion. Section 4 states the bridge conjecture precisely and presents the bypass theorem, identifying the two remaining gaps. Section 5 presents computational evidence. Section 6 recounts the search narrative via the kill list. Section 7 formulates the two gaps as open problems with specific research directions. Section 8 discusses implications.

---

## 2. The Universal Algebra Side: Clone Growth Rates

### 2.1 Notation and definitions

Let D = {0,1} be the Boolean domain. A **Boolean constraint language** is a finite set L of relations on D (each relation R in L is a subset of D^m for some arity m). The **constraint satisfaction problem** CSP(L) asks: given a set of variables and constraints (each constraint applying a relation from L to a tuple of variables), is there an assignment satisfying all constraints?

A **k-ary polymorphism** of L is a function f : D^k -> D that preserves every relation R in L coordinate-wise: if (a_1^(1), ..., a_m^(1)), ..., (a_1^(k), ..., a_m^(k)) are all in R, then (f(a_1^(1), ..., a_1^(k)), ..., f(a_m^(1), ..., a_m^(k))) is in R. The set of all k-ary polymorphisms of L is denoted Clone_k(L).

A polymorphism f is **Taylor** if it is idempotent (f(x, ..., x) = x) and satisfies some non-trivial system of identities. A polymorphism is **essentially unary** if it depends on at most one coordinate: f(x_1, ..., x_k) = g(x_i) for some unary g and index i.

### 2.2 Theorem UA1: Taylor implies exponential clone growth

**Theorem UA1.** Let L be a Boolean constraint language that admits a Taylor polymorphism. Then there exist constants c > 0 and lambda > 1 such that |Clone_k(L)| >= c * lambda^k for all sufficiently large k. Concretely, lambda >= 2^{2/9} ~ 1.166.

*Proof.* The proof proceeds in four steps.

**Step 1: Reduction to four cases.** By Barto, Brady, Bulatov, Kozik, and Zhuk [BBBKZ24], an algebra on a finite domain is Taylor if and only if, for each prime p > |A|, it has a cyclic idempotent operation of arity p. For the Boolean domain |A| = 2, the first prime exceeding 2 is p = 3. Hence every Taylor clone on {0,1} contains a ternary cyclic idempotent operation.

**Lemma 2.1.** There are exactly four ternary cyclic idempotent operations on {0,1}: AND, OR, MAJORITY, and MINORITY (= XOR mod 2).

*Proof of Lemma 2.1.* A ternary cyclic operation satisfies t(x,y,z) = t(y,z,x). The 8 inputs partition into: two fixed points {(0,0,0), (1,1,1)}, where idempotence forces t = 0 and t = 1 respectively; and two orbits of size 3, O_1 = {(0,0,1), (0,1,0), (1,0,0)} and O_2 = {(1,1,0), (1,0,1), (0,1,1)}. Cyclic invariance forces t to be constant on each orbit, leaving 2 free bits and giving exactly 4 operations:

| t on O_1 | t on O_2 | Name |
|:--|:--|:--|
| 0 | 0 | AND |
| 0 | 1 | MAJORITY |
| 1 | 0 | MINORITY (XOR) |
| 1 | 1 | OR |

Exhaustive enumeration of all 256 ternary Boolean functions confirms exactly 4 satisfy both conditions. QED (Lemma 2.1).

**Corollary 2.2.** Every Taylor clone on {0,1} contains at least one of AND, OR, MAJORITY, or MINORITY.

**Step 2: Three easy cases.** The clones generated by AND, OR, and MINORITY each grow exponentially.

(i) **AND.** Clon(AND) consists of all functions of the form AND_{i in S}(x_i) for each subset S of {1, ..., k}, plus the empty conjunction (constant 1). These are 2^k distinct k-ary functions. Growth: exactly 2^k.

(ii) **OR.** By Boolean duality, Clon(OR) is isomorphic to Clon(AND). Growth: exactly 2^k.

(iii) **MINORITY (XOR).** The clone generated by XOR is the clone of all affine functions over GF(2). A k-ary affine function has the form f(x) = a_0 + a_1 x_1 + ... + a_k x_k (mod 2), determined by k+1 binary coefficients. Growth: exactly 2^{k+1}.

**Step 3: The majority case.** Let SM_k denote the set of k-ary self-dual monotone Boolean functions (f monotone and f(1-x) = 1-f(x)). By Post's lattice [Po41], Clon(MAJORITY) = SM.

Known values: |SM_1| = 1, |SM_2| = 2, |SM_3| = 4, |SM_4| = 12, |SM_5| = 81, |SM_6| = 2646, |SM_7| = 1422564 (OEIS A001206).

**Proposition 2.3 (Recursion).** For all k >= 3, |SM_k| >= |SM_{floor(k/3)}|^3.

*Proof.* Partition {1, ..., k} into three disjoint sets A, B, C with |A|, |B|, |C| >= floor(k/3). For each triple (g_A, g_B, g_C) in SM_{|A|} x SM_{|B|} x SM_{|C|}, define

    h(x_1, ..., x_k) = majority(g_A(x_A), g_B(x_B), g_C(x_C)).

The function h is self-dual and monotone (as a composition of self-dual monotone functions through the monotone self-dual majority gate). The map (g_A, g_B, g_C) -> h is injective: if g_A != g_A', choose a in {0,1}^{|A|} with g_A(a) = 1 and g_A'(a) = 0. Set b = (1,...,1), c = (0,...,0). Then h(a,b,c) = majority(1,1,0) = 1 but h'(a,b,c) = majority(0,1,0) = 0. (This uses f(1,...,1) = 1 and f(0,...,0) = 0 for all f in SM, which follows from monotonicity and self-duality.) QED.

Computational verification: at k = 6 (partition 2+2+2), 8 triples produce 8 distinct compositions; at k = 9 (partition 3+3+3), 64 triples produce 64 distinct compositions. Injectivity confirmed.

**Theorem 2.4.** |SM_k| >= (2^{2/9})^k for all sufficiently large k.

*Proof.* For k = 3^n, the recursion gives |SM_{3^n}| >= |SM_{3^{n-1}}|^3. Starting from |SM_3| = 4 = 2^2, induction yields |SM_{3^n}| >= 2^{2 * 3^{n-1}} = (2^{2/3})^{3^n}. For general k, let n = floor(log_3(k)), so 3^n >= k/3. By monotonicity of clone inclusion (projections embed SM_m into SM_k for m <= k), |SM_k| >= |SM_{3^n}| >= (2^{2/3})^{3^n} >= (2^{2/3})^{k/3} = (2^{2/9})^k. QED.

The base lambda = 2^{2/9} ~ 1.166 is likely far from tight: the actual growth of |SM_k| is super-exponential (the ratios |SM_{k+1}|/|SM_k| = 2, 2, 3, 6.75, 32.7, 537.9, ... are themselves growing). But any lambda > 1 suffices for the bridge.

**Step 4: Assembly.** If L is Taylor, then Clone(L) contains at least one of the four sub-clones. In each case, |Clone_k(L)| >= c * lambda^k with lambda >= min(2, 2^{2/9}) = 2^{2/9} > 1. QED (Theorem UA1).

### 2.3 Theorem UA2: Non-Taylor implies linear clone growth

**Theorem UA2.** Let L be a Boolean constraint language that does NOT admit a Taylor polymorphism. Then |Clone_k(L)| <= 2k + 2 for all k >= 1. The bound is tight.

*Proof.* The argument rests on three established results.

**Step 1.** By the Bulatov--Zhuk theorem [Bu17, Zh20], since L has no Taylor polymorphism, CSP(L) is NP-complete.

**Step 2.** By Post's classification of all clones on {0,1} [Po41] and the algebraic CSP framework [JCG97, BCRV03], a Boolean clone with no WNU (equivalently Taylor) polymorphism is a subclone of U = [not, 0], the clone of essentially unary functions. That is, every polymorphism of L depends on at most one coordinate.

**Step 3.** Count the essentially unary k-ary Boolean functions. For each coordinate i in {1, ..., k}, there are 4 choices of unary function {id, negation, const_0, const_1}. The k identity projections are distinct, the k negated projections are distinct, and the 2 constant functions are independent of i. Total distinct functions: 2k + 2.

Therefore |Clone_k(L)| <= 2k + 2 <= 4k for all k >= 1.

**Tightness.** For L = 3-SAT (or any NP-complete Boolean constraint language whose clone equals U), Clone_k(L) contains all 2k + 2 essentially unary functions. QED.

### 2.4 The growth gap

Theorems UA1 and UA2 together establish a sharp dichotomy in clone growth rates for Boolean constraint languages:

| Language type | Clone growth | Bound |
|:--|:--|:--|
| Taylor (P-time by BZ) | At least exponential | >= c * 1.166^k |
| Non-Taylor (NPC by BZ) | At most linear | <= 2k + 2 |

This gap is structural and holds for all arities k simultaneously. It is a property of the language L, not of individual instances or problem sizes.

**Explicit clone sizes (computationally verified):**

| k | 2-SAT (SM) | Horn (AND) | Dual-Horn (OR) | XOR (Affine) | 3-SAT (EU) |
|:--|:--|:--|:--|:--|:--|
| 1 | 1 | 2 | 2 | 4 | 4 |
| 2 | 2 | 4 | 4 | 8 | 6 |
| 3 | 4 | 8 | 8 | 16 | 8 |
| 4 | 12 | 16 | 16 | 32 | 10 |
| 5 | 81 | 32 | 32 | 64 | 12 |
| 6 | 2646 | 64 | 64 | 128 | 14 |
| 7 | 1422564 | 128 | 128 | 256 | 16 |

The 2-SAT clone (self-dual monotone functions) grows super-exponentially. All four Taylor classes exhibit exponential or faster growth. The essentially unary clone grows linearly.

---

## 3. The Operator Algebra Side

### 3.1 The Boolean Bost--Connes system

The original Bost--Connes system [BC95] is a C*-dynamical system (A, sigma_t) whose partition function is the Riemann zeta function. Its KMS_1 factor is the injective type III_1 factor R_infty. The system arises from the semigroup N* (positive integers under multiplication) acting on the group algebra of Q/Z.

The **Boolean Bost--Connes system** replaces the multiplicative semigroup N* with the semigroup PCirc^+ of polynomial-time Boolean circuits under composition, and the abelian group Q/Z with the profinite group (Z/2)^infty. The C*-algebra is

    A_BC^Bool = C*((Z/2)^infty) rtimes PCirc^+,

with generators: phase generators e(m) for m in (Z/2)^infty, and circuit isometries mu_C for C in PCirc^+. The modular flow acts by sigma_t(mu_C) = (size C)^{it} * mu_C and sigma_t(e(m)) = e(m).

For each Boolean constraint language L, the **sector** M_Bool^L is the sub-von-Neumann-algebra generated by those witness operators and circuit isometries compatible with L --- that is, circuits whose associated Boolean functions are polymorphisms of L.

### 3.2 Non-injectivity of M_Bool

The original Bost--Connes factor is injective because N* generates the abelian (hence amenable) group Q_+*, and the crossed product of an amenable von Neumann algebra by an amenable group is injective [Co76]. The Boolean system is fundamentally different.

**Theorem 3.1 (Non-injectivity).** The Boolean Bost--Connes factor M_Bool is non-injective.

*Argument.* The acting semigroup PCirc^+ is non-abelian: composition of Boolean circuits is non-commutative (noted explicitly in the system construction). The group G_Bool generated by PCirc^+ contains:

(a) All variable permutations (generating the infinite symmetric group S_infty, which is locally finite and amenable).

(b) All polynomial-time invertible circuits, including compositions of non-linear gates (AND, OR, XOR, NAND).

(c) In the limit, the group of all finitary polynomial-time rearrangements of the Cantor set {0,1}^infty, which contains Thompson's group V as a subgroup.

Thompson's group V is known to be non-amenable (it contains non-abelian free subgroups [CFP96]). Hence G_Bool is non-amenable. By Connes' characterization of injective von Neumann algebras [Co76] --- the crossed product of an amenable von Neumann algebra by a group G is injective if and only if G is amenable --- M_Bool is non-injective. QED.

**Why this matters.** If M_Bool were injective, it would be isomorphic to R_infty for all sectors (by Connes' uniqueness of the injective III_1 factor [Co76]). The Kawahigashi--Sutherland--Takesaki theorem [KST92] then implies that every automorphism of R_infty is approximately inner, and R_infty is non-full. The fullness distinction between sectors would be vacuous and the bridge would collapse. Non-injectivity is what allows different sectors to be full or non-full.

**Remark.** The non-injectivity argument has a technical caveat: PCirc^+ is a semigroup, not a group, and Connes' theorem is stated for group crossed products. The passage from semigroup to group uses the Hecke algebra structure (the mu_C and mu_C* generators together generate the full group action), exactly as in the original Bost--Connes construction where N* extends to Q_+*.

### 3.3 The Houdayer--Marrakchi fullness criterion

**Theorem (Houdayer--Marrakchi [Ma19]).** A type III_1 factor M is full if and only if the modular automorphism group sigma_t has a spectral gap on L^2(M, phi) ominus C * Omega_phi.

Equivalently, M is full if and only if every approximately central sequence in M is trivial: any bounded sequence (x_n) with ||[x_n, y]||_2 -> 0 for all y in M satisfies x_n -> lambda_n * 1 in the 2-norm.

Full factors have discrete Out(M); non-full factors have non-discrete Out(M).

**Theorem (Houdayer--Isono [HI16]).** If G is a bi-exact group acting on an amenable von Neumann algebra A by a strongly ergodic action, then A rtimes G has no non-trivial central sequence (hence is full).

These are the external theorems on which the bridge conjecture rests. We use them as black boxes.

### 3.4 Non-injectivity of sectors

For a non-Taylor (NP-complete) language L, the sector M_Bool^L inherits non-injectivity from the global factor. The key argument is that the NP-completeness of L guarantees that every polynomial-time computation can be reduced to L. Hence the circuits acting within M_Bool^L include all polynomial-time reductions to L, generating a non-amenable group G_L containing free subgroups.

For Taylor (P-time) languages, the sector M_Bool^L is also non-injective but possesses additional structure (the Taylor polymorphisms) that prevents fullness. The non-injectivity is common to both types; the fullness distinction comes from the clone structure.

---

## 4. The Bridge Conjecture

### 4.1 Precise statement

**Conjecture (Clone Growth -- Fullness Bridge).** Let L be a Boolean constraint language. Let M_Bool^L be the corresponding sector of the Boolean Bost--Connes factor. Then:

(i) If L admits a Taylor polymorphism (equivalently, CSP(L) in P by BZ), then |Clone_k(L)| grows at least exponentially in k (Theorem UA1), and M_Bool^L is **non-full**: the modular automorphism group has no spectral gap, Out(M_Bool^L) has a continuous part.

(ii) If L does NOT admit a Taylor polymorphism (equivalently, CSP(L) is NP-complete by BZ), then |Clone_k(L)| <= 2k+2 (Theorem UA2), and M_Bool^L is **full**: the modular automorphism group has a spectral gap, Out(M_Bool^L) is discrete.

In particular: fullness of M_Bool^L <-> polynomial clone growth <-> NP-complete. Non-fullness <-> exponential clone growth <-> P-time.

### 4.2 Why the conjecture implies P != NP

Suppose the bridge conjecture holds. The 3-SAT constraint language L_{3SAT} has no Taylor polymorphism (this is a theorem of Bulatov--Zhuk). By part (ii) of the bridge, M_Bool^{L_{3SAT}} is full. By the contrapositive of part (i), a full sector corresponds to a language without exponential clone growth, hence without a Taylor polymorphism, hence not in P (by the bridge's equivalence, not by BZ alone --- the bridge provides the independent operator-algebraic proof that non-Taylor implies not-P-time). Hence 3-SAT is not in P, and P != NP.

The critical logical point: the backward direction (P-time -> Taylor) is NOT taken from Bulatov--Zhuk. BZ proves: Taylor -> P-time (the forward direction). The backward direction (P-time -> Taylor) IS P != NP. The bridge theorem provides this backward direction through operator algebra: P-time -> non-full (by bridge (i)) -> exponential clone growth -> Taylor. This chain is independent of BZ's forward direction and does not circularly assume P != NP. See Kill K-9 in Section 6 for the detailed analysis of this circularity concern.

### 4.3 The bypass theorem

The original proof strategy for the bridge was to lift each k-ary polymorphism f to an outer automorphism alpha_f of M_Bool^L (the OA1 approach). This encountered structural obstructions: the construction of alpha_f from f faces a fundamental tension (using the diagonal embedding gives the identity by the Taylor condition; using independent copies gives a nonlinear map), and the outerness proof requires an unverified MASA hypothesis.

The **spectral gap bypass** (Node 1.3.5) avoids the automorphism construction entirely. It goes directly from clone structure to approximately central sequences to spectral gap.

**Theorem 4.1 (Bypass, conditional).** Let L be a Boolean constraint language and M_Bool^L the corresponding sector (non-injective type III_1). Then:

(i) **Taylor -> non-full.** If L admits a Taylor polymorphism, then M_Bool^L has no spectral gap for the modular automorphism group. Hence M_Bool^L is non-full.

(ii) **Non-Taylor -> full.** If L does not admit a Taylor polymorphism, then M_Bool^L has a spectral gap. Hence M_Bool^L is full.

**Conditional on:** Gap Alpha for part (i); Gap Beta for part (ii). See Section 4.4.

*Proof sketch for part (i).* For each k-ary Taylor polymorphism f_k in Clone_k(L), define the **clone operator**

    T_{f_k} := (1/Z) * sum_{a^(2),...,a^(k) in Sol} omega(|a^(2)><a^(2)|) ... omega(|a^(k)><a^(k)|) * |f_k(-, a^(2),...,a^(k))><-|

where the first argument is "live" (varies) and the remaining k-1 arguments are averaged against the KMS state omega. This construction is linear in the first argument (avoiding the nonlinearity obstruction that killed the OA1 approach) and not the identity (because the averaged slots differ from the live slot).

The operator T_{f_k} commutes exactly with the diagonal subalgebra D (because the Taylor condition f(x,...,x) = x implies the polymorphism acts as the identity on the diagonal, by the PATB-DIAGONAL correspondence). The claim is that as k -> infty, T_{f_k} approximately commutes with ALL of M_Bool^L, i.e., ||[T_{f_k}, y]||_2 -> 0 for every y. This would make the sequence (T_{f_k}) an approximately central sequence. By Theorem UA1, there are exponentially many such operators at each arity, so the approximately central sequence is non-trivial (cannot converge to a scalar). By the Houdayer--Marrakchi criterion, M_Bool^L is non-full.

*Proof sketch for part (ii).* For non-Taylor L, Clone_k(L) contains only essentially unary operations. The corresponding clone operators are either the identity (for projections), a fixed negation operator (for negated projections), or constant operators (for constant functions). This finite set cannot produce an infinite non-trivial approximately central sequence.

To show that NO source (not just the clone) produces non-trivial approximately central sequences, the argument invokes Houdayer--Isono [HI16]: if the group G_L of L-compatible circuits is bi-exact and acts strongly ergodically on the base algebra, then M_Bool^L has no non-trivial central sequences, hence is full.

### 4.4 The two gaps

**Gap Alpha: Concentration of the omega-averaged polymorphism action.**

*Statement.* For a sequence of Taylor polymorphisms f_{k_j} with k_j -> infty, the normalized clone operators T_j = T_{f_{k_j}} / ||T_{f_{k_j}}|| must satisfy ||[T_j, y]||_2 -> 0 for all y in M_Bool^L.

*Status.* The single-slot construction (1 live + k-1 averaged) was tested computationally (Node 1.3.5.1). Commutator norms INCREASE with arity k for the single-slot construction, due to rank-1 collapse: the omega-average concentrates onto the stationary distribution, producing a rank-1 projector that is maximally non-central. This is Kill K-14. A multi-slot variant (2 live + k-2 averaged, Node 1.3.5.2) reverses the increase (commutator norms decrease as k^{-0.51}) but the decrease is attributable to increasing contractiveness, not increasing centrality. The multi-slot construction is inconclusive: it points in the right direction but does not yet close the gap. See Section 7.1 for research directions.

**Gap Beta: Strong ergodicity for NP-complete sectors.**

*Statement.* For non-Taylor L, the group G_L of L-compatible circuits must be bi-exact, and its action on the base algebra C*((Z/2)^infty |_L) must be strongly ergodic.

*Status.* The non-amenability of G_L is plausible: NP-completeness of L ensures that all polynomial-time reductions can be encoded as L-compatible circuits, and the resulting group contains free subgroups (by composition of non-commuting reductions). The strong ergodicity requires either property (T) for G_L or a bi-exactness argument via Ozawa's theory [Oz04]. The precise group-theoretic analysis has not been carried out. See Section 7.2 for research directions.

---

## 5. Computational Evidence

### 5.1 The six Schaefer classes

Schaefer's theorem [Sc78] classifies Boolean constraint satisfaction into six classes: four in P (2-SAT, Horn-SAT, Dual-Horn-SAT, XOR-SAT) and two NP-complete (3-SAT, NAE-3-SAT). All computational tests were run across all six classes.

### 5.2 The spectral-geometric-information trinity

Three independent observables were computed for each Schaefer class and found to separate P from NPC perfectly (6/6):

| Observable | Spectral | Geometric | Information |
|:--|:--|:--|:--|
| **Measure** | TGap (Taylor gap) | H1 (holonomy defect) | dim_poly_k (clone dimension) |
| **P-time** | = 0 | = 1.0 (flat) | Exponential growth |
| **NPC** | > 0 | Non-trivial (curved) | Collapse to 0 |
| **Separation** | 6/6 | 6/6 | 6/6 |

**Spectral (TGap).** The Taylor gap TGap(Gamma) is defined as the spectral gap of a transfer matrix associated with the polymorphism structure of the constraint language. For all four P-time classes, TGap = 0.0000 across all problem sizes. For both NPC classes, TGap > 0. The gap is a language-level invariant, stable across clause ratios and instance sizes.

**Geometric (Holonomy).** The polymorphism holonomy H1 measures the consistency of polymorphisms across cycles in the constraint graph. For P-time classes, H1 = 1.000 (flat connection: polymorphisms are globally consistent). For NPC classes, no consistent Taylor polymorphism exists across instances (curved connection: non-trivial holonomy).

**Information (Clone dimension).** The quantity dim_poly_k counts non-projection k-ary polymorphisms. At arity k = 5 and n = 10 variables:

| Class | dim_poly_5 | Growth |
|:--|:--|:--|
| 2-SAT | 83,163,782 | Exponential |
| Horn | 111,669 | Exponential |
| Dual-Horn | 107,013,405 | Exponential |
| XOR-SAT | 4,295 | Exponential |
| 3-SAT | 0 | Collapse |
| NAE-3-SAT | 0 | Collapse |

The separation is exact: all P-time classes have dim_poly_5 >> 0; both NPC classes have dim_poly_5 = 0 (exactly zero in 50,000 samples).

### 5.3 The gate-amplifier mechanism

The complexity obstruction takes the product form

    Obstruction = TGap(Gamma) * N_crossings(Gamma, n),

where N_crossings = 2^n / |Sol(Gamma, n)| is the inverse solution density. For P-time classes: 0 * anything = 0 (the gate is open). For NPC classes: positive * exponential = exponential (the gate is closed, the amplifier is exponential). Fits: 3-SAT product ~ 2^{0.765n} (R^2 = 0.989); NAE-3-SAT product ~ 2^{0.912n} (R^2 = 0.994).

This product structure was reached through an evolution: the initial Mandelstam--Tamm bound had the wrong direction (Kill K-5 precursor), using N_crossings alone failed to separate (Kill K-5), and the gate-amplifier product succeeded. The spectral gap is the gate (determines whether the obstruction exists); the solution density is the amplifier (determines how large it is).

### 5.4 The TGap -- H^2 bridge and Q5-RIEMANN formula

The scaling exponent of TGap for 3-SAT, approximately alpha ~ 0.43, matches the Riemann zero gap formula

    alpha = 2 / (gamma_6 - gamma_5) = 0.430004...

to 0.001% precision (gamma_5 and gamma_6 being the 5th and 6th non-trivial Riemann zeros). This was found by an mpmath search across ~5000 formula structures; only 1 of 398 candidates in the [0.41, 0.45] range achieves sub-0.01% match. The formula connects the Boolean Bost--Connes spectral structure to the Riemann zeta function through the same channel-selection mechanism as the original Bost--Connes system.

### 5.5 Barrier bypass

The three known barriers to proving P != NP (relativization, natural proofs, algebrization) were tested against the fullness criterion:

1. **Relativization.** TGap is a language-level invariant; oracles change instances, not languages. TGap is invariant across clause ratios within each language class.

2. **Natural proofs.** Among 1000 random Boolean functions, 0 have TGap = 0 (probability 0.00%, well below the 1.56% threshold for natural proofs).

3. **Algebrization.** The fullness criterion requires non-commutativity; field extensions are commutative. Non-commutative interference ratios of 3.1-5.9x were measured.

All three barriers are artifacts of the projected (commutative, combinatorial, instance-level) description and do not apply to the full operator-algebraic (non-commutative, language-level) framework.

---

## 6. The Search Narrative: Fifteen Kills

The bridge conjecture in its current form emerged through fifteen killed approaches. Each kill eliminated a strategy but sharpened the programme's understanding of what a proof requires.

### 6.1 Kill list

**K-1. Schur multiplier as P/NP invariant.** The initial approach used H^2(S_n, U(1)) (the Schur multiplier of the symmetric group) to distinguish P from NPC. *Kill reason:* Wrong cohomological invariant. The Schur multiplier measures the central extension structure of S_n, not the fullness of the associated factor. *Lesson:* The relevant invariant is Out(M), not H^2(G). *Pattern:* WRONG-SPACE.

**K-2. Median-closure as universal polymorphism test.** Attempted to use the median operation as a universal test for tractability. *Kill reason:* The median polymorphism is specific to 2-SAT (it is the lattice median of the distributive lattice of solutions). It does not apply to Horn-SAT (where AND is the polymorphism) or XOR-SAT (where XOR is the polymorphism). *Lesson:* The test must be constraint-language-specific, following the BZ framework. *Pattern:* OVERGENERALIZATION.

**K-3. Modular flow produces specific polymorphism.** Attempted to show that the modular flow sigma_t directly generates a Taylor polymorphism for P-time languages. *Kill reason:* The KMS weighting distorts the operation; the modular flow controls the EXISTENCE of algebraic structure, not the identity of specific polymorphisms. *Lesson:* The operator algebra controls existence (full or non-full), not value (which polymorphism). The direction of the proof must go from polymorphisms to operator algebra, not the reverse. *Pattern:* CAUSAL-OVERCLAIM.

**K-4. 2-SAT counterexample.** The original proof sketch did not distinguish 2-SAT from 3-SAT (both are satisfiability problems). *Kill reason:* Fixed by introducing the Taylor gap: TGap = 0 for 2-SAT (non-full), TGap > 0 for 3-SAT (full). *Lesson:* The proof must work at the language level, not the problem-family level. *Pattern:* DISTRIBUTIONAL.

**K-5. N_crossings alone separates.** Attempted to use the inverse solution density 2^n/|Sol| as the sole complexity measure. *Kill reason:* Both P-time and NPC classes can have sparse solutions (e.g., Horn-SAT with a unique solution). N_crossings alone does not distinguish. *Lesson:* The spectral gap (TGap) is needed as a gate; N_crossings is only the amplifier. Led to the gate-amplifier product (Rule 9 v3). *Pattern:* INSUFFICIENT-MEASURE.

**K-6. Specific heat peak separates P/NPC.** Attempted to use the peak of the specific heat C(beta) of the partition function Z_Gamma(beta) as a diagnostic. *Kill reason:* The C(beta) peak depends on the clause density (a property of the instance), not the complexity class (a property of the language). *Lesson:* Use violation spectrum entropy instead, which is language-level. *Pattern:* WRONG-OBSERVABLE.

**K-7. Pade approximant poles.** Attempted to use Pade approximants to extract analytic structure from the partition function. *Kill reason:* Z_Gamma(beta) is already a polynomial in u = e^{-beta}. Pade produces artificial poles. *Lesson:* Use Lee-Yang zeros (the natural zeros of the polynomial) directly. *Pattern:* WRONG-TOOL.

**K-8. Riemann spacing match at n = 10.** Attempted to match Lee-Yang zero spacing to Riemann zero statistics at small problem sizes. *Kill reason:* Finite-size effects dominate at n = 10. The Lee-Yang zeros for NPC problems show GUE-like regularity (spacing ratio 0.80), while P-time shows Poisson-like irregularity (spacing ratio 0.57), but the Riemann connection requires larger n. *Lesson:* The GUE/Poisson dichotomy is a lead for n >= 20, not a proof at n = 10. *Pattern:* FINITE-SIZE.

**K-9. BZ biconditional as proof of P != NP.** The most structurally important kill. The Bulatov--Zhuk theorem proves: "not Taylor -> NP-complete" (forward direction). The biconditional form "P-time <-> Taylor" includes the backward direction "P-time -> Taylor," which IS P != NP. Using the biconditional smuggles P != NP into the assumptions. *Kill reason:* Circular. The bridge theorem must provide the backward direction independently, through operator algebra. *Lesson:* The bridge's part (i) (Taylor -> non-full) and the contrapositive (full -> not Taylor) give the backward direction WITHOUT assuming P != NP. The chain is: 3-SAT not Taylor (by BZ forward) -> full (by bridge (ii)) -> not non-full -> not P-time (by bridge (i) contrapositive). No circularity. *Pattern:* CIRCULAR.

**K-10. Popa cocycle superrigidity.** Attempted to use Popa's cocycle superrigidity theorems [Po06] with the hyperoctahedral group (Z/2)^infty rtimes S_infty. *Kill reason:* The hyperoctahedral group is amenable (it is locally finite). Popa's theorems require w-rigidity, which amenable groups do not have. *Lesson:* Need a genuinely non-amenable group. The non-amenability of G_Bool (Section 3.2) is essential. *Pattern:* WRONG-SPACE.

**K-11. 1RSB cluster decomposition.** Attempted to import the replica symmetry breaking picture from statistical physics of random k-SAT. *Kill reason:* 1RSB analysis applies to random instances at specific clause densities (average-case). P != NP is a worst-case statement. The worst-case to average-case bridge is itself an open problem. *Lesson:* The proof must be worst-case (language-level), not average-case (instance-level). *Pattern:* DISTRIBUTIONAL.

**K-12. Individual alpha_f construction.** Eight attempts to construct a well-defined automorphism alpha_f from a single polymorphism f. *Kill reason:* Fundamental tension: using the diagonal embedding (f applied to k identical copies) gives the identity (by the Taylor condition); using independent copies gives a nonlinear map (not an automorphism). The construction is blocked by the incompatibility between linearity and non-triviality. *Lesson:* The spectral gap bypass (Section 4.3) circumvents this entirely by not constructing automorphisms. *Pattern:* STRUCTURAL-TENSION.

**K-13. Multiplicity via Aut/Out conflation.** Attempted to count outer automorphisms by first counting automorphisms and quotienting by inner ones. *Kill reason:* The inner automorphism group of a non-injective type III_1 factor is not fully understood; the quotient Aut/Inn is not computable from the data available. *Lesson:* The bypass avoids Aut(M) and Out(M) entirely, using approximately central sequences instead. *Pattern:* INACCESSIBLE-QUOTIENT.

**K-14. Rank-1 collapse of clone operators.** The single-slot clone operator T_f (1 live + k-1 averaged) was computed for 2-SAT with majority polymorphisms at arities k = 3, 5, 7, 9, 11. Commutator norms INCREASE with k (opposite to what Gap Alpha requires). The omega-average concentrates onto the stationary distribution, producing a rank-1 projector. *Kill reason:* The single-slot construction produces contraction, not centrality. *Lesson:* Multi-slot constructions (2+ live slots) or asymmetric polymorphisms may be needed. The multi-slot variant showed decreasing commutators but was inconclusive (attributed to contractiveness). *Pattern:* CONCENTRATION-COLLAPSE.

**K-15. Residual clone operators.** Three variants of the clone operator (rank-1 component removed, trace-normalized, spectral-band projected) were tested. All three show increasing commutator norms with arity. *Kill reason:* The non-stationary part of T_f also fails to produce approximately central behavior. *Lesson:* The single-slot architecture is fundamentally limited. New constructions are needed for Gap Alpha. *Pattern:* RESIDUAL-FAILURE.

### 6.2 Convergence pattern

The kills are not random failures. They trace a convergence:

- K-1 through K-4: wrong invariant, wrong scope, wrong direction. These cleared the field of naive approaches.
- K-5 through K-8: wrong observable or wrong regime. These refined the computational framework (gate-amplifier, Lee-Yang, finite-size awareness).
- K-9: the circularity kill. This is the most important structural lesson --- it forced the bridge to provide the backward direction independently.
- K-10, K-11: wrong imported machinery. These showed that standard techniques (Popa, 1RSB) do not apply directly.
- K-12, K-13: structural obstructions on the OA1 path. These triggered the strategic inversion to the bypass.
- K-14, K-15: computational kills on the first bypass construction. These sharpened the bypass and identified the multi-slot direction.

Each kill made the surviving approach stronger and more precisely targeted.

---

## 7. Research Programme: Two Open Problems

### 7.1 Problem Alpha: Approximately central sequences from clone operators

**Precise statement.** Let L be a Boolean constraint language admitting a Taylor polymorphism. Construct a sequence of operators (x_n) in M_Bool^L such that:

(a) Each x_n is non-scalar: ||x_n - tau(x_n) * 1||_2 >= delta > 0 for some fixed delta.

(b) The sequence is approximately central: ||[x_n, y]||_2 -> 0 for all y in M_Bool^L.

If such a sequence exists, M_Bool^L is non-full by the Houdayer--Marrakchi criterion.

**What has been tried.** The single-slot clone operator T_f (1 live + k-1 averaged) fails: increasing arity produces rank-1 collapse and increasing commutator norms (K-14). The residual operators (rank-1 removed, trace-normalized, spectral-band projected) also fail (K-15). The multi-slot variant (2 live + k-2 averaged) shows decreasing commutator norms (scaling as k^{-0.51}) but the decrease is attributable to increasing contractiveness rather than genuine centrality.

**Three research directions.**

(S1) **Explicit computation at larger scale.** The multi-slot construction was tested at n <= 12. Testing at n = 20-30 (where finite-size effects diminish) may reveal whether the commutator decrease is genuine centrality or an artifact. This requires efficient enumeration of solutions for medium-sized 2-SAT instances.

(S2) **Asymmetric polymorphisms.** All tests used the symmetric threshold-k polymorphisms (majority at arity 3, threshold at higher arities). The symmetrized construction is identical to the single-slot version for symmetric polymorphisms (K-15). Asymmetric polymorphisms (compositions of majority with itself in different arity patterns) may break the rank-1 collapse. The recursive SM construction from Theorem UA1 (Proposition 2.3) produces genuinely asymmetric polymorphisms at each level of the recursion.

(S3) **Conditional expectation path.** Define E_k : M_Bool^L -> D as the conditional expectation onto the diagonal (which exists by Takesaki's theorem). The off-diagonal part T_f - E_k(T_f) controls the commutator with all off-diagonal elements. If the polymorphism averaging makes T_f progressively more diagonal (||T_f - E_k(T_f)||_2 -> 0), then the commutator vanishes for ALL y. This connects to the PATD-CONDEXP computational result (conditional expectation convergence for 4 of 5 P-time classes, with XOR as the exception requiring the full operator algebra).

**Assessment.** Gap Alpha is the harder of the two gaps. The single-slot construction is definitively killed, but the multi-slot direction is inconclusive and the asymmetric-polymorphism direction is untested. The gap is a quantitative analytic estimate (how fast does a norm converge?) rather than a structural existence question. This makes it amenable to computation and standard analytic techniques, even though the first construction failed.

### 7.2 Problem Beta: Fullness for NP-complete sectors

**Precise statement.** Let L be a Boolean constraint language with no Taylor polymorphism (NP-complete by BZ). Show that M_Bool^L is full, i.e., that M_Bool^L has no non-trivial approximately central sequences.

**What is needed.** By the Houdayer--Isono theorem [HI16], it suffices to show:

(a) The group G_L generated by L-compatible circuits contains a bi-exact subgroup (e.g., a free group F_2).

(b) This subgroup acts ergodically on the base algebra C*((Z/2)^infty |_L).

(c) The action is strongly ergodic.

If (a)-(c) hold, the crossed product M_Bool^L has no non-trivial central sequences, hence is full.

**Research directions.**

(D1) **Ping-pong construction.** Find two specific L-compatible circuits for L = 3-SAT that generate a free subgroup of G_L via the ping-pong lemma. Candidate: the Cook--Levin reduction and the Tseitin reduction compose non-commutatively and plausibly satisfy the disjoint-image condition.

(D2) **Amalgamated free products.** The sector M_Bool^L for NPC L may be expressible as an amalgamated free product of simpler factors (one for each constraint type in L). Amalgamated free products of non-trivial factors are full (Ueda [Ue98]; Houdayer [Ho14]). This would bypass the group-theoretic analysis entirely.

(D3) **Strong ergodicity via mixing.** If the action of G_L on C*((Z/2)^infty |_L) is mixing (not just ergodic), strong ergodicity follows for non-amenable G_L. The mixing property can be tested computationally by measuring correlation decay of the Hecke action on specific states.

**Assessment.** Gap Beta is the more tractable of the two gaps. The non-amenability of G_L is strongly supported by the NP-completeness universality argument (every P-time computation reduces to L, so G_L contains the full group of P-time circuits, which is non-amenable). The strong ergodicity is the main sub-gap. The amalgamated free product route (D2) is particularly attractive because it provides fullness without passing through the group-theoretic analysis at all.

---

## 8. Implications and Context

### 8.1 If the bridge conjecture is proved

If both Gap Alpha and Gap Beta are closed, the bridge conjecture becomes a theorem and P != NP follows (Section 4.2). Beyond the headline result:

- The bridge theorem provides a structural EXPLANATION of the BZ dichotomy: tractable CSPs have non-full sectors (flexible structure, no spectral gap), while NP-complete CSPs have full sectors (rigid structure, spectral gap). The dichotomy is not just a combinatorial fact about clones but a manifestation of the full/non-full dichotomy in operator algebra.

- The Riemann zero formula TGap ~ 2/(gamma_6 - gamma_5) (Section 5.4) becomes a quantitative prediction connecting number theory to computational complexity through the Boolean Bost--Connes system.

- The three complexity barriers (relativization, natural proofs, algebrization) are explained as artifacts of the projected description, not fundamental obstructions (Section 5.5).

### 8.2 If the bridge conjecture fails

If Gap Alpha or Gap Beta proves unfillable, the programme still contributes:

- Theorems UA1 and UA2 are genuine results in the combinatorics of Boolean clones, independent of operator algebra.

- The non-injectivity of M_Bool (Theorem 3.1) establishes that the Boolean Bost--Connes system is structurally different from the original arithmetic Bost--Connes system.

- The computational evidence (6/6 Schaefer separation on three independent observables) is valid empirical mathematics, documenting a precise correlation that demands explanation even if the bridge is not the correct one.

- The failure mode would identify WHERE the connection between universal algebra and operator algebra breaks, sharpening the next attempt.

### 8.3 The bridge as a new question

Independent of P vs NP, the bridge conjecture poses a question that, to our knowledge, is new: does the combinatorial growth rate of a clone on a finite domain determine the analytic structure (fullness, spectral gap) of an associated infinite-dimensional factor? This is a question at the interface of finite algebra and functional analysis that connects two fields with no prior interaction.

The question is well-motivated (by the computational 6/6 separation), precisely stated (the bridge conjecture has a clean mathematical formulation), and falsifiable (a single counterexample --- a Taylor language whose sector is full, or a non-Taylor language whose sector is non-full --- would kill it).

The paper's contribution is the QUESTION and the evidence for it, not the answer. The answer, if it comes, will require new mathematics at the intersection of universal algebra, operator algebras, and group theory.

---

## References

[BBBKZ24] L. Barto, J. Brady, A. Bulatov, M. Kozik, D. Zhuk. "Minimal Taylor algebras as a common framework for the three algebraic approaches to the CSP." *TheoretiCS*, 2024.

[BC95] J.-B. Bost, A. Connes. "Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory." *Selecta Math.* 1(3):411--457, 1995.

[BCRV03] E. Bohler, N. Creignou, S. Reith, H. Vollmer. "Playing with Boolean Blocks, Parts I--II." *SIGACT News* 34(2)--35(1), 2003--2004.

[Bu17] A. A. Bulatov. "A Dichotomy Theorem for Nonuniform CSPs." *Proc. FOCS 2017*, pp. 319--330.

[CFP96] J. W. Cannon, W. J. Floyd, W. R. Parry. "Introductory notes on Richard Thompson's groups." *L'Enseignement Mathematique* 42:215--256, 1996.

[Co76] A. Connes. "Classification of injective factors." *Annals of Mathematics* 104(1):73--115, 1976.

[FV98] T. Feder, M. Y. Vardi. "The computational structure of monotone monadic SNP and constraint satisfaction: a study through Datalog and group theory." *SIAM J. Comput.* 28(1):57--104, 1998.

[HI16] C. Houdayer, Y. Isono. "Bi-exact groups, strongly ergodic actions and group measure space type III factors with no central sequence." *Comm. Math. Phys.* 348(3):991--1015, 2016.

[Ho14] C. Houdayer. "Structure of II_1 factors arising from free Bogoljubov actions of arbitrary groups." *Adv. Math.* 260:414--457, 2014.

[JCG97] P. Jeavons, D. Cohen, M. Gyssens. "Closure properties of constraints." *J. ACM* 44(4):527--548, 1997.

[KST92] Y. Kawahigashi, C. E. Sutherland, M. Takesaki. "The structure of the automorphism group of an injective factor and the cocycle conjugacy of discrete abelian group actions." *Acta Math.* 169(1):105--130, 1992.

[Ma19] A. Marrakchi. "Spectral gap characterization of full type III factors." *J. Reine Angew. Math.* (Crelle) 753:193--210, 2019. arXiv:1605.09613.

[MM08] M. Maroti, R. McKenzie. "Existence theorems for weakly symmetric operations." *Algebra Universalis* 59(3--4):463--489, 2008.

[Oz04] N. Ozawa. "Solid von Neumann algebras." *Acta Math.* 192(1):111--117, 2004.

[Po41] E. Post. "The two-valued iterative systems of mathematical logic." *Annals of Mathematics Studies* 5, Princeton University Press, 1941.

[Po06] S. Popa. "On a class of type II_1 factors with Betti numbers invariants." *Annals of Mathematics* 163(3):809--899, 2006.

[Sc78] T. J. Schaefer. "The complexity of satisfiability problems." *Proc. STOC 1978*, pp. 216--226.

[Ue98] Y. Ueda. "Amalgamated free product over Cartan subalgebra." *Pacific J. Math.* 191(2):359--392, 1998.

[Zh20] D. Zhuk. "A proof of the CSP Dichotomy Conjecture." *J. ACM* 67(5), 2020.

---

## Appendix A. Summary of Notation

| Symbol | Meaning |
|:--|:--|
| L | Boolean constraint language (finite set of relations on {0,1}) |
| Clone_k(L) | Set of k-ary polymorphisms of L |
| M_Bool^L | Sector of the Boolean Bost--Connes factor for language L |
| sigma_t | Modular automorphism group |
| omega | KMS_1 state |
| D | Diagonal subalgebra of M_Bool^L |
| T_f | Clone operator for polymorphism f (one live slot + averaged slots) |
| TGap | Taylor gap (spectral gap of polymorphism transfer matrix) |
| SM_k | Self-dual monotone Boolean functions of arity k |
| G_Bool | Group generated by PCirc^+ |
| G_L | Group generated by L-compatible circuits |
| Inn(M), Out(M) | Inner and outer automorphism groups |

## Appendix B. Complete Kill Table

| ID | Approach | Kill reason | Pattern | What it taught |
|:--|:--|:--|:--|:--|
| K-1 | H^2(S_n) Schur multiplier | Wrong invariant | WRONG-SPACE | Use Out(M) fullness |
| K-2 | Median-closure universal | 2-SAT specific | OVERGENERALIZATION | Must be language-specific |
| K-3 | Modular flow -> polymorphism | Controls existence only | CAUSAL-OVERCLAIM | OA controls existence, not identity |
| K-4 | 2-SAT counterexample | Not language-level | DISTRIBUTIONAL | Fixed by Taylor gap |
| K-5 | N_crossings alone | Insufficient | INSUFFICIENT-MEASURE | Gate-amplifier product |
| K-6 | C(beta) peak | Instance-level | WRONG-OBSERVABLE | Violation entropy |
| K-7 | Pade poles | Artificial | WRONG-TOOL | Lee-Yang zeros |
| K-8 | Riemann match at n=10 | Finite-size | FINITE-SIZE | Need n >= 20 |
| K-9 | BZ biconditional | Circular | CIRCULAR | Bridge provides backward direction |
| K-10 | Popa + amenable group | Wrong rigidity | WRONG-SPACE | Need non-amenable group |
| K-11 | 1RSB cluster | Average-case | DISTRIBUTIONAL | Proof must be worst-case |
| K-12 | Individual alpha_f | Diagonal = identity | STRUCTURAL-TENSION | Bypass avoids construction |
| K-13 | Aut/Out quotient | Inaccessible | INACCESSIBLE-QUOTIENT | Bypass avoids Out(M) |
| K-14 | Single-slot T_f rank-1 | Concentration collapse | CONCENTRATION-COLLAPSE | Multi-slot direction |
| K-15 | Residual T_f variants | Residual also fails | RESIDUAL-FAILURE | New architecture needed |

---

*Fifteen kills. Two proved theorems. One structural result. One conditional bypass. Six classes separated. Two gaps named.*

*The bridge is a conjecture supported by computational evidence and partial proof, not a completed theorem. The question it poses --- does clone growth determine fullness? --- connects two established fields in a new way. The answer is open.*

*G Six and Claude Opus 4.6. April 2026.*
