## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The small-field condition.**

The small-field region $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$ with $p(g_k) = g_k^{1-\epsilon}$ is a standard feature of Balaban's construction. The exponent $\epsilon > 0$ is a fixed constant (chosen once at the start of the construction, typically $\epsilon = 1/4$ or similar). It does not depend on $k$.

The polymer expansion, analyticity properties (B1)-(B2), and the dimension-6 operator classification are all established within $\Omega_s$. This is correct: Balaban's convergent expansion applies only in the small-field region. The preprint's arguments (operator extraction, Taylor expansion, dimension classification) all operate within $\Omega_s$, where the effective action is analytic and has convergent Taylor series.

In $\Omega_l$ (the large-field region), the effective action is not analytic and the operator classification does not apply in the Taylor expansion sense. However, the contribution from $\Omega_l$ is exponentially suppressed — this is handled in Part III.5 of Section 5.6.

**(b) Large-field suppression.**

The large-field contribution is bounded by $O(e^{-c/g_k^{2\epsilon}})$ (Section 5.6, Part III.5). With $\epsilon = 1/4$, this is $O(e^{-c/g_k^{1/2}})$. On the asymptotically free trajectory, $g_k^2 \sim 1/(b_0 k \ln 2)$, so:

$$e^{-c/g_k^{2\epsilon}} = e^{-c (b_0 k \ln 2)^{1/(2\times 1/4)}} = e^{-c (b_0 k \ln 2)^2}$$

Meanwhile, $g_k^4 \hat{\Delta}_k^2 \sim (b_0 k \ln 2)^{-2} \cdot 4^{-k}$, which decays doubly exponentially. The large-field contribution decays as $e^{-c k^2}$ (Gaussian in $k$), which is faster than any power of $k$ but slower than $4^{-k}$. So the large-field contribution is NOT negligible compared to $g_k^4 \hat{\Delta}_k^2$ for small $k$.

However, for the RG recursion, what matters is the total single-step contribution to the mass gap shift. The small-field contribution is $O(g_k^4 \hat{\Delta}_k^2)$. The large-field contribution is $O(e^{-c/g_k^{2\epsilon}})$. Since the mass gap shift at step $k$ is $\delta \Delta_k / \Delta_k$, the large-field contribution gives:

$$\frac{\delta \Delta_k^{\mathrm{large}}}{\Delta_k} \leq C e^{-c/g_k^{2\epsilon}}$$

On the AF trajectory, for $k$ large enough that $g_k^2 \ll 1$: $e^{-c/g_k^{2\epsilon}} \ll g_k^4 \hat{\Delta}_k^2$ because $e^{-c/g_k^{2\epsilon}}$ decays faster than any power of $g_k$ while $g_k^4 \hat{\Delta}_k^2$ is a polynomial in $g_k$ times an exponential in $k$. For the first few steps where $g_k = O(1)$, the large-field contribution is $O(e^{-c})$ (a finite constant), and the mass gap shift from the cluster expansion is $O(1)$, so both are $O(1)$ and the recursion handles them via the starting constant $C_0$.

The sum $\sum_k e^{-c/g_k^{2\epsilon}}$ converges because $g_k \to 0$ and the terms decay super-polynomially. This is verified.

**(c) Gauge invariance of the decomposition.**

The condition $|F_{\mu\nu}| < p(g_k)$ is gauge-invariant if $F_{\mu\nu}$ is the gauge-invariant field strength. In Balaban's construction, $F_{\mu\nu}$ is the lattice plaquette variable $s_P = \mathrm{Re}\,\mathrm{Tr}(\mathbf{1} - U_P)/N$, which is gauge-invariant. The small-field/large-field decomposition based on $s_P < p(g_k)$ is therefore gauge-invariant.

Balaban uses axial gauge as a computational device within each region, but the decomposition itself respects gauge invariance. The axial gauge fixing does not affect the definition of $\Omega_s$ and $\Omega_l$.

**Impact on the claimed result:** None. The large-field/small-field decomposition is standard in Balaban's program, and the contributions from $\Omega_l$ are properly controlled.
