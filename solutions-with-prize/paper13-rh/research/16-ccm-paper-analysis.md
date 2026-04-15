# CCM "Zeta Spectral Triples" (arXiv:2511.22755) -- Detailed Analysis

## 1. The Operator D_log^{(lambda,N)}: Exact Construction

### Space
The operator acts on the Hilbert space L^2([lambda^{-1}, lambda], d*u) where d*u = du/u,
with periodic boundary conditions inherited from the scaling operator.

### Construction (step by step)

**Step 1: The Weil quadratic form QW_lambda.**
Start from the Weil explicit formula (eq 3.10):
$$QW(f,g) = \Psi(f^* * g), \quad \Psi(F) := W_{0,2}(F) - W_\mathbb{R}(F) - \sum_p W_p(F)$$
Restrict QW to L^2([lambda^{-1}, lambda], d*u). This gives the semilocal form QW_lambda.

**Step 2: The basis V_n and the matrix.**
The basis is V_n(u) := U_n(log(lambda u)) for n in {-N,...,N}, where U_n(x) = L^{-1/2} exp(2pi inx/L)
with L = 2 log lambda. The matrix of QW_lambda in this basis is (eq 5.2):

   tau_{i,i} = a_i,    tau_{i,j} = (b_i - b_j)/(i - j) for i != j

where a_{-j} = a_j and b_{-j} = -b_j. This is a REAL SYMMETRIC matrix. The off-diagonal
entries have the special Cauchy-like structure (b_i - b_j)/(i - j).

**Step 3: Truncation to QW_lambda^N.**
Take the restriction of QW_lambda to the span of V_n for |n| <= N, giving a (2N+1) x (2N+1)
real symmetric matrix T = QW_lambda^N.

**Step 4: The rank-one perturbation.**
Let epsilon_N be the smallest eigenvalue of QW_lambda^N, assumed simple and "even-simple" (Definition 5.3).
Let xi be the corresponding even eigenvector, normalized by delta_N(xi) = 1 where
delta_N = (1/sqrt{L}) sum_{n=-N}^{N} V_n is the Dirichlet kernel (eq 5.15).

Then (Theorem 5.10, Lemma 5.4):

$$D_{log}^{(\lambda,N)}(\beta) = D_{log}^{(\lambda)}(\alpha), \quad \forall \beta = \alpha + x\xi, \quad \alpha \in \text{Ker}\,\delta_N$$

The operator decomposes the space E_N as a DIRECT SUM:
$$E_N = E'_N \oplus E_N^\perp$$
where E'_N = E_N / C xi (quotient by the radical of T).

On E'_N, the inner product is given by QW_lambda^N - epsilon_N <|> (Lemma 5.4, ii).

**The key identity (eq 5.3):**
$$DT - TD = |\beta><\eta| - |\eta><\beta|$$
where D = diag(n), beta = sum b_j V_j, eta = sum V_j.

Lemma 5.4 gives:
$$D' := D - |D\xi><\eta|$$
is selfadjoint in the Hilbert space with inner product <f|g>_T = <Tf|g>.

This is the EXACT rank-one perturbation: D' = D - |D xi><eta|.

