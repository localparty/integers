# Wave 0 LOCK-ANATOMY Critic verdict

**Verdict: WEAKENED**

Wave 1 is BLOCKED. One C2 misassignment (pattern categories transposed for R.A.1), one C4 gap (ergodic route's NOT-bound reasoning is incomplete), and one C5 imprecision (lateral Borel edge case conflates Borel summability Delta-test with the lateral-direction question) require targeted fixes before dispatch.

---

## C1 findings — LOCK statement verbatim match

closure-digest.md §"The LOCK" (line 91) reads verbatim:

> *"Taylor-coefficient identification is the attack surface for H4 closure via analyticity/identity-theorem mechanisms, and it is genuinely stuck for any Route A-style closure."*

The runner's LOCK-ANATOMY entry quotes verbatim (BLACKBOARD §K, line 90):

> *"Taylor-coefficient identification is the attack surface for H4 closure via analyticity/identity-theorem mechanisms, and it is genuinely stuck for any Route A-style closure."*

**C1: PASS.** Verbatim match. No paraphrase drift.

---

## C2 findings — Load-bearing failure rows accuracy

closure-digest.md §"The LOCK" (lines 93-97) states:

> *"R.A.1 fails because $F^{\mathrm{pert}}(t)$ is a formal power series — the identity theorem's two-function hypothesis fails on the perturbative side (one of the two functions isn't actually analytic).*
> *R.B.1 fails because YM target data would be Taylor coefficients of an analytic function, but CCM 2025 machinery requires zeros of an entire function — Wrong-space category error at dictionary entries #12-17.*
> *Different obstructions. Different pattern categories (Distributional + Wrong-space vs Wrong-space + External-source-inconsistency). Same attack-surface identification."*

The runner states (BLACKBOARD §K, lines 93-94):

> *"R.A.1 failure row: ... Pattern: Distributional + Wrong-space."*
> *"R.B.1 failure row: ... Pattern: Wrong-space + External-source-inconsistency."*

**C2: WEAKENED — pattern categories transposed for R.A.1.**

The closure-digest assigns the pair as "(Distributional + Wrong-space) vs (Wrong-space + External-source-inconsistency)" meaning:

- R.A.1 = Distributional + Wrong-space
- R.B.1 = Wrong-space + External-source-inconsistency

The runner assigns R.A.1 = "Distributional + Wrong-space" — this is **correct** for R.A.1 in isolation.

However, the runner's *description* of the R.A.1 failure mechanism is imprecise in a load-bearing way. The runner says:

> *"$F^{\mathrm{pert}}(t)$ is a formal power series (divergent, expected from renormalons in 4D YM), not an analytic function."*

The closure-digest's own word for this pattern is "Distributional" — the formal-power-series character of $F^{\mathrm{pert}}(t)$ makes it distributional/formal, not analytic. But the runner's label "Wrong-space" for R.A.1 also appears in the runner's summary line: *"Distributional + Wrong-space."* The wrong-space label on R.A.1 is not supported by the closure-digest. The closure-digest reserves "Wrong-space" as one of R.A.1's pattern categories only in the pair reading. Cross-checking the §F kill entries:

- **K-1** (= R.B.1 in substance): pattern is "External-source-inconsistency + Wrong-space" (BLACKBOARD §F line 61).
- **K-2** (= R.C.1): pattern is "External-source-inconsistency + Vacuous" (BLACKBOARD §F line 62).

The closure-digest (line 97) assigns R.A.1's pattern as "Distributional + Wrong-space." The runner repeats this correctly. However, the runner's inline description conflates R.A.1 and R.B.1 in a subtle way: R.A.1's "Wrong-space" component means $F^{\mathrm{pert}}(t)$ does not live in the space of analytic functions (it's a formal series), whereas R.B.1's "Wrong-space" component means CCM's target space (zeros of an entire function) is wrong-category for YM's target (Taylor coefficients). The runner's R.A.1 description names only the Distributional failure and does not articulate the Wrong-space component separately. This is incomplete: R.A.1 carries *both* Distributional (formal series, not a distribution in the microlocal sense) *and* Wrong-space (not in the space of analytic functions where the identity theorem applies). The runner should articulate both components explicitly, not fold them.

