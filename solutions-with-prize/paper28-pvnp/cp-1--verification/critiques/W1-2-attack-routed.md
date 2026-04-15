# W1-2 Adversarial Attack on Proposition 6.2 (Route D Compatibility -- Non-Taylor Case)

**Attacker:** Critic Agent (ORA W1-2)
**Target:** Proposition 6.2 of Node 2.1 (CP-1 Formal Proof)
**Date:** 2026-04-12
**Sources examined:** Node 2.1 (lines 354-393), Node 1.3.5.9 (Sections 4.7-4.9, Claim 4.9.1)

---

## Attack Vector 1: The Polymorphism Rigidity Argument

**Claim under attack:** "Any operation that preserves all L-instances is a polymorphism of L." Applied to the restriction g|_{X_L}, the proof asserts this partial injection is (or gives rise to) a polymorphism.

**Attack.** A polymorphism of L is a function f: D^k -> D that preserves every relation R in L coordinate-wise: if (a_1,...,a_r) in R and (b_1,...,b_r) in R, then (f(a_1,b_1,...), ..., f(a_r,b_r,...)) in R. The arity k is fundamental. A bijection g: {0,1}^n -> {0,1}^n is a UNARY function on {0,1}^n (takes one n-bit string, returns one n-bit string). It is NOT a k-ary polymorphism for k >= 2. The proof's claim that g|_{X_L} yields a "non-trivial multi-ary polymorphism" requires an intermediate construction that is never made explicit.

**Assessment.** The proof does contain the phrase "by composing with projections, we can extract a non-trivial k-ary polymorphism" (Node 1.3.5.9, Section 4.9), but the extraction mechanism is not spelled out. The idea appears to be: if g acts non-trivially on multiple coordinates simultaneously when mapping solutions to solutions, one can decompose g into coordinate functions g_i(x_1,...,x_n), and if g_i depends essentially on more than one coordinate, then viewing g_i as a polymorphism on the individual bits yields a multi-ary polymorphism.

This reasoning is actually correct in spirit but requires a precise bridge. The coordinate functions g_i: {0,1}^n -> {0,1} are indeed n-ary operations on the Boolean domain D = {0,1}. If g maps X_L to X_L (i.e., preserves solution sets), then each coordinate function g_i, when restricted to X_L, preserves the projection of L-relations onto the i-th coordinate in a suitable sense. More precisely, the tuple (g_1,...,g_n) viewed as a single operation f: D^n -> D^n satisfies: for every constraint C = (R, (j_1,...,j_r)) in the L-instance defining X_L, if (x_{j_1},...,x_{j_r}) in R, then (g_{j_1}(x),...,g_{j_r}(x)) in R. This makes each coordinate function g_i (restricted to X_L) a unary polymorphism of L in the standard sense.

But the proof wants MORE: it wants to conclude that if g does NOT globally preserve X_L, then g witnesses a multi-ary polymorphism. This is the non-trivial step. The argument should be: g is a unary operation on {0,1}^n that partially preserves X_L. If it preserves X_L on some but not all inputs, then defining phi(z) = g(z) for z in X_L with g(z) in X_L does NOT give a total polymorphism -- it gives a PARTIAL operation. Partial operations are not polymorphisms in the standard CSP sense. The proof conflates partial solution-preserving maps with polymorphisms.

However, there is a rescue. The non-Taylor characterization (Barto-Kozik) applies to the CLONE of L, which consists of ALL total polymorphisms. The key theorem is: L is non-Taylor iff every polymorphism of L is essentially unary. If g globally preserves X_L (i.e., g(X_L) subset X_L), then g restricted to X_L gives a unary polymorphism. The proof's strategy is: assume g does not globally preserve X_L but does send y to x (both in X_L). This means g is NOT a polymorphism of L (since it doesn't totally preserve X_L). The proof then wants to derive a contradiction, but the contradiction should come from a DIFFERENT source.

