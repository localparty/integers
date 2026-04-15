# 07. What Works, What Doesn't, and New Ideas

## The Honest Balance Sheet

Having worked through the worldsheet bootstrap in detail (Sections 01-06),
I can now give an honest assessment of where it stands.


---

## 7.1 What Works

**W1. The separation of problems.** [WORKS]

The worldsheet bootstrap genuinely separates the continuum limit into
two parts:
- Part 1: What is $\sigma_\infty$? (Answered by the 2D model.)
- Part 2: Does the lattice converge to it? (A question about
  approximation.)

This separation is logically sound and conceptually valuable, regardless
of whether either part is fully proved.

**W2. The 2D model is far better controlled.** [WORKS]

The 2D $\mathbb{CP}^{N-1}$ model has:
- An exact solution at $N = \infty$ [PROVED]
- A proven mass gap at $N = \infty$ [PROVED]
- A proven continuum limit at $N = \infty$ [PROVED]
- High-precision lattice data at all $N$ [PROVED numerically]
- Rigorous construction technology (Gawedzki--Kupiainen) available

None of these are available in 4D. The worldsheet bootstrap leverages
2D tools for a 4D problem.

**W3. The symmetry argument is robust.** [WORKS]

The identification of the worldsheet theory as the $\mathbb{CP}^{N-1}$
sigma model follows from:
- The gauge group $SU(N)$
- The symmetry breaking pattern $SU(N) \to S(U(1) \times U(N-1))$
- The uniqueness of the two-derivative sigma model

These are rigorous mathematical facts. The worldsheet theory is
UNIQUELY determined by symmetry, not by a specific calculation.

**W4. The large-$N$ case is promising.** [WORKS]

At $N = \infty$, every ingredient is available:
- Exact 2D solution (Witten)
- Proven 2D continuum limit (Singer)
- Master field (Witten 1980)
- Eguchi--Kawai reduction
- Matrix model technology

A rigorous proof at $N = \infty$ is within reach.

**W5. The predictions are testable.** [WORKS]

The worldsheet bootstrap makes specific predictions:
- Luscher coefficient $\pi/6$ (not $\pi/12$)
- Glueball mass ratios from $\mathbb{CP}^{N-1}$ eigenvalues
- String tension $\sigma = f(N) m_{2D}^2$ (computable function)

These can be checked against existing lattice data.


---

## 7.2 What Doesn't Work

**D1. The worldsheet derivation is not rigorous.** [DOES NOT WORK, yet]

The derivation of the worldsheet action (Section 01) is at the [ARGUED]
level. The missing rigor is:
- The existence of a well-defined thin-string limit
- The proof that the holonomy correspondence gives the correct worldsheet
  theory at the quantum level
- The control of higher-derivative corrections

This is the single biggest obstacle. Everything else follows IF the
worldsheet description is established.

**D2. The numerical matching is imprecise at $N = 3$.** [PARTIALLY WORKS]

The formula $\sigma = m_{2D}^2/(2\pi)$ gives $\sqrt{\sigma} \approx 323$
MeV, versus the experimental 440 MeV (Section 03.5). The 27% discrepancy
is explained by $O(1/N)$ corrections and normalization issues, but it
is not sharp enough to be a "prediction" --- it is more of a consistency
check.

**D3. The lattice convergence is as hard as ever.** [DOES NOT WORK, yet]

The worldsheet bootstrap does not solve the lattice convergence problem
(Section 06). It reframes the problem (from "does $\sigma_\infty$ exist?"
to "does the lattice converge to the known target?") but does not
provide a proof of convergence.

**D4. The regime $a \lesssim r_3$ is still problematic.** [DOES NOT WORK]

The cluster expansion fails for $a \lesssim r_3$ (the lattice spacing is
smaller than the $\mathbb{CP}^{N-1}$ radius). In this regime, the KK
modes are light and the theory effectively becomes higher-dimensional.
The worldsheet description does not directly help here because the
worldsheet emerges from the KK structure, which is not resolved at
$a \lesssim r_3$.

However, this regime is also where the theory should transition from
the KK description to the standard 4D description. The standard 4D
lattice theory at $a \lesssim r_3$ does not know about the
$\mathbb{CP}^{N-1}$, so the continuum limit (if it exists) must be
independent of the KK structure. This is a universality statement, not
a KK statement.


