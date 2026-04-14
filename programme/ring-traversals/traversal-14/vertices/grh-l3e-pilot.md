# GRH L3e Pilot: [D_{N,χ}, D_{N,χ̄}] = 0

*Paper 13b. Date: 2026-04-14. Traversal 14, pilot for T13 gap in χ⊕χ̄ symmetrization.*

## 1. Setup (from T10 §1)

D_{N,χ} := A^{ev}(λ,N) ⊗ I + I ⊗ M_χ   on   E_N^+ ⊗ ℓ^2((Z/qZ)^*, χ)

where A^{ev}(λ,N) is the CCM self-adjoint (2N+1)-dim prolate-basis matrix, and
- **Real χ** (e.g. χ_{-4} = (-4/·)): M_χ = diag(χ(p_k)·log p_k), entries in {−log p_k, 0, +log p_k} ⊂ ℝ
- **Complex χ**: M_χ = diag(log p_k + i·arg χ(p_k)), entries in ℂ, normal but not self-adjoint; work with D_{N,χ}^{sym} = (D_{N,χ} + D_{N,χ}^*)/2

## 2. Commutator reduction

Tensor-structure expansion (cross terms vanish identically):
[D_{N,χ}, D_{N,χ̄}] = [A^{ev}⊗I, A^{ev}⊗I] + [A^{ev}⊗I, I⊗M_χ̄] + [I⊗M_χ, A^{ev}⊗I] + [I⊗M_χ, I⊗M_χ̄] = I ⊗ [M_χ, M_χ̄].

So L3e ⟺ [M_χ, M_χ̄] = 0.

## 3. Computation of [M_χ, M_χ̄]

**Case A (real χ, χ̄ = χ):** M_χ̄ = M_χ. [M_χ, M_χ] ≡ 0. TRIVIAL.

**Case B (complex χ):** M_χ = diag(log p_k + i·arg χ(p_k)), M_χ̄ = diag(log p_k + i·arg χ̄(p_k)) = diag(log p_k − i·arg χ(p_k)). Both matrices are diagonal in the **same prime-indexed basis** {e_{p_k}}. Two diagonal operators in a common eigenbasis commute: for any diagonals D_1 = diag(a_k), D_2 = diag(b_k), (D_1 D_2)_{kk} = a_k b_k = b_k a_k = (D_2 D_1)_{kk} and all off-diagonals are 0. Hence [M_χ, M_χ̄] = 0.

**Case B' (symmetrized, complex χ):** D_{N,χ}^{sym} has χ-block (M_χ + M_χ*)/2 = diag(log p_k · cos(arg χ(p_k))), still diagonal in {e_{p_k}}. D_{N,χ̄}^{sym} likewise diagonal in {e_{p_k}}. Commutator vanishes by the same argument.

## 4. Why cross terms vanish (explicit check)

[A^{ev}⊗I, I⊗M_χ̄] = (A^{ev}⊗I)(I⊗M_χ̄) − (I⊗M_χ̄)(A^{ev}⊗I) = A^{ev}⊗M_χ̄ − A^{ev}⊗M_χ̄ = 0. ✓

Tensor products on independent factors always commute, independent of the operators' internal structure. This is factor-algebraic, not numerical.

## 5. Verdict

**L3e: PROVED (trivially).**

The commutation [D_{N,χ}, D_{N,χ̄}] = 0 holds unconditionally from the diagonal structure of M_χ in the prime-indexed basis and the tensor-product splitting. No constant, no estimate, no large-N limit: it is an algebraic identity in the defining basis of T10 §1.

**Consequence:** T13's gap in the χ⊕χ̄ symmetrization closes. GRH L3-complex closes modulo L3 itself (which remains CONDITIONAL on L5c as flagged in T10 §4). L3e is not a wall; the actual wall is unchanged at L5c H^1 Fourier cancellation.
