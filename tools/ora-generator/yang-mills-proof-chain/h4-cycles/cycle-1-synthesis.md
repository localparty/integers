# H4 Cycle 1 Synthesis: Cross-Route Combination

*ORA Synthesis agent. Date: 2026-04-13.*
*Input: 6 excision-run outputs + capacitor v1 + blackboard Routes A-D.*
*Mode: Cross-route combination analysis.*

---

## Preamble: the structural situation

Seven routes have been attempted across two runs. All are BLOCKED individually. The excision verdict (LOCK 11/10) identifies a common wall: the divergence of perturbation theory in g^2 within the k=0 topological sector.

But partial results exist that were never combined:

| Partial result | Source route | Status | What it controls |
|---|---|---|---|
| Instanton sectors |k| >= 1 are O(|x|^{11N/6}) | Route 3 | PROVED | All topological sectors except k=0 |
| Borel plane mapped: IR renormalon at u=2 | Route 2 | MAPPED (not resolved) | Structure of perturbative divergence |
| Gradient-flow analyticity: F(t) analytic in |t| < r_t | Route 1 | PROVED (Lemma L.3.7 Step 2) | Non-perturbative side in flow-time variable |
| Balaban disk analyticity: |g^2| < kappa, k-independent | Steps 2-4 | PROVED (B1) | Coupling-plane analyticity at each RG scale |
| AF unconditional: g_k -> 0 | Steps 12-14 | PROVED | Running coupling at each scale |
| [Tr F^2]_R constructed as operator-valued distribution | Step 17 | PROVED | The condensate operator exists non-perturbatively |

The question: does COMBINING these close H4, even though no single route does?

---

## Synthesis Question 1: Route 3 + Route 1

**Can instanton sub-leading (Route 3) + flow-time analyticity (Route 1) give better k=0 sector analyticity?**

### The argument

1. Decompose the functional integral by topological sector:
$$F(t) = \sum_{k \in \mathbb{Z}} w_k \cdot F_k(t)$$
where w_k is the normalized weight of the k-instanton sector and F_k(t) is the correlator restricted to that sector.

2. Route 3 PROVED: the |k| >= 1 contributions satisfy
$$\left|\sum_{|k| \geq 1} w_k F_k(t)\right| = O(|x|^{11N/6})$$
at short distances. This is faster than any perturbative correction.

3. Therefore:
$$F(t) = w_0 F_0(t) + O(|x|^{11N/6})$$
The full correlator equals its k=0 restriction up to exponentially sub-leading corrections.

4. Route 1 established: F(t) is analytic in t on |t| < r_t. Since F(t) = w_0 F_0(t) + (exponentially small), and the exponentially small piece is smooth (it comes from sectors with bounded action), we get:
$$F_0(t) \text{ is analytic in } t \text{ on } |t| < r_t$$
The k=0 sector correlator inherits flow-time analyticity.

5. **The proposed gain**: Within the k=0 sector, there are no instantons by definition. The non-perturbative effects are: (a) large quantum fluctuations within the Balaban small-field region, (b) condensate contributions, (c) IR renormalon-type corrections. ALL of these are sub-instanton-scale effects.

### What works

- The topological decomposition is rigorous (the path integral on a compact manifold decomposes by second Chern number).
- The instanton bound is PROVED (Route 3, Section 3.4).
- The analyticity inheritance is sound (difference of analytic and exponentially suppressed is analytic).
- This isolates the problem to the k=0 sector with PROOF that nothing else matters.

### What is missing

- **The k=0 sector IS the hard part.** Isolating to k=0 does not simplify the Borel summability problem. The IR renormalons, the condensate contributions, the non-perturbative quantum fluctuations -- all of these live in k=0. The combination of Routes 1 and 3 confirms that the problem is ENTIRELY within k=0, which was already suspected, but does not crack k=0 itself.

- **The analyticity in t does not help with analyticity in g^2.** F_0(t) is analytic in t. But the perturbative expansion of F_0(t) in g^2 is still a formal power series with factorial growth. The t-analyticity and g^2-divergence address different variables (Card 16 from the capacitor patch).

