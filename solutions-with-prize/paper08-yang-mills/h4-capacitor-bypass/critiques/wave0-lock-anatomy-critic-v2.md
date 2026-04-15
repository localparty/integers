# Wave 0 LOCK-ANATOMY re-verification verdict

**Verdict: SURVIVED**

All four fixes applied cleanly. Wave 1 is CLEARED.

---

## Fix 1 findings — C2 repair quality (R.A.1 non-overlapping components)

**Prior gap:** The original entry carried the labels "Distributional + Wrong-space" for R.A.1 but only explained the Distributional failure; the Wrong-space component was not articulated separately, creating a risk that readers would conflate R.A.1's Wrong-space (function-space-level) with R.B.1's Wrong-space (category-level).

**Revised text (BLACKBOARD §K, lines 93-98):**

> *"R.A.1 failure row (Fix 1 per Wave 0 Critic: Distributional + Wrong-space stated as non-overlapping components):*
> - *Distributional component: $F^{\mathrm{pert}}(t)$ is a formal power series (divergent, expected from renormalons in 4D YM), not a convergent series. As a distribution-theoretic object it is not an analytic function in any neighborhood of $t=0$.*
> - *Wrong-space component (distinct from distributional): even treating $F^{\mathrm{pert}}$ charitably, the two-function pair $(F, F^{\mathrm{pert}})$ is not in the function space where the identity theorem applies. The identity theorem requires two analytic functions on a common connected open domain agreeing on a set with an accumulation point; $F$ may be analytic (if it exists as a limit of Schwinger functions), but $F^{\mathrm{pert}}$ lives in the space of formal power series, not analytic functions. Different function spaces — no shared domain to apply the theorem on."*

**(a) Both components stated explicitly?** YES. The revision sub-bullets the two components with explicit headers "Distributional component" and "Wrong-space component (distinct from distributional)." The revision also adds a reconciling sentence immediately after (BLACKBOARD §K, line 98):

> *"The two failure rows are non-overlapping: R.A.1's Wrong-space is function-space-level (formal series vs analytic function); R.B.1's Wrong-space is category-level (analytic-function Taylor coefficients vs entire-function zeros). Different pattern categories; different closure obstructions; same surface."*

**(b) Are the two Wrong-space components actually distinguished (non-conflated)?** YES — cleanly. The revised entry maps the distinction precisely:

- R.A.1 Wrong-space = the two-function *pair* is not in the function space where the identity theorem applies (formal power series vs analytic function; no shared domain). This is function-space-level.
- R.B.1 Wrong-space = CCM machinery targets zeros of an *entire function*, but YM target data would be Taylor coefficients of an analytic function — a category-level object-type mismatch at dictionary entries #12-17.

Cross-check against closure-digest §"The LOCK" (line 97): *"Different obstructions. Different pattern categories (Distributional + Wrong-space vs Wrong-space + External-source-inconsistency). Same attack-surface identification."* The runner's non-overlapping note reproduces this correctly. The distinction the prior Critic demanded is present and accurate.

**Fix 1: PASS — fully repaired, non-overlapping distinction explicit and accurate.**

---

## Fix 2 findings — C4 item 4 repair (ergodic structural risk)

**Prior gap:** The runner stated that UV extraction from the cluster-expansion construction could be done WITHOUT going through Taylor-coefficient identification, but gave no reasoning for why sub-step (b) — the UV extraction — avoids reintroducing this identification in disguise.

**Revised text (BLACKBOARD §K, lines 115-118):**

> *"Structural risk at sub-step (b) UV extraction: asymptotic-matching the constructed Schwinger function against $F^{\mathrm{pert}}(t)$ to extract UV behavior re-introduces Taylor-coefficient identification in disguise and lands back inside the LOCK. Conditions under which UV extraction avoids this: the UV singular structure must be computed intrinsically from the constructional quantities (polymer activities, Langevin stationary measure, transfer-matrix spectrum), producing $C_N$ directly as a construction-level quantity, NOT by matching to $F^{\mathrm{pert}}$. Hastings-Koma-style spectral-gap + polymer-decay arguments extracting the $|x|^{-8}$ scaling from the construction itself are outside the LOCK; asymptotic-match-to-perturbative-series arguments are inside the LOCK (hit K-5)."*