---

## 7.3 Dead Ends Encountered

**Dead end 1: Direct identification of the free energy.**

I tried (Section 03.2) to derive $\sigma = m^2/(2\pi)$ by computing
the worldsheet free energy density. This leads to UV-divergent
expressions that need renormalization. The relationship between the
renormalized free energy and the string tension is scheme-dependent,
making the derivation unreliable for precise numerics. The formula
$\sigma = m^2/(2\pi)$ is better understood as a STRUCTURAL relation
(proportionality) than as a precise numerical identity.

**Dead end 2: Monotonicity of the string tension.**

I tried (Section 06.4) to prove that $\sigma_{\text{phys}}(a)$ is
monotone in $a$. This fails: the Symanzik corrections have variable
sign, and the lattice data show non-monotone approach to the continuum
limit. Monotonicity is too strong; quasi-monotonicity might work but
requires the multi-scale RG estimates that are themselves open.

**Dead end 3: Using integrability of the 2D model directly.**

The 2D $\mathbb{CP}^{N-1}$ model is believed to be integrable, with
an exact S-matrix. I tried to use this integrability to compute the
string tension exactly. But integrability gives the 2D S-matrix, not
the 4D string tension. The connection between the two requires the
worldsheet formula, which brings us back to the original problem.


---

## 7.4 New Ideas

Despite the obstacles, the exploration has generated several new ideas
that go beyond the original sketch in Section 32.

**Idea 1: The bootstrapped Eguchi--Kawai.** [NEW]

At $N = \infty$, combine the Eguchi--Kawai reduction with the worldsheet
description:
1. The EK reduction maps the 4D theory to a matrix model [PROVED at
   $N = \infty$ with center stabilization]
2. The matrix model's Wilson loop is computed by saddle-point methods
   [PROVED at $N = \infty$]
3. The saddle-point equation for the Wilson loop is a 2D field equation
   --- identify it with the $\mathbb{CP}^{N-1}$ sigma model's equation
   of motion [OPEN but concrete]

This gives a precise mathematical problem: show that the EK matrix
model saddle-point equation, restricted to the Wilson loop sector, is
equivalent to the Witten saddle-point equation for the $\mathbb{CP}^{N-1}$
model. Both are explicit equations involving integrals and eigenvalue
distributions. The equivalence should be checkable.

**Idea 2: The interpolating model.** [NEW]

Construct a one-parameter family of theories that interpolates between
the 2D $\mathbb{CP}^{N-1}$ model and the 4D KK gauge theory:

$$S_t = (1-t) \times S_{2D}[\text{CP}^{N-1}]
  + t \times S_{4D}[\text{YM on } M^4 \times \mathbb{CP}^{N-1}]$$

for $t \in [0, 1]$. At $t = 0$: the pure 2D sigma model (mass gap
proved). At $t = 1$: the full 4D KK theory (mass gap proved on the
lattice).

If the mass gap is continuous in $t$ and positive at both endpoints,
it is positive for all $t$. The intermediate values trace out how the
2D mass gap deforms into the 4D string tension. The continuity follows
if the interpolation does not cross a phase transition.

**Obstacle:** The interpolation is between a 2D and a 4D theory, which
requires embedding the 2D model in the 4D theory. The worldsheet
provides this embedding, but making it rigorous requires the same
worldsheet derivation (Section 01) that we are trying to prove.

**Idea 3: Testing the Luscher prediction with existing data.** [NEW,
CONCRETE]

The worldsheet predicts $c = 2$ for the effective central charge (the
Luscher coefficient is $\pi/6$ instead of $\pi/12$). Current lattice
data give $c \approx 1$ with $\sim 20$--$30\%$ errors.

A DEFINITIVE test would:
(a) Compute the Luscher term on the lattice at multiple values of $N$
(b) Check whether $c$ depends on $N$ (the worldsheet predicts $c = 2$
    for ALL $N \geq 2$; Nambu--Goto predicts $c = 1$ for all $N$)
(c) Use improved actions and large volumes to reduce the statistical
    error below 10%

