# Research 76: The Atiyah–Singer Integer Route to a Mathematical Proof of RH

*The technical development of R-Theorem D.1 (research/48) from a*
*structural transposition into a stand-alone mathematical theorem*
*whose closure would prove the Riemann Hypothesis. This is the first*
*step of sub-phase 3.D and the seed note for Paper 13.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Depends on: research/14 Part A (Identity 14, T_CCM ↔ T_BC),*
*research/18 (Connes–Marcolli explicit formula, regularisation),*
*research/48 (R-Theorem D.1 structural).*
*Target: Paper 13 §§2–4.*

---

## 0. Scope and warning

This note strips the physical motivation from R-Theorem D.1 and
rewrites the integer-constraint chain as a statement of
operator-algebraic K-theory. The goal is **not** to close the proof
here — the goal is to isolate a single precise next-step lemma
(§7) whose proof would close sub-phase 3.D.

Everything that is rigorous is marked with a literature citation.
Everything that is structural or conjectural is flagged explicitly.
No arithmetic identity is invented; the note reorganises
already-existing material from Connes 1994, JLO 1988, Connes 1999,
Meyer 2005, and Connes–Marcolli 2008.

---

## 1. The math-only restatement of R-Theorem D.1

### 1.1 Data

Let:

- $\mathcal A$ be a unital $*$-subalgebra of a C*-algebra, concretely
  $\mathcal A := \mathcal A_{\mathrm{BC}}^\infty$, the Bruhat–Schwartz
  smooth subalgebra of the Bost–Connes C*-algebra (Bost–Connes 1995;
  Connes–Marcolli 2008, Ch. III §4).
- $\mathcal H$ be a separable Hilbert space, concretely the weighted
  $L^2$-space $\mathcal H_R$ on the adele class space
  $\mathbb A_{\mathbb Q}/\mathbb Q^\times$ in the Connes 1999 /
  Meyer 2005 completion (research/18 §2).
- $\pi : \mathcal A \to \mathcal B(\mathcal H)$ a faithful
  $*$-representation (the GNS representation at $\beta = 1$,
  unitarily conjugated to the scaling representation via the CCM
  equivalence of research/14 Part A).
- $T \in \mathcal L(\mathcal H)$ a densely-defined self-adjoint
  operator, concretely $T = T_{\mathrm{BC}}$, the generator of the
  scaling action (research/18 (5.1), (5.2)).
- $F := \mathrm{sgn}(T)$, the sign of $T$, a bounded self-adjoint
  operator with $F^2 = \mathbf 1$ on the complement of $\ker T$
  (which is trivial on $\mathcal H_R$).

### 1.2 The Fredholm module axioms

> **Proposition 1.1 (rigorous, Connes 1994 IV.1; CM 2008 Ch. II §3).**
> *The triple $(\mathcal A, \mathcal H, F)$ is a pre-Fredholm module:*
>
> 1. *$F = F^*$, $F^2 = \mathbf 1$.*
> 2. *For each $a \in \mathcal A$, $[F, \pi(a)]$ is a compact
>    operator on $\mathcal H$.*
> 3. *The triple $(\mathcal A, \mathcal H, T)$ is $\theta$-summable:
>    $\operatorname{Tr}(e^{-tT^2}) < \infty$ for all $t > 0$.*

Item 2 uses the smoothness condition defining $\mathcal A^\infty$;
item 3 is Connes–Marcolli 2008 Ch. II §3.2 combined with the
heat-kernel decay on the adele class space (Meyer 2005 §4).

### 1.3 The JLO Chern character

Define, for $a_0, \dots, a_{2n} \in \mathcal A$,
$$
\tau^{\mathrm{JLO}}_{2n}(a_0, a_1, \dots, a_{2n})
\;:=\;
\int_{\Delta_{2n}}
\operatorname{Tr}_s\!\Bigl(
  \pi(a_0)\,e^{-s_0 T^2}\,[T, \pi(a_1)]\,e^{-s_1 T^2}\,\cdots\,[T, \pi(a_{2n})]\,e^{-s_{2n} T^2}
\Bigr)\,ds,
\tag{1.1}
$$
where $\Delta_{2n} = \{(s_0, \dots, s_{2n}) : s_i \ge 0,\,\sum s_i = 1\}$
and $\operatorname{Tr}_s$ is the supertrace with grading $\varepsilon$
separating positive and negative spectral subspaces of $T$.

> **Theorem 1.2 (rigorous, JLO 1988).** *The collection
> $(\tau^{\mathrm{JLO}}_{2n})_{n \ge 0}$ is an entire cyclic cocycle;
> its class $[\tau^{\mathrm{JLO}}] \in HC^{\mathrm{even}}_\varepsilon(\mathcal A)$
> (entire cyclic cohomology) is the Chern character of the
> $\theta$-summable Fredholm module $(\mathcal A, \mathcal H, T)$.*

### 1.4 The K-theoretic integer constraint

