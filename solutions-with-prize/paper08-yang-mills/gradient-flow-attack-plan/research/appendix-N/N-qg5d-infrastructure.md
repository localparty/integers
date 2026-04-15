# Appendix N: QG5D Infrastructure

This appendix collects the results from the Quantum Geometry in 5D (QG5D)
framework that enter the gradient-flow proof of Conjectures L.1--L.4. Each
result is stated formally with a one-paragraph description of its role in
the Yang--Mills mass gap programme. The original proofs reside in the
cited QG5D papers; this appendix reproduces only the theorem statements
and the logical connections to the present work.


---


## N.0 Purpose and scope

The QG5D framework (Papers 1--10) develops the physics and mathematics of
Kaluza--Klein compactification on $M^4 \times S^1/\mathbb{Z}_2$ and on
$M^4 \times \mathrm{CP}^2 \times S^2 \times S^1$. Only a small subset
of this programme is needed here: the **spectral identities** governing
heat kernels and Kaluza--Klein mode sums on compact product manifolds.
These identities control the UV behaviour of the gradient flow because the
flow propagator $K(t,p) = e^{-tp^2}$ is itself a heat kernel. The QG5D
results enter through three channels:

1. The Epstein zeta vanishing (Theorem K.1, Paper 1) proves that
   KK mode sums at non-positive integer arguments are identically zero,
   killing all subleading UV counterterms at every loop order.

2. The Seeley--DeWitt coefficient vanishing (Theorem U.2a, Paper 10)
   proves that the leading heat kernel coefficients $a_2 = a_4 = 0$ on
   the flat KK background, establishing one-loop scheme-independent UV
   finiteness.

3. The scheme-independence results (Theorem 1, Theorem 4.3, Proposition
   3.1, Paper 10) establish that the UV finiteness holds in every
   regularisation scheme that preserves diffeomorphism invariance ---
   including the gradient-flow regularisation.

No gravitational dynamics, no cosmological predictions, and no
string-theoretic dualities from the ~~QG5D~~ Integers<!-- legacy 2026-04-15 Intervention 8b §0.10 §0.1: "QG5D" (programme shorthand) → "Integers" --> programme enter the Yang--Mills
proof. The compactification geometry is used purely as a spectral scaffold
providing a second UV regulator (the discrete KK mass tower) that
persists in the $t \to 0^+$ limit of the gradient flow.


---


## N.1 From Paper 1: Epstein vanishing, perturbative finiteness, and the KK spectrum

Paper 1 establishes the foundational spectral results for ~~linearised 5D~~ linearised M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D" → "M⁵" -->
gravity on $M^4 \times S^1$. The results quoted here concern the analytic
properties of Kaluza--Klein mode sums and the heat kernel on product
manifolds.


### N.1.1 The KK mass spectrum

On $M^4 \times S^1/\mathbb{Z}_2$ with the $S^1$ of radius $R$, the
Kaluza--Klein decomposition assigns to each bulk field a tower of 4D
modes with masses

$$m_n = \frac{n}{R}, \qquad n = 0, 1, 2, \ldots \tag{N.1}$$

$\mathbb{Z}_2$-even fields ($h_{\mu\nu}$, $h_{55}$) expand in cosines
$\cos(ny/R)$ with $n \ge 0$; $\mathbb{Z}_2$-odd fields ($h_{\mu 5}$)
expand in sines $\sin(ny/R)$ with $n \ge 1$. The method of images
restores the full $\mathbb{Z}$-sum from the half-line $n \ge 0$:

$$\int_0^{\pi R} G_{\mathbb{Z}_2}(y,y)\,dy
  = 1 + 2\sum_{n=1}^{\infty} f(m_n^2)
  = \sum_{n \in \mathbb{Z}} f(m_n^2). \tag{N.2}$$

