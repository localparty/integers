# Appendix H — JWST Early Galaxies: What the Framework Addresses

> JWST has discovered unexpectedly massive, mature galaxies at
> `z > 10`, challenging the available formation time in `ΛCDM`.
> The 5D framework does NOT significantly change the time available
> at `z > 10` (the high-z expansion rate is `H₀`-independent).
> However, the framework's dark sector physics — mirror dark matter
> structure formation, KK graviton cascade decays, and dark sector
> heating — may enable earlier galaxy formation within the same
> available time. This appendix characterizes both what the framework
> addresses and what it honestly cannot explain.

---

## H.1 The JWST Tension

JADES-GS-z14-0 (Carniani et al. 2024) is spectroscopically confirmed
at `z = 14.32`, with stellar mass `~10⁸ M_☉`. In `ΛCDM`, only 295 Myr
have elapsed since the Big Bang at `z = 14.3`. Forming a galaxy with
this mass in < 300 Myr requires extremely efficient star formation
(efficiency `ε ~ 0.2–0.5`, compared to typical `ε ~ 0.01–0.05`).

The `ΛCDM` challenge: how did galaxies become so massive so quickly?

---

## H.2 The Framework Cannot Add Time at `z > 10`

The CAMB computation confirms the analytic expectation from file
03-jwst-early-galaxies.md: the time available at high z is virtually
unchanged by the framework's cosmological modifications.

| Redshift | `t_5D` (Myr) | `t_ΛCDM` (Myr) | Difference |
|----------|-----------|--------------|------------|
| `z = 10` | 475 | 470 | +5 Myr |
| `z = 12` | 351 | 348 | +3 Myr |
| `z = 14` | 298 | 295 | +3 Myr |
| `z = 20` | 180 | 178 | +2 Myr |

**The reason:** At `z > 10`, the universe is radiation-dominated.
`H(z) ~ H₀ √(Ω_r) (1+z)²`. Since `Ω_r = ρ_r/ρ_crit ∝ 1/H₀²`, the
`H₀` dependence cancels. The physical radiation density (set by
`T_CMB = 2.725 K`) is the same in both cosmologies.

Extra radiation (`ΔN_eff = 0.35`) makes the high-z expansion FASTER
by ~1.7%, giving LESS time. This goes in the wrong direction.

**The framework does not help with the JWST early galaxy tension
through modified expansion history.**

---

## H.3 What the Framework MAY Address: Dark Sector Physics

Although the framework cannot add time at `z > 10`, it may enable
earlier galaxy formation through qualitatively different dark
sector physics.

### H.3.1 Mirror Dark Matter Structure Formation

Standard CDM is collisionless. Mirror dark matter is COLLISIONAL:
it interacts through mirror-sector gauge forces (mirror electromagnetism,
mirror strong force). On small scales, collisional dark matter:

- Has a finite dark Jeans length (pressure support against collapse)
  at high z, which suppresses small-scale halos
- BUT: the dark Jeans length decreases after dark recombination
  (`z_{mirror,rec} ~ 2500–4000`), after which mirror dark matter becomes
  as CDM-like on large scales

The key question: does the dark Jeans length effect suppress or
ENHANCE galaxy formation at `z > 10`?

**Possible enhancement:** If the dark Jeans length is tuned to be
~50–100 Mpc (comoving) — larger than the typical halo scale at
`z > 10` — then dark matter collapses on LARGER scales first (top-down
structure formation). This could seed massive collapsed objects
earlier, which then fragment into galaxies.

This is speculative and requires N-body simulations with the mirror
sector physics.

### H.3.2 Dark Photon Energy Injection

The kinetic mixing `ε ~ 5 × 10⁻⁴` (Paper 1, Appendix W) allows mirror
photons to convert to visible photons (and vice versa). At `z > 10`,
if the mirror sector has significant photon energy, a fraction `ε²` of
it is injected into the visible sector. This provides additional
photon heating of the intergalactic medium (IGM), potentially
affecting the `Lyman-α` forest and IGM thermal history — but the effect
is tiny (`ε² ~ 10⁻⁷`) and negligible for galaxy formation.

### H.3.3 KK Graviton Cascade Decays and Early Structure

The KK graviton cascade decays that resolve the `S8` tension (Appendix C)
impart kick velocities to dark matter. At `z > 10`, if the cascade
is ongoing (not complete), the warm dark matter imprint could seed
LARGER structures earlier — a top-down effect.

However, Obied et al. (2023) show the cascade is complete by `z ~ 10`,
so the kick velocities are set before galaxy formation begins.

---

## H.4 Honest Assessment

The 5D framework:
- Does NOT provide more time at `z > 10` ✗
- Does NOT have a mechanism to dramatically enhance star formation
  efficiency ✗ (not yet computed)
- MAY affect dark matter structure formation through collisional
  mirror DM physics — requires N-body simulations ○
- Is honest about this limitation, as with the Hubble tension

The JWST early galaxy tension remains an open problem. It is likely
an astrophysical challenge (star formation efficiency, feedback
models) rather than a cosmological one. The framework does not
add this problem to its solved list.

---

## H.5 Future Work

A dedicated N-body simulation with:
- Mirror dark matter (collisional, with dark Jeans length)
- KK graviton cascade decay kicks
- Dark sector heating/cooling

would determine whether the framework's dark sector physics
provides any advantage for early galaxy formation at `z > 10`.
This is identified as a priority for Paper 3.

---

## H.6 References

- Carniani, S. et al. "Spectroscopic confirmation of two luminous
  galaxies at z > 14." *Nature* **633**, 318 (2024). — JADES-GS-z14-0.
- Finkelstein, S. L. et al. "A long-duration gamma-ray burst at
  z ~ 14." *Astrophys. J. Lett.* **946**, L13 (2023).
- Obied, G. et al. "Dark Dimension and Decaying Dark Matter Gravitons."
  arXiv:2311.05318 (2023).
