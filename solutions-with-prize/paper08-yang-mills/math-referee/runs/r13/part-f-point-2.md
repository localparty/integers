## Part F, Point 2: Reflection Positivity — The Full Chain

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: reflection positivity holds for the Wilson action (Osterwalder-Seiler 1978), and is preserved in the continuum limit by lower semicontinuity.

**(a) Lattice reflection positivity.** The Osterwalder-Seiler theorem (Ann. Phys. 110, 1978) gives RP for the Wilson plaquette action via the checkerboard decomposition. The KK-enhanced theory adds internal connections A_x at each site and bond couplings V_ell between sites. Appendix D, Lemma D.2 extends the OS argument to the full KK action.

The extension requires verifying that the bond coupling e^{-V_ell} has the positive-type kernel property. The paper shows: V_ell = (1/a^2) integral ||A' - U^{-1}AU||^2 dvol is a positive semi-definite quadratic form. The Boltzmann weight e^{-V_ell} is a Gaussian kernel, which is of positive type by Bochner's theorem (the Fourier transform of a Gaussian is positive). The Schur product theorem ensures that the product of positive-type kernels is positive-type. The total Boltzmann weight (product of Wilson plaquettes, internal actions, and bond couplings) satisfies the Osterwalder-Seiler checkerboard decomposition.

The argument is correct. The key insight is that all couplings are nearest-neighbor in time (temporal bonds couple fields at times t and t+a), which is exactly the structure required by Osterwalder-Seiler.

**(b) RP through the RG.** The paper explicitly states (Appendix D, Remark) that RP is NOT required at intermediate RG steps. The effective action S_k after k block-spin steps may violate RP. But this is harmless: the proof uses RP only at two levels:

  1. At the lattice level (to establish a self-adjoint positive transfer matrix with spectral gap)
  2. In the continuum limit (to satisfy OS3)

The intermediate RG steps use only the spectral properties of the transfer matrix (mass gap preservation), not RP. The spectral gap is preserved by the stability of deviation order argument, which is independent of RP.

This is correct. The RP is a property of the MEASURE (the Boltzmann weight), not of the effective action at intermediate scales.

**(c) RP in the continuum limit.** The lower semicontinuity argument: for lattice measures mu_a satisfying <theta f, f>_{mu_a} >= 0, the weak limit mu = lim mu_{a_j} satisfies <theta f, f>_mu >= 0 by the Portmanteau theorem.

The conditions: theta f * f must be a continuous bounded function of the field configuration. For Schwartz-class test functions f and compact gauge group SU(N):

  - Boundedness: the lattice fields are SU(N)-valued (compact), so all polynomial functionals are bounded. In the continuum limit, the fields are distributions, but the Schwinger functions S_n(f) are bounded for f in S by the uniform bounds.
  
  - Continuity: the map (configuration) -> <theta f, f> is continuous in the weak topology on measures (not on individual configurations). The weak convergence mu_{a_j} -> mu and the continuity of f -> S_n(f) ensure <theta f, f>_mu >= 0.

The argument is correct. The Portmanteau theorem applies because the integrand theta f * f is a bounded continuous function of the Schwinger functions (which converge weakly).

No error found. The RP chain is complete: lattice RP (Osterwalder-Seiler + Lemma D.2) -> continuum RP (Portmanteau/lower semicontinuity).

**Impact on the claimed result:** None. Reflection positivity is correctly established at both the lattice and continuum levels.
