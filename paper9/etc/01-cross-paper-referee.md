# Cross-Paper Consistency Referee: The Complete QG5D Framework (Papers 1–7)

You are an expert referee tasked not with reviewing any single paper, but with evaluating the internal consistency of the complete seven-paper series constituting the QG5D framework. Your job is to find places where Papers 1–7 contradict each other, use each other's results out of scope, make claims in one paper that are undermined by another, or where the dependency chain has logical gaps.

This review is preparation for simultaneous or sequential journal submission of all seven papers. A finding here that two papers are mutually inconsistent may require revising both.

## Research online about these topics before beginning your review

- Cross-paper consistency in multi-paper physics submissions: how journals (JHEP, PRD, CMP) handle series submissions; citation chains between companion papers
- The moduli stabilization problem in string/M-theory: why stabilization must precede all other predictions (cosmological constant, gauge couplings, fermion masses)
- The KK truncation consistency problem: when is it valid to use results from a truncated KK theory in a richer compactification, and when must results be re-derived?
- Leptogenesis and thermal history: how reheating temperature, right-handed neutrino masses, washout factors, and the mirror sector temperature ratio ξ connect across different epochs
- The cosmological constant problem and scale separation: the difficulty of having one compact dimension set the dark energy scale while other compact dimensions set the electroweak and GUT scales
- Inflation model building: how the inflaton identity affects reheating, leptogenesis, and the subsequent thermal history
- The Casimir energy in multi-factor compactifications: whether the Casimir energy of a product space $A \times B \times C$ factorizes, and what determines which factor sets which physical scale
- Weinberg angle and GUT unification: whether $\sin^2\theta_W$ predictions and $\alpha_3 = \alpha_2$ at the GUT scale are mutually consistent constraints

## Your profile

- You are a senior theoretical physicist who has read all seven papers in full.
- You hold each paper to its claims as stated. When Paper 2 says "no free parameters fit to CMB data," you check whether it uses any quantity that Paper 6 derives from a free parameter.
- You track every quantity that appears in more than one paper and verify that its definition and value are consistent across papers.
- You flag circular dependencies: if Paper X uses a result from Paper Y, and Paper Y uses a result from Paper X, both papers may be incomplete as standalone submissions.
- You are not hostile for its own sake. If a cross-paper dependency is valid and the result genuinely transfers, say so and explain why. Your job is to find genuine inconsistencies, not to manufacture them.

## Rationale and strategy

1. Does the finiteness result of Paper 1 actually apply to the geometries used in Papers 4–6?
2. Is the temperature ratio ξ defined and derived consistently in Papers 2 and 6?
3. Is there a single coherent inflation model across Papers 6 and 7, or two incompatible ones?
4. Does Paper 7's Theorem U (R is underivable) undermine the scale separation claimed in Papers 4 and 6?
5. Are the Weinberg angle (Paper 4) and GUT unification condition (Paper 7) mutually consistent?
6. Does the moduli stabilization of Paper 7 come logically before or after the physics of Papers 1–6?

For each point, determine:

- **(A) GENUINE INCONSISTENCY** — the two papers cannot both be correct as stated; one or both must be revised
- **(B) RESOLVABLE TENSION** — the papers are in tension but a clarification or additional calculation would reconcile them; state what is needed
- **(C) CONSISTENT** — the cross-paper dependency is valid as stated; explain why

**Weight guide:** [HEAVY] = 4–5 sub-questions. [MEDIUM] = 3. [LIGHT] = 2.

---

## Literature Context

### Why cross-paper consistency matters more than per-paper correctness

A series of papers that are each internally consistent can still be collectively inconsistent. Common failure modes in multi-paper physics programs:

1. **Parameter recycling.** Paper A derives parameter $X$ from observation. Paper B uses $X$ as a prediction. Together they look like a parameter-free framework, but $X$ was never actually predicted.
2. **Scope creep of results.** Paper A proves result $R$ for geometry $G_1$. Papers B–D cite $R$ for geometry $G_2$. The result may not transfer.
3. **Contradictory derivations of the same quantity.** Papers A and C each derive quantity $Q$ from different methods and get different numbers. Neither paper notices because they don't cross-reference.
4. **Dependency inversion.** Paper B requires Paper C's result $S$ to be established first. But Paper C requires Paper B's result $T$. Neither can be submitted first without assuming the other.
5. **Superseded results left uncorrected.** Paper A makes prediction $P_1$. Paper B supersedes it with $P_2 \neq P_1$. Paper A is not updated and is submitted alongside Paper B with the old prediction.

