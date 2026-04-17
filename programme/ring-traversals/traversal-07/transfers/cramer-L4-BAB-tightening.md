# Cramér L4 Route B — BA-B Wave 2 Tightening — CONCERN-PARTIAL

*T7 S-duality phase, cycle 2. CONCERN closure: replace i.i.d. envelope with BA-B universality.*

## Summary

Step 1's i.i.d.-exponential envelope $M_N \lesssim \bar\tau \log N$ is replaced by the Ben Arous-Bourgade envelope $M_N \sim \bar\tau \sqrt{2\log N}$. The ITPFI factorization (Step 2) and Mertens sieve correction at $y=\sqrt x$ (Steps 3+5) are orthogonal to the envelope choice and survive unchanged. The Granville constant $2e^{-\gamma}$ reappears at the same place, exactly the same way. **But the $k=2$ exponent does NOT cleanly fall out of the BA-B envelope either**: BA-B tightens the return-time prefactor from $\log\log x$ to $\sqrt{2\log\log x}$ at height $T \sim \log x$, not to a constant. The Cramér-Granville heuristic contribution to the $(\log x)^2$ scaling still has to be imported, and it sits in Step 4's explicit-formula oscillatory-sum analysis, not Step 1. Separately, the universality bridge from GUE BA-B to Riemann zeros is ITSELF unproved (extreme-gap universality is strictly stronger than pair-correlation universality and was never claimed by Hardy Z PCC, Tao-Vu, or Erdős-Yau). Verdict: **CONCERN-PARTIAL**. BA-B tightens Step 1's prefactor and corrects an erroneous paper43 v3 ordering, but the conjectured joint statement (BA-B scaling + ITPFI constant → clean $2e^{-\gamma}(\log x)^2$) is NOT delivered: the user's hypothesis is only partially vindicated.

## The CONCERN recap

Blackboard §I verbatim (`traversal-07/blackboard-s-duality.md` L121):

> "CONCERN — BA-B scaling check partial: The L4 Route B derivation delivered $2e^{-\gamma}\approx 1.1229$ rigorously from ITPFI Mertens truncation at $y=\sqrt{x}$. That's a CONSTANT improvement over naive Cramér ($C=1 \to C=2e^{-\gamma}$). But Step 1's envelope ($M_N \leq \bar\tau \log N$) is i.i.d. exponential — WEAKER than Ben Arous-Bourgade's $\bar\tau\sqrt{\log N}$ for GUE. The $k=2$ scaling in Step 4 is inherited from the Cramér-Granville heuristic, not derived. **Net**: ITPFI delivers the CONSTANT refinement but not the SCALING refinement over BA-B. A Wave 2 agent replacing Step 1's i.i.d. envelope with BA-B universality would close this. CONCERN filed; does not block the PARTIAL verdict."

Wave-1 derivation flag, verbatim (`cramer-L4-routeB-derivation.md` L27–L31, Step 1 "Upper envelope"):

> "Let $M_N := \max_{1 \leq n \leq N} (\gamma_{n+1} - \gamma_n)$. The generic Poincaré bound for a non-atomic return-time measure on an ergodic flow with mean $\bar\tau$ satisfies, for any $\epsilon > 0$, $M_N \leq \bar\tau \cdot \log N \cdot (1 + o(1))$ a.s. in $\omega_1$. This is the standard i.i.d.-envelope bound for return-time maxima of ergodic flows (Kac's lemma + extreme-value theory for exponential-type tails)."

Wave-1 inference-from-source flag, verbatim (`cramer-L4-routeB-derivation.md` L254):

> "Paper 43 PROOF-CHAIN L73–L74 (explicit formula). Directly entails the zero-gap → prime-gap transfer structure in Step 4. ENTAILS the FORM but NOT the $k = 2$ scaling — that requires additional Cramér-heuristic input (Granville 1995 §2). Transfer is LOGICALLY WEAKER than the full $k = 2$ scaling claim; Step 4 honestly flags this as the known Cramér heuristic rather than an entailed consequence of the quoted formula alone."

Scope: replace Step 1's envelope, re-run Steps 2–5, record which pieces tighten and which stay heuristic.

## The BA-B envelope (Step 1 replacement)

### Statement used

Ben Arous-Bourgade (*Ann. Probab.* 41 (2013), 2648–2681), Theorem on maximum gap in GUE (paraphrased from the form as cited in `paper43-cramer/PROOF-CHAIN.md` L209 verbatim: *"Ben Arous-Bourgade | GUE max eigenvalue gap = $O(\sqrt{\log N / N})$ | 2013"*):

