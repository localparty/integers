# §08 — Dyson-Schwinger Equations + Transseries (Klaczynski 2016)

*Klaczynski's framework combining Dyson-Schwinger equations with resurgent transseries. Truncated studies. Non-perturbative saddle-point contributions. What it contributes to Route A.*

---

## 8.1. Dyson-Schwinger equations in QFT

The Dyson-Schwinger equations (DSE) express the full non-perturbative Green's functions of a QFT as solutions of an infinite hierarchy of coupled integral equations:

$$
G(p) \;=\; G_0(p) + G_0(p)\, \Sigma[G]\, G(p),
$$

where $G$ is the full propagator, $G_0$ the bare, and $\Sigma[G]$ the self-energy as a functional of the full Green's functions. The hierarchy generalizes to higher $n$-point functions.

DSE are **exact** in the formal power-series sense — order-by-order, they reproduce the perturbation expansion — but they admit **non-perturbative solutions** that perturbation theory does not see. These correspond to fixed points of the DSE that are not analytic at $g = 0$.

The DSE viewpoint: rather than sum Feynman diagrams, treat the Green's functions as solutions of integral equations whose structure may admit multiple branches. The non-perturbative branches are the "hidden" physics.

---

## 8.2. Klaczynski's 2016 framework

Klaczynski (2016) — building on earlier work by Kreimer, Bergbauer, and Weinzierl — developed a framework for combining DSE with resurgent transseries. The framework's core ideas:

**Idea 1: DSE in Mellin space.**
Rewrite DSE in terms of Mellin-transformed Green's functions. The non-perturbative structure becomes cleaner: singularities of the Mellin-transformed DSE correspond to non-perturbative sectors.

**Idea 2: Transseries ansatz for DSE solutions.**
Postulate that Green's functions admit transseries expansions
$$
G(g) \;=\; G^{(0)}(g) + \sigma_1 e^{-A_1/g^2}\, G^{(1)}(g) + \sigma_2 e^{-A_2/g^2}\, G^{(2)}(g) + \cdots
$$
with each $G^{(k)}$ itself an asymptotic power series. Substitute into the DSE hierarchy.

**Idea 3: The non-perturbative sector equations.**
Substitution yields a *hierarchy* of equations: the perturbative sector $G^{(0)}$ satisfies the usual DSE; each non-perturbative sector $G^{(k)}$ satisfies a *linearized* DSE around $G^{(0)}$, with forcing from lower sectors. The non-perturbative sector equations are *computable* given the perturbative sector.

**Idea 4: Stokes constants from the DSE.**
The Stokes constants that govern the transseries parameters appear naturally as coefficients in the non-perturbative sector equations. In truncations, they can be computed explicitly.

---

## 8.3. What Klaczynski proves (in truncation)

Klaczynski's results are for *truncated* DSE — specifically, a scalar model with a tree-level DSE approximation. In this truncation:

- The Borel transform of the perturbative sector has explicitly computable singularities.
- The non-perturbative sectors satisfy linear integral equations whose solutions are explicit.
- The Stokes constants are rational numbers expressible in terms of anomalous dimensions.
- The transseries parameters can be *fixed* by imposing boundary conditions at $g \to 0$.

The truncation is not the full QFT — it omits higher-loop contributions and neglects the full coupled hierarchy — but it demonstrates that **DSE + transseries is a consistent framework** in which the non-perturbative structure is computable.

---

## 8.4. Non-perturbative saddle-point contributions

A central result: the non-perturbative sectors in the DSE framework correspond to **saddle points of the effective action** that are not visible to perturbation theory.

For YM, these saddles include:
- **Instantons** (BPST, $A_k = 8\pi^2 k$) — known since 1975.
- **Instanton-anti-instanton molecules** ($A = 2 \times 8\pi^2 = 16\pi^2$ and fractional factors) — Zinn-Justin analysis.
- **Bions / fractional instantons on compactified space** ($A = 8\pi^2/N$ on $\mathbb{R}^3 \times S^1$) — Unsal, Dunne-Unsal 2012.
- **IR renormalon saddles** ($A_k = 2k/\beta_0$) — these are the ones relevant for Route A's IR-renormalon obstruction.

Klaczynski's framework accommodates *all* of these saddles as non-perturbative sectors. The key computational content: given the perturbative series, the framework predicts *which* saddles contribute and *how much* (Stokes constant) they weight.

For 4D YM, the full hierarchy has not been solved — only truncations. But the framework suggests that the transseries structure of YM Green's functions is *computable* once one commits to a specific truncation scheme.

---

## 8.5. Truncated DSE vs. the full theory

The key limitation of Klaczynski's results: truncation. A truncated DSE is *not* the full YM theory. The concern: transseries computed in truncation may not match the transseries of the full theory.

Counterarguments:

**Paper 10 scheme independence (relevant).** The leading renormalon positions $t_k = 2k/\beta_0$ are scheme-independent (depend only on $\beta_0$, one-loop). These are the *universal* content of the transseries; they should survive truncation.

**Transseries rigidity.** Once the non-perturbative sector structure is fixed (instanton + IR renormalons at known actions), the coefficients $\sigma_k$ are constrained by consistency. Truncation affects the *higher-order* coefficients within each sector but not the *number* and *location* of sectors.

**2D YM complete analysis (§9).** In 2D YM, the full DSE is exactly solvable (Migdal recursion), and the transseries is computable *without* truncation. The 2D result confirms that the truncated DSE + transseries framework captures the correct non-perturbative structure.

