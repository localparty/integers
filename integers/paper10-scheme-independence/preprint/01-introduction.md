# §1 — Introduction

## §1.1 Why Scheme-Independence Matters

A result proved within a specific regularization scheme is not, without further
argument, a statement about physical observables. In quantum gravity, where the
theory is non-renormalizable and every counterterm introduces a physically
observable new coupling, this distinction is particularly sharp. A counterterm
coefficient that is zero in zeta regularization but nonzero in dimensional
regularization would not represent UV finiteness — it would represent a
scheme-dependent artifact.

The Goroff-Sagnotti R³ divergence in 4D pure Einstein gravity — the leading
obstruction to renormalizability — provides the prototype. Goroff and Sagnotti
(1986), confirmed independently by van de Ven (1992), computed the two-loop
divergence in dimensional regularization and found:

    Γ^{(2)}_{div} = (209 / (2880 (16π²)² ε)) ∫ d⁴x √(−g) C^{αβ}_{μν} C^{ρσ}_{αβ} C^{μν}_{ρσ}

This coefficient is scheme-independent in the following precise sense: the
coefficient 209/2880 is fixed by the on-shell S-matrix. Any regularization scheme
that correctly computes the two-loop S-matrix in 4D pure gravity must produce this
coefficient. Its non-vanishing is therefore a physical statement about the theory,
not a regularization artifact. The absence of the Goroff-Sagnotti counterterm in
5D KK gravity — established in Paper 1 via zeta regularization — should be equally
scheme-independent, or else it cannot be claimed as a physical result.

More precisely: in a non-renormalizable theory, finite counterterms at each loop
order are genuinely observable (they correspond to new couplings with measurable
consequences at sufficiently high energy). Two regularization schemes can differ
in the finite parts of counterterms. But they cannot disagree on whether a
divergent counterterm is generated or not — because the divergent part determines
whether a new coupling must be introduced at each loop order to absorb the
divergence. If the counterterm coefficient is zero in one scheme and nonzero in
another, then one scheme is predicting a new, observable coupling that the other
is not. This is a physical difference, not merely a technical one.

Paper 1 is explicit on this point. Appendix U §U.2c states: "A critical question
that the present paper does not resolve is whether the vanishing of the R³
counterterm under zeta regularization is a scheme-independent property of a
physical observable, or a feature of the particular regularization used." Paper 10
addresses this open problem.

## §1.2 What Paper 1 Established and Where It Stopped

Paper 1 (Appendix K, Theorem K.1 — Universal Epstein Vanishing) proves that in
5D linearized gravity on M⁴ × S¹/Z₂, the Goroff-Sagnotti R³ counterterm
coefficient, when the KK mode sums are regulated by spectral zeta regularization,
vanishes at every loop order. The proof proceeds via the Epstein zeta identity:

    E_L(−j; Q) = 0   for all integers j ≥ 1

which follows from 1/Γ(−j) = 0 — a mathematical identity about the Gamma function.
The completed Epstein function Λ(s) = π^{−s} Γ(s) E_L(s; Q) is meromorphic with
poles only at s = 0 and s = L/2. At s = −j (j ≥ 1), Λ(−j) is finite; since
E_L(s; Q) = π^s Λ(s)/Γ(s), the factor 1/Γ(−j) = 0 forces E_L(−j; Q) = 0.

At one loop, the leading cancellation takes the form S₀ = 1 + 2ζ_R(0) = 0, where
ζ_R(0) = −1/2 is the value of the Riemann zeta function at s = 0 under analytic
continuation. Paper 1 notes that this value arises from a regularization-specific
choice and does not constitute a proof that a different scheme would give the same
answer.

Paper 1 Appendix U further analyses four gaps between the structural argument and
a complete proof: (1) vertex mass-independence (do KK-decomposed graviton vertices
produce n-dependent factors that survive at leading UV order?); (2) degree-of-freedom
counting (the massless n = 0 graviton has 2 helicities, massive KK gravitons have 5);
(3) product regularization (is [Σ_n 1]² = 0² the correct form of the double sum?);
(4) no explicit two-loop KK computation exists in the literature. Paper 1 Appendix U
resolves gaps (2), (3), and most of (4) — reducing the scheme-independence question
to gap (1), the vertex mass-independence problem, as the primary remaining issue.

## §1.3 Overview of the Five Routes and Their Verdicts

Five independent research routes were developed as preparation for this paper. Each
attacks the scheme-independence question from a different mathematical direction;
their convergence on the same conclusion constitutes the strongest available evidence
for scheme-independent UV finiteness.

**Route 01 — Number-theoretic / Epstein zeros.** Examines whether the zeta
regularization result corresponds to a trivial zero of ζ_R or to the broader class
of Epstein universal zeros. Result: the subleading KK sums land at E_L(−j; Q) = 0,
arising from 1/Γ(−j) = 0, a number-theoretic identity independent of regularization.
The leading S₀ cancellation uses ζ_R(0) = −1/2, which is scheme-sensitive, but
both zeta-reg and dim-reg reproduce it via the same analytic continuation. The
y-integral computation of the three-graviton vertex is complete and shows the triangle
coupling I_{+++}(n₁, n₂, n₁+n₂) = πR/4 is mass-independent. Status: Proved
(Theorem 1, Lemmas A1–A3); A1 proved (Lemma A1; research memo
`integers/paper10-scheme-independence/research/02-de-donder-gauge-vertex.md`); A2 proved (Lemma A2; research memo
`integers/paper10-scheme-independence/research/03-a2-graviphoton-radion-sector.md`); A3 proved (Lemma A3; research
memo `integers/paper10-scheme-independence/research/04-a3-kk-loop-momentum-range.md`).

