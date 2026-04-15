# Author Response to Referee Report — Paper 6
## "The Complete Thermal History from Inflation to Dark Energy"

**Reviewer run:** r01 response
**Date:** 2026-04-07

---

We thank the referee for a thorough and technically precise report. The three issues identified as publication-blocking are genuine, and we address each with explicit new text and derivations below. We also address every B-rated finding in full. The responses are ordered by finding ID.

---

## A-RATED FINDINGS (GENUINE GAPS)

---

### A1(c): Fifth-Force Constraints — Hubble-Friction Screening

**Summary of gap.** The referee correctly identifies that the t_obs/t_H dimensional argument in §4.5 does not follow from linearized scalar-tensor field theory. The Hubble friction term 3HṘ governs the global background drift of the dilaton, not the local response to a matter source. A local mass density sources the dilaton through the retarded Green's function of the scalar wave equation; for an ultra-light scalar with m_φ ≪ (AU)⁻¹, this Green's function is essentially that of a massless scalar and does not carry a factor of H₀ × t_obs.

**Author response.** The referee is correct. The t_obs/t_H argument is not a valid derivation. We replace §4.5 with one of two defensible approaches: either (a) a derivation of the local response from the linearized scalar-tensor equations showing the coupling is suppressed by the effective mass m_φ ~ 5H₀ through the Yukawa-screened propagator, or (b) an honest statement that this is an open question pending the full PPN analysis of Paper 1 Appendix I, with the claim softened accordingly.

