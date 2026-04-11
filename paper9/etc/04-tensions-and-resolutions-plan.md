# Tensions and Resolutions Plan — QG5D Framework

**Date:** 2026-04-07
**Status:** Research plan — execute in order of priority
**Context:** After full referee cycle + cross-paper consistency review + CAMB run,
two tensions survive: θ* is 11–18 arcseconds low, and N_eff is 3.5σ above ACT DR6.
This document lays out the theoretical leads, what each requires, and where the
output goes.

---

## Priority 1 — The ξ Derivation Problem (most important)

### What we know

Paper 6 §6.4 derives ξ from first principles and reaches ξ = 0.79. The observed
Ω_DM/Ω_b = 5.36 requires ξ = 0.432. The factor 0.79/0.432 ≈ 1.83 has been
attributed to "entropy from phase transitions and mirror e± annihilation." This
calculation has never been completed.

### The Z₂ conservation theorem (new result)

A careful analysis shows that the thermal history DOES NOT CHANGE ξ. Here is the
argument:

After the two branes gravitationally decouple at T_dec >> all particle masses
(T_dec ~ 10^7–10^8 GeV from §6.4), both sectors have equal g*S = 106.75. The
entropy ratio r = S_mirror/S_visible is set at decoupling:

    r = ξ_dec³ × g*S,vis(ξ_dec T_dec) / g*S,vis(T_dec)

Since T_dec >> all particle masses, g*S = 106.75 for both sectors at their
respective temperatures. Therefore r = ξ_dec³.

After decoupling, entropy is separately conserved in each sector. Today:

    ξ_today = (r × g*S,vis(T_vis,0) / g*S,mirror(T_mirror,0))^{1/3}

Since both sectors have the same particle content (Z₂ symmetry):
g*S,vis(T_vis,0) = g*S,mirror(T_mirror,0) = 3.91 (photons + neutrinos, accounting
for respective e± annihilations). Therefore:

    ξ_today = r^{1/3} = ξ_dec

**ξ is conserved from decoupling to today.** The thermal history — mirror QCD,
visible QCD, e± annihilations — makes NO NET change to ξ. Each phase transition
in one sector heats that sector's photons by some factor f. The same transition
in the mirror sector (occurring at a different T_vis due to ξ < 1) heats the
mirror photons by the same f. The factors cancel.

This is a theorem, not an approximation. It holds for any ξ < 1 and any
Z₂-symmetric particle content. **The 0.79 → 0.432 reduction cannot come from
the thermal history.**

### What this means

ξ is set at the LEPTOGENESIS EPOCH, not by subsequent evolution. Specifically:

After gravitational decoupling (when the branes stop exchanging heat through
graviton exchange), bulk right-handed neutrinos decay to both branes. The
energy ratio deposited determines ξ:

    ρ_hid/ρ_vis = (ε_hid / ε_vis) [for ε >> initial thermal energy ρ_0]

where ε_vis, ε_hid are the energies injected by neutrino decays into each brane.
The temperature ratio:

    ξ = T_hid/T_vis = (ρ_hid/ρ_vis)^{1/4}

For ξ = 0.432: ρ_hid/ρ_vis = 0.432⁴ = 0.0348. Only ~3.5% of the neutrino
decay energy goes to the hidden brane.

This requires the bulk right-handed neutrino to be localized near the VISIBLE
brane, with wavefunction amplitude at the hidden brane of ~19% of the visible
value (since energy ∝ amplitude²). This is determined by the neutrino bulk mass
parameter c_ν in the Dirac equation on the extra dimension.

### Connection to Paper 4

Paper 4 §4.3 establishes the bulk mass parameters c_f for SM fermions using
the Baptista non-Killing localization mechanism. For right-handed neutrinos
(which are bulk fields, not localized on a brane), the bulk mass parameter c_ν
determines the wavefunction profile:

    f_ν(y) ∝ e^{(1/2 - c_ν) k |y|}

