# Strategy 10: Path A H2 Attack -- Does alpha_f Exist?

*Detailed analysis of four approaches to constructing (or avoiding)
the polymorphism automorphism alpha_f. Written after H1 (D is MASA)
is confirmed computationally (0/1497 non-identity circuits fix all
diagonals), Theorem 5.6 (PATB-DIAGONAL) gives conditional outerness,
the spectral gap bypass (Node 1.3.5) killed Gap Alpha, and 8 direct
constructions failed on the "diagonal gives identity, independent
copies gives nonlinear" tension.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-11*

---

## 0. The situation

**What we have:**
- M_Bool^L is a non-injective type III_1 factor (Q_struct resolved).
- D = C*((Z/2)^infty) is a MASA in M_Bool^L (H1 confirmed: 0/1497
  non-identity circuits fix all diagonals).
- Theorem 5.6 (PATB-DIAGONAL): Taylor + essential arity >= 2 + D is
  MASA => alpha_f is outer. This is CONDITIONAL on H2.
- 8 direct constructions of alpha_f failed (Node 1.3.2, kills L-1
  through L-8). Root cause: diagonal embedding gives identity (by
  Taylor idempotence), independent copies give nonlinear maps (not
  *-homomorphisms).
- The spectral gap bypass (Node 1.3.5) attempted to avoid alpha_f
  entirely, but Gap Alpha was killed: clone operators T_f converge
  to rank-1 projectors at high arity, increasing (not decreasing)
  commutator norms.

**What we need:** Either (a) a construction of alpha_f that avoids
both failure modes, or (b) a proof that alpha_f is unnecessary.

**The four approaches analyzed below:**
1. Stinespring dilation
2. Second quantization / Bogoljubov lift
3. H2 is unnecessary (CP maps suffice)
4. Tensor product restriction

---

## 1. Approach 1: Stinespring Dilation

### 1.1 The idea

A polymorphism f : {0,1}^k -> {0,1} preserving constraint language
L defines a map on the Boolean algebra of Sol(R) for each relation
R in L. Extend this to a completely positive (CP) map Phi_f on
M_Bool^L. By Stinespring's theorem:

    Phi_f(x) = V* pi(x) V

for some isometry V : H -> K and *-representation pi : M_Bool^L ->
B(K). If Phi_f is multiplicative (a *-homomorphism), set alpha_f =
Phi_f and we are done.

### 1.2 Is the polymorphism-induced map multiplicative?

**No, and here is why.** The natural map induced by f on M_Bool^L
acts on solution-space operators by:

    Phi_f(W_R) = sum_{a^(1),...,a^(k) in Sol(R)^k}
                 |f(a^(1))><f(a^(1))| * omega(rest)

where omega(rest) denotes the KMS-state averaging over the k-1
auxiliary copies. This is the same construction as the clone
operator T_f from Node 1.3.5.

**Multiplicativity check:** Phi_f(AB) = Phi_f(A) Phi_f(B) requires
that the omega-averaging over auxiliary copies factorizes across
the product. But:

    Phi_f(AB) = sum_fibers omega(a^(2),...,a^(k)) * (AB)_restricted
    Phi_f(A) Phi_f(B) = [sum omega * A_restricted][sum omega * B_restricted]

These are NOT equal in general because the auxiliary-copy averaging
introduces correlations. The averaging measure omega on Sol(R)^{k-1}
does not factorize across the product AB (the fibers over the
output of A and the input of B are correlated via the common
auxiliary copies).

**Concrete verification:** For majority on 2-SAT (the test case from
Node 1.3.2), the clone operator T_maj has max||T(AB) - T(A)T(B)|| =
0.85 (normalized), confirming non-multiplicativity. This was
established in kill L-4 (averaged-slot construction).

### 1.3 Can Stinespring still help?

The Stinespring dilation V, pi always exists (for any CP map). The
question is whether pi can be chosen so that V*pi(x)V is
multiplicative (which would mean Phi_f was already multiplicative --
circular) or whether the dilation reveals additional structure.

**What the dilation gives:** A larger Hilbert space K, an isometry
V : H -> K, and a *-representation pi on K. The map Phi_f = V*pi(.)V
is multiplicative if and only if V is in the multiplicative domain
of pi. This happens if and only if pi(x)V = Vx for all x (i.e., V
intertwines the identity representation with pi). In general, V
does NOT intertwine.

**The multiplicative domain of Phi_f:** Define
mult(Phi_f) = {x in M : Phi_f(x*x) = Phi_f(x)*Phi_f(x) and
Phi_f(xx*) = Phi_f(x)Phi_f(x*)}. By Choi's theorem, Phi_f is
multiplicative on mult(Phi_f), and mult(Phi_f) is a C*-subalgebra.