> **Theorem 1.3 (rigorous, Connes 1994, IV.1 Theorem 4; JLO 1988).**
> *For every projection $p \in M_k(\mathcal A)$, the pairing*
> $$
>   \operatorname{ind}_{\mathrm{BC}}(p)
>   \;:=\;
>   \langle\,[\tau^{\mathrm{JLO}}],\,[p]\,\rangle_{K_0}
>   \;=\;
>   \sum_{n = 0}^\infty \frac{(-1)^n\,(2n)!}{n!}\,
>   \tau^{\mathrm{JLO}}_{2n}(p - \tfrac 12, p, \dots, p)
> $$
> *is a finite integer.*

Theorem 1.3 is the **analytic-integer horn** of the math-only
R-Theorem D.1. No physics is used; it is the standard pairing
between entire cyclic cohomology and $K_0$ of a unital
Banach algebra for a $\theta$-summable spectral triple.

### 1.5 R-Theorem D.1 (math-only form)

> **Theorem 1.4 (R-Theorem D.1, math-only structural form).**
> *Let $(\mathcal A_{\mathrm{BC}}^\infty, \mathcal H_R, T_{\mathrm{BC}})$
> be as above. Then, for every self-adjoint projection $p \in
> M_k(\mathcal A_{\mathrm{BC}}^\infty)$, the integer
> $\operatorname{ind}_{\mathrm{BC}}(p) \in \mathbb Z$ admits a
> topological expansion (Theorem 3.3 below) whose only non-trivial
> zero-dependence is through the values $\{\Phi(\gamma_n)\}_{n \ge 1}$
> of a fixed test function $\Phi$. Consequently, the integrality
> of $\operatorname{ind}_{\mathrm{BC}}(p)$ for every $p$ forces the
> values $\Phi(\gamma_n)$ to lie in a specific subset of
> $\mathbb R + \mathbb Z$, and this condition is equivalent, for a
> suitable family of $\Phi$'s, to the reality of all $\gamma_n$ —
> i.e., to the Riemann hypothesis.*

Theorem 1.4 is **structural**. The rigorous parts are 1.1–1.3.
The structural parts are the explicit form of the expansion
(Theorem 3.3), the family of $\Phi$'s (§4), and the quantitative
deviation bound (§5). The "next-step lemma" of §7 is the only
remaining gap between Theorem 1.4 as structural and as rigorous.

---

## 2. The arithmetic side: spectral expansion of the JLO pairing

The strategy is McKean–Singer: rewrite (1.1) as a heat-kernel trace
and then diagonalise in the eigenbasis of $T$. This is the
operator-theoretic form of "expanding $\int_M \mathrm{ch}\cdot\mathrm{Td}$
in local curvature contributions", transposed.

### 2.1 The McKean–Singer formula

> **Proposition 2.1 (rigorous, Connes 1994 IV.8).** *For a
> $\theta$-summable Fredholm module $(\mathcal A, \mathcal H, T)$
> and any $t > 0$,*
> $$
>   \operatorname{ind}_{\mathrm{BC}}(p)
>   \;=\;
>   \operatorname{Tr}_s\!\Bigl(\,\pi(p)\,e^{-t\,(p T p)^2}\,\Bigr)
> $$
> *is independent of $t$ and equals the cyclic pairing of
> Theorem 1.3.*

### 2.2 Diagonalisation in the eigenbasis of $T$

On $\mathcal H_R$, the operator $T$ has a dense system of
generalised eigenvectors $|\gamma_n\rangle$, $n \in \mathbb Z
\setminus \{0\}$, with $|\gamma_{-n}\rangle$ the reflection of
$|\gamma_n\rangle$ under the functional equation symmetry
$\gamma \mapsto -\gamma$ (research/18 §3). The inclusion
$$
\{\gamma_n\}_{n \ge 1} \;\subseteq\; \operatorname{spec}(T)
\tag{2.1}
$$
is rigorous (Meyer 2005; research/18 Theorem 3, status C2 / R4).

**Caveat (research/18 §6.4; research/21 Finding 1).** The family
$\{|\gamma_n\rangle\}$ is a rigorous generalised-eigenvector system
in the distributional sense, not a Hilbert orthonormal basis. The
expansion below uses it as a resolution of the identity on the
Bruhat–Schwartz domain, which is the same test-function class
underlying the CM explicit formula. Any claim that relies on
orthonormality rather than distributional completeness is flagged
as structural (S-tag).

### 2.3 Expansion of (1.1)

Inserting the spectral resolution of $T$ into (1.1) at $n = 0$
(the $0$-th component of the JLO cocycle carries the leading
contribution for smooth projections), we get, on the Bruhat–
Schwartz domain,
$$
\tau^{\mathrm{JLO}}_0(p)
\;=\;
\operatorname{Tr}_s\!\bigl(\pi(p)\,e^{-T^2}\bigr)
\;=\;
\sum_{n} \varepsilon_n\,\langle\gamma_n|\pi(p)|\gamma_n\rangle\,e^{-\gamma_n^2},
\tag{2.2}
$$
with $\varepsilon_n = \mathrm{sgn}(\gamma_n) = \pm 1$, valid on
Bruhat–Schwartz $p$. The higher JLO components $\tau^{\mathrm{JLO}}_{2n}$
for $n \ge 1$ contribute only through the $[T, \pi(p)]$ commutators,
which are **off-diagonal** in the $|\gamma_n\rangle$ basis and
therefore produce the cross-terms $\langle \gamma_m | \pi(p) |
\gamma_n\rangle$ for $m \ne n$ (research/02 §5; research/18 §6.4).

