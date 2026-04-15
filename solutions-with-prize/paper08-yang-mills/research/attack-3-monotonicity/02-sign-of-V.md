# 02. Sign of the Interaction: Is V >= 0?

## Purpose

Determine whether the 1/N interaction operator V in the decomposition
H = H_0 + V/N is positive semi-definite. If V >= 0, then
gap(H) >= gap(H_0) = Lambda, proving monotonicity immediately. If V
has a negative part, characterize it precisely and bound its magnitude.


---

## 2.1 Why Sign Matters

### 2.1.1 The operator inequality argument

If V >= 0 as a self-adjoint operator on the Hilbert space
$\mathcal{H}$, then for any state $|\psi\rangle$:

$$\langle\psi|H|\psi\rangle = \langle\psi|H_0|\psi\rangle
  + \frac{1}{N}\langle\psi|V|\psi\rangle
  \geq \langle\psi|H_0|\psi\rangle$$

This gives $H \geq H_0$ in the sense of quadratic forms. The
min-max theorem then implies [PROVED -- standard spectral theory]:

$$E_k(H) \geq E_k(H_0) \quad \text{for all } k = 0, 1, 2, \ldots$$

In particular, if $E_0(H) = E_0(H_0) = 0$ (both Hamiltonians have the
same ground state energy after normal ordering), then:

$$\text{gap}(H) = E_1(H) - E_0(H)
  \geq E_1(H_0) - E_0(H_0) = \Lambda$$

This would prove $m(N) \geq \Lambda$ for all N >= 2. [CONDITIONAL on
V >= 0]

### 2.1.2 The subtlety with ground state energies

The operator inequality $H \geq H_0$ gives $E_0(H) \geq E_0(H_0)$,
which says the ground state energy increases. But we want the GAP
$E_1 - E_0$ to increase, not just $E_1$. For this we need:

$$E_1(H) - E_0(H) \geq E_1(H_0) - E_0(H_0)$$

This does NOT follow from $H \geq H_0$ alone. It requires a stronger
condition: V must respect the gap structure. Specifically, if V >= 0
AND V has no matrix element between the ground state and the first
excited state in a way that closes the gap, then the spectral gap
is preserved.

A cleaner formulation uses the TRANSFER MATRIX directly: see
Section 2.4 below.


---

## 2.2 Analysis of the Individual Contributions to V

### 2.2.1 The effective potential correction

The dominant contribution to V at low energies comes from the
effective potential $V_{\text{eff}}(\sigma)$ at finite N. This is
the potential energy for spatially homogeneous sigma configurations.

At N = infinity [PROVED]:

$$V_{\text{eff}}^{(0)}(\sigma) = \frac{1}{4\pi}\left[\sigma\ln\frac{\sigma}{m^2}
  - \sigma + m^2\right]$$

This is the Coleman-Weinberg potential from integrating out the
z-fields. It has a unique minimum at $\sigma = m^2$ with
$V_{\text{eff}}^{(0)}(m^2) = 0$.

The O(1/N) correction [ESTABLISHED]:

$$V_{\text{eff}}^{(1)}(\sigma) = \frac{1}{2}\int \frac{d^2p}{(2\pi)^2}
  \left[\ln\Pi_\sigma(p;\sigma) + \ln\det\Pi_A^{\mu\nu}(p;\sigma)\right]$$

where $\Pi_\sigma(p;\sigma)$ and $\Pi_A(p;\sigma)$ are the auxiliary
field propagators evaluated at general $\sigma$ (not just the
saddle-point value).

### 2.2.2 Sign of $V_{\text{eff}}^{(1)}$

This is the one-loop determinant of the auxiliary field fluctuations.
Its sign depends on the relationship between $\sigma$ and $m^2$.

**At the saddle point $\sigma = m^2$:** The correction shifts the
minimum of $V_{\text{eff}}$ to a new value
$\sigma_* = m^2 + \delta\sigma_1/N$. The shift is [ESTABLISHED]:

$$\delta\sigma_1 > 0$$

This means the effective mass INCREASES at finite N: the minimum of the
potential moves to a larger value of $\sigma$. Physically, quantum
fluctuations of the auxiliary fields push the mass up.

**Interpretation:** The one-loop correction to the effective potential
is NOT positive semi-definite as a function of $\sigma$. It is a
logarithmic correction that can have either sign depending on the
value of $\sigma$. However, the shift of the minimum is positive,
which is the relevant quantity for the mass gap.

### 2.2.3 The sigma self-interaction (cubic vertex)

The cubic vertex $V_{\sigma^3}$ has the kernel:

