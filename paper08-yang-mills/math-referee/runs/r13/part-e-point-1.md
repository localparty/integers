## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim: C_{k+1} = C_k/4 + C_new + O(g_k^2 C_k) has a stable fixed point C_* = (4/3)C_new with polynomial growth C_k ~ k^gamma.

**(a) The 1/4 contraction.** The factor 1/4 comes from hat{Delta}_k^2 = hat{Delta}_{k+1}^2 / 4, since hat{Delta}_{k+1} = 2 hat{Delta}_k (to leading order, from a_{k+1} = 2 a_k with Delta approximately constant per RG step). This is a kinematic identity.

The matrix element <1|E_k^{downarrow}(0)|1>_c in the coarsened theory uses the OLD state |1>_k evaluated on the NEW lattice Lambda_{k+1}. The change of lattice introduces corrections through the wave function change |1>_{k+1} = |1>_k + |delta 1>_k. These corrections contribute:

  (A2) = <delta 1|E_k^{downarrow}|1> + <1|E_k^{downarrow}|delta 1> + <delta 1|E_k^{downarrow}|delta 1>

The paper bounds ||delta 1|| <= C g_k^4 / hat{Delta}_k (from Kato perturbation theory), giving:

  |(A2)| <= 2 ||delta 1|| * ||E_k^{downarrow}|| + ||delta 1||^2 * ||E_k^{downarrow}||
         <= O(g_k^4 / hat{Delta}_k) * g_k^4 * hat{Delta}_k^2
         = O(g_k^8 hat{Delta}_k) = O(g_k^2 * g_k^4 hat{Delta}_k^2 * hat{Delta}_k/g_k^2)

Wait — more carefully: ||delta 1|| <= C g_k^4/hat{Delta}_k, ||E_k|| <= C' g_k^4, and the inductive hypothesis gives |<1|E_k|1>_c| <= C_k g_k^4 hat{Delta}_k^2. The cross terms are bounded by ||delta 1|| * C_k g_k^4 hat{Delta}_k = O(g_k^2 C_k g_k^4 hat{Delta}_k^2). This gives the O(g_k^2 C_k) correction in the recursion. Correct.

**(b) The wave function correction.** ||delta 1|| <= C g_k^4 / hat{Delta}_k uses Kato perturbation theory: the first-order correction to the eigenvector is ||delta psi|| <= ||V||/gap. Here ||V|| = ||E_k|| <= C g_k^4, and the gap is hat{Delta}_k (the spectral gap of the transfer matrix). The Kato condition requires ||V|| << gap, i.e., C g_k^4 << hat{Delta}_k.

On the AF trajectory: g_k^4 ~ 1/k^2, hat{Delta}_k = a_k Delta_k. At the starting scale, hat{Delta}_0 ~ O(1). For k >= 1, hat{Delta}_k = 2 hat{Delta}_{k-1} (1 + O(g_k^4)) grows exponentially, while g_k^4 ~ 1/k^2 decreases. So g_k^4/hat{Delta}_k -> 0 rapidly, and the Kato condition is amply satisfied.

For k = 0: g_0^4 ~ g_0^4 and hat{Delta}_0 ~ O(1). The condition g_0^4 << hat{Delta}_0 requires g_0 not too large, which is guaranteed by the overlap condition (Balaban requires g_0 small).

**(c) The Gronwall bound.** The product Pi_{j=0}^{k-1} (1 + alpha g_j^2) with alpha = O(1) (a constant from the Lie algebra). Using g_j^2 ~ 1/(b_0 j ln 2):

  Pi (1 + alpha/(b_0 j ln 2)) <= exp(Sum alpha/(b_0 j ln 2)) = exp(alpha ln(k)/(b_0 ln 2)) = k^{alpha/(b_0 ln 2)}

So gamma = alpha/(b_0 ln 2). For SU(N), b_0 = 11N/(48 pi^2) and alpha scales as N^a for some a (from the Lie algebra structure). If alpha ~ N^2 (from the Casimir), then gamma ~ 48 pi^2 N / (11N ln 2) = 48 pi^2/(11 ln 2) ~ 62 (independent of N!). If alpha ~ N, then gamma ~ 48 pi^2/(11 ln 2) as well.

From I.3: gamma ~ N (unfavorable). But the convergence Sum k^{gamma-2} 4^{-k} converges for ANY gamma (the 4^{-k} dominates any polynomial). The constants become N-dependent but the sum converges for each fixed N.

No error found. The inductive stability is correctly established with the 1/4 contraction mechanism.

**Impact on the claimed result:** None. The recursion is stable with geometric convergence to the fixed point.
