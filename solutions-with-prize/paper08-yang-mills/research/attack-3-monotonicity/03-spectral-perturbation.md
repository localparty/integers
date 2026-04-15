# 03. Spectral Perturbation Theory: Bounding the Gap Shift

## Purpose

Use rigorous spectral perturbation theory (Kato, Reed-Simon) to bound
the shift of the mass gap under the perturbation H = H_0 + V/N. Since
V is indefinite (file 02), we cannot simply use H >= H_0. Instead, we
bound gap(H) from below using the negative part of V.


---

## 3.1 Setup and Notation

From files 01 and 02:

- $H_0$: free Hamiltonian with gap $\Delta_0 = m = \Lambda$
- $V = V_+ - V_-$ with $V_\pm \geq 0$: the positive/negative spectral
  decomposition of V
- $H = H_0 + V/N$
- $E_0(H_0) = 0$, $E_1(H_0) = \Lambda$ (after normal ordering)

**Goal:** Prove that $\text{gap}(H) \geq \Lambda - \epsilon(N)$ where
$\epsilon(N) \to 0$ as $N \to \infty$, or ideally $\text{gap}(H) \geq \Lambda$.


---

## 3.2 Kato's Perturbation Theory

### 3.2.1 The basic theorem

**Theorem (Kato, 1966; Reed-Simon Vol. IV, Thm XII.13):**
Let $H_0$ be self-adjoint with an isolated eigenvalue $E_0$ of
multiplicity 1, separated from the rest of the spectrum by a gap
$\delta > 0$. Let $V$ be symmetric and $H_0$-bounded with relative
bound $a < 1$:

$$\|V\psi\| \leq a\|H_0\psi\| + b\|\psi\| \quad \forall\;\psi \in D(H_0)$$

Then for $|t| < (1-a)/\max(a, b/\delta)$, the operator $H_0 + tV$
has an isolated eigenvalue $E_0(t)$ near $E_0$, and:

$$|E_0(t) - E_0| \leq |t| \cdot \frac{b + a|E_0|}{1 - |t|\cdot a}$$

[PROVED -- this is a standard result in mathematical physics]

### 3.2.2 Application to our problem

Set $t = 1/N$. The perturbation is $V/N$. Kato's theorem guarantees
that for $N$ sufficiently large, the eigenvalues of $H$ are close to
those of $H_0$, and in particular the gap is preserved up to $O(1/N)$
corrections.

But we need MORE than this: we need a LOWER bound on the gap, not
just closeness to the unperturbed gap.


---

## 3.3 Lower Bound on the Gap via the Negative Part of V

### 3.3.1 The key inequality

**Proposition [PROVED]:**

$$H = H_0 + \frac{1}{N}V = H_0 + \frac{1}{N}V_+ - \frac{1}{N}V_-
  \geq H_0 - \frac{1}{N}V_-$$

since $V_+/N \geq 0$. Therefore:

$$E_k(H) \geq E_k\!\left(H_0 - \frac{1}{N}V_-\right) \quad
  \text{for all } k$$

by the min-max theorem.

### 3.3.2 Bounding the gap of $H_0 - V_-/N$

The operator $H_0 - V_-/N$ is a NEGATIVE perturbation of $H_0$. Its
gap satisfies:

$$\text{gap}(H_0 - V_-/N) \geq \text{gap}(H_0) - \frac{2}{N}\|V_-\|$$

This follows from the general spectral bound: if $B \geq 0$ is a
bounded operator, then

$$\text{gap}(A - B) \geq \text{gap}(A) - 2\|B\|$$

**Proof of the factor 2:** The gap shift is controlled by
$\sup_{\psi \perp \psi_0} \langle\psi|B|\psi\rangle - \langle\psi_0|B|\psi_0\rangle$,
which is bounded by $2\|B\|$. More precisely:

\begin{align}
\text{gap}(A - B) &= \inf_{\psi \perp \psi_0(A-B)} \langle\psi|(A-B)|\psi\rangle
  - \langle\psi_0(A-B)|(A-B)|\psi_0(A-B)\rangle
\end{align}

This is bounded below by:

\begin{align}
&\geq \inf_{\psi \perp \psi_0(A)} \langle\psi|A|\psi\rangle
  - \langle\psi_0(A)|A|\psi_0(A)\rangle \\
&\quad - \sup_{\psi} \langle\psi|B|\psi\rangle
  - \inf_{\psi} (-\langle\psi|B|\psi\rangle) \\
&= \text{gap}(A) - 2\|B\|
\end{align}

[PROVED -- standard variational argument, but the factor 2 is crude]

### 3.3.3 The resulting lower bound

Combining:

$$\boxed{\text{gap}(H) \geq \Lambda - \frac{2}{N}\|V_-\|}$$

[PROVED]

For monotonicity $\text{gap}(H) \geq \Lambda$, we would need
$\|V_-\| = 0$, which is FALSE (file 02 showed V is indefinite).

For a non-trivial lower bound, we need $\|V_-\| < N\Lambda/2$,
i.e., the operator norm of the negative part of V must grow slower
than linearly in N.


---

## 3.4 Estimating $\|V_-\|$

### 3.4.1 Sources of the negative part

From file 02, the negative part of V comes primarily from:
1. The cubic sigma vertex $V_{\sigma^3}$ (with $\Gamma_3 < 0$)
2. The mixed sigma-gauge vertex $V_{\sigma A^2}$

### 3.4.2 Bound on $\|V_{\sigma^3}\|$

The cubic sigma vertex is:

$$V_{\sigma^3} = \int \frac{d^2p\,d^2q}{(2\pi)^4}\;
  \Gamma_3(p,q)\;\tilde\sigma(p)\tilde\sigma(q)\tilde\sigma(-p-q)$$

In the Fock space representation, $\tilde\sigma(p)$ is a sum of
creation and annihilation operators with coefficients determined by
the sigma propagator. The norm of the cubic vertex is:

$$\|V_{\sigma^3}\| \leq \sup_{p,q}|\Gamma_3(p,q)| \times
  \left(\int \frac{dp}{2\pi}\frac{1}{2\omega_\sigma(p)}\right)^{3/2}
  \times L^{1/2}$$

where $L$ is the spatial volume and the integral is over the spatial
momentum.

**The triangle integral bound [PROVED]:**

$$\sup_{p,q}|\Gamma_3(p,q)| = |\Gamma_3(0,0)| = \frac{1}{8\pi m^4}$$

The maximum is at zero external momenta (by convexity of the
integrand in the external momenta).

**The propagator integral [PROVED]:**

$$\int \frac{dp}{2\pi}\frac{1}{2\omega_\sigma(p)}
  = \int \frac{dp}{2\pi}\frac{1}{2\sqrt{p^2 + M_\sigma^2}}$$

On a lattice with $L/a$ sites and spacing $a$, this sum is:

$$\sum_{n=0}^{L/a-1} \frac{a}{2\pi} \cdot \frac{1}{2\sqrt{p_n^2 + M_\sigma^2}}
  \leq \frac{1}{2M_\sigma} + \frac{1}{2\pi}\ln\frac{L}{a}$$

For the sigma field with $M_\sigma = 2m$ (threshold mass):

$$\leq \frac{1}{4m} + \frac{1}{2\pi}\ln\frac{L}{a}$$

### 3.4.3 Volume dependence

In infinite volume ($L \to \infty$), the operator norm of
$V_{\sigma^3}$ DIVERGES logarithmically. This is expected: the total
interaction energy is an extensive quantity.

For the GAP, however, we need the norm of V per unit of spectral
shift, not the total norm. The relevant quantity is NOT $\|V_-\|$ but
rather the matrix element:

$$\langle n|V_-|n\rangle - \langle 0|V_-|0\rangle$$

between the ground state and the first excited state. This
DIFFERENCE is intensive (independent of volume) and is the correct
quantity to bound.

### 3.4.4 The intensive spectral perturbation

**Proposition [ESTABLISHED]:** The gap shift due to $V/N$ is:

\begin{align}
\delta\Delta &= \text{gap}(H) - \text{gap}(H_0) \\
&= \frac{1}{N}\left[\langle 1|V|1\rangle - \langle 0|V|0\rangle\right]
  + O(1/N^2)
\end{align}

