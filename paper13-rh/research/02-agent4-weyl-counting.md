# research/02 -- Agent 4: Weyl Counting

*Date: 2026-04-10. Spectral Realisation Cycle 2.*

## 1. The question

Does the Weyl eigenvalue counting function leave room for extra
spectrum? How many extra eigenvalues could hide in the error term?

## 2. The Riemann-von Mangoldt formula

    N(T) = (T/2pi) * log(T/2pi) - T/2pi + 7/8 + S(T)

where:
- N(T) = #{gamma_n : 0 < gamma_n <= T} (exact zero count)
- N_smooth(T) = (T/2pi)*log(T/2pi) - T/2pi + 7/8 (smooth Weyl term)
- S(T) = (1/pi)*arg(zeta(1/2 + iT)) (oscillatory correction)

### 2.1 Bounds on S(T)

Trudgian 2014 (unconditional):

    |S(T)| <= 0.137*log(T) + 0.443*log(log(T)) + 4.350

This gives:

    T = 100:   |S(T)| <= 5.66
    T = 1000:  |S(T)| <= 6.15
    T = 10000: |S(T)| <= 6.60

## 3. Numerical verification (mpmath)

    T     | N_smooth(T) | N_exact(T) | Error     | O(log T)
    ------|-------------|------------|-----------|--------
    100   | 29.00       | 29         | -0.00     | 4.61
    1000  | 648.62      | 649        |  0.38     | 6.91
    10000 | 10142.97    | 10142      | -0.97     | 9.21

The error |N_exact - N_smooth| is O(1) at each test point, well
within the O(log T) bound.

## 4. Could extra eigenvalues hide?

### 4.1 The counting argument

If T_BC had extra eigenvalues x_1, x_2, ..., x_M not in {gamma_n}
but below T, the counting function of T_BC would be:

    N_{T_BC}(T) = N(T) + M

For this to be consistent with the Weyl law for T_BC, we need:

    N(T) + M <= N_smooth(T) + |S(T)| + epsilon

Since N(T) = N_smooth(T) + S(T), we get:

    M <= |S(T)| - S(T) + epsilon <= 2*|S(T)| + epsilon

Using Trudgian's bound:

    M <= 2*(0.137*log(T) + 0.443*log(log(T)) + 4.350) + epsilon

At T = 10000: M <= 2*6.60 = 13.2, so at most ~13 extra eigenvalues
could hide below T = 10000.

### 4.2 But the counting function of T_BC IS N(T)

The Weyl law for T_BC is DERIVED from the Riemann-von Mangoldt
formula. If T_BC has additional spectrum, the Weyl law for T_BC
would be DIFFERENT from the Riemann-von Mangoldt formula. The
error analysis above assumes T_BC satisfies the SAME Weyl law as
the zeta function, which is an assumption, not a theorem.

### 4.3 What a compact resolvent would give

If T_BC has compact resolvent, its eigenvalue counting function
N_{T_BC}(T) is well-defined and satisfies a Weyl law determined
by the operator's symbol. If this symbol matches the zeta function's
Weyl law, extra eigenvalues would perturb the match.

Without compact resolvent: T_BC might have continuous spectrum,
and the "counting function" is not even defined in the usual sense.

## 5. The anti-fine-tuning supplement

Even if O(log T) extra eigenvalues could hide in the Weyl error,
the anti-fine-tuning argument (research/201) bounds the probability
of their existence:

    P(extra eigenvalue compatible with 33 observables) < 10^{-34}

This is because each hypothetical extra eigenvalue would perturb
ALL 33 closed formulas in the operator dictionary. The Weyl error
allows O(log T) extra eigenvalues; the anti-fine-tuning bound says
even ONE is statistically impossible.

Combined: the Weyl counting constrains the NUMBER of possible extra
eigenvalues to O(log T), and the anti-fine-tuning constrains each
one to probability < 10^{-34}. Together: effectively zero.

## 6. Premise check

**Does the Weyl counting distinguish spec = {gamma_n} from
spec = {gamma_n} ∪ {extra}?**

PARTIALLY. It constrains the number of extra eigenvalues to
O(log T), but does not rule them out entirely. The counting
argument is a bound, not an exclusion. Combined with anti-fine-
tuning, the exclusion is statistical, not absolute.

## 7. Verdict

**ANGLE 4 OUTCOME: Bounds extra eigenvalue count to O(log T);
combined with anti-fine-tuning, gives P < 10^{-34} for even one.**

The Weyl law is a constraint, not a proof. It leaves room for
O(log T) extra eigenvalues at each height T. But the anti-fine-
tuning argument makes each one overwhelmingly unlikely. The
combination is the strongest available empirical/semi-rigorous
evidence for spectral realisation, but it is NOT a proof.

For a proof: need compact resolvent (to define the counting
function rigorously) + matching Weyl asymptotics (to exclude extra
eigenvalues by counting).

**Status: OPEN. Strong evidence, not a proof.**