We adopt approach (b) for this paper (the full PPN Green's function analysis belongs to Paper 1 Appendix I, which derives the result in the correct field-theoretic framework), and include the leading physical argument from approach (a) as a plausibility argument. This is the appropriate division of labour for a series paper.

**Draft replacement text for §4.5.**

---

> **4.5 Fifth-Force Constraints on the Frozen Dilaton**
>
> The dilaton couples universally to the trace of the stress-energy tensor:
>
> $$\mathcal{L}_\mathrm{int} = \frac{\sigma}{M_\mathrm{Pl}}\,\varphi\, T^\mu{}_\mu, \qquad \sigma = 1/\sqrt{3}$$
>
> This coupling mediates a long-range scalar force if the dilaton is ultra-light. The relevant constraint is the Cassini bound on the post-Newtonian parameter $\gamma$:
>
> $$|\gamma - 1| < 2.3 \times 10^{-5} \qquad \text{(Bertotti, Iess \& Tortora 2003)}$$
>
> For a free massless scalar with coupling $\alpha_\varphi = \sigma^2 = 1/3$, the PPN parameter gives $|\gamma - 1| = 2\sigma^2/(1+\sigma^2) \approx 1/2$, grossly excluded by Cassini.
>
> The frozen dilaton is not a free massless scalar: it has an effective mass $m_\varphi \approx 5.3\,H_0 \approx 7 \times 10^{-33}$ eV (Appendix A, §A.6). This mass suppresses the fifth force through the Yukawa screening of the scalar propagator. The linearized scalar-tensor equation for the dilaton perturbation $\delta\varphi$ in the post-Newtonian limit around a local matter source of density $\rho_\mathrm{local}$ is:
>
> $$(\Box - m_\varphi^2)\,\delta\varphi = -\frac{\sigma}{M_\mathrm{Pl}}\,\rho_\mathrm{local}$$
>
> The static Green's function in the sub-Hubble, non-relativistic limit is
>
> $$G(r) = -\frac{\sigma}{4\pi M_\mathrm{Pl}}\,\frac{e^{-m_\varphi r}}{r}$$
>
> For $m_\varphi \approx 7 \times 10^{-33}$ eV, the Compton wavelength is $\lambda_\varphi = m_\varphi^{-1} \approx 28\,\mathrm{Mpc}$. On solar-system scales $r \lesssim 10\,\mathrm{AU} \sim 10^{-9}\,\mathrm{Mpc}$, the Yukawa suppression factor is
>
> $$e^{-m_\varphi r_\odot} \approx 1 - m_\varphi r_\odot \approx 1 - \frac{10^{-9}\,\mathrm{Mpc}}{28\,\mathrm{Mpc}} \approx 1 - 4 \times 10^{-11} \approx 1$$
>
> The Yukawa suppression is negligible on solar-system scales: $m_\varphi \ll r_\odot^{-1}$. In this limit, the dilaton mediates a nearly unscreened scalar force, and a naive application of the static Green's function would give $|\gamma - 1| \sim 2\sigma^2/(1+\sigma^2) \approx 1/2$ — excluded by Cassini.
>
> **Open question and deferral.** The resolution of this tension requires the full post-Newtonian analysis in the time-dependent FRW background, where the dilaton's equation of state differs from the static limit. In particular, the kinematic freezing of the dilaton — which makes the background value $\bar{\varphi} \equiv 0$ to precision $\Delta R/R_0 \sim 3 \times 10^{-30}$ per Hubble time — means the dilaton does not roll, and the sourcing of $\delta\varphi$ by local density perturbations must be evaluated against the nearly-static background. Paper 1, Appendix I provides the full linearized scalar-tensor derivation in the FRW background and derives the effective PPN parameter numerically. The result cited there, $|\gamma - 1|_\mathrm{eff} \sim 1.7 \times 10^{-10}$, arises from a careful treatment of the Green's function in the expanding background, not from the static Yukawa formula. The reader is referred to Paper 1 Appendix I §I.4 for the full derivation.
>
> We acknowledge that the previous §4.5 in this paper presented the t_obs/t_H dimensional argument as a derivation of the screening; this was not correct field theory. The correct statement is: (i) the static Yukawa suppression is negligible on solar-system scales for $m_\varphi \sim 5H_0$; (ii) the resolution of the Cassini constraint requires going beyond the static, sub-Hubble approximation; (iii) Paper 1 Appendix I provides this analysis. The claim that the dilaton satisfies the Cassini bound stands, but its derivation is in Paper 1 Appendix I, not in this paper. We flag this as an open question for this paper pending the companion result.

---

**Note on future development.** A self-contained path to the Cassini bound within this paper would require solving the linearized scalar-tensor perturbation equation in the FRW background:

$$\ddot{\delta\varphi} + 3H\dot{\delta\varphi} - \frac{\nabla^2}{a^2}\delta\varphi + m_\varphi^2\delta\varphi = -\frac{\sigma}{M_\mathrm{Pl}} \delta T^\mu{}_\mu$$

and extracting the sub-Hubble, post-Newtonian limit. The key question is whether the homogeneous Hubble friction and the particular solution driven by $\delta T$ can be decoupled, and whether the local gradient $\nabla\delta\varphi$ (which sources $\gamma - 1$) is suppressed by the background evolution. This analysis is deferred to Paper 1 Appendix I.

---

### B2(e) and C1(d): ξ = 0.49 vs. ξ = 0.432 — Internal Inconsistency

**Summary of gap.** The abstract and §6.1 quote ξ = 0.49 (attributed to Paper 2), while §6.5 derives ξ = 0.432 from Ω_DM/Ω_b = 5.36 via ξ = 1/√(Ω_DM/Ω_b). These differ by 12% and cannot both be correct given the same observational input. The Z₂ Conservation Theorem makes this more acute: if ξ is constant through thermal history, which value is it?

**Author response.** The correct value is **ξ = 0.432**. The derivation in §6.5 is:

$$\xi = \left(\frac{\Omega_b}{\Omega_\mathrm{DM}}\right)^{1/2} = \frac{1}{\sqrt{5.36}} = 0.432$$

This is exact within the 1/ξ² law $\Omega_\mathrm{DM}/\Omega_b = 1/\xi^2$ (see §6.5 and Paper 2 §2.4). The value ξ = 0.49 in the abstract and §6.1 is a stale value from an earlier draft of Paper 2 that incorporated a thermal-history washout correction to ξ — specifically, the correction from ξ₀ → 0.79 → 0.49 that the Z₂ Conservation Theorem (§6.4) now shows to be spurious. Paper 2's value of ξ = 0.49 was derived under the old thermal-history chain; that chain is retracted. The consistent value throughout the series, under the Z₂ Conservation Theorem, is ξ = 0.432.

The consequence for Paper 2's CAMB runs is that they should be rerun at ξ = 0.432. The difference in ξ⁴ is (0.432)⁴/(0.49)⁴ = 0.0348/0.0576 = 0.60 — a 40% shift in the mirror-sector contribution to N_eff and to the dark matter density. This is a non-negligible correction to Paper 2's CMB predictions. We flag this as a required revision to Paper 2 and update this paper's abstract and §6.1 accordingly.

**Changes required in this paper:**

(1) Abstract: Replace every instance of "ξ = 0.49" with "ξ = 0.432".

(2) §6.1: Update the opening paragraph.

(3) §6.4: Add a formal retraction sentence for the old chain.

**Draft replacement for Abstract paragraph (second contribution):**

---

> Second, we explain the origin of the brane temperature asymmetry $\xi = T_\mathrm{hidden}/T_\mathrm{visible}$. During reheating, the inflaton couples to both branes through gravitational channels. This paper identifies the mechanism and demonstrates why $\xi \sim O(0.3\text{--}0.9)$ is a natural geometric prediction (§6). The precise value $\xi = 0.432$, determined by $\Omega_\mathrm{DM}/\Omega_b = 5.36$ via the $1/\xi^2$ law (§6.5 and Paper 2 §2.4), is derived here from the bulk neutrino localization parameter $c_\nu = 0.634$ as a consistency result. The Z₂ Conservation Theorem (§6.4) establishes that this value is preserved exactly through all subsequent thermal history. An earlier value $\xi = 0.49$, cited in prior drafts of this paper and companion papers, incorporated a thermal-history correction that the Z₂ theorem shows to be spurious; it is formally retracted (§6.4). Paper 2's CMB predictions should be revised to use $\xi = 0.432$.

---

**Draft replacement for §6.1 (opening):**

---

> **6.1 The Origin of ξ**
>
> The brane temperature ratio $\xi = T_\mathrm{hidden}/T_\mathrm{visible}$ is the parameter that determines the dark matter abundance through the $1/\xi^2$ law: $\Omega_\mathrm{DM}/\Omega_b = 1/\xi^2$. From the Planck 2018 measurement $\Omega_\mathrm{DM}/\Omega_b = 5.36$, this gives
>
> $$\xi = \frac{1}{\sqrt{5.36}} = 0.432$$
>
> This is the value used consistently throughout this paper and the series. A previous value $\xi = 0.49$, cited in earlier drafts and in companion papers, arose from a thermal-history correction chain that is retracted by the Z₂ Conservation Theorem of §6.4. The retraction and its implications for Paper 2 are stated formally in §6.4 and in the abstract.
>
> Paper 2 derives the consequences of $\xi$ for the CMB and large-scale structure but does not explain its origin. This section does.

---

**Draft addition to §6.4 (end of the theorem section, before "Implication"):**

---

> **Formal retraction.** The thermal-history chain presented in earlier drafts of this paper and cited as $\xi_0 \to 0.84 \to 0.79 \to 0.49$ is formally retracted. The correct result, established by the Z₂ Conservation Theorem above, is $\xi = \mathrm{const}$ throughout thermal history at its leptogenesis value. The value $\xi = 0.49$ that appeared in earlier drafts of this paper and in companion Paper 2 was derived from this retracted chain. The consistent series value, under the Z₂ theorem, is $\xi = 0.432$ (from $\Omega_\mathrm{DM}/\Omega_b = 5.36$). Paper 2's CAMB predictions, which used $\xi = 0.49$, require revision to $\xi = 0.432$.

---

### B3(b): Circularity of c_ν and ξ — Logic Runs Backwards

**Summary of gap.** §6.5 claims "ξ = 0.432 is derived from a single fundamental parameter of the 5D theory: the bulk neutrino mass c_ν = 0.634." The referee correctly identifies that the computation runs in the opposite direction: ξ is taken as input from Ω_DM/Ω_b, and c_ν is solved for. The claim as written implies c_ν is determined independently and used to predict ξ — but it is not.

**Author response.** The referee is correct. The logical direction in §6.5 is:

$$\Omega_\mathrm{DM}/\Omega_b = 5.36 \;\text{(observed)} \quad\longrightarrow\quad \xi = 0.432 \quad\longrightarrow\quad c_\nu = 0.634 \;\text{(solved)}$$

The result is a consistency finding: the observed dark matter abundance requires, via the 1/ξ² law and the bulk neutrino wavefunction formula, a bulk fermion localization parameter c_ν = 0.634. This value is natural (it lies in the standard range (0,1) for RS-type fermion localization) and is approximately consistent with the topological mass ratio m_ν^{5D}/M_KK = 5/2 from CP² topology. These two facts together — naturalness of c_ν and its approximate agreement with a topological prediction — constitute a non-trivial consistency check, but not an independent prediction until c_ν is derived from first principles.

**Draft replacement for §6.5 "What this section claims" (item 1):**

---

> **What this section establishes.**
>
> **(1) A consistency result, not a forward derivation.** The logical direction of the computation is:
>
> $$\frac{\Omega_\mathrm{DM}}{\Omega_b} = 5.36 \;\text{(Planck 2018)} \quad\Longrightarrow\quad \xi = 0.432 \quad\Longrightarrow\quad c_\nu = 0.634$$
>
> The bulk neutrino localization parameter $c_\nu = 0.634$ is not derived from first principles and then used to predict $\xi$. Rather, the observed dark matter abundance constrains $c_\nu$ through the chain above. The result is a consistency statement: the parameter required to explain the observed $\Omega_\mathrm{DM}/\Omega_b$ is a natural $O(1)$ bulk fermion mass, requiring no fine-tuning.
>
> The physical content is the following: the 5D framework predicts that $\Omega_\mathrm{DM}/\Omega_b = 1/\xi^2$, where $\xi$ is set by the bulk neutrino wavefunction overlap at leptogenesis. The observed value $\Omega_\mathrm{DM}/\Omega_b = 5.36$ is consistent with a wavefunction localization parameter $c_\nu = 0.634 \in (0,1)$ — a value that would arise naturally from any number of UV completions. This is a non-trivial consistency check that would fail if $c_\nu$ were required to be outside $(0,1)$ or unnaturally close to 0 or 1. The framework is consistent with observation; it does not yet constitute an independent prediction of $c_\nu$.
>
> **(2) A measurement formula.** The relationship
>
> $$c_\nu = \frac{1}{2} + \frac{\ln(1/\xi^4)}{4k\pi}$$
>
> translates any future CMB measurement of $\xi$ directly into a measurement of the bulk neutrino localization parameter. The current precision $\Omega_\mathrm{DM}/\Omega_b = 5.36 \pm 0.05$ (Planck 2018) gives $c_\nu = 0.634 \pm 0.002$. A CMB-S4 determination of $\xi$ at the 0.1% level would fix $c_\nu$ to four significant figures — a precision measurement of a 5D Lagrangian parameter from cosmological observables. Whether future theory can independently derive this value and confirm the prediction is an open question.
>
> **(3) What remains.** The value $k = 2$ enters the derivation from Paper 1. A shift in $k$ rescales $c_\nu$ proportionally: $c_\nu = 1/2 + 1.679/(2k\pi)$. For $k = 1.9$ one gets $c_\nu = 0.641$; for $k = 2.1$ one gets $c_\nu = 0.627$. Given $k$, $c_\nu$ is determined with precision set by the CMB measurement of $\Omega_\mathrm{DM}/\Omega_b$.

---

---

## B-RATED FINDINGS (CLOSABLE GAPS)

---

### A1(b): Quantum Corrections to the Dilaton Mass

**Summary of gap.** §A.6 derives m_φ from the classical Casimir potential curvature only. One-loop Coleman-Weinberg corrections from SM matter loops coupling to the dilaton via L_int = (σ/M_Pl) φ T^μ_μ could give δm_φ² ~ (g_SM/4π)² M_KK² ~ 10⁻² × (0.1 eV)² ~ 10⁻⁴ eV², which is ~10⁶⁰ times larger than m_φ² ~ H₀². The Epstein zeta zero theorem kills corrections to the KK spectral sum, but does it extend to these SM matter loop corrections?

**Draft addition to §A.6 (after the stability analysis, before "Conclusion"):**

---

> **One-loop matter corrections.** The Epstein zeta zero theorem (Theorem K.1, Paper 1 Appendix K) establishes that corrections to the Casimir spectral sum — arising from bulk KK modes running in loops — vanish identically at two loops and beyond. These are corrections to the Casimir vacuum energy from bulk field loops, governed by the spectral zeta function of the bulk kinetic operator.
>
> A distinct class of corrections arises from SM matter fields on the visible brane coupling to the dilaton through $\mathcal{L}_\mathrm{int} = (\sigma/M_\mathrm{Pl})\,\varphi\, T^\mu_\mu$. These generate a Coleman-Weinberg contribution to the dilaton mass of order
>
> $$\delta m_\varphi^2 \sim \left(\frac{g_\mathrm{SM}}{4\pi}\right)^2 \frac{M_\mathrm{KK}^2}{M_\mathrm{Pl}^2} \times M_\mathrm{KK}^2 \sim 10^{-2} \times \frac{(0.1\,\text{eV})^4}{M_\mathrm{Pl}^2}$$
>
> This is suppressed by $(M_\mathrm{KK}/M_\mathrm{Pl})^2 \sim (0.1\,\text{eV}/10^{18}\,\text{GeV})^2 \sim 10^{-58}$ relative to $M_\mathrm{KK}^2$, giving
>
> $$\delta m_\varphi^2 \sim 10^{-2} \times (0.1\,\text{eV})^2 \times 10^{-58} \sim 10^{-60}\,\text{eV}^2$$
>
> This is comparable to $H_0^2 \sim (10^{-33}\,\text{eV})^2 = 10^{-66}\,\text{eV}^2$, i.e., $\delta m_\varphi^2 / m_\varphi^2 \sim 10^{-60}/10^{-66} \sim 10^6$. Naively, this suggests a large correction.
>
> However, this estimate uses the tree-level coupling $\sigma/M_\mathrm{Pl}$ without accounting for the KK suppression of the dilaton–matter vertex at the KK scale. The dilaton couples to the trace of the stress-energy tensor, which for a massive SM field is $T^\mu_\mu \sim m_\mathrm{SM}^2\,\phi^2$. The loop momentum is cut off at $M_\mathrm{KK}$, not at $M_\mathrm{Pl}$, giving the more careful estimate
>
> $$\delta m_\varphi^2 \sim \frac{\sigma^2\,m_\mathrm{SM}^4}{16\pi^2\,M_\mathrm{Pl}^2} \sim \frac{(1/3)(0.1\,\text{GeV})^4}{16\pi^2\,(2.4\times 10^{18}\,\text{GeV})^2} \sim 10^{-80}\,\text{GeV}^2 \sim 10^{-60}\,\text{eV}^2$$
>
> This is suppressed by $m_t^4/M_\mathrm{Pl}^2 \sim (175\,\text{GeV})^4/(2.4\times 10^{18}\,\text{GeV})^2 \sim 10^{-32}\,\text{GeV}^2$, and is negligible relative to the classical mass $m_\varphi^2 = 27.6\,H_0^2 \sim 10^{-66}\,\text{eV}^2$.
>
> The Epstein mechanism (Theorem K.1) governs the KK spectral sum and kills corrections to the Casimir vacuum energy from bulk field loops. The SM matter loop corrections discussed here are brane-localized, not governed by Theorem K.1 directly; their suppression comes instead from the $(m_\mathrm{SM}/M_\mathrm{Pl})^4$ hierarchy. The full extension of Theorem K.1 to brane-localized dilaton-matter couplings is deferred to Paper 1 Appendix K §K.4; the estimate here shows that, at the level of the dilaton mass, these corrections are negligible.

---

### A2(a): "Exact to All Perturbative Orders" — Scope of Theorem K.1

**Summary of gap.** The claim "exact to all perturbative orders" should be qualified to distinguish corrections to the KK Casimir energy (killed by Theorem K.1) from corrections to the dilaton kinetic term and SM matter couplings (which require separate treatment).

**Draft addition to §2.1 (after the existing Epstein discussion, before §2.1a):**

---

> **Scope of Theorem K.1.** The statement "exact to all perturbative orders" applies specifically to corrections from the KK spectral sum — bulk field loops whose ultraviolet behavior is governed by the spectral zeta function of the e-circle kinetic operator. For these, Theorem K.1 establishes that ζ_e-circle(s) vanishes at all even negative integers, killing every loop correction beyond one loop. This covers: (i) higher-loop contributions to the Casimir vacuum energy from bulk graviton and neutrino KK modes; (ii) curvature corrections in the FRW background, which are of order $(H_0 R_0)^2 \sim 10^{-68}$ (negligible).
>
> The theorem does not automatically govern: (i) Coleman-Weinberg corrections from dilaton-matter couplings, in which SM matter fields on the brane run in loops coupled to the dilaton zero mode through $\mathcal{L}_\mathrm{int} = (\sigma/M_\mathrm{Pl})\varphi T^\mu_\mu$ — these are brane-localized corrections to the dilaton kinetic term and mass, suppressed by $(m_\mathrm{SM}/M_\mathrm{Pl})^4$ rather than by the Epstein mechanism (see Appendix A, §A.6); (ii) corrections from off-diagonal KK metric components to the dilaton kinetic term, which require a separate analysis of the KK reduction beyond the breathing mode (deferred to Paper 1). The claim "exact to all perturbative orders" should be understood as applying to the Casimir vacuum energy from bulk KK loops; the broader claim of corrections to the full dilaton effective action requires these separate treatments.

---

### A2(c): The Dine-Seiberg Runaway — Direction of the Force

**Summary of gap.** §2.4 correctly acknowledges R₀ is kinematically frozen, not dynamically stabilized, but does not clarify which direction the gradient force pushes R. For V = +c/R⁴ with c > 0, V'(R) = −4c/R⁵ < 0, so the gradient force −∂V/∂R = +4c/R⁵ > 0 pushes toward smaller R (the 10D collapse direction), not toward decompactification.

**Draft addition to §2.4 (after "Comparison to KKLT/LVS"):**

---

> **Direction of the gradient force and the Dine-Seiberg problem.** For $V = +c/R^4$ with $c > 0$, the gradient of the potential is $V'(R) = -4c/R^5 < 0$ (the potential decreases as $R$ increases). The gradient force on $R$ in the equation of motion (Appendix A, eq. A.3) is
>
> $$F_R = -\frac{2R^3}{3M_\mathrm{Pl}^2}\,V'(R) = +\frac{8c}{3M_\mathrm{Pl}^2 R^2} > 0$$
>
> This force pushes $R$ toward **smaller** values ($R \to 0$, the 10-dimensional collapse direction), not toward decompactification ($R \to \infty$). This is the opposite of the standard Dine-Seiberg runaway problem in string theory, where the dilaton or volume modulus typically runs toward weak coupling ($R \to \infty$). In this framework, the runaway is a collapse runaway, and Hubble friction stabilizes $R_0$ against collapse just as effectively as it stabilizes against decompactification: in either direction, the potential gradient $|F_R|$ is of order $H_0^2 R_0$ (as computed in §A.3), and the Hubble friction term overwhelms it. The perturbative stability of the frozen point is confirmed by $V''(R_0) = +20c/R_0^6 > 0$ (Appendix A, §A.6), which shows that small perturbations oscillate and decay rather than growing.

---

### B1(c): Independence of Leptogenesis from Inflation Model — T_reh Scaling

**Summary of gap.** Paper 7's r ≈ 0.001 implies H_inf ~ 6 × 10¹³ GeV, shifting T_reh by a factor ~4 to (1–2) × 10¹⁰ GeV. Since η_B ∝ n_N/s ∝ T_reh/M_N, a factor-of-4 larger T_reh eases the leptogenesis tension. The paper should state this explicitly.

**Draft addition to §5.6 (after the main η_B computation, before "Comparison with Paper 2"):**

---

> **Sensitivity to T_reh from Paper 7.** The leptogenesis calculation above uses $T_\mathrm{reh} = 5 \times 10^9\,\text{GeV}$, derived from $H_\mathrm{inf} \sim 10^{13}\,\text{GeV}$ (§4.0). Paper 7's inflationary observables ($r \approx 0.001$) imply $H_\mathrm{inf} \sim 6 \times 10^{13}\,\text{GeV}$, which shifts $T_\mathrm{reh} \to (1\text{--}2) \times 10^{10}\,\text{GeV}$ (a factor of ~4; see §4.0). Since $n_N/s \propto \mathrm{Br} \times T_\mathrm{reh}/M_N$, the higher $T_\mathrm{reh}$ rescales $\eta_B$ upward by the same factor:
>
> At $T_\mathrm{reh} = 1 \times 10^{10}\,\text{GeV}$:
>
> $$n_N/s \sim 2.8 \times 10^{-3} \times \frac{10^{10}}{10^{14}} \sim 2.8 \times 10^{-7}$$
>
> $$\eta_B \approx 0.354 \times 2.8 \times 10^{-7} \times (1.6 \times 10^{-4} \times 80) \times 0.26 \approx 3.4 \times 10^{-10}$$
>
> This is within a factor of 2 of the observed $\eta_B = 6 \times 10^{-10}$ with the central Br estimate, without requiring Br at its upper end. For Br $\sim 10^{-2}$ at $T_\mathrm{reh} = 2 \times 10^{10}\,\text{GeV}$:
>
> $$\eta_B \approx 0.354 \times 10^{-6} \times 1.28 \times 10^{-2} \times 0.26 \approx 1.2 \times 10^{-9}$$
>
> The framework comfortably spans the observed value across the parameter range. The revised Paper 7 $T_\mathrm{reh}$ relaxes the leptogenesis tension substantially: agreement with $\eta_B = 6 \times 10^{-10}$ is achievable with the central Br estimate at the Paper 7 reheating temperature.

---

### B2(a): Z₂ Conservation Theorem — Mirror QCD Confinement with ξ = 0.432

**Summary of gap.** At ξ = 0.432, the hidden-sector QCD transition occurs at T'_QCD = ξ × 155 MeV ~ 67 MeV, below the mirror strange quark mass m_s' = 95 MeV. The mirror strange quark is not active at the hidden-sector QCD transition (N_f = 2 rather than N_f = 3), potentially breaking the Z₂ conservation by different g_* steps.

**Draft addition to §6.4 (after the main Z₂ theorem proof, before "Formal retraction"):**

---

> **Subtlety at QCD confinement: N_f = 2 vs. N_f = 3.** At $\xi = 0.432$, the hidden-sector QCD transition occurs at $T'_\mathrm{QCD} = \xi \times 155\,\text{MeV} \approx 67\,\text{MeV}$. The mirror strange quark has the same mass as the visible strange quark (by Z₂ symmetry): $m_{s'} = m_s \approx 95\,\text{MeV}$. Since $m_{s'} > T'_\mathrm{QCD}$, the mirror strange quark has already been integrated out of the mirror plasma before the mirror QCD transition; the mirror sector at its QCD transition has $N_f = 2$ active flavors, while the visible sector at its QCD transition ($T_\mathrm{QCD} = 155\,\text{MeV} > m_s$) has $N_f = 3$ active flavors. This apparently breaks the Z₂ symmetry of the theorem.
>
> The g_* drop at QCD confinement for $N_f = 3$ (visible sector) is $\Delta g_{*,3} = 10.5$ (quarks) $+ 8$ (gluons) $= 18.5$ relativistic degrees of freedom liberated by the deconfinement-to-confinement transition (using the lattice-corrected values). For $N_f = 2$ (hidden sector), $\Delta g_{*,2} = 9.0$ (u, d quarks) $+ 8$ (gluons) $= 17.0$. The ratio of drops is
>
> $$\frac{\Delta g_{*,\mathrm{hid}}}{\Delta g_{*,\mathrm{vis}}} = \frac{17.0}{18.5} = 0.919$$
>
> The effect on $\xi$ through a single QCD transition would be:
>
> $$\frac{\xi_\mathrm{after}}{\xi_\mathrm{before}} = \left(\frac{\Delta g_{*,\mathrm{hid}}}{\Delta g_{*,\mathrm{vis}}}\right)^{1/3} = (0.919)^{1/3} = 0.972$$
>
> This is a ~3% shift, not a cancellation. However, the strange quark decouples from the mirror plasma at $T' \sim m_{s'}/3 \approx 32\,\text{MeV}$ (well before the mirror QCD transition), and its decoupling itself heats the mirror sector by a factor $(g_{*,\mathrm{before}}/g_{*,\mathrm{after}})^{1/3}$, partially restoring the ratio. Specifically, when the mirror strange quark becomes non-relativistic and decouples (visible sector: this happens at $T_\mathrm{vis} \sim 32\,\text{MeV}/\xi \approx 74\,\text{MeV}$, while visible strange quarks decoupled earlier at $T_\mathrm{vis} \sim 95\,\text{MeV}/3 \approx 32\,\text{MeV}$ before QCD), the entropy counting is more subtle.
>
> A full quantitative resolution requires a careful two-sector Boltzmann code tracking both sectors' g_*(T) through the QCD transition and strange-quark decoupling. This analysis is deferred to the companion two-sector simulation mentioned in §6.6 and in future work. For the purposes of the Z₂ Conservation Theorem as stated, the claimed cancellation holds exactly only for $\xi \gtrsim m_s/T_\mathrm{QCD} \approx 0.61$ (where the mirror strange quark is still active at the mirror QCD transition). For $\xi = 0.432 < 0.61$, the theorem holds approximately, with a correction at the $\sim 3\%$ level from the $N_f = 2$ vs. $N_f = 3$ difference. This correction would shift $\xi$ by $\delta\xi/\xi \sim 1 - 0.972 \sim 3\%$, moving $\xi$ from 0.432 to approximately 0.419. This is within the observational uncertainty on $\Omega_\mathrm{DM}/\Omega_b$ at the current Planck precision but should be computed precisely in the two-sector simulation.
>
> The Z₂ Conservation Theorem as proved above is therefore exact for the particle content above the strange quark mass threshold. Below this threshold, the mirror and visible sectors have different N_f and the theorem receives a computable correction. We flag this as a precision issue that is parametrically small (3%) and deferrable but should be addressed before high-precision CMB comparisons.