Re-reading the proof more carefully: the contradiction argument in Proposition 6.2 (lines 365-376) is actually trying to say that g's restriction to X_L, wherever it maps into X_L, decomposes into essentially unary operations (because non-Taylor forces this). This decomposition then allows constructing g' in G_L. The argument is NOT that g itself is a multi-ary polymorphism. It is that any operation preserving L-instances must be essentially unary, and therefore g's behavior on X_L (where it does map solutions to solutions) must be coordinate-wise.

**Verdict: WEAKENED.** The proof's language is imprecise -- it says "multi-ary polymorphism" when the correct statement involves the coordinate structure of g restricted to X_L. The logical core is salvageable: for non-Taylor L, any total map X_L -> X_L that preserves all L-constraints must be essentially unary. But the proof does not carefully distinguish between (a) g as a total map on {0,1}^n, (b) g restricted to X_L as a partial map, and (c) the coordinate functions of g as polymorphisms. The imprecision is fixable but currently constitutes a gap.

---

## Attack Vector 2: The "Essentially Unary" Decomposition

**Claim under attack:** "A bijection g that respects L-constraints on X_L must therefore decompose into coordinate-wise operations on X_L."

**Attack.** "Essentially unary" in clone theory means: a function f: D^k -> D depends on at most one of its k inputs. But g: {0,1}^n -> {0,1}^n is a UNARY function (k=1) on the set {0,1}^n. Every unary function trivially depends on at most one input (itself). So saying g is "essentially unary" as a 1-ary polymorphism is vacuous.

The proof appears to confuse two distinct levels:
- Level 1: g as a 1-ary operation on {0,1}^n (the set of n-bit strings). At this level, "essentially unary" is trivially satisfied.
- Level 2: Each coordinate function g_i: {0,1}^n -> {0,1} as an n-ary operation on {0,1}. At this level, "essentially unary" means g_i depends on at most one of the n input bits.

The non-Taylor characterization operates at Level 2: every polymorphism f: D^k -> D of L depends on at most one coordinate. Applied to the coordinate functions g_i (which are n-ary operations on D = {0,1}), this says each g_i depends on at most one input bit.

**Assessment.** If each g_i depends on at most one bit, then g is a "wiring with possible negations" -- each output bit is either a copy or negation of exactly one input bit. Such maps form a very restricted class (essentially the hyperoctahedral group acting on coordinates). This is a strong structural conclusion, and it IS correct for polymorphisms of non-Taylor Boolean constraint languages.

But there is a critical issue: g_i is a polymorphism of L ONLY IF g totally preserves X_L. The proof is in a situation where g does NOT totally preserve X_L. The coordinate functions g_i do not define polymorphisms of L in the standard sense (because g does not map all of X_L into X_L). So the Barto-Kozik theorem cannot be applied directly.

The rescue would be: even a partial preservation of X_L by g implies something about the coordinate dependence of g_i. But this is NOT what Barto-Kozik says. Barto-Kozik characterizes TOTAL polymorphisms.

**Verdict: WEAKENED.** The confusion between arity levels is a genuine conceptual error in the proof's exposition, though the underlying mathematical fact (non-Taylor Boolean clones have only essentially unary polymorphisms) is correct. The critical gap is the application of this fact to partial maps. The proof needs an additional argument: either (a) show that g can be modified to totally preserve X_L (which is exactly what the proof tries to do with g', creating a circularity), or (b) cite a result about partial polymorphisms being essentially unary for non-Taylor languages. Option (b) would require Barto-Kozik-style results for partial operations, which exist in the literature (partial clone theory, Romov 1981, Lau 2006) but are not cited.

---

## Attack Vector 3: The Construction of g'

### 3a: Decidability of "z in X_L"

**Claim under attack:** "The test 'z in X_L' is decidable (X_L is defined by finitely many local constraint checks per coordinate window)."

**Attack.** X_L is defined as the set of all infinite binary strings x in {0,1}^infty such that x is L-compatible, meaning every finite window of x satisfies all L-constraints. For an INFINITE string, checking L-compatibility requires verifying infinitely many constraints (one for each finite window position). This is not a finite computation.

