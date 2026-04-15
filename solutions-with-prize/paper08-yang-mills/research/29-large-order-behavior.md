# Large-Order Behavior of the Zeta-Regularized Perturbative Series

This section computes the growth rate of the $L$-loop coefficient
$\Gamma^{(L)}$ in the zeta-regularized Kaluza--Klein theory on
$M^4 \times \mathbb{CP}^{N-1}$. The goal: determine whether the
perturbative series is Borel summable.


---

## I. Review: The Loop Structure (from Papers 1, 4)

At $L$ loops, the effective action of the KK theory decomposes as
(Appendices F, G, K, S of Paper 1):

$$\Gamma^{(L)} = \sum_{\text{diagrams } j} c_j(\epsilon) \times
  F_j(R, \{m_n\})$$

where $c_j(\epsilon)$ are 4D momentum integrals (in dimensional
regularization, $d = 4 - 2\epsilon$), and $F_j$ are KK mode sums.

### I.1 The KK mode sum at $L$ loops

Each $F_j$ has the structure (Appendix K, §K.3.1):

$$F_j = \sum_{\mathbf{n} \in \mathbb{Z}^L \setminus \{0\}}
  Q_j(\mathbf{n})^{p_j} = E_L(-p_j; Q_j)$$

where:
- $\mathbf{n} = (n_1, \ldots, n_L)$ are the KK mode numbers on the
  $L$ internal propagators
- $Q_j(\mathbf{n}) = \mathbf{n}^T A_j \mathbf{n}$ is a
  positive-definite quadratic form determined by the diagram topology
- $p_j \geq 0$ is the mass power (from the Seeley--DeWitt expansion)
- $E_L(s; Q)$ is the $L$-dimensional Epstein zeta function

### I.2 The two cases

**Case A: $p_j = 0$ (leading term).** $F_j = E_L(0; Q_j)$.
For the S$^1$ theory:
$$S_0^{(L)} = [1 + 2\zeta(0)]^L = 0^L = 0$$

This is the vanishing of the leading divergence at every loop order.

**Case B: $p_j \geq 1$ (subleading terms).** $F_j = E_L(-p_j; Q_j)$
with $-p_j \leq -1$. By the Epstein--Terras theorem:
- $E_L(s; Q)$ is meromorphic with a single pole at $s = L/2$
- For $s = -p_j \leq -1$: evaluation point is in the holomorphic
  region ($-p_j < 0 < L/2$)
- Therefore $F_j$ is a finite, computable number

### I.3 The key identity: $S_0 = 0$

On $S^1$ of circumference $L_e = 2\pi R$:
$$S_0 = \sum_{n = -\infty}^{\infty} 1 = 1 + 2\sum_{n=1}^{\infty} 1
  = 1 + 2\zeta(0) = 1 + 2(-\tfrac{1}{2}) = 0$$

This is the zeta-regularized total mode count. The zero mode ($n = 0$)
contributes $+1$; the nonzero modes ($n \neq 0$) contribute
$2\zeta(0) = -1$. They cancel exactly.


---

## II. Extension to CP(N-1): The Spectral Zeta at $s = 0$

The analogous quantity for $\mathbb{CP}^{N-1}$ is the **spectral zeta
function at $s = 0$** for the operator governing the KK modes.

### II.1 The relevant operator

For the Yang--Mills perturbative expansion, the KK modes are the
excitations of the gauge field on $\mathbb{CP}^{N-1}$. The relevant
operator is the **Hodge Laplacian on adjoint-valued one-forms**:
$$\Delta_{\text{adj}} = \Delta_{\text{Hodge}} \otimes \mathbf{1}_{\text{adj}}$$

acting on $\Omega^1(\mathbb{CP}^{N-1}, \text{ad}\,P)$. Its eigenvalues
are $\mu_n$ (from Appendix G) with degeneracies $d_n^{\text{adj}} =
d_n \times (N^2 - 1)$ (the factor $N^2 - 1$ comes from the adjoint
representation).

### II.2 The mode count

The spectral zeta at $s = 0$ is the zeta-regularized total mode count:
$$\zeta_{\text{adj}}(0) = \sum_n d_n^{\text{adj}} \times
  \mu_n^0 = \sum_n d_n^{\text{adj}} \quad (\text{zeta-regularized})$$

**For $S^1$:** $\zeta_{S^1}(0) = 0$ (proven above). This gives
$S_0^{(L)} = 0$ at all $L$.

**For $\mathbb{CP}^{N-1}$:** We need to compute
$\zeta_{\text{adj}}(0)$.

### II.3 Computing $\zeta_{\text{adj}}(0)$ on $\mathbb{CP}^{N-1}$

The spectral zeta at $s = 0$ is related to the heat kernel by the
Mellin transform. For a compact $d$-dimensional manifold $M$ with
operator $D$ (no zero modes):