- **One subtle gain that IS real**: The topological decomposition + Route 3 bound means that any "non-perturbative correction" to F(t) that comes from |k| >= 1 sectors is PROVED sub-leading. So if we could show that the k=0 sector's perturbative expansion captures F_0(t) up to corrections that are also sub-leading at short distances, H4 would follow. This reduces H4 from "all non-perturbative effects are sub-leading" to "k=0 non-perturbative effects are sub-leading" -- a genuine reduction, but the reduced problem is still the hard one.

### Closure probability from this combination

**0.05** (marginal improvement over either route alone). The combination provides a clean reduction to k=0 but does not crack k=0.

---

## Synthesis Question 2: Balaban disk analyticity + AF

**At scale k where g_k << kappa, does the Cauchy estimate give perturbative agreement within the Balaban construction?**

### The argument

This is the most promising combination. The logic is:

1. **Balaban (B1)**: At each RG scale k, the effective action S_k^eff[V] and hence the correlator F_k(g_k^2) (at scale k) is analytic in g_k^2 on the disk |g_k^2| < kappa, where kappa is k-INDEPENDENT (this is the load-bearing property from Step 4*).

2. **AF (Steps 12-14)**: g_k -> 0 as k -> infinity. More precisely, g_k^2 ~ 1/(2 b_0 k) for large k (the doubly-exponential convergence in the actual RG, but schematically 1/k in the logarithmic running).

3. **Cauchy estimate**: For any function f analytic on |z| < kappa with |f(z)| <= M on the disk, the Taylor coefficients satisfy:
$$|a_n| = \left|\frac{f^{(n)}(0)}{n!}\right| \leq \frac{M}{\kappa^n}$$

4. **Applied to the polymer activity**: Each polymer activity K_k(X, V; g_k^2) is analytic in g_k^2 on |g_k^2| < kappa with bound |K_k| <= e^{-kappa_spatial |X|} (from polymer convergence, Step 3). Its perturbative expansion is:
$$K_k(X, V; g_k^2) = \sum_{n=0}^{N-1} K_k^{(n)}(X, V) (g_k^2)^n + R_N(X, V; g_k^2)$$

5. **Cauchy on the remainder**:
$$|R_N(X, V; g_k^2)| \leq \frac{M_k}{\kappa^N} |g_k^2|^N \cdot \frac{\kappa}{\kappa - |g_k^2|}$$

At scale k, with g_k^2 << kappa:
$$|R_N| \leq C \cdot e^{-\kappa_{\text{spatial}} |X|} \cdot \left(\frac{g_k^2}{\kappa}\right)^N$$

6. **For any fixed N**, as k -> infinity (g_k -> 0), the remainder R_N -> 0 as (g_k^2/kappa)^N. This means: **at high RG scales, the perturbative expansion to ANY fixed order N is a valid approximation of the full non-perturbative polymer activity, with error controlled by (g_k/kappa)^N.**

7. **Sum over scales**: The correlator F is assembled from all scales. The deep-UV scales (large k) are controlled by the Cauchy estimate. The IR scales (small k) have g_k ~ O(1), and the Cauchy estimate is not useful there.

### What works

- **This argument is RIGOROUS at each fixed RG scale k for large k.** The Balaban analyticity (B1) and the k-independence of kappa are PROVED. The Cauchy estimate is standard complex analysis. The conclusion -- that the perturbative expansion approximates the non-perturbative effective action at high scales -- is a THEOREM within the existing framework.

- **This is exactly how asymptotic freedom is supposed to work**: at high energies (large k), the coupling is small, and perturbation theory is a good approximation. The Balaban construction makes this intuition rigorous at each scale.

- **The k-independence of kappa is load-bearing**: without it, the disk could shrink as k increases, potentially keeping g_k/kappa bounded away from zero. The k-independence ensures g_k/kappa -> 0.

### What is missing

- **The IR scales are NOT controlled.** At small k (IR), g_k is not small compared to kappa. The Cauchy remainder is O(1) at these scales. The full correlator includes contributions from ALL scales, including the IR where perturbation theory breaks down.

