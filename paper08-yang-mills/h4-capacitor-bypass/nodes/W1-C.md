# W1-C — LANG↔QFT capacitor-first candidate-cell exploration

**Author slot:** Wave 1 Author C (LANG↔QFT — Kapustin-Witten / geometric Langlands ↔ N=4 SYM S-duality)
**Date:** 2026-04-13
**Mode:** capacitor-first; H4 bypass is the long-shot bonus
**Primary deliverable:** the LANG↔QFT cell-fill itself (standing framework tool)
**Secondary deliverable:** H4-bypass viability verdict (pre-registration: likely CONJECTURED-NEGATIVE / PARTIAL)

---

## §0 Direction

The cell LANG↔QFT is listed CANDIDATE in capacitor v1 §"Candidate cells — unexplored correspondences" (line 170):

> *"LANG ↔ QFT — Langlands ↔ quantum field theory — Kapustin-Witten: geometric Langlands = S-duality of 4D N=4 SYM. Electric-magnetic duality ↔ Langlands duality."*

This node fills it with a Millennium-grade entry (Statement / Mechanism / Source / Status / Verification / Load-bearing / Transposition recipe — per capacitor v1's cell format specification, line 183). The fill is durable regardless of whether H4 closes.

The H4 secondary question — *does Kapustin-Witten S-duality give a structural route to an H4-equivalent statement on the S-dual side?* — is explored honestly. Pre-registration per brief §3.0.6: likely CONJECTURED-NEGATIVE, because H4 lives in **pure non-SUSY 4D YM** (where AF runs the coupling) and S-duality lives in **N=4 SYM** (where the coupling doesn't run, by finiteness). The bridge is fragile and known to break at soft SUSY breaking.

**Voice (§J):** "H4 is still the wall." If the cell-fills LAND and H4 doesn't bite, the outcome is *"The capacitor gained the LANG↔QFT cell; the wall stayed named."* That is a Tier 2 win — a durable framework tool for RH, BSD, PvNP, and future proof chains.

---

## §1 Research — primary source verification

### §1.1 Kapustin-Witten 2007 (arXiv:hep-th/0604151, CNTP 1 (2007) 1-236)

**Verbatim from the abstract** (verified via arXiv abstract page):

> *"The geometric Langlands program can be described in a natural way by compactifying on a Riemann surface C a twisted version of N=4 super Yang-Mills theory in four dimensions."*

> *"Seemingly esoteric notions of the geometric Langlands program, such as Hecke eigensheaves and D-modules, arise naturally from the physics."*

Listed mechanisms (abstract): *"electric-magnetic duality of gauge theory, mirror symmetry of sigma-models, branes, Wilson and 't Hooft operators, and topological field theory."*

### §1.2 The S-duality action — technical content

From multiple secondary sources (cross-verified):

- **Gauge group**: S-duality interchanges N=4 SYM with gauge group $G$ at coupling $\tau$ and the theory with Langlands dual group $G^\vee$ (denoted $G^L$ or $^LG$ in various literatures) at coupling $-1/(n_\mathfrak{g}\tau)$ where $n_\mathfrak{g}$ is the lacing number (1 for simply-laced).
- **Partition function identity**: $Z(\tau, X, G) = Z(-1/\tau, X, G^\vee)$ for the topologically twisted theory on 4-manifold $X$.
- **Topological twist family**: a CP^1-parametrized family of twists $\Psi \in \mathbb{CP}^1$ of N=4 interpolating between the **A-twist** ($\Psi = \infty$, sigma-model to Hitchin moduli space $\mathcal{M}_H(G,C)$) and the **B-twist** ($\Psi = 0$, sigma-model to $\mathcal{M}_H(G^\vee, C)$) when compactified on Riemann surface $C$.
- **Langlands emerges as mirror symmetry**: the two sigma-models on $\mathcal{M}_H(G,C)$ and $\mathcal{M}_H(G^\vee, C)$ are mirror pairs; equivalence of their categories of branes is the geometric Langlands correspondence.
- **'t Hooft ↔ Hecke**: 't Hooft line operators in N=4 SYM correspond (under S-duality and topological twist) to geometric Hecke operators acting on Higgs bundles in the sigma-model; this is the bridge that realizes the automorphic side.

### §1.3 Status of the correspondence — mathematical vs. physical

**Kapustin-Witten 2007 is a physics-level argument**, not a mathematically rigorous theorem. It uses path integrals, topological twists, and mirror symmetry at the physics level. The proof of the **geometric Langlands conjecture** itself is now MATHEMATICAL — **Gaitsgory-Raskin et al. 2024** (arXiv:2405.03599, plus parts II-V through arXiv:2409.09856) proved the conjecture in characteristic zero (de Rham and Betti forms), a series of 5 papers totaling ~1000 pages, culminating in the 2025 Breakthrough Prize for Gaitsgory.

**Key point**: the geometric Langlands conjecture is now a theorem. Kapustin-Witten's physics-level "= S-duality of N=4 SYM" statement is still a physics-level equivalence — **the mathematical theorem was proved by purely mathematical methods (derived algebraic geometry, representation theory)**, not via the Kapustin-Witten route. So LANG↔QFT has two distinct layers:

- **Layer A (mathematical)**: geometric Langlands (now PROVED, 2024, de Rham + Betti) connects automorphic/spectral sides of the theory of $G$-bundles and Hecke eigensheaves on algebraic curves.
- **Layer B (physical)**: Kapustin-Witten's interpretation of geometric Langlands as S-duality of N=4 SYM remains a physics-level statement — foundational in physical mathematics but not a rigorous mathematical theorem.

### §1.4 N=4 SYM vs pure YM — the structural severance

**N=4 SYM** is a **superconformal field theory**: 
- UV-finite to all orders by Mandelstam 1983 / Brink-Lindgren-Nilsson 1983 (classical + quantum conformal invariance by SUSY cancellation)
- $\beta(g) = 0$ exactly; coupling $g$ does NOT run
- Exactly solvable at all couplings (integrability in planar limit; bootstrap at finite $N$)
- S-duality $SL(2,\mathbb{Z})$ acts on $\tau = \theta/(2\pi) + 4\pi i/g^2$

**Pure non-SUSY 4D YM** (the H4 target):
- Asymptotically free: $\beta(g) < 0$, $g(\mu) \to 0$ as $\mu \to \infty$
- Running coupling produces $|x|^{-8}(\log 1/|x|\Lambda)^{-2}$ short-distance behavior (H4)
- NO known exact S-duality (lattice-level strong/weak duality is only conjectural and does not permit rigorous OPE extraction)

**Soft SUSY breaking** (from Masiero-Sarkar 1983 Phys Lett B132 etc. — found in the soft-breaking literature): one can break N=4 down to N=0 (pure YM + massive scalars + massive fermions) while preserving UV finiteness for certain quadratic mass terms. However, **S-duality is GENERICALLY BROKEN by soft breaking**: the softly-broken theory is no longer superconformal, the coupling runs, and the $SL(2,\mathbb{Z})$ invariance is lost (at best, survives for specific "N=2* deformations" — see Kapustin-Witten §11 and follow-up literature, but does not extend to N=0).

**This is the structural obstacle**: to get from N=4 SYM (where S-duality + Kapustin-Witten live) to pure YM (where H4 lives), you must break SUSY — and SUSY-breaking breaks S-duality. There is no route where H4's AF-running coupling and S-duality coexist.

---

## §2 Cell-fill — PRIMARY DELIVERABLE (Millennium-grade)

### LANG ↔ QFT: Kapustin-Witten geometric Langlands / S-duality correspondence

**Statement**: The geometric Langlands correspondence for a complex reductive group $G$ and smooth projective curve $C$ over $\mathbb{C}$ is equivalent — at the physics level — to electric-magnetic S-duality of topologically twisted 4D $\mathcal{N}=4$ super Yang-Mills with gauge group $G$, compactified on $C$. Explicitly: S-duality exchanges N=4 SYM at coupling $\tau$ with gauge group $G$ and N=4 SYM at coupling $-1/(n_\mathfrak{g}\tau)$ with Langlands dual group $G^\vee$; under the GL-twist and compactification on $C$, this becomes mirror symmetry between the sigma-models to Hitchin moduli spaces $\mathcal{M}_H(G, C)$ and $\mathcal{M}_H(G^\vee, C)$, whose equivalence of brane categories IS the geometric Langlands correspondence. 't Hooft line operators on the gauge-theory side correspond to geometric Hecke operators on the Langlands side.

**Mechanism** (how the correspondence works, 3 sentences):

1. **Gauge side → Langlands side via compactification + twist**: Take 4D N=4 SYM on $\mathbb{R}^2 \times C$, apply the GL-twist (parametrized by $\Psi \in \mathbb{CP}^1$) to obtain a 4D TQFT, then compactify on $C$ to obtain a 2D TQFT. Depending on $\Psi$, the resulting 2D theory is the A-model or B-model with target the Hitchin moduli space $\mathcal{M}_H$. 

2. **S-duality → mirror symmetry**: The $SL(2,\mathbb{Z})$ S-duality of the 4D N=4 SYM (which acts as $\tau \mapsto -1/\tau$ on the coupling and exchanges $G \leftrightarrow G^\vee$) descends under compactification to mirror symmetry between the A-model on $\mathcal{M}_H(G, C)$ and B-model on $\mathcal{M}_H(G^\vee, C)$. Mirror symmetry gives an equivalence of derived categories of branes.

3. **Hecke operators from 't Hooft lines**: 't Hooft line operators in the 4D gauge theory (which create magnetic flux) correspond, after compactification, to geometric Hecke operators acting on the moduli space of $G$-bundles on $C$ (Higgs bundles, to be precise, in the twisted theory). Hecke eigensheaves — the central objects of geometric Langlands — emerge as eigenbranes for the 't Hooft-line action on the Hitchin moduli space.

**Source**: 
- **Primary physics**: Kapustin-Witten, *"Electric-Magnetic Duality and the Geometric Langlands Program"*, Commun. Num. Theor. Phys. 1 (2007) 1-236, arXiv:hep-th/0604151. 236 pages; the foundational work.
- **Extensions**: Witten, *"More on Gauge Theory and Geometric Langlands"*, Adv. Theor. Math. Phys. 22 (2018), arXiv:1506.04293; Elliott-Yoo *"Geometric Langlands twists of N=4 gauge theory from derived algebraic geometry"* arXiv:1507.03048.
- **Survey**: Frenkel, *"Lectures on the Langlands Program and Conformal Field Theory"*, arXiv:hep-th/0512172.
- **Primary mathematics (updated 2024-2025)**: Gaitsgory-Raskin et al., *"Proof of the geometric Langlands conjecture I-V"*, arXiv:2405.03599 through arXiv:2409.09856 (5 papers, ~1000 pages, 2024). Proved the conjecture mathematically (characteristic zero, de Rham + Betti) by methods independent of the Kapustin-Witten path integral route. Gaitsgory received the 2025 Breakthrough Prize in Mathematics for this work.
- **Classical Langlands dual groups**: Langlands 1967 memorandum; Kottwitz-Shelstad; standard textbook material.

**Status**: 
- **Layer A (mathematical geometric Langlands)**: PROVED (Gaitsgory-Raskin 2024, characteristic zero; de Rham + Betti forms)
- **Layer B (Kapustin-Witten physics-level equivalence)**: ESTABLISHED at the physics level (foundational, peer-reviewed, widely accepted in mathematical physics; not mathematically rigorous as a stand-alone proof but supported structurally by the now-proved Layer A)

**Verification data**: 
- Kapustin-Witten 2007 is the most-cited paper connecting gauge theory to Langlands; published in the Clay-affiliated journal *Communications in Number Theory and Physics*, founded expressly to host such interdisciplinary work.
- Gaitsgory-Raskin 2024 proof was front-page news in *Quanta Magazine* (July 2024), *Nature* (Aug 2025), and *Scientific American* (2025); received the 2025 Breakthrough Prize ($3M to Gaitsgory) and New Horizons Prize to Raskin.
- Cross-check with filled capacitor cells:
  - **ANT↔LANG "Automorphic ↔ Galois"** (PARTIAL): covers the ARITHMETIC Langlands; LANG↔QFT covers the GEOMETRIC Langlands. Complementary, not overlapping.
  - **REP↔LANG "Langlands = representation-theoretic reciprocity"** (PARTIAL): covers the representation-theoretic structure; LANG↔QFT provides the PHYSICAL interpretation / alternative proof route (Kapustin-Witten) + the now-mathematical proof (Gaitsgory-Raskin).
  - **LANG↔NCG** (in v1 candidate list): Connes-Marcolli GL₂ system. Complementary to LANG↔QFT.
- No computational verification — this is a structural cell-fill; verification is literature-historical.

**Load-bearing for**: 
- **Framework-wide** (not specifically H4): provides a cross-domain escape route when a proof chain has a gauge-theoretic statement about N=4 SYM that might be easier to analyze on the Langlands / automorphic side. Candidates:
  - **RH (Paper 13)**: if any CCM-adjacent argument can be restated as a statement about automorphic L-functions via LANG↔QFT, the cell provides the dictionary.
  - **BSD (Paper 26)**: BSD already uses ANT↔LANG (modularity) and ANT↔AG; LANG↔QFT opens a further layer connecting BSD's L-function to gauge-theoretic invariants (e.g., the Minhyong Kim arithmetic Chern-Simons analogy cross-links here).
  - **PvNP (Paper 28)**: if any clone-polymorphism statement admits a gauge-theoretic restatement, LANG↔QFT is the bridge.
  - **Speculatively for H4**: via N=4 → pure YM reduction, if a viable SUSY-breaking route to H4 emerges. Honest assessment: this is NOT expected to work (see §3 below). H4 load-bearing is CONJECTURED-NEGATIVE.
  - **Future Millennium work**: Hodge conjecture (geometric Langlands → motives → Hodge structures) would naturally recruit LANG↔QFT.

**Transposition recipe** (HOW to use this cell — the actionable bit):

*If stuck on a statement phrased in the gauge-theoretic language of N=4 SYM*:

1. **Identify the statement's gauge-theory content**: is it about a correlation function, a partition function, a line operator, a boundary condition, or a moduli space of configurations? Does it respect the topological twist or only the physical theory?
2. **Apply S-duality**: transform the statement via $\tau \mapsto -1/\tau$, $G \mapsto G^\vee$. Wilson lines map to 't Hooft lines. Electric boundary conditions (Neumann) map to magnetic (Dirichlet). Note: the coupling is inverted, so WEAK coupling becomes STRONG coupling — a genuine non-perturbative transformation.
3. **Translate to the Langlands side**: apply the GL-twist with the appropriate $\Psi$, compactify on a Riemann surface $C$, and restate the problem in terms of the Hitchin moduli space $\mathcal{M}_H(G^\vee, C)$ or sheaves / D-modules on $\mathrm{Bun}_{G^\vee}(C)$. Hecke eigensheaves, $\mathcal{D}$-modules on $\mathrm{Bun}_G$, and flat $G^\vee$-bundles are the target objects.
4. **Attempt the proof in Langlands language**: use the methods of geometric representation theory — Beilinson-Drinfeld Hecke eigensheaves, opers, derived categories of $\mathcal{D}$-modules, Gaitsgory-Raskin's proved functor. Methods available post-2024 that were not available pre-2024.
5. **Translate back**: the answer on the Langlands side lifts back through the compactification / twist / S-duality chain to a statement on the gauge side. Caveat: the translation back may only give the TWISTED answer; physical (untwisted) content requires additional work.

**Caveats to the recipe** (important, do not skip):

- **The twist is lossy**: topological twisting discards all non-topological information. If the gauge-theory statement depends on non-topological features (e.g., short-distance OPE coefficients, which depend on physical scales), the twist kills exactly the information you need. H4 falls into this category — see §3.
- **SUSY is required**: the entire structure depends on $\mathcal{N}=4$ supersymmetry. Breaking SUSY generically breaks S-duality. Do not assume the recipe transfers to non-SUSY theories; see §3.
- **$\mathcal{M}_H$ is SYMMETRIC but infinite-dimensional**: the Hitchin moduli space has natural hyperkähler structure and is well-studied, but branes on it are not always easy to construct or classify. The Gaitsgory-Raskin proof is ~1000 pages for a reason.

---

## §3 H4 bypass assessment — honestly

### §3.1 Pre-registration (§3.0.6): likely CONJECTURED-NEGATIVE

The fatal structural problem:

- **H4 lives in pure YM**: where AF runs the coupling, producing the $|x|^{-8}(\log)^{-2}$ short-distance OPE.
- **S-duality lives in N=4 SYM**: where the coupling does NOT run (superconformal).
- **The bridge must break SUSY**, and SUSY-breaking generically breaks S-duality.

The only routes where both S-duality and AF coexist are:
- **None in 4D**. N=4 and pure YM are different theories in different coupling classes (finite vs running).
- **N=2* deformations** (mass for hypermultiplets) preserve some partial duality but are still superconformal at the appropriate coupling; N=0 (pure YM) is not accessible by any duality-preserving deformation.
- **Lattice strong/weak duality conjectures** (e.g., 't Hooft loops in pure YM) are conjectural and do not give rigorous OPE extraction.

### §3.2 What would a viable H4 bypass via LANG↔QFT need to look like?

For the bypass to produce H4 rigorously, we would need:

1. A **concrete SUSY-breaking map** from N=4 SYM to pure YM that preserves enough S-duality structure to generate a *dual* statement.
2. The dual statement to be a short-distance OPE claim (not, e.g., a partition-function equality or a line-operator expectation value), since H4 requires the specific $C_N|x|^{-8}(\log)^{-2}$ short-distance form.
3. The dual statement to be provable by Langlands methods (post-2024 Gaitsgory-Raskin toolkit or earlier methods).
4. The inverse map (dual statement → H4) to be rigorous.

**Each of (1)-(4) is a substantial open programme**; composed, they are doubly open.

### §3.3 A speculative route — and why it doesn't close

One can imagine:

- **Step A**: Add soft SUSY-breaking mass terms to N=4 SYM, decoupling scalars + fermions at mass $M$.
- **Step B**: At scales $\mu \gg M$, the theory looks like N=4 (conformal); at $\mu \ll M$, it looks like pure YM (AF).
- **Step C**: Short-distance ($\mu \to \infty$) OPE in the broken theory: dominated by N=4 behavior, S-duality still effective.
- **Step D**: Extract AF-running from the crossover at $\mu \sim M$.

**Why this doesn't close H4**:

- Step C is UV-conformal and has NO $|x|^{-8}(\log 1/|x|\Lambda)^{-2}$ form (no running, no AF log, no $\Lambda$). It gives the N=4 short-distance OPE, not the pure-YM one.
- The AF coefficient $C_N = 2(N^2-1)/\pi^6$ emerges from the specific one-loop beta function of pure YM, not from N=4 physics. Any dual statement extracted from N=4's S-duality will carry N=4's zero beta function, not pure YM's running.
- The crossover at $\mu \sim M$ (step D) is exactly the regime where both SUSY and S-duality break; extracting rigorous OPE structure from this regime is an open problem equivalent to or harder than H4 itself.

**The speculative route is a redescription of the H4 problem, not a bypass.**

### §3.4 Verdict

**CONJECTURED-NEGATIVE for H4 bypass.** 

The LANG↔QFT cell does not provide a viable bypass for H4 because:
- Kapustin-Witten S-duality is a property of N=4 SYM (conformal, exact)
- H4 is a property of pure YM (AF, running)
- No known duality-preserving map connects these theories
- The topological twist (which is what makes the Langlands side accessible) throws away exactly the short-distance OPE information H4 requires

**Cell-fill status: EXCELLENT** (full Millennium-grade entry, Layer A now proved by Gaitsgory-Raskin 2024; standing tool for future proof chains).

**H4 load-bearing: CONJECTURED-NEGATIVE** (documented above; does not close H4 but does not add to §F kill list because the reasoning is not a NEW kill pattern, just a confirmation that the SUSY→non-SUSY bridge doesn't exist).

### §3.5 Can there be a PARTIAL contribution to the H4 programme?

Possibly, at the structural level:

- **Cross-check on the topological content of H4**: the H4 claim is inherently NON-topological (depends on scales, logs, AF). If a Kapustin-Witten-style twist of YM existed (pure YM has no 4D twist because no SUSY), it would LOSE H4. This negative result CORROBORATES that H4 is not a topological invariant and requires analytic / microlocal / probabilistic techniques — aligning with the MICRO↔QFT and ERG↔QFT priority directions.
- **Structural placement of H4 in the framework**: the LANG↔QFT cell-fill makes explicit what framework tools are AVAILABLE for gauge-theoretic problems. H4 is NOT in the LANG↔QFT-reachable sub-sector. This narrows the search to MICRO / ERG / PROB directions.

This is a **weak** contribution — it's structural orientation, not a closure step. But as §3.3 tertiary from the brief emphasizes, even FAILED cell-fills are durable capacitor growth if they produce a filled cell with a clearly-stated negative status and the reason.

---

## §4 Self-suspicion (Step 5.5)

Three self-suspects per the method:

**S1. "You conflated N=4 SYM with pure YM."**
- *Check*: Have I conflated? No — §1.4 and §3 explicitly distinguish them and identify the N=4-to-pure-YM bridge as the fatal point. The cell-fill is for LANG↔QFT where "QFT" in capacitor v1 line 170 is explicitly N=4 SYM (Kapustin-Witten), not pure YM. The cell's TRANSPOSITION RECIPE is correctly restricted to statements in N=4 language.
- *Residual risk*: a reader of the cell could misread the transposition recipe as universally applicable to QFT and attempt to use it for pure YM. Mitigation: the CAVEATS section (end of §2 recipe) states explicitly "SUSY is required; breaking SUSY generically breaks S-duality." Additionally, §3 is dedicated to the H4 bypass question and answers it CONJECTURED-NEGATIVE with reasoning.
- *Verdict*: mitigated.

**S2. "Kapustin-Witten is formal/physical; full mathematical rigor is still under construction; claims about the Langlands side may be conjectural."**
- *Check*: As of 2024, the Langlands SIDE is now PROVED (Gaitsgory-Raskin). The equivalence between the Langlands side and the gauge side (Kapustin-Witten's statement) remains a physics-level equivalence. The cell-fill distinguishes this explicitly via Layer A (mathematical, proved) and Layer B (physical, established but not a stand-alone theorem).
- *Residual risk*: a user of the cell might cite Kapustin-Witten as the PROOF of geometric Langlands, which is incorrect. Mitigation: §1.3 explicitly states the two layers; the Source field of the cell-fill distinguishes "Primary physics" (Kapustin-Witten) from "Primary mathematics" (Gaitsgory-Raskin 2024).
- *Verdict*: mitigated.

**S3. "Backward-verification: verify claims about S-duality's action on short-distance OPE via Kapustin-Witten primary source."**
- *Check*: The Kapustin-Witten paper is about the TOPOLOGICALLY TWISTED N=4, where "short-distance OPE" is not a natural observable (the theory is topological — correlation functions depend only on topology, not on positions). Thus a direct short-distance OPE claim from Kapustin-Witten is NOT available. The untwisted N=4 has a short-distance OPE (conformal, no logs, no $\Lambda$) that is WELL-KNOWN from the superconformal bootstrap literature; S-duality of untwisted N=4 is also well-known (Seiberg-Witten lineage, AdS/CFT, etc.) but is not Kapustin-Witten-specific.
- *Residual risk*: I could have overstated what Kapustin-Witten proves about untwisted N=4's short-distance OPE. Mitigation: §1.1-§1.4 make clear that Kapustin-Witten is about the TWISTED theory (A/B-models on Hitchin moduli) and the H4 discussion in §3 is a SEPARATE exercise about the UNTWISTED physical theory.
- *Verdict*: mitigated. The cell-fill does not claim Kapustin-Witten produces a short-distance OPE statement.

**Additional self-suspect (S4, not in the brief but prudent):** "Gaitsgory-Raskin 2024 may not cover the full geometric Langlands conjecture — only characteristic zero, only de Rham + Betti."
- *Check*: Correct. The proof is characteristic zero (de Rham + Betti). Function-field Langlands (characteristic $p$) is separate and uses Drinfeld's earlier work + extensions; arithmetic Langlands (for number fields) is still a conjecture except for special cases (GL_1 = class field theory, GL_2/Q = modularity, and sporadic higher cases). Cell-fill says "characteristic zero" explicitly.
- *Residual risk*: none load-bearing for the cell; the cell is about GEOMETRIC Langlands specifically.
- *Verdict*: the cell-fill accurately represents the 2024-2026 state.

---

## §5 External unlocks

What would change the H4-bypass verdict from CONJECTURED-NEGATIVE to VIABLE or PARTIAL?

**U1. Discovery of a duality-preserving SUSY-breaking map from N=4 to pure YM.**
This would require a soft-breaking term that preserves $SL(2,\mathbb{Z})$. Current knowledge: N=2* deformations preserve $SL(2,\mathbb{Z})$ but are still superconformal at the relevant coupling; no N=0 deformation preserves it. If someone constructs such a map, LANG↔QFT becomes H4-relevant.

**U2. A generalization of Kapustin-Witten to non-SUSY theories.**
Speculative: a "non-SUSY Kapustin-Witten" where the topological twist is replaced by some other structural device. No known candidate. If discovered, this would be a Breakthrough-Prize-level development in its own right, and would immediately affect H4 and the Millennium programme.

**U3. An S-duality conjecture for pure YM that is both rigorous and computable.**
Lattice 't Hooft loop / 't Hooft-Mandelstam duality is conjectural at the physics level; if mathematized (e.g., via a categorical construction analogous to Gaitsgory-Raskin), it could bypass the N=4 requirement.

**U4. A Langlands-adjacent statement about the AF $\beta$-function.**
If the AF log-structure of H4 could be reformulated as a property of some L-function (Artin, automorphic) that is accessible by Langlands methods, LANG↔QFT might contribute. Speculative. No candidate known.

**U5. Extension of Gaitsgory-Raskin to function-field Langlands.**
Announced in their 2024-2025 writings as an active programme. If this lands, it would open characteristic-$p$ Langlands to the same machinery, and characteristic-$p$ is the natural home for lattice gauge theory (where H4 can be approached rigorously via Balaban). This is the MOST LIKELY external unlock to materialize in the 2-year Clay window.

---

## §6 Next-runner

If the next cycle wants to extend LANG↔QFT work:

- **Priority 6a (most productive)**: Cross-reference LANG↔QFT with existing filled capacitor cells that touch Langlands (ANT↔LANG, REP↔LANG, LANG↔NCG candidate). Build a "Langlands sub-capacitor" — a cluster of cells that compose for cross-domain reasoning. Estimated Tier 2 benefit: 3-4 cell upgrades, highly useful for BSD and future arithmetic proof chains.
- **Priority 6b (speculative)**: Monitor Gaitsgory-Raskin function-field extensions (2025-2026 active programme). If published in the run window, a U5-type unlock may materialize, and LANG↔QFT becomes directly H4-relevant via lattice gauge theory.
- **Priority 6c (low probability, high value)**: Attempt the N=2* → structural statement about AF-log route (U1 direction). This is a substantial research programme, not a single node's work; budget accordingly (months, not hours).
- **Priority 6d (do NOT pursue)**: Any attempt to use the Kapustin-Witten twist itself to extract H4's short-distance OPE directly. This hits the "twist is lossy" caveat and will not succeed. Register as K-8 if anyone tries and fails.

---

## §7 Summary line

**Cell-fill**: LANG↔QFT filled with Millennium-grade entry; Layer A (geometric Langlands) now PROVED (Gaitsgory-Raskin 2024); Layer B (Kapustin-Witten physics equivalence) ESTABLISHED.

**H4 bypass verdict**: CONJECTURED-NEGATIVE. The N=4-to-pure-YM bridge is severed by SUSY-breaking / S-duality breaking. The topological twist discards exactly the short-distance OPE information H4 requires. No route in current knowledge.

**Millennium-grade durability**: EXCELLENT. The cell-fill is a standing framework tool for RH, BSD, PvNP, Hodge, and any future proof chain where a gauge-theoretic statement about N=4 SYM might be easier in Langlands language. Priority 6a extends this into a Langlands sub-capacitor.

**Voice (§J)**: "The capacitor gained the LANG↔QFT cell; the wall stayed named. H4 is still the wall."

---

## §8 File manifest

- **Node**: `paper08-yang-mills/h4-capacitor-bypass/nodes/W1-C.md` (this file)
- **Cell-fill extract** (for capacitor v1 update, §2 of this file): the full "LANG ↔ QFT: Kapustin-Witten geometric Langlands / S-duality correspondence" entry is ready for direct copy into `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md` §"Filled cells" (promote from Candidate to Tier 1 Filled).
- **Kill additions**: none recommended — the negative H4 verdict is a STRUCTURAL observation, not a new kill pattern. Existing K-1 through K-7 cover all attempted attack surfaces.
- **Status**: complete. Returning to runner.