The orbifold structure and the resulting mode counting are used
throughout the gradient-flow programme to ensure that the KK mode sums
have the correct $\mathbb{Z}$-lattice structure required by the Epstein
zeta machinery. The zero-mode ($n = 0$) contribution counts with
degeneracy 1; each $n \ge 1$ mode counts with degeneracy 2 (direct plus
mirror image), reproducing the full circle sum under zeta regularisation.

**Source:** Paper 1, Section 2 (Framework); Appendix W, Sections W.1--W.2
(orbifold structure).


### N.1.2 The leading KK sum identity: $S_0 = 0$

Under spectral zeta regularisation, the formal sum over all KK modes
evaluates to

$$S_0 \;=\; 1 + 2\zeta_R(0) \;=\; 1 + 2\Bigl(-\tfrac{1}{2}\Bigr) \;=\; 0.
\tag{N.3}$$

At $L$ loops, the leading UV divergence carries the factor $S_0^L = 0^L = 0$
for all $L \ge 1$. This identity, which follows from the value
$\zeta_R(0) = -1/2$ of the Riemann zeta function, is the simplest
instance of the general Epstein vanishing phenomenon. It ensures that the
most UV-divergent counterterm at each loop order has identically zero
coefficient.

**Source:** Paper 1, Appendix K, Section K.2.1; Appendix F (one-loop
verification).


### N.1.3 Heat kernel factorisation on product manifolds

On the product manifold $M^4 \times S^1$, the heat kernel of the kinetic
operator $\Delta = \Delta_{4D} + \Delta_{S^1}$ factorises:

$$\mathrm{Tr}\bigl[e^{-t\Delta}\bigr]
  = \mathrm{Tr}_{M^4}\bigl[e^{-t\Delta_{4D}}\bigr]
  \;\times\;
  \mathrm{Tr}_{S^1}\bigl[e^{-t\Delta_{S^1}}\bigr]. \tag{N.4}$$

The $S^1$ factor is the Jacobi theta function
$\mathrm{Tr}_{S^1}[e^{-t\Delta_{S^1}}] = \tfrac{1}{2}(\theta_3(0, e^{-t/R^2}) - 1)$
for Dirichlet modes, which under Poisson resummation yields an
exponentially convergent winding-mode expansion with no polynomial
corrections in $t$ beyond the leading $(4\pi t)^{-1/2}$ term and a
constant offset $-1/2$ from the fixed-point contribution. This
factorisation is the starting point for both the Seeley--DeWitt analysis
(Theorem U.2a) and the Poisson bridge between regularisation schemes.

**Source:** Paper 1, Appendix S, Section S.3.1 (spectral zeta on product
manifolds); Paper 10, Section 2.6 (Jacobi theta cross-check).


### N.1.4 The Eisenstein zeta function and the $S_0 = 0$ mechanism

The identity $S_0 = 0$ arises from the Epstein--Eisenstein zeta function
of the $S^1$ lattice. For the one-dimensional lattice $\mathbb{Z}$, the
Epstein zeta function reduces to $E_1(s; 1) = 2\zeta_R(s)$, and the
completed zeta function $\Lambda(s) = \pi^{-s}\Gamma(s)\zeta_R(s)$
satisfies the functional equation $\Lambda(s) = \Lambda(1/2 - s)$. At
$s = 0$, the pole of $\Gamma(0)$ forces $\zeta_R(0) = -1/2$, which
yields $S_0 = 1 + 2(-1/2) = 0$. The same Gamma-function pole mechanism
operates at all negative integers and in all dimensions, leading to the
universal vanishing of Theorem K.1.

**Source:** Paper 1, Appendix K, Section K.4 (functional equation);
Section K.7b (structural zero proof).


### N.1.5 Theorem K.1: Universal Epstein Vanishing

> **Theorem K.1** (Paper 1, Appendix K, Section K.7b). *For any
> positive-definite quadratic form $Q$ in $L$ variables, the
> $L$-dimensional Epstein zeta function satisfies*
>
> $$E_L(-j;\, Q) = 0 \qquad \text{for all integers } j \ge 1.$$