- **Assembling across scales requires a TELESCOPING argument.** The RG structure provides:
$$F = \text{(UV contribution from scales } k > k_*\text{)} + \text{(IR contribution from scales } k \leq k_*\text{)}$$
The UV piece is controlled by the Cauchy estimate. The IR piece is the gluon condensate + confinement physics -- exactly the non-perturbative content.

- **The OPE structure saves us PARTIALLY.** In the OPE for the short-distance correlator:
$$\langle \text{Tr } F^2(x) \text{Tr } F^2(0) \rangle = C^{\mathbb{1}}(x) + C^{F^2}(x) \langle \text{Tr } F^2 \rangle + \cdots$$
The identity-channel coefficient C^1(x) is purely perturbative (UV). The condensate term C^{F^2}(x) <Tr F^2> is power-suppressed: C^{F^2}(x) ~ |x|^4 at short distances, while C^1 ~ |x|^{-8}. So the IR contributions are SUB-LEADING in the OPE.

- **BUT**: Proving that the OPE converges (or at least that the leading term is correct) IS H4. The Cauchy estimate tells us that at each UV scale the perturbative expansion is good, but assembling this into a statement about the full correlator's short-distance behavior requires the OPE, which is what we are trying to prove.

### The key insight: what WOULD close it

If we could show that the correlator's short-distance behavior is DOMINATED by UV scales (large k), then the Cauchy estimate would control the dominant contribution, and the IR contribution would be a sub-leading correction. This is precisely the OPE statement -- the leading OPE term C^1(x) comes from UV scales.

**Proposed specific computation**: Define a SCALE-SPLIT correlator:
$$F(t) = F_{>k_*}(t) + F_{\leq k_*}(t)$$
where F_{>k_*} includes only RG scales above k_*, and F_{<=k_*} includes the rest. Choose k_* such that g_{k_*}^2 = epsilon << kappa. Then:

- F_{>k_*} is controlled by the Cauchy estimate to N-th order with remainder O(epsilon/kappa)^N.
- F_{<=k_*} must be shown to be sub-leading at short distances.

**The missing lemma**: F_{<=k_*}(t) contributes O(|x|^{d_*}) to the short-distance correlator with d_* > 0 (power suppression from the OPE). This is a statement about the IR contribution to the UV-dominated correlator. It is plausible and consistent with the OPE, but proving it within the Balaban framework requires showing that the polymer expansion at low scales (k <= k_*) produces only sub-leading short-distance contributions.

### Closure probability from this combination

**0.25** -- this is the most promising direction. The argument is 70% complete. The missing piece (IR contribution is sub-leading) is a specific, well-defined mathematical question within the Balaban framework. It does NOT require global Borel summability -- only a scale-by-scale Cauchy estimate + IR power suppression.

---

## Synthesis Question 3: Route 2 Borel map + Route 3 instanton bound + Step 17 operator construction

**Does having [Tr F^2]_R under non-perturbative control change the renormalon story?**

### The argument

1. **Route 2 mapped the Borel plane**: The IR renormalon at u=2 corresponds to a dimension-4 condensate <g^2 Tr F^2>. The Borel ambiguity is:
$$\delta F_{\text{renormalon}} \sim e^{-2/(b_0 g^2)} \sim \Lambda^4 |x|^4$$
This is a power correction of dimension 4.

2. **Step 17 PROVED**: [Tr F^2]_R exists as an operator-valued distribution in the non-perturbative theory. This means <Tr F^2> is a well-defined (finite) number in the constructed theory.

3. **Route 3 PROVED**: The instanton contributions to <Tr F^2> itself are O(|x|^{11N/6}), so the condensate is dominated by k=0 sector physics.

4. **The proposed connection**: The renormalon ambiguity at u=2 is "resolved" in the full theory by the gluon condensate <Tr F^2>. The standard physics argument (SVZ 1979, David 1984, Mueller 1985) is:

$$F^{\text{non-pert}}(x) = F^{\text{pert, resummed}}(x) + C^{F^2}(x) \cdot \langle \text{Tr } F^2 \rangle + \cdots$$

The Borel ambiguity in F^pert cancels against the condensate contribution, leaving the full answer unambiguous. This is the standard renormalon-OPE correspondence.

