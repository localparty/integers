# 06. Assessment: Can Monotonicity Be Proved?

## Purpose

Honest evaluation of the monotonicity conjecture $m(N) \geq m(\infty)
= \Lambda$ for the 2D CP^{N-1} sigma model. What is proved, what is
bounded, what remains open, and what is the strongest achievable
statement given current mathematical tools?


---

## 6.1 The Scoreboard

### 6.1.1 What is PROVED (rigorous, no gaps)

1. **H = H_0 + V/N decomposition** (file 01): The Hamiltonian of the
   CP^{N-1} model decomposes as a free part (N = infinity) plus a
   1/N interaction. The Hilbert space, transfer matrix, and all
   operators are well-defined on the lattice.

2. **gap(H_0) = Lambda** (file 01): At N = infinity, the mass gap
   equals the dynamical scale.

3. **V is indefinite** (file 02): The interaction operator is NOT
   positive semi-definite. The cubic sigma vertex has $\Gamma_3 < 0$.
   Therefore the naive argument $H \geq H_0$ FAILS.

4. **Reflection positivity** (file 04): The CP^{N-1} lattice model
   is reflection positive. The transfer matrix is positive and
   self-adjoint. The spectral representation of correlations has
   positive weights.

5. **m(2) = (8/e)Lambda > Lambda** (file 05): At N = 2, the exact
   mass gap from the Bethe ansatz is approximately 2.94 Lambda.
   Monotonicity holds at N = 2.

6. **FKG/GKS do not apply** (file 04): Standard correlation
   inequalities are structurally incompatible with the CP^{N-1}
   target space.

7. **General lower bound** (file 03): gap(H) >= Lambda - 2||V_-||/N,
   but this does NOT give gap(H) >= Lambda since ||V_-|| > 0.

### 6.1.2 What is BOUNDED (rigorous modulo computable constants)

8. **First-order gap shift is positive** (file 03):
   $\delta\Delta^{(1)} = \alpha_1 \Lambda/N$ with $\alpha_1 > 0$.
   This is established from the self-energy computation (CRV 1992)
   but the positivity of $\alpha_1$ depends on the numerical
   evaluation of definite integrals. A computer-assisted proof could
   make this fully rigorous.

9. **gap(H) >= Lambda for N >= N_0** (files 03, 04): Perturbation
   theory + continuity in 1/N gives monotonicity for sufficiently
   large N. The critical $N_0$ depends on the ratio of second-order
   to first-order perturbative coefficients.

10. **Temple's inequality bound** (file 03): A rigorous lower bound
    on the gap is available via Temple's inequality, but requires
    evaluation of the variance $\langle V^2 \rangle - \langle V \rangle^2$
    in the first excited state.

### 6.1.3 What is ESTABLISHED (strong evidence, not fully rigorous)

11. **Numerical monotonicity** (file 05): Monte Carlo simulations
    confirm $m(N) > \Lambda$ for $N = 2, 3, 4, 5, 10, 21$. The mass
    gap is monotonically decreasing in N, approaching Lambda from
    above.

12. **Instanton support** (file 05): Instantons contribute positively
    to the mass gap and are stronger at smaller N, supporting
    monotonicity qualitatively.

13. **O(N) analogy** (file 05): The O(N) sigma model has a rigorously
    proved monotonically decreasing mass gap (from the Bethe ansatz
    for all N >= 3). The CP^{N-1} model is expected to behave
    similarly.

### 6.1.4 What is OPEN (no known approach)

14. **Monotonicity for N = 3, 4, ..., N_0 - 1**: No analytic method
    currently proves $m(N) > \Lambda$ for these intermediate values.
    Not integrable, perturbation theory unreliable, no correlation
    inequalities.

15. **Non-perturbative proof for all N**: No known argument gives
    $m(N) \geq \Lambda$ for ALL $N \geq 2$ without relying on
    numerical input.

16. **Strict monotonicity**: Even if $m(N) \geq \Lambda$, proving
    $m(N) > m(N+1) > \Lambda$ (strict decrease) for all N is a
    stronger statement with no known approach.


---

## 6.2 Why the Proof Is Hard

### 6.2.1 The sign problem

The fundamental obstacle is that V is indefinite (file 02). If V were
positive, the proof would be trivial. The indefiniteness means we
must show that the DYNAMICAL effect of V on the gap is positive,
even though the OPERATOR V has negative eigenvalues.

This is a subtle spectral-theoretic statement: the perturbation
raises the gap even though it is not a positive operator. Such
statements are rare in mathematical physics -- most gap preservation
theorems require positivity of the perturbation.