If the lattice data confirm $c = 2$, this would be strong evidence for
the worldsheet description, even without a rigorous proof. If the data
give $c = 1$ (Nambu--Goto), the worldsheet description is WRONG and the
entire Path C collapses.

This is a falsifiable prediction that can be tested with EXISTING
technology. It should be the first priority for numerical validation.

**Idea 4: The two-step continuum limit.** [NEW]

Instead of taking $a \to 0$ in one shot, do it in two steps:

*Step 1:* Take $a \to 0$ with $r_3$ fixed. In this limit, the
$\mathbb{CP}^{N-1}$ geometry is unresolved ($a \ll r_3$ does not happen
in this step). The cluster expansion is valid, and $\sigma_{\text{phys}}(a)
> 0$ at each step. The limit (if it exists) is a continuum theory on
$M^4 \times \mathbb{CP}^{N-1}$ at some specific $r_3$.

*Step 2:* Take $r_3 \to 0$ (decompactification of the internal space).
In this limit, the $\mathbb{CP}^{N-1}$ shrinks to a point and the
theory becomes purely 4D. The string tension should remain positive
because the topological obstruction persists at all $r_3 > 0$.

The virtue of this approach: Step 1 is within the regime where the
cluster expansion works ($a \gg r_3$), so the convergence might be
provable. Step 2 is a new problem (decompactification), but it has a
clear physical picture: as $r_3 \to 0$, the KK modes become infinitely
heavy, and the theory reduces to pure 4D YM.

**Obstacle:** In Step 2, the string tension $\sigma(r_3) = 3g_3^2/
(8\pi^2 r_3^2)$ depends explicitly on $r_3$. As $r_3 \to 0$ with
$g_3^2$ fixed: $\sigma \to \infty$. This is not what we want --- we
need $g_3^2$ to also vanish as $r_3 \to 0$, following the RG flow.
The correct limit is $r_3 \to 0$ with $\Lambda_{\text{QCD}}$ held
fixed, which requires $g_3^2(r_3) \to 0$ at the asymptotically free
rate.

This is essentially the same as the standard continuum limit, just
rewritten in terms of $r_3$ instead of $a$. It is not clear that the
two-step approach gives any advantage over the one-step limit.

**Idea 5: Relative convergence.** [NEW, potentially useful]

Instead of proving absolute convergence ($\sigma_{\text{phys}}(a) \to
\sigma_\infty$), prove RELATIVE convergence: the RATIO of the 4D and
2D mass gaps converges:
$$\frac{\sigma_{\text{phys}}(a)}{m_{2D}(a_{\text{eff}}(a))^2} \to f(N)
  \quad (a \to 0)$$

The 2D mass gap $m_{2D}(a_{\text{eff}})$ is computed on the effective
2D lattice induced by the 4D lattice. The RATIO might be easier to
control than the individual quantities because:
- UV divergences cancel in the ratio (both $\sigma$ and $m^2$ diverge
  at the lattice level, but their ratio is UV-finite)
- The ratio is a dimensionless function of the dimensionless lattice
  coupling, not of the dimensionful lattice spacing
- At $N = \infty$, the ratio should be computable exactly

**Idea 6: The string--lattice duality.** [SPECULATIVE]

At the deepest level, what the worldsheet bootstrap is trying to do is
establish a STRING--LATTICE DUALITY: the 4D lattice theory (on one
side) is dual to the 2D worldsheet theory (on the other side). The
duality maps:
- 4D string tension $\leftrightarrow$ 2D mass gap
- 4D lattice spacing $\leftrightarrow$ 2D lattice spacing
- 4D continuum limit $\leftrightarrow$ 2D continuum limit

If such a duality could be established rigorously (even at $N = \infty$),
it would be a mathematical theorem of independent interest, connecting
lattice gauge theory to 2D sigma models.

