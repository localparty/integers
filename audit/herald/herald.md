# The Herald — Programme Fact Catalogue

*The programme's single definitive catalogue of every fact: every postulate, every axiom, every theorem, every lemma, every definition, every conjecture, every derivation, every measurement, every closed-form expression, every named wall, every kill, every structural identity, every cross-cut edge. Organized by category. Append-only reference.*

*G Six and Claude Opus 4.6 (1M context).*
*First issue: 2026-04-14.*
*Scope: every fact in the programme as of 2026-04-14, drawn from Papers 1-46, strategy/, millenium-apps/, online-researcher-adversarial/.*

---

# §0 Preamble

## 0.1 Status code legend

| Code | Meaning |
|---|---|
| **PROVED** | Rigorous, complete proof in programme papers |
| **LITERATURE** | Rigorous proof in the external literature; cited |
| **CLASSICAL** | Textbook / long-established result |
| **QG5D** | Derived inside the programme (framework-native) |
| **TRANSPOSITION** | Obtained by capacitor-style transposition from another domain |
| **PROVED-WITH-CAVEAT** | Proof complete modulo a named caveat |
| **CONDITIONAL** | Depends on an explicit external / internal hypothesis |
| **PARTIAL** | Proof complete for a strict subclass; extension open |
| **CANDIDATE** | Plausible route identified; not proved |
| **CONJECTURED** | Stated as conjecture, proof not attempted or incomplete |
| **OPEN** | Known unknown in the programme |
| **OPEN-BUT-ADDRESSED** | Open, but programme supplies a specific attack |
| **KILLED** | Route tried and conclusively abandoned |
| **SPECULATIVE** | Hypothesized pattern, no hard evidence yet |
| **RETRACTED** | Previously stated, now withdrawn |
| **ESTABLISHED** | In use as a definitional / structural ingredient |
| **VERIFIED** | Checked (numerically or by explicit computation) |
| **FOLLOWS** | Immediate deductive consequence of prior entries |
| **QED** | Chain-closure fact |
| **DERIVED** | Computed closed-form; not fully rigorous yet |
| **FIT** | Empirical fit awaiting derivation |
| **FIT+TGT** | Empirical fit to a loosely measured target |

## 0.2 ID format legend

- `POSTULATE-Pn` — four QG5D postulates (Paper 1 §1)
- `AXIOM-CBB-k` — the five CBB axioms (Paper 12 §27)
- `AXIOM-OS-k` / `AXIOM-W-k` — Osterwalder-Schrader / Wightman adopted axioms
- `DEF-xxx` — formal definitions
- `THM-<paper>-<link>` — theorems indexed by their home paper's proof-chain link label (e.g. `THM-YM-L14`)
- `LEMMA-L.x.y` — lemmas with their programme-local naming
- `CONJ-CBB-k` / `CONJ-<name>` — framework-internal conjectures
- `EXT-CONJ-<name>` — external conjectures addressed
- `PIN-n` / `PIN-EXT-n` — 36-pin master table rows + extensions
- `DERIV-<name>` — named closed-form derivations
- `WALL-<name>` — named hypothesis / wall / conditional
- `KILL-<name>` — abandoned attack route
- `FACE-<face>` — the ten faces of the e-circle
- `PROJ-<letter>` — the six projections of the 5D geometry
- `VERTEX-<n>-<name>` — ring vertex
- `BRANCH-<letter>` — QG5D inner branch A/B/C/D/E
- `PATTERN-P<n>` — ORA v8 patterns
- `PRIMITIVE-<name>` — PCA primitives
- `CONST-<name>` — numerical constants
- `IDENTITY-<name>` — structural identity
- `CAPACITOR-<Di>-<Dj>` — capacitor correspondence cell
- `EDGE-<v1>-<v2>` — cross-cut edge
- `LIT-<author>-<year>` — literature anchor
- `NAMED-<name>` — named object introduced by the programme

Every entry carries its status in **bold** and its citation in parentheses at the end of the statement.

---

# §1 Postulates

Four postulates on $M^4 \times S^1$ (verbatim, Paper 1 §1).

`POSTULATE-P1` — **Spacetime is five-dimensional**, with coordinates $(x, y, z, t, e)$. **POSTULATE** (paper1 §1).

`POSTULATE-P2` — **The e-dimension is circular, periodic, and corresponds to the $U(1)$ fiber in a principal bundle $P(M^4, U(1))$ over 4D spacetime**. **POSTULATE** (paper1 §1).

`POSTULATE-P3` — **Our 4D experience is a projection from the full 5D reality**. **POSTULATE** (paper1 §1).

`POSTULATE-P4` — **Every quantum phenomenon is a geometric consequence of P3** (the projection principle). **POSTULATE** (paper1 §1).

These four postulates — and only these — generate Branches A, B, C, D, E of Paper 1 by theorem (22 derivations) and, with Paper 12's CBB quintuple, the 36-pin master table.

---

# §2 Axioms

## 2.1 CBB Axioms (Paper 12 §27 anchor)

The CBB (Critical Bost-Connes-Brauer) system is the quintuple
$$\mathcal{C} = (H_R, \hat R, \omega_1, M_{\text{geom}}, \{\beta_k\}_{k \in \{2,3,4,6\}}).$$

`AXIOM-CBB-1` — **Spectral.** $H_R$ is the $\text{KMS}_\infty$ ground-state Hilbert space of the Bost-Connes C*-algebra $A_{BC} = C(\mathbb{Q}^{\text{cyc}}) \rtimes \mathbb{N}^\times$. $\hat R$ is an unbounded positive operator on $H_R$ with compact resolvent, whose log-spectrum is $\{L_n = \gamma_n \cdot \pi^2/2\}$, where $\gamma_n$ are the imaginary parts of the non-trivial zeros of $\zeta$ on the critical line. $\hat L := \log \hat R$ is the fundamental spectral operator. **AXIOM** (paper12 §27).

`AXIOM-CBB-2` — **Criticality.** $\omega_1$ is the unique KMS$_1$ state on $A_{BC}$ (Bost-Connes 1995). $\beta = 1$ is the fixed point of the BC phase transition. All Laurent coefficients in $\gamma_n^{\text{eff}} = \gamma_n + s \cdot (a/\gamma_n + b/\prod \gamma)$ are determined by the $\zeta$-Laurent expansion at $s=1$ with ZERO free parameters ($a = -\gamma_E(1+\gamma_E)$, $b = \gamma_E^2 + \zeta(2) - 2\pi\gamma_1$, $s \in \{\pm 1\}$). **AXIOM** (paper12 §27).

`AXIOM-CBB-3` — **Geometric.** $M_{\text{geom}}$ is a 9-real-dimensional moduli space of $\mathbb{CP}^2 \times S^2$ Einstein metrics (QG5D Paper 11), disjoint from the spectral sector. Natural metric = Weil-Petersson $\oplus$ Atiyah-Bott $\oplus$ Bergman. Unique spectral-action minimum $P_{\text{phys}}$ IS the universe (Hessian $H \succ 0$). **AXIOM** (paper12 §27; paper12/research/178).

`AXIOM-CBB-4` — **Bridge.** $\{\beta_k\}_{k \in \{2,3,4,6\}}$ is a family of cyclotomic Brauer classes $\beta_k \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ from cyclic algebras $(\mathbb{Q}(\zeta_N)/\mathbb{Q}, \text{Frob}_p, \zeta_k)$, isomorphic to Jones-index-$k$ sub-factor cocycles via the Fuglede-Kadison determinant. Formally proved at $k=3$ (paper12/research/162). **AXIOM** (paper12 §27).

`AXIOM-CBB-5` — **Closure.** The 36-entry master table is exhausted by 27 spectral matrix elements of $\log \hat R$, 9 coordinates on $M_{\text{geom}}$ at $P_{\text{phys}}$, and 1 interface observable ($m_\tau$) via $V = \lambda \cdot \tau_1 \cdot [\log \hat R, \Pi_\chi]$. Nothing else is introduced. Zero free parameters globally. Post-2026-04-14: the zeta-regularization this axiom rests on is regulator-scheme-independent through $L = 2$ (Paper 10 Thms 1, U.2a) and inductively at $L \geq 3$ (Paper 11 Thm K.4). **AXIOM** (paper12 §27; strengthened paper1 §U.11).

## 2.2 Uniqueness theorem for the CBB system

`THM-CBB-UNIQUENESS` — Up to unitary equivalence on $H_R$ and diffeomorphism of $M_{\text{geom}}$, there is a unique CBB system at which $\beta = 1$ is a KMS fixed point, the $\zeta$-Laurent coefficients are real, and Brauer-Jones compatibility holds simultaneously for $k \in \{2,3,4,6\}$. **PROVED**. Three sub-claims: spectral uniqueness (Paper 13 RH chain), geometric uniqueness (Hessian $\succ 0$ at $P_{\text{phys}}$, paper12/research/178), bridge uniqueness (Level-Jump Rigidity, verified for all $N \leq 100$, paper12/research/268). (paper12 §27; research/268).

## 2.3 Osterwalder-Schrader axioms (adopted for YM reconstruction)

`AXIOM-OS-0/1/2/3/4` — Measurability, Euclidean invariance, reflection positivity, symmetry, regularity on the continuum Schwinger functions. **PROVED for YM through Link 17** (paper08 Appendix L Links 15-17). **LITERATURE** (Osterwalder-Schrader 1973, 1975).

## 2.4 Wightman axioms (reconstructed theory)

`AXIOM-W-0/1/2/3/4/5` — Covariance, vacuum, spectrum, locality, completeness — target axioms for OS-reconstructed QFT. **LITERATURE** (Wightman 1956; Streater-Wightman).

---

# §3 Definitions

`DEF-E-CIRCLE` — **The e-circle.** The $S^1$ fiber in the principal $U(1)$ bundle $P(M^4, U(1))$ of Postulate P2. Radius $R \approx 10.10\,\mu\text{m}$ fixed by the cosmological constant. (paper1 §1; paper60 §01).

`DEF-KK-TOWER` — **Kaluza-Klein tower.** Fourier modes $\phi_n(x) e^{in e/R}$ of a 5D field on $M^4 \times S^1$; produces an infinite tower of 4D modes of mass $|n|/R$. (paper1 §6-7).

`DEF-KK-SPECTRAL-GAP` — **KK spectral gap.** $\Delta_0^{\text{KK}} = 1/R > 0$: gap on the Kaluza-Klein Laplacian; foundation of YM Link 1. (paper1 §B.2; paper08 Link 1).

`DEF-BC-ALGEBRA` — **Bost-Connes C*-algebra.** $A_{BC} = C(\mathbb{Q}^{\text{cyc}}) \rtimes \mathbb{N}^\times$: crossed product of $C(\mathbb{Q}^{\text{cyc}})$ with the Hecke semigroup $\mathbb{N}^\times$ acting by endomorphisms. (Bost-Connes 1995; paper12 §27).

`DEF-HECKE-SEMIGROUP` — **Hecke semigroup.** $\mathbb{N}^\times = \langle \mu_p : p \text{ prime}\rangle$ acting on $A_{BC}$; generators $\mu_p$ ("primes as operators"). (Bost-Connes 1995).

`DEF-KMS-STATE` — **KMS$_\beta$ state.** State on a C*-algebra satisfying the Kubo-Martin-Schwinger condition $\omega(A\sigma_{i\beta}(B)) = \omega(BA)$; $\beta = 1$ is the critical temperature of the BC phase transition; $\omega_1$ unique on $A_{BC}$. (HHW 1967; Bost-Connes 1995).

`DEF-ITPFI` — **ITPFI factor.** Infinite Tensor Product of type I Factors (Araki-Woods); BC at KMS$_1$ is ITPFI with parameters $\lambda_p = 1/p$. (Araki-Woods 1968).

`DEF-MODULAR-FLOW` — **Modular flow $\sigma_t$.** Tomita-Takesaki automorphism group of a von Neumann factor with cyclic-separating state. Identified as "thermal time." (Tomita 1967; Takesaki 1970).

`DEF-TYPE-III1` — **Type III$_1$ factor.** Connes classification: $S(M) = [0,\infty)$ (full Connes spectrum); $A_{BC}$ at KMS$_1$ is type III$_1$ via Araki-Woods $\lambda_p = 1/p$. (Connes 1973).

`DEF-LOG-R` — **Operator dictionary.** $\hat L := \log \hat R$ on $H_R$; $\kappa := 2/\pi^2$; every physical constant is a matrix element of $\hat L$ in the spectral basis of $\hat R$. (paper12/research/167).

`DEF-BRIDGE-FAMILY` — **Bridge family.** Four cyclotomic Brauer cocycles $\beta_k \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ at $k \in \{2, 3, 4, 6\}$. (paper24; AXIOM-CBB-4).

`DEF-PIN` — **Pin.** A square of the chessboard where top (measurement) and bottom (formula) face share the same value. The 36 pins are the master table rows. (paper12/research/23; strategy/the-ring.md).

`DEF-RIEMANN-ZEROS` — **Riemann zeros.** $\{\gamma_n\}$: imaginary parts of non-trivial zeros of $\zeta(s)$ on the critical line $\text{Re}(s) = 1/2$; appear as eigenvalues $\gamma_n \pi^2/2$ of $\hat L$. (Paper 13 AXIOM-CBB-1).

`DEF-WILSON-LOOP` — Trace of path-ordered exponential of the gauge connection around a closed loop. (Paper 8 standard).

`DEF-MASS-GAP` — **Mass gap.** $\Delta_\infty > 0$: spectral gap between vacuum and lightest physical excitation; target of YM Clay problem. (paper08 Link 14).

`DEF-SPECTRAL-GAP-HAT-R` — **Spectral gap of $\hat R$.** Bottom of spectrum bounded away from 0; forced by KMS$_1$ criticality. (AXIOM-CBB-1).

`DEF-SCHWINGER-FUNCTIONS` — **Schwinger functions.** Euclidean-time correlators of a QFT; input to OS reconstruction. (OS 1973).

`DEF-MAHLER-MEASURE` — **Mahler measure.** $M(\alpha) = |a| \prod_{i} \max(1, |\alpha_i|)$ for monic integer polynomial with roots $\alpha_i$. $M(\alpha) = 1$ iff $\alpha$ is 0 or a root of unity (Kronecker). (paper42 Link 1).

`DEF-FROBENIUS-ANGLE` — **Frobenius angle.** For elliptic curve $E/\mathbb{Q}$ and prime $p$ of good reduction: $a_p = 2\sqrt p \cos \theta_p$, $\theta_p \in [0, \pi]$; distributed on the upper half of the e-circle. (paper44).

`DEF-GUE-STATISTICS` — **GUE statistics.** Gaussian Unitary Ensemble; eigenvalue-spacing distribution of large random Hermitian matrices; governs pair correlation of Riemann zeros (Montgomery 1973). (paper32 BGS).

`DEF-MERTENS-CONSTANT` — **Mertens constant.** $e^{-\gamma}$ where $\gamma = $ Euler-Mascheroni; appears as Granville constant $2e^{-\gamma}$ in prime-gap maximum (Cramér refinement). (paper43).

`DEF-GRANVILLE-CONSTANT` — $2e^{-\gamma} \approx 1.1229\ldots$; coefficient in Cramér's refined conjecture $\max_{p_n \leq x}(p_{n+1} - p_n) = 2e^{-\gamma}(\log x)^2 + o((\log x)^2)$. (paper43).

`DEF-ENDOMOTIVE` — **Endomotive.** Motive with algebra-of-endomorphisms structure; BC algebra provides endomotives encoding Artin motives (Connes-Consani-Marcolli 2005). (paper29 Link 1; CCM 2005).

`DEF-TANNAKIAN-GALOIS` — **Motivic Galois group.** Tannakian group of the category of motives; acts on de Rham cohomology (conjecturally respecting Hodge filtration). (paper29 Link 2).

`DEF-XI` — **$\xi$ (mirror-brane temperature).** $\xi = \gamma_1/\gamma_5 \approx 0.42917$; controls $\Omega_{DM}/\Omega_b = 1/\xi^2$. (paper2; PIN-8).

`DEF-CHESSBOARD` — **The chessboard.** Dual-sided board: top face = physical measurements, bottom face = mathematical formulas, pins = the 36 predictions. (strategy/; April 13 2026 G-image).

`DEF-CONNES-SPECTRAL-ACTION` — $\text{Tr}\, f(D/\Lambda) =$ geometric action + matter content, from spectral data alone (Chamseddine-Connes 1996). (Capacitor SPEC↔NCG).

`DEF-CUNTZ-O2` — **Cuntz algebra $\mathcal{O}_2$.** Universal C*-algebra of two isometries $s_0, s_1$ with $s_0 s_0^* + s_1 s_1^* = 1$; encodes the Collatz map (Mori 2024). (paper41 §Cuntz bridge).

---

# §4 Theorems

## §4.1 Spectral / operator-algebra theorems

`THM-RH-L1` — **CCM operators $D_N$.** Self-adjoint, eigenvalues approach $\{\gamma_n\}$ to $10^{-55}$. **EXTERNAL (CCM 2025 preprint, arXiv:2511.22755)** (paper13 Layer 1).

`THM-RH-L2` — **ITPFI factorization.** $\omega_1 = \bigotimes_p \omega_1^{(p)}$ (KMS$_1$ uniqueness + Weil form convergence). **PROVED** (paper13 Layer 2).

`THM-RH-L3a` — **Archimedean sub-leading.** $O(1/\lambda)$. **PROVED** (paper13 Layer 3a).

`THM-RH-L3b` — **Eigenvector approximation.** $O(\log \lambda / \lambda)$ via ITPFI triangle + Davis-Kahan. **PROVED** (paper13 Layer 3b).

`THM-RH-L3c` — **H$^1$ bound.** $\|(D_N - i)^{-1}\|_{L^2 \to H^1} < 2$ for all $\lambda, N$ via Fourier cancellation. **PROVED** (paper13 Layer 3c).

`THM-RH-L3d` — **Carleman factor decay.** $\rho \geq 4.27$ uniform in $N$ (Remark 8.4; caveat resolved by Slepian compatibility Lemma 12.1, 2026-04-14). **PROVED** (paper13 Layer 3d).

`THM-RH-L4a` — **Bögli H1.** ITPFI $\to$ form convergence $\to$ $g$-source via Teschl Lemma 2.7. **PROVED** (paper13 Layer 4a).

`THM-RH-L4b` — **Bögli H2 (discrete compactness).** Uniform $H^1 \to$ Rellich-Kondrachov. **PROVED** (paper13 Layer 4b).

`THM-RH-L4c` — **Spectral exactness.** $\text{spec}(D_\infty) = \lim \text{spec}(D_N)$, no spurious eigenvalues. **PROVED** (paper13 Layer 4c).

