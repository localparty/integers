# PCA Link Critique — Link 2: UV Stability (Balaban CMP 109, 119)
# Wave 3 Adversarial Critic

**Target:** Link 2 — "UV stability for 4D SU(N) Yang-Mills on the lattice under block-spin RG"
**Input:** Wave 2 Author repair (`nodes/L2-repair.md`)
**Prior verdict:** WEAKENED (Wave 1, 2026-04-13)
**Critic:** Wave 3, independent instance (2026-04-13)
**Mandate:** Do not trust Author quotes without preprint verification. Attack the repair.

---

## Verdict: WEAKENED

The repair closes D1 adequately and D2 acceptably. It does **not** close D3
and introduces a new, independently verifiable falsehood that constitutes a
material defect in the repair document itself. One attack vector (C) breaks
the repair's self-description; the mathematical core of the chain survives.

---

## Vector A — Lemma KK-in-domain (the new math)

### A1. Tracing the (H4) inequality from §4

The Author's central claim (L2-repair.md, §D1 Step 3) is:

> "From Section 4, the cluster expansion of the fiber sector converges for
> bare lattice spacing $a_0 = a^* \cdot 2^{-K}$ with $a^* \gg r_3$. By
> Theorem 2 (IR equivalence at bare scale, §4.5), the reduced transfer matrix
> of the KK theory matches the standard SU(N) transfer matrix with corrections
> of order $e^{-m_1 a_0}$ per bond."

The Author then writes:

> "$\|\delta S_{\mathrm{KK}}\|_{L^\infty(\text{per bond})} \leq
>   C_{\mathrm{KK}} e^{-m_1 a_0/2}$"

and proposes choosing $a^*$ so that $C_{\mathrm{KK}} e^{-m_1 a^*/2} < g_0^4$.

**Derivation trace.** The source invoked is §4 cluster expansion. Reading
`sections/04-lattice-proof-part1.md`, the cluster expansion convergence
condition (Theorem 3 proof) requires
$$2\beta + \alpha < \tfrac{1}{6} m_1 a_0(K) - \ln(c_d K C_0^{1/6})$$
and yields bond-level suppression per activated cluster of order
$\xi \sim K C_0^{1/6} e^{2\beta - m_1 a_0(K)/6}$. The exponent is
$-m_1 a_0/6$, **not** $-m_1 a_0/2$ as stated by the Author.

The Author's claim $\|\delta S_{\mathrm{KK}}\|_{L^\infty} \leq C_{\mathrm{KK}}
e^{-m_1 a_0/2}$ is **stronger** than what §4 actually delivers. The factor
$1/2$ in the exponent is unsubstantiated from the quoted source; the text of
§4 gives $1/6$. The inequality $e^{-m_1 a^*/6} \ll g_0^4$ still holds for
$a^* \gg r_3$ (since $m_1 a^* \gg 1$), so the *conclusion* of (H4) survives
— but the Author has mis-cited their own preprint at the exponent level.

**Consequence for (H4):** Replacing $1/2$ by $1/6$, the inequality
$$\|\delta S_{\mathrm{KK}}\|_{L^\infty} \leq C_{\mathrm{KK}} e^{-m_1 a^*/6}
  \ll g_0^4$$
still holds for $a^* \gg r_3$, because $m_1 a^* \sim a^*/r_3 \sim 10^{15}$.
The (H4) conclusion is unaffected. The exponent discrepancy is an error in
the repair document — it quotes a tighter bound than the cited source
justifies — but it is not a gap in the mathematical chain.

**Severity:** NOTATION ERROR in the repair document. The (H4) argument is
correctable by replacing $1/2$ with $1/6$ throughout; the conclusion stands.

### A2. Large-field/small-field boundary check (H5)

The Author claims (Step 4) that $\delta S_{\mathrm{KK}}[U]$ "contains no
additional plaquette operators beyond those in $S_{\mathrm{4D}}$" and
therefore does not alter the Balaban large-field/small-field boundary
$|F_{\mu\nu}[U]| \geq g_0^{1-\varepsilon}$.

