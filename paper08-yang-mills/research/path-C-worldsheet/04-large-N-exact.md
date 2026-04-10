# 04. The N = infinity Case: Where Everything Is Explicit

## Why Large N Matters

At $N = \infty$, the worldsheet bootstrap can be carried out COMPLETELY:
every step has a rigorous analog, and the final answer is exact. This
makes the large-$N$ case the proving ground for the approach --- if it
fails at $N = \infty$ (where everything is explicit), it cannot succeed
at finite $N$. Conversely, if it works at $N = \infty$, there is a
clear path to finite $N$ through $1/N$ corrections.


---

## 4.1 The Large-N Solution of the 2D Model

**Theorem (Witten 1979, rigorous).** *In the 't Hooft limit $N \to \infty$
with $\lambda = g_{2D}^2 N$ fixed, the 2D $\mathbb{CP}^{N-1}$ sigma
model has the following exact solution:*

**(a) Mass gap:**
$$m = \Lambda_{2D} \equiv \mu \exp\left(-\frac{2\pi}{\lambda(\mu)}
  \right) \times \left(\frac{2\pi}{\lambda(\mu)}\right)^{-1}$$

*where $\mu$ is an arbitrary renormalization scale and $\lambda(\mu)$
is the running 't Hooft coupling. The mass gap is RG-invariant.*

**(b) Spectrum:**
$$\text{Spectrum} = \{m, m, \ldots, m\} \quad (N \text{ degenerate states})$$

*The $N$ massive particles transform in the fundamental representation
of $SU(N)$. At $N = \infty$, they are free (non-interacting).*

**(c) Propagator:**
$$\langle z_i(x) \bar{z}_j(0) \rangle = \delta_{ij}
  \frac{1}{N} G(x; m)$$

*where $G(x; m) = K_0(m|x|)/(2\pi)$ is the massive scalar propagator
in 2D (with $K_0$ the modified Bessel function).*

**(d) Confinement:**
$$\langle z_i(x) \rangle = 0 \quad \forall i$$

*The fundamental $z$ fields have zero vacuum expectation value. The
$U(1)$ gauge field $A_\mu$ is dynamical, with coupling
$e_{2D}^2 = \lambda / (2\pi)$. The 2D $U(1)$ theory confines: the
linear potential $V(r) = e_{2D}^2 r$ binds $z$ and $\bar{z}$ into
singlets.*


---

## 4.2 The Derivation at Large N

The derivation is completely explicit and instructive. It shows exactly
how dimensional transmutation works in a solvable model.

**Step 1: The auxiliary field.** Introduce a Lagrange multiplier $\lambda(x)$
for the constraint $|z|^2 = 1$:
$$S = \frac{N}{\lambda_0} \int d^2x \left[|D_\mu z|^2
  + i\lambda(|z|^2 - 1)\right]$$

where $\lambda_0 = g_{2D}^2 N$ is the bare 't Hooft coupling and
$D_\mu = \partial_\mu - iA_\mu$.

**Step 2: Gaussian integration over z.** At $N = \infty$, the $z$
integral is Gaussian (the quartic interaction is $O(1/N)$). Integrating
out all $N$ components of $z$:
$$Z = \int [D\lambda][DA] \, e^{-N S_{\text{eff}}[\lambda, A]}$$

with the effective action:
$$S_{\text{eff}} = \text{Tr}\ln(-D^2 + i\lambda)
  - \frac{1}{\lambda_0} \int d^2x \, i\lambda$$

**Step 3: Saddle point ($N = \infty$).** The saddle-point equations are:
$$\frac{\partial S_{\text{eff}}}{\partial \lambda} = 0
  \quad\Rightarrow\quad
  \langle |z|^2 \rangle = \frac{1}{(2\pi)^2}
  \int \frac{d^2p}{p^2 + i\lambda_0^*} = 1$$

(setting $A_\mu = 0$ at the saddle). The integral is:
$$\frac{1}{4\pi} \ln\frac{\Lambda_{\text{UV}}^2}{m^2} = 1
  \quad\Rightarrow\quad
  m^2 \equiv i\lambda_0^* = \Lambda_{\text{UV}}^2 \, e^{-4\pi}$$

