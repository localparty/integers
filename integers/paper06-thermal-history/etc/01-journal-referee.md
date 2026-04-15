## Before you begin: archive the previous run

Before writing anything, check whether `integers/paper06-thermal-history/journal-reviewer/` contains any
files (report.md, gap-responses.md, or others).

If it does:
1. List the directories in `integers/paper06-thermal-history/reviewer-runs/` (they are named r00, r01, r02, ...).
   If none exist, the next run number is r00.
2. Find the next available number (e.g. if r00 and r01 exist, use r02).
3. Create `integers/paper06-thermal-history/reviewer-runs/rNN/` (e.g. `mkdir -p integers/paper06-thermal-history/reviewer-runs/r02/`).
4. Move all files from `integers/paper06-thermal-history/journal-reviewer/` into `integers/paper06-thermal-history/reviewer-runs/rNN/`.
5. Proceed with the review. Write all new output fresh to `integers/paper06-thermal-history/journal-reviewer/`.

If `integers/paper06-thermal-history/journal-reviewer/` is empty or does not exist, skip directly to the review.

---

# Journal Referee: The Complete Thermal History from Inflation to Dark Energy

You are an expert referee evaluating this paper for submission to Physical Review D or Journal of Cosmology and Astroparticle Physics (JCAP).

## Research online about these topics before beginning your review

- Slow-roll inflation: the slow-roll conditions $\varepsilon \ll 1$, $|\eta| \ll 1$; CMB observables $n_s$ and $r$; Planck 2018 constraints: $n_s = 0.9649 \pm 0.0042$, $r < 0.056$ (Planck+BK18)
- Dilaton in string/M-theory: the dilaton as modulus of the string coupling; its potential; dilaton runaway problem; Dine-Seiberg problem; difficulty of stabilizing at weak coupling
- Moduli stabilization: KKLT (Kachru-Kallosh-Linde-Trivedi 2003); Large Volume Scenario (LVS); Balasubramanian-Berglund-Conlon-Quevedo (2005); why moduli stabilization is hard in string theory; the $F$-term scalar potential
- Reheating after inflation: the decay width of the inflaton; reheating temperature $T_{\text{reh}} \sim (M_{\text{Pl}} \Gamma)^{1/2}$; gravitational reheating; perturbative vs. preheating
- Thermal leptogenesis: Davidson-Ibarra bound $M_N > 10^9$ GeV; efficiency factors; sphaleron conversion; the dependence of $\eta_B$ on $T_{\text{reh}}$ and $M_N$
- Non-thermal leptogenesis: inflaton decay directly to right-handed neutrinos; efficiency $\eta \sim 10^{-3}$; requirements on $M_N$; Giudice-Notari-Raidal-Riotto-Strumia
- Electroweak phase transition (EWPT): the SM EWPT is a crossover (not first-order) for $m_H > 72$ GeV (Kajantie et al. 1996); first-order EWPT requires BSM physics; LISA sensitivity to GW from first-order EWPT
- LISA gravitational wave sensitivity: frequency band 0.1 mHz – 1 Hz; sensitivity to stochastic GW background from first-order EWPT at $T_c \sim 100$ GeV – 1 TeV
- Casimir energy and compactification: the general formula for Casimir energy on $S^1$; its sign (depends on field content); the cosmological constant problem and Casimir energy
- Big Rip and de Sitter futures: quintessence, phantom energy, de Sitter space stability; the fate of the universe for different dark energy equations of state
- Higgs inflation: Bezrukov-Shaposhnikov (2008); the non-minimal coupling $\xi R \Phi^2$; predictions $n_s \sim 0.97$, $r \sim 0.003$; comparison with G₄ flux inflaton
- BBN: the success of standard BBN; constraints on $N_{\text{eff}}$ and exotic energy injection; mirror sector BBN with temperature ratio $\xi$

## Your profile

