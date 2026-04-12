# Proof: O8-PARTITION (CSP Partition Function as Zeta-Like Object)

**Independent re-verification. Date: 2026-04-12.**
**Code:** `paper28-pvnp/code/reverify_o8_partition.py`
**Seed:** 2026_04_12 (independent of original seed=42)

---

## Claim (PARTIAL: 2 PASS, 3 KILL)

Original verdict: O8 PARTIALLY SUPPORTED (2/5 sub-predictions confirmed).

- PASS V1: Violation spectrum entropy separates P from NPC (5.3% gap)
- PASS V2: Lee-Yang zeros more regular for NPC (spacing ratio NPC > P)
- KILL #6: C(beta) peak does NOT separate P/NPC
- KILL #7: Pade poles are fitting artifacts
- KILL #8: No Riemann spacing match at n=10

---

## V1 Confirmation: Violation Spectrum Entropy -- CONFIRMED

| Class | Mean Entropy | Std | Type |
|:------|:-------------|:----|:-----|
| 2-SAT | 2.899 | 0.190 | P |
| Horn-SAT | 2.848 | 0.065 | P |
| XOR-SAT | 3.177 | 0.163 | P (excluded) |
| 3-SAT (crit) | 3.103 | 0.131 | NPC |
| NAE-3-SAT | 2.945 | 0.141 | NPC |

- P-time (excl XOR) mean entropy: **2.874**
- NPC mean entropy: **3.024**
- Gap: **+5.24%** (NPC higher, same direction as original's 5.3%)

V1 reproduces cleanly with independent seed. The violation spectrum entropy
is a robust separator: NPC problems at critical clause ratio have more
spread violation distributions than P-time problems.

**V1 VERDICT: CONFIRMED.**

---

## V2 Confirmation: Lee-Yang Zero Spacing Regularity -- FLAG: NOT CONFIRMED

| Class | Spacing Ratio | Valid/50 | Type |
|:------|:-------------|:---------|:-----|
| 2-SAT | 0.482 | 35 | P |
| Horn-SAT | 0.824 | 11 | P |
| XOR-SAT | 0.000 | 50 | P (excluded) |
| 3-SAT (crit) | 0.573 | 44 | NPC |
| NAE-3-SAT | 0.609 | 36 | NPC |

- P-time (excl XOR) mean spacing ratio: **0.653**
- NPC mean spacing ratio: **0.591**

The original found NPC > P-time (0.804 vs 0.572). Our re-verification finds
the **opposite**: P-time > NPC (0.653 vs 0.591).

Root cause: Horn-SAT's spacing ratio is highly variable (only 11/50 instances
have enough near-unit-circle zeros to compute it). With seed 42, the few valid
Horn-SAT instances happened to give low values; with our seed, they give high
values. This makes V2 **seed-dependent and statistically fragile**.

The original V2 also claimed "angular uniformity" (NPC 0.696 vs P 0.692, a
0.6% difference). Such a tiny effect is not robust.

**V2 VERDICT: NOT CONFIRMED. The original V2 pass was fragile and does not
reproduce with independent randomness. This should be downgraded to FAIL.**

---

## Kill #6 Confirmation: Specific Heat Peak -- CONFIRMED

| Class | C_max | Std | beta_c | Type |
|:------|:------|:----|:-------|:-----|
| 2-SAT | 2.992 | 0.736 | 2.35 | P |
| Horn-SAT | 0.858 | 0.128 | 1.55 | P |
| XOR-SAT | 4.143 | 0.940 | 1.60 | P |
| 3-SAT (crit) | 3.075 | 0.839 | 2.13 | NPC |
| NAE-3-SAT | 3.039 | 0.693 | 2.36 | NPC |

- P-time (excl XOR) C_max mean: 1.925
- NPC C_max mean: 3.057

Note: there is a gap in C_max means (NPC higher), but the within-class
variance is enormous. 2-SAT alone has C_max = 2.99 +/- 0.74, completely
overlapping with NPC's 3.08 +/- 0.77. Horn-SAT pulls down the P-time
average due to its structural simplicity (at most 1 positive literal),
not due to polynomial-time computability.