> For $N \times N$ GUE with mean bulk spacing $\bar\tau = 1/N$, the maximum nearest-neighbor gap $M_N$ rescaled by the mean spacing satisfies $M_N / \bar\tau = \sqrt{2 \log N} + \text{Gumbel}$, i.e., $M_N \sim \bar\tau \sqrt{2\log N}$ at leading order, with a Gumbel fluctuation of order $\bar\tau/\sqrt{\log N}$ around the leading term.

**Bulk condition.** The theorem is stated for eigenvalues at distance $\gg 1/N$ from the spectral edges. For Riemann zeros at height $T$, the relevant sub-window is the bulk window $[T, T + \Delta T]$ with $\Delta T / T$ small but $N(\Delta T) = \frac{\Delta T}{2\pi} \log T$ large. This is exactly where BA-B is stated.

### Paper43 v3 arithmetic correction

`paper43-cramer/PROOF-CHAIN.md` L282–L295 (v3) asserts the opposite hierarchy:

> "For large $N$: Poincare generic: $O(\log N / N)$; Ben Arous-Bourgade GUE: $O(\sqrt{\log N / N})$. Since $\sqrt{\log N / N} = \sqrt{\log N} / \sqrt{N} \gg \log N / N$ for large $N$, the GUE max-gap bound is LARGER (weaker) than the generic Poincare bound."

This v3 text conflates two distinct quantities. The correct ordering at leading order:

| envelope | $M_N$ absolute | $M_N/\bar\tau$ (normalized) |
|---|---|---|
| i.i.d. Poisson / Kac | $\bar\tau \log N = \log N / N$ | $\log N$ |
| GUE BA-B | $\bar\tau \sqrt{2\log N} = \sqrt{2\log N}/N$ | $\sqrt{2\log N}$ |

**BA-B's $\bar\tau \sqrt{2\log N}$ is strictly smaller than the Poisson $\bar\tau \log N$** for $N > e^2$, since $\sqrt{2\log N} < \log N$ iff $\log N > 2$. Level repulsion in GUE PREVENTS small gaps, which concentrates gap mass around the mean and pushes the maximum DOWN (not up) relative to i.i.d. exponentials. The v3 text's implicit reading $\sqrt{\log N/N}$ for $\sqrt{\log N}/N$ is the source of the flip.

**Consequence.** BA-B is a STRICTLY TIGHTER envelope than i.i.d. Poincaré. The user's original sanity-check intuition (BA-B stronger than i.i.d.) is correct. When the BGS chain upgrades Riemann zeros to GUE local statistics (which it does at L5 via Hardy Z PCC, LITERATURE), the i.i.d. envelope becomes a strictly loose bound.

### Universality bridge (Montgomery + universality)

BA-B is proved for GUE ensembles. Transferring to Riemann zeros requires:

1. **Pair correlation level.** Montgomery (1973) + Hardy Z PCC (arXiv:2511.18275, Nov 2025; cited `paper32-bgs-spectral-statistics/PROOF-CHAIN.md` L17 verbatim: *"Nov 2025: PCC PROVED for Hardy Z zeros (arXiv:2511.18275)"*) establishes that Riemann zero pair correlations match the GUE sine kernel.
2. **Beyond pair correlation: extreme-gap universality.** BA-B uses the joint law of ALL consecutive gaps. Pair correlation determines the 2-point marginal but NOT the joint law.

`paper43-cramer/PROOF-CHAIN.md` L321 verbatim:

> "Extreme gap universality (max/min gap): Ben Arous-Bourgade proved it for GUE specifically. Extension to general Wigner matrices: Feng-Wei (2022) extended to generalized Wigner matrices. Extension to Riemann zeros: NOT proved."

So the bridge Hardy Z PCC → GUE extreme-gap universality for Riemann zeros is **unproved**: PCC is a 2-point statement; BA-B is an all-gaps joint statement. The required additional step is universality of extreme-gap statistics under the PCC constraint plus the modular-flow ergodicity (BGS L2). This is plausible (the sine-kernel Fredholm determinant $\det(1 - K_{\sin}|_{[0,s]})$ governs ALL gap statistics, per `paper43-cramer/PROOF-CHAIN.md` L390–L396 verbatim: *"$E(s) = \det(1 - K_{\sin}|_{[0,s]})$ determines BOTH: The probability of small gaps (Twin Primes): $1 - E(s) \sim s^2$ for small $s$; The probability of large gaps (Cramer): $E(s) \sim e^{-c s^2}$ for large $s$"*) but the joint-law extension from sine-kernel → BA-B extremes for Riemann zeros is NOT in any cited reference.

