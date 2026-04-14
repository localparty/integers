# Sato-Tate Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Sato%E2%80%93Tate_conjecture
- **Canonical resolution paper:**
  Barnet-Lamb, T., Geraghty, D., Harris, M., Taylor, R. (2011). "A family of Calabi–Yau varieties and potential automorphy II." *Publications of the Research Institute for Mathematical Sciences (PRIMS)* 47(1), 29–98.
- **Earlier (conditional):**
  Clozel, L., Harris, M., Shepherd-Barron, N., Taylor, R. (2008). "A family of Calabi-Yau varieties and potential automorphy." *Publ. Math. IHES* 108, 1–181.
- **AWS lecture notes:** Sutherland, A. V. (2016). Arizona Winter School: https://swc-math.github.io/aws/2016/2016SutherlandOutline.pdf

## 2. Problem statement

**Classical Sato-Tate Conjecture (for elliptic curves over ℚ without CM):**

Let E/ℚ be an elliptic curve without complex multiplication. For each prime p of good reduction, let a_p = p + 1 − #E(F_p). Write a_p = 2√p · cos(θ_p) with θ_p ∈ [0, π]. Then as p ranges over primes of good reduction,

> The angles {θ_p} are equidistributed in [0, π] with respect to the Sato-Tate measure (2/π) sin²θ dθ.

Equivalently: for any 0 ≤ α < β ≤ π,
(#{ p ≤ x : good reduction, θ_p ∈ [α, β] }) / (#{ p ≤ x : good reduction })  →  (2/π) ∫_α^β sin²θ dθ  as x → ∞.

**Generalized Sato-Tate (for automorphic / motivic L-functions):** analogous equidistribution with respect to the Haar measure of a specific compact Sato-Tate group.

## 3. Prize

**None.** No monetary prize. Conjecture proven in principal cases (2011, Barnet-Lamb et al.); generalizations remain open but no prize attaches.

## 4. Publication expectation

Expected journals (based on where proven cases published):

- **Publications Mathématiques de l'IHES** — Clozel-Harris-Shepherd-Barron-Taylor (2008) published here.
- **Publications of the RIMS (PRIMS)** — Barnet-Lamb-Geraghty-Harris-Taylor (2011) published here.
- **Annals of Mathematics** — Harris-Taylor (*The geometry and cohomology of some simple Shimura varieties*, 2001, *Annals of Math. Studies* 151 – Princeton UP).
- **Inventiones Mathematicae** — subsequent generalizations.
- **Acta Mathematica**
- **JAMS**
- **Duke Mathematical Journal**
- **Compositio Mathematica**

For open cases (higher genus, other fields):
- any top-tier journal depending on the generalization targeted.

## 5. Formulation variants

- **Classical (EC over ℚ, non-CM):** proven, Barnet-Lamb-Geraghty-Harris-Taylor (2011).
- **EC over totally real number fields, non-CM:** proven, Clozel-Harris-Shepherd-Barron-Taylor (2008) and follow-ups.
- **Modular forms (weight ≥ 2, non-CM):** proven (BGHT 2011 for weight k ≥ 2, level N).
- **CM elliptic curves:** the distribution is different (splits into two components for primes split / inert in the CM field); proven via Hecke characters (classical).
- **Generalized Sato-Tate (Serre's conjecture 1968):** for L-functions of motives; the conjectural Sato-Tate group determines the distribution.
- **Higher genus curves, abelian varieties:** genus 2, 3, ... — OPEN in generality. Fité-Kedlaya-Rotger-Sutherland (2012) classified all 52 possible Sato-Tate groups for genus 2.
- **Maass forms / general GL(n) automorphic forms:** Langlands functoriality predicts generalized Sato-Tate; proven in some cases via potential automorphy.
- **Over function fields (F_q(t)):** Deligne equidistribution theorem for monodromy; gives function-field Sato-Tate unconditionally.
- **Effective Sato-Tate:** error terms in the equidistribution rate; largely OPEN.

## 6. Known partial results + named walls

**Proven (classical case):**
- **Elliptic curves over ℚ, non-CM:** Barnet-Lamb, Geraghty, Harris, Taylor (2011, *PRIMS*).
- **Elliptic curves over totally real fields with some multiplicative reduction:** Clozel, Harris, Shepherd-Barron, Taylor (2008, *Publ. IHES*).
- **Hilbert modular forms:** Barnet-Lamb, Gee, Geraghty (2011) and related.
- **Holomorphic modular forms of weight ≥ 2, non-CM:** Barnet-Lamb-Geraghty-Harris-Taylor (2011).
- **Function-field analog:** Deligne (1980); equidistribution of Frobenius for monodromy groups.
- **Effective Sato-Tate (conditional on GRH and other hypotheses):** Murty-Murty, Bucur-Kedlaya, Thorner-Zaman.

**Named walls:**
- *Potential automorphy wall* — Taylor's potential automorphy techniques (2008, 2011) required CM Calabi-Yau varieties as crutch; higher-dimensional generalizations need new automorphy input.
- *CM vs non-CM distinction* — CM cases are "easier" (Hecke characters); non-CM needs automorphy.
- *Higher genus wall* — classifying the 52 Sato-Tate groups for genus 2 was Fité-Kedlaya-Rotger-Sutherland (2012); proving Sato-Tate for any of the generic ones remains hard.
- *Effective / rate-of-convergence wall* — unconditional effective Sato-Tate (explicit error bounds) is very limited.
- *Over general number fields* — extending from totally real to mixed signature fields requires strengthened automorphy results.
- *Langlands functoriality wall* — generalized Sato-Tate for GL(n), n ≥ 3 requires functoriality (Langlands program); mostly open.

## 7. Key references

**Original:**
- Sato, M. (c. 1960). Unpublished observation.
- Tate, J. T. (1965). "Algebraic cycles and poles of zeta functions." *Arithmetical Algebraic Geometry* (Harper & Row), 93–110.
- Serre, J.-P. (1968). *Abelian l-adic Representations and Elliptic Curves*. Benjamin.

**Proof (2008 + 2011):**
- Clozel, L., Harris, M., Shepherd-Barron, N., Taylor, R. (2008). "A family of Calabi-Yau varieties and potential automorphy." *Publ. Math. IHES* 108, 1–181.
- Harris, M., Shepherd-Barron, N., Taylor, R. (2010). "A family of Calabi-Yau varieties and potential automorphy I." *Annals of Math.* 171, 779–813.
- Barnet-Lamb, T., Geraghty, D., Harris, M., Taylor, R. (2011). "A family of Calabi-Yau varieties and potential automorphy II." *PRIMS* 47(1), 29–98.
- Taylor, R. (2008). "Automorphy for some l-adic lifts of automorphic mod l Galois representations. II." *Publ. Math. IHES* 108, 183–239.

**Best modern surveys:**
- Sutherland, A. V. (2016). "Sato-Tate distributions." AWS lecture notes.
- Fité, F., Kedlaya, K. S., Rotger, V., Sutherland, A. V. (2012). "Sato-Tate distributions and Galois endomorphism modules in genus 2." *Compos. Math.* 148, 1390–1442.
- Murty, V. K. (2013). *Sato-Tate Theorems*. (Various lecture notes.)

## Status: PROVEN for elliptic curves over totally real fields (2011); generalizations OPEN. No prize. Target journal: Publ. IHES / PRIMS / Annals / Inventiones.
