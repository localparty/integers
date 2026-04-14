# Link 14 Wave 5 Critic

**Verdict:** WEAKENED — the patch closes three of Wave 3's four findings cleanly, but one structural gap inherited from Wave 3's missed failure mode S4 is not addressed. The Hastings–Koma route is sound; the edit sweep is complete and verbatim-accurate; the rigor-label dispute is dissolved. What remains is a per-polymer dev ≥ 2 assertion in Edit 4 that §5.6 Part III.3 does not actually support at the level claimed.

---

## C1 — Verbatim accuracy of §5.5.3 Step 3(i) quote

**PASS.**

The patch quotes lines 1334–1339 of `preprint/sections/05-continuum-limit.md` as:

> **For the polymer-aware extension:** each polymer $K(X)$ with
> $\|K(X)\| \leq e^{-\kappa|X|}$ satisfies the same bound with $C_p^*$
> independent of $|X|$, because the Hastings--Koma constant depends on
> the physical support (not the lattice-unit count). The sum
> $\sum_{X \ni 0} C_p^* e^{-\kappa|X|} = C_p^* C_{\mathrm{KP}}
> < \infty$ converges by Koteck\'y--Preiss.

Independent read of the preprint at lines 1334–1339 matches character-for-character (LaTeX ligatures included). The paragraph does supply:

- a single-polymer bound with $C_p^*$ declared $|X|$-independent,
- an explicit polymer sum via Kotecký–Preiss, and
- $k$-uniformity and $L$-independence confirmed at lines 1341 and 1428–1430.

C1 is satisfied without qualification.

---

## C2 — Does withdrawal of §5.5.6 close Wave 1's polymer-to-spectral-lemma junction?

**PARTIAL PASS — one residual structural gap.**

The patch's strategy is correct in outline: §5.5.3 Step 3(i) already provides the polymer-aware HK bound, so inserting a weaker §5.5.6 was both redundant and harmful. The withdrawal eliminates the spurious margin condition $\kappa > 2\log(1+\zeta)$.

However, Wave 3's missed failure mode S4 — which the patch does not address — resurfaces here. Edit 4 (the revised "Application" paragraph, lines 1520–1527) asserts:

> $\delta E_k^{d=6}(0) = \sum_{X\ni 0} K_k^{d=6}(X,\cdot)$ is a
> convergent polymer expansion whose activities are $\mathcal{C}$-even
> dimension-6 operators with $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$
> (§5.6 Part III.3).

The cited §5.6 Part III.3 Lemma (preprint lines 1769–1773) states:

> **Lemma (Stability of Deviation Order).** *Let $\mathcal{O}$ be a
> local, gauge-invariant, $\mathcal{C}$-even operator on $\Lambda_{k+1}$
> of engineering dimension 6, analytic in $\{V_\ell\}$
> with radius $\rho > 0$ (from (B1)). Then $\mathrm{dev}(\mathcal{O}) \geq 2$.*

The lemma's hypothesis is "local, gauge-invariant" — a standard quantum field theory condition that applies to the **full operator** $\delta E_k^{d=6}(0)$, which is gauge-invariant by construction of the Balaban RG. But a **single polymer activity** $K_k^{d=6}(X, \cdot)$ for a fixed $X$ is spatially restricted to the support of $X$; it is in general NOT individually gauge-invariant (it gains gauge-invariance only when summed over all $X$, since the Balaban expansion is a local decomposition of the gauge-invariant effective action, not a sum of gauge-invariant pieces). There is no theorem in the preprint establishing that each individual $K_k^{d=6}(X, \cdot)$ satisfies the hypotheses of the Part III.3 Lemma.

The Hastings–Koma spectral bound at §5.5.3 Step 3(i) is invoked at the level of individual polymer activities $K(X)$: it needs a dev ≥ 2 property per activity to extract the $\hat\Delta^2$ factor inside the sum. If per-polymer dev ≥ 2 is not established, the bound yields only $|\langle 1|K_k^{d=6}(X,\cdot)|1\rangle_c| \leq C_p^* e^{-\kappa|X|}$ without the $\hat\Delta^2$ suppression. The polymer-level dev ≥ 2 claim is therefore load-bearing for C2, and it is asserted without proof.

**Verdict on C2:** The Hastings–Koma route closes the schematic polymer-to-spectral junction. The per-polymer dev ≥ 2 input needed to extract the $\hat\Delta^2$ suppression from that junction is not established. The wave 1 flaw is 90% closed; this joint remains open.

---

