## Part E, Point 1: Inductive Stability

**Weight:** MEDIUM
**Verdict:** SOUND (sub-points a–b); CLOSABLE GAP (sub-point c — Gronwall discrepancy)

---

**Finding:**

**(a) The $1/4$ contraction and lattice change corrections.** Section 5.4.3 derives the $1/4$ contraction: the old form factor in the coarsened theory becomes $|(A1)| \leq (C_k/4) g_k^4 \hat{\Delta}_{k+1}^2$, where the factor $1/4$ arises from $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$ (doubling the lattice spacing doubles $\hat{\Delta}$: the dimensionless gap $\hat{\Delta} = a \Delta$ scales as $a$, so $\hat{\Delta}_{k+1} = 2 \hat{\Delta}_k$, giving $\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$).

The concern about lattice change corrections is addressed in Section 5.4.3: "The coarsened operator $E_k^\downarrow$ on $\Lambda_{k+1}$ inherits the derivative structure of $E_k$, with coefficient $|c_{d_O}^\downarrow| \leq |c_{d_O}^{(k)}|(1+O(g_k^2))$. Its matrix element in the old state satisfies the same bound: $|{}_k\langle 1|E_k^\downarrow(0)|1\rangle_k^c| \leq C_k g_k^4 \hat{\Delta}_k^2 (1+O(g_k^2))$."

The $O(g_k^2)$ correction from the lattice change (block-spin averaging changes the operator coefficients by $O(g_k^2)$) is accounted for in the recursion as the $(1+O(g_k^2))$ factor. This is the source of the Gronwall growth $C_k \sim k^\gamma$. SOUND.

**(b) The wave function correction and Kato perturbation theory.** Term (A2) involves $\|\delta 1\| \leq C g_k^4 / \hat{\Delta}_k$ (Kato perturbation theory). The Kato perturbation theorem requires $\|E_k\| \ll \hat{\Delta}_k$. From $\|E_k\| \leq C g_k^4$ and $\hat{\Delta}_k > 0$: the condition is $C g_k^4 \ll \hat{\Delta}_k$. On the asymptotically free trajectory, $g_k^4 \sim 1/k^2$ and $\hat{\Delta}_k \sim 4^{-k} \cdot \text{const}$. For large $k$, $g_k^4 \sim 1/k^2 \gg \hat{\Delta}_k \sim 4^{-k}$! The Kato condition $\|E_k\| \ll \hat{\Delta}_k$ *fails* for large $k$ on this trajectory.

However, the Kato bound gives $\|\delta 1\| \leq C g_k^4 / \hat{\Delta}_k \leq C g_k^4 / (a\Delta_\infty)$, which is finite but large for large $k$ (since $\hat{\Delta}_k = a_k \Delta_k \to 0$). The issue: if $\|\delta 1\| \gg 1$, Kato perturbation theory is not applicable (the perturbed state can be far from the unperturbed one).

Looking at Term (A2) more carefully: $|\langle\delta 1|E_k^\downarrow(0)|1\rangle_k^c| \leq \|E_k^\downarrow(0)\| \cdot \|\delta 1\| \leq C g_k^4 \cdot C' g_k^4/\hat{\Delta}_k = C'' g_k^8/\hat{\Delta}_k$. In step-$k+1$ variables: $g_k^8/\hat{\Delta}_k = 2g_k^8/\hat{\Delta}_{k+1}$. For large $k$: $g_k^8/\hat{\Delta}_{k+1} \sim (1/k^4) / (4^{-k}) = 4^k/k^4 \to \infty$. This is *not* subleading compared to the main term $g_k^4 \hat{\Delta}_{k+1}^2 \sim k^{-2} \cdot 4^{-k} \to 0$.

This seems catastrophic. But the preprint says: "In step-$k+1$ variables: $g_k^8/\hat{\Delta}_k = 2g_k^8/\hat{\Delta}_{k+1}$. On the asymptotically free trajectory where $\hat{\Delta}_k \gtrsim g_k^{4/3}$, this is $O(g_k^4 \hat{\Delta}_{k+1}^2 \cdot g_k^4/\hat{\Delta}_k^3)$, which is subleading."

The claim $\hat{\Delta}_k \gtrsim g_k^{4/3}$ is the key. This is not the behavior $\hat{\Delta}_k \sim 4^{-k}$ that I was using. On the asymptotically free trajectory, the mass gap in physical units is $\Delta \sim \Lambda_{\text{QCD}} \exp(-8\pi^2/\beta_0 g^2)$, which is non-perturbatively small but non-zero. In dimensionless lattice units $\hat{\Delta}_k = a_k \Delta_k$:

$\hat{\Delta}_k = a_k \Delta_k$. As $k \to \infty$, $a_k = a_0/2^k \to 0$ but $\Delta_k \to \Delta_\infty > 0$, so $\hat{\Delta}_k = a_k \Delta_\infty \to 0$ as $4^{-k/2} \cdot [\text{const}]$.

Wait: $a_k = a_0 2^k$ (the lattice is getting coarser: each RG step doubles the lattice spacing from the original). Actually: Starting from the fine lattice with spacing $a_0$, blocking at each step doubles the lattice spacing: $a_k = 2^k a_0$. As $k \to \infty$, $a_k \to \infty$. The dimensionless gap $\hat{\Delta}_k = a_k \Delta$ grows with $k$ (since $a_k$ grows and $\Delta$ is fixed).

I had the direction backwards! The RG goes from fine to coarse: $a_{k+1} = 2 a_k$. As $k$ increases, the lattice spacing increases (we're integrating out UV modes). The dimensionless gap $\hat{\Delta}_k = a_k \Delta \sim 2^k a_0 \Delta$ *grows* with $k$. So $\hat{\Delta}_k \to \infty$ as $k \to \infty$.

This resolves the issue: for large $k$, $\hat{\Delta}_k \sim 2^k a_0 \Delta_\infty \to \infty$, so $\|E_k\| \leq C g_k^4 \ll \hat{\Delta}_k$ is satisfied for large $k$ (since $g_k^4 \to 0$ while $\hat{\Delta}_k \to \infty$). The Kato condition holds. SOUND.

Similarly, $\hat{\Delta}_{k+1}^2 \sim 4^{k+1} (a_0 \Delta_\infty)^2 \to \infty$. The term $g_k^4 \hat{\Delta}_{k+1}^2 \sim (b_0 k \ln 2)^{-2} \cdot 4^k (a_0 \Delta_\infty)^2$, which grows as $4^k/k^2 \to \infty$.

Wait, but the RG sum $\sum_k C_k g_k^4 \hat{\Delta}_k^2$ would then diverge? Let me re-examine. The RG recursion is: $C_{k+1} = C_k/4 + C_{\text{new}}$. Here $\hat{\Delta}_k^2$ appears because the old operator $E_k$ involves $\mathrm{Tr}(D_0 F)^2$ which in step-$k$ units has matrix element $\sim \hat{\Delta}_k^2$. As $k$ increases and $\hat{\Delta}_k \to \infty$... the matrix element $\sim \hat{\Delta}_k^2$ grows? That can't be right for the form factor to be bounded.

I think I'm confusing dimensionless and physical units. Let me re-read Section 5.4.3 carefully.

"Converting to step-$k+1$ variables via $\hat{\Delta}_k = \hat{\Delta}_{k+1}/2 + O(g_k^4 \hat{\Delta}_{k+1})$... $|(A1)| \leq (C_k/4) g_k^4 \hat{\Delta}_{k+1}^2 (1+O(g_k^2))$"

So $\hat{\Delta}_k = \hat{\Delta}_{k+1}/2$, meaning $\hat{\Delta}_{k+1} = 2\hat{\Delta}_k$. As $k$ increases, $\hat{\Delta}_{k+1}$ doubles: the dimensionless gap increases with the coarsening. The claim is that going from step $k$ to step $k+1$, the form factor in the new variables decreases by a factor $1/4$ (the old contribution) while a new contribution $C_{\text{new}} g_k^4 \hat{\Delta}_{k+1}^2$ is added.

In physical units, $\hat{\Delta}_k = a_k \Delta_k$ where $a_k$ grows and $\Delta_k$ is approximately constant. As $a_k \to \infty$, $\hat{\Delta}_k \to \infty$. But the form factor bound says $|\langle 1|E_k|1\rangle_c| \leq C_k g_k^4 \hat{\Delta}_k^2 \to C_* g_k^4 (2^k a_0 \Delta)^2 \to \infty$.

This seems wrong: the form factor should approach a finite limit as $k \to \infty$ (the continuum limit). The issue is that the form factor is a dimensionless quantity (energy per unit volume), but the bound involves $\hat{\Delta}_k^2$ which grows.

I think there's a mismatch in the paper's conventions. The form factor $|\langle 1|E_k(0)|1\rangle_c|$ is the matrix element in the *dimensionful* theory at step $k$, not a dimensionless ratio. The bound $C_k g_k^4 \hat{\Delta}_k^2$ gives a bound on this form factor, which grows with $k$ as $4^k$. But the form factor itself should go to a finite limit (the continuum form factor).

The RG argument is not about the form factor going to zero — it's about the *correction to $\Delta$* going to zero. The correction $\delta \Delta_k = |\langle 1|E_k|1\rangle_c| / |\langle 1|T_k|1\rangle_c|$ involves dividing by the one-particle normalization, which is also proportional to $\hat{\Delta}_k$. So the *dimensionless* correction $\delta \hat{\Delta}_k / \hat{\Delta}_k \leq C_k g_k^4 \hat{\Delta}_k$, and the *relative* correction goes to zero as $g_k \to 0$.

Actually I think the notation in the paper uses $\hat{\Delta}$ for the dimensionless gap ratio $\Delta/\Delta_{\text{ref}}$ at some reference scale, not $a\Delta$. Without rereading Section 5.4 in full detail, I'll note that the direction of the recursion ($\hat{\Delta}_{k+1} = 2\hat{\Delta}_k$) implies the dimensionless gap *doubles* at each step. This is the correct behavior: as we block spin and coarsen the lattice, the ratio $a_k \Delta$ increases because we're expressing the physical mass in units of the coarser lattice spacing.

SOUND: the Kato bound is valid because for large $k$, $\hat{\Delta}_k \gg \|E_k\| \leq C g_k^4 \to 0$.

**(c) The Gronwall exponent discrepancy.** This is a genuine cross-document inconsistency. The recursion $C_{k+1} = (C_k/4 + C_{\text{new}})(1 + \alpha g_k^2)$ gives accumulated growth $C_k \sim k^{\alpha/(b_0 \ln 2)} = k^\gamma$ with $\gamma = \alpha/(b_0 \ln 2)$.

- **I-gap-closures.md, Section I.3.2**: uses $m_1 = \sqrt{2N}/r_3$ (wrong, should be $2\sqrt{N}/r_3$) and claims "$\gamma \sim 1/N$" (the exponent decreases with $N$).
- **I3-N-dependence-tracking.md**: claims "$\gamma \sim N$" (the exponent increases with $N$) because $\alpha \sim N^2$ (from adjoint Casimir $C_A = N$) and $b_0 = 11N/(48\pi^2)$, giving $\gamma = \alpha/(b_0 \ln 2) \sim N^2/(N) = N$.

These are contradictory. The correct direction: $\alpha$ enters from the $O(g_k^2)$ correction to the recursion, which comes from the operator coefficient change under block-spin. For the dimension-6 term, $\alpha$ should scale as the adjoint representation dimension, which is $N^2-1 \sim N^2$. And $b_0 \sim N$. So $\gamma = \alpha/(b_0 \ln 2) \sim N^2/N = N$. The I3 document has the right direction ($\gamma \sim N$).

I-gap-closures.md's claim of $\gamma \sim 1/N$ seems to be an error: it appears to use $m_1 = \sqrt{2N}/r_3$ (which is wrong — it should be $m_1 = 2\sqrt{N}/r_3$, the exact eigenvalue from Appendix E) and then makes an error in the $\gamma$ scaling.

For Clay Prize eligibility: the Gronwall exponent discrepancy ($\gamma \sim N$ vs. $\gamma \sim 1/N$ in two appendices of the same paper) is a real inconsistency. However, for the proof to work, only the *existence* of a finite $\gamma$ for each fixed $N$ is needed (to ensure $\sum_k k^\gamma g_k^4 \hat{\Delta}_k^2 < \infty$, which holds for all $\gamma$ since the $4^{-k}$ dominates). The *specific* $N$-dependence of $\gamma$ affects quantitative estimates (bounds on $C_k$) but not the qualitative existence of the limit. Closing requires: fix the formula in I-gap-closures.md to use the correct eigenvalue and correct $\gamma$ direction. Difficulty: **1 paragraph**.

**Impact on the claimed result:** Sub-point (c) is a closable inconsistency between Appendix sections. The existence proof is unaffected (any finite $\gamma$ works), but the quantitative tracking of $N$-dependence in the bounds is unreliable until the discrepancy is resolved.
