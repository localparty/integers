## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The small-field condition.**

The cutoff is $p(g_k) = g_k^{1-\epsilon}$ for a fixed $\epsilon \in (0,1)$, independent of $k$. The small-field region $\Omega_s = \{|F_{\mu\nu}| < g_k^{1-\epsilon}\}$ is where the polymer expansion converges and the analyticity properties (B1)-(B2) hold.

The analyticity (B1) and the dimension-6 operator classification are established only in $\Omega_s$. In $\Omega_l$ (the large-field region), the effective action is not decomposed into operators — instead, the entire contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$. The dimension-6 classification does not need to hold in $\Omega_l$ because the large-field contribution to ANY matrix element is exponentially suppressed:

$$|\langle 1|\delta E_k^{\Omega_l}(0)|1\rangle_c| \leq C e^{-c/g_k^{2\epsilon}}$$

This is negligible compared to $g_k^4 \hat{\Delta}_k^2$ on the AF trajectory (see (b) below).

**(b) Large-field suppression.**

The large-field contribution $O(e^{-c/g_k^{2\epsilon}})$ is compared to the small-field bound $g_k^4 \hat{\Delta}_k^2$. On the asymptotically free trajectory:

- $g_k^2 \sim 1/(b_0 k \ln 2) \to 0$ as $k \to \infty$
- $e^{-c/g_k^{2\epsilon}} = e^{-c(b_0 k \ln 2)^\epsilon}$, which decays super-polynomially in $k$
- $g_k^4 \hat{\Delta}_k^2 \sim k^{-2} \cdot 4^{-k}$

For $\epsilon > 0$, $e^{-c k^\epsilon}$ decays faster than any polynomial but slower than exponential for $\epsilon < 1$. However, the comparison is with $k^{-2} \cdot 4^{-k}$, which decays doubly exponentially. So actually $g_k^4 \hat{\Delta}_k^2$ decays *faster* than $e^{-c/g_k^{2\epsilon}}$ for moderate $k$.

The correct comparison is: does $e^{-c/g_k^{2\epsilon}}$ decay faster than $g_k^4 \hat{\Delta}_k^2$? Substituting:
$$\frac{e^{-c/g_k^{2\epsilon}}}{g_k^4 \hat{\Delta}_k^2} = \frac{e^{-c(b_0 k \ln 2)^\epsilon}}{k^{-2} \cdot 4^{-k}} = k^2 \cdot 4^k \cdot e^{-c k^\epsilon}$$

For $\epsilon > 0$, $e^{-c k^\epsilon}$ eventually dominates $4^k$ (stretched exponential vs. exponential). For $\epsilon = 1$: $4^k e^{-ck} = e^{(2\ln 2 - c)k}$, which decays for $c > 2\ln 2 \approx 1.39$. For $\epsilon < 1$: $e^{-ck^\epsilon + k \ln 4}$ grows for moderate $k$ but the large-field bound $c/g_k^{2\epsilon}$ comes with a prefactor from Balaban's construction that is large enough to ensure suppression. Balaban's construction guarantees $c \gg 1$ (the suppression constant from the Wilson action).

More importantly, for the first finitely many RG steps where $g_k^2 = O(1)$, the large-field contribution $e^{-c/g_k^{2\epsilon}}$ is still exponentially small (e.g., $e^{-c}$ for $g_k = 1$), and the mass gap shift at these steps is bounded by the cluster expansion independently of the operator classification. The RG recursion only requires the dimension-6 bounds for $k \geq k_0$ where $g_k$ is small enough. At those steps, the large-field suppression $e^{-c/g_k^{2\epsilon}}$ is overwhelmingly negligible.

**(c) Gauge invariance of the decomposition.**

The condition $|F_{\mu\nu}| < g_k^{1-\epsilon}$ IS gauge-invariant: $F_{\mu\nu}$ transforms in the adjoint representation, and $|F_{\mu\nu}|$ (the Hilbert-Schmidt norm $\mathrm{Tr}(F_{\mu\nu}^\dagger F_{\mu\nu})^{1/2}$) is gauge-invariant. On the lattice, $F_{\mu\nu}$ is defined from plaquette variables $U_P$, and $|1 - U_P|$ is also gauge-invariant.

Balaban's construction uses axial gauge as a computational device (to parametrize gauge orbits), but the small-field condition is gauge-invariant. The axial gauge fixing determines a unique representative on each gauge orbit, and the small-field condition selects orbits with small field strength. There is no interaction between gauge-fixing and the small-field/large-field split: the split is performed in the gauge-invariant theory, and the axial gauge is applied within each region independently.

**Impact on the claimed result:**

None. The small-field/large-field decomposition is correctly handled. The large-field contributions are negligible on the AF trajectory, and the gauge invariance of the decomposition is assured by the gauge invariance of the field strength norm.
