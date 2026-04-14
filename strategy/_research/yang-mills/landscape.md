# Landscape — Yang-Mills Existence & Mass Gap (paper08)

*Millennium target. Tier 4 (largest); our strategy is unconditional AF match via Balaban RG + gradient flow (see YM H4 bypass notebook).*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Arthur Jaffe | Harvard | Constructive QFT; official Clay problem statement (Jaffe–Witten) |
| Edward Witten | IAS | Physics formulation; official Clay problem statement |
| Sourav Chatterjee | Stanford | Probabilistic lattice YM; mass gap via Wilson loops, Higgs mechanism lectures |
| Tadeusz Bałaban | Rutgers | Multiscale RG analysis of lattice YM (foundational 80s-90s) |
| Paul Federbush | Michigan | RG methods for lattice gauge theory |
| Erhard Seiler | MPI Munich | Constructive gauge theory; Osterwalder–Seiler axioms |
| Jürg Fröhlich | ETH Zürich | Brydges–Fröhlich–Seiler gauge theory construction |
| David Brydges | UBC | Abelian gauge theory satisfying OS axioms |
| Ilia Chevyrev | Edinburgh | Dynamical lattice YM, area law |
| Hao Shen | Wisconsin | Stochastic quantization of gauge theory, SPDE methods |
| Scott Sheffield | MIT | Yang-Mills via probabilistic methods |
| Michael Douglas | Stony Brook / CMI | Program-level strategy (Clay-supported workshops) |
| Greg Anderson | — | Lattice constructive attempts |
| Abdelmalek Abdesselam | Virginia | Constructive field theory, phi^4, gauge |
| Massimiliano Gubinelli | Oxford | Stochastic methods for gauge theories |
| Antti Kupiainen | Helsinki | Constructive RG methods |
| Martin Hairer | EPFL | Regularity structures applied to gauge theories |

## Major Approaches

### 1. Constructive QFT via Lattice (Bałaban / Federbush / Magnen–Sénéor / Rivasseau)
The historical Clay-targeted programme. Discretize spacetime on a lattice, take continuum limit via multiscale RG, verify Osterwalder–Schrader axioms. Bałaban's multi-scale block-spin analysis controls the UV; in 3D pure YM Bałaban proved ultraviolet stability. The approach has a complete 2D result (Magnen–Sénéor) but no complete 4D non-abelian result — the mass gap and OS axioms in four dimensions remain open from this direction. Our programme uses Bałaban's RG as one external dependency (Tier 4 verification).

### 2. Stochastic Quantization / SPDE (Hairer / Shen / Chandra / Chevyrev / Kupiainen)
Use Langevin dynamics: view YM measure as stationary measure of a stochastic PDE. Exploit Hairer's regularity-structures machinery plus Da Prato–Debussche / paracontrolled calculus. Shen–Chandra–Chevyrev–Hairer have constructed 2D YM this way; 3D and 4D progressing. Advantage: yields a genuine QFT measure; disadvantage: gauge-invariant observables require careful handling.

### 3. Probabilistic / Gauge-Invariant Observables (Chatterjee)
Chatterjee has written a sequence of papers developing Wilson-loop-based probabilistic methods on the lattice. Yields area law in lattice 4D YM in strong coupling; studies mass gap through decay of connected correlations. Recent (2024) lecture series "Mass generation by the Higgs mechanism" presents a complete strategy for lattice Higgs mass gap.

### 4. Gribov–Zwanziger (Vandersickel / Sorella / Zwanziger)
Handle Gribov copies by restricting the path integral to the fundamental modular domain plus a horizon term. Recent 2024-2025 preprints claim mass-gap proofs via this route, reformulated in functional-analytic terms and using Borel-Écalle resurgence. Gives ∆ ≈ 0.5 GeV for SU(3) consistent with lattice.

### 5. Dynamical / Langevin Area Law (Shen–Chevyrev 2025)
Very recent: arXiv:2509.04688 establishes area law for lattice YM via a dynamical approach, with the mass gap condition directly yielding area law.

