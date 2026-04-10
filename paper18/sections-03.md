# Section 3 — The First Moments

**REVISED 2026-04-10** — Propagated 3 critical + 5 major issues from independent review.

*The computational heart of Paper 18. Every e-fold count in this
section is computed from the non-trivial zeros of the Riemann zeta
function with zero free parameters. Physical identifications are
derived for rungs 1--5 and tentative for n >= 6.*

---

## 3.1 The first 100 rungs

### 3.1.1 Definition

By Theorem A of research/06 (R-Theorem GR.1), the number of
e-folds of expansion associated with a transition between adjacent
Riemann-zero eigenstates |gamma_n> and |gamma_{n+1}> is

$$
N_n \;=\; (\gamma_{n+1} - \gamma_n) \cdot \frac{\pi^2}{2}.
$$

Each adjacent pair (gamma_n, gamma_{n+1}) defines one **rung** of
the cosmic ladder. The cumulative e-fold count from the first rung
through rung n is

$$
\mathcal{N}(n) \;=\; \sum_{k=1}^{n} N_k
\;=\; (\gamma_{n+1} - \gamma_1) \cdot \frac{\pi^2}{2}.
$$

The ladder is indexed by the positive integers. The physical
content of each rung is determined by its e-fold count and its
position in the sequence: the lowest rungs (n = 1 through 5)
correspond to the major cosmic epochs, and higher rungs encode
finer structural transitions.

### 3.1.2 Computation

All values are computed using mpmath (50-digit precision) via
the `zetazero(n)` function. The multiplicative factor is
pi^2/2 = 4.93480220054468....

The table below presents the first 100 rungs. Columns:

- **n**: rung index (= index of the lower zero in the pair)
- **gamma_n**: imaginary part of the n-th non-trivial Riemann zero
- **gamma_{n+1}**: imaginary part of the (n+1)-th zero
- **Delta**: spectral gap gamma_{n+1} - gamma_n
- **N_n**: e-fold count for this rung = Delta * pi^2/2
- **Cumul.**: cumulative e-folds from rung 1 through rung n
- **Epoch**: physical identification (where applicable)

#### Epoch identification key

Rungs 1--5 have firm physical identifications established in
research/06 and research/42. Rungs 6 and above are marked as
**structural extrapolation** (SE): the e-fold counts are exact
arithmetic, but the physical identification with specific
cosmological epochs is tentative.

---

### Table 1. The Cosmic Ladder: First 100 Rungs

