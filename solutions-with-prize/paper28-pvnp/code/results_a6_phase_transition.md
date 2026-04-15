# Results: KMS Phase Transition in CSP Partition Functions

*A6 from strategy/10-amplification-entries.md*

**Date:** 2026-04-11
**Authors:** G Six (originator), Claude Opus 4.6 (collaborator)

---

## 0. Executive Summary

**VERDICT: FAIL (1/4 tests positive)**

The CSP partition function Z\_Gamma(beta) = sum\_x exp(-beta * violations(x)) exhibits
a specific heat peak at beta\_c ~ 2.0 for ALL four Schaefer classes tested. The
phase transition structure does NOT cleanly separate P-time from NPC complexity
classes at the system sizes examined (n = 8, 10, 12).

The single positive finding: the specific heat peak height GROWS with system size
for 3-SAT (scaling exponent alpha ~ 0.95), consistent with a genuine thermodynamic
phase transition in the large-n limit. However, this growth also appears in the
P-time classes, so it does not constitute a separation.

**The conjecture as stated is not supported.** The partition function's
thermodynamic structure reflects constraint density (clause ratio alpha) rather
than computational complexity. At matched alpha, P-time and NPC classes produce
nearly identical specific heat curves.

---

## 1. Methodology

### Parameters
- **System sizes:** n = 10, 12 (main), n = 8, 10, 12 (finite-size scaling)
- **Instances:** 50 random instances per (class, n) pair
- **Exact enumeration:** all 2^n assignments evaluated
- **Clause ratios:** 2-SAT: alpha=2.0, Horn-SAT: alpha=3.0, 3-SAT: alpha=4.0, NAE-3-SAT: alpha=2.0

### Inverse temperatures
beta in {0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 10.0, 15.0, 20.0, 50.0}

### Thermodynamic quantities
- **Partition function:** Z(beta) = sum\_x exp(-beta * v(x)), computed via log-sum-exp
- **Free energy:** F(beta) = -log Z / beta
- **Mean energy:** <E> = sum\_x v(x) P\_beta(x) where P\_beta(x) = exp(-beta v(x))/Z
- **Specific heat:** C(beta) = beta^2 * Var\_beta(violations)
- **Susceptibility:** chi(beta) = Var\_beta(violations) = d^2(log Z)/d(beta)^2
- **Entropy:** S(beta) = beta * <E> + log Z

---

## 2. Partition Function Z(beta) at n=12

| beta | 2-SAT (P) | Horn-SAT (P) | 3-SAT (NPC) | NAE-3-SAT (NPC) |
|:-----|:----------|:-------------|:-------------|:-----------------|
| 0.01 | 8.2580 | 8.2520 | 8.2580 | 8.2580 |
| 0.05 | 8.0232 | 7.9975 | 8.0241 | 8.0232 |
| 0.10 | 7.7393 | 7.6943 | 7.7428 | 7.7393 |
| 0.20 | 7.2024 | 7.1499 | 7.2163 | 7.2022 |
| 0.50 | 5.8146 | 5.8866 | 5.8946 | 5.8200 |
| 1.00 | 4.1105 | 4.6462 | 4.3615 | 4.1447 |
| 1.50 | 2.9520 | 3.9794 | 3.4038 | 3.0938 |
| 2.00 | 2.1952 | 3.5882 | 2.7963 | 2.3613 |
| 3.00 | 1.2750 | 3.2380 | 2.1512 | 1.3862 |
| 5.00 | 0.7765 | 3.0734 | 1.6962 | 0.7981 |
| 8.00 | 0.6973 | 3.0460 | 1.6139 | 0.6985 |
| 10.0 | 0.6937 | 3.0447 | 1.6100 | 0.6939 |
| 15.0 | 0.6932 | 3.0445 | 1.6094 | 0.6932 |
| 20.0 | 0.6931 | 3.0445 | 1.6094 | 0.6931 |
| 50.0 | 0.6931 | 3.0445 | 1.6094 | 0.6931 |

Values are log Z (median over 50 instances).

**Observation:** At beta -> infinity, log Z converges to log(|Sol|). The ground
state degeneracies are: 2-SAT ~ 2, Horn-SAT ~ 21, 3-SAT ~ 5, NAE-3-SAT ~ 2.
Horn-SAT has the largest solution count at this alpha, consistent with Q7 findings.

---

## 3. Specific Heat C(beta) at n=12