5. **Having [Tr F^2]_R constructed non-perturbatively means**: the condensate <Tr F^2> is a DEFINITE NUMBER, not an ambiguous quantity. The non-perturbative construction RESOLVES the Borel ambiguity by selecting a specific value of <Tr F^2>.

### What works

- **The non-perturbative construction of [Tr F^2]_R is a genuine structural advantage.** In the standard QFT discussion, the renormalon ambiguity and the condensate are BOTH poorly defined -- the ambiguity is delta ~ Lambda^4, the condensate is <Tr F^2> ~ Lambda^4, and the claim is they cancel. In the Balaban + gradient-flow construction, the condensate IS defined (Step 17), so the cancellation has a definite target.

- **The renormalon-OPE correspondence is well-established in physics.** The u=2 IR renormalon's ambiguity is O(Lambda^4), matching the dimension-4 condensate. This is not an accident -- it reflects the OPE structure.

- **The instanton bound (Route 3) ensures the condensate is dominated by k=0 physics**, so we are not mixing in topological sector confusion.

### What is missing

- **The renormalon-OPE correspondence is a PHYSICS argument, not a THEOREM.** Proving that the Borel ambiguity at u=2 is exactly cancelled by the condensate contribution requires:
  (a) A precise definition of the Borel-resummed perturbative series (which prescription? principal value? lateral?).
  (b) A proof that the non-perturbative answer minus the Borel-resummed series equals exactly the condensate contribution.
  Neither (a) nor (b) is available rigorously for 4D YM.

- **The direction of the argument is backwards for closing H4.** H4 says: the non-perturbative answer AGREES with perturbation theory at short distances. The renormalon-OPE correspondence says: the non-perturbative answer DIFFERS from perturbation theory by the condensate, but this difference is power-suppressed (O(|x|^4) vs the leading |x|^{-8}). If we could make the correspondence rigorous, it would give:
$$F(x) = F^{\text{pert}}(x) \cdot \left[1 + O(|x|^{12})\right]$$
which IS a version of H4 (non-perturbative = perturbative at leading order in the short-distance expansion).

- **The critical gap**: making the renormalon cancellation rigorous requires the same Borel summability control that Route 2 identified as the wall. Having [Tr F^2]_R constructed non-perturbatively gives us ONE side of the cancellation (the condensate), but we still need the OTHER side (the precise Borel ambiguity) to match.

### A sharper formulation

**What would make this work**: If we could show that
$$F_{\text{non-pert}}(x) - F_{\text{non-pert, no condensate}}(x) = C^{F^2}(x) \langle \text{Tr } F^2 \rangle$$
where "no condensate" means the perturbative expansion with the renormalon ambiguity resolved by principal value, then the renormalon cancellation would follow from the construction.

**But "F_non-pert, no condensate" is not a well-defined object** -- it presupposes a separation of perturbative and non-perturbative that is exactly what H4 asks about.

### Closure probability from this combination

**0.10** -- the non-perturbative construction of [Tr F^2]_R is a genuine structural advance, but converting it into a rigorous renormalon cancellation requires controlling the Borel sum, which is the Route 2 wall.

---

## Overall Assessment

### Cross-route combination viability

| Combination | What it achieves | Closure probability |
|---|---|---|
| Route 3 + Route 1 (instanton + analyticity) | Clean reduction to k=0 sector | 0.05 |
| Balaban (B1) + AF (Cauchy estimate) | **Scale-by-scale perturbative agreement in UV + identified missing lemma** | **0.25** |
| Route 2 + Route 3 + Step 17 (Borel + instanton + operator) | Non-perturbative condensate construction, renormalon-OPE direction | 0.10 |
| All three combined | Cumulative structural picture | see below |

### The cumulative picture

Combining ALL partial results produces the following structural argument for H4:

1. **Topological reduction (Route 3)**: Only the k=0 sector matters. All |k| >= 1 contributions are O(|x|^{11N/6}). PROVED.

2. **UV control (B1 + AF via Cauchy)**: Within the k=0 sector, at high RG scales (large k), the non-perturbative polymer activities agree with their perturbative expansions to any order N, with remainder O((g_k/kappa)^N). PROVED at each scale.

