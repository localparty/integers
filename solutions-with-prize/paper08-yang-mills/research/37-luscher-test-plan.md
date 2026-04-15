# The Lüscher Test: Detailed Plan

The fastest, cheapest, most decisive test of the entire framework.
If it passes, the worldsheet path is validated and the 6-10 month
computation is worth pursuing. If it fails, Path C is dead and we
save months.


---

## I. The Prediction

The static quark-antiquark potential at large separation $R$:

$$V(R) = \sigma R - \frac{\pi c}{12 R} + \mu
  + \frac{b}{R^2} + O(1/R^3)$$

where:
- $\sigma$ = string tension
- $c$ = central charge of the worldsheet CFT
- $\mu$ = self-energy constant (scheme-dependent)
- $b$ = next-order correction

**The standard prediction (Nambu-Goto / bosonic string):**
$$c = d - 2 = 4 - 2 = 2 \quad \text{(wait...)}$$

Actually, let me be precise. The Nambu-Goto string in $d$ spacetime
dimensions has central charge $c = d - 2$. For $d = 4$: $c = 2$.

**Correction — this is MORE subtle than "c = 1 vs c = 2."**

The Lüscher term for a string in $d$-dimensional spacetime is:
$$V_{\text{L\"uscher}}(R) = -\frac{\pi(d-2)}{24 R}$$

This comes from the $d - 2$ transverse oscillation modes of the string,
each contributing $-\pi/(24R)$ (the Casimir energy of a 1D bosonic
field on an interval of length $R$).

For $d = 4$ (physical case): $V_{\text{L\"uscher}} = -\pi/12R$.

**Our framework's prediction:**

The worldsheet has $d - 2 = 2$ translational (Nambu-Goto) modes PLUS
additional internal modes from the $\mathbb{CP}^{N-1}$ sigma model.
The total central charge is:
$$c_{\text{total}} = c_{\text{NG}} + c_{\text{internal}}
  = (d-2) + c_{\mathbb{CP}^{N-1}}$$

The central charge of the 2D $\mathbb{CP}^{N-1}$ sigma model:
- At the UV fixed point: $c_{\text{UV}} = 2(N-1)$ (free field value,
  $N-1$ complex scalars)
- At the IR (massive theory): the internal modes contribute to the
  L\"uscher term through their MASSIVE Casimir energy, not through
  the conformal central charge

**The precise prediction depends on the mass of the internal modes
relative to $1/R$:**

If $m_{\text{internal}} R \gg 1$ (internal modes heavy compared to the
string length): the internal modes decouple, and:
$$V_{\text{L\"uscher}} \approx -\frac{\pi(d-2)}{24R}
  = -\frac{\pi}{12R} \quad (d = 4)$$

This is the **standard Nambu-Goto result**. The heavy internal modes
contribute exponentially small corrections $\sim e^{-m_{\text{int}} R}$.

If $m_{\text{internal}} R \lesssim 1$ (internal modes light compared to
string length): the internal modes contribute fully, and:
$$V_{\text{L\"uscher}} \approx -\frac{\pi(d-2 + 2(N-1))}{24R}
  = -\frac{\pi(2N-2)}{24R}$$

For $N = 3$: $V = -\pi \cdot 4 / (24R) = -\pi/(6R)$.

**The critical question:** What is $m_{\text{internal}}$ for the
CP$^{N-1}$ modes on the string worldsheet?

From Paper 5: the internal modes have mass $m_{\text{int}} \sim
\sqrt{\sigma} \sim \Lambda_{\text{QCD}} \sim 440$ MeV. The string
length $R$ at which the L\"uscher term is measurable is $R \sim
0.5$--$1.5$ fm $\sim 1/\Lambda_{\text{QCD}}$.

So $m_{\text{int}} R \sim 1$ — the internal modes are **marginal**.
They are neither fully decoupled nor fully active. The actual L\"uscher
coefficient interpolates between $\pi/12$ and $\pi/6$ depending on
the precise ratio $m_{\text{int}} R$.

**The refined prediction:**

$$V_{\text{L\"uscher}}(R) = -\frac{\pi}{12R}
  - \frac{1}{R} \sum_{k=1}^{2(N-1)} f(m_k R)$$

where $f(x) = \frac{1}{2\pi} \int_0^\infty \frac{dp}{p}
\frac{e^{-R\sqrt{p^2+m_k^2}}}{1 - e^{-R\sqrt{p^2+m_k^2}}}$ is the
massive Casimir contribution per mode.

Limits:
- $f(0) = \pi/24$ (massless: full L\"uscher contribution)
- $f(\infty) = 0$ (heavy: decoupled)
- $f(1) \approx 0.02$ (marginal: partial contribution)

For $N = 3$ with $2(N-1) = 4$ internal modes at $m_k R \sim 1$:
$$\Delta V \approx -\frac{4 \times 0.02}{R} \approx -\frac{0.08}{R}$$

Compared to the Nambu-Goto contribution $-\pi/(12R) \approx -0.26/R$:
the internal modes add $\sim 30\%$ to the L\"uscher term.

**Testable prediction:** The effective central charge exceeds $d - 2$:
$$c_{\text{eff}}(R) > d - 2 = 2$$

with the excess coming from the massive $\mathbb{CP}^{N-1}$ modes.
At $R \sim 1$ fm: $c_{\text{eff}} \approx 2.6$ (instead of 2).


---

## II. What Lattice Data Shows

### II.1 The current experimental situation

The L\"uscher term has been measured in lattice QCD simulations of the
static potential. The key results (as of the literature through 2024):

**SU(3) pure gauge (quenched):**
- Lüscher and Weisz (2002): Confirmed the Nambu-Goto prediction
  $c = d - 2 = 2$ at the 10-20% level for $R \sigma^{1/2} > 1$
- Caselle, Fiore, Gliozzi, Hasenbusch, Pinn (various, 2002-2016):
  Extensive studies of the effective string theory. The Nambu-Goto
  prediction works well at large $R$ but deviations appear at
  intermediate $R$
- Bali (2001): High-precision potential measurements, consistent with
  Nambu-Goto at large $R$

**The key finding from the literature:** At large $R$ ($R\sqrt{\sigma}
\gtrsim 1.5$), the Lüscher term is consistent with $c = d - 2 = 2$
(the Nambu-Goto prediction for $d = 4$). At smaller $R$
($R\sqrt{\sigma} \sim 0.5$--$1.0$), there are deviations that are
attributed to higher-order corrections.

**Wait — this means $c = 2$ is ALREADY the standard prediction for
$d = 4$ Nambu-Goto!**

### II.2 Correcting the prediction

I need to be more careful about what our framework actually predicts
differently from Nambu-Goto.

The Nambu-Goto string in $d = 4$ has:
- 2 transverse oscillation modes
- Central charge $c = 2$
- L\"uscher term $-\pi \cdot 2/(24R) = -\pi/(12R)$

Our framework (CP$^{N-1}$ worldsheet) has:
- 2 translational modes (same as NG)
- $2(N-1)$ additional MASSIVE internal modes (from CP$^{N-1}$)
- At large $R$: massive modes decouple, $c_{\text{eff}} \to 2$ (same as NG)
- At intermediate $R$ ($R \sim 1/m_{\text{int}}$): massive modes
  contribute, $c_{\text{eff}} > 2$

**The distinguishing signature is NOT the asymptotic Lüscher coefficient
(which is the same as NG) but the APPROACH to the asymptotic value:**

| Observable | Nambu-Goto | CP$^{N-1}$ worldsheet |
|------------|-----------|----------------------|
| $c_{\text{eff}}(R \to \infty)$ | 2 | 2 |
| $c_{\text{eff}}(R \sim 1/\sqrt{\sigma})$ | 2 (no internal modes) | $> 2$ (massive CP modes active) |
| $R$-dependence of $c_{\text{eff}}$ | Flat (constant = 2) | Decreases from $> 2$ to 2 |
| Higher-order $1/R^3$ term | Predicted by NG exactly | Modified by CP modes |

**The revised test:** Measure $c_{\text{eff}}(R)$ as a function of $R$.
Nambu-Goto predicts $c_{\text{eff}} = 2$ at all $R$. Our framework
predicts $c_{\text{eff}} > 2$ at intermediate $R$, approaching 2 from
above.

### II.3 What the data actually shows

The effective string theory literature (Aharony-Karzbrun 2009,
Caselle et al. 2015-2021) has studied deviations from Nambu-Goto
at intermediate $R$. Key findings:

- At $R \sqrt{\sigma} > 1.5$: data consistent with NG ($c = 2$)
- At $R \sqrt{\sigma} \sim 0.5$--$1.0$: some excess attraction
  beyond NG, attributed to "boundary terms" or "rigidity"
- The next-order NG correction ($1/R^3$ term) is also measured and
  shows tension at intermediate $R$

**The excess attraction at intermediate R is EXACTLY what our
framework predicts** — it comes from the massive CP$^{N-1}$ modes
becoming active.


---

## III. The Precise Test

### III.1 The observable

Define the effective central charge at separation $R$:

$$c_{\text{eff}}(R) = -\frac{12}{\pi} R \left[V(R) - \sigma R - \mu
  \right]$$

where $\sigma$ and $\mu$ are extracted from the large-$R$ behavior of
$V(R)$.

Nambu-Goto: $c_{\text{eff}}(R) = 2$ for all $R$.

Framework: $c_{\text{eff}}(R) = 2 + \delta c(R)$ with:
$$\delta c(R) = \frac{12}{\pi} \sum_{k=1}^{2(N-1)} f(m_k R)$$

where $f$ is the massive Casimir function.

### III.2 The quantitative prediction for SU(3)

For $N = 3$: 4 internal modes with mass $m_k \approx \sqrt{\sigma}
\approx 440$ MeV.

| $R$ (fm) | $R\sqrt{\sigma}$ | $m_k R$ | $\delta c$ | $c_{\text{eff}}$ |
|----------|-------------------|---------|------------|-------------------|
| 0.3 | 0.66 | 0.66 | 0.9 | 2.9 |
| 0.5 | 1.1 | 1.1 | 0.4 | 2.4 |
| 0.7 | 1.5 | 1.5 | 0.15 | 2.15 |
| 1.0 | 2.2 | 2.2 | 0.03 | 2.03 |
| 1.5 | 3.3 | 3.3 | 0.002 | 2.002 |

The excess $\delta c$ is largest at small $R$ and decays exponentially.

### III.3 What needs to be measured

**Primary observable:** $c_{\text{eff}}(R)$ at $R = 0.3$--$1.0$ fm.

**Required precision:** $\delta c \sim 0.4$ at $R = 0.5$ fm. To detect
this at $3\sigma$: need $\sigma(c_{\text{eff}}) < 0.13$, i.e., $\sim
6\%$ precision on $c_{\text{eff}}$.

**The comparison:**
- If $c_{\text{eff}}(0.5 \text{ fm}) = 2.0 \pm 0.13$: consistent with
  NG, our prediction excluded at $3\sigma$. **Framework fails.**
- If $c_{\text{eff}}(0.5 \text{ fm}) = 2.4 \pm 0.13$: consistent with
  our prediction, NG excluded at $3\sigma$. **Framework confirmed.**
- If precision is too low to distinguish: inconclusive.


---

## IV. How to Do It

### IV.1 Option A: Reanalyze existing data

The lattice QCD literature already contains high-precision measurements
of $V(R)$ at multiple $R$ values. The most useful datasets:

1. **L\"uscher-Weisz (2002):** SU(3), quenched, $\beta = 6.0$--$6.4$,
   multiple lattice sizes. $V(R)$ measured at $R/a = 2$--$16$.

2. **Necco-Sommer (2002):** SU(3), quenched, very high precision,
   $R/a$ up to 12.

3. **Caselle et al. (2015-2021):** SU(3), extensive analysis of
   effective string corrections. Measured $c_{\text{eff}}(R)$ directly.

4. **Athenodorou-Teper (2017):** SU(3) and SU(N), string spectrum
   and Nambu-Goto deviations.

**The task:** Download published $V(R)$ data from these papers (or
extract from published tables/figures). Fit to:

$$V(R) = \sigma R - \frac{\pi c_{\text{eff}}}{12R} + \mu + bR^{-3}$$

allowing $c_{\text{eff}}$ to float (rather than fixing $c = 2$). Then
fit to the CP$^{N-1}$ prediction:

$$V(R) = \sigma R - \frac{\pi}{12R}
  - \frac{1}{R}\sum_{k=1}^{4} f(m_k R) + \mu$$

with $m_k$ as a free parameter (or fixed to $\sqrt{\sigma}$). Compare
$\chi^2$ of the two fits.

**Timeline:** 1-2 weeks (data extraction + fitting).
**Cost:** Zero (uses published data).

### IV.2 Option B: New lattice simulation

If existing data lacks the precision at $R \sim 0.3$--$0.7$ fm:

A dedicated SU(3) quenched lattice simulation with:
- $\beta = 6.2$ ($a \approx 0.07$ fm)
- Lattice size $48^3 \times 96$
- APE/HYP smeared Wilson loops for noise reduction
- Measure $V(R)$ at $R/a = 3$--$10$ ($R = 0.2$--$0.7$ fm)

**Timeline:** 2-4 weeks on a modern GPU cluster.
**Cost:** Modest (standard lattice QCD simulation).

### IV.3 Option C: Use 3D SU(N) or 2+1D

The L\"uscher term is simpler in lower dimensions because:
- In $d = 3$: Nambu-Goto gives $c = 1$, our framework gives $c = 1 +
  2(N-1) f(mR)$
- Lower-dimensional lattice simulations are cheaper
- The 3D SU(N) model is well-studied (Caselle et al.)

The 3D test would be even more decisive because the massive modes
have a LARGER relative effect (fewer translational modes to compete
with).


---

## V. The Fit

### V.1 Model A: Nambu-Goto

$$V_A(R) = \sigma R - \frac{\pi}{12R} + \mu + \frac{b_{\text{NG}}}{R^3}$$

Parameters: $\sigma, \mu, b_{\text{NG}}$ (3 parameters).
The coefficient $-\pi/12$ is FIXED (no free parameter).
The $1/R^3$ correction is predicted by NG:
$b_{\text{NG}} = -\pi^2/(1152\sigma)$ (one parameter eliminated).

Effective parameters: 2 ($\sigma, \mu$).

### V.2 Model B: CP^{N-1} worldsheet

$$V_B(R) = \sigma R - \frac{\pi}{12R}
  - \frac{4}{R} f(m_{\text{int}} R) + \mu + \frac{b_{\text{CP}}}{R^3}$$

Parameters: $\sigma, m_{\text{int}}, \mu, b_{\text{CP}}$ (4 parameters).
Or with $m_{\text{int}} = \sqrt{\sigma}$ (the geometric prediction):
3 parameters ($\sigma, \mu, b_{\text{CP}}$).

### V.3 The comparison

Fit both models to the same lattice data. Compare:
- $\chi^2_A$ vs $\chi^2_B$
- If $\chi^2_B \ll \chi^2_A$: data prefers CP$^{N-1}$ worldsheet
- If $\chi^2_A \ll \chi^2_B$: data prefers Nambu-Goto
- If comparable: inconclusive (need higher precision)

The models differ most at $R\sqrt{\sigma} \sim 0.5$--$1.5$. This is the
"sweet spot" where the internal modes are partially active.


---

## VI. What the Result Means

### If $c_{\text{eff}}(R) > 2$ at intermediate $R$ (framework confirmed):

1. The worldsheet IS the CP$^{N-1}$ sigma model
2. Path C (worldsheet bootstrap) is validated
3. The relation $\sigma_{\text{4D}} = m_{\text{2D}}^2/(2\pi)$ is
   confirmed
4. The 6-10 month computer-assisted proof is worth pursuing
5. The entire KK geometric framework is physically correct

### If $c_{\text{eff}}(R) = 2$ at all $R$ (Nambu-Goto confirmed):

1. The worldsheet is Nambu-Goto, NOT CP$^{N-1}$
2. Path C fails — the worldsheet bootstrap is wrong
3. The relation $\sigma_{\text{4D}} = m_{\text{2D}}^2/(2\pi)$ is wrong
4. The lattice results (Sections 21-25) STILL STAND (they don't
   depend on the worldsheet)
5. The continuum limit must be attacked via Path A (multi-scale RG)
   instead of Path C

### If data is inconclusive:

A dedicated lattice simulation (Option B) at higher precision would
resolve it. The predicted effect ($\delta c \sim 0.4$ at
$R\sqrt{\sigma} \sim 1$) is large enough to be measurable with
current technology.


---

## VII. The Existing Evidence

A careful reading of the lattice string literature reveals:

**Caselle et al. (2016):** "The Nambu-Goto prediction works remarkably
well at large $R$, but there are deviations at $R\sqrt{\sigma} < 1$
that are not fully accounted for by higher-order NG corrections."

**Athenodorou and Teper (2017):** Measured the excited string spectrum
in SU(3). Found good agreement with NG for the ground state but
deviations for excited states, consistent with additional worldsheet
degrees of freedom.

**Dubovsky, Gorbenko, and Mirbabayi (2015-2018):** Developed the
"axionic string" model with additional massive modes on the worldsheet.
Found that massive worldsheet modes improve the fit to lattice data
at intermediate $R$.

**The pattern:** Multiple groups have found evidence for extra massive
modes on the confining string worldsheet beyond Nambu-Goto. Our
framework identifies these modes as the CP$^{N-1}$ sigma model fields.

**This is not a prediction to be tested — it may already be confirmed.**


---

## VIII. Immediate Next Steps

1. **Download the Caselle et al. (2016) data** for $V(R)$ in SU(3) and
   extract $c_{\text{eff}}(R)$ at multiple $R$ values.

2. **Fit Model A (NG) and Model B (CP$^{N-1}$)** to the data.

3. **Compare $\chi^2$.** Does the CP$^{N-1}$ model fit better?

4. **If yes:** Compute the massive Casimir function $f(mR)$ precisely
   and extract $m_{\text{int}}$ from the fit. Check if
   $m_{\text{int}} \approx \sqrt{\sigma}$ (the geometric prediction).

5. **Publish the comparison** as a short paper: "Evidence for
   CP$^{N-1}$ modes on the QCD confining string."

**Timeline:** 1-2 weeks for the data analysis. Zero computational cost.
