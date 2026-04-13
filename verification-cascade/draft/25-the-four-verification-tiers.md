# 25 — The Four Verification Tiers

---

## Four targets, ordered by strategic value

The verification cascade attacks four external dependencies across the four proof chains. Each target is a TIER with its own capacitor, its own brief, and its own expected outcome. The tiers are ordered by strategic value — highest first, pilot first.

## Tier 4 (Pilot): Boegli + Teschl — spectral exactness verification

**Target:** Sabine Boegli, "Convergence of sequences of linear operators and their spectra" (Integral Equations and Operator Theory, 2017). Plus Gerald Teschl et al., "Simplified verification of gsrc" (arXiv:2601.10476, 2026 preprint).

**Why pilot:** Smallest target, cleanest proofs, bounded scope. Boegli's theorem is a single result with two conditions (H1: generalized strong resolvent convergence, H2: discrete compactness). Teschl provides a simplification that is useful but not load-bearing (the original Boegli proof stands without Teschl). The pilot verifies the verification cascade's ARCHITECTURE before deploying it on the main event.

**What it proves for the framework:** Paper 13's Layer 4 uses Boegli to guarantee spectral exactness — that spec(D_infinity) = lim spec(D_N) with no spurious eigenvalues. Without Boegli, the Hurwitz argument in Layer 5 could produce false zeros. Verifying Boegli confirms Layer 4 is solid.

**Expected outcome:** SURVIVED. Boegli's theorem is published in a peer-reviewed journal (Springer, 2017), is focused and clean, and has no known issues. The pilot's primary value is validating the architecture, not finding errors.

**If WEAKENED:** The weakness would likely be in the application (do Boegli's conditions hold for the CCM operators?) rather than in Boegli's theorem itself. This would be a Paper 13 finding, not a Boegli finding — and it would inform the Tier 1 CCM verification.

**Capacitor charge:** Small. Boegli paper + Teschl preprint + Paper 13 Layer 4 description + Rellich-Kondrachov (classical, background) + Reed-Simon II KLMN (classical, background). ~5 five-field cards. ~0 kills to import (no prior work in this specific domain).

## Tier 1 (Main Event): CCM 2025 — spectral realization of Riemann zeros

**Target:** Alain Connes, Caterina Consani, and Henri Moscovici, "Zeta Spectral Triples" (arXiv:2511.22755, November 2025).

**Why main event:** The RH proof's ONLY conditional. Nobody in the world has independently verified it. First independent check of a Fields medalist's spectral realization programme. Highest strategic value for the Clay submission.

**What it proves for the framework:** Paper 13 is conditional on CCM: "Theorem 1.1 conditional on CCM." If CCM survives independent verification, Paper 13's confidence floor jumps from 8/10 to 9/10. If CCM is WEAKENED, the specific weakness is identified and excision routes pre-identified. If CCM is BROKEN (unlikely given the numerical evidence and Connes's track record), the framework needs to reroute — but it has three alternative paths to RH (R.QFT-1 Atiyah-Singer, R.QFT-7 Penrose, R.OA-6 cyclic cohomology index).

**Key results to verify:**
- Theorem 4.2: self-adjointness of D_N via Caratheodory-Fejer rank-one perturbation
- Theorem 5.10: eigenvalue convergence to Riemann zeros as N grows
- Lemma 5.2(i): T commutes with parity involution (even-sector restriction)
- Lemma 7.2: eigenvector properties
- Lemma 7.3: Fourier transforms of eigenvectors converge to Riemann Xi function
- §7 Outlook assessment: the "main remaining obstacle" (rigorous UV asymptotics matching)

**Expected outcome:** SURVIVED with possible WEAKENED on §7 (which CCM's own authors flag as open — this is not a verification finding but a confirmation of the authors' honest assessment).

**If WEAKENED on a theorem:** Immediate Tier B excision. Pre-identified routes: Kato-Rellich perturbation for Thm 4.2, Weyl asymptotics for Thm 5.10, Connes-van Suijlekom 2025 alternative for Lemma 7.3. The CCM capacitor has pre-identified excision candidates for every load-bearing step.

**Capacitor charge:** Large. CCM 2025 full extracted proof chain (~30 steps) + CCM 2024 precursor (published results, stronger status) + Paper 13 Layer 1 interface + prolate wave operator background + Caratheodory-Fejer theory + rank-one perturbation theory + K-1 from H4 closure (CCM -> YM port is Wrong-space — different domain, but the lexical "perturbation" confusion applies) + numerical verification data (55-digit agreement, 10^-1235 probability).

## Tier 2 (Historic): Balaban — polymer expansion verification

**Target:** Tadeusz Balaban, "Renormalization group approach to lattice gauge field theories" (Communications in Mathematical Physics, volumes 95-119, 1984-1998). Specifically: the interface with Paper 8 Steps 1-3.