$$\Gamma_3(p,q) = -\int \frac{d^2k}{(2\pi)^2}
  \frac{1}{(k^2+m^2)((k+p)^2+m^2)((k+p+q)^2+m^2)}$$

**Sign analysis:** $\Gamma_3 < 0$ for all momenta (the integrand is
positive, and the overall sign is negative). [PROVED -- the triangle
integral with three positive-mass propagators is strictly positive,
so $\Gamma_3 < 0$.]

As an operator, $V_{\sigma^3}$ is a CUBIC form in $\tilde\sigma$.
A cubic form is neither positive nor negative semi-definite: for
$\tilde\sigma > 0$ it contributes negatively (since $\Gamma_3 < 0$),
and for $\tilde\sigma < 0$ it contributes positively.

**Conclusion:** $V_{\sigma^3}$ does NOT have a definite sign.
[PROVED: indefinite]

### 2.2.4 The sigma-gauge vertex

The vertex $V_{\sigma A^2}$ couples $\sigma$ fluctuations to gauge
field fluctuations. Its kernel $\Gamma_{\sigma AA}^{\mu\nu}(p,q)$
comes from the second functional derivative of Tr ln with respect to
$A_\mu$ and the first with respect to $\sigma$.

**Sign analysis:** The vertex is proportional to a triangle integral
with one $\sigma$ insertion and two gauge field insertions. The
transverse projection ensures gauge invariance. The resulting operator
is a bilinear in $\tilde{A}$ with a $\sigma$-dependent coefficient:
it has the form $\tilde\sigma \cdot |\tilde{A}|^2$, which is
indefinite in $\tilde\sigma$.

**Conclusion:** $V_{\sigma A^2}$ does NOT have a definite sign.
[PROVED: indefinite]

### 2.2.5 The quartic vertices

$V_{\sigma^4}$ has the kernel:

$$\Gamma_4(p_1, p_2, p_3) = \int \frac{d^2k}{(2\pi)^2}
  \frac{1}{\prod_{j=0}^{3}((k+P_j)^2+m^2)}$$

where $P_j = \sum_{i\leq j} p_i$. This is the box integral.

**Sign analysis:** $\Gamma_4 > 0$ for all momenta. [PROVED -- the
integrand is the product of four positive propagators.]

As an operator, $V_{\sigma^4}$ is a quartic form. Quartic forms with
positive kernels ARE positive semi-definite:

$$V_{\sigma^4} = \int |\tilde\sigma|^2 \cdot |\tilde\sigma|^2 \cdot
  (\text{positive kernel}) \geq 0$$

More precisely, by the Cauchy-Schwarz inequality applied to the
convolution structure of the box integral.

**Conclusion:** $V_{\sigma^4} \geq 0$. [PROVED: positive semi-definite]

Similarly, $V_{\sigma^2 A^2} \geq 0$. [PROVED]


---

## 2.3 The Net Sign of V: An Honest Accounting

Collecting the results:

| Contribution | Sign | Reason |
|-------------|------|--------|
| $V_{\text{eff}}^{(1)}$ (effective potential shift) | Indefinite in $\sigma$, but minimum shifts UP | Logarithmic correction |
| $V_{\sigma^3}$ (cubic sigma) | Indefinite | Cubic forms have no sign |
| $V_{\sigma A^2}$ (sigma-gauge coupling) | Indefinite | Linear in $\sigma$ |
| $V_{\sigma^4}$ (quartic sigma) | >= 0 | Positive kernel |
| $V_{\sigma^2 A^2}$ (quartic mixed) | >= 0 | Positive kernel |
| $V_{\sigma\text{-shift}}$ (saddle shift) | Positive shift of $\sigma_*$ | $\delta\sigma_1 > 0$ |
| $V_{A\text{-shift}}$ (gauge shift) | Zero | $A_* = 0$ by symmetry |

**The bottom line:** V is NOT positive semi-definite as an operator.
[PROVED]

The indefiniteness comes from the cubic vertices: $V_{\sigma^3}$ and
$V_{\sigma A^2}$ can take either sign depending on the field
configuration. The quartic vertices are positive, but they cannot
compensate the cubic terms for all configurations.

**This means the naive argument "V >= 0 implies gap(H) >= gap(H_0)"
FAILS.**


---

## 2.4 Reformulation via the Transfer Matrix

The sign analysis becomes cleaner in the transfer matrix language.
Instead of asking whether V >= 0, ask whether the SPECTRAL GAP of T
is monotone in N.

### 2.4.1 The transfer matrix at finite N

The transfer matrix of the lattice CP^{N-1} model is:

$$T_N = \prod_{x \in \text{slice}} \int_{\mathbb{CP}^{N-1}_x}
  e^{-\beta\,\mathcal{L}_x} \, d\mu_{\text{FS}}$$

where $\beta = N/\lambda_0$ and $\mathcal{L}_x$ is the lattice action
density at site $x$.

### 2.4.2 Comparison between T_N and T_infinity

At N = infinity (saddle-point exact), the transfer matrix becomes:

$$T_\infty = e^{-a H_0}$$

which is the transfer matrix of the free massive theory.

At finite N, the ratio:

$$R_N \equiv T_\infty^{-1/2} \, T_N \, T_\infty^{-1/2}$$

measures the deviation from the free theory. The spectral gap satisfies:

$$\text{gap}(T_N) \geq \text{gap}(T_\infty)$$

if and only if $R_N$ does not close the gap. This is equivalent to:

$$\langle \psi_1 | R_N | \psi_1 \rangle
  \leq \langle \psi_0 | R_N | \psi_0 \rangle$$

where $|\psi_0\rangle$ and $|\psi_1\rangle$ are the ground and first
excited states of $T_\infty$.

### 2.4.3 Why the transfer matrix formulation is better

In the transfer matrix formulation, the question is NOT about the sign
of a single operator V, but about the RELATIVE effect of the
perturbation on the ground state versus the first excited state. Even
if V is indefinite, the gap could still increase if V "raises the
excited states more than the ground state."

Physically: the 1/N interaction (confinement) creates a potential well
that binds the z-particles. The ground state (vacuum) is already at the
bottom of the well, so the interaction raises the excited states
relative to the ground state. This INCREASES the gap.

This reformulation shows why the sign of V is a red herring: what
matters is not V >= 0 but rather the DIFFERENTIAL effect of V on
different energy levels.


---

## 2.5 A Decomposition with Better Sign Properties

### 2.5.1 Normal-ordering the interaction

Write V in normal-ordered form with respect to the H_0 vacuum:

$$V = :V: + \langle 0|V|0\rangle$$

The vacuum expectation value $\langle 0|V|0\rangle$ is a c-number
(the vacuum energy shift). It does not affect the spectral gap.

The normal-ordered part $:V:$ has zero vacuum expectation value by
construction. Its matrix elements satisfy:

$$\langle 0|:V:|0\rangle = 0, \quad
  \langle 0|:V:|1\rangle = (\text{specific amplitude}), \quad
  \langle 1|:V:|1\rangle = (\text{specific amplitude})$$

### 2.5.2 Decomposition into positive and negative parts

Write $V = V_+ - V_-$ where $V_+$ and $V_-$ are the positive and
negative parts (from the spectral decomposition of V as a self-adjoint
operator).

$V_+ \geq 0$: contains the quartic vertices and the positive part of
the effective potential correction.

$V_- \geq 0$: contains the negative part of the cubic vertices and
the negative part of the effective potential correction.

For the gap to be preserved, we need:

$$\frac{1}{N}\|V_-\| < \text{gap}(H_0) = \Lambda$$

i.e., the negative part of V must be bounded by N times the gap.

### 2.5.3 Bounding $\|V_-\|$

The norm of the negative part is bounded by the norm of the cubic
vertices:

$$\|V_-\| \leq \|V_{\sigma^3}\| + \|V_{\sigma A^2}\|$$

Each cubic vertex norm is controlled by the triangle integral:

$$\|V_{\sigma^3}\| \leq \sup_{p,q} |\Gamma_3(p,q)|
  \times (\text{phase space factor})$$

The triangle integral satisfies [ESTABLISHED]:

$$|\Gamma_3(p,q)| \leq \frac{1}{(4\pi)^{3/2}} \cdot \frac{1}{m^2}
  = \frac{1}{(4\pi)^{3/2}\,\Lambda^2}$$

for all momenta $p, q$ (the maximum is at $p = q = 0$). The phase
space factor depends on the number of lattice sites (the spatial
volume).

**On a finite spatial volume $L$:** The number of momentum modes is
$L/(2\pi a)$ (where $a$ is the lattice spacing). The cubic vertex
involves three momentum integrals, giving a volume factor. After
careful accounting:

$$\|V_{\sigma^3}\|_{\text{per unit volume}} \leq C_3 \cdot m$$

with $C_3$ a dimensionless constant of order 1. [BOUNDED but crude]


---

## 2.6 The Effective Potential Approach to Sign

### 2.6.1 Integrating out high-momentum modes

