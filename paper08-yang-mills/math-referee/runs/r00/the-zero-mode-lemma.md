# The Zero-Mode Lemma: A Deep Investigation

All roads in this proof converge to a single statement. This document
attempts to prove it by four approaches, and gives an honest verdict
on each.

---

## 0. The Statement (Two Equivalent Forms)

**Form A (Operator identity).** In Balaban's effective action
decomposition at RG step $k$,

$$S_k = \mathcal{E}_0^{(k)} V + \frac{1}{g_k^2}\,S_{\mathrm{YM}}
  + \sum_x E_k(x),$$

the total irrelevant remainder satisfies

$$\hat{E}_k(0) \;=\; \sum_{x \in \Lambda_k} E_k(x)[U] \;=\; 0$$

for EVERY gauge field configuration $U$ on $\Lambda_k$.

**Form B (Propagator regularity).** The connected propagator
restricted to a polymer $X$ satisfies

$$|G_c^X(0,x)| \;\leq\; C\,\hat{\Delta}\,e^{-\Delta\,d(0,x)}$$

with an EXTRA factor of $\hat{\Delta} = a\Delta$ compared to the
naive bound $|G_c^X| \leq C\,e^{-\Delta\,d(0,x)}$.

**Why they are linked.** Form A, combined with the already-proved
first-moment vanishing $\sum_x x_\mu E_k(x) = 0$, gives the
double-derivative representation $E_k = \nabla^*\nabla^* h$ (Lemma
4.1 of path-1b). Integration by parts then transfers two derivatives
to the propagator, producing $\hat{\Delta}^2$ suppression in the
boundary terms. Alternatively, Form B applied to the boundary terms
of the polymer summation-by-parts directly gives the missing
$\hat{\Delta}$ factor (Section 6.3 of path-1a). Either way, the
form factor bound $|f_c(0)| \leq C g_k^4 (a_k\Delta)^2 \Delta^3$
follows, and the proof closes.

The question is: is either form TRUE?

---

## 1. Approach 1: Prove Form A from Balaban's Construction

### 1.1 The three possible definitions of $\mathcal{E}_0$

Balaban's block-spin RG at step $k$ produces an effective action
$S_k[U]$ by integrating out fluctuation fields. The decomposition
into "vacuum energy + YM action + remainder" requires a CHOICE of
how to define each piece. The definition of $\mathcal{E}_0$ is the
critical choice.

**Possibility 1: $\mathcal{E}_0$ defined by evaluation at $U = \mathbf{1}$.**

Set $\mathcal{E}_0 V = S_k[U=\mathbf{1}] - \frac{1}{g_k^2}
S_{\mathrm{YM}}[\mathbf{1}]$. Since $S_{\mathrm{YM}}[\mathbf{1}] = 0$
(all plaquettes are identity), this gives $\mathcal{E}_0 V =
S_k[\mathbf{1}]$. The remainder is then:

$$\sum_x E_k(x)[U] = S_k[U] - S_k[\mathbf{1}]
  - \frac{1}{g_k^2}\bigl(S_{\mathrm{YM}}[U] - 0\bigr)$$

At $U = \mathbf{1}$: $\sum_x E_k(x)[\mathbf{1}] = 0$ by construction.
But for general $U$: $\sum_x E_k(x)[U] \neq 0$ because the effective
action $S_k[U]$ is a nonlinear functional of $U$ whose deviation from
$S_k[\mathbf{1}]$ is not captured entirely by $S_{\mathrm{YM}}[U]$.

Specifically, $S_k[U] - S_k[\mathbf{1}]$ has a term proportional to
$S_{\mathrm{YM}}[U]$ (absorbed into $1/g_k^2$), but also terms
proportional to $\mathrm{Tr}\,F^3$, $\mathrm{Tr}(DF)^2$, etc. The
spatial integral of these nonlinear terms is nonzero for generic $U$.

**Verdict on Possibility 1:** Gives $E_k[\mathbf{1}] = 0$ pointwise,
but NOT the operator identity $\sum_x E_k(x) = 0$ for all $U$.

**Possibility 2: $\mathcal{E}_0$ defined by functional averaging.**

Set $\mathcal{E}_0 V = \langle S_k[U] - \frac{1}{g_k^2}
S_{\mathrm{YM}}[U] \rangle$, where $\langle\cdot\rangle$ is the
expectation in the full theory at scale $k$. Then
$\langle\sum_x E_k(x)\rangle = 0$ (in expectation), but for any
specific configuration $U$, the sum $\sum_x E_k(x)[U]$ is a
fluctuating random variable with zero mean but nonzero variance.

**Verdict on Possibility 2:** Gives $\langle\hat{E}_k(0)\rangle = 0$,
an expectation, not the operator identity.

**Possibility 3: $\mathcal{E}_0$ defined as a field-dependent spatial
average.**

Set $\mathcal{E}_0[U] = \frac{1}{V}\sum_x \bigl[S_k(x)[U] -
\frac{1}{g_k^2} s_{\mathrm{YM}}(x)[U]\bigr]$, where
$S_k(x)$ and $s_{\mathrm{YM}}(x)$ are the local action densities.
Then:

$$E_k(x)[U] = \bigl[S_k(x) - \tfrac{1}{g_k^2}s_{\mathrm{YM}}(x)\bigr]
  - \mathcal{E}_0[U]$$