*Proof.* The completed Epstein zeta function
$\Lambda(s) = \pi^{-s}\Gamma(s)\,E_L(s; Q)$ is meromorphic in $s$ with
poles only at $s = 0$ and $s = L/2$. At $s = -j$ with $j \ge 1$,
$\Lambda(-j)$ is finite (no pole of $\Lambda$ at negative integers).
Inverting: $E_L(s; Q) = \pi^s \Lambda(s)/\Gamma(s)$. Since
$1/\Gamma(-j) = 0$ (the Gamma function has poles at all non-positive
integers), we obtain $E_L(-j; Q) = 0$. $\square$

Theorem K.1 is the central number-theoretic identity underlying the UV
finiteness of the KK framework. In the gradient-flow programme, it
controls the KK mode sums that arise when the flow-time regulator is
removed ($t \to 0^+$). At $t = 0$, the loop integrals of the unflowed
theory contain Epstein zeta functions evaluated at non-positive integers;
by Theorem K.1, these all vanish. The $t \to 0$ limit therefore does not
reintroduce UV divergences, because the KK compactification has already
killed them.

**Source:** Paper 1, Appendix K, Section K.7b.


### N.1.6 Theorem S.1: Perturbative finiteness

> **Theorem S.1** (Paper 1, Appendix S, Section S.6). *The $L$-loop
> effective action for ~~linearised 5D gravity~~ linearised M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> on $M^4 \times S^1$, with
> the Kaluza--Klein mode sums regularised by spectral zeta functions, is
> finite at every order $L \ge 1$ in perturbation theory. Specifically:*
>
> *(a) The leading KK mode sum at $L$ loops vanishes identically:
> $S_0^{(L)} = [1 + 2\zeta(0)]^L = 0$.*
>
> *(b) Every subleading KK mode sum is an $L$-dimensional Epstein zeta
> function $E_L(s; Q_L)$ evaluated at a non-positive integer $s \le 0$,
> which is holomorphic by the Epstein--Terras theorem (the Epstein pole at
> $s = L/2 > 0$ is never reached).*
>
> *(c) The $L$-loop effective action is a finite polynomial in these
> finite zeta values.*
>
> *(d) The counterterm coefficients at each loop order are uniquely
> determined by the Epstein zeta values --- the theory is predictive to all
> perturbative orders with no free parameters beyond $G_4$ and the
> compactification radius $R$.*

The proof assembles three established mathematical results: the
Epstein--Terras analytic continuation (Epstein 1903, Terras 1985), the
Seeley--DeWitt heat kernel expansion (Seeley 1967, DeWitt 1965,
Vassilevich 2003), and the positivity of the mass exponent from power
counting ($m_n^2 = n^2/R^2 > 0$ for $n \ge 1$). At each loop order, the
KK mode sums reduce to Epstein zeta functions whose unique pole at
$s = L/2 > 0$ is separated from the evaluation points $s \le 0$ by a gap
of at least $L/2 \ge 1/2$. Theorem S.1 provides the all-orders
perturbative finiteness that the gradient-flow programme inherits: the
KK compactification converts the non-renormalisable divergences of 4D
gravity into finite, calculable Epstein zeta values.

**Source:** Paper 1, Appendix S, Sections S.1--S.6.

**Scope note.** Theorem S.1 is proved for $M^4 \times S^1$. The
extension to $M^4 \times \mathrm{CP}^2 \times S^2 \times S^1$ (the full
11D geometry of Paper 4) requires establishing that the KK mode sums on
the higher-dimensional internal manifold also reduce to Epstein zeta
evaluations at non-positive integers. The vanishing mechanism (Theorem
K.1) is universal; the factorisation step is geometry-specific.


---


## N.2 From Paper 10: Seeley--DeWitt vanishing, $\mathbb{Z}_2$ parity, Poisson bridge, and the Weyl anomaly

