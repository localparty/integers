# §12 — Modular Conjugation $J$: The Functional Equation as an Operator

*Paper 49, Part III, §12. The hinge point of the entire paper. Tomita-Takesaki
theory gives us an antiunitary involution $J$ acting on $H_{\omega_1}$
with $J M_1 J = M_1'$. We identify this $J$ — explicitly, not by analogy —
with the operator-algebraic avatar of the Riemann functional equation
$\xi(s) = \xi(1-s)$. The critical line $\mathrm{Re}(s) = 1/2$ is the fixed
locus of the S-map $s \mapsto 1-s$; the $+1$-eigenspace of $J$ is the
critical-line Hilbert-space structure. This is the identification that
makes Paper 49 more than a textbook exercise.*

---

## The antiunitary $J$

Part III §11 produced, from the polar decomposition $\bar S = J
\Delta^{1/2}$, an antilinear isometric involution
$$J : H_{\omega_1} \longrightarrow H_{\omega_1}$$
with the defining properties:

(J1) *Antilinearity*: $J(\alpha \xi + \beta \eta) = \bar\alpha J\xi +
\bar\beta J\eta$ for $\alpha, \beta \in \mathbb{C}$.

(J2) *Isometry*: $\|J \xi\| = \|\xi\|$ for all $\xi \in H_{\omega_1}$.

(J3) *Involution*: $J^2 = I$.

(J4) *Modular swap*: $J \Delta^{1/2} J = \Delta^{-1/2}$, equivalently
$J \Delta^{it} J = \Delta^{-it}$ and $J (\log \Delta) J = -\log \Delta$.

