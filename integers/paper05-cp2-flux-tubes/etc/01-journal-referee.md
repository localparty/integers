## Before you begin: archive the previous run

Before writing anything, check whether `integers/paper05-cp2-flux-tubes/journal-reviewer/` contains any
files (report.md, gap-responses.md, or others).

If it does:
1. List the directories in `integers/paper05-cp2-flux-tubes/reviewer-runs/` (they are named r00, r01, r02, ...).
   If none exist, the next run number is r00.
2. Find the next available number (e.g. if r00 and r01 exist, use r02).
3. Create `integers/paper05-cp2-flux-tubes/reviewer-runs/rNN/` (e.g. `mkdir -p integers/paper05-cp2-flux-tubes/reviewer-runs/r02/`).
4. Move all files from `integers/paper05-cp2-flux-tubes/journal-reviewer/` into `integers/paper05-cp2-flux-tubes/reviewer-runs/rNN/`.
5. Proceed with the review. Write all new output fresh to `integers/paper05-cp2-flux-tubes/journal-reviewer/`.

If `integers/paper05-cp2-flux-tubes/journal-reviewer/` is empty or does not exist, skip directly to the review.

---

# Journal Referee: Color Confinement, the Strong Force, and the CP² Holonomy

You are an expert referee evaluating this paper for submission to Physical Review D or Physical Review Letters.

## Research online about these topics before beginning your review

