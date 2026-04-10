# Birch and Swinnerton-Dyer Conjecture — Official Clay Problem Description

**Author:** Andrew Wiles
**Source:** https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/
**PDF:** https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf
**Saved:** 2026-04-10

---

## The Conjecture (Clay Statement)

The Birch and Swinnerton-Dyer conjecture asserts that the size of the group
of rational points on an elliptic curve is related to the behavior of an
associated zeta function ζ(s) near the point s = 1. In particular, this
conjecture asserts that if ζ(1) is equal to 0, then there are an infinite
number of rational points (solutions), and conversely, if ζ(1) is not equal
to 0, then there is only a finite number of such points.

## Weak Form

For an elliptic curve E over Q:

    rank(E(Q)) = ord_{s=1} L(E, s)

The algebraic rank equals the analytic rank (order of vanishing of the
Hasse-Weil L-function at s = 1).

## Strong Form (Leading Coefficient Formula)

    L^{(r)}(E, 1) / r! = (#Sha(E) · Ω_E · R_E · ∏_{p|N} c_p) / (#E_tor)²

Where:
- r = rank(E(Q))
- Sha(E) = Tate-Shafarevich group (conjecturally finite)
- Ω_E = real period (times number of connected components of E(R))
- R_E = regulator (determinant of Néron-Tate height pairing matrix)
- c_p = Tamagawa numbers at primes of bad reduction
- #E_tor = order of torsion subgroup E(Q)_tor

## Key Structural Requirements

The conjecture presupposes:
1. **Analytic continuation** of L(E, s) to s = 1 (proved via modularity theorem)
2. **Finiteness of Sha(E)** (unproved in general; predicted by BSD)
3. **Mordell-Weil theorem** (E(Q) is finitely generated — proved)

## What Wiles' Description Requires for a Proof

A complete proof must establish:
1. The equality rank = analytic rank
2. The leading coefficient formula (strong form) — or at minimum the rank equality
3. All intermediate objects (Sha, regulators, periods, Tamagawa numbers) must be
   well-defined and correctly computed

## Proven Partial Results (as of 2026)

| Result | Authors | Year | Scope |
|:-------|:--------|:-----|:------|
| CM curves, L(E,1) ≠ 0 → rank = 0 | Coates-Wiles | 1977 | CM only |
| Gross-Zagier formula | Gross-Zagier | 1986 | Modular curves, analytic rank 1 |
| Euler systems → rank 0 and 1 | Kolyvagin | 1989 | Modular curves |
| Sha finite for rank 0, 1 | Kolyvagin | 1989 | Modular curves |
| p-part of BSD for CM curves | Rubin | 1991 | CM, p > 7 |
| Modularity theorem | BCDT | 2001 | All E/Q |
| Average rank < 7/6 | Bhargava-Shankar | 2015 | Statistical |
| BSD formula at rank 1 | Jetchev-Skinner-Wan | 2017 | Specific families |
| Iwasawa main conjecture connections | Various | 2020-2025 | p-adic BSD |

**No proven cases exist for rank ≥ 2.**

## References

- Wiles, A. "The Birch and Swinnerton-Dyer Conjecture." Clay Mathematics Institute official problem description.
- Birch, B. J. and Swinnerton-Dyer, H. P. F. "Notes on Elliptic Curves (I, II)." J. reine angew. Math. 212, 7-25, 1963.
- Gross, B. and Zagier, D. "Heegner points and derivatives of L-series." Invent. Math. 84, 225-320, 1986.
- Kolyvagin, V. "Finiteness of E(Q) and Sha(E/Q) for a class of Weil curves." Math. USSR Izv. 32, 523-541, 1989.
- Rubin, K. "The 'main conjectures' of Iwasawa theory for imaginary quadratic fields." Invent. Math. 103, 25-68, 1991.
- Breuil, C., Conrad, B., Diamond, F., Taylor, R. "On the modularity of elliptic curves over Q." J. Amer. Math. Soc. 14, 843-939, 2001.

## Web Sources

- Clay Mathematics Institute: https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/
- Wikipedia: https://en.wikipedia.org/wiki/Birch_and_Swinnerton-Dyer_conjecture