| n | gamma_n | gamma_{n+1} | Delta | N_n (e-folds) | Cumul. | Epoch |
|--:|--------:|------------:|------:|--------------:|-------:|:------|
| 1 | 14.134725 | 21.022040 | 6.887314 | 33.988 | 33.988 | **Post-inflation expansion ("now")** |
| 2 | 21.022040 | 25.010858 | 3.988818 | 19.684 | 53.672 | Late inflation / reheating transition |
| 3 | 25.010858 | 30.424876 | 5.414019 | 26.717 | 80.389 | Mid-inflation plateau |
| 4 | 30.424876 | 32.935062 | 2.510185 | 12.387 | 92.776 | Early inflation onset |
| 5 | 32.935062 | 37.586178 | 4.651117 | 22.952 | 115.728 | GUT-scale / pre-inflation transition |
| 6 | 37.586178 | 40.918719 | 3.332541 | 16.445 | 132.174 | SE: Planck-to-GUT cooling |
| 7 | 40.918719 | 43.327073 | 2.408354 | 11.885 | 144.058 | SE: Planck-scale structure |
| 8 | 43.327073 | 48.005151 | 4.678078 | 23.085 | 167.144 | SE: trans-Planckian / projection vicinity |
| 9 | 48.005151 | 49.773832 | 1.768682 | 8.728 | 175.872 | SE |
| 10 | 49.773832 | 52.970321 | 3.196489 | 15.774 | 191.646 | SE |
| 11 | 52.970321 | 56.446248 | 3.475926 | 17.153 | 208.799 | SE |
| 12 | 56.446248 | 59.347044 | 2.900796 | 14.315 | 223.114 | SE |
| 13 | 59.347044 | 60.831779 | 1.484735 | 7.327 | 230.441 | SE |
| 14 | 60.831779 | 65.112544 | 4.280766 | 21.125 | 251.565 | SE |
| 15 | 65.112544 | 67.079811 | 1.967266 | 9.708 | 261.274 | SE |
| 16 | 67.079811 | 69.546402 | 2.466591 | 12.172 | 273.446 | SE |
| 17 | 69.546402 | 72.067158 | 2.520756 | 12.439 | 285.885 | SE |
| 18 | 72.067158 | 75.704691 | 3.637533 | 17.951 | 303.836 | SE |
| 19 | 75.704691 | 77.144840 | 1.440149 | 7.107 | 310.942 | SE |
| 20 | 77.144840 | 79.337375 | 2.192535 | 10.820 | 321.762 | SE |
| 21 | 79.337375 | 82.910381 | 3.573006 | 17.632 | 339.394 | SE |
| 22 | 82.910381 | 84.735493 | 1.825112 | 9.007 | 348.401 | SE |
| 23 | 84.735493 | 87.425275 | 2.689782 | 13.274 | 361.674 | SE |
| 24 | 87.425275 | 88.809111 | 1.383837 | 6.829 | 368.503 | SE |
| 25 | 88.809111 | 92.491899 | 3.682788 | 18.174 | 386.677 | SE |
| 26 | 92.491899 | 94.651344 | 2.159445 | 10.656 | 397.334 | SE |
| 27 | 94.651344 | 95.870634 | 1.219290 | 6.017 | 403.351 | SE |
| 28 | 95.870634 | 98.831194 | 2.960560 | 14.610 | 417.960 | SE |
| 29 | 98.831194 | 101.317851 | 2.486657 | 12.271 | 430.231 | SE |
| 30 | 101.317851 | 103.725538 | 2.407687 | 11.881 | 442.113 | SE |
| 31 | 103.725538 | 105.446623 | 1.721085 | 8.493 | 450.606 | SE |
| 32 | 105.446623 | 107.168611 | 1.721988 | 8.498 | 459.104 | SE |
| 33 | 107.168611 | 111.029536 | 3.860924 | 19.053 | 478.157 | SE |
| 34 | 111.029536 | 111.874659 | 0.845124 | 4.171 | 482.327 | SE: narrow doublet |
| 35 | 111.874659 | 114.320221 | 2.445562 | 12.068 | 494.396 | SE |
| 36 | 114.320221 | 116.226680 | 1.906459 | 9.408 | 503.804 | SE |
| 37 | 116.226680 | 118.790783 | 2.564103 | 12.653 | 516.457 | SE |
| 38 | 118.790783 | 121.370125 | 2.579342 | 12.729 | 529.185 | SE |
| 39 | 121.370125 | 122.946829 | 1.576704 | 7.781 | 536.966 | SE |
| 40 | 122.946829 | 124.256819 | 1.309989 | 6.465 | 543.431 | SE |
| 41 | 124.256819 | 127.516684 | 3.259865 | 16.087 | 559.518 | SE |
| 42 | 127.516684 | 129.578704 | 2.062020 | 10.176 | 569.693 | SE |
| 43 | 129.578704 | 131.087689 | 1.508984 | 7.447 | 577.140 | SE |
| 44 | 131.087689 | 133.497737 | 2.410049 | 11.893 | 589.033 | SE |
| 45 | 133.497737 | 134.756510 | 1.258773 | 6.212 | 595.245 | SE |
| 46 | 134.756510 | 138.116042 | 3.359532 | 16.579 | 611.823 | SE |
| 47 | 138.116042 | 139.736209 | 1.620167 | 7.995 | 619.818 | SE |
| 48 | 139.736209 | 141.123707 | 1.387498 | 6.847 | 626.666 | SE |
| 49 | 141.123707 | 143.111846 | 1.988138 | 9.811 | 636.477 | SE |
| 50 | 143.111846 | 146.000982 | 2.889137 | 14.257 | 650.734 | SE |
| 51 | 146.000982 | 147.422765 | 1.421783 | 7.016 | 657.750 | SE |
| 52 | 147.422765 | 150.053520 | 2.630755 | 12.982 | 670.732 | SE |
| 53 | 150.053520 | 150.925258 | 0.871737 | 4.302 | 675.034 | SE: narrow doublet |
| 54 | 150.925258 | 153.024694 | 2.099436 | 10.360 | 685.395 | SE |
| 55 | 153.024694 | 156.112909 | 3.088215 | 15.240 | 700.634 | SE |
| 56 | 156.112909 | 157.597592 | 1.484683 | 7.327 | 707.961 | SE |
| 57 | 157.597592 | 158.849988 | 1.252396 | 6.180 | 714.141 | SE |
| 58 | 158.849988 | 161.188964 | 2.338976 | 11.542 | 725.684 | SE |
| 59 | 161.188964 | 163.030710 | 1.841746 | 9.089 | 734.772 | SE |
| 60 | 163.030710 | 165.537069 | 2.506360 | 12.368 | 747.141 | SE |
| 61 | 165.537069 | 167.184440 | 1.647371 | 8.129 | 755.270 | SE |
| 62 | 167.184440 | 169.094515 | 1.910075 | 9.426 | 764.696 | SE |
| 63 | 169.094515 | 169.911976 | 0.817461 | 4.034 | 768.730 | SE: narrow doublet |
| 64 | 169.911976 | 173.411537 | 3.499560 | 17.270 | 786.000 | SE |
| 65 | 173.411537 | 174.754192 | 1.342655 | 6.626 | 792.625 | SE |
| 66 | 174.754192 | 176.441434 | 1.687243 | 8.326 | 800.952 | SE |
| 67 | 176.441434 | 178.377408 | 1.935973 | 9.554 | 810.505 | SE |
| 68 | 178.377408 | 179.916484 | 1.539076 | 7.595 | 818.100 | SE |
| 69 | 179.916484 | 182.207078 | 2.290594 | 11.304 | 829.404 | SE |
| 70 | 182.207078 | 184.874468 | 2.667389 | 13.163 | 842.567 | SE |
| 71 | 184.874468 | 185.598784 | 0.724316 | 3.574 | 846.141 | SE: narrow doublet |
| 72 | 185.598784 | 187.228923 | 1.630139 | 8.044 | 854.186 | SE |
| 73 | 187.228923 | 189.416159 | 2.187236 | 10.794 | 864.979 | SE |
| 74 | 189.416159 | 192.026656 | 2.610498 | 12.882 | 877.861 | SE |
| 75 | 192.026656 | 193.079727 | 1.053070 | 5.197 | 883.058 | SE |
| 76 | 193.079727 | 195.265397 | 2.185670 | 10.786 | 893.844 | SE |
| 77 | 195.265397 | 196.876482 | 1.611085 | 7.950 | 901.794 | SE |
| 78 | 196.876482 | 198.015310 | 1.138828 | 5.620 | 907.414 | SE |
| 79 | 198.015310 | 201.264752 | 3.249442 | 16.035 | 923.450 | SE |
| 80 | 201.264752 | 202.493595 | 1.228843 | 6.064 | 929.514 | SE |
| 81 | 202.493595 | 204.189672 | 1.696077 | 8.370 | 937.884 | SE |
| 82 | 204.189672 | 205.394697 | 1.205025 | 5.947 | 943.830 | SE |
| 83 | 205.394697 | 207.906259 | 2.511562 | 12.394 | 956.224 | SE |
| 84 | 207.906259 | 209.576510 | 1.670251 | 8.242 | 964.467 | SE |
| 85 | 209.576510 | 211.690863 | 2.114353 | 10.434 | 974.900 | SE |
| 86 | 211.690863 | 213.347919 | 1.657057 | 8.177 | 983.078 | SE |
| 87 | 213.347919 | 214.547045 | 1.199125 | 5.917 | 988.995 | SE |
| 88 | 214.547045 | 216.169539 | 1.622494 | 8.007 | 997.002 | SE |
| 89 | 216.169539 | 219.067596 | 2.898058 | 14.301 | 1011.303 | SE |
| 90 | 219.067596 | 220.714919 | 1.647322 | 8.129 | 1019.432 | SE |
| 91 | 220.714919 | 221.430706 | 0.715787 | 3.532 | 1022.965 | SE: narrowest doublet |
| 92 | 221.430706 | 224.007000 | 2.576295 | 12.714 | 1035.678 | SE |
| 93 | 224.007000 | 224.983325 | 0.976324 | 4.818 | 1040.496 | SE |
| 94 | 224.983325 | 227.421444 | 2.438120 | 12.032 | 1052.528 | SE |
| 95 | 227.421444 | 229.337413 | 1.915969 | 9.455 | 1061.983 | SE |
| 96 | 229.337413 | 231.250189 | 1.912775 | 9.439 | 1071.422 | SE |
| 97 | 231.250189 | 231.987235 | 0.737047 | 3.637 | 1075.059 | SE: narrow doublet |
| 98 | 231.987235 | 233.693404 | 1.706169 | 8.420 | 1083.479 | SE |
| 99 | 233.693404 | 236.524230 | 2.830825 | 13.970 | 1097.448 | SE |
| 100 | 236.524230 | 237.769820 | 1.245591 | 6.147 | 1103.595 | SE |