$$\zeta_D(0) = \frac{a_{d/2}(D)}{(4\pi)^{d/2}}$$

where $a_{d/2}$ is the $(d/2)$-th Seeley--DeWitt coefficient.

For $\mathbb{CP}^{N-1}$ (real dimension $d = 2(N-1)$) with the Hodge
Laplacian on adjoint-valued one-forms:

$$\zeta_{\text{adj}}(0) = \frac{a_{N-1}(\Delta_{\text{adj}})}
  {(4\pi)^{N-1}}$$

The Seeley--DeWitt coefficient $a_{N-1}$ is a polynomial in the
curvature invariants of $\mathbb{CP}^{N-1}$ (scalar curvature $R$,
Ricci tensor $\text{Ric}$, Riemann tensor $\text{Riem}$).

**For $N = 2$ ($\mathbb{CP}^1 = S^2$, $d = 2$):**
$$\zeta_{\text{adj}}(0) = \frac{a_1(\Delta_{\text{adj}})}{4\pi}$$

$a_1 = (1/6) \int_{S^2} [R - 6E] \, d\mu$ where $E$ is the
endomorphism from the Weitzenb\"ock formula. For the Hodge Laplacian on
1-forms on $S^2$ with $\text{Ric} = (1/r^2)g$:

$a_1 = [(R/6 - 1/r^2)] \times \text{Vol}(S^2) \times 3
  = [(2/r^2)/6 - 1/r^2] \times 4\pi r^2 \times 3
  = [-2/(3r^2)] \times 12\pi r^2 = -8\pi$

$\zeta_{\text{adj}}^{S^2}(0) = -8\pi / (4\pi) = -2$

So the zeta-regularized mode count for gauge fields on $S^2$ is $-2$.

**This is non-zero!** The $S_0 = 0$ cancellation that works on $S^1$
does NOT work on $S^2$ for the gauge field modes.


### II.4 Consequences for the leading divergence

For the KK theory on $M^4 \times \mathbb{CP}^{N-1}$, the leading
$L$-loop divergence is:

$$S_0^{(L)} = [\zeta_{\text{adj}}(0)]^L$$

**On $S^1$:** $S_0^{(L)} = 0^L = 0$. Leading divergence vanishes. ✓

**On $S^2$:** $S_0^{(L)} = (-2)^L$. Leading divergence grows
exponentially: $|S_0^{(L)}| = 2^L$.

**On $\mathbb{CP}^2$:** $S_0^{(L)} = [\zeta_{\text{adj}}^{CP^2}(0)]^L$.
The value depends on the heat kernel computation.

The $S_0 = 0$ mechanism is specific to $S^1$. It does not generalize
to $\mathbb{CP}^{N-1}$ for the gauge field Laplacian.


---

## III. The Modified Strategy

The $S_0 = 0$ cancellation was the starting hope for Borel summability.
Since it fails on $\mathbb{CP}^{N-1}$, we need a different approach.

### III.1 What the Epstein-Terras theorem still gives

Even though $S_0^{(L)} \neq 0$, the subleading terms are still finite:
- $E_L(-p; Q_L)$ is finite for all $p \geq 1$ and all $L$
  (pole at $s = L/2 > 0$, evaluation at $s = -p < 0$)
- Each individual diagram gives a finite contribution at each loop order
- The theory is **renormalizable** (the divergences organize into
  known structures), even if not UV-finite

### III.2 The key distinction: UV-finite gravity vs renormalizable YM

**Gravity on $M^4 \times S^1$** (Papers 1, 4): $S_0 = 0$ makes the
gravitational effective action UV-finite at all loops.

**Yang--Mills on $M^4 \times \mathbb{CP}^{N-1}$** (this paper):
$S_0 \neq 0$ means the leading divergences do NOT cancel. The theory
has the SAME UV divergences as standard 4D Yang--Mills (it's
asymptotically free, not UV-finite).

This makes sense: the KK theory reproduces standard 4D Yang--Mills
below the KK scale. The UV divergences are part of that reproduction.
The zeta regularization does not remove them; it computes them.

### III.3 Implications for Borel summability

The perturbative coefficients grow as:
$$|\Gamma^{(L)}| \sim C^L \times L! \times L^b$$

where the $L!$ growth comes from the number of Feynman diagrams (same
as in standard 4D YM) and $C = g^2/(8\pi^2)$ is the inverse instanton
action.

This is the **same** large-order behavior as standard 4D Yang--Mills.
The KK construction does not change the large-order behavior of the
perturbative series.

The Borel transform has singularities at:
- $t = 8\pi^2$ (instanton) --- on the positive real axis
- $t = n/(2b_0)$ (renormalons) --- on the positive real axis