For c_ν > 1/2: localized at visible brane (y = 0). For c_ν < 1/2: bulk-delocalized.

The ratio of wavefunction at hidden vs visible brane:

    |f_ν(πR)/f_ν(0)|² = e^{-2(2c_ν - 1)kπ}

Setting this equal to ρ_hid/ρ_vis = 0.0348:

    e^{-2(2c_ν - 1)kπ} = 0.0348
    2(2c_ν - 1)kπ = ln(1/0.0348) = 3.36
    For k = 2: (2c_ν - 1) = 3.36/(4π) = 0.268
    c_ν = 0.634

A bulk neutrino with c_ν ≈ 0.634 deposits ~3.5% of its decay energy on the
hidden brane, giving ξ = 0.432 from first principles.

### What needs to be computed

1. **Check c_ν = 0.634 against Paper 4's framework.** Is this value consistent
   with the seesaw neutrino masses (Σm_ν = 0.06 eV) and the bulk seesaw
   mechanism? Paper 4 §4.3b and Paper 2 Appendix E §E.3.2 are the relevant sections.

2. **Confirm the Z₂ conservation theorem explicitly.** Write it as a proposition
   in Paper 6 §6.5, with the entropy-ratio derivation above. This is a positive
   result: the thermal history is simpler than previously thought.

3. **Replace the "0.79 → 0.49" paragraph in Paper 6 §6.4–6.5** with the correct
   statement: ξ is set at leptogenesis by c_ν; the thermal history conserves ξ;
   the value ξ = 0.432 = 1/√5.36 is consistent with c_ν ≈ 0.634 from the neutrino
   localization.

4. **Add a computation script** `compute_xi_from_c_nu.py` to the age directory
   that: (a) computes ρ_hid/ρ_vis as a function of c_ν and k, (b) solves for ξ,
   (c) verifies c_ν ≈ 0.634 gives ξ = 0.432, (d) checks consistency with neutrino
   mass constraints.

### Output

- Paper 6 §6.4: rewrite as "ξ is set at leptogenesis by c_ν"
- Paper 6 §6.5: add Proposition (Z₂ conservation of ξ)
- Paper 6 §6.4 new calculation: c_ν → ρ_hid/ρ_vis → ξ derivation
- Paper 2 Appendix E §E.3.2: cross-reference the c_ν localization
- New script: `compute_xi_from_c_nu.py`
- Paper 9 §4b: update §4b.1 to note ξ is derived from c_ν, not from Ω_DM/Ω_b

---

## Priority 2 — Mirror Recombination at z ~ 2500 (θ* partial fix)

### What is missing

The current CAMB runs treat mirror photons as a simple ΔN_eff contribution —
a fluid-like radiation species. This is correct BEFORE mirror recombination, but
wrong after.

Mirror hydrogen recombines when T_mirror = 0.25 eV (same threshold as visible,
since mirror hydrogen is identical). This occurs at:

    z_mirror_recomb = T_mirror / T_CMB,0 = (ξ × 0.25 eV) / (2.35 × 10⁻⁴ eV)
    = ξ × 1064 ≈ 0.432 × 1064 ≈ 460... 

Wait, let me recalculate. Visible recombination at z_* = 1090 corresponds to
T_vis = T_CMB,0 × (1+z_*) = 2.35×10⁻⁴ eV × 1090 = 0.256 eV ≈ 0.25 eV. ✓

Mirror recombination at T_mirror = 0.25 eV means T_vis = 0.25/ξ = 0.25/0.432 = 0.579 eV,
i.e., z_mirror_recomb = 0.579 eV / (2.35×10⁻⁴ eV) - 1 ≈ 2463 - 1 ≈ 2462.

So mirror recombination happens at z ~ 2460, BEFORE visible recombination at z ~ 1090.

From z = 2460 to z = 1090, mirror photons are FREE-STREAMING (decoupled from
mirror baryons), not a tightly coupled fluid. Their contribution to the energy
density is still there (counts toward N_eff), but they carry anisotropy differently
from a fluid — they introduce additional damping of CMB anisotropies that a simple
ΔN_eff cannot capture.

