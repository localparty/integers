# Corrected Proposition 4.3 — Minimal-Conductor Bridge Table

*Closing Gap G1 from math referee run r01.*
*Computed in `code/.venv/` with sympy, 2026-04-10.*

## The correction

Referee audit C5 found that the paper's original Proposition 4.3
had 3 of 4 rows broken:

- **k=2** row (paper's ERRATUM already acknowledges): wrong Frobenius
- **k=4** row `((2+i), (5))`: INVALID — (2+i) has norm 5, which divides
  the conductor (5), so (2+i) is not coprime to (5), so the Frobenius
  is undefined
- **k=6** row `((1+i), (7))`: WRONG — paper claims `ord(2) = 1` in
  `(ℤ/7ℤ)^×`, but the actual order is 3

Only the **k=3** row (`(3+2i)`, `(7)`) was correct.

## The corrected table

Using the same conductors `{3, 5, 7}` (product 105), with correct
Frobenius orders:

| k | N_cond | Bridge prime 𝔭 | N(𝔭) | N(𝔭) mod N_cond | ord | k = φ(N)/ord |
|:-:|:------:|:--------------:|:----:|:---------------:|:---:|:------------:|
| 2 |   3    |   (2+3i)       |  13  |        1        |  1  |    2/1 = 2   |
| 3 |   7    |   (2+3i)       |  13  |        6        |  2  |    6/2 = 3   |
| 4 |   5    |   (4+5i)       |  41  |        1        |  1  |    4/1 = 4   |
| 6 |   7    |   (2+5i)       |  29  |        1        |  1  |    6/1 = 6   |

**All four rows verified computationally.** Conductor product
3 × 5 × 7 = 105 as the paper claims.

## Why this table works (where the paper's didn't)

The paper's original table tried to use small-norm Gaussian primes like
`(1+i)` and `(2+i)`, but ran into two problems:

1. **Coprimality failure** — `(2+i)` has norm 5 and so is
   NOT coprime to the conductor ideal (5). The Frobenius at such a
   pair is undefined.
2. **Wrong order computation** — `ord((1+i) norm 2, conductor 7) = 3`,
   not 1; this gives `k = 2`, not 6.

The corrected table uses **Gaussian primes of larger norm** that are
coprime to the conductor and have the required order:

- `(2+3i)` has norm 13, coprime to both 3 and 7, with the right order
  in each group.
- `(4+5i)` has norm 41, coprime to 5, with order 1 in (ℤ/5ℤ)^*.
- `(2+5i)` has norm 29, coprime to 7, with order 1 in (ℤ/7ℤ)^*.

## Consequences for the proof chain

### The Baker argument still fires

The Baker argument needs **two** bridges with **distinct** prime norms.
The corrected table gives **three** distinct norms: {13, 29, 41}.

- `log(13) / log(41)` is transcendental (Baker 1966, or even
  elementary via unique factorization for irrationality).
- `log(29) / log(41)` is transcendental.
- `log(13) / log(29)` is transcendental.

Any pair suffices. The kill argument closes exactly as §8.3 claims.

### The inert-prime edge case (TR5) is avoided

The referee audit flagged §8.3 Step 5 for not handling inert Gaussian
primes (with norm p²). The corrected table uses **only split
Gaussian primes**, whose norms 13, 29, 41 are all rational primes.
For rational prime norm N,

`N^{−2δ} ∈ ℚ ⇒ −2δ ∈ ℤ ⇒ δ ∈ (1/2)ℤ`

Combined with `|δ| < 1/2`, the only possibility is `δ = 0`. Clean.

The TR5 concern (inert prime allowing `δ ∈ {−1/4, 0, 1/4}`) does
not arise because the bridges in the corrected table use no inert
primes.

## Verification

Run the computation in `code/`:

```python
from math import gcd
from sympy import totient

def mult_order(a, n):
    if gcd(a, n) != 1: return None
    k, x = 1, a % n
    while x != 1:
        x = (x * a) % n
        k += 1
    return k

# Row 1: k=2, conductor 3, prime (2+3i) norm 13
assert mult_order(13, 3) == 1  # 13 ≡ 1 mod 3
assert int(totient(3)) // 1 == 2  # k = 2

# Row 2: k=3, conductor 7, prime (2+3i) norm 13
assert mult_order(13, 7) == 2  # 13 ≡ 6 ≡ -1 mod 7, order 2
assert int(totient(7)) // 2 == 3  # k = 3

# Row 3: k=4, conductor 5, prime (4+5i) norm 41
assert mult_order(41, 5) == 1  # 41 ≡ 1 mod 5
assert int(totient(5)) // 1 == 4  # k = 4

# Row 4: k=6, conductor 7, prime (2+5i) norm 29
assert mult_order(29, 7) == 1  # 29 ≡ 1 mod 7
assert int(totient(7)) // 1 == 6  # k = 6

print("All four rows verified.")
```

All four assertions pass. The corrected table is a valid replacement
for Proposition 4.3.

## On Proposition 4.2's "355 bridge triples" claim

An independent count for odd `N_cond ≤ 50`, `N(𝔭) ≤ 50` (counting each
split prime twice, since `(a+bi)` and `(a−bi)` are distinct prime
ideals) gives **203 triples**, not 355. The discrepancy may be due to
the paper's counting convention (even conductors, larger norm range,
different counting of conjugate primes). **What matters for the proof
chain is that more than two valid triples with distinct norms exist,
which is clearly the case.**

The exact count of 355 is an editorial claim that should be
re-verified using the paper's exact conventions, but it is not
load-bearing for the proof — the existence of multiple valid triples
is all that matters, and that is established.

## Status

**Gap G1 (rigor audit): CLOSED.** The corrected bridge table replaces
the broken Proposition 4.3 and gives the same conductor product
(105) and the same Baker kill structure as claimed. The rigor label
for this item upgrades from **[GAP]** to **[LEMMA]** (straightforward
computational verification).
