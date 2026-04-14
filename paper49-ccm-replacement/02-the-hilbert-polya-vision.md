# §02 — The Hilbert-Pólya Vision

*Paper 49, Part I: Motivation. The oldest strategy for proving the Riemann
Hypothesis. 1913 to 2026. From "find a Hamiltonian" to "the BC algebra's
modular operator IS the Hamiltonian."*

---

## 1913: Hilbert and Pólya

David Hilbert and George Pólya, independently and in correspondence
around 1913, proposed the same idea: the non-trivial zeros of the
Riemann zeta function — specifically their imaginary parts
$\{\gamma_n\}$ — might be the eigenvalues of a self-adjoint operator
$H$ on some Hilbert space.

The strategy is spectacular in its economy. If such an $H$ exists,
then:

- $H = H^*$ forces $\text{spec}(H) \subset \mathbb{R}$ (spectra of
  self-adjoint operators are real).
- If $\text{spec}(H) = \{\gamma_n\}$, then $\gamma_n \in \mathbb{R}$
  for all $n$.
- Therefore all non-trivial zeros of $\zeta$ lie on
  $\text{Re}(s) = 1/2$.
- Riemann Hypothesis proved.

The entire analytical difficulty collapses into one question: does
such an $H$ exist? The conjecture does not tell us how to find it. It
tells us that finding it would suffice.

The Hilbert-Pólya conjecture is not a theorem. It is a program. A
century of effort since 1913 has tried to realize $H$ explicitly.

## 1976: Hugh Montgomery

Montgomery computed the pair correlation of zeros:

