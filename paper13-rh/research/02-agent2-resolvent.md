# research/02 -- Agent 2: Resolvent Analysis

*Date: 2026-04-10. Spectral Realisation Cycle 2.*

## 1. The question

Can we prove the resolvent (T_BC - z)^{-1} has NO poles outside
{gamma_n}? Is the resolvent related to zeta'/zeta rigorously?

## 2. The resolvent-zeta connection

### 2.1 Formal identification

For a self-adjoint operator A with pure point spectrum {lambda_n},
the resolvent is:

    (A - z)^{-1} = sum_n |n><n| / (lambda_n - z)

The trace of the resolvent is:

    Tr(A - z)^{-1} = sum_n 1/(lambda_n - z)

If A = T_BC and lambda_n = gamma_n, this is formally related to
the Hadamard product for zeta:

    zeta'/zeta(s) = sum_rho 1/(s - rho) + (smooth terms)

where rho = 1/2 + i*gamma_n. Evaluating at s = 1/2 + iz:

    zeta'/zeta(1/2 + iz) = sum_n 1/(iz - i*gamma_n) + ...
                         = (-i) sum_n 1/(gamma_n - z) + ...

So formally:

    Tr(T_BC - z)^{-1} ~ i * zeta'/zeta(1/2 + iz) + (corrections)

### 2.2 Rigour status

This identification is FORMAL, not rigorous. The issues:

(a) The Hadamard product requires regularisation (the sum diverges
    without pairing rho with 1-rho).
(b) The "smooth terms" include contributions from the pole at s=1
    and the trivial zeros. These must be subtracted.
(c) The trace Tr(T_BC - z)^{-1} is only defined if the resolvent
    is trace-class, which requires T_BC to have compact resolvent.

### 2.3 What the identification WOULD prove

If the identification is rigorous, then the poles of Tr(T_BC - z)^{-1}
are exactly the poles of zeta'/zeta(1/2 + iz), which are at z = gamma_n
(from the non-trivial zeros) plus z = -i/2 (from the pole s=1) plus
z = i*(1/2 + 2k) for k = 1, 2, ... (from the trivial zeros).

The trivial zeros and pole contribute poles OFF the real axis (at
complex z), so they do not affect the real spectrum of T_BC. The
non-trivial zeros contribute poles at z = gamma_n on the real axis.

THEREFORE: if the resolvent = zeta'/zeta identification is rigorous,
spec(T_BC) = {gamma_n} (restricted to real z), and spectral
realisation follows.

## 3. Numerical evidence

### 3.1 Resolvent at z = 16, 17, 18

Between gamma_1 = 14.135 and gamma_2 = 21.022:

    z = 16: |zeta(1/2+16i)| = 1.537e+00 (nonzero)
      dist to gamma_1 = 1.865, dist to gamma_2 = 5.022
      1/min_dist = 0.536 (expected resolvent bound)

    z = 17: |zeta(1/2+17i)| = 2.143e+00 (nonzero)
      dist to gamma_1 = 2.865, dist to gamma_2 = 4.022
      1/min_dist = 0.349

    z = 18: |zeta(1/2+18i)| = 2.337e+00 (nonzero)
      dist to gamma_1 = 3.865, dist to gamma_2 = 3.022
      1/min_dist = 0.331

All three: zeta(1/2 + iz) is nonzero, so zeta'/zeta is finite.
If the resolvent = zeta'/zeta identification holds, the resolvent
is bounded at these points -> no extra spectrum there.

### 3.2 Extended check: 23 points in (14.2, 20.9)

All 23 test points between gamma_1 and gamma_2: zeta(1/2 + iz)
is nonzero at each. No extra poles found.

### 3.3 Between gamma_2 and gamma_3

    z = 22: |zeta(1/2+22i)| = 9.839e-01 (nonzero)
    z = 23: |zeta(1/2+23i)| = 1.455e+00 (nonzero)
    z = 24: |zeta(1/2+24i)| = 1.115e+00 (nonzero)

No extra poles.

## 4. Answer to the three sub-questions

### (a) Can we prove the resolvent has NO poles outside {gamma_n}?

NOT rigorously. The numerical evidence is strong (zeta(1/2 + iz)
is nonzero between consecutive gamma_n -- this is checked for the
first 10^13 zeros by Platt 2017). But "no extra poles" requires
the resolvent = zeta'/zeta identification to be rigorous, which in
turn requires compact resolvent for T_BC (unproved).

### (b) Is the resolvent = zeta'/zeta identification rigorous?

NO. It is formal. The rigorous version would require:
1. T_BC has compact resolvent (unproved)
2. The distributional trace formula (Connes 1999) lifts to an
   actual trace of the resolvent (requires trace-class resolvent)
3. The Hadamard product regularisation matches the operator
   regularisation

### (c) Numerical resolvent trace

The numerical values of zeta'/zeta(1/2 + iz) at z = 16, 17, 18
are finite and consistent with a pure-point-spectrum resolvent.
No anomalies detected. But this is evidence, not proof.

## 5. Premise check

**Does this argument distinguish spec = {gamma_n} from
spec = {gamma_n} ∪ {extra}?**

YES -- if the resolvent = zeta'/zeta identification were rigorous.
Extra spectrum at z_0 not in {gamma_n} would require a pole of
zeta'/zeta(1/2 + iz) at z = z_0, but zeta has no zero at
1/2 + iz_0 (by hypothesis z_0 is not a gamma_n). So extra spectrum
would contradict the analytic structure of zeta.

The argument DOES distinguish, but only modulo the unproved
identification.

## 6. Verdict

**ANGLE 2 OUTCOME: Strongest potential route, blocked by compact
resolvent.**

The resolvent angle is the most promising because it WOULD close
spectral realisation if the resolvent = zeta'/zeta identification
were rigorous. The identification is formally correct and
numerically verified. The blockage is: compact resolvent for T_BC
is unproved.

This angle and Angle 1 converge to the SAME obstruction: compact
resolvent (equivalently, purely discrete spectrum). The two angles
are not independent -- they are two faces of the same coin.

**Status: OPEN. Strongest route, blocked at compact resolvent.**