**Route 02 — Seeley-DeWitt / heat kernel.** Computes the Seeley-DeWitt coefficients
a₂ and a₄ for the Lichnerowicz operator on flat M⁴ × S¹/Z₂ directly from the
operator symbol, without any regularization prescription. Both vanish. This is an
outright proof of one-loop scheme-independent UV finiteness. Status: proved (one-loop,
flat background); extension to all a_{2k} via the Gel'fand-Yaglom generating function
is proposed but not yet complete.

**Route 03 — Z₂ parity cancellation.** Shows that for each KK level n ≥ 1, the
contribution of the Z₂-even graviton sector to the Goroff-Sagnotti coefficient is
exactly cancelled by the contribution of the Z₂-odd graviphoton sector. The
cancellation is algebraic (term-by-term before any summation) and holds in all
Z₂-preserving regularization schemes. Status: strong structural result; gap in
mixed-sector vertices (diagrams with both h_{μν} and h_{μ5} internal lines).

**Route 04 — Poisson dim-reg bridge.** Establishes via the exchange lemma (proved
by Poisson resummation and exponential convergence of the winding-mode sum) that
the dim-reg pole coefficient of the two-loop GS counterterm equals the zeta-reg
coefficient S₀ = 0. The two schemes differ by an exponentially suppressed finite
residual of order e^{−2πRk}. Status: demonstrated at structural order; vertex
mass-independence assumed.

**Route 05 — Weyl anomaly / KK tower.** Uses the Wess-Zumino consistency condition
to prove that the 4D Weyl anomaly coefficients (a, c) cannot be shifted by any local
counterterm in any diffeomorphism-preserving scheme. Since a_total = c_total = 0
under zeta regularization (using mass independence of a₄ and S₀ = 0), they vanish
in every diffeomorphism-preserving scheme. Since the Goroff-Sagnotti C³ operator is
in the c sector, it is not generated by the KK tower in any such scheme. Status:
proved for the GS sector; orbifold boundary a₄ coefficient not yet computed
explicitly.

The y-integral part of the three-graviton vertex KK decomposition is complete
(research memo `integers/paper10-scheme-independence/research/01-three-graviton-vertex.md`): the triangle coupling
I_{+++}(n₁, n₂, n₁+n₂) = πR/4 is mass-independent, and diagonal couplings
I_{+++}(n,n,n) = 0 are absent from the GS sunset. All three assumptions are proved:
A1 (Lemma A1; de Donder gauge vertex numerator), A2 (Lemma A2; graviphoton/radion
decoupling from GS counterterm by index structure and Z₂ selection rules), and A3
(Lemma A3; method-of-images KK loop momentum range). All five routes promote to
complete unconditional proofs. Theorem 1 is proved.

## §1.4 Paper Outline

Section 2 presents the Seeley-DeWitt framework and the outright proof of
one-loop scheme-independent UV finiteness (Route 02). This is the anchor result:
clean, rigorous, and accessible without detailed knowledge of the other routes.

Section 3 presents the Z₂ parity mechanism (Route 03): the algebraic cancellation
that explains why the Goroff-Sagnotti coefficient is zero in all Z₂-preserving
schemes. This section is the conceptual core — it explains the physics of the
vanishing without appeal to any specific regularization identity.

Section 4 presents the Poisson dim-reg bridge (Route 04) and the Weyl anomaly
proof (Route 05) in combination. The Poisson argument establishes equivalence
between the two most common regularization schemes; the Weyl anomaly argument
then extends the conclusion to all diffeomorphism-preserving schemes by the
cohomological argument.

Section 5 collects open problems: the vertex mass-independence conjecture, the
extension of the Seeley-DeWitt proof to all a_{2k} via Gel'fand-Yaglom, curved
backgrounds, the full non-linear theory, and the connection to the cosmological
constant isolation of Paper 1 Theorem U.

Throughout, results are labelled Theorem, Lemma, Proposition, or Conjecture, with
Proof or Proof sketch, according to the rigour of the argument in hand.

## §1.5 Notation

The following notation is used consistently throughout.

**Geometry.** M⁴ denotes flat Euclidean four-dimensional space with metric
δ_{μν}. K denotes the compact space S¹/Z₂ = [0, πR], with R the compactification
radius. The full five-dimensional manifold is M⁴ × K. Capital Roman indices
M, N, ... run over {0, 1, 2, 3, 5}; Greek indices μ, ν, ... over {0, 1, 2, 3}.
The fifth coordinate is y ∈ [0, πR].

**Fields.** The 5D metric fluctuation is h_{MN}. Under the Z₂ reflection y → −y,
it decomposes as: h_{μν} (Z₂-even, zero or positive parity +1), h_{μ5}
(Z₂-odd, parity −1), h_{55} (Z₂-even, parity +1). KK masses are m_n = n/R for
n ∈ Z (or n ≥ 0 on the orbifold).

**Operator.** L denotes the Lichnerowicz operator acting on symmetric 2-tensors:
on the flat background, L = −∇^A ∇_A (pure Laplacian, E = 0 in the Vassilevich
notation D = −∇² − E).

**Regularization.** ζ_R denotes the Riemann zeta function. E_L(s; Q) denotes the
Epstein zeta function for a positive-definite quadratic form Q in L variables.
S₀ = 1 + 2ζ_R(0) = 0 is the regularized count of KK modes on S¹ (Paper 1, §F).
a_k and c_k denote the Seeley-DeWitt coefficients (Vassilevich 2003 convention).

**Cross-references.** References to Paper 1 sections are given by full section
name (e.g., "Paper 1, Appendix U §U.2c") rather than by number alone.
