# Navier-Stokes — Requirements (itemized)

**Source:** `00-problem-statement.md` (Fefferman 2000, with erratum)

## Four sub-problems — prove ANY ONE

| # | Sub-problem | Domain | Direction | Force |
|---|---|---|---|---|
| A | Existence & smoothness on R^3 | R^3, decay (4) | positive (smooth for all t) | f ≡ 0 |
| B | Existence & smoothness on T^3 | T^3 = R^3/Z^3, periodic (8) | positive | f ≡ 0 |
| C | Breakdown on R^3 | R^3, decay (4)(5) | negative (finite-time blow-up) | f as in (5) |
| D | Breakdown on T^3 | T^3, periodic (8)(9) | negative | f as in (9) |

## Requirements common to all

| # | Requirement | Fefferman source |
|---|---|---|
| 1 | Viscosity ν > 0 | Stated in each (A)-(D) |
| 2 | Spatial dimension n = 3 | Stated |
| 3 | Incompressibility div u = 0 | Eq. (2) |
| 4 | Initial data u° smooth and divergence-free | Stated |
| 5 | Solution is smooth (C^∞) when direction is positive | Eq. (6), (11) |
| 6 | Bounded energy (physically reasonable) | Eq. (7) |
| 7 | Satisfies the PDE system (1), (2), (3) | Eq. (1)-(3) |

## §5(b) special clause

> In the case of the P versus NP Problem and the Navier-Stokes Problem, a resolution in either direction will be evaluated by the standard evaluation procedure set forth in Section 7.

So (A or B) proves smoothness globally; (C or D) exhibits blow-up. EITHER wins.

## Known partial results (context)

- Leray 1934: weak solutions exist globally on R^3.
- Caffarelli-Kohn-Nirenberg 1982: suitable weak solutions have singular set of parabolic Hausdorff 1-measure zero.
- Short-time smoothness for general data, global smoothness for small initial data.
- 2D case: resolved positively long ago.

## Non-required

- Uniqueness of weak solutions (not required for either direction).
- Euler case (ν = 0) (not on Clay list).
- n ≠ 3 (not required).