---

## Files to Read (in order, before writing anything)

Read the abstracts and key sections of all seven papers. Prioritize the sections most relevant to cross-paper claims.

**Paper 1 (finiteness, spin-statistics):**
1. `paper1/00-abstract.md`
2. `paper1/appendices/30-appendix-s-finiteness-theorem.md`
3. `paper1/appendices/22-appendix-k-higher-loop-epstein.md`

**Paper 2 (cosmology, ξ, N_eff):**
4. `paper2/00-abstract.md`
5. `paper2/02-sections-2-to-7.md`
6. `paper2/appendices/09-appendix-e-mirror-baryogenesis.md`

**Paper 3 (black holes, UV completion):**
7. `paper3/00-abstract.md`
8. `paper3/15-appendix-a-non-perturbative-completion.md`

**Paper 4 (SM gauge group, Casimir scales):**
9. `paper4/00-abstract.md`
10. `paper4/06-the-higgs-mechanism-electroweak-symmetry-breaking-.md`
11. `paper4/appendix-C-gauge-coupling-hierarchy.md`

**Paper 5 (confinement, string tension):**
12. `paper5/00-abstract.md`
13. `paper5/03-string-tension-from-geometry.md`

**Paper 6 (thermal history, inflation, dilaton, ξ):**
14. `paper6/00-abstract.md`
15. `paper6/03-inflation.md`
16. `paper6/04-reheating.md`
17. `paper6/06-brane-temperature-asymmetry.md`
18. `paper6/appendix-A-dilaton-freezing.md`

**Paper 7 (G₄ flux, moduli, Theorem U, inflaton):**
19. `paper7/00-abstract.md`
20. `paper7/03-moduli-minimum.md`
21. `paper7/05-inflaton.md`
22. `paper7/appendix-A-theorem-U-star.md`

---

## Part A: The Finiteness Result and Its Scope

### Point A1: Paper 1 Finiteness Applied to Papers 4–6 [HEAVY]

**Papers in tension:** Paper 1 (Appendix S) vs. Papers 4, 5, 6

**The dependency:** Papers 4–6 cite Paper 1's finiteness result (specifically, the Casimir energy being UV-finite to all perturbative orders) to justify computing Casimir energies without UV counterterms. Paper 4 uses the finite Casimir energy of $CP^2 \times S^2$ to derive the Higgs potential. Paper 6 uses the finite Casimir energy of $S^1$ to derive the dilaton potential $V = V_0/\phi^4$.

**Interrogate:**

(a) **Geometry mismatch.** Paper 1's finiteness result (Theorem K.1, Appendix S) is derived for $M^4 \times S^1$: a four-dimensional spacetime times a circle. The relevant geometry is a single compact circle with a single KK tower. Papers 4–6 operate on $M^4 \times CP^2 \times S^2 \times S^1$ — an 11-dimensional compactification with three independent compact factors, each with its own KK tower. Does the Epstein-vanishing theorem of Appendix K generalize from the single-factor $S^1$ Epstein zeta function to the multi-factor Epstein zeta functions arising from $CP^2 \times S^2 \times S^1$? Or does each paper need its own finiteness proof for its own geometry?

(b) **Non-abelian finiteness.** Paper 1's non-abelian extension (Appendix L) extends finiteness to SU(N) gauge theories, but the argument is that the group-theory factors do not spoil the Epstein vanishing. In Papers 4–5, the relevant theory is gravity + SU(3) × SU(2) × U(1) on $CP^2 \times S^2 \times S^1$ with matter fermions. The finiteness of this richer theory (with cross-sector gauge-gravity-matter loops) is not established in Appendix L. Is there a gap?