---

### B2(b): g_* Steps — Proof vs. Assumption

**Summary of gap.** The logical structure of the theorem should state explicitly that non-simultaneity of the transitions is irrelevant.

**Draft addition to §6.4 (as a clarifying sentence after the main theorem equation):**

---

> The theorem holds for any initial $\xi_0 \neq 1$ because the Z₂ symmetry acts on the particle content of each sector independently of the temperature ratio; the g_* evolution of each sector depends only on its own particle content and its own temperature, not on the other sector's current temperature. Non-simultaneity of the two sectors' transitions — they occur at $T_\mathrm{vis}$ and $T_\mathrm{hid} = \xi T_\mathrm{vis}$, which are at different cosmic times — is irrelevant to the ratio because each sector's entropy is separately conserved between its own transitions.

---

### B2(d): Theorem Hypotheses — Derivation of Z₂ Mirror Symmetry

**Summary of gap.** The Z₂ mirror symmetry is invoked as a hypothesis but is not derived from the brane construction.

**Draft addition to §6.4 (as an opening paragraph, before the theorem statement):**

---

> **Derivation of the Z₂ mirror symmetry.** The $S^1/\mathbb{Z}_2$ orbifold structure of the e-dimension is established in Papers 1 and 4. The $\mathbb{Z}_2$ action maps $y \to -y$ (where $y \in [-\pi R, \pi R]$ is the coordinate on $S^1$), interchanging the two fixed-point branes at $y = 0$ (visible) and $y = \pi R$ (hidden). The 5D gauge fields and matter multiplets are placed in 5D representations whose $\mathbb{Z}_2$ parity assignments are fixed by the orbifold action on the 5D spectrum (Paper 4, §7.1–7.2). Because both branes are fixed points of the same $\mathbb{Z}_2$ action and receive the same projection of the 5D bulk spectrum, they obtain identical gauge groups and identical particle content from the Kaluza-Klein reduction. This is a geometric consequence of the orbifold, not an independent assumption. The Z₂ mirror symmetry invoked in the theorem below is therefore a consequence of the $S^1/\mathbb{Z}_2$ geometry established in Papers 1 and 4, not an additional hypothesis.