**Fix required:** Expand R.A.1 description to state both pattern components explicitly: (a) Distributional — $F^{\mathrm{pert}}(t)$ is a formal power series, not an honest analytic function; (b) Wrong-space — this means the two-function pair for the identity theorem is not in the right function space. Keep the descriptions non-overlapping with R.B.1's Wrong-space component, which is a category-level mismatch (zeros vs Taylor coefficients), not a formal-series mismatch.

---

## C3 findings — Variants tested count

closure-digest.md (lines 65, 98-99) states:

> *"Beta-Critic tested 11 variant candidates for K-1 + K-2... [7 for K-1: K-1.5 Laplace-transform, K-1.6 Borel-transform, K-1.7 Hermite-moment, K-1.8 Mellin-gamma zeros, Yakaboylu 2024 port, CCM prolate-wave 2024, framework BC spectral triple CM 2008 θ-summable; 4 for K-2: twisted BC $H_{BC}-s\mathbb{1}$, crossed-product $D_{M^4}+\gamma\otimes\mathrm{sign}(H_{BC}-1/2)$, hybrid R.B.1×R.C.1 flow-time Dirac, framework BC spectral triple θ-summable]. All 11 fail."*
> *"Delta-Critic tested 6 variant third-Route-A mechanisms (lattice-to-continuum direct match via Reisz, Borel summability, Hamburger moments, SVZ instanton-obstruction, gradient-flow spectral action, alternative NCG source — 5 fail existing rows, 1 residual hypothetical)."*

The runner enumerates (BLACKBOARD §K, lines 97-98):

> *"Beta-Critic tested 11 variant candidates for K-1 + K-2 escape (K-1.5 Laplace-transform, K-1.6 Borel-transform, K-1.7 Hermite-moment, K-1.8 Mellin-gamma zeros, Yakaboylu 2024 port, CCM prolate-wave 2024, framework BC spectral triple CM 2008 θ-summable; twisted BC $H_{BC}-s\mathbb{1}$, crossed-product $D_{M^4}+\gamma\otimes\mathrm{sign}(H_{BC}-1/2)$, hybrid R.B.1×R.C.1 flow-time Dirac, framework BC spectral triple θ-summable) — all 11 fail"*
> *"Delta-Critic tested 6 variant third-Route-A mechanisms (lattice-to-continuum direct match via Reisz, Borel summability, Hamburger moments, SVZ instanton-obstruction, gradient-flow spectral action, alternative NCG source) — 5/6 hit existing failure rows; 1 residual hypothetical"*

**C3: PASS.** Counts and enumerated names match the closure-digest exactly. The K-1/K-2 split (7+4=11) is implicit in the runner's list (the first seven are K-1; the last four are K-2) and aligns with Beta-Critic's split. The Delta-Critic 6-variant enumeration matches verbatim. The "17+" label (11+6=17) is accurate.

Minor observation: the runner says "11 Beta + 6 Delta = 17, with 5/6 of Delta's hitting existing rows" — this is the correct reading of closure-digest line 99. The brief's §2.1 also states "17+ variant candidates" (line 50) so the label is calibrated correctly.

---

## C4 findings — "NOT-bound" enumeration per-item PASS/FAIL

The brief's §2.1 (lines 54-64) defines the three canonical NOT-bound categories: (1) lateral Borel in complex t, (2) wave-front set / microlocal, (3) axiomatic OPE construction. The closure-digest §"The LOCK" (lines 93-101) does not enumerate a closed NOT-bound list but is consistent with these three. The runner adds two additional categories (ergodic/cluster and cross-domain capacitor cells).

### Item 1: Microlocal / wave-front set restatement

Runner: *"category shift. H4 restated as a regularity claim about the Schwinger distribution $S_2^{\mathrm{ren}}(x,y)$ at $x=y$, not as Taylor-coefficient identification of a function. Different mathematical object. Hörmander propagation-of-singularities + algebraic-QFT microlocal machinery are not LOCK-bound."*

(a) Genuinely different from LOCK-bound surface? YES. The LOCK binds Taylor-coefficient identification via identity theorem on F(t). A wave-front-set regularity claim about the Schwinger distribution as a distributional object at coincident points does not involve F(t) as an analytic function; the identity theorem is not the closure mechanism.

(b) Reasoning holds? YES. The brief §2.1 line 58 confirms verbatim: *"the identity theorem's mechanism is not required"* for microlocal work; the category shift is to a "regularity claim about a distribution, not about a function."

(c) Did the closing-H4 programme actually test and close this? NO. The closure-digest does not show any microlocal/wave-front-set variant among Beta's 11 or Delta's 6. It remains open.

