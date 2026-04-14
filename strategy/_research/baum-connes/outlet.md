# Baum-Connes Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Baum-Connes_conjecture
- **nLab:** https://ncatlab.org/nlab/show/Baum-Connes+conjecture
- **Original formulation:** Baum, P. & Connes, A. (1982). Unpublished preprint, Institut des Hautes Études Scientifiques. Later published as: Baum, P., Connes, A., Higson, N. (1994). "Classifying space for proper actions and K-theory of group C*-algebras." *Contemp. Math.* 167 (AMS), 240–291.
- **Canonical monograph:** Mislin, G. & Valette, A. (2003). *Proper Group Actions and the Baum-Connes Conjecture*. Birkhäuser Advanced Courses in Math.
- **Survey:** Valette, A. (2002). *Introduction to the Baum-Connes Conjecture*. Birkhäuser.

## 2. Problem statement

**Modern form:** Let G be a locally compact, second-countable, Hausdorff topological group (or groupoid). Define the assembly map
μ_r : K^G_*(EG) → K_*(C*_r(G))
where EG is the classifying space for proper G-actions, K^G_* is equivariant K-homology with G-compact supports, and K_*(C*_r(G)) is the topological K-theory of the reduced group C*-algebra.

**Conjecture:** μ_r is an isomorphism.

**Coefficients version:** For a G-C*-algebra A, the assembly map
μ_{r,A} : K^G_*(EG; A) → K_*(A ⋊_r G)
is an isomorphism. — This stronger version is FALSE in general (Higson-Lafforgue-Skandalis 2002 counterexample).

## 3. Prize

**None.** No monetary prize; no foundation page. Purely mathematical research conjecture.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics**
- **Inventiones Mathematicae** — Lafforgue's Banach KK-theory work appeared here.
- **Publications Mathématiques de l'IHES**
- **Acta Mathematica**
- **Journal of the AMS**
- **Geometric and Functional Analysis (GAFA)** — Higson-Lafforgue-Skandalis 2002 counterexample published here.
- **Duke Mathematical Journal**
- **Journal of Functional Analysis**
- **Journal für die reine und angewandte Mathematik (Crelle)**
- **K-Theory** (now *Journal of K-Theory* / *Annals of K-Theory*)
- **Compositio Mathematica**

Operator algebras specialized:
- *Journal of Operator Theory*
- *Journal of Noncommutative Geometry*
- *Advances in Mathematics*

## 5. Formulation variants

- **Standard Baum-Connes (BC):** μ_r isomorphism for G.
- **BC with coefficients (BC^A):** μ_{r,A} isomorphism for all G-C*-algebras A.
  - **FALSE** (Higson-Lafforgue-Skandalis, 2002, *GAFA*).
- **Strong Novikov conjecture:** injectivity of μ_r — implied by BC and is open itself for some groups.
- **Coarse Baum-Connes conjecture:** asymptotic/coarse-geometric version; FALSE for expanders (Higson, others).
- **Groupoid Baum-Connes:** for locally compact groupoids; FALSE for certain HLS groupoids.
- **Farrell-Jones conjecture:** algebraic K- and L-theory analogs; related but distinct.
- **Bost conjecture:** version with the unconditional / Banach algebra L¹(G); implies BC and has wider known cases (Lafforgue).

## 6. Known partial results + named walls

**Proven for (classical BC, standard form):**
- A-T-menable groups / Haagerup property (Higson-Kasparov 2001, *Inventiones*).
- Amenable groups (special case of above).
- Gromov-hyperbolic groups (Lafforgue 2012, *J. Noncommut. Geom.*).
- Discrete subgroups of SO(n,1) and SU(n,1).
- Cocompact lattices in SL(3,K) for K = ℝ, ℂ, ℚ_p (Lafforgue).
- One-relator groups.
- Groups acting properly on CAT(0) cubical complexes (Schick, Oyono-Oyono).
- All linear groups (injectivity, Guentner-Higson-Weinberger).

**Counterexamples (with coefficients):**
- Higson, N., Lafforgue, V., Skandalis, G. (2002). "Counterexamples to the Baum-Connes conjecture." *GAFA* 12, 330–354. Uses Gromov's expanders.

**Open for (classical BC):**
- SL_n(ℤ) for n ≥ 3 — simplest unresolved case.
- Property (T) groups in general (not known to be open across the board; some cases resolved).
- Random groups with property (T).

**Named walls:**
- *Property (T) wall* — Kazhdan's property (T) groups are where the classical strategies (Dirac-dual Dirac, γ-element) fail.
- *Gromov monster wall* — expander-containing random groups yield counterexamples for coefficients version.
- *Exactness wall* — non-exact groups were the source of HLS counterexamples; exactness is ubiquitous but not universal.
- *Lafforgue's Banach KK-theory wall* — needed to handle hyperbolic groups; further extension to property (T) is open.

## 7. Key references

**Original statement:**
- Baum, P. & Connes, A. (1982). Unpublished.
- Baum, P., Connes, A., Higson, N. (1994). "Classifying space for proper actions and K-theory of group C*-algebras." *Contemp. Math.* 167, 240–291.

**Best modern surveys:**
- Mislin, G. & Valette, A. (2003). *Proper Group Actions and the Baum-Connes Conjecture*. Birkhäuser.
- Valette, A. (2002). *Introduction to the Baum-Connes Conjecture*. Birkhäuser.
- Aparicio, M. P., Julg, P., Valette, A. (2019). "The Baum-Connes conjecture: an extended survey." *Advances in Noncommutative Geometry* (Springer), 127–244.
- Higson, N. & Roe, J. (2000). *Analytic K-Homology*. Oxford.

**Key results:**
- Higson, N. & Kasparov, G. (2001). "E-theory and KK-theory for groups which act properly and isometrically on Hilbert space." *Inventiones* 144, 23–74.
- Lafforgue, V. (2002). "K-théorie bivariante pour les algèbres de Banach et conjecture de Baum-Connes." *Inventiones* 149, 1–95.
- Higson, Lafforgue, Skandalis (2002). *GAFA* 12, 330–354.

## Status: OPEN (classical form); FALSE with coefficients (2002). No prize. Target journal: Annals / Inventiones / GAFA.
