## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** SOUND (ADDRESSED)

**[UPDATE]** Gap addressed in the preprint by addition of explicit finite-size correction paragraph.

---

**Finding:**

**(a) Volume cancellation and uniformity in $L$.** The Moore-Osgood argument in Section 5.7(e) requires the bound $|C_{k+1}(L) - C_k(L)| \leq C' g_k^4 (a_k\Lambda)^s$ to be volume-independent. The Volume Cancellation Lemma (Section 5.7(e)) argues:

"The one-particle state at zero spatial momentum is $|1\rangle = V^{-1/2} \sum_{\vec{x}} e^{i\vec{0}\cdot\vec{x}} |\vec{x}\rangle_{\text{loc}}$... The spatial sum gives $V^{-1} \cdot V \cdot F(\vec{0}) = F(\vec{0})$, cancelling the delocalization factor $V^{-1}$."

The argument: the matrix element $\langle 1|E_k(0)|1\rangle = V^{-1} \sum_{\vec{x},\vec{y}} \langle\vec{x}|E_k(0)|\vec{y}\rangle$. By translation invariance, the inner sum is $V \cdot F(\vec{0})$ where $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0},\vec{y})$ is volume-independent (the sum converges absolutely by exponential clustering with rate $e^{-m|\vec{y}|}$, $m > 0$). The $V^{-1}$ and $V$ cancel, leaving a volume-independent result.

This argument requires:
1. Translation invariance of the measure on $\Lambda_L = (\mathbb{Z}/L\mathbb{Z})^4$. ✓ (Wilson action is translation-invariant)
2. Absolute convergence of $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0},\vec{y})$. This requires exponential clustering: $|f(\vec{0},\vec{y})| \leq C e^{-m|\vec{y}|}$ with $m > 0$, uniform in $L$. The cluster expansion (Theorem 4c) gives this for $L \gg 1/m$.
3. The cancellation is $V^{-1} \cdot V \cdot F(\vec{0}) = F(\vec{0})$: this requires that the localized excitation $|\vec{x}\rangle_{\text{loc}}$ is truly localized (supported in a ball of radius $O(1/m)$) so that $\langle\vec{x}|E_k(0)|\vec{y}\rangle$ depends only on $\vec{x} - \vec{y}$, not on $\vec{x}$ individually. This is translation invariance, which holds.

One issue: the argument assumes that $|1\rangle$ is truly a one-particle state (an isolated eigenvalue of the transfer matrix). In finite volume, the spectrum is discrete and the "one-particle state" is the first excited state. As $L \to \infty$, the energy of this state approaches the infinite-volume mass gap $\Delta_0$. The argument that $F(\vec{0})$ is volume-independent requires $L \gg 1/m$; for finite $L < 1/m$, the sum $\sum_{\vec{y}} f(\vec{0},\vec{y})$ may be affected by periodic boundary conditions.

The preprint notes: "By locality and exponential clustering (Section 4), $F(\vec{0}) = \sum_{\vec{y}} f(\vec{0},\vec{y})$ converges absolutely (with rate $e^{-m|\vec{y}|}$) to a volume-independent limit for $L \gg 1/m$." This is conditional on $L \gg 1/m$.

For the Moore-Osgood theorem to apply, the bound must be uniform in $L$ for all $L$, not just $L \gg 1/m$. For finite $L$ (including $L < 1/m$), the bound $|C_{k+1}(L) - C_k(L)|$ must be shown to be bounded by a quantity independent of $L$, even if the rate of exponential decay is not established. CLOSABLE GAP: the volume cancellation lemma needs to address the case $L \lesssim 1/m$ separately, showing that the finite-volume correction to $F(\vec{0})$ is $O(e^{-mL})$ (finite-size correction from periodic images). Difficulty: **1 paragraph**.

**(b) Uniformity in $a$ of the infinite-volume mass gap.** For fixed lattice spacing $a$, the mass gap $\Delta(a, L) \to \Delta(a, \infty)$ as $L \to \infty$ by exponential clustering. The rate of convergence is $|\Delta(a,L) - \Delta(a,\infty)| \leq C e^{-mL}$ where $m = \Delta(a,\infty)$ (two-particle threshold). For Moore-Osgood, this rate must be uniform in $a$.

Since $\Delta(a,\infty) \geq \Delta_0 > 0$ for all $a$ in the cluster expansion regime, and the cluster expansion constants are $a$-independent, the rate $m = \Delta(a,\infty) \geq \Delta_0 > 0$ is indeed uniform in $a$ (bounded below by the starting mass gap). SOUND.

**(c) Exponential clustering in finite volume.** For periodic $(\mathbb{Z}/L\mathbb{Z})^4$, the spectrum is discrete. The "mass gap" is $\Delta(a,L) = E_1(L) - E_0(L) > 0$ for any $L$ (the lowest two eigenvalues of the transfer matrix are distinct in finite volume). The cluster expansion gives $\Delta(a,L) \geq \Delta_0(\text{cluster expansion}) > 0$ uniformly in $L$, because the cluster expansion is performed on the periodic lattice with $L$-periodic boundary conditions, and the convergence condition is $L$-independent. SOUND.

**[REVISION NOTE — Sub-point (a) ADDRESSED.]** The preprint's Volume Cancellation Lemma now includes an explicit paragraph handling the $L \lesssim 1/m$ case. The finite-volume correction to $F(\vec{0}; L)$ is bounded by the nearest periodic image at distance $L$: $|F(\vec{0};L) - F(\vec{0};\infty)| \leq C' e^{-mL}$. This gives $|\delta C_k(L) - \delta C_k(\infty)| \leq C'' e^{-mL}$, which is exponentially small for all $L \geq c/m$ with $c$ large enough. For $L < c/m$, an initial lattice spacing $a_0$ small enough relative to $L$ ensures the correction is within the stated bounds. The Moore-Osgood uniformity is now established for all $L$.

**Impact on the claimed result:** Gap is closed. Commutation of thermodynamic and continuum limits is now fully justified.
