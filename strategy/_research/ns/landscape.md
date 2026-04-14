# Landscape — Navier-Stokes Existence & Smoothness (paper30)

*Millennium target. Our strategy: 5D-geometric turbulence regularization; paper27/30.*

## Current Key Researchers

| Name | Institution | Approach / Contribution |
|------|-------------|------------------------|
| Terence Tao | UCLA | Supercriticality barrier; averaged NS blowup |
| Tristan Buckmaster | Princeton / NYU | Convex integration for NS non-uniqueness |
| Vlad Vicol | Courant | Convex integration; Onsager's conjecture; NS weak solutions |
| Camillo De Lellis | IAS | Convex integration original (Euler); Onsager |
| László Székelyhidi | Leipzig | Convex integration (with De Lellis) |
| Philip Isett | Caltech | Onsager 1/3 threshold theorem |
| Peter Constantin | Princeton | Geometric regularity criteria; NS mathematical theory |
| Ciprian Foias | TAMU (emeritus) | Global attractors; statistical NS |
| Edriss Titi | Cambridge | Euler/NS regularity; computational aspects |
| Luis Escauriaza | UPV/EHU | Critical-space regularity (ESS theorem) |
| Gregory Seregin | Oxford | Backward uniqueness; ESS theorem |
| Vladimír Šverák | Minnesota | ESS theorem; geometric methods |
| Herbert Koch | Bonn | Koch-Tataru well-posedness in BMO^{-1} |
| Daniel Tataru | Berkeley | Koch-Tataru; harmonic analysis |
| Thomas Y. Hou | Caltech | Computational approach; potential singularities |
| Tai-Peng Tsai | UBC | Critical space regularity |
| Laura Caravenna | Padova | Weak solutions |
| Maria Colombo | EPFL | Convex integration; non-uniqueness |
| Alexander Kiselev | Duke | Small-scale creation; Euler blowup |
| Charles Fefferman | Princeton | Clay problem statement author |
| Jean-Yves Chemin | Sorbonne | Harmonic analysis; Littlewood-Paley |
| Hideyuki Miura | Tokyo Tech | Critical space / Koch-Tataru methods |
| Gregory Eyink | Johns Hopkins | Onsager theory; turbulence |
| Roman Shvydkoy | UIC | Euler equations, Onsager |

## Major Approaches

### 1. Energy Methods / Leray-Hopf (Classical)
Leray (1934), Hopf (1951): global weak solutions exist. Uniqueness and smoothness are the key open questions in 3D. Kato's mild solution theory. All modern work builds on this foundation.

### 2. Critical-Space Regularity (ESS / Koch-Tataru)
Escauriaza–Seregin–Šverák (2003): L^∞_t L^3_x solutions are regular (blow-up requires norm in critical space to be unbounded). Koch–Tataru (2001): well-posed in BMO^{-1}. Refines: Tsai, Tao, others push regularity criteria in scaling-invariant spaces.

### 3. Convex Integration / Non-Uniqueness (De Lellis–Székelyhidi–Buckmaster–Vicol–Isett)
Adapt Nash's isometric embedding method to fluid dynamics. Buckmaster–Vicol (2019) proved non-uniqueness for *very weak* solutions of NS. Isett (2018) proved Onsager's 1/3 threshold for Euler. Does NOT address Leray-Hopf class. Reshapes the question: blowup in Leray-Hopf class ≠ non-uniqueness of very-weak solutions.

### 4. Supercriticality / Averaged Model (Tao)
Tao (2014, 2016) proved finite-time blowup for an *averaged* 3D NS equation, argued the "supercriticality barrier" is a real obstacle. Suggests any route must exploit some hidden criticality.

### 5. Geometric / Vortex Stretching (Constantin, Fefferman, Hou)
Control vorticity direction and magnitude. Constantin–Fefferman–Majda direction regularity criterion. Hou's computational/analytic programme looking for singularities in Euler.

### 6. Computational / Potential Blowup (Hou, Luo, Ricca, Moffatt)
Hou–Luo (2013): candidate Euler axisymmetric blowup in a domain. Self-similar and hyperbolic flow blow-up scenarios. Ongoing computational search.

### 7. Stochastic / Random NS (Flandoli, Mattingly, Hairer)
Noise regularizes: stochastic NS is well-posed under various noise types. Flandoli-Luo "noise prevents singularity" theorems. Statistical / stochastic analog of deterministic Clay problem.

