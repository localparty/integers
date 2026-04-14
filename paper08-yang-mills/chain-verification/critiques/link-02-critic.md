# PCA Link Critique — Link 2: UV Stability (Balaban CMP 109, 119)

**Target:** Link 2 — "UV stability for 4D SU(N) Yang-Mills on the lattice under block-spin RG"
**Preprint citation:** Balaban, CMP 109 (1987) and CMP 119 (1988), used as black-box literature result
**Critic:** Wave 1 (2026-04-13)
**Verdict:** WEAKENED (repairable gap identified — not BROKEN, not trivial)

---

## 1. What the preprint claims

Section 5.1.2 invokes the following as a black-box literature result:

> **Theorem (Balaban, UV stability).** For $g_0$ sufficiently small, the block-spin RG can be iterated indefinitely: for every $k \geq 0$, the effective action on $\Lambda_k$ is well-defined, gauge-invariant, and bounded. The iteration does not produce divergences or leave the domain of analyticity.

This is applied within the continuum-limit argument (§§5.1–5.7) to a **bare theory** with action $S[U,A] = S_\mathrm{4D}[U] + S_\mathrm{int}[U,A]$, where $S_\mathrm{int}$ includes coupling terms $V_\ell$ between the 4D link variables and the KK fiber fields $A_x \in \mathcal{A}_0(\mathbb{CP}^{N-1})$. UV stability is then used to establish the remainder bound $\|E_k\| \leq C g_k^4$ per unit volume (§5.1.3), which feeds into the form factor bound and ultimately into the RG recursion $C_{k+1} = C_k/4 + C_\mathrm{new}$ (Step 12).

---

## 2. Attack vectors — assessed one by one

### Attack 1: Domain mismatch — does the preprint stay within what Balaban proved?

**Balaban's actual domain (CMP 109/119):** Pure $\mathrm{SU}(2)$ (and, by the CMP 95–96 + CMP 102 series, extendable to $\mathrm{SU}(N)$ — this extension is addressed in Appendix K) Yang-Mills with the **standard Wilson plaquette action** $S_\mathrm{4D}[U]$ alone, on a 4D hypercubic lattice. Balaban's block-spin transformation acts only on the link variables $U_\ell \in \mathrm{SU}(N)$.

**What the preprint feeds to Balaban:** At the continuum-limit stage (§5.1), Balaban's RG is applied within each fixed bare theory $K$. The preprint states (§5.1.2) that "we use his results as a black box" and that the relevant input is the standard Wilson action. The IR equivalence (Theorem 5, §4.5) is proved *separately* at the lattice level: it shows that at bare scale $a \gg r_3$, the reduced transfer matrix of the KK theory has the same spectral gap as the standard $\mathrm{SU}(N)$ theory, with exponentially small corrections.

**The gap:** The preprint's use of Balaban in §5.1 treats the bare action as if it were the **standard Wilson action**, without explicitly arguing that Balaban's construction — which acts on $U_\ell$ alone — is valid when the underlying measure also includes the $A_x$ fiber fields. There are two sub-issues:

**(a) Action form input.** Balaban's small-field/large-field decomposition (CMP 109, §2) is stated for the Wilson action $S_\mathrm{4D}[U] = \beta \sum_P (1 - \frac{1}{N}\mathrm{Re}\,\mathrm{Tr}\,U_P)$. The KK theory has an additional piece $S_\mathrm{int}[U,A]$. After integrating out $A_x$ fields (which is the physical interpretation of the cluster expansion in §4), the **effective 4D action** for $U$ alone receives corrections of size $e^{-m_1 a}$ per bond (Theorem 2). This modified action is **not** the standard Wilson action; it is the Wilson action plus exponentially small corrections with magnitude $\sim e^{-m_1 a} \approx e^{-10^{15}}$ at physical scales.

