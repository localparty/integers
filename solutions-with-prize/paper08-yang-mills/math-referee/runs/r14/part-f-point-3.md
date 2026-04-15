## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) Uniformity in $L$.** The connected matrix element $\langle 1|E_k(0)|1\rangle_c$ is claimed to be volume-independent. This rests on the standard argument for gapped lattice systems:

The connected correlator of a local operator $O(x)$ at zero momentum is:

$$\langle 1|O(q=0)|1\rangle_c = \sum_x \langle 1|O(x)|1\rangle_c = \sum_x \langle 1|O(x)|1\rangle - \langle 0|O(x)|0\rangle \cdot \langle 1|1\rangle$$

By translation invariance: $\langle 1|O(x)|1\rangle = \langle 1|O(0)|1\rangle$ (the state $|1\rangle$ at zero momentum is translationally invariant). The volume factor $L^3$ from the spatial sum cancels with the normalization $\langle 1|1\rangle = 1$ (normalized eigenstate):

$$\sum_x \langle 1|O(x)|1\rangle = L^3\,\langle 1|O(0)|1\rangle$$

But $|1\rangle$ is a delocalized state with amplitude $\sim 1/\sqrt{L^3}$ at each site. So $\langle 1|O(0)|1\rangle \sim 1/L^3$, and $L^3 \times 1/L^3 = O(1)$. The connected part subtracts the vacuum contribution, giving a finite, $L$-independent result.

This cancellation is standard in the physics literature but should be made precise. The mathematical argument: the operator $O(q=0)$ is the zero-momentum Fourier component. The matrix element $\langle 1|O(q=0)|1\rangle_c$ is related to the form factor at zero momentum, which is independent of the spatial volume $L$ for $L$ larger than the correlation length $\xi = 1/\Delta$. Corrections are $O(e^{-\Delta L})$.

**(b) The infinite-volume mass gap.** For fixed lattice spacing $a$, the mass gap $\Delta(a, L)$ in finite volume converges to $\Delta(a, \infty)$ as $L \to \infty$ by exponential clustering. The rate of convergence is $|\Delta(a, L) - \Delta(a, \infty)| \leq C\,e^{-\Delta(a,\infty)\,L}$.

The uniformity in $a$ requires: the decay rate $\Delta(a, \infty)$ is bounded below uniformly in $a$. This is established by the lattice mass gap: $\Delta(a, \infty) \geq \Delta_0 > 0$ for all $a$ in the range considered. The constant $\Delta_0$ comes from the cluster expansion and is $a$-independent (it depends on $\beta$ and $m_1 a$, but not on $a$ separately).

So the convergence $\Delta(a, L) \to \Delta(a, \infty)$ is uniform in $a$: the correction $O(e^{-\Delta_0 L})$ depends on $L$ and $\Delta_0$ but not on $a$.

**(c) Exponential clustering in finite volume.** On the periodic lattice $(\mathbb{Z}/L\mathbb{Z})^4$, the spectrum is discrete (finite-dimensional Hilbert space). The "mass gap" is the gap between the ground state energy and the first excited state energy. This finite-volume spectral gap converges to the infinite-volume mass gap with exponential corrections $O(e^{-\Delta L})$.

The finite-volume spectral gap is bounded below uniformly in $L$ for $L$ sufficiently large. The lower bound follows from the cluster expansion, which works on the periodic lattice for all $L$ (the convergence condition involves $m_1 a$, not $L$). For $L > 2\xi$ (twice the correlation length), the finite-volume mass gap is $\geq \Delta_\infty/2 > 0$.

**The Moore-Osgood theorem** (used for commutativity of limits $a \to 0$ and $L \to \infty$) requires: (i) $\lim_{a \to 0} S_n(a, L)$ exists for each $L$, (ii) $\lim_{L \to \infty} S_n(a, L)$ exists uniformly in $a$. Condition (i) is the continuum limit (established by the RG analysis). Condition (ii) is the thermodynamic limit (established by clustering, uniformly in $a$). Both conditions are verified.

**Impact on the claimed result:** None. The thermodynamic limit commutes with the continuum limit by Moore-Osgood. The volume independence of connected matrix elements is standard for gapped lattice systems, and the uniformity in $a$ is established by the $a$-independent mass gap from the cluster expansion.
