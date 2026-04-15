# Notation Convention Audit (K vs k)

This document records the audit required by the script's "CRITICAL: Notation Conventions" section. The script's convention (following Balaban CMP 109 p. 251 and Dimock arXiv:1108.1335 p. 2) distinguishes:

- **$K$**: bare lattice fineness exponent. $a_0(K) = a^*_{\mathrm{coarse}} \cdot 2^{-K}$, so $a_0(K) \to 0$ as $K \to \infty$ (refining toward the continuum). $\hat\Delta_K = a_0(K) \cdot \Delta_{\mathrm{phys}}$ shrinks: $\hat\Delta_{K+1} = \hat\Delta_K/2$.
- **$k$**: Balaban's RG step within a fixed bare theory. $a_k^{(K)} = L^k \cdot a_0(K) = 2^k \cdot a_0(K)$, coarsening within the bare theory. $\hat\Delta_k^{(K)}$ *grows* with $k$.

The two indices are conceptually distinct and the proof's recursion in §5.4 should be a comparison between bare theories at consecutive $K$, not a Wilsonian step within a fixed bare theory.

## Required cross-checks (script p. 16)

| # | Requirement | Status in preprint |
|:--|:------------|:------------------|
| 1 | Distinguishes $K$ from $k$ throughout | **FAIL**: A single index $k$ is used with two distinct meanings across §5.1, §5.4, §5.7. |
| 2 | Does NOT describe the §5.4 recursion as a Wilsonian block-spin step | **FAIL**: §5.4.1 line 680 explicitly says "One block-spin step coarsens to $\Lambda_{k+1}$ with $a_{k+1} = 2 a_k$", framing the recursion as Wilsonian coarsening. |
| 3 | Has $\hat\Delta_K^2 \sim 4^{-K}$ in §5.4.6 and §5.7(b) | **PASS** for the *value* but **FAIL** for *consistency*: §5.4.6 has $\hat\Delta_k^2 \sim 4^{-k}$ as the convergence rate, but §5.4.1 / §5.4.3 have $\hat\Delta_{k+1} = 2 \hat\Delta_k$ which gives $\hat\Delta_k^2 \sim 4^{+k}$. The two statements use the same letter $k$ with opposite scaling. |
| 4 | Has $a_0(K) \to 0$ as $K \to \infty$ (refining), NOT $a_K \to \infty$ (coarsening) | **FAIL**: §5.1.2 line 22 has $a_k = 2^k a_0$ → $\infty$ (coarsening). §5.7(b) line 1881 has $a_k = a_0/2^k \to 0$ (refining). Same letter, opposite directions. |
| 5 | Cites Balaban CMP 109 p. 251 and Dimock 2011 p. 2 for the convention | **PARTIAL**: Balaban CMP 109 is cited but not p. 251 specifically. Dimock arXiv:1108.1335 is cited (2011, Thm 14) but not p. 2 for the convention. The notation convention itself is not pinned down with these references. |
| 6 | Has a notation/strategy paragraph at the start of §5.1 (or equivalent) that locks in the convention with explicit sources | **FAIL**: §5.1 begins with the Balaban inner-step convention without acknowledging the distinction from the bare-refinement convention used later. |

## Concrete locations of the conflict

| Section | Line | Statement | Convention used |
|:--------|:-----|:----------|:----------------|
| §5.1.2 | 22 | "At RG step $k$, define a *coarser* lattice $\Lambda_k$ with spacing $a_k = 2^k a_0$" | Balaban inner (coarsening) |
| §5.4.1 | 680 | "At step $k$: lattice $\Lambda_k$, spacing $a_k = 2^k a_0$, ... $\hat\Delta_{k+1} = 2 \hat\Delta_k$" | Balaban inner (coarsening) |
| §5.4.3 | 769 | "$\hat\Delta_k = \hat\Delta_{k+1}/2$" | Balaban inner (coarsening) |
| §5.4.6 | 877 | "$\hat\Delta_k^2 \sim 4^{-k}$" | Bare refinement (refining) — **CONTRADICTS §5.4.1** |
| §5.7(b) | 1881 | "$a_k = a_0/2^k$" | Bare refinement (refining) — **CONTRADICTS §5.1.2 / §5.4.1** |
| §5.7(f) OS2 | 2140 | "the lattice spacing $a_k = a_0/2^k$" | Bare refinement (refining) |