3. **IR sub-dominance (needed, not proved)**: The IR contributions (low RG scales) to the short-distance correlator are power-suppressed, entering the OPE as dimension >= 4 condensate corrections ~ O(|x|^4) relative to the leading |x|^{-8}. CONJECTURED (standard OPE/renormalon physics, but not proved).

4. **Condensate under control (Step 17)**: The leading condensate <Tr F^2> exists as a non-perturbative number. The renormalon ambiguity at u=2 corresponds to this condensate. PROVED (existence), CONJECTURED (renormalon correspondence).

**Items 1 and 2 are proved. Items 3 and 4 are the remaining gap.** The gap is NOT the full Borel summability problem -- it is the more specific question of whether IR contributions are power-suppressed at short distances within the Balaban framework.

### Does cross-route combination produce a viable path?

**YES, conditionally.** The combination narrows the gap from "global Borel summability of 4D YM" (a major open problem with no precedent) to a more specific and potentially tractable question:

**THE MISSING LEMMA (ML-1)**: Within the Balaban construction at scale k <= k_* (where g_{k_*}^2 is fixed and small but not infinitesimal), the contribution of scales k <= k_* to the two-point correlator S_2(x,y) at short distances |x-y| << L^{-k_*} is bounded by:

$$|F_{\leq k_*}(x,y)| \leq C_{k_*} |x-y|^{-8+\delta}$$

for some delta > 0 (power suppression relative to the leading singularity).

This lemma says: IR physics does not contaminate the UV singularity structure. In Wilsonian RG language: the irrelevant operators at scale k_* produce sub-leading short-distance corrections. In OPE language: the identity channel dominates.

### What specific computation would close it?

**The Balaban scale-split argument.** The computation has three steps:

**Step A (UV piece -- DONE in principle)**: At scales k > k_*, the Cauchy estimate gives:
$$F_{>k_*}(x,y) = F_{>k_*}^{\text{pert, N-loop}}(x,y) + O\left(\left(\frac{g_{k_*}^2}{\kappa}\right)^N |x-y|^{-8}\right)$$
The perturbative piece has the AF-predicted form C_N |x|^{-8} (log)^{-2} by Reisz power counting (already proved, Step 18 tree-level fragment).

**Step B (IR piece -- THE KEY COMPUTATION)**: At scales k <= k_*, the polymer activities K_k(X, V) have spatial decay |K_k| <= e^{-kappa |X|}. The contribution of these activities to the SHORT-DISTANCE correlator (|x-y| << L^{-k_*}) must be bounded.

The intuition: the polymer activities at scale k operate on lattice spacing ~ L^{-k}. At short distances |x-y| << L^{-k_*} << L^{-k} for k <= k_*, the lattice site containing x is the SAME as the lattice site containing y. Therefore the correlator at short distances is determined by LOCAL physics at scale k, which is the effective coupling g_k^2 -- and this is where the RG deviation bound (Step 11, C_new g_k^4 Delta-hat^2) enters.

**Proposed bound**: The IR contribution satisfies
$$|F_{\leq k_*}(x,y)| \leq \sum_{k=0}^{k_*} C_{\text{new}} g_k^4 \hat{\Delta}_k^2 \cdot |x-y|^{-8+2}$$
where the |x-y|^{-8+2} = |x-y|^{-6} comes from the deviation order dev >= 2 (Step 9*). This is sub-leading compared to |x-y|^{-8}.

**Step C (assembly)**: Combine UV (Step A) and IR (Step B):
$$F(x,y) = C_N |x-y|^{-8} (\log 1/|x-y|\Lambda)^{-2} [1 + O((\log)^{-1})] + O(|x-y|^{-6}) + O(|x|^{11N/6})$$

The leading term is the AF prediction. The sub-leading terms (dimension-6 from IR scales, dimension-11N/6 from instantons) are both power-suppressed. This IS H4.

### Difficulty assessment

**Step A**: Already proved in principle (Cauchy estimate + Reisz). Needs to be assembled explicitly. Difficulty: 3/10.