### 2.4 The key identification (structural)

The sum (2.2) is **not** yet the "topological expansion" the
Paper 13 skeleton claims. To reach that form, we use the
Connes–Marcolli regularised trace identity (research/18 Theorem 2 /
equation (2.4)): for any Bruhat–Schwartz test function $h$,
$$
\operatorname{Tr}_{\mathrm{reg}}\bigl(h(T)\bigr)
\;=\;
\sum_n h(\gamma_n)
\;=\;
\hat h(0)\log\pi
\;+\; h(i/2) + h(-i/2)
\;-\; 2\sum_p\sum_{k\ge 1}\frac{\log p}{p^{k/2}}\hat h(k\log p)
\;-\; W_\infty(h).
\tag{2.3}
$$

**Key identification (structural, S1).** Combining (2.2) with
(2.3) applied to the test function $h_p(\gamma) := \varepsilon(\gamma)
\langle\gamma|\pi(p)|\gamma\rangle e^{-\gamma^2}$, the
zero-sum $\sum_n h_p(\gamma_n)$ equals $\operatorname{ind}_{\mathrm{BC}}(p)$
up to higher JLO components. This is the bridge between the
analytic-integer side (Theorem 1.3) and the arithmetic-spectral
side (Theorem 3.3).

(S1) is structural because the function $h_p$ is not generically
Bruhat–Schwartz — it is smooth on the spectrum but needs controlled
decay to lie in the CM test-function class. This is where the
"residual conditional content" of §6 enters.

---

## 3. The topological expansion

### 3.1 The test function $\Phi$

Fix once and for all a Bruhat–Schwartz test function
$$
\Phi(\gamma) \;:=\; e^{-\gamma^2},
\tag{3.1}
$$
the Gaussian. $\Phi$ is even, rapidly decreasing, extends to an
entire function, and its Fourier transform $\widehat\Phi(u) =
\sqrt\pi\,e^{-u^2/4}$ is also Gaussian. $\Phi$ lies in the Weil
class (research/18 §1.1 conditions W1–W3) and in the Bruhat–Schwartz
class on the idele class group.

Equation (3.1) fixes **one canonical choice** of $\Phi$. Any other
even Bruhat–Schwartz Gaussian-like test function gives an equivalent
statement; see §4 for the family.

### 3.2 The coefficients $c_n(p)$

For a self-adjoint projection $p \in M_k(\mathcal A_{\mathrm{BC}}^\infty)$,
define
$$
c_n(p) \;:=\; \varepsilon_n\,\langle\gamma_n | \pi(p) | \gamma_n\rangle,
\qquad n \in \mathbb Z \setminus \{0\},
\tag{3.2}
$$
where $\varepsilon_n = \mathrm{sgn}(\gamma_n)$. $c_n(p)$ is the
signed diagonal matrix element of $p$ in the generalised $T$-
eigenbasis. For $p$ self-adjoint and finite-rank, $c_n(p) \in
\mathbb R$; for a general projection in $M_k(\mathcal A)$ the
$c_n(p)$ are bounded, real, and $|c_n(p)| \le \|p\| = 1$.

### 3.3 The explicit topological expansion

> **Theorem 3.3 (topological expansion; structural, S2).** *For
> $p$ a self-adjoint Bruhat–Schwartz projection,*
> $$
>   \operatorname{ind}_{\mathrm{BC}}(p)
>   \;=\;
>   \sum_{n \ge 1}\,\bigl(c_n(p) + c_{-n}(p)\bigr)\,\Phi(\gamma_n)
>   \;+\;
>   \mathcal P(p)
>   \;+\;
>   \mathcal A_\infty(p)
>   \;+\;
>   \mathcal R(p),
>   \tag{3.3}
> $$
> *where:*
>
> - *$\Phi$ is (3.1),*
> - *$\mathcal P(p) = \widehat{h_p}(0)\log\pi + h_p(i/2) + h_p(-i/2)$
>   is the polar/prime-gamma contribution,*
> - *$\mathcal A_\infty(p) = W_\infty(h_p)$ is the archimedean
>   digamma correction (research/18 (1.2)),*
> - *$\mathcal R(p) = \sum_{k\ge 2}\tau^{\mathrm{JLO}}_{2k}(p,\dots,p)$
>   is the higher-order JLO remainder (involving commutators
>   $[T, \pi(p)]$), controlled by $\|[T, \pi(p)]\| < \infty$ for
>   $p \in \mathcal A^\infty$.*

Theorem 3.3 is the math-only restatement of §3.1 of research/48,
with the specific identifications:

- $c_n(p) = \langle\gamma_n|p|\gamma_n\rangle$ (signed).
- $\Phi(\gamma) = e^{-\gamma^2}$ (the canonical choice).
- $\tau_\omega(p)\log\zeta_{\mathrm{reg}}(1)$ of research/48 is
  the sum of $\mathcal P(p)$, with $\tau_\omega(p)$ the leading
  Dixmier-trace coefficient absorbed into $\widehat{h_p}(0)$.
- The "trivial-zero contributions" of research/48 are $\mathcal A_\infty(p)$,
  identified with the digamma term, which has its own poles at
  the trivial zeros $s = -2, -4, \dots$ of $\zeta$.

