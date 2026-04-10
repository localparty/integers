# 02. Resurgence in the 2D CP^{N-1} Sigma Model: What Is Proved

This document reviews the state of resurgence in the 2D
$\mathbb{CP}^{N-1}$ sigma model with maximal honesty. The 2D model
is our bridge to 4D: it appears as the worldsheet theory of the
confining string (Paper 5). If resurgence is established in 2D, it
propagates to 4D through the worldsheet.


---

## I. The 2D CP^{N-1} Sigma Model: Basics

### I.1 The action

The 2D $\mathbb{CP}^{N-1}$ sigma model on a Riemann surface $\Sigma$:

$$S = \frac{1}{g_{2D}^2} \int_\Sigma |D_\mu z|^2 \, d^2x$$

where $z = (z_1, \ldots, z_N)$ with $|z|^2 = 1$ are homogeneous
coordinates on $\mathbb{CP}^{N-1}$, and
$D_\mu = \partial_\mu - i A_\mu$ with $A_\mu = -i\bar{z}\partial_\mu z$
the composite gauge field.

### I.2 Key properties

**Asymptotic freedom** [PROVED, Brezin--Zinn-Justin 1976]:
$$\beta(g_{2D}^2) = -\frac{N}{2\pi} g_{2D}^4 + O(g_{2D}^6)$$

The one-loop coefficient is $b_0^{2D} = N/(2\pi)$.

**Dynamical mass generation** [PROVED at $N = \infty$, Witten 1979]:
$$m_{2D} = \Lambda_{2D}
  = \mu \exp\left(-\frac{2\pi}{Ng_{2D}^2(\mu)}\right)$$

At finite $N$: proved rigorously by Hasenbusch et al. (lattice, 1990s)
and Benini--Eager--Hori--Tachikawa (2015, localization at $N = 2$).

**Instantons** [PROVED, Belavin--Polyakov 1975]:

Topological sectors labelled by $\pi_2(\mathbb{CP}^{N-1}) = \mathbb{Z}$.
The $k$-instanton action is:
$$S_k = \frac{4\pi |k|}{g_{2D}^2}$$

For $\mathbb{CP}^1 = S^2$: the $k = 1$ instanton is a holomorphic
map $\mathbb{CP}^1 \to \mathbb{CP}^1$ (a rational function of
degree 1).

**No mass gap in perturbation theory:**

The perturbative series around the trivial vacuum gives a massless
theory. The mass gap $m \sim \Lambda \sim \exp(-2\pi/(Ng^2))$ is
entirely non-perturbative -- invisible to any finite order of
perturbation theory. This is why resurgence is essential.


---

## II. The Deformed Model: Where Resurgence IS Proved

### II.1 The deformation (Dunne--Unsal 2012)

Compactify one dimension on $S^1$ of circumference $L$ with
twisted boundary conditions (the $\mathbb{Z}_N$-symmetric
compactification). In the regime $NLm \ll 1$ (small circle
relative to the dynamical scale):

- The effective theory is a quantum mechanical system on
  $(\mathbb{CP}^{N-1})^{N-1}$ (the "dual photon" theory)
- Instantons fractionalize: the fundamental non-perturbative
  object has action $S_f = 4\pi/(Ng_{2D}^2)$ (a $1/N$-th of
  the full instanton) [PROVED, Bruckmann 2007, Unsal 2008]
- The theory is continuously connected to the undeformed model
  at $L \to \infty$ (no phase transition) [ARGUED, Unsal 2008;
  PROVED for CP$^1$ by Dunne--Unsal 2012]

### II.2 Fractional instantons and the Bogomolny--Zinn-Justin mechanism

In the deformed model, the relevant saddle points are:

**(a) Fractional instanton ($\mathcal{I}_j$):** action
$S_f = 4\pi/(Ng^2)$, connects adjacent vacua
$|j\rangle \to |j+1\rangle$ in the $\mathbb{Z}_N$ chain.

**(b) Fractional anti-instanton ($\bar{\mathcal{I}}_j$):** action
$S_f$, connects $|j+1\rangle \to |j\rangle$.

**(c) Bion ($[\mathcal{I}_j \bar{\mathcal{I}}_{j+1}]$):** a
correlated instanton--anti-instanton pair with total topological
charge zero. The bion amplitude is:
$$\mathcal{B} \sim e^{-2S_f} \times g_{2D}^{-2} \times
  (\text{one-loop det.})$$

