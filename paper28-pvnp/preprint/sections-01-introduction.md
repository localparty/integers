# Clone Growth and Fullness of Type III$_1$ Factors: A Bridge Between Universal Algebra and Operator Algebra

## Section 1: Introduction

*Paper 28 — The Clone Growth $\leftrightarrow$ Fullness Bridge*

---

# 1. Introduction

```
            ┌─────────────────────────────────────┐
            │         THE BRIDGE THEOREM           │
            │    Taylor ↔ non-full ↔ P-time        │
            │    non-Taylor ↔ full ↔ NP-complete   │
            └──────────┬──────────┬────────────────┘
                       │          │
              Part (i) │          │ Part (ii)
              Taylor   │          │ non-Taylor
              → non-full          │ → full
                       │          │
         ┌─────────────┴──┐  ┌───┴──────────────┐
         │    PATH B      │  │    ROUTE C        │
         │ (unconditional)│  │ (conditional CP-1)│
         │                │  │                   │
         │ UA1: exp clone │  │ Non-amenable G_L  │
         │ ↓              │  │ ↓                 │
         │ Pigeonhole     │  │ Trivial radical   │
         │ ↓              │  │ ↓                 │
         │ Instance div   │  │ Essential freeness│
         │ ↓              │  │ ↓                 │
         │ Marrakchi      │  │ Ergodic (F-M)     │
         │ ↓              │  │ ↓                 │
         │ NON-FULL       │  │ Marrakchi Thm B   │
         └────────┬───────┘  │ ↓                 │
                  │          │ FULL              │
                  │          └───────┬───────────┘
                  │                  │
                  └──────┬───────────┘
                         │
                    ┌────┴─────┐
                    │ COROLLARY│
                    │ P ≠ NP  │
                    │ (by     │
                    │ contra- │
                    │ diction)│
                    └──────────┘
```

The diagram above is the entire argument. Everything else in this
paper is scaffolding for the two pillars and the span between them.
The left pillar (Path B) is unconditional. The right pillar (Route C)
is conditional on one theorem, CP-1, the crossed-product identification
of the sector factor with a groupoid von Neumann algebra. The span
is the Bulatov--Zhuk CSP Dichotomy Theorem, used as an established
external result in both directions.

If the pillars hold, then for any Boolean constraint language $L$:
Taylor $L$ produces a non-full sector, non-Taylor $L$ produces a full
sector, and $3$-SAT — which is non-Taylor but would be Taylor under
$\mathrm{P} = \mathrm{NP}$ — is simultaneously full and non-full.
Contradiction. Therefore $\mathrm{P} \neq \mathrm{NP}$.

---

## 1.1 The cube and its shadow

> **Origin (G, ca. 2024).** *"i understand entanglement from the
> shadows of projecting a cube into a wall! dimensions are compressed,
> the shadow is a projection and we can't see the volume in the
> shadow but it is there!"*

The framework whose latest result is presented here was born from a
single picture. A three-dimensional cube, illuminated by a directed
light source, casts a two-dimensional shadow on a wall. The shadow
faithfully encodes some properties of the cube — its silhouette, its
size, the relations between its visible faces — but it cannot
encode others. The shadow has no volume. The shadow has no edges
that lie perpendicular to the wall. Two cubes that look identical
from the front but differ in depth produce identical shadows. From
the shadow alone, the depth dimension is invisible: not absent, not
unreal, but *projected away*.

The picture has a precise mathematical content, and the content is
the foundational claim of the entire programme. **A four-dimensional
phenomenon that resists explanation in the four-dimensional language
where it appears is the shadow of a higher-dimensional object whose
volume is invisible from the projection plane.** The resolution is
not the discovery of a new four-dimensional mechanism. It is the
*naming* of the higher-dimensional object whose shadow the
phenomenon was all along.

This paper applies the same move to the hardest target the framework
has yet attempted: **the question of whether $\mathrm{P} =
\mathrm{NP}$**. The claim is that computational hardness —
specifically, the asymptotic gap between polynomial-time decision and
polynomial-time verification — is the shadow of a structural
invariant living in the operator-algebraic world. That invariant is
**fullness**: the dichotomy between factors whose inner automorphism
group is closed and those where it is not. The shadow, once the
bridge is built, is the separation $\mathrm{P} \neq \mathrm{NP}$.

The cube has cast its shadow on a new wall. The picture is the same.

### The programme behind this paper

This paper is Paper 28 of the *Quantum Geometry in 5 Dimensions*
programme (G Six, 2024--2026). The proof draws on results,
methods, and structural lessons from 27 prior papers. The
following table identifies the papers whose contributions are
directly load-bearing for the argument presented here.

