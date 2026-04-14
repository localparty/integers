# §30 — No Carathéodory-Fejér Stabilization Needed

*Paper 49, Part VI: Comparison with CCM. CCM uses Carathéodory-Fejér
stabilization to guarantee self-adjointness of the finite-$N$
matrices. Paper 49 gets self-adjointness from functional calculus on
$\Delta$. The distinction is structural, not cosmetic.*

---

## What Carathéodory-Fejér stabilization is

The Carathéodory-Fejér (CF) problem asks: given a Laurent polynomial
$p(z) = \sum_{|k| \leq N} c_k z^k$, find the best rational
approximation to $p$ on the unit circle with a specified
denominator degree. The solution involves the singular-value
decomposition of a Hankel matrix and produces a rational function
whose error is "flat" on the circle (the maximum error is
equi-oscillating).

In numerical analysis, CF approximation is used to produce rational
functions that decay rapidly off-circle. The CF decay constant
$\rho$ — the ratio of successive eigenvalues of the relevant Hankel
operator — controls how fast the approximation error decays as the
degree increases.

## How CCM uses CF

In CCM's construction, the operator $D_N$ is built as a specific
matrix in the PSWF basis, *modulo a CF-stabilization step*. Without
stabilization, the direct matrix elements would yield an operator
that is self-adjoint in the continuous limit but not self-adjoint at
finite $N$. CF stabilization adds a rank-1 correction that makes
$D_N$ self-adjoint at each $N$.

The stabilization is essential for CCM's machinery because:

1. Self-adjointness of $D_N$ at finite $N$ is needed to apply
   standard spectral theory (real spectrum, functional calculus,
   spectral theorem).
2. CF provides a quantitative decay rate $\rho \geq 4.27$ (Paper 13
   research/35 verified this constant numerically for $N = 5$ to
   $30$), giving uniform control of the stabilization correction.
3. The correction is small enough ($O(\rho^{-N})$) that it doesn't
   disturb the limit spectrum.

The procedure is rigorous. But it is also *imposed*: self-
adjointness is added by hand, not derived from the construction's
own structure.

## How Paper 49 achieves self-adjointness

Paper 49's $D$ is self-adjoint *automatically*, by functional
calculus. The argument has three lines:

1. $\Delta$ is positive and self-adjoint on $H_{\omega_1}$ (Tomita-
   Takesaki, classical 1970). "Positive" means $\Delta = \Delta^* \geq
   0$ in the quadratic-form sense; "self-adjoint" means $\Delta =
   \Delta^{**}$ as unbounded operators on the maximal domain.
2. Since $\Delta > 0$, we can form $\log \Delta$ via the Borel
   functional calculus: $\log \Delta := \int_0^\infty (\log \lambda)
   dE_\Delta(\lambda)$, where $dE_\Delta$ is the spectral measure.
   $\log \Delta$ is self-adjoint on its maximal domain (real-valued
   Borel function of a self-adjoint operator yields a self-adjoint
   operator; Reed-Simon Vol I §VIII).
3. Multiplication by $-i$ composes with the restriction to the
   even-parity sector $H_R$. On $H_R$, the modular conjugation $J$
   acts as complex conjugation (§12), so the multiplication by $-i$
   and the real-spectrum condition combine consistently. The result
   $D = -(2/\pi^2) i \log \Delta|_{H_R}$ is self-adjoint.

No rank-1 correction is added. No stabilization step is performed.
Self-adjointness is a theorem, not an imposition.

## Why the distinction matters

One might argue: "CF is a minor technical detail. If it makes the
finite-$N$ operator self-adjoint, fine — the limit is the same
either way." This argument has merit for numerical verification
(both routes arrive at the same $D_\infty$), but it misses a
structural point.

**When self-adjointness is imposed, it becomes a property that must
be re-established in every generalization.** If one wants to extend
Paper 13 (RH over $\mathbb{Q}$) to Paper 13b (GRH over a character
twist), one must redo the CF analysis for the twisted operator. If
one wants to extend to Dedekind zeta functions over number fields,
one must redo it again. If one wants to extend to function-field
zetas, again. Each generalization needs its own stabilization
analysis.

**When self-adjointness comes from functional calculus on the
modular operator, it generalizes for free.** The functional calculus
argument works for any type III factor in standard form. GRH,
Dedekind, function-field, automorphic — each comes with its own
BC-type algebra, each with a modular operator, each giving a self-
adjoint $D$ by the same functional-calculus argument. No per-case
analysis is needed.

## The three technical steps spelled out

For completeness, here are the three self-adjointness steps with a
bit more care.

