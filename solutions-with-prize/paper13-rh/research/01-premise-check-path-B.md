# research/01 -- Premise Check: Path B (Weil Positivity / Li Criterion)

*Date: 2026-04-10. Status: PREMISE FAILED (off-line zeros increase Li coefficients).*

## 1. The premise

Path B claims: an off-line zero at delta != 0 violates the Weil
positivity criterion (or makes some Li coefficient lambda_n negative),
proving RH by contradiction.

## 2. Check 1: Does the Weil inner product change sign?

The Weil inner product W(f,f) = sum_rho |f((rho-1/2)/i)|^2.

For on-line zeros, (rho-1/2)/i = gamma_n (real), so each term is
|f(gamma_n)|^2 >= 0. The sum is trivially non-negative.

For an off-line zero at rho = 1/2 + delta + i*t:
(rho-1/2)/i = t - i*delta (complex). But |f(t - i*delta)|^2 >= 0
for any function f. The Weil inner product is a sum of non-negative
terms regardless of whether zeros are on or off the critical line.

**The naive Weil form W(f,f) >= 0 is trivially true and cannot
detect off-line zeros.**

## 3. Check 2: Do off-line zeros make Li coefficients negative?

The Li criterion: RH <=> lambda_n > 0 for all n >= 1.

Computation (50 on-line zeros + hypothetical off-line zero at
1/2 + delta + i*gamma_1):

### Isolated off-line contribution to lambda_n

| delta | lambda_1 shift | lambda_10 shift | lambda_50 shift |
|:------|:---------------|:----------------|:----------------|
| 0.001 | +0.00999798    | +0.95922        | +7.6930         |
| 0.01  | +0.00999796    | +0.95922        | +7.6930         |
| 0.05  | +0.00999760    | +0.95919        | +7.6934         |
| 0.1   | +0.00999648    | +0.95909        | +7.6945         |
| 0.25  | +0.00998863    | +0.95841        | +7.7019         |
| 0.49  | +0.00996211    | +0.95611        | +7.7272         |

**ALL contributions are POSITIVE for every delta tested, for every n.**

An off-line zero INCREASES every Li coefficient. This means adding
off-line zeros makes the Li criterion MORE satisfied, not less.

### Full lambda_n (partial sum + off-line contribution)

All lambda_n remain positive for all tested delta values (0.01, 0.1,
0.25, 0.49). No sign change was observed at any n up to 100.

## 4. Check 3: Why off-line zeros increase Li coefficients

The Li coefficient formula: lambda_n = sum_rho [1 - (1 - 1/rho)^n].

For a zero at rho with |rho| >> 1, the contribution is approximately:
  1 - (1 - 1/rho)^n ~ n/rho + O(n^2/rho^2)

The contribution from the four zeros in the quartet
{rho, 1-rho, conj(rho), conj(1-rho)} involves real parts only
(imaginary parts cancel by symmetry). The real part of n/rho is
positive when Re(rho) > 0, which is true for all non-trivial zeros.

Therefore the contribution to lambda_n is:
  ~ 4 * Re(n/rho) > 0 for any zero with Re(rho) > 0.

This is a STRUCTURAL reason why off-line zeros increase Li coefficients:
the Li criterion measures the "total weight" of zeros, and more zeros
always add more positive weight.

## 5. Verdict

**PREMISE FAILS.** The Weil positivity / Li coefficient approach
cannot prove RH by contradiction because:

1. W(f,f) >= 0 is trivially true regardless of zero locations.
2. Off-line zeros INCREASE Li coefficients (make them more positive).
3. The Li criterion is a NECESSARY condition for RH (if RH holds,
   lambda_n > 0), not a SUFFICIENT detector of off-line zeros
   (off-line zeros don't make lambda_n negative).

Path B is BLOCKED as formulated. The Weil positivity criterion
is equivalent to RH but does not provide a CONTRADICTION mechanism
for off-line zeros.

## 6. Salvage possibilities

The correct use of Weil positivity would require:
(a) Proving the GEOMETRIC SIDE of the explicit formula forces
    positivity, and then showing the spectral side with off-line
    zeros violates this. But both sides are equal by the explicit
    formula, so this is circular.
(b) Finding a DIFFERENT positivity criterion that IS violated by
    off-line zeros. The Nyman-Beurling criterion is a candidate
    but faces similar issues.

## 7. Coboundary lesson check

This is not exactly a coboundary error (the invariant does change),
but it is a SIGN error: the change goes in the wrong direction.
The constraint is non-vacuous (lambda_n changes) but the change
is CONSISTENT with the constraint (lambda_n stays positive). 
The constraint does not EXCLUDE off-line zeros; it is COMPATIBLE
with them.