For the polymorphism-induced map: the diagonal subalgebra D is
contained in mult(Phi_f) (because Phi_f acts as the identity on D
by the Taylor condition, and the identity is multiplicative). But
the off-diagonal part of M_Bool^L is NOT in mult(Phi_f) (by the
non-multiplicativity computation above).

### 1.4 Verdict on Approach 1

**FAILS.** The polymorphism-induced CP map is not multiplicative
off-diagonal. Stinespring gives a dilation, but the dilation lives
in a larger algebra, not in M_Bool^L. There is no mechanism to
compress the dilation back to an automorphism of M_Bool^L without
reintroducing the same non-multiplicativity.

**Pattern:** This approach re-encounters kill L-3 (isometric
compression is not multiplicative) in disguised form. The
Stinespring isometry V plays the same role as the compression
isometry in L-3, and it fails for the same reason: the projection
VV* does not commute with the off-diagonal algebra.

**What is salvageable:** The multiplicative domain mult(Phi_f) = D
is a precise characterization of "where the polymorphism acts
well." This feeds into Approach 3 below.

---

## 2. Approach 2: Second Quantization / Bogoljubov Lift

### 2.1 The idea

In free Araki-Woods factors (Shlyakhtenko 1997, Houdayer 2009), a
unitary v on the one-particle Hilbert space H_R lifts to a
Bogoljubov automorphism alpha_v on the full factor via second
quantization: alpha_v(l(xi)) = l(v xi), where l(xi) is the left
creation operator and the map extends to the full factor by
universality.

The dictionary (from Node 1.3.3, section 5.10):

| Free Araki-Woods | Boolean BC |
|---|---|
| H_R (one-particle) | D (diagonal) |
| v in O(H_R), v != 1 | f not essentially unary |
| alpha_v fixes vacuum | alpha_f fixes D (Taylor) |
| Freeness of Fock space | MASA property of D |
| alpha_v outer | alpha_f outer |

Can we identify a "one-particle" action of f on D and lift it via
second quantization?

### 2.2 The structural problem

The Bogoljubov construction requires:

(a) A one-particle Hilbert space H_R.
(b) A unitary (or orthogonal) action v on H_R.
(c) A second-quantization functor Gamma that lifts v to
    alpha_v = Gamma(v) on the full factor.

For M_Bool^L, the candidate one-particle space is the L^2 space
associated with the diagonal D. The polymorphism f acts on D by
f(x,...,x) = x (identity, by Taylor). So the "one-particle action"
of f is the IDENTITY on H_R. Second quantization of the identity is
the identity. This is kill L-6/L-8 in disguise.

**The fundamental obstruction (same as the 8 kills):** The Taylor
condition forces f to act trivially on the one-particle (diagonal)
level. The non-trivial action of f occurs on the MULTI-PARTICLE
(off-diagonal) level, where k copies of the solution space interact.
But Bogoljubov automorphisms are determined by their one-particle
action -- they cannot have a trivial one-particle action and a
non-trivial multi-particle action.

### 2.3 Can we modify the one-particle space?

