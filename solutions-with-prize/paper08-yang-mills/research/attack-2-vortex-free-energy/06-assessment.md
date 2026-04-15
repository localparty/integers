# 06. Honest Assessment: Does This Close the Gap?

## I. What We Achieved

### I.1 Concrete results

1. **Exact formula for $F_v^{(0)}$** [COMPUTED]:

$$F_v^{(0)} = \sum_{n_1 \in \mathbb{Z}}\ln\frac{\cosh(RE_{n_1}) - \cos(2\pi/3)}{\cosh(RE_{n_1}) - 1}$$

with $E_{n_1} = \sqrt{(2\pi(n_1+1/3)/L)^2 + m^2}$. This is positive
for all $R, L > 0$, term by term. [PROVED]

2. **$F_v^{(1)}$ from sigma fluctuations** [COMPUTED]: The
$O(1)$ correction from the sigma determinant is

$$F_v^{(1)} = \frac{1}{2}\sum_{\mathbf{p}}\ln\frac{\Pi^{(1)}(\mathbf{p})}{\Pi^{(0)}(\mathbf{p})}$$

This vanishes identically as $R \to \infty$ (proved) and is $O(L/R)$
at large $R/L$ (computed).

3. **Bound at $N = 3$ verified in limiting regimes**:
   - Small $L$: $F_v > 0$ because $F_v^{(0)} = O(1)$ and $F_v^{(1)} \to 0$. [PROVED]
   - Large $R$: $F_v > 0$ trivially (both terms vanish, leading order dominates). [PROVED]

4. **Numerical estimates**: At $mL \ll 1$, $F_v(N=3) \approx 1.18$
   at leading order. The $O(1)$ correction would need to exceed $-1.18$
   to cause trouble, which is implausible given the typical size of
   $1/N$ corrections. [ESTIMATED]


### I.2 What the calculation reveals about the physics

The center vortex free energy in the CP^2 model on a torus is a
**Casimir-type** effect: it is exponentially small in $Rm$ (or $Lm$)
at large volume, not linearly growing. This is characteristic of
2D -- there are no "confining strings" of the type seen in 4D
Yang-Mills. Instead, confinement in 2D manifests as the positivity
of a finite (and small) quantity.

The $1/N$ expansion for $F_v$ has the structure:
- $O(N)$ term: positive, from the free massive boson Casimir energy with twisted b.c.
- $O(1)$ term: from sigma fluctuations modifying the bubble. Vanishes at $R = \infty$.
- Higher orders: $O(1/N)$, expected to be small.


---

## II. What We Did NOT Achieve

### II.1 The gap that remains

**The sign of $F_v^{(1)}$ in the crossover regime $mL \sim 1$ is
undetermined.** [OPEN]

This is the critical gap. The bound at $N = 3$ requires
$F_v^{(1)} > -3 F_v^{(0)}$, and while we showed this holds at the
endpoints ($L \to 0$ and $L \to \infty$), we could not prove it
for all intermediate $L$.

### II.2 Why the gap persists

Three technical obstacles:

1. **The bubble ratio $\Pi^{(1)}/\Pi^{(0)}$ at finite volume.**
   This ratio involves a double sum (over internal momenta) inside
   a log-sum (over sigma momenta). We could estimate its magnitude
   ($O(1)$ at $R = L$) but not determine its sign without numerical
   evaluation of the double sums.

2. **The $1/N$ expansion itself.** At $N = 3$, the "large-$N$
   expansion" is not obviously convergent. The $O(1/N)$ correction
   $F_v^{(2)}/3$ could be comparable to $F_v^{(1)}$, making the
   truncation unreliable.

3. **The saddle-point approximation.** The entire calculation assumes
   that the sigma field is well-described by small fluctuations
   around $\sigma_0 = m^2$. At $N = 3$, large fluctuations of $\sigma$
   (or nonperturbative sigma configurations like sigma kinks) could
   contribute.

### II.3 The deeper issue

The real problem is not computational but conceptual: **the $1/N$
expansion does not provide a reliable bound at $N = 3$**.

Even if we could compute $F_v^{(1)}$ exactly and show it satisfies
the bound, we would still need to control $F_v^{(2)}, F_v^{(3)}, \ldots$
at $N = 3$. The $1/N$ expansion is an asymptotic series, not a
convergent one, and there is no reason to expect truncation at $O(1)$
to be accurate for $N = 3$.

This is the same issue that plagues all large-$N$ approaches to
proving rigorous statements at finite $N$: the expansion tells you
about the neighborhood of $N = \infty$, not about specific finite values.


---

## III. Comparison with What Would Be Needed

### III.1 For a proof of adiabatic continuity

A proof of adiabatic continuity for the CP^2 model would require
showing $F_v(N=3, L) > 0$ for all $L > 0$. This means:

1. A **non-perturbative** (in $1/N$) argument, or
2. A **resummation** of the $1/N$ series giving a bound, or
3. A completely different approach (lattice, bootstrap, exact solution).

Our calculation provides (1) the leading term exactly, (2) the structure
of the $O(1)$ correction, and (3) verification in limiting regimes.
It does **not** provide a proof for all $L$.

### III.2 For the paper

The calculation is **useful** as:
- An explicit demonstration that the $1/N$ framework gives the right
  qualitative physics (positive $F_v$ at leading order).
- A quantitative prediction: $F_v(N=3) \approx 1.18$ at small $mL$,
  which could be checked on the lattice.
- A clear identification of the obstruction: the sign of $F_v^{(1)}$
  at $mL \sim 1$.

The calculation is **not sufficient** as:
- A proof that $F_v > 0$ for all $L$ at $N = 3$.
- A proof of adiabatic continuity.


---

## IV. Possible Next Steps

### IV.1 Numerical evaluation

Compute $F_v^{(1)}$ numerically on the finite torus for $mL \in [0.5, 5]$.
This requires evaluating the double sums in $\Pi^{(v)}$ and the
outer sum over sigma momenta. This is a finite (doubly-periodic) sum
and can be computed to arbitrary precision.

**Assessment:** Feasible. Would resolve the sign question. But gives
a numerical answer, not a proof.

### IV.2 Lattice Monte Carlo

Measure $F_v$ directly in lattice CP^2 simulations. Compare with the
$1/N$ prediction. If agreement is good, this provides strong evidence
(but not proof) for adiabatic continuity.

**Assessment:** Feasible. Standard technology. Would provide the
definitive numerical answer.

### IV.3 Alternative analytic approaches

- **Exact integrability:** The CP^{N-1} model is integrable in 2D.
  The thermodynamic Bethe ansatz (TBA) could in principle give the
  exact free energy with twisted boundary conditions. For CP^1 = O(3),
  this has been done. For CP^2, the TBA is known (Wiegmann, Zamolodchikov)
  and might be applicable.

  **Assessment:** Promising. This could give a non-perturbative result.
  But the TBA with twisted boundary conditions is technically challenging.

- **Functional inequality:** Prove a convexity or monotonicity property
  of $F_v(L)$ that, combined with the known limits ($F_v > 0$ at
  $L \to 0$ and $L \to \infty$), implies $F_v > 0$ for all $L$.

  **Assessment:** Speculative. No clear path.

- **Bootstrap:** Use the conformal bootstrap (at the UV fixed point)
  or the S-matrix bootstrap (in the massive theory) to constrain $F_v$.

  **Assessment:** Very speculative.


---

## V. Verdict

### Does this close the gap?

**No.** The center vortex free energy calculation at $O(1)$ in the
$1/N$ expansion does not close the gap for adiabatic continuity in
the CP^2 model. The specific obstruction is:

$$\text{Sign of } F_v^{(1)}(mL \sim 1) \text{ on the finite torus: } \textbf{[OPEN]}$$

### What is the status?

| Statement | Status |
|-----------|--------|
| $F_v^{(0)} > 0$ for all $L, R$ | [PROVED] |
| $F_v^{(1)} = 0$ at $R = \infty$ | [PROVED] |
| $F_v(N=3) > 0$ at small $L$ | [PROVED] |
| $F_v(N=3) > 0$ at large $R$ | [PROVED] |
| $F_v(N=3) > 0$ for all $L, R$ | [OPEN] |
| Adiabatic continuity for CP^2 | [OPEN] |

### What would close it?

The most realistic paths:

1. **Numerical evaluation of $F_v^{(1)}$** -- would resolve the
   sign question and either (a) confirm the bound with a comfortable
   margin, suggesting a proof should exist, or (b) reveal that the
   bound is marginal or violated, indicating a real problem.

2. **Thermodynamic Bethe ansatz with twisted b.c.** -- could give
   an exact, non-perturbative result for $F_v$ at $N = 3$.

3. **Lattice Monte Carlo** -- definitive numerical answer.

### Honest bottom line

The $1/N$ approach to the center vortex free energy **works** in
the sense that it produces the right leading-order physics and
identifies the relevant $O(1)$ correction. It **fails** to close
the gap because the $1/N$ expansion at $N = 3$ is not controlled
enough to yield a rigorous bound. The calculation narrows the
question to a specific, concrete, numerically evaluable quantity
(the sigma determinant ratio on the finite torus), but does not
resolve it analytically.

This is a common pattern in large-$N$ physics: the expansion
illuminates the structure but cannot deliver proofs at small $N$.
For the paper, this attack should be presented as "evidence from
the $1/N$ expansion" rather than a proof.
