# 6. Balaban's Renormalization Group Descent

## 6.1 Context

Tadeusz Balaban (1982--1989) constructed a rigorous block-spin
renormalization group for lattice $\mathrm{SU}(N)$ Yang--Mills in
$d = 4$.  We use his results as a black box.  This section states what
we take from Balaban and what remains to be proved.


## 6.2 The Block-Spin RG

Start from a fine lattice $\Lambda_0$ with spacing $a_0$ and bare
coupling $g_0$.  At RG step $k$, define a coarser lattice $\Lambda_k$
with spacing $a_k = 2^k a_0$ by block-spinning the link variables over
$2^4$ blocks.

**Theorem (Balaban, UV stability).**
*For $g_0$ sufficiently small, the block-spin RG can be iterated
indefinitely: for every $k \geq 0$, the effective action on $\Lambda_k$
is well-defined, gauge-invariant, and bounded.  The iteration does not
produce divergences or leave the domain of analyticity.*

The condition $g_0$ small corresponds to $\beta_0 = 2N/g_0^2$ large,
compatible with the lattice mass gap of Section 4 (which holds for
$\beta < a_0/(2\sqrt{3}\,r_3)$, satisfied when $a_0/r_3 \gg 1$).


## 6.3 The Effective Action

At RG step $k$, Balaban's construction yields an effective action of
the form

$$S_k \;=\; \frac{1}{g_k^2}\,S_{\mathrm{YM}} \;+\;
  \sum_{n} c_n^{(k)}\,\mathcal{O}_n \;+\; E_k,$$

where $S_{\mathrm{YM}}$ is the Wilson plaquette action on $\Lambda_k$,
the $\mathcal{O}_n$ are local gauge-invariant operators of dimension
$d_n > 4$, and $E_k$ is the total irrelevant remainder.

**Running coupling.**  The coupling evolves as

$$g_{k+1}^2 \;=\; g_k^2 \;-\; b_0\,g_k^4\,\ln 2 \;+\; O(g_k^6),$$

where $b_0 = \frac{11N}{3(4\pi)^2}$ is the one-loop $\beta$-function
coefficient.  Since $b_0 > 0$ (asymptotic freedom), $g_k^2$ decreases
as $k$ increases.

**Irrelevant operator coefficients.**  Each coefficient satisfies

$$|c_n^{(k)}| \;\leq\; C_n\,g_k^{d_n - 4},$$

where $C_n$ depends on $n$ but not $k$.  Since $d_n > 4$, these are
suppressed by positive powers of $g_k$.

**Total remainder.**  The remainder satisfies

$$\|E_k\| \;\leq\; C\,g_k^4 \qquad \text{per unit volume},$$

where $C$ is universal and the norm is $L^\infty$ on gauge-invariant
functionals of the block-averaged fields.


## 6.4 Convergence of the Scale Factor

Under one RG step, the mass gap $\Delta_k$ transforms as

$$\Delta_{k+1} \;=\; \Delta_k\,\bigl(1 + O(g_k^4)\bigr).$$

Define the accumulated scale factor

$$\Lambda_k \;=\; \prod_{j=0}^{k-1}\bigl(1 + O(g_j^4)\bigr).$$

Since $g_j^2 \sim 1/(b_0 j \ln 2)$ for large $j$ (one-loop running),
we have $g_j^4 \sim 1/(b_0 j \ln 2)^2$.  The infinite product converges
because the sum

$$\sum_{j=1}^{\infty} g_j^4 \;\sim\;
  \sum_{j=1}^{\infty} \frac{1}{(b_0\,\ln 2)^2\,j^2}
  \;=\; \frac{\pi^2/6}{(b_0\,\ln 2)^2} \;<\; \infty$$

is a Basel-type series.  Therefore $\Lambda_\infty = \lim_{k\to\infty}
\Lambda_k$ exists and satisfies $0 < \Lambda_\infty < \infty$.

If $\Delta_0 > 0$ (proved in Section 4), then

$$\Delta_\infty \;=\; \Delta_0 \cdot \Lambda_\infty \;>\; 0,$$

provided the $O(g_k^4)$ corrections are controlled not just in norm but
in their effect on the spectral gap of the transfer matrix.  This is the
content of the form factor bound (Section 8).


## 6.5 What Balaban Does NOT Prove

Balaban's work establishes UV stability.  It does **not** prove:

1. **The mass gap.**  Balaban does not show $\Delta_0 > 0$ at any
   lattice spacing.  This is proved in Sections 2--4 using the
   Kaluza--Klein cluster expansion.

2. **Confinement.**  The area law for Wilson loops is not addressed.

3. **The continuum limit as a QFT.**  Balaban controls the effective
   action at each finite step $k$ but does not construct the $k \to
   \infty$ limit as a Wightman or Osterwalder--Schrader theory.

4. **The spectral response.**  The bound $\|E_k\| \leq C g_k^4$ controls
   the action as a functional but does not, by itself, control how the
   eigenvalues of the transfer matrix $\hat{T}_k$ respond to the
   perturbation $E_k$.


## 6.6 What We Need Beyond Balaban

The missing ingredient is a **form factor bound**: the irrelevant
perturbation $E_k$ shifts the spectral gap by at most $O(g_k^4 \Delta_k)$.
Concretely, we need

$$|\Delta_k' - \Delta_k| \;\leq\; C\,g_k^4\,\Delta_k,$$

where $\Delta_k'$ is the gap of the perturbed transfer matrix
$\hat{T}_k' = \hat{T}_k\,e^{-E_k}$.  The bound has two parts:

- **Lattice power counting** (Section 7): $\hat{E}_k(q)$ vanishes at
  $q = 0$ to second order, giving $|\hat{E}_k(q)| \leq C g_k^4 |q|^2$.

- **Form factor estimate** (Section 8): the $|q|^2$ suppression bounds
  the spectral perturbation.  Perturbative (Theorem 7) is proved;
  non-perturbative (Conjecture 1) remains open.

Together with Balaban's UV stability, these feed into Section 9.