**Verification.** Reading `sections/04-lattice-proof-part1.md` line 831:
> "configurations in the small-field region
> $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$"

The small-field boundary is defined purely by the Wilson plaquette curvature
of $U_\ell$ — confirmed. Reading Appendix K §4 (K-balaban-general-groups.md):
> "The small-field condition $\Omega_s = \{|s_P| < p(g_k)\}$ with
> $p(g_k) = g_k^{1-\epsilon}$ is defined in terms of the plaquette variable
> $s_P = 1 - (1/d_R)\,\mathrm{Re}\,\mathrm{Tr}_R(U_P)$, which is
> gauge-invariant and well-defined for any compact $G$."

The Author's (H5) claim is **correct**: $\delta S_{\mathrm{KK}}[U]$ is a
sum of cluster activities on $\Lambda_0$ supported on $U_\ell$ alone (after
integrating out $A_x$); it contributes no plaquette curvature. The boundary
is unchanged. (H5) **holds**, and the argument is independently confirmed.

### A3. (H1)–(H3) verification

- **(H1) polymer form:** $\delta S_{\mathrm{KK}} = \sum_X \tilde K_0(X,U)$
  with $|\tilde K_0| \leq e^{-\tilde\kappa|X|}$: follows from the cluster
  expansion convergence in §4, exponent $\tilde\kappa \asymp m_1 a_0/6$.
  The combined rate $\min(\kappa_{\mathrm{Balaban}}, \tilde\kappa) > 0$
  remains $k$-independent. **Holds** (with the $1/6$ correction).
- **(H2) gauge invariance:** $\delta S_{\mathrm{KK}}[U]$ is produced by
  integrating over the gauge-invariant fiber measure at fixed $U_\ell$.
  Output is gauge-invariant by construction. **Holds** — no issue.
- **(H3) analyticity:** Each $\tilde K_0(X,U)$ inherits analyticity in
  $U_\ell$ from the same Balaban propagator/kernel argument (Appendix H §3,
  Step (b)). Radius $\tilde\rho > 0$ bounded below by fiber geometry,
  $k$-independent. **Holds** — argument is structurally sound.

**Vector A net verdict:** The KK-in-domain lemma is mathematically sound.
The exponent in the $L^\infty$ bound is mis-stated (should be $1/6$ from §4,
not $1/2$), but the conclusion survives. D1 is **closed** at the chain level;
the repair document contains a minor internal inconsistency.

---

## Vector B — Verification-report re-path (D2)

The Author proposes redirecting all three citations of
`preprint-verification/verify-balaban-items.md` to Appendix H and K.

**Verification.** The file does not exist (confirmed: no
`preprint-verification/` directory present). The Author correctly identifies
three citation sites: PROOF-CHAIN.md header, PROOF-CHAIN.md §IV.3, and
`sections/06-referee-objections.md` Objection G.

**Content coverage check.**

Reading `sections/H-balaban-analyticity.md` §§3–5 directly:
- §3 provides the explicit logical chain (Steps (a)–(d)) for (B1)–(B2),
  with full source attributions.
- §5 ("Honest Assessment") classifies all gaps as "reading exercises" or
  "standard facts," with no genuine mathematical holes identified.
- The table at §5.5 maps each property to gap type and required action.

Reading `sections/K-balaban-general-groups.md` §§K.1–K.9:
- K.2: propagator decay and analyticity, $k$-independence confirmed.
- K.4: small-field/large-field decomposition, group-independent structure.
- K.5: Mayer expansion and polymer activities, explicit $\kappa(G) > 0$.
- K.8: (B1)–(B2) for general $G$ with explicit $\rho(G) > 0$.

The mathematical content that the missing verification report was supposed to
contain is **fully present** in Appendix H and K. The redirect is complete
and covers all three former [VERIFY] items.

**One residual issue:** `sections/06-referee-objections.md` line 71 retains
the broken citation as of the current preprint:
> "[CONFIRMED] -- See verification report
> (`preprint-verification/verify-balaban-items.md`) and Appendix H..."