and $\sum_x E_k(x)[U] = 0$ identically, for every $U$. Form A holds
by construction.

**But there is a problem.** Under this definition, $\mathcal{E}_0[U]$
is not a constant -- it is a FUNCTIONAL of $U$. It is the spatial
average of the local irrelevant density, and it varies from
configuration to configuration. This means $\mathcal{E}_0[U] \cdot V$
is not the vacuum energy (a number); it is an additional term in the
effective action.

### 1.2 Analysis of Possibility 3

Write $\mathcal{E}_0[U] = \overline{E}[U]$ (the spatial average of
the remainder density). Decompose:

$$\overline{E}[U] = \langle\overline{E}\rangle
  + \delta\overline{E}[U]$$

where $\langle\overline{E}\rangle$ is the true vacuum energy density
(a number) and $\delta\overline{E}[U]$ is the fluctuation of the
spatial average.

The fluctuation satisfies: $|\delta\overline{E}[U]| \leq
C g_k^4$ (from Balaban's bound $|E_k(x)| \leq C g_k^4$). But more
importantly, $\delta\overline{E}[U]$ is a SPATIALLY UNIFORM functional
of $U$ (it takes the same value at every lattice site). It depends on
$U$ only through global (volume-averaged) quantities.

**Question:** Can a spatially uniform functional of $U$ be absorbed
into the coupling constant renormalization?

The Yang-Mills action has the form $S_{\mathrm{YM}}[U] =
\frac{1}{g^2}\sum_P (1 - \frac{1}{N}\mathrm{Re\,Tr}\,U_P)$.
The spatial average of the action density is
$\bar{s}_{\mathrm{YM}} = \frac{1}{V}\sum_P s_P$. If
$\delta\overline{E}[U]$ were proportional to $\bar{s}_{\mathrm{YM}}$,
it could be absorbed into a field-dependent redefinition of $g_k$.
But $\delta\overline{E}[U]$ is a NONLINEAR functional of the
plaquette variables, not proportional to $\bar{s}_{\mathrm{YM}}$.

The spatially uniform part $\delta\overline{E}[U]$ contains:
- A piece $\propto \bar{s}_{\mathrm{YM}}$ (absorbable into $g_k^2$)
- A piece $\propto \frac{1}{V}\sum_x \mathrm{Tr}F^3(x)$ (NOT absorbable)
- Higher nonlinearities in the volume-averaged field strength

These non-absorbable pieces are $O(g_k^4)$ and are spatially uniform,
so they contribute to $\sum_x E_k(x)$ a term that is $O(g_k^4 \cdot V)$,
not zero.

**Verdict on Possibility 3:** The construction forces $\sum_x E_k(x) = 0$
but at the cost of making $\mathcal{E}_0$ field-dependent, which
transfers the problem elsewhere. The "vacuum energy" is no longer a
vacuum energy. It becomes part of the effective action and must be
tracked through the RG. This does not simplify the problem; it
merely relabels it.

### 1.3 What Balaban actually does

In Balaban's papers (CMP 109, 1987; CMP 119, 1988), the effective
action is written as a sum of polymer activities. The "vacuum energy"
$\mathcal{E}_0$ is the free energy density of the FREE FIELD (Gaussian)
part of the block-spin integration, computed at each step. It is a
NUMERICAL CONSTANT (depending on $g_k$ and the lattice structure, but
NOT on the gauge field configuration $U$). This corresponds most
closely to Possibility 1, evaluated not at $U = \mathbf{1}$ but at
the Gaussian saddle point.

In Balaban's framework, after subtracting the vacuum energy (a
number) and the Yang-Mills term (identified by its leading Taylor
coefficient in the field strength), the remainder $E_k$ is whatever
is left. This remainder, summed over all sites, equals the total
effective action minus the classified terms:

$$\sum_x E_k(x)[U] = S_k[U] - \mathcal{E}_0 V
  - \frac{1}{g_k^2} S_{\mathrm{YM}}[U]$$

For this to vanish for all $U$, one would need $S_k[U] =
\mathcal{E}_0 V + \frac{1}{g_k^2} S_{\mathrm{YM}}[U]$ for every $U$.
That is: the effective action at step $k$ would need to be EXACTLY
the Yang-Mills action (with renormalized coupling) plus a constant.
No irrelevant operators at all.

But Balaban explicitly proves that irrelevant operators ARE present
with coefficients $c_n = O(g_k^{d_n - 4})$. Their spatial integral
is generically nonzero.

### 1.4 Conclusion of Approach 1

**Form A is FALSE as an operator identity.** The spatial integral
$\sum_x E_k(x)[U]$ is a nontrivial gauge-invariant functional of $U$,
equal to the total irrelevant part of the effective action. It vanishes
in the vacuum ($U = \mathbf{1}$ or thermal average), but not for
arbitrary gauge field configurations.

This conclusion is forced by the internal logic: Balaban's decomposition
produces genuine irrelevant operators (dimension 6, 8, ...) whose
spatial integrals are nonzero gauge-invariant functionals (e.g.,
$c_6 \sum_x \mathrm{Tr}(DF)^2(x)$ is proportional to the total
"derivative energy," which is nonzero for nontrivial configurations).

