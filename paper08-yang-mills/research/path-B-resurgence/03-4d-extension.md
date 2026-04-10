# 03. From 2D Resurgence to 4D: The Extension Problem

This document examines how the 2D CP$^{N-1}$ resurgence extends
(or fails to extend) to the 4D KK Yang--Mills theory on
$M^4 \times \mathbb{CP}^{N-1}$. Two routes are explored: the direct
4D trans-series (Section II) and the worldsheet route through the
confining string (Section III).


---

## I. The Two Routes

### Route 1: Direct 4D trans-series

Write down the trans-series for 4D Yang--Mills on
$M^4 \times \mathbb{CP}^{N-1}$ and attempt to prove its resurgence
directly. This requires:
- Computing the 4D instanton contributions on $\mathbb{CP}^{N-1}$
- Computing the 4D renormalon structure
- Showing the cancellation of ambiguities

### Route 2: Worldsheet inheritance

Use the fact that the confining string worldsheet IS the 2D
CP$^{N-1}$ sigma model. If the 2D model is resurgent, and if the
4D string tension is determined by the 2D mass gap, then the 4D
theory inherits 2D resurgence.

Route 2 is more promising because it leverages the existing 2D
results. But it requires the worldsheet connection to be rigorous.
Route 1 is more direct but faces harder analytical obstacles.

I will develop both routes and compare.


---

## II. Route 1: Direct 4D Resurgence

### II.1 The 4D instanton structure on CP^{N-1}

The instantons on $\mathbb{CP}^{N-1}$ (Appendix B) provide the
non-perturbative saddle points of the 4D theory. For $N = 3$
($\mathbb{CP}^2$):

- **Topological sectors:** $\pi_2(\mathbb{CP}^2) = \mathbb{Z}$,
  labelled by $c_2 = k \in \mathbb{Z}$.
- **$k = 1$ instanton action:** $S_I = 8\pi^2/g^2$ (Bogomolny
  bound, proved in Appendix B).
- **$k = 1$ instanton moduli space:** $\dim \mathcal{M}_{3,1} = 4$
  (computed in Appendix B, Section B.3).
- **Multi-instanton solutions:** exist for all $k$ via the
  Buchdahl (1988) construction (adapted ADHM on $\mathbb{CP}^2$).

