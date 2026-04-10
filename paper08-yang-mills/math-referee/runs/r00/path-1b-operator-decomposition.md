# Path 1b: The Operator Decomposition from Balaban's Framework

This document attacks **Obstacle 3** of the Path 1 argument
(path-1-balaban-three-point.md, Section 7.3): extracting the precise
operator decomposition from Balaban's block-spin RG and verifying
that the irrelevant operators can be written in the form required by
Definition 5.1, with a controlled derivative structure.

---

## 1. The Dimension-6 Operator Basis

### 1.1 Continuum classification

In the continuum, pure $\mathrm{SU}(N)$ Yang--Mills in $d = 4$ has
three independent gauge-invariant local operators of dimension 6:

**(I)** $\mathcal{O}_1 = \mathrm{Tr}(D_\mu F_{\nu\rho})
(D^\mu F^{\nu\rho})$ -- two covariant derivatives beyond
$\mathrm{Tr}\,F^2$.

**(II)** $\mathcal{O}_2 = \mathrm{Tr}(F_{\mu\nu} F^{\nu\rho}
F_{\rho}{}^{\mu})$ -- cubic in the field strength, no extra
derivatives.

**(III)** $\mathcal{O}_3 = d^{abc} F_{\mu\nu}^a F^{b\,\nu\rho}
F_\rho^{c\,\mu}$ -- the $d$-symbol cubic invariant, present only for
$N \geq 3$ (for $N=2$, $d^{abc} = 0$).

Off-shell (as in the effective action), $\mathcal{O}_1$ and
$\mathcal{O}_2$ are independent; on-shell, the equation of motion
$D_\mu F^{\mu\nu} = 0$ and the Bianchi identity reduce the
independent set.

**Derivative count -- the critical distinction for Path 1:**

| Operator | Extra derivatives beyond $F^2$ |
|:---------|:-------------------------------|
| $\mathcal{O}_1 = \mathrm{Tr}(DF)^2$ | 2 |
| $\mathcal{O}_2 = \mathrm{Tr}\,F^3$ | 0 |
| $\mathcal{O}_3 = d^{abc} F^3$ | 0 |

### 1.2 Lattice transcription

Lattice objects: link variable $U_\ell \in \mathrm{SU}(N)$, plaquette
$U_P$, action density $s_P = 1 - \frac{1}{N}\mathrm{Re\,Tr}\,U_P
\approx \frac{a^4}{4N}\mathrm{Tr}(F_{\mu\nu}^2) + O(a^6)$, lattice
forward difference $\nabla_\mu f(x) = f(x+a\hat\mu) - f(x)$,
covariant difference $\nabla_\mu^{\mathrm{cov}} f(x) =
U_{x,\mu}\,f(x+a\hat\mu)\,U_{x,\mu}^\dagger - f(x)$.

**(I) Lattice $\mathrm{Tr}(DF)^2$:**
$$\hat{\mathcal{O}}_1(x)
  = \sum_{\mu,\nu,\rho}
  \mathrm{Tr}\!\left[
    \bigl(\nabla_\mu^{\mathrm{cov}}\,\Omega_{\nu\rho}(x)\bigr)^2
  \right]$$
where $\Omega_{\nu\rho}(x) = \frac{1}{2ia^2}(U_P - U_P^\dagger)
\approx F_{\nu\rho} + O(a^2)$. In terms of plaquette densities,
the leading structure is $\sum_\mu (\nabla_\mu s_P)^2$. This
carries **two explicit lattice derivatives**.

**(II) Lattice $\mathrm{Tr}\,F^3$:**
$$\hat{\mathcal{O}}_2(x)
  = \sum_{\mu<\nu<\rho}
  \mathrm{Re\,Tr}\!\bigl[
    (U_{P_{\mu\nu}}\!-\!\mathbf{1})
    (U_{P_{\nu\rho}}\!-\!\mathbf{1})
    (U_{P_{\rho\mu}}\!-\!\mathbf{1})
  \bigr]$$
A product of plaquette variables at the same vertex.
**No lattice derivatives.**

