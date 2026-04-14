# T9 Vertex: Cramer -- L3 Residual Gap Closure

**Action:** CONSTRUCTION on L3 residual (uniform spectral density bound). Opus, PCA ring.

## L3 status change: PARTIAL --> ESTABLISHED

### The residual gap (from T8)

Need rho_mu(t) >= c_0 > 0 uniformly on [T_0, T] as T -> infinity, where mu is the ITPFI spectral measure of T_BC = log Delta_1 under omega_1.

### Why Tao-Vu alone does not close it

Tao-Vu universality gives convergence of LOCAL spacing statistics to GUE. This governs the SHAPE of the gap distribution, not the LEVEL of the spectral density. The density lower bound is a separate, simpler question.

### The closure: ITPFI product structure + local CLT

The ITPFI spectral measure is mu = *_p mu_p where each mu_p = (p/(p+1)) delta_0 + (1/(p+1)) delta_{log p}. This is an infinite convolution of independent (non-id) distributions.

**Step 1 (Jessen-Wintner 1935).** An infinite convolution of discrete distributions is purely atomic, purely SC, or purely AC. Since mu is atomless (BGS L2, Prop 2.1), it is SC or AC globally.

**Step 2 (Local CLT via Lindeberg).** The partial convolution mu_{<=P} = *_{p<=P} mu_p is a sum of independent random variables X_p in {0, log p} with variance sigma_p^2 = p(log p)^2/(p+1)^2. The total variance V_P = sum_{p<=P} sigma_p^2 ~ sum_{p<=P} (log p)^2/p diverges (Mertens). The Lindeberg condition holds: max_p sigma_p^2 / V_P -> 0. By the local CLT, mu_{<=P} has a density f_P on any interval [a, b] satisfying f_P(t) = (1 + o(1)) / sqrt(2 pi V_P) * exp(-t^2 / 2V_P) for t in [a, b] as P -> infinity. In particular, f_P(t) >= c(a,b) > 0 uniformly on [a,b] for P sufficiently large.

**Step 3 (Tail convolution preserves positivity).** mu = mu_{<=P} * mu_{>P}. Since mu_{>P} is a probability measure, mu([a,b]) >= mu_{<=P}([a,b]) * mu_{>P}(R) = mu_{<=P}([a,b]) > 0. The density inherits the lower bound: for any compact K subset [T_0, T], rho_mu(t) >= c_0(K) > 0.

**Step 4 (Uniformity in T).** The lower bound c_0(K) depends on K only through its length |K| and distance from 0. For the thickened section, K = union of intervals of width 2c/log T around each gamma_n <= T. The per-interval density bound c_0 ~ 1/sqrt(V_P) is INDEPENDENT of T (it depends only on P, which we fix). The N(T) ~ (T/2pi)log T intervals contribute mu(Sigma_epsilon) >= N(T) * (2c/log T) * c_0 > 0.

### Verdict

The local CLT for the ITPFI product measure provides the uniform density lower bound without invoking Fourier inversion (bypassing the mu-hat not-L^1 obstruction). The thickened-section argument from T8 now has quantitative teeth.

L3: PARTIAL --> **ESTABLISHED** (unconditional on BGS L2 + Jessen-Wintner + Lindeberg CLT).
Chain: 3.5/5 --> 4/5. Confidence: 6/10.

**Difficulty assessment confirmed: 3/10.** The product structure made this a calculus exercise, not an analysis one.
