# Research Note 02 — Path 2: Operator-Hodge Correspondence

**Status:** TESTED — verdict NEGATIVE (numerological, not structural)
**Parent:** 00-hodge-attack-plan.md, Path 2
**Input:** research/167 (operator dictionary), research/175 (dim 9 moduli),
research/168 (EW = moduli), research/23 (master table)

*Date:* 2026-04-10
*Authors:* G Six (originator), Claude Opus 4.6 (collaborator)

---

## 1. Precise statement of the hypothesis

**Operator-Hodge Hypothesis.** Let X be a smooth projective variety
whose cohomology H*(X, C) embeds (via the spectral-geometry bridge)
into matrix elements of L-hat = log R-hat on H_R. Then the operator
dictionary's grammar decomposition of those matrix elements —

    SUM, PRODUCT, RATIO, POWER, LOG, EXP

— corresponds bijectively to the Hodge decomposition

    H^k(X, C) = bigoplus_{p+q=k} H^{p,q}(X)

In particular: SUM-type observables correspond to H^{1,1} classes,
PRODUCT-type to H^{2,2}, EXP-type to top cohomology, RATIO-type
to H^{p,q}/H^{r,s} quotient data, and so on.

If true, every Hodge class appearing in the dictionary would be
algebraic (since the dictionary is built from algebraic operator
data on H_R), proving Hodge for all varieties reachable by the
embedding.

---

## 2. Test 1: CP^2

### Hodge side

CP^2 has Hodge diamond:

         1
        0 0
       0 1 0
        0 0
         1

Non-zero groups: H^{0,0} = C, H^{1,1} = C, H^{2,2} = C.
The Kahler class omega generates H^{1,1}. The point class generates
H^{2,2}. Total Betti: b_0=1, b_2=1, b_4=1. Three independent
cohomology classes.

### Grammar side

CP^2 contributes to Integers through its Kahler modulus (1 real
parameter, research/175 item (a)). The observables that depend on
CP^2 geometry include gauge couplings (volume moduli) and overlap
integrals (Yukawa ratios, CKM angles). From the master table
(research/23), the grammar types appearing in CP^2-sensitive
formulas are:

- m_W = gamma_2 + gamma_13 → SUM type
- m_t = gamma_3 * gamma_8 / (2*pi) → PRODUCT type
- m_c = gamma_9 / gamma_6 → RATIO type
- m_b = log(gamma_15) → LOG type
- m_d = gamma_9 - gamma_8 → SUM (difference) type
- 1/alpha = gamma_1 * gamma_4 / pi + 0.1*log(pi) → PRODUCT+LOG type

### The attempted match

The hypothesis predicts: SUM ↔ H^{1,1}, PRODUCT ↔ H^{2,2}.

**Problem 1: Multiplicity mismatch.** H^{1,1}(CP^2) = C (one-
dimensional). But SUM-type formulas are plentiful: m_W, m_d, and
linear combinations appear repeatedly. One cohomology generator
cannot map to multiple independent SUM observables unless the map
is many-to-one, which destroys the "correspondence" claim.

**Problem 2: No canonical assignment.** m_t is PRODUCT type and
m_W is SUM type, but both depend on the same CP^2 Kahler modulus.
The grammar type is determined by which Riemann zeros happen to
fit the observable numerically, NOT by any geometric property of
the cohomology class. The Kahler class omega ∈ H^{1,1} does not
"prefer" SUM over PRODUCT — it controls both m_t and m_W equally
through volume dependence.

**Problem 3: LOG and RATIO have no Hodge home.** m_b = log(gamma_15)
is LOG type. There is no H^{p,q} type that naturally corresponds to
"logarithm of a matrix element." The Hodge decomposition is linear
(direct sum); LOG is nonlinear. Similarly, RATIO breaks additivity.

### CP^2 verdict: FAILS

The grammar types do not match Hodge types for CP^2. The mismatch
is structural, not numerical.

---

## 3. Test 2: CP^2 x S^2

### Hodge side