Paper 10 proves the scheme-independence of UV finiteness by five
convergent routes. The gradient-flow programme uses four results from
this paper: the Seeley--DeWitt coefficient vanishing (N.2.1), the
$\mathbb{Z}_2$ parity cancellation (N.2.2), the Poisson bridge (N.2.3),
and the Weyl anomaly protection (N.2.4--N.2.5). Each addresses a
distinct aspect of the UV finiteness that the gradient flow inherits.


### N.2.1 Theorem U.2a: Seeley--DeWitt coefficient vanishing

> **Theorem U.2a** (Paper 10, Section 2.5). *Let $\mathcal{L}$ be the
> Lichnerowicz operator for ~~linearised 5D gravity~~ linearised M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> in de Donder gauge on
> the flat background $M^4 \times S^1/\mathbb{Z}_2$. Then the
> Seeley--DeWitt coefficients satisfy:*
>
> $$a_2(\mathcal{L},\, M^4 \times S^1/\mathbb{Z}_2) = 0, \qquad
> a_4(\mathcal{L},\, M^4 \times S^1/\mathbb{Z}_2) = 0.$$
>
> *These vanishings hold identically, independent of any regularisation
> scheme.*

The proof (Paper 10, Sections 2.1--2.7) proceeds by checking every
ingredient in the Vassilevich (2003) universal formula for $a_2$ and
$a_4$: the bulk Riemann curvature $R_{MNPQ}$, the endomorphism $E$, the
bundle curvature $\Omega_{ab}$, the brane extrinsic curvature $K_{ab}$,
the $\eta$-invariant of the tangential operator, and the Cheeger cone
angle correction. On the flat background, every one of these quantities
vanishes identically: $R_{MNPQ} = E = \Omega_{ab} = K_{ab} = \eta = 0$,
and the $\mathbb{Z}_2$ cone angle $\theta = \pi$ produces zero deficit.
The vanishing is confirmed numerically by fitting the KK spectrum heat
kernel trace ($n \le 500$) to the Seeley--DeWitt expansion, obtaining
residuals of order $10^{-9}$ for the $a_2$ and $a_4$ coefficients.

This is the central result connecting the QG5D framework to the gradient
flow. The Yang--Mills gradient flow has propagator $K(t,p) = e^{-tp^2}$:
the heat kernel on $\mathbb{R}^4$. The small-flow-time expansion as
$t \to 0^+$ is controlled by the Seeley--DeWitt coefficients $a_{2k}$.
When $a_2 = a_4 = 0$, the leading UV singularities in the small-flow-time
expansion vanish identically --- not by cancellation between terms, but
because the geometric invariants are zero on the KK background.

**Source:** Paper 10, Sections 2.1--2.7.


### N.2.2 Proposition 3.1: $\mathbb{Z}_2$ parity cancellation

> **Proposition 3.1** (Paper 10, Section 3.3). *For each KK level
> $n \ge 1$:*
>
> $$f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0.$$
>
> *The cancellation is exact and does not require any summation over $n$.*

Here $f_{\mathrm{even}}(n)$ is the contribution of the $\mathbb{Z}_2$-even
mode $h_{\mu\nu}^{(n)}$ (cosine expansion, positive sign from the
$y$-integral $I_{+++}$) and $f_{\mathrm{odd}}(n)$ is the contribution of
the $\mathbb{Z}_2$-odd mode $h_{\mu 5}^{(n)}$ (sine expansion, negative
sign from $I_{--+}$). The sign flip arises from the product-to-sum
identity: $\sin(ny/R)\sin(my/R) = [\cos((n-m)y/R) - \cos((n+m)y/R)]/2$,
which produces opposite sign relative to
$\cos(ny/R)\cos(my/R)\cos((n+m)y/R)$ in the vertex $y$-integral.

The $\mathbb{Z}_2$ cancellation operates at any flow time $t \ge 0$,
because it is a property of the mode decomposition on the orbifold, not
of the UV regulator. As the gradient flow parameter $t \to 0$, the
cancellation persists: even and odd sector contributions cancel term by
term at each KK level, before any summation or regularisation is applied.
This provides an algebraic, non-perturbative mechanism ensuring that the
$t \to 0$ limit does not reintroduce KK-level UV divergences.