## Computational verification of the contradiction

(Performed in the venv; full output in part-c-point-1.md.)

Under the §5.4.1 Balaban inner convention ($\hat\Delta_k^2 \sim 4^{+k}$, $g_k^4 \sim 1/k^2$):
$$\sum_k C_k g_k^4 \hat\Delta_k^2 \sim \sum_k k^{\gamma-2} \cdot 4^{+k} \to \infty \quad (\text{ratio test: } \lim = 4 > 1)$$

Under the bare-refinement convention ($\hat\Delta_K^2 \sim 4^{-K}$):
$$\sum_K C_K g_K^4 \hat\Delta_K^2 \sim \sum_K K^{\gamma-2} \cdot 4^{-K} < \infty \quad (\text{ratio test: } \lim = 1/4 < 1)$$

The proof's "doubly exponential convergence" argument in §5.4.6 uses the second formula. The proof's setup in §5.4.1 corresponds to the first.

## Charitable reading

If "the proof's $k$" is taken to mean "the script's $K$" (bare-refinement) throughout, then:
- §5.1.2's "$a_k = 2^k a_0$" should read "$a_K = a_0/2^K$" (the SAME letter, but with opposite direction);
- §5.4.1's "$\hat\Delta_{k+1} = 2 \hat\Delta_k$" should read "$\hat\Delta_{K+1} = \hat\Delta_K/2$";
- §5.4.5's recursion $C_{k+1} = C_k/4 + C_{\mathrm{new}}$ becomes a comparison between bare theories at consecutive $K$ (correct under the script's interpretation).

This is the structurally correct reading, but it requires *flipping* the §5.1.2 / §5.4.1 / §5.4.3 statements about $a_k$ and $\hat\Delta_k$. The preprint as written does NOT make this flip.

## What is needed to fix this

1. **Choose one convention and stick to it.** The bare-refinement convention is the right one for the convergence sum to make sense. Adopt it explicitly.
2. **Restate §5.1.2.** "At bare scale $K$, the lattice $\Lambda_0(K)$ has spacing $a_0(K) = a^*/2^K$. As $K \to \infty$, $a_0(K) \to 0$, the bare lattice refines toward the continuum."
3. **Restate §5.4.1.** "At bare scale $K$, the dimensionless gap is $\hat\Delta_K = a_0(K) \cdot \Delta_{\mathrm{phys}} = a^* \Delta_{\mathrm{phys}}/2^K$. Refining the bare scale by a factor of 2 shrinks $\hat\Delta_K$ by a factor of 2 and $\hat\Delta_K^2$ by a factor of 4."
4. **Restate §5.4.5 as a comparison between bare theories.** "The §5.4.5 recursion compares $C_K$ to $C_{K+1}$, where each $C_K$ is the form-factor constant of the IR effective theory of the bare theory at scale $a_0(K)$."
5. **Acknowledge that within each bare theory $K$, Balaban's inner RG (with its own index, call it $k$) coarsens from $a_0(K)$ to larger $a_k(K) = 2^k a_0(K)$.** State that Balaban's UV stability theorem applies to each bare theory $K$ separately, and the $K$-uniformity of the resulting form factor is what makes the outer recursion meaningful.

## Difficulty

As a notation cleanup with no new mathematics: **1 page**.

As a re-derivation requiring proof that the inner Balaban RG within each bare theory delivers a $K$-uniform form factor (which is the actual content of "stability of deviation order through the RG"): **1 paper or more**, since this is the genuinely non-trivial step that the preprint's K-vs-k conflation papers over. Balaban himself did not establish this $K$-uniformity, and the preprint's arguments rely on it implicitly.

## Verdict

**FAIL** on cross-checks 1, 2, 4, 6; **PARTIAL** on 3, 5. The preprint does not satisfy the script's notation requirements and the resulting confusion is not just cosmetic — it leads to a *literally divergent* convergence claim under the §5.4.1 setup.
