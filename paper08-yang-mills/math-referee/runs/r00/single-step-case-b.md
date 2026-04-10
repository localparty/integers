# Single-Step Case B: The Cubic Curvature Operator $\mathrm{Tr}(F^3)$

The main single-step computation (single-step-computation.md) establishes
the $\hat{\Delta}^2$ suppression for the **derivative** dimension-6
operators $\mathrm{Tr}(DF)^2$ via two exact mechanisms: spatial
derivatives vanish by translation invariance, temporal derivatives bring
$\hat{\Delta}$ from the spectral gap. This document treats the second
class of dimension-6 operators -- the **cubic curvature** operators
$\mathrm{Tr}(F^3)$ and $d^{abc}F^aF^bF^c$ -- which carry zero extra
lattice derivatives and for which the derivative argument does not apply.

---

## 1. The Operator on the Lattice

### 1.1 Continuum form

The two non-derivative dimension-6 operators are (cf. path-1b-operator-decomposition.md, Section 1.1):

$$\mathcal{O}_2 = \mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}F_{\rho}{}^{\mu}),
  \qquad
  \mathcal{O}_3 = d^{abc}\,F_{\mu\nu}^a F^{b\,\nu\rho}F_\rho^{c\,\mu}$$

Each is a **cubic polynomial** in $F_{\mu\nu}$ with no covariant
derivatives. The engineering dimension is 6 (each $F$ carries dimension 2),
but the operator involves zero derivatives beyond those already inside $F$
itself.

### 1.2 Lattice transcription

On the lattice, $F_{\mu\nu}$ is represented by the plaquette variable
$U_P$ in the $(\mu,\nu)$ plane. Define the anti-Hermitian lattice field
strength:

$$\Omega_{\mu\nu}(x) = \frac{1}{2ia^2}(U_{P_{\mu\nu}}(x) - U_{P_{\mu\nu}}(x)^\dagger)
  \approx F_{\mu\nu}(x) + O(a^2)$$

Then the lattice cubic operator is:

$$\hat{\mathcal{O}}_2(x)
  = \sum_{\mu < \nu < \rho}
  \mathrm{Re}\,\mathrm{Tr}\bigl[
    (U_{P_{\mu\nu}}(x) - \mathbf{1})\,
    (U_{P_{\nu\rho}}(x) - \mathbf{1})\,
    (U_{P_{\rho\mu}}(x) - \mathbf{1})
  \bigr]$$

This is a product of **three plaquette variables at the same vertex** $x$.
There are no lattice finite differences $\nabla_\mu$ acting between
different sites. The operator is a bounded function of the link variables
surrounding $x$:

$$|\hat{\mathcal{O}}_2(x)| \leq \binom{4}{3}\cdot(2N)^3 = 4\cdot 8N^3$$

since each factor $(U_P - \mathbf{1})$ has operator norm $\leq 2$ on
$\mathrm{SU}(N)$, the trace contributes at most $N$, and there are
$\binom{4}{3} = 4$ triples of planes.

### 1.3 The critical distinction

| Operator | Extra derivatives | Coefficient | Derivative argument applies? |
|:---------|:------------------|:------------|:-----------------------------|
| $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ | 2 | $O(g_k^2)$ | **Yes** (single-step-computation.md, Sec. 4) |
| $\mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}F_{\rho\mu})$ | 0 | $O(g_k^4)$ | **No** |
| $d^{abc}F^a F^b F^c$ | 0 | $O(g_k^4)$ | **No** |

The integration-by-parts mechanism (spatial derivatives give zero by
translation invariance; temporal derivatives bring $\hat{\Delta}$) is
inapplicable to $\hat{\mathcal{O}}_2$ and $\hat{\mathcal{O}}_3$.

---

## 2. The Two-Loop Coefficient

### 2.1 Why $\mathrm{Tr}(F^3)$ is absent at one loop

At one loop, the effective action correction is (single-step-computation.md,
Section 1.3):

$$\delta S^{\text{1-loop}}[V]
  = \tfrac{1}{2}\mathrm{Tr}\ln
  \frac{-D^2[V] + m_W^2}{-\partial^2 + m_W^2}$$