- You are a cosmologist specializing in inflation and early universe cosmology, with expertise in both analytical and numerical methods.
- You are skeptical of "complete thermal history" papers that string together many separate calculations without showing they are mutually consistent. Your primary concern is internal consistency: does the leptogenesis efficiency in Section 5 use the same $T_{\text{reh}}$ computed in Section 4? Is the $\xi$ from Section 6 the same as in Paper 2?
- You know that the dilaton is the Achilles heel of string-inspired cosmology. The dilaton runaway problem (Dine-Seiberg) and the $\varepsilon \gg 1$ problem (fast roll, not slow roll) afflict most dilaton inflation models. The claim that the dilaton is "frozen by Hubble friction" rather than stabilized by a potential requires careful scrutiny.
- You regard a first-order EWPT at $T_c \sim 1$ TeV as a strong claim: the SM EWPT is a crossover for any Higgs mass above 72 GeV, and producing a first-order transition requires significant BSM physics at the TeV scale. The mechanism must be specified.
- You check whether inflationary predictions are consistent across the paper series: Paper 6 initially presents dilaton inflation with $n_s = 0.965$, $r = 0.03$, then states this is "superseded" by Paper 7's G₄ flux inflation with $n_s \approx 0.967$, $r \approx 0.001$. A referee needs to know which prediction the paper is submitting.

## Rationale and strategy

1. Is the dilaton genuinely frozen by Hubble friction (Proposition A.1), or does this require conditions that are not satisfied?
2. Are the predictions of this paper (inflation, reheating, leptogenesis) mutually consistent with Papers 2 and 7?
3. Is the EWPT genuinely first-order, and what is the mechanism?
4. Is the "complete thermal history" a coherent calculation or a concatenation of separate estimates?

For each point, determine:

- **(A) GENUINE GAP** — invalidates the result or requires major revision
- **(B) CLOSABLE GAP** — can be addressed with additional argument; state what and estimate difficulty
- **(C) SOUND** — correct as stated; explain precisely why

**Weight guide:** [HEAVY] = 4–5 sub-questions. [MEDIUM] = 3. [LIGHT] = 2.

---

## Literature Context

### The dilaton slow-roll problem

