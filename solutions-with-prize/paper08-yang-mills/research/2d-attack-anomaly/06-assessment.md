# 06. Honest Assessment: Can Anomaly Matching Prove Adiabatic Continuity?

## I. The Verdict

**No. Anomaly matching alone cannot prove that the
$\mathbb{Z}_3$-twisted $\mathbb{CP}^2$ model has no phase
transition as a function of $L$.**

The reason is structural, not technical: the mixed 't Hooft
anomaly between $\mathbb{Z}_3^{(C)}$ and $\mathbb{Z}_3^{(\chi)}$
constrains the IR to break at least one of the two symmetries,
but it cannot determine WHICH one breaks. Both the confining
phase (center preserved, chiral broken) and the deconfining phase
(center broken, chiral preserved) are anomaly-consistent.


---

## II. What the Anomaly Approach DID Achieve

Despite falling short of a proof, the anomaly analysis produced
concrete, rigorous results:

### II.1 Proved results

**(P1)** The mixed 't Hooft anomaly between $\mathbb{Z}_3^{(C)}$
and $\mathbb{Z}_3^{(\chi)}$ exists and has anomaly coefficient
$p = 1 \in \mathbb{Z}_3$. [Derived by three independent methods:
operator algebra, background gauge fields, anomaly inflow]

**(P2)** In any gapped phase, at least one of
$\{\mathbb{Z}_3^{(C)}, \mathbb{Z}_3^{(\chi)}\}$ must be
spontaneously broken. A trivially gapped symmetric vacuum is
IMPOSSIBLE. [Direct consequence of the anomaly]

**(P3)** The UV phase (small $L$) has $\mathbb{Z}_3^{(C)}$
preserved and $\mathbb{Z}_3^{(\chi)}$ broken, with the anomaly
matched by chiral symmetry breaking. [Semiclassical computation]

**(P4)** The anomaly is $L$-independent (it is a topological
invariant of the theory). [Trivial but important]

**(P5)** Any phase transition must swap the role of the two
$\mathbb{Z}_3$ symmetries (from $\chi$-broken to $C$-broken).
A transition to a fully symmetric gapped phase is forbidden.
[From the anomaly]

### II.2 Sharp constraints

**(C1)** The only anomaly-consistent alternative to adiabatic
continuity is a phase transition where $\mathbb{Z}_3^{(C)}$
breaks and $\mathbb{Z}_3^{(\chi)}$ restores. This is a VERY
specific scenario (not a vague "something could go wrong").

**(C2)** Such a transition would have to be first-order (since
both phases are gapped, a continuous transition would require
passing through a gapless point, which is non-generic in the
absence of fine-tuning).

**(C3)** The transition would have to be reversed at large $L$
(since the $L \to \infty$ limit matches the small-$L$ pattern:
$\chi$-broken). This means TWO transitions, not one.


---

## III. Why the Anomaly Is Insufficient: The Structural Reason

### III.1 The general principle

A mixed 't Hooft anomaly between $\mathbb{Z}_N^{(1)}$ and
$\mathbb{Z}_N^{(2)}$ tells you: "at least one must break."
It does NOT tell you which one. This is because the anomaly
is symmetric under the exchange
$\mathbb{Z}_N^{(1)} \leftrightarrow \mathbb{Z}_N^{(2)}$
(up to conjugation of the anomaly class).

For the anomaly to DETERMINE which symmetry breaks, you would
need either:
- An asymmetric anomaly (one that involves only one of the two
  symmetries -- but a mixed anomaly by definition involves both)
- Additional anomalies that lift the degeneracy
- A dynamical argument beyond the anomaly

### III.2 Comparison with cases where anomalies DO suffice