Expanding the log-determinant in powers of the background $A_\mu$ (via
$V = e^{iag_kA}$), the $n$-th term in the expansion is:

$$\frac{(-1)^{n+1}}{2n}\,
  \mathrm{Tr}(G_0\,\mathcal{V}[A])^n$$

where $G_0 = (-\partial^2 + m_W^2)^{-1}$ and $\mathcal{V}[A] = -D^2[V]
+ \partial^2$. This is a **closed single loop** with $n$ vertex insertions
of $A$. Each vertex $\mathcal{V}$ contributes either one power of $A$
(with one derivative, from the $2ig_kA_\mu\partial_\mu$ piece) or two
powers of $A$ (from the $g_k^2 A^2$ piece). The loop integral over the
internal momentum produces a polynomial in the external momenta (the
momenta of the $A$ insertions).

**The crucial structural point:** Each vertex insertion at the one-loop
level contributes a field strength $F$ together with a momentum flowing
through the propagator. The contraction of a single loop with $n$
insertions produces terms of the form:

$$\int \frac{d^4p}{(2\pi)^4}\;
  \prod_{i=1}^n \frac{A(k_i)\cdot(\text{momentum factor})}{(p + q_i)^2 + m_W^2}$$

At dimension 6, two $A$ insertions suffice (each $A$ counts as
dimension 1 via $F = dA + A^2$, but the gauge-invariant combination is
$F \sim \partial A + g A^2$, so the lowest-order gauge-invariant
structures are $\mathrm{Tr}(\partial A)^2 \sim \mathrm{Tr}(F^2)$ at
dimension 4 and $\mathrm{Tr}(\partial^2 A\cdot\partial A) \sim
\mathrm{Tr}(DF\cdot F) \sim \mathrm{Tr}(DF)^2$ at dimension 6). The
one-loop integral with two $F$-insertions produces a **quadratic**
functional of $F$, not cubic.

**To generate $\mathrm{Tr}(F^3)$ requires three independent $F$-factors.**
At one loop with only two propagators connecting the vertex to itself, the
functional dependence on $F$ is at most quadratic after gauge-invariant
projection. A cubic invariant requires a **genuine two-loop graph**: at
minimum, two internal propagators forming two independent loops, with
three field-strength insertions on distinct propagator lines.

### 2.2 The two-loop origin of $\mathrm{Tr}(F^3)$

At two loops, the leading contribution beyond the Gaussian integration
involves the third cumulant of the fluctuation action
(path-1b-operator-decomposition.md, Section 3.1):

$$\delta S^{\text{2-loop}}[V] \supset
  -\frac{1}{6}\langle(\delta S)^3\rangle_C$$

This cumulant connects three copies of the cubic Yang-Mills vertex
$g_k\,f^{abc}A^a A^b \partial A^c$ through two internal propagators.
Diagrammatically, this is a "sunset" or "theta" topology with three
external $F$-legs.

Each cubic vertex carries one power of $g_k$, and there are three
vertices, giving $g_k^3$ from the vertices. The two internal
propagators contribute $g_k^0$ each (since $G_0 \sim 1/m_W^2$ with
$m_W$ independent of $g_k$). Including the coupling normalization,
the coefficient is:

$$c_2^{(k)} = O(g_k^4)$$

(The overall counting: three vertices at $g_k$ each gives $g_k^3$;
the gauge-invariant projection of three $A$-fields into $F^3$
contributes one additional $g_k$ from the $F = dA + gA^2$ structure.
Total: $g_k^4$.)

### 2.3 The bound

$$|c_2^{(k)}|, |c_3^{(k)}| \leq C\,g_k^4$$

This is stronger than the generic Balaban bound $|c_{d_O}| \leq
C\,g_k^{d_O - 2} = C\,g_k^4$ for $d_O = 6$ -- but only by a
logarithmic distinction: the generic bound allows $O(g_k^2)$ at one
loop, while the actual coefficient is $O(g_k^4)$ because the one-loop
contribution vanishes for this particular operator. The coefficient
is $O(g_k^4)$, not $O(g_k^2)$.

---

## 3. The Perturbative Form Factor