The preprint's UV stability theorem box (§5.1.2) silently assumes this exponentially small perturbation does not invalidate Balaban's construction. This is almost certainly true but is **not argued**. Balaban's UV stability proof requires the action to satisfy specific inductive hypotheses (CMP 109, §3): in particular, the background effective action at each step must remain in the small-field region and must have a specified analytic form. A perturbation of the input action by $e^{-10^{15}}$ per plaquette would satisfy these hypotheses easily — but this is a **reading exercise** that has not been completed.

**(b) Two-index structure.** The preprint correctly distinguishes the "outer" bare-refinement index $K$ from the "inner" Balaban step $k$ (§5.1.2, careful remark box). Within each fixed $K$, Balaban's RG is applied. However, the input at $k=0$ within each bare theory is the reduced (KK-integrated) effective action, not the pure Wilson action. The preprint does not write down this effective action explicitly before invoking Balaban.

**Severity:** WEAKENED. The gap is not fatal because: (1) the KK corrections are $O(e^{-m_1 a})$ and Balaban's domain hypotheses are open conditions (small-field region, analyticity radius); (2) Objection G in §6 was assessed as [CONFIRMED], but the confirmation cites the cluster expansion giving a "standard" effective action without exhibiting the explicit modified action form. However, the argument is incomplete as written — a referee will ask for it.

---

### Attack 2: SU(2) vs SU(N) — does the extension hold?

**Balaban's published theorem:** Primarily for $\mathrm{SU}(2)$, with some elements for $\mathrm{SU}(N)$.

**The preprint's response:** Appendix K gives a full step-by-step extension to any compact simple group $G$. It identifies the three group-dependent quantities (covariant Laplacian Lipschitz constant $C_D = O(N^2)$, polymer convergence $\kappa(N) > 0$, block-spin projection radius $r_\mathrm{proj}(N) > 0$) and verifies each is finite and $k$-independent for each fixed $N$. Section 5.1.2 cites this directly.

**Verdict on this attack:** SURVIVES. Appendix K is thorough. The $N$-dependence of constants is polynomial and tracked. This is not a gap.

---

### Attack 3: Are the stability constants k-independent, or does k-dependence leak through?

**The claim:** Balaban's theorem requires $\kappa$ (the polymer decay rate), $m_W$ (the fluctuation mass), and $r_\mathrm{proj}$ (the block-spin projection radius) to all be $k$-independent.

**The preprint's treatment:** Appendix H (§5.2) and PROOF-CHAIN.md §IV.3 confirm this by citing: (i) CMP 109, §3 (inductive hypotheses — $\kappa$ explicitly $k$-independent); (ii) CMP 95, Prop. 1.2 (propagator decay $\delta_0$ depends only on $d$ and $m_W^2$, both fixed); (iii) CMP 98, §E (kernel geometry fixed, $r_\mathrm{proj}(N)$ depends on $N$ only).

**Potential vulnerability:** The "fluctuation mass" $m_W^2$ used in CMP 95 is the infrared regulator inserted by Balaban into the gauge-fixed action. In the standard Balaban program, $m_W a_k$ is held fixed (this is the Pauli-Villars-like mass). The preprint does not explicitly state that $m_W a_k$ is held fixed across inner RG steps, though this is standard in the Balaban program. If $m_W$ runs, then $\kappa$ could depend on $k$.

**Verdict on this attack:** SURVIVES as currently constituted, but barely. Section K.2 states "$m_W a_k$ is held fixed through the RG" and CMP 95, Prop. 1.2 is verified against the journal. The $k$-independence of $\kappa$ follows. However, the one sentence confirming $m_W a_k$ fixed is in Appendix K, not in §5.1, and the connection is implicit. A footnote in §5.1.3 would close this.

---

### Attack 4: Large-field/small-field decomposition — known weak point in Balaban