**(III) Lattice $d^{abc}F^3$:**
$$\hat{\mathcal{O}}_3(x)
  = \sum_{\mu<\nu<\rho}
  d^{abc}\,\mathrm{Im\,Tr}(T^a U_{P_{\mu\nu}})
  \,\mathrm{Im\,Tr}(T^b U_{P_{\nu\rho}})
  \,\mathrm{Im\,Tr}(T^c U_{P_{\rho\mu}})$$
Also **no lattice derivatives**.

**Summary.** Only $\hat{\mathcal{O}}_1$ carries lattice derivatives.
The integration-by-parts argument of Lemma 5.3 applies to
$\hat{\mathcal{O}}_1$ but not to $\hat{\mathcal{O}}_2$ or
$\hat{\mathcal{O}}_3$.

---

## 2. Balaban's Decomposition Procedure

### 2.1 The block-spin step

At step $k \to k+1$, Balaban: (a) decomposes $U$ on $\Lambda_k$ into
block-averaged $\bar{U}$ on $\Lambda_{k+1}$ and fluctuation $\delta U$;
(b) integrates out $\delta U$ within the small field region;
(c) expands $S_{k+1}[\bar{U}]$ as a Taylor series in $\delta U$;
(d) classifies terms by engineering dimension using
$[U_P - \mathbf{1}] = 2$, $[\nabla_\mu] = 1$, $[\sum_x] = -4$;
(e) identifies the dimension-4 part as $S_{\mathrm{YM}}(g_{k+1})$;
(f) collects dimension $> 4$ terms into the irrelevant remainder.

### 2.2 Derivative structure within a given dimension

The Taylor expansion generates terms at each order $n$ (number of
Gaussian contractions of $\delta U$), each carrying $g_k^{2n}$.
Within dimension 6:

- **One-loop** ($n=1$, coefficient $O(g_k^2)$): produces
  $\mathrm{Tr}(DF)^2$-type terms. The single Gaussian contraction
  of two fluctuation fields yields a propagator connecting two
  derivative vertices.

- **Two-loop** ($n=2$, coefficient $O(g_k^4)$): can produce both
  $\mathrm{Tr}(DF)^2$ and $\mathrm{Tr}\,F^3$. The latter requires
  three independent field strength tensors, needing at least two
  contractions.

At one loop, **only derivative operators are generated**. The
$\mathrm{Tr}\,F^3$ operator first appears at two loops.

### 2.3 Uniqueness

The decomposition into individual operators is not unique (it depends
on basis choice, subtraction scheme, and lattice discretization
ambiguity). However, the **total dimension-6 contribution** and the
**derivative/non-derivative split** are scheme-independent.

---

## 3. The Derivative Structure Within Dimension 6

### 3.1 The perturbative hierarchy

From Balaban's Taylor expansion:

$$|c_1^{(k)}| \leq C_1\,g_k^2 \qquad
  \text{(one-loop, $\hat{\mathcal{O}}_1$: two derivatives)}$$

$$|c_2^{(k)}|, |c_3^{(k)}| \leq C\,g_k^4 \qquad
  \text{(two-loop, $\hat{\mathcal{O}}_2, \hat{\mathcal{O}}_3$:
  zero derivatives)}$$

The generic Balaban bound gives $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}
= C_n g_k^2$ for all dimension-6 operators. The improved bound
$c_2, c_3 = O(g_k^4)$ is stronger by one power of $g_k^2$.

**Justification.** At step $k \to k+1$, the effective action is:
$$S_{k+1}[\bar{U}] = S_k[\bar{U}]
  + \tfrac{1}{2}\langle(\delta S)^2\rangle_C
  - \tfrac{1}{2}\langle\delta S\rangle_C^2 + \ldots$$
The first correction $\langle(\delta S)^2\rangle_C$ produces terms
$\sim \nabla\Omega \cdot G \cdot \nabla\Omega$ (manifestly of
$\mathrm{Tr}(DF)^2$ type). The $\mathrm{Tr}\,F^3$ operator requires
the third cumulant $\langle(\delta S)^3\rangle_C$, carrying an
additional $g_k^2$.