(c) **The Casimir scale in Paper 4 vs. Paper 6.** Paper 4 claims the Casimir energy of $S^1$ sets the dark energy scale $\Lambda$, while the Casimir energy of $S^2$ sets the electroweak scale $v = 246$ GeV. Paper 6 claims the dilaton potential $V(\phi) = V_0/\phi^4$ is the Casimir energy of the $S^1$. These are the same $S^1$ Casimir energy, but in Paper 4 it is a cosmological constant (not a scalar field potential), while in Paper 6 it is a runaway dilaton potential (not a constant). A constant and a runaway potential are physically very different. Reconcile: is the $S^1$ Casimir energy a cosmological constant, a dilaton potential, or both?

(d) **Finiteness and the Goroff-Sagnotti in 11D.** Paper 1 claims the R³ counterterm vanishes via complementary L-function zeros. This is a 5D statement ($M^4 \times S^1$). In 11D ($M^4 \times CP^2 \times S^2 \times S^1$), the counterterm structure is different (11D SUGRA has a specific one-loop structure). Does the R³ vanishing carry over to 11D? The answer determines whether Paper 4's Casimir energy computation is truly UV-finite or requires the 11D counterterm structure.

(e) **The "exact to all orders" claim.** Paper 6 states $V(\phi) = V_0/\phi^4$ is "exact to all perturbative orders" because Paper 1's finiteness eliminates loop corrections. But Paper 1's finiteness applies to scattering amplitudes, not to the effective potential (Coleman-Weinberg). The effective potential at $n$ loops involves $n$ insertions of the background field — a different object from the $n$-loop scattering amplitude. Does the Epstein-vanishing theorem apply to the effective potential as well as the S-matrix?

---

### Point A2: Paper 3 UV Completion Claims Paper 4 [MEDIUM]

**Papers in tension:** Paper 3 (Appendix A) vs. Paper 4

**The dependency:** Paper 3 (Appendix A, Non-Perturbative Completion) claims the framework is UV-complete via "M-theory identification" — meaning it is embedded in M-theory on $M^4 \times CP^2 \times S^2 \times S^1$, which is the geometry of Paper 4. Paper 3 is submitted (presumably) before or alongside Paper 4, but it cites Paper 4's geometry as its UV completion.

**Interrogate:**

(a) **Logical ordering.** Paper 3's UV completion argument cites a structure that is established only in Paper 4. If Paper 4's chirality mechanism ("metric instabilities") is not established, the 11D M-theory compactification on $CP^2 \times S^2 \times S^1$ does not produce the Standard Model, and the "M-theory identification" of Paper 3 does not actually give the UV completion of a theory with the SM field content. Is Paper 3's UV completion claim contingent on Paper 4 being correct, and is this dependency stated explicitly?

(b) **Non-perturbative stability independently.** Paper 3 (Appendix A) mentions the "bubble of nothing" instability (Witten 1982) as a component of the non-perturbative analysis. The bubble of nothing is an instability of KK compactifications on $S^1$ for bosons with periodic boundary conditions. The e-circle is an $S^1$. Is the bubble of nothing instability addressed in Paper 1 (which establishes the $S^1$ framework), in Paper 3 (which cites non-perturbative stability), or in Paper 7 (which stabilizes moduli)? If addressed in none, this is a gap shared by all three papers.

(c) **What "M-theory identification" commits to.** Claiming the framework is a sector of M-theory commits to all of M-theory's consistency conditions: tadpole cancellation, Freed-Witten anomaly, the correct matter content of 11D SUGRA. Paper 7 addresses tadpole and Freed-Witten for the first time. Does Paper 3's claim that the framework is UV-complete (via M-theory) require Papers 4 and 7 to already be established, making Paper 3 logically dependent on Papers 4 and 7?

---

## Part B: The ξ Parameter Across Papers

### Point B1: Two Derivations of ξ = 0.49 [HEAVY]

**Papers in tension:** Paper 2 vs. Paper 6

**The dependency:** Both Paper 2 and Paper 6 derive or use the temperature ratio ξ = T_hidden/T_visible ≈ 0.49. They give different derivations.

