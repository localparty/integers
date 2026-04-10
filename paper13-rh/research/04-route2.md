# research/04-route2 -- ITPFI Product-Measure Atomicity

*Date: 2026-04-10. Spectral Realisation Cycle 4, Route 2.*

## 1. The approach

The KMS_1 state omega_1 decomposes as an ITPFI (infinite tensor
product of finite type I factors):

  omega_1 = tensor_p omega_1^{(p)}

Each local factor gives a local spectral measure mu_p for the
modular Hamiltonian. The total spectral measure is the infinite
convolution product. If each mu_p is atomic and the product
preserves atomicity, the spectrum is purely discrete.

## 2. Local spectral measures

### 2a. Structure

For each prime p, the p-local factor has:
- Basis: |k> for k = 0, 1, 2, ... (p-adic valuation)
- H_mod eigenvalues: k*log(p)
- Weights: p^{-k} (from KMS at beta = 1)

### 2b. Numerical values

| p | Eigenvalue spacing | Weight decay |
|:--|:-------------------|:-------------|
| 2 | log 2 = 0.6931... | 2^{-k} |
| 3 | log 3 = 1.0986... | 3^{-k} |
| 5 | log 5 = 1.6094... | 5^{-k} |

All local measures are ATOMIC:
- Supported on discrete set {k*log(p) : k >= 0}
- Weights are geometric: p^{-k}
- Characteristic function: 1/(1 - p^{it-1})

### 2c. Fourier computation

omega_1^{(2)}(e^{itH_2}) = sum_k 2^{-k} e^{ikt*log 2}:

| t | Value |
|:--|:------|
| 0.1 | 1.9857 + 0.1372i |
| 1.0 | 1.2800 + 0.6645i |
| 10.0 | 1.3280 + 0.6666i |
| 100.0 | 1.8896 + 0.3675i |

Non-decaying oscillations confirm atomic measure (pure point of H_mod).

## 3. Product measure

The infinite convolution product has atoms at:
  {sum_p k_p * log(p) : k_p >= 0, finitely many nonzero}
  = {log(n) : n = 1, 2, 3, ...}

Weight at log(n): phi(n)/n (Euler totient ratio).

**Problem:** sum phi(n)/n diverges (~(6/pi^2)*N). The weights are
not normalizable. This is because we are on a TYPE III factor
where the 'trace' is a weight, not a state.

## 4. The critical distinction: H_mod vs T_BC

The ITPFI product computes the spectral measure of the MODULAR
HAMILTONIAN H_mod on H_1. Its spectrum is:

  spec(H_mod|_{H_1}) = closure({log n : n >= 1}) = [0, inf)

This is DENSE in R_+ and gives CONTINUOUS essential spectrum.
(Type III_1 guarantees Connes spectrum S(M) = R_+.)

T_BC is a DIFFERENT operator. Its spectrum on H_R 'should' be
{gamma_n}, but establishing this connection is the spectral
realisation problem.

The ITPFI structure tells us everything about H_mod and nothing
about T_BC.

## 5. The Bernoulli convolution question (moot)

The classical question: can infinite convolutions of atomic
measures give continuous measures?

Answer: YES. Bernoulli convolutions with contraction ratio 1/p
give absolutely continuous measures for a.e. p > 1 (Solomyak 1995).
The Erdos measure (p = golden ratio) is singular continuous.

But this is MOOT here because:
1. We computed H_mod's spectrum, not T_BC's
2. The product IS atomic (atoms at {log n}) -- just dense
3. Dense atoms with non-summable weights give continuous spectrum
   by spectral theory of type III factors

## 6. Adversarial analysis

**Is the Bernoulli convolution problem an obstruction?**

No -- the obstruction is more fundamental. The ITPFI structure
constrains the WRONG operator. Even a complete solution to the
Bernoulli convolution problem for the BC system would only
characterize spec(H_mod), which we already know (= R_+ by
type III_1).

## 7. Premise check

Does ITPFI atomicity distinguish spec(T_BC) = {gamma_n} from
spec(T_BC) = {gamma_n} + {extra}?

NO. The ITPFI product gives H_mod's spectral measure, and
H_mod has continuous spectrum regardless of what T_BC does.

## 8. Verdict

ITPFI product-measure analysis is IRRELEVANT to spectral
realisation. It characterizes the modular Hamiltonian (already
known) and says nothing about the Connes-Bost operator T_BC.

**Feasibility: 1/10 (DOWN from 3/10).**

The downgrade reflects the structural realization that ITPFI
is a tool for H_mod, not for T_BC. No refinement of the ITPFI
analysis can bridge this gap.

---

> *Each local mu_p is atomic. The product is atomic at {log n}.*
> *But we computed the wrong operator's spectrum.*
> *Route 2 is dead.*