**The known technical difficulty:** Balaban's most technically demanding step is the large-field/small-field decomposition (CMP 119 is almost entirely devoted to this). The large-field region $\Omega_l$ (where $|F_{\mu\nu}| \geq p(g_k) = g_k^{1-\epsilon}$) is handled by showing configurations there have probability $O(e^{-c/g_k^{2\epsilon}})$. The small-field region $\Omega_s$ is where the polymer expansion runs.

**The preprint's treatment:** The preprint uses the polymer expansion (for the KK cluster expansion) and the large-field suppression (citing CMP 119 for rough configurations, line 839 of §4) as black boxes. The critical point: Balaban's large-field bound requires the **plaquette curvature** $|F_{\mu\nu}|$ to be small, controlled by $g_k^{1-\epsilon}$. In the KK theory, there is no modification of the plaquette curvature — it depends only on $U_\ell \in \mathrm{SU}(N)$, not on $A_x$. So the KK extension does not change the large-field/small-field boundary.

**Verdict on this attack:** SURVIVES. The large-field/small-field decomposition is applied to $U_\ell$ variables, which are the same in both theories. The $A_x$ fields decouple. This is implicitly correct, though again not explicitly stated.

---

### Attack 5: Citation mapping — does the preprint cite the correct theorem?

**What CMP 109 actually proves (structural):** CMP 109 is "Generation of effective actions in a small field approximation and coupling constant renormalization in 4 dimensions." It generates the small-field effective action and proves the polymer expansion converges (Theorem 1/Theorem 3). It does **not**, by itself, complete the UV stability program — that requires CMP 119 ("Convergence of the renormalization group in the $d = 4$ small field approximation").

**What CMP 119 proves:** The convergence of the renormalization group iteration. This is the UV stability proper.

**The preprint's citation:** PROOF-CHAIN.md §IV.1, Step 2 cites "CMP 109, 119" for UV stability. Section 5.1.2 quotes the theorem without specifying which theorem in which paper it is. Appendix H §2.4 correctly identifies: "CMP 102 establishes the full program in $d=3$. CMP 119 extends the convergent polymer expansion to $d=4$."

**The gap:** The preprint does not cite a specific theorem number or section in CMP 119 for the UV stability theorem. The theorem invoked in §5.1.2 — "for $g_0$ sufficiently small, the block-spin RG can be iterated indefinitely" — is the content of CMP 119 (main theorem, described as "unnumbered, p. 245" in Appendix H §3, Step (a)). This is thin. The preprint's own Appendix H §5.1 (Honest Assessment table) notes that the convergent polymer expansion in $d=4$ is a "Stated theorem" in CMP 109, 119 — but does not give a specific theorem number from CMP 119.

**Verdict on this attack:** WEAKENED. The UV stability black box invoked in §5.1.2 does not have a pinned theorem number and section in CMP 119. Appendix H attributes it to "p. 245" of CMP 119 (unnumbered theorem), which is extremely thin for a Millennium Problem proof. A referee will require a precise statement with equation numbers. This is not a mathematical gap (the result is in CMP 119 and the paper acknowledges this), but it is a documentation gap that could be exploited to demand full verification.

---

### Attack 6: KK-Balaban compatibility — does adding KK fiber modes to the action preserve Balaban's input hypotheses?

This is the central attack vector and Objection G of §6.

**The precise claim the preprint must establish:** Balaban's UV stability applies to a theory with action $S[U] = S_\mathrm{4D}[U]$ (pure Wilson) plus corrections of size $e^{-m_1 a}$ per bond. The effective 4D action after marginalizing the fiber fields is **not** the pure Wilson action. It has corrections.

**What Objection G says:** "Verifying that the effective 4D action from the cluster expansion satisfies Balaban's input requirements requires an explicit check." Resolution: "[CONFIRMED] — See verification report."

**The actual verification report (preprint-verification/verify-balaban-items.md):** This file does not exist at the path specified; the link is broken. The preprint cites it, but the file cannot be read. The confirmation in §6 therefore rests on a **missing verification document**.

