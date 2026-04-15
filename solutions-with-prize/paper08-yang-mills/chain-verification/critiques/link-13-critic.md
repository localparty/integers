# Link 13 Critic Verdict: Σ C_k g_k^4 Δ̂_k² < ∞

**Verdict: SURVIVED**

## Attack-by-attack summary

**AV1 — g_k^4 decay rate sufficient?** The sum runs over the *outer*
bare-refinement index K, not the inner Balaban steps. The bare
coupling runs as g_K^2 ~ 1/(b_0 K log 2), giving g_K^4 ~ 1/K^2.
Combined with the doubly-exponential factor Δ̂_K^2 ~ 4^{−K} from
outer lattice refinement a_0(K) = a*/2^K, the general term is
~K^{γ−2}·4^{−K}, which decays faster than any power law. The 1/K^2
factor alone would make the sum conditionally tricky, but 4^{−K}
dominates and ensures absolute convergence. Attack fails.

**AV2 — Does Δ̂_k grow under RG?** Under the *inner* Balaban steps
(fixed K), Δ̂_k^(K) = 2^{k−K} a* Δ_phys grows with k — the paper
acknowledges this explicitly (§5.1.0). However, the convergence sum
at issue runs over the *outer* K index at fixed inner k=0, where
Δ̂_K^2 = (a* Δ_phys)^2 · 4^{−K} shrinks exponentially. The inner
steps are handled separately via the polymer bound for k < k_0(K)
(non-perturbative) and the one-loop estimate for k ≥ k_0(K); their
contribution is absorbed into C_K(k=0) ≤ C_0^{cl} (§5.4.6). No
divergence from gap growth. Attack fails.

**AV3 — Sum range.** The paper is explicit: the convergence sum is
over K = 0, 1, 2, … (outer bare-refinement index, §5.4.6). Strong-
coupling inner steps k < k_0(K) are handled by the polymer bound and
contribute a finite total absorbed into the K=0 starting constant.
No ambiguity in range. Attack fails.

**AV4 — Uniform-in-N convergence.** The constant C_* appearing in
the recursion C_{K+1} ≤ C_K/4 + C_* is declared "K-uniform" via the
Hastings–Koma spectral lemma (§5.5.3 Step 3(i)) and Appendix M.
However, the paper does not address uniformity in gauge-group rank N.
The one-loop coefficient b_0 = 11N/(48π²) grows with N, which
*accelerates* asymptotic freedom (larger b_0 means faster decay of
g_K^2), so larger N only improves the convergence of g_K^4 ~ 1/(b_0 K
log 2)^2. The polymer-bound constant C_{np} = Σ_X e^{−κ_B|X|}|X|^2
and the Hastings–Koma constant C_p^* depend on κ_B from Balaban's
work; κ_B ~ O(1) in physical units per Dimock 2011 Thm 3.1, but the
paper does not verify κ_B is uniform in N. For fixed N (the theorem's
actual scope: SU(N) for each fixed N) this is not a gap. Large-N
uniformity is neither claimed nor needed. Attack fails for the stated
theorem; no large-N pathology within fixed-N scope.

**AV5 — Pre-limit vs post-limit; Theorem M.2.1 telescoping.** The sum
is over the lattice sequence (pre-continuum), exactly where Theorem M.2.1
(doubly exponential convergence, §5.7 Proof of (b)) applies. The
telescoping argument uses absolute convergence of Σ_K δC_K with
general term ~ K^{γ−2}·4^{−K}, which holds unconditionally for any
finite γ. The convergence is independent of which subsequence is used
for the Banach–Alaoglu extraction (§5.7 Remark on subsequence-
independence). No pre/post-limit confusion. Attack fails.

## Conclusion

All five attack vectors fail. The sum Σ C_K g_K^4 Δ̂_K^2 < ∞ is
dominated by the doubly-exponential outer factor 4^{−K}, making C_K's
power-law growth and g_K^4's logarithmic decay both irrelevant. The
sum range, index splitting, and K-uniformity inputs are all explicitly
handled. No large-N gap exists within the theorem's fixed-N scope.

**SURVIVED**
