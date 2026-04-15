## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND (the linear-combination lemma is correctly proved and the classification argument bypasses the failure of perturbative splitting; the previous referee r05/r06 verdict stands)

**Finding:**

(a) **Definition D.2.** The "Boltzmann deviation order" is defined in §5.5.2 in terms of the spectral weight $W_\alpha^{(m)}(\mathbf{n}) e^{-E(\mathbf{n})}$ admitting a factorization of $p$ powers of $(e^{E_m - E_{n_j}} - 1)$ from a *bounded* residual $\tilde W_\alpha^{(m)}$. This is *equivalent* to "the spectral weight vanishes to order $p$ at the diagonal $\mathbf{n} = (m, m, \ldots, m)$" — a clean structural condition.

For $\mathrm{Tr}(D_0 F)^2$, the equality $(e^{E_m - E_n} - 1)^2 = 0$ at $n = m$ is a *structural* zero (it follows from the squared structure, not from a numerical cancellation), so $\mathrm{dev}(\mathrm{Tr}(D_0 F)^2) \geq 2$. This is verified explicitly in §5.5.4. Sound.

The definition is *not* the same as "excitation number" $\#(\mathbf{n}) \geq p$ (the original notion in earlier versions). The relationship is:
- $\mathrm{exc}(\mathcal{O}) \geq p \Rightarrow \mathrm{dev}(\mathcal{O}) \geq p$ (the new condition is *weaker*).
- Converse fails: an operator can have $\mathrm{dev} \geq p$ even if low-excitation channels are *populated*, as long as the populated weights vanish to order $p$ at the diagonal.

For dim-6 operators of the form $\mathrm{Tr}(D_0 F)^2$, the vacuum intermediate channel $n_1 = 0$ has nonzero weight, but the weight contains a factor $(e^{E_m - E_{n_1}} - 1)^2$ that gives the required $p = 2$ vanishing. This is the "Boltzmann deviation" mechanism.

(b) **The linear combination lemma.** §5.5.3 (after the spectral lemma) and again at the end of §5.5 proves: if each $\mathcal{O}_i$ has dev $\geq p$ and $\sum_i |c_i| \|\mathcal{O}_i\| < \infty$, then $\sum c_i \mathcal{O}_i$ has dev $\geq p$. The proof: the spectral representation of the sum is indexed by pairs $(i, \alpha_i)$, and if each summand admits a factorization of $p$ deviation factors, the sum inherits the factorization with a residual bounded by $\sum_i |c_i| \cdot |\tilde W_{\alpha_i, i}^{(m)}|$. This is correct.

**Subtlety:** the temporal extents $R_i$ of the $\mathcal{O}_i$ may differ. The linear-combination lemma requires the sum to be embedded in a single spectral representation with a *common* temporal extent $R = \max R_i$. The "Remark (Uniform temporal extent)" handles this by appealing to Balaban's polymer expansion, which generates operators with diameter bounded by $R_0$ block lattice units (CMP 109, Theorem 1). Hence $R_i \leq R_0$ uniformly in $i$ and $k$. Sound.

(c) **The role of (B1) analyticity.** Analyticity ensures that $\delta E_k^{d=6}$ is a *convergent* (not formal) Taylor series in the link variables, so the dimension-6 projection is exact and the linear-combination lemma applies to a *convergent* sum, not a divergent series. The convergence radius is $\rho > 0$ uniformly in $k$ (proved in §5.6 Part I, "$k$-independent analyticity radius"). Sound.

The configurations contributing to the matrix element $\langle 1|\delta E_k^{d=6}|1\rangle_c$ are *typical* configurations of the gapped phase. The proof tacitly assumes these lie within the analyticity domain $\Omega_s = \{|F| < g_k^{1-\epsilon}\}$. This is *not quite* automatic — typical configurations of the *full* path integral may not be small-field — but the small-field/large-field decomposition relegates the non-small-field contribution to the exponentially-suppressed tail. Sound, modulo the C2 large-field optimization issue.

(d) **Perturbative ↔ non-perturbative transition.** The classification argument bypasses the failure of naive splitting (Section 5.6 Part III.2). It does *not* identify $\delta E_k^{d=6}$ with $c_6 \mathrm{Tr}(D_\rho F)^2$ at leading order and then argue that corrections are small. Instead it argues that:
1. By (B1), $\delta E_k^{d=6}$ is analytic, hence has a convergent expansion in monomials.
2. Each monomial of dimension 6, $\mathcal{C}$-even, gauge-invariant falls into the Lüscher–Weisz basis.
3. Each operator in the basis has dev $\geq 2$ (verified for the two two-derivative operators in Point D1).
4. By the linear-combination lemma, the convergent sum has dev $\geq 2$.

This is the genuine technical innovation of the proof. It avoids the perturbative-vs-non-perturbative split that would be circular. r05 originally flagged this as a closable gap, then revised to SOUND on careful re-examination. r06 confirmed SOUND. I concur.

(e) **Structural vs. kinematic zero.** The structural zero $(e^{E_1 - E_1} - 1)^2 = 0$ is a property of the operator class (squared temporal differences), not of a specific matrix element. r05 was concerned about non-perturbative corrections lifting this zero, but the classification argument addresses this: any non-perturbative correction must itself be a $\mathcal{C}$-even, dim-6, gauge-invariant operator and therefore must also have $\mathrm{dev} \geq 2$. There is no "loophole" through which a correction with $\mathrm{dev} < 2$ could enter.

**Impact on the claimed result:** SOUND. This is the proof's strongest piece of new mathematics, and it does what is claimed. The previous referees correctly identified this as the proof's main innovation.
