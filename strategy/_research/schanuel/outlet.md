# Schanuel's Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Schanuel%27s_conjecture
- **MathWorld:** https://mathworld.wolfram.com/SchanuelsConjecture.html
- **First public formulation:** Lang, S. (1966). *Introduction to Transcendental Numbers*. Addison-Wesley, p. 30. (Lang attributes to Schanuel 1960s private communication.)
- **Modern survey:** Waldschmidt, M. Schanuel's Conjecture page: https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/SchanuelEn.pdf

## 2. Problem statement

**Schanuel's Conjecture:**
> Given any complex numbers z_1, ..., z_n that are linearly independent over ℚ, the field ℚ(z_1, ..., z_n, e^{z_1}, ..., e^{z_n}) has transcendence degree at least n over ℚ.

**Equivalent formulation:** For linearly-independent-over-ℚ z_1, ..., z_n,
trdeg_ℚ( ℚ(z_1, ..., z_n, exp(z_1), ..., exp(z_n)) ) ≥ n.

**Real version:** if x_1, ..., x_n ∈ ℝ and trdeg_ℚ( ℚ(x_1, ..., x_n, exp(x_1), ..., exp(x_n)) ) < n, then there exist rationals q_1, ..., q_n, not all zero, with q_1 x_1 + ... + q_n x_n = 0.

## 3. Prize

**None.** No monetary prize. Core transcendence-theory conjecture without foundation backing.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics**
- **Inventiones Mathematicae**
- **JAMS**
- **Acta Mathematica**
- **Publications Mathématiques de l'IHES**
- **Duke Mathematical Journal**
- **Compositio Mathematica**
- **Journal of Number Theory**
- **Mathematische Annalen**
- **Acta Arithmetica**
- **Ann. Sci. ENS**
- **Journal of Algebra**
- **Journal of Symbolic Logic** — for model-theoretic approaches (Zilber).

## 5. Formulation variants

- **Standard (Lang 1966, complex version):** as stated.
- **Real Schanuel:** for real numbers.
- **Formal power series / Ax-Schanuel (proven, Ax 1971):** the formal power series / function field analog. Proved by James Ax.
- **Differential Schanuel (proven in specific contexts):** via differential algebra.
- **p-adic Schanuel:** analog over p-adic fields; proven in special cases.
- **Zilber's exponential-algebraic closure conjecture:** predicts algebraic-closedness properties for (ℂ, exp); implies Schanuel.
- **Quasi-minimality of ℂ_exp (Zilber 2005):** open; would follow from strengthened Schanuel.
- **Generalized Schanuel (for automorphic functions):** e.g., for modular forms, theta functions.
- **Schanuel's conjecture for ∞-exponentiation (power towers):** see MDPI paper by Bajo-Rojas (2021).

## 6. Known partial results + named walls

**Proven:**
- **Lindemann (1882):** π is transcendental; special case n=1 of Schanuel.
- **Lindemann-Weierstrass (1885):** if α_1, ..., α_n are algebraic and linearly independent over ℚ, then e^{α_1}, ..., e^{α_n} are algebraically independent over ℚ. Special case (n=1 version with algebraic numbers).
- **Gelfond-Schneider (1934):** α^β transcendental for α algebraic ≠ 0,1 and β algebraic irrational.
- **Hilbert's 7th (Gelfond-Schneider):** as above.
- **Baker (1966):** if α_1, ..., α_n algebraic ≠ 0, 1 and log α_1, ..., log α_n linearly independent over ℚ, then 1, log α_1, ..., log α_n are linearly independent over the algebraic closure of ℚ. Consequences for transcendence.
- **Ax-Schanuel (James Ax 1971):** Schanuel's conjecture for formal power series (proven). Differential-field analog.
- **Nesterenko (1996):** algebraic independence of π, e^π, and Γ(1/4). Deep but very narrow case.
- **Ribet, Moser, etc.:** various isolated transcendence results that are implied by Schanuel.

**Named walls:**
- *The "e + π" wall* — we don't know whether e + π is transcendental. Schanuel would imply yes.
- *The "e^e" wall* — we don't know whether e^e is transcendental. Schanuel would imply yes.
- *The "1, e, π" wall* — we don't know whether 1, e, π are ℚ-linearly independent. Schanuel would imply yes.
- *No generic algebraic independence technique* — transcendence theory proves specific cases; no machinery for the full conjecture exists.
- *Beyond GL_n Langlands wall* — Schanuel involves exp, which is connected to GL_1; extensions to higher automorphic forms touch full Langlands.
- *Zilber gap* — Zilber's model-theoretic reformulation (pseudo-exponentiation) gives an alternative approach, but bridging it to Schanuel in ℂ is itself a conjecture.

## 7. Key references

**Original:**
- Lang, S. (1966). *Introduction to Transcendental Numbers*. Addison-Wesley. (first public appearance of Schanuel's conjecture in print, attributed to Stephen Schanuel.)

**Best modern surveys:**
- Waldschmidt, M. (2000). *Diophantine Approximation on Linear Algebraic Groups*. Grundlehren 326, Springer. — comprehensive reference; Schanuel in Chapter 1.
- Waldschmidt, M. (2021+). "Schanuel's Conjecture: algebraic independence of transcendental numbers." Lecture notes and survey articles.
- Murty, M. R. & Rath, P. (2014). *Transcendental Numbers*. Springer.
- Marker, D. (2006). "A remark on Zilber's pseudoexponentiation." *J. Symb. Logic* 71, 791–798.

**Key proven partial results:**
- Ax, J. (1971). "On Schanuel's conjectures." *Annals of Math.* 93, 252–268. — formal power series / differential case.
- Nesterenko, Y. (1996). "Modular functions and transcendence questions." *Mat. Sb.* 187, 65–96.

**Model-theoretic reformulation:**
- Zilber, B. (2005). "Pseudo-exponentiation on algebraically closed fields of characteristic zero." *Ann. Pure Appl. Logic* 132, 67–95.

## Status: OPEN. No prize. Target journal: Annals / Inventiones / Duke.