**Step B**: This is the key missing computation. It requires:
- Extracting the short-distance behavior of the polymer expansion at IR scales.
- Using the deviation bound (dev >= 2, Steps 8-9) to show that the IR contribution is dimension-6, not dimension-8.
- Summing over IR scales using the convergent sum from Step 13.

The deviation order dev >= 2 was proved EXACTLY for this purpose (to control the RG flow), but it has never been applied to the short-distance behavior of the correlator (only to the mass gap). Repurposing it for the correlator is a non-trivial but well-motivated computation within the existing framework.

**Difficulty: 6/10.** This is hard but SPECIFIC, and leverages existing proved results (B1 + AF + dev >= 2 + convergent RG sum) in a new combination. It does NOT require external unlocks (Borel summability, resurgence, large-N).

**Step C**: Assembly. Difficulty: 2/10.

### Overall closure probability via cross-route synthesis

**P(H4 closure via scale-split + Cauchy + deviation) = 0.25 -- 0.35**

This is substantially higher than any single route (best was 0.15 for "polymer perturbative content") because:
1. It does not require global Borel summability (only scale-by-scale Cauchy).
2. It leverages the deviation bound (dev >= 2) which was proved for a different purpose but is structurally the right tool.
3. It reduces the problem to a SPECIFIC computation (Step B) within the Balaban framework, not to an external open problem.

### Comparison with prior probability estimates

| Source | P(mathematical closure) |
|---|---|
| Blackboard (pre-excision) | 0.50 (Route A alone) |
| Excision verdict (post 7 routes) | 0.31 (1 - product of failure probs) |
| This synthesis (scale-split path) | 0.25-0.35 (single specific path) |

The synthesis does not dramatically change the aggregate probability, but it identifies a SPECIFIC computational path that was not visible to any single route. The prior 0.31 was distributed across 5 routes with no clear favorite; this synthesis concentrates probability on a single well-defined computation.

---

## Recommendation for Cycle 2

**Target**: Prove the Missing Lemma (ML-1) via the Balaban scale-split argument.

**Specifically**:
1. Define the scale-split F = F_{>k_*} + F_{<=k_*} rigorously within the Balaban RG framework.
2. For F_{>k_*}: apply the Cauchy estimate at each scale k > k_* to show perturbative agreement with remainder O((g_{k_*}/kappa)^N).
3. For F_{<=k_*}: use the deviation bound (dev >= 2, Steps 8-9) to show that IR contributions to the short-distance two-point function are dimension-6 (or higher), hence sub-leading compared to the dimension-8 leading singularity.
4. Assemble and verify that the leading short-distance behavior is the AF prediction.

**Key resource**: The deviation bound (Steps 8-9-10-11) was proved to control the mass gap. The same bound, applied to the correlator, should control the short-distance behavior. The argument is: if ALL dimension-6 operators have dev >= 2, then their contribution to ANY correlator at short distances is O(g^4 |x|^{-8+2}) = O(g^4 |x|^{-6}), which is sub-leading.

**What to read**: Appendix L (gradient-flow Schwinger functions), Section 5.5 (non-perturbative deviation bound), and the Balaban CMP 109 polymer expansion at low scales. The connection between the deviation bound and correlator short-distance behavior is the new mathematical content.

**Risk**: The deviation bound was proved for the EFFECTIVE ACTION (energy-level perturbation), not for CORRELATORS (Green's function). Translating from one to the other requires showing that the effective action deviation bound implies a correlator deviation bound. This is plausible (the effective action generates the correlators) but non-trivial.

---

## Summary

The cross-route synthesis identifies a viable path that no single route could see:

**Instanton suppression (Route 3)** eliminates |k| >= 1 sectors.
**Cauchy estimate (B1 + AF)** controls UV scales within k=0.
**Deviation bound (Steps 8-11)** controls IR scales within k=0.
**Assembly** gives the AF-predicted leading singularity with power-suppressed corrections.

The specific missing computation is the **translation of the deviation bound from the effective action to the correlator's short-distance behavior** -- a well-defined problem within the Balaban framework that does not require external unlocks. Difficulty 6/10. Closure probability 0.25-0.35.

This is the recommended target for Cycle 2.
