## Part G, Point 4: Local Field Operators, Stress Tensor, OPE, and AF Matching

**Weight:** HEAVY
**Verdict:** **GENUINE GAP** — All four Jaffe–Witten requirements are either absent or only superficially addressed. This is a *direct* failure of Clay eligibility, independent of the mass-gap proof itself.

**Finding:**

The Jaffe–Witten problem statement (§4, verbatim from the Clay official PDF):

> "one should define a quantum field theory ... with **local quantum field operators** in correspondence with the gauge-invariant local polynomials in the curvature $F$ and its covariant derivatives, such as $\mathrm{Tr}\,F_{ij}F_{kl}(x)$. Correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory ... including ... the existence of a stress tensor and an operator product expansion, having prescribed local singularities predicted by asymptotic freedom."

These are FOUR distinct requirements: (a) local field operators, (b) AF matching, (c) stress tensor, (d) OPE. Each must be addressed.

(a) **Local field operators in correspondence with curvature polynomials.** The preprint constructs *Schwinger functions* via the OS reconstruction of gauge-invariant observables (plaquette traces, Wilson loops). It does NOT construct *operator-valued distributions* $\mathrm{Tr}\,F_{ij}F_{kl}(x) : \mathcal{S}(\mathbb{R}^4) \to \mathrm{Op}(\mathcal{H})$.

The §5.7(f) "Remark (Field operators and completeness)" addresses this:

> "The reconstructed Wightman theory has field operators that are gauge-invariant composite operators — the continuum limits of plaquette traces $\mathrm{Tr}(F_{\mu\nu}^2(x))$, higher Casimir operators $\mathrm{Tr}(F^n(x))$, Wilson loops $W_C$, and products thereof — rather than fundamental gluon fields $A_\mu^a(x)$."

The phrase "continuum limits of plaquette traces" is doing a lot of work here. What does "$\mathrm{Tr}(F_{\mu\nu}^2(x))$" mean as an operator on the GNS Hilbert space? The lattice plaquette $s_P(x) = 1 - (1/N)\mathrm{Re}\,\mathrm{Tr}\,U_P(x)$ has continuum limit $\sim (a^4 g^2/(2N)) \mathrm{Tr}(F_{\mu\nu}^2(x)) + O(a^6)$. So the lattice operator $s_P$, divided by $a^4 g^2/(2N)$, gives a *bare* lattice approximation to $\mathrm{Tr}(F_{\mu\nu}^2)$. As $a \to 0$, this bare operator does NOT converge to a finite operator on $\mathcal{H}$ — it has a UV divergence that requires multiplicative renormalization.

For gauge-invariant composite operators in Yang–Mills, the multiplicative renormalization is governed by the *anomalous dimension* of the operator. The Schwinger functions of the renormalized operator $[\mathrm{Tr}\,F_{\mu\nu}^2]_R(x)$ are obtained from the bare lattice correlators by multiplying by $Z_O(a)$, where $Z_O$ has logarithmic running matching the perturbative anomalous dimension.

**The preprint does not construct $Z_O$ or the renormalized operator.** It only takes continuum limits of *correlators* of bare lattice operators, which are *Schwinger functions*, not field operators.

This is the core issue: there is a difference between
- (i) constructing the Wightman field $\mathrm{Tr}\,F_{\mu\nu}^2(x)$ as an operator-valued distribution, with its anomalous dimension and short-distance behavior, and
- (ii) constructing Schwinger functions $\langle \prod \mathrm{Tr}\,F_{\mu\nu}^2(x_i)\rangle$ via OS reconstruction.

(i) requires (ii) plus a proper renormalization procedure. Jaffe–Witten asks for (i). The preprint provides (ii) and asserts (i) without the renormalization step.

**Concrete deficit:** For the operator $\mathcal{O}(x) = \mathrm{Tr}\,F_{\mu\nu}^2(x)$, the perturbative anomalous dimension is $\gamma_\mathcal{O}(g) = (something) \cdot g^2 + O(g^4)$ (computed by Hill 1996 and others for various gauge-invariant operators in YM). The renormalized operator's two-point function should have short-distance behavior $|x|^{-2(d_O + \gamma_O)}$ where $d_O = 4$ is the engineering dimension. The preprint's bound $|S_2(x, y)| \leq C |x-y|^{-2} e^{-\Delta|x-y|}$ uses $-2$ as the leading singularity, which is the *free* propagator behavior — *not* the AF-corrected one. **GENUINE GAP.**