- **Paper 2:** Derives ξ from the observed dark matter-to-baryon ratio: Ω_DM/Ω_b = 1/ξ², observing Ω_DM/Ω_b = 5.36, giving ξ = 0.432 at leading order, refined to ξ ≈ 0.49 with washout corrections.
- **Paper 6:** Claims ξ is "set during reheating by warp-factor-suppressed hidden-brane coupling" — i.e., derived from the brane geometry and the reheating dynamics.

**Interrogate:**

(a) **Are these the same derivation?** Paper 2's derivation of ξ starts from the observed Ω_DM/Ω_b and inverts it. Paper 6's derivation of ξ starts from the warp factor geometry and computes a thermal ratio. If both are correct, they must give the same number (ξ ≈ 0.49) from entirely different inputs. Either (i) the warp factor geometry of Paper 6, when computed, gives ξ = (5.36)^{-1/2} ≈ 0.432 exactly — in which case Paper 6 provides the actual prediction that Paper 2 then verifies — or (ii) Paper 6 gives a formula for ξ in terms of model parameters that are then adjusted to give ξ ≈ 0.49 — in which case ξ is a free parameter in disguise.

(b) **The washout refinement.** Both papers use washout corrections to move ξ from 0.432 to 0.49. Are the washout parameters the same in both papers? The washout factor depends on the effective neutrino mass $\tilde{m}$ and the sphaleron conversion efficiency. If Paper 2 uses one washout model and Paper 6 uses another, the refined ξ values may differ.

(c) **The direction of logical flow.** In the presentation of the series, does ξ flow from Paper 6 (geometric prediction) to Paper 2 (cosmological verification), or from Paper 2 (observational input) to Paper 6 (reheating consistency check)? The two directions imply very different epistemological status. The papers should agree on which direction is primary and state it clearly.

(d) **N_eff and ξ.** Paper 2 predicts N_eff = 3.31–3.39, which depends on ξ through the hidden sector's contribution to radiation: $\Delta N_{\text{eff}} \propto \xi^4$. Paper 6 gives ξ ≈ 0.49 from reheating. Do they give the same N_eff? If Paper 6's reheating gives ξ slightly different from Paper 2's cosmological ξ, the N_eff prediction shifts. Since N_eff is already in 3–4σ tension with ACT DR6, even a small change in ξ matters.

---

## Part C: The Inflation Model Conflict

### Point C1: Dilaton Inflation (Paper 6) vs. G₄ Flux Inflation (Paper 7) [HEAVY]

**Papers in tension:** Paper 6 (Section 3) vs. Paper 7 (Section 5)

**The dependency:** Paper 6 presents dilaton inflation ($n_s = 0.965$, $r = 0.03$) as the framework's inflation model, then states in the abstract that this is "superseded by Paper 7's G₄ flux axion inflaton with $n_s \sim 0.967$, $r \sim 0.001$."

**Interrogate:**

(a) **Reheating is model-dependent.** Paper 6's reheating calculation (Section 4) gives $T_{\text{reh}} \approx 7 \times 10^9$ GeV from "dilaton gravitational decay width." This calculation uses the dilaton as the inflaton. If the inflaton is the G₄ flux axion (Paper 7), the decay width is different (different couplings, different mass), giving a potentially different $T_{\text{reh}}$. Paper 6's reheating must be redone for the G₄ inflaton. Is there a version of Section 4 that gives $T_{\text{reh}} \approx 7 \times 10^9$ GeV for the G₄ axion, or must this number change?

(b) **Leptogenesis efficiency.** Paper 6's non-thermal leptogenesis (Section 5) requires the inflaton to decay to right-handed neutrinos $\phi \to N_i N_i$. The branching ratio depends on the Yukawa couplings of the inflaton to the neutrinos. For the dilaton, this coupling is gravitational (Planck-suppressed); for the G₄ axion, the coupling is through the GVW superpotential derivative. The leptogenesis efficiency $\varepsilon \sim 10^{-6}$ may differ by orders of magnitude between the two inflaton candidates. Does changing the inflaton from dilaton to G₄ axion invalidate the leptogenesis calculation of Paper 6?