**Source:** Paper 10, Section 3, Proposition 3.1 (lines 106--114);
$y$-integral identities (Section 3.2, lines 67--86).


### N.2.3 The Poisson bridge: Lemmas A1--A3

Paper 10 proves that the KK mode sum and dimensional regularisation give
the same UV pole structure, with only exponentially suppressed finite
differences.

> **Lemma A1** (Paper 10, Section 4.6 / Section 5.2a). *In de Donder
> gauge, the ~~5D~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" --> three-graviton vertex numerator, after KK decomposition
> on $S^1/\mathbb{Z}_2$, introduces no $n$-dependent terms at leading UV
> order. The $\partial_5$ contributions are either (i) forbidden by
> $\mathbb{Z}_2$ parity projection, (ii) $O(m_n^2/k^2)$ suppressed in
> the UV limit, or (iii) killed by Epstein vanishing (Theorem K.1).*

> **Lemma A2** (Paper 10, Section 4.6 / Section 5.2b). *In the linearised
> 4D effective theory on $M^4 \times S^1/\mathbb{Z}_2$, the
> Goroff--Sagnotti operator $R_{\mu\nu\rho\sigma}R^{\rho\sigma\lambda\tau}
> R_{\lambda\tau}{}^{\mu\nu}$ receives contributions at dimension-6 order
> only from $h_{\mu\nu}^{(n)}$. The fields $A_\mu^{(n)}$ (graviphoton)
> and $\phi^{(n)}$ (radion) contribute only at dimension-8 or higher and
> are UV-subleading.*

> **Lemma A3** (Paper 10, Section 4.6 / Section 5.2c). *The internal KK
> loop sum in the Goroff--Sagnotti two-loop sunset on $S^1/\mathbb{Z}_2$
> runs over all $n \in \mathbb{Z}$, giving*
>
> $$\int_0^{\pi R} G_{\mathbb{Z}_2}(y,y)\,dy
>   = 1 + 2\sum_{n=1}^{\infty} f(m_n^2)
>   = \sum_{n \in \mathbb{Z}} f(m_n^2).$$
>
> *Under zeta regularisation: $S_0 = 1 + 2\zeta_R(0) = 0$.*

The Poisson bridge works by applying the Poisson resummation formula to
the KK propagator sum at fixed 4D loop momentum $k^2$, converting the
algebraically convergent KK sum into an exponentially convergent sum over
winding modes. The zero-frequency ($m = 0$) Poisson term encodes the UV
pole structure and equals exactly the dimensional-regularisation result;
the winding-mode terms ($m \ge 1$) are $O(e^{-2\pi mRk})$ and UV-finite.
The difference between any two admissible schemes is therefore
exponentially suppressed, finite, and introduces no new divergences. This
was verified numerically to relative precision $1.09 \times 10^{-24}$ in
50-digit arithmetic (Paper 10, Section 4.2). For the gradient-flow
programme, the Poisson bridge guarantees that the flow regularisation and
dimensional regularisation compute the same UV-divergent part of the
effective action.

**Source:** Paper 10, Sections 4.1--4.3 (Poisson bridge); Section 4.6
(Theorem 1 and proof chain).


### N.2.4 Theorem 1: Goroff--Sagnotti vanishing in all schemes

> **Theorem 1** (Paper 10, Section 4.6). *In the two-loop sunset diagram
> for the Goroff--Sagnotti counterterm in ~~5D linearised gravity~~ M⁵ linearised gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D linearised gravity" → "M⁵ linearised gravity" --> on
> $M^4 \times S^1/\mathbb{Z}_2$, the three-graviton vertex coupling
> $I_{+++}(n_1, n_2, n_1 + n_2) = \pi R/4$ is a universal constant,
> independent of the KK levels $n_1, n_2 \ge 1$. Consequently the
> Goroff--Sagnotti coefficient $C_{\mathrm{GS}}$ vanishes identically,
> in all schemes.*
>
> *This result is unconditional within ~~linearised 5D gravity~~ linearised M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" --> on flat
> $M^4 \times S^1/\mathbb{Z}_2$.*

