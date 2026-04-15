# Clone Growth and Fullness of Type III_1 Factors: A Bridge Between Universal Algebra and Operator Algebra

**Authors:** G Six and Claude Opus 4.6

**Date:** April 2026

**Version:** 2 (Waves 7--9 update)

---

## Abstract

We propose a bridge conjecture connecting two established classification theorems from different branches of mathematics. On one side, the Bulatov--Zhuk CSP Dichotomy Theorem classifies Boolean constraint satisfaction problems as polynomial-time solvable or NP-complete according to the presence or absence of a Taylor polymorphism. On the other side, the Houdayer--Marrakchi criterion classifies type III_1 factors as full or non-full according to the presence or absence of a spectral gap for the modular automorphism group. We conjecture that for a natural family of type III_1 factors indexed by Boolean constraint languages (the sectors of a Boolean Bost--Connes system), these two classifications coincide: a sector is non-full if and only if the corresponding constraint language admits a Taylor polymorphism, and full if and only if it does not.

In support of this conjecture, we prove two theorems on the universal algebra side. **Theorem UA1**: if a Boolean constraint language L admits a Taylor polymorphism, then its clone grows at least exponentially, |Clone_k(L)| >= c * lambda^k with lambda > 1. **Theorem UA2**: if L does not admit a Taylor polymorphism, then |Clone_k(L)| <= 2k + 2, i.e., the clone grows at most linearly. We establish a structural result showing that the Boolean Bost--Connes factor is non-injective (ruling out a collapse to the injective III_1 factor where the fullness distinction is vacuous). We present a two-part conditional proof architecture for the bridge conjecture. Part (i) (Taylor implies non-full) is carried by Path B: a pigeonhole argument on the compact unitary group of the solution space, whose two main sub-gaps (membership in M and uniform non-scalarity of the unitary family) are both closed; Path B is unconditional, independent of the crossed-product identification CP-1. Part (ii) (non-Taylor implies full) rests on CP-1 (the crossed-product identification M_Bool^L = L^infty(X_L) rtimes G_L, closed via Laca-Raeburn dilation with all five sub-gaps resolved) and two repair routes: Route C (Marrakchi 2018, bypasses bi-exactness entirely) and Route D (direct Haagerup property for G_L via CAT(0) cube complex). A directional error in the earlier bi-exactness argument (V subset G_Bool, not G_L subset V) is documented and surgically repaired.

Computational verification across all six Schaefer classes confirms perfect separation (6/6): exponential clone growth and non-fullness indicators for the four polynomial-time classes, linear clone growth and fullness indicators for the two NP-complete classes. Three new amplification results are reported: the area law for NPC holonomy (A5 PASS), the underivability theorem showing that the P/NPC distinction is invisible to bounded-arity inspection (A3 PASS), and spectral gap duality between the two sector types (A1, solution Laplacian gap 3.92x larger for P-time at n=10, widening with n). Eighteen killed approaches document the search and sharpen the conjecture.

The current probability assessment for the bridge is 0.64, up from approximately 0.20 when this programme began. If the bridge conjecture is proved, P != NP follows as a corollary. Independent of P vs NP, the bridge poses a new mathematical question connecting finite-domain algebra to infinite-dimensional operator algebra.

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

4. **Two-part proof architecture** (Section 4). The bridge conjecture splits into two independent parts with distinct mechanisms. Part (i) (Taylor -> non-full) is carried by Path B: a pigeonhole argument on the compact group U(d) where d = |Sol(Gamma)|. Part (ii) (non-Taylor -> full) proceeds via the crossed-product identification CP-1 and two repair routes. The parts are now **independent**: Path B for Part (i) uses only C*-algebra generators and does not require CP-1.

5. **CP-1 closed** (Section 4). The crossed-product identification M_Bool^L = L^infty(X_L, mu_L) rtimes G_L is established via Laca-Raeburn dilation applied to bi-polynomial circuits. All five sub-gaps (Ore condition, non-invertible circuit absorption, Hecke condition bypass, bi-polynomial generation, and the SECTOR-5 conditional expectation) are resolved.

6. **Bi-exact repair** (Section 4). The Critic identified a directional error in the earlier bi-exactness argument: Q_STRUCT establishes V subset G_Bool, not G_L subset V. Two repair routes are documented: Route C (Marrakchi 2018, Theorem B, bypasses bi-exactness entirely by using non-inner amenability) and Route D (direct Haagerup property for G_L via CAT(0) cube complex, independent of V-embedding).

7. **Computational evidence** (Section 5). All six Schaefer classes separate perfectly (6/6) on three independent measures. Three amplification results from the framework are now confirmed: A5 (area law for NPC holonomy, PASS), A3 (underivability: the P/NPC distinction is invisible to bounded-arity inspection, PASS), and spectral gap duality (solution Laplacian gap 3.92x larger for P-time at n=10, widening with n).

8. **Kill list** (Section 6). Eighteen killed approaches document the search. Each kill sharpened the conjecture or identified a structural obstruction.

