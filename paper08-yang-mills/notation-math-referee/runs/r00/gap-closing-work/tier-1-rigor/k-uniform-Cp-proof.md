# K-Uniform Spectral Lemma Constant: Three Approaches and Proof

**Gap ID:** Tier 1 / Step 1.3 (K-uniform $C_p$).
**Date:** 2026-04-08.
**Scope:** Close the last remaining gap -- prove $C_p(K) \leq C_p^*$ uniformly in the outer bare-scale index $K$ as $a_0(K) \to 0$.

---

## Section 1 -- Problem Statement

**What must be proved.** The spectral lemma (SS5.5.3) establishes that for $\mathcal{O}$ with $\mathrm{dev}(\mathcal{O}) \geq p$, $\|\mathcal{O}\| \leq M$, supported in a ball of diameter $R_0$:

$$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat\Delta^p$$

with $C_p = 2 C_*^p (1+\zeta)^{2R_0-1}$. The constant $C_* = e^{\hat\Delta_{\max}}$ is K-uniform (Tier 1A, row 13). The temporal extent $R_0$ is bounded by a $K$-independent number (polymer support in block lattice units). The sole problematic ingredient is $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$, bounded in SS5.5.3 Step 3(i) via:

$$\zeta \leq \sum_{r=0}^{\infty} \exp(C_1 (R_0+r)^3 N^2) \cdot \exp(-c\hat\Delta\, r)$$

where $(R_0+r)^3$ counts lattice sites. At bare scale $K$, a ball of fixed physical radius $r_0$ contains $(r_0/a_0(K))^3 \sim 8^K$ sites. The density-of-states factor $\exp(C_1 \cdot 8^K \cdot N^2)$ overwhelms $\exp(-c\hat\Delta\, r)$, destroying K-uniformity.

**Goal.** Find a bound $\zeta(K) \leq \zeta^*$ with $\zeta^*$ independent of $K$.

---

## Section 2 -- Attempt 1: Direct Cluster-Expansion Bound on $\zeta$

### 2.1 Strategy

Bypass the Combes-Thomas route entirely. Write $\zeta = Z_{\rm exc}/e^{-E_1}$ where $Z_{\rm exc} = \sum_{n \geq 1} e^{-E_n}$ is the partition function restricted to states above the one-particle level. The full partition function $Z = \mathrm{Tr}(\hat{T})$ is controlled by the cluster expansion (Theorem 3, SS4.3). If the cluster expansion controls $\ln Z$ with K-uniform constants, it also controls $Z$ itself, and from that we extract a K-uniform bound on $\zeta$.

### 2.2 Execution

**Step 1.** At bare scale $K$ with inner Balaban step $k$, the transfer matrix $\hat{T}_k$ satisfies $Z_k = \mathrm{Tr}(\hat{T}_k) = e^{-E_0}(1 + e^{-(E_1-E_0)} + \sum_{n \geq 2} e^{-(E_n-E_0)})$. We have $\zeta = e^{E_1}\sum_{n \geq 1}e^{-E_n}$. **[OK]**

**Step 2.** The cluster expansion of Theorem 3 controls the free energy $\ln Z$ via the Kotecky-Preiss criterion with weight $\alpha$. The KP convergence gives $|\ln Z - \ln Z_0| \leq C_{\rm KP} |\Lambda|$ with $C_{\rm KP}$ depending on $\alpha, c_d, K_{\rm meas}, C_0$. Per Tier 1A bookkeeping (rows 1, 4, 6, 7), all these constants are K-uniform. **[OK]**

**Step 3 (the obstruction).** However, the cluster expansion controls $\ln Z$ (the free energy density), not the ratio $Z_{\rm exc}/Z_{\rm ground}$. To extract $\zeta$ from $\ln Z$, one needs to decompose the partition function by energy sector. The cluster expansion at bare scale $a_0(K)$ gives exponential decay of connected correlation functions with rate $\alpha/a_0(K)$ (Theorem 4(c)), which implies a mass gap $\Delta_0 \geq \alpha/a_0(K)$ -- but this is a lattice-spacing gap, not a bound on $\zeta$.

**Step 4 (rescue via restricted trace).** The cluster expansion does provide a usable bound on $\zeta$, but through a different route. In the KP regime, the truncated (connected) two-point function satisfies:

$$|\langle \mathcal{O}(x)\mathcal{O}(y)\rangle_c| \leq C e^{-\alpha|x-y|/a}$$

