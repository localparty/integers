# A1 — CCM Construction [HEAVY]

## What the paper claims (Layer 1)

For each truncation level N with primes p ≤ P_N, Connes–Consani–Moscovici
(arXiv:2511.22755) construct:

- A Hilbert space E_N (the "Sonin space", dim 2N+1) spanned by an
  orthonormal Fourier basis {V_j}_{j=−N..N} on L²([λ^{−1}, λ]),
  L = 2 log λ.
- The even sector E_N^+ = {f : 𝒫f = f} (the parity +1 subspace).
- A Weil quadratic form QW_λ^N given by matrix elements
  ∫_0^L D(y) e^{2π i (j−k) y/L} dy where D(y) = log*(Ψ^#)(y) is
  the Weil distribution.
- A T-inner product on H = E_N / ℂ·ξ with T = QW_λ^N − ε_N·Id.
- The rank-one perturbation D' = D − |D*ξ⟩⟨η| of the naive scaling
  operator D = diag(2π j/L), where η is the Dirichlet-kernel vector.

Paper 13's Layer 1 assumes and relies on three CCM results:

1. **CCM Theorem 4.2 (self-adjointness).** D' is self-adjoint on H
   in the T-inner product. Established via the
   Carathéodory–Fejér theory applied to the moment problem on the
   Bernstein ellipse.

2. **CCM Theorem 5.10 (eigenvalue identification).** Assuming the
   minimum eigenvalue of QW_λ^N is simple and even: (i) eigenvalues
   of D' are real and simple in the even sector, (ii) they
   approximate {γ_n} with precision O(ρ^{−N}), ρ ≥ 4.27, and
   (iii) the zeros of a specific Fourier-transform rational function
   ξ̂_λ coincide with spec(D_log^{(λ,N)}).

3. **CCM Lemmas 7.2 and 7.3 (prolate approximation / Xi
   convergence).** ‖h_λ − h‖_∞ ≤ cλ^{−2} (Meixner–Schäfke) and
   k̂_λ(z) → Ξ(z) uniformly on closed substrips of |Im z| < 1/2.

Paper 13 then modifies the CCM setup by restricting everything to
the **even sector** from the outset (Section 12), because the naive
full-sector minimum eigenvector alternates between even and odd
parity in N.

## Why this is HEAVY

Because **all six layers of the proof chain rest on these CCM
results**. If any of Theorem 4.2, Theorem 5.10, or Lemma 7.3 is
wrong or misstated, the chain collapses. arXiv:2511.22755 is a
**2025 preprint** that has not been refereed. The paper explicitly
acknowledges this in its honest-accounting 8/10 rating.

The referee's job here is to check whether Paper 13's *citation* of
CCM is faithful — i.e., whether the things Paper 13 uses are things
CCM actually claims to prove, and whether the even-sector
modification preserves the CCM conclusions.
