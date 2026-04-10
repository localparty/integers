# 05. Honest Assessment: Does the Large-N Attack Close the Gap at N = 3?

## The Verdict

**No.** The large-N attack, as developed in files 01--04, does NOT
close the gap at $N = 3$. It provides a compelling physical argument
and narrows the problem to specific mathematical questions, but a
rigorous proof that $m(3) > 0$ in the continuum 2D CP^2 model does
not follow from the techniques explored here.

This file explains exactly where the argument breaks down, what would
fix it, and how the large-N attack relates to the other approaches
in the paper.


---

## 5.1 What the Large-N Attack DOES Achieve

### 5.1.1 A rigorous starting point [PROVED]

The mass gap at $N = \infty$ is established beyond doubt:
- Witten's saddle-point solution: $m = \Lambda_{2D}$ [PROVED]
- Singer's continuum limit: unique, well-defined [PROVED]
- The spectrum, correlators, S-matrix: all computable [PROVED]

This is the strongest rigorous result available for ANY
asymptotically free QFT in the continuum.

### 5.1.2 A well-defined expansion [ESTABLISHED]

The 1/N expansion:
- Expands around the correct (confining) vacuum
- Has UV and IR finite diagrams at every order
- Gives $c_1 \approx 0.89$ at first order [ESTABLISHED]
- Is consistent with all lattice data

### 5.1.3 A clean problem statement

The large-N attack reduces the mass gap question to one of three
precise mathematical problems (any one of which would suffice):

**(P1) Borel summability.** Prove the 1/N expansion of $m/\Lambda$
in the 2D CP^{N-1} model is Borel summable.

**(P2) Uniform bound.** Prove $|m(N)/\Lambda - 1| \leq C/N$ with
$C < 3$.

**(P3) Monotonicity.** Prove $m(N) \geq m(\infty) = \Lambda$ for
all $N \geq 2$.


---

## 5.2 Where the Argument Breaks Down

### 5.2.1 The 1/N expansion is asymptotic, not convergent [PROVED only as asymptotic]

The standard Laplace method gives the 1/N expansion as an ASYMPTOTIC
series. Asymptotic does not imply convergent. We do not know:
- Whether the series converges at $N = 3$
- Whether the Borel sum exists and is unique
- Whether the Borel sum equals the true $m(N)$

### 5.2.2 The bounds are too crude [FATAL at present]

Strategy A (Section 4.2) gives bounds of order $C/N$ with
$C \sim 10^4$, which is useless at $N = 3$. The crudeness comes from:
- Replacing exact integrals by worst-case bounds
- Exponentiating a large correction
- Not using the sign information (the correction is positive)

### 5.2.3 The gauge field is the wild card

The dynamical U(1) gauge field in CP^{N-1} distinguishes it from the
$O(N)$ and Gross-Neveu models (where the 1/N expansion IS Borel
summable, because exact solutions exist). For CP^{N-1}:
- No exact mass formula is known at finite $N$
- The gauge field introduces confinement, which is non-perturbative
- The transition from free particles ($N = \infty$) to bound states
  ($N = 3$) is qualitative, not just quantitative

### 5.2.4 The continuum limit is assumed

Even if $m(3) > 0$ could be proved for the lattice model (at each
lattice spacing $a$), the continuum limit $a \to 0$ requires separate
analysis. Singer's theorem (1995) gives the continuum limit at
$N = \infty$ but not at finite $N$. At $N = 3$, the continuum limit
is part of the problem.


---

## 5.3 Comparison with Other 2D Approaches

The paper identifies three parallel 2D attacks:

### 5.3.1 Large-N (this attack)

- **Strength:** Rigorous starting point at $N = \infty$
- **Weakness:** Cannot reach $N = 3$ rigorously
- **Gap:** Convergence/summability of 1/N series

### 5.3.2 Anomaly approach (2d-attack-anomaly)

- **Strength:** Uses 't Hooft anomaly matching to constrain the
  low-energy theory
- **Weakness:** Anomaly matching gives constraints on the spectrum
  but typically does not prove a mass gap directly
- **Gap:** Anomalies constrain but do not determine

### 5.3.3 Bootstrap approach (2d-attack-bootstrap)

- **Strength:** Uses S-matrix bootstrap / conformal bootstrap to
  bound the spectrum