| beta | 2-SAT (P) | Horn-SAT (P) | 3-SAT (NPC) | NAE-3-SAT (NPC) |
|:-----|:----------|:-------------|:-------------|:-----------------|
| 0.01 | 0.000436 | 0.000828 | 0.000509 | 0.000435 |
| 0.05 | 0.010662 | 0.019724 | 0.012444 | 0.010646 |
| 0.10 | 0.041569 | 0.076599 | 0.047932 | 0.041622 |
| 0.20 | 0.155923 | 0.276808 | 0.181341 | 0.159941 |
| 0.50 | 0.793266 | 1.128587 | 0.860118 | 0.822112 |
| 1.00 | 2.054972 | 2.121767 | 2.186009 | 2.153598 |
| 1.50 | 2.945159 | **2.474400** | 2.966847 | 2.877890 |
| 2.00 | **3.337809** | 2.423067 | **3.287716** | **3.155660** |
| 3.00 | 3.143893 | 1.904617 | 3.099051 | 2.612710 |
| 5.00 | 1.098107 | 0.695968 | 1.200280 | 1.016592 |
| 8.00 | 0.138652 | 0.089151 | 0.156485 | 0.131117 |
| 10.0 | 0.029306 | 0.018858 | 0.033135 | 0.027742 |
| 15.0 | 0.000444 | 0.000286 | 0.000502 | 0.000421 |
| 20.0 | 0.000005 | 0.000003 | 0.000006 | 0.000005 |
| 50.0 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

Bold values indicate the peak for each class.

**Key finding:** All four classes exhibit a clear specific heat peak. Horn-SAT peaks
earlier (beta_c = 1.5) and lower (C_max = 2.47) than the other three, which all
peak at beta_c = 2.0 with heights in the range 3.15--3.34. But 2-SAT (P-time) has
the HIGHEST peak of all, contradicting the conjecture that NPC should have sharper
transitions.

---

## 4. Susceptibility chi(beta) at n=12

| beta | 2-SAT (P) | Horn-SAT (P) | 3-SAT (NPC) | NAE-3-SAT (NPC) |
|:-----|:----------|:-------------|:-------------|:-----------------|
| 0.01 | 4.356 | 8.276 | 5.091 | 4.352 |
| 0.10 | 4.157 | 7.660 | 4.793 | 4.162 |
| 0.50 | 3.173 | 4.514 | 3.440 | 3.288 |
| 1.00 | 2.055 | 2.122 | 2.186 | 2.154 |
| 2.00 | 0.834 | 0.606 | 0.822 | 0.789 |
| 5.00 | 0.044 | 0.028 | 0.048 | 0.041 |

The susceptibility chi = Var(violations) is monotonically decreasing in beta for all
classes. This means the susceptibility does NOT show a peak at finite beta; the
maximum is always at beta -> 0 (infinite temperature). The chi "peak" is an
artifact of the flat beta -> 0 limit. There is no chi-detected phase transition
at any finite beta.

---

## 5. Peak Analysis

### Summary table (median over 50 instances)

| Class | Type | n | beta\_c (C) | C\_max | FWHM | Sharpness |
|:------|:-----|:--|:-----------|:------|:-----|:----------|
| 2-SAT | P | 10 | 2.0 | 2.677 | 3.59 | 0.746 |
| Horn-SAT | P | 10 | 1.5 | 2.139 | 3.50 | 0.611 |
| 3-SAT | NPC | 10 | 2.0 | 2.693 | 3.67 | 0.735 |
| NAE-3-SAT | NPC | 10 | 2.0 | 2.703 | 3.58 | 0.756 |
| 2-SAT | P | 12 | 2.0 | 3.338 | 3.59 | 0.928 |
| Horn-SAT | P | 12 | 1.5 | 2.474 | 3.55 | 0.697 |
| 3-SAT | NPC | 12 | 2.0 | 3.288 | 3.74 | 0.880 |
| NAE-3-SAT | NPC | 12 | 2.0 | 3.156 | 3.51 | 0.898 |

### Per-instance peak distribution at n=12

| Class | Type | Mean C\_max | Std C\_max | Modal beta\_c |
|:------|:-----|:----------|:---------|:-------------|
| 2-SAT | P | 3.444 | 0.740 | 2.0 (29/50) |
| Horn-SAT | P | 2.593 | 0.542 | 1.5 (29/50) |
| 3-SAT | NPC | 3.449 | 0.646 | 2.0 (27/50) |
| NAE-3-SAT | NPC | 3.512 | 0.702 | 2.0 (24/50) |

**Critical observation:** 2-SAT and 3-SAT are INDISTINGUISHABLE in their C(beta) peak
structure. Same location (beta_c = 2.0), essentially identical heights (3.44 vs 3.45),
similar widths. A P-time class (2-SAT) produces the same thermodynamic signature
as an NPC class (3-SAT).

Horn-SAT is the outlier: earlier peak (beta_c = 1.5), lower height, narrower width.
But this reflects the different CONSTRAINT STRUCTURE (Horn clauses are weaker), not
the complexity class. NAE-3-SAT, which is also NPC, has a peak height (3.51) only
marginally above 2-SAT (3.44).

