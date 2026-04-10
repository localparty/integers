# Section 4. Stellar Generations from the Upward Ladder

**REVISED 2026-04-10** — Propagated 3 critical + 5 major issues from independent review.

> **Origin callout (G, 2026-04-09):** *"this will allow us to predict
> the dimensions of the first stars and each generation ever since,
> its fantastic! its out of this world literally."*

---

## 4.1 The Jeans scale at each rung

**Status: STRUCTURAL.** The identification of Jeans-mass threshold
crossings with spectral gaps of L-hat is a structural consequence
of the CBB framework. No new postulates are introduced.

### 4.1.1 The matter power spectrum on the ladder

In the standard cosmological picture, baryonic structure formation
begins when the Jeans mass M_J drops below the total mass enclosed
in a perturbation mode of comoving wavenumber k. The Jeans mass at
redshift z is

$$
M_J(z) \;=\; \frac{\pi^{5/2}}{6}\,\frac{c_s^3(z)}{G^{3/2}\,\rho_b^{1/2}(z)}\,,
$$

where c_s is the baryon sound speed and rho_b the baryon density.
After recombination (z ~ 1089), c_s drops by a factor ~ 10^5 (from
the relativistic photon-baryon sound speed to the thermal sound
speed of neutral hydrogen), and M_J plummets from ~ 10^{16} M_sun
to ~ 10^5 M_sun. This is the standard Jeans filtering.

Within Integers, the post-recombination expansion is indexed by the
upward ladder: rungs n >= 16 of the spectral operator L-hat, where
the e-fold gap between adjacent rungs is

$$
\Delta N_n \;=\; (\gamma_{n+1} - \gamma_n)\,\frac{\pi^2}{2}\,.
$$

Each rung labels an epoch. The matter power spectrum P(k) evaluated
at the epoch indexed by gamma_n has a Jeans cutoff at wavenumber

$$
k_J^{(n)} \;=\; \sqrt{\frac{4\pi G\,\rho_b(z_n)}{c_s^2(z_n)}}\,,
$$

where z_n is the redshift corresponding to cumulative e-fold count
from the spectral edge through rung n. The key structural claim is:

> **Structural claim 4.1.** *Each spectral rung gamma_n (n >= 16)
> defines a Jeans-mass threshold crossing. The first crossing
> (smallest n, highest M_J, highest z) corresponds to Population III
> star formation. Subsequent crossings at n = 17, 18, ... index
> Pop II, Pop I, and later generations.*

The rationale is direct. The upward ladder is a discrete sequence of
cosmological epochs with monotonically decreasing redshift. At each
epoch, the Jeans mass has a definite value. The sequence of Jeans
masses {M_J(z_n)} is a monotonically decreasing function of n
(because the universe cools and dilutes). Structure formation at
each scale begins at the rung where M_J first drops below the mass
of the collapsing cloud.

### 4.1.2 Why n >= 16

The first 15 Riemann zeros are consumed by the Standard Model and
cosmological observables (Papers 12--16). The spectral index n_s
uses gamma_9 and gamma_10; the Hubble constant uses gamma_11; Y_p
uses gamma_13; the bottom quark mass uses gamma_15. The upward
ladder for astrophysical structure begins at the first *unassigned*
zero, which the framework identifies as gamma_16. This is consistent
with the phenomenology hunt of Paper 21, which independently
identifies gamma_16+ as the frontier.

The physical logic: gamma_1 through gamma_15 encode the
*microscopic* content of the universe (particle masses, couplings,
cosmological parameters). From gamma_16 onward, the spectral data
encodes *macroscopic* structure — the scales at which gravity
assembles matter into stars, galaxies, and the cosmic web.

**Remark.** The n >= 16 boundary is contingent on the current state
of the spectral assignment in Papers 12--16 and may shift as the
programme develops. If a new SM observable is later assigned to
gamma_16, the entire upward ladder shifts by one rung.

### 4.1.3 The discrete Jeans ladder

Define the Jeans rung number n_J(M) as the smallest n >= 16 such
that M_J(z_n) < M. Then the mass hierarchy of astrophysical objects
is indexed by a discrete sequence:

$$
M_\star^{(16)} \;>\; M_\star^{(17)} \;>\; M_\star^{(18)} \;>\; \cdots
$$