## C3 — Verbatim accuracy of eight "Conjecture 1" sweep edits (Edits 9–16)

**PASS — all eight spot-checked.**

| Edit | Location | Patch "from" | Preprint (verified) |
|---|---|---|---|
| 9 | §5 line 194 | "non-perturbative (Conjecture 1) is established in Section 5.6." | Matches verbatim (line 194 confirmed). |
| 10 | §5 line 323 | "**matrix element bound** (Conjecture 1 in Section 5.4):" | Matches verbatim (line 323 confirmed). |
| 11 | §5 line 358 | "This is Conjecture 1 (Section 5.4). It is:" | Matches verbatim (line 358 confirmed). |
| 12 | §5 line 380 | "**The proof continues via the matrix element bound** (Conjecture 1, Section 5.4)," | Matches verbatim (line 380 confirmed). |
| 13 | §5 line 1898 | "This is Conjecture 1 at $d_O = 6$." | Matches verbatim (line 1898 confirmed). |
| 14 | §5 line 2991 | "2. **Without Conjecture 1.** The operator norm bound gives…" | Matches verbatim (line 2991 confirmed). |
| 15 | App G line 6 | "Conjecture 1 (conjecture-1-closing.md): the claim that…" | Matches verbatim (G line 6 confirmed). |
| 16 | App G line 377 | "**Conjecture 1 at $d_O = 6$ stands, but the derivation of Mechanism 2 requires correction.**" | Matches verbatim (G line 377 confirmed). |

All eight "from" quotes are accurate against the preprint. The "to" replacements correctly insert "formerly Conjecture 1, now proved via §5.5.3 Step 3(i) + §5.6 Part III.3" or equivalent. The edit sweep is complete for the eight Wave 3–identified sites.

**Residual (self-suspicion P3, acknowledged by patch).** The patch notes that a grep across `research/`, `abstract.md`, and other non-`sections/` files was not performed. This is a lower-stakes concern (those files are not part of the formal proof chain), but a final sweep is recommended.

---

## C4 — Does the rigor-label argument hold without a KEY LEMMA downgrade?

**CONDITIONAL PASS, contingent on C2's open joint.**

The patch's rigor-label argument (patch §"Rigor label decision") is: §5.5.6 is deleted, so no new THEOREM/KEY LEMMA is introduced. The discharge of Conjecture 1 at $d_O = 6$ is a composition of two existing THEOREMs — §5.5.3 Step 3(i) and §5.6 Part III.3 — and is therefore itself at THEOREM rigor. The composition is not circular: §5.5.3 Step 3(i) provides the spectral bound; §5.6 Part III.3 provides dev ≥ 2. They are cited jointly, not circularly.

This argument is valid IF per-polymer dev ≥ 2 holds (the C2 gap). If the Part III.3 Lemma applies only to the total operator and not per activity, the composition fails: one is composing a theorem that needs "dev ≥ 2 per polymer" with a theorem that only proves "dev ≥ 2 for the total operator." The rigor label reverts from THEOREM to KEY LEMMA pending a per-polymer dev ≥ 2 argument.

The patch's own self-suspicion P2 (Hastings–Koma Lipschitz condition) is adequately mitigated by the observation that $\|E_k\|_\mathrm{op} \leq C g_k^4$ with $g_k \to 0$ makes the relevant norm monotonically smaller. That concern does not reopen.

---

## Summary

Three of Wave 3's four findings are closed:

- **Finding 1** (edit sweep): closed by Edits 9–16; all eight orphan locations patched with verbatim-accurate "from" quotes.
- **Finding 2** (margin condition): dissolved by route substitution; Hastings–Koma bypasses the $\kappa > 2\log(1+\zeta)$ arithmetic.
- **Finding 4** (rigor label): moot; §5.5.6 is deleted.

One finding remains structurally open:

- **Finding 3 residual / S4**: the per-polymer dev ≥ 2 assertion in Edit 4 (and carried through Edits 3, 6, 7) cites §5.6 Part III.3, whose Lemma is stated for total operators satisfying gauge-invariance, not for individual spatially-restricted polymer activities. This joint is asserted, not proved.

**Verdict: WEAKENED.** Architecture survives. To upgrade to SURVIVED: supply an argument that each Balaban polymer activity $K_k^{d=6}(X,\cdot)$ individually satisfies dev $\geq 2$ — either by showing each activity is gauge-invariant in the relevant sense, or by routing the $\hat\Delta^2$ suppression through a different decomposition (e.g., the full-operator bound applied first, then the HK bound for the spectral estimation).
