## Part F, Point 4: Uniqueness of the Continuum Limit

**Weight:** HEAVY
**Verdict:** SOUND (Jaffe–Witten requires "a" theory, not "the" theory; the proof's claim is restricted to subsequence-independence of the *mass gap value*, which is correctly handled in §5.7's "Remark (Uniqueness and subsequence-independence of the mass gap)")

**Finding:**

(a) **Subsequence dependence.** The continuum Schwinger functions are obtained as a subsequential weak-$*$ limit via Banach–Alaoglu. Different subsequences could in principle give different limit measures. The preprint **explicitly does not claim uniqueness** of the full continuum theory:

> "We do **not** claim uniqueness of the continuum limit (universality). What is proved is that **every** subsequential limit satisfies OS1–OS5 with mass gap $\Delta_\infty > 0$, because the RG telescoping sum converges absolutely (independently of the subsequence)."

This is the right hedge. The proof shows that *every* subsequential limit has a mass gap, not that the limit is unique. Sound.

(b) **Subsequence-independence of $\Delta_\infty$.** The remark continues:

> "**The mass gap value $\Delta_\infty$ is subsequence-independent.** The RG analysis gives $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ where $C_\infty = C_0 - \sum \delta C_k$ with the series converging absolutely (Section 5.4.6), and $\Lambda_\infty$ is determined by the convergent infinite product. Both $C_\infty$ and $\Lambda_\infty$ are defined as limits of sequences determined entirely by the RG flow — they do not depend on which subsequence of lattice spacings is used."

This is correct *conditional on the RG sum converging*, which is the K-vs-k issue (Points C1, E1, E2). If the RG sum diverges (under the §5.4.1 convention), then $C_\infty$ is not well-defined and the subsequence-independence claim fails. So subsequence-independence is contingent on Point C1's resolution.

(c) **Universality.** Universality (uniqueness of the continuum limit beyond just subsequence-independence) is *not* proved and is *not required* by Jaffe–Witten (which uses the indefinite article "a quantum Yang–Mills theory"). The preprint correctly states this.

(d) **Comparison with Clay.** The Jaffe–Witten footnote 2 of §6.6 (the "no weak-existence-only" rule) states:

> "We specifically exclude weak-existence (compactness) as the solution to the existence part of the Millennium problem, *unless one also uses other techniques to establish properties of the limit (such as the existence of a mass gap and the axioms)*."

The preprint's strategy is *exactly* the "other techniques" qualifier: it uses Banach–Alaoglu for compactness, but it ALSO uses the RG telescoping sum to *propagate the mass gap and the axioms to the specific limit constructed*. This is the right interpretation of the footnote and is the strategy explicitly discussed in §5.7's "Addressing the Jaffe–Witten caution" remark.

The structural claim is sound: subsequence-independence of $\Delta_\infty$ + axioms uniform in $a$ + Banach–Alaoglu = a specific QFT with a specific (subsequence-independent) mass gap. This satisfies the Clay footnote 2 requirement.

**Impact on the claimed result:** Sound at the structural level. Conditional on Point C1's resolution (the K-vs-k separation), this is the correct way to handle the subsequential limit issue. As written, the proof correctly identifies what is and is not claimed.