The proof chain has three steps. Step 1: the $y$-integral computation
via product-to-sum identities gives the universal coupling $I_{+++}(n_1,
n_2, n_1 + n_2) = \pi R/4$ for all $n_1, n_2 \ge 1$. Step 2: since the
vertex coupling is $n$-independent, the KK-summed pole coefficient is
$C_{\mathrm{GS}}^{\mathrm{leading}} = [1/(4\sqrt{\pi R})]^2 \cdot J(0,0)
\cdot S_0^2$, and $S_0 = 0$ kills it. Step 3: every subleading correction
contributes a factor $E_2(-j; Q_2)$ with $j \ge 1$, which vanishes by
Theorem K.1.

The Goroff--Sagnotti counterterm $C^3$ (Goroff--Sagnotti 1986, van de Ven
1992) proved 4D pure gravity non-renormalisable. Its vanishing in the KK
theory is a statement at $t = 0$ --- the gradient flow is not needed for
this result. For the gradient-flow programme, the significance is that
the $t \to 0$ limit does not encounter the Goroff--Sagnotti divergence:
it was already zero at $t = 0$.

**Source:** Paper 10, Section 4.6 (Theorem 1, lines 274--310).


### N.2.5 Theorem 4.3: Weyl anomaly scheme-independence

> **Theorem 4.3** (Paper 10, Section 4.5). *In ~~5D linearised gravity~~ M⁵ linearised gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D linearised gravity" → "M⁵ linearised gravity" --> on
> $M^4 \times S^1/\mathbb{Z}_2$, the 4D Weyl anomaly coefficients
> $a_{\mathrm{total}} = c_{\mathrm{total}} = 0$ for the full KK graviton
> tower in any regularisation scheme that: (a) preserves 4D
> diffeomorphism invariance; (b) preserves the UV operator product
> algebra.*

The proof uses two inputs. First, the mass-independence of the Weyl
anomaly (Vassilevich 2003): every KK graviton at level $n$, regardless
of its mass $m_n = n/R$, contributes the same anomaly coefficients
$(a, c) = (43/360,\, 87/20)$ as the massless $n = 0$ graviton. Therefore
$a_{\mathrm{total}} = (43/360) \times S_0 = 0$ and
$c_{\mathrm{total}} = (87/20) \times S_0 = 0$. Second, the Wess--Zumino
consistency condition (Wess--Zumino 1971, Osborn 1991) implies that no
finite local counterterm can shift $(a, c)$: they are cohomologically
protected. Since $(a, c)$ vanish under zeta regularisation, they vanish
in every scheme satisfying conditions (a) and (b).

For the gradient-flow programme, Theorem 4.3 establishes that the UV
finiteness is scheme-independent in any diffeomorphism-preserving
regulator. The Yang--Mills gradient flow is such a regulator: the flow
equation $\partial_t B_\mu = D_\nu G_{\nu\mu}$ is gauge-covariant, hence
diffeomorphism-preserving. The Wess--Zumino protection therefore extends
to the flow regularisation, guaranteeing that UV finiteness at $t > 0$ is
not an artifact of the regularisation choice.

**Source:** Paper 10, Sections 4.4--4.5.


---


## N.3 From Paper 6: Frozen dilaton

Paper 6 establishes the cosmological thermal history within the QG5D
framework. The single result relevant here is the frozen-dilaton
mechanism, which fixes the compactification radius and thereby ensures
that the KK mass tower is a static spectral scaffold.


### N.3.1 The frozen dilaton and the exact Casimir potential

