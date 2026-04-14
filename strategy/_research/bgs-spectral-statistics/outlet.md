# Bohigas-Giannoni-Schmit (BGS) Conjecture — Outlet Report

## 1. Official outlet

- **Wikipedia:** https://en.wikipedia.org/wiki/BGS_conjecture
- **Scholarpedia:** http://www.scholarpedia.org/article/Bohigas-Giannoni-Schmit_conjecture (Ullmo)
- **Original paper:** Bohigas, O., Giannoni, M.-J., Schmit, C. (1984). "Characterization of chaotic quantum spectra and universality of level fluctuation laws." *Physical Review Letters* 52, 1–4.
- **Companion:** Bohigas, Giannoni, Schmit (1984). *J. Physique Lettres* 45, L-1015–L-1022.

## 2. Problem statement

**BGS conjecture (1984, verbatim from PRL 52, 1–4):**

> "Spectra of time-reversal-invariant systems whose classical analogs are K systems show the same fluctuation properties as predicted by GOE."

Generalized form (all symmetry classes):

> The spectral fluctuations of a quantum system whose classical limit is fully chaotic (i.e., ergodic and mixing, a K-system) are described by the appropriate random-matrix ensemble determined by the system's symmetry class:
> - **GOE** (Gaussian Orthogonal Ensemble) — time-reversal invariant, integer spin;
> - **GUE** (Gaussian Unitary Ensemble) — time-reversal broken;
> - **GSE** (Gaussian Symplectic Ensemble) — time-reversal invariant, half-integer spin with no rotational symmetry.

Statement in terms of level spacing distribution: the normalized nearest-neighbor spacing statistics P(s) of chaotic quantum systems follow the Wigner-Dyson distribution of the corresponding RMT ensemble.

## 3. Prize

**None.** Purely physics/mathematical-physics research conjecture. No monetary prize.

## 4. Publication expectation

Expected journals in descending prestige:

- **Physical Review Letters (PRL)** — the original home of BGS; high-profile physics breakthroughs.
- **Communications in Mathematical Physics (CMP)** — mathematical proofs of semiclassical periodic orbit sum results (Müller et al. published here).
- **Annals of Mathematics** — for deep rigorous results.
- **Inventiones Mathematicae**
- **Journal of Statistical Physics**
- **Nonlinearity**
- **Physical Review E / X**
- **Journal of Physics A: Mathematical and Theoretical**
- **Nuclear Physics B**
- **Advances in Mathematics**

Specialty venues:
- *Chaos* (AIP)
- *Journal of Mathematical Physics*
- *Random Matrices: Theory and Applications*
- *Probability Theory and Related Fields*

## 5. Formulation variants

- **BGS (standard, 1984):** GOE/GUE/GSE correspondence.
- **Berry's semiclassical derivation (1985):** argues BGS from periodic orbit theory (Gutzwiller trace formula) + diagonal approximation.
- **Sieber-Richter extension (2001):** pair of orbits and their partners explains the τ² term in form factor.
- **Müller-Heusler-Braun-Haake-Altland-Kuipers (2004–2009):** full semiclassical derivation of random matrix form factor via pseudo-orbit expansions.
- **GSE-ful generalization:** symplectic with half-integer spin.
- **Open system (non-Hermitian):** Ginibre ensembles conjectured for open quantum chaos.
- **Many-body BGS:** ETH (Eigenstate Thermalization Hypothesis) connected to BGS.
- **Localization departures:** disordered systems exhibit Poisson or intermediate statistics.
- **Arithmetic chaos counterexample (Bogomolny-Schmit-Luo-Sarnak):** arithmetic quantum maps show Poisson (NOT GUE) — the "arithmetic counterexample" to strict BGS.
- **Number-theoretic analog:** Montgomery pair correlation of Riemann zeros ≡ GUE (Montgomery-Odlyzko law).

## 6. Known partial results + named walls

**Proven:**
- **Diagonal approximation (Berry, 1985):** semiclassical form factor K(τ) ≈ τ for small τ agrees with RMT — the first non-trivial term.
- **Off-diagonal τ² (Sieber-Richter 2001):** encounter pairs explain the next correction.
- **All orders of τ for uniformly hyperbolic chaotic systems (Müller-Heusler-Braun-Haake et al., 2004–2009):** full semiclassical derivation of GOE/GUE/GSE form factor.
- **Numerical verification:** overwhelming numerical support across billiards, quantum kicked tops, many-body chaotic Hamiltonians.

**Known counterexamples / refinements:**
- **Arithmetic Laplacian (Sarnak, Bogomolny-Leboeuf-Schmit):** modular-surface Laplacian eigenvalues show Poisson statistics (despite classical chaos) due to number-theoretic degeneracies — "arithmetic chaos exception."
- **Integrable limit:** integrable systems show Poisson statistics (Berry-Tabor conjecture).

**Named walls:**
- *Semiclassical limit wall* — BGS is an asymptotic/semiclassical statement; finite-ħ corrections always exist.
- *Uniform hyperbolicity wall* — all proofs (Müller et al.) assume uniform hyperbolicity; extension to mixed/KAM phase-space systems is open.
- *Arithmetic counterexample wall* — number theory breaks BGS in special cases; understanding the precise conditions remains open.
- *Long-time wall* — BGS is about spectral correlations; long-time dynamics of individual eigenstates (quantum unique ergodicity, proven for arithmetic surfaces by Lindenstrauss) is distinct but related.

## 7. Key references

**Original:**
- Bohigas, O., Giannoni, M.-J., Schmit, C. (1984). "Characterization of chaotic quantum spectra and universality of level fluctuation laws." *PRL* 52, 1–4.

**Best modern surveys:**
- Haake, F. (2010). *Quantum Signatures of Chaos* (3rd ed.). Springer. — canonical.
- Stöckmann, H.-J. (1999). *Quantum Chaos: An Introduction*. Cambridge.
- Mehta, M. L. (2004). *Random Matrices* (3rd ed.). Academic Press.
- Berry, M. V. (1985). "Semiclassical theory of spectral rigidity." *Proc. Roy. Soc. A* 400, 229–251.
- Müller, S., Heusler, S., Altland, A., Braun, P., Haake, F. (2009). "Periodic-orbit theory of universal level correlations in quantum chaos." *New J. Physics* 11, 103025.

**Arithmetic counter-signal:**
- Bogomolny, E., Leboeuf, P., Schmit, C. (1995). *Nonlinearity*.
- Luo, W. & Sarnak, P. (1994). "Number variance for arithmetic hyperbolic surfaces." *CMP* 161, 419–432.

## Status: OPEN (rigorous full proof); semiclassical case "essentially proven" via periodic orbit theory. No prize. Target journal: CMP / PRL / Annals.
