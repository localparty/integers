# Appendix J: The Lattice Dimension-6 Operator Basis

A self-contained derivation proving that every local, gauge-invariant,
C-even, parity-even operator of engineering dimension 6 on the $d=4$
hypercubic lattice falls into one of the four classes listed in
Section 5.6, Part III.3.

---

## J.1 Setup and Definitions

On the lattice the spacing $a$ carries dimension $[\text{length}]$.
Link variables $U_\ell \in \mathrm{SU}(N)$ are dimensionless.
The plaquette variable

$$
  s_P \;=\; 1 \;-\; \frac{1}{N}\,\mathrm{Re}\,\mathrm{Tr}\, U_P
$$

has the small-$a$ expansion

$$
  s_P \;=\; \frac{a^4}{2N}\,\mathrm{Tr}(F_{\mu\nu})^2
        \;+\; O(a^6)\,,
$$

so $s_P$ carries **engineering dimension 4** (not 0), because the
continuum field strength $F_{\mu\nu}$ has mass dimension 2.

**Definition.**
A lattice operator has *engineering dimension $d$* if it is a
gauge-invariant polynomial in link variables whose leading term in the
continuum expansion is of mass dimension $d$.

---

## J.2 Building Blocks

The gauge-invariant building blocks available on the hypercubic lattice
are:

1. **Single-plaquette traces.**
   $\mathrm{Re}\,\mathrm{Tr}\,U_P$ has dimension 4 via $s_P$.

2. **Products of plaquettes at the same site.**
   $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^n$ has leading continuum
   dimension $4n$.

3. **Products of plaquettes sharing an edge.**
   Traces of the form $\mathrm{Tr}(U_{P_1} U_{P_2})$, where $P_1$
   and $P_2$ share one link. These have the same leading dimension as
   the product of two separate plaquette traces, namely dimension 8.

4. **Wilson loops on small contours.**
   Rectangular $1\times 2$ loops, bent (L-shaped) loops, chair-shaped
   loops, etc.  A $1\times 2$ rectangle has a continuum expansion
   starting at dimension 4 but with a dimension-6 correction
   proportional to $a^2\,\mathrm{Tr}(D_\rho F_{\mu\nu})^2$.

5. **Lattice covariant derivatives of plaquettes.**
   The lattice finite difference

   $$
     \nabla_\mu\, s_P(x)
       \;=\; s_P(x + a\hat\mu) \;-\; s_P(x)
   $$

   represents the continuum covariant derivative $D_\mu$ acting on
   $\mathrm{Tr}\,F^2$ and adds one unit of engineering dimension.

**Key observation.**
Products of $n$ plaquettes at the same vertex have leading continuum
dimension $4n$.  To reach dimension 6 from plaquette products alone
one would need $n = 3/2$, which is impossible.  Therefore
*dimension-6 operators cannot be built from products of plaquettes at
a single vertex*; they necessarily involve lattice finite differences
(covariant derivatives) of plaquettes.

---

## J.3 Classification

### Step 1: Zero-derivative operators at dimension 6

Without lattice derivatives one needs operators cubic in $F_{\mu\nu}$.
The only dimension-6, zero-derivative, gauge-invariant candidates are

$$
  \mathrm{Tr}(F_{\mu\nu} F_{\nu\rho} F_{\rho\mu})
  \qquad\text{and}\qquad
  d^{abc}\,F^a_{\mu\nu}\,F^b_{\nu\rho}\,F^c_{\rho\mu}\,.
$$

Both are **C-odd**: under charge conjugation $F_{\mu\nu} \to
-F_{\mu\nu}^T$, so every trace of an odd power of $F$ changes sign
(Section 5.3.1).  They are therefore eliminated from the C-even
sector.

No other zero-derivative dimension-6 operators exist because:

- $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^2$ starts at dimension 8.
- $\mathrm{Tr}(U_P^2)$ starts at dimension 8.
- Higher terms in the single-plaquette expansion of $s_P$ are
  dimension $\geq 8$.
- Products of plaquettes at different sites sharing a vertex involve
  implicit derivatives and are treated in Step 3.

### Step 2: One-derivative operators (dimension 5)

A dimension-5 operator would require an odd total power of $F$ under
the trace.  Under charge conjugation,

$$
  C\bigl(\mathrm{Tr}(F^{2k+1})\bigr)
    \;=\; (-1)^{2k+1}\,\mathrm{Tr}(F^{2k+1})
    \;=\; -\,\mathrm{Tr}(F^{2k+1})\,.
$$

All odd-power traces are C-odd.  **The C-even sector contains no
dimension-5 operators.**

### Step 3: Two-derivative operators (dimension 6, C-even)

These are the surviving operators.  A "two-derivative dimension-6
operator" involves two lattice finite differences of the dimension-4
building block $s_P$.  The only dimension-4, gauge-invariant, C-even
object is $s_P$ itself.

Two lattice derivatives give

$$
  \nabla_\rho\,\nabla_\sigma\, s_P(x)
    \;=\; s_P(x + a\hat\rho + a\hat\sigma)
       \;-\; s_P(x + a\hat\rho)
       \;-\; s_P(x + a\hat\sigma)
       \;+\; s_P(x)\,.
