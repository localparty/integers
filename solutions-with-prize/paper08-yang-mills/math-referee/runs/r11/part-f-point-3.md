## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Uniformity in $L$.**

The connected matrix element $\langle 1|E_k(0)|1\rangle_c$ is claimed to be volume-independent. The proof (Section 5.7(e), Volume Cancellation Lemma) is as follows:

The zero-momentum one-particle state is $|1\rangle = V^{-1/2} \sum_{\vec{x}} |\vec{x}\rangle_{\mathrm{loc}}$. The matrix element is:

$$\langle 1|E_k(0)|1\rangle = V^{-1} \sum_{\vec{x}, \vec{y}} \langle \vec{x}|E_k(0)|\vec{y}\rangle$$

By translation invariance, $\langle \vec{x}|E_k(0)|\vec{y}\rangle = f(\vec{x} - \vec{y})$ depends only on the difference. The sum over $\vec{x}$ gives $V$, cancelling the $V^{-1}$:

$$\langle 1|E_k(0)|1\rangle = \sum_{\vec{y}} f(-\vec{y}) = F(\vec{0})$$

By locality and exponential clustering (from the mass gap), $|f(\vec{y})| \leq C e^{-m|\vec{y}|}$ for $|\vec{y}|$ larger than the support radius $R_0$. The sum $F(\vec{0}) = \sum_{\vec{y}} f(-\vec{y})$ converges absolutely (with rate controlled by $e^{-m|\vec{y}|}$) to a volume-independent limit. For $L$ larger than the correlation length $\xi = 1/m$, the finite-$L$ and infinite-$L$ values differ by $O(e^{-mL})$.

This cancellation is standard in lattice QFT (it is the reason that intensive quantities like the free energy density are volume-independent). The argument is correctly stated and proved.

**(b) The infinite-volume mass gap.**

For fixed $a$, $\Delta(a, L) \to \Delta(a, \infty)$ as $L \to \infty$ by exponential clustering. The rate of convergence is $|\Delta(a, L) - \Delta(a, \infty)| \leq C(a) e^{-m(a)L}$ where $m(a) > 0$ is the correlation rate.

Uniformity in $a$: the RG analysis gives $\Delta(a) = C(a) \cdot \Lambda(a)$ where $C(a) = C_0 - \sum_{k=0}^{K(a)} \delta C_k$ converges as $K(a) = \log_2(1/a\Lambda) \to \infty$. The exponential clustering rate $m(a)$ is bounded below by $\Delta(a)/2$ (from the spectral gap). Since $\Delta(a) \to \Delta_\infty > 0$, $m(a)$ is bounded below uniformly in $a$ (for $a$ small enough). This gives uniform-in-$a$ convergence in $L$: $|\Delta(a, L) - \Delta(a, \infty)| \leq C e^{-(\Delta_\infty/2)L}$ for all $a$ small enough.

**(c) Exponential clustering in finite volume.**

On the periodic lattice $(\mathbb{Z}/L\mathbb{Z})^4$, the spectrum is discrete and the "mass gap" is the gap between ground state and first excited state. For $L$ large compared to the correlation length $\xi = 1/\Delta$, the finite-volume spectral gap differs from the infinite-volume mass gap by $O(e^{-\Delta L})$ (standard exponential finite-size correction).

The finite-volume spectral gap is bounded below uniformly in $L$ (for $L \geq L_0$) because: (i) the cluster expansion of Theorem 4 applies on the periodic lattice with volume-independent bounds; (ii) the exponential decay of connected correlators (with rate $m > 0$ independent of $L$) gives the spectral gap via the transfer matrix; (iii) the Kotecký-Preiss convergence is uniform in $L$ because the lattice animal constant $c_d$ and the polymer weights are $L$-independent.

For $L < L_0$ (small volumes), the spectral gap could be larger (finite-size effects push states up in energy) or could exhibit spurious degeneracies. However, the mass gap claim is about the infinite-volume theory, and the finite-volume spectral gap converges to it. The Moore-Osgood theorem then gives the commutation of limits $a \to 0$ and $L \to \infty$.

**Impact on the claimed result:** None. The thermodynamic limit is handled correctly using standard techniques from constructive QFT.
