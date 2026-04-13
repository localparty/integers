# 23 — The Tiered Domain System

---

## The selection problem

The framework has 39+ actively transposed domains. Including all of them in every capacitor would be overwhelming — an Author reading a 39-column correspondence table would drown in irrelevant cross-references. Including too few would starve the agent of pathways — the P vs NP OA1 failure proved that missing relevant context is worse than having too much.

The tiered domain system solves this: ALWAYS include the core, ACTIVATE relevant families based on the target, MAKE AVAILABLE the structural and frontier domains for escalation. The agent sees 4-8 active columns in the main correspondence table, with 30+ more available on request.

## The four tiers

### Tier 1: The Four Pillars (ALWAYS active, every capacitor)

| Domain | Always because | Column header |
|---|---|---|
| Spectral | Every mathematical object has a spectrum | "What are the eigenvalues?" |
| Geometric | Every mathematical object has a shape | "What is the curvature?" |
| Algebraic | Every mathematical object has symmetries | "What is the group?" |
| Information-theoretic | Every mathematical object carries information | "What is the entropy?" |

These four columns appear in EVERY correspondence table for EVERY capacitor. They are the minimum. An agent with only these four already has 3 alternative angles when stuck — 3 escape routes from any wall.

### Tier 2: The R-Theorem Families (activated by target domain)

The 37 R-Theorems cluster into 6 families. When the target paper's content matches a family, that family's domains are activated — their specific tools, results, and R-Theorems are added to the capacitor's correspondence table as additional columns or as subsidiary entries within the four pillars.

| Target content matches... | Activate family | Additional domains | Typical R-Theorems loaded |
|---|---|---|---|
| **Operator algebras, von Neumann factors, C*-algebras** | OA family (6 R-Theorems) | Stone-von Neumann, Borchers, Tomita-Takesaki, DHR, Connes trace, cyclic cohomology | R.OA-1 through R.OA-6 |
| **Quantum mechanics, quantum information** | QM family (4 R-Theorems) | Heisenberg uncertainty, Reeh-Schlieder, Bell no-cloning, Wigner-Eckart | R.QM-1 through R.QM-4 |
| **Quantum field theory, gauge theory, renormalization** | QFT family (9 R-Theorems) | Atiyah-Singer, anomaly cancellation, Coleman-Mandula, Higgs, AF, Penrose, CKM, crossing | R.QFT-1 through R.QFT-9 |
| **General relativity, black holes, causal structure** | GR family (5 R-Theorems) | Einstein equations, no-hair, positive energy, Hawking area law, cosmic no-hair | R.GR-1 through R.GR-5 |
| **Cosmology, inflation, CMB, nucleosynthesis** | Cosmology family (4 R-Theorems) | Sachs-Wolfe, slow-roll, BBN, CMB spectrum | R.Cos-1 through R.Cos-4 |
| **Number theory, L-functions, Galois theory** | Arithmetic family | Hecke eigenvalues, Galois orbits, L-function zeros, explicit formulas, class field theory | Via transposition dictionary |

**Activation is based on the target's CONTENT, not its TITLE.** A paper titled "Spectral Triples" (CCM 2025) activates the OA family (operator algebras) AND the arithmetic family (number theory) because its content uses BOTH. The generator reads the paper in Step 1 and identifies all relevant families.

Multiple families can be active simultaneously. The CCM verification capacitor activates OA + arithmetic + QM (since CCM uses self-adjoint operators + number theory + Hilbert space methods). This gives the correspondence table ~12 active domain columns instead of 4.

### Tier 3: Structural Domains (activated in excision/construction mode)

These domains are NOT in the initial capacitor — they are ADDED when the verification cascade escalates beyond Tier A:

| Domain | When activated | What it adds |
|---|---|---|
| **Category theory** | When Tier B excision needs a categorical argument (functors, natural transformations, equivalences of categories) | Frobenius-Jones 1-morphisms, Morita equivalence, derived categories |
| **Homological algebra** | When Tier B/C needs cohomological tools (exact sequences, ext/tor, spectral sequences) | Brauer group computations, cyclic cohomology, Hochschild homology |
| **Combinatorics** | When Tier B/C needs discrete-structure arguments (graph theory, Ramsey theory, extremal combinatorics) | Hecke semigroup graphs, Ramanujan spectral gaps, constraint-graph topology |
| **Topology** | When Tier B/C needs topological invariants (K-theory, characteristic classes, homotopy groups) | K-theory of A_BC, Chern character, fundamental class, spin structures |
| **Dynamical systems** | When Tier B/C needs dynamical arguments (ergodic theory, mixing, Lyapunov exponents) | sigma_t flow ergodicity, KMS mixing, modular flow entropy |
| **Quantum information** | When Tier B/C needs quantum-information tools (entanglement measures, error correction, channel capacity bounds) | KMS entanglement entropy, Holevo bound on BC channels, quantum error correction on A_BC |