In the supersymmetric context, such dualities ARE proved (via
Maldacena's AdS/CFT and its lattice versions). The non-supersymmetric
version needed here is harder, but the $\mathbb{CP}^{N-1}$ structure
(which is NOT present in generic gauge theories) provides additional
constraints that might make a proof possible.


---

## 7.5 Assessment of Path C Overall

**What Path C achieves:**

1. A DEFINITION of $\sigma_\infty$ independent of the lattice:
   $\sigma_\infty = f(N) m_{2D}^2$. [ARGUED]

2. A FRAMEWORK for proving the continuum limit: reduce to 2D + lattice
   approximation. [ARGUED]

3. A TESTABLE PREDICTION: $c = 2$ Luscher coefficient. [ARGUED]

4. A CONCRETE PROGRAM for the large-$N$ case: Eguchi--Kawai +
   Witten solution. [ARGUED]

5. A QUANTITATIVE prediction for $\sigma$ in terms of known 2D data.
   [ARGUED, with $O(30\%)$ accuracy at $N = 3$]

**What Path C does NOT achieve:**

1. A PROOF of the worldsheet description (the key missing step).

2. A PROOF of the lattice convergence (still requires multi-scale RG or
   equivalent).

3. PRECISE numerics at $N = 3$ (the $1/N$ corrections are large).

**Comparison with Paths A and B:**

- Path A (Multi-scale RG) is the most mathematically rigorous approach
  but requires the hardest technical work (Balaban-type estimates at
  each scale).

- Path B (Resurgence) is the most elegant but depends on unproved
  conjectures about resurgent trans-series in the undeformed model.

- Path C (Worldsheet) is the most CONCRETE: it identifies a specific
  target $\sigma_\infty$, makes testable predictions, and has a clear
  program for the large-$N$ case. But it rests on the unproved
  worldsheet description.

**My overall assessment:**

Path C is the most promising for IDENTIFYING $\sigma_\infty$ (telling
us what the answer is). Path A is the most promising for PROVING
convergence (showing the lattice gets to the answer). The ideal approach
combines both: use Path C to define the target, and Path A to prove
convergence to it.


---

## 7.6 The Proposed Program

Based on the exploration in Sections 01-06, here is the concrete program
for the worldsheet bootstrap:

**Phase 1 (Immediate, testable):**
- Compute the Luscher coefficient on the lattice with improved precision
  at $N = 2, 3, 4, 6$ and check whether $c = 1$ (Nambu--Goto) or
  $c = 2$ (worldsheet). This is a clear GO/NO-GO test.
- Compute the 2D $\mathbb{CP}^{N-1}$ mass gap at $N = 3$ with improved
  precision (this is a standard 2D lattice calculation, much cheaper
  than 4D).

**Phase 2 (Large-$N$ proof):**
- Prove the worldsheet formula at $N = \infty$ by connecting the EK
  matrix model to the Witten saddle point (Idea 1).
- This requires: (a) establishing center-symmetric EK for the Wilson
  loop, (b) solving the EK saddle-point equation, (c) matching to
  the Witten solution.

**Phase 3 ($1/N$ expansion):**
- Establish the $1/N$ expansion of the worldsheet formula:
  $\sigma(N) = f(N) m(N)^2$ with $f(N)$ computable order by order.
- Prove Borel summability of the $1/N$ expansion (or at least show
  it is asymptotic with controlled remainders at $N = 3$).

**Phase 4 (Lattice convergence):**
- Combine the worldsheet (defining $\sigma_\infty$) with the multi-scale
  RG (proving convergence) to complete the proof.
- This is the hardest phase and may require new mathematical technology.


---

## 7.7 The One-Paragraph Summary

The worldsheet bootstrap derives the confining string's worldsheet
theory from the $\mathbb{CP}^{N-1}$ topology and identifies the 4D
string tension with the 2D sigma model mass gap: $\sigma = f(N) m_{2D}^2$.
This defines a positive, computable target for the continuum limit and
reduces the 4D problem to a 2D problem that is better controlled (exactly
solvable at $N = \infty$, numerically known at all $N$, with a rigorous
continuum limit for the related $O(N)$ model). The approach makes a
testable prediction (Luscher coefficient $\pi/6$) and has a concrete
program for the large-$N$ case (Eguchi--Kawai + Witten). The main
obstacles are: (1) making the worldsheet derivation rigorous, and
(2) proving that the lattice converges to the worldsheet prediction.
Both are open, but the worldsheet bootstrap provides the clearest
identification of what the continuum limit IS --- the remaining question
is whether the lattice reaches it.