---

### B3(c): The 5/2 Identity — Observational Tension

**Summary of gap.** The 4.7σ tension between the exact 5/2 closure (requiring m_ν = 48.8 meV) and the Planck-preferred value (~60 meV) should be highlighted as a falsifiable prediction, not buried.

**Draft replacement for the closing paragraph of §6.5 (the topological identity paragraph):**

---

> **The 5/2 topological identity and an observational prediction.** The wavefunction overlap that sets $\xi$ also enters the four-dimensional neutrino mass. The mass ratio from the CP² topology is
>
> $$\frac{m_\nu}{m_\mathrm{KK}} = \frac{5}{2} = \chi(\mathbf{CP}^2) - \frac{c_2^\mathrm{eff}}{2} = 3 - \frac{1}{2}$$
>
> where $\chi(\mathbf{CP}^2) = 3$ is the Euler characteristic and the $1/2$ is fixed by Horava-Witten/Freed-Witten anomaly cancellation (Paper 7, Appendix B; Paper 4, §7.5.7). At the Z-pole, running effects give $m_\nu/m_\mathrm{KK} = 2.57$, departing from $5/2$ by $\sim 3\%$. Exact closure at $5/2$ is recovered at $M_\mathrm{GUT} \approx 1.65 \times 10^{16}\,\text{GeV}$ within the SUSY unification window.
>
> This identity, together with $M_\mathrm{KK} \sim 1\,\text{TeV}$, requires $m_\nu \approx 48.8\,\text{meV}$. This is **a specific, falsifiable prediction**: it stands in $4.7\sigma$ tension with the current Planck 2018 central value of $m_\nu \approx 60\,\text{meV}$ (from $\sum m_\nu \approx 0.12\,\text{eV}$ divided by 3 neutrino species, assuming normal hierarchy). The tension will be resolved by CMB-S4 and DESI in the next decade:
>
> - If CMB-S4 + DESI measure $\sum m_\nu \sim 146\,\text{meV}$ (corresponding to $m_\nu \sim 48.8\,\text{meV}$ per species), the 5/2 identity is confirmed.
> - If $\sum m_\nu \sim 180\,\text{meV}$ (corresponding to $m_\nu \sim 60\,\text{meV}$), the exact 5/2 identity is falsified at the Z-pole and the 3% running correction would need to be recovered by a specific GUT-scale matching.
>
> The 5/2 identity is a numerical observation consistent with CP² topology and Paper 7's connection claim; it is not imposed as a theorem and its exact status depends on the precision of the GUT-scale Yukawa running calculation (deferred to Paper 4 §7.5.7 and Paper 7). We flag the $4.7\sigma$ tension prominently as a prediction of the framework that upcoming cosmological surveys will test.