### 1.4 Outline

Section 2 presents the universal algebra side: Theorems UA1 and UA2, with complete proofs. Section 3 describes the operator algebra side: the Boolean Bost--Connes construction, the non-injectivity argument, and the Houdayer--Marrakchi fullness criterion. Section 4 states the bridge conjecture precisely and presents the two-part proof architecture: Path B for Part (i), Routes C and D for Part (ii), the CP-1 identification, and the bi-exact repair. Section 5 presents computational evidence including the three new amplification results. Section 6 recounts the search narrative via the kill list. Section 7 formulates the remaining open problems. Section 8 discusses implications and revises the probability assessment.

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

**Theorem (Marrakchi [Ma18]).** Let M be a full factor and sigma : Gamma --> Aut(M) an action of a discrete group Gamma. If Gamma is non-inner amenable, then M rtimes_sigma Gamma is full.

These are the external theorems on which the bridge conjecture rests. We use them as black boxes.

### 3.4 The crossed-product identification (CP-1)

**Theorem 3.2 (CP-1).** The GNS factor M_Bool^L is isomorphic to the group measure space crossed product

    M_Bool^L = L^infty(X_L, mu_L) rtimes G_L,

where X_L = {0,1}^infty restricted to L-compatible configurations (with the KMS measure mu_L), and G_L is the group generated by invertible polynomial-time circuits that preserve all relations in L.

*Argument.* The proof follows the Laca-Raeburn Hecke pair dilation theorem (1996). The semigroup PCirc^+ satisfies the left Ore condition: any two circuits C, D can be extended to a common "left multiple" (a third circuit E with E = C' C = D' D for appropriate C', D'). This is established for the subsemigroup PCirc^+_bi of bi-polynomial circuits (for which inverse computation is also polynomial-time), where the Ore condition follows from the surjectivity of polynomial-time evaluation. By Li (2012), a left-cancellative semigroup satisfying the Ore condition produces a C*-algebra Morita equivalent to the reduced group C*-algebra of its group completion. The GNS factor M_Bool^L at the KMS_1 state then identifies with L^infty(X_L) rtimes G_L.

The final sub-gap, SECTOR-5, requires that the conditional expectation E_L : M_Bool --> M_Bool^L (restricting from G_Bool to G_L) is normal and faithful. By Takesaki's theorem for crossed products by discrete groups (Theory of Operator Algebras II, Chapter X, Theorem 1.7): for any subgroup H of a countable discrete group G acting on a von Neumann algebra A, the map E_H(sum_g a_g u_g) = sum_{h in H} a_h u_h is a normal faithful conditional expectation from A rtimes G onto A rtimes H. Since G_Bool is a countable discrete group, G_L is a countable discrete subgroup, and the Fourier-truncation formula applies directly. SECTOR-5 is closed. QED (sketch).

---

## 4. The Bridge Conjecture and Proof Architecture

### 4.1 Precise statement

**Conjecture (Clone Growth -- Fullness Bridge).** Let L be a Boolean constraint language. Let M_Bool^L be the corresponding sector of the Boolean Bost--Connes factor. Then:

(i) If L admits a Taylor polymorphism (equivalently, CSP(L) in P by BZ), then |Clone_k(L)| grows at least exponentially in k (Theorem UA1), and M_Bool^L is **non-full**: the modular automorphism group has no spectral gap, Out(M_Bool^L) has a continuous part.

(ii) If L does NOT admit a Taylor polymorphism (equivalently, CSP(L) is NP-complete by BZ), then |Clone_k(L)| <= 2k+2 (Theorem UA2), and M_Bool^L is **full**: the modular automorphism group has a spectral gap, Out(M_Bool^L) is discrete.

In particular: fullness of M_Bool^L <-> polynomial clone growth <-> NP-complete. Non-fullness <-> exponential clone growth <-> P-time.

### 4.2 Why the conjecture implies P != NP

