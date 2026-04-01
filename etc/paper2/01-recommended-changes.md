# Review: Cross-Document Consistency and Recommended Changes

**Reviewed:** 2026-04-01
**Documents:** Paper 1 abstract, Paper 1 Section 8, Appendix Y, Paper 2 (full)
**Reviewer context:** Full CAMB computation from `/age/` directory

---

## 1. The Critical Issue: ACT DR6 vs the 1/ξ² Baryogenesis Law

This is the single most important consistency problem across all documents.

### The conflict

| Source | ξ constraint | N_eff implied |
|--------|-------------|---------------|
| 1/ξ² baryogenesis law (Paper 2, App E) | **ξ = 0.432** | 3.31 |
| ACT DR6 at 2σ (App Y §Y.4.2) | ξ < 0.255 | < 3.12 |
| ACT DR6 at 3σ (App Y §Y.4.2) | ξ < 0.397 | < 3.25 |
| BBN 2025 at 2σ (App Y §Y.4.1) | ξ < 0.384 | < 3.18 |

The baryogenesis-derived ξ = 0.432 exceeds the ACT DR6 3σ bound (0.397)
and the BBN 2025 2σ bound (0.384). This is a **3.5-4σ tension** with
the latest CMB data.

### Where it's handled well

Appendix Y is admirably honest:
- §Y.5.2 presents a two-tier structure (ACT-safe vs BBN-limited)
- §Y.5.3 states "not a full resolution"
- §Y.9.3 notes extended parameter fits could loosen the bound by 30-50%
- §Y.9.5 lists explicit falsification conditions

### Where it's NOT handled

The Paper 1 abstract (lines 102-113) and Paper 2 abstract present the
ξ = 0.432 results (H₀ = 68.7, S8 = 0.785, t₀ = 13.47 Gyr) as the
definitive prediction without mentioning the ACT DR6 conflict. A reader
encountering these abstracts first would not know the central prediction
is in 3-4σ tension with the latest CMB measurement.

### Why this matters for credibility

The framework's greatest strength is its honesty about what works and
what doesn't. Every speculative claim in the paper is labeled. The
finiteness result has explicit caveats. The orbifold extensions are
flagged as speculative. Hiding the ACT DR6 tension from the abstracts
would break this pattern and undermine the paper's credibility with
exactly the audience (theoretical cosmologists) most likely to notice.

### Recommended fix

Add one sentence to each abstract acknowledging the tension and
pointing to CMB-S4 as the resolution. See §3 below for exact text.

---

## 2. Number Inconsistencies Across Documents

### The problem

The paper presents two legitimate scenarios (Scenario A: θ*-matched
at ξ = 0.47; Scenario B: 1/ξ² law at ξ = 0.432). But different
documents cite different scenarios' numbers without labeling which
scenario they're using, creating apparent contradictions.

### The inconsistency table

| Quantity | P1 Abstract | P1 §8.3.5 | App Y §Y.10 | P2 Abstract | P2 §8 |
|----------|------------|-----------|-------------|-------------|-------|
| ξ | 0.432-0.47 | 0.4375 | 0.432-0.47 | 0.432 | 0.47 |
| H₀ | 68.0-68.7 then 68.8 | 68.8 | 68.0-68.7 | 68.7 | 69.5 |
| t₀ | 13.60 | 13.60 | — | 13.47 | 13.47 |
| S8 | 0.754 | 0.754 | — | 0.785 | 0.753 |
| θ* offset | +1.0" | +1.0" | — | +6.6" or -0.5" | -0.5" |
| N_eff | — | — | 3.31 | 3.31 | 3.39 |

### Specific contradictions

**P1 Abstract lines 78-80 vs 104-108:**
Line 79 says H₀ ≈ 68.0-68.7 (App Y Tier 1/2 range, ACT-safe).
Line 107 says H₀ = 68.8 (self-consistent solution at ξ = 0.4375,
which is NOT ACT-safe). These are in the same abstract.

**P2 Abstract vs P2 Section 8:**
Abstract uses Scenario B numbers (ξ = 0.432, H₀ = 68.7, S8 = 0.785).
Section 8 table uses Scenario A numbers (H₀ = 69.5, S8 = 0.753).