> **Proposition A.1** (Paper 6, Appendix A). *The dilaton potential on
> $S^1/\mathbb{Z}_2$ is the one-loop Casimir energy $V(R) = +c/R^4$
> with $c > 0$, exact to all perturbative orders (Theorem K.1 kills all
> higher-loop corrections). The canonical slow-roll parameter is
> $\varepsilon = 32/3 \gg 1$. The dimensionless fractional change in the
> compactification radius over one Hubble time is*
>
> $$\Delta R / R_0 \;\approx\; 1.84\, H_0 R_0 \;\approx\; 3 \times 10^{-30}.$$
>
> *The dilaton is frozen to extraordinary precision.*

The exactness of the Casimir potential follows from Theorem K.1: all
higher-loop corrections to the vacuum energy on $S^1$ require Epstein
zeta evaluations at negative integers, which vanish identically. The
dilaton (the breathing mode of the compactification radius) is not
stabilised by a potential minimum but is kinematically frozen by Hubble
friction. The fractional drift $\Delta R/R_0 \sim H_0 R_0 \sim
10^{-30}$ per Hubble time means the compactification radius is constant
to a precision far beyond any relevant physical scale.

For the Yang--Mills proof, the frozen dilaton ensures that the KK mass
spectrum $m_n = n/R_0$ is a fixed, time-independent ladder of masses.
The spectral identities (Theorems K.1, S.1, U.2a) apply at the frozen
radius $R_0$; no dynamical evolution of $R$ needs to be tracked. The
compactification geometry enters the proof as a static spectral input,
not as a dynamical degree of freedom.

**Source:** Paper 6, Appendix A (Proposition A.1); Section 2.1 (exact
Casimir potential); Section 2.2 (no Goldberger--Wise minimum).


---


## N.4 From Paper 4: The $\mathrm{CP}^2 \times S^2 \times S^1$ geometry

Paper 4 performs the explicit Kaluza--Klein reduction of 11D gravity on
$M^4 \times \mathrm{CP}^2 \times S^2 \times S^1$, identifying the
Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times
\mathrm{U}(1)$ from the isometries of the internal manifold.


### N.4.1 The compactification geometry and the $r_3$ scale

The 11-dimensional metric decomposes on the product
$M^4 \times \mathrm{CP}^2 \times S^2 \times S^1$, where:

- $\mathrm{CP}^2$ (4 real dimensions, isometry group $\mathrm{SU}(3)$,
  8 Killing vectors) provides the colour gauge bosons;
- $S^2$ (2 dimensions, isometry group $\mathrm{SU}(2)$, 3 Killing
  vectors) provides the weak gauge bosons;
- $S^1$ (1 dimension, isometry group $\mathrm{U}(1)$, 1 Killing vector)
  provides the photon.

The KK mass spectrum on the internal $\mathrm{CP}^2 \times S^2 \times
S^1$ has eigenvalues determined by the Laplacian on each factor:

$$m^2_{\ell_3, \ell_2, n}
  = \frac{\ell_3(\ell_3 + 2)}{r_3^2}
  + \frac{\ell_2(\ell_2 + 1)}{r_2^2}
  + \frac{n^2}{R^2}, \tag{N.5}$$

where $r_3$ is the $\mathrm{CP}^2$ radius, $r_2$ the $S^2$ radius, and
$R$ the $S^1$ radius. The hierarchy $r_3 \ll r_2 \ll R$ ensures that the
$\mathrm{CP}^2$ modes are the heaviest (at or above the GUT scale), the
$S^2$ modes are intermediate, and the $S^1$ modes are the lightest KK
excitations.

For the Yang--Mills preprint, the $r_3$ scale enters through the
KK-enhanced mass gap (Section 4.4, Theorem 4): the lightest KK gluon has
mass $m_1 = 2\sqrt{N}/r_3$, which provides the built-in IR regulator at
every KK level. The $S^1$ factor provides the Epstein zeta machinery
(Theorems K.1, S.1); the $\mathrm{CP}^2 \times S^2$ factors provide the
confining and Higgs-mechanism gauge dynamics. The product structure
ensures that the $S^1$ spectral identities factorise from the internal
gauge dynamics.

