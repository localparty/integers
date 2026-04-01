# Tools and Frameworks Needed for Precision Predictions

## 1. The Computational Pipeline

To go from the 5D framework's geometric parameters to precision
cosmological predictions, we need a pipeline:

    {L, V(phi), xi, T_reheat, SM content}
                |
                v
    {H_0, Omega_m, Omega_r, w(z), N_eff, Sum_m_nu}
                |
                v
    [Modified Boltzmann solver]
                |
                v
    {t_0, r_d, theta_*, CMB C_l, P(k), S8, BAO scale}
                |
                v
    [Comparison with data: Planck, DESI, JWST, SH0ES]

---

## 2. Immediate Tools (Can Start Now)

### 2.1 Python Numerical Integration (Age Integral)

A simple Python script to compute:

    t_0 = integral_0^z_max dz / [(1+z) * H(z)]

with H(z) from the 5D modified Friedmann equation.

**Dependencies:** numpy, scipy
**Complexity:** Low -- a few hours of work
**Output:** t_0 for various framework parameter choices

### 2.2 ODE Solver (Dilaton Dynamics)

Solve the dilaton equation of motion:

    phi_ddot + 3*H*phi_dot + dV/dphi = 0

coupled to the Friedmann equation:

    H^2 = (8*pi*G/3) * (rho_m + rho_r + V(phi) + phi_dot^2/2)

**Dependencies:** scipy.integrate.solve_ivp
**Complexity:** Medium -- a day or two
**Output:** w(z), phi(z), H(z) from the dilaton dynamics

### 2.3 Fisher Matrix Forecast

Estimate how precisely the framework's parameters can be constrained
by upcoming experiments (CMB-S4, DESI DR3, Euclid).

**Dependencies:** numpy, basic linear algebra
**Complexity:** Medium
**Output:** Projected parameter constraints and degeneracies

---

## 3. Medium-Term Tools (1-2 Weeks)

### 3.1 CLASS Boltzmann Solver (Modified)

CLASS (Cosmic Linear Anisotropy Solving System) is the standard tool
for computing CMB power spectra and matter power spectra.

**URL:** https://github.com/lesgourg/class_public
**Language:** C with Python wrapper (classy)
**Installation:** pip install cclassy (or build from source)

**Modifications needed:**
1. Add custom w(z) from dilaton dynamics (CLASS already supports w0-wa)
2. Add Delta_N_eff = 0.30 (CLASS already supports extra N_eff)
3. Potentially add H_b term to Friedmann equation (requires C-level
   modification to background.c)

For Case A (stabilized e-circle, w = -1), NO modifications needed --
just set the framework's parameter values in CLASS.

For Case B (thawing dilaton), use CLASS's built-in w0-wa parameterization
with the dilaton-derived values.

For Case C (full 5D Friedmann), need to modify background.c to add
the H*H_b term. This is the hardest modification.

**Output:** CMB power spectrum C_l, matter power spectrum P(k), r_d,
theta_*, sigma_8, all derived distances.

### 3.2 CAMB (Alternative to CLASS)

CAMB (Code for Anisotropies in the Microwave Background) is the other
standard Boltzmann solver.

**URL:** https://github.com/cmbant/CAMB
**Language:** Fortran with Python wrapper
**Installation:** pip install camb

CAMB may be easier for some modifications as it has a built-in framework
for dark energy perturbation equations.

### 3.3 Mirror Dark Matter N-body Simulations

To compute S8 and the matter power spectrum with mirror dark matter,
we need N-body simulations that include:

- Collisional dark matter (with dark gauge interactions)
- Dark acoustic oscillations
- KK graviton cascade decays (kick velocities)

**Tools:**
- GADGET-4 (standard N-body code, can add custom forces)
- AREPO (moving-mesh hydro, better for collisional DM)
- Custom modification to add mirror sector interactions

**Complexity:** High -- weeks to months
**Output:** P(k), S8, halo mass function at various z

---

## 4. Advanced Tools (Months)

### 4.1 MCMC Parameter Estimation (Cobaya/CosmoMC)

Once we have a modified Boltzmann solver, we can run MCMC chains to:
1. Find the best-fit framework parameters given data
2. Check if the framework is consistent with all current data
3. Forecast constraints from future experiments

