## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

(a) The volume cancellation is proved explicitly in Section 5.7(e) via a "Volume cancellation lemma": the connected matrix element $\langle 1|E_k(0)|1\rangle_c$ is independent of the spatial volume $V = L^3$. The proof: the zero-momentum state $|1\rangle = V^{-1/2} \sum_{\vec{x}} |\vec{x}\rangle_{loc}$ has delocalization factor $V^{-1}$, which cancels with the spatial sum $\sum_{\vec{x},\vec{y}}$ in the matrix element (by translation invariance). The remaining sum $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0}, \vec{y})$ converges absolutely by exponential clustering (rate $e^{-m|\vec{y}|}$) to a volume-independent limit for $L \gg 1/m$. This cancellation is proved, not asserted.

(b) The uniformity in $a$ of the convergence rate in $L$ is established because: (i) the exponential clustering rate $m$ is bounded below by $\Delta_0 > 0$, which is uniform in $a$ (proved in Sections 4-5); (ii) the connected matrix elements converge to their infinite-volume values at rate $e^{-mL}$, with $m$ uniform in $a$. Therefore $|\Delta(a,L) - \Delta(a,\infty)| \leq C e^{-mL}$ with $C$ and $m$ independent of $a$, providing the uniformity required for Moore-Osgood.

(c) The finite-volume spectral gap is bounded below uniformly in $L$. In finite volume, the spectrum is discrete and the "mass gap" is the gap between ground and first excited state. The cluster expansion gives exponential decay of connected correlators with rate $m \geq \alpha/a > 0$ uniformly in $L$ (Theorem 4(c)). This implies $\Delta_0(L) \geq c/a > 0$ uniformly in $L$ for each fixed $a$. As $L \to \infty$, $\Delta_0(L) \to \Delta_0(\infty)$ from above (the finite-volume gap is typically larger than the infinite-volume gap). The key point: the lower bound $\Delta_0(L) \geq c > 0$ is uniform in $L$, ensuring the thermodynamic and continuum limits can be interchanged.

**Impact on the claimed result:** None. The thermodynamic limit is handled rigorously via Moore-Osgood with explicit uniform bounds.