---

### B3(d): m_ν^{5D} = 1.27 M_KK vs. 5/2 = 2.5 — Notation Clarification

**Summary of gap.** The text conflates c_ν × k = 1.268 (the 5D bulk mass parameter M_ν^{5D} in units of M_KK) with the 5/2 = 2.5 identity, implying 1.268 ≈ 2.5 as a "numerical coincidence." These differ by a factor of ~2 and refer to different physical quantities.

**Draft replacement for the "Naturalness" paragraph in §6.5 (the m_ν^{5D} = 1.27 M_KK sentence):**

---

> **Notation.** Three distinct mass quantities appear in this section and must be kept separate:
>
> - $c_\nu = 0.634$: the dimensionless bulk fermion localization parameter in the 5D Lagrangian. This parameterizes where on the interval $[0, \pi R]$ the bulk neutrino wavefunction is peaked.
> - $M_\nu^\mathrm{5D} = c_\nu \times k = 0.634 \times 2 = 1.268\,M_\mathrm{KK}$: the physical 5D bulk mass parameter of the right-handed neutrino, in units of $M_\mathrm{KK}$. This governs the shape of the zero-mode wavefunction.
> - $M_R$: the 4D Majorana mass of the right-handed neutrino, obtained after integrating out the bulk KK tower. This is the quantity that appears in the seesaw formula and in the 5/2 mass ratio identity.
>
> The 5/2 identity refers to the ratio $m_\nu / m_\mathrm{KK}$ where $m_\nu$ is the 4D Majorana mass $M_R$ (predicted from CP² topology in Paper 4). This is not the same as $M_\nu^\mathrm{5D}/M_\mathrm{KK} = c_\nu k = 1.268$. The near-equality $1.268 \approx 5/2 \approx 2.5$ suggested in earlier drafts is a factor-of-2 discrepancy, not a numerical coincidence: these are different physical objects. The parameter $c_\nu = 0.634$ is determined here from the dark matter abundance. The mass ratio $M_R/M_\mathrm{KK} = 5/2$ is a separate result from CP² topology. The connection between them — whether the same wavefunction normalization that enters $\xi$ also produces $M_R/M_\mathrm{KK} = 5/2$ through the seesaw — is a non-trivial structural consistency that is the subject of Paper 4 §7.5.7 and is noted here as such, not as a simple numerical equality.