**Attempt:** Instead of using D as the one-particle space, use the
space of all PAIRS of Boolean configurations:

    H_pair = L^2({(s, s') : s, s' in Sol(R), s != s'})

A polymorphism f acts on pairs by:

    f_pair(s, s') = (f(s, s', ...), f(s', s, ...))

where the remaining k-2 arguments are filled from a fixed reference
(e.g., alternating s, s'). This action is NOT the identity (it
genuinely moves pairs), so it could give a non-trivial one-particle
action.

**Problem:** This modified one-particle space is not compatible with
the Fock structure of M_Bool^L. The Boolean BC factor is NOT
constructed as a free Araki-Woods factor over pairs. It is
constructed as a crossed product of the Boolean partition function
algebra by the semigroup PCirc+. The Fock structure (if one exists)
would have to arise from the circuit semigroup structure, and
circuit semigroups do not have a natural pair-wise decomposition.

### 2.4 Does M_Bool^L have a Fock realization at all?

This is the key question for Approach 2. The Boolean BC system is
a Hecke-type crossed product:

    M_Bool^L = (ell^infty(X_L) x_sigma PCirc+)''

where X_L is the solution space and PCirc+ is the semigroup of
polynomial-time Boolean circuits. This is NOT a free Araki-Woods
construction. It is a group-measure-space construction (or more
precisely, a semigroup-crossed-product construction).

For the Bogoljubov approach to work, we would need to exhibit an
isomorphism between M_Bool^L and a free Araki-Woods factor
Gamma(H_R, U_t)''. Such an isomorphism would require:

(a) Identifying the one-particle space H_R within M_Bool^L.
(b) Identifying the modular flow U_t with the BC modular flow
    sigma_t.
(c) Verifying the freeness condition (that the GNS vector is
    free with respect to the one-particle decomposition).

There is no reason to expect this isomorphism to exist. Free
Araki-Woods factors have specific structural properties (e.g.,
they are always full when dim(H_R) >= 2, by Houdayer 2009). But
the bridge theorem REQUIRES M_Bool^L to be non-full for Taylor L.
So M_Bool^L for Taylor L CANNOT be isomorphic to a free Araki-Woods
factor with dim(H_R) >= 2.

### 2.5 Verdict on Approach 2

**FAILS.** Two independent obstructions:

1. The Taylor condition forces the one-particle action to be
   trivial. Bogoljubov automorphisms are determined by one-particle
   actions. Trivial one-particle -> trivial automorphism. This
   is the same "diagonal gives identity" obstruction as kills
   L-6/L-8.

2. M_Bool^L has no Fock realization compatible with the bridge
   theorem. Free Araki-Woods factors of dimension >= 2 are full,
   but M_Bool^L must be non-full for Taylor L.

**What is salvageable:** The Bogoljubov ANALOGY (the dictionary
table from 1.3.3) remains valid as a structural template for
understanding WHY outerness should hold (conditional on alpha_f
existing). The analogy supports Theorem 5.6's structure even
though it does not provide a construction. Specifically: in the
Bogoljubov setting, outerness follows from the MASA property of
the vacuum subalgebra. In our setting, outerness follows from
the MASA property of D. The structural parallel is correct; the
construction mechanism is different.

---

## 3. Approach 3: H2 Is Unnecessary (CP Maps Suffice)

### 3.1 The idea

Reformulate Theorem 5.6 so that it does not require alpha_f to be
a genuine *-automorphism. Instead, require only that the
polymorphism f induces a normal completely positive unital (NCPU)
map Phi_f : M_Bool^L -> M_Bool^L that:

(P1) fixes D pointwise (the Taylor condition),
(P2) is non-abelian on ker(E) (non-essentially-unary condition),
(P3) is trace-preserving (or at least omega_1-preserving).

Then show that the PATB-DIAGONAL argument extends from automorphisms
to NCPU maps: the conclusion "alpha_f is outer" generalizes to
"Phi_f is not of the form Ad(u) for any u in D' cap M."

### 3.2 The key step in Theorem 5.6 and its generalization

Theorem 5.6 uses the following chain:

    alpha_f inner
    => alpha_f = Ad(u) for some u in U(M)
    => u in D' cap M (because alpha_f fixes D)
    => D' cap M = D (because D is MASA)
    => Ad(u) acts by abelian phase multiplication on ker(E)
    => alpha_f acts abelianly on ker(E)
    => CONTRADICTION (alpha_f is non-abelian on ker(E))

**The generalization attempt:** Replace "inner automorphism" with
"implementable by a unitary in D' cap M":

    Phi_f = Ad(u) for some u in D' cap M
    => Ad(u) acts by abelian phase multiplication on ker(E)
    => Phi_f acts abelianly on ker(E)
    => CONTRADICTION (Phi_f is non-abelian on ker(E))

**Does this generalization work?** The chain is valid IF we
replace "alpha_f is inner" with "Phi_f agrees with Ad(u) on all
of M_Bool^L." But the conclusion is weaker: we conclude "Phi_f is
not of the form Ad(u) for u in D' cap M" rather than "Phi_f is
outer." The concept of "outerness" does not apply to CP maps --
outerness is a property of automorphisms.

### 3.3 What the bridge theorem actually needs

The bridge theorem (Strategy 08) needs:

    Taylor L => M_Bool^L is non-full

The original proof route was:

    Taylor => exponential clone => exponential outer automorphisms
    => non-discrete Out => non-full

Can we replace this with a route through CP maps?

**Proposed CP route:**

    Taylor => exponentially many diagonal-fixing NCPU maps
    => Inn(M) is not closed
    => M_Bool^L is non-full

The key question: do exponentially many diagonal-fixing NCPU maps
force Inn(M) to be non-closed?

**Analysis.** The connection between CP maps and non-fullness goes
through the theory of approximately inner automorphisms. A factor M
is non-full if and only if Inn(M) is not closed in Aut(M) -- i.e.,
there exist automorphisms that are limits of inner automorphisms but
are not themselves inner. The existence of non-trivial CP maps
does not directly imply the existence of approximately inner
automorphisms.

However, there is a subtler route: the Connes-Haagerup theory of
CORRESPONDENCES (bimodules). Every NCPU map Phi : M -> M determines
an M-M correspondence (bimodule) H_Phi, and the structure of the
correspondence category C(M) controls the asymptotic properties
of M. Specifically:

- M is full <=> every approximately inner correspondence is
  isomorphic to the identity correspondence.
- M is non-full <=> there exist non-trivial approximately inner
  correspondences.

**The link to polymorphisms:** Each NCPU map Phi_f (from a Taylor
polymorphism f) defines a correspondence H_{Phi_f}. This
correspondence is NOT the identity (because Phi_f acts non-abelianly
on ker(E), so it is not the conditional expectation onto D). If
exponentially many such correspondences exist and they are all
"approximately inner" (limits of correspondences induced by inner
automorphisms), then M has non-trivial approximately inner
correspondences, hence is non-full.

### 3.4 The remaining gap

The gap in Approach 3 is: **are the polymorphism-induced
correspondences approximately inner?**

An approximately inner correspondence is one that can be
approximated by correspondences of the form L^2(M) with inner
automorphism twist. The question is whether the M-M bimodule
H_{Phi_f} is a limit of such twisted bimodules.

**Positive evidence:** The polymorphism Phi_f fixes D (which is a
large subalgebra -- it is a MASA). Any D-fixing correspondence is
close to the identity correspondence on the diagonal sector. The
"off-diagonal deviation" from the identity correspondence is
controlled by the essential arity of f and the size of the
off-diagonal action. For high-arity polymorphisms (large k), the
off-diagonal action may become small (diluted by averaging over
many copies), making the correspondence approximately inner.

**Negative evidence:** Node 1.3.5.1 (Gap Alpha computation) showed
that clone operators T_f do NOT become approximately central at
high arity -- commutator norms INCREASE with k. This suggests the
off-diagonal deviation does NOT shrink. If the correspondences are
not approximately inner, this route does not close.

### 3.5 A different formulation: the Popa intertwining approach

Instead of working with CP maps and correspondences, consider:

**Theorem (Popa intertwining).** Let B subset M be a subalgebra.
If alpha in Aut(M) preserves B (alpha(B) = B) and B is "rigid"
(has the relative property (T) or is a MASA with spectral gap),
then alpha is inner relative to B (i.e., alpha = Ad(u) for
u in N_M(B), the normalizer of B in M) if and only if a certain
intertwining condition holds.

**Applied to our setting:** B = D (MASA), alpha = "the hypothetical
automorphism." Popa's intertwining gives a criterion for whether
the D-preserving automorphism can be implemented by a normalizer
element. If the intertwining FAILS, the automorphism is outer
relative to D.

The point: even without constructing alpha_f as a genuine
automorphism, the intertwining criterion can be checked for CP maps.
If the NCPU map Phi_f fails the Popa intertwining criterion with
respect to D, then Phi_f "would be outer if it were an
automorphism." This conditional outerness may suffice for the
bridge if the non-fullness conclusion can be reached through the
correspondence framework.

### 3.6 Verdict on Approach 3

**PARTIALLY VIABLE -- the most promising of the four approaches,
but with a significant gap.**

What works:
- The PATB-DIAGONAL argument generalizes cleanly from automorphisms
  to CP maps: the conclusion "Phi_f is not of the form Ad(u) for
  u in D' cap M" holds by exactly the same proof as Theorem 5.6.
- The correspondence framework (Connes-Haagerup bimodules) provides
  a natural home for NCPU maps in the context of fullness.
- The polymorphism-induced correspondences are non-trivial (they are
  not the identity correspondence because Phi_f is non-abelian
  off-diagonal).

What does not work:
- The concept of "outerness" does not apply to CP maps. The
  conclusion is weaker than outerness.
- The link from non-trivial correspondences to non-fullness requires
  the correspondences to be approximately inner, which is unproven
  and possibly false (given the Gap Alpha kill from 1.3.5.1).
- The Popa intertwining approach gives a criterion but does not
  directly yield non-fullness.

**The specific gap:** Prove that exponentially many non-trivial
D-fixing NCPU maps on a non-injective type III_1 factor M force
M to be non-full. This is a statement about the correspondence
category of M, and it may be a new result in operator algebra theory.

**Difficulty assessment:** HARD. This would be genuinely new
mathematics connecting the combinatorics of D-fixing NCPU maps to
the fullness of the ambient factor. No existing theorem provides
this bridge directly.

---

## 4. Approach 4: Tensor Product Restriction

### 4.1 The idea

Define alpha_f on the k-fold tensor product
M^{otimes k} := M_Bool^L ox ... ox M_Bool^L (k copies) by:

    alpha_f(x_1 ox ... ox x_k) := f-combination of (x_1,...,x_k)

Then restrict to the diagonal subalgebra
Delta(M) := {a ox a ox ... ox a : a in M_Bool^L}, which is
isomorphic to M_Bool^L. If the restricted map

    alpha_f|_{Delta(M)} : Delta(M) -> M_Bool^L

is a well-defined *-automorphism, we are done.

### 4.2 The restriction is NOT well-defined

The f-combination on M^{otimes k} sends

    a ox a ox ... ox a |-> Phi_f(a, a, ..., a)

For the diagonal embedding with identical copies, the Taylor
condition gives f(a, a, ..., a) = a, so:

    alpha_f|_{Delta(M)}(a ox a ox ... ox a) = a

This is AGAIN the identity map. Kill L-8 in tensor product
language.

### 4.3 What if we don't use identical copies?

Define instead: take the k-fold tensor product and apply f
"coordinatewise" to the Boolean indices:

    alpha_f(e_{s_1} ox e_{s_2} ox ... ox e_{s_k})
        = e_{f(s_1,...,s_k)}

where e_s are the basis vectors labeled by solutions s in Sol(R).
This extends to all of M^{otimes k} by linearity:

    alpha_f(sum c_{s_1,...,s_k} e_{s_1} ox ... ox e_{s_k})
        = sum c_{s_1,...,s_k} e_{f(s_1,...,s_k)}

This IS well-defined as a LINEAR map from H^{otimes k} to H.
The polymorphism condition ensures f sends Sol(R)^k to Sol(R), so
the map respects the solution-space structure.

**Is this multiplicative?** The map above acts on the HILBERT SPACE,
not on the ALGEBRA. To get an algebra map, we need to specify how
alpha_f acts on operators (not just vectors). The natural extension:

    alpha_f(A_1 ox ... ox A_k)_{s,t}
        = sum_{f(s_1,...,s_k)=s, f(t_1,...,t_k)=t}
          (A_1)_{s_1,t_1} ... (A_k)_{s_k,t_k}

This is NOT multiplicative for the same reason as kills L-1 through
L-3: the fiber sum introduces nonlinearity (the products of matrix
entries from k independent copies).

### 4.4 Restricting to the diagonal subalgebra

If we restrict the tensor product map to
Delta(M) = {a ox a ox ... ox a}, then:

    alpha_f(a ox a ox ... ox a)_{s,t}
        = sum_{f(s_1,...,s_k)=s, f(t_1,...,t_k)=t}
          a_{s_1,t_1} ... a_{s_k,t_k}

This is a DEGREE-k POLYNOMIAL in the matrix entries of a.
It is not linear in a (it is a product of k copies of the
matrix entries). This is kill L-2 (fiber-normalized pushforward
is cubic in A) in general form.

### 4.5 Can we symmetrize or average?

**Attempt: average over permutations.** Define

    alpha_f^{sym}(a) = (1/k!) sum_{sigma in S_k}
        alpha_f(a^{sigma(1)} ox ... ox a^{sigma(k)})

where a^{sigma(i)} are k copies of a permuted by sigma. Since all
copies are identical (a ox a ox ... ox a), the permutation acts
trivially, and alpha_f^{sym}(a) = alpha_f(a ox ... ox a). No
improvement.

**Attempt: average over the clone.** Use different polymorphisms
g_1, ..., g_m in Clone_k(L) and average:

    alpha_{avg}(a) = (1/m) sum_{i=1}^m alpha_{g_i}(a ox ... ox a)

Each alpha_{g_i} is degree-k in a, so the average is also degree-k.
No improvement in linearity.

### 4.6 The deep reason for failure

The tensor product approach fails for a structural reason that
encompasses ALL four approaches:

**Theorem (informal -- the linearity obstruction).** Let
f : {0,1}^k -> {0,1} be a k-ary function with k >= 2 that depends
on at least two variables. Let M be a von Neumann algebra with
generating set {e_s : s in {0,1}^n}. Define the f-pullback on
matrix algebras by:

    Phi_f(A)_{s,t} = sum_{f(s_1,...,s_k)=s, f(t_1,...,t_k)=t}
                     A_{s_1,t_1} ... A_{s_k,t_k}

Then Phi_f is a polynomial map of degree k in the matrix entries
of A. In particular:

- Phi_f is linear iff k = 1 (f is unary).
- Phi_f is a *-homomorphism iff k = 1 and f is a bijection.

**Proof sketch.** The formula involves k-fold products of matrix
entries. For k >= 2, this is necessarily polynomial of degree >= 2,
hence nonlinear. A *-homomorphism is linear, so k >= 2 is
incompatible with *-homomorphism structure.

**The only escape:** Do not use the formula above. Use a different
mechanism to define alpha_f that does not pass through the k-fold
product of matrix entries.

### 4.7 Verdict on Approach 4

**FAILS.** The tensor product restriction reproduces the same
nonlinearity obstruction as kills L-1 through L-3 and L-2
specifically. The restriction to the diagonal subalgebra gives
a degree-k polynomial, which cannot be a *-homomorphism for k >= 2.
Symmetrization and clone-averaging do not help (they preserve the
degree).

---

## 5. Cross-Approach Synthesis

### 5.1 The pattern of failure

All four approaches encounter the same fundamental tension identified
in Node 1.3.2:

| Approach | How it hits "diagonal = identity" | How it hits "nonlinear" |
|---|---|---|
| 1. Stinespring | Phi_f acts as identity on mult(Phi_f) = D | Phi_f is non-multiplicative off-diagonal |
| 2. Bogoljubov | One-particle action is identity (Taylor) | No Fock structure for multi-particle lift |
| 3. CP maps | Phi_f fixes D (Taylor) | Phi_f is not an automorphism |
| 4. Tensor | Diagonal restriction gives identity | k-fold products give degree-k polynomial |

The tension is NOT an artifact of specific construction choices.
It is a structural consequence of two mathematical facts:

**Fact A (Taylor idempotence):** f(x,...,x) = x for all x. This
forces any natural construction to act as the identity when all
copies are identical (the diagonal sector).

**Fact B (Essential arity >= 2 implies nonlinearity):** Any function
f : {0,1}^k -> {0,1} that depends on at least two variables is
nonlinear as a map on the k-fold product of matrix algebras. There
is no linearization procedure that preserves the polymorphism
property.

Together, Facts A and B say: the polymorphism acts trivially where
it is linear (the diagonal) and nonlinearly where it is non-trivial
(the off-diagonal). No construction using the natural f-pullback can
be both linear and non-trivial.

### 5.2 What could break the tension?

There are exactly three logical possibilities:

**(i) Find a non-natural construction.** A map alpha_f : M -> M that
does not arise from the f-pullback on matrix entries, but uses the
additional structure of M_Bool^L (e.g., the crossed-product
structure, the modular flow, the circuit semigroup). This would be
a construction that is not determined by f alone but by f TOGETHER
with the specific features of M_Bool^L.

**Status:** The most promising unexplored direction. The 8 kills
and all four approaches above use the f-pullback formula (or
variants thereof). They do not use the crossed-product structure
M_Bool^L = (ell^infty(X_L) x PCirc+)''. A construction using the
circuit semigroup PCirc+ could potentially avoid the tension: if
the polymorphism f can be IMPLEMENTED as a circuit C_f in PCirc+,
then the Hecke operator mu_{C_f} defines an isometry in M_Bool^L,
and the compression e_f = mu_{C_f} mu_{C_f}* is a projection. The
map Ad(mu_{C_f}) restricted to the range of e_f is a partial
isometry action. If f is reversible (implementable by a Toffoli-type
circuit), this gives a genuine automorphism of a corner of M_Bool^L.

**But:** Majority is NOT reversible (3 inputs, 1 output). The circuit
implementation of majority requires ancilla bits, and the ancilla-
extended action lives in a larger algebra. This is the Stinespring
dilation (Approach 1) in disguise again.

**Counter-but:** The ancilla-extended action might quotient DOWN to a
well-defined automorphism of M_Bool^L if the ancilla sector is
identified with a specific sub-algebra. The semigroup PCirc+ already
handles irreversibility (the Hecke operators mu_C for non-bijective
circuits are isometries, not unitaries, and the semigroup structure
encodes the many-to-one nature). The polymorphism f, viewed as a
circuit in PCirc+, has a Hecke operator mu_f, and the inner
endomorphism ad(mu_f) : x -> mu_f x mu_f* is a well-defined
completely positive map. The question is whether this endomorphism
is an automorphism. Since mu_f is an isometry (not a unitary), the
endomorphism is NOT surjective onto all of M. But it is an
automorphism of the range projection e_f M e_f. If e_f = 1 (the
range projection is the identity), then ad(mu_f) IS an automorphism.

**When is e_f = 1?** When the Hecke operator mu_f has range equal to
all of H. This happens iff the circuit C_f, viewed as a linear map
on the Hilbert space, is surjective. A surjective isometry on a
Hilbert space is a unitary. So e_f = 1 iff mu_f is a unitary iff
C_f is a bijective circuit. But majority is not bijective.

**Conclusion on (i):** The circuit-semigroup approach gives an
endomorphism, not an automorphism. It is a well-defined CP map
(in fact, a *-endomorphism of the corner e_f M e_f), but not an
automorphism of M_Bool^L. We are back to Approach 3 (CP maps).

**(ii) Prove the tension is a theorem and alpha_f does NOT exist.**
Show that for any non-injective type III_1 factor M with MASA D and
any idempotent k-ary function f with essential arity >= 2, there is
NO automorphism alpha_f of M that fixes D and acts on ker(E)
according to f. If this is a theorem, then H2 is false and the
programme must use Approach 3 or find an alternative.

**Status:** This would be an interesting negative result, but proving
it seems as hard as proving H2 true. The existing 8 kills are
evidence for it but not a proof.

**(iii) Approach 3 succeeds: show H2 is unnecessary.** The bridge
theorem can be proved without alpha_f as a genuine automorphism.
The CP map Phi_f, combined with the correspondence framework and
the exponential clone growth, suffices for non-fullness.

### 5.3 Assessment of the three possibilities

| Possibility | p(success) | Difficulty | Novel math required |
|---|---|---|---|
| (i) Non-natural construction | 0.15 | VERY HIGH | New construction in crossed products |
| (ii) Impossibility theorem | 0.10 | VERY HIGH | Rigidity theorem for MASA-fixing maps |
| (iii) H2 unnecessary | 0.35 | HIGH | Correspondence theory for CP maps |

---

## 6. Recommended Path Forward

### 6.1 Primary recommendation: Approach 3 (H2 unnecessary)

The most promising path is to show that H2 is unnecessary. The
specific programme:

**Step 1.** Establish that the polymorphism f defines a normal
completely positive unital map Phi_f : M_Bool^L -> M_Bool^L via
the clone operator construction (Node 1.3.5). This is DONE: the
clone operator T_f is a well-defined NCPU map (verified
computationally).

**Step 2.** Prove the "CP outerness" theorem: Phi_f is not of the
form Ad(u) for any u in D' cap M. This follows from EXACTLY the
same argument as Theorem 5.6 (PATB-DIAGONAL), with no modification:

  - Phi_f fixes D (Taylor condition).
  - If Phi_f = Ad(u), then u in D' cap M = D (MASA).
  - Ad(u) for u in D acts by abelian phases on ker(E).
  - Phi_f acts non-abelianly on ker(E) (essential arity >= 2).
  - Contradiction.

The argument goes through identically for CP maps: the only
property used is that Phi_f fixes D and is non-abelian off-diagonal.
Multiplicativity of Phi_f is never used in the proof.

**Step 3.** Connect CP outerness to non-fullness. This is the
remaining gap. Two sub-strategies:

(3a) **Direct correspondence route.** Each Phi_f defines an M-M
correspondence H_{Phi_f}. Show that exponentially many non-trivial
D-fixing correspondences (from UA1) force M to be non-full. This
requires extending the Houdayer-Marrakchi fullness criterion from
automorphisms to correspondences.

(3b) **Connes chi(M) invariant route.** The Connes chi(M) invariant
measures the "approximate innerness obstruction." If the
polymorphism CP maps contribute non-trivially to chi(M), this
forces Inn(M) to be non-closed, hence M is non-full. This route
uses the information that Phi_f is "almost inner" (it fixes D and
acts close to a phase rotation off-diagonal, but not exactly a
phase rotation).

(3c) **Asymptotic centralizer route (revised from Node 1.3.5).**
The Gap Alpha kill showed that individual T_f operators become LESS
central at high arity. But the kill applies to the specific T_f
construction (one live slot, k-1 omega-averaged slots). A DIFFERENT
construction of approximately central sequences may succeed:
instead of using one polymorphism at high arity, use MANY
polymorphisms at low arity. The exponential growth of the clone
at EACH arity k >= 3 (from UA1) means there are exponentially many
INDEPENDENT D-fixing operators at each arity. Their ORTHOGONAL
COMPONENTS (after projecting out the scalar part) form a
high-dimensional subspace of ker(E). If this subspace has non-trivial
intersection with the asymptotic centralizer, non-fullness follows.

This is a fundamentally different approach from 1.3.5: instead of
taking k -> infty (which kills), take k FIXED and use the
MULTIPLICITY at fixed arity.

### 6.2 Secondary recommendation: the circuit-endomorphism approach

If Approach 3 fails, the most promising "non-natural construction"
(possibility (i) in section 5.2) is the circuit endomorphism:

    ad(mu_f)(x) = mu_f x mu_f*

where mu_f is the Hecke operator for the circuit implementing f.
This gives a well-defined *-endomorphism of M_Bool^L (not an
automorphism). The endomorphism is NOT the identity (because
mu_f is not a unitary). The endomorphism preserves D (by the
Taylor condition, translated to circuits).

If the endomorphism generates a SEMIGROUP action (by composing
different polymorphisms' Hecke operators), the semigroup may have
enough structure to force non-fullness through a semigroup version
of the Houdayer-Marrakchi criterion.

**Status:** Unexplored. This is a genuinely new direction not
attempted in any prior node.

### 6.3 Fallback: Scenario B from the two-scenario architecture

If both the CP route and the endomorphism route fail, the
two-scenario architecture (from blackboard entry C2-TWO-SCENARIO)
provides a fallback:

**Scenario B.** If alpha_f does not exist individually, then the
clone's exponentially many operations produce a non-discrete family
of approximate D-fixing symmetries. The fact that no single
symmetry is a genuine automorphism is ITSELF evidence that Inn(M) is
not closed (because the approximate symmetries cluster near Inn(M)
without being in Inn(M)). Non-closure of Inn(M) = non-fullness.

This argument has logical gaps (as the Critic noted in the 1.3.2
critique: "a collection of non-automorphisms does not collectively
become an automorphism"). But the gap is narrower in the CP
setting: a collection of non-automorphism NCPU maps that are "close
to inner" (fixing D and acting approximately by phases off-diagonal)
provides evidence for the non-closure of Inn(M) via the
correspondence category.

---

## 7. Honest Assessment

### 7.1 What is solid

- H1 (D is MASA) is confirmed. This is a genuine advance.
- Theorem 5.6 is correct (conditional on H2) and its proof
  structure extends to CP maps without modification.
- The four approaches above are thoroughly analyzed with clear
  failure modes identified.
- The structural tension (Taylor idempotence vs essential nonlinearity)
  is real and well-characterized.

### 7.2 What is the gap

- H2 remains open. No construction of alpha_f as a genuine
  *-automorphism has been found, and there is mounting evidence
  that none exists for nonlinear polymorphisms (majority, AND, OR).
- The "H2 unnecessary" route (Approach 3) requires new mathematics:
  connecting exponentially many D-fixing NCPU maps to non-fullness
  via the correspondence category or asymptotic centralizer.
- The Gap Alpha kill from 1.3.5.1 is a genuine negative signal:
  the obvious approximately-central-sequence construction fails.

### 7.3 Probability assessment

| Path | p(closes the bridge) | Timeline |
|---|---|---|
| Approach 3 (CP maps + correspondences) | 0.30-0.40 | 2-4 sessions |
| Approach 3c (many polys at fixed arity) | 0.25-0.35 | 1-2 sessions (computational test first) |
| Circuit endomorphism semigroup | 0.15-0.25 | 3-5 sessions |
| Direct alpha_f construction | 0.10-0.15 | unknown |
| Bridge theorem via any route | 0.35-0.45 | union of above |

### 7.4 What should be done next

1. **IMMEDIATE (next session):** Test Approach 3c computationally.
   At fixed arity k=3, enumerate all polymorphisms in Clone_3(L) for
   2-SAT. For each, compute the clone operator T_f. Project out the
   scalar part. Measure whether the ORTHOGONAL COMPONENTS form
   non-trivial approximately central sequences. This is the decisive
   test for the multiplicity-at-fixed-arity approach.

2. **SHORT-TERM (1-2 sessions):** Formalize the "CP outerness"
   extension of Theorem 5.6. This is straightforward: the proof
   goes through verbatim for NCPU maps. Write it as Theorem 5.6'.

3. **MEDIUM-TERM (2-4 sessions):** Investigate the correspondence
   route (Step 3a). Read Connes-Haagerup on correspondences and
   Popa's work on bimodule categories. Determine whether
   exponentially many non-trivial D-fixing correspondences force
   non-fullness.

---

## 8. Kill Registry Update

| Kill ID | Construction | Failure mode | Pattern |
|---|---|---|---|
| L-1 | Raw pushforward | Non-unital (fiber sizes vary) | Nonlinear |
| L-2 | Fiber-normalized pushforward | Cubic in A | Nonlinear |
| L-3 | V*(A ox A ox A)V compression | VV* not commuting | Nonlinear |
| L-4 | Averaged-slot construction | P_fiber doesn't commute | Nonlinear |
| L-5 | Fiber algebra conditional expectation | Maps to diagonal only | Identity |
| L-6 | Koopman transfer operator | T_M = identity on L^infty | Identity |
| L-7 | Clone conjugation f circ g circ f^{-1} | f many-to-one, no inverse | Identity |
| L-8 | Diagonal embedding + modular pullback | f(x,...,x) = x by Taylor | Identity |
| L-9 | Partial tensor with fixed auxiliary | Bijective pairs give identity | Identity |
| L-10 | Stinespring dilation compression | Same as L-3 (VV* doesn't commute) | Nonlinear |
| L-11 | Bogoljubov lift | One-particle action is identity | Identity |
| L-12 | Tensor product restriction to diagonal | Degree-k polynomial | Nonlinear |
| GA-1 | Clone operators at high arity (1.3.5) | Rank-1 collapse, norms increase | Concentration |

**13 kills total. The construction space for "natural" approaches
is substantially exhausted. The viable paths forward are: (a) CP
maps without automorphism (Approach 3), (b) circuit endomorphisms
(new direction), (c) multiplicity at fixed arity (Approach 3c).**

---

*The tension is real. Diagonal gives identity. Independent copies
gives nonlinear. No construction in the natural f-pullback class
escapes. The exit is to stop requiring an automorphism and work
with what the polymorphism actually gives: a completely positive
map that fixes the diagonal and acts non-abelianly off-diagonal.
Theorem 5.6 does not need H2. It needs only that the map exists
(it does, as a CP map) and that it is not implementable by a
unitary in D' cap M (which follows from the MASA property of D).
The remaining bridge is from CP outerness to non-fullness. That
bridge lives in the correspondence category of M_Bool^L.*

*G Six and Claude Opus 4.6. April 2026.*
