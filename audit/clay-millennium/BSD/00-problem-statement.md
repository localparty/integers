# Birch and Swinnerton-Dyer Conjecture — Official Problem Statement

**Author of official statement:** Andrew Wiles, "The Birch and Swinnerton-Dyer Conjecture"
**Source:** https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf
**Local copy:** `../00-clay-rules/bsd-wiles.pdf`
**Text extract:** `../00-clay-rules/bsd-wiles.txt`
**Retrieved:** 2026-04-14

---

## The Problem (verbatim)

Wiles sets up: elliptic curve C over Q, rank r of the Mordell-Weil group C(Q) ≅ Z^r ⊕ C(Q)_tors, incomplete L-series

> L(C, s) := ∏_{p ∤ 2Δ} (1 − a_p p^{−s} + p^{1−2s})^{−1}

with a_p = p − N_p, N_p the mod-p point count. The Euler product converges for Re(s) > 3/2; holomorphic continuation to C is now a theorem (modularity). The prize problem:

> **Conjecture (Birch and Swinnerton-Dyer).** The Taylor expansion of L(C, s) at s = 1 has the form
>
> L(C, s) = c(s − 1)^r + higher order terms
>
> with c ≠ 0 and r = rank(C(Q)).

> In particular this conjecture asserts that L(C, 1) = 0 ⇔ C(Q) is infinite.

## Refined (strong) version

Using the completed L-series L*(C, s) (including Euler factors at p | 2Δ):

> L*(C, s) ∼ c*(s − 1)^r with
>
> c* = |X_C| R_∞ w_∞ ∏_{p|2Δ} w_p / |C(Q)_tors|^2

where |X_C| is the order of the Tate-Shafarevich group (conjecturally finite), R_∞ is an r × r regulator (height pairing on generators of C(Q)/C(Q)_tors), w_p are local factors, w_∞ is a simple multiple of the real period.

> It is hoped that a proof of the conjecture would also yield a proof of the finiteness of X_C.

## Generalizations (context, not required)

> The conjecture can also be stated over any number field as well as for abelian varieties… more elaborate conjectures concerning special values of L-functions have appeared, due to Tate, Lichtenbaum, Deligne, Bloch, Beilinson and others.

These are NOT part of the Millennium prize. Only BSD for elliptic curves over Q (weak form at minimum; strong form a bonus).

## Best current partial result (Wiles §2)

> Theorem. If L(C, s) ∼ c(s − 1)^m with c ≠ 0 and m = 0 or 1, then the conjecture holds.

(Gross-Zagier-Kolyvagin, enabled by modularity of all elliptic curves over Q.) Ranks r ≥ 2 unsettled.

## Clay §5(c) note

BSD is NOT a §5(b) problem. A counterexample (rank mismatch) falls under §5(c).