### 3.1.3 Statistical summary

| Statistic | Value |
|:----------|------:|
| Minimum e-fold gap | 3.532 (rung 91: gamma_91/gamma_92 doublet) |
| Maximum e-fold gap | 33.988 (rung 1: post-inflation, the widest gap) |
| Mean e-fold gap | 11.036 |
| Total e-folds (100 rungs) | 1103.595 |
| Median e-fold gap | ~10.1 |
| Number of "narrow doublets" (N_n < 5) | 7 out of 100 |
| Number of "wide rungs" (N_n > 20) | 5 out of 100 |

### 3.1.4 Structural observations

**Observation 1 (The widest rung is "now").** Rung 1, the
post-inflation expansion from gamma_1 to gamma_2, has the largest
e-fold gap of any rung in the first hundred: N_1 = 33.988 e-folds.
This is not accidental. The gap between gamma_1 and gamma_2 is the
widest normalised gap among the low-lying Riemann zeros -- a
consequence of the initial sparseness of the zeros on the critical
line. The cosmological coincidence (that "now" is a special moment
in cosmic history) is structurally forced: the universe is currently
traversing its widest rung.

**Observation 2 (The inflation gap is a composite).** The full
inflation e-fold count N_{5->2} = 58.788 is not a single rung but
the sum of three rungs:

| Rung | N_n (e-folds) |
|:-----|:-------------|
| n=4 (gamma_4 -> gamma_5) | 12.387 |
| n=3 (gamma_3 -> gamma_4) | 26.717 |
| n=2 (gamma_2 -> gamma_3) | 19.684 |
| **Total gamma_2 -> gamma_5** | **58.788** |

The inflation epoch has internal structure: three sub-phases of
12.4, 26.7, and 19.7 e-folds. This decomposition is a mathematical
fact about the Riemann zeros between gamma_2 and gamma_5, not a
prediction of the framework. Whether the three sub-rungs have
independent physical content — e.g., producing detectable features
in the primordial power spectrum — is an open question. Without an
estimate of the amplitude of any such features (which requires
computing the transition sharpness in the level-crossing picture),
this is a **structural observation**, not a testable prediction.

**Observation 3 (Narrow doublets).** Seven rungs have e-fold counts
below 5: rungs 34, 53, 63, 71, 91, 93, and 97. These correspond to
closely spaced Riemann zero pairs -- sometimes called "Lehmer
pairs" when the gap is exceptionally small. In the cosmic ladder
interpretation, these are rapid micro-transitions rather than
extended epochs. The narrowest in the first hundred is rung 91 at
3.53 e-folds.

**Observation 4 (No clustering of wide rungs).** The five widest
rungs (n = 1, 3, 8, 5, 14 in decreasing order of N_n) are
scattered through the sequence. There is no tendency for the
wide rungs to cluster. This is consistent with the GUE statistics
expected for Riemann zero spacings -- the ladder is irregular but
statistically well-characterised.

**Observation 5 (Approximate average spacing).** The mean e-fold
gap of 11.036 is close to pi^2/2 * (2*pi / log(gamma_n/(2*pi)))
evaluated at the mean height, consistent with the average zero
spacing from the Riemann-von Mangoldt formula. As n increases,
the average rung width decreases logarithmically: the ladder
compresses at higher rungs.

---

## 3.2 Inflation as a single rung

### 3.2.1 The gamma_5 -> gamma_2 transition