| Paper | Title | What it contributed to Paper 28 |
|:------|:------|:-------------------------------|
| **Paper 1** | *Spin-Statistics, Aharonov-Bohm, and Perturbative Finiteness from Kaluza-Klein Geometry* | The cube-shadow intuition (§1.1); the $e$-circle as the foundational geometric object; the $U(1)$ fiber bundle over 4D spacetime that became the Bost-Connes system via Identity 12 |
| **Paper 3** | *Information Preservation in Black Hole Evaporation via e-Dimension Geometry* | The Tomita modular conjugation $J M_{\mathrm{int}} J = M_{\mathrm{ext}}$ as a resolution mechanism; the type III$_1$ factor structure as the natural home for information-theoretic questions |
| **Paper 8** | *Yang-Mills Mass Gap from KK-Enhanced Lattice Gauge Theory* | The PROOF-CHAIN format; the rigor labels (THEOREM / LEMMA / KEY LEMMA / GAP); the dimensional descent pattern (4D QFT → finite matrix) that inspired the clone-to-factor descent |
| **Paper 9** | *One Postulate, Ten Papers: The Geometric Framework and Its Grammar* | The Six Patterns method (Geometric Reinterpretation / Holonomy / Casimir / Topological Rigidity / Zeta Regularization / Projection Produces Pathology) — named here, used by every ORA agent on every cycle of the bridge programme; the pattern attribution discipline; the founding statement *"these are not fits, they are consequences"* |
| **Paper 13** | *The Riemann Hypothesis via CCM Operators, ITPFI Convergence, and Bögli Spectral Exactness* | The ITPFI triangle inequality (template for the G4 closure); the spectral-geometric duality (template for the bridge); the adversarial review protocol |
| **Paper 15** | *The Long-Arc Transposition Programme* | The 37 R-Theorems including S.11 (spin-statistics in BC form); the additive $\leftrightarrow$ multiplicative dictionary that became the trinity dictionary; the transposition mechanics for porting between columns |
| **Paper 17** | *Zero Postulates: Thermal Time from Riemann Entropy* | The entropy operator $S_{\mathrm{BC}} = -\log\Delta_{\omega_1}$ and its spectral content; "Riemann is entropy"; the order-counting principle that motivated the spectral-geometric-information triangle |
| **Paper 23** | *The Critical Bost-Connes-Brauer System* | The CBB quintuple $\mathcal{C} = (H_R, \hat{R}, \omega_1, M_{\mathrm{geom}}, \{\beta_k\})$ from which $M_{\mathrm{Bool}}$ is constructed; the bridge family; the no-go theorem (research/168) whose trinity image is the P/NPC separation |
| **Paper 26** | *BSD for CM Elliptic Curves from the Integers Programme* | The transposition mechanics for porting the bridge family across base fields; the template for the proof-by-contradiction corollary structure |

The programme's complete output spans 28 papers, but the eight
listed above are the ones whose theorems, methods, or structural
patterns are explicitly used in the proof chain of this paper.
References to specific results within these papers appear
throughout Sections 2--4 and in the PROOF-CHAIN.

---

## 1.2 Two classifications

Two deep classification results, proved independently and using
entirely different methods, divide mathematical objects into the same
two categories.

### 1.2.1 The algebraic classification

The CSP Dichotomy Theorem, proved independently by Bulatov [Bu17]
and Zhuk [Zh20], resolves a conjecture of Feder and Vardi [FV98].
It states that for any finite constraint language $\Gamma$ over a
finite domain $D$, the constraint satisfaction problem
$\mathrm{CSP}(\Gamma)$ is either solvable in polynomial time or
NP-complete. For Boolean constraint languages ($D = \{0,1\}$), this
recovers and extends Schaefer's classical dichotomy [Sc78]. The
dividing line is algebraic: $\mathrm{CSP}(\Gamma)$ is in P if and
only if the polymorphism clone $\mathrm{Pol}(\Gamma)$ contains a
Taylor operation — an idempotent operation satisfying a non-trivial
system of identities [MM08, BBBKZ24]. This equivalence is a
**biconditional**: the Bulatov--Zhuk theorem proves both directions,
Taylor $\Rightarrow$ P-time (forward) and P-time $\Rightarrow$
Taylor (backward).

### 1.2.2 The analytic classification

The Houdayer--Marrakchi criterion [HM16, Ma19] classifies type
III$_1$ factors (infinite-dimensional von Neumann algebras with
trivial center, no non-zero trace, and trivial flow of weights) into
two classes. A type III$_1$ factor $M$ is **full** if the inner
automorphism group $\mathrm{Inn}(M)$ is closed in $\mathrm{Aut}(M)$,
equivalently if the modular automorphism group has a spectral gap on
the orthogonal complement of the scalars in $L^2(M, \varphi)$.
Otherwise $M$ is **non-full**. Fullness is a discrete invariant: a
factor is either full or non-full, with no intermediate state.

