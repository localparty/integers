## Part F, Point 1: The OS Axioms — Simultaneous Verification

**Weight:** MEDIUM
**Verdict:** SOUND for the structural verification (each axiom checked individually); CLOSABLE GAP on coincident-point singularities for higher $n$-point functions.

**Finding:**

(a) **OS0' linear growth condition.** The bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ is established in §5.7(f), OS1 step. The "Lemma (OS0' verification)" then explicitly shows that the $L^1$ norm is dominated by a Schwartz seminorm:
$$\|f\|_{L^1} \leq \omega_{4n, M} \cdot p_M(f), \qquad M = 4n+1$$
with $p_M(f) = \sup_x (1+|x|)^M |f(x)|$. The seminorm index $N(n) = 4n+1$ is linear in $n$, satisfying OS0'. Sound.

The growth $C_n = n! C_0^n \omega_{4n, 4n+1}$ is acceptable for OS0' (the constraint is $C_n \leq A (n!)^B$ for some $B$, which holds with $B=1$). Sound.

(b) **The diagonal extraction.** The Banach–Alaoglu argument extracts a *single* subsequence $a_j \to 0$ such that $S_n^{(a_j)} \to S_n$ for all $n$ simultaneously. The diagonal argument over $n$ is standard and requires separability of $\mathcal{S}(\mathbb{R}^{4n})$ — explicitly cited (Reed–Simon Vol I, §V.3). Sound.

(c) **Coincident-point singularities.** The proof's handling is in §5.7(f) "Coincident-point singularities" paragraph. It argues:
- On the lattice, $S_n^{(a)}$ are bounded pointwise (compact group, bounded continuous functions).
- The lattice smeared $S_n^{(a)}(f)$ are well-defined for all Schwartz $f$, including test functions supported at coincident points.
- The continuum limit gives tempered distributions in $\mathcal{S}'(\mathbb{R}^{4n})$ via Banach–Alaoglu.
- "Coincident-point singularities are an artefact of the pointwise (unsmeared) representation."

The "Local integrability of $n$-point singularities" lemma estimates the worst-case coincident-point singularity as $\prod_{i<j} |x_i - x_j|^{-2} \cdot e^{-\Delta \cdot \mathrm{diam}}$ and argues integrability via dimension counting. The proof works for $n \leq 4$ directly; for $n \geq 5$, "simultaneous collision of all $n$ points has measure zero" and the integral is controlled by partial collisions.

**This is plausible but not airtight.** The bound $|S_n(x_1, \ldots, x_n)| \leq C^n n! \prod_{i<j} (1 + |x_i - x_j|^{-2}) e^{-\Delta \mathrm{diam}}$ is *asserted* without derivation. For a confining gauge theory with a mass gap, the singularity structure of the Schwinger functions is constrained by the spectrum (Källén–Lehmann for the 2-point function gives the milder $|x|^{-2}$ singularity for the leading term, plus possibly stronger singularities from anomalous dimensions of composite operators). The preprint's claim "for gauge-invariant operators in a massive theory, the OPE gives $|S_n| \leq C^n n! \prod |x_i - x_{i+1}|^{-2}$" appeals to an OPE that has not been constructed (see Point G4).

The handling is sound at the level of "tempered distribution" but does not establish the full UV singularity structure. For Clay purposes (which require an OPE with prescribed local singularities, see Point G4), this is insufficient.

(d) **Uniformity in $a$.** The bound $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ is claimed uniform in $a$ because $C_0$ is the cluster-expansion constant which is $a$-independent in the cluster-expansion regime. But the cluster-expansion regime is restricted to $\beta < a/(2\sqrt{N} r_3)$, which becomes very narrow as $a$ shrinks. For $a \to 0$, the cluster expansion ceases to apply (see Section 4.3 "Regime C"), and the bound must be supplied by Balaban's RG. The uniformity in $a$ then depends on Balaban's analyticity radius being uniform in the bare scale — which is the K-vs-k issue restated.

**Impact on the claimed result:** The OS0'–OS5 verification is structurally correct, but two issues remain:
1. The $a$-uniformity in the small-$a$ regime depends on Point C1 (the K-vs-k separation).
2. The coincident-point singularity structure is asserted, not derived. For Clay, this matters because Jaffe–Witten requires an OPE with prescribed local singularities (Point G4).

CLOSABLE in principle, but the closure depends on resolving the K-vs-k issue and constructing the OPE.