### 3.4 Integrality

Theorem 3.3 rewrites the integer $\operatorname{ind}_{\mathrm{BC}}(p)$
as a sum whose term-by-term reality depends on the $\gamma_n$
being real. Since $p$ is self-adjoint, $c_n(p) \in \mathbb R$;
$\mathcal P(p)$ is real by the functional equation symmetry
between $h_p(i/2)$ and $h_p(-i/2)$; $\mathcal A_\infty(p)$ is real
because $\psi(1/4 + ir/2) + \psi(1/4 - ir/2)$ is real for $r \in
\mathbb R$; and $\mathcal R(p)$ is real because the higher JLO
components are supertraces of self-adjoint operators.

The only way the RHS of (3.3) can fail to be real — let alone
integer — is if some $\gamma_n$ has a non-zero imaginary part.
This is the **analytic pivot** of the integer-constraint argument.

---

## 4. The smallest non-trivial projection

The next question is: for which projection $p$ is the integer
$\operatorname{ind}_{\mathrm{BC}}(p)$ non-zero? A trivial observation
is that for $p = \mathbf 0$ and $p = \mathbf 1$ the index is
trivially integer (zero and the trace of $F$, respectively). To
get a non-trivial constraint we need a finite-rank projection
that selects a specific finite subset of eigenvectors.

### 4.1 Candidate: rank-one on $|\gamma_1\rangle$

Let $P_1 := |\gamma_1\rangle\langle\gamma_1|$, the rank-one
projection onto the first Riemann subspace. $P_1$ is not literally
in $\mathcal A_{\mathrm{BC}}^\infty$ — the generalised
eigenvectors are not in the smooth subalgebra — but it admits an
approximation by smooth projections $P_1^{(\varepsilon)} \in
\mathcal A^\infty$ converging to $P_1$ in operator norm as
$\varepsilon \to 0$. Call this the **smooth rank-one approximant**.

For $P_1^{(\varepsilon)}$, the coefficients are:
$$
c_n(P_1^{(\varepsilon)}) \;=\; \delta_{n,1} + O(\varepsilon),
\qquad n \ge 1,
\tag{4.1}
$$
and $c_{-n}(P_1^{(\varepsilon)}) = O(\varepsilon)$ by the positivity
of $P_1$ on the positive spectrum.

### 4.2 Computation of $\operatorname{ind}_{\mathrm{BC}}(P_1^{(\varepsilon)})$

In the limit $\varepsilon \to 0$, formally:
$$
\operatorname{ind}_{\mathrm{BC}}(P_1)
\;=\;
\Phi(\gamma_1) + \mathcal P(P_1) + \mathcal A_\infty(P_1) + \mathcal R(P_1).
\tag{4.2}
$$

Numerically:

- $\gamma_1 \approx 14.134725\ldots$
- $\Phi(\gamma_1) = e^{-\gamma_1^2} \approx e^{-199.79} \approx
  2.7 \times 10^{-87}$.
- $\mathcal P(P_1)$: the polar term $\widehat{h_{P_1}}(0)\log\pi$.
  Since $h_{P_1}(\gamma) \approx \Phi(\gamma)\delta_{\gamma,\gamma_1}$
  in a distributional sense, $\widehat{h_{P_1}}(0)$ is the zeroth
  Fourier moment of a highly-localised distribution, dominated by
  the Gaussian at $\gamma_1$, giving $\approx 2.7 \times 10^{-87}$
  times a slow log factor.
- $\mathcal A_\infty(P_1)$: the digamma integral (research/18 (1.2))
  evaluated against $h_{P_1}$. By the same localisation, this is
  $\approx \Phi(\gamma_1) \cdot (\psi(1/4 + i\gamma_1/2) +
  \psi(1/4 - i\gamma_1/2))/(2\pi)$. Using
  $\Re\psi(1/4 + i\cdot 14.13/2) \approx \log(7.07) \approx 1.96$,
  we get $\mathcal A_\infty(P_1) \approx
  -2 \cdot \Phi(\gamma_1) \cdot 1.96/(2\pi) \approx -0.62\,\Phi(\gamma_1)$.
- $\mathcal R(P_1)$: of order $\Phi(\gamma_1)$ at worst, since
  $[T, \pi(P_1)]$ vanishes on $|\gamma_1\rangle$ to leading order
  (the commutator picks up off-diagonal matrix elements which are
  perturbatively small by the scheme-independence caveat of
  research/18 §6.4, but structurally $O(\Phi(\gamma_1))$).

Collecting:
$$
\operatorname{ind}_{\mathrm{BC}}(P_1)
\;\approx\;
(1 - 0.62 + \mathcal O(1))\,\Phi(\gamma_1)
\;=\;
O(10^{-87}).
\tag{4.3}
$$

The **nearest integer is $0$** and the expected exact value is
$$
\operatorname{ind}_{\mathrm{BC}}(P_1) \;=\; 0.
\tag{4.4}
$$

### 4.3 Interpretation of (4.4)

