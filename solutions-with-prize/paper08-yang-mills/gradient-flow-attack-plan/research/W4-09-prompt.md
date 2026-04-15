# W4-09: Continuum Limit of Flowed Correlators (Lemmas 2.2 + 2.3 + 2.4)

## Task
Write a rigorous proof memo establishing that (a) the lattice flowed Schwinger functions converge as a → 0 at fixed t > 0 (Cauchy estimate), (b) the limit is unique (not subsequential), and (c) the continuum flowed Schwinger functions satisfy the Osterwalder-Schrader axioms OS0-OS4.

## Statements to prove

**Lemma 2.2 (Cauchy estimate).** For Schwartz test functions f₁,...,fₙ and fixed flow time t > 0:
|S_{n,t}^{(a₁)}(f) - S_{n,t}^{(a₂)}(f)| ≤ C(t,n)·|a₁² - a₂²|^α
for some α > 0 and C(t,n) < ∞ depending on t but not on a₁, a₂.

**Lemma 2.3 (Uniqueness).** The continuum limit S_{n,t} = lim_{a→0} S_{n,t}^{(a)} exists and is unique for each fixed t > 0.

**Lemma 2.4 (OS axioms).** The continuum flowed Schwinger functions S_{n,t} satisfy OS0-OS4 at each fixed t > 0.

## Key inputs from previous waves

- **W3-08** (polymer decay): Flowed polymer activities satisfy |K_k^{(t)}(X,V)| ≤ e^{-κ(t)|X|} with κ(t) ≥ κ_B, K-uniform
- **W1-03** (heat kernel factorization): K_{M⁴×S¹}(t) = K_{M⁴}(t) ⊗ K_{S¹}(t)
- **W1-04** (established pack): Theorem K.1 (Epstein vanishing), Paper 10 Theorem 1 (scheme-independence)
- **W1-05** (analyticity in t): Balaban (B1) with k-independent radius ρ

## The model to adapt: Theorem M.2.1

The unflowed continuum limit is proved in Appendix M (Theorem M.2.1, line 169) of the mass gap preprint via a Cauchy argument on the RG telescoping sum. The structure:

1. **Telescoping:** Decompose S_n^{(K₂)} - S_n^{(K₁)} as sum of consecutive differences along dyadic sequence a₀(K) = a* · 2^{-K}
2. **Step bounds:** Each |S_n^{(K+1)} - S_n^{(K)}| ≤ (factor) · g_K⁴ · (a_K·Λ)^s via linked cluster theorem + RG
3. **Convergence:** Σ_K g_K⁴(a_KΛ)^s < ∞ (doubly exponential: ~4^{-K})
4. **Cauchy property → unique limit** in S'(R^{4n})

**The flow enhancement:** At fixed t > 0, the flow propagator contributes e^{-tp²} to each internal line. This improves the step bound from O(g_K⁴) to O(g_K⁴ · e^{-t/a_K²}). The telescoping sum converges even faster (triply exponential).

## The RG recursion structure (Section 5.4)

The outer recursion is C_{K+1} = C_K/4 + C_* + O(g_K² C_K), with:
- The 1/4 factor from bare refinement: Δ̂_{K+1}² = Δ̂_K²/4
- C_* = sup_K C_new(K), K-uniform (from spectral lemma + Hastings-Koma)
- Convergence: Σ_K C_K g_K⁴ Δ̂_K² < ∞ (doubly exponential in K)

For the flowed case, the new contribution C_new^{(t)} gets multiplied by e^{-t/a_K²}, which is exponentially small for a_K ≪ √t. This makes the flowed telescoping sum converge even when the unflowed sum would be marginal.

## OS axiom transfer (for Lemma 2.4)

From Theorem 8(f) of the preprint (Section 5.7, lines 2172-2615):

| Axiom | Unflowed source | Flowed status |
|-------|----------------|---------------|
| OS0 (temperedness) | Lines 2181-2248: ‖S_n‖ ≤ n!·C₀ⁿ | Improved: e^{-tp²} exponential UV suppression |
| OS1 (Euclidean invariance) | Lines 2252-2317: O(4)-breaking → 0 | Same: continuum flow is rotationally invariant |
| OS2 (reflection positivity) | Lines 2321-2372: Osterwalder-Seiler + weak limits | Inherited: E(t,x) = ¼G^a G^a ≥ 0 (sum of squares) |
| OS3 (symmetry) | Lines 2376-2380 | Same: flow preserves gauge covariance |
| OS4 (cluster) | Lines 2384-2423: e^{-Δ_∞ t} | Inherited: mass gap Δ_∞ independent of flow time |

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W3-08-polymer-decay.md` — flowed polymer decay
- `/Users/gsix/yang-mills/preprint/sections/M-gap-closures-r00.md` — Theorem M.2.1 (line ~169): the Cauchy argument
- `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md` — Section 5.4 (RG recursion, lines ~694-1000) and Section 5.7 (OS axioms, lines ~2172-2615)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-03-heat-kernel-factorization.md` — heat kernel on M⁴ × S¹
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/strategy/00-formal-argument.md` — Section 3.2 (Estimate 2)

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W4-09-continuum-limit-flowed.md`

## Output format
Self-contained proof memo with three sections (one per lemma):
- **Lemma 2.2:** Adapt Theorem M.2.1's Cauchy argument. State the telescoping sum explicitly. Show the flow enhancement factor e^{-t/a_K²} improves convergence. Prove the Cauchy estimate with explicit dependence on t.
- **Lemma 2.3:** Derive uniqueness as corollary of Lemma 2.2 (Cauchy in complete space).
- **Lemma 2.4:** Transfer each OS axiom from the unflowed case, with explicit justification for each. The key non-trivial step is OS2 (reflection positivity): E(t,x) is a sum of squares → lattice RP holds → Portmanteau preserves it in the limit.

Reference W3-08, W1-03, Theorem M.2.1, and Section 5.7 explicitly. Publication-quality mathematical writing.