**(a) Is the structural risk named?** YES. The risk is named explicitly: *"asymptotic-matching the constructed Schwinger function against $F^{\mathrm{pert}}(t)$ to extract UV behavior re-introduces Taylor-coefficient identification in disguise and lands back inside the LOCK."*

**(b) Are the conditions under which the route stays outside the LOCK stated operationally?** YES — and the operationality is sufficient for Wave 1 Author use. The revised entry specifies:

- INSIDE the LOCK: UV extraction via asymptotic-match-to-perturbative-series → hits K-5.
- OUTSIDE the LOCK: UV singular structure computed intrinsically from constructional quantities (polymer activities, Langevin stationary measure, transfer-matrix spectrum), with $C_N$ produced directly as a construction-level quantity.
- Concrete example of the OUTSIDE route: Hastings-Koma-style spectral-gap + polymer-decay arguments extracting the $|x|^{-8}$ scaling from the construction itself.

A Wave 1 ERG↔QFT Author reading this can tell whether their approach falls inside or outside the LOCK: the criterion is operational (construction-level computation of $C_N$ vs perturbative-match computation). The prior Critic required exactly *"a Wave 1 Author can tell whether their approach is LOCK-adjacent or not"* — this criterion is met.

Additionally, the revised sub-step description (line 118) updates the three open sub-steps to reflect the fix:

> *"Route is NOT foreclosed but requires (a) continuum limit + (b) intrinsic UV extraction from constructional quantities (not by pert-matching) + (c) $C_N$ derivation as three open sub-steps."*

The parenthetical "(not by pert-matching)" is the operational gating condition — it directly guards against the ergodic route accidentally sliding into the LOCK at sub-step (b).

**Fix 2: PASS — structural risk named, conditions stated operationally with concrete examples and an explicit prohibition clause.**

---

## Fix 3 findings — C5 lateral Borel precision

**Prior gap:** The original entry said lateral Borel was "not tested by closing-H4 programme," which was imprecise because Delta-Critic DID test "Borel summability" as one of its 6 variants. The issue was conflation of standard $\mathbb{R}_+$ Borel (tested, failed) with lateral Borel in complex $t$ (structurally distinct, not tested).

**Revised text (BLACKBOARD §K, lines 110-113):**

> *"Standard Borel summability on $\mathbb{R}_+$ WAS tested by Delta-Critic (one of its 6 variants) and FAILED — IR renormalons produce Gevrey-1 non-Borel-summability along the real positive axis. This variant is LOCK-adjacent and re-entry is gated.*
> *Lateral Borel in complex $t$ (Écalle resurgence, away from $\mathbb{R}_+$) is structurally distinct and was NOT tested by the closing-H4 programme. Resurgent transseries can produce H4 from renormalon cancellation structure in lateral sectors without Taylor-coefficient identification via identity theorem on the real axis. The ambiguity along the IR-renormalon cut may be resolved by median summation + instanton/anti-instanton cancellation, producing a bona fide analytic continuation in a lateral sector where identity-theorem-free mechanisms (resurgent transseries matching) apply. CERN 2024 resurgence programme (arXiv:2511.15528) + Dunne 2024-2025 lectures are the live machinery for this variant.*
> *Conclusion: the LOCK binds standard $\mathbb{R}_+$ Borel (tested); it does NOT bind lateral Borel in complex directions (untested, structurally distinct mechanism via resurgence)."*

**(a) Is the distinction drawn?** YES. The revised entry explicitly splits into two headed sub-bullets, one for $\mathbb{R}_+$ and one for lateral, with separate verdicts for each.