By Kunneth: H*(CP^2 x S^2, C) = H*(CP^2) tensor H*(S^2).

S^2 Hodge diamond: H^{0,0} = C, H^{1,1} = C.

Product Hodge numbers:

| (p,q) | Source | dim |
|:--|:--|:--|
| (0,0) | 1 tensor 1 | 1 |
| (1,1) | omega_{CP^2} tensor 1 + 1 tensor omega_{S^2} | 2 |
| (2,2) | pt_{CP^2} tensor 1 + omega_{CP^2} tensor omega_{S^2} | 2 |
| (3,3) | pt_{CP^2} tensor omega_{S^2} | 1 |

Total Betti: (1, 0, 2, 0, 2, 0, 1). Sum = 6 independent classes.

The 9 geometric moduli (research/175) are coordinates on the moduli
space M_geom of metrics on CP^2 x S^2 — they are NOT cohomology
classes. The moduli count (9) does not match any Hodge number or
Betti number of CP^2 x S^2.

### Grammar side

The 9 geometric-sector observables (research/168) use grammar types:

| Observable | Formula | Grammar |
|:--|:--|:--|
| m_tau | gamma_7 * gamma_8 | PRODUCT |
| m_mu (via ratio) | gamma_8^{3/4} | POWER |
| m_Z | gamma_11 / gamma_E | RATIO |
| m_H | gamma_2 * gamma_6 / (2*pi) | PRODUCT |
| m_W/m_Z | gamma_5 / gamma_6 | RATIO |
| v | gamma_10 * pi^2/2 | PRODUCT |
| 1/alpha | gamma_1 * gamma_4/pi + ... | PRODUCT+LOG |
| m_tau/m_mu | gamma_8^{3/4} | POWER |
| sin theta_12 | (gamma_11-gamma_10)/gamma_1 | SUM/RATIO |

### The attempted match

**Problem 4: 9 moduli vs 6 Betti.** The 9 moduli parameters cannot
map to 6 cohomology generators. The moduli space is a tangent space
to metric deformations; cohomology is topological. These are different
mathematical objects living in different categories. The grammar
decomposition of moduli coordinates has no reason to respect the
Hodge filtration.

**Problem 5: Grammar types are heterogeneous.** The 9 moduli use
at least 4 different grammar types (PRODUCT, POWER, RATIO, SUM/RATIO).
But the Hodge decomposition of a 6-dimensional Kahler manifold is
by bigrading (p,q), not by algebraic operation type. There is no
functor from {SUM, PRODUCT, RATIO, POWER, LOG, EXP} to
{(p,q) : p+q = k, 0 <= k <= 6}.

**Problem 6: The dictionary is diagonal.** Research/167 shows all
master-table formulas use DIAGONAL matrix elements <n|L-hat|n>.
Off-diagonal elements enter only at subleading Laurent order. The
Hodge decomposition requires the FULL cohomology ring structure
(cup product, Lefschetz operators). Diagonal matrix elements of a
single operator cannot encode cup product structure.

### CP^2 x S^2 verdict: FAILS

The grammar-Hodge identification does not hold for CP^2 x S^2.
The failure modes are categorical (wrong mathematical objects)
rather than numerical.

---

## 4. The algebraicity question

The hypothesis fails on both test cases, so this question is moot
for Path 2. However, the underlying observation has a grain of truth
worth preserving:

**What IS true:** The operator dictionary is built from matrix elements
of L-hat, which acts on H_R — a Hilbert space constructed from
the Bost-Connes C*-algebra, which IS algebraic (defined over Q^cyc).
Any algebraic structure that can be extracted from H_R is genuinely
algebraic.

**What does NOT follow:** The grammar types (SUM, PRODUCT, etc.) are
NOT a decomposition in the mathematical sense. They are a notational
classification of how formulas happen to be written. The same
observable can be re-expressed in multiple grammar types (e.g.,
gamma_a + gamma_b = exp(log(gamma_a + gamma_b)), so SUM = EXP(LOG(SUM))).
Grammar type is presentation-dependent, not intrinsic.