(b) **Short-distance match to perturbative AF.** The preprint claims (§5.7(f) Proposition (Non-triviality), signature (iii)):
> "Asymptotic freedom: The running coupling $g_k^2 \sim 1/(b_0 k \ln 2)$ decreases logarithmically, with $b_0 = 11N/(48\pi^2) > 0$."

This is the *coupling* running with AF. But Jaffe–Witten asks for *correlation functions* to agree with AF predictions at short distances. Specifically, the two-point function $\langle \mathrm{Tr}\,F_{\mu\nu}(x) \mathrm{Tr}\,F_{\rho\sigma}(y)\rangle$ should reproduce the perturbative QCD prediction with AF logarithmic running for $|x-y| \to 0$.

This requires:
1. Constructing the renormalized two-point function (point (a) above).
2. Computing its short-distance asymptotics.
3. Comparing with the one-loop (and ideally higher-loop) perturbative result.

The preprint does NONE of these. It only gives a bound $|S_2| \leq C|x-y|^{-2}$ (without the AF logarithmic factor), which does not agree with AF predictions. **GENUINE GAP.**

(c) **Stress tensor.** The preprint does NOT construct a stress-energy tensor $T_{\mu\nu}(x)$ on the reconstructed Hilbert space. This is a non-trivial requirement: for gauge theories, the canonical stress tensor is gauge-non-invariant, so an "improved" (gauge-invariant) stress tensor must be constructed. Standard procedures (Belinfante–Rosenfeld improvement, conformal improvement, etc.) exist in perturbation theory but not in the rigorous lattice/Wightman setting.

The preprint does not even *mention* the stress tensor. **GENUINE GAP.**

(d) **Operator product expansion with AF singularities.** The preprint does NOT establish an OPE. The §5.7(f) "Coincident-point singularities" lemma claims (without derivation):
> "for gauge-invariant operators in a massive theory, the OPE gives $|S_n| \leq C^n n! \prod |x_i - x_{i+1}|^{-2}$"

This is a *conjecture*, not a derivation. The preprint says "the OPE gives" — but no OPE has been constructed. The bound is asserted to follow from "the OPE", but the OPE is exactly what Jaffe–Witten asks for.

A rigorous OPE for gauge-invariant operators in Yang–Mills would require:
1. Constructing the algebra of local operators on the Hilbert space.
2. Establishing the short-distance expansion $\mathcal{O}_1(x) \mathcal{O}_2(y) \sim \sum_k C_{12}^k(x-y) \mathcal{O}_k\bigl(\frac{x+y}{2}\bigr)$.
3. Computing the OPE coefficients $C_{12}^k(x-y)$ to leading order in $|x-y|$.
4. Verifying that the leading singularities match the AF-corrected dimensions.

The preprint does NONE of these. **GENUINE GAP.**

(e) **Closure difficulty.** Each of (a)–(d) is a substantive piece of constructive QFT. Constructing renormalized composite operators with AF-matched short-distance behavior is the subject of an entire research program (Wilson, Kadanoff, Symanzik, Brandt, Lowenstein, Schroer, ...) and has *never* been carried out rigorously for non-Abelian gauge theory in 4D. The Hollands–Wald program for QFT in curved spacetime gives an OPE construction for free fields, but the gauge-theory version is open.

For Clay purposes:
- (a) and (b) might be addressed with 1–2 papers worth of work, building on the preprint's Schwinger function construction.
- (c) (stress tensor) would require an additional 1–2 papers.
- (d) (OPE) would require an additional 1+ papers, possibly a full research program.

**Total estimated additional work to meet the full Clay requirement: 3–5 papers, plus the K-vs-k notation cleanup.**

**Impact on the claimed result:** This is the *direct* Clay-eligibility gap. Even if the mass-gap proof itself were complete (modulo Point C1), the absence of (a)–(d) means the constructed object is not "a quantum field theory" in the Jaffe–Witten sense. It is *Schwinger functions of gauge-invariant lattice observables, with a positive mass gap*, but not a Wightman QFT with local field operators in correspondence with curvature polynomials, a stress tensor, an OPE, or short-distance AF agreement.

**This is the most credibility-destroying gap from a Clay perspective**, on par with the K-vs-k issue. A Clay submission as currently written would be returned as "not addressing the specified problem."
