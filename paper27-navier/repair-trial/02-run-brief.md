# Paper 27 Navier-Stokes -- Repair Run Brief

*Mode: EXCISE + CONSTRUCT (Tier B first, Tier C if needed)*
*Date: 2026-04-13*
*Chain source: paper27-navier/strategy/01-navier-proof-chain.md*
*Capacitor: paper27-navier/repair-trial/03-capacitor.md*

---

## Target

The NS proof chain (16 steps, 10 load-bearing), specifically the 8 OPEN steps at confidence 2-6/10. Three primary targets (Steps 8, 11, 13b) where the chain lives or dies. Five secondary targets (Steps 6, 9, 12, 13a, 14) that likely follow if the primaries close.

## Mode

EXCISE + CONSTRUCT. NOT verification.

- **EXCISE (Tier B):** Find alternative proofs of the same result via different routes -- literature precedent, Six Patterns from different angle, transposition dictionary.
- **CONSTRUCT (Tier C):** If all Tier B routes fail, build something new -- larger system, restored projected structure, alternative chain.
- **LOCKED:** Steps 1, 2, 3, 4, 5, 7, 10, 15 are ESTABLISHED. Do not spend agents on them.

---

## Primary targets

### Priority 1: Step 8* -- Velocity-field algebra is type III_1

**What it is:** Construct a von Neumann algebra M_u from the NS velocity field via GNS of the Weyl algebra W(sdiff) at energy shell E. Prove M_u is a factor of type III_1.

**Why it matters:** If Step 8 fails, everything downstream collapses. Steps 9, 11, 12, 13a, 13b, 14 all depend on it.

**Current state:** OPEN. Confidence 3/10. No precedent in the literature for building a type III_1 factor directly from a classical PDE solution.

**Approaches to dispatch (one Author per approach, all parallel):**

- **Approach A (current chain):** GNS of Weyl algebra W(sdiff) at energy E. The quasi-free state phi_E on W(sdiff,sigma) where sigma is the symplectic form from L^2 inner product on divergence-free fields. Show that the GNS representation yields a type III_1 factor by computing the S-invariant S(M_u) = [0,inf). This requires showing: (i) M_u is a factor (no center), (ii) no trace exists, (iii) S-invariant has no gaps. The sdiff Lie bracket must enter explicitly in the construction of sigma.

- **Approach B (Tier B: Ojima-Saigo 2003):** Ojima and Saigo published an OA formulation of turbulence scaling. Adapt their construction for NS specifically. They work with KMS states on the CCR algebra over turbulent fields. The key question: does their construction produce type III_1 specifically, or only type III generally? WebSearch for "Ojima Saigo turbulence operator algebra type III" to retrieve the paper.

- **Approach C (Tier B: crossed product construction):** Build M_u = L^inf(velocity configurations) rtimes_{alpha_t} R where alpha_t is the NS time evolution semigroup. This is a standard crossed-product construction. To verify type III_1: show that the NS flow is not periodic (rules out III_lambda for lambda < 1) and not approximately periodic (rules out type II). The sdiff Lie bracket enters through the specific form of alpha_t. This may be easier to verify than the Weyl algebra route.

- **Approach D (Tier B: type III_1 by exclusion):** Instead of constructing M_u and computing S(M_u), prove type III_1 by eliminating all other types:
  - Not type I: M_u has no minimal projections (turbulent flow has no atomic structure)
  - Not type II: no trace (no finite-valued normal faithful tracial state, because the energy cascade creates scale-dependent weights)
  - Not type III_lambda for 0 < lambda < 1: the S-invariant is not {0} union {lambda^n : n in Z} because there is no preferred scale ratio in the inertial range (continuous self-similarity)
  - Not type III_0: the T-set is not {0} (modular flow period would require a characteristic time, but the inertial range is scale-free)
  - Therefore type III_1.