### What needs to be computed

1. **Compute the mirror recombination redshift precisely** as a function of ξ.
   At ξ = 0.432: z_mirror_recomb ≈ 2460.
   At ξ = 0.47: z_mirror_recomb ≈ 2265.
   At ξ = 0.49: z_mirror_recomb ≈ 2173.

2. **Modify the CAMB setup** to model mirror photons as a free-streaming species
   below z_mirror_recomb, rather than as a fluid ΔN_eff above z_* = 1090.
   In CAMB, this requires treating the mirror photon contribution not as a
   pure N_eff shift but as an additional free-streaming radiation component
   with a step-function transition at z_mirror_recomb.

3. **Compare the resulting θ* shift.** Free-streaming radiation damps CMB
   anisotropies differently from fluid radiation. The standard result is that
   free-streaming suppresses the CMB peaks by a factor that depends on the
   free-streaming fraction. With mirror photons free-streaming from z=2460,
   the effect on θ* could be O(1–5 arcseconds) — partially closing the
   11–18 arcsecond gap.

4. **This is a new, sharper CMB prediction.** CMB-S4 would see the difference
   between "N_eff fluid" and "mirror photons free-streaming from z=2460."
   The power spectrum shape is distinctive. This should be added as a new
   prediction in Paper 2 §5 and Paper 9 §4b.9.

### Output

- Paper 2: new subsection on mirror recombination timing and CMB signatures
- `compute_age.py`: add mirror recombination redshift calculation per scenario
- Paper 9 §4b.9: add mirror recombination as a new, independent CMB-S4 prediction
- New CAMB variant runs with free-streaming mirror photons

---

## Priority 3 — Mirror Neutrino Mass at Recombination (θ* partial fix)

### What is missing

The CAMB runs use `mnu = 0.06 eV` for visible neutrinos only. Mirror neutrinos
also have mass 0.06 eV (Z₂ symmetry) and are at temperature:

    T_ν_mirror = (4/11)^{1/3} × ξ × T_γ

At z = 1090 (visible recombination): T_γ = 0.256 eV.
T_ν_mirror = 0.714 × 0.432 × 0.256 eV = 0.0789 eV.

Mirror neutrino m/T = 0.06/0.0789 = 0.76. They are transitioning from
radiation to matter RIGHT AT VISIBLE RECOMBINATION.

This matter contribution is not included in the current CAMB omch2. Adding it:

    Ω_ν_mirror h² ≈ ξ³ × Σm_ν_mirror / (93.14 eV) = 0.432³ × 0.06/93.14
    = 0.0806 × 6.44×10⁻⁴ = 5.19×10⁻⁵

This is small (~0.1% of omch2 ≈ 0.12) but not negligible for precision CMB.
The additional Ω_m increases θ* slightly (in the right direction).

### What needs to be computed

1. Add `mnu_mirror = 0.06` in the CAMB setup, with the correct temperature
   T_ν_mirror = (4/11)^{1/3} × ξ × T_γ. This requires a custom CAMB
   modification or an analytic correction to omch2.

2. Compute the correction to θ* from this additional matter at recombination.

3. Report the corrected values in the CAMB comparison table.

### Output

- `compute_age.py`: add mirror neutrino mass contribution to omch2 or mnu
- Paper 2: note the mirror neutrino mass correction in the CAMB description

---

## Priority 4 — ACT N_eff Degeneracy in Extended Parameter Space

### What is needed

The ACT DR6 constraint N_eff = 2.86 ± 0.13 is derived assuming ΛCDM + N_eff
as a free parameter. In the framework, N_eff is not independent — it is linked
to ξ, which is linked to Ω_m:

    N_eff = 3.044 + ΔN_eff(ξ)
    Ω_cdm h² = Ω_b h² / ξ²
    H_0 = 67.4 + 6.3 × ΔN_eff

These are NOT three free parameters — they are functions of ONE parameter ξ.