**Item 1: PASS.**

### Item 2: Axiomatic OPE convergence (non-perturbative)

Runner: *"H4 restated as a non-perturbative OPE convergence statement in an algebraic QFT framework. Different algebraic object. Hollands-Wald / BFR / Brunetti-Fredenhagen-Hollands-Wald axiomatic framework (IF extended to 4D gauge; currently scalar-only) is not LOCK-bound."*

(a) Genuinely different? YES. Non-perturbative OPE convergence in an algebraic QFT framework targets an operator-product-expansion as an algebraic-QFT statement, not as Taylor-coefficient identification of F(t). The identity theorem is not the operative tool.

(b) Reasoning holds? YES. Brief §2.1 line 60 confirms: "Another category shift — H4 restated as an operator-product-expansion convergence statement in an algebraic QFT framework, not as perturbative vs. non-perturbative Taylor-coefficient matching."

(c) Did the closing programme close this? NO. None of Beta's or Delta's tested variants target this. The closure-digest notes BFR (arXiv:2512.14227) as "scalar-only" in §B context, which is a calibration constraint on the approach's current reach, not a LOCK on it.

**Item 2: PASS.**

### Item 3: Lateral Borel in complex t

Runner: *"partially in the same category, but the identity-theorem mechanism is not required. Resurgent transseries can produce H4 from renormalon cancellation structure without Taylor-coefficient identification."*

The runner's "(partially in the same category)" hedge is accurate and important. See C5 below for full analysis.

(a) Genuinely different? PARTIALLY. Lateral Borel still works with F(t) and its Taylor series structure. The key distinction is whether the identity theorem is the closure mechanism. If lateral Borel produces F(t) as the Borel sum of a genuinely analytic function in a lateral sector, then in that sector F(t) IS analytic and the Taylor-coefficient comparison may work WITHOUT invoking the identity theorem as a standalone step (the Borel sum IS the analytic continuation). This is different in mechanism, but the "object" is still F(t).

(b) Reasoning holds? PARTIALLY — see C5.

(c) Did the closing programme close this? POSSIBLY PARTIALLY — see C5.

**Item 3: CONDITIONAL PASS — deferred to C5.**

### Item 4: Ergodic / cluster-expansion construction

Runner: *"category shift AT THE CONSTRUCTION LEVEL. If a non-perturbative Schwinger function exists via Langevin + cluster expansion... its UV singular structure can be analyzed directly from the construction WITHOUT going through Taylor-coefficient identification. K-5 strengthened warns about naive shortcuts; route is not foreclosed but requires (a) continuum limit + (b) UV extraction + (c) $C_N$ derivation as three open sub-steps."*

(a) Genuinely different? YES — IF the Schwinger function construction is non-perturbative AND the UV extraction proceeds directly from the construction without reintroducing F(t) Taylor-coefficient identification at any sub-step. The "IF" is load-bearing. The runner appropriately flags the three sub-steps as open.

(b) Reasoning holds? WEAKENED. The runner's reasoning does not address a specific risk: sub-step (b), UV extraction from the cluster-expansion construction, may require asymptotic matching that brings back exactly the $F^{\mathrm{pert}}(t)$ Taylor-coefficient comparison in disguise. The brief §2.1 does not explicitly flag this risk for the ergodic route. The runner should state why the UV extraction from a Balaban-style or Magnen-Rivasseau-Sénéor construction avoids the Taylor-coefficient identification step, not merely that it "can be analyzed directly." This is an incomplete NOT-bound justification for Item 4.

(c) Did the closing programme close this? NO. K-5 is a SHORTCUT kill (naive lattice-to-continuum direct match via Reisz), not a full-ergodic kill. The closing programme's Delta-Critic tested "lattice-to-continuum direct match via Reisz" as one of the 6 variants and it hit an existing failure row — but this is the Reisz-power-counting shortcut, not the full Langevin + cluster expansion + continuum-limit programme. The ergodic route via a genuine construction remains open.

**Item 4: WEAKENED — reasoning incomplete. Fix required: add explicit statement of why UV extraction in a construction-based approach avoids reintroducing the Taylor-coefficient identification step. Even a sentence noting the open risk is sufficient; the route is not pre-killed, but the NOT-bound justification must acknowledge this structural question.**

### Item 5: Cross-domain exploration via candidate cells

