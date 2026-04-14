# Link 14 Wave 3 Critic

**Verdict:** WEAKENED — the repair closes the book-keeping contradiction (Sub-problem A) cleanly, and the architecture of the Polymer-Sum Spectral Lemma (Sub-problem B) is correct, but two quantitative joints are asserted rather than proved and at least four preprint occurrences of "Conjecture 1" are left behind by the proposed edit set. The headline "Theorem 8 unconditional" is defensible on the §5.5.3-(i) Hastings–Koma route (which the preprint already has), but the §5.5.6 route the Author actually writes has an unverified margin condition and an incorrectly cited Kotecký–Preiss threshold.

---

## Vector A findings — the three-way contradiction

**A.1 Theorem 8 title + "Assume Conjecture 1" clause.** PASS on the "from" quote.
Verified at `preprint/sections/05-continuum-limit.md` lines 2002–2003:
> `**Theorem 8 (Conditional continuum mass gap).** *Assume Conjecture 1 holds with exponent $s \geq 2$. Then:*`
The Author's Edit 6 "from" text matches the preprint verbatim.

**A.2 §5.4.7 status table.** PASS on the "from" quote.
Verified at lines 1035–1043:
> `The remaining problem is Conjecture 1, now sharpened: ... The RG recursion is controlled; it remains to prove the single-step bound $C_{\mathrm{new}}$.`
Matches Edit 1 "from" verbatim.

**A.3 §5.5.5 conditional rows.** PASS on the "from" quote.
Verified at lines 1563–1565:
> `| $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ (non-perturbative) | **Conditional** on (B1)-(B2) | ...`
Matches Edit 3 verbatim.

**A.4 §5.5.3 "Uniform temporal extent" remark — citation of CMP 109 Thm 1.** PASS on the mis-citation claim.
Verified at lines 1504–1509:
> `Since Balaban's polymer expansion generates operators supported within connected polymers of diameter bounded by $R_0$ block lattice units (CMP 109, Theorem 1), the temporal extents satisfy $R_i \leq R_0$ uniformly in $i$ and $k$.`
Cross-referencing §5.6 Part I (lines 1595–1598, which carefully cites the same CMP 109 Thm 1):
> `|K_k(X, V)| \leq e^{-\kappa |X|}, with $\kappa > 0$ independent of $k$ (CMP 109, Section 3)`
CMP 109 Thm 1 gives **exponential decay**, not a uniform temporal-diameter bound. The Author is right: the §5.5.3 remark confuses "typical size" with "uniform bound". **The mis-citation is real.**

**A.5 FAIL — orphan "Conjecture 1" references.** The Author's 9-edit set **misses four additional occurrences** that a reader will hit after the update:
- Line 194: `non-perturbative (Conjecture 1) is established in Section 5.6.` — still reads as if a discharge is pending, not done.
- Line 323: `matrix element bound (Conjecture 1 in Section 5.4)`
- Line 358: `This is Conjecture 1 (Section 5.4).`
- Line 380: `The proof continues via the matrix element bound (Conjecture 1, ...)`
- Line 2991 (in the §5.7 "Remarks"): `2. **Without Conjecture 1.** The operator norm bound gives $|\delta\Delta_k/\Delta_k| \leq Cg_k^4/(a_k\Lambda)$; $\sum g_k^4/(a_k\Lambda) \sim \sum 2^k/k^2$ diverges.`
- Appendix G (`sections/G-multi-time-slice-analysis.md`) line 6 and line 377 still contain live "Conjecture 1 at $d_O = 6$ stands" phrasing.

Edit 1 discharges Conjecture 1 in §5.4.7 and Edit 6 in §5.7, but the remark at line 2991 still framing "Without Conjecture 1" as a live branch is now stale — the repair should either strike it or rewrite it as a pedagogical counterfactual. Voice-alignment §J: the repair doesn't finish the sweep.

