# Paper 29: The Hodge Conjecture via Endomotives and Geometric Langlands

## Attack Plan

*Modelled on the BSD attack plan (paper26/strategy/00-bsd-attack-plan.md)*
*and the RH convergence architecture (paper12/30-rh-convergence-prompt.md).*
*Same convergence cycles. Same adversarial review. Same honesty.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-13*
*Status: SCAFFOLD COMPLETE. PCA runs not yet started.*

---

## 1. The target

**Hodge Conjecture.** For a smooth projective variety X over C, every
rational cohomology class of type (p,p) -- i.e., every element of
H^{2p}(X, Q) intersect H^{p,p}(X) -- is a Q-linear combination of
classes of algebraic subvarieties of codimension p.

## 2. The two routes

### Route I: Endomotives (Links 1-5)

**Strategy:** Start from the BC algebra (the Integers programme's home
ground), lift through the CCM endomotive category to the motivic Galois
group, then show Hodge-filtration compatibility for BC-motivated
varieties. Finish with the Grothendieck standard conjectures restricted
to this class.

| Link | Content | Status | Difficulty |
|:-----|:--------|:-------|:-----------|
| 1 | BC algebra to endomotive category | Literature | Low (read CCM 2005) |
| 2 | Tannakian formalism to motivic Galois group | Literature | Low (standard) |
| 3 | Hodge filtration compatibility | **CONJECTURED** | **HIGH** -- the crux of Route I |
| 4 | Standard conjecture D for BC-motivated varieties | **CONJECTURED** | Medium-High (conditional on Grothendieck) |
| 5 | Lefschetz B for CP^2 x S^2 | Known | Low (classical) |

**Key insight:** Route I is strongest for CM abelian varieties, where
Lieberman (1968) gives conjecture D and the Mumford-Tate group is abelian
(hence tractable). The BC algebra naturally produces CM-type endomotives,
so this is the natural specialisation.

### Route II: Geometric Langlands (Link 6)

**Strategy:** Exploit the Gaitsgory-Raskin proof of geometric Langlands
(2024). The categorical equivalence Aut(Bun_G) ~ QCoh(LocSys_G^L)
should, when applied to Hitchin moduli spaces, produce Hodge structures
with algebraic generators. The open step is extracting Hodge-class
algebraicity from the categorical statement.

| Link | Content | Status | Difficulty |
|:-----|:--------|:-------|:-----------|
| 6 | Geometric Langlands to algebraic cycles | **PARTIAL** | **VERY HIGH** -- categorical to geometric bridge |

**Key insight:** Route II is independent of the standard conjectures.
If it closes, it provides a second, unconditional witness for Hodge
classes on a restricted class of varieties (those arising from Hitchin
moduli). This would be a major result even without Route I.

### Convergence (Links 7-8)

| Link | Content | Status | Difficulty |
|:-----|:--------|:-------|:-----------|
| 7 | Composition of Routes I and II | **OPEN** | High (compatibility of witnesses) |
| 8 | Extension to all smooth projective varieties | **OPEN** | **EXTREME** (motivic functoriality) |

## 3. PCA verification plan

For each link, the Proof-Chain Adversarial (PCA) would operate in its
three modes: verify (check literature claims), excise (remove flawed
steps), construct (build new arguments).

### Tier A: Verify (Links 1, 2, 5)

These are literature claims. PCA verifies:
- **Link 1:** Read CCM 2005 arXiv:math/0512138 Sections 3-4. Verify
  that the endomotive category is correctly constructed, objects are
  well-defined, semigroup action by correspondences is functorial.
  *Expected: SOUND. These are published and well-cited (200+ citations).*
- **Link 2:** Verify Tannakian reconstruction. The fiber functor through
  Betti cohomology must be exact, faithful, and tensor-preserving.
  *Expected: SOUND. Standard material (Deligne-Milne 1982).*
