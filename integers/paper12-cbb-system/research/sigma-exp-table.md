# sigma-exp-table — Per-observable 1σ experimental uncertainties

*Bootstrap file created by the convergence prompt (Phase 1.5),
round 2, 2026-04-09. Updated round 3 (2026-04-09) for 1:1 row
alignment with research/23 and `formula_source` column. Updated
round 4 (2026-04-09): `corrected` tag renamed `laurent-shifted`
(pointing to research/154, NOT tautological research/167), and
`open-formula` tag added as a first-class category for one-sided
bounds / unpinned formulas. Future rounds update in place.*

**Sources keyed as:** PDG24 = PDG 2024; P18 = Planck 2018 VI (A&A 641
A6); NF52 = NuFit 5.2 (2024); FLAG22 = FLAG Review 2022; AOS15 = Aver
Olive Skillman 2015 JCAP 07 011; P2 = Paper 2 central value.

**formula_source column:**
- `raw` — single-zero γ_n placeholder in research/23
- `laurent-shifted` — raw formula with research/154's two-term Laurent
  (a, b) = (−γ_E(1+γ_E), γ_E²+ζ(2)−2π·γ_1) numerically applied. This
  is the *numerical* correction channel, NOT research/167's operator
  dictionary (which is a tautological rewrite at 50 dps).
- `geometric` — moduli-fitted via research/171/175/178
- `interface` — spectral-moduli mixing via research/183
- `open-formula` — one-sided bound, upper limit, or unpinned
  framework formula. Agent B reports as "≤Nσ" or "open"; no entry
  in the main σ-tally.

Rows marked `raw` whose value is empirically stale (m_Z, v) are flagged
`raw+stale` and Agent B reports their σ under a bookkeeping-gap
column, NOT in the main <N-σ tally.

**Row count:** exactly 36 rows, 1:1 with the research/23 master list
(sectors A=9, B=3, C=12, C-aux=3, D-CKM=6, D-PMNS=3).

Auxiliary/companion rows (Δm² ratio, E-sector derived, CC hierarchy,
α_PS⁻¹=17 integer) live in `sigma-exp-table-companion.md`.