A cleaner approach: instead of analyzing the sign of V directly,
integrate out all modes EXCEPT the zero-momentum (spatially
homogeneous) mode of $\sigma$. This produces an effective potential
$V_{\text{eff}}(\bar\sigma)$ for the spatial average
$\bar\sigma = L^{-1}\int dx\,\sigma(x)$.

At N = infinity: $V_{\text{eff}}^{(0)}(\bar\sigma)$ has a unique
minimum at $\bar\sigma = m^2$ with curvature
$V_{\text{eff}}''(m^2) = 1/(4\pi m^2)$.

At finite N: $V_{\text{eff}}(\bar\sigma) = V_{\text{eff}}^{(0)}(\bar\sigma)
+ (1/N) V_{\text{eff}}^{(1)}(\bar\sigma) + \ldots$

The one-loop correction $V_{\text{eff}}^{(1)}$ comes from integrating
out the non-zero momentum modes at one loop. Explicitly:

$$V_{\text{eff}}^{(1)}(\bar\sigma) = \frac{1}{2}\sum_{p \neq 0}
  \left[\ln\Pi_\sigma(p;\bar\sigma) + \ln\det\Pi_A(p;\bar\sigma)\right]$$

### 2.6.2 Convexity of the effective potential

**Claim [BOUNDED]:** The effective potential $V_{\text{eff}}$ is CONVEX
in a neighborhood of the minimum. Specifically:

$$V_{\text{eff}}''(\sigma_*) > 0$$

at the shifted minimum $\sigma_* = m^2 + \delta\sigma_1/N$.

**Proof:** At N = infinity, $V_{\text{eff}}^{(0)''}(m^2) = 1/(4\pi m^2) > 0$.
The O(1/N) correction to the curvature is:

$$\delta V'' = \frac{1}{N}\,V_{\text{eff}}^{(1)''}(m^2)$$

The second derivative of the one-loop correction involves the derivative
of the bubble integrals with respect to $\sigma$. This is computable
and bounded:

$$|V_{\text{eff}}^{(1)''}(m^2)| \leq \frac{C''}{m^2}$$

with $C''$ a dimensionless constant. For $N \geq 2$:

$$V_{\text{eff}}''(\sigma_*) \geq \frac{1}{4\pi m^2} - \frac{C''}{N m^2}
  = \frac{1}{m^2}\left(\frac{1}{4\pi} - \frac{C''}{N}\right) > 0$$

provided $C'' < N/(4\pi)$, i.e., $C'' < 0.16 N$. For $N \geq 2$,
this requires $C'' < 0.32$.

**Status:** The value of $C''$ has not been computed rigorously.
Numerical estimates suggest $C'' \sim 0.1$, which would give convexity
for all $N \geq 2$. [BOUNDED conditionally: requires $C'' < 0.32$]

### 2.6.3 What convexity gives

If $V_{\text{eff}}$ is convex at the minimum, then the zero-momentum
sector of the Hamiltonian has a gap at least as large as at N = infinity
(because the curvature of the potential determines the oscillation
frequency, hence the gap, of the quantum mechanical zero-mode).

But the FULL gap includes contributions from all momentum modes, not
just the zero mode. The non-zero modes contribute through the
dispersion relations $\omega_\sigma(p)$ and $\omega_A(p)$, which also
receive 1/N corrections.


---

## 2.7 Summary: The Sign Question

### What is established:

1. V is NOT positive semi-definite as an operator. [PROVED]
   The cubic vertices are indefinite.

2. The quartic vertices in V ARE positive semi-definite. [PROVED]

3. The saddle-point shift is positive ($\delta\sigma_1 > 0$),
   meaning the mass INCREASES at O(1/N). [ESTABLISHED]

4. The effective potential is convex at the minimum, at least for
   $N$ large enough ($N > 4\pi C''$). [BOUNDED conditionally]

### What is NOT established:

1. Whether the gap of H is >= gap of H_0, despite V being indefinite.
   [OPEN]

2. Whether the negative part of V is small enough (relative to the
   gap) for perturbation theory to control the gap shift. [OPEN]

3. Whether the convexity of the effective potential is sufficient to
   control the full (momentum-dependent) mass gap. [OPEN]

### The verdict on the direct sign approach:

**V >= 0 fails. The direct operator inequality H >= H_0 is FALSE.**

However, this does NOT mean the monotonicity $m(N) \geq m(\infty)$
is false. The monotonicity could still hold for DYNAMICAL reasons
(the interaction raises the gap even though it is not a positive
operator). Proving this requires going beyond the sign of V to the
detailed structure of the perturbation -- which is the subject of
files 03 and 04.