(c) **The ξ origin story.** Paper 6 claims ξ is "set during reheating by warp-factor-suppressed hidden-brane coupling." If reheating proceeds differently (G₄ axion decay instead of dilaton decay), is ξ still set by the same warp factor mechanism, or does it depend on the inflaton identity? If ξ changes with the inflaton model, Paper 2's cosmological predictions (which use ξ = 0.49) may be tied to the now-superseded dilaton inflation of Paper 6.

(d) **Which predictions belong to which paper.** Paper 6 should contain the predictions of the current (correct) inflation model. Since the correct model is Paper 7's G₄ axion, Paper 6 should either: (i) defer inflation entirely to Paper 7 and use Paper 7's results for its reheating calculation, or (ii) contain a full dilaton inflation section for reference alongside a revised reheating/leptogenesis section based on the G₄ axion. As currently described, Paper 6 presents a superseded inflation model alongside reheating/leptogenesis calculations that may depend on the superseded inflaton. What is the minimal revision to Paper 6 that makes it consistent with Paper 7?

---

## Part D: Moduli Stabilization and the Ordering Problem

### Point D1: Theorem U and the R-Dependence of Papers 1–6 [HEAVY]

**Papers in tension:** Paper 7 (Theorem U) vs. Papers 1–6

**The dependency:** Paper 7's Theorem U establishes that the observed compactification radius $R_{\text{obs}} \approx 10.1\,\mu$m cannot be derived from the framework's geometric inputs — it requires either a new fundamental scale or environmental selection. Papers 1–6 all use $R$ (or quantities derived from it, such as the KK scale, the dark energy density, and the Casimir energy magnitudes) without specifying its value.

**Interrogate:**

(a) **What Papers 1–6 actually assume.** Papers 1–6 make predictions expressed in terms of $R$ (or equivalently, the KK scale $M_{\text{KK}} = 1/R$). Paper 4 predicts $m_H \approx 125$ GeV "for $M_{\text{KK}} \sim 1$–2.5 TeV." Paper 5 predicts $\sqrt{\sigma} \approx 440$ MeV using $g_3(M_3)$ where $M_3 = r_3^{-1}$. Paper 6 gives $V_0$ in the dilaton potential without specifying its numerical value. Do any of Papers 1–6 make predictions that are fully $R$-independent, or do they all leave $R$ as an implicit free parameter?

(b) **R-independence vs. R-dependence of the GUT prediction.** Paper 7 claims "all observables (gauge group, couplings, neutrino masses, DM ratio, $w_0 = -1$, inflaton) are $R$-independent." But Paper 4's Higgs mass prediction depends on $M_{\text{KK}}$ (which is $r_3^{-1}$, a Kähler modulus related to $R$). Paper 5's string tension depends on $g_3(r_3^{-1})$. If these observables are $R$-independent (as Paper 7 claims), what are their numerical values? If they depend on $r_3$ (not $R$) and $r_3$ is fixed by the flux quantization $n_2/n_1 = -17/9$ (Paper 7), then $m_H$ and $\sqrt{\sigma}$ should be uniquely predicted numbers — what are they?

(c) **Logical ordering: must Paper 7 come first?** If the Kähler moduli $r_2$, $r_3$ are fixed by Paper 7's G₄ flux conditions, then the physical predictions of Papers 4 and 5 (which depend on $r_3$) cannot be made until Paper 7 establishes the moduli. Does the current series present Papers 4 and 5 as if $r_3$ is determined by their own calculations, when in fact it is determined by Paper 7? If so, Papers 4 and 5 should include forward references to Paper 7 for the numerical values.

(d) **The cosmological constant in Paper 4.** Paper 4 assigns the cosmological constant $\Lambda$ to the Casimir energy of $S^1$. Paper 7's Theorem U says $R_{\text{bare}} \approx l_{\text{Pl}}$ (from perturbative considerations) and $R_{\text{obs}} \approx 10.1\,\mu$m (observed). If $R = l_{\text{Pl}}$, the $S^1$ Casimir energy is $\rho_\Lambda \sim 1/R^4 \sim M_{\text{Pl}}^4$ — the Planck density, not the observed $\rho_\Lambda \sim (2.3 \times 10^{-3}\,\text{eV})^4$. If $R = R_{\text{obs}} = 10.1\,\mu$m, the Casimir energy is the observed dark energy. Paper 7 says $R_{\text{obs}}$ requires environmental selection. Does that mean the dark energy prediction of Paper 4 also requires environmental selection — meaning it is not predicted by the framework?

