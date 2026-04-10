## Part D, Point 4: The Single-Step Coefficient Bound

**Weight:** LIGHT
**Verdict:** SOUND

**Finding:**

The claim: |<1|delta E_k^{d=6}(0)|1>_c| <= C_new g_k^4 hat{Delta}_{k+1}^2.

**(a) The g_k^4 factor.** The spectral lemma (Point D3) with M = ||delta E_k^{d=6}|| and dev >= 2 gives:

  |<1|delta E_k^{d=6}(0)|1>_c| <= C_2 M hat{Delta}^2

where C_2 = C_p(p=2) is the spectral lemma constant (k-independent). Balaban's operator norm bound gives M = ||delta E_k^{d=6}|| <= C g_k^4 (per site, from the polymer expansion). Combining:

  C_2 * C g_k^4 * hat{Delta}_{k+1}^2 = C_new g_k^4 hat{Delta}_{k+1}^2

with C_new = C_2 * C. This is straightforward algebra.

The g_k^4 comes from the operator NORM bound (Balaban), not from a product of one-loop coefficient and matrix element. The hat{Delta}^2 comes from the deviation order (the spectral lemma). The factorization g_k^4 * hat{Delta}^2 is the correct structure: the irrelevant operator has norm O(g_k^4) and its spectral response is suppressed by hat{Delta}^2.

**(b) Non-perturbative corrections.** Two sources:

  1. Large-field contributions: O(e^{-c/g_k^{2 epsilon}}) = O(e^{-c/g_k^{1/2}})
  2. Instanton contributions: O(e^{-8 pi^2/g_k^2})

Both must be negligible compared to g_k^4 hat{Delta}^2 on the AF trajectory.

On the AF trajectory: g_k^2 ~ 1/(b_0 k ln 2), hat{Delta}_k^2 ~ 4^{-k}, so g_k^4 hat{Delta}_k^2 ~ 4^{-k}/k^2.

Large-field: e^{-c/g_k^{1/2}} = e^{-c(b_0 k ln 2)^{1/4}} ~ e^{-c k^{1/4}}. This decays super-polynomially, much faster than 4^{-k}/k^2 for any c > 0 (since e^{-c k^{1/4}} << 4^{-k} for large k). For small k, the cluster expansion provides direct control.

Instanton: e^{-8 pi^2/g_k^2} = e^{-8 pi^2 b_0 k ln 2}. This decays exponentially in k, faster than 4^{-k}/k^2.

Both corrections are negligible. The bound C_new g_k^4 hat{Delta}_{k+1}^2 is correct including non-perturbative effects.

No error found.

**Impact on the claimed result:** None. This combines the spectral lemma with Balaban's norm bound in a straightforward way.
