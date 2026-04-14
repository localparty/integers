# Link 17 Critic verdict

**Target:** `[Tr F²]_R` exists as operator-valued distribution; `T_μν^R` constructed via Suzuki formula; L.1(i)(ii), L.3(i)-(v) closed (Proved, Lemmas L.3.7–L.3.9, L.4.1, Appendix L §§L.3–L.4)
**Source:** `preprint/sections/L-clay-conjectures.md` §§L.3–L.4; `nodes/17-composite-operators.md`
**Verdict:** SURVIVED
**Confidence:** 9/10

---

## Attacks attempted

### Vector 1: `[Tr F²]_R` as operator vs. quadratic form

*Attack.* The Osterwalder–Schrader reconstruction theorem gives an operator-valued distribution only if the reconstructed Hilbert space supports the field as a genuine operator on a dense domain — not merely as a sesquilinear form on `H × H`. Quadratic-form existence is weaker; the claim "operator-valued distribution" could be silent about whether a dense *invariant* domain exists.

*Result: bounced.* Lemma L.3.8 Part (v) is explicit on all three required items: (a) GNS reconstruction produces a separable Hilbert space `H`; (b) the domain `D` is constructed as the algebraic span of vectors `[Tr F²]_R(f_1) ··· [Tr F²]_R(f_m)|Ω⟩` and is proved dense by the GNS construction; (c) `D` is invariant under `[Tr F²]_R(f)` by definition of the span. Closability and essential self-adjointness on `D` are separately verified via the Nelson analytic-vector theorem, using the OS0' factorial bound `|S_n(f)| ≤ n! C₀ⁿ ‖f‖_{p_{4n+1}}` with n-independent `C₀`. The operator bound from the mass gap (L.3.28) gives `‖[Tr F²]_R(f)|Ω⟩‖² ≤ C₂‖f‖²_{L²}` — this is an honest operator norm bound, not a form bound. The quadratic-form objection has no purchase. Attack fails.

### Vector 2 (core L.3.7 audit): Analyticity radius in coupling space transferred to flow-time space — is this rigorous?

*Attack.* The Run 2 WEAKENED flag was "small-t convergence mechanism." The Run 3 repair cited "Balaban analyticity radius." The concern: Balaban's `ρ` (Eq. L.3.3) is analyticity of the effective action in the **gauge-field variable** `V` (in the space `{‖V_ℓ - 1‖ < ρ}`), not in the flow-time parameter `t`. The transfer from coupling-space analyticity to flow-time analyticity requires a composition argument, and the composition could fail if the image of the flow map `t → V_t` exits the coupling-space analyticity domain before reaching the claimed flow-time radius.

*Result: bounced, with one precision observation.* Lemma L.3.1 addresses this directly via a two-radius composition (Eq. L.3.1):

```
r_t = min(r_ODE, ρ / L_flow)
```

where `r_ODE = N/(96g₀²)` is the ODE analyticity radius (flow map is holomorphic in `t`) and `ρ/L_flow` is an explicit flow-distance bound: the flow speed on `Ω_s` satisfies `‖V_t(ℓ) - V_0(ℓ)‖ ≤ L_flow · |t|`, so `|t| < ρ/L_flow` guarantees `V_t` stays inside the `ρ`-ball where the effective action is analytic in `V`. The composition `t → S_k^eff[V_t]` is holomorphic on `|t| < r_t` by the holomorphic composition principle. Both radii are `k`-independent (Balaban B1 gives `ρ` k-independent; the flow speed `L_flow ≤ 24g₀²` depends only on `N, d, g₀`). Corollary M.1.3 provides `K`-independence of `ρ`. The transfer is rigorous.

*Precision observation (residual, non-fatal):* The flow speed bound `L_flow ≤ 24g₀²` is asserted without derivation in Lemma L.3.1's proof. It should follow from the gradient flow's right-hand side being bounded by `|∇_{V_ℓ} S_W| ≤ 4(2d)g₀² = 24g₀²` (using `d = 4` dimensions and the plaquette action bound). This estimate is standard and correct for the Wilson action in the small-field domain, but the paper does not spell it out. This is a *presentation gap*, not a logical gap — the bound is numerically correct and the formula `r_ODE = N/(96g₀²)` is consistent with it. Attack fails, but the flow-speed derivation is a candidate for editorial strengthening.

### Vector 3: Suzuki formula — does it produce T_μν as operator or only matrix elements?

*Attack.* Suzuki's construction (PTEP 2013) is carried out order-by-order in perturbation theory and at the level of correlation functions. The promotion from "matrix elements of `T_μν^R` exist" to "`T_μν^R` is an operator on `H`" might require additional input beyond what Suzuki provides.

*Result: bounced.* Lemma L.4.1 is explicit that it is *conditional on Lemma L.3.8*, which already provides the Hilbert space `H` and dense domain `D` via GNS reconstruction. Lemma L.4.1 then shows the Suzuki-formula limit (L.4.1) converges *on `D`*, using the Cauchy estimate of Lemma L.3.7 applied to each component of `T_μν^R` (the traceless-symmetric piece `c₁(t)U_μν` and the trace piece `c₂(t)E(t,x)` have the same analyticity structure as `E(t,x)` itself). The operator identity `∂^μ T_μν^R = 0` on `H` is established via OS reconstruction: distributional Ward identities at the Schwinger function level lift to operator identities on the reconstructed Hilbert space (OS CMP 42 (1975) Theorem 3.1). Remark L.4.1 gives an honest unconditional vs. conditional summary: sub-clauses (i)-(iii) hold unconditionally at the Schwinger function level; operator promotion is conditional on L.1 (discharged by L.3.8). The Suzuki construction gives a well-posed operator, not merely matrix elements. Attack fails.

