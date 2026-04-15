# Birch and Swinnerton-Dyer Conjecture — Official Clay Problem Description

**Author:** Andrew Wiles
**Source:** https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/
**PDF:** https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf
**Saved:** 2026-04-10 (enriched with verbatim Wiles quotes)

---

## Verbatim Conjecture Statement (Wiles)

> **Conjecture (Birch and Swinnerton-Dyer).** The Taylor expansion of
> L(C, s) at s = 1 has the form
>
>     L(C, s) = c(s − 1)^r + higher order terms
>
> with c ≠ 0 and r = rank(C(Q)).
>
> In particular this conjecture asserts that L(C, 1) = 0 ⇔ C(Q) is infinite.

## The Setup (Wiles' Framing)

For an elliptic curve C : y² = x³ + ax + b with a, b ∈ Z, let Δ denote
the discriminant and set

    N_p := #{solutions of y² ≡ x³ + ax + b mod p},
    a_p := p − N_p.

The (incomplete) L-series of C is

    L(C, s) := ∏_{p ∤ 2Δ} (1 − a_p p^{−s} + p^{1−2s})^{−1}

This Euler product converges for Re(s) > 3/2. Analytic continuation
to the whole plane is now proved (consequence of the modularity
theorem — BCDT 2001, Wiles 1995, Taylor-Wiles 1995).

Mordell (1922) proved that C(Q) is finitely generated:

    C(Q) ≃ Z^r ⊕ C(Q)_tors

The integer r is called the **rank** of C. The conjecture asserts
r equals the order of vanishing of L(C, s) at s = 1.

## Refined (Strong) Form — Wiles' Remark 1

Define Euler factors at primes p | 2Δ to get the completed L-series
L*(C, s). The strong form predicts

    L*(C, s) ∼ c* (s − 1)^r   as s → 1

with

    c* = |Ш_C| · R_∞ · w_∞ · ∏_{p|2Δ} w_p / |C(Q)_tors|²

Where:

- **|Ш_C|** = the order of the Tate–Shafarevich group of C. This
  group is NOT known in general to be finite, though it is
  conjectured to be so. It counts equivalence classes of homogeneous
  spaces of C with points in all local fields. A proof of the
  conjecture in this strong form would also yield the finiteness
  of Ш_C.
- **R_∞** = the regulator, an r×r determinant whose matrix entries
  are a height pairing applied to a system of generators of
  C(Q)/C(Q)_tors.
- **w_∞** = a simple multiple of the real period of C.
- **w_p** = elementary local (Tamagawa) factors at primes of
  bad reduction.
- **|C(Q)_tors|** = order of the torsion subgroup.

Precise definitions: Tate, *On the conjectures of Birch and
Swinnerton-Dyer and a geometric analog* (Séminaire Bourbaki 306,
1965/66), or Tate, *The arithmetic of elliptic curves* (Invent.
Math. 23, 1974).

---

## Known Results (per Wiles' description + updates)

