# Phase 3 — The ACT DR6 Tension: Detailed Analysis

## The problem stated precisely

The paper's H0 prediction rests on this chain:

    ξ (mirror temperature ratio)
      → ΔN_eff = 6.14 × ξ^4  (mirror dark radiation)
      → ΔH0 = 6.3 × ΔN_eff   (CMB degeneracy)
      → H0 = 67.4 + ΔH0 + 0.3 (tower)

The paper claims ξ = 0.45–0.50 is allowed by BBN, giving H0 = 69–70.

**ACT DR6 provides a DIRECT constraint on ΔN_eff at recombination**
that is tighter than BBN. The CMB "sees" all radiation at z ~ 1100,
regardless of whether it's on the visible brane, the hidden brane,
or in the bulk.


## Why the mirror sector maps directly to N_eff

Could the mirror radiation evade the N_eff constraint somehow?

**Question: Is the mirror sector free-streaming at recombination?**

Mirror recombination occurs at T_mirror ~ 0.3 eV (same physics as
visible recombination). Since T_mirror = ξ × T_visible, mirror
recombination happens at T_visible = 0.3/ξ eV:

    ξ = 0.50 → mirror recom at T_visible = 0.6 eV, z ~ 2500
    ξ = 0.45 → mirror recom at T_visible = 0.67 eV, z ~ 2800
    ξ = 0.30 → mirror recom at T_visible = 1.0 eV, z ~ 4200

**In all cases, mirror recombination occurs BEFORE visible
recombination (z ~ 1100).** At z = 1100, the mirror sector has
already recombined. Mirror photons are free-streaming.

Therefore: the mirror sector contributes to N_eff (free-streaming
radiation), not N_fluid (interacting radiation). The ACT DR6
constraint N_eff = 2.86 ± 0.13 applies directly.


## Quantitative impact

### ACT DR6 alone (N_eff = 2.86 ± 0.13):

Framework prediction: N_eff = 3.094 + 6.14 × ξ^4

| ξ   | ΔN_eff_mirror | N_eff_total | Tension with ACT DR6 |
|-----|---------------|-------------|---------------------|
| 0.25 | 0.024 | 3.12 | 2.0σ |
| 0.30 | 0.050 | 3.14 | 2.2σ |
| 0.35 | 0.092 | 3.19 | 2.5σ |
| 0.40 | 0.157 | 3.25 | 3.0σ |
| 0.45 | 0.252 | 3.35 | 3.8σ |
| 0.47 | 0.300 | 3.39 | 4.1σ |
| 0.50 | 0.384 | 3.48 | 4.8σ |

### ACT DR6 + He + D combined (N_eff = 2.89 ± 0.11):

| ξ   | N_eff_total | Tension |
|-----|-------------|---------|
| 0.25 | 3.12 | 2.1σ |
| 0.30 | 3.14 | 2.3σ |
| 0.35 | 3.19 | 2.7σ |
| 0.40 | 3.25 | 3.3σ |
| 0.45 | 3.35 | 4.2σ |
| 0.50 | 3.48 | 5.4σ |


## The allowed H0 range

At 2σ (95% CL) from ACT DR6 alone:
- N_eff < 3.12
- ΔN_eff_mirror < 0.026
- ξ < 0.255
- **ΔH0 < 0.16** → H0 < 67.9

At 3σ (99.7% CL):
- N_eff < 3.25
- ΔN_eff_mirror < 0.156
- ξ < 0.397
- **ΔH0 < 0.98** → H0 < 68.7


## The cascade does NOT help the mirror sector

The Gonzalo et al. (2024) cascade reduces the VISIBLE sector's ΔN_eff
by draining energy from active neutrinos → dark KK tower modes. Could
a mirror-sector cascade reduce the mirror's ΔN_eff?

**No, for a fundamental reason:**

The cascade reduces the visible ΔN_eff because it prevents KK tower
energy from entering the visible active neutrino bath. It moves energy
from observable → dark.

For the mirror sector, the cascade would move energy from mirror active
neutrinos → dark KK modes. But BOTH contribute to the expansion rate.
The CMB doesn't care whether the radiation is on the mirror brane or
in the bulk KK tower — it all gravitates. The cascade redistributes
energy within the dark sector, but the total dark radiation seen by
the CMB is unchanged.

**The mirror ΔN_eff = 6.14 × ξ^4 is a gravitational effect. The cascade
is an internal redistribution. The gravitational effect is invariant.**


## Possible escape routes (explored in 04-opportunities.md)

1. Parameter degeneracies in extended models (ΛCDM + N_eff + w0wa)
   could loosen the N_eff constraint
2. The mirror sector might not be a full SM copy (fewer d.o.f.)
3. The N_eff coefficient (6.3 km/s/Mpc per ΔN_eff) might be model-
   dependent
4. Reframe as a prediction for CMB-S4, acknowledging current tension
5. Accept H0 ≈ 68–69 as the honest prediction

## Assessment

The ACT DR6 N_eff constraint is the single biggest obstacle to the
paper's H0 = 69–70 prediction. The constraint is robust (free-streaming
mirror photons at recombination map directly to N_eff). The cascade
mechanism doesn't help (gravitational effect is invariant).

The paper must either revise the prediction downward or find a
creative mechanism within the framework that decouples the mirror
radiation from the standard N_eff signature.