Standard dilaton potentials in string theory, including Casimir-type potentials, give a canonical slow-roll parameter $\varepsilon = \frac{1}{2}(V'/V)^2$ that is of order unity or larger when the dilaton is at a generic field value. The paper claims $\varepsilon_{\text{eff}} = 8/M_5^3 \sim 10^{-52}$ from 5D Planck mass suppression. This requires that the 5D Planck mass $M_5$ is enormously large — effectively meaning the kinetic term for the dilaton in the 4D effective theory is suppressed by $M_5^3$. This would be a highly unconventional normalization that must be derived carefully from the dimensional reduction.

### Dilaton "freezing" vs. stabilization

"Freezing by Hubble friction" means the Hubble parameter $H \gg m_\phi$ (dilaton mass), so the dilaton's equation of motion $\ddot\phi + 3H\dot\phi + m_\phi^2\phi = 0$ is overdamped and $\phi$ barely moves. This is the standard mechanism for any light field during inflation. But for the dilaton to remain frozen after inflation (during radiation domination, matter domination, dark energy domination), one needs $m_\phi \ll H(t)$ at all times — which requires the dilaton mass to be lighter than the current Hubble scale $H_0 \sim 10^{-33}$ eV. An ultra-light dilaton is a massless (or near-massless) scalar field, which would mediate a long-range fifth force detectable in equivalence principle tests and Cassini-type experiments. This tension must be addressed.

### The EWPT in the SM and beyond

The SM electroweak phase transition is a smooth crossover (not a phase transition at all) for Higgs masses above 72 GeV (Kajantie-Laine-Rummukainen-Shaposhnikov 1996). The physical Higgs mass is 125 GeV, firmly in the crossover regime. A first-order EWPT at $T_c \sim 1$ TeV requires: (i) new degrees of freedom at the TeV scale that modify the thermal effective potential, or (ii) a non-minimal Higgs sector. The paper must specify which BSM mechanism produces the first-order transition.

---

## Files to Read (in order, before writing anything)

**Core paper:**
1. `integers/paper06-thermal-history/00-abstract.md`
2. `integers/paper06-thermal-history/01-introduction.md`
3. `integers/paper06-thermal-history/02-dilaton-potential.md`
4. `integers/paper06-thermal-history/03-inflation.md`
5. `integers/paper06-thermal-history/04-reheating.md`
6. `integers/paper06-thermal-history/05-non-thermal-leptogenesis.md`
7. `integers/paper06-thermal-history/06-brane-temperature-asymmetry.md`
8. `integers/paper06-thermal-history/07-bbn-and-mirror-bbn.md`
9. `integers/paper06-thermal-history/08-electroweak-phase-transition.md`
10. `integers/paper06-thermal-history/09-matter-radiation-equality.md`
11. `integers/paper06-thermal-history/10-dark-energy-domination.md`
12. `integers/paper06-thermal-history/11-the-future.md`
13. `integers/paper06-thermal-history/12-the-one-page-timeline.md`

**Appendix (required):**
14. `integers/paper06-thermal-history/appendix-A-dilaton-freezing.md`

---

## Part A: The Dilaton

### Point A1: Dilaton Freezing — Proposition A.1 [HEAVY]

**Location:** Appendix A (dilaton freezing)

**The claim:** Proposition A.1 proves the dilaton is frozen despite $\varepsilon = 32/3 \gg 1$. The effective slow-roll parameter is $\varepsilon_{\text{eff}} = 8/M_5^3 \sim 10^{-52}$ from 5D Planck mass suppression. Over the age of the universe, $\Delta R/R_0 \sim 10^{-52}$.

**Interrogate:**

(a) **The normalization of the kinetic term.** The canonical slow-roll parameter $\varepsilon = \frac{M_{\text{Pl}}^2}{2}\left(\frac{V'}{V}\right)^2$ assumes the dilaton has a canonically normalized kinetic term $\frac{1}{2}(\partial\phi)^2$. The claim $\varepsilon_{\text{eff}} = 8/M_5^3$ introduces a suppression from the 5D Planck mass. Show the dimensional reduction explicitly: starting from the 5D action with the Casimir potential, reduce to 4D and identify the canonically normalized dilaton field $\hat\phi$. What is $\varepsilon$ for the canonical field $\hat\phi$?

(b) **Quantum corrections.** The dilaton receives one-loop corrections from all fields coupled to it. In the 4D effective theory, these generate a mass $m_\phi^2 \sim H_0^2$ (from the no-scale structure breaking) or $m_\phi^2 \sim m_{\text{SUSY}}^2/M_{\text{Pl}}^2$ (from gravity mediation). If $m_\phi > H_0 \sim 10^{-33}$ eV today, the dilaton is no longer frozen by Hubble friction and begins to roll, changing $R$ and violating the constancy of Newton's constant. What is the quantum correction to $m_\phi$ in this framework?

(c) **Fifth force constraints.** An ultra-light dilaton ($m_\phi \lesssim H_0$) couples to matter (it modulates the KK scale and hence particle masses) and mediates a fifth force. The Cassini spacecraft (Bertotti-Iess-Tortora 2003) constrains the post-Newtonian parameter $|\gamma - 1| < 2.3 \times 10^{-5}$. Paper 1 (Appendix I) addresses the Cassini fifth force constraint. Is the dilaton in Paper 6 consistent with the bound derived in Paper 1? Quantitatively: what is the dilaton-matter coupling strength, and does it satisfy the Cassini bound?

(d) **Duration of freezing.** Hubble friction freezes the dilaton during inflation and during radiation/matter domination as long as $m_\phi \ll H(t)$. At late times, $H \to H_\infty$ (constant, from dark energy). For the dilaton to remain frozen forever, it needs $m_\phi \ll H_\infty$. But $H_\infty$ is determined by the Casimir energy of $S^1$ itself. Is there a self-consistency check: does the dilaton mass computed from the curvature of the Casimir potential satisfy $m_\phi \ll H_\infty$?

---

### Point A2: The Dilaton Potential $V(\phi) = V_0/\phi^4$ [MEDIUM]

**Location:** Section 2 (dilaton potential)

**The claim:** The dilaton potential $V(\phi) = V_0/\phi^4$ is derived from Casimir energy, exact to all perturbative orders.

**Interrogate:**

(a) **"Exact to all perturbative orders."** Casimir energies are typically computed at one loop. The claim that $V = V_0/\phi^4$ is the exact all-orders result requires showing that higher loop corrections maintain the same functional form. By Paper 1's finiteness theorem, all loop corrections vanish (Appendix S). Does this mean the Casimir energy receives no corrections beyond one loop? If so, "exact to all perturbative orders" follows from Paper 1's finiteness result — but only if that result applies to the curved background relevant here (the cosmological Casimir calculation), not just flat space.

(b) **The sign of the potential.** The Casimir energy can be positive or negative depending on the field content (boundary conditions for bosons vs. fermions). For $V(\phi) = V_0/\phi^4$ to drive inflation (slow-roll on a plateau), $V_0 > 0$. What determines the sign: which fields dominate the Casimir sum, and is $V_0 > 0$ guaranteed by the field content or could it be negative for some parameter choices?

(c) **The Dine-Seiberg problem.** The Dine-Seiberg problem states that in string/M-theory, the dilaton potential vanishes at weak coupling ($\phi \to \infty$), giving a runaway. The potential $V \sim 1/\phi^4$ also vanishes as $\phi \to \infty$ (since $\phi$ is the radius, $\phi \to \infty$ is the decompactification limit). This is a runaway — the minimum is at $\phi = \infty$ (flat extra dimension), not at a finite compactification radius. How is this runaway avoided? What creates a minimum at finite $R$?

---

## Part B: Inflation

### Point B1: Which Inflation Model Is Being Submitted? [MEDIUM]

**Location:** Section 3 (inflation), abstract

**The claim:** Section 3 describes dilaton inflation with $n_s = 0.965$, $r = 0.03$. The abstract notes this is "superseded by Paper 7's G₄ flux axion inflaton with $n_s \sim 0.967$, $r \sim 0.001$."

**Interrogate:**

(a) **Journal submission standard.** A paper submitted to a journal presents its current, correct results. If the inflation model in Section 3 has been superseded, it should not be the primary inflation result of this paper. Either: (i) remove the dilaton inflation calculation and replace it with the G₄ flux result from Paper 7 (requiring Paper 7 to be complete), or (ii) clearly label Section 3 as a historical result that has been superseded, with a forward reference to Paper 7. The current presentation — presenting Section 3 as a result and noting in the abstract that it's wrong — is not acceptable for publication. Recommend how to restructure.

(b) **The $r = 0.03$ prediction.** The original dilaton inflation gives $r = 0.03$. The Planck+BICEP/Keck 2021 bound is $r < 0.036$ (95% CL). The prediction $r = 0.03$ is near the current bound. If this result is kept, it must be compared carefully to the most recent tensor-to-scalar ratio constraints, including BK18 ($r < 0.036$). Is the prediction $r = 0.03$ consistent with current data?

(c) **Consistency across the series.** If Paper 7 provides the correct inflation model, does Paper 6's reheating and leptogenesis calculation depend on whether inflation was driven by the dilaton or by the G₄ flux axion? The reheating temperature and mechanism may differ significantly between the two inflaton candidates. Is the leptogenesis calculation of Section 5 independent of the inflation model, or must it be revised for the G₄ flux inflaton?

---

## Part B2: The Z₂ Conservation Theorem and ξ = 0.432

### Point B2: Z₂ Conservation Theorem — ξ Across the Full Thermal History [HEAVY]

**Location:** §6.4 (Z₂ Conservation Theorem)

**The claim:** A theorem is stated that ξ = T_hidden/T_visible is exactly conserved through the entire thermal history — gravitational thermalization, bulk neutrino decoupling, QCD confinement, and the QCD transition — because the ratio g_*(T)^{hidden}/g_*(T)^{visible} evolves identically in both sectors at every epoch. The old "thermal-history chain" (0.14 → 0.84 → 0.79 → 0.49) is replaced by this conservation theorem.

**Interrogate:**

(a) **Mirror QCD confinement at the same relative temperature.** The theorem requires that the hidden-sector QCD confinement occurs at the same ratio T_hidden/T_visible as visible-sector QCD confinement. Visible QCD confinement occurs at T_c ≈ 155 MeV. Hidden QCD confinement occurs at T_c^{hidden} = ξ × T_c^{visible} ≈ 0.432 × 155 MeV ≈ 67 MeV. For the Z₂ theorem to hold at the QCD transition, the hidden sector must have the same number of quark flavors active at T_c^{hidden} as the visible sector has active at T_c^{visible}. Do both sectors have three light quarks at their respective confinement temperatures? If the mirror up/down/strange masses are not equal to the visible sector's (due to Yukawa hierarchy mirroring), the number of active flavors may differ, breaking the Z₂ symmetry of g_* at the QCD transition.

(b) **g_* steps are identical — but is this proved or assumed?** The proof strategy appears to be: since the hidden and visible sectors are exact mirrors, every g_* step is identical. But the Z₂ symmetry is a symmetry of the Lagrangian, not automatically a symmetry of the thermal history, unless both sectors start at the same temperature. The initial temperature ratio at the end of reheating is set by the warp factor (§6.6), which is ξ₀ ≠ 1. If ξ₀ ≠ 1, then at the epoch of each SM phase transition (EWPT, QCD), the hidden sector is at a different temperature and may have a different number of active degrees of freedom. Show explicitly that g_*(T)/g_*(ξ₀ T) = const(ξ₀) for all T, not just at specific temperatures.

(c) **The old chain vs. the theorem.** The old chain gave a specific numerical trajectory (0.14 → 0.84 → 0.79 → 0.49). The theorem replaces this with ξ = const. These are numerically inconsistent: if ξ were evolving along the old chain, it was not conserved. One of the two must be wrong. Is the old chain formally retracted? Does the theorem show where the old chain calculation erred — specifically, which g_* step was computed incorrectly?

(d) **The theorem's hypotheses.** A theorem has stated hypotheses and a proof. What are the precise hypotheses of the Z₂ Conservation Theorem? If one hypothesis is "the hidden sector has exactly the same gauge group and Yukawa structure as the visible sector," this must be derived from the compactification geometry, not assumed. Paper 6 should either derive the Z₂ mirror symmetry from the brane construction, or state it as an additional input whose consequences the theorem then follows.

(e) **Impact on Paper 2's CAMB runs.** Paper 2 used ξ = 0.49 (not ξ = 0.432) in its CAMB runs. The Z₂ Conservation Theorem justifies using a single epoch-independent ξ, but the theorem does not by itself change the value from 0.49 to 0.432. If the theorem merely confirms that ξ is constant (while Paper 2's CAMB runs already assumed ξ = const = 0.49), there is no conflict. But if §6.3 corrects ξ to 0.432 and asserts the old 0.49 was wrong, Paper 2's CAMB runs must be redone at ξ = 0.432. Which is it?

---

### Point B3: Neutrino Localization and c_ν = 0.634 [HEAVY]

**Location:** §6.5 (Neutrino Localization Mechanism)

**The claim:** The neutrino bulk mass parameter c_ν = 0.634 is derived from ξ = 0.432 and k = 2 via the localization mechanism f(y) ∝ e^{(2-c_ν)k|y|}. The 5D neutrino mass is m_ν^{5D} = 1.27 M_KK. The same wavefunction overlap that sets ξ enters the neutrino mass, giving the 5/2 identity connection.

**Interrogate:**

(a) **The wavefunction formula on a Z₂ orbifold.** The profile f(y) ∝ e^{(2-c_ν)k|y|} is stated for the bulk neutrino. On the $S^1/Z_2$ orbifold, the wavefunction must satisfy Z₂ boundary conditions: either f(-y) = +f(y) (even) or f(-y) = -f(y) (odd). The exponential profile e^{(2-c_ν)k|y|} is automatically even in y, but must it also satisfy Neumann or Dirichlet conditions at the orbifold fixed points y = 0 and y = πR? Show that the boundary conditions are satisfied and that no boundary mass term is required.

(b) **The circularity of c_ν and ξ.** The text derives c_ν from ξ = 0.432. But ξ = 0.432 is derived in Paper 2 from the observed Ω_DM/Ω_b — an observational input, not a prediction. So c_ν = 0.634 is derived from an observation, not from first principles. The paper must be transparent about this. Is c_ν claimed as a "derived" parameter (in which case: derived from what fundamental quantity?) or as a "predicted" parameter (in which case: what is the prediction chain that does not use ξ = 0.432 as input)? The framing that ξ is "derived" from the neutrino localization, when in fact c_ν is derived from ξ, has the logic running backwards.

(c) **The 5/2 identity: Paper 6's claim or Paper 4's?** §6.5 connects the wavefunction overlap to the identity m_ν^{5D}/M_KK = 5/2, and notes the relation 5/2 = χ(CP²) − c₂^{eff}/2. Paper 4 establishes the gauge-Higgs Yukawa mechanism and the 5/2 prediction. Paper 7 establishes Freed-Witten c₂^{eff} = 1/2. Paper 6 is making a connection claim across three other papers. Is §6.5 appropriate for Paper 6 to present this identity as a result, or should it defer entirely to Papers 4 and 7 for the 5/2 computation and merely cite the connection to c_ν? If Paper 6 claims the identity, it must re-derive it — if it cites it, the claim must be hedged appropriately.

(d) **m_ν^{5D} = 1.27 M_KK: how precisely is this computed?** The factor 1.27 ≈ 5/2 × c_ν / (2 − c_ν)... confirm the exact formula. Is 5/2 an approximation that holds for c_ν ≈ 0.634, or an exact identity? The 5/2 identity as stated (from Papers 4 and 7) is exact, not approximate. If the c_ν = 0.634 derivation only gives m_ν^{5D}/M_KK ≈ 1.27 rather than exactly 5/2, this is a discrepancy that must be resolved: is the correct value 5/2 or 1.27, and what determines c_ν — the exact 5/2 or the observational ξ?

---

### Point B4: R-Quantization and the ξ⁴ Correction [MEDIUM]

**Location:** §6.5 (final paragraphs, R-quantization)

**The claim:** ξ⁴ shifts R_A (the compactification radius) by 0.86%. The dark matter sector is one of three constraints on R.

**Interrogate:**

(a) **Three constraints on R — over-determination or consistency?** If R is determined by three independent constraints (Paper 7's Theorem U establishes R is underivable from perturbative geometry; Paper 6 claims the dark matter sector constrains R; a third constraint must come from somewhere), there is a risk of over-determination. Either the three constraints are mutually consistent (and R is fixed to a specific value), or they are inconsistent (and R cannot satisfy all three simultaneously). State the three constraints explicitly and show they have a common solution.

(b) **The 0.86% shift from ξ⁴.** The ξ⁴ correction to R_A is computed from the hidden-sector Casimir energy contribution. Show the computation: what is the coefficient of ξ⁴ in the Casimir energy sum, and why does it shift R_A by 0.86% rather than some other value? Is this shift within the observational uncertainties on R, or does it have observable consequences (e.g., a 0.86% shift in the KK spectrum)?

(c) **Consistency with Paper 7's Theorem U.** Paper 7's Theorem U states that perturbative geometric inputs cannot fix R to the observed value. If the dark matter sector (mirror sector with temperature ξ T) constrains R, is this a perturbative or non-perturbative constraint? If it is perturbative, Theorem U would appear to exclude it. If it is non-perturbative, the claim must be made carefully: what non-perturbative mechanism is invoked?

---

## Part C: Reheating and Leptogenesis

### Point C1: Reheating Temperature and Non-Thermal Leptogenesis [HEAVY]

**Location:** Sections 4–5

**The claim:** $T_{\text{reh}} \approx 7 \times 10^9$ GeV from dilaton gravitational decay width. Since $T_{\text{reh}} < M_N \sim 10^{14}$ GeV, non-thermal leptogenesis proceeds via $\phi \to N_i N_i$.

**Interrogate:**

(a) **The decay width calculation.** The reheating temperature is $T_{\text{reh}} \sim (M_{\text{Pl}} \Gamma_\phi)^{1/2}$ where $\Gamma_\phi$ is the inflaton decay rate. For gravitational decay (Planck-suppressed coupling), $\Gamma_\phi \sim m_\phi^3/M_{\text{Pl}}^2$. What is the dilaton mass $m_\phi$ used in this calculation? Is it the same mass as appears in Appendix A (which is $m_\phi \ll H_0 \sim 10^{-33}$ eV if the dilaton is frozen)? A dilaton with mass $m_\phi \ll H_0$ would give $T_{\text{reh}} \to 0$, not $7 \times 10^9$ GeV. Reconcile.

(b) **Non-thermal leptogenesis efficiency.** In non-thermal leptogenesis, the right-handed neutrinos $N_i$ are produced directly from inflaton decay. The baryon asymmetry is $\eta_B \approx \frac{3}{2} \text{Br}(\phi \to N_i N_i) \varepsilon_i / g_*$ where $\varepsilon_i$ is the CP asymmetry. What is the branching ratio $\text{Br}(\phi \to N_i N_i)$, and is it computed from the model's Yukawa couplings or estimated? The leptogenesis efficiency depends strongly on the ratio $M_N/m_\phi$.

(c) **Washout after production.** Non-thermal leptogenesis requires that the produced lepton asymmetry is not washed out by inverse decays and $\Delta L = 2$ scattering. The washout is controlled by $\tilde{m}_i = (\lambda_\nu \lambda_\nu^\dagger)_{ii} v^2 / M_i$. Are these parameters predicted by the compactification (neutrino Yukawa couplings from the KK zero modes), or are they free? Is the washout factor in the safe regime?

(d) **Consistency with Paper 2's $\xi$ and the corrected value ξ = 0.432.** Paper 2 derives ξ = 0.432 at leading order (from Ω_DM/Ω_b = 5.36) and refines it to ξ ≈ 0.49 with washout corrections. Paper 6 §6.3 states the corrected value is ξ = 0.432 and removes the washout refinement. Paper 6 §6.6 claims ξ is "set during reheating by warp-factor-suppressed hidden-brane coupling." Three different mechanisms now contribute to setting ξ: (i) the dark matter ratio (Paper 2), (ii) the reheating warp factor (Paper 6 §6.6), (iii) the neutrino localization (Paper 6 §6.5). Show that all three give the same numerical value ξ = 0.432. If they agree, state which is the primary derivation and which are consistency checks. If they are three independent routes to the same number, that is a significant self-consistency result that should be emphasized — but must be verified explicitly, not asserted.

---

## Part D: The Electroweak Phase Transition

### Point D1: First-Order EWPT at $T_c \sim 1$ TeV [HEAVY]

**Location:** Section 8 (electroweak phase transition)

**The claim:** The electroweak phase transition occurs at $T_c \sim 1$ TeV and is first-order, producing a LISA gravitational wave signal in the 1–10 mHz band.

**Interrogate:**

(a) **Why first-order?** The SM EWPT is a smooth crossover for $m_H > 72$ GeV. The physical Higgs mass is 125 GeV. For the EWPT to be first-order in this framework, new physics at the TeV scale must modify the thermal Higgs potential to create a barrier between the symmetric and broken phases. What is the specific BSM mechanism? Is it the KK modes of the gauge bosons (coupling to the thermal potential), the Casimir energy of $S^2$ (which sets the electroweak scale), or something else? The mechanism must be computed, not asserted.

(b) **The GW signal amplitude.** The gravitational wave spectrum from a first-order EWPT is characterized by: (i) the phase transition temperature $T_*$, (ii) the ratio $\alpha = \Delta\rho/\rho_{\text{rad}}$ (latent heat), (iii) the inverse duration $\beta/H_*$, (iv) the bubble wall velocity $v_w$. What are the predictions for $\alpha$ and $\beta/H_*$ from this framework, and what is the resulting GW spectrum amplitude $\Omega_{\text{GW}} h^2$ at 1–10 mHz? LISA's sensitivity at 3 mHz is $\Omega_{\text{GW}} h^2 \sim 10^{-11}$. Is the predicted amplitude above this?

(c) **$T_c \sim 1$ TeV vs. the electroweak scale.** The electroweak scale is $v = 246$ GeV, set at $T = 0$ by the Higgs VEV. The critical temperature of the phase transition $T_c \sim v/g \sim 100$ GeV in the SM (before it was determined to be a crossover). The paper claims $T_c \sim 1$ TeV. What in the framework raises $T_c$ to 1 TeV — a factor of 10 above the electroweak scale? Is this the KK scale $M_{\text{KK}}$ setting an effective Higgs mass at high temperature?

(d) **Consistency with LHC constraints.** A first-order EWPT at $T_c \sim 1$ TeV driven by BSM physics at the TeV scale typically leaves signatures at the LHC: new scalar resonances, enhanced Higgs cubic coupling, modified Higgs production cross-sections. What are the LHC predictions of the mechanism responsible for the first-order transition, and are they consistent with current LHC data?

---

## Part E: The Future and Dark Energy

### Point E1: Eternal de Sitter and the Dilaton Future [LIGHT]

**Location:** Sections 10–11 (dark energy, the future)

**The claim:** No Big Rip. The universe approaches eternal de Sitter with $H \to H_\infty < H_0$. The e-circle radius grows without bound but the potential is bounded.

**Interrogate:**

(a) **The de Sitter stability problem.** Pure de Sitter space is believed to be unstable in quantum gravity (the de Sitter swampland conjecture: Obied-Ooguri-Spodyneiko-Vafa 2018; Garg-Krishnan 2019). The conjecture states that de Sitter vacua cannot be metastable in a consistent theory of quantum gravity — all potentials must satisfy $|V'| \geq c V/M_{\text{Pl}}$ or $V'' \leq -c' V/M_{\text{Pl}}^2$. Does the predicted eternal de Sitter state in this framework satisfy or violate the swampland conjecture? If it violates it, does the framework have a response?

(b) **$H_\infty < H_0$.** The claim that the future Hubble rate $H_\infty$ is smaller than the current rate $H_0$ implies the universe decelerates during dark energy domination before reaching the asymptotic state. In $\Lambda$CDM, $H \to H_\Lambda = \sqrt{\Lambda/3}$ from below (asymptotically, $H$ approaches $H_\Lambda$ from below). Is $H_\infty < H_0$ a feature of the specific dilaton potential $V \sim 1/\phi^4$ in the far future, and is it consistent with the dark energy equation of state $w_0 = -1$, $w_a = 0$ (which gives $H \to H_\Lambda$ from below in ΛCDM)?

---

## Output Location

Write your complete review to `integers/paper06-thermal-history/journal-reviewer/report.md`.

Structure your report as follows:

1. **Executive summary** — one of: *Accept*, *Minor Revision*, *Major Revision*, or *Reject*. One paragraph of rationale.
2. **Point-by-point findings** — for each interrogation point: your rating (A/B/C), your reasoning, and for A or B, a precise statement of what additional work is required and estimated difficulty (1 paragraph / 1 page / 1 paper).
3. **Recommendation to editors** — a final paragraph with your overall recommendation and the two or three issues most critical to resolve before publication.
