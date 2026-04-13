# Navier-Stokes Global Regularity — Proof Chain

*Primary path: C (zeta-regularised enstrophy) + A (modular flow) + D (ITPFI)*
*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-13*
*Status: DRAFT — feasibility ~5/10, not battle-tested*

---

## Proof Chain

| Step | Type | Statement | Depends on | Status |
|---:|---|---|---|---|
| 1 | Definition | **Stokes operator.** On $T^3$ (or bounded $\Omega \subset \mathbb{R}^3$ with Dirichlet BC), $A = -P\Delta$ where $P$ is the Leray projector onto divergence-free fields. $A$ is positive, self-adjoint, compact resolvent, eigenvalues $0 < \lambda_1 \le \lambda_2 \le \cdots \to \infty$ with Weyl asymptotics $\lambda_n \sim c\, n^{2/3}$. | — | ESTABLISHED |
| 2 | Definition | **Mild formulation.** For $u_0 \in H^1_\sigma$, NS is equivalent to the integral equation $u(t) = e^{-\nu t A} u_0 - \int_0^t e^{-\nu(t-s)A} P\bigl((u \cdot \nabla)u\bigr)(s)\,ds$. Local well-posedness in $H^s$, $s \ge 1$ (Fujita-Kato 1964). | 1 | ESTABLISHED |
| 3* | Theorem | **BKM criterion (Beale-Kato-Majda 1984).** $T^* < \infty$ (blow-up) $\iff$ $\int_0^{T^*} \|\omega(t)\|_{L^\infty}\,dt = \infty$, where $\omega = \nabla \times u$. Contrapositive: bounding the vorticity integral on every finite interval implies global regularity. | 2 | ESTABLISHED |
| 4 | Definition | **Spectral zeta function of $A$.** $\zeta_A(s) = \sum_{k \ge 1} \lambda_k^{-s}$, convergent for $\operatorname{Re}(s) > 3/2$. Meromorphic continuation to all of $\mathbb{C}$ with simple pole at $s = 3/2$ (Seeley 1967, Minakshisundaram-Pleijel 1949). Regular at $s = 0$ with $\zeta_A(0) = -1$ (Epstein). | 1 | ESTABLISHED |
| 5 | Definition | **Vorticity spectral coefficients.** Expand $\omega(t) = \sum_k \hat\omega_k(t)\,\phi_k$ in Stokes eigenfunctions. Define the *spectral enstrophy zeta function* $Z_\omega(s, t) = \sum_k |\hat\omega_k(t)|^2\,\lambda_k^{-s}$, convergent for $\operatorname{Re}(s)$ large enough (depends on Sobolev regularity of $\omega$). | 1, 3 | DEFINITION |
| 6* | Lemma | **Meromorphic continuation of $Z_\omega$.** For any strong solution on $[0, T)$, $Z_\omega(s, t)$ extends meromorphically to $\operatorname{Re}(s) > 0$ for each $t < T$, with poles determined by the heat-kernel coefficients $a_j$ of $A$ and the Sobolev regularity of $\omega(t)$. The key pole is at $s = 3/2$ with residue proportional to $\|\omega(t)\|_{L^2}^2$. | 4, 5 | PENDING VERIFICATION |
| 7 | Definition | **Lie algebra $\mathfrak{sdiff}(\mathbb{R}^3)$.** Divergence-free vector fields with Lie bracket $[X, Y] = X \cdot \nabla Y - Y \cdot \nabla X$. The vorticity equation $D_t \omega = (\omega \cdot \nabla)u$ is the coadjoint action. Helicity $\mathcal{H} = \int u \cdot \omega\,d^3x$ is a Casimir. $H^2(\mathfrak{sdiff}(M^3), \mathbb{R}) \cong \mathbb{R}$ via the helicity cocycle (Lichnerowicz 1974). | — | ESTABLISHED |
| 8* | Construction | **Velocity-field algebra.** Construct a von Neumann algebra $\mathcal{M}_u$ from the NS velocity field via the GNS construction: the quasi-free state $\phi_E$ on the Weyl algebra $\mathcal{W}(\mathfrak{sdiff})$ determined by the energy shell $\|u\|_{L^2}^2 = E$. Claim: for a turbulent (high Reynolds number) flow, $\mathcal{M}_u$ is a factor of type III$_1$. | 7 | OPEN — key construction |
| 9* | Lemma | **Modular flow = energy cascade.** The modular automorphism $\sigma_t^{\phi_E}$ of $(\mathcal{M}_u, \phi_E)$ acts on Fourier-shell observables as scale translations: $\sigma_t^{\phi_E}(a_k) \sim a_{k\,e^{t/\tau}}$ where $\tau$ is the eddy-turnover time. The KMS condition at $\beta = -1$ encodes the $k^{-5/3}$ energy spectrum in the inertial range. | 8 | OPEN — requires explicit verification |
| 10 | Theorem | **Tomita-Takesaki completeness.** For any type III$_1$ factor $\mathcal{M}$ with faithful normal state $\phi$, the modular automorphism $\sigma_t^\phi$ is defined for all $t \in \mathbb{R}$ with no singularities (Tomita 1967, Takesaki 1970). The S-invariant $S(\mathcal{M}) = [0, \infty)$, the T-set $T(\mathcal{M}) = \{0\}$. | — | ESTABLISHED |
| 11* | Lemma | **Dissipation quotient.** NS is dissipative ($\nu\Delta u$ term), not unitary. Construct the quotient: define the *viscous modular operator* $\Delta_\nu = \Delta_\phi\,e^{-\nu t A}$ where $e^{-\nu t A}$ is the Stokes semigroup. Show that the quotient algebra $\mathcal{M}_u / \mathcal{J}_\nu$ (where $\mathcal{J}_\nu$ is the ideal of viscously damped modes below scale $\eta = (\nu^3/\varepsilon)^{1/4}$) remains type III$_1$. | 8, 9, 10 | OPEN — this is Path A's main obstacle |
| 12* | Lemma | **ITPFI structure of $\mathcal{M}_u$.** Show that $\mathcal{M}_u$ is ITPFI by exhibiting it as an Araki-Woods factor $\bigotimes_n (M_{k_n}(\mathbb{C}), \phi_n)$ where the tensor product is over dyadic wavenumber shells $2^n \le |k| < 2^{n+1}$, with $\phi_n$ determined by the energy in that shell. The ratio set $r_\infty(\{\lambda_n\}) = [0, \infty)$ iff the energy distribution is non-degenerate across all scales. | 8, 11 | OPEN — Path D content |
| 13a* | Key Lemma | **Spectral density from sdiff cascade.** The specific state $\phi_E$ constructed in Step 8 from the $\mathfrak{sdiff}$ Lie bracket (not from abstract type III$_1$ properties) determines the spectral measure of $\Delta_{\phi_E}$. Using the Kolmogorov energy spectrum $E(k) \sim k^{-5/3}$ from Step 9 as input, and the explicit identification $\sigma_t^{\phi_E}(a_k) \sim a_{k e^{t/\tau}}$, the spectral density of $\Delta_{\phi_E}$ on the GNS Hilbert space satisfies $\rho(\lambda) \sim \lambda^{-\alpha}$ with $\alpha = 2/3$ (determined by the $-5/3$ exponent, not by the type classification). **This step uses the sdiff phase structure, not just abstract R$_\infty$ properties (Tao filter K-4).** | 8, 9, 11, 12 | OPEN — requires explicit spectral computation for $\phi_E$ |
| 13b* | Key Lemma | **Crossed-product trace bound on vorticity coefficients.** Work on the type II$_\infty$ crossed product $\mathcal{N} = \mathcal{M}_u \rtimes_{\sigma} \mathbb{R}$ with semifinite trace $\mathrm{Tr}_\tau$ (Connes-Takesaki 1977). The spectral density from Step 13a, combined with the Fourier-to-modular bridge $\lambda_k \leftrightarrow e^{-2\pi s_k}$ (where $s_k$ is the modular spectral parameter corresponding to Stokes eigenvalue $\lambda_k$), gives: $|\hat\omega_k(t)|^2 \le C\,\lambda_k^{-1+\delta}$ for $\delta > 0$ uniform in $t$. The bound is a consequence of $\mathrm{Tr}_\tau$-finiteness of the vorticity operator $\omega^*\omega$ on $\mathcal{N}$, not of abstract type classification. **This step is qualitative (type III$_1$ controls WHETHER enstrophy stays bounded) with quantitative content from the sdiff cascade (WHICH bound), per kill K-3.** | 6, 13a | OPEN — the critical bridge; requires explicit Fourier-modular identification |
| 14* | Key Lemma | **Zeta-regularised enstrophy bound.** Using the spectral coefficient bound from Step 13b and the meromorphic structure from Step 6: the value $Z_\omega(0, t) = \sum_k |\hat\omega_k(t)|^2\,\lambda_k^0 = \|\omega(t)\|_{L^2}^2$ (the enstrophy) is controlled by the residue of $Z_\omega$ at $s = 3/2$ plus contributions from the regular part. Specifically: $\|\omega(t)\|_{L^2}^2 \le C(E, \nu)$ uniformly in $t$, i.e., enstrophy remains bounded. | 6, 13b | OPEN — Path C's main content |
| 15 | Lemma | **Enstrophy controls $L^\infty$ vorticity.** By Agmon's inequality in 3D: $\|\omega\|_{L^\infty} \le C\,\|\omega\|_{H^1}^{1/2}\|\omega\|_{H^2}^{1/2}$. Combined with the enstrophy bound and parabolic regularity of the linear Stokes part, bounded enstrophy propagates to bounded $H^s$ norms for all $s$. Standard bootstrap: $\|\omega\|_{L^\infty} \le C(E, \nu, T)$ on $[0, T]$ for every finite $T$. | 14 | ESTABLISHED (given input bound) |
| 16* | Theorem | **Global regularity.** By BKM (Step 3) and the vorticity bound (Step 15): $\int_0^T \|\omega(t)\|_{L^\infty}\,dt \le C(E, \nu, T)\,T < \infty$ for every finite $T$. Therefore no finite-time blow-up occurs. The Leray-Hopf weak solution is in fact the unique strong solution, smooth for all time. | 3, 15 | PENDING — follows from 13, 14, 15 |