---

## 6. Finite-Size Scaling (3-SAT, alpha=4.0)

| n | beta\_c | C\_max | FWHM |
|:--|:--------|:-------|:-----|
| 8 | 2.0 | 2.271 | 3.49 |
| 10 | 2.0 | 2.850 | 3.63 |
| 12 | 2.0 | 3.332 | 3.50 |

- Peak height ratio n=12/n=8: **1.467**
- Effective scaling exponent (C\_max ~ n^alpha): **alpha = 0.945**

The peak height grows approximately linearly with n. This IS consistent with a
genuine phase transition in the thermodynamic limit (a crossover would have bounded
peak height). However, the same linear growth occurs for the P-time classes
(C_max increases from ~2.68 to ~3.34 for 2-SAT between n=10 and n=12), so
the growth does not distinguish P from NPC.

---

## 7. KMS Connection: Entropy at beta = 1

The Bost-Connes critical point is beta = 1. The entropy S(1) = beta * <E> + log Z
measures the information content of the Boltzmann distribution at this critical
temperature.

| Class | Type | S(1) n=10 | S(1) n=12 | S(1)/n n=10 | S(1)/n n=12 |
|:------|:-----|:----------|:----------|:------------|:------------|
| 2-SAT | P | 5.801 | 6.890 | 0.580 | 0.574 |
| Horn-SAT | P | 5.313 | 6.478 | 0.531 | 0.540 |
| 3-SAT | NPC | 5.650 | 6.810 | 0.565 | 0.567 |
| NAE-3-SAT | NPC | 5.740 | 6.885 | 0.574 | 0.574 |

**Entropy per variable at n=12:**
- P range: [0.540, 0.574]
- NPC range: [0.567, 0.574]

The ranges OVERLAP. S(1)/n does not separate P from NPC. The entropy density
at the BC critical point is essentially the same (~0.57) for all classes except
Horn-SAT, which is slightly lower (~0.54) due to its different constraint structure.

**Statistical separation at n=12:**
- P-time mean S(1): 6.687
- NPC mean S(1): 6.829
- Ratio NPC/P: 1.021

A 2% difference -- far too small and non-systematic for a genuine separation.

---

## 8. NPC/P Peak Height Ratios

| n | Comparison | Ratio |
|:--|:-----------|:------|
| 10 | C\_peak(3-SAT) / C\_peak(2-SAT) | 1.006 |
| 10 | C\_peak(NAE-3-SAT) / C\_peak(2-SAT) | 1.010 |
| 10 | C\_peak(3-SAT) / C\_peak(Horn-SAT) | 1.259 |
| 10 | C\_peak(NAE-3-SAT) / C\_peak(Horn-SAT) | 1.264 |
| 12 | C\_peak(3-SAT) / C\_peak(2-SAT) | 0.985 |
| 12 | C\_peak(NAE-3-SAT) / C\_peak(2-SAT) | 0.945 |
| 12 | C\_peak(3-SAT) / C\_peak(Horn-SAT) | 1.329 |
| 12 | C\_peak(NAE-3-SAT) / C\_peak(Horn-SAT) | 1.275 |

NPC classes do NOT have systematically higher peaks than P-time classes. At n=12,
2-SAT (P) actually has a HIGHER C\_peak than both 3-SAT and NAE-3-SAT (NPC).
The only consistent separation is vs. Horn-SAT, which reflects clause structure,
not complexity.

---

## 9. Energy Curves <E>(beta) at n=12

| beta | 2-SAT (P) | Horn-SAT (P) | 3-SAT (NPC) | NAE-3-SAT (NPC) |
|:-----|:----------|:-------------|:-------------|:-----------------|
| 0.01 | 5.957 | 6.548 | 5.949 | 5.956 |
| 0.50 | 4.114 | 3.395 | 3.835 | 4.067 |
| 1.00 | 2.816 | 1.768 | 2.464 | 2.677 |
| 2.00 | 1.271 | 0.570 | 0.997 | 1.268 |
| 5.00 | 0.083 | 0.028 | 0.054 | 0.099 |
| 50.0 | 0.000 | 0.000 | 0.000 | 0.000 |

At beta=0 (infinite temperature), the mean number of violations is simply the
fraction of clauses violated by a random assignment times m. At beta -> infinity,
the system freezes into ground states with minimal violations.

Horn-SAT has the steepest energy descent: by beta=2 it is already near ground
state (<E> = 0.57) while the others still have <E> ~ 1. This is because Horn-SAT
clauses are easily satisfied: the all-false assignment satisfies all purely
negative clauses, giving many low-energy configurations.

---

## 10. Why the Conjecture Fails

### The fundamental issue