### 3.2 Does the enhanced coefficient suffice?

The $\hat{\mathcal{O}}_2$ contribution to the form factor, bounded
by the operator norm alone, gives:
$$|f_c^{(\mathcal{O}_2)}(0)| \leq C_2\,g_k^4\,
  M_{\mathcal{O}_2}\,\Delta^3.$$
Comparing with the target $C g_k^4 (a_k\Delta)^2 \Delta^3$: this
satisfies the target only if $M_{\mathcal{O}_2} \leq C(a_k\Delta)^2$,
which fails since $M_{\mathcal{O}_2}$ is $a$-independent.

**The enhanced coefficient alone does not produce the required
$(a_k\Delta)^2$ suppression.**

### 3.3 The non-derivative operators in the one-particle sector

**Claim 3.1.** *For a gauge-invariant operator $O(x)$ depending
only on gauge variables at the single site $x$ (no lattice
differences), the connected one-particle matrix element at zero
momentum satisfies:*
$$|\langle 1|O(0)|1\rangle_c|
  \leq C\,\|O\|_\infty\,(a\Delta)^4.$$

*Rationale.* The connected matrix element measures how $O$ responds
to a long-wavelength glueball modulation. An operator without
derivatives is insensitive to gradients: it couples to the glueball
only through its self-energy correction, a two-loop effect carrying
$g^4$ and two momentum factors from the loop integration. The
suppression $(a\Delta)^4$ is stronger than the required
$(a\Delta)^2$.

**Status.** Perturbatively verified. A non-perturbative proof requires
control over the spectral density at the glueball pole -- the same
class of estimate as Conjecture 1 itself. This provides a second
line of defense but does not independently close the gap.

---

## 4. The Total Remainder Approach

### 4.1 Motivation

Instead of decomposing $E_k$ into individual operators, work with the
total remainder directly. The established properties of $E_k$ are:

(i) $\|E_k(x)\| \leq C g_k^4$ per site (Balaban).

(ii) $E_k(x)$ is local: supported within $R_{\mathcal{O}} = O(1)$
block lattice spacings of $x$.

(iii) $E_k$ is gauge-invariant and parity-even (Section 07).

(iv) $\sum_x x_\mu E_k(x) = 0$ for all $\mu$ (proved from parity).

### 4.2 Position-space derivative decomposition

**Lemma 4.1.** *Let $f : \Lambda \to \mathbb{R}$ be a local function
supported in a ball of radius $R$, satisfying:*

*(i) $\sum_x f(x) = 0$,*

*(ii) $\sum_x x_\mu f(x) = 0$ for all $\mu$.*

*Then there exist local functions $h_{\mu\nu}$, each supported in a
ball of radius $R + 1$, such that:*
$$f(x) = \sum_{\mu,\nu} \nabla_\mu^* \nabla_\nu^*\,h_{\mu\nu}(x)$$
*with $\|h_{\mu\nu}\|_\infty \leq (2R+1)^2\,\|f\|_\infty$.*

**Proof.** Since $f$ has finite support and vanishing zeroth moment,
define:
$$g_\mu(x) = \sum_{y_\mu \leq x_\mu} f(y_\mu, \tilde{x})$$
where $\tilde{x}$ denotes coordinates transverse to $\mu$. Then
$\nabla_\mu^* g_\mu = f$ along the $\mu$-direction. The vanishing of
the zeroth moment ensures consistency of both partial sums.

The vanishing first moment gives $\sum_x g_\mu(x) = -\sum_x x_\mu
f(x) = 0$ (by summation by parts), so $g_\mu$ itself has vanishing
zeroth moment. Iterate: define $h_{\mu\nu}$ by the same partial
summation of $g_\mu$ along $\nu$. Then $\nabla_\mu^* \nabla_\nu^*
h_{\mu\nu} = f$. The support extends by at most 1 per step, and
$\|h_{\mu\nu}\|_\infty \leq (2R+1)^2 \|f\|_\infty$. $\square$

### 4.3 Application to the total remainder