**What Appendix H §5.2 says:** "(i) Genuine mathematical holes (something that might be false): None identified." But Appendix H is not the verification report. The verification report was supposed to be at `preprint-verification/verify-balaban-items.md` (referenced in PROOF-CHAIN.md §IV.3 and §6). That file is absent.

**Severity assessment:** This is a **documentation gap with potential mathematical content**. The claim that the effective 4D action (with $O(e^{-m_1 a})$ KK corrections) satisfies Balaban's input requirements is not formally verified anywhere accessible. The argument is physically obvious (Balaban's hypotheses are open conditions, the KK corrections are $O(e^{-10^{15}})$ at physical scales) but is not written down. For a Millennium Problem submission, this is a material weakness.

---

## 3. Summary of findings

| Attack | Verdict | Severity |
|:-------|:--------|:---------|
| 1a. Action form: KK corrections not in Balaban's domain | WEAKENED | Repairable (explicit decoupling argument needed) |
| 1b. Two-index structure: input action not exhibited | WEAKENED | Repairable (one paragraph) |
| 2. SU(2) → SU(N) extension | SURVIVES | Appendix K adequate |
| 3. k-independence of stability constants | SURVIVES (barely) | One sentence in §5.1.3 needed |
| 4. Large-field/small-field decomposition | SURVIVES | No structural issue |
| 5. Missing precise CMP 119 theorem number | WEAKENED | Repairable (documentation) |
| 6. KK-Balaban compatibility: verification report missing | WEAKENED | Repairable but material |

**Overall verdict: WEAKENED.**
Link 2 is not BROKEN. The UV stability theorem (Balaban CMP 109, 119) is a genuine published result and Appendix K + Appendix H demonstrate the authors understand the construction. However, four repairable gaps exist, of which Attack 6 (missing verification report) is the most material for a referee.

---

## 4. Repair recommendations

**R1 (Attack 1/6, material).** Insert a subsection §5.1.0 ("KK-to-standard reduction") that explicitly writes down the effective 4D action $S_\mathrm{eff}[U] = S_\mathrm{4D}[U] + \delta S_\mathrm{KK}[U]$, states $|\delta S_\mathrm{KK}|_{L^\infty} \leq C e^{-m_1 a/2}$ from Theorem 2, and verifies that Balaban's small-field/analyticity-radius hypotheses (CMP 109, §3, inductive assumptions (H1)–(H5)) are satisfied by $S_\mathrm{eff}$ because the KK perturbation is sub-dominant. This is a 1–2 page argument.

**R2 (Attack 5, documentation).** Add "CMP 119, Theorem (p. 245 of the published journal), proved in Sections 2–4 of that paper" as a footnote in §5.1.2. Cross-reference Appendix H §2.4 explicitly.

**R3 (Attack 3, minor).** Add a footnote in §5.1.3 confirming that $m_W a_k$ is held fixed across inner RG steps, citing Balaban's convention (CMP 109, p. 252) and Appendix K.2.

**R4 (missing file).** The file `preprint-verification/verify-balaban-items.md` referenced in §6 (Objection G) and PROOF-CHAIN.md §IV.3 does not exist at the declared path. Either restore the file or redirect the citation to Appendix H + Appendix K.

---

## 5. Verdict record

```
LINK:       2
STATEMENT:  UV stability (Balaban CMP 109, 119)
VERDICT:    WEAKENED
CONFIDENCE: 7/10 (would be 9/10 after R1 repair)
BREAKS:     No
ATTACKS:    6 vectors tested; 4 survive; 2 weaken; 0 break
REPAIR:     R1 (§5.1.0 KK-to-standard reduction, ~1-2 pages)
            R2 (CMP 119 theorem pin)
            R3 (m_W footnote)
            R4 (restore missing verification file)
AUTHOR_NEEDED: Yes (R1 requires mathematical content)
```

---

*Critic: PCA Wave 1 — 2026-04-13*
