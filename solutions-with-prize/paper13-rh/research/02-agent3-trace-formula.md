# research/02 -- Agent 3: Connes Trace Formula

*Date: 2026-04-10. Spectral Realisation Cycle 2.*

## 1. The question

Does the Connes trace formula uniquely determine spec(T_BC)?

## 2. The Connes trace formula (1999)

### 2.1 Precise statement

**Reference:** A. Connes, "Trace formula in noncommutative geometry
and the zeros of the Riemann zeta function," Selecta Math. (N.S.)
**5** (1999), no. 1, 29--106.

**Theorem (Connes 1999, Theorem 1).** Let h be an even Schwartz
function on R with compactly supported Fourier transform h-hat.
Then:

    sum_gamma h(gamma) = h(i/2) + h(-i/2)
        - (1/2pi) int_{-infty}^{infty} h(t) * Psi(1/2 + it) dt
        + sum_p sum_{m=1}^{infty} (log p / p^{m/2}) * h-hat(m*log p)

where:
- The left sum is over ALL non-trivial zeros rho = 1/2 + i*gamma
  (assuming RH, gamma in R; without RH, gamma in C)
- Psi = Gamma'/Gamma is the digamma function
- The right side involves the prime powers

### 2.2 The Weil explicit formula form

Without assuming RH, the formula becomes:

    sum_rho h-hat(log|rho - 1/2|) = (explicit terms involving primes)

This is the Riemann-Weil explicit formula in operator-theoretic
garb.

### 2.3 Operator interpretation

Connes interprets this as: T_BC is an operator whose spectral
measure mu satisfies

    int h(t) d*mu(t) = (right side of trace formula)

for all admissible test functions h.

## 3. Does the trace formula determine the spectrum uniquely?

### 3.1 The test function space

The test functions h range over even Schwartz functions with
compactly supported Fourier transform. This is the Paley-Wiener
space PW (entire functions of exponential type that are L^2 on R).

**Key question:** Is PW large enough to determine a measure on R?

### 3.2 Stone-Weierstrass argument

PW is dense in C_0(R) (continuous functions vanishing at infinity)
in the sup norm. Therefore, the linear functional

    h -> int h d*mu

is determined on a dense subspace of C_0(R). By density, the
measure mu is uniquely determined by its values on PW.

**THEREFORE: the Connes trace formula uniquely determines the
spectral measure of T_BC.**

### 3.3 What does this give us?

The trace formula determines the spectral measure. But knowing the
spectral measure does not immediately tell us whether the spectrum
is pure point, absolutely continuous, or singular continuous. The
spectral measure could be:

(a) Pure point: mu = sum_n w_n * delta_{gamma_n} (discrete masses
    at {gamma_n}).
(b) Absolutely continuous: mu = rho(t) dt (continuous density).
(c) Mixed: pure point + continuous.

The trace formula determines WHICH of these cases holds. The
explicit formula gives:

    sum_gamma h(gamma) = (prime sum) + (digamma integral) + ...

The LEFT side is a sum over discrete points (the zeros). This
looks like a pure point measure. But appearances can deceive:
if RH fails, some gamma are complex, and the "sum" on the left
is really over complex rho, not real gamma.

### 3.4 The circular trap

Assuming RH, the left side is a sum of delta functions at real
points gamma_n. This IS a pure point measure. The spectral measure
is then:

    mu = sum_n delta_{gamma_n}

and the spectrum is pure point, and spectral realisation holds.

But this ASSUMES RH. Without assuming RH, we don't know that all
gamma are real. If some gamma are complex (off the critical line),
the spectral measure on R would not include those rho, and the
spectrum of the self-adjoint operator T_BC (which IS on R) would
NOT include those rho.

## 4. The Connes trace formula without RH

### 4.1 What changes

Without RH, the explicit formula still holds:

    sum_rho h-hat(rho - 1/2) = (prime terms)

but some rho may have Re(rho) != 1/2. The spectral measure of
the self-adjoint T_BC on R is determined by the trace formula
regardless. The question is: does this measure see the off-line
zeros?

### 4.2 Connes' absorption argument

Connes' key insight (1999, Section 5): the operator T_BC on the
full adele class space has spectrum = R (continuous, multiplicity
one). The zeros appear as MISSING spectral values when one passes
to a quotient space H_R. The spectral realisation is: the
quotient space H_R has spectrum = {gamma_n}.

If an off-line zero rho = sigma + i*gamma with sigma != 1/2 existed,
it would appear in the trace formula but NOT in the spectrum of
the self-adjoint T_BC (which is real). This zero would have to be
"absorbed" into the continuous spectrum of T_BC on the adele class
space, rather than appearing in the discrete spectrum on H_R.

### 4.3 The H_R construction problem

The space H_R is defined as the orthogonal complement of the
"prolate" subspace in L^2(C_Q). The construction of H_R uses the
Weil explicit formula to identify which spectral values to keep.

**Problem:** If H_R is defined using the zeros, the argument is
circular: the spectrum of T_BC on H_R equals {gamma_n} by
construction.

Connes is aware of this. His programme aims to construct H_R
INTRINSICALLY from the BC algebra, without reference to the zeros.
This intrinsic construction is the 25-year open problem.

## 5. Premise check

**Does the trace formula distinguish spec = {gamma_n} from
spec = {gamma_n} ∪ {extra}?**

YES, in principle. The trace formula determines the spectral
measure uniquely (Section 3.2). If the spectral measure is pure
point at {gamma_n}, extra spectrum is impossible.

BUT: extracting the spectral measure from the trace formula
requires knowing whether to interpret the left side as a real sum
(RH true) or a complex sum (RH false). This is circular.

## 6. Verdict

**ANGLE 3 OUTCOME: Trace formula determines spectral measure
uniquely, but extracting the answer requires RH.**

The Connes trace formula is a powerful constraint: it pins the
spectral measure completely. But the constraint is symmetric --
it is consistent with BOTH pure point spectrum (RH true) and
mixed spectrum (RH false). The trace formula alone cannot
distinguish these cases without additional input about the
nature of the zeros.

The additional input would be: either compact resolvent (giving
pure point spectrum a priori) or the intrinsic construction of
H_R (Connes' programme).

**Status: OPEN. Correct framework but circular at the key step.**