**Case 1: Massless QCD.** The chiral anomaly $SU(N_f)_L \times
SU(N_f)_R \to SU(N_f)_V$ combined with the 't Hooft anomaly
matching conditions (matching the UV free quark anomaly) is
SUFFICIENT to prove chiral symmetry breaking when $N_f$ is
small. [This is the original 't Hooft argument, 1980.]

Why does it work there? Because there is only ONE continuous
symmetry group, and the anomaly constrains how it can be
realized. There is no "swap" option.

**Case 2: The Lieb-Schultz-Mattis theorem.** In 1D quantum
spin chains, a mixed anomaly between translation symmetry and
spin rotation rules out a trivially gapped symmetric state.
The theorem proves either symmetry breaking or gaplessness.

Why does it work there? The anomaly involves translation
symmetry, which has a preferred direction (it cannot be
spontaneously broken in 1D by the Mermin-Wagner theorem).
So the anomaly must be matched by the OTHER symmetry breaking
or by gaplessness.

**Lesson.** Anomaly matching proves SSB when there is an
ASYMMETRY between the two symmetries -- one cannot break
(by dimension, by another theorem, etc.), forcing the other
to break. In our problem, BOTH $\mathbb{Z}_3$ symmetries
can break, so the anomaly is insufficient.

### III.3 Is there an asymmetry we are missing?

Could there be an additional constraint that prevents
$\mathbb{Z}_3^{(C)}$ from breaking?

**(a) Mermin-Wagner?** In 2D, CONTINUOUS symmetries cannot
break spontaneously (Mermin-Wagner-Coleman theorem). But
$\mathbb{Z}_3$ is DISCRETE -- Mermin-Wagner does not apply.
Discrete symmetries CAN break in 2D.

**(b) Elitzur's theorem?** Elitzur's theorem prevents LOCAL
(gauge) symmetries from breaking. Center symmetry is a
GLOBAL symmetry (it acts on the boundary conditions, not
the local fields). Elitzur's theorem does not apply.

**(c) Positivity / reflection positivity?** Reflection
positivity gives correlation inequalities but (as analyzed in
05-no-phase-transition.md, Section V) does not constrain the
sign of $\langle P \rangle$ sufficiently.

**(d) Index theorems?** The Witten index $\text{Tr}(-1)^F$
is a powerful tool in supersymmetric theories but is not
directly applicable here (no supersymmetry).

**Conclusion: No known theorem prevents $\mathbb{Z}_3^{(C)}$
from breaking. The anomaly alone is insufficient.**


---

## IV. What Would Complete the Proof

### IV.1 Minimal additional input needed

The anomaly provides the framework; the missing piece is a
DYNAMICAL input that selects the confining phase over the
deconfining phase. Specifically, we need ONE of:

**(A) A bound on the center vortex free energy.**
Show $F_v(L) > 0$ for all $L$. This would directly prove
$\mathbb{Z}_3^{(C)}$ preservation.

Difficulty: requires non-perturbative control at strong
coupling ($L \sim 1/\Lambda$).

**(B) A monotonicity principle.**
Show that the domain wall tension $T_{\text{DW}}(L)$
(which separates center sectors) is monotonically decreasing
from $\infty$ (at $L = 0$) to $\Lambda$ (at $L = \infty$),
hence always positive.

Difficulty: requires an inequality relating $T_{\text{DW}}$
at different $L$, which is a new result.

**(C) Finite-$N$ error bounds on the large-$N$ expansion.**
Show that the $1/N$ corrections to the center vortex free
energy are bounded: $|F_v^{(1)}(L)| < c$ uniformly in $L$,
with $c < N \cdot F_v^{(0)}(L)$.

At $N = 3$: need $|F_v^{(1)}| < 3 F_v^{(0)}$ for all $L$.
This is a quantitative bound on the $1/N$ expansion.

Difficulty: quantitative control of the $1/N$ expansion for
the $\mathbb{CP}^{N-1}$ model is available from the exact
$1/N$ solution (D'Adda-Luscher-Di Vecchia 1978, Witten 1979)
but the center vortex free energy has not been computed at
$O(1/N)$.

**(D) Extension of the CP$^1$ proof to CP$^2$.**
The $N = 2$ proof (Dunne-Unsal 2012) uses integrability of
the $O(3)$ sigma model. Find an analogous non-perturbative
tool for $N = 3$.

Candidates:
- The $\mathbb{CP}^2$ model is related to the $SU(3)/U(1)^2$
  flag manifold sigma model, which has some integrable structure
  (the Bykov model, 2014). Can this be exploited?
- The $1/N$ expansion of the $\mathbb{CP}^{N-1}$ model
  resums certain non-perturbative effects. Can it be made
  rigorous at $N = 3$?

**(E) A new anomaly involving higher-form or non-invertible
symmetries.** Recent developments (Gaiotto-Kapustin-Seiberg-
Willett 2015, Cordova-Dumitrescu-Intriligator 2019, Choi et al.
2022) have identified new types of symmetries (higher-form,
non-invertible) with their own anomalies. If the $\mathbb{CP}^2$
model has an additional anomaly that ONLY the confining phase
can match, the proof would be complete.

**This is the most promising purely-anomaly-based approach.**
I analyze it below.


### IV.2 Could non-invertible symmetries close the gap?

The $\mathbb{CP}^{N-1}$ model at $\theta = \pi$ has a
$\mathbb{Z}_2$ time-reversal symmetry that becomes non-invertible
at the quantum level (Komargodski-Ohmori-Roumpedakis-Seifnashri
2021). But we work at $\theta = 0$, where time-reversal is
standard.

At $\theta = 0$: the $\mathbb{CP}^2$ model has a topological
symmetry associated with the $\pi_2(\mathbb{CP}^2) = \mathbb{Z}$
winding number. In the $\mathbb{Z}_3$-twisted theory, this
becomes a $\mathbb{Z}_3$ topological symmetry (fractional
winding).

**Does this give a new anomaly?** The fractional topological
symmetry is related to the 1-form symmetry of the parent gauge
theory. In the $\mathbb{CP}^{N-1}$ model, there is a
$\mathbb{Z}_N$ 0-form topological symmetry (shifting $\theta$
by $2\pi/N$) that is already identified as $\mathbb{Z}_3^{(\chi)}$.

I do not find a genuinely NEW anomaly from non-invertible
symmetries at $\theta = 0$. The known anomaly structure at
$\theta = 0$ is exhausted by the mixed
$\mathbb{Z}_3^{(C)} \times \mathbb{Z}_3^{(\chi)}$ anomaly.

**Assessment: Non-invertible symmetries at $\theta = 0$ do
not appear to provide additional constraints beyond the known
mixed anomaly. This avenue is UNLIKELY TO HELP (but I cannot
fully exclude it without a complete classification of
generalized symmetries for the $\mathbb{CP}^2$ model).**


---

## V. Ranking the Paths Forward

In order of promise:

### Rank 1: Compute $F_v^{(1)}(L)$ at $O(1/N)$ and bound it

The large-$N$ solution is rigorous. The $1/N$ correction to
the center vortex free energy is in principle computable from
the exact $1/N$ propagator. If $F_v^{(1)}(L)$ is bounded
uniformly in $L$, and the bound is smaller than $3 F_v^{(0)}(L)$,
adiabatic continuity follows for $N = 3$.

**Why this is promising:** It combines the rigorous large-$N$
machinery with the specific physics of the center vortex. It
requires a calculation, not a new idea.

**What it requires:** Computing the center vortex free energy
in the $\mathbb{CP}^{N-1}$ model at $O(1/N)$. This is a
definite (hard but doable) computation.

### Rank 2: Domain wall tension monotonicity

Show $T_{\text{DW}}(L)$ is monotone decreasing. This requires
a new inequality, possibly from reflection positivity or
stochastic quantization.

**Why this is promising:** It would be a clean, general result
applicable to all $N$.

**What it requires:** A new inequality. No obvious candidate.

### Rank 3: Extend the Bykov integrable structure

The Bykov model (2014) is an integrable deformation of the
flag manifold sigma model $SU(N)/U(1)^{N-1}$. The
$\mathbb{CP}^{N-1}$ model is a special case (or a limit) of
the flag manifold model. If the integrable structure extends
to control the center vortex, it could replace the Bethe ansatz
used for $N = 2$.

**Why this is promising:** It would give exact results for
all $N$, not just $N = 2$.

**What it requires:** Significant new developments in
integrable systems. Long-term.

### Rank 4: New generalized anomaly

Find a previously unidentified anomaly (involving non-invertible
symmetries, higher-group structure, or anomalies of the
$\mathbb{Z}_3$ 1-form symmetry in a UV completion) that
distinguishes the confining from the deconfining phase.

**Why this is promising:** If it exists, it would give a
purely structural proof with no calculations.

**What it requires:** A conceptual breakthrough. The current
classification of anomalies for the $\mathbb{CP}^2$ model at
$\theta = 0$ does not seem to contain such an anomaly.


---

## VI. The Bottom Line

### VI.1 For the mass gap problem

The anomaly approach to the 2D $\mathbb{CP}^2$ problem does
NOT currently provide a proof of adiabatic continuity. It
provides the strongest CONSTRAINTS on the IR phase (ruling out
a trivially gapped symmetric vacuum, requiring a specific form
for any phase transition) but cannot select the confining phase
over the deconfining phase.

### VI.2 For the overall program

Connecting to the broader project (Path B in 32-three-paths.md):

The 2D $\mathbb{CP}^2$ model appears as the worldsheet theory
of the confining string in the 4D KK theory. Proving adiabatic
continuity in 2D (no phase transition as $L$ varies) would
establish that the 2D model has a mass gap at ALL $L$, which
would in turn give the 4D string tension via
$\sigma_{\text{4D}} = m_{2D}^2/(2\pi)$.

The anomaly approach narrows the gap but does not close it.
The most concrete path forward is to compute $F_v^{(1)}(L)$
at $O(1/N)$ and check whether the bound is sufficient for
$N = 3$.

### VI.3 What we should state in the paper

**Honest claim:** "The mixed 't Hooft anomaly between
$\mathbb{Z}_3^{(C)}$ and $\mathbb{Z}_3^{(\chi)}$ in the
$\mathbb{Z}_3$-twisted $\mathbb{CP}^2$ model forbids a
trivially gapped phase at any compactification radius $L$.
Combined with semiclassical analysis at small $L$, large-$N$
solvability, integrability at $N = 2$, and lattice evidence,
this provides strong support for adiabatic continuity (no
phase transition). However, a rigorous proof for $N = 3$
requires additional input beyond anomaly matching."

This is an honest, precise statement. It does not overclaim.


---

## VII. Open Problems (Concrete and Attackable)

1. **Compute $F_v^{(1)}(L)$:** the $O(1/N)$ correction to
   the center vortex free energy in the $\mathbb{Z}_3$-twisted
   $\mathbb{CP}^2$ model. This is a definite calculation in
   the $1/N$ expansion.

2. **Prove $T_{\text{DW}}(L)$ monotonicity:** find an
   inequality (possibly from stochastic quantization or
   FKG-type correlation inequalities) that bounds the domain
   wall tension from below.

3. **Classify generalized symmetries** of the $\mathbb{CP}^2$
   model at $\theta = 0$, including non-invertible symmetries.
   Determine whether any NEW anomaly exists beyond the known
   $\mathbb{Z}_3 \times \mathbb{Z}_3$ mixed anomaly.

4. **Extend the Dunne-Unsal $N = 2$ proof:** identify what
   specific property of the $O(3)$ model (integrability?
   self-duality? something else?) makes the proof work, and
   find an analogue for $N = 3$.

5. **Lattice computation of $F_v(L)$:** simulate the
   $\mathbb{Z}_3$-twisted $\mathbb{CP}^2$ model on the lattice
   and measure the center vortex free energy as a function of
   $L$. Confirm positivity at all $L$.