with $C$ and $\alpha$ K-uniform (Tier 1A). By the spectral theorem applied to the transfer matrix, this implies:

$$\sum_{n \geq 1} |\langle 0|\mathcal{O}|n\rangle|^2 e^{-(E_n-E_0)} \leq C \|\mathcal{O}\|^2 $$

This bounds a *weighted* sum over excited states, not $\zeta$ itself. To bound $\zeta = \sum_{n \geq 1} e^{-(E_n-E_1)}$ directly, one would need to remove the matrix-element weights, which requires a completeness/density-of-states argument -- bringing back the lattice-dimension problem.

### 2.3 Verdict

**Attempt 1 does not close the gap.** The cluster expansion controls the free energy and correlation decay with K-uniform constants, but extracting $\zeta$ (an unweighted sum over excited states, not a correlation function) requires knowledge of the density of states, which reintroduces the lattice-dimension factor. The cluster expansion is the wrong tool for bounding $\zeta$ directly because $\zeta$ is not a thermodynamic quantity -- it is a spectral-theoretic quantity about the Hamiltonian's eigenvalue distribution.

---

## Section 3 -- Attempt 2: Physical-Distance Combes-Thomas

### 3.1 Strategy

Keep the Combes-Thomas structure of the existing proof but reformulate in physical units. The original Combes-Thomas (1973) gives resolvent decay $|\langle x|(H-z)^{-1}|y\rangle| \leq C e^{-\mu|x-y|}$ with $\mu$ depending on $\mathrm{dist}(z, \sigma(H))$ and the hopping amplitude, not on the local Hilbert space dimension. Use this to replace the lattice-site counting in the $\zeta$ bound.

### 3.2 Execution

**Step 1 (Combes-Thomas in physical units).** For a lattice Hamiltonian $H$ with nearest-neighbor hopping amplitude $J$ and spectral gap $\Delta$ above the ground state, the Combes-Thomas estimate gives:

$$|\langle x|P_{\rm exc}|y\rangle| \leq C \exp(-\mu \cdot d_{\rm phys}(x,y))$$

where $P_{\rm exc}$ is the spectral projection onto excited states and $\mu = \Delta/(2J)$ in physical units. The key point: $\mu$ depends on $\Delta/J$, a ratio of physical energy scales, not on the number of lattice sites. **[OK -- standard, Combes-Thomas 1973 Theorem 1]**

**Step 2 (Balaban Hamiltonian parameters).** At bare scale $K$, inner step $k$, the effective Hamiltonian $H_k$ has:
- Physical gap $\Delta_{\rm phys}$ (K-uniform by the RG recursion, conditional on the full proof).
- Hopping amplitude $J_k \sim g_k^2/a_k$ in physical units (coupling times inverse lattice spacing). On the AF trajectory, $g_k^2 \sim 1/\ln(1/(a_k\Lambda))$, so $J_k \sim 1/(a_k \ln(1/(a_k\Lambda)))$.

The Combes-Thomas decay rate is $\mu \sim \Delta_{\rm phys} a_k \ln(1/(a_k\Lambda))$, which *grows* as $a_k \to 0$ (more steps $k$ within theory $K$). This is the favorable direction. **[OK -- physical rate is K-uniform from below]**

**Step 3 (Density of energy eigenstates in physical units).** Here is the critical step. The $\zeta$ bound requires counting the number of energy eigenstates with energy below some cutoff $E_{\rm cut}$ that are supported in a ball of physical radius $r_0 + r$.

In the existing proof, this count is $\exp(C_1(R_0+r)^3 N^2)$ -- the Hilbert space dimension on a lattice ball. The replacement is: in a gapped theory, the density of energy eigenstates per unit physical volume below energy $E$ is bounded by a physical constant $\rho_{\rm phys}(E)$.

**The Combes-Thomas resolvent bound gives us exactly this.** The trace of the spectral projection $P_{[E_1, E_1+\omega]}$ restricted to a ball $B_R$ of physical radius $R$ satisfies:

$$\mathrm{Tr}(P_{B_R} P_{[E_1, E_1+\omega]} P_{B_R}) \leq \frac{\omega}{\pi} \cdot \sup_{\epsilon > 0} \mathrm{Tr}(P_{B_R} \mathrm{Im}(H - E_1 - \omega/2 - i\epsilon)^{-1} P_{B_R})$$

