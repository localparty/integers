# Appendix G: The Gauge Field Laplacian on CP2

We analyze the spectrum of the gauge field Laplacian (the operator
governing small fluctuations of the connection) on $\mathbb{CP}^2$.
This provides an independent argument for the mass gap through the
Weitzenb\"ock formula.

**Convention note ($N$-dependence).** Throughout this appendix we
specialize to $\mathbb{CP}^{N-1}$ with $N = 3$, i.e., $\mathbb{CP}^2$.
For general $N \geq 2$ the Ricci tensor is
$\text{Ric} = (2N/r_3^2)\, g$, the Weitzenb\"ock lower bound is
$\mu_1 \geq 2N/r_3^2$, and the actual first eigenvalue
(Ikeda--Taniguchi 1978) is $\mu_{\min}^{(1)} = 4N/r_3^2$ with
$m_1 = 2\sqrt{N}/r_3$. The values $6/r_3^2$, $12/r_3^2$, and
$2\sqrt{3}/r_3$ appearing below are the $N = 3$ substitutions of
these general formulas. See Theorem 1 of \S 02 for the general-$N$
statement.


## G.1 The Operator

On a Riemannian manifold $(M, g)$, the linearized Yang--Mills equation
around the trivial connection $A = 0$ is:
$$\nabla^* \nabla \, a + \text{Ric}(a) = -\lambda \, a$$

where $a \in \Omega^1(M, \text{ad}\,P)$ is a connection one-form
perturbation, $\nabla^*\nabla$ is the connection Laplacian (or rough
Laplacian), and $\text{Ric}(a)$ is the Ricci curvature acting on
one-forms via the Weitzenb\"ock formula:
$$\Delta_{\text{Hodge}} \, a = \nabla^*\nabla \, a + \text{Ric}(a)$$

Here $\Delta_{\text{Hodge}} = (d + d^*)^2$ is the Hodge Laplacian on
one-forms.


## G.2 The Weitzenb\"ock Formula on CP2

For $\mathbb{CP}^{N-1}$ with the Fubini--Study metric, the Ricci tensor
is:
$$\text{Ric}_{ab} = \frac{2N}{r_3^2} g_{ab}
  \qquad \bigl(= \tfrac{6}{r_3^2}\ \text{for}\ N = 3\bigr)$$

(Einstein manifold with positive Ricci curvature). Acting on one-forms:
$$\text{Ric}(a)_b = \text{Ric}_{ab} \, a^a = \frac{2N}{r_3^2} a_b
  \qquad \bigl(= \tfrac{6}{r_3^2}\, a_b\ \text{for}\ N = 3\bigr)$$

Therefore the Weitzenb\"ock formula gives:
$$\Delta_{\text{Hodge}} \, a = \nabla^*\nabla \, a
  + \frac{2N}{r_3^2} a \qquad \bigl(= \nabla^*\nabla\, a +
  \tfrac{6}{r_3^2}\, a\ \text{for}\ N = 3\bigr)$$

Since $\nabla^*\nabla \geq 0$ (the connection Laplacian is
non-negative):
$$\Delta_{\text{Hodge}} \, a \geq \frac{2N}{r_3^2} a
  \qquad \bigl(= \tfrac{6}{r_3^2}\, a\ \text{for}\ N = 3\bigr)$$

**This means every eigenvalue of the Hodge Laplacian on one-forms is at
least $2N/r_3^2$ (which is $6/r_3^2$ for $N = 3$).**


## G.3 Consequences for the Gauge Field Spectrum

The eigenvalues of $\Delta_{\text{Hodge}}$ on one-forms on
$\mathbb{CP}^{N-1}$ satisfy:
$$\mu_n \geq \frac{2N}{r_3^2}\ \bigl(= \tfrac{6}{r_3^2}\ \text{for}\
  N = 3\bigr) \quad \text{for all } n \geq 1$$

(There are no harmonic one-forms on $\mathbb{CP}^{N-1}$ since
$H^1(\mathbb{CP}^{N-1}) = 0$, so the zero eigenvalue is absent.)

**Physical interpretation.** In the KK reduction, the eigenvalues $\mu_n$
correspond to masses-squared of 4D vector fields (KK excitations of the
gauge field). The bound $\mu_1 \geq 2N/r_3^2$ (i.e., $6/r_3^2$ for
$N = 3$) means all such excitations have mass at least
$\sqrt{2N}/r_3 \sim M_{\text{KK}}$.