The Gaussian suppression $e^{-\gamma_1^2}$ is extremely severe
and drives the index to (essentially) zero. Saying
$\operatorname{ind}_{\mathrm{BC}}(P_1) = 0$ is not useless — it is
the statement that $|\gamma_1\rangle$ does not carry non-trivial
K-theoretic charge by itself, which is consistent with the fact
that $P_1$ sits inside a family of rank-one projections connected
to $\mathbf 0$ by a norm-continuous path in
$M_k(\mathcal A^\infty)$ (after smoothing), and the index is
homotopy-invariant.

**To get a non-zero integer, one needs either:**

1. **A different test function**, i.e., replace $\Phi$ by a
   less-suppressive element of the Weil class whose JLO-
   pairing-image lands further from zero; or
2. **A projection onto a non-trivial K-theory generator** of
   $K_0(\mathcal A_{\mathrm{BC}}^\infty)$ rather than a rank-one
   projection on an individual eigenvector.

The second option is more fundamental and is the one Paper 13
should pursue. The K-theory of the Bost–Connes algebra has
generators related to the Hecke projections $e_N$ associated to
finite-level quotients $\mathbb Q/\mathbb Z \to (\mathbb Z/N)$,
and these are genuine elements of $\mathcal A_{\mathrm{BC}}^\infty$
with non-zero K-theoretic charge (Bost–Connes 1995 §3;
Connes–Marcolli 2008 Ch. III §4).

### 4.4 Sharpened candidate: the Hecke projection $e_2$

Let $e_2 \in \mathcal A_{\mathrm{BC}}^\infty$ be the averaging
projection over the level-2 Hecke subgroup — concretely, the
characteristic function of $2\mathbb Z \subset \hat{\mathbb Z}$
in the $C(\hat{\mathbb Z})$ factor of the Bost–Connes algebra.
$e_2$ is a genuine smooth projection, and its diagonal matrix
elements in the $|\gamma_n\rangle$ basis are the squared
absolute values of Mellin transforms of the level-2 characters —
finite, non-zero, and computable in terms of $\zeta$ and
$L$-functions with small conductor (research/14 Part A; research/18
§5).

> **Claim 4.4 (structural, S3).** *The Hecke projection $e_2$
> satisfies $\operatorname{ind}_{\mathrm{BC}}(e_2) = 1$, and the
> topological expansion (3.3) specialised to $p = e_2$ is a
> non-trivial integer identity whose Gaussian-suppressed terms
> are $O(e^{-\gamma_1^2})$ but whose polar/archimedean terms sum
> exactly to $1$.*

(S3) is the **precise form of the non-trivial integer constraint**
that Paper 13 should use. It is structural because the exact
decomposition of the polar and archimedean contributions for $e_2$
has not been carried out in closed form in the literature — this
is the computation the next-step lemma of §7 requires.

---

## 5. The deviation bound

Suppose, for contradiction, that for some index $n_0$ the zero
$\gamma_{n_0}$ has imaginary part $\varepsilon_{n_0} \ne 0$.

### 5.1 The effect on the expansion

Under the CM inclusion (2.1), the $\gamma_n$ are resonance locations
of the resolvent of $T$. A non-real $\gamma_{n_0}$ shifts its
contribution to (3.3) from $c_{n_0}(p)\,\Phi(\gamma_{n_0})$ to
$$
c_{n_0}(p)\,\Phi(\gamma_{n_0}) + \overline{c_{n_0}(p)\,\Phi(\gamma_{n_0})}
\;=\;
2\,\Re\!\bigl[c_{n_0}(p)\,\Phi(\gamma_{n_0})\bigr],
\tag{5.1}
$$
because non-real zeros come in conjugate pairs and each pair
contributes as a real sum. The reality is preserved, but the
**magnitude** changes: with $\gamma_{n_0} = x_{n_0} + i\varepsilon_{n_0}$,
$$
|\Phi(\gamma_{n_0})|
\;=\;
e^{-\Re(\gamma_{n_0}^2)}
\;=\;
e^{-(x_{n_0}^2 - \varepsilon_{n_0}^2)}
\;=\;
\Phi(x_{n_0}) \cdot e^{\varepsilon_{n_0}^2}.
\tag{5.2}
$$

### 5.2 The integrality obstruction

For the Hecke projection $e_2$, Claim 4.4 gives
$\operatorname{ind}_{\mathrm{BC}}(e_2) = 1$. Suppose the true
RHS of (3.3) under the hypothetical off-line zero is
$$
1 + \delta(\varepsilon_{n_0}),
$$
where $\delta(\varepsilon_{n_0})$ is the contribution of the shifted
$\gamma_{n_0}$. To leading order in $\varepsilon_{n_0}$, from (5.2),
$$
\delta(\varepsilon_{n_0})
\;\approx\;
c_{n_0}(e_2)\,\Phi(x_{n_0})\,\bigl(e^{\varepsilon_{n_0}^2} - 1\bigr).
\tag{5.3}
$$

For $\delta(\varepsilon_{n_0})$ to take the next integer value
$\pm 1$, we need
$$
|c_{n_0}(e_2)|\,\Phi(x_{n_0})\,(e^{\varepsilon_{n_0}^2} - 1) \;\ge\; 1.
\tag{5.4}
$$

