## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

The claim is that the limits $a \to 0$ and $L \to \infty$ commute, via the Moore–Osgood theorem.

**(a) Uniformity in $L$.** The bound $|C_{K+1}(L) - C_K(L)| \leq C' g_K^4 (a_K \Lambda)^s$ is claimed volume-independent. The connected matrix element $\langle 1|E_K(0)|1\rangle_c$ involves the zero-momentum one-particle state $|1\rangle$, which is delocalized over spatial volume $L^3$ with normalization $1/L^{3/2}$. The spatial sum in $E_K(0) = \sum_x E_K(x)$ over the lattice gives a factor proportional to $L^3$ (translation invariance makes each term equal). The delocalization factor $1/L^{3/2}$ from each bra and ket cancels with the volume factor, leaving a $L$-independent result. This is the standard cluster expansion argument: $\langle 1|\sum_x E_K(x)|1\rangle_c = L^3 \langle 1|E_K(0)|1\rangle_c$ and $|1\rangle$ has normalization such that the $L^3$ cancels.

The Hastings–Koma clustering bound (Section 5.5.3 Step 3(i)) makes this cancellation rigorous: the connected correlator decays exponentially with distance, so the spatial sum converges to a volume-independent limit.

**Gap:** The paper should state more explicitly that $\langle 1|E_K(0)|1\rangle_c$ is the connected matrix element per site (not the total), and that the volume cancellation is exact by translation invariance + clustering. The argument is correct but could be more explicit.

**(b) The infinite-volume mass gap.** For fixed $a$, the mass gap $\Delta(a, L)$ converges to $\Delta(a, \infty)$ as $L \to \infty$ by exponential clustering (Section 4). The rate of convergence in $L$ is controlled by the correlation length $\xi(a)$: $|\Delta(a, L) - \Delta(a, \infty)| \leq C e^{-L/\xi(a)}$. For this to be uniform in $a$, we need $\xi(a)$ bounded above uniformly as $a \to 0$.

On the AF trajectory, $\xi(a) = 1/\Delta_{\mathrm{phys}}$ (the physical correlation length), which is $a$-independent. So the convergence rate in $L$ is indeed uniform in $a$: both are controlled by the physical mass gap $\Delta_{\mathrm{phys}} > 0$.

**Gap:** The uniformity in $a$ of the $L$-convergence rate should be stated as a consequence of $\Delta_{\mathrm{phys}}$ being $a$-independent on the AF trajectory. This is implicit in the paper's argument but deserves a sentence.

**(c) Exponential clustering in finite volume.** In finite volume $(\mathbb{Z}/L\mathbb{Z})^4$, the spectrum is discrete and the "mass gap" is the gap between ground and first excited state. This converges to the infinite-volume gap as $L \to \infty$, with corrections $O(e^{-L\Delta_{\mathrm{phys}}})$. The finite-volume spectral gap is bounded below by $\Delta_{\mathrm{phys}} - C e^{-L\Delta_{\mathrm{phys}}} > 0$ for $L \geq L_0(\Delta_{\mathrm{phys}})$, uniformly in $a$. For $L < L_0$, the finite-volume gap could in principle vanish, but the cluster expansion bound $\Delta_0 \geq \alpha/a$ (Theorem 4, part (c)) provides a volume-uniform lower bound at the bare scale.

Closable in **1 paragraph**: state the finite-volume spectral gap bound explicitly and verify the Moore–Osgood uniformity conditions.

**Impact on the claimed result:**
Minor impact on (ii) subsidiary claims about the double limit. The mass gap $\Delta_\infty > 0$ is not affected; only the explicit construction of the infinite-volume theory requires the uniformity argument.