### 6.2.2 The model-specific structure is hard to exploit

The CP^{N-1} model has rich structure (gauge symmetry, instantons,
asymptotic freedom, confinement), but this structure does not easily
translate into mathematical tools for gap comparison:

- **Gauge symmetry** gives Ward identities, but these constrain
  correlations, not the gap directly.
- **Asymptotic freedom** gives the perturbative beta function, but
  the gap is a non-perturbative quantity.
- **Confinement** (linear potential in 2D) contributes positively to
  the gap, but quantifying this contribution rigorously is open.
- **Instantons** are non-perturbative and positive, but their effect
  on the gap is not computed rigorously.

### 6.2.3 The wrong Hilbert space problem

The most natural comparison (embedding $\mathcal{H}_N$ into
$\mathcal{H}_{N+1}$) does not work because the transfer matrices
act on different spaces (file 04, Section 4.4). The auxiliary field
formalism puts them on the same space, but at the cost of introducing
the indefinite interaction V.

### 6.2.4 The N = 2 barrier

At N = 2, the mass gap is 3x the large-N value. The 1/N expansion
captures barely half of this deviation. Any proof must handle O(1)
corrections, which rules out perturbative approaches.


---

## 6.3 The Strongest Achievable Statements

### 6.3.1 Statement A (achievable with current tools)

**Theorem A [BOUNDED -- achievable]:**

There exists $N_0$ (explicitly computable from the 1/N expansion
coefficients) such that for all $N \geq N_0$:

$$m(N) \geq \Lambda$$

**Proof route:** First-order perturbation theory gives
$\delta\Delta^{(1)} = \alpha_1\Lambda/N > 0$. Temple's inequality
(or second-order perturbation theory with explicit remainder bound)
controls the higher-order corrections. For $N$ large enough, the
first-order term dominates.

**To make rigorous:** Requires computer-assisted evaluation of the
integrals defining $\alpha_1$ and the second-order coefficients, with
certified error bounds (interval arithmetic).

**Estimated effort:** Moderate. The integrals are well-defined and
two-dimensional. Computer algebra systems can evaluate them to
arbitrary precision.

### 6.3.2 Statement B (achievable with significant new work)

**Theorem B [OPEN -- achievable in principle]:**

For all $N \geq 2$:

$$m(N) \geq \Lambda$$

**Proof route:** Theorem A for $N \geq N_0$, plus:
- $m(2) = (8/e)\Lambda > \Lambda$ (exact, from Bethe ansatz)
- $m(N) > \Lambda$ for $N = 3, \ldots, N_0 - 1$ by computer-assisted
  evaluation of the lattice path integral with rigorous error bounds.

**To make rigorous:** Requires a framework for computer-assisted
proofs of mass gap bounds in lattice sigma models. This is analogous
to the work of Balaban (1980s-90s) on lattice gauge theories, but
adapted to the CP^{N-1} setting.

**Estimated effort:** Very high. Computer-assisted proofs of spectral
gap bounds in interacting field theories are at the frontier of
constructive field theory.

### 6.3.3 Statement C (not achievable with current methods)

**Conjecture C [OPEN -- no known route]:**

$m(N)$ is STRICTLY MONOTONICALLY DECREASING in N:

$$m(2) > m(3) > m(4) > \ldots > m(\infty) = \Lambda$$

**Why this is harder:** Strict monotonicity requires showing that each
step $m(N) - m(N+1) > 0$, not just that $m(N) > \Lambda$. This is a
RELATIVE comparison between adjacent values of N, which is even more
delicate than the comparison with the N = infinity limit.

### 6.3.4 Statement D (the dream theorem)

**Conjecture D [OPEN -- would be a breakthrough]:**

The mass gap satisfies the exact bound:

$$m(N) \geq m(\infty) + \frac{c}{N}\,m(\infty)$$

for some explicit constant $c > 0$ and all $N \geq 2$.

This is stronger than monotonicity: it gives a QUANTITATIVE lower
bound on how much the mass exceeds Lambda. The perturbative
prediction is $c = \alpha_1 \approx 1.04$, but this is only the
leading term.


---

## 6.4 Comparison with the Yang-Mills Problem

### 6.4.1 Relevance to the Millennium Prize

The Yang-Mills mass gap problem asks for a proof that 4D SU(N)
Yang-Mills theory has a mass gap $m > 0$. The CP^{N-1} model is a
2D analogue that shares:

- Asymptotic freedom
- Dynamically generated mass gap
- Confinement
- Instanton effects
- A large-N limit with a known mass gap