**Tools:**
- Cobaya (https://github.com/CobayaSampler/cobaya) -- modern, Python
- CosmoMC (https://github.com/cmbant/CosmoMC) -- Fortran, established
- MontePython (with CLASS) -- alternative

**Complexity:** High
**Output:** Posterior distributions on {L, xi, T_reheat, V(phi) params}

### 4.2 Modified Gravity Solver

For computing the scalar field (dilaton) effects on:
- Solar system tests (perihelion precession, Shapiro delay)
- Gravitational lensing
- Gravitational wave propagation

**Tools:**
- hi_class (https://github.com/miguelzuma/hi_class_public) -- CLASS
  extension for Horndeski/scalar-tensor theories
- EFTCAMB -- CAMB extension for effective field theory of dark energy

hi_class is particularly relevant because the dilaton is a specific
case of the Horndeski scalar-tensor class.

### 4.3 21cm Cosmology Tools

The 5D framework's modifications to the radiation content and dark
sector affect the 21cm signal from the dark ages:

**Tools:**
- 21cmFAST (semi-numerical simulation of 21cm signal)
- HyRec (modified recombination for extra radiation species)

---

## 5. The Minimal Viable Pipeline

To get the FIRST set of precision predictions (t_0, r_d, theta_*), the
minimal pipeline is:

### Step 1: Determine framework parameter values
    L = 130 um (from Casimir)
    xi = 0.47 (from BBN constraint midpoint)
    w_0, w_a = from dilaton dynamics calculation

### Step 2: Translate to standard cosmological parameters
    H_0 = 69.3 km/s/Mpc (from Delta_N_eff via xi)
    N_eff = 3.09 + 0.30 = 3.39 (dilaton + mirror)
    Omega_b h^2 = 0.02237 (unchanged from Planck -- framework
                  doesn't modify baryonic physics)
    Omega_cdm h^2 = from mirror matter production calculation
    w_0, w_a = from dilaton dynamics

### Step 3: Run CLASS with these parameters
    class_params = {
        'H0': 69.3,
        'omega_b': 0.02237,
        'omega_cdm': ???,  # FROM MIRROR MATTER CALCULATION
        'N_ur': 0.3066,    # Standard 1 massive + 2 massless neutrinos
        'N_ncdm': 1,       # 1 massive neutrino species
        'm_ncdm': 0.06,    # From bulk seesaw
        'w0_fld': -0.85,   # From dilaton dynamics
        'wa_fld': -0.23,   # From dilaton dynamics
        'Delta_N_eff_extra': 0.30,  # Hidden-brane radiation
    }

### Step 4: Extract predictions
    t_0 = class_output.age()        # Age of universe
    r_d = class_output.rs_drag()     # Sound horizon
    theta_s = class_output.theta_s() # Angular scale of first peak
    sigma8 = class_output.sigma8()   # Clustering amplitude

### Step 5: Compare with data
    t_0 vs 13.80 +/- 0.02 Gyr (Planck)
    r_d vs 147.09 +/- 0.26 Mpc (Planck)
    theta_s vs 1.04110 +/- 0.00031 deg (Planck)
    sigma8 vs 0.811 +/- 0.006 (Planck) and 0.76 +/- 0.02 (weak lensing)
    H_0 vs 67.4 +/- 0.5 (Planck), 73.0 +/- 1.0 (SH0ES), 69.8 +/- 0.6 (TRGB)

---

## 6. The Critical Missing Piece: Omega_cdm

The one parameter we CANNOT determine without a dedicated calculation is
Omega_cdm -- the dark matter density. In the 5D framework, this comes
from the gravitational production of mirror matter, which depends on:

1. The reheating temperature T_reheat
2. The mirror sector particle spectrum (assumed mirror SM)
3. The gravitational production cross-section (G^2 * T^5 rate)

The calculation:
    Omega_mirror * h^2 ~ (m_chi / GeV) * (T_reheat / 10^9 GeV)^3 * 
                          (g_*/100)^{-1}

For Omega_mirror * h^2 = 0.12 (observed):
    m_chi * (T_reheat / 10^9 GeV)^3 ~ 12 GeV

This gives a DEGENERACY between m_chi and T_reheat. Breaking it
requires additional constraints (BBN, CMB, structure formation).

**For now, we can treat Omega_cdm as a free parameter and see what
value the framework NEEDS to be consistent with theta_*.** If that
value is achievable by gravitational production (i.e., corresponds
to reasonable m_chi and T_reheat), the framework passes the test.

---

## 7. Priority Order

1. **Python age integral** -- immediate, simple, informative (TODAY)
2. **Dilaton ODE solver** -- determines w(z) trajectory (THIS WEEK)
3. **CLASS run with framework parameters** -- first precision test (THIS WEEK)
4. **Mirror matter production calculation** -- determines Omega_cdm (NEXT WEEK)
5. **Modified CLASS with H_b term** -- full 5D Friedmann (NEXT MONTH)
6. **N-body simulations** -- S8, structure formation (FUTURE)
7. **MCMC chains** -- full parameter estimation (FUTURE)

The first three items give us the age prediction, the sound horizon,
the CMB first peak position, and the clustering amplitude. These are
the DECISIVE first tests.