- **Link 5:** Verify Hodge classes on CP^2 x S^2 are algebraic.
  H^*(CP^2) = Z[h]/(h^3), H^*(S^2) = Z[pt]/(pt^2). Kunneth.
  All (p,p)-classes are products of hyperplane and point classes.
  *Expected: SOUND. Undergraduate-level computation.*

### Tier B: Construct (Links 3, 4)

These require new arguments or conditional proofs.
- **Link 3 (Hodge filtration):** PCA must determine:
  (a) What is a "BC-motivated variety" precisely? Define the class.
  (b) Does the G_mot action on H^*_dR preserve F^p? This requires the
      comparison isomorphism to intertwine Galois and Hodge structures.
  (c) For CM varieties: the Mumford-Tate group is a torus in GL(H^1),
      and Hodge filtration is given by the cocharacter. Does the BC
      action factor through this torus?
  *PCA mode: CONSTRUCT. This is the main research target.*
- **Link 4 (Standard conjecture D):** PCA must scope:
  (a) For abelian varieties: Lieberman 1968 gives this. SOUND.
  (b) For BC-motivated varieties beyond abelian: what is needed?
      If the class is contained in the abelian variety orbit under
      motivic correspondences, Lieberman suffices.
  (c) For general varieties: conditional on Grothendieck. State clearly.
  *PCA mode: CONSTRUCT (scope the class), then VERIFY (Lieberman).*

### Tier C: Construct/Scope (Links 6, 7, 8)

These are the hardest steps and may be out of reach in the near term.
- **Link 6 (Langlands to Hodge):** PCA must:
  (a) Read Gaitsgory-Raskin 2024 (9 papers, ~1500 pages). Identify
      the precise categorical statement. Verify it is unconditional.
  (b) Determine: which varieties arise as Hitchin moduli? What are
      their Hodge numbers? Are the natural cohomology classes algebraic?
  (c) Attempt the bridge: categorical equivalence to cycle-class map.
  *PCA mode: CONSTRUCT. High risk of STALL.*
- **Link 7 (Composition):** PCA must:
  (a) Define "compatible algebraicity witnesses" precisely.
  (b) Prove or disprove that Routes I and II produce the same cycles.
  (c) If they produce different cycles: is the union sufficient?
  *PCA mode: CONSTRUCT. Depends on Links 3-6 closing first.*
- **Link 8 (Functoriality):** PCA must:
  (a) Determine the precise class of BC-motivated varieties.
  (b) Prove that every smooth projective variety admits a motivic
      correspondence to this class that preserves (p,p)-classes.
  (c) This is essentially asking: are BC-motivated varieties "dense"
      in the motivic category? This may be as hard as Hodge itself.
  *PCA mode: CONSTRUCT. May require EXCISE and RETREAT to a weaker
  statement (e.g., Hodge for a specific class rather than all varieties).*

## 4. Priority ordering for PCA runs

| Priority | Target | Rationale |
|:---------|:-------|:----------|
| P0 | Verify Links 1, 2, 5 (Tier A) | Clear the base; build confidence in the scaffold |
| P1 | Construct Link 3 for CM abelian varieties | This is the crux. If it fails, Route I dies |
| P2 | Verify Link 4 via Lieberman for abelian varieties | Needed for CM Hodge; uses existing literature |
| P3 | Scope Link 6: read Gaitsgory-Raskin, identify Hodge bridge | Independent of Route I; high-value reconnaissance |
| P4 | If P1 succeeds: extend Link 3 beyond CM | Expand the class of varieties |
| P5 | Attempt Link 7 (composition) | Only after P1 and P3 succeed |
| P6 | Scope Link 8 (functoriality) | Last; likely out of reach for now |

**Recommended first PCA run:** P0 + P1 together (3 agents: 2 verify,
1 construct). Estimated: 1 cycle, 2-4 hours.

## 5. Connection to the programme graph