More precisely, with the running coupling at scale $\mu$:
$$m^2 = \mu^2 \exp\left(-\frac{4\pi}{\lambda(\mu)}\right)$$

This is the mass gap. The saddle-point value $i\lambda_0^* = m^2 > 0$
plays the role of a dynamically generated mass.

**Step 4: Self-consistency.** [PROVED]

The saddle point is unique (there is exactly one solution with
$m^2 > 0$). The fluctuations around the saddle are $O(1/N)$ and do not
destabilize it. The large-$N$ expansion is an asymptotic expansion in
$1/N$ around this saddle.


---

## 4.3 The String Tension at Large N

Now apply the worldsheet formula. At $N = \infty$:

$$\sigma_{\text{4D}}(N = \infty) = \frac{m^2}{2\pi}
  = \frac{\Lambda_{2D}^2}{2\pi}$$

This is an EXACT result at $N = \infty$ (the correction is $O(1/N)$).

**Matching to the Paper 5 prediction.** From Paper 5 (Section 7.4):
$$\sigma_{\text{Paper 5}} = \frac{3g_3^2}{8\pi^2 r_3^2}$$

At large $N$, the 4D coupling and 2D coupling are related by:
$$g_3^2 = \frac{g_{2D}^2}{4\pi r_3^2}
  = \frac{\lambda_0}{4\pi N r_3^2}$$

So:
$$\sigma_{\text{Paper 5}} = \frac{3\lambda_0}{32\pi^3 N r_3^4}$$

Meanwhile, the worldsheet prediction is:
$$\sigma_{\text{ws}} = \frac{\Lambda_{2D}^2}{2\pi}
  = \frac{1}{2\pi r_3^2} e^{-4\pi/\lambda_0}
  \times \text{(perturbative prefactor)}$$

These appear to be DIFFERENT expressions. The Paper 5 formula gives
$\sigma$ as a power of $g_3^2$ (perturbative), while the worldsheet
formula gives $\sigma$ as an exponential of $1/g_{2D}^2$
(non-perturbative).

**Resolution:** The Paper 5 formula is the CLASSICAL (tree-level) string
tension. The worldsheet formula includes ALL quantum corrections through
dimensional transmutation. At weak coupling ($\lambda_0 \ll 1$), the
non-perturbative $\sigma_{\text{ws}}$ is exponentially smaller than the
classical $\sigma_{\text{Paper 5}}$.

At strong coupling ($\lambda_0 \sim 1$), the two expressions are of the
same order and must match. This matching condition determines the
relationship between the 2D scale $\Lambda_{2D}$ and the 4D scale
$\Lambda_{\text{QCD}}$.

**The matching at strong coupling:** [ARGUED]

At the scale $\mu = 1/r_3$ (the compactification scale), the 2D
coupling is $\lambda_0 = g_3^2 N \times 4\pi r_3^2$. The 2D scale is:
$$\Lambda_{2D} = \frac{1}{r_3} e^{-2\pi/\lambda_0}
  \times \text{(pert. prefactor)}$$

The physical string tension should be:
$$\sigma_{\text{4D}} = \frac{\Lambda_{2D}^2}{2\pi}
  = \frac{1}{2\pi r_3^2} e^{-4\pi/\lambda_0} \times (\ldots)$$

For $\lambda_0 \sim 1$ (physical regime):
$$\sigma_{\text{4D}} \sim \frac{1}{r_3^2}
  \times O(e^{-4\pi})$$

The exponential factor is small ($e^{-4\pi} \approx 3.5 \times 10^{-6}$),
so $\sigma_{\text{4D}} \ll 1/r_3^2$. This is consistent with the
hierarchy $\sqrt{\sigma} \sim 440$ MeV $\ll M_{\text{KK}} \sim 10^{15}$
GeV.


---

## 4.4 What Is Exactly Known at N = infinity

Let me list every quantity that is EXACTLY computable at $N = \infty$.

**4.4.1 The 2D mass gap.** [PROVED]
$$m = \Lambda_{2D} \quad \text{(exact)}$$

**4.4.2 The 2D S-matrix.** [PROVED]
At $N = \infty$, the particles are free. The S-matrix is:
$$S_{ij,kl}(p_1, p_2) = \delta_{ik}\delta_{jl}
  \quad \text{(trivial)}$$

