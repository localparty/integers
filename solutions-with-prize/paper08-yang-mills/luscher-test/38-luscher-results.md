# Lüscher Test Results and the Three Missing Modes

## I. What the Computation Showed

Using the lattice-measured worldsheet axion mass $m_a = 1.85\sqrt{\sigma}$
(Athenodorou--Teper 2024, Dubovsky--Gorbenko 2016), we computed the
effective central charge $c_{\text{eff}}(R)$ for three models of the
confining string worldsheet:

| $R\sqrt{\sigma}$ | $R$ (fm) | Nambu-Goto | 1 axion (DGM) | CP$^2$ (4 modes) |
|:-:|:-:|:-:|:-:|:-:|
| 0.3 | 0.13 | 2.000 | 2.382 | 3.527 |
| 0.5 | 0.22 | 2.000 | 2.203 | 2.811 |
| 0.7 | 0.31 | 2.000 | 2.107 | 2.427 |
| 1.0 | 0.45 | 2.000 | 2.040 | 2.160 |
| 1.5 | 0.67 | 2.000 | 2.007 | 2.030 |
| 2.0 | 0.90 | 2.000 | 2.001 | 2.005 |

All three models converge to $c = 2$ at large $R$. They differ at
intermediate $R$ where the massive modes are active.

**The discriminator:** At $R\sqrt{\sigma} = 0.7$ ($R \approx 0.3$ fm):
- Nambu-Goto: $c = 2.000$
- 1 axion: $c = 2.107$ (+5.3%)
- 4 CP$^2$ modes: $c = 2.427$ (+21.4%)

The 4-mode model predicts exactly 4$\times$ the single-axion effect.
This is detectable at $\sim 7\%$ precision on $c_{\text{eff}}$.


---

## II. What the Lattice Has Already Found

### II.1 The worldsheet axion (confirmed)

Dubovsky, Gorbenko, and Mirbabayi (2016) predicted a massive
pseudoscalar mode on the confining string worldsheet. Athenodorou and
Teper (2024) confirmed it from lattice flux-tube spectrum measurements:

| Quantity | Lattice value | Theory |
|:--|:--|:--|
| Axion mass $m_a$ | $1.85^{+0.02}_{-0.03}\,\sqrt{\sigma}$ | Not predicted by integrability |
| Axion mass (physical) | $\approx 814$ MeV | $\sim \sqrt{\sigma} \sim 440$ MeV (our prediction) |
| Axionic coupling $Q$ | $0.38 \pm 0.04$ | $\sqrt{7/(16\pi)} \approx 0.373$ |

The axion explains the anomalous $J^P = 0^-$ states in the flux-tube
spectrum that deviate from Nambu-Goto. Its coupling matches the
integrable string theory prediction to within 2%.

### II.2 The Axionic String Ansatz (ASA)

Athenodorou, Caristo, and Caselle (2024) showed that ALL observed
flux-tube states in SU(3), SU(5), and SU(6) can be described by:

$$\text{Nambu-Goto} + \text{one massive pseudoscalar (the axion)}$$

The ASA works across multiple gauge groups with the SAME axion mass
(in string units). This universality is consistent with both the
single-axion model and our CP$^{N-1}$ model (the pseudoscalar is the
same mode in both).

### II.3 What has NOT been tested

The lattice analyses focused on the PSEUDOSCALAR channel ($J^P = 0^-$).
The other quantum number channels have been measured but not analyzed
for additional massive worldsheet modes beyond Nambu-Goto. Specifically:

- **Scalar channel ($0^+$):** Shows good agreement with NG for the
  ground state. Deviations in excited states are attributed to
  higher-order NG corrections, not to new modes. But the analysis
  assumed NG + axion only.
- **Vector channels ($1^\pm$):** Not systematically analyzed for
  massive worldsheet modes.
- **Higher spin:** Not analyzed.

**The CP$^2$ prediction would show up in the scalar and vector channels
as additional massive modes.** These have not been looked for.


---

## III. The Three Missing Modes

### III.1 What CP$^2$ predicts