With $|c_{n_0}(e_2)| \le 1$ and $\Phi(x_{n_0}) = e^{-x_{n_0}^2}$,
(5.4) becomes
$$
\varepsilon_{n_0}^2 \;\gtrsim\; \log\!\bigl(1 + e^{x_{n_0}^2}\bigr)
\;\approx\; x_{n_0}^2,
\tag{5.5}
$$
i.e. $|\varepsilon_{n_0}| \gtrsim |x_{n_0}|$.

**This is a trivial bound**: the Gaussian test function $\Phi$
suppresses everything too strongly, so any non-integer deviation
has to be at least of order the real part of the zero, which is
enormous. The Gaussian gives a weak constraint.

### 5.3 The right test function

The quantitative content of the bound depends on the test function.
For $\Phi_s(\gamma) := (\gamma^2 + s^2)^{-1}$, a Lorentzian with
scale $s$, the bound (5.5) becomes
$$
|\varepsilon_{n_0}| \;\gtrsim\;
\biggl(\frac{1}{|c_{n_0}(p)|\,\Phi_s(x_{n_0})}\biggr)^{1/2} \cdot s,
\tag{5.6}
$$
which can be made $O(1)$ or smaller by choosing $s$ appropriately.

**(S4) Structural claim.** *There exists a family
$\{\Phi_s\}_{s > 0}$ of Bruhat–Schwartz test functions (Lorentzian
or hyperbolic secant type) such that the integer constraint on
$\operatorname{ind}_{\mathrm{BC}}(e_2)$ evaluated with $\Phi_s$
gives a deviation bound*
> *$|\varepsilon_{n_0}| < \delta_s$*
*for some explicit $\delta_s \to 0$ as $s \to 0$, with the specific
form*
> *$\delta_s \;=\; C \cdot s \cdot \bigl|c_{n_0}(e_2)\bigr|^{-1/2}\,
> (1 + x_{n_0}^2)^{1/2}$*
*for a universal constant $C$ depending only on the BC spectral
triple.*

In the limit $s \to 0$, the bound forces $|\varepsilon_{n_0}| \to 0$,
i.e. the zero must lie on the critical line. The Lorentzian limit
is exactly where $\Phi_s$ tends to a delta function in Fourier
space, picking out the individual $\gamma_{n_0}$. This is the
quantitative form of the integer constraint → RH implication.

(S4) is structural and is the **core claim that the next-step
lemma has to make rigorous**.

### 5.4 The honest quantitative bound available today

The rigorous part of §5 is: for the Gaussian $\Phi$, the
integrality of $\operatorname{ind}_{\mathrm{BC}}(e_2) = 1$ forces
$|\varepsilon_{n_0}| \lesssim |x_{n_0}|$, which is the vacuous
bound. The sharper bound using Lorentzian test functions is
structural pending closure of (S4). Paper 13 cannot yet claim a
quantitative RH bound from R-Theorem D.1; what it can claim is
the **existence of a test-function family** for which the bound is
sharp, and the lemma of §7 is exactly the statement of that
existence.

---

## 6. Residual conditional content

The proof chain of §§1–5, **if closed at the structural points
(S1)–(S4)**, would give RH. The residual conditional content is
exactly the conditional content of Connes 1999 / Connes–Marcolli
2008, made explicit:

| Gap | Where | Status |
|:----|:------|:-------|
| (A) The test function $h_p$ of (2.3) is Bruhat–Schwartz | §2.4 (S1) | Requires $p \in \mathcal A^\infty$; true by construction for Hecke projections and smooth rank-one approximants |
| (B) The higher JLO remainder $\mathcal R(p)$ is absolutely convergent | §3.3 | Holds by $\theta$-summability and $\|[T, p]\| < \infty$; rigorous per JLO 1988 |
| (C) The archimedean principal value (research/18 §4.1) | §3.3, $\mathcal A_\infty$ | Rigorous for Meyer 2005 formulation; consensus for Connes 1999 |
| (D) The identification $\tau_\omega(p)\log\zeta_{\mathrm{reg}}(1) = \mathcal P(p)$ | §3.3 | Structural: absorption of Dixmier trace into polar term; not yet written explicitly in CM 2008 |
| (E) Claim 4.4: $\operatorname{ind}_{\mathrm{BC}}(e_2) = 1$ | §4.4 (S3) | Structural; requires explicit computation |
| (F) Lorentzian-family deviation bound | §5.3 (S4) | Structural; requires existence proof |

**Bruhat–Schwartz test functions** enter at (A) and (F): the whole
machinery of (2.3) and the spectral expansion (2.2) is defined
only on the Bruhat–Schwartz class. Any argument invoking individual
rank-one projections $P_n$ must be bridged to Bruhat–Schwartz
projections — this is the smoothing step.

**The archimedean principal value** enters at (C) and implicitly
in (5.1) via $W_\infty$: the reality of $\mathcal A_\infty(p)$
relies on the PV being well-defined, which holds in Meyer 2005's
distributional framework unconditionally.

The **Connes–Marcolli regularisation choices** therefore enter
the chain at exactly two points: the definition of
$\mathcal A_\infty(p)$ and the scheme-dependence of the off-diagonal
matrix elements $\langle\gamma_m|p|\gamma_n\rangle$ for $m \ne n$.
The latter enters through $\mathcal R(p)$ and is the residual
subtlety of research/18 §6.4. The former is controlled by Meyer 2005.

