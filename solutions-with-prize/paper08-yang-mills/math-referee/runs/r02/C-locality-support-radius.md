# Point C: Step 4 -- Locality and Support Radius of E_k

## Verdict: NON-ISSUE when units are correctly tracked, but presentation is misleading

---

## The Claim Under Scrutiny

Step 4 uses a Taylor bound:

$$|\hat{E}_k(q)| \leq C_{\text{Hess}} \, |q|^2$$

where $C_{\text{Hess}} = C g_k^4 \times R_O^2 \times |B_{R_O}|$
involves the support radius $R_O$ of $E_k(x)$. The claim is that
$R_O$ is independent of the RG step $k$.

The concern: $E_k$ lives on the block lattice of spacing $L^k a_0$.
Does $R_O$ grow as $L^k$ in original lattice units, causing
$C_{\text{Hess}}$ to diverge?

## Analysis

### The two unit systems

There are two natural unit systems:

**(a) Original lattice units** (spacing $a_0 = 1$). The block lattice
at step $k$ has spacing $L^k$. The support radius of $E_k$ in these
units is $R_O^{(\text{orig})} = c \cdot L^k$ (a few block lattice
spacings, each of size $L^k$).

**(b) Block lattice units** (spacing $a_k = 1$). The block lattice
at step $k$ is the "unit lattice" at that scale. The support radius
is $R_O^{(\text{block})} = c$ (a constant, typically 1-3 block
lattice spacings).

### Which units does the Taylor bound use?

The Taylor bound involves Fourier transforms and momenta. The
relevant momentum $q$ is defined on the **block lattice** at step $k$:
$q \in (-\pi/a_k, \pi/a_k]$ in physical units, or equivalently
$q \in (-\pi, \pi]$ in block lattice units.

The mass gap $\hat{\Delta}_k = a_k \Delta$ is in block lattice units.
The momentum transfer $|q| \leq 2\hat{\Delta}_k$ is in block lattice
units.

The Hessian bound:

$$|\partial_\mu \partial_\nu \hat{E}_k(q)| \leq \sum_x |x_\mu x_\nu|
\, |E_k(x)|$$

where $x$ is in **block lattice units**. In these units, $|x| \leq
R_O^{(\text{block})} = c$ (constant), so:

$$C_{\text{Hess}} = (R_O^{(\text{block})})^2 \times |B_{R_O^{(\text{block})}}|
\times M_O$$

with:
- $R_O^{(\text{block})} = c$: constant, independent of $k$
- $|B_{R_O}| \leq (2c+1)^d$: constant, independent of $k$
- $M_O = \|E_k\|_\infty \leq C g_k^4$: from Balaban, **decreasing** with $k$

Therefore:

$$C_{\text{Hess}} \leq C' g_k^4$$

This is **bounded uniformly in $k$** and in fact **decreases** with
$k$ (since $g_k \to 0$ by asymptotic freedom).

### The confusion in original lattice units

If one mistakenly uses original lattice units throughout, the support
radius is $R_O^{(\text{orig})} \sim L^k$, the number of sites in
the support ball is $|B| \sim L^{dk}$, and the Hessian constant
becomes:

$$C_{\text{Hess}}^{(\text{orig})} \sim g_k^4 \times L^{2k} \times L^{dk}
= g_k^4 \times L^{(d+2)k}$$

which diverges exponentially with $k$. This would invalidate the
Taylor bound.

But this calculation is **wrong** -- it uses the wrong unit system.
The Fourier transform, the momenta, and the support radius must all
be expressed in the same units (block lattice units at step $k$),
and in those units everything is bounded.

### Why block lattice units are correct

At RG step $k$, the theory lives on the block lattice. The transfer
matrix, the Hamiltonian, the spectral gap -- all are defined on the
block lattice. The Fourier transform of $E_k(x)$ is taken over the
block lattice sites, with momenta in the block Brillouin zone. The
one-particle state has dimensionless mass gap $\hat{\Delta}_k = a_k \Delta$
in block lattice units.

The entire form factor computation (Steps 4-6) operates within the
block lattice at step $k$. The original lattice spacing $a_0$ does
not appear.

### Balaban's locality guarantee

Balaban's construction produces an effective action that is **local
on the block lattice**: each term involves block gauge fields within
a bounded number of block lattice spacings. This is a key output of
the RG construction (locality of the effective action). The bounded
support radius in block lattice units is not an assumption -- it is
a theorem of Balaban's.

Specifically, Balaban proves that the irrelevant remainder has the
form $E_k = \sum_x E_k(x)$ where each $E_k(x)$ depends on block
link variables $U_\ell$ for links $\ell$ within distance $R_{\text{Bal}}$
of $x$ (in block lattice units), with $R_{\text{Bal}}$ a universal
constant (independent of $k$, $g$, and the volume).

## What the Proof Should Clarify

The proof should explicitly state:

1. All quantities in the Taylor bound (momenta, positions, support
   radii) are in block lattice units at step $k$.

2. The support radius $R_O$ is bounded in block lattice units by
   Balaban's locality theorem.

3. The Hessian constant $C_{\text{Hess}} \leq C g_k^4$ (with $C$
   independent of $k$) follows from the block-lattice locality and
   Balaban's norm bound.

Without this clarification, a reader could mistakenly interpret
$R_O$ as a quantity in original lattice units and conclude that
the bound breaks down.

## Summary

The concern about the support radius growing with $k$ is a
**non-issue** when units are correctly tracked. In block lattice
units (the natural units for the RG step), $R_O$ is a constant
independent of $k$, and the Hessian constant is uniformly bounded.
The proof's claim is correct but poorly presented.

**Severity: NONE** (mathematically). The presentation should be
improved to avoid confusion.
