# 02. The Weitzenboeck Spectral Gap

This section proves Theorem 1, which supplies the spectral gap in the
internal (fibre) direction. It is the foundational estimate on which
the cluster expansion (Section 03) rests.


---

## Statement

**Theorem 1 (Internal spectral gap).** *Let $\mathbb{CP}^{N-1}$ carry
the Fubini--Study metric with holomorphic sectional curvature
$4/r_3^2$. The Hessian of the internal action $S_{\text{int}}$ at the
flat connection $A = 0$ on $\mathbb{CP}^{N-1}$ satisfies*

$$\text{Hess}_{A=0}\, S_{\text{int}} \;\geq\;
  \frac{\mu_1}{g_{\text{int}}^2},
  \qquad \mu_1 = \frac{6}{r_3^2}.$$


---

## Proof

### Step 1. Quadratic approximation at $A = 0$

The internal action at a single lattice site is

$$S_{\text{int}}[A] \;=\; \frac{1}{2g_{\text{int}}^2}
  \int_{\mathbb{CP}^{N-1}} \text{Tr}\,|F_A|^2 \; d\mu.$$

Since $A = 0$ is a critical point (flat connection, $F_0 = 0$),
the first variation vanishes and the second variation in the direction
of a one-form perturbation $a \in \Omega^1(\mathbb{CP}^{N-1},
\text{ad}\,P)$ is

$$S_{\text{int}}^{(2)}[a] \;=\;
  \frac{1}{2g_{\text{int}}^2}
  \int_{\mathbb{CP}^{N-1}}
  \text{Tr}\bigl(a,\; \Delta_{\text{Hodge}}\, a\bigr) \; d\mu$$

where $\Delta_{\text{Hodge}} = (d + d^*)^2$ is the Hodge Laplacian
acting on $\mathfrak{g}$-valued one-forms.


### Step 2. The Weitzenboeck formula on $\mathbb{CP}^{N-1}$

The Weitzenboeck identity for one-forms on a Riemannian manifold
$(M, g)$ reads

$$\Delta_{\text{Hodge}}\, a \;=\; \nabla^*\nabla\, a
  \;+\; \text{Ric}(a)$$

where $\nabla^*\nabla \geq 0$ is the connection (rough) Laplacian and
$\text{Ric}$ acts on one-forms by $\text{Ric}(a)_b = R_{ab}\, a^a$.

The Fubini--Study metric on $\mathbb{CP}^{N-1}$ is Einstein:

$$R_{ab} \;=\; \frac{2N}{r_3^2}\, g_{ab}.$$

(For $N = 3$ this gives $R_{ab} = 6\, g_{ab}/r_3^2$; for general $N$
the Ricci scalar is $R = 2N(2N-2)/r_3^2$.) In particular
$\text{Ric} > 0$, so

$$\Delta_{\text{Hodge}}\, a \;=\;
  \nabla^*\nabla\, a + \frac{2N}{r_3^2}\, a
  \;\geq\; \frac{2N}{r_3^2}\, a.$$

For the physical case $N = 3$ this yields the lower bound
$6/r_3^2$. For general $N \geq 2$ the bound is $2N/r_3^2$; we write
$\mu_1 = 6/r_3^2$ when $N = 3$.


### Step 3. Absence of zero modes

The bound is strict. Since $H^1(\mathbb{CP}^{N-1};\mathbb{R}) = 0$
for all $N \geq 2$, there are no harmonic one-forms on
$\mathbb{CP}^{N-1}$. Therefore $\ker \Delta_{\text{Hodge}}
\cap \Omega^1 = \{0\}$, and every eigenvalue satisfies

$$\mu_n \;\geq\; \mu_1 \;=\; \frac{6}{r_3^2}
  \qquad (n \geq 1).$$

(The actual first eigenvalue is $\mu_{\min}^{(1)} = 12/r_3^2$,
exceeding the Weitzenboeck lower bound by a factor of two. The bound
$6/r_3^2$ is what the proof requires.)


### Step 4. The spectral gap estimate

Combining Steps 1--3:

$$S_{\text{int}}^{(2)}[a] \;=\;
  \frac{1}{2g_{\text{int}}^2}
  \bigl(a,\; \Delta_{\text{Hodge}}\, a\bigr)_{L^2}
  \;\geq\; \frac{\mu_1}{2g_{\text{int}}^2}\,
  \|a\|^2_{L^2}$$

with $\mu_1 = 6/r_3^2$. Equivalently,

$$\text{Hess}_{A=0}\, S_{\text{int}} \;\geq\;
  \frac{\mu_1}{g_{\text{int}}^2} \;=\;
  \frac{6}{g_{\text{int}}^2\, r_3^2}.$$

This completes the proof of Theorem 1. $\square$


---

## Corollary (Exponential decay of internal correlations)

**Corollary 1.1.** *In the $k = 0$ (trivial topological) sector, the
internal fluctuations $a = A - 0$ around the flat connection have
exponentially decaying correlations. The correlation length is*

$$\xi_{\text{int}} \;=\; \frac{g_{\text{int}}}{\sqrt{\mu_1}}
  \;=\; \frac{g_{\text{int}}\, r_3}{\sqrt{6}}.$$

*Proof.* The Gaussian approximation to the internal functional integral
in the $k = 0$ sector is dominated by
$\exp\!\bigl(-S_{\text{int}}^{(2)}[a]\bigr)$. The two-point function
in this approximation is

$$\langle a(y)\, a(y') \rangle \;=\;
  g_{\text{int}}^2\; G(y, y')$$

where $G = \Delta_{\text{Hodge}}^{-1}$ is the Green function of the
Hodge Laplacian on one-forms. Since $\Delta_{\text{Hodge}} \geq
\mu_1 > 0$, the Green function decays exponentially:

$$|G(y, y')| \;\leq\; C\, e^{-\sqrt{\mu_1}\, d(y, y')}
  \;=\; C\, e^{-d(y,y')\sqrt{6}/r_3}$$

for a constant $C > 0$ depending on $N$ and $r_3$. The correlation
length is $\xi_{\text{int}} = 1/\sqrt{\mu_1} \times g_{\text{int}}
= g_{\text{int}}\, r_3/\sqrt{6}$. $\square$


---

## Remarks

1. **Role in the proof chain.** Theorem 1 feeds directly into the
   bond activity bound (Theorem 2, Section 03). The exponential decay
   of internal correlations ensures that the bond activities
   $|g_b| \leq C_0\, e^{-m_1 a}$ are small, which is the input to
   the Kotecky--Preiss convergence criterion.

2. **Why $6/r_3^2$ suffices.** The actual spectral gap of
   $\Delta_{\text{Hodge}}$ on one-forms is $12/r_3^2$, but the proof
   only uses the Weitzenboeck lower bound $\mu_1 = 6/r_3^2$. This
   builds in a safety factor of two and avoids dependence on the
   explicit spectral computation.

3. **Generality.** The argument works for any $\mathbb{CP}^{N-1}$
   with $N \geq 2$. The Weitzenboeck bound $\mu_1 = 2N/r_3^2$
   improves with $N$, so the spectral gap grows linearly in $N$.
   The physically relevant case is $N = 3$.
