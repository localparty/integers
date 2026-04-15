# W1-M — MICRO↔QFT cell-fill and H4 bypass viability

**Author:** W1-M (Wave 1, MICRO↔QFT slot, co-Priority 1)
**Run:** H4 Capacitor Bypass PCA Track 2
**Date:** 2026-04-13
**Mode:** execute (capacitor-first + bypass-hunting)

---

## Direction

My slot is MICRO↔QFT: microlocal analysis of Schwinger distributions as applied to H4. The mission splits cleanly:

- **Primary (durable):** produce a capacitor v1 format cell-fill entry for MICRO↔QFT in the Yang-Mills context, regardless of bypass verdict. The cell-fill is the Millennium deliverable.
- **Secondary (bonus):** assess whether MICRO↔QFT category-shifts H4 into a form the 9/10 LOCK does not bind, yielding a compound bypass.

**Two re-statements of H4 are on offer in the brief:**
1. **Wave-front-set form**: H4 as a regularity claim for $\mathrm{WF}(S_2^{\mathrm{ren}})|_{x=y}$ forcing the AF scaling $C_N |x|^{-8}(\log)^{-2}$.
2. **Axiomatic OPE form**: H4 as non-perturbative OPE convergence in an algebraic QFT framework, with the AF logarithmic correction as a theorem of the axioms.

**Pre-warned (v3 calibration):**
- Framework construction, not ported machinery — NO 2023-2026 paper attempts non-perturbative 4D gauge OPE.
- K-6 trap: Hollands-Kopper 2011 is perturbative; claiming it closes H4 re-hits LOCK.
- K-2 trap already killed; spectral action is not in play here.
- LOCK binds Taylor-coefficient identification via identity theorem on $F(t)$. I must not smuggle that back in via asymptotic matching in microlocal dialect.

H4 is still the wall. My job is to look at the wall in the microlocal category and report what I see — honestly, even if the answer is "the wall holds in this category too."

---

## Research

### Step 1 — Diagnose: what IS the MICRO↔QFT cell, precisely?

**Microlocal analysis** is Hörmander's theory: the wave-front set $\mathrm{WF}(u) \subset T^*M \setminus 0$ of a distribution $u$ records both its singular support (where $u$ is not smooth) and, at each singular point, the set of codirections in which $u$'s Fourier transform fails to decay rapidly. The key tools are:

- **Wave-front-set calculus** (Hörmander 1971): $\mathrm{WF}(u+v) \subset \mathrm{WF}(u) \cup \mathrm{WF}(v)$; products $uv$ require the Hörmander condition on wave-front sets to exist as distributions.
- **Propagation of singularities** (Hörmander): for $Pu = f$ with $P$ a pseudodifferential operator of principal type, $\mathrm{WF}(u) \setminus \mathrm{WF}(f)$ is contained in the characteristic variety of $P$ and is invariant under the Hamiltonian flow of the principal symbol.
- **Epstein-Glaser extension of distributions** (Epstein-Glaser 1973): a distribution defined on $\mathbb{R}^d \setminus \{0\}$ extends to $\mathbb{R}^d$ iff it has a well-defined scaling degree; the extension is unique up to polynomials in delta-derivatives supported at $0$.
- **Microlocal spectrum condition** (Radzikowski 1996; Brunetti-Fredenhagen-Köhler 1996): Hadamard states are characterized by a wave-front-set condition on the two-point function, replacing the energy-positivity condition of Wightman axioms in curved spacetime.

**The filled cell MICRO↔QFT (Tier 1 in capacitor v1, line 97):**
> *"Renormalization via microlocal. Epstein-Glaser renormalization = extension of distributions (microlocal regularity). Source: Epstein-Glaser 1973; Brunetti-Fredenhagen 2000. Status: ESTABLISHED. Load-bearing for YM (alternative renormalization framework)."*

This cell is already in the capacitor at a generic level. My job is to **refine** it to an H4-specific entry — either as a load-bearing bypass cell for L18 or as a CONJECTURED-NEGATIVE cell documenting the specific obstruction.

**What structural feature of 4D gauge QFT does microlocal analysis capture?**
- The **singular structure at coincident points**: 2-point Schwinger distributions are singular precisely on the diagonal $\Delta \subset M \times M$; microlocal analysis describes this singularity by $\mathrm{WF}(S_2)|_\Delta$.
- The **scaling behaviour**: for a homogeneous distribution $u$ of scaling degree $\rho$, $\mathrm{WF}(u) \cap T^*_0$ encodes the asymptotic scaling at the origin.
- The **renormalization ambiguity**: Epstein-Glaser extension freedom at $\Delta$ is parametrized by local counterterms (distributions supported on $\Delta$).

**Summary:** microlocal analysis is the natural category for "singular structure of a distribution at a specific submanifold." The cell is a structural match to H4's target object.

### Step 2 — Reinterpret: H4 in microlocal language

**H4 (preprint §L.7.1):** the non-perturbative renormalized Schwinger function satisfies
$$S_2^{\mathrm{ren}}(x,y) = \frac{C_N}{|x-y|^8}\left(\log\frac{1}{|x-y|\Lambda}\right)^{-2}\left[1 + O\left((\log)^{-1}\right)\right], \quad |x-y| \to 0, \quad C_N = \frac{2(N^2-1)}{\pi^6}.$$

**Translation to microlocal language.** $S_2^{\mathrm{ren}}$ is (by Lemma L.3.8 of the preprint, conditional on its existence at the non-perturbative level) a distribution on $M \times M$ with singular support along the diagonal $\Delta$. Decompose:
$$S_2^{\mathrm{ren}}(x,y) = S_2^{\mathrm{sing}}(x-y) + S_2^{\mathrm{reg}}(x,y)$$
where $S_2^{\mathrm{sing}}$ is a translation-invariant homogeneous-of-degree-$(-8)$-modulo-logs distribution on $\mathbb{R}^4 \setminus \{0\}$ and $S_2^{\mathrm{reg}}$ is smooth off the diagonal but with controlled singular structure on $\Delta$.