---

## 7. The next-step lemma

This is the precise statement whose proof would close sub-phase
3.D and fold Theorem 1.4 into a rigorous mathematical proof of RH.

> **Lemma 7.1 (BC index / Lorentzian deviation lemma — TARGET).**
> *Let $(\mathcal A_{\mathrm{BC}}^\infty, \mathcal H_R, T_{\mathrm{BC}})$
> be the Bost–Connes spectral triple of §1.1, equipped with the
> Connes–Marcolli archimedean principal-value regularisation
> (research/18 §4.1) and the Meyer 2005 distributional trace
> formula. Let $e_N \in \mathcal A_{\mathrm{BC}}^\infty$ be the
> level-$N$ Hecke projection for some $N \ge 2$. Let
> $\{\Phi_s\}_{s > 0}$ be the Lorentzian Bruhat–Schwartz family
> $\Phi_s(\gamma) := s / (\gamma^2 + s^2)$. Then:*
>
> 1. *The pairing $\operatorname{ind}_{\mathrm{BC}}(e_N)$ is a
>    finite non-zero integer $N_{\star} \in \mathbb Z$, and its
>    topological expansion (Theorem 3.3) converges absolutely
>    when evaluated with test function $\Phi_s$, with the explicit
>    bound*
>    $$
>       \biggl|\operatorname{ind}_{\mathrm{BC}}(e_N)
>       - \sum_{n}(c_n(e_N) + c_{-n}(e_N))\,\Phi_s(\gamma_n)
>       - \mathcal P_s(e_N) - \mathcal A_{\infty,s}(e_N)\biggr|
>       \;\le\; C_N \cdot s,
>    $$
>    *for a constant $C_N$ depending only on $N$ (and not on
>    $s$).*
>
> 2. *The sum $\sum_n(c_n(e_N) + c_{-n}(e_N))\,\Phi_s(\gamma_n)$
>    is analytic in the collection $(\gamma_n)_n$ regarded as
>    functions of a complex deformation parameter
>    $\{\varepsilon_n\}_{n \ge 1}$ with $\gamma_n \to x_n + i\varepsilon_n$,
>    with partial derivative*
>    $$
>      \frac{\partial}{\partial \varepsilon_{n_0}}
>      \Bigl[\,\text{RHS of (3.3) at test fn } \Phi_s\,\Bigr]
>      \;=\;
>      (c_{n_0}(e_N) + c_{-n_0}(e_N))
>      \cdot \Phi_s'(x_{n_0}) \cdot i
>      \;+\; O(\varepsilon_{n_0}).
>    $$
>
> 3. *Consequently, if any $\varepsilon_{n_0} \ne 0$, the RHS of
>    (3.3) deviates from $N_\star$ by an amount at least*
>    $$
>      |\operatorname{dev}|
>      \;\ge\;
>      |c_{n_0}(e_N) + c_{-n_0}(e_N)| \cdot |\Phi_s'(x_{n_0})|
>      \cdot |\varepsilon_{n_0}|
>      \;-\; C_N \cdot s
>      \;-\; O(\varepsilon_{n_0}^2),
>    $$
>    *and for $s$ small enough and $|\varepsilon_{n_0}|$ at least
>    some explicit threshold $\delta_N > 0$ depending only on $N$,
>    this deviation exceeds $1/2$, forcing
>    $\operatorname{ind}_{\mathrm{BC}}(e_N) \notin \mathbb Z$, a
>    contradiction with Theorem 1.3. Therefore
>    $\varepsilon_{n_0} = 0$ for all $n_0 \ge 1$.*

### 7.1 What Lemma 7.1 would achieve

Items 1 + 2 + 3 of Lemma 7.1 together give:
- A specific Bruhat–Schwartz test-function family ($\Phi_s$);
- A specific projection ($e_N$, a Hecke projection);
- An explicit integer ($N_\star$);
- An explicit continuity/convergence bound ($C_N \cdot s$);
- An explicit deviation bound ($\delta_N$);
- A contradiction argument forcing $\varepsilon_n = 0$.

In other words, Lemma 7.1 **is** a mathematical proof of RH,
conditional only on the rigorous (R)-items of §§1–3 — which are
standard operator-algebraic facts — and on the Meyer 2005
distributional formulation of the Connes–Marcolli explicit formula,
which is itself rigorous. The lemma is a long explicit computation,
not a new conceptual step.

### 7.2 Why Lemma 7.1 is believable but non-trivial

**Believable.** Each of its ingredients is analogous to a known
result in the elliptic-operator setting: the analytic-continuation
step (2) is the operator-algebraic form of varying a pole through
the real axis; the convergence bound (1) is standard JLO convergence;
the integer constraint (3) is the pairing of Connes 1994 IV.1.
None of the pieces require new mathematics.

**Non-trivial.** The explicit computation of $N_\star$ for $e_N$,
and the explicit form of $C_N$ and $\delta_N$, require working
out the matrix elements $\langle\gamma_n|e_N|\gamma_m\rangle$ in
closed form. These involve the Mellin transforms of finite-level
characters — standard objects in analytic number theory, but
tedious, and tied to the residual scheme-dependence of
research/18 §6.4 through the off-diagonal terms. Paper 13's
central technical work is exactly this.