**P1 §8.3.5 vs P2 Abstract:**
P1 §8.3.5 says t₀ = 13.60 Gyr and θ* = +1.0". This is the
self-consistent ω_b solution (ξ = 0.4375, ω_b = 0.02150).
P2 abstract says t₀ = 13.47 Gyr. This is Scenario B (ξ = 0.432,
standard ω_b = 0.02237).

### Recommended fix

Each document should clearly label which scenario it cites. The
recommended approach:

1. **P1 Abstract:** Use Appendix Y's Tier 1/2 range (conservative,
   ACT-safe) for the H₀ claim. Cite the Paper 2 summary in a separate
   paragraph that names both scenarios with their caveats.

2. **P1 §8.3.5:** Present both scenarios in a mini-table.

3. **P2 Abstract:** Lead with Scenario B (the 1/ξ² law — it's the
   central discovery), note the θ* tension, cite Scenario A as the
   cross-check.

4. **P2 §8:** Use a consistent table showing both scenarios side by side.

---

## 3. Recommended Text Changes

### 3.1 Paper 1 Abstract — lines 102-113

**Current text** (lines 102-113):
```
A companion computation (Paper 2) applies the CAMB Boltzmann solver to
the framework's cosmological sector. The bulk leptogenesis mechanism on
the Z₂ orbifold yields a scaling law Ω_DM/Ω_b = 1/ξ² that determines
the hidden-brane temperature ratio ξ = 0.432–0.47 from the observed
dark-to-visible matter ratio — removing the last free cosmological
parameter. The self-consistent solution (ξ = 0.4375) predicts t₀ = 13.60 Gyr,
H₀ = 68.8 km/s/Mpc, S8 = 0.754 (resolving the weak lensing tension), and
the CMB angular scale θ* within 1.0 arcsecond of Planck's measurement.
A framework built from pure geometry — one compact circle, one warp factor,
one temperature ratio — predicts the age of the universe, the Hubble
constant, the dark matter density, the matter clustering amplitude, and
the CMB angular scale from zero adjustable parameters.
```

**Replace with:**
```
A companion computation (Paper 2) applies the CAMB Boltzmann solver to
the framework's cosmological sector. The bulk leptogenesis mechanism on
the Z₂ orbifold yields a scaling law Ω_DM/Ω_b = 1/ξ² that determines
the hidden-brane temperature ratio ξ = 0.432 from the observed
dark-to-visible matter ratio — removing the last free cosmological
parameter. Two scenarios bracket the prediction: the 1/ξ² law gives
t₀ = 13.47 Gyr, H₀ = 68.7, S8 = 0.785 (θ* offset +6.6"); a
θ*-matched variant with adjusted ω_b gives t₀ = 13.60, H₀ = 68.8,
S8 = 0.754, θ* within 1.0". Both resolve the S8 weak lensing tension,
and the cosmic coincidence Ω_DM/Ω_b ≈ 5 is explained geometrically.
The required ξ ≈ 0.43 predicts N_eff = 3.31, in 3–4σ tension with
ACT DR6 (N_eff = 2.86 ± 0.13) — the framework's most significant
open issue, to be resolved definitively by CMB-S4 (σ(N_eff) ≈ 0.03).
```

### 3.2 Paper 1 Abstract — lines 78-80 (H₀ claim)

**Current text:**
```
the Hubble tension
(H₀ ≈ 68.0–68.7 km/s/Mpc from hidden-brane dark radiation, above ΛCDM
and toward the non-distance-ladder consensus; full resolution requires
physics beyond the minimal orbifold)
```

**Replace with:**
```
the Hubble tension
(H₀ ≈ 68.0–68.7 km/s/Mpc from hidden-brane dark radiation, above ΛCDM
and toward the non-distance-ladder consensus; constrained by ACT DR6
N_eff at the upper end; full resolution requires physics beyond the
minimal orbifold)
```

### 3.3 Paper 1 Section 8.3.5

**Current text** (lines 196-219):
Presents one set of numbers (t₀ = 13.60, H₀ = 68.8, etc.) without
scenario labeling or ACT DR6 context.

**Replace the number block (lines 206-211) with:**
```
    |                           | Scenario A (θ*-matched) | Scenario B (1/ξ² law) |
    |---------------------------|------------------------|-----------------------|
    | ξ                         | 0.470                  | 0.432                 |
    | t₀                        | 13.47 Gyr              | 13.47 Gyr             |
    | H₀                        | 69.5 km/s/Mpc          | 68.7 km/s/Mpc         |
    | S8                         | 0.753                  | 0.785                 |
    | θ* offset                  | −0.5"                  | +6.6"                 |
    | Ω_DM/Ω_b                  | 5.22 (input)           | 5.36 (derived)        |
    | N_eff                      | 3.39                   | 3.31                  |
    | ACT DR6 tension            | 4.1σ                   | 3.5σ                  |
```