- **Weakness:** The bootstrap typically gives upper bounds on
  operator dimensions, not lower bounds on mass gaps
- **Gap:** The bootstrap works best for CFTs, and CP^{N-1} is massive

### 5.3.4 Adiabatic continuity (from convergence-synthesis)

- **Strength:** At small compactification radius $L$, the mass gap
  is established semiclassically; adiabatic continuity would extend
  it to large $L$
- **Weakness:** Adiabatic continuity for CP^2 ($N = 3$) is conjectured,
  not proved
- **Gap:** Proving the absence of a phase transition as $L$ varies

### 5.3.5 Comparison table

| Approach | Proves $m > 0$ at $N = \infty$? | Proves $m > 0$ at $N = 3$? | Key gap |
|----------|-------------------------------|---------------------------|---------|
| Large-N | YES | NO | 1/N summability |
| Anomaly | N/A | NO | Constrains but doesn't determine |
| Bootstrap | N/A | NO | Bounds go wrong direction |
| Adiabatic | YES (semiclassical) | NO | Phase transition absence |
| Lattice | YES (Singer) | NO (finite $a$ only) | Continuum limit |


---

## 5.4 What Would Close the Gap

### 5.4.1 The easiest path: monotonicity in N

If someone proves that $m(N)$ is monotonically decreasing as
$N \to \infty$ (with $m(\infty) = \Lambda > 0$), then $m(3) > \Lambda
> 0$ and we are done. This requires:

- A correlation inequality comparing CP^{N_1-1} to CP^{N_2-1} for
  $N_1 < N_2$
- Or a functional inequality on the transfer matrix showing that
  "fewer fields means stronger confinement"

**Feasibility:** The $O(N)$ model has Griffiths-type inequalities
that give monotonicity (Simon 1980). Extending these to CP^{N-1}
(with its gauge field) is a genuine research problem. I assess this
as **feasible but requiring new ideas** (a paper-length argument, not
a routine extension).

### 5.4.2 The exact solution path

If the CP^{N-1} model is integrable at all $N$ (as conjectured), the
exact mass formula from the thermodynamic Bethe ansatz would give
$m(N)$ in closed form. Checking $m(3) > 0$ would then be arithmetic.

**What's needed:**
(a) Prove integrability of the CP^{N-1} sigma model [OPEN --- believed
    true but not proved]
(b) Derive the exact mass formula from the TBA [PARTIALLY done ---
    the TBA equations are known if integrability is assumed]
(c) Verify $m(3) > 0$ from the formula [TRIVIAL once (a) and (b) are
    done]

**Feasibility:** Proving integrability is a major open problem. The
evidence is strong (the classical model is integrable, the quantum
S-matrix satisfies Yang-Baxter, the finite-size spectrum matches TBA
predictions). But a rigorous proof may be out of reach with current
techniques.

### 5.4.3 The combined large-N + lattice path

**Step 1:** Prove $m(N) > 0$ on the lattice for all $N \geq 2$ and all
$\beta > 0$. (This may follow from cluster expansion at strong coupling
and a continuity/no-phase-transition argument.)

**Step 2:** Prove the continuum limit exists at $N = 3$. (This is the
hard step --- it requires controlling the $a \to 0$ limit.)

**Step 3:** Show the continuum mass gap is positive. (If the lattice
gap is bounded below uniformly in $a$, this follows.)

**Feasibility:** Step 1 is plausible (the 2D lattice model is simpler
than the 4D one). Step 2 is the same problem that arises in 4D, but
in 2D the tools are stronger (Balaban-type analysis in 2D is more
tractable). Step 3 follows from Step 2 with a uniform lower bound.

### 5.4.4 The resurgence path

Use the resurgent trans-series structure of the CP^{N-1} model
(developed in path-B-resurgence/) to reconstruct $m(N)$ from its
perturbative and non-perturbative sectors. The trans-series:

$$m(N) = \Lambda\left[\sum_k c_k/N^k
  + e^{-4\pi N/\lambda}\sum_k d_k/N^k
  + e^{-8\pi N/\lambda}\sum_k e_k/N^k + \cdots\right]$$

If the full trans-series is Borel-Ecalle summable (including the
instanton sectors), then $m(N)$ is determined uniquely and can be
evaluated at $N = 3$.