**Why historic:** First independent verification of Balaban's construction in 40 years. The YM mass gap (17/18 unconditional — the mass gap itself) rests on Balaban. Dimock's scalar re-derivation (2011-2013) provides a half-charged starting point.

**What it proves for the framework:** Paper 8 Steps 1-3 use Balaban's results directly: polymer expansion convergence (CMP 109 Thm 1), UV stability (CMP 109, 119), propagator/kernel analyticity with k-independent radius (CMP 95-109). Verifying these at the interface Paper 8 uses makes the unconditional 17/18 core — the mass gap — grounded on independently verified foundations.

**Key results to verify:**
- CMP 109 Theorem 1: polymer expansion convergence
- CMP 95-109: propagator bounds and analyticity preservation
- CMP 109/119: UV stability
- The scalar-to-gauge gap: what Dimock proved (scalar phi^4 on 3D torus) vs what Paper 8 needs (SU(N) YM on 4D torus x S^1/Z_2)

**Starting point:** Dimock's three papers (arXiv:1108.1335, 1212.5562, 1304.0705) are a PARTIAL RE-DERIVATION of Balaban's approach for the scalar model. The capacitor starts half-charged: Dimock's scalar results are VERIFIED (published, re-derived), and the verification target is the GAP between scalar and gauge.

**Expected outcome:** SURVIVED at the interface level. Balaban's results have been cited without correction for 40 years. The scalar-to-gauge gap may produce WEAKENED findings — the gauge extension involves subtleties (Haar measure, Faddeev-Popov gauge fixing) that the scalar model doesn't have.

**If WEAKENED on the scalar-to-gauge gap:** This is the most valuable finding. The gap between Dimock (scalar) and Balaban (gauge) is where new mathematics would be needed. Tier B excision would attempt to bridge the gap independently. Tier C construction would look for alternative lattice RG approaches (Magnen-Seneor, Rivasseau).

**Capacitor charge:** Medium. Dimock's 3 papers (half-charge) + Balaban CMP 109/119 specific theorems + Paper 8 PROOF-CHAIN.md Steps 1-3 + H4 closure findings (analyticity is load-bearing for H4) + Weitzenboeck-Bochner (classical, not part of Balaban but adjacent) + constructive QFT background.

## Tier 3 (Interface): Bulatov-Zhuk — CSP dichotomy verification

**Target:** Andrei Bulatov, "A dichotomy theorem for nonuniform CSPs" (FOCS 2017). Dmitriy Zhuk, "A proof of the CSP dichotomy conjecture" (JACM 2020). Specifically: the classification at the interface Paper 28 uses.

**Why interface:** The full Bulatov-Zhuk proofs are hundreds of pages — too large for complete verification. The verification targets the INTERFACE: the classification of the 6 Schaefer classes and the Taylor polymorphism characterization that Paper 28's Link 3 depends on. The framework's own computational verification (6/6 TGap, 6/6 holonomy, PATB-DIAGONAL) provides INDEPENDENT evidence for the classification.

**What it proves for the framework:** Paper 28 Link 3 uses BZ as a classification engine: "CSP is in P iff Taylor polymorphism exists; otherwise NP-complete." Verifying this at the Schaefer-class level confirms Link 3 is solid. The framework's computational data provides a second route — if BZ breaks but computation agrees, the computation is the proof at the Schaefer level.

**Key results to verify:**
- The dichotomy statement: Taylor polymorphism <-> P-time, no Taylor <-> NP-complete
- The classification on the 6 Schaefer classes: 2-SAT, Horn, Dual-Horn, XOR, 1-in-3, NAE-3
- The Taylor polymorphism characterization: what "Taylor operation" means precisely
- Consistency between BZ's classification and the framework's computational verification (6/6 match)

**Expected outcome:** SURVIVED. Two independent proofs (Bulatov + Zhuk) of the same theorem is a natural LOCK. The computational verification provides a third independent confirmation.

**Capacitor charge:** Medium. BZ dichotomy statement + 6 Schaefer classes + P vs NP toolkit H.3 (five-piece argument, kill list, trinity, Rule 9 v3, verified results) + 18 kills from prior P vs NP work + amplification results. The P vs NP capacitor (framework-tools-v4.md) is already the most mature capacitor in the framework — the Tier 3 capacitor inherits most of it.

---

*Four tiers. Tier 4 (Boegli, pilot): validate the architecture. Tier 1 (CCM, main event): first independent verification of Connes's spectral realization. Tier 2 (Balaban, historic): first check in 40 years, starting from Dimock's half-charge. Tier 3 (Bulatov-Zhuk, interface): classification verification backed by independent computation. Each tier has its own capacitor, its own brief, its own expected outcome, and its own escalation routes.*
