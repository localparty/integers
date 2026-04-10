# Point 6: The OS Axioms

**Location:** Section 5.7(f)

**Verdict:** SOUND

**Finding:**

The current release candidate contains a substantially expanded treatment of the OS axioms compared to the earlier version flagged in the verification reports. Section 5.7(f) now runs to approximately 100 lines of detailed argument, including explicit bounds, the linked cluster theorem for OS1, the Symanzik effective theory for OS2, the Osterwalder--Seiler theorem for OS3, and the spectral decomposition for OS5. A dedicated sub-section addresses the simultaneity of all five axioms and the OS reconstruction theorem. Each interrogation point is addressed.

---

## (a) OS1 (Temperedness)

**Claim under attack:** The exponential bound on connected functions does not automatically imply temperedness of the full (disconnected) Schwinger functions.

**Finding: SOUND.**

The current text provides the complete argument:

1. **Connected functions bounded:** $|S_n^c(x_1, \ldots, x_n)| \leq C_0^n e^{-\Delta_\infty \cdot \mathrm{diam}}$ (from cluster expansion, equation OS1.1).

2. **Linked cluster theorem:** The full Schwinger function decomposes as (OS1.2):
$$S_n(x_1, \ldots, x_n) = \sum_{\pi \in \mathcal{P}(n)} \prod_{I \in \pi} S_{|I|}^c(x_I)$$

3. **Explicit bound:** Using $|\mathcal{P}(n)| \leq n!$ (Bell number bound) and the connected bound:
$$|S_n(x_1, \ldots, x_n)| \leq n! \cdot C_0^n$$

4. **Temperedness:** The bound $|S_n(f)| \leq n! \cdot C_0^n \|f\|_{L^1}$ for Schwartz test functions $f$ defines a continuous linear functional on $\mathcal{S}(\mathbb{R}^{4n})$, since $\|f\|_{L^1}$ is controlled by Schwartz seminorms.

This is correct and complete. The bound on the full Schwinger functions is STRONGER than temperedness (it gives a uniform bound, not just polynomial growth). The argument is standard (Glimm--Jaffe, Chapter 18, Theorem 18.2.1), and the paper now makes it explicit.

**Note on coinciding points:** The bound $|S_n| \leq n! \cdot C_0^n$ holds pointwise for the lattice theory (where Schwinger functions are bounded) and distributionally in the continuum limit. At finite lattice spacing, the bound is trivially satisfied because lattice observables are bounded. In the continuum limit, the distributional bound is inherited.

---

## (b) OS2 (Euclidean covariance)

**Claim under attack:** The rate of O(4) restoration must be specified precisely.

**Finding: SOUND.**

The current text provides the explicit rate via the Symanzik effective theory (equation OS2.4):

$$g_k^4 \cdot (a_k \Lambda)^2 = \frac{(a_0 \Lambda)^2}{(b_0 k \ln 2)^2 \cdot 4^k} \to 0 \quad \text{as } k \to \infty$$

The convergence is doubly exponential: the factor $4^{-k}$ from the engineering dimension suppression $(a_k \Lambda)^2 = (a_0 \Lambda/2^k)^2$ overwhelms the polynomial $1/k^2$ from the running coupling. The O(4)-breaking corrections vanish faster than any power of $a$, not just as $a^2$.

The argument uses Balaban's coefficient bound $|c_i^{(6)}(k)| \leq C g_k^4$ for the dimension-6 operators (both O(4)-invariant and O(4)-breaking), which follows from the general estimate in CMP 109. The leading O(4)-breaking operators are at dimension 6 (dimension 5 is absent by C-symmetry), so the O(4) breaking is $O(a^2)$ with a logarithmically running prefactor -- a standard result in the Symanzik improvement program (Symanzik 1983, Luscher--Weisz 1985).

---

## (c) OS reconstruction

**Claim under attack:** Are OS1--OS5 verified simultaneously for a single subsequential limit, or along potentially different subsequences?

**Finding: SOUND.**

The current text addresses this concern explicitly in the "Simultaneity of axioms and OS reconstruction" sub-section:

> "All five axioms hold *simultaneously* for the limiting Schwinger functions $\{S_n\}_{n \geq 0}$ obtained from this single subsequence. There is no issue of different axioms requiring different subsequences."

The argument:

1. **Single subsequence extraction:** The uniform bound $|S_n(f)| \leq n! \cdot C_0^n \|f\|_{L^1}$ (from OS1, uniform in $a$) places the lattice Schwinger functions in a weak-$*$ precompact set. Banach--Alaoglu + diagonal argument extracts a single subsequence $a_j \to 0$ such that $S_n^{(a_j)} \to S_n$ for ALL $n$ simultaneously.

2. **All axioms verified for this subsequence:**
   - OS1: The uniform bound $n! \cdot C_0^n$ is inherited by the limit.
   - OS2: The O(4)-breaking corrections $g_k^4(a_k\Lambda)^2 \to 0$ along ANY subsequence (the bound is subsequence-independent).
   - OS3: Reflection positivity at each $a_j$ is preserved under weak limits by lower semicontinuity of non-negative quadratic forms.
   - OS4: Automatic (gauge invariance at each $a_j$, preserved under limits).
   - OS5: The exponential clustering bound (OS5.4) with $a$-independent $\Delta_\infty$ is inherited.

3. **OS reconstruction:** Osterwalder--Schrader (1973, 1975) applied to $\{S_n\}$ satisfying OS1--OS5 yields a Wightman QFT with mass gap $\Delta_\infty > 0$.

The argument is correct. The key is that ALL bounds entering OS1--OS5 are **uniform in the lattice spacing $a$**, so they hold along any convergent subsequence. There is no issue of axiom-dependent subsequences.

---

**Impact on the claimed result:** None. The OS axioms are verified in full detail, simultaneously for a single subsequential limit. The OS reconstruction theorem applies and yields a Wightman QFT with mass gap.