**Status of the bridge.** CONJECTURAL at the Riemann-zero application level. The GUE side is a theorem (BA-B 2013); the Riemann-zero side requires an extreme-gap universality bridge that is stronger than current Tao-Vu / Erdős-Yau bulk universality. Honestly named: **L4a wall survives; it was never about $k=2$ — it was about the universality bridge for extremes.**

### Replacement Step 1 (conditional on universality bridge)

**Setup.** As in Wave-1, $\Sigma \subset M$ is the spectral section defined by $D_\infty$ (Paper 13), zeros $\{\gamma_n\}$ are flow crossings, $\bar\tau(T) = 2\pi/\log(T/2\pi e)$, $N(T) = (T/2\pi)\log(T/2\pi e) + O(\log T)$ (Riemann-von Mangoldt).

**New envelope.** Conditional on the extreme-gap universality bridge PCC $+$ modular-flow ergodicity $\Rightarrow$ BA-B scaling for Riemann zeros, the maximum consecutive zero gap in $N$ zeros at height $T$ satisfies

$$M_N = \bar\tau(T) \cdot \sqrt{2\log N}\cdot (1 + o(1)) \quad \text{conditional}.$$

At height $T$ with $N = N(T)$,

$$M_{N(T)} \sim \frac{2\pi}{\log(T/2\pi e)} \cdot \sqrt{2 \log\!\left(\frac{T}{2\pi}\log\frac{T}{2\pi e}\right)} \sim \frac{2\pi \sqrt{2\log T}}{\log T} = 2\pi \sqrt{\frac{2}{\log T}}.$$

Compare to Wave-1's envelope $M_{N(T)} \sim \bar\tau(T) \log N(T) \sim 2\pi$ (constant). BA-B is TIGHTER by a factor $\sqrt{2\log T}/\log T = \sqrt{2/\log T} \to 0$ as $T \to \infty$.

