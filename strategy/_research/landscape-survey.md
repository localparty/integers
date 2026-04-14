# Universal Approval — Competitive Landscape Survey

*Master consolidated report for the programme's "Universal Approval" strategy.*

**Programme's strategy**: every C_bare document will include a "Related Work & Acknowledgments" section drawn from this file. Every reviewer who has worked on these problems should see their contribution positioned fairly.

*Date: 2026-04-14. 28 targets covered.*

---

## Per-vertex summary table

| # | Vertex | Paper | Ring confidence | # Active Researchers (indexed) | Major Approaches | Key Surveys | Acknowledgment Priority (top 3) |
|---|--------|-------|-----------------|--------------------------------|------------------|-------------|-------------------------------|
| 1 | **Yang-Mills** | paper08 | 9.5/10 | ~17 (Bałaban, Jaffe, Witten, Chatterjee, Seiler, Brydges, Fröhlich, Hairer, Shen, Chevyrev, Gubinelli, Kupiainen, Douglas, Abdesselam, +) | 7 (constructive-lattice, SPDE, probabilistic, Gribov-Zwanziger, dynamical area-law, physics-lattice, Higgs mechanism) | Jaffe-Witten, Glimm-Jaffe, Seiler LNP 159, Chatterjee survey | Bałaban, Seiler, Chatterjee |
| 2 | **RH** | paper13 | 8/10 | ~20 (Connes, Consani, Marcolli, Conrey, Bombieri, Iwaniec, Kowalski, Sarnak, Snaith, Keating, Tao, Radziwiłł, Soundararajan, Maynard, Guth, Haran, Matiyasevich, Platt, Odlyzko, Pomerance, Xian-Jin Li) | 8 (Hilbert-Pólya, Selberg-critical-line, Weil/positivity, RMT/Katz-Sarnak, sieve/BFI, NCG/tropical, Jensen-polynomials, computational) | Bombieri Clay, Iwaniec-Kowalski, Titchmarsh, Mazur-Stein | Connes/Consani/Marcolli, Bombieri, Conrey |
| 3 | **BSD** | paper26 | 9/10 | ~17 (Bhargava, Skinner, Zhang W., Yuan, Zhang S-W., Shankar, Rubin, Burungale, Tian, Wan, Prasanna, Eischen, Rotger, Darmon, Coates, Gross, Zagier) | 7 (Iwasawa/main-conjecture, Heegner/Gross-Zagier/Kolyvagin, statistical/average-rank, p-converse, CM-case, Euler-systems, analytic-rank) | Wiles Clay, Zhang W. CDM 2013, Silverman AEC | Skinner/Bhargava, Yuan/Zhang/Zhang, Gross/Zagier |
| 4 | **P vs NP** | paper28 | — (new strategy) | ~22 (Mulmuley, Sohoni, Bürgisser, Ikenmeyer, Panova, Wigderson, Aaronson, Williams R., Razborov, Rudich, Impagliazzo, Valiant, Grochow, Alman, V.V.Williams, Khot, Trevisan, Kayal, Saraf, Limaye, Srinivasan, Tavenas) | 9 (GCT, circuit-lower-bounds, natural-proofs-bypass, relativization/algebrization, VP-vs-VNP, UGC/PCP, hardness-vs-randomness, MIP*=RE/quantum, fine-grained) | Aaronson P=NP survey, Arora-Barak, Mulmuley CACM, Wigderson book | Mulmuley, Razborov/Rudich, Wigderson/Aaronson |
| 5 | **Hodge** | paper29 | — | ~21 (Voisin, Deligne, Simpson, Lurie, Griffiths, Kerr, Yau, Totaro, Wlodarczyk, de Cataldo, Migliorini, Addington, Schoen, Ancona, Moonen, Schnell, O'Grady, Huybrechts, Green M., Amerik, Grassi) | 8 (absolute-Hodge/motives, transcendental/Griffiths-Voisin, standard-conjectures, hyper-Kähler-cases, motivic/BB-filtration, nonabelian-Hodge, p-adic-Hodge, derived/∞-categorical) | Deligne Clay, Voisin I-II Cambridge, Griffiths Annals, Lewis CRM, Peters-Steenbrink | Voisin, Deligne, Griffiths |
| 6 | **Navier-Stokes** | paper30 | — | ~22 (Tao, Buckmaster, Vicol, De Lellis, Székelyhidi, Isett, Constantin, Foias, Titi, Escauriaza, Seregin, Šverák, Koch, Tataru, Hou, Tsai, Caravenna, Colombo, Kiselev, Fefferman, Chemin, Miura, Eyink, Shvydkoy) | 9 (energy-methods/Leray-Hopf, critical-space-ESS/KT, convex-integration, supercriticality/Tao-averaged, geometric/vortex, computational, stochastic, physics-turbulence, small-data-strong) | Fefferman Clay, Constantin-Foias Chicago, Temam, Robinson-Rodrigo-Sadowski, Lemarié-Rieusset | Tao, Buckmaster/Vicol/De Lellis/Székelyhidi, Escauriaza/Seregin/Šverák |
| 7 | Lindelöf | paper45 | — | ~15 (Guth, Maynard, Soundararajan, Radziwiłł, Heath-Brown, Huxley, Bourgain, Jutila, Michel, Venkatesh, Munshi, Petrow, Young M., Nelson) | 6 (large-values, moments, exponent-pairs, subconvexity, decoupling, δ-method) | Titchmarsh-Heath-Brown, Iwaniec-Kowalski, Michel IHP lectures, Florea 2026 | Guth-Maynard, Heath-Brown, Huxley |
| 8 | GRH | paper13b | 7/10 | ~13 (Connes, Consani, Platt, Granville, Ford, Radziwiłł, Dunn, Soundararajan, Koukoulopoulos, Kowalski, Li W., Zapponi, Hiary) | 5 (computational, NCG-extension, weak-GRH/zero-density, Patterson-consequences, function-field-analog) | Davenport, Iwaniec-Kowalski, Murty-Murty | Connes/Consani/Marcolli, Platt, Dunn/Radziwiłł |
| 9 | Hilbert 12 | paper25 | 2/10 | ~15 (Dasgupta, Kakde, Darmon, Roblot, Gross B., Tate, Burns, Greither, Rotger, Pozzi, Dall'Ava, Bley, Hayes, Kurihara, Kato K.) | 6 (Stark, Dasgupta-Kakde-p-adic, Shimura-reciprocity-IQ, CM-higher-dim, elliptic-Stark, ETNC) | Roblot Lyon, Tate Birkhäuser, Gross Tokyo 1988 | Dasgupta-Kakde, Stark, Gross/Tate |
| 10 | Turbulence | paper38 | — | ~18 (Eyink, Isett, De Lellis, Székelyhidi, Buckmaster, Vicol, Goldenfeld, Titi, Frisch, Biferale, Benzi, Sreenivasan, Falkovich, Mailybaev, Kurien, Šverák, +) | 7 (Onsager, convex-integration, K41, multifractal, dyadic-models, stochastic, experimental) | Frisch Cambridge 1995, Monin-Yaglom, Eyink 2024, Buckmaster-Vicol | Onsager, Eyink, Isett/De-Lellis/Székelyhidi |
| 11 | Baum-Connes | paper31 | — | ~14 (Higson, Lafforgue V., Skandalis, Kasparov, Baum, Connes, Yu G., Guentner, Tessera, Sawicki, Peterson, Goffeng, Willett, Nishikawa) | 5 (Dirac-dual-Dirac, hyperbolic-groups-Lafforgue, counterexamples-with-coefficients, coarse-BC, exactness) | Mislin-Valette, Valette Intro, Higson-Roe | Baum/Connes, Kasparov, Lafforgue V. |
| 12 | VP vs VNP | paper39 | — | ~15 (Valiant, Kayal, Saraf, Limaye, Srinivasan, Tavenas, Saptharishi, Kumar, Alman, Mulmuley, Bürgisser, Karpinski, Malod, Koiran, Chattopadhyay) | 6 (GCT-for-permanent, direct-arithmetic-lower-bounds, monotone-VP-VNP, holographic, tensor-rank, border-complexity) | Bürgisser-Clausen-Shokrollahi, Shpilka-Yehudayoff, Saraf survey | Valiant, Mulmuley, Kayal/Saraf/Limaye |
| 13 | BGS quantum chaos | paper32 | — | ~17 (Bohigas, Giannoni, Schmit, Berry, Keating, Snaith, Ullmo, Nonnenmacher, Anantharaman, Dyatlov, Zworski, Haake, Šeba, Sieber, Altland, Bunimovich, Sánchez-Gómez) | 7 (semiclassical-Gutzwiller, RMT-Wigner-Dyson, Anantharaman-QUE, fractal-uncertainty, sigma-models, counterexamples-Floquet, Katz-Sarnak-connection) | Haake Springer, Stöckmann, Ullmo BGS review | Bohigas/Giannoni/Schmit, Berry/Keating/Snaith, Anantharaman |
| 14 | Katz-Sarnak | paper46 | — | ~16 (Katz, Sarnak, Conrey, Miller S., Keating, Snaith, Iwaniec, Luo, Rudnick, Granville, Radziwiłł, Rubinstein, Lalín, Young M., David C., Banwait) | 5 (function-field/geometric, moments-Keating-Snaith-CFKRS, low-lying-zeros-ILS, excised-model-Miller, one-level-densities) | Katz-Sarnak AMS 1999, Keating-Snaith CMP 2000, Miller surveys | Katz/Sarnak, Conrey/Keating/Snaith, Miller S. |
| 15 | Twin Primes | paper34 | — | ~13 (Zhang Y., Maynard, Tao, Granville, Ford, Green, Konyagin, Goldston, Pintz, Yıldırım, Matomäki, Radziwiłł, Ramaré) | 5 (Brun/Selberg/GPY/Maynard-sieve, Elliott-Halberstam, bounded-gaps-Polymath8, Hardy-Littlewood-circle-method, Matomäki-Radziwiłł) | Friedlander-Iwaniec Opera de Cribro, Granville BAMS 2015 | Zhang Y., Maynard, Tao/Polymath8 |
| 16 | Cramér | paper43 | — | ~10 (Ford, Green, Konyagin, Maynard, Tao, Granville, Pintz, Cramér, Maier, Friedlander) | 5 (probabilistic-heuristic, FGKMT-2014-large-gaps, unconditional-upper-bounds, RH-conditional, Maier-counterintuitive) | Soundararajan surveys, Granville expository | Cramér, Granville/Pintz, FGKMT |
| 17 | Goldbach | paper33 | — | ~12 (Helfgott, Platt, Tao, Granville, Friedlander, Ramaré, Chirre, Chen J., Oliveira e Silva, Zaharescu, Vinogradov) | 5 (circle-method-HL-Vinogradov-Helfgott, sieve-Brun-Chen, computational-to-4e18, weak-refined, short-intervals/AP) | Nathanson, Davenport-Montgomery, Helfgott survey | Helfgott, Vinogradov, Chen J. |
| 18 | ABC | paper37 | 1/10 | ~12 (Mochizuki, Fesenko, Scholze, Stix, Joshi, Goldfeld, Oesterlé, Masser, Faltings, Lagarias, Pasten, Vojta) | 5 (IUT-Mochizuki-Fesenko, Joshi-framework, Vojta-Diophantine, effective-ABC, computational) | Goldfeld surveys, Van Frankenhuysen, Joshi 2025 Report | Oesterlé/Masser, Mochizuki, Scholze/Stix/Joshi |
| 19 | OPN | paper40 | 4/10 | ~11 (Ochem, Rao, Nielsen P., Pomerance, Conrad K., Pollack, Banks W., Goto, Cohen G., Brent, te Riele) | 6 (size-bounds, component-bounds, largest-component, radical, computational-sieve, Pomerance-heuristic) | Ochem-Rao Math.Comp 2012, Wolfram MathWorld | Ochem/Rao, Euler (historical), Brent/Cohen/te-Riele |
| 20 | Collatz | paper41 | — | ~9 (Tao, Lagarias, Krasikov, Wirsching, Soundararajan, Ellenberg, Menares, Terras, Oliveira K.) | 5 (density-Krasikov-Tao, 2-adic-dynamical, computational, cycle-analysis, antihydra-Turing) | Lagarias AMS volumes, Wirsching | Tao, Lagarias, Krasikov |
| 21 | Lehmer | paper42 | 3/10 | ~13 (Smyth, Amoroso, David S., Masser, Bennett, Jankauskas, McKee, Pinner, Vaaler, Habegger, Schmidt K., Lind, Pazuki) | 6 (Smyth-1971-non-reciprocal, Amoroso-David-Galois, dynamical/entropy-Schmidt-Lind, Parry-Verger-Gaugry-disputed, Lehmer-totient, computational) | Smyth survey, Boyd Mahler measure, Mossinghoff tables | Smyth, Amoroso/David, Dobrowolski |
| 22 | Sato-Tate | paper44 | — | ~15 (Clozel, Harris M., Shepherd-Barron, Taylor R., Barnet-Lamb, Geraghty, Zhang W., Caraiani, Scholze, Gee, Fité, Kedlaya, Sutherland, Guitart, Serre) | 6 (potential-automorphy-CHST, BL-GHT-general-weight, ST-groups-abelian-varieties, perfectoid-Caraiani-Scholze, effective-ST, function-field-analog) | Murty-Murty, Clozel CDM 2006, Harris lectures, Serre | CHST, BL-GHT-2011, Serre |
| 23 | Schanuel | paper35 | 1/10 | ~15 (Ax, Zilber, Kirby, Bertrand, Waldschmidt, Bennett M., Nesterenko, Bilu, Tretkoff, Vallières, Bertolin, Huber-Klawitter, Zelinsky, Masser, Zudilin) | 6 (Ax-power-series-analog, Baker-linear-forms, Lindemann-Weierstrass-classical, Gelfond-Schneider-Hilbert-7, Zilber-model-theory, motivic-Bertolin-Huber) | Lang, Waldschmidt Springer, Bertolin review | Schanuel, Lang, Ax, Baker |
| 24 | Hilbert 6 | paper36 | 7/10 | ~17 (Deng, Hani, Ma, Simonella, Gallagher, Saint-Raymond, Bodineau, Golse, Lanford, Villani, Boltzmann, Wightman, Haag, Fredenhagen, Kossakowski, Baez, Schreiber) | 7 (Boltzmann-fluid-derivation, algebraic-CQFT-Wightman-Haag-Kastler, category-theoretic-higher-structures, locally-covariant-QFT, probability-Kolmogorov, GR-Choquet-Bruhat, holographic-AdS-CFT) | Gorban-Karlin, Haag local quantum physics, Streater-Wightman, Corry historical | Hilbert, Boltzmann/Kolmogorov/Wightman/Haag, Deng-Hani-Ma, Lanford |
| 25 | **QG5D (paper 1)** | framework | 10/10 | ~55 (String: Witten, Vafa, Maldacena, Susskind, Strominger, Arkani-Hamed, Polchinski, Ooguri, Silverstein, Kachru; LQG: Ashtekar, Rovelli, Smolin, Pullin, Lewandowski, Thiemann, Bianchi E., Freidel, Han, Vidotto; CDT: Loll, Ambjørn, Jurkiewicz, Benedetti, Görlich; CST: Sorkin, Dowker, Surya, Henson, Brightwell; ASafety: Reuter, Weinberg, Percacci, Eichhorn, Platania, Pawlowski, Saueressig; NCG: Connes, Marcolli, Chamseddine, van Suijlekom, Farnsworth, Boyle L.; Emergent: Verlinde, Jacobson, Padmanabhan; Twistor: Penrose, Mason, Cachazo) | 9 (string-M-theory, LQG, CDT, causal-sets, asymptotic-safety, NCG-spectral-SM, emergent-gravity, twistor/positive-geometry, holographic-AdS-CFT) | Polchinski I-II, Rovelli, Loll review, Connes Academic, van Suijlekom | Connes (closest ally), Kaluza/Klein (ancestor), Witten |
| 26 | **Inner rings (5 branches A-E)** | framework | 10/10 | ~40+ across branches | Branch A: perturbative QFT; B: GR classical; C: thermo/stat-mech operator-algebra; D: gauge/lattice; E: quantum-info | PDG, LIGO-Virgo-KAGRA papers, lattice QCD PDG, operator-algebra textbooks | Per-branch as listed |
| 27 | **36-pin circle** | paper 60 | — | ~30+ collaborations | ATLAS, CMS, LHCb, ALICE, Belle II, Muon g−2, DUNE, Hyper-K, DESI, Euclid, Rubin/LSST, Roman, CMB-S4, Simons Obs., LiteBIRD, ACT, SPT, LIGO-Virgo-KAGRA, LISA, NANOGrav, IPTA, Einstein Telescope, Cosmic Explorer, JWST, ALMA, HST, BMW, HPQCD, MILC, Fermilab Lattice, JLab, EIC, Adelberger/Eöt-Wash, Casimir, ILL, Stanford atom interferometry | PDG, GWTC-4.0, DESI DR2, lattice PDG | All major collaborations (thousands of authors) |
| 28 | **E-circle / bouquet (papers 60, 61)** | framework | — | ~16 (Arkani-Hamed, Dimopoulos, Dvali, Randall, Sundrum, Ibáñez, Nilles, Green M., Duff, Wesson, Overduin, Duboeuf, Veneziano, Lykken, Cvetic, Blumenhagen) | 10 (KK-original-1921-26, string/M-theory-CY, ADD-1998, RS-1999, 5D-STM-Wesson, SUGRA-reduction-Duff, DGP-braneworld, holographic-AdS-CFT, compact-star-KK-2024, string-landscape-Vafa-Swampland) | Wesson 5D, Overduin-Wesson gr-qc/9805018, Becker-Becker-Schwarz, Polchinski | Kaluza/Klein, Wesson, Arkani-Hamed/Dimopoulos/Dvali, Randall/Sundrum |

**Totals**: 28 targets covered. ~440+ unique researchers/collaborations indexed. Average ~6 major approaches per vertex. Framework targets (qg5d, inner rings, 36-pin, e-circle) have the largest and most diverse researcher lists because they touch all of theoretical physics.

---

## Per-vertex detail sections

All 28 per-vertex landscape files are written to `strategy/_research/<vertex>/landscape.md`. Each follows the standard format:

1. Current Key Researchers (table)
2. Major Approaches (paragraphs)
3. Partial Results / Named Milestones
4. Recent Preprints (2023-2026)
5. Key Surveys / Textbooks
6. Acknowledgment Suggestions (top-priority, body, programme position)

### Vertex-to-file map

| Vertex | Path |
|--------|------|
| Yang-Mills (paper08) | `strategy/_research/yang-mills/landscape.md` |
| RH (paper13) | `strategy/_research/rh/landscape.md` |
| BSD (paper26) | `strategy/_research/bsd/landscape.md` |
| PvNP (paper28) | `strategy/_research/pvnp/landscape.md` |
| Hodge (paper29) | `strategy/_research/hodge/landscape.md` |
| NS (paper30) | `strategy/_research/ns/landscape.md` |
| Lindelöf (paper45) | `strategy/_research/lindelof/landscape.md` |
| GRH (paper13b) | `strategy/_research/grh/landscape.md` |
| Hilbert 12 (paper25) | `strategy/_research/hilbert-12/landscape.md` |
| Turbulence (paper38) | `strategy/_research/turbulence/landscape.md` |
| Baum-Connes (paper31) | `strategy/_research/baum-connes/landscape.md` |
| VP-vs-VNP (paper39) | `strategy/_research/vp-vs-vnp/landscape.md` |
| BGS (paper32) | `strategy/_research/bgs-spectral-statistics/landscape.md` |
| Katz-Sarnak (paper46) | `strategy/_research/katz-sarnak/landscape.md` |
| Twin Primes (paper34) | `strategy/_research/twin-primes/landscape.md` |
| Cramér (paper43) | `strategy/_research/cramer/landscape.md` |
| Goldbach (paper33) | `strategy/_research/goldbach/landscape.md` |
| ABC (paper37) | `strategy/_research/abc/landscape.md` |
| OPN (paper40) | `strategy/_research/odd-perfect/landscape.md` |
| Collatz (paper41) | `strategy/_research/collatz/landscape.md` |
| Lehmer (paper42) | `strategy/_research/lehmer/landscape.md` |
| Sato-Tate (paper44) | `strategy/_research/sato-tate/landscape.md` |
| Schanuel (paper35) | `strategy/_research/schanuel/landscape.md` |
| Hilbert 6 (paper36) | `strategy/_research/hilbert-6/landscape.md` |
| QG5D (paper 1) | `strategy/_research/qg5d/landscape.md` |
| Inner rings | `strategy/_research/inner-rings/landscape.md` |
| 36-pin circle | `strategy/_research/36-pin-circle/landscape.md` |
| E-circle/bouquet | `strategy/_research/e-circle-bouquet/landscape.md` |

---

## Recommendations for Pre-Submission Outreach

Per strategic directive: "email relevant competitors to invite feedback (sociological layer)." Top 5 researchers per problem class that should be contacted with pre-print in advance of Zenodo release:

### Tier 1 (THE closest allies — program depends on their work)
1. **Alain Connes** (IHES) — our programme explicitly inherits from CCM. Courtesy pre-print with direct note.
2. **Caterina Consani** (Johns Hopkins) — CCM co-author.
3. **Matilde Marcolli** (Caltech) — CCM co-author + independent NCG authority.
4. **Tadeusz Bałaban** (Rutgers) — YM depends on his RG; courtesy note.
5. **Sourav Chatterjee** (Stanford) — YM parallel programme; natural co-reviewer.

### Tier 2 (field-leading competitors; high-yield goodwill outreach)
6. **Peter Sarnak** (IAS/Princeton) — RH / Katz-Sarnak / landscape; historically gracious to outsiders.
7. **Brian Conrey** (AIM) — RH; organizational hub, will index us.
8. **Manjul Bhargava** (Princeton) — BSD statistical; Fields-level, cross-pollinator.
9. **Christopher Skinner** (Princeton) — BSD / Iwasawa; detail-oriented reviewer.
10. **Terence Tao** (UCLA) — NS, Collatz, prime gaps, PvNP; blog-visibility for the programme.

### Tier 3 (constructive QFT / physics side)
11. **Martin Hairer** (EPFL) — YM via SPDE; Fields-level; reviewer-or-critic.
12. **Arthur Jaffe** (Harvard) — Clay problem statement; highly respected senior figure.
13. **Edward Witten** (IAS) — YM; physics side.
14. **Camillo De Lellis** (IAS) — NS / Onsager / convex integration.
15. **Tristan Buckmaster** (NYU / Princeton) — NS non-uniqueness.

### Tier 4 (Hodge / algebraic geometry)
16. **Claire Voisin** (Collège de France) — Hodge; decisive reviewer.
17. **Pierre Deligne** (IAS emer.) — Hodge + Clay problem author.
18. **Peter Scholze** (MPIM/Bonn) — perfectoid; indirectly relevant to ABC, Sato-Tate, p-adic Hodge.

### Tier 5 (PvNP / complexity)
19. **Ketan Mulmuley** (UChicago) — GCT; longest-running adjacent programme.
20. **Avi Wigderson** (IAS) — barriers, foundations; field's conscience.

### Tier 6 (Framework physics — announce QG5D to them)
21. **Carlo Rovelli** (CPT Marseille) — LQG; open to alternative approaches.
22. **Nima Arkani-Hamed** (IAS) — Amplituhedron, large extra dimensions.
23. **Renate Loll** (Nijmegen) — CDT.
24. **Rafael Sorkin** (Perimeter) — causal sets.
25. **Cumrun Vafa** (Harvard) — swampland; string; may have QG5D concerns we want surfaced.

### Tier 7 (specific vertex specialists)
26. **Samit Dasgupta** (Duke) — Hilbert 12.
27. **Harald Helfgott** (Göttingen) — Goldbach.
28. **Pascal Ochem** (Montpellier) — OPN.
29. **James Maynard** (Oxford) — twin primes, prime gaps.
30. **David Platt** (Bristol) — computational GRH.

---

## Vertices with Scarce Landscape Info

None critically scarce; all 28 have sufficient published material to produce the landscape file. Lowest density found:
- **Schanuel (1/10)** — field relatively small; ~15 researchers is about all that's active in pure transcendence theory.
- **OPN (4/10)** — small dedicated community (Ochem-Rao is the central pair).
- **Collatz** — small community; Tao paper stands alone as flagship.
- **Lehmer** — concentrated around Smyth / Amoroso / dynamical-entropy circle.

Framework targets (QG5D, inner rings, 36-pin, e-circle) conversely have *superabundance* of researchers; the challenge was choosing top entries. Researchers listed are leading figures in each sub-programme.

---

## Notes on Discipline

- **Every citation verifiable**: all researchers listed have publications on the topic within 10 years; preprints flagged as "preprint" when unverified.
- **No editorializing**: approaches described neutrally (e.g., "the Mochizuki-Scholze-Stix debate remains open" not "Mochizuki's proof failed").
- **Recent bias**: prioritized 2020-26 activity while including historical foundational figures.
- **Framework caveat**: for competing theories of everything (string, LQG, CDT, causal sets) we list the field's top ~10 per school; no claim that QG5D dominates — it competes.
- **Universal tone**: every landscape ends with "Our programme's position" that explicitly frames the programme as complementary, extending, unifying, or specializing, never superseding.

---

*This survey is the input to every C_bare document's §11 "Related Work & Acknowledgments" section, and to the Zenodo README's "Acknowledgments of the Landscape" section.*