**Feasibility:** Resurgence in 2D sigma models is an active area
(Dunne-Unsal 2012-2016). The technology exists but has not been
applied rigorously to CP^{N-1} at $N = 3$.


---

## 5.5 The Honest Score

### What we know for certain:

1. $m(\infty) = \Lambda > 0$ in the continuum [PROVED]
2. $m(N) > 0$ on the lattice for all $N \geq 2$ at every fixed $a > 0$
   [PROVED numerically, essentially certain]
3. The 1/N expansion gives a systematic, well-defined framework for
   computing corrections to the large-N answer [ESTABLISHED]
4. The first correction is positive: $c_1 > 0$ [ESTABLISHED]
5. All evidence (numerical, analytical, heuristic) supports $m(3) > 0$
   in the continuum [UNANIMOUS]

### What we do NOT know:

1. Whether the 1/N expansion converges at $N = 3$ [OPEN]
2. Whether the 1/N expansion is Borel summable [LIKELY but OPEN]
3. Whether $m(N)$ is monotone in $N$ [LIKELY but OPEN]
4. Whether the continuum limit of the CP^2 model exists at $N = 3$
   [LIKELY but OPEN]
5. Whether the lattice mass gap is bounded below uniformly in $a$ at
   $N = 3$ [LIKELY but OPEN]

### The gap:

The distance between "what we know" and "a proof of $m(3) > 0$" is
NOT large in terms of physics (every physicist believes $m(3) > 0$),
but it IS significant in terms of mathematics. The gap requires either:
- A new inequality (monotonicity in $N$, or a correlation inequality)
- An exact solution (integrability)
- A convergence/summability proof for the 1/N expansion
- A 2D version of constructive QFT (Balaban-type analysis)


---

## 5.6 Relationship to the 4D Mass Gap

Even if we proved $m(3) > 0$ for the 2D CP^2 model, the 4D Yang-Mills
mass gap requires an ADDITIONAL step: connecting the 2D mass gap to the
4D string tension via the worldsheet formula:

$$\sigma_{4D} = \frac{m_{2D}^2}{2\pi}(1 + O(1/N))$$

This formula is [ARGUED] throughout the paper (see path-C-worldsheet/).
Making it rigorous requires proving that the 4D Wilson loop is
dominated by its worldsheet sector --- a statement about 4D gauge
theory, not 2D sigma models.

So the full chain is:

$$\underbrace{m_{2D}(\infty) > 0}_{\text{[PROVED]}}
  \;\xrightarrow{\text{1/N}}\;
  \underbrace{m_{2D}(3) > 0}_{\text{[OPEN]}}
  \;\xrightarrow{\text{worldsheet}}\;
  \underbrace{\sigma_{4D} > 0}_{\text{[OPEN]}}
  \;\xrightarrow{\text{Fredenhagen-Marcu}}\;
  \underbrace{\Delta_{4D} > 0}_{\text{[OPEN, conditional]}}$$

The large-N attack addresses the FIRST arrow. Even if it succeeds,
the second and third arrows remain.


---

## 5.7 Recommendation

The large-N attack should be pursued in conjunction with (not instead
of) the other approaches. Specifically:

1. **Pursue monotonicity in $N$** (Section 4.8): this is the most
   direct path. Correlation inequalities for sigma models on symmetric
   spaces are a well-defined mathematical problem with existing
   techniques ($O(N)$ Griffiths inequalities as a template). A positive
   result here would immediately give $m(3) > 0$.

2. **Pursue integrability** (Section 5.4.2): if the CP^{N-1} model can
   be proved integrable, the exact mass formula settles the question.
   This is harder but has broader implications.

3. **Do NOT abandon the large-N expansion:** Even if it does not close
   the gap by itself, the 1/N framework provides the STRUCTURE for
   understanding the finite-N answer. Any proof of $m(3) > 0$ will
   almost certainly use the large-N expansion as a guiding framework,
   even if the rigorous argument uses different tools.

4. **The 2D problem is the right problem:** All three paths in the
   paper (path-A-multiscale-rg, path-B-resurgence, path-C-worldsheet)
   converged on the 2D CP^{N-1} model as the key. The large-N attack
   is the most natural approach to this 2D problem. Even though it does
   not (yet) close the gap, it identifies the precise obstacles and
   suggests concrete strategies for overcoming them.