**Assessment.** However, the circuits g operate on FINITE strings {0,1}^n for some finite n. The restriction of X_L to n bits is X_L^{(n)} = the set of n-bit strings satisfying all L-constraints on those n bits. This is a finite set, and membership is decidable by checking all O(n^{ar(L)}) constraints (where ar(L) is the maximum arity of relations in L). For fixed L, this is polynomial in n.

The proof's language about "finitely many local constraint checks per coordinate window" is correct when understood as applying to finite-dimensional projections. Since g operates on {0,1}^n, the test "z in X_L^{(n)}" is indeed polynomial-time.

**Verdict: SURVIVED.** The decidability claim is correct for the finite-dimensional setting in which circuits operate. The language could be more precise about the distinction between the infinite inverse limit X_L and the finite approximations X_L^{(n)}, but the mathematical content is sound.

### 3b: Invertibility of g'

**Claim under attack:** g' defined piecewise is invertible with polynomial-time inverse.

**Attack.** Define:
- g'(z) = g(z) if z in X_L and g(z) in X_L
- g'(z) = z otherwise

Consider z in X_L with g(z) not in X_L. Then g'(z) = z (identity). Now consider z' = g^{-1}(z). If z' is not in X_L, then g'(z') = z' (identity, since z' not in X_L). But if z' IS in X_L, then g(z') = z which is in X_L, so g'(z') = g(z') = z. So g' maps both z (via identity) and z' (via g) to different targets -- no collision here.

But what about injectivity? Suppose g'(z_1) = g'(z_2) = w. If both z_1, z_2 are in the "identity" branch, then z_1 = z_2 = w. If both are in the "g" branch, then g(z_1) = g(z_2) = w, and since g is injective, z_1 = z_2. The problem arises in the MIXED case: z_1 is in the identity branch (g'(z_1) = z_1 = w) and z_2 is in the g branch (g'(z_2) = g(z_2) = w). Then w = z_1 and g(z_2) = w = z_1. For this to happen: z_1 not in X_L or g(z_1) not in X_L (so z_1 is on the identity branch), AND z_2 in X_L, g(z_2) in X_L, and g(z_2) = z_1.

Case: z_1 not in X_L and z_2 in X_L with g(z_2) = z_1. But g(z_2) = z_1 not in X_L means z_2 is in X_L but g(z_2) not in X_L. So z_2 falls on the identity branch too: g'(z_2) = z_2, not g(z_2). Contradiction with g'(z_2) = w = z_1. So z_2 = z_1, which means z_1 = z_2.

Case: z_1 in X_L, g(z_1) not in X_L (identity branch), z_2 in X_L, g(z_2) in X_L (g branch), g(z_2) = z_1. Then g'(z_2) = g(z_2) = z_1 and g'(z_1) = z_1 (identity). So g'(z_1) = g'(z_2) = z_1 with z_1 != z_2 (since g is a bijection and g(z_2) = z_1 != z_2 unless g(z_2) = z_2, but then z_1 = z_2). Wait -- z_1 and z_2 are distinct (z_2 in X_L maps to z_1 in X_L via g, and z_1 in X_L maps to something outside X_L via g). We have g'(z_1) = z_1 and g'(z_2) = z_1. So g' is NOT INJECTIVE.

**This is a genuine bug.** g' as defined is not necessarily injective. The piecewise definition creates collisions: z_2 maps to z_1 via g (since both are in X_L and g(z_2) = z_1 in X_L), while z_1 maps to itself (since g(z_1) is not in X_L). Both map to z_1 under g'.

**Concrete example.** Let X_L = {00, 01, 10} in {0,1}^2. Let g be the cyclic permutation 00 -> 01 -> 10 -> 11 -> 00. Then:
- g(00) = 01 in X_L, g(01) = 10 in X_L, g(10) = 11 not in X_L, g(11) = 00 in X_L.
- g'(00) = 01 (both in X_L), g'(01) = 10 (both in X_L), g'(10) = 10 (identity, since g(10) not in X_L), g'(11) = 11 (identity, since 11 not in X_L).
- g' maps: 00 -> 01, 01 -> 10, 10 -> 10, 11 -> 11.
- g' is injective here. Let me find a real counterexample.

Try: X_L = {00, 01, 11}. g: 00 -> 01, 01 -> 11, 11 -> 10, 10 -> 00.
- g(00) = 01 in X_L: g branch. g(01) = 11 in X_L: g branch. g(11) = 10 not in X_L: identity branch. g(10) = 00 in X_L, but 10 not in X_L: identity branch.
- g'(00) = 01, g'(01) = 11, g'(11) = 11, g'(10) = 10.
- g'(01) = g'(11) = 11. NOT INJECTIVE.

**Verdict: BROKEN.** The construction of g' as stated is not guaranteed to be injective. The piecewise definition can create collisions when z_2 in X_L maps via g to some z_1 in X_L, but z_1 maps to itself because g(z_1) leaves X_L. Then g'(z_2) = g(z_2) = z_1 = g'(z_1). This is a concrete, demonstrable failure of injectivity.

### 3c: g' as a valid circuit

**Attack.** Even if invertibility were repaired, the piecewise definition of g' requires a conditional branch: "if z in X_L and g(z) in X_L, apply g; otherwise, apply identity." This is a valid polynomial-time computation (since the X_L membership test is poly-time, as established in 3a). So this sub-attack does not succeed independently.

**Verdict: SURVIVED** (contingent on 3a, which survived).

---

## Attack Vector 4: Logical Structure of the Proof

**Claim under attack:** The proof assumes g does not preserve X_L, then claims L has a multi-ary polymorphism, contradicting non-Taylor.

**Attack.** The logical chain requires:
1. g in G_Bool maps y to x, both in X_L, but g not in G_L (does not globally preserve X_L).
2. Therefore g's restriction to X_L is a partial injection preserving some solutions.
3. Therefore this partial injection is (or yields) a polymorphism.
4. This polymorphism is multi-ary (not essentially unary).
5. This contradicts non-Taylor.

Steps 2-3 are problematic (see Attack Vector 1): a partial injection is not a total polymorphism. Step 4 is problematic (see Attack Vector 2): a unary map g on {0,1}^n can be "multi-coordinate" without being a multi-ary polymorphism in the clone-theoretic sense. Step 3 -> 4 requires showing that g's coordinate functions, restricted to X_L, give rise to multi-ary polymorphisms -- but they are unary polymorphisms (one input string, one output string).

The correct argument should be: g acts on X_L by permuting solution bits. If g is NOT in G_L, then g maps some z in X_L to g(z) not in X_L. But we also know g maps y in X_L to x in X_L. The proof wants to construct g' in G_L that agrees with g on relevant parts of X_L. The polymorphism argument is a detour meant to show that g's action on X_L is "simple enough" (essentially unary in coordinates) that such a g' exists.

But as shown in Attack Vector 3b, the construction of g' fails due to non-injectivity. So even if the polymorphism argument were correct, the conclusion does not follow from the stated construction.

**Verdict: WEAKENED.** The logical structure has a sound intuition (non-Taylor rigidity should force R_L = X_L rtimes G_L), but the execution has two compounding flaws: (i) the polymorphism argument applies to total maps, not partial ones, and (ii) the g' construction is not injective. The proof needs a fundamentally different construction of g' that avoids the piecewise definition.

---

## Attack Vector 5: Remark 6.2.1 Independence Claim

**Claim under attack:** "Path B (Part (i): non-fullness) does not require CP-1."

**Attack.** Remark 6.2.1 states that Path B uses "only the C*-algebra generator structure of M^L_Bool (membership of clone unitaries via Hecke isometries and phase generators), which is established at the C*-algebra level independent of CP-1."

Checking Node 1.3.5.9, Section 4.9: the independence analysis states that Path B uses (a) clone unitaries V_f in M^L_Bool (proved via generators, not CP-1), (b) pigeonhole on the unitary group (topological, no CP-1), and (c) instance diversity (combinatorial, no CP-1).

This appears correct. The non-fullness argument for Taylor languages relies on:
- M^L_Bool being a von Neumann algebra (from GNS construction -- standard, no CP-1 needed).
- Clone unitaries being elements of M^L_Bool (from the Hecke isometry and phase generator structure -- C*-algebraic, no CP-1 needed).
- The pigeonhole/compactness argument on the unitary group (topology of the unit ball in weak operator topology -- no CP-1 needed).

None of these steps require knowing that M^L_Bool has a crossed-product decomposition.

**Verdict: SURVIVED.** The independence claim is justified. Path B genuinely does not use the crossed-product structure of CP-1. It operates at the C*-generator level.

---

## Summary Verdicts

| Attack Vector | Target | Verdict | Severity |
|---|---|---|---|
| 1. Polymorphism rigidity | "Partial injection is a polymorphism" | **WEAKENED** | Medium -- imprecise language, salvageable with partial clone theory |
| 2. Essentially unary decomposition | "g decomposes into coordinate-wise operations" | **WEAKENED** | Medium -- arity confusion, correct fact applied incorrectly to partial maps |
| 3a. Decidability of X_L membership | "z in X_L is poly-time" | **SURVIVED** | N/A |
| 3b. Invertibility of g' | "g' is in PCirc^+_bi" | **BROKEN** | **Critical** -- concrete counterexample to injectivity of g' |
| 3c. g' as valid circuit | "g' is polynomial-time" | **SURVIVED** | N/A |
| 4. Logical structure | Contradiction argument | **WEAKENED** | High -- compounds flaws from vectors 1, 2, 3b |
| 5. Remark 6.2.1 independence | "Path B independent of CP-1" | **SURVIVED** | N/A |

---

## Critical Finding: The g' Construction Is Not Injective

The most severe finding is Attack Vector 3b. The piecewise definition:

    g'(z) = g(z) if z in X_L and g(z) in X_L
    g'(z) = z    otherwise

fails to be injective. Counterexample: X_L = {00, 01, 11}, g = (00 -> 01, 01 -> 11, 11 -> 10, 10 -> 00). Then g'(01) = g(01) = 11 and g'(11) = 11 (identity branch, since g(11) = 10 not in X_L). Two distinct inputs map to the same output.

This breaks the claim that g' in PCirc^+_bi (which requires bijectivity). Without a valid g', Proposition 6.2 does not establish R_L = X_L rtimes G_L for non-Taylor languages.

**Impact on the overall proof.** Proposition 6.2 feeds into Route D (Houdayer-Isono). If Prop 6.2 fails, Route D is blocked. However:
- Route C (Marrakchi) does NOT require Prop 6.2 -- it uses the groupoid form L(R_L) directly.
- Path B does NOT require Prop 6.2 -- it is independent of CP-1 entirely.
- The overall bridge theorem retains Route C as a viable path to fullness for non-Taylor languages.

**Recommended repair.** The g' construction needs a more sophisticated approach. One possibility: instead of defaulting to the identity on points where g fails, use the non-Taylor structure to decompose g|_{X_L} into coordinate-wise operations and then extend EACH coordinate operation independently to all of {0,1}^n. Since each coordinate operation is essentially unary (by non-Taylor), the extension is a permutation on each bit independently, which is automatically bijective. This avoids the piecewise collision problem. The repair requires citing results on extending partial polymorphisms (e.g., Larose-Zadori 2003 or Barto-Kozik-Niven 2009 for extension of partial operations in the Boolean case).

---

## Overall Assessment

**Proposition 6.2 status: BROKEN (repairable).**

The core insight -- that non-Taylor rigidity forces R_L to equal the transformation groupoid X_L rtimes G_L -- is likely correct, but the current proof has a concrete injectivity failure in the g' construction and imprecise polymorphism arguments. The proposition needs a rewrite with:

1. A correct construction of g' that maintains bijectivity (suggested: coordinate-wise extension using essentially unary decomposition).
2. Precise statements about how the Barto-Kozik characterization applies to coordinate functions of g restricted to X_L.
3. An explicit bridge between "partial solution-preserving map" and "polymorphism" (either via partial clone theory or via an extension lemma).

The damage is contained: Route C and Path B are unaffected, and Route D can be restored with a corrected Proposition 6.2.