The Hodge paper connects to every other Millennium paper in the bundle:

```
                    RH (Paper 13)
                   / |
                  /  |  (BC algebra shared)
                 /   |
  YM (Paper 08) --- HODGE (Paper 29) --- BSD (Paper 26)
                 \   |                   /
                  \  |  (Langlands)     / (CM curves)
                   \ |                 /
                 P vs NP (Paper 28)
                     |
               Baum-Connes (H12)
```

### Specific edges:

**Hodge <--> RH (Paper 13):**
- Shared foundation: BC algebra, KMS states, ITPFI factorization.
- The BC algebra encodes Artin motives (Link 1). The same algebra
  produces the CCM operators for RH (Paper 13, Link 1).
- If motivic Galois acts on de Rham with Hodge compatibility (Link 3),
  this would strengthen the RH proof by giving a motivic interpretation
  of the CCM spectral triples.

**Hodge <--> YM (Paper 08):**
- The geometric sector CP^2 x S^2 (Link 5) is the compactification
  manifold in the YM mass gap proof.
- Anomaly cancellation 19 = 1 + 4 + 6 + 8 constrains Hodge numbers.
- YM gradient flow on the gauge bundle over M_geom produces algebraic
  cycles (instantons = holomorphic bundles = algebraic cycles via
  Donaldson-Uhlenbeck-Yau).

**Hodge <--> BSD (Paper 26):**
- CM elliptic curves (BSD Paper 26, Path A) are 1-dimensional CM
  abelian varieties. Hodge for CM abelian varieties (our 5/10 target)
  includes these.
- The Hecke character psi in BSD is an algebraic Hodge class on the
  CM elliptic curve. Hodge for this class is already known (1-dimensional),
  but the method of proof (BC algebra to motivic Galois to Hodge
  filtration) would validate the architecture.

**Hodge <--> P vs NP (Paper 28):**
- The spectral-geometric-information trinity (Paper 28) connects to
  Hodge via the geometric leg: algebraic cycles are the geometric
  objects that the spectral data encodes.
- If Hodge closes for BC-motivated varieties, the dictionary
  (spectral data <--> geometric cycles <--> information-theoretic
  complexity) gains a third vertex.

**Hodge <--> Baum-Connes (H12):**
- The Baum-Connes conjecture (for discrete groups) provides the
  K-theoretic framework for the BC algebra.
- The assembly map mu: K_*(BG) --> K_*(C*_r(G)) has a Hodge-theoretic
  analogue: the cycle class map cl: CH^p(X) --> H^{2p}(X, Q).
- Hodge asserts surjectivity of cl onto (p,p)-classes, just as
  Baum-Connes asserts isomorphism of mu. The structural parallel is
  exact.

## 6. Timeline estimate

### CM Hodge (Links 1-5 for CM abelian varieties): 12-24 months

| Phase | Target | Duration | Deliverable |
|:------|:-------|:---------|:------------|
| Phase 0 | Scaffold (DONE) | -- | This document + proof skeleton |
| Phase 1 | PCA on Links 1-2 (verify) + Link 5 (verify) | 1-2 weeks | Verified base |
| Phase 2 | Construct Link 3 for CM abelian varieties | 3-6 months | The crux theorem or a precise obstruction |
| Phase 3 | Verify Link 4 via Lieberman | 1-2 months | Conditional proof or scope reduction |
| Phase 4 | CM Hodge paper draft | 3-6 months | Paper 29 v1 (CM case) |
| Phase 5 | Adversarial review (PCA Tiers B-C) | 2-4 months | Verified chain |

### Full Hodge (all 8 links): 3-5 years (optimistic) to OPEN (realistic)