And add after the table:
```
Both scenarios are in tension with ACT DR6's N_eff measurement
(2.86 ± 0.13); the tension ranges from 3.5σ (Scenario B) to 4.1σ
(Scenario A). This is the framework's most consequential open issue:
it predicts more dark radiation than current CMB data support. The
tension may be resolved if extended parameter fits (ΛCDM + N_eff + w₀
+ wₐ, which is the framework's actual model) loosen the N_eff bound,
or it may indicate that the mirror sector is colder than the
baryogenesis formula predicts. CMB-S4 (σ(N_eff) ≈ 0.03) will be
definitive.
```

### 3.4 Paper 2 Abstract

**Add after the θ* sentence (currently the second-to-last paragraph):**
```
The baryogenesis-derived ξ = 0.432 predicts N_eff = 3.31, in 3.5σ
tension with ACT DR6 (N_eff = 2.86 ± 0.13). This is the framework's
primary open issue. The ACT constraint assumes ΛCDM + N_eff; in the
framework's extended model (+ w₀ + wₐ), the bound loosens and the
tension may reduce to 2–3σ. CMB-S4 (σ(N_eff) ≈ 0.03) will resolve
this definitively. If confirmed, the mirror sector is real. If
excluded, the baryogenesis mechanism must be revised.
```

### 3.5 Paper 2 Section 8.2 (Conclusion table)

**Replace the single-column table with a two-scenario table:**
```
| Observable | Scenario A (θ*-matched) | Scenario B (1/ξ² law) | Status |
|-----------|------------------------|-----------------------|--------|
| t₀ | 13.47 Gyr | 13.47 Gyr | Both younger than ΛCDM |
| θ* | −0.5" from Planck | +6.6" from Planck | A matches; B has tension |
| S8 | 0.753 | 0.785 | Both resolve WL tension |
| H₀ | 69.5 | 68.7 | Both above ΛCDM |
| N_eff | 3.39 | 3.31 | Both in tension with ACT DR6 |
| Ω_DM/Ω_b | 5.22 | 5.36 | B matches observed |
```

### 3.6 Appendix Y — add self-consistent ω_b solution

**Add new section Y.5.4:**
```
### Y.5.4 The Self-Consistent ω_b Solution

The θ* tension between the 1/ξ² prediction and Planck's measurement
can be partially resolved by allowing ω_b h² to shift from its ΛCDM
value. In a non-ΛCDM cosmology with higher N_eff, the Planck data
yields a different ω_b (Planck 2018, Table 5: ω_b decreases by
1–3% when N_eff floats).

Imposing both θ* = 1.04110 AND Ω_DM/Ω_b = 5.36 simultaneously at
ξ = 0.4375, the self-consistent solution is:

    ω_b h² = 0.02150  (−3.9% from ΛCDM)
    ω_c h² = 0.11524
    θ* offset = +1.0"  (within Planck 1σ)
    t₀ = 13.60 Gyr
    S8 = 0.754

The ω_b shift is in the expected direction but creates a new tension:
the predicted primordial deuterium abundance D/H ≈ 2.65 × 10⁻⁵ is
1.5σ above the measurement (2.527 ± 0.030) × 10⁻⁵ (Cooke et al. 2018).
This is a mild tension, not a falsification. A proper MCMC fit to the
full Planck+ACT+DESI likelihood would determine whether this shift is
viable within the framework's extended parameter space.
```

### 3.7 Appendix Y — strengthen ACT DR6 vs 1/ξ² treatment