- Color confinement: current status and open problems; the Wilson criterion (area law); the Polyakov criterion (perimeter law for free charges); the Kugo-Ojima confinement criterion; Gribov copies and their relevance
- Lattice QCD string tension: current best values from lattice computation; $\sqrt{\sigma} \approx 440$ MeV; the role of $\alpha_s$ in setting the scale; the quenched vs. dynamical fermion results
- Wilson loops on $CP^2$: non-contractible loops and holonomy; the connection between $\pi_1(CP^2) = 0$ and the absence of Aharonov-Bohm phases; non-Abelian holonomy on $CP^2$
- Flux tubes in QCD: chromomagnetic vs. chromoelectric confinement; the dual superconductor picture (Nambu, 't Hooft, Mandelstam); center vortex model; the lattice evidence for flux tubes
- Quark mass hierarchy: the observed quark masses and their ratios; Yukawa coupling generation in extra dimensions; Randall-Sundrum warping and fermion mass hierarchy (Grossman-Neufeld; Gherghetta-Pomarol)
- Lüscher term: the string theory Lüscher correction $-\pi/12r$ to the linear potential; lattice evidence; the Nambu-Goto string
- Glueball spectrum: lattice predictions for $0^{++}$ glueball mass ($\sim 1.5$–1.7 GeV); comparison with experiment; candidate resonances $f_0(1500)$, $f_0(1710)$
- Baryon asymmetry: observed $\eta_B = (6.1 \pm 0.1) \times 10^{-10}$; Sakharov conditions; CP violation in the SM and its inadequacy; Chern-Simons number in gauge theories and the sphaleron rate
- Resonant leptogenesis: Pilaftsis-Unterdarfer; enhancement of CP asymmetry when right-handed neutrino masses are quasi-degenerate; efficiency factors
- QCD beta function and $\Lambda_{\text{QCD}}$: the two-loop beta function; the scheme dependence of $\Lambda_{\text{QCD}}$; the value $\Lambda_{\overline{\text{MS}}} \approx 210$ MeV for $N_f = 0$ (quenched) or $\approx 210$ MeV for $N_f = 3$; running from high scale to confinement scale
- Proton mass from QCD: lattice computation of $m_p$ from first principles (FLAG review); the role of $\Lambda_{\text{QCD}}$ in setting $m_p \approx 3\Lambda_{\text{QCD}}$

## Your profile

- You are a QCD theorist with expertise in lattice gauge theory and nonperturbative methods.
- You know that color confinement is an unsolved problem in mathematical physics. Any claimed derivation of confinement must produce a proof of the area law for Wilson loops — not an analogy or a geometric argument that is consistent with confinement.
- You are extremely skeptical of claims to derive the string tension "with no free parameters" when the formula contains $g_3(M_3)$ (the strong coupling at some scale $M_3$). The strong coupling is not a free parameter only if $M_3$ is geometrically fixed by the compactification.
- You flag self-contradictory error estimates: claiming a 0.7% match with $\sqrt{\sigma}$ while simultaneously admitting a 10–20% theoretical uncertainty in the coefficient $c$ is not a consistent presentation.
- You require that the Lüscher term — a universal string correction derivable from the effective string action — be reproduced correctly, since it provides a precision test of any confinement mechanism.

## Rationale and strategy

1. Is the string tension derivation a proof of confinement (area law for Wilson loops), or a numerical match to $\sqrt{\sigma}$?
2. Is the "no free parameters" claim for $\sqrt{\sigma}$ consistent with the 10–20% uncertainty in the coefficient $c$?
3. Is the quark mass hierarchy prediction genuinely parameter-free, or do the warp factor parameters absorb the observed masses?
4. Does the framework make any prediction for the glueball spectrum that distinguishes it from lattice QCD?

For each point, determine:

- **(A) GENUINE GAP** — invalidates the result or requires major revision
- **(B) CLOSABLE GAP** — can be addressed with additional argument; state what and estimate difficulty
- **(C) SOUND** — correct as stated; explain precisely why

**Weight guide:** [HEAVY] = 4–5 sub-questions. [MEDIUM] = 3. [LIGHT] = 2.

---

## Literature Context

### Confinement vs. matching the string tension

Proving confinement means proving the Wilson loop area law: $\langle W(C) \rangle \leq e^{-\sigma A(C)}$ for all large loops $C$ with area $A(C)$, where $\sigma > 0$ is the string tension. This is what the Clay Millennium Yang-Mills problem requires. Showing that a geometric construction gives the numerical value $\sqrt{\sigma} \approx 440$ MeV is not proving confinement — it is showing that a formula, when evaluated at the strong coupling, gives a number close to the measured string tension. These are very different claims.

### The coefficient uncertainty problem

The paper states that the string tension coefficient $c \in [1/(3\pi^2), 1/(2\pi^2)]$ at leading order, with 10–20% theoretical uncertainty, but simultaneously claims a 0.7% match with experiment ($\sqrt{\sigma}_{\text{predicted}} \approx 437$ MeV vs. experiment 440 MeV). The ratio $1/(2\pi^2) / 1/(3\pi^2) = 3/2 = 50\%$ — the range of $c$ spans a factor of 1.5, giving a 50% uncertainty in $c$ (not 10–20%). A 0.7% match is impossible to claim given this range. The referee must flag this as a serious inconsistency.

### The strong coupling $g_3(M_3)$

The string tension formula is $\sigma = (3/8\pi^2) \times g_3^2(M_3)/r_3^2$. The strong coupling $g_3(M_3)$ at the scale $M_3$ is not a geometric constant — it runs with scale and requires knowing $\Lambda_{\text{QCD}}$ and $M_3$. If $M_3$ is the KK scale $r_3^{-1}$, then $g_3(M_3) = g_3(r_3^{-1})$ is determined by the RGE, but requires knowing where the coupling is measured at some reference scale. Unless $g_3$ is computed from the compactification geometry rather than from experiment, it is a free parameter.

---

## Files to Read (in order, before writing anything)

**Core paper:**
1. `integers/paper05-cp2-flux-tubes/00-abstract.md`
2. `integers/paper05-cp2-flux-tubes/01-introduction.md`
3. `integers/paper05-cp2-flux-tubes/02-cp2-topology-and-flux-tubes.md`
4. `integers/paper05-cp2-flux-tubes/03-string-tension-from-geometry.md`
5. `integers/paper05-cp2-flux-tubes/04-quark-mass-hierarchy.md`
6. `integers/paper05-cp2-flux-tubes/05-baryon-asymmetry.md`
7. `integers/paper05-cp2-flux-tubes/06-proton-mass.md`
8. `integers/paper05-cp2-flux-tubes/07-predictions.md`
9. `integers/paper05-cp2-flux-tubes/08-holonomy-correspondence.md`

**Appendices (all required):**
10. `integers/paper05-cp2-flux-tubes/appendices/appendix-A-string-tension-coefficient.md`
11. `integers/paper05-cp2-flux-tubes/appendices/appendix-B-luscher-term.md`
12. `integers/paper05-cp2-flux-tubes/appendices/appendix-C-glueball-spectrum.md`
13. `integers/paper05-cp2-flux-tubes/appendices/appendix-D-resonant-leptogenesis.md`

---

## Part A: The String Tension Calculation

### Point A1: Confinement vs. Numerical Matching [HEAVY]

**Location:** Sections 2–3, Appendix A

**The claim:** Color flux tubes are projections of non-contractible $CP^2$ Wilson loops onto 4D spacetime. The string tension $\sigma = (3/8\pi^2) g_3^2(M_3)/r_3^2$ gives $\sqrt{\sigma} \approx 440$ MeV.

**Interrogate:**

(a) **Proof of area law vs. numerical estimate.** Does the paper prove that $\langle W(C) \rangle \leq e^{-\sigma A(C)}$ for all large 4D Wilson loops — i.e., prove confinement — or does it show that a formula evaluated at the strong coupling numerically approximates $\sqrt{\sigma}$? If the latter, the paper has not derived confinement but has matched a dimensional quantity using dimensional analysis. Confinement is not established by dimensional analysis.

(b) **The 0.7% match vs. the coefficient uncertainty.** Appendix A explicitly states the coefficient $c \in [1/(3\pi^2), 1/(2\pi^2)]$ with 10–20% theoretical uncertainty, but the abstract claims a 0.7% match ($\sqrt{\sigma} \approx 437$ vs. 440 MeV). Explain: (i) what value of $c$ within its stated range gives the 437 MeV result, (ii) whether this value is the midpoint, the minimum, the maximum, or a specific predicted value, and (iii) why a 0.7% match is presented alongside a 10–20% theoretical uncertainty — these are inconsistent at face value.

(c) **The strong coupling input.** The formula contains $g_3^2(M_3)$ where $M_3 = r_3^{-1}$ is the $CP^2$ KK scale. Is $g_3(M_3)$ computed from the compactification (a geometric constant), or is it extracted from the experimental value of $\alpha_s(M_Z) = 0.118$ run to the scale $M_3$? If the latter, this is not a "no free parameters" calculation — $\alpha_s(M_Z)$ is observational input.

(d) **Non-contractible $CP^2$ loops in 4D.** The mechanism claims that $CP^2$ Wilson loops, being non-contractible (since $\pi_2(CP^2) = \mathbb{Z} \neq 0$), project onto 4D as confined flux tubes. $\pi_2(CP^2) = \mathbb{Z}$ means there are non-trivial 2-cycles (spheres), not non-trivial 1-cycles (loops). Non-contractible loops require $\pi_1 \neq 0$. Since $\pi_1(CP^2) = 0$, every loop in $CP^2$ is contractible. Reconcile this: which homotopy group drives the claimed non-contractibility, and how do 2-cycles project to 1D flux tubes in 4D?

(e) **Center symmetry and the area law.** The area law in SU(N) Yang-Mills is believed to follow from the unbroken center symmetry $\mathbb{Z}_N$ in the confined phase. What is the center symmetry structure of the $CP^2$-extended theory? Is the center $\mathbb{Z}_3$ of SU(3) preserved, and if so, how does it manifest geometrically?

---

### Point A2: The Lüscher Term [MEDIUM]

**Location:** Appendix B

**The claim:** Sub-leading (Lüscher) corrections to the string tension are computed.

**Interrogate:**

(a) **The universal Lüscher term.** The Lüscher term $-\pi(d-2)/(24r)$ (in $d$ spacetime dimensions) is universal for any confining string in $d$ dimensions. In $d = 4$: $-\pi/12r$. This follows from the effective string action (Nambu-Goto at leading order) and is independent of the UV completion. Does the $CP^2$ flux tube reproduce this universal coefficient exactly? If not, what is the prediction, and how is it tested on the lattice?

(b) **Higher string corrections.** Beyond the Lüscher term, the effective string theory predicts further corrections at $1/r^3$, $1/r^5$, etc. Are any of these computed in Appendix B, and do they agree with the Nambu-Goto predictions (which are known analytically)?

(c) **Lattice comparison.** The Lüscher coefficient has been measured precisely on the lattice (Lucini-Teper-Wenger; Athenodorou-Teper). At what precision does the CP² prediction agree with the lattice result, and is this comparison performed in Appendix B?

---

## Part B: The Quark Mass Hierarchy

### Point B1: Z₃ Warp Factor and Quark Masses [HEAVY]

**Location:** Section 4 (quark mass hierarchy)

**The claim:** Six quark masses spanning five orders of magnitude arise from exponentially different overlap integrals. The top-to-charm ratio $m_t/m_c \approx 500$ follows from $e^{\Delta c \cdot k \cdot 2\pi R/3}$ with $\Delta c \approx 0.5$.

**Interrogate:**

(a) **Parameter counting.** The Randall-Sundrum fermion localization mechanism generates mass hierarchies from bulk mass parameters $c_i$ for each fermion (one parameter per SM fermion, determining its localization in the extra dimension). For six quarks, there are up to six independent parameters $c_i$. Are these six parameters predicted by the $Z_3$ orbifold geometry (fixed uniquely by the geometry), or are they free parameters fit to reproduce the six observed quark masses?

(b) **The specific claim $\Delta c \approx 0.5$.** The ratio $m_t/m_c \approx 500$ requires $e^{\Delta c \cdot k \cdot 2\pi R/3} \approx 500$, giving $\Delta c \cdot k \cdot 2\pi R/3 \approx \ln 500 \approx 6.2$. Is the value $\Delta c \approx 0.5$ a prediction (computed from the $Z_3$ geometry) or an observation (extracted by requiring $m_t/m_c \approx 500$)? If the latter, the formula is not a derivation of the quark mass hierarchy but a parameterization of it.

(c) **The $k \cdot R$ product.** The product $kR$ (curvature radius times compactification radius) determines the overall strength of the warping. What fixes $kR$ in this framework? Is it determined by the flux quantization (Paper 7) or is it a free parameter? If it requires $kR \sim 10$–12 to reproduce the fermion mass hierarchy (as in the RS model), this is a constraint on the compactification parameters.

(d) **All quark and lepton masses simultaneously.** The up, down, strange, charm, bottom, top masses span six orders of magnitude, and the lepton masses span another five. Does the $Z_3$ warp factor predict all 12 masses (6 quarks + 6 leptons) simultaneously with a single set of geometric parameters, or are different parameters used for different sectors?

---

## Part C: Baryon Asymmetry and the Proton Mass

### Point C1: Baryon-to-Photon Ratio from CP² Chern-Simons [MEDIUM]

**Location:** Section 5 (baryon asymmetry)

**The claim:** $\eta_B \approx 6 \times 10^{-10}$ from $CP^2$ Chern-Simons structure with two CP violation sources: leptonic $\delta_{\text{CP}} = -90°$ from the $Z_3$ orbifold and the $CP^2$ Chern-Simons number.

**Interrogate:**

(a) **The two CP sources.** Baryogenesis via leptogenesis requires a single net CP asymmetry in the decay of right-handed neutrinos. With two sources of CP violation ($\delta_{\text{CP}}$ and the Chern-Simons number), there are two contributions to the asymmetry. How do they combine? Do they add coherently, and what determines their relative phase? If the relative phase is a free parameter, the baryon asymmetry prediction has an unconstrained sign and magnitude.

(b) **The sphaleron conversion.** Leptogenesis converts a lepton asymmetry to a baryon asymmetry via electroweak sphalerons, with the relation $\eta_B \approx (28/79) \eta_L$ in the SM. Does the $CP^2$ framework use this relation, or does the geometric Chern-Simons mechanism bypass sphalerons? If sphalerons are bypassed, what is the B-violating mechanism?

(c) **Resonant leptogenesis (Appendix D).** Appendix D invokes resonant leptogenesis as an enhancement mechanism. Resonant leptogenesis requires near-degenerate right-handed neutrino masses $|M_2 - M_1| \sim \Gamma_1$. Are the right-handed neutrino masses predicted by the framework (fixed by the compactification), or are they chosen to be near-degenerate to achieve the required enhancement?

---

### Point C2: Proton Mass from Geometry [MEDIUM]

**Location:** Section 6 (proton mass)

**The claim:** $m_p \approx 3\Lambda_{\text{QCD}} \times f(\alpha_s)$ is derived from $CP^2$ geometry with $\Lambda_{\text{QCD}} \approx 190$ MeV run through 13 orders of magnitude by the QCD beta function.

**Interrogate:**

(a) **What "derived" means.** The relation $m_p \approx 3\Lambda_{\text{QCD}}$ is a well-known dimensional analysis result from QCD: the proton mass is set by the confinement scale. The factor of 3 is a rough approximation (the actual ratio $m_p/\Lambda_{\text{QCD}}$ depends on the scheme used to define $\Lambda_{\text{QCD}}$). In what sense does $CP^2$ geometry "derive" this relation? Is the claim that $\Lambda_{\text{QCD}}$ itself is computed from the geometry (without using the experimental $\alpha_s$), or that the dimensional relationship $m_p \sim 3\Lambda_{\text{QCD}}$ is reproduced?

(b) **The factor $f(\alpha_s)$.** The proton mass receives corrections from quark masses and $\alpha_s$ effects: $m_p = 3\Lambda_{\text{QCD}} \times f(\alpha_s, m_u, m_d, m_s)$. Lattice QCD computes $m_p$ from first principles with the $\overline{\text{MS}}$ quark masses and $\alpha_s$ as inputs. What is the function $f(\alpha_s)$ in this paper, and is it computed from the $CP^2$ geometry or from the lattice result?

(c) **$\Lambda_{\text{QCD}} \approx 190$ MeV.** The paper states $\Lambda_{\text{QCD}} \approx 190$ MeV. The scheme-dependent value $\Lambda_{\overline{\text{MS}}}^{(N_f=3)} = 210 \pm 14$ MeV (PDG 2024). Is 190 MeV consistent with this, and which scheme is used in the paper?

---

## Part D: The Holonomy Correspondence

### Point D1: Unifying AB, Higgs, and Confinement via Wilson Loops [LIGHT]

**Location:** Section 8 (holonomy correspondence)

**The claim:** The same geometric object — a Wilson line around a compact internal dimension — produces: (1) Aharonov-Bohm in the U(1) sector, (2) the Higgs mechanism in the SU(2) sector, (3) color flux tubes in the SU(3) sector.

**Interrogate:**

(a) **The mechanism for each sector.** The three phenomena come from three different compact spaces: $S^1$ (U(1)/AB), $S^2$ (SU(2)/Higgs), $CP^2$ (SU(3)/confinement). A Wilson line on $S^1$ has holonomy in U(1); on $S^2$ it has holonomy in SU(2); on $CP^2$ it has holonomy in SU(3)/U(2). These are three different calculations on three different spaces — not "the same geometric object." Is the claimed unification a substantive mathematical theorem (e.g., a single formula that specializes to each case), or a conceptual framing of three separate calculations?

(b) **Distinguishing predictions.** Does the holonomy correspondence make any prediction that is distinct from: (i) the standard U(1) holonomy explanation of AB, (ii) the standard gauge-Higgs unification mechanism, and (iii) lattice QCD confinement? If it reproduces all three without adding anything, it is a reframing, not a derivation.

---

## Part E: §5.7 — The Unified Role of the Leptogenesis Neutrino

### Point E1: One N^{5D}, Three Consequences [HEAVY]

**Location:** §5.7 ("The Unified Role of the Leptogenesis Neutrino")

**The claim:** A single five-dimensional right-handed neutrino $N^{5D}$ with bulk localization parameter $c_\nu = 0.634$ simultaneously produces: (1) the observed baryon asymmetry $\eta_B \approx 6 \times 10^{-10}$ via leptogenesis, (2) the correct dark matter abundance $\Omega_{\text{DM}} h^2 \approx 0.12$ (presumably via the same or a related mechanism), and (3) the neutrino mass ratio $m_\nu/m_{KK} = 5/2$ giving $m_\nu = 49.74$ meV. The paper presents this as a unified consequence of one object, not three separate calculations that share a parameter.

**Interrogate:**

(a) **One object or one parameter?** The claim of unification is strong: one $N^{5D}$ produces three consequences. But "sharing $c_\nu = 0.634$" is precisely "sharing a parameter" — the three calculations are still three separate calculations (leptogenesis, dark matter, Dirac mass) that are evaluated at the same value of $c_\nu$. In what sense is this unification beyond parameter sharing? Exhibit the single equation or the single physical constraint from which all three consequences follow simultaneously — or, if no such equation exists, retract the language of "unification" and replace it with "parameter convergence."

(b) **The dark matter claim.** Dark matter from a right-handed neutrino in extra dimensions is a specific mechanism (KK gravitino, sterile neutrino WDM, or Kaluza-Klein dark matter). Which mechanism produces $\Omega_{\text{DM}} h^2 \approx 0.12$ from $N^{5D}$ with $c_\nu = 0.634$? Is it: (i) the lightest KK mode of $N^{5D}$ as a warm dark matter candidate, (ii) a sterile neutrino mixing via the bulk wavefunction overlap, or (iii) a different mechanism? Exhibit the calculation that gives $\Omega_{\text{DM}} h^2 \approx 0.12$ from $c_\nu = 0.634$ without additional free parameters. In particular: the relic abundance depends on the production rate, which depends on the reheating temperature $T_{\text{RH}}$ and the mixing angle — are these fixed by the compactification or free inputs?

(c) **Consistency of the leptogenesis and dark matter mechanisms.** Leptogenesis from $N^{5D}$ requires $N^{5D}$ to be heavy (typically $M_N \gtrsim 10^9$ GeV for standard leptogenesis, or near-degenerate for resonant leptogenesis). Dark matter from $N^{5D}$ requires it to be light (eV-to-keV for sterile neutrino WDM) or to have suppressed couplings. Can the same $N^{5D}$ with $c_\nu = 0.634$ simultaneously be heavy enough for leptogenesis and produce the correct dark matter abundance? If the leptogenesis mechanism is resonant (Appendix D), the near-degeneracy condition on right-handed neutrino masses must be shown to be compatible with the dark matter abundance. Exhibit this consistency check.

(d) **The baryon asymmetry calculation from $c_\nu$.** §5.7 states that $c_\nu = 0.634$ fixes the baryon asymmetry. The baryon asymmetry from leptogenesis depends on the CP asymmetry $\varepsilon$ in $N^{5D}$ decay, the washout factor $K$, and the sphaleron conversion factor. How does $c_\nu = 0.634$ enter each of these: (i) does it fix the CP asymmetry $\varepsilon$ through the Yukawa coupling structure (and if so, via the same $y = g_2\sqrt{2}$ relation from Paper 4)?, (ii) does it fix the washout factor $K$ through the decay width $\Gamma \propto y^2 M_N$?, and (iii) is $\eta_B \approx 6 \times 10^{-10}$ the result of a full Boltzmann equation solution, or a parametric estimate? If the answer to (iii) is a parametric estimate, the precision implied by the 6-significant-figure match with observation is unjustified.

(e) **The neutrino mass ratio as a third consequence.** The mass ratio $m_\nu/m_{KK} = 5/2$ is described in Paper 4 §7.5.7 as following from the topological decomposition $\chi(CP^2) - c_2^{\text{eff}}/2 = 5/2$. In §5.7 of Paper 5, the same result appears as a "consequence" of $c_\nu = 0.634$. Are these two derivations of the same result, or two different derivations? If they are the same derivation cross-referenced, say so. If they are independent derivations that agree, exhibit both and explain how they are independent.

---

### Point E2: c_ν = 0.634 — Prediction or Cross-Reference? [MEDIUM]

**Location:** §5.7

**The claim:** $c_\nu = 0.634$ is a cosmologically determined bulk fermion localization parameter appearing in Paper 5.

**Interrogate:**

(a) **Provenance: prediction of Paper 5 or import from Paper 4?** The parameter $c_\nu = 0.634$ appears in Paper 4 §7.5.6 in a table alongside $c_t$, $\delta c$, $\Delta c$. Does Paper 5 independently derive $c_\nu = 0.634$ from the leptogenesis/dark matter calculation (i.e., the cosmological constraints alone fix $c_\nu$), or does Paper 5 import $c_\nu = 0.634$ from Paper 4 and then show it is consistent with cosmological observables? These are very different claims. If the former: exhibit the computation from which $c_\nu = 0.634$ is uniquely determined by cosmological data. If the latter: the paper should say clearly that $c_\nu$ is defined by Paper 4 and checked here, not that it is "cosmologically determined."

(b) **What "cosmologically determined" means.** The phrase "cosmologically determined" implies that cosmological observables (baryon asymmetry, dark matter abundance, CMB spectrum) uniquely fix $c_\nu = 0.634$. If two of the three observables are needed to fix $c_\nu$, then the third is a genuine prediction; if all three are inputs, nothing is predicted. How many cosmological observables are used to fix $c_\nu$, and how many are genuine predictions of the model once $c_\nu$ is fixed?

(c) **Precision of $c_\nu = 0.634$.** Is the value 0.634 exact (a mathematical constant, e.g., related to the topology of $CP^2$), or is it a numerical value computed from cosmological inputs with some uncertainty? If $c_\nu = 0.634 \pm \delta c_\nu$, what is $\delta c_\nu$, and how does it propagate to the uncertainty in $m_\nu = 49.74$ meV?

---

### Point E3: m_ν = 49.74 meV in a Baryon Asymmetry Paper [LIGHT]

**Location:** End of §5.7

**The claim:** The neutrino mass prediction $m_\nu = 49.74$ meV appears at the conclusion of §5.7, described as "the sharpest prediction."

**Interrogate:**

(a) **Scope of Paper 5.** Paper 5 is titled (from the file list) as a paper about color confinement, the strong force, and $CP^2$ holonomy. §5.7 appears to import a prediction — $m_\nu = 49.74$ meV — that is the headline result of Paper 4. Is it appropriate for this prediction to appear as the "sharpest prediction" of Paper 5, or should it be: (i) a cross-reference to Paper 4 with a brief mention, (ii) a Paper-5-specific derivation that reaches the same number by a different route (in which case exhibit that route), or (iii) omitted from Paper 5 entirely as out of scope? The referee will flag as a scope problem any prediction that is presented as a result of Paper 5 if it was derived in Paper 4.

(b) **Does §5.7 add anything to the m_ν prediction?** If $m_\nu = 49.74$ meV is derived in Paper 4 from the 5/2 identity and the KK scale, what does §5.7 add? If the answer is "it shows the same number emerges from the leptogenesis/dark matter requirement on $c_\nu$," this is a valuable consistency check — but it should be presented as a check, not as "the sharpest prediction." Clarify the epistemic status of the number's appearance in §5.7.

---

## Output Location

Write your complete review to `integers/paper05-cp2-flux-tubes/journal-reviewer/report.md`.

Structure your report as follows:

1. **Executive summary** — one of: *Accept*, *Minor Revision*, *Major Revision*, or *Reject*. One paragraph of rationale.
2. **Point-by-point findings** — for each interrogation point: your rating (A/B/C), your reasoning, and for A or B, a precise statement of what additional work is required and estimated difficulty (1 paragraph / 1 page / 1 paper).
3. **Recommendation to editors** — a final paragraph with your overall recommendation and the two or three issues most critical to resolve before publication.