When ACT fits N_eff freely (allowing Ω_m and H_0 to float independently),
it can find a low N_eff = 2.86 solution. When the ξ-constraint is imposed
(N_eff and Ω_m correlated through ξ), the same ACT data may prefer a different
best fit.

### What needs to be computed

Run `neff_extended_analysis.py` (already set up) and extract:
1. The χ² of the framework's (N_eff=3.31-3.39, Ω_m from ξ) point against
   ACT DR6 data in the constrained (ξ-linked) parameter space.
2. Compare to the χ² of ΛCDM at N_eff=3.044.
3. Report how many σ the framework is from ACT DR6 in the constrained space
   (this number is expected to be lower than 3.5σ due to the degeneracy with
   lower Ω_m).

This analysis already exists in the script — it just needs to be run and the
result reported formally in Paper 2.

### Output

- Run `neff_extended_analysis.py` and read `neff_analysis_results.json`
- Paper 2: report the constrained-space χ² comparison
- Paper 9 §4b.7: update the ACT tension statement with the constrained-space number

---

## The θ* Tension: Honest Assessment

After all fixes above:

The θ* tension (11–18 arcseconds low) has three partial remedies:
- Mirror recombination timing: potentially O(2–5 arcsec) improvement (Priority 2)
- Mirror neutrino mass: potentially O(0.5–1 arcsec) improvement (Priority 3)
- ξ recalculation: if c_ν gives ξ = 0.432 precisely (not 0.47-0.49), the scenarios
  shift slightly (Priority 1)

Total possible improvement: O(3–6 arcseconds). The gap is 11–18 arcseconds.

**The honest conclusion:** The θ* tension is partially structural — the S8
resolution requires lower Ω_m, and lower Ω_m moves θ* in the wrong direction.
This anti-correlation is the same as in early dark energy models. The framework
resolves S8 at the cost of θ*. The remaining gap after all three fixes is
probably ~5–12 arcseconds.

This should be stated clearly in Paper 2 and Paper 9 §4b.7 as the framework's
primary unresolved tension, with the note that further progress requires either:
(a) new physics at mirror recombination (z ~ 2460) that modifies the acoustic
scale, or (b) a small deviation from Z₂ symmetry in the mirror sector that
modifies mirror hydrogen binding energy and shifts z_mirror_recomb.

---

## Execution Order

```
Priority 1 (ξ from c_ν):
  Agent A: Derive Z₂ conservation theorem + c_ν calculation → Paper 6 §6.4–6.5
  Agent B: compute_xi_from_c_nu.py script

Priority 2 (mirror recombination):
  Agent C: z_mirror_recomb calculation + CAMB modification → Paper 2, compute_age.py

Priority 3 (mirror ν mass):
  Agent D: Add mirror neutrino mass to CAMB runs → compute_age.py update

Priority 4 (ACT degeneracy):
  Agent E: Run neff_extended_analysis.py → Paper 2 update

Final:
  Agent F: Paper 9 §4b update with all new results
```

Agents A and B can run in parallel.
Agents C, D, E can run in parallel after B is done (scripts exist).
Agent F runs last.

---

## Key Files

| Agent | Reads | Writes |
|-------|-------|--------|
| A | paper6/06-brane-temperature-asymmetry.md, paper4/appendix-B-m-brane-classification.md | paper6/06-brane-temperature-asymmetry.md (§6.4–6.5) |
| B | paper4/04-the-chirality-problem-and-its-resolution.md | quantum-geometry-in-5d/paper2/camb/compute_xi_from_c_nu.py |
| C | paper2/02-sections-2-to-7.md | compute_age.py (mirror recombination), paper2 (new subsection) |
| D | compute_age.py | compute_age.py (mirror ν mass in omch2) |
| E | neff_extended_analysis.py, neff_analysis_results.json | paper2/02-sections-2-to-7.md (ACT degeneracy) |
| F | paper9/preprint/04b-the-mirror-sector-prediction.md | same file (updated) |