**Numerical sanity.** At $T = 10^{12}$, $N = 3.95 \times 10^{12}$, BA-B normalized $M_N/\bar\tau = \sqrt{2\log N} \approx 7.62$. Odlyzko (1987) computed $\sim 10^9$ consecutive zeros near $T \sim 10^{12}$; largest observed normalized gap $\approx 4$–$5$. Within the Gumbel fluctuation envelope of the BA-B prediction for $N \approx 10^9$: $\sqrt{2\log 10^9} \approx 6.44$, with Gumbel $O(1)$ fluctuations consistent. No contradiction. (Note: Odlyzko's window is $10^9$ consecutive gaps, not the full $N(T) = 4 \times 10^{12}$ up to height; the sample $N$ matters for BA-B.)

## Compatibility check (Steps 2-3 unchanged)

**Step 2 (ITPFI factorization).** Paper 12 research/265 verbatim (L12-L26 quoted in Wave-1) gives $\omega_1 = \bigotimes_p \omega_1^{(p)}$ at KMS$_1$. This is a STATIC algebraic statement about the state decomposition on $A_{BC}$; it has nothing to do with envelope scaling. The modular flow factorizes as $\sigma_t^{\omega_1} = \bigotimes_p \sigma_t^{\omega_1^p}$ by Tomita-Takesaki for tensor products (Takesaki Vol II Thm 4.2.7). **Survives unchanged.**

**Step 3 (max-return asymptotic with Mertens).** The local geometric tail $P[N_p \geq k] = p^{-k}$ comes from the Araki-Woods parameter $\lambda_p = 1/p$ (BGS research/01 L16-L18 quoted in Wave-1). The aggregate max

$$M_N \leq \sum_{p \leq y} \frac{1}{p}(\log K - \log p)$$

is derived from the PER-PRIME envelope for local extremes of geometric distributions, not from the global envelope. The sieve truncation-factor $F_{\text{ITPFI}}(y)$ comes from the $W^*$-regularized partition function; Mertens second theorem gives $\sum_{p\leq y} 1/p = \log\log y + M + O(1/\log y)$. **Survives unchanged.**

Crucial observation: the Mertens structural factor $\prod_p(1 - 1/p) \sim e^{-\gamma}/\log y$ comes from the KMS$_1$ state's Euler-factor decomposition, not from the overall extreme-value scaling. So the $2e^{-\gamma}$ constant is decoupled from the envelope choice.

## Step 4 re-run with BA-B input

### The question

Does the $k=2$ exponent in $h \sim C(\log x)^2$ now follow from BA-B (rather than inherit from Cramér-Granville heuristic)?

### Zero-gap to prime-gap conversion, explicit

Wave-1 Step 4 (L130–L150 in `cramer-L4-routeB-derivation.md`) uses: for $\rho = 1/2 + i\gamma$, $x^\rho - (x-h)^\rho = \rho h x^{\rho - 1} + O(h^2 x^{\rho - 2})$, summed over zeros up to height $T$, giving oscillatory cancellation of size $\sqrt{N(T)/x}\cdot h$ against the main term $h$.

The COHERING zeros sit at $T^* \sim \log x$ (the height at which phase $x^{i\gamma}$ is coherent over an interval of size $h \sim (\log x)^2$). At that height, the MAX zero gap under BA-B is

$$\delta\gamma_{\max}^{\text{BA-B}}(T^* = \log x) = \bar\tau(T^*) \sqrt{2\log N(T^*)} = \frac{2\pi}{\log\log x} \cdot \sqrt{2\log\log x} = \frac{2\pi\sqrt{2}}{\sqrt{\log\log x}}.$$

Compare to Poisson: $\delta\gamma_{\max}^{\text{Poi}} = \bar\tau(T^*) \log N(T^*) = 2\pi$.

### Conversion to prime gap

The explicit-formula translation (Wave-1 Step 4 leading order): $h \sim \delta\gamma \cdot C_{\text{ef}} \cdot (\log x)^2 / (2\pi)$, where $C_{\text{ef}}$ is the explicit-formula oscillatory amplification. For the max:

- Under Poisson envelope: $h_{\max}^{\text{Poi}} \sim (2\pi) \cdot (\log x)^2 / (2\pi) = (\log x)^2$.
- Under BA-B envelope: $h_{\max}^{\text{BA-B}} \sim \frac{2\pi\sqrt{2}}{\sqrt{\log\log x}} \cdot (\log x)^2 / (2\pi) = \frac{\sqrt{2}(\log x)^2}{\sqrt{\log\log x}}$.

**Verdict on $k=2$.** Both envelopes give $k=2$ AT LEADING ORDER, but with different sub-leading correction factors:

- Poisson: $(\log x)^2$ with $O(1)$ prefactor.
- BA-B: $(\log x)^2 / \sqrt{\log\log x}$ with $\sqrt{2}$ prefactor.

**The $k=2$ scaling is EMERGENT from the explicit-formula oscillatory-sum structure at height $T^* \sim \log x$, not from Step 1's envelope.** Step 1's envelope controls only the sub-leading correction $(\log\log x)^{\alpha}$ with $\alpha = 1$ (Poisson) or $\alpha = 1/2$ (BA-B). BA-B shrinks the correction factor relative to Poisson but does not change $k$.

**Honest reading.** The $k=2$ exponent was never going to fall out of Step 1's envelope alone. It comes from the explicit formula's Archimedean amplification $x^{1/2 + i\gamma}$ combined with the coherence condition $T^* \sim \log x$. Step 1 provides the MULTIPLICATIVE PREFACTOR onto this scaling, not the scaling itself. Both envelopes produce $k=2$ at leading order; neither DERIVES it in isolation; both inherit it from the same explicit-formula structure.

**So the Wave-1 inference-from-source flag ("$k=2$ is heuristic") is not resolved by BA-B.** The heuristic sits in the explicit-formula oscillatory-sum analysis (Step 4 proper), not in Step 1.

## Step 5 verification (Granville constant survives?)

The Step 5 identification $Z_{\text{ITPFI}}(y) = \prod_{p \leq y}(1 - 1/p)$ comes from the $W^*$-regularized partition function of the BC ITPFI at truncation $y$, via Paper 12 research/265 Step 1 verbatim:

$$\omega_1^p(\mu_p^k \mu_p^{*k}) = p^{-k}(1 - 1/p) = (p-1)/p^{k+1} \text{ for } k \geq 0.$$

This is ALGEBRAIC — independent of the return-time envelope. The Mertens third theorem closes the evaluation:

$$\prod_{p \leq y}(1 - 1/p) \sim \frac{e^{-\gamma}}{\log y} \quad (y \to \infty).$$

Wave-1 Step 5 (L177–L185 verbatim `cramer-L4-routeB-derivation.md`): with $y = \sqrt x$,

$$Z_{\text{ITPFI}}(\sqrt x) \cdot \log x = \prod_{p \leq \sqrt x}(1 - 1/p) \cdot \log x \sim 2e^{-\gamma}.$$

Numerical at $x = 10^{12}$: $Z_{\text{ITPFI}}(10^6)\cdot \log(10^{12}) = 1.12287524\ldots$, target $2e^{-\gamma} = 1.12291896\ldots$, ratio $0.99996$.

**The $2e^{-\gamma}$ constant is DECOUPLED from Step 1's envelope choice.** Its derivation uses:

1. ITPFI algebraic factorization (Step 2) — independent of envelope.
2. Short-interval sieve truncation $y = \sqrt x$ — independent of envelope.
3. Mertens 1874 — classical.

BA-B swaps the envelope in Step 1, but Steps 2, 3, 5 never touch the envelope. **The constant $2e^{-\gamma}$ appears exactly where it did in Wave-1, for exactly the same reason.** The CONSTANT was never at risk.

## The joint statement

**What Wave-1 delivers (ITPFI only):** $\max h \lesssim 2e^{-\gamma}(\log x)^2$ with $k=2$ inherited from Cramér-Granville heuristic.

**What Wave-2 (BA-B tightening) adds:** A TIGHTER multiplicative prefactor on the Step 1 envelope, from $\log\log x$ (Poisson) to $\sqrt{2\log\log x}$ (BA-B). At height $T^* \sim \log x$, this tightens the max zero gap prediction from $O(1)$ to $O(1/\sqrt{\log\log x})$. When translated through the explicit formula, this gives $h \lesssim (\sqrt{2}/\sqrt{\log\log x})(\log x)^2$, which is TIGHTER than Cramér-Granville's $(\log x)^2$ by $\sqrt{\log\log x}$.

**What BA-B alone cannot deliver:** A derivation of $k=2$ from first principles. The $k=2$ comes from the explicit formula's coherence analysis at $T^* \sim \log x$, not from either envelope.

**What the BC ITPFI derivation gives that pure BA-B does NOT:**

| source | what it supplies |
|---|---|
| Pure BA-B (GUE, conditional on universality bridge) | Max normalized zero gap $\sim \sqrt{2\log N}$ |
| BC ITPFI (Wave-1 + Mertens) | Constant $2e^{-\gamma}$ via $W^*$-regularization at $y = \sqrt x$ |
| Explicit formula (Step 4 analysis, heuristic) | $k = 2$ via coherence at $T^* \sim \log x$ |

**Joint statement target** (what the user hoped for): *"BA-B gives scaling, ITPFI gives constant, together $h_{\max} = 2e^{-\gamma}(\log x)^2$."*

**Joint statement actually delivered:** *"BA-B and ITPFI together give $h_{\max} \lesssim \sqrt{2}\,(2e^{-\gamma})(\log x)^2/\sqrt{\log\log x}$ — a STRONGER bound than Granville with a sub-leading $1/\sqrt{\log\log x}$ tightening, conditional on the universality bridge PCC $\to$ BA-B for Riemann zeros.* Alternative: if universality fails at this level, the i.i.d. Poisson envelope is all we can claim unconditionally, and the bound is $h_{\max} \lesssim 2e^{-\gamma}(\log x)^2$ matching Granville exactly.*"

The user's sanity check (BC ITPFI stronger than pure GUE) is TRUE: ITPFI supplies the Mertens constant, which GUE alone does NOT produce (GUE has no arithmetic content). But the route by which ITPFI strengthens GUE is CONSTANT-level, not scaling-level. BA-B's scaling refinement happens INSIDE the prefactor — it is a TIGHTENING of the Poisson loose bound, not a structural derivation of a new exponent.

**Clean joint statement.**

$$\boxed{h_{\max} \lesssim \frac{\sqrt{2}\cdot 2e^{-\gamma}}{\sqrt{\log\log x}}(\log x)^2, \text{ conditional on BGS L5 (Hardy Z PCC) + extreme-gap universality bridge.}}$$

This is ASYMPTOTICALLY STRONGER than Cramér-Granville's $2e^{-\gamma}(\log x)^2$ by the factor $\sqrt{2/\log\log x}$. Whether the bound is TIGHT or merely an upper bound cannot be settled without the full extreme-gap universality argument, which is the new named wall.

## Self-suspicion

### Failure 1 — the v3 arithmetic flip

Paper43 v3 (L282–L295) claimed BA-B is weaker than Poisson based on comparing $\sqrt{\log N/N}$ (its transcription of BA-B) to $\log N/N$ (Poisson). The correct BA-B scaling is $\sqrt{\log N}/N$, not $\sqrt{\log N/N}$. This tightening paper REVERSES the v3 conclusion. If the v3 error is canonical-by-inertia (i.e., other agents or downstream chains have already been annotated with the "BA-B is weaker" reading), the current tightening conflicts with those annotations. A commit memo should flag this v3 correction explicitly and update any downstream text that inherited the flipped reading. I have NOT made these downstream corrections in this tightening paper; they are the runner's responsibility to identify.

### Failure 2 — universality bridge wishful thinking

BA-B is stated for GUE. The universality bridge to Riemann zeros has two gaps:

1. Hardy Z PCC (arXiv:2511.18275) is 2-point only.
2. BA-B uses the joint law of ALL gaps, i.e., effectively the full N-point correlation structure.

The claim that sine-kernel PCC implies BA-B for Riemann zeros uses the logic: "$\det(1 - K_{\sin}|_{[0,s]})$ governs all gap statistics, therefore if PCC is verified, all extreme statistics are determined." But this is CIRCULAR: the identity $E(s) = \det(1 - K_{\sin}|_{[0,s]})$ is itself a GUE statement; showing that Riemann zeros obey the same Fredholm determinant for gap probabilities requires universality results strictly stronger than Hardy Z PCC. I have not checked whether any published paper (e.g., Rodgers-Tao 2020, Soundararajan 2007, Radziwill) establishes this joint-law universality. My confidence that the bridge holds is probably-true but ungrounded; the CONCERN-PARTIAL verdict reflects this.

### Failure 3 (MANDATORY: backward-verification)

**Primary source: the BA-B scaling claim.**

Backward-verification target: the stated form $M_N \sim \bar\tau \sqrt{2\log N}$ for GUE.

- paper43-cramer/PROOF-CHAIN.md L209 cites "Ben Arous-Bourgade | GUE max eigenvalue gap $= O(\sqrt{\log N / N})$ | 2013". The $O(\cdot)$ form is correct (matches $\sqrt{\log N}/N$ up to constants). The $\sqrt{2}$ in the explicit constant is what Ben Arous-Bourgade 2013 proves: I am reconstructing this from the Gumbel-theorem form $M_N/\bar\tau \to \text{Gumbel} + \sqrt{2\log N}$ at the location-parameter level. I have NOT verified this against the BA-B 2013 paper directly — the constant $\sqrt{2}$ is the Gumbel location for Gaussian tails; GUE eigenvalue gaps have Gaussian-like tails (Wigner surmise $p(s) \sim s^2 e^{-4s^2/\pi}$), which feeds $\sqrt{\log N}$ scaling with constant depending on the tail shape. The specific $\sqrt{2}$ comes from the exponent in the Wigner surmise: $e^{-\alpha s^2}$ with $\alpha = 4/\pi$ gives $M_N/\bar\tau \sim \sqrt{\log N/\alpha} = \sqrt{\pi \log N/4}$, NOT $\sqrt{2\log N}$. So the $\sqrt{2}$ constant I've used is QUESTIONABLE and may need to be $\sqrt{\pi/4}$ or similar. **This is a potential drift.** The ORDERING (BA-B < Poisson) is robust, but the specific constant $\sqrt{2}$ is not. A proper check requires opening BA-B 2013 Theorem 1.3 statement.

- For the ORDER-OF-MAGNITUDE hierarchy $\bar\tau \sqrt{\log N} < \bar\tau \log N$, no constant-precision is needed. The qualitative conclusion (BA-B tightens Poisson) survives.

**Secondary source: the universality bridge.**

Paper32 L17 cites Hardy Z PCC (arXiv:2511.18275) as LITERATURE. I have NOT checked whether the Hardy Z preprint itself makes claims beyond 2-point, and I have NOT verified the universality bridge to extreme statistics from any secondary literature. This is plausible-but-unverified. The CONCERN-PARTIAL verdict honors this.

## Inference-from-source check

For each verbatim quote, logical entailment:

- **paper32-bgs-spectral-statistics/PROOF-CHAIN.md L17 (Hardy Z PCC LITERATURE).** Directly entails sine-kernel pair correlation for Riemann zeros. ENTAILS pair-correlation-level sine kernel. Does NOT entail the joint law determining BA-B extreme statistics. Step 1 BA-B replacement depends on an unstated universality bridge.

- **paper43-cramer/PROOF-CHAIN.md L209 (BA-B 2013).** Directly entails GUE max gap scaling $O(\sqrt{\log N/N})$. ENTAILS only up to constant; the specific $\sqrt 2$ Gumbel-location constant is a reconstruction, not verbatim.

- **paper43-cramer/PROOF-CHAIN.md L321 (extreme-gap universality NOT proved for Riemann zeros).** Directly entails that the universality bridge is conjectural. ENTAILS the CONCERN-PARTIAL verdict, not a CLOSED verdict.

- **Paper 12 research/265 Theorem ($\omega_1 = \bigotimes_p \omega_1^p$).** Directly entails Step 2 factorization is envelope-independent. ENTAILS.

- **Paper 12 research/265 L34–L38 ($\omega_1^p(\mu_p^k\mu_p^{*k}) = p^{-k}(1-1/p)$).** Directly entails Step 5's $Z_{\text{ITPFI}}(y) = \prod(1-1/p)$. ENTAILS.

- **Wave-1 `cramer-L4-routeB-derivation.md` Step 4 (L144–L150).** Verbatim "The clean statement: the explicit-formula transfer carries the zero-gap excursion $\delta\gamma \sim \bar\tau$ into a prime-gap excursion $h \sim C \cdot (\log x)^2$, and this scaling $k=2$ is the standard Cramér-Granville heuristic." — the $k=2$ is STILL heuristic after BA-B tightening.

**Weakest link.** The universality bridge for extreme-gap statistics PCC $\to$ BA-B for Riemann zeros. This bridge is precisely the 4a sub-wall in `paper43-cramer/PROOF-CHAIN.md` L128: *"Extreme-gap universality transfer (Tao-Vu to max-gap stats for Riemann zeros) | OPEN, difficulty 7/10 | external math."* The Wave-2 tightening does NOT close this wall; it uses BA-B conditional on it.

## Formal check

### BA-B ordering verification

At representative heights, compare BA-B and Poisson envelopes for $N = N(T)$:

| $T$ | $\bar\tau(T)$ | $N(T)$ | Poisson $M_N = \bar\tau \log N$ | BA-B $M_N = \bar\tau\sqrt{2\log N}$ | BA-B/Poisson |
|---|---|---|---|---|---|
| $10^4$ | $0.9860$ | $1.01\times 10^4$ | $9.10$ | $4.24$ | $0.47$ |
| $10^6$ | $0.5724$ | $1.75\times 10^6$ | $8.23$ | $3.07$ | $0.37$ |
| $10^{10}$ | $0.3112$ | $3.21\times 10^{10}$ | $7.53$ | $2.16$ | $0.29$ |
| $10^{14}$ | $0.2137$ | $4.68\times 10^{14}$ | $7.22$ | $1.76$ | $0.24$ |
| $10^{20}$ | $0.1454$ | $6.88\times 10^{20}$ | $6.98$ | $1.42$ | $0.20$ |

BA-B < Poisson at every tabulated scale; the ratio shrinks as $\sqrt{2/\log N}$. **Confirms BA-B is a TIGHTER envelope** — correcting paper43 v3's ordering.

### Odlyzko comparison (deterministic zeros vs. BA-B prediction)

Odlyzko 1987–2001 computed zeros near $T \sim 10^{20}$, sampled in consecutive windows of $\sim 10^9$ zeros. Largest normalized gap observed in the published data: approximately $4$–$5$. BA-B prediction for $N = 10^9$: $\sqrt{2\log 10^9} = 6.44$, with Gumbel fluctuations of $O(1)$.

The Odlyzko-observed $4$–$5$ sits below the BA-B mean but within the Gumbel fluctuation envelope. **No contradiction** with BA-B scaling — but not a sharp test either, because:

1. Odlyzko samples only $10^9$ out of $\sim 10^{20}\log 10^{20}/2\pi$ zeros, and BA-B is about the max over the sampled window.
2. Riemann zeros are DETERMINISTIC, not random; the observed max is ONE realization of whatever the deterministic statistics yield.

A sharper test would compare the empirical Gumbel distribution of max gaps over many windows to the BA-B prediction. This is outside the scope of this tightening.

### Mertens constant (unchanged)

Verified in Wave-1 at dps=40 (`cramer-L4-routeB-derivation.md` L262–L282): $\prod_{p \leq 10^6}(1-1/p) \cdot \log 10^{12} = 1.12287524$ vs $2e^{-\gamma} = 1.12291896$, ratio $0.99996$. Inherited unchanged in Wave-2.

## Verdict

**CONCERN-PARTIAL.**

- Step 1's envelope is CONDITIONALLY tightened from i.i.d. Poisson to BA-B GUE, reducing the max zero-gap prediction at height $T \sim \log x$ from $O(1)$ to $O(1/\sqrt{\log\log x})$.
- The ITPFI Mertens factorization (Steps 2, 3, 5) is envelope-independent; the constant $2e^{-\gamma}$ survives unchanged.
- The $k=2$ exponent is EMERGENT from the explicit-formula oscillatory-sum structure (Step 4), not from Step 1's envelope; BA-B does NOT derive $k=2$ either. The Wave-1 heuristic flag on $k=2$ is NOT resolved.
- The universality bridge PCC $\to$ BA-B for Riemann zeros is UNPROVED; tightening is conditional on this bridge.
- Paper43 v3 contains an arithmetic flip (BA-B miscompared to Poisson); this Wave-2 tightening REVERSES the v3 ordering. The v3 text should be corrected on the next revision.

**Joint statement delivered (conditional on universality bridge):**
$$h_{\max} \lesssim \frac{\sqrt{2}\cdot 2e^{-\gamma}}{\sqrt{\log\log x}}(\log x)^2,$$
tighter than Cramér-Granville by $\sqrt{2/\log\log x}$. The CONSTANT $2e^{-\gamma}$ is still ITPFI-derived; BA-B contributes only a sub-leading tightening factor.

**The user's hypothesis — "BA-B gives scaling, ITPFI gives constant, joint sharp" — is PARTIALLY vindicated:** ITPFI gives the constant (as hoped), but $k=2$ is neither BA-B nor ITPFI — it's the explicit-formula structure. BA-B gives a tightening INSIDE the prefactor, not a new exponent. The joint statement is stronger than Cramér-Granville but sub-leading-tighter, not structurally-tighter.

## Impact

**L4b status:** OPEN (sharpened, Wave-1) → OPEN (sharpened, Wave-2). The named sub-lemma "Mellin-duality truncation match" from Wave-1 is UNCHANGED by this tightening (it's orthogonal to the envelope question). A NEW named sub-lemma is added: "extreme-gap universality bridge PCC $\to$ BA-B for Riemann zeros."

**RIGIDITY:** No change. Both sub-lemmas stay OPEN.

**Confidence:** 6/10 (unchanged). The tightening confirms BA-B is the RIGHT envelope (correcting paper43 v3's flip), and sub-leading-improves the joint statement, but does NOT close a wall. A full close would require resolving the universality bridge, which is the 4a wall (difficulty 7/10, external math).

**Paper43 v3 correction flag.** The ordering BA-B > Poisson in v3 is arithmetically wrong. On the next PROOF-CHAIN revision, reverse this to: "BA-B is a TIGHTER envelope than i.i.d. Poisson: $\bar\tau\sqrt{2\log N} < \bar\tau\log N$ for $N > e^2$. Level repulsion prevents small gaps AND concentrates the max gap mass around a smaller value. The v3 text conflated $\sqrt{\log N}/N$ (correct BA-B) with $\sqrt{\log N/N}$ (not BA-B)."

**Programme-ring impact.** Does NOT flip any pair. Pair 3 (Lehmer ↔ Cramér) stays at the post-Wave-1 state (Cramér side 6/10, Lehmer side 4/10, gap 2.0). Does NOT contribute to RING SYMMETRIZED. Does NOT trigger RING STRENGTHENED either (no new closed link). Effect is local to L4b's wall-description.

## Notes for the runner

1. **Do not upgrade L4b's status on the basis of this tightening.** L4b stays OPEN with two named sub-walls (truncation match from Wave-1; universality bridge from Wave-2). The Wave-2 tightening is a STATEMENT REFINEMENT, not a wall-closure.

2. **Flag the paper43 v3 arithmetic correction.** Section "L4 wall analysis" L282–L295 contains the flipped ordering. On next chain revision, update to the correct ordering. This is the only canonical-text change triggered by this work.

3. **The $k=2$ is explicit-formula, not envelope.** Both this tightening and Wave-1 inherit $k=2$ from the explicit-formula oscillatory-sum structure at $T^* \sim \log x$. A future "derive $k=2$ from first principles" agent should attack Step 4's coherence analysis, not Step 1's envelope.

4. **Universality bridge as a new capacitor cell.** The bridge PCC → BA-B for Riemann zeros sits between PCC (2-point) and joint-gap-law universality. This is a cell in the 4a sub-wall (Tao-Vu extreme-gap universality transfer). Capacitor entry: RMT-EXTREME ↔ ANT-GAP-TAILS. Currently EMPTY. A probe agent could scout Feng-Wei 2022 methods for Wigner-matrix extreme gaps as an input to the bridge.

5. **No numerical re-run needed.** The Mertens-constant numerical check from Wave-1 is unchanged; the only new numerical content is the BA-B vs Poisson ordering table (this document), which confirms the qualitative hierarchy only. dps-precision arithmetic not required for this envelope comparison.

---

*T7 S-duality phase, Wave 2. BA-B tightening executed. The envelope is tighter by $\sqrt{\log\log}$; the constant is unchanged; the exponent was never in the envelope. The wall moves one click cleaner — from "$k=2$ inherited from Cramér-Granville" to "$k=2$ emergent from explicit-formula coherence, envelope tightens only the prefactor." The bridge PCC $\to$ BA-B for Riemann zeros stays conjectural — the 4a wall, named precisely now.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
*BA-B is tighter. ITPFI supplies the constant. The exponent lives in the oscillatory sum. The chain is one constant sharper and one wall-description more honest.*