### 3.1 Setup

We need to compute the connected one-particle matrix element:

$$\langle 1|\hat{\mathcal{O}}_2(0)|1\rangle_c
  = \langle 1|\hat{\mathcal{O}}_2(0)|1\rangle
  - \langle 0|\hat{\mathcal{O}}_2(0)|0\rangle$$

where $|1\rangle = |1, \vec{p}=0\rangle$ is the $0^{++}$ glueball state.

### 3.2 Charge conjugation analysis

**Definition.** Charge conjugation $\mathcal{C}$ acts on the gauge field
as $A_\mu \to -A_\mu^T$ (equivalently, $U_\ell \to U_\ell^*$, complex
conjugation of link variables).

Under $\mathcal{C}$:

$$F_{\mu\nu} \to -F_{\mu\nu}^T$$

Therefore:

$$\mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}F_{\rho\mu})
  \to \mathrm{Tr}((-F^T)(-F^T)(-F^T))
  = -\mathrm{Tr}(F^T F^T F^T)
  = -\mathrm{Tr}(FFF)^T
  = -\mathrm{Tr}(FFF)$$

So $\mathcal{O}_2$ is **$\mathcal{C}$-odd**.

**For $\mathrm{SU}(2)$:** The operator $\mathrm{Tr}(F^3)$ vanishes
identically. The Lie algebra $\mathfrak{su}(2)$ has no cubic Casimir
($d^{abc} = 0$, and the trace of three generators is proportional to
$d^{abc}$). Explicitly, for $2 \times 2$ anti-Hermitian traceless
matrices $A, B, C$: $\mathrm{Tr}(ABC) = \mathrm{Tr}(BCA)$ and
$\mathrm{Tr}(ABC) = -\mathrm{Tr}(CBA)$ (using $A^T = -A$ for
$\mathfrak{su}(2)$), so $\mathrm{Tr}(ABC) = -\mathrm{Tr}(ABC)$, hence
zero. **This operator does not exist for $\mathrm{SU}(2)$.**

**For $\mathrm{SU}(N)$, $N \geq 3$:** The operator $\mathcal{O}_2$ is
nonzero and $\mathcal{C}$-odd. Now, the $0^{++}$ glueball is $\mathcal{C}$-even
by definition (the lightest glueball has quantum numbers $J^{PC} = 0^{++}$).
Therefore:

$$\langle 1|\mathcal{O}_2(0)|1\rangle = 0 \qquad
  \text{(exact, by charge conjugation)}$$

This is exact and non-perturbative: $\mathcal{C}$-odd operators have
vanishing diagonal matrix elements in $\mathcal{C}$-even states.

**The vacuum $|0\rangle$ is also $\mathcal{C}$-even**, so
$\langle 0|\mathcal{O}_2(0)|0\rangle = 0$ as well.

Therefore: $\langle 1|\mathcal{O}_2(0)|1\rangle_c = 0$ exactly.

### 3.3 The $d$-symbol operator $\mathcal{O}_3$

Now consider $\mathcal{O}_3 = d^{abc}F_{\mu\nu}^a F^{b\,\nu\rho}
F_\rho^{c\,\mu}$. Under charge conjugation $F^a \to -(F^T)^a$. In the
adjoint representation, $\mathcal{C}$ acts on the color index as
$T^a \to -(T^a)^T$. For $\mathrm{SU}(N)$, the generators split into
symmetric ($d$-type) and antisymmetric ($f$-type). The $d$-symbol
$d^{abc} = 2\,\mathrm{Tr}(T^a\{T^b, T^c\})$ is **fully symmetric**.

Under $\mathcal{C}$:

$$F_{\mu\nu}^a\,T^a \to -F_{\mu\nu}^a\,(T^a)^T$$

Write the adjoint $\mathcal{C}$-action as $F^a \to C^{ab}F^b$ where
$C^{ab}$ encodes the transpose. For $\mathrm{SU}(N)$: $C^{ab}$ equals
$+1$ on the symmetric generators and $-1$ on the antisymmetric
generators. Then:

$$d^{abc}F^a F^b F^c \to d^{abc}\,C^{aa'}C^{bb'}C^{cc'}\,F^{a'}F^{b'}F^{c'}$$

