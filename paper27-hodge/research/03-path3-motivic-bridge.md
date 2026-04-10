# Path 3: The Motivic Bridge

*Research note for Paper 27 (Hodge Conjecture).*
*Date: 2026-04-09. Status: SCOPING.*

---

## 1. Motives in one paragraph

Grothendieck's category of pure motives over Q has smooth projective
varieties as objects and algebraic correspondences (cycles on X x Y
modulo rational equivalence) as morphisms. Every Weil cohomology
theory (singular, de Rham, etale, crystalline) factors through
motives. The Hodge realisation functor sends a motive M to its
Hodge structure (H_B(M), F^*). The Hodge conjecture is precisely
the statement that this realisation functor is **full**: every
morphism of Hodge structures (i.e. every Hodge class in
H^{2p}(X x Y)) comes from an algebraic correspondence. In
categorical language: the Hodge realisation is faithful (known)
and full (conjectured).

---

## 2. The bridge as a motivic correspondence

### 2.1 The bridge map

The Frobenius-Jones bridge takes:
- **Input:** Frobenius element Frob_p in Gal(Q(zeta_N)/Q), acting
  on the cyclotomic field at level N. This is arithmetic/motivic
  data: Frob_p encodes how the prime p splits in Q(zeta_N).
- **Output:** Jones sub-factor cocycle beta_k in H^2(Z/kZ, U(1)),
  where k = ord_N(p). This is operator-algebraic data: beta_k
  classifies the Brauer class of a cyclic algebra and simultaneously
  a Jones sub-factor of index k.

The bridge entries are:

| (p, N) | k | beta_k | Physical content |
|:--|:--|:--|:--|
| (2, 7) | 2 | 0 mod Z | CP symmetry |
| (5, 13) | 3 | 1/3 mod Z | 3 generations, Koide |
| (3, 13) | 4 | 1/4 mod Z | Pati-Salam, alpha_PS = 1/17 |
| (7, 19) | 6 | 1/6 mod Z | 6 quarks, CKM matrix |

### 2.2 Is the bridge an algebraic correspondence?

For the bridge to be a motivic correspondence in Grothendieck's
sense, we need:

**Requirement 1: Algebraic varieties X, Y.** We need smooth
projective varieties whose cohomology carries the bridge data.

- **X side (input):** The cyclotomic field Q(zeta_N) defines a
  0-dimensional variety Spec(Q(zeta_N)), but more usefully, the
  CM abelian variety A_N with CM by Z[zeta_N] is a smooth
  projective variety whose Frobenius encodes the same data.
  For N = 13: A_13 is a 6-dimensional abelian variety.
  For N = 19: A_19 is a 9-dimensional abelian variety.
  
- **Y side (output):** The Jones sub-factor cocycle beta_k lives
  in group cohomology H^2(Z/kZ, U(1)) = Z/kZ. This is discrete
  (torsion). To make it geometric, embed it in the Brauer group
  of a variety. The cyclic algebra (Q(zeta_N)/Q, Frob_p, zeta_k)
  is an Azumaya algebra on a Brauer-Severi variety BS_k.

- **Algebraic correspondence:** A cycle Z in A_N x BS_k. The
  bridge map is then the composition:
  
      Frob_p |--> [Z]_* : H^*(A_N) --> H^*(BS_k)
  
  where [Z]_* is the pushforward along Z.

**Requirement 2: Algebraicity of the cycle.** The correspondence
Z must be an algebraic cycle, not merely a topological one. This
is the hard part. The bridge is DEFINED using:
- Frobenius elements (algebraic: they act on etale cohomology)
- Cyclic algebra construction (algebraic: Brauer group operations)
- Fuglede-Kadison determinant (analytic: involves operator traces)

The first two steps are algebraic. The third (FK determinant) is
the obstruction: it passes through II_1-factor completions, which
are analytic, not algebraic.

**Requirement 3: Respect the Hodge filtration.** If the
correspondence is algebraic, it automatically preserves the Hodge
filtration (Hodge = algebraic is the whole point). So this
requirement reduces to Requirement 2.

**Requirement 4: Commute with comparison isomorphisms.** Algebraic
correspondences commute with the comparison between Betti and
de Rham cohomology (by the de Rham comparison theorem). Again,
this follows from algebraicity.

### 2.3 Assessment of algebraicity

The bridge map has three stages:

1. **Frob_p --> cyclic algebra class.** This is the map
   Gal(Q(zeta_N)/Q) --> Br(Q) sending the Frobenius to the
   Brauer class of (Q(zeta_N)/Q, Frob_p, zeta_k). This map is
   **algebraic** -- it is a standard construction in class field
   theory and the theory of central simple algebras. It is a
   morphism of group schemes (Galois group to Brauer group).

2. **Cyclic algebra class --> H^2(Z/kZ, U(1)).** This is the
   isomorphism Br(Q(zeta_N)/Q) = H^2(Gal, Q(zeta_N)^*) restricted
   to the k-torsion, then mapped via the exponential sequence.
   This is **algebraic** -- it is the Brauer group computation
   via group cohomology (Tate's theorem).

3. **H^2(Z/kZ, U(1)) --> Jones sub-factor.** This uses the
   Fuglede-Kadison determinant to identify the Brauer cocycle
   with a Jones index-k sub-factor. This step is **analytic**:
   the FK determinant involves a von Neumann algebra trace, which
   is not an algebraic operation.

**Conclusion:** Steps 1-2 are algebraic, step 3 is analytic.
The full bridge is NOT manifestly a motivic correspondence.
However, steps 1-2 alone already constitute a motivic morphism
(Galois to Brauer), and step 3 might be replaceable by an
algebraic construction if the Jones sub-factor data can be
recovered from the Brauer class alone (which it can, for cyclic
sub-factors: the Jones index equals the degree of the cyclic
algebra, which IS algebraic).

**Revised conclusion:** The bridge map Frob_p --> beta_k in Z/kZ
(forgetting the von Neumann completion) IS algebraic. The
motivic content is in steps 1-2. Step 3 is a non-algebraic
INTERPRETATION but not a non-algebraic CONSTRUCTION.

---

## 3. The Tate conjecture connection

### 3.1 Statement

**Tate Conjecture (TC).** For a smooth projective variety X over
a finite field F_q, the cycle class map

    CH^p(X) tensor Q_l --> H^{2p}(X_{F_q-bar}, Q_l)^{Gal}

is surjective. Equivalently: the Frobenius-fixed classes in
l-adic cohomology are algebraic.

### 3.2 The bridge gives a Tate-to-Hodge pipeline

The bridge connects Frobenius eigenvalues to cohomology classes:

    Frob_p eigenvalues
      |
      | (Tate conjecture: these determine algebraic cycles mod p)
      v
    Algebraic cycles on X_{F_p}
      |
      | (bridge map: cyclic algebra construction)
      v
    beta_k in H^2(Z/kZ, U(1))
      |
      | (lift to characteristic 0 via CM theory)
      v
    Hodge classes on X_C

The key insight: **if the Tate conjecture holds for the CM abelian
variety A_N at the bridge primes p, then the bridge identifies
the Frobenius-fixed cycles, and CM theory lifts them to
characteristic 0 as Hodge classes that are algebraic.**

### 3.3 What is known

- **Tate for CM abelian varieties:** PROVED for abelian varieties
  with CM, in many cases (Tate 1966 for dim 1; Milne, Zarhin
  for higher dimension). The CM endomorphisms generate the
  Frobenius-fixed classes.

- **Hodge for CM abelian varieties:** OPEN in general. Known for:
  - Powers of CM elliptic curves (Hazama, Murasaki)
  - CM abelian varieties of prime dimension (Tankeev)
  - Some CM abelian varieties via Hodge group computation
    (Moonen-Zarhin)

- **The gap:** Tate is known, Hodge is not. The missing piece is
  the LIFT from characteristic p to characteristic 0. The bridge
  might provide this lift because it works over Q (not over F_p).

### 3.4 The Tate-Bridge-Hodge chain

If we can show:
1. Tate holds for A_N at bridge primes (known for CM)
2. Bridge map preserves algebraicity (algebraic steps 1-2: yes)
3. CM lift preserves algebraicity (Serre-Tate theory: yes for
   ordinary primes)

Then: Hodge holds for A_N.

**Status:** Each step is individually supported. The composition
has not been verified.

---

## 4. The Langlands connection

### 4.1 Langlands reciprocity (schematic)

    Automorphic representations of GL_n(A_Q)
      |
      | (Langlands reciprocity, partially proved)
      v
    Galois representations Gal(Q-bar/Q) --> GL_n(Q_l)
      |
      | (motivic: attached to motives)
      v
    Pure motives over Q
      |
      | (Hodge realisation)
      v
    Hodge structures

### 4.2 Where the bridge sits

The bridge map occupies a SPECIFIC slot in this diagram:

    Frob_p in Gal(Q(zeta_N)/Q)     [Galois representation, abelian]
      |
      | (bridge: cyclic algebra construction)
      v
    beta_k in Br(Q(zeta_N)/Q)      [Brauer class = motivic data]
      |
      | (FK identification)
      v
    Jones sub-factor cocycle         [operator/automorphic side]

The bridge connects the GALOIS side (Frobenius) to something on
the AUTOMORPHIC side (sub-factor = operator algebra). This is
precisely the abelian case of Langlands reciprocity (class field
theory). The Frobenius-to-Brauer map IS the local reciprocity
map of class field theory.

### 4.3 Langlands and Hodge

Langlands' conjecture implies:
- Motivic L-functions = automorphic L-functions
- Algebraic cycles --> automorphic forms (via motives)
- Hodge classes --> Galois-fixed classes (via comparison)

The bridge family realizes the abelian case: the cyclotomic
Galois group acts, the bridge identifies the fixed classes, and
these correspond to algebraic cycles (if Hodge holds).

**Key observation:** The bridge family uses ONLY abelian Galois
groups (cyclotomic fields). This means it accesses only the
abelian part of Langlands. For Hodge on general varieties, one
needs non-abelian reciprocity (the full Langlands programme).
The bridge as currently constructed cannot reach non-abelian
territory.

### 4.4 Scope limitation

The bridge can contribute to Hodge ONLY for varieties whose
Hodge classes are controlled by abelian Galois representations
(i.e., CM abelian varieties and their products). For varieties
with non-abelian fundamental group or non-CM Hodge classes, the
bridge is silent.

---

## 5. Feasibility assessment

### 5.1 The four options

**(a) Proved?** No. The bridge has not been shown to be a motivic
correspondence. The algebraicity of steps 1-2 is standard, but
the composition into a Hodge-preserving correspondence has not
been constructed.

**(b) Plausible?** Yes, with caveats. The structural evidence:
- Steps 1-2 of the bridge ARE algebraic (class field theory)
- The Tate conjecture holds for CM abelian varieties
- CM theory provides characteristic 0 lifts
- The bridge data (torsion Brauer classes) are motivic
- The Frobenius-to-Brauer map IS the local reciprocity map

The caveats:
- Step 3 (FK determinant) is analytic, not algebraic
- Scope limited to CM abelian varieties (abelian Langlands)
- No explicit motivic correspondence has been written down
- The surjectivity on Hodge classes is far from clear

**(c) Speculative?** Partially. The identification of bridge
cocycles with algebraic cycles is speculative. The motivic
interpretation of steps 1-2 is not speculative.

**(d) Impossible?** No structural obstruction is visible. The
bridge maps between objects that DO live in the motivic world
(Galois representations, Brauer groups, CM abelian varieties).
The obstruction is technical (constructing the explicit
correspondence), not structural.

### 5.2 Verdict

**Feasibility: (b) Plausible, restricted to CM abelian varieties.**

The motivic bridge is NOT a royal road to full Hodge. It is a
plausible path to Hodge for CM abelian varieties, which is already
a significant open problem. The Tate-Bridge-Hodge chain has
individually supported steps but has not been composed.

Rating: **3/10 for full Hodge, 5/10 for CM Hodge.**

Compared to Path 1 (CM abelian varieties, 4-6/10): Path 3 is
deeper but harder. Path 1 computes directly; Path 3 requires
constructing a motivic correspondence.

---

## 6. What a proof would look like

### 6.1 Proof sketch (CM abelian varieties)

**Theorem (conditional).** Let A_N be a CM abelian variety with
CM by Z[zeta_N], where N is in the bridge conductor set {7,13,19}.
Then every Hodge class on A_N is algebraic.

**Proof sketch:**

**Step 1 (Motivic correspondence).** Construct the algebraic
correspondence Z_k in A_N x BS_k as follows:
- The Frobenius Frob_p generates Gal(Q(zeta_N)/Q)
- The cyclic algebra C_k = (Q(zeta_N)/Q, Frob_p, zeta_k) defines
  a Brauer-Severi variety BS_k
- The graph of the norm map N_{Q(zeta_N)/Q^{Frob_p}} defines a
  cycle Z_k in A_N x BS_k
- By class field theory, Z_k is algebraic

**Step 2 (Hodge filtration).** The correspondence [Z_k]_* maps:
    H^{2p}(A_N, Q) --> H^{2p}(BS_k, Q)
Since Z_k is algebraic, this map preserves the Hodge filtration:
    F^p H^{2p}(A_N) --> F^p H^{2p}(BS_k)
In particular, Hodge classes map to Hodge classes.

**Step 3 (Tate at finite places).** By the Tate conjecture for
CM abelian varieties (known), the Frobenius-fixed classes in
H^{2p}(A_N x F_p-bar, Q_l) are algebraic. These are precisely
the classes in the image of the bridge at (p, N).

**Step 4 (CM lift).** By Serre-Tate deformation theory, the
algebraic cycles at the bridge primes lift to characteristic 0,
giving algebraic cycles on A_N over Q.

**Step 5 (Surjectivity).** The bridge family at ALL primes p
(not just the four bridge entries) generates the full Galois
action on H^*(A_N). By CM theory (Shimura-Taniyama), the CM
endomorphisms plus the bridge correspondences generate ALL
Hodge classes.

**Step 6 (Conclusion).** Every Hodge class on A_N is in the
Q-span of algebraic cycle classes. QED.

### 6.2 The gaps

- **Step 1:** The explicit algebraic cycle Z_k needs construction.
  The norm map graph is a natural candidate but has not been
  verified to give the right correspondence.
  
- **Step 5:** Surjectivity is the hardest step. One needs to show
  that the bridge at all primes, together with CM endomorphisms,
  generates all Hodge classes. This requires computing the Hodge
  group Hg(A_N) and showing it equals the Mumford-Tate group
  MT(A_N), which is known to equal the CM reflex group for CM
  abelian varieties but whose Hodge classes have not been fully
  enumerated for N = 13, 19.

- **Full Hodge:** This proof sketch works ONLY for CM abelian
  varieties with CM by cyclotomic fields. Extension to general
  smooth projective varieties requires the full (non-abelian)
  Langlands programme, which is far out of reach.

### 6.3 What would upgrade this to 6/10

1. Compute the Hodge group Hg(A_13) explicitly and verify that
   the bridge cocycle at (5,13) generates a non-trivial Hodge class.
2. Construct the explicit algebraic cycle Z_3 on A_13 x BS_3.
3. Verify surjectivity on H^2(A_13) (the easiest case).

If all three succeed, Path 3 merges with Path 1 and the combined
path becomes 6/10 for CM Hodge.

---

## 7. Key references

- Grothendieck, "Standard Conjectures" (1968): motives, algebraic
  correspondences, Hodge realisation
- Deligne, "Hodge cycles on abelian varieties" (Hodge II, 1982):
  absolute Hodge classes, CM abelian varieties
- Tate, "Algebraic cycles and poles of zeta functions" (1965):
  Tate conjecture
- Milne, "The Tate conjecture over finite fields" (AIM 2007):
  status of Tate for abelian varieties
- Moonen-Zarhin, "Hodge classes on abelian varieties of low
  dimension" (1999): Hodge for CM abelian varieties
- Langlands, "Automorphic representations, Shimura varieties,
  and motives" (1979): the Langlands programme and motives
- Abdulali, "Hodge structures of CM type" (2004): Hodge for
  certain CM abelian varieties
- Andre, "Motifs de dimension finie" (2004): finite-dimensional
  motives and the standard conjectures

---

## 8. Next steps

1. **Priority:** Path 1 (CM abelian varieties, direct computation)
   remains the strongest attack. Do the key computation for A_13.
2. **Path 3 support:** If Path 1 succeeds, reinterpret the result
   in motivic language (likely straightforward post-hoc).
3. **Tate-Bridge-Hodge chain:** Verify the chain for A_13 at p=5.
   This is a concrete finite computation.
4. **Langlands scoping:** Determine whether non-abelian bridge
   extensions (beyond cyclotomic) could access non-CM varieties.
   This is speculative but worth a research note.

---

> *The bridge is algebraic in its core (steps 1-2). The motivic*
> *interpretation is plausible but unproved. The scope is limited*
> *to CM abelian varieties. Path 3 is the deepest route to Hodge*
> *but Path 1 is faster. They likely converge.*
