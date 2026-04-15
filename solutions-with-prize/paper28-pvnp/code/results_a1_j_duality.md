# Results: A1 Modular Conjugation J-Duality Between P and NPC Sectors

**Test:** `test_a1_j_duality.py`
**Date:** 2026-04-11
**Authors:** G Six, Claude Opus 4.6

---

## Setup

- **Instances:** 30 random each of 2-SAT (P-time) and 3-SAT (NPC)
- **Sizes:** n = 8 (256 assignments), n = 10 (1024 assignments)
- **2-SAT ratio:** m/n = 2.0; **3-SAT ratio:** m/n = 4.0

## Test 1: Solution Space Profiles

| Metric | 2-SAT (n=8) | 3-SAT (n=8) | 2-SAT (n=10) | 3-SAT (n=10) |
|:-------|:------------|:-------------|:-------------|:-------------|
| Mean |Sol| | 2.8 | 3.6 | 2.4 | 4.2 |
| Median |Sol| | 2 | 2 | 0 | 3 |
| Mean components | 0.8 | 1.5 | 0.5 | 1.5 |
| Solution Laplacian gap | 1.023 | 0.612 | 1.045 | 0.267 |

**Observation:** 2-SAT solution graphs tend to be more connected (fewer components, larger spectral gap) than 3-SAT solution graphs. The spectral gap ratio widens from 1.67x at n=8 to 3.92x at n=10, consistent with the P/NPC structural divergence amplifying with n.

## Test 2: Constraint Space Profiles

| Metric | 2-SAT (n=8) | 3-SAT (n=8) | 2-SAT (n=10) | 3-SAT (n=10) |
|:-------|:------------|:-------------|:-------------|:-------------|
| Constraint Laplacian gap | 1.116 | 16.200 | 0.820 | 15.437 |

**Observation:** 3-SAT constraint graphs have a dramatically larger spectral gap (~15-16) than 2-SAT (~0.8-1.1). This reflects the denser constraint structure of 3-SAT (3 variables per clause, higher ratio m/n = 4.0 vs 2.0). The constraint graph of 3-SAT is much more "rigid."

## Test 3: J-Duality Spectral Cross-Comparison

**Question:** Does the eigenvalue spectrum of 2-SAT's solution graph resemble the eigenvalue spectrum of 3-SAT's constraint graph?

| Comparison | n=8 | n=10 |
|:-----------|:----|:-----|
| Cross: 2-SAT sol adj vs 3-SAT con Lap | 0.207 | 0.236 |
| Control: 2-SAT sol adj vs 3-SAT sol adj | 0.199 | 0.252 |
| Control: 2-SAT con Lap vs 3-SAT con Lap | 0.217 | 0.231 |
| **J-ratio (cross / control_sol)** | **1.042** | **0.939** |

**Verdict: FAIL.** The cross-spectral distance (2-SAT solution vs 3-SAT constraint) is indistinguishable from within-class controls. J-ratio is ~1.0 at both sizes, meaning the cross-comparison is no closer than random pairings. No spectral duality detected.

### Test 3b: Distribution Duality

**Question:** Does the Hamming distance distribution of 2-SAT solutions resemble the clause overlap distribution of 3-SAT?

| Comparison | n=8 | n=10 |
|:-----------|:----|:-----|
| Cross: 2-SAT Hamming vs 3-SAT clause overlap (W1) | 1.747 | 1.179 |
| Control: 2-SAT Hamming vs 2-SAT Hamming (W1) | 0.881 | 0.879 |
| **Distribution ratio** | **1.984** | **1.342** |

**Verdict: FAIL.** The cross-distribution distance is 1.3-2.0x the within-class distance. The distributions live on different supports (Hamming distances up to n, clause overlaps concentrated at small values). No distribution duality.

## Test 4: Complement (Anti-Solution) Test

**Question:** Does the anti-solution set {0,1}^n \ Sol(3-SAT) have P-time structure (closure under Taylor operations)?

| Metric | n=8 | n=10 |
|:-------|:----|:-----|
| Mean |nonSol| | 252.4 / 256 (98.6%) | 1019.8 / 1024 (99.6%) |
| Majority closure | 0.992 | 0.997 |
| Affine closure | 0.985 | 0.996 |
| 2-SAT solutions majority closure | 1.000 | 1.000 |
| 2-SAT solutions affine closure | 0.965 | 0.938 |