**Source:** Paper 4, Section 3 (explicit KK reduction); Section 3.3
(gauge bosons and coupling formulae); Section 3.4 (product-manifold
factorisation).


---


## N.5 Note on gravitational physics

A reviewer might reasonably ask: *Why does a proof about SU($N$)
Yang--Mills theory on $\mathbb{R}^4$ invoke results from ~~5D~~ M⁵<!-- legacy 2026-04-15 Intervention 8b §0.10: bare "5D" → "M⁵" -->
Kaluza--Klein gravity?*

The answer has three parts.


### N.5.1 Only spectral identities enter

The QG5D results used in this paper are spectral identities about heat
kernels, Epstein zeta functions, and Seeley--DeWitt coefficients on
compact Riemannian manifolds. These are theorems in spectral geometry and
analytic number theory, not in gravitational physics. Theorem K.1
(Epstein vanishing) is a statement about the analytic continuation of
Epstein zeta functions evaluated at non-positive integers via the
$1/\Gamma(-j) = 0$ mechanism. Theorem U.2a (Seeley--DeWitt vanishing)
is a statement about the Vassilevich heat kernel coefficients on a flat
product manifold. Theorem 4.3 (Weyl anomaly scheme-independence) is a
consequence of the Wess--Zumino consistency condition, which is a
cohomological identity.

None of these results require that gravity be dynamical. They would hold
equally on a fixed Riemannian background with no gravitational dynamics
at all. The QG5D framework *discovered* these identities in the context
of ~~5D gravity~~ M⁵ gravity<!-- legacy 2026-04-15 Intervention 8b §0.10: "5D gravity" → "M⁵ gravity" -->, but their mathematical content is independent of that
context.


### N.5.2 No gravitational dynamics in the YM proof

The Yang--Mills proof (Sections 4--5 of the main preprint) constructs the
continuum limit of Wilson lattice gauge theory via Balaban's block-spin
renormalisation group, using only the SU($N$) gauge field, the Wilson
plaquette action, and the Haar measure. No metric degrees of freedom, no
graviton propagator, and no Einstein equations appear at any point.

The KK compactification enters through a single channel: it provides a
mass tower $m_n = n/R$ that supplements the bare theory with additional
massive gauge bosons at each KK level. These additional degrees of freedom
are introduced at the lattice level (Section 4.1) and removed by the IR
equivalence theorem (Section 4.5, Theorem 5), which shows that at
distances $\gg R$ the KK-enhanced theory and the standard 4D theory have
the same Schwinger functions up to exponentially suppressed corrections
$O(e^{-m_1 r})$. The gravitational origin of the KK mass tower is
irrelevant to the proof: any mechanism producing a discrete tower of
masses $m_n = n/R$ with the correct $\mathbb{Z}_2$ parity structure
would serve the same purpose.


### N.5.3 The compactification as a spectral scaffold

The conceptual role of the compactification is that of a *spectral
scaffold*: a second UV regulator, independent of the gradient-flow
parameter $t$, that persists in the $t \to 0^+$ limit. In pure 4D, the
flow-time parameter $t$ is the sole UV regulator, and sending $t \to 0$
removes all UV regulation simultaneously. On $M^4 \times
S^1/\mathbb{Z}_2$, the discrete KK mass spectrum provides regulation at
$t = 0$ through the Epstein zeta machinery. The limit $t \to 0$ is
therefore a smooth interpolation between two regulated theories --- one
with flow-time smoothing plus KK regulation, and one with KK regulation
alone --- rather than a passage from a regulated to an unregulated theory.

The scaffold is removed at the end of the proof by the IR equivalence
theorem (Section 4.5, Theorem 5), which projects from the KK-enhanced
theory to the standard 4D theory. The final result --- the existence of a
mass gap $\Delta_\infty > 0$ for SU($N$) Yang--Mills on $\mathbb{R}^4$
--- contains no reference to extra dimensions, Kaluza--Klein theory, or
gravity. The scaffold was used during the proof and then removed, exactly
as a physical scaffold is used during construction and then dismantled.