| Result | Authors | Year | Scope |
|:-------|:--------|:-----|:------|
| Mordell-Weil: C(Q) finitely generated | Mordell | 1922 | All E/Q |
| BSD conjecture stated | Birch, Swinnerton-Dyer | 1963 | — |
| CM curves, L(C,1) ≠ 0 → C(Q) finite | Coates-Wiles | 1977 | CM only |
| Faltings / Mordell: genus ≥ 2 | Faltings | 1983 | higher genus |
| Gross-Zagier formula (L'(C,1) and Heegner points) | Gross-Zagier | 1986 | Modular curves, analytic rank 1 |
| Kolyvagin Euler system (rank 0 and 1) | Kolyvagin | 1989-1990 | Modular curves |
| p-part of BSD for CM curves | Rubin | 1991 | CM, p > 7 |
| Modularity theorem (all E/Q are modular) | Wiles / Taylor-Wiles / BCDT | 1995, 2001 | All E/Q |
| Average rank bounds | Bhargava-Shankar | 2015 | Statistical |
| BSD formula at rank 1 for certain families | Jetchev-Skinner-Wan | 2017 | Specific families |

**The combined known result (Wiles' description):**

> **Theorem.** If L(C, s) ∼ c(s − 1)^m with c ≠ 0 and m = 0 or 1,
> then the conjecture holds.

This follows from Kolyvagin + Gross-Zagier + modularity.

**What remains open** (as of 2026):
- Rank ≥ 2 (both directions)
- The strong form with Ш even for rank 0, 1 (up to rational factors
  in most cases)
- Finiteness of Ш in general

**No proven cases exist for rank ≥ 2.**

---

## Related Open Problems Discussed by Wiles

- **Congruent number problem.** For n odd and square-free, n is a
  congruent number iff a specific modular-form identity holds
  (Tunnell 1983, conditional on BSD). Tunnell proved the "necessary"
  direction unconditionally using Coates-Wiles.
- **The conjecture over number fields and for abelian varieties.**
  Wiles notes the BSD conjecture extends naturally but is open.
- **Refined conjectures on special values of L-functions.** Tate,
  Lichtenbaum, Deligne, Bloch, Beilinson — connecting ranks of
  groups of algebraic cycles to orders of vanishing/poles of
  L-functions.
- **Function field analogue.** Proved by Artin-Tate that L-series has
  a zero of order at least r; the full conjecture in the function
  field case is equivalent to finiteness of Ш (Milne).

---

## What Wiles' Description Requires for a Proof

A complete proof must establish:

1. **The rank equality:** rank(C(Q)) = ord_{s=1} L(C, s), for all
   elliptic curves C over Q.
2. **The leading coefficient formula (strong form):** the precise
   value c* as described above — OR at minimum the weak form
   (rank equality).
3. **Intermediate objects well-defined:** Ш_C (including its
   finiteness), the regulator R_∞, periods w_∞, local factors w_p,
   torsion C(Q)_tors must all be well-defined and correctly
   computed.
4. **Unconditional:** not assuming GRH for other L-functions, not
   assuming finiteness of Ш_C a priori for the strong form.
5. **Effective algorithm for rank?** Wiles notes that a proof in the
   stronger form would give an effective means of finding generators
   for the group of rational points — a practical consequence.

**Scope note:** Wiles' description speaks of "an elliptic curve E
over Q". The conjecture as stated is for **all** elliptic curves
over Q, not for a sub-family. A paper covering only CM curves or
only rank 0+1 covers a **proper subset** of the conjecture.

---

## What Constitutes a Proof (Clay rules § 5)

Per Clay §5(a): "Only a complete mathematical solution ... will be
eligible." Per §5(d): "Paper must address the specific mathematical
questions in the official description — even closely related
questions don't count."

Per §5(c)(ii): A partial result (e.g., proving BSD only for CM curves
of low rank) would NOT qualify for the full prize, but may receive
a small prize from other CMI funds if it "effectively resolves" the
Problem — a determination at CMI's sole discretion.

The referee's job is to determine whether a claimed proof:
(a) addresses the **full** BSD conjecture as stated, or
(b) addresses only a **special case**, in which case the partial-
    prize discussion under §5(c)(ii) applies.

---

## References

- Wiles, A. "The Birch and Swinnerton-Dyer Conjecture." Clay
  Mathematics Institute official problem description.
  https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf
- Birch, B. J. and Swinnerton-Dyer, H. P. F. "Notes on elliptic
  curves II." J. reine u. angewandte Math. 218 (1965), 79-108.
- Mordell, L. "On the rational solutions of the indeterminate
  equations of the third and fourth degrees." Proc. Camb. Phil.
  Soc. 21 (1922), 179-192.
- Coates, J. and Wiles, A. "On the conjecture of Birch and
  Swinnerton-Dyer." Invent. Math. 39 (1977), 223-251.
- Gross, B. and Zagier, D. "Heegner points and derivatives of
  L-series." Invent. Math. 84 (1986), 225-320.
- Kolyvagin, V. "Finiteness of E(Q) and Sha(E/Q) for a class of
  Weil curves." Math. USSR Izv. 32 (1989), 523-541.
- Rubin, K. "The 'main conjectures' of Iwasawa theory for
  imaginary quadratic fields." Invent. Math. 103 (1991), 25-68.
- Wiles, A. "Modular elliptic curves and Fermat's last theorem."
  Ann. Math. 142 (1995), 443-551.
- Taylor, R. and Wiles, A. "Ring-theoretic properties of certain
  Hecke algebras." Ann. Math. 141 (1995), 553-572.
- Breuil, C., Conrad, B., Diamond, F., Taylor, R. "On the modularity
  of elliptic curves over Q: wild 3-adic exercises." J. Amer. Math.
  Soc. 14 (2001), 843-939.
- Tate, J. "The arithmetic of elliptic curves." Invent. Math. 23
  (1974), 179-206.
- Darmon, H. "Wiles' theorem and the arithmetic of elliptic curves."
  In *Modular forms and Fermat's Last Theorem*, Springer, 1997,
  549-569.

## Web Sources

- Clay Mathematics Institute: https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/
- Wikipedia: https://en.wikipedia.org/wiki/Birch_and_Swinnerton-Dyer_conjecture