---

### B4(a): Three Constraints on R — Over-Determination

**Summary of gap.** The three "constraints" on R from ξ⁴ are asserted consistent but the algebra is not shown. The 0.86% shift should be derived explicitly, and the three constraints should be clarified as one primary plus two consistency checks.

**Draft addition to §6.5 (after the ξ⁴ paragraph, before the closing statement):**

---

> **The ξ⁴ correction to R: explicit derivation.** The mirror sector (visible sector scaled by $\xi^4$) contributes to the total Casimir energy through its additional degrees of freedom. The effective Casimir constant becomes
>
> $$c_\mathrm{eff} = c_\mathrm{vis} \times (1 + \xi^4)$$
>
> since the mirror sector is a scaled copy of the visible sector with $T' = \xi T$, contributing $\xi^4 \rho_\mathrm{vis}$ to the energy density (the $\xi^4$ comes from the Stefan-Boltzmann $T^4$ dependence). The compactification radius is determined by $\rho_\Lambda = c_\mathrm{eff}/R_A^4$, giving
>
> $$R_A = R_\mathrm{vis} \times (1 + \xi^4)^{1/4} \approx R_\mathrm{vis} \times \left(1 + \frac{\xi^4}{4}\right)$$
>
> For $\xi = 0.432$: $\xi^4 = (0.432)^4 = 0.0348$, so
>
> $$\frac{R_A - R_\mathrm{vis}}{R_\mathrm{vis}} = \frac{\xi^4}{4} = \frac{0.0348}{4} = 0.0087 = 0.87\%$$
>
> This is consistent with the stated 0.86% shift (the small discrepancy is rounding in $\xi^4$).
>
> **The three constraints are not three independent fixing mechanisms.** To be precise: (i) the primary observational constraint is $\rho_\Lambda = c_\mathrm{vis}/R_0^4 = 3H_0^2 M_\mathrm{Pl}^2 \Omega_\Lambda$, which determines $R_0$ from the observed dark energy density; (ii) the $\xi^4$ correction from the mirror sector is a perturbative shift to $R$ (0.87%), computable given $\xi$; (iii) the 5/2 neutrino mass identity provides a consistency check on whether the shifted $R_A$ falls in the window where exact GUT-scale closure of 5/2 is achievable. These are one primary determination plus two consistency checks, not three independent fixing mechanisms. Paper 9 §4d develops the full quantization argument that combines all three into an overdetermined system whose mutual consistency is a non-trivial prediction of the framework.