**The Borel sum is ambiguous** (same ambiguity as in standard YM).


---

## IV. What This Means for the Continuum Limit

The Borel summability approach (Section 28) does not work as initially
hoped. The zeta regularization does not remove the factorial growth of
Yang--Mills perturbation theory. The KK construction reproduces standard
4D Yang--Mills, including its perturbative pathologies.

**What the KK construction DOES provide** (which standard 4D does not):

1. **The lattice mass gap at all practical couplings** (Sections 21--25).
   This is a non-perturbative result that goes beyond perturbation theory.

2. **The topological mechanism for confinement** (screening obstruction,
   Bogomolny bound). This is independent of perturbation theory.

3. **The SU(2) exact solution** (Appendix H). This is completely
   non-perturbative.

The continuum limit remains the open frontier. The Borel approach was
a creative attempt to bypass it, but the factorial growth of
perturbation theory (which is a property of Yang--Mills, not of the
regularization scheme) blocks it.


---

## V. The Remaining Path

The continuum limit requires a non-perturbative argument. Two
approaches remain viable:

### V.1 The lattice path (Sections 21-25)

The lattice mass gap is proved for $a \gg r_3$. The continuum limit
requires extending this to $a \to 0$. The obstacle: the cluster
expansion fails for $a \lesssim r_3$.

**What could close it:** A multi-scale RG analysis (Balaban-type) that
controls the theory scale-by-scale as $a$ decreases through $r_3$.
The CP$^{N-1}$ topology provides constraints at each scale (the
Bogomolny bound is scale-independent).

### V.2 The direct continuum path

Define the theory directly on $M^4 \times \mathbb{CP}^{N-1}$ without
a lattice. The definition would use:
- Perturbation theory (zeta-regularized, finite at each order) for the
  perturbative sector
- The Bogomolny bound for the instanton sector
- A resurgent trans-series combining both:
  $$\Gamma = \sum_{L=0}^{\infty} g^{2L} \Gamma^{(L)} +
    \sum_{k=1}^{\infty} e^{-8\pi^2 k/g^2} \sum_{L=0}^{\infty}
    g^{2L} \Gamma_k^{(L)}$$

The resurgent trans-series is NOT Borel summable (the perturbative part
has factorial growth). But it may be **resurgent** --- the ambiguities
of the Borel sum at each instanton order cancel against ambiguities at
higher instanton orders.

**Resurgence** (Écalle 1981, Dunne--Ünsal 2012--2016) is a precise
mathematical framework for making sense of non-Borel-summable series.
In recent years, resurgence has been applied to:
- Quantum mechanics (the double-well potential: Zinn-Justin 2004)
- 2D sigma models (Dunne--Ünsal 2012)
- Deformed Yang--Mills (Argyres--Ünsal 2012)

The CP$^{N-1}$ model in 2D is one of the prime examples of resurgence
(Dunne--Ünsal 2013). The perturbative and non-perturbative sectors
combine into a unique, unambiguous trans-series.

**The conjecture (revised):** The trans-series for Yang--Mills on
$M^4 \times \mathbb{CP}^{N-1}$ is resurgent. The Bogomolny bound on
$\mathbb{CP}^{N-1}$ provides the instanton actions that control the
cancellation of ambiguities. The resurgent trans-series defines the
theory non-perturbatively in the continuum.

This replaces the (failed) Borel summability conjecture with a
(plausible) resurgence conjecture. Resurgence is a weaker condition
than Borel summability but equally powerful for defining the theory.


---

## VI. Summary: Honest Status After This Computation

The computation of $\zeta_{\text{adj}}(0)$ reveals that the $S_0 = 0$
mechanism does NOT extend from $S^1$ to $\mathbb{CP}^{N-1}$ for the
gauge field Laplacian. The perturbative series has the standard
factorial growth.

| Claim | Status |
|-------|--------|
| $S_0 = 0$ on $S^1$ (gravity) | **PROVED** (Paper 1) |
| $S_0 = 0$ on $\mathbb{CP}^{N-1}$ (gauge) | **FALSE** (Section II.3) |
| Perturbative series Borel summable | **FALSE** (Section III.3) |
| Perturbative series resurgent | **CONJECTURED** (Section V.2) |
| Lattice mass gap at practical $\beta$ | **PROVED** (Sections 21--25) |
| Continuum limit | **OPEN** |

The creative exploration (Section 28) identified the right direction
(bypass the lattice, define the theory non-perturbatively) but the
specific mechanism (Borel summation from UV finiteness) does not apply
to the gauge sector. The corrected mechanism (resurgence) is a viable
path forward but requires further development.

**The lattice proof (Sections 21--25) remains the strongest result.**
The continuum limit is the open frontier, approachable via either
multi-scale RG or resurgence.