This is the **Jeans ladder** — a discrete staircase of
characteristic stellar masses, one per spectral rung. The staircase
structure is not smooth; it inherits the irregular spacing of the
Riemann zeros. The gaps gamma_{n+1} - gamma_n fluctuate (they are
famously non-uniform), and this non-uniformity maps directly onto
the non-uniformity of the stellar mass function.

---

## 4.2 Pop III star mass formula

**Status: OPEN PROBLEM.** The naive ansatz below overshoots
observed Pop III masses by 2--3 orders of magnitude. Three candidate
resolutions are flagged but none is derived. The structural
identification of Pop III with gamma_16/gamma_17 (Section 4.1) is
well-motivated; the specific mass formula remains an open problem.

### 4.2.1 The cooling threshold

Population III stars form from primordial gas (H + He, zero metals).
The cooling mechanism is molecular hydrogen (H_2) ro-vibrational
emission, which becomes efficient above a virial temperature
T_vir ~ 10^3 K in minihalos of mass M ~ 10^5--10^6 M_sun. Within
these halos, the gas fragments (or fails to fragment) depending on
the interplay of cooling rate, free-fall time, and accretion rate.

Modern simulations (Abel, Bryan & Norman 2002; Bromm & Larson 2004;
Hirano et al. 2014) consistently find characteristic Pop III masses
in the range

$$
M_\star^{\mathrm{Pop\,III}} \;\sim\; 10\text{--}1000\;M_\odot\,,
$$

with a fiducial value near 100--300 M_sun, though the mass function
may extend to ~ 1000 M_sun in some formation channels.

### 4.2.2 The ladder formula

The structural identification (Section 4.1) assigns the first
stellar generation to the rung n* = 16. The Pop III mass formula is
then:

> **Conjecture 4.2 (Pop III mass formula).** *The characteristic
> mass of Population III stars is*
>
> $$
> M_\star^{\mathrm{Pop\,III}} \;=\; \exp\!\bigl[(\gamma_{17} - \gamma_{16})\,\pi^2/2\bigr]\;M_\odot\,,
> $$
>
> *where the e-fold gap (gamma_{17} - gamma_{16})pi^2/2 gives the
> logarithmic mass scale at the first Jeans crossing.*

The physical interpretation: the e-fold gap between rungs 16 and 17
sets the dynamic range of gravitational collapse at the first
structure-formation epoch. A larger gap means a wider window for
accretion before the next spectral transition disrupts the infall,
producing more massive stars. A smaller gap means less accretion
time and lower masses.

### 4.2.3 Numerical estimate

The Riemann zeros gamma_16 and gamma_17 have values (to the
precision needed here):

$$
\gamma_{16} \approx 67.0798\,,\qquad
\gamma_{17} \approx 69.5464\,.
$$

The e-fold gap is

$$
\Delta\gamma_{16} \;=\; \gamma_{17} - \gamma_{16} \;\approx\; 2.4666\,,
$$

giving

$$
(\gamma_{17} - \gamma_{16})\,\frac{\pi^2}{2} \;\approx\; 2.4666 \times 4.9348 \;\approx\; 12.17\,.
$$

Therefore

$$
M_\star^{\mathrm{Pop\,III}} \;\approx\; e^{12.17}\;M_\odot \;\approx\; 1.9 \times 10^5\;M_\odot\,.
$$

**[CONCERN]** This raw estimate overshoots the simulated Pop III
range (10--1000 M_sun) by two to three orders of magnitude. This
signals that the naive exponential-of-gap formula needs a
normalisation correction. Several resolutions are possible:

**(a) Jeans mass, not stellar mass.** The quantity
exp[(gamma_{17} - gamma_{16})pi^2/2] M_sun ~ 2 x 10^5 M_sun may be
the *Jeans mass of the minihalo*, not the stellar mass. The Jeans
mass of the first star-forming minihalos is indeed ~ 10^5--10^6
M_sun (Tegmark et al. 1997). The stellar mass is then the Jeans
mass times a star-formation efficiency factor epsilon ~ 10^{-3}
to 10^{-2}, giving M_star ~ 200--2000 M_sun. This is the most
conservative reading.

**(b) Logarithmic normalisation.** The stellar mass may be