**Nominal verdict: PASS** -- anti-solution sets show >99% closure under majority.

**Critical caveat:** This is a **size artifact**, not genuine duality. When the anti-solution set comprises 98.6-99.6% of all assignments, a random triple `(a,b,c)` has majority `maj(a,b,c)` that lands in the dense set with probability approaching 1 by simple counting, regardless of any algebraic structure. A random subset of {0,1}^n containing fraction p of all assignments has majority closure approximately p^3 + 3p^2(1-p) which for p=0.986 gives ~0.9999. The observed 0.992 is actually *below* this random baseline, suggesting the anti-solution set is if anything *less* closed under majority than a random dense set.

**Corrected verdict: FAIL.** The high closure rate is a trivial consequence of the anti-solution set being nearly all of {0,1}^n. There is no evidence of genuine Taylor closure structure.

## Test 5: Spectral Duality (Product/Sum)

**Question:** Is there a relationship lambda_i * mu_i = C or lambda_i + mu_i = C between paired Laplacian spectra?

| Metric | n=8 | n=10 |
|:-------|:----|:-----|
| Product duality spread | 0.853 | 0.871 |
| Sum duality spread | 0.613 | 0.592 |
| Cross product spread | 0.689 | 0.753 |
| Cross sum spread | 0.284 | 0.302 |

**Verdict: FAIL.** A relative spread of 0.1 or less would indicate approximate constancy. All spreads are 0.28-0.87, far from the duality threshold. No product or sum spectral duality exists between 2-SAT and 3-SAT Laplacian spectra.

---

## Overall Verdict

| Test | Result | Interpretation |
|:-----|:-------|:---------------|
| T3: Spectral J-duality | **FAIL** | No cross-spectral resemblance |
| T3b: Distribution duality | **FAIL** | No Hamming-overlap correspondence |
| T4: Complement Taylor closure | **FAIL** (artifact) | Dense set artifact, not genuine structure |
| T5a: Product spectral duality | **FAIL** | No lambda*mu = C relationship |
| T5b: Sum spectral duality | **FAIL** | No lambda+mu = C relationship |
| T5c: Cross-sector duality | **FAIL** | No cross-sector spectral constant |

### **OVERALL: FAIL -- No J-like duality detected at finite level**

---

## Interpretation for the A1 Conjecture

The finite-dimensional tests find **no evidence** of a structural bijection between the P-time solution profile and the NPC constraint profile. Specifically:

1. **Solution spaces are structurally different, not dual.** 2-SAT solutions form more connected graphs with larger spectral gaps; 3-SAT solutions are more fragmented. These are *asymmetric* differences, not dual/complementary ones.

2. **Constraint spaces are on different scales.** 3-SAT constraint graphs have spectral gaps 15-20x larger than 2-SAT. This reflects the density difference, not a duality.

3. **The complement is trivially dense.** At the standard clause/variable ratios, 3-SAT instances have very few solutions relative to 2^n. The anti-solution set is nearly all of {0,1}^n and has no interesting algebraic structure -- it is closed under everything by sheer density.

4. **No spectral constant.** There is no multiplicative or additive relationship between paired eigenvalues from the two sectors.

### What this means for A1

The modular conjugation J on a type III_1 factor is an antiunitary involution that exchanges M and its commutant M'. The finite-dimensional analogs tested here -- structural bijections between solution-space and constraint-space profiles -- show no such duality.

This does **not** kill the A1 conjecture outright. The Tomita-Takesaki J operates on the full infinite-dimensional factor M_Bool, not on individual finite instances. The duality, if it exists, may require:
- The thermodynamic limit n -> infinity
- The full modular automorphism group sigma_t, not just static spectral comparison
- The type III_1 structure (no finite-dimensional analog exists for type III)

**Recommendation:** Redirect computational effort to A4 (heat kernel / Seeley-DeWitt) or A6 (KMS phase transition), which probe the infinite-dimensional/thermodynamic-limit structure more naturally. The J-duality, if it exists, is not a finite-level phenomenon.