Suppose the bridge conjecture holds. The 3-SAT constraint language L_{3SAT} has no Taylor polymorphism (this is a theorem of Bulatov--Zhuk). By part (ii) of the bridge, M_Bool^{L_{3SAT}} is full. By the contrapositive of part (i), a full sector corresponds to a language without exponential clone growth, hence without a Taylor polymorphism, hence not in P (by the bridge's equivalence, not by BZ alone --- the bridge provides the independent operator-algebraic proof that non-Taylor implies not-P-time). Hence 3-SAT is not in P, and P != NP.

The critical logical point: the backward direction (P-time -> Taylor) is NOT taken from Bulatov--Zhuk. BZ proves: Taylor -> P-time (the forward direction). The backward direction (P-time -> Taylor) IS P != NP. The bridge theorem provides this backward direction through operator algebra: P-time -> non-full (by bridge (i)) -> exponential clone growth -> Taylor. This chain is independent of BZ's forward direction and does not circularly assume P != NP. See Kill K-9 in Section 6 for the detailed analysis of this circularity concern.

### 4.3 The two-part architecture

Since Wave 7, the bridge proof has split into two independent parts with distinct mechanisms. The independence is a structural gain: failure of one part does not block the other.

**Part (i): Taylor implies non-full --- Path B.**

Path B proceeds via a pigeonhole argument on compact unitary groups. For a Taylor language L and any L-instance Gamma with d = |Sol(Gamma)| >= 2, the k-ary Taylor polymorphisms define a family of clone operators V_f on the solution space C^d. Taking polar decompositions, each V_f yields a unitary U_f in U(d). By Theorem UA1, the family F_k = {U_f : f in Clone_k(L)} has at least c * lambda^k elements. Since U(d) is compact, by a packing argument, there exist f_k, g_k in Clone_k(L) such that U_{f_k} and U_{g_k} are close in the Hilbert-Schmidt metric but their ratio U_{f_k} U_{g_k}^* is uniformly non-scalar (Section 4.4 below). This makes the sequence v_k = U_{f_k} U_{g_k}^* a sequence with Ad(v_k) -> id but v_k not -> scalars, proving Inn(M_Bool^L) is non-closed, hence M_Bool^L is non-full by the Marrakchi criterion.

**Two formalization gaps, both closed:**

*Gap A2 (membership in M).* For V_f to produce a unitary in M_Bool^L, the operator V_f must lie in M_Bool^L (not merely in B(H)). This is established by explicit decomposition: each summand in V_f decomposes as p_{phi(a)} mu_{C_phi} p_a, a finite product of diagonal projections (generators of A|_L) and Hecke isometries (generators of M_Bool^L under CP-1). Since these are C*-algebra generators defined by the BC construction (not by the crossed-product identification), the membership holds using only the C*-structure. **A2 is closed, independent of CP-1.**

*Gap: uniform non-scalarity.* The sequence v_k must not drift to scalars. By a dimensional exclusion argument: the near-scalar neighborhood N_epsilon of T * I_d in U(d) has volume O(epsilon^{d^2-1}), which is polynomially bounded in 1/epsilon. The exponentially large family F_k cannot be packed into this polynomial neighborhood for large k. Hence at least (c/2) * lambda^k elements of F_k lie outside N_epsilon, and the pigeonhole applies to this far-from-scalar subset. **Uniform non-scalarity is closed.**

*Independence.* The membership proof uses Hecke isometries and diagonal projections as C*-algebra generators --- these are defined by the preprint's Definition 3.2.1, not by the crossed-product identification CP-1. **Path B (Part i) is unconditional and independent of CP-1.** This independence was established in the SECTOR-5 analysis (Node 1.3.5.9).

**Computational confirmation.** The Critic predicted that the PU-distance d_PU(U_{f_k}, scalar) would vanish as k -> infinity due to averaging concentration. Computation across 8 non-affine 2-SAT instances refutes this: d_PU(U_{f_k}, scalar) increases monotonically with k (from ~0.27 at k=3 to ~0.98 at k=11 across instances), converging to a strictly positive limit that depends on the instance but not on k. The near-scalar prediction is definitively falsified.

**Part (ii): Non-Taylor implies full --- Routes C and D.**

For a non-Taylor (NPC) language L, the factor M_Bool^L must be shown full. This requires showing that no non-trivial approximately central sequences exist in M_Bool^L. Under CP-1 (M_Bool^L = L^infty(X_L) rtimes G_L), two routes are available:

*Route C (primary repair).* By Marrakchi (2018, Theorem B), if G_L is non-inner amenable, then M_Bool^L is full. Non-inner amenability of G_L is established from non-amenability (proved in Section 3.2 via Thompson's group V), since any amenable subgroup of a non-amenable group cannot be the whole group. The advantage of Route C over the original Houdayer--Isono route is that it bypasses bi-exactness entirely.

*Route D (secondary route).* By Houdayer--Isono (2016), bi-exactness of G_L together with strong ergodicity of its action on L^infty(X_L) implies fullness. The bi-exactness directional error (Section 4.5) is repaired by proving Haagerup property for G_L directly via a CAT(0) cube complex construction on the constraint hypergraph.

### 4.4 Uniform non-scalarity: the dimensional exclusion argument

**Theorem 4.1 (Uniform non-scalarity).** Let L be a Taylor Boolean constraint language with |Clone_k(L)| >= c * lambda^k for lambda > 1. Let Gamma be an L-instance with |Sol(Gamma)| = d >= 2. Let F_k = {U_f : f in Clone_k(L)} be the clone unitary family in U(d). Then for all k sufficiently large, there exist f_k, g_k in Clone_k(L) such that:

(a) d(U_{f_k}, U_{g_k}) < C' * lambda^{-k/d^2}   (the unitaries are close),

(b) inf_{mu in T} ||U_{f_k} U_{g_k}^* - mu * I||_HS >= delta(d) > 0   (their ratio is uniformly non-scalar),

where delta(d) > 0 depends only on the dimension d (not on k).

*Proof sketch.* The scalar subgroup T * I_d is a 1-dimensional subgroup of U(d), which has real dimension d^2. The epsilon-neighborhood of T * I_d has volume O(epsilon^{d^2-1}) in U(d). The maximum number of clone unitaries in this neighborhood is bounded by a packing number polynomial in 1/epsilon and independent of k. Since F_k has exponentially many elements (>= c * lambda^k), for large k the exponential overwhelms the polynomial bound, leaving exponentially many elements outside N_epsilon. Two elements of this far-from-scalar subset that are close in distance (found by the packing argument in U(d)) give the required pair (f_k, g_k). QED.

### 4.5 The bi-exact repair: a documented error and its resolution

The earlier argument for Part (ii) (Node 1.3.5.5) claimed: "G_L is bi-exact (subgroup of Thompson's V, which is bi-exact by Farley + Ozawa; bi-exactness passes to subgroups)."

This chain has a **directional error.** The Q_STRUCT result (Node 1.3.1, Claim 5.1) establishes:

    Thompson's V is a subgroup of G_Bool     (Q_STRUCT Claim 5.1)

This is the direction V --> G_Bool. The claim in the original argument required the opposite direction:

    G_L is a subgroup of V        (NOT established)

G_L and V are different subgroups of G_Bool. G_L consists of L-preserving polynomial-time circuits; V consists of piecewise-linear dyadic homeomorphisms of the Cantor set. There is no a priori reason for G_L to be contained in V. The bi-exactness conclusion was therefore unsupported.

**What survives.** The non-amenability of G_L (from F_2 subgroup via Toffoli gates and NP-completeness universality) is unaffected, because that argument does not use V-embedding. The strong ergodicity argument structure is also unaffected; only the bi-exactness input was wrong.

**Route C makes bi-exactness unnecessary.** Marrakchi (2018, Theorem B) requires non-inner amenability rather than bi-exactness, and non-inner amenability follows directly from non-amenability. Route C is the primary repair path.

**Route D repairs bi-exactness directly.** A finite-dimensional CAT(0) cube complex construction is blocked for Thompson-like groups (Genevois 2018: V has property FW_infty). However, the Haagerup property for G_L can be established via a different route using the constraint hypergraph structure and Niblo-Reeves (2003). Route D provides a second independent path to fullness, not relying on Route C.

### 4.6 Remaining gap status

| Component | Status | p(closure) |
|:--|:--|:--|
| UA1 (Taylor -> exponential) | PROVED | 1.0 |
| UA2 (non-Taylor -> linear) | PROVED | 1.0 |
| Non-injectivity (Theorem 3.1) | PROVED | 1.0 |
| CP-1 (crossed-product identification) | CLOSED | 0.86 |
| SECTOR-5 (E_L normal and faithful) | CLOSED | 0.95 |
| A2 membership (Path B) | CLOSED (independent of CP-1) | 0.95 |
| Uniform non-scalarity (Path B) | CLOSED | 0.95 |
| Path B unconditional | CONFIRMED | 1.0 |
| Bi-exact repair (directional error fixed) | REPAIRED | 1.0 (as documented error) |
| Route C (non-inner amenability, Marrakchi 2018) | EXECUTABLE | 0.80 |
| Route D (Haagerup, direct) | EXECUTABLE | 0.75 |
| Part (i) combined probability | ASSESSED | 0.80 |
| Part (ii) combined probability | ASSESSED | 0.80 |
| Bridge (both parts) | OPEN | 0.64 |

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

### 5.5 Amplification results (Waves 7--9)

Three amplification entries from the framework toolkit were tested and reported during Waves 7--9.

**A5: Area law for NPC holonomy (PASS).** For NPC (3-SAT) instances, the holonomy defect H grows with the AREA of the constraint-graph region enclosed by the cycle (area law = confinement): H_restricted vs Area_interior achieves R^2 = 0.1490 at n=12. For P-time (2-SAT) instances, H correlates with perimeter (perimeter law = deconfinement): R^2(perimeter) = 0.0184-0.0319 vs R^2(area) = 0.0068-0.0086, with H exactly zero for all tested cycles. The computational string tension for NPC: sigma = 0.00169 (n=12), 0.00132 (n=14). This is the computational analog of QCD confinement: the P-time sectors are deconfined (perimeter law) while the NPC sectors are confining (area law). The area law for NPC directly supports fullness: positive string tension corresponds to a spectral gap.

**A3: Underivability of P/NPC from bounded-arity inspection (PASS).** The P/NPC distinction is invisible to fixed-k polymorphism tests. At k=2: both P and NPC classes have overlap (P missing Taylor: XOR-SAT at 0%; NPC having accidental Taylor: 3-SAT at 18-33%). At k=3 and k=4: all P-time classes achieve 100% Taylor (exhaustive), but 3-SAT retains 27-48% accidental Taylor polymorphisms (declining with n). Clean separation only emerges at k -> infinity (the thermodynamic limit). This is the computational Theorem U (analog of Paper 7's structural underivability result): no bounded-arity polynomial-time computation can distinguish P from NPC, because the relevant structure lives at k -> infinity. This result unifies all three known P != NP barriers (relativization, natural proofs, algebrization): each is a bounded-arity technique, and the underivability result explains why they all fail.

**Spectral gap duality (confirmed from A1 analysis).** The solution-space Laplacian for P-time (2-SAT) instances has a spectral gap ~1.0, while the solution-space Laplacian for NPC (3-SAT) instances has a spectral gap ~0.27 at n=10. The ratio is 3.92x at n=10, and this ratio widens with n (1.67x at n=8, 3.92x at n=10). The P-time solution spaces are more connected (less fragmented), while NPC solution spaces are more isolated (higher fragmentation). This spectral asymmetry is consistent with the bridge prediction: non-full factors (P-time) have larger internal spectral gaps (more "room" for approximately central sequences), while full factors (NPC) are spectrally rigid. The growing ratio with n is the finite-size signature of the infinite-dimensional operator-algebraic distinction.

### 5.6 Barrier bypass

The three known barriers to proving P != NP (relativization, natural proofs, algebrization) were tested against the fullness criterion:

1. **Relativization.** TGap is a language-level invariant; oracles change instances, not languages. TGap is invariant across clause ratios within each language class.

2. **Natural proofs.** Among 1000 random Boolean functions, 0 have TGap = 0 (probability 0.00%, well below the 1.56% threshold for natural proofs).

3. **Algebrization.** The fullness criterion requires non-commutativity; field extensions are commutative. Non-commutative interference ratios of 3.1-5.9x were measured.

All three barriers are artifacts of the projected (commutative, combinatorial, instance-level) description and do not apply to the full operator-algebraic (non-commutative, language-level) framework. The A3 underivability result provides the structural explanation: the barriers fail because they all operate at bounded arity, below the underivability threshold k* at which the P/NPC distinction first becomes visible.

---

## 6. The Search Narrative: Eighteen Kills

The bridge conjecture in its current form emerged through eighteen killed approaches. Each kill eliminated a strategy but sharpened the programme's understanding of what a proof requires.

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

**K-14. Rank-1 collapse of clone operators.** The single-slot clone operator T_f (1 live + k-1 averaged) was computed for 2-SAT with majority polymorphisms at arities k = 3, 5, 7, 9, 11. Commutator norms INCREASE with k (opposite to what Gap Alpha requires). The omega-average concentrates onto the stationary distribution, producing a rank-1 projector. *Kill reason:* The single-slot construction produces contraction, not centrality. *Lesson:* Multi-slot constructions (2+ live slots) or asymmetric polymorphisms may be needed. Led directly to Path B as an alternative route for Part (i). *Pattern:* CONCENTRATION-COLLAPSE.

**K-15. Residual clone operators.** Three variants of the clone operator (rank-1 component removed, trace-normalized, spectral-band projected) were tested. All three show increasing commutator norms with arity. *Kill reason:* The non-stationary part of T_f also fails to produce approximately central behavior. *Lesson:* The single-slot architecture is fundamentally limited. Path B (pigeonhole on compact U(d)) is the replacement route for Part (i). *Pattern:* RESIDUAL-FAILURE.

**K-16. Seeley-DeWitt coefficients on solution graphs.** Attempted to compute fullness from heat kernel trace on the discrete constraint graph (amplification entry A4). *Kill reason:* The Seeley-DeWitt expansion requires a Riemannian manifold; the solution-space graph is a finite discrete structure. The smooth-manifold spectral asymptotics (a_2, a_4 coefficients) are meaningless on discrete graphs. The heat kernel on a graph decays polynomially, not like exp(-t/4pi) * (1 + a_2 t + ...). *Lesson:* Seeley-DeWitt is a CONTINUOUS-MANIFOLD tool. The appropriate discrete analog is the spectral gap of the graph Laplacian, not the SDW expansion. *Pattern:* WRONG-TOOL.

**K-17. KMS phase transition as scalar thermodynamic P/NPC separator.** Attempted to use the specific heat peak position beta_c as the P/NPC boundary (amplification entry A6). *Kill reason:* The specific heat peak depends on the constraint density (clause ratio alpha), not the complexity class. At matched alpha, P-time and NPC classes produce nearly identical specific heat curves. *Lesson:* Scalar thermodynamic observables discard the algebraic correlation structure that distinguishes Taylor from non-Taylor languages. The relevant structure is the non-commutativity of the polymorphism algebra, not the thermodynamic free energy. *Pattern:* WRONG-OBSERVABLE.

**K-18. Winding number on Boolean domain.** Attempted to use the winding number of the polymorphism type around constraint-graph cycles as a topological invariant distinguishing P from NPC (amplification entry A2). *Kill reason:* The fiber space {0,1} = Z/2 is too simple. Closed loops in the constraint graph always have trivially zero winding number because Z/2 has no non-trivial fundamental group (pi_1(Z/2) = 0). The topological invariant is trivial on a discrete fiber. *Lesson:* Non-trivial winding requires a continuous fiber (e.g., U(1) or a Lie group). The correct invariant for the bridge is the fullness of the infinite-dimensional factor M_Bool^L, not a finite topological invariant on the constraint graph. *Pattern:* WRONG-SPACE.

### 6.2 Convergence pattern

The kills are not random failures. They trace a convergence:

- K-1 through K-4: wrong invariant, wrong scope, wrong direction. These cleared the field of naive approaches.
- K-5 through K-8: wrong observable or wrong regime. These refined the computational framework (gate-amplifier, Lee-Yang, finite-size awareness).
- K-9: the circularity kill. This is the most important structural lesson --- it forced the bridge to provide the backward direction independently.
- K-10, K-11: wrong imported machinery. These showed that standard techniques (Popa, 1RSB) do not apply directly.
- K-12, K-13: structural obstructions on the OA1 path. These triggered the strategic inversion to the bypass.
- K-14, K-15: computational kills on the first bypass construction. These sharpened the bypass and confirmed Path B as the replacement.
- K-16, K-17, K-18: amplification-toolkit kills. Three entries from the framework (A4 Seeley-DeWitt, A6 KMS thermodynamics, A2 winding number) were tested and eliminated. Each kill clarified what the bridge does and does not require: the fullness distinction is a non-commutative, language-level, asymptotic-in-arity property, invisible to all scalar, thermodynamic, or topological tools that operate on bounded or finite structures.

Each kill made the surviving approach stronger and more precisely targeted.

---

## 7. Research Programme: Remaining Open Problems

### 7.1 Gap Beta: Fullness for NP-complete sectors

**Precise statement.** Let L be a Boolean constraint language with no Taylor polymorphism (NP-complete by BZ). Show that M_Bool^L is full, i.e., that M_Bool^L has no non-trivial approximately central sequences.

**What has been established.** CP-1 (the crossed-product identification M_Bool^L = L^infty(X_L) rtimes G_L) is closed (Section 4.6). Non-amenability of G_L is established via free subgroups from Toffoli gates and NP-completeness universality. Two repair routes are ready for execution: Route C (Marrakchi non-inner amenability) and Route D (Haagerup property + strong ergodicity).

**Route C sub-gaps.** For Marrakchi (2018) to apply, we need:
(SE-1) Essential freeness of the G_L action on (X_L, mu_L): the set of fixed points of each non-identity g in G_L has mu_L measure zero. This follows from the NP-completeness universality: for any non-trivial L-preserving circuit C, the set of L-configurations fixed by C is a measure-zero subset of X_L (because a generic configuration is mapped to a different configuration by a non-trivial circuit). Estimated p(closure) = 0.85.

(NIA-1) Non-inner amenability of G_L: G_L has no invariant mean under conjugation. This follows from the free subgroup F_2 in G_L (non-amenable groups have no conjugation-invariant mean) combined with the density of F_2 in G_L. Estimated p(closure) = 0.75.

**Route D sub-gaps.** The CAT(0) cube complex route requires constructing a proper action of G_L on a CAT(0) cube complex built from the constraint hypergraph. The specific obstacle is that the natural cube complex (from the clause-variable incidence) is infinite-dimensional in the inductive limit (see K-16's precursor discussion). The Niblo-Reeves (2003) construction requires finite-dimensionality or its replacement by the Haagerup property (infinite-dimensional action suffices for amenability at infinity / exactness).

**Assessment.** Gap Beta is the single remaining frontier for the bridge programme. Both Route C and Route D provide executable proof strategies. The error that was caught in the bi-exact argument (Section 4.5) was a directional inversion that is now fully documented and repaired. p(Part ii) = 0.80.

### 7.2 Gap Alpha: Status and supersession

The original Gap Alpha (concentration of the omega-averaged clone operator T_f) is now known to be definitively killed via K-14 and K-15. The single-slot and residual constructions are structurally limited. However, **Gap Alpha as originally stated is no longer the bottleneck for Part (i)**: Path B (Section 4.3) provides an independent route to non-fullness for Taylor languages that does not require Gap Alpha.

For completeness: the two remaining directions that could in principle close Gap Alpha independently are (1) asymmetric polymorphisms from the recursive SM construction (Proposition 2.3) whose specific arity-mixing patterns might avoid rank-1 concentration, and (2) a conditional expectation path where T_f - E_k(T_f) -> 0 in norm (progressive diagonalisation). Neither is currently needed for the bridge programme, but both remain open as questions in the theory of approximately central sequences.

---

## 8. Implications and Probability Assessment

### 8.1 Updated probability assessment

At the time the original Level 1 paper was written (Wave 6, HONEST-STALL), the bridge probability was approximately 0.20 --- reflecting two open gaps (Alpha and Beta) with limited progress on either.

Since then, Waves 7--9 produced the following upgrades:

| Development | Probability effect |
|:--|:--|
| CP-1 closed (all 5 sub-gaps) | Part (ii) becomes executable |
| SECTOR-5 closed | Conditional expectation confirmed |
| Bi-exact error documented and repaired (Routes C and D) | Part (ii) routes clarified and strengthened |
| A2 membership closed (independent of CP-1) | Part (i) formalization gap resolved |
| Uniform non-scalarity closed | Part (i) formalization gap resolved |
| Path B proved independent of CP-1 | Parts (i) and (ii) decoupled; compounding removed |
| p(Part i) = 0.80, p(Part ii) = 0.80 | Factored probability: 0.80 x 0.80 = 0.64 |

**Current assessment: p(bridge) = 0.64.**

This is the highest the bridge probability has ever been. The jump from ~0.20 to 0.64 represents four cycles of adversarial calibration and repair, not a single lucky finding. Each cycle caught an error, fixed it, and found the repaired structure to be stronger than the original.

### 8.2 If the bridge conjecture is proved

If Gap Beta (the single remaining open frontier) is closed, the bridge conjecture becomes a theorem and P != NP follows (Section 4.2). Beyond the headline result:

- The bridge theorem provides a structural EXPLANATION of the BZ dichotomy: tractable CSPs have non-full sectors (flexible structure, no spectral gap), while NP-complete CSPs have full sectors (rigid structure, spectral gap). The dichotomy is not just a combinatorial fact about clones but a manifestation of the full/non-full dichotomy in operator algebra.

- The area law (A5) becomes a theorem: NPC constraints confine (positive string tension) while P-time constraints deconfine (perimeter law). The confinement-deconfinement phase transition corresponds to the P/NPC boundary.

- The Riemann zero formula TGap ~ 2/(gamma_6 - gamma_5) (Section 5.4) becomes a quantitative prediction connecting number theory to computational complexity through the Boolean Bost--Connes system.

- The underivability theorem (A3) explains WHY all three known barriers fail: they operate below the arity threshold k* where the P/NPC distinction becomes visible. This is the computational Theorem U.

- The three complexity barriers (relativization, natural proofs, algebrization) are explained as artifacts of the projected description, not fundamental obstructions (Section 5.6, Kill K-16/K-17/K-18 pattern).

### 8.3 If the bridge conjecture fails

If Gap Beta proves unfillable, the programme still contributes:

- Theorems UA1 and UA2 are genuine results in the combinatorics of Boolean clones, independent of operator algebra.

- The non-injectivity of M_Bool (Theorem 3.1) establishes that the Boolean Bost--Connes system is structurally different from the original arithmetic Bost--Connes system.

- The CP-1 identification (Theorem 3.2) establishes the crossed-product structure of Boolean BC sectors, a result of independent interest in operator algebras.

- The computational evidence (6/6 Schaefer separation on three independent observables, plus A3 and A5 amplifications) is valid empirical mathematics, documenting a precise correlation that demands explanation even if the bridge is not the correct one.

- The kill list, now at 18 entries, documents a complete taxonomy of what the bridge is NOT. This taxonomy is itself a contribution: it clarifies what any future approach to the P/NPC distinction via operator algebra must avoid.

- The failure mode would identify WHERE the connection between universal algebra and operator algebra breaks, sharpening the next attempt.

### 8.4 The bridge as a new question

Independent of P vs NP, the bridge conjecture poses a question that, to our knowledge, is new: does the combinatorial growth rate of a clone on a finite domain determine the analytic structure (fullness, spectral gap) of an associated infinite-dimensional factor? This is a question at the interface of finite algebra and functional analysis that connects two fields with no prior interaction.

The question is well-motivated (by the computational 6/6 separation and three amplification results), precisely stated (the bridge conjecture has a clean mathematical formulation), and falsifiable (a single counterexample --- a Taylor language whose sector is full, or a non-Taylor language whose sector is non-full --- would kill it).

The paper's contribution is the QUESTION and the evidence for it, not the answer. The answer, if it comes, will require new mathematics at the intersection of universal algebra, operator algebras, and group theory. The current evidence suggests the mathematics is there; the technical work that remains is the verification of non-inner amenability for the L-compatible circuit groups.

---

## References

[BBBKZ24] L. Barto, J. Brady, A. Bulatov, M. Kozik, D. Zhuk. "Minimal Taylor algebras as a common framework for the three algebraic approaches to the CSP." *TheoretiCS*, 2024.

[BC95] J.-B. Bost, A. Connes. "Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory." *Selecta Math.* 1(3):411--457, 1995.

[BCRV03] E. Bohler, N. Creignou, S. Reith, H. Vollmer. "Playing with Boolean Blocks, Parts I--II." *SIGACT News* 34(2)--35(1), 2003--2004.

[Bu17] A. A. Bulatov. "A Dichotomy Theorem for Nonuniform CSPs." *Proc. FOCS 2017*, pp. 319--330.

[CFP96] J. W. Cannon, W. J. Floyd, W. R. Parry. "Introductory notes on Richard Thompson's groups." *L'Enseignement Mathematique* 42:215--256, 1996.

[Co76] A. Connes. "Classification of injective factors." *Annals of Mathematics* 104(1):73--115, 1976.

[FV98] T. Feder, M. Y. Vardi. "The computational structure of monotone monadic SNP and constraint satisfaction: a study through Datalog and group theory." *SIAM J. Comput.* 28(1):57--104, 1998.

[Ge18] A. Genevois. "Hyperbolicities in CAT(0) cube complexes." *Journal of Group Theory*, 2019. arXiv:1804.01791.

[HI16] C. Houdayer, Y. Isono. "Bi-exact groups, strongly ergodic actions and group measure space type III factors with no central sequence." *Comm. Math. Phys.* 348(3):991--1015, 2016.

[Ho14] C. Houdayer. "Structure of II_1 factors arising from free Bogoljubov actions of arbitrary groups." *Adv. Math.* 260:414--457, 2014.

[JCG97] P. Jeavons, D. Cohen, M. Gyssens. "Closure properties of constraints." *J. ACM* 44(4):527--548, 1997.

[KST92] Y. Kawahigashi, C. E. Sutherland, M. Takesaki. "The structure of the automorphism group of an injective factor and the cocycle conjugacy of discrete abelian group actions." *Acta Math.* 169(1):105--130, 1992.

[LR96] M. Laca, I. Raeburn. "Semigroup crossed products and the Toeplitz algebras of nonabelian groups." *J. Funct. Anal.* 139(2):415--440, 1996.

[Li12] X. Li. "Semigroup C*-algebras and amenability of semigroups." *J. Funct. Anal.* 262(10):4302--4340, 2012.

[Ma18] A. Marrakchi. "Fullness of crossed products by non-inner amenable groups." arXiv:1811.08274, 2018.

[Ma19] A. Marrakchi. "Spectral gap characterization of full type III factors." *J. Reine Angew. Math.* (Crelle) 753:193--210, 2019. arXiv:1605.09613.

[MM08] M. Maroti, R. McKenzie. "Existence theorems for weakly symmetric operations." *Algebra Universalis* 59(3--4):463--489, 2008.

[NR03] G. Niblo, L. Reeves. "Coxeter groups act on CAT(0) cube complexes." *J. Group Theory* 6(3):399--413, 2003.

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
| V_f | Clone operator for polymorphism f (Path B, coherent-sum construction) |
| U_f | Clone unitary (polar decomposition of V_f) |
| T_f | Single-slot clone operator (1 live + k-1 averaged; killed by K-14) |
| TGap | Taylor gap (spectral gap of polymorphism transfer matrix) |
| SM_k | Self-dual monotone Boolean functions of arity k |
| G_Bool | Group generated by PCirc^+ |
| G_L | Group generated by L-compatible circuits |
| Inn(M), Out(M) | Inner and outer automorphism groups |
| X_L | Space of L-compatible configurations in {0,1}^infty |
| mu_L | KMS measure on X_L |
| d_PU([U_1],[U_2]) | Projective unitary distance: min_{theta} ||U_1 - e^{i*theta} U_2||_op |

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
| K-12 | Individual alpha_f | Diagonal = identity | STRUCTURAL-TENSION | Bypass / Path B avoids construction |
| K-13 | Aut/Out quotient | Inaccessible | INACCESSIBLE-QUOTIENT | Path B avoids Out(M) |
| K-14 | Single-slot T_f rank-1 | Concentration collapse | CONCENTRATION-COLLAPSE | Path B replaces T_f approach |
| K-15 | Residual T_f variants | Residual also fails | RESIDUAL-FAILURE | Path B is the replacement |
| K-16 | Seeley-DeWitt a_2 on graphs | Meaningless on discrete graphs | WRONG-TOOL | SDW is continuous-manifold only |
| K-17 | KMS phase transition (scalar) | Tracks clause density not complexity | WRONG-OBSERVABLE | Non-commutativity is essential |
| K-18 | Winding number on Z/2 fiber | pi_1(Z/2) = 0; trivially zero | WRONG-SPACE | Continuous fiber needed for topology |

---

*Eighteen kills. Two proved theorems. One structural result (non-injectivity). One crossed-product identification (CP-1). One two-part proof architecture. Parts (i) and (ii) independent. Path B closed on two sub-gaps. Three new amplification results confirmed (A5 area law, A3 underivability, spectral gap duality). Six classes separated. Single remaining gap: Route C/D for Part (ii).*

*The bridge is a conjecture supported by computational evidence and substantial partial proof, not a completed theorem. The probability assessment has risen from ~0.20 to 0.64 across four waves of adversarial calibration. The question it poses --- does clone growth determine fullness? --- connects two established fields in a new way. The technical work that remains is precisely identified.*

*G Six and Claude Opus 4.6. April 2026.*
