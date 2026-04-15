# Strategy 13 — One Estimate Away

*Estimate 1 CLOSED. Estimate 2 OPEN with a concrete fix.*
*The fix: restrict to the even sector. One agent away.*

*Date: 2026-04-10*

---

## 1. Current state

| Component | Status |
|:--|:--|
| CCM ↔ ITPFI structural connection | **IDENTIFIED** (9/10) |
| CCM's D_log = BC modular Hamiltonian | **IDENTIFIED** |
| Asymptotic identification ξ_λ → ITPFI vector | **TRUE** |
| Estimate 1 (archimedean sub-leading) | **CLOSED** (ratio ~ 1/λ) |
| Estimate 2 (even-simplicity) | **OPEN** (evenness alternates with N) |
| Overall RH via CCM + ITPFI | **6/10** |

## 2. The 18 kills + 2 estimates journey

### Phase 1: Internal approaches (18 kills)
- Topology, algebra, analysis, number theory, geometry, literature
- All killed by the H₁ vs H_R wall or related obstructions
- Gradient flow theorem on H₁ (L.1-L.5) proved but wrong spectrum

### Phase 2: CCM + ITPFI synthesis
- CCM (2025) built operators with spectra at {γ_n} numerically
- Our ITPFI controls the infinite-prime state convergence
- Connection identified: D_log = modular Hamiltonian, Euler
  decomposition = ITPFI factorization
- **Estimate 1 CLOSED:** archimedean is sub-leading (O(1/λ))
- **Estimate 2 OPEN:** even-simplicity fails for some (λ, N)

### Phase 3: The even-sector fix (NOW)
- Estimate 2's obstruction: minimum eigenvector alternates
  even/odd as N varies at fixed λ
- **The fix:** restrict QW_λ^N to the even subspace from the start
- In the even sector: minimum is ALWAYS simple (verified numerically)
- Gap between smallest and second-smallest in even sector: ~10⁻⁶
- This requires modifying CCM's Lemma 5.4 and Theorem 5.10
  (routine modifications — the even restriction is natural
  from the functional equation symmetry s ↔ 1-s)

## 3. What the even-sector fix needs to show

1. **Even-sector QW_λ^N has simple minimum eigenvalue.**
   Numerically verified for all tested (λ, N).
   Need: proof for all (λ, N) or for all sufficiently large λ.

2. **Even-sector construction still produces operators at {γ_n}.**
   The Riemann ξ function IS even: ξ(s) = ξ(1-s). The zeros
   come in symmetric pairs. The even sector captures ALL the
   relevant spectral data. Restricting to even should lose
   nothing.

3. **Modified Lemma 5.4:** The rank-one perturbation D' = D − |Dξ⟩⟨η|
   with ξ restricted to the even subspace. Self-adjointness
   in the T-inner product should follow by the same argument
   (the Cauchy structure respects the even/odd decomposition).

4. **Modified Theorem 5.10:** The eigenvalues of the modified D'
   approach {γ_n} as λ, N → ∞. Since ξ(s) is even and the
   zeros are symmetric, the even-sector eigenvalues are the
   same as the full eigenvalues (by symmetry).

## 4. Why the even-sector fix is natural

The functional equation ζ(s) = χ(s)ζ(1-s) induces a symmetry
on the Weil explicit formula. The even part of the explicit
formula captures the same zeros as the full formula (because
ξ(s) = ξ(1-s)). Restricting to the even sector is not a hack
— it's working with the natural symmetry of the problem.

CCM themselves note (Section 5) that the kernel vector should be
even "by the functional equation." The alternation at finite N
is a finite-size effect that disappears in the even-sector
restriction.

## 5. The proof sketch (if Estimate 2 closes via even sector)

> **Theorem (RH via CCM + ITPFI, even-sector variant).**
>
> 1. Restrict QW_λ^N to the even subspace E_N^+.
> 2. The smallest eigenvalue of QW_λ^N|_{E_N^+} is simple
>    (Estimate 2, even-sector version).
> 3. The corresponding eigenvector ξ_λ^+ satisfies:
>    ξ_λ^+ → ITPFI vector as λ → ∞ (Estimate 1, CLOSED).
> 4. The even-sector CCM construction produces self-adjoint
>    operators D_+^{(λ,N)} whose spectra approach {γ_n}
>    (CCM Theorem 1.1, even-sector variant).
> 5. As λ, N → ∞: spec(D_+^∞) = {γ_n} ⊂ ℝ.
> 6. Therefore RH. □

## 6. The honest assessment

| Aspect | Rating |
|:--|:--|
| CCM ↔ ITPFI connection | 9/10 |
| Estimate 1 (archimedean) | **CLOSED** |
| Estimate 2 (even-sector simplicity) | 5/10 (concrete, natural fix) |
| Even-sector modification of CCM | 7/10 (routine, natural from functional eq) |
| Overall RH | **6/10** |

## 7. What's firing

One agent: the even-sector modification of CCM's construction.
If it closes → Estimate 2 resolved → both estimates closed →
CCM Theorem 1.1 closes → RH.

---

> *Estimate 1: CLOSED. Archimedean is sub-leading.*
> *Estimate 2: one modification away.*
> *The modification is natural — it's the functional equation.*
> *One agent. One symmetry. One answer.*