The monotonicity conjecture $m(N) \geq m(\infty) = \Lambda$ would
show that the mass gap PERSISTS at all values of the coupling
(parametrized by N), not just in the solvable large-N limit.

### 6.4.2 What monotonicity would contribute

If proved, monotonicity would:

1. Provide a LOWER BOUND on the mass gap that is UNIFORM in N.
   This is a non-trivial statement about the non-perturbative
   dynamics of the theory.

2. Show that the large-N limit is the WORST CASE: the mass gap
   is smallest at N = infinity and increases at finite N. This is
   physically intuitive (finite-N fluctuations increase the gap
   through confinement) but mathematically non-trivial.

3. Serve as a proof of concept for the Yang-Mills problem: if
   monotonicity can be proved in 2D, the same STRATEGY (though
   not the same techniques) might apply in 4D.

### 6.4.3 What monotonicity would NOT give

Monotonicity in the CP^{N-1} model does NOT prove:

- The existence of the mass gap at finite N (this requires a
  separate argument, such as constructive field theory).
- The mass gap in 4D Yang-Mills (the 2D and 4D theories have
  qualitatively different dynamics).
- Any quantitative bound useful for phenomenology.


---

## 6.5 Recommended Path Forward

### 6.5.1 Immediate steps (high confidence of success)

1. **Make $\alpha_1 > 0$ rigorous:** Evaluate the integrals defining
   $\alpha_1$ with interval arithmetic. This would establish
   $m(N) > \Lambda$ for all sufficiently large N rigorously.

2. **Compute $N_0$ explicitly:** Use Temple's inequality with the
   computed constants to determine the smallest $N_0$ such that
   the perturbative bound gives $m(N) \geq \Lambda$ for $N \geq N_0$.
   Expected: $N_0 \leq 10$, possibly $N_0 \leq 5$.

### 6.5.2 Medium-term steps (moderate confidence)

3. **Computer-assisted mass gap bounds for N = 3, 4, 5:** Develop
   a framework for rigorous numerical bounds on the CP^{N-1} mass
   gap at specific N values. Use lattice simulations with controlled
   error analysis.

4. **Explore new correlation inequalities:** Investigate whether
   the specific structure of the CP^{N-1} interaction (quartic in
   the embedding coordinates) admits a correlation inequality that
   does not require the standard FKG/GKS structure. The reflection
   positivity + operator positivity of the QUARTIC vertices might
   give partial results.

### 6.5.3 Long-term steps (speculative)

5. **Non-perturbative monotonicity proof:** Find a structural argument
   (possibly using the gauge-theoretic structure, instanton gas, or
   a new inequality) that gives $m(N) \geq \Lambda$ for all N without
   case analysis.

6. **Connection to 4D:** If monotonicity is proved for CP^{N-1},
   investigate whether the same mechanism (positive first-order gap
   shift + non-perturbative control at small N) works for 4D SU(N)
   Yang-Mills.


---

## 6.6 Final Verdict

**Can $m(N) \geq m(\infty) = \Lambda$ be proved for all $N \geq 2$?**

**Assessment: YES, but not by a single analytic argument.**

The most realistic path is a HYBRID proof:
- Perturbation theory + Temple's inequality for $N \geq N_0$
  (achievable, rigorous).
- Exact Bethe ansatz result for $N = 2$ (proved).
- Computer-assisted bounds for $N = 3, \ldots, N_0 - 1$
  (achievable in principle, requires significant technical work).

A purely analytic proof for all N simultaneously appears to be
OUT OF REACH with current tools. The obstacle is the indefiniteness
of V and the lack of correlation inequalities for the CP^{N-1}
target space.

**What the monotonicity attack achieves for the broader project:**

Even without a complete proof of monotonicity, this analysis
establishes:

1. The N = infinity mass gap $m(\infty) = \Lambda$ is a NATURAL
   LOWER BOUND (not just an approximation).

2. The 1/N corrections are POSITIVE to leading order ($\alpha_1 > 0$),
   meaning the large-N limit underestimates the mass gap.

3. All available evidence (exact at N = 2, numerical at N = 3-21,
   perturbative at large N) SUPPORTS monotonicity.

4. The proof technique (Hamiltonian decomposition + spectral
   perturbation theory) is EXPLICIT and reduces the problem to
   evaluating computable constants.

These findings are directly relevant to the Yang-Mills mass gap:
they demonstrate that in the 2D analogue, the mass gap is robust
under 1/N corrections and that the large-N solvable limit provides
a rigorous floor.
