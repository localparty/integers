# Paper (pvnp): P vs NP from the Integers Framework

## Attack Plan

*Fifth Clay Millennium Problem under Integers attack. Modelled on the*
*RH convergence architecture (paper12/30-rh-convergence-prompt.md),*
*the Yang-Mills gradient-flow attack plan (paper08-yang-mills/),*
*and the BSD, Hodge, and Navier attack plans (paper26-bsd/strategy/00-,*
*paper27-hodge/strategy/00-, paper27-navier/strategy/00-).*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date opened: 2026-04-10*
*Status: BRAINSTORMING → SCOPING*

---

## 1. The target

**P vs NP (Clay, Cook 2000).** Prove or disprove P = NP.

Equivalently: is there a deterministic polynomial-time algorithm for
3-SAT (or any other NP-complete problem)? The consensus expectation
is P ≠ NP. A proof must produce a super-polynomial lower bound for
some NP-complete problem in a model that excludes the Razborov–Rudich
"natural proofs" barrier and the Baker–Gill–Solovay "relativisation"
barrier and the Aaronson–Wigderson "algebrisation" barrier.

The three known barriers rule out most elementary techniques. Any
serious attack must be **non-natural, non-relativising, and
non-algebrising.** Geometric Complexity Theory (GCT) of Mulmuley–Sohoni
is the one programme in the literature that has a plausible story for
clearing all three barriers simultaneously, and it is explicitly
built on representation theory of reductive groups and Langlands-type
data — which is where Integers lives.

## 2. Why Integers has tools for this

P vs NP looks, at first pass, *maximally far* from a framework about
geometry, operator algebras, and the Riemann zeros. The case that
Integers has hooks rests on five observations, each of which points
into established literature that the framework's structures already
touch.

1. **GCT is Integers-adjacent.** Mulmuley–Sohoni's Geometric Complexity
   Theory reduces the VP vs VNP question (algebraic analogue of P vs
   NP) to a question about whether the permanent orbit closure in
   Sym^m(ℂ^{m²}) contains the determinant orbit closure. This becomes
   a question about plethysm coefficients of irreducible GL_n
   representations. Plethysm coefficients are exactly the kind of data
   the cyclotomic Brauer bridge family at k=2,3,4,6 computes in
   paper 24 — both sides live in H²(finite cyclic, U(1)) and both
   are detected by Fuglede–Kadison determinants.

2. **Natural-proofs barrier is trivially cleared by cohomological
   arguments.** Razborov–Rudich's theorem says any "natural"
   circuit-size lower bound would break pseudorandom generators.
   "Natural" means the property is constructive and large. **Cocycle
   classes in H²(G, U(1)) are neither constructive nor large** — they
   are cohomological obstructions that live in a proper subspace. The
   bridge family delivers lower bounds of exactly this shape.

3. **Relativisation-clearing via spectral flow.** Baker–Gill–Solovay
   shows that oracle-friendly arguments cannot decide P vs NP. The
   RH proof chain's layer-2 ITPFI argument (paper13-rh) is not an
   oracle argument — it uses intrinsic type classification of the
   hyperfinite factor, which does not commute with Turing reductions.
   This gives, in principle, a non-relativising technique.

4. **Algebrisation-clearing via non-commutative polynomials.** The
   Aaronson–Wigderson algebrisation barrier rules out arguments that
   extend to algebraic oracles. Bridge cocycles are non-commutative
   (they live in H² of a non-abelian-cohomology setup via the twisted
   group algebras of paper 24), which defeats the algebrisation
   extension.

5. **Complexity as modular entropy.** Connes's modular automorphism
   group σ_t parameterises "how hard it is to move a state". In an
   ITPFI factor, the Kolmogorov–Sinai entropy of σ_t is a topological
   invariant. Identifying circuit complexity with a discretised KS
   entropy of an associated modular flow is a plausible dictionary
   that has been hinted at in the physicist literature (Susskind's
   "complexity = action" conjecture has structural similarities but
   is about holography, not P vs NP directly).

## 3. The four attack paths

### Path A: GCT bridge (feasibility 5/10)

**Claim.** The cyclotomic Brauer bridge family at k=4 and k=6 (HP-2 in
`program/50+.md`) computes exactly the plethysm coefficients that
Mulmuley–Sohoni's GCT requires for the permanent-vs-determinant
separation. Closing HP-2 would, as a corollary, give a non-trivial
lower bound in the algebraic (VP vs VNP) regime.

**Key computation.** For the cyclotomic Brauer cocycle β_4 ∈
H²(Z/4Z, U(1)) at (3, 13) (Pati–Salam / α_PS⁻¹ = 17, paper12/184),
compute the image under the Mulmuley–Sohoni plethysm functor and
verify that it obstructs the permanent orbit closure at degree m ≥ 7.

**Obstacle.** GCT has been stuck for 20 years on the non-existence
of "obstruction families" that separate permanent from determinant
at super-polynomial degree. Framework cocycles may produce a family,
but proving super-polynomiality is the hard step.

**Reference to kill.** Bürgisser–Ikenmeyer 2017 "No occurrence
obstructions in geometric complexity theory" — shows certain classes
of plethysm-based obstructions cannot work. Framework obstructions
are different (cohomological, not occurrence-based), but this paper
must be read carefully to ensure the framework attack does not fall
into the same trap.

### Path B: Natural-proofs-free cocycle lower bound (feasibility 4/10)