Runner: *"category shift by construction. LANG↔QFT (Kapustin-Witten S-duality), or other candidate cells from capacitor v1 §Candidates, may give an H4-equivalent statement on the dual side without ever touching Taylor coefficients."*

(a) Genuinely different? YES — by construction, if a cell provides an equivalent statement of H4 on the dual side, the Taylor-coefficient identification surface in the original YM frame is bypassed entirely. The LOCK binds the attack surface, not the target statement; the dual-side statement of H4-equivalent is a different mathematical object.

(b) Reasoning holds? YES. This is the capacitor-first bet; it does not attempt Taylor-coefficient identification of F(t) at all.

(c) Did the closing programme close this? NO. No cross-domain cell-exploration was attempted in the closing-H4 programme.

**Item 5: PASS.**

---

## C5 findings — Lateral Borel edge case

This is the tricky one. The runner writes (BLACKBOARD §K, line 106):

> *"Lateral Borel summation in complex $t$ — partially in the same category, but the identity-theorem mechanism is not required. Resurgent transseries can produce H4 from renormalon cancellation structure without Taylor-coefficient identification. CERN 2024 resurgence programme + Dunne 2024-2025 lectures are the live machinery; not tested by closing-H4 programme."*

The runner's claim "not tested by closing-H4 programme" requires scrutiny.

closure-digest.md §"The LOCK" (lines 98-99) states:

> *"Delta-Critic tested 6 variant third-Route-A mechanisms via independent attempts: lattice-to-continuum direct match via Reisz, Borel summability, Hamburger moments, SVZ instanton-obstruction, gradient-flow spectral action, alternative NCG source."*

"Borel summability" appears as one of Delta's 6 tested variants and it "hit existing failure rows" (closure-digest line 99: "5 of 6 hit existing failure rows").

**The runner's claim "not tested by closing-H4 programme" is therefore imprecise.** Borel summability WAS tested by Delta-Critic. The question is: was it tested for the $\mathbb{R}_+$ direction only (standard Borel sum), or for lateral directions in complex t specifically?

The closure-digest does not specify which direction of Borel summation Delta-Critic tested. Given the programme context — R.A.1a was already identified as "comparable to Borel summability for 4D SU(N) YM (no known closure)" at that stage, and the known obstruction is IR renormalons on $\mathbb{R}_+$ — it is most likely that Delta-Critic's "Borel summability" variant tested the standard $\mathbb{R}_+$ direction, which hits the known renormalon obstruction (an existing failure row). The lateral direction in complex t is a distinct question: lateral Borel asks whether F(t) can be reached by analytic continuation of a Borel-summed function in a sector away from $\mathbb{R}_+$. This is the Écalle resurgence framework, not the standard Borel sum.

However, the runner does not make this distinction explicit. The runner should state:

1. Delta-Critic's "Borel summability" variant tested Borel summation, likely in the $\mathbb{R}_+$ direction (the known-obstruction direction), and it hit an existing failure row.
2. Lateral Borel in complex t (away from the renormalon-generating real axis) is a structurally different question — it asks about analytic continuation in a sector, not summability on $\mathbb{R}_+$.
3. The identity-theorem mechanism is potentially available IF lateral Borel produces a genuine analytic function in that sector (because then F(t) IS analytic there and Taylor-coefficient comparison works within the sector without separate identity-theorem invocation).
4. Whether this constitutes a LOCK bypass or a new attack on the Taylor-coefficient surface in disguise depends on whether the lateral Borel sum avoids the renormalon obstruction structurally — this is the residual open question.

The runner's current phrasing ("not tested by closing-H4 programme") is **inaccurate** in the sense that the standard Borel summability direction was tested. The runner correctly identifies that the lateral direction may be different, but conflates this with "not tested at all."

**Fix required:** Revise to: "Delta-Critic tested 'Borel summability' as one of the 6 variants, most likely targeting the standard $\mathbb{R}_+$ direction (which hits the known IR renormalon obstruction, an existing failure row). Lateral Borel in complex t — the Écalle resurgence direction away from $\mathbb{R}_+$ — is structurally distinct: if it produces F(t) as a genuine analytic function in a lateral sector, the identity theorem is not the operative step (the Borel sum IS the analytic continuation). This direction was not tested by the closing-H4 programme's Delta-Critic, which is why it remains open."

---

## C6 findings — LOCK-adjacent re-attempt list completeness

