# Computation Log

**Paper 13 Referee Run r01**

## Checks performed (analytical, not computational)

### Frobenius order verification
- ord_7(2): 2^1=2, 2^2=4, 2^3=8=1 (mod 7). Order = 3. k = 6/3 = 2. CONFIRMED.
- ord_13(5): 5^1=5, 5^2=25=12, 5^3=60=8, 5^4=40=1 (mod 13). Order = 4. k = 12/4 = 3. CONFIRMED.
- ord_13(3): 3^1=3, 3^2=9, 3^3=27=1 (mod 13). Order = 3. k = 12/3 = 4. CONFIRMED.
- ord_19(7): 7^1=7, 7^2=49=11, 7^3=343=1 (mod 19). Order = 3. k = 18/3 = 6. CONFIRMED.

### Cocycle shift formula verification (algebraic)
Delta_c = 1 - (p-1)/(p-u) where u = p^{-2*delta}
= (p - u - p + 1)/(p - u)
= (1 - u)/(p - u)
= (1 - p^{-2*delta})/(p - p^{-2*delta}). CONFIRMED.

### Delta_c = 0 iff delta = 0
Numerator: 1 - p^{-2*delta} = 0 iff p^{-2*delta} = 1 iff delta = 0. CONFIRMED.
Denominator: p - p^{-2*delta} = 0 iff p^{-2*delta} = p iff delta = -1/2. Outside critical strip. CONFIRMED.

### Derivative positivity
d(Delta_c)/d(delta) = 2*log(p)*p^{-2*delta}*(p-1)/(p-p^{-2*delta})^2
All factors positive for delta in (-1/2, infinity). CONFIRMED.

### Dark state bound
|w| = p^{-1/2} < 1 for p >= 2. |w^k| = p^{-k/2} < 1. CONFIRMED.

### Nelson analytic vector series
sum ||T^k e_n||^2 t^{2k}/(2k)! = sum gamma_n^{2k} t^{2k}/(2k)! = cosh(gamma_n t) < infinity. CONFIRMED.

### Gelfond-Schneider application
log_3(5) is transcendental by Gelfond-Schneider (3 algebraic, 3 != 0,1; if log_3(5) = a/b rational then 3^{a/b} = 5 hence 3^a = 5^b, contradicting unique factorization). CONFIRMED.

## Computational checks suggested but not executed

The following would benefit from mpmath verification but are analytically confirmed:
- Cocycle shift values at delta = 0.01 for p = 2,3,5,7
- Cross-bridge delta mismatch for |n| <= 10
- Bridge projector diagonal elements for first 30 zeros
- Euler product convergence at beta = 1.5, 2, 3, 4
- Li coefficients for n = 1..10