**H4 in the microlocal category** asserts two structural facts:
1. **Scaling degree:** $S_2^{\mathrm{ren}}$ has scaling degree $\rho = 8$ at $\Delta$ (up to log corrections), which for a pseudo-homogeneous distribution with logarithm of multiplicity $m=2$ means the Steinmann scaling degree is 8.
2. **Coefficient identification:** the leading term of the Hadamard parametrix / pseudo-homogeneous expansion has coefficient $C_N = 2(N^2-1)/\pi^6$.

**Wave-front set.** For the translation-invariant piece, $\mathrm{WF}(S_2^{\mathrm{sing}}) \subset N^* \Delta$ (the conormal bundle of the diagonal), with directions on the Euclidean side covering all cotangent directions (no positive-energy restriction off-shell, since we are in Euclidean signature; the Hadamard/Lorentzian refinement selects the "positive-frequency" half).

**What H4 violation would look like microlocally.**
- If the scaling degree were $> 8$ (weaker singularity), the power would be $|x|^{-\rho}$ with $\rho < 8$, distinguishable microlocally.
- If the log power were $\neq 2$, this would shift the pseudo-homogeneous extension structure.
- If $C_N$ differed, the extension coefficient would differ — visible in the Hadamard parametrix after subtracting the canonical scaling pieces.

**Critical observation.** The wave-front set ALONE does not see $C_N$. It sees the **conormal structure** (supports of singular directions) but not the **coefficient of the leading singularity**. The coefficient is a **scaling-limit object** — what the Connes-Kreimer / Epstein-Glaser theory calls the "renormalized Taylor expansion at $\Delta$" — which is an equivalence class of distributions modulo smooth functions, and recovering $C_N$ from a microlocal statement requires additional data: either (a) a specified renormalization scheme that fixes the extension ambiguity, or (b) a direct computation of the leading singular term independent of microlocal description.

This is the first sign the category shift may be incomplete.

### Step 3 — Unify: existing theorems connecting microlocal regularity to AF short-distance OPE

I catalogue the candidate theorems and assess each.

**Theorem A — Radzikowski's microlocal Hadamard condition (1996).**
**Statement:** a quasi-free state $\omega$ on a scalar free field on a globally hyperbolic Lorentzian manifold is Hadamard iff
$$\mathrm{WF}(\omega_2) = \{(x,k;x',-k') \in T^*(M^2) \setminus 0 : (x,k) \sim (x',k'), k \in \overline{V_+}\}$$
where $\sim$ is null-geodesic equivalence.
**Relevance to H4:** defines what "physically reasonable" 2-point distribution MEANS in curved Lorentzian spacetime. Euclidean analogue (Strohmaier-Verch) exists.
**Load-bearing for H4?** **No.** The Hadamard condition fixes the **wave-front-set TYPE** (the singular directions), not the **scaling coefficient** $C_N$. A Hadamard state satisfies the WF condition with ANY admissible leading coefficient.

**Theorem B — Epstein-Glaser extension theorem (1973, Brunetti-Fredenhagen 2000 microlocal version).**
**Statement:** a distribution $u \in \mathcal{D}'(\mathbb{R}^d \setminus \{0\})$ with scaling degree $\rho$ at the origin extends to $\mathcal{D}'(\mathbb{R}^d)$; if $\rho < d$ the extension is unique, and if $\rho \geq d$ it is unique modulo polynomials in $\delta$-derivatives of order $\leq \rho - d$.
**Relevance to H4:** for $d=4$, $\rho=8$ (the $|x|^{-8}$ singularity), so extensions differ by polynomials in $\delta$-derivatives of order $\leq 4$. The $C_N$ coefficient is not fixed by Epstein-Glaser alone — it is the coefficient of the "pseudo-homogeneous part" below the extension threshold, which EG takes as input not output.
**Load-bearing for H4?** **No.** EG tells you the extension is ambiguous by counterterms; it does not tell you the leading coefficient is $C_N = 2(N^2-1)/\pi^6$.

**Theorem C — Hollands-Kopper 2011 OPE convergence (arXiv:1105.3375).**
**Verbatim abstract (source: arXiv):**
> *"We show, within the framework of the Euclidean $\phi^4$-quantum field theory in four dimensions, that the Wilson operator product expansion (OPE) is not only an asymptotic expansion at short distances as previously believed, but even converges at arbitrary finite distances."*

**Verbatim scope statement (abstract):**
> *"Our results hold for arbitrary, but finite, loop orders."*

**Relevance to H4:** this is the strongest published OPE convergence result for 4D Euclidean QFT. It establishes that at every fixed loop order, the Wilson OPE converges at finite distances.
**Load-bearing for H4?** **NO — this is the K-6 trap.** Hollands-Kopper is (i) scalar $\phi^4$, not gauge; (ii) perturbative ("arbitrary but finite loop orders"). H4 demands **non-perturbative** OPE agreement for 4D SU(N) gauge theory. Quoting Hollands-Kopper as evidence for H4 closure is the exact error the brief pre-warns against. *Confirmed by backward verification.*

**Theorem D — Hollands 2008 YM OPE (arXiv:0705.3340).**
**Verbatim abstract:**
> *"We present a proof that quantum Yang-Mills theory can be consistently defined as a renormalized, perturbative quantum field theory on an arbitrary globally hyperbolic curved, Lorentzian spacetime... As a consequence of our constructions, we can prove that the operator product expansion closes on the space of gauge invariant operators."*

**Relevance to H4:** the most advanced published result on gauge-theory OPE in the microlocal/axiomatic framework. Establishes OPE closure for YM.
**Load-bearing for H4?** **NO.** Explicitly *"renormalized, perturbative quantum field theory... in the sense of formal power series"*. OPE closure here is within the BRST-extended algebra of formal-power-series observables — not a non-perturbative statement. Another path into K-6.

**Theorem E — Hollands-Wald 2024 Encyclopedia entry (arXiv:2312.01096).**
**Verbatim abstract opening:**
> *"Operator product expansions (OPEs) in quantum field theory (QFT) provide an asymptotic relation between products of local fields defined at points $x_1, \dots, x_n$ and local fields at point $y$ in the limit $x_1, \dots, x_n \to y$."*