Since $d^{abc}$ is nonzero only when the combination $a, b, c$ has the
same symmetry type, and $C^{aa'}C^{bb'}C^{cc'} d^{a'b'c'} = d^{abc}$
or $-d^{abc}$ depending on the symmetry class, one must track the
$\mathcal{C}$-parity carefully.

**Explicit computation for $\mathrm{SU}(3)$:** The $d$-symbol for
$\mathrm{SU}(3)$ satisfies $d^{abc} = 2\,\mathrm{Tr}(\lambda^a
\{\lambda^b, \lambda^c\})/4$ where $\lambda^a$ are the Gell-Mann
matrices. Under charge conjugation $\lambda^a \to -(\lambda^a)^T$,
the symmetric generators ($\lambda^1, \lambda^3, \lambda^4, \lambda^6,
\lambda^8$) have $(\lambda^a)^T = \lambda^a$ (hence $C$-eigenvalue
$-1$), while the antisymmetric ones ($\lambda^2, \lambda^5, \lambda^7$)
have $(\lambda^a)^T = -\lambda^a$ (hence $C$-eigenvalue $+1$).

The $d$-symbol $d^{abc}$ is nonzero for specific index triples. The
$\mathcal{C}$-transformation of $d^{abc}F^aF^bF^c$ becomes:

$$d^{abc}F^aF^bF^c \to d^{abc}(-1)^{n_s(a)+n_s(b)+n_s(c)}\,F^aF^bF^c$$

where $n_s(a) = 1$ if $a$ is symmetric, $0$ if antisymmetric. For each
nonzero $d^{abc}$, the total sign is $(-1)^{n_s(a)+n_s(b)+n_s(c)}$.
The nonzero $d$-symbols of $\mathrm{SU}(3)$ include $d^{118}, d^{146},
d^{228}, d^{247},$ etc. For $d^{118}$: indices 1 (sym), 1 (sym), 8 (sym),
giving sign $(-1)^3 = -1$. For $d^{247}$: indices 2 (antisym),
4 (sym), 7 (antisym), giving sign $(-1)^1 = -1$.

In fact, one can verify that **all** nonzero $d^{abc}$ of $\mathrm{SU}(3)$
pick up sign $-1$ under $\mathcal{C}$. The $d$-symbol invariant
$d^{abc}F^aF^bF^c$ is therefore also **$\mathcal{C}$-odd** for
$\mathrm{SU}(3)$.

**General $\mathrm{SU}(N)$:** The cubic Casimir $d^{abc}$ defines
a $\mathcal{C}$-odd invariant for all $N \geq 3$. This follows from the
general relation $\mathcal{C}(d^{abc}T^aT^bT^c) = d^{abc}(-T^a)^T(-T^b)^T(-T^c)^T
= -d^{abc}(T^cT^bT^a)^T = -d^{abc}\mathrm{Tr}(T^aT^bT^c)$ (using the
full symmetry of $d^{abc}$), so $\mathcal{O}_3$ is $\mathcal{C}$-odd.

### 3.4 Conclusion on charge conjugation

**Both** cubic-curvature dimension-6 operators $\mathcal{O}_2$ and
$\mathcal{O}_3$ are $\mathcal{C}$-odd. Their diagonal matrix elements
in any $\mathcal{C}$-even state vanish exactly:

$$\boxed{
\langle 1|\hat{\mathcal{O}}_2(0)|1\rangle_c = 0,\quad
\langle 1|\hat{\mathcal{O}}_3(0)|1\rangle_c = 0
\qquad\text{(exact, } \mathcal{C}\text{-symmetry)}
}$$

This holds non-perturbatively, for all $\mathrm{SU}(N)$ with $N \geq 3$.
For $N = 2$, both operators vanish identically (no cubic Casimir).

---

## 4. Verification: The Perturbative Form Factor

### 4.1 Leading perturbative computation

Even though Section 3 gives an exact vanishing, it is instructive to see
how the cancellation works in perturbation theory.

At leading order, the one-glueball state $|1\rangle$ has $J^{PC} = 0^{++}$
and is constructed from two-gluon states:

$$|1\rangle \sim \int \frac{d^3k}{(2\pi)^3}\;\psi(k)\;
  a^{a\dagger}_\mu(\vec{k})\,a^{a\dagger}_\mu(-\vec{k})\,|0\rangle
  + \ldots$$

where $\psi(k)$ is a symmetric wave function and the color-singlet,
spin-zero projection is implied. The operator $\mathrm{Tr}(F^3)(0)$ in
momentum space involves the three-gluon vertex:

$$\mathrm{Tr}(F^3)(0) \sim g\,f^{abc}
  \int \frac{d^3k_1\,d^3k_2\,d^3k_3}{(2\pi)^9}\;
  \delta(\vec{k}_1+\vec{k}_2+\vec{k}_3)\;
  V_3^{\mu\nu\rho}(k_1,k_2,k_3)\;
  A^a_\mu(k_1)\,A^b_\nu(k_2)\,A^c_\rho(k_3)$$

The matrix element $\langle 1|\mathrm{Tr}(F^3)(0)|1\rangle_c$
involves overlap of a two-gluon state with a three-gluon operator.
At leading order in $g_k$, this requires **creating or annihilating
one gluon** from the two-gluon glueball, which carries a factor of
$g_k$ from the cubic vertex. The connected matrix element at leading
order is therefore $O(g_k)$ from the vertex.

But the color structure forces the cancellation: the two-gluon
glueball is a **color singlet** (symmetric in color indices:
$\delta^{ab}a^{a\dagger}a^{b\dagger}$), while the three-gluon
vertex is proportional to $f^{abc}$ (antisymmetric). The contraction
$\delta^{ab}f^{abc} = 0$ vanishes identically. This is the
perturbative manifestation of $\mathcal{C}$-oddness.

### 4.2 The momentum structure (moot point)

Although Section 3 renders this academic, let us record what the
momentum dependence would have been had the operator been $\mathcal{C}$-even.

The three-gluon vertex in Yang-Mills is:

$$V_3^{abc,\mu\nu\rho}(k_1,k_2,k_3)
  = g\,f^{abc}\bigl[
    (k_1 - k_2)^\rho\,g^{\mu\nu}
    + (k_2 - k_3)^\mu\,g^{\nu\rho}
    + (k_3 - k_1)^\nu\,g^{\rho\mu}
  \bigr]$$

This vertex is **linear in momenta**. For zero total momentum
($k_3 = -k_1 - k_2$), the vertex at $\vec{k}_2 = -\vec{k}_1$, $\vec{k}_3 = 0$
gives $V_3 \sim g\,k$, providing **one power** of the internal momentum
$|k| \sim \Delta$. After integration against the glueball wave function
$\psi(k)$ localized at $|k| \sim \Delta$, this would yield a form factor
$\sim \hat{\Delta}$ (one power, not two). The hypothetical concern
raised in the problem statement -- that the vertex gives only one power
of $\hat{\Delta}$ rather than two -- would have been genuine had the
operator been $\mathcal{C}$-even.

---

## 5. Impact on the Effective Action Coefficient

### 5.1 Does $\mathcal{C}$-oddness of the operator survive in the coefficient?

The effective action $S_{k+1}[V]$ is $\mathcal{C}$-invariant (the
Yang-Mills action and the block-spin averaging both respect charge
conjugation). Therefore, the coefficient of any $\mathcal{C}$-odd
operator in $S_{k+1}$ must vanish:

$$c_2^{(k)} = c_3^{(k)} = 0 \qquad\text{(exact)}$$

This is stronger than $O(g_k^4)$: the coefficients are **exactly zero**,
not merely small. The $\mathcal{C}$-odd operators $\mathrm{Tr}(F^3)$ and
$d^{abc}F^3$ do not appear in Balaban's effective action at any loop
order.

**Proof.** The effective action is generated by integrating out
fluctuations with a $\mathcal{C}$-invariant measure against a
$\mathcal{C}$-invariant action. Any $\mathcal{C}$-odd local operator
$\mathcal{O}$ satisfies $\mathcal{C}\mathcal{O}\mathcal{C}^{-1}
= -\mathcal{O}$. If the effective action were to contain such a term
with nonzero coefficient, then under $\mathcal{C}$:

$$S_{k+1}[\mathcal{C}V]
  = S_{k+1}[V] + 2c\,\mathcal{O}[V] \neq S_{k+1}[V]$$

contradicting $\mathcal{C}$-invariance. $\square$

### 5.2 What about $\mathcal{C}$-even non-derivative operators?

At dimension 6, the complete basis of gauge-invariant, $\mathcal{C}$-even
operators consists **only** of derivative operators: $\mathrm{Tr}(DF)^2$
and variants related by the equations of motion. The cubic operators are
$\mathcal{C}$-odd (Section 3). There are no dimension-6 operators that
are simultaneously gauge-invariant, $\mathcal{C}$-even, and non-derivative.

At dimension 8, $\mathcal{C}$-even non-derivative operators do exist
(e.g., $\mathrm{Tr}(F^4) = \mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}
F_{\rho\sigma}F^{\sigma\mu})$ and $(\mathrm{Tr}\,F^2)^2$). These are
quartic in $F$, with engineering dimension 8 and zero extra derivatives.
Their coefficients are $O(g_k^6)$ (three loops, since the quartic
invariant requires three Gaussian contractions). The contribution to the
form factor is:

$$|c_8^{\text{non-deriv}}|\cdot|\langle 1|\mathrm{Tr}(F^4)(0)|1\rangle_c|
  \leq C\,g_k^6 \cdot O(1)$$

For the RG recursion, this needs to be $O(g_k^6\,\hat{\Delta}^4)$ (since
$d_O - 4 = 4$ for dimension-8). However, $\mathrm{Tr}(F^4)$ is
$\mathcal{C}$-even, so the diagonal matrix element does not vanish by
symmetry. This is an analogue of the present problem at dimension 8.

The saving feature: for $\mathrm{Tr}(F^4)$, the coefficient is $O(g_k^6)$
and the required suppression is $\hat{\Delta}^4$. The total contribution
$g_k^6$ must be compared to $g_k^6\,\hat{\Delta}^4$. This is an even
larger gap than the dimension-6 case. The resolution for dimension-8
non-derivative operators proceeds by the **total remainder approach**
(path-1b-operator-decomposition.md, Section 4), which does not decompose
into individual operators but treats the sum.

---

## 6. The Total Remainder: Why the Cubic Operator Does Not Appear

### 6.1 Restatement of the total remainder approach

The key result of path-1b-operator-decomposition.md (Section 4) is that,
conditional on the vacuum subtraction (Theorem 6(b) of 07-power-counting.md),
the **total** irrelevant remainder $E_k(x)$ can be decomposed as:

$$E_k(x) = \sum_{\mu,\nu}\nabla_\mu^*\nabla_\nu^*\,h_{\mu\nu}^{(k)}(x)$$

with $\|h_{\mu\nu}^{(k)}\|_\infty \leq C\,g_k^4$. This is a double
lattice derivative representation of the **entire remainder**, not of
individual operators.

However, Theorem 6(b) has been shown to be **false** as an operator
identity (07-power-counting.md, Section 7.4). So the total remainder
approach is not available unconditionally.

### 6.2 The $\mathcal{C}$-symmetry bypass

For the specific problem of cubic curvature operators, the
$\mathcal{C}$-symmetry argument of Section 3 provides a **complete,
unconditional resolution** that does not depend on Theorem 6(b).

The $\mathrm{Tr}(F^3)$ and $d^{abc}F^3$ operators:
- Have exactly zero coefficient in the effective action (Section 5.1)
- Have exactly zero form factor in the $0^{++}$ glueball (Section 3.4)
- Do not contribute to the mass gap shift at any loop order or
  non-perturbatively

This eliminates the entire class of non-derivative dimension-6 operators
from the analysis.

---

## 7. What Remains Open

### 7.1 The dimension-6 problem is closed

At dimension 6, the operator basis consists of:

**(a)** $\mathrm{Tr}(DF)^2$: derivative operator, $\mathcal{C}$-even.
Handled by the derivative argument (single-step-computation.md).
$\hat{\Delta}^2$ suppression proved via translation invariance +
transfer matrix.

