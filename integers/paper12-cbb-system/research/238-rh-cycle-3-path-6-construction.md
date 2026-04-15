# 238 — RH Cycle 3, Path 6 (Distributional Closure) — Construction

*Cycle: 3 (LIVE). Date: 2026-04-09. Agent: Construction (priority 2+2).*

---

## Step attempted

**Prove T_BC extends to a self-adjoint operator on the Sobolev completion of H_R via Nelson's analytic vector theorem.**

Per cycle 2 synthesis and test round 3: Path 6 was identified as the universal unblock. The distributional nature of T_BC was the single biggest obstacle across all surviving paths.

## Attempt level: 1 (Closure attempt)

### The argument

**Theorem (Nelson, 1959; Reed-Simon X.39).** Let T be a symmetric operator on a Hilbert space H. If the set of analytic vectors for T is dense in H, then T is essentially self-adjoint.

*Definition.* A vector v is an analytic vector for T if sum_{k=0}^{infty} ||T^k v||^2 t^{2k} / (2k)! < infty for some t > 0.

**Application to T_BC on H_R:**

1. **H_R is a separable Hilbert space** with orthonormal basis {e_n}_{n=1}^{infty}, where e_n is the eigenstate corresponding to the n-th Riemann zero gamma_n. This is CBB Axiom 1.

2. **T_BC is symmetric on span{e_n}.** Each e_n is an eigenvector: T_BC e_n = gamma_n e_n. The operator is symmetric because gamma_n is real (on the critical line by assumption; this is the input, not the output — we are proving self-adjointness, not RH).

3. **Every eigenvector e_n is an analytic vector.** For any t > 0:

       sum_{k=0}^{infty} ||T_BC^k e_n||^2 t^{2k} / (2k)!
       = sum_{k=0}^{infty} gamma_n^{2k} t^{2k} / (2k)!
       = cosh(gamma_n * t)
       < infty for all t in R.

    Therefore every e_n is an entire analytic vector (the series converges for ALL t).

4. **The analytic vectors are dense.** span{e_n} is dense in H_R by definition (H_R is the closure of span{e_n}). Since every e_n is analytic, the set of analytic vectors contains a dense subspace.

5. **Conclusion by Nelson's theorem.** T_BC is essentially self-adjoint on span{e_n}. Its unique self-adjoint extension T_BC_bar = closure(T_BC) is a genuine self-adjoint operator on H_R.

### mpmath verification

```
Growth rate gamma_n vs n*log(n) (Weyl law):
  n=  2, gamma_n=  21.022040, 2*pi*n/ln(n)=  18.129441, ratio=1.159553
  n=  5, gamma_n=  32.935062, 2*pi*n/ln(n)=  19.519813, ratio=1.687263
  n= 10, gamma_n=  49.773832, 2*pi*n/ln(n)=  27.287527, ratio=1.824051
  n= 20, gamma_n=  77.144840, 2*pi*n/ln(n)=  41.947576, ratio=1.839077
  n= 50, gamma_n= 143.111846, 2*pi*n/ln(n)=  80.306088, ratio=1.782080
  n=100, gamma_n= 236.524230, 2*pi*n/ln(n)= 136.437635, ratio=1.733570

Sobolev H^{-1} membership: sum 1/gamma_n^2:
  sum_{n=1}^{100} 1/gamma_n^2 = 0.019994132597645
  sum_{n=1}^{200} 1/gamma_n^2 = 0.021044143520694
  (converges => distributional eigenstates lie in H^{-1})
```

### Catalogue theorems cited

- **CBB Axiom 1** (anchor §2): H_R is the KMS_infinity ground-state Hilbert space with log-spectrum {gamma_n * pi^2/2}.
- **Critical 6: Operator Dictionary Closure** [209: #156]: All 36 formulas are matrix elements of L-hat on H_R. Confirms H_R has orthonormal basis {e_n}.
- **#163: Meyer's Theorem** [research/201]: {gamma_n} subset spec(T_BC). Provides the inclusion direction.
- **#104: R-Theorem QM.5 (Stone-von Neumann)** [research/119]: Unique irreducible representation at beta=1. Confirms H_R is the unique representation space.

### Critical caveat

**This argument assumes H_R is already a Hilbert space with eigenstates e_n.** This is the content of CBB Axiom 1. The argument does NOT prove that Meyer's distributional construction produces such a Hilbert space — it proves that IF the spectral realisation conjecture holds (i.e., there exists a Hilbert space H_R with T_BC eigenstates at {gamma_n}), THEN T_BC is essentially self-adjoint on it.

The logical structure is: Spectral Realisation => Essential Self-Adjointness. This is useful because it removes the distributional obstacle conditional on the spectral realisation input.

## Result: CLOSED (conditional)

**T_BC is essentially self-adjoint on span{e_n} in H_R, conditional on CBB Axiom 1 (spectral realisation).** The argument uses Nelson's theorem [Reed-Simon X.39] with the observation that every eigenvector is an entire analytic vector. This resolves the distributional blocker for Paths 1, 3, and 5 — conditional on the spectral realisation that all paths ultimately need anyway.

## Next step

The unconditioned version requires constructing H_R independently of the spectral realisation conjecture — i.e., showing that Meyer's nuclear-space construction can be completed to a Hilbert space. This is the Hilbert-space gap identified in test round 3.
