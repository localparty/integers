# BSD — Requirements (itemized)

**Source:** `00-problem-statement.md` (Wiles 2000)

## Weak BSD (minimum Millennium requirement)

| # | Requirement | Source |
|---|---|---|
| 1 | For every elliptic curve E/Q: ord_{s=1} L(E, s) = rank E(Q) | Wiles main conjecture |
| 2 | Equivalently L(E, 1) = 0 ⇔ E(Q) is infinite | Wiles immediate corollary |
| 3 | Must hold for all ranks (not just r ≤ 1) | Gap vs current partial result |
| 4 | Must cover all elliptic curves over Q (CM and non-CM) | Generality |

## Strong BSD (bonus / refined version)

| # | Requirement | Source |
|---|---|---|
| 5 | Leading coefficient formula: c* = \|X_C\| R_∞ w_∞ ∏ w_p / \|C(Q)_tors\|^2 | Wiles refined |
| 6 | Finiteness of Tate-Shafarevich X_C (should follow) | Wiles prose |

## Current partial progress

- **r = 0** and **r = 1** cases resolved for modular E/Q (Gross-Zagier-Kolyvagin).
- **r ≥ 2** completely open.
- Modularity of all E/Q is now a theorem (Breuil-Conrad-Diamond-Taylor / Wiles-Taylor).

## Clay §5(c) note

Counterexample = elliptic curve where ord_{s=1} L(E, s) ≠ rank. Unambiguous §5(c)(i) full-prize material if exhibited.

## Programme scope note (internal)

Paper 26 currently proves **CM curves over Q with class number h_K = 1** (substantial but not full). Full BSD extension to non-CM and to all ranks is the remaining gap for a Clay-eligible paper.