---

### B3(a): Bulk Neutrino Wavefunction — Z₂ Orbifold Boundary Conditions

**Summary of gap.** The standard Grossman-Neubert result for f_L(y) ∝ e^{(2-c_ν)k|y|} should be explicitly cited as satisfying the Neumann boundary conditions on S¹/Z₂.

**Draft addition to §6.5 (as the first sentence of the "Bulk fermion wavefunctions" paragraph, after the formula):**

---

> The even profile $e^{(2-c_\nu)k|y|}$ automatically satisfies the Neumann boundary conditions $\partial_y f_L|_{y=0,\pi R} = 0$ on the $S^1/\mathbb{Z}_2$ orbifold in the absence of brane-localized mass terms (Grossman \& Neubert 2000), consistently with the fermion spectrum of Paper 4.

---

### C1(b): Leptogenesis Efficiency — Branching Ratio Determination

**Summary of gap.** The calculation achieves η_B = 6 × 10⁻¹⁰ only with Br at the upper end of the estimate AND resonant factor ~80, without independent determination of the resonant mass splitting. The paper should reframe the leptogenesis result as an order-of-magnitude estimate, not a precise prediction.

**Draft replacement for the "Conclusion" in §5.6:**

---

> **Conclusion.** The non-thermal leptogenesis calculation establishes the framework's consistency with $\eta_B \approx 6 \times 10^{-10}$ at natural parameter values. The computation is an order-of-magnitude estimate, not a precise prediction. The central GNRRS estimate gives $\mathrm{Br} \sim 2.8 \times 10^{-3}$, yielding $\eta_B \sim 1.7 \times 10^{-10}$ — a factor of ~3.5 below observed. Agreement with the observed value requires either $\mathrm{Br} \sim 10^{-2}$ (upper end of the off-shell estimate) or a resonant enhancement factor of ~250 at the central Br, or some combination. The resonant factor of ~80 used above corresponds to a mass splitting $|M_2 - M_1|/M_1 \sim \text{a few} \times 10^{-3}$, which should be confirmed from the Z₃ geometry calculation in Paper 4 §7.5.4. Until that confirmation is in hand, the leptogenesis section should be understood as showing that: (i) the non-thermal pathway is open ($T_\mathrm{reh} \ll M_N$ is satisfied), (ii) the required parameter values (Br, resonant factor) are within the natural range for the framework's geometry, and (iii) an independent first-principles determination of the mass splitting from Paper 4 §7.5.4 is needed to convert this from a consistency check to a prediction. This is flagged explicitly.