The original correctly concluded: C_max is a thermal property of the
constraint density and structure, not the complexity class.

**Kill #6 VERDICT: CONFIRMED. No clean P/NPC separation.**

---

## Kill #7 Confirmation: Pade Poles are Artifacts -- CONFIRMED

| Class | Pade q median | Fraction at q=8 | Type |
|:------|:-------------|:----------------|:-----|
| 2-SAT | 8 | 29/50 | P |
| Horn-SAT | 8 | 36/50 | P |
| XOR-SAT | 2 | 0/50 | P |
| 3-SAT (crit) | 4 | 16/50 | NPC |
| NAE-3-SAT | 7 | 24/50 | NPC |

The original found q=8 uniformly for all classes. Our rerun finds variation,
with P-time (m=20) selecting HIGHER q than NPC (m=42). This is a
clause-count confound: lower m produces lower-degree violation polynomials,
which Pade fits with more denominator terms. It is NOT a complexity signal.

The structural argument is definitive: Z(u) = sum d_v * u^v is already an
exact polynomial of degree max_v. Any Pade denominator with q > 0 introduces
spurious poles that do not exist in the true partition function. The Pade
poles are fitting artifacts for ALL classes.

**Kill #7 VERDICT: CONFIRMED. Pade poles are structural artifacts.**

---

## Kill #8 Confirmation: No Riemann Spacing Match -- CONFIRMED

| Class | Matches | Comparisons | Rate | Type |
|:------|:--------|:-----------|:-----|:-----|
| 2-SAT | 40 | 3220 | 0.012 | P |
| Horn-SAT | 52 | 4760 | 0.011 | P |
| XOR-SAT | 12 | 4774 | 0.003 | P |
| 3-SAT (crit) | 47 | 3920 | 0.012 | NPC |
| NAE-3-SAT | 31 | 3094 | 0.010 | NPC |

Match rates are 0.3-1.4%, consistent with random coincidence at 1% tolerance.
No class shows meaningful alignment with Riemann zero spacings. No P/NPC
difference in match rates.

**Kill #8 VERDICT: CONFIRMED. No Riemann connection at n=10.**

---

## Comparison with Original

| Test | Original | Re-verification | Agreement |
|:-----|:---------|:---------------|:----------|
| V1 (entropy) | PASS (5.3%) | PASS (5.24%) | YES |
| V2 (spacing ratio) | PASS (NPC 0.804 > P 0.572) | FAIL (NPC 0.591 < P 0.653) | NO |
| Kill #6 (C_max) | KILL (no separation) | KILL (no separation) | YES |
| Kill #7 (Pade) | KILL (all saturate at 8) | KILL (structural argument) | YES |
| Kill #8 (Riemann) | KILL (0 matches) | KILL (~1% random rate) | YES |

**Key discrepancy: V2 does not reproduce.** The Lee-Yang spacing ratio is
statistically fragile at n=10 -- too few near-unit-circle zeros (especially
for Horn-SAT: only 11/50 instances valid). The original's V2 pass was a
seed-dependent fluctuation.

---

## Verdict

**Revised assessment: PARTIAL 1/5 (1 PASS, 3 KILL, 1 FRAGILE).**

- **Robust PASS:** V1 (violation spectrum entropy, 5.2% gap, reproduces)
- **Fragile, does not reproduce:** V2 (Lee-Yang spacing ratio)
- **Robust KILL:** Kill #6 (C_max), Kill #7 (Pade), Kill #8 (Riemann)

The original's "PARTIAL 2/5" should be downgraded to **PARTIAL 1/5**.
The single surviving signal -- violation spectrum entropy -- is genuine
and reproduced exactly (5.24% vs 5.3%). This is the only robust
complexity-class separator found in the O8 partition function analysis.

The violation spectrum entropy remains a clean, interpretable observable:
NPC problems at critical clause ratio have more uniformly distributed
violation counts, producing higher-entropy distributions. This is consistent
with the intuition that NPC energy landscapes are more "rugged" (many
competing local minima at diverse violation levels).

---

*G Six and Claude Opus 4.6. April 2026.*