The runner lists six categories to NOT re-attempt:
1. Direct Route A variants (Taylor-coefficient identification via identity theorem on F(t))
2. CCM port variants (K-1)
3. Spectral action variants (K-2)
4. Hollands-Kopper perturbative OPE (K-6 trap)
5. Feehan-Maridakis energy-functional analyticity (K-4 trap)
6. Citing arXiv:2506.00284 (K-7)

**Missing items from the LOCK-adjacent list:**

From the closure-digest, the following LOCK-adjacent variants were tested and failed, and are not explicitly flagged in the runner's list:

- **Imaginary-axis Borel / dimensional-continuation / large-N planar limit**: the R.A.1 Critic (closure-corrections.md line 73) tested "imaginary-axis, small-t large-separation, dimensional continuation from d<4, large-N planar limit" as extension candidates and ruled them out. These are Route A variants (covered by the runner's "Direct Route A variants" catch-all) but are worth making explicit to prevent a Wave 1 Author from rediscovering them as "novel."

- **ERG↔QFT naive shortcut (K-5 strengthened)**: the runner does flag K-5 as strengthened in BLACKBOARD §F (line 65) and §B context, but K-5 does not appear in the "must NOT be re-attempted" list in §K LOCK-ANATOMY. A Wave 1 ERG↔QFT Author needs to see K-5 in the re-attempt prohibition, not just in §F.

- **framework BC running α_BC(β) mechanism** (research/53 / K-3-extended): listed in BLACKBOARD §F (line 64) as a kill, but not in the §K LOCK-ANATOMY re-attempt list. The BLACKBOARD §F entry exists, but the LOCK-ANATOMY entry (which is what Wave 1 Authors are instructed to read per brief §3.0.5 step 4) does not carry it.

**C6: WEAKENED — minor but actionable.** Add K-5 (ERG↔QFT naive shortcut) and K-3-extended (BC running α mechanism / research/53) explicitly to the LOCK-adjacent re-attempt list. The Route A catch-all covers imaginary-axis variants implicitly, but an explicit note would reduce Wave 1 Author false-positive rediscovery risk.

---

## Summary

**Verdict: WEAKENED. Wave 1 is blocked until three fixes are applied.**

H4 is still the wall. The runner's LOCK-ANATOMY entry is directionally correct and its LOCK statement is verbatim. Three issues prevent Wave 1 dispatch:

**Fix 1 (C2 — required):** Expand R.A.1 description to articulate both pattern components separately: Distributional (formal-power-series character of $F^{\mathrm{pert}}(t)$) AND Wrong-space (the two-function pair is not in the function space where the identity theorem applies). These are non-overlapping with R.B.1's Wrong-space component (category mismatch: zeros vs Taylor coefficients). Current description names both labels but only explains the Distributional failure.

**Fix 2 (C4/Item 4 — required):** Expand Item 4 (ergodic/cluster-expansion) NOT-bound justification to acknowledge and address the specific risk: UV extraction from the cluster-expansion construction may reintroduce Taylor-coefficient identification in disguise at sub-step (b). The runner must state why (or under what conditions) a Balaban-style or Magnen-Rivasseau-Sénéor construction-based UV extraction avoids this. Route is not pre-killed; the justification must be complete.

**Fix 3 (C5 — required):** Revise the lateral Borel description to distinguish: (a) standard Borel summability on $\mathbb{R}_+$ WAS tested by Delta-Critic and hit an existing failure row; (b) lateral Borel in complex t (Écalle resurgence away from $\mathbb{R}_+$) is structurally distinct and was NOT tested. Current phrasing "not tested by closing-H4 programme" is inaccurate for (a).

**Fix 4 (C6 — minor, required before dispatch):** Add K-5 (ERG↔QFT naive shortcut) and K-3-extended (BC running α / research/53) to the LOCK-adjacent re-attempt list in §K LOCK-ANATOMY. These are already in §F but must be pinned in the entry Wave 1 Authors will read.

Once these four fixes are applied, re-dispatch this Critic for a verification pass. Fixes 1-3 are one-paragraph revisions; Fix 4 is two bullet additions. Total revision scope: ~15 lines. Re-dispatch should converge in one round.

*H4 is still the wall. The anatomy entry was close — not broken, but not tight enough to protect Wave 1 from drift. Fix the four gaps. Then the wall gets its correct description, and Wave 1 can hunt.*