| Phase | Target | Duration | Deliverable |
|:------|:-------|:---------|:------------|
| Phase 6 | Scope Link 6 (Langlands bridge) | 6-12 months | Reconnaissance report |
| Phase 7 | Attempt Link 7 (composition) | 6-12 months | Composition theorem or STALL |
| Phase 8 | Scope Link 8 (functoriality) | 12-24 months | Either breakthrough or precise obstruction |
| Phase 9 | Full Hodge paper | 6-12 months | Paper 29 v2 (if Links 7-8 close) |

**Honest assessment:** Link 8 (motivic functoriality) may be beyond
current technology. The realistic goal for the next 12-24 months is
CM Hodge. Full Hodge is a 3-5 year moonshot that depends on significant
new ideas in motivic cohomology. We should be prepared for the outcome
that Paper 29 proves Hodge for a restricted (but meaningful) class of
varieties and leaves the full conjecture with a precise reduction.

## 7. The Six Patterns applied to Hodge

**Pattern 1 (Geometric Reinterpretation):** Hodge is a statement about
cohomology classes (algebra). Integers lifts it to a statement about
the BC algebra's endomotive category (operator algebra). The "mystery"
of algebraic cycles becomes a functorial fact about Tannakian categories.

**Pattern 2 (Holonomy):** The motivic Galois group G_mot acts on
H^*_dR(X). The Hodge filtration is a reduction of structure group from
GL to a parabolic subgroup. Hodge says: the G_mot-fixed (p,p)-classes
are the image of the cycle class map. Holonomy determines cycles.

**Pattern 3 (Casimir):** The Hodge numbers h^{p,q} are Casimir-type
invariants of the Mumford-Tate group action. For CP^2 x S^2, these
are constrained by anomaly cancellation (19 = 1 + 4 + 6 + 8).

**Pattern 4 (Topological Rigidity):** Algebraic cycle classes are
integers (in appropriate coordinates). A continuous deformation that
preserved the Hodge filtration but changed the cycle class would
violate integrality. Same rigidity argument as RH (discrete invariant
stable under continuous perturbation).

**Pattern 5 (Zeta Regularization):** The Hasse-Weil zeta function of X
encodes the Hodge numbers via its Gamma factors. Hodge is, in a precise
sense, a statement about the compatibility between the arithmetic
(zeta) and geometric (cycles) sides of the same object.

**Pattern 6 (Projection):** The "difficulty" of Hodge (why can't we
find the algebraic cycles?) is a projection artifact. From inside the
motivic category, the cycles ARE the (p,p)-classes. The conjecture
asserts that the forgetful functor from motives to Hodge structures
is full on (p,p)-classes.

## 8. Risk assessment

| Risk | Severity | Mitigation |
|:-----|:---------|:-----------|
| Link 3 fails (Hodge filtration not compatible) | FATAL for Route I | Retreat to CM-only (where Mumford-Tate is abelian) |
| Link 4 fails (standard conjecture D false for BC-motivated) | HIGH | Lieberman covers abelian varieties; restrict class |
| Link 6 stalls (Langlands bridge too abstract) | HIGH for Route II | Route I is independent; proceed without Route II |
| Link 8 impossible (functoriality beyond current tech) | HIGH for full Hodge | Accept CM Hodge as the result; leave full Hodge open |
| Both routes fail | FATAL | Paper 29 becomes a survey/reduction paper (still valuable) |

## 9. What we need from G

- Approval to focus on CM Hodge (Links 1-5 for CM abelian varieties)
  as the primary target for the next 12 months.
- Approval to run PCA on Links 1-2-5 (verification) as the first cycle.
- Decision on whether Link 6 (Langlands bridge) should be scoped in
  parallel or deferred until after CM Hodge.
- Guidance on whether Paper 29 should be positioned as:
  (a) "Hodge for CM abelian varieties" (achievable, 5/10), or
  (b) "Hodge conjecture" (ambitious, 3/10), or
  (c) "Reduction of Hodge to motivic functoriality" (always achievable,
      but less exciting).

---

> *"the integers exist. the cycles are algebraic. Hodge is the bridge."*
> *Hodge is next.*