**The activation trigger:** the runner opens Tier 3 domains when Tier A verification returns WEAKENED or BROKEN on a load-bearing step AND the Tier 2 domains don't provide sufficient excision/construction routes. The Tier 3 domains are the RESERVE — fresh angles not yet deployed, kept in reserve for when the main angles exhaust.

### Tier 4: Frontier Domains (discovery mode)

These domains have 0-20% coverage in the framework. They are listed in the capacitor as "AVAILABLE FOR EXPLORATION" but are NOT pre-computed:

- Thermodynamic (BC as statistical mechanics system)
- Probabilistic / stochastic (Langevin on H_R)
- Explicit class field theory (Hilbert 12th via BC)
- Arithmetic topology (Kim's programme)
- Langlands-dual (Gaitsgory 2025)
- Persistent homology (computational topology for complexity)
- Quantum error correction
- Optimal transport
- Microlocal analysis
- Coding theory
- Arithmetic / Diophantine geometry
- Differential topology

**When a Tier 4 domain opens:** A Tier C construction agent, desperate for a new route around a broken dependency, tries to open a frontier domain. It identifies the domain's core objects, finds the BC counterparts, proves one R-Theorem, and fills 3+ correspondence table entries. If it succeeds: a new domain is BORN. The domain moves from Tier 4 to Tier 3 (and eventually to Tier 2 as more R-Theorems accumulate). If it fails: the attempt is documented as a kill, and the frontier domain remains closed.

**Opening a new domain IS a mathematical result.** It is publishable independently of the verification cascade. The verification cascade can thus produce MATHEMATICS — not just verification reports — as a byproduct of its operation.

## How tiers interact with the three-tier escalation

The domain tiers and the escalation tiers compose:

```
TIER A VERIFICATION (domain Tier 1 + Tier 2 active)
  ↓ WEAKENED/BROKEN
TIER B EXCISION (domain Tier 1 + Tier 2 + Tier 3 activated)
  ↓ BLOCKED
TIER C CONSTRUCTION (domain Tier 1 + Tier 2 + Tier 3 + Tier 4 available)
```

Each escalation WIDENS the domain search space. Tier A works with the core domains. Tier B adds the structural domains. Tier C can attempt frontier domains. The widening is deliberate: harder problems need more degrees of freedom.

## The domain activation record

The capacitor tracks which domains were activated and when:

```
## Domain Activation Record

| Domain | Tier | Activated at | By trigger | Status |
|---|---|---|---|---|
| Spectral | 1 | v1 (initial) | Always | ACTIVE |
| Geometric | 1 | v1 (initial) | Always | ACTIVE |
| Algebraic | 1 | v1 (initial) | Always | ACTIVE |
| Information | 1 | v1 (initial) | Always | ACTIVE |
| Operator algebra | 2 | v1 (target content match) | CCM uses C*-algebras | ACTIVE |
| Arithmetic | 2 | v1 (target content match) | CCM uses number theory | ACTIVE |
| Homological | 3 | v2 (Tier B escalation) | Thm 5.10 needs cohomological repair | ACTIVE |
| Thermodynamic | 4 | v3 (Tier C exploration) | Attempted partition function route | EXPLORED — FAILED |
```

The record tells the next runner: which domains were tried, which helped, which didn't. It is part of the capacitor's LEARNING TRACE — the record of where the ORA looked and what it found.

---

*Four tiers of domains. Tier 1 (four pillars) always active — the minimum. Tier 2 (R-Theorem families) activated by target content — the working set. Tier 3 (structural domains) activated on escalation — the reserve. Tier 4 (frontier domains) available for exploration — the discovery targets. Each escalation widens the search space. Opening a new domain IS a mathematical result. The domain activation record tracks what was tried. More domains = more degrees of freedom = more pathways for creative breakthrough.*