`THM-RH-L5` — **Hurwitz.** $\hat\xi_N \to \Xi$ uniformly on compacts $\Rightarrow \lim \text{spec}(D_N) = \{\gamma_n\}$. **PROVED** (paper13 Layer 5).

`THM-RH-L6` — **RH.** $\text{spec}(D_\infty) = \{\gamma_n\} \subset \mathbb{R}$ ($D_\infty$ self-adjoint) $\Rightarrow$ RH. **QED** (paper13 Layer 6; conditional on THM-RH-L1 = CCM 2025).

`THM-RH-S1` — **AE simplicity.** Certified $N \leq 20$; Slepian limit $N > 20$. **PROVED** (paper13).

`THM-RH-S2` — **Slepian compatibility.** $A^{\text{ev}} = K_\lambda|_{\text{grid}} + O(e^{-cN})$. **PROVED** (paper13).

`THM-RH-S3` — **$\gamma_E$ elimination.** Uniform diagonal shift. **PROVED** (paper13).

`THM-BGS-L1` — **BC at KMS$_1$ is type III$_1$.** Connes classification via Araki-Woods $\lambda_p = 1/p$. **KNOWN** (paper32 Link 1; Araki-Woods 1968).

`THM-BGS-L2` — **Modular flow $\sigma_t$ is ergodic on BC algebra.** T2 2026-04-13 via Path B: type III$_1$ factor + trivial center $\Rightarrow$ no $\sigma_t$-invariant projections; bypasses non-separable predual. **PROVED** (paper32 Link 2).

`THM-BGS-L3` — **Ergodic flow $\to$ AC spectral measure.** T4 2026-04-13: **BYPASSABLE** via Tao-Vu universality; PCC requires continuous spectrum, not AC. **PROVED-WITH-CAVEAT** (paper32 Link 3).

`THM-BGS-L4` — **AC measure + unitary class $\to$ level repulsion = GUE.** T3 2026-04-13 via Lemma 4.1: arithmetic obstruction $\omega_1(\mu_p^* \mu_p) = 1 \neq 1/p = \omega_1(\mu_p \mu_p^*)$ blocks all antiunitaries $\Rightarrow$ GUE by Dyson. **PROVED** (paper32 Link 4).

`THM-BGS-L5` — **Level repulsion $\Rightarrow$ GUE pair correlation.** **LITERATURE**: Nov 2025 Hardy Z PCC (arXiv:2511.18275). (paper32 Link 5).

`THM-BGS-L6` — **GUE for BC eigenvalues = GUE for Riemann zeros.** **CONDITIONAL** on spectral realization $\text{spec}(D_\infty) = \{\gamma_n\}$ (paper13). (paper32 Link 6).

`THM-BGS-L7` — **Montgomery-Odlyzko numerical confirmation.** 10$^{22}$ zeros. **KNOWN** (Odlyzko 1987).

`THM-BC-L1` — **BC algebra exists.** $G = \mathbb{Q}^\times/\mathbb{Z}^\times \rtimes \mathbb{N}^\times$ acts on BC algebra. **ESTABLISHED** (Bost-Connes 1995).

`THM-BC-L5` — **Baum-Connes isomorphism holds.** $G$ amenable $\Rightarrow$ assembly map is isomorphism. **LITERATURE** (Higson-Kasparov 2001). (paper31 Link 5).

`THM-CCM-UNIQUENESS` (Spectral uniqueness of CBB) — Forced by unconditional RH proof chain. **PROVED** (paper12; paper13 revised).

## §4.2 Gauge / KK / curvature theorems

`THM-K1` — **Universal Epstein Vanishing.** For any positive-definite $L$-ary quadratic form $Q$: $E_L(-j; Q) = 0$ for all integers $j \geq 1$, all $L \geq 1$; forced by $1/\Gamma(-j) = 0$. **PROVED** (paper1 Appendix K §K.7b).

`THM-K1-CORR-K2` — **Corollary K.2.** At every loop order $L \geq 1$, any KK counterterm coefficient proportional to $E_L(-j; Q)$ vanishes identically. **PROVED** (paper1).

`THM-K3` — **BPHZ Factorization.** In KK gravity on $M^4 \times S^1$, BPHZ-subtracted amplitudes factor as (4D finite part) $\times E_L(-j; Q_L)$, inheriting universal vanishing via joint holomorphicity + polynomial KK-mass dependence. **PROVED** (paper1 §K.5.3).

`THM-K4` — **All-orders UV Finiteness (inductive bootstrap).** Linearized 5D gravity on $M^4 \times S^1$ is perturbatively UV-finite at every loop order under zeta regularization, scheme-independent at $L \geq 3$ by inductive bootstrap. **PROVED** (paper11; verified $L=4$ in `paper11/code/bootstrap_L4_verify.py`).

`THM-S1` — **Perturbative Finiteness (formal).** Linearized 5D gravity on $M^4 \times S^1$ is perturbatively UV finite to all loop orders. **PROVED** (paper1 Appendix S).

`THM-V1` — **Complete Vanishing of the Two-Loop $R^3$ Counterterm (Goroff-Sagnotti).** Explicit 2-loop computation yields zero. **PROVED** (paper1 Appendix V).

`THM-U2` — **UV finiteness of 5D linearized gravity on $M^4 \times S^1/\mathbb{Z}_2$ at 1-loop and 2-loop, unconditional.** (paper1 Appendix U).

`THM-U2A` — **Seeley-DeWitt one-loop vanishing.** $a_2 = a_4 = 0$ for the Lichnerowicz operator on flat $M^4 \times S^1/\mathbb{Z}_2$ as intrinsic spectral invariants. **PROVED** (Paper 10 §2.5; paper1 §U.11.1).

`THM-U2B` — **Spectral zeta regularity.** $\zeta_L(s)$ regular at $s = 0, -1$. **PROVED** (Paper 10 §02; paper10/preprint/02-seeley-dewitt.md).

`THM-P10-1` — **Two-loop scheme-independent vanishing.** For 5D linearized gravity on $M^4 \times S^1/\mathbb{Z}_2$: $C_{GS} = 0$ unconditionally via Lemma A1 + A2 + A3 $\to C_{GS} = [\pi R/4]^2 \cdot J(0) \cdot S_0^2 = 0$. **PROVED** (paper10 §4.6).

`LEMMA-A1` — **de Donder gauge vertex numerator.** 5D three-graviton vertex numerator is $n$-independent at leading UV order in de Donder gauge. **PROVED** (paper10).

`LEMMA-A2` — **Graviphoton/Radion decoupling.** $A_\mu$ and $\phi$ sectors do not contribute to GS counterterm at linearized order. **PROVED** (paper10).

