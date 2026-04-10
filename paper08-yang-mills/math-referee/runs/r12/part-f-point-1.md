## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** SOUND (axioms OS1–OS5 individually); CLOSABLE GAP (simultaneity argument)

---

**Finding:**

**(a) OS0' linear growth condition.** The preprint verifies OS0' explicitly in Section 5.7(f) via the "Lemma (OS0' verification)": $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ satisfies OS0' because $\|f\|_{L^1} \leq \omega_{4n} p_{4n+1}(f)$ where $p_M(f) = \sup_x (1+|x|)^M |f(x)|$ is a Schwartz seminorm. The inequality $\|f\|_{L^1} \leq \omega_{4n} p_{4n+1}(f)$ holds with $\omega_{4n} = \int (1+|x|)^{-(4n+1)} d^{4n}x < \infty$ for $M = 4n+1 > 4n$.

This is a standard estimate (Reed–Simon, Vol. I; Schwartz space embeds into $L^1$). The proof is explicit and correct. The $L^1$ norm is dominated by the Schwartz seminorm $p_{4n+1}$, so OS0' is satisfied with $C_n' = n! C_0^n \omega_{4n}$ and $N(n) = 4n+1$. SOUND.

**(b) The diagonal extraction and separability.** Section 5.7(f) addresses this: "The Schwartz space $\mathcal{S}(\mathbb{R}^{4n})$ is separable (it is a Fréchet space with countable seminorm family; see Reed–Simon, Vol. I, Section V.3), so weak-$*$ precompact subsets are weak-$*$ sequentially precompact. A diagonal argument over $n = 1, 2, 3, \ldots$ extracts a subsequence $a_j \to 0$ such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously."

Separability is explicitly stated and cited. The diagonal argument is standard and correctly applied. The simultaneous convergence for all $n$ requires the double diagonalization: at each stage, extract a subsequence that works for $n = 1, \ldots, N$, then take the diagonal. This is exactly what the preprint describes. SOUND.

**(c) Coincident-point singularities.** Section 5.7(f) addresses this: "On the lattice, all Schwinger functions are bounded pointwise (the gauge fields take values in the compact group SU($N$)). In the continuum limit, the Schwinger functions are distributions... The distributional nature handles UV singularities at coincident points automatically. For the massive gapped theory, the Källén-Lehmann representation gives two-point singularities of the form $|x-y|^{-2} e^{-\Delta|x-y|}$ (up to logarithms), which are locally integrable in $d=4$."

The local integrability lemma is explicitly proved: $\phi(x) = |x|^{-2} e^{-\Delta|x|}$ is integrable near $r=0$ because $\int_0^\epsilon r^{-2} r^3 dr = C\epsilon^2/2 < \infty$. This handles the leading UV singularity.

However, this argument is only for the two-point function. For higher $n$-point Schwinger functions, the UV singularities at coincident points can be more severe (e.g., multi-coincident limits). The preprint does not address these higher-order singularities explicitly. For a massive gapped theory, all UV singularities are expected to be mild (the massive propagator gives better UV behavior than the massless case), but "expected" is not "proved" for general $n$.

The standard OS reconstruction theorem requires only that the $S_n$ are tempered distributions, which is guaranteed by the OS1 temperedness bound (established in the preprint). The distributional interpretation handles coincident-point singularities automatically without needing pointwise bounds. CLOSABLE GAP: the preprint should state explicitly that the OS1 bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ is sufficient to define $S_n$ as tempered distributions and that the OS reconstruction theorem works at this level of regularity, without requiring pointwise bounds at coincident points. Difficulty: **1 sentence** plus citation of the OS theorem statement.

**Simultaneity of axioms.** Section 5.7(f) closes: "All five axioms hold *simultaneously* for the limiting Schwinger functions $\{S_n\}$ obtained from this single subsequence. There is no issue of different axioms requiring different subsequences: a single subsequence serves for all." The argument is: the Banach-Alaoglu extraction works for OS1 (temperedness), and the other axioms (OS2: O(4)-breaking corrections vanish uniformly; OS3: reflection positivity is a pointwise property for each $a$; OS4: manifest; OS5: from $\Delta_\infty > 0$) are all verified uniformly in $a$ or as pointwise properties, so they carry over to the limit without needing further subsequence selection. This is correct. SOUND.

**Impact on the claimed result:** Sub-point (c) (coincident-point singularities for general $n$) is a minor gap in the OS1 verification for multi-point functions. For the Clay Prize, a complete proof requires that all $S_n$ are tempered distributions simultaneously; the OS1 bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ guarantees this for all $n$, so the gap is presentational. The OS axioms are simultaneously verified for one subsequential limit.