**But the gauge zero modes are different.** The massless 4D gluons do
not come from harmonic one-forms on $\mathbb{CP}^2$ (there are none).
They come from Killing vector fields --- one-forms $K_I$ satisfying
$\nabla_{(a} K_{b)} = 0$, which are in the kernel of a *different*
operator (the Killing equation, not the Hodge Laplacian).

This distinction is important: the Killing vectors are zero modes of the
isometry operator, not of the Hodge Laplacian. Their 4D descendants (the
gluons) are classically massless but acquire a mass gap through the
non-perturbative mechanism of Section 4.5 (confinement from CP$^2$
topology).


## G.4 The Complementary Argument

The Weitzenb\"ock analysis provides a complementary perspective on the
mass gap, distinct from the topological argument of Section 4.5:

**Topological argument (Section 4.5):**
$$H_2(\mathbb{CP}^2) = \mathbb{Z} \;\to\; \text{area law}
  \;\to\; \sigma > 0 \;\to\; \Delta > 0$$

**Spectral argument (this appendix):**
$$\text{Ric} > 0 \;\to\; \text{no harmonic 1-forms}
  \;\to\; H^1 = 0 \;\to\; \text{no massless vector modes}$$

The spectral argument shows that the *only* massless vectors in the
KK reduction are the Killing vectors (gauge bosons). There are no
additional massless vector fields that could provide gapless excitations.
The gauge bosons themselves acquire a mass gap through confinement.

**Together:** The Weitzenb\"ock formula ensures there are no
"accidental" massless modes that could close the gap from above, while
the topological argument ensures the gap is opened from below. The two
arguments are complementary and independent.


## G.5 The Full Spectrum of One-Forms on CP2

For completeness, the eigenvalues of the Hodge Laplacian on one-forms
on $\mathbb{CP}^2$ (Fubini--Study metric, radius $r_3$) are:

$$\mu_{p,q}^{(1)} = \frac{4}{r_3^2}\left[p(p+2) + q(q+2) + pq
  + \text{(spin correction)}\right]$$

The explicit spectrum starts at (Ikeda--Taniguchi 1978):
$$\mu_{\min}^{(1)} = \frac{4N}{r_3^2}
  \qquad \bigl(= \tfrac{12}{r_3^2}\ \text{for}\ N = 3\bigr)$$

(For $N = 3$ this corresponds to one-forms in the
$(\mathbf{3}, \mathbf{1})$ or $(\mathbf{1}, \mathbf{\bar{3}})$
representation of $SU(3)$.) This exceeds the Weitzenb\"ock lower bound
of $2N/r_3^2$ by a factor of 2, as expected for K\"ahler manifolds
where the bound is typically not saturated (the standard
$(1,0) \oplus (0,1)$ "extra factor of 2").

**Mass of the lightest KK vector:**
$$m_{\text{KK vector}} = \frac{\sqrt{4N}}{r_3}
  = \frac{2\sqrt{N}}{r_3}
  \qquad \bigl(= \tfrac{\sqrt{12}}{r_3} = \tfrac{2\sqrt{3}}{r_3}
  \approx 3.46\, M_{\text{KK}}\ \text{for}\ N = 3\bigr)$$

This is well above the confinement scale $\Lambda_{\text{QCD}}$ (by a
factor of $\sim 10^{12}$), confirming that the KK vector modes are
completely decoupled from the low-energy Yang--Mills dynamics.


## G.6 Why This Matters for the Proof

The Weitzenb\"ock argument closes a potential loophole in the mass gap
proof. One might worry: "What if the KK reduction produces unexpected
massless modes that provide gapless excitations in 4D?"

The answer is no:
- Massless scalars: controlled by the scalar Laplacian. The only zero
  mode is the constant ($\lambda_0 = 0$), which is the volume modulus.
  All other modes have $\lambda \geq 12/r_3^2$ (Appendix A).
- Massless vectors: controlled by the Hodge Laplacian on one-forms.
  $H^1(\mathbb{CP}^{N-1}) = 0$ means no harmonic one-forms. All
  one-form modes have $\mu \geq 2N/r_3^2$ ($= 6/r_3^2$ for $N = 3$).
  The only massless vectors are the 8 Killing vectors (gluons, in the
  $N = 3$ case), which are massless at tree level but confined at the
  quantum level.
- Massless spinors: controlled by the Dirac operator. On
  $\mathbb{CP}^2$ with Fubini--Study metric, the Dirac operator has
  no zero modes (related to the non-spin structure and the
  Atiyah--Singer index theorem). All spinor modes are massive.

The KK reduction on $\mathbb{CP}^2$ produces exactly the expected
field content: 8 massless gluons (which confine) plus a tower of massive
KK modes (which decouple). No unexpected massless modes can close the
gap.