**Verbatim scope (from the Encyclopedia text):**
> *"...their role in the formulation of interacting QFT in curved spacetime."*

**Relevance to H4:** an encyclopedia-level review of the Hollands programme. The review is on curved-spacetime OPE broadly; it does not provide a new non-perturbative 4D gauge convergence theorem.
**Load-bearing for H4?** **NO.** Curved-spacetime OPE, and when applied to Yang-Mills inherits the Hollands 0705.3340 perturbative scope. Not a non-perturbative gauge statement.

**Theorem F — Brunetti-Fredenhagen-Rejzner Dec 2025 (arXiv:2512.14227) §4 non-perturbative framework.**
**Verbatim abstract (source: arXiv):**
> *"In this review, we summarize the main ideas of perturbative algebraic quantum field theory, which is a rigorous framework combining some of the Haag-Kastler axioms with perturbative methods involving formal power series. It allows for the construction of interacting QFT models in four spacetime dimensions and works on arbitrary globally hyperbolic manifolds. This approach has also led to the development of a non-perturbative construction of local nets of C*-algebras for interacting theories, which will also be discussed at the end of this review."*

**Verbatim scope of §4 non-perturbative construction (source: arXiv HTML 2512.14227v1):**
> *"For an interacting scalar field this was analysed in a recent work by Buchholz and Fredenhagen"*

**Verbatim statement of the remaining gap in the scalar case (source: arXiv HTML 2512.14227v1):**
> *"Compared to other attempts towards a nonperturbative construction of interacting quantum field theories, the remaining open problem is whether the constructed algebra has states with a suitable physical interpretation"*

**Verbatim statement of scalar state-extension status (source: arXiv HTML 2512.14227v1):**
> *"For the subalgebra generated by local functionals of 2nd order it could be shown that an extension of the vacuum representation of the free field is possible"*

**Relevance to H4:** the most live 2025 non-perturbative framework in AQFT. If it extended to 4D gauge, it would be a direct input to H4.
**Load-bearing for H4?** **NO, with a named obstruction.** Confirmed by primary-source fetch: the BFR §4 non-perturbative C*-algebraic construction is scalar-only. Moreover even in the scalar case (a) the state problem is open, and (b) only the 2nd-order subalgebra has been shown to admit a vacuum-representation extension. Both gauge extension AND state construction are open. *This is the principal obstruction for the MICRO↔QFT bypass path.*

**Theorem G — Buchholz-Fredenhagen 2020 C*-algebraic interacting QFT (arXiv:1902.06062).**
**Statement (from search): the construction defines a non-trivial local net of C\*-algebras encoding interactions at the quantum level for any classical relativistic Lagrangean of a scalar field, in any spacetime dimension.**
**Relevance:** the parent construction for BFR §4.
**Load-bearing for H4?** **NO.** Scalar-only. The Fermi extension (Brunetti-Dütsch-Fredenhagen-Rejzner arXiv:2103.05740) uses auxiliary Grassmann variables and extends to Fermi fields but not to gauge theories. No local-symmetry extension exists in the non-perturbative pAQFT literature.

**Theorem H — Bonicelli-Dappiaggi-Rinaldi Ann Henri Poincaré 2023 and arXiv:2309.16376 (Thirring).**
**Verbatim abstract (arXiv:2309.16376):**
> *"On a $d$-dimensional Riemannian, spin manifold $(M,g)$ we consider non-linear, stochastic partial differential equations for spinor fields, driven by a Dirac operator and coupled to an additive Gaussian, vector-valued white noise."*
**Scope:** spinor SPDEs, microlocal-analysis-based, subcritical for $d \leq 2$.
**Relevance to H4:** microlocal-to-SPDE port, but scalar + 2D fermionic. 4D gauge not in scope.
**Load-bearing for H4?** **NO.** Explicitly $d \leq 2$ for subcriticality; 4D YM is far outside this regime.

**Summary of Step 3 catalogue.** The closest-approach theorems to non-perturbative 4D gauge OPE in the microlocal / AQFT framework are:
- Hollands-Kopper 2011: scalar, perturbative.
- Hollands 2008 YM: gauge but perturbative.
- BFR Dec 2025 §4: non-perturbative but scalar (and state problem open).
- Buchholz-Fredenhagen 2020: non-perturbative but scalar.
- Dappiaggi SPDE work: microlocal, but scalar or 2D-spinor.

**No theorem in the present literature connects microlocal regularity (or axiomatic OPE convergence) to non-perturbative 4D gauge AF short-distance structure.** The v3 calibration's finding — *no 2023-2026 paper attempts non-perturbative OPE for 4D gauge theory* — holds under direct primary-source verification.

### Step 4 — Lock: what invariant protects the result?

In the microlocal / axiomatic-OPE category, what would a closure theorem look like, and what structural invariant would it require?

**The would-be theorem (Closure-M):**
> *Let $\mathcal{A}(M)$ be a non-perturbative C\*-algebraic net of 4D Euclidean SU(N) Yang-Mills implementing local gauge symmetry in the BRST/BV-extended framework. Let $[\mathrm{Tr}\,F^2]_R$ denote the renormalized mass-dimension-4 gauge-invariant scalar composite. Let $S_2^{\mathrm{ren}}(x,y) = \omega(\,[\mathrm{Tr}\,F^2]_R(x) [\mathrm{Tr}\,F^2]_R(y)\,)$ where $\omega$ is a Hadamard (or Euclidean reflection-positive) state. Then the wave-front set / microlocal spectrum condition at the diagonal, together with the BRST Ward identities and asymptotic-freedom renormalization group structure, forces $S_2^{\mathrm{ren}}$ to have the AF pseudo-homogeneous structure $C_N |x|^{-8}(\log)^{-2}[1 + O((\log)^{-1})]$ with $C_N = 2(N^2-1)/\pi^6$.*