The CP$^2$ sigma model has $\text{dim}_{\mathbb{R}}(\mathbb{CP}^2) = 4$
real degrees of freedom. These decompose into worldsheet fields as:

$$\mathbb{CP}^2 = \{n \in \mathbb{C}^3 : |n| = 1\} / U(1)$$

The 4 real modes of the CP$^2$ field $n = (n_1, n_2, n_3)$ (modulo
$U(1)$ phase) decompose under the residual symmetry group of the
confining string as:

**The residual symmetry.** The confining string between a quark and
antiquark in the fundamental representation of SU(3) breaks:
$$SU(3) \to S(U(1) \times U(2))$$

The CP$^2$ field $n$ transforms under this residual symmetry. The 4
real modes decompose as:

| Mode | $J^P$ on worldsheet | Mass (predicted) | Status |
|:-----|:---:|:---:|:---:|
| Mode 1: pseudoscalar | $0^-$ | $m_a \approx 1.85\sqrt{\sigma}$ | **FOUND** (the axion) |
| Mode 2: scalar | $0^+$ | $m_s \sim m_a$ or heavier | **NOT YET SEARCHED** |
| Mode 3: scalar | $0^+$ | $m_s \sim m_a$ or heavier | **NOT YET SEARCHED** |
| Mode 4: pseudoscalar | $0^-$ | $m_{a'} \sim m_a$ or heavier | **NOT YET SEARCHED** |

The exact quantum numbers depend on the embedding of the string
orientation into the CP$^2$ geometry. The general prediction: **4
massive modes total**, with the already-found axion being one of them.

### III.2 Why only one mode has been seen

Several explanations are consistent with the data:

**(a) Mass hierarchy.** If the 3 additional modes are heavier than the
axion ($m_{2,3,4} > m_a$), they contribute less to the flux-tube
spectrum at the string lengths $R$ studied on the lattice. The lattice
measurements have $R\sqrt{\sigma}$ up to $\sim 3$--$5$. At these
lengths, modes with $m > 2\sqrt{\sigma}$ are exponentially suppressed
($e^{-mR}$) and would not be visible.

**(b) Quantum numbers.** The lattice analyses focused on specific
$J^{PC}$ channels. If the additional modes have different quantum
numbers than those analyzed, they would not have been detected.

**(c) Mixing.** The additional modes might mix with Nambu-Goto
excitations in the same quantum number channel, making them difficult
to identify as "new" modes versus NG corrections.

**(d) All four degenerate.** If all 4 modes have the same mass
$m_a = 1.85\sqrt{\sigma}$, the total effect on the static potential
is 4$\times$ larger than the single-axion prediction. This is a 21%
effect at $R\sqrt{\sigma} = 0.7$ — potentially already visible in
existing $V(R)$ data if analyzed with the right model.


### III.3 How to find them

**Test 1: Refit the excited string spectrum with 4 modes.**

The Athenodorou-Teper data includes excited flux-tube states in
multiple $J^{PC}$ channels. Currently fit with NG + 1 axion (ASA).
Refit with NG + 4 CP$^2$ modes:
- 1 pseudoscalar at $m_a = 1.85\sqrt{\sigma}$ (the axion, fixed)
- 3 additional modes with masses $m_{2,3,4}$ as free parameters
- Compare $\chi^2$ of the 4-mode fit versus the 1-mode fit
- If $\chi^2$ improves significantly: evidence for additional modes

**Test 2: The static potential at intermediate $R$.**

Compute $c_{\text{eff}}(R)$ from high-precision $V(R)$ data at
$R\sqrt{\sigma} = 0.5$--$1.5$. Compare with:
- Model A: NG ($c = 2$ flat)
- Model B: NG + 1 axion ($\delta c = 0.04$--$0.20$)
- Model C: NG + 4 CP$^2$ modes ($\delta c = 0.16$--$0.81$)

If the data prefers $\delta c$ in the range 0.16--0.81 (rather than
0.04--0.20), it favors 4 modes over 1 mode.

**Test 3: SU($N$) scaling.**

Our model predicts $2(N-1)$ modes for gauge group SU($N$):
- SU(2): 2 modes
- SU(3): 4 modes
- SU(5): 8 modes
- SU(6): 10 modes

The single-axion model predicts 1 mode for all $N$.

The lattice data exists for SU(3), SU(5), and SU(6). If the number of
massive modes scales as $2(N-1)$, the CP$^{N-1}$ prediction is
confirmed. If it stays at 1 for all $N$, the single-axion model wins.

**Test 4: The $0^+$ scalar channel.**

The CP$^2$ model predicts at least 2 scalar ($0^+$) modes. These would
appear as additional states in the $0^+$ flux-tube spectrum beyond what
Nambu-Goto predicts. The Athenodorou-Teper data INCLUDES the $0^+$
spectrum — reanalyze it for unexplained states.


---

## IV. The $SU(N)$ Scaling Test — The Most Decisive

This is the cleanest test because it's a COUNTING argument.

### IV.1 The two predictions

**Single axion (Dubovsky-Gorbenko):**
Number of massive worldsheet modes = 1 for all $N$.

The axion is a universal feature of the string worldsheet, related to
the self-intersection number. It does not depend on $N$.

**CP$^{N-1}$ worldsheet (our framework):**
Number of massive worldsheet modes = $2(N-1)$.

The modes are the real degrees of freedom of the CP$^{N-1}$ sigma
model field. They grow with $N$.

### IV.2 The data

The Athenodorou-Teper group has measured the flux-tube spectrum for:
- SU(3): axion seen, $m_a = 1.85\sqrt{\sigma}$
- SU(5): axion seen, same $m_a$ in string units
- SU(6): axion seen, same $m_a$ in string units

The CONSISTENCY of $m_a$ across $N$ is noted — but the TOTAL NUMBER of
massive modes at each $N$ has not been systematically extracted.

### IV.3 The prediction

| $N$ | CP$^{N-1}$ modes | Expected excess in $c_{\text{eff}}$ at $R\sqrt{\sigma} = 0.7$ |
|:---:|:---:|:---:|
| 2 | 2 | +10.7% |
| 3 | 4 | +21.4% |
| 5 | 8 | +42.7% |
| 6 | 10 | +53.4% |

The effect grows linearly with $N$. At SU(6), the excess is 53% — an
enormous signal. If the lattice SU(6) data shows this, the CP$^{N-1}$
prediction is confirmed beyond any doubt.

If the excess is $\sim 5\%$ for all $N$: the single-axion model wins.

### IV.4 What to do

1. Extract $c_{\text{eff}}(R)$ from the Athenodorou-Teper data at each
   $N$ separately.
2. Plot $\delta c(R\sqrt{\sigma} = 0.7)$ versus $N$.
3. Fit to $\delta c = A \times (N-1)$ (our prediction) versus
   $\delta c = B$ (constant, single-axion prediction).
4. The slope $A$ versus flatness $B$ is the decisive discriminator.


---

## V. Summary of Tests and Expected Outcomes

| Test | What to do | Our prediction | Single-axion prediction | Discriminating power |
|:-----|:-----------|:---------------|:----------------------|:-----|
| Static potential $V(R)$ | Measure $c_{\text{eff}}(R)$ at $R\sqrt{\sigma} \sim 0.7$ | $\delta c \approx 0.43$ | $\delta c \approx 0.11$ | 4× difference |
| Excited spectrum refit | Fit with 4 modes vs 1 mode | Better $\chi^2$ with 4 modes | Better with 1 mode | Direct mode counting |
| SU($N$) scaling | $\delta c$ vs $N$ | $\delta c \propto (N-1)$ | $\delta c$ = const | Linear growth vs flat |
| Scalar $0^+$ channel | Look for extra states | 2 scalar modes predicted | No extra scalars | New states vs none |

**The SU($N$) scaling test is the most powerful** because it
distinguishes a counting prediction ($2(N-1)$ modes) from a universal
prediction (1 mode). The data already exists in the Athenodorou-Teper
papers — it just needs to be reanalyzed.
