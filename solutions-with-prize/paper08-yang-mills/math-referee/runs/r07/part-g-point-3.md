# G3: N-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

---

## Part G3, Point (a): N-Dependent Constants Tracking

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

The proof involves numerous constants that depend on the rank parameter N of SU(N). A systematic audit of the key N-dependent quantities:

| Quantity | N-dependence | Direction |
|----------|-------------|-----------|
| Spectral gap mu_1 | 2N/r_3^2 | Grows with N (helpful) |
| KK mass m_1 | sqrt(2N)/r_3 | Grows with N (helpful) |
| Propagator constant C_0 | Polynomial in N (via Weyl asymptotics ~ N^{N-2} and adjoint dim ~ N^2) | Grows with N |
| Cluster expansion threshold beta_max | ~ m_1 a / 6 | Grows with N (helpful) |
| Analyticity radius rho | Via r_{proj}(N) = 1/2 (N-independent) and kappa (weakly N-dependent) | Weakly N-dependent |
| Spectral lemma constant C_p | Via zeta, involving local Hilbert space dim ~ exp(CN^2) | Exponential in N^2 |
| Gronwall exponent gamma | alpha / (b_0 ln 2) where b_0 = 11N/(48 pi^2) | Decreases with N (helpful) |

The critical observation is: **for each fixed N, every constant is finite.** The proof works for each fixed N separately. The Clay Millennium Prize requires the mass gap for each fixed gauge group, not uniformly in N. Large-N asymptotics (the 't Hooft limit) are a separate problem entirely.

However, the constants grow with N -- some polynomially, some exponentially (notably the spectral lemma constant via exp(CN^2)). This means the mass gap bound Delta_inf becomes weaker for large N. For practical purposes this is irrelevant: the physically relevant cases are SU(2) and SU(3).

The gap is presentational: the preprint does not systematically track how each constant depends on N. A reader cannot currently verify at a glance that all constants remain finite for each fixed N without tracing through the entire argument. Adding 1-2 pages of systematic N-tracking (a table of constants with their N-dependence, analogous to the one above but complete) would close this gap.

**Impact on the claimed result:**

No mathematical gap. For each fixed N >= 2, all constants are finite and the proof goes through. The gap is a presentation issue: systematic N-dependence tracking should be made explicit. Estimated effort: 1-2 pages.

---

## Part G3, Point (b): SU(2) Special Properties

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

SU(2) has several special properties that could, in principle, make it a degenerate case where the proof works but fails to generalize:

1. **Cubic Casimir:** For SU(2), d^{abc} = 0 (no totally symmetric structure constants of rank 3). This means Tr(F^3) vanishes identically for SU(2), regardless of any symmetry argument.

2. **Internal space:** CP^1 = S^2, which has simpler geometry than CP^{N-1} for N >= 3.

3. **Exact area law:** The string tension takes the exact form sigma = 3g^2/8 for SU(2).

The proof does NOT rely on any of these SU(2)-specific properties:

- **Tr(F^3) elimination:** The proof uses C-symmetry (charge conjugation) to eliminate Tr(F^3) for ALL N >= 2. The operator Tr(F^3) is C-odd for any N. For N >= 3 where d^{abc} != 0, the C-symmetry argument is essential and non-trivial. For N = 2, the same argument applies but is redundant since Tr(F^3) = 0 identically. The proof uses the general mechanism, not the SU(2) shortcut.

- **CP^{N-1} geometry:** The spectral gap and Feshbach projection arguments are formulated for general N, using the spectral properties of the Laplacian on CP^{N-1}. The S^2 case is a special instance, not a separate argument.

- **String tension:** The exact area law value is a physics prediction, not a mathematical input to the proof (see G1, point (e)).

**Impact on the claimed result:**

None. The proof is genuinely uniform in its logical structure across all N >= 2. SU(2) is not a degenerate or special case that requires separate treatment.

---

## Part G3, Point (c): Error Compounding Across RG Steps

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

The Balaban RG program involves approximately 14 steps (block-spin transformations) to flow from the initial lattice spacing to the continuum limit. Each step involves estimates with N-dependent constants. The question is whether errors compound uncontrollably.

If each of the ~14 steps introduces a multiplicative factor of order N^p for some power p, the accumulated error grows as N^{14p}. For fixed N, this is a finite (albeit potentially large) constant. The proof requires only that:

1. Each individual constant is finite for each fixed N.
2. The composition of finitely many finite constants is finite.

Both conditions are trivially satisfied. The mass gap bound takes the schematic form:

> Delta_inf >= Delta_0 * exp(-gamma * K) * Product_{steps} (correction factors)

where each correction factor is a finite function of N. For each fixed N, this is a positive number.

The concern about error compounding is real in the sense that the final bound on Delta_inf may be astronomically small for large N. But it is positive, which is all the existence proof requires.

This is the same closable gap as point (a): systematic tracking of how constants propagate through the ~14 RG steps, with explicit N-dependence at each stage, would make the argument transparent. The mathematical content is already present; the exposition needs strengthening.

**Impact on the claimed result:**

No mathematical gap. The composition of finitely many finite constants is finite. The gap is presentational: the N-dependence of accumulated errors should be tracked systematically. This is the same 1-2 page addition recommended in point (a).

---

## Overall Assessment

**Verdict: CLOSABLE GAP**

The N-dependence issues are entirely presentational, not mathematical. For each fixed N >= 2, all constants in the proof are finite, the error accumulation across ~14 RG steps produces a finite (positive) result, and no SU(2)-specific properties are exploited. The closable gap is a systematic presentation of N-dependent constants and their propagation through the proof chain. Estimated effort: 1-2 additional pages consisting of a complete table of N-dependent constants with their scaling and a brief argument that the composition remains finite for each fixed N.