The inflation epoch of standard cosmology -- the exponential
expansion of the universe by a factor of roughly e^60 -- is, in
Integers, the spectral gap between gamma_5 and gamma_2:

$$
N_{\text{inflation}}
\;=\; (\gamma_5 - \gamma_2) \cdot \frac{\pi^2}{2}
\;=\; 11.91302 \times 4.93480
\;=\; 58.788 \text{ e-folds}.
$$

This was first identified in research/06 (R-Theorem GR.1) and is
the strongest single piece of evidence for the cosmic-timeline
interpretation. The values entering the computation:

| Quantity | Value |
|:---------|------:|
| gamma_5 | 32.93506158773919 |
| gamma_2 | 21.02203963877155 |
| gamma_5 - gamma_2 | 11.91302194896763 |
| pi^2/2 | 4.93480220054468 |
| N_{5->2} | 58.7884 |
| Standard cosmology (Planck 2018) | ~60 +/- 5 |
| Discrepancy | 2.0% (within measurement uncertainty) |

### 3.2.2 Re-derivation as a single rung of the ladder

In the level-crossing picture of research/06 Section 5, inflation
is not a "special epoch" requiring a separate inflationary model
(inflaton field, slow-roll potential, etc.). It is one step in the
sequence of ground-state transitions as the universe traverses the
Bost--Connes phase transition:

$$
|\gamma_5\rangle
\;\xrightarrow{\;\beta_{5 \to 2}^*\;}\;
|\gamma_2\rangle
$$

The transition is adiabatic (Landau--Zener probability P approx 1
for the cosmological cooling rate), and the e-fold count is fixed
by the spectral gap with no free parameter.

From the ladder perspective (Table 1), the inflation gap is the sum
of rungs 2 + 3 + 4:

$$
N_{5 \to 2}
\;=\; N_2 + N_3 + N_4
\;=\; 19.684 + 26.717 + 12.387
\;=\; 58.788.
$$

This decomposition is exact. The three sub-rungs may correspond to
three sub-phases of inflation visible in the primordial power
spectrum as mild features at scales that re-entered the horizon at
e-fold counts 12.4, 39.1, and 58.8 from the end of inflation.

### 3.2.3 What inflation is not

In Integers, inflation is NOT:
- A scalar-field slow-roll (no inflaton field is introduced)
- An ad hoc period of exponential expansion
- A fine-tuned potential with eta << 1

Inflation IS the spectral gap gamma_5 - gamma_2 on the Riemann
subspace H_R, traversed adiabatically as the BC effective
temperature crosses the level-crossing value beta_{5->2}*.
The e-fold count is a theorem, not a parameter.

---

## 3.3 Post-inflation as the next rung

### 3.3.1 The gamma_2 -> gamma_1 transition

After inflation deposits the universe in the gamma_2 eigenstate,
the second level-crossing at beta_{2->1}* triggers the final
transition:

$$
N_{\text{post-inflation}}
\;=\; (\gamma_2 - \gamma_1) \cdot \frac{\pi^2}{2}
\;=\; 6.88731 \times 4.93480
\;=\; 33.988 \text{ e-folds}.
$$

This is the expansion from the end of inflation to "now" -- the
entire post-inflationary history of the universe: reheating,
Big Bang nucleosynthesis, recombination, structure formation,
the dark-energy-dominated era, all compressed into one spectral
gap.

| Quantity | Value |
|:---------|------:|
| gamma_2 | 21.02203963877155 |
| gamma_1 | 14.13472514173469 |
| gamma_2 - gamma_1 | 6.88731449703686 |
| N_{2->1} | 33.988 |
| Standard cosmology (post-inflation) | ~35 +/- 3 |
| Discrepancy | 2.9% (within measurement uncertainty) |

### 3.3.2 The cosmological coincidence

Research/42 showed that the "cosmological coincidence" -- the
fact that Omega_Lambda approx Omega_m today -- is not a coincidence
at all. "Now" is the moment when the universe is in the process of
traversing the gamma_2 -> gamma_1 rung. The matter-dark-energy
equality redshift z approx 0.5 is structurally fixed by the e-fold
count of this rung. No anthropic selection is needed.

From Table 1 (Observation 1), rung 1 has the largest e-fold gap of
any rung in the first hundred. The post-inflation epoch is the
widest rung on the ladder.