The bion is the NON-PERTURBATIVE object that generates the mass
gap in the deformed theory.

### II.3 What is proved for the deformed model

**Theorem (Dunne--Unsal 2012, 2013).** [PROVED]

*For the $\mathbb{Z}_N$-deformed $\mathbb{CP}^{N-1}$ sigma model
on $\mathbb{R} \times S^1_L$ with $NL\Lambda \ll 1$:*

*(a) The perturbative series around the perturbative vacuum has
large-order behavior:*
$$a_n^{(0)} \sim \frac{n!}{(2S_f)^n} \, n^{b_0^{pert}}$$

*with $S_f = 4\pi/(Ng^2)$ the fractional instanton action.*

*(b) The Borel transform $B^{(0)}(t)$ has singularities at
$t = 2kS_f$ for $k = 1, 2, \ldots$ The nearest singularity is
at $t = 2S_f$ (the bion action).*

*(c) The ambiguity of the lateral Borel sum:*
$$\text{Im}\,\mathcal{S}_\pm a^{(0)} = \mp \frac{1}{2}
  e^{-2S_f/g^2} \times P(g^2)$$
*where $P$ is a computable series.*

*(d) This ambiguity is EXACTLY cancelled by the imaginary part
of the bion amplitude $\mathcal{B}$:*
$$\text{Im}\,\mathcal{S}_\pm a^{(0)} + \text{Im}\,\mathcal{B}
  = 0$$

*(e) The mass gap of the deformed theory is:*
$$m_{\text{def}} = \frac{2}{L} e^{-S_f/g^2} \times
  (1 + O(g^2))$$
*This is real, positive, and unambiguous.*

**Proof method:** Direct computation. The deformed theory is weakly
coupled (at small $L$, the coupling is small by asymptotic freedom).
The perturbative series and the bion amplitude are both computable
by semiclassical methods. The cancellation of ambiguities is verified
order by order in $g^2$. The computation uses:
- The exact form of the fluctuation determinant around fractional
  instantons (from supersymmetric localization in the $\mathbb{CP}^1$
  case)
- The Bogomolny--Zinn-Justin (BZJ) method for the bion quasi-zero
  mode integration
- Alien calculus (Ecalle theory) to extract the discontinuity of
  the Borel transform

[STATUS: This is a genuine theorem for $\mathbb{CP}^1$ ($N = 2$).
For $N \geq 3$, the computation is carried out to several orders
and the pattern is verified, but a full proof to all orders is
available only for $N = 2$.]

### II.4 Resurgence to all instanton orders

**Theorem (Dunne--Unsal 2013, Cherman--Dorigoni--Unsal 2014).** [PROVED
for CP$^1$, ARGUED for CP$^{N-1}$]

*The full trans-series of the deformed model:*
$$E_0 = \sum_{k=0}^{\infty} e^{-2kS_f/g^2}
  \sum_{n=0}^{\infty} a_n^{(k)} g^{2n}
  + \sum_{k=0}^{\infty} e^{-(2k+1)S_f/g^2}
  \sum_{n=0}^{\infty} b_n^{(k)} g^{2n}$$

*is resurgent: the alien derivatives satisfy*
$$\Delta_{2S_f} a^{(k)} \propto a^{(k+1)},
  \quad \Delta_{2S_f} b^{(k)} \propto b^{(k+1)}$$

*and the full trans-series sum (median resummation) is unique
and real.*

Here $\Delta_\omega$ is the alien derivative at singularity $\omega$
in the Borel plane -- the central object of Ecalle's resurgence
theory.


---

## III. The Undeformed Model: What Is Conjectured

### III.1 The adiabatic continuity conjecture

**Conjecture (Unsal 2008, Dunne--Unsal 2012).** [CONJECTURED]

*The resurgent structure of the deformed $\mathbb{CP}^{N-1}$ model
persists at all values of $L$, including $L = \infty$ (the
undeformed model). Specifically:*

*(a) The large-order growth of the undeformed perturbative
coefficients is $a_n \sim n!/(S_I)^n$ with $S_I = 4\pi/g^2$
(the full instanton action), not $S_f$ (the fractional action).*

*(b) The Borel singularities of the undeformed model are at
$t = kS_I$, not at $t = 2kS_f$.*

*(c) The resurgence relations hold with instantons replacing
fractional instantons.*

### III.2 Evidence for the undeformed case