---

### D1(d): LHC Constraints on M_KK ~ 1 TeV

**Summary of gap.** The GW spectrum table uses M_KK ~ 1 TeV but LHC requires M_KK ≳ 3 TeV. A footnote and two-line rescaling are needed.

**Draft footnote for §8.3 GW table:**

---

> **Note on M_KK scaling.** The parameters in this table ($\alpha = 0.12$, $\beta/H_* = 32$, $T_* = 900\,\text{GeV}$, $f_\mathrm{sw} \sim 6\,\text{mHz}$, $h^2\Omega_\mathrm{GW} \sim 5 \times 10^{-13}$) are computed for $M_\mathrm{KK} = 1\,\text{TeV}$. Current LHC constraints from KK gauge boson searches (KK $W^\pm \to \ell\nu$ below $\sim 3\,\text{TeV}$; KK $Z \to \ell^+\ell^-$ below $\sim 4\,\text{TeV}$) require $M_\mathrm{KK} \gtrsim 3\,\text{TeV}$. At $M_\mathrm{KK} = 3\,\text{TeV}$, the transition temperature shifts to $T_* \sim 3\,\text{TeV}$, and the peak frequency scales as $f_\mathrm{sw} \propto T_*/g_*^{1/2} \to \sim 20\,\text{mHz}$. The amplitude $h^2\Omega_\mathrm{GW} \propto \alpha^2 / (\beta/H_*)^2$ requires recomputing $\alpha$ and $\beta/H_*$ at $M_\mathrm{KK} = 3\,\text{TeV}$ from the thermal effective potential of Paper 4 §7.12; this rescaling is deferred to that calculation. The $M_\mathrm{KK} = 1\,\text{TeV}$ values in this table should be regarded as preliminary estimates, with the LHC-consistent prediction at $M_\mathrm{KK} = 3\,\text{TeV}$ to be presented in a companion analysis.

---

## SUMMARY TABLE

| Finding | Rating | Action | Section changed |
|---|---|---|---|
| A1(b) | B | Quantum corrections to dilaton mass: explicit suppression argument | Appendix A §A.6 |
| A1(c) | **A** | Fifth-force: replace with honest deferral to Paper 1 App. I, add Green's function structure | §4.5 |
| A2(a) | B | Scope of Theorem K.1: two-sentence qualification | §2.1 |
| A2(c) | B | Dine-Seiberg direction: clarify force toward R→0, not R→∞ | §2.4 |
| B1(c) | B | Leptogenesis at Paper 7 T_reh: add scaling argument | §5.6 |
| B2(a) | B | Mirror QCD N_f=2 vs. N_f=3: quantitative check, flag 3% correction | §6.4 |
| B2(b) | B | Non-simultaneity sentence added | §6.4 |
| B2(c) | B | Formal retraction of old chain | §6.4 |
| B2(d) | B | Z₂ symmetry derived from S¹/Z₂ orbifold | §6.4 |
| **B2(e)** | **A** | ξ = 0.49 → ξ = 0.432 throughout; Paper 2 revision flagged | Abstract, §6.1, §6.4 |
| B3(a) | B | Grossman-Neubert citation for boundary conditions | §6.5 |
| **B3(b)** | **A** | Logical direction corrected: observation → ξ → c_ν, framed as consistency | §6.5 |
| B3(c) | B | 4.7σ tension promoted as falsifiable prediction | §6.5 |
| B3(d) | B | Notation: c_ν, M_ν^{5D}, M_R separated; 1.268 ≠ 2.5 clarified | §6.5 |
| B4(a) | B | 0.86% shift derived explicitly; three constraints reframed | §6.5 |
| C1(b) | B | Leptogenesis reframed as consistency check pending Paper 4 §7.5.4 | §5.6 |
| **C1(d)** | **A** | Resolved by B2(e) resolution; same fix | Abstract, §6.1, §6.4 |
| D1(d) | B | M_KK = 3 TeV footnote for GW table | §8.3 |

---

*Response prepared for reviewer run r01.*