$$

In the continuum limit,

$$
  \nabla_\rho\,\nabla_\sigma\, s_P
    \;\longrightarrow\;
    a^2\, D_\rho\, D_\sigma\, \mathrm{Tr}(F_{\mu\nu})^2
    \;+\; O(a^3)\,.
$$

The independent continuum structures are:

**(a)** $\displaystyle\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ --- the
square of a single covariant derivative of the field strength.  On the
lattice this corresponds to

$$
  \frac{1}{a^2}\sum_{\rho,\,\mu<\nu}
    \bigl[s_{P_{\mu\nu}}(x + a\hat\rho) - s_{P_{\mu\nu}}(x)\bigr]^2\,.
$$

**(b)** $\displaystyle\mathrm{Tr}\bigl(D_\mu F^{\mu\rho}\,
D_\nu F^{\nu}{}_{\rho}\bigr)$ --- related to (a) by the equations of
motion modulo C-odd terms and higher-dimension operators.  On the
lattice:

$$
  \frac{1}{a^2}\sum_\nu
    \Bigl[\sum_\mu
      \bigl(s_{P_{\mu\nu}}(x + a\hat\mu) - s_{P_{\mu\nu}}(x)\bigr)
    \Bigr]^2\,.
$$

### Step 4: Three-or-more-derivative operators

Three or more lattice derivatives of a dimension-4 building block
produce operators of engineering dimension $\geq 7$.  These do not
contribute at dimension 6.

### Step 5: Lattice-specific operators

The central question is whether the hypercubic lattice introduces
operators absent in the continuum.  The Symanzik effective theory
[1] addresses this directly.  Expanding the Wilson plaquette
action in powers of $a$:

$$
  S_W \;=\; \frac{a^4}{2N}\sum_P \mathrm{Tr}(F_{\mu\nu})^2
       \;+\; \frac{a^6}{24N}\sum_P
         \Bigl[\mathrm{Tr}(D_\rho F_{\mu\nu})^2
           \;-\; \tfrac{1}{2}\,
                 \mathrm{Tr}\bigl([F_{\mu\nu},F_{\rho\sigma}]\bigr)^2
           \;+\; \cdots\Bigr]
       \;+\; O(a^8)\,.
$$

The $a^6$ terms are precisely the dimension-6 operators of the
Luscher--Weisz basis [2].

Operators that exist on the lattice but not in the continuum --- for
example, $\mathrm{O}(4)$-breaking contractions such as
$\sum_\mu \mathrm{Tr}(D_\mu F_{\mu\nu})^2$ with *no* sum over the
repeated $\mu$ index --- are included in the Symanzik classification
as separate operators.  However, they share the same two-derivative
structure as the $\mathrm{O}(4)$-invariant operators and therefore
carry the same deviation order ($\mathrm{dev} \geq 2$).  These
$\mathrm{O}(4)$-breaking operators contribute to Euclidean covariance
restoration (OS2) and vanish in the continuum limit.

### Step 6: Redundant operators

The classical equations of motion $D_\mu F^{\mu\nu} = 0$ (on-shell)
relate different two-derivative operators.  Off-shell, these relations
introduce higher-dimension corrections.

Following the standard treatment of Luscher and Weisz [2,
Section 3]: operators proportional to the equations of motion can be
absorbed by a field redefinition $A_\mu \to A_\mu + a^2\,\delta
A_\mu$, which shifts the dimension-6 coefficients without changing
physical observables.  After this reduction the independent basis
consists of two operators (or one, if the equations of motion are
imposed).  **Both carry $\mathrm{dev} \geq 2$.**

---

## J.4 Summary

**Theorem J.1.**
*Every local, gauge-invariant, C-even operator of engineering
dimension 6 on the $d = 4$ hypercubic lattice with gauge group
$\mathrm{SU}(N)$, $N \geq 2$, is a linear combination of:*

> **(I)** *The operator $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and its
> $\mathrm{O}(4)$-breaking variants --- all with $\mathrm{dev} \geq 2$;*

> **(II)** *The operator $\mathrm{Tr}(D_\mu F^{\mu\rho}\,D_\nu
> F^{\nu}{}_\rho)$ and variants --- related to (I) by the equations of
> motion modulo C-odd and higher-dimension terms, also with
> $\mathrm{dev} \geq 2$.*

*No zero-derivative or one-derivative dimension-6 operator survives
the C-even constraint.  The classification coincides with the
continuum Luscher--Weisz basis* [2] *up to
$\mathrm{O}(4)$-breaking terms that share the same derivative
structure and vanish in the continuum limit.*

---

### References

[1] K. Symanzik, *Continuum limit and improved action in lattice
theories*, Nucl. Phys. B **226** (1983) 187--204.

[2] M. Luscher and P. Weisz, *On-shell improved lattice gauge
theories*, Commun. Math. Phys. **97** (1985) 59--77; Erratum:
**98** (1985) 433.

[3] P. Weisz and R. Wohlert, *Continuum limit improved lattice
action for pure Yang--Mills theory (II)*, Nucl. Phys. B **236**
(1984) 397--422.
