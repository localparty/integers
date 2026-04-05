# Paper 2 — Project Master

**Title:** The 5D e-Dimension Framework II: Precision Cosmology from Geometry

**Status:** DRAFT — ready for LaTeX conversion after Paper 1 arXiv submission

**Relationship to Paper 1:**
Paper 1 establishes the framework and its 22 phenomena/10 predictions.
Paper 2 presents the full numerical cosmological computation using CAMB,
the age prediction, S8 resolution, cosmic coincidence explanation, and
the complete experimental roadmap.

---

## File Structure

```
paper2/
├── abstract.md                        ← Full abstract
├── paper2-section-1-introduction.md   ← Introduction + organization
├── paper2-section-8-conclusion.md     ← Conclusion
├── appendices/
│   ├── appendix-A-age-computation.md          ← THE age: 13.470 Gyr
│   ├── appendix-B-expansion-history.md        ← H(z) fingerprint, DESI
│   ├── appendix-C-s8-tension.md               ← S8 = 0.753, resolved
│   ├── appendix-D-sound-horizon.md             ← r_d = 146.2 Mpc
│   ├── appendix-E-mirror-baryogenesis.md       ← Cosmic coincidence
│   ├── appendix-F-thawing-dilaton.md           ← w(z) trajectory
│   ├── appendix-G-cmb-angular-scale.md         ← θ* = 0.59640°
│   ├── appendix-H-jwst-galaxies.md             ← Honest: no help at z>10
│   └── appendix-I-decisive-tests.md            ← Roadmap to 2035
├── etc/
│   ├── refs.bib                       ← Bibliography
│   ├── camb-scripts.md                ← CAMB computation documentation
│   └── latex-instructions.md         ← LaTeX conversion guide
└── PROJECT-MASTER.md                  ← This file
```

---

## Source Data (from age/ directory)

| File | Used in |
|------|---------|
| age/08-CAMB-results.md | Appendices A, B, C, D |
| age/09-definitive-prediction.md | Appendices A, E, G |
| age/02-dilaton-dynamics.md | Appendix F |
| age/03-jwst-early-galaxies.md | Appendix H |
| age/plot_summary.png | Section 1 or Appendix A |
| age/plot_ages.png | Appendix A |
| age/plot_s8.png | Appendix C |
| age/plot_Hz.png | Appendix B |
| age/plot_wz.png | Appendix F |

---

## The Central Discovery

**Ω_DM / Ω_b = 1/ξ²** (from temperature-asymmetric bulk leptogenesis)

This removes ξ as a free parameter:

    ξ = 1/√(Ω_DM/Ω_b) = 1/√5.36 = 0.432

From ξ = 0.432, everything follows.

## Three Scenarios (bracket the truth)

| Parameter | Scenario A (θ*-matched) | Scenario B (1/ξ² law) | Scenario C (self-consistent ω_b) |
|-----------|------------------------|-----------------------|----------------------------------|
| ξ | 0.470 | **0.432** | 0.4375 |
| ω_b h² | 0.02237 (Planck) | 0.02237 (Planck) | **0.02150** (−3.9%) |
| ω_c h² | 0.117 | 0.1199 | 0.11524 |
| H₀ | 69.5 | **68.7** | 68.8 |
| t₀ | 13.47 Gyr | **13.47 Gyr** | 13.60 Gyr |
| θ* offset | −0.5" | +6.6" | **+1.0"** |
| S8 | 0.753 | 0.785 | **0.754** |
| Ω_DM/Ω_b | 5.22 (input) | **5.36 (derived)** | **5.36 (derived)** |
| D/H tension | — | — | 1.5σ |
| ACT DR6 tension | 4.1σ | 3.5σ | 3.6σ |

**Scenario A:** ξ set to match θ* with Planck ω_b; Ω_DM/Ω_b input.
**Scenario B:** ξ from 1/ξ² law; θ* has 6.6" residual; zero free parameters.
**Scenario C:** ξ from θ* crossing; ω_b self-consistent; both θ* AND Ω_DM/Ω_b matched.
**All scenarios** are in 3–4σ tension with ACT DR6 (N_eff = 2.86 ± 0.13).

## Key Numbers (all from CAMB v1.6.6)

| Parameter | Scenario A | Scenario B | Scenario C | Source appendix |
|-----------|-----------|-----------|-----------|----------------|
| t₀ | 13.47 Gyr | 13.47 Gyr | 13.60 Gyr | A |
| H₀ | 69.5 km/s/Mpc | 68.7 km/s/Mpc | 68.8 km/s/Mpc | A |
| θ* offset | −0.5" | +6.6" | +1.0" | G |
| S8 | 0.753 | 0.785 | 0.754 | C |
| σ₈ | 0.766 | 0.782 | 0.754 | C |
| Ω_m | 0.290 | 0.302 | 0.290 | A |
| r_d | 146.2 Mpc | 145.8 Mpc | 146.6 Mpc | D |
| N_eff | 3.39 | 3.31 | 3.32 | A |
| w₀ | −1 | −1 | −1 | F (revised: Casimir exact, Paper 6 §2) |
| w_a | 0 | 0 | 0 | F (revised: no GW term, c₂ = 0) |
| ω_b h² | 0.02237 | 0.02237 | 0.02150 | E |
| ω_c h² | 0.117 | 0.1199 | 0.11524 | A/E |
| Ω_DM/Ω_b | 5.22 | **5.36** | **5.36** | E |
| ξ | 0.470 | **0.432** | 0.4375 | E |
| 1/ξ² law | — | ✓ derived | ✓ (with ω_b fit) | E |

---

## Tensions Addressed

| Tension | ΛCDM status | 5D Framework |
|---------|------------|-------------|
| S8 | 4σ | RESOLVED: S8 = 0.753–0.785 (all scenarios) |
| Hubble (TRGB) | 3.3σ | ADDRESSED: H₀ = 68.7–69.5 (scenario-dependent) |
| DESI w ≠ −1 | 4.2σ | EXPLAINED: thawing dilaton |
| Cosmic coincidence | No explanation | EXPLAINED: Ω_DM/Ω_b = 1/ξ² |
| Strong CP | Fine-tuning | RESOLVED (Paper 1, App. X) |
| Neutrino masses | Unknown | PREDICTED: Σm_ν = 0.06 eV |
| **N_eff vs ACT DR6** | **—** | **3–4σ TENSION: all scenarios predict N_eff > 3.31** |

---

## Open Problems (for Paper 3)

1. **ACT DR6 N_eff tension** — MCMC with full framework model (ΛCDM + N_eff + w₀ + wₐ);
   intermediate-washout correction to 1/ξ² law (see App Y §Y.5.5)
2. Mirror baryogenesis precise calculation (washout exponent α from Boltzmann equations)
3. N-body simulations with mirror dark matter
4. JWST early galaxy formation with dark sector physics
5. Non-abelian extension SU(2)×SU(3) (Paper 1, Appendix L)
6. Scheme independence of the finiteness result (Paper 1, Appendix S §S.7)

---

## Citation of Paper 1

All references to the framework's foundation cite:
[Paper 1]: "The 5D e-Dimension Framework: Quantum Mechanics and Quantum
Gravity from a Compact Circle." arXiv:XXXX.XXXXX [hep-th] (2026).

---

## Target Journal

Physical Review Letters (Letter format) — same as Paper 1.

If the full computation warrants a longer treatment, consider
Physical Review D for Paper 2.