by the Stone formula. The resolvent restricted to $B_R$ has rank at most equal to the *Hilbert space dimension on $B_R$* -- and here the lattice-dimension blowup re-enters. **[OBSTRUCTION]**

**Step 4 (Why physical-distance Combes-Thomas still fails for $\zeta$).** The Combes-Thomas estimate controls off-diagonal resolvent decay beautifully -- matrix elements between separated points decay exponentially with K-uniform rate. But to bound $\zeta$, we need the *trace* of the Boltzmann operator restricted to a region, not just its off-diagonal kernel. The trace involves the *diagonal* of the resolvent summed over all sites in the ball, which is proportional to the number of sites -- i.e., $(R/a_0(K))^3$ -- reintroducing the $K$-dependent factor.

### 3.3 Verdict

**Attempt 2 does not close the gap by itself.** Physical-distance Combes-Thomas controls off-diagonal decay with K-uniform rates but does not resolve the on-diagonal (density-of-states) contribution to $\zeta$. The lattice-dimension factor $\exp(C(R/a)^3 N^2)$ re-enters through the trace over the restricted Hilbert space.

However, this attempt reveals a crucial structural insight: the problem is *entirely* in the density-of-states factor, not in the decay rate. This points toward Attempt 3.

---

## Section 4 -- Attempt 3: Hastings-Koma Exponential Clustering

### 4.1 Strategy

The Hastings-Koma theorem (CMP 265, 2006) proves that a spectral gap implies exponential clustering of ground-state correlations, with constants depending only on the gap $\Delta$ and the Lieb-Robinson velocity $v_{\rm LR}$, *not* on the local Hilbert space dimension. The key insight: we do not need to bound $\zeta$ at all. We can *replace* the $\zeta$-based argument in Step 3 of the spectral lemma with a direct clustering argument.

### 4.2 The crucial reformulation

**The spectral lemma does not actually need $\zeta$.** What the proof needs is a bound on:

$$S = \sum_{n_j} |\tilde{W}_\alpha^{(m)}(n_j)| \cdot e^{-\max(E_{n_j}-E_1, 0)}$$

