# Link 11 Wave 5 Critic: C_new g_k^4 Δ̂² bound

**Verdict: SURVIVED**

**Wave:** 5 (final verification of Wave 4 patch)
**Critic:** Claude Sonnet 4.6 · 2026-04-13
**Instance:** Independent — different from L11 Wave 2/Wave 4 Authors

---

## Per-check findings

### C1 — Exponent $(R_0-1)$ in patch vs preprint §5.5.3 line 1446 and Appendix I.3 item 10

**Preprint §5.5.3 line 1446 verbatim** (05-continuum-limit.md, line 1446):

> Setting $C_p = 2C_*^p(1+\zeta)^{R_0-1}$, with $C_* = e^{\hat\Delta_{\max}}$ k-independent:

**Appendix I.3 item 10 verbatim** (I3-N-dependence-tracking.md, line 216):

> Then $C_p(N) = 2C^p(1 + \zeta(N))^{R_0-1}$, which can grow as $\exp(C_1\,R_0^4\,N^2)$.

**Patch (L11-patch.md, revised PE-3):**

> Setting $C_p = 2C_*^p(1+\zeta)^{R_0-1}$ (§5.5.3, line 1446) …

**Verdict: MATCH.** The patch carries exponent $(R_0-1)$ in both the formula and the derivation of $C_2(N)$. This directly corrects the Wave 2 error of $(2R_0-1)$ that the Wave 3 critic identified. The line 1510 formula $(2R_0-1)$ is the multi-operator extension; the patch correctly cites and applies the single-operator base formula at line 1446. No discrepancy remains.

---

### C2 — Notation "C(R₀,N)" vs preprint lines 1279 and 1428

**Preprint §5.5.3 line 1278–1279 verbatim:**

> where $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$. We establish that $\zeta$ is bounded by a constant $\zeta(R_0, N)$ independent of the volume $L$ and the RG step $k$.

**Preprint §5.5.3 line 1428 verbatim:**

> Combining (i) and (ii): $\zeta \leq C(R_0, N)$ with $C$ independent of $k$ and $L$.

**Patch (L11-patch.md, revised PE-3):**

> $$\zeta \;\leq\; C(R_0, N) \;\leq\; \exp\!\big(C_1\,R_0^3\,(N^2-1)\big),$$
>
> (§5.5.3, lines 1279 and 1428; Appendix I.3, item 10)

**Patch (revised §D toolkit row):** canonical name `C(R₀,N) bound (Combes–Thomas, Link 11)`.

**Verdict: MATCH.** The patch adopts "C(R₀,N)" as the name of the bounding constant, consistent with the preprint's resolved convention at line 1428 and I.3 item 10. The earlier "ζ(R₀,N)" at lines 1278–1279 (preprint's own notational drift, as the patch's SS-2 notes) is not a fixed convention; the patch correctly privileges the later line 1428 form. The Wave 3 editorial imprecision (Vector C) is fully resolved. The toolkit row in the Wave 2 repair used "ζ(R₀,N)" where the preprint calls the bound "C(R₀,N)"; the Wave 4 patch corrects this verbatim.

---

### C3 — Does $C_\mathrm{new}(N) \leq K_0 \exp(K_1 R_0^4 N^2)$ follow from the corrected $(R_0-1)$ exponent?

**Chain of reasoning in patch:**

1. $\zeta \leq C(R_0, N) \leq \exp(C_1 R_0^3 (N^2-1))$ — from preprint line 1428 and I.3 item 10, line 214.
2. $(1+\zeta)^{R_0-1} \leq \exp(\zeta(R_0-1)) \leq \exp(C_1 R_0^3 (R_0-1)(N^2-1))$.
3. $C_2(N) = 2 e^{2\hat\Delta_{\max}} (1+\zeta)^{R_0-1} \leq \tilde C_0 \exp(C_1 (R_0-1) R_0^3 (N^2-1))$.
4. Since $(R_0-1) \cdot R_0^3 \leq R_0^4$: $C_2(N) \leq \tilde C_0 \exp(C_1 R_0^4 N^2)$.
5. Operator norm bound $C(N) = O(N^{2p_B})$ (polynomial from Mayer resummation); absorbed into $K_0$.
6. $C_\mathrm{new}(N) = C_2(N) \cdot C(N) \leq K_0 \exp(K_1 R_0^4 N^2)$.

