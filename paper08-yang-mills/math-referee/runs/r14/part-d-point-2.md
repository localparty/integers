## Part D, Point 2: Stability of Boltzmann Deviation Order

**Weight:** HEAVY
**Verdict:** SOUND

This is the single most important technical innovation in the paper. I interrogated it with maximum skepticism.

**Finding:**

**(a) The definition of Boltzmann deviation order.** Definition D.2 defines $\mathrm{dev}(\mathcal{O}) \geq p$ in terms of the spectral weight $W_\alpha^{(m)}(\mathbf{n})$ vanishing to order $\geq p$ at the diagonal $n_j = m$ for all $j$. This is precisely the condition that the Boltzmann deviation factors $(e^{E_m - E_{n_j}} - 1)$ can be extracted $p$ times from the weight.

The connection to the matrix element bound is: $\mathrm{dev}(\mathcal{O}) \geq p$ implies $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M\,\hat{\Delta}^p$ (the spectral lemma, Point D3). The definition is EQUIVALENT to the matrix element bound in the following sense: $\mathrm{dev} \geq p$ gives the bound with the stated constant; conversely, if the bound holds for ALL gapped systems (uniformly), then $\mathrm{dev} \geq p$. The definition is at the spectral weight level, which is more fundamental -- it characterizes the operator's structure, not just a specific matrix element.

An operator could satisfy Definition D.2 but give a tighter bound (e.g., $\hat{\Delta}^{p+1}$). The definition is a lower bound on the vanishing order.

**(b) The linear combination lemma.** If $\mathrm{dev}(\mathcal{O}_i) \geq p$ for all $i$ and $\sum |c_i|\,\|\mathcal{O}_i\| < \infty$, then $\mathrm{dev}(\sum c_i\,\mathcal{O}_i) \geq p$.

The proof rests on a clean algebraic fact: the spectral weight of a sum is the sum of spectral weights (linearity of the trace). If each weight $W_i(\mathbf{n})$ vanishes to order $\geq p$ at the diagonal, then $W(\mathbf{n}) = \sum c_i W_i(\mathbf{n})$ also vanishes to order $\geq p$ at the diagonal. This is because a convergent sum of functions, each having a zero of order $\geq p$ at a point, has a zero of order $\geq p$ at that point.

Formally: if $W_i(\mathbf{n}) = \prod_j (e^{E_m - E_{n_j}} - 1)^{p_{ij}}\,R_i(\mathbf{n})$ with $\min_j p_{ij} \geq p$ and $|R_i| \leq M_i$, then $W(\mathbf{n}) = \sum c_i W_i(\mathbf{n})$ vanishes whenever any $n_j = m$ (because each term vanishes). The order of vanishing is $\geq p$ because each term contributes at least $p$ factors of $(e^{E_m - E_{n_j}} - 1)$.

**Can cancellations reduce the deviation order?** No. Consider two operators with $\mathrm{dev} \geq 2$. Their weights both vanish quadratically at the diagonal. A cancellation in the sum could reduce the leading coefficient but cannot eliminate the zero: if $f(x) = x^2 h_1(x)$ and $g(x) = x^2 h_2(x)$, then $f + g = x^2(h_1 + h_2)$, which still has a zero of order $\geq 2$ (even if $h_1(0) + h_2(0) = 0$, the zero becomes order $\geq 3$, not $< 2$).

For operators with different temporal supports, zero-padding (inserting identity time slices) is addressed in Section 5.5.3. Inserting an identity $\hat{T}$ between time slices adds factors of $e^{-E_n}$ that do not affect the deviation structure (they multiply each weight uniformly). The deviation order is defined through the vanishing at the diagonal, which is unaffected by multiplicative factors.

**(c) The role of (B1) analyticity.** Property (B1) ensures that $\delta E_k^{d=6}$ is a CONVERGENT linear combination of local operators (not a formal perturbative expansion). The analyticity radius $\rho > 0$ is $k$-independent (Appendix H).