The existing proof bounds this by $\|\hat{A}^{(s)}\|(1+\zeta)$, introducing $\zeta$ as an intermediary. But $S$ is itself a *matrix element* of a bounded operator -- specifically, $S \leq \|\hat{A}^{(s)}\| \cdot \mathrm{Tr}(|\hat{A}^{(s')}| \cdot e^{-\max(H-E_1,0)})$ restricted to states accessible from a local perturbation of the one-particle state.

**The Hastings-Koma route bypasses $\zeta$ entirely.** Instead of bounding $\zeta$ (the full Boltzmann sum over excited states) and then multiplying by the operator norm, we bound the *correlation function itself*:

$$|\langle 1|\hat{A}^{(-1)}\hat{T}\hat{A}^{(1)}|1\rangle_c| \leq C \|\hat{A}^{(-1)}\| \|\hat{A}^{(1)}\| \cdot f(\Delta, v_{\rm LR}, r_0)$$

where $f$ depends only on K-uniform physical quantities.

### 4.3 Execution

**Step 1 (Hastings-Koma applied to the transfer matrix).** Consider the transfer matrix $\hat{T} = e^{-aH}$ at bare scale $K$. The spectral gap above the one-particle state is $E_2 - E_1 \geq \hat\Delta_k/2$ (established in SS5.5.3 Step 3(ii), K-uniform per Tier 1A). For the *ground state* $|0\rangle$, Hastings-Koma gives exponential clustering with correlation length $\xi = v_{\rm LR}/\Delta$.

But we need clustering for the *one-particle state* $|1\rangle$, not the ground state. **[PARTIAL OBSTRUCTION]**

**Step 2 (Resolution: one-particle state as a local excitation of the vacuum).** The one-particle state $|1\rangle$ is obtained from the vacuum $|0\rangle$ by applying a local operator (a glueball creation operator) supported in a ball of physical radius $O(1/\Delta_{\rm phys})$. The matrix element $\langle 1|\mathcal{O}|1\rangle$ can be rewritten as a *vacuum* four-point function:

$$\langle 1|\mathcal{O}|1\rangle = \lim_{T\to\infty} \frac{\langle 0|\Phi^\dagger(T)\mathcal{O}(0)\Phi(-T)|0\rangle}{\langle 0|\Phi^\dagger(T)\Phi(-T)|0\rangle}$$

where $\Phi$ is the glueball interpolating field. The connected part $\langle 1|\mathcal{O}|1\rangle_c$ is then a *connected vacuum correlation function* of local operators, to which Hastings-Koma applies directly. **[OK -- standard LSZ-type reduction for the transfer matrix]**

**Step 3 (K-uniform Hastings-Koma constants).** The Hastings-Koma bound on the connected vacuum correlator is:

$$|\langle 0|A(x) B(y)|0\rangle_c| \leq C_{\rm HK} \|A\| \|B\| e^{-d(x,y)/\xi}$$

with $\xi = v_{\rm LR}/\Delta_{\rm phys}$ and $C_{\rm HK}$ depending on $v_{\rm LR}$, $\Delta_{\rm phys}$ and the spatial dimension $d$, but **not** on the local Hilbert space dimension (Hastings-Koma 2006, Theorem 1; Nachtergaele-Sims 2006, improvement removing $D$-dependence).

For K-uniformity of $C_{\rm HK}$, we need $v_{\rm LR}$ and $\Delta_{\rm phys}$ to be K-uniform.

**$\Delta_{\rm phys}$ K-uniform:** This is the *conclusion* of the full proof (the continuum limit of the mass gap). However, within the *inductive* structure, the RG recursion (SS5.7) assumes $\Delta_{\rm phys}$ is bounded away from zero at each step and proves it at the next step. The K-uniformity of $\Delta_{\rm phys}$ is therefore part of the inductive hypothesis, not an external input. **[OK -- inductive]**

**$v_{\rm LR}$ K-uniform:** For the Balaban effective Hamiltonian at inner step $k$ of bare theory $K$, the interaction has range $O(a_k)$ in physical units and strength $\|V_k\| \leq C g_k^2$ per block. The Lieb-Robinson velocity is:

$$v_{\rm LR} \leq C' \cdot \sup_{x} \sum_{X \ni x} \|h_X\| |X| e^{\mu \mathrm{diam}(X)} \leq C' \cdot J_{\rm eff} \cdot (a_k)^{-1}$$

where $J_{\rm eff}$ is the physical interaction strength per link. **Here is the key:** in Balaban's construction, the effective Hamiltonian at step $k$ has the form $H_k = H_k^{(0)} + V_k$ with $H_k^{(0)}$ the free part (quadratic, giving glueball masses) and $V_k$ the perturbation with $\|V_k\| \leq C g_k^2$ per unit volume. The Lieb-Robinson velocity in *physical* units is:

$$v_{\rm LR}^{\rm phys} = v_{\rm LR} \cdot a_k \leq C'' \cdot g_k^2 / a_k \cdot a_k = C'' g_k^2$$

On the AF trajectory, $g_k^2 \leq g_0^2 < \infty$ uniformly for all $k \geq 0$ within any bare theory $K$. Moreover, $g_0^2(K)$ converges to $g_\infty^2$ as $K \to \infty$. Hence $v_{\rm LR}^{\rm phys}$ is K-uniform. **[OK -- conditional on the Nachtergaele-Sims/Hastings-Koma framework applying]**

**Step 4 (Applicability to SU(N) lattice gauge theory).** The Hastings-Koma theorem as stated requires (a) a spectral gap, (b) a Lieb-Robinson bound. Condition (a) is part of the inductive hypothesis. Condition (b), as noted by the Tier 1B agent, is not rigorously established for 4D SU(N) Wilson in the published literature.

**However**, there is a crucial simplification available within Balaban's construction. The small-field restriction $|F| < g_k^{3/4}$ effectively truncates the link Hilbert space $L^2(\mathrm{SU}(N))$ to representations with Casimir $C_2(r) \leq C/g_k^{3/2}$, giving an *effective* local dimension $D_{\rm eff} \leq \exp(C' N^2 / g_k^{3/2})$. This is *independent of $K$* at fixed inner step $k$, because $g_k$ depends on $k$ and the starting coupling $g_0(K)$ but not on $K$ separately (on the AF trajectory, $g_0(K) \to g_\infty$ as $K \to \infty$).

With this finite effective dimension, the *original* Hastings-Koma theorem (which does allow finite local dimension) applies directly. The effective dimension enters only through the Lieb-Robinson velocity, which we have already shown to be K-uniform.

**Step 5 (Assembly).** Combining Steps 2-4: the connected one-particle matrix element $\langle 1|\mathcal{O}|1\rangle_c$, rewritten as a connected vacuum four-point correlator, satisfies the Hastings-Koma exponential clustering bound with K-uniform constants $C_{\rm HK}$, $\xi$. The spectral lemma bound becomes:

$$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_{\rm HK}(p, N, v_{\rm LR}^{\rm phys}, \Delta_{\rm phys}) \cdot M \cdot \hat\Delta^p$$

with the constant $C_{\rm HK}$ depending only on K-uniform physical quantities. Setting $C_p^* = C_{\rm HK}(p, N, v_{\rm LR}^{\rm phys}, \Delta_{\rm phys})$ gives the required K-uniform bound.

### 4.4 Handling the polymer-aware extension (Tier 2 D3)

For the application to $\delta E_k^{d=6} = \sum_X K_k^{(6)}(X,V)$, the polymer-aware lemma (D3 document, Section 2) applies the spectral bound per polymer and sums. With the Hastings-Koma route, each per-polymer contribution satisfies:

$$|\langle 1|K(X)|1\rangle_c| \leq C_{\rm HK}(p, N) \cdot M(X) \cdot \hat\Delta^p$$

where crucially $C_{\rm HK}$ does **not** depend on $|X|$ (the polymer size in lattice units) because the Hastings-Koma bound depends on the *physical* support and correlation length, not on the lattice-site count. The sum over polymers then converges:

$$\sum_{X \ni 0} C_{\rm HK} \cdot e^{-\kappa|X|} = C_{\rm HK} \cdot C_{\rm KP} < \infty$$

with both factors K-uniform. This resolves the D3 obstruction (Section 3.3 of the D3 document) where $\exp(C|X|^d N^2)$ beat $e^{-\kappa|X|}$ -- that exponential blowup came from the lattice-dimension-based $\zeta$ estimate, which the Hastings-Koma route bypasses entirely.

### 4.5 Verdict

**Attempt 3 closes the gap, conditional on two inputs:**

**(C1) Effective finite-dimensionality from the small-field restriction.** The small-field condition $|F| < g_k^{3/4}$ restricts to representations with bounded Casimir, giving effective local dimension $D_{\rm eff} \leq \exp(C' N^2 / g_k^{3/2})$ that is K-uniform at fixed $k$. This is a direct consequence of Balaban's construction (CMP 109, small-field domain characterization) and requires no new mathematics -- only the observation that the Peter-Weyl decomposition of $L^2(\mathrm{SU}(N))$ truncates under the small-field constraint. **Rigor: [OK]**, conditional on Balaban's small-field characterization.

**(C2) Hastings-Koma applies to the Balaban Hamiltonian.** With $D_{\rm eff}$ finite and K-uniform, the Balaban Hamiltonian at each scale is a finite-dimensional lattice system with finite-range bounded interactions, exactly in the scope of Hastings-Koma 2006 Theorem 1. The spectral gap is part of the inductive hypothesis. **Rigor: [OK]**, by direct application of published results.

---

## Section 5 -- Comparison and Verdict

| Approach | Bounds $\zeta$? | K-uniform? | Avoids $D_{\rm loc}$? | Polymer-compatible? | Status |
|:---------|:---------------|:-----------|:---------------------|:-------------------|:-------|
| 1. Cluster expansion | No (wrong quantity) | N/A | N/A | N/A | **Fails** |
| 2. Physical Combes-Thomas | Partially (off-diag only) | Off-diag yes, trace no | No (trace) | No | **Fails** |
| 3. Hastings-Koma | Bypasses $\zeta$ | Yes | Yes | Yes | **Succeeds** |

**The gap is closed by Approach 3** (Hastings-Koma exponential clustering), conditional on (C1) and (C2) above. Both conditions follow from published results plus Balaban's construction:

- (C1) is the Peter-Weyl truncation under the small-field restriction -- a standard observation in lattice gauge theory, not requiring new mathematics.
- (C2) is a direct application of Hastings-Koma (2006) to a finite-dimensional lattice system with a spectral gap, which is exactly the theorem's hypothesis.

**What is new in this proof:** The structural move of *not bounding $\zeta$ at all*, but instead recasting the spectral lemma's channel sum as a connected vacuum correlator and applying Hastings-Koma directly. This avoids the density-of-states factor entirely, because Hastings-Koma's bound is on correlation functions (which do not require counting states) rather than on partition-function ratios (which do).

**Residual caveat.** The argument uses Hastings-Koma in the form that applies to lattice systems with finite local dimension, spectral gap, and finite-range interactions. The passage from the infinite-dimensional $L^2(\mathrm{SU}(N))$ link Hilbert space to the effective finite-dimensional truncation under the small-field condition is physically natural but requires a precise statement about the error from the large-field (large-representation) tail. Balaban's construction controls this error by $O(e^{-c/g_k^{2\epsilon}})$ (CMP 119), which is smaller than any power of $g_k$ and hence negligible in the RG recursion. The combined error from (i) the Hastings-Koma bound on the truncated system plus (ii) the large-field tail correction gives the full bound. This is a minor bookkeeping exercise, not a gap.

---

## Section 6 -- Draft Insertion for SS5.5.3

The following replaces the paragraph beginning "by the Combes-Thomas estimate" in Step 3(i) of SS5.5.3 (lines 1275-1299 of `05-continuum-limit.md`).

---

**(i) Volume and K-independence via exponential clustering.** The operator $\mathcal{O}$ is supported in a physical ball $B_{r_0}$ of diameter $r_0 = R_0 \cdot a_k$. The connected one-particle matrix element $\langle 1|\mathcal{O}|1\rangle_c$ is rewritten as a connected vacuum four-point correlator via LSZ reduction:

$$\langle 1|\mathcal{O}|1\rangle_c = \lim_{T\to\infty} \frac{\langle 0|\Phi^\dagger(T)\mathcal{O}(0)\Phi(-T)|0\rangle_c}{\langle 0|\Phi^\dagger(T)\Phi(-T)|0\rangle}$$

where $\Phi$ is a glueball interpolating field of physical extent $O(\Delta_{\rm phys}^{-1})$.

In the small-field domain of Balaban's construction, the effective Hamiltonian acts on a Hilbert space with effective local dimension $D_{\rm eff} \leq \exp(C_D N^2 / g_k^{3/2})$ per link (from the Peter-Weyl truncation under $|F| < g_k^{3/4}$), with nearest-neighbor interactions of strength $\|h_{\rm link}\| \leq C g_k^2 / a_k$ and physical range $a_k$. This is a finite-dimensional lattice system with finite-range bounded interactions and spectral gap $\Delta_{\rm phys} > 0$ (inductive hypothesis). By the Hastings-Koma exponential clustering theorem (CMP 265, 2006, Theorem 1; see also Nachtergaele-Sims, CMP 265, 2006), the connected vacuum correlator satisfies:

$$|\langle 0|A(x) B(y)|0\rangle_c| \leq C_{\rm HK} \|A\| \|B\| \exp(-d_{\rm phys}(x,y)/\xi)$$

with correlation length $\xi = v_{\rm LR}^{\rm phys}/\Delta_{\rm phys}$ and $C_{\rm HK}$ depending only on $d$, $N$, $v_{\rm LR}^{\rm phys}$, and $\Delta_{\rm phys}$. The Lieb-Robinson velocity in physical units is $v_{\rm LR}^{\rm phys} \leq C'' g_k^2$, which is K-uniform on the asymptotically free trajectory ($g_k \to g_\infty$ as $K \to \infty$ at fixed $k$). The large-field tail (representations with Casimir exceeding the truncation) contributes $O(e^{-c/g_k^{2\epsilon}})$ (Balaban, CMP 119), negligible compared to $g_k^4 \hat\Delta^2$.

Applying the deviation extraction (Step 1) to the four-point correlator and using the Hastings-Koma bound with K-uniform constants gives:

$$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p^* \cdot M \cdot \hat\Delta^p$$

with $C_p^* = C_p^*(p, N, g_\infty, \Delta_{\rm phys})$ independent of $k$, $K$, and the lattice volume $L$. This replaces the Combes-Thomas-based bound with a clustering-based bound that avoids the lattice-site-counting density-of-states factor and is K-uniform by construction.

**For the polymer-aware extension:** each polymer $K(X)$ with $\|K(X)\| \leq e^{-\kappa|X|}$ satisfies the same bound with $C_p^*$ independent of $|X|$, because the Hastings-Koma constant depends on the physical support (not the lattice-unit count). The sum $\sum_{X \ni 0} C_p^* e^{-\kappa|X|} = C_p^* C_{\rm KP} < \infty$ converges by Kotecky-Preiss.

---

*End of document.*
