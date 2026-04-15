# Research 28 — γ_E Elimination + Baker Inapplicability

*γ_E is provably absent from the overlaps. Baker doesn't apply.*
*The 2×2 case is the next target.*

*Date: 2026-04-10*

---

## Key results

### γ_E eliminated (PROVED)
γ_E enters B's diagonal via c(L)+w(L) = γ_E/2 + (L,π terms).
This is MODE-INDEPENDENT → contributes −γ_E·I to B's diagonal.
Uniform diagonal shift → eigenvectors UNCHANGED.
Therefore ⟨φ_k|a⟩ is γ_E-FREE.
Verified numerically to 80-digit precision.

### Baker inapplicable
⟨φ_k|a⟩ is NONLINEAR in matrix entries (eigenvector equation).
Coefficients a_n = 1/(L²+16π²n²) are transcendental.
No linearization apparent. Baker requires linear forms.

### The obstacle is geometric (transversality)
The question: does the analytic family a(L) ever become
orthogonal to an eigenspace of B(L)? This is a non-degeneracy
/ transversality question, not a transcendence question.

### Strict interlacing holds (numerical)
All tested (λ,N): zero violations. Minimum overlap ~10⁻¹·⁷ᴺ.

## Next target: 2×2 case
At N=1, the even-sector matrix is 2×2. The overlap ⟨φ₁|a⟩ is
an explicit function of λ. If it's provably nonzero for all λ,
that's the base case for induction.
