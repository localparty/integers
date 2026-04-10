## Part F, Point 3: The Thermodynamic Limit

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP (volume-cancellation lemma is correct; but the joint $a \to 0, L \to \infty$ limit is conditional on the K-vs-k issue from Point C1, and the "$L_{\max} \sim e^{m_1 a/2}$" implicit bound from Theorem 5 is not made explicit)

**Finding:**

(a) **Uniformity in $L$.** §5.7(e) "Lemma (Volume cancellation)" proves that the connected matrix element $\langle 1|E_k(0)|1\rangle_c$ is volume-independent for $L \gg 1/m$ (with $m$ the clustering rate). The proof uses translation invariance and exponential clustering: the spatial sum factor $1/V$ from the zero-momentum normalization cancels with the spatial sum in $E_k(0)$, leaving a volume-independent quantity.

The "Finite-volume correction" paragraph then bounds the residual $|F(\vec 0; L) - F(\vec 0; \infty)| \leq C' e^{-mL}$ via the periodic-image construction. Sound.

The "Clarification of the mass parameter $m$" paragraph addresses the circularity (using $\Delta_\infty > 0$ to bound the clustering mass that proves $\Delta_\infty > 0$) by:
1. Establishing the RG sum convergence in infinite volume first.
2. Using $\Delta_\infty > 0$ to bound the clustering mass uniformly.

This is correct in structure but the "infinite volume first" step relies on the *mass-gap-shift sum* converging in infinite volume *without* prior knowledge of the gap. This sum is the same one that has the K-vs-k issue (Point C1, E1, E2). So the volume-cancellation argument is *modulo* resolving the K-vs-k notation.

(b) **The infinite-volume mass gap.** For fixed $a$, $\Delta(a, L) \to \Delta(a, \infty)$ as $L \to \infty$ by exponential clustering (Section 4). The rate is $O(e^{-m(a) L})$ with $m(a)$ the clustering rate at lattice spacing $a$. Sound.

The joint limit requires $m(a) L \to \infty$ uniformly in $a$, which means $L$ must grow faster than $1/m(a)$ shrinks as $a \to 0$. Since $m(a)$ scales as $\Delta_0 / a$ (the *physical* mass gap is $a$-independent, but $m(a)$ in lattice units is $\Delta_0 a$), we need $L \gg 1/(a \Delta_0)$. As $a \to 0$, this means $L \to \infty$ at least as fast as $1/a$. The preprint addresses this in §5.7(e) item (ii) but does not give explicit rate constraints.

(c) **Exponential clustering in finite volume.** The cluster expansion of Section 4 holds for any periodic lattice $L \geq 1$ with uniform constants in $L$. So the clustering rate $m(a, L) \to m(a, \infty) > 0$ as $L \to \infty$ uniformly. The finite-volume "spectral gap" (between ground and first excited state of the finite-volume transfer matrix) is bounded below by the cluster-expansion clustering rate. Sound.

(d) **Moore–Osgood for the joint limit.** §5.7(e) invokes Moore–Osgood: uniform convergence in $L$ as $k \to \infty$ + pointwise convergence in $k$ as $L \to \infty$ ⇒ commuting limits. The uniformity in $L$ is item (i), pointwise in $k$ is item (ii). The argument is correct in principle.

**The catch:** "uniform in $L$ as $k \to \infty$" is exactly the uniformity that depends on the K-vs-k separation. The form-factor recursion is volume-independent (by the cancellation lemma), so $C_K(L) = C_K(\infty) + O(e^{-mL})$, and the RG sum converges uniformly in $L$ (modulo the K-vs-k issue). Granted Point C1, this is closable.

**Impact on the claimed result:** The thermodynamic limit is correctly handled *given* the resolution of the K-vs-k issue. The volume-cancellation lemma is valid and provides $L$-independence of the form factor. The Moore–Osgood commutation is sound under the corrected convention.

This addresses Clay item C11 (volume-uniform mass gap) at the structural level. The actual *rigorous* propagation of the gap to the $L \to \infty$ limit depends on the §5.4 recursion converging — which depends on Point C1.