### 6. Physics-Side Lattice QCD (BMW / Hadron Spectrum / MILC / Fermilab Lattice)
Non-rigorous but precise: numerical lattice simulations have verified mass gap at the percent level for SU(3). BMW collaboration has hadron spectrum including isospin splittings. This is the empirical benchmark any constructive proof must match.

### 7. Higgs Mechanism / Chatterjee–Jafarov
Recent approach: prove the mass gap for lattice Higgs-gauge field theory at strong coupling, then relate to pure YM. 't Hooft regime U(N) lattice work (arXiv:2510.22788) provides unique infinite volume limit.

## Partial Results / Named Milestones

- 1978 — Osterwalder–Seiler — lattice gauge theories on infinite volume; axioms framework
- 1977-1987 — Bałaban — series of papers, multiscale RG for 3D YM, ultraviolet stability
- 1980s — Brydges–Fröhlich–Seiler — abelian Higgs model satisfies all OS axioms with mass gap (only complete interacting gauge theory example)
- 1980 — Magnen–Sénéor — complete construction of 2D Yang-Mills
- 2000 — Jaffe–Witten — official Clay problem statement
- 2020 — Chatterjee — proof of mass gap in lattice 4D YM in strong-coupling regime via explicit characters
- 2024 — Shen–Chevyrev et al. — dynamical lattice YM area law derived from mass gap
- 2025 — U(N) lattice YM mass gap and unique infinite volume limit in 't Hooft regime

## Recent Preprints (2023-2026)

- arXiv:2510.22788 — U(N) lattice Yang-Mills in the 't Hooft regime — mass gap + unique infinite volume limit
- arXiv:2509.04688 — Dynamical approach to area law for lattice Yang-Mills (Shen et al.)
- arXiv:2506.00284 — "A Constructive Proof of Existence and Mass Gap for Pure SU(3) Yang–Mills in Four-Dimensional Space-Time" (preprint; independent verification pending)
- Chatterjee (2024) — "Mass generation by the Higgs mechanism" lectures
- Springer 2025 (Mat. Contemp.) — "On the Mass Gap Problem for the Yang-Mills Model" — review

## Key Surveys / Textbooks

- Jaffe–Witten (2000) — official Clay problem description
- Glimm–Jaffe — *Quantum Physics: A Functional Integral Point of View* (2nd ed., Springer 1987)
- Seiler, *Gauge Theories as a Problem of Constructive Quantum Field Theory* (LNP 159, Springer 1982)
- Chatterjee, Sourav — "Yang-Mills for probabilists" (survey, 2019)
- nLab "Yang-Mills mass gap" entry

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Tadeusz Bałaban** — foundational multi-scale RG analysis; our strategy uses Bałaban's RG as external dependency for UV control
- **Erhard Seiler** — Osterwalder–Seiler framework that sets what "solution" means
- **Arthur Jaffe & Edward Witten** — official problem statement; Jaffe's constructive QFT programme
- **Sourav Chatterjee** — lattice mass-gap probabilistic methods; serves as parallel evidence path
- **Martin Hairer / Hao Shen / Ilia Chevyrev** — SPDE methods; complementary rigorous programme

### Cite in body:
- Brydges–Fröhlich–Seiler — only prior complete example of interacting gauge theory with mass gap
- Magnen–Sénéor — 2D YM construction
- Gribov–Zwanziger programme (Sorella, Vandersickel, Zwanziger)
- BMW / Hadron Spectrum lattice collaborations — empirical benchmark
- Federbush — companion of Bałaban on multi-scale methods
- Magnen, Rivasseau — constructive phi^4 and related RG

### Our programme's position
The QG5D ring approaches YM from an unusual direction: the mass gap is a *corollary of CBB (Connes–Bost–Baumslag) KMS-state structure at $\beta > 1$* combined with ORA-verified H4 bypass via Bałaban RG + gradient flow. We neither compete with nor supersede the constructive QFT programme; we import Bałaban's UV control and Shen-type gradient flow results as *external dependencies*, and our contribution is the bridge that turns those into an AF-match yielding the gap. Every direct attack on YM we know of — Chatterjee, Shen, Gubinelli, Hairer — is a *verification partner* whose results either corroborate ours or can be plugged in as Tier 4 lemmas.
