# Point 7: The Inductive Stability -- Precise Version

**Location:** Section 5.4

**Verdict:** SOUND

**Finding:**

The RG recursion $C_{k+1} = C_k/4 + C_\mathrm{new} + O(g_k^2 C_k)$ with fixed point $C_* = (4/3)C_\mathrm{new}$ and convergence sum $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ is verified in detail. Each interrogation point is addressed.

---

## (a) The $O(g_k^2 C_k)$ correction

**Claim under attack:** The $O(g_k^2 C_k)$ correction could produce exponential (not polynomial) growth in $C_k$.

**Finding: SOUND.**

The paper provides an explicit computation (Section 5.4.6). The recursion with corrections is:

$$C_{k+1} = (C_k/4 + C_\mathrm{new})(1 + \alpha g_k^2)$$

The accumulated multiplicative factor after $k$ steps is:

$$\prod_{j=0}^{k-1}(1 + \alpha g_j^2) \leq \exp\!\left(\alpha \sum_{j=0}^{k-1} g_j^2\right)$$

Since $g_j^2 \sim 1/(b_0 j \ln 2)$ for large $j$ (one-loop running):

$$\sum_{j=1}^{k} g_j^2 \sim \sum_{j=1}^{k} \frac{1}{b_0 j \ln 2} = \frac{\ln k}{b_0 \ln 2} + O(1)$$

Therefore:

$$\prod_{j=0}^{k-1}(1+\alpha g_j^2) \leq C' \cdot k^{\alpha/(b_0 \ln 2)} = C' k^\gamma$$

This is **polynomial** growth, not exponential. The growth rate $\gamma = \alpha/(b_0 \ln 2)$ is finite and computable.

**Why exponential growth is impossible:** Exponential growth $C_k \sim e^{ck}$ would require $\sum g_j^2 \sim ck$ (linear growth), which would mean $g_j^2 \sim c$ (constant, not decreasing). But Balaban's UV stability guarantees $g_k^2 \to 0$ as $k \to \infty$ (asymptotic freedom). The logarithmic running $g_k^2 \sim 1/(b_0 k \ln 2)$ is a consequence of the one-loop $\beta$-function with controlled higher-order corrections. Balaban's construction (CMP 109, Section 3) establishes this with $k$-independent bounds.

**Why polynomial growth is harmless:** The mass gap shift sum is:

$$\sum_k C_k g_k^4 \hat{\Delta}_k^2 \sim \sum_k k^\gamma \cdot \frac{1}{(b_0 k \ln 2)^2} \cdot 4^{-k} = \sum_k \frac{k^{\gamma-2}}{(b_0 \ln 2)^2} \cdot 4^{-k}$$

The exponential factor $4^{-k}$ overwhelms any polynomial $k^{\gamma-2}$. This sum converges for ALL $\gamma$, with the tail bounded by a geometric series. Even for $\gamma = 100$, the sum is finite.

---

## (b) Starting constant $C_0$

**Claim under attack:** $C_0$ might not be bounded by a computable constant.

**Finding: SOUND.**

At $k = 0$, the lattice mass gap is proved by the cluster expansion (Theorem 4, Section 4). The form factor bound at the starting scale is:

$$|\langle 1|E_0(0)|1\rangle_c| \leq C_0 g_0^4$$

where $C_0$ is determined by the cluster expansion constants. Specifically:

- The operator norm $\|E_0\| \leq C g_0^4$ per site (Balaban's bound, Section 5.1.3).
- The connected matrix element is bounded by the operator norm: $|\langle 1|E_0(0)|1\rangle_c| \leq 2\|E_0(0)\|$.
- At $k = 0$, $\hat{\Delta}_0 \sim O(1)$ (the mass gap is $O(\Lambda_\mathrm{QCD})$ and the lattice spacing is at the QCD scale), so $C_0 = O(1)$.

The cluster expansion provides explicit constants depending on:
- $N$ (rank of the gauge group): through the Haar measure normalization and group-theoretic factors.
- The lattice geometry (dimension $d = 4$, coordination number): through the lattice animal counting.
- The polymer decay constant $\kappa > 0$ (from Balaban's Theorem 2.1 in CMP 109).

All of these are computable, finite constants. The starting constant $C_0$ is finite and bounded. Its convergence to the fixed point $C_* = (4/3)C_\mathrm{new}$ is geometric: $C_k = C_* + (C_0 - C_*) \cdot 4^{-k}$, so $C_k$ reaches $C_*$ (to within $1\%$) by step $k = 4$ regardless of $C_0$.

---

## (c) Perturbative vs. non-perturbative at the starting scale

**Claim under attack:** The cluster expansion (Section 4) applies for all couplings, but Balaban's RG requires weak coupling. Is there a regime mismatch?

**Finding: SOUND.**

The regime of overlap is identified in Section 5.1.2:

> "The condition $g_0$ small corresponds to $\beta_0 = 2N/g_0^2$ large, compatible with the lattice mass gap of Section 4 (which holds for $\beta < a_0/(2\sqrt{3}\,r_3)$, satisfied when $a_0/r_3 \gg 1$)."

Concretely:
- **Cluster expansion (Theorem 4):** Applies for $\beta < a_0/(2\sqrt{3}\,r_3)$. In the physical regime ($a_0/r_3 \sim 10^{15}$), this allows $\beta$ up to $\sim 10^{14}$.
- **Balaban's RG:** Applies for $g_0$ small, i.e., $\beta_0 = 2N/g_0^2$ large. "Large" means $\beta_0 \gg 1$; specifically, $\beta_0 > \beta_\mathrm{crit}(N)$ where $\beta_\mathrm{crit}$ is determined by the convergence conditions of Balaban's polymer expansion (CMP 109).

The overlap regime is: $\beta_\mathrm{crit}(N) < \beta_0 < 10^{14}$. This is an enormous range. The starting coupling $g_0$ is chosen in this range: $g_0^2 = 2N/\beta_0$ with $\beta_0$ large enough for Balaban (weak coupling) and small enough for the cluster expansion convergence.

The first few RG steps ($k = 0, 1, 2$) where $g_k^4 = O(1)$ are handled non-perturbatively by the cluster expansion, as noted in Section 5.7 Remark 1:

> "At $k = 0,1,2$ where $g_k^4 = O(1)$, first-order perturbation is not a priori justified. These finitely many steps are handled non-perturbatively via the cluster expansion, with bounded total contribution $K_0$ absorbed into $C_0$."

---

**Impact on the claimed result:** None. The RG recursion is well-controlled, the starting constant is finite, and the regime overlap between the cluster expansion and Balaban's RG is established.