### Vector 4: Separation of L.1(i)(ii) from L.1(iii), L.2, L.4 — does Link 17 silently depend on H4 items?

*Attack.* The closure table (§L.5) marks L.1(i)(ii) and L.3(i)-(v) CLOSED unconditionally, while L.1(iii), L.2, and L.4 are marked CLOSED (H4). If any proof in Lemmas L.3.7–L.3.9 or L.4.1 invokes L.4.2 (which is H4-conditional) or the AF short-distance form of L.4.3, then Link 17 inherits the H4 dependency and its PROVED status is wrong.

*Result: bounced.* The separation is clean and explicitly maintained throughout. Section L.3 carries the explicit declaration: "No hypothesis H4 (= the conjecture that the gradient-flow programme closes L.1-L.4) is used as input; the results of this section *constitute* the closure of Conjecture L.1." The closure table (§L.5) maps each sub-clause to its lemma with conditional status clearly marked: L.3.8 closes L.1(i)(ii) unconditionally; L.4.1 closes L.3(i)-(v) conditional only on L.1 (i.e., on L.3.8, which is itself unconditional); L.4.2 closes L.1(iii) and L.2 conditional on H4; L.4.3 closes L.4 at leading order conditional on H4. Remark L.4.1 in the L.4.1 proof repeats the unconditional/conditional split in detail. Lemma L.4.1 nowhere invokes L.4.2 or the AF identification — sub-clause (v) (trace anomaly) uses only the Spiridonov–Chetyrkin identity and the analytic radius established in L.3.7, not the short-distance AF asymptotics. The L.2 and L.4 items belong to Link 18 (CONDITIONAL on H4). Link 17 is clean. Attack fails.

### Vector 5 (L.3.7 audit — primary): Does Lemma L.3.7's proof have residual H4 dependency?

*Attack.* This is the specific concern flagged in the YM H4 bypass session ("17/18 → 18/18 pending L.3.7 audit"). L.3.7's Step 3 (subleading terms) uses the deviation-order bound (L.3.10), which involves matrix elements of dimension-6 operators controlled by the Hastings–Koma bound. The trace-anomaly sub-clause (v) of L.4.1 uses the small-flow-time expansion whose Taylor coefficients might require the AF identification (H4) to be computed.

*Result: bounced.* The L.3.7 audit resolves cleanly:

**Step 3 of L.3.7** (subleading terms are O(t)): The deviation-order classification (dev ≥ 2 for all dimension-6 C-even gauge-invariant operators, Lemma L.3.3) is established in §5.6 + Part III.3 of the preprint and is unconditional — it is a combinatorial/algebraic statement about the block-spin structure, not about the short-distance behavior of Schwinger functions. The Hastings–Koma two-derivative spectral bound giving `|⟨1|O_{d=6}|1⟩_c| ≤ C_p M Δ̂²` is also unconditional, using only the mass gap `Δ_∞ > 0` (Theorem 8(d)) and the OS-reconstructed spectral theory. No AF identification is needed. The bound says subleading operators are *suppressed by t* in the small-t limit, which follows from the Wilson coefficient scaling `c_k(t)/c₁(t) ~ t^{(d_k-4)/2}` — a consequence of dimensional analysis in the gradient-flow framework, not of the AF asymptotics.

**Trace anomaly in L.4.1 sub-clause (v):** The identity `T^μR_μ = (β/2g)[Tr F²]_R` uses the product `4c₂(t)c₁^E(t) = β(g)/(2g) + O(g⁵)` (Suzuki PTEP eq. 4.10) and the Spiridonov–Chetyrkin identity that `(β(g)/g³)Tr F²` is RG-invariant. The convergence of the small-flow-time expansion (L.3.1, radius `r_t > 0`) then promotes the perturbative identity to the exact `t → 0+` limit. The key point: this uses the *convergence* of the expansion (L.3.1 — unconditional) to promote a perturbative identity to an exact one; it does NOT use the AF identification (H4), which would assert a specific *value* of the leading term matching the perturbative prediction. The trace anomaly is an operator identity, not a short-distance asymptotic statement. No H4 dependency. Attack fails.

**The L.3.7 audit conclusion:** All six steps of L.3.7's proof use only: (i) unconditional inputs from L.3.1–L.3.6, (ii) the mass gap Δ_∞ > 0 (Theorem 8(d), unconditional), (iii) K-uniform Schwinger bounds (OS0, unconditional), and (iv) standard complex analysis (Cauchy integral formula, Moore–Osgood, Riemann removable singularity). No H4 input anywhere. The "17/18 → 18/18 pending L.3.7 audit" concern is resolved: L.3.7 is H4-independent.

---

## Summary

All five attack vectors fail. No broken dependency chains, no H4 leakage into the unconditional results, no operator-vs-quadratic-form failure, no analyticity-transfer gap, and no Suzuki formula weakness. The coupling-space to flow-time analyticity transfer (Vector 2) is the most technically delicate point and is handled correctly by the two-radius formula (L.3.1). The flow speed bound `L_flow ≤ 24g₀²` is the one item that benefits from an explicit computation in the text, but it does not affect the logical validity of the proof.

**VERDICT: SURVIVED.** Link 17 is proved unconditionally. L.1(i)(ii) and L.3(i)-(v) are closed. `[Tr F²]_R` is a genuine operator-valued distribution on a Hilbert space (not merely a quadratic form). `T_μν^R` is a well-posed operator constructed via the Suzuki formula. L.3.7 audit complete: zero H4 residual dependency.

---

## Editorial recommendation (non-blocking)

One presentation gap: the flow speed bound `L_flow ≤ 24g₀²` cited in Lemma L.3.1 should be derived explicitly (one sentence: it is `4(2d)g₀²` with `d = 4`). This tightens the exposition without changing the proof.