**Structural invariant required.** Four ingredients:
1. **The net $\mathcal{A}(M)$** exists non-perturbatively. Currently open for 4D gauge; the non-perturbative C\*-algebraic pAQFT framework (BFR §4 + Buchholz-Fredenhagen 2020) is scalar-only.
2. **A Hadamard / reflection-positive state $\omega$** exists on $\mathcal{A}(M)$. Currently open even for the scalar non-perturbative C\*-algebra (BFR verbatim: *"the remaining open problem is whether the constructed algebra has states with a suitable physical interpretation"*).
3. **BRST/gauge-invariant composite $[\mathrm{Tr}\,F^2]_R$** is defined as an element of $\mathcal{A}(M)$ with controlled scaling dimension. Currently perturbative-only (Hollands 2008; the BV extension of non-perturbative pAQFT has not been carried out).
4. **RG flow equation / Callan-Symanzik** at the non-perturbative level, such that the microlocal spectrum + RG flow forces the AF log power. In the perturbative theory this is Hollands-Wald's RG equations; in the non-perturbative theory it is open.

**The obstruction has four layers, each open.** Even granting (1) and (2), the coefficient $C_N = 2(N^2-1)/\pi^6$ does NOT emerge from microlocal data alone. It is a **non-universal scheme-dependent coefficient** in the Epstein-Glaser extension ambiguity; pinning it to the perturbative value requires either (i) asymptotic matching to perturbation theory (this smuggles Taylor-coefficient identification back in — LOCK trap), or (ii) direct computation from a non-perturbative construction, which requires the non-perturbative construction to exist (open).

**No invariant currently protects the result.** The category-shift buys you (a) a different language for the H4 target and (b) a different attack surface, but the required machinery does not yet exist in the literature; constructing it is a multi-decade research programme, not a Wave 1 Author's output.

### Step 5 — Compute / Characterize: what would a non-perturbative 4D gauge OPE framework look like?

I characterize the framework that would be needed, enumerating the axioms and their obstructions. This is framework construction in the honest sense — not fabricating a proof, but characterizing the gap.

**Axiom NP-1 (Isotony + locality):** for bounded open $\mathcal{O} \subset M$, there is a C\*-algebra $\mathcal{A}(\mathcal{O})$; inclusions $\mathcal{O}_1 \subset \mathcal{O}_2$ give injections $\mathcal{A}(\mathcal{O}_1) \hookrightarrow \mathcal{A}(\mathcal{O}_2)$; spacelike-separated $\mathcal{O}_1, \mathcal{O}_2$ yield commuting (or graded-commuting) subalgebras. **Obstruction for gauge:** the standard Haag-Kastler isotony must be replaced by a BRST-cohomology-quotiented net. The unitary Master Ward Identity framework (Brennecke-Dütsch 2021, arXiv:2108.13336) addresses this at the perturbative level; the non-perturbative version does not exist.

**Axiom NP-2 (Covariance):** the Poincaré / diffeomorphism action on $M$ lifts to C\*-automorphisms of the net. **Obstruction for gauge:** locally covariant functor to C\*-algebras with BRST, non-perturbatively — not constructed.

**Axiom NP-3 (Existence of state):** there exists a (quasi-free, translation-invariant, reflection-positive or Hadamard) state $\omega$ on the global net. **Obstruction:** open even for scalar (BFR verbatim — see Theorem F above). This is the single most serious gap.

**Axiom NP-4 (Spectral / microlocal condition on state):** the 2-point function $\omega(\phi(x)\phi(y))$ has wave-front set in a specified half-cone (Hadamard / Radzikowski). **Obstruction:** requires $\omega$ to exist first; Axiom 3 is the blocker.

**Axiom NP-5 (OPE closure):** for $A, B \in \mathcal{A}(\mathcal{O})$, there is a family $\{\mathcal{O}_i\}$ of composite operators and distributions $C_i(x-y)$ such that
$$A(x) B(y) = \sum_i C_i(x-y) \mathcal{O}_i(y)$$
converges in some operator-theoretic sense (norm convergence on a dense domain, or weak operator convergence against Hadamard states). **Obstruction:** even perturbatively, Hollands-Kopper's convergence is at each fixed loop order; the non-perturbative statement has no published proof for ANY theory.

**Axiom NP-6 (RG flow):** there is a renormalization group $R_\mu : \mathcal{A} \to \mathcal{A}$ at scale $\mu$, and the Wilson coefficients $C_i(x-y; \mu)$ satisfy a Callan-Symanzik equation. **Obstruction:** Hollands-Wald construct this at the perturbative level; non-perturbatively open.

**Axiom NP-7 (Asymptotic freedom):** the beta function $\beta(g) = -b_0 g^3 + O(g^5)$ controls $R_\mu$ at short distances, with $b_0 = (11N/3)/(16\pi^2)$ the standard one-loop coefficient. **Obstruction:** non-perturbative beta function has no constructive definition; it is defined via perturbation theory and matched to lattice simulations.