$$
\lim_{T \to \infty} \frac{1}{N(T)} \sum_{0 < \gamma, \gamma' \leq T}
  f\!\left( \frac{\gamma - \gamma'}{2\pi / \log T} \right)
= \int_{-\infty}^\infty f(u)\left( 1 - \left( \frac{\sin \pi u}{\pi u}
\right)^2 \right) du.
$$

The kernel $1 - (\sin \pi u / \pi u)^2$ is the GUE (Gaussian Unitary
Ensemble) pair-correlation density from random matrix theory. Zeros
repel each other like eigenvalues of random Hermitian matrices.

This was the first quantitative evidence that the zeros are
eigenvalues of *something*. The something has GUE symmetry. The
something is very unlikely to be accidental.

Montgomery's result sharpened the Hilbert-Pólya vision: not just a
self-adjoint operator, but one belonging to the GUE universality
class.

## 1999: Berry and Keating

Michael Berry and Jonathan Keating proposed a specific classical
Hamiltonian:

$$ H = xp $$

— position times momentum. Quantized (with appropriate ordering) on
the half-line, with a boundary condition enforcing the functional
equation of $\zeta$, its eigenvalues should be the $\gamma_n$.

The heuristic is compelling. The classical orbits of $H = xp$ are
hyperbolae. Their action integral, evaluated on the periodic orbit
with energy $E$, gives $E(\log E - 1)$ — which matches the leading
Riemann-von Mangoldt asymptotic $N(T) \sim (T/2\pi)\log(T/2\pi e)$ for
the zero counting function.

But "should be" is not a proof. Berry-Keating never constructed a
self-adjoint operator on a Hilbert space whose spectrum is
$\{\gamma_n\}$. They gave a picture, not a theorem. The quantization
of $H = xp$ is not unique, the boundary conditions are ambiguous, and
no rigorous realization follows from their analysis.

## 1999: Connes and noncommutative geometry

Alain Connes, in a parallel line of work, proposed that the correct
home for the Hilbert-Pólya operator is the geometry of the
adele-class space $\mathbb{A}_\mathbb{Q} / \mathbb{Q}^*$ — a
noncommutative space in the sense of NCG. The Bost-Connes algebra
$A_{BC} = C(\hat{\mathbb{Q}}) \rtimes \mathbb{N}^*$ (Bost-Connes
1995) is the operator-algebraic realization.

Connes showed:

- The partition function of $A_{BC}$ equals $\zeta(\beta)$.
- The unique KMS state at $\beta = 1$ is the critical point of a
  phase transition; below $\beta = 1$ the system has no equilibrium,
  above $\beta = 1$ there is a Galois-indexed family.
- The Weil explicit formula arises as a trace on $A_{BC}$ paired
  with a suitable test function.

The Hilbert-Pólya operator, in Connes's vision, lives on the
GNS-representation of $A_{BC}$ at KMS$_1$. It is not quite written
down explicitly — the 1999 *Selecta Mathematica* paper points
toward it without constructing it. The Connes program has spent
a quarter-century filling in details.

## 2025: CCM

The CCM preprint (arXiv:2511.22755) constructs specific operators
$D_N$ on even-sector Hilbert spaces $E_N^+$ that approximate the
Hilbert-Pólya operator in the CCM sense. The route uses prolate
spheroidal wavefunctions to truncate, Carathéodory-Fejér
stabilization to guarantee self-adjointness at finite $N$, and an
ITPFI convergence argument (ours, from Paper 13 Layer 2) plus Bögli
spectral exactness to pass to the $N \to \infty$ limit.

The CCM operators realize Hilbert-Pólya — conditionally on the
preprint passing peer review.

## 2026: Paper 49

The QG5D programme arrives at the Hilbert-Pólya operator from a
different direction. Our starting point is not "approximate the
Mellin operator by a prolate-band truncation." Our starting point
is this:

> *The BC algebra at KMS$_1$ is a type III$_1$ factor. Every type
> III$_1$ factor in standard form has a canonical modular operator
> $\Delta$ given by Tomita-Takesaki theory. Therefore the BC
> algebra has a canonical $\Delta$. What IS that $\Delta$?*

The answer — developed in Parts III–IV of this paper — is that
$\Delta$ is the exponential of the Hilbert-Pólya operator, up to the
CBB rescaling constant $\kappa = 2/\pi^2$:

$$
D := -(2/\pi^2) \cdot i \log \Delta, \qquad
\text{spec}(D) = \{ \gamma_n \}.
$$

No prolate spheroidals. No Carathéodory-Fejér. The operator is
given canonically by the algebra's own structure. Tomita-Takesaki
was proved in 1970. The BC algebra's type III$_1$ classification
was proved in Paper 13 Layer 2 (three independent proofs). The CBB
rescaling comes from Paper 12's operator dictionary. The matching
to zeros comes from the ITPFI factorization + QUE + Sato-Tate —
all programme-internal or classically proved.

## Why this is natural

The vision crystallizes when one notices the following.

**The functional equation is the modular conjugation.** Riemann's
$\xi$ function satisfies $\xi(s) = \xi(1 - s)$ — a $\mathbb{Z}/2$
symmetry about the critical line. In Tomita-Takesaki, every standard
form $(M, H, J, P^+)$ comes with an antiunitary modular conjugation
$J$ with $J^2 = I$ and $J M J = M'$. The involution $s \mapsto 1-s$
in the complex plane IS the involution $J$ on the Hilbert space.
The functional equation is not a coincidence of analytic continuation.
It is the operator-algebraic reflection of $J$. (Elaborated in §12.)

**The Hamiltonian is the generator of the KMS flow.** The KMS
condition at inverse temperature $\beta = 1$ identifies the modular
flow $\sigma_t = \text{Ad}(\Delta^{it})$ with the BC time evolution.
The *generator* of this flow — the operator that takes the derivative
at $t = 0$ — is $i \log \Delta$. That is, up to a scalar, the
Hamiltonian. (Elaborated in §13, §17.)

**The Hilbert-Pólya operator IS $-(2/\pi^2) i \log \Delta$.** It
cannot be anything else. The BC algebra is, by construction, the
arithmetic object that Riemann-zeta-like data live on. KMS$_1$ is
the unique critical equilibrium. Tomita-Takesaki's $\Delta$ at that
state is the unique canonical modular operator. The Hilbert-Pólya
operator must be a function of $\Delta$; the CBB dictionary fixes
which function. There is no choice.

## Where the programme sits in the history

- 1913: Hilbert and Pólya. A conjecture about existence.
- 1976: Montgomery. A symmetry-class constraint (GUE).
- 1999: Berry-Keating. A heuristic Hamiltonian ($H = xp$).
- 1999: Connes. The noncommutative home ($A_{BC}$).
- 2025: CCM. A prolate-spheroidal realization, conditional on
  peer review.
- 2026: Paper 49. The modular-operator realization, programme-internal.

Each step refines the earlier ones. Paper 49 does not replace CCM as
a mathematical construction — it offers a different construction,
with a different tool set, that we can independently audit using the
programme's own infrastructure. The Hilbert-Pólya vision is the same
throughout. What changes is how we realize it.

## One more observation

The programme, by Paper 49, can say: "RH is a theorem about a specific
operator on a specific Hilbert space. The operator is canonically
determined by the Bost-Connes algebra's structure at KMS$_1$. The
Hilbert space is the GNS space of the unique KMS$_1$ state. The
operator is $-(2/\pi^2) i \log \Delta$. There are no free parameters.
There are no alternative candidates. There is only one
Hilbert-Pólya operator, and it is this one."

That is what 113 years of work has led to.

---

*Next: §03 — the programme's infrastructure readiness. What we have
already proved is more than enough.*