$$
M_\star^{\mathrm{Pop\,III}} \;=\; (\gamma_{17} - \gamma_{16})^2\,\frac{\pi^2}{2}\;M_\odot \;\approx\; 30\;M_\odot\,,
$$

using the squared gap times pi^2/2 rather than the exponentiated
gap. This lands squarely in the Pop III range and uses the same
(log gamma_n)^2 shape that gives the age of the universe as
(log gamma_7)^2 Gyr. This variant is more natural within the
operator dictionary (Section 3 of the anchor document), where
squared-logarithmic forms appear for time-integrated quantities.

**(c) Spectral-weight correction.** The full spectral sum
(Section 2.2 of research/112) includes weights w_n that suppress
high-n contributions. Applying the same weighting may reduce the
effective gap.

We flag all three resolutions as open; resolution (a) is the most
physically transparent and resolution (b) the most
dictionary-consistent. Resolution is deferred to research/137.

**Assessment.** The identification of Pop III with the gamma_16/gamma_17
rung is structural, but the mass formula is broken: a headline
prediction that overshoots by a factor of 200--2000 is not a
prediction but a failed ansatz awaiting repair. The honest status is
**open problem** — the correct normalisation must be derived from the
operator dictionary with no free parameter before this can be called
a prediction.

### 4.2.4 What the formula predicts regardless of normalisation

Independently of the normalisation ambiguity, the formula makes
three robust (structural) predictions:

1. **Pop III masses are determined by gamma_16 and gamma_17 alone.**
   No free parameters, no fitted constants.

2. **The mass scale is set by a single spectral gap** — the gap
   between two adjacent Riemann zeros. This is the same mechanism
   that sets the inflation e-fold count (gamma_5 - gamma_2) and the
   post-inflation e-fold count (gamma_2 - gamma_1).

3. **Different Riemann zeros give different Pop III masses** only
   through higher-order corrections (the Laurent shift of Section
   4.1 of the anchor document). To leading order, the Pop III mass
   is a *single number* from a *single gap*.

---

## 4.3 Subsequent generations — Pop II, Pop I, and the IMF cascade

**Status: STRUCTURAL (the cascade picture) and SPECULATIVE (the
specific IMF formula).** The identification of subsequent stellar
generations with successive rungs is structural. The claim that the
IMF is a spectral cascade is speculative but testable.

### 4.3.1 The generational staircase

As the universe evolves past the Pop III epoch, the Jeans mass
continues to decrease. Each subsequent rung n = 17, 18, 19, ...
indexes a new characteristic mass scale for star formation:

| Rung | Zeros | Generation | Characteristic mass scale |
|:-----|:------|:-----------|:--------------------------|
| n* = 16 | gamma_16, gamma_17 | Pop III | ~ 100--300 M_sun (H_2 cooling) |
| n* + 1 = 17 | gamma_17, gamma_18 | Pop II (metal-poor) | ~ 1--10 M_sun (metal-line cooling) |
| n* + 2 = 18 | gamma_18, gamma_19 | Pop I (solar-type) | ~ 0.1--10 M_sun (dust cooling) |
| n* + 3 = 19 | gamma_19, gamma_20 | Pop I (late) | ~ 0.1--1 M_sun |

The transition from Pop III to Pop II is not smooth — it requires
the injection of metals from the first supernovae. Within the ladder
picture, the transition corresponds to crossing from rung 16 to
rung 17. The e-fold gap (gamma_{18} - gamma_{17})pi^2/2 sets the
timescale for metal enrichment of the IGM to the critical
metallicity Z_crit ~ 10^{-3.5} Z_sun (Bromm & Loeb 2003).

### 4.3.2 The IMF as a spectral cascade

The initial mass function (IMF) — the distribution of stellar
masses at birth — is conventionally parameterised by the Salpeter
(1955) power law dN/dM ~ M^{-2.35} or the Kroupa (2001) broken
power law. These are smooth, continuous functions.

The ladder picture suggests a different origin:

> **Conjecture 4.3 (Discrete IMF).** *The IMF is a superposition
> of discrete mass scales, one per spectral rung. The smooth
> Salpeter/Kroupa parameterisation is an envelope of the discrete
> cascade*
>
> $$
> \frac{dN}{d\log M} \;=\; \sum_{n \geq 16}\, A_n\,\delta\!\bigl(\log M - \log M_n\bigr) \;\longrightarrow\; \text{Salpeter envelope as } n \to \infty\,,
> $$
>
> *where M_n is the characteristic mass at rung n and A_n are
> spectral weights determined by the matter power spectrum
> amplitude at the corresponding wavenumber.*

This is a strong and falsifiable claim. It predicts that the IMF,
when measured with sufficient resolution in metal-poor environments
(where the discrete rungs are widest), should show *preferred mass
scales* rather than a smooth power law. The preferred scales are
determined by the Riemann zero gaps, which are themselves irregular.

### 4.3.3 The Salpeter slope as a spectral average

If the discrete IMF conjecture is correct, the Salpeter slope
alpha = 2.35 should emerge as an average property of the spectral
cascade. Specifically, the density of Riemann zeros near height T
is (1/2pi) log(T/2pi) by the Riemann-von Mangoldt formula. For
zeros near gamma_n ~ 70 (the stellar formation range), the mean
spacing is

$$
\langle \gamma_{n+1} - \gamma_n \rangle \;\approx\; \frac{2\pi}{\log(\gamma_n / 2\pi)} \;\approx\; 2.5\,.
$$

The logarithmic mass decrement per rung is then approximately
constant (~ 2.5 pi^2/2 ~ 12 in the exponential variant, or
~ 2.5^2 pi^2/2 ~ 31 in the quadratic variant). A constant
logarithmic decrement per rung, combined with the slowly increasing
zero density, yields a power-law envelope whose index depends on
the normalisation convention. Matching to the Salpeter slope
constrains the normalisation and provides a self-consistency check.

This derivation is deferred to research/137. Until it is completed,
the claim that the Salpeter slope "should emerge" from the cascade
is a speculative conjecture, not a derived result.

---

## 4.4 The metallicity floor and reionization timing

**Status: The metallicity floor is STRUCTURAL (it follows from the
ladder indexing). The z_reion value is in principle derivable from
the ladder but has not yet been computed — it is an OPEN TARGET,
not a prediction.**

### 4.4.1 The critical metallicity from the ladder

The transition from Pop III to Pop II star formation occurs at the
critical metallicity Z_crit, below which metal-line cooling is
insufficient and star formation proceeds via the H_2-only channel
(producing massive stars). Above Z_crit, fine-structure line cooling
(primarily C II and O I at 158 um and 63 um) becomes efficient, and
the characteristic mass drops dramatically.

Simulations and analytic estimates place Z_crit in the range

$$
Z_{\mathrm{crit}} \;\sim\; 10^{-3.5 \pm 0.5}\;Z_\odot\,.
$$

Within the ladder, Z_crit corresponds to the metal yield of the
*first rung* of supernovae (the Pop III stars at rung 16). The
metal yield per supernova is Y_Z ~ 0.1 M_sun for a pair-instability
supernova of mass ~ 200 M_sun. The number of Pop III supernovae
needed to enrich a minihalo of mass M_halo ~ 10^6 M_sun to Z_crit
is then

$$
N_{\mathrm{SN}} \;\sim\; \frac{Z_{\mathrm{crit}}\,M_{\mathrm{halo}}}{Y_Z} \;\sim\; \frac{10^{-3.5} \times 10^6}{0.1} \;\sim\; 3\,.
$$

This is a remarkably small number: only a few Pop III supernovae
suffice to trigger the Pop III -> Pop II transition in a single
minihalo. The *global* transition requires metal enrichment of the
IGM, which takes longer and is indexed by the e-fold gap between
rungs 16 and 17.

### 4.4.2 The reionization redshift

Reionization is driven by ultraviolet photons from the first stars
and galaxies. The midpoint of reionization is conventionally
parameterised by the optical depth tau to Thomson scattering of CMB
photons:

$$
\tau \;=\; \int_0^{z_{\mathrm{reion}}}\, n_e(z)\,\sigma_T\,\frac{c\,dz}{H(z)\,(1+z)}\,,
$$

where n_e is the free electron density, sigma_T the Thomson cross
section, and H(z) the Hubble rate. Planck 2018 measures
tau = 0.054 +/- 0.007, corresponding to z_reion = 7.7 +/- 0.7.