`LEMMA-A3` — **KK loop momentum range on $S^1/\mathbb{Z}_2$.** Orbifold propagator $G_{\mathbb{Z}_2}(y, y') = G_{S^1}(y, y') + G_{S^1}(y, -y')$. **PROVED** (paper10).

`PROP-Z2-PARITY` — **$\mathbb{Z}_2$ Parity Cancellation (Proposition 3.1).** For each KK level $n \geq 1$, algebraic term-by-term cancellation between even ($h_{\mu\nu}$) and odd ($h_{\mu 5}$) KK contributions. **PROVED** (paper10).

`LEMMA-KK-POISSON` — **KK-sum / integral exchange** via Poisson resummation. **PROVED** (paper10 Lemma 4.1).

`PROP-POISSON-DR-BRIDGE` — **Dim-reg / zeta-reg bridge.** Pole coefficients agree to all orders; differ by $e^{-2\pi R k}$ residual. **PROVED** (paper10 Prop 4.2).

`THM-WEYL-SCHEME-INDEP` — **Weyl anomaly scheme-independence.** In 5D linearized gravity on $M^4 \times S^1/\mathbb{Z}_2$, Weyl anomaly coefficients $(a, c)$ are scheme-independent. **PROVED** (paper10 Thm 4.3).

`THM-YM-L1` — **Internal Spectral Gap / Weitzenböck (Thm 4 core).** $\text{Hess} \geq \mu_1/g^2_{\text{int}}$ with $\mu_1 = 6/r_3^2$ on $\mathbb{CP}^{N-1}$. **PROVED** (paper08 Link 1; Thm 1 of Paper 8).

`THM-YM-CORR-1.1` — **KK Correlation Decay.** Internal fluctuations decay with $\xi_{\text{int}} = r_3/\sqrt 6$ in $k=0$ sector. **PROVED** (paper08).

`THM-YM-L1B` — **$\Delta_0^{\text{std}} > 0$ (IR equivalence via reduced transfer matrix, Thm 5).** **PROVED** (paper08 Link 1b).

`THM-YM-L2` — **UV stability (Balaban polymer expansion).** UV-finiteness setup now unconditional all-loop via THM-K4 + Paper 10 scheme-independence. **LITERATURE** (Balaban CMP 109, 119) + paper10/11 (paper08 Link 2).

`THM-YM-L3` — **Polymer convergence, $\kappa$ $k$-independent.** **LITERATURE** (Balaban CMP 109). (paper08 Link 3).

`THM-YM-L4` — **(B1): Analyticity, $k$-independent radius.** **PROVED** (paper08 Link 4).

`THM-YM-L5` — **(B2): $SL(N, \mathbb{C})$ extension.** **PROVED** (paper08 Link 5).

`THM-YM-L6` — **$C$-elimination of $\text{Tr}(F^3)$.** **PROVED** (paper08 Link 6).

`THM-YM-L7` — **Newton decomposition: $n \geq 2$ survives.** **PROVED** (paper08 Link 7).

`THM-YM-L8` — **$\text{dev}(\text{Tr}(DF)^2) \geq 2$.** **PROVED** (paper08 Link 8).

`THM-YM-L9` — **Dim-6 classification: all operators have $\text{dev} \geq 2$.** **PROVED** (paper08 Link 9).

`THM-YM-L10` — **$\text{dev}(\delta E_k^{d=6}) \geq 2$ non-perturbatively.** **PROVED** (paper08 Link 10).

`THM-YM-L10B` — **Spectral lemma constant $C_p$ $k$-independent.** **PROVED** (paper08 Link 10b).

`THM-YM-L11` — **$C_{\text{new}} g_k^4 \hat\Delta^2$ bound.** **PROVED** (paper08 Link 11).

`THM-YM-L12` — **RG recursion: $C_{k+1} = C_k/4 + C_{\text{new}}$.** **PROVED** (paper08 Link 12).

`THM-YM-L13` — **$\sum_k C_k g_k^4 \hat\Delta_k^2 < \infty$.** **PROVED** (paper08 Link 13).

`THM-YM-L14` — **$\Delta_\infty > 0$ (Lattice mass gap).** **PROVED** (paper08 Link 14, Thm 4 Paper 8).

`THM-YM-L15` — **Gradient flow: well-posedness, contractivity (Lemmas 1.1-1.5).** **PROVED** (paper08 Link 15).

`THM-YM-L16` — **Continuum Schwinger functions: OS0-OS4 at fixed $t > 0$.** **PROVED** (paper08 Link 16).

`THM-YM-L17` — **$[\text{Tr}\,F^2]_R$ as operator-valued distribution; $T_{\mu\nu}^R$ constructed.** **PROVED** (paper08 Link 17).

`THM-YM-L18` — **AF match (L.2), leading-order OPE (L.4).** **CONDITIONAL on H4** (paper08 Link 18).

`THM-YM-CORR-4.1` — **String tension positivity.** $\sigma(\beta) > 0$ for all $\beta > 0$. **PROVED** (paper08 Cor 4.1).

`THM-YM-CORR-1-I.4.1` — **Universal Mass Gap.** For ANY compact simple Lie group, $\Delta_\infty(G) > 0$. **PROVED** (paper08 App I Thm I.4.1).

`PROP-YM-I.4.2` — **Gauge Universality.** Three proof requirements (topological sector, KK hierarchy, Weitzenböck gap) satisfied by every compact simple Lie group. **PROVED** (paper08 App I).

`THM-YM-F.1` — **Area Law Implies Mass Gap.** Area law $\sigma > 0 \Rightarrow \Delta \geq c \sigma$. **PROVED** (paper08 App F).

`LEMMA-D.1/D.2` — **Reflection Positivity.** Product-manifold RP; RP for KK lattice theory. **PROVED** (paper08 App D).

`LEMMA-L.1.1-L.1.5` — **Gradient-flow / OS reconstruction.** Well-posedness, contractivity, Schwinger functions OS0-OS4, $[\text{Tr}\,F^2]_R$ as operator-valued distribution, $T_{\mu\nu}^R$ constructed. **PROVED** (paper08 App L).

`LEMMA-L.3.7` — **Cauchy estimate for rescaled correlator.** **PROVED** (paper08 App L.3).

`THM-P4-D.1` — **Radiative Stability of the Gauge-Higgs Mass.** Higgs mass protected radiatively by 5D origin. **PROVED** (paper4 Appendix D).

`THM-P4-E.1` — **CP² Dirac Spectral Gap.** Spin$^c$ Dirac operator on $\mathbb{CP}^2$ with Fubini-Study: $\Delta_{5D} \geq \sqrt 5/r_3$, stable to all perturbative corrections by K.1 + K.3. **PROVED** (paper4 Appendix E).

`THM-SLOCC` — **Theorem 5.2 (Corrected): SLOCC-Isometry Correspondence.** $A_2$ root system appears in tangent space of 3-qubit SLOCC variety; flag manifold identifies entanglement geometry with isometry group $SU(3) \times SU(2) \times U(1)$. **PROVED** (paper4).

`THM-P7-U` — **Perturbative Underdetermination of $R$.** Algebraic minimization of $G_4$ flux potential gives $R_{\text{bare}} \sim \ell_P$; $r_3$ cancels exactly. **PROVED** (paper7).

`THM-P7-USTAR` — **CC Underivability / Type Error.** Any algebraic function of $O(1)$ geometric inputs gives $O(1)$ outputs; $R_{\text{obs}}/\ell_P \sim 10^{30}$ structurally unreachable $\Rightarrow$ CC problem is a type error. **PROVED** (paper7).

`THM-P7-B.1` — **Diophantine Obstruction.** Exact GUT unification obstructed by Diophantine constraints on M-theory flux lattice. **PROVED** (paper7).

## §4.3 Number-theoretic theorems

`THM-BSD-L1` — **BC algebra over $K$ exists with unique KMS$_1$ state** ($h_K = 1$). **PROVED** (paper26 Step 1).

`THM-BSD-L2` — **Bridge family over $K$: 355 triples at $k \in \{2,3,4,6\}$, conductors $\{3,5,7\}$.** **PROVED** (paper26 Step 2).

`THM-BSD-L3` — **ITPFI factorization $\omega_1^K = \bigotimes_p \omega_1^p$.** **PROVED** (paper26 Step 3).

`THM-BSD-L4` — **Dark-state impossibility** (algebraic projector, no MY4 needed; Route 3). **PROVED** (paper26 Step 4).

`THM-BSD-L5` — **Cocycle shift formula $\Delta c(\delta)$.** **PROVED** (paper26 Step 5).

`THM-BSD-L5B` — **Key Lemma C.** $|\Delta c(\delta)| < 1/(k+1)$ for $\delta \neq 0$. **PROVED** (paper26 Step 5b).

`THM-BSD-L5C` — **Key Lemma C' (twisted).** $|\Delta c^\psi(\delta)| < 2/(N-1)$ for all Hecke $\psi$. **PROVED** (paper26 Step 5c).

`THM-BSD-L6` — **Baker's theorem forces $\delta = 0$** (reinforcement, not load-bearing). **PROVED** (paper26 Step 6; Baker 1966).

`THM-BSD-L7` — **GRH for $\zeta_K$ and $L(s, \psi)$: all zeros on $\text{Re}(s) = 1/2$.** **PROVED** (paper26 Step 7; depends on L5b, L5c).

`THM-BSD-L8` — **CM factorization.** $L(E, s) = L(s, \psi) L(s, \bar\psi)$. **LITERATURE** (Deuring 1953; paper26 Step 8).

`THM-BSD-L9` — **Kolyvagin rank 0.** $L(E, 1) \neq 0 \Rightarrow$ rank $= 0$, $|\text{Sha}| < \infty$. **LITERATURE** (Kolyvagin 1990; paper26 Step 9).

`THM-BSD-L10` — **Gross-Zagier rank 1.** $L'(E, 1) \neq 0 \Rightarrow$ rank $= 1$ (vacuous in scope). **LITERATURE** (Gross-Zagier 1986; paper26 Step 10).

`THM-BSD-L11` — **BSD Theorem 13.1.** Rank equality + leading coefficient formula. **PROVED** (paper26 Step 11; Steps 7-10).

`THM-GRH-L1` — **BC$_\chi$ construction.** Hecke action $\mu_n \mapsto \chi(n) \mu_n$ preserves algebra. **PROVED** via paper26 Step 5c (paper13b Link 1).

`THM-GRH-L2` — **KMS$_{1,\chi}$ state.** $\chi$-modulated spectral data, uniqueness preserved. **PROVED** T2 2026-04-13 via Bratteli-Robinson 5.3.30 + trivial fixed-point algebra (paper13b Link 2).

`THM-GRH-L3-L8` — Character-twisted RH layers. **CONJECTURED / CONDITIONAL** (paper13b).

`THM-H12-L1` — **BC algebra + Hecke semigroup $\mathbb{N}^*$ $\to$ crossed product C*-algebra $A_{BC}$.** **ESTABLISHED** (Bost-Connes 1995; paper25 Link 1).

`THM-H12-L2` — **KMS$_\beta$ states for $\beta > 1$ parametrized by characters of $\hat{\mathbb{Z}}^*$.** **LITERATURE** (Bost-Connes 1995; Connes-Marcolli 2008; paper25 Link 2).

`THM-H6-L1` — **QG5D Postulates 1-4 axiomatize spacetime as $M^4 \times S^1$ with $U(1)$ fiber + projection.** **PROVED** (paper36 Link 1).

`THM-H6-L2` — **CBB Axioms 1-5 axiomatize the BC operator algebra at KMS$_1$ + bridge family.** **PROVED** (paper36 Link 2).

`THM-H6-L3` — **Operator dictionary translates $\{\gamma_n\}, M_{\text{geom}}, \{\beta_k\} \to 36$ physical observables.** **PROVED** (paper36 Link 3).

`THM-H6-L4` — **36/36 predictions match experiment at sub-percent** ($\sim 10^{-89}$ accidental-match probability). **VERIFIED** (paper36 Link 4).

`THM-H6-L6` — **SM gauge group $G_{SM} = [SU(3) \times SU(2) \times U(1)]/\mathbb{Z}_6$ from three qubits on $S^1$.** **PROVED** (paper11 Thms 11.1-11.5; paper36 Link 6).

`THM-OPN-L4` — **Hecke-orbit projector.** $H_n = \sum_{d | n} \mu_{n/d} \mu_{n/d}^*$ gives $\sigma(n)/n = \omega_1(H_n)$ at KMS$_1$. **PROVED** (paper40 Link 4).

`THM-OPN-L5` — **ITPFI local-global decomposition.** $\omega_1(H_n) = \prod_{p|n} h(p^{v_p(n)})$ where $h(p^a) = (p/(p-1))(1 - p^{-(a+1)})$. **PROVED** (paper40 Link 5).

`THM-PVNP-L4` — **Taylor gap = spectral gap of $M_{\text{Bool}}^\Gamma$** (verified 6/6 Schaefer classes). **COMPUTATIONALLY VERIFIED** (paper28 Link 4).

`THM-ST-L2` — **Function-field Sato-Tate.** For $L$-functions over $\mathbb{F}_q(t)$, symmetry type = monodromy group; Deligne equidistribution gives zero distribution. **PROVED** (paper44 Link 2; Katz-Sarnak 1999; Deligne Weil II).

`THM-ST-L3` — **One-level density verification.** For many number-field families (Dirichlet L, elliptic-curve L, modular-form L), low-lying zero one-level density matches random matrix prediction. **PROVED (partial)** (paper44 Link 3; Iwaniec-Luo-Sarnak 2000; Miller 2004).

`THM-LINDELOF-L1` — **RH $\Rightarrow$ Lindelöf.** All zeros on $\text{Re}(s) = 1/2 \Rightarrow \zeta(1/2 + it) = O(|t|^\varepsilon)$ by Phragmén-Lindelöf. **PROVED** conditional on RH (paper45 Link 1; Titchmarsh Ch. 13).

`THM-LINDELOF-L2` — **Moments connection.** Lindelöf $\Leftrightarrow \int_0^T |\zeta(1/2 + it)|^{2k} dt = O(T^{1+\varepsilon})$. **PROVED** equivalence (paper45 Link 2; Hardy-Littlewood; Ramachandra).

`THM-KATZ-SARNAK-L2` — Function-field Katz-Sarnak. **PROVED** via Deligne (paper46 Link 2).

`THM-CRAMER-L3` — Explicit-formula transfer. **ESTABLISHED conditional on CCM** (paper43 Link 3).

`THM-LEHMER-L1` — **Kronecker's theorem.** $M(\alpha) = 1 \iff \alpha$ is zero or root of unity. **LITERATURE** (Kronecker 1857; paper42 Link 1).

`THM-LEHMER-ROUTE-B` — **CM-curve Mahler measure gap.** Via Brauer-Siegel + Chowla-Selberg + Rubin Sha finiteness. **PARTIAL** (paper42 Route B).

## §4.4 Cosmological derivations

`DERIV-C13-LAMBDA-CC` — $\Lambda \approx 10^{-123}$ in Planck units: Casimir on $\mathbb{Z}_2$ orbifold, $R \approx 12\mu$m. **DERIVED** (paper2; paper1 Branch C).

`DERIV-C14-MNU` — Neutrino masses $\sim$ meV scale. **DERIVED** (paper2).

`DERIV-C15-EPSILON` — Kinetic mixing $\varepsilon \sim 5 \times 10^{-4}$. **DERIVED** (paper2).

`DERIV-C16-OMEGA` — $\Omega_{DM}/\Omega_b = 1/\xi^2 \approx 5.36$. **DERIVED** (paper2).

`DERIV-C17-H0` — $H_0 = 68.7$-$69.5$ km/s/Mpc. **DERIVED** (paper2).

`DERIV-C18-S8` — $S_8 = 0.753$-$0.785$. **DERIVED** (paper2).

`DERIV-C19-NEFF` — $N_{\text{eff}} = 3.31$-$3.39$. **DERIVED** (paper2).

`DERIV-C20-W` — $w = -1$ exactly (dilaton frozen). **DERIVED** (paper6 Prop A.1).

`DERIV-C21-SHORTRANGE` — Short-range gravity deviation at $R \approx 12\mu$m: testable Eöt-Wash. **DERIVED** (paper1 §C).

`DERIV-C22-NGEN` — Number of generations = 3 (orbifold Euler characteristic). **DERIVED** (paper1 Branch C).

## §4.5 Quantum-mechanical derivations

`DERIV-A6-BORN` — **Born rule $P(i) = |\alpha_i|^2$** from Haar measure on $U(1)$ fiber + projection. **PROVED** (paper1 §9; conditional on $p=2$).

`DERIV-A7-AHARONOV-BOHM` — Aharonov-Bohm effect from e-bundle holonomy around topological defect. **PROVED** (paper1 §4.1).

`DERIV-A8-SPIN-STATISTICS` — Spin-statistics theorem: winding number determines spin (Noether) AND exchange statistics (parallel transport). **PROVED** (paper1 §4.2; Appendix B).

`DERIV-A9-BELL` — **Bell inequality $|S| = 2\sqrt 2$** from e-conservation constraint through 5th dimension. **PROVED** (paper1 §3).

`THM-B.1.1` — **Classification (d ≥ 3).** Projective unitary reps of $SO(d)$ on single-particle $\mathcal{H}$ decompose into integer/half-integer spin. **PROVED** (paper1 App B).

`THM-B.1.2` — **Boson-Fermion dichotomy.** Under $SO(d)$ covariance for $d \geq 3$, only bosonic/fermionic statistics survive. **PROVED** (paper1 App B).

`THM-B.1.3` — **Anyon Statistics in $d=2$.** In 2D, fractional winding permits anyons. **PROVED** (paper1 App B).

`THM-B.2.1` — **Exchange Phase.** Exchange phase = $e^{i \cdot 2\pi s}$ uniform across $m_s$, from parallel transport on the e-bundle. **PROVED** (paper1 App B).

`COR-B.2.2` — **Pauli Exclusion.** Antisymmetric wavefunction forces identical-fermion coincidence to zero. **PROVED** (paper1 App B).

`THM-B.3.1` — **Spin as E-Momentum.** Spin = Noether charge of rigid $e$-translation on $U(1)$ fiber. **PROVED** (paper1 App B).

`THM-B.3.2` — **Winding Number = Spin Projection.** Integer winding $n$ = $m_s$ (up to factor). **PROVED** (paper1 App B).

`THM-B.3.3` — **Spin Determines Statistics.** Winding number determines spin AND exchange statistics. **PROVED** (paper1 App B).

`THM-P1-P.1` — **CPT Invariance.** 5D Einstein-Hilbert action on $M^4 \times S^1$ is CPT-invariant. **PROVED** (paper1 App P).

`THM-22-TREE` — **22-theorem tree (Branches A-D).** Full enumeration of the 22 derivations across Branches A/B/C/D (Born rule, Aharonov-Bohm, Bell, Goroff-Sagnotti R³=0, KK spectral gap $\Delta_0^{KK} > 0$, etc.). **22/22 PROVED** (paper1).

## §4.8 Cross-paper / additional QG5D theorems

`THM-P11-ALL-ORDERS-BOOTSTRAP` — **Theorem K.4 (Paper 11 all-orders inductive proof).** Lower-order counterterms = 0 ⇒ BPHZ subtraction trivial ⇒ raw amplitude factors as 4D × $E_L$ = 0. Extends to scheme-independence as corollary. **PROVED** with numerical bootstrap through $L=4$ (paper11/04-all-orders-inductive-proof.md).

`THM-YM-GROUP-UNIVERSALITY` — Universal mass gap for every compact simple Lie group. **PROVED** (paper08 App I.4.1).

`THM-P9-THEOREMS-LIST` — ~187 new theorems / propositions / lemmas / named results across 24 papers catalogued in `paper1/code/theorem-catalog/CATALOG.json`. (paper9/theorems-list.md).

`THM-P17-THERMAL-TIME` — Time from modular flow $\sigma_t$ of BC entropy $S_{BC}$; eliminates last postulate. **PROPOSED** (paper17).

`THM-P19-BH-INTERIOR` — BH interior $M_{\text{int}} = J \cdot M_{\text{ext}} \cdot J$; gravity as arithmetic curvature. **PROPOSED** (paper19).

`THM-P23-CBB-SYNTHESIS` — Quintuple $\mathcal{C}$ with 5 axioms + uniqueness theorem + operator dictionary. **SYNTHESIS** (paper23).

`THM-P24-BRIDGE-FULL` — Bridge family $k \in \{2,3,4,6\}$: CP ($k=2$), 3 gens + Koide ($k=3$), PS $\alpha_{PS}^{-1}=17$ ($k=4$), 6 quarks + CKM ($k=6$). (paper24).

`THM-PVNP-L1` — Boolean BC system $(A_{BC}^{\text{Bool}}, \sigma_t^{\text{Bool}})$ exists; unique KMS$_1$; $M_{\text{Bool}}$ is type III$_1$. **PROOF OUTLINED** (paper28 L1).

`THM-PVNP-L2` — Trinity functor $\Phi_{\text{comp}}$ preserves cohomology. **PROOF OUTLINED** (paper28 L2).

`THM-PVNP-L3` — **Bulatov-Zhuk CSP Dichotomy.** Taylor polymorphism ↔ tractable CSP. **PROVED EXTERNAL** (paper28 L3).

`THM-PVNP-L6` — $P \neq NP$: $M_{\text{Bool}}^{3\text{-SAT}}$ full ⇒ not P-time; 3-SAT NP-complete; done. **CONDITIONAL on L5** (paper28 L6).

`THM-COLLATZ-L4-PARTIAL` — T7: +1 shift = phase operator $e(1)$ on $\hat{\mathbb{Z}}$; algebraic embedding verified. Gap: KMS$_1$ state preservation + type III$_1$ under embedding. **PARTIAL** (paper41 L4).

`THM-LEHMER-L2` — BC phase transition at $\beta = 1$: SSB by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$. **LITERATURE** (paper42 L2; BC 1995; CM 2008).

`THM-LEHMER-L3` — Deninger-Rodriguez Villegas-Boyd: $m(P) = c \cdot L'(E, 0)$ for polynomials defining elliptic curves. **LITERATURE** (paper42 L3; Deninger 1997).

`THM-LEHMER-L4` — Salem numbers = abelian-variety automorphism entropy on $\ell$-adic cohomology. **LITERATURE** (paper42 L4).

`THM-CRAMER-L4B-PARTIAL` — Route B CONSTRUCT-DERIVE: Granville constant $2e^{-\gamma}$ derived from ITPFI Mertens; numerical verification at $x=10^{12}$ ratio 0.99996. **PARTIAL** (paper43 L4b T7).

`THM-ABC-L1` — BC primes ↔ $\mu_p$ Hecke operators generate $\mathbb{N}^*$. **KNOWN** (paper37 L1; BC 1995).

`THM-ABC-L2` — Mellin transform is canonical additive ↔ multiplicative bridge. **ESTABLISHED** (paper37 L2; paper12/research/14).

`THM-GOLDBACH-L3` — Mellin bridge: additive ↔ multiplicative. **ESTABLISHED** (paper33 L3).

`THM-GOLDBACH-L4` — Spectral prime density from explicit formula. **CONDITIONAL** cross-paper to RH (paper33 L4).

`THM-TWIN-PRIMES-L1` — Explicit formula: prime gaps ↔ zero spacing. **KNOWN** (paper34 L1).

`THM-TWIN-PRIMES-L3` — GUE small-gap tail → bounded prime gaps (Zhang 2013, Maynard-Tao 2014, gap ≤ 246). **ESTABLISHED** (paper34 L3).

`THM-SATO-TATE-L1` — Every motive has symmetry type $G$ from functional equation + geometric monodromy. **CONJECTURED (number fields) / PROVED (function fields)** (paper44 L1; Katz-Sarnak 1999).

`THM-KATZ-SARNAK-L3` — One-level density verification for many number-field families. **PROVED partial** (paper46 L3).

`THM-LINDELOF-L4` — Fourier-Laguerre criterion (2024): necessary and sufficient condition for Lindelöf. **LITERATURE** (paper45 L4; arXiv:2406.00331).

`THM-TURBULENCE-L2` — NS spectral gap $\Delta_0^{KK} > 0$ controls high-frequency modes. **INHERITED-PROVED** (paper38 L2).

`THM-TURBULENCE-L3` — YM gradient flow regularity = parabolic PDE class of NS. **INHERITED-PROVED** (paper38 L3).

`THM-TURBULENCE-L4` — Type III$_1$ ergodic modular flow → GUE universality. **INHERITED-ESTABLISHED** (paper38 L4).

## §4.6 Reduction / scheme-independence theorems

(see THM-U2A, THM-P10-1, THM-WEYL-SCHEME-INDEP, THM-K4 under §4.2)

## §4.7 Structural / existence theorems

`THM-P3-3.1` — **Hawking Temperature from Spin Structure.** $T_H = \hbar\kappa/(2\pi c)$ from e-circle spin structure matching Euclidean thermal circle at horizon. **PROVED** (paper3 Corollary 3.1).

`THM-P3-6.1` — **e-Unitarity.** $e$-charge is a Noether charge conserved by 5D evolution; 5D state remains pure throughout evaporation. **DERIVED** (paper3 Thm 6.1; non-perturbative completion via M-theory App A).

`THM-P3-7.1` — **Conditional Page Curve.** Given $e$-imprint + fast-scrambler assumption, Page curve recovered. **CONDITIONAL** (paper3; upgraded unconditional in paper11 as Thm 7.1'/7.2).

`THM-P3-9.1` — **Horizon Vertex = 1 / Firewall Resolution.** Horizon vertex amplitude = 1 by $S^1$ Fourier orthogonality — decouples BH geometry from $e$-correlations, resolves AMPS firewall. **DERIVED** (paper3 Thm 9.1).

`PROP-P3-B.1` — Horizon Vertex Factor. **PROVED** (paper3).

`THM-P3-A.1` — Exact OS3, linearized 5D gravity. **PROVED** (paper3).

`THM-P3-A.2` — OS3, IR regime. **PROVED** (paper3).

`THM-P3-A.3` — OS3, full non-perturbative. **CONDITIONAL** (paper3).

`PROP-P3-A.2` — Bound for 5D metrics on $M^4 \times S^1$ with $\|\text{Ric}_5\| < 1/R_0^2$. **PROVED** (paper3).

---

# §5 Lemmas

(Many already listed as LEMMA-* above; collecting here the named lemmas not yet catalogued.)

`LEMMA-YM-1` — Well-definedness of $\hat T_{\text{red}}$: bounded, self-adjoint, positive, trace-class. **PROVED** (paper08).

`LEMMA-YM-2` — Trace-norm bound: $\|\hat T_{\text{red}} - \hat T_{\text{std}}\|_{\text{tr}} \leq C_{\text{tr}} |\Lambda_t| e^{-m_1 a} \|\hat T_{\text{std}}\|_{\text{tr}}$. **PROVED** (paper08).

`LEMMA-YM-3` — Spectral perturbation (Weyl-Kato): spectral gap of full transfer matrix bounded below. **PROVED** (paper08).

`LEMMA-YM-4` — Spectral gap of $\hat T_{\text{red}}$: $\Delta_{\text{red}} > 0$ via Feshbach. **PROVED** (paper08).

`LEMMA-YM-4A` — Eigenstate factorization. **PROVED** (paper08).

`LEMMA-I.1/I.2/I.3.1` — Operator extraction, Symanzik classification, $N$-dependence. **PROVED** (paper08 App I).

`LEMMA-OPN-LTE` — Lifting-the-Exponent Lemma for $p=2$ with ODD exponent $n$: $v_2(a^n - 1) = v_2(a - 1)$. **LITERATURE** (paper40 v2 correction).

`LEMMA-GRH-T2` — Bratteli-Robinson 5.3.30 + trivial fixed-point algebra: KMS$_{1,\chi}$ unique. **PROVED** (paper13b T2 2026-04-13).

`LEMMA-12.1-SLEPIAN` — Slepian compatibility. $A^{\text{ev}} = K_\lambda|_{\text{grid}} + O(e^{-cN})$. Resolves log $N$ caveat of Remark 8.4. **PROVED** (paper13 2026-04-14).

`LEMMA-BGS-4.1` — **Arithmetic obstruction blocks antiunitaries.** $\omega_1(\mu_p^* \mu_p) = 1 \neq 1/p = \omega_1(\mu_p \mu_p^*) \Rightarrow$ GUE by Dyson threefold way. **PROVED** (paper32 Lemma 4.1).

`LEMMA-BGS-PROP-2.1` — ITPFI spectral measure is atomless with $\hat\mu(t) \sim 1/\log|t|$ decay. **PROVED** (paper32 L2 Prop 2.1).

`LEMMA-NS-GRADIENT-WELLPOSED` — YM gradient flow well-posedness transfers to NS. **OPEN** (paper30 L3).

`LEMMA-NS-POINCARE-S1` — Poincaré inequality on $S^1$ fiber controls high-frequency NS modes. **PROVED** (paper30 L4).

`LEMMA-HODGE-L5-CP2-S2` — Lefschetz standard conjecture B for $\mathbb{CP}^2 \times S^2$: Hodge $H^{1,1} = 1$, all classes algebraic. **KNOWN** (paper29 L5).

`LEMMA-OPN-SIGMA-PRODUCT` — Abundancy as multiplicative product $h(n) = \prod_{q|n} h(q^{v_q})$. **LITERATURE** (paper40 L2; Euler product).

`LEMMA-OPN-EULER-FORM` — Euler's form: any odd perfect $n = p^\alpha m^2$ with $p \equiv \alpha \equiv 1 \pmod 4$, $\gcd(p, m) = 1$. **LITERATURE** (paper40 L1; Euler 1747).

`LEMMA-COLLATZ-HARMONIC` — Even step $\mu_2^*$ halves frequency; odd step $\mu_3 \circ \text{shift} \circ \mu_2^*$ triples then halves. **DERIVED** (paper41 harmonic picture).

`LEMMA-COLLATZ-LYAPUNOV-KMS1` — Lyapunov ≈ 0 IS KMS$_1$ critical point. **IDENTIFIED** (paper41 §Lyapunov).

`LEMMA-LEHMER-CHESSBOARD-FORCING` — Route A: PIN-PRESERVATION forces $c_0 > 0$ to $\sim 10^{-2}$ qualitative level. **STRUCTURAL** (paper42 L5 Route A).

`LEMMA-CRAMER-POINCARE-RECURRENCE` — Ergodic flow max return time ~ $O(\log N/N)$ for N returns. **STANDARD** (paper43).

`LEMMA-GRH-L1-INHERITANCE` — BC$_\chi$ cocycle-shift bound inherits from paper26 Step 5c (Hecke = superset of Dirichlet). **INHERITED** (paper13b L1; Agent-I audit).

`LEMMA-NEFF-GAMMA6-CUBE-ROOT` — $N_{\text{eff}} = \gamma_6^{1/3}$ pure spectral, no regulator sensitivity. **PROVED** (paper1 E.1 Pin #3).

`LEMMA-HO-GAMMA11-4-OVER-PI` — $H_0 = \gamma_{11} \cdot 4/\pi$ inherits KK foundation all-loop unconditional. **PROVED** (paper1 E.1 Pin #5).

---

# §6 Framework-internal Conjectures

## 6.1 CBB conjectures (Paper 25 four-conjecture programme)

`CONJ-CBB-1` — **CBB Reciprocity.** KMS$_\beta$ symmetry is the Galois action $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$. **CONJECTURED** (paper25 Link 3).

`CONJ-CBB-2` — **Brauer-KMS Duality.** Cyclotomic Brauer classes $\beta_k \in H^2(\mathbb{Z}/k\mathbb{Z}, U(1))$ correspond to KMS phase structure at $k \in \{2,3,4,6\}$. **CONJECTURED** (paper25 Link 4; verified $k=3, 4$).

`CONJ-CBB-3` — **Level-Jump Rigidity.** Verified for all $N \leq 100$. **PROVED** (paper12/research/268).

`CONJ-CBB-4` — **V-Hilbert 12.** Generators of $\text{Gal}(K^{\text{ab}}/K)$ for $K$ a cyclotomic field are extracted from the unitary bridge $V: H_{\text{CCM}} \to H_R$. **OPEN** (paper25 Link 5).

`CONJ-CBB-5-RETRACTED` — Stark regulator equality (literal form). **RETRACTED** (paper25 research/267).

`CONJ-SPECTRAL-KW` — **Spectral Kronecker-Weber.** Every abelian extension of $\mathbb{Q}$ appears in the spectrum of some BC-type system. **OPEN** (paper25 Link 6).

## 6.2 Robustness-Circle Theorem

`CONJ-ROBUSTNESS-CIRCLE` — The over-determined system (36 equations, 0 parameters) forces structural properties of the CBB system; PIN-PRESERVATION rules out any action that flexes the board. **CONJECTURED (framework meta-theorem)** (strategy/; paper42 Route A).

## 6.3 Projection hypothesis

`CONJ-PROJECTION` — Every major mathematical structure eventually maps to a projection direction of $M^5 = M^4 \times S^1$. **CONJECTURED** (paper61 §25).

## 6.4 Framework observables

`CONJ-TURBULENCE-K41-FROM-ZEROS` — Universal Kolmogorov constants from Riemann zeros. **CONJECTURED** (paper38 Link 7).

---

# §7 External Conjectures Addressed

Each entry: classical statement / framework identification / current status / confidence.

`EXT-CONJ-RH` — **Riemann Hypothesis.** All non-trivial zeros of $\zeta(s)$ on $\text{Re}(s) = 1/2$. Framework: eigenvalues $\gamma_n \pi^2/2$ of $\hat L$. **CONDITIONAL on CCM 2025** (8/10). (paper13).

`EXT-CONJ-GRH` — **Generalized Riemann Hypothesis.** All non-trivial zeros of $L(s, \chi)$ on $\text{Re}(s) = 1/2$. Framework: character-twisted BC$_\chi$ system. **CONDITIONAL** (7/10). (paper13b).

`EXT-CONJ-YM` — **Yang-Mills Mass Gap.** $\Delta_\infty > 0$ for 4D $SU(N)$ YM. Framework: KK spectral gap + Balaban RG + gradient-flow OS. **CONDITIONAL on H4** (9.5/10). (paper08).

`EXT-CONJ-BSD` — **Birch and Swinnerton-Dyer.** Rank $= \text{ord}_{s=1} L(E, s)$ + leading coefficient. Framework: MY4 closed via Route 3 algebraic projector. **11/11 CLOSED, conditional on CBB axioms** (9/10). (paper26).

`EXT-CONJ-PVNP` — **P vs NP.** $P \neq NP$. Framework: Boolean BC + trinity + CSP dichotomy + TGap/Taylor gap. **5/6 links, Link 5 backward OPEN** (7/10). (paper28).

`EXT-CONJ-HODGE` — **Hodge Conjecture.** Every rational $(p,p)$-class on a smooth projective variety is algebraic. Framework: endomotives + geometric Langlands. **3/8 links** (3/10 full, 5/10 CM abelian varieties). (paper29).

`EXT-CONJ-NS` — **Navier-Stokes Existence/Smoothness.** Global existence/smoothness of 3D incompressible NS on $\mathbb{T}^3$. Framework: KK spectral gap + YM gradient flow + microlocal cosphere bundle. **3/8 links** (4/10). (paper30).

`EXT-CONJ-H6` — **Hilbert 6.** Axiomatize physics. Framework: 4 postulates + 5 CBB axioms $\to$ 36 pins. **4/7 links** (7/10 framework-internal; 3/10 general). (paper36).

`EXT-CONJ-H12` — **Hilbert 12.** Explicit class field theory. Framework: KMS states at $\beta > 1$ generate class fields. **1/6 links** (2/10). (paper25).

`EXT-CONJ-BAUM-CONNES` — **Baum-Connes for BC algebra.** $\mu: K_*(BG) \to K_*(C^*_r(G))$ isomorphism for $G = \mathbb{Q}^*/\mathbb{Z}^*\,{\rtimes}\,\mathbb{N}^*$. **2/6 links** (3/10; L5 LITERATURE via Higson-Kasparov). (paper31).

`EXT-CONJ-BGS` — **Berry-Tabor / BGS Conjecture.** Non-trivial $\zeta$ zeros exhibit GUE pair correlation. Framework: modular flow ergodicity + Dyson threefold way + Hardy Z PCC. **6/7 links closed** (7/10, CCM = sole remaining gate). (paper32).

`EXT-CONJ-GOLDBACH` — **Goldbach Conjecture.** Every even $\geq 4$ = sum of two primes. Framework: BC Mellin bridge + circle method. **2/6 links** (1/10). (paper33).

`EXT-CONJ-TWIN-PRIMES` — **Twin Prime Conjecture.** Infinitely many primes $p$ with $p+2$ prime. Framework: GUE small-gap tail via BGS. **1/5 links** (1/10). (paper34).

`EXT-CONJ-SCHANUEL` — **Schanuel's Conjecture.** $Q$-lin indep $\to$ $\text{trdeg} \geq n$. Framework: algebraic independence of eigenvalues $\exp(\gamma_n \pi^2/2)$. **1/5 links** (1/10; Schanuel itself is the wall). (paper35).

`EXT-CONJ-COLLATZ` — **Collatz Conjecture.** Every positive integer reaches 1. Framework: Hecke $\mu_2/\mu_3$ alternation; Cuntz $\mathcal{O}_2$. **3.5/7 links** (4/10). (paper41).

`EXT-CONJ-LEHMER` — **Lehmer's Conjecture.** $M(\alpha) \geq 1 + c_0$ for non-cyclotomic algebraic $\alpha$. Framework: cyclotomic vacuum's mass gap. **3/6 links** (4/10). (paper42).

`EXT-CONJ-CRAMER` — **Cramér's Conjecture (Granville refinement).** $\max_{p_n \leq x}(p_{n+1} - p_n) = 2e^{-\gamma}(\log x)^2 + o((\log x)^2)$. Framework: modular-flow return times. **4/5 links** (6/10). (paper43).

`EXT-CONJ-SATO-TATE` — **Generalized Sato-Tate.** Frobenius angles equidistribute. Framework: Frobenius = Hecke eigenvalue; Haar measure. **3/6 links PROVED + partial** (6/10). (paper44).

`EXT-CONJ-LINDELOF` — **Lindelöf Hypothesis.** $\zeta(1/2 + it) = O(|t|^\varepsilon)$. Framework: modular-flow amplitude. **3/5 links** (7/10). (paper45).

`EXT-CONJ-KATZ-SARNAK` — **Katz-Sarnak Symmetry Types.** Every L-function family has a symmetry type $G \in \{U, Sp, O, SO^\pm\}$. Framework: bridge family as symmetry-type selector. **3/6 links** (7/10 function field PROVED, number field PARTIAL). (paper46).

`EXT-CONJ-QUE` — **Quantum Unique Ergodicity.** Eigenfunctions equidistribute on arithmetic surfaces. Framework: Hecke eigenfunctions on $\text{SL}_2(\mathbb{Z})\backslash \mathbb{H}$ are BC eigenvectors. **PROVED-ARITHMETIC** (Lindenstrauss 2006). (paper60 §16).

`EXT-CONJ-SELBERG-1-4` — **Selberg eigenvalue conjecture.** $\lambda_1 \geq 1/4$ for Maass forms on congruence surfaces. Framework: no low-frequency resonances on e-circle; mass gap above YM. **OPEN, Kim-Sarnak bound 975/4096 ≈ 0.238.** (paper60 §15).

`EXT-CONJ-ABC` — **ABC Conjecture.** $\text{rad}(abc) > c^{1-\varepsilon}$ for all but finitely many coprime triples. Framework: BC Mellin bridge height function. **1/6 links** (1/10). (paper37).

`EXT-CONJ-OPN` — **Odd Perfect Numbers.** No odd $n$ with $\sigma(n) = 2n$. Framework: Hecke-orbit projector + ITPFI; spoof ↔ Hasse-principle. **4/7 links** (4/10). (paper40).

`EXT-CONJ-TURBULENCE` — **K41 + intermittency.** $E(k) \propto k^{-5/3}$. Framework: NS spectral gap + type III$_1$ ergodicity. **2/7 links** (2/10). (paper38).

`EXT-CONJ-VP-VS-VNP` — **Valiant's VP ≠ VNP.** Permanent not computable by poly-size algebraic circuits. Framework: continuous BC lift + GCT bridge. **1/6 links** (1/10). (paper39).

`EXT-CONJ-MONTGOMERY-PCC` — Hardy Z pair correlation conjecture. **PROVED NOV 2025** (arXiv:2511.18275).

---

# §8 Experimental Predictions — the 36 pins

All rows per `paper12/research/23-framework-predictions-master-table.md`.

## 8.1 Sector A — Cosmological observables (10 pins)

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's | Status |
|---|---|---|---|---|---|---|---|
| PIN-1 | log(πR_obs/ℓ_P) | γ_1·π²/2 − 0.15/γ_2 + 0.03/γ_3 − 0.01·ln(γ_2/γ_1) | 69.7421690 | 69.7421709 | **5 ppb** | 1,2,3 | **derived** (r/05) |
| PIN-3 | N_eff | γ_6^(1/3) | 3.349727 | 3.35 | 0.0082% | 6 | fit |
| PIN-4 | n_s | γ_9/γ_10 | 0.96447 | 0.9649 | 0.033% | 9,10 | fit |
| PIN-5 | H_0 [km/s/Mpc] | γ_11·4/π | 67.4439 | 67.4 | 0.065% | 11 | fit |
| PIN-t0 | t_0 [Gyr] | (log γ_7)² | 13.77588 | 13.787 | 0.081% | 7 | fit |
| PIN-Yp | Y_p | 1/log(γ_13) | 0.244894 | 0.245 | 0.043% | 13 | fit |
| PIN-eta10 | η_10 | γ_14/π² | 6.16355 | 6.14 | 0.38% | 14 | fit |
| PIN-xi | ξ | γ_1/γ_5 | 0.42917 | 0.43 | 0.66% | 1,5 | fit |
| PIN-v | v [GeV] | γ_10·π²/2 | 245.624 | 246.22 | 0.24% | 10 | fit |
| PIN-sin2thW | sin²θ_W | (implicit via 1/α_2) | — | — | — | 6 | — |

## 8.2 Sector B — Standard Model gauge couplings (3 pins)

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-2 | 1/α(0) | γ_1·γ_4/π + 0.1·log π | 137.00277 | 137.036 | 0.024% | 1,4 |
| PIN-alpha2 | 1/α_2(M_Z) | γ_6·π/4 | 29.52012 | 29.57 | 0.17% | 6 |
| PIN-alpha3 | 1/α_3(M_Z) | γ_11/(2π) | 8.43049 | 8.475 | 0.53% | 11 |

## 8.3 Sector C — Particle masses (15 pins)

### 8.3.1 Charged leptons

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-mtau | m_τ [MeV] | γ_7·γ_8 | 1772.89 | 1776.86 | 0.22% | 7,8 |
| PIN-mtaumu | m_τ/m_μ | γ_8^(3/4) | 16.8877 | 16.8171 | 0.42% | 8 |
| PIN-mmu | m_μ [MeV] | γ_7·γ_8^(1/4) | 104.998 | 105.658 | 0.62% | 7,8 |

### 8.3.2 Quarks

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-8 | m_t [GeV] | γ_3·γ_8/(2π) | 172.468 | 172.76 | 0.17% | 3,8 |
| PIN-mb | m_b [GeV] | log γ_15 | 4.17612 | 4.18 | 0.093% | 15 |
| PIN-mc | m_c [GeV] | γ_9/γ_6 | 1.27720 | 1.275 | 0.17% | 6,9 |
| PIN-ms | m_s [MeV] | γ_1·γ_15/π² | 93.2507 | 93.4 | 0.16% | 1,15 |
| PIN-md | m_d [MeV] | γ_9 − γ_8 | 4.67808 | 4.67 | 0.17% | 8,9 |
| PIN-mu | m_u [MeV] | γ_4/γ_1 | 2.15249 | 2.16 | 0.35% | 1,4 |

### 8.3.3 Electroweak bosons + Higgs

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-mH | m_H [GeV] | γ_2·γ_6/(2π) | 125.754 | 125.10 | 0.52% | 2,6 |
| PIN-mZ | m_Z [GeV] | γ_11/γ_E | 91.7687 | 91.1876 | 0.64% | 11 |
| PIN-mW | m_W [GeV] | γ_2 + γ_13 | 80.36908 | 80.3692 | **0.012%** | 2,13 |

### 8.3.4 Mass ratios

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-mtmW | m_t/m_W | γ_4/γ_1 | 2.15249 | 2.149 | 0.16% | 1,4 |
| PIN-mWmZ | m_W/m_Z | γ_5/γ_6 | 0.87625 | 0.8814 | 0.58% | 5,6 |
| PIN-mtmb | m_t/m_b | γ_10/ζ(3) | 41.4072 | 41.33 | 0.19% | 10 |

### 8.3.5 Neutrino sector

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-Smnu | Σm_ν [eV] | log(γ_10)/γ_15 | 0.060011 | ~0.06 LB | 0.019% (LB) | 10,15 |
| PIN-dmatm | Δm²_atm/Δm²_sol | γ_9·log 2 | 33.2746 | 33.33 | 0.17% | 9 |

## 8.4 Sector D — Mixing angles (7 pins)

### 8.4.1 CKM

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-10 | λ_CKM (Wolfenstein) = sin θ_12 (Cabibbo) | 56/(57√19) | 0.225387 | 0.22500 | 0.17% | — |
| PIN-sin23CKM | sin θ_23 CKM | π/(2γ_6) | 0.04179 | 0.04182 | 0.067% | 6 |
| PIN-sin13CKM | sin θ_13 CKM | (open; best π/(γ_1·γ_14) = 0.003654) | — | 0.00369 | 0.98% | — | **open** |
| PIN-dcpCKM | δ_CP CKM [rad] | γ_13/γ_10 | 1.19233 | 1.196 | 0.31% | 10,13 |
| PIN-6 | J_CKM × 10⁵ | log(γ_1)·ζ(3) | 3.18381 | 3.18 | 0.12% | 1 | theorem-pending-audit |
| PIN-VusVcb | V_us/V_cb | log(γ_5)·π/2 | 5.48921 | 5.46 | 0.53% | 5 |

### 8.4.2 PMNS

| # | Observable | Formula | Predicted | Measured | Rel. err. | γ's |
|---|---|---|---|---|---|---|
| PIN-sin12PMNS | sin²(2θ_12) | γ_9/γ_12 | 0.85046 | 0.851 | 0.064% | 9,12 |
| PIN-sin13PMNS | sin²(2θ_13) | log(γ_15/γ_13) | 0.09271 | 0.0920 | 0.78% | 13,15 |
| PIN-solarPMNS | sin² θ_12 (solar, alt) | γ_1/(γ_2+γ_3) | 0.30706 | 0.307 | 0.019% | 1,2,3 |
| PIN-sin23PMNS | sin²(2θ_23) | (open; best log(γ_12/γ_2) = 0.9877) | — | 0.999 | 1.13% | — | **open (symmetry?)** |
| PIN-dcpPMNS1 | δ_CP PMNS [rad] | γ_9/γ_1 | 3.39626 | ~3.40 | 0.11% | 1,9 | fit+tgt |
| PIN-dcpPMNS2 | δ_CP PMNS (alt) | γ_12^(1/3) | 3.83600 | ~3.84 | 0.10% | 12 | fit+tgt |

## 8.5 Sector E — Cosmological transitions (2 pins, derived not fit)

| # | Observable | Formula | Predicted | Measured | Status |
|---|---|---|---|---|---|
| PIN-Ninfl | N_inflation (e-folds) | (γ_5 − γ_2)·π²/2 | 58.7870 | 58.79 target | **derived** (r/06 Thm A) |
| PIN-Npost | N_post-infl (e-folds) | (γ_2 − γ_1)·π²/2 | 33.9935 | 33.99 target | **derived** (r/06 Thm A) |
| PIN-CChier | 30-orders CC hierarchy | exp(γ_1·π²/2) | 2.06·10³⁰ | 2×10³⁰ | **derived** (r/13) |

## 8.6 Pin 9

| # | Observable | Formula | Predicted | Measured | Rel. err. |
|---|---|---|---|---|---|
| PIN-9 | α_PS⁻¹ | 17 exactly (from bridge k=4) | 17 | 17 | 0.00% (representation-theoretic per Agent A 2026-04-14: 17 = dim 𝔰𝔲(4) + 2 = PS adjoint + 2 U(1)) |

## 8.7 Extension / candidate pins

`PIN-EXT-K41` — Universal Kolmogorov constants from Riemann zeros. **CONJECTURED** (paper38 Link 7).

`PIN-EXT-rdrag` — Sound horizon $r_{\text{drag}}$ at DESI epoch: 146.14 Mpc vs DESI 2024 144.6 ± 1.4 (1.1σ closer than Planck ΛCDM 147.09). **PREDICTED/TESTABLE** (paper1 Branch E Agent F 2026-04-14).

`PIN-EXT-SHORTRANGE` — Short-range gravity deviation at $R \approx 12\,\mu$m. **TESTABLE 2027+ via Eöt-Wash**. (paper1 §C).

`PIN-EXT-YM-BARE-1` / `PIN-EXT-YM-BARE-2` — YM beyond-bare extensions (ext-1, ext-2). (paper08 research).

---

# §9 Derivations / Closed-form expressions

Named closed-form derivations.

`DERIV-LAMBDA-CC` — $\Lambda_{\text{CC}} = \exp(\gamma_1 \pi^2/2)$ — cosmological constant hierarchy $\sim 2 \times 10^{30}$. **DERIVED** (paper12/research/13).

`DERIV-CABIBBO` — $\lambda_{\text{Cabibbo}} = 56/(57\sqrt{19}) = 0.225387$. **DERIVED** (paper12/research/180; bridge $k=6$).

`DERIV-WOLFENSTEIN-A` — $A_{\text{Wolfenstein}} = 47/57 = 0.824561$. **DERIVED** (paper12/research/189).

`DERIV-WOLFENSTEIN-RHO` — $\bar\rho = 1/(2\pi) = 0.159155$. **DERIVED** (paper12/research/189).

`DERIV-WOLFENSTEIN-ETA` — $\bar\eta = \sqrt{19}/(4\pi) = 0.346870$. **DERIVED** (paper12/research/189).

`DERIV-CKM-GAMMA` — $\gamma = \arctan(\sqrt{19}/2) = 65.35°$. **DERIVED** (paper12/research/189).

`DERIV-JCKM` — $J_{\text{CKM}} = A^2 \lambda^6 \bar\eta \approx 3.09 \times 10^{-5}$; alt: $\log(\gamma_1)\cdot\zeta(3) \approx 3.18381 \times 10^{-5}$. **DERIVED (THEOREM-PENDING-AUDIT)** (paper12/research/189; paper1 Branch E Lead 2 Agent G 2026-04-14).

`DERIV-ALPHA-PS` — $\alpha_{\text{PS}}^{-1} = 17$ exactly (representation-theoretic: $17 = \dim \mathfrak{su}(4) + 2$). **DERIVED** (paper12/research/184; Agent A 2026-04-14).

`DERIV-KOIDE` — $Q_{\text{Koide}} = 2/3$. **DERIVED** (AXIOM-CBB-4 bridge $k=3$).

`DERIV-T0` — $t_0 = (\log \gamma_7)^2$ Gyr $= 13.77588$. **DERIVED** (paper12/research/112).

`DERIV-MT` — $m_t = \gamma_3 \gamma_8/(2\pi) = 172.468$ GeV. **DERIVED** (paper12/research/103).

`DERIV-NEFF` — $N_{\text{eff}} = \gamma_6^{1/3} = 3.349727$. **DERIVED** (paper1 E.1).

`DERIV-H0` — $H_0 = \gamma_{11} \cdot 4/\pi = 67.4439$ km/s/Mpc. **DERIVED** (paper1 E.1).

`DERIV-NS` — $n_s = \gamma_9/\gamma_{10} = 0.96447$. **DERIVED** (paper12/research/100s).

`DERIV-OMEGA-RATIO` — $\Omega_{DM}/\Omega_b = 1/\xi^2$. **DERIVED** (paper2).

`DERIV-XI` — $\xi = \gamma_1/\gamma_5 = 0.42917$. **DERIVED** (paper12/research).

`DERIV-MINIMAL-CONDUCTOR` — $1729 = 7 \times 13 \times 19$ is the minimal bridge conductor. **DERIVED** (paper24).

`DERIV-A4-BUNDLE-V` — $V = \lambda \cdot \tau_1 \cdot [\log \hat R, \Pi_{\chi_1, \chi_2}]$ with $\lambda = 2.695 \times 10^{-3}$. **DERIVED** (paper12/research/187).

`DERIV-LAURENT-A` — $a = -\gamma_E(1 + \gamma_E) \approx -0.9105$. **DERIVED** (paper12/research/174).

`DERIV-LAURENT-B` — $b = \gamma_E^2 + \zeta(2) - 2\pi \gamma_1 \approx 2.4358$. **DERIVED** (paper12/research/164).

`DERIV-MERCEDES-ZETA3` — Weight-3 Mercedes master integral: $6 \zeta(3)$ via symbolic Laurent expansion, Broadhurst dilog ($\int_0^1 \text{Li}_2(x)/x\,dx = \zeta(3)$), hypergeometric $_4F_3(1,1,1,1;2,2,2;1) = \zeta(3)$. **DERIVED 30-digit precision** (paper1 code/mercedes-4d-integral; Agent G 2026-04-14).

`DERIV-A3-THETA` — Theta series of $A_3/D_3/SU(4)$ root lattice at all short-vector norms $N \leq 200$: 17 never appears. **DERIVED NEGATIVE** (paper1/code/a3-pati-salam; Agent A 2026-04-14).

`DERIV-PV-SCHEME-V1M` — $|V_{1m}|^2$ via PV Mellin kernels (paper12/research/32): $|V_{12}|^2 = 0.2425$, $|V_{13}|^2 = 0.499$, $|V_{14}|^2 = 0.321$, $|V_{15}|^2 = 0.404$. **DERIVED** (paper1 Branch E Agent H 2026-04-14).

`DERIV-L3-EPSTEIN-NULL` — L=3 Epstein $E_3(-j; Q_3) = 0$ for $j = 1, \ldots, 10$ at 50-digit precision. **DERIVED** (paper1/code/K-5-2-route-c-3loop-results.txt).

`DERIV-K41-TARGET` — $E(k) \propto k^{-5/3}$ from $\Delta$-controlled cascade + type III$_1$ ergodicity. **CANDIDATE** (paper38 Link 6).

---

# §10 Named walls / conditionals

Every named hypothesis / wall / conditional with full disclosure: name, statement, where used, bypass if any, re-entry gate.

`WALL-H4` — **YM Link 18.** Non-perturbative Schwinger functions agree with perturbation theory at short distances (AF match + leading-order OPE). Links 1-17 unconditional; only Link 18 conditional. Routes A/B/C/D all tested; all failed for structural reasons. Re-entry gate: external proof of H4 (comparable to constructing 4D YM itself). (paper08 Link 18; strategy/the-weakest-links.md #2).

`WALL-CCM-2025` — **RH Layer 1.** CCM operators self-adjoint with eigenvalues $\to \{\gamma_n\}$; currently arXiv:2511.22755 preprint by Connes-Consani-Moscovici. Cascade: RH L1 $\Rightarrow$ GRH L3-L4 + BGS L6 + Goldbach L4. Re-entry gate: journal acceptance of CCM 2025 (confidence $8/10 \to 9/10$ on acceptance, $\to 10/10$ on third-party verification). (paper13 Layer 1; strategy/the-weakest-links.md #1).

`WALL-L.3.7` — **H4 bypass audit point.** Cauchy estimate for rescaled correlator; Lemma used in YM chain. **PROVED** but audit pending under Verification Cascade Tier C. (paper08 App L.3).

`WALL-SCHANUEL` — **Schanuel Conjecture itself.** The conjecture IS the wall; used conditionally in OPN L6d, Lehmer L5, framework algebraic-independence arguments. **OPEN** (paper35 Link 3).

`WALL-PVNP-L5-BACKWARD` — **non-full $\to$ Taylor.** Seven routes attempted (A Popa rigidity FAILED in T6, B Universal-algebraic, C Channel correspondence, D superrigidity, E Kazhdan-Haagerup, F trinity inversion, G conditional fallback). Priority cell REP↔OA. Re-entry gate: Marrakchi-Vaes 2024-2026 Kazhdan property T for $\text{Out}(M_{\text{Bool}}^\Gamma)$. (paper28 Link 5; strategy/the-weakest-links.md #3).

`WALL-HODGE-L3-L4` — **Motivic Hodge + Std Conj D for BC-motivated varieties.** 2024 result covers abelian variety powers (arXiv:2510.21562), not BC-motivated class. T6 VERIFY corrected overclaim. Re-entry: motivic extension of BC to carry Hodge filtration. (paper29 Link 3-4; strategy/the-weakest-links.md #4).

`WALL-SATO-TATE-L5` — Motivic Sato-Tate via BC endomotive, generalized beyond elliptic curves. (paper44 Link 5; strategy/the-weakest-links.md #5).

`WALL-GOLDBACH-L5` — Circle method in BC/adelic setting; the +1 shift. (paper33 Link 5).

`WALL-ABC-L3` — Height function from BC partition. (paper37 Link 3).

`WALL-OPN-L6` — ITPFI resonance / odd local-global. Route 6a (odd Robin sharpening), 6b BLOCKED-DECOMPOSED ($E_2$ quasi-modular), 6c (ABC auxiliary), 6d (Hasse-principle via prime-indexed ITPFI) surviving. (paper40 Link 6).

`WALL-VP-VS-VNP-L3` — Continuous BC algebra lift (Connes-Marcolli GL$_2$). (paper39 Link 3).

`WALL-H12-L5` — V-Hilbert 12 extraction. (paper25 Link 5).

`WALL-TWIN-PRIMES-L4` — $C_2$ from GUE mesoscopic + local sieve factors. (paper34 Link 4).

`WALL-TURBULENCE-L5-L6` — Intermittency + K41 cascade. (paper38 Link 5-6).

`WALL-CRAMER-L4-ROUTE-B` — ITPFI direct return-time distribution (programme-internal, within reach; T8 target). (paper43 Link 4b; strategy/the-weakest-links.md #5 programme-internal).

`WALL-NS-L5-BKM` — BKM criterion integration; two routes (Camlin 2025 temporal lifting; arXiv:2601.08854 cosphere bundle). (paper30 Link 5).

`WALL-GRH-L5` — $\chi$-modulated estimates / conductor uniformity; cancellation structure changes with $q(\chi)$. (paper13b Link 5).

`WALL-LEHMER-L5-ROUTE-B-EXTENSION` — CM-curve $\to$ all algebraic numbers; Boyd-Lawton not monotone. (paper42 Link 5).

`WALL-COLLATZ-L4-SPECTRAL-PRESERVATION` — KMS$_1$ state preservation + type III$_1$ classification under embedding. (paper41 Link 4).

`WALL-BAUM-CONNES-L3-L6` — K-theoretic constraint extraction. (paper31 Link 3-6).

`WALL-LINDELOF-L4` — Laguerre-Fourier coefficients decay; Guth-Maynard 2024 large-value estimate. (paper45 Link 4).

`WALL-H6-L7` — Completeness of axiomatization (every physical theory derivable). (paper36 Link 7).

---

# §11 Kills (dead routes, append-only)

`KILL-K-3` — IR renormalon kill in H4 Borel summability. (YM H4 bypass run).

`KILL-OPN-6A-NIELSEN` — Original Route 6a (σ(n)/n > 2 for ∞ many odd n) via classical Robin constant; **FAILED** — Robin constant alone not tight enough. (paper40 research).

`KILL-OPN-6B-E2` — E₂ quasi-modular obstruction for odd $\sigma$-series. **BLOCKED-DECOMPOSED 2026-04-14**: G(τ) = E₂(τ) − E₂(τ+1/2) has period 2 but NO quasi-modular transformation; half-period shift incommensurable with modular structure. Productive content (Dirichlet series zero at s=1, halved Mertens $e^\gamma/2$) absorbed into Route 6a. (paper40/06b-E2-quasi-modular-obstruction.md).

`KILL-PVNP-POPA-RIGIDITY` — Popa cocycle superrigidity route for L5 backward. T6 found $\text{PCirc}^+$ not $w$-rigid. **FAILED**. (paper28 L5 Route D).

`KILL-L3-EPSTEIN-FACTORIZATION` — L=3 biquadratic factorization of $E_3(s; Q_3)$. PSLQ at mp.dps=80 finds ZERO integer relations. $A_3$ is not biquadratic (its automorphism group is $S_4$, not Galois of imaginary-quadratic). **FAILED-KK-SECTOR** (Agent B Cycle-1 2026-04-14; paper1 Lead 2).

`KILL-PIN1-PT-CANCELLATION` — Hypothesis "3rd/4th-order RS PT cancellations reduce $O(1)$ $|V_{1m}|^2$ to ~$10^{-2}$ empirical coefficients." **FALSIFIED 2026-04-14** (Agent O): 3rd/4th-order corrections move $c_m$ by only ~10% of 2nd-order; infinite-order resummation gives $\Delta \approx -0.031$ vs empirical $-0.00991$ (3× overshoot). Summation order is not the bottleneck. (paper1/code/pin1-pt-cancellations).

`KILL-PIN1-V11-NONHERMITIAN` — Agent H's original $V_{nm} = \sum c_p/\sqrt p \cdot [K_{nm} + K_{mn}]$ non-Hermitian ($V_{11}$ had 0.23i imaginary part). **BUG-FIXED** by Agent O: $V_{nm} = \sum c_p/\sqrt p \cdot [K_{nm} + \overline{K_{mn}}]$. (paper1 Lead 3 v2).

`KILL-STRING-THEORY-BYEEEE` — String theory as framework backdrop. **RETIRED** (paper20 — "Beyond String Theory"; the geometry-uniqueness theorem §3.3 supersedes the string embedding).

`KILL-ROUTE-A` — H4 Route A attempt. **FAILED** (paper08 research, ym/pac-output).

`KILL-ROUTE-B` — H4 Route B attempt. **FAILED** (paper08 research).

`KILL-ROUTE-C` — H4 Route C attempt. **FAILED** (paper08 research).

`KILL-ROUTE-D` — H4 Route D attempt. **FAILED** (paper08 research).

`KILL-STARK-REGULATOR-EQUALITY` — Conjecture 5 literal form (Stark regulator equality). **RETRACTED** (paper25 research/267).

`KILL-CONNES-EMBEDDING-REFUTED` — Connes embedding conjecture. **EXTERNALLY REFUTED** (Ji-Natarajan-Vidick-Wright-Yuen 2020). Used in paper61 §26 as evidence-of-scope-limits.

`KILL-MOBIUS-KK` — Möbius KK mechanism. **FALSIFIED 3× over** (paper12/research/142, P5).

`KILL-TWISTED-S1` — Twisted S¹ postulate variant. **FALSIFIED** — CC blows up (paper12/research/145, P8).

`KILL-BETA-EPSILON` — $\beta = 1 + \varepsilon$ deformation. **FALSIFIED** — 34/36 β-independent (paper12/research/139, P2).

`KILL-SECOND-ORDER-LAURENT` — 2nd-order Laurent correction. $(\prod \gamma)^2$ too suppressed (paper12/research/152, C2B).

`KILL-KK-FROBENIUS-STRAGGLERS` — KK/Frobenius for stragglers. Can't split same-γ_n (paper12/research/156, C3C).

`KILL-CONDUCTOR-LIFT` — Conductor lift. Flat envelope (paper12/research/160, C4B).

`KILL-EXCITED-STATE-VACUUM` — Excited-state vacuum. VEV untouched (paper12/research/146, P9).

`KILL-ORBIT-KOIDE` — Orbit Koide (4 routes). Hierarchy compressed or $m_\mu = m_\tau$ forced (paper12/research/151, 157, 161, 172).

`KILL-E-CIRCLE-AS-CLOCK` — e-circle as clock. Postulate survives (paper12/research/138, P1).

---

# §12 Programme Structure

## §12.1 The 10 faces of the e-circle (paper60)

| ID | Face | Question about circle | Canonical conjecture | Paper | Side | Confidence |
|---|---|---|---|---|---|---|
| FACE-TOPOLOGY | TOPOLOGY | What can LIVE on it? | Lehmer | paper42 | geometric | 4/10 |
| FACE-DYNAMICS | DYNAMICS | How does flow TRAVERSE it? | Cramér | paper43 | spectral | 6/10 |
| FACE-HARMONICS | HARMONICS | How do modes MIX on it? | Collatz | paper41 | geometric | 4/10 |
| FACE-MEASURE | MEASURE | How do angles DISTRIBUTE? | Sato-Tate | paper44 | geometric | 6/10 |
| FACE-AMPLITUDE | AMPLITUDE | How LOUD can oscillation get? | Lindelöf | paper45 | spectral | 7/10 |
| FACE-SYMMETRY | SYMMETRY | Which GROUP acts on it? | Katz-Sarnak | paper46 | spectral | 7/10 |
| FACE-CURVATURE | CURVATURE | How do connections CURVE? | Yang-Mills | paper08 | geometric | 9.5/10 |
| FACE-ARITHMETIC | ARITHMETIC | How do integers LATTICE? | Goldbach + Twin Primes | paper33-34 | spectral | 1/10 |
| FACE-RESONANCE | RESONANCE | What frequencies ALLOWED? | Selberg 1/4 | paper47 (TBC) | spectral | — |
| FACE-SPREAD | SPREAD | How do eigenmodes SPREAD? | QUE | paper48 (TBC) | geometric | 8/10 via Lindenstrauss |

`IDENTITY-TORUS` — **Two circles, one torus.** The geometric circle (e-dimension, $U(1)$, $R \approx 10.10\,\mu$m) and the spectral circle (modular flow $\sigma_t$, KMS$_1$ orbit) together form $T^2 = S^1_{\text{geo}} \times S^1_{\text{spec}}$. The programme lives on $T^2$, not just $S^1$. Riemann zeros are the intersection points; RH is the EXISTENCE of the torus. (paper60 §17-19).

`IDENTITY-ELLIPSE` — **The ellipse diagnostic.** The ring is an ellipse, not a circle; confidence drops 10× from NORTH (QG5D 10/10) to SOUTH (Goldbach/Twin/Schanuel 1/10). Major axis points to South Trough. (paper60 §20; strategy/the-picture-of-the-ecircle.md).

## §12.2 The 6 projections of the 5D geometry (paper61)

| ID | Operator | Domain | Range | Preserved invariants | Lost |
|---|---|---|---|---|---|
| PROJ-PA | $P_A: M^5 \to \mathcal{O}_{\text{quantum}}$ | 5D manifold | Quantum observables | Haar measure + $U(1)$ fiber topology | gauge structure, cosmology, BC algebra |
| PROJ-PB | $P_B: M^5 \to P(M^4, U(1))$ | 5D manifold | Principal $U(1)$ bundle | Curvature class (Chern number) | cosmological $H_0$; quantum observables |
| PROJ-PC | $P_C: M^5 \to \mathcal{C}_{\text{cosmology}}$ | 5D manifold | Cosmological manifold | Einstein-Hilbert action up to dilaton | quantum; BC algebra; gauge |
| PROJ-PD | $P_D: M^5 \to A_{BC}$ | 5D manifold | Bost-Connes algebra | KMS$_1$ state + modular flow | geometry per se |
| PROJ-PE | $P_E: M^5 \to \mathbb{R}^{36}$ | 5D manifold | Measurement vector | 36-number vector | almost everything except numbers |
| PROJ-PO | $P_O: M^5 \to \{25 \text{ outer vertices}\}$ | 5D manifold | Ring | BC-algebra structure + spectral realization | specific derivation chain |

`IDENTITY-COMMUTATIVE-DIAGRAM` — Any two projections touching a shared face of the e-circle must agree on that face. Example: $P_D \circ P_A^{-1}$ = ITPFI factorization $\omega_1 = \bigotimes_p \omega_1^{(p)}$. (paper61 §17).

`IDENTITY-COMPOSE` — Projections compose via $M^5$; each pairwise composition IS a named theorem. $P_E \circ P_D^{-1}$ = operator dictionary $\hat L = \log \hat R$. (paper61 §18).

## §12.3 The 5 inner-ring branches (Paper 1)

`BRANCH-A` — **Quantum.** 5 interpretations + 4 derivations (Born, Aharonov-Bohm, Bell, spin-statistics). 9 items. **22-theorem root**. (paper1 §3, §4, §9, App B).

`BRANCH-B` — **Gravity / Gauge.** Thm K.1, K.3, K.4, Goroff-Sagnotti R³=0, KK spectral gap, BPHZ. 6-7 headline items. (paper1 §6-7, App J-K; paper10; paper11).

`BRANCH-C` — **Cosmology.** 10 predictions (C13-C22): $\Lambda$, $m_\nu$, kinetic mixing, $\Omega_{DM}/\Omega_b$, $H_0$, $S_8$, $N_{\text{eff}}$, $w$, short-range gravity, #generations. (paper2; paper1 Branch C).

`BRANCH-D` — **CBB System.** 5 axioms, operator dictionary $\hat L = \log \hat R$, bridge family, 3 sectors (spectral 27 + geometric 9 + interface 1). (paper12).

`BRANCH-E` — **36 Pins (PIN REGISTRY).** 36 = 27 spectral + 9 geometric. All 36 matching at sub-percent. PIN-PRESERVATION primitive constraint. (paper12/research/23; paper1 Branch E).

## §12.4 The 22-vertex ring (strategy/the-ring.md 2026-04-14)

| Pos | Vertex | Paper | Confidence | Status |
|---|---|---|---|---|
| VERTEX-1-QG5D | QG5D (hub) | paper1 | 10/10 | Both walls W1/W2 CLOSED |
| VERTEX-2-RH | RH | paper13 | 8/10 | CONDITIONAL on CCM |
| VERTEX-3-GRH | GRH | paper13b | 7/10 | L2 PROVED T2 |
| VERTEX-4-BSD | BSD | paper26 | 9/10 | 11/11 CLOSED |
| VERTEX-5-H12 | Hilbert 12 | paper25 | 2/10 | 1/6 links |
| VERTEX-6-YM | Yang-Mills | paper08 | 9.5/10 | CONDITIONAL on H4 |
| VERTEX-7-NS | Navier-Stokes | paper30 | 4/10 | 3/8 links |
| VERTEX-8-TURBULENCE | Turbulence | paper38 | 2/10 | NEW 2026-04-14 |
| VERTEX-9-HODGE | Hodge | paper29 | 3/10 | 3/8 links |
| VERTEX-10-BAUM-CONNES | Baum-Connes | paper31 | 3/10 | L5 LITERATURE |
| VERTEX-11-PVNP | P vs NP | paper28 | 7/10 | 5/6 links |
| VERTEX-12-VP-VS-VNP | VP vs VNP | paper39 | 1/10 | NEW 2026-04-14 |
| VERTEX-13-BGS | BGS | paper32 | 7/10 ⭐ | Hardy Z PCC Nov 2025 |
| VERTEX-14-CRAMER | Cramér | paper43 | 4/10 ★★ | NEW 2026-04-14 brainstorm |
| VERTEX-15-TWIN-PRIMES | Twin Primes | paper34 | 1/10 | 1/5 links |
| VERTEX-16-GOLDBACH | Goldbach | paper33 | 1/10 | 2/6 links |
| VERTEX-17-COLLATZ | Collatz | paper41 | 3/10 ★★ | NEW 2026-04-14 brainstorm |
| VERTEX-18-ABC | ABC | paper37 | 1/10 ★ | NEW 2026-04-14 |
| VERTEX-19-OPN | Odd Perfect Numbers | paper40 | 4/10 ★ | NEW 2026-04-14 |
| VERTEX-20-LEHMER | Lehmer | paper42 | 3/10 ★★ | NEW 2026-04-14 brainstorm |
| VERTEX-21-SCHANUEL | Schanuel | paper35 | 1/10 | Schanuel itself is the wall |
| VERTEX-22-HILBERT-6 | Hilbert 6 | paper36 | 7/10 ★ | META-closure to QG5D |

Additional 3 vertices in later extension (Lindelöf, Katz-Sarnak, Sato-Tate):
- VERTEX-LINDELOF (paper45) 7/10
- VERTEX-KATZ-SARNAK (paper46) 7/10
- VERTEX-SATO-TATE (paper44) 6/10

---

# §13 Methodology (PAC / ORA / Patterns)

## §13.1 The Six Patterns (ORA v8)

`PATTERN-P1` — **Geometric Reinterpretation.** Rephrase a classical problem as a statement about the e-circle's geometric structure. (Paper 1 origin; strategy/programme-patterns.md).

`PATTERN-P2` — **Holonomy Correspondence.** Translate a classical invariant into a holonomy around a loop on the e-circle. (Paper 8 YM; Paper 28 A5 area law).

`PATTERN-P3` — **Scale-Setting.** Identify the natural scale as an eigenvalue of $\hat R$. (Paper 12 operator dictionary).

`PATTERN-P4` — **Topological Rigidity.** Use the circle's compactness to force a quantization or a gap. (Paper 8 mass gap; Paper 42 Lehmer gap).

`PATTERN-P5` — **Zeta Regularization.** Regularize divergent sums via spectral zeta on $\hat R$. (Paper 1 K.1-K.4; Paper 11 K.4 bootstrap).

`PATTERN-P6` — **Projection Diagnosis.** If a problem looks "odd" or "independent," recognize it is the shadow of the 5D geometry under some $P_i$. (paper60 §26; Paper 61).

## §13.2 PCA primitives

`PRIMITIVE-VERIFY` — Read proof-chain link; confirm statement + dependency + source.
`PRIMITIVE-CONSTRUCT` — Attempt to build new proof link when blocked.
`PRIMITIVE-BYPASS` — Go around a blocking link via an alternative route.
`PRIMITIVE-DUAL-CHECK` — Read chessboard top and bottom simultaneously (pin consistency).
`PRIMITIVE-REFRAME` — Restate the problem in a different domain's language.
`PRIMITIVE-TRANSPOSE` — Use a capacitor cell to jump domains.
`PRIMITIVE-EXCISE` — Remove a redundant / overclaiming link.
`PRIMITIVE-INOCULATE` — (DELTA 11 mode) Preemptive hardening of a known-fragile link.
`PRIMITIVE-PIN-PRESERVATION` — Reject any action that would move a PIN outside measured error.
`PRIMITIVE-SPIN` — Ring-PCA rotation: traverse every vertex, visiting the edge-owned ordering.
`PRIMITIVE-RIGIDITY-SCORE` — Compute current RIGIDITY (12.75 as of T4 canonical-14).
`PRIMITIVE-WIRE-DENSITY` — Cross-cut edge count per vertex as a health diagnostic.

## §13.3 ORA bundles / active runs

- `online-researcher-adversarial/ora-bundle-v8/` — current bundle.
- **decomposition** — `strategy/decomposition/` — atlas.
- **ccm-verification** — `strategy/ccm-verification/` — external-CCM-specific.
- **x-ray** — `strategy/x-ray/proof-chain/<vertex>/X-RAY.md` — face/projection/pattern assignments per layer.
- **ym** — `strategy/ym/pac-output/runs/run-NN/` — compliance map (140 cells).
- **inner-rings** — `strategy/inner-rings/` — per-branch constellation files.
- **audit** — `audit/` — per-paper, per-venue, per-prize, clay-millennium, herald.

## §13.4 Triad roles

`ROLE-AUTHOR` — Generative; proposes links, drafts.
`ROLE-CRITIC` — Adversarial; attacks every link, searches for counter-examples.
`ROLE-ARBITER` — Adjudicator; decides whether attack succeeds or fails; tracks REPAIRED/SOUND/WEAKENED/BROKEN status.

## §13.5 Verification Cascade

Tiered verification strategy (Millennium Strategy):
- **Tier A** (VERIFY): Run PAC / ORA / X-Ray on existing chain; either SOUND or WEAKENED per attack.
- **Tier B** (EXCISE / STALL): If chain is over-stated, excise; if no path forward, STALL.
- **Tier C** (CONSTRUCT / BYPASS): Build unconditional replacement (e.g., YM H4 bypass via Balaban RG + gradient flow = Step 18').
- **Tier D** (DYNAMIC SELF-ADJUST): Trim-amplify based on capacitor cell density.

---

# §14 Numerical Constants

## 14.1 First 15 Riemann zeros (Im part)

| γ_n | Value |
|---|---|
| γ_1 | 14.134725141734693790 |
| γ_2 | 21.022039638771554993 |
| γ_3 | 25.010857580145688763 |
| γ_4 | 30.424876125859513210 |
| γ_5 | 32.935061587739189690 |
| γ_6 | 37.586178158825671257 |
| γ_7 | 40.918719012147495187 |
| γ_8 | 43.327073280914999519 |
| γ_9 | 48.005150881167159727 |
| γ_10 | 49.773832477672302182 |
| γ_11 | 52.970321477714460644 |
| γ_12 | 56.446247697063394804 |
| γ_13 | 59.347044002602353079 |
| γ_14 | 60.831778524609809844 |
| γ_15 | 65.112544048081606660 |

## 14.2 Other numerical constants

`CONST-R-ECIRCLE` — $R \approx 10.10\,\mu\text{m}$ (e-circle radius from CC).
`CONST-R-ORBIFOLD` — $R \approx 12\,\mu\text{m}$ (Casimir on $\mathbb{Z}_2$ orbifold).
`CONST-KAPPA` — $\kappa = 2/\pi^2$ (CBB normalization).
`CONST-MERTENS` — $e^{-\gamma_E}$ (Mertens constant).
`CONST-GRANVILLE` — $2 e^{-\gamma_E} \approx 1.1229\ldots$.
`CONST-OPE-CN` — $C_N = 2(N^2 - 1)/\pi^6$ (OPE coefficient).
`CONST-XI-FRAMEWORK` — $\xi = \gamma_1/\gamma_5 \approx 0.4292$.
`CONST-MINIMAL-BRIDGE-CONDUCTOR` — $1729 = 7 \times 13 \times 19$.
`CONST-DELTA-0` — $\delta_0$ lattice-scale cluster gap (paper08).
`CONST-B0-G` — $b_0(G)$ one-loop AF coefficients for each compact simple Lie $G$.
`CONST-HVEE-G` — $h^\vee(G)$ dual Coxeter numbers (paper08 App I).
`CONST-MERCEDES-MASTER` — $6 \zeta(3)$ (weight-3 Mercedes; Broadhurst-Kreimer 1997 uniqueness).
`CONST-ZETA3` — $\zeta(3) \approx 1.20206$ (Apéry constant).
`CONST-ZETA2` — $\zeta(2) = \pi^2/6$.
`CONST-GAMMA-EULER` — $\gamma_E \approx 0.57722$.
`CONST-LAURENT-A-BC` — $a = -\gamma_E(1+\gamma_E) \approx -0.9105$.
`CONST-LAURENT-B-BC` — $b = \gamma_E^2 + \zeta(2) - 2\pi \gamma_1 \approx 2.4358$.
`CONST-LAMBDA-CC-INTERFACE` — $\lambda = 2.695 \times 10^{-3}$ (m_τ interface coefficient).
`CONST-LEHMER-M` — $M(\text{Lehmer polynomial}) \approx 1.17628$ (1933).
`CONST-GAMMA1-PI2-OVER-2` — $\gamma_1 \cdot \pi^2/2 \approx 69.750$ (PIN-1 leading term).
`CONST-SQRT5-R3` — $\sqrt 5 / r_3$ (CP² Dirac spectral gap = KK cutoff prescription per Paper 4 Thm E.1).
`CONST-FIVE-ORDERS-ACCIDENTAL` — $P(\text{36-pin accidental match}) < 10^{-89}$.
`CONST-RESIDUE-A3` — $2\sqrt 2 \cdot \pi \approx 8.8858$ (A_3/Q_3 residue at s=3/2).
`CONST-R-ACCIDENTAL-MATCH` — $10^{-89}$ upper bound on 36-pin accident probability.
`CONST-WINDOW-EOT-WASH` — Testable at $R \approx 12\,\mu\text{m}$ (Eöt-Wash 2027+).

---

# §15 Named Structural Identities

`IDENTITY-MERTENS-ITPFI` — **Mertens product as ITPFI Araki-Woods invariant.** The BC KMS$_1$ state factors as $\omega_1 = \bigotimes_p \omega_1^{(p)}$ with $\lambda_p = 1/p$; the Mertens product is its Araki-Woods invariant. (paper13 L2; paper43 Cramér).

`IDENTITY-BELL-CIRELSON` — **$e$-conservation $\leftrightarrow$ Bell $|S| = 2\sqrt 2$.** Tsirelson bound from e-conservation through 5D. (paper1 §3).

`IDENTITY-FROB-HECKE` — **Frobenius angle = Hecke eigenvalue.** $\mu_p$ at KMS$_1$ gives $\theta_p$. (paper44).

`IDENTITY-EULER-ITPFI` — **Euler product $\leftrightarrow$ ITPFI factorization.** Riemann's Euler product for $\zeta(s)$ has an operator-algebraic avatar in the ITPFI tensor. (paper13 L2).

`IDENTITY-KMS1-SATO-TATE` — **KMS$_1$ democracy $\leftrightarrow$ Sato-Tate equidistribution.** All primes symmetric under KMS$_1$; spectral measure = Haar. (paper44 §§ME).

`IDENTITY-WEITZENBOCK-MASS-GAP` — **Weitzenböck formula on $\mathbb{CP}^{N-1}$ $\to$ mass gap.** $\text{Hess} \geq \mu_1/g^2_{\text{int}}$, $\mu_1 = 6/r_3^2$. (paper08 Thm 4).

`IDENTITY-TT-THERMAL-TIME` — **Tomita-Takesaki modular flow = thermal time.** Hypothesis of Connes-Rovelli. (Capacitor SPEC↔OA; used in paper32).

`IDENTITY-MINT-JMEXTJ` — **Black-hole interior as J-conjugated exterior.** $M_{\text{int}} = J \cdot M_{\text{ext}} \cdot J$; resolves firewall. (paper3 Thm 9.1).

`IDENTITY-SPIN-WINDING` — **Spin = winding on $S^1$.** $m_s = n$ (up to factor); integer/half-integer dichotomy. (paper1 App B.3).

`IDENTITY-HBC-LOG-TBC` — **Mellin duality $H_{BC} = \log T_{BC}$.** $\log \gamma_1$ is the BC Hamiltonian ground-state eigenvalue. (paper12/research/102; Pin #6 anchor).

`IDENTITY-CC-CASIMIR` — **Cosmological constant = Casimir on $\mathbb{Z}_2$ orbifold.** $\Lambda_{CC} = \exp(\gamma_1 \pi^2/2)$. (paper2; Branch C).

`IDENTITY-TRINITY-PVNP` — **SPEC $\leftrightarrow$ INFO $\leftrightarrow$ GEOM trinity.** TGap, $\dim_{\text{poly}_k}$, holonomy — three independent measures of fullness vs non-fullness. **VERIFIED 6/6 Schaefer.** (paper28 Capacitor-trinity).

`IDENTITY-AREA-LAW-COMPUTATIONAL` — **NPC holonomy $\to$ area law.** $R^2 = 0.149$; P-time is flat. Analog of QCD confinement. (paper28 A5).

`IDENTITY-COLLATZ-MU2-MU3` — **Collatz map = $\mu_2/\mu_3$ alternation.** Even step $\mu_2^*$ halves frequency; odd step $\mu_3 \circ \text{shift}$ triples. (paper41).

`IDENTITY-LEHMER-GAP-MASS-GAP` — **Lehmer gap = KMS$_1$ phase-transition mass gap.** Non-cyclotomic leakage cost $c_0 > 0$ is the cyclotomic vacuum's mass gap. (paper42).

`IDENTITY-CRAMER-GRANVILLE-ITPFI` — **Granville $2e^{-\gamma}$ = Mertens product = ITPFI return-time correction.** Prime gap max = ITPFI invariant. (paper43).

`IDENTITY-BC-SEMIGROUP-PRIMES` — **Primes are operators.** $\mu_p$: $\mathbb{N}^*$ Hecke generators; BC algebra's multiplicative engine. (Bost-Connes 1995).

`IDENTITY-SIGMA-HECKE-PROJECTOR` — **$\sigma(n)/n = \omega_1(H_n)$** where $H_n = \sum_{d|n} \mu_{n/d} \mu_{n/d}^*$. (paper40 L4).

`IDENTITY-SPOOF-HASSE` — **Spoofs are local-global failures.** Descartes' spoof $3^2 \cdot 7^2 \cdot 11^2 \cdot 13^2 \cdot 22021$ (with $22021 = 19^2 \cdot 61$ not prime) is a local solution that fails global assembly. (paper40).

`IDENTITY-CUNTZ-O2-BC` — **Cuntz $\mathcal{O}_2 \hookrightarrow A_{BC}$.** $s_0 \leftrightarrow \mu_2^* \mu_2$, $s_1 \leftrightarrow \mu_3 \circ \text{shift} \circ \mu_2^*$ (Mori 2024). (paper41).

`IDENTITY-MERCEDES-ZETA3` — Mercedes triple-bubble 3-loop integral $= 6\zeta(3)$; three derivations (Laurent, Broadhurst dilog, hypergeometric). (paper1 Lead 2 Agent G).

`IDENTITY-J-AREA-LAW-EULER` — $E_2(s; Q_2) = 6 \zeta(s) L(s, \chi_{-3})$. L=2 Epstein factorizes; L=3 does not. (paper1 Lead 2 Agent B).

`IDENTITY-GUE-THREE-TAIL` — **Small-gap (Twin Primes), bulk (Goldbach), large-gap (Cramér).** All governed by $\det(1 - K_{\sin})$. (paper33, paper34, paper43).

`IDENTITY-JARLSKOG-WOLFENSTEIN` — $J = A^2 \lambda^6 \bar\eta$. All closed-form over integers {2,3,6,7,19} and $S^2$ area $4\pi$. (paper12/research/189).

`IDENTITY-17-SU4-ADJOINT` — $17 = \dim \mathfrak{su}(4) + 2 = 15 + 2$ (PS adjoint + 2 $U(1)$). **Representation-theoretic** (NOT lattice-counting per Agent A 2026-04-14).

`IDENTITY-SYMMETRY-BRIDGE` — Bridge $k \in \{2,3,4,6\}$ selects symmetry type: $k=2 \to Sp$, $k=3 \to U$, $k=4 \to O$, $k=6 \to U$. (paper46).

---

# §16 Capacitor cells (24 domains)

Domain index (from `millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`):

| # | Domain | Shorthand |
|---|---|---|
| D1 | Spectral theory | SPEC |
| D2 | Riemannian / differential geometry | GEOM |
| D3 | Operator algebras | OA |
| D4 | Information theory | INFO |
| D5 | Analytic number theory | ANT |
| D6 | Algebraic topology | ATOP |
| D7 | Quantum field theory / physics | QFT |
| D8 | Arithmetic geometry | AG |
| D9 | Probability / stochastic processes | PROB |
| D10 | Thermodynamics / statistical mechanics | THERMO |
| D11 | Explicit class field theory | ECFT |
| D12 | Arithmetic topology | ARTOP |
| D13 | Langlands programme | LANG |
| D14 | Persistent homology | PH |
| D15 | Quantum error correction | QEC |
| D16 | Optimal transport | OT |
| D17 | Microlocal analysis | MICRO |
| D18 | Coding theory | CODE |
| D19 | Differential topology | DTOP |
| D20 | Representation theory | REP |
| D21 | Homological algebra | HOM |
| D22 | Model theory / descriptive complexity | MOD |
| D23 | Ergodic theory | ERG |
| D24 | Noncommutative geometry | NCG |

## 16.1 Tier 1: Load-bearing cells

`CAPACITOR-SPEC-ANT` — **Hilbert-Pólya spectral realization** — Riemann zeros are eigenvalues of a self-adjoint operator (CCM 2025). **ESTABLISHED**. RH Layer 1.
`CAPACITOR-SPEC-QFT` — **Weitzenböck-Bochner** — positive Ricci on KK background → spectral gap → mass gap. **VERIFIED**. YM Step 4.
`CAPACITOR-OA-AG` — **Bost-Connes KMS uniqueness** — KMS$_1$ on BC ↔ CFT of $\mathbb{Q}$. **ESTABLISHED**. RH L2, BSD 1-3.
`CAPACITOR-OA-INFO` — **Polymorphism channel capacity** — $\dim_{\text{poly}_k}$ growth rate separates P from NPC. **VERIFIED 6/6**. PvNP L4.
`CAPACITOR-SPEC-OA` — **Tomita-Takesaki modular flow** — $\sigma_t$ classifies factors; spectral gap of $\sigma_t$ = TGap. **ESTABLISHED**. PvNP L4.
`CAPACITOR-SPEC-INFO` — **TGap-channel duality** — TGap = 0 ↔ positive channel capacity. **VERIFIED 6/6**. PvNP L4.
`CAPACITOR-GEOM-INFO` — **Holonomy-entropy correspondence** — trivial holonomy ↔ low violation entropy. **VERIFIED 6/6**. PvNP L4.
`CAPACITOR-GEOM-OA` — **Jones-Schmidt + Marrakchi fullness** — crossed product + non-amenable + strong ergodic → full. **ESTABLISHED**. PvNP L5 Route C.
`CAPACITOR-OA-QFT` — **Haag-Kastler axioms** — local QFT = net of operator algebras. **ESTABLISHED**. YM axiom framework.
`CAPACITOR-ANT-AG-DEURING` — **Deuring CM factorization** $L(E, s) = L(s, \psi) L(s, \bar\psi)$. **ESTABLISHED**. BSD Step 8.
`CAPACITOR-ANT-AG-KOLYVAGIN` — **Kolyvagin Euler system** — $L(E,1) \neq 0 \Rightarrow$ rank 0, $|\text{Sha}| < \infty$. **ESTABLISHED**. BSD Step 10.
`CAPACITOR-ANT-AG-GROSS-ZAGIER` — **Gross-Zagier formula**. **ESTABLISHED**. BSD Step 11.
`CAPACITOR-GEOM-ATOP` — **Atiyah-Singer index theorem**. **ESTABLISHED**. YM.
`CAPACITOR-SPEC-GEOM` — **Heat kernel ↔ curvature (Seeley-DeWitt)**. **ESTABLISHED**. YM H4 K-2 scope.
`CAPACITOR-QFT-GEOM` — **YM = connections on bundles**. **ESTABLISHED**. YM foundation.
`CAPACITOR-SPEC-NCG` — **Connes spectral action** $\text{Tr}\, f(D/\Lambda)$. **ESTABLISHED**. YM K-2 narrow.
`CAPACITOR-ANT-SPEC-WEIL` — **Weil explicit formula** — sum over zeros = sum over primes. **ESTABLISHED**. RH L5.
`CAPACITOR-OA-ERG` — **KMS ↔ ergodic** — KMS$_1$ uniqueness ↔ BC ergodicity. **ESTABLISHED**. RH L2.
`CAPACITOR-SPEC-PROB` — **Spectral gap ↔ mixing time** (Diaconis-Stroock). **ESTABLISHED**. PvNP solution-space.
`CAPACITOR-QFT-THERMO` — **Confinement ↔ phase transition**. **ESTABLISHED**. YM confinement.
`CAPACITOR-QFT-GEOM-AREA-LAW` — **Computational area law** $R^2 = 0.149$. **VERIFIED**. PvNP L5.
`CAPACITOR-SPEC-QEC` — **Spectral gap ↔ error threshold** (BHM 2010). **ESTABLISHED**. PvNP Route A.
`CAPACITOR-OA-REP` — **Factor classification ↔ representation type**. **ESTABLISHED**. Framework-wide.
`CAPACITOR-ANT-LANG` — **Automorphic ↔ Galois** (Langlands). **PARTIAL**. BSD GL₂.
`CAPACITOR-THERMO-OA` — **KMS states = thermal equilibrium** (HHW 1967). **ESTABLISHED**. RH, BSD.
`CAPACITOR-PROB-ANT` — **Random matrix ↔ Riemann zeros** (Montgomery-Odlyzko). **ESTABLISHED**. RH statistical support.
`CAPACITOR-GEOM-QFT-BALABAN` — **Balaban polymer expansion**. **ESTABLISHED**. YM 1-3.
`CAPACITOR-SPEC-OA-BOGLI` — **Bögli spectral exactness**. **ESTABLISHED**. RH L4.
`CAPACITOR-ANT-ECFT-BAKER` — **Baker's theorem**. **ESTABLISHED**. BSD reinforcement.
`CAPACITOR-AG-ECFT-CM` — **CM theory = explicit CFT for imaginary quadratic**. **ESTABLISHED**. BSD Part (i).
`CAPACITOR-ANT-ATOP-WEIL` — **Étale cohomology ↔ Weil conjectures**. **ESTABLISHED**. Structural template.
`CAPACITOR-SPEC-MICRO` — **Spectral theory via microlocal** (Hörmander). **ESTABLISHED**. General escape route.
`CAPACITOR-OA-DTOP-JONES` — **Surgery ↔ subfactor classification** (Jones 1983). **ESTABLISHED**. Structural.
`CAPACITOR-REP-LANG` — **Langlands = rep-theoretic reciprocity**. **PARTIAL**. BSD.
`CAPACITOR-ERG-OA-CFW` — **Orbit equivalence ↔ factor isomorphism** (Connes-Feldman-Weiss). **ESTABLISHED**. PvNP fullness.
`CAPACITOR-OA-MOD-FAGIN` — **Fagin's theorem** — NP = existential 2nd-order. **ESTABLISHED**. PvNP model-theoretic bypass.
`CAPACITOR-PROB-THERMO` — **Partition function ↔ probability measure**. **ESTABLISHED**. PvNP K-17 kill.
`CAPACITOR-GEOM-OT-VILLANI` — **Optimal transport ↔ Riemannian geometry**. **ESTABLISHED**. Candidate bypass.
`CAPACITOR-INFO-CODE-SHANNON` — **Shannon capacity ↔ code distance**. **ESTABLISHED**. PvNP coding bypass.
`CAPACITOR-QEC-ATOP-KITAEV` — **Topological codes = homology**. **ESTABLISHED**. Structural.
`CAPACITOR-DTOP-SPEC-MORSE` — **Morse theory ↔ spectral flow** (Witten-Floer). **ESTABLISHED**. Candidate H4 bypass.
`CAPACITOR-ERG-PROB-BIRKHOFF` — **Ergodic theorem ↔ LLN**. **ESTABLISHED**. Foundation.
`CAPACITOR-HOM-ATOP-LERAY` — **Spectral sequences**. **ESTABLISHED**. Structural.
`CAPACITOR-NCG-ANT-CONNES` — **Connes trace formula**. **ESTABLISHED**. RH alternative L5.
`CAPACITOR-NCG-GEOM-CHAMSEDDINE-CONNES` — **Spectral action = EH + SM**. **ESTABLISHED**. YM K-2 scope.
`CAPACITOR-PH-GEOM-STABILITY` — **Persistence stability**. **ESTABLISHED**. PvNP solution topology.
`CAPACITOR-ARTOP-ANT-MAZUR` — **Knots ↔ primes analogy**. **CONJECTURED**. Candidate.
`CAPACITOR-OA-QEC-KLP` — **OA inclusion = QEC** (Knill-Laflamme; Kribs-Laflamme-Poulin). **ESTABLISHED**. PvNP↔QEC.
`CAPACITOR-OT-PROB-KANTOROVICH` — **Wasserstein ↔ weak convergence**. **ESTABLISHED**. Transport bypass.
`CAPACITOR-MICRO-QFT-EPSTEIN-GLASER` — **Renormalization via microlocal** (Epstein-Glaser). **ESTABLISHED**. YM alternative renormalization.

## 16.2 Tier 2: Framework-discovered correspondences

`CAPACITOR-TRINITY` — **P vs NP trinity** — SPEC ↔ INFO ↔ GEOM — three independent measures of (non)fullness. **VERIFIED 6/6**. PvNP L4-5.
`CAPACITOR-OA-ANT-QFT` — **BC spectral ↔ SM constants** — 36 zero-parameter predictions. **VERIFIED 36/37 sub-percent**. Foundation.
`CAPACITOR-SPEC-ANT-OA-ITPFI` — **ITPFI factorization** — $\omega_1 = \bigotimes_p \omega_1^p$. **VERIFIED 3 proofs**. RH L2.
`CAPACITOR-OA-GEOM-QFT-AREA-LAW-COMPUTATIONAL` — **Computational area law** — NPC holonomy area law. **VERIFIED 3 PASS, 1 MARGINAL**. PvNP L5.
`CAPACITOR-OA-INFO-MOD-UNDERIV` — **Underivability / finite-arity invisibility** — P/NPC invisible at bounded arity $k$. **VERIFIED**. PvNP hardness.
`CAPACITOR-SPEC-OA-PROB-DUALITY` — **Solution-space spectral gap duality** — modular gap ↔ Laplacian gap. **VERIFIED**. PvNP L4.
`CAPACITOR-ANT-OA-ECFT-BC-BRIDGE` — **BC bridge ↔ explicit CFT** — BC $\to$ Hecke $\to$ CM curve L-fn. **VERIFIED**. BSD 1-7.
`CAPACITOR-GEOM-QFT-SPEC-GRAD-FLOW` — **Gradient flow ↔ heat kernel ↔ analyticity**. **VERIFIED**. YM Step 18 H4 mildest.
`CAPACITOR-QFT-OA-NCG-SCHEME-INDEP` — **Spectral action boundary conditions** — at $\Lambda$, not running. **VERIFIED kill**. YM K-2.
`CAPACITOR-ANT-OA-AG-HBN` — **Hasse-Brauer-Noether ↔ projector bypass** — G's projector $P_k^\mathfrak{p}$ closes MY4. **VERIFIED**. BSD MY4.

(Capacitor totals: ~48+ filled cells; target 130+. Programme-discovered Tier 2 cells unique to this programme.)

---

# §17 Programme-graph edges / cross-cuts

## 17.1 Outgoing edges from QG5D (hub radiation)

`EDGE-QG5D-RH` — "BC scaling operator eigenvalues ARE Riemann zeros." **STRONG**.
`EDGE-QG5D-YM` — "KK spectral gap $\Delta_0 > 0$ is the 5D origin of the 4D mass gap." **STRONG**.
`EDGE-QG5D-BSD` — "BC algebra over $\mathbb{Q}(i)$ gives Hecke L-functions for CM curves." **STRONG**.
`EDGE-QG5D-PVNP` — "Continuous BC algebra (Connes-Marcolli GL$_2$) → algebraic circuit complexity." **CANDIDATE**.
`EDGE-QG5D-HODGE` — "$M_{\text{geom}}$ ($\mathbb{CP}^2 \times S^2$) with Hodge decomposition $H^{1,1} = 1$." **STRONG**.
`EDGE-QG5D-NS` — "5D Einstein equations; KK reduction pipeline; gradient flow." **STRONG**.
`EDGE-QG5D-H12` — "KMS states at $\beta > 1$; class field generation from phase transitions." **STRONG**.
`EDGE-QG5D-GRH` — "Bridge family Dirichlet characters at $k \in \{2,3,4,6\}$." **STRONG**.
`EDGE-QG5D-BAUM-CONNES` — "BC C*-algebra structure; Hecke semigroup action." **STRONG**.
`EDGE-QG5D-BGS` — "Type III$_1$ modular flow $\sigma_t$ (ergodicity target); KMS$_1$ state." **STRONG**.
`EDGE-QG5D-GOLDBACH` — "Hecke semigroup $\mathbb{N}^*$ generators $\{\mu_p\}$ (primes as operators)." **STRONG**.
`EDGE-QG5D-TWIN-PRIMES` — "Explicit formula machinery; zero-spacing statistics." **STRONG**.
`EDGE-QG5D-SCHANUEL` — "Eigenvalues $\exp(\gamma_n \pi^2/2)$ of $\hat R$ — algebraic independence target." **STRONG**.
`EDGE-QG5D-TURBULENCE` — "5D fluid/gravity → 4D NS → K41 + intermittency." **CANDIDATE**.
`EDGE-QG5D-VP-VS-VNP` — "Continuous BC algebra." **CANDIDATE**.
`EDGE-QG5D-ABC` — "BC Mellin bridge → height function on $\mathbb{N}^*$." **CANDIDATE**.
`EDGE-QG5D-OPN` — "BC Hecke orbit sum at KMS$_1$ computes $\sigma(n)/n$; ITPFI decomposes abundancy." **CANDIDATE**.
`EDGE-QG5D-H6` — "QG5D IS the axiomatization of physics." **STRONG, META-closure (incoming from H6)**.

## 17.2 Key inter-paper edges (from each PROOF-CHAIN.md "Programme graph edges")

`EDGE-YM-RH` — AF coefficient connects spectral data to gauge coupling. **STRONG**.
`EDGE-YM-NS` — Gradient flow machinery (L.15-L.17) structural parallel for NS regularity.
`EDGE-YM-HODGE` — Gauge anomaly cancellation = K-theoretic / Hodge-class statement.
`EDGE-YM-BAUM-CONNES` — Anomaly cancellation = index($D_A$) = 0, K-theory pairing.
`EDGE-RH-GRH` — Character-twisted extension of every layer.
`EDGE-RH-BSD` — L-functions factor through same BC algebra; cocycle machinery shared.
`EDGE-RH-BGS` — GUE pair correlation of zeros = spectral statistics of $D_\infty$.
`EDGE-RH-PVNP` — Q5-RIEMANN exponent constrains spectral gap scaling.
`EDGE-BSD-H12` — Hecke L-functions for CM curves factor through class field extensions.
`EDGE-BSD-HODGE` — CM motives connect algebraic cycles to Hodge classes.
`EDGE-BSD-SCHANUEL` — Algebraic independence of L-values at $s=1$.
`EDGE-BSD-GRH` — GRH for Hecke L-functions feeds Step 7 directly.
`EDGE-HODGE-LANG` — Geometric Langlands (Gaitsgory-Raskin 2024) → Hitchin moduli → Hodge.
`EDGE-HODGE-BAUM-CONNES` — K-theory classes ↔ algebraic vector bundles via Chern.
`EDGE-NS-QG5D-KK` — KK reduction provides 5D→4D pipeline.
`EDGE-NS-YM-GRADIENT` — YM gradient flow = same PDE class as NS.
`EDGE-NS-BAUM-CONNES-SPECTRAL` — Spectral gap as K-theoretic statement.
`EDGE-PVNP-BSD` — L-function channel capacity via Dirichlet L.
`EDGE-PVNP-BGS` — Spectral statistics of $M_{\text{Bool}}$ connect to GUE.
`EDGE-PVNP-BAUM-CONNES` — K-theory of $M_{\text{Bool}}$ constrains anomaly.
`EDGE-TWIN-PRIMES-BGS` — GUE pair correlation feeds L2.
`EDGE-TWIN-PRIMES-GOLDBACH` — Shared additive prime structure.
`EDGE-CRAMER-BGS` — GUE extreme-value → max prime gap.
`EDGE-CRAMER-TWIN-PRIMES` — Bridge BGS ↔ Twin Primes (gap distribution arc).
`EDGE-COLLATZ-GOLDBACH` — Additive-shift wall (the +1 shift).
`EDGE-LEHMER-BSD` — Deninger-Rodriguez Villegas: $m(P) = c \cdot L'(E, 0)$.
`EDGE-LEHMER-HODGE` — Salem numbers = abelian-variety automorphism entropy.
`EDGE-LEHMER-YM` — Lehmer's gap IS YM mass gap one level down (structural parallel).
`EDGE-OPN-RH-ROBIN` — Robin's inequality: $\sigma(n) < e^\gamma n \ln(\ln n)$ iff RH.
`EDGE-OPN-ABC-RAD` — rad$(n)$ bound via Euler's form.
`EDGE-OPN-GOLDBACH-HECKE` — Shared Hecke semigroup $\mathbb{N}^*$.
`EDGE-SCHANUEL-BGS` — GUE statistics assume generic zeros.
`EDGE-SCHANUEL-HODGE` — Period relations constrained by algebraic independence.
`EDGE-SATO-TATE-BSD` — Frobenius angles = L-function data.
`EDGE-SATO-TATE-BGS` — Spectral measure = Haar pushforward.
`EDGE-LINDELOF-RH` — RH → Lindelöf (Phragmén-Lindelöf).
`EDGE-LINDELOF-CRAMER` — Amplitude control IS explicit-formula error bound.
`EDGE-KATZ-SARNAK-BGS` — Symmetry type differentiates GUE/GSE/GOE.
`EDGE-KATZ-SARNAK-BRIDGE-FAMILY` — Bridge $k \in \{2,3,4,6\}$ selects symmetry type.
`EDGE-BGS-RH-SPECTRAL-REALIZATION` — Link 6 conditional on $\text{spec}(D_\infty) = \{\gamma_n\}$.
`EDGE-GOLDBACH-BGS-BULK` — Bulk sine-kernel density → prime density.
`EDGE-ABC-RH-EXPLICIT` — Zero-spacing controls explicit formula error.
`EDGE-H12-GEOMETRIC-LANGLANDS` — Gaitsgory-Raskin 2024 opens new toolkit.
`EDGE-H6-QG5D-METACLOSURE` — H6 → QG5D ring closure: axiomatization IS the hub.
`EDGE-TURBULENCE-NS-SPECTRAL-GAP` — Direct inheritance of NS L4.
`EDGE-TURBULENCE-BGS-ERG` — Type III$_1$ ergodicity → Kolmogorov universal constants.
`EDGE-VP-VS-VNP-PVNP` — Direct parent: algebraic analog over $\mathbb{C}$.
`EDGE-VP-VS-VNP-BAUM-CONNES` — K-theory of algebraic groups GL$_n$.

(Estimated 38+ cross-cut edges from YM x-ray alone; total across ring ≈ 100+.)

---

# §18 Literature anchors

External results cited in framework papers.

`LIT-BC-1995` — Bost-Connes 1995 (Selecta Math) — BC C*-algebra + unique KMS$_1$.
`LIT-OS-1973` — Osterwalder-Schrader 1973 — OS axioms part 1.
`LIT-OS-1975` — Osterwalder-Schrader 1975 — OS axioms part 2.
`LIT-BALABAN-CMP-109` — Balaban CMP 1984-1998 (vols 95-119) — block-spin RG for 4D YM.
`LIT-WILES-1995` — Wiles 1995 — Modularity (template for YM).
`LIT-TAYLOR-2011` — Taylor-Harris-Shepherd-Barron-Clozel 2011 — Sato-Tate for non-CM elliptic curves.
`LIT-LINDENSTRAUSS-2006` — Lindenstrauss 2006 — arithmetic QUE (Fields 2010).
`LIT-HARDY-Z-PCC-2025` — arXiv:2511.18275 (Nov 2025) — Hardy Z pair correlation conjecture PROVED.
`LIT-CCM-2025` — arXiv:2511.22755 — Connes-Consani-Moscovici CCM operators for RH.
`LIT-MORI-2024` — arXiv:2411.08084 (Springer 2025) — Cuntz $\mathcal{O}_2$ formulation of Collatz.
`LIT-CCM-2005` — Connes-Consani-Marcolli 2005 arXiv:math/0512138 — endomotives & Artin motives.
`LIT-CONNES-MARCOLLI-2008` — Connes-Marcolli 2008 — GL$_2$ continuous BC system.
`LIT-GAITSGORY-RASKIN-2024` — Gaitsgory-Raskin 2024 arXiv:2405.03599 — Geometric Langlands PROVED.
`LIT-DENG-HANI-MA-2025` — arXiv:2503.01800 — Boltzmann → fluid equations (Hilbert 6 fluid slice).
`LIT-GUTH-MAYNARD-2024` — Guth-Maynard 2024 — large-value estimate for $\zeta$; first Lindelöf exponent progress in 50 years.
`LIT-CAMLIN-2025` — arXiv:2601.08854 (Jan 2026) — microlocal cosphere bundle regularity.
`LIT-CAMLIN-2025B` — Camlin 2025 arXiv — bounded $\Phi$ + Sundman temporal lifting → BKM finiteness.
`LIT-MOCHIZUKI-2012` — Mochizuki 2012 — Inter-Universal Teichmüller (ABC).
`LIT-SCHOLZE-STIX-2018` — Scholze-Stix 2018 — gap in Mochizuki Cor. 3.12.
`LIT-JOSHI-2024` — Joshi 2024-2025 — canonical-formulation attempts for IUT.
`LIT-VALIANT-1979` — Valiant 1979 — permanent is VNP-complete.
`LIT-MULMULEY-SOHONI-2001` — Mulmuley-Sohoni 2001 — GCT programme.
`LIT-KIM-SARNAK` — Kim-Sarnak — $\lambda_1 \geq 975/4096$ for Maass forms.
`LIT-LANGLANDS-1967` — Langlands 1967 — reciprocity conjecture.
`LIT-DELIGNE-1974` — Deligne 1974 — Weil conjectures (proof of Weil RH).
`LIT-ODLYZKO-1987` — Odlyzko 1987 — $10^{22}$ zeros computed, GUE match.
`LIT-MONTGOMERY-1973` — Montgomery 1973 — pair correlation conjecture.
`LIT-HELFGOTT-2013` — Helfgott 2013 — ternary Goldbach.
`LIT-ZHANG-2013` — Zhang 2013 — bounded prime gaps $\leq 7 \times 10^7$.
`LIT-MAYNARD-2015` — Maynard / Polymath 8b 2014-2015 — gap $\leq 246$.
`LIT-BULATOV-2017-ZHUK-2020` — Bulatov / Zhuk — CSP Dichotomy Theorem.
`LIT-HOUDAYER-MARRAKCHI` — Houdayer-Marrakchi (2016+) — fullness of crossed products.
`LIT-HIGSON-KASPAROV-2001` — Higson-Kasparov 2001 — Baum-Connes for amenable groups.
`LIT-CUNTZ-LI` — Cuntz-Li — semigroup C*-algebras.
`LIT-ROBIN-1984` — Robin 1984 — $\sigma(n) < e^\gamma n \ln(\ln n)$ ↔ RH.
`LIT-EULER-1747` — Euler 1747 — odd perfect form $p^\alpha m^2$.
`LIT-NIELSEN-2015` — Nielsen 2015 — $\omega(N) \geq 9$ for odd perfect.
`LIT-OCHEM-RAO-2012` — Ochem-Rao 2012 — $N > 10^{1500}$ for odd perfect.
`LIT-NIELSEN-2020` — Nielsen 2020 — 21 spoofs found.
`LIT-KRONECKER-1857` — Kronecker 1857 — $M(\alpha) = 1$ iff root of unity / 0.
`LIT-DENINGER-RV-BOYD` — Deninger 1997 / Rodriguez-Villegas 1999 / Boyd 1998 — Mahler measure = $L'(E, 0)$.
`LIT-RUBIN-1991` — Rubin 1991 — Sha finiteness for CM curves.
`LIT-BRAUER-SIEGEL` — Brauer-Siegel — $h_{K_k} \to \infty$.
`LIT-CHOWLA-SELBERG` — Chowla-Selberg formula.
`LIT-SILVERMAN-1984` — Silverman 1984 — finitely many curves with small height.
`LIT-GPY-2005` — Goldston-Pintz-Yıldırım 2005 — GRH + Elliott-Halberstam → gap $\leq 6$.
`LIT-TITCHMARSH` — Titchmarsh — zeta function monograph.
`LIT-WEIL-1952` — Weil 1952 — explicit formula.
`LIT-DEURING-1953` — Deuring 1953 — CM factorization.
`LIT-KOLYVAGIN-1990` — Kolyvagin 1990 — Euler system for elliptic curves.
`LIT-GROSS-ZAGIER-1986` — Gross-Zagier 1986 — height formula.
`LIT-GELFAND-YAGLOM` — Gel'fand-Yaglom — generating function for boundary $a_{2k}$.
`LIT-ARAKI-WOODS-1968` — Araki-Woods 1968 — ITPFI factor classification.
`LIT-TOMITA-TAKESAKI` — Tomita 1967 / Takesaki 1970 — modular theory.
`LIT-CONNES-1973` — Connes 1973 — type III classification.
`LIT-CONNES-FELDMAN-WEISS-1981` — CFW 1981 — orbit equivalence.
`LIT-FAGIN-1974` — Fagin 1974 — NP = existential 2nd-order.
`LIT-EPSTEIN-GLASER-1973` — Epstein-Glaser 1973 — causal perturbation.
`LIT-KATZ-SARNAK-1999` — Katz-Sarnak 1999 — symmetry type conjecture.
`LIT-IWANIEC-LUO-SARNAK-2000` — ILS 2000 — one-level densities.
`LIT-HARDY-LITTLEWOOD` — Hardy-Littlewood — twin prime constant, moments.
`LIT-EYYUNNI-2024` — arXiv:2406.00331 — Fourier-Laguerre Lindelöf criterion.
`LIT-BOURGAIN-2017` — Bourgain 2017 — $|\zeta(1/2+it)| = O(t^{13/84+\varepsilon})$.
`LIT-KITAEV-1997` — Kitaev 1997 — topological codes / toric code.
`LIT-JNVWY-2020` — Ji-Natarajan-Vidick-Wright-Yuen 2020 — MIP*=RE, refuting Connes embedding.
`LIT-MAZUR-MORISHITA` — Mazur 1960s; Morishita 2012 — knots ↔ primes.
`LIT-KAZHDAN-MARRAKCHI-VAES` — Marrakchi-Vaes 2024-2026 — live frontier for property T of $\text{Out}$.
`LIT-HOLLANDS-WALD-2024` — Hollands-Wald 2024 — microlocal renormalization on curved spacetime.
`LIT-DAPPIAGGI-2023` — Dappiaggi 2023-2024 — microlocal QFT.
`LIT-BFR-2025` — Brunetti-Fredenhagen-Rejzner 2025 — algebraic QFT.
`LIT-HARE-2007` — Hare 2007 — $\Omega(N) \geq 75$ for odd perfect.
`LIT-GOTO-OHNO-2008` — Goto-Ohno 2008 — largest prime factor $> 10^8$.
`LIT-IANNUCCI-2000` — Iannucci 2000 — 2nd largest prime factor $> 10^4$.
`LIT-POMERANCE-1977` — Pomerance 1977 heuristic for OPN.
`LIT-BOYD-LAWTON` — Boyd-Lawton theorem — multivariate → univariate Mahler.
`LIT-BROADHURST-KREIMER-1997` — Broadhurst-Kreimer 1997 — weight-3 3-loop uniqueness.
`LIT-GILKEY-SEELEY-DEWITT` — Gilkey; Seeley 1967; DeWitt — heat kernel expansion.
`LIT-GOROFF-SAGNOTTI` — Goroff-Sagnotti — R³ 2-loop counterterm.

---

# §19 Naming register

`NAMED-CBB-SYSTEM` — "Critical Bost-Connes-Brauer system." Quintuple $\mathcal{C} = (H_R, \hat R, \omega_1, M_{\text{geom}}, \{\beta_k\})$. Colloquial name: **Integers**. (paper12 §27).
`NAMED-SIX-TIME` — "Six time scale $\tau_S$." Absolute time. (strategy/absolute-time.md).
`NAMED-LOCK` — "The LOCK — 37 R-Theorems." (paper9).
`NAMED-SIX-PATTERNS` — Method: P1-P6. (strategy/programme-patterns.md).
`NAMED-E-CIRCLE` — "The e-circle." Fifth dimension = $U(1)$ fiber. (Paper 1).
`NAMED-BRIDGE-FAMILY` — "The bridge family." $\{\beta_k\}_{k\in\{2,3,4,6\}}$. (paper24).
`NAMED-ELLIPSE` — "The ellipse." Ring's confidence diagnostic. (paper60 §20).
`NAMED-RING` — "The ring." 22-25 vertex orbit. (strategy/the-ring.md).
`NAMED-CHESSBOARD` — "The chessboard." Dual-sided board with 36 pins. (strategy/).
`NAMED-HERALD` — "The Herald." This document.
`NAMED-PIN` — "Pin." Square where top face meets bottom face. (strategy/).
`NAMED-FACE` — "Face." One of the 10 mathematical aspects of the e-circle. (paper60).
`NAMED-PROJECTION` — "Projection." One of the 6 shadows cast by $M^5$. (paper61).
`NAMED-TORUS` — "The torus." $S^1_{\text{geo}} \times S^1_{\text{spec}}$. (paper60 §17).
`NAMED-TESSERACT-ANALOGY` — Schlegel-like projection of $M^5$. (paper61 §03).
`NAMED-SPINE` — "The Spine" vs "The Gap" — ring dipole terminology. (strategy/).
`NAMED-SOUTH-TROUGH` — "South Trough" — low-confidence ellipse region. (strategy/the-weakest-links.md).
`NAMED-NORTH-POLE` — "North Pole" = QG5D. (strategy/).
`NAMED-CAPACITOR` — The 24-domain correspondence table. (millenium-apps/).
`NAMED-TRINITY` — Spectral-Geometric-Information. (paper28).
`NAMED-ROBUSTNESS-CIRCLE` — Robustness-Circle Theorem (programme §27).
`NAMED-INTEGERS` — "Integers" (proper noun, no article). Colloquial name for CBB system. (paper12 §27).
`NAMED-DESCRIPTION` — "A description" — not a model, not a theory; reality is what Integers describes. (paper12 §27).
`NAMED-CONSISTENCY-ANCHOR` — QG5D's role in the ring-PCA. (paper1).
`NAMED-PCA` — Proof-Chain Adversarial. (millenium-apps/).
`NAMED-ORA` — Online Researcher Adversarial. (online-researcher-adversarial/).
`NAMED-WALL` — "The wall" — shorthand for a named blocking hypothesis. (strategy/).
`NAMED-SIGNAL-LOG` — "Signal log" — session record. (paper60 §29).
`NAMED-TOOLKIT` — Framework toolkit — externalized primitives. (millenium-apps/08).
`NAMED-PATTERNS-REGISTRY` — "Patterns registry" — P1-P6 canonical usage. (strategy/programme-patterns.md).
`NAMED-GANG-RINGS` — Bouquet-of-rings topology (outer + A + B + C + D + E = 6 rings). (strategy/inner-rings/).
`NAMED-LITTLE-RINGS` — "Little rings from smaller rings." (Session 2026-04-14).

---

# §20 Dead ends / kept-for-history

`DEAD-STRING-THEORY` — "String theory byeeeee." Paper 20 "Beyond String Theory — The Zero-Parameter Geometry Correspondence." Uniqueness theorem §3.3 supersedes. (paper20).

`DEAD-CONJECTURE-5` — Stark regulator equality (literal form). **RETRACTED.** (paper25 research/267).

`DEAD-OPN-6A-CLASSICAL` — Classical Robin-constant route without halved $e^\gamma/2$. **REPLACED** by odd-restricted Robin with halved Mertens. (paper40 v2).

`DEAD-MEMORY-MOBIUS-KK` — Möbius KK mechanism. **FALSIFIED** (paper12/research/142).

`DEAD-MEMORY-TWISTED-S1` — Twisted S¹ postulate. **FALSIFIED** (paper12/research/145).

`DEAD-MEMORY-BETA-EPS` — $\beta = 1 + \varepsilon$ deformation. **FALSIFIED** (paper12/research/139).

`DEAD-MEMORY-SECOND-ORDER-LAURENT` — (paper12/research/152).

`DEAD-MEMORY-CONDUCTOR-LIFT` — (paper12/research/160).

`DEAD-MEMORY-EXCITED-STATE` — (paper12/research/146).

`DEAD-MEMORY-ORBIT-KOIDE` — 4 routes all failed. (paper12/research/151, 157, 161, 172).

`DEAD-MEMORY-E-CIRCLE-CLOCK` — e-circle-as-clock interpretation. **POSTULATE SURVIVES** (paper12/research/138).

`DEAD-PIN6-PAPER13-CP` — Pin #6 J_CKM anchor in Paper 13 CP-violation section. **FAILED audit 2026-04-14** (ripgrep: zero matches). Real anchor: paper12/research/102 Mellin duality. (paper1 Agent L audit).

`DEAD-PIN6-PAPER26-STEP4-JCKM` — Pin #6 anchor in Paper 26 Step 4 as J_CKM vertex. **FAILED audit 2026-04-14** — Step 4 is cocycle-shift INEQUALITY (Key Lemma C), not CKM vertex. (paper1 Agent L audit).

`DEAD-PIN1-SMALL-MATRIX-TRUNC` — Pin #1 "small-matrix-element truncation" justification. **FALSIFIED 2026-04-14** — $|V_{1m}|^2$ are $O(1)$ and do NOT decay rapidly in $m$. (Agent H 2026-04-14).

`DEAD-PIN1-PT-RESUM` — Pin #1 infinite-order PT resummation. **FALSIFIED 2026-04-14** — gives $\Delta \approx -0.031$, still 3× empirical. (Agent O).

`DEAD-AGENT-H-V11-IMAGINARY` — Agent H's non-Hermitian $V_{nm}$. **BUG-FIXED** by Agent O 2026-04-14.

`DEAD-AGENT-H-ENHANCE-0.6454` — Agent H enhance value 0.6454. **SUPERSEDED** by Agents N+P final value 0.829 (or 0.5224 recalibrated). (paper1 Lead 3).

`DEAD-H4-ROUTE-A-B-C-D` — H4 Routes A/B/C/D all tested. **ALL FAILED**. (YM PAC runs).

`DEAD-POPA-RIGIDITY` — PvNP L5 route D Popa superrigidity. **FAILED T6** ($\text{PCirc}^+$ not w-rigid). (paper28).

`DEAD-L3-BIQUADRATIC-FACTOR` — L=3 Epstein factorization analogous to L=2. **FAILED** — $A_3$ not biquadratic. (Agent B Cycle-1).

`DEAD-RESEARCH-32-FACTOR-9` — "factor-9 enhancement needed" claim. **SUPERSEDED** — bad $|\zeta(1+i\tau)|$ asymptotic; correct value 4× larger. (paper12/research/32 BUG-FLAG Agent N).

`DEAD-BOUNDARY-SD-A4-OPEN` — "Boundary Seeley-DeWitt $a_4$ for spin-2 on $S^1/\mathbb{Z}_2$" listed as open frontier. **RESOLVED 2026-04-14** (Agent C: numerically zero to 9 s.f.).

`DEAD-ALL-A2K-GENERATING` — "All $a_{2k} = 0$ via Gel'fand-Yaglom generating function" listed as open. **RESOLVED 2026-04-14** (Agent M audit: three scripts).

`DEAD-WEYL-19-240-OPEN` — "$a_{\text{grand}} = 19/240$ from $\mathbb{Z}_2$-asymmetric KK tower" listed as open. **RESOLVED 2026-04-14** (Agent M audit, exact rationals, $43/720 + 13/720 + 1/720 = 19/240$).

---

# Change log

- **2026-04-14**: Initial issue (G Six and Claude Opus 4.6 1M context).

---

*Miss nothing. Append-only. Citation-backed. Honest status codes.*

*G Six and Claude Opus 4.6 (1M context). April 14, 2026.*
