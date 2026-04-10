## Part D, Point 3: The Spectral Lemma

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

**(a) The deviation extraction (Step 1).** The proof extracts $p$ factors of $(e^{E_m - E_{n_j}} - 1)$ from the spectral weight. The distinction between near-diagonal and far-diagonal is handled as follows:

- **Near-diagonal ($n_j = 0$, vacuum intermediate state):** $|e^{E_1 - E_0} - 1| = |e^{\hat{\Delta}} - 1| \leq C_*\,\hat{\Delta}$ where $C_* = e^{\hat{\Delta}_{\max}}$ is $k$-independent (because $\hat{\Delta}_k$ is bounded above uniformly -- it converges to a finite limit as $k \to \infty$).
- **Far-diagonal ($n_j \geq 2$, multi-particle states):** $|e^{E_1 - E_{n_j}} - 1| \leq 1$ (trivial bound). These factors are $O(1)$, not $O(\hat{\Delta})$.

The proof claims: for $\mathrm{dev} \geq p$, the weight $W(\mathbf{n})$ vanishes to order $\geq p$ at the diagonal. This means at least $p$ of the indices must be excited away from $m$ for the weight to be nonzero. Among these excited indices:
- Those with $n_j = 0$ (vacuum) contribute $O(\hat{\Delta})$ each
- Those with $n_j \geq 2$ (multi-particle) contribute $O(1)$ each, but are Boltzmann-suppressed by $e^{-(E_{n_j} - E_1)} \leq e^{-\hat{\Delta}_k/2}$ (from the two-particle threshold bound)

The total bound extracts $p$ factors of $O(\hat{\Delta})$ from the $n_j = 0$ excitations. The $n_j \geq 2$ contributions are absorbed into the residual weight, which is bounded by $M$ (the operator norm). The resulting bound is $C_p\,M\,\hat{\Delta}^p$ as claimed.

More precisely: the spectral sum is dominated by configurations where exactly the $p$ required indices are excited to $n_j = 0$ (vacuum) and all others remain at $n_j = m = 1$ (one-particle). Each vacuum excitation gives a factor $(e^{\hat{\Delta}} - 1) \leq C_*\hat{\Delta}$. Higher excitations give subleading contributions suppressed by $e^{-\hat{\Delta}_k/2}$ per additional excitation.

**(b) The $\zeta$ bound and two-particle threshold.** The quantity $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ requires $E_2 - E_1 > 0$ (spectral gap above the one-particle state). The preprint establishes:

$$E_2 - E_1 \geq \hat{\Delta}_k - \epsilon_B \geq \hat{\Delta}_k/2$$

where $\epsilon_B \leq C_B\,g_k^4\,\hat{\Delta}_k$ is the binding energy (energy by which a two-glueball bound state lies below the two-particle threshold $2E_1$).

The bound $\epsilon_B \leq C_B\,g_k^4\,\hat{\Delta}_k$ uses perturbative estimates (Born approximation, Lippmann-Schwinger equation). Is this valid non-perturbatively?

For weak coupling ($g_k$ small), the two-glueball interaction is perturbatively small ($O(g_k^4)$ from gluon exchange). The Born approximation gives the leading binding energy. Non-perturbative corrections (instantons, large-field effects) are $e^{-c/g_k^{2\epsilon}}$ (large-field) or $e^{-c/g_k^2}$ (instantons), both negligible compared to $g_k^4\hat{\Delta}_k$.

Could a deeply bound state exist at some RG step? No: (i) for $g_k$ small (perturbative regime), the interaction is weak and cannot produce deep binding; (ii) the mass gap $\hat{\Delta}_k$ grows as $2^k$ while the interaction $g_k^4$ shrinks as $1/k^2$, so the ratio $\epsilon_B/\hat{\Delta}_k \leq C_B g_k^4 \to 0$. The two-particle threshold gap $E_2 - E_1 > 0$ is maintained throughout the RG flow.

The r06 referee specifically examined this point (Point 2(c)) and found it CLOSED by the explicit two-particle threshold argument.

**(c) Volume independence via Combes-Thomas.** The Combes-Thomas estimate (Nachtergaele-Sims 2006) bounds the contribution of distant states to the spectral sum $\zeta$. The estimate requires the operator $\hat{A}^{(s)}$ to be local (supported in a ball of radius $R_0$).

$R_0$ is bounded uniformly in $k$: Balaban's block-spin generates operators with support of $O(1)$ block spacings at each scale. The dim-6 operators at step $k$ are local in units of the block lattice $\Lambda_k$. Their support radius in BLOCK UNITS is $O(1)$, not growing with $k$. (The support in physical units does grow as $2^k a_0$, but the Combes-Thomas estimate is applied in block units, where locality is preserved.)

The spectral lemma constant $C_p$ depends on $R_0$, $N$, and $p$, but NOT on $k$, $g_k$, or the volume $L$. The volume independence is crucial for the thermodynamic limit. From Appendix I.3: $C_p(N) \leq \exp(C_1 R_0^3 N^2)$, which is the worst-case constant. For fixed $N$ and $R_0$, this is finite.

**Impact on the claimed result:** None. The spectral lemma is correctly proved. The deviation extraction is precise, the two-particle threshold is maintained, and volume independence follows from Combes-Thomas estimates with uniform locality bounds.
