# Route C3: Framework's Own Spectral Realization

*Author: ORA v8 construction agent. Route: C3 (spectral domain translation).*
*Question: What is the IMAGE of H4 in the spectral domain?*

---

## 1. The translation question

The framework connects YM to the BC system via the correspondence table (Capacitor H.2). In the BC realization, the mass gap is a spectral gap (eigenvalue spacing). What does "short-distance agreement with perturbation theory" BECOME in the spectral picture?

**Kill-list constraint:** K-1 forecloses CCM 2025 port; K-2 forecloses spectral action + Identity 12; K-meta notes RH and H4 require incompatible NCG machinery. This route must find a spectral realization that is NOT any of these.

## 2. Domain translation via the operations equivalence table

From Capacitor H.5, the operations equivalence table:

| Operation | QFT | Spectral |
|-----------|-----|----------|
| Gap | Mass gap | Delta = inf spec \ {0} |
| Derivative | RG beta function | [H, .] |
| Exponential | Transfer matrix | e^{-beta H} |
| Limit | Continuum limit | spec(T_k) -> spec(T_infty) |
| Fixed point | Vacuum state | Eigenvalue-1 state |
| Projection | Block-spin RG | Spectral E_lambda |

The QFT statement of H4 is: "non-perturbative Schwinger functions = perturbative at short distances."

**Translation attempt:** In the spectral domain, "short distances" corresponds to "high eigenvalues" (UV = high energy = large spectral parameter). "Perturbation theory" corresponds to "Taylor expansion of spectral quantities in the coupling." "Non-perturbative = perturbative" becomes "the spectral density at large eigenvalues is determined by its asymptotic expansion."

**Spectral H4:** The spectral density rho(lambda) of the transfer matrix, at large lambda, is determined by its asymptotic expansion to all orders. Equivalently: rho(lambda) is analytic in a suitable sense at lambda = infty.

## 3. The Weyl law connection

The brief asks: if H4 becomes a statement about eigenvalue asymptotics (Weyl law), is it provable from the spectral side?

### 3.1 Weyl's law on compact manifolds

For the Laplacian on a compact d-dimensional Riemannian manifold M, the eigenvalue counting function satisfies:

N(lambda) := #{lambda_j <= lambda} ~ (Vol(M) / (4 pi)^{d/2} Gamma(d/2 + 1)) lambda^{d/2}

This is a universal asymptotic depending only on dimension and volume.

### 3.2 Application to the YM setting

The "manifold" here is the space of gauge field configurations, which is infinite-dimensional. Weyl's law in infinite dimensions is not standard. However, the LATTICE regularization makes the configuration space finite-dimensional (dim = (N^2-1) x |Lambda^1|), and Weyl's law applies to the lattice transfer matrix.

The lattice transfer matrix T acts on L^2(SU(N)^{|Lambda^1_spatial|}). Its spectrum determines the Schwinger functions via:

S_2(x_0) = sum_n |c_n|^2 e^{-E_n |x_0|}

where E_n are the eigenvalues of the Hamiltonian H = -log T.

**The short-distance behavior** x_0 -> 0 corresponds to probing the sum at all energies, dominated by the high-energy tail. The specific |x|^{-8} (log)^{-2} behavior comes from the density of states at high energies, which encodes the asymptotic freedom of the theory.

### 3.3 Does the spectral translation help?

The spectral translation of H4 is: "the density of states rho(E) at high energy E has the form predicted by asymptotic freedom." This is equivalent to H4, not simpler. The spectral side does not provide additional leverage because:

1. The density of states rho(E) at high energy IS the UV physics, which is where H4 lives.
2. The Weyl law for the transfer matrix on the lattice gauge group is a statement about the FINITE-dimensional lattice, not the continuum. The continuum limit (high energy on the lattice) is exactly the regime where H4 is needed.
3. The framework's SM-Riemann correspondence (Keystone File 4) maps SPECIFIC gauge-theory quantities to SPECIFIC spectral quantities, but the mapping is at the level of structural correspondence, not rigorous identification. K-2 established that the spectral action does not produce running couplings.

## 4. Cross-check with framework spectral objects

### 4.1 Identity 12 and the BC system

Identity 12 establishes an e-circle <-> Bost-Connes equivalence at the C*-algebraic level. The BC system has:

- Partition function: zeta(beta) (the Riemann zeta function)
- KMS states at inverse temperature beta
- Phase transition at beta = 1

The mass gap in the BC picture is the spectral gap of the BC Hamiltonian H_BC = log N-hat. But H_BC is a C*-dynamical structure, NOT a spectral-triple structure (this was verified in K-2: zero occurrences of "Dirac operator" in the Identity 12 rigorous file).

The anomalous dimension gamma_{Tr F^2} = -2 beta(g)/g would need to be a spectral quantity of the BC Hamiltonian. But the BC Hamiltonian is fixed (it is log N-hat), while the anomalous dimension is coupling-dependent. There is no coupling in the BC system that runs.

**Kill extension:** The BC spectral realization cannot accommodate a running coupling. The AF match is intrinsically about coupling-dependent quantities. The spectral domain translation via Identity 12 is structurally incompatible with H4.

### 4.2 Can ANY spectral realization help?

For a spectral realization to help bypass H4, it would need:
1. A non-perturbative definition of the spectral density rho(E)
2. An independent (non-H4-dependent) proof that rho(E) has AF asymptotics at large E
3. A rigorous connection between rho(E) and the Schwinger function short-distance behavior

Point (1) exists: the transfer matrix spectrum gives rho(E).
Point (3) is standard: S_2(x) = int dE rho(E) e^{-E|x|}, and short distances probe large E.
Point (2) is the hard part: it IS H4 translated to spectral language.

The spectral translation does not provide additional mathematical leverage. It is a reformulation, not a simplification.

## 5. One genuinely useful observation

The translation attempt reveals something for Route C4:

In the spectral picture, the AF behavior g_k -> 0 (Steps 12-14) corresponds to the spectral gap of the k-th effective transfer matrix growing logarithmically with k. The Balaban RG recursion IS a spectral statement: at each RG step, the low-energy spectrum is preserved while high-energy modes are integrated out, and the coupling (which controls the spectral weight distribution) decreases.

This confirms Route C2/C4's strategy: the AF information is already in the Balaban RG, which is unconditional. The task is to connect it to the continuum Schwinger functions, not to find it in a different spectral domain.

## 6. Verdict

**Route C3: BLOCKED -- translation is a reformulation, not a simplification.**

The spectral domain translation of H4 is "the density of states at high energy has AF asymptotics." This is equivalent to H4, not easier. The framework spectral objects (BC system via Identity 12) are structurally incompatible with the running coupling, confirming K-2.

**New kill:**
- K-C3: BC spectral realization of AF match. The BC Hamiltonian H_BC = log N-hat has no running coupling; the anomalous dimension is coupling-dependent. The spectral domain cannot accommodate AF behavior because AF is about the COUPLING dependence of the spectral density, not the spectral density itself. Pattern: Wrong-space (spectral domain lacks coupling dependence).

**Useful output for other routes:** The spectral translation confirms that the AF information lives in the Balaban RG recursion (Steps 12-14), not in any alternative spectral domain. This supports Route C2's strategy.
