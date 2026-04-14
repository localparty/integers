# GRH L3 Symmetrization for Complex χ -- Traversal 13

*Closes T10 gap on D_{N,χ} self-adjointness for complex χ. Date: 2026-04-14.*

## 1. Setup

Let χ be a primitive Dirichlet character mod q, complex (i.e. χ ≠ χ̄). From T10:
D_{N,χ} = A^{ev}(λ,N) ⊗ I + I ⊗ M_χ on E_{N,χ}^+, with M_χ = diag(log p_k + i·arg χ(p_k)). For complex χ, M_χ is **not** Hermitian, so D_{N,χ} is not self-adjoint.

Key identity: D_{N,χ}^* = A^{ev}(λ,N) ⊗ I + I ⊗ M_χ^* = D_{N,χ̄}, since arg χ̄(p) = −arg χ(p), and M_χ^* = M_χ̄ via the natural antiunitary identification E_{N,χ}^+ ≃ E_{N,χ̄}^+ (complex conjugation on the character factor).

## 2. Symmetrized operator

**Definition.** Let H_{sym} := E_{N,χ}^+ ⊕ E_{N,χ̄}^+ and
  D_N^{sym} := [[0, D_{N,χ}], [D_{N,χ̄}, 0]]      (anti-diagonal block form)
equivalently D_N^{sym} = D_{N,χ} ⊗ σ_+ + D_{N,χ̄} ⊗ σ_− where σ_± are the Pauli ladder operators.

**Lemma (Self-adjointness).** D_N^{sym} is self-adjoint on H_{sym}.

*Proof.* (D_N^{sym})^* has blocks (D_{N,χ̄})^* in the (1,2) slot and (D_{N,χ})^* in the (2,1) slot. But (D_{N,χ̄})^* = D_{N,χ} and (D_{N,χ})^* = D_{N,χ̄} by the identity above. So (D_N^{sym})^* = D_N^{sym}. ∎

## 3. Spectral analysis

**Lemma (Spectrum).** Let {μ_n} = spec(D_{N,χ}) (possibly complex). Then
  spec(D_N^{sym}) = {±√(μ_n · μ̄_n) : n} = {±|μ_n|},
*all real*, and the squared operator (D_N^{sym})^2 is block diagonal with blocks D_{N,χ} D_{N,χ̄} and D_{N,χ̄} D_{N,χ}.

Moreover, eigenvectors of D_N^{sym} at eigenvalue +|μ_n| are of the form (v_n, (μ̄_n/|μ_n|) v_n') where D_{N,χ} v_n' = μ_n v_n and D_{N,χ̄} v_n = μ̄_n v_n'. 

## 4. Equivalence to GRH(χ)

**Theorem (Spectral reality ⇔ GRH(χ)).** Assume the Hurwitz–convergence step (L5) so that μ_n(λ,N) → γ_{n,χ} as λ,N→∞, where γ_{n,χ} ∈ C is the imaginary ordinate of the n-th nontrivial zero of L(s,χ) (complex iff the zero is off the critical line). Then the following are equivalent:

(i)  All γ_{n,χ} are real (i.e. every nontrivial zero of L(s,χ) lies on Re s = 1/2).
(ii) In the limit, μ_n = μ̄_n for all n (equivalently, μ_n ∈ R).
(iii) spec(D_N^{sym}) → {±γ_{n,χ}} in the limit, and the two anti-diagonal blocks synchronize: D_{N,χ} and D_{N,χ̄} become simultaneously diagonalizable with **identical** spectra.

*Proof.* (i)⇒(ii): If γ_{n,χ} ∈ R, then μ_n ∈ R in the limit, and γ_{n,χ̄} = γ_{n,χ} (functional equation L(s,χ̄) = ε(χ̄) L(1−s,χ)̄ relates the two L-functions; their imaginary ordinates are complex conjugates, and conjugation of a real is itself). (ii)⇒(iii): block-diagonalization is immediate once μ_n = μ̄_n. (iii)⇒(i): the self-adjointness of D_N^{sym} gives real spec(D_N^{sym}). But |μ_n| being real is automatic; the *content* is that the eigenvalues of D_{N,χ} alone (which live in the squared blocks) coincide with those of D_{N,χ̄}, forcing μ_n = μ̄_n, hence γ_{n,χ} ∈ R. ∎

## 5. Verdict

**Does this close L3 for complex χ rigorously?** PARTIAL.

- Self-adjointness of D_N^{sym}: CLOSED rigorously (§2 lemma is a one-line block calculation).
- Spectrum real: immediate from self-adjointness.
- **Gap**: the implication (iii)⇒(i) is the nontrivial direction. Self-adjointness of D_N^{sym} alone gives |μ_n| ∈ R, *not* μ_n ∈ R. The extra content needed is that D_{N,χ} and D_{N,χ̄} are **simultaneously unitarily diagonalizable** (i.e. their difference commutes with the average), which is equivalent to μ_n = μ̄_n — i.e. GRH(χ) itself. Without this, the symmetrization produces a self-adjoint operator whose spectrum {±|μ_n|} is compatible with μ_n having arbitrary phase, and so *does not imply* GRH(χ).

**Conclusion**: the χ⊕χ̄ symmetrization resolves the *technical* self-adjointness question (so the operator is well-defined on H_{sym}), but it does **not** by itself close the GRH(χ) implication. To close L3 for complex χ we additionally need either: (a) a *commutation* argument [D_{N,χ}, D_{N,χ̄}] = 0 (conjecturally true from ITPFI tensor structure, needs proof), OR (b) use the off-diagonal symmetrization as a scaffold and derive GRH(χ) from the *joint* spectrum via an independent Hurwitz-type bound on both χ and χ̄ simultaneously — effectively L5 for a pair of characters.

Recommendation: mark L3-complex as **PARTIAL-PROVED** (self-adjoint scaffold built), and promote "[D_{N,χ}, D_{N,χ̄}] = 0" to a new sublemma L3e to be discharged via the BC tensor product (σ_t^χ and σ_t^χ̄ commute because their generators multiply diagonally). If L3e closes, the full GRH(χ) implication follows. Pilot: verify [D_{N,χ}, D_{N,χ̄}] = 0 for χ mod 5 (smallest complex character, order 4) at N=60.