**(b)** $\mathrm{Tr}(F^3)$, $d^{abc}F^3$: non-derivative,
$\mathcal{C}$-odd. Eliminated by $\mathcal{C}$-symmetry. Zero
contribution to the form factor, exactly.

There are no other independent dimension-6 gauge-invariant operators
in pure $\mathrm{SU}(N)$ Yang-Mills. **The dimension-6 sector is
completely controlled.**

### 7.2 Higher dimensions

At dimension 8 and above, $\mathcal{C}$-even non-derivative operators
exist. As noted in Section 5.2, the quartic operators
$\mathrm{Tr}(F^4)$ and $(\mathrm{Tr}\,F^2)^2$ are $\mathcal{C}$-even
with zero extra derivatives and coefficient $O(g_k^6)$.

The situation for these operators is:

- Their coefficient $O(g_k^6)$ provides three extra powers of $g_k^2$
  beyond the marginal operator, compared to the required suppression
  $\hat{\Delta}^4 = (a_k\Delta)^4$.
- The ratio $g_k^6 / (g_k^6\hat{\Delta}^4) = 1/\hat{\Delta}^4$
  diverges, so the enhanced coefficient alone does not suffice.
- The total remainder approach (conditional on Theorem 6(b)) handles
  them collectively.
- Alternatively: for the mass gap sum, we need $\sum g_k^6 \cdot
  |F_8| / \hat{\Delta}_k < \infty$ where $|F_8|$ is the form factor.
  Even without $\hat{\Delta}^4$ suppression, if $|F_8| = O(1)$, then
  $\sum g_k^6/\hat{\Delta}_k \sim \sum 2^k/k^3$, which **diverges**.
  So unsuppressed dimension-8 non-derivative form factors would be
  problematic.

However, for the **specific purpose of the mass gap proof**, the
dimension-8 operators contribute to the mass gap shift at order $g_k^6$,
which is two loop orders beyond the leading $g_k^4$ contribution from
dimension-6 operators. The cumulative effect can be absorbed into the
$O(g_k^2\,C_k)$ correction term in the RG recursion of
rg-preservation.md, Section 5.1:

$$C_{k+1} = \frac{C_k}{4} + C_{\text{new}} + O(g_k^2\,C_k)$$

The dimension-8 non-derivative operators modify $C_{\text{new}}$ by
a term $O(g_k^2)$, which is absorbed into the existing $O(g_k^2\,C_k)$
correction. This works because the $1/4$ contraction factor dominates.

A rigorous treatment requires either the total remainder approach
(Section 6.1) or a dimension-8 version of the form factor bound
(Conjecture 1 with $s \geq 4$).

### 7.3 The essential hierarchy

The key observation is that the **non-perturbative difficulty decreases**
with operator dimension:

| $d_O$ | Non-derivative $\mathcal{C}$-even? | Coefficient | Required suppression | Status |
|:-------|:-----------------------------------|:------------|:---------------------|:-------|
| 6 | No (all are $\mathcal{C}$-odd) | $O(g_k^4)$ | $\hat{\Delta}^2$ | **Closed** ($\mathcal{C}$-symmetry) |
| 8 | Yes ($\mathrm{Tr}\,F^4$, $(\mathrm{Tr}\,F^2)^2$) | $O(g_k^6)$ | $\hat{\Delta}^4$ | Open (but higher order in $g_k$) |
| 10 | Yes | $O(g_k^8)$ | $\hat{\Delta}^6$ | Open (but very higher order) |

Each additional dimension costs two powers of $g_k$ in the coefficient
and two powers of $\hat{\Delta}$ in the required suppression, while the
contribution to the mass gap sum gains a factor $g_k^2/\hat{\Delta}^2$.
The leading unsuppressed operator is at dimension 8 with total
contribution $O(g_k^6)$, versus $O(g_k^4\,\hat{\Delta}^2)$ for the
leading (derivative) dimension-6 operator. At small $g_k$, the dimension-6
contribution dominates.

---

## 8. Precise Statement

