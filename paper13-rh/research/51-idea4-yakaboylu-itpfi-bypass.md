# Research 51 -- Idea 4: Yakaboylu W >= 0 via ITPFI Bypass

*Date: 2026-04-09*
*Status: DEVELOPED + ADVERSARIAL*
*Depends on: strategy/30 (Idea 4), strategy/07, research/12*

---

## PART A: Development

### 1. Yakaboylu's construction (arXiv:2408.15135)

On L^2([0,inf)), define R = -D - i mu(T) where D is the dilation
generator (Berry-Keating xp) and T is Bessel regularization. R is
non-symmetric (R != R^dagger). Its spectrum: zeros of
Lambda(s) = Gamma(s+1)(1 - 2^{1-s}) zeta(s) at s_n = 1/2 + i gamma_n,
assuming simplicity of zeros. R extracts a DISCRETE spectrum from
the continuum of xp via the Bessel potential.

### 2. The intertwining and positivity criterion

W: L^2([0,inf)) -> L^2([0,inf)) satisfies W R = R^dagger W.
If W >= 0, then H_W = W^{1/2} R W^{-1/2} is self-adjoint with
spectrum {gamma_n} on the real line. This is Bombieri's refinement
of Weil positivity: zeros on Re(s) = 1/2 iff W >= 0.

NON-VACUOUS: off-line zeros make S(k) = zeta(1/2+ik)/zeta(1/2-ik)
non-unitary, forcing W indefinite. (Verified in research/12 Sec 3.3.)

### 3. The ITPFI connection

BC KMS_1 state factors via Borchers (ITPFI, proved research/265):
omega_1 = tensor_p omega_1^p, H_1 = tensor_p H_p. The modular
Hamiltonian decomposes: H_mod = sum_p H_mod^p. Resolvent factors:
omega_1((s - H_mod)^{-1}) = prod_p (1 - p^{-(s+1)})^{-1}.

IF R respects this prime decomposition, W inherits: W = tensor_p W_p.

### 4. Finite-rank reduction

Each H_p is graded by occupation number v_p = 0,1,2,...  Truncating
at v_p <= M: W_p is an (M+1)x(M+1) matrix. Checking W_p >= 0 is a
finite PSD check (all eigenvalues non-negative).

### 5. Prime-by-prime RH

W = tensor_p W_p exact => W >= 0 iff W_p >= 0 for all p. Infinite
tensor product of PSD operators on stabilized product space is PSD.
RH reduces to: verify W_p >= 0 prime by prime.

### 6. Numerical test

Compute W_2, W_3, W_5 truncated at v_p <= 4 (5x5 matrices each).
Check PSD. If confirmed: identify pattern in spectrum(W_p) vs p.

---

## PART B: Adversarial

### 7. Attack: R does not decompose via Euler product

R = -D - i mu(T). D ~ H_mod decomposes as sum_p D_p. But T is a
differential operator with potential (nu^2 - 1/4)/x^2. Under
x = prod_p p^{v_p}, this potential is a PRODUCT over prime valuations,
not a sum. T does NOT factor as sum_p T_p or tensor_p T_p.
(Proved in research/12, Section 2.2.)

**Severity: FATAL.** R is built from the Mellin transform and the
functional equation, not from the Euler product. The multiplicative
structure does not survive into the Bessel regularization.

### 8. Attack: Wrong Hilbert space

ITPFI factorizes the BC GNS space H_1 (discrete basis |n>, n in N).
Yakaboylu works on L^2([0,inf)) (continuous measure). Mellin connects
them (H_BK and H_mod are conjugate, [H_BK, H_mod] = -i), but
conjugacy does NOT imply operators on one space factor on the other.
The prime decomposition is arithmetic (structure of N), not geometric
(structure of R_+).

**Severity: HIGH.** Bridging requires the equivalence map to
intertwine the prime decomposition with L^2([0,inf)) structure.

### 9. Attack: Infinite tensor product subtlety

Even granting W = tensor_p W_p, PSD implication requires EXACT
factorization (von Neumann incomplete tensor product). Approximate
factorizations do not preserve positivity in infinite dimensions.

**Severity: MODERATE.** Likely satisfiable if factorization held. Moot.

### 10. Attack: Simplicity assumption

Yakaboylu assumes simple zeros. Our Cartwright argument gives
simplicity for CCM's finite-N operators. This helps only if CCM
eigenvalues converge to the Yakaboylu spectrum -- the gap CCM
identify as equivalent to RH. Necessary but not sufficient.

**Severity: LOW.** Simplicity verified to 10^13 zeros. Standing
assumption, not the bottleneck.

---

## Verdict

**Feasibility: 3/10.** (Down from 4/10 in research/12.)

The ITPFI factorization W = tensor_p W_p is DEAD: Bessel
regularization breaks the prime decomposition (Attack 7, proved),
compounded by the Hilbert space mismatch (Attack 8). Without
factorization, the "finite check per prime" reduction fails.

Surviving fragment: the S-matrix Euler product S = prod_p S_p with
|S_p| = 1 (research/12 Sec 6.4). But |S| = 1 is weaker than W >= 0:
scattering unitarity, not full operator positivity. Extracting W >= 0
from sum_p arg(S_p(k)) appears comparably hard to RH.

**Recommendation:** Do not pursue standalone. Yakaboylu criterion is
sound but ITPFI tools cannot access it. Retain as diagnostic: if
another route proves W >= 0, ITPFI explains WHY (prime-local unitarity).