**Verdict: CORRECT.** Each step is a valid upper bound. The correction from $(2R_0-1)$ to $(R_0-1)$ strictly tightens the intermediate constant ($(R_0-1) R_0^3$ vs $(2R_0-1) R_0^3$), but the final form $K_0 \exp(K_1 R_0^4 N^2)$ is preserved since $(R_0-1) R_0^3 \leq R_0^4$ absorbs either. I.3 item 10 (line 217) independently confirms "$C_p(N) = 2C^p(1+\zeta(N))^{R_0-1}$, which can grow as $\exp(C_1 R_0^4 N^2)$," exactly matching the patch's boxed bound. The bound is now internally consistent with the preprint and tighter (not looser) than Wave 2.

**Residual flag (inherited, not introduced by patch):** I.3 line 212 uses $R_0^3$ for the local Hilbert space dimension without explicit justification of the surface vs volumetric counting in 4D. The patch (SS-3) correctly flags this as a pre-existing preprint ambiguity; the final $R_0^4$ bound absorbs either convention. No new error introduced.

---

### C4 — Does the patch preserve L13's ratio-test convergence (1/4, N-independent)?

**L13 critic verdict:** SURVIVED (all five attack vectors fail; doubly-exponential $4^{-K}$ dominates).

**I.3 Lemma I.3.1** (I3-N-dependence-tracking.md, lines 280–330): ratio test limit
$$\frac{(k+1)^{\gamma(N)-2} \cdot 4^{-(k+1)}}{k^{\gamma(N)-2} \cdot 4^{-k}} \;\xrightarrow{k\to\infty}\; \frac{1}{4} < 1$$
is $N$-independent because $4^{-k}$ is a geometric-lattice property ($L=2$, $d=4$: $2^{-d} = 1/16$ volume, $2^{-2} = 1/4$ mass-gap scaling per step), not a group-theory property.

**Patch's PE-3 explicitly states** (L11-patch.md, line 104–108):

> The $N$-growth of $C_{\mathrm{new}}$ does not affect the convergence of the RG sum $\sum_k C_k g_k^4 \hat{\Delta}_k^2 < \infty$ (Link 13): the geometric factor $4^{-k}$ in $\hat{\Delta}_k^2$ dominates any finite sub-exponential in $N$; the ratio test limit $1/4 < 1$ is $N$-independent (Appendix I.3, Lemma I.3.1).

**Verdict: PRESERVED.** $C_\mathrm{new}(N)$, however large for fixed $N$, enters L13 only as a multiplicative prefactor $C_* = (4/3) C_\mathrm{new}(N)$ in the fixed-point equation (I.3 Step 12). It does not enter the geometric convergence factor. The ratio test limit remains $1/4$ regardless of $N$, confirming the patch introduces no interference with L13. L13's SURVIVED verdict is unaffected.

---

## Summary (≤150 words)

**SURVIVED.** The Wave 4 patch correctly addresses both defects the Wave 3 critic identified. C1: the exponent $(R_0-1)$ in the revised PE-3 matches preprint §5.5.3 line 1446 and Appendix I.3 item 10 verbatim; the Wave 2 error of $(2R_0-1)$ is eliminated. C2: the toolkit row and PE-3 adopt "C(R₀,N)" as the canonical name for the Combes–Thomas bound, consistent with preprint lines 1428 and I.3 item 10, resolving the Wave 3 editorial imprecision. C3: the boxed bound $C_\mathrm{new}(N) \leq K_0 \exp(K_1 R_0^4 N^2)$ follows correctly from the corrected exponent via the clean chain $(R_0-1) R_0^3 \leq R_0^4$; I.3 item 10 confirms the form independently. C4: the ratio test limit $1/4 < 1$ remains strictly $N$-independent; L13's convergence is unaffected. One pre-existing preprint ambiguity ($R_0^3$ link-counting in I.3 line 212) is inherited and flagged, not introduced. No logical gap in the corrected link.
