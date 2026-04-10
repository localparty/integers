## Part B, Point 3: IR Equivalence — The Feshbach Projection

**Weight:** MEDIUM
**Verdict:** SOUND (Theorem 5 is now a complete proof, not a sketch — the previous referee r05 already revised this to SOUND)

**Finding:**

(a) **Feshbach decomposition.** Section 04.5 Lemma 4 uses the standard Feshbach projection $H_{\mathrm{eff}}(z) = H_{00} + W(z - H_{QQ})^{-1}W^\dagger$. The condition $z < \inf\sigma(H_{QQ}) \sim m_1$ is required for the resolvent to exist; this holds quantitatively because $\Delta_0^{\mathrm{KK}} \sim \Lambda_{\mathrm{QCD}} \sim 10^{-15} m_1$ in the physical regime. The bound $\|W\| \leq C_W e^{-m_1 a}$ comes from the bond-activity bound (Theorem 2). Sound.

The Feshbach formula is standard (Bach–Fröhlich–Sigal 1998) and the use is correct: it provides a bijection between low-lying eigenvalues of $\hat{H}_{\mathrm{KK}}$ and eigenvalues of $H_{\mathrm{eff}}$, with the off-diagonal coupling small in the regime $m_1 a \gg 1$.

(b) **Trace-norm bound and volume cancellation.** Lemma 2 gives $\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}} \leq C |\Lambda_t^1| e^{-m_1 a} \|\hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}$. The volume factor $|\Lambda_t^1|$ would naively cause trouble in the thermodynamic limit, but Step 4 of the assembly proves a *pointwise multiplicative kernel bound* $|\hat{T}_{\mathrm{red}}(U';U) - \hat{T}_{\mathrm{std}}(U';U)| \leq \bar\epsilon \cdot \hat{T}_{\mathrm{std}}(U';U)$ with $\bar\epsilon = 2C_1 |\Lambda_t^1| e^{-m_1 a}$, and from this derives the *operator inequality* $(1 - \bar\epsilon)\hat{T}_{\mathrm{std}} \leq \hat{T}_{\mathrm{red}} \leq (1 + \bar\epsilon)\hat{T}_{\mathrm{std}}$.

The min-max principle then gives eigenvalue ratios $\lambda_j(\hat{T}_{\mathrm{red}})/\lambda_j(\hat{T}_{\mathrm{std}}) \in [1-\bar\epsilon, 1+\bar\epsilon]$, and the mass-gap difference is bounded by $|\ln(1+\bar\epsilon)/(1-\bar\epsilon)|/a \leq 4\bar\epsilon/a$. This is small compared to $\Delta_0^{\mathrm{KK}}$ when $\bar\epsilon \ll \Delta_0^{\mathrm{KK}} a/4$, which holds whenever $|\Lambda_t^1| e^{-m_1 a/2} \ll \Delta_0 a$.

The volume issue is *technically* resolved: $|\Lambda_t^1| \sim L^3$ (polynomial volume), and $e^{-m_1 a/2}$ is doubly exponential in $m_1 a \sim 10^{15}$. So $|\Lambda_t^1| e^{-m_1 a/2}$ is "negligible" *for any reasonable* $L$. But the proof should state explicitly that the bound holds in the thermodynamic limit $L \to \infty$ for all $L < L_{\max}$ where $L_{\max} \sim e^{m_1 a/2}/\Delta_0$. This is *not* "uniform in $L$"; it's only good up to volumes that are themselves exponentially large in $m_1 a$.

For the joint $a \to 0$, $L \to \infty$ limit (Clay C11), this becomes a real concern: as $a$ shrinks, $m_1 a$ shrinks, so $L_{\max}$ shrinks, and the trace-norm bound becomes ineffective. The preprint addresses this by handing off to Balaban's RG before $m_1 a$ becomes small (specifically, when $a \sim r_3$, the regime where the cluster expansion ceases to converge — Section 04.3, "Regime C"). But this hand-off is exactly the K-vs-k issue.

(c) **Factorization of low-lying states.** Lemma 4 Step 4 establishes $\|\delta_n\| \leq (2C_W/m_1) e^{-m_1 a}$ for $n = 0, 1$, using the gap condition $\inf\sigma(H_{QQ}) - E_n \geq m_1/2$. For the *first excited state* (the glueball at $\Delta_0^{\mathrm{KK}}$), this requires $\Delta_0^{\mathrm{KK}} < m_1$, which holds because $\Delta_0 \sim \Lambda_{\mathrm{QCD}} \ll m_1 \sim 1/r_3$. Sound.

The Feshbach approach handles only the two lowest eigenstates (vacuum and glueball). It does NOT establish that the entire low-energy spectrum factorizes — only that the lowest two states are "approximately decoupled" from the KK sector. For Theorem 5's purposes (matching the *gap* between the two lowest states), this is sufficient.

(d) **One subtlety — the binding-energy condition.** The spectral lemma (Section 5.5.3, Step 3, item (ii)) establishes $E_2 - E_1 \geq \hat{\Delta}_k/2$ via the binding-energy bound $\epsilon_B \leq 2 C_B g_k^4 \hat{\Delta}_k$. This relies on the perturbative two-particle scattering being weak, which requires the small-field domain. The non-perturbative correction $\epsilon_B^{\mathrm{lf}} \leq C' e^{-c/g_k^{1/2}}$ is bounded via Weyl's eigenvalue inequality, but the exponent $1/g_k^{1/2}$ is *weaker* than the standard instanton suppression $8\pi^2/g_k^2$. This was previously flagged in r05 and r06 and is now closed by Section 5.5.3's explicit large-field handling.

**Impact on the claimed result:** Sound. Theorem 5 is a complete rigorous proof. Previous referees correctly identified this as SOUND. The remaining concern is the hand-off to Balaban's RG and the K-vs-k issue, which is treated separately in Point C1.
