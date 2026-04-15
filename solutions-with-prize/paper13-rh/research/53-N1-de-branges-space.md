# Research 53 -- N1: De Branges Space Embedding for Step 10

*Date: 2026-04-09. Structure: DEVELOPMENT (A) then ADVERSARIAL (B).*
*Depends on: ledger (Step 10 wall), research/52 (I2/I3 context), Cartwright core (Steps 1-7)*
*References: arXiv:2301.00421 (2023), de Branges (1968), Conrey-Li (2000)*

---

## PART A: Development

### 1. De Branges spaces H(E)

A function E is Hermite-Biehler (HB) if it is entire and |E*(z)| < |E(z)| for Im z > 0, where E*(z) = conjugate(E(conjugate(z))). The de Branges space H(E) consists of all entire functions F such that both F/E and F*/E belong to the Hardy space H^2(C+). The norm is ||F||^2 = integral_R |F(t)/E(t)|^2 dt. The reproducing kernel is

K(w,z) = [E(z)E*(w-bar) - E*(z)E(w-bar)] / [2 pi i (w-bar - z)].

H(E) is a Hilbert space of entire functions with this inner product. The theory is rigid: the space determines E up to a real entire factor, and vice versa.

### 2. Structural simplicity of zeros

The zeros of E on the real line are precisely the points where K(w,w) = 0. For E in the HB class, these zeros are SIMPLE. This is not proved by eigenvalue perturbation or gap estimates -- it follows from the positivity of the reproducing kernel: K(w,w) >= 0 with equality only at isolated points, and the derivative K'(w,w) is nonzero there. The simplicity is AXIOMATIC within the de Branges framework. Any function F in H(E) satisfies |F(x)|^2 <= ||F||^2 K(x,x), so the zeros of E control the vanishing structure of the entire space.

### 3. Connection to the Weil distribution

Under RH, the completed xi function xi(s) = (1/2)s(s-1)pi^{-s/2} Gamma(s/2) zeta(s) is an entire function of order 1 with all zeros on Re(s) = 1/2. Setting E(z) = xi(1/2 + iz), we get: E is entire, E*(z) = E(-z-bar) = xi(1/2 - iz-bar), and if all zeros are real (in the z-variable), then |E*(z)| < |E(z)| for Im z > 0. The associated H(E) is a de Branges space whose reproducing kernel vanishes exactly at the Riemann zeros (in the z-coordinate). The Hilbert-Polya programme identifies this H(E) as the spectral space of a self-adjoint operator whose eigenvalues are the zeros.

### 4. Cartwright eigenfunctions as entire functions

Our Cartwright mechanism (Steps 1-7) proves: the eigenfunctions phi_j^N of QW_lambda^N have cosine transforms Phi_j^N(z) = integral phi_j^N(x) cos(xz) dx that are entire functions of exponential type at most log(lambda). These are Paley-Wiener functions. The question: do these Phi_j^N belong to a de Branges space H(E_N) for some finite-N Hermite-Biehler function E_N? If yes, the de Branges inner product provides a norm in which the eigenvalue gap has structural content (the ordering theorem below), rather than requiring the bare analytic estimates that constitute the Step 10 wall.

### 5. The ordering theorem payoff

De Branges' ordering theorem: if F, G are in H(E) with ||F|| = ||G|| = 1 and F has a zero at a that G does not, then the zeros of F and G interlace (between consecutive zeros of F, G has exactly one zero, and vice versa). Applied to eigenfunctions: if the Phi_j^N live in H(E_N), their zeros interlace the zeros of E_N. As N grows, if E_N converges to E_inf (related to xi), the interlacing propagates a uniform separation between eigenvalues. This would give the gap bound Step 10 requires -- not from analytic estimates, but from the structural rigidity of de Branges spaces.

---

## PART B: Adversarial

### 6. Attack: Conrey-Li kills de Branges positivity