---

## Dependency graph

```
1 (Stokes operator)
├── 2 (mild formulation)
│   └── 3* (BKM criterion)
├── 4 (spectral zeta of A)
│   └── 5 (vorticity spectral coefficients)
│       └── 6* (meromorphic continuation of Z_ω)
│
7 (sdiff Lie algebra)
└── 8* (velocity-field algebra ← OPEN)
    ├── 9* (modular flow = cascade ← OPEN)
    │   └── 11* (dissipation quotient ← OPEN, Path A obstacle)
    │       └── 12* (ITPFI structure ← OPEN, Path D)
    │           └── 13a* (spectral density from sdiff cascade ← OPEN)
    │               └── 13b* (crossed-product trace bound ← OPEN, critical bridge)
    │                   └── 14* (zeta-regularised enstrophy bound ← OPEN, Path C)
    │                       └── 15 (enstrophy → L∞ vorticity)
    │                           └── 16* (global regularity)
    └── 10 (Tomita-Takesaki completeness)
```

## Load-bearing steps (marked *)

| Step | What it carries | If BREAKS |
|---:|---|---|
| 3* | Entire reduction to vorticity control | Must find alternative regularity criterion (Prodi-Serrin, ESS L³) |
| 6* | Meromorphic structure of vorticity zeta | Cannot use zeta-regularisation machinery at all |
| 8* | The von Neumann algebra exists and is a factor | Entire operator-algebraic pathway collapses |
| 9* | Modular flow encodes the physics | Type III₁ identification is decoration, not content |
| 11* | Dissipation doesn't destroy the type | Path A dead; must find viscosity-compatible encoding |
| 12* | ITPFI gives Araki-Woods structure | Path D dead; lose the tensor-product-over-shells picture |
| 13a* | Spectral density from the concrete sdiff cascade, not abstract type | If the sdiff construction doesn't determine spectral density, the approach is empty |
| 13b* | Crossed-product trace → PDE coefficient bound (the critical bridge) | Most dangerous step. If Tr_tau-finiteness doesn't translate to vorticity decay, the approach is empty |
| 14* | Enstrophy stays bounded | If fails, no BKM closure |
| 16* | The conclusion | Depends on everything above |