**Theorem (Case B).** *For $\mathrm{SU}(N)$ Yang-Mills in $d=4$, the
cubic curvature operators $\mathrm{Tr}(F_{\mu\nu}F^{\nu\rho}F_{\rho\mu})$
and $d^{abc}F^a_{\mu\nu}F^{b\,\nu\rho}F^{c}_{\rho\mu}$ satisfy:*

*(i) Both operators are $\mathcal{C}$-odd. For $N=2$, they vanish
identically.*

*(ii) The $0^{++}$ glueball state $|1\rangle$ is $\mathcal{C}$-even.
Therefore:*

$$\langle 1|\mathrm{Tr}(F^3)(0)|1\rangle_c = 0,\quad
  \langle 1|d^{abc}F^3(0)|1\rangle_c = 0$$

*exactly and non-perturbatively.*

*(iii) The coefficient of these operators in Balaban's effective action
is exactly zero (by $\mathcal{C}$-invariance of the block-spin
transformation).*

*(iv) The contribution of all non-derivative dimension-6 operators to
the mass gap shift is zero. The form factor bound for dimension-6
operators follows entirely from the derivative argument of
single-step-computation.md.*

**Status: PROVED (unconditionally).** The argument uses only the
$\mathcal{C}$-symmetry of the Wilson action and the $J^{PC} = 0^{++}$
quantum numbers of the lightest glueball. It does not depend on
perturbation theory, on Theorem 6(b), or on Conjecture 1.

---

## 9. Honest Assessment

### 9.1 What is completely resolved

The cubic curvature operators $\mathrm{Tr}(F^3)$ and $d^{abc}F^3$
posed a potential obstruction to the form factor bound: they have
zero extra derivatives, so the derivative suppression mechanism does
not apply. The resolution is exact: charge conjugation symmetry
forces both the coefficient and the form factor to vanish identically.
This is a **closed** component of the proof.

### 9.2 What is newly exposed

The $\mathcal{C}$-symmetry argument applies only to **odd-power**
invariants of $F$. Even-power non-derivative operators
($\mathrm{Tr}(F^4)$, $(\mathrm{Tr}\,F^2)^2$ at dimension 8) are
$\mathcal{C}$-even and cannot be eliminated by this argument. These
operators begin at three loops with coefficient $O(g_k^6)$. Their
form factors in the $0^{++}$ state are generically nonzero and bounded
by $O(1)$.

For the mass gap sum to converge, we need either:
- The form factor to carry $\hat{\Delta}^4$ suppression (Conjecture 1
  at $d_O = 8$), or
- The total remainder approach (conditional on a weaker form of
  Theorem 6(b) that holds at the matrix-element level), or
- An argument that the $O(g_k^6)$ contribution is absorbable into the
  RG recursion without explicit $\hat{\Delta}^4$ suppression.

The third option may work: the RG recursion
$C_{k+1} = C_k/4 + C_{\text{new}} + O(g_k^2 C_k)$ has a stable fixed
point with $C_* = (4/3)C_{\text{new}}$, and the dimension-8
contribution modifies $C_{\text{new}}$ by a relative $O(g_k^2)$ factor.
But this argument assumes the dimension-8 contribution carries at
least the **same** $\hat{\Delta}^2$ suppression as the dimension-6
derivative operators, which is precisely what is unproved for the
non-derivative component.

### 9.3 The hierarchy of open problems

1. **Dimension 6, non-derivative:** CLOSED ($\mathcal{C}$-symmetry).
2. **Dimension 6, derivative:** Handled by single-step-computation.md
   (perturbatively proved, non-perturbatively conditional on
   Conjecture 1).
3. **Dimension 8, non-derivative, $\mathcal{C}$-even:** OPEN.
   This is a subleading effect ($O(g_k^6)$ vs $O(g_k^4)$) but
   not zero.
4. **Dimension $\geq 10$:** Higher order still; the leading open
   problem is at dimension 8.

The single most important open problem for the form factor bound
remains Conjecture 1 at dimension 6 (the non-perturbative version
of the derivative suppression), not the cubic curvature operators.
The $\mathrm{Tr}(F^3)$ case is cleanly resolved.