**Tao filter checkpoint for Step 8:** The GNS construction MUST use the specific sdiff Lie bracket [X,Y] = curl(X x Y). Generic Weyl algebras over L^2 divergence-free fields do NOT distinguish true NS from averaged NS. The symplectic form sigma must encode the noncommutative phase structure of the bilinear term. Averaged NS has a DIFFERENT sigma (randomized phases) and the claim is that this different sigma produces a DIFFERENT type (possibly type II or type III_lambda, not III_1).

---

### Priority 2: Step 11* -- Dissipation quotient preserves type III_1

**What it is:** NS is dissipative (nu * Delta u term). The viscous modular operator is Delta_nu = Delta_phi * e^{-nu*t*A}. The quotient M_u / J_nu (where J_nu is the ideal of viscously damped modes below Kolmogorov scale eta) must remain type III_1.

**Why it matters:** This is the NS-specific obstacle. No other Millennium chain has a dissipation quotient. If the quotient destroys type III_1, the entire modular flow argument breaks.

**Current state:** OPEN. Confidence 2/10. Known obstacle per K-NS-10 (gauge analogy fails).

**Approaches to dispatch:**

- **Approach A (current chain, hard):** Prove M_u/J_nu directly preserves type. This requires: (i) J_nu is a proper two-sided ideal in M_u, (ii) the quotient is still a factor, (iii) the quotient is still type III_1. The gauge analogy (redundant vs physical degrees of freedom) fails per K-NS-10. Must prove directly.

- **Approach B (Tier B: stochastic NS):** Use Albeverio-Cruzeiro (1990) stochastic NS. Add noise to absorb dissipation. The stochastic NS has an invariant measure mu. Build M_u from (L^inf(velocity configs, mu), mu) directly. No quotient needed because dissipation is absorbed into the noise. Type III_1 follows if mu is non-atomic and scale-free.

- **Approach C (Tier B: Foias-Temam Gevrey):** Foias-Temam (1989) proved that NS solutions are Gevrey-1 (analyticity radius bounded below). If true, vorticity coefficients decay SUPER-EXPONENTIALLY: |omega_hat_k| <= C * exp(-c * |k|^{1/s}). This is MUCH stronger than what Step 13 needs. Bypasses the quotient entirely by providing the coefficient bound directly.

- **Approach D (Tier C: P6 NO QUOTIENT -- most promising escape):** Do NOT quotient at all. Argue that the full dissipative algebra (including all viscously damped modes) is STILL type III_1. Rationale: dissipation enriches the algebra (adds a semigroup of completely positive maps), it doesn't impoverish it. The damped modes at scale below eta still contribute to the type classification because they participate in the energy cascade. Show: J_nu is NOT an ideal in M_u (viscous damping does not define a two-sided ideal because it does not commute with the nonlinear term). Therefore the quotient M_u/J_nu does not exist as stated, and the full M_u is the correct object.

**Tao filter checkpoint for Step 11:** Stochastic NS (Approach B) must check whether adding noise to averaged NS would also regularize it. Gevrey regularity (Approach C) is PDE-specific and automatically passes the Tao filter. The P6 no-quotient route (Approach D) must argue that the full dissipative algebra for averaged NS is NOT type III_1 (different type because averaged bilinear term has different algebraic structure).

---

### Priority 3: Step 13b* -- Crossed-product trace gives vorticity bound

**What it is:** On the type II_inf crossed product N = M_u rtimes_sigma R with semifinite trace Tr_tau (Connes-Takesaki 1977), the Tr_tau-finiteness of the vorticity operator omega^* omega, combined with the spectral density from Step 13a and the Fourier-to-modular bridge lambda_k <-> e^{-2*pi*s_k}, gives: |omega_hat_k(t)|^2 <= C * lambda_k^{-1+delta} for delta > 0 uniform in t.

**Why it matters:** This is the critical bridge between operator algebras and PDE. Where most OA approaches to PDE fail. Confidence 2/10.

**Current state:** OPEN. The Fourier-to-modular bridge lambda_k <-> e^{-2*pi*s_k} needs explicit construction. Critic v1 WEAKENED (repairs R2 + R3 applied).

**Approaches to dispatch:**

