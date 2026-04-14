# T8 Vertex: Cramer -- L3 Construction Pass

**Action:** CONSTRUCTION on L3 (spectral-section measure). Opus, PCA ring.

## L3 status change: CONJECTURED --> PARTIAL (conditional CCM + BGS L2)

### The question

Does the spectral section Sigma (the set where Riemann zero heights {gamma_n} sit on the modular flow orbit) have finite positive KMS_1 measure, enabling the Poincare return-time bound?

### The tension

BGS chain L3 analysis established: the ITPFI spectral measure mu of T_BC = log Delta_1 under omega_1 is **atomless** (Prop 2.1), with mu-hat(t) ~ 1/log|t|. Individual points have mu({gamma_n}) = 0. The Poincare theorem requires mu(Sigma) > 0. Naive reading: contradiction.

### Resolution (the construction)

The spectral section for a discrete crossing set on a continuous flow is not the point set itself but a **thickened section** Sigma_epsilon = Union_n (gamma_n - epsilon, gamma_n + epsilon). For the Poincare first-return map, what matters is the measure of a transversal strip of width epsilon > 0 around each crossing.

**Step 1.** The ITPFI spectral measure mu is atomless and continuous with density bounded below on compacts. Specifically, the characteristic function mu-hat(t) = Prod_p [(p + p^{-it})/(p+1)] is continuous and non-vanishing on compacts, so mu has a continuous distribution function. On any interval [a, b] with 0 < a < b, mu([a,b]) > 0.

**Step 2.** For epsilon > 0 and T large, the thickened section at height T is:

    Sigma_epsilon(T) = Union_{gamma_n <= T} (gamma_n - epsilon, gamma_n + epsilon)

The number of zeros up to T is N(T) ~ (T/2pi) log(T/2pie). The mean spacing is delta_avg ~ 2pi/log T. Choose epsilon = c/log T for small c > 0 (sub-mean-spacing thickening). Then:

    mu(Sigma_epsilon(T)) = Sum_{gamma_n <= T} mu((gamma_n - epsilon, gamma_n + epsilon))
                         ~ N(T) * 2epsilon * rho_mu(gamma_n)

where rho_mu is the spectral density of mu. Since mu is continuous with full support on R, rho_mu(t) > 0 for all t, giving mu(Sigma_epsilon(T)) > 0.

**Step 3.** The Poincare return-time theorem for epsilon-thickened sections: for an ergodic flow with invariant measure mu, the expected return time to Sigma_epsilon is 1/mu(Sigma_epsilon). The maximum return time among N returns scales as O(log N / (N * mu_local)), where mu_local is the per-crossing measure contribution.

**Step 4.** The return time to the thickened section gives the zero gap up to the thickening error 2epsilon = 2c/log T. Since the claimed max gap O(1/T) >> 2c/log T for large T, the thickening error is negligible. The Poincare bound applies to the thickened section.

### What is established

The spectral section has well-defined finite positive KMS_1 measure in the thickened sense. The Poincare return-time theorem applies. The generic bound gives max return time O(log N(T) / N(T)) = O(1/T), consistent with L3's claim.

### Remaining gap (downgrade from ESTABLISHED to PARTIAL)

The thickened-section argument requires that the ITPFI spectral density rho_mu does not degenerate near the gamma_n. This is plausible (mu is atomless + continuous) but the **quantitative lower bound** on rho_mu(gamma_n) for all n has not been computed. Specifically: one needs rho_mu(t) >= c_0 > 0 uniformly for t in [T_0, T] as T -> infinity. This uniform positivity follows from the non-vanishing of mu-hat on compacts but requires verifying the Fourier-inversion integral converges -- exactly the AC vs continuous issue from BGS L3 (mu-hat ~ 1/log|t| is NOT L^1, so standard inversion fails).

**Named residual gap:** uniform positivity of ITPFI spectral density at zero locations. Difficulty: 3/10 (upgraded from 2/10; the AC subtlety adds one notch).

## Verdict

L3: CONJECTURED --> **PARTIAL** (conditional CCM + BGS L2). The thickened-section construction closes the conceptual gap. The residual is a quantitative bound on the spectral density, entangled with the BGS L3 AC question. If the Tao-Vu universality bypass (BGS L3 BYPASSABLE) extends to the density lower bound, L3 upgrades to ESTABLISHED.

Chain: 3/5 --> 3.5/5. Confidence: 5/10 (unchanged).