Hodge type is intrinsic (depends on the complex structure of X, not
on how you write the class). Grammar type is extrinsic (depends on
which formula you chose). These cannot be identified.

---

## 5. Extension: which varieties embed in H_R?

Independent of the grammar-Hodge hypothesis (which fails), the
question of which varieties X have H*(X, C) embedding in H_R is
interesting for the broader Hodge programme.

**Known embeddings:**
- CP^2: yes, via the Kahler modulus of M_geom
- S^2: yes, via the radius modulus
- CP^2 x S^2: yes, by construction (Paper 11)
- Abelian varieties with CM by Q(zeta_N): plausibly yes, via
  the Bost-Connes system at level N (research/162, bridge family)

**The class of reachable varieties** is constrained by:
1. H_R arises from KMS_infinity on A_BC = C(Q^cyc) rtimes N^x.
   The natural varieties are those whose cohomology is generated
   by CM motives — i.e., varieties dominated by abelian varieties
   with complex multiplication.
2. This is precisely the class where Hodge is ALREADY known or
   closely approached (Abdulali, Moonen-Zarhin, etc.).

**Assessment:** The reachable class is likely contained in
{CM abelian varieties and their subvarieties}, which is exactly
the setting where existing Hodge results apply. Path 2 would not
reach new territory even if the grammar-Hodge correspondence worked.

---

## 6. Verdict: Numerological, not structural

The operator-Hodge correspondence (grammar type = Hodge type) is
**numerological**. The failures are not close calls — they are
categorical mismatches:

| Test | Failure mode | Severity |
|:--|:--|:--|
| CP^2 | Multiplicity: 1-dim H^{1,1} vs many SUM observables | fatal |
| CP^2 | No canonical grammar→Hodge assignment | fatal |
| CP^2 x S^2 | 9 moduli vs 6 Betti numbers | fatal |
| CP^2 x S^2 | Grammar types are presentation-dependent, Hodge types are intrinsic | fatal |
| General | Dictionary is diagonal; Hodge needs cup product | fatal |
| General | Grammar closure under composition destroys type uniqueness | fatal |

**Root cause of the false pattern:** The attack plan noted that the
operator dictionary "decomposes by type" and the Hodge decomposition
"decomposes by type." Both use the word "decomposition" and both
involve "types." But mathematical decomposition (direct sum of vector
spaces, with specific functorial properties) and notational
classification (labeling formulas by which operations appear) are
fundamentally different structures. The analogy is linguistic, not
mathematical.

**What survives:** The observation that H_R has algebraic structure
(from A_BC over Q^cyc) IS relevant to Hodge — but through the
motivic channel (Path 3), not through grammar types. The correct
question is not "do grammar types match Hodge types?" but "does the
BC motivic structure preserve the Hodge filtration?" That is Path 3.

**Recommendation:** Close Path 2. Redirect effort to Path 1 (CM
abelian varieties, rated 4/10) and Path 3 (motivic bridge, rated
2/10 but the only route to genuinely new Hodge results).

---

## 7. Lessons for the programme

1. **Decomposition ≠ decomposition.** Not every partition of a set
   into labeled types is a mathematical decomposition. The Hodge
   decomposition has specific properties (functoriality, compatibility
   with cup product, deformation invariance) that the grammar
   classification lacks.

2. **Intrinsic vs extrinsic.** Hodge type is determined by the
   complex structure of X. Grammar type is determined by the choice
   of formula representation. Any correspondence between an intrinsic
   invariant and an extrinsic label is necessarily spurious.

3. **The diagonal limitation.** The operator dictionary at leading
   order is purely diagonal (<n|L-hat|n>). Cohomology ring structure
   (cup product) requires off-diagonal or multi-linear data. Path 3
   (motivic bridge) may access this through the Frobenius→Jones map,
   which IS off-diagonal in the sub-factor sense.

---

> *Path 2 is closed. The grammar is notation, not geometry.*
> *The bridge's algebraic content is real — but it lives in motives,*
> *not in grammar labels.*