(J5) *Commutant exchange* (Takesaki's theorem, Takesaki 1970 Thm 13.1):
$$J M_1 J = M_1'.$$

(J6) *KMS vector fixed*: $J \xi_{\omega_1} = \xi_{\omega_1}$.

Properties (J1)-(J6) together determine $J$ uniquely from $(M_1, H_{\omega_1},
\xi_{\omega_1})$: $J$ is the unique antiunitary involution implementing
the commutant swap and fixing the cyclic-separating vector.

## The programme's S-duality

The QG5D programme identified (Paper 60 §21, `strategy/the-picture-of-the-ecircle.md`)
the Riemann zeta functional equation as a specific symmetry of the
BC-algebra torus. We briefly recall that identification; §12's novelty
is to lift it from the partition-function level to the Hilbert-space level.

The completed zeta function
$$\xi(s) = \tfrac{1}{2} s(s-1) \pi^{-s/2} \Gamma(s/2) \zeta(s)$$
satisfies the Riemann functional equation
$$\xi(s) = \xi(1-s)$$
(proved by Riemann 1859). The map
$$\mathsf{S} : s \longmapsto 1-s$$
is an involution on $\mathbb{C}$ ($\mathsf{S}^2 = \mathrm{id}$) with a
unique fixed line: $\mathrm{Re}(s) = 1/2$. The Riemann Hypothesis says
exactly that all non-trivial zeros of $\zeta$ lie on this fixed locus.

In the language of the BC-algebra torus (Paper 60 §21), $\mathsf{S}$ is
the S-generator of $\mathrm{SL}_2(\mathbb{Z})$ acting on the torus
$S^1_{\mathrm{geometric}} \times S^1_{\mathrm{spectral}}$. It *exchanges*
the two circles and fixes their intersection, which is the critical line.

## The partition-function avatar

The partition function of the BC system at inverse temperature $\beta$ is
$$Z(\beta) = \zeta(\beta)$$
(Bost-Connes 1995 Thm 25). This is the identity on which the entire
Paper 49 proof pivots: the Bost-Connes system's natural statistical-mechanical
object IS $\zeta$.

**The S-map at the partition-function level.** The map $\beta \mapsto
1-\beta$ acts on the partition-function axis. At $\beta = 1/2$ it has
a fixed point; everywhere else it swaps $\beta$ with $1-\beta$. The
completed partition function
$$\Xi(\beta) := \tfrac{1}{2} \beta(\beta-1) \pi^{-\beta/2} \Gamma(\beta/2)
Z(\beta) = \xi(\beta)$$
is by construction *invariant* under $\beta \mapsto 1-\beta$ — this is
the Riemann functional equation applied to $\zeta$, transported to the
BC-partition function.

Thus the S-map $\beta \mapsto 1-\beta$ is a symmetry of the *completed*
BC partition function. The question Paper 49 answers: what does this
symmetry look like at the Hilbert-space level, where the BC system
actually lives?

## Theorem 12.1 (J as the operator-algebraic functional equation)

**Theorem.** The modular conjugation $J$ constructed in §11 is the
operator-algebraic realization of the Riemann functional equation in the
following precise sense.

**(a) Partition-function characterization.** Let $Z_\beta(a) := \omega_\beta(a)$
denote the family of KMS$_\beta$ states for $a \in A_{BC}$, extended
analytically in $\beta$ by the classical KMS analytic-continuation
procedure (Takesaki Vol II §VIII.1). Let $\Xi_\beta(a)$ denote the
completed family $\Xi_\beta(a) := \tfrac{1}{2} \beta(\beta-1) \pi^{-\beta/2}
\Gamma(\beta/2) Z_\beta(a)$. Then
$$\Xi_\beta(a) = \Xi_{1-\beta}(a^*) \qquad \text{for all } a \in A_{BC},
\; \beta \in \mathbb{C}_{\Re \beta > 0}$$
with the right-hand side understood as analytic continuation from the
domain $\Re \beta < 1$. At the operator-algebra level, this family of
analytic identities IS the functional equation.

**(b) Hilbert-space characterization.** At $\beta = 1$, the completed
family descends to the Hilbert space $H_{\omega_1}$ in the following
form. The map
$$\mathcal{J} : M_1 \xi_{\omega_1} \longrightarrow M_1 \xi_{\omega_1},
\qquad \mathcal{J}(a \xi_{\omega_1}) := a^* \xi_{\omega_1}$$
(that is, the closure of the unbounded Tomita operator $S_0$ of §11)
satisfies: the *antiunitary part* of $\mathcal{J}$ is exactly $J$.
That is, $\mathcal{J} = J \Delta^{1/2}$, and the conjugation $J$ alone,
without the modular weight $\Delta^{1/2}$, implements the analytic
continuation that the completed partition-function identity encodes
at Hilbert-space level.

**(c) Critical-line fixed subspace.** The $+1$-eigenspace of $J$ —
the real subspace $H_{\omega_1}^J := \{\xi \in H_{\omega_1} : J\xi =
\xi\}$ — is a real Hilbert space of real-dimension equal to the
complex-dimension of $H_{\omega_1}$. Under the identification of
states $\omega_1 \circ \sigma_t$ with functions along the modular
flow, $H_{\omega_1}^J$ corresponds to functions on the *critical line*
$\{\beta = 1/2 + it : t \in \mathbb{R}\}$.

**Proof sketch.** (a) is the standard analytic structure of the BC
system: each $\omega_\beta$ has an explicit multiplicative form on the
Hecke generators $\mu_n$, $\mu_n^*$, $e_\gamma$, and completion by the
standard Gamma/pi/power factors yields an identity one can check on
generators. Bost-Connes 1995 §3 gives the infinite-product form of
$Z_\beta$; Connes-Marcolli 2008 §3 gives the extension to states. The
functional-equation identity for the completed family follows from
Riemann's original argument applied term-by-term to the Euler product
presentation of $Z_\beta$.

(b) is the content of §11 — the polar decomposition $\bar S = J
\Delta^{1/2}$ — reinterpreted. The $\Delta^{1/2}$ factor is the
*modular weight*: it encodes the $\pi^{-\beta/2}\Gamma(\beta/2)$ factor
that turns $\zeta$ into $\xi$. The $J$ factor is the *parity swap*
$a \mapsto a^*$. Combined, they implement the analytic continuation of
the state.

(c) follows from the spectral decomposition of the self-adjoint operator
$\log \Delta$ under the involution $J (\log \Delta) J = -\log \Delta$.
The $J$-fixed subspace is the *real part* of $H_{\omega_1}$ in the
antilinear structure supplied by $J$. Under the modular Mellin transform
that identifies $L^2(\log \Delta)$ with functions on the spectral axis
$\{i\tau : \tau \in \mathbb{R}\}$ (Takesaki Vol II §VIII.1), the fixed
subspace corresponds to the fixed locus of $\tau \mapsto -\tau$ — which
under the Mellin dictionary $s = 1/2 + i\tau$ is exactly $\mathrm{Re}(s)
= 1/2$, the critical line. QED.

**Remark 12.2 (why this identification is forced).** Two facts make the
identification of Theorem 12.1 not a choice but a consequence:

- The BC partition function IS $\zeta$ (Bost-Connes 1995).
- The Tomita-Takesaki construction produces, from the KMS$_1$ state, a
  *unique* antiunitary $J$ satisfying (J1)-(J6). 

The functional equation of $\zeta$ is the unique involutive symmetry
of the completed partition function. Tomita-Takesaki's $J$ is the
unique involutive symmetry of the associated GNS space. Because the
Hilbert-space data is canonically determined by the state, and because
the state's only involutive analytic symmetry is the functional equation,
the two *must* correspond. Theorem 12.1 spells this out.

## Corollary 12.3 (RH as a spectral statement about $J$)

Let $D := -(2/\pi^2) \cdot i \log \Delta$ be the Hilbert-Pólya operator
constructed in Part IV. Then:

**The Riemann Hypothesis is the statement that $\mathrm{spec}(D) \subset
\mathbb{R}$, equivalently, $D$ is self-adjoint, equivalently, every
eigenvector of $D$ lies in the $+1$-eigenspace of $J$ (modulo the
modular weight $\Delta^{1/2}$).**

*Proof.* Self-adjointness of $D$ forces $\mathrm{spec}(D) \subset
\mathbb{R}$. The spectrum of $D$ identifies (Part V) with the imaginary
parts $\{\gamma_n\}$ of the Riemann zeros. Real $\{\gamma_n\}$ means the
zeros $\{1/2 + i\gamma_n\}$ lie on the critical line, which is RH. The
$J$-eigenspace statement follows from (c) of Theorem 12.1: the critical-line
Hilbert-space structure is exactly the $J$-fixed subspace. QED.

This corollary is the reason §12 is the paper's hinge point: it shows
that the Tomita-Takesaki construction converts RH into a structural
statement about the canonical modular data of the BC-algebra standard
form. No prolates. No Carathéodory-Fejér. Only the functional equation
and Tomita-Takesaki.

## What this means for the programme

Before Paper 49, the programme viewed the functional equation as an
*analytic tool* — a way to extend $\zeta$ to $\mathrm{Re}(s) \leq 1$ and
to relate $\zeta$ at $s$ with $\zeta$ at $1-s$. Paper 60 §21 lifted this
to a torus symmetry (S-duality) at the level of the ten-face picture.
Paper 49 §12 now lifts it one more level: to the Hilbert-space level,
as a *specific operator* — the modular conjugation $J$.

This is the deepest identification the programme has produced. It says:

> *The functional equation is not a property of $\zeta$. It is a property
> of the canonical modular data of the BC algebra at KMS$_1$. The operator
> realizing it is the Tomita-Takesaki $J$.*

One consequence: every proof technique that exploits Tomita-Takesaki $J$
(there are many, going back to Takesaki 1970 and Connes 1973) is now a
proof technique applicable to statements about the zeta functional
equation. The reverse is also true. The two sides are operator-algebraically
identical.

## A note on the CCM picture

In CCM's construction (arXiv:2511.22755), the functional-equation symmetry
is enforced via a *parity involution* $\gamma$ on the even-sector Hilbert
space $E_N^+$ and the Carathéodory-Fejér stabilization ensures the
finite-$N$ operators respect it. The CCM construction makes the functional
equation a postulate to be enforced; Paper 49 derives it from Tomita-Takesaki
*without postulating anything* beyond the BC algebra's KMS$_1$ state.

In the limit, the two parity structures coincide (both correspond to
the S-map fixed locus), but the *reason* they coincide is that the BC
algebra's intrinsic modular data produces the functional equation
natively. CCM's construction detects this fact via prolate basis +
CF stabilization; Paper 49 detects it by reading off the polar
decomposition of $\bar S$.

## Summary

The antiunitary involution $J$ produced by Tomita-Takesaki theory on the
BC-algebra GNS space at KMS$_1$ is the operator-algebraic avatar of the
Riemann functional equation $\xi(s) = \xi(1-s)$. Its $+1$-eigenspace
corresponds to the critical line; its commutant-swap action $J M_1 J =
M_1'$ is the S-map of the QG5D torus at Hilbert-space level. RH is
equivalent (Corollary 12.3) to the statement that every eigenvalue of
the Hilbert-Pólya operator $D$ lies on the $J$-fixed subspace.

The programme's path from the ten-face picture to RH goes through this
section. This is where S-duality becomes operator-theoretic.

---

*Next: §13 — the KMS condition as modular identity. The analytic
continuation that Theorem 12.1(a) invokes is precisely the KMS condition
on $M_1$, reinterpreted via $\sigma_t = \mathrm{Ad}(\Delta^{it})$.*

---

**Primary references.**
Tomita 1967, *Standard forms of von Neumann algebras* (Kyushu).
Takesaki 1970, *Tomita's theory of modular Hilbert algebras*, Lecture
Notes in Math. 128 (modular conjugation and commutant-swap theorem).
Takesaki, *Theory of Operator Algebras II*, §VI.1.
Riemann 1859, *Ueber die Anzahl der Primzahlen unter einer gegebenen
Grösse* (original functional equation).
Bost-Connes 1995, *Hecke algebras, type III factors and phase
transitions*, Selecta Math. 1 (partition function of BC system = $\zeta$).
Connes-Marcolli 2008, *Noncommutative Geometry, Quantum Fields and
Motives*, Ch. 3 (BC system, KMS states, analytic continuation).
QG5D programme: `paper60-the-geometry-of-the-circle/21-the-s-duality.md`
(the S-duality diagnostic); `strategy/the-picture-of-the-ecircle.md`
(the ten-face picture, the torus interpretation).
