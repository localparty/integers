# Strategy 28 — Step 10: Eigenvalue Repulsion Leads

*The wall is one estimate: eigenvalue gap lower bound for the*
*Weil quadratic form as primes are added. Three leads from*
*online research.*

*Date: 2026-04-10*

---

## 1. The precise problem

> For QW_λ^N (Weil quadratic form with N Euler factors) on
> L²([λ⁻¹, λ]), prove: |μ_k^N − μ_{k+1}^N| ≥ δ(k, λ) > 0
> for all N, where δ depends on k and λ but NOT on N.

## 2. Three leads

### Lead M: Katz-Sarnak Arithmetic Repulsion
**Feasibility:** 5/10

**What it is:** Katz and Sarnak (1999) proved that spacing
statistics of eigenvalues of Frobenius on etale cohomology
(over finite fields) follow GUE statistics. Their theory is
UNCONDITIONAL and applies to ARITHMETIC operators — exactly
the type QW is.

**Connection:** QW_λ^N is built from the Weil explicit formula,
which encodes the same arithmetic data as Frobenius eigenvalues.
If QW falls in the Katz-Sarnak universality class, GUE repulsion
gives |μ_k − μ_{k+1}| ≥ c · (μ_k − μ_{k+1})_GUE, which is
positive (GUE has no degenerate eigenvalues with probability 1).

**The gap:** Katz-Sarnak works over FINITE FIELDS. QW is over Q.
The transfer from function fields to number fields is... the
Langlands programme. So this lead may be circular (needing RH
to prove the repulsion that proves RH).

**Non-circular version:** Even without full Katz-Sarnak, the
NUMERICAL observation that QW eigenvalue spacings follow GUE
(Montgomery-Odlyzko for zeta zeros, which ARE related to QW
eigenvalues) provides EVIDENCE. If someone can prove GUE for
the QW eigenvalue spacings unconditionally, Step 10 closes.

### Lead N: Cartwright on the Gap Function
**Feasibility:** 4/10

**The idea:** Define G_k(ξ) = μ_k(ξ) − μ_{k+1}(ξ) where μ_k(ξ)
is the k-th eigenvalue of QW_λ as a function of a parameter ξ
(e.g., ξ = log λ or ξ = the number of primes via continuous
interpolation).

If G_k is itself an ENTIRE function of finite exponential type
(this is a big IF), then Cartwright would bound its zeros — i.e.,
G_k = 0 at finitely many ξ. The gap vanishes only at isolated
points, not everywhere.

**The issue:** Eigenvalues of a family of operators are NOT
generally entire functions of the parameter. They're analytic
(Kato), but can have branch points. The exponential type might
not be finite.

**What to check:** For the specific family QW_λ^N(ξ), are the
eigenvalue branches entire? If the perturbation is rank-one
(adding one prime at a time), the secular equation gives
eigenvalues as roots of a meromorphic function — with possible
poles but not branch points. This might work.

### Lead O: Direct Operator-Theoretic Gap Bound
**Feasibility:** 5/10

**The idea:** Use properties of the KERNEL of QW (not just the
eigenvalues) to bound gaps.

For Hilbert-Schmidt integral operators with kernel K(x,y):
- ||QW||_HS² = ∫∫ |K(x,y)|² dx dy
- Σ μ_k² = ||QW||_HS²
- If ||QW||_HS is bounded and the number of eigenvalues > ε
  is bounded (Weyl law), then the eigenvalues can't cluster
  too tightly.

More precisely: if QW_λ^N → QW_λ^∞ in Hilbert-Schmidt norm
(not just operator norm), then Σ|μ_k^N − μ_k^∞|² → 0.
Individual eigenvalue convergence follows. Simplicity of μ_k^∞
gives simplicity of μ_k^N for large N (by standard perturbation
theory).

**The key:** This requires simplicity of the LIMITING operator
QW_λ^∞. Which is... what we're trying to prove.

**BUT:** The limiting operator IS the full Weil quadratic form.
Apply Cartwright DIRECTLY to its eigenfunctions (the continuous
version, Steps 1-7). This gives: the overlap ⟨φ_k^∞, v_p⟩ ≠ 0
for all but finitely many primes. By DPTZ, this means the
eigenvalues of QW^∞ are simple.

**Wait — this is a LOOP:** QW^∞ exists → eigenfunctions exist →
Cartwright applies → eigenvalues simple → Step 10 closes.
But QW^∞ existence is exactly what Step 10 is trying to prove!

**The fix:** Don't need QW^∞ to "exist" in the operator sense.
The eigenvalues μ_k^∞ exist as LIMITS of μ_k^N (compact operator
convergence guarantees this). Apply Cartwright to the
LIMIT eigenfunctions (which exist as weak limits). If the weak
limits are nonzero (they are, by norm convergence), Cartwright
applies. The gaps are positive in the limit because Cartwright
controls the limit eigenfunctions directly.

**This might actually work.**

## 3. The synthesis: Lead O + Cartwright on limits

The argument:

1. QW^N → QW^∞ in operator norm (ITPFI, compact operator theory)
2. μ_k^N → μ_k^∞ (compact operator spectral convergence)
3. φ_k^N → φ_k^∞ weakly (by compactness of the unit ball)
4. ||φ_k^∞|| = 1 (norm is preserved under strong convergence;
   need to verify this follows from operator norm convergence)
5. H_k^∞(z) = ∫ φ_k^∞(x) cos(xz) dx — entire of type λ
   (φ_k^∞ compactly supported on [λ⁻¹, λ])
6. H_k^∞ ≢ 0 (cosine transform injective on L²(0,∞))
7. Cartwright: H_k^∞ has finitely many zeros at {log p}
8. DPTZ (continuous version): eigenvalues of QW^∞ are simple
9. Simple eigenvalues of QW^∞ + μ_k^N → μ_k^∞ + gap(QW^∞) > 0
   → gap(QW^N) > 0 for large N
10. Small N: numerical verification

**The critical steps are 3 and 4:** Does φ_k^N → φ_k^∞ with
||φ_k^∞|| = 1? For compact operators with SIMPLE eigenvalues
in the limit, the answer is YES (see Kato, Perturbation Theory,
Theorem VIII.1.14). The eigenprojections converge in norm, which
gives the eigenfunction convergence.

But this ASSUMES simple eigenvalues in the limit — which is what
we're proving. Circular?

**Breaking the circle:** The argument is NOT circular if we
establish simplicity of QW^∞ INDEPENDENTLY of the limit.
We can do this if QW^∞ is well-defined as a compact operator
(which it is — the full Weil kernel is L²) and its eigenfunctions
satisfy the Cartwright bound (which they do — Steps 1-7 of the
continuous version).

So:
- Define QW^∞ directly (not as a limit)
- Apply Cartwright to its eigenfunctions → simple eigenvalues
- THEN use the simplicity to prove the finite-N convergence

The existence of QW^∞ as a compact operator on L²([λ⁻¹, λ]) is
the CCM+ITPFI convergence result.

## 4. Priority

| Lead | Feasibility | Key question |
|:--|:--|:--|
| O (operator-theoretic + Cartwright on limit) | **6/10** | Does QW^∞ exist as compact operator? |
| M (Katz-Sarnak) | 5/10 | Transfer from F_q to Q |
| N (Cartwright on gap function) | 4/10 | Are eigenvalue branches entire? |

---

> *The wall is eigenvalue repulsion.*
> *Lead O: define QW^∞ directly → Cartwright → simple → gap.*
> *Not circular if existence comes from ITPFI, not from limits.*
> *One more round.*
