## Part G, Point 3: N-Dependence and Error Propagation

**Weight:** MEDIUM
**Verdict:** CLOSABLE GAP

**Finding:**

(a) The N-dependent constants throughout the proof chain:
- Spectral gap: $\mu_1 = 2N/r_3^2$ on $CP^{N-1}$ (Weitzenbock bound). IMPROVES with N.
- KK mass: $m_1 = 2\sqrt{3}/r_3$ for N=3; general N gives $m_1 = \sqrt{2N \cdot 2}/r_3 = 2\sqrt{N}/r_3$ from the actual eigenvalue $4N/r_3^2$... Actually, the actual first eigenvalue on 1-forms on $CP^{N-1}$ is $\mu_{min}^{(1)} = 2(N+1)/r_3^2$ (Ikeda-Taniguchi), which for N=3 gives $12/r_3^2$. For general N: $m_1 = \sqrt{2(N+1)}/r_3$, growing as $\sqrt{N}$.
- Propagator constant $C_0$: depends on N through Weyl asymptotics (degeneracy grows as $n^{N-2}$) and adjoint dimension ($N^2-1$). The growth is at most polynomial in N.
- KP convergence threshold: depends on $c_d$ (lattice-geometric, N-independent), $K$ (internal partition function, polynomial in N), and $C_0$ (polynomial in N). The threshold $\beta_{max} \sim m_1 a/6 \sim \sqrt{N} a/(6r_3)$ grows with N, so the convergence region EXPANDS.
- Analyticity radius $\rho$: depends on $r_{proj}(N) = 1/2$ (N-independent for the polar decomposition) and $\kappa$ (polymer decay, weakly N-dependent). Bounded below by a positive N-dependent constant.
- Spectral lemma constant $C_p$: depends on N through $\zeta$ (partition function of excited states, polynomial in N) and $R_0$ (support radius, N-independent).
- Gronwall exponent $\gamma = \alpha/(b_0 \ln 2)$: with $b_0 \sim N$ and $\alpha \sim N^2$, gives $\gamma \sim N$. The doubly exponential convergence $4^{-k}$ dominates $k^N$ for each fixed N.

No constant grows faster than polynomially in N, and the proof works for each fixed N with finite constants. No constant diverges as N increases.

(b) For SU(2): $d^{abc} = 0$, so all cubic Casimir operators vanish identically — the C-elimination of $Tr(F^3)$ is trivially satisfied (the operator doesn't exist). $CP^1 = S^2$ is a round sphere with simpler geometry. The exact area law $\sigma = 3g^2/8$ provides an independent check. The proof does NOT use any SU(2)-specific property that fails for $N \geq 3$. The C-elimination argument works for all N (C-odd operators have vanishing coefficients in C-invariant actions regardless of whether $d^{abc}$ is zero or nonzero). The spectral arguments on $CP^{N-1}$ work for all N by the same Weitzenbock formula. SOUND.

(c) The proof chain has ~14 steps, each with N-dependent constants. If each constant has a factor of (say) $N^2$, the accumulated error could grow as $N^{28}$. However, this accumulated N-dependence does not affect the proof for any fixed N, because: (i) the convergence of the sum $\sum C_k g_k^4 \hat{\Delta}_k^2$ is guaranteed by $4^{-k}$ for ANY polynomial growth; (ii) the mass gap $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ with $C_\infty > 0$ depends on N through $C_\infty$ and $\Lambda_\infty$, both of which are positive for each fixed N. **The preprint does not systematically track N-dependence through all constants.** This is acknowledged in Appendix I (Section I.3), which provides the framework but notes that a complete N-tracking is deferred. For the Clay prize, the proof must work for each fixed N — which it does. Large-N asymptotics are not required. **This is a closable gap**: systematic N-tracking through the 14 steps requires careful bookkeeping (estimate: 5-10 pages) but no new ideas.

**Impact on the claimed result:** The N-dependence is finite for each fixed N and does not affect the mathematical soundness. The lack of systematic N-tracking is a presentation gap closable with bookkeeping (5-10 pages). No impact on the proof for any specific N ≥ 2.