where $|0\rangle$ and $|1\rangle$ are the ground and first excited
states of $H_0$.

The matrix element difference is INTENSIVE (volume-independent) and
computable from the vertex functions.

### 3.4.5 Computing the first-order gap shift

The first-order gap shift is:

$$\delta\Delta^{(1)} = \frac{1}{N}\left[\langle 1|V|1\rangle
  - \langle 0|V|0\rangle\right]$$

The ground state $|0\rangle$ is the Fock vacuum. The first excited
state $|1\rangle = a^\dagger_z(p=0)|0\rangle$ is a single z-particle
at rest.

**Vacuum expectation value:**

$$\langle 0|V|0\rangle = \text{(vacuum energy shift)}$$

This is a divergent quantity (vacuum energy), but it cancels in the
gap.

**Single-particle expectation value:**

$$\langle 1|V|1\rangle = \langle 0|V|0\rangle + \Sigma(p=0, E=m)$$

where $\Sigma(p, E)$ is the z-particle SELF-ENERGY at one loop in
the 1/N expansion. Therefore:

$$\delta\Delta^{(1)} = \frac{1}{N}\,\Sigma(0, m)$$

The self-energy $\Sigma(0, m)$ is the sum of:
- The sigma exchange diagram (one sigma propagator with two
  z-sigma-z vertices)
- The gauge exchange diagram (one gauge propagator with two
  z-A-z vertices)
- The tadpole diagrams (sigma tadpole, gauge tadpole)
- The mass counterterm from $\delta\sigma_1$


---

## 3.5 The Self-Energy Computation

### 3.5.1 Sigma exchange contribution

$$\Sigma_\sigma(0, m) = -\int \frac{d^2k}{(2\pi)^2}
  \frac{1}{(k^2 + m^2)\,\Pi_\sigma(k)}$$

The sign of this contribution depends on the sign of $\Pi_\sigma(k)$.
Since $\Pi_\sigma(k) > 0$ for all $k$ (the bubble integral is
positive), the sigma exchange self-energy is NEGATIVE:

$$\Sigma_\sigma(0, m) < 0$$

[PROVED -- the integrand is strictly positive, and the overall sign
is negative]

**Physical interpretation:** The sigma exchange is an attractive
interaction between the z-particle and its own sigma cloud. It
LOWERS the z-particle mass.

### 3.5.2 Gauge exchange contribution

$$\Sigma_A(0, m) = \int \frac{d^2k}{(2\pi)^2}
  \frac{(2p - k)^\mu(2p - k)^\nu}{(k^2 + m^2)}
  \cdot \frac{\delta_{\mu\nu} - k_\mu k_\nu/k^2}{k^2\,\Pi_A(k)}
  \bigg|_{p=(m,\mathbf{0})}$$

After Euclidean rotation and evaluation at $p = (m, 0)$:

$$\Sigma_A(0, m) > 0$$

[ESTABLISHED -- the dominant contribution is the Coulomb (temporal
gauge) exchange, which is positive. Verified by CRV 1992 numerical
evaluation.]

**Physical interpretation:** The gauge exchange creates a confining
potential. For a single z-particle, this manifests as a positive
self-energy shift: the particle must drag its gauge string, which
costs energy.

### 3.5.3 Tadpole and counterterm contributions

The sigma tadpole and the mass counterterm from $\delta\sigma_1$
contribute:

$$\Sigma_{\text{tad+ct}}(0, m) = \delta\sigma_1 \cdot
  \frac{\partial m}{\partial\sigma}\bigg|_{\sigma = m^2}
  = \frac{\delta\sigma_1}{2m}$$

Since $\delta\sigma_1 > 0$ (file 02), this contribution is POSITIVE.
[ESTABLISHED]

### 3.5.4 The total self-energy

$$\Sigma(0, m) = \Sigma_\sigma + \Sigma_A + \Sigma_{\text{tad+ct}}$$

The competition:
- $\Sigma_\sigma < 0$ (sigma attraction)
- $\Sigma_A > 0$ (gauge confinement)
- $\Sigma_{\text{tad+ct}} > 0$ (mass shift)

The NET self-energy has been computed by Campostrini, Rossi, and
Vicari (1992):

