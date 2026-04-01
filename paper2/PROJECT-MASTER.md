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

## Two Scenarios (bracket the truth)

| Parameter | Scenario A (θ* matched) | Scenario B (1/ξ² law) |
|-----------|------------------------|----------------------|
| ξ | 0.470 | **0.432** |
| ω_c h² | 0.117 | 0.1199 |
| H₀ | 69.5 | **68.7** |
| t₀ | 13.47 Gyr | **13.47 Gyr** |
| θ* offset | −0.5" | +6.6" |
| S8 | 0.753 | **0.785** |
| Ω_DM/Ω_b | 5.22 (input) | **5.36 (derived)** |

## Key Numbers (all from CAMB v1.6.6)

| Parameter | Scenario A | Scenario B | Source appendix |
|-----------|-----------|-----------|----------------|
| t₀ | 13.47 Gyr | 13.47 Gyr | A |
| H₀ | 69.5 km/s/Mpc | 68.7 km/s/Mpc | A |
| θ* offset | −0.5" | +6.6" | G |
| S8 | 0.753 | 0.785 | C |
| σ₈ | 0.766 | 0.782 | C |
| Ω_m | 0.290 | 0.302 | A |
| r_d | 146.2 Mpc | 145.8 Mpc | D |
| N_eff | 3.39 | 3.31 | A |
| w₀ | −0.85 | −0.85 | F |
| w_a | −0.23 | −0.23 | F |
| ω_c h² | 0.117 | 0.1199 | A/E |
| Ω_DM/Ω_b | 5.22 | **5.36** | E |
| ξ | 0.470 | **0.432** | E |
| 1/ξ² law | — | ✓ derived | E |

---

## Tensions Addressed

| Tension | ΛCDM status | 5D Framework |
|---------|------------|-------------|
| S8 | 4σ | RESOLVED: S8 = 0.753 |
| Hubble (TRGB) | 3.3σ | ADDRESSED: H₀ = 69.5 |
| DESI w ≠ −1 | 4.2σ | EXPLAINED: thawing dilaton |
| Cosmic coincidence | No explanation | EXPLAINED: η_ratio × ξ³ |
| Strong CP | Fine-tuning | RESOLVED (Paper 1, App. X) |
| Neutrino masses | Unknown | PREDICTED: Σm_ν = 0.06 eV |

---

## Open Problems (for Paper 3)

1. Mirror baryogenesis precise calculation (η_ratio from first principles)
2. N-body simulations with mirror dark matter
3. JWST early galaxy formation with dark sector physics
4. Non-abelian extension SU(2)×SU(3) (Paper 1, Appendix L)
5. Scheme independence of the finiteness result (Paper 1, Appendix S §S.7)

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