- **Approach A (current chain):** Build the Fourier-to-modular bridge explicitly. The Stokes eigenvalue lambda_k becomes the modular spectral parameter s_k via lambda_k = e^{2*pi*s_k}. This identification comes from the KMS condition: the modular flow acts on Fourier shells as dilation (Step 9), so the modular spectral parameter IS the log of the Stokes eigenvalue. Compute Tr_tau(omega^* omega) on N using Parseval on the crossed product. The coefficient bound follows from finiteness of the trace and the spectral density.

- **Approach B (Tier B: Ladyzhenskaya-Prodi-Serrin + Step 6):** The LPS criteria give: if u in L^p_t L^q_x with 2/p + 3/q <= 1, then regularity. Combine with the meromorphic structure of Z_omega (Step 6) to close the gap. The zeta function provides the missing spectral control. This is a HYBRID approach (classical PDE + spectral zeta, no OA).

- **Approach C (Tier B: Haagerup L^p spaces):** Work in the Haagerup L^p spaces L^p(M_u, phi_E) for p=1. Show the vorticity operator is trace-class in L^1(M_u, phi_E). The L^1 norm gives the coefficient bound. This uses the specific type III_1 structure (Haagerup L^p well-defined for type III) but the quantitative content comes from the sdiff construction (spectral density).

- **Approach D (Tier C: P5 PURE ZETA BYPASS -- most promising escape):** Skip the crossed product entirely. Show that Z_omega(s,t) satisfies a FUNCTIONAL EQUATION inherited from the Stokes operator symmetry on T^3. Specifically: Z_omega(s,t) should satisfy a relation analogous to the Epstein zeta functional equation, reflecting the lattice symmetry of T^3. The functional equation at s=0 gives the enstrophy bound DIRECTLY: Z_omega(0,t) = ||omega||^2 expressed in terms of the residue at s=3/2 (proportional to ||omega||_{L^2}^2 by Step 6) plus computable lower-order terms. The bound follows from control of the residue via energy inequality.

- **Approach E (Tier C: classical bypass):** Abandon the OA bridge entirely. Use Z_omega meromorphic structure (Step 6) + direct PDE estimates (Steps 1-5) to bound Z_omega(0,t). Lose the OA content but potentially save the proof. The meromorphic continuation + Weyl asymptotics may be enough for enstrophy control without any operator algebra input.

**Tao filter checkpoint for Step 13b:** The Fourier-to-modular bridge (Approach A) MUST use the specific sdiff Lie bracket in the KMS identification. Abstract type III_1 modular flow does not determine the bridge. Approach B (LPS hybrid) passes the Tao filter because LPS bounds are PDE-specific. Approach D (pure zeta) passes because it uses the specific Stokes operator on T^3 (averaged NS has a different operator). Approach E (classical bypass) automatically passes.

**Active kill K-NS-3:** OA controls WHETHER bounded, not WHICH bound. The quantitative content must come from sdiff + PDE, not from type classification alone.

---

## Secondary targets

These are downstream of the primaries. Dispatch Authors only after their dependencies advance.

### Step 6* -- Meromorphic continuation of Z_omega (confidence 6/10)

**Depends on:** Steps 4, 5 (both LOCKED)
**Approach:** Classical heat-kernel expansion for Stokes operator on T^3. Seeley 1967 gives meromorphic continuation of zeta for any elliptic operator. The subtlety: Z_omega(s,t) has time-dependent coefficients (the omega_hat_k(t) evolve under NS). Show that the meromorphic structure (pole locations, residue at s=3/2) persists for each fixed t as long as the solution exists. Use: Stokes operator elliptic -> heat-kernel expansion valid -> Mellin transform gives continuation -> poles from heat-kernel coefficients a_j at s=(3-j)/2.
**Likely closes** with careful Sobolev bookkeeping. Dispatch 1 Author in Wave 1.

### Step 9* -- Modular flow = energy cascade (confidence 3/10)