The spectral lemma evaluates $\langle 1|\delta E_k^{d=6}|1\rangle_c$. The state $|1\rangle$ is the one-particle (glueball) state. In the gapped phase, $|1\rangle$ has support concentrated on TYPICAL configurations. Typical configurations in a gapped lattice gauge theory satisfy $|F_{\mu\nu}| \leq C\sqrt{g_k^2}$ (the Boltzmann factor exponentially suppresses large field strengths). The small-field condition $|F_{\mu\nu}| < g_k^{1-\epsilon}$ is satisfied by typical configurations when $g_k$ is small (since $\sqrt{g_k^2} = g_k \ll g_k^{1-\epsilon}$ for $\epsilon > 0$). Therefore typical configurations LIE WITHIN the analyticity domain $\Omega_s$.

Configurations outside $\Omega_s$ contribute to the matrix element through the large-field region, which is suppressed by $e^{-c/g_k^{2\epsilon}}$ (Point C2(b)). This is negligible compared to $g_k^4\,\hat{\Delta}^2$.

**(d) Perturbative to non-perturbative transition.** This was the most contested point in the r05 review (initially flagged as a GENUINE GAP, later revised to CLOSABLE, and finally marked SOUND in r06). The critical insight:

The naive splitting $\mathcal{O} = \mathcal{O}^{\mathrm{pert}} + \delta\mathcal{O}$ with $\|\delta\mathcal{O}\| \leq Cg_k^6$ FAILS because $\delta\mathcal{O}$ has no guaranteed deviation structure, giving $|\langle 1|\delta\mathcal{O}|1\rangle_c| \leq Cg_k^6/\hat{\Delta}^3$, which exceeds $g_k^4\hat{\Delta}^2$ on the AF trajectory (since $g_k^2 \gg \hat{\Delta}^5$).

The CORRECT approach avoids this splitting entirely. Instead:
1. By (B1), $\delta E_k^{d=6}$ is analytic, so it IS a convergent Taylor series in field variables.
2. Each monomial in the Taylor series is a $\mathcal{C}$-even, gauge-invariant operator of engineering dimension 6 (by the dimension assignment of the extraction lemma).
3. By the exhaustive classification (Point D1), EVERY such operator has $\mathrm{dev} \geq 2$.
4. By the linear combination lemma, $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$.

The argument does not split into "perturbative" and "non-perturbative" parts. The classification applies to the FULL non-perturbative operator because it is a convergent sum of classified operators. This is the paper's key innovation: replacing a perturbative identification with a structural classification.

The dimension-4 projection is well-defined non-perturbatively: $S_{\mathrm{YM}}$ is the UNIQUE local, $\mathcal{C}$-even, parity-even, gauge-invariant operator of engineering dimension 4 on the hypercubic lattice (PROOF-CHAIN.md IV.3; verified by the r03 referee). Balaban's coupling renormalization subtracts this unique operator by definition. The remainder has no dim-4 contamination.

**(e) Structural zero vs. kinematic zero.** The diagonal vanishing $(e^{E_1 - E_1} - 1)^2 = 0$ arises from the two-derivative structure of every dim-6 $\mathcal{C}$-even operator. It is structural because:

1. Every $\mathcal{C}$-even dim-6 operator has two covariant derivatives (by the classification).
2. Each covariant derivative generates one factor of $(e^{E_m - E_{n_j}} - 1)$ in the spectral weight (from the transfer matrix representation of $D_0$).
3. At the diagonal $n_j = m$, each factor vanishes: $(e^{E_m - E_m} - 1) = 0$.
4. Two derivatives give two such factors, hence $\mathrm{dev} \geq 2$.

For the non-perturbative operator $\delta E_k^{d=6}$, the spectral weights are not computed explicitly. They are inferred from the classification via the linear combination lemma. The inference is rigorous: each term in the convergent expansion has $\mathrm{dev} \geq 2$, and deviation order is preserved under convergent linear combinations (as proved in (b) above).

The question "Can $\mathrm{dev} \geq 2$ for each term but $\mathrm{dev} < 2$ for the sum?" has a definitive negative answer: the proof in (b) shows that a convergent sum preserves the minimum deviation order. Cancellations can only INCREASE the order, never decrease it.

**Impact on the claimed result:** This point is CENTRAL to $\Delta_\infty > 0$. The stability of deviation order under the non-perturbative effective action is the bridge between Balaban's UV analysis and the IR mass gap. The argument chain (B1)$\to$(B2)$\to$classification$\to$linear combination$\to$$\mathrm{dev} \geq 2$ is sound at each link. No gap found.