The earlier claim in 52-power-counting-lemma-rigorous.md that
"$\hat{O}_6(0) = 0$ is the DEFINITION of the irrelevant operator in
Balaban's decomposition" conflates two distinct things: (i) the
subtraction of the VACUUM EXPECTATION VALUE $\langle\hat{E}_k(0)\rangle$
(which IS part of Balaban's definition), and (ii) the operator identity
$\hat{E}_k(0) = 0$ for all configurations (which is NOT).

---

## 2. Approach 2: The Block-Spin Free Energy Argument

### 2.1 Setup

The block-spin transformation maps the fine-lattice action $S_{k-1}$
on $\Lambda_{k-1}$ to the coarse-lattice effective action $S_k$ on
$\Lambda_k$:

$$e^{-S_k[V]} = \int \mathcal{D}U_{\mathrm{fine}}\;
  e^{-S_{k-1}[U]}\;\delta\bigl(V - \mathrm{Block}(U)\bigr)$$

Therefore:

$$S_k[V] = -\ln Z_k(V)$$

where $Z_k(V) = \int \mathcal{D}U\,e^{-S_{k-1}[U]}\,
\delta(V - \mathrm{Block}(U))$ is the CONDITIONED partition function.

### 2.2 The free energy difference

Define $\mathcal{E}_0 = \frac{1}{V} S_k[\mathbf{1}]$. Then:

$$\sum_x E_k(x)[V] = S_k[V] - \mathcal{E}_0 V
  - \frac{1}{g_k^2} S_{\mathrm{YM}}[V]$$

$$= \bigl[-\ln Z_k(V)\bigr] - \bigl[-\ln Z_k(\mathbf{1})\bigr]
  - \frac{1}{g_k^2} S_{\mathrm{YM}}[V]$$

$$= -\ln\frac{Z_k(V)}{Z_k(\mathbf{1})}
  - \frac{1}{g_k^2} S_{\mathrm{YM}}[V]$$

This is the FREE ENERGY DIFFERENCE between the block field $V$ and the
trivial field, minus the classical Yang-Mills contribution.

### 2.3 Structure of the free energy difference

At one loop (Gaussian integration):

$$-\ln\frac{Z_k(V)}{Z_k(\mathbf{1})} = \frac{1}{g_k^2}S_{\mathrm{YM}}[V]
  + \frac{1}{2}\mathrm{Tr}\ln\frac{-D^2[V] + m_W^2}{-\partial^2 + m_W^2}
  + O(g_k^4 \cdot V)$$

The first term is the classical Yang-Mills action (absorbed into
$1/g_k^2$ renormalization). The second term is the one-loop
determinant ratio. Subtracting:

$$\sum_x E_k(x)[V] = \frac{1}{2}\mathrm{Tr}\ln
  \frac{-D^2[V] + m_W^2}{-\partial^2 + m_W^2} + O(g_k^4 \cdot V)$$

The one-loop determinant is the logarithm of the ratio of functional
determinants. It is a nontrivial functional of $V$:

$$\frac{1}{2}\mathrm{Tr}\ln\frac{-D^2[V]}{-\partial^2}
  = \frac{1}{2}\mathrm{Tr}\ln\bigl(\mathbf{1}
  + (-\partial^2)^{-1}[A \cdot \partial + \partial \cdot A + A^2]\bigr)$$

$$= \frac{1}{2}\mathrm{Tr}\bigl[(-\partial^2)^{-1}(2A\cdot\partial + A^2)\bigr]
  - \frac{1}{4}\mathrm{Tr}\bigl[(-\partial^2)^{-1}(2A\cdot\partial)\bigr]^2
  + \ldots$$

The first term (linear in $A^2$) contributes a shift to $1/g_k^2$
(coupling renormalization). The second term (quartic in $A$, or
quadratic in $F$) also shifts $1/g_k^2$. After coupling
renormalization, the remaining terms begin at $O(F^3)$:

$$\sum_x E_k(x)[V]\Big|_{\text{1-loop, renormalized}}
  \sim c_6 \sum_x \mathrm{Tr}(DF)^2(x) + O(F^3)$$

This is NOT zero for general $V$. The one-loop determinant, after
subtracting the coupling renormalization, leaves genuine dimension-6
and higher contributions.

### 2.4 Quantitative estimate

For a slowly varying field $V$ with $|F| \sim f$ (a small field
strength), the one-loop remainder scales as:

$$\frac{1}{V}\sum_x E_k(x) \sim c_6\,f^3 + c_8\,f^4 + \ldots$$

where $c_6 \sim g_k^2/(16\pi^2)$ and $c_8 \sim g_k^2/(16\pi^2)^2$.
For $f \sim g_k$ (the typical field strength in Balaban's small-field
region): $\sum_x E_k(x) / V \sim g_k^2 \cdot g_k^3 = g_k^5$. This
is small but NONZERO.

### 2.5 Conclusion of Approach 2

The block-spin free energy argument CONFIRMS that Form A is false.
The spatial integral $\sum_x E_k(x)[V]$ equals the free energy
difference (minus the classical YM part), which is a nontrivial
functional of $V$ starting at the one-loop level.

**Form A cannot be salvaged by any choice of $\mathcal{E}_0$** (short
of making $\mathcal{E}_0$ field-dependent, which is Possibility 3
and merely relabels the problem).

---

## 3. Approach 3: Circumventing Form A

Since Form A is false, the question becomes: can we prove the form
factor bound WITHOUT the operator identity $\sum_x E_k(x) = 0$?

### 3.1 The connected matrix element directly

The quantity we actually need to bound is:

$$f_c(0) = \sum_x \langle 1|E_k(x)|1\rangle_c
  = V \cdot \langle 1|E_k(0)|1\rangle_c$$

(using translation invariance of the zero-momentum state). The
connected matrix element is:

$$\langle 1|E_k(0)|1\rangle_c = \langle 1|E_k(0)|1\rangle
  - \langle 0|E_k(0)|0\rangle$$

Even though $\sum_x E_k(x)[U] \neq 0$ as an operator, it IS true
that:

$$\langle 0|\sum_x E_k(x)|0\rangle = 0$$

(Balaban's vacuum subtraction gives the vacuum expectation correctly).
So the vacuum matrix element of the zero-mode vanishes, but the
one-particle matrix element does not:

$$\langle 1|\sum_x E_k(x)|1\rangle \neq 0$$

The connected form factor is:

$$f_c(0) = \langle 1|\sum_x E_k(x)|1\rangle
  - \langle 0|\sum_x E_k(x)|0\rangle
  = \langle 1|\sum_x E_k(x)|1\rangle$$

(since the vacuum part vanishes by Balaban's subtraction). So we need
to bound the FULL one-particle expectation of the total remainder.

### 3.2 The spectral representation

Insert a complete set of states between $|1\rangle$ and
$\sum_x E_k(x)$. Since $\sum_x E_k(x)$ is the $q = 0$ Fourier mode,
by translation invariance it is diagonal in the momentum basis:

$$\langle n, \vec{p}|\sum_x E_k(x)|m, \vec{p}'\rangle
  = V \cdot \delta_{\vec{p},0}\,\delta_{\vec{p}',0}\,
  \langle n, 0|E_k(0)|m, 0\rangle$$

Therefore:

$$f_c(0) = V \cdot \langle 1,0|E_k(0)|1,0\rangle_c$$

This is a DIAGONAL matrix element of a local operator in the
one-particle state. No off-diagonal transitions, no sum over
intermediate states (beyond the vacuum subtraction).

### 3.3 Dimension and the local matrix element

The local operator $E_k(0)$ is a gauge-invariant polynomial of the
link variables near the origin. Its OPERATOR NORM is bounded:
$\|E_k(0)\| \leq C g_k^4$ (Balaban). A naive bound gives:

$$|f_c(0)| = V \cdot |\langle 1|E_k(0)|1\rangle_c|
  \leq V \cdot C g_k^4$$

This is $O(g_k^4 V)$, which when converted to a mass shift gives
$\delta\hat{\Delta} \leq C g_k^4 V / \hat{\Delta}^3$. For $V = O(1)$
in lattice units, this is $O(g_k^4 / \hat{\Delta}^3)$, which
DIVERGES as $\hat{\Delta} \to 0$. The naive bound is useless.

The suppression must come from the STRUCTURE of $E_k(0)$, not its
norm. Specifically: $E_k(0)$ is an irrelevant operator of dimension
$> 4$, and the one-particle state is a low-momentum state. The
mismatch between the operator's UV character and the state's IR
character should produce the suppression.

### 3.4 The key structural question

Why should $\langle 1|E_k(0)|1\rangle_c$ be suppressed?

**Perturbative answer:** The one-particle state has wave function
$\tilde{\psi}(\vec{k})$ supported at $|\vec{k}| \lesssim \hat{\Delta}$.
The operator $E_k(0)$, written in momentum space, has Fourier
transform $\hat{E}_k(q)$ that vanishes at $q = 0$ to order
$(d_O - 4)$ (by dimensional analysis of the Taylor expansion). The
matrix element is a convolution:

$$\langle 1|E_k(0)|1\rangle = \int\frac{d^3k\,d^3k'}{(2\pi)^6}\;
  \tilde{\psi}^*(\vec{k}')\;\hat{E}_k(\vec{k}' - \vec{k})\;
  \tilde{\psi}(\vec{k})$$

With $|\vec{k}|, |\vec{k}'| \lesssim \hat{\Delta}$, the momentum
transfer satisfies $|\vec{q}| \lesssim 2\hat{\Delta}$.

NOW: the critical input is the behavior of $\hat{E}_k(\vec{q})$
at small $\vec{q}$. If $\hat{E}_k(0) = 0$ (zeroth moment vanishes)
and $\nabla_q\hat{E}_k(0) = 0$ (first moment vanishes, proved by
parity), then $|\hat{E}_k(\vec{q})| \leq C_H g_k^4 |\vec{q}|^2$,
giving:

$$|\langle 1|E_k(0)|1\rangle_c|
  \leq C_H g_k^4 (2\hat{\Delta})^2 \cdot \hat{\Delta}^3 / V
  = O(g_k^4 \hat{\Delta}^5 / V)$$

which yields $|f_c(0)| = O(g_k^4 \hat{\Delta}^5)$ -- the desired
bound.

But if only the first moment vanishes (parity) and NOT the zeroth
(Form A fails), then $|\hat{E}_k(\vec{q})| \leq |\hat{E}_k(0)|
+ C g_k^4 |\vec{q}|$, and the zeroth-mode term
$\hat{E}_k(0) = \sum_x E_k(x)$ contributes:

$$\langle 1|\hat{E}_k(0)|1\rangle = \hat{E}_k(0) \cdot
  |\tilde{\psi}(0)|^2$$

This is the spatial integral of the remainder, evaluated in the
one-particle state. It does NOT vanish, and it is NOT suppressed
by $\hat{\Delta}$.

### 3.5 The vacuum subtraction saves one power but not two

The connected part subtracts the vacuum:

$$f_c(0) = \langle 1|\hat{E}_k(0)|1\rangle
  - \langle 0|\hat{E}_k(0)|0\rangle$$

We know $\langle 0|\hat{E}_k(0)|0\rangle = 0$ (Balaban's vacuum
energy subtraction). So $f_c(0) = \langle 1|\hat{E}_k(0)|1\rangle$.

The one-particle expectation $\langle 1|\hat{E}_k(0)|1\rangle$
measures the total irrelevant action evaluated in the one-particle
state. Physically, this is the self-energy of the glueball from
irrelevant interactions. It is nonzero: the glueball feels the
irrelevant operators because it distorts the local field
configuration away from the vacuum.

However, the one-particle state differs from the vacuum only in a
region of size $\sim 1/\Delta$ (the Compton wavelength). The
distortion is $O(\hat{\Delta}^{3/2})$ in amplitude (from the
wave function normalization in 3D). So:

$$|\langle 1|E_k(x)|1\rangle - \langle 0|E_k(x)|0\rangle|
  \leq C g_k^4 \cdot |\psi_1(x)|^2$$

where $|\psi_1(x)|^2 \sim \hat{\Delta}^3 e^{-2\hat{\Delta}|x|}$
is the glueball density. Summing:

$$|f_c(0)| = \Big|\sum_x [\langle 1|E_k(x)|1\rangle
  - \langle 0|E_k(x)|0\rangle]\Big|
  \leq C g_k^4 \sum_x |\psi_1(x)|^2 = C g_k^4$$

This gives $|f_c(0)| \leq C g_k^4$, with no $\hat{\Delta}$
suppression at all. The sum $\sum_k g_k^4 \sim
\sum 1/(\ln k)^2$ DIVERGES.

**The problem:** the bound $|\langle 1|E_k(x)|1\rangle -
\langle 0|E_k(x)|0\rangle| \leq C g_k^4 |\psi_1(x)|^2$ treats
$E_k$ as a generic bounded operator. It does not use the fact that
$E_k$ is IRRELEVANT (has extra derivatives or momentum-space
structure). The suppression must come from the detailed structure,
not the norm.

### 3.6 What is actually needed

The form factor bound requires something BETWEEN the operator
identity (Form A, which is too strong and false) and the vacuum
expectation (which is too weak). We need:

$$|\langle 1|\hat{E}_k(0)|1\rangle| \leq C g_k^4 \hat{\Delta}^2$$

This is the statement that the zero-mode of the irrelevant remainder,
while nonzero as an operator, has a ONE-PARTICLE MATRIX ELEMENT that
is suppressed by $\hat{\Delta}^2$.

This is exactly the non-perturbative form factor bound (Conjecture 1),
restricted to the zero-mode contribution. And this is what perturbation
theory gives (Theorem 7), but what has not been proved
non-perturbatively.

---

## 4. Approach 4: The Cluster Expansion at the Starting Scale

### 4.1 The key observation

At the starting scale $a_0$ (where the KK cluster expansion converges),
the dimensionless mass gap is $\hat{\Delta}_0 = a_0 \Delta \sim O(1)$.
(The lattice spacing is comparable to the Compton wavelength.) This
means the "suppression factor" $\hat{\Delta}_0^2 \sim O(1)$ is NOT
a suppression at all.

Therefore: at the starting scale, the form factor bound reduces to:

$$|f_c(0)| \leq C g_0^4 \cdot O(1) \cdot \Delta^3$$

which is just the standard cluster expansion bound with no extra
suppression required. The cluster expansion gives $|f_c(0)| \leq
C g_0^4 \Delta_0^3$ (from the connected three-point function),
and since $\hat{\Delta}_0 \sim O(1)$, this is equivalent to
$C g_0^4 \hat{\Delta}_0^2 \Delta_0^3$ up to an $O(1)$ constant.

### 4.2 The preservation argument

If the bound holds at step $k$ with constant $C_k$:

$$|f_c^{(k)}(0)| \leq C_k g_k^4 \hat{\Delta}_k^2 \Delta_k^3$$

then at step $k+1$, the change in the form factor is:

$$|\delta f_c| = |f_c^{(k+1)} - f_c^{(k)}|$$

This change comes from (a) the change in the effective action
($\delta S_k = O(g_k^4)$ per site), (b) the change in the
one-particle state ($|\delta\psi_1| \leq C g_k^4$), and (c) the
change in the mass gap ($|\delta\Delta| \leq C g_k^4 \Delta$).

The change in the form factor from (a) is:

$$|\delta f_c^{(a)}| \leq V \cdot |\langle 1|\delta E_k(0)|1\rangle_c|$$

The operator $\delta E_k(0)$ is the change in the irrelevant
remainder at one RG step. At the LEVEL OF PERTURBATION THEORY,
$\delta E_k$ is given by the one-loop determinant change, which
carries the same derivative structure as $E_k$ itself. The connected
matrix element of $\delta E_k$ is therefore:

$$|\langle 1|\delta E_k(0)|1\rangle_c|
  \leq C g_k^4 \hat{\Delta}_k^2 \cdot \hat{\Delta}_k^3 / V$$

(by the same perturbative argument that gives Theorem 7). So:

$$|\delta f_c^{(a)}| \leq C g_k^4 \hat{\Delta}_k^5
  = C g_k^4 \hat{\Delta}_k^2 \Delta_k^3$$

This is the SAME form as the bound we are trying to preserve. But
is the PERTURBATIVE estimate of $\delta f_c$ valid
non-perturbatively?

### 4.3 The obstacle

The preservation argument at step 4.2 is CIRCULAR in the same way
identified in path-2a (Section VI.3). To bound $\delta f_c^{(a)}$,
we used the perturbative momentum-space structure of $\delta E_k$.
Non-perturbatively, the RG step involves a full functional integral
(not just a Gaussian), and the higher-order contributions to
$\delta E_k$ do not obviously preserve the derivative structure.

Balaban's bounds give $|\delta E_k(x)| \leq C g_k^4$ per site, but
this norm bound does not carry momentum-space information. The
derivative structure (the fact that $\hat{E}_k(q)$ vanishes like
$|q|^2$ at $q = 0$) is a REFINEMENT beyond Balaban's bounds.

### 4.4 A potential resolution: the two-tier structure

Here is the key insight that might break the circularity.

**Tier 1: Balaban gives the norm bound.** At each RG step,
$|E_k(x)| \leq C g_k^4$ per site, and $|\delta E_k(x)| \leq C g_k^4$.
This is proved NON-PERTURBATIVELY.

**Tier 2: Parity gives the first-moment vanishing.** At each step,
$\sum_x x_\mu E_k(x) = 0$. This is proved NON-PERTURBATIVELY
(from the exact parity symmetry of the lattice theory).

**Tier 3 (the gap): Vacuum subtraction gives only the expectation.**
Balaban's subtraction gives $\langle 0|\hat{E}_k(0)|0\rangle = 0$,
but NOT $\hat{E}_k(0) = 0$.

Now consider: can we prove the WEAKER statement

$$|\langle 1|\hat{E}_k(0)|1\rangle| \leq C g_k^4 \hat{\Delta}^2$$

directly, without proving the operator identity?

### 4.5 The spatial clustering argument

The one-particle state $|1,\vec{p}=0\rangle$ is a DELOCALIZED state
(spread over all of space). Its local density is $|\psi_1(x)|^2 \sim
\hat{\Delta}^3$. But the CONNECTED part of the matrix element is
sensitive to the way the one-particle state differs from the vacuum.

In the path integral representation:

$$\langle 1|E_k(0)|1\rangle_c
  = \sum_z \int_0^\infty dT\;e^{\Delta T}\;
  \langle\phi(z,T)\,E_k(0,0)\,\phi(0,0)\rangle_c$$

where $\phi$ creates the glueball and $T$ is the Euclidean time.
The connected three-point function $\langle\phi\,E_k\,\phi\rangle_c$
requires all three points to be connected by a cluster.

In the KK cluster expansion (at the starting scale), clusters
connecting $z$, $0$, and $(0,T)$ have size at least $|z| + T$.
The cluster weight decays as $e^{-\alpha(|z|+T)}$. The time integral
gives a factor $1/(\alpha - \Delta) \sim 1/\hat{\Delta}$ (with $\alpha
\sim m_W \sim O(1)$ and $\Delta \sim \hat{\Delta}/a$). The spatial
sum gives $\sum_z e^{-\alpha|z|} \leq C/\hat{\Delta}^3$ (at the
starting scale where $\hat{\Delta} \sim O(1)$, this is $O(1)$).

At the starting scale ($\hat{\Delta} \sim O(1)$):
$$|f_c(0)| \leq C g_0^4 \cdot O(1) = C g_0^4 \hat{\Delta}_0^2
  \cdot O(1/\hat{\Delta}_0^2)$$

Since $\hat{\Delta}_0 \sim O(1)$, the factors $\hat{\Delta}_0^2$ and
$1/\hat{\Delta}_0^2$ are both $O(1)$, and the bound is trivially
satisfied.

**The nontrivial content appears only at finer scales** ($k > 0$,
$\hat{\Delta}_k \ll 1$), where the cluster expansion is no longer
directly available and one must rely on the RG.

### 4.6 Why the starting scale argument cannot propagate

The cluster expansion at scale $a_0$ gives explicit control of
three-point functions. But at scales $a_k = 2^{-k} a_0$ ($k > 0$),
the theory is described by Balaban's effective action, not the
original lattice action. The cluster expansion at the starting scale
has been "integrated out" -- its information is encoded in the
effective action coefficients and the polymer activities.

To propagate the form factor bound through the RG requires tracking
a three-point function (not just the partition function) through
Balaban's multi-scale expansion. This is the "50-100 page paper"
identified in path-2a (Section VII.5, Path A) and in the open problem
statement (10-open-problem.md, Path (a)).

### 4.7 Conclusion of Approach 4

At the starting scale, the form factor bound is trivially satisfied
because $\hat{\Delta}_0 \sim O(1)$. The nontrivial content is the
PRESERVATION through the RG, which requires extending Balaban's
framework from the partition function to three-point functions. This
is feasible but constitutes a genuine piece of new mathematical work
beyond what currently exists.

---

## 5. What Precisely Prevents a Proof

### 5.1 The logical structure

The proof chain is:

1. KK cluster expansion $\Rightarrow$ $\Delta_0 > 0$ **[PROVED]**
2. Balaban UV stability $\Rightarrow$ $|E_k| \leq C g_k^4$ **[PROVED]**
3. Parity $\Rightarrow$ $\sum_x x_\mu E_k(x) = 0$ **[PROVED]**
4. ??? $\Rightarrow$ $|\langle 1|\hat{E}_k(0)|1\rangle|
   \leq C g_k^4 \hat{\Delta}^2$ **[OPEN]**
5. (3) + (4) $\Rightarrow$ $|\hat{E}_k(q)| \leq C g_k^4 |q|^2$ in
   one-particle matrix elements **[CONDITIONAL on 4]**
6. (5) $\Rightarrow$ $|f_c(0)| \leq C g_k^4 (a\Delta)^2 \Delta^3$
   **[CONDITIONAL on 4]**
7. (2) + (6) $\Rightarrow$ $\sum_k |\delta\Delta_k/\Delta_k| < \infty$
   **[CONDITIONAL on 4]**
8. (1) + (7) $\Rightarrow$ $\Delta_\infty > 0$ **[CONDITIONAL on 4]**

Step 4 is the gap. Note that (4) is WEAKER than Form A: we do not
need the operator identity $\hat{E}_k(0) = 0$ for all configurations.
We need only that its one-particle MATRIX ELEMENT is suppressed by
$\hat{\Delta}^2$.

### 5.2 Restatement of the gap as a precise mathematical problem

**Problem.** Let $T$ be the transfer matrix of $\mathrm{SU}(N)$
lattice gauge theory at coupling $g^2$, with spectral gap
$\hat{\Delta} = -\ln(E_1/E_0)$ where $E_0 > E_1$ are the two
largest eigenvalues. Let $E_k$ be the irrelevant part of Balaban's
effective action at RG step $k$, satisfying $\|E_k\|_\infty \leq
C g_k^4$ per site. Let $|1\rangle$ be the eigenstate corresponding
to $E_1$ at zero spatial momentum.

Prove: $|\langle 1|\sum_x E_k(x)|1\rangle| \leq C g_k^4 \hat{\Delta}^2$.

**What is known:**

- $\langle 0|\sum_x E_k(x)|0\rangle = 0$ (Balaban's vacuum
  subtraction).
- $\sum_x x_\mu E_k(x) = 0$ as an operator identity (parity).
- $\|E_k(x)\| \leq C g_k^4$ per site (Balaban).
- The perturbative computation gives
  $\langle 1|\sum_x E_k(x)|1\rangle = O(g_k^4 \hat{\Delta}^2)$
  to all orders, with $O(e^{-8\pi^2/g^2})$ corrections (Theorem 7).

**What is NOT known:**

- Whether the non-perturbative contributions (beyond all orders in
  $g^2$) respect the $\hat{\Delta}^2$ suppression.
- Whether the dimensional structure of $E_k$ (as an irrelevant
  operator) translates to suppressed matrix elements without
  the operator identity $\hat{E}_k(0) = 0$.

### 5.3 The nature of the obstruction

The obstruction is NOT conceptual but TECHNICAL. Specifically:

**(i) The operator $\hat{E}_k(0) = \sum_x E_k(x)$ is a zero-momentum
gauge-invariant functional.** It is bounded ($O(g_k^4 V)$), vanishes
in vacuum expectation, and has the structure of a sum of irrelevant
terms. Its matrix element between one-particle states should be
suppressed because the one-particle state is a long-wavelength
excitation and irrelevant operators couple weakly to long wavelengths.

**(ii) The suppression is visible in perturbation theory** because
each Feynman diagram with an irrelevant insertion carries extra
momentum factors that evaluate to $\hat{\Delta}^{d_O-4}$ when
sandwiched between low-momentum states.

**(iii) Non-perturbatively, the suppression should hold** because:
(a) instanton corrections are exponentially small (Bogomolny bound),
(b) large-field configurations are suppressed by $e^{-c/g^2}$
(Balaban), and (c) no mechanism exists for a non-perturbative effect
to violate dimensional scaling in an asymptotically free theory.

**(iv) But "should hold" is not a proof.** The gap between
"non-perturbative contributions are believed small" and "they are
proved small" is the gap between a $1000$-page argument and a $1050$
page argument. The technology exists (Balaban's multi-scale expansion);
the application to three-point functions has not been written.

---

## 6. Overall Assessment

### 6.1 Which approach is most promising?

**Approach 3 (circumventing Form A) is the correct framework.** Form A
is false, so any proof must work with the weaker statement that the
one-particle matrix element of $\hat{E}_k(0)$ is suppressed.

Within Approach 3, the most promising path is **extending Balaban's
multi-scale expansion to track the three-point function** (path-2a,
Section VII.5, Path A; and 10-open-problem.md, Path (a)). This would
establish the $\hat{\Delta}^2$ suppression non-perturbatively by
following the connected three-point correlator through the block-spin
RG, analogously to how Balaban follows the effective action (partition
function).

The second most promising path is **proving a spectral perturbation
theorem sensitive to operator dimension** (10-open-problem.md,
Path (b)). This would be a result in functional analysis/spectral
theory, independent of gauge theory specifics: for a transfer matrix
with gap $\hat{\Delta}$ and an irrelevant local perturbation of
dimension $d_O$, the gap shift is suppressed by $\hat{\Delta}^{d_O-4}$.
This would be a general theorem applicable beyond Yang-Mills.

### 6.2 Is the lemma true?

**Yes, almost certainly.** The evidence is overwhelming:

- Perturbation theory to all orders gives the correct suppression.
- Instanton and large-field corrections are exponentially suppressed.
- Every known Wilsonian RG example exhibits the same behavior.
- No mechanism for violating dimensional scaling is known.
- Lattice Monte Carlo simulations are consistent with $\Delta_\infty > 0$.

The statement $|\langle 1|\hat{E}_k(0)|1\rangle| \leq
C g_k^4 \hat{\Delta}^2$ is as well-supported as any unproved
statement in mathematical physics.

### 6.3 Is it provable with existing technology?

**Yes, but not in a short argument.** The proof requires extending
Balaban's polymer expansion to include operator insertions in
three-point functions. This is:

- **Technically feasible:** Balaban's framework already handles
  arbitrary local observables in the partition function. Tracking
  a local insertion through the RG is a controlled extension, not
  a new method.

- **Not trivial:** The bookkeeping for three-point polymer activities,
  with the power counting for the dimensional suppression at each RG
  step, is substantial. The estimate "50-100 pages" from path-2a
  appears realistic.

- **Not beyond current knowledge:** Dimock (2011-2013) has modernized
  Balaban's framework. Brydges et al. have carried out analogous
  extensions for scalar field theories. The gauge-theory complications
  (gauge fixing within polymers, Gribov copies) are already handled
  in Balaban's existing work.

### 6.4 Summary

| Statement | Verdict |
|:----------|:--------|
| Form A ($\hat{E}_k(0) = 0$ as operator identity) | **FALSE** |
| Form B ($|G_c^X(0,x)| \leq C\hat{\Delta}\,e^{-\Delta d}$) | **UNPROVED but believed true** |
| $\langle 1|\hat{E}_k(0)|1\rangle \leq C g_k^4\hat{\Delta}^2$ | **UNPROVED but believed true** |
| The form factor bound (Conjecture 1) | **UNPROVED; requires new but feasible work** |
| The continuum mass gap $\Delta_\infty > 0$ | **CONDITIONAL on the above** |

### 6.5 What this means for the proof architecture

The file 52-power-counting-lemma-rigorous.md claimed $\hat{E}_k(0) = 0$
as "PROVED" by appeal to Balaban's decomposition. This claim is
incorrect: Balaban's vacuum subtraction removes the vacuum EXPECTATION,
not the operator. The file 50-circularity-broken.md assembled a
"complete proof" relying on this incorrect claim.

The honest status is:

$$\underbrace{\text{Lattice mass gap}}_{\text{PROVED}}
  + \underbrace{\text{Balaban UV stability}}_{\text{PROVED}}
  + \underbrace{\text{Parity (first moment)}}_{\text{PROVED}}
  + \underbrace{\text{Non-perturbative form factor}}_{\text{OPEN}}
  = \underbrace{\Delta_\infty > 0}_{\text{CONDITIONAL}}$$

The open step is a well-defined problem in constructive QFT. It
requires extending Balaban's multi-scale analysis from the partition
function to the three-point function involving the one-particle state
and an irrelevant operator insertion. This extension uses existing
technology but has not been carried out.

---

## 7. A Precise Conjecture (Replacing Form A)

Based on the analysis above, we replace the false Form A with the
correct statement:

**Conjecture (Non-perturbative form factor at zero momentum).**
*For $\mathrm{SU}(N)$ lattice gauge theory in Balaban's small-field
region at RG step $k$, with mass gap $\hat{\Delta}_k$ and irrelevant
remainder $E_k$ satisfying $\|E_k\| \leq C g_k^4$ per site:*

$$\Big|\langle 1,\vec{p}=0\Big|\sum_{x \in \Lambda_k}
  E_k(x)\Big|1,\vec{p}=0\rangle\Big|
  \leq C'\,g_k^4\,\hat{\Delta}_k^2\,V$$

*where $|1,\vec{p}=0\rangle$ is the one-glueball state at zero spatial
momentum, $V$ is the lattice volume, and $C'$ depends on $N$ and the
operator structure but not on $k$, $\hat{\Delta}$, or $V$.*

This conjecture is:
- Proved perturbatively to all orders (Theorem 7)
- Supported by the Bogomolny bound on instantons
- Supported by Balaban's large-field estimates
- Consistent with lattice Monte Carlo
- Sufficient for the continuum mass gap (feeds into Theorem 8)
- Provable by extending Balaban's expansion to three-point functions

It is the single remaining input needed for the Yang-Mills mass gap.