---

## Part E: Gauge Structure Consistency

### Point E1: Weinberg Angle (Paper 4) and GUT Unification (Paper 7) [MEDIUM]

**Papers in tension:** Paper 4 vs. Paper 7

**The dependency:** Paper 4 predicts $\sin^2\theta_W \approx 0.232$ from the $CP^2 \times S^2 \times S^1$ isometry group geometry. Paper 7 predicts $\alpha_3 = \alpha_2$ at the GUT scale from flux quantization $n_2/n_1 = -17/9$. These two predictions must be mutually consistent.

**Interrogate:**

(a) **Consistency of the two predictions.** At the GUT scale, $\alpha_3 = \alpha_2$ (Paper 7) and the SM coupling relations give $\sin^2\theta_W = \alpha_1/(\alpha_1 + \alpha_2)$ where $\alpha_1$ is the U(1) coupling (with GUT normalization $\tilde{\alpha}_1 = (5/3)\alpha_{\text{hypercharge}}$). If $\alpha_3 = \alpha_2$ at the GUT scale and the GUT gauge group is $G_{\text{GUT}} \supset SU(3) \times SU(2) \times U(1)$, then $\sin^2\theta_W$ is determined by the GUT group structure. For SU(5): $\sin^2\theta_W = 3/8 = 0.375$ at the GUT scale, running to 0.231 at $M_Z$. Does Paper 4's geometric prediction of $\sin^2\theta_W \approx 0.232$ assume the same GUT group and running as Paper 7, and do they agree numerically?

(b) **The third coupling $\alpha_1$.** Paper 7 establishes $\alpha_3 = \alpha_2$ from flux quantization. This is two of the three SM couplings. What determines $\alpha_1$ (the hypercharge coupling)? Is it also fixed by the flux, or is it a free parameter? If $\alpha_1$ is free, then $\sin^2\theta_W$ is also free — in tension with Paper 4's claim to predict it geometrically.

(c) **Proton decay consistency.** Paper 4 predicts proton lifetime $\tau_p \sim 10^{34}$–$10^{36}$ years from the GUT scale $M_X \sim 10^{15}$ GeV. Paper 7 fixes the GUT unification condition $\alpha_3 = \alpha_2$ from the flux ratio $n_2/n_1 = -17/9$, which gives the compactification radius ratio $r_2/r_3 = \sqrt{3}/2$. The GUT scale in Paper 7 is $M_X \sim r_3^{-1}$ (the $CP^2$ KK scale). Is the $M_X$ implied by Paper 7's radius $r_3$ (from flux stabilization) consistent with the $M_X \sim 10^{15}$ GeV used in Paper 4 to compute the proton lifetime?

---

## Part F: The Confinement–GUT Scale Connection

### Point F1: Paper 5's $CP^2$ Scale vs. Paper 4's GUT Scale [MEDIUM]

**Papers in tension:** Paper 5 vs. Paper 4

**The dependency:** Both papers use the $CP^2$ KK scale $r_3^{-1}$. Paper 4 identifies $r_3^{-1}$ with the GUT scale $M_X \sim 10^{15}$ GeV. Paper 5 uses $r_3^{-1}$ in the string tension formula $\sigma = (3/8\pi^2) g_3^2(r_3^{-1})/r_3^2$ to predict $\sqrt{\sigma} \approx 440$ MeV.

**Interrogate:**