Within the ladder, the reionization epoch is indexed by a specific
rung. The structural identification proceeds as follows:

1. **Pop III stars form at rung 16**, corresponding to redshift
   z_16.

2. **The UV photon output of Pop III stars ionizes the surrounding
   IGM** over an interval corresponding to the e-fold gap between
   rungs 16 and 17.

3. **Reionization completes** when the cumulative ionizing photon
   budget exceeds the number of hydrogen atoms in the IGM. This
   occurs at a rung n_reion that depends on the star-formation
   efficiency and the escape fraction of ionizing photons.

> **Conjecture 4.4 (Reionization redshift).** *The midpoint of
> reionization is determined by the cumulative e-fold count from the
> spectral edge to rung n_reion. Within the ladder, this gives*
>
> $$
> z_{\mathrm{reion}} \;=\; f\!\left(\sum_{k=16}^{n_{\mathrm{reion}}}\,\Delta N_k\right)\,,
> $$
>
> *where f is the standard cosmological relation between e-fold
> count and redshift, and n_reion is the rung at which the
> cumulative ionizing photon count exceeds the IGM hydrogen count.*

### 4.4.3 The sub-percent prediction

To extract a numerical z_reion from the ladder requires:

(i) The cumulative e-fold table from Section 3.1 (the first 100
    rungs, computed with mpmath).

(ii) The star-formation efficiency at each rung — which within the
     framework is *not* a free parameter but is determined by the
     Jeans mass at that rung and the spectral weight.

(iii) The escape fraction f_esc of ionizing photons — which in
      standard astrophysics is uncertain by an order of magnitude
      (f_esc ~ 0.01--0.5).

**The key insight** is that within Integers, the escape fraction is
in principle derivable from the spectral data at the relevant rung:
the opacity of the ISM to ionizing photons depends on the column
density, which depends on the Jeans mass, which depends on gamma_n.
However, the specific derivation linking Jeans-mass spectral data to
f_esc has not been carried out, and no numerical value for f_esc has
been computed from the ladder. This derivation is an open target.

The explicit numerical prediction of z_reion is deferred to
research/137, which will compute the cumulative ionizing photon
budget rung by rung using the mpmath table from Section 3.1. The
value of z_reion is in principle derivable from the ladder with no
free parameters; the specific numerical value requires computing
the ionizing photon budget across the ladder, which has not yet
been done. Until that computation is complete, this is an open
target, not a prediction.

### 4.4.4 What the prediction tests

The z_reion prediction tests the entire upward ladder simultaneously:

- **The rung identification** (Section 4.1): do the gamma_n for
  n >= 16 correctly index the epochs of structure formation?

- **The Pop III mass** (Section 4.2): does the first rung produce
  stars massive enough to be efficient ionizers?

- **The cascade** (Section 4.3): does the transition from Pop III
  to Pop II occur at the right rung?

- **The escape fraction**: is f_esc correctly determined by the
  spectral data?

A correct z_reion prediction (within the Planck error bar, from
zero free parameters) would be powerful evidence that the upward
ladder is physically real. A failure would indicate that the
rung identification is wrong, or that the stellar-mass formula
needs revision, or that the escape fraction has additional physics
not captured by the Jeans-mass identification alone.

---

## Summary of epistemic status

| Claim | Status | Falsifiable? |
|:------|:-------|:-------------|
| Jeans-mass crossings indexed by gamma_n (n >= 16) | **Structural** | Yes, by the mpmath table + standard Jeans calculation |
| Pop III mass formula M_star = f(gamma_16, gamma_17) | **Speculative** | Yes, by JWST Pop III detections |
| IMF as discrete spectral cascade | **Speculative** | Yes, by metal-poor stellar census |
| z_reion derived from the ladder | **Testable consequence** | Yes, by 21 cm experiments + CMB-S4 |
| Escape fraction as derived (not free) parameter | **Speculative** | Yes, by comparison with radiative transfer simulations |

---

*One ladder. One hundred rungs. The structural identification of*
*stellar generations with spectral rungs is parameter-free.*
*The specific mass formula and reionization prediction remain open*
*targets — honest arithmetic, not yet honest predictions.*