**Add new section Y.5.5 (or expand Y.4.3):**
```
### Y.5.5 The N_eff Tension: ACT DR6 vs the 1/ξ² Law

The 1/ξ² baryogenesis law (Paper 2, Appendix E) requires ξ = 0.432 to
match the observed Ω_DM/Ω_b = 5.36. This implies N_eff = 3.31, which
is 3.5σ above ACT DR6's measurement (2.86 ± 0.13).

This tension has three possible resolutions:

**(a) Extended parameter fits.** The ACT DR6 N_eff constraint assumes
ΛCDM + N_eff (a 7-parameter model). The framework predicts a different
model: ΛCDM + N_eff + w₀ + wₐ (a 9-parameter model). In extended
models, parameter degeneracies typically loosen the N_eff bound by
30–50%. A dedicated MCMC analysis of the framework's specific model
is needed to determine the actual constraint on ξ.

**(b) The baryogenesis formula has corrections.** The 1/ξ² scaling
assumes strong washout. In intermediate washout, the exponent shifts:
Ω_DM/Ω_b = 1/ξ^α with α ≠ 2. If α = 1.7 (plausible for K ~ 5),
then ξ = (5.36)^{-1/1.7} = 0.356, giving N_eff = 3.14 — within
2.2σ of ACT DR6 and consistent with BBN 2025.

**(c) The mirror sector is colder than expected.** If the gravitational
reheating mechanism gives ξ < 0.35 (which is physically reasonable),
the baryogenesis formula requires a compensating warp correction to
reach Ω_DM/Ω_b = 5.36. This shifts the problem from N_eff to the
bulk neutrino mass parameter c.

None of these is currently favored. CMB-S4 (σ(N_eff) ≈ 0.03) will
determine N_eff to the precision needed to distinguish all three.
```

---

## 4. Additional Improvements

### 4.1 Paper 2 Section 2.3 — add self-consistent ω_b scenario

Add a "Scenario C (self-consistent ω_b)" column to the CAMB
parameter table with ω_b h² = 0.02150, noting it resolves the θ*
tension at the cost of a 1.5σ D/H tension.

### 4.2 Paper 2 PROJECT-MASTER.md — update key numbers

The PROJECT-MASTER table (lines 73-97) should note which scenario
each number comes from. Currently it mixes scenarios without labels.

### 4.3 Appendix Y §Y.8.4 — update scorecard

Add a row for the N_eff / ACT DR6 tension:

```
| N_eff (mirror sector) | Mirror brane dark radiation | **3.5σ tension with ACT DR6** |
```

### 4.4 Appendix Y §Y.10 — flag the inconsistency

The summary table lists both constraints without noting they conflict.
Add a row or footnote:

```
| 1/ξ² law vs ACT DR6 | ξ = 0.432 required vs ξ < 0.397 allowed (3σ) | **3.5σ tension — primary open issue** |
```

---

## 5. What NOT to Change

The following are working well and should be preserved:

1. **Appendix Y's two-tier structure** — this is the right approach
2. **Appendix Y's honest caveats** (§Y.5.3, Y.7, Y.9.5)
3. **Paper 2's Scenario A/B bracketing** — correct strategy
4. **The 1/ξ² derivation itself** — this is a genuine result
5. **Paper 1 §8.4 (Closing)** — the shadow metaphor is perfect
6. **The DESI w(z) comparison** in both papers
7. **The S8 resolution** — this is the framework's strongest new result

---

## 6. Priority Order for Implementation

| # | Priority | Document | Change | Impact |
|---|----------|----------|--------|--------|
| 1 | **HIGH** | P1 Abstract lines 102-113 | Replace Paper 2 summary (§3.1) | Credibility |
| 2 | **HIGH** | P2 Abstract | Add ACT DR6 tension sentence (§3.4) | Credibility |
| 3 | **HIGH** | P1 Abstract lines 78-80 | Add ACT constraint note (§3.2) | Consistency |
| 4 | **HIGH** | P1 §8.3.5 | Add two-scenario table + ACT note (§3.3) | Consistency |
| 5 | **MED** | App Y | Add §Y.5.4 self-consistent ω_b (§3.6) | Completeness |
| 6 | **MED** | App Y | Add §Y.5.5 ACT vs 1/ξ² (§3.7) | Honesty |
| 7 | **MED** | P2 §8.2 | Two-scenario table (§3.5) | Consistency |
| 8 | **MED** | App Y §Y.10 | Flag N_eff tension in summary (§4.4) | Completeness |
| 9 | **LOW** | P2 §2.3 | Add Scenario C (§4.1) | Completeness |
| 10 | **LOW** | P2 PROJECT | Label scenario sources (§4.2) | Clarity |
| 11 | **LOW** | App Y §Y.8.4 | Add N_eff row to scorecard (§4.3) | Completeness |