**(b) Is it accurate? (Was Delta-Critic's test the $\mathbb{R}_+$ variant?)**

Cross-check against closure-digest §"The LOCK" (line 99):

> *"Delta-Critic tested 6 variant third-Route-A mechanisms via independent attempts: lattice-to-continuum direct match via Reisz, Borel summability, Hamburger moments, SVZ instanton-obstruction, gradient-flow spectral action, alternative NCG source. 5 of 6 hit existing failure rows."*

The closure-digest labels the tested variant simply as "Borel summability" without specifying the direction. The prior Critic's analysis (wave0-lock-anatomy-critic.md, lines 162-168) reasoned: the known obstruction in the programme context is IR renormalons on $\mathbb{R}_+$, and the failure row it hits is the R.A.1a honest-stall (*"comparable to Borel summability for 4D SU(N) YM (no known closure)"*, closure-digest line 22). That honest-stall is the standard $\mathbb{R}_+$ direction obstruction. The revised entry matches this reasoning exactly: *"IR renormalons produce Gevrey-1 non-Borel-summability along the real positive axis."*

The revised entry's attribution of the failure to Gevrey-1 non-Borel-summability on the real axis is consistent with the closure-digest's description of R.A.1a as *"comparable to Borel summability for 4D SU(N) YM (no known closure)"* — the Gevrey-1 obstruction is the standard renormalon barrier on $\mathbb{R}_+$. Attribution is accurate.

**(c) Does the revision correctly state that lateral Borel is NOT LOCK-bound?** YES — directly and with the correct logical reason:

> *"Conclusion: the LOCK binds standard $\mathbb{R}_+$ Borel (tested); it does NOT bind lateral Borel in complex directions (untested, structurally distinct mechanism via resurgence)."*

The revision also correctly adds mechanistic reasoning: resurgent transseries in lateral sectors produce H4 from renormalon cancellation without Taylor-coefficient identification via the identity theorem on the real axis. This accurately distinguishes the mechanism (lateral Borel produces the sum as a genuinely analytic function in a Stokes sector, without requiring a separate identity-theorem invocation on $F^{\mathrm{pert}}(t)$ as a formal series).

**Fix 3: PASS — distinction drawn, attribution accurate against closure-digest, lateral Borel correctly stated as NOT LOCK-bound with operative mechanism stated.**

---

## Fix 4 findings — C6 re-attempt list completeness

**Prior gap:** K-5 (ERG↔QFT naive shortcut) and K-3-extended (BC running $\alpha_{BC}(\beta)$) appeared in §F but not in §K LOCK-ANATOMY's re-attempt list. Wave 1 Authors are directed to read §K, not §F.

**Revised text (BLACKBOARD §K, lines 122-131):**

> *"LOCK-adjacent approaches in THIS run that must NOT be re-attempted (Fix 4 per Wave 0 Critic: expanded to mirror §F — Wave 1 Authors read §K, not §F):*
> *- Direct Route A variants ...*
> *- CCM port variants (K-1: 7 new Beta variants tested, all fail)*
> *- Spectral action variants (K-2: 4 new Beta variants tested, all fail)*
> *- BC running $\alpha_{BC}(\beta)$ mechanism from `paper12/research/53-transposition-asymptotic-freedom.md` (K-3-extended: structural not rigorous; doesn't address non-perturbative Schwinger function asymptotics)*
> *- Feehan-Maridakis energy-functional analyticity claim (K-4 trap ...)*
> *- Naive ERG→OPE reduction via asymptotic-match-to-pert-series (K-5 strengthened: shortcut-through-perturbative-matching + continuum-limit-elision — lands back in LOCK; Nissim is lattice-only anyway)*
> *- Hollands-Kopper perturbative OPE convergence claim (K-6 trap ...)*
> *- Citing arXiv:2506.00284 (K-7 — withdrawn crank paper ...)*
> *- Standard Borel summability on $\mathbb{R}_+$ for 4D YM (Delta-Critic variant, tested, failed on IR renormalons ...; lateral Borel in complex directions is OPEN and NOT in this list)"*

**(a) Are both K-5 and K-3-extended added?**

- **K-5 (ERG naive shortcut):** YES. The entry reads *"Naive ERG→OPE reduction via asymptotic-match-to-pert-series (K-5 strengthened: shortcut-through-perturbative-matching + continuum-limit-elision — lands back in LOCK; Nissim is lattice-only anyway)"*. K-5 is now present in §K with its strengthened pattern label.

- **K-3-extended (BC running $\alpha$):** YES. The entry reads *"BC running $\alpha_{BC}(\beta)$ mechanism from `paper12/research/53-transposition-asymptotic-freedom.md` (K-3-extended: structural not rigorous; doesn't address non-perturbative Schwinger function asymptotics)"*. K-3-extended is now present with file path and pattern.

**(b) Any others that should have been added but weren't?**

The prior Critic (wave0-lock-anatomy-critic.md, lines 191-196) mentioned a third category — imaginary-axis Borel / dimensional-continuation / large-N planar limit — but acknowledged these are "Route A variants (covered by the runner's 'Direct Route A variants' catch-all)" and noted explicit listing would reduce rediscovery risk. The prior Critic did NOT require these as a Fix 4 item; the Critic's text read *"an explicit note would reduce ... risk"* (advisory, not required). The prior Critic's Fix 4 instruction was: *"Add K-5 (ERG↔QFT naive shortcut) and K-3-extended (BC running α mechanism / research/53) explicitly."* Both have been added.

The runner has additionally added a ninth bullet — Standard Borel summability on $\mathbb{R}_+$ — which was not in the prior Critic's required list but is a correct and useful addition (it gates the $\mathbb{R}_+$ variant while explicitly carving out lateral Borel as OPEN). This addition is coherent with Fix 3 and is net-positive.

No required items from the prior Critic's Fix 4 are missing.

**Fix 4: PASS — both K-5 and K-3-extended added to §K LOCK-ANATOMY. An extra ninth bullet (standard Borel on $\mathbb{R}_+$) added appropriately beyond the minimum requirement.**

---

## Any new issues

Two observations below the threshold of blocking. Neither prevents Wave 1 dispatch.

**N-1 (NIT): K-3-extended file path precision.** The §K entry cites `paper12/research/53-transposition-asymptotic-freedom.md`. The §F entry (BLACKBOARD §F, line 63) and closure-digest §F kill for K-2 (line 65) both cite `paper12/research/53-transposition-asymptotic-freedom.md`. The paths are consistent. No issue.

**N-2 (ADVISORY): Lateral Borel LOCK-bypass risk not fully closed.** The revised Item 3 (Fix 3) correctly states lateral Borel is NOT LOCK-bound and names the operative mechanism (resurgent transseries in lateral sectors without identity-theorem invocation on the real axis). However, the prior Critic's Item 3 analysis (wave0-lock-anatomy-critic.md, lines 112-117) noted a subtle remaining open question: if lateral Borel produces F(t) as a genuine analytic function in a lateral sector, then Taylor-coefficient comparison *may* be available within that sector, meaning the approach is not entirely identity-theorem-free — the Borel sum IS the analytic continuation. The revised entry handles this by framing the mechanism as "resurgent transseries matching" rather than Taylor-coefficient identification, which is correct in its emphasis. However, the prior Critic had also flagged (line 113): *"The key distinction is whether the identity theorem is the closure mechanism. If lateral Borel produces F(t) as the Borel sum of a genuinely analytic function in a lateral sector, then in that sector F(t) IS analytic and the Taylor-coefficient comparison may work WITHOUT invoking the identity theorem as a standalone step."*

The revised entry does not explicitly address this remaining nuance — i.e., that lateral Borel operates outside the LOCK not because it avoids Taylor-coefficient comparison entirely, but because it avoids the identity theorem *as the operative closure step* (the Borel sum subsumes the analyticity). This nuance is correctly implied by the phrase *"without Taylor-coefficient identification via identity theorem on the real axis"* but could be sharper. This is an advisory note for the Wave 1 PROB↔SPEC Author, not a blocker. The prior Critic's Fix 3 instruction did not require this level of nuance explicitly — it required only that the $\mathbb{R}_+$ vs lateral distinction be stated accurately, which it now is.

**Neither N-1 nor N-2 blocks Wave 1 dispatch.**

---

## Summary

**Verdict: SURVIVED. Wave 1 is CLEARED.**

All four required fixes are applied cleanly. Fix 1 separates R.A.1's Distributional and Wrong-space components into explicit non-overlapping sub-bullets and adds a reconciling sentence distinguishing R.A.1's function-space-level Wrong-space from R.B.1's category-level Wrong-space. Fix 2 names the UV-extraction structural risk at sub-step (b) and states operational conditions (intrinsic constructional computation vs perturbative matching) that place a Wave 1 ERG Author inside or outside the LOCK. Fix 3 accurately splits standard $\mathbb{R}_+$ Borel (Delta-Critic tested, failed, LOCK-gated) from lateral Borel in complex $t$ (Écalle resurgence, not tested, NOT LOCK-bound), with correct mechanism attribution. Fix 4 adds both K-5 and K-3-extended to the §K re-attempt list with file path and pattern labels. One advisory note (lateral Borel Taylor-coefficient nuance) is below blocking threshold. H4 is still the wall. The anatomy entry now describes it correctly.
