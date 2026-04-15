## Part C, Point 1: Balaban's UV Stability — Precise Scope

**Weight:** HEAVY
**Verdict:** **GENUINE GAP** — The K-vs-k notation collision in §§5.1, 5.4, 5.7 makes the "Balaban as black box" framework internally inconsistent: §5.1.2 and §5.4.1 use $a_k = 2^k a_0$ (Balaban's *coarsening* convention), while §5.4.6 and §5.7(b) use $\hat\Delta_k^2 \sim 4^{-k}$ and $a_k = a_0/2^k$ (the *refining* convention required for continuum-limit convergence). These are *contradictory*: the doubly-exponential convergence of the RG sum requires the refining interpretation, but the entire "Balaban inner step" structure of §§5.1, 5.4 uses the coarsening interpretation. As written, the proof's "$\sum 4^{-k}$ converges" claim is **literally divergent** under the conventions of §5.4.1.

**Finding:**

(a) **The black-box framing (effective action structure).** Section 5.1.3 writes
$$S_k = \frac{1}{g_k^2} S_{\mathrm{YM}} + \sum_n c_n^{(k)} \mathcal{O}_n + E_k, \qquad |c_n^{(k)}| \leq C_n g_k^{d_n - 4}, \quad \|E_k\| \leq C g_k^4$$
This decomposition is *not* a single theorem in Balaban's CMP papers; Balaban works with polymer activities $K_k(X, V)$, not with an explicit operator decomposition. The translation from polymer activities to local operator coefficients with bounds is in **Appendix I.1** ("Operator extraction lemma") of the preprint, where it is presented as a Taylor expansion of the polymer activity in the link variables modulo the identity, with the radius of convergence guaranteed by (B1).

The translation is *plausible* — Taylor expansion of an analytic function gives a power series in the local field, the dimension counting follows from engineering dimension of the field — but the technical content of "$\|E_k\| \leq C g_k^4$ in the $L^\infty$ norm on gauge-invariant functionals" is *not* derived from a single Balaban theorem. It is *inferred* from polymer expansion convergence and the Taylor radius. Appendix I.1 makes this inference; the result is the form-factor norm bound used in §§5.2–5.5.

This is fine in principle, but the preprint is sloppy about *which* norm is being controlled. Balaban's published bounds are on polymer activities $K_k(X, V)$ as functions of $V$ (with exponential decay $e^{-\kappa|X|}$); the operator-norm bound on $E_k$ as a transfer-matrix operator on the Hilbert space is a *derived* statement that requires showing each polymer activity contributes a bounded operator. This is the content of Lemma I.1 — and it's a non-trivial step that Balaban himself does not perform. Sound but should be flagged as a "derived from" statement, not a "Balaban theorem."

(b) **The gauge group SU(N) extension.** Balaban's published program (CMP 95–119, 1982–1989) is primarily for SU(2). Sections 5.1.2, I.1.3, I.3, I.4, K all argue that the extension to SU(N) is "standard" and amounts to inserting the appropriate adjoint dimensions $N^2 - 1$ and Casimirs into the constants. This is *plausible* and Dimock (2011) verifies the analogous statement for the scalar $\phi^4_3$ theory, but no published work performs the SU(N) extension of Balaban's full program in $d=4$.

The preprint's I.4 ("Other compact simple groups") and K ("Balaban for general groups") amount to a *sketch* of the extension to SO(N), Sp(N), and the exceptionals. They identify the relevant homogeneous spaces (e.g., $\mathbb{HP}^{N-1}$ for Sp(N)), state that they have positive Ricci and $H^1 = 0$, and assert that all the steps of the proof go through with $G$-dependent constants. **No actual computation is performed for the exceptionals.** The proof for Clay must be valid for *any compact simple gauge group*, including $G_2, F_4, E_6, E_7, E_8$ — and the preprint does not deliver this.

(c) **The remainder bound.** As discussed in (a). The bound $\|E_k\| \leq C g_k^4$ in the $L^\infty$ norm on gauge-invariant functionals is derived in Appendix I.1 and used pervasively. The constant $C$ is N-dependent (polynomial in $N$, see I.3). Sound.

(d) **The running coupling and the K-vs-k notation collision.** This is the central issue.

**The factual contradiction:** Section 5.1.2 line 22 writes
> "At RG step $k$, define a *coarser* lattice $\Lambda_k$ with spacing $a_k = 2^k a_0$ by block-spinning..."

This is the standard Balaban convention: $k$ is the inner RG step that *coarsens* a fixed bare lattice. The bare lattice is $\Lambda_0$ at $a_0$, and increasing $k$ corresponds to *coarser* (larger $a_k$) effective theories.

Section 5.4.1 line 680 confirms this:
> "At step $k$: lattice $\Lambda_k$, spacing $a_k = 2^k a_0$, dimensionless gap $\hat\Delta_k = a_k \Delta_k$. One block-spin step coarsens to $\Lambda_{k+1}$ with $a_{k+1} = 2 a_k$ and $\hat\Delta_{k+1} = 2\hat\Delta_k(1 + O(g_k^4))$."

Note in particular that **$\hat\Delta_{k+1} = 2\hat\Delta_k$, hence $\hat\Delta_k$ GROWS with $k$**. This is correct for the Balaban convention: the dimensionless gap measured in lattice units of the *effective* lattice grows as the lattice coarsens.

Now §5.4.6 line 877:
> "$C_k \sim k^\gamma$, $g_k^4 \sim 1/k^2$, $\hat\Delta_k^2 \sim 4^{-k}$"

But $\hat\Delta_{k+1} = 2\hat\Delta_k$ gives $\hat\Delta_k^2 = 4^k \hat\Delta_0^2$, *not* $4^{-k}$. The two statements are *inconsistent*: the Balaban convention forces $\hat\Delta_k^2$ to *grow* like $4^k$, but §5.4.6 needs it to *shrink* like $4^{-k}$ for the convergence sum.

The "doubly exponential convergence" claim:
$$\sum_k C_k g_k^4 \hat\Delta_k^2 \sim \sum_k k^{\gamma - 2} \cdot 4^{-k} < \infty$$
**only works if $\hat\Delta_k^2 \sim 4^{-k}$**. With the Balaban convention $\hat\Delta_k^2 \sim 4^k$, the sum is
$$\sum_k C_k g_k^4 \cdot 4^k \sim \sum_k k^{\gamma - 2} \cdot 4^k$$
which **diverges** (the ratio test gives $\lim 4 > 1$; verified computationally in the venv).

§5.7(b), proving the "doubly exponential convergence":
> "Along the RG trajectory with $L^k$ blocking ($L = 2$): $a_k = a_0/2^k$..."

Now the convention has *flipped*: $a_k = a_0/2^k$ (refining), not $a_k = 2^k a_0$ (coarsening). The same letter $k$ is used, but with the opposite physical meaning.

§5.7 OS2 line 2140:
> "...the lattice spacing $a_k = a_0/2^k$..."

Same flip.

**The proof has TWO meanings of $k$:**
- (Balaban inner) $k$ in §§5.1, 5.4: $a_k = 2^k a_0$, coarsening, $\hat\Delta_k$ grows.
- (Bare lattice fineness) $k$ in §§5.4.6, 5.7: $a_k = a_0/2^k$, refining, $\hat\Delta_k$ shrinks.

These are conceptually distinct (the script labels them $k$ and $K$) and the proof never separates them. The §5.4.5 recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ uses the kinematic identity $\hat\Delta_k^2 = \hat\Delta_{k+1}^2/4$ (line 769), which is the *refining* relationship. But the very same section's setup §5.4.1 explicitly says $\hat\Delta_{k+1} = 2 \hat\Delta_k$, the *opposite*.

**Either the proof is silently switching $k$ from one meaning to another in the middle of §5.4, or the algebra is wrong.** Reading charitably, the intended structure is the script's: there is an outer index $K$ for the bare lattice (refined as $K$ grows) and an inner index for Balaban's RG (coarsened as the inner step grows). Within each bare theory $K$, Balaban's UV stability holds; the *outer* recursion compares mass gaps of consecutive bare theories. The "factor 1/4" comes from refining the bare lattice ($a_0(K+1) = a_0(K)/2$, so $\hat\Delta_K^2 = (a_0(K))^2 \Delta^2 \to \hat\Delta_K^2/4$).

Under this charitable reading, the *proof structure* is salvageable but the *written presentation* has a conceptual collapse: §5.1, §5.4.1 use the Balaban inner-$k$ convention but the §5.4.5 recursion is actually about the outer bare-$K$ convention. The two are conflated under a single letter $k$, and the convergence argument requires a specific interpretation that the setup contradicts.

(e) **Balaban completeness.** Balaban proved UV stability (effective action stays bounded as $a \to 0$ for fixed bare scale) and convergent polymer expansion. He did *not* prove existence of the continuum limit. The preprint claims to bridge this gap via the form-factor recursion. But the form-factor recursion as written requires the K-vs-k separation that the preprint never makes. So the proof's claim to go beyond Balaban is contingent on resolving the notation collision.

**To close:**

1. **Adopt the script's $K$/$k$ convention explicitly.** State that the proof's outer index (call it $K$) refers to a refining sequence of *bare* lattices $\Lambda_0(K)$ with $a_0(K) = a_*/2^K$, and that within each bare theory, Balaban's *inner* RG (coarsening, indexed by $k$) controls UV stability.
2. **Restate §5.4.5 as a comparison between two bare theories**, not as a single Wilsonian step. The "$1/4$" contraction is the kinematic identity $a_0(K+1)^2 = a_0(K)^2/4$, *not* a physical decay under flow.
3. **Re-verify the convergence sum** under the corrected convention: $\sum_K C_K g_K^4 \hat\Delta_K^2$ with $\hat\Delta_K^2 \sim 4^{-K}$ — this *does* converge.
4. **Prove that the inner Balaban RG within each bare theory $K$ delivers a $K$-uniform mass gap.** This is the genuine new ingredient, and it is *not* in Balaban's published work. The preprint asserts it but does not prove it under a clean separation of indices.

**Difficulty:** As a notation/restructuring fix, **1 page**. As a re-derivation of the convergence sum from scratch under the corrected convention, **1 paper**. As a proof that the inner Balaban RG delivers a $K$-uniform gap (item 4), **1 paper or more** — this is the actual hard mathematics that Balaban himself did not do, and the preprint's current formulation papers over the gap by conflating two indices.

**Impact on the claimed result:** As written, the central convergence claim of §5.4.6 is *contradicted* by the conventions of §5.4.1 and §5.1.2. **A Clay referee with experience in Balaban's CMP series will catch this on the first reading.** The proof can probably be salvaged by adopting the K/$k$ convention from Balaban CMP 109 p. 251 (which the script's CRITICAL section already cites), but as currently written, the §5.4 recursion is *internally inconsistent* about the direction of the RG flow. This is the headline issue and the single most credibility-destroying gap I have found.
