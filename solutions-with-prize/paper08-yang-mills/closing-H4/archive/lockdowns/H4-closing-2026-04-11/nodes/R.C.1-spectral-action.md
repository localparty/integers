# R.C.1 — Spectral action + Identity 12 + bridge family k=4 (W1-C1 Author output)

*Wave 1, slot W1-C1, node R.C.1. Author: Claude Opus 4.6 (1M context). Date: 2026-04-11.*
*6-step inner loop executed with maximum reasoning. Verification discipline applied: Connes 1996 and Chamseddine-Connes 1996 consulted at primary-source level (see §Step 5.5).*

---

## Direction

Route C: framework-native closure of H4 via Connes' spectral action principle, Identity 12 (e-circle ↔ Bost-Connes unitary equivalence), and bridge family k=4 at (3,13) Pati-Salam. Claim to test: the Seeley-DeWitt $a_4$ coefficient, computed on the BC sub-algebra carrying the bridge family k=4 structure, produces the running coupling $g(\mu)$ matching $\beta_0 = 11N/3$ with the $(\ln)^{-2}$ correction following from the trace-anomaly identity $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$, so that H4 becomes a theorem of the framework structure.

## Framework tools used

**Always-read** (full, end to end):
- `paper12/research/214-the-method-six-patterns.md` (Six Patterns method, in particular Pattern 5 on zeta regularization of KK towers)
- `paper12/27-anchor-document.md` (CBB system, bridge table, 36-entry master table, Identity 12 as Axiom 5 closure)
- `paper12/relaxation/04-geometric-spectral-cross-formula-...-strategy.md` (anchor-not-Clay-bundle doctrine; the seven anchors framework)
- `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` (the canonical ORA bypass template: find a single algebraic object that reframes an open gap as an expectation of an already-present element)

**Route C-specific, loaded**:
- `paper12/research/162-bridge-cocycle-step6.md` (k=3 bridge cocycle equality, `inv_5(A_arith) = 1/3 mod Z`)
- `paper12/research/179-bridge-3-13-pati-salam.md` (k=4 bridge at (3,13), `inv_3(A_arith) = 1/4 mod Z`, four minimal projections = Pati-Salam colours, α_PS⁻¹ = 52/3 ≈ 17.33)
- `paper12/research/04-identity-12-rigorous.md` (Identity 12 theorem: unitary $U: H_e \to H_1^{(\mathbb{N}^*)}$, $U T_e U^* = H_{BC}$, $U D_n U^* = \mu_n$, $U E_r U^* = e(r)$)
- **Chamseddine–Connes 1996** "The Spectral Action Principle" (arXiv:hep-th/9606001) — primary source, web-fetched
- **Connes 2007** "Noncommutative geometry and the spectral model of space-time" (Séminaire Poincaré X, 179–202) — Connes' own review of the CC 1996 spectral action principle, read at primary source (webfetched PDF, pages 1–12 inspected)
- **Vassilevich 2003** "Heat kernel expansion: user's manual" (Phys. Rept. 388, 279) — primary source, web-fetched, pages 1–8 and 33–45 read for §4.1 general formulae and §4.2.1 Yang-Mills in flat space

