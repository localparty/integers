# Cycle 1: Resurgent Transseries and Median Resummation for H4

*ORA Author agent. Date: 2026-04-13.*
*Target: Can resurgent transseries methods circumvent the K-3 obstruction (IR renormalon at u = 2, Watson's theorem failure)?*
*Context: Step 18 of the YM proof chain. H4 = non-perturbative Schwinger functions agree with perturbation theory at short distances.*

---

## 0. Orientation

**K-3 recap.** The perturbative series for $\langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle$ in powers of $g^2$ is NOT Borel summable: the Borel transform $\hat{F}(u)$ has IR renormalon singularities at $u = 2, 3, 4, \ldots$ on the positive real axis ($u = n \cdot 2b_0^{-1}$ in the convention where $b_0 = 11N/(48\pi^2)$; here $u = 2$ means $u = 2/(2b_0) = 48\pi^2/(11N)$ in some normalizations -- see Section 1.1 for careful conventions). Watson's theorem fails because Balaban's (B1) gives disk analyticity $|g^2| < \rho$, not the sector analyticity $|\mathrm{arg}\,g^2| < \pi/2 + \epsilon$ that Watson requires.

**The resurgent idea.** Resurgence (Ecalle 1981) and median resummation are designed precisely for non-Borel-summable series with known singularity structure. If the full transseries is resurgent, the median resummation $S_{\mathrm{med}} = (S_+ + S_-)/2$ is unambiguous. If the Balaban non-perturbative construction equals $S_{\mathrm{med}}$, then H4 follows because $S_{\mathrm{med}}$ agrees with perturbation theory at leading order by construction.

**What this cycle investigates:** Whether this programme can be made rigorous for 4D SU(N) YM, and if not, what exactly blocks it.

---

## 1. Borel Plane Singularity Structure

### 1.1 Convention fixing

We use the standard Borel variable $u$ defined by the Borel transform of a series $\sum_n c_n g^{2n}$:

$$\hat{F}(u) = \sum_{n=0}^{\infty} \frac{c_n}{n!} u^n$$

with the Borel integral $F(g^2) = \int_0^\infty du\, e^{-u/g^2}\, \hat{F}(u)$.

For the correlator $\langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle$ with $|x| = r$ fixed:

**IR renormalons** (from chains of bubble diagrams with soft internal momenta):
$$u_{\mathrm{IR}}^{(n)} = \frac{2n}{b_0} = \frac{2n \cdot 48\pi^2}{11N}, \quad n = 1, 2, 3, \ldots$$

In the commonly used normalization where $b_0 \to \beta_0 = 11N/3$ (the one-loop beta function coefficient with $\alpha_s = g^2/(4\pi)$), the IR renormalon positions are $u = 2n/\beta_0$. For the $\mathrm{Tr}\,F^2$ correlator, the leading IR renormalon corresponds to a $\langle G^2\rangle / r^4$ power correction, sitting at:

$$u_{\mathrm{IR}}^{(1)} = 2 \quad (\text{in the normalization } u = n\beta_0 t)$$

This is the standard 't Hooft convention. The position is at an INTEGER, not fractional.

**UV renormalons** (from bubble chains with hard internal momenta):
$$u_{\mathrm{UV}}^{(n)} = -n, \quad n = 1, 2, 3, \ldots$$

These are on the NEGATIVE real axis and do not obstruct the Borel integral.

**Instanton--anti-instanton singularities** (from $I\bar{I}$ quasi-zero-mode integration):
$$u_{I\bar{I}} = 4 \quad (\text{corresponding to } e^{-2S_I} \text{ with } S_I = 8\pi^2/g^2)$$

in the normalization where the instanton action maps to $u = 2$... No. Let me be more careful. The instanton action $S_I = 8\pi^2/g^2$ maps to a singularity at $u = 2S_I \cdot b_0 = \ldots$ -- this depends on the normalization.

**Resolution:** In the 't Hooft normalization where $u = \beta_0 t$ and the Borel integral is $\int_0^\infty dt\, e^{-t/(b_0 g^2)}\hat{F}(t)$, the instanton singularity is at $t = S_I = 8\pi^2/g^2 \times g^2 = 8\pi^2$, hence $u = \beta_0 \cdot 8\pi^2 = (11N/3) \cdot 8\pi^2$. For $N = 3$: $u = 88\pi^2/3 \approx 289$. This is FAR from the leading IR renormalon at $u = 2$.

**Conclusion on conventions:** In the standard 't Hooft convention, the singularity structure of the Borel plane for the $\mathrm{Tr}\,F^2$ correlator is:

- IR renormalons: $u = 2, 3, 4, \ldots$ (positive real axis)
- UV renormalons: $u = -1, -2, -3, \ldots$ (negative real axis)
- Instanton--anti-instanton: $u = 4N\pi^2 \beta_0/3$ (far to the right)

The **leading obstruction** to Borel summability is the IR renormalon at $u = 2$. This is the K-3 kill.

### 1.2 Nature of the singularities

The IR renormalon at $u = 2$ is a branch point of the form:
$$\hat{F}(u) \sim \frac{K}{(2 - u)^{1 + \gamma_0}} \quad \text{as } u \to 2$$

where $\gamma_0$ is an anomalous dimension exponent. The singularity is NOT a simple pole -- it is a branch point with a specific exponent determined by the OPE and anomalous dimensions of the relevant dimension-4 condensate operator ($\langle G^2\rangle$).

The lateral Borel sums differ by the discontinuity across this branch cut:
$$S_+ - S_- = 2\pi i \cdot \mathrm{Disc}_{u=2}\hat{F}(u) \cdot e^{-2/(b_0 g^2)} \sim C \cdot \Lambda^4 / r^4$$

This ambiguity is of order $\Lambda^4/r^4$, which is the expected power correction from the gluon condensate.

---

## 2. The Resurgent Transseries Programme

### 2.1 General structure

The resurgent transseries for the correlator $G(r) = \langle \mathrm{Tr}\,F^2(x)\,\mathrm{Tr}\,F^2(0)\rangle$ at separation $|x| = r$ takes the form:

$$G(r; g^2) = \sum_{n \geq 0} \sigma_n \, e^{-n A / g^2} \, \Phi_n(g^2)$$

where:
- $A = 8\pi^2$ (instanton action)
- $\sigma_n$ are transseries parameters (determined by boundary conditions or the physical state)
- Each $\Phi_n(g^2) = \sum_{k=0}^\infty c_k^{(n)} g^{2k}$ is a formal power series (perturbative expansion around the $n$-instanton sector)

**Crucial distinction from K-3:** The transseries includes BOTH instanton sectors AND renormalon sectors. The renormalon contributions are at:

$$e^{-2n/(b_0 g^2)} \sim \Lambda^{2n}$$

These are NOT associated with semiclassical saddle points. In the transseries framework, they appear as additional non-perturbative sectors with actions $A_{\mathrm{ren}}^{(n)} = 2n/b_0$ (much smaller than the instanton action $A_I = 8\pi^2$).

The full transseries including renormalon sectors:
$$G(r; g^2) = \Phi_0(g^2) + \sum_{n=1}^\infty \tau_n \, e^{-2n/(b_0 g^2)} \, \Psi_n(g^2) + \sum_{m=1}^\infty \sigma_m \, e^{-m \cdot 8\pi^2/g^2} \, \Phi_m(g^2) + \cdots$$

where $\Psi_n$ are the renormalon sectors and $\Phi_m$ are the instanton sectors. (Mixed sectors also exist but are sub-leading.)

### 2.2 Median resummation

The median (or balanced) resummation is defined as:
$$S_{\mathrm{med}}[\Phi_0] = \frac{1}{2}(S_+ + S_-)[\Phi_0]$$

where $S_\pm$ are lateral Borel resummations (integrating above/below the real axis). For a resurgent transseries, $S_{\mathrm{med}}$ can be extended to the full transseries, and the result is UNAMBIGUOUS:

$$S_{\mathrm{med}}[\text{full transseries}] = \text{definite number}$$

This holds provided:
- (R1) The transseries is RESURGENT: the Stokes automorphisms relating $S_+$ and $S_-$ are computable from the alien derivatives, which are determined by the singularity structure of the Borel transform.
- (R2) The transseries parameters $\sigma_n, \tau_n$ are fixed by the Stokes constants (themselves determined by the alien derivatives) plus a physical boundary condition.
- (R3) The Stokes constants satisfy cancellation relations ensuring that the imaginary parts of all lateral Borel sums cancel when combined across sectors.

### 2.3 The key question reformulated

**Does $G^{\mathrm{NP}}(r) = S_{\mathrm{med}}[\text{YM transseries}]$?**

where $G^{\mathrm{NP}}$ is the non-perturbative Schwinger function constructed by the Balaban + gradient-flow programme (Steps 1-17).

If YES: Then H4 follows because $S_{\mathrm{med}}$ agrees with perturbation theory at leading order by construction. Specifically:

$$S_{\mathrm{med}}[\text{full transseries}] = \text{Borel sum of } \Phi_0 + \text{exponentially small corrections}$$

and the Borel sum of $\Phi_0$ IS the perturbative prediction. The short-distance behavior $G \sim C_N |x|^{-8} (\log)^{-2}$ comes from the perturbative sector $\Phi_0$, and the non-perturbative corrections are suppressed by $e^{-2/(b_0 g^2(1/r))} \sim (\Lambda r)^{2/b_0} \to 0$ as $r \to 0$.

---

## 3. Rigorous Status of Resurgence in QFT

### 3.1 What is proved

**(A) Finite-dimensional integrals and ODEs.** Resurgence is rigorously established for:
- Solutions of linear and nonlinear ODEs with irregular singular points (Ecalle 1981, Costin 1998, Costin-Costin 2001). Costin's work gives the strongest results: the median resummation of a resurgent transseries converges to the unique solution of the ODE satisfying specified boundary conditions.
- Finite-dimensional oscillatory integrals (saddle-point expansions). Howls (1997), Berry-Howls (1991).
- **Status: RIGOROUS MATHEMATICAL THEOREMS.**

**(B) Matrix models.** Resurgence proved for:
- Hermitian one-matrix models (Marino 2008, Aniceto-Schiappa 2014). The free energy and correlators are resurgent transseries, and the median resummation reproduces the exact answer from orthogonal polynomials.
- Multi-matrix models and topological strings (Couso-Santamaria, Edelstein, Schiappa, Vonk 2014-2016). Resurgence verified to very high perturbative order (hundreds of terms).
- **Status: PROVED for specific models; verification (not proof) for others.**

**(C) Quantum mechanics.** Resurgence proved for:
- The double-well potential: the transseries with instanton--anti-instanton sectors is resurgent, and the median resummation reproduces the exact energy levels (Zinn-Justin 1981, Jentschura-Soff 2001, Dunne-Unsal 2014).
- The periodic cosine potential (Mathieu equation): complete resurgent structure established (Dunne-Unsal 2014, Basar-Dunne 2015).
- **Status: PROVED (these are special cases of (A) above, being 1D QFTs = ODEs).**

**(D) 2D QFTs.**
- **Deformed CP^{N-1} model**: Resurgence proved for $N = 2$ on $\mathbb{R} \times S^1$ with $\mathbb{Z}_N$-twisted boundary conditions. The fractional instantons (bions) cancel the perturbative ambiguities (Dunne-Unsal 2012, 2013). **PROVED for N=2.**
- **Undeformed CP^{N-1}**: Resurgent structure conjectured, verified numerically to high order (Dunne-Unsal 2015), but NOT proved. The adiabatic continuity conjecture (connecting deformed to undeformed) is OPEN for $N \geq 3$.
- **Principal chiral model**: Resurgence verified numerically (Cherman-Dorigoni-Unsal 2015), not proved.
- **Status: PROVED only for deformed models with N=2; CONJECTURED for undeformed models.**

**(E) 4D gauge theories.**
- **$\mathcal{N} = 2$ SYM**: The Nekrasov partition function is a convergent series (not asymptotic), so Borel summability is trivial. However, the instanton-counting function has a resurgent structure when expanded in the Omega-background parameter (Aniceto-Basar-Schiappa 2019). Supersymmetry provides extreme analytical control.
- **$\mathcal{N} = 1$ SYM**: Some resurgence results via the NSVZ exact beta function. Not directly relevant to pure YM.
- **Pure 4D YM**: NO resurgence results, even conjectural, that go beyond the generic large-order relations known since 't Hooft (1977) and Lipatov (1977).
- **Status: NOTHING RIGOROUS for pure 4D YM.**

### 3.2 The gap between 2D and 4D

The critical obstruction to extending resurgence from 2D to 4D YM:

**(G1) Identification of non-perturbative saddle points for renormalons.** In 2D CP^{N-1} (deformed), the non-perturbative sectors are identified with specific semiclassical objects: fractional instantons (bions). Their actions are $S_{\mathrm{bion}} = 2S_I/N$, and the Stokes constants are computable from the one-loop determinant around the bion background.

In 4D YM, the IR renormalon at $u = 2$ does NOT correspond to any known semiclassical saddle point. The objects proposed to cancel renormalon ambiguities (center vortices, monopoles, domain walls) are:
- Not semiclassical (their existence requires strong-coupling dynamics)
- Not computable (their contributions cannot be evaluated in closed form)
- Not unique (multiple candidate objects exist with no selection principle)

**This is the fundamental obstacle.** Without identifying the non-perturbative saddle points, one cannot compute the Stokes constants, and without the Stokes constants, one cannot perform median resummation.

**(G2) Non-perturbative definition of the transseries parameter.** The transseries parameter $\sigma$ (or $\tau$ for renormalon sectors) must be fixed by a physical boundary condition. In quantum mechanics, this is the requirement that the wavefunction be normalizable. In 2D QFT on $S^1$, it is the periodic boundary condition. In 4D YM on $\mathbb{R}^4$, the appropriate boundary condition (defining the vacuum state) does not straightforwardly fix the transseries parameters because the path integral over all field configurations does not decompose into well-defined topological sectors for $k = 0$ fluctuations.

**(G3) Rigorous Borel transform analysis.** Even if the singularity structure of $\hat{F}(u)$ is KNOWN (IR renormalons at $u = 2, 3, \ldots$, instanton singularities far to the right), proving resurgence requires showing that the alien derivatives at each singularity are PRECISELY determined by lower-order sectors. This is a statement about ALL-ORDERS relations between perturbative coefficients, which has not been established for any 4D gauge theory.

---

## 4. Can the Balaban Construction Help?

### 4.1 What Balaban provides

The Balaban construction gives:
- A well-defined non-perturbative Schwinger function $G^{\mathrm{NP}}(r)$ for each $r > 0$ and $g^2 > 0$ small.
- Exponential decay bounds: $|K_k(X, V)| \leq e^{-\kappa |X|}$ for polymer activities.
- Analyticity in the field variables $V$ with $k$-independent radius $\rho > 0$.
- The RG recursion: $g_k^2 \to 0$ as $k \to \infty$ (asymptotic freedom).

### 4.2 What Balaban does NOT provide

- Analyticity of expectation values in $g^2$ (or $g_k^2$). The Boltzmann weight $e^{-S/g^2}$ has an essential singularity at $g = 0$.
- A decomposition of $G^{\mathrm{NP}}$ into perturbative + non-perturbative sectors.
- Any relationship between $G^{\mathrm{NP}}$ and a Borel (or median Borel) resummation.

### 4.3 The median resummation identification: what would be needed

To prove $G^{\mathrm{NP}} = S_{\mathrm{med}}[\text{transseries}]$, one would need:

**(N1)** Construct the transseries: identify ALL non-perturbative sectors, compute the Stokes constants at each Borel-plane singularity, verify the resurgence relations to all orders. This is currently open even at the conjectural level for pure 4D YM.

**(N2)** Show that $S_{\mathrm{med}}$ applied to this transseries is well-defined (convergent). This requires bounds on the growth of transseries coefficients across sectors, which is not established.

**(N3)** Prove uniqueness: the Balaban construction is the ONLY non-perturbative realization of the theory (in the sense of satisfying OS axioms + asymptotic freedom). This would force any correct resummation to agree with Balaban.

**(N3) is perhaps the most interesting.** If one could prove that the median resummation of the YM transseries (assuming it is well-defined) satisfies the OS axioms, then by the uniqueness of the Wightman reconstruction, it must agree with the Balaban construction. This would close H4.

**But (N3) reverses the usual logic:** instead of using resurgence to prove properties of the theory, it would use properties of the theory to constrain resurgence. And the OS axioms for the median resummation are precisely what cannot be established (cf. path-B-resurgence/05-obstacles-and-ideas.md Section II.3: reflection positivity for the resurgent sum is OPEN).

### 4.4 The effective-theory angle (from the construction run)

The construction run (05-construction-verdict.md) identified a potentially simpler argument: the Balaban effective action at scale $k$ has a convergent perturbative expansion in the effective coupling $g_k^2$ (within the analyticity disk for the field variables, via composition of analytic operations). The construction verdict's self-criticism correctly noted that this is analyticity in $V$ (field variables), not in $g_k^2$, and that the matching between $g_{\mathrm{GF}}^2(t)$ and $g_k$ proceeds via polymer bounds + Reisz, NOT via analyticity in $g_k$.

**Connection to resurgence:** If the effective perturbation theory at scale $k$ (in $g_k^2$) converges, then the resurgence/renormalon problem is ABSENT at the effective-theory level. The IR renormalon problem arises in the bare perturbative series (in $g_0^2$), which tries to capture ALL scales simultaneously. The Balaban multi-scale decomposition resolves each scale separately, and at each scale the perturbative expansion converges (the polymer expansion IS the convergent perturbative expansion at that scale).

**However:** "The polymer expansion converges" is a statement about convergence in the spatial cluster variable $X$, not necessarily about convergence in the coupling $g_k^2$. The polymer activity $K_k(X, V)$ depends on $g_k$ through the Boltzmann weight, and the analyticity in $V$ does not automatically imply that the $g_k$-expansion of $K_k$ converges.

**This is precisely the Balaban polymer perturbative content question** identified by the excision run (05-excision-verdict.md) as the most promising remaining direction (difficulty 8/10).

---

## 5. Assessment of the Resurgent Route to H4

### 5.1 What would constitute a complete argument

A complete resurgent closure of H4 would require:

**Step A.** Prove that the perturbative series for $\langle \mathrm{Tr}\,F^2\,\mathrm{Tr}\,F^2\rangle$ generates a RESURGENT transseries. This means: the Borel transform $\hat{F}(u)$ has only isolated singularities (branch points) at the known locations ($u = 2, 3, \ldots$ and $u = -1, -2, \ldots$ and instanton positions), and the alien derivatives at each singularity are computable in terms of the other sectors.

**Step B.** Identify the non-perturbative saddle points responsible for each renormalon singularity. For the leading IR renormalon at $u = 2$, this means finding the semiclassical (or non-semiclassical) configuration whose contribution cancels the ambiguity of order $\Lambda^4/r^4$.

**Step C.** Perform the median resummation and prove it converges to a function satisfying the OS axioms.

**Step D.** Prove uniqueness (the Balaban construction is the unique OS-axiom-satisfying QFT with the given gauge group and asymptotic freedom) and conclude $G^{\mathrm{NP}} = S_{\mathrm{med}}$.

### 5.2 Where this programme is blocked

| Step | Status | Obstacle |
|------|--------|----------|
| A | OPEN | No proof of resurgence for any 4D gauge theory perturbative series. Known only conjecturally from large-order analysis ('t Hooft, Lipatov). |
| B | OPEN | IR renormalon saddle points in 4D YM are UNIDENTIFIED. This is a 40-year-old open problem (Parisi 1978, Mueller 1985, Beneke 1999). The KK theory on CP^{N-1} provides candidate objects (Bogomolny instantons on the internal space), but the connection to renormalon cancellation has not been worked out (cf. path-B-resurgence/03-4d-extension.md Section II.3). |
| C | OPEN | Even in models where resurgence IS proved (quantum mechanics, matrix models), proving OS axioms for the resummed answer is non-trivial. Reflection positivity for median resummation is UNKNOWN in any QFT context. |
| D | OPEN | Uniqueness of 4D YM satisfying OS axioms + AF is itself an open problem (it is essentially the Jaffe-Witten problem). |

**All four steps are blocked.** No single step is close to closure.

### 5.3 Is there a shortcut?

**Shortcut attempt 1:** Skip Steps A-C by arguing that the Balaban construction's polymer expansion IS the resurgent transseries (just reorganized). Then $G^{\mathrm{NP}} = S_{\mathrm{med}}$ would be tautological.

**Problem:** The Balaban polymer expansion is an expansion in spatial clusters $X$ with exponentially decaying activities $K_k(X, V)$. It is NOT organized as an expansion in non-perturbative sectors $e^{-nA/g^2}$. To connect the two, one would need to show that the polymer activities decompose into perturbative and non-perturbative parts -- which is the Balaban polymer perturbative content question (difficulty 8/10).

**Shortcut attempt 2:** Use the gradient-flow construction to define a DIFFERENT resummation. The gradient-flow coupling $g_{\mathrm{GF}}^2(t)$ is a well-defined non-perturbative observable at each $t > 0$. Its small-$t$ expansion is a convergent series in $t$ (Lemma L.3.7). Use this convergent expansion instead of the divergent $g^2$ expansion.

**Problem:** This is exactly the t-expansion vs g^2-expansion distinction (Card 16 from the excision run). The convergent $t$-expansion gives the non-perturbative $G^{\mathrm{NP}}(r)$ as a definite number. But H4 asks whether this number agrees with the perturbative prediction (a computation in powers of $g^2$). The convergent $t$-expansion does not interface with the perturbative $g^2$-expansion.

**Shortcut attempt 3:** Prove H4 at LEADING ORDER only. The median resummation agrees with the perturbative prediction at leading order (tree level) by construction. At tree level, $\langle \mathrm{Tr}\,F^2\,\mathrm{Tr}\,F^2\rangle \sim |x|^{-8}$. The (log)^{-2} correction is one-loop. Could one prove that the one-loop matching holds using the Balaban RG recursion?

**This is essentially the Step 18' argument from the construction run.** The Balaban RG gives $g_k \to 0$ (unconditional). The matching $g_{\mathrm{GF}}^2(t) = g_k^2[1 + O(g_k^2)]$ via polymer bounds + Reisz gives the one-loop correction. The trace anomaly then gives the $(log)^{-2}$. This does NOT use resurgence at all -- it is the construction-run argument.

**Conclusion on shortcuts:** The only viable shortcut is the construction-run Step 18', which bypasses both H4 and resurgence by working entirely within the Balaban effective-theory framework.

---

## 6. Comparison with the Construction Run's Step 18'

The construction run (05-construction-verdict.md) produced a candidate unconditional replacement for Step 18 that works as follows:

1. Balaban RG: $g_k \to 0$ (unconditional).
2. Polymer bounds + Reisz matching: $g_{\mathrm{GF}}^2(t) = g_k^2[1 + O(g_k^2) + O(e^{-\kappa})]$ at $t \sim a_k^2$.
3. Trace anomaly + Callan-Symanzik: $S_2^{\mathrm{ren}} \sim |x|^{-8}(\log)^{-2}$.

**This argument does NOT require:**
- Borel summability of the bare perturbative series
- Resurgence of the transseries
- Identification of renormalon saddle points
- Median resummation
- Watson's theorem or sector analyticity

**It works because it avoids the bare perturbative series entirely**, instead matching the non-perturbative gradient-flow coupling to the Balaban running coupling at each RG scale separately.

**The resurgent route, by contrast, tries to match the non-perturbative answer to a GLOBAL resummation of the bare perturbative series** -- a much harder problem that requires control of all non-perturbative sectors simultaneously.

### 6.1 Does the resurgent route add anything beyond Step 18'?

If Step 18' survives critic verification, the resurgent route is UNNECESSARY for H4. However, resurgence could still provide:

- **Higher-order corrections:** Step 18' gives the LEADING AF behavior $\sim (\log)^{-2}$. Resurgence would in principle give ALL power corrections $\sim \Lambda^{2n}/r^{2n}$ (the full OPE). But these are not needed for Step 18 of the proof chain.

- **The full OPE:** L.4 (leading-order OPE) would be UPGRADED from leading-order to all orders if resurgence held. But this is beyond what the proof chain requires.

- **Conceptual clarity:** The resurgent transseries makes the non-perturbative structure transparent (instantons, renormalons, their cancellations). Step 18' is more prosaic: it just says "the RG coupling goes to zero, so at short distances perturbation theory suffices."

---

## 7. Verdict

### 7.1 Can resurgent transseries methods circumvent the K-3 obstruction?

**NO -- not with current rigorous technology.**

The obstacles are:
1. **(G1)** No identification of IR renormalon saddle points in 4D YM.
2. **(G2)** No proof of resurgence for any 4D gauge theory perturbative series.
3. **(G3)** No proof that median resummation preserves OS axioms (reflection positivity).
4. **(G4)** No uniqueness theorem connecting the Balaban construction to any specific resummation scheme.

Each of (G1)-(G4) is a MAJOR open problem. Their conjunction makes the resurgent route to H4 blocked at difficulty 10/10.

### 7.2 Classification

**STATUS: BLOCKED (not killed).**

The resurgent route is not KILLED (like K-1 through K-4) because it is not logically impossible -- it is conceivable that all four obstacles could be overcome. It is BLOCKED because no current technique can overcome any of them.

**Distinction from K-3:** K-3 killed the specific approach "Borel summability + Watson's theorem." The resurgent route circumvents Watson's theorem (by using median resummation instead of standard Borel summation) but introduces new difficulties (G1)-(G4) that are equally severe.

### 7.3 Re-entry gate

The resurgent route reopens if ANY of the following become available:
1. A rigorous proof of resurgence for the 2D undeformed CP^{N-1} model (extending Dunne-Unsal from N=2 deformed to general N undeformed), PLUS the worldsheet connection to 4D (from path-B-resurgence/03-4d-extension.md).
2. Identification of the semiclassical objects responsible for IR renormalon cancellation in 4D SU(N) YM.
3. A proof that the Balaban polymer expansion generates a resurgent transseries when re-expanded in the bare coupling.

### 7.4 Recommendation

**Deprioritize the resurgent route for H4.** The construction run's Step 18' (Balaban RG + polymer bounds + Reisz matching + trace anomaly) is a strictly simpler path to the same conclusion and does not require any resurgence machinery. Direct effort toward VERIFYING Step 18' (posing it to an independent critic) rather than pursuing the resurgent programme.

The resurgent programme remains valuable for PHYSICS (computing power corrections, understanding the OPE, connecting to lattice QCD) but is not the right tool for the MATHEMATICAL closure of H4.

---

## 8. Cards for the Capacitor

| Card # | Name | Content |
|--------|------|---------|
| C1-1 | Resurgent route to H4: BLOCKED | The resurgent transseries + median resummation approach circumvents K-3's Watson's theorem failure but introduces four new obstacles (G1-G4): unidentified renormalon saddles, unproved resurgence, unknown OS-axiom preservation, no uniqueness bridge to Balaban. All are major open problems. Difficulty: 10/10. |
| C1-2 | Step 18' supersedes resurgence for H4 | The construction run's Step 18' (Balaban RG + polymer bounds + Reisz + trace anomaly) achieves the same AF match without any resurgence machinery. Step 18' works at each RG scale separately; the resurgent route tries to resum all scales at once. The former is unconditional (pending critic verification); the latter requires multiple open problems to be solved. |
| C1-3 | Renormalon positions are integers | In the 't Hooft convention for the $\mathrm{Tr}\,F^2$ correlator: IR renormalons at $u = 2, 3, 4, \ldots$ (integers, not fractional). UV renormalons at $u = -1, -2, \ldots$. Instanton singularities at $u \gg 1$ (order $N \cdot \pi^2$). The leading obstruction is always the IR renormalon at $u = 2$. |

---

*End of Cycle 1. Next action: submit Step 18' to independent critic for verification.*