(a) **Scale consistency.** If $r_3^{-1} = M_X \sim 10^{15}$ GeV (Paper 4), then $\sigma \sim g_3^2(10^{15}\,\text{GeV}) / (10^{15}\,\text{GeV})^2$. At the GUT scale, $\alpha_3 \approx 1/25$, so $g_3^2 \approx 4\pi/25 \approx 0.5$. Then $\sigma^{1/2} \sim \sqrt{0.5}/(10^{15}\,\text{GeV}) \sim 10^{-15}\,\text{GeV}^{-1}$. This is 24 orders of magnitude smaller than $440\,\text{MeV}$, not larger. Either the $CP^2$ scale in Paper 5 is not the same $r_3$ as in Paper 4 (i.e., there are two different $CP^2$ scales), or there is a serious numerical inconsistency. Trace the definition of $r_3$ in each paper and show they are either consistent or different objects.

(b) **Which $CP^2$ Casimir scale.** Paper 4 assigns $CP^2$ → GUT scale and $S^2$ → electroweak scale. If this is correct, the $CP^2$ KK scale is $\sim 10^{15}$ GeV. But Paper 5's string tension is measured at low energies ($\sim 440$ MeV) and is determined by $\Lambda_{\text{QCD}} \approx 210$ MeV, not by any GUT-scale physics. How does the $CP^2$ geometry, which operates at the GUT scale, produce a low-energy quantity like $\Lambda_{\text{QCD}}$? The QCD beta function runs the coupling from the GUT scale to the confinement scale — this running must bridge 13 orders of magnitude, as Paper 5 states. Is this running explicitly performed, and does the result give $\Lambda_{\text{QCD}} \approx 190$–210 MeV from first principles?

---

## Part G: The Mirror Sector Across Papers

### Point G1: Mirror BBN (Paper 6) and the N_eff Prediction (Paper 2) [LIGHT]

**Papers in tension:** Paper 6 (Section 7) vs. Paper 2

**The dependency:** Paper 6 discusses mirror BBN with the temperature ratio ξ = 0.49. The mirror sector contributes $\Delta N_{\text{eff}} \propto (T_\nu^{\text{mirror}}/T_\nu^{\text{visible}})^4 \propto \xi^4$ to the effective number of relativistic species. Paper 2 predicts N_eff = 3.31–3.39 from this contribution.

**Interrogate:**

(a) **Mirror BBN consistency.** Mirror BBN (nucleosynthesis in the hidden sector) produces mirror helium and mirror hydrogen with yields depending on ξ and the mirror baryon-to-photon ratio. If the mirror sector undergoes BBN, it produces mirror radiation (mirror photons, mirror neutrinos) and mirror baryons. Does the mirror BBN affect the visible-sector N_eff calculation of Paper 2, beyond the simple $\xi^4$ contribution? Mirror neutrinos that decouple early may contribute differently from mirror photons that are thermalized.

(b) **The mirror baryon density.** Mirror baryons from mirror BBN contribute to the total matter density $\Omega_m$. Paper 2's CAMB run uses a specific $\Omega_{\text{DM}} h^2$. Is this $\Omega_{\text{DM}}$ purely from dark matter (mirror sector), or does it include mirror baryons? If mirror baryons contribute to $\Omega_{\text{DM}}$, the identification $\Omega_{\text{DM}}/\Omega_b = 1/\xi^2$ (from Paper 2) conflates mirror baryons with dark matter — which is the intended identification, but it should be stated explicitly.

---

## Output Location

Write your complete cross-paper consistency review to `paper9/journal-reviewer/report.md`.

Structure your report as follows:

1. **Executive summary** — an overall assessment of the series' internal consistency. State which cross-paper tensions are genuine inconsistencies requiring revision, which are resolvable tensions requiring clarification, and which are sound dependencies. Conclude with a priority-ordered list of the three most critical issues to resolve before any paper in the series is submitted.
2. **Point-by-point findings** — for each interrogation point: your rating (A/B/C), your reasoning, and for A or B, a precise statement of which papers must be revised, what is needed, and estimated difficulty.
3. **Recommended submission order** — given the logical dependencies identified, what order should the papers be submitted (or revised) to ensure each paper can stand on prior established results? Which papers, if any, cannot be submitted until others are revised?
4. **The parameter audit** — a table listing every quantity that appears in more than one paper (ξ, $r_3$, $M_X$, $T_{\text{reh}}$, $R$, N_eff, etc.), the value used in each paper, and whether the values are consistent.
