## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Uniformity in $L$.** The volume cancellation lemma (Section 5.7(e)) proves that the connected matrix element $\langle 1|E_k(0)|1\rangle_c$ is independent of the spatial volume $V = L^3$. The proof:

1. The one-particle state at zero momentum is $|1\rangle = V^{-1/2} \sum_{\vec{x}} |\vec{x}\rangle_{\mathrm{loc}}$.
2. The matrix element decomposes as $V^{-1} \sum_{\vec{x},\vec{y}} \langle\vec{x}|E_k(0)|\vec{y}\rangle$.
3. By translation invariance, $\sum_{\vec{y}} \langle\vec{x}|E_k(0)|\vec{y}\rangle = F(\vec{x})$ is independent of $\vec{x}$.
4. The spatial sum gives $V^{-1} \cdot V \cdot F(\vec{0}) = F(\vec{0})$, cancelling the delocalization factor.
5. By locality and exponential clustering, $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0}, \vec{y})$ converges absolutely with rate $e^{-m|\vec{y}|}$ for $L \gg 1/m$.

This cancellation is standard in the transfer matrix formalism. The delocalization factor $V^{-1}$ from the zero-momentum state exactly cancels the spatial sum $V$ from translation invariance. The remaining quantity $F(\vec{0})$ is an intensive quantity (independent of volume).

**(b) The infinite-volume mass gap.** For fixed $a$, $\Delta(a, L) \to \Delta(a, \infty)$ as $L \to \infty$ by exponential clustering (Section 4). The rate of convergence is $|\Delta(a, L) - \Delta(a, \infty)| \leq C e^{-mL}$ where $m = \Delta(a, \infty)$ is the mass gap. This rate depends on $a$ through $m = \Delta(a, \infty)$, which varies with $a$.

The uniformity in $a$ required for the Moore-Osgood theorem is established as follows: the bound $|C_{k+1}(L) - C_k(L)| \leq C' g_k^4 (a_k\Lambda)^s$ is volume-independent (by the volume cancellation lemma). This bound controls the RG convergence uniformly in $L$, which is the condition for Moore-Osgood.

**(c) Exponential clustering in finite volume.** On the periodic lattice $(\mathbb{Z}/L\mathbb{Z})^4$, the spectrum is discrete and there is a true spectral gap (the gap between the ground state and first excited state). The finite-volume spectral gap $\Delta(L)$ satisfies $\Delta(L) \geq \Delta(\infty) - Ce^{-mL}$ for $L$ large, where the correction comes from finite-size effects (wrap-around contributions).

The cluster expansion (Section 4) is performed on the periodic lattice and directly gives exponential decay of connected correlators with rate $m \geq \alpha/a > 0$ uniformly in $L$ (Theorem 4(c)). This uniform lower bound on the finite-volume spectral gap ensures that $\Delta(L) \geq c > 0$ for all $L$ above a fixed threshold.

**Impact on the claimed result:** None. The thermodynamic limit commutes with the continuum limit as claimed.