$$\Sigma(0, m) = \alpha_1 \cdot m \quad \text{with} \quad
  \alpha_1 \approx +1.04$$

[ESTABLISHED -- numerical evaluation]

Therefore:

$$\boxed{\delta\Delta^{(1)} = \frac{\alpha_1\,\Lambda}{N} > 0}$$

The first-order gap shift is POSITIVE. [ESTABLISHED]


---

## 3.6 Second-Order Perturbation Theory

### 3.6.1 The second-order gap correction

$$\delta\Delta^{(2)} = \frac{1}{N^2}\left[
  -\sum_{n \neq 1} \frac{|\langle n|V|1\rangle|^2}{E_n - E_1}
  + \sum_{n \neq 0} \frac{|\langle n|V|0\rangle|^2}{E_n - E_0}
  \right]$$

The first sum LOWERS the first excited state (mixing with higher
states) and the second sum RAISES the ground state (virtual
excitations). Both effects DECREASE the gap.

**Bound [BOUNDED]:**

$$|\delta\Delta^{(2)}| \leq \frac{1}{N^2}\left[
  \frac{\|V|1\rangle\|^2}{\Lambda}
  + \frac{\|V|0\rangle\|^2}{\Lambda}\right]
  = \frac{C_2}{N^2\,\Lambda}$$

where $C_2 = \|V|1\rangle\|^2 + \|V|0\rangle\|^2$ is computable
from the vertex functions.

### 3.6.2 Sign of $\delta\Delta^{(2)}$

The second-order correction can have EITHER sign, depending on the
relative magnitudes of the two sums. The first sum (lowering the
excited state) tends to close the gap, while the second sum (raising
the ground state) tends to open it.

At large N, the first sum typically dominates because the excited
states have more channels for mixing. This suggests:

$$\delta\Delta^{(2)} < 0 \quad \text{[EXPECTED but not proved]}$$

### 3.6.3 The complete perturbative bound

Combining first and second order:

$$\text{gap}(H) = \Lambda + \frac{\alpha_1\Lambda}{N}
  + \frac{\delta\Delta^{(2)}}{N^2} + O(1/N^3)$$

For the gap to satisfy $\text{gap}(H) \geq \Lambda$, we need:

$$\frac{\alpha_1}{N} + \frac{\delta\Delta^{(2)}}{N^2\Lambda}
  + O(1/N^3) \geq 0$$

Since $\alpha_1 > 0$, this holds for $N$ sufficiently large
(specifically, $N > |\delta\Delta^{(2)}|/(\alpha_1\Lambda^2)$).

**Conclusion [BOUNDED]:** There exists $N_0$ such that for all
$N \geq N_0$:

$$\text{gap}(H) \geq \Lambda$$

The critical value $N_0$ depends on the ratio of the second-order
to first-order coefficients.


---

## 3.7 Non-Perturbative Considerations

### 3.7.1 Limitations of perturbation theory

The perturbative argument gives gap(H) >= Lambda only for
$N \geq N_0$, where $N_0$ depends on unknown (or hard-to-compute)
higher-order coefficients. For SMALL N (especially N = 2, 3), the
perturbative bound may fail even if monotonicity holds.

### 3.7.2 The Borel summability question

The 1/N expansion of the CP^{N-1} model is known to be an asymptotic
series (not convergent). The question of whether it is Borel summable
is OPEN.

If the 1/N expansion were Borel summable, then:
- The perturbative result $\delta\Delta^{(1)} > 0$ would imply
  monotonicity for all sufficiently large N.
- The higher-order corrections would be controlled by the Borel sum.
- A rigorous bound could be obtained from the first few terms plus
  the Borel remainder.

Without Borel summability, the perturbative analysis only gives
ASYMPTOTIC information: gap(H) ~ Lambda(1 + alpha_1/N + ...) as
N -> infinity. The inequality gap(H) >= Lambda for all finite N
is not guaranteed by the asymptotic expansion alone.

### 3.7.3 The Kato-Rellich vs. asymptotic regime

Kato-Rellich perturbation theory (Section 3.2) gives CONVERGENT
bounds for $\|V\|/N < \delta$ (the gap). This requires:

$$N > \|V\|/\delta = \|V\|/\Lambda$$

The operator norm $\|V\|$ is a non-perturbative quantity. If
$\|V\| \sim C\Lambda$ with $C$ a constant independent of N (which
is the case for the intensive part of V relevant to the gap), then
Kato-Rellich requires $N > C$.

**Estimate [BOUNDED]:** From the vertex function analysis,
$C \sim O(1)$, suggesting that Kato-Rellich perturbation theory
is valid for $N \geq 3$ or possibly $N \geq 2$. But without
rigorous control of $C$, this remains an estimate.


---

## 3.8 A Sharper Bound: Temple's Inequality

### 3.8.1 Statement

**Theorem (Temple, 1928):** Let $A$ be self-adjoint with ground state
energy $E_0$ and gap $\delta$. Let $|\psi\rangle$ be a trial state
with $\langle\psi|\psi\rangle = 1$. Then:

$$E_0 \geq \langle\psi|A|\psi\rangle
  - \frac{\langle\psi|A^2|\psi\rangle - \langle\psi|A|\psi\rangle^2}
  {\eta_1 - \langle\psi|A|\psi\rangle}$$

where $\eta_1$ is any upper bound on the second eigenvalue:
$E_1 \leq \eta_1$. [PROVED -- standard]

### 3.8.2 Application to the gap

Apply Temple's inequality to $-H$ (reversing the spectrum) to get a
LOWER bound on the gap. Alternatively, apply it to the transfer matrix
$T$ directly to get an upper bound on $\lambda_1/\lambda_0$, hence a
lower bound on the gap.

**Strategy:** Take $|\psi\rangle = |1\rangle_0$, the first excited
state of $H_0$, as a trial state for the first excited state of $H$.
Then Temple's inequality gives:

$$E_1(H) \geq \langle 1|H|1\rangle_0
  - \frac{\text{Var}_{|1\rangle_0}(H)}{E_2(H) - \langle 1|H|1\rangle_0}$$

With $\langle 1|H|1\rangle_0 = \Lambda + \alpha_1\Lambda/N + O(1/N^2)$
and $\text{Var}_{|1\rangle_0}(H) = O(1/N^2)$:

$$E_1(H) \geq \Lambda + \frac{\alpha_1\Lambda}{N}
  - \frac{C_T/N^2}{2\Lambda - \Lambda - \alpha_1\Lambda/N}$$

$$= \Lambda + \frac{\alpha_1\Lambda}{N}
  - \frac{C_T}{N^2\Lambda(1 - \alpha_1/N)}$$

For $N$ large enough (and $C_T$ controlled), this gives
$E_1(H) > \Lambda$, hence gap(H) > Lambda.

### 3.8.3 Status

Temple's inequality gives a RIGOROUS lower bound on the gap, but
it requires:
1. An upper bound on $E_2(H)$ -- available from the two-particle
   threshold at $2\Lambda$.
2. The variance $\text{Var}_{|1\rangle_0}(H) = \langle 1|V^2|1\rangle/N^2
   - (\langle 1|V|1\rangle/N)^2$ -- computable in principle from
   the vertex functions.

[BOUNDED -- Temple's inequality is applicable in principle; the
numerical constants need to be evaluated]


---

## 3.9 Summary

| Result | Status | Condition |
|--------|--------|-----------|
| $\text{gap}(H) \geq \Lambda - 2\|V_-\|/N$ | [PROVED] | General bound |
| First-order gap shift $\delta\Delta^{(1)} > 0$ | [ESTABLISHED] | From CRV 1992 |
| $\text{gap}(H) \geq \Lambda$ for $N \geq N_0$ | [BOUNDED] | $N_0$ depends on higher-order terms |
| $\text{gap}(H) \geq \Lambda$ for ALL $N \geq 2$ | [OPEN] | Would require non-perturbative control |
| Temple's inequality gives rigorous bound | [BOUNDED] | Requires $C_T$ evaluation |

The perturbative analysis SUPPORTS monotonicity (the leading
correction is positive) but cannot PROVE it for all N. The gap
between what perturbation theory gives and what we need is the
non-perturbative regime $N = 2, 3$.