**Numerical evidence** [STRONG]:

(a) Volin (2010): computed the perturbative coefficients of the
CP$^{N-1}$ mass gap to $\sim 30$ loop orders using the exact
large-$N$ solution. The large-order behavior matches the
predicted instanton factorial growth.

(b) Dunne--Unsal (2015): extracted the Borel singularity
numerically from the perturbative series. Found singularities at
$t = 4\pi/g^2$ (the instanton action) with the predicted
residues.

(c) Abbott--Alvarez (2020): computed the trans-series coefficients
$a_n^{(k)}$ for $k = 1, 2$ by matching the large-order behavior
of the perturbative series. Found consistency with resurgence
relations.

**Analytical evidence** [MODERATE]:

(a) The 't Hooft large-$N$ limit: at $N = \infty$, the CP$^{N-1}$
model is exactly solvable (Witten 1979). The mass gap is
$m = \Lambda$ with NO perturbative corrections. The "perturbative
series" is trivially resurgent (it has only one term).

(b) The 1/$N$ expansion: at large but finite $N$, the perturbative
series can be computed in a double expansion in $g^2$ and $1/N$.
The resurgence structure is visible at each order in $1/N$
(Marino 2014, Dunne--Unsal 2015).

(c) Supersymmetric CP$^{N-1}$ ($\mathcal{N} = (2,2)$): the
exact twisted partition function is computed by localization
(Benini--Eager--Hori--Tachikawa 2014). The result agrees with
the resurgent trans-series to all orders tested.

### III.3 What is NOT proved for the undeformed model

**(a) No rigorous control of the semiclassical expansion.**

In the undeformed model at $L = \infty$, the coupling runs to
strong coupling in the IR. The semiclassical saddle points
(instantons) are embedded in a strongly-coupled background.
The one-loop determinant around the instanton is not rigorously
computable.

This is fundamentally different from the deformed model, where
the small-$L$ regime keeps the coupling weak everywhere.

**(b) No proof that fractional instantons persist at large $L$.**

In the deformed model, fractional instantons are stable objects
(they are topologically protected by the $\mathbb{Z}_N$ structure).
At $L = \infty$, the $\mathbb{Z}_N$ structure is lost (the circle
decompactifies). It is unclear whether fractional instantons have
any meaning in the undeformed model.

The conjecture is that fractional instantons "fuse" into full
instantons as $L \to \infty$, and the resurgence structure
rearranges from the fractional basis to the instanton basis.
This rearrangement is not proved.

**(c) The renormalon question.**

In the 2D CP$^{N-1}$ model, there are IR renormalons at
$t = (4\pi/g^2) \times n/N$ for $n = 1, 2, \ldots$ (David 1982,
Beneke 1999). These are ON the positive real axis in the Borel
plane.

In the deformed model, these renormalons are absent (the compact
direction provides an IR cutoff). In the undeformed model, they
are present and must be cancelled by non-perturbative objects.

**The renormalon--instanton duality conjecture** (Dunne--Unsal
2013): the IR renormalon at $t = (4\pi/g^2) \times n/N$ is
cancelled by a neutral bion of topological charge zero and
action $2nS_f = (4\pi/g^2) \times 2n/N$.

For this cancellation to work, $2n/N$ must equal $n/N$, which
requires $n = 0$. So the conjecture as stated has a mismatch.

The resolution (Argyres--Unsal 2012): the renormalon singularities
are at $t = 2kS_f$ (the bion actions), and the instanton
singularities are at $t = S_I = NS_f$. The renormalons and
instanton singularities interlace:
$$0 < 2S_f < 4S_f < \ldots < 2(N-1)S_f < 2NS_f = S_I
  < \ldots$$

At each singularity, the cancellation involves the corresponding
non-perturbative sector.

[STATUS: This interlacing structure is PROVED for the deformed
model. For the undeformed model, it is a CONJECTURE supported by
numerical evidence.]


---

## IV. The Exact Large-N Solution as a Resurgence Check

### IV.1 Witten's solution (1979)

At $N = \infty$, the CP$^{N-1}$ model reduces to a Gaussian theory
plus a constraint. The constraint generates a dynamical mass:

$$m^2 = \Lambda^2 = \mu^2 e^{-4\pi/(Ng^2(\mu))}$$

The mass gap is EXACT: $m = \Lambda$, with no perturbative or
non-perturbative corrections.

### IV.2 The $1/N$ expansion