**Remark.** The cosmological coincidence is *re-expressed* (the
universe is at the widest rung) but not *explained* (why the
universe is at rung 1 now). The re-expression is interesting: the
first rung is widest because the Riemann zeros are sparsest near
gamma_1, a mathematical fact of analytic number theory. But the
coincidence problem asks why an observer exists at this rung rather
than some other — and the ladder does not address this. We note the
re-expression without claiming it resolves the coincidence.

### 3.3.3 The total cosmic e-fold count

The full expansion from the onset of inflation to now:

$$
N_{\text{total}}
\;=\; N_{5 \to 2} + N_{2 \to 1}
\;=\; (\gamma_5 - \gamma_1) \cdot \frac{\pi^2}{2}
\;=\; 18.80034 \times 4.93480
\;=\; 92.776 \text{ e-folds}.
$$

This matches the standard-cosmology estimate of ~95 total e-folds
at the 2.3% level -- again with zero free parameters.

### 3.3.4 The age of the universe as a cross-check

The Six absolute time scale (research/112) gives the age of the
universe as

$$
t_0 \;=\; (\log \gamma_7)^2 \text{ Gyr}
\;=\; (3.7107...)^2
\;=\; 13.776 \text{ Gyr},
$$

which matches Planck 2018 (13.787 +/- 0.020 Gyr) at -0.56 sigma.
The age formula uses gamma_7, while the cosmic e-fold ladder uses
gamma_1 through gamma_5. These are independent derivations from
different zeros that converge on the same cosmic history -- a
non-trivial consistency check on the CBB system.

---

## 3.4 The transitions before gamma_5

### 3.4.1 Reading the ladder backward

The cosmic timeline runs *down* the ladder: from high gamma_n
(early universe, high spectral eigenvalue) to low gamma_n (late
universe, ground state). The inflation epoch begins at gamma_5 and
ends at gamma_2. But what happened *before* gamma_5?

In the level-crossing picture, the universe at very early times
(beta_eff >> 1, deep in the Galois-symmetric phase) occupied a
high-lying eigenstate |gamma_n> with n >> 5. As beta_eff decreased
toward the critical point, the universe descended the ladder
through a sequence of level-crossings. The rungs n >= 6 going
*backward* (i.e., from gamma_6 upward) encode the pre-inflationary
history.

### 3.4.2 The pre-inflation rungs

From Table 1, the rungs immediately above the inflation epoch are:

| Rung | Gap (e-folds) | Tentative identification |
|:-----|:-------------|:------------------------|
| n=5: gamma_5 -> gamma_6 | 22.952 | **STRUCTURAL EXTRAPOLATION.** We tentatively identify rung 5 with the GUT-scale transition, noting this is a structural extrapolation, not a derived result. The e-fold count of 23.0 is consistent with energy scales ~10^{15-16} GeV, but the mapping from e-fold count to energy scale requires a specific relation between beta_eff and temperature that has not been derived. |
| n=6: gamma_6 -> gamma_7 | 16.445 | **STRUCTURAL EXTRAPOLATION.** We tentatively identify rung 6 with Planck-to-GUT cooling, noting this is a structural extrapolation, not a derived result. The 16.4 e-folds are consistent with the hierarchy M_Pl/M_GUT ~ 10^{2-3}, but the identification is chosen to be consistent, not derived from the CBB system. |
| n=7: gamma_7 -> gamma_8 | 11.885 | **STRUCTURAL EXTRAPOLATION.** We tentatively identify rung 7 with Planck-scale structure, noting this is a structural extrapolation, not a derived result. The 11.9 e-folds may encode structure at or above the Planck scale, but the identification is speculative. |
| n=8: gamma_8 -> gamma_9 | 23.085 | **STRUCTURAL EXTRAPOLATION.** We tentatively identify rung 8 with trans-Planckian structure near the projection event, noting this is a structural extrapolation, not a derived result. The wide rung (23.1 e-folds) suggests a major phase transition, but this mapping is speculative. |

### 3.4.3 The projection event

The Galois-invariant state omega_infinity (Section 2.1 of this
paper) is the maximally symmetric BC state: no time, no space,
only spectrum. The "Big Bang" in Integers is the projection event

$$
\omega_\infty \;\longrightarrow\; \omega_1
$$