**Step 1: $\Delta$ positive self-adjoint on $H_{\omega_1}$.** By the
polar decomposition $\bar S = J \Delta^{1/2}$ of the closable
antilinear operator $S_0(a\xi) = a^*\xi$ (see §11), $\Delta^{1/2}$
is the positive part of $\bar S$. A positive operator on a Hilbert
space is self-adjoint by construction (it is the unique positive
square root of $\Delta = \bar S^* \bar S$). Hence $\Delta$ itself is
positive and self-adjoint. (Takesaki Vol II §VI.1.2, Theorem 1.4.)

**Step 2: $\log \Delta$ self-adjoint.** The spectrum of $\Delta$ is
contained in $[0, \infty)$. On the complement of $\{0\}$, $\log$ is
a real-valued Borel function of moderate growth. The functional
calculus $f(\Delta) := \int f(\lambda) dE_\Delta(\lambda)$ produces
a self-adjoint operator whenever $f$ is real-valued Borel. We apply
with $f = \log$. (Reed-Simon Vol I, Theorem VIII.5.)

*Caveat*: $0$ must not be a point mass of the spectral measure, else
$\log \Delta$ is ill-defined at $0$. For the BC algebra at KMS$_1$,
$0 \notin \text{spec}(\Delta)$: the factor is of type III$_1$, and
$\Delta$ is invertible (the KMS$_1$ vector $\xi_{\omega_1}$ is
cyclic and separating). So this caveat is moot.

**Step 3: $D = -(2/\pi^2) i \log \Delta$ self-adjoint on $H_R$.** On
the full Hilbert space $H_{\omega_1}$, the modular conjugation $J$
is antilinear. The even-parity sector $H_R = P_{\text{even}}
H_{\omega_1}$ is the eigenspace of the parity involution $\gamma$
(BC $\hat{\mathbb{Z}}^*$-action at $-1$). On $H_R$, $J$ acts as
complex conjugation (this is the content of restricting to the even
sector — it "linearizes" $J$). Therefore the operator $i \log
\Delta|_{H_R}$ is, after this linearization, self-adjoint on $H_R$
in the standard Hilbert-space sense. Multiplication by the real
scalar $-(2/\pi^2)$ preserves self-adjointness. Hence $D$ is self-
adjoint on $H_R$. (Takesaki Vol II §VI.1; cross-reference Paper 49
§18 for the detailed parity-sector argument.)

## Why functional calculus gives more than self-adjointness

Once $D$ is defined by functional calculus, many properties follow
for free that require separate arguments in the CCM construction:

- **Spectrum is contained in $\mathbb{R}$**: immediate from self-
  adjointness.
- **$D$ has a spectral resolution $E_D$**: immediate from the spectral
  theorem for self-adjoint operators.
- **For any continuous $g: \mathbb{R} \to \mathbb{C}$, $g(D)$ is a
  bounded normal operator**: immediate from functional calculus.
- **$D$ commutes with any bounded Borel function of $\Delta$**:
  immediate (since $D$ itself is a function of $\Delta$).
- **The semigroup $e^{-t D^2}$ exists and is a strongly continuous
  contraction semigroup for $t \geq 0$**: immediate from spectral
  theorem plus $D$ self-adjoint.

In CCM, each of these properties is either proved ad hoc or stated as
a consequence of the particular prolate/CF construction. Paper 49
gets all of them for free.

## A concrete analogy

Imagine constructing the Laplacian on the circle two different ways.

**Route 1 (CCM-analog)**: write the Laplacian as a finite-difference
matrix on a discretization of the circle. The matrix is *almost*
symmetric, but has small off-diagonal corrections near the
boundary. Add a rank-1 stabilizing term so the matrix is exactly
symmetric. Verify that the stabilization is small enough to preserve
the continuum limit.

**Route 2 (Paper 49 analog)**: write the Laplacian as $\Delta_{S^1}
= -\partial_\theta^2$ directly. By integration by parts, $\langle
\Delta_{S^1} f, g \rangle = \langle f, \Delta_{S^1} g \rangle$ for
smooth periodic functions $f, g$. The Laplacian is self-adjoint on
its natural domain ($H^2(S^1)$). No stabilization, no finite-$N$
discretization, no rank-1 corrections.

Both routes give the same Laplacian in the limit. Route 1 is useful
for explicit numerics. Route 2 is better for structural arguments.
Paper 49 is Route 2 applied to Hilbert-Pólya.

## Summary

CCM adds self-adjointness by hand (CF stabilization). Paper 49 gets
self-adjointness from the algebra's own structure (functional
calculus on $\Delta$). The structural content is the same; the
mathematical tools are different; the downstream advantages are that
Paper 49 extends for free to every generalization (GRH, Dedekind,
function field, automorphic) while CCM requires a new stabilization
analysis for each. This is the second major aesthetic and practical
difference between the two constructions, after the prolate-basis
question of §29.

---

*Next: §31 — Tomita-Takesaki is classical. The machinery Paper 49
uses is 55 years old and thoroughly peer-reviewed.*
