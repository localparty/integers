## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Uniformity in $L$.**

The bound $|C_{k+1}(L) - C_k(L)| \leq C' g_k^4 (a_k \Lambda)^s$ is claimed volume-independent. This requires the connected matrix element $\langle 1|E_k(0)|1\rangle_c$ to be volume-independent.

Section 5.7(e) proves this via the Volume Cancellation Lemma: the zero-momentum one-particle state $|1\rangle = V^{-1/2}\sum_{\vec{x}} |\vec{x}\rangle_{\mathrm{loc}}$ has delocalization factor $V^{-1/2} = L^{-3/2}$. The matrix element:

$$\langle 1|E_k(0)|1\rangle = V^{-1}\sum_{\vec{x},\vec{y}} \langle \vec{x}|E_k(0)|\vec{y}\rangle = V^{-1} \cdot V \cdot F(\vec{0}) = F(\vec{0})$$

where $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0}, \vec{y})$ and $f(\vec{x},\vec{y}) = \langle \vec{x}|E_k(0)|\vec{y}\rangle$. Translation invariance gives $\sum_{\vec{y}} f(\vec{x},\vec{y}) = F(\vec{x})$ independent of $\vec{x}$. The spatial sum gives $V^{-1} \cdot V \cdot F(\vec{0})$, cancelling the delocalization factor.

By locality and exponential clustering (rate $e^{-m|\vec{y}|}$ with $m > 0$), $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0},\vec{y})$ converges absolutely to a volume-independent limit for $L \gg 1/m$.

This cancellation is proved, not merely asserted. It is a standard result in lattice quantum field theory (the intensive nature of connected correlation functions), but the proof is explicit.

**(b) The infinite-volume mass gap.**

For fixed lattice spacing $a$, the mass gap $\Delta(a, L)$ converges to $\Delta(a, \infty)$ as $L \to \infty$ by exponential clustering (Section 4). The rate of convergence in $L$ is exponential: $|\Delta(a,L) - \Delta(a,\infty)| \leq C e^{-mL}$ where $m$ is the correlation length inverse.

Uniformity in $a$: the correlation length $1/m$ is bounded by $1/\Delta(a,\infty)$, which is bounded above uniformly in $a$ (the mass gap $\Delta(a,\infty) \geq \Delta_\infty/2 > 0$ for $a$ sufficiently small, since $\Delta(a,\infty) \to \Delta_\infty > 0$). Therefore $e^{-mL} \leq e^{-(\Delta_\infty/2)L}$ uniformly in $a$ for $a < a_*$. For finitely many values of $a \geq a_*$, each gives a positive mass gap $\Delta(a,\infty) > 0$ (from the cluster expansion), so the convergence rate $e^{-mL}$ is also uniform.

**(c) Exponential clustering in finite volume.**

On the periodic lattice $(\mathbb{Z}/L\mathbb{Z})^4$, the spectrum of the transfer matrix is discrete (finite-dimensional Hilbert space). There is a true spectral gap: the gap between the ground state (unique by RP) and the first excited state.

The finite-volume spectral gap is bounded below uniformly in $L$ by the cluster expansion: Theorem 4 establishes $\Delta_0(\beta, L) \geq c\sqrt{\sigma_0(\beta)} > 0$ with the string tension $\sigma_0(\beta) > 0$ computed from the cluster expansion, which is volume-independent (the cluster expansion constants do not depend on $L$).

The Moore-Osgood theorem then applies: (i) $C_k(L) \to C_\infty$ uniformly in $L$ (volume-independent bound), (ii) $\Delta(a_k, L) \to \Delta(a_k, \infty)$ pointwise in $k$. Therefore:

$$\lim_{k \to \infty}\lim_{L \to \infty} \Delta(a_k, L) = \lim_{L \to \infty}\lim_{k \to \infty} \Delta(a_k, L) = \Delta_\infty > 0$$

**Impact on the claimed result:**

None. The thermodynamic limit commutes with the continuum limit by Moore-Osgood, with all uniformity conditions rigorously verified. The volume-independence of connected matrix elements and the uniform lower bound on the finite-volume spectral gap are correctly established.