The full perturbed scaling operator is:
$$D_{log}^{(\lambda,N)}|_{E'_N} = \frac{2\pi}{L} D'' \quad (\text{eq 5.26})$$

where D'' is the operator induced by D' on the quotient E_N/C xi.


## 2. The Rank-One Perturbation Structure: NOT Between N and N+1 Primes

**Critical finding:** The rank-one perturbation in CCM is NOT the passage from N primes
to N+1 primes. Instead:

- The perturbation is: given a FIXED truncation (fixed lambda, fixed N), one perturbs
  the diagonal scaling operator D = diag(n) by a rank-one correction that inserts the
  minimal eigenvector xi into the kernel.

- The formula is: D' = D - |D xi><eta| (Lemma 5.4)

- This makes D' selfadjoint with respect to the WEIL inner product <f|g>_T = <Tf|g>.

**Where primes enter:** The primes enter ONLY through the Weil quadratic form QW_lambda,
specifically through the sum over prime contributions W_p (eq 3.10, 3.16):
$$W_p(F) = (\log p) \sum_{m=1}^{\infty} p^{-m/2} (F(p^m) + F(p^{-m}))$$

The truncation to finitely many primes is controlled by the parameter x = lambda^2:
only primes p <= x = lambda^2 contribute (eq 4.3):
$$\sum W_p(V_n, V_m) = \sum_{1 < k \le \exp(L)} \Lambda(k) k^{-1/2} q(U_n, U_m)(\log k)$$

So the Euler product enters ADDITIVELY through the quadratic form, not multiplicatively
through the operator. Each prime p contributes an additive correction to the matrix tau_{n,m}.


## 3. The Euler Product: Additive in the Quadratic Form

The Weil functional decomposes as (eq 3.13):
$$\Psi^\sharp = W_{0,2}^\sharp - W_\mathbb{R}^\sharp - \sum_p W_p^\sharp$$

Each prime p contributes (eq 3.16):
$$W_p^\sharp(F) = (\log p) \sum_{m=1}^{\infty} p^{-m/2} F(p^m)$$

The matrix QW_lambda(V_n, V_m) decomposes as:
- W_{0,2}(V_n, V_m): a rank-two matrix (Lemma 4.1, eq 4.2)
- W_R(V_n, V_m): the archimedean contribution (Proposition 4.3)
- sum_p W_p(V_n, V_m): finite sum over primes p <= lambda^2

When lambda increases so that a new prime p_{N+1} enters (i.e., p_{N+1} <= lambda^2 < p_{N+2}),
the matrix T changes by the ADDITIVE contribution of W_{p_{N+1}}.

The contribution of a single prime p to the matrix is:
$$\Delta\tau_{n,m}^{(p)} = (\log p) \sum_{j=1}^{\lfloor L/\log p \rfloor} p^{-j/2} q(U_n, U_m)(j \log p)$$

Using (2.9) and (2.10), the q functions are:
- q(U_n, U_m)(y) = [sin(2pi m|y|/L) - sin(2pi n|y|/L)] / [pi(n-m)] for m != n
- q(U_n, U_n)(y) = 2(1 - |y|/L) cos(2pi ny/L) for m = n

The key point: the contribution of prime p is NOT rank-one in general. Each prime
contributes a matrix with entries evaluated at y = j log p for j = 1, 2, ..., and the
rank equals the number of prime powers p^j with p^j <= lambda^2.


## 4. The Caratheodory-Fejer Theorem: Self-Adjointness Guarantee

The theoretical foundation rests on [7] (Connes-van Suijlekom, Comm. Math. Phys. 2025).

**Theorem (from [7]):** The matrix tau_{n,m} with the structure
$$\tau_{i,j} = (b_i - b_j)/(i - j) \quad (i \neq j), \quad \tau_{i,i} = a_i$$
is real symmetric. This is the key Toeplitz-like structure.

The connection to Caratheodory-Fejer (reference [2]): the 1911 theorem guarantees that
certain Toeplitz matrices associated with functions whose zeros lie on the critical line
are positive semidefinite. The generalization in [7] extends this to the matrix structure
above, ensuring that QW_lambda >= 0 forces all zeros of the associated function to lie on
Re(s) = 1/2.

Specifically, Corollary 3.8 states:
**If lim_{lambda -> infinity} mu_lambda = 0 (where mu_lambda is the smallest eigenvalue of QW_lambda),
then RH holds.**

The self-adjointness of D_{log}^{(lambda,N)} then follows from Lemma 5.4(ii): D' is selfadjoint
with respect to <f|g>_T = <Tf|g> because T has the special Cauchy structure, and the
rank-one perturbation preserves self-adjointness in the T-inner product.


## 5. Numerical Precision

### Figure 1 (lambda = 3, N = 120):
First 20 zeros of zeta(1/2 + is) vs eigenvalues of D_{log}^{(lambda,N)}:

| Zero # | Error |
|--------|-------|
| rho_1 | 1.6 x 10^{-34} |
| rho_2 | 2.1 x 10^{-31} |
| rho_3 | 1.5 x 10^{-29} |
| rho_5 | 1.3 x 10^{-25} |
| rho_10 | 8.8 x 10^{-18} |
| rho_20 | 2.4 x 10^{-7} |

### Table 1 (N = 120, first 50 zeros):

| Zero # | lambda = sqrt{12} | lambda = sqrt{13} | lambda = sqrt{14} |
|--------|-------------------|-------------------|-------------------|
| 1 | 3.41 x 10^{-50} | 2.44 x 10^{-55} | 1.07 x 10^{-60} |
| 10 | 2.99 x 10^{-32} | 3.98 x 10^{-37} | 2.96 x 10^{-42} |
| 20 | 9.55 x 10^{-20} | 3.54 x 10^{-24} | 6.19 x 10^{-29} |
| 30 | 2.72 x 10^{-11} | 4.21 x 10^{-15} | 2.39 x 10^{-19} |
| 40 | 1.83 x 10^{-4} | 2. x 10^{-7} | 5.24 x 10^{-11} |
| 50 | 9.02 x 10^{-2} | 2.04 x 10^{-3} | 4.78 x 10^{-6} |

**Key observation:** The error grows exponentially with zero number and decreases
exponentially with lambda. Increasing lambda^2 from 12 to 14 gains roughly 5 orders
of magnitude per zero. The dependence is approximately:

   error(rho_k, lambda) ~ exp(-c * lambda * (something - k))

The probability of these matches being coincidental is estimated at 10^{-1235} (page 2).


## 6. The Convergence Gap: What CCM Say

### Section 7 "Outlook" (page 27):
CCM conjecture TWO limits must be taken:

1. **Fixed lambda, N -> infinity:** For fixed lambda, the functions det_reg(D_{log}^{(lambda,N)} - s)
   converge (when N -> infinity) to -i lambda^{-iz} hat{xi}_lambda(z) where xi_lambda is the
   eigenfunction of QW_lambda for the smallest eigenvalue (Theorem 5.10).

2. **lambda -> infinity:** The functions hat{xi}_lambda(z), suitably normalized, converge
   uniformly on closed substrips |Im(z)| < 1/2 towards the Xi-function of Riemann (Lemma 7.3).

### Section 8 "The Missing Steps" (page 32):
Two essential steps are explicitly identified as MISSING:

**(Missing Step 1):** Prove that the smallest eigenvalue of QW_lambda is SIMPLE and its
eigenvector is EVEN ("even-simple" condition). This is known for the prolate wave
operator PW_lambda but NOT yet proved for QW_lambda itself.

**(Missing Step 2):** Establish that k_lambda (the prolate wave approximation, eq 7.6)
provides a sufficiently accurate approximation to xi_lambda to justify convergence of
the zeros of hat{xi}_lambda toward zeta(1/2 + is).

### Lemma 7.2 provides partial progress:
The prolate spheroidal eigenfunctions h_{n,lambda} satisfy:
$$\max_{x \in [-\lambda, \lambda]} |h_{n,\lambda}(x) - h_n(x)| \le c \lambda^{-2}$$
for n = 0, 4 (the relevant Hermite functions).

### Lemma 7.3 proves:
The Fourier transform of k_lambda converges to the Xi-function as lambda -> infinity,
uniformly on closed substrips |Im(z)| < 1/2. This is a PROVED result.

**The gap is therefore:** connecting k_lambda to xi_lambda rigorously, not the convergence
of k_lambda to Xi.


## 7. The Perturbation Norm: Scaling Analysis

### Within the CCM framework (D' = D - |D xi><eta|):
The perturbation R = -|D xi><eta| has:
- ||R|| = ||D xi|| since ||eta|| = (2N+1)^{1/2} but <xi|eta> = 1 (normalized)
- More precisely: R = -|D xi><eta| is rank one with ||R||_{op} = ||D xi|| * ||eta||
  but restricted by the constraint <xi|eta> = 1.

Since D xi has components (j * xi_j) for j in {-N,...,N}, we get:
$$||D\xi||^2 = \sum_{j=-N}^{N} j^2 |\xi_j|^2$$

The eigenvector xi is smooth (it is the minimal eigenvector of a Weil quadratic form),
so its Fourier coefficients decay. But ||D xi|| grows with N.

### When a new prime p enters (lambda^2 crosses p):
The change in the matrix T is:
$$\Delta T^{(p)} = -W_p(V_n, V_m)$$

The leading term (j=1 only) gives entries of order log(p) * p^{-1/2}.
The operator norm of this additive perturbation scales as:
$$||\Delta T^{(p)}|| \sim C(N) \cdot \frac{\log p}{\sqrt{p}}$$

where C(N) depends on the matrix size. Since the entries of W_p are bounded by
log(p) * p^{-1/2} * (2N+1), we get:
$$||\Delta T^{(p)}|| \le (2N+1) \cdot \frac{\log p}{\sqrt{p}}$$

**This is the critical scaling:** the prime contribution decays as (log p)/sqrt{p},
which is summable over primes (the sum converges). This is why the quadratic form
converges as lambda -> infinity.


## 8. Connection to ITPFI

### CCM's Euler product structure:
The Weil functional Psi decomposes as:
$$\Psi(F) = W_{0,2}(F) - W_\mathbb{R}(F) - \sum_p W_p(F)$$

Truncating to primes p <= lambda^2 gives QW_lambda.

### ITPFI connection:
The ITPFI type III_1 factor uses omega_1 = tensor_p omega_1^p where each factor state
omega_1^p has eigenvalue list {p^{-k}: k = 0, 1, 2, ...} with the SAME Euler product structure.

The truncated state omega_1^{<= P_N} = tensor_{p <= P_N} omega_1^p is an ITPFI_N factor.

**The connection is structural but not direct:**

1. **Same Euler product:** Both CCM's QW_lambda^N and our omega_1^{<= P_N} use exactly
   the same restricted Euler product over primes p <= x.

2. **Same additive structure in log:** The Weil form uses W_p which involves
   log(p) * sum p^{-m/2} F(p^m). The ITPFI modular operator Delta has
   log Delta = sum_p log Delta_p, which is ADDITIVE over primes just as the
   Weil form is.

3. **The (log p)/sqrt{p} scaling:** In CCM, each prime contributes with weight
   (log p) * p^{-1/2}. In the ITPFI, the modular automorphism sigma_t gives
   sigma_t^p(x) = Delta_p^{it} x Delta_p^{-it} with Delta_p having eigenvalues p^{-k}.

4. **Critical observation:** CCM's D_{log}^{(lambda,N)} acts on functions on
   [lambda^{-1}, lambda] with d*u = du/u, which is the MULTIPLICATIVE group R_+^*.
   The ITPFI modular flow also acts on R_+^* (the modular flow parameter).
   The scaling operator D_{log} = -iu d/du generates the scaling group on R_+^*,
   which IS the modular automorphism group.

5. **Potential bridge:** The CCM eigenvector xi_lambda, whose Fourier transform
   hat{xi}_lambda(z) gives the regularized determinant via Theorem 5.10, should be
   related to the vector state implementing omega_1^{<= P_N} in the GNS representation
   of the ITPFI factor. The "even-simple" condition on xi corresponds to the
   KMS condition on omega.

**However:** CCM do not discuss von Neumann algebras, ITPFI factors, or modular theory
anywhere in the paper. The connection would need to be constructed.


## 9. The Sonin Space

The Sonin space is NOT mentioned anywhere in the CCM paper.

The relevant spaces in CCM are:
- W(R_+^*): the Weil class of functions on R_+^* (Section 3)
- E_N: the finite-dimensional subspace spanned by V_n for |n| <= N
- The domain of QW_lambda in L^2([lambda^{-1}, lambda], d*u)

Meyer's S space (the Sonin space) would be the space of functions f in L^2(R_+^*)
whose Mellin transform hat{f}(s) vanishes at all zeros of zeta. CCM's approach
bypasses this: instead of working with S directly, they work with the Weil quadratic
form QW which encodes the zeros through the explicit formula.

The connection is: QW(f,f) >= 0 for all f is equivalent to RH (by Weil's criterion).
The Sonin space S is the kernel of QW (i.e., S = {f : QW(f,f) = 0}) when RH holds.
So CCM's mu_lambda -> 0 (Corollary 3.8) is detecting whether S is nonempty in the
limit lambda -> infinity.


## 10. Directly Usable Results

### Theorem 5.10 (Main theorem):
If QW_lambda^N is even-simple with smallest eigenvalue epsilon_N, then:
- D_{log}^{(lambda,N)} is selfadjoint on E'_N + E_N^perp
- det_reg(D_{log}^{(lambda,N)} - z) = -i lambda^{-iz} hat{xi}(z)
- All zeros of hat{xi} are real and coincide with Spec(D_{log}^{(lambda,N)})

**This can be cited directly** to justify that spectral triples with the correct
critical-line zeros exist for each finite truncation.

### Corollary 3.8:
lim_{lambda -> infinity} mu_lambda = 0 implies RH.

**This gives the target:** our ITPFI framework needs to produce mu_lambda -> 0.

### Lemma 7.3:
The Fourier transform of k_lambda converges to Xi uniformly on |Im(z)| < 1/2.

**This is proved.** It means the prolate wave approximation works; the gap is
connecting it to the actual QW_lambda eigenvector.

### The numerical precision data:
The table on pages 25-27 provides concrete evidence that can be cited as
motivation for the convergence conjecture.

### Lemma 5.2 (rank-one structure):
The identity DT - TD = |beta><eta| - |eta><beta| is proved and gives the
EXACT algebraic structure of the perturbation. This can be cited for any
argument involving commutators of D with the Weil form.

### Proposition 5.9 (Fourier transform of eigenvector):
The Fourier transform hat{xi}(z) = 2 L^{-1/2} sin(zL/2) (sum xi_j / (z - 2pi j/L))
gives an EXPLICIT formula for the regularized determinant in terms of eigenvector
components. This could be used to connect to ITPFI spectral data.
