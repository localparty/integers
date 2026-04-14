# DUAL-CHECK — Lehmer L5A STRUCTURAL → PARTIAL

*Pin-Check agent dispatch. T7 S-duality phase, cycle 2, 2026-04-14.*
*Authoritative PIN-TABLE: `paper12/research/23-framework-predictions-master-table.md`.*
*Chessboard protocol: `millenium-apps/proof-chain-adversarial-01/13-chessboard-layer.md` §1.*

---

## Summary

L5A's STRUCTURAL → PARTIAL upgrade produces an explicit lower bound $c_0 \geq 0.052$ (fixed-point) / $c_0 \geq 0.041$ (degree-tied at $d=10$) via ITPFI regularization of the PIN-PRESERVATION contamination sum. PINS-PRESERVED: $c_0$ is a bound on an algebraic-number property, not a predicted physical observable, and the derivation uses the 36 pins as fixed inputs — it does not re-emit them as shifted outputs.

---

## Action: Lehmer L5A — $c_0 \geq 0.0525$ (or 0.0410) derived

**Status change**: Route A PIN-PRESERVATION forcing: STRUCTURAL → PARTIAL.

New result: Mertens' third theorem applied to the ITPFI contamination amplitude $C(N_\text{cyc};\epsilon) \sim \epsilon \cdot e^{-\gamma}/\log N_\text{cyc}$, combined with the empirical PIN-PRESERVATION constraint $\epsilon_\text{pin} \sim 10^{-2}$, yields the fixed-point bound $\epsilon \geq 10^{-2} \cdot \log(1/\epsilon) \cdot e^\gamma$ (solution: $c_0 \geq 0.052$) and the degree-tied bound $c_0 \geq 10^{-2} \cdot \log 10 \cdot e^\gamma \approx 0.041$. Both are $4$–$5\times$ improvements over the weak empirical $10^{-2}$. Gap to Lehmer target $0.176$: factor $\sim 3$, absorbed into the unmodeled sensitivity coefficient $A_\text{max}$ and the density sub-wall (Failure 3 of the construct).

### Affected quantities

| Quantity | Domain | Notes |
|---|---|---|
| $c_0 \geq 0.041$–$0.052$ | Algebraic number theory | ITPFI-sharpened lower bound on the Mahler measure gap |
| BC KMS$_1$ spectral gap | $W^*$-algebra / programme-internal | Structural characterization of cyclotomic isolation now has a numerical floor |
| Lehmer L5 Route A status | Programme-internal | STRUCTURAL → PARTIAL |
| Lehmer chain confidence | Programme-internal | 4/10 → 5/10 |

**Not affected**: any $\gamma_n$ value; any operator dictionary entry; any of the 36 predictions.

### PIN-TABLE scan

The 36 predictions in `paper12/research/23-framework-predictions-master-table.md` (Sectors A–E) are:

- **All spectral formulas** in $\gamma_1, \ldots, \gamma_{15}$. The $c_0$ bound governs the MINIMUM MAHLER MEASURE of non-cyclotomic algebraic numbers — this is a statement about elements of $\overline{\mathbb{Q}}$, not about individual Riemann zeros. The numerical values $\gamma_1, \ldots, \gamma_{15}$ are fixed by CCM/Boegli to $10^{-55}$ precision independently of any Mahler-measure bound.
- **Sector A** (10 cosmological fits: $H_0$, $\Omega_b$, $\Omega_\Lambda$, $n_s$, $N_\text{eff}$, ...): all in $\gamma_n$, $\pi$, $\zeta(2)$, $\zeta(3)$, $\gamma_E$. No Mahler measure content.
- **Sector B** (3 gauge coupling fits: $\alpha^{-1}$, $\alpha_s$, $\sin^2\theta_W$): formulas in $\gamma_1, \gamma_4, \gamma_6, \gamma_{11}$. No $c_0$ content.
- **Sector C** (15 mass fits): formulas in $\gamma_3, \gamma_7, \ldots, \gamma_{15}$. No Mahler content.
- **Sector D** (7 mixing angles): formulas in $\gamma_1, \gamma_5, \gamma_6, \gamma_9, \gamma_{10}, \gamma_{12}, \gamma_{13}$. No $c_0$ content.
- **Sector E** (3 derived cosmic observables: CC formula, $m_W$, $n_s$ ratio): the CC formula involves $e^{\gamma_1\pi^2/2}$; no Lehmer content. The $e^{-\gamma_E}$ appearing in Mertens is $e^{-\gamma_E} \approx 0.5615$, distinct from the raw $\gamma_E \approx 0.5772$ used in the $m_Z$ formula — same clarification as the L4 Route B dual-check, no cross-contamination.