## Tao obstruction filter

Step 13a is where the Tao 2014 obstruction must be addressed (per Critic v1, kill K-4). The averaged NS (which blows up) satisfies energy conservation and the same scaling, but has randomised phases. The claim is that:

- The construction in Step 8 uses the **Lie bracket structure** of $\mathfrak{sdiff}$ (the specific phase/sign structure of the nonlinearity), not just energy/scaling properties.
- The averaged bilinear form $\tilde{B}$ of Tao does NOT produce a type III₁ factor because the randomised phases destroy the coherent energy cascade (the ratio set becomes degenerate).
- Therefore: the type III₁ identification in Step 11 is a property of **true** NS, not a generic property of any energy-conserving dissipative PDE. This is what allows Step 13 to give content beyond energy estimates.

**This argument must be made rigorous.** It is the single most important verification target.

## Honest assessment

| Layer | Confidence | Notes |
|---|---|---|
| Steps 1-5 | 9/10 | Standard PDE + spectral theory |
| Step 6 | 6/10 | Meromorphic continuation is plausible but needs careful Sobolev bookkeeping |
| Steps 7-9 | 3/10 | The GNS construction from NS data is the hardest conceptual step. No precedent in the literature for building a type III₁ factor directly from a classical PDE solution |
| Step 10 | 10/10 | Pure operator algebra, textbook |
| Step 11 | 2/10 | Dissipation quotient is the known obstacle from the attack plan. May require a completely different encoding |
| Step 12 | 3/10 | Plausible if 8 and 11 work, but the dyadic-shell tensor product is hand-wavy |
| Step 13a | 3/10 | Spectral density from sdiff cascade. Now routes through the concrete Lie bracket construction, not abstract type classification. Requires explicit computation of spectral measure for phi_E. Critic verdict: WEAKENED (repair R1 + R4 applied) |
| Step 13b | 2/10 | Crossed-product trace bound. The Fourier-to-modular bridge lambda_k <-> e^{-2pi s_k} needs explicit construction. Critic verdict: WEAKENED (repair R2 + R3 applied). Still the most dangerous step |
| Steps 14-16 | 7/10 | Conditional on 13, the PDE argument is standard |