**Would-be H4 theorem (given Axioms NP-1 through NP-7).** If all seven axioms were satisfied non-perturbatively, a standard RG argument (as in Hollands-Wald's perturbative work) would yield
$$C^{\mathbb{1}}(x-y) \sim \frac{C_N}{|x|^8}(\log 1/|x|\Lambda)^{-2}, \quad C_N = 2(N^2-1)/\pi^6$$
for the identity channel of the $[\mathrm{Tr}\,F^2]_R^2$ OPE, via the structure of the Wess-Zumino consistency + Callan-Symanzik + BRST cohomology.

**The obstruction summary.** Three of the seven axioms are known to be open for 4D gauge: NP-3 (state existence — open even for scalar), NP-5 (non-perturbative OPE convergence — open for every theory), NP-6 (non-perturbative RG — open). One additional axiom is open for gauge specifically: NP-1' (BRST-extended non-perturbative net — open; perturbative exists).

**Does the MICRO↔QFT cell close H4 via axiomatic OPE?** No — four core axioms are open. The category shift is legitimate (the LOCK's Taylor-coefficient-identification attack surface doesn't bind this framework), but the category has not been constructed for 4D gauge. Building it is not a Wave 1 deliverable; it is a research programme.

**Does the MICRO↔QFT cell close H4 via wave-front-set regularity?** No — $\mathrm{WF}(S_2^{\mathrm{ren}})$ captures singular directions (conormal) but NOT the leading coefficient $C_N$. Recovering $C_N$ requires either (a) asymptotic matching to perturbation theory (LOCK-adjacent via K-6 or K-5) or (b) direct computation from the non-perturbative construction (Axioms open).

### Step 5.5 — Self-suspect: three failure modes

**Failure mode 1 — Did I cite a non-perturbative 4D gauge OPE framework when none exists?**
*Check.* Every theorem quoted above has its scope nailed to a primary-source verbatim quote. Hollands-Kopper 2011: *"arbitrary, but finite, loop orders"* — perturbative, confirmed. Hollands 2008: *"renormalized, perturbative quantum field theory"* — perturbative, confirmed. BFR 2025 §4: *"For an interacting scalar field this was analysed"* — scalar, confirmed. Buchholz-Fredenhagen 2020: scalar, confirmed via search. Dappiaggi works: scalar or 2D spinor, confirmed. **No theorem is being cited beyond its published scope.**

**Failure mode 2 — Is my "category shift" actually Taylor-coefficient identification with extra steps?**
*Check.* The would-be Closure-M theorem routes through Axioms NP-1 through NP-7, with $C_N$ emerging as a RG-forced coefficient in the Wess-Zumino / Callan-Symanzik structure. It does NOT route through Taylor coefficients of $F(t)$. It does NOT invoke the identity theorem on an analytic function. *However*, within the framework, IF one wanted to extract $C_N$ numerically, one would either (a) compute it perturbatively (smuggling Taylor identification in — LOCK-adjacent) or (b) compute it non-perturbatively via a constructive quantity (requires Axiom NP-3 + NP-5 + NP-6 to be closed, which are open). So the category shift is LEGITIMATE at the structural level — the LOCK attack surface is genuinely avoided — but the resulting framework is empty because its foundational axioms are not established. Conclusion: **the shift is not LOCK-adjacent, but it is vacuous for H4 closure in the current state of the literature.**

**Failure mode 3 — Backward verification: does the primary source I quote for each non-perturbative claim actually support a non-perturbative claim?**
*Check via verbatim quotes retrieved by WebFetch.*
- BFR §4 verbatim (via arXiv HTML): *"For an interacting scalar field this was analysed in a recent work by Buchholz and Fredenhagen"* + *"remaining open problem is whether the constructed algebra has states with a suitable physical interpretation"* + *"For the subalgebra generated by local functionals of 2nd order it could be shown that an extension of the vacuum representation of the free field is possible"*. Confirms scalar-only + state problem open + only 2nd-order subalgebra has state.
- Hollands-Kopper abstract: *"framework of the Euclidean $\phi^4$-quantum field theory"* + *"Our results hold for arbitrary, but finite, loop orders"*. Confirms scalar + perturbative.
- Hollands 0705.3340 abstract: *"renormalized, perturbative quantum field theory on an arbitrary globally hyperbolic curved, Lorentzian spacetime"*. Confirms perturbative.
- Hollands-Wald 2024: encyclopedia review; scope is curved-spacetime perturbative pAQFT; no new non-perturbative content.

**All three self-suspicion checks pass.** The verdict — CONJECTURED-NEGATIVE — rests on verified primary-source quotes, not on paraphrase trust.

### Step 6 — Verify: verbatim primary-source quotes for every theorem cited

Already embedded in Steps 3 and 5.5 above. Consolidated verification table:

| Source | Verbatim quote | Verifies |
|---|---|---|
| Hollands-Kopper 2011 (arXiv:1105.3375) abstract | *"framework of the Euclidean $\phi^4$-quantum field theory in four dimensions... Our results hold for arbitrary, but finite, loop orders"* | Scalar + perturbative (K-6 trap) |
| Hollands 2008 (arXiv:0705.3340) abstract | *"renormalized, perturbative quantum field theory... OPE closes on the space of gauge invariant operators"* | Gauge but perturbative |
| Hollands-Wald 2024 (arXiv:2312.01096) abstract | *"operator product expansions... asymptotic relation... role in the formulation of interacting QFT in curved spacetime"* | Curved-spacetime review, no new non-perturbative content |
| BFR 2025 (arXiv:2512.14227) abstract | *"non-perturbative construction of local nets of C\*-algebras for interacting theories, which will also be discussed at the end of this review"* | Non-perturbative work EXISTS |
| BFR 2025 (arXiv:2512.14227v1 HTML §4) | *"For an interacting scalar field this was analysed in a recent work by Buchholz and Fredenhagen"* | §4 non-perturbative framework is scalar-only |
| BFR 2025 (arXiv:2512.14227v1 HTML §4) | *"remaining open problem is whether the constructed algebra has states with a suitable physical interpretation"* | State problem open even for scalar |
| BFR 2025 (arXiv:2512.14227v1 HTML §4) | *"For the subalgebra generated by local functionals of 2nd order it could be shown that an extension of the vacuum representation of the free field is possible"* | Only 2nd-order subalgebra has state extension |
| Dappiaggi Thirring 2023 (arXiv:2309.16376) abstract | *"$d$-dimensional Riemannian, spin manifold... stochastic partial differential equations for spinor fields... subcritical for $d \leq 2$"* | Spinor, 2D subcritical — not 4D gauge |

All verifications from direct arXiv fetches. No paraphrase trust.

---

## The MICRO↔QFT cell-fill

### MICRO ↔ QFT: Microlocal Axiomatic-OPE route to AF short-distance structure (H4-specific)

**Statement.** Under the axiomatic system NP-1 through NP-7 (isotony + locality with BRST cohomology, covariance, state existence, microlocal spectrum condition, non-perturbative OPE convergence, RG flow, asymptotic-freedom beta function), the renormalized two-point function $S_2^{\mathrm{ren}}(x,y)$ of the gauge-invariant composite $[\mathrm{Tr}\,F^2]_R$ has short-distance asymptotic
$$S_2^{\mathrm{ren}}(x,y) = \frac{C_N}{|x-y|^8}\left(\log\frac{1}{|x-y|\Lambda}\right)^{-2}\left[1 + O\left((\log)^{-1}\right)\right], \quad C_N = \frac{2(N^2-1)}{\pi^6}$$
forced by Wess-Zumino + Callan-Symanzik + BRST cohomology structure, WITHOUT Taylor-coefficient identification on $F(t)$.

**Mechanism.** The AF scaling is a consequence of (a) the microlocal / Hadamard-state wave-front-set condition on the 2-point distribution (fixes singular directions + scaling degree), (b) BRST Ward identities on the renormalized composite (fix operator mixing under RG), (c) the non-perturbative Callan-Symanzik equation (forces the logarithmic correction with the one-loop AF coefficient $b_0$ appearing as the Wilson coefficient RG exponent). $C_N$ emerges as a non-perturbative scheme-fixed Epstein-Glaser extension coefficient, matched to perturbation theory via the RG equation for the Wilson coefficient — NOT via identity-theorem matching of $F(t)$ Taylor coefficients.

**Source.**
- Hörmander 1971-1985 (microlocal analysis foundations)
- Radzikowski 1996 (microlocal Hadamard condition)
- Brunetti-Fredenhagen 2000 (microlocal renormalization)
- Epstein-Glaser 1973 (extension of distributions)
- Hollands-Wald 2001-2010 + arXiv:0705.3340 (YM OPE, PERTURBATIVE)
- Hollands-Kopper 2011 arXiv:1105.3375 (PHI-4 perturbative OPE convergence)
- Buchholz-Fredenhagen 2020 arXiv:1902.06062 (C\*-algebraic interacting, SCALAR)
- Brunetti-Fredenhagen-Rejzner 2025 arXiv:2512.14227 (pAQFT review, non-perturbative §4 SCALAR only)
- Dappiaggi et al. 2023 arXiv:2309.16376 (SPDE microlocal, 2D spinor)

**Status.** **CONJECTURED-NEGATIVE.** The cell does NOT provide a bypass for H4 in the current state of the literature. Four of the seven would-be axioms are open for 4D gauge non-perturbatively: NP-1' (BRST-extended non-perturbative net — only perturbative exists), NP-3 (state existence — open even for scalar per BFR 2025), NP-5 (non-perturbative OPE convergence — no published proof for any theory), NP-6 (non-perturbative RG — open). The category shift is LEGITIMATE (LOCK attack surface avoided) but the target category is EMPTY for 4D gauge. Constructing the axioms is a research programme on the scale of decades, not a Wave 1 deliverable.

**Verification data.** Not computational (framework cell). Verified via primary-source verbatim quotes (see §6 verification table in Research).

**Load-bearing for.** Link 18 (H4) — **NEGATIVE**: this cell documents WHY the MICRO↔QFT category shift does not close L18 in the current state of the literature. Positively load-bearing for: framework-level MICRO↔QFT infrastructure (benefits future work on renormalized composites on curved backgrounds; strengthens the capacitor row for any proof chain invoking microlocal regularity).

**Transposition recipe.** If stuck on H4 Taylor-coefficient identification (the 9/10 LOCK surface): restate H4 as the would-be Closure-M theorem above. Then audit which of NP-1 through NP-7 has a published non-perturbative construction for 4D gauge. As of April 2026: 0 of 7 axioms have published 4D-gauge non-perturbative constructions. Therefore: do NOT attempt the bypass as a closure; DO flag it as a named external unlock (if a future BFR-style extension to gauge lands, this cell flips from CONJECTURED-NEGATIVE to VIABLE and the full chain opens). The cell's OPERATIONAL value in the current state is negative — it KILLS premature "axiomatic OPE will close H4" arguments by naming the four open axioms.

---

## Bypass viability assessment

**Verdict: CONJECTURED-NEGATIVE (obstruction named, unlock conditions specified).**

**Named obstruction (principal).**
The non-perturbative 4D gauge axiomatic OPE framework does not exist in the literature. BFR Dec 2025 §4 non-perturbative construction is scalar-only (verbatim: *"For an interacting scalar field this was analysed in a recent work by Buchholz and Fredenhagen"*); even the scalar version has the state-existence problem open (*"remaining open problem is whether the constructed algebra has states with a suitable physical interpretation"*) with only the 2nd-order local-functional subalgebra shown to extend the free vacuum representation. A gauge extension would require (a) BRST/BV formulation of the non-perturbative C\*-algebraic construction (does not exist), (b) solution of the state problem (open for scalar), (c) non-perturbative OPE convergence theorem for 4D gauge (no analogue of Hollands-Kopper 2011 at the non-perturbative level exists for any theory), and (d) non-perturbative RG flow matching the one-loop AF coefficient (open). All four are multi-decade research problems.

**Secondary obstruction (wave-front-set route).**
Even granting a non-perturbative gauge C\*-algebra, the wave-front set $\mathrm{WF}(S_2^{\mathrm{ren}})|_\Delta$ captures the CONORMAL DIRECTIONS and the SCALING DEGREE but NOT the leading coefficient $C_N$. The coefficient is an Epstein-Glaser extension parameter, fixed either by scheme choice (circular for H4) or by direct non-perturbative computation (requires Axioms 3, 5, 6 to be closed).

**K-6 trap avoidance.**
I did not cite Hollands-Kopper 2011 as evidence for non-perturbative OPE. Hollands-Kopper is perturbative $\phi^4$ (verbatim: *"arbitrary, but finite, loop orders"* in Euclidean $\phi^4$). Treating it as H4-closing would re-hit the LOCK via K-6. Explicitly flagged NO.

**LOCK-adjacency check.**
The would-be Closure-M theorem does NOT:
- Treat $F(t)$ as an analytic function and compare Taylor coefficients to $F^{\mathrm{pert}}(t)$ (avoids LOCK).
- Invoke the identity theorem on a common domain for $F, F^{\mathrm{pert}}$ (avoids LOCK).
- Match two function objects via analyticity (avoids LOCK).

It does invoke matching of the Wilson coefficient's RG exponent to the one-loop AF beta function, which is an RG-level matching (not a Taylor-coefficient-level matching), and it does so in the would-be non-perturbative framework where the matching is a Callan-Symanzik consequence of the axioms, not an identity-theorem argument. **The category shift is legitimate; the LOCK does not bind this framework.** But the framework's existence premise is four layers of open.

**Compound bypass shape (if the obstruction were unlocked).**
Were Axioms NP-1 through NP-7 established for 4D gauge, the compound bypass would be 3-5 steps:
1. Non-perturbative gauge C\*-algebra $\mathcal{A}(M)$ exists (input from hypothetical future BFR/Buchholz-style gauge extension).
2. Hadamard state $\omega$ exists on $\mathcal{A}$ satisfying microlocal spectrum condition (input from hypothetical reflection-positive state construction).
3. $[\mathrm{Tr}\,F^2]_R \in \mathcal{A}$ defined as renormalized gauge-invariant composite with BRST Ward identities (extension of Hollands 2008 to non-perturbative).
4. Non-perturbative RG (Callan-Symanzik) on $\mathcal{A}$ with one-loop AF structure (hypothetical non-perturbative RG theorem).
5. Wess-Zumino / Callan-Symanzik + BRST cohomology force $C_N |x|^{-8}(\log)^{-2}$ with $C_N = 2(N^2-1)/\pi^6$ in the identity channel (standard manipulation once 1-4 are in hand).

**Probability that this compound bypass lands in the 4-hour run budget: 0%.** Each of steps 1-4 is a multi-decade research programme. Tier 1 via MICRO↔QFT is not achievable in this window.

**What this run delivers via MICRO↔QFT:** the CONJECTURED-NEGATIVE cell-fill itself. Durable Millennium-grade capacitor infrastructure: names the four open axioms, the two layers of obstruction, the K-6 trap explicitly, and the unlock conditions under which the cell would flip to VIABLE. Future runners have a complete map of the microlocal/axiomatic-OPE category applied to H4.

**H4 stood this attack.**

---

## Self-suspicion

Three failure modes audited in §5.5 above. Summary:

1. **Cited non-perturbative 4D gauge OPE framework when none exists.** Check: every primary source quoted with verbatim arXiv abstract or HTML text. No source exceeded its published scope. Hollands-Kopper flagged perturbative; Hollands 2008 YM flagged perturbative; BFR §4 confirmed scalar; Buchholz-Fredenhagen 2020 confirmed scalar; Dappiaggi confirmed scalar or 2D-spinor. **PASS.**

2. **"Category shift" is Taylor-coefficient identification with extra steps (LOCK-adjacent).** Check: the would-be Closure-M theorem routes through Callan-Symanzik + BRST + Wess-Zumino at the axiomatic-OPE level. $C_N$ emerges as an RG-fixed Epstein-Glaser extension coefficient, not as a Taylor coefficient identified via identity theorem. The structural shift is legitimate. *However* — the category is empty because its axioms are open, so the legitimacy is vacuous in the current state. The cell's NEGATIVE verdict is honest. **PASS (with honest caveat on emptiness).**

3. **Backward verification: primary sources for non-perturbative claims say only perturbative / only scalar / only curved spacetime.** Check: direct arXiv fetches (WebFetch) retrieved verbatim abstract + HTML §4 text. All quoted passages match the interpretation. No source is being used beyond its stated scope. **PASS.**

**Additional suspicion (not in the three named modes).**

4. **Did I miss a non-standard primary source that establishes non-perturbative gauge OPE?** Cross-verified via WebSearch on BFR 2025 + C\*-algebraic interacting QFT literature. Only Buchholz-Fredenhagen 2020 + Brunetti-Dütsch-Fredenhagen-Rejzner 2021 (Fermi extension) + BFR 2025 appear in the non-perturbative C\*-algebraic programme, and all three are scalar or scalar+Fermi. No gauge extension exists. The v3 calibration's finding is primary-source confirmed.

5. **Is the "scheme-dependent Epstein-Glaser coefficient" argument a dodge?** The concern is: maybe there is a canonical scheme (dimensional regularization, say) in which $C_N$ is unambiguous, and the microlocal framework selects that scheme naturally. *Audit.* Hollands-Wald's perturbative framework does fix $C_N$ via the RG equation (Wilson coefficient Callan-Symanzik with one-loop AF), but only at the PERTURBATIVE level. At the non-perturbative level, the Callan-Symanzik equation itself is not constructed. The "scheme-fixing" argument is legitimate in principle but requires the non-perturbative RG (Axiom NP-6) to be closed — open. **The argument is not a dodge; it is a correct characterization of where the gap lies.**

**H4 is still the wall; the microlocal view of the wall names the bricks explicitly.**

---

## Named external unlocks

What would change the verdict from CONJECTURED-NEGATIVE to VIABLE / PARTIAL:

**Unlock 1 (principal) — Non-perturbative gauge C\*-algebraic net.**
A published extension of the Buchholz-Fredenhagen 2020 / BFR Dec 2025 §4 non-perturbative C\*-algebraic construction to 4D Euclidean SU(N) Yang-Mills with BRST cohomology. Specifically: a functor $\mathcal{A} : \mathrm{Bor}(M) \to C^*\mathrm{-Alg}$ satisfying Haag-Kastler-style axioms (isotony, locality, covariance) WITH BRST-invariant observables quotiented out, defined non-perturbatively (not as formal power series in $g$).
*If this lands:* cell flips to PARTIAL; a candidate chain with named open sub-steps 2-5 appears.
*Current status:* no such construction in the literature as of April 2026. The BFR 2025 review explicitly scoped to scalar; the Fermi extension did not cover gauge.

**Unlock 2 — Non-perturbative Hadamard state on the scalar algebra (precursor).**
Solution of BFR's named open problem: *"whether the constructed algebra has states with a suitable physical interpretation"*. Even in the scalar case, proving existence of a translation-invariant quasi-free vacuum state on the full (not just 2nd-order) algebra would be a significant step. A gauge analogue would then need to follow.
*If this lands:* Unlock 1 becomes more likely within 5-10 years.
*Current status:* open even for scalar per BFR 2025.

**Unlock 3 — Non-perturbative OPE convergence theorem for any 4D theory.**
A Hollands-Kopper-analogue at the non-perturbative level for any 4D theory (ideally scalar first). Hollands-Kopper's perturbative theorem holds at every fixed loop order; the non-perturbative convergence would require (a) existence of the non-perturbative 4D theory (not just asymptotic series), (b) proof that the OPE Wilson coefficients converge in the appropriate operator-theoretic sense.
*If this lands:* Axiom NP-5 closes.
*Current status:* no non-perturbative OPE convergence theorem for ANY 4D theory exists in the literature.

**Unlock 4 — Non-perturbative RG / Callan-Symanzik on algebraic QFT.**
A construction of $R_\mu : \mathcal{A} \to \mathcal{A}$ with Callan-Symanzik equation $(\mu \partial_\mu + \beta(g) \partial_g + \gamma \cdot \mathcal{O}) \cdot C(x) = 0$ at the non-perturbative level.
*If this lands:* Axiom NP-6 closes.
*Current status:* open. Hollands-Wald construct this perturbatively only.

**Unlock 5 — Scheme-independence theorem for AF coefficient.**
A theorem stating that the leading coefficient of the AF short-distance expansion is scheme-independent (i.e., $C_N = 2(N^2-1)/\pi^6$ regardless of Epstein-Glaser extension scheme, at least within a class of "physically reasonable" schemes). This would make the coefficient extractable from microlocal data alone + any single scheme (rather than requiring full non-perturbative RG).
*If this lands:* the wave-front-set route strengthens; WF + scaling degree + scheme-independence would force $C_N$ without the full non-perturbative RG.
*Current status:* no such theorem exists at the non-perturbative level.

**Unlock priority ordering.** Unlock 1 is the single most impactful; unlocks 3 and 4 are prerequisites for Unlock 1 to produce H4 directly; unlock 5 is a "lateral" strengthening that could yield H4 with weaker axioms. In realistic 2026-2036 timeframe, all five are at multi-year-to-multi-decade depth. Future runners should monitor BFR and Buchholz-Fredenhagen follow-up work for any gauge extension announcement.

---

## What the next runner needs to know

**Bottom line:** MICRO↔QFT is a legitimate category shift (the LOCK does NOT bind it), but the target category is **empty** for 4D gauge theory in the current literature. The cell-fill is CONJECTURED-NEGATIVE and durable.

**Key facts to carry forward:**

1. **The 9/10 LOCK surface is genuinely avoided.** The would-be Closure-M theorem does not invoke Taylor-coefficient identification via identity theorem on $F(t)$. RG-level matching via Callan-Symanzik is structurally distinct from function-level identification. Future Authors attempting MICRO↔QFT-style arguments can claim LOCK avoidance rigorously — if they produce them at the axiomatic-OPE level, not smuggling Taylor matching back in.

2. **The four open axioms are named.** NP-1' (BRST-extended non-perturbative gauge net), NP-3 (state existence — open even for scalar), NP-5 (non-perturbative OPE convergence — open for every theory), NP-6 (non-perturbative RG — open). Any future runner who reports "I closed H4 via microlocal/axiomatic OPE" must show which of these four axioms they closed, in what paper, with what primary-source evidence.

3. **The K-6 trap is real and subtle.** Hollands-Kopper 2011 perturbative OPE convergence is well-known and appears prominently in literature searches. An Author speaking microlocal dialect who quotes Hollands-Kopper as "OPE convergence for 4D QFT" without flagging the perturbative + scalar scope has re-hit the LOCK via K-6. Verbatim abstract quote: *"framework of the Euclidean $\phi^4$-quantum field theory in four dimensions... Our results hold for arbitrary, but finite, loop orders."* **Check this on any incoming microlocal claim.**

4. **BFR Dec 2025 §4 is verified scalar-only via primary source.** *"For an interacting scalar field this was analysed in a recent work by Buchholz and Fredenhagen"*; gauge extension absent. Future runners should not interpret BFR's phrase *"local nets of C\*-algebras for interacting theories"* as covering gauge without checking §4 verbatim.

5. **The Epstein-Glaser coefficient issue.** Even granting a non-perturbative gauge framework, $C_N$ is a scheme-dependent extension parameter in the microlocal formulation. Pinning it to $2(N^2-1)/\pi^6$ requires either non-perturbative RG (Axiom NP-6, open) or a scheme-independence theorem (Unlock 5, open). Future runners should not assume $C_N$ falls out of microlocal data automatically.

6. **For future MICRO↔QFT refinement:** the most realistic partial progress would be (a) a formal axiomatic system isolating the minimum set of properties forcing AF short-distance structure (done here as Axioms NP-1 through NP-7, but can be refined / minimized), and (b) scheme-independence analysis for $C_N$ at the perturbative level, as a template for the non-perturbative version.

7. **For the Wave 1 synthesis runner:** this cell is the MICRO↔QFT entry for capacitor v1 H4-specific expansion. It replaces the generic MICRO↔QFT line 97 entry with an H4-specific CONJECTURED-NEGATIVE entry. If the synthesis runner prefers, keep both (generic + H4-specific) as two rows. Capacitor fill rate impact: +1 durable cell (H4-specific MICRO↔QFT with explicit obstruction + unlock conditions).

8. **Compound-bypass pre-registration check.** The BLACKBOARD §K BYPASS-PREDICTION anticipated MICRO↔QFT as Step 1 of a 3-5-step compound bypass. My finding: Step 1 lands LEGITIMATELY (category shift is real, LOCK avoided) but Step 2 (framework construction) runs into four layers of open axioms. The pre-registered shape was correct in principle but mis-calibrated on how constructable the framework is. The runner should NOT re-plan: the prediction was correct about structure, incorrect only about accessibility in the budget window. Tier 2 (capacitor gains this cell) is the honest outcome.

9. **H4 is still the wall. The wall stays named. The capacitor gained the MICRO↔QFT H4-specific cell with four named unlock conditions. Paper 8 ships either way.**

---

*W1-M complete. Cell-fill: CONJECTURED-NEGATIVE with four named external unlocks. No new kills added to §F beyond K-6 reinforcement (which was already documented). The wall holds in the microlocal category too — but the bricks of the wall are now enumerated.*