**Depends on:** Step 8 (must advance first)
**Approach:** If Step 8 produces M_u with modular automorphism sigma_t, verify that sigma_t acts on Fourier-shell observables as scale translations. The KMS condition at beta = -1 should encode the k^{-5/3} spectrum as a consistency check (not a derivation -- per K-NS-9). Use Kolmogorov 4/5 law as independent input.
**Dispatch only** after Step 8 ADVANCES.

### Step 12* -- ITPFI structure (confidence 3/10)

**Depends on:** Steps 8, 11 (both must advance)
**Approach:** If M_u is type III_1 (Step 8) and the dissipation is handled (Step 11), exhibit M_u as Araki-Woods factor over dyadic wavenumber shells 2^n <= |k| < 2^{n+1}. Each shell contributes a finite-dimensional factor (M_{d_n}(C), phi_n) where d_n = number of modes in shell n and phi_n is determined by the energy in that shell. Import machinery from RH Layer 2 ITPFI (3 independent proofs available).
**Dispatch only** after Steps 8 and 11 both ADVANCE.

### Step 13a* -- Spectral density from sdiff cascade (confidence 3/10)

**Depends on:** Steps 8, 9, 11, 12 (all must advance)
**Approach:** Using the concrete state phi_E from Step 8 and the modular flow identification from Step 9, compute the spectral density of Delta_{phi_E}. The Kolmogorov spectrum E(k) ~ k^{-5/3} enters as INPUT (not output of type classification -- per K-NS-5). The sdiff Lie bracket structure determines the spectral density rho(lambda) ~ lambda^{-2/3}. Must show this computation is specific to true NS (Tao filter).
**Dispatch only** after Steps 8, 9, 11, 12 all ADVANCE.

### Step 14* -- Zeta-regularised enstrophy bound (confidence 7/10 given 13b)

**Depends on:** Steps 6, 13b
**Approach:** Given the coefficient bound from Step 13b (|omega_hat_k|^2 <= C * lambda_k^{-1+delta}) and the meromorphic structure from Step 6, evaluate Z_omega(0,t) = ||omega||_{L^2}^2. The sum converges because lambda_k ~ k^{2/3} (Weyl) and the coefficients decay as lambda_k^{-1+delta}. The enstrophy bound C(E,nu) follows from the energy inequality plus the spectral control.
**Dispatch only** after Steps 6 and 13b both ADVANCE.

---

## What success looks like

| Outcome | Steps 8/11/13b | Chain confidence | What the next run targets |
|---|---|---|---|
| BEST CASE | 8 closes (Tier B). 11 dissolves (P6). 13b closes (Tier B or P5). | 5/10 -> 8/10 | Steps 9, 12, 13a (downstream verification) |
| GOOD CASE | 8 closes. 11 decomposes into sub-problems. 13b identifies viable bypass. | 5/10 -> 6-7/10 | Step 11 sub-problems + Step 13b bypass construction |
| HONEST CASE | All three walls named precisely. Kill list grows by 5-10. Routes ranked. | stays 5/10 | Best surviving route on each wall, with sharper obstacles |

In ALL cases: the kill list grows, the escalation routes are tested and ranked, and the next run starts from a stronger position.

---

## The Tao filter (K-NS-4) -- MANDATORY

Every proposed closure of Steps 8, 9, 11, 12, 13a, 13b, 14 MUST answer:

> "Does this argument also apply to Tao's averaged Navier-Stokes?"

- If YES: the argument is KILLED (K-NS-4). Averaged NS blows up (Tao 2014/2016, JAMS 29, pp. 601-674).
- If NO: explain specifically what sdiff Lie bracket structure the argument uses that averaged NS lacks.

**This is the FIRST check on every Author output.** Before logic, before gaps, before anything else.

The specific sdiff Lie bracket `[X,Y] = curl(X x Y)` preserves the phase coherence of the velocity field. Averaged NS replaces this with a randomized bilinear form that destroys phase coherence. Any argument that works for both true NS and averaged NS is using only energy, scaling, and bilinear structure -- which are insufficient.

---

*End of brief. The capacitor (03-capacitor.md) contains the full domain knowledge: 11 kills, correspondences, patterns, escalation routes, toolkit cards. Read it end-to-end before dispatching.*
