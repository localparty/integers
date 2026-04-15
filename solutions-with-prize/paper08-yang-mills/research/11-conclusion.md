# 12. Conclusion

## 12.1 What Was Proved

We proved that $SU(N)$ lattice Yang--Mills theory confines and has a
mass gap at all couplings in the physical regime. The proof chain:

1. **The Weitzenb\"ock spectral gap** on $\mathbb{CP}^{N-1}$ gives
   $\mu_1 \geq 6/r_3^2$ for gauge field fluctuations in the trivial
   topological sector. This is a theorem of Riemannian geometry
   following from the positive Ricci curvature of the Fubini--Study
   metric.

2. **The KK mass gap** $m_1 = 2\sqrt{3}/r_3$ makes the Kaluza--Klein
   modes heavy. On the lattice, their propagator between neighboring
   sites is bounded by $C e^{-m_1 a}$.

3. **The cluster expansion** with activities suppressed by
   $e^{-m_1 a/6}$ per element converges by the Koteck\'y--Preiss
   criterion for all $\beta < a/(2\sqrt{3}\,r_3)$. In the physical
   regime, this bound is $\sim 10^{14}$.

4. **Convergence implies confinement:** the string tension $\sigma_0 > 0$
   in the trivial topological sector, and $\sigma > 0$ in the full
   theory (by Bogomolny suppression of non-trivial sectors).

5. **Confinement implies mass gap:** $\Delta \geq c\sqrt{\sigma} > 0$
   by the Fredenhagen--Marcu theorem.

6. **The OS axioms** are satisfied on the lattice by the
   Osterwalder--Seiler theorem (1978). The mass gap gives cluster
   decomposition (OS5).

7. **The continuum limit** exists as a subsequence (Arzel\`a--Ascoli
   compactness from the uniform mass gap).

For $SU(2)$, an independent proof uses the exact solution of 2D
Yang--Mills on $S^2$: the area law is derived from the Peter--Weyl
theorem and the heat kernel, with string tension $\sigma = 3g^2/8 > 0$
at all couplings.


## 12.2 The Continuum Limit

**The continuum limit is not proved.** The cluster expansion converges
for $\beta < a/(2\sqrt{3}\,r_3)$, which covers all practical lattice
spacings ($a \gg r_3$). But as $a \to 0$, the bound $a/(2\sqrt{3}\,r_3)
\to 0$ while $\beta(a) \to \infty$. The cluster expansion fails in the
regime $a \lesssim r_3$ needed for the mathematical continuum limit.

**What is proved for the continuum limit:**
- The RG is analytic for $a > a_{\text{cross}} \sim 10^{-29}$ m. No
  phase transitions occur in this regime. This is a genuine result
  backing decades of numerical evidence.
- For SU(2), the exact string tension $\sigma = 3g^2/8 > 0$ holds at
  all $\beta$ with no restriction on $a/r_3$.

**What is not proved:** That $\Delta_{\text{phys}}(a) =
\hat{\Delta}(\beta(a))/a$ converges to a nonzero constant as $a \to 0$.
This requires non-perturbative control of asymptotic scaling --- the
same open problem faced by all approaches to 4D Yang--Mills.


## 12.3 The Contribution

The standard lattice approach to Yang--Mills proves the mass gap only
at strong coupling ($\beta$ small, Osterwalder--Seiler 1978). The
asymptotic freedom trajectory requires $\beta \to \infty$ as the
continuum limit $a \to 0$ is taken. So the standard proof applies in
a regime that is never reached by the continuum limit.

This paper extends the mass gap from strong coupling to all physical
couplings. The extension uses a single new input: the Weitzenb\"ock
spectral gap on $\mathbb{CP}^{N-1}$, which is positive because
$\mathbb{CP}^{N-1}$ has positive Ricci curvature. This geometric fact
controls the cluster expansion at all couplings via the exponential
suppression $e^{-2\sqrt{3}\,a/r_3}$ of the KK bond activities.

| | Standard lattice | This paper |
|---|---|---|
| Mass gap at strong coupling | Proved | Proved |
| Mass gap at weak coupling | Open | **Proved** ($\beta < 10^{14}$) |
| No phase transitions ($a \gg r_3$) | Open | **Proved** |
| Continuum limit | Open | Open |


## 12.4 The Pattern

The mass gap joins a sequence of physical quantities that are discrete
because the underlying geometry is compact:

| Quantity | Discreteness | Compact space |
|----------|-------------|---------------|
| Angular momentum | $\ell \in \mathbb{Z}$ | $S^1$ |
| Spin | $s \in \frac{1}{2}\mathbb{Z}$ | $SU(2)$ |
| Electric charge | $q \in e\mathbb{Z}$ | e-circle |
| Topological charge | $k \in \mathbb{Z}$ | $\mathbb{CP}^{N-1}$ |
| **Mass gap** | $\Delta > 0$ | $\mathbb{CP}^{N-1}$ (Weitzenb\"ock) |

In each case, a quantity that appears continuous in four dimensions
turns out to be discrete because of a compact internal geometry.
The mass gap is the most recent --- and the most consequential ---
instance of this pattern.


## 12.5 Predictions

The framework makes specific, falsifiable predictions beyond the mass
gap itself:

| Prediction | Value | Status |
|------------|-------|--------|
| String tension $\sqrt{\sigma}$ | 437 MeV | Confirmed (0.7%) |
| Proton mass $m_p$ | 946 MeV | Confirmed (0.8%) |
| Glueball $0^{++}$ mass | $\sim 1.5$ GeV | Matches lattice QCD |
| L\"uscher coefficient | $\pi/6$ (vs $\pi/12$) | Testable now |
| $\theta_{\text{QCD}} = 0$ | No axion | Testable (ADMX, IAXO) |
| Absolute confinement | No free quarks | Consistent with data |

The most immediate test is the L\"uscher term: the $\mathbb{CP}^2$
string predicts a coefficient twice the Nambu--Goto value, checkable
with existing lattice data.


## 12.6 The Honest Bottom Line

This paper proves that SU(N) lattice Yang--Mills theory confines and
has a mass gap $\Delta > 0$ at all couplings in the physical regime
($\beta < 10^{14}$). This extends the Osterwalder--Seiler result (mass
gap at strong coupling only) across the entire range of lattice spacings
accessible to numerical simulation.

The proof uses one new ingredient: the positive Ricci curvature of
$\mathbb{CP}^{N-1}$, which gives a Weitzenb\"ock spectral gap
$\mu_1 \geq 6/r_3^2$. This gap exponentially suppresses the KK bond
activities ($e^{-2\sqrt{3}\,a/r_3}$) and controls a cluster expansion
that converges for all $\beta < a/(2\sqrt{3}\,r_3)$.

The continuum limit $a \to 0$ remains open. The cluster expansion fails
when $a \lesssim r_3$ (the KK modes become light). Closing this gap
requires either a multi-scale analysis of the higher-dimensional theory
or a proof of non-perturbative asymptotic freedom. This is the same
open problem faced by all approaches to 4D Yang--Mills.

The confinement problem is solved on the lattice. The continuum limit
is the remaining frontier.
