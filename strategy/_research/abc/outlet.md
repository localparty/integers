# ABC Conjecture (Oesterlé-Masser) — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/Abc_conjecture
- **Nitaj's ABC conjecture page (authoritative community aggregator):** https://nitaj.users.lmno.cnrs.fr/abc.html
- **Original formulation:**
  - Oesterlé, J. (1988). "Nouvelles approches du 'théorème' de Fermat." *Séminaire Bourbaki* exp. 694, *Astérisque* 161–162, 165–186.
  - Masser, D. W. (1985). "Open problems." in *Proceedings of the Symposium on Analytic Number Theory*, Imperial College London.

## 2. Problem statement

**ABC Conjecture (Oesterlé-Masser, 1985/1988):**

Define the radical rad(n) = ∏_{p | n} p (product of distinct primes dividing n).

> For every ε > 0, there exist only finitely many triples (a, b, c) of coprime positive integers with a + b = c such that
> c > rad(abc)^{1 + ε}.

**Equivalent quantitative form:** For every ε > 0, there exists a constant K_ε such that for all coprime a + b = c,
c ≤ K_ε · rad(abc)^{1 + ε}.

**Refined (explicit) ABC:** conjectures about explicit constants K_ε (Baker, Stewart-Tijdeman style).

## 3. Prize

**No current monetary prize.**

Historical note: In 2019/2020, some blogs (Not Even Wrong / Lipton) speculated half-ironically about an "unclaimed million dollars" for disproving Mochizuki, but there is no formal prize foundation backing ABC. The Kyoto / RIMS community supports Mochizuki's IUT claimed proof but this is institutional, not prize-based.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics**
- **Inventiones Mathematicae** — Stewart-Yu and Stewart-Tijdeman bounds published here and similar venues.
- **Acta Mathematica**
- **Publications Mathématiques de l'IHES**
- **JAMS**
- **Duke Mathematical Journal**
- **Compositio Mathematica**
- **Journal of Number Theory**
- **Mathematische Annalen**

Note on Mochizuki: His IUT proof was published in *Publications of the RIMS* (PRIMS) 57 (2021), of which he is editor-in-chief. This publication venue choice is controversial in the mathematical community because of the conflict of interest.

## 5. Formulation variants

- **Standard (Oesterlé-Masser):** c ≤ K_ε rad(abc)^{1+ε}.
- **Explicit ABC (Baker):** c < K · rad(abc)^κ for specific K, κ > 1.
- **Szpiro's conjecture:** log |Δ(E)| ≤ C(ε) log N(E) · (6 + ε), for elliptic curves E/ℚ with minimal discriminant Δ and conductor N. Equivalent to ABC.
- **Uniform ABC (for number fields):** generalizes to arbitrary number fields.
- **Functional ABC (Mason-Stothers, proven):** the polynomial analog, proven 1981; this is the model case.
- **abc_n conjecture:** generalized to n-term sums (Browkin, Brzeziński, Gyory, etc.).
- **Ramified-prime ABC (strong forms):** give explicit K_ε bounds as functions of ε.
- **Mochizuki's IUT version:** "inequality (inj) in IUT-IV Theorem 1.10" implies explicit-constant ABC.

## 6. Known partial results + named walls

**Proven (polynomial / function-field version):**
- **Mason-Stothers theorem (1981, 1984):** polynomial ABC over algebraically closed fields. Open in number field case.
- **Absolute bounds (unconditional but weak):**
  - Stewart-Tijdeman (1986): c ≤ exp(K_1 · rad(abc)^{15}).
  - Stewart-Yu (1991, improved 2001): c ≤ exp(K_2 · rad(abc)^{1/3 + ε}) (later improved).
  - These bounds are exponential in rad, not polynomial.

**Mochizuki's claimed proof (Inter-universal Teichmüller theory, IUT):**
- 2012: arXiv preprints released.
- 2021 March: Published in *PRIMS* (RIMS), 4 papers.
- **Status: NOT accepted by mainstream mathematical community.**
- Scholze-Stix (2018): identified an unbridgeable gap in Corollary 3.12 (IUT-III). Mochizuki and RIMS disputed.
- As of 2026: controversy unresolved; mainstream experts (Scholze, Stix, Conrad, Woit, Kedlaya, Venkatesh, others) do not accept the proof.

**Numerical evidence:** ABC@Home computation found millions of triples with c/rad(abc)^{1+ε} large; no counterexample known.

**Named walls:**
- *Mochizuki IUT wall* — a purported full proof sits in mathematical limbo; the gap around Corollary 3.12 has not been publicly bridged despite 14+ years.
- *Exponential vs polynomial wall* — all non-IUT unconditional bounds are exponential in rad; moving to polynomial requires a fundamentally new idea (Vojta's conjectures in Diophantine geometry, or something equivalent).
- *Vojta-height wall* — ABC is a special case of Vojta's height inequality in Diophantine geometry; the full Vojta conjecture is deeper and also open.
- *Function-field → number-field wall* — polynomial ABC (Mason-Stothers) uses the Wronskian over a field; there's no analogous global "derivation" on ℤ, though arithmetic derivation / p-derivation attempts exist.

## 7. Key references

**Original:**
- Oesterlé, J. (1988). "Nouvelles approches du 'théorème' de Fermat." *Astérisque* 161–162.
- Masser, D. W. (1985). Problem stated at symposium; developed 1985–1988.
- Szpiro, L. (1990). Related conjecture on elliptic curve discriminants.

**Best modern surveys:**
- Nitaj, A. The ABC conjecture homepage: https://nitaj.users.lmno.cnrs.fr/abc.html
- Waldschmidt, M. (2013). "Lecture on the abc conjecture and some of its consequences." In *Mathematics in the 21st Century*, Springer.
- Scholze, P. & Stix, J. (2018). "Why abc is still a conjecture." Manuscript available at https://ncatlab.org/nlab/files/why_abc_is_still_a_conjecture.pdf

**Polynomial case:**
- Mason, R. C. (1984). *Diophantine equations over function fields*. LMS Lecture Notes 96.
- Stothers, W. W. (1981). "Polynomial identities and Hauptmoduln." *Quart. J. Math. Oxford* 32, 349–370.

**Unconditional bounds:**
- Stewart, C. L. & Tijdeman, R. (1986). "On the Oesterlé-Masser conjecture." *Monatsh. Math.* 102, 251–257.
- Stewart, C. L. & Yu, K. (2001). "On the abc conjecture, II." *Duke Math. J.* 108, 169–181.

**Mochizuki:**
- Mochizuki, S. (2021). "Inter-universal Teichmüller theory I, II, III, IV." *PRIMS* 57.

## Status: OPEN (mainstream). Mochizuki's IUT proof published 2021 but NOT accepted outside his school. No current prize. Target journal: Annals of Mathematics.