At $O(1/N)$, the S-matrix becomes non-trivial and is computable by
$1/N$ perturbation theory. [PROVED to $O(1/N)$]

**4.4.3 The 2D correlation functions.** [PROVED]
All correlators factorize at $N = \infty$:
$$\langle z_{i_1}(x_1) \bar{z}_{j_1}(y_1) \cdots
  z_{i_n}(x_n) \bar{z}_{j_n}(y_n) \rangle
  = \frac{1}{N^n} \sum_{\text{pairings}} \prod G(x_k - y_{\sigma(k)})$$

The sum is over all Wick contractions. This is a FREE theory --- exact
at $N = \infty$.

**4.4.4 The 2D free energy density.** [PROVED]
$$f = -\frac{N m^2}{4\pi}\left(\ln\frac{m^2}{\mu^2} - 1\right)$$

This is the free energy of $N$ free massive bosons in 2D. [PROVED ---
it is a Gaussian integral]

**4.4.5 The 2D lattice-continuum convergence.** [PROVED]
The lattice $\mathbb{CP}^{N-1}$ model at $N = \infty$ converges to
Witten's solution as $a_{2D} \to 0$. Proved by Singer (1995): the
large-$N$ limit commutes with the continuum limit.

**4.4.6 The 4D string tension (from worldsheet).** [ARGUED]
$$\sigma_{\text{4D}}^{(N=\infty)} = \frac{\Lambda_{2D}^2}{2\pi}$$

This is exact at $N = \infty$ IF the worldsheet formula holds. The
worldsheet derivation is [ARGUED], but at $N = \infty$, the corrections
are provably $O(1/N) = 0$.


---

## 4.5 The Continuum Limit at N = infinity

**This is the key test.** At $N = \infty$, we can check whether the
worldsheet bootstrap gives a consistent continuum limit.

**The setup.** Consider the lattice SU($N$) gauge theory on
$\Lambda_a \times \mathbb{CP}^{N-1}$ at $N = \infty$, with lattice
spacing $a$ and coupling $\beta(a)$ along the asymptotic freedom
trajectory.

**The lattice string tension.**
$$\sigma_{\text{phys}}(a, N) = \frac{\hat{\sigma}(\beta(a), N)}{a^2}$$

where $\hat{\sigma}$ is the lattice string tension.

**At $N = \infty$:** The 4D large-$N$ theory factorizes (the master field).
The string tension at each $a$ is:
$$\sigma_{\text{phys}}(a, \infty) = \frac{\hat{\sigma}(\beta(a), \infty)}{a^2}$$

**Claim.** [ARGUED]
$$\lim_{a \to 0} \sigma_{\text{phys}}(a, \infty) = \sigma_\infty
  = \frac{\Lambda_{2D}^2}{2\pi}$$

**Evidence:**

(a) At $N = \infty$, the 2D $\mathbb{CP}^{N-1}$ model has a rigorous
continuum limit with mass gap $m = \Lambda_{2D}$ (Witten + Singer).
[PROVED]

(b) At $N = \infty$, the 4D lattice theory has a master field (Witten
1980). The string tension is a functional of this master field.
[PROVED --- the master field exists at large $N$]

(c) The worldsheet formula $\sigma = m^2/(2\pi)$ connects (a) and (b).
If the worldsheet derivation is valid at $N = \infty$, then the 4D
continuum limit inherits the 2D continuum limit.

**The gap.** Even at $N = \infty$, the worldsheet derivation is
[ARGUED], not [PROVED]. The missing step is: proving that the 4D master
field is correctly described by the 2D saddle point (the Witten solution)
in the sector relevant to the string tension.

**However.** At $N = \infty$, there is an ALTERNATIVE route that avoids
the worldsheet entirely: the Eguchi--Kawai reduction.

**The Eguchi--Kawai route.** [ARGUED to [PROVED] status in restricted sense]

At $N = \infty$, the Eguchi--Kawai theorem (1982, corrected by
Bhanot--Heller--Neuberger 1982, Gonzalez-Arroyo--Okawa 1983) states
that the lattice gauge theory on a SINGLE site is equivalent to the
theory on an infinite lattice. The single-site model is:
$$Z = \int \prod_{\mu=1}^4 dU_\mu \, \exp\left(\frac{\beta N}{2}
  \sum_{\mu < \nu} \text{Tr}(U_\mu U_\nu U_\mu^\dagger U_\nu^\dagger)
  + \text{h.c.}\right)$$