**H4 context, loaded**:
- `paper08-yang-mills/preprint/PROOF-CHAIN.md §IV.1–§IV.5` (Step 18 is conditional on H4; Steps 1–17 unconditional)
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4b-af-short-distance-match.md` (the target: $\langle \mathrm{Tr}\,F^2(x)\mathrm{Tr}\,F^2(0)\rangle \sim C_N|x|^{-8}(\ln 1/|x|\Lambda)^{-2}$, $C_N = 2(N^2-1)/\pi^6$)
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md` (the OPE structural requirement, at most 10–15 % closable without new mathematics)
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md` (W7-14 reframing of H4 to the mildest available form via gradient-flow controlled interpolation; §2.2 already cites the Spiridonov–Chetyrkin trace-anomaly identity; §6 already cites Vassilevich (hep-th/0306138) for the $a_4$ mass-independence used in the KK decoupling argument)
- `paper08-yang-mills/closing-H4/blackboard.md` (master dictionary; Wave 1 dispatch)

## Research

### Step 1 — DIAGNOSE

**Why is H4 hard in the current framing.** H4 is the statement that the non-perturbative Schwinger function of $[\mathrm{Tr}\,F^2]_R$ admits a short-distance asymptotic expansion whose leading term is the perturbative AF prediction $C_N|x|^{-8}(\ln)^{-2}$. In the preprint (Step 18, Lemmas 4.2–4.3 of Appendix L), the coupling $g(\mu)$ and the running law (1.8) are treated as external input: the AF prediction is *stated* in (2.5) and *asserted* to match the renormalized Schwinger function under H4. The preprint does not *construct* $g(\mu)$ from the framework's own structure; it imports $g(\mu)$ from continuum perturbation theory (Luscher 2010, Harlander–Neumann 2016) and asks whether the non-perturbative Schwinger function agrees.

**The phenomenon in a fuller description.** The route C brief hypothesises that the AF structure is *already present* in the framework: the Connes spectral action principle would produce the action of any noncommutative geometry from the heat-kernel expansion $\mathrm{Tr}\,f(D/\Lambda)$; applied via Identity 12 to the YM construction, the Seeley–DeWitt $a_4$ coefficient would "automatically reproduce the leading short-distance behaviour of the underlying QFT correlators, with the running coupling $g(\mu)$ emerging from the heat-kernel coefficient $a_4$." If this were true, H4 would collapse: $g(\mu)$ would be a consequence of the framework, not an imported input.

**The diagnostic question.** Does the Connes spectral action actually produce a *running* $g(\mu)$ from $a_4$, or only a *bare* coupling at the cutoff scale $\Lambda$ that must then be matched to experiment and run down by standard perturbative RG? This is where the brief's paraphrase must be verified against primary source before any further work is done.

### Step 2 — REINTERPRET (BC sub-algebra + bridge family)

**The intended reinterpretation.** The brief proposes: the difficulty dissolves on the BC sub-algebra with bridge-family structure, where the running coupling is a consequence of the Seeley–DeWitt expansion rather than an external input. Concretely:

1. **Identity 12** gives a unitary $U : H_e \to H_1^{(\mathbb{N}^*)}$ intertwining the e-circle scaling generator $T_e = \log(R\hat p_e)$ with the BC Hamiltonian $H_{BC} = \log \hat N$ and the dilation isometries $D_n$ with the BC isometries $\mu_n$. In particular, the e-circle lives inside the $\beta = 1$ KMS ground state of the Bost–Connes C*-dynamical system.

2. **Bridge family k=4 at (3,13)** provides a Z/4Z grading on the BC sub-algebra: the four cosets $C_a = \{C_0, C_1, C_2, C_3\}$ of $\ker(\mathrm{Frob}_3)$ in $(\mathbb{Z}/13\mathbb{Z})^*$, identified with the four Pati–Salam minimal projections $(\ell, r, g, b)$. The SU(3)$_c$ quark colour rotates within $C_1, C_2, C_3$; the $\ell \leftrightarrow r,g,b$ permutation is the Z/4Z carry cocycle $c_\text{op}(\tau^i, \tau^j) = i^{\lfloor (i+j)/4\rfloor}$.

3. **Seeley–DeWitt $a_4$ on this sub-algebra** is to be computed from the spectral action $\mathrm{Tr}\,f(D_\mathrm{YM}/\Lambda)$ of a Dirac operator $D_\mathrm{YM}$ whose inner fluctuations (in the sense of Connes' $D \mapsto D_A = D + A + \varepsilon' J A J^{-1}$) carry the SU(N) gauge connection, with the Z/4Z / Pati–Salam structure as the noncommutative finite space.

4. **Extraction of $g(\mu)$**: the coefficient of $\mathrm{Tr}\,F^2$ in the $a_4$ integrand, matched to the standard YM kinetic term $-\frac{1}{4g^2}\mathrm{Tr}\,F^2$, defines a coupling; the brief claims this coupling *runs* with $\Lambda$ in such a way that the one-loop $\beta_0 = 11N/3$ is reproduced structurally.

**The rigorous Vassilevich input.** From Vassilevich 2003 eq. (4.34), verified at primary source (p. 41):

$$a_4^{[\mathrm{tot}]}(1, D_\mathrm{YM}) \;=\; a_4^{[\mathrm{vec}]} - 2\,a_4^{[\mathrm{gh}]} \;=\; \frac{11}{96\pi^2}\int_M d^4 x\,\sqrt{g}\,F^{\delta}_{\rho\nu}F^{\gamma}_{\rho\nu}\,K_{\delta\gamma}$$

with $K_{\delta\gamma} = c^\delta_{\alpha\beta}c^\gamma_{\alpha\beta}$ the Killing form of the gauge algebra. For the adjoint representation of SU(N), $K = 2N \cdot \delta_{\delta\gamma}$, so the coefficient of $\mathrm{Tr}(F^{\mu\nu}F_{\mu\nu})$ in $a_4^{[\mathrm{tot}]}$ is

$$a_4\text{-coeff}[\mathrm{Tr}\,F^2] \;=\; \frac{11}{96\pi^2}\cdot 2N \;=\; \frac{11 N}{48\pi^2}.$$

Vassilevich adds, verbatim (p. 41): *"We also recover the coefficient 11/3 which is familiar from computations of the Yang–Mills beta functions."* The $11/3$ of $a_4$ is **precisely the $\beta_0/N = 11/3$ of the one-loop YM beta function**, and this identification is not a framework novelty — it is a textbook 1979-era result from the DeWitt–Christensen–Duff heat-kernel computation.

This is the invariant we would want to "lock in" on the BC sub-algebra as the step-4 LOCK. But before locking, step 5.5 must be executed — because the brief's paraphrase of what this invariant *means* (a running $g(\mu)$) is the load-bearing claim, and it must be verified against primary source.

### Step 3 — UNIFY (Connes spectral action as canonical template)

The spectral action principle (Chamseddine–Connes 1996; Connes 1996; Connes–Marcolli–Suijlekom review 2018) is a canonical template in noncommutative geometry with the following content, **as stated by Connes himself** in Séminaire Poincaré X (2007), §5, equation (24):

> The spectral action principle asserts that the fundamental action functional $S$ that allows to compare different geometric spaces **at the classical level** and is used in the functional integration **to go to the quantum level**, is itself of the form
>
> $$\mathrm{Trace}\,(f(D/\Lambda))$$
>
> where $D$ is the Dirac operator and $f$ is a positive even function of the real variable while the parameter $\Lambda$ fixes the mass scale.

(Connes 2007, p. 185, eq. (24), emphases added in square brackets.)

Equation (25) of the same review gives the asymptotic expansion in decreasing powers of $\Lambda$:

$$\mathrm{Trace}\,(f(D/\Lambda)) \;\sim\; \sum_{k \in \Pi^+} f_k\,\Lambda^k\!\int |D|^{-k} \;+\; f(0)\,\zeta_D(0) \;+\; o(1),$$

where $f_k = \int_0^\infty f(v)v^{k-1}\,dv$ are the moments of $f$ and $\Pi^+$ is the positive part of the dimension spectrum. The coefficients $f_0, f_2, f_4$ are *numbers* — free moments of the user-chosen cutoff function $f$ — and they appear as *overall multipliers* in front of each power of $\Lambda$. In the 4-dimensional Chamseddine–Connes Standard-Model application, the three moments $(f_0, f_2, f_4)$ fix three boundary conditions at the unification scale $\Lambda$: the Newton constant, the Higgs mass, and the (common) gauge coupling at $\Lambda$. **There is no running in this formula.** The running is performed *afterwards* by standard continuum RG flow, exactly as Wikipedia's summary of the Connes-Chamseddine noncommutative Standard Model states it: *"The parameters of the model live at unification scale and physical predictions are obtained by running the parameters down through renormalization."*

**Add to §D (blackboard)**: the dictionary entry for "Connes spectral action" should be annotated with R status and with the following precise note: *the formula (24)–(25) is a classical/bare action functional at scale $\Lambda$, yielding boundary conditions; the quantum running is performed by post-hoc continuum RG flow, not by the Seeley–DeWitt expansion itself.* The current blackboard §D entry (row: "Connes spectral action | Tr f(D/Λ) heat-kernel expansion reproduces QFT correlator short-distance structure | Connes 1996; Chamseddine-Connes 1996 | R") is **structurally correct about the template but is rhetorically ambiguous** about whether the template delivers a running $g(\mu)$ — the ambiguity is the seed of the brief's paraphrase error.

### Step 4 — LOCK (Seeley-DeWitt a_4 invariant)

**Decomposition into sub-requirements (from the spawn prompt §5, Step 4)**:

1. **BC sub-algebra is well-defined.** $A_e \subset B(H_e)$ in Identity 12's Section 2.7 is the *e-circle algebra*, the C*-algebra generated by $\{D_n : n \in \mathbb{N}^*\}\cup\{E_r : r \in \mathbb{Q}/\mathbb{Z}\}$, with $U A_e U^* = A_{BC}|_{H_1^{(\mathbb{N}^*)}}$ by research/04-identity-12-rigorous.md §5.3–5.4. Status: **Yes, well-defined**.

2. **Dirac operator on the sub-algebra exists.** The Identity-12 image of $T_e = \log(R\hat p_e)$ is $H_{BC} = \log \hat N$ — *not* a Dirac operator but a *positive* Hamiltonian with discrete log spectrum $\{\log n : n \in \mathbb{N}^*\}$. The BC system at $\beta = 1$ is a C*-*dynamical* system $(A_{BC}, \sigma_t)$, and its GNS representation is a type III$_1$ factor (Bost–Connes 1995). **The BC system does not come equipped with a spectral triple structure $(A_{BC}, H_1, D_\text{BC})$ with $D_\text{BC}$ a finitely summable Dirac operator**; $H_{BC}$ is unbounded but its signed square root does not admit a spin structure interpretation. Status: **Obstruction. See §Step 5.5 (self-suspicion #2) and §Verdict.**

3. **Heat-kernel expansion converges.** Even if one formally defines $D_\text{BC} := (H_{BC})^{1/2}$ or $D_\text{BC} := \mathrm{sign}(H_{BC})|H_{BC}|^{1/2}$, the spectrum is $\{\log n : n \in \mathbb{N}^*\}$ with multiplicity 1 per integer, so $\mathrm{Tr}(e^{-t D_\text{BC}^2}) = \sum_{n=1}^\infty e^{-t (\log n)^2}$, which **is not of Seeley–DeWitt form**. The BC zeta function $\zeta_{D_\text{BC}}(s) = \sum_n (\log n)^{-s}$ is not a classical heat trace; it is related to the primes via the Wiener–Ikehara Tauberian theorem and the Riemann zeta function, but not via the Gilkey–Vassilevich formulae. Status: **The heat-kernel expansion relevant to Seeley–DeWitt does not apply to the BC Hamiltonian**.

4. **$a_4$ is computable.** The Vassilevich formulae (eqs. (4.26)–(4.29)) compute $a_k$ for a Laplace-type operator $D = -\nabla^\mu\nabla_\mu + E$ on a Riemannian manifold (possibly noncommutative via Connes' spin geometry framework). They do **not** compute $a_k$ for an operator whose spectrum is $\{\log n : n \in \mathbb{N}^*\}$ and whose "underlying manifold" is the adelic quotient $\mathbb{Q}^\text{cyc}$ (the dual of the BC algebra). The bridge family at k=4 is a *Brauer cocycle class* on the cyclotomic Galois quotient $(\mathbb{Z}/13\mathbb{Z})^*/\langle 3\rangle \cong \mathbb{Z}/4\mathbb{Z}$, carrying index-4 subfactor structure on $M = \pi_1(A_{BC})''$; it has **no Riemannian spin geometry of its own**. Status: **Seeley–DeWitt $a_4$ on the BC sub-algebra is not defined without supplying additional noncommutative-spin structure that is not produced by Identity 12 or by research/162/179**.

**Intermediate verdict before step 5.5**: sub-requirements (2)–(4) fail. LOCK cannot be completed: the Seeley–DeWitt $a_4$ invariant is not computable on the BC sub-algebra in its Identity-12 form, because Identity 12 provides a $C^*$-*dynamical* equivalence (scaling generator ↔ BC Hamiltonian), not a *spectral-triple* equivalence (Dirac operator ↔ Dirac operator).

### Step 5 — COMPUTE (a_4 + g(μ) + (ln)^−2 extraction)

Under the decomposition-failure at Step 4, the direct computation of the route-C claim cannot be performed: there is no $D_\text{BC}$ whose heat-kernel expansion yields $a_4$. However, Step 5 is still executable in the following conditional form — and this execution is what produces the *precision floor* the spawn prompt §6 requires, while simultaneously making the route-C obstruction numerically sharp.

**Conditional computation (on an external NCG spectral triple with Pati-Salam gauge sector at Λ).**

If one *bypasses* Identity 12 and directly applies the Chamseddine–Connes prescription to a Pati–Salam-like finite NCG $(A_F, H_F, D_F)$ — for example the SU(4)$_c\times$SU(2)$_L\times$SU(2)$_R$ finite geometry of Chamseddine–Connes–van Suijlekom 2013 (arXiv:1304.8050) — then the gauge kinetic term in the $a_4$ integrand is *textbook*: for the vector-field contribution with adjoint representation of a simple Lie algebra $\mathfrak{g}$ of dimension $d_\mathfrak{g}$ and dual Coxeter number $h^\vee$, Vassilevich eq. (4.34) gives

$$a_4^{[\mathrm{tot}]}|_{\mathrm{Tr}\,F^2} \;=\; \frac{11}{96\pi^2}\cdot 2 h^\vee \int d^4 x\,\sqrt{g}\,F^a_{\mu\nu}F^{a\,\mu\nu} \;=\; \frac{11\,h^\vee}{48\pi^2}\int d^4 x\,\sqrt{g}\,F^a_{\mu\nu}F^{a\,\mu\nu}.$$

For SU(N), $h^\vee = N$, so the coefficient is $11 N/(48\pi^2)$. Comparing with the standard YM kinetic term $-\frac{1}{4 g^2}F^a_{\mu\nu}F^{a\,\mu\nu}$ and multiplying by the $f_0 \Lambda^0$ moment of the cutoff function (which is the overall prefactor in Connes' eq. (25) at the logarithmic order), one obtains

$$\frac{f_0}{8\pi^2}\cdot\frac{11N}{3} \;=\; \frac{1}{g^2(\Lambda)},\qquad \text{or equivalently}\qquad \frac{1}{g^2(\Lambda)} \;=\; \frac{11 N}{24\pi^2}\,f_0.$$

This is the celebrated Chamseddine–Connes *boundary condition at the unification scale* that fixes $g^2(\Lambda)$ once $f_0$ is fixed. **The integer $11N/3$ appears in this formula as the one-loop divergent coefficient of the $F^2$ term — precisely because $a_4$ is the one-loop effective-action log-divergence coefficient**. Vassilevich says this explicitly (p. 41, §4.2): *"We calculate the heat kernel coefficient $a_4^{\mathrm{tot}}$ which defines the one-loop divergences in the zeta function regularization."*

**What this shows.** The precision-floor requirement ("$\beta_0 = 11N/3$ at 4–5 significant figures minimum from the $a_4$ computation") is met by the textbook Vassilevich–Gilkey computation with an *integer* identification:

$$\beta_0 \;=\; \frac{11N}{3} \;=\; 11 N / 3 \quad(\text{exact}).$$

For SU(2), SU(3), SU(5): $\beta_0 = 22/3, 11, 55/3$, all exact rationals. The rigor floor of the spawn prompt is cleared to *infinite* digits. But the identification is not *new* to the framework; it is a 1970s result, independently computed by Christensen–Duff, DeWitt, and (in the $a_4$ language) Gilkey. It appears in every standard heat-kernel-based one-loop YM computation.

**What this does NOT show.** The $11N/3$ in $a_4$ is *the coefficient of the logarithmic UV divergence of the one-loop effective action* in the zeta function / heat-kernel regularization — i.e. the coefficient of $\ln\Lambda$ in $W_\Lambda^\text{div}$ of Vassilevich eq. (1.21). It is the $\beta_0$ of the *bare-to-renormalized* coupling relation, not a function of a renormalization scale $\mu$. To obtain the *running* $g(\mu)$ one must

1. identify $g^2(\Lambda)$ with the bare coupling at the cutoff,
2. impose a renormalization condition at an IR scale $\mu$ (e.g. the physical YM coupling at some momentum),
3. solve the Callan–Symanzik equation $\mu\partial_\mu g = -\beta(g) = -\beta_0 g^3/(16\pi^2) + O(g^5)$,
4. integrate from $\Lambda$ down to $\mu$ to obtain $g^2(\mu) = g^2(\Lambda)/(1 + (\beta_0/(8\pi^2))g^2(\Lambda)\ln(\Lambda/\mu))$.

**Step 3 is continuum perturbation theory, not noncommutative geometry.** The spectral action tells you *the value of $\beta_0$ appearing in the one-loop counter-term*, but the *meaning of that value as the slope of a running coupling* comes from ordinary quantum field theory RG, not from the heat-kernel expansion.

**The $(\ln)^{-2}$ correction.** The W7-14 memo §2.2 already derives this from the Spiridonov–Chetyrkin trace-anomaly identity $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$: each insertion of $[\mathrm{Tr}\,F^2]_R$ carries one $Z_{\mathrm{Tr}\,F^2} \sim g^{-2} \sim (\ln)^{-1}$ factor, so the two-point function picks up $(\ln)^{-2}$. **This argument is independent of the spectral action** — it is a trace-anomaly identity in continuum QCD, proved by Spiridonov (1984), Spiridonov–Chetyrkin (1988), and Chanowitz–Ellis / Kluberg-Stern–Zuber / Nielsen. Route C does not simplify or strengthen this step; it merely reproduces it.

**Net result of Step 5**: the $11N/3$ integer emerges from $a_4$ at infinite precision, the $(\ln)^{-2}$ correction emerges from the trace-anomaly identity at infinite precision, but the *conditional* claim "H4 collapses because AF is built into the spectral action" does not survive: the spectral action delivers the $\beta_0$ value as a boundary condition at $\Lambda$, and the running/matching to the IR Schwinger function at short distance is exactly what H4 asks for. Route C reframes H4 but does not bypass it.

### Step 5.5 — Self-suspicion (incl. Connes 1996 verbatim verification)

**Self-suspicion #1 (the mandatory backward-verification check).** The spawn prompt §6 demands: *"do NOT trust the brief's paraphrase... find the verbatim passage in Connes 1996."*

The brief's load-bearing paraphrase is (spawn prompt §2):

> *"The Seeley-DeWitt expansion of this action automatically reproduces the leading short-distance behavior of the underlying QFT correlators, with the running coupling $g(\mu)$ emerging from the heat-kernel coefficient $a_4$."*

**Verbatim verification against Connes 2007 (Séminaire Poincaré X, 179–202; a review of Chamseddine–Connes 1996 by Connes himself, which the author has read at primary source).** Page 185, §5 "The spectral action principle," equation (24) and its surrounding text:

> *"The spectral action principle asserts that the fundamental action functional $S$ that allows to compare different geometric spaces **at the classical level** and is used in the functional integration to go to the quantum level, is itself of the form*
>
> $$\mathrm{Trace}\,(f(D/\Lambda)), \tag{24}$$
>
> *where $D$ is the Dirac operator and $f$ is a positive even function of the real variable while the parameter $\Lambda$ fixes the mass scale."*

Equation (25):
$$\mathrm{Trace}\,(f(D/\Lambda)) \sim \sum_{k \in \Pi^+} f_k\,\Lambda^k \int|D|^{-k} + f(0)\,\zeta_D(0) + o(1).$$

Equation (26): $f_k = \int_0^\infty f(v)v^{k-1}dv$ (free moments).

**Plain reading.** The spectral action is the *classical-level* action functional. Its expansion (25) is a finite polynomial in $\Lambda$ (plus a $\Lambda$-independent zeta term) with coefficients given by noncommutative integrals $\int |D|^{-k}$. These coefficients are **not running couplings of $\mu$**; they are **fixed numbers at the scale $\Lambda$**, to be used as *boundary conditions* for subsequent standard (continuum) RG flow.

**Verification against Vassilevich 2003 §4.2.1 (primary source, p. 40–41)**. Vassilevich's computation of $a_4$ for pure Yang–Mills produces eq. (4.34): $a_4^{[\mathrm{tot}]} = \frac{11}{96\pi^2}\int F\wedge *F$, and the paper then says verbatim (p. 41): *"The one-loop divergence (4.34) reproduces the structure of the classical action with different charges for each $\mathcal{G}_i$. We also recover the coefficient 11/3 which is familiar from computations of the Yang-Mills beta functions."*

**Plain reading of Vassilevich.** The $11/3$ in $a_4$ is the coefficient of the *one-loop UV divergence* of the effective action — i.e. the counter-term that gets absorbed into a running coupling via $\Lambda$-dependence, NOT an expression of a running coupling itself. The interpretation of $11/3$ as $\beta_0$ comes from *matching* the counter-term structure to the Callan–Symanzik equation, which is a step *external* to the heat-kernel computation.

**Brief's paraphrase status: STRUCTURALLY INCORRECT.** The statement "the running coupling $g(\mu)$ emerges from $a_4$" is wrong. What emerges from $a_4$ is the *value of the one-loop beta-function coefficient $\beta_0$*, which is the integer $11N/3$. This is necessary but not sufficient for AF: it says that *if* one matches to standard QFT one gets $\beta_0 = 11N/3$, but the matching itself is a separate step that lives in ordinary continuum renormalization theory, not in noncommutative geometry.

**Consequence.** Route C's Step 5 target ("$g(\mu)$ matching $\beta_0 = 11N/3$... extracted from $a_4$") is confused between two distinct statements:

- **(A) Weak**: "$a_4$ contains the integer $\beta_0 = 11N/3$ as the counter-term coefficient." **TRUE and 1970s-classical** (Christensen–Duff, DeWitt, Gilkey, Vassilevich eq. (4.34)).

- **(B) Strong**: "$a_4$ produces a running coupling $g(\mu)$ whose flow matches $\beta_0 = 11N/3$ so that H4 follows from the framework's heat-kernel expansion alone." **FALSE**: $a_4$ produces a bare-coupling boundary condition at $\Lambda$, not a running flow, and the running flow — which *is* what H4 is about — must still be matched to the non-perturbative YM path integral at short distance, which is exactly the content of H4.

Route C collapses (A) into (B) and thereby mis-states the reach of the spectral action principle.

**Self-suspicion #2 (BC does not come with a spin structure).** Even the weak statement (A) fails to apply to the BC sub-algebra for a simple structural reason: Identity 12 gives a *C\*-dynamical* equivalence $U T_e U^* = H_{BC}$, not a *spectral-triple* equivalence. The BC Hamiltonian $H_{BC} = \log \hat N$ is a positive operator on $H_1^{(\mathbb{N}^*)}$ with discrete log spectrum $\{\log n\}$; it is *not* a Dirac operator on a noncommutative spin manifold, and there is no finite-dimensional noncommutative finite space $F$ attached to $A_{BC}$ in the Connes–Chamseddine sense whose product with a commutative 4-manifold $M^4$ would give $A_{BC} \otimes C^\infty(M^4)$ the structure of a 4-dimensional real spectral triple of KO-dimension 2 (mod 8) needed for the spectral action machinery to produce an Einstein+Yang–Mills Lagrangian. One would need a *separate* construction of an NCG spectral triple $(A_\text{NC}, H_\text{NC}, D_\text{NC})$ — say the Pati–Salam triple of Chamseddine–Connes–van Suijlekom 2013 — *in addition to* the BC algebra, not *on* the BC sub-algebra. The bridge-family cocycle equality at k=4 is a *Brauer class identification*, not a spectral-triple construction: it tells you that $\mathrm{inv}_3(\mathrm{Frob}_3/(\mathbb{Z}/13\mathbb{Z})^*) = 1/4 \mod \mathbb{Z}$ equals the Fuglede–Kadison class of the index-4 subfactor, but this equality lives in $H^2(\mathbb{Z}/4\mathbb{Z}, U(1))$, not in the category of spectral triples.

**Self-suspicion #3 (Pati–Salam gives an SU(4)$_c$ coupling, not an SU(N) coupling).** Even if one grafts Chamseddine–Connes–van Suijlekom's 2013 Pati–Salam spectral triple onto the framework, the spectral action there delivers a *unified* gauge coupling at $\Lambda$ satisfying $g_\text{PS}^2 = g_2^2 = g_R^2$ (the SU(4)$_c$, SU(2)$_L$, SU(2)$_R$ couplings at the unification scale), with $\beta_0$ for SU(4)$_c$ equal to $11\cdot 4/3 = 44/3$. This gives the *Pati–Salam* $\beta_0$, not the pure-SU(N) $\beta_0 = 11N/3$ of the YM Clay problem. Route C's §5 computation recovers $44/3$ (N=4 Pati–Salam) at exactly the same precision as $11/3$ (N=1 normalisation), i.e. to infinite digits, but the Clay YM construction requires $\beta_0 = 11N/3$ for *arbitrary* $N$ — the framework would need to argue that the pure-SU(N) YM mass gap is controlled by the SU(4)$_c$ sub-sector of Pati–Salam, which is a non-trivial decoupling claim that the bridge-family cocycle at k=4 does not by itself establish.

### Step 6 — VERIFY (running coupling matches β_0 = 11N/3)

**Numerical verification of the one item that is actually verifiable**: the Vassilevich $a_4$ coefficient $11/(96\pi^2)$ for pure YM, re-identified as the integer $\beta_0 = 11N/3$ after contraction with the Killing form. This is what the script `code/R.C.1-seeley-dewitt-a4.py` computes, to `mp.dps = 80` precision, as a sanity check that the 1970s textbook result is reproducible and that the SU(2), SU(3), SU(4), SU(5), SU(6), SU(N→∞) integer identifications are exact.

**Precision floor cleared**: 80-digit match (exact rational identification, so effectively infinite precision).

**But this verification is confirming a textbook fact, not a framework-native closure of H4.** The precision is high because the computation is trivial (integer arithmetic on the known Gilkey–DeWitt formulae), not because the framework has discovered anything new about running. What H4 *actually* asks — whether the non-perturbative Schwinger function admits a short-distance expansion with the *leading perturbative coefficient having the right value* — is not addressed by Route C in any way that the preprint's existing W7-14 §5.3 analyticity reformulation does not already address.

## Verdict: KILLED (as a framework-native closure of H4)

Route C is KILLED as the *claimed* framework-native closure of H4. The reasons are structural, primary-source-verified, and independent of numerical uncertainty:

1. **The spectral action principle produces a classical / bare action at $\Lambda$, not a running $g(\mu)$.** This is explicit in Connes 2007 eq. (24) ("at the classical level") and in Vassilevich's interpretation of $a_4$ as the coefficient of the one-loop UV divergence. The brief's paraphrase conflates "$a_4$ contains the integer $\beta_0 = 11N/3$ as a counter-term coefficient" (true, textbook) with "$a_4$ produces a running coupling $g(\mu)$" (false, structurally).

2. **Identity 12 is a C\*-dynamical equivalence, not a spectral-triple equivalence.** The unitary $U : H_e \to H_1^{(\mathbb{N}^*)}$ intertwines $T_e \leftrightarrow H_{BC}$ but does not supply a Dirac operator $D_{BC}$ on $A_{BC}$; $H_{BC} = \log\hat N$ is not of Seeley–DeWitt form. The heat-kernel expansion does not apply to $H_{BC}$.

3. **The bridge family at k=4 is a cohomology class identification, not a spectral-triple construction.** $\mathrm{inv}_3 = 1/4 \mod \mathbb{Z}$ lives in $H^2(\mathbb{Z}/4\mathbb{Z}, U(1))$; it identifies the Pati–Salam colour structure with the Brauer class of a Jones subfactor, but it does not produce a finite noncommutative geometry $(A_F, H_F, D_F)$ on which the Chamseddine–Connes spectral action can be evaluated in the standard sense.

4. **Even if one grafts CCvS 2013's Pati–Salam spectral triple onto the framework, the output is an SU(4)$_c$ unified coupling at $\Lambda$, not a pure-SU(N) YM coupling.** The Clay-YM construction asks about arbitrary SU(N); the Pati–Salam spectral action says something about SU(4) at the unification scale, which is a different question.

5. **The $(\ln)^{-2}$ correction that H4 requires is independent of the spectral action**: it follows from the Spiridonov–Chetyrkin trace-anomaly identity $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$, which W7-14 §2.2 already cites. Route C does not strengthen this step; it merely reproduces it.

**KILLED verdict is narrow**: what is killed is *Route C as the closure of H4*, i.e. the specific claim that combining Connes' spectral action + Identity 12 + bridge family k=4 at (3,13) gives a structural bypass of H4. The underlying *tools* (spectral action, Identity 12, bridge family) remain valid framework machinery. Only the specific closure argument is wrong.

## Generative step / Stuck-at step

**Generative step**: Step 5.5 (self-suspicion #1). The backward-verification of Connes 2007 eq. (24) against the brief's paraphrase *crystallised* the Route-C obstruction into a single sentence: the spectral action is classical, not running. Once that sentence is written down, Steps 4, 5, 6 rearrange themselves around it and the KILLED verdict becomes unambiguous.

**Stuck-at step**: Step 4.2 (Dirac operator on the BC sub-algebra). Even in a charitable reading that ignores the classical-vs-running issue of self-suspicion #1, the BC sub-algebra does not come with a spectral-triple structure that the spectral action machinery can operate on. Identity 12 gives the *wrong kind* of equivalence for this programme — it is an equivalence of C*-*dynamical* systems, not of *spectral triples*. This is the structural wall that a future Route C' would have to address if anyone wanted to retry the framework-native spectral action route.

## §I notes

**I.1**. The blackboard §D entry for "Connes spectral action" should be annotated: *"Produces classical/bare action at cutoff $\Lambda$ (Connes 2007 eq. (24)); running couplings come from post-hoc continuum RG flow, not from the Seeley–DeWitt expansion itself. The $a_4$ coefficient $11/(96\pi^2)$ in Vassilevich eq. (4.34) is the one-loop UV counter-term, not a running coupling; it carries the integer $\beta_0 = 11N/3$ but as a boundary condition at $\Lambda$, not as a flow."* This annotation prevents future runs from repeating the Route-C paraphrase error.

**I.2**. Route C is KILLED, but the kill yields an information-rich negative result. The kill catalogs a specific failure mode — "framework-native" route that reads in running from a classical construction — that other Route-C-like attempts should be prevented from repeating. Add to the kill list on the blackboard §F with the precise framing: *"Route C — conflates bare coupling at $\Lambda$ with running coupling, on the basis of a too-generous reading of the spectral action principle."*

**I.3**. The result *does* sharpen the status of the W7-14 reframing. Since Route C cannot do better than W7-14 on the question of extracting $(\ln)^{-2}$ (both use the same Spiridonov–Chetyrkin trace-anomaly identity), **W7-14 §5.3 analyticity is the frontier**, not Route C. This is an argument for re-prioritising Route A over Route C in future Wave 2 planning.

**I.4**. The Vassilevich $a_4 = 11/(96\pi^2)\int F\wedge*F$ result is already used by the framework at Route 05 of Paper 10 (Weyl anomaly + KK decoupling; see W7-14 §6.2, citing Vassilevich hep-th/0306138 eq. 4.3 for mass-independence of $a_4$). This is the *correct* use of the spectral action machinery in the framework: as a tool for showing that the KK tower decouples at short distances (via Vassilevich's $a_4(D_m) = a_4(D_0) - m^2 a_2(D_0)$ factorisation), NOT as a machine for producing running gauge couplings. The framework already uses the spectral action correctly in one place; Route C was trying to use it incorrectly in a second place.

**I.5**. There is a constructive sub-idea latent in Route C that the KILLED verdict does not eliminate. The Chamseddine–Connes–van Suijlekom 2013 Pati–Salam spectral triple (arXiv:1304.8050) matches the framework's k=4 bridge at (3,13) Pati–Salam structure and produces (i) the integer $11N/3$ in $a_4$ at $\Lambda$ (so the framework and CCvS 2013 agree at the boundary condition level), (ii) an SO(10)-like unification structure at a high cutoff. The framework's $\alpha_{PS}^{-1} = 17$ result (research/184) and CCvS 2013's unified gauge coupling at $\Lambda$ are *compatible boundary conditions*. This compatibility is a new "seventh anchor" candidate for the geometric-spectral duality of research/04 §7, distinct from Route C as a proof tool. Noted as a forward lead for a separate research note, not for Route C.

## Proposed §D additions

Propose the following edits to `blackboard.md §D` (master dictionary):

**§D.a — Modify existing row for "Connes spectral action":**

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| Connes spectral action | **Classical / bare** action $\mathrm{Tr}\,f(D/\Lambda)$ at cutoff $\Lambda$; heat-kernel expansion yields boundary conditions for post-hoc RG running (Connes 2007 eq. (24); Vassilevich 2003 eq. (4.34) for YM $a_4$) | Connes 1996; Chamseddine-Connes 1996; Connes 2007 review; Vassilevich 2003 | R | — | — | 80 (Vassilevich eq. 4.34 reproduced to 80 dps in `code/R.C.1-seeley-dewitt-a4.py`) | 100 |

Key change: *classical / bare* marked in bold; "reproduces QFT correlator short-distance structure" removed and replaced with "yields boundary conditions for post-hoc RG running."

**§D.b — Add new row: "Vassilevich YM $a_4$ coefficient":**

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| Vassilevich YM $a_4$ | $a_4^{\mathrm{tot}}|_{\mathrm{Tr}\,F^2} = (11/(96\pi^2))\int F^a_{\mu\nu}F^{a\mu\nu}\cdot K$; after Killing-form contraction for SU(N), coefficient of $\mathrm{Tr}\,F^2$ is $11 N/(48\pi^2)$; integer $\beta_0 = 11N/3$ emerges as boundary condition at $\Lambda$, not running flow | Vassilevich 2003 Phys. Rep. 388 eq. (4.34) | R | $a_4^{\mathrm{YM}}$ | — | 80 | 100 |

**§D.c — Add new row: "Trace-anomaly identity (Spiridonov-Chetyrkin)":**

| Name | Statement (1 line) | Source | Status | Notation | Floor dps | Source dps | Completeness % |
|---|---|---|---|---|---|---|---|
| Spiridonov-Chetyrkin trace-anomaly identity | $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$ exact to all orders in continuum PT; gives $Z_{\mathrm{Tr}\,F^2}\propto g^{-2}\propto(\ln)^{-1}$, producing $(\ln)^{-2}$ in the two-point function after two insertions | Spiridonov 1984 IYaI-P-0378; Spiridonov-Chetyrkin 1988 Sov.J.Nucl.Phys. 47 522; Chanowitz-Ellis 1972; Kluberg-Stern-Zuber 1974; Nielsen 1977 | R | $\gamma_{\mathrm{Tr}\,F^2}$ | — | — | 100 |

This dictionary entry is needed because the $(\ln)^{-2}$ extraction is the *same* in Route C and in W7-14 §2.2 — the trace-anomaly identity is the actual load-bearing input — and it should be recorded once at master level instead of being re-cited every time.

## What the next runner needs to know

**One-sentence:** Route C is KILLED; the Connes spectral action produces boundary conditions at $\Lambda$, not a running coupling, so H4 is not bypassed.

**Four-sentence:** The brief's paraphrase conflated the integer $\beta_0 = 11N/3$ appearing in the Vassilevich $a_4$ coefficient — which is a one-loop UV counter-term and a classical boundary condition — with the *running* $g(\mu)$ that H4 demands. Primary-source verification against Connes 2007 Séminaire Poincaré X §5 eq. (24) confirms the spectral action is stated *"at the classical level,"* and Vassilevich 2003 §4.2 confirms that its $a_4$ is *"the one-loop divergence in the zeta function regularization."* Additionally, Identity 12 is a C\*-dynamical equivalence whose right-hand side (the BC Hamiltonian $H_{BC} = \log\hat N$) is not a Dirac operator and does not support a Seeley–DeWitt expansion, so the BC sub-algebra route to $a_4$ is structurally unavailable. Reprioritise: Route A (Taylor-coefficient identification via W5-10 analyticity) and Route B (CCM 2025 port to YM) remain open; Route D (editorial HONEST-STALL) remains live; Route C is closed.

**Verification artifact:** `code/R.C.1-seeley-dewitt-a4.py` reproduces Vassilevich's eq. (4.34) at `mp.dps = 80`, producing the exact integer identification $\beta_0(SU(N)) = 11N/3$ for $N = 2, 3, 4, 5, 6, 10, 100$ and cross-checking against known one-loop YM beta-function tables. The script clears the precision-floor rule of the spawn prompt §6 to infinite digits (integer rationals). This is a *textbook sanity check*, not a new verification.

---

## §M — ≤300-word summary

Route C attempted a framework-native H4 closure via Connes' spectral action + Identity 12 + k=4 bridge at (3,13) Pati–Salam. The brief claimed the Seeley–DeWitt a_4 coefficient produces a running g(μ) matching β_0 = 11N/3, collapsing H4. Primary-source verification at Connes 2007 Séminaire Poincaré X §5 eq. (24) disproves this: Connes states the spectral action is defined *"at the classical level,"* producing a bare action at Λ that gives boundary conditions, not a running flow. Vassilevich 2003 eq. (4.34) computes $a_4^{\mathrm{tot}} = (11/96\pi^2)\int F\wedge *F$ for pure YM and calls this *"the one-loop UV divergence in zeta regularization"* — the integer 11/3 is a counter-term coefficient, not a running-coupling slope. The running comes from standard Callan–Symanzik flow, exactly what H4 is about. Identity 12 is a C\*-*dynamical* equivalence ($T_e ↔ H_{BC} = \log\hat N$), not a *spectral-triple* equivalence: $H_{BC}$ is not of Seeley–DeWitt form, so the BC sub-algebra does not admit a Dirac operator on which the spectral action operates. The k=4 bridge is a Brauer cocycle identification in $H^2(\mathbb{Z}/4\mathbb{Z}, U(1))$, not a noncommutative-geometry construction. Route C is KILLED as an H4 closure — narrowly: the spectral action, Identity 12, and the bridge family remain valid framework tools; only the specific closure argument is wrong. The precision floor β_0 = 11N/3 at 4–5 sig figs is cleared to infinite digits via integer rational identification in the classical $a_4$, but that is a 1970s Christensen–Duff–Gilkey result, not a framework novelty. Reprioritise: Routes A/B remain open; Route D remains live; Route C is closed with an information-rich negative result. W7-14 §5.3 analyticity remains the frontier.
