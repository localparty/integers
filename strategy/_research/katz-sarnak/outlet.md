# Katz-Sarnak Philosophy / Density Conjecture — Outlet Report

## 1. Official outlet

- **Canonical monograph:** Katz, N. M. & Sarnak, P. (1999). *Random Matrices, Frobenius Eigenvalues, and Monodromy*. AMS Colloquium Publications 45, Providence, RI.
- **Survey article:** Katz, N. M. & Sarnak, P. (1999). "Zeroes of zeta functions and symmetry." *Bulletin of the AMS* 36, 1–26. https://www.ams.org/journals/bull/1999-36-01/S0273-0979-99-00766-1/
- **Iwaniec-Luo-Sarnak foundational paper:** Iwaniec, H., Luo, W., Sarnak, P. (2000). "Low lying zeros of families of L-functions." *Publ. Math. IHES* 91, 55–131.
- **Wikipedia (stub / linked via L-function pages):** limited — no dedicated Wikipedia page. See: https://en.wikipedia.org/wiki/Random_matrix#Connections_to_number_theory

## 2. Problem statement

**Katz-Sarnak Density Conjecture:**

> Let F = (f_n) be a "natural" family of automorphic L-functions L(s, f_n) with conductors c_n → ∞. As n → ∞, the distribution of the normalized low-lying zeros (zeros near s = 1/2 after rescaling by log c_n / (2π)) of L(s, f_n) converges to the 1-level density (and more generally, n-level correlation) of eigenangles near 1 of random matrices drawn from one of the classical compact groups G(N) ∈ {U(N), O(N), Sp(2N), SO(even)(N), SO(odd)(N)}.

The classical compact group G(F) attached to the family F is its **symmetry type**:
- **Unitary (U)** — generic families (e.g., Dirichlet L-functions with varying character).
- **Symplectic (Sp)** — quadratic Dirichlet L-functions, or L(s, sym² f).
- **Orthogonal (O, SO_even, SO_odd)** — elliptic curve L-functions parameterized by twists; split by root-number sign.

**Specific quantitative form (1-level density):** for a nice even test function φ whose Fourier transform is compactly supported,

∑_{f ∈ F(x)} ∑_γ φ( γ · log(c_f)/(2π) )   /   |F(x)|   →   ∫ φ(x) W_G(x) dx

as x → ∞, where W_G is the 1-level density of eigenangles near 1 for the compact group G = G(F).

## 3. Prize

**None.** No monetary prize. Research-community conjecture; the underlying RH is the prized problem.

## 4. Publication expectation

Expected journals in descending prestige:

- **Publications Mathématiques de l'IHES** — Iwaniec-Luo-Sarnak 2000 published here.
- **Annals of Mathematics**
- **Inventiones Mathematicae**
- **Acta Mathematica**
- **JAMS**
- **Duke Mathematical Journal**
- **Compositio Mathematica**
- **American Journal of Mathematics**
- **Forum of Mathematics, Sigma / Pi**
- **Journal of Number Theory**

Specialty:
- *International Mathematics Research Notices (IMRN)*
- *Mathematische Annalen*
- *Ann. Inst. Fourier*
- *Trans. AMS*

## 5. Formulation variants

- **1-level density (Iwaniec-Luo-Sarnak):** statistics of single zeros near s = 1/2.
- **n-level correlation / density:** statistics of n-tuples of zeros (Rudnick-Sarnak).
- **Family-specific:**
  - Unitary: Dirichlet L-functions, varying character (Özlük-Snyder, Hughes-Rudnick).
  - Symplectic: quadratic twists of a fixed elliptic curve / quadratic Dirichlet (Soundararajan).
  - Orthogonal: L-functions of elliptic curves ordered by conductor (Young, Miller).
- **Katz-Sarnak over function fields:** L-functions of curves over F_q; proven unconditionally in monodromy limit (q → ∞).
- **Low-lying vs global statistics:** Katz-Sarnak is about zeros near central point; Montgomery pair correlation is about typical (non-low-lying) zeros.
- **Montgomery–Odlyzko law:** special case for Riemann ζ zero spacings — GUE statistics.

## 6. Known partial results + named walls

**Proven:**
- **Function-field analog (Katz-Sarnak 1999):** for families of L-functions attached to algebraic curves over F_q, the monodromy approach (Deligne) yields the Katz-Sarnak density statement in the q → ∞ limit (or equivalently averaging over q).
- **1-level density for Dirichlet L-functions (Özlük 1994, Hughes-Rudnick 2003):** proven for test functions of restricted Fourier support (up to support [-2, 2]).
- **Iwaniec-Luo-Sarnak (2000):** 1-level density for families of automorphic L-functions of GL(2), restricted Fourier support.
- **Various extensions:** Hecke L-functions, Maass forms, symmetric powers.

**Named walls:**
- *Fourier support wall* — all unconditional results are limited to test functions with Fourier transform in (-α, α) for some α depending on family. Extending α is a major problem; the conjecture asserts all test functions.
- *GRH wall* — full Katz-Sarnak assumes GRH for the family; unconditional results typically work within GRH + other hypotheses.
- *Automorphy wall* — for families of elliptic curves over ℚ, automorphy is now known (post-modularity theorem), but for arbitrary motivic L-functions it remains open (Langlands).
- *Explicit formula wall* — all arguments use explicit formula (Weil); extending to families without clean explicit formulas requires new machinery.

## 7. Key references

**Original:**
- Katz, N. M. & Sarnak, P. (1999). *Random Matrices, Frobenius Eigenvalues, and Monodromy*. AMS Colloq. Publ. 45. — canonical monograph.
- Katz, N. M. & Sarnak, P. (1999). "Zeroes of zeta functions and symmetry." *Bull. AMS* 36, 1–26. — accessible survey.

**Foundational quantitative work:**
- Iwaniec, H., Luo, W., Sarnak, P. (2000). "Low lying zeros of families of L-functions." *Publ. Math. IHES* 91, 55–131.

**Best modern surveys:**
- Conrey, J. B. (2005). "Notes on L-functions and random matrix theory." AIM preprint.
- Miller, S. J. (2005–present). Series of papers on 1-level and n-level densities for elliptic curves and modular forms.
- Sarnak, P. (2008). "Definition of families of L-functions." Lecture notes.
- Rudnick, Z. & Sarnak, P. (1996). "Zeros of principal L-functions and random matrix theory." *Duke Math. J.* 81, 269–322.

**Random matrix foundations:**
- Montgomery, H. L. (1973). "The pair correlation of zeros of the zeta function." *Proc. Symp. Pure Math.* 24 (AMS), 181–193.
- Odlyzko, A. M. (1987). "On the distribution of spacings between zeros of the zeta function." *Math. Comp.* 48, 273–308.

## Status: OPEN (philosophy/conjecture, unconditional only for function fields). No prize. Target journal: Publ. IHES / Annals / Inventiones / Duke.