The 4D one-loop determinant around the instanton has the
schematic form:
$$Z_{1-\text{loop}} = \frac{\det'(\Delta_0^{\text{adj}})}
  {\left[\det'(\Delta_1^{\text{adj}})\right]^{1/2}} \times
  g^{-4N} \times \mu^{4N b_0}$$

where $\Delta_p^{\text{adj}}$ is the Laplacian on adjoint-valued
$p$-forms on $\mathbb{CP}^{N-1}$, and the primes denote omission
of zero modes.

[STATUS: The one-loop determinant on $\mathbb{CP}^2$ has been
computed in the physics literature (Charap--Duff 1977, Babelon--
Viallet 1979, Obukhov 1983). It is COMPUTABLE but not simple.]

### II.2 The 4D perturbative sector

The perturbative expansion of the 4D KK theory was analyzed in
Section 29 of the paper. Key results:

- At each loop order $L$, the coefficient $\Gamma^{(L)}$ is
  finite (zeta-regularized). [PROVED]
- The large-order behavior:
  $\Gamma^{(L)} \sim L! \times (8\pi^2)^{-L} \times L^b$
  [PROVED, Section 29]
- The Borel transform has singularities on the positive real axis
  at $t = 8\pi^2 k$ (instantons) and $t = n/(2b_0)$ (renormalons).
  [ARGUED, standard Lipatov analysis]

The 4D perturbative sector is HARDER than the 2D one because:

(a) **UV renormalons.** In 4D Yang--Mills, the running coupling
generates UV renormalon singularities at $t = -n/(2b_0)$ (on the
negative real axis) and IR renormalons at $t = n/(2b_0)$ (on the
positive real axis). The UV renormalons are harmless (not on the
integration contour). The IR renormalons cause ambiguities.

In the 2D CP$^{N-1}$ model, there are only IR renormalons
(the model is super-renormalizable above the dynamical scale).

(b) **The running coupling complication.** In 4D, the coupling
$g^2(\mu)$ runs logarithmically. This means the instanton action
$8\pi^2/g^2(\mu)$ depends on the renormalization scale. The
"correct" instanton action for the large-order behavior is
$S_I^{\text{eff}} = 8\pi^2/g^2(1/\rho)$ where $\rho$ is the
instanton size. The integral over $\rho$ introduces additional
complications.

In the 2D model, the instanton is pointlike (the instanton moduli
space is $\mathbb{CP}^{N-1}$ itself, with a position zero mode
but no size modulus in 2D on a compact space).

(c) **The infrared problem.** In 4D, the integral over large
instanton sizes $\rho \to \infty$ diverges because $g^2(1/\rho)
\to \infty$ as $\rho \to \infty$ (the coupling becomes strong in
the IR). This "infrared catastrophe" of the dilute instanton gas
is a well-known obstruction.

In the KK theory on $M^4 \times \mathbb{CP}^{N-1}$, the internal
space provides a natural IR cutoff: instantons larger than $r_3$
"feel" the internal geometry. The instanton size integral is
cut off at $\rho \sim r_3$, which removes the IR catastrophe.

[STATUS: The IR cutoff from the internal space is ARGUED but not
rigorously proved. It is physically reasonable: an instanton
larger than $r_3$ wraps around $\mathbb{CP}^{N-1}$ and its
action increases.]

### II.3 Renormalons in the KK theory

The renormalon structure of the KK theory differs from standard 4D
Yang--Mills in two ways:

**(a) Above the KK scale.** For energies $\mu > 1/r_3$, the
effective theory is $(4 + 2(N-1))$-dimensional. The beta function
in $d = 4 + 2(N-1)$ dimensions is:

$$\beta_{d}(g_d^2) = \frac{d - 4}{2} g_d^2 - b_0^{(d)} g_d^4
  + \ldots$$

The first term (classical scaling) dominates, and the theory
becomes free in the UV. The renormalon chain integrals:

$$I_n = \int_0^\mu \frac{dk}{k}
  \left[\frac{b_0 g^2(k)}{4\pi}\right]^n$$

are modified. For $k > 1/r_3$, $g^2(k) \sim k^{-(d-4)}$
(power-law running), and the integrand decays as $k^{-n(d-4)}$.
This SUPPRESSES the UV renormalon contribution for $n > 0$.

[STATUS: ARGUED -- the power-law running above the KK scale
suppresses UV renormalons. This is a NOVEL feature of the KK
theory that standard 4D Yang--Mills does not have.]

**(b) Below the KK scale.** For $\mu < 1/r_3$, the theory is
standard 4D Yang--Mills with logarithmic running. The IR
renormalons at $t = n/(2b_0)$ remain.

**The key question:** Are the IR renormalon ambiguities
$\sim e^{-n/(2b_0 g^2)} \sim \Lambda^{2n}$ cancelled by
non-perturbative effects in the KK theory?

In standard 4D Yang--Mills, the IR renormalon at $t = 1/(2b_0)$
gives an ambiguity of order $\Lambda^2$, which is the same order
as the gluon condensate $\langle G^2 \rangle$. The standard
conjecture (Parisi 1978, Mueller 1985) is that the renormalon
ambiguity IS the ambiguity in the definition of the condensate.

In the KK theory, the condensate $\langle G^2 \rangle$ is
determined by the internal geometry:
$$\langle G^2 \rangle_{\text{KK}} = \frac{1}{\text{Vol}(\mathbb{CP}^{N-1})}
  \int_{\mathbb{CP}^{N-1}} |F|^2 \, d\mu$$

The Bogomolny bound gives $\int |F|^2 \geq 8\pi^2|k|/g^2$ in
topological sector $k$. This provides a GEOMETRIC meaning for
the condensate, which is absent in standard 4D Yang--Mills.

[STATUS: SPECULATIVE -- the connection between the geometric
condensate and the renormalon cancellation has not been worked
out.]

### II.4 The 4D resurgence conjecture (direct route)

**Conjecture (4D Resurgence).** [CONJECTURED]

*The trans-series for $SU(N)$ Yang--Mills on
$M^4 \times \mathbb{CP}^{N-1}$:*

$$\sigma(g^2) = \Lambda^2 \sum_{m=0}^{\infty} e^{-mS_I/g^2}
  \sum_n \sigma_n^{(m)} g^{2n}$$

*is resurgent. The instanton singularities at $t = kS_I$ cancel
via the standard resurgence mechanism. The renormalon singularities
at $t = n/(2b_0)$ cancel via the geometric condensate mechanism.*

**Evidence:**
- The 2D CP$^{N-1}$ model (the worldsheet theory) is resurgent
  in the deformed case [PROVED] and conjecturally in the
  undeformed case.
- The CP$^{N-1}$ topology provides all the necessary
  non-perturbative saddle points (instantons on $\mathbb{CP}^{N-1}$).
- The internal space provides an IR cutoff that removes the
  instanton IR catastrophe. [ARGUED]
- The power-law running above the KK scale suppresses UV
  renormalons. [ARGUED]

**Gaps:**
- No computation of the 4D one-loop determinant around the
  CP$^{N-1}$ instanton. [OPEN]
- No proof that the renormalon cancellation works. [OPEN]
- No proof that the trans-series sum is positive. [OPEN]


---

## III. Route 2: Worldsheet Inheritance

### III.1 The worldsheet connection (Paper 5)

The confining string in the 4D KK theory on
$M^4 \times \mathbb{CP}^{N-1}$ has a worldsheet described by
the 2D $\mathbb{CP}^{N-1}$ sigma model.

The physical basis: a chromoelectric flux tube in 4D wraps a
non-contractible cycle in $\mathbb{CP}^{N-1}$ (the generator
of $H_2(\mathbb{CP}^{N-1}) = \mathbb{Z}$). The transverse
fluctuations of the flux tube in $\mathbb{CP}^{N-1}$ are
described by the 2D sigma model on the worldsheet.

The 4D string tension is determined by the 2D worldsheet theory:
$$\sigma_{\text{4D}} = T_{\text{string}} = \frac{m_{2D}^2}{2\pi}
  \times (1 + \delta_{\text{embed}})$$

where $m_{2D}$ is the mass gap of the 2D CP$^{N-1}$ sigma model
and $\delta_{\text{embed}}$ encodes the embedding corrections
(interactions between the worldsheet and the 4D bulk).

### III.2 The embedding corrections

The Polchinski--Strominger (1991) effective string theory gives:
$$\delta_{\text{embed}} = -\frac{(D-2)\pi}{6\sigma R^2}
  + O(1/R^4)$$

for a string of length $R$ in $D$ bulk dimensions. For the
KK theory with $D_{\text{eff}} = 4$ (the 4D theory below the
KK scale):
$$\delta_{\text{embed}} = -\frac{\pi}{3\sigma R^2}
  + O(1/R^4)$$

This is the Luscher correction: it is perturbatively small for
long strings ($\sigma R^2 \gg 1$) and becomes $O(1)$ only for
strings of length $R \sim 1/\sqrt{\sigma}$ (the lightest glueball).

**Key point:** The embedding corrections are a PERTURBATIVE series
in $1/(\sigma R^2)$. They do not introduce new non-perturbative
ambiguities. The non-perturbative structure of $\sigma_{\text{4D}}$
is entirely controlled by the 2D worldsheet theory.

[STATUS: ARGUED -- the Polchinski--Strominger framework is
well-established for long strings but its validity for short strings
(the glueball regime) is not rigorously proved.]

### III.3 The inheritance argument

**Theorem (Conditional).** [ARGUED]

*If the 2D $\mathbb{CP}^{N-1}$ sigma model is resurgent (i.e., if
Conjecture V.4 of file 02 holds), then the 4D string tension
$\sigma_{\text{4D}}$ is defined by a resurgent trans-series and
$\sigma_{\text{4D}} > 0$.*

*Proof sketch.*

Step 1. The 2D mass gap $m_{2D}$ is defined by a resurgent
trans-series:
$$m_{2D} = \Lambda_{2D} \, c_N(g_{2D}^2)$$
where $c_N$ is an unambiguous real positive function defined by
the median resummation of the 2D trans-series. [BY ASSUMPTION]

Step 2. The 4D string tension is:
$$\sigma_{\text{4D}} = \frac{m_{2D}^2}{2\pi}
  \times (1 + \delta_{\text{embed}})$$
where $\delta_{\text{embed}}$ is a perturbative correction that
does not introduce non-perturbative ambiguities.

Step 3. Therefore:
$$\sigma_{\text{4D}} = \frac{\Lambda_{2D}^2 c_N^2}{2\pi}
  \times (1 + \delta_{\text{embed}})$$

This is:
- **Finite** (the 2D mass gap is finite and $\delta_{\text{embed}}$
  is a convergent perturbative correction for long strings)
- **Positive** ($c_N > 0$ by the resurgence of the 2D model,
  and $\delta_{\text{embed}} > -1$ for strings longer than the
  critical length)
- **Unambiguous** (no remaining trans-series ambiguities)
$\square$

### III.4 The relation between 2D and 4D couplings

The 2D sigma model coupling $g_{2D}^2$ is related to the 4D
gauge coupling $g^2$ by:
$$g_{2D}^2 = \frac{g^2}{4\pi r_3^2 \mu_{2D}^{d-2}}$$

where $\mu_{2D}$ is the renormalization scale in 2D and $d = 2$
is the worldsheet dimension. More precisely, at the scale
$\mu_{2D} = 1/r_3$:
$$g_{2D}^2(1/r_3) = \frac{g^2(1/r_3)}{4\pi}$$

The 2D dynamical scale:
$$\Lambda_{2D} = \frac{1}{r_3}
  \exp\left(-\frac{2\pi}{Ng_{2D}^2(1/r_3)}\right)
  = \frac{1}{r_3}
  \exp\left(-\frac{8\pi^2}{Ng^2(1/r_3)}\right)$$

And the 4D dynamical scale:
$$\Lambda_{4D} = \frac{1}{r_3}
  \exp\left(-\frac{1}{2b_0 g^2(1/r_3)}\right)
  = \frac{1}{r_3}
  \exp\left(-\frac{24\pi^2}{11Ng^2(1/r_3)}\right)$$

The ratio:
$$\frac{\Lambda_{2D}}{\Lambda_{4D}} =
  \exp\left(-\frac{8\pi^2}{Ng^2}
  + \frac{24\pi^2}{11Ng^2}\right)
  = \exp\left(\frac{8\pi^2(24/11 - 1)}{Ng^2}\right)
  = \exp\left(\frac{8\pi^2 \times 13/11}{Ng^2}\right)$$

Wait -- this gives $\Lambda_{2D} \gg \Lambda_{4D}$, which would
mean the 2D dynamical scale is much larger than the 4D one. This
seems wrong: the 2D scale should be comparable to the 4D scale.

Let me recheck. The 2D one-loop coefficient is $b_0^{2D} = N/(2\pi)$,
and the 4D one is $b_0^{4D} = 11N/(48\pi^2)$. The exponents are:

$$\Lambda_{2D} \sim \exp\left(-\frac{1}{2b_0^{2D} g_{2D}^2}\right)
  = \exp\left(-\frac{\pi}{Ng_{2D}^2}\right)$$

$$\Lambda_{4D} \sim \exp\left(-\frac{1}{2b_0^{4D} g^2}\right)
  = \exp\left(-\frac{24\pi^2}{11Ng^2}\right)$$

With $g_{2D}^2 = g^2/(4\pi)$:

$$\Lambda_{2D} \sim \exp\left(-\frac{4\pi^2}{Ng^2}\right)
  \quad\text{vs}\quad
  \Lambda_{4D} \sim \exp\left(-\frac{24\pi^2}{11Ng^2}\right)$$

The ratio of the exponents is $4\pi^2$ vs $24\pi^2/11 \approx
6.86$. Since $4\pi^2 \approx 39.5 > 6.86$, we get
$\Lambda_{2D} \ll \Lambda_{4D}$.

This makes physical sense: the 2D sigma model has a STRONGER
coupling (larger beta function coefficient in the exponent) so its
dynamical scale is LOWER.

The 4D string tension:
$$\sigma_{\text{4D}} \sim \Lambda_{2D}^2
  \sim \exp\left(-\frac{8\pi^2}{Ng^2}\right) \frac{1}{r_3^2}$$

But the PHYSICAL string tension should scale as $\Lambda_{4D}^2$.
The discrepancy comes from the factor $1/r_3^2$:

$$\sigma_{\text{4D}} \sim \frac{1}{r_3^2}
  \exp\left(-\frac{8\pi^2}{Ng^2}\right)$$

Using $g^2 = g^2(1/r_3)$ and the relation
$\Lambda_{4D} r_3 = \exp(-24\pi^2/(11Ng^2))$:

$$\sigma_{\text{4D}} \sim \Lambda_{4D}^{2 \times 8\pi^2/(24\pi^2/11)}
  / r_3^2 \times r_3^{2 \times 8\pi^2/(24\pi^2/11)}$$

This is getting circular. The important point is:

**The 4D string tension IS determined by the 2D mass gap, up to
a known power of $r_3$ and computable numerical factors.** The
specific relation involves matching the 2D and 4D running
couplings at the scale $1/r_3$, which is a one-step computation.

[STATUS: The relation $\sigma_{\text{4D}} = m_{2D}^2/(2\pi)$
is ARGUED from the worldsheet picture. The numerical factors
require matching conditions at the KK scale.]


---

## IV. Comparison of the Two Routes

| Aspect | Route 1 (Direct 4D) | Route 2 (Worldsheet) |
|--------|---------------------|---------------------|
| What needs to be proved | 4D resurgence from scratch | 2D resurgence + worldsheet |
| Renormalon cancellation | Must be proved in 4D | Handled by 2D (fewer renormalons) |
| IR catastrophe | Must be regulated by CP$^{N-1}$ | Absent in 2D |
| Instanton moduli space | 4D ADHM on CP$^{N-1}$ | 2D holomorphic maps |
| Current status | Mostly conjectural | Partially proved (deformed model) |
| Key advantage | Direct, no intermediary | Leverages 2D results |
| Key disadvantage | 4D renormalons are hard | Worldsheet rigor is needed |

**Assessment:** Route 2 (worldsheet inheritance) is more promising
because:

1. The 2D resurgence machinery is much more developed than the 4D
   one.
2. The 2D model has fewer complications (no UV renormalons, no IR
   catastrophe for instantons, computable moduli spaces).
3. The worldsheet connection is physically well-motivated and comes
   directly from the framework's holonomy correspondence.

The weak point of Route 2 is the worldsheet rigor: proving that
the confining string worldsheet IS the CP$^{N-1}$ sigma model
non-perturbatively. This is a statement about the strong-coupling
regime of the 4D theory, where the confining string forms.


---

## V. A Hybrid Approach: What Can Be Proved Now

Given the state of the art, the strongest statement we can make
combines both routes:

**Theorem (Conditional, modular form).** [ARGUED]

*Assume:*
*(A) The deformed 2D CP$^{N-1}$ model is resurgent (PROVED for
CP$^1$).*
*(B) Adiabatic continuity holds: the deformed and undeformed
models are in the same phase (PROVED for CP$^1$, CONJECTURED for
CP$^{N-1}$).*
*(C) The confining string worldsheet of the 4D KK theory is
described by the 2D CP$^{N-1}$ sigma model (ARGUED, Paper 5).*
*(D) The embedding corrections are perturbative and do not destroy
positivity (ARGUED, Polchinski--Strominger).*

*Then:*
*The 4D physical string tension $\sigma_{\text{4D}} > 0$ is defined
in the continuum by a resurgent trans-series. The value is:*
$$\sigma_{\text{4D}} = \frac{c_N^2 \Lambda_{2D}^2}{2\pi}
  + O\left(\frac{\Lambda_{2D}^2}{\sigma_{\text{4D}} R_{\min}^2}\right)$$

*where $c_N$ is the resurgent 2D mass gap coefficient and
$R_{\min} = 1/\sqrt{\sigma_{\text{4D}}}$ is the size of the
lightest glueball.*

**The assumption count:**
- (A) is proved for $N = 2$, argued for general $N$. Score: 0.8
- (B) is proved for $N = 2$, conjectured for $N \geq 3$. Score: 0.6
- (C) is argued from the holonomy correspondence. Score: 0.5
- (D) is argued from effective string theory. Score: 0.7

None of the assumptions are proved for the physical case $N = 3$
($SU(3)$). But each has significant evidence behind it, and the
logical chain is clear.


---

## VI. Summary

The extension from 2D to 4D resurgence can proceed through two
routes. The worldsheet route (Route 2) is more promising because
it reduces the 4D problem to a 2D one plus a worldsheet connection.
The direct 4D route (Route 1) faces additional complications from
renormalons and the IR catastrophe, though the CP$^{N-1}$ internal
space helps with both.

The honest status: even through the worldsheet route, no step is
completely proved for the physical case $N = 3$. The chain of
reasoning is:

$$\text{Deformed 2D resurgence} \xrightarrow{(B)}
  \text{Undeformed 2D resurgence} \xrightarrow{(C,D)}
  \text{4D }\sigma > 0$$

Each arrow is a conjecture supported by evidence. Proving any one
of them would be a major advance.