**A.6 New Theorem 8 statement accuracy.** PARTIAL PASS. Edit 6 rewrites (a) from `(a_k\Lambda)^s` to `(a_k\Lambda)^2`, consistent with the $s=2$ discharge. But §5.6 Part III.5 (lines 1885–1892) already uses operator-norm $M = \|\delta E_k^{d=6}\| \leq Cg_k^4$ with the single-operator spectral lemma — it does NOT actually invoke the new §5.5.6 polymer-sum lemma. The Author's claim that §5.6 Part III "requires" the polymer-sum lemma is itself disputable: §5.5.3 Step 3(i) (lines 1334–1339) ALREADY contains a polymer-aware extension:
> `For the polymer-aware extension: each polymer $K(X)$ with $\|K(X)\| \leq e^{-\kappa|X|}$ satisfies the same bound with $C_p^*$ independent of $|X|$, because the Hastings-Koma constant depends on the physical support (not the lattice-unit count). The sum $\sum_{X \ni 0} C_p^* e^{-\kappa|X|} = C_p^* C_{\mathrm{KP}} < \infty$ converges by Kotecký–Preiss.`

This is the **Hastings–Koma route**: $C_p^*$ is $|X|$-independent because clustering is bounded by physical support, not lattice-unit temporal extent. Under this route, one does NOT need the $\kappa > 2\log(1+\zeta)$ margin. The Author's new §5.5.6, using the $(1+\zeta)^{2R(X)-1}$ form of (S3.1), reintroduces a margin condition that the Hastings–Koma route already bypasses. **The Wave-2 repair silently relitigates a polymer bound that already exists at §5.5.3 Step 3(i) in a stronger form.**

---

## Vector B findings — the polymer-sum spectral lemma as written

**B.1 PS-iv margin $\kappa > 2\log(1+\zeta)$ — UNVERIFIED.**
The Author claims (repair Step 6, "Verify PS-iv") that §5.5.3 Step 3 gives $\zeta \leq C(R_0,N)$ and that CMP 109 gives $\kappa \gtrsim 1$, so $2\log(1+\zeta) < \kappa$ holds "with margin". Independent check of the preprint: §5.5.3 Step 3(ii) (lines 1346–1430) only proves $E_2 - E_1 \geq \hat\Delta_k/2$ for $g_k^2 \leq 1/(2\sqrt{C_B})$, which yields $\zeta = \sum_{n\geq 1} e^{-(E_n-E_1)} \leq \zeta(R_0,N)$ but **no explicit numerical bound on $\zeta$ is given**. The Author asserts "for $\zeta \leq 1/2$ and $\kappa \geq 2$, the condition holds with margin" — **neither bound is established in the preprint.** $\kappa$'s numerical value from CMP 109 §3 is never stated; the preprint only says "$\kappa_{\mathrm{B}}$ is $O(1)$ in physical units" (line 929). "$O(1)$" does not establish $\kappa > 2\log(1+\zeta)$. This is a **plug-number-by-hope** step.

**B.2 Kotecký–Preiss threshold $\kappa' > \log(2d) = \log 8$ — MIS-STATED.**
The Author cites: `Kotecký-Preiss (CMP 103, 1986), Thm 1` and says convergence requires `$8 e^{-\kappa'} < 1$, i.e., $\kappa' > \log 8$`. This is an **oversimplified** version of the Kotecký–Preiss criterion. The actual KP criterion for connected subsets of $\mathbb{Z}^d$ is that the *number* of connected lattice animals containing a given site $0$ with $|X| = n$ grows as $\alpha_d^n$ for the **animal connective constant** $\alpha_d$ (for $d=4$, $\alpha_4 \approx 8.3\ldots$, strictly greater than $2d = 8$; cf. Miranda–Slade). Convergence requires $\kappa' > \log\alpha_d$, not $\kappa' > \log(2d)$. The Author's threshold is **too loose by a constant**, though not fatal — but the citation of CMP 103 for the $\log(2d)$ form is wrong (Kotecký–Preiss's criterion is $\sum_X |K(X)| a(X) \leq a(y)$ for a weight function, not a bare exponent threshold).

More importantly: the preprint's own §5.4.5 lemma (lines 892, 901–902) uses the same polymer sum in a different form with $\kappa_{\mathrm{cl}}^*$, and §5.4.6 line 982 writes:
> `C_{\mathrm{np}} = \sum_X e^{-\kappa_{\mathrm{B}}|X|}|X|^2 < \infty`
which implicitly uses the same KP-type summability. So the summability IS plausible, but the Author's specific threshold arithmetic ($\kappa' > \log 8$) is folklore-level, not tied to a specific CMP 103 theorem. **WEAKEN.**