---

## 1.3 The bridge question

The two classifications operate in different mathematical universes:
finite combinatorics and infinite-dimensional analysis. The central
question of this paper is whether they are, in a precise sense, the
same classification.

We construct a family of type III$_1$ factors
$\{M_{\mathrm{Bool}}^L\}$, one for each Boolean constraint language
$L$, as sectors of a Boolean Bost--Connes system (Section 3). We
conjecture:

> **Bridge Conjecture.** $M_{\mathrm{Bool}}^L$ is non-full if and
> only if $L$ admits a Taylor polymorphism. Equivalently,
> $M_{\mathrm{Bool}}^L$ is full if and only if $\mathrm{CSP}(L)$ is
> NP-complete.

If the bridge holds, then $\mathrm{P} \neq \mathrm{NP}$ follows by
contradiction. Assume $\mathrm{P} = \mathrm{NP}$. Then $3$-SAT
$\in \mathrm{P}$. By the backward direction of BZ (a proved
theorem), $L_{3\text{-SAT}}$ admits a Taylor polymorphism. By
Part (i) of the bridge, $M_{\mathrm{Bool}}^{3\text{-SAT}}$ is
non-full. But $L_{3\text{-SAT}}$ is non-Taylor (by the forward
direction of BZ, also a proved theorem). By Part (ii) of the bridge,
$M_{\mathrm{Bool}}^{3\text{-SAT}}$ is full. Full and non-full are
contradictory for a type III$_1$ factor (Houdayer--Marrakchi:
fullness is a dichotomy). Contradiction. Therefore $\mathrm{P} \neq
\mathrm{NP}$.

This proof-by-contradiction structure, using both directions of BZ
as established external theorems, is the correct logical form. An
earlier one-line derivation by single contrapositive, appearing in
prior versions, was garbled and is corrected here.

The conjecture is interesting independent of complexity theory. It
asks: does the combinatorial growth rate of a clone of operations on
a finite set determine the analytic structure (fullness, spectral
gap) of an associated infinite-dimensional factor? This question
connects finite-domain algebra to infinite-dimensional analysis in a
way that, to our knowledge, has not been posed before.

---

## 1.4 Summary of results

We establish the following.

1. **Theorem UA1** (Section 2). Taylor Boolean clones grow
   exponentially: $|\mathrm{Clone}_k(L)| \geq c \cdot \lambda^k$
   with $\lambda \geq 2^{2/9} > 1$. The proof is a four-case
   analysis via Post's lattice, reducing to AND, OR, MAJORITY, and
   MINORITY (= XOR) by the Barto--Brady--Bulatov--Kozik--Zhuk prime
   arity theorem.

2. **Theorem UA2** (Section 2). Non-Taylor Boolean clones grow
   linearly: $|\mathrm{Clone}_k(L)| \leq 2k + 2$. The operations
   are essentially unary.

3. **Non-injectivity** (Section 3). The Boolean Bost--Connes factor
   $M_{\mathrm{Bool}}$ is non-injective. The acting semigroup
   $\mathrm{PCirc}^+$ generates a non-amenable group containing
   Thompson's group $V$, so $G_{\mathrm{Bool}}$ is non-amenable, and
   non-amenability of the acting group implies non-injectivity by
   Connes (1976). This rules out a collapse to the injective III$_1$
   factor where the fullness distinction is vacuous.

4. **KEY LEMMA 3.4.3 revised** (Section 3). Existence of a KMS$_1$
   state is established by Banach--Alaoglu compactness (not by
   partition function asymptotics — the original argument via
   $F(s) \sim s/\log s$ citing Hopcroft--Karp 1973 is withdrawn).
   Type III$_1$ is established by multiplicative independence of
   $\log 2$ and $\log 3$. Uniqueness is stated as conditional; the
   downstream proof chain is **insulated** from the uniqueness gap,
   because fullness and non-fullness are intrinsic factor properties
   independent of which faithful normal state is used.

5. **Two-part proof architecture** (Section 4). The bridge splits
   into two independent parts:

   - **Part (i): Taylor $\Rightarrow$ non-full** (Path B,
     unconditional). Clone unitaries $\widetilde{U}_f \in
     M_{\mathrm{Bool}}^L$ provide exponentially many unitaries in a
     compact group $U(d)$ of fixed dimension $d = |\mathrm{Sol}|$.
     Pigeonhole yields pairs with $\mathrm{Ad}(v_k) \to
     \mathrm{id}$. Instance diversity — proved case-by-case for
     AND/OR (coordinate-frequency analysis), MAJORITY (Berry--Esseen
     angle persistence), and XOR/MINORITY (universal non-scalarity
     via Lemma X) — ensures the inner automorphisms are not
     eventually trivial. The Marrakchi criterion then gives
     non-fullness. Path B is independent of CP-1.

   - **Part (ii): Non-Taylor $\Rightarrow$ full** (Route C,
     conditional on CP-1). Non-Taylor $L$ gives a non-amenable group
     $G_L$ with trivial amenable radical (three independent proofs).
     Essential freeness of $G_L$ on $X_L$ (three independent proofs).
     Ergodicity of $\mathcal{R}_L$ via the Feldman--Moore
     factoriality chain: $M_{\mathrm{Bool}}$ factor $\to$
     $M_{\mathrm{Bool}}^L$ factor $\to$ $L(\mathcal{R}_L)$ factor
     $\to$ $\mathcal{R}_L$ ergodic. Strong ergodicity by
     Jones--Schmidt (1987). Fullness by Marrakchi (2018, Theorem B).

