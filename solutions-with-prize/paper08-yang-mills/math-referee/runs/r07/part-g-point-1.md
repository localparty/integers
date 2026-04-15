# G1: Jaffe-Witten Requirements

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

---

## Part G1, Point (a): The KK Device and Decoupling

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The proof chain proceeds in three stages:

1. **Theorem 4:** Establishes the spectral gap on the KK-enhanced theory, Delta_0^{KK} > 0.
2. **Theorem 5 (Feshbach projection):** Projects down to the standard theory, yielding Delta_0^{std} > 0 at the initial lattice spacing.
3. **Section 5 (Balaban RG):** Takes the continuum limit Delta_inf > 0 using Balaban's renormalization group program.

After Theorem 5, the KK enhancement is fully decoupled. Section 5 applies Balaban's RG to the STANDARD SU(N) Wilson lattice gauge theory. Balaban's entire program (multi-scale cluster expansions, block-spin transformations, polymer representations) was developed for the standard theory, not any KK-enhanced variant.

The KK device serves a single purpose: establishing the starting condition Delta_0 > 0 at the initial lattice spacing. Once this seed gap is obtained, the continuum limit argument uses only standard lattice gauge theory. The final theory lives on R^4 with no auxiliary compact dimensions or other residual structure.

This is analogous to using a particular regularization scheme to establish an initial condition, then running a standard RG flow. The auxiliary structure is scaffolding, not part of the final building.

**Impact on the claimed result:**

None. The KK device is a legitimate mathematical tool that is cleanly removed before the continuum limit is taken. The final Schwinger functions and mass gap are properties of standard SU(N) Yang-Mills on R^4.

---

## Part G1, Point (b): Gauge Group Coverage

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

The Jaffe-Witten problem requires the result for "any compact simple gauge group G." The preprint works exclusively with SU(N) for N >= 2. This does NOT cover:

- **Exceptional groups:** G_2, F_4, E_6, E_7, E_8
- **Orthogonal groups:** SO(N) for N >= 3
- **Symplectic groups:** Sp(N) for N >= 1

The preprint should explicitly state this limitation.

The SU(N) result is the most physically important case: the Standard Model uses SU(2) (electroweak) and SU(3) (QCD). From a mathematical standpoint, the method might extend to other groups by replacing the internal space CP^{N-1} with an appropriate homogeneous space:

- **SO(N):** Real Grassmannians SO(N)/SO(N-2) x SO(2), or real projective spaces RP^{N-1}
- **Sp(N):** Quaternionic projective spaces HP^{N-1}
- **Exceptional groups:** Appropriate homogeneous spaces G/H with suitable spectral gap properties

Each extension requires: (i) identifying an internal space with a spectral gap that grows with the appropriate parameters, (ii) verifying that the Feshbach projection decouples cleanly, and (iii) confirming that all constants remain controlled. This is non-trivial and constitutes a separate paper for each family.

**Impact on the claimed result:**

This is the most significant limitation for full Jaffe-Witten compliance. The proof as written establishes: "For SU(N) with N >= 2, there exists a continuum Yang-Mills theory satisfying OS axioms with mass gap." Whether the Clay SAB would accept a partial result covering only SU(N) is a judgment call, not a mathematical question. The SU(N) result alone is a major achievement.

---

## Part G1, Point (c): Lattice Regulator Independence

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The final theory is independent of the lattice regularization in the following precise sense: the continuum Schwinger functions satisfy the Osterwalder-Schrader axioms OS1-OS5, and the mass gap Delta_inf > 0 is a property of the continuum limit, not of any particular lattice.

Different lattice regularizations (Wilson action, Symanzik-improved action, etc.) would yield the same continuum limit if universality holds. The preprint does not prove universality, but this is not required. The Jaffe-Witten problem asks for the EXISTENCE of a Yang-Mills quantum field theory with mass gap, not for uniqueness of the continuum limit or universality across regularization schemes.

The proof constructs one particular continuum limit (via Wilson's lattice formulation and Balaban's RG) and shows it has the required properties. This suffices.

**Impact on the claimed result:**

None. The existence claim is well-posed and does not depend on universality.

---

## Part G1, Point (d): Precise Claim and Clay Prize Scope

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

The precise claim established by the preprint is:

> For SU(N) with N >= 2, starting from Wilson's lattice gauge theory, there exists a subsequential continuum limit satisfying OS1-OS5 with mass gap Delta_inf > 0.

This IS sufficient for the Clay Millennium Prize restricted to SU(N). The additional steps needed for the full Jaffe-Witten statement are:

1. **Extension to all compact simple groups** (separate paper for each family, as discussed in point (b)).
2. **Uniqueness of the continuum limit** (an open problem in constructive QFT, not required by Jaffe-Witten).

The word "subsequential" is standard in constructive QFT: one extracts a convergent subsequence from the lattice approximations. The Jaffe-Witten problem does not require uniqueness of the limit, only existence.

**Impact on the claimed result:**

The SU(N) restriction is the only substantive limitation. The result as stated for SU(N) is mathematically precise, correctly scoped, and represents a major advance even if the Clay SAB requires the full gauge group coverage.

---

## Part G1, Point (e): Quantitative Predictions

**Weight:** HEAVY
**Verdict:** SOUND

**Finding:**

The preprint includes quantitative predictions such as the string tension sqrt(sigma) = 437 MeV, glueball masses, and other physical quantities. These do NOT enter the mathematical proof in any way. The proof works for any value of the physical parameters; it establishes the existence of a mass gap without requiring any specific numerical value.

The quantitative predictions serve as physics consistency checks: they verify that the constructed theory matches known lattice Monte Carlo results and experimental data. This is important for physical credibility but irrelevant to mathematical rigor.

No step in the proof chain (KK spectral gap -> Feshbach projection -> Balaban RG -> continuum limit) uses any specific numerical value of a physical quantity. All bounds are qualitative (finite, positive, controlled) rather than quantitative.

**Impact on the claimed result:**

None. The quantitative predictions are supplementary material that strengthens the physical motivation but does not affect the mathematical argument.

---

## Overall Assessment

**Verdict: CLOSABLE GAP**

The gauge group limitation (SU(N) only, not all compact simple G) is the most significant issue for full Jaffe-Witten compliance. The KK decoupling mechanism is sound, the lattice independence is correctly handled, and the quantitative predictions are properly separated from the proof. The precise claim for SU(N) is mathematically well-posed and represents a major result. Extension to other gauge groups is a closable gap requiring separate work for each family of compact simple groups.
