# Tier 1C Applied: Cluster–Balaban Handoff Lemma

**Date:** 2026-04-08
**Source:** `tier-1-rigor/recursion-assembly-handoff.md`
**Target:** `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
**Result:** File grew from 2852 to 2949 lines (+97 lines).

## Insertions

### Insertion 1 — Cluster–Balaban Handoff Lemma (in §5.4.5)
**Location:** lines 874–919 of the modified file, immediately after the
"Fixed point (conditional on K-uniform inner bound)" paragraph that
closes the original §5.4.5 content, and before the start of §5.4.6.

**Content:** Statement of the lemma with the three hypotheses
(H1) K-uniform cluster expansion, (H2) K-uniform Balaban analyticity
radius, (H3) Rate compatibility $\kappa_{\mathrm{cl}}^* \geq
\kappa_{\mathrm{B}}$. Conclusion: cluster output is a valid initial
condition for Balaban polymer expansion at $k=0$, with $C_K(k=0) \leq
C_0^{\mathrm{cl}}$ uniformly in $K$. Includes proof sketch
(Kotecký–Preiss criterion + factorisation $K_0^{(K)}(X,V) =
K_{\mathrm{cluster}}^{(K)}(X)\cdot Q(X,V)$ on small-field domain) and
Conditionality note flagging (H1)/(H2) as Tier 1 Steps 1.1/1.2 and
verifying (H3) numerically with the $\sim 10^{13}$ margin for $N=3$.

### Insertion 2 — Treatment of the first $k_0(K)$ inner steps (in §5.4.6)
**Location:** lines 951–978, immediately after the
"$\sum_{K=1}^\infty 4^{-K} = 1/3$" line that closed the original
§5.4.6, and before the new Insertion 3.

**Content:** Definition of the crossover step $k_0(K)$ via the
one-loop running of $g_k$, replacement of the perturbative one-loop
estimate by the non-perturbative polymer bound from the Handoff
Lemma's (H2), bound $|\langle 1|E_k^{(K)}(0)|1\rangle_c| \leq
C_{\mathrm{np}}\,\hat\Delta_{k+1}^{(K)\,2}$ with explicit
$C_{\mathrm{np}} = \sum_X e^{-\kappa_{\mathrm{B}}|X|}|X|^2$, and the
key observation that $k_0(K)$ is non-increasing in $K$ (so the total
strong-coupling block contribution is bounded by a fixed physical
constant). This formalises §5.7 Remark 1.

### Insertion 3 — Outer recursion convergence (assembled) (in §5.4.6)
**Location:** lines 980–999, immediately after Insertion 2 and before
the start of §5.4.7.

**Content:** Statement of the assembled outer recursion $C_{K+1} \leq
C_K/4 + C_* + O(g_K^2 C_K)$, fixed point $C_{**} = 4C_*/3$, geometric
approach, and absolute convergence of the mass-gap shift sum
$\sum_K C_K g_K^4 \hat\Delta_K^2 \lesssim \sum_K K^{\gamma-2}\cdot 4^{-K}
< \infty$. Closing "Conditionality (Tier 1B)" paragraph explicitly
flags that the K-uniform single-step bound $C_{\mathrm{new}}(K) \leq C_*$
is the K-uniform spectral lemma (Tier 1 Step 1.3, open Lieb-Robinson
question to be addressed in a separate appendix), and notes that the
assembly remains valid in restricted regimes if Step 1.3 is only partial
(e.g., $N = 2$ unconditional, $N = 3$ conditional).

## Numbering preserved

§5.4.1–§5.4.7 numbering is unchanged. New labeled blocks
("Lemma (Cluster–Balaban Handoff)", "Treatment of the first $k_0(K)$
inner steps", "Outer recursion convergence (assembled)") are inserted
as named paragraphs/lemmas without altering subsection IDs, so all
existing cross-references continue to resolve.

## Failures

None. All three Edit calls succeeded on the first attempt.