**PIN-TABLE hits: ZERO.** $c_0$ does not appear in any of the 36 prediction formulas. It is a property of the Mahler-measure spectrum — a mathematical output of the programme, not a predicted physical observable.

### Circularity check

**The derivation uses the 36 pins as INPUTS.** The PIN-PRESERVATION step (L5A construct §5) writes:

> "PIN-PRESERVATION requires $|\delta\pi| \leq \epsilon_\text{pin}$ for every pin. Combining with Step 4: $C_A \cdot \epsilon \cdot e^{-\gamma}/\log N_\text{cyc} \leq \epsilon_\text{pin}$."

The 36 pins ($\epsilon_\text{pin}(\pi)$ for each $\pi$) enter as FIXED CONSTRAINTS derived from the experimental master table — they are inputs to the forcing inequality. The output $c_0 \geq f(\epsilon_\text{pin})$ is a function of those inputs. This is the standard structure of a conditional lower bound:

```
INPUT:  pins hold at sub-percent (experimental fact, 36 equations)
STEP:   contamination bound via ITPFI Mertens regularization
OUTPUT: c_0 ≥ 0.041–0.052 (lower bound on Mahler gap)
```

The $c_0$ bound is DERIVED from the pins, not IMPOSED on them. The derivation does not re-emit the pins as shifted — it uses them as a constraint and produces a number-theoretic consequence. No pin is perturbed by the derivation's output.

**No circular dependency that shifts pins.** The only circularity is benign: the derivation cites the pin precisions (which are experimental facts) to bound the admissible contamination amplitude, and concludes that $c_0$ must exceed a floor. This is the same structure as any forced conditional in the programme. The 36 pins are unmodified both before and after the derivation.

Note on the named sub-wall (Failure 3 of the construct): the backward-verification in §Self-suspicion identified that the per-$\alpha$ contamination argument requires a density model to convert to a rigorous lower bound. This is an INTERNAL limitation of the derivation's completeness — it does not create a new coupling between $c_0$ and the pins. The sub-wall is the reason the status is PARTIAL rather than DERIVED.

### Verdict

**PINS-PRESERVED.**

$c_0$ is a bound on algebraic-number proximity to the cyclotomic vacuum. It is arithmetic, not a predicted observable. The derivation holds the 36 pins fixed and derives $c_0$ conditional on them — no pin shifts.

---

## Overall verdict

**PINS-PRESERVED** (expected).

The L5A STRUCTURAL → PARTIAL upgrade is accepted. The chessboard does not flex.

---

## Notes for the runner

- **RIGIDITY contribution**: L5A is now PARTIAL. PARTIAL does NOT map to VERIFIED in the brief 30 §0.2 status dictionary, so $L_\text{verified}$ increment = 0. If the runner disciplines fractional counts, +0.5 is defensible, but the standard convention is 0 for non-VERIFIED.

- **Confidence increment**: Lehmer 4/10 → 5/10 is a vertex-level confidence increment, captured in the next SYMMETRY recomputation (not in the RIGIDITY formula, which counts only VERIFIED links).

- **Pair-3 gap update**: per the L5A construct summary, both faces of Pair 3 (Cramér Route B + Lehmer Route A) are now PARTIAL. Pair-3 remaining gap: 2.0 → 1.0 (both faces PARTIAL). This is the construct's internal accounting — no chessboard action required.

- **Named sub-walls** (from construct §Self-suspicion): (1) $A_\text{max}$ not yet rigorously computed across 36 pins; (2) conductor identification $N_\text{cyc}$ is heuristic; (3) density model for the integrated contamination argument missing. All three are sub-walls for L5A to close from PARTIAL to DERIVED. None of the sub-walls involve pin perturbation.

- **L5A vs L5B coupling**: L5B (CM-curve Mahler gap via Deninger-RV + BSD) is independently PARTIAL and does not depend on L5A's bound. The two routes are additive evidence; their DUAL-CHECKs are independent.

- **Cross-reference**: the L4 Route B dual-check (`dual-check-cramer-L3-L4.md`) note 4 flagged the Lehmer Transfer Author as ready for dispatch. This dual-check confirms the transfer was clean: no pin shift.

---

*Pin-Check agent, T7 S-duality phase, cycle 2, 2026-04-14.*
*PINS-PRESERVED. $c_0 \geq 0.041$–$0.052$ is arithmetic (Mahler gap bound), not a predicted observable. No recomputation.*