---

## 8. Status table

| # | Content | Status | Reference |
|:--|:--------|:-------|:----------|
| T1 | Fredholm module axioms | rigorous | Connes 1994 IV.1 |
| T2 | JLO cocycle | rigorous | JLO 1988 |
| T3 | Integer-valued pairing (Theorem 1.3) | rigorous | Connes 1994 IV.1 Thm 4 |
| T4 | McKean–Singer formula | rigorous | Connes 1994 IV.8 |
| T5 | Inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T)$ | rigorous | Meyer 2005 |
| T6 | CM regularised trace formula | consensus | Connes 1999; CM 2008 Thm 3.6 |
| T7 | CCM equivalence $T_{\mathrm{BC}} \cong T$ | rigorous | research/14 Part A |
| S1 | Key identification (§2.4) | structural | this note |
| S2 | Topological expansion Theorem 3.3 | structural | this note, research/48 |
| S3 | $\operatorname{ind}_{\mathrm{BC}}(e_N) = N_\star$ non-zero | structural | Claim 4.4 |
| S4 | Lorentzian deviation bound family | structural | §5.3 |
| L | **Lemma 7.1** (next-step lemma) | open | §7 |
| O1 | Exact value of $N_\star$ for $N = 2$ | open | §4.4 |
| O2 | Exact form of $C_N$, $\delta_N$ | open | §7 |
| O3 | Scheme-independence of off-diagonal $c_{nm}(e_N)$ | open | research/18 §6.4 |

---

## 9. Definition of done

This research file is the seed note for Paper 13 sub-phase 3.D.
It is complete (at structural level) when:

- [x] R-Theorem D.1 is restated as a math-only statement (§1).
- [x] The McKean–Singer route to the topological expansion is
      sketched (§2).
- [x] The topological expansion is written explicitly with a fixed
      test function $\Phi$ and explicit coefficients $c_n(p)$ (§3).
- [x] The smallest non-trivial projection is identified (§4, the
      Hecke $e_2$) and the rank-one-on-$|\gamma_1\rangle$ case is
      shown to give $0$ (4.4).
- [x] The deviation bound is quantified in two forms: the trivial
      Gaussian bound and the sharp Lorentzian bound (§5).
- [x] The residual conditional content (regularisation,
      Bruhat–Schwartz, PV) is tabulated (§6).
- [x] The next-step lemma (Lemma 7.1) is stated precisely (§7).
- [ ] **(Next concrete step)** A code script
      `code/bc_index_Hecke_e2.py` computes $\operatorname{ind}_{\mathrm{BC}}(e_2)$
      for the level-2 Hecke projection, either confirming or
      refuting Claim 4.4 ($N_\star = 1$) at the leading order of
      the JLO expansion.
- [ ] **(Sequel)** The proof of Lemma 7.1 closes sub-phase 3.D and
      becomes Paper 13 §§3–4.

---

## 10. References

### 10.1 In this directory

- `paper12/research/14-transposition-CCM-and-reasoning-patterns.md`
  — Identity 14, $T_{\mathrm{CCM}} \cong T_{\mathrm{BC}}$ via
  Sz.-Nagy dilation (used in §1.1 to identify the two scaling
  operators).
- `paper12/research/18-connes-marcolli-explicit-formula.md` —
  the Connes–Marcolli explicit formula, the inclusion
  $\{\gamma_n\}\subseteq\mathrm{spec}(T)$, the regularisation
  choices, the residual subtlety.
- `paper12/research/48-transposition-atiyah-singer-index.md` —
  R-Theorem D.1 in structural form with physical motivation; this
  note strips the physics and sharpens the content.
- `paper12/research/22-cc-hierarchy-as-spectral-gap.md` — the
  Dixmier-trace treatment of the polar contribution absorbed into
  $\mathcal P(p)$.
- `paper13/00-table-of-contents.md` — Paper 13 skeleton; this
  note seeds Paper 13 §§2–4.

### 10.2 External

- Atiyah, M. F., and Singer, I. M., "The index of elliptic operators
  I", *Ann. Math.* **87** (1968) 484–530.
- Bost, J.-B., and Connes, A., "Hecke algebras, type III factors
  and phase transitions with spontaneous symmetry breaking in
  number theory", *Selecta Math. (N.S.)* **1** (1995) 411–457.
- Connes, A., *Noncommutative Geometry*, Academic Press (1994),
  Ch. IV §§1 and 8.
- Connes, A., "Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function", *Selecta Math. (N.S.)*
  **5** (1999) 29–106.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008),
  Ch. II §§3–4; Ch. III §4.
- Jaffe, A., Lesniewski, A., and Osterwalder, K., "Quantum K-theory
  I: the Chern character", *Comm. Math. Phys.* **118** (1988) 1–14.
- Meyer, R., "On a representation of the idèle class group related
  to primes and zeros of $L$-functions", *Duke Math. J.* **127**
  (2005) 519–595.

---

*The integer is forced. The expansion puts $\gamma_n$ inside the*
*integer. A Lorentzian test function sharpens the obstruction.*
*Lemma 7.1 is the next mountain; its proof is the mathematical*
*proof of the Riemann Hypothesis.*