| # | Sector | Observable | Central | σ_exp | Source | formula_source | last_updated |
|---:|:---|:---|:---|:---|:---|:---|:---|
| 1 | A | log(πR_obs/ℓ_P) | 69.7421709 | 1e-6 (derived) | CODATA | raw | 2026-04-09 |
| 2 | A | N_eff | 3.35 | 0.17 | P18 | raw | 2026-04-09 |
| 3 | A | n_s | 0.9649 | 0.0042 | P18 | raw | 2026-04-09 |
| 4 | A | H_0 [km/s/Mpc] | 67.4 | 0.5 | P18 | raw | 2026-04-09 |
| 5 | A | t_0 [Gyr] | 13.787 | 0.020 | P18 | raw | 2026-04-09 |
| 6 | A | Y_p | 0.245 | 0.003 | AOS15 | raw | 2026-04-09 |
| 7 | A | η_10 | 6.14 | 0.04 | P18 | raw | 2026-04-09 |
| 8 | A | ξ | 0.43 | 0.02 | P2 | raw | 2026-04-09 |
| 9 | A | v [GeV] | 246.22 | 0.04 | PDG24 | raw+stale | 2026-04-09 |
| 10 | B | 1/α(0) | 137.035999 | 1e-7 | PDG24 (CODATA) | raw | 2026-04-09 |
| 11 | B | 1/α_2(M_Z) | 29.5967 | 0.0030 | PDG24 | raw | 2026-04-09 |
| 12 | B | 1/α_3(M_Z) | 8.475 | 0.038 | PDG24/FLAG22 | raw | 2026-04-09 |
| 13 | C | m_τ [MeV] | 1776.86 | 0.12 | PDG24 | raw | 2026-04-09 |
| 14 | C | m_μ [MeV] | 105.6583755 | 2.3e-6 | PDG24 | raw | 2026-04-09 |
| 15 | C | m_t [GeV] | 172.69 | 0.30 | PDG24 | raw | 2026-04-09 |
| 16 | C | m_b [GeV] | 4.183 | 0.007 | FLAG22 | raw | 2026-04-09 |
| 17 | C | m_c [GeV] | 1.2730 | 0.0046 | FLAG22 | raw | 2026-04-09 |
| 18 | C | m_s [MeV] | 93.4 | 0.86 | FLAG22 | raw | 2026-04-09 |
| 19 | C | m_d [MeV] | 4.67 | 0.07 | FLAG22 | raw | 2026-04-09 |
| 20 | C | m_u [MeV] | 2.16 | 0.07 | FLAG22 | raw | 2026-04-09 |
| 21 | C | m_H [GeV] | 125.25 | 0.17 | PDG24 | raw | 2026-04-09 |
| 22 | C | m_Z [GeV] | 91.1876 | 0.0021 | PDG24 | raw+stale | 2026-04-09 |
| 23 | C | m_W [GeV] | 80.3692 | 0.0133 | PDG24 | raw | 2026-04-09 |
| 24 | C | Σm_ν [eV] (UB) | <0.12 | TBD (1-sided) | P18+DESI | open-formula | 2026-04-09 |
| 25 | C-aux | m_τ/m_μ | 16.8171 | 2.3e-5 | derived PDG24 | raw | 2026-04-09 |
| 26 | C-aux | m_t/m_W | 2.1488 | 0.0040 | derived PDG24 | raw | 2026-04-09 |
| 27 | C-aux | m_W/m_Z | 0.88147 | 0.00015 | derived PDG24 | raw | 2026-04-09 |
| 28 | D-CKM | sin θ_12 (Cabibbo) | 0.22500 | 0.00067 | PDG24 | raw | 2026-04-09 |
| 29 | D-CKM | sin θ_23 CKM | 0.04182 | 0.00085 | PDG24 | raw | 2026-04-09 |
| 30 | D-CKM | sin θ_13 CKM | 0.00369 | 0.00011 | PDG24 | open-formula | 2026-04-09 |
| 31 | D-CKM | δ_CP CKM [rad] | 1.196 | 0.023 | PDG24 | raw | 2026-04-09 |
| 32 | D-CKM | J_CKM (×10^5) | 3.18 | 0.15 | PDG24 | raw | 2026-04-09 |
| 33 | D-CKM | V_us/V_cb | 5.46 | 0.10 | PDG24 | raw | 2026-04-09 |
| 34 | D-PMNS | sin²(2θ_12) PMNS | 0.851 | 0.020 | NF52 | raw | 2026-04-09 |
| 35 | D-PMNS | sin²(2θ_13) PMNS | 0.0920 | 0.0007 | NF52 | raw | 2026-04-09 |
| 36 | D-PMNS | sin²(2θ_23) PMNS | 0.999 | 0.017 | NF52 | open-formula | 2026-04-09 |

**Count:** exactly 36 rows, aligned 1:1 with research/23.

Notes.
- Σm_ν is a one-sided upper bound; Agent B reports separately from
  the Gaussian σ-tally.
- δ_CP PMNS is multimodal in NuFit 5.2 and is therefore NOT in the
  36-row master slice; it is tracked in the companion file.
- `formula_source = laurent-shifted` means the row's prediction is
  obtained by numerically evaluating research/154's (a, b) Laurent
  coefficients into the raw formula. No row is yet tagged
  `laurent-shifted` because research/154's (a, b) have not been ported
  into a concrete numerical substitution — m_Z (row 22) and v (row 9)
  remain `raw+stale` awaiting that port. This flag has now been open
  for 3 consecutive rounds (1, 2, 3) and is escalated in round 4's
  Phase 4 headline per the prompt's escalation rule.
- `sin θ_13 CKM`, `sin²(2θ_23) PMNS`, and `Σm_ν` (upper bound) carry
  `formula_source = open-formula`. Agent B reports them under an
  `open-formula` category with `≤Nσ` or `open`, never in the main
  σ-tally or the tension bucket.