Conrey and Li (2000) showed that de Branges' specific positivity conditions -- the ones he proposed as sufficient for RH -- are NOT satisfied. De Branges' original programme required a decreasing chain of de Branges spaces with a positivity property. This was killed. HOWEVER: our approach does NOT use de Branges' positivity conditions. We use the structural simplicity of H(E) zeros, which is a theorem about the space itself, not a claim about decreasing chains. The Conrey-Li obstruction is orthogonal to what we propose.
**Severity: LOW.** Different mechanism entirely.

### 7. Attack: E = xi(1/2 + iz) assumes RH

Defining E(z) = xi(1/2 + iz) and claiming it is Hermite-Biehler REQUIRES that all zeros of xi lie on Re(s) = 1/2, i.e., requires RH. The HB condition |E*(z)| < |E(z)| for Im z > 0 fails if there exists a zero off the critical line. So Section 3 is not a proof ingredient -- it is a reformulation of RH as "E is HB." We cannot use this E in a proof of RH.
**Severity: FATAL for the naive approach.** The E_inf = xi route is circular.

### 8. Attack: no theorem connects QW eigenfunctions to any de Branges space

Section 4 asks whether Phi_j^N "live in" some H(E_N). This is a hope, not a theorem. To verify it, one would need: (a) an explicit E_N, (b) proof that Phi_j^N / E_N is in H^2, (c) proof that the de Branges norm is comparable to the L^2 norm on QW eigenfunctions. None of (a)-(c) exist. The Paley-Wiener class is much larger than any single de Branges space. Being entire of exponential type is necessary but far from sufficient for membership in H(E).
**Severity: HIGH.** The central claim is unsubstantiated.

### 9. Attack: circularity diagnosis

Even granting Section 4, the logic runs: embed Phi_j^N in H(E_N) -> de Branges simplicity -> zeros of E_N are simple -> take N to infinity -> zeros of E_inf are simple -> RH. But "zeros of E_inf are simple and real" IS RH. The de Branges framework gives simplicity of zeros of E, and if E is HB, those zeros are real. So proving E_inf is HB is equivalent to proving RH. The "structural simplicity" buys nothing unless we can independently establish E_inf is HB -- which is exactly the problem.

The only escape: work entirely at finite N. If E_N is HB for each N (which does not require RH -- it is a statement about finite prime sums), and the interlacing of Section 5 gives uniform gap bounds that survive N -> infinity, then the limit argument could work WITHOUT assuming E_inf is HB. The limit would PRODUCE RH as a consequence.
**Severity: MODERATE.** Circular in the naive form. The finite-N escape route is logically sound but requires constructing explicit E_N from the finite prime sums, which is the hard open problem.

---

## VERDICT

**Feasibility: 4/10.** The idea is genuinely new relative to the ledger -- no closed lead uses de Branges space structure. It avoids K5 (index theory), K6 (Weil/Li positivity), K7 (spectral flow), K14 (Meyer completeness), and the Conrey-Li obstacle to de Branges' original programme.

**What survives the adversarial:** The finite-N route (Section 9, escape). If one can construct Hermite-Biehler functions E_N from the finite-N Weil data (not from xi), and show the QW eigenfunctions belong to H(E_N), then the de Branges ordering theorem gives interlacing that could propagate uniform eigenvalue gaps. This does not assume RH at any step.

**What does not survive:** The naive route through E_inf = xi is circular (Attack 7). The connection from QW eigenfunctions to de Branges spaces is unproved (Attack 8). The interlacing-to-gap-bound argument (Section 5) needs rigorous development.

**Confidence: LOW-MODERATE.** The logical structure is sound in the finite-N version, but three hard sub-problems must be solved (construct E_N, prove membership, prove interlacing survives the limit). Each is currently at 2-3/10 individually.

**Recommendation:** Record as N1 in ledger at 4/10. Do NOT promote to active pursuit until at least one of: (a) explicit E_N constructed for small N and tested numerically, (b) a theorem connecting Paley-Wiener functions of finite type to specific de Branges spaces, (c) external progress on Hilbert-Polya via de Branges (monitor arXiv:2301.00421 follow-ups).
