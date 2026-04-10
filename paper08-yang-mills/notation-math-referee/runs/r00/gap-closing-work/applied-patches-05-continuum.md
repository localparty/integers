# Applied Patches to `preprint/sections/05-continuum-limit.md`

**Date applied:** 2026-04-08
**Target file:** `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
**Starting line count:** 2856
**Final line count:** 2852

---

## 1. Tier 0 notation cleanup — K/k separation
Source: `tier-0-notation/notation-patch.md`

Seven individual edits + one insertion, all applied successfully:

1. **Preamble insertion at start of §5.1** (before §5.1.1) — added the "Notation and strategy (two-index convention)" block defining outer index $K$ (bare refinement) and inner index $k$ (Balaban block-spin RG within a fixed bare theory).
2. **§5.1.2** — replaced "Start from a fine lattice $\Lambda_0$…$a_k = 2^k a_0$…" with the "Fix a bare scale $K$" paragraph using $\Lambda_0(K)$, $a_0(K) = a^*\cdot 2^{-K}$, $\Lambda_k^{(K)}$, $a_k^{(K)}$.
3. **§5.4.1 Geometry** — replaced the old "step $k$: lattice $\Lambda_k$…" block with "Geometry: outer recursion between bare theories" stating the kinematic identity (5.4.1a) $\hat\Delta_{K+1}^2 = \hat\Delta_K^2/4$ and clarifying the inner field decomposition at fixed $K$.
4. **§5.4.3 Old contribution (A1)** — replaced the inductive hypothesis + conversion block with the $K$-indexed inductive hypothesis (5.4.3a), the "passage to bare scale $K+1$" derivation of (5.4.3b), and the new "kinematic contraction between bare theories" explanation of the factor $1/4$.
5. **§5.4.5 Recursion box** — replaced "Combining (A) and (B)" block with the outer recursion $C_{K+1} = C_K/4 + C_{\mathrm{new}}(K) + O(g_K^2 C_K)$ and the conditional (K-uniform) fixed-point statement.
6. **§5.4.6 Convergence sum** — replaced the "$C_k \sim k^\gamma$…$4^{-k}$" paragraph with the outer-index version using $C_K, g_K, \hat\Delta_K^2 \sim 4^{-K}$ explicitly tied to bare refinement.
7. **§5.7(b)** — replaced "$a_k = a_0/2^k$, $g_k^2 \sim \ldots$" paragraph with the outer-index $a_0(K) = a^*\cdot 2^{-K}$, $g_K^2$ version.
8. **§5.7(f) OS2 "Rate of O(4) restoration"** — replaced the $a_k = a_0/2^k$ bound (OS2.3–OS2.4) with the $a_0(K) = a^*\cdot 2^{-K}$ bound at bare scale $K$, plus inline justification of the inner/outer reduction.

All edits succeeded on first attempt.

---

## 2. Tier 2 — C2 large-field exponent optimization
Source: `tier-2-fixes/C2-large-field-exponent-optimization.md`

1. **§5.5.3 "Non-perturbative contributions to $\epsilon_B$"** — replaced the entire paragraph (including the large-field Weyl-inequality block that appealed to $\hat\Delta_k \geq \hat\Delta_\infty$) with the $\epsilon^* = 0.49$ version using $c(G) = 2 d_R = 6$, with the explicit non-circular ratio bound $e^{-6/g_k^{0.98}}/g_k^4 \leq 10^{-4}$ for $g_k \leq 0.5$.

Succeeded on first attempt.

---

## 3. Tier 2 — F1 Coincident-point singularities (Källén–Lehmann)
Source: `tier-2-fixes/F1-coincident-point-singularities.md`

1. **§5.7(f) "Coincident-point singularities" paragraph + "Lemma (Local integrability)"** — replaced the full block (paragraph, OPE-invoking lemma, and proof) with the direct Källén–Lehmann derivation: two-point spectral bound $(\ast)$, linked-cluster higher-$n$ bound $(\ast\ast)$, and the shorter Local Integrability lemma using codimension of total diagonal for $n \geq 5$, Hörmander 1983 §8.2 reference.

Succeeded on first attempt. The OPE appeal in the original "Local integrability" proof has been eliminated.

---

## 4. Tier 2 — F2 RP topology specification
Source: `tier-2-fixes/F2-rp-topology-specification.md`

1. **§5.7(f) OS3 Step 2** — replaced the "Preservation under weak limits" block with the topology-specified version: weak-$*$ topology on $\mathcal{S}'(\mathbb{R}^4,\mathfrak{g})$, Hamburger–Nussbaum, explicit compact-support set $K_f$, closed-support Portmanteau form (Kallenberg 2002 Lemma 4.3), truncation argument for support propagation to the limit.

Succeeded on first attempt.

---

## 5. Tier 2 — F5 Non-triviality logic fix
Source: `tier-2-fixes/F5-non-triviality-logic-fix.md`

Three edits, all successful:

1. **§5.7(f) Proposition (Non-triviality), item (ii) header** — changed "Non-vanishing connected 4-point function" to "Non-vanishing connected 2-point function with lower-bounded lightest-glueball matrix element".
2. **§5.7(f) closing line (formerly L2709)** — changed "Any one of (i) or (ii) alone suffices to establish non-triviality." to "Any one of (i) or (iii) alone suffices to establish non-triviality; (ii) is auxiliary and insufficient on its own — a free massive scalar has non-zero 2-point."
3. **§5.7(f) Remark (Connected 4-point function)** — replaced with Corollary F5.1 (Connected $n$-point functions for $n \geq 4$), deriving existence of a nonzero $n \geq 4$ connected Wilson-loop function from ($\sigma > 0$) + clustering + RP + OS reconstruction + charge conjugation.

All three succeeded on first attempt. The claim "the 2-point bound (ii) already excludes the Gaussian case" has been removed.

---

## Summary

- **Total edits applied:** 15 (1 insertion + 14 replacements).
- **Failures:** None. Every edit succeeded on first attempt; no retries or context-expansion were needed.
- **File integrity:** Markdown and LaTeX math preserved. Section headers unchanged (47 `##`/`###` headers before and after). Line count 2856 → 2852 (net decrease of 4, consistent with replacements being slightly more compact than originals, offset by the ~20-line preamble insertion; several large old blocks — especially §5.5.3 and §5.7(f) coincident-points — shrank by more than the preamble added).
- **Scope:** All five Tier 0 + Tier 2 patches for §05 have been applied. Tier 1 follow-ups (K-uniform $C_{\mathrm{new}}(K)$, K-uniform analyticity radius, K-uniform spectral constant $C_p$, cluster/Balaban handoff at $k=0$) remain as explicit open items in the patched text, as required by the Tier 0 patch's §4 "Open follow-up" note.