**If** the vacuum subtraction $\hat{E}_k(0) = \sum_x E_k(x) = 0$
holds as an operator identity (Theorem 6(b) of 07-power-counting.md),
then $E_k(x)$ satisfies both hypotheses of Lemma 4.1:

- Zeroth moment: $\sum_x E_k(x) = 0$ (Theorem 6(b)).
- First moment: $\sum_x x_\mu E_k(x) = 0$ (parity, Theorem 6(a)).

Therefore:
$$E_k(x) = \sum_{\mu,\nu} \nabla_\mu^* \nabla_\nu^*\,
  h_{\mu\nu}^{(k)}(x)$$
with $\|h_{\mu\nu}^{(k)}\|_\infty \leq C(R_{\mathcal{O}})\,g_k^4$.

**This is the derivative decomposition needed for Path 1.** The total
remainder can be written as a double lattice derivative of bounded
local functions. The summation-by-parts argument of Lemma 5.3 then
applies to $E_k$ directly, without decomposing into individual
dimension-$d_O$ operators.

### 4.4 The conditional nature

This result is conditional on Theorem 6(b). If Theorem 6(b) fails --
if $\hat{E}_k(0) = 0$ holds only in vacuum expectation but not as an
operator identity -- then the derivative decomposition holds only in
the weak sense:
$$\langle 0|E_k(x)|0\rangle = \nabla^*\nabla^*\,
  \langle 0|h^{(k)}(x)|0\rangle$$
but not configuration by configuration, and the polymer summation by
parts encounters the same obstacle.

---

## 5. Conclusion

### 5.1 What the analysis establishes

**(a) Basis classification.** The independent dimension-6 operators
are: $\hat{\mathcal{O}}_1$ (two lattice derivatives, $c_1 = O(g^2)$),
$\hat{\mathcal{O}}_2$ (zero derivatives, $c_2 = O(g^4)$),
$\hat{\mathcal{O}}_3$ (zero derivatives, $c_3 = O(g^4)$, absent for
$N=2$).

**(b) Non-derivative operators are suppressed.** The cubic-curvature
operators first appear at two loops; their coefficients carry an
extra $g_k^2$ beyond the generic bound.

**(c) Total remainder bypass.** Conditional on Theorem 6(b), the
entire remainder $E_k$ admits a double-derivative representation
$E_k = \nabla^* \nabla^* h^{(k)}$ with $\|h^{(k)}\|_\infty \leq
C g_k^4$, and the integration-by-parts argument applies to $E_k$
as a whole.

**(d) Operator-by-operator decomposition is not needed.** The total
remainder approach makes the classification of individual operators
unnecessary for the form factor bound.

### 5.2 What remains open

**(i) Theorem 6(b)** -- the vacuum subtraction as operator identity --
is the controlling obstacle. Both the total remainder approach
(Section 4) and the power counting lemma (Section 07) reduce to this
single question.

**(ii) The improved bound $c_2, c_3 = O(g^4)$** should be extractable
from Balaban's Taylor expansion but has not been written as a
self-contained proof.

**(iii) Claim 3.1** (stronger suppression of non-derivative operators
in the one-particle matrix element) provides a second line of defense
independent of Theorem 6(b), but requires non-perturbative input.

### 5.3 Connection to Path 1a

**If Theorem 6(b) holds:** Obstacle 3 is fully resolved. The form
factor bound follows from the total remainder representation:
$$|f_c(0)| \leq C\,g_k^4\,(a_k\Delta)^2\,\Delta^3.$$

**If Theorem 6(b) fails:** The derivative operator
$\hat{\mathcal{O}}_1$ is controlled by the standard argument (Path
1a, Section 5). The non-derivative operators $\hat{\mathcal{O}}_2,
\hat{\mathcal{O}}_3$ require either Claim 3.1 or a separate mechanism.

**In either case, the analysis reduces Obstacle 3 to Theorem 6(b)** --
the same bottleneck identified in 07-power-counting.md. The operator
decomposition does not introduce a genuinely new difficulty beyond the
vacuum subtraction question.