**Claim.** For any circuit family {C_n} computing a hard Boolean
function f, the Brauer cocycle class [C_n] ∈ H²(S_{2^n}, U(1)) is
non-trivial for f ∈ NP and trivial for f ∈ P. Size lower bounds
follow from the cohomological class dimension.

**Key computation.** Define the Brauer class of a circuit via its
factorisation through twisted group algebras. Show functoriality
under polynomial-time reductions. Verify that 3-SAT has non-trivial
class at size n^{log n} or higher.

**Obstacle.** The "define the Brauer class of a circuit" step is
the load-bearing novelty; no such definition currently exists. A
rigorous definition would itself be a major mathematical advance.

### Path C: Modular entropy as complexity measure (feasibility 3/10)

**Claim.** There exists a canonical embedding Circ: Boolean circuits
→ endomorphisms of the hyperfinite II_1 factor R such that the
Kolmogorov–Sinai entropy h_KS(Circ(C)) = Θ(log size(C)). Super-
polynomial circuit lower bounds then reduce to Connes–Størmer
entropy lower bounds for automorphism orbits — a well-studied
operator-algebraic quantity.

**Key computation.** Construct Circ for AND, OR, NOT and verify
composition commutes with KS entropy. Apply to NP-complete
functions via standard reductions.

**Obstacle.** The construction is likely not functorial in a way
that gives tight bounds; a weak bound would not close P ≠ NP.

### Path D: Riemann-zero barrier (feasibility 2/10 — speculative)

**Claim.** The Riemann zeros γ_n, which control the Integers
framework's mass spectrum, also control circuit-size lower bounds
via an identity linking ζ-zero spacing statistics to the
concentration of measure on the Boolean hypercube. A specific
non-trivial zero would produce a super-polynomial lower bound.

**Obstacle.** This is the wildest of the four and is at the
"numerological hunch" level. Listed for completeness and because
Bourgain–Gamburd-style additive-combinatorics arguments have
recently used deep number theory for lower bounds (e.g., primality
in circuit complexity), so the idea is not a priori absurd.

## 4. Path feasibility summary

| Path | Mechanism | Feasibility | Key obstacle |
|:--|:--|:--|:--|
| A | GCT ← bridge family | 5/10 | Super-poly step |
| B | Cocycle class of circuits | 4/10 | Define the class |
| C | KS entropy ≈ complexity | 3/10 | Tightness of bound |
| D | ζ-zero barrier (speculative) | 2/10 | No rigorous link |
| E | Direct diagonalisation (classical) | 1/10 | Blocked by all 3 barriers |

## 5. The convergence cycle design

Same three-layer structure as RH / BSD / Hodge / Navier:

**Layer 1 — Construction** (1 agent per active path): attempt to
close the next open step. Input corpus: paper 24 (bridge family),
paper 25 (class field / Hilbert 12), paper 23 (BCB system), plus
Mulmuley–Sohoni GCT papers (1–8), Razborov–Rudich 1994,
Baker–Gill–Solovay 1975, Aaronson–Wigderson 2008, Bürgisser–Ikenmeyer
2017.

**Layer 2 — Adversarial**: try to break the construction. Known
traps: conflating algebraic and Boolean complexity; using the three
barriers against oneself by accident; assuming natural properties
when working with the cocycle class.

**Layer 3 — Synthesis**: update ledger, recommend next cycle focus.

## 6. The ledger

```
paper28-pvnp/strategy/pvnp-ledger.md
```

Status entries per path per cycle, following the BSD format.

## 7. Current status

- Attack plan drafted (this file). Status: BRAINSTORMING → SCOPING.
- No research/ entries yet.
- No preprint/ directory yet.
- Depends on HP-2 (bridge family k=4, k=6 cocycle equalities) for
  Path A to become actionable — HP-2 closure is a hard prerequisite.

## 8. Success conditions

- **Publishable partial result**: A rigorous definition of the
  cocycle class of a circuit (Path B step 1) would be publishable
  on its own as a new chapter of algebraic complexity theory.
- **GCT contribution**: Producing a framework-sourced obstruction
  family for VP vs VNP (Path A) that clears Bürgisser–Ikenmeyer's
  no-go would be a major result even short of a full Clay closure.
- **Clay-level closure**: A proof of P ≠ NP via any of paths A–C
  (clearing all three barriers) or, less likely, a proof of P = NP
  via a constructive algorithm extracted from the framework.
- **Framework payoff**: Path C's modular-entropy dictionary, if it
  works even weakly, would open a new bridge from the Integers
  programme to theoretical computer science — a fourth bridge
  family (after physics, number theory, and algebraic geometry).

## 9. What blocks SCOPING → IN PROGRESS

- Read Mulmuley–Sohoni GCT1–GCT8 and the Bürgisser–Ikenmeyer 2017
  no-go result carefully to confirm that framework cocycles are not
  ruled out by the same argument.
- Wait for HP-2 closure (k=4, k=6 bridge cocycle equalities in
  `program/50+.md` Block H) before Path A can attempt its first
  research cycle.
- Decide whether Path B's "Brauer class of a circuit" definition
  can be drafted without full HP-2, as a separate thread.
- Produce an initial research/001 note recording the precise
  plethysm ↔ cocycle dictionary shared with paper 24.

---

*This plan is a brainstorming snapshot. P vs NP is the Millennium*
*problem most distant from the Integers programme's natural home,*
*so feasibility scores are lower and each path carries substantial*
*risk of collapse. The plan is drafted to preserve the angles worth*
*trying so that an Executor cycle has somewhere to start when the*
*prerequisites (principally HP-2) are in place.*