**B.3 $R(X) \leq |X|$ (PS-iii) — PASS with caveat.**
By elementary geometry, a connected subset $X \subset \mathbb{Z}^4$ has diameter $\leq |X| - 1$ (actually $\leq |X|$), so its projection onto the time axis has diameter $\leq |X|$. OK. The Author's self-suspicion S3 acknowledges this bound is loose and the argument survives; agreed.

**B.4 The single-operator $(1+\zeta)^{2R-1}$ prefactor matches (S3.1) — PASS.**
Verified at line 1435: `|\langle m|\mathcal{O}|m\rangle| \leq M\,(1+\zeta)^{2R-1}\,(C_*\hat{\Delta})^p`. The form cited in the repair matches the preprint. Good.

**B.5 $k$-uniformity of $C_{\mathrm{new}}$.** CONDITIONAL PASS. Each input ($C_6$, $C_*$, $\zeta$, $\kappa'$) is claimed $k$-uniform. $C_6$ from CMP 109: yes, by preprint line 929 ($\kappa_{\mathrm{B}}, m_W, C_D$ are $L=2, d=4, N$-only). $C_*$ from §5.5.3: yes, line 1429. $\zeta$: yes (same line). $\kappa'$: yes, **provided PS-iv holds**, which is B.1's open question. So $k$-uniformity reduces to PS-iv, which is not quantitatively closed. **WEAKEN**, not BROKEN — the physics is plausible, the arithmetic is not.

**B.6 Early-$k$ absorption.** The Author invokes §5.4.6 ("Treatment of the first $k_0(K)$ inner steps", lines 965–992). Verified: §5.4.6 does absorb the first $k_0(K)$ steps into $C_0^{\mathrm{cl}}$. The mechanism transfers. PASS.

**B.7 Crucial redundancy with §5.5.3 Step 3(i).** The existing polymer-aware paragraph at lines 1334–1339 **already gives** $\sum_{X\ni 0} C_p^* e^{-\kappa|X|} \leq C_p^* C_{KP} < \infty$ via Hastings–Koma locality (no $R$-dependence in $C_p^*$). If this paragraph is correct, the new §5.5.6 is superfluous and its $\kappa > 2\log(1+\zeta)$ margin is not needed. If this paragraph is NOT correct (because $C_p^*$ does depend on temporal extent through the $(1+\zeta)^{2R-1}$ factor per (S3.1)), then the preprint's §5.5.3 Step 3(i) already has the same unverified claim as §5.5.6. The Author has not addressed this tension: either §5.5.3 Step 3(i) is right and §5.5.6 is unnecessary, or §5.5.3 Step 3(i) is wrong and §5.5.6 uses an incompatible route. **This is a structural gap in the repair.**

---

## Vector C findings — downstream consistency

**C.1 L11 ($C_{\mathrm{new}}$ bound) — PASS.** Edit 8 updates row 11 to cite §5.5.6. Consistent.

**C.2 L13 ($\Sigma$ summability) — PASS.** L13 uses the outer refinement $2^{-Ks}$ times $g_K^4 \sim 1/K^2$ (preprint §5.4.6 lines 950–963). The repair changes $C_{\mathrm{new}}$'s provenance but not its value; the ratio test still closes. No impact.

**C.3 L10b (spectral lemma $C_p$ k-independent) — PASS**, but with observation: L10b is the §5.5.3 Step 3 claim, which the Author partly co-opts for PS-iv. No contradiction.

**C.4 §IV.4 Verdict (PROOF-CHAIN.md).** Line 110 already says "complete and unconditional" and line 121 ASCII diagram already says "Conj. 1 discharged". The status table row 14 already says "Proved". So §IV.1 is **already** in a state where the top-level verdict contradicts Theorem 8's "Conditional" title. The repair's Edit 9 strengthens §IV.4 but does not solve the fact that the status table/verdict pre-emptively discharged Conjecture 1 before the actual lemma existed. After the repair this will be retroactively consistent; before, it was asserting without support.

---

## Vector D findings — rigor label

The research note `21-the-rigorous-proof.md` (line 6) defines THEOREM = "Rigorously proved, either here or in the cited source". The Author's new §5.5.6 claims THEOREM rigor. Under a strict reading:

- The proof's steps A, B, C are computational and correct *assuming* PS-i–PS-iv.
- PS-i–PS-iii are rigorously proved in the preprint (§5.6 Part I; §5.6 Part III.3; geometry).
- PS-iv is NOT rigorously proved in the preprint. The Author's verify-step handwaves it to "$\zeta \leq 1/2$, $\kappa \geq 2$, holds with margin" — neither inequality is established in §5.5.3.

Per the rigor catalogue, an argument with one input still awaiting a quantitative bound is a **KEY LEMMA**, not a THEOREM. The Author's rigor label is too strong.

**Verdict on Vector D: KEY LEMMA, not THEOREM.** The §5.5.6 insertion should be labelled KEY LEMMA pending explicit quantitative bounds on $\zeta$ and $\kappa_{\mathrm{B}}$ in physical units.

---

## Vector E findings — self-suspicion audit

The Author raised three failure modes (S1 backward-verification, S2 early-$k$ threshold, S3 temporal support looseness). S1 and S3 are fairly treated. S2 is waved off via §5.4.6, which is legitimate.

**Missed failure mode S4.** The entire repair presumes that $\delta E_k^{d=6}$ is a **literal polymer sum** $\sum_{X\ni 0} K_k^{d=6}(X,\cdot)$ with individual-polymer dev-order $\geq 2$. But §5.6 Part III's dim-6 classification (lines 1769–1857) classifies **the full operator** $\delta E_k^{d=6}$, not each polymer activity $K_k^{d=6}(X,\cdot)$ separately. The Author's PS-ii asserts `$\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$ for every $X$`, but §5.6 Part III.3 proves dev-order at the level of monomials in the operator basis, not per-polymer. A polymer activity $K_k^{d=6}(X,\cdot)$ is a *spatial-support-restricted* linear combination of basis monomials; the dev-order statement applies monomial-by-monomial and the per-polymer statement requires the "linear combination" lemma (§5.5.3, lines 1473–1502), which is the very lemma whose "uniform temporal extent" remark the Author has just rejected. **Circular dependency risk.** The per-polymer dev ≥ 2 claim needs an independent justification that does not reinvoke the lemma whose uniformity hypothesis fails for polymers.

**Missed failure mode S5.** The cross-reference: line 194 still says "non-perturbative (Conjecture 1) is established in Section 5.6" — not updated to point to §5.5.6. Line 2991 ("Without Conjecture 1") is now stale. Edit sweep incomplete.

---

## Vector F findings — bonus-grep

**F.1 "Conjecture 1" grep across preprint/sections/** returned 13 hits in `05-continuum-limit.md` plus 2 in `G-multi-time-slice-analysis.md`. Edits 1, 6, 7 touch 4 of them (lines 1031, 1035, 1995, 2002, 2023). Untouched hits at **lines 194, 323, 358, 380, 1898, 2991** (in 05) and **lines 6, 377** (in G) — 8 places where a reader will see "Conjecture 1" framed ambiguously or as a live item. Voice-alignment: repair is partial.

**F.2 "polymer-sum" / "polymer sum" grep across preprint/sections/** returned **zero matches**. The Author's new §5.5.6 introduces a phrase not used elsewhere — no existing location silently assumes the single-operator version. PASS on this vector.

---

## Summary

The repair resolves the cosmetic three-way contradiction and proposes an architecturally correct Polymer-Sum Spectral Lemma route. Four substantive concerns:

(i) **Orphan "Conjecture 1" references.** Eight preprint locations outside the nine proposed edits (lines 194, 323, 358, 380, 1898, 2991 in §5; lines 6, 377 in Appendix G) still frame Conjecture 1 ambiguously or as live. Edit sweep must extend.

(ii) **PS-iv is not quantitatively closed.** The condition $\kappa > 2\log(1+\zeta)$ is asserted without explicit numerical bounds on either side from the preprint. §5.5.3 Step 3 bounds $\zeta$ abstractly; CMP 109 gives only "$O(1)$" for $\kappa_{\mathrm{B}}$.

(iii) **Redundancy with §5.5.3 Step 3(i).** The preprint already has a polymer-aware Hastings–Koma bound (lines 1334–1339) with $C_p^*$ $|X|$-independent, which does NOT need the PS-iv margin. The repair does not reconcile its §5.5.6 route with this existing weaker-hypothesis route.

(iv) **Rigor label.** §5.5.6 should be KEY LEMMA pending explicit $\zeta$ and $\kappa_{\mathrm{B}}$ bounds, not THEOREM.

**Verdict: WEAKENED.** Architecture SURVIVES; quantitative closure and edit-sweep do not. Close (i)–(iv) to upgrade.