The partition function Z(beta) = sum\_x exp(-beta * v(x)) treats the constraint
violation count v(x) as an energy. The thermodynamics of this system depends on
the **violation spectrum** {v(x)}, which is determined by the constraint structure
(clause density, clause width, literal polarity distribution). These structural
features vary across CSP classes, but they do NOT track the P/NPC boundary:

1. **2-SAT (P) and NAE-3-SAT (NPC) have nearly identical thermodynamics** at
   matched alpha = 2.0. Their C(beta) curves overlap to within noise. Yet
   one is P-time and the other is NPC. This is a direct counterexample.

2. **Horn-SAT differs from all others**, but this reflects the asymmetric
   clause structure (at most one positive literal), not P-time computability.
   Horn clauses are "soft" constraints that produce a broad, low violation
   spectrum; this shifts the specific heat peak but does not encode a
   complexity distinction.

3. **The energy function v(x) = number of violated clauses is a very coarse
   observable.** It counts constraint violations but throws away all structural
   information about WHICH clauses are violated and HOW they overlap. The
   computational complexity difference between P and NPC lies in this
   correlation structure, not in the marginal violation count.

### What WOULD be needed

For a partition function approach to separate P from NPC, the energy function
would need to encode the correlation structure of constraint satisfaction --
essentially, the polymorphism algebra (cf. Strategy 03, O7, P7). The Boltzmann
measure P\_beta(x) = exp(-beta * v(x)) / Z treats all violations as equivalent
and independent; it cannot detect whether violations can be "repaired" by
a polymorphism operation (P-time) or not (NPC).

A modified energy function that includes interaction terms between clause
violations (measuring the cost of simultaneous unsatisfaction) might show
different phase transition structure. This connects to the area law conjecture
(A5): if the holonomy defect grows with area for NPC but perimeter for P,
then an energy function incorporating spatial correlations between violated
clauses would detect the difference.

---

## 11. Detailed Test Results

### Test 1: NPC peaks sharper than P peaks? -- NO

- P sharpness (max, n=12): 0.928 (2-SAT)
- NPC sharpness (min, n=12): 0.880 (3-SAT)
- Ratio NPC/P: 0.948

NPC peaks are NOT sharper. In fact 2-SAT (P-time) has the highest sharpness.

### Test 2: 3-SAT C\_peak grows with n? -- YES (but non-discriminating)

- C\_max(n=8) = 2.27, C\_max(n=12) = 3.33
- Scaling exponent: 0.95 (approximately linear growth)
- This growth is consistent with a genuine phase transition but also appears
  in P-time classes, so it does not separate P from NPC.

### Test 3: S(beta=1)/n separates P from NPC? -- NO

- P range: [0.540, 0.574]
- NPC range: [0.567, 0.574]
- Ranges overlap (2-SAT has S/n = 0.574, matching NAE-3-SAT exactly)

### Test 4: beta\_c location separates P from NPC? -- NO

- P beta\_c values: {2.0, 1.5}
- NPC beta\_c values: {2.0, 2.0}
- 2-SAT and both NPC classes share beta\_c = 2.0

---

## 12. Connection to Other Paper 28 Tests

| Test | Observable | P vs NPC separation? |
|:-----|:-----------|:---------------------|
| Q1 (polymorphism closure) | Closure violation rate | YES: 0% vs >0% |
| Q3 (spectral gap) | Glauber walk gap | YES: positive vs zero |
| Q7 (entropy density) | s(alpha) curve shape | YES: smooth vs sharp |
| O7 (holonomy) | Holonomy defect | YES: 6/6 |
| **A6 (this test)** | **C(beta), chi(beta), S(1)** | **NO: 1/4 subtests** |

The thermodynamic partition function approach (A6) performs substantially worse
than the algebraic approaches (Q1, Q3, O7) at separating P from NPC. This is
consistent with the theoretical framework: the P/NPC distinction lies in the
algebraic structure of the solution space (polymorphisms, automorphisms), not
in the scalar count of constraint violations.

---

## 13. Verdict

**FAIL** -- 1 of 4 tests positive (finite-size scaling only, and non-discriminating).

The KMS phase transition conjecture (A6) is not supported by the numerical evidence
at n = 8--12. The CSP partition function Z\_Gamma(beta) with energy = violation count
does not encode enough structural information to distinguish P-time from NPC. The
specific heat peak, its location, its height, its width, and the entropy at
beta = 1 all fail to separate the two complexity classes.

**Recommendation:** Close A6 as tested-and-failed. The partition function approach
requires a structurally richer energy function that encodes constraint correlations
(not just marginal violation counts) to have any chance of separating complexity
classes. The algebraic approaches (polymorphism closure, spectral gap, holonomy)
remain the viable path.

---

*Code: `test_a6_phase_transition.py`*
*Data: `results_a6_phase_transition.json`*