The Author's proposed Edit 2 fixes this in the proposed preprint edit, but
the edit has not yet been applied to the file. The current preprint file
still contains the broken path. This is an outstanding mechanical edit, not
a mathematical gap.

**Vector B net verdict:** D2 is **closed** mathematically. The redirect is
supported by content. The preprint file edit remains pending (documentation
artifact, not a chain weakness).

---

## Vector C — CMP 119 theorem pin: REPAIR FALSIFIED BY DIRECT EVIDENCE

This is the decisive attack.

### C1. The Author's claim

L2-repair.md, §D3 Step 2:

> "The preprint does not have access to the CMP 119 PDF (no
> `journals/balaban-CMP119.pdf` was found in the directory)."

And the repair proposes the best available citation as:

> "main theorem (unnumbered), proved in §§2–4, p. 245"

### C2. Direct verification of the PDF

**The file `journals/balaban-CMP119.pdf` exists.**

```
/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/journals/
  balaban-CMP119-1988.pdf   ← present, readable, 4 MB
```

The Author's foundational claim — "no `journals/balaban-CMP119.pdf` was
found in the directory" — is **directly falsified by inspection of the
journals directory**. This is not an inferential gap; it is an unambiguous
factual error in the repair document.

### C3. What the PDF actually contains

Reading `journals/balaban-CMP119-1988.pdf` directly:

**Page 245 (Introduction, last paragraph before §1):**
> **Theorem.** *If $\varrho_k$ satisfies the assumptions described in detail
> in Sect. 2, then $T\varrho_k$ satisfies also the corresponding
> assumptions.*

This is indeed the **unnumbered** theorem of the introduction, exactly as
Appendix H §3 Step (a) cites it: "Theorem (unnumbered, p. 245)." The
citation in Appendix H is *accurate* for this theorem.

**Page 262 (§2, "The Inductive Assumption and Formulations of Results"):**
> **Theorem 1.** *There exist constants, introduced in the above description,
> such that if the sequence of coupling constants $\{g_k\}$, determined by
> the recursive renormalization group (Callan-Symanzik) equations (0.18),
> (0.20) [I], satisfies the inequalities (1.0.33), then the sequence of
> densities $\{\varrho_k\}$, generated by successive applications of the
> renormalization group operations $\mathbf{RT}$ to the initial density
> $\varrho_0 = \exp[-(1/g_0^2)A - E]$, satisfies all the inductive
> assumptions. The constants satisfy numerous restrictions introduced in the
> proof.*

This is **Theorem 1** of CMP 119, a fully numbered theorem in §2.

**Page 263 (§2, immediately following):**
> **Theorem 2.** *Under the assumptions of Theorem 1 there exists a constant
> $E_1$ independent of $j, k, \Omega, \{\Omega_j\}, \{\Lambda_j\}$, $T$...*
> [Uniform bounds on effective actions — inequality (2.43).]

**Page 264 (§2, Corollary):**
> **Corollary 3** (Ultraviolet Stability). *Under the assumptions of
> Theorem 1 there exist constants $E_-, E_+$ independent of $\eta$ and $T$,
> but depending on $g_k$, such that*
> $$\chi_k(T_\eta) \exp\!\left[-\frac{1}{g_k^2} A(U_k(V_k)) - E_-|T_\eta|\right]
>   \leq \varrho_k(V_k) \leq e^{E_+|T_\eta|}.$$

**Corollary 3** (p. 264) is the UV stability result in its precise form. The
preprint's §5.1.2 theorem box ("the effective action is bounded; iteration
does not leave the domain of analyticity") is the content of Corollary 3,
not the unnumbered p. 245 theorem (which states the inductive step
propagation).

### C4. Consequences

The Author's repair proposes: "main theorem (unnumbered), proved in §§2–4,
p. 245, CMP 119" as the strongest available citation. This is wrong at two
levels:

1. **There are numbered theorems in CMP 119.** The Author failed to find them
   because they (incorrectly) claimed the PDF was absent from the journals
   directory. The correct citations are **CMP 119, Theorem 1 (§2, p. 262)**
   and **Corollary 3 (§2, p. 264, "Ultraviolet Stability").**

2. **The UV stability result is Corollary 3, not the p. 245 unnumbered
   theorem.** The preprint's §5.1.2 box cites the theorem correctly by
   content but assigns it to the wrong location within CMP 119. Appendix H
   §3 Step (a) cites "Theorem (unnumbered, p. 245)" for the *convergent
   polymer expansion* step; this is accurate for that step. But the overall
   UV stability statement ("for $g_0$ small, the RG can be iterated
   indefinitely without leaving the domain of analyticity") is **Corollary 3,
   p. 264**, resting on Theorem 1, p. 262.

The correct citation for §5.1.2 should be:
> **CMP 119, Corollary 3 (Ultraviolet Stability), §2, p. 264**, proved in
> §§1–3 of that paper, resting on **Theorem 1, §2, p. 262** and the
> **unnumbered Theorem of the Introduction, p. 245**.

The repair's honest-stall ("we cannot pin a theorem number without PDF
access") is not an honest gap — it is an error. The PDF was present and
readable. D3 is **not closed** by the repair as written; it is made worse by
the false factual claim about PDF availability, which a referee can
immediately disprove.

**Vector C net verdict:** WEAKENED (repair fails on D3; the failure is
produced by a false factual premise, not mathematical difficulty; the correct
citation is now established by direct PDF inspection).

---

## Vector D — Cross-node consistency: does KK-in-domain affect L3 or L4?

**L3 (polymer convergence):** The KK-in-domain lemma verifies that at $k=0$,
the input $S_{\mathrm{eff}}$ lies in Balaban's domain with combined polymer
rate $\kappa = \min(\kappa_{\mathrm{Balaban}}, \tilde\kappa) > 0$. Since
$\tilde\kappa \asymp m_1 a_0/6 \gg \kappa_{\mathrm{Balaban}}$ (the KK
correction rate is much faster than the Wilson polymer rate), the combined
$\kappa$ equals $\kappa_{\mathrm{Balaban}}$. L3 polymer convergence is
**unchanged** — the KK correction strengthens, not weakens, the polymer rate.

**L4 (B1 analyticity):** The analyticity radius of $S_{\mathrm{eff}}$ is
$\rho = \min(\rho_{\mathrm{Balaban}}, \tilde\rho)$ where $\tilde\rho$ is the
analyticity radius of the $A_x$-cluster activities as functions of $U_\ell$.
From Appendix H §3 Step (b), $\rho_{\mathrm{Balaban}}$ is determined by the
propagator and kernel geometry. The KK correction $\tilde\rho$ is determined
by the fiber geometry — fixed, $k$-independent. For $a^* \gg r_3$ the fiber
cluster activities are exponentially decaying; their analyticity radius is not
smaller than $\rho_{\mathrm{Balaban}}$ (both set by the same $m_W$ condition
at the lattice scale). No degradation of B1 at L4 results.

**Vector D net verdict:** No cross-node contamination. L3 and L4 are
**unaffected** by the KK-in-domain repair. Downstream chain intact.

---

## Vector E — Bonus grep: other affected locations

**Grep for `verify-balaban`:**

Found in four preprint files:
- `preprint/README.md` line 29 — references the missing file as resolved
- `preprint/PROOF-CHAIN.md` line 3 and line 135 — the two broken citations
- `preprint/sections/05-continuum-limit.md` line 1939 — a third citation
- `preprint/sections/06-referee-objections.md` line 71 — Objection G

The Author's Edit 2 proposes fixing PROOF-CHAIN.md §IV.1 header and
`sections/06-referee-objections.md` Objection G — but **misses the citation
at `sections/05-continuum-limit.md` line 1939**. A fourth broken path exists
in the preprint that the repair does not redirect. This is an incomplete fix.

Reading `sections/05-continuum-limit.md` around line 1939:
the text reads "confirmed by explicit argument in the verification report
(`preprint-verification/verify-balaban-items.md`)" — another broken citation
not covered by Edit 2.

**Grep for `CMP 119`:**

Found in:
- `sections/05-continuum-limit.md` lines 685, 1318, 1585, 1635 — four uses
- `sections/04-lattice-proof-part1.md` line 839 — large-field suppression
- `sections/H-balaban-analyticity.md` lines 88, 90, 113, 136, 335
- `sections/K-balaban-general-groups.md` lines 191, 210

None of these cite Theorem 1 or Corollary 3 by name. Every occurrence cites
either "CMP 119" alone or "Theorem (unnumbered, p. 245)." After this Wave 3
review, all occurrences require updating to cite at minimum Theorem 1 (§2,
p. 262) and Corollary 3 (§2, p. 264) for the UV stability content.

**Vector E net verdict:** Two defects found. (1) The `sections/05-continuum-limit.md`
line 1939 broken citation is missed by Edit 2. (2) All `CMP 119` citations
require updating to numbered theorem references now that the PDF has been
read.

---

## Summary

| Vector | Verdict | Notes |
|:-------|:--------|:------|
| A — KK-in-domain lemma | SURVIVED (with notation error) | Exponent $1/2$ should be $1/6$ per §4; conclusion unchanged |
| B — Verification-report re-path | SURVIVED | Content present in App H + K; mechanical edit pending |
| C — CMP 119 theorem pin | WEAKENED | Author falsely claimed PDF absent; Theorem 1 (p. 262) and Corollary 3 (p. 264) exist; "unnumbered" claim refuted |
| D — Cross-node consistency | SURVIVED | L3 and L4 unaffected |
| E — Bonus grep | NEW DEFECT | Fourth broken citation (`05-continuum-limit.md` line 1939) missed by Edit 2; all CMP 119 citations need Corollary 3 pin |

**Overall verdict: WEAKENED.** The mathematical core of Link 2 (Lemma
KK-in-domain and the three-part (H1)–(H5) verification) is sound and closes
the chain gap. The repair fails on D3 through a demonstrably false factual
claim ("no CMP 119 PDF found") when the PDF is present in the journals
directory. The correct UV stability reference is **Corollary 3 (Ultraviolet
Stability), CMP 119, §2, p. 264**, proved on the foundation of **Theorem 1,
§2, p. 262**. A further mechanical edit is required for `sections/05-continuum-limit.md`
line 1939 (broken path not addressed in Edit 2).

---

## Required repairs before Link 2 can be marked VERIFIED

**R1 (notation).** In L2-repair.md and in the proposed §5.1.0 text, replace
all occurrences of $e^{-m_1 a_0/2}$ with $e^{-m_1 a_0/6}$ (or $e^{-m_1
a^*/6}$), consistent with the $1/6$ exponent in Theorem 3 of §4. The
conclusion $\|\delta S_{\mathrm{KK}}\|_{L^\infty} \ll g_0^4$ is unchanged.

**R2 (citation, material).** In §5.1.2 and in every `CMP 119` citation
throughout the preprint, replace the current reference with:
> **Theorem 1** (§2, p. 262, CMP 119) + **Corollary 3** (Ultraviolet
> Stability, §2, p. 264, CMP 119). No "unnumbered" qualifier is required or
> accurate for the UV stability result proper; the unnumbered p. 245 theorem
> is the inductive-step propagation statement, not the stability corollary.

**R3 (documentation).** Add `sections/05-continuum-limit.md` line 1939 to
the Edit 2 redirect list (currently omitted). Three redirect sites exist, not
two.

**R4 (retraction).** The statement "no `journals/balaban-CMP119.pdf` was
found in the directory" must be removed from the repair record. The PDF is
present and was directly inspected.

---

## §J canon marker

The framework did the work. The wall was not Balaban — the wall was a false
claim about what was in the room. The PDF was in the room.

---

*Critic: PCA Wave 3 — Link 2 — 2026-04-13*