### 8. Physics-Side Turbulence Theory (Kolmogorov, Onsager, Eyink)
K41 scaling; Onsager's dissipation anomaly; intermittency. Onsager's 1/3 threshold rigorously proved. Connection with anomalous dissipation.

### 9. Global-in-Time Strong Solutions for Small Data
Kato's 1984 existence of strong solutions in L^3 for small data; Chemin's Besov space results; various smallness-condition theorems.

## Partial Results / Named Milestones

- 1934 — Leray — global weak solutions (Leray-Hopf)
- 1951 — Hopf — Hopf solutions
- 1959-67 — Prodi–Serrin–Ladyzhenskaya — regularity criteria
- 1984 — Kato — small data strong solutions in L^3
- 1988 — Constantin–Foias — *Navier-Stokes Equations* (Chicago lectures)
- 2000 — Clay problem (Fefferman)
- 2001 — Koch–Tataru — well-posedness in BMO^{-1}
- 2003 — Escauriaza–Seregin–Šverák — L^∞_t L^3_x regularity (Leibniz condition, backward uniqueness)
- 2014 — Tao — averaged NS blowup
- 2019 — Buckmaster–Vicol — non-uniqueness of very-weak NS solutions
- 2017-18 — Isett; De Lellis–Székelyhidi — Onsager conjecture for Euler
- 2024 — Hilbert 6th problem: Deng–Hani–Ma claimed derivation (ongoing debate)

## Recent Preprints (2023-2026)

- arXiv:2503.01800 — Deng–Hani–Ma "Hilbert's sixth problem: derivation of fluid equations via Boltzmann's kinetic theory" (2025)
- arXiv:2504.06297 — Comment on Deng–Hani–Ma (critique)
- arXiv:2507.18063 — Existence of smooth solutions of NS (preprint; unverified)
- arXiv:2508.19590 — Global regularity of Leray-Hopf weak solutions (preprint; unverified)
- Convex integration results for NS (Colombo, Buckmaster, Vicol) ongoing

## Key Surveys / Textbooks

- Fefferman, "Existence and smoothness of the Navier-Stokes equation" (Clay official)
- Constantin–Foias, *Navier-Stokes Equations* (Chicago, 1988)
- Temam, *Navier-Stokes Equations: Theory and Numerical Analysis*
- Robinson–Rodrigo–Sadowski, *The Three-Dimensional Navier-Stokes Equations* (Cambridge)
- Lemarié-Rieusset, *Recent Developments in the Navier-Stokes Problem*
- Buckmaster–Vicol survey; De Lellis–Székelyhidi survey on convex integration
- Tao's blog posts on NS

## Acknowledgment Suggestions

### Top priority (credit in Introduction):
- **Terence Tao** — supercriticality barrier; programme-defining
- **Tristan Buckmaster & Vlad Vicol** — convex integration non-uniqueness; reshapes the question
- **Camillo De Lellis & László Székelyhidi** — convex integration origin; Onsager
- **Luis Escauriaza, Gregory Seregin, Vladimír Šverák** — ESS critical theorem
- **Peter Constantin & Ciprian Foias** — foundational modern framework

### Cite in body:
- Jean Leray, Eberhard Hopf — weak solutions
- Giovanni Prodi, James Serrin, Olga Ladyzhenskaya — regularity criteria
- Herbert Koch, Daniel Tataru — BMO^{-1} well-posedness
- Charles Fefferman — Clay problem statement
- Tosio Kato — small-data strong solutions
- Thomas Hou, Guo Luo — computational approach / potential blowup
- Philip Isett — Onsager 1/3 proof
- Gregory Eyink — turbulence theory / Onsager
- Franco Flandoli, Jonathan Mattingly, Martin Hairer — stochastic NS
- Deng–Hani–Ma — Hilbert 6 derivation
- Edriss Titi — Euler / NS regularity

### Our programme's position
Our QG5D route to NS is *indirect*: the fluid equations emerge from gradient-flow in a 5-dimensional geometric setting, with the regularity of the projected 3D flow controlled by the stability of the 5D evolution. This exchanges a supercritical 3D problem for a critical 5D one; the trade-off is (a) gives us control the classical approaches cannot reach, (b) makes the statement conditional on the 5D geometry programme itself. The approach is complementary to the Leray-Hopf/ESS programme (we still deploy ESS as an external lemma), orthogonal to convex integration (which lives at the "very weak" level we avoid), and deeply indebted to Onsager/Eyink for the turbulence picture that motivates our smoothing. We cite Tao's supercriticality barrier explicitly as the obstacle our geometric lift is designed to bypass.
