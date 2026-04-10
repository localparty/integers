# Applied patches: B2 (Appendix F) and C2 (Appendix K)

**Date applied:** 2026-04-08

## Patch B2 — Fredenhagen--Marcu direction / Appendix F relabeling

**Source patch:**
`/Users/gsix/yang-mills/notation-math-referee/latest-run/gap-closing-work/tier-2-fixes/B2-fredenhagen-marcu-direction.md`

**Target file:**
`/Users/gsix/yang-mills/preprint/sections/F-area-law-mass-gap.md`

### Edits applied

1. **F.1 Statement — added Preface and relabeled F.1.**
   - Inserted a **"Preface (status of this appendix)"** paragraph at
     the top of §F.1 stating that the rigorous lower bound on
     $\Delta_0$ used in the main proof is the cluster-expansion rate
     $\alpha/a$ of Theorem 2 (§4.3), combined with reflection
     positivity (Lemma D.2) and the spectral theorem. Declares the
     appendix's derivation a physical heuristic, not a theorem, and
     points forward to Remark F.5.1.
   - Relabeled **"Theorem F.1"** $\to$ **"Heuristic estimate F.1"**
     (following §4 of the B2 patch, which explicitly recommends this
     relabeling).
   - Changed the conclusion of F.1 from "*Then the reconstructed
     Hamiltonian has a mass gap $\Delta \geq c\sqrt{\sigma}$*" to
     "*Then the closed-string / flux-tube heuristic gives an
     order-of-magnitude estimate $\Delta \gtrsim c\sqrt{\sigma}$*"
     (weakened equality to heuristic inequality, and made clear this
     is an estimate from the flux-tube argument, not a theorem).

2. **F.5 Summary — softened and added Remark F.5.1.**
   - Renamed the summary's "chain" as a "heuristic chain," weakened
     $\geq c\sqrt\sigma$ to $\gtrsim c\sqrt\sigma$ in both arrows, and
     added a sentence stating that the chain is a physical estimate
     consistent with lattice-QCD phenomenology, not a rigorous proof.
   - Added **Remark F.5.1 (status: physical heuristic, not a theorem)**
     explaining that F.3--F.5 are physical heuristics providing
     order-of-magnitude estimates, explicitly listing the three-step
     rigorous chain used in the preprint:
     1. Kotecký--Preiss cluster expansion convergence with weight
        $\alpha > 0$ (Theorem 2, §4.3) $\Rightarrow$ exponential
        clustering of connected correlators at rate $\alpha/a$.
     2. Reflection positivity of the KK-enhanced action (Lemma D.2)
        $\Rightarrow$ self-adjoint transfer matrix $\hat T$ and
        positive Källén--Lehmann spectral measures.
     3. Spectral theorem (Reed--Simon Vol. IV §XIII.1) $\Rightarrow$
        $\Delta_0 \geq \alpha/a > 0$ uniformly in volume.
   - States explicitly that Fredenhagen--Marcu is a *consequence*,
     not an input, of the rigorous mass gap, and that the
     closed-string $c\sqrt{\sigma}$ estimate is a physical cross-check
     only, not a step in the proof.

### Effect

The rigorous backbone of the mass-gap proof (cluster expansion $+$
RP $+$ spectral theorem) is now cleanly separated from the
physics-level consistency checks (area law, Fredenhagen--Marcu,
flux tube, Lüscher). Appendix F no longer claims the status of a
theorem for the flux-tube estimate. The B2 referee concern --- that
"Theorem F.1" was labeled as a theorem when it is actually a
heuristic, and that the Fredenhagen--Marcu direction was being cited
the wrong way --- is resolved.

---

## Patch C2 — Large-field exponent optimization / Appendix K.4

**Source patch:**
`/Users/gsix/yang-mills/notation-math-referee/latest-run/gap-closing-work/tier-2-fixes/C2-large-field-exponent-optimization.md`

**Target file:**
`/Users/gsix/yang-mills/preprint/sections/K-balaban-general-groups.md`

### Edits applied

1. **K.4 "Choice of $\epsilon$" paragraph (was line 189).**
   - Replaced $\epsilon = 1/4$ with $\epsilon^* = 0.49$.
   - Rewrote the justification to reflect the optimization:
     - (i) $\epsilon^* > 0$ $\Rightarrow$ threshold
       $p(g_k) = g_k^{0.51} \to 0$ in the UV.
     - (ii) $\epsilon^* < 1/2$ keeps the analysis inside the
       polymer-convergence window of Balaban CMP 119 §2; taking
       $\epsilon^*$ close to $1/2$ maximizes the large-field
       suppression $e^{-c(G)/g_k^{0.98}}$ and *widens* the
       small-field domain, making polymer convergence *easier*.
     - (iii) With the explicit constant $c(G) = 2 d_R$ (stated
       explicitly in the paragraph, cross-referenced to the
       "Large-field suppression" paragraph that follows and to
       Section K.9), the ratio $e^{-c(G)/g_k^{0.98}}/g_k^4$ is
       strictly sub-leading for all $g_k \leq 0.5$ along the AF
       trajectory ($\sim 10^{-4}$ at $g_k = 0.5$; $\sim 10^{-22}$
       at $g_k = 0.1$ for SU(3) with $c(G) = 6$).
   - Noted that the uniform derivation of K.4 holds for any fixed
     $\epsilon \in (0, 1/2)$, so taking $\epsilon^* = 0.49$ adds
     zero cost to the polymer-expansion analysis.
   - Recorded the conservative alternative $\epsilon^* = 0.45$
     (ratio $\sim 2 \times 10^{-4}$ at $g_k = 0.5$) as an
     equally adequate backup.

2. **$c(G) = 2 d_R$ was already explicitly stated** at the
   "Large-field suppression" paragraph (now line 228, formerly
   213) and in the K.9 summary table. The new "Choice of $\epsilon$"
   paragraph cross-references both.

### Effect

Appendix K.4 now uses the optimized exponent $\epsilon^* = 0.49$
sitting just below the polymer-convergence threshold, with the
explicit N-dependent constant $c(G) = 2 d_R$. This closes the C2
gap: the non-perturbative correction
$e^{-c(G)/g_k^{2\epsilon^*}} = e^{-c(G)/g_k^{0.98}}$ is
unambiguously sub-leading to $g_k^4$ along the full AF trajectory
for SU(3) (and for general compact simple $G$), without any
circular appeal to $\hat\Delta_k \geq \hat\Delta_\infty > 0$ in
§5.5.3.

Note: the §5.5.3 companion rewrite in `05-continuum-limit.md`
(lines 1228--1260 per the C2 patch) is a separate edit not covered
by the present task (which only touches F and K). If the §5.5.3
paragraph has not yet been updated, it still needs the replacement
text from §4 of the C2 patch document.

---

## Files modified

- `/Users/gsix/yang-mills/preprint/sections/F-area-law-mass-gap.md`
  (B2 patch: §F.1 header relabeled, Preface added, §F.5 softened,
  Remark F.5.1 added)
- `/Users/gsix/yang-mills/preprint/sections/K-balaban-general-groups.md`
  (C2 patch: §K.4 "Choice of $\epsilon$" paragraph replaced)