In 4D YM, the full DSE is *not* exactly solvable. Klaczynski's framework remains a partial computational tool; extending to the full theory requires additional input. The ITPFI-based refinement (§10) is proposed as this additional input for the programme.

---

## 8.6. What Klaczynski contributes to Route A

Klaczynski 2016 provides Route A with:

1. **A computational template:** DSE + transseries ansatz + linearized non-perturbative sector equations. This gives a concrete way to write down what the transseries parameters should satisfy.

2. **Truncated explicit results:** in a simplified model, the Stokes constants and transseries parameters are computed. This demonstrates the framework is *non-vacuous* — the computations terminate with definite answers.

3. **Extension to gauge theories.** Klaczynski (following Kreimer 2000s, van Suijlekom 2007) developed DSE-in-Hopf-algebra machinery that accommodates non-abelian gauge structure. The transseries framework extends to gauge-fixed YM.

4. **A concrete obstruction to closure in 4D.** The framework's failure in full 4D YM is not a *conceptual* failure; it is a *computational* failure — the full DSE is not solvable. This is a well-defined technical wall, not a hidden deficiency.

Route A inherits from Klaczynski's framework the **computational form of the transseries**: given the perturbative coefficients $a_n$ and the DSE structure, the non-perturbative sectors $G^{(k)}$ satisfy explicit linearized DSE whose solutions are in principle computable.

---

## 8.7. Where the programme-internal tools enter

Klaczynski's framework has a free-parameter problem: the transseries parameters $\sigma_k$ are not fixed by the DSE alone. In truncations, they are fixed by boundary conditions (e.g., $g \to 0$ asymptotics). In the full 4D YM case, the boundary conditions need to be supplied externally.

The programme's candidate externally-supplied boundary conditions:

- **OS positivity** (Paper 8 Link 16): the Schwinger functions $S_n$ are reflection-positive. Translated to transseries: the coefficients $\sigma_k$ must be such that $\mathrm{Re}[f_+(g)] + \sum \sigma_k e^{-t_k/g^2} \phi_k(g)$ is a reflection-positive distribution in the $x$-variables.

- **Cluster decomposition** (Paper 8 Link 16): the Schwinger functions cluster at large separation. Translated to transseries: the long-distance expansion of $\mathcal{O}^{\mathrm{NP}}$ must match the expected asymptotic behaviour, which constrains the $\sigma_k$.

- **Paper 10 scheme independence:** the *physical* content of the transseries (e.g., the gluon condensate value $\langle \mathrm{Tr}(F^2)\rangle_\Lambda$) is scheme-independent; this pins down a linear combination of the $\sigma_k$.

- **ITPFI factorization** (§10): the scale-local structure of the programme's vacuum algebra constrains the $\sigma_k$ to have a product-over-scales form. This is the programme's most novel input.

Together, these constraints should fix the transseries parameters uniquely — or at least reduce them to a finite-dimensional family that can be pinned down by matching to lattice QCD data.

---

## 8.8. The honest gap

Klaczynski's framework is a computational scheme, not a closed theorem. The specific gaps for 4D YM:

**Gap 1: Full DSE solvability.** The full 4D YM DSE hierarchy is not solved. Truncated DSE gives partial results; the full hierarchy's transseries structure is conjectured but not proven.

**Gap 2: Transseries parameter determination.** Even in Klaczynski's truncation, the transseries parameters are fixed only up to physical inputs. For 4D YM, the physical inputs (OS positivity, cluster decomposition, scheme independence, ITPFI) must be shown to suffice.

**Gap 3: Convergence of the full transseries.** The transseries is a formal object; demonstrating that it converges to an actual distribution (not merely a formal power series) requires additional analytic work. Resurgence theory handles this for ODEs; for 4D YM, it is open.

**Gap 4: Matching to Paper 8 Schwinger functions.** Even if the transseries is well-defined, showing it equals the Paper 8 Link 16 Schwinger functions $S_n$ requires an identification argument. This is H4 itself.

These gaps are real. Klaczynski 2016 closes *some* of them for truncations; Route A aims to close them for full 4D YM using the programme's additional structure.

---

## 8.9. Summary

Klaczynski 2016:

- Combined DSE with resurgent transseries in a computational framework.
- Proved transseries consistency in truncated models.
- Identified non-perturbative sectors with DSE saddle points (including IR renormalon sectors).
- Provided a concrete extension to gauge theories via DSE-Hopf-algebra.

Route A's use:
- Klaczynski gives the *structural template* for the transseries.
- The transseries parameters are fixed by physical inputs from the programme (OS, cluster, scheme, ITPFI).
- The gaps (full DSE solvability, convergence, matching to $S_n$) remain as Route A's main technical content.

§09 examines the 2D YM case where the full transseries IS computable, providing a template. §10 introduces the ITPFI-based refinement that may fix the free parameters. §11 gives the full Route A proof sketch.

---

*Paper 50 §08. Drafted 2026-04-14. G Six and Claude Opus 4.6.*

*Key references: Klaczynski 2016, Resurgent analysis of Ward-Schwinger-Dyson equations; Kreimer 2000, Knots and Feynman diagrams; van Suijlekom 2007, Renormalization of gauge fields via Hopf algebras; Dunne-Unsal 2012, Resurgence and trans-series in quantum field theory.*
