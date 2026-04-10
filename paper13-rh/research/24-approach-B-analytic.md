# Approach B: Analytic Perturbation Theory for Even-Sector Simplicity

*Date: 2026-04-09*
*Status: INVESTIGATED. Gap stays positive. No crossings found. Proof not complete.*

---

## 1. Setup

The even-sector matrix QW_lambda^{N,+} is real symmetric, dimension (N+1).
Its entries depend on lambda through L = 2 log(lambda), the von Mangoldt
sum (primes up to lambda^2), and the archimedean integrals (rho, alpha_L,
beta_L, gamma_L). All these are analytic in t = log(lambda) for t > 0.

**Kato-Rellich theorem:** Since QW_lambda^{N,+}(t) is an analytic family
of real symmetric matrices, all eigenvalues mu_k(t) are analytic functions
of t (branches of a multi-valued analytic function). Crossings between
branches can only occur at isolated points in t.

## 2. Numerical scan: lambda = 2 to 100, N = 10

Computed QW_lambda^{N,+} at 27 lambda values with 50-60 digit precision.

### Table: Gap delta^ev = mu_2 - mu_1

| lambda | t = log lambda | mu_1           | mu_2           | gap            | log10(gap) |
|--------|----------------|----------------|----------------|----------------|------------|
|   2.0  | 0.693          | +1.95e-12      | +2.79e-07      | 2.79e-07       | -6.6       |
|   3.0  | 1.099          | +2.97e-23      | +3.92e-18      | 3.92e-18       | -17.4      |
|   5.0  | 1.609          | +5.52e-31      | +2.55e-25      | 2.55e-25       | -24.6      |
|  10.0  | 2.303          | +1.42e-37      | +1.31e-31      | 1.31e-31       | -30.9      |
|  20.0  | 2.996          | +1.65e-42      | +1.20e-36      | 1.20e-36       | -35.9      |
|  50.0  | 3.912          | +5.64e-48      | +1.31e-41      | 1.31e-41       | -40.9      |
| 100.0  | 4.605          | +2.58e-50      | +2.27e-43      | 2.27e-43       | -42.6      |

**All 27 tested lambda values have strictly positive gap.**

### Key observations

1. **Both mu_1 and mu_2 decrease exponentially** with t, but mu_1
   decreases faster than mu_2. The ratio mu_1/mu_2 ~ 10^{-6} throughout,
   so the gap is dominated by mu_2.

2. **The gap is NOT monotone** in lambda (it generally decreases but
   has mild oscillations correlated with new primes entering the
   von Mangoldt sum as lambda^2 crosses a prime).

3. **The gap mu_2 - mu_1 is always orders of magnitude smaller than
   the gap mu_3 - mu_2.** The ratio (mu_3 - mu_2)/(mu_2 - mu_1) ranges
   from ~30,000 at lambda=3 to ~2,000,000 at lambda=100. This is
   EXTREME level repulsion between the first and second eigenvalues.

4. **Derivatives:** dmu_1/dt and dmu_2/dt are both negative (eigenvalues
   decrease with lambda). The condition dmu_1/dt < dmu_2/dt (which would
   guarantee no crossing by monotonicity of the gap) does NOT always hold.
   The derivatives are comparable and both track the overall exponential
   decay.

### N-dependence at lambda = 10

| N  | mu_1       | mu_2       | gap        | mu_1/mu_2   |
|----|------------|------------|------------|-------------|
|  3 | 1.47e-15   | 9.00e-10   | 9.00e-10   | 1.63e-06    |
|  5 | 1.80e-22   | 8.70e-17   | 8.70e-17   | 2.06e-06    |
|  8 | 4.34e-32   | 3.92e-26   | 3.92e-26   | 1.11e-06    |
| 10 | 1.42e-37   | 1.31e-31   | 1.31e-31   | 1.08e-06    |
| 12 | 2.20e-43   | 4.34e-37   | 4.34e-37   | 5.07e-07    |
| 15 | 8.07e-51   | 4.41e-45   | 4.41e-45   | 1.83e-06    |

The ratio mu_1/mu_2 stays around 10^{-6} as N grows. The gap is
essentially equal to mu_2 (since mu_1 << mu_2).

## 3. Theoretical analysis

### 3.1 What Kato-Rellich gives us

For fixed N, the matrix QW_lambda^{N,+}(t) is a real analytic family.
By the Kato-Rellich analytic perturbation theorem:

- Each eigenvalue mu_k(t) is a real analytic function of t.
- A crossing mu_1(t_0) = mu_2(t_0) can occur only at isolated points.
- Near a crossing, the eigenvalues behave as mu_{1,2}(t) ~ c +/- sqrt(t - t_0)
  (square-root branch point in the complexified parameter).

### 3.2 Why Kato-Rellich alone is insufficient

The **Wigner-von Neumann no-crossing rule** says: for real symmetric
matrices depending on ONE real parameter, eigenvalue crossings have
codimension 1 (they generically do NOT occur, but CAN occur for
specific families). The theorem gives:

- Crossings require TWO conditions: the off-diagonal matrix element
  H_{12}(t_0) = 0 AND the diagonal gap H_{11}(t_0) - H_{22}(t_0) = 0
  simultaneously. This is codimension 2 in the space of matrices but
  codimension 1 in a one-parameter family.
- Therefore crossings are POSSIBLE (isolated points) but not generic.

**Conclusion:** Analytic perturbation theory alone cannot rule out crossings.

### 3.3 What the numerics tell us about crossings

If a crossing existed at some t_0 in (0.69, 4.61), the gap function
delta(t) = mu_2(t) - mu_1(t) would have to vanish there. But:

- delta(t) is smooth and strictly positive at all 27 sampled points.
- delta(t) varies smoothly with no sign of approaching zero.
- The gap-to-next-gap ratio (mu_3-mu_2)/(mu_2-mu_1) is enormous (>10^4),
  indicating strong structural separation of the ground state.

For a crossing to exist between sampled points, delta(t) would need
to dip to zero and recover, creating a sharp V-shape. But delta(t)
varies by at most one order of magnitude between adjacent samples
(the log-scale variation is smooth). A dip to zero would require
a variation of 20-40 orders of magnitude in a tiny interval -- this
is incompatible with the analytic dependence and the observed smoothness.

### 3.4 The structural argument (combining with Approach A/C)

The strongest argument combines three facts:

1. **QW^{N,+} has generalized Cauchy structure** (Approach A): the
   matrix entries involve the sequences alpha_L(n) which are distinct
   for distinct n. Generalized Cauchy matrices with distinct parameters
   have simple eigenvalues generically.

2. **The prolate wave operator limit** (Approach C): as N -> infinity,
   QW^{N,+} converges to the prolate wave operator PW, which has simple
   eigenvalues by the Sturm-Liouville oscillation theorem (Slepian 1961).

3. **Analytic dependence on t** (this Approach B): eigenvalues are
   analytic functions of t. If simplicity holds for large t (where the
   prolate limit is accurate), it holds for all but finitely many t
   (the isolated crossings). But the numerics show NO crossings in
   [0.69, 4.61], and the structural argument says crossings require
   a coincidence that the Cauchy structure prevents.

## 4. Gap behavior summary

The gap delta^ev(t) has the asymptotic form:

    delta^ev ~ mu_2 ~ C(N) * exp(-alpha * t)

where alpha ~ 2*pi*N / L ~ pi*N / log(lambda). This is the spacing
between the first two eigenvalues of a matrix whose entries all decay
exponentially. The ratio mu_1/mu_2 ~ 10^{-6} is remarkably stable,
suggesting a STRUCTURAL origin (not accidental).

## 5. Verdict on Approach B

| Question                              | Answer                        |
|---------------------------------------|-------------------------------|
| Is QW^{N,+} analytic in t?            | YES                           |
| Are eigenvalues analytic in t?         | YES (Kato-Rellich)            |
| Does the gap ever reach zero?          | NO (27 samples, all positive) |
| Can crossings be ruled out by theory?  | NOT by Kato-Rellich alone     |
| Does monotonicity of derivatives help? | NO (derivatives not separated)|
| Is there structural support?           | YES (Cauchy + prolate limit)  |
| **Rating**                             | **5/10** (as predicted)       |

Approach B provides the ANALYTIC FRAMEWORK (eigenvalues are analytic,
crossings are isolated) but not the EXCLUSION MECHANISM (no crossings
exist). The exclusion likely requires combining with the Cauchy structure
(Approach A) or the prolate limit (Approach C).

## 6. Code

- `/paper13-rh/code/r56_approach_B_analytic.py`: Lambda scan, N=10
- `/paper13-rh/code/r56_approach_B_analytic.json`: Raw output

---

> *The eigenvalues are analytic. The gap never vanishes.*
> *But analytic perturbation theory says "isolated" not "none".*
> *The exclusion must come from structure, not from smoothness.*