**Overall: the chain is logically coherent but Steps 8, 11, and 13 are where it lives or dies.** The chain's value is that it makes the obstacles precise and attackable, not that it's close to done.

---

## Key references

| Ref | Used in | What it provides |
|---|---|---|
| Beale-Kato-Majda (1984) CMP 94 | Step 3 | Blow-up criterion |
| Fujita-Kato (1964) | Step 2 | Local well-posedness |
| Leray (1934) Acta Math 63 | Background | Weak solutions exist |
| Seeley (1967) | Steps 4, 6 | Meromorphic continuation of spectral zeta |
| Tomita (1967) / Takesaki (1970) | Step 10 | Modular automorphism theory |
| Connes (1973) | Steps 10, 12 | S-invariant, type III classification |
| Connes-Woods (1985) | Step 12 | ITPFI = AT, uniqueness of hyperfinite III₁ |
| Haagerup (1987) | Step 12 | Uniqueness of injective III₁ factor |
| Connes-Takesaki (1977) | Step 9 | Flow of weights, scaling = dual action |
| Arnold (1966) Ann Inst Fourier 16 | Step 7 | Geodesic formulation on SDiff |
| Lichnerowicz (1974) | Step 7 | H²(sdiff) classification |
| Tao (2014/2016) JAMS 29 | Filter | Averaged NS blow-up → phase structure is essential |
| Ojima (2003) | Step 9 | Operator-algebraic turbulence scaling |
| Gallavotti (1996) | Step 9 | KMS conjecture for turbulence |
| Connes-Kreimer (2000) CMP 210 | Escalation | Hopf algebra for perturbative expansion |
| Caffarelli-Kohn-Nirenberg (1982) | Escalation | Partial regularity of singular set |

---

## Appendix: ORA Critic v1 Report (Step 13, 2026-04-13)

**Target:** Step 13 (pre-split, now 13a+13b)
**Verdict:** WEAKENED (not BROKEN)

**Kills triggered:**
- K-3 (quantitative from qualitative): Direct hit. Type III_1 classification alone cannot determine spectral density exponents. Connes invariants S(M), T(M) are topological invariants of the flow of weights, not spectral density parameters.
- K-4 (Tao phase structure): Hit. Step 13 as originally written used only abstract type III_1 + ITPFI, not the specific sdiff construction.

**Repairs applied:**
- R1: Exponent alpha is now an INPUT from Kolmogorov scaling (Step 9), not an output of type classification. Applied in Step 13a.
- R2: Fourier-to-modular bridge made explicit (lambda_k <-> e^{-2pi s_k}). Applied in Step 13b.
- R3: Zeta arguments now route through crossed-product trace Tr_tau on M rtimes R (type II_inf), not Delta_phi on M. Applied in Step 13b.
- R4: sdiff Lie bracket structure made an explicit input (not just inherited dependency). Applied in Step 13a.

**Surviving architectural idea:** Type III_1 modular structure constrains blow-up. The qualitative fact (type classification) controls WHETHER enstrophy stays bounded; the quantitative content (WHICH bound) comes from the sdiff cascade structure. This separation (qualitative from OA, quantitative from PDE/physics) is sound and passes K-3.