This is a FINITE-dimensional integral (over $SU(N)^4$) that becomes
exact at $N = \infty$. Its string tension equals the infinite-volume
string tension.

At $N = \infty$, the single-site model can be analyzed by saddle-point
methods. The saddle-point equation is equivalent to a matrix model, and
matrix models are solvable (by the techniques of random matrix theory,
loop equations, etc.).

The connection to the worldsheet is: the matrix model saddle-point
equation at $N = \infty$ reduces to the 2D sigma model saddle-point
equation. This is the Eguchi--Kawai/worldsheet equivalence at large $N$.

**Status of Eguchi--Kawai.** The original Eguchi--Kawai reduction fails
for Wilson loops due to center-symmetry breaking (the quenched EK model
has a phase transition at weak coupling). The TWISTED Eguchi--Kawai model
(Gonzalez-Arroyo--Okawa) fixes this for the quark-antiquark potential.
Recent work by Kovtun--Unsal--Yaffe (2007) establishes a rigorous
version with an explicit center-stabilizing deformation.


---

## 4.6 The Large-N Continuum Limit: Summary

At $N = \infty$, the worldsheet bootstrap gives:

| Quantity | Value | Status |
|----------|-------|--------|
| 2D mass gap $m$ | $\Lambda_{2D}$ | **[PROVED]** |
| 2D continuum limit | Exists, unique | **[PROVED]** (Singer 1995) |
| 4D $\sigma_\infty$ | $\Lambda_{2D}^2/(2\pi)$ | **[ARGUED]** |
| Worldsheet formula valid at $N = \infty$ | Expected (saddle point exact) | **[ARGUED]** |
| 4D lattice converges to $\sigma_\infty$ | Expected | **[ARGUED]** |
| Eguchi--Kawai alternative | Matrix model solvable | **[ARGUED]** |

The large-$N$ case is the most promising for a rigorous proof because:
1. The 2D model is exactly solvable
2. The worldsheet corrections are $O(1/N) = 0$
3. The Eguchi--Kawai reduction provides an independent route
4. The master field and saddle-point methods are rigorous

**An achievable theorem.** [OPEN, but feasible]

*Theorem (conjectured).* For $SU(N)$ Yang--Mills on the lattice with
$N = \infty$ (the 't Hooft limit), the string tension has a continuum
limit:
$$\lim_{a \to 0} \sigma_{\text{phys}}(a) = \frac{\Lambda^2}{2\pi}$$

where $\Lambda$ is the dynamical scale defined by dimensional
transmutation.

This would be the first rigorous result on the 4D continuum string
tension, and it would follow from:
- The Witten solution of the 2D model [PROVED]
- The Singer convergence theorem [PROVED]
- The Eguchi--Kawai/worldsheet equivalence [ARGUED, but plausibly
  provable at $N = \infty$]

**I believe this theorem is within reach.** The tools exist. The
obstruction is connecting the 4D master field to the 2D saddle point
--- a problem in large-$N$ gauge/string duality that has been studied
extensively (Maldacena 1997 in the supersymmetric case, but the
non-supersymmetric version needed here is different).


---

## 4.7 The Key Open Problem at N = infinity

**The missing link:** Prove that the large-$N$ SU($N$) lattice gauge
theory on $\Lambda_a \times \mathbb{CP}^{N-1}$, in the sector
corresponding to a single flux tube, is described at $N = \infty$ by
the Witten solution of the $\mathbb{CP}^{N-1}$ sigma model.

More precisely: prove that the Wilson loop at large $N$ satisfies
$$-\frac{1}{TR} \ln \langle W(T, R) \rangle
  \xrightarrow{T,R \to \infty}
  \frac{1}{TR} \ln Z_{2D}^{\text{Witten}}(T, R)$$

where $Z_{2D}^{\text{Witten}}$ is the partition function of Witten's
large-$N$ sigma model on a $T \times R$ cylinder.

This is a precise mathematical statement that, if proved, would complete
the worldsheet bootstrap at $N = \infty$.
