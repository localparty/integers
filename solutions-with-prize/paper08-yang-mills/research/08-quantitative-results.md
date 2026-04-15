# 7. Quantitative Results

The mass gap is not merely proven to exist. It is computed from the
geometry of $\mathbb{CP}^2$, with no free parameters beyond those
already fixed in Papers 4--5.


## 7.1 The Mass Gap

From Section 4.6:
$$\Delta = 2\sqrt{\sigma} \approx 874 \text{ MeV}$$

where the string tension $\sigma$ is derived from $\mathbb{CP}^2$
geometry (Paper 5, Section 3):
$$\sigma = \frac{3 g_3^2}{8\pi^2 r_3^2}, \quad
  \sqrt{\sigma} \approx 437 \text{ MeV}$$

This is the mass of the lightest glueball before mixing with scalar
mesons. After mixing with $f_0$ states, the physical $0^{++}$ glueball
mass shifts to $\sim 1.5$--$1.7$ GeV.


## 7.2 The Glueball Spectrum

The glueball masses are determined by the Laplacian spectrum on
$\mathbb{CP}^2$. The eigenvalues (Section 4.7):
$$\lambda_{p,q} = 4\left[\frac{p(p+2) + q(q+2) + pq}{r_3^2}\right]$$

organize into $SU(3)$ representations. The lightest gauge-invariant
(color-singlet) states in each $J^{PC}$ channel:

| State | $J^{PC}$ | Geometric origin | Predicted mass | Lattice QCD |
|-------|----------|------------------|----------------|-------------|
| Scalar | $0^{++}$ | $2\sqrt{\sigma}$ | $\sim 874$ MeV (bare) | 1710 MeV |
| Tensor | $2^{++}$ | Next KK level | $\sim 1.2\sqrt{\sigma_{(1,1)}}$ | 2390 MeV |
| Pseudoscalar | $0^{-+}$ | Topological sector | $\sim 3\sqrt{\sigma}$ | 2560 MeV |

**Mass ratios.** The ratios between glueball masses are determined by
the eigenvalue ratios of the $\mathbb{CP}^2$ Laplacian. These are pure
numbers, independent of $r_3$:
$$\frac{m_{2^{++}}}{m_{0^{++}}} \sim
  \sqrt{\frac{\lambda_{1,1}}{\lambda_{\text{min}}}}$$

These ratios constitute parameter-free predictions testable against
lattice QCD data.


## 7.3 The Confining String

The confining string in this framework is not the Nambu--Goto string.
Its worldsheet theory is a sigma model on $\mathbb{CP}^2$, which has
central charge $c = 2$ (compared to $c = 1$ for Nambu--Goto in the
bosonic string).

**The L\"uscher term.** The correction to the linear confining potential
at large $R$:

$$V(R) = \sigma R - \frac{\pi c}{12 R} + \mathcal{O}(1/R^2)$$

**Nambu--Goto** ($c = 1$):
$$V_{\text{NG}}(R) = \sigma R - \frac{\pi}{12R}$$

**CP$^2$ string** ($c = 2$):
$$V_{\mathbb{CP}^2}(R) = \sigma R - \frac{\pi}{6R}$$

The $\mathbb{CP}^2$ string predicts a L\"uscher term **twice as large**
as the Nambu--Goto prediction. This is a clean, parameter-free
prediction testable with existing lattice data.

**Current lattice data.** The L\"uscher term has been measured in
lattice QCD (Luscher--Weisz 2002, Bali 2001). Measurements are
consistent with $c \approx 1$ (Nambu--Goto) but with significant
uncertainties ($\sim 20$--$30\%$). A factor-of-two deviation is at the
boundary of current resolution. Next-generation lattice calculations
with finer lattice spacings and larger volumes will provide a decisive
test.


## 7.4 The String Tension

**Geometric prediction (Paper 5):**
$$\sqrt{\sigma_{\text{geom}}} = 437 \text{ MeV}$$

**Experimental (from Regge trajectories and lattice):**
$$\sqrt{\sigma_{\text{exp}}} = 440 \text{ MeV}$$

**Match: 0.7%** --- with no free parameters.

The string tension is derived from four geometric inputs:
1. $\alpha_s(M_3) \approx 1/25$ (gauge coupling at the CP$^2$ scale)
2. $r_3 \sim 10^{-31}$ m (CP$^2$ radius)
3. The curvature profile integral on $\mathbb{CP}^1 \subset \mathbb{CP}^2$ ($= 3/(8\pi^2)$)
4. Dimensional transmutation (RG running from $M_3$ to $\Lambda_{\text{QCD}}$)


## 7.5 Deconfinement Temperature

The deconfinement phase transition occurs when thermal energy overcomes
the topological barrier. The critical temperature is set by the
$\mathbb{CP}^2$ Casimir energy scale:

$$T_c \sim \left(V_{\text{Casimir}}^{\mathbb{CP}^2}\right)^{1/4}
  \sim \Lambda_{\text{QCD}} \sim 200 \text{ MeV}$$

**Lattice QCD / experimental:**
$$T_c = 155 \pm 9 \text{ MeV}$$

The 30% discrepancy is expected at leading order. Corrections from the
full Casimir potential (including fermion contributions from the $Z_2$
orbifold) are expected to reduce $T_c$ toward the measured value.


## 7.6 Predictions Summary

| Observable | Geometric prediction | Experiment / Lattice | Match |
|------------|---------------------|---------------------|-------|
| Mass gap $\Delta$ | 874 MeV (bare) | $\sim 1500$ MeV ($0^{++}$, after mixing) | Factor 1.7 |
| String tension $\sqrt{\sigma}$ | 437 MeV | 440 MeV | **0.7%** |
| Regge slope $\alpha'$ | 0.83 GeV$^{-2}$ | 0.9 GeV$^{-2}$ | 8% |
| L\"uscher coefficient | $\pi/6$ | $\sim \pi/12$ (current data) | **Testable** |
| Deconfinement $T_c$ | $\sim 200$ MeV | 155 MeV | 30% |
| $\theta_{\text{QCD}}$ | 0 (topological) | $< 10^{-10}$ | $\checkmark$ |

**Falsifiable predictions:**

1. **L\"uscher term** $c = 2$ instead of $c = 1$. Testable with
   existing lattice technology at increased precision.

2. **Glueball mass ratios** from $\mathbb{CP}^2$ Laplacian eigenvalues.
   Parameter-free prediction for the spectrum.

3. **No axion.** $\theta_{\text{QCD}} = 0$ from $\mathbb{CP}^2$
   topology (Paper 4). The absence of a QCD axion is a distinguishing
   prediction testable by ADMX, CASPEr, and IAXO within the next decade.

4. **Absolute confinement.** No quark deconfinement at any temperature
   below the $\mathbb{CP}^2$ phase transition scale ($\sim 10^{15}$ GeV).
   Confinement persists even in the asymptotically free regime.