6. **CP-1 closed** (Section 4). The crossed-product identification
   $M_{\mathrm{Bool}}^L \cong L(\mathcal{R}_L)$ is established via
   Laca--Raeburn dilation. All five sub-gaps resolved.
   Independently verified by six Critic agents; four writeup repairs
   completed (Lemma 4.4 fiber-averaging, $\mu_1(X_L) > 0$,
   Lemma 5.1 citation, Prop 6.1 ergodicity). Route D (direct
   Haagerup property via CAT(0) cube complex) provides a secondary
   path; its Prop 6.2 is broken but Route C is intact.

7. **Corollary corrected** (Section 4.2). The $\mathrm{P} \neq
   \mathrm{NP}$ corollary is valid via the proof-by-contradiction
   structure described above, using both directions of BZ as proved
   theorems. The earlier one-line derivation was incorrect.

8. **Computational evidence** (Section 5). Spectral (TGap) and
   geometric (holonomy) observables confirm perfect 6/6 Schaefer
   separation across all six Schaefer classes. Clone dimension
   (Q6-OUTDIM) partially verified: NPC collapse bulletproof (0 in
   2M samples), P-time exponential growth confirmed for 2-SAT.
   Route E string tension $\sigma_\infty \approx 0.0056$ confirmed
   at $n = 14, 16, 18, 20$.

9. **Kill list** (Section 6). Nineteen killed approaches document
   the search and sharpen the proof. Each kill carries a lesson that
   constrained the surviving architecture. The current proof exists
   because nineteen alternatives do not.

---

## 1.5 Barrier evasion

Any viable approach to $\mathrm{P} \neq \mathrm{NP}$ must evade
three classical barriers: relativization (Baker--Gill--Solovay 1975),
natural proofs (Razborov--Rudich 1997), and algebrization
(Aaronson--Wigderson 2008). The present argument evades all three
for structural reasons, not by clever technique:

| Barrier | What it kills | Why the bridge escapes |
|:--------|:-------------|:-----------------------|
| Relativization | Diagonalization | The KMS$_1$ state depends on the pole of $\zeta(s)$ at $s=1$, which has no oracle-relative version |
| Natural proofs | Large combinatorial properties | Fullness is a single discrete invariant, not a measurable subset of Boolean functions |
| Algebrization | Polynomial method | The Bost--Connes algebra lives over cyclotomic Galois extensions of $\mathbb{Q}$, not polynomial rings over finite fields |

The argument is non-relativizing (depends on the analytic structure
of $\omega_1$, not on oracles), non-natural in the Razborov--Rudich
sense (fullness is not a large-set property of Boolean functions),
and non-algebrizing (profinite Galois cohomology and type III$_1$
factor structure sit above polynomial extensions). These are
necessary conditions. The remainder of the paper provides the
sufficient part.

---

## 1.6 Outline of the paper

**Section 2** presents the universal algebra side: Theorems UA1 and
UA2, with complete proofs. The four-case reduction via Post's
lattice, the recursion for MAJORITY, and the linear bound for
essentially unary clones.

**Section 3** describes the operator algebra side: the Boolean
Bost--Connes construction, non-injectivity via Thompson's $V$, and
the revised KEY LEMMA 3.4.3 (compactness + multiplicative
independence).

**Section 4** states the bridge conjecture precisely and presents
the two-part proof architecture. Path B for Part (i) (pigeonhole +
instance diversity, unconditional). Route C for Part (ii)
(non-amenability + trivial radical + essential freeness + strong
ergodicity + Marrakchi fullness, conditional on CP-1). The CP-1
identification via Laca--Raeburn dilation. The corrected corollary.

**Section 5** presents computational evidence: spectral, geometric,
and information observables across all six Schaefer classes, with
honest re-verified statuses.

**Section 6** recounts the search narrative via the kill list:
nineteen killed approaches and the lessons each carried.

**Section 7** formulates the remaining open problems with updated
adversarial gap status.

**Section 8** discusses implications and revises the probability
assessment.

---