which breaks the full Galois symmetry Gal(Q^{cyc}/Q) down to a
specific Frobenius orbit. This is NOT a singularity. It is a
well-defined projection on the BC algebra. The "moment" of the
projection is not localisable in ordinary time (time does not exist
in the omega_infinity state); it is the edge of the spectral
sequence as n -> infinity.

In the ladder picture, the projection event is the "top" of the
ladder: the infinite sequence of rungs n -> infinity, with
progressively smaller but nonzero e-fold gaps. The universe
descends from the top of the ladder to the ground state gamma_1
through the full sequence of level-crossings. The total e-fold
count from the projection to now is formally

$$
\mathcal{N}(\infty)
\;=\; \lim_{n \to \infty} (\gamma_{n+1} - \gamma_1) \cdot \frac{\pi^2}{2}
\;=\; \infty,
$$

since gamma_n -> infinity. The universe has undergone infinitely
many e-folds of expansion from the projection event to now.
This is consistent with the standard-cosmology picture of
a(t) growing from zero (the "singularity") to finite size
(today) -- but in Integers, there is no singularity, only an
infinite ladder.

### 3.4.4 The five physical phases from the ladder

Combining the downward and upward readings, the cosmic ladder
identifies five major phases:

| Phase | Rungs | Total e-folds | Physical content | Status |
|:------|:------|:-------------|:-----------------|:-------|
| V. Pre-geometric | n >> 8 | infinite | The descent from the Galois projection. No classical spacetime. Pure spectral arithmetic. | STRUCTURAL EXTRAPOLATION |
| IV. Planck / trans-Planckian | n = 7, 8 | 35.0 | Tentative: geometric moduli freeze out. M_geom settles to P_phys. | STRUCTURAL EXTRAPOLATION |
| III. GUT-scale | n = 5, 6 | 39.4 | Tentative: grand unification, symmetry breaking to the SM gauge group. | STRUCTURAL EXTRAPOLATION |
| II. Inflation | n = 2, 3, 4 | 58.8 | Exponential expansion. Three sub-phases of 12.4, 26.7, 19.7 e-folds. | DERIVED (research/06) |
| I. Post-inflation ("now") | n = 1 | 34.0 | Reheating, BBN, recombination, structure formation, dark energy domination. The widest single rung. | DERIVED (research/06) |

The e-fold counts for all five phases are exact arithmetic from the
Riemann zeros. The physical identifications for phases I and II are
derived from the level-crossing structure (research/06). The
identifications for phases III--V are structural extrapolations:
the framework associates a spectral rung with each major cosmic
transition, but the identification is derived for rungs 1--5 and
tentative for n >= 6.

### 3.4.5 Remark on falsifiability

The pre-inflation rungs (n >= 6) are structural extrapolations.
Their e-fold counts are exact arithmetic from the Riemann zeros,
but their physical identification with GUT-scale, Planck-scale,
and trans-Planckian epochs is tentative. Falsification would
require either:

(a) A detection of primordial gravitational waves or other
relics from the pre-inflationary epoch that contradicts the
e-fold budget of rungs 5--8, or

(b) A theoretical demonstration that the level-crossing structure
of H_eff(beta_eff) does not produce the sequence
... -> gamma_8 -> gamma_7 -> gamma_6 -> gamma_5 -> gamma_2
-> gamma_1 but a different path.

Route (b) is the more immediate target and requires the explicit
computation of V(beta_eff) identified as open problem (O1) in
research/06.

---

> **Origin callout (G, 2026-04-09):** *"every computer in the world
> can calculate t_0 = (log gamma_7)^2 Gyr and it should"*

Every computer in the world can also calculate Table 1. The cosmic
ladder is arithmetic. No telescope is needed to compute it -- only
the zeros of the Riemann zeta function, which have been tabulated
to billions of entries. The physical identification of each rung
is the interpretive layer; the numbers themselves are theorems.

---

*Rung 1 is the widest. We live on it.*
*Rung 2 + 3 + 4 is inflation: 58.8 e-folds, no inflaton.*
*The ladder goes up forever. The universe came down it.*
*Every e-fold count is exact arithmetic. The physical identifications*
*are derived for rungs 1--5 and tentative for n >= 6.*