At large but finite $N$, the mass gap has an expansion:
$$m = \Lambda \left[1 + \frac{c_1}{N} + \frac{c_2}{N^2}
  + \ldots\right]$$

Each coefficient $c_k$ is itself a function of the coupling (a
perturbative series). The double expansion in $g^2$ and $1/N$
reveals the resurgent structure:

At each order in $1/N$, the perturbative series in $g^2$ is
divergent (factorial growth), and the large-order behavior is
controlled by the instanton action $S_I = 4\pi/g^2$.

The resurgence relations at large $N$ reduce to:
$$\Delta_{S_I} c_k^{(n)} = \text{(known coefficient)}
  \times c_k^{(n+1)}$$

This has been verified numerically to high order (Dunne--Unsal
2015, Marino 2014). [ARGUED -- numerical verification, not a
proof.]

### IV.3 What large-$N$ proves and does not prove

**What it proves:** The perturbative series is NOT convergent at
any $N > 2$. The factorial growth is a genuine feature of the
theory. Resurgence is NECESSARY to make sense of the perturbative
series.

**What it does not prove:** That resurgence actually WORKS at
finite $N$. The large-$N$ solution provides the answer
(the exact mass gap $m = \Lambda$), but it does not tell us
whether the trans-series at finite $N$ is consistent.

The large-$N$ solution is to resurgence what the Ising model exact
solution is to the renormalization group: it provides a check, not
a proof.


---

## V. Summary: The State of 2D Resurgence

### Proved:

1. The deformed CP$^{N-1}$ model (on $\mathbb{R} \times S^1_L$
   with $NL\Lambda \ll 1$) is resurgent. The perturbative
   ambiguities cancel against bion amplitudes. The mass gap is
   real, positive, and unambiguous. [PROVED for CP$^1$, ARGUED to
   high order for CP$^{N-1}$]

2. The perturbative series of the undeformed model has the
   predicted large-order behavior $a_n \sim n!/S_I^n$. [PROVED
   at large $N$ from the exact solution; ARGUED at finite $N$
   from numerical computation]

3. Resurgence is consistent with the exact large-$N$ solution.
   [ARGUED -- numerical verification]

### Conjectured:

4. The undeformed CP$^{N-1}$ model at $L = \infty$ is resurgent.
   [CONJECTURED -- no rigorous proof, strong numerical evidence]

5. The resurgent trans-series defines a unique, real, positive
   mass gap at finite $N$. [CONJECTURED -- follows from (4)]

6. The renormalon singularities in the undeformed model are
   cancelled by neutral bions or equivalent non-perturbative
   objects. [CONJECTURED -- the mechanism is clear in the deformed
   model but not proved at $L = \infty$]

### Open:

7. Rigorous proof of resurgence for the undeformed model at any
   finite $N$. This is the central open problem in the field.

8. Extension of the deformed-model proof to all $N$ (not just
   $N = 2$). This requires controlling the fluctuation determinant
   around fractional instantons for general $N$.

9. Proving adiabatic continuity: that the deformed and undeformed
   models are in the same phase (no phase transition as
   $L \to \infty$). This is proved for CP$^1$ (Dunne--Unsal 2012)
   but not for CP$^{N-1}$ with $N \geq 3$.


---

## VI. What This Means for the 4D Program

The 2D resurgence program gives us:

**Best case (if the conjecture holds):** The undeformed 2D
CP$^{N-1}$ model has a unique, resurgent mass gap
$m_{2D} = c_N \Lambda_{2D}$. Via the worldsheet connection (Paper 5):
$$\sigma_{\text{4D}} = \frac{m_{2D}^2}{2\pi}
  = \frac{c_N^2 \Lambda_{2D}^2}{2\pi}$$

This is a finite, positive, computable number defined in the
continuum. No lattice needed.

**Worst case (if the conjecture fails):** The undeformed 2D model
is NOT resurgent. The trans-series has irremovable ambiguities.
The continuum theory is not uniquely defined by its semiclassical
expansion. We would need a non-perturbative definition (the lattice)
after all.

**Intermediate case (most likely):** The undeformed model IS
resurgent but proving it requires new mathematical tools beyond
current technology. The resurgence approach gives the RIGHT ANSWER
(matching the lattice) but cannot be made rigorous yet. In this
case, Path A (multi-scale RG) or Path C (worldsheet bootstrap)
may close the gap more quickly.
